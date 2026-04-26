---
title: "Keeping research backlog separate from repo improvement backlog"
added: 2026-03-02T08:19:48+00:00
status: completed
priority: high
tags: [process, workflow, organisation]
started: 2026-03-02T08:19:48+00:00
completed: 2026-03-02T08:19:48+00:00
output: [knowledge]
---

# Keeping research backlog separate from repo improvement backlog

## Question / Hypothesis

What is the cleanest way to separate two distinct types of work — *what to research* vs *how to improve this repo* — so that neither overwhelms the other and each can be prioritised independently?

## Context

In a repo that is both a research tracker *and* a code project, the backlog naturally splits into two kinds of items:
1. **Research items** — questions and topics to investigate (e.g. "best way to synthesise information")
2. **Repo improvement items** — code, tooling, and structural work (e.g. "add YouTube fetcher")

Mixing these in a single list makes prioritisation harder and obscures what is actually being worked on.

## Scope

**In scope:**
- File-system separation strategy
- Labelling and status field conventions
- How to reference a research item from a repo improvement item and vice versa

**Out of scope:**
- External project management tools

## Approach

1. Implement the two-file approach: `Research/backlog/` + `BACKLOG.md`
2. Define a cross-reference convention (e.g. `see Research/backlog/YYYY-MM-DD-title.md`)
3. Document the convention in `AGENTS.md` and `Research/README.md`

## Sources

- [x] Existing conventions in `davidamitchell/Latest-developments-` — https://github.com/davidamitchell/Latest-developments-
- [x] `BACKLOG.md` in this repo — https://github.com/davidamitchell/Research/blob/main/BACKLOG.md
- [x] `Research/README.md` in this repo — https://github.com/davidamitchell/Research/blob/main/Research/README.md
- [x] `AGENTS.md` Non-Negotiable Constraints section — https://github.com/davidamitchell/Research/blob/main/.github/copilot-instructions.md

## Findings

### Executive Summary

The cleanest separation is a two-location file system approach: research items live as individual `.md` files under `Research/backlog/`, and repo improvement items live as numbered entries in a single `BACKLOG.md` at the repo root. Each location has distinct status conventions, priority mechanisms, and naming schemes suited to its item type. Cross-references flow in one direction: a completed research item can produce a `backlog-item` output that spawns a numbered entry in `BACKLOG.md`, but repo improvement items do not generate research items. This approach is already implemented and documented in this repo; the findings confirm the design is correct and identify the cross-reference pattern as the key mechanism that makes the two lists interoperable without merging them.

### Key Findings

1. **Two-location separation works cleanly.** `Research/backlog/` holds research questions as individual dated `.md` files; `BACKLOG.md` holds code/tooling/process work as numbered items. The file system location alone encodes which type of work an item is — no labels or tags needed to distinguish them.
2. **Header notes reinforce the boundary.** `BACKLOG.md` opens with an explicit callout: "This file tracks repo improvement work. For research item backlog, see `Research/backlog/`." `Research/README.md` has a dedicated section titled "Separating Research Backlog from Repo Improvement Backlog". Both serve as onboarding guardrails for agents and humans.
3. **AGENTS.md enforces the constraint at the rules level.** The Non-Negotiable Constraints section lists "Keep research backlog (`Research/backlog/`) separate from repo improvement backlog (`BACKLOG.md`)" as a hard rule. This surfaces the convention in agent instructions before any file browsing is needed.
4. **Status conventions differ and are appropriate for each type.** Research items use front-matter `status: backlog | in-progress | completed` and move between directories. `BACKLOG.md` items use inline `status: open | done | archived`. The difference reflects that research items have richer lifecycle metadata (started/completed dates, outputs) while improvement items need only a quick status signal.
5. **Priority mechanisms differ appropriately.** Research items carry a `priority: high | medium | low` front-matter field, enabling programmatic sorting. `BACKLOG.md` items are ordered numerically and by epic; priority is conveyed by ordering, not a field. Research items benefit from explicit priority because the research loop processes them autonomously; `BACKLOG.md` items are typically worked by an agent in response to owner instruction.
6. **Cross-references flow research → improvement, not the reverse.** A research item can produce a `backlog-item` output type, which spawns a new numbered entry in `BACKLOG.md`. The reverse direction (a `BACKLOG.md` item referencing a research item) uses a prose note in the `Context` field (e.g., W-0020: "Research item `Research/completed/2026-02-27-indexing-and-tracking-method.md` was completed first; findings directly informed the ADR."). This one-way convention prevents circular dependencies.
7. **`davidamitchell/Latest-developments-` uses a single `BACKLOG.md` with no research item tracking.** That repo is a pipeline project with no research function; its backlog is entirely improvement-type work organised as Epic/Slice tables. It does not provide a pattern to follow for the research/improvement split — it is simply a repo that has no need for the split.
8. **The `output:` field in the research item template is the formal cross-reference mechanism.** Setting `output: [backlog-item]` in a research item's front-matter signals that the research produced a repo improvement task, and the `## Output` section describes and links it. This makes the cross-reference machine-readable and searchable.

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| Two-location separation encodes item type by file system location | `BACKLOG.md` header; `Research/README.md` structure | high | Both locations observed directly in this repo |
| Header notes reinforce the boundary | `BACKLOG.md` lines 1–5; `Research/README.md` § Separating Research Backlog from Repo Improvement Backlog | high | Direct inspection |
| AGENTS.md enforces the constraint | `AGENTS.md` Non-Negotiable Constraints section | high | Listed as a non-negotiable rule |
| Research items use front-matter status; BACKLOG.md uses inline status | `Research/_template.md`; `BACKLOG.md` items W-0001 through W-0029 | high | Direct inspection |
| Research items have explicit priority field for autonomous processing | `Research/_template.md`; `research-prompt.md` priority sort logic | high | Research loop uses `priority:` to select next item |
| Cross-references flow research → improvement via `output:` field | W-0020 `Context` note; research item `## Output` section format | high | Observed in W-0020 and template |
| `Latest-developments-` uses single BACKLOG.md with no research tracking | `davidamitchell/Latest-developments-` `BACKLOG.md` | high | Direct API inspection; no `Research/` directory exists in that repo |
| `output: [backlog-item]` is the formal cross-reference mechanism | `Research/_template.md` output field options | high | Defined in template |

### Assumptions

- **Assumption:** The separation should be maintained indefinitely, not merged as the repo grows. **Justification:** Research items and improvement items have fundamentally different lifecycles, metadata needs, and automation patterns. Merging them would require a single format to serve both, which would degrade both. The two-file approach remains appropriate regardless of scale.
- **Assumption:** Agents working on this repo will read `AGENTS.md` before acting. **Justification:** `AGENTS.md` is the single source of truth per the repo's design; all agent entry points (`.github/copilot-instructions.md`, `.claude/CLAUDE.md`) point to it.

### Analysis

The two-location approach succeeds because it maps the categorical difference between item types onto the file system, which is the most primitive and durable form of organisation. There is no schema to maintain, no tags to keep consistent, and no tooling to build. The boundary is enforced at three levels: file system location (structural), header notes in each file (documentary), and `AGENTS.md` rules (behavioural). These three levels create redundancy — any one layer alone would be fragile; together they make the convention robust across agent sessions.

The `Latest-developments-` comparison is useful in the negative: a single `BACKLOG.md` with Epic/Slice tables works well when all work is improvement-type. Once a repo contains genuine research questions that require investigation, synthesis, and evidence tracking, that format breaks down. Individual `.md` files per research item provide the space needed for Findings, Evidence Maps, and Output sections — none of which fit in a table row.

The unresolved design question is prioritisation within `BACKLOG.md`. Research items have an explicit `priority:` field because the research loop selects items autonomously. `BACKLOG.md` relies on ordering, which works when an agent reads the whole file but is less reliable as the file grows. This is out of scope for this item but worth flagging.

### Risks, Gaps, and Uncertainties

- `BACKLOG.md` has no explicit priority field. As the file grows, ordering-as-priority degrades. An agent asked to "pick the highest-priority improvement item" has no machine-readable signal equivalent to the `priority:` field in research items.
- There is no automated check that prevents a research item from being added to `BACKLOG.md` or vice versa. Enforcement is entirely by convention and agent instruction. A future CI check could verify this.

### Open Questions

- Should `BACKLOG.md` gain an explicit `priority:` field for items, mirroring the research item convention, to support autonomous improvement work? This could become a `BACKLOG.md` item.
- Should a CI check verify that no `.md` files exist directly in `BACKLOG.md` format under `Research/backlog/` and vice versa?

---

## Output

- Type: knowledge
- Description: The two-location separation (`Research/backlog/` + `BACKLOG.md`) is confirmed as the correct design. Convention is documented in `AGENTS.md` (Non-Negotiable Constraints), `Research/README.md`, and `BACKLOG.md` header note. Cross-reference mechanism: research items use `output: [backlog-item]` and the `## Output` section; improvement items reference research items via prose `Context` notes.
- Sources:
  - https://github.com/davidamitchell/Research/blob/main/BACKLOG.md (repo improvement backlog format and header note)
  - https://github.com/davidamitchell/Research/blob/main/Research/README.md (research workflow and separation documentation)
  - https://github.com/davidamitchell/Latest-developments-/blob/main/BACKLOG.md (comparison: single-type backlog in a pipeline repo)