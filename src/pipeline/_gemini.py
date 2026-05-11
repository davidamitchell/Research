"""Shared Gemini client factory used by the enrichment pipeline.

Ported from davidamitchell/Latest-developments- and adapted for the Research
repo's Markdown-based corpus.

Three concerns:

_HeaderCapturingClient — httpx.Client that records x-ratelimit-* response headers
_RateLimiter          — adaptive per-minute pacer driven by those headers
_ModelCascade         — walks through models in order as each model's daily quota
                        is exhausted

All code that calls the Gemini API should obtain a client via make_gemini_client()
so header capture is universal and rate-limit state is shared across calls.
"""

from __future__ import annotations

import logging
import time
from datetime import UTC, datetime

import httpx

logger = logging.getLogger(__name__)

# ---------------------------------------------------------------------------
# Model cascade
# ---------------------------------------------------------------------------

# Try newest models first; advance when a model's daily quota is exhausted.
# Each model has its own independent free-tier quota pool — never assume a
# single global RPM.  Unknown limits (gemini-3-*) default to 15 RPM; verify
# at aistudio.google.com before relying on those models for large backfills.
#
#   gemini-3-flash         — check aistudio.google.com for current limits
#   gemini-3.1-flash-lite  — check aistudio.google.com for current limits
#   gemini-2.5-flash-lite  30 RPM / 1 500 RPD — fastest; best throughput
#   gemini-2.0-flash       15 RPM / 1 500 RPD — high RPD; strong capability
#   gemini-2.5-flash       10 RPM /   500 RPD — strongest reasoning; lower RPD
_MODEL_CASCADE: list[str] = [
    "gemini-3-flash",
    "gemini-3.1-flash-lite",
    "gemini-2.5-flash-lite",
    "gemini-2.0-flash",
    "gemini-2.5-flash",
]

# Per-model RPM for the free tier.  Used by _ModelCascade to set the correct
# pacing interval when the rate limiter is reset on model advance.
# Conservative 15 RPM is used for models whose limits are not yet documented.
_MODEL_RATES: dict[str, int] = {
    "gemini-3-flash": 15,
    "gemini-3.1-flash-lite": 15,
    "gemini-2.5-flash-lite": 30,
    "gemini-2.0-flash": 15,
    "gemini-2.5-flash": 10,
}


# ---------------------------------------------------------------------------
# HTTP transport
# ---------------------------------------------------------------------------


class _HeaderCapturingClient(httpx.Client):
    """httpx.Client that records x-ratelimit-* headers after every response.

    Injected into genai.Client via HttpOptions(httpx_client=...) — a supported,
    documented hook — so all Gemini calls flow through it automatically.
    """

    def __init__(self, **kwargs: object) -> None:
        kwargs.setdefault("follow_redirects", True)
        super().__init__(**kwargs)  # type: ignore[arg-type]
        self.ratelimit_headers: dict[str, str] = {}

    def send(self, request: httpx.Request, **kwargs: object) -> httpx.Response:  # type: ignore[override]
        response = super().send(request, **kwargs)  # type: ignore[arg-type]
        self.ratelimit_headers = {
            k.lower(): v for k, v in response.headers.items() if k.lower().startswith("x-ratelimit")
        }
        return response


# ---------------------------------------------------------------------------
# Rate limiter
# ---------------------------------------------------------------------------


def _parse_reset_seconds(reset_str: str) -> float | None:
    """Parse x-ratelimit-reset-requests into seconds until reset.

    Handles: bare float ("60"), duration with suffix ("4s"), ISO-8601 timestamp.
    Returns None when the string is empty or unparseable.
    """
    s = reset_str.strip()
    if not s:
        return None
    if s.endswith("s"):
        try:
            return max(float(s[:-1]), 0.0)
        except ValueError:
            pass
    try:
        return max(float(s), 0.0)
    except ValueError:
        pass
    try:
        reset_dt = datetime.fromisoformat(s.replace("Z", "+00:00"))
        return max((reset_dt - datetime.now(UTC)).total_seconds(), 0.0)
    except (ValueError, OverflowError):
        pass
    return None


class _RateLimiter:
    """Adaptive per-minute pacer for Gemini API calls.

    Uses 60/rpm seconds as a minimum interval floor.  Before each wait() call,
    the captured x-ratelimit-remaining-requests header is inspected:

    - remaining == 0 → wait for the reset window (x-ratelimit-reset-requests)
    - remaining <= 3 → triple the interval to coast to the window boundary
    - remaining >  3 → restore the minimum interval

    When headers are absent (network error or mocked client in tests), the
    fixed interval is used unchanged.
    """

    def __init__(self, rpm: int = 15, http_client: _HeaderCapturingClient | None = None) -> None:
        self._min_interval = 60.0 / rpm
        self._interval = self._min_interval
        self._last: float = 0.0
        self._http_client = http_client

    def _update_from_headers(self, headers: dict[str, str]) -> None:
        remaining_str = headers.get("x-ratelimit-remaining-requests")
        if not remaining_str:
            return
        try:
            remaining = int(remaining_str)
        except ValueError:
            logger.debug(
                "Rate limiter: non-integer x-ratelimit-remaining-requests %r", remaining_str
            )
            return

        if remaining <= 0:
            reset_str = headers.get("x-ratelimit-reset-requests", "")
            wait = _parse_reset_seconds(reset_str) or 60.0
            logger.warning("Rate limiter: quota window exhausted — waiting %.1fs for reset", wait)
            self._interval = wait
        elif remaining <= 3:
            self._interval = max(self._min_interval * 3, 20.0)
            logger.debug(
                "Rate limiter: %d request(s) remaining — slowing to %.1fs interval",
                remaining,
                self._interval,
            )
        else:
            self._interval = self._min_interval

    def wait(self) -> None:
        if self._http_client and self._http_client.ratelimit_headers:
            self._update_from_headers(self._http_client.ratelimit_headers)
        now = time.monotonic()
        gap = self._interval - (now - self._last)
        if gap > 0:
            logger.debug("Rate limiter: waiting %.1fs before next Gemini call", gap)
            time.sleep(gap)
        self._last = time.monotonic()


# ---------------------------------------------------------------------------
# Model cascade
# ---------------------------------------------------------------------------


class _ModelCascade:
    """Walks through Gemini models in cascade order as each model's daily quota is exhausted.

    Starts at starting_model (must appear in _MODEL_CASCADE; treated as a sole
    option otherwise).  Each advance() resets the rate limiter so the new model
    gets a fresh pacing window.  The shared _HeaderCapturingClient is cleared of
    stale headers on advance so the new model's first response is read cleanly.

    Two triggers for advance():
    1. Quota-exhaustion exception from the caller
    2. check_daily_quota_header() — proactive: x-ratelimit-remaining-*-per-day == 0
    """

    def __init__(self, starting_model: str, rpm: int, http_client: _HeaderCapturingClient) -> None:
        try:
            idx = _MODEL_CASCADE.index(starting_model)
            self._models = _MODEL_CASCADE[idx:]
        except ValueError:
            self._models = [starting_model]
        self._idx = 0
        self._default_rpm = rpm  # fallback when model not in _MODEL_RATES
        self._http_client = http_client
        self._limiter = _RateLimiter(rpm=self._model_rpm(), http_client=http_client)

    def _model_rpm(self) -> int:
        """Return the documented RPM for the current model, or the default."""
        return _MODEL_RATES.get(self.model, self._default_rpm)

    @property
    def model(self) -> str:
        return self._models[min(self._idx, len(self._models) - 1)]

    @property
    def all_exhausted(self) -> bool:
        return self._idx >= len(self._models)

    def advance(self) -> bool:
        """Switch to the next model.  Returns True if one is available, False if done."""
        prev = self.model
        self._idx += 1
        if not self.all_exhausted:
            logger.warning("Quota exhausted for %r — switching to %r", prev, self.model)
            self._http_client.ratelimit_headers = {}
            self._limiter = _RateLimiter(rpm=self._model_rpm(), http_client=self._http_client)
            return True
        logger.error("All models in cascade exhausted — AI enrichment disabled for this run")
        return False

    def wait(self) -> None:
        self._limiter.wait()

    def check_daily_quota_header(self) -> bool:
        """Return True when response headers signal this model's daily allowance is zero."""
        headers = self._http_client.ratelimit_headers
        for key in (
            "x-ratelimit-remaining-requests-per-day",
            "x-ratelimit-remaining-tokens-per-day",
            "x-ratelimit-remaining-day",
        ):
            val = headers.get(key)
            if val is not None:
                try:
                    if int(val) <= 0:
                        return True
                except ValueError:
                    pass
        return False


# ---------------------------------------------------------------------------
# Client factory
# ---------------------------------------------------------------------------


def make_gemini_client(api_key: str) -> tuple[object, _HeaderCapturingClient]:
    """Construct a Gemini client wired to a header-capturing httpx transport.

    Returns (genai_client, http_client).  All callers should use this factory so
    every Gemini call captures x-ratelimit-* headers consistently.

    Pass http_client to _ModelCascade to enable adaptive pacing and quota
    detection.
    """
    from google import genai  # noqa: PLC0415
    from google.genai import types  # noqa: PLC0415

    http_client = _HeaderCapturingClient()
    client = genai.Client(
        api_key=api_key,
        http_options=types.HttpOptions(httpx_client=http_client),
    )
    return client, http_client
