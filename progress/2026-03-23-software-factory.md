# 2026-03-23 — Research Loop (software-factory)

**Completed:**

Research item:
- `Research/in-progress/2026-03-23-software-factory.md` — draft; the software factory concept (AI coding agents replacing manual code production) is production-validated at Stripe scale (1,300+ AI-authored PRs/week) and the TOC analysis predicts that when software scarcity is removed, the governance apparatus built around it (SAFe, investment boards, QA teams) becomes unnecessary overhead; mid-tier banks have a closing window of approximately 2–4 years to redesign their delivery process before AI-native fintechs close the regulatory and domain-data gap.

Sources consulted:
- https://alexop.dev/posts/the-software-factory/ (primary source article: software factory concept, Beer Commerce example, Stripe Minions, Gas Town, skills, backpressure)
- https://news.ycombinator.com/item?id=47226107 (HN: OctopusGarden dark factory implementation — six documented challenges including compliance, debuggability, security)
- https://news.ycombinator.com/item?id=47435275 (HN: TTal multi-agent orchestration tool — two-plane manager/worker architecture)
- https://stripe.dev/blog/minions-stripes-one-shot-end-to-end-coding-agents (via web search: Stripe Minions architecture, blueprints, Toolshed, devboxes)
- Web search: TOC in software development and AI bottleneck migration (velocityschedulingsystem.com, theagilemindset.co.uk, isixsigma.com)
- Web search: AI-native organisations (HBS Online, Forbes Business Council, Scrum.org, Deloitte Insights 2026)
- Web search: mid-tier bank modernisation (Finastra, IBM IBV, McKinsey, Appinventiv, Pega)
- Web search: cost of software approaching zero (BCG, Goldman Sachs, LangChain State of Agents, CloudZero)
- Prior research: `Research/completed/2026-02-28-ai-strategy-swe-focus.md` (ANZ 40–55%, DORA 2024 data, Google 25%)
- Prior research: `Research/completed/2026-03-14-reliable-software-llm-era.md` (cognitive debt, Quint, reliability risks)
- Prior research: `Research/completed/2026-03-21-technology-capability-models.md` (capability taxonomy landscape)

## Mini-Retro

1. **Did the process work?** Yes. Parallel web fetching of the three source URLs and three supplementary searches produced enough material to complete all §0–§7 sections without needing additional rounds. The prior repository research cross-references were directly useful (DORA data, cognitive debt, transaction cost theory).

2. **What slowed down or went wrong?** The HN discussion threads were single-post items (the "Show HN" submissions) rather than threaded discussions, so the practitioner depth was limited to the original authors' notes. The Stripe Minions blog was not directly fetchable (returned Stripe's front page), requiring reliance on secondary web search summaries — medium confidence rather than high.

3. **What single change would prevent this next time?** For HN threads, prefer fetching the full thread (all comments) rather than just the root post — the comments typically contain the richest practitioner counterarguments and failure modes.

4. **Is this a pattern?** Partially. The Stripe direct-URL limitation is a recurring issue with vendor blog posts that require JavaScript rendering; the workaround (web search for secondary summaries) is reliable but downgrades confidence. This has appeared before with other vendor blogs.
