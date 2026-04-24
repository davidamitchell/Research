# 2026-04-24 -- Research Loop (business-led-low-code-agent-governance)

**Completed:**

Research item:
- `Research/completed/2026-04-24-business-led-low-code-agent-governance.md` -- completed; the item concludes that business-led low-code agent creation is durable only when it sits inside a governed platform with risk-based intake, bounded low-risk use cases, controlled environments, and enforceable data and channel guardrails. It uses DORA, NIST, Microsoft governance documentation, and RPA citizen-development evidence to show that decentralised maker speed without those foundations turns into fragmentation and support seam debt.

Sources consulted:
- https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report (DORA 2025 overview)
- https://airc.nist.gov/airmf-resources/airmf/5-sec-core/ (NIST AI RMF Core Map guidance)
- https://learn.microsoft.com/en-us/microsoft-copilot-studio/admin-data-loss-prevention (Copilot Studio control surface)

## Mini-Retro

1. **Did the process work?** Yes, the research-loop flow worked end to end, and the second review pass caught a few citation-shape issues that were straightforward to fix.
2. **What slowed down or went wrong?** The main friction was that source-access notes for broken seeded URLs were initially written as evidence-backed facts, which the reviewer correctly treated as a citation discipline problem.
3. **What single change would prevent this next time?** Treat source-access observations as plain `Access note:` metadata in §2 instead of citing inaccessible URLs as proof of their own access outcome.
4. **Is this a pattern?** Not yet as a repo-wide recurring pattern, but it is common enough in research-loop sessions to justify tightening the prompt.

## Applied improvements

- Updated `research-prompt.md` to require inaccessible-source observations to be recorded as plain `Access note:` metadata rather than as evidence-backed factual claims.
