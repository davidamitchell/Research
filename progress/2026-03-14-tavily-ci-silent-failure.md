# Session: Fix Tavily CI Silent Failure

**Date:** 2026-03-14
**Slug:** tavily-ci-silent-failure

## Context

`test_tavily_live_search` used `@pytest.mark.skipif(not _TAVILY_KEY, ...)`. When
`TAVILY_API_KEY` was absent from the environment, the test silently skipped — a skipped
test reports as `s` (not `F`), so a broken or missing credential produced a green CI run.
This was identified as the root cause of the 2026-03-13 silent Tavily failure recorded in
PROGRESS.md, where an invalid API key caused the agent to fall back to `web_search`
without any CI signal.

## Changes Made

- `pyproject.toml`: registered `integration` pytest marker
- `tests/test_mcp_config.py`:
  - Updated module docstring to document the `@pytest.mark.integration` pattern and
    local dev usage (`pytest -m "not integration"`)
  - Added `test_tavily_api_key_is_configured` — unconditional integration test that
    asserts `TAVILY_API_KEY` is non-empty; fails loudly in CI when the secret is absent
  - Added `@pytest.mark.integration` to both the new test and `test_tavily_live_search`
- `CHANGELOG.md`: added entries under `[Unreleased]`

## Verification

- `pytest -m "not integration"` passes with no Tavily key set (all integration tests excluded)
- `pytest -m integration` without `TAVILY_API_KEY` fails on `test_tavily_api_key_is_configured`
- `pytest -m integration` with a valid key passes both integration tests

## Pattern Learned

Silent-skip is a silent failure. Any credential-gated test that uses only `skipif` will
silently pass CI when the secret is misconfigured. The fix pattern is a companion
unconditional test marked `@pytest.mark.integration` that asserts the credential exists.
