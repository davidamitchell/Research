# 2026-05-22 -- Theme report audit script

**Completed:**
- `scripts/theme_report.py` — added theme audit CLI that scans `Research/completed/`, extracts `themes` and `ai_themes`, computes frequency/provenance/near-duplicates/items-with-neither, and writes `state/theme_report.json` + `state/theme_report.md`.
- `tests/test_theme_report.py` — added focused tests for extraction formats, collection/provenance counts, near-duplicate heuristics, report schema, markdown sections, and CLI output generation.

## Mini-Retro

1. **Did the process work?** Yes. Reusing the `tag_report` structure and importing shared similarity helpers kept the implementation small and aligned with existing conventions.
2. **What slowed down or went wrong?** The first field-regex version accidentally captured block-list lines as inline values due newline matching, which broke three extraction tests.
3. **What single change would prevent this next time?** Prefer explicit `[ \t]*` in frontmatter key regexes when distinguishing inline vs block YAML values.
4. **Is this a pattern?** Yes—frontmatter parsing edge cases recur when regexes are too permissive about whitespace/newlines.
5. **Does any documentation need updating?** Not for this slice; behavior is self-contained in a new script/test pair and does not change user-facing workflow docs.
6. **Do the default instructions need updating?** No new persistent convention emerged beyond existing guidance to write tests first for parser edge cases.
