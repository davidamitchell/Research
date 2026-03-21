---
title: "Dependency Mapping Across .NET Codebases, Terraform, Dynatrace, Confluence, Log Aggregation, and CSDM"
added: 2026-03-21
status: backlog  # backlog | in-progress | reviewing | completed
priority: high  # low | medium | high
blocks: []
tags: [dependency-mapping, dotnet, terraform, dynatrace, confluence, log-aggregation, csdm, architecture, discovery, agents, observability, infrastructure-as-code]
started: ~
completed: ~
output: [knowledge]
---

# Dependency Mapping Across .NET Codebases, Terraform, Dynatrace, Confluence, Log Aggregation, and CSDM

## Research Question

What practical tools and methodologies are being used to map dependencies across .NET codebases, Terraform configurations, Dynatrace Application Performance Management (APM) monitoring, and solution documentation in Confluence — and how are organisations practically implementing these approaches to produce a detailed understanding of existing-state architecture and dependency trees? How do signals from log aggregation and Configuration and Service Data Model (CSDM) systems extend and validate these maps? What role can locally-running agents play in automating discovery and mapping across all these surfaces, given that every source will be incomplete, partially incorrect, or contain blind spots?

Supporting questions:
- What static analysis and tooling approaches exist for extracting dependency graphs from .NET codebases (project references, NuGet packages, inter-service calls, database dependencies)?
- How can Terraform configurations be parsed to produce resource and module dependency graphs, and what tools and Infrastructure as Code (IaC) analysis tools exist for this?
- How does Dynatrace APM's automated dependency discovery (SmartScape, service flow, Smartscape topology) complement or conflict with statically-derived maps, and how is the data exported or queried?
- What is the role of Confluence documentation as a source of dependency information — and what are its failure modes (staleness, incompleteness, inconsistency)?
- How do log aggregation pipelines (e.g., Elastic Stack, Splunk, Datadog) surface runtime dependency signals that neither static analysis nor APM topology captures?
- What is CSDM in the ServiceNow context, and how does it model application, service, and infrastructure dependencies — and where does it typically break down in practice?
- How can locally-running agents (LLM-based code analysis, graph extraction, cross-source reconciliation) automate the discovery and reconciliation of dependencies across all these surfaces?
- What strategies exist for handling the reality that all of these sources are partially wrong, incomplete, or out of date — and how do organisations build confidence in their composite dependency maps despite this?
- What does a pragmatic "good enough" dependency map look like when starting from heterogeneous, imperfect sources?

## Scope

**In scope:**
- Static analysis tooling for .NET dependency extraction: NDepend, dotnet-depends, Roslyn-based analysers, Visual Studio Architecture tools, custom scripting over .csproj / solution files
- IaC dependency mapping tools for Terraform: `terraform graph`, Infracost, Checkov, Blast Radius, Rover, Spacelift dependency views
- Dynatrace APM dependency discovery: SmartScape topology API, service flow API, Davis AI anomaly context, export and query patterns
- Confluence as a dependency knowledge source: API-driven extraction, Confluence graph traversal, staleness detection
- Log aggregation as a dependency signal source: service-to-service call patterns derived from structured log data in Elastic Stack (ELK), Splunk, or Datadog
- CSDM (ServiceNow Configuration and Service Data Model): structure, typical coverage, known gaps, and how it is used in practice as a dependency registry
- Agent-assisted discovery: locally-running LLM agents used for code graph extraction, cross-source reconciliation, gap detection, and natural language querying of dependency graphs
- Cross-source reconciliation strategies: how to merge and validate maps from heterogeneous sources when each source is partially wrong
- Practical organisational implementation patterns: team structures, tooling stacks, governance approaches, incremental improvement strategies
- Prior research context from this repository (where relevant): see in-progress items on architecture and agent memory systems

**Out of scope:**
- Microservice mesh tools (Istio, Linkerd) as primary dependency mapping mechanisms — may be noted but not a focus
- Security-specific dependency scanning (SCA, CVE scanning) beyond their use as a dependency signal
- Non-.NET languages and runtimes unless the approach generalises
- Vendor feature comparisons below the level of architectural decisions
- Implementation of a specific dependency mapping tool or pipeline for a specific organisation

**Constraints:** Publicly accessible sources — vendor documentation, technical blog posts, conference talks (QCon, GOTO, InfoQ), GitHub repositories, and practitioner write-ups. Given the applied, operational nature of this question, practitioner accounts (engineering blog posts, case studies) carry as much weight as academic literature. Web search at retrieval time for current tooling state. All sources to be documented at URL or DOI level.

## Context

Large organisations accumulate their system architecture across many heterogeneous surfaces: source code repositories, infrastructure configuration, monitoring data, a Configuration Management Database (CMDB) or CSDM, log streams, and tribal knowledge encoded (loosely) in Confluence pages. No single surface gives a complete picture of dependencies.

The practical problem is: given access to all of these surfaces simultaneously, how do you build a working model of "what depends on what" — a dependency tree that is detailed enough to reason about blast radius, change impact, decommissioning safety, and migration sequencing — when every source is incomplete, partially wrong, and with known blind spots?

The key constraints that make this non-trivial:
1. **Imperfect sources** — Terraform configs drift from actual infra; Dynatrace topology only sees what is instrumented; Confluence pages go stale; CSDM entries are manually maintained and lag reality; log-derived call graphs are incomplete for low-traffic paths.
2. **Heterogeneous formats** — .NET project graphs, Terraform plan graphs, Dynatrace topology JSON, Confluence page graphs, CMDB/CSDM tables, and log-derived call matrices are all different graph representations with different semantics.
3. **Local agent capability** — the availability of locally-running LLM agents that can read code, parse configuration, call APIs, and reason across sources opens up new approaches to automated discovery and reconciliation that were not practical before 2023.

This research aims to catalogue what is being done in practice, identify the best current tooling for each surface, and synthesise a pragmatic multi-surface dependency mapping approach that accounts for incompleteness from the start.

## Approach

1. **Surface-by-surface tool audit** — for each of the five primary surfaces (.NET, Terraform, Dynatrace, Confluence, log aggregation) and the CSDM registry, identify: the leading open-source and commercial tools, the format of the dependency data they produce, their known limitations, and how their output can be exported for downstream processing.
2. **CSDM deep-dive** — clarify what CSDM is in the ServiceNow context, how it structures application, service, and infrastructure relationships, what a typical enterprise CSDM looks like in practice (coverage, accuracy, staleness), and how it is used (or not used) as a dependency source.
3. **Log aggregation as a dependency signal** — investigate how structured log data can be mined to infer service-to-service dependencies, what patterns exist for this (e.g., request tracing, correlation ID following, service name extraction from log fields), and how this compares to APM-derived topology.
4. **Agent-assisted discovery patterns** — investigate what is being done with locally-running LLM agents (code analysis agents, graph extraction agents, reconciliation agents) for dependency discovery. What agent architectures are being used? What tasks are agents well-suited for in this context (code parsing, API querying, cross-source reconciliation, gap identification, natural language querying of dependency graphs)?
5. **Cross-source reconciliation strategies** — how do organisations (and tools) merge dependency data from heterogeneous sources? What conflict resolution strategies exist when sources disagree? How is confidence or staleness tracked per-edge in a composite dependency graph?
6. **Pragmatic "good enough" map strategies** — what organisational and technical strategies do practitioners use to build usable dependency maps from imperfect sources? How do they communicate confidence levels and known gaps? What iterative improvement patterns exist?
7. **Synthesis** — produce Executive Summary, Key Findings, Evidence Map, and a practical tooling/approach guide.

## Sources

- [ ] NDepend — .NET dependency analysis tool — https://www.ndepend.com/docs/
- [ ] `dotnet-depends` — open-source NuGet dependency CLI — https://github.com/josteink/dotnet-depends
- [ ] `terraform graph` command — HashiCorp documentation — https://developer.hashicorp.com/terraform/cli/commands/graph
- [ ] Blast Radius — Terraform visualisation tool — https://github.com/28mm/blast-radius
- [ ] Rover — Terraform visualisation tool — https://github.com/im2nguyen/rover
- [ ] Dynatrace SmartScape topology API documentation — https://docs.dynatrace.com/docs/dynatrace-api/environment-api/topology-and-smartscape
- [ ] Dynatrace service flow API — https://docs.dynatrace.com/docs/dynatrace-api/environment-api/service-flow
- [ ] ServiceNow CSDM documentation — https://docs.servicenow.com/bundle/washingtondc-it-asset-management/page/product/csdm/concept/csdm-overview.html
- [ ] ServiceNow CSDM implementation guide and practitioner accounts — search: "CSDM implementation lessons learned" site:community.servicenow.com OR site:devops.com
- [ ] Confluence REST API — Atlassian documentation — https://developer.atlassian.com/cloud/confluence/rest/v2/intro/
- [ ] ELK Stack (Elasticsearch, Logstash, Kibana) for log-derived dependency mapping — https://www.elastic.co/elastic-stack
- [ ] Splunk service dependency discovery from log data — https://docs.splunk.com/Documentation/Splunk/latest/Viz/ServiceMap
- [ ] Datadog Service Map — https://docs.datadoghq.com/tracing/services/services_map/
- [ ] QCon / InfoQ practitioner talks on dependency mapping and architecture discovery (2022–2026) — search: "dependency mapping architecture" site:infoq.com
- [ ] Thoughtworks Technology Radar entries on architecture visualisation and dependency tools (2022–2026) — https://www.thoughtworks.com/radar
- [ ] "Living Architecture Documentation" — practitioner write-ups on architecture-as-code and dependency graph maintenance
- [ ] LLM agent-assisted code analysis patterns — search: "LLM agent codebase dependency analysis" OR "AI-assisted architecture discovery"
- [ ] Structurizr / C4 model as a dependency registry — Simon Brown — https://structurizr.com/
- [ ] Backstage software catalogue as a dependency registry — https://backstage.io/docs/features/software-catalog/
- [ ] CMDB accuracy and staleness research — practitioner accounts and vendor documentation

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
