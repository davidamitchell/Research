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

`davidamitchell/Skills` `research/SKILL.md` contains a new §0.5 step: before §1 Question Decomposition, the agent asks "what disciplines, roles, or stakeholders would approach this question differently?" and generates one sub-question per perspective. The step is labelled **§0.5 Perspective Discovery**. `research-prompt.md` in this repo is updated to invoke §0.5 before §1. Existing §0–§7 numbering is preserved; §0.5 is inserted between them.

### Context

STORM (NAACL 2024) demonstrated a +10% improvement in coverage breadth against baseline RAG by surveying related viewpoints before decomposing a question into sub-questions. The current research skill starts directly at §1 Question Decomposition from a single perspective. Adding a perspective-discovery pass increases the breadth of sub-questions generated without changing downstream steps. Requires a PR to `davidamitchell/Skills` then a submodule pointer update here via `sync-skills.yml`.

---

## W-0039

status: open
created: 2026-04-27
updated: 2026-04-27

### Outcome

`research-prompt.md` contains an explicit instruction after §4 Findings: use `sequential_thinking` to take the position of a sceptic or adjacent-domain expert and generate at least two objections to the draft findings. Unresolved objections are recorded in `## Risks, Gaps`. The instruction names `sequential_thinking` by its MCP tool name so the agent calls it correctly.

### Context

The research loop runs a monologue, not a dialogue. STORM's simulated expert conversation surfaces gaps that single-pass question decomposition misses. The `sequential_thinking` MCP server is already configured in `.mcp.json` and is the nearest available equivalent. Adding an adversarial challenge step after drafting findings — before finalising — catches shallow reasoning before the item is committed.

---

## W-0040

status: open
created: 2026-04-27
updated: 2026-04-27

### Outcome

(a) `Research/_template.md` frontmatter contains a new `gaps:` field (YAML list, default `[]`). Each gap is a short string: the open question left unanswered by this item.

(b) A script `scripts/aggregate_gaps.py` reads `gaps:` from all completed items, counts occurrences of identical or near-identical gap strings, and writes `state/gap_registry.json` mapping each gap string to the list of item slugs that raised it and an occurrence count.

(c) `research-prompt.md` contains an instruction: after completing §6 Synthesis, extract 1–5 open questions that the research could not answer and write them into the `gaps:` frontmatter field of the completed item.

(d) Items where a gap appears in three or more completed items are flagged in `gap_registry.json` with `"promote": true`. The research loop prompt instructs the agent to check `gap_registry.json` at the start of a session and create a new backlog item for any gap flagged `promote: true` that does not already have a corresponding backlog item.

Tests cover: template field presence, script output schema, promotion threshold logic.

### Context

~280 instances of gap/risk language exist across completed items but all are inside body text — none are structured data. There is no mechanism to turn "outstanding question X" into a backlog item, and no way to query the gap corpus. This is the biggest structural gap in the research system. The Knowledge Explorer pattern (structured gap register with automatic promotion) is the design to follow. Lightweight: YAML list in frontmatter + a Python aggregator script.

---

## W-0041

status: open
created: 2026-04-27
updated: 2026-04-27

### Outcome

`research-prompt.md` contains an instruction after §4 Findings: before moving to §5, write 3–5 key concepts discovered in this item and their relationships into the memory graph using the `@modelcontextprotocol/server-memory` MCP tools (`create_entities`, `create_relations`, `add_observations`). Each concept is an entity; each relationship between concepts is a relation. The item slug is added as an observation on each entity so provenance is traceable.

A corresponding instruction at §0 Initialise: query the memory graph for entities related to the research question before beginning investigation, to surface what prior sessions already established.

### Context

The `@modelcontextprotocol/server-memory` MCP server is already configured in `.mcp.json` but is not used by the research loop. The loop currently accumulates knowledge in files but does not build a cross-session knowledge graph. The pattern from Letta and persistent memory systems: as each item completes, key concepts and relations are written into the graph; subsequent sessions query the graph first. This converts the corpus from passive storage into an active, queryable knowledge base. Implementation is ~10 lines of prompt instruction using existing infrastructure.

---

## W-0042

status: open
created: 2026-04-27
updated: 2026-04-27

### Outcome

`research-prompt.md` contains an explicit step in §2 Investigation: for any claim designated as an anchor finding (a claim that a Key Finding will directly depend on), search arXiv using `arxiv_mcp_server` to locate the primary paper that makes that claim, verify the paper says what the claim asserts, and record the arXiv ID in the source list. Claims that cannot be verified against primary literature are downgraded from `[fact]` to `[inference]` with a note.

### Context

The `arxiv_mcp_server` MCP is configured in `.mcp.json` but the research prompt does not instruct the agent to use it for claim verification. Academic research systems use citation verification (claim → find the paper → check what the paper actually says) rather than multi-source frequency agreement. This is a higher-fidelity verification heuristic. The step applies only to anchor claims — those that Key Findings directly depend on — to keep session time bounded.

---

## W-0043

status: done
created: 2026-04-27
updated: 2026-04-28

### Outcome

(a) A canonical tag vocabulary is defined in `docs/tag-vocabulary.md`. It maps synonym clusters to a single canonical form. At minimum, it resolves: `ai` / `ai-agents` / `agentic-ai` / `agentic-systems` / `agents` → canonical; `llm` / `large-language-model` / `llm-agent` → canonical; and the top 20 singleton-or-near-synonym clusters identified by inspection.

(b) A script `scripts/canonicalise_tags.py` reads the vocabulary map and rewrites `tags:` frontmatter in all files under `Research/completed/`, `Research/backlog/`, and `Research/in-progress/` to use canonical forms only.

(c) `Research/_template.md` references `docs/tag-vocabulary.md` in a comment on the `tags:` field.

(d) `research-prompt.md` includes an instruction: when assigning tags, consult `docs/tag-vocabulary.md` and use only canonical forms.

Tests cover: vocabulary file exists and is valid YAML, script produces correct output on a fixture file, no new singleton tags are introduced by the script.

### Context

798 unique tags exist across ~180 completed items (~4.4 per item). The majority appear only once. Near-synonyms proliferate with no canonical form and no hierarchy. Tags are currently useless for navigation at scale. This is a high-priority fix because the static site tag pages are the primary navigation mechanism.

---

## W-0044

status: done
created: 2026-04-27
updated: 2026-04-28

### Outcome

`Research/_template.md` frontmatter contains three new fields:
- `cites: []` — list of item slugs this item directly depends on or quotes
- `related: []` — list of item slugs that are thematically connected
- `superseded_by: ~` — slug of a later item that overrides or replaces this item's conclusions (null if not superseded)

`research-prompt.md` instructs the agent to populate these fields during §0 Initialise (check completed corpus for prior related work) and §6 Synthesis (record which items this one cites or is related to).

`scripts/build_site.py` reads `cites:` and `related:` from frontmatter and renders them on item pages as structured link lists, in addition to the existing tag-overlap-based related items. `superseded_by:` renders as a banner warning on the item page.

Tests cover: frontmatter parsing of new fields, site builder renders cites/related/superseded correctly.

### Context

Cross-references currently exist only as inline prose. There is no `cites:` or `related:` in the frontmatter schema. A citation graph cannot be built; "what items does this one depend on?" cannot be answered programmatically. The knowledge-linking research item (`2026-03-03-knowledge-linking-connected-corpus.md`) established the relationship types (`extends`, `contradicts`, `depends-on`, `spawned-from`, `see-also`) and the auto-detection approach. This item implements the structured frontmatter fields that make those relationships machine-readable.

---

## W-0045

status: done
created: 2026-04-27
updated: 2026-04-28

### Outcome

(a) `Research/_template.md` frontmatter contains `superseded_by: ~` (covered by W-0044) and a new `supersedes: ~` field — the slug of an older item that this item replaces or materially updates.

(b) `scripts/build_site.py` renders a banner on any item where `superseded_by:` is set, linking to the superseding item. Items with a non-null `superseded_by:` are visually marked in browse/tag pages.

(c) `research-prompt.md` instructs the agent: when completing an item, check whether any existing completed item is materially contradicted or superseded by the new findings; if so, set `supersedes:` on the new item and `superseded_by:` on the old item and commit both changes.

### Context

Older items may be contradicted or superseded by newer ones with no signal to the reader. A reader of a 2026-02 item gets no indication that 20 subsequent items have refined or overturned parts of it. Freshness signalling requires: (1) a frontmatter field pair (`supersedes`/`superseded_by`), (2) a site rendering change, and (3) a prompt instruction. Depends on W-0044 for the frontmatter schema extension pattern.

---

## W-0046

status: done
created: 2026-04-27
updated: 2026-04-28

### Outcome

`Research/_template.md` frontmatter contains a new `item_type: primary` field with allowed values `primary | synthesis`. Items produced by a single research session answering a specific question use `primary`. Items produced by cross-item integration (combining findings from multiple completed items) use `synthesis`.

`research-prompt.md` instructs the agent: set `item_type: synthesis` when the research question explicitly asks to integrate or compare findings across existing completed items; otherwise set `item_type: primary`.

`scripts/build_site.py` renders `item_type: synthesis` items with a distinct visual indicator on browse and tag pages.

`src/research/item.py` parses `item_type` and `python -m src.main research list` displays it.

Tests cover: frontmatter parsing, CLI output, site builder rendering.

### Context

`output: [knowledge]` currently covers everything from a narrow factual lookup to a major multi-week synthesis. There is no distinction between primary research (answering a specific question) and secondary synthesis (integrating findings across items). The research loop treats all items identically. Differentiating item types enables filtering ("show me only synthesis items"), drives the research prompt to apply the synthesis skill for integration work, and makes the corpus navigable by depth.

---

## W-0047

status: done
created: 2026-04-27
updated: 2026-04-28

### Outcome

`Research/_template.md` frontmatter contains a new `confidence: medium` field with allowed values `high | medium | low` and definitions in a comment:
- `high` — all key findings supported by primary sources; no unresolved contradictions
- `medium` — key findings supported by secondary sources or inference chains with low uncertainty
- `low` — key findings rely on a single source, significant gaps remain, or multiple unresolved contradictions exist

`research-prompt.md` instructs the agent to set `confidence:` at §7 Recursive Review based on the evidence quality of the Key Findings taken as a whole.

`scripts/build_site.py` renders the confidence grade on item pages and allows filtering by confidence in browse/tag pages.

`src/research/item.py` parses `confidence` and `python -m src.main research list` displays it.

Tests cover: frontmatter parsing, CLI output, site builder rendering.

### Context

Individual claims carry `[fact]`/`[inference]`/`[assumption]` labels (good), but there is no overall confidence or evidence grade for an item as a whole. A reader cannot filter "show me only high-confidence findings." An item with 20 `[assumption]` labels and an item with 20 `[fact]` labels both appear identical in browse/tag navigation. Item-level confidence grades make corpus reliability visible at a glance.

---

## W-0048

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

Two implementation options for W-0049:

- **Option A (research first):** Complete W-0048 before implementing W-0049. The `versions:` field is low-risk but the relationship vocabulary question is unresolved without evidence.
- **Option B (implement now, validate later):** Implement W-0049 immediately with the pragmatic model. If W-0048 findings contradict the design, an ADR (Architecture Decision Record) supersedes and the schema is updated. The version history itself captures the correction.

---

## W-0049

status: done
created: 2026-04-27
updated: 2026-04-28

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

Blocked on W-0048 if Option A is chosen; can proceed independently under Option B.

---

## W-0050

status: done
created: 2026-04-27
updated: 2026-04-27

### Outcome

`docs/backlog.html` is generated by `scripts/build_site.py` and lists all items in `Research/backlog/` as non-linkable cards showing title, date, priority badge, tags, and research question excerpt. A "Backlog" nav link is added to all pages. The `build_site.yml` workflow triggers on changes to `Research/backlog/**`.

### Context

Epic 2 — Static site. Makes the outstanding research question backlog visible on the published site without requiring access to the GitHub repository. Companion page to `all-items.html`.
## W-0051

status: done
created: 2026-04-27
updated: 2026-05-05

### Outcome

A synthesis workflow is implemented end-to-end:

- `Knowledge/` directory created at repo root for cross-item synthesis artifacts (distinct from `Research/completed/` primary research items)
- `Knowledge/_template.md` — synthesis item template with sections: Cluster (list of source item slugs), Synthesis Question, Perspectives Considered, Cross-Item Findings, Contradictions and Tensions, Confidence Map, Open Questions
- `synthesis-prompt.md` — synthesis agent prompt analogous to `research-prompt.md`; instructs the agent to read all source items via `filesystem` MCP, apply multi-perspective synthesis (not concatenation), identify contradictions across items, and populate `cites:` with source slugs
- `.github/workflows/synthesis-loop.yml` — manual-trigger-only workflow (`workflow_dispatch`) accepting `source_items` (comma-separated slugs) and `synthesis_question` inputs; feeds `synthesis-prompt.md` to the Copilot CLI; never runs on schedule
- Site (`build_site.py`) updated to render `Knowledge/` items alongside `Research/completed/` items
- `item_type: synthesis` items in `Research/` are excluded from the autonomous research loop (enforced by W-0046 type field logic)

Blocked on W-0046 (item_type field) and W-0044 (cites field). ADR required.

### Context

The current system produces primary research items (single-question answers) but has no mechanism for producing knowledge artifacts that integrate findings across multiple items. This is the systematic review equivalent — a distinct output type with its own methodology. Without it, the gap between accumulated research and usable knowledge cannot be closed. The synthesis workflow is the prerequisite for the authoring workflow (W-0052).

---

## W-0052

status: open
created: 2026-04-27
updated: 2026-04-27

### Outcome

An authoring workflow is implemented for producing finished papers and framework documents:

- `Outputs/papers/` and `Outputs/frameworks/` directories created at repo root
- `Outputs/_paper-template.md` — paper template: Abstract, Introduction, Background (with cites to synthesis and primary items), Argument, Evidence, Implications, Conclusion, References
- `Outputs/_framework-template.md` — framework template: Purpose, Scope, Conditions for Use, Decision Criteria or Maturity Levels, Worked Examples, Limitations, References
- `authoring-prompt.md` — authoring agent prompt; instructs the agent to draw on specified synthesis and primary items, apply the `strategy-author` and `strategic-persuasion` skills, produce a finished draft, and populate the references section from `cites:` fields
- `.github/workflows/authoring-loop.yml` — manual-trigger-only workflow accepting `output_type` (paper | framework), `title`, and `source_items` inputs
- Site updated to render `Outputs/` items alongside research and knowledge items

Blocked on W-0051 (synthesis workflow must exist before authoring draws on synthesis items — W-0051 is now done). ADR required.

### Context

The research corpus and synthesis layer produce material that has direct value as publishable articles and practical frameworks. Currently no workflow exists to take that material and produce a finished artifact. The authoring workflow closes the last gap in the DIKW chain: data → information (primary research) → knowledge (synthesis) → wisdom (authored output). Papers and frameworks are the deliverable form that makes the research useful to audiences beyond the researcher.

---

## W-0053

status: done
created: 2026-04-27
updated: 2026-04-28

### Outcome

A tag co-occurrence review workflow complements W-0043's canonical vocabulary with an evidence-driven discovery mechanism:

- `scripts/tag_report.py` scans all `Research/completed/*.md` and `Research/backlog/*.md` and computes: tag frequency, tag co-occurrence matrix, near-duplicate candidates (Levenshtein distance ≤ 2 or prefix/suffix overlap ≥ 0.8), singleton tags (appear only once), and strong co-occurrence pairs (appear together in >80% of each other's occurrences — strong synonymy signal)
- Output written to `state/tag_report.json` and human-readable `state/tag_report.md`
- A workflow (`tag-review.yml`) runs monthly and on `workflow_dispatch`, commits the updated report, and opens a GitHub issue listing near-duplicate and singleton candidates for human review
- The vocabulary in W-0043 is populated by reviewing the tag report output rather than by manual curation from scratch — the co-occurrence data drives what gets added to the canonical map

### Context

W-0043 defines the canonical tag vocabulary as the goal; W-0053 provides the evidence base for building and maintaining it without predefined assumptions. Running the co-occurrence report first means the vocabulary reflects what tags actually cluster in the corpus rather than what seems reasonable in advance. This is the difference between top-down taxonomy (W-0043 alone) and bottom-up taxonomy with human curation (W-0043 + W-0053 together). The intent is that W-0053 runs first, the human reviews the report, and the W-0043 vocabulary is populated from that evidence. W-0053 should be implemented and run before W-0043 is executed.

## W-0054

status: open
created: 2026-04-27
updated: 2026-04-27

### Outcome

The research item picker enforces actual dependency ordering:

- A `depends_on: []` frontmatter field is added to `Research/_template.md` — lists slugs of items that must be in `Research/completed/` before this item can be picked
- `cmd_pick` in `src/research/cli.py` filters out any backlog item where one or more `depends_on` slugs are not present in `Research/completed/`
- The `ResearchItem` dataclass is extended with `depends_on: list[str]`
- The existing `blocks` field is retained as-is (it signals "I block these items" for priority sorting); `depends_on` is the inverse (it signals "I need these items done first")
- Tests cover: item with satisfied dependencies is eligible; item with unsatisfied dependency is excluded; item with empty `depends_on` is always eligible
- `copilot-instructions.md` updated to document both fields and their distinct semantics

ADR required (picker behaviour change — items can now be excluded from picking, not just deprioritised).

### Context

The current picker uses the `blocks` field only as a priority sort tiebreaker — items with non-empty `blocks` lists are sorted higher, but items listed in `blocks` are not prevented from being picked before their prerequisites complete. Synthesis items that depend on multiple primary items being done first can be auto-started before their sources are available. The `depends_on` field provides actual gating: if prerequisites are not complete, the item is invisible to the picker.

---

## W-0055

status: open
created: 2026-04-27
updated: 2026-04-27

### Outcome

`BACKLOG.md` is split into per-item files under a `backlog-items/` directory (or similar). Each W-XXXX item becomes its own file: `backlog-items/W-0001.md`, `backlog-items/W-0002.md`, etc. A single `BACKLOG.md` is generated from these files (or `BACKLOG.md` is replaced with an index linking to them).

This eliminates the W-number collision class of merge conflicts: every PR that adds a new item creates a new file rather than appending to a shared file. Two PRs open simultaneously cannot conflict as long as they choose different filenames.

Migration path: convert existing items, update `research-loop.yml` to write to the per-item format, update any tooling that reads `BACKLOG.md`.

### Context

W-number collisions happen whenever a feature PR stays open while the research loop appends a new W-item to `BACKLOG.md` on `main`. Both branches independently compute "next number = last number + 1" and choose the same value. The conflict is structurally inevitable given the current monolithic append model. Splitting to per-item files is the root-cause fix documented in the Known Recurring Patterns table of `.github/copilot-instructions.md`.

---

---

## W-0056

status: open
created: 2026-04-29
updated: 2026-04-29

### Outcome

All 215 completed research items have their `## Sources` section display names updated to the canonical `inline-citation` format documented in `Research/_template.md`:

- Papers with named authors: `[Smith et al. (YYYY) Title](url)` or `[Surname, A.K. (YYYY). Title](url)`
- Docs / standards / org pages: `[Organisation Title](url)` (no bare colon-separated format)

The migration can be verified by running `scripts/extract_metadata.py` and `scripts/build_site.py` and confirming that ≥95% of citation chips on generated pages display `Author (YYYY)` or a recognisable org name rather than a bare URL domain.

### Context

As of 2026-04-29, the `_extract_citation_label` function in `build_site.py` achieves 89% year-extraction rate from existing display names. The remaining 11% fall back to URL-domain labels (e.g. `Edelmansmithfield (n.d.)`, `Prnewswire (n.d.)`). Updating source display names to the canonical format would push coverage to ~100% and make citation chips more informative on the published site. This is a bulk manual migration (2142 source entries across 215 files).

---

## W-0057

status: open
created: 2026-04-29
updated: 2026-04-29

### Outcome

`scripts/build_site.py` includes a `normalize_source_display_name(display_name: str) -> str` utility that rewrites common legacy source line formats to the canonical `inline-citation` display name format without human intervention:

- `Surname, A.K. (YYYY). Title` → `Surname (YYYY) Title`
- `Org: description (YYYY)` → `Org (YYYY) Description`
- `bare-url-only` lines → unchanged (no display name to normalise)

A `scripts/migrate_source_display_names.py` script applies this to all `Research/completed/*.md` files and creates a git commit with a summary of changes. The migration is idempotent (already-canonical names are unchanged).

### Context

W-0056 tracks the manual migration. W-0057 tracks the automated approach. The automated approach is worthwhile because 2142 entries would take significant manual time and introduce inconsistencies. A script that converts the most common patterns (80%+ of entries) and leaves complex cases for manual review is a better lever.


## W-0059

status: done
created: 2026-05-03
updated: 2026-05-05

### Outcome

A process evaluation harness is implemented that samples completed research items and runs them through a specified process step for comparison:

- `scripts/eval_harness.py` — core harness script:
  - `sample_items(completed_dir, n, seed)` — random sample with optional seed for reproducibility
  - `extract_question()`, `extract_approach()`, `extract_key_findings()` — section text extraction from completed item Markdown
  - Three named process steps with full prompt templates: `perspective-discovery` (§0.5b), `question-decomposition` (§1), `adversarial-challenge` (§4.5)
  - `build_process_prompt(process_name, context)` — fills prompt template from item context
  - `score_structural_completeness()` — checks required output patterns (0.0–1.0)
  - `score_coverage_overlap()` — word-level Jaccard similarity between generated and original content (0.0–1.0)
  - `score_perspective_slots()` — checks all four STORM lens labels present (perspective-discovery only)
  - `generate_eval_report()` + `format_markdown_report()` — JSON + Markdown report to `state/eval_reports/`
  - CLI: `--process`, `--n`, `--seed`, `--completed-dir`, `--responses-dir`, `--output-dir`, `--list-processes`, `--dump-prompts-dir`
- `tests/test_eval_harness.py` — 60 unit tests covering extraction, sampling, prompt building, scoring, report generation, CLI, and prompt dump
- `.github/workflows/eval-harness.yml` — manual workflow dispatch with `process`, `n`, `seed` inputs; commits report to `state/eval_reports/`; uses `ref: ${{ github.ref }}` so it can be triggered from any branch
- `.github/workflows/eval-loop.yml` — Copilot-powered evaluation loop mirroring `research-loop.yml` safety controls (HARD_MAX_ITERATIONS=10, FAILURE_THRESHOLD=2, 60-min job timeout)

**Workflow:**
1. Run harness to generate prompt bundle: `python scripts/eval_harness.py --process perspective-discovery --n 5 --seed 42`
2. Paste each prompt into an LLM; save responses as `<slug>.txt` in a directory
3. Re-run with `--responses-dir` to score responses against original items
4. Report compares structural completeness, coverage overlap (Jaccard), and process-specific metrics

### Context

When new or modified process steps (such as §0.5b Perspective Discovery) are proposed, evaluating them against a random sample of past research questions gives evidence about whether they would improve investigation coverage and quality. Without the harness, evaluation is purely subjective. The harness produces reproducible, seeded prompt bundles and deterministic comparison scores, enabling A/B comparison of process variants.

## W-0060

status: open
created: 2026-05-09
updated: 2026-05-09

### Outcome

Each completed research item has a dedicated GH Pages page that renders its metadata fields — `confidence`, `item_type`, `cites`, `related`, `superseded_by` — as structured, human-readable content rather than raw YAML frontmatter:

- `scripts/build_site.py` updated: individual item pages include a metadata sidebar or panel showing each field with a human label (e.g. "Confidence: High", "Type: Primary", "Cites: [linked list]", "Related: [linked list]", "Superseded by: [link]")
- `cites` and `related` slugs are rendered as hyperlinks to the corresponding item pages; `superseded_by` renders as a link with a visual deprecation indicator
- `item_type` and `confidence` use styled badges (e.g. colour-coded pills) consistent with the existing site design
- Fields that are null or empty are omitted from the rendered output (not shown as blank)
- Tests cover: metadata panel renders correct labels, slugs resolve to correct links, null fields are omitted, deprecated item shows deprecation indicator

### Context

Current individual item pages show only the Markdown body. Readers cannot see relationship metadata (cites, related, superseded_by) or quality signals (confidence, item_type) without reading the raw frontmatter. Making these fields visible on rendered pages enables readers to assess item quality, trace citation chains, and navigate the corpus without accessing GitHub directly. Companion to W-0061 (synthesis candidates page).

---

## W-0061

status: open
created: 2026-05-09
updated: 2026-05-11

### Outcome

The GH Pages site includes a synthesis candidates page at `docs/synthesis-candidates.html` listing groups of completed items that share two or more `ai_themes` values:

- `scripts/build_site.py` updated: a `generate_synthesis_candidates()` function groups completed items by shared `ai_themes` values (≥2 shared themes), ranks clusters by cluster size and average item confidence, and renders them as a browsable page
- Each cluster card shows: shared `ai_themes`, item count, list of item titles linked to their individual pages, and a "Synthesise this cluster" call-to-action linking to the `synthesis-loop.yml` dispatch instructions
- The page is linked from the site nav alongside "All Items", "Backlog", and "Tags"
- A "Synthesis Candidates" link is added to all site pages in the nav
- The workflow trigger (`build_site.yml`) already covers `Research/completed/**`; no workflow changes needed
- Tests cover: cluster computation returns correct groups, minimum-theme threshold is respected, ranking is deterministic, nav link is present in all page templates

### Context

The synthesis workflow (W-0051) exists but has no discovery mechanism — a reader must manually identify which items cluster well for synthesis. The synthesis candidates page surfaces this automatically.

**Revised clustering signal (2026-05-11):** Original design used tag co-occurrence (depending on W-0043 canonical vocabulary and W-0053 tag report). With `ai_themes` enrichment (W-0069) providing a clean 16-item controlled-vocabulary classification on all items, `ai_themes` overlap is a superior clustering signal: the vocabulary is already controlled, no near-synonym noise, and all 300+ items will be classified after the backfill. The W-0043/W-0053 dependency for this item is removed. Tag co-occurrence can still be used as a secondary signal once W-0062 completes.

Blocked on W-0069 (ai_themes backfill) and W-0070 (ai_themes wired into site).

---

## W-0062

status: open
created: 2026-05-09
updated: 2026-05-09

### Outcome

All tags across `Research/completed/` and `Research/backlog/` conform to the canonical vocabulary defined in `docs/tag-vocabulary.md`. The tag report (`scripts/tag_report.py`) shows zero promotion candidates after the run:

- `scripts/canonicalise_tags.py` is run against the full corpus; any tags not yet in the vocabulary map are either added to `docs/tag-vocabulary.md` as canonical entries or rewritten to an existing canonical form
- After canonicalisation, `scripts/tag_report.py` is re-run; the output `state/tag_report.md` shows zero near-duplicate candidates and zero singleton-promotion candidates
- The `tag-review.yml` workflow is triggered to confirm the clean state and close any open tag-review issues
- A commit records the canonical state with message `tags: canonicalise full corpus — zero promotion candidates`
- Tests confirm: no file in `Research/completed/` or `Research/backlog/` contains a tag that is an alias in `docs/tag-vocabulary.md`

### Context

W-0043 (canonical vocabulary) and W-0053 (tag report script) are done but the corpus has not been fully re-canonicalised since the vocabulary was defined. Tags accumulate with every new completed item. This slice closes the loop: running canonicalisation to completion so that the tag report is a green signal rather than an ongoing list of candidates. Blocked on W-0043 and W-0053 (both done).

---

## W-0063

status: open
created: 2026-05-09
updated: 2026-05-09

### Outcome

All existing completed items in `Research/completed/` are reviewed for structural correctness and corrected in place where they fail:

- A `scripts/item_audit.py` script checks every completed item for: all required frontmatter fields present and non-null, `status: completed`, at least one entry in `output:`, `## Findings` section present and non-empty, `## Sources` section present with at least one URL, no hollow filler phrases (using the `remove-ai-slop` skill vocabulary), citations in canonical `Author (Year)` suffix format
- The script outputs a machine-readable audit report to `state/item_audit.json` and a human-readable summary to `state/item_audit.md`
- Items that fail one or more checks are corrected: missing fields added, hollow prose removed or rewritten, malformed citations reformatted
- Every corrected item receives a `versions:` frontmatter entry recording: `version`, `sha` (populated after commit), `changed` (today's date), `progress` path, and a one-line `summary` of what was corrected
- Tests cover: audit script identifies known failures in fixture items, corrected items pass re-audit, versions entry format is validated

### Context

The corpus has grown to ~287 completed items, many produced before current quality standards were established. Structural inconsistencies (missing fields, hollow prose, malformed citations) degrade the published site and undermine the research-reviewer signal. A systematic audit and correction pass is needed before the quality bar can be considered enforced rather than aspirational. Blocked on W-0067 (citation-standards.md) for the citation-format check.

---

## W-0064

status: open
created: 2026-05-09
updated: 2026-05-09

### Outcome

The site generator, item template, and research prompt are inspected for the root cause of repeated or near-identical content appearing across generated pages or completed items. The cause is documented and a targeted fix is applied:

- A `scripts/similarity_report.py` script computes pairwise cosine similarity between completed items using TF-IDF on the `## Findings` section text; items with similarity > 0.85 are flagged as near-duplicates
- The similarity report is written to `state/similarity_report.md` and committed
- The three likely root causes are investigated: (a) `research-prompt.md` contains boilerplate that agents copy verbatim, (b) `Research/_template.md` placeholder text survives into completed items, (c) `build_site.py` duplicates content blocks across pages
- Each identified root cause is documented in a progress note and fixed: prompt boilerplate replaced with instructions, template placeholders made unambiguous, site generator deduplication added
- An ADR is written if the fix involves a structural change to the template or prompt

### Context

Repeated content across completed items or site pages reduces the signal-to-noise ratio of the corpus and makes the published site appear low-quality. It also inflates the synthesis candidates page with false clusters (items that share text rather than concepts). Identifying and fixing the root cause prevents new items from reproducing the pattern. This is a maintenance slice that enables reliable quality signals downstream.

---

## W-0065

status: open
created: 2026-05-09
updated: 2026-05-09

### Outcome

The `research-question` skill (in `davidamitchell/Skills`) is evaluated against a sample of past backlog items and any structural weaknesses are corrected:

- Using `scripts/eval_harness.py` (W-0059), a sample of 10 past backlog items is drawn; the skill's five-test quality check (Specific, Answerable, Scoped, Motivated, Decomposable) is applied to each item's research question
- A structured evaluation report is written to `state/eval_reports/research-question-skill-eval.md` with per-item pass/fail verdicts and failure reasons
- Structural weaknesses identified (e.g. the SASM-D tests are underspecified, the rewrite guidance is vague, scope constraints are not enforced) are documented as findings
- A PR is opened in `davidamitchell/Skills` correcting the `research-question` skill's SKILL.md — updated tests, clearer rewrite criteria, explicit scope-constraint enforcement
- After the Skills PR merges, the submodule pointer in this repo is advanced and the `copilot-instructions.md` updated if the skill invocation instructions change

### Context

The `research-question` skill gates every new backlog item's quality but has never been formally evaluated against real outputs. The eval harness (W-0059) now provides the mechanism. Without this evaluation, the skill may be producing questions that pass its own tests but are still too broad, unanswerable in a single session, or lack binding constraints — leading to low-quality research items that are expensive to produce and hard to synthesise. Blocked on W-0059 (eval harness — done).

---

## W-0066

status: open
created: 2026-05-09
updated: 2026-05-09

### Outcome

The `research-reviewer` skill and the `research-review.yml` workflow together produce a reliable pass/fail signal. False passes and false failures are identified and corrected:

- A sample of 10 completed items is drawn: 5 known-good items (high confidence, full citations, no hollow prose) and 5 known-weak items (missing fields, uncited claims, hollow phrases)
- Each item is run through `research-review.yml` and the OVERALL/VIOLATION log lines are captured (per the established pattern: workflow success alone does not confirm item-level review pass)
- False passes (known-weak item receives OVERALL: PASS) and false failures (known-good item receives OVERALL: FAIL) are recorded with the specific check that produced the wrong result
- The `research-reviewer` skill's check rules are corrected: tightened where false passes occur, relaxed or clarified where false failures occur
- A PR is opened in `davidamitchell/Skills` with the corrected skill; the submodule pointer in this repo is advanced after merge
- The `research-review.yml` workflow is updated if any workflow-level changes (not just skill-level) are needed to surface item-level results reliably

### Context

The research-review workflow currently auto-passes some items without running meaningful checks (this is a known failure mode: workflow success hides item-level review failures). A systematic evaluation against known-good and known-weak items is the only way to calibrate the skill so its pass/fail signal is trustworthy enough to gate the `research-loop.yml` completion step.

---

## W-0067

status: open
created: 2026-05-09
updated: 2026-05-09

### Outcome

A `docs/citation-standards.md` file exists, defines the required citation format with examples, and is referenced from both `research-prompt.md` and `Research/_template.md`. The CI review step fails any completed item that contains an uncited factual claim:

- `docs/citation-standards.md` is created: defines the canonical citation format (`Author (Year) Title` suffix style), shows five worked examples (paper with named authors, org documentation, web page, dataset, preprint), and lists prohibited formats (bare URLs as the only citation, footnote-style, inline author-date without source URL)
- `Research/_template.md` updated: a comment on the `## Sources` and `## Findings` sections links to `docs/citation-standards.md`
- `research-prompt.md` updated: Step 6 companion checks reference `docs/citation-standards.md` explicitly; the uncited-claim check is strengthened from advisory to blocking
- A `scripts/citation_check.py` script scans completed items and flags: factual claims (sentences containing numbers, percentages, named entities, or study references) that lack a trailing citation, and sources in `## Sources` that have no matching citation in `## Findings`
- `ci.yml` updated: `citation_check.py` runs as a check on any PR that modifies `Research/completed/**`; the step fails if any item in the PR has uncited factual claims
- Tests cover: citation check correctly identifies uncited claims in fixture items, canonical format is accepted, prohibited formats are rejected

### Context

Uncited factual claims are the most common quality failure in completed items. The `citation-discipline` skill exists but is advisory; the research-prompt citation check is advisory. Making citation enforcement automated and blocking in CI removes the human review burden and ensures the standard is actually enforced rather than aspirationally stated. Blocked on W-0063 (corpus audit) — citation-check results are only meaningful after the corpus has been corrected to a known baseline.

---

## W-0068

status: open
created: 2026-05-09
updated: 2026-05-09

### Outcome

The synthesis and authoring workflows produce at least one completed synthesis item that could withstand peer review — claims sourced, speculation labelled, contradictions surfaced, argument coherent across items:

- A topic cluster is selected from the synthesis candidates page (W-0061) or manually identified if W-0061 is not yet done: the cluster should have ≥5 completed items with overlapping tags
- `synthesis-loop.yml` is triggered for the selected cluster; the resulting synthesis item in `Knowledge/` is reviewed against the following criteria: every key finding links to ≥1 source item via `cites:`, no claim appears without a confidence label, contradictions between source items are explicitly named in the "Contradictions and Tensions" section, the synthesis question is answered directly in the Executive Summary
- If the first synthesis fails the review, the prompt or workflow is corrected and re-run until a passing synthesis is produced
- The passing synthesis item is committed and its path recorded in this backlog item's Outcome
- A progress note documents which criteria passed and which required iteration

### Context

W-0051 (synthesis workflow) and W-0052 (authoring workflow) exist but have never been validated against a quality bar. "The workflow exists" is not the same as "the workflow produces useful outputs." This slice provides the end-to-end proof that the synthesis pipeline can produce a knowledge artifact that meets the peer-review standard defined by the `citation-discipline`, `speculation-control`, and `remove-ai-slop` skills. Blocked on W-0051 (synthesis workflow — done) and preferably on W-0061 (synthesis candidates page) for cluster discovery.

---

## W-0069

status: ready
created: 2026-05-11
updated: 2026-05-11

### Outcome

All completed research items carry an `ai_themes` frontmatter field drawn from the 16-item controlled vocabulary, and the enrichment pipeline is running on `main`:

- Branch `claude/update-gemini-models-y7wIV` is merged to `main`; `src/pipeline/_gemini.py`, `scripts/enrich_items.py`, and `.github/workflows/enrich-items.yml` are present on `main`
- The `Enrich Items with AI Themes` workflow is triggered in backfill mode with `max_items: 297`; it runs to completion (or to quota exhaustion, leaving a checkpoint)
- Every completed item in `Research/completed/` either has `ai_themes: [...]` set or has been attempted (quota exhaustion is the only acceptable reason for absence)
- `make check` and `pytest` pass on `main` post-merge

### Context

`src/pipeline/_gemini.py` implements the Gemini client factory, adaptive rate limiter (`_RateLimiter`), and model cascade (`_ModelCascade`) ported from `davidamitchell/Latest-developments-`. `scripts/enrich_items.py` adds `ai_themes` to completed items idempotently. The branch has 47 passing unit tests, a clean ruff check, ADR-0015, and the `GEMINI_API_KEY` secret is confirmed present in the repository. This is the prerequisite for W-0070 and W-0061.

---

## W-0070

status: open
created: 2026-05-11
updated: 2026-05-11

### Outcome

The GH Pages site exposes `ai_themes` as a navigable dimension: 16 theme index pages, per-item theme badges, and related-by-theme links on each item page:

- `scripts/build_site.py` updated:
  - 16 theme pages at `docs/themes/<theme-slug>.html`, each listing all items carrying that theme, sorted by date descending; structured identically to existing tag pages
  - Each item page shows `ai_themes` as styled badges (consistent with existing tag badges) linking to the corresponding theme page
  - The "Related Items" section on each item page gains a "Related by theme" subsection listing items that share ≥2 `ai_themes` values with the current item, capped at 5 items
  - A "Themes" nav link is added to all pages, linking to a `docs/themes/index.html` that lists all 16 themes with item counts
- `build_site.yml` trigger already covers `Research/completed/**`; no workflow changes needed
- Tests cover: theme pages render for all 16 themes, item badges link correctly, related-by-theme returns items with ≥2 shared themes, items with no `ai_themes` degrade gracefully (field absent → no badges, no related-by-theme)

### Context

Once W-0069 (backfill) is done, every item has `ai_themes` set but the site renders none of it — the enrichment is invisible. This item makes it visible and useful. Theme pages give readers a cleaner navigation layer than the 935-tag tag pages (643 of which are singletons). The related-by-theme links improve cross-item discovery without requiring manual `related:` frontmatter. Prerequisite for W-0061 (synthesis candidates using `ai_themes` clusters). Blocked on W-0069.

---

## W-0071

status: open
created: 2026-05-13
updated: 2026-05-13

### Outcome

Graph capability backlog is explicitly scoped and sequenced using existing completed research and current open work:

1. **Review backlog** — map overlaps and dependencies across W-0034, W-0044, W-0051, W-0061, and W-0070 so graph work does not duplicate existing related-items/thread/theme features.
2. **Understand research** — extract design constraints from completed research on knowledge linking and map architecture (`2026-03-03-knowledge-linking-connected-corpus.md`, `2026-05-02-cross-item-synthesis-knowledge-map-architecture.md`).
3. **Design** — produce a graph model that is file-based and GitHub Pages compatible, with traceable edges and explicit provenance.
4. **Review design** — run a design review pass (correctness, maintainability, constraints fit) before implementation.
5. **High-level backlog items** — capture implementation epics for data model/export, GitHub Pages user interface, and quality gates.
6. **Refine backlog items** — split epics into small, testable slices with acceptance criteria and dependencies.
7. **Review whole backlog and adjust sequencing** — ensure graph items are ordered relative to existing synthesis/theme work and that blocked relationships are explicit.

### Context

This item is the backlog-construction slice requested by the issue. It does **not** implement graph functionality; it defines and sequences the work so implementation can proceed with low rework risk.

---

## W-0072

status: open
created: 2026-05-13
updated: 2026-05-13

### Outcome

`scripts/build_site.py` produces a graph artifact for the published corpus (for example `docs/data/graph.json`) with explicit provenance and baseline weighting:

- Nodes represent published items (`Research/completed/` and `Knowledge/`) with slug, title, type, and URL.
- Edges represent machine-readable relationships (`cites`, `related`, and other explicitly supported relationship sources already in the corpus).
- Every edge includes a `weight` field initialized to `1`.
- Every edge includes traceability fields showing exactly where it came from (source item slug, relationship field/type, and evidence reference needed to explain the edge in the user interface).
- Tests verify deterministic output and required schema fields.

### Context

Current site generation computes relationship links for rendering but does not expose a first-class traceable graph artifact with weighted edges. This is the minimum viable graph substrate.

`build_site.py` already builds an in-memory relationship graph (line ~2965, `"Building relationship graph…"`) and loads `cites`/`related_slugs` per item. Exporting to JSON is a serialization step on data that already exists — do not re-derive the graph from scratch.

**Build watch-outs:**
- `docs/data/` is inside `docs/` which is auto-generated and must never be committed on a feature branch. The `build_site.yml` workflow is the sole write path. Verify the artifact directory is created inside the existing `build_site.py` `main()` function, after the `DOCS_DIR.mkdir(exist_ok=True)` call at line ~2998, so it is always regenerated on a clean build.
- Tag-filtered items: `build_site.py` drops singleton tags before building links (line ~2960). The graph artifact must be serialized after this filter runs, or node metadata will be inconsistent with what the site renders.
- `docs/` must not be staged or committed on the implementing branch. Run `git status` before every commit and confirm no `docs/` paths appear.

Blocked on W-0071.

---

## W-0073

status: open
created: 2026-05-13
updated: 2026-05-13

### Outcome

GitHub Pages includes a graph view that is traceable in the front end:

- A dedicated graph page is generated and linked from site navigation.
- The page loads the generated graph artifact and renders nodes/edges in a static-site-friendly way.
- Selecting an edge reveals provenance (why the edge exists, where it came from, and links back to source item pages).
- The page remains usable without external services or runtime credentials.
- Tests cover rendering hooks and edge-traceability display logic.

### Context

The issue requires graph functionality to be traceable in the GitHub Pages user interface, not just in backend data.

**ADR required before implementation.** Rendering an interactive graph in a browser requires a JavaScript visualization library (D3, Sigma, vis.js, or equivalent). Adding any such library is a new external dependency and triggers the ADR requirement in the Non-Negotiable Constraints. Write the ADR using the `adr` skill before writing any implementation code.

**Build watch-outs:**
- The graph page must be generated inside `build_site.py` alongside existing page generation, not as a separate script, so `build_site.yml` picks it up automatically with no workflow changes.
- Avoid CDN-loaded scripts if the library can be vendored (bundled inline or as a local asset under `docs/`). CDN loading creates a runtime external dependency that breaks the "usable without external services" requirement if the CDN is unavailable.
- If vendoring the library produces binary or minified files in `docs/`, confirm they are handled by the `build_site.yml` workflow write path — not committed manually on the branch.
- `docs/` must not be staged or committed on the implementing branch. Run `git status` before every commit and confirm no `docs/` paths appear.

Blocked on W-0072.

---

## W-0074

status: open
created: 2026-05-13
updated: 2026-05-13

### Outcome

Graph quality gates are enforced in code and tests:

- Validation ensures every edge references existing node slugs.
- Validation ensures every edge has `weight` and provenance fields.
- Validation ensures edge generation is reproducible from repository state.
- CI coverage includes graph artifact and graph-page generation paths.

### Context

Traceability requirements are only reliable if schema and integrity checks fail fast during generation and test runs.

Blocked on W-0072 and W-0073.

---

## W-0075

status: open
created: 2026-05-13
updated: 2026-05-13

### Outcome

Edge-weighting evolves beyond the baseline `weight: 1` model:

- A weighting algorithm is defined and documented (for example combining relationship type, evidence strength, or recency signals).
- The algorithm preserves deterministic output and backwards-compatible schema.
- Weighting rationale is inspectable so users can understand why a given edge is stronger/weaker.
- Tests cover scoring rules and stability expectations.

### Context

The issue explicitly requires weighted edges with an initial default of `1`, plus follow-on stories for a later weighting algorithm. This item is that follow-on phase.

Blocked on W-0072 and W-0074.
