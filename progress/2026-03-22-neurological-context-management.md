# 2026-03-22 — Research Loop (neurological-context-management)

**Completed:**

Research item:
- `Research/completed/2026-03-15-neurological-context-management.md` — completed; this item finds that human decision-making uses a sharply capacity-limited active context, explicit prefrontal-style gating, schema formation, and suppression of stale search paths rather than a flat pool of always-active information. The strongest AI implication is a layered context architecture with a small active buffer, resident high-authority priors, separate episodic and schema stores, and escalation to slower deliberation when novelty or conflict appears.

Sources consulted:
- https://pmc.ncbi.nlm.nih.gov/articles/PMC2864034/ (Cowan review on working-memory capacity limits)
- https://pubmed.ncbi.nlm.nih.gov/11283309/ (Miller and Cohen review on prefrontal cognitive control)
- https://pmc.ncbi.nlm.nih.gov/articles/PMC3789138/ (Preston and Eichenbaum review on hippocampal-prefrontal schema formation)

## Mini-Retro

1. **Did the process work?** Yes; the research loop, draft review, and revision cycle produced a much tighter note with stronger URL-level evidence and cleaner claim discipline.
2. **What slowed down or went wrong?** Several canonical journal pages were not directly accessible, and the first review pass exposed that internal repository-item citations had leaked into claim-bearing sections instead of staying as prior-work context.
3. **What single change would prevent this next time?** Add an early preflight grep that rejects repository-path citations anywhere outside the prior-work/source list before the first draft commit.
4. **Is this a pattern?** Yes; it matches the known recurring review pattern around citation discipline and claim-bearing sections, especially when prior completed research items are used as scaffolding during drafting.
