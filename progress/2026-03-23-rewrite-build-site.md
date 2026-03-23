# 2026-03-23 — Rewrite build_site.py

## What happened

Complete rewrite of `scripts/build_site.py` (1071 → 1572 lines).

## Changes

### New pages generated
- `docs/index.html` — landing page (stats block, thread pills, tag pills, inline search preview)
- `docs/browse.html` — filterable research card grid (formerly index.html)
- `docs/threads.html` — threads listing
- `docs/threads/<slug>.html` — individual thread pages
- `docs/threads-index.json` — thread data for JS

### New functions
- `detect_threads(items)` — groups items by `thread` frontmatter (explicit) or shared ≥3 tags (implicit)
- `load_links(items)` — builds per-item related-items map (shared ≥2 tags)
- `strip_evidence_map(text)` — strips tooling-appended Evidence Map sections
- `get_findings_excerpt(item)` — plain-text excerpt from Findings section
- `detect_shared_sources(items)` — groups items sharing source filenames

### Updated generators
- `build_landing` (new) — stats, thread pills, tag pills, inline search preview
- `build_browse` (new) — filterable grid with URL state
- `build_item_page` — adds key claims block (top bullets from Findings) + related items panel
- `build_tag_page` / `build_tags_index` — back-link now points to browse.html
- `build_search_index` — adds `findings_excerpt` field

### CSS
- `.item-content h2`: `text-transform: uppercase` → `text-transform: lowercase`
- New components: stats-block, key-claims, related items, thread connectors, landing search preview, thread/tag pills, featured sections, thread listing

### Nav
- Added Browse and Threads links alongside Tags and Search

## Verification
- `python3 scripts/build_site.py` — built 112 items, 564 tag pages, 10 threads, no errors
- `python3 -c "import ast; ast.parse(...)"` — syntax OK
- `make check` (ruff) — all checks passed (scoped to `src/` and `tests/`)

## Commit
`9db9886` on branch `copilot/build-github-pages-site`
