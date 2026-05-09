---
title: "Build vs improve tradeoff: how should organisations allocate effort between feature delivery and throughput-improvement work, and what do theoretical models imply for velocity, quality, and Pareto-shaped outcomes?"
added: 2026-05-09T02:05:08+00:00
status: reviewing
priority: medium
blocks: []
tags: [workflow, organisational-theory, software-engineering, measurement, throughput, reliability, technical-debt, platform-engineering]
started: 2026-05-09T07:27:16+00:00
completed: ~
output: [knowledge]
cites: [2026-04-01-backpressure-theory-of-constraints, 2026-04-26-software-engineering-investment-case-llm, 2026-03-26-measuring-opportunity-cost]
related: [2026-05-08-productivity-incentive-metrics-quality-review-agentic-ai, 2026-04-01-backpressure-theory-of-constraints, 2026-03-26-measuring-opportunity-cost]
superseded_by: ~
supersedes: ~
item_type: primary
confidence: medium
versions: []
---

# Build vs improve tradeoff: how should organisations allocate effort between feature delivery and throughput-improvement work, and what do theoretical models imply for velocity, quality, and Pareto-shaped outcomes?

## Research Question

Given constrained engineering capacity, how should organisations allocate effort between (1) building features within an existing system and (2) improving the system itself (tooling, process, architecture, and quality controls) to maximise long-run throughput and delivery quality? Which theoretical models from software engineering, operations science, economics, and adjacent disciplines best explain this tradeoff, and how does a Pareto distribution framing (for defects, bottlenecks, or value concentration) change recommended allocation strategies?

## Scope

**In scope:**
- Theory of Constraints, queueing theory, and flow-based models (including Little's Law) as explanations for throughput and latency tradeoffs
- Quality-throughput interactions: how local speed optimisation can increase rework, defect escape, and systemic drag
- Industry models for balancing feature delivery versus capability-building investment (for example platform engineering and reliability engineering)
- Pareto distribution applications to software systems (for example concentration of defects, incidents, or value in a minority of modules or actions)
- Practical decision frameworks for allocation under finite team capacity

**Out of scope:**
- Vendor-specific tool comparisons
- Detailed staffing plans for a single organisation
- Cost modelling that requires proprietary internal financial data
- General Artificial Intelligence policy debates not directly linked to throughput/quality allocation decisions

**Constraints:**
- Expand all acronyms on first use
- Distinguish established empirical findings from conceptual models
- Prioritise models with observable operational metrics over purely rhetorical advice

## Context

Portfolio decisions about build-versus-improve allocation are system decisions rather than task-level decisions, because queue length, bottlenecks, instability, and rework determine how much feature effort becomes shipped value. [inference; source: https://econpapers.repec.org/RePEc:inm:oropre:v:9:y:1961:i:3:p:383-387; https://dora.dev/guides/dora-metrics/; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-01-backpressure-theory-of-constraints.md]

The practical question is when an organisation should keep shipping through the existing system and when it should divert capacity into tooling, architecture, process, or quality controls to restore effective throughput. [inference; source: https://sre.google/workbook/eliminating-toil/; https://arxiv.org/html/2403.06484v1; https://dora.dev/capabilities/platform-engineering/]

## Approach

1. **Model inventory and comparison:** Catalogue relevant models from operations research, software engineering, economics, and systems thinking (for example Theory of Constraints, queueing, reliability growth, dynamic capabilities).
2. **Mechanism mapping:** For each model, map the mechanism linking short-term build effort, system-improvement effort, throughput, velocity, and quality outcomes.
3. **Pareto analysis lens:** Evaluate where Pareto-like concentration appears (defect hotspots, bottleneck resources, high-leverage process constraints) and how it changes investment strategy.
4. **Decision framework synthesis:** Derive practical allocation patterns (for example trigger conditions, leading indicators, and guardrails) for choosing build versus improve over time.

## Sources

Starting points and consulted sources:

- [x] [Goldratt and Cox (1984) The Goal](https://www.routledge.com/The-Goal-A-Process-of-Ongoing-Improvement/Goldratt-Cox/p/book/9781138384020)
- [x] [Little (1961) A Proof for the Queuing Formula: L = (lambda) W](https://econpapers.repec.org/RePEc:inm:oropre:v:9:y:1961:i:3:p:383-387)
- [x] [Reinertsen (2009) The Principles of Product Development Flow](https://www.celeritaspublishing.com/book/the-principles-of-product-development-flow/)
- [x] [Forsgren et al. (2018) Accelerate](https://itrevolution.com/product/accelerate/)
- [x] [Wikipedia Pareto principle](https://en.wikipedia.org/wiki/Pareto_principle)
- [x] [Google Site Reliability Engineering (SRE) Workbook: Eliminating Toil](https://sre.google/workbook/eliminating-toil/)
- [x] [DevOps Research and Assessment (DORA) Metrics Guide](https://dora.dev/guides/dora-metrics/)
- [x] [DevOps Research and Assessment (DORA) Measurement Frameworks Guide](https://dora.dev/research/2025/measurement-frameworks/)
- [x] [DevOps Research and Assessment (DORA) Platform engineering](https://dora.dev/capabilities/platform-engineering/)
- [x] [Google (2024) DORA Accelerate State of DevOps 2024 Report](https://research.google/pubs/dora-accelerate-state-of-devops-2024-report/)
- [x] [Frontiers in Computer Science (2026) Platform engineering and internal developer portals: a multivocal literature review](https://www.frontiersin.org/journals/computer-science/articles/10.3389/fcomp.2026.1814498/full)
- [x] [Avgeriou et al. (2024) Technical Debt Management: The Road Ahead for Successful Software Delivery](https://arxiv.org/html/2403.06484v1)
- [x] [Deloitte (2026) Measuring technical debt and latent potential](https://www.deloitte.com/us/en/insights/topics/technology-management/technical-debt-impact.html)
- [x] [Nagappan and Ball (2005) Use of Relative Code Churn Measures to Predict System Defect Density](https://www.microsoft.com/en-us/research/publication/use-of-relative-code-churn-measures-to-predict-system-defect-density/)
- [x] [Mitchell (2026) What is "backpressure" in the Theory of Constraints?](https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-01-backpressure-theory-of-constraints.md)
- [x] [Mitchell (2026) The measurement asymmetry: why we cut costs but can't see lost opportunities](https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-26-measuring-opportunity-cost.md)
- [x] [Mitchell (2026) What is the strongest evidence-based argument that investing in software engineering capability rather than citizen development tooling is the correct response to systems capability debt?](https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-26-software-engineering-investment-case-llm.md)
- [x] [Mitchell (2026) What metrics beyond code acceptance rates best capture net organisational value when Artificial Intelligence (AI) coding tools are adopted with productivity mandates?](https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-08-productivity-incentive-metrics-quality-review-agentic-ai.md)

---

## Research Skill Output

*(Full output from running the research skill, retained verbatim in the completed item. Sections 0-5 are the investigation; Section 6 seeds the Findings section below.)*

### §0 Initialise

- Question: Given constrained engineering capacity, when should an organisation keep allocating attention to new features and when should it spend that attention on improving tooling, process, architecture, and quality controls?
- Scope: flow models, quality-throughput interaction, capability-building investment models, Pareto-style concentration, and practical decision triggers.
- Constraints: distinguish conceptual models from empirical evidence; prefer observable metrics; expand acronyms on first use.
- Output format: structured synthesis with Executive Summary, Key Findings, Evidence Map, Assumptions, Analysis, Risks, Open Questions, and Output.
- [assumption; source: https://dora.dev/research/2025/measurement-frameworks/; https://econpapers.repec.org/RePEc:inm:oropre:v:9:y:1961:i:3:p:383-387] The most decision-useful answer will be a trigger-based allocation rule, not a universal fixed percentage split, because the available evidence mostly describes mechanisms and operating indicators rather than one stable optimal ratio.

### §1 Question Decomposition

1. Flow and bottlenecks
   1. What does Theory of Constraints (TOC) say about where improvement work creates the most throughput?
   2. What does Little's Law imply about Work in Progress (WIP), cycle time, and overloaded delivery systems?
2. Quality and rework
   1. How does technical debt convert short-term feature speed into later rework or lower velocity?
   2. When does quality work become throughput work rather than "overhead"?
3. Capability-building investment
   1. What do DevOps Research and Assessment (DORA) metrics imply about speed-versus-stability tradeoffs?
   2. What does Site Reliability Engineering (SRE) toil guidance imply about when to automate or improve the system?
   3. What does platform engineering literature imply about internal capability investment, implementation order, and payback shape?
4. Pareto lens
   1. Where do concentration effects appear in software systems?
   2. How should concentration change allocation strategy?
5. Decision synthesis
   1. What indicators should trigger a shift from build to improve?
   2. What rival allocation heuristics should be rejected or qualified?

### §2 Investigation

Access note: Routledge, Celeritas, and IT Revolution landing pages inspected; purchase-page surfaces only; not used as evidence.

Access note: seeded Organisation for Economic Co-operation and Development (OECD) glossary URL returned 404; replaced in Sources with accessible academic or official material on the Pareto principle and defect concentration.

#### A. Flow and bottlenecks

- [fact; source: https://en.wikipedia.org/wiki/Theory_of_constraints; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-01-backpressure-theory-of-constraints.md] Theory of Constraints holds that every manageable system has at least one constraint, and only by increasing flow through that constraint can overall throughput increase.
- [fact; source: https://en.wikipedia.org/wiki/Theory_of_constraints] The five focusing steps are identify the constraint, exploit it, subordinate everything else to it, elevate it, and then repeat once the constraint moves.
- [fact; source: https://econpapers.repec.org/RePEc:inm:oropre:v:9:y:1961:i:3:p:383-387] Little's Law states that in a stationary queuing process the average number of units in the system equals the arrival rate multiplied by the average time a unit spends in the system.
- [inference; source: https://econpapers.repec.org/RePEc:inm:oropre:v:9:y:1961:i:3:p:383-387; https://en.wikipedia.org/wiki/Theory_of_constraints; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-01-backpressure-theory-of-constraints.md] In software delivery terms, pushing more feature work into an already loaded system raises WIP and lead time before it raises completed value, so local utilisation gains can reduce whole-system throughput.

#### B. Quality, rework, and debt

- [fact; source: https://arxiv.org/html/2403.06484v1] Technical Debt is commonly created under time pressure, insufficient funding, limited engineering resources, or large feature complexity, and unmanaged debt leads to reduced team velocity, harder maintenance, and frequent unexpected rework.
- [fact; source: https://www.deloitte.com/us/en/insights/topics/technology-management/technical-debt-impact.html] Deloitte's 2026 Global Technology Leadership Study estimates that technical debt accounts for 21% to 40% of an organisation's information-technology spending, which is a large enough burden to treat debt service as a capacity problem rather than as a cosmetic code-quality issue.
- [inference; source: https://arxiv.org/html/2403.06484v1; https://www.deloitte.com/us/en/insights/topics/technology-management/technical-debt-impact.html; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-26-measuring-opportunity-cost.md] When rework and debt service are materially consuming engineering attention, improvement work that removes debt can have higher long-run throughput return than shipping the next marginal feature.

#### C. Throughput, instability, and toil

- [fact; source: https://dora.dev/guides/dora-metrics/] DORA measures software delivery performance through throughput metrics, change lead time, deployment frequency, failed deployment recovery time, and instability metrics, change fail rate and deployment rework rate.
- [fact; source: https://dora.dev/guides/dora-metrics/] DORA states that speed and stability are not long-run tradeoffs for top performers; high performers do well across all five metrics while low performers do poorly across them.
- [fact; source: https://sre.google/workbook/eliminating-toil/] Google limits SRE teams to 50% operational work and defines toil as repetitive, automatable, low-enduring-value work whose growth can consume the team if left unchecked.
- [fact; source: https://sre.google/workbook/eliminating-toil/] The SRE workbook explicitly recommends quantifying toil, comparing time saved against time invested, and prioritising toil-reduction projects to maximise return on engineering investment.
- [inference; source: https://dora.dev/guides/dora-metrics/; https://sre.google/workbook/eliminating-toil/] Once operational load, recovery work, or review overhead is large enough to degrade throughput or instability metrics, system-improvement work is not optional overhead but the work required to restore delivery capacity.

#### D. Capability-building investment

- [fact; source: https://dora.dev/capabilities/platform-engineering/; https://research.google/pubs/dora-accelerate-state-of-devops-2024-report/] DORA describes platform engineering as a sociotechnical discipline that abstracts complexity through repeatable, secure, self-service workflows and identifies it as a key capability in high-performing organisations.
- [fact; source: https://dora.dev/capabilities/platform-engineering/] DORA also states that platform engineering often follows a J-curve, meaning organisations can see an initial dip before recovering at a higher level of performance as the platform matures.
- [fact; source: https://dora.dev/capabilities/platform-engineering/] DORA recommends starting with a minimum viable platform, focusing on the most common workflow, and giving clear feedback rather than attempting a comprehensive platform build all at once.
- [fact; source: https://www.frontiersin.org/journals/computer-science/articles/10.3389/fcomp.2026.1814498/full] The 2026 multivocal literature review concludes that evidence supports treating platforms as products, combining delivery metrics with developer-experience measures, and designing golden paths as enablers rather than mandates.
- [inference; source: https://dora.dev/capabilities/platform-engineering/; https://www.frontiersin.org/journals/computer-science/articles/10.3389/fcomp.2026.1814498/full; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-26-software-engineering-investment-case-llm.md] Capability-building investment is most defensible when it removes recurring friction from the dominant workflow, because that is where platform quality compounds across many future feature deliveries.

#### E. Pareto concentration and hotspots

- [fact; source: https://en.wikipedia.org/wiki/Pareto_principle] The Pareto principle is the claim that many outcomes are driven by a minority of causes, commonly summarised as roughly 80% of consequences coming from 20% of causes.
- [fact; source: https://www.microsoft.com/en-us/research/publication/use-of-relative-code-churn-measures-to-predict-system-defect-density/] Nagappan and Ball show that relative code churn is highly predictive of defect density and can distinguish fault-prone from not-fault-prone binaries with 89.0% accuracy in a Windows Server 2003 case study.
- [inference; source: https://en.wikipedia.org/wiki/Pareto_principle; https://www.microsoft.com/en-us/research/publication/use-of-relative-code-churn-measures-to-predict-system-defect-density/] In practical allocation terms, Pareto framing means improvement work should target the hot spots, queues, and repetitive operational pain points that dominate delay or defect escape rather than being spread evenly across the estate.

#### F. Cross-item continuity

- [fact; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-01-backpressure-theory-of-constraints.md] The repository's earlier backpressure item already established that Drum-Buffer-Rope work release is the operational TOC mechanism for preventing upstream overload of a downstream constraint.
- [fact; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-26-measuring-opportunity-cost.md] The repository's earlier opportunity-cost item established that organisations systematically overweight visible short-term savings and underweight harder-to-measure long-term value.
- [inference; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-01-backpressure-theory-of-constraints.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-26-measuring-opportunity-cost.md] Taken together with the external evidence above, prior completed items support a decision rule in which build-versus-improve is governed by bottleneck relief and hidden-cost reduction rather than by fixed feature quotas.

### §3 Reasoning

- [inference; source: https://econpapers.repec.org/RePEc:inm:oropre:v:9:y:1961:i:3:p:383-387; https://en.wikipedia.org/wiki/Theory_of_constraints; https://dora.dev/guides/dora-metrics/] The strongest synthesis is that build-versus-improve is a dynamic constraint-management choice, not a stable ratio choice, because queues, bottlenecks, and instability move over time.
- [inference; source: https://arxiv.org/html/2403.06484v1; https://sre.google/workbook/eliminating-toil/; https://dora.dev/guides/dora-metrics/] Quality work becomes throughput work once debt, toil, rework, or recovery burden materially slows the main delivery path.
- [inference; source: https://en.wikipedia.org/wiki/Pareto_principle; https://www.microsoft.com/en-us/research/publication/use-of-relative-code-churn-measures-to-predict-system-defect-density/] Pareto framing does not justify generic "improvement time"; it justifies concentrated intervention on the small number of modules, queues, or workflows producing most delay, defects, or operating pain.
- [assumption; source: https://dora.dev/research/2025/measurement-frameworks/; https://dora.dev/guides/dora-metrics/] The organisation can observe at least basic proxies for WIP, lead time, failure, recovery, and toil; without those signals, any allocation rule falls back to managerial intuition.

### §4 Consistency Check

- [fact; source: https://dora.dev/guides/dora-metrics/] There is no contradiction between "improve the system" and "ship faster" when the improvement attacks the current throughput or instability bottleneck, because DORA's evidence says top performers improve both speed and stability together.
- [fact; source: https://dora.dev/capabilities/platform-engineering/] Platform investment should not be sold as instant payoff, because DORA explicitly warns that platform engineering can follow a J-curve with temporary disruption before later gains.
- [inference; source: https://arxiv.org/html/2403.06484v1; https://sre.google/workbook/eliminating-toil/] Not every improvement project deserves priority; the models only support improvement-first allocation when the chosen work is tightly coupled to the current constraint, hotspot, or repetitive operational drag.
- [inference; source: https://econpapers.repec.org/RePEc:inm:oropre:v:9:y:1961:i:3:p:383-387; https://www.microsoft.com/en-us/research/publication/use-of-relative-code-churn-measures-to-predict-system-defect-density/] The absence of a universal percentage split is not a gap in logic; it follows from the evidence that queue pressure and hotspot concentration vary across systems and over time.

### §5 Depth and Breadth Expansion

- [fact; source: https://econpapers.repec.org/RePEc:inm:oropre:v:9:y:1961:i:3:p:383-387; https://en.wikipedia.org/wiki/Theory_of_constraints] Technical lens: the direct control variables are queue size, bottleneck capacity, and release discipline, not total developer busyness.
- [inference; source: https://arxiv.org/html/2403.06484v1; https://www.deloitte.com/us/en/insights/topics/technology-management/technical-debt-impact.html; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-26-measuring-opportunity-cost.md] Economic lens: the core tradeoff is intertemporal, because feature-first shortcuts book visible short-term gains while pushing hidden maintenance cost and slower future throughput into later periods.
- [inference; source: https://sre.google/workbook/eliminating-toil/; https://dora.dev/research/2025/measurement-frameworks/; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-26-measuring-opportunity-cost.md] Behavioural lens: organisations systematically underinvest in system work because repetitive operational pain, prevented incidents, and avoided queue growth are less visible than shipped features or cost cuts.
- [inference; source: https://dora.dev/capabilities/platform-engineering/; https://www.frontiersin.org/journals/computer-science/articles/10.3389/fcomp.2026.1814498/full; https://sre.google/workbook/eliminating-toil/] Organisational lens: dedicated platform and reliability disciplines are institutional mechanisms for protecting improvement capacity from being consumed by near-term delivery pressure.

### §6 Synthesis

**Executive summary:**

Organisations should allocate build-versus-improve effort by following the current bottleneck, not by holding a fixed percentage split, because Theory of Constraints and Little's Law both imply that overloaded systems convert extra feature intake into more queue length and longer lead time before they convert it into shipped value. [inference; source: https://en.wikipedia.org/wiki/Theory_of_constraints; https://econpapers.repec.org/RePEc:inm:oropre:v:9:y:1961:i:3:p:383-387; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-01-backpressure-theory-of-constraints.md]

System-improvement work becomes throughput work once debt, toil, rework, or unstable deployment pipelines are the binding constraint, because those frictions tax every subsequent feature and reduce the amount of delivered value per unit of engineering effort. [inference; source: https://arxiv.org/html/2403.06484v1; https://sre.google/workbook/eliminating-toil/; https://dora.dev/guides/dora-metrics/]

DORA and platform-engineering evidence qualify the supposed speed-versus-quality tradeoff: the best long-run outcome is not "more features now" versus "better system later," but better software faster through targeted improvements to the delivery system. [inference; source: https://dora.dev/guides/dora-metrics/; https://dora.dev/capabilities/platform-engineering/; https://research.google/pubs/dora-accelerate-state-of-devops-2024-report/]

Pareto-style concentration changes the recommendation from generic improvement time to hotspot-focused intervention, because a minority of modules, workflows, or queues usually dominate defect risk, review load, or delivery delay. [inference; source: https://en.wikipedia.org/wiki/Pareto_principle; https://www.microsoft.com/en-us/research/publication/use-of-relative-code-churn-measures-to-predict-system-defect-density/]

**Key findings:**

1. **The strongest theoretical rule is to allocate scarce capacity to the current bottleneck rather than to preserve a fixed build-versus-improve ratio, because Theory of Constraints predicts that improving non-constraints yields little system-wide throughput gain while relieving the binding constraint changes total output.** ([inference]; medium confidence; source: https://en.wikipedia.org/wiki/Theory_of_constraints; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-01-backpressure-theory-of-constraints.md)
2. **Little's Law implies that when feature demand pushes more work into a delivery system than the system can complete, Work in Progress rises and lead time lengthens, so apparent short-term busyness can reduce throughput and predictability rather than increase them.** ([inference]; high confidence; source: https://econpapers.repec.org/RePEc:inm:oropre:v:9:y:1961:i:3:p:383-387; https://dora.dev/guides/dora-metrics/)
3. **Technical debt converts some short-term feature speed into later drag, because shortcuts taken under time or resource pressure create harder maintenance, reduced velocity, and unexpected rework that consume future engineering capacity.** ([fact]; medium confidence; source: https://arxiv.org/html/2403.06484v1; https://www.deloitte.com/us/en/insights/topics/technology-management/technical-debt-impact.html)
4. **The best public delivery evidence does not support a permanent tradeoff between speed and quality, because DORA finds that top-performing teams achieve both higher throughput and lower instability when they improve testing, deployment, and feedback systems.** ([fact]; high confidence; source: https://dora.dev/guides/dora-metrics/; https://research.google/pubs/dora-accelerate-state-of-devops-2024-report/)
5. **Once repetitive operational work becomes a large enough share of team attention, improvement work should displace marginal feature work, because Site Reliability Engineering guidance treats toil reduction and automation as return-on-investment decisions required to protect engineering capacity.** ([inference]; high confidence; source: https://sre.google/workbook/eliminating-toil/)
6. **Pareto-style concentration means improvement investment should be targeted at hot spots rather than spread uniformly, because a minority of modules or workflows often drive most defect risk or delivery friction and therefore offer the highest leverage for capacity recovery.** ([inference]; medium confidence; source: https://en.wikipedia.org/wiki/Pareto_principle; https://www.microsoft.com/en-us/research/publication/use-of-relative-code-churn-measures-to-predict-system-defect-density/)
7. **Platform engineering is a valid form of throughput-improvement investment when it builds high-quality self-service golden paths for common workflows, but the evidence also says it should be introduced incrementally because the payback can follow a J-curve rather than an immediate straight line.** ([fact]; medium confidence; source: https://dora.dev/capabilities/platform-engineering/; https://www.frontiersin.org/journals/computer-science/articles/10.3389/fcomp.2026.1814498/full)
8. **The most practical allocation policy is trigger-based: keep feature delivery primary while lead time, failure, recovery, toil share, and hotspot concentration stay within agreed bands, then shift capacity toward improvement when those indicators worsen persistently.** ([inference]; medium confidence; source: https://dora.dev/guides/dora-metrics/; https://sre.google/workbook/eliminating-toil/; https://www.microsoft.com/en-us/research/publication/use-of-relative-code-churn-measures-to-predict-system-defect-density/)

**Evidence map:**

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [inference] Follow the current bottleneck, not a fixed ratio. | https://en.wikipedia.org/wiki/Theory_of_constraints ; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-01-backpressure-theory-of-constraints.md | medium | constraint-governed allocation |
| [inference] Excess Work in Progress increases lead time and reduces predictability. | https://econpapers.repec.org/RePEc:inm:oropre:v:9:y:1961:i:3:p:383-387 ; https://dora.dev/guides/dora-metrics/ | high | queue pressure |
| [fact] Technical debt creates reduced velocity and unexpected rework. | https://arxiv.org/html/2403.06484v1 ; https://www.deloitte.com/us/en/insights/topics/technology-management/technical-debt-impact.html | medium | debt as capacity tax |
| [fact] High performers do not trade speed for stability in the long run. | https://dora.dev/guides/dora-metrics/ ; https://research.google/pubs/dora-accelerate-state-of-devops-2024-report/ | high | throughput plus instability |
| [inference] Toil-heavy systems should shift capacity into automation and system improvement. | https://sre.google/workbook/eliminating-toil/ | high | toil cap and return logic |
| [inference] Pareto concentration makes hotspot-focused improvement higher leverage than uniform improvement. | https://en.wikipedia.org/wiki/Pareto_principle ; https://www.microsoft.com/en-us/research/publication/use-of-relative-code-churn-measures-to-predict-system-defect-density/ | medium | vital-few targeting |
| [fact] Platform engineering should start with common workflows and may show J-curve payback. | https://dora.dev/capabilities/platform-engineering/ ; https://www.frontiersin.org/journals/computer-science/articles/10.3389/fcomp.2026.1814498/full | medium | incremental rollout |
| [inference] A trigger-based policy is more defensible than a universal percentage split. | https://dora.dev/guides/dora-metrics/ ; https://sre.google/workbook/eliminating-toil/ ; https://www.microsoft.com/en-us/research/publication/use-of-relative-code-churn-measures-to-predict-system-defect-density/ | medium | metric-governed shift |

**Assumptions:**

- [assumption; source: https://dora.dev/research/2025/measurement-frameworks/; https://dora.dev/guides/dora-metrics/] The organisation can measure at least basic flow and instability indicators, because the synthesis depends on observable triggers rather than on a purely narrative notion of "the system feels slow."
- [assumption; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-26-measuring-opportunity-cost.md; https://arxiv.org/html/2403.06484v1] Demand for additional feature work is real enough that pausing it has an opportunity cost, because otherwise the build-versus-improve choice collapses into a pure maintenance problem.

**Analysis:**

The evidence base is stronger on mechanisms than on exact percentages, so the synthesis weights causal models and operating indicators above any fixed ratio heuristic. [fact; source: https://econpapers.repec.org/RePEc:inm:oropre:v:9:y:1961:i:3:p:383-387; https://dora.dev/guides/dora-metrics/; https://sre.google/workbook/eliminating-toil/]

The decisive combination is Little's Law plus Theory of Constraints: one explains why overloaded systems get slower as queues grow, and the other explains why only the bottleneck matters for throughput improvement. [inference; source: https://econpapers.repec.org/RePEc:inm:oropre:v:9:y:1961:i:3:p:383-387; https://en.wikipedia.org/wiki/Theory_of_constraints]

Technical debt and toil matter because they turn invisible system frictions into recurring taxes on every later change, which means improvement work can have higher marginal value than the next feature once those taxes become the dominant constraint. [inference; source: https://arxiv.org/html/2403.06484v1; https://sre.google/workbook/eliminating-toil/; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-26-measuring-opportunity-cost.md]

The strongest rival remedy is to preserve feature delivery and solve delay by adding people or by mandating more output, but the flow literature does not support that when the real constraint is queueing, defect hot spots, or unstable operating paths rather than headcount alone. [inference; source: https://en.wikipedia.org/wiki/Theory_of_constraints; https://econpapers.repec.org/RePEc:inm:oropre:v:9:y:1961:i:3:p:383-387; https://www.microsoft.com/en-us/research/publication/use-of-relative-code-churn-measures-to-predict-system-defect-density/]

**Risks, gaps, uncertainties:**

- [fact; source: https://econpapers.repec.org/RePEc:inm:oropre:v:9:y:1961:i:3:p:383-387; https://en.wikipedia.org/wiki/Theory_of_constraints] Flow models explain direction and mechanism well, but they do not yield a universally valid percentage split between feature work and system improvement.
- [fact; source: https://www.frontiersin.org/journals/computer-science/articles/10.3389/fcomp.2026.1814498/full; https://dora.dev/capabilities/platform-engineering/] Platform-engineering evidence is useful and increasingly structured, but academic causal evidence on exact payback remains thinner than practitioner guidance.
- [fact; source: https://www.deloitte.com/us/en/insights/topics/technology-management/technical-debt-impact.html; https://arxiv.org/html/2403.06484v1] Technical debt cost magnitudes are partly survey-based and model-based, so precise burden estimates are less robust than the general claim that debt creates rework and slower future delivery.
- [inference; source: https://sre.google/workbook/eliminating-toil/; https://dora.dev/research/2025/measurement-frameworks/] Organisations with poor measurement may still know they are overloaded, but the trigger-based policy becomes noisier when toil, lead time, and recovery data are not instrumented well.

**Open questions:**

- [inference; source: https://dora.dev/guides/dora-metrics/; https://sre.google/workbook/eliminating-toil/] Which numeric trigger bands, for example toil share or recovery-time thresholds, are most predictive of when improvement work should temporarily dominate feature work in different operating environments?
- [inference; source: https://dora.dev/capabilities/platform-engineering/; https://www.frontiersin.org/journals/computer-science/articles/10.3389/fcomp.2026.1814498/full] What is the strongest before-and-after evidence for platform engineering payback outside vendor or survey claims, especially in legacy-heavy enterprises?
- [inference; source: https://www.microsoft.com/en-us/research/publication/use-of-relative-code-churn-measures-to-predict-system-defect-density/; https://en.wikipedia.org/wiki/Pareto_principle] Which hotspot indicators, churn, incidents, rework, or review delay, are most reliable for selecting the vital few improvement targets in different codebases?

### §7 Recursive Review

- Acronym audit: completed.
- Claim-label sweep in Research Skill Output: completed.
- Findings parity target established: Findings mirrors Section 6 claims, confidence, and sources.
- Companion-item cross-reference sweep: completed.
- Source-URL sweep: completed.
- Em-dash sweep: completed.

---

## Findings

*(Populated from §6 Synthesis above.)*

### Executive Summary

Organisations should allocate build-versus-improve effort by following the current bottleneck, not by holding a fixed percentage split, because Theory of Constraints and Little's Law both imply that overloaded systems convert extra feature intake into more queue length and longer lead time before they convert it into shipped value. [inference; source: https://en.wikipedia.org/wiki/Theory_of_constraints; https://econpapers.repec.org/RePEc:inm:oropre:v:9:y:1961:i:3:p:383-387; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-01-backpressure-theory-of-constraints.md]

System-improvement work becomes throughput work once debt, toil, rework, or unstable deployment pipelines are the binding constraint, because those frictions tax every subsequent feature and reduce the amount of delivered value per unit of engineering effort. [inference; source: https://arxiv.org/html/2403.06484v1; https://sre.google/workbook/eliminating-toil/; https://dora.dev/guides/dora-metrics/]

DORA and platform-engineering evidence qualify the supposed speed-versus-quality tradeoff: the best long-run outcome is not "more features now" versus "better system later," but better software faster through targeted improvements to the delivery system. [inference; source: https://dora.dev/guides/dora-metrics/; https://dora.dev/capabilities/platform-engineering/; https://research.google/pubs/dora-accelerate-state-of-devops-2024-report/]

Pareto-style concentration changes the recommendation from generic improvement time to hotspot-focused intervention, because a minority of modules, workflows, or queues usually dominate defect risk, review load, or delivery delay. [inference; source: https://en.wikipedia.org/wiki/Pareto_principle; https://www.microsoft.com/en-us/research/publication/use-of-relative-code-churn-measures-to-predict-system-defect-density/]

### Key Findings

1. **The strongest theoretical rule is to allocate scarce capacity to the current bottleneck rather than to preserve a fixed build-versus-improve ratio, because Theory of Constraints predicts that improving non-constraints yields little system-wide throughput gain while relieving the binding constraint changes total output.** ([inference]; medium confidence; source: https://en.wikipedia.org/wiki/Theory_of_constraints; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-01-backpressure-theory-of-constraints.md)
2. **Little's Law implies that when feature demand pushes more work into a delivery system than the system can complete, Work in Progress rises and lead time lengthens, so apparent short-term busyness can reduce throughput and predictability rather than increase them.** ([inference]; high confidence; source: https://econpapers.repec.org/RePEc:inm:oropre:v:9:y:1961:i:3:p:383-387; https://dora.dev/guides/dora-metrics/)
3. **Technical debt converts some short-term feature speed into later drag, because shortcuts taken under time or resource pressure create harder maintenance, reduced velocity, and unexpected rework that consume future engineering capacity.** ([fact]; medium confidence; source: https://arxiv.org/html/2403.06484v1; https://www.deloitte.com/us/en/insights/topics/technology-management/technical-debt-impact.html)
4. **The best public delivery evidence does not support a permanent tradeoff between speed and quality, because DORA finds that top-performing teams achieve both higher throughput and lower instability when they improve testing, deployment, and feedback systems.** ([fact]; high confidence; source: https://dora.dev/guides/dora-metrics/; https://research.google/pubs/dora-accelerate-state-of-devops-2024-report/)
5. **Once repetitive operational work becomes a large enough share of team attention, improvement work should displace marginal feature work, because Site Reliability Engineering guidance treats toil reduction and automation as return-on-investment decisions required to protect engineering capacity.** ([inference]; high confidence; source: https://sre.google/workbook/eliminating-toil/)
6. **Pareto-style concentration means improvement investment should be targeted at hot spots rather than spread uniformly, because a minority of modules or workflows often drive most defect risk or delivery friction and therefore offer the highest leverage for capacity recovery.** ([inference]; medium confidence; source: https://en.wikipedia.org/wiki/Pareto_principle; https://www.microsoft.com/en-us/research/publication/use-of-relative-code-churn-measures-to-predict-system-defect-density/)
7. **Platform engineering is a valid form of throughput-improvement investment when it builds high-quality self-service golden paths for common workflows, but the evidence also says it should be introduced incrementally because the payback can follow a J-curve rather than an immediate straight line.** ([fact]; medium confidence; source: https://dora.dev/capabilities/platform-engineering/; https://www.frontiersin.org/journals/computer-science/articles/10.3389/fcomp.2026.1814498/full)
8. **The most practical allocation policy is trigger-based: keep feature delivery primary while lead time, failure, recovery, toil share, and hotspot concentration stay within agreed bands, then shift capacity toward improvement when those indicators worsen persistently.** ([inference]; medium confidence; source: https://dora.dev/guides/dora-metrics/; https://sre.google/workbook/eliminating-toil/; https://www.microsoft.com/en-us/research/publication/use-of-relative-code-churn-measures-to-predict-system-defect-density/)

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [inference] Follow the current bottleneck, not a fixed ratio. | https://en.wikipedia.org/wiki/Theory_of_constraints ; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-01-backpressure-theory-of-constraints.md | medium | constraint-governed allocation |
| [inference] Excess Work in Progress increases lead time and reduces predictability. | https://econpapers.repec.org/RePEc:inm:oropre:v:9:y:1961:i:3:p:383-387 ; https://dora.dev/guides/dora-metrics/ | high | queue pressure |
| [fact] Technical debt creates reduced velocity and unexpected rework. | https://arxiv.org/html/2403.06484v1 ; https://www.deloitte.com/us/en/insights/topics/technology-management/technical-debt-impact.html | medium | debt as capacity tax |
| [fact] High performers do not trade speed for stability in the long run. | https://dora.dev/guides/dora-metrics/ ; https://research.google/pubs/dora-accelerate-state-of-devops-2024-report/ | high | throughput plus instability |
| [inference] Toil-heavy systems should shift capacity into automation and system improvement. | https://sre.google/workbook/eliminating-toil/ | high | toil cap and return logic |
| [inference] Pareto concentration makes hotspot-focused improvement higher leverage than uniform improvement. | https://en.wikipedia.org/wiki/Pareto_principle ; https://www.microsoft.com/en-us/research/publication/use-of-relative-code-churn-measures-to-predict-system-defect-density/ | medium | vital-few targeting |
| [fact] Platform engineering should start with common workflows and may show J-curve payback. | https://dora.dev/capabilities/platform-engineering/ ; https://www.frontiersin.org/journals/computer-science/articles/10.3389/fcomp.2026.1814498/full | medium | incremental rollout |
| [inference] A trigger-based policy is more defensible than a universal percentage split. | https://dora.dev/guides/dora-metrics/ ; https://sre.google/workbook/eliminating-toil/ ; https://www.microsoft.com/en-us/research/publication/use-of-relative-code-churn-measures-to-predict-system-defect-density/ | medium | metric-governed shift |

### Assumptions

- [assumption; source: https://dora.dev/research/2025/measurement-frameworks/; https://dora.dev/guides/dora-metrics/] The organisation can measure at least basic flow and instability indicators, because the synthesis depends on observable triggers rather than on a purely narrative notion of "the system feels slow."
- [assumption; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-26-measuring-opportunity-cost.md; https://arxiv.org/html/2403.06484v1] Demand for additional feature work is real enough that pausing it has an opportunity cost, because otherwise the build-versus-improve choice collapses into a pure maintenance problem.

### Analysis

The evidence base is stronger on mechanisms than on exact percentages, so the synthesis weights causal models and operating indicators above any fixed ratio heuristic. [fact; source: https://econpapers.repec.org/RePEc:inm:oropre:v:9:y:1961:i:3:p:383-387; https://dora.dev/guides/dora-metrics/; https://sre.google/workbook/eliminating-toil/]

The decisive combination is Little's Law plus Theory of Constraints: one explains why overloaded systems get slower as queues grow, and the other explains why only the bottleneck matters for throughput improvement. [inference; source: https://econpapers.repec.org/RePEc:inm:oropre:v:9:y:1961:i:3:p:383-387; https://en.wikipedia.org/wiki/Theory_of_constraints]

Technical debt and toil matter because they turn invisible system frictions into recurring taxes on every later change, which means improvement work can have higher marginal value than the next feature once those taxes become the dominant constraint. [inference; source: https://arxiv.org/html/2403.06484v1; https://sre.google/workbook/eliminating-toil/; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-26-measuring-opportunity-cost.md]

The strongest rival remedy is to preserve feature delivery and solve delay by adding people or by mandating more output, but the flow literature does not support that when the real constraint is queueing, defect hot spots, or unstable operating paths rather than headcount alone. [inference; source: https://en.wikipedia.org/wiki/Theory_of_constraints; https://econpapers.repec.org/RePEc:inm:oropre:v:9:y:1961:i:3:p:383-387; https://www.microsoft.com/en-us/research/publication/use-of-relative-code-churn-measures-to-predict-system-defect-density/]

### Risks, Gaps, and Uncertainties

- [fact; source: https://econpapers.repec.org/RePEc:inm:oropre:v:9:y:1961:i:3:p:383-387; https://en.wikipedia.org/wiki/Theory_of_constraints] Flow models explain direction and mechanism well, but they do not yield a universally valid percentage split between feature work and system improvement.
- [fact; source: https://www.frontiersin.org/journals/computer-science/articles/10.3389/fcomp.2026.1814498/full; https://dora.dev/capabilities/platform-engineering/] Platform-engineering evidence is useful and increasingly structured, but academic causal evidence on exact payback remains thinner than practitioner guidance.
- [fact; source: https://www.deloitte.com/us/en/insights/topics/technology-management/technical-debt-impact.html; https://arxiv.org/html/2403.06484v1] Technical debt cost magnitudes are partly survey-based and model-based, so precise burden estimates are less robust than the general claim that debt creates rework and slower future delivery.
- [inference; source: https://sre.google/workbook/eliminating-toil/; https://dora.dev/research/2025/measurement-frameworks/] Organisations with poor measurement may still know they are overloaded, but the trigger-based policy becomes noisier when toil, lead time, and recovery data are not instrumented well.

### Open Questions

- [inference; source: https://dora.dev/guides/dora-metrics/; https://sre.google/workbook/eliminating-toil/] Which numeric trigger bands, for example toil share or recovery-time thresholds, are most predictive of when improvement work should temporarily dominate feature work in different operating environments?
- [inference; source: https://dora.dev/capabilities/platform-engineering/; https://www.frontiersin.org/journals/computer-science/articles/10.3389/fcomp.2026.1814498/full] What is the strongest before-and-after evidence for platform engineering payback outside vendor or survey claims, especially in legacy-heavy enterprises?
- [inference; source: https://www.microsoft.com/en-us/research/publication/use-of-relative-code-churn-measures-to-predict-system-defect-density/; https://en.wikipedia.org/wiki/Pareto_principle] Which hotspot indicators, churn, incidents, rework, or review delay, are most reliable for selecting the vital few improvement targets in different codebases?

---

## Output

*(Filled in on completion.)*

- Type: knowledge
- Description: A trigger-based allocation framework for deciding when feature delivery should yield to system-improvement work, grounded in queueing, bottleneck, toil, technical-debt, and hotspot-concentration evidence. [inference; source: https://econpapers.repec.org/RePEc:inm:oropre:v:9:y:1961:i:3:p:383-387; https://sre.google/workbook/eliminating-toil/; https://dora.dev/guides/dora-metrics/]
- Links:
  - [Little (1961) A Proof for the Queuing Formula: L = (lambda) W](https://econpapers.repec.org/RePEc:inm:oropre:v:9:y:1961:i:3:p:383-387)
  - [DevOps Research and Assessment (DORA) Metrics Guide](https://dora.dev/guides/dora-metrics/)
  - [Google Site Reliability Engineering (SRE) Workbook: Eliminating Toil](https://sre.google/workbook/eliminating-toil/)
