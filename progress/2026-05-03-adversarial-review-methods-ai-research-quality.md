# 2026-05-03 -- Research Loop (adversarial-review-methods-ai-research-quality)

**Completed:**

Research item:
- `Research/completed/2026-05-02-adversarial-review-methods-ai-research-quality.md` -- completed; the item concludes that generic self-critique is too weak for reliable research-quality review, while a structured objection-and-verification gate is a plausible prompt-only control supported by adjacent evidence from self-refine, verification, multi-perspective questioning, and adversarial collaboration. It also produces a concrete prompt block that ranks risky claims, generates two substantive objections, checks them with `sequential_thinking`, and blocks finalisation when important objections survive verification.

Sources consulted:
- https://aclanthology.org/2024.findings-acl.212/ (Chain-of-Verification structure for draft, check, and revise loops)
- https://arxiv.org/abs/2406.01297 (critical survey on when Large Language Models can and cannot self-correct)
- https://arxiv.org/abs/2402.14207 (STORM evidence on multi-perspective questioning and coverage gains)

## Mini-Retro

1. **Did the process work?** Yes. The review loop caught exactly the evidence-strength overstatements that were easiest to miss during drafting.
2. **What slowed down or went wrong?** The item needed several passes to distinguish direct facts from cross-paper syntheses and to lower confidence on repository-specific design recommendations.
3. **What single change would prevent this next time?** Nothing new beyond the current review discipline; the existing log-inspection rule already exposed the real problems.
4. **Is this a pattern?** Yes. It matches the known pattern that synthesized claims in research items are easy to overstate if confidence and epistemic labels are not tightened aggressively before review.
