---
review_count: 2
title: "Tracking How Work Travels Across Organisational Systems"
added: 2026-03-15
status: completed
priority: medium  # low | medium | high
blocks: []  # slugs (filename without .md) of backlog items that cannot start until this one is complete
tags: [knowledge-management, work-tracking, sharepoint, confluence, ado, jira, git, monitoring, data-platform, provenance]
started: 2026-03-22
completed: 2026-03-22
output: [knowledge]
---

# Tracking How Work Travels Across Organisational Systems

## Research Question

Can we track how a unit of 'Work' -- an idea or concept -- travels across organisational systems (SharePoint, Confluence, Azure DevOps (ADO)/Jira, Git, monitoring systems, and data platforms), and what mechanisms or patterns exist to trace its full lifecycle from inception to delivery and beyond?

## Scope

**In scope:**
- Definition of 'Work' as a traceable unit: idea, requirement, task, change, incident, or feature
- Systems where Work manifests: SharePoint (documents/wikis), Confluence (wikis/pages), Azure DevOps (ADO)/Jira (backlog/issues), Git (code/commits/pull requests (PRs)), monitoring systems (alerts/incidents), data platforms (pipelines/jobs)
- Existing cross-system linking mechanisms: issue keys in commit messages, pull request references in deployment records, alert-to-incident linkage, pipeline job references
- Industry patterns and standards for work provenance (for example OpenLineage, Value Stream Mapping (VSM), software supply chain provenance)
- Feasibility of building an organisation-wide Work provenance graph

**Out of scope:**
- Deep implementation guides for any single tool's internal data model
- Security, access control, or governance policies for each system
- Change management or process redesign recommendations

**Constraints:** Publicly accessible documentation, open-source tooling, and general industry literature; no access to proprietary organisational data.

## Context

Work in modern software organisations does not live in a single system. An idea starts as a conversation or a document in SharePoint or Confluence, becomes a ticket in ADO or Jira, gets implemented as commits and pull requests in Git, is shipped via a pipeline, generates alerts in monitoring, and may ultimately shape data in a data platform. Each system maintains its own identity for the same unit of work, often with loose or hand-crafted links between them. This fragmentation makes it difficult to answer questions like: "Where did this feature come from?", "Which deployment caused this alert?", or "What business goal does this pipeline serve?" Understanding whether and how these links can be made systematic -- and what tooling already exists -- informs decisions about observability, onboarding, and organisational knowledge management.

## Approach

1. Define 'Work' as a multi-stage artefact and map its typical lifecycle stages across the six system categories (document -> ticket -> commit/pull request -> deployment -> alert/incident -> data job).
2. Survey the linking mechanisms that each system exposes natively (for example Jira smart commits, ADO `AB#nnn` syntax in Git, GitHub Deployments Application Programming Interface (API), alert annotations).
3. Identify existing open-source or commercial tooling that attempts cross-system work tracing (for example LinearB, Sleuth, Allma, OpenLineage, value stream management platforms).
4. Examine the OpenLineage specification and similar provenance standards to assess their applicability beyond data pipelines to the broader Work lifecycle.
5. Assess feasibility: what data is accessible via Application Programming Interfaces (APIs), what is locked in unstructured text, and what inference (for example semantic matching) would be required to fill gaps?
6. Synthesise: what is the minimum viable approach for tracing Work end-to-end in a typical organisation, and what are the blockers?

## Sources

- [x] https://openlineage.io -- OpenLineage overview; confirms the project is an open framework for data lineage collection and analysis
- [x] https://openlineage.io/docs/spec/object-model/ -- current OpenLineage object model; jobs, runs, datasets, and design-time/runtime events
- [x] https://openlineage.io/docs/1.38.0/guides/facets -- current OpenLineage facets guide; standard and custom metadata extension points
- [x] https://docs.github.com/en/issues/tracking-your-work-with-issues/linking-a-pull-request-to-an-issue -- GitHub issue and pull request linking
- [x] https://learn.microsoft.com/en-us/azure/devops/boards/github/link-to-from-github -- Azure Boards to GitHub linking with `AB#` references, branch links, and integrated build links
- [x] https://support.atlassian.com/jira-software-cloud/docs/process-issues-with-smart-commits/ -- current Jira Smart Commits documentation (replaces the original listed web link, which now returns 404)
- [x] https://support.atlassian.com/platform-experiences/docs/use-smart-links-to-view-projects-in-confluence/ -- Confluence Smart Links for Jira and Atlassian project links
- [x] https://learn.microsoft.com/en-us/graph/api/resources/driveitem?view=graph-rest-1.0 -- SharePoint document-library items as `driveItem` / `listItem` resources with stable identifiers
- [x] https://docs.github.com/en/rest/deployments/deployments -- GitHub deployment and deployment status events for release-stage traceability
- [x] https://support.pagerduty.com/main/docs/recent-changes -- PagerDuty change events and incident change-correlation model for monitoring-stage linkage
- [x] https://linearb.zendesk.com/hc/en-us/articles/45768080630043-Integrating-Jira-Cloud-into-LinearB-OAuth-2-0 -- LinearB documentation on matching Jira issue keys to branches, PRs, commits, and incidents
- [x] https://www.sleuth.io/post/dora-metrics-explained/ -- Sleuth article on DevOps Research and Assessment (DORA) metrics, including deployment frequency, change lead time, change failure rate, and mean time to recovery (MTTR)
- [x] https://www.sleuth.io -- checked because it was in the original item; the site now markets agent-governance products rather than the older DORA-tracing positioning
- [x] https://asq.org/quality-resources/lean/value-stream-mapping -- American Society for Quality overview of Value Stream Mapping (VSM) as a lean flow-mapping method
- [x] Prior completed research: `Research/completed/2026-03-21-dependency-mapping-dotnet-terraform-dynatrace.md`
- [x] Prior completed research: `Research/completed/2026-03-15-latent-concept-extraction-confluence.md`
- [x] Prior completed research: `Research/completed/2026-03-08-servicenow-process-mapping.md`
- [x] Prior completed research: `Research/completed/2026-03-03-knowledge-linking-connected-corpus.md`

---

## Research Skill Output

*(Full output from running the research skill -- retained verbatim in the completed item. Sections 0-5 are the investigation; Section 6 seeds the Findings section below.)*

### §0 Initialise

- **[fact]** The research question asks whether one unit of organisational work can be traced across document systems, issue trackers, source control, deployment tooling, monitoring, and data platforms, then reconstructed as a single lifecycle view. Source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-15-tracking-work-across-systems.md
- **[fact]** The scope is bounded to public documentation, open-source tooling, and general industry literature, so the answer must focus on patterns that do not depend on private enterprise schemas. Source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-15-tracking-work-across-systems.md
- **[fact]** The deliverable must cover native linking mechanisms, provenance standards, feasibility limits, and a minimum viable end-to-end approach rather than a single-tool recommendation. Source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-15-tracking-work-across-systems.md
- **[fact]** Prior completed repository work already established two adjacent constraints: Confluence-derived knowledge extraction depends on provenance and content hygiene, and dependency maps become reliable only when multiple partial system views are merged rather than treated as a single source of truth. Sources: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-15-latent-concept-extraction-confluence.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-21-dependency-mapping-dotnet-terraform-dynatrace.md.
- **[assumption]** The missing local `.github/skills/research/SKILL.md` file means the fallback numbered research process in `research-prompt.md` is the operative method for this run. **Justification:** the repository does not contain the named skill file, while `research-prompt.md` defines the same required Sections 0-7 structure. Sources: https://github.com/davidamitchell/Research/blob/main/research-prompt.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-15-tracking-work-across-systems.md
- **[fact]** Output format for this item is a structured knowledge artefact with labelled claims, explicit citations, a seeded Findings section, and an evidence map that re-states each key finding. Sources: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-15-tracking-work-across-systems.md; https://github.com/davidamitchell/Research/blob/main/research-prompt.md

### §1 Question Decomposition

- **Root question:** Can one unit of work be traced end-to-end across organisational systems, and if so, what mechanism makes that possible?

- **A. Work identity and lifecycle model**
  - A1. What counts as the same unit of work across documents, tickets, code changes, deployments, incidents, and data jobs?
  - A2. Which lifecycle stages have strong native identifiers, and which stages rely on loose references or inference?

- **B. Native linking mechanisms by surface**
  - B1. What native linkage exists from issue trackers to Git commits, branches, and pull requests?
  - B2. What native linkage exists from code change to deployment?
  - B3. What native linkage exists from deployment to incident or monitoring event?
  - B4. What native linkage exists from documents or wiki pages to tracked work?

- **C. Standards and tooling**
  - C1. What does OpenLineage model natively, and where does its entity model stop?
  - C2. What do commercial work-tracing tools actually correlate across systems?
  - C3. What does Value Stream Mapping contribute, and what does it not preserve?

- **D. Feasibility and architecture**
  - D1. What data can be harvested deterministically from current systems by identifier, web link, or webhook event?
  - D2. Where is semantic inference required because the connection is implicit or missing?
  - D3. What is the minimum viable provenance graph for a typical organisation?

### §2 Investigation

#### A. Work identity and lifecycle stages

- **[fact]** GitHub issues and pull requests can be explicitly linked, and closing keywords in pull request descriptions or commit messages close linked issues when merged into the default branch; this gives a strong local identity bridge between issue and code-review objects but only inside GitHub's own model. Source: https://docs.github.com/en/issues/tracking-your-work-with-issues/linking-a-pull-request-to-an-issue
- **[fact]** Azure Boards can link work items to GitHub commits, pull requests, branches, and builds, and the `AB#ID` syntax in commit messages or pull request descriptions creates these links and can transition work-item state. Source: https://learn.microsoft.com/en-us/azure/devops/boards/github/link-to-from-github
- **[fact]** Jira Smart Commits let commit messages comment on issues, record time, and transition workflow state when the commit contains a Jira issue key and command syntax such as `#comment`, `#time`, or a transition command. Source: https://support.atlassian.com/jira-software-cloud/docs/process-issues-with-smart-commits/
- **[inference]** The strongest native lifecycle identity in mainstream engineering tooling is therefore not a universal work identifier but a chain of local references: issue key or work-item identifier -> branch/commit/pull request -> build/deployment object. Sources: https://docs.github.com/en/issues/tracking-your-work-with-issues/linking-a-pull-request-to-an-issue; https://learn.microsoft.com/en-us/azure/devops/boards/github/link-to-from-github; https://support.atlassian.com/jira-software-cloud/docs/process-issues-with-smart-commits/

#### B. Document and wiki surfaces

- **[fact]** SharePoint document-library artefacts are exposed in Microsoft Graph as `driveItem` resources, and items in SharePoint document libraries can also be represented as `listItem` resources; both are addressable by unique identifier. Source: https://learn.microsoft.com/en-us/graph/api/resources/driveitem?view=graph-rest-1.0
- **[fact]** Confluence Smart Links render pasted Jira or Atlassian project links with visible status and preserve permission checks, which means Confluence can display linked work context but does not itself create a cross-system work model beyond stored links. Source: https://support.atlassian.com/platform-experiences/docs/use-smart-links-to-view-projects-in-confluence/
- **[inference]** SharePoint and Confluence give stable document nodes and linkable web links, but they usually act as entry points or context containers rather than authoritative identity systems for work provenance. Sources: https://learn.microsoft.com/en-us/graph/api/resources/driveitem?view=graph-rest-1.0; https://support.atlassian.com/platform-experiences/docs/use-smart-links-to-view-projects-in-confluence/
- **[assumption]** In most organisations, document-to-ticket linkage will require either explicit pasted links, metadata fields, or naming conventions because the public docs reviewed here do not show a native, vendor-neutral way to declare "this page is the origin of work item X." **Justification:** the reviewed SharePoint and Confluence docs expose addressable artefacts and rendered links, but not a shared provenance schema. Sources: https://learn.microsoft.com/en-us/graph/api/resources/driveitem?view=graph-rest-1.0; https://support.atlassian.com/platform-experiences/docs/use-smart-links-to-view-projects-in-confluence/

#### C. Deployment and incident stages

- **[fact]** GitHub deployments are requests to deploy a specific ref, and GitHub emits both `deployment` and `deployment_status` events with environment, state, optional description, and optional `log_url`; this creates a machine-readable release-stage object linked to a commit SHA or ref. Source: https://docs.github.com/en/rest/deployments/deployments
- **[fact]** Azure Boards can automatically create an "Integrated in build" link on work items for pipelines, which extends work-item traceability from issue and pull request objects into build artefacts. Source: https://learn.microsoft.com/en-us/azure/devops/boards/github/link-to-from-github
- **[fact]** PagerDuty change events represent deploys, builds, configuration updates, and similar service changes; they can be shown on incidents, include links such as the pull request and repository, and are correlated to incidents by time, related service, or machine-learning-based similarity. Source: https://support.pagerduty.com/main/docs/recent-changes
- **[inference]** The deployment-to-incident step is traceable when change-event tooling is deliberately configured, but it is weaker and more probabilistic than issue-to-commit linking because correlation often depends on time windows, service topology, or learned association rather than a single required key. Sources: https://docs.github.com/en/rest/deployments/deployments; https://support.pagerduty.com/main/docs/recent-changes

#### D. Data-platform lineage and standards

- **[fact]** OpenLineage models lineage around three core entities -- Job, Run, and Dataset -- and supports runtime `RunEvent` plus design-time `JobEvent` and `DatasetEvent` metadata updates. Source: https://openlineage.io/docs/spec/object-model/
- **[fact]** OpenLineage facets attach metadata such as source code location and version, schema, ownership, lifecycle state changes, and custom project-specific extensions to Jobs, Runs, and Datasets. Sources: https://openlineage.io/docs/spec/object-model/; https://openlineage.io/docs/1.38.0/guides/facets
- **[inference]** OpenLineage is strong for pipeline and dataset provenance because it captures job execution and data transformation events, but its native object model does not directly include documents, tickets, pull requests, deployments, or incidents; extending it to those surfaces would require custom modelling outside the core standard. Sources: https://openlineage.io/docs/spec/object-model/; https://openlineage.io/docs/1.38.0/guides/facets
- **[fact]** Value Stream Mapping is a lean tool that uses a flowchart to document every step in a process and combines material-processing steps with information flow and related data. Source: https://asq.org/quality-resources/lean/value-stream-mapping
- **[inference]** Value Stream Mapping is therefore useful as a conceptual framing for where work flows, but not sufficient as a machine-readable provenance mechanism because it does not define persistent cross-system identifiers or event schemas. Source: https://asq.org/quality-resources/lean/value-stream-mapping

#### E. Commercial work-tracing tools

- **[fact]** LinearB documents that its Jira integration syncs Jira projects, boards, issues, and incidents, and that its matching logic associates Git branches, pull request titles, and commit messages to Jira issues by issue key conventions. Source: https://linearb.zendesk.com/hc/en-us/articles/45768080630043-Integrating-Jira-Cloud-into-LinearB-OAuth-2-0
- **[fact]** Sleuth's DevOps Research and Assessment (DORA) article frames deployment frequency, change lead time, change failure rate, and mean time to recovery as metrics that connect individual changes and deployments to production outcomes and recovery performance. Source: https://www.sleuth.io/post/dora-metrics-explained/
- **[fact]** The originally listed `https://www.sleuth.io` home page now markets agent-governance products rather than DORA-tracing products, so product-positioning evidence from that domain is historically unstable and must be taken from dated subpages rather than the current home page. Source: https://www.sleuth.io
- **[inference]** Commercial tools add value mainly by normalising local identifiers and correlating operational signals across systems; they do not remove the underlying need for explicit keys, web links, service maps, or integration-specific metadata. Sources: https://linearb.zendesk.com/hc/en-us/articles/45768080630043-Integrating-Jira-Cloud-into-LinearB-OAuth-2-0; https://support.pagerduty.com/main/docs/recent-changes; https://www.sleuth.io/post/dora-metrics-explained/

#### F. Feasibility and minimum viable architecture

- **[fact]** Public documentation across GitHub, Azure Boards, Jira, PagerDuty, SharePoint, Confluence, and OpenLineage consistently exposes machine-readable objects identified by local identifiers, namespaced names, web links, or event payloads. Sources: https://docs.github.com/en/issues/tracking-your-work-with-issues/linking-a-pull-request-to-an-issue; https://learn.microsoft.com/en-us/azure/devops/boards/github/link-to-from-github; https://support.atlassian.com/jira-software-cloud/docs/process-issues-with-smart-commits/; https://support.pagerduty.com/main/docs/recent-changes; https://learn.microsoft.com/en-us/graph/api/resources/driveitem?view=graph-rest-1.0; https://support.atlassian.com/platform-experiences/docs/use-smart-links-to-view-projects-in-confluence/; https://openlineage.io/docs/spec/object-model/
- **[inference]** An organisation-wide Work provenance graph is technically feasible if it treats those local objects as graph nodes and records typed edges such as `documents`, `implements`, `deploys`, `changes`, `correlates-with`, and `produces`, each with source provenance and confidence. Sources: https://docs.github.com/en/rest/deployments/deployments; https://support.pagerduty.com/main/docs/recent-changes; https://openlineage.io/docs/spec/object-model/
- **[inference]** The irreducible blockers are semantic drift at the document layer, inconsistent naming or key discipline in commits and pull requests, missing deployment/change-event instrumentation, and the fact that some late-stage correlations are probabilistic rather than deterministic. Sources: https://support.atlassian.com/platform-experiences/docs/use-smart-links-to-view-projects-in-confluence/; https://support.atlassian.com/jira-software-cloud/docs/process-issues-with-smart-commits/; https://support.pagerduty.com/main/docs/recent-changes
- **[assumption]** A practical minimum viable graph should prefer explicit keys and web links over semantic matching, and reserve inference for gap-filling after deterministic links are exhausted. **Justification:** every reviewed system offers some stable identifier surface, while the weaker parts of the lifecycle are exactly where correlation confidence drops. Sources: https://learn.microsoft.com/en-us/azure/devops/boards/github/link-to-from-github; https://docs.github.com/en/rest/deployments/deployments; https://support.pagerduty.com/main/docs/recent-changes; https://openlineage.io/docs/spec/object-model/

### §3 Reasoning

- **[fact]** Deterministic links exist where a system explicitly stores another system's identifier or web link, such as `AB#123` links, Jira issue keys in commits, GitHub issue keywords, deployment objects tied to refs, and PagerDuty change events carrying pull request or repository links. Sources: https://learn.microsoft.com/en-us/azure/devops/boards/github/link-to-from-github; https://support.atlassian.com/jira-software-cloud/docs/process-issues-with-smart-commits/; https://docs.github.com/en/issues/tracking-your-work-with-issues/linking-a-pull-request-to-an-issue; https://docs.github.com/en/rest/deployments/deployments; https://support.pagerduty.com/main/docs/recent-changes
- **[fact]** Standardised provenance is strongest in the data-platform segment because OpenLineage natively models Jobs, Runs, and Datasets and defines extensible metadata facets around them. Sources: https://openlineage.io/docs/spec/object-model/; https://openlineage.io/docs/1.38.0/guides/facets
- **[inference]** The organisational challenge is not that work cannot be traced at all, but that different lifecycle segments use different identity systems with different strengths, so an end-to-end answer requires composition rather than discovery of a hidden universal ID. Sources: https://learn.microsoft.com/en-us/azure/devops/boards/github/link-to-from-github; https://support.atlassian.com/jira-software-cloud/docs/process-issues-with-smart-commits/; https://openlineage.io/docs/spec/object-model/
- **[inference]** A provenance graph is the natural synthesis layer because it can preserve heterogeneous node types, edge provenance, and confidence without forcing all systems into one vendor's object model. Sources: https://openlineage.io/docs/spec/object-model/; https://docs.github.com/en/rest/deployments/deployments; https://support.pagerduty.com/main/docs/recent-changes

### §4 Consistency Check

- **[fact]** No reviewed source contradicted the claim that issue trackers and Git systems offer stronger native linkage than documents and monitoring systems; the disagreement is in degree of automation, not in whether those links exist. Sources: https://docs.github.com/en/issues/tracking-your-work-with-issues/linking-a-pull-request-to-an-issue; https://learn.microsoft.com/en-us/azure/devops/boards/github/link-to-from-github; https://support.atlassian.com/jira-software-cloud/docs/process-issues-with-smart-commits/; https://support.atlassian.com/platform-experiences/docs/use-smart-links-to-view-projects-in-confluence/
- **[fact]** The originally listed Jira Smart Commits web link and Azure deployment-gates web link have drifted, so current canonical documentation had to replace them; this is a source-maintenance issue, not a contradiction in the substantive findings. Sources: https://support.atlassian.com/jira-software-cloud/docs/process-issues-with-smart-commits/; https://learn.microsoft.com/en-us/azure/devops/pipelines/release/deployment-gates
- **[fact]** The originally listed Sleuth home page no longer supports the same product claim implied by the item; this was resolved by separating present-day site positioning from older DORA-related material on the same domain. Sources: https://www.sleuth.io; https://www.sleuth.io/post/dora-metrics-explained/
- **[inference]** The evidence is internally consistent if the answer distinguishes deterministic linkage, correlation-based linkage, and conceptual mapping rather than treating them as equivalent forms of traceability. Sources: https://docs.github.com/en/issues/tracking-your-work-with-issues/linking-a-pull-request-to-an-issue; https://learn.microsoft.com/en-us/azure/devops/boards/github/link-to-from-github; https://support.atlassian.com/platform-experiences/docs/use-smart-links-to-view-projects-in-confluence/; https://support.pagerduty.com/main/docs/recent-changes; https://openlineage.io/docs/spec/object-model/

### §5 Depth and Breadth Expansion

- **[technical][inference]** The technically minimal graph schema is small: node type, native identifier or web link, system of origin, timestamp, typed edge, evidence source, and confidence. That is enough to merge documents, work items, commits, deployments, incidents, and data jobs without flattening their semantics. Sources: https://learn.microsoft.com/en-us/graph/api/resources/driveitem?view=graph-rest-1.0; https://docs.github.com/en/rest/deployments/deployments; https://openlineage.io/docs/spec/object-model/
- **[economic][inference]** The main cost driver is not API access but operational discipline: branch naming, commit-message hygiene, deployment instrumentation, and service mapping all require ongoing behaviour and governance. Sources: https://support.atlassian.com/jira-software-cloud/docs/process-issues-with-smart-commits/; https://learn.microsoft.com/en-us/azure/devops/boards/github/link-to-from-github; https://support.pagerduty.com/main/docs/recent-changes
- **[behavioural][inference]** Teams will trust the graph only if each edge carries provenance and confidence, because some edges are direct declarations while others are correlations or inferred joins. Sources: https://support.pagerduty.com/main/docs/recent-changes; https://openlineage.io/docs/1.38.0/guides/facets
- **[historical][inference]** Value Stream Mapping remains useful for describing end-to-end flow, but modern operational systems now expose evented objects that allow machine-readable provenance for lifecycle segments that VSM still treats as mapped process steps rather than typed events. Sources: https://asq.org/quality-resources/lean/value-stream-mapping; https://docs.github.com/en/rest/deployments/deployments; https://openlineage.io/docs/spec/object-model/

### §6 Synthesis

**Executive summary:**

- **[inference]** End-to-end work tracking across organisational systems is feasible, but only as a multi-system provenance graph assembled from local identifiers, web links, and event payloads rather than as a single native identifier shared by SharePoint, Confluence, Jira, Azure Boards, Git, monitoring, and data platforms. Sources: https://learn.microsoft.com/en-us/graph/api/resources/driveitem?view=graph-rest-1.0; https://support.atlassian.com/platform-experiences/docs/use-smart-links-to-view-projects-in-confluence/; https://learn.microsoft.com/en-us/azure/devops/boards/github/link-to-from-github; https://support.atlassian.com/jira-software-cloud/docs/process-issues-with-smart-commits/; https://docs.github.com/en/rest/deployments/deployments; https://support.pagerduty.com/main/docs/recent-changes; https://openlineage.io/docs/spec/object-model/
- **[inference]** Native linkage is strongest from ticket to code to build or deployment because GitHub, Azure Boards, and Jira all support explicit cross-references between work items, commits, pull requests, branches, and builds. Sources: https://docs.github.com/en/issues/tracking-your-work-with-issues/linking-a-pull-request-to-an-issue; https://learn.microsoft.com/en-us/azure/devops/boards/github/link-to-from-github; https://support.atlassian.com/jira-software-cloud/docs/process-issues-with-smart-commits/
- **[fact]** Document systems and monitoring systems expose addressable artefacts and events, but they usually need explicit links, service mapping, or correlation logic to join into the same lifecycle view. Sources: https://learn.microsoft.com/en-us/graph/api/resources/driveitem?view=graph-rest-1.0; https://support.atlassian.com/platform-experiences/docs/use-smart-links-to-view-projects-in-confluence/; https://support.pagerduty.com/main/docs/recent-changes
- **[fact]** OpenLineage provides the clearest standard model for the data-platform segment, but its native entities stop at Jobs, Runs, and Datasets, so broader work provenance needs a super-graph or custom extension layer. Sources: https://openlineage.io/docs/spec/object-model/; https://openlineage.io/docs/1.38.0/guides/facets
- **[inference]** The minimum viable approach is to standardise one canonical work key at the issue layer, harvest every deterministic link exposed by current tools, add typed deployment and incident events, and attach provenance plus confidence to every graph edge before using semantic inference for the remaining gaps. Sources: https://learn.microsoft.com/en-us/azure/devops/boards/github/link-to-from-github; https://support.atlassian.com/jira-software-cloud/docs/process-issues-with-smart-commits/; https://docs.github.com/en/rest/deployments/deployments; https://support.pagerduty.com/main/docs/recent-changes; https://openlineage.io/docs/spec/object-model/

**Key findings:**

1. **[fact][high confidence]** Azure Boards, Jira Software, and GitHub all support explicit issue-to-code linkage, but they do so through local conventions such as `AB#123`, Jira issue keys in commit text, and pull request closing keywords rather than through a shared cross-vendor work identifier. Sources: https://learn.microsoft.com/en-us/azure/devops/boards/github/link-to-from-github; https://support.atlassian.com/jira-software-cloud/docs/process-issues-with-smart-commits/; https://docs.github.com/en/issues/tracking-your-work-with-issues/linking-a-pull-request-to-an-issue
2. **[fact][high confidence]** SharePoint and Confluence provide stable document or page nodes that can anchor provenance, but their public documentation shows them primarily as addressable content surfaces and rendered links, not as authoritative lifecycle registries for engineering work. Sources: https://learn.microsoft.com/en-us/graph/api/resources/driveitem?view=graph-rest-1.0; https://support.atlassian.com/platform-experiences/docs/use-smart-links-to-view-projects-in-confluence/
3. **[inference][high confidence]** Release-stage traceability is materially stronger when deployments are represented as first-class objects, because GitHub deployment records attach environment and status data to a specific ref while Azure Boards can also attach integrated build evidence back to the originating work item. Sources: https://docs.github.com/en/rest/deployments/deployments; https://learn.microsoft.com/en-us/azure/devops/boards/github/link-to-from-github
4. **[inference][medium confidence]** Monitoring-stage linkage is achievable but weaker than code-stage linkage, because PagerDuty change correlation can connect incidents to recent deploy or change events through time, related service, and learned similarity rather than by requiring one mandatory explicit work key. Sources: https://support.pagerduty.com/main/docs/recent-changes
5. **[fact][high confidence]** OpenLineage is an effective provenance standard for data jobs and datasets because it models jobs, runs, datasets, and extensible facets, but it does not natively cover documents, issue trackers, pull requests, deployments, or incidents. Sources: https://openlineage.io/docs/spec/object-model/; https://openlineage.io/docs/1.38.0/guides/facets
6. **[inference][medium confidence]** Commercial tracing products such as LinearB and the older Sleuth positioning add value mainly by normalising existing identifiers and correlating operational signals, which means their usefulness still depends on disciplined issue-key usage, deployment events, and service mapping in the underlying systems. Sources: https://linearb.zendesk.com/hc/en-us/articles/45768080630043-Integrating-Jira-Cloud-into-LinearB-OAuth-2-0; https://www.sleuth.io/post/dora-metrics-explained/; https://support.pagerduty.com/main/docs/recent-changes
7. **[inference][high confidence]** A practical organisation-wide answer is therefore not a monolithic system of record but a provenance graph that stores heterogeneous node types and typed edges with evidence, because each platform owns only one slice of the lifecycle and none owns the whole journey. Sources: https://learn.microsoft.com/en-us/graph/api/resources/driveitem?view=graph-rest-1.0; https://docs.github.com/en/rest/deployments/deployments; https://openlineage.io/docs/spec/object-model/
8. **[inference][high confidence]** The minimum viable implementation should begin at the issue layer as the canonical work key, capture deterministic joins first, and then use selective semantic or correlation-based inference only where document origins, incidents, or downstream data jobs cannot be attached explicitly. Sources: https://learn.microsoft.com/en-us/azure/devops/boards/github/link-to-from-github; https://support.atlassian.com/jira-software-cloud/docs/process-issues-with-smart-commits/; https://support.pagerduty.com/main/docs/recent-changes; https://openlineage.io/docs/spec/object-model/

**Evidence map:**

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [fact] Issue trackers and Git tools link through local conventions, not a shared cross-vendor identifier. | https://learn.microsoft.com/en-us/azure/devops/boards/github/link-to-from-github; https://support.atlassian.com/jira-software-cloud/docs/process-issues-with-smart-commits/; https://docs.github.com/en/issues/tracking-your-work-with-issues/linking-a-pull-request-to-an-issue | high | Strong convergence across three primary vendor docs. |
| [fact] Documents and wiki pages are stable nodes but weak provenance authorities. | https://learn.microsoft.com/en-us/graph/api/resources/driveitem?view=graph-rest-1.0; https://support.atlassian.com/platform-experiences/docs/use-smart-links-to-view-projects-in-confluence/ | high | Strong evidence for addressability, weak evidence for lifecycle ownership. |
| [inference] Deployments become strong provenance nodes when represented as first-class deployment objects. | https://docs.github.com/en/rest/deployments/deployments; https://learn.microsoft.com/en-us/azure/devops/boards/github/link-to-from-github | high | Deployment refs, environment fields, and build links are explicit. |
| [inference] Incident linkage is often correlation-based rather than deterministic. | https://support.pagerduty.com/main/docs/recent-changes | medium | Primary source is strong, but pattern is vendor-specific rather than universal. |
| [fact] OpenLineage is robust for data-platform provenance but narrower than whole-work provenance. | https://openlineage.io/docs/spec/object-model/; https://openlineage.io/docs/1.38.0/guides/facets | high | Core entities stop at Job, Run, Dataset. |
| [fact] Commercial tools mainly normalise existing identifiers and signals. | https://linearb.zendesk.com/hc/en-us/articles/45768080630043-Integrating-Jira-Cloud-into-LinearB-OAuth-2-0; https://www.sleuth.io/post/dora-metrics-explained/; https://support.pagerduty.com/main/docs/recent-changes | medium | Evidence is credible but partly product-positioning rather than neutral benchmarking. |
| [inference] A provenance graph is the natural organisation-wide synthesis layer. | https://learn.microsoft.com/en-us/graph/api/resources/driveitem?view=graph-rest-1.0; https://docs.github.com/en/rest/deployments/deployments; https://openlineage.io/docs/spec/object-model/ | high | Inference follows directly from heterogeneous but addressable node types. |
| [inference] Minimum viable approach should start with issue-layer canonical keys and deterministic joins. | https://learn.microsoft.com/en-us/azure/devops/boards/github/link-to-from-github; https://support.atlassian.com/jira-software-cloud/docs/process-issues-with-smart-commits/; https://support.pagerduty.com/main/docs/recent-changes; https://openlineage.io/docs/spec/object-model/ | high | Best-supported architecture pattern from the evidence set. |

**Assumptions:**

- **[assumption]** Most organisations will choose an issue or work-item identifier as the canonical work key rather than a document identifier. **Justification:** reviewed tooling gives the strongest explicit joins around work items, commits, pull requests, and builds. Sources: https://learn.microsoft.com/en-us/azure/devops/boards/github/link-to-from-github; https://support.atlassian.com/jira-software-cloud/docs/process-issues-with-smart-commits/
- **[assumption]** Semantic matching should be a secondary repair mechanism rather than the default join strategy. **Justification:** deterministic identifiers and web links exist across most reviewed systems, while correlation quality falls at the exact points where explicit linkage is absent. Sources: https://support.pagerduty.com/main/docs/recent-changes; https://openlineage.io/docs/spec/object-model/
- **[assumption]** Documents remain valuable provenance nodes even when they are not authoritative identifiers, because they capture early intent and decision context. **Justification:** SharePoint and Confluence both expose stable addressable artefacts that can be linked into a graph. Sources: https://learn.microsoft.com/en-us/graph/api/resources/driveitem?view=graph-rest-1.0; https://support.atlassian.com/platform-experiences/docs/use-smart-links-to-view-projects-in-confluence/

**Analysis:**

- **[fact]** The reviewed systems form three traceability regimes: deterministic joins at the issue/code/build layer, evented joins at the deployment/data layer, and correlation or manual-link joins at the document and incident layers. Sources: https://learn.microsoft.com/en-us/azure/devops/boards/github/link-to-from-github; https://docs.github.com/en/rest/deployments/deployments; https://support.pagerduty.com/main/docs/recent-changes; https://openlineage.io/docs/spec/object-model/
- **[inference]** This regime split explains why organisations often feel that work is "almost" traceable: the middle of the lifecycle is well-instrumented, while the beginning and end require stronger metadata discipline or explicit service topology to avoid ambiguity. Sources: https://learn.microsoft.com/en-us/graph/api/resources/driveitem?view=graph-rest-1.0; https://support.atlassian.com/platform-experiences/docs/use-smart-links-to-view-projects-in-confluence/; https://support.pagerduty.com/main/docs/recent-changes
- **[inference]** OpenLineage demonstrates that a standard event model is possible for one segment of the lifecycle, but the broader organisational problem is ontological rather than purely technical because "document", "issue", "deployment", and "incident" are different classes of entity with different ownership and evidence quality. Sources: https://openlineage.io/docs/spec/object-model/; https://openlineage.io/docs/1.38.0/guides/facets
- **[inference]** The best architecture is therefore layered: capture native links exactly as emitted, store them in a graph with provenance and timestamps, and only then compute higher-level journey views such as "idea -> requirement -> code -> deploy -> incident -> data job." Sources: https://docs.github.com/en/rest/deployments/deployments; https://support.pagerduty.com/main/docs/recent-changes; https://openlineage.io/docs/spec/object-model/

**Risks, gaps, uncertainties:**

- **[fact]** The reviewed public docs do not provide a vendor-neutral standard for document-origin provenance analogous to OpenLineage's data-job model. Sources: https://learn.microsoft.com/en-us/graph/api/resources/driveitem?view=graph-rest-1.0; https://support.atlassian.com/platform-experiences/docs/use-smart-links-to-view-projects-in-confluence/; https://openlineage.io/docs/spec/object-model/
- **[fact]** Some listed sources had drifted or changed substantially, including the original Jira Smart Commits web link, the Azure deployment-gates web link, and the current Sleuth home page, which increases uncertainty when product evidence is time-sensitive. Sources: https://support.atlassian.com/jira-software-cloud/docs/process-issues-with-smart-commits/; https://learn.microsoft.com/en-us/azure/devops/pipelines/release/deployment-gates; https://www.sleuth.io
- **[inference]** Organisations with weak naming discipline or incomplete deployment and incident instrumentation will not get reliable end-to-end lineage even if every relevant API is technically available. Sources: https://support.atlassian.com/jira-software-cloud/docs/process-issues-with-smart-commits/; https://docs.github.com/en/rest/deployments/deployments; https://support.pagerduty.com/main/docs/recent-changes
- **[inference]** Commercial-tool marketing evidence is useful for identifying market patterns, but it is weaker than standards or product documentation for proving exact cross-system semantics. Sources: https://linearb.zendesk.com/hc/en-us/articles/45768080630043-Integrating-Jira-Cloud-into-LinearB-OAuth-2-0; https://www.sleuth.io/post/dora-metrics-explained/

**Open questions:**

- **[inference]** What is the lightest-weight cross-system schema for representing document-origin links, decision records, and issue creation events without forcing teams to adopt a new authoring tool?
- **[inference]** Which monitoring and data-platform vendors besides PagerDuty and OpenLineage expose the cleanest deploy-to-incident and issue-to-pipeline joins with public APIs?
- **[inference]** How should provenance graphs represent contradictory or superseded document context when multiple Confluence or SharePoint pages claim to explain the same work item?

### §7 Recursive Review

- **[fact]** Every finding in Section 6 is traceable to claims established in Sections 2-5, and no new substantive claim was introduced in the Findings-only material. Source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-15-tracking-work-across-systems.md
- **[fact]** Claims that rely on direct product behaviour are labelled as facts with web-link citations, while architecture recommendations and cross-system conclusions are labelled as inferences. Source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-15-tracking-work-across-systems.md
- **[fact]** Uncertainties are explicit in the source-drift notes, in the weaker status of commercial-product evidence, and in the distinction between deterministic and correlation-based joins. Source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-15-tracking-work-across-systems.md
- **[inference]** The document is ready for external review because it answers the research question directly, keeps unsupported speculation out of the Findings, and states the main blockers in operational rather than abstract terms. Source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-15-tracking-work-across-systems.md

---

## Findings

### Executive Summary

- **[inference]** End-to-end tracking of organisational work is achievable, but only by building a graph of work artefacts and typed evidence links (a provenance graph) that stitches together local identifiers, web links, and event records from multiple systems rather than by discovering a single native identifier that already follows the work everywhere. Sources: https://learn.microsoft.com/en-us/graph/api/resources/driveitem?view=graph-rest-1.0; https://learn.microsoft.com/en-us/azure/devops/boards/github/link-to-from-github; https://docs.github.com/en/rest/deployments/deployments; https://support.pagerduty.com/main/docs/recent-changes; https://openlineage.io/docs/spec/object-model/
- **[inference]** The strongest native traceability today sits in the issue-to-code-to-build or deployment path, where GitHub, Azure Boards, and Jira all provide explicit mechanisms for linking work items, branches, commits, pull requests, and builds. Sources: https://docs.github.com/en/issues/tracking-your-work-with-issues/linking-a-pull-request-to-an-issue; https://learn.microsoft.com/en-us/azure/devops/boards/github/link-to-from-github; https://support.atlassian.com/jira-software-cloud/docs/process-issues-with-smart-commits/
- **[fact]** SharePoint, Confluence, monitoring systems, and data platforms can all contribute important lifecycle evidence, but they do so through weaker document links, service correlations, or specialised standards such as OpenLineage rather than through one shared work-tracking schema. Sources: https://learn.microsoft.com/en-us/graph/api/resources/driveitem?view=graph-rest-1.0; https://support.atlassian.com/platform-experiences/docs/use-smart-links-to-view-projects-in-confluence/; https://support.pagerduty.com/main/docs/recent-changes; https://openlineage.io/docs/spec/object-model/
- **[inference]** The best minimum viable approach is to choose the issue layer as the canonical work key, ingest every deterministic native link the tools already expose, and then attach provenance plus confidence to any correlation-based or inferred joins that extend the lifecycle into documents, incidents, and data jobs. Sources: https://learn.microsoft.com/en-us/azure/devops/boards/github/link-to-from-github; https://support.atlassian.com/jira-software-cloud/docs/process-issues-with-smart-commits/; https://support.pagerduty.com/main/docs/recent-changes; https://openlineage.io/docs/spec/object-model/

### Key Findings

1. **[fact][high confidence]** Azure Boards, Jira Software, and GitHub all support explicit issue-to-code linkage, but they rely on product-specific identifiers and text conventions such as `AB#123`, Jira issue keys, and pull request closing keywords instead of one shared cross-system work identifier. Sources: https://learn.microsoft.com/en-us/azure/devops/boards/github/link-to-from-github; https://support.atlassian.com/jira-software-cloud/docs/process-issues-with-smart-commits/; https://docs.github.com/en/issues/tracking-your-work-with-issues/linking-a-pull-request-to-an-issue
2. **[fact][high confidence]** SharePoint and Confluence expose stable, addressable artefacts that can anchor provenance, but their public documentation positions them primarily as content surfaces and link renderers rather than as authoritative registries for the lifecycle of engineering work. Sources: https://learn.microsoft.com/en-us/graph/api/resources/driveitem?view=graph-rest-1.0; https://support.atlassian.com/platform-experiences/docs/use-smart-links-to-view-projects-in-confluence/
3. **[inference][high confidence]** Deployment-stage traceability becomes materially stronger when deployments are modelled as first-class records, because GitHub deployment objects tie an environment and status history to a specific ref while Azure Boards can return build evidence to the originating work item. Sources: https://docs.github.com/en/rest/deployments/deployments; https://learn.microsoft.com/en-us/azure/devops/boards/github/link-to-from-github
4. **[inference][medium confidence]** Monitoring-stage linkage is usually correlation-based rather than strictly deterministic, because PagerDuty connects incidents to recent changes by time, related service, and machine-learning similarity instead of requiring every incident to carry the original issue or deployment identifier. Sources: https://support.pagerduty.com/main/docs/recent-changes
5. **[fact][high confidence]** OpenLineage provides a mature provenance model for the data-platform segment through Jobs, Runs, Datasets, and extensible facets, but its native entity set stops short of documents, pull requests, deployments, and incidents. Sources: https://openlineage.io/docs/spec/object-model/; https://openlineage.io/docs/1.38.0/guides/facets
6. **[fact][medium confidence]** Commercial products such as LinearB and the older Sleuth positioning create value mainly by standardising existing keys and correlating signals across systems, which means their effectiveness still depends on disciplined issue references, deployment records, and service-mapping data upstream. Sources: https://linearb.zendesk.com/hc/en-us/articles/45768080630043-Integrating-Jira-Cloud-into-LinearB-OAuth-2-0; https://www.sleuth.io/post/dora-metrics-explained/; https://support.pagerduty.com/main/docs/recent-changes
7. **[inference][high confidence]** The most defensible organisation-wide architecture is a provenance graph with typed nodes and edges, because each platform owns only one segment of the lifecycle and no reviewed standard already spans document intent, tracked work, code change, release, incident, and data lineage together. Sources: https://learn.microsoft.com/en-us/graph/api/resources/driveitem?view=graph-rest-1.0; https://docs.github.com/en/rest/deployments/deployments; https://openlineage.io/docs/spec/object-model/
8. **[inference][high confidence]** A minimum viable implementation should start at the issue layer as the canonical work key, capture deterministic joins first, and treat semantic matching or correlation as a secondary repair strategy for missing document-origin, incident, or downstream data-job links. Sources: https://learn.microsoft.com/en-us/azure/devops/boards/github/link-to-from-github; https://support.atlassian.com/jira-software-cloud/docs/process-issues-with-smart-commits/; https://support.pagerduty.com/main/docs/recent-changes; https://openlineage.io/docs/spec/object-model/

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [fact] Issue-to-code links are strong but product-specific. | https://learn.microsoft.com/en-us/azure/devops/boards/github/link-to-from-github; https://support.atlassian.com/jira-software-cloud/docs/process-issues-with-smart-commits/; https://docs.github.com/en/issues/tracking-your-work-with-issues/linking-a-pull-request-to-an-issue | high | Three independent primary docs converge. |
| [fact] Documents are stable provenance nodes but weak lifecycle authorities. | https://learn.microsoft.com/en-us/graph/api/resources/driveitem?view=graph-rest-1.0; https://support.atlassian.com/platform-experiences/docs/use-smart-links-to-view-projects-in-confluence/ | high | Good support for addressability, weaker support for lifecycle ownership. |
| [inference] Deployment records strengthen traceability. | https://docs.github.com/en/rest/deployments/deployments; https://learn.microsoft.com/en-us/azure/devops/boards/github/link-to-from-github | high | Deployment objects and build links are explicit machine-readable joins. |
| [inference] Incident linkage is correlation-heavy. | https://support.pagerduty.com/main/docs/recent-changes | medium | Strong primary source, but vendor-specific implementation. |
| [fact] OpenLineage is strong for data jobs but narrow for broader work provenance. | https://openlineage.io/docs/spec/object-model/; https://openlineage.io/docs/1.38.0/guides/facets | high | Clear entity-boundary evidence. |
| [inference] Commercial tools depend on upstream identifier discipline. | https://linearb.zendesk.com/hc/en-us/articles/45768080630043-Integrating-Jira-Cloud-into-LinearB-OAuth-2-0; https://www.sleuth.io/post/dora-metrics-explained/; https://support.pagerduty.com/main/docs/recent-changes | medium | Good directional evidence, but partly product-positioning material. |
| [inference] A provenance graph is the best synthesis layer. | https://learn.microsoft.com/en-us/graph/api/resources/driveitem?view=graph-rest-1.0; https://docs.github.com/en/rest/deployments/deployments; https://openlineage.io/docs/spec/object-model/ | high | Inference directly supported by heterogeneous node and edge types. |
| [inference] The minimum viable approach should start with canonical issue keys and deterministic joins. | https://learn.microsoft.com/en-us/azure/devops/boards/github/link-to-from-github; https://support.atlassian.com/jira-software-cloud/docs/process-issues-with-smart-commits/; https://support.pagerduty.com/main/docs/recent-changes; https://openlineage.io/docs/spec/object-model/ | high | Best-supported practical implementation path. |

### Assumptions

- **[assumption]** The issue or work-item layer is the best canonical key for most organisations. **Justification:** the strongest reviewed native joins cluster around Azure Boards and Jira issue identifiers. Sources: https://learn.microsoft.com/en-us/azure/devops/boards/github/link-to-from-github; https://support.atlassian.com/jira-software-cloud/docs/process-issues-with-smart-commits/
- **[assumption]** Documents should be modelled as contextual provenance nodes even when they are not authoritative identifiers. **Justification:** SharePoint and Confluence both expose stable, linkable artefacts that can preserve origin and decision context. Sources: https://learn.microsoft.com/en-us/graph/api/resources/driveitem?view=graph-rest-1.0; https://support.atlassian.com/platform-experiences/docs/use-smart-links-to-view-projects-in-confluence/
- **[assumption]** Semantic inference should be reserved for explicit-link gaps rather than used as the default join strategy. **Justification:** deterministic identifiers and event objects exist across much of the lifecycle, while confidence drops noticeably at the correlation layer. Sources: https://docs.github.com/en/rest/deployments/deployments; https://support.pagerduty.com/main/docs/recent-changes; https://openlineage.io/docs/spec/object-model/

### Analysis

- **[fact]** The evidence supports a layered traceability model: deterministic reference links at the issue and code layer, first-class event objects at the deployment and data layer, and weaker explicit-link or correlation logic at the document and incident layer. Sources: https://learn.microsoft.com/en-us/azure/devops/boards/github/link-to-from-github; https://docs.github.com/en/rest/deployments/deployments; https://support.pagerduty.com/main/docs/recent-changes; https://openlineage.io/docs/spec/object-model/
- **[inference]** This layered model explains why organisations can usually answer "which ticket drove this pull request?" more confidently than "which document started this work?" or "which deployment caused this incident?" because the latter questions rely on looser metadata or probabilistic correlation. Sources: https://learn.microsoft.com/en-us/graph/api/resources/driveitem?view=graph-rest-1.0; https://support.atlassian.com/platform-experiences/docs/use-smart-links-to-view-projects-in-confluence/; https://support.pagerduty.com/main/docs/recent-changes
- **[inference]** OpenLineage's success inside data platforms suggests that broader work provenance should also be event-centric and extensible, but the broader problem needs a super-graph because the lifecycle crosses entity types that were never designed to share one canonical schema. Sources: https://openlineage.io/docs/spec/object-model/; https://openlineage.io/docs/1.38.0/guides/facets
- **[inference]** The minimum viable design choice is therefore organisational rather than purely technical: choose a canonical issue key, enforce identifier hygiene, emit deployments and change events, and preserve edge provenance so that downstream graphs expose certainty and ambiguity separately. Sources: https://learn.microsoft.com/en-us/azure/devops/boards/github/link-to-from-github; https://docs.github.com/en/rest/deployments/deployments; https://support.pagerduty.com/main/docs/recent-changes

### Risks, Gaps, and Uncertainties

- **[fact]** The reviewed public sources do not define one vendor-neutral standard that covers documents, tracked work, code changes, deployments, incidents, and data lineage together. Sources: https://openlineage.io/docs/spec/object-model/; https://learn.microsoft.com/en-us/graph/api/resources/driveitem?view=graph-rest-1.0; https://support.pagerduty.com/main/docs/recent-changes
- **[fact]** Several originally listed sources had drifted or moved, which means product-level evidence in this domain can become stale quickly and must be revalidated before implementation decisions. Sources: https://support.atlassian.com/jira-software-cloud/docs/process-issues-with-smart-commits/; https://learn.microsoft.com/en-us/azure/devops/pipelines/release/deployment-gates; https://www.sleuth.io
- **[inference]** The real operational risk is false confidence: a graph that hides whether an edge is declared, correlated, or inferred will look more precise than the evidence actually warrants. Sources: https://support.pagerduty.com/main/docs/recent-changes; https://openlineage.io/docs/1.38.0/guides/facets
- **[inference]** Organisations with inconsistent branch naming, missing issue keys, or absent deployment or change-event instrumentation will only recover a partial lifecycle regardless of how good the graph technology is. Sources: https://support.atlassian.com/jira-software-cloud/docs/process-issues-with-smart-commits/; https://docs.github.com/en/rest/deployments/deployments; https://support.pagerduty.com/main/docs/recent-changes

### Open Questions

- **[inference]** What is the smallest metadata contract that would let SharePoint and Confluence pages declare themselves as the origin or justification of a specific work item without forcing a new authoring workflow?
- **[inference]** Which public monitoring and observability APIs provide the cleanest deterministic deployment-to-incident joins beyond PagerDuty's correlation model?
- **[inference]** What graph query patterns are most useful for users once the lifecycle graph exists: origin tracing, blast-radius analysis, compliance evidence, or onboarding explanations?

---

## Output

- Type: knowledge
- Description: Evidence-backed synthesis of how work can be traced across documents, issue trackers, Git, deployments, incidents, and data pipelines, including a minimum viable provenance-graph architecture and its main blockers.
- Links:
  - https://learn.microsoft.com/en-us/azure/devops/boards/github/link-to-from-github
  - https://docs.github.com/en/rest/deployments/deployments
  - https://openlineage.io/docs/spec/object-model/
