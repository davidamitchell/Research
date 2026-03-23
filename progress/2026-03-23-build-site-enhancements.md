# 2026-03-23 · build-site-enhancements

## What was done

Built on the previous session's `build_site.py` rewrite. This session added:

### New: `scripts/extract_metadata.py`
- Reads all `Research/completed/*.md` (same exclusion rules as build_site.py)
- Produces `state/content_metadata.json` with per-item:
  - `named_concepts` — top-20 2–4 word noun phrases via n-gram frequency (stopword filtered)
  - `source_urls` — https URLs from Sources section, deduped, excluding repo self-links
  - `key_claims` — first sentence of each Key Findings bullet (up to 8)
- Processed 112 items, 2240 concepts, 833 URLs

### Updated: `scripts/build_site.py`
- Ruff fixes: removed unused `slug_map` variable and unused loop index `_i`
- All checks pass: `ruff check scripts/ && ruff format --check scripts/`

### Updated: `.github/workflows/build_site.yml`
- Added `scripts/*.py` to trigger paths
- Added `Extract metadata` step (runs before `Build site`)
- Commit step now includes `state/content_metadata.json`

### New output: `state/content_metadata.json`
- Committed to repo (4343-line JSON, ~112 items)

## Build output
- 112 research pages, 564 tag pages, 10 thread pages
- All generated cleanly with no errors

## Commits
- `206947b` feat: add extract_metadata.py, rewrite build_site.py with threads/landing/browse, update workflow
