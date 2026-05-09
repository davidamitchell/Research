# 2026-05-09 -- Research Loop (build-vs-improve-throughput-tradeoff)

**Completed:**

Research item:
- `Research/completed/2026-05-09-build-vs-improve-throughput-tradeoff.md` -- completed; the item concludes that organisations should not use a fixed build-versus-improve percentage, but should shift capacity toward system improvement when bottlenecks, queue growth, toil, instability, or hotspot concentration become the active constraint. It combines Theory of Constraints, Little's Law, technical-debt drag, Site Reliability Engineering toil guidance, platform-engineering capability investment, and Pareto-style hotspot targeting into a trigger-based allocation rule.

Sources consulted:
- https://econpapers.repec.org/RePEc:inm:oropre:v:9:y:1961:i:3:p:383-387 (Little's Law abstract and bibliographic record)
- https://www.tocinstitute.org/five-focusing-steps.html (Theory of Constraints focusing-step definition and bottleneck guidance)
- https://dora.dev/guides/dora-metrics/ (delivery throughput and instability guidance)

## Mini-Retro

1. **Did the process work?** Yes. The review loop surfaced concrete citation-discipline issues early enough to correct them before completion, and the second-pass auto-pass path still allowed the item to move forward after the required fixes.
2. **What slowed down or went wrong?** The first draft leaned on tertiary definition sources and review-metadata text inside `## Research Skill Output`, which triggered avoidable review failures and an extra iteration.
3. **What single change would prevent this next time?** Nothing beyond applying the existing citation-discipline checks more aggressively before the first draft commit.
4. **Is this a pattern?** Yes. It matches the repository's existing citation-discipline pattern: source authority and review-safe wording remain the most common reasons research items need one extra pass.
