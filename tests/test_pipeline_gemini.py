"""Tests for src.pipeline._gemini — rate limiter, model cascade, client factory."""

from __future__ import annotations

import time
from unittest.mock import MagicMock, patch

import pytest

from src.pipeline._gemini import (
    _FALLBACK_CASCADE,
    _MODEL_CASCADE,
    _HeaderCapturingClient,
    _model_sort_key,
    _ModelCascade,
    _parse_reset_seconds,
    _RateLimiter,
    build_model_cascade,
)

# ---------------------------------------------------------------------------
# _parse_reset_seconds
# ---------------------------------------------------------------------------


class TestParseResetSeconds:
    def test_bare_float(self) -> None:
        assert _parse_reset_seconds("60") == 60.0

    def test_seconds_suffix(self) -> None:
        assert _parse_reset_seconds("4s") == 4.0

    def test_empty_string(self) -> None:
        assert _parse_reset_seconds("") is None

    def test_whitespace(self) -> None:
        assert _parse_reset_seconds("  ") is None

    def test_unparseable(self) -> None:
        assert _parse_reset_seconds("soon") is None

    def test_negative_clamped_to_zero(self) -> None:
        assert _parse_reset_seconds("-5") == 0.0

    def test_iso8601_past_date(self) -> None:
        # A timestamp in the distant past should give 0.0 (clamped).
        result = _parse_reset_seconds("2020-01-01T00:00:00Z")
        assert result == 0.0


# ---------------------------------------------------------------------------
# _HeaderCapturingClient
# ---------------------------------------------------------------------------


class TestHeaderCapturingClient:
    def test_captures_ratelimit_headers(self) -> None:
        client = _HeaderCapturingClient()
        mock_response = MagicMock()
        mock_response.headers = {
            "x-ratelimit-remaining-requests": "10",
            "content-type": "application/json",
        }
        with patch.object(client.__class__.__bases__[0], "send", return_value=mock_response):
            client.send(MagicMock())
        assert client.ratelimit_headers == {"x-ratelimit-remaining-requests": "10"}

    def test_ignores_non_ratelimit_headers(self) -> None:
        client = _HeaderCapturingClient()
        mock_response = MagicMock()
        mock_response.headers = {"content-type": "application/json"}
        with patch.object(client.__class__.__bases__[0], "send", return_value=mock_response):
            client.send(MagicMock())
        assert client.ratelimit_headers == {}


# ---------------------------------------------------------------------------
# _RateLimiter
# ---------------------------------------------------------------------------


class TestRateLimiter:
    def test_wait_respects_interval(self) -> None:
        limiter = _RateLimiter(rpm=60)  # 1s interval
        limiter._last = time.monotonic()
        # Immediately calling wait should sleep ~1s; we just check it calls sleep.
        with patch("src.pipeline._gemini.time.sleep") as mock_sleep:
            limiter.wait()
        mock_sleep.assert_called_once()
        gap = mock_sleep.call_args[0][0]
        assert gap > 0  # slept a positive duration

    def test_no_sleep_after_enough_time(self) -> None:
        limiter = _RateLimiter(rpm=60)
        limiter._last = time.monotonic() - 2.0  # 2s ago > 1s interval
        with patch("src.pipeline._gemini.time.sleep") as mock_sleep:
            limiter.wait()
        mock_sleep.assert_not_called()

    def test_slows_when_few_requests_remaining(self) -> None:
        http_client = _HeaderCapturingClient()
        http_client.ratelimit_headers = {"x-ratelimit-remaining-requests": "2"}
        limiter = _RateLimiter(rpm=60, http_client=http_client)
        limiter._last = time.monotonic()
        with patch("src.pipeline._gemini.time.sleep"):
            limiter.wait()
        assert limiter._interval >= 20.0  # tripled from 1s min, but clamped to 20s

    def test_waits_for_reset_when_exhausted(self) -> None:
        http_client = _HeaderCapturingClient()
        http_client.ratelimit_headers = {
            "x-ratelimit-remaining-requests": "0",
            "x-ratelimit-reset-requests": "30s",
        }
        limiter = _RateLimiter(rpm=60, http_client=http_client)
        limiter._last = time.monotonic()
        with patch("src.pipeline._gemini.time.sleep") as mock_sleep:
            limiter.wait()
        # The interval should now be 30s (the reset window).
        assert limiter._interval == 30.0
        mock_sleep.assert_called_once()


# ---------------------------------------------------------------------------
# _model_sort_key
# ---------------------------------------------------------------------------


class TestModelSortKey:
    def test_pro_before_flash(self) -> None:
        assert _model_sort_key("gemini-2.5-pro") < _model_sort_key("gemini-2.5-flash")

    def test_flash_before_flash_lite(self) -> None:
        assert _model_sort_key("gemini-2.5-flash") < _model_sort_key("gemini-2.5-flash-lite")

    def test_newer_version_first(self) -> None:
        # gemini-3 should sort before gemini-2.5 within the same tier
        assert _model_sort_key("gemini-3-flash") < _model_sort_key("gemini-2.5-flash")

    def test_stable_before_experimental(self) -> None:
        assert _model_sort_key("gemini-2.5-flash") < _model_sort_key("gemini-2.5-flash-preview")

    def test_flash_lite_not_claimed_by_flash(self) -> None:
        # flash-lite tier (2) must be strictly higher than flash tier (1)
        flash_tier = _model_sort_key("gemini-2.5-flash")[0]
        lite_tier = _model_sort_key("gemini-2.5-flash-lite")[0]
        assert lite_tier > flash_tier

    def test_unknown_model_sorted_last(self) -> None:
        assert _model_sort_key("some-unknown-model")[0] == 3

    def test_sort_produces_correct_order(self) -> None:
        models = [
            "gemini-2.5-flash-lite",
            "gemini-2.5-pro",
            "gemini-3-flash",
            "gemini-2.5-flash",
        ]
        models.sort(key=_model_sort_key)
        # Pro tier (0) always before Flash (1) regardless of version number.
        assert models == [
            "gemini-2.5-pro",
            "gemini-3-flash",
            "gemini-2.5-flash",
            "gemini-2.5-flash-lite",
        ]


# ---------------------------------------------------------------------------
# _ModelCascade
# ---------------------------------------------------------------------------


class TestModelCascade:
    def _make_cascade(self, models: list[str] | None = None) -> _ModelCascade:
        http_client = _HeaderCapturingClient()
        default_models = ["model-a", "model-b", "model-c"]
        return _ModelCascade(
            models=models or default_models,
            rpm=15,
            http_client=http_client,
        )

    def test_starts_at_first_model(self) -> None:
        cascade = self._make_cascade(["model-a", "model-b", "model-c"])
        assert cascade.model == "model-a"

    def test_advance_moves_to_next_model(self) -> None:
        cascade = self._make_cascade()
        ok = cascade.advance()
        assert ok
        assert cascade.model == "model-b"

    def test_all_exhausted_after_draining_cascade(self) -> None:
        cascade = self._make_cascade()
        for _ in range(len(cascade._models)):
            cascade.advance()
        assert cascade.all_exhausted

    def test_advance_returns_false_when_exhausted(self) -> None:
        cascade = self._make_cascade(["model-a"])
        ok = cascade.advance()
        assert not ok
        assert cascade.all_exhausted

    def test_check_daily_quota_header_zero(self) -> None:
        cascade = self._make_cascade()
        cascade._http_client.ratelimit_headers = {"x-ratelimit-remaining-requests-per-day": "0"}
        assert cascade.check_daily_quota_header() is True

    def test_check_daily_quota_header_nonzero(self) -> None:
        cascade = self._make_cascade()
        cascade._http_client.ratelimit_headers = {"x-ratelimit-remaining-requests-per-day": "100"}
        assert cascade.check_daily_quota_header() is False

    def test_fallback_cascade_alias(self) -> None:
        """_MODEL_CASCADE is an alias for _FALLBACK_CASCADE."""
        assert _MODEL_CASCADE is _FALLBACK_CASCADE

    def test_fallback_cascade_non_empty(self) -> None:
        assert len(_FALLBACK_CASCADE) > 0

    def test_fallback_cascade_order(self) -> None:
        """Fallback cascade must be sorted by tier+version (same as dynamic sort)."""
        sorted_copy = sorted(_FALLBACK_CASCADE, key=_model_sort_key)
        assert sorted_copy == _FALLBACK_CASCADE


# ---------------------------------------------------------------------------
# build_model_cascade
# ---------------------------------------------------------------------------


class TestBuildModelCascade:
    def _make_model_entry(self, name: str, methods: list[str] | None = None) -> dict:
        return {
            "name": f"models/{name}",
            "supportedGenerationMethods": methods if methods is not None else ["generateContent"],
        }

    def _mock_response(self, model_names: list[str]) -> MagicMock:
        resp = MagicMock()
        resp.json.return_value = {"models": [self._make_model_entry(n) for n in model_names]}
        resp.raise_for_status.return_value = None
        return resp

    def test_returns_fallback_on_network_error(self) -> None:
        with patch("src.pipeline._gemini.httpx.Client") as mock_cls:
            mock_cls.return_value.__enter__.return_value.get.side_effect = OSError("timeout")
            result = build_model_cascade("key", "gemini-2.5-flash-lite")
        # Falls back — result starts at the hint or uses the full fallback
        assert isinstance(result, list)
        assert len(result) > 0

    def test_sorts_pro_before_flash(self) -> None:
        with patch("src.pipeline._gemini.httpx.Client") as mock_cls:
            mock_cls.return_value.__enter__.return_value.get.return_value = self._mock_response(
                ["gemini-2.5-flash", "gemini-2.5-pro"]
            )
            result = build_model_cascade("key", "gemini-2.5-pro")
        assert result.index("gemini-2.5-pro") < result.index("gemini-2.5-flash")

    def test_sorts_flash_before_flash_lite(self) -> None:
        with patch("src.pipeline._gemini.httpx.Client") as mock_cls:
            mock_cls.return_value.__enter__.return_value.get.return_value = self._mock_response(
                ["gemini-2.5-flash-lite", "gemini-2.5-flash"]
            )
            result = build_model_cascade("key", "gemini-2.5-flash")
        assert result.index("gemini-2.5-flash") < result.index("gemini-2.5-flash-lite")

    def test_skips_non_generate_content_models(self) -> None:
        with patch("src.pipeline._gemini.httpx.Client") as mock_cls:
            mock_cls.return_value.__enter__.return_value.get.return_value = MagicMock(
                json=lambda: {
                    "models": [
                        self._make_model_entry("gemini-2.5-flash", ["embedContent"]),
                        self._make_model_entry("gemini-2.5-flash-lite", ["generateContent"]),
                    ]
                },
                raise_for_status=lambda: None,
            )
            result = build_model_cascade("key", "gemini-2.5-flash-lite")
        assert "gemini-2.5-flash" not in result
        assert "gemini-2.5-flash-lite" in result

    def test_skips_unversioned_models(self) -> None:
        with patch("src.pipeline._gemini.httpx.Client") as mock_cls:
            mock_cls.return_value.__enter__.return_value.get.return_value = MagicMock(
                json=lambda: {
                    "models": [
                        self._make_model_entry("gemini-pro"),  # legacy, no version
                        self._make_model_entry("gemini-2.5-flash"),
                    ]
                },
                raise_for_status=lambda: None,
            )
            result = build_model_cascade("key", "gemini-2.5-flash")
        assert "gemini-pro" not in result
        assert "gemini-2.5-flash" in result

    def test_returns_fallback_when_no_models(self) -> None:
        with patch("src.pipeline._gemini.httpx.Client") as mock_cls:
            mock_cls.return_value.__enter__.return_value.get.return_value = MagicMock(
                json=lambda: {"models": []},
                raise_for_status=lambda: None,
            )
            result = build_model_cascade("key", "gemini-2.5-flash-lite")
        assert isinstance(result, list)
        assert len(result) > 0

    def test_api_key_redacted_in_logs(self, caplog: pytest.LogCaptureFixture) -> None:
        import logging

        with (
            patch("src.pipeline._gemini.httpx.Client") as mock_cls,
            caplog.at_level(logging.WARNING, logger="src.pipeline._gemini"),
        ):
            mock_cls.return_value.__enter__.return_value.get.side_effect = OSError(
                "GET https://example.com?key=super-secret-key-123 failed"
            )
            build_model_cascade("super-secret-key-123", "gemini-2.5-flash-lite")
        assert "super-secret-key-123" not in caplog.text


# ---------------------------------------------------------------------------
# make_gemini_client — unit test (does not call network)
# ---------------------------------------------------------------------------


class TestMakeGeminiClient:
    def test_returns_client_and_http_client(self) -> None:
        mock_client = MagicMock()
        mock_genai = MagicMock()
        mock_genai.Client.return_value = mock_client
        mock_types = MagicMock()

        with (
            patch("src.pipeline._gemini._HeaderCapturingClient") as mock_hcc,
            patch.dict(
                "sys.modules",
                {
                    "google": MagicMock(genai=mock_genai),
                    "google.genai": mock_genai,
                    "google.genai.types": mock_types,
                },
            ),
        ):
            http_inst = MagicMock(spec=_HeaderCapturingClient)
            mock_hcc.return_value = http_inst
            # Import lazily after patching to pick up the mocked modules.
            from src.pipeline._gemini import make_gemini_client  # noqa: PLC0415

            client, http_client = make_gemini_client("test-key")

        assert http_client is http_inst
        # Client is whatever genai.Client() returns.
        assert client is not None

    @pytest.mark.integration
    def test_integration_list_models(self) -> None:
        """Verify the API key is valid and at least one model is reachable."""
        import os

        api_key = os.environ.get("GEMINI_API_KEY")
        if not api_key:
            pytest.skip("GEMINI_API_KEY not set")

        from src.pipeline._gemini import make_gemini_client

        client, _ = make_gemini_client(api_key)
        # List available models — just check we get a response.
        models = list(client.models.list())
        assert len(models) > 0
