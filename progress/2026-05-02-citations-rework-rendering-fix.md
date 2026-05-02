# 2026-05-02 — Citations rework rendering fix

**Issue:** #(citations rework incomplete) — citation style not consistently applied in newly completed items or in the GitHub Pages build.

## Completed

- Diagnosed three citation format variants in completed research items:
  - **Format A** (mid-era, ~April 2026): `[inference; confidence: medium; source: URL]` prefix on Key Findings list items — not stripped by `strip_evidence_labels` because the regex didn't include the `confidence:` keyword.
  - **Format B** (handled): `[inference; source: URL]` inline label — already handled by `_EVIDENCE_SOURCE_LABEL_RE`.
  - **Format C** (current, ~May 2026): `([inference]; medium confidence; source: URL)` suffix on Key Findings list items — not stripped and sources not extracted by `_extract_sources_from_line`.

- **`scripts/extract_metadata.py`**:
  - Updated `_extract_sources_from_line` to also extract URLs from `(...)` parentheticals containing `source:`, in addition to `[...]` brackets. This enables Format C source extraction.
  - Updated `extract_key_claims` to strip the trailing `(; confidence; source: URL)` suffix that remains after bracket removal strips `[inference]`. The new regex handles both the simple `(high confidence)` form and the richer `(; medium confidence; source: URL)` form.
  - Updated docstring to document all four handled formats.

- **`scripts/build_site.py`**:
  - Updated `_EVIDENCE_SOURCE_LABEL_RE` to also match `[type; confidence: X; source: URL]` (Format A) via an optional `(?:;\s*confidence:\s*(?:high|medium|low))?` group.
  - Added `_KEY_FINDING_SUFFIX_RE` for the suffix Format C trailing annotation.
  - Updated `strip_evidence_labels` to apply both the prefix and suffix regexes to list items, producing clean claim text in the rendered Findings section.

- Added tests in `tests/test_extract_metadata.py` for Format C (4 new tests).
- Added tests in `tests/test_build_site.py` for Format A and Format C stripping (5 new tests).
- All 339 tests pass (1 pre-existing failure unrelated to this change: `test_tavily_api_key_is_configured`).
- `make check` passes clean.

## Mini-Retro

1. **Did the process work?** Yes. Tracing the HTML output backward to the markdown source and then to the extraction/rendering pipeline was the right diagnostic approach. The multiple-format issue was immediately visible once I looked at the actual rendered HTML vs. the source markdown.

2. **What slowed down or went wrong?** Nothing significant. The three-format situation required careful analysis to ensure each was handled without breaking the others.

3. **What single change would prevent this next time?** Add a note to `research-prompt.md` or the inline citation skill that Key Findings MUST use Format C (suffix with parens) for all new items, so the rendering pipeline handles them consistently. The proliferation of formats happened because the prompt guidance was updated but older items remained in Format A.

4. **Is this a pattern?** Yes — a known recurring pattern: format drift between research loop outputs. The root fix here is surgical (support all three formats), but a longer-term improvement would be a linting step in the research-review workflow that rejects items with non-conforming citation formats.

5. **Does any documentation need updating?** No user-facing docs need updating. The `research-prompt.md` already specifies Format C for new items. The build pipeline now handles all three formats.

6. **Do the default instructions need updating?** No new conventions emerged that aren't already in place.
