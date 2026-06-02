# 2026-06-02 — Complete research item: ITIL capacity baseline assertion vs telemetry

**Item:** `Research/completed/2026-05-31-itil-capacity-baseline-assertion-vs-telemetry.md`

**Completed:**
- Fixed two rounds of review violations; item passed review (auto-pass at review_count=2 cap)
- Moved to `Research/completed/` via `python -m src.main research complete`
- Added Thread 25 to `learnings.md`

**Key finding:** ITIL capacity management uses "should" not "shall" for all measurement requirements, structurally tolerates assertion-based baselines, and specifies no mandatory validation gate after service go-live. ISO/IEC 20000-1:2018 Clause 8.6 closes this gap with "shall" language for certified organisations.

## Round 1 review violations fixed

- IEC not expanded on first prose use → added expansion in Sources section
- §2 B1 ITIL 4 "should" claim `[fact]` → `[inference]` (PeopleCert source is secondary/paywalled)
- §5 lens paragraphs missing trailing `[inference; source:]` labels → added
- Analysis had near-verbatim repetition and missing alternative-explanation paragraph → removed repetition, added rival hypothesis (Iden & Eikebrokk data cost vs. mandate absence)
- §7 acronym audit missing IEC → updated

## Round 2 review violations fixed

- §3 point 3: `[fact]` → `[inference]` (same ITIL 4 "should" claim)
- §2 D1/D2: `[fact]` → `[inference]` for ISO 20000 Clause 8.6 text (paywalled standard); added access note
- §2 E1: Removed quotation marks from Iden & Eikebrokk paraphrase (source access-restricted)
- KF2: `high` → `medium` confidence (single source — IT Process Wiki)
- KF3: `[fact]` → `[inference]` + medium confidence; rewrote "gradient of assertion tolerance" to describe the actual sub-process distinction
- KF6: `[fact]` → `[inference]` + medium confidence; removed "closes the assertion-tolerance gap" evaluative claim
- KF7: Removed specific quoted phrase; standardised to paraphrase (source access-restricted)
- §6 Analysis: added per-sentence labels throughout; removed "genuine strengthening", replaced "inherently costly" with "costly"
- §6 Executive Summary: ISO 20000 last sentence `[fact]` → `[inference]`
- §6 Evidence Map: updated KF3, KF6 labels and ISO 20000 note
- §6 + Findings Risks/Gaps: added ISO 20000 paywall acknowledgment
- Findings Executive Summary: ISO 20000 last sentence `[fact]` → `[inference]`
- Findings Analysis: per-sentence labels throughout; removed "genuine tightening", "inherently expensive"
- Findings Risks/Gaps: added ISO 20000 paywall note
- Output section: ISO 20000 `[fact]` → `[inference]`
- §5 Technical lens: "inherently projection-based" → "structurally projection-based"
- §7: updated to reflect all changes

## Mini-Retro

1. **Did the process work?** Yes, but required two full review cycles. Most violations in round 2 were introduced by inconsistent label propagation — fixing §2 but not the corresponding §3, §6, and Findings locations.

2. **What slowed down or went wrong?** The most time-consuming pattern was label inconsistency across mirrored sections (§2 → §3 → §6 Key Findings → Findings Key Findings → Evidence Map). Fixing one location without fixing all mirrored locations causes the review to re-flag the same violation in different section(s) next pass.

3. **What single change would prevent this next time?** Before committing any label fix, grep the entire document for the same quoted phrase or claim pattern and fix ALL occurrences in one pass. A claim like `[fact]` for ITIL 4 "should" was fixed in §2 but not §3 and KF3 and Findings KF3 — all four need updating together.

4. **Is this a pattern?** Yes — this matches the "multi-section label propagation" pattern. The Known Recurring Patterns table already covers per-sentence labels and closing-sentence labels; this variant (same claim in mirrored sections) is slightly different. However, it's covered adequately by the parity-check rule (§6 Synthesis and Findings must stay aligned). The missing step was extending the parity check to §3 Reasoning (which mirrors §2 claims) and the Evidence Map.

5. **Does any documentation need updating?** The §7 recursive review checklist could explicitly note: "for every label change in §2, grep all of §3, §6, and Findings for the same claim and fix the same label there." This would prevent the round-2 §3 violation.

6. **Do the default instructions need updating?** No new conventions needed — the existing parity-check rule covers it. Enforcement of that rule needs to be more systematic: run `grep -n "\[fact\]" item.md` and audit every `[fact]` instance across all sections before committing any label fix.
