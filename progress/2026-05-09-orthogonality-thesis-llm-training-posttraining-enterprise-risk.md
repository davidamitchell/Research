# 2026-05-09 -- Research Loop (orthogonality-thesis-llm-training-posttraining-enterprise-risk)

**Completed:**

Research item:
- `Research/completed/2026-05-09-orthogonality-thesis-llm-training-posttraining-enterprise-risk.md` -- completed; modern post-training weakens a simplistic orthogonality reading but does not justify treating capable Large Language Model systems as durably enterprise-safe by default. The item concludes that current post-training is better understood as behaviour shaping than objective certification, so tool-using deployments still need bounded machine identities, deterministic external controls, runtime monitoring, and earned autonomy.

Sources consulted:
- https://nickbostrom.com/superintelligentwill.pdf (orthogonality thesis and instrumental convergence baseline)
- https://www.anthropic.com/research/alignment-faking (strategic compliance evidence under monitoring pressure)
- https://www.aws.amazon.com/blogs/security/four-security-principles-for-agentic-ai-systems/ (enterprise control model for deterministic boundaries and earned autonomy)

## Mini-Retro

1. **Did the process work?** Yes, but only after several review-driven wording and evidence-calibration fixes.
2. **What slowed down or went wrong?** Cross-source synthesis claims were initially written too strongly, and one identity-control conclusion needed the directly relevant completed IAM item cited at the point of claim.
3. **What single change would prevent this next time?** Add a self-review check that cross-source conclusions about shifted objectives, strategic compliance, or evidence breadth default to `[inference]` unless a cited source states the combined claim directly.
4. **Is this a pattern?** Yes. It matches the repo's known citation-discipline pattern, especially around acronym expansion and fact-versus-inference calibration in synthesis prose.

## Applied improvements

- Updated `research-prompt.md` to add `2g1` and `2g2`, which now force an explicit check for cross-source synthesis claims and evidence-scope wording before review.

## Pending skill improvements

- Mirror the new `research-prompt.md` checks into the upstream research/citation skills so cross-source synthesis defaults and evidence-scope claims are caught before the review workflow.
