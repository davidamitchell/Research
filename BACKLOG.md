# Backlog

This file tracks **repo improvement** work — code, tooling, structure, and process changes.

For **research item** backlog, see `Research/backlog/`.

Status legend: `[ ]` Not started · `[→]` In progress · `[x]` Done · `[~]` Deferred

---

## Epic 0 — Foundation

| # | Slice | Status | Notes |
|---|---|---|---|
| 0.1 | Create README, AGENTS, BACKLOG, PROGRESS | `[x]` | |
| 0.2 | Create `docs/adr/` with initial ADR | `[x]` | ADR-0001 |
| 0.3 | Create `pyproject.toml`, `requirements.txt`, `.python-version` | `[x]` | |
| 0.4 | Add `.devcontainer/`, `Makefile`, `.env.example` | `[x]` | Codespaces-ready |
| 0.5 | Create `src/` skeleton — `main.py`, `logger.py`, `research/item.py` | `[x]` | |
| 0.6 | Create `tests/` skeleton — `conftest.py` | `[x]` | |
| 0.7 | Add `Research/` directory with state subdirs and template | `[x]` | |
| 0.8 | Add `.github/copilot-instructions.md`, `.github/mcp.json`, `.mcp.json` | `[x]` | |
| 0.9 | Add `.github/workflows/ci.yml` | `[x]` | |
| 0.10 | Add agent skills submodules (`.github/skills/`, `.claude/skills/`) + sync workflow | `[x]` | Submodules reference `davidamitchell/Skills`; run `git submodule update --init` to populate |

---

## Epic 1 — Research Item Process

Tooling to make adding and tracking research items fast and consistent.

| # | Slice | Status | Notes |
|---|---|---|---|
| 1.1 | CLI command: `python -m src.main research add "<title>"` — creates a timestamped file from template in `Research/backlog/` | `[ ]` | |
| 1.2 | CLI command: `python -m src.main research list` — lists backlog / in-progress items | `[ ]` | |
| 1.3 | CLI command: `python -m src.main research start <filename>` — moves file to `in-progress/` | `[ ]` | |
| 1.4 | CLI command: `python -m src.main research complete <filename>` — moves file to `completed/` | `[ ]` | |
| 1.5 | Tests for all CLI research commands | `[ ]` | |

**Acceptance criteria:** `python -m src.main research add "test item"` creates a correctly named file in `Research/backlog/` with all template sections filled in.

---

## Epic 2 — YouTube Transcript Fetcher

Port and adapt the YouTube transcript fetcher from `davidamitchell/Latest-developments-`.

| # | Slice | Status | Notes |
|---|---|---|---|
| 2.1 | `src/fetchers/youtube.py` — fetch transcript for a channel's latest videos | `[ ]` | Port from Latest-developments- repo |
| 2.2 | `config/sources.yaml` — define YouTube sources config schema | `[ ]` | |
| 2.3 | CLI: `python -m src.main fetch youtube <channel_id>` — print transcript to stdout | `[ ]` | |
| 2.4 | Unit tests with mocked HTTP | `[ ]` | |

**Acceptance criteria:** `python -m src.main fetch youtube <channel_id>` prints the transcript of the latest video for the given channel.

---

## Epic 3 — Indexing and Tracking

Decide on and implement an indexing and tracking method for research content.

| # | Slice | Status | Notes |
|---|---|---|---|
| 3.1 | Write ADR-0002: indexing and tracking approach (local JSON, SQLite, or vector store) | `[ ]` | Depends on research item: `Research/backlog/indexing-and-tracking-method.md` |
| 3.2 | Implement chosen approach | `[ ]` | Depends on 3.1 |
| 3.3 | `state/index.json` (or SQLite) — stores processed item metadata | `[ ]` | |

---

## Deferred / Ideas

| Idea | Notes |
|---|---|
| Web interface for research items | Out of scope for file-first approach |
| Automated research summary emails | Possible future Epic using Latest-developments- pattern |
| Vector semantic search across completed items | Useful once `completed/` has enough items |
