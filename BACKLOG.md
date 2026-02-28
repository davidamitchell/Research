# Backlog

> This file tracks **repo improvement** work — code, tooling, structure, and process changes.
> For **research item** backlog, see `Research/backlog/`.

---

## W-0001

status: done
created: 2026-02-27
updated: 2026-02-27

### Outcome

README, AGENTS.md, BACKLOG.md, and PROGRESS.md exist at the repo root with content covering project purpose, agent instructions, work tracking, and session history.

### Context

Foundation scaffold required before any other work can begin.

---

## W-0002

status: done
created: 2026-02-27
updated: 2026-02-27

### Outcome

`docs/adr/` exists with an index file and at least one ADR (0001) following MADR format.

### Context

ADRs capture design decisions before context is lost.

---

## W-0003

status: done
created: 2026-02-27
updated: 2026-02-27

### Outcome

`pyproject.toml`, `requirements.txt`, and `.python-version` are present; `pip install -e ".[dev]"` succeeds and `python -m pytest` can be invoked.

### Context

Python project tooling defined in `pyproject.toml` as the single source of truth.

---

## W-0004

status: done
created: 2026-02-27
updated: 2026-02-27

### Outcome

`.devcontainer/devcontainer.json`, `Makefile`, and `.env.example` are present; `make dev-install` succeeds and the dev environment is ready in Codespaces without manual steps.

---

## W-0005

status: done
created: 2026-02-27
updated: 2026-02-27

### Outcome

`src/main.py`, `src/logger.py`, `src/research/item.py`, and `src/fetchers/__init__.py` exist with working implementations; `python -m src.main` runs without errors.

---

## W-0006

status: done
created: 2026-02-27
updated: 2026-02-27

### Outcome

`tests/conftest.py` exists and `pytest tests/` collects and passes at least one test.

---

## W-0007

status: done
created: 2026-02-27
updated: 2026-02-27

### Outcome

`Research/backlog/`, `Research/in-progress/`, `Research/completed/`, `Research/_template.md`, and `Research/README.md` exist; the template can be copied and filled in to create a valid research item.

---

## W-0008

status: done
created: 2026-02-27
updated: 2026-02-27

### Outcome

`.github/copilot-instructions.md` points to `AGENTS.md`; `.github/mcp.json` and `.mcp.json` contain valid MCP server configurations for GitHub Copilot and Claude Code respectively.

---

## W-0009

status: done
created: 2026-02-27
updated: 2026-02-27

### Outcome

`.github/workflows/ci.yml` runs ruff lint, format check, and pytest on every push and pull request; CI passes on a clean branch.

---

## W-0010

status: done
created: 2026-02-27
updated: 2026-02-27

### Outcome

`.gitmodules` declares `.github/skills/` and `.claude/skills/` as submodules of `davidamitchell/Skills`; `.github/workflows/sync-skills.yml` runs weekly and advances both submodule pointers to the latest upstream commit.

---

## W-0011

status: done
created: 2026-02-27
updated: 2026-02-28

### Outcome

`python -m src.main research add "test item"` creates a correctly named, template-populated file in `Research/backlog/` with today's date prefix and all front-matter fields present.

### Context

Epic 1 — Research Item Process. Reduces friction for capturing new research ideas.

---

## W-0012

status: done
created: 2026-02-27
updated: 2026-02-28

### Outcome

`python -m src.main research list` prints all items in `Research/backlog/` and `Research/in-progress/` with their title and status, one per line.

### Context

Epic 1 — Research Item Process.

---

## W-0013

status: done
created: 2026-02-27
updated: 2026-02-28

### Outcome

`python -m src.main research start <filename>` moves the named file from `Research/backlog/` to `Research/in-progress/` and updates its `status:` front-matter field to `in-progress`.

### Context

Epic 1 — Research Item Process.

---

## W-0014

status: done
created: 2026-02-27
updated: 2026-02-28

### Outcome

`python -m src.main research complete <filename>` moves the named file from `Research/in-progress/` to `Research/completed/` and updates its `status:` front-matter field to `completed`.

### Context

Epic 1 — Research Item Process.

---

## W-0015

status: done
created: 2026-02-27
updated: 2026-02-28

### Outcome

`pytest tests/test_research_cli.py` passes; tests cover `add`, `list`, `start`, and `complete` commands with expected file-system outcomes verified.

### Context

Epic 1 — Research Item Process. Tests use `tmp_path` fixtures; no real `Research/` directory mutation.

---

## W-0016

status: done
created: 2026-02-27
updated: 2026-02-28

### Outcome

`src/fetchers/youtube.py` implements the `Fetcher` protocol and returns transcripts (or description fallback) for a channel's latest N videos and for individual video URLs without raising an exception.

### Context

Epic 2 — YouTube Transcript Fetcher.

---

## W-0017

status: done
created: 2026-02-27
updated: 2026-02-28

### Outcome

`config/sources.yaml` defines a complete, documented YouTube sources schema (channels + individual videos); `src/config.py` validates it on load and raises a descriptive error on invalid input.

### Context

Epic 2 — YouTube Transcript Fetcher.

---

## W-0018

status: done
created: 2026-02-27
updated: 2026-02-28

### Outcome

`python -m src.main fetch youtube --video <url>` prints the transcript to stdout; `--channel <id>` fetches the latest N videos from a channel. Both paths are wired in `src/main.py`.

### Context

Epic 2 — YouTube Transcript Fetcher. Depends on W-0016 and W-0017.

---

## W-0019

status: done
created: 2026-02-27
updated: 2026-02-28

### Outcome

`pytest tests/test_fetchers_youtube.py` passes with all HTTP and transcript calls mocked; covers transcript fetch, description fallback, single-video fetch, and error handling.

### Context

Epic 2 — YouTube Transcript Fetcher.

---

## W-0020

status: done
created: 2026-02-27
updated: 2026-02-28

### Outcome

`docs/adr/0003-indexing-and-tracking-approach.md` documents the chosen indexing and tracking approach: JSON state file (`state/index.json`) for URL-based deduplication + YAML front-matter in research item `.md` files for item metadata. ADR includes rationale, rejected alternatives (SQLite, YAML index, vector store), and migration trigger criteria.

### Context

Epic 3 — Indexing and Tracking. Research item `Research/completed/2026-02-27-indexing-and-tracking-method.md` was completed first; findings directly informed the ADR.

---

## W-0021

status: done
created: 2026-02-27
updated: 2026-02-28

### Outcome

`src/state.py` implements `StateStore`: `is_processed(url)`, `record(item)`, `processed_urls()`. Writes are atomic (temp file + `os.replace`). Default path is `state/index.json`. Schema matches ADR-0003.

### Context

Epic 3 — Indexing and Tracking. Depends on W-0020 (ADR-0003 accepted).

---

## W-0022

status: done
created: 2026-02-27
updated: 2026-02-28

### Outcome

`state/index.json` persists processed item metadata across runs; running the pipeline twice does not reprocess already-indexed items. `_fetch_youtube` in `src/main.py` skips already-processed URLs and prints `[skip]` for each. `tests/test_state.py` has 12 tests covering all `StateStore` behaviour.

### Context

Epic 3 — Indexing and Tracking. Depends on W-0021.

---

## W-0023

status: archived
created: 2026-02-27
updated: 2026-02-27

### Outcome

A web interface allows browsing research items and their status in a browser.

### Notes

Out of scope for the file-first approach. Revisit if the corpus grows large enough to warrant it.

---

## W-0024

status: archived
created: 2026-02-27
updated: 2026-02-27

### Outcome

A weekly automated email summarises newly completed research items, modelled on the `davidamitchell/Latest-developments-` digest pattern.

### Notes

Deferred — no email infrastructure in this repo yet.

---

## W-0025

status: archived
created: 2026-02-27
updated: 2026-02-27

### Outcome

`python -m src.main search "<query>"` returns semantically related completed research items ranked by relevance.

### Notes

Deferred — requires a vector index; useful once `Research/completed/` has enough items.

---

## W-0026

status: done
created: 2026-02-28
updated: 2026-02-28

### Outcome

`.github/skills/` and `.claude/skills/` are properly initialised git submodules pointing to `davidamitchell/Skills`; `.claude/CLAUDE.md` exists as a thin stub pointing to `AGENTS.md`; `docs/adr/0002-agent-skills-submodule.md` documents the decision; `sync-skills.yml` advances both submodule pointers weekly.

### Context

Skills were declared in `.gitmodules` but never registered as actual git submodules (no gitlink entries in the tree). This slice completes the setup end-to-end, matching the pattern used in `davidamitchell/Latest-developments-`.

---
