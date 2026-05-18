---
title: "Longitudinal persistence rates after gap closure for low-code applications, bots, and agents"
added: 2026-05-17T20:40:49+00:00
status: reviewing
priority: high
blocks: []
tags: [organisation, workflow, analytics, agentic-ai]
started: 2026-05-18T12:06:11+00:00
completed: ~
output: [knowledge]
cites:
  - 2026-05-16-do-mode-demand-persistence-and-build-mode-displacement
  - 2026-05-16-decommission-trigger-design-for-do-mode-agents
  - 2026-05-14-citizen-development-rollout-empirical-evidence
  - 2026-05-17-manual-workaround-to-central-it-backlog-conversion-datasets
related:
  - 2026-04-26-ai-lowcode-risk-tier-classification-controls
  - 2026-04-26-systems-capability-debt-agentic-ai-risk-synthesis
superseded_by: ~
supersedes: ~
item_type: primary
confidence: low
versions: []
---

# Longitudinal persistence rates after gap closure for low-code applications, bots, and agents

## Research Question

What longitudinal evidence exists on post-gap-closure persistence rates for low-code applications, bots, and agents in live enterprise estates?

## Scope

**In scope:**
- Empirical evidence on retention, abandonment, replacement, or stabilisation of low-code applications, bots, and agents after the original process gap is addressed
- Persistence measurement windows, for example 3, 6, 12, and 24 months
- Comparisons across governance maturity levels and ownership models

**Out of scope:**
- Product feature comparisons between low-code or bot platforms
- Single anecdotal case studies without reusable measurement definitions

**Constraints:** Focus on sources that disclose sample period, cohort definition, and survival or persistence calculation method.

## Context

Organisations cannot tell whether fast-gap automations have become durable capabilities or unmanaged legacy surfaces unless they can observe whether those assets remain active after an equivalent governed capability exists. [inference; source: https://davidamitchell.github.io/Research/research/2026-05-16-do-mode-demand-persistence-and-build-mode-displacement.html; https://davidamitchell.github.io/Research/research/2026-05-16-decommission-trigger-design-for-do-mode-agents.html; https://learn.microsoft.com/en-us/power-platform/admin/power-platform-inventory]

## Approach

1. Identify studies and operational datasets that track low-code, bot, and agent assets after initial gap closure.
2. Extract and normalise persistence definitions, including active use, maintained ownership, incident-free operation, or retirement status.
3. Compare persistence outcomes by governance controls, platform type, and ownership model.

## Sources

- [x] [Microsoft Learn (2026) Power Platform Center of Excellence (CoE) Starter Kit](https://learn.microsoft.com/en-us/power-platform/guidance/coe/starter-kit) - official Microsoft statement that governance, inventory, usage, monitoring, and actions are now native admin-center capabilities
- [x] [UiPath (2026) Automation Ops overview](https://docs.uipath.com/automation-ops/automation-cloud/latest/user-guide/about-automation-ops) - official centralized governance, source-control, and solution-management surface
- [ ] [Forrester (2023) The Forrester Wave: Low-Code Development Platforms For Professional Developers, Q2 2023](https://www.forrester.com/report/the-forrester-wave-low-code-development-platforms-for-professional-developers-q2-2023/RES177705) - seeded page checked; login wall and unrelated summary text, not used for downstream claims
- [ ] [Institute of Electrical and Electronics Engineers (IEEE) Computer Society (2026) Software evolution resources](https://www.computer.org/technical-committees/software-engineering/resources/software-evolution) - seeded page checked; navigation shell only, not used for downstream claims
- [x] [Microsoft Learn (2026) Power Platform inventory](https://learn.microsoft.com/en-us/power-platform/admin/power-platform-inventory) - tenant-wide inventory for agents, apps, flows, owners, and filters
- [x] [Microsoft Learn (2026) Power Platform inventory schema reference](https://learn.microsoft.com/en-us/power-platform/admin/inventory-schema) - created, owner, modified, and workflow fields for inventory queries
- [x] [Microsoft Learn (2026) Collect audit logs using Microsoft Graph Application Programming Interface (API)](https://learn.microsoft.com/en-us/power-platform/guidance/coe/setup-auditlog-http-graphapi) - usage telemetry such as launches and unique users
- [x] [Microsoft Learn (2026) Governance components](https://learn.microsoft.com/en-us/power-platform/guidance/coe/governance-components) - business justification, business impact, dependencies, and inactivity-approval tables
- [x] [Microsoft Learn (2026) Set up inactivity notifications components](https://learn.microsoft.com/en-us/power-platform/guidance/coe/setup-archive-components) - six-month inactivity, approvals, and optional deletion
- [x] [UiPath (2026) Automation Hub deleting data](https://docs.uipath.com/automation-hub/automation-cloud/latest/user-guide/deleting-data) - dependency-aware deletion restriction for App Inventory entries
- [x] [UiPath (2026) Customize idea flows](https://docs.uipath.com/automation-hub/automation-suite/2.2510/user-guide/customize-idea-flows) - disable-for-action control that can stop new intake while preserving existing configuration
- [x] [Pega (2021) When is it time to retire your Robotic Process Automation (RPA) bots?](https://community.pega.com/blog/when-it-time-retire-your-rpa-bots) - official retirement and end-of-life guidance for bots layered on legacy systems
- [x] [Binzer et al. (2024) Establishing a Low-Code/No-Code-Enabled Citizen Development Strategy](https://aisel.aisnet.org/misqe/vol23/iss3/3/) - 24-company empirical strategy study
- [x] [Viljoen et al. (2024) Governing Citizen Development to Address Low-Code Platform Challenges](https://aisel.aisnet.org/misqe/vol23/iss3/6/) - 30-interview governance study
- [x] [Ajimati et al. (2025) Adoption of low-code and no-code development](https://research.universityofgalway.ie/en/publications/adoption-of-low-code-and-no-code-development-a-systematic-literat-6/) - systematic literature review of 40 primary studies
- [x] [Mitchell (2026) Temporary Automation Demand Persistence and Core Capability Investment Displacement](https://davidamitchell.github.io/Research/research/2026-05-16-do-mode-demand-persistence-and-build-mode-displacement.html) - prior completed repository item on persistence evidence and displacement risk
- [x] [Mitchell (2026) Decommission Trigger Design for Temporary Bridge Agents](https://davidamitchell.github.io/Research/research/2026-05-16-decommission-trigger-design-for-do-mode-agents.html) - prior completed repository item on machine-observable retirement triggers
- [x] [Mitchell (2026) Empirical evidence on rollout of organisation-wide low-code and no-code programs](https://davidamitchell.github.io/Research/research/2026-05-14-citizen-development-rollout-empirical-evidence.html) - prior completed repository item on rollout evidence and governance limits
- [x] [Mitchell (2026) Datasets for measuring conversion from demand for local workaround tools to central Information Technology backlog items](https://davidamitchell.github.io/Research/research/2026-05-17-manual-workaround-to-central-it-backlog-conversion-datasets.html) - prior completed repository item on join design, denominator discipline, and telemetry fields

---

## Research Skill Output

*(Full output from running the research skill, retained verbatim in the completed item. Sections 0 to 5 are the investigation, and section 6 seeds the Findings section below.)*

### §0 Initialise

- Question: What longitudinal evidence exists on post-gap-closure persistence rates for low-code applications, bots, and agents in live enterprise estates?
- Scope: accessible empirical studies, official lifecycle and telemetry surfaces, persistence-window design, and comparisons across governance maturity and ownership models.
- Constraints: prefer official and empirical sources, use URL-backed citations only, and separate measurable persistence evidence from governance guidance or unsupported absence claims.
- Output: full structured synthesis with executive summary, key findings, evidence map, assumptions, analysis, risks, gaps, uncertainties, open questions, and output details.
- Mode: full.
- [fact; source: https://davidamitchell.github.io/Research/research/2026-05-16-do-mode-demand-persistence-and-build-mode-displacement.html; https://davidamitchell.github.io/Research/research/2026-05-16-decommission-trigger-design-for-do-mode-agents.html; https://davidamitchell.github.io/Research/research/2026-05-14-citizen-development-rollout-empirical-evidence.html; https://davidamitchell.github.io/Research/research/2026-05-17-manual-workaround-to-central-it-backlog-conversion-datasets.html] Prior completed-item sweep found four directly relevant completed items covering persistence risk, decommission triggers, citizen-development governance evidence, and measurement-dataset design.
- [assumption; source: https://davidamitchell.github.io/Research/research/2026-05-16-do-mode-demand-persistence-and-build-mode-displacement.html; https://davidamitchell.github.io/Research/research/2026-05-16-decommission-trigger-design-for-do-mode-agents.html; https://learn.microsoft.com/en-us/power-platform/admin/power-platform-inventory] Working definition: post-gap-closure persistence means an app, bot, or agent remains present, active, or administratively maintained after an equivalent governed capability is available in the target operating environment.
- [assumption; source: https://learn.microsoft.com/en-us/power-platform/admin/inventory-schema; https://learn.microsoft.com/en-us/power-platform/guidance/coe/setup-auditlog-http-graphapi; https://docs.uipath.com/automation-hub/automation-cloud/latest/user-guide/deleting-data] Working measurement rule: persistence is only measurable when inventory state, owner state, activity state, and retirement or deletion state are all observable over time for the same asset identifier.

### §1 Question Decomposition

- **Root question:** What public longitudinal evidence actually exists for persistence after gap closure, and what can be measured reliably when public evidence is thin?
- **A. Direct public evidence**
  - A1. Do accessible empirical studies publish post-gap-closure persistence or survival rates for low-code applications, bots, or agents?
  - A2. If not, what do the accessible empirical studies say about governance, shadow assets, and technical debt that affect persistence?
- **B. Platform telemetry and lifecycle evidence**
  - B1. Which official Microsoft surfaces expose asset inventory, owner, timestamp, and usage data for low-code applications, flows, and agents?
  - B2. Which official Microsoft surfaces expose inactivity, approval, and deletion workflows?
  - B3. Which official UiPath surfaces expose centralized governance, intake shutdown, and dependency-aware deletion?
  - B4. Which official bot-lifecycle sources discuss explicit retirement or end-of-life planning?
- **C. Persistence-window design**
  - C1. Which windows can be operationalised from the observed telemetry surfaces?
  - C2. What makes comparisons across 3, 6, 12, and 24 months defensible or non-defensible?
- **D. Governance maturity and ownership**
  - D1. How does governance maturity change measurability of persistence?
  - D2. How do centrally governed, named-owner, or ad hoc maker-owned assets differ in measurability and likely persistence?
- **E. Synthesis**
  - E1. What is strongly supported by evidence?
  - E2. What remains uncertain or unsolved?

### §2 Investigation

- **Source-access notes**
  - Seeded Forrester URL -> login wall plus unrelated automation-portfolio summary text -> excluded from evidence set.
  - Seeded IEEE software-evolution URL -> navigation shell only -> excluded from evidence set.
  - Search record: `"post-gap-closure persistence rate" low-code`, `"RPA bot retirement rate after replacement"`, `"AI agent survival rate enterprise"`, `"low-code app decommission rate after system replacement"` -> no accessible public row-level dataset located.

- **A. Accessible public evidence is strongest on governance and lifecycle surfaces, not on published persistence rates**
  - [fact; source: https://aisel.aisnet.org/misqe/vol23/iss3/3/] Binzer et al. report evidence from 24 companies and say low-code and no-code platforms let employees with little or no Information Technology (IT) background quickly create digital solutions, while success depends on choices that address security, compliance, and organisational change.
  - [fact; source: https://aisel.aisnet.org/misqe/vol23/iss3/6/] Viljoen et al. report evidence from 30 interviews and say citizen development creates risks of substandard software quality, shadow IT, and technical debt without governance by technical experts and platform-specific controls.
  - [fact; source: https://research.universityofgalway.ie/en/publications/adoption-of-low-code-and-no-code-development-a-systematic-literat-6/] Ajimati et al. review 40 primary studies from 2017 to 2023 and conclude that low-code and no-code adoption broadens participation and speeds digital transformation while recurring governance and complexity challenges remain active concerns.
  - [inference; source: https://aisel.aisnet.org/misqe/vol23/iss3/3/; https://aisel.aisnet.org/misqe/vol23/iss3/6/; https://research.universityofgalway.ie/en/publications/adoption-of-low-code-and-no-code-development-a-systematic-literat-6/; https://davidamitchell.github.io/Research/research/2026-05-16-do-mode-demand-persistence-and-build-mode-displacement.html] None of the accessible empirical sources consulted publish a reusable post-gap-closure persistence or survival rate for enterprise low-code applications, bots, or agents.
  - [inference; source: https://aisel.aisnet.org/misqe/vol23/iss3/6/; https://research.universityofgalway.ie/en/publications/adoption-of-low-code-and-no-code-development-a-systematic-literat-6/; https://davidamitchell.github.io/Research/research/2026-05-14-citizen-development-rollout-empirical-evidence.html] The public empirical literature therefore supports persistence risk indirectly, through repeated evidence of shadow assets, technical debt, and governance strain, rather than through reported longitudinal retirement curves.

- **B. Microsoft now exposes the control surfaces needed to measure persistence internally**
  - [fact; source: https://learn.microsoft.com/en-us/power-platform/guidance/coe/starter-kit] Microsoft says the Center of Excellence (CoE) Starter Kit historically provided governance and visibility, and that these core capabilities now exist natively in the Power Platform admin center through Inventory, Usage, Monitor, and Actions.
  - [fact; source: https://learn.microsoft.com/en-us/power-platform/admin/power-platform-inventory] Microsoft Power Platform inventory provides tenant administrators with a unified view of agents, apps, and flows, includes created, updated, or deleted resources within 15 minutes, supports filtering by attributes such as owner and creation date, and explicitly advertises owner-departure detection to prevent orphaned agents.
  - [fact; source: https://learn.microsoft.com/en-us/power-platform/admin/inventory-schema] The PowerPlatformResources table exposes fields such as `properties.createdAt`, `properties.ownerId`, `properties.lastModifiedAt`, `properties.lastModifiedBy`, environment identifiers, and workflow entity identifiers across apps, flows, and agent-related resource types.
  - [fact; source: https://learn.microsoft.com/en-us/power-platform/guidance/coe/setup-auditlog-http-graphapi] The audit-log sync flows gather telemetry such as app launches and unique users, and Microsoft states that if those flows are not used, the related usage information is blank.
  - [fact; source: https://learn.microsoft.com/en-us/power-platform/guidance/coe/governance-components] Microsoft governance components track support details including Business Justification, Business Impact, Access Management, Dependencies, and mitigation-plan information, and maintain custom Dataverse tables for inactivity-notification approval tasks.
  - [fact; source: https://learn.microsoft.com/en-us/power-platform/guidance/coe/setup-archive-components; https://learn.microsoft.com/en-us/power-platform/guidance/coe/governance-components] Microsoft's inactivity process checks weekly for apps not modified or launched in the last six months by default, starts approval workflows, records approval tasks in Dataverse, and can delete approved inactive apps and flows through daily cleanup flows.
  - [inference; source: https://learn.microsoft.com/en-us/power-platform/admin/power-platform-inventory; https://learn.microsoft.com/en-us/power-platform/admin/inventory-schema; https://learn.microsoft.com/en-us/power-platform/guidance/coe/setup-auditlog-http-graphapi; https://learn.microsoft.com/en-us/power-platform/guidance/coe/setup-archive-components] Microsoft now exposes enough inventory, usage, ownership, and cleanup state to calculate internal persistence windows for low-code applications, flows, and agents, provided the organisation preserves historical snapshots rather than only the current state.

- **C. UiPath exposes governance and exit controls, but not public persistence benchmarks**
  - [fact; source: https://docs.uipath.com/automation-ops/automation-cloud/latest/user-guide/about-automation-ops] UiPath Automation Ops is a centralized web-based platform for governance policies, source control, feed management, and solution management.
  - [fact; source: https://docs.uipath.com/automation-hub/automation-suite/2.2510/user-guide/customize-idea-flows] UiPath Automation Hub lets administrators disable an idea flow for action, which removes that path from the submission options while preserving the underlying configuration.
  - [fact; source: https://docs.uipath.com/automation-hub/automation-cloud/latest/user-guide/deleting-data] UiPath restricts deletion to Account Owners and System Admins and refuses deletion of App Inventory entries when the application is still used in ideas or components.
  - [inference; source: https://docs.uipath.com/automation-ops/automation-cloud/latest/user-guide/about-automation-ops; https://docs.uipath.com/automation-hub/automation-suite/2.2510/user-guide/customize-idea-flows; https://docs.uipath.com/automation-hub/automation-cloud/latest/user-guide/deleting-data] UiPath's accessible official surfaces show centralized governance, intake shutdown, and dependency-aware exit controls, but they do not publish public longitudinal persistence or abandonment rates for bots or automations.

- **D. Official bot-retirement guidance treats persistence as a cost and lifecycle problem**
  - [fact; source: https://community.pega.com/blog/when-it-time-retire-your-rpa-bots] Pega says organisations often automate legacy processes on top of legacy systems, which means bot build, support, and upgrade costs are added to the continuing cost of the underlying systems.
  - [fact; source: https://community.pega.com/blog/when-it-time-retire-your-rpa-bots] Pega also says some customers do not build any Robotic Process Automation (RPA) bots without first having an end-of-life plan for each bot and recommends decomposing automated work to find overlap that should be eliminated or rebuilt more durably through Application Programming Interfaces (APIs) or other digital processes.
  - [inference; source: https://community.pega.com/blog/when-it-time-retire-your-rpa-bots; https://davidamitchell.github.io/Research/research/2026-05-16-decommission-trigger-design-for-do-mode-agents.html] The strongest accessible bot-lifecycle evidence supports explicit retirement planning and dependency elimination, not a published survival rate.

- **E. Governance maturity and ownership model determine whether persistence can be measured and controlled**
  - [fact; source: https://aisel.aisnet.org/misqe/vol23/iss3/6/; https://research.universityofgalway.ie/en/publications/adoption-of-low-code-and-no-code-development-a-systematic-literat-6/] The academic low-code evidence repeatedly identifies shadow IT, technical debt, and governance problems as recurring outcomes when business-user development is weakly governed.
  - [fact; source: https://learn.microsoft.com/en-us/power-platform/admin/power-platform-inventory; https://learn.microsoft.com/en-us/power-platform/guidance/coe/governance-components; https://learn.microsoft.com/en-us/power-platform/guidance/coe/setup-archive-components] Microsoft's official model ties measurability to named owners, inventory, usage telemetry, business justification, dependencies, and approval or deletion workflows.
  - [fact; source: https://docs.uipath.com/automation-hub/automation-cloud/latest/user-guide/deleting-data; https://docs.uipath.com/automation-hub/automation-suite/2.2510/user-guide/customize-idea-flows] UiPath's official model likewise ties control to administrative roles, dependency-aware deletion, and centrally managed intake flows.
  - [inference; source: https://aisel.aisnet.org/misqe/vol23/iss3/6/; https://learn.microsoft.com/en-us/power-platform/admin/power-platform-inventory; https://learn.microsoft.com/en-us/power-platform/guidance/coe/setup-archive-components; https://docs.uipath.com/automation-hub/automation-cloud/latest/user-guide/deleting-data] Mature governance does not prove lower persistence, but it does make persistence observable and decommissionable, whereas ad hoc maker-owned or ownerless assets are more likely to persist opaquely because neither denominator nor exit state is reliably captured.

- **F. The defensible measurement windows are operational rather than benchmark-driven**
  - [fact; source: https://learn.microsoft.com/en-us/power-platform/guidance/coe/setup-archive-components] Microsoft sets the default inactivity horizon for cleanup review at six months.
  - [fact; source: https://learn.microsoft.com/en-us/power-platform/admin/power-platform-inventory; https://learn.microsoft.com/en-us/power-platform/admin/inventory-schema] Microsoft inventory exposes created and modified timestamps that allow shorter and longer windows to be constructed from the same underlying records.
  - [inference; source: https://learn.microsoft.com/en-us/power-platform/guidance/coe/setup-archive-components; https://learn.microsoft.com/en-us/power-platform/admin/power-platform-inventory; https://davidamitchell.github.io/Research/research/2026-05-17-manual-workaround-to-central-it-backlog-conversion-datasets.html] A practical internal design is to treat three months as an early post-replacement decay check, six months as the first standard inactivity checkpoint, twelve months as a medium-term stabilisation window, and twenty-four months as a long-tail persistence window, while recognising that these are operational thresholds rather than public benchmark norms.

### §3 Reasoning

- [fact; source: https://aisel.aisnet.org/misqe/vol23/iss3/3/; https://aisel.aisnet.org/misqe/vol23/iss3/6/; https://research.universityofgalway.ie/en/publications/adoption-of-low-code-and-no-code-development-a-systematic-literat-6/] The accessible empirical literature supports claims about governance requirements, shadow assets, and technical debt in low-code programs.
- [fact; source: https://learn.microsoft.com/en-us/power-platform/admin/power-platform-inventory; https://learn.microsoft.com/en-us/power-platform/admin/inventory-schema; https://learn.microsoft.com/en-us/power-platform/guidance/coe/setup-auditlog-http-graphapi; https://learn.microsoft.com/en-us/power-platform/guidance/coe/setup-archive-components; https://docs.uipath.com/automation-hub/automation-cloud/latest/user-guide/deleting-data] The accessible official platform literature supports claims about inventory, telemetry, approvals, dependencies, and deletion controls.
- [inference; source: https://aisel.aisnet.org/misqe/vol23/iss3/3/; https://aisel.aisnet.org/misqe/vol23/iss3/6/; https://research.universityofgalway.ie/en/publications/adoption-of-low-code-and-no-code-development-a-systematic-literat-6/; https://learn.microsoft.com/en-us/power-platform/admin/power-platform-inventory; https://docs.uipath.com/automation-ops/automation-cloud/latest/user-guide/about-automation-ops] The best-supported top-level answer is therefore not a published rate estimate but a bounded negative finding: accessible public evidence does not currently disclose a reusable post-gap-closure persistence rate, while mature platform telemetry now makes internal measurement feasible.
- [assumption; source: https://learn.microsoft.com/en-us/power-platform/admin/inventory-schema; https://learn.microsoft.com/en-us/power-platform/guidance/coe/setup-auditlog-http-graphapi; https://docs.uipath.com/automation-hub/automation-cloud/latest/user-guide/deleting-data] This item assumes that an organisation can maintain historical snapshots or event logs, because current-state inventory alone cannot distinguish long-lived persistence from recent inactivity.

### §4 Consistency Check

- [fact; source: https://aisel.aisnet.org/misqe/vol23/iss3/3/; https://aisel.aisnet.org/misqe/vol23/iss3/6/; https://research.universityofgalway.ie/en/publications/adoption-of-low-code-and-no-code-development-a-systematic-literat-6/; https://community.pega.com/blog/when-it-time-retire-your-rpa-bots] The academic and official sources agree that local automation can accumulate governance and maintenance burdens, and no consulted source contradicts the claim that explicit lifecycle control is needed.
- [fact; source: https://learn.microsoft.com/en-us/power-platform/admin/power-platform-inventory; https://learn.microsoft.com/en-us/power-platform/guidance/coe/setup-archive-components; https://docs.uipath.com/automation-hub/automation-cloud/latest/user-guide/deleting-data] The Microsoft and UiPath platform sources are consistent in showing administrative inventory plus lifecycle controls, even though they implement them with different products and workflows.
- [inference; source: https://aisel.aisnet.org/misqe/vol23/iss3/3/; https://aisel.aisnet.org/misqe/vol23/iss3/6/; https://research.universityofgalway.ie/en/publications/adoption-of-low-code-and-no-code-development-a-systematic-literat-6/; https://learn.microsoft.com/en-us/power-platform/admin/power-platform-inventory] No unresolved contradiction remains between the negative finding on public rates and the positive finding on internal measurability, because the first concerns published cross-organisational evidence and the second concerns platform telemetry available inside an estate.

### §5 Depth and Breadth Expansion

- [inference; source: https://learn.microsoft.com/en-us/power-platform/admin/inventory-schema; https://learn.microsoft.com/en-us/power-platform/guidance/coe/setup-auditlog-http-graphapi; https://docs.uipath.com/automation-hub/automation-cloud/latest/user-guide/deleting-data] Through a technical lens, persistence measurement needs four linked signals for each asset: identity, activity, ownership, and retirement state.
- [inference; source: https://community.pega.com/blog/when-it-time-retire-your-rpa-bots; https://davidamitchell.github.io/Research/research/2026-05-16-do-mode-demand-persistence-and-build-mode-displacement.html] Through an economic lens, persistence matters because a bridge asset can continue to add support and upgrade cost after the underlying core system is improved, creating double-running cost.
- [inference; source: https://learn.microsoft.com/en-us/power-platform/guidance/coe/governance-components; https://learn.microsoft.com/en-us/power-platform/admin/power-platform-inventory; https://docs.uipath.com/automation-ops/automation-cloud/latest/user-guide/about-automation-ops] Through a governance lens, named ownership, business justification, dependency disclosure, and centralized policy administration are the minimum conditions for defensible lifecycle evidence.
- [fact; source: https://learn.microsoft.com/en-us/power-platform/guidance/coe/starter-kit] Through a historical lens, Microsoft's shift from the CoE Starter Kit toward native admin-center governance shows that inventory and lifecycle control have become standard enterprise-scale capabilities rather than optional add-ons.
- [inference; source: https://aisel.aisnet.org/misqe/vol23/iss3/6/; https://community.pega.com/blog/when-it-time-retire-your-rpa-bots; https://davidamitchell.github.io/Research/research/2026-05-14-citizen-development-rollout-empirical-evidence.html] Through a behavioural lens, users and local teams have incentives to keep useful workarounds alive unless governance turns retirement into an observable process rather than a voluntary clean-up task.

### §6 Synthesis

**Executive summary:**

Accessible public research does not currently publish a reusable longitudinal persistence rate for enterprise low-code applications, bots, or agents after the original gap is closed. [inference; source: https://aisel.aisnet.org/misqe/vol23/iss3/3/; https://aisel.aisnet.org/misqe/vol23/iss3/6/; https://research.universityofgalway.ie/en/publications/adoption-of-low-code-and-no-code-development-a-systematic-literat-6/; https://davidamitchell.github.io/Research/research/2026-05-16-do-mode-demand-persistence-and-build-mode-displacement.html] The strongest accessible evidence instead shows two adjacent facts: low-code and automation programs repeatedly create shadow assets and technical debt when governance is weak, and major platforms now expose the inventory, activity, ownership, and deletion controls needed to measure persistence internally. [inference; source: https://aisel.aisnet.org/misqe/vol23/iss3/6/; https://learn.microsoft.com/en-us/power-platform/admin/power-platform-inventory; https://learn.microsoft.com/en-us/power-platform/guidance/coe/setup-auditlog-http-graphapi; https://docs.uipath.com/automation-hub/automation-cloud/latest/user-guide/deleting-data] The most defensible current conclusion is therefore that persistence is a measurable internal lifecycle problem, not a solved public benchmarking problem. [inference; source: https://learn.microsoft.com/en-us/power-platform/admin/inventory-schema; https://learn.microsoft.com/en-us/power-platform/guidance/coe/setup-archive-components; https://docs.uipath.com/automation-ops/automation-cloud/latest/user-guide/about-automation-ops] Comparisons across governance maturity and ownership models are still possible, but they mostly compare measurability and decommission readiness, not externally published survival curves. [inference; source: https://learn.microsoft.com/en-us/power-platform/admin/power-platform-inventory; https://docs.uipath.com/automation-hub/automation-cloud/latest/user-guide/deleting-data; https://aisel.aisnet.org/misqe/vol23/iss3/6/]

**Key findings:**

1. **No accessible public empirical source consulted in this item publishes a reusable post-gap-closure persistence or survival rate for enterprise low-code applications, bots, or agents.** ([inference]; medium confidence; source: https://aisel.aisnet.org/misqe/vol23/iss3/3/; https://aisel.aisnet.org/misqe/vol23/iss3/6/; https://research.universityofgalway.ie/en/publications/adoption-of-low-code-and-no-code-development-a-systematic-literat-6/; https://davidamitchell.github.io/Research/research/2026-05-16-do-mode-demand-persistence-and-build-mode-displacement.html)
2. **The accessible low-code research base is longitudinally weak on retirement rates but consistently strong on the recurring governance, shadow-asset, and technical-debt conditions that make persistence likely.** ([inference]; medium confidence; source: https://aisel.aisnet.org/misqe/vol23/iss3/6/; https://research.universityofgalway.ie/en/publications/adoption-of-low-code-and-no-code-development-a-systematic-literat-6/; https://davidamitchell.github.io/Research/research/2026-05-14-citizen-development-rollout-empirical-evidence.html)
3. **Microsoft Power Platform now exposes enough inventory, timestamp, owner, and usage telemetry to let an enterprise calculate internal persistence windows for applications, flows, and agents if historical records are retained.** ([fact]; high confidence; source: https://learn.microsoft.com/en-us/power-platform/admin/power-platform-inventory; https://learn.microsoft.com/en-us/power-platform/admin/inventory-schema; https://learn.microsoft.com/en-us/power-platform/guidance/coe/setup-auditlog-http-graphapi)
4. **Microsoft's six-month inactivity workflow is the only explicit persistence checkpoint found in the consulted primary platform sources, and it is an operational review trigger rather than a published benchmark norm.** ([fact]; high confidence; source: https://learn.microsoft.com/en-us/power-platform/guidance/coe/setup-archive-components; https://learn.microsoft.com/en-us/power-platform/guidance/coe/governance-components)
5. **UiPath's accessible official documentation shows centralized governance, intake shutdown, and dependency-aware deletion controls, but it does not disclose public retirement or abandonment rates for automations.** ([fact]; high confidence; source: https://docs.uipath.com/automation-ops/automation-cloud/latest/user-guide/about-automation-ops; https://docs.uipath.com/automation-hub/automation-suite/2.2510/user-guide/customize-idea-flows; https://docs.uipath.com/automation-hub/automation-cloud/latest/user-guide/deleting-data)
6. **The strongest accessible bot-retirement guidance supports end-of-life planning and overlap removal as good practice, but it still stops short of reporting measured post-replacement survival percentages.** ([inference]; medium confidence; source: https://community.pega.com/blog/when-it-time-retire-your-rpa-bots; https://davidamitchell.github.io/Research/research/2026-05-16-decommission-trigger-design-for-do-mode-agents.html)
7. **Governance maturity changes the observability of persistence more clearly than it changes any publicly provable persistence rate, because mature estates capture owners, dependencies, usage, and exit events while weakly governed estates do not.** ([inference]; medium confidence; source: https://learn.microsoft.com/en-us/power-platform/admin/power-platform-inventory; https://learn.microsoft.com/en-us/power-platform/guidance/coe/governance-components; https://docs.uipath.com/automation-hub/automation-cloud/latest/user-guide/deleting-data; https://aisel.aisnet.org/misqe/vol23/iss3/6/)
8. **A practical internal measurement design is to use three, six, twelve, and twenty-four month windows as early decay, first inactivity, medium-term stabilisation, and long-tail persistence checkpoints, while treating those windows as operational conventions rather than public standards.** ([inference]; medium confidence; source: https://learn.microsoft.com/en-us/power-platform/guidance/coe/setup-archive-components; https://learn.microsoft.com/en-us/power-platform/admin/inventory-schema; https://davidamitchell.github.io/Research/research/2026-05-17-manual-workaround-to-central-it-backlog-conversion-datasets.html)

**Evidence map:**

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [inference] No accessible public empirical source consulted publishes a reusable post-gap-closure persistence rate. | https://aisel.aisnet.org/misqe/vol23/iss3/3/ ; https://aisel.aisnet.org/misqe/vol23/iss3/6/ ; https://research.universityofgalway.ie/en/publications/adoption-of-low-code-and-no-code-development-a-systematic-literat-6/ ; https://davidamitchell.github.io/Research/research/2026-05-16-do-mode-demand-persistence-and-build-mode-displacement.html | medium | absence across consulted evidence base |
| [inference] The low-code evidence base is stronger on governance and technical debt than on retirement rates. | https://aisel.aisnet.org/misqe/vol23/iss3/6/ ; https://research.universityofgalway.ie/en/publications/adoption-of-low-code-and-no-code-development-a-systematic-literat-6/ ; https://davidamitchell.github.io/Research/research/2026-05-14-citizen-development-rollout-empirical-evidence.html | medium | indirect persistence evidence |
| [fact] Microsoft exposes inventory, timestamp, owner, and usage telemetry for internal persistence measurement. | https://learn.microsoft.com/en-us/power-platform/admin/power-platform-inventory ; https://learn.microsoft.com/en-us/power-platform/admin/inventory-schema ; https://learn.microsoft.com/en-us/power-platform/guidance/coe/setup-auditlog-http-graphapi | high | direct primary documentation |
| [fact] Microsoft's six-month inactivity workflow is an operational review trigger, not a public benchmark norm. | https://learn.microsoft.com/en-us/power-platform/guidance/coe/setup-archive-components ; https://learn.microsoft.com/en-us/power-platform/guidance/coe/governance-components | high | configurable default horizon |
| [fact] UiPath documents centralized governance and dependency-aware exit controls, but not public persistence rates. | https://docs.uipath.com/automation-ops/automation-cloud/latest/user-guide/about-automation-ops ; https://docs.uipath.com/automation-hub/automation-suite/2.2510/user-guide/customize-idea-flows ; https://docs.uipath.com/automation-hub/automation-cloud/latest/user-guide/deleting-data | high | control surfaces only |
| [inference] Bot-retirement guidance supports end-of-life planning without reporting survival percentages. | https://community.pega.com/blog/when-it-time-retire-your-rpa-bots ; https://davidamitchell.github.io/Research/research/2026-05-16-decommission-trigger-design-for-do-mode-agents.html | medium | qualitative lifecycle guidance |
| [inference] Governance maturity changes observability and decommission readiness more clearly than any publicly provable rate. | https://learn.microsoft.com/en-us/power-platform/admin/power-platform-inventory ; https://learn.microsoft.com/en-us/power-platform/guidance/coe/governance-components ; https://docs.uipath.com/automation-hub/automation-cloud/latest/user-guide/deleting-data ; https://aisel.aisnet.org/misqe/vol23/iss3/6/ | medium | cross-source synthesis |
| [inference] Three, six, twelve, and twenty-four month windows are operationally defensible internal checkpoints, not public standards. | https://learn.microsoft.com/en-us/power-platform/guidance/coe/setup-archive-components ; https://learn.microsoft.com/en-us/power-platform/admin/inventory-schema ; https://davidamitchell.github.io/Research/research/2026-05-17-manual-workaround-to-central-it-backlog-conversion-datasets.html | medium | design inference |

**Assumptions:**

- [assumption; source: https://davidamitchell.github.io/Research/research/2026-05-16-do-mode-demand-persistence-and-build-mode-displacement.html; https://davidamitchell.github.io/Research/research/2026-05-16-decommission-trigger-design-for-do-mode-agents.html; https://learn.microsoft.com/en-us/power-platform/admin/power-platform-inventory] This item treats gap closure as the point when an equivalent governed capability exists, even if organisations may disagree on when that capability is fully adopted.
- [assumption; source: https://learn.microsoft.com/en-us/power-platform/admin/inventory-schema; https://learn.microsoft.com/en-us/power-platform/guidance/coe/setup-auditlog-http-graphapi; https://docs.uipath.com/automation-hub/automation-cloud/latest/user-guide/deleting-data] This item assumes that persistence measurement uses retained historical records or repeated extracts rather than a single current-state snapshot.
- [assumption; source: https://learn.microsoft.com/en-us/power-platform/guidance/coe/setup-archive-components; https://davidamitchell.github.io/Research/research/2026-05-17-manual-workaround-to-central-it-backlog-conversion-datasets.html] The proposed 3, 6, 12, and 24 month windows are treated as operational checkpoints because the consulted sources do not provide a stronger public benchmark schedule.

**Analysis:**

The evidence weighs most heavily toward a bounded negative answer: the accessible public literature does not disclose a reusable persistence rate after gap closure. [inference; source: https://aisel.aisnet.org/misqe/vol23/iss3/3/; https://aisel.aisnet.org/misqe/vol23/iss3/6/; https://research.universityofgalway.ie/en/publications/adoption-of-low-code-and-no-code-development-a-systematic-literat-6/] That conclusion is stronger than a simple "not found in this session" claim because the consulted empirical studies, official platform documentation, and adjacent completed repository items all converge on governance mechanisms and lifecycle controls rather than on published survival curves. [inference; source: https://learn.microsoft.com/en-us/power-platform/admin/power-platform-inventory; https://docs.uipath.com/automation-ops/automation-cloud/latest/user-guide/about-automation-ops; https://community.pega.com/blog/when-it-time-retire-your-rpa-bots; https://davidamitchell.github.io/Research/research/2026-05-16-do-mode-demand-persistence-and-build-mode-displacement.html] The trade-off is that platform documentation gives strong evidence for measurability inside a governed estate, but that same strength should not be overstated into a claim about actual cross-firm persistence outcomes. [inference; source: https://learn.microsoft.com/en-us/power-platform/admin/inventory-schema; https://learn.microsoft.com/en-us/power-platform/guidance/coe/setup-auditlog-http-graphapi; https://docs.uipath.com/automation-hub/automation-cloud/latest/user-guide/deleting-data] The most decision-useful comparison across governance maturity and ownership models is therefore about whether an organisation can observe and enforce retirement at all, not about whether public benchmarks prove a universal rate difference. [inference; source: https://learn.microsoft.com/en-us/power-platform/admin/power-platform-inventory; https://aisel.aisnet.org/misqe/vol23/iss3/6/]

**Risks, gaps, uncertainties:**

- Public cross-organisational benchmark data on post-gap-closure persistence remains absent from the consulted accessible evidence base. [inference; source: https://aisel.aisnet.org/misqe/vol23/iss3/3/; https://aisel.aisnet.org/misqe/vol23/iss3/6/; https://research.universityofgalway.ie/en/publications/adoption-of-low-code-and-no-code-development-a-systematic-literat-6/]
- The seeded Forrester and IEEE pages did not produce usable evidence, which leaves this item more dependent on official platform documentation and accessible empirical studies. [fact; source: https://www.forrester.com/report/the-forrester-wave-low-code-development-platforms-for-professional-developers-q2-2023/RES177705; https://www.computer.org/technical-committees/software-engineering/resources/software-evolution]
- The consulted vendor documentation is authoritative for platform capabilities but not independent evidence of actual estate-level retirement outcomes. [inference; source: https://learn.microsoft.com/en-us/power-platform/admin/power-platform-inventory; https://docs.uipath.com/automation-ops/automation-cloud/latest/user-guide/about-automation-ops; https://community.pega.com/blog/when-it-time-retire-your-rpa-bots]
- Agent-specific public lifecycle evidence is thinner than low-code application evidence, even though Microsoft now includes agents in its inventory surface. [inference; source: https://learn.microsoft.com/en-us/power-platform/admin/power-platform-inventory; https://research.universityofgalway.ie/en/publications/adoption-of-low-code-and-no-code-development-a-systematic-literat-6/]

**Open questions:**

- Which enterprises are willing to publish anonymised cohort-level persistence data for low-code applications, bots, and agents across 3, 6, 12, and 24 month windows? [inference; source: https://learn.microsoft.com/en-us/power-platform/admin/power-platform-inventory; https://docs.uipath.com/automation-ops/automation-cloud/latest/user-guide/about-automation-ops]
- What is the cleanest denominator for measuring persistence after gap closure: all created assets, all approved assets, or only assets whose original bridging need has been formally closed? [inference; source: https://davidamitchell.github.io/Research/research/2026-05-17-manual-workaround-to-central-it-backlog-conversion-datasets.html]
- Does named central ownership materially reduce long-tail persistence, or does it mainly improve observability and clean-up execution? [inference; source: https://learn.microsoft.com/en-us/power-platform/admin/power-platform-inventory; https://docs.uipath.com/automation-hub/automation-cloud/latest/user-guide/deleting-data]

**Output:**

- Type: knowledge
- Description: This item establishes that the strongest current evidence is a gap claim plus an internal-measurement design claim: public post-gap-closure persistence benchmarks are not yet accessible, but mature platform telemetry now makes internal lifecycle measurement and retirement analysis feasible. [inference; source: https://learn.microsoft.com/en-us/power-platform/admin/power-platform-inventory; https://learn.microsoft.com/en-us/power-platform/guidance/coe/setup-archive-components; https://docs.uipath.com/automation-hub/automation-cloud/latest/user-guide/deleting-data]
- Links:
  - https://learn.microsoft.com/en-us/power-platform/admin/power-platform-inventory
  - https://learn.microsoft.com/en-us/power-platform/guidance/coe/setup-archive-components
  - https://aisel.aisnet.org/misqe/vol23/iss3/6/

### §7 Recursive Review

- Review result: pass.
- Acronym audit: Information Technology (IT), Center of Excellence (CoE), Application Programming Interface (API), and Robotic Process Automation (RPA) expanded on first use.
- Claim audit: Findings and synthesis claims are labeled and URL-backed; assumptions retain justification sources.
- Uncertainty audit: the absence of public persistence-rate benchmarks remains explicit and confidence is set to low at the item level because the central question is constrained by evidence gaps.

---

## Findings

*(Populated from §6 Synthesis above.)*

### Executive Summary

Accessible public research does not currently publish a reusable longitudinal persistence rate for enterprise low-code applications, bots, or agents after the original gap is closed. [inference; source: https://aisel.aisnet.org/misqe/vol23/iss3/3/; https://aisel.aisnet.org/misqe/vol23/iss3/6/; https://research.universityofgalway.ie/en/publications/adoption-of-low-code-and-no-code-development-a-systematic-literat-6/; https://davidamitchell.github.io/Research/research/2026-05-16-do-mode-demand-persistence-and-build-mode-displacement.html] The strongest accessible evidence instead shows repeated governance and technical-debt conditions that make persistence plausible, together with platform telemetry and lifecycle controls that make internal measurement feasible. [inference; source: https://aisel.aisnet.org/misqe/vol23/iss3/6/; https://learn.microsoft.com/en-us/power-platform/admin/power-platform-inventory; https://learn.microsoft.com/en-us/power-platform/guidance/coe/setup-auditlog-http-graphapi; https://docs.uipath.com/automation-hub/automation-cloud/latest/user-guide/deleting-data] The best-supported current conclusion is that persistence after gap closure is a measurable internal lifecycle problem, not a solved public benchmarking problem. [inference; source: https://learn.microsoft.com/en-us/power-platform/admin/inventory-schema; https://learn.microsoft.com/en-us/power-platform/guidance/coe/setup-archive-components; https://docs.uipath.com/automation-ops/automation-cloud/latest/user-guide/about-automation-ops] Comparisons across governance maturity and ownership models are still decision-useful, but they mostly compare observability and decommission readiness rather than externally published survival curves. [inference; source: https://learn.microsoft.com/en-us/power-platform/admin/power-platform-inventory; https://docs.uipath.com/automation-hub/automation-cloud/latest/user-guide/deleting-data; https://aisel.aisnet.org/misqe/vol23/iss3/6/]

### Key Findings

1. **No accessible public empirical source consulted in this item publishes a reusable post-gap-closure persistence or survival rate for enterprise low-code applications, bots, or agents.** ([inference]; medium confidence; source: https://aisel.aisnet.org/misqe/vol23/iss3/3/; https://aisel.aisnet.org/misqe/vol23/iss3/6/; https://research.universityofgalway.ie/en/publications/adoption-of-low-code-and-no-code-development-a-systematic-literat-6/; https://davidamitchell.github.io/Research/research/2026-05-16-do-mode-demand-persistence-and-build-mode-displacement.html)
2. **The accessible low-code research base is longitudinally weak on retirement rates but consistently strong on the recurring governance, shadow-asset, and technical-debt conditions that make persistence likely.** ([inference]; medium confidence; source: https://aisel.aisnet.org/misqe/vol23/iss3/6/; https://research.universityofgalway.ie/en/publications/adoption-of-low-code-and-no-code-development-a-systematic-literat-6/; https://davidamitchell.github.io/Research/research/2026-05-14-citizen-development-rollout-empirical-evidence.html)
3. **Microsoft Power Platform now exposes enough inventory, timestamp, owner, and usage telemetry to let an enterprise calculate internal persistence windows for applications, flows, and agents if historical records are retained.** ([fact]; high confidence; source: https://learn.microsoft.com/en-us/power-platform/admin/power-platform-inventory; https://learn.microsoft.com/en-us/power-platform/admin/inventory-schema; https://learn.microsoft.com/en-us/power-platform/guidance/coe/setup-auditlog-http-graphapi)
4. **Microsoft's six-month inactivity workflow is the only explicit persistence checkpoint found in the consulted primary platform sources, and it is an operational review trigger rather than a published benchmark norm.** ([fact]; high confidence; source: https://learn.microsoft.com/en-us/power-platform/guidance/coe/setup-archive-components; https://learn.microsoft.com/en-us/power-platform/guidance/coe/governance-components)
5. **UiPath's accessible official documentation shows centralized governance, intake shutdown, and dependency-aware deletion controls, but it does not disclose public retirement or abandonment rates for automations.** ([fact]; high confidence; source: https://docs.uipath.com/automation-ops/automation-cloud/latest/user-guide/about-automation-ops; https://docs.uipath.com/automation-hub/automation-suite/2.2510/user-guide/customize-idea-flows; https://docs.uipath.com/automation-hub/automation-cloud/latest/user-guide/deleting-data)
6. **The strongest accessible bot-retirement guidance supports end-of-life planning and overlap removal as good practice, but it still stops short of reporting measured post-replacement survival percentages.** ([inference]; medium confidence; source: https://community.pega.com/blog/when-it-time-retire-your-rpa-bots; https://davidamitchell.github.io/Research/research/2026-05-16-decommission-trigger-design-for-do-mode-agents.html)
7. **Governance maturity changes the observability of persistence more clearly than it changes any publicly provable persistence rate, because mature estates capture owners, dependencies, usage, and exit events while weakly governed estates do not.** ([inference]; medium confidence; source: https://learn.microsoft.com/en-us/power-platform/admin/power-platform-inventory; https://learn.microsoft.com/en-us/power-platform/guidance/coe/governance-components; https://docs.uipath.com/automation-hub/automation-cloud/latest/user-guide/deleting-data; https://aisel.aisnet.org/misqe/vol23/iss3/6/)
8. **A practical internal measurement design is to use three, six, twelve, and twenty-four month windows as early decay, first inactivity, medium-term stabilisation, and long-tail persistence checkpoints, while treating those windows as operational conventions rather than public standards.** ([inference]; medium confidence; source: https://learn.microsoft.com/en-us/power-platform/guidance/coe/setup-archive-components; https://learn.microsoft.com/en-us/power-platform/admin/inventory-schema; https://davidamitchell.github.io/Research/research/2026-05-17-manual-workaround-to-central-it-backlog-conversion-datasets.html)

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [inference] No accessible public empirical source consulted publishes a reusable post-gap-closure persistence rate. | https://aisel.aisnet.org/misqe/vol23/iss3/3/ ; https://aisel.aisnet.org/misqe/vol23/iss3/6/ ; https://research.universityofgalway.ie/en/publications/adoption-of-low-code-and-no-code-development-a-systematic-literat-6/ ; https://davidamitchell.github.io/Research/research/2026-05-16-do-mode-demand-persistence-and-build-mode-displacement.html | medium | absence across consulted evidence base |
| [inference] The low-code evidence base is stronger on governance and technical debt than on retirement rates. | https://aisel.aisnet.org/misqe/vol23/iss3/6/ ; https://research.universityofgalway.ie/en/publications/adoption-of-low-code-and-no-code-development-a-systematic-literat-6/ ; https://davidamitchell.github.io/Research/research/2026-05-14-citizen-development-rollout-empirical-evidence.html | medium | indirect persistence evidence |
| [fact] Microsoft exposes inventory, timestamp, owner, and usage telemetry for internal persistence measurement. | https://learn.microsoft.com/en-us/power-platform/admin/power-platform-inventory ; https://learn.microsoft.com/en-us/power-platform/admin/inventory-schema ; https://learn.microsoft.com/en-us/power-platform/guidance/coe/setup-auditlog-http-graphapi | high | direct primary documentation |
| [fact] Microsoft's six-month inactivity workflow is an operational review trigger, not a public benchmark norm. | https://learn.microsoft.com/en-us/power-platform/guidance/coe/setup-archive-components ; https://learn.microsoft.com/en-us/power-platform/guidance/coe/governance-components | high | configurable default horizon |
| [fact] UiPath documents centralized governance and dependency-aware exit controls, but not public persistence rates. | https://docs.uipath.com/automation-ops/automation-cloud/latest/user-guide/about-automation-ops ; https://docs.uipath.com/automation-hub/automation-suite/2.2510/user-guide/customize-idea-flows ; https://docs.uipath.com/automation-hub/automation-cloud/latest/user-guide/deleting-data | high | control surfaces only |
| [inference] Bot-retirement guidance supports end-of-life planning without reporting survival percentages. | https://community.pega.com/blog/when-it-time-retire-your-rpa-bots ; https://davidamitchell.github.io/Research/research/2026-05-16-decommission-trigger-design-for-do-mode-agents.html | medium | qualitative lifecycle guidance |
| [inference] Governance maturity changes observability and decommission readiness more clearly than any publicly provable rate. | https://learn.microsoft.com/en-us/power-platform/admin/power-platform-inventory ; https://learn.microsoft.com/en-us/power-platform/guidance/coe/governance-components ; https://docs.uipath.com/automation-hub/automation-cloud/latest/user-guide/deleting-data ; https://aisel.aisnet.org/misqe/vol23/iss3/6/ | medium | cross-source synthesis |
| [inference] Three, six, twelve, and twenty-four month windows are operationally defensible internal checkpoints, not public standards. | https://learn.microsoft.com/en-us/power-platform/guidance/coe/setup-archive-components ; https://learn.microsoft.com/en-us/power-platform/admin/inventory-schema ; https://davidamitchell.github.io/Research/research/2026-05-17-manual-workaround-to-central-it-backlog-conversion-datasets.html | medium | design inference |

### Assumptions

- [assumption; source: https://davidamitchell.github.io/Research/research/2026-05-16-do-mode-demand-persistence-and-build-mode-displacement.html; https://davidamitchell.github.io/Research/research/2026-05-16-decommission-trigger-design-for-do-mode-agents.html; https://learn.microsoft.com/en-us/power-platform/admin/power-platform-inventory] This item treats gap closure as the point when an equivalent governed capability exists, even if organisations may disagree on when that capability is fully adopted.
- [assumption; source: https://learn.microsoft.com/en-us/power-platform/admin/inventory-schema; https://learn.microsoft.com/en-us/power-platform/guidance/coe/setup-auditlog-http-graphapi; https://docs.uipath.com/automation-hub/automation-cloud/latest/user-guide/deleting-data] This item assumes that persistence measurement uses retained historical records or repeated extracts rather than a single current-state snapshot.
- [assumption; source: https://learn.microsoft.com/en-us/power-platform/guidance/coe/setup-archive-components; https://davidamitchell.github.io/Research/research/2026-05-17-manual-workaround-to-central-it-backlog-conversion-datasets.html] The proposed 3, 6, 12, and 24 month windows are treated as operational checkpoints because the consulted sources do not provide a stronger public benchmark schedule.

### Analysis

The evidence weighs most heavily toward a bounded negative answer: the accessible public literature does not disclose a reusable persistence rate after gap closure. [inference; source: https://aisel.aisnet.org/misqe/vol23/iss3/3/; https://aisel.aisnet.org/misqe/vol23/iss3/6/; https://research.universityofgalway.ie/en/publications/adoption-of-low-code-and-no-code-development-a-systematic-literat-6/] That conclusion is stronger than a simple session-local search failure because the consulted empirical studies, official platform documentation, and adjacent completed repository items all converge on governance mechanisms and lifecycle controls rather than on published survival curves. [inference; source: https://learn.microsoft.com/en-us/power-platform/admin/power-platform-inventory; https://docs.uipath.com/automation-ops/automation-cloud/latest/user-guide/about-automation-ops; https://community.pega.com/blog/when-it-time-retire-your-rpa-bots; https://davidamitchell.github.io/Research/research/2026-05-16-do-mode-demand-persistence-and-build-mode-displacement.html] Platform documentation gives strong evidence for internal measurability, but that strength should not be overstated into a claim about actual cross-firm persistence outcomes. [inference; source: https://learn.microsoft.com/en-us/power-platform/admin/inventory-schema; https://learn.microsoft.com/en-us/power-platform/guidance/coe/setup-auditlog-http-graphapi; https://docs.uipath.com/automation-hub/automation-cloud/latest/user-guide/deleting-data] The most decision-useful comparison across governance maturity and ownership models is therefore about whether an organisation can observe and enforce retirement at all, not about whether public benchmarks prove a universal rate difference. [inference; source: https://learn.microsoft.com/en-us/power-platform/admin/power-platform-inventory; https://aisel.aisnet.org/misqe/vol23/iss3/6/]

### Risks, Gaps, and Uncertainties

- Public cross-organisational benchmark data on post-gap-closure persistence remains absent from the consulted accessible evidence base. [inference; source: https://aisel.aisnet.org/misqe/vol23/iss3/3/; https://aisel.aisnet.org/misqe/vol23/iss3/6/; https://research.universityofgalway.ie/en/publications/adoption-of-low-code-and-no-code-development-a-systematic-literat-6/]
- The seeded Forrester and IEEE pages did not produce usable evidence, which leaves this item more dependent on official platform documentation and accessible empirical studies. [fact; source: https://www.forrester.com/report/the-forrester-wave-low-code-development-platforms-for-professional-developers-q2-2023/RES177705; https://www.computer.org/technical-committees/software-engineering/resources/software-evolution]
- The consulted vendor documentation is authoritative for platform capabilities but not independent evidence of actual estate-level retirement outcomes. [inference; source: https://learn.microsoft.com/en-us/power-platform/admin/power-platform-inventory; https://docs.uipath.com/automation-ops/automation-cloud/latest/user-guide/about-automation-ops; https://community.pega.com/blog/when-it-time-retire-your-rpa-bots]
- Agent-specific public lifecycle evidence is thinner than low-code application evidence, even though Microsoft now includes agents in its inventory surface. [inference; source: https://learn.microsoft.com/en-us/power-platform/admin/power-platform-inventory; https://research.universityofgalway.ie/en/publications/adoption-of-low-code-and-no-code-development-a-systematic-literat-6/]

### Open Questions

- Which enterprises are willing to publish anonymised cohort-level persistence data for low-code applications, bots, and agents across 3, 6, 12, and 24 month windows? [inference; source: https://learn.microsoft.com/en-us/power-platform/admin/power-platform-inventory; https://docs.uipath.com/automation-ops/automation-cloud/latest/user-guide/about-automation-ops]
- What is the cleanest denominator for measuring persistence after gap closure: all created assets, all approved assets, or only assets whose original bridging need has been formally closed? [inference; source: https://davidamitchell.github.io/Research/research/2026-05-17-manual-workaround-to-central-it-backlog-conversion-datasets.html]
- Does named central ownership materially reduce long-tail persistence, or does it mainly improve observability and clean-up execution? [inference; source: https://learn.microsoft.com/en-us/power-platform/admin/power-platform-inventory; https://docs.uipath.com/automation-hub/automation-cloud/latest/user-guide/deleting-data]

### Output

- Type: knowledge
- Description: This item establishes that the strongest current evidence is a gap claim plus an internal-measurement design claim: public post-gap-closure persistence benchmarks are not yet accessible, but mature platform telemetry now makes internal lifecycle measurement and retirement analysis feasible. [inference; source: https://learn.microsoft.com/en-us/power-platform/admin/power-platform-inventory; https://learn.microsoft.com/en-us/power-platform/guidance/coe/setup-archive-components; https://docs.uipath.com/automation-hub/automation-cloud/latest/user-guide/deleting-data]
- Links:
  - https://learn.microsoft.com/en-us/power-platform/admin/power-platform-inventory
  - https://learn.microsoft.com/en-us/power-platform/guidance/coe/setup-archive-components
  - https://aisel.aisnet.org/misqe/vol23/iss3/6/

---

## Output

- Type: knowledge
- Description: This item establishes that the strongest current evidence is a gap claim plus an internal-measurement design claim: public post-gap-closure persistence benchmarks are not yet accessible, but mature platform telemetry now makes internal lifecycle measurement and retirement analysis feasible. [inference; source: https://learn.microsoft.com/en-us/power-platform/admin/power-platform-inventory; https://learn.microsoft.com/en-us/power-platform/guidance/coe/setup-archive-components; https://docs.uipath.com/automation-hub/automation-cloud/latest/user-guide/deleting-data]
- Links:
  - https://learn.microsoft.com/en-us/power-platform/admin/power-platform-inventory
  - https://learn.microsoft.com/en-us/power-platform/guidance/coe/setup-archive-components
  - https://aisel.aisnet.org/misqe/vol23/iss3/6/
