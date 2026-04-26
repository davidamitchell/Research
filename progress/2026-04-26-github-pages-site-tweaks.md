# 2026-04-26 — GitHub Pages site tweaks

## Completed

- `scripts/build_site.py` — `load_items()`: made the sort key explicit as
  `(added, filename)` descending so same-date items are ordered deterministically
  by filename (reverse-alphabetical) rather than relying on stable-sort insertion order.
- `scripts/build_site.py` — `build_research_master_page()`:
  - Strip the `## Table of Contents` section (heading + list items + `---` separator)
    from `md_text` before rendering, reducing page size and DOM element count by ~165
    `<li>/<a>` elements.
  - Convert deprecated `<a name="...">` anchors to HTML5 `<a id="...">` form in
    `md_text` before rendering (fixes the pre-existing failing test).
  - Merged the two `<p class="page-subtitle">` elements into one to reduce DOM depth.
  - Confirmed no JavaScript is emitted (already the case; explicitly documented).
- `tests/test_build_site.py` — added two new tests:
  - `test_build_research_master_page_no_toc` — asserts "Table of Contents" not in HTML.
  - `test_build_research_master_page_no_javascript` — asserts no `<script>` in HTML.
- Pre-existing failing test `test_build_research_master_page_contains_toc_anchors`
  now passes (the `<a name>` → `<a id>` conversion in Python fixes it).
- `make check` passes (ruff lint + format).
- `python -m pytest tests/` — 218 passed, 1 pre-existing skip (TAVILY_API_KEY absent),
  unrelated to this work.
- Local build verified: `python scripts/build_site.py` — 464 pages written.
- `docs/` NOT committed — auto-generated, will be rebuilt by `build_site.yml` on merge.

## Mini-Retro

1. **Did the process work?** Yes. The changes were surgical: two function edits and two
   new tests. The pre-existing test failure (anchors) was directly caused by the change
   being requested, so fixing it was natural.
2. **What slowed down or went wrong?** Nothing significant. The TOC regex needed care
   to match the exact blank-line/`---`/blank-line boundary pattern.
3. **What single change would prevent friction next time?** None needed — the change
   was straightforward.
4. **Is this a pattern?** No.
5. **Does documentation need updating?** No; the docstring for
   `build_research_master_page()` was updated inline.
6. **Do default instructions need updating?** No.

## Follow-up: PR#403 datetime migration

After PR#403 merged, all frontmatter `added` fields became full ISO 8601 datetime
(`YYYY-MM-DDTHH:MM:SS+00:00`). Updated `load_items()` to:
- Parse `added` as a `datetime` object (with UTC timezone) rather than `date`
- YAML auto-parses ISO 8601 datetime strings as `datetime.datetime` objects; plain
  date strings fall back to `date` objects which are converted to midnight UTC datetime
- Sort key is now `(added_dt, filename)` — full datetime gives sub-day ordering;
  filename provides stable tiebreaker for the rare case of exact-same timestamp
- `added_str` continues to expose just `YYYY-MM-DD` for display purposes
- `_thread_date_range()` updated to call `.date().isoformat()` so display is still
  `YYYY-MM-DD` format
- Tests updated: `_make_item` helper accepts `date | datetime` and normalises to tz-aware
  `datetime`; all 219 tests pass, pre-existing TAVILY skip unchanged
