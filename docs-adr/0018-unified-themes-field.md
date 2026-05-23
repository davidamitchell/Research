# ADR-0018: Unified `themes` field replacing `tags` and `ai_themes`

Date: 2026-05-23
Status: accepted

## Context

The research corpus accumulated two competing theme fields without a shared controlled vocabulary:

- `tags:` — 798 unique values at the point of this decision, with the majority
  appearing only once (singleton tags). Added manually by authors with no vocabulary
  constraint, producing the classic controlled-vocabulary explosion anti-pattern.
- `ai_themes:` — a 16-item controlled vocabulary introduced via Gemini enrichment
  (ADR-0015, W-0069). Covers ~86% of completed items at the time of this decision
  (343 of ~400). Demonstrates that a small, curated vocabulary can achieve near-total
  coverage with far lower maintenance cost than unconstrained tagging.

The co-existence of two fields creates ambiguity for site navigation (W-0070, W-0079),
synthesis candidate detection (W-0081), and theme governance (W-0080). Authors and
the enrichment pipeline face a choice between two fields with no canonical mapping
between them.

W-0076 established the algorithmic grounding: Levenshtein edit distance ≤ 2 combined
with token Jaccard similarity ≥ 0.6 is the appropriate near-duplicate detection pair
for slug-based labels; a ≥3-item threshold prevents singleton growth; a SKOS
(Simple Knowledge Organization System) prefLabel/altLabel structure is applicable
without RDF tooling.

## Decision

Retire `tags:` and `ai_themes:` as distinct frontmatter fields and replace them with
a single canonical `themes:` field governed by the controlled vocabulary in
`docs/themes-vocabulary.md`.

### Field definition

```yaml
themes: []  # canonical slugs from docs/themes-vocabulary.md; 3–5 per item
```

- **Location in frontmatter:** replaces `tags:` (removed) and `ai_themes:` (removed).
  Added after `output:` and before `cites:`.
- **Value type:** list of lowercase-hyphenated slug strings.
- **Cardinality:** 3–5 themes per item at enrichment time; more are acceptable when
  warranted.
- **Vocabulary source:** `docs/themes-vocabulary.md` — 22 canonical slugs at launch,
  with a synonym/alias map. Governed by the ≥3-item growth policy.

### Migration

`scripts/canonicalise_themes.py` performs a one-time migration of all completed and
backlog items, merging `tags:` and `ai_themes:` values through the synonym map and
writing canonical slugs to `themes:`. The legacy fields are removed. The script is
idempotent.

`scripts/validate_themes.py` confirms no residual `tags:` or `ai_themes:` fields
remain after migration.

### Ongoing governance

`scripts/theme_report.py` and the `theme-review.yml` monthly workflow surface
near-duplicate candidates and items lacking `themes:` for human review (W-0080).

### Site impact

`scripts/build_site.py` already contains an `extract_themes()` function with a
`themes`-preferred / `ai_themes`-fallback. W-0079 extends it to generate theme
index pages, per-item badges, related-by-theme links, and a themes navigation entry.

## Consequences

### Positive

- Single field, single vocabulary, single source of truth — eliminates the ambiguity
  between `tags:` and `ai_themes:`.
- 22 canonical slugs vs 798 unique tag values — dramatically simpler for authors and
  the enrichment pipeline.
- The alias/synonym map enables graceful migration without losing the signal in legacy
  `ai_themes:` values (which are already canonical-slug-formatted).
- Near-duplicate detection via Levenshtein + Jaccard is pure Python, O(V²) on the
  vocabulary (V ≤ 40), and adds no external dependencies.
- The ≥3-item growth threshold prevents singleton accumulation and ensures theme
  additions are evidence-based.

### Negative / Trade-offs

- `tags:` field is removed — any site functionality dependent on `tags:` must be
  updated (handled in W-0079). Tag pages (`docs/tags/`) will be superseded by theme
  pages (`docs/themes/`).
- Migration is a one-time bulk change to ~400 files. The idempotent design and the
  `validate_themes.py` check mitigate this risk, but it is a large diff.
- Authors familiar with the `tags:` field must learn the new vocabulary. The
  `research-prompt.md` and `Research/_template.md` are updated to guide them.

### Neutral

- Items without `themes:` degrade gracefully on the site (no badges, no
  related-by-theme) — identical to the existing `ai_themes`-absent behaviour.
- The `ai_themes:` field is preserved in the YAML synonym map as an implicit alias
  set — all 16 `ai_themes` slugs are canonical in the new vocabulary. The migration
  is lossless for items with `ai_themes:` values.
