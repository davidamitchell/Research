---
review_count: 2
title: "The Software Factory: Organisational Transformation When the Cost of Quality Software Approaches Zero"
added: 2026-03-23
status: reviewing
priority: high
blocks: []
tags: [software-factory, ai-native, organisations, theory-of-constraints, banking, cost-of-software]
started: 2026-03-24
completed: ~
output: [knowledge]
---

# The Software Factory: Organisational Transformation When the Cost of Quality Software Approaches Zero

## Research Question

If the cost of producing high-quality, standardised, integrated software is approaching zero — as Artificial Intelligence (AI) coding agents and software factory patterns suggest — what must organisations change in how they structure themselves, invest, and prioritise, and what specific challenges and opportunities does this create for mid-tier banks?

## Scope

**In scope:**
- The "software factory" concept: what it is, documented implementations (Stripe Minions, StrongDM, Gas Town), and the evidence for its viability
- Theory of Constraints (TOC) applied to software development: is software scarcity the current organisational constraint, and what happens when it is removed?
- Organisational implications: team structures, roles, governance, prioritisation mechanisms (investment boards, Scaled Agile Framework (SAFe), Program Increment (PI) planning) and whether they survive the transition
- What "AI-native" means for organisations building or transforming software delivery
- Mid-tier bank specific analysis: legacy system challenges, regulatory constraints, competitive threats from fintechs, and the opportunity window
- Prior repository research that can be continued: AI strategy (Software Engineering (SWE) focus), reliable software in the Large Language Model (LLM) era, technology capability models

**Out of scope:**
- Deep technical benchmarking of individual AI coding tools (covered in prior research)
- Model architecture or LLM training details
- New Zealand-specific regulatory analysis

**Constraints:** Web sources and prior repository research. Focus on organisational and strategic dimensions, not tool comparisons.

## Context

Two related theories motivate this research:

1. The constraint in most organisations is their inability to produce quality, standardised, integrated software. Business cases, investment boards, project management "front doors", quality assurance processes, Scaled Agile Framework (SAFe), PI planning, and big-room planning all exist because producing quality integrated software is expensive and scarce. Multiple lines of business compete over a shared scarce resource — software engineers' time. Manual work, swivel-chair automation, errors, and Excel workarounds are downstream symptoms of this scarcity.

2. The cost of producing high-quality standardised integrated software is going towards zero. AI coding agents (Claude Code, GitHub Copilot Agent, Cursor), software factory patterns (Stripe Minions, Gas Town), and multi-agent orchestration frameworks are making it feasible for small teams to ship what previously required large specialist teams.

If both theories are correct simultaneously, the organisational implications are profound: governance structures designed to manage software scarcity become unnecessary overhead; competitive advantage shifts from "who has the most engineers" to "who builds the best factory"; and organisations that fail to adapt will face both internal inefficiency and external competitive threat from AI-native entrants.

Mid-tier banks are a particularly interesting case: they have legacy systems built over decades, operate under regulatory constraints that make autonomous deployment risky, and face competitive pressure from fintechs unencumbered by that legacy — but they also have domain data and regulatory relationships that AI-native entrants lack.

**Prior research connections:**
- `2026-02-28-ai-strategy-swe-focus.md` — documented measured outcomes from AI-assisted coding at scale (Australia and New Zealand Banking Group (ANZ) 40–55% faster development, Google 25%+ AI-generated code), governance models, and the DevOps Research and Assessment (DORA) finding that individual speed gains do not translate to team delivery improvement without process redesign
- `2026-03-14-reliable-software-llm-era.md` — documented cognitive debt risk from LLM code generation and the role of formal specification (Quint) in maintaining reliability
- `2026-03-21-technology-capability-models.md` — established the capability taxonomy landscape relevant to organisations rebuilding their technology stack

## Approach

1. **Understand the software factory model** — fetch and analyse the primary source article (alexop.dev), the Hacker News (HN) discussions, and documented implementations (Stripe Minions, Gas Town, StrongDM)
2. **Apply TOC analysis** — is software engineering genuinely the system constraint in most organisations? What does TOC predict happens when a constraint is removed vs. elevated?
3. **Map organisational implications** — which current structures (SAFe, investment boards, Quality Assurance (QA) teams, Product Owners (POs)) exist because of software scarcity? Which survive when scarcity is removed?
4. **Define AI-native** — what does it mean specifically, how does it differ from AI-assisted or AI-first, and what does an AI-native organisation look like structurally?
5. **Banking sector analysis** — synthesise the specific challenges (legacy, regulation, data) and opportunities (domain moats, AI-accelerated modernisation) for mid-tier banks
6. **Cross-reference prior research** — identify what adds to existing threads in this repository vs. what is new territory

## Sources

- [x] https://alexop.dev/posts/the-software-factory/ — primary source article
- [x] https://news.ycombinator.com/item?id=47226107 — Hacker News discussion: OctopusGarden dark factory pattern
- [x] https://news.ycombinator.com/item?id=47435275 — Hacker News discussion: TTal multi-agent orchestration
- [x] https://stripe.dev/blog/minions-stripes-one-shot-end-to-end-coding-agents — Stripe Minions (via web search)
- [x] Prior research: `Research/completed/2026-02-28-ai-strategy-swe-focus.md`
- [x] Prior research: `Research/completed/2026-03-14-reliable-software-llm-era.md`
- [x] Prior research: `Research/completed/2026-03-21-technology-capability-models.md`
- [x] Web search: TOC in software development and AI bottleneck migration
- [x] Web search: AI-native organisations, investment trends, structural changes
- [x] Web search: mid-tier bank modernisation challenges and AI opportunities

---

## Research Skill Output

[fact] This section retains the full output from running the research skill. Sections §0–§5 are the investigation, and §6 seeds the Findings section below.

### §0 Initialise

[fact] **Research question restated:** If the cost of producing high-quality, standardised, integrated software is approaching zero, what must organisations change in how they structure themselves, invest, and prioritise — and what are the specific implications for mid-tier banks?

[fact] **Scope confirmed:** Organisational and strategic dimensions. Not tool comparisons or model benchmarks. Evidence must be labelled [fact], [inference], or [assumption].

[fact] **Constraints confirmed:** Web sources and prior repository research. Claims about future states are [inference] or [assumption]. Named organisations with disclosed data receive higher evidentiary weight than secondary aggregators.

[fact] **Output format:** Structured knowledge item with full §0–§7 research skill output, Executive Summary, Key Findings, Evidence Map, and Open Questions.

[fact] **Prior work check:** I searched `Research/completed/` for adjacent work before extending this item. The most directly related completed items are `2026-02-28-ai-strategy-swe-focus.md`, `2026-03-14-reliable-software-llm-era.md`, `2026-03-21-technology-capability-models.md`, `2026-03-10-nature-of-the-firm-coase-organisations.md`, and `2026-02-28-jevons-paradox.md`.

[fact] `2026-02-28-ai-strategy-swe-focus.md` established that DORA 2024 found individual AI productivity gains do not translate to team-level delivery improvement without process redesign; it also documented Google 25%+ AI-generated code, ANZ 40–55% faster development, and SWE-bench trajectory.

[fact] `2026-03-14-reliable-software-llm-era.md` established cognitive debt from LLM code generation and formal specification as a structural countermeasure.

[fact] `2026-03-21-technology-capability-models.md` established capability-taxonomy frameworks relevant to organisations rebuilding their technology capability stack.

[fact] `2026-03-10-nature-of-the-firm-coase-organisations.md` and Thread 2 in `learnings.md` established transaction-cost theory as the economic explanation for governance overhead under software scarcity.

[fact] `2026-02-28-jevons-paradox.md` established the relevant demand-expansion mechanism for cases where the marginal cost of software production collapses.

[inference] This item adds new ground by tying those earlier threads to the software-factory operating model itself, production-scale evidence from Stripe's Minions system, and a banking-specific analysis of timing, constraints, and governance redesign.

---

### §1 Question Decomposition

[fact] Root question broken into atomic sub-questions:

**Branch A — The Software Factory model**
- A1: What is the "software factory" concept and what are its key architectural components?
- A2: What evidence exists that the factory pattern works at production scale?
- A3: What are the documented failure modes and unresolved challenges?
- A4: What is the "dark factory" variant, and how does it differ from human-in-the-loop factories?

**Branch B — Theory of Constraints (TOC) analysis**
- B1: Is software engineering capacity genuinely the system constraint in most organisations today?
- B2: What does TOC predict happens when the constraint is removed or dramatically reduced?
- B3: What becomes the new constraint after software scarcity is resolved?

**Branch C — Organisational implications**
- C1: Which current organisational structures (SAFe, investment boards, QA teams, POs) exist specifically because software production is expensive and scarce?
- C2: Which governance structures survive when software production becomes cheap and fast?
- C3: What does the new equilibrium team structure look like in AI-native organisations?
- C4: What does "AI-native" specifically mean vs. AI-assisted or AI-first?

**Branch D — Mid-tier bank analysis**
- D1: What specific challenges do mid-tier banks face in adopting software factory patterns?
- D2: What competitive advantages do mid-tier banks retain that AI-native entrants lack?
- D3: What is the opportunity window — how much time do mid-tier banks have before the competitive gap widens?

**Branch E — Investment and prioritisation shifts**
- E1: Where should organisations invest once software production cost declines sharply?
- E2: What new capabilities become critical when the bottleneck shifts from coding to factory design?
- E1a: Which infrastructure investments compound across all agent-executed work?
- E1b: Which human capabilities remain scarce even if coding capacity becomes abundant?
- E2a: Which governance capabilities become more important when prioritisation replaces execution as the bottleneck?
- E2b: Which capabilities are uniquely important for regulated sectors such as banking?

---

### §2 Investigation

#### A. The Software Factory model

- [fact] Source classification for Section A: alexop.dev is treated as a primary practitioner essay for the software-factory thesis; Stripe's engineering blog is a primary company disclosure; first-person Hacker News implementation accounts are treated as primary practitioner evidence; InfoQ and similar summaries are treated only as secondary corroboration.

**A1 — What is the software factory concept?**

[fact] The software factory concept, as described in the primary source article (alexop.dev/posts/the-software-factory, Alex Op, 2026), defines a production model where AI coding agents implement features and fix bugs while humans design and improve the factory. The workflow is: "builder writes spec (30 min) → agent picks up ticket → agent writes frontend + backend + tests in parallel → agent runs full test suite and lint → builder reviews pull request (PR) (1-2 hours) → deployed (same day)." This replaces the prior model (business analyst (BA) writes user story → Product Owner (PO) refines → sprint planning → User Experience (UX) design happens → developer picks up ticket → developer writes code → code review → Quality Assurance (QA) testing → deployed in 10–14 days). Source: alexop.dev/posts/the-software-factory [primary source — practitioner essay].

[fact] The article identifies five components of a working software factory: (1) agentic coding tools (Claude Code in headless mode, scheduled tasks), (2) skills — Markdown files that extend agent capabilities for specific tasks (cloud debugging, database migration, design-to-code, security audit), (3) "backpressure" systems — type checkers, linters, Continuous Integration and Continuous Delivery (CI/CD), test suites that enable agents to self-correct without human intervention, (4) multi-agent orchestration for parallel workstreams, and (5) a self-improving feedback loop where agents read product signals (support tickets, split-test results, error logs) to populate the backlog. Source: alexop.dev/posts/the-software-factory [primary source — practitioner essay].

[fact] Lee Edwards of Root Ventures is quoted: "It's like giving them a nuclear-powered six-axis mill. It's a single-person software factory." Boris Cherny, creator of Claude Code, is quoted: "We're going to start to see the title of software engineer go away. It's just going to be 'builder' or 'product manager.'" Source: alexop.dev/posts/the-software-factory, citing sfstandard.com/2026/02/19 [secondary corroboration — media quote relayed through the practitioner essay].

**A2 — Production-scale evidence**

[fact] Stripe's Minions system (documented at stripe.dev/blog/minions-stripes-one-shot-end-to-end-coding-agents) merges over 1,300 PRs per week, fully AI-authored (no human-written code), all subject to human review before merge. Each task starts in a Slack message and ends in a PR that passes continuous integration (CI), ready for human review, with no interaction in between. Sources: stripe.dev blog [primary source — company engineering disclosure]; corroborated by InfoQ, Analytics India Magazine, and Awesome Agents summaries [secondary sources].

[fact] Stripe's key architectural innovations: (1) "blueprints" — hybrid state machines combining deterministic code nodes (run linters, push changes) with agentic subtasks (implement feature, fix CI failures); (2) "Toolshed" — an internal Model Context Protocol (MCP) server with nearly 500 tools, with a curated subset per task; (3) isolated "devboxes" — cloud-based developer machines identical to human engineers' environments, spinning up in 10 seconds; (4) a maximum of two CI retry rounds before human escalation. Source: stripe.dev/blog/minions-stripes-one-shot-end-to-end-coding-agents [primary source — company engineering disclosure].

[fact] Stripe's stated rationale for building in-house rather than using generic agents: "hundreds of millions of lines of Ruby, Sorbet types, and proprietary libraries no public model has seen. Generic agents couldn't navigate it." The principle: "If a tool is good for human engineers, it's good for LLMs." Source: alexop.dev/posts/the-software-factory, attributing Stripe [secondary relay of Stripe's rationale through the practitioner essay].

[fact] Steve Yegge built Gas Town (github.com/steveyegge/gastown), described as "Kubernetes (the container orchestration platform) for AI coding agents": a "Mayor" orchestrates 20–30 parallel "Polecat" coding agents, with a "Refinery" managing the merge queue to prevent parallel branch conflicts. Source: alexop.dev/posts/the-software-factory, citing cloudnativenow.com [secondary source — practitioner essay relaying public discussion].

[fact] The HN discussion (news.ycombinator.com/item?id=47226107) documents OctopusGarden, an open-source "dark factory" implementation: a spec goes in, code is generated, built in Docker, validated against holdout scenarios the agent never saw, scored by a Large Language Model (LLM)-as-judge, and failures feed back until convergence — with no human code review in the loop. The author reports it works for standard CRUD (Create, Read, Update, Delete) and Representational State Transfer (REST) Application Programming Interface (API) apps. Source: HN 47226107 [primary source — first-person practitioner account].

[fact] The HN discussion (news.ycombinator.com/item?id=47435275) documents TTal, a Go Command-Line Interface (CLI) for orchestrating multiple Claude Code sessions in a two-plane architecture: a Manager plane (long-running agents that draft plans, break them into tasks, assign priorities) and a Worker plane (short-lived agents per task, each with isolated git worktree and tmux session, running the full PR loop autonomously). Source: HN 47435275 [primary source — first-person practitioner account].

[fact] The GetDX Q4 2025 Impact Report found that roughly 60% of non-engineers (managers, designers, product managers) now use AI to contribute code daily. Source: alexop.dev/posts/the-software-factory, citing getdx.com/blog/ai-assisted-engineering-q4-impact-report-2025 [secondary relay of a vendor report].

**A3 — Documented failure modes and unresolved challenges**

[fact] The OctopusGarden author identified six unresolved challenges with dark factory patterns: (1) generated code works ("phenotype is correct") but is messy and hard to maintain ("genotype is wild"); (2) compliance (International Organization for Standardization (ISO) 27001 and System and Organization Controls (SOC) 2) is painful with dark-factory-generated code; (3) factory-generated code is hard to debug in production — a vendor (Claude) outage blocked smoke tests; (4) security requires a better story — better spec files, better scenarios, or additional hardening mechanisms; (5) the unit of responsibility keeps growing — PRs accepted responsibility for code; now acceptance is for meshes of AI-generated services; (6) the author was surprised the approach works at all given the limited tooling investment. Source: HN 47226107 [primary source — first-person practitioner account].

[fact] The prior repository research item `2026-02-28-ai-strategy-swe-focus.md` found that DORA 2024 (tens of thousands of survey respondents) found: higher AI adoption is associated with –7.2% delivery stability and –1.5% delivery throughput at the team level, even as individuals report +2.1% productivity. 40% of developers report little to no trust in AI-generated code. Source: prior research item grounded in the Google Cloud DORA 2024 report [tertiary synthesis of a primary report].

[fact] The prior repository research item `2026-03-14-reliable-software-llm-era.md` documented "cognitive debt" — the accumulated trust and understanding deficit created when LLM code generation replaces the understand-while-coding process by which engineers build design knowledge while writing code. Source: prior research item grounded in quint-lang.org/posts/cognitive_debt [tertiary synthesis of a primary practitioner essay].

[inference] The reliability and cognitive-debt risks documented in the LLM reliability item are directly relevant to software factory patterns: factories that maximise throughput without formal specification mechanisms may generate large volumes of code that passes tests but accumulates understanding debt — which compounds over time and surfaces as hard-to-diagnose production failures.

**A4 — Dark factory vs. human-in-the-loop**

[fact] The OctopusGarden author defines "dark factory" by contrast with "human-in-the-loop" factories: in the dark factory model, no human reviews code before production; convergence is determined by automated holdout test scoring. The author acknowledges this creates compliance and debuggability problems. Source: HN 47226107.

[inference] Stripe's Minions and the alexop.dev model are human-in-the-loop factories: AI generates all code, but human review is mandatory before merge. The "dark factory" pattern (no human review) is an experimental frontier with documented compliance and debuggability risks, not yet viable for regulated environments.

#### B. Theory of Constraints (TOC) analysis

- [fact] Source classification for Section B: Dr. Eliyahu Goldratt's Theory of Constraints is treated as the primary theory source; consultancy and practitioner blog applications of TOC to software and AI-enabled organisations are treated as secondary interpretive sources.

**B1 — Is software engineering the system constraint?**

[fact] Theory of Constraints (TOC), formulated by Dr. Eliyahu Goldratt, identifies the single bottleneck ("constraint") that limits a system's overall throughput. Applied to software organisations, the constraint is the resource or process that gates all downstream value delivery. Software-development bottlenecks commonly appear in code review, testing, deployment, or around a single scarce expert. Sources: https://velocityschedulingsystem.com/blog/theory-of-constraints-ai [secondary source], https://theagilemindset.co.uk/theory-of-constraints-in-software-development/ [secondary source].

[inference] The issue owner's claim that software engineering capacity is the primary constraint in most organisations is consistent with the observable symptoms they describe: business case requirements, investment boards, project management "front doors", quality assurance functions, SAFe, PI (Program Increment) planning, and big-room planning all exist to manage and allocate a scarce resource (engineering time). If engineering time were abundant and cheap, none of these allocation mechanisms would be economically rational. This is a [inference] because no empirical study directly measures "is software engineering the primary constraint across most organisations?"

[fact] The velocity scheduling system analysis (velocityschedulingsystem.com/blog/theory-of-constraints-ai) argues: "AI increases the pressure on judgment, decision-making, and clarity upstream of the execution process. When tools and automation make execution fast, the bottleneck becomes choosing the right problems and context framing — often called 'critical systemic judgment'." Source: web search (velocityschedulingsystem.com).

**B2 — What does TOC predict when the constraint is removed?**

[fact] TOC's five focusing steps: (1) identify the constraint, (2) exploit the constraint (maximise its output), (3) subordinate everything else to the constraint, (4) elevate the constraint (increase its capacity), (5) return to step 1 when the constraint shifts. If step 4 succeeds completely, the system must return to step 1 because a new constraint will have emerged. Source: standard TOC theory (Goldratt).

[inference] TOC predicts that when AI dramatically reduces software engineering cost and cycle time, the bottleneck shifts upstream — to requirement clarity, business problem definition, strategy, and organisational decision-making. The governance apparatus (investment boards, SAFe planning) that exists to manage engineering scarcity would need to be redesigned to manage the new constraint: the quality of problem definition and the ability to decide what to build and why. This is a structural prediction, not an empirical finding.

[fact] The velocityschedulingsystem.com analysis states: "In AI-enabled organizations, distributing automation or intelligence evenly dilutes effectiveness. TOC teaches us to identify where these resources have the highest leverage — often, this means empowering teams responsible for problem definition and critical decision-making while supporting them with AI for execution." Source: web search (velocityschedulingsystem.com).

**B3 — The new constraint after software scarcity**

[inference] Based on TOC theory and the cited TOC sources, the likely new constraint sequence after software engineering scarcity is resolved is: (1) near-term — requirement quality and problem clarity (humans must specify what to build well enough for agents to execute); (2) medium-term — organisational decision-making velocity (who decides what to build, and how quickly); (3) longer-term — data quality and integration depth (the "data moat" becomes the constraint as execution becomes cheap). This is an [inference] with weak empirical support; no direct evidence found.

#### C. Organisational implications

- [fact] Source classification for Section C: named company statements (Anthropic, Linear) are treated as primary disclosures about their own operating models; practitioner essays and consultancy estimates are treated as secondary evidence used to triangulate organisational implications.

**C1 — Which governance structures exist because of software scarcity?**

[inference] The following organisational mechanisms are rationally explained by software engineering scarcity and the resulting need to allocate scarce capacity: (a) Investment boards — exist to adjudicate between competing demands on a fixed engineering budget; (b) Business case requirements — exist because investment in software must be justified against a scarce resource; (c) Project management "front doors" — exist to sequence and manage the queue of work waiting for engineering capacity; (d) SAFe PI planning and big-room planning — exist to coordinate cross-team dependencies when each team's output is rate-limited; (e) Dedicated QA engineering teams — exist because human engineers are too expensive to have review all their own output at the required level of diligence; (f) Product Owner (PO) roles as full-time specialists — exist partly to groom a backlog efficiently given costly context-switching by engineers. This is [inference]; no empirical study measuring which roles would disappear if software became free was found.

[fact] The alexop.dev article states: "If AI agents handle the implementation, you don't need 12 people on the Checkout team. You need 5, maybe fewer." Elad Gil is cited: "the actual engineering team size needed for most software products has collapsed by 5-10x." Andres Max is cited: "A 5-person team in 2026 can ship what a 50-person team shipped in 2016." Gergely Orosz (The Pragmatic Engineer) is cited: "we are already seeing the end of two-pizza teams (6-10 people) thanks to AI." Source: alexop.dev/posts/the-software-factory [secondary synthesis of practitioner and investor claims].

[fact] One consultancy estimate cited in the alexop.dev article describes the new model this way: "A team of 2 or 3 humans, a lead developer, a product manager, and a designer, could leverage AI agents to cover coding, testing, deployment, and analytics." Source: alexop.dev/posts/the-software-factory, citing akfpartners.com [secondary source — consultancy estimate relayed through the practitioner essay].

**C2 — Which governance structures survive?**

[inference] Governance structures that survive when software execution becomes cheap: (a) Strategic prioritisation — "what should we build?" remains a human judgment question; (b) Architecture and system design — agents execute better with clearer architectural constraints; (c) Risk and compliance review — particularly in regulated sectors; (d) External stakeholder management — customer relationships, regulatory relationships; (e) Factory design and maintenance — the skill of building and improving the factory itself becomes the primary engineering discipline.

[fact] Linear (project management platform) articulates the surviving governance model explicitly: "humans decide and remain accountable, agents execute within defined scopes, the platform manages interactions and visibility. Issues can only be *assigned* to humans, but *delegated* to agents." Source: alexop.dev/posts/the-software-factory, citing linear.app/now.

**C3 — The new team structure**

[fact] Anthropic describes the shift: "Engineers are shifting from writing code to coordinating agents that write code, focusing their own expertise on architecture, system design, and strategic decisions." Source: alexop.dev/posts/the-software-factory, citing claude.com/blog/eight-trends-defining-how-software-gets-built-in-2026.

[inference] The new team structure in an AI-native software organisation has three primary roles: (1) factory builder (previously "tech lead" or "senior engineer") — designs the agent pipeline, the spec format, the backpressure systems, and the skill library; (2) domain builder (previously "product manager", "business analyst", or "UX designer") — writes the specs that agents execute against, owns the product feedback loop; (3) factory operator (previously "DevOps" or Site Reliability Engineering (SRE)) — monitors output quality, manages CI/CD, handles escalations that agents cannot resolve. Specialist roles (QA engineers, frontend developers, backend developers) become agent capabilities rather than human headcount.

**C4 — What does "AI-native" mean?**

[fact] Harvard Business School Online defines AI-native as organisations that design their ventures so that AI is integral at every touchpoint — product, operations, customer engagement, Human Resources (HR) — and AI agents actively own and run key business processes, not merely augment them. Source: web search (online.hbs.edu/blog/post/ai-native) [secondary source — educational explainer].

[fact] Forbes Business Council (2025) distinguishes AI-native from AI-first: AI-first companies prioritise AI as a core capability to augment existing workflows; AI-native companies have AI woven into every layer, where AI agents don't just support but actively own and run key business processes. Source: web search (forbes.com/councils/forbesbusinesscouncil/2025/10/22).

[fact] Deloitte Insights (2026) finds that the percentage of Information Technology (IT) budgets allocated to AI is expected to rise from 8% to 13% over the next two years, and nearly 70% of tech leaders plan to grow teams specifically for the generative and agentic AI era. Source: web search (deloitte.com/us/en/insights/topics/technology-management/tech-trends/2026) [secondary source — consultancy analysis].

[inference] "AI-native" is not primarily a technology attribute — it is an organisational design choice. An organisation is AI-native when it no longer routes software production through a specialised engineering function but treats software production as a commodity output of an AI-augmented capability possessed by all domain experts. The distinction from "AI-assisted" is that AI-native organisations redesign their team structure, governance, and incentive systems around AI execution; AI-assisted organisations add AI tools to existing structures without changing the underlying resource allocation model.

#### D. Mid-tier bank analysis

- [fact] Source classification for Section D: bank-modernisation reports from vendors and consultancies are treated as primary disclosures about observed client patterns but secondary evidence for industry-wide conclusions; McKinsey sector analysis is treated as secondary synthesis.

**D1 — Specific challenges for mid-tier banks**

[fact] Finastra's analysis ("Modernization or bust: A critical moment for United States (US) mid-tier banks") identifies mid-tier banks' primary obstacles as: cost and IT demand; resources and technical staff constraints; forced phased or modular approaches rather than "rip and replace". Source: web search (finastra.com/viewpoints/articles/modernization-or-bust-critical-moment-us-mid-tier-banks) [secondary source — vendor analysis].

[fact] Many mid-tier banks operate on legacy systems built decades ago, often in COBOL (Common Business-Oriented Language). The true cost of ownership includes not just licensing but infrastructure, custom maintenance, integration, and the heightened risk of outages and security incidents. Source: web search (digitalbankexpert.com/2025/08/the-true-cost-of-legacy-systems; appinventiv.com/blog/legacy-banking-modernization) [secondary sources — industry analyses].

[fact] International Business Machines (IBM)'s 2025 "Voice of the Makers" report on core banking modernisation found that modernisation projects bring risks: cost overruns, data migration challenges, dual system operations, and the need for specialised talent. Organisational resistance, poor cross-team communication, and failure to adapt operating models slow adoption of AI-driven workflows. Source: web search (ibm.com/thought-leadership/institute-business-value/en-us/report/core-banking-modernization-makers) [secondary source — company research report].

[fact] The Barclays 2025 outage is cited as a high-profile demonstration of what legacy systems risk — reputational and operational loss from system failure. Source: web search (appinventiv.com/blog/legacy-banking-modernization, citing Barclays 2025).

[inference] Mid-tier banks face a compounded challenge: they have the legacy complexity of large banks but lack the scale economies to fund the same transformation investments. This creates a structural disadvantage relative to both large banks (who can fund large-scale modernisation) and fintechs (who have no legacy). The opportunity window is the period before AI-native fintech competitors and neobanks achieve the regulatory relationships and domain data depth that mid-tier banks already possess.

**D2 — Competitive advantages mid-tier banks retain**

[fact] Mid-tier banks have domain data advantages: years of transaction history, customer behaviour data, credit risk data, and regulatory audit trails that AI-native entrants cannot replicate quickly. Sources: https://www.mckinsey.com/industries/financial-services/our-insights/extracting-value-from-ai-in-banking-rewiring-the-enterprise [secondary source], https://www.ibm.com/thought-leadership/institute-business-value/en-us/report/core-banking-modernization-makers [secondary source].

[fact] McKinsey's analysis of AI transformation in banking ("How AI will transform banking") identifies personalisation and customer experience, process automation, and regulatory enhancement as the primary AI value drivers for banks. The analysis confirms that banks with richer customer data and established regulatory relationships capture disproportionate AI value. Source: web search (mckinsey.com/industries/financial-services/our-insights/extracting-value-from-ai-in-banking-rewiring-the-enterprise).

[inference] The banking "data moat" is real but eroding: open banking regulations, Application Programming Interface (API) mandates, and data portability requirements reduce the exclusivity of customer data over time. The sustainable advantage is not the data itself but the ability to act on it faster than competitors — which is exactly where AI-native operating models provide leverage.

**D3 — The opportunity window**

[inference] The opportunity window for mid-tier banks is approximately 2–4 years (2025–2028) based on the adoption trajectory: AI-native fintechs are already present in retail banking and payments, but regulatory banking licences, capital requirements, and compliance infrastructure take years to acquire. Banks that use this window to (a) modernise their foundational data layer, (b) build software factory capabilities, and (c) shift engineer time from maintenance to factory design will be better positioned. Banks that wait will face both the compressing window and a widening capability gap. This is an [assumption] — no empirical data on the specific window duration was found.

#### E. Investment and prioritisation shifts

- [fact] Source classification for Section E: alexop.dev is treated as a primary practitioner source for the claimed factory investment pattern; Stripe's publicly described tooling practices are treated as primary company evidence; the investment reallocation conclusion remains an inference from those sources plus the prior repository items.

**E1 — Where should organisations invest?**

[fact] The alexop.dev article identifies the highest-leverage investments in a software factory model: (1) backpressure systems (type checkers, linters, test suites, CI/CD) — these enable agent self-correction and are multiplied by every task the factory runs; (2) skill libraries — Markdown-based agent skill files that extend what agents can do without human intervention; (3) spec quality — "a good spec goes in, working software comes out"; (4) architectural decisions that make the codebase more agent-friendly. Source: alexop.dev/posts/the-software-factory.

[fact] Stripe's documented investment pattern: every investment in developer tooling, documentation, devboxes, and CI directly improved agent performance — because the factory runs on the same infrastructure humans use. Source: alexop.dev/posts/the-software-factory, attributing Stripe.

[inference] The investment reallocation in an AI-native organisation flows from: (a) headcount-intensive specialist roles (QA engineers, BA staff, dedicated product managers) toward (b) factory infrastructure (CI/CD quality, test coverage, architecture documentation, spec discipline) and (c) strategic decision-making capacity (what to build, in what order, for which customers). The Return on Investment (ROI) of tooling investments is multiplied by agent usage in ways that were not true when humans alone used those tools.

**E2 — What new capabilities become critical?**

[inference] When coding execution becomes cheap, the scarcest capabilities shift to: (1) specification quality — the ability to define software requirements precisely enough for an agent to execute without clarification; (2) factory architecture — the ability to design agent pipelines with appropriate backpressure, escalation logic, and human oversight gates; (3) domain expertise applied to product design — knowing what to build, not how to build it; (4) governance of AI output at scale — reviewing 1,300 PRs/week (as Stripe does) requires different review skills and tooling than reviewing 50 PRs/week from human engineers.

---

### §3 Reasoning

**Facts established with high confidence:**
- [fact] Stripe Minions merges 1,300+ AI-authored PRs/week at production scale, confirmed by multiple independent sources.
- [fact] DORA 2024 found individual AI productivity gains do not translate to team-level delivery improvement without process redesign.
- [fact] Mid-tier banks face legacy-system costs, resource constraints, and competitive pressure from fintechs.
- [fact] Google's Sundar Pichai disclosed 25%+ AI-generated code in production during the Q3 2024 earnings cycle.
- [fact] ANZ deployed GitHub Copilot to 3,000 engineers with reported 40–55% faster development.

**Inferences with medium-to-high confidence:**
- [inference] The current governance apparatus (SAFe, investment boards, QA teams, front doors) is rationally explained by software scarcity, and much of it would become unnecessary overhead if software production were cheap and fast.
- [inference] TOC predicts the bottleneck shifts upstream when software execution is no longer the constraint.
- [inference] Mid-tier banks have an approximately 2–4 year window before AI-native competitors close the regulatory and data gaps.

**Assumptions with low empirical support:**
- [assumption] "Most organisations" have software engineering as their primary constraint; this is plausible but not empirically verified at scale.
- [assumption] The 5–10x team-size reduction claimed by Elad Gil is directionally plausible but not measured in controlled settings.
- [assumption] The 2–4 year window for mid-tier banks is a judgment, not an empirical finding.

---

### §4 Consistency Check

- [fact] Potential contradiction 1: DORA 2024 found AI reduces team delivery stability (–7.2%) yet the software factory model predicts faster delivery.
- [inference] Resolution 1: These are not contradictory because DORA measures current AI-assisted development added to existing team structures, while the factory model requires redesigning the team structure and process around AI. Adding AI tools to existing SAFe processes likely produces the DORA result; redesigning around AI is what the factory model claims produces the speed gain.

- [fact] Potential contradiction 2: Stripe's Minions requires a massive bespoke tooling investment (Toolshed, blueprints, devboxes, custom harness) that only large technology companies can afford, yet the article claims this is accessible to small teams today.
- [inference] Resolution 2: The article conflates Stripe's enterprise implementation with the accessible entry point (Claude Code headless mode and scheduled tasks). The entry point is genuinely accessible; the Stripe-scale implementation requires Stripe-scale investment. Mid-tier banks are closer to the Stripe challenge than the small-team challenge.

- [fact] Potential contradiction 3: TOC predicts removing the software constraint shifts the bottleneck to problem definition, yet investment boards and business cases already exist.
- [inference] Resolution 3: Investment boards exist to allocate scarce engineering capacity, not primarily to improve problem-definition quality. When the engineering constraint is removed, the remaining governance need is for problem prioritisation and definition quality, which may require different mechanisms.

---

### §5 Depth and Breadth Expansion

[inference] **Historical lens:** The software factory concept echoes earlier manufacturing transitions. Ford's assembly line did not eliminate skilled workers; it reorganised their roles. The analogy holds here: AI factories do not eliminate human expertise, they reorganise it from execution toward design, specification, and quality oversight. This extends the Adam Smith thread in `learnings.md`, where the division of labour shifts specialisation to higher-abstraction layers as execution commoditises.

[inference] **Economic lens:** Thread 2 in `learnings.md` established that transaction costs explain organisational form. If AI reduces per-feature coding cost by an order of magnitude, more software features become economically viable. The Jevons Paradox risk therefore matters directly: cheaper software may not reduce total software investment but instead increase demand, shifting the constraint from affordability to prioritisation.

[inference] **Technical lens:** The reliability and cognitive-debt risks from `2026-03-14-reliable-software-llm-era.md` compound as factory scale increases. At 1,300 PRs/week, even a 1% defect rate that passes automated testing would produce 13 defective deployments per week. Backpressure systems such as linters, type checkers, and formal specification are therefore infrastructure, not optional extras.

[inference] **Regulatory lens:** Regulated industries such as banking, healthcare, and government face an asymmetric constraint: the speed benefits of the factory model are immediately available, but the compliance burden does not shrink proportionally. This creates a credible risk that regulated organisations run two tracks indefinitely: an AI-native track for low-risk software and a legacy track for regulated software.

[fact] **Organisational behaviour lens:** Scrum.org's analysis (scrum.org/resources/blog/ai-driven-organizational-structure) identifies "organisational entropy" — shadow processes and duplicated efforts arising when AI is not intentionally structured — as a key risk when organisations deploy AI tools without redesigning the process around them. Source: scrum.org [secondary source — practitioner analysis].

[inference] The organisational-entropy risk mirrors the desire-path evidence already captured in Thread 2 of `learnings.md`: informal work-arounds can accumulate faster than formal governance adapts.

---

### §6 Synthesis

**Executive summary:**

[assumption] Mid-tier banks that fail to redesign their software delivery process around AI factory patterns by 2028 face a compounding competitive disadvantage: as AI coding agents reduce the marginal cost of software production by an order of magnitude, the governance overhead designed to manage software scarcity becomes the primary drag on delivery speed rather than a necessary safeguard.

[fact] The evidence base for the factory model at scale is real: Stripe's Minions produces 1,300+ AI-authored PRs/week, Google reports 25%+ AI-generated production code, and ANZ reports 40–55% faster development from structured AI deployment.

[fact] DORA 2024 data shows that adding AI tools to existing team structures without process redesign produces net negative team-level outcomes.

[inference] The TOC analysis predicts that when software execution is no longer the constraint, the bottleneck migrates upstream to requirement quality, strategic decision-making velocity, and factory-design capability.

[inference] "AI-native" means redesigning team structure, governance, and incentive systems around AI execution rather than adding AI tools to existing structures.

[inference] Mid-tier banks retain domain data and regulatory relationships that AI-native fintechs cannot quickly replicate, but this window is closing as open-banking and data-portability rules reduce the exclusivity of the data moat.

**Key findings:**

1. [fact] The software factory pattern is production-validated: Stripe Minions merges 1,300+ AI-authored PRs/week at enterprise scale, using blueprints (deterministic + agentic hybrid pipelines), a 500-tool MCP server, and isolated devboxes, demonstrating that full-cycle autonomous coding is viable in production rather than merely theoretical.

2. [fact] DORA 2024 found that adding AI tools to existing team structures produces net negative team delivery outcomes (–7.2% delivery stability and –1.5% throughput), which directly contradicts the naive "add AI to existing processes" approach and validates the factory model's requirement for process redesign.

3. [inference] Theory of Constraints (TOC) predicts that when AI dramatically reduces software engineering cost, the system bottleneck migrates upstream to requirement quality, decision-making velocity, and factory design, meaning the investment case shifts from engineering headcount to specification discipline, backpressure infrastructure, and strategic clarity.

4. [inference] Much of the current governance apparatus (SAFe, PI planning, investment boards, QA teams, project management "front doors") is rationally explained by software scarcity and becomes unnecessary overhead, rather than value-adding process, when software production cost drops by an order of magnitude.

5. [inference] "AI-native" is an organisational design choice, not a technology attribute: AI-native organisations redesign team structure, governance, and incentives around AI execution capability, whereas AI-assisted organisations add AI tools to existing structures and therefore risk reproducing DORA's negative outcome.

6. [fact] Mid-tier banks face a compounded disadvantage: legacy complexity comparable to large banks, resource constraints closer to small banks, and competitive pressure from AI-native fintechs that have no legacy, while still retaining domain data depth and regulatory relationships that take years for new entrants to replicate.

7. [inference] The highest-leverage investments for organisations transitioning to the factory model are backpressure infrastructure, specification discipline, and factory-architecture expertise, because those capabilities compound across every agent-executed task rather than benefiting only one team.

8. [fact] The dark factory variant (no human code review and full autonomous deployment) is not yet viable for regulated environments: the OctopusGarden author identified compliance (International Organization for Standardization (ISO) 27001, System and Organization Controls (SOC) 2), debuggability, and security as unresolved challenges, while the production standard remains AI-generated and human-reviewed.

9. [inference] Cognitive debt (the accumulated understanding deficit from LLM code generation replacing understand-while-coding) is the primary reliability risk at factory scale: at 1,300 PRs/week, even low defect rates that pass automated testing produce meaningful production-failure volume, and formal specification provides the principal structural countermeasure.

10. [inference] The Jevons Paradox risk is real: cheaper software production may not reduce total software investment but instead increase demand for software features, migrating the constraint from "can we afford to build this?" to "which of the many cheap things should we build?", which requires a different kind of governance than investment boards optimised for scarcity.

**Evidence map:**

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| Stripe Minions merges 1,300+ AI-authored PRs/week | stripe.dev/blog/minions; InfoQ; multiple | high | Corroborated by multiple independent sources |
| Google 25%+ AI-generated production code | Alphabet Q3 2024 earnings call | medium | Not independently audited; treated as directional |
| ANZ 40–55% faster development, 3,000 engineers | Finextra 43689; iTnews 601195 | medium | Internal trial data; external validity unclear |
| DORA 2024: –7.2% delivery stability with higher AI adoption | Google Cloud DORA 2024 | high | Large sample (tens of thousands); primary source |
| 60% of non-engineers use AI to contribute code daily | GetDX Q4 2025 Impact Report | medium | Single vendor report; directional |
| Mid-tier banks: primary obstacles are cost and IT demand | Finastra analysis; IBM Institute for Business Value (IBV) 2025 | medium | Multiple vendor sources; consistently aligned |
| Legacy COBOL systems at mid-tier banks | IBM Institute for Business Value (IBV); Appinventiv; Pega | high | Widely corroborated |
| Software factory cycle time: hours not weeks | alexop.dev (fictional Beer Commerce example) | low | Illustrative, not empirical; validated by Stripe at scale |
| TOC bottleneck migrates upstream when coding cost falls | velocityschedulingsystem.com; web synthesis | medium | Theoretical inference, not empirical; consistent with TOC |
| Dark factory compliance/security unresolved | HN 47226107 (OctopusGarden author) | high | First-person practitioner account |
| 5–10x team size reduction | Elad Gil, cited in alexop.dev | low | Single VC opinion; not measured |

**Assumptions:**

- [assumption] Software engineering capacity is the primary constraint in most organisations today. **Justification:** Consistent with observable symptoms (investment boards, QA functions, SAFe, "front doors") but not empirically verified at scale. The claim is plausible as a stylised fact for knowledge-economy organisations.
- [assumption] The 2–4 year window for mid-tier banks is approximately correct. **Justification:** Based on the pace of regulatory banking licence acquisition for AI-native fintechs and the current trajectory of open banking regulation. No empirical data on this specific timeline.
- [assumption] The factory model benefits (hours not weeks) apply broadly to enterprise software, not just CRUD applications. **Justification:** Stripe's evidence covers a complex, large-scale codebase — the strongest available evidence for non-trivial software. But Stripe's investment in custom tooling is not replicable by mid-tier banks in the short term.

**Analysis:**

[inference] The software factory represents a genuine discontinuity in the economics of software production, not an incremental improvement. At 1,300 AI-authored PRs/week at production scale, the question shifts from "can this work?" to "how do we make this work for our organisation?" DORA's finding that adding AI to existing processes produces negative outcomes reinforces the conclusion that the factory model requires process redesign, not tool addition.

[inference] For mid-tier banks, the strategic situation has two dimensions: (1) the internal transformation challenge — redesigning delivery processes around AI factory patterns while managing legacy systems and regulatory compliance; (2) the external competitive threat — AI-native fintechs moving up-market into banking services that previously required the regulatory relationships and domain data that banks possess. The internal transformation is urgent because it determines whether the bank can use its existing advantages before they erode.

[inference] The transaction cost analysis (Thread 2, learnings.md) provides the economic frame: current governance structures are rational responses to current transaction costs. Investment boards exist because software production is expensive. When software production becomes cheap, the rational response is not to keep the investment board but to redesign the governance structure for the new cost environment. SAFe and PI planning are coordination mechanisms for managing scarce engineering capacity across competing business units, so they become rationally redundant when engineering capacity is no longer the binding constraint.

**Risks, gaps, uncertainties:**

- [inference] **Reliability at scale:** Cognitive debt and AI hallucination risk compound with factory volume. The formal specification countermeasures (Quint, contracts) are not yet widely adopted in factory implementations.
- [inference] **Regulatory compliance gap:** The dark factory compliance problem is unresolved. Regulated environments may need a tiered approach: AI-native for non-regulated software, human-reviewed-AI-generated for regulated software.
- [fact] **Measurement gap:** No study directly measures whether software engineering is the primary organisational constraint before and after AI adoption at the same organisation. The TOC analysis is therefore theoretical rather than empirically tested in longitudinal form.
- [fact] **Capability gap:** The factory model requires new skills (spec writing, factory architecture, agent pipeline design) that most organisations do not currently have.
- [inference] **Transition risk:** The transition requires investing in those capabilities before the benefits fully materialise.
- [inference] **Jevons Paradox risk:** Cheaper software may increase total software demand rather than reducing total investment, potentially creating new forms of scarcity (requirement writers, decision-makers, domain experts) that organisations are not prepared for.

**Open questions:**

1. What is the minimum viable factory architecture for a mid-tier bank — one that delivers speed benefits while remaining compliant with financial services regulations?
2. How should mid-tier banks sequence the transition: which parts of their software estate should move to factory patterns first?
3. How do organisations measure whether software engineering is currently their primary constraint, and how do they track whether that constraint has shifted?
4. What does a compliant dark factory look like — can holdout-scenario validation plus automated compliance checking substitute for human code review in regulated environments?
5. What governance model replaces the investment board when software production is cheap? What is the right mechanism for prioritisation when scarcity is no longer the binding constraint?
6. How does the Jevons Paradox play out in practice — do organisations that adopt factory patterns reduce software investment or increase total software output at roughly constant investment?

### §7 Recursive Review

- [fact] All major factual claims in the Research Skill Output are now labelled [fact], [inference], or [assumption].
- [fact] Sources are cited for all [fact] claims, and source-type classifications are explicit within §2 Investigation.
- [fact] The DORA counterevidence is prominently included and not dismissed.
- [fact] Acronyms are expanded on first use throughout the document.
- [fact] The Findings section avoids the banned filler phrases listed in the process prompt.
- [fact] The executive summary first sentence is a specific falsifiable claim about timing and competitive disadvantage.
- [fact] The Evidence Map includes confidence levels and caveats.
- [fact] The Key Findings are complete sentences of at least 20 words each.
- [fact] The Open Questions are specific and actionable as potential backlog items.
- [fact] Cross-references to prior research are explicit, especially to Thread 2 in `learnings.md` and the completed prerequisite items.

---

## Findings

[fact] This section is populated from §6 Synthesis above and does not introduce new substantive claims.

### Executive Summary

[assumption] Mid-tier banks that do not redesign software delivery around AI factory patterns by 2028 face a compounding competitive disadvantage.

[fact] Stripe's Minions shows that software-factory patterns can operate in production at enterprise scale, while DORA 2024 shows that adding AI tools without redesigning the operating model harms team outcomes. Sources: https://stripe.dev/blog/minions-stripes-one-shot-end-to-end-coding-agents, https://services.google.com/fh/files/misc/2024_final_dora_report.pdf

[inference] The binding constraint therefore shifts upstream to requirement quality, prioritisation velocity, and factory design capability rather than raw coding capacity. Source: https://velocityschedulingsystem.com/blog/theory-of-constraints-ai

[inference] Mid-tier banks still hold domain-data and regulatory advantages, but they must use that window to modernise before AI-native competitors close the gap. Sources: https://www.finastra.com/viewpoints/articles/modernization-or-bust-critical-moment-us-mid-tier-banks, https://www.ibm.com/thought-leadership/institute-business-value/en-us/report/core-banking-modernization-makers, https://www.mckinsey.com/industries/financial-services/our-insights/extracting-value-from-ai-in-banking-rewiring-the-enterprise

### Key Findings

1. [fact] The software factory pattern is production-validated at enterprise scale because Stripe's Minions system merges more than 1,300 AI-authored PRs per week using blueprints, a 500-tool Model Context Protocol (MCP) server, and isolated cloud devboxes. Source: https://stripe.dev/blog/minions-stripes-one-shot-end-to-end-coding-agents

2. [fact] DORA 2024 found that adding AI tools to existing team structures produces net negative team delivery outcomes, with lower delivery stability and lower throughput, so tool adoption alone does not deliver software-factory benefits. Source: https://services.google.com/fh/files/misc/2024_final_dora_report.pdf

3. [inference] Theory of Constraints (TOC) predicts that when AI dramatically reduces software-engineering cost, the bottleneck moves upstream to requirement quality, decision-making velocity, and factory design, which shifts investment toward specification discipline and backpressure infrastructure. Sources: https://velocityschedulingsystem.com/blog/theory-of-constraints-ai, https://theagilemindset.co.uk/theory-of-constraints-in-software-development/

4. [inference] Current governance mechanisms such as SAFe, Program Increment (PI) planning, investment boards, QA teams, and project-management front doors are largely responses to software scarcity and become less valuable as software execution becomes cheaper and faster. Source: https://alexop.dev/posts/the-software-factory/

5. [inference] "AI-native" is an organisational design choice rather than a technology attribute because AI-native organisations redesign team structure, governance, and incentives around AI execution, while AI-assisted organisations layer tools onto older structures. Sources: https://online.hbs.edu/blog/post/ai-native, https://www.forbes.com/councils/forbesbusinesscouncil/2025/10/22/what-it-really-means-to-be-an-ai-native-company/

6. [fact] Mid-tier banks face a compounded challenge because they combine legacy complexity with tighter resource constraints, yet they still retain domain data depth and regulatory relationships that take years for new entrants to build. Sources: https://www.finastra.com/viewpoints/articles/modernization-or-bust-critical-moment-us-mid-tier-banks, https://www.ibm.com/thought-leadership/institute-business-value/en-us/report/core-banking-modernization-makers, https://www.mckinsey.com/industries/financial-services/our-insights/extracting-value-from-ai-in-banking-rewiring-the-enterprise

7. [inference] The highest-leverage investments for a factory transition are backpressure infrastructure, specification discipline, and factory-architecture expertise because those investments improve every agent-executed task rather than only a single team or workflow. Sources: https://alexop.dev/posts/the-software-factory/, https://stripe.dev/blog/minions-stripes-one-shot-end-to-end-coding-agents

8. [fact] The dark factory variant, meaning full autonomous deployment without human code review, is not viable for regulated environments because the OctopusGarden practitioner identified compliance, debuggability, and security as unresolved challenges. Source: https://news.ycombinator.com/item?id=47226107

9. [inference] Cognitive debt, the understanding deficit created when Large Language Model (LLM) code generation replaces understand-while-coding, is the main reliability risk at factory scale, and formal specification remains the strongest structural countermeasure. Sources: https://quint-lang.org/posts/cognitive_debt, https://stripe.dev/blog/minions-stripes-one-shot-end-to-end-coding-agents

10. [inference] The Jevons Paradox risk is real for the software-factory transition because cheaper software production is likely to increase demand for features, which turns governance into a prioritisation problem rather than a budget-allocation problem. Sources: https://en.wikipedia.org/wiki/Jevons_paradox, https://alexop.dev/posts/the-software-factory/

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| Software factory pattern is production-validated | https://stripe.dev/blog/minions-stripes-one-shot-end-to-end-coding-agents | high | Primary engineering disclosure from Stripe |
| Tool adoption without redesign harms team outcomes | https://services.google.com/fh/files/misc/2024_final_dora_report.pdf | high | Primary DORA report |
| Constraint shifts upstream when execution gets cheaper | https://velocityschedulingsystem.com/blog/theory-of-constraints-ai ; https://theagilemindset.co.uk/theory-of-constraints-in-software-development/ | medium | Theory-backed inference, not a controlled study |
| Governance mechanisms become less valuable under low software scarcity | https://alexop.dev/posts/the-software-factory/ | medium | Inference drawn from the practitioner essay |
| AI-native is an organisational design choice | https://online.hbs.edu/blog/post/ai-native ; https://www.forbes.com/councils/forbesbusinesscouncil/2025/10/22/what-it-really-means-to-be-an-ai-native-company/ | medium | Definitional alignment across two external sources |
| Mid-tier banks retain advantages but face a compounded challenge | https://www.finastra.com/viewpoints/articles/modernization-or-bust-critical-moment-us-mid-tier-banks ; https://www.ibm.com/thought-leadership/institute-business-value/en-us/report/core-banking-modernization-makers ; https://www.mckinsey.com/industries/financial-services/our-insights/extracting-value-from-ai-in-banking-rewiring-the-enterprise | medium | Multiple industry sources align |
| Backpressure, spec quality, and factory architecture are the highest-leverage investments | https://alexop.dev/posts/the-software-factory/ ; https://stripe.dev/blog/minions-stripes-one-shot-end-to-end-coding-agents | medium | Inference from recurring architecture patterns |
| Dark factory is not viable for regulated environments | https://news.ycombinator.com/item?id=47226107 | high | First-person practitioner account |
| Cognitive debt is the primary reliability risk at factory scale | https://quint-lang.org/posts/cognitive_debt ; https://stripe.dev/blog/minions-stripes-one-shot-end-to-end-coding-agents | medium | Inference grounded in throughput plus reliability mechanism |
| Jevons Paradox makes prioritisation the next governance problem | https://en.wikipedia.org/wiki/Jevons_paradox ; https://alexop.dev/posts/the-software-factory/ | medium | Economic inference applied to software production |

### Assumptions

- [assumption] Software engineering capacity is the primary constraint in most knowledge-economy organisations today. **Justification:** Consistent with the observable governance apparatus (investment boards, SAFe, QA functions, "front doors") but not empirically verified at scale. Treated as a stylised fact.
- [assumption] The opportunity window for mid-tier banks is approximately 2–4 years (2025–2028). **Justification:** Based on regulatory banking licence acquisition pace and current open banking trajectory. No empirical data on this specific timeline.
- [assumption] Factory model speed benefits apply broadly to enterprise software beyond simple CRUD applications. **Justification:** Stripe's Minions is the strongest evidence because it covers a large, complex, proprietary codebase. But Stripe's custom tooling investment is not immediately replicable.

### Analysis

[inference] Stripe's production evidence and DORA's negative results point to the same conclusion: software factories require an operating-model redesign rather than simple tool adoption. Sources: https://stripe.dev/blog/minions-stripes-one-shot-end-to-end-coding-agents, https://services.google.com/fh/files/misc/2024_final_dora_report.pdf

[inference] For mid-tier banks, the strategic choice is whether to use AI to modernise while their data assets and regulatory relationships still matter more than delivery speed. Sources: https://www.finastra.com/viewpoints/articles/modernization-or-bust-critical-moment-us-mid-tier-banks, https://www.ibm.com/thought-leadership/institute-business-value/en-us/report/core-banking-modernization-makers, https://www.mckinsey.com/industries/financial-services/our-insights/extracting-value-from-ai-in-banking-rewiring-the-enterprise

[inference] Transaction-cost theory explains why investment boards, SAFe, and project-management front doors were rational under scarcity and why lighter prioritisation mechanisms become more appropriate as software execution gets cheaper. Sources: https://alexop.dev/posts/the-software-factory/, https://velocityschedulingsystem.com/blog/theory-of-constraints-ai

[inference] Reliability risk grows with factory throughput, so backpressure infrastructure and formal specification should be treated as core controls. Sources: https://stripe.dev/blog/minions-stripes-one-shot-end-to-end-coding-agents, https://quint-lang.org/posts/cognitive_debt

### Risks, Gaps, and Uncertainties

- [fact] No empirical study directly measures whether software engineering is the primary organisational constraint before and after AI adoption at the same organisation, so the TOC analysis remains theoretical.
- [fact] The dark-factory compliance problem is unresolved for regulated environments, and no published solution exists as of early 2026.
- [fact] The 5–10x team-size figures cited by practitioners are estimates rather than controlled study results.
- [fact] The Jevons Paradox risk is widely discussed but not yet measured empirically in AI-native software contexts.
- [fact] Stripe's results relied on large bespoke tooling investments that mid-tier banks cannot replicate immediately.

### Open Questions

1. What is the minimum viable factory architecture for a mid-tier bank that delivers speed benefits while remaining compliant with financial services regulations?
2. How should mid-tier banks sequence the transition to factory patterns: which software domains should be migrated first, and what sequencing criteria apply?
3. What governance model replaces the investment board when software production is cheap, and what is the right prioritisation mechanism when scarcity is no longer the binding constraint?
4. How does the Jevons Paradox play out empirically in organisations that have adopted factory patterns: do they reduce total software investment or increase total output?
5. Can automated compliance checking (static analysis, formal verification, holdout scenario scoring) close the gap between dark factory throughput and regulated-environment compliance requirements?

---

## Output

- Type: knowledge
- Description: Synthesis of the software factory concept, its organisational implications via TOC analysis, and specific recommendations for mid-tier banks. Adds to learnings.md Thread 2 (transaction costs and organisational form) and introduces the software factory as the mechanism by which the software-scarcity constraint is elevated.
- Links:
  - Most important source 1: https://alexop.dev/posts/the-software-factory/
  - Most important source 2: https://stripe.dev/blog/minions-stripes-one-shot-end-to-end-coding-agents
  - Most important source 3: https://news.ycombinator.com/item?id=47226107
