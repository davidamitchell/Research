"""Shared Gemini client factory used by the enrichment pipeline.

Ported from davidamitchell/Latest-developments- and adapted for the Research
repo's Markdown-based corpus.

Four concerns:

_HeaderCapturingClient  — httpx.Client that records x-ratelimit-* response headers
_RateLimiter            — adaptive per-minute pacer driven by those headers
_ModelCascade           — walks through models in order as each model's DAILY QUOTA
                          is exhausted (RPM backoff is handled by _RateLimiter, not
                          by advancing the cascade)
build_model_cascade()   — queries ListModels at runtime to build the fully-sorted
                          cascade; never hard-codes or guesses model IDs

All code that makes Gemini API calls should obtain a client via make_gemini_client()
so header capture is universal and the rate-limit state is shared.
"""

from __future__ import annotations

import logging
import re
import time
from datetime import UTC, datetime

import httpx

logger = logging.getLogger(__name__)

# ---------------------------------------------------------------------------
# Model cascade — safe fallback used when ListModels cannot be reached
# ---------------------------------------------------------------------------
#
# build_model_cascade() queries the API and returns ALL available models sorted
# by tier (Pro → Flash → Flash-Lite) then by version (newest first).  This
# fallback is only used when the HTTP call fails.
#
# Cascade advances on DAILY QUOTA exhaustion only.  RPM rate-limiting is handled
# by _RateLimiter waiting for the x-ratelimit-reset-requests window.
#
# Verified free-tier limits (confirmed from 429 quotaValue fields, 2026-05-12):
#   gemini-2.5-flash-lite  10 RPM (NOT 30 — that is the paid tier)
#   gemini-2.5-flash       10 RPM (uses thinking tokens; ThinkingConfig needed)
#   gemini-2.0-flash       limit: 0 on free tier (cascade skips immediately)
_FALLBACK_CASCADE: list[str] = [
    "gemini-2.5-pro",
    "gemini-2.5-flash",
    "gemini-2.5-flash-lite",
]

# Kept for backwards compatibility with callers that import _MODEL_CASCADE.
_MODEL_CASCADE: list[str] = _FALLBACK_CASCADE


# ---------------------------------------------------------------------------
# Runtime model discovery
# ---------------------------------------------------------------------------


def _model_sort_key(model_id: str) -> tuple[int, int, int, int]:
    """Sort key implementing the desired cascade tier order.

    Tier 0 — Pro        (highest capability, lowest daily quota)
    Tier 1 — Flash      (balanced)
    Tier 2 — Flash-Lite (highest daily quota, lightest capability)
    Tier 3 — Unrecognised (sorted last)

    Within each tier: newest major.minor first, stable releases before
    experimental/preview variants.
    """
    if re.search(r"gemini-\d.*-flash-lite", model_id):
        tier = 2
    elif re.search(r"gemini-\d.*-flash", model_id):
        tier = 1
    elif re.search(r"gemini-\d.*-pro", model_id):
        tier = 0
    else:
        tier = 3

    m = re.match(r"gemini-(\d+)(?:\.(\d+))?", model_id)
    if not m:
        return (tier, 0, 0, 0)
    major = int(m.group(1))
    minor = int(m.group(2) or "0")
    is_experimental = 1 if re.search(r"preview|exp\b|experimental", model_id, re.IGNORECASE) else 0
    return (tier, -major, -minor, is_experimental)


def build_model_cascade(api_key: str, fallback_hint: str) -> list[str]:
    """Query ListModels and return the full ordered model cascade.

    Makes a direct REST call to the Gemini API — does not require a genai
    client to be created first.  Filters to versioned Pro and Flash models
    that support generateContent, then sorts by tier and version:

        Tier 0 — Pro     (gemini-X.Y-pro)          highest capability
        Tier 1 — Flash   (gemini-X.Y-flash)         balanced
        Tier 2 — Flash-Lite (gemini-X.Y-flash-lite) highest daily quota

    Within each tier: newest version first, stable before experimental.

    Falls back to _FALLBACK_CASCADE on any network or API error.  The
    API key is redacted from exception messages before logging.
    """
    url = f"https://generativelanguage.googleapis.com/v1beta/models?key={api_key}&pageSize=200"
    try:
        with httpx.Client(follow_redirects=True, timeout=15.0) as http:
            resp = http.get(url)
            resp.raise_for_status()
            data = resp.json()

        model_ids: list[str] = []
        for model in data.get("models", []):
            name: str = model.get("name", "")
            methods: list[str] = model.get("supportedGenerationMethods", [])
            if not name.startswith("models/"):
                continue
            model_id = name[len("models/") :]
            # Only versioned flash/pro models — exclude legacy IDs like "gemini-pro".
            if not re.match(r"gemini-\d+(?:\.\d+)?-(pro|flash)", model_id):
                continue
            if "generateContent" not in methods:
                continue
            # Exclude TTS variants — audio-only, reject TEXT output with 400 INVALID_ARGUMENT.
            if re.search(r"-tts\b", model_id):
                continue
            model_ids.append(model_id)

        if not model_ids:
            logger.warning("ListModels returned no usable models — using fallback cascade")
            return _build_fallback(fallback_hint)

        model_ids.sort(key=_model_sort_key)
        logger.info(
            "Available models (%d, sorted by tier+version): %s",
            len(model_ids),
            ", ".join(model_ids),
        )
        return model_ids

    except Exception as exc:
        # Redact API key before logging — httpx.HTTPStatusError includes the full
        # request URL (with ?key=...) in its __str__.
        safe_msg = re.sub(r"key=[^&\s]+", "key=***", str(exc))
        logger.warning("ListModels failed (%s) — using fallback cascade", safe_msg)
        return _build_fallback(fallback_hint)


def _build_fallback(starting_model: str) -> list[str]:
    if starting_model in _FALLBACK_CASCADE:
        idx = _FALLBACK_CASCADE.index(starting_model)
        return list(_FALLBACK_CASCADE[idx:])
    return [starting_model] + list(_FALLBACK_CASCADE)


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

    Uses 60/rpm seconds as a minimum interval floor.  Before each wait() call
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

    Initialise with the list returned by build_model_cascade() so actual API
    model IDs are used.  Each advance() resets the rate limiter so the new model
    gets a fresh pacing window and stale x-ratelimit-* headers are cleared.

    Two triggers for advance():
    1. Quota-exhaustion exception from the caller (429/403)
    2. check_daily_quota_header() — proactive: x-ratelimit-remaining-*-per-day == 0
    """

    def __init__(
        self,
        models: list[str],
        rpm: int,
        http_client: _HeaderCapturingClient,
    ) -> None:
        self._models = list(models) if models else list(_FALLBACK_CASCADE)
        self._idx = 0
        self._rpm = rpm
        self._http_client = http_client
        self._limiter = _RateLimiter(rpm=rpm, http_client=http_client)
        logger.info("Model cascade (%d models): %s", len(self._models), ", ".join(self._models))

    @property
    def model(self) -> str:
        return self._models[min(self._idx, len(self._models) - 1)]

    @property
    def all_exhausted(self) -> bool:
        return self._idx >= len(self._models)

    def advance(self) -> bool:
        """Switch to the next model.  Returns True if one is available, False if done."""
        if self.all_exhausted:
            return False
        prev = self.model
        self._idx += 1
        if not self.all_exhausted:
            logger.warning("Daily quota exhausted for %r — switching to %r", prev, self.model)
            self._http_client.ratelimit_headers = {}
            self._limiter = _RateLimiter(rpm=self._rpm, http_client=self._http_client)
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
