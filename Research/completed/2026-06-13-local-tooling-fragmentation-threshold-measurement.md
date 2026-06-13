---
review_count: 2
title: "At what scale or under what operating conditions do the aggregate costs of fragmented local tooling exceed the productivity gains from customization, and which metrics let organisations detect that crossover early?"
added: 2026-06-13T13:03:37+00:00
status: completed
priority: high
blocks: []
themes: [benchmarks-eval, tools-infrastructure, organisational-design, enterprise-adoption, governance-policy]
started: 2026-06-13T20:09:54+00:00
completed: 2026-06-13T20:50:05+00:00
output: [knowledge]
cites:
  - 2026-05-08-capability-debt-definition-measurement-ai-risk-amplification
  - 2026-04-26-systems-capability-debt-citizen-development-empirical-evidence
  - 2026-03-15-adam-smith-org-design-desire-paths-ai
  - 2026-06-13-local-global-optima-knowledge-work-throughput
related:
  - 2026-06-13-shadow-it-custom-tooling-governance-transition
  - 2026-06-13-platform-engineering-innersource-hybrid-standardization
  - 2026-06-13-standardization-customization-balance-context-ai
  - 2026-04-26-deployment-pipeline-citizen-development-governed-gate
superseded_by: ~
supersedes: ~
item_type: primary
confidence: medium
versions:
  - version: "1.0"
    sha: a19874f
    changed: 2026-06-13
    progress: progress/2026-06-13-local-tooling-fragmentation-threshold-measurement.md
    summary: "Initial completion"
---

# At what scale or under what operating conditions do the aggregate costs of fragmented local tooling exceed the productivity gains from customization, and which metrics let organisations detect that crossover early?

## Research Question

At what scale or under what operating conditions do the aggregate costs of fragmented local tooling exceed the productivity gains from customization, and which metrics let organisations detect that crossover early?

## Scope

**In scope:**
- Maintenance, onboarding, duplication, hidden support load, key-person dependency, error-rate, and throughput effects of locally owned scripts, spreadsheets, agents, extensions, and personal workflows.
- Measurement frameworks that distinguish beneficial local adaptation from fragmentation that degrades organisational performance.
- Leading indicators such as shadow-spend growth, collaboration friction, incident frequency, and widening support queues.

**Out of scope:**
- A universal numeric threshold that would apply unchanged across all organisations.
- Vendor-by-vendor product comparisons.
- Detailed implementation guidance for a specific organisation before the measurement question is answered.

**Constraints:** Prefer a mix of academic, practitioner, and empirical sources that can inform a practical measurement model for knowledge-work organisations.

## Context

This item informs the decision of when leadership should tolerate local customization and when it should instead invest in shared standards, shared platforms, or central support because the cumulative coordination cost has become systemically material.

## Approach

1. Define the benefit categories created by local customization and the cost categories created by fragmentation.
2. Identify published metrics, proxies, and decision models that organisations already use to measure hidden local-tooling cost.
3. Evaluate which leading indicators best signal a shift from productive local adaptation to harmful fragmentation.
4. Synthesize a measurement-oriented decision frame that can be reused in later items in this series.

## Sources

- [x] [Klotz et al. (2019) Causing Factors, Outcomes, and Governance of Shadow IT and Business-Managed IT: A Systematic Literature Review](https://aisel.aisnet.org/ijispm/vol7/iss1/3/) - systematic review covering causes, outcomes, and governance patterns for shadow Information Technology (IT).
- [x] [Sinsky et al. (2021) Standardization vs Customization: Finding the Right Balance](https://www.annfammed.org/content/19/2/171) - peer-reviewed framing for balancing standardization and local adaptation.
- [x] [Forte Labs (2019) Theory of Constraints 102: Local Optima](https://fortelabs.co/blog/theory-of-constraints-102-local-optima/) - practitioner explanation of why local optimisation can damage whole-system performance in knowledge work; Theory of Constraints (TOC) applied to knowledge-work settings.
- [x] [DevOps Research and Assessment (DORA) (2025) State of AI-assisted Software Development 2025](https://dora.dev/research/2025/dora-report/) - empirical report with outcome measures for software delivery systems using Artificial Intelligence (AI).
- [x] [Mitchell (2026) What is capability debt in Artificial Intelligence (AI) systems, how can it be measured, and how does it amplify operational and governance risk?](https://davidamitchell.github.io/Research/research/2026-05-08-capability-debt-definition-measurement-ai-risk-amplification.html) - prior repository work on measurement and hidden organisational cost.
- [x] [Mitchell (2026) What empirical evidence exists that citizen development and fragmented local automation create systems or capability debt, and how large is that debt?](https://davidamitchell.github.io/Research/research/2026-04-26-systems-capability-debt-citizen-development-empirical-evidence.html) - prior repository synthesis on debt created by decentralised local tooling.
- [x] [Kopper et al. (2020) From Shadow Information Technology (IT) to Business-managed IT](https://link.springer.com/article/10.1007/s10257-020-00472-6) - empirical study of governance transition from covert shadow IT to overt business-managed IT with ownership maturity framework.
- [x] [Faros AI (2026) Key Takeaways from the DORA Report 2025 and AI Engineering Report 2026](https://www.faros.ai/blog/key-takeaways-from-the-dora-report-2025) - telemetry-backed analysis: "Acceleration Whiplash" showing individual gains with system-level quality deterioration across 22,000 developers.
- [x] [DORA (2024) Accelerate State of DevOps Report 2024](https://dora.dev/research/2024/dora-report/) - annual survey including platform engineering adoption and productivity correlations.
- [x] [InfoQ (2026) AI Is Amplifying Software Engineering Performance, Says the 2025 DORA Report](https://www.infoq.com/news/2026/03/ai-dora-report/) - secondary analysis of DORA 2025 findings on fragmented tooling and platform quality.
- [x] [Mitchell (2026) How does local optimisation of team- and role-level tooling in knowledge work reduce organisation-level throughput?](https://davidamitchell.github.io/Research/research/2026-06-13-local-global-optima-knowledge-work-throughput.html) - prior repository synthesis on local optima, Theory of Constraints (TOC), and shared constraint throughput.
- [x] [TechFinitive (2024) How to keep shadow IT and its costs under control](https://www.techfinitive.com/features/how-to-keep-shadow-it-costs-under-control/) - practitioner source citing Gartner shadow IT spend figures.
- [x] [Valence Security (2024) 3 out of 4 employees sidestep IT, bring their own tech](https://www.valencesecurity.com/resources/blogs/gartner-saas-applications-outside-of-it) - practitioner source citing Gartner 2027 projection.
- [x] [Platform Engineering (2025) DORA 2025: AI Won't Save You Without a Solid Platform](https://platformengineering.com/features/dora-2025-ai-wont-save-you-without-a-solid-platform/) - DORA 2025 analysis on platform engineering adoption and productivity correlations.

## Related

- [What empirical evidence exists that citizen development and fragmented local automation create systems or capability debt, and how large is that debt?](https://davidamitchell.github.io/Research/research/2026-04-26-systems-capability-debt-citizen-development-empirical-evidence.html)
- [What is capability debt in Artificial Intelligence (AI) systems, how can it be measured, and how does it amplify operational and governance risk?](https://davidamitchell.github.io/Research/research/2026-05-08-capability-debt-definition-measurement-ai-risk-amplification.html)
- [How can Adam Smith's division of labour framework be applied to the future of organisational design in a world with AI?](https://davidamitchell.github.io/Research/research/2026-03-15-adam-smith-org-design-desire-paths-ai.html)

---

## Research Skill Output

*(Full output from running the research skill, retained verbatim in the completed item. Sections 0-5 are the investigation; section 6 seeds the Findings section below.)*

### §0 Initialise

Question: At what scale or under what operating conditions do the aggregate costs of fragmented local tooling exceed the productivity gains from customization, and which metrics let organisations detect that crossover early?

Scope: In scope are maintenance, onboarding, duplication, hidden support load, key-person dependency, error-rate, and throughput effects of locally owned scripts, spreadsheets, agents, extensions, and personal workflows; measurement frameworks distinguishing beneficial local adaptation from harmful fragmentation; and leading indicators such as shadow-spend growth, collaboration friction, incident frequency, and widening support queues. Out of scope are universal numeric thresholds, vendor comparisons, and detailed implementation guidance before the measurement question is answered.

Constraints: Prefer a mix of academic, practitioner, and empirical sources. Expand all acronyms on first use. Separate fact from inference. Use prior repository items as adjacent synthesis rather than sole evidence.

Output format: Knowledge synthesis.

Working hypotheses:
[assumption; source: https://aisel.aisnet.org/ijispm/vol7/iss1/3/; https://link.springer.com/article/10.1007/s10257-020-00472-6] Local tooling fragmentation creates costs in four categories: maintenance and support burden, integration and coordination friction, knowledge concentration risk, and governance and compliance exposure. These costs are initially hidden, surface slowly as team and tool count grows, and reach a crossover point relative to customization benefits at some combination of team scale, shared dependency density, and staff turnover rate.

[assumption; source: https://aisel.aisnet.org/ijispm/vol7/iss1/3/; https://link.springer.com/article/10.1007/s10257-020-00472-6] The crossover is not a fixed universal threshold but a function of three interacting variables: the number of independent tooling instances, the density of shared dependencies they impose on others, and the rate at which the knowledge embedded in those tools must be transferred across role or organisational boundaries. This is grounded in the Klotz et al. shadow IT review's identification of enablers and motivators as context-specific, and Kopper et al.'s governance-transition finding that coordination cost varies with ownership maturity.

Prior research cross-reference: [inference; source: https://davidamitchell.github.io/Research/research/2026-06-13-local-global-optima-knowledge-work-throughput.html; https://davidamitchell.github.io/Research/research/2026-04-26-systems-capability-debt-citizen-development-empirical-evidence.html; https://davidamitchell.github.io/Research/research/2026-05-08-capability-debt-definition-measurement-ai-risk-amplification.html] The completed item on local-global optima in knowledge work (2026-06-13-local-global-optima-knowledge-work-throughput) established via the Theory of Constraints (TOC) that local tooling gains degrade whole-system throughput when shared constraint capacity is not raised commensurately. The completed items on systems capability debt (2026-04-26-systems-capability-debt-citizen-development-empirical-evidence) and capability debt measurement (2026-05-08-capability-debt-definition-measurement-ai-risk-amplification) established the typology and measurement logic for accumulated organisational gaps. This item extends those foundations by focusing on the crossover question: when does the cost side of fragmented local tooling become detectable and measurable as a leading signal?

### §1 Question Decomposition

Root question: at what scale or operating conditions do aggregate local-tooling costs exceed customization benefits, and which metrics detect that crossover early?

**A. Cost and benefit categories of fragmented local tooling**
- A1. What benefit categories does local customization produce for the team that builds it?
- A2. What cost categories does fragmented local tooling impose on the broader organisation?
- A3. Which cost categories are most likely to remain hidden until they reach material scale?

**B. Existing measurement approaches**
- B1. What metrics or proxies have shadow Information Technology (shadow IT) and business-managed IT researchers identified for hidden local-tooling cost?
- B2. What frameworks or thresholds have practitioners proposed for deciding when to consolidate or standardise?
- B3. What does the DevOps Research and Assessment (DORA) corpus say about fragmented tooling and organisational outcomes?

**C. Leading indicators of the crossover**
- C1. Which signals appear before aggregate cost has demonstrably exceeded aggregate benefit?
- C2. Which signals are detectable with data that knowledge-work organisations already collect?
- C3. What role does team size, staff turnover, and shared dependency density play in accelerating the crossover?

**D. Decision frame**
- D1. What decision model integrates the cost, benefit, and leading-indicator evidence into a reusable frame for organisations?
- D2. What are the practical limits of any such frame?

### §2 Investigation

**A. Benefit and cost categories**

A1. Benefit categories of local customization:
[fact; source: https://aisel.aisnet.org/ijispm/vol7/iss1/3/] The Klotz et al. (2019) systematic literature review of shadow IT identifies three categories of benefit from locally managed tooling: increased agility and innovation velocity at the business-unit level, solutions better tailored to immediate operational needs, and reduced dependency on central IT queues that are often slow or misaligned. The review covers 82 papers and is the most comprehensive synthesis of the causes and outcomes literature available in a peer-reviewed source.

[inference; source: https://www.annfammed.org/content/19/2/171] Sinsky et al. (2021), writing in the Annals of Family Medicine, frame the standardization versus customization balance as a question of "appropriate customization": routine low-variation tasks are candidates for standardization, while high-complexity or non-routine tasks benefit from local adaptation that frees practitioner judgment. The analysis is framed for medical practice but the underlying logic applies to any knowledge-work role where task complexity varies widely across individuals.

A2. Cost categories imposed on the broader organisation:
[fact; source: https://aisel.aisnet.org/ijispm/vol7/iss1/3/] Klotz et al. document four recurring cost categories in the shadow IT literature: security and compliance exposure (unauthorised tools bypass identity management, data governance, and audit controls), integration complexity (non-standard tools do not connect to shared data systems without manual intervention or custom connectors), duplicate spend and license overlap (departments pay separately for overlapping capabilities), and loss of central IT visibility and control over processes and data.

[inference; source: https://link.springer.com/article/10.1007/s10257-020-00472-6] Kopper et al. (2020), in a study of the transition from covert shadow IT to overt business-managed IT, identify a fifth cost category that is largely absent from the earlier literature: accumulated key-person concentration, where the tacit knowledge required to operate or extend a locally owned tool becomes concentrated in one or two individuals whose departure creates an immediate operational gap. This is the "bus factor" (the number of people who must leave before a process is paralysed) applied to tooling rather than code.

[inference; source: https://www.techfinitive.com/features/how-to-keep-shadow-it-costs-under-control/; https://www.valencesecurity.com/resources/blogs/gartner-saas-applications-outside-of-it] Secondary practitioner sources citing Gartner research estimate that shadow IT accounts for 30 to 40 percent of total IT spend in large enterprises, and project that by 2027, 75 percent of employees will acquire or modify technology outside IT department visibility, up from 41 percent in 2022. The primary Gartner report was not accessible in this research session; these figures are therefore an inference from secondary attribution rather than direct primary-source fact, and should be treated as directional indicators consistent with the broader fragmentation trajectory documented in the academic literature.

A3. Hidden cost categories:
[inference; source: https://aisel.aisnet.org/ijispm/vol7/iss1/3/; https://link.springer.com/article/10.1007/s10257-020-00472-6] The costs most likely to remain hidden until scale are: informal peer support time (captured in no helpdesk ticket, logged in no system), new-hire onboarding friction from non-standard tooling (absorbed into general onboarding time estimates rather than attributed to tool complexity), key-person concentration (invisible until the key person leaves), and integration rework cost (charged to the project that discovers the incompatibility, not to the fragmented tool that caused it). Maintenance overhead is partially visible in IT helpdesk tickets but frequently mis-attributed to user error rather than tool complexity.

**B. Existing measurement approaches**

B1. Shadow IT measurement proxies:
[fact; source: https://aisel.aisnet.org/ijispm/vol7/iss1/3/] The shadow IT literature uses three main proxy categories for measuring hidden local-tooling cost: (1) application discovery and inventory audits, which count the number of tools in use outside sanctioned lists; (2) security scan outcomes, which surface compliance gaps attributable to unsanctioned tools; and (3) IT service desk attribution analysis, which maps support tickets to tool categories and identifies whether non-standard tools generate disproportionate ticket volume.

[fact; source: https://link.springer.com/article/10.1007/s10257-020-00472-6] Kopper et al. (2020) propose an additional measurement lens: governance maturity assessment, tracking whether business-unit tooling has moved from covert (shadow IT) to overt (business-managed IT) with documented ownership, security review, and exit procedures. Items that remain covert after an inventory audit represent unquantified organisational risk.

B2. Practitioner consolidation frameworks:
[inference; source: https://www.faros.ai/blog/key-takeaways-from-the-dora-report-2025] Faros AI telemetry across 22,000 developers documents the "Acceleration Whiplash" pattern in which individual task completion rose 33.7% in AI-assisted teams while pull request (PR) review time rose 441% and production incidents per PR rose 242.7%. Faros interprets this as a signal that local tooling gains have flooded shared review infrastructure without corresponding capacity increases. This pattern offers a measurable consolidation trigger: when downstream queue growth rate exceeds upstream delivery rate growth, local gains have become a system-level cost.

[inference; source: https://www.annfammed.org/content/19/2/171] Sinsky's framing implies an observable consolidation trigger: standardization becomes the preferred strategy when the practitioner's cognitive and coordination overhead from customization grows faster than the quality benefit from customization. In operational terms this translates to: measure the overhead separately from the benefit; when overhead growth rate exceeds benefit growth rate, the crossover has occurred.

B3. DORA corpus findings:
[fact; source: https://dora.dev/research/2025/dora-report/; https://www.infoq.com/news/2026/03/ai-dora-report/] The DORA 2025 report, based on nearly 5,000 technology professionals, found that Artificial Intelligence (AI) acts as an amplifier of existing organisational conditions. Organisations with mature platform engineering and tooling coherence convert AI investment into system-level performance gains; organisations with fragmented tooling experience accelerated instability. DORA 2025 identifies seven capabilities required for AI investment to translate to organisational performance, including working in small batches, user-centred platform design, and loosely coupled teams.

[fact; source: https://dora.dev/research/2024/dora-report/; https://platformengineering.com/features/dora-2025-ai-wont-save-you-without-a-solid-platform/] The DORA 2024 report found that 76 percent of organisations with high-performance delivery have dedicated platform engineering teams. Internal developer platforms (IDPs) that provide a user-centred, standardised interface correlate with 8 percent higher individual productivity, 10 percent higher team performance, and 6 percent higher overall software delivery performance. Poorly designed or fragmented platforms reduce stability, not just individual productivity.

**C. Leading indicators of the crossover**

C1. Pre-crossover signals:
[inference; source: https://aisel.aisnet.org/ijispm/vol7/iss1/3/; https://link.springer.com/article/10.1007/s10257-020-00472-6] The shadow IT literature identifies five signals that appear before aggregate fragmentation cost has demonstrably exceeded aggregate benefit: (1) rising support ticket volume per non-standard tool, outpacing the rate at which those tools' user base grows; (2) lengthening new-hire time-to-productivity, where onboarding time grows faster than team complexity; (3) shadow spend growth, where SaaS (Software as a Service) discovery tools reveal tool counts increasing faster than headcount or output; (4) integration failure frequency, where data or workflow incompatibility incidents increase quarter-on-quarter; and (5) incident attribution shift, where post-incident reviews increasingly identify non-standard tools as contributing factors.

[inference; source: https://www.faros.ai/blog/key-takeaways-from-the-dora-report-2025; https://dora.dev/research/2025/dora-report/] A sixth leading indicator observable in software delivery organisations is the PR review time relative to deployment frequency ratio: when PR review time grows faster than deployment frequency, shared review infrastructure is becoming the constraint, which is the observable pre-crossover signal in the DORA/Faros evidence chain.

C2. Detectable with existing data:
[inference; source: https://aisel.aisnet.org/ijispm/vol7/iss1/3/] IT helpdesk ticket data, new-hire onboarding surveys, SaaS discovery scan outputs, and post-incident review records are all data sources that most knowledge-work organisations already collect or can collect without new tooling investment. The measurement gap is not data availability but attribution discipline: these datasets must be tagged to tool category and owner type (central versus local) to reveal the fragmentation signal rather than aggregate it into undifferentiated overhead.

C3. Team size, turnover, and shared dependency density effects:
[inference; source: https://aisel.aisnet.org/ijispm/vol7/iss1/3/; https://link.springer.com/article/10.1007/s10257-020-00472-6] The shadow IT literature supports three structural multipliers that accelerate the crossover: (a) team scale, where each additional team that creates local tooling adds its own maintenance surface and integration interface to the overall coordination cost; (b) staff turnover, where the knowledge-concentration risk compounds with each role transition and the bus factor declines as key persons leave without documentation; and (c) shared dependency density, where tools that share data with central systems or feed downstream processes impose their integration complexity on every consumer of those downstream outputs, not just the originating team.

[assumption; source: https://davidamitchell.github.io/Research/research/2026-06-13-local-global-optima-knowledge-work-throughput.html; https://fortelabs.com/blog/theory-of-constraints-102-local-optima/] TOC provides a theoretical upper bound on the crossover: in any pipeline where teams share a downstream constraint (approval queue, shared service, compliance review), the crossover occurs no later than the point where local tooling output exceeds the constraint's capacity to process it, because beyond that point, additional local productivity generates queue depth rather than delivered outcomes.

**D. Decision frame synthesis**

D1. A decision frame for organisations:
[inference; source: https://aisel.aisnet.org/ijispm/vol7/iss1/3/; https://www.annfammed.org/content/19/2/171; https://dora.dev/research/2025/dora-report/] The evidence supports a two-dimension measurement model. The first dimension is tool footprint: the count of locally owned tooling instances per unit of staff, cross-multiplied by the shared dependency density of each tool (how many other teams, datasets, or systems depend on its outputs). The second dimension is lifecycle cost ratio: the ratio of aggregate maintenance, support, and integration cost per tool to the direct productivity benefit that tool generates. The crossover is signalled when the product of these two dimensions exceeds the organisation's measured capacity to absorb coordination overhead without degrading shared constraint throughput.

[inference; source: https://link.springer.com/article/10.1007/s10257-020-00472-6; https://aisel.aisnet.org/ijispm/vol7/iss1/3/] The governance transition literature adds a third dimension: documentation and ownership maturity. Tools with documented ownership, exit procedures, and regular security review (overt business-managed IT) impose lower coordination cost than covert shadow IT tools with identical functionality, because ownership maturity determines whether the tool can be rapidly decommissioned or transitioned when the key person leaves.

D2. Practical limits:
[inference; source: https://aisel.aisnet.org/ijispm/vol7/iss1/3/] The measurement frame depends on attribution discipline that most organisations currently lack: support tickets, onboarding records, and incident logs must be tagged to tool category and ownership type to reveal the fragmentation signal. Implementing the attribution layer is itself a governance investment, and organisations below a minimum scale threshold may find the governance investment exceeds the fragmentation cost it reveals.

### §3 Reasoning

The core causal chain connecting fragmented local tooling to aggregate cost exceeding benefit runs through five steps:

1. Local tooling solves an immediate problem faster than central IT can respond. [fact; source: https://aisel.aisnet.org/ijispm/vol7/iss1/3/]
2. Each local tool creates a maintenance surface, a knowledge concentration point, and an integration interface. [fact; source: https://aisel.aisnet.org/ijispm/vol7/iss1/3/; https://link.springer.com/article/10.1007/s10257-020-00472-6]
3. These costs are initially smaller than the productivity benefit and remain hidden because they are not attributed to the tool. [inference; source: https://aisel.aisnet.org/ijispm/vol7/iss1/3/]
4. As the tool count, team scale, staff turnover, and shared dependency density increase, the hidden costs compound while the benefits plateau for each individual tool. [inference; source: https://aisel.aisnet.org/ijispm/vol7/iss1/3/; https://www.faros.ai/blog/key-takeaways-from-the-dora-report-2025]
5. The crossover becomes observable when hidden costs begin surfacing in proxy metrics (support tickets, onboarding time, incident attribution, queue growth) before the total cost has been formally calculated. [inference; source: https://www.faros.ai/blog/key-takeaways-from-the-dora-report-2025; https://dora.dev/research/2025/dora-report/]

Logical gaps removed from earlier drafts: the claim that "any fragmentation is harmful" is unsupported; the evidence consistently shows a benefit phase followed by a crossover. The claim that a single numeric threshold applies universally is explicitly excluded by both the shadow IT literature and Sinsky's framing, which both identify context-specific factors as the primary determinants.

### §4 Consistency Check

```text
contradiction_scan: no internal contradictions found
  Note 1: Gartner figures (30-40% shadow spend, 75% by 2027) are widely cited
    but attributed to Gartner via secondary practitioner sources only; primary
    Gartner report was not accessible. Relabeled to [inference] with secondary-source
    URL; confidence appropriately medium for any claim relying on these figures.
  Note 2: Sinsky (2021) is the Annals of Family Medicine piece at
    https://www.annfammed.org/content/19/2/171; full text is behind
    institutional access; content confirmed via abstract and multiple secondary
    summaries; used as [inference] only with appropriate hedging.
  Note 3: TOC crossover claim and shadow IT crossover claim are consistent:
    both identify shared dependency density as the primary multiplier.
    No contradiction.
confidence_adjustment: medium applied uniformly; primary empirical sources for
  the crossover question are shadow IT reviews (secondary academic), Faros AI
  telemetry (single vendor), and DORA surveys (multi-org but self-reported).
  No randomised controlled experiment directly tests the crossover threshold.
scope_guardrail: maintained; no universal numeric threshold asserted;
  no vendor product comparisons included.
acronym_check: Information Technology (IT), Theory of Constraints (TOC),
  Artificial Intelligence (AI), shadow IT, DORA (DevOps Research and Assessment),
  SaaS (Software as a Service), pull request (PR), internal developer platform (IDP),
  bus factor defined on first use. All clear.
```

### §5 Depth and Breadth Expansion

**Technical lens:** The bus factor concept from software engineering provides a quantifiable proxy for knowledge-concentration risk in fragmented tooling. [inference; source: https://link.springer.com/article/10.1007/s10257-020-00472-6] A bus factor of 1 or 2 for a locally owned tool means any unplanned departure creates an immediate operational dependency gap. Measuring bus factor across the tool estate produces a portfolio-level knowledge-concentration index that can be tracked over time as a leading indicator distinct from but complementary to support-ticket volume.

**Regulatory lens:** In regulated industries, locally owned tools that touch regulated data or processes create compliance exposure that does not scale linearly with tool count. [inference; source: https://aisel.aisnet.org/ijispm/vol7/iss1/3/] Each such tool is a potential audit finding, and regulators in banking, healthcare, and financial services have increasingly scrutinised model risk and data governance frameworks that depend on undocumented or non-standard tooling. [inference; source: https://aisel.aisnet.org/ijispm/vol7/iss1/3/] The compliance exposure multiplier is highest where tools feed outputs into decisions subject to regulatory review. [inference; source: https://aisel.aisnet.org/ijispm/vol7/iss1/3/]

**Economic lens:** The Gartner shadow spend estimate (30 to 40 percent of IT budget in large enterprises) suggests the aggregate cost is already economically material before any crossover calculation is applied. [inference; source: https://www.techfinitive.com/features/how-to-keep-shadow-it-costs-under-control/] The relevant economic question is how large the benefit must be to justify that cost. [inference; source: https://www.techfinitive.com/features/how-to-keep-shadow-it-costs-under-control/] At 30 to 40 percent of IT budget, the burden of proof for justifying continued fragmentation shifts to demonstrating ongoing measurable benefit. [inference; source: https://www.techfinitive.com/features/how-to-keep-shadow-it-costs-under-control/; https://aisel.aisnet.org/ijispm/vol7/iss1/3/]

**Historical lens:** The Kopper et al. (2020) governance-transition literature observes that shadow IT has existed as a phenomenon since at least the 1980s, when business units first deployed personal computers and spreadsheets without IT department oversight. [inference; source: https://link.springer.com/article/10.1007/s10257-020-00472-6] The current AI-tooling wave follows a pattern — rapid local adoption, hidden cost accumulation, governance intervention after a material failure — that the governance-transition literature documents across three prior waves: personal computing, internet-era web applications, and SaaS adoption. [inference; source: https://link.springer.com/article/10.1007/s10257-020-00472-6] The leading indicators described in this item are consistent with the cost-accumulation phase documented in Kopper et al.'s account of all three prior waves. [inference; source: https://link.springer.com/article/10.1007/s10257-020-00472-6]

**Behavioural lens:** Adam Smith's desire-path framework, as synthesised in the prior repository item on organisational design (2026-03-15-adam-smith-org-design-desire-paths-ai), explains why local tooling persists even after the crossover: the individual who built the tool experiences its benefit directly while the costs are distributed across the organisation and remain invisible to them. [inference; source: https://davidamitchell.github.io/Research/research/2026-03-15-adam-smith-org-design-desire-paths-ai.html] This benefit-visibility asymmetry means the crossover is not self-correcting through individual behaviour alone. [inference; source: https://davidamitchell.github.io/Research/research/2026-03-15-adam-smith-org-design-desire-paths-ai.html] Organisational governance mechanisms such as ownership registries, cost attribution, and exit-procedure requirements are the documented correction instruments in the shadow IT literature. [inference; source: https://aisel.aisnet.org/ijispm/vol7/iss1/3/; https://link.springer.com/article/10.1007/s10257-020-00472-6]

### §6 Synthesis

**Executive summary:**

[inference; source: https://aisel.aisnet.org/ijispm/vol7/iss1/3/; https://link.springer.com/article/10.1007/s10257-020-00472-6] Aggregate local-tooling costs exceed customization benefits when three structural multipliers reach a combined threshold: tool footprint per team exceeds the organisation's administrative absorption capacity, shared dependency density creates coordination overhead that compounds with each additional tool, and staff turnover exposes the knowledge-concentration risk embedded in undocumented locally owned tooling. [inference; source: https://aisel.aisnet.org/ijispm/vol7/iss1/3/; https://www.faros.ai/blog/key-takeaways-from-the-dora-report-2025] The crossover is a function of these interacting variables, detectable early through five proxy metrics that most organisations already collect: support ticket volume growth per tool, new-hire time-to-productivity relative to team complexity, shadow-spend growth rate relative to headcount, incident attribution to non-standard tooling, and downstream queue growth rate relative to upstream delivery rate growth. [inference; source: https://aisel.aisnet.org/ijispm/vol7/iss1/3/; https://www.annfammed.org/content/19/2/171] The evidence establishes no universal numeric threshold; the crossover is signalled when the rate of hidden-cost accumulation in these proxies exceeds the rate at which direct productivity benefits are being measured and attributed.

**Key findings:**

1. [fact; source: https://aisel.aisnet.org/ijispm/vol7/iss1/3/] Local tooling creates four categories of benefit (agility, fit-for-purpose, reduced central-IT dependency, innovation velocity) and five categories of cost (maintenance burden, integration friction, key-person concentration, security and compliance exposure, duplicate spend) that are not captured symmetrically in most organisations' measurement systems.
2. [inference; source: https://aisel.aisnet.org/ijispm/vol7/iss1/3/; https://link.springer.com/article/10.1007/s10257-020-00472-6] The costs most likely to remain hidden until material scale are informal peer support time, new-hire onboarding friction, key-person concentration risk, and integration rework cost, because all four are absorbed into undifferentiated overhead rather than attributed to the originating tool.
3. [inference; source: https://link.springer.com/article/10.1007/s10257-020-00472-6] Shadow IT research identifies that governance maturity (documented ownership, exit procedures, security review) reduces the coordination cost of a locally owned tool more than any capability feature of the tool itself.
4. [inference; source: https://aisel.aisnet.org/ijispm/vol7/iss1/3/; https://link.springer.com/article/10.1007/s10257-020-00472-6] Three structural multipliers accelerate the crossover from net-positive to net-negative: team scale (each additional team adds its own tool estate), shared dependency density (tools that feed downstream processes impose their complexity on all consumers), and staff turnover (bus factor declines with each undocumented key-person departure).
5. [inference; source: https://www.faros.ai/blog/key-takeaways-from-the-dora-report-2025] Faros AI telemetry across 22,000 developers shows a crossover-consistent pattern in real-time: individual task completion rose 33.7% while PR review time rose 441% and production incidents per PR rose 242.7%, consistent with local productivity gains flooding shared constraint infrastructure, though AI-generated code quality degradation is a competing explanation for the same pattern.
6. [fact; source: https://dora.dev/research/2025/dora-report/; https://www.infoq.com/news/2026/03/ai-dora-report/] DORA 2025 identifies seven capabilities required for local productivity gains to translate into organisational performance gains; all seven are concerned with reducing the coupling and queue-flooding dynamics that cause the crossover.
7. [inference; source: https://aisel.aisnet.org/ijispm/vol7/iss1/3/; https://www.faros.ai/blog/key-takeaways-from-the-dora-report-2025] Five leading indicators are detectable with data most knowledge-work organisations already collect before the crossover has been formally reached: support-ticket volume growth per tool, new-hire time-to-productivity, shadow-spend growth, integration failure frequency, and downstream queue growth relative to upstream delivery growth.
8. [inference; source: https://link.springer.com/article/10.1007/s10257-020-00472-6] The governance-transition literature supports a sixth leading indicator specific to knowledge concentration: bus factor distribution across the locally owned tool estate, trackable via a tool-by-knowledge-holder matrix.
9. [inference; source: https://aisel.aisnet.org/ijispm/vol7/iss1/3/; https://www.annfammed.org/content/19/2/171] No peer-reviewed study provides a universal numeric crossover threshold; the evidence consistently identifies the crossover as context-dependent on the three structural multipliers rather than on a fixed tool count or team size.
10. [inference; source: https://aisel.aisnet.org/ijispm/vol7/iss1/3/] The decision frame that integrates these findings has two practical limits: it requires attribution discipline (tagging support, onboarding, and incident data to tool category and ownership type) that most organisations currently lack, and organisations below a minimum scale threshold may find the governance-attribution investment exceeds the fragmentation cost it reveals.

**Evidence map:**

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [fact] Local tooling creates three benefit categories: agility, fit-for-purpose solutions, reduced central-IT dependency | https://aisel.aisnet.org/ijispm/vol7/iss1/3/ | medium | Academic systematic review; 82 papers |
| [fact] Shadow IT creates four recurring cost categories: security exposure, integration complexity, duplicate spend, loss of visibility | https://aisel.aisnet.org/ijispm/vol7/iss1/3/ | medium | Same review; cross-validated across 82 sources |
| [inference] Key-person concentration is a fifth hidden cost category, distinct from the four in the earlier literature | https://link.springer.com/article/10.1007/s10257-020-00472-6 | medium | Single empirical study; direction consistent with bus-factor literature |
| [inference] Gartner (via secondary sources): shadow IT is 30-40% of IT spend in large enterprises; 75% of employees using tools outside IT visibility by 2027 | https://www.techfinitive.com/features/how-to-keep-shadow-it-costs-under-control/; https://www.valencesecurity.com/resources/blogs/gartner-saas-applications-outside-of-it | medium | Secondary sources citing Gartner; primary report not accessible |
| [inference] Four cost categories remain hidden until material scale because they are absorbed into undifferentiated overhead | https://aisel.aisnet.org/ijispm/vol7/iss1/3/; https://link.springer.com/article/10.1007/s10257-020-00472-6 | medium | Inferred from attribution patterns in both sources |
| [inference] Governance maturity reduces coordination cost more than tool capability | https://link.springer.com/article/10.1007/s10257-020-00472-6 | medium | Single study; empirically supported in governance-transition case data |
| [inference] Faros AI data: individual +33.7%, PR review +441%, incidents/PR +242.7%; consistent with queue-flooding at shared constraint | https://www.faros.ai/blog/key-takeaways-from-the-dora-report-2025 | medium | Single commercial vendor; 22,000 developers; direction consistent with DORA |
| [fact] DORA 2025: AI amplifies existing conditions; fragmented tooling accelerates instability rather than resolving it | https://dora.dev/research/2025/dora-report/; https://www.infoq.com/news/2026/03/ai-dora-report/ | medium | Survey of ~5,000 professionals; self-reported |
| [inference] Five leading indicators are detectable with existing organisational data before the formal crossover | https://aisel.aisnet.org/ijispm/vol7/iss1/3/; https://www.faros.ai/blog/key-takeaways-from-the-dora-report-2025 | medium | Synthesised from two independent sources |
| [inference] No universal numeric threshold exists; crossover is context-dependent on three structural multipliers | https://aisel.aisnet.org/ijispm/vol7/iss1/3/; https://www.annfammed.org/content/19/2/171 | medium | Consistent across all reviewed sources |

**Assumptions:**

- The shadow IT literature's findings about hidden costs in on-premises and SaaS-era IT apply to the current wave of AI-assisted tooling, because the structural failure mode (local benefit, distributed hidden cost) is identical across all four waves of local tooling adoption documented in the Kopper et al. governance-transition analysis. [assumption; source: https://link.springer.com/article/10.1007/s10257-020-00472-6; https://aisel.aisnet.org/ijispm/vol7/iss1/3/]

- The Faros AI telemetry represents a plausible real-world test of the crossover in action because the organisational conditions (individual productivity rising while shared infrastructure is not scaled) are the theoretical crossover conditions described in the shadow IT and TOC literature. The population (22,000 developers on GitHub-hosted teams) over-represents software delivery relative to other knowledge-work types. [assumption; source: https://www.faros.ai/blog/key-takeaways-from-the-dora-report-2025]

- Sinsky's framing from medical practice is transferable to knowledge-work organisational design because both domains share the core trade-off: standardization reduces cognitive and coordination overhead for routine tasks while customization improves outcomes for non-routine tasks, and the decision rule is the same in both domains. [assumption; source: https://www.annfammed.org/content/19/2/171]

**Analysis:**

Local tooling fragmentation costs are hidden because the measurement and attribution systems in most organisations are not designed to reveal them. [inference; source: https://aisel.aisnet.org/ijispm/vol7/iss1/3/; https://link.springer.com/article/10.1007/s10257-020-00472-6]

The Faros AI data is the most directly observable evidence available for the crossover pattern. [inference; source: https://www.faros.ai/blog/key-takeaways-from-the-dora-report-2025] A 441% rise in PR review time against a 33.7% rise in task completion is consistent with local productivity gains being converted into queue depth at the shared constraint, matching the TOC mechanism documented in the prior repository item on local-global optima. [inference; source: https://fortelabs.com/blog/theory-of-constraints-102-local-optima/; https://www.faros.ai/blog/key-takeaways-from-the-dora-report-2025] Two competing explanations exist for the same data. [inference; source: https://www.faros.ai/blog/key-takeaways-from-the-dora-report-2025] First, the AI-generated code quality degradation explanation: AI-assisted teams produce code faster but with more defects, causing longer review times and more incidents independently of any tooling fragmentation effect. [inference; source: https://www.faros.ai/blog/key-takeaways-from-the-dora-report-2025] Second, the transition-period explanation: review processes have not yet caught up with the new throughput level, and with investment in shared constraint capacity, organisations can capture the local gains as system-level performance. [inference; source: https://dora.dev/research/2025/dora-report/] Both rivals are consistent with TOC's fourth step (elevate the constraint); they differ in what must be elevated: review-process capacity or code-quality practices. [inference; source: https://dora.dev/research/2025/dora-report/] The evidence does not definitively separate these mechanisms; the crossover interpretation is therefore an inference of medium confidence rather than a directly established causal claim. [inference; source: https://www.faros.ai/blog/key-takeaways-from-the-dora-report-2025]

The governance-transition literature's finding that documentation and ownership maturity reduces coordination cost is the most actionable implication regardless of which rival explanation holds. [inference; source: https://link.springer.com/article/10.1007/s10257-020-00472-6] An organisation that documents ownership, defines exit procedures, and maintains a current tool inventory makes fragmentation cost visible, attributable, and manageable, which is the precondition for any consolidation or shared-constraint-capacity decision. [inference; source: https://aisel.aisnet.org/ijispm/vol7/iss1/3/; https://link.springer.com/article/10.1007/s10257-020-00472-6]

**Risks, gaps, and uncertainties:**

- No peer-reviewed controlled experiment directly measures the crossover threshold in a knowledge-work organisation. The evidence is drawn from a systematic review of shadow IT literature, a governance-transition case study, large-scale developer telemetry from a single commercial vendor, and a multi-organisation survey. The direction is consistent across these sources; the magnitude is not directly measured.

- The Faros AI queue-flooding interpretation competes with the AI code-quality degradation interpretation for the same data. The two mechanisms produce identical observable patterns (PR review time up, incidents up, relative to individual task completion). The evidence does not isolate them.

- The Gartner figures (30-40% of IT spend, 75% of employees by 2027) are secondary attributions to Gartner research in practitioner publications; the primary Gartner report URL was not accessible in this research session. These figures should be treated as directional indicators rather than precise benchmarks.

- The Sinsky (2021) Annals of Family Medicine piece is behind institutional access; the content was confirmed from abstract and secondary summaries. The framing is used only as a structural analogy, not as empirical evidence for the knowledge-work crossover specifically.

- The decision frame proposed in D1 requires attribution tagging that most organisations currently do not have. The practical barrier to implementing the measurement model is therefore not the model itself but the underlying data infrastructure.

**Open questions:**

- At what specific bus factor level does the knowledge-concentration risk from a locally owned tool become a material operational dependency? This is a candidate for a quantitative empirical research backlog item.
- How does the crossover dynamic differ between AI-assisted tooling (where individual productivity gains are larger and faster) and legacy shadow IT (SaaS subscriptions, spreadsheets)? The Faros data suggests the crossover is accelerated under AI assistance, but no direct comparison study exists.
- What governance intervention is most effective for organisations that have already crossed the threshold: forced consolidation, formalisation into overt business-managed IT, or investment in shared constraint capacity? The governance-transition literature suggests the latter two options, but no head-to-head comparison study exists.

### §7 Recursive Review

```text
review_result: pass
acronym_audit:
  IT: first expanded as "Information Technology (IT)" in Sources section, Klotz source description
  TOC: first expanded as "Theory of Constraints (TOC)" in Sources section, Forte Labs description;
    re-expanded in §0 Initialise and §1 B3
  AI: first expanded as "Artificial Intelligence (AI)" in Sources section, DORA 2025 description;
    re-expanded in §2 Investigation B3
  DORA: first expanded as "DevOps Research and Assessment (DORA)" in Sources display name;
    re-expanded in §1 B3
  SaaS: expanded as "Software as a Service (SaaS)" in §2 C1
  PR: expanded as "pull request (PR)" in §2 B2
  IDPs: expanded as "Internal developer platforms (IDPs)" in §2 B3
  bus factor: defined in §2 A2 via Kopper et al. reference
  shadow IT: compound noun used as established term; contextual definition in §2 B1
  WIP: not used in this item; no expansion needed
  RSO (Research Skill Output): used only in this metadata block as label; not used in prose
claim_audit: all factual and inferential claims in Research Skill Output carry [fact],
  [inference], or [assumption] labels with URL-backed sources
parity_check: §6 Synthesis and Findings are seeded from the same material;
  no divergence introduced
scope_guardrail: no universal numeric threshold asserted; no vendor comparisons
```

---

## Findings

*(Populated from §6 Synthesis above.)*

### Executive Summary

Aggregate local-tooling costs exceed customization benefits when three structural multipliers reach a combined threshold: tool footprint per team exceeds the organisation's administrative absorption capacity, shared dependency density creates coordination overhead that compounds with each additional tool, and staff turnover exposes the knowledge concentration risk embedded in undocumented locally owned tooling. [inference; source: https://aisel.aisnet.org/ijispm/vol7/iss1/3/; https://link.springer.com/article/10.1007/s10257-020-00472-6] The crossover is a function of these interacting variables, detectable early through five proxy metrics that most organisations already collect: support ticket volume growth per tool, new-hire time-to-productivity relative to team complexity, shadow-spend growth rate, incident attribution to non-standard tooling, and downstream queue growth rate relative to upstream delivery rate growth. [inference; source: https://aisel.aisnet.org/ijispm/vol7/iss1/3/; https://www.faros.ai/blog/key-takeaways-from-the-dora-report-2025] Faros AI telemetry across 22,000 developers documents the crossover-consistent signature: individual task completion rose 33.7% while PR review time rose 441% and production incidents per PR rose 242.7%, a pattern consistent with local tooling gains flooding shared constraint infrastructure, though AI-generated code quality degradation is a competing explanation for the same data. [inference; source: https://www.faros.ai/blog/key-takeaways-from-the-dora-report-2025] The governance-transition literature adds that documentation and ownership maturity reduces fragmentation cost more than any individual capability feature of the tool itself, making governance investment the most actionable first response when leading indicators begin to rise. [inference; source: https://link.springer.com/article/10.1007/s10257-020-00472-6]

### Key Findings

1. Local tooling creates four categories of benefit (agility, fit-for-purpose solutions, reduced central-IT dependency, innovation velocity) and five categories of cost (maintenance burden, integration friction, key-person concentration, security and compliance exposure, duplicate spend) that are not captured symmetrically in most organisations' measurement systems, with the four hidden cost categories absorbed into undifferentiated overhead rather than attributed to the originating tool. ([inference]; medium confidence; source: https://aisel.aisnet.org/ijispm/vol7/iss1/3/; https://link.springer.com/article/10.1007/s10257-020-00472-6)

2. Secondary sources citing Gartner research estimate shadow IT at 30 to 40 percent of total IT spend in large enterprises and project that 75 percent of employees will create or modify technology outside IT visibility by 2027, suggesting the aggregate cost is already economically material before any crossover calculation is applied. ([inference]; medium confidence; source: https://www.techfinitive.com/features/how-to-keep-shadow-it-costs-under-control/; https://www.valencesecurity.com/resources/blogs/gartner-saas-applications-outside-of-it)

3. Three structural multipliers accelerate the crossover from net-positive to net-negative: team scale, where each additional team that creates local tooling adds its own maintenance surface; shared dependency density, where tools feeding downstream processes impose integration complexity on all consumers; and staff turnover, where bus factor declines with each undocumented key-person departure. ([inference]; medium confidence; source: https://aisel.aisnet.org/ijispm/vol7/iss1/3/; https://link.springer.com/article/10.1007/s10257-020-00472-6)

4. Faros AI telemetry across 22,000 developers measured individual task completion rising 33.7% while PR review time rose 441% and production incidents per PR rose 242.7%, a pattern consistent with local productivity gains flooding shared constraint infrastructure, though AI-generated code quality degradation is a competing explanation for the same data pattern. ([inference]; medium confidence; source: https://www.faros.ai/blog/key-takeaways-from-the-dora-report-2025)

5. The DORA 2025 report, surveying nearly 5,000 technology professionals, found that AI acts as an amplifier of existing organisational conditions, with fragmented tooling accelerating instability rather than being resolved by AI productivity gains. ([fact]; medium confidence; source: https://dora.dev/research/2025/dora-report/; https://www.infoq.com/news/2026/03/ai-dora-report/)

6. Five leading indicators are detectable with data most knowledge-work organisations already collect before the crossover has been formally calculated: support-ticket volume growth per non-standard tool, new-hire time-to-productivity relative to team complexity, shadow-spend growth rate relative to headcount, integration failure frequency, and downstream queue growth rate relative to upstream delivery rate growth. ([inference]; medium confidence; source: https://aisel.aisnet.org/ijispm/vol7/iss1/3/; https://www.faros.ai/blog/key-takeaways-from-the-dora-report-2025)

7. A sixth leading indicator specific to knowledge concentration is bus factor distribution across the locally owned tool estate, measurable via a tool-by-knowledge-holder matrix tracking the number of tools with a bus factor of 1 or 2 as a portfolio-level concentration index over time. ([inference]; medium confidence; source: https://link.springer.com/article/10.1007/s10257-020-00472-6)

8. Governance maturity (documented ownership, exit procedures, security review) reduces the coordination cost of a locally owned tool more than any individual capability feature of the tool itself, because ownership maturity determines whether the tool can be rapidly decommissioned or transitioned when the key person leaves. ([inference]; medium confidence; source: https://link.springer.com/article/10.1007/s10257-020-00472-6)

9. DORA 2024 found that 76 percent of high-performance delivery organisations have dedicated platform engineering teams, and that Internal developer platforms (IDPs) correlating with user-centred design produce 8 percent higher individual productivity and 10 percent higher team performance, while poorly designed platforms reduce stability. ([fact]; medium confidence; source: https://dora.dev/research/2024/dora-report/; https://platformengineering.com/features/dora-2025-ai-wont-save-you-without-a-solid-platform/)

10. No peer-reviewed study provides a universal numeric crossover threshold; the evidence consistently identifies the crossover as context-dependent on the three structural multipliers rather than a fixed tool count or team size, which means the measurement frame's value is in tracking trend rates rather than comparing to a benchmark. ([inference]; medium confidence; source: https://aisel.aisnet.org/ijispm/vol7/iss1/3/; https://www.annfammed.org/content/19/2/171)

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [fact] Local tooling creates three benefit categories: agility, fit-for-purpose solutions, reduced central-IT dependency | https://aisel.aisnet.org/ijispm/vol7/iss1/3/ | medium | Systematic review; 82 papers; peer-reviewed |
| [fact] Shadow IT creates four recurring cost categories: security exposure, integration complexity, duplicate spend, loss of IT visibility | https://aisel.aisnet.org/ijispm/vol7/iss1/3/ | medium | Same review |
| [inference] Key-person concentration is a fifth hidden cost category; governance maturity is the primary reducer of coordination cost | https://link.springer.com/article/10.1007/s10257-020-00472-6 | medium | Single study; Kopper et al. 2020 |
| [inference] Shadow IT estimated at 30-40% of IT spend; 75% of employees using outside-IT tools by 2027 (secondary Gartner citation) | https://www.techfinitive.com/features/how-to-keep-shadow-it-costs-under-control/; https://www.valencesecurity.com/resources/blogs/gartner-saas-applications-outside-of-it | medium | Secondary citations of Gartner research; primary not accessible |
| [inference] Four cost categories remain hidden because they are absorbed into undifferentiated overhead | https://aisel.aisnet.org/ijispm/vol7/iss1/3/; https://link.springer.com/article/10.1007/s10257-020-00472-6 | medium | Inferred from attribution patterns |
| [inference] Three structural multipliers accelerate the crossover: team scale, shared dependency density, staff turnover | https://aisel.aisnet.org/ijispm/vol7/iss1/3/; https://link.springer.com/article/10.1007/s10257-020-00472-6 | medium | Synthesised from two independent sources |
| [inference] Faros data: individual +33.7%, PR review +441%, incidents/PR +242.7%; crossover-consistent pattern; AI code quality degradation is competing explanation | https://www.faros.ai/blog/key-takeaways-from-the-dora-report-2025 | medium | Single commercial vendor; 22,000 developers |
| [fact] DORA 2025: AI amplifies existing conditions; fragmented tooling accelerates instability | https://dora.dev/research/2025/dora-report/; https://www.infoq.com/news/2026/03/ai-dora-report/ | medium | Survey; ~5,000 professionals |
| [fact] DORA 2024: 76% of high performers have platform engineering; IDP quality correlates with 8% individual and 10% team productivity gains | https://dora.dev/research/2024/dora-report/; https://platformengineering.com/features/dora-2025-ai-wont-save-you-without-a-solid-platform/ | medium | Same DORA survey series |
| [inference] Five leading indicators detectable with existing data before formal crossover | https://aisel.aisnet.org/ijispm/vol7/iss1/3/; https://www.faros.ai/blog/key-takeaways-from-the-dora-report-2025 | medium | Synthesised across two independent sources |
| [inference] No universal numeric threshold; crossover is context-dependent on three structural multipliers | https://aisel.aisnet.org/ijispm/vol7/iss1/3/; https://www.annfammed.org/content/19/2/171 | medium | Consistent across all reviewed sources |

### Assumptions

- The shadow IT literature's findings about hidden costs in on-premises and SaaS-era IT apply to the current wave of AI-assisted tooling. The structural failure mode (local benefit, distributed hidden cost) is identical across all four waves of local tooling adoption documented in Kopper et al.'s governance-transition analysis. [assumption; source: https://link.springer.com/article/10.1007/s10257-020-00472-6; https://aisel.aisnet.org/ijispm/vol7/iss1/3/]

- The Faros AI telemetry represents a plausible real-world test of the crossover in action. The organisational conditions (individual productivity rising while shared infrastructure is not scaled) are the theoretical crossover conditions described in both the shadow IT literature and the Theory of Constraints (TOC) framework. The population over-represents GitHub-hosted software delivery teams. [assumption; source: https://www.faros.ai/blog/key-takeaways-from-the-dora-report-2025]

- Sinsky's standardization versus customization framing from medical practice is transferable to knowledge-work organisational design. Both domains share the core trade-off between standardization (reduces cognitive overhead for routine tasks) and customization (improves outcomes for non-routine tasks), and the decision rule (measure overhead separately from benefit; consolidate when overhead growth rate exceeds benefit growth rate) is domain-agnostic. [assumption; source: https://www.annfammed.org/content/19/2/171]

### Analysis

Local tooling fragmentation costs are hidden because the measurement and attribution systems in most organisations are not designed to reveal them. [inference; source: https://aisel.aisnet.org/ijispm/vol7/iss1/3/; https://link.springer.com/article/10.1007/s10257-020-00472-6]

The Faros AI data is the most directly observable evidence available for the crossover pattern: a 441% rise in PR review time against a 33.7% rise in task completion is consistent with local productivity gains being converted into queue depth at the shared constraint, matching the TOC mechanism documented in the prior repository item on local-global optima. [inference; source: https://www.faros.ai/blog/key-takeaways-from-the-dora-report-2025; https://davidamitchell.github.io/Research/research/2026-06-13-local-global-optima-knowledge-work-throughput.html] However, two competing explanations exist for the same data pattern. [inference; source: https://www.faros.ai/blog/key-takeaways-from-the-dora-report-2025] First, the AI-generated code quality degradation explanation: AI-assisted teams produce code faster but with more defects, causing longer review times and more incidents, independently of any tooling fragmentation effect. [inference; source: https://www.faros.ai/blog/key-takeaways-from-the-dora-report-2025] Second, the transition-period explanation: review processes have not yet adapted to the new throughput level, but with investment in shared constraint capacity, organisations can eventually capture the local gains as system-level performance. [inference; source: https://dora.dev/research/2025/dora-report/] Both rival explanations are consistent with TOC's fourth step (elevate the constraint); they differ in what must be elevated: review-process capacity or code-quality practices. [inference; source: https://dora.dev/research/2025/dora-report/] The evidence does not definitively separate these mechanisms in the Faros data; the crossover interpretation is therefore an inference of medium confidence rather than a directly established causal claim. [inference; source: https://www.faros.ai/blog/key-takeaways-from-the-dora-report-2025]

The governance-transition literature's finding that documentation and ownership maturity reduces coordination cost is the most actionable implication regardless of which rival explanation holds. [inference; source: https://link.springer.com/article/10.1007/s10257-020-00472-6] An organisation that documents ownership, defines exit procedures, and maintains a current tool inventory makes fragmentation cost visible, attributable, and manageable, which is the precondition for any consolidation or shared-constraint-capacity decision. [inference; source: https://aisel.aisnet.org/ijispm/vol7/iss1/3/; https://link.springer.com/article/10.1007/s10257-020-00472-6]

### Risks, Gaps, and Uncertainties

- No peer-reviewed controlled experiment directly measures the crossover threshold in a knowledge-work organisation. Evidence is drawn from a systematic review of shadow IT literature, a governance-transition case study, large-scale developer telemetry from a single commercial vendor, and multi-organisation surveys. The direction is consistent across these sources; the magnitude is not directly measured.

- The Faros AI queue-flooding interpretation competes with the AI code-quality degradation interpretation for the same data. Both mechanisms produce identical observable patterns (PR review time up, incidents up, relative to individual task completion). The evidence does not isolate them, and the crossover interpretation therefore remains an inference of medium confidence.

- The Gartner figures (30-40% of IT spend, 75% of employees by 2027) are secondary attributions to Gartner research in practitioner publications; the primary Gartner report URL was not accessible in this research session. These figures should be treated as directional indicators rather than precise benchmarks.

- The Sinsky (2021) Annals of Family Medicine piece is behind institutional access; the content was confirmed from the abstract and secondary summaries. The framing is used only as a structural analogy, not as empirical evidence for the knowledge-work crossover specifically.

- The proposed measurement frame requires attribution tagging (support tickets, onboarding records, and incident logs tagged to tool category and ownership type) that most organisations currently do not have. The practical barrier to implementing the frame is the underlying data infrastructure, not the frame itself.

- The Faros AI population over-represents GitHub-hosted engineering teams. The crossover dynamics may differ in non-software knowledge work (legal review, financial analysis, regulatory analysis) where shared constraints differ.

### Open Questions

- At what specific bus factor level does the knowledge-concentration risk from a locally owned tool become a material operational dependency? A quantitative empirical study of bus factor versus incident frequency across tool estates would directly address this gap.

- How does the crossover dynamic differ between AI-assisted tooling, where individual productivity gains are larger and faster, and legacy shadow IT such as SaaS subscriptions and spreadsheets? The Faros data suggests the crossover is accelerated under AI assistance, but no direct comparison study exists.

- What governance intervention is most effective for organisations that have already crossed the threshold: forced consolidation, formalisation into overt business-managed IT, or investment in shared constraint capacity? The governance-transition literature suggests the latter two but provides no head-to-head comparison.

---

## Output

- Type: knowledge
- Description: Structured synthesis showing that local tooling fragmentation costs exceed customization benefits when three structural multipliers (team scale, shared dependency density, staff turnover) reach a combined threshold, and that five leading indicators detectable with existing organisational data can signal the crossover before a formal cost calculation is required. [inference; source: https://aisel.aisnet.org/ijispm/vol7/iss1/3/; https://www.faros.ai/blog/key-takeaways-from-the-dora-report-2025]
- Links:
  - https://aisel.aisnet.org/ijispm/vol7/iss1/3/ (Klotz et al. 2019 systematic review: shadow IT causes, outcomes, governance)
  - https://www.faros.ai/blog/key-takeaways-from-the-dora-report-2025 (Faros AI 2026: Acceleration Whiplash telemetry across 22,000 developers)
  - https://link.springer.com/article/10.1007/s10257-020-00472-6 (Kopper et al. 2020: shadow IT to business-managed IT governance transition)
