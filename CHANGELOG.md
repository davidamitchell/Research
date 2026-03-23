# Changelog

All notable changes to this project will be documented here.

Format follows [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).

## [Unreleased]

### Fixed
- `research-loop.yml` Run research loop step: replaced `GH_TOKEN` with `GITHUB_TOKEN` (the env var the Copilot CLI actually reads); added `TAVILY_API_KEY` and `YOUTUBE_DATA_API` to the env block so the Tavily MCP server and YouTube fetcher no longer fail silently
- `research-loop.yml` header comment: updated required-secrets documentation to list all three secrets (`COPILOT_GITHUB_TOKEN`, `TAVILY_API_KEY`, `YOUTUBE_DATA_API`) with their purposes
- `test_research_loop.py`: added three new tests asserting `GITHUB_TOKEN` (not `GH_TOKEN`) and both `TAVILY_API_KEY` / `YOUTUBE_DATA_API` are present in the loop step env block

### Added
- `@pytest.mark.integration` marker registered in `pyproject.toml`; run `pytest -m "not integration"` locally to skip credential-gated tests
- `test_tavily_api_key_is_configured` — unconditional integration test that asserts `TAVILY_API_KEY` is set; fails loudly in CI when the secret is absent or misconfigured, closing the silent-skip gap
- `@pytest.mark.integration` applied to both `test_tavily_api_key_is_configured` and `test_tavily_live_search` for consistent grouping
- `reviewing` status to the research item lifecycle (`backlog → in-progress → reviewing → completed`); `reviewing` maps to `in-progress/` so no file moves during review
- `research draft` CLI command (`python -m src.main research draft <filename>`) — updates `status` to `reviewing` in-place; does not move the file
- ADR-0007: Reviewing state and workflow_dispatch trigger for research review
- **Known Recurring Failure Patterns** table in `.github/copilot-instructions.md` Continuous Improvement section — persistent registry of patterns observed 3+ times with root fix documented; future sessions add new rows during Mini-Retro
- **Quick Reference block** at top of `.github/copilot-instructions.md` — 5-item summary of most-missed rules, visible before Project Overview; addresses "lost in the middle" effect for large instruction files
- **Evaluation protocol** in `.github/copilot-instructions.md` Improvement Flywheel section — mandates external benchmarking (not self-inspection) when evaluating the system

### Fixed
- `Research/_template.md`: `reviewing` added to status comment (`backlog | in-progress | reviewing | completed`); previously missing despite being a valid status since PR #104
- `research-prompt.md` Step 8: commit message format corrected from `<filename>` to `${SLUG}` variable, matching Step 13 convention
- `research-prompt.md` Steps 8–9: review workflow is now a genuine blocking gate — added `gh run list` + `gh run watch` to wait for completion; Step 9 now uses `gh issue list` for programmatic outcome detection; added `gh issue close` when review passes
- `.github/copilot-instructions.md` line 176: stale section reference corrected from "research-prompt.md §4" to "Steps 3–7 of research-prompt.md"
- `.github/copilot-instructions.md` line 399: research loop description corrected from "commits the completed item" to accurately describe draft → review → complete sequence
- `.github/copilot-instructions.md` Completing Research step 4: added "close the review issue" before completing the item

### Changed
- `research-review.yml`: removed `push` trigger on `Research/completed/**`; review is now triggered exclusively via `workflow_dispatch` with `item_path` input; `item_path` description updated to accept `Research/in-progress/` paths
- `cmd_complete`: soft guard — warns to stderr if item status is not `reviewing` before completing, but proceeds anyway (no hard block)
- `research-prompt.md`: replaced single "Complete the item" step with three steps — draft (mark as reviewing), handle review outcome, then complete
- `Research/in-progress/README.md`: documents `reviewing` status and that files stay here during review
- `Research/README.md`: updated lifecycle section to show four-state flow and the new `research draft` command
- `research-prompt.md` Step 6: added inline acronym expansion audit with 13-entry table of high-frequency failures (LLM, CLI, SDK, PAT, MCP, RAG, CoT, SRE, ITSM, PaaS, MECE, PR, API) — addresses root cause of 19+ research review failures; audit is now self-contained and does not depend on the skills submodule being available
- `research-prompt.md`: added Step 11 (Update `learnings.md`) between Complete and Create session log; Steps 11-12 renumbered to 12-13
- `research-prompt.md` Step 12 (session log): added Mini-Retro format to session log template so automated research loop sessions produce retros
- `.github/copilot-instructions.md` Completing Research: added `learnings.md` update as step 5; renumbered steps 5-6 to 6-7
- `.github/copilot-instructions.md` Known Recurring Patterns: added "surface evaluation" pattern entry

### Changed
- `research-prompt.md`: collapsed duplicated source-marking, output-quality, prior-work-check, and companion-skill-check rules to single-line deferrals to `research/SKILL.md §0`, `§2`, `§6`, and `§8`
- `research-prompt.md`: DRY refactor — collapsed duplicate remove-ai-slop and self-review steps (old Steps 6 and 8) into a single step referencing `research/SKILL.md §8 Output Finalisation`; renumbered affected steps; retained inline source-marking, output-quality, and prior-work-check content (to be referenced from skill once submodule is updated)

### Fixed
- `Research/completed/2026-03-08-ios-shortcuts-github-api-memory-capture.md`: expanded PAT, MIME, LTE acronyms; fixed secondary rate limit citation URL; corrected "most common failure mode" to "a likely failure mode"; added `[inference]` labels to unattributed claims (issues #66)
- `Research/completed/2026-03-08-inbox-folder-capture-triage-pattern.md`: expanded PKM, HCI, ULID acronyms; corrected `[fact]`→`[inference]` on YAML front-matter claim; removed unverifiable AAAI ICWSM citation; added `Opinion:` and `[inference]` labels; rewrote AI-slop patterns in Findings Analysis (issue #65)
- `Research/completed/2026-03-08-claude-ios-mcp-remote-integration.md`: expanded MCP, SSE, RFC, ASGI, WSGI, PAT acronyms; added Cloudflare Workers pricing citation; added Connectors Directory URL; added `Opinion:` and `[inference]` labels to subjective claims (issue #64)
- `Research/completed/2026-03-08-servicenow-csdm-data-modelling.md`: expanded ITSM, GRC, IRM, CI, CMDB, TBM, ITOM, DORA, RBNZ acronyms; replaced unverifiable "web search synthesis" citations with specific URLs; labelled uncited partner sources as `[inference]`; added `[fact]`/`[inference]` labels to §5 analytical claims; rewrote repetitive Findings Analysis paragraph openings; compressed near-verbatim repeated insight (issue #63)

### Added
- Research backlog items for mobile memory capture and retrieval (8 items covering iOS Shortcuts, Telegram, Slack, Claude iOS MCP, self-hosted MCP, LanceDB index rebuild, ChatGPT Actions, inbox pattern)
- `Research/completed/2026-03-04-sdlc-ai-prompt-patterns.md`: completed research on emergent AI prompt patterns for SDLC phases; key findings: 55.8% Build-phase speed gain (Peng et al. 2023), SCoT +13.79% Pass@1 over CoT (Li et al. 2023), DORA 2024 AI adoption correlation (+3.4% code quality, -7.2% delivery stability); phase taxonomy, evidence map, and tooling alignment framework including MCP prompts primitive
- `.github/copilot-instructions.md` (full content, replaces `AGENTS.md` stub)
- `CHANGELOG.md` (this file)
- `docs-adr/0006-standardise-agent-instructions.md`
- `## Continuous Improvement & Learning` unified self-improvement framework in `.github/copilot-instructions.md`
- `## Chain-of-Thought Reasoning` section in `.github/copilot-instructions.md`

### Changed
- `.github/copilot-instructions.md`: replaced `## Mini-Retro — After Each Piece of Work` and `## When to Update These Instructions` with the unified Continuous Improvement & Learning framework

### Removed
- `AGENTS.md` (content moved to `.github/copilot-instructions.md`)
- `.claude/` directory and `.claude/skills` submodule

### Changed
- `.gitmodules`: removed `.claude/skills` entry
- `.github/workflows/sync-skills.yml`: removed `.claude/skills` sync step
- `README.md`: updated to reflect current structure
- `BACKLOG.md`: added W-0033 for standardisation work
- `docs-adr/README.md`: added ADR-0006, added "When to write an ADR" section
