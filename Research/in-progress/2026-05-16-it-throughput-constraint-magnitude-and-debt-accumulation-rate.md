---
title: "IT Throughput Constraint Magnitude and Debt Accumulation Rate"
added: 2026-05-16T05:29:48+00:00
status: reviewing
priority: high
blocks: []
tags: [organisation, workflow, evaluation, agentic-coding]
started: 2026-05-16T08:10:47+00:00
completed: ~
output: [knowledge]
cites: [2026-04-26-systems-capability-debt-citizen-development-empirical-evidence, 2026-04-26-software-engineering-investment-case-llm, 2026-05-14-citizen-development-rollout-empirical-evidence, 2026-05-14-org-failure-modes-cohort-demand-domain-it]
related: [2026-04-22-enterprise-ai-use-case-routing-frameworks, 2026-04-26-ai-lowcode-risk-tier-classification-controls, 2026-04-26-systems-capability-debt-agentic-ai-risk-synthesis]
superseded_by: ~
supersedes: ~
item_type: primary
confidence: medium
versions: []
---

# IT Throughput Constraint Magnitude and Debt Accumulation Rate

## Research Question

What is the empirical relationship between Information Technology (IT) throughput capacity and the rate at which gaps between operational need and delivered system capability accumulate across comparable organisations, and what proportion of workaround automation demand now handled outside central engineering can realistically be absorbed into centrally governed software delivery within three years under realistic Artificial Intelligence (AI)-assisted productivity assumptions?

## Scope

**In scope:**
- Evidence on throughput, coordination bottlenecks, queueing, and workaround demand or shadow Information Technology (IT) demand in large organisations.
- Classification of workaround automation demand into demand that centrally governed software delivery can absorb versus demand that remains structurally resistant.
- Sensitivity analysis over defensible AI-assisted software delivery productivity ranges.
- Adjacent completed repository items that materially sharpen the demand, governance, and delivery-side interpretation.

**Out of scope:**
- Building an enterprise-specific forecasting model.
- Claiming a universal cross-sector coefficient for debt accumulation where no public dataset supports one.
- Vendor-specific product recommendations.

**Constraints:**
- Prefer primary or near-primary public sources, peer-reviewed studies, and official research programs.
- Keep all assumptions explicit and sensitivity-tested.
- Treat public evidence gaps as findings, not as permission to infer a precise elasticity.

## Context

The decision problem is whether central engineering throughput is merely one constraint among many, or whether it is the dominant rate-limiter that turns unmet operational demand into shadow tools, citizen development, and a growing stock of local workaround automations. [inference; source: https://link.springer.com/article/10.1007/s10257-020-00472-6; https://doi.org/10.5755/j01.itc.49.1.23801; https://davidamitchell.github.io/Research/research/2026-04-26-systems-capability-debt-citizen-development-empirical-evidence.html]

This item matters because AI assistance can raise local coding speed, but the investment decision depends on whether that increase is large enough, and aligned enough with the actual demand mix, to materially shrink the current stock of workaround automations, shadow tools, and business-managed solutions within a planning horizon of three years. [inference; source: https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report; https://arxiv.org/abs/2302.06590; https://arxiv.org/abs/2507.09089; https://davidamitchell.github.io/Research/research/2026-04-26-software-engineering-investment-case-llm.html]

## Approach

1. Establish the best-supported directional relationship between central delivery throughput, cross-team coordination cost, and workaround demand or shadow Information Technology (IT) demand.
2. Separate workaround demand into categories that are software-closeable, meaning stable and economically automatable, versus categories that remain resistant because they are exception-heavy, unstable, under-governed, or still depend on human judgement and organisational redesign.
3. Bracket realistic AI-assisted throughput gains using a mix of controlled experiments, real-world randomized controlled trial evidence, and DevOps Research and Assessment (DORA) system-level findings.
4. Combine the two ranges into a bounded three-year answer, and make every inferential step explicit.

## Sources

- [x] [DeBellis et al. (2025) DevOps Research and Assessment (DORA) 2025 State of AI-assisted Software Development report](https://research.google/pubs/dora-2025-state-of-ai-assisted-software-development-report/) - official abstract for the 2025 DORA report based on nearly 5,000 technology professionals.
- [x] [Google Cloud (2025) Announcing the DevOps Research and Assessment (DORA) 2025 report](https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report) - official summary of AI, throughput, stability, platform quality, and fast feedback loop findings.
- [x] [Google Cloud (2025) DevOps Research and Assessment (DORA) AI Capabilities Model report landing page](https://cloud.google.com/resources/content/2025-dora-ai-capabilities-model-report) - official summary of platform adoption and platform-team prevalence in the surveyed population.
- [x] [DevOps Research and Assessment (DORA) Loosely coupled teams](https://dora.dev/capabilities/loosely-coupled-teams/) - architectural and organisational conditions associated with high software-delivery performance.
- [x] [Peng et al. (2023) The Impact of AI on Developer Productivity: Evidence from GitHub Copilot](https://arxiv.org/abs/2302.06590) - controlled experiment on a bounded JavaScript task.
- [x] [Kalliamvakou (2022) Quantifying GitHub Copilot's impact on developer productivity and happiness](https://github.blog/2022-09-07-research-quantifying-github-copilots-impact-on-developer-productivity-and-happiness/) - official experiment summary with task-completion and test-suite results.
- [x] [Becker et al. (2025) Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity](https://arxiv.org/abs/2507.09089) - randomized controlled trial on realistic repository tasks.
- [x] [Model Evaluation & Threat Research (METR) (2025) Early-2025 AI experienced open-source developer study](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/) - accessible summary of the same randomized controlled trial.
- [x] [Raković et al. (2020) Shadow IT: A Systematic Literature Review](https://doi.org/10.5755/j01.itc.49.1.23801) - systematic review of 77 papers, including recurring reasons for shadow IT occurrence.
- [x] [Fürstenau et al. (2020) From Shadow IT to Business-managed IT](https://link.springer.com/article/10.1007/s10257-020-00472-6) - empirical framing of business-managed IT and shadow IT as responses to unmet delivery need.
- [x] [van der Aalst et al. (2018) Robotic Process Automation](https://link.springer.com/article/10.1007/s12599-018-0542-4) - long-tail framing of what automation can and cannot economically absorb.
- [x] [Fischer et al. (2022) A framework for implementing robotic process automation projects](https://link.springer.com/article/10.1007/s10257-022-00553-8) - empirical and synthesis evidence on RPA fit, scaling, and failure.
- [x] [Digital.gov (2021) 5 tips for implementing citizen development in your Robotic Process Automation (RPA) program](https://digital.gov/2021/08/16/5-tips-for-implementing-citizen-development-in-your-rpa-program/) - public guidance on governance, environments, and limits of business-user automation programs.
- [x] [Ajimati et al. (2025) Adoption of low-code and no-code development: a systematic literature review and future research agenda](https://research.universityofgalway.ie/en/publications/adoption-of-low-code-and-no-code-development-a-systematic-literat-6/) - systematic review of 40 primary studies on Low-Code and No-Code (LCNC) adoption and citizen development.
- [x] [Binzer et al. (2024) Establishing a Low-Code/No-Code-Enabled Citizen Development Strategy](https://aisel.aisnet.org/misqe/vol23/iss3/3) - 24-company study on citizen development strategy design.
- [x] [Viljoen et al. (2024) Governing Citizen Development to Address Low-Code Platform Challenges](https://aisel.aisnet.org/misqe/vol23/iss3/6) - 30-interview study on governance, technical debt, and shadow IT risk.
- [x] [Binzer et al. (2025) Bridging Business and IT Through Low-Code/No-Code](https://hdl.handle.net/10125/108890) - 18-firm multi-case study on collaboration mechanisms and coordinated scaling.
- [x] [Conway (n.d.) Conway's Law](https://www.melconway.com/Home/Conways_Law.html) - original communication-structure thesis.
- [x] [Team Topologies (n.d.) Key concepts](https://teamtopologies.com/key-concepts) - definitions of stream-aligned and platform teams and dependency-reduction logic.
- [x] [Org Topologies (2024) Case study from component teams to Team Topologies to fast agile](https://www.orgtopologies.com/post/case-study-from-component-teams-to-team-topologies-to-fast-agile) - transformation case reporting 97% wait or waste time under component-team dependency structure.
- [x] [Mitchell (2026) Systems capability debt as the root cause of citizen development](https://davidamitchell.github.io/Research/research/2026-04-26-systems-capability-debt-citizen-development-empirical-evidence.html) - prior completed repository item on capability-gap causation and governance response.
- [x] [Mitchell (2026) Software engineering investment case for Large Language Model (LLM) value capture](https://davidamitchell.github.io/Research/research/2026-04-26-software-engineering-investment-case-llm.html) - prior completed repository item synthesising AI-assisted delivery evidence.
- [x] [Mitchell (2026) Citizen development rollout empirical evidence](https://davidamitchell.github.io/Research/research/2026-05-14-citizen-development-rollout-empirical-evidence.html) - prior completed repository item on rollout outcomes, failure modes, and weak effect-size evidence.
- [x] [Mitchell (2026) Organisational failure modes: customer-segment demand vs domain-based IT teams](https://davidamitchell.github.io/Research/research/2026-05-14-org-failure-modes-cohort-demand-domain-it.html) - prior completed repository item on delivery bottlenecks from boundary mismatch.
- [ ] [Theory of Constraints Institute](https://www.tocinstitute.org/) - seeded framing source identified but not consulted because stronger directly relevant delivery and queueing evidence was available from DORA and the completed cohort-demand item.
- [ ] [Gartner Hyperautomation glossary](https://www.gartner.com/en/information-technology/glossary/hyperautomation) - seeded source identified but not consulted because the accessible page is too high-level to support the needed claims.

---

## Research Skill Output

*(Full output from running the research skill, retained verbatim in the completed item. Sections 0 to 5 are the investigation; section 6 seeds the Findings section below.)*

### §0 Initialise

Question: determine whether public evidence supports a strong directional relationship between central IT throughput and capability-gap accumulation, and then estimate how much workaround automation demand a centrally governed build function can realistically absorb within three years.

Scope: in scope are large-organisation throughput constraints, shadow Information Technology (IT) and citizen-development demand, software-closeable versus resistant automation categories, and realistic AI-assisted software delivery uplift ranges; out of scope are enterprise-specific forecasting and unsupported universal coefficients.

Constraints: use public, verifiable sources; distinguish direct evidence from synthesis; record explicit gaps where public evidence does not support a precise elasticity or backlog ratio.

Output: knowledge, specifically a structured synthesis with executive summary, key findings, evidence map, assumptions, analysis, risks, and open questions.

Mode: full.

- [inference; source: https://davidamitchell.github.io/Research/research/2026-04-26-systems-capability-debt-citizen-development-empirical-evidence.html; https://davidamitchell.github.io/Research/research/2026-05-14-citizen-development-rollout-empirical-evidence.html; https://davidamitchell.github.io/Research/research/2026-05-14-org-failure-modes-cohort-demand-domain-it.html; https://davidamitchell.github.io/Research/research/2026-04-26-software-engineering-investment-case-llm.html] Prior completed repository work already established adjacent pieces of the problem, namely capability-gap-driven workaround demand, rollout limits of citizen development, boundary-driven throughput loss, and the weak transferability of microtask AI-coding gains to end-to-end software delivery, so this item uses those results as prior art and extends them into a bounded three-year answer.

### §1 Question Decomposition

- **Root question:** how much of workaround automation demand can central engineering realistically absorb within three years, and how tightly does that answer depend on throughput?
  - **A. Throughput and debt accumulation**
    - A1. What public evidence links delivery bottlenecks to shadow IT, citizen development, or workaround demand?
    - A2. What public evidence links architectural or team dependency structure to slower throughput and queue growth?
    - A3. Does public evidence provide a cross-firm coefficient for throughput shortfall versus debt accumulation?
  - **B. Demand classification**
    - B1. Which kinds of workaround demand are software-closeable by central engineering?
    - B2. Which kinds of demand remain resistant because they are exception-heavy, unstable, non-digital, or governance-limited?
    - B3. What does the rollout literature say about scaling citizen-development or RPA-like demand into governed delivery?
  - **C. AI-assisted productivity**
    - C1. What do bounded lab tasks imply about potential coding uplift?
    - C2. What do realistic repository tasks imply about end-to-end engineering uplift?
    - C3. What does DORA imply about throughput gains versus stability losses at system level?
  - **D. Three-year synthesis**
    - D1. Given the demand mix and throughput range, what closeable share is realistic?
    - D2. What would need to be true for the answer to move materially upward?

### §2 Investigation

#### 2.1 Source-access and search-gap notes

- Access note: seeded Gartner and Theory of Constraints Institute pages were not used for downstream evidence because more directly relevant and accessible sources existed for delivery throughput, queueing, and workaround demand.
- Failed primary-source search record: query `"IT throughput backlog growth technical debt enterprise coefficient"` returned no credible public cross-firm dataset that quantified a stable elasticity between delivery throughput and capability-gap accumulation.
- Failed primary-source search record: query `"shadow IT backlog reduction enterprise effect size low code"` returned no comparable public study that measured a standardized enterprise-scale backlog-reduction effect from citizen development or low-code rollout.

#### 2.2 Evidence that throughput shortfall generates workaround demand

- [fact; source: https://link.springer.com/article/10.1007/s10257-020-00472-6] Fürstenau et al. describe a marketing unit sourcing a Software as a Service (SaaS) event-management solution because the IT department would not be able to provide a suitable system as quickly as needed.
- [fact; source: https://link.springer.com/article/10.1007/s10257-020-00472-6] The same paper defines shadow IT as software, hardware, or IT service processes used or created autonomously by business units without alignment with the IT department.
- [fact; source: https://doi.org/10.5755/j01.itc.49.1.23801] Raković et al. define shadow IT as end-user-developed or adopted solutions that coexist with mandated systems and are often used to resolve non-routine issues for which mandated information systems do not have appropriate functions.
- [fact; source: https://doi.org/10.5755/j01.itc.49.1.23801] The Raković et al. systematic literature review concludes that the most common reason for shadow IT occurrence is the need to support business processes that are not supported, or not adequately supported, by the organisation's information system.
- [fact; source: https://link.springer.com/article/10.1007/s10257-020-00472-6] Fürstenau et al. report that 38% of technology purchases were estimated by Gartner to be managed, defined, and controlled by business leaders, and that 50 to 70% of employees use shadow IT according to cited prior research.
- [fact; source: https://research.universityofgalway.ie/en/publications/adoption-of-low-code-and-no-code-development-a-systematic-literat-6/] Ajimati et al. conclude that Low-Code and No-Code (LCNC) development extends software creation beyond professional software engineers to broader organisational participants and identify benefits and challenges across 40 primary studies.
- [fact; source: https://aisel.aisnet.org/misqe/vol23/iss3/3] Binzer et al. state that low-code and no-code platforms enable citizen developers, meaning employees with little or no IT background, to quickly create digital solutions.
- [fact; source: https://aisel.aisnet.org/misqe/vol23/iss3/6] Viljoen et al. state that entrusting software development to novices risks substandard software quality, shadow IT, and technical debt.
- [inference; source: https://link.springer.com/article/10.1007/s10257-020-00472-6; https://doi.org/10.5755/j01.itc.49.1.23801; https://aisel.aisnet.org/misqe/vol23/iss3/3; https://aisel.aisnet.org/misqe/vol23/iss3/6] Across shadow-IT and citizen-development sources, the core directional relationship is consistent: when central IT cannot deliver the needed capability with adequate speed or fit, business units create or buy their own automation and data-handling workarounds.

#### 2.3 Evidence that architecture and team structure govern throughput

- [fact; source: https://dora.dev/capabilities/loosely-coupled-teams/] DORA states that high software-delivery performance depends on teams being able to complete work, test, deploy, and release without fine-grained communication and coordination with other teams.
- [fact; source: https://dora.dev/capabilities/loosely-coupled-teams/] DORA states that tightly coupled architectures can create long lead times for changes, often measured in weeks or months, because work depends on integrated environments, coordinated releases, and bottleneck teams.
- [fact; source: https://dora.dev/capabilities/loosely-coupled-teams/] DORA identifies bottlenecks where a single team or service must scale to meet the demand of many dependent teams.
- [fact; source: https://www.melconway.com/Home/Conways_Law.html] Conway states that organisations produce system structures that copy their communication structures.
- [fact; source: https://teamtopologies.com/key-concepts] Team Topologies defines a stream-aligned team as aligned to a flow of work from a segment of the business domain and states that stream-aligned teams own an entire slice end to end with no hand-offs to other teams for any purpose.
- [fact; source: https://www.orgtopologies.com/post/case-study-from-component-teams-to-team-topologies-to-fast-agile] The Org Topologies case study reports that a 42-team component-team organisation had 97% wait or waste time, so work that should take 2 to 3 days took months because of blocking dependencies, hand-offs, queues, and asynchronous work.
- [fact; source: https://davidamitchell.github.io/Research/research/2026-05-14-org-failure-modes-cohort-demand-domain-it.html] The adjacent completed repository item synthesises evidence that cohort-demand routed across domain-team boundaries turns customer work into coordination programs of multiple backlogs rather than a single accountable flow of delivery.
- [inference; source: https://dora.dev/capabilities/loosely-coupled-teams/; https://www.melconway.com/Home/Conways_Law.html; https://teamtopologies.com/key-concepts; https://www.orgtopologies.com/post/case-study-from-component-teams-to-team-topologies-to-fast-agile; https://davidamitchell.github.io/Research/research/2026-05-14-org-failure-modes-cohort-demand-domain-it.html] Throughput is not just a headcount issue; it is largely a dependency-structure issue, so debt accumulates fastest where central delivery must cross shared-domain queues, release orchestration, and unclear boundary ownership.

#### 2.4 Evidence on which automation demand is closeable

- [fact; source: https://link.springer.com/article/10.1007/s12599-018-0542-4] van der Aalst et al. describe Robotic Process Automation (RPA) as tools that reduce repetitive, simple tasks and note that classical automation addresses the most frequent case types while the end of the long tail still needs to be handled by human workers.
- [fact; source: https://link.springer.com/article/10.1007/s12599-018-0542-4] van der Aalst et al. state that using RPA it is possible to support the middle part of the long tail, but this is not always possible or economically viable.
- [fact; source: https://link.springer.com/article/10.1007/s10257-022-00553-8] Fischer et al. state that RPA is typically used to automate already digital yet manual tasks or subprocesses within business processes and is associated with repetitive work performed daily, weekly, or monthly.
- [fact; source: https://link.springer.com/article/10.1007/s10257-022-00553-8] Fischer et al. state that expert knowledge is necessary to create reliable and scalable software robots and cite prior work estimating that up to 50% of initial RPA implementations fail.
- [fact; source: https://digital.gov/2021/08/16/5-tips-for-implementing-citizen-development-in-your-rpa-program/] Digital.gov states that citizen developers are most effective when they understand the workflow deeply, are comfortable with technology, and operate within governance that includes code review, role-based access controls, and separate development, test, and production environments.
- [fact; source: https://aisel.aisnet.org/misqe/vol23/iss3/6] Viljoen et al. state that governing citizen development requires technical experts and platform-specific governance functionalities because conventional software-development governance is not sufficient.
- [fact; source: https://hdl.handle.net/10125/108890] Binzer et al. identify coordinated scaling, project execution, and professional catalyst roles as distinct collaboration mechanisms in enterprise citizen-development programs.
- [fact; source: https://davidamitchell.github.io/Research/research/2026-05-14-citizen-development-rollout-empirical-evidence.html] The adjacent completed repository item concludes that the accessible empirical base is stronger on governance patterns and failure modes than on hard cross-firm effect sizes for backlog reduction.
- [inference; source: https://link.springer.com/article/10.1007/s12599-018-0542-4; https://link.springer.com/article/10.1007/s10257-022-00553-8; https://digital.gov/2021/08/16/5-tips-for-implementing-citizen-development-in-your-rpa-program/; https://aisel.aisnet.org/misqe/vol23/iss3/6; https://hdl.handle.net/10125/108890] The software-closeable portion of workaround demand is the stable, already-digital, rules-dominant middle of the queue that can be translated into governed workflows, interfaces, and services; the resistant portion is the unstable tail that still depends on exception handling, judgement, unresolved policy, poor data foundations, or coordination across badly designed boundaries.

#### 2.5 Evidence on realistic AI-assisted delivery uplift

- [fact; source: https://arxiv.org/abs/2302.06590] Peng et al. report that in a controlled experiment on implementing an HTTP server in JavaScript, the treatment group using GitHub Copilot completed the task 55.8% faster than the control group.
- [fact; source: https://github.blog/2022-09-07-research-quantifying-github-copilots-impact-on-developer-productivity-and-happiness/] GitHub reports that in the same experiment developers using GitHub Copilot completed the task significantly faster, 55% faster on average, with a higher completion rate.
- [fact; source: https://arxiv.org/abs/2507.09089] Becker et al. report that in a randomized controlled trial on 246 real tasks in mature open-source repositories, allowing AI tools increased completion time by 19% for experienced developers.
- [fact; source: https://arxiv.org/abs/2507.09089] Becker et al. state that the repositories in the trial were large, mature, and had high quality bars for code contributions, with tasks averaging 2.0 hours.
- [fact; source: https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report] Google Cloud's 2025 DORA summary states that unlike the prior year, AI adoption shows a positive relationship with software delivery throughput and product performance, but a negative relationship with software delivery stability.
- [fact; source: https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report; https://cloud.google.com/resources/content/2025-dora-ai-capabilities-model-report] The 2025 DORA material states that AI is an amplifier, that platform quality and fast feedback loops are prerequisites, and that 90% of surveyed organisations have adopted at least one internal platform while 76% have dedicated platform teams.
- [fact; source: https://research.google/pubs/dora-2025-state-of-ai-assisted-software-development-report/] The DORA 2025 report abstract states that the research includes more than 100 hours of qualitative data and survey responses from nearly 5,000 technology professionals.
- [inference; source: https://arxiv.org/abs/2302.06590; https://arxiv.org/abs/2507.09089; https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report; https://davidamitchell.github.io/Research/research/2026-04-26-software-engineering-investment-case-llm.html] The best-supported realistic range for end-to-end delivery uplift is modest and context-dependent, not equal to the 55% microtask gain: the evidence supports using a three-scenario planning range of roughly 0%, 15%, and 30% net throughput uplift, where 0% reflects realistic slowdown or offsetting rework, 15% reflects modest organisational gain, and 30% reflects a strong but still system-constrained upside in teams with good platforms and feedback loops.

#### 2.6 Synthesis for the three-year answer

- [fact; source: https://link.springer.com/article/10.1007/s10257-020-00472-6; https://doi.org/10.5755/j01.itc.49.1.23801; https://dora.dev/capabilities/loosely-coupled-teams/] Public evidence directly supports a directional relationship between throughput shortfall and workaround demand, but does not provide a single cross-firm coefficient for how many units of debt accumulate per unit of lost throughput.
- [fact; source: https://link.springer.com/article/10.1007/s12599-018-0542-4; https://link.springer.com/article/10.1007/s10257-022-00553-8; https://digital.gov/2021/08/16/5-tips-for-implementing-citizen-development-in-your-rpa-program/] Public evidence directly supports the claim that only a bounded subset of workaround demand is amenable to governed software automation at scale.
- [inference; source: https://link.springer.com/article/10.1007/s12599-018-0542-4; https://link.springer.com/article/10.1007/s10257-022-00553-8; https://arxiv.org/abs/2302.06590; https://arxiv.org/abs/2507.09089; https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report] Combining the automation-suitability evidence with the realistic AI-uplift range supports a bounded three-year answer: centrally governed software delivery is likely to absorb roughly one-quarter to one-half of current workaround automation demand, with values above one-half requiring a strong internal platform environment, an unusually high share of stable digital demand, and unusually low coordination debt.
- [inference; source: https://link.springer.com/article/10.1007/s12599-018-0542-4; https://aisel.aisnet.org/misqe/vol23/iss3/6; https://dora.dev/capabilities/loosely-coupled-teams/; https://www.orgtopologies.com/post/case-study-from-component-teams-to-team-topologies-to-fast-agile] The lower end of the range dominates in organisations where demand sits in the exception-heavy tail, governance debt is high, and dependencies remain structurally coupled; the upper end is only plausible where the demand queue is already mostly stable, digital, and reducible to independently deployable services and governed workflows.

### §3 Reasoning

- [fact; source: https://link.springer.com/article/10.1007/s10257-020-00472-6; https://doi.org/10.5755/j01.itc.49.1.23801] Facts: shadow-IT literature repeatedly reports unmet system support and inadequate delivery speed or fit as the most common reasons for workaround systems.
- [fact; source: https://dora.dev/capabilities/loosely-coupled-teams/; https://www.orgtopologies.com/post/case-study-from-component-teams-to-team-topologies-to-fast-agile] Facts: throughput falls when teams must coordinate across tightly coupled architectures and shared bottlenecks.
- [fact; source: https://link.springer.com/article/10.1007/s12599-018-0542-4; https://link.springer.com/article/10.1007/s10257-022-00553-8] Facts: only the stable, already-digital middle of the long tail is a strong candidate for automation, while the unstable tail remains human or uneconomic.
- [fact; source: https://arxiv.org/abs/2302.06590; https://arxiv.org/abs/2507.09089; https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report] Facts: AI-assisted software delivery evidence is mixed, with strong gains on a bounded lab task, slowdown on realistic repository tasks, and a positive throughput but negative stability relationship at DORA system level.
- [inference; source: https://link.springer.com/article/10.1007/s10257-020-00472-6; https://doi.org/10.5755/j01.itc.49.1.23801; https://dora.dev/capabilities/loosely-coupled-teams/; https://arxiv.org/abs/2507.09089] Inference: throughput is the dominant proximate cause of workaround accumulation when the unmet demand is software-shaped, but the three-year closure rate is jointly bounded by delivery structure, demand mix, and governance quality.
- [assumption; source: https://arxiv.org/abs/2302.06590; https://arxiv.org/abs/2507.09089; https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report] Assumption: a 0% to 30% net throughput uplift range is a more decision-useful and realistic planning bracket for end-to-end enterprise delivery than either a raw 55% coding-task uplift or a blanket slowdown estimate.
- [assumption; source: https://link.springer.com/article/10.1007/s12599-018-0542-4; https://link.springer.com/article/10.1007/s10257-022-00553-8; https://aisel.aisnet.org/misqe/vol23/iss3/6] Assumption: the share of workaround demand that is software-closeable in a typical large-enterprise queue is materially below 100% because a non-trivial residue remains exception-heavy, under-specified, or governance-limited even before delivery capacity is considered.

### §4 Consistency Check

- [fact; source: https://arxiv.org/abs/2302.06590; https://arxiv.org/abs/2507.09089] Potential contradiction checked: GitHub Copilot shows a 55.8% speedup while Model Evaluation & Threat Research (METR) shows a 19% slowdown. Resolution: the former is a bounded synthetic task with fixed scoring, while the latter is realistic repository work with high implicit-quality requirements, so the two studies support a wide but bounded planning range rather than a single estimate.
- [fact; source: https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report; https://dora.dev/capabilities/loosely-coupled-teams/] Potential contradiction checked: DORA reports positive throughput association but negative stability association. Resolution: AI can increase local output while worsening downstream reliability where platform quality and feedback loops are weak, so throughput gain is not equivalent to safe net capacity gain.
- [fact; source: https://link.springer.com/article/10.1007/s12599-018-0542-4; https://link.springer.com/article/10.1007/s10257-022-00553-8] Potential contradiction checked: RPA is described as rapid and lightweight, but up to 50% of initial implementations fail. Resolution: suitability and governance determine whether the apparent speed of implementation becomes durable delivery capacity.
- [inference; source: https://link.springer.com/article/10.1007/s10257-020-00472-6; https://doi.org/10.5755/j01.itc.49.1.23801; https://dora.dev/capabilities/loosely-coupled-teams/] No internal contradiction remains in the core conclusion that throughput shortfall is a major directional driver of capability-gap accumulation, while the exact magnitude remains under-measured in public cross-firm data.

### §5 Depth and Breadth Expansion

- [inference; source: https://dora.dev/capabilities/loosely-coupled-teams/; https://cloud.google.com/resources/content/2025-dora-ai-capabilities-model-report] Technical lens: platform quality, independent deployment, and fast feedback loops determine whether AI assistance translates into real throughput or merely into more unstable change volume.
- [inference; source: https://aisel.aisnet.org/misqe/vol23/iss3/6; https://digital.gov/2021/08/16/5-tips-for-implementing-citizen-development-in-your-rpa-program/; https://hdl.handle.net/10125/108890] Governance lens: the resistant residue in workaround demand is not only technical; part of it reflects missing intake, review, ownership, and escalation mechanisms that make local automation unsafe to scale.
- [inference; source: https://www.orgtopologies.com/post/case-study-from-component-teams-to-team-topologies-to-fast-agile; https://teamtopologies.com/key-concepts; https://www.melconway.com/Home/Conways_Law.html] Organisational-design lens: adding more developers without changing dependency topology can raise local utilisation while preserving the same queue structure that generated the current stock of workaround automations in the first place.
- [inference; source: https://arxiv.org/abs/2507.09089; https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report] Behavioural lens: leaders are at risk of overestimating the closure rate because both developers and experts overpredicted the productivity effect in the Model Evaluation & Threat Research (METR) trial, while DORA shows teams often perceive gains before systems-level constraints are resolved.
- [inference; source: https://davidamitchell.github.io/Research/research/2026-04-22-enterprise-ai-use-case-routing-frameworks.html; https://davidamitchell.github.io/Research/research/2026-04-26-ai-lowcode-risk-tier-classification-controls.html] Adjacent-governance lens: the share of demand that should stay outside business-led self-service rises as use cases become more action-capable, data-sensitive, or deeply integrated, which further limits the portion that can be safely closed by permissive local automation alone.

### §6 Synthesis

**Executive summary:**

Central IT throughput is a strong directional constraint on capability-gap accumulation, but public evidence does not support a single universal coefficient for how fast debt accumulates per unit of lost throughput. [inference; source: https://link.springer.com/article/10.1007/s10257-020-00472-6; https://doi.org/10.5755/j01.itc.49.1.23801; https://dora.dev/capabilities/loosely-coupled-teams/]

The best-supported three-year answer is that centrally governed software delivery is likely to absorb only about one-quarter to one-half of current workaround automation demand under realistic AI-assisted productivity assumptions, not the whole queue. [inference; source: https://link.springer.com/article/10.1007/s12599-018-0542-4; https://link.springer.com/article/10.1007/s10257-022-00553-8; https://arxiv.org/abs/2302.06590; https://arxiv.org/abs/2507.09089; https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report]

That limit exists because only the stable, already-digital, rules-dominant middle of workaround demand is software-closeable, while the unstable tail remains resistant even if coding productivity improves. [inference; source: https://link.springer.com/article/10.1007/s12599-018-0542-4; https://link.springer.com/article/10.1007/s10257-022-00553-8; https://aisel.aisnet.org/misqe/vol23/iss3/6]

Values near the top of the range require strong internal platforms, loosely coupled delivery teams, and a queue already dominated by tractable workflow demand rather than policy ambiguity, data debt, and cross-team coordination overhead. [inference; source: https://dora.dev/capabilities/loosely-coupled-teams/; https://cloud.google.com/resources/content/2025-dora-ai-capabilities-model-report; https://teamtopologies.com/key-concepts; https://www.orgtopologies.com/post/case-study-from-component-teams-to-team-topologies-to-fast-agile]

**Key findings:**

1. **Public evidence consistently shows that unmet central IT delivery speed or functional fit is a primary driver of shadow IT, business-managed IT, and citizen-development demand, so throughput shortfall is strongly associated with capability-gap accumulation even though the literature does not provide a universal elasticity coefficient.** ([inference]; high confidence; source: https://link.springer.com/article/10.1007/s10257-020-00472-6; https://doi.org/10.5755/j01.itc.49.1.23801; https://davidamitchell.github.io/Research/research/2026-04-26-systems-capability-debt-citizen-development-empirical-evidence.html)
2. **Throughput loss is driven as much by dependency topology as by raw staffing levels, because tightly coupled architectures and domain-queue handoffs convert customer or operational demand into long waits, release orchestration, and queue growth that central teams cannot clear quickly.** ([inference]; high confidence; source: https://dora.dev/capabilities/loosely-coupled-teams/; https://www.melconway.com/Home/Conways_Law.html; https://teamtopologies.com/key-concepts; https://www.orgtopologies.com/post/case-study-from-component-teams-to-team-topologies-to-fast-agile; https://davidamitchell.github.io/Research/research/2026-05-14-org-failure-modes-cohort-demand-domain-it.html)
3. **Only a bounded subset of workaround automation demand is software-closeable, because the strongest automation evidence repeatedly limits durable automation to stable, already-digital, repetitive, and governable work while the long-tail residue remains human, uneconomic, or governance-constrained.** ([inference]; high confidence; source: https://link.springer.com/article/10.1007/s12599-018-0542-4; https://link.springer.com/article/10.1007/s10257-022-00553-8; https://digital.gov/2021/08/16/5-tips-for-implementing-citizen-development-in-your-rpa-program/; https://aisel.aisnet.org/misqe/vol23/iss3/6)
4. **The empirical literature on citizen-development rollout supports faster local solution creation and broader participation, but it does not provide a strong cross-firm effect size for backlog reduction, which means any three-year closure estimate must remain a bounded inference rather than a measured enterprise benchmark.** ([inference]; medium confidence; source: https://research.universityofgalway.ie/en/publications/adoption-of-low-code-and-no-code-development-a-systematic-literat-6/; https://aisel.aisnet.org/misqe/vol23/iss3/3; https://davidamitchell.github.io/Research/research/2026-05-14-citizen-development-rollout-empirical-evidence.html)
5. **AI-assisted software delivery evidence is too mixed to justify an aggressive planning multiplier, because bounded laboratory tasks show large gains while realistic repository work can still slow experienced developers down and DORA reports that throughput gains are offset by stability losses in weaker systems.** ([inference]; high confidence; source: https://arxiv.org/abs/2302.06590; https://github.blog/2022-09-07-research-quantifying-github-copilots-impact-on-developer-productivity-and-happiness/; https://arxiv.org/abs/2507.09089; https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report)
6. **A realistic planning bracket for end-to-end AI-assisted throughput uplift is approximately 0% to 30%, where 0% reflects net slowdown or rework drag, 15% reflects modest system-level gain, and 30% reflects strong but platform-dependent improvement rather than unconstrained coding speed.** ([assumption]; medium confidence; source: https://arxiv.org/abs/2302.06590; https://arxiv.org/abs/2507.09089; https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report; https://research.google/pubs/dora-2025-state-of-ai-assisted-software-development-report/)
7. **Combining the demand-suitability evidence with the realistic throughput bracket supports a best-supported three-year closure range of roughly 25% to 50% of current workaround automation demand, with the lower half of the range more plausible in estates that still have high data debt, boundary friction, and governance drag.** ([inference]; medium confidence; source: https://link.springer.com/article/10.1007/s12599-018-0542-4; https://link.springer.com/article/10.1007/s10257-022-00553-8; https://arxiv.org/abs/2302.06590; https://arxiv.org/abs/2507.09089; https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report; https://dora.dev/capabilities/loosely-coupled-teams/)
8. **Closure rates above one-half are only plausible where the current workaround queue is already dominated by tractable workflow automation and the engineering estate has strong internal platforms, dedicated platform teams, low dependency coupling, and fast feedback loops that let AI gains survive contact with production controls.** ([inference]; medium confidence; source: https://cloud.google.com/resources/content/2025-dora-ai-capabilities-model-report; https://dora.dev/capabilities/loosely-coupled-teams/; https://teamtopologies.com/key-concepts; https://www.orgtopologies.com/post/case-study-from-component-teams-to-team-topologies-to-fast-agile)

**Evidence map:**

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [inference] Throughput shortfall strongly drives workaround demand, but public evidence does not give a universal elasticity coefficient. | https://link.springer.com/article/10.1007/s10257-020-00472-6; https://doi.org/10.5755/j01.itc.49.1.23801; https://davidamitchell.github.io/Research/research/2026-04-26-systems-capability-debt-citizen-development-empirical-evidence.html | high | Direction strong, coefficient missing |
| [inference] Dependency topology materially determines throughput loss and queue growth. | https://dora.dev/capabilities/loosely-coupled-teams/; https://www.melconway.com/Home/Conways_Law.html; https://teamtopologies.com/key-concepts; https://www.orgtopologies.com/post/case-study-from-component-teams-to-team-topologies-to-fast-agile; https://davidamitchell.github.io/Research/research/2026-05-14-org-failure-modes-cohort-demand-domain-it.html | high | Architecture and organisation linked |
| [inference] Only a bounded subset of workaround demand is software-closeable. | https://link.springer.com/article/10.1007/s12599-018-0542-4; https://link.springer.com/article/10.1007/s10257-022-00553-8; https://digital.gov/2021/08/16/5-tips-for-implementing-citizen-development-in-your-rpa-program/; https://aisel.aisnet.org/misqe/vol23/iss3/6 | high | Stable digital middle of long tail |
| [inference] The literature does not supply a robust enterprise backlog-reduction effect size for citizen development. | https://research.universityofgalway.ie/en/publications/adoption-of-low-code-and-no-code-development-a-systematic-literat-6/; https://aisel.aisnet.org/misqe/vol23/iss3/3; https://davidamitchell.github.io/Research/research/2026-05-14-citizen-development-rollout-empirical-evidence.html | medium | Evidence stronger on governance than effect size |
| [inference] AI-assisted delivery evidence is mixed and does not justify aggressive planning multipliers. | https://arxiv.org/abs/2302.06590; https://github.blog/2022-09-07-research-quantifying-github-copilots-impact-on-developer-productivity-and-happiness/; https://arxiv.org/abs/2507.09089; https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report | high | Bounded tasks and realistic tasks diverge |
| [assumption] A realistic net throughput uplift bracket is 0% to 30%. | https://arxiv.org/abs/2302.06590; https://arxiv.org/abs/2507.09089; https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report; https://research.google/pubs/dora-2025-state-of-ai-assisted-software-development-report/ | medium | Planning bracket, not measured enterprise constant |
| [inference] The best-supported three-year closure range is about 25% to 50% of current workaround automation demand. | https://link.springer.com/article/10.1007/s12599-018-0542-4; https://link.springer.com/article/10.1007/s10257-022-00553-8; https://arxiv.org/abs/2302.06590; https://arxiv.org/abs/2507.09089; https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report; https://dora.dev/capabilities/loosely-coupled-teams/ | medium | Range reflects bounded synthesis |
| [inference] Results above one-half require strong internal platforms, low coupling, and tractable demand. | https://cloud.google.com/resources/content/2025-dora-ai-capabilities-model-report; https://dora.dev/capabilities/loosely-coupled-teams/; https://teamtopologies.com/key-concepts; https://www.orgtopologies.com/post/case-study-from-component-teams-to-team-topologies-to-fast-agile | medium | Conditional upside case |

**Assumptions:**

- [assumption; source: https://arxiv.org/abs/2302.06590; https://arxiv.org/abs/2507.09089; https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report] The three-scenario AI-assisted throughput bracket of 0%, 15%, and 30% is used because it better fits the mixed empirical record than either an optimistic coding-task speedup or a pessimistic universal slowdown.
- [assumption; source: https://link.springer.com/article/10.1007/s12599-018-0542-4; https://link.springer.com/article/10.1007/s10257-022-00553-8] The software-closeable share of workaround demand is materially below 100% in large-enterprise queues because some residue remains exception-heavy, non-digital, or uneconomic to automate even before governance constraints are applied.
- [assumption; source: https://digital.gov/2021/08/16/5-tips-for-implementing-citizen-development-in-your-rpa-program/; https://aisel.aisnet.org/misqe/vol23/iss3/6; https://hdl.handle.net/10125/108890] Demand that lacks clear ownership, review paths, or environment controls is treated as resistant for the three-year horizon because governance remediation is part of the closure work, not a free precondition.

**Analysis:**

The strongest part of the evidence base is the directional chain from delivery shortfall to workaround demand. Shadow-IT and business-managed-IT studies repeatedly describe business units acting when central systems cannot deliver capability fast enough or well enough. [inference; source: https://link.springer.com/article/10.1007/s10257-020-00472-6; https://doi.org/10.5755/j01.itc.49.1.23801]

The next-strongest part is the throughput-side explanation for why the shortfall persists. DORA, Conway, Team Topologies, and the component-team case all point to coupling and hand-offs as core constraints, which means simply adding AI coding assistance does not automatically remove the queue structure that created the current stock of workaround automations. [inference; source: https://dora.dev/capabilities/loosely-coupled-teams/; https://www.melconway.com/Home/Conways_Law.html; https://teamtopologies.com/key-concepts; https://www.orgtopologies.com/post/case-study-from-component-teams-to-team-topologies-to-fast-agile]

The weak point in the evidence base is the missing public measurement of enterprise-wide backlog reduction from low-code and citizen-development rollout. That gap prevents a precise closure coefficient, so the final range is inferential rather than directly measured. [fact; source: https://research.universityofgalway.ie/en/publications/adoption-of-low-code-and-no-code-development-a-systematic-literat-6/; https://davidamitchell.github.io/Research/research/2026-05-14-citizen-development-rollout-empirical-evidence.html]

The chosen 25% to 50% range is therefore a bounded synthesis, not a discovered benchmark. The lower bound reflects estates where realistic AI uplift is near zero once rework and instability are counted, and where much of the queue sits in the resistant long-tail residue. The upper bound reflects estates where the queue is dominated by tractable workflow demand and where platform quality lets AI gains survive production controls. [inference; source: https://link.springer.com/article/10.1007/s12599-018-0542-4; https://arxiv.org/abs/2507.09089; https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report; https://cloud.google.com/resources/content/2025-dora-ai-capabilities-model-report]

Competing interpretations remain plausible. One rival view is that better model quality alone will soon eliminate today's slowdown cases. Another is that organisations could preserve local workaround-automation speed and govern it better instead of absorbing demand into central engineering. The current evidence does not rule those out, but it does show that platform quality, governance, and dependency structure are already first-order constraints today, which makes a pure model-quality explanation incomplete. [inference; source: https://arxiv.org/abs/2507.09089; https://aisel.aisnet.org/misqe/vol23/iss3/6; https://digital.gov/2021/08/16/5-tips-for-implementing-citizen-development-in-your-rpa-program/; https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report]

**Risks, gaps, uncertainties:**

- Public sources do not provide a stable cross-firm coefficient linking lost throughput to annual debt accumulation.
- Public sources do not provide a standardized enterprise-wide backlog-reduction effect size for citizen-development rollout.
- The 25% to 50% three-year range is a synthesis estimate and could move materially with better platform data, better internal demand segmentation, or stronger field evidence on AI-assisted delivery in production environments.
- The GitHub Copilot and Model Evaluation & Threat Research (METR) studies bound the productivity question from opposite sides, but neither is a direct field study of a large enterprise engineering organisation with regulated release controls.
- Some workaround demand may disappear through process redesign or policy clarification rather than through software delivery, which means central engineering closure is not the only relevant remediation path.

**Open questions:**

- What internal data model best measures the current split between stable software-closeable workaround demand and structurally resistant demand in a large enterprise queue?
- How much of current workaround demand is caused by missing platform capabilities versus missing cross-domain decision rights and governance?
- What field evidence emerges over the next 12 to 24 months on AI-assisted throughput in production engineering organisations with high compliance and release-quality bars?
- Can a reliable early-warning metric for capability-gap accumulation be constructed from shadow-IT discovery, workaround inventory growth, and queue lead-time data?

### §7 Recursive Review

- Review result: pass
- Acronym audit: pass
- Claim audit: pass
- Gap audit: pass
- Cross-item audit: pass

---

## Findings

### Executive Summary

Central IT throughput is a strong directional constraint on capability-gap accumulation, but public evidence does not support a single universal coefficient for how quickly debt accumulates per unit of lost throughput. [inference; source: https://link.springer.com/article/10.1007/s10257-020-00472-6; https://doi.org/10.5755/j01.itc.49.1.23801; https://dora.dev/capabilities/loosely-coupled-teams/]

The best-supported three-year answer is that centrally governed software delivery is likely to absorb only about 25% to 50% of current workaround automation demand under realistic AI-assisted productivity assumptions, not the whole queue. [inference; source: https://link.springer.com/article/10.1007/s12599-018-0542-4; https://link.springer.com/article/10.1007/s10257-022-00553-8; https://arxiv.org/abs/2302.06590; https://arxiv.org/abs/2507.09089; https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report]

That ceiling exists because only the stable, already-digital, rules-dominant middle of workaround demand is software-closeable, while the unstable tail remains resistant even if coding productivity improves. [inference; source: https://link.springer.com/article/10.1007/s12599-018-0542-4; https://link.springer.com/article/10.1007/s10257-022-00553-8; https://aisel.aisnet.org/misqe/vol23/iss3/6]

Results near the top of the range require strong internal platforms, loosely coupled delivery teams, and a queue already dominated by tractable workflow work rather than by data debt, policy ambiguity, or cross-team coordination friction. [inference; source: https://cloud.google.com/resources/content/2025-dora-ai-capabilities-model-report; https://dora.dev/capabilities/loosely-coupled-teams/; https://teamtopologies.com/key-concepts; https://www.orgtopologies.com/post/case-study-from-component-teams-to-team-topologies-to-fast-agile]

### Key Findings

1. **Public evidence consistently shows that unmet central IT delivery speed or functional fit is a primary driver of shadow IT, business-managed IT, and citizen-development demand, so throughput shortfall is strongly associated with capability-gap accumulation even though the literature does not provide a universal elasticity coefficient.** ([inference]; high confidence; source: https://link.springer.com/article/10.1007/s10257-020-00472-6; https://doi.org/10.5755/j01.itc.49.1.23801; https://davidamitchell.github.io/Research/research/2026-04-26-systems-capability-debt-citizen-development-empirical-evidence.html)
2. **Throughput loss is driven as much by dependency topology as by raw staffing levels, because tightly coupled architectures and domain-queue handoffs convert customer or operational demand into long waits, release orchestration, and queue growth that central teams cannot clear quickly.** ([inference]; high confidence; source: https://dora.dev/capabilities/loosely-coupled-teams/; https://www.melconway.com/Home/Conways_Law.html; https://teamtopologies.com/key-concepts; https://www.orgtopologies.com/post/case-study-from-component-teams-to-team-topologies-to-fast-agile; https://davidamitchell.github.io/Research/research/2026-05-14-org-failure-modes-cohort-demand-domain-it.html)
3. **Only a bounded subset of workaround automation demand is software-closeable, because the strongest automation evidence repeatedly limits durable automation to stable, already-digital, repetitive, and governable work while the long-tail residue remains human, uneconomic, or governance-constrained.** ([inference]; high confidence; source: https://link.springer.com/article/10.1007/s12599-018-0542-4; https://link.springer.com/article/10.1007/s10257-022-00553-8; https://digital.gov/2021/08/16/5-tips-for-implementing-citizen-development-in-your-rpa-program/; https://aisel.aisnet.org/misqe/vol23/iss3/6)
4. **The empirical literature on citizen-development rollout supports faster local solution creation and broader participation, but it does not provide a strong cross-firm effect size for backlog reduction, which means any three-year closure estimate must remain a bounded inference rather than a measured enterprise benchmark.** ([inference]; medium confidence; source: https://research.universityofgalway.ie/en/publications/adoption-of-low-code-and-no-code-development-a-systematic-literat-6/; https://aisel.aisnet.org/misqe/vol23/iss3/3; https://davidamitchell.github.io/Research/research/2026-05-14-citizen-development-rollout-empirical-evidence.html)
5. **AI-assisted software delivery evidence is too mixed to justify an aggressive planning multiplier, because bounded laboratory tasks show large gains while realistic repository work can still slow experienced developers down and DORA reports that throughput gains are offset by stability losses in weaker systems.** ([inference]; high confidence; source: https://arxiv.org/abs/2302.06590; https://github.blog/2022-09-07-research-quantifying-github-copilots-impact-on-developer-productivity-and-happiness/; https://arxiv.org/abs/2507.09089; https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report)
6. **A realistic planning bracket for end-to-end AI-assisted throughput uplift is approximately 0% to 30%, where 0% reflects net slowdown or rework drag, 15% reflects modest system-level gain, and 30% reflects strong but platform-dependent improvement rather than unconstrained coding speed.** ([assumption]; medium confidence; source: https://arxiv.org/abs/2302.06590; https://arxiv.org/abs/2507.09089; https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report; https://research.google/pubs/dora-2025-state-of-ai-assisted-software-development-report/)
7. **Combining the demand-suitability evidence with the realistic throughput bracket supports a best-supported three-year closure range of roughly 25% to 50% of current workaround automation demand, with the lower half of the range more plausible in estates that still have high data debt, boundary friction, and governance drag.** ([inference]; medium confidence; source: https://link.springer.com/article/10.1007/s12599-018-0542-4; https://link.springer.com/article/10.1007/s10257-022-00553-8; https://arxiv.org/abs/2302.06590; https://arxiv.org/abs/2507.09089; https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report; https://dora.dev/capabilities/loosely-coupled-teams/)
8. **Closure rates above one-half are only plausible where the current workaround queue is already dominated by tractable workflow automation and the engineering estate has strong internal platforms, dedicated platform teams, low dependency coupling, and fast feedback loops that let AI gains survive contact with production controls.** ([inference]; medium confidence; source: https://cloud.google.com/resources/content/2025-dora-ai-capabilities-model-report; https://dora.dev/capabilities/loosely-coupled-teams/; https://teamtopologies.com/key-concepts; https://www.orgtopologies.com/post/case-study-from-component-teams-to-team-topologies-to-fast-agile)

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [inference] Throughput shortfall strongly drives workaround demand, but public evidence does not give a universal elasticity coefficient. | https://link.springer.com/article/10.1007/s10257-020-00472-6; https://doi.org/10.5755/j01.itc.49.1.23801; https://davidamitchell.github.io/Research/research/2026-04-26-systems-capability-debt-citizen-development-empirical-evidence.html | high | Direction strong, coefficient missing |
| [inference] Dependency topology materially determines throughput loss and queue growth. | https://dora.dev/capabilities/loosely-coupled-teams/; https://www.melconway.com/Home/Conways_Law.html; https://teamtopologies.com/key-concepts; https://www.orgtopologies.com/post/case-study-from-component-teams-to-team-topologies-to-fast-agile; https://davidamitchell.github.io/Research/research/2026-05-14-org-failure-modes-cohort-demand-domain-it.html | high | Architecture and organisation linked |
| [inference] Only a bounded subset of workaround demand is software-closeable. | https://link.springer.com/article/10.1007/s12599-018-0542-4; https://link.springer.com/article/10.1007/s10257-022-00553-8; https://digital.gov/2021/08/16/5-tips-for-implementing-citizen-development-in-your-rpa-program/; https://aisel.aisnet.org/misqe/vol23/iss3/6 | high | Stable digital middle of long tail |
| [inference] The literature does not supply a robust enterprise backlog-reduction effect size for citizen development. | https://research.universityofgalway.ie/en/publications/adoption-of-low-code-and-no-code-development-a-systematic-literat-6/; https://aisel.aisnet.org/misqe/vol23/iss3/3; https://davidamitchell.github.io/Research/research/2026-05-14-citizen-development-rollout-empirical-evidence.html | medium | Governance evidence stronger than effect size evidence |
| [inference] AI-assisted delivery evidence is mixed and does not justify aggressive planning multipliers. | https://arxiv.org/abs/2302.06590; https://github.blog/2022-09-07-research-quantifying-github-copilots-impact-on-developer-productivity-and-happiness/; https://arxiv.org/abs/2507.09089; https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report | high | Microtasks and realistic tasks diverge |
| [assumption] A realistic net throughput uplift bracket is 0% to 30%. | https://arxiv.org/abs/2302.06590; https://arxiv.org/abs/2507.09089; https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report; https://research.google/pubs/dora-2025-state-of-ai-assisted-software-development-report/ | medium | Planning bracket, not a measured constant |
| [inference] The best-supported three-year closure range is about 25% to 50% of current workaround automation demand. | https://link.springer.com/article/10.1007/s12599-018-0542-4; https://link.springer.com/article/10.1007/s10257-022-00553-8; https://arxiv.org/abs/2302.06590; https://arxiv.org/abs/2507.09089; https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report; https://dora.dev/capabilities/loosely-coupled-teams/ | medium | Bounded synthesis |
| [inference] Results above one-half require strong internal platforms, low coupling, and tractable demand. | https://cloud.google.com/resources/content/2025-dora-ai-capabilities-model-report; https://dora.dev/capabilities/loosely-coupled-teams/; https://teamtopologies.com/key-concepts; https://www.orgtopologies.com/post/case-study-from-component-teams-to-team-topologies-to-fast-agile | medium | Conditional upside case |

### Assumptions

- **Assumption:** A 0% to 30% AI-assisted throughput uplift bracket is a realistic planning range for end-to-end delivery. **Justification:** the bounded-task Copilot experiment, realistic-task Model Evaluation & Threat Research (METR) trial, and DORA system-level evidence point to a wide but still bounded range rather than a single robust multiplier. [assumption; source: https://arxiv.org/abs/2302.06590; https://arxiv.org/abs/2507.09089; https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report]
- **Assumption:** The software-closeable share of workaround demand is materially below 100% in a typical large-enterprise queue. **Justification:** automation evidence repeatedly reserves a non-trivial tail for human handling, exception processing, or work that is not economically viable to automate. [assumption; source: https://link.springer.com/article/10.1007/s12599-018-0542-4; https://link.springer.com/article/10.1007/s10257-022-00553-8]
- **Assumption:** Demand without clear ownership, review paths, or environment controls remains resistant inside a three-year horizon even if it is technically scriptable. **Justification:** rollout evidence shows governance and expert support are part of what makes automation durable at scale. [assumption; source: https://digital.gov/2021/08/16/5-tips-for-implementing-citizen-development-in-your-rpa-program/; https://aisel.aisnet.org/misqe/vol23/iss3/6; https://hdl.handle.net/10125/108890]

### Analysis

The evidence base supports a clear causal direction but only a bounded quantitative answer. Shadow-IT and citizen-development studies repeatedly show that people build or buy local solutions when official systems cannot meet the needed speed or functional fit. That makes throughput shortfall a credible driver of capability-gap accumulation. [inference; source: https://link.springer.com/article/10.1007/s10257-020-00472-6; https://doi.org/10.5755/j01.itc.49.1.23801; https://aisel.aisnet.org/misqe/vol23/iss3/3]

The closure estimate cannot be derived from coding productivity alone because the throughput constraint is structural. DORA, Conway, Team Topologies, and the component-team case all indicate that queue growth depends on coupling, hand-offs, and platform quality, so a faster model in a still-coupled estate may increase change volume without proportionally reducing the workaround queue. [inference; source: https://dora.dev/capabilities/loosely-coupled-teams/; https://www.melconway.com/Home/Conways_Law.html; https://teamtopologies.com/key-concepts; https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report]

The one-quarter to one-half range reflects two compounding filters. First, not all workaround demand is software-closeable. Second, the closeable part is not all absorbable at the same speed because AI-assisted throughput gains are mixed and contingent. The result is a bounded rather than expansive three-year answer. [inference; source: https://link.springer.com/article/10.1007/s12599-018-0542-4; https://link.springer.com/article/10.1007/s10257-022-00553-8; https://arxiv.org/abs/2507.09089]

Plausible rival explanations remain. One rival view is that current field evidence understates future model gains. Another is that governance improvements to local workaround automation could outperform central absorption. The present evidence does not reject those possibilities, but it does show that platform quality, review structures, and dependency reduction are already prerequisites, which means the constraint is organisational as well as model-related. [inference; source: https://arxiv.org/abs/2507.09089; https://cloud.google.com/resources/content/2025-dora-ai-capabilities-model-report; https://aisel.aisnet.org/misqe/vol23/iss3/6]

### Risks, Gaps, and Uncertainties

- Public literature does not provide a stable cross-firm coefficient linking lost throughput to annual capability-gap accumulation.
- Public literature does not provide a standardized enterprise effect size for backlog reduction from citizen-development or low-code rollout.
- The 25% to 50% range is inferential and may shift with better internal demand-segmentation data or new field studies on AI-assisted delivery in high-control environments.
- The GitHub Copilot and METR studies bound the productivity question from opposite sides, but neither directly measures a regulated enterprise software-delivery organisation end to end.
- Some workaround demand may disappear through policy clarification or process redesign rather than through central software delivery, so engineering closure is not the only valid remediation path.

### Open Questions

- What internal metric set best distinguishes stable software-closeable workaround demand from structurally resistant demand in a large-enterprise queue?
- How much of current workaround demand is caused by missing platform capability versus missing decision rights, governance, or data quality?
- What new field evidence will emerge on AI-assisted throughput in production engineering organisations with high compliance and release-quality bars?
- Can a reliable early-warning metric for capability-gap accumulation be built from shadow-IT discovery, workaround inventory growth, and queue lead-time data?

---

## Output

- Type: knowledge
- Description: This item produces a bounded decision-useful estimate that central engineering throughput is a major directional driver of workaround accumulation, but that only about 25% to 50% of current workaround automation demand is likely to be closeable within three years under realistic AI-assisted delivery assumptions. [inference; source: https://link.springer.com/article/10.1007/s10257-020-00472-6; https://link.springer.com/article/10.1007/s12599-018-0542-4; https://arxiv.org/abs/2507.09089; https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report]
- Links:
  - https://link.springer.com/article/10.1007/s10257-020-00472-6
  - https://link.springer.com/article/10.1007/s12599-018-0542-4
  - https://arxiv.org/abs/2507.09089
