# 2026-03-12 — Evaluate instructions and feedback for continuous improvement

## Task

Evaluate the repository instructions against recent commits, PRs, and owner feedback. Suggest and implement improvements specifically related to continuous self-improvement.

---

## Evaluation findings

### What is working well

1. **Non-Negotiable Constraints** — explicit, named, enforced. The submodule read-only constraint was added proactively after the second violation.
2. **Mini-Retro requirement** — present in the instructions, and sessions are writing them.
3. **Improvement Flywheel** — the `Do the work → run the retro → fix root cause → better system` loop is documented and partially working.
4. **Session logs** — created consistently; contain useful context for future sessions.
5. **CHANGELOG.md** — being maintained; ADR triggers are clear.
6. **`learnings.md`** — substantive cross-cutting synthesis with six threads; evidence-backed.

### What is not working: key patterns

#### Pattern 1 (systemic): Acronym expansion failures in every research review
**19+ open GitHub issues** (81–107) all report the same citation-discipline failure: abbreviations like `LLM`, `CLI`, `SDK`, `PAT`, `ITSM`, `PaaS`, `SRE`, `MECE` are used before being expanded on first use.

Root cause: `research-prompt.md` Step 6 (companion skill checks) deferred the citation-discipline check to `research/SKILL.md §8`, which is only available when the skills submodule is initialised. In the cloud runner, the submodule is often absent, so the check doesn't happen. Even when available, the acronym rule is abstract enough that the agent doesn't catch concrete violations before submitting.

The Continuous Improvement section explicitly says "the same friction in two retros → it's a pattern → prioritise fixing the root cause." This appeared in 19+ sessions with no root-cause fix applied. That gap has now been closed.

#### Pattern 2: Research loop session logs lacked mini-retro
The `copilot-instructions.md` says "every session ends with a mini-retro", but `research-prompt.md` Step 11 (the session log template) didn't include the mini-retro format. Automated research loop sessions therefore produced logs without retros, disconnecting the improvement flywheel from the highest-volume session type.

#### Pattern 3: `learnings.md` update was ad-hoc
`learnings.md` is a cross-cutting synthesis document, but neither `research-prompt.md` nor `copilot-instructions.md` required updating it as part of completing a research item. Updates depended on the agent remembering to check it.

---

## Changes made

### `research-prompt.md` — Step 6 (companion skill checks)
Added an **inline acronym expansion audit** directly in the step — not a deferral to the skill file. The audit:
- Lists the specific abbreviations that have failed review most often (13 entries drawn from the review issue history)
- Gives the exact expansion format required
- Must be run before Step 7 (sense check), so violations are caught before the draft is submitted

### `research-prompt.md` — New Step 11 (update `learnings.md`)
Added a mandatory step after "Complete the item": check whether any key finding adds signal to an existing thread in `learnings.md`, or opens a new one. The step has clear "do / don't" guidance to prevent noise (per-item summaries don't belong there).

### `research-prompt.md` — Step 12 (was Step 11): Mini-Retro in session log
Added the four mini-retro questions to the session log template. The automated research loop now produces session logs that close the improvement flywheel.

### `research-prompt.md` — Step 13 (was Step 12): renumbered
Commit step renumbered from 12 to 13 to accommodate the new learnings step.

### `.github/copilot-instructions.md` — Completing Research workflow
Added `learnings.md` update as step 5 between "complete the item" and "create session log". Steps 5 and 6 renumbered to 6 and 7.

### `.github/copilot-instructions.md` — Known Recurring Failure Patterns
Added a new subsection under "Improvement Comes in Classes" with a table of three documented patterns:
- Acronym not expanded on first use
- Editing `.github/skills/` directly
- `web search synthesis` used as a citation

Each entry records the pattern, its impact, and the root fix applied. Future sessions add new rows here when a new recurring pattern is identified.

---

## Mini-Retro

1. **Did the process work?** Yes. The evaluation approach — reading instructions, then cross-referencing against open issues and recent PRs — surfaced clear, specific gaps rather than vague suggestions.

2. **What slowed down or went wrong?** The 19+ open review issues all describe the same problem (acronym expansion) but there was no single place that named it as a known pattern. Finding the pattern required reading all the issues. A "Known Recurring Patterns" table would have surfaced this immediately.

3. **What single change would prevent this next time?** The Known Recurring Patterns table now exists. When the next session encounters an acronym violation in a review, the table entry points directly to the inline audit in Step 6. The loop is closed.

4. **Is this a pattern?** Yes — "improvement identified in retro but not applied to the instructions" is itself a meta-pattern. The fix is the "Known Recurring Patterns" table: it makes the gap between observation and instruction-update visible, and closes it by requiring the table to be updated in the same Mini-Retro that identifies the pattern.
