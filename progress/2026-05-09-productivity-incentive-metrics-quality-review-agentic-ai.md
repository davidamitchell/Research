# 2026-05-09 -- Research Loop (productivity-incentive-metrics-quality-review-agentic-ai)

**Completed:**

Research item:
- `Research/completed/2026-05-08-productivity-incentive-metrics-quality-review-agentic-ai.md` -- completed; the item concludes that acceptance rate and code volume are local-usefulness signals, not standalone net-value metrics, and that organisations need a team-level multi-metric scorecard that pairs speed with stability, maintainability, review quality, and capability retention. It also shows that repository-scale evidence can diverge from bounded-task gains, so speed-focused mandates risk hiding quality costs in rework, review collapse, and technical debt.

Sources consulted:
- https://dora.dev/research/2025/measurement-frameworks/ (official DORA guidance on AI-era measurement frameworks)
- https://cloud.google.com/blog/products/devops-sre/announcing-the-2024-dora-report (official DORA evidence on AI adoption trade-offs)
- https://arxiv.org/html/2511.04427v2 (repository-level evidence on transient velocity gains and persistent quality degradation)

## Mini-Retro

1. **Did the process work?** Yes, the research loop and review workflow surfaced the main evidence-label and definition issues before completion.
2. **What slowed down or went wrong?** The review workflow required two iterations because several cross-source synthesis claims were initially labeled too strongly and a couple of management terms were clearer when rewritten into plain language.
3. **What single change would prevent this next time?** Start by phrasing cross-source conclusions as inferences by default, and rewrite soft management jargon into plain descriptive language before the first review pass.
4. **Is this a pattern?** No. This session mostly reinforced the existing rule that synthesis claims and coined labels need especially careful wording.

## Applied improvements

- Updated `research-prompt.md` to add a self-review check that cross-source package claims using management jargon default to plain language or explicit authoritative definitions, and default to `[inference]` when they synthesise multiple sourced components.
