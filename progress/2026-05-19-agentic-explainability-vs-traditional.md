# 2026-05-19 -- Research Loop (agentic-explainability-vs-traditional)

**Completed:**

Research item:
- `Research/completed/2026-05-18-agentic-explainability-vs-traditional.md` -- completed; the item concludes that production-scale deterministic software and multi-step Large Language Model systems both become globally opaque enough to require observability and reconstruction, but they are not explainability-equivalent. Deterministic systems still keep a local replay advantage, while present-day Large Language Model systems add residual nondeterminism and model-internal opacity before scale is even introduced.

Sources consulted:
- https://arxiv.org/abs/1702.08608 (formal explainability framing)
- https://arxiv.org/abs/1711.00399 (counterfactual explanation and bounded explanation surface)
- https://sre.google/sre-book/monitoring-distributed-systems/ (production-scale deterministic-system observability limits)

## Mini-Retro

1. **Did the process work?** Yes. The review workflow found real claim-labeling issues that were faster to fix than to debate upfront.
2. **What slowed down or went wrong?** The hardest part was keeping comparative claims narrow enough that the evidence supported both sides of the comparison instead of only the Large Language Model side.
3. **What single change would prevent this next time?** Nothing new beyond the current review rules; the existing comparative-claim and self-referential-metadata checks already caught the weak spots.
4. **Is this a pattern?** Yes. It matches the existing recurring pattern about synthesis claims outrunning the direct scope of their sources rather than introducing a new class of failure.
