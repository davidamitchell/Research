# 2026-05-30 — Complete split-authority-p1-operating-model-synthesis

**Item:** `Research/completed/2026-05-29-split-authority-p1-operating-model-synthesis.md`
**Issue:** Research loop assignment (synthesis item)
**Review cycles:** 4 (3 FAILs, 1 PASS)

## Completed

- Full §0–§7 Research Skill Output written from stub, drawing on 11 completed repository items as proxies for the 6 incomplete Q1-Q6 dependency items
- Findings section seeded from §6 Synthesis: Executive Summary, 10 Key Findings, Evidence Map, Assumptions, Analysis, Risks/Gaps, Open Questions
- Four review cycles completed; item passed all checks (citation-discipline, speculation-control, remove-ai-slop, peer-reviewer, logical-coherence, alternative-explanations, cross-item-integration)
- `learnings.md` Thread 18 updated with the governance-operating-model corollary and its five design principles
- Item moved to `Research/completed/`

## Review Failures and Fixes Applied

**Review 1 (FAIL — 4 violations):**
- `remove-ai-slop`: All 10 Key Findings had full sentences in bold → removed bold from all 10 KFs
- `citation-discipline` (a): §2 C2 causal claim labelled `[fact]` should be `[inference]` → corrected
- `citation-discipline` (b): §2 B1 healthcare claim had no source → narrowed to SRE/SCM only with sources
- `citation-discipline` (c): Analysis cited "all §2 citations collectively" → replaced with explicit URL list
- `cross-item-integration`: `bureaucracy-circumvention` and `do-mode-demand-persistence` in `related:` but not cited in body → added inline citations; moved both to `cites:`

**Review 2 (FAIL — 3 violations, pass 1 of 2 so no issue raised):**
- Acronym "BAU" not expanded at first narrative prose use → expanded to "Business As Usual (BAU)" at §2 B1
- Acronym "IT" not expanded at first narrative prose use → expanded to "Information Technology (IT)" at §2 A1
- Acronym "AI" not expanded at first use → expanded to "Artificial Intelligence (AI)" at §6 Open Questions

**Review 3 (FAIL — 3 violations, pass 2 of 2 so no issue raised):**
- `citation-discipline`: §2 B1 SRE/SCM claim cited `dora.dev/capabilities/loosely-coupled-teams` which covers team architecture not SRE change classification → replaced with `sre.google/workbook/eliminating-toil/`
- `remove-ai-slop`: Triple "X only works if Y" Rule of Three in Analysis → restructured to two-clause form
- `peer-reviewer / alternative-explanations`: Technical quality/debt as alternative delivery constraint not addressed → added third rival model paragraph; mirrored note in §6 Risks and Gaps

**Review 4: PASS** — all seven checks passed.

## Mini-Retro

1. **Did the process work?** The research skill process worked well for a synthesis item. Drawing on 11 completed repository items as proxies for the 6 unfinished Q1-Q6 dependency items was a sound pragmatic choice, clearly labelled as an assumption. The §0–§7 structure kept the investigation organised. The first complete draft was rejected on four separate dimensions simultaneously, which suggests the self-review checks in Step 6 were underdone before the first submission.

2. **What slowed down or went wrong?** Four review cycles is too many. Three of the four FAIL cycles were caused by violations that a more careful pre-submission sweep would have caught:
   - The Rule of Three ("only works if") pattern is a recognisable AI slop signal that should have been caught in §6 self-review.
   - The wrong source for the SRE/SCM claim (DORA loosely-coupled-teams) was plausible-looking but incorrect — a reviewer spotted it immediately. Matching each cited URL to the specific claim it supports is a discipline that takes more time than it appears to.
   - The alternative-explanations gap (technical quality as a rival constraint) was the most substantive miss: this is a well-known competing hypothesis that DORA research directly supports, and the item explicitly cites DORA. The peer-reviewer check exists precisely to catch this class of gap.

3. **What single change would prevent this next time?** Before triggering the first review run, apply a dedicated "rival hypotheses" audit: for each central claim, ask "what is the most prominent competing explanation in the literature I've already cited, and is it addressed in Analysis?" This would have caught the technical quality alternative before submission.

4. **Is this a pattern?** Yes. The alternative-explanations failure is the same structural gap that has appeared before. When a synthesis item draws on sources that discuss multiple drivers of an outcome (DORA, ToC), the central claim must explicitly engage with all major drivers those sources identify, not only the one the synthesis is arguing for. This is the peer-reviewer check's core job.

5. **Does any documentation need updating?** Added the governance-operating-model corollary to `learnings.md` Thread 18. No other documentation changes needed.

6. **Do the default instructions need updating?** The Known Recurring Patterns table in `.github/copilot-instructions.md` should add: "Alternative-explanations gap in synthesis items" — when a synthesis item cites sources that discuss multiple constraint or driver types, the Analysis must address each as a rival or complementary explanation. Added below.
