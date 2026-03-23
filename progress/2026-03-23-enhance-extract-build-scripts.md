# 2026-03-23 — enhance-extract-build-scripts

## Task
Significant enhancement to `scripts/extract_metadata.py` and `scripts/build_site.py`.

## Changes Made

### extract_metadata.py
- **Fixed `extract_source_urls()`**: Replaced generic URL regex with targeted patterns for Markdown `[Name](url)`, `Label: url`, and `Label — url` formats
- **Added `_extract_key_claims_fallback()`**: Extracts first sentences from `* [inference]`/`* [fact]` bullets in the Executive Summary subsection when no Key Findings bold bullets exist
- **Updated `extract_key_claims()`**: Falls back to the new helper when no claims found in Key Findings

### build_site.py
- **2a File safety**: `shutil.rmtree` + recreate `RESEARCH_DIR`, `TAGS_DIR`, `THREADS_DIR` at start of `main()` to clear stale pages
- **2b Title normalisation**: `make_display_title()` collapses acronym expansions (e.g. "Long Name (ABBR)" → "ABBR"), colon-truncates, and limits to 80 chars. `display_title` added to all items; subtitle shown on item pages when shortened
- **2c Singleton tag filtering**: `filter_singleton_tags()` drops singletons where item has other navigable tags; retains them when it's the sole tag
- **2d Wiki link**: Meta bar on item pages includes `wiki →` link to GitHub wiki
- **2e Named reference autolinking**: `parse_source_refs()` + `autolink_html()` replace first unlinked named ref occurrence and autolink bare `https://` URLs in rendered section HTML
- **2f Mobile CSS**: Replaced narrow `@media (max-width: 600px)` with full `@media (max-width: 640px)` block; added `.full-title-subtitle` style
- **2g search-index.json**: Added `full_title` field; `title` field now uses `display_title`
- **2h Empty states**: Browse no-results only shown when filters active; search count only shown when query non-empty
- **2i Detailed build summary**: All stats printed on completion
- **2j Exit code 1**: `SystemExit(1)` raised on parse error in `load_items()`

## Results
- `python scripts/extract_metadata.py`: 112 items processed, 513 source URLs found ✅
- `python scripts/build_site.py`: 112 items, 294 pages written, all checks pass ✅
- `ruff check scripts/ && ruff format --check scripts/`: All checks passed ✅

## Security Summary
No security vulnerabilities introduced. All HTML output is escaped via the `escape()` helper. Autolinking only inserts URLs that come from the item's own Sources section.
