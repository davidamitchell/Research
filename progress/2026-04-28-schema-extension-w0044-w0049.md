# 2026-04-28 -- Schema Extension: New Research Item Frontmatter Fields (W-0044 to W-0049) + Tag Co-occurrence Report (W-0053)

**Completed:**

- `Research/_template.md` — added 7 new frontmatter fields after `output:`: `cites`, `related`, `superseded_by`, `supersedes`, `item_type`, `confidence`, `versions`
- `src/research/item.py` — `ResearchItem` dataclass extended with the 7 new fields; defaults to `[]`, `None`, `"primary"`, `"medium"`, `[]` when absent from frontmatter
- `scripts/build_site.py` — updated `load_items()` to capture new fields; added `_render_cites_related()` and `_render_versions()` helpers; updated `build_item_page()` to render synthesis badge, confidence badge, superseded banner, cites/related link sections, and version history table; updated `render_card()` for synthesis badge and superseded data attribute
- `research-prompt.md` — added explicit "Frontmatter fields to populate during research" block in Step 1 with per-field population instructions
- `tests/test_research_item.py` — added 7 new tests covering default values, parsing of all new fields
- `tests/test_build_site.py` — added 14 new tests covering synthesis badge, superseded banner, confidence badge, cites/related sections, versions table, and empty-state rendering
- `docs-adr/0013-research-item-frontmatter-schema-extension.md` — ADR documenting the decision, field semantics, immutability rule, migration approach, and trade-offs
- `docs-adr/README.md` — updated index with ADR-0013
- `.github/copilot-instructions.md` — added versions immutability rule to Non-Negotiable Constraints
- Migration of ~214 completed items + 1 backlog item — all new fields added with defaults via automated script
- `scripts/tag_report.py` — tag co-occurrence report generator (W-0053): scans completed + backlog items, computes tag frequency, co-occurrence matrix, near-duplicate candidates (Levenshtein ≤ 2 or prefix/suffix overlap ≥ 0.8), singleton tags, strong co-occurrence pairs (>80% threshold, min co-occurrence 2)
- `.github/workflows/tag-review.yml` — monthly workflow (1st of month, 06:00 UTC) + workflow_dispatch: generates report, commits to main, opens GitHub issue with near-duplicate and singleton candidates
- `state/tag_report.json` + `state/tag_report.md` — initial report: 214 items scanned, 949 unique tags, 658 singletons, 26 strong synonym pairs, 68 near-duplicate candidates
- `tests/test_tag_report.py` — 27 tests covering Levenshtein distance, prefix/suffix overlap, tag extraction, co-occurrence matrix, strong pairs, near-duplicates, full report structure, and Markdown rendering
- `BACKLOG.md` — W-0043 remains open (depends on reviewing W-0053 output); W-0053 marked done

## Mini-Retro

1. **Did the process work?** Yes. The W-0053 implementation was clean and self-contained — pure tooling with no migration needed.

2. **What slowed down or went wrong?** The initial strong-pairs detection was too aggressive: singleton tags (1 occurrence each) that happen to appear in the same item trivially produce 100% co-occurrence ratios, flooding the output with noise. Fixed by requiring `min_cooccurrence ≥ 2`.

3. **What single change would prevent this next time?** When building co-occurrence metrics, always apply a minimum count filter to exclude trivially-satisfied ratios from low-frequency items. This is a standard data quality pattern for co-occurrence analysis.

4. **Is this a pattern?** Not previously documented — adding to known patterns: "co-occurrence ratio with no minimum count yields trivial 100% matches."

5. **Does any documentation need updating?** No changes needed beyond what was done here.

6. **Do the default instructions need updating?** No new conventions needed.
