# Session: build-site-v3

**Date:** 2026-03-23
**PR:** #291 — feat: static GitHub Pages site for completed research items

## Work done

Addressed comment 4108846362: full v3 specification for the GitHub Pages site pipeline.

### Changes made

**`scripts/extract_metadata.py`**
- Fixed `source_urls` extraction: now uses Markdown `[Name](URL)` pattern + `Label: https://...` and `Label — https://...` (was HTML `<a href>` regex that found nothing in plain Markdown files)
- Added key_claims fallback: if no `- **` Key Findings bullets found, falls back to `* [inference]`/`* [fact]` bullets in Executive Summary subsection

**`scripts/build_site.py`**
- **File safety**: `shutil.rmtree` + recreate `docs/research/`, `docs/tags/`, `docs/threads/` at each build start. Leaves `docs/adr/`, `docs/issues/` untouched.
- **Title normalisation**: `make_display_title()` — collapses `"Long Name (ABBR)"` to `"ABBR"`, colon-truncates, 80-char limit. Full original title shown as subtitle on item pages when shortened.
- **Singleton tag filtering**: `filter_singleton_tags()` — drops tags with count==1 if item has other non-singleton tags; retains if sole tag. Result: 397 singleton tags dropped, 167 unique tags remaining (was 564).
- **Wiki link**: `wiki →` added to item page meta bars linking to `https://github.com/davidamitchell/Research/wiki/[slug]`
- **Named reference autolinking**: `parse_source_refs()` + `autolink_html()` — links named references from Sources section and autolinks bare `https://` URLs in section HTML
- **Mobile responsive CSS**: `@media (max-width: 640px)` block — sticky nav, single-column cards, 2x2 stats, larger touch targets, flex-wrap meta bar
- **`search-index.json`**: added `full_title` field (original title), `title` = display_title
- **Empty states**: browse.html and search.html only show "no matching items" when filters/query are active and produce zero results — never on page load
- **Detailed build summary**: comprehensive stats including exclusion reasons, singleton counts, thread breakdown, edge counts, items with key claims
- **Exit code 1** on YAML parse failure

## Build output
112 items, 11 excluded, 294 pages, 167 tags, 397 singletons dropped, 10 threads, 58 items with key claims

## Mini-Retro

1. **Did the process work?** Yes. The two-phase agent approach (sub-agent implements, main agent verifies) worked cleanly.
2. **What slowed down?** Fetching the full comment required API calls — the problem statement truncated it at ~16KB.
3. **What single change would prevent this next time?** The comment truncation in the problem statement is environment-level; nothing to fix. The key bug fix (markdown URL extraction vs HTML) was straightforward once the full spec was read.
4. **Is this a pattern?** No — the extract_metadata source_urls bug was a first-time oversight.
