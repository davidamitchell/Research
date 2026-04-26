# 2026-04-26 — GitHub.io: Research Master page, All Items page, valid HTML anchors

## Completed

- `Research/Research_Master.md` — changed all 157 `<a name="...">` anchors to `<a id="...">` for valid HTML5
- `scripts/build_site.py` — added two new page builders:
  - `build_research_master_page()` → `docs/research-master.html` — renders Research_Master.md as HTML with matching site styles and a GitHub source link
  - `build_all_items_page()` → `docs/all-items.html` — complete list of all 167 completed research items newest-first using the existing `render_card()` component and `BROWSE_JS` live search
- `scripts/build_site.py` — updated `build_landing()` to add a "more" section at the bottom of the landing page with pill links to All Items and Research Master
- `scripts/build_site.py` — updated `main()` with steps 3 and 4 for the two new pages; renumbered downstream steps; updated module docstring
- `tests/test_build_site.py` — added 6 tests covering `build_all_items_page` and `build_research_master_page`; updated `_make_item` helper to include `display_title` and `added_str` fields needed by `render_card`
- Local build verified: `python scripts/build_site.py` runs cleanly, 462 pages written
- `make check` passes (ruff lint + format)
- `python -m pytest tests/` — 216 passed, 1 pre-existing skip/fail (TAVILY_API_KEY absent), unrelated to this work
- `docs/` NOT committed — auto-generated, will be rebuilt by `build_site.yml` on merge to main

## Mini-Retro

1. **Did the process work?** Yes — the changes were surgical. Three files touched, six new tests, build verified.
2. **What slowed down or went wrong?** One edit accidentally dropped the `def _render_claim(text: str) -> str:` function signature line; caught immediately by `make check`. Test assertions needed two small fixes: HTML output has leading whitespace so `startswith` checks should use `in`, and `<meta name="viewport">` contains `name=` so the anchor check needed to narrow to `<a name=`.
3. **What single change would prevent this next time?** The edit tool only shows surrounding context; double-checking the resulting code block with `view` after each edit catches dropped lines before running tests.
4. **Is this a pattern?** Partial (dropped function signature in an edit). Single occurrence — not yet a recurring pattern.
5. **Does any documentation need updating?** Module docstring in `build_site.py` updated inline. No other user-facing docs affected.
6. **Do the default instructions need updating?** No new conventions emerged.
