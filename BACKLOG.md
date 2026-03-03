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

## W-0027

status: open
created: 2026-03-01
updated: 2026-03-01

### Outcome

`research/SKILL.md` in `davidamitchell/Skills` is updated with: citation-discipline and speculation-control composability instructions; confidence calibration table (high/medium/low); constraint parameter (full/bounded/rapid) with per-mode evidence sufficiency criteria; source prioritisation heuristic; output calibration guidance; tool-awareness note referencing AGENTS.md § MCP Configuration.

### Context

Retro findings from the AI strategy research session (2026-02-28) — issue #8. Requires a PR to `davidamitchell/Skills` (not this repo). Once merged, `sync-skills.yml` will pull in the updated submodule pointer, or trigger manually.

---

## W-0028

status: open
created: 2026-03-01
updated: 2026-03-01

### Outcome

`strategy-author/SKILL.md` in `davidamitchell/Skills` is updated with: research-to-diagnosis translation process; contextual adaptation notes for non-commercial settings (government, NZ SME, regulated financial); required time horizon statement in Metrics and Milestones; structured trade-offs format (alternative → rejection reason → re-evaluation signal); two diagnostic precision tests (falsifiability + constraint test); review triggers section (time-based and event-based); "symptom vs cause" added to Behavioral Constraints.

### Context

Review findings from post AI strategy research (2026-02-28) — issue #9. Requires a PR to `davidamitchell/Skills` (not this repo). Once merged, `sync-skills.yml` will pull in the updated submodule pointer.

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

## W-0029

status: done
created: 2026-03-02
updated: 2026-03-02

### Outcome

`.github/workflows/research-loop.yml` has safety controls preventing runaway autonomous loops: `timeout-minutes: 90` hard ceiling, constrained `max_items` dropdown (1–5), `HARD_MAX_ITERATIONS=10` shell guard, consecutive-failure abort at threshold 2, and 30-second inter-iteration sleep. Secret renamed to `COPILOT_GITHUB_TOKEN`. `tests/test_research_loop.py` proves all controls are in place. `docs/adr/0004-autonomous-research-loop.md` documents design decisions and rejected alternatives.

### Context

Owner confirmed the `COPILOT_GITHUB_TOKEN` secret is set. Original workflow had no timeout, accepted free-text `max_items` including `0` (unlimited), and had no consecutive-failure guard. ADR-0004 captures the full design rationale.

---

## W-0031

status: open
created: 2026-03-02
updated: 2026-03-02

### Outcome

A research review CI step runs automatically when a research item is moved to `Research/completed/`. The step applies the existing agent skills in sequence — `citation-discipline` (claims are sourced), `speculation-control` (uncertain claims are marked), `remove-ai-slop` (writing is direct and precise) — and fails the check if any skill reports violations. The design is informed by the findings of `Research/backlog/2026-03-02-research-quality-assurance-methodology.md`, which maps which review dimensions are automatable and in what order.

### Context

The existing CI pipeline (`.github/workflows/ci.yml`) runs linting and Python tests only. Research content quality is not checked. The skills already exist in `.github/skills/` (citation-discipline, speculation-control, remove-ai-slop) but are not wired into any automated gate.

This item is blocked until `Research/backlog/2026-03-02-research-quality-assurance-methodology.md` is completed: the CI step design depends on knowing which checks are automatable, which require agent reasoning, and in what order they should run. Once the research findings are available, this item can be scoped precisely. At minimum the CI step should be a `workflow_dispatch`-triggered GitHub Actions workflow that accepts a completed item path and runs each automatable skill check in sequence.

**Dependency:** `Research/backlog/2026-03-02-research-quality-assurance-methodology.md` (research on knowledge QA methodology — defines what is automatable and what design the CI step should follow)

---

## W-0032

status: open
created: 2026-03-03
updated: 2026-03-03

### Outcome

`brave_search` is removed from both `.github/mcp.json` and `.mcp.json`; the Tavily MCP entry uses the correct API key environment variable name so that `tavily-mcp` starts without error. `AGENTS.md` MCP Configuration section is updated to reflect the new server list.

### Context

`brave_search` is not actively used and requires a `BRAVE_API_KEY` credential that is not listed in the approved credentials table in `AGENTS.md`. Removing it reduces the attack surface and removes an unneeded external dependency.

The Tavily MCP server (`tavily-mcp@latest`) is currently configured with `TAVILY_API_KEY` but the server may expect a different env var name (e.g. `TAVILY_API_KEY` vs `tvly-...` token format). Investigate the correct variable name required by `tavily-mcp@latest`, update both MCP config files accordingly, and confirm the server starts cleanly. If a `TAVILY_API_KEY` repo secret does not yet exist, document what value is needed.

### Notes

Follow the e2e testing patterns in [`davidamitchell/Latest-developments-`](https://github.com/davidamitchell/Latest-developments-): apply the full testing pyramid (unit tests on business logic **plus** smoke/integration tests that exercise the pipeline end-to-end with mocked network calls, as in `tests/test_smoke.py`). Unit tests alone are not sufficient — see the Testing section and Slice Completion Checklist in that repo's `AGENTS.md` for the full pattern. In particular:

- Write unit tests that assert the MCP config JSON is valid, does not contain `brave_search`, and references the correct Tavily env var after the changes.
- Add a smoke-level check that loads both config files end-to-end (parse → validate → assert expected server list) to catch integration-level regressions that unit tests miss.
- Slice is not done until `make check` and `make test` both pass and the checklist item "Full testing pyramid applied" is satisfied.

---

## W-0030

status: done
created: 2026-03-02
updated: 2026-03-02

### Outcome

`src/wiki/publish.py` converts completed research items to GitHub wiki pages (strips YAML front-matter, generates `Home.md` date-sorted index, generates `_Sidebar.md` tag navigation, full-rebuild on each run). `.github/workflows/publish-wiki.yml` triggers on push to `main` touching `Research/completed/**` and on `workflow_dispatch`; uses `GITHUB_TOKEN` with `contents: write` — no PAT required. `tests/test_wiki.py` has 24 tests covering all module functions. Research item `Research/completed/2026-03-01-github-wiki-research-content.md` is completed with full findings.

### Context

Spawned from `Research/backlog/2026-03-01-github-wiki-research-content.md`. Owner must enable the wiki once in repository Settings → Features → Wikis before the first workflow run can push to it.

---
