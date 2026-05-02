# 2026-05-02 -- Research Loop (systematic-review-methodology-ai-synthesis)

**Completed:**

Research item:
- `Research/completed/2026-05-02-systematic-review-methodology-ai-synthesis.md` -- completed; the item concludes that W-0051 should use a hybrid method stack, Cochrane and PRISMA for rigor, narrative synthesis for default integration, and optional realist-synthesis or meta-ethnographic passes only for mechanism or meaning questions. It also recommends a claim-first provenance model, explicit contradiction handling, and a manual-only `synthesis-loop.yml` so cross-item synthesis can stay auditable and avoid false consensus.

Sources consulted:
- https://training.cochrane.org/handbook/current/chapter-09 (Cochrane synthesis preparation framework)
- https://arxiv.org/abs/2402.14207 (STORM architecture and perspective-guided evidence gathering)
- https://arxiv.org/abs/2401.01313 (hallucination-mitigation survey)

## Mini-Retro

1. **Did the process work?** Yes. The review workflow caught the remaining epistemic-label and definition issues that were easy to miss during the initial drafting pass.
2. **What slowed down or went wrong?** The main slowdown was that the review workflow can finish successfully on an auto-pass path while the log still contains real violations, so I had to inspect the log rather than trust the run conclusion.
3. **What single change would prevent this next time?** Nothing. The current prompt already warns about the auto-pass path and the need to inspect `OVERALL:` and `VIOLATION:` lines directly.
4. **Is this a pattern?** Yes. It matches the existing documented pattern that review logs, not workflow conclusion alone, are the source of truth for research-review outcomes.
