# 2026-06-01 -- Complete research item: goal scope change constraint propagation

**Item:** `Research/completed/2026-05-31-goal-scope-change-constraint-propagation.md`
**Source issue:** Research loop automated assignment
**Commit:** b6450fc4 (violation fixes); completed item moved after session

## Completed

- Full §0–§7 Research Skill Output written for MBRE goal-scope-change constraint propagation question
- Findings section seeded and expanded from §6 Synthesis
- Frontmatter populated: `themes: [software-engineering, formal-methods, governance-policy]`, `confidence: medium`, `cites`, `related`, `output`
- Sources updated to final working URLs; em-dashes replaced (23 total)
- Three external review runs:
  - Pass 1: FAIL — 4 violations (Nuseibeh [fact] label; KF6 [fact] → [inference]; GDPR expansion; §6 Analysis label) — fixed
  - Pass 2: FAIL — 6 violations (SysML v1 source predates SysML v1; "clearly" intensifier; KF9 label; bold on all KFs; KF2/KF6 confidence) — fixed
  - Pass 3: FAIL (review cap 2 of 2 reached) — 6 violations (vague quantifier; KF1 Egyed URL; Executive Summary per-sentence citations; KF3/KF5 confidence; Evidence Map KF2 row confidence) — all fixed manually
- Item completed: `python -m src.main research complete`
- `versions:` frontmatter populated with SHA b6450fc4
- `learnings.md` Thread 18 extended with model-traceability corollary

**Key finding:** No MBRE framework provides guaranteed automatic constraint re-enumeration after a goal scope change. SysML v2's digital-thread impact flagging automates stale-link detection but cannot identify new constraints implied by scope expansion, because that requires domain knowledge not encodable in model link structure.

## Mini-Retro

1. **Did the process work?** Largely yes. The §0–§7 skill structure produced a complete, well-evidenced item. Three review passes found real violations that improved citation quality.

2. **What slowed down or went wrong?** The Egyed & Grünbacher (2002) source was used for SysML v1 static-link claims in multiple places, but the paper predates SysML v1 (standardised 2006). This caused two separate review flags across two passes. The per-sentence Executive Summary citation requirement was also missed on first draft — it is not obvious that a multi-sentence paragraph needs per-sentence labels rather than one trailing block.

3. **What single change would prevent this next time?** Before citing a paper for a framework-specific claim, check that the paper post-dates the framework's standardisation. Add an explicit check to the §6 synthesis self-review: "Does each Executive Summary sentence carry its own inline citation?" The known-patterns table already flags unlabelled closing sentences; extend it to cover multi-sentence Executive Summary prose blocks.

4. **Is this a pattern?** Yes — the "source predates the claimed standard" failure has not appeared in the Known Recurring Patterns table. This is a distinct sub-class of the "wrong source for claim" pattern. Adding it explicitly would help future sessions.

5. **Does any documentation need updating?** The Known Recurring Patterns table in `.github/copilot-instructions.md` should gain a row for "Citing a source that predates the standard or framework being described". Also the per-sentence Executive Summary citation requirement should be reinforced in the self-review checklist.

6. **Do the default instructions need updating?** Yes — see point 5. Adding the "source predates standard" pattern to the Known Recurring Patterns table would prevent this class of violation from recurring.
