# 2026-04-28 -- Schema Extension: New Research Item Frontmatter Fields (W-0044 to W-0049)

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

## Mini-Retro

1. **Did the process work?** Yes. Batching five backlog items into one PR was the right call; the migration could be done once rather than five times. The `swe` → `tdd` → `code-review` loop was applied implicitly throughout.

2. **What slowed down or went wrong?** One test assertion needed fixing: checking `"superseded-banner" not in html` was too broad because the CSS string contains that class name. The correct assertion is `'<div class="superseded-banner">' not in html`. This is a known pattern with inline-CSS page builders.

3. **What single change would prevent this next time?** For tests that check absence of rendered elements in pages with inline CSS, always check for the full HTML tag form (`<div class="...">`) rather than just the class name string.

4. **Is this a pattern?** Not a recurring one specifically, but "absence test in HTML with inline CSS" is a class of pitfall worth remembering.

5. **Does any documentation need updating?** `.github/copilot-instructions.md` updated with versions immutability rule. ADR-0013 written and indexed.

6. **Do the default instructions need updating?** No new conventions beyond what was already added in this session.
