# 2026-05-06 -- Research Loop (aibom-effectiveness-risk-mitigation-limits)

**Completed:**

Research item:
- `Research/completed/2026-05-06-aibom-effectiveness-risk-mitigation-limits.md` -- completed; this item concludes that AIBOM meaningfully reduces structural drift, scope, and incident-reconstruction risk, but creates false assurance if teams mistake inventory completeness for semantic safety. It identifies prompt injection, poisoned retrieval content, memory poisoning, and harmful use of correctly declared tools as the main boundary cases, and proposes operational metrics for structural coverage, drift latency, blast-radius reduction, and false-assurance monitoring.

Sources consulted:
- https://www.nist.gov/itl/ai-risk-management-framework (governance, measurement, and explainability framing)
- https://arxiv.org/abs/2302.12173 (indirect prompt injection through retrieved content)
- https://www.microsoft.com/en-us/security/blog/2025/04/24/new-whitepaper-outlines-the-taxonomy-of-failure-modes-in-ai-agents/ (agentic failure modes and memory-poisoning controls)

## Mini-Retro

1. **Did the process work?** Yes. The item converged after the review loop forced tighter handling of domain-term definitions, inference labels, and title-level framing.
2. **What slowed down or went wrong?** Most rework came from research-review quality checks, not from missing evidence. The main friction was turning valid conclusions into review-clean prose with the exact epistemic labeling and first-use-definition pattern the workflow expects.
3. **What single change would prevent this next time?** Nothing new needs changing in the prompt. The existing research prompt already warned about first-use domain terms in titles and about over-strong fact labels; I needed to apply those checks earlier in the first draft.
4. **Is this a pattern?** Yes. It matches the existing known pattern that citation-discipline failures often come from acronym or domain-term first use and from treating synthesis as fact instead of inference.
