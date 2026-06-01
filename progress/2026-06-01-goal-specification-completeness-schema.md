# 2026-06-01 -- Complete research item: goal-specification-completeness-schema

**Completed:**
- `Research/completed/2026-05-31-goal-specification-completeness-schema.md` — researched and completed; establishes the five minimum schema fields a Goal specification must carry for automated actionability (intent statement, success criterion, actor assignment, domain scope, initial conditions) and a two-stage validation pipeline (structural completeness check + semantic consistency check); hard-error vs. degraded-mode error semantics documented across KAOS/GORE, IEEE 29148, ArchiMate 3.2, and PDDL.

**Work done this session:**
- Read item and conducted web research across KAOS/Goal-Oriented Requirements Engineering (GORE), Institute of Electrical and Electronics Engineers (IEEE) 29148, TOGAF/ArchiMate, Planning Domain Definition Language (PDDL), and Taye & Ghoul (2023) ontology paper
- Wrote full §§0–7 Research Skill Output
- Populated Findings section with 12 Key Findings, Evidence Map, Analysis, and cross-item citations
- Went through 4 review cycles: 3 failures, 1 pass
- Fixed violations in each cycle: em-dashes, IEEE expansion, Key Finding bold removal, Analysis para opening labels, cross-item citations, KF confidence calibration, SysML expansion, per-sentence labels for all mid-paragraph evaluative claims, §5 regulatory lens claim narrowed to remove unsupported DO-178C/ISO 26262 cross-standard claim
- Updated `learnings.md` Thread 18 with new item

**Final commit:** cb0115d1

## Mini-Retro

1. **Did the process work?** Mostly yes. The research itself was sound and the findings are well-supported. The review cycle caught genuine violations rather than false positives -- each failure identified real labelling gaps.

2. **What slowed down or went wrong?**
   - Required 4 review cycles (3 failures before pass). Each failure surfaced a different class of violation because the review agent applies checks at varying granularity per run.
   - The most persistent pattern: evaluative comparative claims in mid-paragraph positions between two already-labeled sentences -- the review correctly treats each sentence as independent and requires its own label. This is correct behaviour but easy to miss when editing.
   - §5 Regulatory lens had an unsupported cross-standard claim (DO-178C/ISO 26262 referencing IEEE 29148) that was not caught during self-review because the cited sources were used for adjacent claims in the same paragraph.
   - SysML was expanded inside a prior Python script but the fix silently failed to persist (Python script wrote successfully but the file was overwritten by a subsequent script that loaded an older version -- debugging revealed a file-write ordering issue in the multi-step fix approach).

3. **What single change would prevent this next time?**
   Run all sentence-level label audits in a single Python pass over the full Findings section before committing, rather than fixing only the named sentences from the review report. The pattern is that fixing the reported sentences is correct but new unlabeled sentences become visible to the next review run because the fix changes paragraph flow.

4. **Is this a pattern?** Yes -- this is a known recurring pattern: "Unlabeled closing/summary sentences and mid-paragraph evaluative claims." The Known Recurring Patterns table already has two related entries (closing sentences and §3 causal chain lists). This session adds evidence that mid-paragraph evaluative claims using comparative terms ("safer", "more usable", "most severe", "only rational") are the most common missed case.

5. **Does any documentation need updating?** The Known Recurring Patterns table could be sharpened with: "Mid-paragraph comparative/evaluative claims without per-sentence labels" as a distinct entry, since the existing entries focus on paragraph-closing sentences and §3 causal chains, not on mid-paragraph sentences that fall between two already-labeled sentences.

6. **Do the default instructions need updating?** Yes -- the Known Recurring Patterns table should be updated to explicitly call out mid-paragraph evaluative sentences between labeled sentences as a separate failure class. The current entry ("Unlabeled closing/summary sentences") only covers closing sentences; mid-paragraph unlabeled evaluative claims are a distinct and recurring failure class that the review consistently flags.
