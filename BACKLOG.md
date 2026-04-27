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

`docs-adr/` exists with an index file and at least one ADR (0001) following MADR format.

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

status: open
created: 2026-02-27
updated: 2026-03-28

### Outcome

`.devcontainer/devcontainer.json`, `Makefile`, and `.env.example` are present; `make dev-install` succeeds and the dev environment is ready in Codespaces without manual steps.

### Notes

`.devcontainer/devcontainer.json` is absent — confirmed 2026-03-28. W-0004 was incorrectly marked done. Reopened. See W-0036 for the full environment consistency work that will deliver this.

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

`docs-adr/0003-indexing-and-tracking-approach.md` documents the chosen indexing and tracking approach: JSON state file (`state/index.json`) for URL-based deduplication + YAML front-matter in research item `.md` files for item metadata. ADR includes rationale, rejected alternatives (SQLite, YAML index, vector store), and migration trigger criteria.

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

status: done
created: 2026-03-01
updated: 2026-03-09

### Outcome

`research/SKILL.md` in `davidamitchell/Skills` is updated with: citation-discipline and speculation-control composability instructions; confidence calibration table (high/medium/low); constraint parameter (full/bounded/rapid) with per-mode evidence sufficiency criteria; source prioritisation heuristic; output calibration guidance; tool-awareness note referencing AGENTS.md § MCP Configuration.

### Context

Retro findings from the AI strategy research session (2026-02-28) — issue #8. Requires a PR to `davidamitchell/Skills` (not this repo). Once merged, `sync-skills.yml` will pull in the updated submodule pointer, or trigger manually.

### Notes

Delivered by Skills v1.1 PR — research/SKILL.md now contains citation-discipline and speculation-control composability, confidence calibration table, constraint parameter with per-mode evidence sufficiency, source prioritisation heuristic, output calibration guidance, and tool-awareness note.

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

`.github/skills/` and `.claude/skills/` are properly initialised git submodules pointing to `davidamitchell/Skills`; `.claude/CLAUDE.md` exists as a thin stub pointing to `AGENTS.md`; `docs-adr/0002-agent-skills-submodule.md` documents the decision; `sync-skills.yml` advances both submodule pointers weekly.

### Context

Skills were declared in `.gitmodules` but never registered as actual git submodules (no gitlink entries in the tree). This slice completes the setup end-to-end, matching the pattern used in `davidamitchell/Latest-developments-`.

---

## W-0029

status: done
created: 2026-03-02
updated: 2026-03-02

### Outcome

`.github/workflows/research-loop.yml` has safety controls preventing runaway autonomous loops: `timeout-minutes: 90` hard ceiling, constrained `max_items` dropdown (1–5), `HARD_MAX_ITERATIONS=10` shell guard, consecutive-failure abort at threshold 2, and 30-second inter-iteration sleep. Secret renamed to `COPILOT_GITHUB_TOKEN`. `tests/test_research_loop.py` proves all controls are in place. `docs-adr/0004-autonomous-research-loop.md` documents design decisions and rejected alternatives.

### Context

Owner confirmed the `COPILOT_GITHUB_TOKEN` secret is set. Original workflow had no timeout, accepted free-text `max_items` including `0` (unlimited), and had no consecutive-failure guard. ADR-0004 captures the full design rationale.

---

## W-0031

status: done
created: 2026-03-02
updated: 2026-03-07

### Outcome

A research review CI step runs automatically when a research item is moved to `Research/completed/`. The step applies the existing agent skills in sequence — `citation-discipline` (claims are sourced), `speculation-control` (uncertain claims are marked), `remove-ai-slop` (writing is direct and precise) — and fails the check if any skill reports violations. The design is informed by the findings of `Research/backlog/2026-03-02-research-quality-assurance-methodology.md`, which maps which review dimensions are automatable and in what order.

### Context

The existing CI pipeline (`.github/workflows/ci.yml`) runs linting and Python tests only. Research content quality is not checked. The skills already exist in `.github/skills/` (citation-discipline, speculation-control, remove-ai-slop) but are not wired into any automated gate.

This item is blocked until `Research/backlog/2026-03-02-research-quality-assurance-methodology.md` is completed: the CI step design depends on knowing which checks are automatable, which require agent reasoning, and in what order they should run. Once the research findings are available, this item can be scoped precisely. At minimum the CI step should be a `workflow_dispatch`-triggered GitHub Actions workflow that accepts a completed item path and runs each automatable skill check in sequence.

**Dependency:** `Research/backlog/2026-03-02-research-quality-assurance-methodology.md` (research on knowledge QA methodology — defines what is automatable and what design the CI step should follow)

### Notes

Implemented the "at minimum" path: the dependency research item has not yet been
completed, but the minimum viable outcome is fully specified and has been built:

- `.github/workflows/research-review.yml` — triggers on `push` to main when
  `Research/completed/**.md` changes, and on `workflow_dispatch` with an
  `item_path` input. Initialises `.github/skills` submodule, invokes the Copilot
  CLI with `research-review-prompt.md`, and fails the job if the agent writes
  `OVERALL: FAIL` to `/tmp/research-review-report.txt`. Uses `contents: read`
  permissions so no accidental commits are possible.
- `research-review-prompt.md` — audit-only prompt: tells the agent to read each
  SKILL.md, check the item for violations, write a structured PASS/FAIL report,
  and explicitly not modify or commit anything.
- `tests/test_research_review.py` — 29 structural tests proving workflow
  attributes (trigger, permissions, submodule, COPILOT_GITHUB_TOKEN, timeout) and
  prompt content (placeholder, skill references, output format, prohibitions).

When `Research/backlog/2026-03-02-research-quality-assurance-methodology.md` is
completed, revisit this workflow to refine which checks are LLM-automatable vs
heuristic-automatable and adjust the ordering accordingly.

---

## W-0032

status: done
created: 2026-03-03
updated: 2026-03-04

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

## W-0033

status: done
created: 2026-03-07
updated: 2026-03-07

### Outcome

Repository structure is standardised: single `.github/copilot-instructions.md` source of truth, `.github/skills` submodule, `sync-skills.yml` workflow, `BACKLOG.md`, `PROGRESS.md`, `CHANGELOG.md`, and `docs-adr/` all present and consistent.

### Context

Standardisation pass to remove AGENTS.md/.claude/ and align with all other repos in the davidamitchell organisation.

---

## W-0034

status: open
created: 2026-03-08
updated: 2026-03-08

### Outcome

The completed research corpus is more than a flat collection of files: (1) a **meta-distillation layer** proactively aggregates findings across items — on a schedule or when new items complete — surfacing higher-order themes, categories, and emergent ideas not visible in any single item; (2) a **knowledge map** renders the relationships between items, concepts, and tags as a connected, navigable structure; (3) a **search and synthesis interface** supports both reactive (query-time) and active (push-based) synthesis — answering ad-hoc queries with provenance links and automatically publishing new distilled insights as the corpus grows.

### Context

Three distinct but related needs identified by the owner:

1. **Meta distillation / categorisation** — as `Research/completed/` grows, cross-item patterns and new hypotheses become invisible. An aggregation step is needed to surface what multiple items, taken together, imply. This must be both **reactive** (answer a specific question) and **active** (run automatically, e.g. when a new item is completed or on a schedule, and commit the result). This is distinct from reading items individually.

2. **Knowledge map** — the existing wiki (`W-0030`) produces a flat date-sorted index and a tag sidebar. A map goes further: it shows how items relate to one another (shared tags, concept overlap, dependency chains, thematic clusters). Could be a static graph rendered in the wiki, a Mermaid diagram, or a separate page. Ideally regenerated automatically on each corpus change.

3. **Search and synthesis** — `W-0025` (deferred semantic search) covers retrieval; this slice adds the synthesis step: given a query, return a distilled answer drawn from multiple relevant items, not just matching file paths. Also includes **active synthesis**: when enough new items accumulate (or on a weekly schedule), generate a digest of new insights and commit it to the repo/wiki without the owner needing to ask.

All three share the goal of making the research corpus navigable, connected, and insight-generating — more than the sum of its parts. The **active** dimension is a first-class requirement: the system should push insights to the owner, not only respond when queried.

**Suggested implementation order:**
- Start with a research item in `Research/backlog/` to define the approach (tool choices, index format, LLM-vs-heuristic trade-offs, active vs reactive trigger design) before building.
- Knowledge map (static Mermaid/tag-graph via `publish.py` extension) is the lowest-effort first step — naturally active because `publish-wiki.yml` already triggers on corpus changes.
- Active meta-distillation (scheduled workflow, context-window pass over all completed items, committed digest) is the second step.
- Reactive search and synthesis builds on the same index and can be added as a `workflow_dispatch` interface or CLI command.

**Related items:** W-0025 (deferred semantic search — can be revived as part of this slice), W-0030 (wiki publish pipeline — the map and active digest extend this).

---

## W-0035

status: open
created: 2026-03-28
updated: 2026-03-28

### Outcome

Confirmed, documented answers to:
1. Which files the GitHub Copilot coding agent reads automatically when an issue is assigned to it (`.github/copilot-instructions.md`, `.github/skills/`, `AGENTS.md` — loading order and whether submodules are materialised).
2. Which files the Claude iOS `code` feature loads when opened against this repo (`CLAUDE.md`, `AGENTS.md`, `.github/copilot-instructions.md` — confirmed loading order).
3. Whether `AGENTS.md` at the repo root is needed for either agent, and whether ADR-0006 (which deleted it) needs superseding.

Findings stored in `Research/completed/2026-03-28-agent-instruction-loading.md`. ADR updated or superseded if the answer changes the current single-file decision.

### Context

ADR-0006 removed `AGENTS.md` on the assumption that `.github/copilot-instructions.md` was sufficient for all agents. If either the Copilot coding agent or Claude iOS requires `AGENTS.md` to locate instructions reliably, that assumption is wrong. The research item `Research/backlog/2026-03-28-agent-instruction-loading-and-skills-access.md` investigates this.

---

## W-0036

status: open
created: 2026-03-28
updated: 2026-03-28

### Outcome

`.devcontainer/devcontainer.json` exists with: Python 3.11 base image, `postCreateCommand` running `make dev-install && git submodule update --init .github/skills`, GitHub CLI feature. `copilot-setup-steps.yml` exists (if the schema supports it) with the same setup steps. `.github/copilot-instructions.md` contains an explicit setup instruction that causes Claude iOS to run the correct steps before starting work. `research-loop.yml` inline setup steps are consolidated or removed where redundant.

### Context

Three agent entry points exist: (1) Copilot coding agent via assigned GitHub issues, (2) Claude iOS `code` feature, (3) `research-loop.yml` workflow. Each currently handles environment setup differently or not at all. `.devcontainer/devcontainer.json` is absent (W-0004 incorrectly marked done). The research item `Research/backlog/2026-03-28-environment-setup-consistency.md` defines what each agent needs and whether a single file can serve all three.

Blocked on W-0035 (need to know what each agent reads before specifying what to write).

---

## W-0037

status: open
created: 2026-03-28
updated: 2026-03-28

### Outcome

Confirmed, documented answers to:
1. The exact schema and behaviour of `.github/copilot-setup-steps.yml` — what it does, when it runs, what it supports (submodule init, pip install), and whether it replaces or complements `devcontainer.json` for the Copilot coding agent.
2. How Claude iOS respects (or does not respect) environment setup configuration files — what mechanism, if any, causes it to run setup steps before starting work.
3. Whether a single setup declaration file can serve both agents, or whether separate files are required.

Findings stored in `Research/completed/2026-03-28-agent-env-setup-schema.md`. Directly unblocks W-0036 implementation.

### Context

Before writing `.devcontainer/devcontainer.json` and `copilot-setup-steps.yml`, the schema and runtime behaviour of each must be verified. The research item `Research/backlog/2026-03-28-environment-setup-consistency.md` covers this as Q1–Q3.

---

## W-0038

status: open
created: 2026-04-27
updated: 2026-04-27

### Outcome

Confirmed, documented answers to:
1. What are the practical norms from arXiv, SSRN, OSF (Open Science Framework), and registered reports for handling corrections, commentary, replication, and disputes in a file-based corpus?
2. How do Zettelkasten implementations (Obsidian Publish, Roam, Logseq) handle note versioning and amendment?
3. What is the minimum viable design for `replicates:` and `corrects:` relationship types in `## Related Items` to cover the gaps in the current five-type edge vocabulary (`extends`, `contradicts`, `depends-on`, `spawned-from`, `see-also`)?
4. Does the pragmatic versioning model (frontmatter `versions:` array + git history as the diff) provide sufficient auditability, or is a strict arXiv-style vN file approach warranted?

Findings stored in `Research/completed/YYYY-MM-DD-research-item-versioning-norms.md`. An ADR (Architecture Decision Record) is written if the findings change the frontmatter design or output type vocabulary.

### Context

Completed items in this repo are currently edited post-completion (acronym fixes, label corrections, finding revisions) with no formal record of what changed. The proposed design keeps the same file, uses git history as the diff, and adds a `versions:` frontmatter array as the human-readable index (version number, commit SHA, date, progress log path, one-line summary).

This research item validates that design against academic pre-print and PKM (Personal Knowledge Management) norms before the frontmatter schema is locked in. It also evaluates whether `replicates` and `corrects` should join the `## Related Items` relationship vocabulary.

Spawned from design session 2026-04-27 on academic norms for completed research items.

### Notes

Two implementation options for W-0039:

- **Option A (research first):** Complete W-0038 before implementing W-0039. The `versions:` field is low-risk but the relationship vocabulary question is unresolved without evidence.
- **Option B (implement now, validate later):** Implement W-0039 immediately with the pragmatic model. If W-0038 findings contradict the design, an ADR (Architecture Decision Record) supersedes and the schema is updated. The version history itself captures the correction.

---

## W-0039

status: open
created: 2026-04-27
updated: 2026-04-27

### Outcome

1. `Research/_template.md` has a `versions:` array field with sub-fields: `version`, `sha`, `changed`, `progress`, `summary`.
2. `src/research/item.py` `ResearchItem` dataclass has `versions: list[dict]` field; parses cleanly from existing completed items (defaults to empty list when field is absent — no migration of existing files required).
3. `.github/copilot-instructions.md` has an explicit immutability rule: any edit to a completed item's findings, claims, or conclusions requires a new `versions:` entry, a progress log, and SHA (commit hash) populated after the commit. Tag additions and `## Related Items` changes are exempt from this rule.
4. `scripts/build_site.py` renders a version history table on item pages: version number, date, one-line summary, and SHA (commit hash) linked to the GitHub commit URL.
5. Tests in `tests/test_research_cli.py` or a new test file cover: parsing a `versions:` field; defaulting to empty list when the field is absent; correct rendering in the site build (if applicable).

### Context

When completed items are edited there is currently no record of what changed, when, or why. This item implements the design decided 2026-04-27: same file path (no file renaming or archiving), git history as the diff, frontmatter `versions:` array as the human-readable index.

Version numbering convention:
- `1.0` — initial completion
- `1.x` — minor corrections (label fixes, acronym expansions, broken URL replacements, formatting)
- `2.0` — substantive revision (findings changed, conclusions revised, major new evidence added)

Blocked on W-0038 if Option A is chosen; can proceed independently under Option B.

---
