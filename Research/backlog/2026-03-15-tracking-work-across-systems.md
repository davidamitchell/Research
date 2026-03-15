---
title: "Tracking How Work Travels Across Organisational Systems"
added: 2026-03-15
status: backlog  # backlog | in-progress | reviewing | completed
priority: medium  # low | medium | high
blocks: []  # slugs (filename without .md) of backlog items that cannot start until this one is complete
tags: [knowledge-management, work-tracking, sharepoint, confluence, ado, jira, git, monitoring, data-platform, provenance]
started: ~
completed: ~
output: [knowledge]
---

# Tracking How Work Travels Across Organisational Systems

## Research Question

Can we track how a unit of 'Work' — an idea or concept — travels across organisational systems (SharePoint, Confluence, Azure DevOps (ADO)/Jira, Git, monitoring systems, and data platforms), and what mechanisms or patterns exist to trace its full lifecycle from inception to delivery and beyond?

## Scope

**In scope:**
- Definition of 'Work' as a traceable unit: idea, requirement, task, change, incident, or feature
- Systems where Work manifests: SharePoint (documents/wikis), Confluence (wikis/pages), Azure DevOps (ADO)/Jira (backlog/issues), Git (code/commits/PRs), monitoring systems (alerts/incidents), data platforms (pipelines/jobs)
- Existing cross-system linking mechanisms: issue keys in commit messages, PR references in deployment records, alert-to-incident linkage, pipeline job references
- Industry patterns and standards for work provenance (e.g. Open Lineage, Value Stream Mapping, software supply chain)
- Feasibility of building an organisation-wide Work provenance graph

**Out of scope:**
- Deep implementation guides for any single tool's internal data model
- Security, access control, or governance policies for each system
- Change management or process redesign recommendations

**Constraints:** Publicly accessible documentation, open-source tooling, and general industry literature; no access to proprietary organisational data.

## Context

Work in modern software organisations does not live in a single system. An idea starts as a conversation or a document in SharePoint or Confluence, becomes a ticket in ADO or Jira, gets implemented as commits and pull requests in Git, is shipped via a pipeline, generates alerts in monitoring, and may ultimately shape data in a data platform. Each system maintains its own identity for the same unit of work, often with loose or hand-crafted links between them. This fragmentation makes it difficult to answer questions like: "Where did this feature come from?", "Which deployment caused this alert?", or "What business goal does this pipeline serve?". Understanding whether and how these links can be made systematic — and what tooling already exists — informs decisions about observability, onboarding, and organisational knowledge management.

## Approach

1. Define 'Work' as a multi-stage artefact and map its typical lifecycle stages across the six system categories (document → ticket → commit/PR → deployment → alert/incident → data job).
2. Survey the linking mechanisms that each system exposes natively (e.g. Jira smart commits, ADO AB#nnn syntax in Git, GitHub Deployments API, alert annotations).
3. Identify existing open-source or commercial tooling that attempts cross-system work tracing (e.g. LinearB, Sleuth, Allma, Open Lineage, value stream management platforms).
4. Examine the Open Lineage specification and similar provenance standards to assess their applicability beyond data pipelines to the broader Work lifecycle.
5. Assess feasibility: what data is accessible via APIs, what is locked in unstructured text, and what inference (e.g. semantic matching) would be required to fill gaps?
6. Synthesise: what is the minimum viable approach for tracing Work end-to-end in a typical organisation, and what are the blockers?

## Sources

- [ ] https://openlineage.io — Open Lineage specification for data pipeline provenance
- [ ] https://docs.github.com/en/issues/tracking-your-work-with-issues/linking-a-pull-request-to-an-issue — GitHub cross-linking mechanism
- [ ] https://learn.microsoft.com/en-us/azure/devops/boards/github/link-to-from-github — ADO ↔ GitHub linking (AB# syntax)
- [ ] https://support.atlassian.com/jira-software-cloud/docs/use-smart-commits/ — Jira smart commits
- [ ] https://linearb.io — LinearB: engineering metrics and work tracing across Git and project management
- [ ] https://www.sleuth.io — Sleuth: DevOps Research and Assessment (DORA) metrics and deployment/incident correlation
- [ ] https://en.wikipedia.org/wiki/Value_stream_mapping — Value Stream Mapping (VSM) background
- [ ] https://learn.microsoft.com/en-us/azure/devops/pipelines/release/deployment-gates — ADO deployment gates and traceability

---

## Research Skill Output

*(Full output from running the research skill — retained verbatim in the completed item. §§0–5 are the investigation; §6 seeds the Findings section below.)*

### §0 Initialise

Restate the research question. Confirm scope, constraints, and output format.

-

### §1 Question Decomposition

Approach sub-questions broken into atomic questions — each answerable with a single evidence-based claim.

-

### §2 Investigation

Evidence gathered per atomic question. Label each claim: **[fact]**, **[inference]**, or **[assumption]** with source.

-

### §3 Reasoning

Facts, inferences, and assumptions explicitly separated. No unsupported generalisations or narrative leaps.

-

### §4 Consistency Check

Internal contradictions identified and resolved (or explicitly flagged where unresolvable).

-

### §5 Depth and Breadth Expansion

Findings re-examined through relevant lenses (technical, regulatory, economic, historical, behavioural).

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

Final pass: every section justified, all threads synthesised, every claim sourced or labelled, all uncertainties explicit.

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
