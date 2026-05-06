# 2026-05-06 -- Research Loop (fact-checking-tools-research-quality-improvement)

**Completed:**

Research item:
- `Research/completed/2026-05-06-fact-checking-tools-research-quality-improvement.md` -- completed; the synthesis concludes that the next review-loop upgrade should be a layered control stack, prompt and rubric tightening first, deterministic lint second, and sampled semantic fact-checking only after those cheaper controls exist. It also turns that conclusion into concrete file-level recommendations for `research-review-prompt.md`, `research-prompt.md`, and `.github/workflows/research-review.yml`, plus three draft backlog candidates.

Sources consulted:
- https://github.com/davidamitchell/Research/blob/main/research-review-prompt.md (current automated review rubric)
- https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-06-barnum-statements-ai-responses-theory-practice.md (Barnum failure mode and mitigation stack)
- https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-06-factscore-precision-scoring-atomic-claims.md (atomic-claim precision and offline-audit fit)

## Mini-Retro

1. **Did the process work?** Yes. The prerequisite-item synthesis plus the review workflow surfaced a clear layered recommendation rather than a false choice between prompt-only controls and heavyweight tooling.
2. **What slowed down or went wrong?** The review workflow's `review_count` commit raced with local pushes once, and the first review pass also exposed several label and first-use term issues that were easy to miss in a long mirrored item.
3. **What single change would prevent this next time?** Nothing additional beyond the existing prompt discipline; the remaining issues were item-specific wording errors rather than a missing process step.
4. **Is this a pattern?** No. The review-count race is an occasional workflow timing issue, but the underlying item was completed cleanly after ordinary review-loop iteration.
