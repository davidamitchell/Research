# 2026-03-14 — Fix Research Loop Env Vars (fix-research-loop-env-vars)

## What changed

- `.github/workflows/research-loop.yml` — added `TAVILY_API_KEY: ${{ secrets.TAVILY_API_KEY }}` to the
  `Run research loop` step `env` block. Without this, the Tavily MCP server received no API key and
  silently fell back to `web_search` on every research loop run.

- `tests/test_research_loop.py` — added `test_workflow_research_step_sets_tavily_api_key` which parses
  the workflow YAML and asserts the `Run research loop` step declares `TAVILY_API_KEY` in its `env`
  block. This test will fail loudly if the env var is accidentally removed.

## Root cause

The "Run research loop" step in `research-loop.yml` only declared `GH_TOKEN` in its `env` block.
The GitHub Copilot CLI inherits the environment of the runner step, so `TAVILY_API_KEY` was never
visible to the tavily MCP server process spawned by the Copilot agent. Every research session since
the tavily server was added has silently failed to authenticate — the fallback to `web_search` masked
the breakage.

## Mini-Retro

1. **Did the process work?** Yes. One-line workflow fix + structural test + progress note.
2. **What slowed down or went wrong?** A stale memory entry claimed the fix had already been applied.
   Always verify memories against actual file contents before treating them as ground truth.
3. **What single change would prevent this next time?** The new structural test —
   `test_workflow_research_step_sets_tavily_api_key` — is precisely that change. CI will now fail if
   the env var disappears from the step.
