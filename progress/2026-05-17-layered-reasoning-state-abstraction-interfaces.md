# 2026-05-17 -- Research Loop (layered-reasoning-state-abstraction-interfaces)

**Completed:**

Research item:
- `Research/completed/2026-05-17-layered-reasoning-state-abstraction-interfaces.md` -- completed; the item concludes that the safest LLM to EBM boundary is a canonical typed state envelope that preserves only decision-relevant invariants, with AST or CST and graph views treated as derived projections rather than competing sources of authority. It also concludes that asynchronous feedback should use localized repair artifacts, such as named invariant violations and JSON Patch operations, before escalation to regeneration or fail-closed fallback.

Sources consulted:
- https://www.di.ens.fr/~cousot/COUSOTpapers/POPL77.shtml (abstract interpretation basis for lossy-but-sufficient state preservation)
- https://openreview.net/forum?id=BZ5a1r-kVsf (LeCun's multi-level abstraction architecture for autonomous machine intelligence)
- https://developers.openai.com/api/docs/guides/structured-outputs (official schema-constrained generation guidance)

## Mini-Retro

1. **Did the process work?** Yes; the draft-review-fix loop surfaced two genuine overclaims and one citation-discipline edge case before completion.
2. **What slowed down or went wrong?** Seeded source URLs included one wrong arXiv identifier and one blocked OpenAI blog page, which forced source replacement and extra review passes.
3. **What single change would prevent this next time?** Nothing beyond the current prompt rules; the existing review workflow caught the exact issues that needed correction.
4. **Is this a pattern?** Partly; bad or stale seeded URLs are a recurring friction, but the current prompt already instructs replacement with accessible official sources and the review workflow enforced that correctly.
