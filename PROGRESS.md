# Progress

Last updated: 2026-02-27

---

## Current Status

**Phase:** Epic 0 — Foundation (in progress)
**Active slice:** 0.1–0.10 (initial scaffold)
**Branch:** `copilot/create-research-backlog-structure`

---

| Epic | Title | Status | Complete |
|---|---|---|---|
| 0 | Foundation | In Progress | 10 / 10 slices |
| 1 | Research Item Process | Not started | 0 / 5 slices |
| 2 | YouTube Transcript Fetcher | Not started | 0 / 4 slices |
| 3 | Indexing and Tracking | Not started | 0 / 3 slices |

---

## Work Log

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

**Notes:**
- Research backlog and repo improvement backlog are intentionally separate:
  - `Research/backlog/` = what to research
  - `BACKLOG.md` = how to improve this repo
- Submodules (`.github/skills/`, `.claude/skills/`) are declared in `.gitmodules` but must be initialised manually: `git submodule update --init --recursive`
- YouTube transcript fetcher will be ported from `davidamitchell/Latest-developments-` in Epic 2

---

## Next Steps

1. Epic 1 — research item CLI commands (`add`, `list`, `start`, `complete`)
2. Epic 2 — port YouTube transcript fetcher
3. Epic 3 — decide on indexing approach (research item in `Research/backlog/`)
