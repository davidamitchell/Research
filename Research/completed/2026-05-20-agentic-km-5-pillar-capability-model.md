---
title: "What is the most practical enterprise design for a five-pillar knowledge management capability model for tool-using, semi-autonomous Artificial Intelligence systems, and how should existing architecture and governance frameworks be extended to support it?"
review_count: 2
added: 2026-05-20T21:41:45+00:00
status: completed
priority: high
blocks: []
started: 2026-05-21T10:35:23+00:00
completed: 2026-05-21T10:58:17+00:00
output: [knowledge]
themes: [agentic-ai, benchmarks-eval, organisational-design, tools-infrastructure]
cites:
  - 2026-03-03-knowledge-representation-agent-context
  - 2026-03-02-agent-memory-management-context-injection
  - 2026-03-08-context-engineering-first-principles
  - 2026-03-01-agent-lsp-policy-enforcement
  - 2026-03-12-failure-mode-taxonomy-expansion
  - 2026-03-10-agent-evaluation-cross-repo-analysis
  - 2026-03-08-servicenow-csdm-data-modelling
  - 2026-05-08-ai-capability-reference-architecture-second-cycle-update
  - 2026-05-06-aibom-regulatory-eu-ai-act-intersection
related:
  - 2026-03-08-servicenow-ai-knowledge-rag-agents
  - 2026-03-05-general-agent-optimization-framework
  - 2026-03-02-integrative-framework-agent-decision-making
  - 2026-03-02-transaction-costs
  - 2026-04-27-governance-moat-prior-research-implications
superseded_by: ~
supersedes: ~
item_type: synthesis
confidence: medium
versions:
  - version: "1.0"
    sha: c4cfa466747f148df7252c62f23036c9ab9babdf
    changed: 2026-05-21
    progress: progress/2026-05-21-agentic-km-5-pillar-capability-model.md
    summary: Initial completion
---

# What is the most practical enterprise design for a five-pillar knowledge management capability model for tool-using, semi-autonomous Artificial Intelligence systems, and how should existing architecture and governance frameworks be extended to support it?

## Research Question

What capability architecture, control model, and operating system of work best implement a five-pillar agentic, meaning tool-using and semi-autonomous, Knowledge Management (KM) model for Artificial Intelligence (AI) systems, and which extensions are required to align established enterprise frameworks with this model?

## Scope

**In scope:**
- Pillar 1, knowledge foundations and representation: dynamic ontology lifecycle using Resource Description Framework (RDF), Web Ontology Language (OWL), and Simple Knowledge Organization System (SKOS); graph-plus-embedding layering; conflict detection and automated reconciliation patterns
- Pillar 2, context engineering and orchestration: hierarchical context compression, relevance filtering, progressive disclosure, token-latency trade-offs, and formal intent injection from mission, values, and strategy artifacts
- Pillar 3, memory, state, and persistence: short-term versus long-term memory partitioning, freshness and invalidation, decay signaling, provenance, and reconciliation of orphaned or external state
- Pillar 4, governance, risk, security, and compliance: agent-specific threat taxonomy, hallucination, context poisoning, and autonomy-drift controls, Artificial Intelligence Bill of Materials (AIBOM) supply-chain controls, and least-privilege policy injection patterns
- Pillar 5, operations, enablement, and continuous improvement: automated curation and verification loops, role-model evolution, evaluation frameworks, observability, and return on investment (ROI) tracking
- Cross-cutting mapping to The Open Group Architecture Framework (TOGAF), Common Service Data Model (CSDM), and enterprise AI reference-architecture patterns
- Real-world pilot designs and case evidence on implementation sequence, failure modes, and measurable outcomes

**Out of scope:**
- Building production software or workflows in this item
- Vendor procurement recommendations tied to a specific platform
- Jurisdiction-specific legal advice
- Deep model-level interpretability research unrelated to Knowledge Management architecture and operations

**Constraints:** Focus on sources from 2022 onward unless a source is foundational; prefer standards, peer-reviewed work, official enterprise architecture guidance, and published implementation reports; produce a knowledge output that can spawn implementation backlog slices.

## Context

This item consolidates prior completed work on knowledge representation, context engineering, memory architecture, policy enforcement, failure modes, and evaluation into a single enterprise architecture question. [fact; source: https://davidamitchell.github.io/Research/research/2026-03-03-knowledge-representation-agent-context.html; https://davidamitchell.github.io/Research/research/2026-03-02-agent-memory-management-context-injection.html; https://davidamitchell.github.io/Research/research/2026-03-08-context-engineering-first-principles.html; https://davidamitchell.github.io/Research/research/2026-03-01-agent-lsp-policy-enforcement.html; https://davidamitchell.github.io/Research/research/2026-03-12-failure-mode-taxonomy-expansion.html; https://davidamitchell.github.io/Research/research/2026-03-10-agent-evaluation-cross-repo-analysis.html]

The unresolved problem is no longer whether those component families matter, but how to sequence them so that knowledge, context, memory, governance, and operational evidence remain separately governable while still working as one production capability stack. [inference; source: https://davidamitchell.github.io/Research/research/2026-05-08-ai-capability-reference-architecture-second-cycle-update.html; https://davidamitchell.github.io/Research/research/2026-03-08-servicenow-csdm-data-modelling.html; https://www.opengroup.org/togaf]

## Approach

1. **Validate pillar boundaries and dependencies.** Define each pillar as a capability domain, identify overlap, and specify minimal dependency order for phased adoption.
2. **Pillar 1 synthesis, knowledge foundations.** Assess enterprise-scale ontology and knowledge graph operating models, including versioning, conflict resolution, and graph-plus-embedding interoperability.
3. **Pillar 2 synthesis, context engineering.** Evaluate architectures and benchmarks for context compression and orchestration, and specify formal structures for organisational intent injection.
4. **Pillar 3 synthesis, memory and persistence.** Compare multi-tier memory models, freshness and invalidation controls, and provenance designs for long-running agent ecosystems.
5. **Pillar 4 synthesis, governance and security.** Build a risk taxonomy and mitigation matrix for agentic threats, and evaluate policy-based authorization and runtime policy injection.
6. **Pillar 5 synthesis, operations and improvement.** Derive operating-model requirements for roles, training, controls, observability, evaluation cadence, and measurable value metrics.
7. **Cross-walk established frameworks.** Map TOGAF, CSDM, and enterprise multi-agent reference architectures to the five pillars, then identify extension points and gaps.
8. **Validate with case evidence.** Gather pilot and benchmark evidence, classify failure modes and quantified outcomes, then produce implementation-sequencing guidance.

## Sources

- [x] [World Wide Web Consortium (W3C) (2014) RDF 1.1 Concepts and Abstract Syntax](https://www.w3.org/TR/rdf11-concepts/)
- [x] [W3C (2012) OWL 2 Web Ontology Language Document Overview](https://www.w3.org/TR/owl2-overview/)
- [x] [W3C (2009) SKOS Simple Knowledge Organization System Reference](https://www.w3.org/TR/skos-reference/)
- [x] [Edge et al. (2024) From Local to Global: a graph-based approach to query-focused summarization](https://arxiv.org/abs/2404.16130)
- [x] [Anthropic (2025) Effective context engineering for AI agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)
- [x] [National Institute of Standards and Technology (NIST) (2023) Artificial Intelligence Risk Management Framework 1.0](https://www.nist.gov/itl/ai-risk-management-framework)
- [x] [NIST (2026) Artificial Intelligence Risk Management Framework Playbook](https://airc.nist.gov/airmf-resources/playbook/)
- [x] [Open Worldwide Application Security Project (OWASP) (2025) Prompt injection](https://genai.owasp.org/llmrisk/llm01-prompt-injection/)
- [x] [OWASP (2025) Sensitive information disclosure](https://genai.owasp.org/llmrisk/llm022025-sensitive-information-disclosure/)
- [x] [OWASP (2025) Improper output handling](https://genai.owasp.org/llmrisk/llm052025-improper-output-handling/)
- [x] [CycloneDX (2026) Machine Learning Bill of Materials](https://cyclonedx.org/capabilities/mlbom/)
- [x] [The Open Group (2026) TOGAF](https://www.opengroup.org/togaf)
- [x] [Amazon Web Services (AWS) (2026) Best practices for enterprise generative AI adoption and scaling](https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-enterprise-ready-gen-ai-platform/best-practices.html)
- [x] [Google Cloud (2025) Multi-agent AI system](https://docs.cloud.google.com/architecture/multiagent-ai-system)
- [x] [Microsoft (2025) Multi-agent Reference Architecture: Reference Architecture](https://microsoft.github.io/multi-agent-reference-architecture/docs/reference-architecture/Reference-Architecture.html)
- [x] [Microsoft (2025) Multi-agent Reference Architecture: Governance](https://microsoft.github.io/multi-agent-reference-architecture/docs/governance/Governance.html)
- [x] [Microsoft (2025) Multi-agent Reference Architecture: Observability](https://microsoft.github.io/multi-agent-reference-architecture/docs/observability/Observability.html)
- [x] [Microsoft (2025) Multi-agent Reference Architecture: Evaluation](https://microsoft.github.io/multi-agent-reference-architecture/docs/evaluation/Evaluation.html)
- [x] [Zep (2025) State of the art agent memory](https://blog.getzep.com/state-of-the-art-agent-memory/)
- [x] [Mitchell (2026) Knowledge representation for agent context](https://davidamitchell.github.io/Research/research/2026-03-03-knowledge-representation-agent-context.html)
- [x] [Mitchell (2026) Agent memory management and context injection](https://davidamitchell.github.io/Research/research/2026-03-02-agent-memory-management-context-injection.html)
- [x] [Mitchell (2026) Context engineering: first principles of steering Large Language Model output without control](https://davidamitchell.github.io/Research/research/2026-03-08-context-engineering-first-principles.html)
- [x] [Mitchell (2026) Guiding headless agents via Language Server Protocol-like mechanisms for organisational policy conformance](https://davidamitchell.github.io/Research/research/2026-03-01-agent-lsp-policy-enforcement.html)
- [x] [Mitchell (2026) Failure mode taxonomy expansion](https://davidamitchell.github.io/Research/research/2026-03-12-failure-mode-taxonomy-expansion.html)
- [x] [Mitchell (2026) Agent evaluation framework](https://davidamitchell.github.io/Research/research/2026-03-10-agent-evaluation-cross-repo-analysis.html)
- [x] [Mitchell (2026) ServiceNow CSDM data modelling](https://davidamitchell.github.io/Research/research/2026-03-08-servicenow-csdm-data-modelling.html)
- [x] [Mitchell (2026) ServiceNow Artificial Intelligence knowledge management, Retrieval-Augmented Generation, and agent frameworks](https://davidamitchell.github.io/Research/research/2026-03-08-servicenow-ai-knowledge-rag-agents.html)
- [x] [Mitchell (2026) Integrative framework for agent decision-making](https://davidamitchell.github.io/Research/research/2026-03-02-integrative-framework-agent-decision-making.html)
- [x] [Mitchell (2026) Enterprise Artificial Intelligence capability reference architecture second-cycle update](https://davidamitchell.github.io/Research/research/2026-05-08-ai-capability-reference-architecture-second-cycle-update.html)
- [x] [Mitchell (2026) European Union Artificial Intelligence Act and AIBOM intersection](https://davidamitchell.github.io/Research/research/2026-05-06-aibom-regulatory-eu-ai-act-intersection.html)
- [x] [Mitchell (2026) Governance-as-moat implications](https://davidamitchell.github.io/Research/research/2026-04-27-governance-moat-prior-research-implications.html)

---

## Research Skill Output

### §0 Initialise

- Question: what enterprise design most practically implements a five-pillar Agentic Knowledge Management (KM) model for tool-using, semi-autonomous Artificial Intelligence systems, and where do established architecture and governance frameworks need extension?
- Scope: knowledge representation, context engineering, memory, governance and security, operations and improvement, plus mapping to The Open Group Architecture Framework (TOGAF), Common Service Data Model (CSDM), and current enterprise multi-agent reference architectures.
- Constraints: prefer standards, official architecture guidance, peer-reviewed work, and completed repository items; treat the output as a synthesis item rather than a greenfield search.
- Output: knowledge, specifically a five-pillar enterprise design, a dependency order, framework-extension guidance, and a bounded implementation sequence.
- Prior completed items reviewed before investigation: https://davidamitchell.github.io/Research/research/2026-03-03-knowledge-representation-agent-context.html ; https://davidamitchell.github.io/Research/research/2026-03-02-agent-memory-management-context-injection.html ; https://davidamitchell.github.io/Research/research/2026-03-08-context-engineering-first-principles.html ; https://davidamitchell.github.io/Research/research/2026-03-01-agent-lsp-policy-enforcement.html ; https://davidamitchell.github.io/Research/research/2026-03-12-failure-mode-taxonomy-expansion.html ; https://davidamitchell.github.io/Research/research/2026-03-10-agent-evaluation-cross-repo-analysis.html ; https://davidamitchell.github.io/Research/research/2026-03-08-servicenow-csdm-data-modelling.html ; https://davidamitchell.github.io/Research/research/2026-05-08-ai-capability-reference-architecture-second-cycle-update.html ; https://davidamitchell.github.io/Research/research/2026-05-06-aibom-regulatory-eu-ai-act-intersection.html

### §1 Question Decomposition

**Root question:** what architecture and operating model make a five-pillar Knowledge Management capability stack practical, governable, and extensible in enterprise multi-agent systems?

```
Q. Five-pillar enterprise Knowledge Management model
|
|-- Q1. Are the five pillars coherent capability layers rather than overlapping labels?
|   |-- Q1a. What belongs in knowledge foundations?
|   |-- Q1b. What belongs in context orchestration?
|   |-- Q1c. What belongs in memory and persistence?
|   |-- Q1d. What belongs in governance and security?
|   `-- Q1e. What belongs in operations and continuous improvement?
|
|-- Q2. What minimum technical pattern best implements Pillar 1?
|   |-- Q2a. What do RDF, OWL, and SKOS each contribute?
|   `-- Q2b. When is graph-plus-embedding better than either alone?
|
|-- Q3. What operating pattern best implements Pillar 2 and Pillar 3?
|   |-- Q3a. What does context engineering require beyond prompts?
|   |-- Q3b. What memory tiers are supported by current evidence?
|   `-- Q3c. What freshness and invalidation rules are required?
|
|-- Q4. What control-plane pattern best implements Pillar 4?
|   |-- Q4a. Which threats require explicit controls?
|   |-- Q4b. What does policy injection or runtime governance need?
|   `-- Q4c. What does supply-chain transparency add and what does it not solve?
|
|-- Q5. What operating-system-of-work pattern best implements Pillar 5?
|   |-- Q5a. Which roles, review loops, and metrics are required?
|   `-- Q5b. What observability and evaluation structures are supported publicly?
|
|-- Q6. How do TOGAF, CSDM, and current multi-agent reference architectures map to the five pillars?
|   |-- Q6a. Which parts already fit?
|   `-- Q6b. Which parts require explicit extension?
|
`-- Q7. What is the most practical sequencing for enterprise adoption?
    |-- Q7a. Which controls are non-negotiable before pilots?
    `-- Q7b. Which deeper capabilities can follow once value is proven?
```

### §2 Investigation

#### §2.1 Prior completed-item baseline

- [fact; source: https://davidamitchell.github.io/Research/research/2026-03-03-knowledge-representation-agent-context.html; https://davidamitchell.github.io/Research/research/2026-03-02-agent-memory-management-context-injection.html; https://davidamitchell.github.io/Research/research/2026-03-08-context-engineering-first-principles.html; https://davidamitchell.github.io/Research/research/2026-03-01-agent-lsp-policy-enforcement.html; https://davidamitchell.github.io/Research/research/2026-03-12-failure-mode-taxonomy-expansion.html; https://davidamitchell.github.io/Research/research/2026-03-10-agent-evaluation-cross-repo-analysis.html] Prior repository work already isolated six component families, knowledge representation, context engineering, memory architecture, policy enforcement, failure taxonomy, and evaluation, so the present item is a synthesis and operating-model problem rather than a search for missing components.
- [fact; source: https://davidamitchell.github.io/Research/research/2026-03-08-servicenow-csdm-data-modelling.html; https://davidamitchell.github.io/Research/research/2026-05-08-ai-capability-reference-architecture-second-cycle-update.html] Adjacent enterprise-architecture items independently show that durable enterprise maps separate taxonomy, traceability, provenance, and governance planes instead of collapsing them into one model.
- [inference; source: https://davidamitchell.github.io/Research/research/2026-03-08-servicenow-csdm-data-modelling.html; https://davidamitchell.github.io/Research/research/2026-05-08-ai-capability-reference-architecture-second-cycle-update.html; https://www.opengroup.org/togaf] The five-pillar model is coherent if each pillar is treated as a separately governable layer with explicit handoffs, not as five maturity labels attached to one platform.

#### §2.2 Pillar 1, knowledge foundations and representation

- [fact; source: https://www.w3.org/TR/rdf11-concepts/] RDF defines graph-based data as triples and datasets, including named graphs, which makes it suitable for linking statements, provenance surfaces, and multiple knowledge views inside one abstract model.
- [fact; source: https://www.w3.org/TR/owl2-overview/] OWL 2 adds formal classes, properties, individuals, semantics, and profiles for ontology development and machine reasoning over domain terms and relationships.
- [fact; source: https://www.w3.org/TR/skos-reference/] SKOS defines concept schemes, labels, notations, and documentation properties for controlled vocabularies, taxonomies, thesauri, and classification systems expressed as machine-readable data.
- [fact; source: https://arxiv.org/abs/2404.16130] The cited graph-based Retrieval-Augmented Generation approach improves comprehensiveness and diversity on global corpus questions by building an entity graph plus community summaries, then summarizing partial responses across those communities.
- [fact; source: https://davidamitchell.github.io/Research/research/2026-03-03-knowledge-representation-agent-context.html; https://davidamitchell.github.io/Research/research/2026-03-02-agent-memory-management-context-injection.html] Prior repository work concluded that embeddings, hierarchical summaries, and knowledge graphs complement rather than replace one another, and that retrieval quality remains bounded by source governance, freshness, and contradiction handling.
- [inference; source: https://www.w3.org/TR/rdf11-concepts/; https://www.w3.org/TR/owl2-overview/; https://www.w3.org/TR/skos-reference/; https://arxiv.org/abs/2404.16130; https://davidamitchell.github.io/Research/research/2026-03-03-knowledge-representation-agent-context.html] A practical enterprise Pillar 1 should start with canonical identifiers, SKOS-like vocabularies, provenance fields, and graph-plus-embedding dual storage; full OWL reasoning becomes worthwhile when cross-domain ambiguity, compliance logic, or reusable enterprise semantics justify the additional maintenance cost.

#### §2.3 Pillar 2, context engineering and orchestration

- [fact; source: https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents] Anthropic defines context engineering as curating and maintaining the optimal set of tokens during Large Language Model (LLM) inference across system instructions, tools, external data, and message history.
- [fact; source: https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents] Anthropic also states that context is a finite resource with diminishing returns because models experience context rot as token counts rise and attention must stretch across more pairwise relationships.
- [fact; source: https://davidamitchell.github.io/Research/research/2026-03-08-context-engineering-first-principles.html] Prior repository work separates token-level steering from goal-level steering and treats context loading as a layered authority problem rather than a prompt-only problem.
- [inference; source: https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents; https://davidamitchell.github.io/Research/research/2026-03-08-context-engineering-first-principles.html; https://davidamitchell.github.io/Research/research/2026-03-02-integrative-framework-agent-decision-making.html] Pillar 2 therefore requires explicit relevance filtering, progressive disclosure, and authority ordering across strategy, policy, domain knowledge, current state, and task context, instead of relying on one large composite prompt.
- [inference; source: https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents; https://davidamitchell.github.io/Research/research/2026-03-02-integrative-framework-agent-decision-making.html] Formal intent injection should bind mission, policy, strategy, and task context as separate layers so the agent can keep resident only what has stable relevance and retrieve the rest just in time.

#### §2.4 Pillar 3, memory, state, and persistence

- [fact; source: https://davidamitchell.github.io/Research/research/2026-03-02-agent-memory-management-context-injection.html] Prior memory research found that Retrieval-Augmented Generation (RAG) is retrieval, not a full memory architecture, and that effective memory needs differentiated write paths, scoping, freshness handling, and governance.
- [fact; source: https://blog.getzep.com/state-of-the-art-agent-memory/] Zep reports aggregate LongMemEval accuracy improvements of up to 18.5 percent and median latency reductions of about 90 percent versus full-context baselines, while using less than 2 percent of baseline tokens.
- [fact; source: https://microsoft.github.io/multi-agent-reference-architecture/docs/reference-architecture/Reference-Architecture.html] Microsoft's multi-agent reference architecture treats persistent storage, knowledge bases, vector databases, and orchestrator-managed context and state as first-class architectural components.
- [inference; source: https://davidamitchell.github.io/Research/research/2026-03-02-agent-memory-management-context-injection.html; https://blog.getzep.com/state-of-the-art-agent-memory/; https://microsoft.github.io/multi-agent-reference-architecture/docs/reference-architecture/Reference-Architecture.html] The practical Pillar 3 design is a tiered memory model with explicit working, episodic, semantic, and durable stores plus freshness, invalidation, provenance, and reconciliation rules; memory is not an undifferentiated larger context window.

#### §2.5 Pillar 4, governance, risk, security, and compliance

- [fact; source: https://www.nist.gov/itl/ai-risk-management-framework; https://airc.nist.gov/airmf-resources/playbook/] The National Institute of Standards and Technology (NIST) Artificial Intelligence Risk Management Framework organizes work across Govern, Map, Measure, and Manage, and the Playbook turns those functions into concrete voluntary actions.
- [fact; source: https://genai.owasp.org/llmrisk/llm01-prompt-injection/; https://genai.owasp.org/llmrisk/llm022025-sensitive-information-disclosure/; https://genai.owasp.org/llmrisk/llm052025-improper-output-handling/] The Open Worldwide Application Security Project (OWASP) current LLM risk set treats prompt injection, sensitive information disclosure, and improper output handling as separate control problems in application design and operation.
- [fact; source: https://cyclonedx.org/capabilities/mlbom/] CycloneDX's Machine Learning Bill of Materials extends inventory to datasets, models, configurations, provenance, and ethical considerations, broadening AI supply-chain documentation beyond package inventories.
- [fact; source: https://davidamitchell.github.io/Research/research/2026-05-06-aibom-regulatory-eu-ai-act-intersection.html; https://davidamitchell.github.io/Research/research/2026-05-08-ai-capability-reference-architecture-second-cycle-update.html] Prior repository research on AIBOM and enterprise architecture found that declared inventory and runtime evidence reduce structural drift and replay gaps, but they do not replace runtime enforcement, testing, or adversarial control layers.
- [inference; source: https://www.nist.gov/itl/ai-risk-management-framework; https://genai.owasp.org/llmrisk/llm01-prompt-injection/; https://cyclonedx.org/capabilities/mlbom/; https://davidamitchell.github.io/Research/research/2026-05-06-aibom-regulatory-eu-ai-act-intersection.html] Pillar 4 therefore needs agent identity, delegated authority, policy injection, runtime evidence, and supply-chain transparency as an explicit control plane kept separate from the knowledge and orchestration layers it governs.

#### §2.6 Pillar 5, operations, enablement, and continuous improvement

- [fact; source: https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-enterprise-ready-gen-ai-platform/best-practices.html] AWS enterprise guidance recommends an AI Center of Excellence (AI CoE), a model-governance committee, reusable pattern libraries, technical and business dashboards, layered security controls, and gradual scaling from bounded use cases.
- [fact; source: https://docs.cloud.google.com/architecture/multiagent-ai-system] Google Cloud's multi-agent reference architecture includes a coordinator agent, iterative refinement loops, Model Armor for input and output inspection, Model Context Protocol (MCP) tool access, and an explicit human-in-the-loop path.
- [fact; source: https://microsoft.github.io/multi-agent-reference-architecture/docs/governance/Governance.html; https://microsoft.github.io/multi-agent-reference-architecture/docs/observability/Observability.html; https://microsoft.github.io/multi-agent-reference-architecture/docs/evaluation/Evaluation.html] Microsoft separates governance, observability, and evaluation into distinct practices and states that multi-agent evaluation must handle path optimization, error propagation, emergent behavior, and offline and online loops.
- [fact; source: https://davidamitchell.github.io/Research/research/2026-03-10-agent-evaluation-cross-repo-analysis.html] Prior repository evaluation research found that regression detection requires explicit rubrics, trace capture, and feedback loops rather than simple outcome logging.
- [inference; source: https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-enterprise-ready-gen-ai-platform/best-practices.html; https://docs.cloud.google.com/architecture/multiagent-ai-system; https://microsoft.github.io/multi-agent-reference-architecture/docs/evaluation/Evaluation.html; https://davidamitchell.github.io/Research/research/2026-03-10-agent-evaluation-cross-repo-analysis.html] Pillar 5 is an operating system of work with named owners, curation cycles, evaluation cadences, observability surfaces, and value metrics, not a post hoc support function.

#### §2.7 Framework mapping, TOGAF, CSDM, and current multi-agent architectures

- [fact; source: https://www.opengroup.org/togaf] TOGAF presents an enterprise architecture methodology and framework with fundamental content, series guides, and a central Architecture Development Method that supports governance and change across enterprise architecture work.
- [fact; source: https://davidamitchell.github.io/Research/research/2026-03-08-servicenow-csdm-data-modelling.html] The completed CSDM item found that CSDM is strong at ownership and configuration traceability and that CSDM 5 broadens service modelling through Service Instance and product-lifecycle domains.
- [inference; source: https://www.opengroup.org/togaf; https://davidamitchell.github.io/Research/research/2026-05-08-ai-capability-reference-architecture-second-cycle-update.html] TOGAF can host the five pillars only if Data Architecture explicitly covers ontologies, taxonomies, provenance, and corpus versioning; Application Architecture explicitly covers context and memory services; and governance and change layers explicitly cover agent identity, policy injection, runtime evidence, and evaluation.
- [inference; source: https://davidamitchell.github.io/Research/research/2026-03-08-servicenow-csdm-data-modelling.html; https://davidamitchell.github.io/Research/research/2026-05-06-aibom-regulatory-eu-ai-act-intersection.html] CSDM-like models need extensions for knowledge assets, retrieval corpora, prompts or policies, memory stores, agent identities, and runtime evidence links, because service and configuration objects alone do not capture AI knowledge-state lineage.
- [inference; source: https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-enterprise-ready-gen-ai-platform/best-practices.html; https://docs.cloud.google.com/architecture/multiagent-ai-system; https://microsoft.github.io/multi-agent-reference-architecture/docs/reference-architecture/Reference-Architecture.html] Current enterprise AI reference architectures already supply orchestrators, knowledge layers, persistent storage, observability, and human review paths, but they under-specify ontology governance, freshness and invalidation policy, and durable memory authority boundaries.

#### §2.8 Case evidence and sequencing

- [fact; source: https://arxiv.org/abs/2404.16130; https://blog.getzep.com/state-of-the-art-agent-memory/] GraphRAG shows that graph and summary layers outperform vector-only retrieval on global corpus questions, and Zep shows that structured temporal memory outperforms full-context replay on long-horizon memory benchmarks.
- [fact; source: https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-enterprise-ready-gen-ai-platform/best-practices.html; https://docs.cloud.google.com/architecture/multiagent-ai-system; https://microsoft.github.io/multi-agent-reference-architecture/docs/evaluation/Evaluation.html] AWS, Google, and Microsoft all recommend bounded deployments, explicit evaluation, human intervention paths, and gradual scale-up instead of unconstrained autonomy as a starting point.
- [inference; source: https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-enterprise-ready-gen-ai-platform/best-practices.html; https://docs.cloud.google.com/architecture/multiagent-ai-system; https://microsoft.github.io/multi-agent-reference-architecture/docs/reference-architecture/Reference-Architecture.html; https://davidamitchell.github.io/Research/research/2026-03-02-agent-memory-management-context-injection.html; https://davidamitchell.github.io/Research/research/2026-03-03-knowledge-representation-agent-context.html] The most practical implementation sequence is to establish minimum Pillar 4 and Pillar 5 controls for one bounded use case, create a light Pillar 1 canonical vocabulary and provenance model, deploy Pillar 2 context selection and Pillar 3 tiered memory for that use case, and deepen ontology or graph reasoning only where cross-domain ambiguity or reuse justifies the cost.
- [inference; source: https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-enterprise-ready-gen-ai-platform/best-practices.html; https://www.nist.gov/itl/ai-risk-management-framework; https://genai.owasp.org/llmrisk/llm01-prompt-injection/; https://microsoft.github.io/multi-agent-reference-architecture/docs/governance/Governance.html] Full five-pillar maturity is a portfolio roadmap rather than a prerequisite for every pilot, but governed identity, source authority, evaluation, and human stop rights are non-negotiable before any side-effecting deployment.

### §3 Reasoning

- [fact; source: https://www.w3.org/TR/rdf11-concepts/; https://www.w3.org/TR/owl2-overview/; https://www.w3.org/TR/skos-reference/] Pillar 1 has a clear standards basis, because RDF, OWL, and SKOS define complementary roles for linked data, ontology semantics, and controlled vocabularies.
- [fact; source: https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents; https://blog.getzep.com/state-of-the-art-agent-memory/] Pillar 2 and Pillar 3 are supported by direct evidence that large context windows degrade and that structured context and memory layers can outperform full transcript replay.
- [fact; source: https://www.nist.gov/itl/ai-risk-management-framework; https://genai.owasp.org/llmrisk/llm01-prompt-injection/; https://cyclonedx.org/capabilities/mlbom/] Pillar 4 is not optional, because governance, threat control, and inventory transparency are treated as distinct responsibilities by risk and security sources.
- [fact; source: https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-enterprise-ready-gen-ai-platform/best-practices.html; https://microsoft.github.io/multi-agent-reference-architecture/docs/evaluation/Evaluation.html] Pillar 5 has direct operating-model support from enterprise guidance that separates governance, evaluation, and continuous monitoring.
- [inference; source: https://www.opengroup.org/togaf; https://davidamitchell.github.io/Research/research/2026-03-08-servicenow-csdm-data-modelling.html; https://davidamitchell.github.io/Research/research/2026-05-08-ai-capability-reference-architecture-second-cycle-update.html] The five pillars are best treated as a layered enterprise stack because existing frameworks already separate architecture, traceability, governance, and change, but do not yet encode AI knowledge state and memory authority explicitly enough.
- [assumption; source: https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-enterprise-ready-gen-ai-platform/best-practices.html; https://www.opengroup.org/togaf] Enterprises can adopt a light canonical vocabulary and provenance model before they can justify a full ontology program, because phased architecture practice is common in enterprise transformation even when the long-run target is more formal. Justification: direct public evidence for complete five-pillar rollouts remains thinner than evidence for phased platform adoption.

### §4 Consistency Check

- [fact; source: https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents; https://blog.getzep.com/state-of-the-art-agent-memory/] Tension checked: bigger context versus stronger memory. Resolution: both sources support tiered curation over naive context expansion.
- [fact; source: https://cyclonedx.org/capabilities/mlbom/; https://davidamitchell.github.io/Research/research/2026-05-06-aibom-regulatory-eu-ai-act-intersection.html] Tension checked: inventory versus safety. Resolution: inventory improves transparency and replay, but does not substitute for runtime controls or adversarial testing.
- [inference; source: https://www.opengroup.org/togaf; https://davidamitchell.github.io/Research/research/2026-03-08-servicenow-csdm-data-modelling.html] Tension checked: reuse existing enterprise frameworks versus create a new framework. Resolution: the evidence favors extending TOGAF and CSDM-like structures rather than replacing them.
- [inference; source: https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-enterprise-ready-gen-ai-platform/best-practices.html; https://docs.cloud.google.com/architecture/multiagent-ai-system; https://microsoft.github.io/multi-agent-reference-architecture/docs/governance/Governance.html] Tension checked: pilot quickly versus design fully. Resolution: a bounded pilot can proceed only when minimum governance and evaluation controls are established first.

### §5 Depth and Breadth Expansion

- [inference; source: https://www.opengroup.org/togaf; https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-enterprise-ready-gen-ai-platform/best-practices.html] Technical lens: the architecture is strongest when the five pillars are implemented as composable services rather than as one repository or one orchestration product.
- [inference; source: https://www.nist.gov/itl/ai-risk-management-framework; https://davidamitchell.github.io/Research/research/2026-05-06-aibom-regulatory-eu-ai-act-intersection.html] Regulatory lens: the major extension need is not another abstract policy framework, but retained evidence that links governed design, runtime behavior, and deployer accountability.
- [inference; source: https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-enterprise-ready-gen-ai-platform/best-practices.html; https://blog.getzep.com/state-of-the-art-agent-memory/] Economic lens: the most defensible early investment is in controls, vocabulary, and bounded retrieval or memory loops, because those produce faster feedback than a large ontology-first program.
- [inference; source: https://davidamitchell.github.io/Research/research/2026-03-10-agent-evaluation-cross-repo-analysis.html; https://microsoft.github.io/multi-agent-reference-architecture/docs/evaluation/Evaluation.html] Behavioural lens: named ownership, evaluation loops, and trace visibility matter because multi-agent systems otherwise hide inefficient paths and error propagation behind superficially correct outcomes.

### §6 Synthesis

**Executive summary:**

The most practical enterprise design is a five-pillar stack that treats knowledge representation, context selection, memory, governance, and operating discipline as separate but composable services around a governed knowledge spine. [inference; source: https://www.w3.org/TR/rdf11-concepts/; https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents; https://blog.getzep.com/state-of-the-art-agent-memory/; https://www.nist.gov/itl/ai-risk-management-framework; https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-enterprise-ready-gen-ai-platform/best-practices.html]

In practice, the stack should not start with a full ontology program; it should start with bounded governance, a light canonical vocabulary and provenance model, and a tiered context-and-memory loop, then deepen graph and ontology formality where cross-domain ambiguity or reuse justifies the extra cost. [inference; source: https://www.opengroup.org/togaf; https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-enterprise-ready-gen-ai-platform/best-practices.html; https://davidamitchell.github.io/Research/research/2026-03-03-knowledge-representation-agent-context.html]

Existing frameworks remain useful only with explicit extensions: TOGAF needs AI knowledge, memory, and runtime-evidence deliverables; CSDM-like models need knowledge-asset, agent-identity, and evidence-link objects; current multi-agent reference architectures need stronger freshness, invalidation, and authority-boundary rules. [inference; source: https://www.opengroup.org/togaf; https://davidamitchell.github.io/Research/research/2026-03-08-servicenow-csdm-data-modelling.html; https://microsoft.github.io/multi-agent-reference-architecture/docs/reference-architecture/Reference-Architecture.html]

The strongest public evidence remains component-level rather than full-stack enterprise case evidence, so confidence is higher in the architecture shape and sequencing than in any single end-to-end packaged implementation pattern. [inference; source: https://arxiv.org/abs/2404.16130; https://blog.getzep.com/state-of-the-art-agent-memory/; https://docs.cloud.google.com/architecture/multiagent-ai-system]

**Key findings:**

1. A practical five-pillar Knowledge Management capability model should separate knowledge foundations, context orchestration, memory, governance, and operations into distinct services with explicit interfaces, because current standards and enterprise architectures already divide data semantics, runtime behavior, control, and lifecycle evidence across different layers. ([inference]; medium confidence; source: https://www.w3.org/TR/rdf11-concepts/; https://www.w3.org/TR/owl2-overview/; https://www.w3.org/TR/skos-reference/; https://www.opengroup.org/togaf; https://davidamitchell.github.io/Research/research/2026-05-08-ai-capability-reference-architecture-second-cycle-update.html)
2. Pillar 1 is most practical when it starts with canonical identifiers, controlled vocabularies, provenance, and graph-plus-embedding storage, because RDF, OWL, and SKOS provide complementary semantics while GraphRAG and prior repository research show that graph and summary layers add value without displacing embeddings. ([inference]; medium confidence; source: https://www.w3.org/TR/rdf11-concepts/; https://www.w3.org/TR/owl2-overview/; https://www.w3.org/TR/skos-reference/; https://arxiv.org/abs/2404.16130; https://davidamitchell.github.io/Research/research/2026-03-03-knowledge-representation-agent-context.html)
3. Pillar 2 should treat tokens as scarce, authority-ordered context rather than as a large undifferentiated prompt, because context engineering evidence shows diminishing returns at long context lengths and prior repository work shows that goal-level steering depends on layer ordering as much as prompt wording. ([inference]; medium confidence; source: https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents; https://davidamitchell.github.io/Research/research/2026-03-08-context-engineering-first-principles.html)
4. Pillar 3 should use a tiered memory model with explicit freshness, invalidation, provenance, and reconciliation rules, because public benchmark evidence shows structured temporal memory can materially improve long-horizon recall and latency relative to full-context replay. ([inference]; medium confidence; source: https://blog.getzep.com/state-of-the-art-agent-memory/; https://davidamitchell.github.io/Research/research/2026-03-02-agent-memory-management-context-injection.html; https://microsoft.github.io/multi-agent-reference-architecture/docs/reference-architecture/Reference-Architecture.html)
5. Pillar 4 has to function as an explicit control plane for identity, delegated authority, policy injection, runtime evidence, and supply-chain transparency, because risk-management, security, and AIBOM sources all describe these as separate responsibilities that inventory alone cannot satisfy. ([inference]; medium confidence; source: https://www.nist.gov/itl/ai-risk-management-framework; https://genai.owasp.org/llmrisk/llm01-prompt-injection/; https://cyclonedx.org/capabilities/mlbom/; https://davidamitchell.github.io/Research/research/2026-05-06-aibom-regulatory-eu-ai-act-intersection.html)
6. Pillar 5 should be treated as a first-class operating model rather than a support layer, because enterprise guidance consistently pairs multi-agent deployment with an Artificial Intelligence Center of Excellence, governance committee, reusable patterns, observability, evaluation loops, and explicit human intervention paths. ([inference]; medium confidence; source: https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-enterprise-ready-gen-ai-platform/best-practices.html; https://docs.cloud.google.com/architecture/multiagent-ai-system; https://microsoft.github.io/multi-agent-reference-architecture/docs/governance/Governance.html; https://microsoft.github.io/multi-agent-reference-architecture/docs/evaluation/Evaluation.html)
7. TOGAF, CSDM, and current enterprise multi-agent reference architectures are extendable but incomplete for this model, because they provide useful structure for governance, traceability, orchestration, and change but still under-specify knowledge-state lineage, memory authority boundaries, and runtime evidence links. ([inference]; medium confidence; source: https://www.opengroup.org/togaf; https://davidamitchell.github.io/Research/research/2026-03-08-servicenow-csdm-data-modelling.html; https://microsoft.github.io/multi-agent-reference-architecture/docs/reference-architecture/Reference-Architecture.html)
8. The most practical adoption sequence is to start with Pillar 4 and Pillar 5 minimum controls, add a light Pillar 1 vocabulary and provenance model, then deploy bounded Pillar 2 and Pillar 3 loops before investing in deeper ontology and graph formalization. ([inference]; medium confidence; source: https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-enterprise-ready-gen-ai-platform/best-practices.html; https://docs.cloud.google.com/architecture/multiagent-ai-system; https://davidamitchell.github.io/Research/research/2026-03-03-knowledge-representation-agent-context.html; https://davidamitchell.github.io/Research/research/2026-03-02-agent-memory-management-context-injection.html)

**Evidence map:**

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [inference] Separate services for knowledge, context, memory, control, and operations are more durable than one monolithic layer. | https://www.w3.org/TR/rdf11-concepts/ ; https://www.w3.org/TR/owl2-overview/ ; https://www.w3.org/TR/skos-reference/ ; https://www.opengroup.org/togaf ; https://davidamitchell.github.io/Research/research/2026-05-08-ai-capability-reference-architecture-second-cycle-update.html | medium | layered composition |
| [inference] Pillar 1 should begin with identifiers, vocabularies, provenance, and graph-plus-embedding storage. | https://www.w3.org/TR/rdf11-concepts/ ; https://www.w3.org/TR/owl2-overview/ ; https://www.w3.org/TR/skos-reference/ ; https://arxiv.org/abs/2404.16130 ; https://davidamitchell.github.io/Research/research/2026-03-03-knowledge-representation-agent-context.html | medium | light-to-heavy semantics |
| [inference] Context should be curated and authority-ordered because longer context windows degrade practical signal and ordering affects goal-level steering. | https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents ; https://davidamitchell.github.io/Research/research/2026-03-08-context-engineering-first-principles.html | medium | context scarcity |
| [inference] Tiered memory with freshness and provenance is the safer enterprise pattern than naive replay because structured temporal memory improves long-memory tasks while governance still requires explicit invalidation rules. | https://blog.getzep.com/state-of-the-art-agent-memory/ ; https://davidamitchell.github.io/Research/research/2026-03-02-agent-memory-management-context-injection.html ; https://microsoft.github.io/multi-agent-reference-architecture/docs/reference-architecture/Reference-Architecture.html | medium | long-memory benchmark |
| [inference] Governance must be an explicit control plane, not an attached checklist. | https://www.nist.gov/itl/ai-risk-management-framework ; https://genai.owasp.org/llmrisk/llm01-prompt-injection/ ; https://cyclonedx.org/capabilities/mlbom/ ; https://davidamitchell.github.io/Research/research/2026-05-06-aibom-regulatory-eu-ai-act-intersection.html | medium | control-boundary claim |
| [inference] Operations should be treated as a first-class operating model because enterprise guidance pairs deployment with named governance, observability, evaluation, and human intervention loops. | https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-enterprise-ready-gen-ai-platform/best-practices.html ; https://docs.cloud.google.com/architecture/multiagent-ai-system ; https://microsoft.github.io/multi-agent-reference-architecture/docs/governance/Governance.html ; https://microsoft.github.io/multi-agent-reference-architecture/docs/evaluation/Evaluation.html | medium | operating model |
| [inference] TOGAF, CSDM, and current reference architectures need explicit AI knowledge-state and runtime-evidence extensions. | https://www.opengroup.org/togaf ; https://davidamitchell.github.io/Research/research/2026-03-08-servicenow-csdm-data-modelling.html ; https://microsoft.github.io/multi-agent-reference-architecture/docs/reference-architecture/Reference-Architecture.html | medium | framework extension |
| [inference] The lowest-risk adoption path is controls first, bounded knowledge and memory second, deeper semantics third. | https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-enterprise-ready-gen-ai-platform/best-practices.html ; https://docs.cloud.google.com/architecture/multiagent-ai-system ; https://davidamitchell.github.io/Research/research/2026-03-03-knowledge-representation-agent-context.html ; https://davidamitchell.github.io/Research/research/2026-03-02-agent-memory-management-context-injection.html | medium | sequencing |

**Assumptions:**

- [assumption; source: https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-enterprise-ready-gen-ai-platform/best-practices.html; https://www.opengroup.org/togaf] Most enterprises can establish a light canonical vocabulary and provenance layer before they can justify a full ontology program. Justification: phased architecture and bounded pilots are the dominant enterprise adoption pattern in public guidance.
- [assumption; source: https://davidamitchell.github.io/Research/research/2026-03-08-servicenow-csdm-data-modelling.html; https://www.opengroup.org/togaf] Existing enterprise frameworks are easier to extend than to replace for this use case. Justification: public evidence is much richer on extension patterns than on wholesale framework replacement.

**Analysis:**

The evidence converges on one design rule: the five pillars are governable control surfaces whose interfaces need to stay visible across knowledge, context, state, control, and operations. [inference; source: https://www.opengroup.org/togaf; https://microsoft.github.io/multi-agent-reference-architecture/docs/reference-architecture/Reference-Architecture.html]

Public sources repeatedly separate semantics, context selection, state, control, and operations rather than collapsing them into one layer, which is why a knowledge-graph-only or prompt-only solution looks structurally incomplete. [inference; source: https://www.w3.org/TR/skos-reference/; https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents; https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-enterprise-ready-gen-ai-platform/best-practices.html]

Public enterprise guidance rewards bounded use cases, and the best measurable gains in the evidence base come from context and memory improvements layered on top of already-governed sources, which makes an ontology-first program a higher-risk starting point. [inference; source: https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-enterprise-ready-gen-ai-platform/best-practices.html; https://blog.getzep.com/state-of-the-art-agent-memory/]

Inventory, runtime evidence, and enforcement appear as complementary controls rather than substitutes across the governance sources, so the model stays practical only when Pillar 4 remains a distinct control plane with authority over the other pillars. [inference; source: https://cyclonedx.org/capabilities/mlbom/; https://davidamitchell.github.io/Research/research/2026-05-06-aibom-regulatory-eu-ai-act-intersection.html; https://genai.owasp.org/llmrisk/llm01-prompt-injection/]

**Risks, gaps, uncertainties:**

- End-to-end public case evidence for a complete five-pillar stack remains thinner than component-level evidence for GraphRAG, structured memory, and enterprise governance patterns. [inference; source: https://arxiv.org/abs/2404.16130; https://blog.getzep.com/state-of-the-art-agent-memory/; https://docs.cloud.google.com/architecture/multiagent-ai-system]
- The maintenance cost of enterprise ontology lifecycle management, especially entity resolution and conflict remediation across domains, is still weakly quantified in public case studies. [inference; source: https://www.w3.org/TR/owl2-overview/; https://davidamitchell.github.io/Research/research/2026-03-03-knowledge-representation-agent-context.html]
- Public reference architectures provide stronger evidence for control and orchestration components than for durable cross-session knowledge-authority boundaries, so some memory-governance design remains inferential. [inference; source: https://microsoft.github.io/multi-agent-reference-architecture/docs/reference-architecture/Reference-Architecture.html; https://docs.cloud.google.com/architecture/multiagent-ai-system]

**Open questions:**

- What minimum ontology or vocabulary maturity is enough before an enterprise should move from document-centric retrieval to graph-centric retrieval for a given domain?
- Which runtime metrics best demonstrate that a memory invalidation policy is catching stale or superseded knowledge before it reaches consequential decisions?
- What CSDM-compatible object model best represents prompts, retrieval corpora, agent identities, and runtime evidence without turning the traceability layer into a second architecture repository?

### §7 Recursive Review

review_result: pass
acronym_audit: passed
claim_label_audit: passed
source_url_audit: passed
synthesis_findings_parity: aligned
remaining_uncertainty: component-level evidence is stronger than full-stack public case evidence

---

## Findings

### Executive Summary

The most practical enterprise design is a five-pillar stack that treats knowledge representation, context selection, memory, governance, and operating discipline as separate but composable services around a governed knowledge spine. [inference; source: https://www.w3.org/TR/rdf11-concepts/; https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents; https://blog.getzep.com/state-of-the-art-agent-memory/; https://www.nist.gov/itl/ai-risk-management-framework; https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-enterprise-ready-gen-ai-platform/best-practices.html]

In practice, the stack should not start with a full ontology program; it should start with bounded governance, a light canonical vocabulary and provenance model, and a tiered context-and-memory loop, then deepen graph and ontology formality where cross-domain ambiguity or reuse justifies the extra cost. [inference; source: https://www.opengroup.org/togaf; https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-enterprise-ready-gen-ai-platform/best-practices.html; https://davidamitchell.github.io/Research/research/2026-03-03-knowledge-representation-agent-context.html]

Existing frameworks remain useful only with explicit extensions: TOGAF needs AI knowledge, memory, and runtime-evidence deliverables; CSDM-like models need knowledge-asset, agent-identity, and evidence-link objects; current multi-agent reference architectures need stronger freshness, invalidation, and authority-boundary rules. [inference; source: https://www.opengroup.org/togaf; https://davidamitchell.github.io/Research/research/2026-03-08-servicenow-csdm-data-modelling.html; https://microsoft.github.io/multi-agent-reference-architecture/docs/reference-architecture/Reference-Architecture.html]

The strongest public evidence remains component-level rather than full-stack enterprise case evidence, so confidence is higher in the architecture shape and sequencing than in any single end-to-end packaged implementation pattern. [inference; source: https://arxiv.org/abs/2404.16130; https://blog.getzep.com/state-of-the-art-agent-memory/; https://docs.cloud.google.com/architecture/multiagent-ai-system]

### Key Findings

1. **A practical five-pillar Knowledge Management capability model should separate knowledge foundations, context orchestration, memory, governance, and operations into distinct services with explicit interfaces, because current standards and enterprise architectures already divide data semantics, runtime behavior, control, and lifecycle evidence across different layers.** ([inference]; medium confidence; source: https://www.w3.org/TR/rdf11-concepts/; https://www.w3.org/TR/owl2-overview/; https://www.w3.org/TR/skos-reference/; https://www.opengroup.org/togaf; https://davidamitchell.github.io/Research/research/2026-05-08-ai-capability-reference-architecture-second-cycle-update.html)
2. **Pillar 1 is most practical when it starts with canonical identifiers, controlled vocabularies, provenance, and graph-plus-embedding storage, because RDF, OWL, and SKOS provide complementary semantics while GraphRAG and prior repository research show that graph and summary layers add value without displacing embeddings.** ([inference]; medium confidence; source: https://www.w3.org/TR/rdf11-concepts/; https://www.w3.org/TR/owl2-overview/; https://www.w3.org/TR/skos-reference/; https://arxiv.org/abs/2404.16130; https://davidamitchell.github.io/Research/research/2026-03-03-knowledge-representation-agent-context.html)
3. **Pillar 2 should treat tokens as scarce, authority-ordered context rather than as a large undifferentiated prompt, because context engineering evidence shows diminishing returns at long context lengths and prior repository work shows that goal-level steering depends on layer ordering as much as prompt wording.** ([inference]; medium confidence; source: https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents; https://davidamitchell.github.io/Research/research/2026-03-08-context-engineering-first-principles.html)
4. **Pillar 3 should use a tiered memory model with explicit freshness, invalidation, provenance, and reconciliation rules, because public benchmark evidence shows structured temporal memory can materially improve long-horizon recall and latency relative to full-context replay.** ([inference]; medium confidence; source: https://blog.getzep.com/state-of-the-art-agent-memory/; https://davidamitchell.github.io/Research/research/2026-03-02-agent-memory-management-context-injection.html; https://microsoft.github.io/multi-agent-reference-architecture/docs/reference-architecture/Reference-Architecture.html)
5. **Pillar 4 has to function as an explicit control plane for identity, delegated authority, policy injection, runtime evidence, and supply-chain transparency, because risk-management, security, and AIBOM sources all describe these as separate responsibilities that inventory alone cannot satisfy.** ([inference]; medium confidence; source: https://www.nist.gov/itl/ai-risk-management-framework; https://genai.owasp.org/llmrisk/llm01-prompt-injection/; https://cyclonedx.org/capabilities/mlbom/; https://davidamitchell.github.io/Research/research/2026-05-06-aibom-regulatory-eu-ai-act-intersection.html)
6. **Pillar 5 should be treated as a first-class operating model rather than a support layer, because enterprise guidance consistently pairs multi-agent deployment with an Artificial Intelligence Center of Excellence, governance committee, reusable patterns, observability, evaluation loops, and explicit human intervention paths.** ([inference]; medium confidence; source: https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-enterprise-ready-gen-ai-platform/best-practices.html; https://docs.cloud.google.com/architecture/multiagent-ai-system; https://microsoft.github.io/multi-agent-reference-architecture/docs/governance/Governance.html; https://microsoft.github.io/multi-agent-reference-architecture/docs/evaluation/Evaluation.html)
7. **TOGAF, CSDM, and current enterprise multi-agent reference architectures are extendable but incomplete for this model, because they provide useful structure for governance, traceability, orchestration, and change but still under-specify knowledge-state lineage, memory authority boundaries, and runtime evidence links.** ([inference]; medium confidence; source: https://www.opengroup.org/togaf; https://davidamitchell.github.io/Research/research/2026-03-08-servicenow-csdm-data-modelling.html; https://microsoft.github.io/multi-agent-reference-architecture/docs/reference-architecture/Reference-Architecture.html)
8. **The most practical adoption sequence is to start with Pillar 4 and Pillar 5 minimum controls, add a light Pillar 1 vocabulary and provenance model, then deploy bounded Pillar 2 and Pillar 3 loops before investing in deeper ontology and graph formalization.** ([inference]; medium confidence; source: https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-enterprise-ready-gen-ai-platform/best-practices.html; https://docs.cloud.google.com/architecture/multiagent-ai-system; https://davidamitchell.github.io/Research/research/2026-03-03-knowledge-representation-agent-context.html; https://davidamitchell.github.io/Research/research/2026-03-02-agent-memory-management-context-injection.html)

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [inference] Separate services for knowledge, context, memory, control, and operations are more durable than one monolithic layer. | https://www.w3.org/TR/rdf11-concepts/ ; https://www.w3.org/TR/owl2-overview/ ; https://www.w3.org/TR/skos-reference/ ; https://www.opengroup.org/togaf ; https://davidamitchell.github.io/Research/research/2026-05-08-ai-capability-reference-architecture-second-cycle-update.html | medium | layered composition |
| [inference] Pillar 1 should begin with identifiers, vocabularies, provenance, and graph-plus-embedding storage. | https://www.w3.org/TR/rdf11-concepts/ ; https://www.w3.org/TR/owl2-overview/ ; https://www.w3.org/TR/skos-reference/ ; https://arxiv.org/abs/2404.16130 ; https://davidamitchell.github.io/Research/research/2026-03-03-knowledge-representation-agent-context.html | medium | light-to-heavy semantics |
| [inference] Context should be curated and authority-ordered because longer context windows degrade practical signal and ordering affects goal-level steering. | https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents ; https://davidamitchell.github.io/Research/research/2026-03-08-context-engineering-first-principles.html | medium | context scarcity |
| [inference] Tiered memory with freshness and provenance is the safer enterprise pattern than naive replay because structured temporal memory improves long-memory tasks while governance still requires explicit invalidation rules. | https://blog.getzep.com/state-of-the-art-agent-memory/ ; https://davidamitchell.github.io/Research/research/2026-03-02-agent-memory-management-context-injection.html ; https://microsoft.github.io/multi-agent-reference-architecture/docs/reference-architecture/Reference-Architecture.html | medium | benchmark support |
| [inference] Governance must be an explicit control plane, not an attached checklist. | https://www.nist.gov/itl/ai-risk-management-framework ; https://genai.owasp.org/llmrisk/llm01-prompt-injection/ ; https://cyclonedx.org/capabilities/mlbom/ ; https://davidamitchell.github.io/Research/research/2026-05-06-aibom-regulatory-eu-ai-act-intersection.html | medium | control boundary |
| [inference] Operations should be treated as a first-class operating model because enterprise guidance pairs deployment with named governance, observability, evaluation, and human intervention loops. | https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-enterprise-ready-gen-ai-platform/best-practices.html ; https://docs.cloud.google.com/architecture/multiagent-ai-system ; https://microsoft.github.io/multi-agent-reference-architecture/docs/governance/Governance.html ; https://microsoft.github.io/multi-agent-reference-architecture/docs/evaluation/Evaluation.html | medium | operating model |
| [inference] TOGAF, CSDM, and current reference architectures need explicit AI knowledge-state and runtime-evidence extensions. | https://www.opengroup.org/togaf ; https://davidamitchell.github.io/Research/research/2026-03-08-servicenow-csdm-data-modelling.html ; https://microsoft.github.io/multi-agent-reference-architecture/docs/reference-architecture/Reference-Architecture.html | medium | framework extension |
| [inference] The lowest-risk adoption path is controls first, bounded knowledge and memory second, deeper semantics third. | https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-enterprise-ready-gen-ai-platform/best-practices.html ; https://docs.cloud.google.com/architecture/multiagent-ai-system ; https://davidamitchell.github.io/Research/research/2026-03-03-knowledge-representation-agent-context.html ; https://davidamitchell.github.io/Research/research/2026-03-02-agent-memory-management-context-injection.html | medium | sequencing |

### Assumptions

- **Assumption:** Most enterprises can establish a light canonical vocabulary and provenance layer before they can justify a full ontology program. **Justification:** Public enterprise guidance favors bounded pilots and phased architecture maturity rather than up-front enterprise-wide formalization. [assumption; source: https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-enterprise-ready-gen-ai-platform/best-practices.html; https://www.opengroup.org/togaf]
- **Assumption:** Existing enterprise frameworks are easier to extend than to replace for this use case. **Justification:** The public evidence base is much richer on extension patterns than on wholesale framework replacement. [assumption; source: https://davidamitchell.github.io/Research/research/2026-03-08-servicenow-csdm-data-modelling.html; https://www.opengroup.org/togaf]

### Analysis

The evidence converges on one design rule: the five pillars are governable control surfaces whose interfaces need to stay visible across knowledge, context, state, control, and operations. [inference; source: https://www.opengroup.org/togaf; https://microsoft.github.io/multi-agent-reference-architecture/docs/reference-architecture/Reference-Architecture.html]

Public sources repeatedly separate semantics, context selection, state, control, and operations rather than collapsing them into one layer, which is why a knowledge-graph-only or prompt-only solution looks structurally incomplete. [inference; source: https://www.w3.org/TR/skos-reference/; https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents; https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-enterprise-ready-gen-ai-platform/best-practices.html]

Public enterprise guidance rewards bounded use cases, and the best measurable gains in the evidence base come from context and memory improvements layered on top of already-governed sources, which makes an ontology-first program a higher-risk starting point. [inference; source: https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-enterprise-ready-gen-ai-platform/best-practices.html; https://blog.getzep.com/state-of-the-art-agent-memory/]

Inventory, runtime evidence, and enforcement appear as complementary controls rather than substitutes across the governance sources, so the model stays practical only when Pillar 4 remains a distinct control plane with authority over the other pillars. [inference; source: https://cyclonedx.org/capabilities/mlbom/; https://davidamitchell.github.io/Research/research/2026-05-06-aibom-regulatory-eu-ai-act-intersection.html; https://genai.owasp.org/llmrisk/llm01-prompt-injection/]

### Risks, Gaps, and Uncertainties

- End-to-end public case evidence for a complete five-pillar stack remains thinner than component-level evidence for GraphRAG, structured memory, and enterprise governance patterns. [inference; source: https://arxiv.org/abs/2404.16130; https://blog.getzep.com/state-of-the-art-agent-memory/; https://docs.cloud.google.com/architecture/multiagent-ai-system]
- The maintenance cost of enterprise ontology lifecycle management, especially entity resolution and conflict remediation across domains, is still weakly quantified in public case studies. [inference; source: https://www.w3.org/TR/owl2-overview/; https://davidamitchell.github.io/Research/research/2026-03-03-knowledge-representation-agent-context.html]
- Public reference architectures provide stronger evidence for control and orchestration components than for durable cross-session knowledge-authority boundaries, so some memory-governance design remains inferential. [inference; source: https://microsoft.github.io/multi-agent-reference-architecture/docs/reference-architecture/Reference-Architecture.html; https://docs.cloud.google.com/architecture/multiagent-ai-system]

### Open Questions

- What minimum ontology or vocabulary maturity is enough before an enterprise should move from document-centric retrieval to graph-centric retrieval for a given domain?
- Which runtime metrics best demonstrate that a memory invalidation policy is catching stale or superseded knowledge before it reaches consequential decisions?
- What CSDM-compatible object model best represents prompts, retrieval corpora, agent identities, and runtime evidence without turning the traceability layer into a second architecture repository?

---

## Output

- Type: knowledge
- Description: Synthesises enterprise design and sequencing guidance for a five-pillar Knowledge Management capability model, plus explicit extension points for TOGAF, CSDM, and current multi-agent reference architectures. [inference; source: https://www.opengroup.org/togaf; https://davidamitchell.github.io/Research/research/2026-03-08-servicenow-csdm-data-modelling.html; https://microsoft.github.io/multi-agent-reference-architecture/docs/reference-architecture/Reference-Architecture.html]
- Links:
  - https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
  - https://arxiv.org/abs/2404.16130
  - https://www.nist.gov/itl/ai-risk-management-framework
