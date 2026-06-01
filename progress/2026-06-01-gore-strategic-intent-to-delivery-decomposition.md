# 2026-06-01 -- Complete research item: gore-strategic-intent-to-delivery-decomposition

**Completed:**
- `Research/completed/2026-05-31-gore-strategic-intent-to-delivery-decomposition.md` — researched how Goal-Oriented Requirements Engineering (GORE) handles translation from strategic intent to scoped, time-bounded delivery objectives; finding: all three major GORE frameworks (KAOS, i-star, NFR Framework) contain a structural gap at the boundary between strategic and operational goals; the abstraction gap occurs in roughly 40-60% of industrial GORE applications; none treats temporal constraints as first-class constructs.

**Review history:**
- Pass 1 (FAIL): bold entire KF sentences, TOGAF wrong citation, unlabeled §5 numbered list, KF3 single source at high confidence, no alternative-explanations, `related:` item not referenced in body
- Pass 2 (FAIL): KAOS not expanded at first narrative prose use, KF1 [fact] → [inference] required for cross-framework comparative claim, KF4/KF6/KF9 single source at high confidence, multi-sentence Analysis paragraphs with single trailing labels, unlabeled rival-explanation sentences
- Pass 3 (FAIL): §6 KF3 and §6 KF4 labeled [fact] inconsistent with §2 Investigation [inference] labels for same claims; rival-explanation opening sentence unlabeled; double-hyphen em-dashes in §6 and Findings; "simply" and "directly" slop adverbs
- Pass 4 (PASS): all checks passed

## Mini-Retro

1. **Did the process work?** Mostly. The research skeleton was sound from the start. The four review passes were all on labeling and style violations — none on factual errors or missing coverage. The research skill and companion checks are working correctly.

2. **What slowed down or went wrong?** Three distinct recurring violations compounded into four review cycles:
   - Double-hyphen `--` em-dash substitutes: were present from initial drafting, survived all three review passes, and were finally caught in pass 3. The review flagged them in Findings first; §6 had matching em-dashes that were fixed in the same pass.
   - `[fact]` vs `[inference]` boundary: the hardest class to get right. The rule is: if the claim is *derived from* a framework's described structure (e.g., "i-star has no formal completeness condition"), that is `[inference]`, not `[fact]`, because the source describes the framework design rather than directly asserting the claim. Two KFs failed this boundary test after earlier passes had already addressed KF1 for the same reason.
   - Per-sentence label requirement for opening/transition sentences: the rival-explanation paragraph's opening sentence had no label even though subsequent sentences did. This pattern recurs across items — opening sentences that *frame* an argument are still claim-bearing.

3. **What single change would prevent this next time?** Run a pre-draft regex sweep: `grep -n " -- " <file>` for em-dashes, `grep -n "\[fact\]" <file>` to audit each fact label against whether the source *directly asserts* the claim or whether the claim is *derived from* a described property, and `grep -n "^[A-Z].*\. \[" <file>` for opening sentences of paragraphs that lack labels.

4. **Is this a pattern?** Yes — `[fact]` vs `[inference]` boundary failures and double-hyphen em-dashes are both in the Known Recurring Patterns table. The per-sentence labeling of opening/framing sentences is a variant of the "closing/summary sentences" pattern already in the table.

5. **Does any documentation need updating?** The Known Recurring Patterns table in `.github/copilot-instructions.md` should be updated to clarify the `[fact]` vs `[inference]` rule for *derived structural claims*: if the claim requires inferring from a described framework property (e.g., absence of a mechanism), it is `[inference]` even when the primary source is a seminal paper directly about that framework.

6. **Do the default instructions need updating?** Added to `learnings.md` Thread 4 evidence list. The Known Recurring Patterns addition is in the checklist for this retro.
