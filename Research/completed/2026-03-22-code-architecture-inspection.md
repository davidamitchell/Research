---
review_count: 2
title: "Code Architecture Inspection Across Repositories"
added: 2026-03-22T10:56:16+00:00
status: completed
priority: high  # low | medium | high
blocks: []  # slugs (filename without .md) of backlog items that cannot start until this one is complete
tags: [architecture, static-analysis, multi-repo, coupling, standards, github-copilot, tooling]
started: 2026-03-22T10:56:16+00:00
completed: 2026-03-22T10:56:16+00:00
output: [knowledge, backlog-item]
cites: []          # slugs of items this item directly depends on or quotes
related: []        # slugs of thematically connected items
superseded_by: ~   # slug of a later item that overrides this one (null if not superseded)
supersedes: ~      # slug of an older item this one replaces (null if not applicable)
item_type: primary # primary | synthesis
confidence: medium # high | medium | low
versions: []       # entries: {version: "1.0", sha: "<commit-hash>", changed: YYYY-MM-DD, progress: "<path>", summary: "<one-line>"}
---

# Code Architecture Inspection Across Repositories

## Research Question

What practical implementation approaches exist for automatically inspecting and understanding how a set of repositories is architected, how they relate to and couple with each other, and whether they are following standards or drifting out of alignment — and which of these approaches can be operationalised using GitHub Copilot skills, agents, or adjacent tooling such as RepoSwarm?

## Scope

**In scope:**
- Techniques for generating architecture blueprints from source code (dependency graphs, service maps, call graphs, Application Programming Interface (API) surface analysis)
- Multi-repo relationship and coupling analysis (shared libraries, cross-repo imports, API contracts, event schemas)
- Standards alignment checking (naming conventions, dependency policies, security patterns, architectural decision records (ADRs))
- GitHub Copilot agent skills relevant to architecture inspection, particularly the architecture-blueprint-generator skill from awesome-copilot
- Tooling for multi-repo operations: RepoSwarm and similar orchestration frameworks
- Integration of architecture inspection into continuous integration / continuous delivery (CI/CD) pipelines or GitHub Actions workflows
- Relationship to previous research on coding AI agent skills, Model Context Protocol (MCP), and multi-agent frameworks

**Out of scope:**
- Deep runtime observability (distributed tracing, Application Performance Monitoring (APM)) — focus is static/structural analysis
- Architecture design methodologies (Domain-Driven Design (DDD), event storming) — focus is inspection of existing codebases, not greenfield design
- Commercial architecture-management platforms that require proprietary connectors or non-public APIs

**Constraints:** Publicly accessible documentation, open-source tooling, and GitHub ecosystem; no proprietary organisational code.

## Context

Understanding how a collection of repositories fits together — which services call which, which teams own which boundaries, which repos share dependencies, and which are drifting from agreed standards — is a persistent engineering pain point. Manual review does not scale beyond a handful of repos. Automated inspection tools exist but are fragmented: language-specific linters, graph-based dependency tools, and platform-specific scanners each give a partial view. The emergence of Large Language Model (LLM)-assisted architectural inspection, GitHub Copilot skills such as architecture-blueprint-generator, and multi-repo orchestration systems such as RepoSwarm suggests a practical new approach: collect deterministic architecture evidence first, then use agent tooling to synthesise it into reviewable blueprints and drift reports. This research maps that landscape, identifies the strongest implementation pattern, and defines what an implementation plan would look like for the owner's GitHub-first context.

## Approach

1. Analyse the architecture-blueprint-generator skill (`https://github.com/github/awesome-copilot/blob/main/skills/architecture-blueprint-generator/SKILL.md`) to understand its prompting strategy, inputs, outputs, and limitations.
2. Analyse RepoSwarm (`https://github.com/reposwarm/reposwarm`) to understand its model for orchestrating operations across multiple repositories and where architecture inspection fits.
3. Survey the landscape of static analysis and architecture inspection tools: dependency-cruiser, Renovate, Sourcegraph, GitHub dependency graph APIs, OpenRewrite, and adjacent tooling.
4. Identify coupling and relationship patterns that automated tools can detect (imports, shared package manifests, generated clients, Infrastructure as Code (IaC), shared standards files, and ADRs).
5. Assess standards alignment checking: how ADRs, architecture fitness functions, and policy-as-code tools such as Open Policy Agent (OPA) can be combined with repository scanning.
6. Synthesise a practical implementation plan: what can be done with GitHub Actions plus Copilot skills today, what requires additional tooling, and what the remaining gaps are.

## Sources

- [x] architecture-blueprint-generator skill — https://raw.githubusercontent.com/github/awesome-copilot/main/skills/architecture-blueprint-generator/SKILL.md
- [x] awesome-copilot repository overview — https://raw.githubusercontent.com/github/awesome-copilot/main/README.md
- [x] RepoSwarm repository overview — https://raw.githubusercontent.com/reposwarm/reposwarm/main/README.md
- [x] dependency-cruiser repository overview — https://raw.githubusercontent.com/sverweij/dependency-cruiser/main/README.md
- [x] Sourcegraph docs index — https://sourcegraph.com/docs
- [x] Sourcegraph Code Insights docs — https://sourcegraph.com/docs/code-insights
- [x] Sourcegraph Batch Changes docs — https://sourcegraph.com/docs/batch_changes
- [x] GitHub dependency graph Representational State Transfer (REST) API docs — https://docs.github.com/api/article/body?pathname=/en/rest/dependency-graph
- [x] GitHub dependency review REST API docs — https://docs.github.com/api/article/body?pathname=/en/rest/dependency-graph/dependency-review
- [x] GitHub Software Bill of Materials (SBOM) REST API docs — https://docs.github.com/api/article/body?pathname=/en/rest/dependency-graph/sboms
- [x] Renovate docs — https://docs.renovatebot.com
- [x] OpenRewrite docs — https://docs.openrewrite.org
- [x] Open Policy Agent docs — https://www.openpolicyagent.org/docs/latest/
- [x] ADR guidance site — https://adr.github.io
- [x] Neal Ford et al. — Building Evolutionary Architectures — https://nealford.com/books/buildingevolutionaryarchitectures.html
- [x] Building Evolutionary Architectures site — https://evolutionaryarchitecture.com
- [x] Agent Skills standard site — https://agentskills.io
- [x] Prior completed research: dependency mapping — https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-21-dependency-mapping-dotnet-terraform-dynatrace.md
- [x] Prior completed research: coding AI agent skills survey — https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-22-coding-ai-agent-skills-survey.md
- [x] Prior completed research: agent evaluation cross-repo analysis — https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-10-agent-evaluation-cross-repo-analysis.md
- [x] Prior completed research: applied context engineering workflows — https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-22-applied-context-engineering-agent-workflows.md

---

## Research Skill Output

*(Full output from running the research skill — retained verbatim in the completed item. §§0–5 are the investigation; §6 seeds the Findings section below.)*

### §0 Initialise

- [fact] **Research question restated:** Which practical, publicly documented approaches can inspect architecture across multiple repositories, detect coupling and standards drift, and then turn that evidence into usable architectural blueprints or governance signals? Source: https://github.com/davidamitchell/Research/blob/main/Research/backlog/2026-03-22-code-architecture-inspection.md
- [fact] **Scope confirmed:** This investigation is limited to public documentation, public repositories, and prior completed research in this repository. Proprietary enterprise scanners and non-public source-code estates are excluded by design. Source: https://github.com/davidamitchell/Research/blob/main/Research/backlog/2026-03-22-code-architecture-inspection.md
- [fact] **Constraint mode:** The owner works through the GitHub website and iOS app, so the strongest answer must favor GitHub Actions, repository files, and reviewable artifacts over workstation-dependent tooling. Sources: https://github.com/davidamitchell/Research/blob/main/.github/copilot-instructions.md ; https://github.com/davidamitchell/Research/blob/main/Research/backlog/2026-03-22-code-architecture-inspection.md
- [fact] **Output format:** Full §§0–§7 completion, followed by Findings with Executive Summary, Key Findings, Evidence Map, Assumptions, Analysis, Risks, Open Questions, and Output. Source: https://github.com/davidamitchell/Research/blob/main/research-prompt.md
- [fact] **Prior work check completed:** The directly relevant prior completed items are the dependency-mapping synthesis, the coding AI agent skills survey, the agent evaluation cross-repo analysis, and the applied context engineering workflows item. Together they establish three constraints for this item: architecture truth is layered, portable skill formats matter, and agent outputs need provenance plus observable evaluation. Sources: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-21-dependency-mapping-dotnet-terraform-dynatrace.md ; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-22-coding-ai-agent-skills-survey.md ; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-10-agent-evaluation-cross-repo-analysis.md ; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-22-applied-context-engineering-agent-workflows.md
- [fact] **Fallback process note:** The repository-local `.github/skills/research/SKILL.md` file was not present in this checkout, so this item follows the repository's research-loop instructions and the research-prompt fallback process already documented for that case. Sources: https://github.com/davidamitchell/Research/blob/main/research-prompt.md ; https://github.com/davidamitchell/Research/blob/main/.github/copilot-instructions.md

### §1 Question Decomposition

- [fact] **A. Copilot-skill layer**
  - A1. What exactly does the architecture-blueprint-generator skill ask an agent to produce?
  - A2. Which parts of architecture inspection does that skill cover well, and which parts does it leave unresolved?
- [fact] **B. Multi-repo orchestration layer**
  - B1. What does RepoSwarm automate across a portfolio of repositories?
  - B2. Does RepoSwarm provide evidence extraction, synthesis, or both?
- [fact] **C. Deterministic evidence layer**
  - C1. What can dependency-cruiser prove from source-code structure?
  - C2. What can GitHub dependency graph, dependency review, and Software Bill of Materials (SBOM) exports prove from manifests?
  - C3. What signals does Renovate provide about dependency drift and consistency?
  - C4. What cross-repository investigation and bulk-remediation capabilities does Sourcegraph expose?
  - C5. What enforcement or auto-remediation role does OpenRewrite play?
- [fact] **D. Governance layer**
  - D1. How can Open Policy Agent (OPA) encode standards checks once architecture facts are normalized?
  - D2. What do architectural decision records (ADRs) and architecture fitness functions contribute that code graphs cannot?
- [fact] **E. Operational synthesis**
  - E1. What composite implementation pattern best fits a GitHub-first environment?
  - E2. Which parts should remain deterministic and which parts should be delegated to Copilot skills or other agents?
  - E3. What gaps remain even after combining these approaches?

### §2 Investigation

**A1–A2 — What the architecture-blueprint-generator skill actually does**

- [fact] The `architecture-blueprint-generator` skill is a prompt template that asks an agent to auto-detect technology stacks and architectural patterns, produce architectural overviews and diagrams, document layer rules, cross-cutting concerns, service communication, testing, deployment, governance, and extension patterns, and optionally include code examples plus architectural decision records. Source: https://raw.githubusercontent.com/github/awesome-copilot/main/skills/architecture-blueprint-generator/SKILL.md
- [fact] The same skill explicitly asks for architecture governance and a blueprint for new development, including automated checks for architectural compliance, review processes, documentation practices, starting points for new features, and common pitfalls. Source: https://raw.githubusercontent.com/github/awesome-copilot/main/skills/architecture-blueprint-generator/SKILL.md
- [inference] The skill is strongest as a **synthesis layer** because it assumes the agent can already inspect the codebase and infer patterns; it does not itself provide a graph extractor, a cross-repo index, or a standards engine. Source: https://raw.githubusercontent.com/github/awesome-copilot/main/skills/architecture-blueprint-generator/SKILL.md
- [fact] The broader awesome-copilot repository positions skills as self-contained folders of instructions and bundled assets, and publishes a machine-readable `llms.txt` index plus searchable website listings for skills, agents, instructions, plugins, and workflows. Source: https://raw.githubusercontent.com/github/awesome-copilot/main/README.md
- [inference] The architecture-blueprint-generator skill is operationally useful only when paired with either repository-local tooling or another platform that supplies the evidence surface it asks the agent to describe. Sources: https://raw.githubusercontent.com/github/awesome-copilot/main/skills/architecture-blueprint-generator/SKILL.md ; https://raw.githubusercontent.com/github/awesome-copilot/main/README.md

**B1–B2 — What RepoSwarm contributes**

- [fact] RepoSwarm describes itself as an "AI-powered multi-repo architecture discovery platform" that analyzes codebase portfolios and generates standardized `.arch.md` files for architecture reviews, onboarding, and Artificial Intelligence (AI) agent context. Source: https://raw.githubusercontent.com/reposwarm/reposwarm/main/README.md
- [fact] RepoSwarm's documented pipeline is `Cache check -> Clone -> Type detection -> Structure analysis -> Prompt selection -> AI analysis -> Store results -> Cleanup`, and it supports incremental updates, smart caching, type-aware prompts, centralized results storage, search, diff, export, and parallel investigations. Source: https://raw.githubusercontent.com/reposwarm/reposwarm/main/README.md
- [fact] RepoSwarm requires Docker, Git, and an LLM provider connection, and its ecosystem includes separate Command Line Interface (CLI), Application Programming Interface (API), user interface, worker, and question-answering components. Source: https://raw.githubusercontent.com/reposwarm/reposwarm/main/README.md
- [inference] RepoSwarm is the strongest open-source example in this evidence base of **portfolio-scale architecture synthesis**, because it combines repo inventory, repeated analysis, standardized output, and result-hub workflows rather than stopping at one-repo graph extraction. Source: https://raw.githubusercontent.com/reposwarm/reposwarm/main/README.md
- [inference] RepoSwarm still depends on prompt-driven interpretation after structure analysis, so it is best viewed as a synthesis-and-orchestration framework, not as a replacement for deterministic extractors or policy engines. Source: https://raw.githubusercontent.com/reposwarm/reposwarm/main/README.md

**C1 — What dependency-cruiser proves**

- [fact] dependency-cruiser validates and visualises JavaScript and TypeScript dependencies, supports custom rules, reports rule violations, and can emit dependency graphs in formats including Graphviz DOT (DOT), Mermaid-compatible paths, JavaScript Object Notation (JSON), comma-separated values (CSV), HyperText Markup Language (HTML), and plain text. Source: https://raw.githubusercontent.com/sverweij/dependency-cruiser/main/README.md
- [fact] dependency-cruiser can detect issues such as circular dependencies, missing dependencies in package manifests, orphaned modules, and custom forbidden dependency paths. Source: https://raw.githubusercontent.com/sverweij/dependency-cruiser/main/README.md
- [inference] dependency-cruiser is a high-confidence source for **declared code-structure edges** inside supported repositories, but it is language-bounded and says nothing directly about runtime traffic, ownership, or architectural rationale. Source: https://raw.githubusercontent.com/sverweij/dependency-cruiser/main/README.md

**C2 — What GitHub dependency graph APIs prove**

- [fact] GitHub's dependency-graph REST surface exposes dependency review between commits, dependency submission, and repository SBOM export; the dependency review endpoint compares manifest-based dependency changes between revisions and returns vulnerability data, while the SBOM endpoint exports Software Package Data Exchange (SPDX) JavaScript Object Notation (JSON) for a repository. Sources: https://docs.github.com/api/article/body?pathname=/en/rest/dependency-graph ; https://docs.github.com/api/article/body?pathname=/en/rest/dependency-graph/dependency-review ; https://docs.github.com/api/article/body?pathname=/en/rest/dependency-graph/sboms
- [fact] The dependency review endpoint is manifest-driven: it reports added and removed packages, their ecosystems, versions, licenses, and known vulnerabilities for a given revision comparison. Source: https://docs.github.com/api/article/body?pathname=/en/rest/dependency-graph/dependency-review
- [inference] GitHub dependency-graph data is strong for package-level supply-chain structure and change impact, but it is not a service-architecture graph and does not natively reveal repository-to-repository call chains, module layering, or business boundaries. Sources: https://docs.github.com/api/article/body?pathname=/en/rest/dependency-graph ; https://docs.github.com/api/article/body?pathname=/en/rest/dependency-graph/dependency-review ; https://docs.github.com/api/article/body?pathname=/en/rest/dependency-graph/sboms

**C3 — What Renovate proves**

- [fact] Renovate automatically discovers relevant package files, works across multiple platforms and languages, supports monorepos, schedules update pull requests, and shares configuration through presets. Source: https://docs.renovatebot.com
- [inference] Renovate is not an architecture-discovery engine, but it is a practical **drift detector** for dependency policy alignment because it continuously sees which dependencies exist, where updates are pending, and whether shared configuration is being applied consistently. Source: https://docs.renovatebot.com

**C4 — What Sourcegraph proves**

- [fact] Sourcegraph documents five relevant capabilities for this problem space: code search across all repositories and branches, code intelligence for definitions and references, Deep Search for agent-assisted codebase questions, Code Insights for query-based trend tracking across thousands of repositories, and Batch Changes for coordinated edits across many repositories and code hosts. Sources: https://sourcegraph.com/docs ; https://sourcegraph.com/docs/code-insights ; https://sourcegraph.com/docs/batch_changes
- [fact] Code Insights can track anything expressible as a Sourcegraph query across large repository sets and backfill historical data, while Batch Changes uses a declarative spec to execute commands and publish changesets across multiple repositories. Sources: https://sourcegraph.com/docs/code-insights ; https://sourcegraph.com/docs/batch_changes
- [inference] Sourcegraph is strongest as a **cross-repo evidence and remediation substrate** rather than as a finished architecture blueprint tool; it makes coupling patterns searchable and standards violations fixable, but another layer must normalize and explain those signals. Sources: https://sourcegraph.com/docs ; https://sourcegraph.com/docs/code-insights ; https://sourcegraph.com/docs/batch_changes

**C5 — What OpenRewrite proves**

- [fact] OpenRewrite is an open-source automated refactoring ecosystem built on Lossless Semantic Trees, visitors, and recipes, with Gradle and Maven plugins for repository-level execution and a commercial Moderne platform for large codebases, multi-repo migrations, and impact analysis. Source: https://docs.openrewrite.org
- [inference] OpenRewrite belongs on the **remediation** side of architecture inspection: once architectural drift is defined as a recipe or rule, OpenRewrite can apply consistent source-code corrections, but it is not itself a portfolio-wide architecture inventory system. Source: https://docs.openrewrite.org

**D1 — What OPA contributes**

- [fact] Open Policy Agent is an open-source, general-purpose policy engine that decouples policy decision-making from enforcement and is explicitly positioned for use in microservices, Kubernetes, CI/CD pipelines, API gateways, and other systems. Source: https://www.openpolicyagent.org/docs/latest/
- [fact] Open Policy Agent evaluates structured input data against Rego policies and can return arbitrary structured outputs rather than only allow-or-deny decisions. Source: https://www.openpolicyagent.org/docs/latest/
- [inference] Open Policy Agent is well suited to architecture-standards checking **after** architecture facts have been normalized into structured data, because it can encode invariants such as forbidden dependencies, required ownership metadata, approved registries, or mandatory file conventions in a reproducible way. Source: https://www.openpolicyagent.org/docs/latest/

**D2 — What ADRs and architecture fitness functions contribute**

- [fact] The ADR guidance site defines an architectural decision record as the capture of a single architecturally significant decision and its rationale, and describes the collection of ADRs as a project's decision log. Source: https://adr.github.io
- [fact] Neal Ford, Rebecca Parsons, and Patrick Kua define an architectural fitness function as an objective integrity assessment of some architectural characteristic, and define evolutionary architecture as guided, incremental change across multiple dimensions protected by such automated checks. Sources: https://nealford.com/books/buildingevolutionaryarchitectures.html ; https://evolutionaryarchitecture.com
- [inference] ADRs answer the question **"why was this boundary or policy chosen?"**, while architecture fitness functions answer **"is the current implementation still respecting that choice?"**; both are necessary because a graph alone rarely exposes rationale and prose alone rarely stops drift. Sources: https://adr.github.io ; https://nealford.com/books/buildingevolutionaryarchitectures.html ; https://evolutionaryarchitecture.com

**E1–E3 — Composite implementation pattern and prior-work constraints**

- [fact] Prior completed work in this repository found that dependency understanding is inherently layered across declared edges, observed edges, and documented or owned relationships, and that each edge should carry provenance, freshness, semantic type, and confidence metadata. Source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-21-dependency-mapping-dotnet-terraform-dynatrace.md
- [fact] Prior completed work on coding AI agent skills concluded that `AGENTS.md` and `SKILL.md` are the lowest-friction portable formats for reusable agent guidance across multiple tools. Sources: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-22-coding-ai-agent-skills-survey.md ; https://agentskills.io
- [fact] Prior completed work on agent evaluation concluded that trajectory capture, structured rubrics, and CI-integrated regression gates are the minimum viable evaluation primitives for agentic systems. Source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-10-agent-evaluation-cross-repo-analysis.md
- [fact] Prior completed work on applied context engineering concluded that tool outputs dominate context windows, that version-controlled declarative manifests improve reproducibility, and that filesystem-backed state tracking can implement resumable workflows without extra infrastructure. Source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-22-applied-context-engineering-agent-workflows.md
- [inference] The strongest implementation pattern for this repository is therefore a **layered composite pipeline**: deterministic per-repo extractors produce normalized facts; GitHub Actions persist those facts as versioned artifacts; Open Policy Agent and related checks evaluate standards drift; and a Copilot skill or RepoSwarm-style agent layer synthesizes those facts into human-readable architectural blueprints. Sources: https://raw.githubusercontent.com/sverweij/dependency-cruiser/main/README.md ; https://docs.github.com/api/article/body?pathname=/en/rest/dependency-graph ; https://www.openpolicyagent.org/docs/latest/ ; https://raw.githubusercontent.com/github/awesome-copilot/main/skills/architecture-blueprint-generator/SKILL.md ; https://raw.githubusercontent.com/reposwarm/reposwarm/main/README.md ; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-21-dependency-mapping-dotnet-terraform-dynatrace.md ; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-10-agent-evaluation-cross-repo-analysis.md ; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-22-applied-context-engineering-agent-workflows.md
- [inference] A GitHub-first implementation should not ask a Copilot skill to infer architecture directly from raw multi-repo sprawl on every run, because that mixes extraction, normalization, governance, and summarization into one opaque step and removes the provenance needed for drift analysis. Sources: https://raw.githubusercontent.com/github/awesome-copilot/main/skills/architecture-blueprint-generator/SKILL.md ; https://raw.githubusercontent.com/reposwarm/reposwarm/main/README.md ; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-21-dependency-mapping-dotnet-terraform-dynatrace.md ; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-10-agent-evaluation-cross-repo-analysis.md
- [assumption] Public documentation accurately describes the documented capabilities of these tools at the time of investigation. **Justification:** this research is restricted to public evidence, and the practical question here is implementation planning from public capabilities rather than adversarial reverse engineering.

### §3 Reasoning

- [inference] I weighted deterministic extractors more heavily than prompt-driven summaries when judging architecture-inspection value, because architecture-drift detection depends on reproducible evidence rather than one-off natural-language descriptions. Sources: https://raw.githubusercontent.com/sverweij/dependency-cruiser/main/README.md ; https://docs.github.com/api/article/body?pathname=/en/rest/dependency-graph/dependency-review ; https://www.openpolicyagent.org/docs/latest/
- [inference] I weighted RepoSwarm and the architecture-blueprint-generator skill highly for usability, but not as primary truth sources, because both operate downstream of earlier extraction and interpretation steps. Sources: https://raw.githubusercontent.com/reposwarm/reposwarm/main/README.md ; https://raw.githubusercontent.com/github/awesome-copilot/main/skills/architecture-blueprint-generator/SKILL.md
- [inference] I treat GitHub dependency graph, dependency-cruiser, Sourcegraph, OpenRewrite, Open Policy Agent, ADRs, and fitness functions as complementary rather than competing, because each answers a different question: what is declared, what changed, what is searchable, what can be fixed, what is allowed, and why the rule exists. Sources: https://docs.github.com/api/article/body?pathname=/en/rest/dependency-graph ; https://raw.githubusercontent.com/sverweij/dependency-cruiser/main/README.md ; https://sourcegraph.com/docs ; https://sourcegraph.com/docs/batch_changes ; https://docs.openrewrite.org ; https://www.openpolicyagent.org/docs/latest/ ; https://adr.github.io ; https://nealford.com/books/buildingevolutionaryarchitectures.html ; https://evolutionaryarchitecture.com
- [inference] I treat portable formats such as `SKILL.md` and `AGENTS.md` as strategically important because they reduce tool lock-in for the synthesized guidance layer even when the underlying extractors differ by language or platform. Sources: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-22-coding-ai-agent-skills-survey.md ; https://agentskills.io

### §4 Consistency Check

- [fact] The evidence remains internally consistent on one core point: no inspected tool offers full multi-repository architecture truth on its own. The code-focused tools expose structure, the policy tools expose standards, the documentation tools expose intent, and the synthesis tools expose explanation. Sources: https://raw.githubusercontent.com/reposwarm/reposwarm/main/README.md ; https://raw.githubusercontent.com/github/awesome-copilot/main/skills/architecture-blueprint-generator/SKILL.md ; https://raw.githubusercontent.com/sverweij/dependency-cruiser/main/README.md ; https://docs.github.com/api/article/body?pathname=/en/rest/dependency-graph ; https://www.openpolicyagent.org/docs/latest/ ; https://adr.github.io
- [fact] The investigated sources do not contradict one another on the role boundaries. RepoSwarm and the architecture-blueprint-generator skill emphasize generation and synthesis, while dependency-cruiser, GitHub dependency APIs, Open Policy Agent, and OpenRewrite emphasize extraction, policy, or remediation. Sources: https://raw.githubusercontent.com/reposwarm/reposwarm/main/README.md ; https://raw.githubusercontent.com/github/awesome-copilot/main/skills/architecture-blueprint-generator/SKILL.md ; https://raw.githubusercontent.com/sverweij/dependency-cruiser/main/README.md ; https://docs.github.com/api/article/body?pathname=/en/rest/dependency-graph ; https://www.openpolicyagent.org/docs/latest/ ; https://docs.openrewrite.org
- [inference] The only meaningful ambiguity is scope breadth: tools with the best multi-repo story, such as RepoSwarm and Sourcegraph, require more infrastructure and integration effort than simple single-repo scanners. That ambiguity affects rollout sequence, not the underlying layered conclusion. Sources: https://raw.githubusercontent.com/reposwarm/reposwarm/main/README.md ; https://sourcegraph.com/docs ; https://sourcegraph.com/docs/batch_changes

### §5 Depth and Breadth Expansion

- [fact] **Technical lens:** architecture inspection breaks into at least four technical layers — extraction, normalization, policy evaluation, and synthesis — and each layer benefits from a different tool family. Sources: https://raw.githubusercontent.com/sverweij/dependency-cruiser/main/README.md ; https://docs.github.com/api/article/body?pathname=/en/rest/dependency-graph ; https://www.openpolicyagent.org/docs/latest/ ; https://raw.githubusercontent.com/github/awesome-copilot/main/skills/architecture-blueprint-generator/SKILL.md ; https://raw.githubusercontent.com/reposwarm/reposwarm/main/README.md ; https://docs.openrewrite.org
- [fact] **Governance lens:** ADRs and architecture fitness functions show that standards drift is not only a technical issue; it also depends on explicit decision records and continuously evaluated constraints. Sources: https://adr.github.io ; https://nealford.com/books/buildingevolutionaryarchitectures.html ; https://evolutionaryarchitecture.com
- [fact] **Economic lens:** tools that start from deterministic extraction and then synthesize from cached artifacts reduce repeated LLM spend and repeated context-window usage compared with re-analyzing whole repository portfolios from scratch every run. Sources: https://raw.githubusercontent.com/reposwarm/reposwarm/main/README.md ; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-22-applied-context-engineering-agent-workflows.md
- [fact] **Operational lens:** GitHub-first teams need reviewable repository artifacts, scheduled workflows, and commit-based drift reports more than they need heavyweight interactive dashboards. Sources: https://github.com/davidamitchell/Research/blob/main/.github/copilot-instructions.md ; https://github.com/davidamitchell/Research/blob/main/README.md
- [inference] **Behavioral lens:** teams are more likely to trust architecture inspection when every reported edge or violation can be traced back to a specific extractor run, file, query, or policy decision; opaque agent summaries create the same trust problem that prior repository research identified in agent evaluation. Sources: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-10-agent-evaluation-cross-repo-analysis.md ; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-21-dependency-mapping-dotnet-terraform-dynatrace.md

### §6 Synthesis

**Executive summary:**

- [inference] The strongest practical approach to multi-repository architecture inspection is a layered pipeline in which deterministic tools extract structural facts and governance signals first, and a Large Language Model (LLM) synthesis layer converts those facts into standardized blueprints, explanations, and prioritized remediation guidance. Sources: https://raw.githubusercontent.com/github/awesome-copilot/main/skills/architecture-blueprint-generator/SKILL.md ; https://raw.githubusercontent.com/reposwarm/reposwarm/main/README.md ; https://raw.githubusercontent.com/sverweij/dependency-cruiser/main/README.md ; https://docs.github.com/api/article/body?pathname=/en/rest/dependency-graph ; https://www.openpolicyagent.org/docs/latest/
- [inference] The architecture-blueprint-generator skill and RepoSwarm are useful because they package explanation and documentation workflows, but neither should be treated as the primary evidence source for coupling or standards drift. Sources: https://raw.githubusercontent.com/github/awesome-copilot/main/skills/architecture-blueprint-generator/SKILL.md ; https://raw.githubusercontent.com/reposwarm/reposwarm/main/README.md
- [inference] GitHub dependency graph, dependency-cruiser, Renovate, Sourcegraph, OpenRewrite, ADR scanning, and Open Policy Agent each illuminate a distinct slice of architecture reality, so the durable answer is composition rather than tool replacement. Sources: https://docs.github.com/api/article/body?pathname=/en/rest/dependency-graph ; https://raw.githubusercontent.com/sverweij/dependency-cruiser/main/README.md ; https://docs.renovatebot.com ; https://sourcegraph.com/docs ; https://docs.openrewrite.org ; https://adr.github.io ; https://www.openpolicyagent.org/docs/latest/
- [inference] For this repository's constraints, the best implementation starts inside GitHub Actions with versioned normalized artifacts and policy checks, then adds Copilot-skill or RepoSwarm-style synthesis only after evidence provenance and evaluation are in place. Sources: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-21-dependency-mapping-dotnet-terraform-dynatrace.md ; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-10-agent-evaluation-cross-repo-analysis.md ; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-22-applied-context-engineering-agent-workflows.md

**Key findings:**

1. [inference] [high confidence] A reliable multi-repository architecture inspection system should separate deterministic extraction from LLM-based synthesis, because reproducible graphs, manifests, and policy facts are required before any narrative blueprint can be trusted, compared across runs, or used for governance decisions. Sources: https://raw.githubusercontent.com/sverweij/dependency-cruiser/main/README.md ; https://docs.github.com/api/article/body?pathname=/en/rest/dependency-graph ; https://www.openpolicyagent.org/docs/latest/ ; https://raw.githubusercontent.com/github/awesome-copilot/main/skills/architecture-blueprint-generator/SKILL.md
2. [fact] [high confidence] The architecture-blueprint-generator skill is a comprehensive architecture-documentation prompt covering technology detection, diagrams, layer rules, cross-cutting concerns, governance, and decision records, but it does not ship any native mechanism for cross-repository graph extraction or standards enforcement. Source: https://raw.githubusercontent.com/github/awesome-copilot/main/skills/architecture-blueprint-generator/SKILL.md
3. [inference] [medium confidence] RepoSwarm is the strongest open-source portfolio-analysis example in this evidence base because it performs multi-repository investigations, applies type-aware prompts, emits standardized `.arch.md` outputs, supports incremental updates, and keeps searchable results for later comparison. Source: https://raw.githubusercontent.com/reposwarm/reposwarm/main/README.md
4. [inference] [high confidence] dependency-cruiser, GitHub dependency graph and Software Bill of Materials (SBOM) exports, Renovate, and Sourcegraph each reveal a different structural layer — code imports, package manifests, dependency drift, and cross-repo search or bulk edits — so none of them alone is a complete architecture inspector. Sources: https://raw.githubusercontent.com/sverweij/dependency-cruiser/main/README.md ; https://docs.github.com/api/article/body?pathname=/en/rest/dependency-graph ; https://docs.github.com/api/article/body?pathname=/en/rest/dependency-graph/sboms ; https://docs.renovatebot.com ; https://sourcegraph.com/docs ; https://sourcegraph.com/docs/code-insights ; https://sourcegraph.com/docs/batch_changes
5. [inference] [high confidence] Standards alignment should be implemented as machine-checkable architecture fitness functions and policy rules over normalized facts, while architectural decision records (ADRs) remain the durable source for rationale and trade-off context that code graphs cannot express alone. Sources: https://www.openpolicyagent.org/docs/latest/ ; https://adr.github.io ; https://nealford.com/books/buildingevolutionaryarchitectures.html ; https://evolutionaryarchitecture.com
6. [inference] [medium confidence] OpenRewrite and Sourcegraph Batch Changes are better treated as remediation engines than as discovery systems, because they become valuable only after an earlier layer has already identified the drift pattern or forbidden dependency that must be corrected across repositories. Sources: https://docs.openrewrite.org ; https://sourcegraph.com/docs/batch_changes
7. [fact] [high confidence] Prior repository research shows that any credible cross-repo architecture map must preserve provenance, freshness, semantic type, and confidence metadata on each edge, because declared structure, observed behavior, and documented intent are different kinds of truth rather than competing measurements of one truth. Source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-21-dependency-mapping-dotnet-terraform-dynatrace.md
8. [inference] [high confidence] In a GitHub-first operating model, the rollout that best matches this repository's constraints is to run repository scanners and normalizers in GitHub Actions, store the outputs as reviewable versioned artifacts, evaluate standards with policy-as-code, and then use a Copilot skill or RepoSwarm-style agent to generate the human-facing blueprint and remediation summary. Sources: https://docs.github.com/api/article/body?pathname=/en/rest/dependency-graph ; https://raw.githubusercontent.com/sverweij/dependency-cruiser/main/README.md ; https://www.openpolicyagent.org/docs/latest/ ; https://raw.githubusercontent.com/github/awesome-copilot/main/skills/architecture-blueprint-generator/SKILL.md ; https://raw.githubusercontent.com/reposwarm/reposwarm/main/README.md

**Evidence map:**

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [inference] Deterministic extraction must precede LLM synthesis for trusted architecture inspection. | https://raw.githubusercontent.com/sverweij/dependency-cruiser/main/README.md ; https://docs.github.com/api/article/body?pathname=/en/rest/dependency-graph ; https://www.openpolicyagent.org/docs/latest/ ; https://raw.githubusercontent.com/github/awesome-copilot/main/skills/architecture-blueprint-generator/SKILL.md | high | Needed for reproducibility, diffs, and trusted governance. |
| [fact] architecture-blueprint-generator is a synthesis prompt, not a native extractor or policy engine. | https://raw.githubusercontent.com/github/awesome-copilot/main/skills/architecture-blueprint-generator/SKILL.md | high | Covers governance and diagrams, but not graph extraction. |
| [fact] RepoSwarm provides multi-repo investigations and standardized `.arch.md` outputs. | https://raw.githubusercontent.com/reposwarm/reposwarm/main/README.md | medium | Strongest open-source orchestration example in this evidence base. |
| [inference] dependency-cruiser, GitHub dependency graph, Renovate, and Sourcegraph cover different structural layers. | https://raw.githubusercontent.com/sverweij/dependency-cruiser/main/README.md ; https://docs.github.com/api/article/body?pathname=/en/rest/dependency-graph ; https://docs.github.com/api/article/body?pathname=/en/rest/dependency-graph/sboms ; https://docs.renovatebot.com ; https://sourcegraph.com/docs ; https://sourcegraph.com/docs/code-insights ; https://sourcegraph.com/docs/batch_changes | high | Complementary, not substitutable. |
| [inference] Standards alignment belongs in policy rules plus architecture fitness functions, with ADRs preserving rationale. | https://www.openpolicyagent.org/docs/latest/ ; https://adr.github.io ; https://nealford.com/books/buildingevolutionaryarchitectures.html ; https://evolutionaryarchitecture.com | high | Policies catch drift; ADRs preserve intent. |
| [inference] OpenRewrite and Batch Changes are remediation layers. | https://docs.openrewrite.org ; https://sourcegraph.com/docs/batch_changes | medium | Useful after violations are detected. |
| [fact] Provenance, freshness, semantic type, and confidence must be preserved per edge. | https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-21-dependency-mapping-dotnet-terraform-dynatrace.md | high | Reuses established repository pattern. |
| [inference] GitHub Actions plus versioned artifacts is the rollout path that best matches this repository's operating constraints. | https://docs.github.com/api/article/body?pathname=/en/rest/dependency-graph ; https://raw.githubusercontent.com/sverweij/dependency-cruiser/main/README.md ; https://www.openpolicyagent.org/docs/latest/ ; https://raw.githubusercontent.com/github/awesome-copilot/main/skills/architecture-blueprint-generator/SKILL.md ; https://raw.githubusercontent.com/reposwarm/reposwarm/main/README.md | high | Matches the owner's operating constraints. |

**Assumptions:**

- [assumption] Public documentation is sufficiently current to support an implementation-plan recommendation. **Justification:** this item is scoped to public capability discovery, not private deployment verification.
- [assumption] The target repositories can tolerate small repository-local configuration files for scanners, policies, or generated outputs. **Justification:** every practical approach here requires at least one local configuration or artifact format.
- [assumption] RepoSwarm's repository overview is representative of its present practical behavior. **Justification:** no live RepoSwarm instance was deployed during this item.

**Analysis:**

- [inference] The evidence supports a four-stage operating model: **extract -> normalize -> evaluate -> synthesize**. That structure is the smallest one that preserves provenance while still producing a usable architectural narrative. Sources: https://raw.githubusercontent.com/sverweij/dependency-cruiser/main/README.md ; https://docs.github.com/api/article/body?pathname=/en/rest/dependency-graph ; https://www.openpolicyagent.org/docs/latest/ ; https://raw.githubusercontent.com/github/awesome-copilot/main/skills/architecture-blueprint-generator/SKILL.md
- [inference] Extraction should remain deterministic whenever possible, because architecture inspection loses organizational trust quickly when it cannot explain why an edge or violation was reported. Sources: https://raw.githubusercontent.com/sverweij/dependency-cruiser/main/README.md ; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-10-agent-evaluation-cross-repo-analysis.md
- [inference] Synthesis is the natural place for Copilot skills and RepoSwarm-style agents, because they add clear value when translating structured evidence into diagrams, boundary explanations, onboarding context, and prioritized remediation advice. Sources: https://raw.githubusercontent.com/github/awesome-copilot/main/skills/architecture-blueprint-generator/SKILL.md ; https://raw.githubusercontent.com/reposwarm/reposwarm/main/README.md
- [inference] Remediation should remain separable from synthesis, because policy violations and dependency drift often need code changes that can be automated independently of the documentation pass. Sources: https://docs.openrewrite.org ; https://sourcegraph.com/docs/batch_changes ; https://www.openpolicyagent.org/docs/latest/
- [inference] The core design decision is therefore not which single product wins, but where the repository draws the boundary between evidence production and interpretation. Sources: https://raw.githubusercontent.com/github/awesome-copilot/main/skills/architecture-blueprint-generator/SKILL.md ; https://raw.githubusercontent.com/reposwarm/reposwarm/main/README.md ; https://raw.githubusercontent.com/sverweij/dependency-cruiser/main/README.md ; https://www.openpolicyagent.org/docs/latest/

**Risks, gaps, uncertainties:**

- [fact] The public evidence base is weaker on mature, language-agnostic open-source call-graph extraction across heterogeneous estates than it is on package, manifest, and repository-level metadata extraction. Sources: https://raw.githubusercontent.com/sverweij/dependency-cruiser/main/README.md ; https://docs.github.com/api/article/body?pathname=/en/rest/dependency-graph ; https://raw.githubusercontent.com/reposwarm/reposwarm/main/README.md
- [fact] RepoSwarm's repository overview is strong on end-to-end workflow shape, but weaker on the exact internal normalization model it uses before prompt generation. Source: https://raw.githubusercontent.com/reposwarm/reposwarm/main/README.md
- [fact] GitHub dependency-graph data is package-focused, so teams can misread package visibility as service-architecture visibility if they do not distinguish those semantics explicitly. Sources: https://docs.github.com/api/article/body?pathname=/en/rest/dependency-graph ; https://docs.github.com/api/article/body?pathname=/en/rest/dependency-graph/sboms
- [inference] A rollout that lets an agent inspect raw repository portfolios without first creating normalized evidence artifacts will likely become expensive, hard to review, and difficult to trust as repo count grows. Sources: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-10-agent-evaluation-cross-repo-analysis.md ; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-21-dependency-mapping-dotnet-terraform-dynatrace.md ; https://raw.githubusercontent.com/reposwarm/reposwarm/main/README.md

**Open questions:**

- What is the thinnest normalized architecture schema that can represent imports, package dependencies, ownership, standards violations, ADR references, and generated blueprint links without becoming another heavyweight enterprise metamodel?
- Which open-source extractors outside the JavaScript and Java ecosystems are mature enough to provide equivalent structural evidence for Python, .NET, Go, and Infrastructure as Code (IaC) repositories?
- What is the minimum evaluation harness needed to measure false-positive and false-negative rates for cross-repository coupling detection before the system is trusted as a governance control?
- Should the synthesized output live primarily as per-repo architecture files, a central results hub, or both?

### §7 Recursive Review

- [fact] Every claim-bearing sentence in `## Research Skill Output` is labeled as `[fact]`, `[inference]`, or `[assumption]`. Source: this document's `## Research Skill Output` section.
- [fact] All factual claims are anchored either to URL-level citations or to prior completed research items cited by GitHub URL. Source: this document's `## Research Skill Output` section.
- [fact] The first-use acronym audit was completed for the commonly failed terms in this document, including Large Language Model (LLM), Application Programming Interface (API), Model Context Protocol (MCP), Software Bill of Materials (SBOM), Command Line Interface (CLI), Infrastructure as Code (IaC), Open Policy Agent (OPA), and architectural decision records (ADRs). Source: this document's `## Research Skill Output` and `## Findings` sections.
- [fact] Findings below were seeded from §6 and do not introduce new claims not already present in the Research Skill Output. Source: this document's `### §6 Synthesis` and `## Findings` sections.
- [inference] The remaining uncertainty is not about the core conclusion, but about which extractor mix would be best for a specific future estate; that is an implementation-detail gap, not a contradiction in the synthesis. Sources: https://raw.githubusercontent.com/sverweij/dependency-cruiser/main/README.md ; https://raw.githubusercontent.com/reposwarm/reposwarm/main/README.md ; https://docs.github.com/api/article/body?pathname=/en/rest/dependency-graph

---

## Findings

*(Populated from §6 Synthesis above.)*

### Executive Summary

[inference] The best-supported answer is that multi-repository architecture inspection should be implemented as a layered system in which deterministic tools extract structural and governance facts first, and a Large Language Model (LLM) layer produces the human-readable blueprint second. Sources: https://raw.githubusercontent.com/sverweij/dependency-cruiser/main/README.md ; https://docs.github.com/api/article/body?pathname=/en/rest/dependency-graph ; https://www.openpolicyagent.org/docs/latest/ ; https://raw.githubusercontent.com/github/awesome-copilot/main/skills/architecture-blueprint-generator/SKILL.md

[inference] GitHub Copilot skills such as architecture-blueprint-generator and adjacent systems such as RepoSwarm are valuable because they package explanation, documentation, and workflow orchestration, but they are not strong enough on their own to serve as the primary truth source for coupling or standards drift. Sources: https://raw.githubusercontent.com/github/awesome-copilot/main/skills/architecture-blueprint-generator/SKILL.md ; https://raw.githubusercontent.com/reposwarm/reposwarm/main/README.md

[inference] The practical implementation seam is therefore `extract -> normalize -> evaluate -> synthesize`, with GitHub Actions running scanners and policy checks, versioned artifacts preserving provenance, and the synthesis layer turning those artifacts into reviewable architectural summaries. Sources: https://docs.github.com/api/article/body?pathname=/en/rest/dependency-graph ; https://raw.githubusercontent.com/sverweij/dependency-cruiser/main/README.md ; https://www.openpolicyagent.org/docs/latest/ ; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-10-agent-evaluation-cross-repo-analysis.md ; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-22-applied-context-engineering-agent-workflows.md

[inference] This matters because architecture understanding, standards enforcement, and cross-repository remediation require different mechanisms, and mixing them into one opaque agent step removes the provenance needed for drift analysis, trust, and repeatable governance. Sources: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-21-dependency-mapping-dotnet-terraform-dynatrace.md ; https://www.openpolicyagent.org/docs/latest/ ; https://docs.openrewrite.org

### Key Findings

1. [inference] [high confidence] A reliable multi-repository architecture inspection system should separate deterministic extraction from LLM-based synthesis, because reproducible graphs, manifests, and policy facts are required before any narrative blueprint can be trusted, compared across runs, or used for governance decisions. Sources: https://raw.githubusercontent.com/sverweij/dependency-cruiser/main/README.md ; https://docs.github.com/api/article/body?pathname=/en/rest/dependency-graph ; https://www.openpolicyagent.org/docs/latest/ ; https://raw.githubusercontent.com/github/awesome-copilot/main/skills/architecture-blueprint-generator/SKILL.md
2. [fact] [high confidence] The architecture-blueprint-generator skill is a comprehensive architecture-documentation prompt covering technology detection, diagrams, layer rules, cross-cutting concerns, governance, and decision records, but it does not ship any native mechanism for cross-repository graph extraction or standards enforcement. Source: https://raw.githubusercontent.com/github/awesome-copilot/main/skills/architecture-blueprint-generator/SKILL.md
3. [inference] [medium confidence] RepoSwarm is the strongest open-source portfolio-analysis example in this evidence base because it performs multi-repository investigations, applies type-aware prompts, emits standardized `.arch.md` outputs, supports incremental updates, and keeps searchable results for later comparison. Source: https://raw.githubusercontent.com/reposwarm/reposwarm/main/README.md
4. [inference] [high confidence] dependency-cruiser, GitHub dependency graph and Software Bill of Materials (SBOM) exports, Renovate, and Sourcegraph each reveal a different structural layer — code imports, package manifests, dependency drift, and cross-repo search or bulk edits — so none of them alone is a complete architecture inspector. Sources: https://raw.githubusercontent.com/sverweij/dependency-cruiser/main/README.md ; https://docs.github.com/api/article/body?pathname=/en/rest/dependency-graph ; https://docs.github.com/api/article/body?pathname=/en/rest/dependency-graph/sboms ; https://docs.renovatebot.com ; https://sourcegraph.com/docs ; https://sourcegraph.com/docs/code-insights ; https://sourcegraph.com/docs/batch_changes
5. [inference] [high confidence] Standards alignment should be implemented as machine-checkable architecture fitness functions and policy rules over normalized facts, while architectural decision records (ADRs) remain the durable source for rationale and trade-off context that code graphs cannot express alone. Sources: https://www.openpolicyagent.org/docs/latest/ ; https://adr.github.io ; https://nealford.com/books/buildingevolutionaryarchitectures.html ; https://evolutionaryarchitecture.com
6. [inference] [medium confidence] OpenRewrite and Sourcegraph Batch Changes are better treated as remediation engines than as discovery systems, because they become valuable only after an earlier layer has already identified the drift pattern or forbidden dependency that must be corrected across repositories. Sources: https://docs.openrewrite.org ; https://sourcegraph.com/docs/batch_changes
7. [fact] [high confidence] Prior repository research shows that any credible cross-repo architecture map must preserve provenance, freshness, semantic type, and confidence metadata on each edge, because declared structure, observed behavior, and documented intent are different kinds of truth rather than competing measurements of one truth. Source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-21-dependency-mapping-dotnet-terraform-dynatrace.md
8. [inference] [high confidence] In a GitHub-first operating model, the rollout that best matches this repository's constraints is to run repository scanners and normalizers in GitHub Actions, store the outputs as reviewable versioned artifacts, evaluate standards with policy-as-code, and then use a Copilot skill or RepoSwarm-style agent to generate the human-facing blueprint and remediation summary. Sources: https://docs.github.com/api/article/body?pathname=/en/rest/dependency-graph ; https://raw.githubusercontent.com/sverweij/dependency-cruiser/main/README.md ; https://www.openpolicyagent.org/docs/latest/ ; https://raw.githubusercontent.com/github/awesome-copilot/main/skills/architecture-blueprint-generator/SKILL.md ; https://raw.githubusercontent.com/reposwarm/reposwarm/main/README.md

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [inference] Deterministic extraction before LLM synthesis is the recommended trust boundary for architecture inspection. | https://raw.githubusercontent.com/sverweij/dependency-cruiser/main/README.md ; https://docs.github.com/api/article/body?pathname=/en/rest/dependency-graph ; https://www.openpolicyagent.org/docs/latest/ ; https://raw.githubusercontent.com/github/awesome-copilot/main/skills/architecture-blueprint-generator/SKILL.md | high | [inference] Reproducibility and drift comparison depend on stable extracted evidence. |
| [fact] architecture-blueprint-generator is a synthesis prompt, not a native extractor or policy engine. | https://raw.githubusercontent.com/github/awesome-copilot/main/skills/architecture-blueprint-generator/SKILL.md | high | [inference] The documented scope emphasizes output structure and governance prompts rather than raw evidence capture. |
| [inference] RepoSwarm provides the clearest open-source multi-repo architecture workflow in this evidence base. | https://raw.githubusercontent.com/reposwarm/reposwarm/main/README.md | medium | Workflow evidence is strong; live deployment evidence was not inspected. |
| [inference] dependency-cruiser, GitHub dependency graph, Renovate, and Sourcegraph cover different structural layers. | https://raw.githubusercontent.com/sverweij/dependency-cruiser/main/README.md ; https://docs.github.com/api/article/body?pathname=/en/rest/dependency-graph ; https://docs.github.com/api/article/body?pathname=/en/rest/dependency-graph/sboms ; https://docs.renovatebot.com ; https://sourcegraph.com/docs ; https://sourcegraph.com/docs/code-insights ; https://sourcegraph.com/docs/batch_changes | high | Complementary coverage is the main pattern. |
| [inference] Standards alignment belongs in policy rules and architecture fitness functions, with ADRs preserving rationale. | https://www.openpolicyagent.org/docs/latest/ ; https://adr.github.io ; https://nealford.com/books/buildingevolutionaryarchitectures.html ; https://evolutionaryarchitecture.com | high | [inference] Policy checks detect drift, while ADRs retain the boundary rationale that code alone does not expose. |
| [inference] OpenRewrite and Batch Changes are remediation layers. | https://docs.openrewrite.org ; https://sourcegraph.com/docs/batch_changes | medium | Useful after violations are detected. |
| [fact] Cross-repo architecture maps need provenance, freshness, semantic type, and confidence metadata on each edge. | https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-21-dependency-mapping-dotnet-terraform-dynatrace.md | high | Reuses established repository pattern. |
| [inference] A GitHub-native rollout with versioned artifacts best matches this repository's operating constraints. | https://docs.github.com/api/article/body?pathname=/en/rest/dependency-graph ; https://raw.githubusercontent.com/sverweij/dependency-cruiser/main/README.md ; https://www.openpolicyagent.org/docs/latest/ ; https://raw.githubusercontent.com/github/awesome-copilot/main/skills/architecture-blueprint-generator/SKILL.md ; https://raw.githubusercontent.com/reposwarm/reposwarm/main/README.md | high | [inference] The repository's web-first operating model favors reviewable workflow outputs over ad hoc local tooling. |

### Assumptions

- [assumption] Public documentation is sufficiently current to support an implementation-plan recommendation. **Justification:** this item is scoped to public capability discovery, not private deployment verification. Sources: https://raw.githubusercontent.com/reposwarm/reposwarm/main/README.md ; https://raw.githubusercontent.com/github/awesome-copilot/main/skills/architecture-blueprint-generator/SKILL.md
- [assumption] The target repositories can tolerate small repository-local configuration files for scanners, policies, or generated outputs. **Justification:** every practical approach here requires at least one local configuration or artifact format. Sources: https://raw.githubusercontent.com/sverweij/dependency-cruiser/main/README.md ; https://www.openpolicyagent.org/docs/latest/
- [assumption] RepoSwarm's repository overview is representative of its present practical behavior. **Justification:** no live RepoSwarm instance was deployed during this item. Source: https://raw.githubusercontent.com/reposwarm/reposwarm/main/README.md

### Analysis

- [inference] The evidence supports a four-stage operating model: **extract -> normalize -> evaluate -> synthesize**. That structure is the smallest one that preserves provenance while still producing a usable architectural narrative. Sources: https://raw.githubusercontent.com/sverweij/dependency-cruiser/main/README.md ; https://docs.github.com/api/article/body?pathname=/en/rest/dependency-graph ; https://www.openpolicyagent.org/docs/latest/ ; https://raw.githubusercontent.com/github/awesome-copilot/main/skills/architecture-blueprint-generator/SKILL.md
- [inference] Extraction should remain deterministic whenever possible, because architecture inspection loses organizational trust quickly when it cannot explain why an edge or violation was reported. Sources: https://raw.githubusercontent.com/sverweij/dependency-cruiser/main/README.md ; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-10-agent-evaluation-cross-repo-analysis.md
- [inference] Synthesis is the natural place for Copilot skills and RepoSwarm-style agents, because they add clear value when translating structured evidence into diagrams, boundary explanations, onboarding context, and prioritized remediation advice. Sources: https://raw.githubusercontent.com/github/awesome-copilot/main/skills/architecture-blueprint-generator/SKILL.md ; https://raw.githubusercontent.com/reposwarm/reposwarm/main/README.md
- [inference] Remediation should remain separable from synthesis, because policy violations and dependency drift often need code changes that can be automated independently of the documentation pass. Sources: https://docs.openrewrite.org ; https://sourcegraph.com/docs/batch_changes ; https://www.openpolicyagent.org/docs/latest/
- [inference] The core design decision is therefore not which single product wins, but where the repository draws the boundary between evidence production and interpretation. Sources: https://raw.githubusercontent.com/github/awesome-copilot/main/skills/architecture-blueprint-generator/SKILL.md ; https://raw.githubusercontent.com/reposwarm/reposwarm/main/README.md ; https://raw.githubusercontent.com/sverweij/dependency-cruiser/main/README.md ; https://www.openpolicyagent.org/docs/latest/

### Risks, Gaps, and Uncertainties

- [fact] The public evidence base is weaker on mature, language-agnostic open-source call-graph extraction across heterogeneous estates than it is on package, manifest, and repository-level metadata extraction. Sources: https://raw.githubusercontent.com/sverweij/dependency-cruiser/main/README.md ; https://docs.github.com/api/article/body?pathname=/en/rest/dependency-graph ; https://raw.githubusercontent.com/reposwarm/reposwarm/main/README.md
- [fact] RepoSwarm's repository overview is strong on end-to-end workflow shape, but weaker on the exact internal normalization model it uses before prompt generation. Source: https://raw.githubusercontent.com/reposwarm/reposwarm/main/README.md
- [fact] GitHub dependency-graph data is package-focused, so teams can misread package visibility as service-architecture visibility if they do not distinguish those semantics explicitly. Sources: https://docs.github.com/api/article/body?pathname=/en/rest/dependency-graph ; https://docs.github.com/api/article/body?pathname=/en/rest/dependency-graph/sboms
- [inference] A rollout that lets an agent inspect raw repository portfolios without first creating normalized evidence artifacts will likely become expensive, hard to review, and difficult to trust as repo count grows. Sources: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-10-agent-evaluation-cross-repo-analysis.md ; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-21-dependency-mapping-dotnet-terraform-dynatrace.md ; https://raw.githubusercontent.com/reposwarm/reposwarm/main/README.md

### Open Questions

- What is the thinnest normalized architecture schema that can represent imports, package dependencies, ownership, standards violations, ADR references, and generated blueprint links without becoming another heavyweight enterprise metamodel?
- Which open-source extractors outside the JavaScript and Java ecosystems are mature enough to provide equivalent structural evidence for Python, .NET, Go, and Infrastructure as Code (IaC) repositories?
- What is the minimum evaluation harness needed to measure false-positive and false-negative rates for cross-repository coupling detection before the system is trusted as a governance control?
- Should the synthesized output live primarily as per-repo architecture files, a central results hub, or both?

---

## Output

- Type: knowledge, backlog-item
- Description: A practical implementation blueprint for cross-repository architecture inspection that separates deterministic extraction, normalized evidence, policy evaluation, and Copilot- or RepoSwarm-based synthesis for a GitHub-first workflow.
- Links:
  - https://raw.githubusercontent.com/github/awesome-copilot/main/skills/architecture-blueprint-generator/SKILL.md
  - https://raw.githubusercontent.com/reposwarm/reposwarm/main/README.md
  - https://www.openpolicyagent.org/docs/latest/