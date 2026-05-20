---
review_count: 2
title: "Datasets for measuring conversion from demand for local workaround tools to central Information Technology backlog items"
added: 2026-05-17T20:40:49+00:00
status: completed
priority: high
blocks: []
tags: [organisation, workflow, analytics]
themes: [governance-policy, benchmarks-eval, tools-infrastructure, knowledge-management, workflow-automation]
started: 2026-05-18T11:41:57+00:00
completed: 2026-05-18T12:04:26+00:00
output: []
cites:
  - 2026-05-16-do-mode-demand-persistence-and-build-mode-displacement
  - 2026-05-09-system-of-record-bypass-control-deficiencies
  - 2026-05-14-citizen-development-rollout-empirical-evidence
  - 2026-05-17-build-mode-failure-vs-do-mode-incident-comparison-denominator
related:
  - 2026-04-26-systems-capability-debt-citizen-development-empirical-evidence
  - 2026-03-08-servicenow-process-mapping
superseded_by: ~
supersedes: ~
item_type: primary
confidence: medium
versions:
  - version: "1.0"
    sha: c473819bbe68d52bc0784add41f819fc60ddd612
    changed: 2026-05-18
    progress: progress/2026-05-18-manual-workaround-to-central-it-backlog-conversion-datasets.md
    summary: "Initial completion"
---

# Datasets for measuring conversion from demand for local workaround tools to central Information Technology backlog items

## Research Question

What public or internal datasets can validly measure the rate at which demand for local workaround tools, such as local apps, flows, lists, or spreadsheets, is converted into formal central Information Technology (IT) backlog items?

## Scope

**In scope:**
- Public benchmark datasets and industry surveys that expose demand, ticket, backlog, and completion fields
- Internal operational datasets from ticketing, workflow, and portfolio systems that can be joined for conversion-rate measurement
- Measurement designs that support repeatable month-over-month conversion tracking

**Out of scope:**
- Prescriptive tooling selection or implementation of any specific IT service management platform
- Causal claims about why conversion does or does not happen without supporting evidence

**Constraints:** Prefer sources with documented schemas or metric definitions, and prioritise data structures that can be reproduced in enterprise environments.

## Context

Leadership cannot prioritize remediation of workaround-heavy operating areas without a measurable funnel from workaround signal to governed backlog intake. [inference; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-16-do-mode-demand-persistence-and-build-mode-displacement.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-09-system-of-record-bypass-control-deficiencies.md; https://csrc.nist.gov/publications/detail/sp/800-55/rev-1/final]

## Approach

1. Catalogue candidate public and internal datasets with fields that capture workaround demand and backlog conversion events.
2. Define join keys and denominator choices needed to compute conversion rates without double counting.
3. Assess data-quality, governance, and history-loss distortion, meaning bias caused when only records that remain visible later are counted, that affect comparability across organisations.

## Sources

- [ ] [Google Cloud DevOps Research and Assessment overview](https://cloud.google.com/architecture/devops/devops-measurement-metrics) - seeded page checked; not used for downstream claims
- [x] [DevOps Research and Assessment (DORA) (2026) DORA's software delivery performance metrics](https://dora.dev/guides/dora-metrics/) - official metric definitions, scope cautions, and notes on data coming from multiple systems
- [x] [Atlassian Jira Cloud REST issue search documentation](https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-issue-search/) - issue search fields and search result structure
- [x] [Atlassian Jira Cloud REST issues documentation](https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-issues/) - bulk changelog fetch and issue-history extraction
- [x] [Atlassian Jira Cloud REST issue fields documentation](https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-issue-fields/) - system and custom field discovery
- [x] [GitHub Docs REST issues documentation](https://docs.github.com/en/rest/issues/issues) - issue state, timestamps, labels, milestones, and assignee fields
- [x] [GitHub Docs REST timeline events documentation](https://docs.github.com/en/rest/issues/timeline) - timestamped lifecycle events for issues
- [x] [GitHub Docs issue event types reference](https://docs.github.com/en/rest/using-the-rest-api/issue-event-types) - semantics of labeled, assigned, closed, commented, and related timeline events
- [x] [Microsoft Learn (2026) Power Platform Center of Excellence (CoE) Starter Kit](https://learn.microsoft.com/en-us/power-platform/guidance/coe/starter-kit) - governance and telemetry positioning, plus the shift to native admin-center inventory
- [x] [Microsoft Learn (2026) Set up inventory components](https://learn.microsoft.com/en-us/power-platform/guidance/coe/setup-core-components) - resource inventory synced into tables for apps, flows, and makers
- [x] [Microsoft Learn (2026) Collect audit logs using Microsoft Graph Application Programming Interface (API)](https://learn.microsoft.com/en-us/power-platform/guidance/coe/setup-auditlog-http-graphapi) - app launches and unique-user telemetry
- [x] [Microsoft Learn (2026) Use governance components](https://learn.microsoft.com/en-us/power-platform/guidance/coe/governance-components) - business justification, business impact, dependency, and mitigation-plan fields
- [x] [Microsoft Learn (2026) Power Platform inventory](https://learn.microsoft.com/en-us/power-platform/admin/power-platform-inventory) - tenant-wide inventory, filtering, owner data, and export surface
- [x] [Microsoft Learn (2026) Power Platform inventory schema reference](https://learn.microsoft.com/en-us/power-platform/admin/inventory-schema) - queryable fields such as owner, environment, created, and modified timestamps
- [x] [Microsoft Learn (2026) Power Platform inventory Application Programming Interface (API)](https://learn.microsoft.com/en-us/power-platform/admin/inventory-api) - query structure, joins, projections, and count queries
- [x] [ServiceNow Community (2023) Quick start guide for Demand Management](https://www.servicenow.com/community/spm-blog/quick-start-guide-for-demand-management/ba-p/2722545) - centralized intake, demand assessment, and promotion framing
- [x] [National Institute of Standards and Technology (NIST) Special Publication (SP) 800-55 Revision 1 landing page](https://csrc.nist.gov/publications/detail/sp/800-55/rev-1/final) - official measurement-design reference used for repeatable, quantifiable, comparable, and decision-useful metric criteria
- [x] [Mitchell (2026) Temporary Automation Demand Persistence and Core Capability Investment Displacement](https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-16-do-mode-demand-persistence-and-build-mode-displacement.md) - prior completed item on persistent workaround demand and governance implications
- [x] [Mitchell (2026) Control deficiencies from bypassing designated workforce record platforms](https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-09-system-of-record-bypass-control-deficiencies.md) - prior completed item on derivative-record and origin-link failures
- [x] [Mitchell (2026) Empirical evidence on rollout of organisation-wide low-code and no-code programs](https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-14-citizen-development-rollout-empirical-evidence.md) - prior completed item on citizen-development governance and shadow demand
- [x] [Mitchell (2026) Matched denominator for comparing post-pipeline release-based failures with production live-runtime incidents](https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-17-build-mode-failure-vs-do-mode-incident-comparison-denominator.md) - prior completed item on denominator discipline and comparable measurement units

---

## Research Skill Output

*(Full output from running the research skill, retained verbatim in the completed item. Sections 0 to 5 are the investigation, and section 6 seeds the Findings section below.)*

### §0 Initialise

- Question: What public or internal datasets can validly measure the rate at which demand for local workaround tools, such as local apps, flows, lists, or spreadsheets, is converted into formal central Information Technology (IT) backlog items?
- Scope: public benchmark and survey datasets, internal ticketing and portfolio datasets, denominator and join-key design, and data-quality risks for month-over-month conversion tracking
- Constraints: prefer documented schemas or metric definitions, use URL-backed citations only, and distinguish dataset availability from claims about actual enterprise conversion performance
- Output: full structured synthesis with executive summary, key findings, evidence map, assumptions, analysis, risks, and open questions
- Mode: full
- [fact; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-16-do-mode-demand-persistence-and-build-mode-displacement.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-09-system-of-record-bypass-control-deficiencies.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-14-citizen-development-rollout-empirical-evidence.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-17-build-mode-failure-vs-do-mode-incident-comparison-denominator.md] Prior completed-item sweep found four directly relevant repository items: one on persistent workaround demand, one on control failure when authoritative systems are bypassed, one on citizen-development governance evidence, and one on denominator discipline for comparable operational measurement.
- [assumption; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-16-do-mode-demand-persistence-and-build-mode-displacement.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-09-system-of-record-bypass-control-deficiencies.md; https://learn.microsoft.com/en-us/power-platform/guidance/coe/governance-components] In this item, manual workaround demand means requests, telemetry, or governance records showing that business users created or depended on local apps, flows, lists, spreadsheets, or other ad hoc artifacts because the central path could not satisfy the need quickly enough.
- [assumption; source: https://csrc.nist.gov/publications/detail/sp/800-55/rev-1/final; https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-issues/; https://docs.github.com/en/rest/issues/timeline; https://www.servicenow.com/community/spm-blog/quick-start-guide-for-demand-management/ba-p/2722545] In this item, a workaround signal counts as converted only when a formal backlog, demand, enhancement, defect, or equivalent governed work item can be durably linked to the originating workaround record and dated in a workflow history.

### §1 Question Decomposition

- **Root question:** Which datasets can validly measure workaround-demand to central-backlog conversion, and what measurement design is required to use them without distortion?
- **A. Public evidence base**
  - A1. Do public benchmark datasets directly expose workaround-demand and backlog-conversion records?
  - A2. Which public sources are useful only for metric-design guidance rather than direct rate estimation?
- **B. Internal ticketing and work-management datasets**
  - B1. What fields and history surfaces does Jira expose for backlog conversion measurement?
  - B2. What fields and history surfaces does GitHub expose for issue-lifecycle and backlog-state measurement?
  - B3. What fields and telemetry surfaces do Power Platform governance datasets expose for workaround-demand measurement?
  - B4. What central intake or demand datasets does ServiceNow expose for formal backlog conversion measurement?
- **C. Join design**
  - C1. What link keys are needed to connect workaround signals to central backlog items?
  - C2. What denominator should be used to compute a comparable conversion rate?
  - C3. How should many-to-one and one-to-many mappings be handled without double counting?
- **D. Bias and data quality**
  - D1. What goes wrong when only current-state tables are used?
  - D2. What governance gaps hide workaround demand before it reaches the backlog?
  - D3. Which dataset families are strong enough for month-over-month tracking?

### §2 Investigation

- **Source-access notes**
  - Google Cloud seed page -> localization shell only -> excluded from evidence set
  - ServiceNow docs pages -> application shell only -> evidence set uses the readable community quick-start page plus official documentation URLs surfaced by search

- **A. Public benchmark landscape**
  - [fact; source: https://dora.dev/guides/dora-metrics/] DORA says its software-delivery metrics are best suited to measuring one application or service at a time and warns that comparing metrics across very different applications can be misleading.
  - [fact; source: https://dora.dev/guides/dora-metrics/] DORA also says the data needed to collect delivery metrics often exists in multiple systems and that building precise integrations across those systems may not be worth the initial investment.
  - [fact; source: https://learn.microsoft.com/en-us/power-platform/admin/power-platform-inventory; https://learn.microsoft.com/en-us/power-platform/admin/inventory-schema; https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-issue-search/; https://docs.github.com/en/rest/issues/issues] The official Microsoft, Atlassian, and GitHub sources in scope document schemas, fields, and administrative query surfaces rather than publishing a cross-organisational benchmark dataset of workaround signals linked to formal backlog outcomes.
  - [inference; source: https://dora.dev/guides/dora-metrics/; https://learn.microsoft.com/en-us/power-platform/admin/power-platform-inventory; https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-issue-search/; https://docs.github.com/en/rest/issues/issues] No consulted public source provides a row-level benchmark dataset that directly measures enterprise manual-workaround demand and its later conversion into central Information Technology backlog items across organisations.
  - [inference; source: https://docs.github.com/en/rest/issues/issues; https://docs.github.com/en/rest/issues/timeline; https://docs.github.com/en/rest/using-the-rest-api/issue-event-types] Public issue trackers can still serve as method-testing surrogate datasets when repositories expose issue creation, labels, milestones, closure, and lifecycle events, but they are surrogates for workflow design rather than valid benchmarks of enterprise workaround demand.

- **B1. Jira dataset surfaces**
  - [fact; source: https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-issue-search/] Jira issue search returns SearchResults for a Jira Query Language (JQL) expression and exposes issues plus selected fields for the matching issue set.
  - [fact; source: https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-issues/] Jira bulk changelog fetch returns paginated changelog histories for up to 1000 issues and can filter the histories by field ID.
  - [fact; source: https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-issue-fields/] Jira field discovery returns both system and custom issue fields, including field IDs, names, and schema metadata.
  - [inference; source: https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-issue-search/; https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-issues/; https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-issue-fields/] Jira can validly measure conversion when an organisation records workaround source information in custom fields or links, searches the candidate issue set with JQL, and reconstructs transition timing from the changelog instead of relying only on current status.

- **B2. GitHub dataset surfaces**
  - [fact; source: https://docs.github.com/en/rest/issues/issues] GitHub issue objects expose state, created and closed timestamps, labels, assignees, milestones, comments, and repository context.
  - [fact; source: https://docs.github.com/en/rest/issues/timeline; https://docs.github.com/en/rest/using-the-rest-api/issue-event-types] GitHub timeline events expose timestamped lifecycle events such as assigned, labeled, closed, commented, and linked events.
  - [inference; source: https://docs.github.com/en/rest/issues/issues; https://docs.github.com/en/rest/issues/timeline; https://docs.github.com/en/rest/using-the-rest-api/issue-event-types] GitHub can support conversion measurement when labels, milestones, linked issues, or repository conventions distinguish workaround signals from governed backlog items, but that validity depends on the organisation enforcing those conventions consistently.
  - [inference; source: https://docs.github.com/en/rest/issues/issues; https://docs.github.com/en/rest/issues/timeline] GitHub public repositories are the strongest public surrogate dataset in scope because they expose both issue records and lifecycle history, but they still miss private workaround demand that never becomes a repository issue.

- **B3. Power Platform workaround-demand datasets**
  - [fact; source: https://learn.microsoft.com/en-us/power-platform/guidance/coe/starter-kit; https://learn.microsoft.com/en-us/power-platform/guidance/coe/setup-core-components] The Center of Excellence (CoE) Starter Kit and its successor admin-center surfaces are designed to give administrators visibility into apps, flows, makers, and usage across a tenant, and the setup guidance says the inventory syncs all resources into tables for admin apps, flows, and dashboards.
  - [fact; source: https://learn.microsoft.com/en-us/power-platform/guidance/coe/setup-auditlog-http-graphapi] The audit-log sync flows gather telemetry such as unique users and launches for apps, and the guidance says that without these flows the dashboard shows blank usage information.
  - [fact; source: https://learn.microsoft.com/en-us/power-platform/guidance/coe/governance-components] The governance components collect support details such as Business Justification, Business Impact, Access Management, Dependencies, Conditions of use, and Mitigation Plan details for apps, flows, bots, connectors, and related resources.
  - [fact; source: https://learn.microsoft.com/en-us/power-platform/admin/power-platform-inventory; https://learn.microsoft.com/en-us/power-platform/admin/inventory-schema; https://learn.microsoft.com/en-us/power-platform/admin/inventory-api] Power Platform inventory exposes owner, creator, created-at, last-modified, environment, and workflow entity fields across apps, flows, agents, environments, and environment groups, and the inventory Application Programming Interface (API) supports joins, projections, counts, and filtered queries over the PowerPlatformResources table.
  - [inference; source: https://learn.microsoft.com/en-us/power-platform/guidance/coe/setup-core-components; https://learn.microsoft.com/en-us/power-platform/guidance/coe/setup-auditlog-http-graphapi; https://learn.microsoft.com/en-us/power-platform/guidance/coe/governance-components; https://learn.microsoft.com/en-us/power-platform/admin/inventory-schema] Power Platform governance datasets are strong workaround-demand sources because they capture locally built solutions, who owns them, how much they are used, and why they exist before any central backlog item is opened.

- **B4. ServiceNow central-demand datasets**
  - [fact; source: https://www.servicenow.com/community/spm-blog/quick-start-guide-for-demand-management/ba-p/2722545] ServiceNow says Demand Management centralizes strategic requests from business to Information Technology, automates steps in the investment decision process, and works for new products, services, and enhancements to existing products or services.
  - [fact; source: https://www.servicenow.com/community/spm-blog/quick-start-guide-for-demand-management/ba-p/2722545] The same ServiceNow guide says the application provides tools for capturing, centralizing, and assessing strategic and operational demands, gives a single location for managing demand information, evaluates competing demands, consolidates intake sources, and creates shared visibility.
  - [inference; source: https://www.servicenow.com/community/spm-blog/quick-start-guide-for-demand-management/ba-p/2722545] A ServiceNow Demand Management dataset is therefore a credible central-backlog target dataset when implemented, because it supplies the governed intake queue against which workaround-origin signals can be matched.

- **C. Join design and denominator choice**
  - [fact; source: https://csrc.nist.gov/publications/detail/sp/800-55/rev-1/final] NIST Special Publication 800-55 says useful measures should be repeatable, quantifiable, comparable, and decision-useful for management and investment choices.
  - [fact; source: https://dora.dev/guides/dora-metrics/] DORA says metric context matters, recommends measuring one application or service at a time, and warns that blended comparisons across disparate systems can mislead.
  - [fact; source: https://learn.microsoft.com/en-us/power-platform/admin/inventory-schema; https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-issue-fields/; https://docs.github.com/en/rest/issues/issues] The consulted schema sources expose stable identifiers, owners, timestamps, environments, issue fields, labels, milestones, and related metadata that can be used as join candidates.
  - [inference; source: https://csrc.nist.gov/publications/detail/sp/800-55/rev-1/final; https://dora.dev/guides/dora-metrics/; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-17-build-mode-failure-vs-do-mode-incident-comparison-denominator.md] The defensible denominator is distinct workaround signals for one application, service, environment, or workflow class over a defined cohort period, because that denominator is closest to the underlying demand being converted and matches the repository's prior denominator-discipline finding that comparable rates need a single realised unit of analysis.
  - [inference; source: https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-issue-search/; https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-issues/; https://docs.github.com/en/rest/issues/issues; https://learn.microsoft.com/en-us/power-platform/admin/inventory-schema; https://www.servicenow.com/community/spm-blog/quick-start-guide-for-demand-management/ba-p/2722545] The minimum join key set is an origin record identifier plus at least one stable context key such as application or service, environment, owning team, workflow class, or linked dependency, because timestamps alone do not distinguish one workaround problem from another.
  - [inference; source: https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-issues/; https://docs.github.com/en/rest/issues/timeline; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-09-system-of-record-bypass-control-deficiencies.md] Many-to-one and one-to-many mappings should be handled with an explicit link table rather than implicit matching, or the metric will double count split demands and merged backlog items.

- **D. Bias and data-quality risks**
  - [fact; source: https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-issues/; https://docs.github.com/en/rest/issues/timeline] Jira changelog histories and GitHub timeline events exist specifically because current issue state alone does not preserve lifecycle timing.
  - [fact; source: https://learn.microsoft.com/en-us/power-platform/admin/power-platform-inventory] Power Platform inventory is a fast-updating current-state inventory and shows resources that appear within about 15 minutes, but the documentation does not describe it as a built-in historical snapshot dataset.
  - [inference; source: https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-issues/; https://docs.github.com/en/rest/issues/timeline; https://learn.microsoft.com/en-us/power-platform/admin/power-platform-inventory] Month-over-month conversion measurement requires retained history or periodic snapshots, because current-state tables alone hide closed, deleted, or reclassified records that no longer appear in the surviving dataset.
  - [inference; source: https://learn.microsoft.com/en-us/power-platform/guidance/coe/governance-components; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-16-do-mode-demand-persistence-and-build-mode-displacement.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-14-citizen-development-rollout-empirical-evidence.md] The largest false-negative risk is hidden demand, because local workarounds that are never inventoried, justified, or escalated will depress the measured conversion rate even when workaround demand is actually rising.
  - [inference; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-09-system-of-record-bypass-control-deficiencies.md; https://learn.microsoft.com/en-us/power-platform/guidance/coe/governance-components; https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-issue-fields/] The largest false-positive risk is weak origin linkage, because records can be linked after the fact or by loose text matching instead of durable origin IDs, which inflates apparent conversion without proving a true source-to-backlog pathway.

### §3 Reasoning

- [inference; source: https://dora.dev/guides/dora-metrics/; https://csrc.nist.gov/publications/detail/sp/800-55/rev-1/final] The evidence supports a two-part answer: there is no consulted public benchmark dataset that directly publishes enterprise workaround-to-backlog conversion, but there are several internal operational datasets with documented fields that can support the metric if they are joined correctly.
- [inference; source: https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-issue-search/; https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-issues/; https://docs.github.com/en/rest/issues/issues; https://docs.github.com/en/rest/issues/timeline; https://learn.microsoft.com/en-us/power-platform/admin/inventory-schema; https://www.servicenow.com/community/spm-blog/quick-start-guide-for-demand-management/ba-p/2722545] The measurement problem is therefore less about finding a single canonical dataset and more about pairing a workaround-signal dataset with a governed-backlog dataset and preserving the link history between them.
- [inference; source: https://learn.microsoft.com/en-us/power-platform/guidance/coe/setup-auditlog-http-graphapi; https://learn.microsoft.com/en-us/power-platform/guidance/coe/governance-components; https://www.servicenow.com/community/spm-blog/quick-start-guide-for-demand-management/ba-p/2722545] The strongest internal design in scope combines a workaround-side telemetry source that records local solution creation and usage with a central intake source that records formal demand qualification and prioritization.
- [inference; source: https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-issues/; https://docs.github.com/en/rest/issues/timeline; https://learn.microsoft.com/en-us/power-platform/admin/power-platform-inventory] History surfaces matter as much as entity tables, because conversion is a rate over time and not merely a cross-sectional count of open records.

### §4 Consistency Check

- [fact; source: https://docs.github.com/en/rest/issues/issues; https://docs.github.com/en/rest/issues/timeline] GitHub is the only consulted source set in scope that also supports a public surrogate dataset, so any statement that "public datasets exist" must stay narrower than the statement that "public benchmark datasets exist."
- [fact; source: https://dora.dev/guides/dora-metrics/; https://csrc.nist.gov/publications/detail/sp/800-55/rev-1/final] The measurement-design claims are bounded to one application or service class and to repeatable, quantifiable, comparable metrics, which keeps the synthesis aligned with the cited guidance.
- [inference; source: https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-issues/; https://docs.github.com/en/rest/issues/timeline; https://learn.microsoft.com/en-us/power-platform/admin/power-platform-inventory] There is no internal contradiction between recommending current-state inventory tables and warning about hidden-history distortion, because the recommendation is to use those tables only when paired with history or periodic snapshots.

### §5 Depth and Breadth Expansion

- [inference; source: https://learn.microsoft.com/en-us/power-platform/guidance/coe/governance-components; https://www.servicenow.com/community/spm-blog/quick-start-guide-for-demand-management/ba-p/2722545] Technical lens: the metric is implementable only where source systems expose stable identifiers and queryable timestamps, which means low-code governance datasets and central demand systems are more useful than narrative-only request channels.
- [inference; source: https://csrc.nist.gov/publications/detail/sp/800-55/rev-1/final; https://dora.dev/guides/dora-metrics/] Economic lens: a valid conversion metric is valuable because it makes backlog-investment decisions comparable over time, but over-engineered cross-system integration should be avoided until the organisation has settled the unit of analysis and origin-link discipline.
- [inference; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-09-system-of-record-bypass-control-deficiencies.md; https://learn.microsoft.com/en-us/power-platform/guidance/coe/governance-components] Governance lens: origin linkage is a control surface as well as an analytics requirement, because weak linkage between workaround artifacts and formal backlog items prevents audit, prioritization, and accountability.
- [inference; source: https://www.servicenow.com/community/spm-blog/quick-start-guide-for-demand-management/ba-p/2722545; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-16-do-mode-demand-persistence-and-build-mode-displacement.md] Historical and behavioural lens: organisations that already centralize demand intake still need explicit escalation habits, because workaround demand can remain local and invisible even when a formal backlog system exists.

### §6 Synthesis

**Executive summary:**

No consulted public benchmark dataset directly measures the rate at which enterprise manual workaround demand becomes formal central Information Technology backlog work, so valid measurement depends on joining internal workaround-signal datasets to governed backlog datasets with durable origin links. [inference; source: https://dora.dev/guides/dora-metrics/; https://learn.microsoft.com/en-us/power-platform/admin/power-platform-inventory; https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-issue-search/; https://docs.github.com/en/rest/issues/issues]
The strongest workaround-side datasets in scope are Power Platform inventory, audit-log, and governance datasets because they record local apps and flows, ownership, usage, and business justification before central escalation. [inference; source: https://learn.microsoft.com/en-us/power-platform/guidance/coe/setup-core-components; https://learn.microsoft.com/en-us/power-platform/guidance/coe/setup-auditlog-http-graphapi; https://learn.microsoft.com/en-us/power-platform/guidance/coe/governance-components; https://learn.microsoft.com/en-us/power-platform/admin/inventory-schema]
A centralized demand or backlog dataset, such as ServiceNow Demand Management or equivalent Jira or GitHub work-item datasets with enforced origin fields, is needed on the target side of the metric. [inference; source: https://www.servicenow.com/community/spm-blog/quick-start-guide-for-demand-management/ba-p/2722545; https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-issue-search/; https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-issues/; https://docs.github.com/en/rest/issues/issues; https://docs.github.com/en/rest/issues/timeline]
The critical design choice is not tool brand but measurement grain: count distinct workaround signals for one service or workflow class, preserve the link table to formal backlog records, and retain history so closed or deleted records do not disappear from the rate. [inference; source: https://csrc.nist.gov/publications/detail/sp/800-55/rev-1/final; https://dora.dev/guides/dora-metrics/; https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-issues/; https://docs.github.com/en/rest/issues/timeline]

**Key findings:**

1. **No consulted public benchmark dataset directly publishes enterprise manual-workaround signals linked to formal central Information Technology backlog outcomes, so external sources in scope are mainly useful for metric design, field discovery, and method testing rather than for direct rate benchmarking.** ([inference]; high confidence; source: https://dora.dev/guides/dora-metrics/; https://learn.microsoft.com/en-us/power-platform/admin/power-platform-inventory; https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-issue-search/; https://docs.github.com/en/rest/issues/issues)
2. **Jira can support conversion measurement when organisations search the candidate issue set with Jira Query Language, preserve custom fields for workaround origin, and use bulk changelog histories instead of current issue status alone to reconstruct backlog entry and completion timing.** ([inference]; high confidence; source: https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-issue-search/; https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-issues/; https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-issue-fields/)
3. **GitHub issue datasets can support the same measurement pattern through state, labels, milestones, timestamps, and timeline events, and public repositories make GitHub the strongest public surrogate dataset in scope for testing conversion logic before applying it to private enterprise data.** ([inference]; medium confidence; source: https://docs.github.com/en/rest/issues/issues; https://docs.github.com/en/rest/issues/timeline; https://docs.github.com/en/rest/using-the-rest-api/issue-event-types)
4. **Power Platform governance datasets provide strong demand-side coverage because inventory records expose owners, environments, and timestamps, audit-log flows add launches and unique-user telemetry, and governance components capture business justification, impact, dependencies, and mitigation details for locally built solutions.** ([inference]; high confidence; source: https://learn.microsoft.com/en-us/power-platform/guidance/coe/setup-core-components; https://learn.microsoft.com/en-us/power-platform/guidance/coe/setup-auditlog-http-graphapi; https://learn.microsoft.com/en-us/power-platform/guidance/coe/governance-components; https://learn.microsoft.com/en-us/power-platform/admin/inventory-schema)
5. **ServiceNow Demand Management is explicitly designed to capture, centralize, assess, and prioritize business and operational demands before promotion into formal delivery work, which makes it a credible target-side dataset when that module is implemented.** ([inference]; low confidence; source: https://www.servicenow.com/community/spm-blog/quick-start-guide-for-demand-management/ba-p/2722545)
6. **The defensible conversion denominator is distinct workaround signals within one application, service, environment, or workflow class, because both metric-design guidance and prior repository work show that mixed units and blended populations make comparison misleading.** ([inference]; high confidence; source: https://csrc.nist.gov/publications/detail/sp/800-55/rev-1/final; https://dora.dev/guides/dora-metrics/; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-17-build-mode-failure-vs-do-mode-incident-comparison-denominator.md)
7. **Month-over-month conversion tracking is invalid without retained history or periodic snapshots, because current-state tables hide deleted, closed, merged, or reclassified records and therefore bias the numerator and denominator toward whatever records still survive later.** ([inference]; high confidence; source: https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-issues/; https://docs.github.com/en/rest/issues/timeline; https://learn.microsoft.com/en-us/power-platform/admin/power-platform-inventory; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-09-system-of-record-bypass-control-deficiencies.md)
8. **The highest-risk failure mode is weak origin linkage between local workaround artifacts and governed backlog records, because text-only matching and late manual linkage can make conversion appear stronger or weaker than it actually is without proving a true escalation pathway.** ([inference]; medium confidence; source: https://learn.microsoft.com/en-us/power-platform/guidance/coe/governance-components; https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-issue-fields/; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-09-system-of-record-bypass-control-deficiencies.md)

**Evidence map:**

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [inference] No consulted public benchmark dataset directly publishes enterprise workaround-to-backlog conversion records. | https://dora.dev/guides/dora-metrics/ ; https://learn.microsoft.com/en-us/power-platform/admin/power-platform-inventory ; https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-issue-search/ ; https://docs.github.com/en/rest/issues/issues | high | Public docs expose metric patterns and schemas, not a cross-org benchmark corpus |
| [inference] Jira supports conversion measurement when issue search, custom fields, and changelog history are used together. | https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-issue-search/ ; https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-issues/ ; https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-issue-fields/ | high | Requires explicit origin-field discipline |
| [inference] GitHub is the strongest public surrogate dataset in scope for testing conversion logic. | https://docs.github.com/en/rest/issues/issues ; https://docs.github.com/en/rest/issues/timeline ; https://docs.github.com/en/rest/using-the-rest-api/issue-event-types | medium | Surrogate only, not direct enterprise benchmark evidence |
| [inference] Power Platform governance datasets provide strong demand-side coverage for local solutions. | https://learn.microsoft.com/en-us/power-platform/guidance/coe/setup-core-components ; https://learn.microsoft.com/en-us/power-platform/guidance/coe/setup-auditlog-http-graphapi ; https://learn.microsoft.com/en-us/power-platform/guidance/coe/governance-components ; https://learn.microsoft.com/en-us/power-platform/admin/inventory-schema | high | Coverage judgment derived from multiple documented fields |
| [inference] ServiceNow Demand Management is a credible target-side dataset when implemented. | https://www.servicenow.com/community/spm-blog/quick-start-guide-for-demand-management/ba-p/2722545 | low | Supported by one readable intake source, so evidence remains thin |
| [inference] Distinct workaround signals per service or workflow class are the defensible denominator. | https://csrc.nist.gov/publications/detail/sp/800-55/rev-1/final ; https://dora.dev/guides/dora-metrics/ ; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-17-build-mode-failure-vs-do-mode-incident-comparison-denominator.md | high | Aligns metric design with comparable unit of analysis |
| [inference] Retained history or periodic snapshots are necessary to avoid bias from counting only surviving records. | https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-issues/ ; https://docs.github.com/en/rest/issues/timeline ; https://learn.microsoft.com/en-us/power-platform/admin/power-platform-inventory ; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-09-system-of-record-bypass-control-deficiencies.md | high | Current-state tables alone are insufficient |
| [inference] Weak origin linkage between source artifacts and backlog items is the main failure mode for the metric. | https://learn.microsoft.com/en-us/power-platform/guidance/coe/governance-components ; https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-issue-fields/ ; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-09-system-of-record-bypass-control-deficiencies.md | medium | Link-table discipline is required |

**Assumptions:**

- [assumption; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-16-do-mode-demand-persistence-and-build-mode-displacement.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-09-system-of-record-bypass-control-deficiencies.md; https://learn.microsoft.com/en-us/power-platform/guidance/coe/governance-components] Manual workaround demand is operationally proxied by local solutions and governance records that exist because the central path did not meet the need quickly enough.
- [assumption; source: https://csrc.nist.gov/publications/detail/sp/800-55/rev-1/final; https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-issues/; https://docs.github.com/en/rest/issues/timeline; https://www.servicenow.com/community/spm-blog/quick-start-guide-for-demand-management/ba-p/2722545] A conversion event should be counted only when the origin signal and target backlog record are linked in a durable system field, relationship, or link table rather than inferred only from text similarity.
- [assumption; source: https://dora.dev/guides/dora-metrics/; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-17-build-mode-failure-vs-do-mode-incident-comparison-denominator.md] Starting at one service or workflow class is preferable to an enterprise-wide blended rate because the application-level measure is more likely to stay comparable and decision-useful.

**Analysis:**

The core evidence pattern is asymmetrical: public sources tell us how to structure the metric, while internal operational systems provide the records needed to compute it. [inference; source: https://dora.dev/guides/dora-metrics/; https://learn.microsoft.com/en-us/power-platform/admin/power-platform-inventory; https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-issue-search/]
That asymmetry makes the workaround-side dataset choice especially important, because demand is usually hidden first in local apps, flows, lists, or issue queues rather than in central portfolio tools. [inference; source: https://learn.microsoft.com/en-us/power-platform/guidance/coe/setup-core-components; https://learn.microsoft.com/en-us/power-platform/guidance/coe/governance-components; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-16-do-mode-demand-persistence-and-build-mode-displacement.md]
Power Platform governance data is strong on that hidden-demand side, while ServiceNow Demand Management is strong on the formal-intake side; Jira and GitHub are flexible enough to play either role when organisations enforce origin fields and lifecycle conventions. [inference; source: https://learn.microsoft.com/en-us/power-platform/guidance/coe/setup-auditlog-http-graphapi; https://www.servicenow.com/community/spm-blog/quick-start-guide-for-demand-management/ba-p/2722545; https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-issues/; https://docs.github.com/en/rest/issues/timeline]
The main trade-off is between faster implementation and stronger validity: text-matched joins are cheaper, but durable origin IDs and history retention are what make the rate auditable and defensible. [inference; source: https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-issue-fields/; https://docs.github.com/en/rest/issues/timeline; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-09-system-of-record-bypass-control-deficiencies.md]
A plausible rival interpretation is that public issue trackers alone are enough because they expose lifecycle fields and events, but those datasets only capture work that has already been raised in a tracked system and therefore cannot directly measure hidden enterprise workaround demand. [inference; source: https://docs.github.com/en/rest/issues/issues; https://docs.github.com/en/rest/issues/timeline; https://learn.microsoft.com/en-us/power-platform/guidance/coe/governance-components]

**Risks, gaps, uncertainties:**

- Public cross-organisational benchmark coverage remains thin, so external comparison of absolute conversion rates is weak even when internal measurement is good. [inference; source: https://dora.dev/guides/dora-metrics/; https://learn.microsoft.com/en-us/power-platform/admin/power-platform-inventory]
- The consulted ServiceNow evidence is sufficient to support centralized-intake claims, but it is thinner than the Microsoft, Atlassian, and GitHub evidence because this item relies mainly on one readable ServiceNow demand-intake source. [inference; source: https://www.servicenow.com/community/spm-blog/quick-start-guide-for-demand-management/ba-p/2722545]
- Hidden local workarounds that never enter inventory, governance, or issue-tracking systems will still bias the denominator downward. [inference; source: https://learn.microsoft.com/en-us/power-platform/guidance/coe/governance-components; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-14-citizen-development-rollout-empirical-evidence.md]
- The evidence base is stronger on schema and measurement design than on published empirical distributions of actual conversion performance. [inference; source: https://dora.dev/guides/dora-metrics/; https://csrc.nist.gov/publications/detail/sp/800-55/rev-1/final]

**Open questions:**

- Which backlog-state transitions should count as "converted" in organisations that use multi-stage triage before formal prioritization?
- How should the metric treat one workaround signal that deliberately spawns several backlog items across integration, data, and user-interface teams?
- What sampling or survey method best estimates hidden workaround demand that never appears in any system-of-record dataset?

### §7 Recursive Review

- Review result: pass
- Acronym audit: first-use expansions checked for Information Technology (IT), DevOps Research and Assessment (DORA), Jira Query Language (JQL), Application Programming Interface (API), Center of Excellence (CoE), and National Institute of Standards and Technology (NIST)
- Claim audit: every factual and inferential claim in the Research Skill Output is labeled and URL-backed or marked as an assumption
- Cross-item integration audit: prior completed items on persistent demand, origin-link failure, citizen-development governance, and denominator design are integrated where they materially sharpen the measurement design

---

## Findings

*(Populated from §6 Synthesis above.)*

### Executive Summary

No consulted public benchmark dataset directly measures the rate at which enterprise manual workaround demand becomes formal central Information Technology backlog work, so valid measurement depends on joining internal workaround-signal datasets to governed backlog datasets with durable origin links. [inference; source: https://dora.dev/guides/dora-metrics/; https://learn.microsoft.com/en-us/power-platform/admin/power-platform-inventory; https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-issue-search/; https://docs.github.com/en/rest/issues/issues]
The strongest workaround-side datasets in scope are Power Platform inventory, audit-log, and governance datasets because they record local apps and flows, ownership, usage, and business justification before central escalation. [inference; source: https://learn.microsoft.com/en-us/power-platform/guidance/coe/setup-core-components; https://learn.microsoft.com/en-us/power-platform/guidance/coe/setup-auditlog-http-graphapi; https://learn.microsoft.com/en-us/power-platform/guidance/coe/governance-components; https://learn.microsoft.com/en-us/power-platform/admin/inventory-schema]
A centralized demand or backlog dataset, such as ServiceNow Demand Management or equivalent Jira or GitHub work-item datasets with enforced origin fields, is needed on the target side of the metric. [inference; source: https://www.servicenow.com/community/spm-blog/quick-start-guide-for-demand-management/ba-p/2722545; https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-issue-search/; https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-issues/; https://docs.github.com/en/rest/issues/issues; https://docs.github.com/en/rest/issues/timeline]
The critical design choice is not tool brand but measurement grain: count distinct workaround signals for one service or workflow class, preserve the link table to formal backlog records, and retain history so closed or deleted records do not disappear from the rate. [inference; source: https://csrc.nist.gov/publications/detail/sp/800-55/rev-1/final; https://dora.dev/guides/dora-metrics/; https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-issues/; https://docs.github.com/en/rest/issues/timeline]

### Key Findings

1. **No consulted public benchmark dataset directly publishes enterprise manual-workaround signals linked to formal central Information Technology backlog outcomes, so external sources in scope are mainly useful for metric design, field discovery, and method testing rather than for direct rate benchmarking.** ([inference]; high confidence; source: https://dora.dev/guides/dora-metrics/; https://learn.microsoft.com/en-us/power-platform/admin/power-platform-inventory; https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-issue-search/; https://docs.github.com/en/rest/issues/issues)
2. **Jira can support conversion measurement when organisations search the candidate issue set with Jira Query Language, preserve custom fields for workaround origin, and use bulk changelog histories instead of current issue status alone to reconstruct backlog entry and completion timing.** ([inference]; high confidence; source: https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-issue-search/; https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-issues/; https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-issue-fields/)
3. **GitHub issue datasets can support the same measurement pattern through state, labels, milestones, timestamps, and timeline events, and public repositories make GitHub the strongest public surrogate dataset in scope for testing conversion logic before applying it to private enterprise data.** ([inference]; medium confidence; source: https://docs.github.com/en/rest/issues/issues; https://docs.github.com/en/rest/issues/timeline; https://docs.github.com/en/rest/using-the-rest-api/issue-event-types)
4. **Power Platform governance datasets provide strong demand-side coverage because inventory records expose owners, environments, and timestamps, audit-log flows add launches and unique-user telemetry, and governance components capture business justification, impact, dependencies, and mitigation details for locally built solutions.** ([inference]; high confidence; source: https://learn.microsoft.com/en-us/power-platform/guidance/coe/setup-core-components; https://learn.microsoft.com/en-us/power-platform/guidance/coe/setup-auditlog-http-graphapi; https://learn.microsoft.com/en-us/power-platform/guidance/coe/governance-components; https://learn.microsoft.com/en-us/power-platform/admin/inventory-schema)
5. **ServiceNow Demand Management is explicitly designed to capture, centralize, assess, and prioritize business and operational demands before promotion into formal delivery work, which makes it a credible target-side dataset when that module is implemented.** ([inference]; low confidence; source: https://www.servicenow.com/community/spm-blog/quick-start-guide-for-demand-management/ba-p/2722545)
6. **The defensible conversion denominator is distinct workaround signals within one application, service, environment, or workflow class, because both metric-design guidance and prior repository work show that mixed units and blended populations make comparison misleading.** ([inference]; high confidence; source: https://csrc.nist.gov/publications/detail/sp/800-55/rev-1/final; https://dora.dev/guides/dora-metrics/; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-17-build-mode-failure-vs-do-mode-incident-comparison-denominator.md)
7. **Month-over-month conversion tracking is invalid without retained history or periodic snapshots, because current-state tables hide deleted, closed, merged, or reclassified records and therefore bias the numerator and denominator toward whatever records still survive later.** ([inference]; high confidence; source: https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-issues/; https://docs.github.com/en/rest/issues/timeline; https://learn.microsoft.com/en-us/power-platform/admin/power-platform-inventory; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-09-system-of-record-bypass-control-deficiencies.md)
8. **The highest-risk failure mode is weak origin linkage between local workaround artifacts and governed backlog records, because text-only matching and late manual linkage can make conversion appear stronger or weaker than it actually is without proving a true escalation pathway.** ([inference]; medium confidence; source: https://learn.microsoft.com/en-us/power-platform/guidance/coe/governance-components; https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-issue-fields/; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-09-system-of-record-bypass-control-deficiencies.md)

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [inference] No consulted public benchmark dataset directly publishes enterprise workaround-to-backlog conversion records. | https://dora.dev/guides/dora-metrics/ ; https://learn.microsoft.com/en-us/power-platform/admin/power-platform-inventory ; https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-issue-search/ ; https://docs.github.com/en/rest/issues/issues | high | Public docs expose metric patterns and schemas, not a cross-org benchmark corpus |
| [inference] Jira supports conversion measurement when issue search, custom fields, and changelog history are used together. | https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-issue-search/ ; https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-issues/ ; https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-issue-fields/ | high | Requires explicit origin-field discipline |
| [inference] GitHub is the strongest public surrogate dataset in scope for testing conversion logic. | https://docs.github.com/en/rest/issues/issues ; https://docs.github.com/en/rest/issues/timeline ; https://docs.github.com/en/rest/using-the-rest-api/issue-event-types | medium | Surrogate only, not direct enterprise benchmark evidence |
| [inference] Power Platform governance datasets provide strong demand-side coverage for local solutions. | https://learn.microsoft.com/en-us/power-platform/guidance/coe/setup-core-components ; https://learn.microsoft.com/en-us/power-platform/guidance/coe/setup-auditlog-http-graphapi ; https://learn.microsoft.com/en-us/power-platform/guidance/coe/governance-components ; https://learn.microsoft.com/en-us/power-platform/admin/inventory-schema | high | Coverage judgment derived from multiple documented fields |
| [inference] ServiceNow Demand Management is a credible target-side dataset when implemented. | https://www.servicenow.com/community/spm-blog/quick-start-guide-for-demand-management/ba-p/2722545 | low | Supported by one readable intake source, so evidence remains thin |
| [inference] Distinct workaround signals per service or workflow class are the defensible denominator. | https://csrc.nist.gov/publications/detail/sp/800-55/rev-1/final ; https://dora.dev/guides/dora-metrics/ ; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-17-build-mode-failure-vs-do-mode-incident-comparison-denominator.md | high | Aligns metric design with comparable unit of analysis |
| [inference] Retained history or periodic snapshots are necessary to avoid bias from counting only surviving records. | https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-issues/ ; https://docs.github.com/en/rest/issues/timeline ; https://learn.microsoft.com/en-us/power-platform/admin/power-platform-inventory ; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-09-system-of-record-bypass-control-deficiencies.md | high | Current-state tables alone are insufficient |
| [inference] Weak origin linkage between source artifacts and backlog items is the main failure mode for the metric. | https://learn.microsoft.com/en-us/power-platform/guidance/coe/governance-components ; https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-issue-fields/ ; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-09-system-of-record-bypass-control-deficiencies.md | medium | Link-table discipline is required |

### Assumptions

- [assumption; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-16-do-mode-demand-persistence-and-build-mode-displacement.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-09-system-of-record-bypass-control-deficiencies.md; https://learn.microsoft.com/en-us/power-platform/guidance/coe/governance-components] Manual workaround demand is operationally proxied by local solutions and governance records that exist because the central path did not meet the need quickly enough.
- [assumption; source: https://csrc.nist.gov/publications/detail/sp/800-55/rev-1/final; https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-issues/; https://docs.github.com/en/rest/issues/timeline; https://www.servicenow.com/community/spm-blog/quick-start-guide-for-demand-management/ba-p/2722545] A conversion event should be counted only when the origin signal and target backlog record are linked in a durable system field, relationship, or link table rather than inferred only from text similarity.
- [assumption; source: https://dora.dev/guides/dora-metrics/; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-17-build-mode-failure-vs-do-mode-incident-comparison-denominator.md] Starting at one service or workflow class is preferable to an enterprise-wide blended rate because the application-level measure is more likely to stay comparable and decision-useful.

### Analysis

The core evidence pattern is asymmetrical: public sources tell us how to structure the metric, while internal operational systems provide the records needed to compute it. [inference; source: https://dora.dev/guides/dora-metrics/; https://learn.microsoft.com/en-us/power-platform/admin/power-platform-inventory; https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-issue-search/]
That asymmetry makes the workaround-side dataset choice especially important, because demand is usually hidden first in local apps, flows, lists, or issue queues rather than in central portfolio tools. [inference; source: https://learn.microsoft.com/en-us/power-platform/guidance/coe/setup-core-components; https://learn.microsoft.com/en-us/power-platform/guidance/coe/governance-components; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-16-do-mode-demand-persistence-and-build-mode-displacement.md]
Power Platform governance data is strong on that hidden-demand side, while ServiceNow Demand Management is strong on the formal-intake side; Jira and GitHub are flexible enough to play either role when organisations enforce origin fields and lifecycle conventions. [inference; source: https://learn.microsoft.com/en-us/power-platform/guidance/coe/setup-auditlog-http-graphapi; https://www.servicenow.com/community/spm-blog/quick-start-guide-for-demand-management/ba-p/2722545; https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-issues/; https://docs.github.com/en/rest/issues/timeline]
The main trade-off is between faster implementation and stronger validity: text-matched joins are cheaper, but durable origin IDs and history retention are what make the rate auditable and defensible. [inference; source: https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-issue-fields/; https://docs.github.com/en/rest/issues/timeline; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-09-system-of-record-bypass-control-deficiencies.md]
A plausible rival interpretation is that public issue trackers alone are enough because they expose lifecycle fields and events, but those datasets only capture work that has already been raised in a tracked system and therefore cannot directly measure hidden enterprise workaround demand. [inference; source: https://docs.github.com/en/rest/issues/issues; https://docs.github.com/en/rest/issues/timeline; https://learn.microsoft.com/en-us/power-platform/guidance/coe/governance-components]

### Risks, Gaps, and Uncertainties

- Public cross-organisational benchmark coverage remains thin, so external comparison of absolute conversion rates is weak even when internal measurement is good. [inference; source: https://dora.dev/guides/dora-metrics/; https://learn.microsoft.com/en-us/power-platform/admin/power-platform-inventory]
- The consulted ServiceNow evidence is sufficient to support centralized-intake claims, but it is thinner than the Microsoft, Atlassian, and GitHub evidence because this item relies mainly on one readable ServiceNow demand-intake source. [inference; source: https://www.servicenow.com/community/spm-blog/quick-start-guide-for-demand-management/ba-p/2722545]
- Hidden local workarounds that never enter inventory, governance, or issue-tracking systems will still bias the denominator downward. [inference; source: https://learn.microsoft.com/en-us/power-platform/guidance/coe/governance-components; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-14-citizen-development-rollout-empirical-evidence.md]
- The evidence base is stronger on schema and measurement design than on published empirical distributions of actual conversion performance. [inference; source: https://dora.dev/guides/dora-metrics/; https://csrc.nist.gov/publications/detail/sp/800-55/rev-1/final]

### Open Questions

- Which backlog-state transitions should count as "converted" in organisations that use multi-stage triage before formal prioritization?
- How should the metric treat one workaround signal that deliberately spawns several backlog items across integration, data, and user-interface teams?
- What sampling or survey method best estimates hidden workaround demand that never appears in any system-of-record dataset?

---

## Output

- Type: knowledge
- Description: Research item identifying which public and internal datasets can support workaround-demand to backlog-conversion measurement, and specifying the join, denominator, and history requirements needed to make the metric defensible. [inference; source: https://dora.dev/guides/dora-metrics/; https://csrc.nist.gov/publications/detail/sp/800-55/rev-1/final; https://learn.microsoft.com/en-us/power-platform/admin/inventory-schema]
- Links:
  - https://learn.microsoft.com/en-us/power-platform/guidance/coe/governance-components
  - https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-issues/
  - https://www.servicenow.com/community/spm-blog/quick-start-guide-for-demand-management/ba-p/2722545
