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
