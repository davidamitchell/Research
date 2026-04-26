# 2026-04-26 -- Research Loop (ai-agent-control-plane-architecture-enterprise)

**Completed:**

Research item:
- `Research/completed/2026-04-26-ai-agent-control-plane-architecture-enterprise.md` -- completed; the item concludes that enterprise AI and low-code governance needs a composite control plane with central policy decision and administration, translation and distribution services, heterogeneous enforcement adapters, and a closed-loop evidence system. It also lays out a bootstrap path that starts with inventory, risk-tier intake, guardrails, and logging before deeper runtime automation.

Sources consulted:
- https://csrc.nist.gov/pubs/sp/800/207/final (zero trust component model)
- https://www.openpolicyagent.org/docs/latest/philosophy/ (decoupled policy engine pattern)
- https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-72 (post-market monitoring loop)

## Mini-Retro

1. **Did the process work?** Yes, the workflow and review loop produced a completed item with a coherent architecture and a stronger evidence map after one correction pass.
2. **What slowed down or went wrong?** The first review pass exposed two recurring failure modes: a claim that spanned more control surfaces than its citations directly supported, and an access-note sentence that described a dead seeded URL without treating the replacement-source boundary carefully enough.
3. **What single change would prevent this next time?** Add an explicit self-review check that dead seeded URLs must be replaced in `## Sources` and that multi-surface architecture claims must either cite each surface directly or be narrowed before draft.
4. **Is this a pattern?** Yes, it matches the broader citation-discipline pattern already visible in this repo: architectural synthesis fails review when source scope is wider or narrower than the sentence that cites it.

## Applied improvements

- Updated `research-prompt.md` to add a self-review rule for replacing dead seeded URLs with working official sources and for narrowing multi-surface architecture claims when the cited evidence does not directly support every named surface.

## Pending skill improvements

- Mirror the same source-substitution and multi-surface-claim audit into `.github/skills/research/SKILL.md` in the Skills repo, because the review failure came from research-skill behavior rather than item-specific domain content.
