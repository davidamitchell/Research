# Progress

Last updated: 2026-02-28 (skills submodules initialised)

---

## Current Status

**Phase:** Epic 3 — Indexing and Tracking (W-0020 done; W-0021 and W-0022 have defined scope from ADR-0003 but retain `needing_refinement` status until implementation is started)
**Next phase:** Epic 3 — Implement JSON state file (W-0021) and dedup logic (W-0022)
**Branch:** `copilot/start-research-backlog-item`

---

| Epic | Title | Status | Complete |
|---|---|---|---|
| 0 | Foundation | Done | 10 / 10 slices |
| 1 | Research Item Process | Done | 5 / 5 slices |
| 2 | YouTube Transcript Fetcher | Done | 4 / 4 slices |
| 3 | Indexing and Tracking | In Progress | 1 / 3 slices |

---

## Work Log

### 2026-02-28 — Session 7 (research item: indexing and tracking method)

**Completed:**

Research items:
- `Research/completed/2026-02-27-indexing-and-tracking-method.md` — completed; findings recommend JSON state file (`state/index.json`) for URL-based deduplication + YAML front-matter for item metadata; SQLite and vector stores deferred with clear migration trigger criteria

System improvements:
- `docs/adr/0003-indexing-and-tracking-approach.md` — ADR documenting the chosen approach, rejected alternatives, and migration trigger; unblocks Epic 3
- `docs/adr/README.md` — index updated
- `BACKLOG.md` — W-0020 marked done
- `PROGRESS.md` — Epic 3 status updated to "In Progress (1/3 slices)"

**MCP/Skills status:**
- Skills submodules initialized via `git submodule update --init`; `research` skill read and applied for evidence gathering and synthesis structure
- `web_search` used for research (analogous to `brave_search` MCP); `web_fetch` available
- `brave_search`, `arxiv`, `filesystem`, `sequential_thinking`, and `memory` MCP servers are not available in this agent environment (no Codespaces, no API keys); noted below in Next Steps

**Notes:**
- Epic 3 (indexing) is now unblocked: W-0021 (implement JSON state) and W-0022 (dedup logic) can proceed
- Skills submodules require `git submodule update --init` after a fresh clone in this CI environment; they are not auto-initialized

---

### 2026-02-27 — Session 1

**Completed:**
- `README.md` — updated with project description and quick start
- `AGENTS.md` — comprehensive agent instructions adapted from `davidamitchell/Latest-developments-`; research-specific workflow (add/start/complete items), output types, skills table, MCP config notes
- `BACKLOG.md` — repo improvement backlog, separate from research item backlog
- `PROGRESS.md` — this file
- `pyproject.toml`, `requirements.txt`, `.python-version` — Python 3.11 project config
- `.env.example` — example env vars
- `Makefile` — dev targets matching reference repo
- `.gitmodules` — skills submodule references (`davidamitchell/Skills`)
- `.github/copilot-instructions.md` — thin stub pointing to `AGENTS.md`
- `.github/mcp.json` — MCP server config for GitHub Copilot Agent
- `.mcp.json` — MCP server config for Claude Code and other agents
- `.devcontainer/devcontainer.json` — Codespaces setup
- `.github/workflows/ci.yml` — lint + test CI
- `.github/workflows/sync-skills.yml` — weekly skills submodule sync
- `docs/adr/README.md` — ADR index with template
- `docs/adr/0001-use-python-as-primary-language.md` — first ADR
- `Research/README.md` — research workflow documentation
- `Research/_template.md` — template for a new research item
- `Research/backlog/` — 9 research items added from the project backlog
- `Research/in-progress/` — placeholder
- `Research/completed/` — placeholder
- `src/main.py`, `src/logger.py`, `src/research/item.py`, `src/fetchers/__init__.py` — source skeleton
- `tests/conftest.py` — test skeleton
- `config/sources.yaml` — sources config stub

### 2026-02-28 — Session 2 (kickoff backlog work)

**Completed:**

Epic 1 — Research Item Process (W-0011 to W-0015):
- `src/research/cli.py` — `add`, `list`, `start`, `complete` commands
- `src/main.py` — wired research and fetch sub-commands
- `tests/test_research_cli.py` — full test coverage of all CLI commands

Epic 2 — YouTube Transcript Fetcher (W-0016 to W-0019):
- `src/fetchers/youtube.py` — `YouTubeFetcher` implementing the `Fetcher` protocol; supports channel feeds and individual video URLs; transcript fallback to description
- `src/config.py` — `load_config()` with schema validation for all sections
- `config/sources.yaml` — updated schema: `youtube.channels` + `youtube.videos`; added `https://youtu.be/HYUoS0GkGCs` as first video to process
- `tests/test_fetchers_youtube.py` — 15 tests with all network calls mocked
- `tests/test_config.py` — 9 tests for config loading and validation

Research items:
- `Research/backlog/2026-02-28-youtube-video-HYUoS0GkGCs-concepts.md` — research item for the video

**Notes:**
- 52 tests pass, `make check` clean
- `python -m src.main fetch youtube --video https://youtu.be/HYUoS0GkGCs` is the command to pull the transcript (requires network access to YouTube)
- Epic 3 (indexing) is blocked until `Research/backlog/2026-02-27-indexing-and-tracking-method.md` is completed

---

### 2026-02-28 — Session 6 (skills submodules — W-0026)

**Completed:**

- `.github/skills` — git submodule properly initialised, pointing to `davidamitchell/Skills` at `7095c41e842f036e2241ad9ae3aa1360db04be83` (latest)
- `.claude/skills` — same submodule added for Claude Code
- `.claude/CLAUDE.md` — thin stub pointing to `AGENTS.md` (matches `Latest-developments-` pattern)
- `docs/adr/0002-agent-skills-submodule.md` — ADR documenting the submodule decision
- `docs/adr/README.md` — index updated
- `BACKLOG.md` — W-0026 added and marked done

**Root cause of the gap:** The `.gitmodules` file was created manually in Session 1 (the entries were written as plain text) but `git submodule add` was never run, so no gitlink entries were committed into the tree. The skill directories did not exist and agents had no access to the skill files.

**Notes:**
- `sync-skills.yml` already handles both submodule paths — no changes needed there
- `AGENTS.md` already documents both submodule paths and the skills table correctly — no changes needed
- Weekly Monday sync will keep both pointers current without manual intervention

---

### 2026-02-28 — Session 5 (AI Strategy backlog item — government/opposition coverage)

**Completed:**

Research items:
- `Research/backlog/2026-02-28-ai-strategy.md` — enhanced to explicitly cover NZ current government (National-led coalition) and opposition (Labour, Green Party) AI policy positions; added Approach step 3 and corresponding source entry

---

### 2026-02-28 — Session 4 (AI Strategy backlog item)

**Completed:**

Research items:
- `Research/backlog/2026-02-28-ai-strategy.md` — AI strategy research item covering global/NZ examples, NZ regulatory and policy landscape (RBNZ, DIA, MBIE, PNZ), relevant case law, policy frameworks and categorisation schemas, DORA AI capability model, use-case typology (augmentation → agentic BUs), and the exploit vs explore distinction

---

### 2026-02-28 — Session 3 (Jevons Paradox backlog item)

**Completed:**

Research items:
- `Research/backlog/2026-02-28-jevons-paradox.md` — deep-dive on Jevons Paradox mechanics, historical sector examples, counter-examples, current SWE/code-cost commentary, and a 1/5/10-year speculative framework

System improvements:
- `AGENTS.md` — added explicit "Update PROGRESS.md" step to the Research Item Workflow (add/start/complete) so agents cannot skip it
- `Research/README.md` — same update to the quick-command workflow section

---

## Next Steps

1. Run `python -m src.main fetch youtube --video https://youtu.be/HYUoS0GkGCs` in a networked environment to pull the transcript
2. Extract concepts from the transcript and create per-concept deep-dive research items
3. Complete each concept research item, then synthesise findings back in `2026-02-28-youtube-video-HYUoS0GkGCs-concepts.md`
4. Epic 3 — decide on indexing approach once the indexing research item is completed
