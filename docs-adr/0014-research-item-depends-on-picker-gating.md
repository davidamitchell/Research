# ADR-0014: Research item `depends_on` field and picker gating

Date: 2026-05-03
Status: Accepted

## Context

The research item picker (`cmd_pick` in `src/research/cli.py`) selected backlog items using only
the `blocks` field for priority sorting. Items in `blocks` were sorted higher but were never
prevented from being picked before their prerequisites completed.

This caused a concrete failure mode: synthesis items that explicitly depend on multiple primary
items being completed first could be auto-started before their sources existed. The picker had no
hard gating — only soft priority hints.

The `blocks` field signals "I block these items" (from the blocking item's perspective). The
missing inverse is "I need these items done before I can start" (from the dependent item's
perspective).

## Decision

Add a `depends_on: []` frontmatter field to `Research/_template.md` and `ResearchItem` dataclass.
Each entry is the slug (filename stem without `.md`) of a completed item that must exist in
`Research/completed/` before the dependent item is eligible to be picked.

`cmd_pick` builds `completed_slugs` (the set of all `.md` filename stems in `Research/completed/`)
and filters backlog items: any item where one or more `depends_on` slugs are absent from
`completed_slugs` is excluded from the candidate set entirely.

The `blocks` field is retained unchanged — it remains a priority sort hint, not a gate.

Field semantics:
- `blocks: [slug-a, slug-b]` — this item should be picked *before* slug-a and slug-b (priority)
- `depends_on: [slug-c, slug-d]` — this item *cannot* be picked until slug-c and slug-d are
  completed (hard gate)

## Consequences

### Positive
- P-1: Synthesis items and other order-sensitive work can declare prerequisites and will never be
  auto-started before their sources exist.
- P-2: The field defaults to `[]`, making it opt-in — all existing items behave identically.
- P-3: The gate is deterministic and inspectable: `Research/completed/` is the authoritative
  record of completion.

### Negative / Trade-offs
- N-1: An item with unsatisfied `depends_on` is invisible to the picker. If the prerequisites are
  never completed, the dependent item is permanently excluded. This is intentional but must be
  documented so agents do not mistake exclusion for a bug.
- N-2: Slugs in `depends_on` are not validated at write time — a typo will silently exclude the
  item. Future tooling could add a lint check.

### Neutral
- Existing items with no `depends_on` field default to `[]` and are unaffected — no migration
  required.
