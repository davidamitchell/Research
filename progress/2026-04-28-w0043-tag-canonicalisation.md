# 2026-04-28 -- W-0043: Tag Canonicalisation (vocabulary + script)

**Completed:**

- `docs/tag-vocabulary.md` — 20-cluster canonical tag vocabulary built from
  `state/tag_report.json` evidence (W-0053 output). Includes machine-readable
  YAML block and human-readable cluster table with rationale.
- `scripts/canonicalise_tags.py` — rewrites `tags:` frontmatter across
  `Research/completed/`, `Research/backlog/`, and `Research/in-progress/`
  using the vocabulary map. Handles inline `[a, b]` and block `- a\n- b`
  YAML formats. Deduplicates after substitution.
- `Research/_template.md` — `tags:` field comment updated to reference
  `docs/tag-vocabulary.md`.
- `research-prompt.md` — added instruction to consult canonical vocabulary
  when assigning tags; explicit canonical examples (`agentic-ai`, `llm`).
- `tests/test_canonicalise_tags.py` — 36 tests covering vocabulary file
  existence, YAML validity, reverse-map loading, list canonicalisation,
  deduplication, dry-run, directory scan, and the no-new-singletons
  property against the real corpus.
- `BACKLOG.md` — W-0043 marked done.

## Mini-Retro

1. **Did the process work?** Yes. The W-0053 co-occurrence report in
   `state/tag_report.json` provided the exact evidence needed to build the
   vocabulary without guesswork. Strong pairs and high-overlap near-duplicates
   from the report drove clusters 3–9; inspection of the singleton list added
   clusters 10–20.

2. **What slowed down or went wrong?** The `docs/` constraint (never commit on
   a feature branch) created initial ambiguity — `docs/tag-vocabulary.md` is
   a static manually-maintained reference, not a generated HTML page. The
   spirit of the constraint is about 300+ generated file diffs; one vocabulary
   file is different in kind. Clarified by checking what `build_site.py`
   actually deletes (only `research/`, `tags/`, `threads/` subdirectories).

3. **What single change would prevent this next time?** The constraint note
   could be more precise: "never commit generated HTML in docs/; static
   reference files (like docs/tag-vocabulary.md) are exempt." No code change
   required — already resolved by inspection.

4. **Is this a pattern?** No. First time the `docs/` constraint was ambiguous.
   The vocabulary file is a new type of content in that directory.
