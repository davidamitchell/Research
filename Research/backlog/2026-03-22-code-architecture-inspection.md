---
title: "Code Architecture Inspection Across Repositories"
added: 2026-03-22
status: backlog  # backlog | in-progress | reviewing | completed
priority: high  # low | medium | high
blocks: []  # slugs (filename without .md) of backlog items that cannot start until this one is complete
tags: [architecture, static-analysis, multi-repo, coupling, standards, github-copilot, tooling]
started: ~
completed: ~
output: [knowledge, backlog-item]
---

# Code Architecture Inspection Across Repositories

## Research Question

What practical implementation approaches exist for automatically inspecting and understanding how a set of repositories is architected, how they relate to and couple with each other, and whether they are following standards or drifting out of alignment — and which of these approaches can be operationalised using GitHub Copilot skills, agents, or adjacent tooling such as reposwarm?

## Scope

**In scope:**
- Techniques for generating architecture blueprints from source code (dependency graphs, service maps, call graphs, API surface analysis)
- Multi-repo relationship and coupling analysis (shared libraries, cross-repo imports, API contracts, event schemas)
- Standards alignment checking (naming conventions, dependency policies, security patterns, architectural decision records (ADRs))
- GitHub Copilot agent skills relevant to architecture inspection, particularly the architecture-blueprint-generator skill from awesome-copilot
- Tooling for multi-repo operations: reposwarm and similar orchestration frameworks
- Integration of architecture inspection into continuous integration / continuous delivery (CI/CD) pipelines or GitHub Actions workflows
- Relationship to previous research on coding AI agent skills, MCP, and multi-agent frameworks

**Out of scope:**
- Deep runtime observability (distributed tracing, Application Performance Monitoring (APM)) — focus is static/structural analysis
- Architecture design methodologies (Domain-Driven Design (DDD), event storming) — focus is inspection of existing codebases, not greenfield design
- Commercial Architecture Management platforms that require proprietary connectors or non-public APIs

**Constraints:** Publicly accessible documentation, open-source tooling, and GitHub ecosystem; no proprietary organisational code.

## Context

Understanding how a collection of repositories fits together — which services call which, which teams own which boundaries, which repos share dependencies, and which are drifting from agreed standards — is a persistent engineering pain point. Manual review does not scale beyond a handful of repos. Automated inspection tools exist but are fragmented: language-specific linters, graph-based dependency tools, and platform-specific scanners each give a partial view. The emergence of GitHub Copilot skills (e.g. architecture-blueprint-generator in awesome-copilot) and multi-repo agent orchestration (e.g. reposwarm) suggests a new class of approach: LLM-assisted architectural inspection that can synthesise across repos at a level of abstraction above raw code. This research maps the current landscape, identifies the most promising practical approaches, and defines what an implementation plan would look like for the owner's context.

## Approach

1. Analyse the architecture-blueprint-generator skill (`https://github.com/github/awesome-copilot/blob/main/skills/architecture-blueprint-generator/SKILL.md`) to understand its prompting strategy, inputs, outputs, and limitations.
2. Analyse reposwarm (`https://github.com/reposwarm/reposwarm`) to understand its model for orchestrating operations across multiple repositories and where architecture inspection fits.
3. Survey the landscape of static analysis and architecture inspection tools: dependency-cruiser, Renovate for dependency graphs, Sourcegraph, GitHub's code search API, OpenRewrite, and similar.
4. Identify coupling and relationship patterns that automated tools can detect (imports, shared container registries, shared infrastructure-as-code (IaC), API client generation from OpenAPI specs, event schema registries).
5. Assess standards alignment checking: how ADRs, Architecture Fitness Functions (AFF), and policy-as-code (e.g. Open Policy Agent (OPA)) can be combined with repository scanning.
6. Synthesise a practical implementation plan: what can be done with GitHub Actions + Copilot skills today, what requires additional tooling, and what are the gaps.

## Sources

- [ ] https://github.com/github/awesome-copilot/blob/main/skills/architecture-blueprint-generator/SKILL.md — architecture-blueprint-generator Copilot skill
- [ ] https://github.com/reposwarm/reposwarm — multi-repo agent orchestration framework
- [ ] https://github.com/sverweij/dependency-cruiser — dependency-cruiser: validate and visualise JavaScript/TypeScript dependencies
- [ ] https://sourcegraph.com/docs — Sourcegraph code intelligence and cross-repo search
- [ ] https://docs.github.com/en/rest/dependency-graph — GitHub Dependency Graph REST API
- [ ] https://docs.renovatebot.com — Renovate dependency management and graph output
- [ ] https://www.openrewrite.org — OpenRewrite: automated source code refactoring and standards enforcement
- [ ] https://www.openpolicyagent.org — Open Policy Agent (OPA): policy-as-code for standards compliance
- [ ] https://evolutionarytesting.io/architecture-fitness-functions — Architecture Fitness Functions (AFF) concept from Building Evolutionary Architectures
- [ ] https://adr.github.io — Architecture Decision Records (ADRs) specification and tooling

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

- Type: knowledge, backlog-item
- Description:
- Links:
