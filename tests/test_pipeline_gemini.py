"""Tests for src.pipeline._gemini — rate limiter, model cascade, client factory."""

from __future__ import annotations

import time
from unittest.mock import MagicMock, patch

import pytest

from src.pipeline._gemini import (
    _DESIRED_CASCADE,
    _MODEL_CASCADE,
    _MODEL_RATES,
    _HeaderCapturingClient,
    _ModelCascade,
    _parse_reset_seconds,
    _RateLimiter,
    resolve_cascade,
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
# _ModelCascade
# ---------------------------------------------------------------------------


class TestModelCascade:
    def _make_cascade(
        self,
        starting: str = "model-a",
        models: list[str] | None = None,
    ) -> _ModelCascade:
        http_client = _HeaderCapturingClient()
        default_models = ["model-a", "model-b", "model-c"]
        return _ModelCascade(
            starting, rpm=15, http_client=http_client, models=models or default_models
        )

    def test_starts_at_correct_model(self) -> None:
        cascade = self._make_cascade("model-b", models=["model-a", "model-b", "model-c"])
        assert cascade.model == "model-b"
        assert cascade._models == ["model-b", "model-c"]

    def test_starts_at_head_when_model_not_in_list(self) -> None:
        cascade = self._make_cascade("unknown", models=["model-a", "model-b"])
        # Falls back to full list when starting_model not found.
        assert cascade.model == "model-a"
        assert not cascade.all_exhausted

    def test_advance_moves_to_next_model(self) -> None:
        cascade = self._make_cascade("model-a")
        ok = cascade.advance()
        assert ok
        assert cascade.model == "model-b"

    def test_all_exhausted_after_draining_cascade(self) -> None:
        cascade = self._make_cascade("model-a")
        for _ in range(len(cascade._models)):
            cascade.advance()
        assert cascade.all_exhausted

    def test_advance_returns_false_when_exhausted(self) -> None:
        cascade = self._make_cascade("model-a", models=["model-a"])
        ok = cascade.advance()
        assert not ok
        assert cascade.all_exhausted

    def test_per_model_rpm_used_on_advance(self) -> None:
        """After advancing, the new model's documented RPM is used."""
        cascade = self._make_cascade(
            "gemini-3-flash", models=["gemini-3-flash", "gemini-2.5-flash-lite"]
        )
        cascade.advance()
        assert cascade.model == "gemini-2.5-flash-lite"
        assert cascade._limiter._min_interval == pytest.approx(
            60.0 / _MODEL_RATES["gemini-2.5-flash-lite"]
        )

    def test_per_model_rpm_fragment_lookup(self) -> None:
        """Fragment-based RPM lookup handles version-suffixed model IDs."""
        cascade = self._make_cascade(
            "gemini-2.5-flash-lite-001", models=["gemini-2.5-flash-lite-001"]
        )
        # "gemini-2.5-flash-lite" fragment matches the suffixed ID → 10 RPM.
        assert cascade._limiter._min_interval == pytest.approx(60.0 / 10)

    def test_check_daily_quota_header_zero(self) -> None:
        cascade = self._make_cascade()
        cascade._http_client.ratelimit_headers = {"x-ratelimit-remaining-requests-per-day": "0"}
        assert cascade.check_daily_quota_header() is True

    def test_check_daily_quota_header_nonzero(self) -> None:
        cascade = self._make_cascade()
        cascade._http_client.ratelimit_headers = {"x-ratelimit-remaining-requests-per-day": "100"}
        assert cascade.check_daily_quota_header() is False

    def test_desired_cascade_order(self) -> None:
        """Pro models first, then Flash, then Flash Lite (highest throughput last)."""
        fragments = [f for f, _ in _DESIRED_CASCADE]
        assert fragments[0] == "gemini-3.1-pro"
        assert fragments[1] == "gemini-2.5-pro"
        assert fragments[2] == "gemini-3-flash"
        assert fragments[3] == "gemini-2.5-flash"
        assert fragments[4] == "gemini-3.1-flash-lite"
        assert fragments[5] == "gemini-2.5-flash-lite"
        # _MODEL_CASCADE is derived from _DESIRED_CASCADE — same order.
        assert fragments == _MODEL_CASCADE

    def test_desired_cascade_fallback_rpms_non_zero(self) -> None:
        """Every cascade entry must specify a positive fallback RPM."""
        for fragment, rpm in _DESIRED_CASCADE:
            assert rpm > 0, f"Zero fallback_rpm for {fragment!r}"

    def test_per_model_rpm_initial_verified_model(self) -> None:
        """Cascade uses the verified _MODEL_RATES RPM for a known model."""
        cascade = self._make_cascade("gemini-2.5-flash-lite", models=["gemini-2.5-flash-lite"])
        assert cascade._limiter._min_interval == pytest.approx(60.0 / 10)  # confirmed free tier


# ---------------------------------------------------------------------------
# resolve_cascade
# ---------------------------------------------------------------------------


class TestResolveCascade:
    def _make_model(self, name: str, methods: list[str] | None = None) -> MagicMock:
        m = MagicMock()
        m.name = f"models/{name}"
        m.supported_generation_methods = methods if methods is not None else ["generateContent"]
        return m

    def test_returns_fragments_on_api_failure(self) -> None:
        client = MagicMock()
        client.models.list.side_effect = RuntimeError("network error")
        result = resolve_cascade(client)
        assert result == _MODEL_CASCADE

    def test_maps_fragments_to_actual_ids(self) -> None:
        client = MagicMock()
        client.models.list.return_value = [
            self._make_model("gemini-3-flash"),
            self._make_model("gemini-2.5-flash"),
            self._make_model("gemini-2.5-flash-lite"),
        ]
        result = resolve_cascade(client)
        assert "gemini-3-flash" in result
        assert "gemini-2.5-flash" in result
        assert "gemini-2.5-flash-lite" in result
        # Cascade priority order is preserved.
        assert result.index("gemini-3-flash") < result.index("gemini-2.5-flash")
        assert result.index("gemini-2.5-flash") < result.index("gemini-2.5-flash-lite")

    def test_skips_models_not_in_api(self) -> None:
        """Pro models not yet on the account are silently skipped."""
        client = MagicMock()
        client.models.list.return_value = [self._make_model("gemini-3-flash")]
        result = resolve_cascade(client)
        assert result == ["gemini-3-flash"]
        assert "gemini-3.1-pro" not in result

    def test_flash_does_not_claim_flash_lite(self) -> None:
        """'gemini-2.5-flash' fragment must not match 'gemini-2.5-flash-lite' models."""
        client = MagicMock()
        client.models.list.return_value = [
            self._make_model("gemini-2.5-flash"),
            self._make_model("gemini-2.5-flash-lite"),
        ]
        result = resolve_cascade(client)
        # Both should be present as separate entries.
        assert result.count("gemini-2.5-flash") == 1
        assert result.count("gemini-2.5-flash-lite") == 1

    def test_prefers_shortest_id_over_preview(self) -> None:
        """Canonical ID is preferred over dated preview variants."""
        client = MagicMock()
        client.models.list.return_value = [
            self._make_model("gemini-2.5-flash"),
            self._make_model("gemini-2.5-flash-preview-06-05"),
        ]
        result = resolve_cascade(client)
        # "gemini-2.5-flash" is shorter and wins.
        assert "gemini-2.5-flash" in result
        assert "gemini-2.5-flash-preview-06-05" not in result

    def test_skips_non_generate_content_models(self) -> None:
        client = MagicMock()
        client.models.list.return_value = [
            self._make_model("gemini-3-flash", methods=["embedContent"]),
            self._make_model("gemini-2.5-flash-lite", methods=["generateContent"]),
        ]
        result = resolve_cascade(client)
        assert "gemini-3-flash" not in result
        assert "gemini-2.5-flash-lite" in result


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
