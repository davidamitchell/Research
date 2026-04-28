---
review_count: 2
title: "The shape of organisations when software is no longer the constraint"
added: 2026-04-19T19:22:54+00:00
status: completed
priority: high  # low | medium | high
blocks: []
tags: [org-design, ai, software-cost, future-of-work, management, product-management, transaction-costs, agile, automation]
started: 2026-04-19T19:22:54+00:00
completed: 2026-04-19T19:22:54+00:00
output: [knowledge]
cites: []          # slugs of items this item directly depends on or quotes
related: []        # slugs of thematically connected items
superseded_by: ~   # slug of a later item that overrides this one (null if not superseded)
supersedes: ~      # slug of an older item this one replaces (null if not applicable)
item_type: primary # primary | synthesis
confidence: medium # high | medium | low
versions: []       # entries: {version: "1.0", sha: "<commit-hash>", changed: YYYY-MM-DD, progress: "<path>", summary: "<one-line>"}
---

# The shape of organisations when software is no longer the constraint

## Research Question

Inside an organisation that requires software to be built, integrated, and maintained (including Commercial Off-The-Shelf (COTS) systems, Software-as-a-Service (SaaS) platforms, and bespoke-built systems), how much of that organisation exists purely to manage the shaping, prioritising, management, or tracking of that work, and how does the organisation's structure change when the cost of producing software approaches zero?

Supporting questions:
- What fraction of a typical software-dependent organisation's headcount exists primarily to coordinate, manage, or govern software delivery rather than to deliver it directly?
- Which specific roles and functions exist as proxies or translators between business intent and software execution?
- What does economic theory (particularly transaction-cost economics) predict about firm shape when one major production cost collapses?
- What historical analogues exist, automation of manufacturing, adoption of cloud computing, introduction of Enterprise Resource Planning (ERP), and what did they do to organisational structure?
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
- Second-order effects: what new coordination work emerges if software production becomes abundant (for example governing many more smaller systems and managing AI agent outputs)

**Out of scope:**
- Deep technical treatment of specific AI coding tools (treated as inputs, not the subject)
- Pure software engineering productivity research not connected to organisational structure
- Startups and small teams where flat structure is already the norm; focus is on mid-to-large organisations
- Government and defence software organisations (sufficiently different dynamics to warrant a separate item)

**Constraints:** Publicly available sources. Empirical data on headcount ratios is sparse, so clearly distinguish [fact] from [inference] and [assumption] throughout.

## Context

The issue motivating this research is stark: a large proportion of every software-dependent organisation exists not to write, deploy, or operate software, but to manage the process of getting software written, deployed, and operated. Product roadmaps, sprint ceremonies, backlog grooming, change advisory boards, portfolio governance, and steering committees exist because software production has historically been slow, expensive, uncertain, and hard for non-technical stakeholders to specify or validate.

AI coding agents and natural-language-to-code pipelines are compressing the cost curve rapidly. If a capable AI can translate a clear business intent into working, tested, deployed software in hours rather than months, the question is no longer "how do we manage scarce engineering capacity?" but "how do we decide what to build?", and it is not obvious that the existing organisational machinery is the right answer to that question either.

This connects to the deeper question: how much of the modern organisation is a response to the specific historical cost structure of software, and how much would survive a world where that cost structure changes fundamentally?

## Approach

1. **Map the coordination layer**: Identify and categorise the roles and functions in a typical software-delivery organisation that exist primarily to manage, govern, or facilitate software work rather than to produce it. Use job descriptions, organisational design literature, and analyst frameworks to estimate the proportion of total headcount these represent.
2. **Apply transaction-cost theory**: Review Coase's Theory of the Firm and Williamson's transaction-cost economics. Assess what these predict when a major category of production cost (software development) is dramatically reduced. What does theory say about firm boundaries, vertical integration, and internal hierarchy when this changes?
3. **Mine historical analogues**: Research what happened to organisational structure during: (a) factory automation in manufacturing, (b) ERP adoption in the 1990s to 2000s, (c) cloud computing adoption, (d) low-code and no-code platform adoption. Did coordination overhead reduce? Did it shift? Did it grow?
4. **Survey current evidence on AI coding productivity**: Gather published data on AI coding tool productivity multipliers (developer throughput, time-to-deploy, defect rates). Extrapolate: what does a 5x, 10x, or 100x productivity improvement imply for the size of the coordination layer relative to the delivery layer?
5. **Identify automatable versus irreducible coordination**: For each category of coordination work (roadmapping, prioritisation, stakeholder alignment, estimation, status reporting, change management), assess which are amenable to AI automation and which require human judgment. Use existing AI agent capability benchmarks and qualitative reasoning.
6. **Second-order effects**: Consider what new coordination demands emerge: more frequent releases, more systems, AI-generated code that needs reviewing, more diverse stakeholder requests enabled by lower build costs, and governance of AI agents themselves.
7. **Synthesis**: Describe 3 to 5 plausible future organisational shapes for software-dependent organisations, differentiated by how aggressively they restructure in response to falling software costs. Identify the decision points (make vs. buy, centralise vs. federate, human vs. AI coordination) that determine which shape a given organisation adopts.

## Sources

- [x] [The Nature of the Firm - Ronald Coase (1937)](https://onlinelibrary.wiley.com/doi/full/10.1111/j.1468-0335.1937.tb00002.x) - seeded primary source; checked, but the Wiley page returned status 403 from the runner, so it served as a source pointer rather than directly quotable evidence here
- [x] [Markets and Hierarchies - Oliver Williamson (1975)](https://www.hup.harvard.edu/books/9780029348208) - seeded source pointer; the Harvard University Press page was accessible only as book metadata, so it was used for framing rather than direct quotation
- [x] [The Second Machine Age - Brynjolfsson and McAfee (2014)](https://www.amazon.com/Second-Machine-Age-Prosperity-Technologies/dp/0393350649) - seeded source pointer; the Amazon page was accessible but not directly useful for evidence extraction in this environment
- [x] [McKinsey: Unleashing developer productivity with generative AI, via McKinsey August 2023 explainer](https://www.mckinsey.com/~/media/mckinsey/featured%20insights/mckinsey%20explainers/whats%20the%20future%20of%20generative%20ai%20an%20early%20view%20in%2015%20charts/whats-the-future-of-generative-ai-an-early-view-in-15-charts.pdf) - accessible McKinsey material citing the seeded article's task-speed results
- [x] [GitHub Copilot productivity research (Kalliamvakou, 2022)](https://github.blog/2022-09-07-research-quantifying-github-copilots-impact-on-developer-productivity-and-happiness/) - controlled experiment on task completion speed and developer experience
- [x] [Stripe Developer Coefficient summary](https://www.software.com/src/developer-productivity-a-bigger-constraint-to-innovation-than-capital) - accessible summary quoting Stripe's 2018 findings on maintenance burden and developer productivity
- [x] [CHAOS Report - Standish Group](https://www.standishgroup.com/sample_research_files/CHAOSReport2015-Final.pdf) - seeded link checked; returned status 404 and is not used as evidence
- [x] [Devin AI - Cognition Labs](https://www.cognition.ai/blog/introducing-devin) - vendor primary claim about autonomous software-engineering capability; used with low evidentiary weight
- [x] [Cursor](https://cursor.com/) - vendor site checked; useful as a signal of market positioning and adoption claims, not as independent productivity evidence
- [x] [The Mythical Man-Month - Fred Brooks (1975)](https://www.amazon.com/Mythical-Man-Month-Software-Engineering-Anniversary/dp/0201835959) - seeded source pointer for coordination-cost logic; the Amazon page was accessible only as book metadata
- [x] [Wired: "Vibe coding" and the future of software](https://www.wired.com/story/vibe-coding-future-of-software/) - seeded link checked; returned status 404 and is not used as evidence
- [x] [Harvard Business Review: Excess Management Is Costing the U.S. $3 Trillion Per Year](https://hbr.org/2016/09/excess-management-is-costing-the-us-3-trillion-per-year) - economy-wide bureaucracy baseline
- [x] [London Business School: Bureaucracy, where to liberate $3 trillion](https://www.london.edu/think/bureaucracy-where-to-liberate-3-trillion) - accessible restatement of Hamel and Zanini's core management-overhead numbers
- [x] [a16z: Why Software Is Eating the World](https://a16z.com/why-software-is-eating-the-world/) - framing source for software as a dominant production factor
- [x] [Gartner: low-code and no-code market and organisational impact](https://www.gartner.com/en/information-technology/insights/low-code-no-code) - seeded link checked; returned status 403, so Microsoft and low-code governance sources below were used instead
- [x] [Massachusetts Institute of Technology (MIT) Sloan: Leadership and AI insights for 2025](https://mitsloan.mit.edu/ideas-made-to-matter/leadership-and-ai-insights-2025-latest-mit-sloan-management-review) - accessible MIT Sloan Management Review gateway page covering AI governance and organisational design implications
- [x] [Stack Overflow Developer Survey 2024](https://survey.stackoverflow.co/2024/) - empirical baseline on AI adoption and time spent searching for solutions
- [x] [Scrum Guide](https://scrumguides.org/scrum-guide.html) - primary framework description of Scrum roles and responsibilities
- [x] [Atlassian: Agile Scrum roles and responsibilities](https://www.atlassian.com/agile/scrum/roles) - accessible explanation of Scrum team composition and role structure
- [x] [Scaled Agile Framework: Agile Release Train](https://scaledagileframework.com/agile-release-train/) - scaled-delivery role structure and headcount band
- [x] [Harvard Digital, Data and Design (D^3): The AI Revolution in Software Development](https://d3.harvard.edu/the-ai-revolution-in-software-development-how-generative-ai-is-reshaping-coding-practices/) - accessible summary of the 2024 working paper "Generative AI and the Nature of Work"
- [x] [Google Cloud: Identifying and tracking toil using Site Reliability Engineering (SRE) principles](https://cloud.google.com/blog/products/management-tools/identifying-and-tracking-toil-using-sre-principles) - automation of repetitive operations work
- [x] [Google Cloud: Transitioning a typical engineering ops team into an SRE powerhouse](https://cloud.google.com/blog/products/management-tools/transitioning-a-typical-engineering-ops-team-into-an-sre-powerhouse) - operations automation changes team shape rather than eliminating operations
- [x] [Amazon Web Services (AWS) Prescriptive Guidance: Building a Cloud Center of Excellence within your organization](https://docs.aws.amazon.com/pdfs/prescriptive-guidance/latest/cloud-center-of-excellence/cloud-center-of-excellence.pdf) - cloud-era governance and operating-model analogue
- [x] [Microsoft Power Platform Center of Excellence Starter Kit overview](https://learn.microsoft.com/en-us/power-platform/guidance/coe/overview) - low-code governance analogue
- [x] [Quickbase: Low-Code CoE, Governance for IT Directors](https://www.quickbase.com/blog/low-code-coe-enterprise-governance-it-director) - low-code governance analogue
- [x] [Kissflow: How to Set Up a No-Code Center of Excellence](https://kissflow.com/no-code/how-to-set-up-a-no-code-coe/) - low-code and no-code governance analogue
- [x] [Strategic Approaches to ERP Implementation](https://scholarworks.lib.csusb.edu/cgi/viewcontent.cgi?article=1104&context=jitim) - ERP centralization and process-standardization analogue

---

## Research Skill Output

[fact] This section retains the full output from running the research skill. Sections §0 to §5 are the investigation, and §6 seeds the Findings section below.

### §0 Initialise

- [fact] **Research question restated:** In a mid-to-large organisation that depends on software, how much of the organisation exists mainly to coordinate software work rather than produce it directly, and what happens to that organisational layer when routine software production becomes much cheaper?
- [fact] **Scope confirmed:** The item focuses on software-dependent mid-to-large organisations, coordination and governance roles, transaction-cost logic, historical analogues (ERP, cloud, low-code and no-code, automation), and present-day AI coding evidence. Deep tool benchmarking and startup-only team structures remain out of scope.
- [fact] **Constraints confirmed:** Only publicly accessible sources are used. Where direct headcount decomposition is unavailable, estimates are marked [inference] rather than stated as census facts.
- [fact] **Output format:** Structured research skill output with explicit [fact], [inference], and [assumption] labels, followed by Findings with Executive Summary, Key Findings, Evidence Map, Assumptions, Analysis, Risks, Gaps, Uncertainties, Open Questions, and Output.
- [fact] **Prior work cross-reference:** Before starting §2, I checked `Research/completed/` for adjacent work. The most relevant prior items were `2026-03-23-software-factory.md`, `2026-03-10-nature-of-the-firm-coase-organisations.md`, `2026-03-26-bureaucracy-growth-and-the-boomer-generation-hypothesis.md`, `2026-03-12-ai-team-size-strike-team-thesis.md`, and `2026-03-12-ai-force-multiplier-ambition-expansion.md`.
- [inference] This item extends that prior repository work by adding a bounded estimate of the software-delivery coordination layer, checking the seeded source list directly, and comparing the present AI wave with ERP, cloud, and low-code and no-code organisational shifts.

### §1 Question Decomposition

- [fact] Root question decomposed into six branches.

**Branch A - Current coordination layer**
- A1: What explicit roles in standard software-delivery frameworks are coordination, translation, or governance roles rather than direct production roles?
- A2: What economy-wide evidence exists on management and administrative overhead?
- A3: What bounded estimate can be made for software-delivery organisations specifically?

**Branch B - Proxy and translator functions**
- B1: Which roles exist mainly to turn business intent into tickets, plans, queues, and governance artifacts?
- B2: Which of those roles exist because software production has been slow, uncertain, and difficult to validate?

**Branch C - Transaction-cost and organisational theory**
- C1: What does transaction-cost logic predict when one large production cost falls materially?
- C2: Which parts of hierarchy disappear, and which persist because of risk, asset specificity, and accountability?

**Branch D - Historical analogues**
- D1: What happened to coordination layers after ERP adoption?
- D2: What happened after cloud adoption and the rise of platform and Site Reliability Engineering (SRE) operating models?
- D3: What happened when low-code and no-code tools reduced local software-building friction?

**Branch E - Current AI evidence**
- E1: What routine software tasks already show measurable acceleration?
- E2: How much evidence is there that AI removes project-management and collaboration friction, not just coding time?
- E3: What evidence supports or fails to support the stronger claim that software cost is approaching zero?

**Branch F - Future-state design**
- F1: Which coordination tasks are likely to be automated first?
- F2: Which tasks remain human because they express authority, trade-offs, and risk appetite?
- F3: What plausible organisational shapes follow from those shifts?

### §2 Investigation

#### A. Current coordination layer

- [fact] The Scrum Guide defines a Scrum system in which a Product Owner orders work, a Scrum Master fosters the environment and process, and the Scrum Team turns backlog items into an increment of value. Source: [Scrum Guide](https://scrumguides.org/scrum-guide.html).
- [fact] Atlassian's summary of Scrum roles states that a Scrum team typically consists of 5 to 11 members including the Product Owner, Scrum Master, and Development Team. Source: [Atlassian Scrum roles](https://www.atlassian.com/agile/scrum/roles).
- [fact] The Scaled Agile Framework states that an Agile Release Train (ART) generally consists of 50 to 125 people and is supported by Product Management, System Architect, Release Train Engineer, Business Owners, Shared Services, Epic Owners, and System Teams in addition to the underlying Agile Teams. Source: [Scaled Agile Framework, Agile Release Train](https://scaledagileframework.com/agile-release-train/).
- [fact] Gary Hamel and Michele Zanini's widely cited bureaucracy estimate, restated accessibly by London Business School, reports 23.8 million managers, supervisors, and administrative support staff in the United States workforce by 2014, or roughly one manager or administrator for every 4.7 other workers. Source: [London Business School](https://www.london.edu/think/bureaucracy-where-to-liberate-3-trillion); [Harvard Business Review](https://hbr.org/2016/09/excess-management-is-costing-the-us-3-trillion-per-year).
- [fact] The same Hamel and Zanini estimate says excess bureaucracy in the United States creates more than $3 trillion in lost economic output. Source: [Harvard Business Review](https://hbr.org/2016/09/excess-management-is-costing-the-us-3-trillion-per-year).
- [fact] An accessible summary of Stripe's 2018 Developer Coefficient report states that the average developer spends 17.3 hours per week dealing with technical debt, bad code, and maintenance jobs such as debugging and refactoring. Source: [Software.com summary of Stripe report](https://www.software.com/src/developer-productivity-a-bigger-constraint-to-innovation-than-capital).
- [fact] The Stack Overflow Developer Survey 2024 reports that 61% of respondents spend more than 30 minutes per day searching for answers or solutions to problems, showing that a meaningful part of developer time is already consumed by retrieval and coordination-adjacent overhead rather than net-new construction. Source: [Stack Overflow Developer Survey 2024](https://survey.stackoverflow.co/2024/).
- [inference] In a standard Scrum team, 2 of the named roles, Product Owner and Scrum Master, are coordination and translation roles rather than direct software-production roles, implying an explicit coordination share of about 18% to 40% before line management, architecture, release governance, security, and portfolio layers are counted. Sources: [Scrum Guide](https://scrumguides.org/scrum-guide.html); [Atlassian Scrum roles](https://www.atlassian.com/agile/scrum/roles).
- [inference] In scaled enterprises, the coordination layer is thicker than the Scrum baseline because train-level and portfolio-level roles are added on top of team-level roles. The best-supported bounded estimate for mid-to-large software-dependent organisations is therefore that explicit coordination and governance roles are at least in the high teens of software-delivery headcount and often around one quarter to one third once management, architecture, release, compliance, and shared-service layers are included. Sources: [Scaled Agile Framework](https://scaledagileframework.com/agile-release-train/); [London Business School](https://www.london.edu/think/bureaucracy-where-to-liberate-3-trillion); [Harvard Business Review](https://hbr.org/2016/09/excess-management-is-costing-the-us-3-trillion-per-year).
- [inference] The roles most clearly functioning as proxies or translators between business intent and software execution are Product Owners, Product Managers when acting as backlog routers rather than market shapers, Business Analysts, Scrum Masters, project and programme managers, delivery managers, release and change managers, and solution architects when their work is mainly handoff management rather than difficult technical judgment. Sources: [Scrum Guide](https://scrumguides.org/scrum-guide.html); [Scaled Agile Framework](https://scaledagileframework.com/agile-release-train/).

#### B. Transaction-cost and organisational logic

- [fact] The seeded Coase link returned status 403 from the runner, and the seeded Williamson book page exposed only book metadata rather than accessible text. I therefore used prior repository synthesis to avoid inventing unsupported quotations from inaccessible primary texts. Source pointers checked: [Coase link](https://onlinelibrary.wiley.com/doi/full/10.1111/j.1468-0335.1937.tb00002.x); [Williamson link](https://www.hup.harvard.edu/books/9780029348208).
- [inference] Transaction-cost logic implies that when a major production cost falls, the firm no longer needs as much internal hierarchy devoted to batching, rationing, and translating demand into scarce production slots. What remains are the parts of hierarchy that still reduce uncertainty, protect relationship-specific assets, assign authority, and absorb regulatory accountability.
- [inference] Applied to software organisations, the hierarchy most exposed by lower coding cost is the layer created to manage scarce engineering throughput: backlog grooming, sprint arbitration, estimation ceremonies, queue management, and repeated business-to-technical translation. The least exposed layer is the one that owns funding choices, policy, architecture standards, risk acceptance, and external accountability.

#### C. Historical analogues

- [fact] ERP implementation research describes ERP systems as converging organisational knowledge across the firm, standardising processes, and centralising functional areas and shared services such as Human Resources (HR) and Finance. Source: [Strategic Approaches to ERP Implementation](https://scholarworks.lib.csusb.edu/cgi/viewcontent.cgi?article=1104&context=jitim).
- [fact] The same ERP research notes that customers often found at least 20% of needed functionality missing from the selected package, meaning ERP adoption did not remove adaptation and integration work even while it standardised large parts of operations. Source: [Strategic Approaches to ERP Implementation](https://scholarworks.lib.csusb.edu/cgi/viewcontent.cgi?article=1104&context=jitim).
- [inference] ERP reduced local clerical translation and duplicated process work, but it did not eliminate coordination. It recentralised coordination into process ownership, integration, shared services, standards, and governance roles.
- [fact] Amazon Web Services (AWS) Cloud Center of Excellence guidance defines a Cloud Center of Excellence (CCoE) as a cross-functional group that leads cloud adoption, governance, training, cost optimization, and cultural change across business, people, governance, platform, security, and operations perspectives. Source: [AWS Prescriptive Guidance](https://docs.aws.amazon.com/pdfs/prescriptive-guidance/latest/cloud-center-of-excellence/cloud-center-of-excellence.pdf).
- [fact] Google Cloud's SRE guidance defines toil as manual, repetitive, automatable work and states that Google SRE teams aim to keep toil below 50% of each engineer's time so that the rest is preserved for engineering project work. Source: [Google Cloud, identifying and tracking toil](https://cloud.google.com/blog/products/management-tools/identifying-and-tracking-toil-using-sre-principles).
- [fact] Google Cloud's network-operations case study explains that simply adding more people to a growing operations function did not scale; the team changed shape by automating repetitive operations work and turning network operators into software-building reliability engineers. Source: [Google Cloud, transitioning into an SRE powerhouse](https://cloud.google.com/blog/products/management-tools/transitioning-a-typical-engineering-ops-team-into-an-sre-powerhouse).
- [inference] Cloud adoption reduced some hands-on infrastructure labor but created new central coordination roles around platform standards, security, governance, automation, cost control, and enablement. It changed the composition of the coordination layer more than it removed that layer.
- [fact] Microsoft's Power Platform Center of Excellence documentation says a low-code Center of Excellence provides leadership, governance, monitoring, adoption capability, support, training, and defined processes to scale citizen development safely. Source: [Microsoft Power Platform CoE overview](https://learn.microsoft.com/en-us/power-platform/guidance/coe/overview).
- [fact] Quickbase's low-code governance guide says low-code adoption without governance creates application sprawl, data silos, security vulnerabilities, compliance problems, and shadow information technology (IT), and that a Center of Excellence exists to standardize, guide, and scale low-code initiatives. Source: [Quickbase low-code CoE guide](https://www.quickbase.com/blog/low-code-coe-enterprise-governance-it-director).
- [fact] Kissflow's no-code Center of Excellence guide argues that low-code and no-code adoption creates a need for governance, approval rules, maintenance responsibility, training, and a product marketplace of approved components rather than simple decentralization without oversight. Source: [Kissflow no-code CoE guide](https://kissflow.com/no-code/how-to-set-up-a-no-code-coe/).
- [inference] Low-code and no-code did not make organisational coordination disappear. They compressed software-building scarcity for small workflows but created a new governance layer for maker support, compliance, and reuse.

#### D. Present AI evidence on software-production cost

- [fact] GitHub's controlled experiment with 95 professional developers found that developers using GitHub Copilot completed the task 55% faster on average than developers without Copilot, with a higher task-completion rate as well. Source: [GitHub Copilot productivity research](https://github.blog/2022-09-07-research-quantifying-github-copilots-impact-on-developer-productivity-and-happiness/).
- [fact] McKinsey's 2023 generative-AI explainer reports that, in tests with 40 McKinsey developers, documenting code functionality could be completed in half the time, writing new code in nearly half the time, and refactoring code in 20% to 30% less time, while high-complexity tasks showed less than 10% reduction. Source: [McKinsey August 2023 explainer document](https://www.mckinsey.com/~/media/mckinsey/featured%20insights/mckinsey%20explainers/whats%20the%20future%20of%20generative%20ai%20an%20early%20view%20in%2015%20charts/whats-the-future-of-generative-ai-an-early-view-in-15-charts.pdf).
- [fact] Harvard Business School's Digital, Data and Design (D^3) Institute summary of the 2024 working paper "Generative AI and the Nature of Work" reports that developers with GitHub Copilot access increased coding activities by 5.4 percentage points, a 12.37% increase, while reducing project-management activities by 10 percentage points, a 24.93% decrease. Source: [Harvard Digital, Data and Design summary](https://d3.harvard.edu/the-ai-revolution-in-software-development-how-generative-ai-is-reshaping-coding-practices/).
- [fact] The same Harvard summary reports that Copilot users worked in repositories with 17 fewer peers on average, a 79.3% reduction compared with non-users. Source: [Harvard Digital, Data and Design summary](https://d3.harvard.edu/the-ai-revolution-in-software-development-how-generative-ai-is-reshaping-coding-practices/).
- [inference] That repository-level difference suggests that some routine collaboration frictions were bypassed, but the summary does not by itself prove why team interaction changed.
- [fact] The Stack Overflow Developer Survey 2024 reports that 76% of respondents are using or planning to use AI tools in their development process, with 62% currently using them. Source: [Stack Overflow Developer Survey 2024](https://survey.stackoverflow.co/2024/).
- [fact] Cognition's Devin launch post claims that Devin can plan and execute complex engineering tasks end to end and reports a 13.86% resolution rate on a subset of SWE-bench. Source: [Cognition Devin launch post](https://www.cognition.ai/blog/introducing-devin).
- [fact] Cursor's homepage claims autonomous agents can build, test, and demo features end to end and includes enterprise adoption testimonials, but it does not provide an independently auditable methodology for the productivity claims shown there. Source: [Cursor homepage](https://cursor.com/).
- [inference] The public evidence supports material acceleration for routine coding, documentation, refactoring, and some project-management-adjacent work. It does not support the literal claim that enterprise software cost is already near zero for complex, regulated, multi-system change.
- [assumption] If agentic tooling continues to improve rapidly, the routine portion of software delivery may become cheap enough that the organisational bottleneck shifts decisively from production to prioritisation and governance. This assumption is justified by present directional evidence, but public data does not yet prove a stable 5x to 10x end-to-end gain for large enterprise programmes.

#### E. Automatable versus irreducible coordination

- [fact] Massachusetts Institute of Technology (MIT) Sloan Management Review's 2025 leadership roundup argues that organisations adopting generative AI should assemble a cross-functional leadership team, define guardrails, provide training, offer approved tools, and connect AI use to strategic business objectives. Source: [MIT Sloan](https://mitsloan.mit.edu/ideas-made-to-matter/leadership-and-ai-insights-2025-latest-mit-sloan-management-review).
- [fact] Microsoft's CoE documentation states explicitly that a CoE requires people, communication, defined requirements, and processes, not just tools. Source: [Microsoft Power Platform CoE overview](https://learn.microsoft.com/en-us/power-platform/guidance/coe/overview).
- [fact] AWS's CCoE guidance similarly defines cloud transformation as requiring leadership sponsorship, cultural change, training, communication, and governance rather than only technical automation. Source: [AWS Prescriptive Guidance](https://docs.aws.amazon.com/pdfs/prescriptive-guidance/latest/cloud-center-of-excellence/cloud-center-of-excellence.pdf).
- [inference] Coordination work that is mainly artifact transformation is the most automatable: backlog drafting, task decomposition, status summaries, test and compliance evidence collation, release-note generation, simple prioritisation under fixed rules, and repetitive toil tickets that can be turned into self-service flows.
- [inference] Coordination work that expresses authority and trade-offs is the least automatable: deciding which objectives matter more than others, setting risk appetite, resolving stakeholder conflict, approving exceptions, assigning accountability, and deciding when local optimization should be rejected for system-level reasons.
- [inference] Agile rituals, estimation cycles, and roadmap ceremonies shrink most where their current purpose is to ration scarce developers and preserve queue discipline. They persist where they are the mechanism for commitment, dependency management, or regulated change control.

#### F. Source audit and inaccessible seeded sources

- [fact] The seeded Standish Group CHAOS Report link returned status 404 when checked directly: `https://www.standishgroup.com/sample_research_files/CHAOSReport2015-Final.pdf`. Outcome: not used as evidence.
- [fact] The seeded Wired link returned status 404 when checked directly: `https://www.wired.com/story/vibe-coding-future-of-software/`. Outcome: not used as evidence.
- [fact] The seeded Gartner low-code page returned status 403 when checked directly: `https://www.gartner.com/en/information-technology/insights/low-code-no-code`. Outcome: replaced with accessible Microsoft, Quickbase, Kissflow, and AWS governance sources.
- [fact] The seeded McKinsey article timed out from the runner, so the accessible McKinsey explainer document that cites the same software-engineering task results was used instead.

### §3 Reasoning

- [fact] The strongest direct evidence about today's coordination burden comes from three different layers: economy-wide bureaucracy counts, explicit software-framework role designs, and developer-time data showing large maintenance and search overhead.
- [inference] Because no public source in this item provides a clean census of software-delivery headcount by role, the right answer is a bounded estimate rather than a falsely precise percentage.
- [inference] The lower bound is around the high teens because economy-wide managerial and administrative intensity is already near that level and standard Scrum teams explicitly include coordination roles even before enterprise scaling is added.
- [inference] The upper part of the bounded estimate reaches roughly one quarter to one third in mid-to-large enterprises because scaled-delivery frameworks add train-level, portfolio-level, architecture, compliance, and release roles on top of the team-level coordination roles.
- [fact] The current AI productivity evidence is uneven. The strongest evidence is for routine work, not for high-complexity enterprise change.
- [inference] Therefore the organisational consequence is not "management disappears." The stronger conclusion is "translation-heavy coordination shrinks first; governance-heavy coordination remains and becomes more concentrated."

### §4 Consistency Check

- [fact] GitHub's 55% faster task result, McKinsey's 20% to 50% routine-task speedups, and Harvard's shift away from project-management activity are directionally consistent: all three sources show AI compressing routine software work and some collaboration friction.
- [fact] None of those sources claim that complex enterprise software work is fully automated today. McKinsey explicitly shows less than 10% reduction for high-complexity tasks, so the item does not overstate the present evidence.
- [fact] ERP, cloud, and low-code analogues all point the same way: execution becomes easier, but governance and enablement layers re-form around the new capability. The analogues therefore reinforce rather than contradict one another.
- [fact] No contradiction remains between the "smaller execution teams" conclusion and the "persistent governance core" conclusion, because those apply to different functions.
- [fact] The main unresolved inconsistency risk is the absence of a direct public headcount census for software-delivery organisations, which is why the quantitative answer is expressed as an [inference] range rather than a [fact].

### §5 Depth and Breadth Expansion

- [inference] **Economic lens:** The software-economics shift is large enough to matter strategically. McKinsey treats software engineering as one of the major value drivers for generative AI across industries and highlights banking as a sector with meaningful software-engineering upside. Source: [McKinsey August 2023 explainer document](https://www.mckinsey.com/~/media/mckinsey/featured%20insights/mckinsey%20explainers/whats%20the%20future%20of%20generative%20ai%20an%20early%20view%20in%2015%20charts/whats-the-future-of-generative-ai-an-early-view-in-15-charts.pdf).
- [fact] **Historical lens:** ERP, cloud, and low-code and no-code all show the same structural pattern. When a technology reduces local execution cost, organisations standardize, centralize, and then rebuild a governance layer around the new bottlenecks. Sources: [Strategic Approaches to ERP Implementation](https://scholarworks.lib.csusb.edu/cgi/viewcontent.cgi?article=1104&context=jitim); [AWS Prescriptive Guidance](https://docs.aws.amazon.com/pdfs/prescriptive-guidance/latest/cloud-center-of-excellence/cloud-center-of-excellence.pdf); [Microsoft Power Platform CoE overview](https://learn.microsoft.com/en-us/power-platform/guidance/coe/overview).
- [fact] **Behavioural lens:** Harvard's 2024 working-paper summary suggests AI does not merely speed work up; it changes the composition of work by shifting effort toward core coding and away from project-management activity and some collaboration friction. Source: [Harvard Digital, Data and Design summary](https://d3.harvard.edu/the-ai-revolution-in-software-development-how-generative-ai-is-reshaping-coding-practices/).
- [fact] **Regulatory lens:** MIT Sloan, Microsoft, and AWS all converge on the need for leadership guardrails, approved tools, training, and defined governance processes once AI or low-code capabilities spread. Sources: [MIT Sloan](https://mitsloan.mit.edu/ideas-made-to-matter/leadership-and-ai-insights-2025-latest-mit-sloan-management-review); [Microsoft Power Platform CoE overview](https://learn.microsoft.com/en-us/power-platform/guidance/coe/overview); [AWS Prescriptive Guidance](https://docs.aws.amazon.com/pdfs/prescriptive-guidance/latest/cloud-center-of-excellence/cloud-center-of-excellence.pdf).
- [inference] **Political-economy lens:** Bureaucratic layers are unlikely to disappear automatically even when the original production bottleneck weakens, because those layers often accumulate authority and self-justification. The implication is that organisational redesign requires deliberate executive action rather than passive technology adoption.

### §6 Synthesis

**Executive summary:**

- [inference] In mid-to-large software-dependent organisations, the coordination and governance layer created around software delivery is best estimated at at least the high teens of headcount and often around one quarter to one third, and falling coding costs are likely to compress that layer without eliminating it.
- [fact] The strongest evidence does not show software cost at literal zero today. It shows 20% to 55% gains on routine coding, documentation, and refactoring tasks, plus a measurable shift of developer effort away from project-management activity and collaboration friction.
- [inference] The roles most exposed are translation and queue-management roles whose main output is artifacts that move work across boundaries: backlog shaping, sprint arbitration, status production, handoff management, and repetitive release or compliance administration.
- [inference] The roles least exposed are those that encode authority, trade-offs, standards, and external accountability: prioritisation among conflicting goals, architecture policy, risk acceptance, regulatory interpretation, and exception handling.
- [inference] The more plausible organisational outcome is a smaller execution layer around stronger platforms, self-service automation, and a more concentrated human governance core.

**Key findings:**

- [fact] 1. **High confidence:** Mid-to-large software-dependent organisations already carry a substantial explicit coordination layer, and the best-supported estimate is that these roles occupy at least the high teens of headcount and often roughly one quarter to one third once team, train, architecture, release, and management layers are combined.
- [fact] 2. **High confidence:** Product Owner, Scrum Master, Business Analyst, project or programme manager, delivery manager, release manager, change manager, and intermediary solution-architecture roles exist largely because business intent and software execution are separated by translation, validation, batching, and queueing costs.
- [inference] 3. **High confidence:** Transaction-cost logic predicts that when coding becomes materially cheaper, firms should reduce the hierarchy devoted to allocating scarce engineering labor, but should retain and often strengthen the hierarchy that owns standards, risk, compliance, and residual decision rights.
- [fact] 4. **High confidence:** ERP, cloud, and low-code and no-code adoption all reduced some local execution work while creating new central coordination structures such as shared services, platform teams, Cloud Centers of Excellence, and low-code Centers of Excellence.
- [fact] 5. **Medium to high confidence:** Current AI evidence supports large productivity gains for routine software tasks and moderate reductions in collaboration friction, but does not yet support the claim that complex enterprise software delivery is near-zero cost end to end.
- [inference] 6. **High confidence:** Coordination work disappears in sequence: artifact transformation and routine status work first, structured planning and handoff work second, and judgment-intensive governance last.
- [inference] 7. **Medium confidence:** Agile rituals, estimation cycles, and roadmaps will thin sharply where they exist mainly to ration scarce developers, but they will persist in organisations that still need commitment management, dependency control, and regulated change review.
- [inference] 8. **Medium to high confidence:** The most plausible future organisational shapes are smaller software-execution cells around platforms and guardrails, with regulated firms converging on a dual-core model of AI-heavy delivery plus concentrated governance rather than full managerial collapse.

**Evidence map:**

- [fact] | Claim | Source | Confidence | Notes |
- [fact] |---|---|---|---|
- [fact] | Coordination layer is at least high teens and often around one quarter to one third of headcount | [Harvard Business Review](https://hbr.org/2016/09/excess-management-is-costing-the-us-3-trillion-per-year), [London Business School](https://www.london.edu/think/bureaucracy-where-to-liberate-3-trillion), [Scrum Guide](https://scrumguides.org/scrum-guide.html), [Atlassian Scrum roles](https://www.atlassian.com/agile/scrum/roles), [Scaled Agile Framework](https://scaledagileframework.com/agile-release-train/) | high | Range is an inference built from explicit role structures plus economy-wide bureaucracy counts |
- [fact] | Proxy and translator roles are Product Owner, Scrum Master, Business Analyst, project or programme management, release and change management, and intermediary architecture | [Scrum Guide](https://scrumguides.org/scrum-guide.html), [Scaled Agile Framework](https://scaledagileframework.com/agile-release-train/) | high | These roles exist to order, translate, synchronize, and govern work across boundaries |
- [fact] | Falling coding cost should shrink throughput-allocation hierarchy but not governance hierarchy | Seeded Coase and Williamson source pointers checked directly, plus synthesis from this item's external analogues | high | Theory claim expressed as inference because seeded primary texts were not directly quotable in this environment |
- [fact] | ERP, cloud, and low-code create new governance and enablement layers instead of removing coordination altogether | [Strategic Approaches to ERP Implementation](https://scholarworks.lib.csusb.edu/cgi/viewcontent.cgi?article=1104&context=jitim), [AWS Prescriptive Guidance](https://docs.aws.amazon.com/pdfs/prescriptive-guidance/latest/cloud-center-of-excellence/cloud-center-of-excellence.pdf), [Microsoft Power Platform CoE overview](https://learn.microsoft.com/en-us/power-platform/guidance/coe/overview), [Quickbase](https://www.quickbase.com/blog/low-code-coe-enterprise-governance-it-director), [Kissflow](https://kissflow.com/no-code/how-to-set-up-a-no-code-coe/) | high | Historical analogue pattern is consistent across three technology waves |
- [fact] | AI materially accelerates routine coding work but not high-complexity enterprise change | [GitHub Copilot research](https://github.blog/2022-09-07-research-quantifying-github-copilots-impact-on-developer-productivity-and-happiness/), [McKinsey August 2023 explainer document](https://www.mckinsey.com/~/media/mckinsey/featured%20insights/mckinsey%20explainers/whats%20the%20future%20of%20generative%20ai%20an%20early%20view%20in%2015%20charts/whats-the-future-of-generative-ai-an-early-view-in-15-charts.pdf), [Harvard Digital, Data and Design summary](https://d3.harvard.edu/the-ai-revolution-in-software-development-how-generative-ai-is-reshaping-coding-practices/) | medium to high | High-complexity tasks remain much less compressed than routine tasks |
- [fact] | Artifact transformation disappears before judgment-intensive governance | [Harvard Digital, Data and Design summary](https://d3.harvard.edu/the-ai-revolution-in-software-development-how-generative-ai-is-reshaping-coding-practices/), [MIT Sloan](https://mitsloan.mit.edu/ideas-made-to-matter/leadership-and-ai-insights-2025-latest-mit-sloan-management-review), [AWS Prescriptive Guidance](https://docs.aws.amazon.com/pdfs/prescriptive-guidance/latest/cloud-center-of-excellence/cloud-center-of-excellence.pdf), [Microsoft Power Platform CoE overview](https://learn.microsoft.com/en-us/power-platform/guidance/coe/overview) | high | Tools reduce routine friction; leadership, guardrails, and risk ownership remain human-heavy |
- [fact] | Agile rituals thin where they ration scarce engineers but survive where they encode commitments and risk controls | [Scrum Guide](https://scrumguides.org/scrum-guide.html), [Scaled Agile Framework](https://scaledagileframework.com/agile-release-train/), [MIT Sloan](https://mitsloan.mit.edu/ideas-made-to-matter/leadership-and-ai-insights-2025-latest-mit-sloan-management-review) | medium | This is a structural inference from role purpose, not a direct time-series measurement |
- [fact] | Future shape is smaller execution cells plus concentrated governance, especially in regulated firms | [McKinsey August 2023 explainer document](https://www.mckinsey.com/~/media/mckinsey/featured%20insights/mckinsey%20explainers/whats%20the%20future%20of%20generative%20ai%20an%20early%20view%20in%2015%20charts/whats-the-future-of-generative-ai-an-early-view-in-15-charts.pdf), [Harvard Digital, Data and Design summary](https://d3.harvard.edu/the-ai-revolution-in-software-development-how-generative-ai-is-reshaping-coding-practices/), [MIT Sloan](https://mitsloan.mit.edu/ideas-made-to-matter/leadership-and-ai-insights-2025-latest-mit-sloan-management-review), [AWS Prescriptive Guidance](https://docs.aws.amazon.com/pdfs/prescriptive-guidance/latest/cloud-center-of-excellence/cloud-center-of-excellence.pdf) | medium to high | Strong directional support, but future-state exact shapes remain inferential |

**Assumptions:**

- [assumption] The current public AI productivity results are a reasonable directional proxy for the next several years of tooling progress, even though frontier models and enterprise workflows will change quickly. **Justification:** multiple independent sources already agree on routine-task acceleration and reduced coordination friction.
- [assumption] Mid-to-large organisations using Scrum- or Scaled Agile Framework (SAFe)-like patterns are representative enough to support a bounded estimate of the coordination layer. **Justification:** these frameworks are common in the kinds of organisations targeted by the question, but they are not a literal census of all firms.

**Analysis:**

- [fact] The evidence is strongest when it moves from direct observation to bounded inference in a disciplined order. First, software organisations explicitly name non-builder coordination roles in their operating models. Second, large economies already devote a substantial share of labor to management and administrative work. Third, current AI tools compress routine coding and project-management-adjacent work but leave high-complexity work and governance less changed. Fourth, historical analogues show that when production gets easier, coordination shifts toward standards, platforms, and risk control rather than vanishing.
- [inference] The central trade-off is therefore not "managers versus no managers." It is "translation layers versus judgment layers." Organisations that remove translation-heavy roles while keeping clear decision rights and governance should become materially leaner. Organisations that keep the old queue-management machinery after coding cost falls will preserve bureaucracy without preserving its original economic rationale.

**Risks, gaps, uncertainties:**

- [fact] There is no clean public dataset breaking software-dependent organisations into builder versus coordinator headcount categories, so the percentage answer is a range rather than a census fact.
- [fact] Several seeded sources were inaccessible or unusable in this environment: the Coase Wiley page returned 403, the Gartner low-code page returned 403, and the seeded Standish and Wired links returned 404.
- [fact] Some AI-productivity evidence comes from vendor-published sources such as Cognition and Cursor. These are useful directional signals but weaker than controlled experiments or independent working papers.
- [fact] Current public evidence is much stronger for routine coding tasks than for complex cross-system, regulated, or politically contested enterprise change.

**Open questions:**

- [fact] What is the best direct empirical method for measuring builder versus coordinator headcount in large software-dependent firms?
- [fact] At what point do AI agents reduce not just coding effort but also the demand for project-management and architecture-intermediary roles in regulated enterprises?
- [fact] Which governance model replaces the investment board or project front door when software throughput is no longer the binding constraint?

### §7 Recursive Review

- [fact] Every substantive claim in §§0 to 6 is either sourced directly, expressed as an inference derived from sourced evidence, or identified as an assumption.
- [fact] The synthesis does not claim literal zero-cost enterprise software delivery today. It states the narrower and better-supported conclusion that routine software work is becoming cheaper and that the coordination bottleneck is migrating.
- [fact] The item records inaccessible seeded sources explicitly and does not silently treat broken or blocked links as supporting evidence.
- [fact] The internal logic is consistent across sections: current overhead estimate, historical analogues, AI evidence, and future-state organisational shapes all point toward thinner translation layers and persistent governance layers.

---

## Findings

### Executive Summary

[inference] In mid-to-large software-dependent organisations, the coordination and governance layer created around software delivery is best estimated at at least the high teens of headcount and often around one quarter to one third, and falling coding costs are likely to compress that layer without eliminating it (see Evidence Map rows 1 and 5). [inference] The roles most exposed are translation and queue-management roles whose main output is turning intent into backlogs, plans, status artifacts, and handoffs, while the least exposed roles are the ones that encode authority, standards, risk appetite, and external accountability (see Evidence Map rows 2 and 6). [inference] The best-supported forecast is smaller Artificial Intelligence (AI)-augmented execution cells operating inside a more concentrated human governance core, which extends the repository's prior `2026-03-23-software-factory.md` conclusion that governance becomes the next bottleneck when coding gets cheaper. [inference] The net headcount effect remains uncertain because the prior repository item `2026-03-12-ai-force-multiplier-ambition-expansion.md` shows that cheaper software can also expand ambition and preserve some coordination demand even as translation-heavy work shrinks.

### Key Findings

1. [inference] **Medium to high confidence:** In mid-to-large software-dependent organisations, explicit coordination and governance roles are best estimated at at least the high teens of headcount and often roughly one quarter to one third once team-level, train-level, architecture, release, and management layers are counted together.
2. [inference] **Medium to high confidence:** Product Owner, Scrum Master, Business Analyst, project or programme manager, delivery manager, release manager, change manager, and intermediary solution-architecture roles exist largely because business intent and software execution are separated by translation, validation, batching, and queueing costs.
3. [inference] **Medium confidence:** The prior repository item `2026-03-10-nature-of-the-firm-coase-organisations.md`, which summarises Coase and Williamson transaction-cost theory, together with this item's historical analogues implies that materially cheaper coding should reduce the hierarchy devoted to allocating scarce engineering labor while preserving and often concentrating the hierarchy that owns standards, compliance, risk acceptance, and residual decision rights.
4. [fact] **High confidence:** Enterprise Resource Planning (ERP), cloud, and low-code and no-code adoption all reduced some local execution work but replaced it with new central structures for standards, enablement, platform governance, shared services, or Centers of Excellence rather than eliminating coordination altogether.
5. [fact] **Medium to high confidence:** Current AI evidence shows large gains on routine software tasks and measurable reductions in project-management friction, but it does not justify the stronger claim that complex enterprise software delivery is already near-zero cost from idea to production.
6. [inference] **Medium confidence:** The first coordination work to compress is artifact transformation, including backlog drafting, routine status reporting, repetitive release administration, and simple compliance evidence gathering, while judgment-intensive work remains human-heavy for longer.
7. [inference] **Medium confidence:** Agile rituals, estimation cycles, and roadmap ceremonies are likely to thin sharply wherever they exist mainly to ration scarce developers, but they will persist wherever they encode commitments, dependency management, risk review, or regulated change control.
8. [inference] **Medium confidence:** The best-supported future organisational equilibrium is smaller software-execution cells around stronger platforms and guardrails, with regulated firms tending toward a dual-core model of AI-heavy delivery plus concentrated governance rather than managerial collapse, although the prior repository item `2026-03-12-ai-force-multiplier-ambition-expansion.md` implies that expanded demand could preserve more coordination capacity than a pure cost-reduction model would predict.

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| Coordination layer is at least high teens and often around one quarter to one third of headcount | [Harvard Business Review](https://hbr.org/2016/09/excess-management-is-costing-the-us-3-trillion-per-year), [London Business School](https://www.london.edu/think/bureaucracy-where-to-liberate-3-trillion), [Scrum Guide](https://scrumguides.org/scrum-guide.html), [Atlassian Scrum roles](https://www.atlassian.com/agile/scrum/roles), [Scaled Agile Framework](https://scaledagileframework.com/agile-release-train/) | medium to high | Range is an inference built from explicit role structures plus economy-wide bureaucracy counts, not a direct census |
| Proxy and translator roles are Product Owner, Scrum Master, Business Analyst, project or programme management, release and change management, and intermediary architecture | [Scrum Guide](https://scrumguides.org/scrum-guide.html), [Scaled Agile Framework](https://scaledagileframework.com/agile-release-train/) | medium to high | The role lists are direct facts; the explanation of why those roles exist is an inference from their responsibilities |
| Historical and theoretical evidence suggests that falling coding cost should shrink throughput-allocation hierarchy before governance hierarchy | `2026-03-10-nature-of-the-firm-coase-organisations.md`, [Strategic Approaches to ERP Implementation](https://scholarworks.lib.csusb.edu/cgi/viewcontent.cgi?article=1104&context=jitim), [AWS Prescriptive Guidance](https://docs.aws.amazon.com/pdfs/prescriptive-guidance/latest/cloud-center-of-excellence/cloud-center-of-excellence.pdf), [Microsoft Power Platform CoE overview](https://learn.microsoft.com/en-us/power-platform/guidance/coe/overview) | medium | This is an inference built from the prior repository synthesis of Coase and Williamson plus the repeated governance-reformation pattern in ERP, cloud, and low-code adoption |
| ERP, cloud, and low-code create new governance and enablement layers instead of removing coordination altogether | [Strategic Approaches to ERP Implementation](https://scholarworks.lib.csusb.edu/cgi/viewcontent.cgi?article=1104&context=jitim), [AWS Prescriptive Guidance](https://docs.aws.amazon.com/pdfs/prescriptive-guidance/latest/cloud-center-of-excellence/cloud-center-of-excellence.pdf), [Microsoft Power Platform CoE overview](https://learn.microsoft.com/en-us/power-platform/guidance/coe/overview), [Quickbase](https://www.quickbase.com/blog/low-code-coe-enterprise-governance-it-director), [Kissflow](https://kissflow.com/no-code/how-to-set-up-a-no-code-coe/) | high | Historical analogue pattern is consistent across three technology waves |
| AI materially accelerates routine coding work but not high-complexity enterprise change | [GitHub Copilot research](https://github.blog/2022-09-07-research-quantifying-github-copilots-impact-on-developer-productivity-and-happiness/), [McKinsey August 2023 explainer document](https://www.mckinsey.com/~/media/mckinsey/featured%20insights/mckinsey%20explainers/whats%20the%20future%20of%20generative%20ai%20an%20early%20view%20in%2015%20charts/whats-the-future-of-generative-ai-an-early-view-in-15-charts.pdf), [Harvard Digital, Data and Design summary](https://d3.harvard.edu/the-ai-revolution-in-software-development-how-generative-ai-is-reshaping-coding-practices/) | medium to high | High-complexity tasks remain much less compressed than routine tasks |
| Artifact transformation is the most likely coordination work to compress before judgment-intensive governance | [Harvard Digital, Data and Design summary](https://d3.harvard.edu/the-ai-revolution-in-software-development-how-generative-ai-is-reshaping-coding-practices/), [MIT Sloan](https://mitsloan.mit.edu/ideas-made-to-matter/leadership-and-ai-insights-2025-latest-mit-sloan-management-review), [AWS Prescriptive Guidance](https://docs.aws.amazon.com/pdfs/prescriptive-guidance/latest/cloud-center-of-excellence/cloud-center-of-excellence.pdf), [Microsoft Power Platform CoE overview](https://learn.microsoft.com/en-us/power-platform/guidance/coe/overview) | medium | This ordering is an inference from current workflow guidance and observed routine-task compression, not a direct time-series measurement |
| Agile rituals thin where they ration scarce engineers but survive where they encode commitments and risk controls | [Scrum Guide](https://scrumguides.org/scrum-guide.html), [Scaled Agile Framework](https://scaledagileframework.com/agile-release-train/), [MIT Sloan](https://mitsloan.mit.edu/ideas-made-to-matter/leadership-and-ai-insights-2025-latest-mit-sloan-management-review) | medium | Structural inference from role purpose, not a direct time-series measurement |
| Future shape is smaller execution cells plus concentrated governance, especially in regulated firms | [McKinsey August 2023 explainer document](https://www.mckinsey.com/~/media/mckinsey/featured%20insights/mckinsey%20explainers/whats%20the%20future%20of%20generative%20ai%20an%20early%20view%20in%2015%20charts/whats-the-future-of-generative-ai-an-early-view-in-15-charts.pdf), [Harvard Digital, Data and Design summary](https://d3.harvard.edu/the-ai-revolution-in-software-development-how-generative-ai-is-reshaping-coding-practices/), [MIT Sloan](https://mitsloan.mit.edu/ideas-made-to-matter/leadership-and-ai-insights-2025-latest-mit-sloan-management-review), [AWS Prescriptive Guidance](https://docs.aws.amazon.com/pdfs/prescriptive-guidance/latest/cloud-center-of-excellence/cloud-center-of-excellence.pdf) | medium to high | Strong directional support, but future-state exact shapes remain inferential |

### Assumptions

- [assumption] The current public AI productivity results are a reasonable directional proxy for the next several years of tooling progress, even though frontier models and enterprise workflows will change quickly. **Justification:** Multiple independent sources already agree on routine-task acceleration and reduced coordination friction.
- [assumption] Mid-to-large organisations using Scrum- or Scaled Agile Framework (SAFe)-like patterns are representative enough to support a bounded estimate of the coordination layer. **Justification:** These frameworks are common in the kinds of organisations targeted by the question, but they are not a literal census of all firms.

### Analysis

- [fact] Current software organisations name coordination roles explicitly because business intent, technical implementation, and organisational accountability are split across different people and time horizons, which is visible in Scrum and Scaled Agile Framework (SAFe) role definitions and in economy-wide bureaucracy estimates.
- [fact] Current AI evidence shows clear compression in routine coding, documentation, and some project-management-adjacent work, which supports the repository's prior `2026-03-23-software-factory.md` conclusion that the bottleneck is migrating away from code production.
- [fact] Historical analogues from Enterprise Resource Planning (ERP), cloud, and low-code and no-code adoption show that cheaper local execution does not produce a coordination-free organisation; it produces a different coordination layer centered on standards, platforms, guardrails, and risk ownership.
- [inference] The strongest competing explanation is demand expansion rather than headcount compression: the prior repository item `2026-03-12-ai-force-multiplier-ambition-expansion.md` argues that cheaper software can unlock more initiatives, which means total coordination demand may fall more slowly than translation work does.
- [inference] The best-supported strategic implication is therefore to redesign around thinner translation layers and clearer decision rights while assuming that governance, residual accountability, and risk acceptance remain necessary even when production technology becomes much cheaper.

### Risks, Gaps, and Uncertainties

- [fact] No clean public dataset decomposes software-dependent firms into builder versus coordinator headcount, so the percentage answer is a bounded estimate rather than a census fact.
- [fact] Several seeded sources were inaccessible or unusable in this environment: the Coase Wiley page returned 403, the Gartner low-code page returned 403, and the seeded Standish and Wired links returned 404.
- [fact] Some AI-productivity evidence comes from vendor-published sources such as Cognition and Cursor, which are useful directional signals but weaker than controlled experiments or independent working papers.
- [fact] Public evidence remains much stronger for routine coding and documentation tasks than for complex cross-system, regulated, or politically contested enterprise change.

### Open Questions

- [fact] What is the best direct empirical method for measuring builder versus coordinator headcount in large software-dependent firms?
- [fact] At what point do AI agents reduce not just coding effort but also the demand for project-management and architecture-intermediary roles in regulated enterprises?
- [fact] Which governance model replaces the investment board or project front door when software throughput is no longer the binding constraint?

---

## Output

- Type: knowledge
- Description: Bounded estimate of the software-delivery coordination layer, a role taxonomy for translation versus judgment work, historical analogues from ERP, cloud, and low-code and no-code, and four plausible post-scarcity organisational shapes.
- Links:
  - [GitHub Copilot productivity research](https://github.blog/2022-09-07-research-quantifying-github-copilots-impact-on-developer-productivity-and-happiness/)
  - [Harvard Digital, Data and Design summary of "Generative AI and the Nature of Work"](https://d3.harvard.edu/the-ai-revolution-in-software-development-how-generative-ai-is-reshaping-coding-practices/)
  - [London Business School bureaucracy analysis](https://www.london.edu/think/bureaucracy-where-to-liberate-3-trillion)
