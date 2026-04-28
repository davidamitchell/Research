---
title: "Which software categories face declining demand versus increasing demand as AI coding agents make custom software generation cheap?"
added: 2026-04-28T21:06:12+00:00
status: backlog  # backlog | in-progress | reviewing | completed
priority: medium  # low | medium | high
blocks: []  # slugs (filename without .md) of backlog items that cannot start until this one is complete
tags: [ai, software-cost, saas, build-vs-buy, idp, internal-developer-platform, hosting, platform-engineering, market-structure, ai-coding, transaction-costs]
started: ~
completed: ~
output: [knowledge]  # skill | tool | agent | knowledge | backlog-item
cites: []          # slugs of items this item directly depends on or quotes
related: [2026-04-02-org-shape-software-cost-zero, 2026-03-23-software-factory, 2026-04-26-software-engineering-investment-case-llm]        # slugs of thematically connected items
superseded_by: ~   # slug of a later item that overrides this one (null if not superseded)
supersedes: ~      # slug of an older item this one replaces (null if not applicable)
item_type: primary # primary | synthesis
confidence: medium # high | medium | low
versions: []       # entries: {version: "1.0", sha: "<commit-hash>", changed: YYYY-MM-DD, progress: "<path>", summary: "<one-line>"}
---

# Which software categories face declining demand versus increasing demand as AI coding agents make custom software generation cheap?

## Research Question

As Artificial Intelligence (AI) coding agents (such as Anthropic Claude Code, OpenAI Codex, and GitHub Copilot Workspace) make custom software generation materially cheaper, which categories of commercial software face declining demand because the build-it-yourself path becomes viable, which categories face increasing demand because cheaper software production amplifies the need for them, and what structural properties distinguish each group?

## Scope

**In scope:**
- Commercial and Software-as-a-Service (SaaS) software categories whose demand is plausibly affected by AI coding agents reducing custom software build costs
- The build-vs-buy decision framework and how it shifts when build cost approaches zero (transaction-cost economics lens)
- Specific examples of software categories facing demand decline: niche vertical SaaS, simple CRUD (Create-Read-Update-Delete) applications, basic reporting and dashboarding tools, workflow automation tools with narrow scope
- Specific examples of software categories facing demand increase: Internal Developer Platforms (IDPs), cloud hosting and infrastructure, observability and monitoring platforms, CI/CD (Continuous Integration / Continuous Delivery) pipeline tooling, auth/identity services, deployment infrastructure
- Structural properties that predict which category a class of software falls into (e.g., network effects, data gravity, multi-tenancy advantages, regulatory compliance moat, infrastructure complexity)
- Historical analogues: what happened to related software categories when prior constraint-removals occurred (e.g., cloud computing and server management software, spreadsheets and custom business application demand)

**Out of scope:**
- Deep technical treatment of any specific AI coding tool (Claude Code, Codex, etc.)
- Open-source software economics (distinct dynamics from commercial SaaS demand)
- Hardware and embedded systems categories
- Pure enterprise-internal tooling choices (covered by `2026-04-02-org-shape-software-cost-zero`)

**Constraints:** Near-term horizon (1–5 years); commercial software market focus; must produce a reusable taxonomy/classification framework, not just a list of examples

## Context

There is growing discussion — from practitioner commentary, investor analysis, and technology forecasting — that AI coding agents are beginning to shift the classic build-vs-buy calculus for software. Tools like Claude Code and Codex lower the marginal cost of building custom software dramatically, which should, if the economics hold, reduce demand for software whose main value proposition is that it would otherwise be expensive to build. At the same time, the more software is produced, the more demand grows for the infrastructure layer that runs, governs, and observes it: hosting platforms, Internal Developer Platforms (IDPs), deployment pipelines, identity and access management, and observability tooling. Understanding which software categories fall into each camp — and what structural property explains the difference — informs platform investment strategy, product roadmap decisions, and enterprise tooling choices. This item directly extends the "org shape when software cost is zero" research (`2026-04-02-org-shape-software-cost-zero`) by shifting the lens from organisational structure to software market structure.

## Approach

1. **Economic framing**: Apply the build-vs-buy transaction-cost model to derive when declining build cost shifts the decision boundary. Identify the categories of utility a piece of software can provide and which of those utilities lose their buy-premium when build cost drops.
2. **Declining-demand category identification**: Gather examples and analyst commentary on SaaS and commercial software categories that are already seeing, or are predicted to see, demand decline due to AI coding. Characterise each by its structural properties.
3. **Increasing-demand category identification**: Gather examples of software categories that benefit from more software being produced — hosting, IDPs, CI/CD, observability, auth/identity — and characterise why each grows rather than shrinks.
4. **Structural property taxonomy**: Identify the distinguishing structural properties (network effects, data gravity, compliance moat, infrastructure complexity, multi-tenancy advantage, etc.) that predict which side of the divide a category falls on. Produce a two-by-two or equivalent classification framework.
5. **Historical analogue check**: Compare the predicted pattern against what actually happened in prior constraint-removal episodes (cloud and server management, low-code and IT gatekeeping) to test and calibrate the framework.
6. **Synthesis**: Produce a classification framework with worked examples for each category, including example products/categories for each cell, and a brief investment/strategy implication per class.

## Sources

Starting points — papers, articles, videos, repos, docs.
**Every source must include a URL.** Use `[Display Name](https://url)` for named sources or a bare `https://url` for direct links. Sources without URLs cannot be verified or linked on the site.

- [ ] [Shopify CEO Tobi Lütke on AI and building software](https://x.com/tobi/status/1909231945071276226) — practitioner example of shifting build-vs-buy calculus
- [ ] [a16z: The New Stack for Software](https://a16z.com/the-new-stack-for-ai/) — investor framing on infrastructure benefiting from AI proliferation
- [ ] [Simon Willison on AI tools changing what's worth building](https://simonwillison.net/) — practitioner commentary on the build frontier shifting
- [ ] [Benedict Evans on AI and SaaS disruption](https://www.ben-evans.com/) — market analysis of software category dynamics under AI
- [ ] [Coase's Theory of the Firm (Wikipedia summary)](https://en.wikipedia.org/wiki/Theory_of_the_firm) — transaction-cost economics foundation for build-vs-buy analysis

---

## Research Skill Output

*(Full output from running the research skill — retained verbatim in the completed item. §§0–5 are the investigation; §6 seeds the Findings section below.)*

### §0 Initialise

-

### §1 Question Decomposition

-

### §2 Investigation

-

### §3 Reasoning

-

### §4 Consistency Check

-

### §5 Depth and Breadth Expansion

-

### §6 Synthesis

*(This section seeds the Findings below.)*

**Executive summary:**

**Key findings:**

**Evidence map:**

**Assumptions:**

**Analysis:**

**Risks, gaps, uncertainties:**

**Open questions:**

### §7 Recursive Review

-

---

## Findings

*(Populated from §6 Synthesis above.)*

### Executive Summary

3–5 sentences. What is the answer to the research question? State the key conclusion directly.

### Key Findings

Ordered list. Each finding is a specific, evidence-backed claim.

1.
2.

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| | | high / medium / low | |

### Assumptions

Explicit assumptions made during the investigation and the justification for each.

- **Assumption:** ... **Justification:** ...

### Analysis

How the evidence was weighed, what trade-offs were identified, and how competing interpretations were resolved.

### Risks, Gaps, and Uncertainties

What is still unknown? Where does the evidence fall short? What could change the conclusion?

-

### Open Questions

Questions that surfaced during research but are out of scope for this item. Each may become a new backlog item.

-

---

## Output

*(Fill in when completing — what was produced as a result of this research?)*

- Type: knowledge
- Description:
- Links:
