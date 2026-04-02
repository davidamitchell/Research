---
title: "The shape of organisations when software is no longer the constraint"
added: 2026-04-02
status: backlog  # backlog | in-progress | reviewing | completed
priority: high  # low | medium | high
blocks: []
tags: [org-design, ai, software-cost, future-of-work, management, product-management, transaction-costs, agile, automation]
started: ~
completed: ~
output: [knowledge]
---

# The shape of organisations when software is no longer the constraint

## Research Question

Inside an organisation that requires software to be built, integrated, and maintained (including Commercial Off-The-Shelf (COTS) systems, Software-as-a-Service (SaaS) platforms, and bespoke-built systems), how much of that organisation exists purely to manage the shaping, prioritising, management, or tracking of that work — and how does the organisation's structure change when the cost of producing software approaches zero?

Supporting questions:
- What fraction of a typical software-dependent organisation's headcount exists primarily to coordinate, manage, or govern software delivery rather than to deliver it directly?
- Which specific roles and functions exist as proxies or translators between business intent and software execution?
- What does economic theory (particularly transaction-cost economics) predict about firm shape when one major production cost collapses?
- What historical analogues exist — automation of manufacturing, adoption of cloud computing, introduction of Enterprise Resource Planning (ERP) — and what did they do to organisational structure?
- What does "software cost going to zero" mean in practice today (Artificial Intelligence (AI)-assisted development, AI coding agents, natural-language-to-code pipelines)?
- Which coordination and management functions could themselves be automated, and which require irreducible human judgment?
- What happens to Agile rituals, planning cycles, estimation, and roadmapping when throughput is no longer the binding constraint?

## Scope

**In scope:**
- Roles and functions that exist primarily to shape, prioritise, manage, track, or govern software work: Product Managers (PMs), Project Managers, Business Analysts (BAs), Scrum Masters, Programme Managers, Delivery Managers, Solution Architects acting as go-betweens, Change and Release Managers, and middle management layers coordinating these functions
- Economic and organisational theory relevant to how constraint changes reshape firm structure (transaction-cost economics, Theory of the Firm, resource-based view)
- Historical case studies of constraint removal: factory automation and supervisory overhead, ERP adoption and headcount in IT departments, cloud computing and operations staffing, low-code/no-code platforms and IT gatekeeping
- Current and near-term AI coding tools and agents (GitHub Copilot, Cursor, Devin, OpenAI Codex, Claude code tools) as empirical data points on cost reduction
- Empirical research and analyst estimates of what proportion of software-delivery organisations is management/coordination overhead
- Second-order effects: what new coordination work emerges if software production becomes abundant (e.g. governing many more smaller systems, managing AI agent outputs)

**Out of scope:**
- Deep technical treatment of specific AI coding tools (treated as inputs, not the subject)
- Pure software engineering productivity research not connected to organisational structure
- Startups and small teams where flat structure is already the norm; focus is on mid-to-large organisations
- Government and defence software organisations (sufficiently different dynamics to warrant a separate item)

**Constraints:** Publicly available sources. Empirical data on headcount ratios is sparse — clearly distinguish [fact] from [inference] and [assumption] throughout.

## Context

The issue motivating this research is stark: a large proportion of every software-dependent organisation exists not to write, deploy, or operate software, but to manage the process of getting software written, deployed, and operated. Product roadmaps, sprint ceremonies, backlog grooming, change advisory boards, portfolio governance, steering committees — these structures exist because software production has historically been slow, expensive, uncertain, and hard for non-technical stakeholders to specify or validate.

AI coding agents and natural-language-to-code pipelines are compressing the cost curve rapidly. If a capable AI can translate a clear business intent into working, tested, deployed software in hours rather than months, the question is no longer "how do we manage scarce engineering capacity?" but "how do we decide what to build?" — and it is not obvious that the existing organisational machinery is the right answer to that question either.

This connects to the deeper question: how much of the modern organisation is a response to the specific historical cost structure of software, and how much would survive a world where that cost structure changes fundamentally?

## Approach

1. **Map the coordination layer** — Identify and categorise the roles and functions in a typical software-delivery organisation that exist primarily to manage, govern, or facilitate software work rather than to produce it. Use job descriptions, organisational design literature, and analyst frameworks to estimate the proportion of total headcount these represent.
2. **Apply transaction-cost theory** — Review Coase's Theory of the Firm and Williamson's transaction-cost economics. Assess what these predict when a major category of production cost (software development) is dramatically reduced. What does theory say about firm boundaries, vertical integration, and internal hierarchy when this changes?
3. **Mine historical analogues** — Research what happened to organisational structure during: (a) factory automation in manufacturing, (b) ERP adoption in the 1990s–2000s, (c) cloud computing adoption, (d) low-code/no-code platform adoption. Did coordination overhead reduce? Did it shift? Did it grow?
4. **Survey current evidence on AI coding productivity** — Gather published data on AI coding tool productivity multipliers (developer throughput, time-to-deploy, defect rates). Extrapolate: what does a 5×, 10×, or 100× productivity improvement imply for the size of the coordination layer relative to the delivery layer?
5. **Identify automatable versus irreducible coordination** — For each category of coordination work (roadmapping, prioritisation, stakeholder alignment, estimation, status reporting, change management), assess which are amenable to AI automation and which require human judgment. Use existing AI agent capability benchmarks and qualitative reasoning.
6. **Second-order effects** — Consider what new coordination demands emerge: more frequent releases, more systems, AI-generated code that needs reviewing, more diverse stakeholder requests enabled by lower build costs, governance of AI agents themselves.
7. **Synthesis** — Describe 3–5 plausible future organisational shapes for software-dependent organisations, differentiated by how aggressively they restructure in response to falling software costs. Identify the decision points (make vs. buy, centralise vs. federate, human vs. AI coordination) that determine which shape a given organisation adopts.

## Sources

- [ ] [The Nature of the Firm — Ronald Coase (1937)](https://onlinelibrary.wiley.com/doi/full/10.1111/j.1468-0335.1937.tb00002.x) — foundational paper on transaction-cost economics and why firms exist; directly relevant to how firm shape changes when transaction costs fall
- [ ] [Markets and Hierarchies — Oliver Williamson (1975)](https://www.hup.harvard.edu/books/9780029348208) — extends Coase; provides framework for predicting when hierarchies shrink in favour of markets as costs fall
- [ ] [The Second Machine Age — Brynjolfsson and McAfee (2014)](https://www.amazon.com/Second-Machine-Age-Prosperity-Technologies/dp/0393350649) — examines labour market and organisational effects of digital automation; Chapter 11 on organisational change
- [ ] [McKinsey: The state of AI in software development (2023)](https://www.mckinsey.com/capabilities/mckinsey-digital/our-insights/unleashing-developer-productivity-with-generative-ai) — analyst data on AI coding productivity multipliers and developer experience
- [ ] [GitHub Copilot productivity research (Kalliamvakou, 2022)](https://github.blog/2022-09-07-research-quantifying-github-copilots-impact-on-developer-productivity-and-happiness/) — empirical study showing 55% faster task completion with Copilot; baseline for extrapolating constraint removal
- [ ] [Stripe: The developer coefficient (2018)](https://stripe.com/files/reports/the-developer-coefficient.pdf) — survey-based estimate that developers spend only 32% of their time writing code; rest is coordination, meetings, context-switching; quantifies the current coordination burden
- [ ] [CHAOS Report — Standish Group](https://www.standishgroup.com/sample_research_files/CHAOSReport2015-Final.pdf) — long-running dataset on software project outcomes; context for why coordination overhead grew historically
- [ ] [Devin AI — Cognition Labs](https://www.cognition.ai/blog/introducing-devin) — first public demonstration of an autonomous AI software engineer; signal for where the cost curve is heading
- [ ] [Cursor — AI code editor](https://cursor.com) — current leading AI-assisted coding environment; empirical evidence of productivity change for individual developers
- [ ] [The Mythical Man-Month — Fred Brooks (1975)](https://www.amazon.com/Mythical-Man-Month-Software-Engineering-Anniversary/dp/0201835959) — classic analysis of why adding people to late software projects makes them later; relevant to understanding why coordination overhead scales poorly and what removing the scarcity constraint might change
- [ ] [Wired: "Vibe coding" and the future of software (2025)](https://www.wired.com/story/vibe-coding-future-of-software/) — contemporary reporting on natural-language-to-code development and its organisational implications
- [ ] [HBR: What happens to management when AI writes the code? (search)](https://hbr.org) — search Harvard Business Review for relevant management and organisational design analysis of AI coding tools
- [ ] [a16z: Software is eating the world — Marc Andreessen (2011)](https://a16z.com/why-software-is-eating-the-world/) — foundational framing of software as the dominant production factor; context for what "software cost going to zero" reverses
- [ ] [Gartner: Low-code/no-code market and organisational impact](https://www.gartner.com/en/information-technology/insights/low-code-no-code) — earlier wave of "democratised software" and its actual organisational effects; a closer historical analogue than full automation
- [ ] [MIT Sloan: The Future of Organisation Design with AI (search)](https://sloanreview.mit.edu) — search for research on AI and organisational structure changes
- [ ] [Stack Overflow Developer Survey 2024](https://survey.stackoverflow.co/2024/) — developer time allocation, tooling adoption, and AI usage; empirical baseline

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

### Key Findings

1.
2.

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| | | high / medium / low | |

### Assumptions

- **Assumption:** ... **Justification:** ...

### Analysis

### Risks, Gaps, and Uncertainties

-

### Open Questions

-

---

## Output

- Type: knowledge
- Description:
- Links:
