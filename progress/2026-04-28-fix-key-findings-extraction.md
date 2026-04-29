# 2026-04-28 -- Fix Key Findings extraction in extract_metadata.py

**Completed:**
- `scripts/extract_metadata.py` — fixed `extract_key_claims` to handle all three Key Findings bullet formats; 22 items previously had "High confidence" / "Medium confidence" extracted as the claim text instead of the actual finding; the newest format (source bracket first) was being silently skipped
- `state/content_metadata.json` — regenerated; all 212 items processed cleanly with correct claim text
- `tests/test_extract_metadata.py` — added 10 tests covering all three formats and edge cases

## Root Cause

Three Key Findings bullet formats exist in the research corpus:

| Format | Example | Bug |
|---|---|---|
| Format 1 (older) | `1. **Claim.** (high confidence)` | Worked correctly |
| Format 2 (mid-era) | `1. **High confidence.** [source] Claim text` | Source bracket stripping left `High confidence. [inference;` → "High confidence" extracted as claim |
| Format 3 (current) | `1. [source] **High confidence:** Claim text` | Line regex required `**` immediately after list marker; Format 3 starts with `[`, so lines were silently skipped → empty `key_claims` |

**Fix:** Rewrote `extract_key_claims` to:
1. Match any numbered/bulleted list item (not just those starting with `**`)
2. Strip all `[…]` brackets wholesale (source references, regardless of length)
3. Strip bold confidence-level prefixes (`**High confidence.**`, `**Medium confidence:**`)
4. Strip trailing parenthetical confidence labels `(high confidence)`

## Mini-Retro

1. **Did the process work?** Yes. Root cause was straightforward once the three formats were compared side by side.
2. **What slowed down or went wrong?** The initial look at the HTML showed the Key Findings section *was* present in the generated page for one item. The real issue was that the `key_claims` block at the top of item pages (the "key claims" summary box) was populated with "High confidence" / "Medium confidence" strings. Needed to check `state/content_metadata.json` directly to confirm.
3. **What single change would prevent this next time?** The research loop should standardise the Key Findings format in `research-prompt.md` so new items consistently use one format. However, the extraction function should also be format-tolerant — which it now is.
4. **Is this a pattern?** No — this was a one-off format drift as the research loop evolved. The fix is now defensive against all known variants.
5. **Does any documentation need updating?** No user-facing docs affected.
6. **Do the default instructions need updating?** No new conventions introduced.
