# Session: fix-research-loop-env-vars

**Date:** 2026-03-14  
**Issue:** #7 — research-loop.yml sets wrong/incomplete env vars  

## What was wrong

The `Run research loop` step in `.github/workflows/research-loop.yml` only set one env var, and used the wrong name:

```yaml
env:
  GH_TOKEN: ${{ secrets.COPILOT_GITHUB_TOKEN }}
```

This caused two silent failures:
1. The Copilot CLI authenticates via `GITHUB_TOKEN`, not `GH_TOKEN` — the CLI ran unauthenticated.
2. `TAVILY_API_KEY` and `YOUTUBE_DATA_API` were never set — the Tavily MCP server and YouTube fetcher silently failed.

## Changes made

- `.github/workflows/research-loop.yml` — replaced `GH_TOKEN` with `GITHUB_TOKEN`; added `TAVILY_API_KEY` and `YOUTUBE_DATA_API` to the loop step `env:` block
- `.github/workflows/research-loop.yml` — updated header comment to document all three required secrets
- `tests/test_research_loop.py` — added `test_workflow_run_loop_step_uses_github_token_not_gh_token`, `test_workflow_run_loop_step_sets_tavily_api_key`, `test_workflow_run_loop_step_sets_youtube_data_api`
- `CHANGELOG.md` — logged fix under `[Unreleased]`
