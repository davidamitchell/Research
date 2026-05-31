# 2026-05-31 -- Complete Q5 Control Model Tradeoff

**Completed:**
- `Research/completed/2026-05-29-split-authority-q5-control-model-tradeoff.md` — answered: Class 1 → post-hoc review; Class 2 → bounded delegation; Class 3 → pre-approval; governed by five selection criteria and four conditional modifiers; theoretical grounding from TCE discriminating alignment, COSO preventive-detective distinction, ITIL 4 Change Enablement, and SRE error budget policy as concrete trigger-based regime-shift instantiation.

**Review passes required:** 3 (auto-passed on third trigger after review cap reached)

**Violations fixed across three review rounds:**
1. Pass 1: ITIL expansion missing in RSO; DORA format inverted; three unlabeled evaluative superlatives
2. Pass 2: Seven unlabeled inference sentences; bolded numbered-list headers; KF4 `[fact]` → `[inference]`
3. Pass 3: SRE analogy sentence unlabeled; §6 opening sentence unlabeled; behavioural risk opening sentence unlabeled (in RSO §6 and Findings); `[SLO]` → `(SLO)` in two occurrences

## Mini-Retro

1. **Did the process work?** Yes. The research skill output and Findings structure held up. The content was sound on first draft; all three review cycles surfaced citation-discipline and speculation-control violations, not substantive content problems.

2. **What slowed down or went wrong?** Three full review passes were needed. The persistent pattern is single unlabeled sentences that follow a labeled sentence — reviewers do not extend a label across a sentence boundary. The §6 Synthesis opening sentence and Findings Analysis opening sentence both required labels that were missed because the immediately preceding context made them feel covered.

3. **What single change would prevent this next time?** Before triggering the first review: run `grep -n "^\(The\|These\|This\|A \|An \)" <item>` on §6 Synthesis and Findings Analysis to catch opening sentences without trailing labels, then inspect each one explicitly. Opening sentences of sections are the highest-risk location for missing labels because authors rely on section context rather than sentence-level tagging.

4. **Is this a pattern?** Yes — unlabeled closing/summary sentences and opening sentences is already in the Known Recurring Patterns table. This session adds the corollary: sentence-boundary label blindness is most acute at **section openings**, not just paragraph closings.

5. **Does any documentation need updating?** The Known Recurring Patterns table entry for unlabeled opening/closing sentences already notes §6 Synthesis and Findings Executive Summary as high-risk. The session confirms this extends to any paragraph-opening sentence in Analysis and RSO narrative paragraphs. No new table entry needed; the existing entry covers this.

6. **Do the default instructions need updating?** No new convention emerged. The existing self-review checklist item (2c, 2d) already covers this. No changes to `.github/copilot-instructions.md` required.
