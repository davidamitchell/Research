# 2026-06-01 — Goal-constraint feedback convergence vs. cycling

**Completed:**
- `Research/completed/2026-05-31-goal-constraint-feedback-convergence-vs-cycling.md` — researched and completed; maps control-theory convergence conditions (Lyapunov stability, gain/phase margin, feedback delay) to software delivery specification loops; produces three operationalisable design rules: scope-cap to the failing constraint, cadence-matching above constraint-surface change rate, and pre-loop feasibility check; confidence: medium

**Sources used:**
- Åström and Murray, *Feedback Systems* (2020): primary control theory grounding
- Ogata, *Modern Control Engineering* (2010): Nyquist/Bode stability criteria
- Reinertsen, *Principles of Product Development Flow* (2009): product-development flow and cost-of-WIP framing
- DORA 2023 State of DevOps Report: empirical evidence on elite vs. low performers
- Prior completed items: `formal-methods-interdependent-inputs-feasibility`, `split-authority-q6-instability-leading-indicators`

**Review passes:** 4 (3 FAIL → auto-pass on cap)

---

## Mini-Retro

1. **Did the process work?** The research skill process worked correctly. The item reached a well-scoped, evidence-backed conclusion. The control theory to software delivery mapping is tractable and the design rules are operationalisable.

2. **What slowed down or went wrong?** Three review passes failed before the auto-pass cap. The dominant failure pattern was name-only citations without URLs in §3 and §5 (occurring 10+ times in a single item), and opening-sentence inline label omissions in §6 and Findings Executive Summary. These are repeat violations from the Known Recurring Patterns table and should have been caught in the pre-commit self-review step.

3. **What single change would prevent this next time?** Run a targeted `grep` for `source:.*[A-Z][a-z].*Chapter\|source:.*[A-Z][a-z].*(20[0-9][0-9])` before committing, to detect any name-year citation without a URL. This catches the §3 and §5 name-only pattern in under 5 seconds.

4. **Is this a pattern?** Yes — name-only citations in §3 Reasoning and §5 lenses are flagged in the Known Recurring Patterns table as a recurrence ("§3 causal chain items" and "§5 name-only sources"). This session hit both variants again. The root cause is that §3 and §5 are written in a more discursive style and citations tend to be written as author-year-title rather than URL-backed references. The fix (grep pre-commit check) is the correct mechanical guard.

5. **Does any documentation need updating?** The grep command above could be added to the pre-commit self-review checklist in `.github/copilot-instructions.md` to formalise it. Not adding now to avoid scope creep in this session.

6. **Do the default instructions need updating?** No new conventions emerged. The existing Known Recurring Patterns entries cover what happened here.
