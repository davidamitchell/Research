# 2026-04-22 -- Research Loop (enterprise-ai-capability-model)

**Completed:**

Research item:
- `Research/completed/2026-04-22-enterprise-ai-capability-model.md` -- completed; the item concludes that enterprise AI use-case intake works best as a three-layer dependency map, with foundational shared rails checked before any claim of reuse. It also distinguishes that intake model from a portfolio-level maturity model, and uses DORA, NIST, ISO, AI Index, GitHub, GitClear, and Faros evidence to show that local productivity gains do not substitute for governance, context, evaluation, platform safety nets, and operating-model readiness.

Sources consulted:
- https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report (software-delivery and prerequisite-capability evidence)
- https://doi.org/10.6028/NIST.AI.100-1 (risk-management and governance baseline)
- https://learn.microsoft.com/en-us/microsoft-copilot-studio/guidance/maturity-model-overview (concrete comparison point for a five-level portfolio maturity model)

## Mini-Retro

1. **Did the process work?** Yes. The research loop, review pass, and final completion flow worked end to end, and the external review caught a real citation-discipline weakness rather than only superficial issues.
2. **What slowed down or went wrong?** The first review cycle focused on claim classification, and the second surfaced a narrower citation-discipline issue around undefined domain shorthand and maturity-model terminology that was easy to miss during self-review.
3. **What single change would prevent this next time?** Add an explicit self-review rule that specialised architecture shorthand must be rewritten in plain language or linked to an authoritative definition on first use.
4. **Is this a pattern?** Yes. It is the same general citation-discipline family as the recurring acronym-expansion failures, but broader: specialised shorthand and undefined terms trigger the same review friction even when the logic is sound.

## Applied improvements

- Updated `research-prompt.md` to add a self-review check for undefined domain shorthand and maturity-model terminology.

## Pending skill improvements

- `.github/skills/citation-discipline/SKILL.md` should add an explicit check for non-self-evident domain shorthand, so terms like "maturity ladder", "knowledge graph", and "critic stack" are either defined with authoritative sources or rewritten in plain language on first use.
