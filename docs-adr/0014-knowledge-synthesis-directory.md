# ADR-0014: Knowledge/ synthesis directory and schema

Date: 2026-05-05
Status: accepted

## Context

The completed research corpus has grown to ~40 items across four natural thematic
clusters. Individual research items each answer a single bounded question; they do
not produce integrated conclusions that span multiple items. Without a synthesis
layer, the corpus accumulates knowledge but never reaches the decision-relevant
"wisdom" level of the DIKW hierarchy.

Two completed research items establish the architectural requirements:

- **2026-03-03-cross-item-synthesis-meta-insights** defines the synthesis
  methodology: a four-step process (extract → cluster → identify relationships
  → write integrated conclusions), a minimum output structure, and a false-consensus
  guard (no claim without a source-item citation).
- **2026-05-02-cross-item-synthesis-knowledge-map-architecture** confirms that
  synthesis outputs should follow the existing item schema (using `cites`,
  `confidence`, `versions`, and frontmatter provenance) rather than a parallel
  content store, and that `workflow_dispatch` is the correct trigger pattern for
  on-demand synthesis.

A new directory, schema, prompt, and workflow are required because:

1. Synthesis items have a structurally different section layout from primary
   research items (Synthesis Question, Cross-Item Findings, Contradictions and
   Tensions, Confidence Map rather than Research Question, Findings).
2. The synthesis agent needs a dedicated prompt (`synthesis-prompt.md`) that
   enforces cross-item citation requirements and the false-consensus guard.
3. The site generator must route synthesis item pages to a separate URL prefix
   (`/Research/knowledge/`) so they are discoverable but visually distinct.
4. A dedicated `synthesise.yml` workflow provides a website-accessible trigger
   (no local IDE required) that accepts a synthesis question and optional source
   item slugs.

The decision introduces new storage (a `Knowledge/` directory at the repo root)
and a new document type, both of which meet the ADR-required "when to write an ADR"
criteria in `.github/copilot-instructions.md`.

## Decision

### 1. New directory: `Knowledge/`

Synthesis items are stored in `Knowledge/<YYYY-MM-DD>-<theme-slug>.md` at the
repository root. This directory is:

- Separate from `Research/completed/` to avoid the autonomous research loop
  picking up synthesis items as research targets.
- Always tracked (contains `.gitkeep`).
- Included in `build_site.yml` trigger paths so that pushing a new synthesis
  item automatically rebuilds the site.

### 2. Frontmatter schema for synthesis items

```yaml
title: "Synthesis title as a noun phrase"
synthesised: YYYY-MM-DD        # date the synthesis was produced
status: draft | published
theme: short-slug              # used in the filename
source_items: []               # slugs of Research/completed/ items used
tags: []                       # canonical tags from docs/tag-vocabulary.md
cites: []                      # same list as source_items (machine-readable citations)
confidence: high | medium | low
versions: []                   # {version, sha, changed, progress, summary}
```

The `cites` field aligns with ADR-0013, which introduced the citation graph.
`source_items` is a human-readable alias stored for clarity; `cites` is the
machine-readable edge used by the site generator.

### 3. Section layout for synthesis items

```markdown
## Synthesis Question
## Source Items
## Perspectives Considered
## Cross-Item Findings
## Contradictions and Tensions
## Confidence Map
## Open Questions
```

The site generator (`scripts/build_site.py`) adds these section names to
`SECTIONS_ORDERED` so they are extracted and rendered on the item page.

### 4. Site routing

Synthesis item pages are built to `docs/knowledge/<slug>.html` and linked from
`/Research/knowledge/`. A new `docs/knowledge/index.html` lists all synthesis
items. The "Synthesis" link is added to the site navigation bar.

Synthesis items appear in:
- `docs/knowledge/index.html` (primary listing)
- `docs/all-items.html` (merged with research items)
- `docs/search-index.json` (with correct `url` field for JS search)
- Tag pages (`docs/tags/<tag>.html`)

Synthesis items are **not** included in `docs/browse.html` or thread detection
(these are research-item-specific views).

### 5. Synthesis prompt and workflow

- `synthesis-prompt.md` — the 12-step synthesis agent prompt injected into
  each Copilot CLI synthesis session.
- `.github/workflows/synthesis-loop.yml` — `workflow_dispatch`-only workflow
  following the `research-loop.yml` pattern. Inputs: `synthesis_question`
  (required), `source_items` (optional comma-separated slugs). Commits directly
  to `main` using `COPILOT_GITHUB_TOKEN`.

### 6. No new credentials required

`COPILOT_GITHUB_TOKEN` and `TAVILY_API_KEY` are already approved repository
secrets. The synthesis workflow uses the same secrets as `research-loop.yml`.

## Consequences

### Positive

- Synthesis outputs are findable, citable, and versioned using the same
  infrastructure as primary research items.
- False consensus is guarded at the prompt level: no synthesis claim without
  an explicit source-item citation.
- The site navigation exposes synthesis items as a first-class collection.
- The workflow is triggerable from the GitHub website without a local IDE.
- No new credentials or external services are required.

### Negative / Trade-offs

- `Knowledge/` items are not included in thread detection. Thread logic operates
  on `Research/completed/` only; synthesis items would require a separate
  clustering pass to detect synthesis-level threads.
- The `build_site.py` `build_all_items_page()` merges research and synthesis items,
  which may make the "All Items" page busier as the synthesis corpus grows.
- The `synthesis-loop.yml` workflow requires the same `COPILOT_GITHUB_TOKEN`
  PAT constraint as `research-loop.yml`: the PAT must have Copilot access.

### Neutral

- `Knowledge/_template.md` serves as the canonical synthesis item template.
  Agents copy it when starting a new synthesis item.
- The `synthesis-prompt.md` is the single tuning lever for synthesis behaviour;
  no code change is required to improve synthesis quality or add new sections.
