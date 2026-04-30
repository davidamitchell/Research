# 2026-04-30 -- Research Loop (grill-me-ai-alignment-shared-design)

**Completed:**

Research item:
- `Research/completed/2026-04-30-grill-me-ai-alignment-shared-design.md` -- completed; the item finds that Grill Me is best understood as a clarification-first requirements-discovery workflow, not a magic prompt. Direct clarification-before-code studies support better first-pass correctness and reliability on ambiguous tasks, while the remaining uncertainty is the full project-length time trade-off outside controlled benchmarks.

Sources consulted:
- https://raw.githubusercontent.com/mattpocock/skills/main/skills/productivity/grill-me/SKILL.md (primary definition of the Grill Me technique)
- https://arxiv.org/abs/2310.10996 (ClarifyGPT evidence for clarification-before-code gains)
- https://openreview.net/forum?id=s566pj5E5M (ClariGen abstract-level evidence on clarification improving correctness and reliability)

## Mini-Retro

1. **Did the process work?** Yes. The research-review loop caught confidence and acronym issues that were faster to fix with concrete workflow feedback than by trying to pre-guess every edge case.
2. **What slowed down or went wrong?** Benchmark shorthand and confidence calibration were easy to miss even after a manual self-review, especially when the evidence was strong in substance but thinner than the rubric required.
3. **What single change would prevent this next time?** Add MBPP, GPT-4, and A/B-style comparison shorthand to the prompt's mandatory acronym audit so benchmark terminology gets expanded or rewritten before the first draft commit.
4. **Is this a pattern?** Yes. It matches the known recurring pattern where acronym expansion is the most common research-review failure class.

## Applied improvements

- Updated `research-prompt.md` to add MBPP and A/B to the explicit acronym audit table, and expanded the self-review checklist so GPT-4, MBPP, and A/B-style shorthand are checked before draft commit.

## Pending skill improvements

- Mirror the new MBPP, GPT-4, and A/B acronym examples into the read-only research skill acronym checklist in `.github/skills/` after the Skills submodule is updated in `davidamitchell/Skills`.
