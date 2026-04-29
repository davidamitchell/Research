# 2026-04-29 -- Fix source links in key claims on GitHub Pages

**Completed:**
- `scripts/extract_metadata.py` — changed `extract_key_claims` return type from `list[str]` to `list[dict]` (`{"text": str, "sources": list[str]}`); added `_extract_sources_from_line` helper to capture all `https://` URLs from `[...; source: ...]` brackets in Key Findings bullets before they are stripped
- `scripts/build_site.py` — updated `_render_key_claims` to handle new dict format (backward-compatible with legacy `str` entries); added `_render_source_links` helper that renders source URLs as compact monospace domain-name badge links; added CSS for `.claim-sources` and `.claim-source-link` classes
- `state/content_metadata.json` — regenerated with new `list[dict]` format for all 213 items
- `tests/test_extract_metadata.py` — updated all existing tests to check `claims[n]["text"]` and `claims[n]["sources"]`; added `test_no_source_bracket_produces_empty_sources` for Format 1 (no source bracket)

**Root cause:**
`extract_key_claims` in `extract_metadata.py` stripped all `[...]` brackets before storing claims, discarding source URLs. The stored `key_claims` were clean strings with no provenance. `_render_key_claims` in `build_site.py` rendered only the text, so no source links appeared in the "key claims" block on generated pages.

**Fix:**
Before stripping brackets, collect any `https://` URLs from brackets containing a `source:` keyword. Store them alongside the claim text as `{"text": ..., "sources": [...]}`. Render them as clickable domain-name chips in the key claims block.

## Mini-Retro

1. **Did the process work?** Yes — root cause was clear from reading the code; fix was a clean, targeted two-file change (extract + render) with test updates.
2. **What slowed down or went wrong?** The Playwright MCP browser was locked; used Python `playwright` library directly to take the screenshot.
3. **What single change would prevent this next time?** Nothing structural — the root cause was a deliberate design decision (store clean text, no sources) that was later flagged as losing useful data. The format change is contained and backward-compatible on the render side.
4. **Is this a pattern?** No — first occurrence of this specific gap.
5. **Does any documentation need updating?** No — `scripts/` is already documented as the place to edit for site changes.
6. **Do the default instructions need updating?** No.

---

## Session 2 — 2026-04-29 (citation skill conformance)

**Follow-up work triggered by PR comment:**
- Updated `.github/skills` submodule pointer to latest (adds `inline-citation` and `peer-reviewer` skills)
- Reviewed `inline-citation` skill: canonical form `<a href="URL">Author (Year)</a>`
- Updated `scripts/build_site.py`:
  - Added `_extract_citation_label(display_name, url)`: extracts `Author (Year)` / `Org (n.d.)` from Sources section display names
  - Updated `_render_source_links` to accept `url_to_label` dict and render conformant citation chips
  - Updated `_render_key_claims` to thread `url_to_label` through
  - Updated `build_item_page` to build `url_to_label` from `parse_source_refs` and pass it to `_render_key_claims`
  - Updated CSS: `.claim-source-link` now uses teal border and colour so chips stand out as citations
- Updated `Research/_template.md`:
  - Sources section: documented `Author (Year)` display name format for papers and org-title format for documentation
  - Key Findings section: clarified suffix style and noted that source URLs must match `## Sources` entries for citation rendering
- Updated `research-prompt.md`:
  - Added reference to `citation-discipline` and `inline-citation` skills in Step 4 companion checks
  - Documents the canonical display name format for Sources entries
- Added tests to `tests/test_build_site.py`:
  - `test_extract_citation_label_et_al`, `test_extract_citation_label_single_author`, `test_extract_citation_label_org_no_year`, `test_extract_citation_label_known_org`
  - `test_render_source_links_uses_label_map`, `test_render_source_links_fallback_without_label_map`, `test_render_source_links_deduplicates`
- All 314 tests pass; 1 pre-existing TAVILY skip

**Mini-Retro:**
1. **Did the process work?** Yes — new skills were clear, changes were well-scoped and tested.
2. **What slowed down or went wrong?** Playwright MCP still locked; reinstalled `playwright` pip package each session.
3. **What single change would prevent this next time?** Pre-install `playwright` as a dev dependency or in `copilot-setup-steps.yml`.
4. **Is this a pattern?** Yes — Playwright not available across sessions. Worth adding to `copilot-setup-steps.yml`.
