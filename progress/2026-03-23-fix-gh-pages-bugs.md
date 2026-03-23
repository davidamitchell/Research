# 2026-03-23 — Fix GitHub Pages Bugs

## Task

Fixed four bugs in the GitHub Pages pipeline plus UX improvements, per issue #... .

## Changes Made

### Bug 1: `scripts/extract_metadata.py`
- Added module-level `_KEY_CLAIMS_SKIP_PREFIXES` regex constant.
- In `extract_key_claims`: after stripping bold markers and splitting into sentences, now
  skips any leading sentence starting with `confidence:`, `[inference]`, `[fact]`, or
  `[assumption]` (case-insensitive) and uses the next valid sentence instead.
- **Before**: `"Confidence: high. Actual claim text."` → key claim `"Confidence: high"`
- **After**: key claim `"Actual claim text"`

### Bug 2: `scripts/build_site.py` — tag count in stats block
- Changed `build_landing` to build a flat `all_tags_flat` list, then use
  `len(set(all_tags_flat))` for `tag_count` and `Counter(all_tags_flat)` for frequency.
- Makes the intent explicit: count unique tags only.

### Bug 3: `scripts/build_site.py` — Evidence Map tables in Findings
- Added `strip_evidence_map_table(text)` helper that removes any heading line containing
  "Evidence Map" and all subsequent `|`-prefixed table lines (with blank-line gap handling).
- Applied in `build_item_page` per-section render and in `get_findings_excerpt`
  (for search index excerpts).

### Bug 4: `scripts/build_site.py` — stray HTML closing tags
- Added module-level `_STRAY_CLOSE_TAGS_RE = re.compile(r"</(?:p|li|td|div)>(?=[\"'>])")`.
- Applied as post-render cleanup in `build_item_page` after `autolink_html`.
- Only removes closing tags immediately followed by `"`, `'`, or `>` — the pattern
  created by broken href attributes — leaving normal structural closing tags intact.

### Navigation changes (`scripts/build_site.py`)
- Removed "Browse" from `html_nav()`.
- Added "GitHub" link (`https://github.com/davidamitchell/Research`, opens in new tab).
- Item page breadcrumbs: removed "Browse" intermediate step (`Research / item` now).
- Tag page back-links: changed `← browse` → `← all tags` pointing to tags index.

### Tag filter (`scripts/build_site.py`)
- `build_tags_index`: added `id="tags-list"` and `data-tag` attributes on each `<li>`.
- Added filter input `#tag-filter` with inline JS that hides/shows list items on input.
- Removed Browse back-link from tags index header.

### ADR-0010 (`docs-adr/0010-github-pages-static-site.md`)
- New ADR documenting GitHub Pages static site as the primary research delivery channel.
- Supersedes ADR-0005 (GitHub wiki), documenting the migration trigger conditions met.
- Updated `docs-adr/README.md` index.

## Validation

- `ruff check scripts/ && ruff format --check scripts/` — ✓ passes
- `python -m pytest tests/ -q` — 190 passed, 1 pre-existing failure (TAVILY_API_KEY),
  1 skipped — no regressions introduced
- CodeQL analysis — 0 alerts
