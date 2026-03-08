# 2026-03-08 — Improve Research Review System

**Completed:**

System improvements:
- `research-review-prompt.md` — added scope notes to Steps 1 and 2, scoping
  citation-discipline and speculation-control off the `## Context` section.
  Full citation and speculation checks apply to `## Research Skill Output` and
  `## Findings`; the `## Context` section gets a lighter standard (hard factual
  claims only for citation; overconfident assertions only for speculation).
- `research-prompt.md` — inserted new Step 8 (Self-review) between the Sense
  check step and the Complete step. Agent now runs all three quality checks
  in audit-only mode against the in-progress item and fixes any violations
  before completing. Steps 8, 9, 10 renumbered to 9, 10, 11 accordingly.
- `.github/workflows/research-review.yml` — added `issues: write` permission;
  added a label-creation step (idempotent via `2>/dev/null || true`); added
  `gh issue create` / `gh issue comment` logic so each FAIL opens or updates
  a `research-review`-labelled GitHub issue assigned to davidamitchell.
- `Research/_template.md` — updated `## Context` hint text to make clear that
  the section is a framing device, that hard factual claims must still be
  sourced, and that working hypotheses and motivating rationale do not require
  labels.
- `tests/test_research_review.py` — added 5 new tests covering the scope notes
  in Steps 1 and 2 of the review prompt, the `issues: write` permission, the
  `gh issue create` reference, and the idempotent label creation.
