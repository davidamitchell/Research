---
review_count: 2
title: "What capabilities, sub-capabilities, architectural patterns, and maturity dimensions define tool-using, semi-autonomous Semantic Knowledge Management systems?"
added: 2026-05-21T11:07:25+00:00
status: completed
priority: high
blocks: []
started: 2026-05-22T06:02:12+00:00
completed: 2026-05-22T06:37:14+00:00
output: []
themes: [agentic-ai, knowledge-management]
cites:
  - 2026-05-21-dynamic-resource-discovery-context-ontology
  - 2026-05-12-knowledge-graph-agentic-runtime-dependency
  - 2026-05-12-knowledge-graph-lifecycle-management-agentic
  - 2026-05-15-ontology-landscape-for-curated-enterprise-context
  - 2026-05-20-agentic-km-5-pillar-capability-model
related:
  - 2026-03-18-api-context-hubs-rag-mcp
  - 2026-03-03-knowledge-representation-agent-context
  - 2026-03-02-agent-memory-management-context-injection
superseded_by: ~
supersedes: ~
item_type: primary
confidence: medium
versions:
  - version: "1.0"
    sha: 9c236fe199dadda3a505c89ccb98e539c4eececb
    changed: 2026-05-22
    progress: progress/2026-05-22-agentic-semantic-km-capability-model.md
    summary: Initial completion
---

# What capabilities, sub-capabilities, architectural patterns, and maturity dimensions define tool-using, semi-autonomous Semantic Knowledge Management systems?

## Research Question

What are the key capabilities, sub-capabilities, architectural patterns, and maturity dimensions for tool-using, semi-autonomous Semantic Knowledge Management (SKM) systems that integrate automated harvesting and extraction, Resource Description Framework (RDF) and Web Ontology Language (OWL) based knowledge graphs, dynamic context selection and durable memory references, agent reasoning and orchestration, and semantic interoperability?

## Scope

**In scope:**
- Capability taxonomies and maturity dimensions for tool-using, semi-autonomous SKM systems
- Sub-capabilities for ingestion, extraction, ontology management, graph maintenance, context and memory operations, reasoning, orchestration, and interoperability
- Reference architectures and implementation patterns from semantic graph platforms and agent orchestration frameworks
- Human tasks and operating roles required to design, govern, and run these systems
- Mapping of adjacent models, legacy Knowledge Management (KM) frameworks, multi-agent capability models, and graph-based Retrieval-Augmented Generation (GraphRAG) patterns, into a unified SKM capability hierarchy

**Out of scope:**
- Building or modifying production code in this repository
- Vendor procurement decisions or pricing comparisons
- Domain-specific vertical implementations, healthcare, finance, and similar sectors, beyond extracting generalizable patterns
- Benchmarking specific model providers

**Constraints:** Focus on frameworks, reference architectures, ontologies, and implementations with public documentation; prioritize sources from 2019 onward plus foundational standards; output type is knowledge; every source listed must include a Uniform Resource Locator (URL).

## Context

This item aims to produce a defensible capability model for tool-using, semi-autonomous SKM systems so architecture and maturity assessments can be grounded in explicit evidence rather than ad hoc feature lists.[inference; source: https://cmmiinstitute.com/learning/appraisals/levels; https://davidamitchell.github.io/Research/research/2026-05-20-agentic-km-5-pillar-capability-model.html]

## Approach

1. **Extract capability primitives from existing KM and maturity frameworks.**
   1a. Which classic Knowledge Management (KM) capabilities remain relevant for tool-using, semi-autonomous systems?
   1b. Which capability and maturity dimensions are missing when ontology-native and agent-native behaviors are required?
2. **Catalogue semantic graph and ontology capabilities.**
   2a. What sub-capabilities are required for RDF and OWL modeling, schema evolution, reasoning, and semantic interoperability?
   2b. What harvesting and extraction patterns feed these semantic layers reliably?
3. **Catalogue agentic runtime capabilities.**
   3a. What context-selection and durable-memory-reference capabilities are required for dynamic agent execution?
   3b. What reasoning, planning, tool invocation, and orchestration capabilities appear consistently in reference architectures?
4. **Identify architectural patterns and implementation archetypes.**
   4a. Which architecture patterns, graph-based Retrieval-Augmented Generation (GraphRAG), retrieval-plus-reasoning, planner-executor, and registry-mediated tool discovery, recur across implementations?
   4b. How do these patterns map to capabilities, process flows, and human tasks?
5. **Synthesize a hierarchical capability model and maturity rubric.**
   5a. What top-level capabilities and sub-capabilities form the minimum complete model?
   5b. What maturity levels differentiate initial, repeatable, managed, quantitatively managed, and optimizing SKM practices?

## Sources

- [ ] [American Productivity & Quality Center (APQC) Knowledge Management Framework](https://www.apqc.org/resource-library/resource-listing/apqcs-knowledge-management-framework)
- [ ] [American Productivity & Quality Center (APQC) Process Frameworks](https://www.apqc.org/process-frameworks)
- [x] [CMMI Institute What is Capability Maturity Model Integration (CMMI)?](https://cmmiinstitute.com/)
- [x] [Capability Maturity Model Integration (CMMI) Institute Levels of capability and performance](https://cmmiinstitute.com/learning/appraisals/levels)
- [x] [World Wide Web Consortium (W3C) RDF 1.1 Concepts and Abstract Syntax](https://www.w3.org/TR/rdf11-concepts/)
- [x] [W3C OWL 2 Web Ontology Language Document Overview](https://www.w3.org/TR/owl2-overview/)
- [x] [W3C SPARQL Protocol and RDF Query Language (SPARQL) 1.1 Query Language](https://www.w3.org/TR/sparql11-query/)
- [x] [Edge et al. (2024) From Local to Global: A GraphRAG approach to query-focused summarization](https://arxiv.org/abs/2404.16130)
- [x] [Model Context Protocol (MCP) Introduction](https://modelcontextprotocol.io/introduction)
- [x] [Model Context Protocol (MCP) Architecture overview](https://modelcontextprotocol.io/docs/learn/architecture)
- [x] [Anthropic Effective context engineering for Artificial Intelligence (AI) agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)
- [x] [metaphacts Semantic knowledge modeling](https://metaphacts.com/solutions/semantic-knowledge-modeling)
- [x] [Stardog Virtual Graphs](https://docs.stardog.com/virtual-graphs/)
- [x] [Stardog Reasoning and inference](https://docs.stardog.com/inference-engine/)
- [x] [Freitas et al. (2017) Model-driven engineering of multi-agent systems based on ontologies](https://smart-pucrs.github.io/publications/pdf/ao2017ArturFreitas.pdf)
- [x] [LangGraph Overview](https://docs.langchain.com/oss/python/langgraph/overview)
- [x] [LangGraph Durable execution](https://docs.langchain.com/oss/python/langgraph/durable-execution)
- [x] [LangGraph Persistence](https://docs.langchain.com/oss/python/langgraph/persistence)
- [x] [LangChain Memory concepts](https://docs.langchain.com/oss/python/concepts/memory)
- [x] [LangGraph Interrupts](https://docs.langchain.com/oss/python/langgraph/interrupts)
- [x] [Anthropic Building effective agents](https://www.anthropic.com/research/building-effective-agents)
- [x] [Microsoft Multi-agent Reference Architecture: Reference Architecture](https://microsoft.github.io/multi-agent-reference-architecture/docs/reference-architecture/Reference-Architecture.html)
- [x] [Microsoft Multi-agent Reference Architecture: Governance](https://microsoft.github.io/multi-agent-reference-architecture/docs/governance/Governance.html)
- [x] [Mitchell (2026) Dynamic Resource Discovery architecture pattern and context engineering](https://davidamitchell.github.io/Research/research/2026-05-21-dynamic-resource-discovery-context-ontology.html)
- [x] [Mitchell (2026) Knowledge Graph in the live execution path of multi-step Large Language Model (LLM) systems](https://davidamitchell.github.io/Research/research/2026-05-12-knowledge-graph-agentic-runtime-dependency.html)
- [x] [Mitchell (2026) Knowledge Graph lifecycle management for multi-step software agents](https://davidamitchell.github.io/Research/research/2026-05-12-knowledge-graph-lifecycle-management-agentic.html)
- [x] [Mitchell (2026) Ontology landscape for curated lexical and structured enterprise context](https://davidamitchell.github.io/Research/research/2026-05-15-ontology-landscape-for-curated-enterprise-context.html)
- [x] [Mitchell (2026) Five-pillar Knowledge Management capability model for tool-using, semi-autonomous Artificial Intelligence systems](https://davidamitchell.github.io/Research/research/2026-05-20-agentic-km-5-pillar-capability-model.html)

---

## Research Skill Output

### §0 Initialise

question: determine the minimum complete capability hierarchy, recurring architecture patterns, and maturity rubric for tool-using, semi-autonomous Semantic Knowledge Management systems.

scope: ingestion and extraction, semantic graph operations, context and memory management, reasoning and orchestration, interoperability, and operating roles are in scope; production coding, vendor procurement, and model-provider benchmarking are out of scope.

constraints: full-mode research, Uniform Resource Locator (URL) backed sources only, public standards and implementation documentation preferred, and prior completed repository items must be integrated where they materially qualify the same control surface.

output_format: full research record with synthesis mirrored into Findings.

mode: full

- [inference] The most relevant prior completed items are Mitchell (2026) on Dynamic Resource Discovery, Mitchell (2026) on Knowledge Graph runtime dependency, Mitchell (2026) on Knowledge Graph lifecycle management, Mitchell (2026) on ontology landscape for enterprise context, and Mitchell (2026) on the five-pillar Knowledge Management model, because they already separate discovery, runtime dependency, lifecycle control, semantic-layer trade-offs, and enterprise operating-model concerns that this item now recombines into a finer-grained capability hierarchy.[source: https://davidamitchell.github.io/Research/research/2026-05-21-dynamic-resource-discovery-context-ontology.html; https://davidamitchell.github.io/Research/research/2026-05-12-knowledge-graph-agentic-runtime-dependency.html; https://davidamitchell.github.io/Research/research/2026-05-12-knowledge-graph-lifecycle-management-agentic.html; https://davidamitchell.github.io/Research/research/2026-05-15-ontology-landscape-for-curated-enterprise-context.html; https://davidamitchell.github.io/Research/research/2026-05-20-agentic-km-5-pillar-capability-model.html]
- [inference] Working definition: a tool-using, semi-autonomous SKM system combines knowledge capture and semantic graph management with runtime context assembly, durable memory, open interoperability surfaces, and agent orchestration over governed external tools and data sources.[source: https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents; https://modelcontextprotocol.io/docs/learn/architecture; https://docs.langchain.com/oss/python/langgraph/overview; https://microsoft.github.io/multi-agent-reference-architecture/docs/reference-architecture/Reference-Architecture.html]

### §1 Question Decomposition

- A. Legacy capability and maturity baselines
  - A1. What capability and maturity scaffolding do public Knowledge Management and improvement frameworks contribute?
  - A2. Which parts of that scaffolding remain useful once semantic graphs and agent runtimes are added?
- B. Semantic knowledge layer
  - B1. What capabilities are required for RDF datasets, OWL ontologies, and SPARQL access?
  - B2. What platform capabilities recur for semantic modeling, mapping, and reasoning?
  - B3. Which lifecycle controls are needed to keep graph semantics stable over time?
- C. Ingestion and graph maintenance
  - C1. What harvesting and extraction patterns build or refresh the semantic layer?
  - C2. What maintenance capabilities keep graph content fresh, queryable, and trustworthy?
- D. Runtime context and memory
  - D1. What capabilities assemble the right working context for each step?
  - D2. What capabilities preserve short-term and long-term memory without forcing full preloading?
  - D3. What controls make long-running agent state resumable and inspectable?
- E. Reasoning, orchestration, and interoperability
  - E1. Which orchestration patterns recur across public agent references?
  - E2. What discovery and capability-description surfaces make tool use composable?
  - E3. How do ontology-backed coordination models relate to orchestrator and supervisor designs?
- F. Operating model and maturity
  - F1. Which human roles are required to design, govern, and improve the system?
  - F2. What top-level capabilities and sub-capabilities form the minimum complete model?
  - F3. What maturity levels differentiate initial, repeatable, managed, quantitatively managed, and optimizing practice?

### §2 Investigation

#### 2.0 Identified but not consulted

- [ ] [American Productivity & Quality Center (APQC) Knowledge Management Framework](https://www.apqc.org/resource-library/resource-listing/apqcs-knowledge-management-framework)
- [ ] [American Productivity & Quality Center (APQC) Process Frameworks](https://www.apqc.org/process-frameworks)
- Access note: APQC URLs returned 403 during this session

#### 2.1 Legacy capability and maturity baselines

- [fact] The Capability Maturity Model Integration (CMMI) maturity model defines capability levels for individual practice areas and maturity levels for organization-wide improvement, ranging from Initial through Optimizing.[source: https://cmmiinstitute.com/learning/appraisals/levels]
- [fact] The CMMI Institute describes Capability Level 2 as managed project-level practice, Capability Level 3 as use of organizational standards and tailoring, Maturity Level 4 as quantitatively managed, and Maturity Level 5 as optimizing through continuous improvement.[source: https://cmmiinstitute.com/learning/appraisals/levels]
- [fact] The CMMI ecosystem includes Lead Appraisers, Instructors, Associates, Professionals, and Consultants, which shows that mature capability programs require explicit assessment, training, and improvement roles rather than only technical implementation roles.[source: https://cmmiinstitute.com/; https://cmmiinstitute.com/learning/appraisals/levels]
- [fact] The prior five-pillar Knowledge Management item in this repository separated knowledge foundations, context engineering, memory and state, governance, and operations into distinct enterprise capability domains.[source: https://davidamitchell.github.io/Research/research/2026-05-20-agentic-km-5-pillar-capability-model.html]
- [inference] CMMI contributes a useful maturity grammar for this item, but it does not define the semantic graph, discovery, memory, or tool-interoperability capabilities required by SKM systems, so its value here is staging logic rather than domain content.[source: https://cmmiinstitute.com/learning/appraisals/levels; https://davidamitchell.github.io/Research/research/2026-05-20-agentic-km-5-pillar-capability-model.html]

#### 2.2 Semantic knowledge layer capabilities

- [fact] RDF provides a graph-based data model of triples and datasets, where a dataset contains a default graph and zero or more named graphs.[source: https://www.w3.org/TR/rdf11-concepts/]
- [fact] OWL 2 provides formally defined classes, properties, individuals, semantics, and profiles for ontology development and exchange, and OWL ontologies can be exchanged as RDF documents.[source: https://www.w3.org/TR/owl2-overview/]
- [fact] SPARQL 1.1 provides graph pattern matching, optional patterns, property paths, subqueries, aggregation, and federated query over RDF graphs.[source: https://www.w3.org/TR/sparql11-query/]
- [fact] metaphactory describes semantic knowledge modeling as collaborative work among business users, domain experts, subject matter experts, ontology engineers, and taxonomists, and it explicitly grounds its platform on OWL, Shapes Constraint Language (SHACL), Simple Knowledge Organization System (SKOS), and Data Catalog Vocabulary (DCAT).[source: https://metaphacts.com/solutions/semantic-knowledge-modeling]
- [fact] Stardog Virtual Graphs declaratively map structured and semi-structured enterprise data into a knowledge graph, rewrite portions of SPARQL queries into native source queries, and support querying remote data in situ.[source: https://docs.stardog.com/virtual-graphs/]
- [fact] Stardog performs reasoning lazily at query time instead of materializing inferred triples, and this query-time approach is what allows reasoning over virtual graphs.[source: https://docs.stardog.com/inference-engine/]
- [fact] The prior ontology landscape item concluded that a durable enterprise semantic layer is usually a layered ontology-plus-graph architecture rather than a pure ontology-only deployment.[source: https://davidamitchell.github.io/Research/research/2026-05-15-ontology-landscape-for-curated-enterprise-context.html]
- [inference] The semantic layer of an SKM system therefore needs at least six sub-capabilities: ontology and taxonomy authoring, source-to-ontology mapping, federated or virtualized query, constraint validation and reasoning, semantic search over named graphs or equivalent partitions, and version-aware lifecycle control.[source: https://www.w3.org/TR/rdf11-concepts/; https://www.w3.org/TR/owl2-overview/; https://www.w3.org/TR/sparql11-query/; https://metaphacts.com/solutions/semantic-knowledge-modeling; https://docs.stardog.com/virtual-graphs/; https://docs.stardog.com/inference-engine/; https://davidamitchell.github.io/Research/research/2026-05-15-ontology-landscape-for-curated-enterprise-context.html]

#### 2.3 Ingestion, extraction, and graph maintenance

- [fact] GraphRAG builds an entity knowledge graph from source documents and then pre-generates community summaries that can later be combined into final answers for corpus-level questions.[source: https://arxiv.org/abs/2404.16130]
- [fact] Stardog Virtual Graphs support both explicit mappings and direct mapping from relational schemas, which means semantic integration can occur through live virtualization as well as through materialized graph publishing.[source: https://docs.stardog.com/virtual-graphs/]
- [fact] The prior Knowledge Graph lifecycle item concluded that additive-first schema evolution, explicit derivation links, provenance-aware conflict handling, and conservative entity resolution are safer than silent in-place rewrites for agent-dependent graphs.[source: https://davidamitchell.github.io/Research/research/2026-05-12-knowledge-graph-lifecycle-management-agentic.html]
- [fact] The prior Knowledge Graph runtime item concluded that a graph used during execution should be treated as a tiered dependency with explicit freshness limits, fallback behavior, and failure handling.[source: https://davidamitchell.github.io/Research/research/2026-05-12-knowledge-graph-agentic-runtime-dependency.html]
- [inference] Harvesting and extraction capabilities split into two recurrent patterns: document-to-graph extraction pipelines that create graph-ready entities and summaries, and source virtualization pipelines that project existing operational data into the semantic layer without forcing immediate materialization.[source: https://arxiv.org/abs/2404.16130; https://docs.stardog.com/virtual-graphs/; https://davidamitchell.github.io/Research/research/2026-05-12-knowledge-graph-lifecycle-management-agentic.html]
- [inference] Maintenance capabilities cannot stop at ingestion, because freshness, provenance, conflict management, and safe publication determine whether the semantic layer remains usable for downstream agents.[source: https://docs.stardog.com/virtual-graphs/; https://davidamitchell.github.io/Research/research/2026-05-12-knowledge-graph-lifecycle-management-agentic.html; https://davidamitchell.github.io/Research/research/2026-05-12-knowledge-graph-agentic-runtime-dependency.html]

#### 2.4 Runtime context, memory, and durable state

- [fact] Anthropic defines context engineering as curating and maintaining the optimal set of tokens during Large Language Model (LLM) inference across prompts, tools, external data, Model Context Protocol (MCP) surfaces, and message history.[source: https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents]
- [fact] Anthropic recommends just-in-time context strategies in which agents keep lightweight identifiers such as file paths, stored queries, or links and dynamically load data into context only when needed.[source: https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents]
- [fact] LangGraph describes itself as a low-level orchestration framework and runtime for long-running, stateful agents, focused on durable execution, human-in-the-loop control, and memory.[source: https://docs.langchain.com/oss/python/langgraph/overview]
- [fact] LangGraph durable execution requires persistence, a thread identifier, and task-wrapped non-deterministic or side-effecting operations so a workflow can resume from its last recorded state without replaying completed work incorrectly.[source: https://docs.langchain.com/oss/python/langgraph/durable-execution]
- [fact] LangGraph persistence saves checkpoints as snapshots of graph state at each super-step and uses thread identifiers as the key for restoring and resuming state.[source: https://docs.langchain.com/oss/python/langgraph/persistence]
- [fact] LangChain's memory concepts distinguish short-term memory, thread-scoped state for the active conversation, from long-term memory, namespace-scoped facts or records that can be recalled across sessions.[source: https://docs.langchain.com/oss/python/concepts/memory]
- [fact] LangGraph interrupts pause execution, persist state, and resume later against the same thread identifier, which makes human approval and runtime repair first-class orchestration features rather than ad hoc exceptions.[source: https://docs.langchain.com/oss/python/langgraph/interrupts]
- [inference] Dynamic context and durable memory references in SKM systems are best treated as selective retrieval plus durable pointers into state and storage, not as a strategy of preloading entire knowledge objects into the model context window.[source: https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents; https://docs.langchain.com/oss/python/langgraph/overview; https://docs.langchain.com/oss/python/langgraph/durable-execution; https://docs.langchain.com/oss/python/concepts/memory]

#### 2.5 Reasoning, orchestration, and interoperability

- [fact] Anthropic distinguishes workflows, where LLMs and tools follow predefined code paths, from agents, where LLMs dynamically direct their own tool use and processes, and it identifies routing, parallelization, orchestrator-workers, and evaluator-optimizer as recurring workflow patterns.[source: https://www.anthropic.com/research/building-effective-agents]
- [fact] MCP is an open standard for connecting AI applications to external systems, and the architecture documentation defines tools, resources, and prompts as the three server primitives discoverable through `*/list` methods.[source: https://modelcontextprotocol.io/introduction; https://modelcontextprotocol.io/docs/learn/architecture]
- [fact] The Microsoft Multi-agent Reference Architecture places an orchestrator, classifier, agent registry, knowledge layer, persistent state store, supervisor agent, and MCP server in one governed control plane.[source: https://microsoft.github.io/multi-agent-reference-architecture/docs/reference-architecture/Reference-Architecture.html]
- [fact] The prior Dynamic Resource Discovery item concluded that registries, machine-readable capability descriptors, lookup or advertisement mechanisms, and late binding recur across discovery systems and contemporary MCP deployments.[source: https://davidamitchell.github.io/Research/research/2026-05-21-dynamic-resource-discovery-context-ontology.html]
- [fact] Freitas et al. propose an ontology-based modeling approach for multi-agent systems that integrates agent, environment, and organization dimensions and argue that ontologies add semantic reasoning and verification to agent-oriented software engineering.[source: https://smart-pucrs.github.io/publications/pdf/ao2017ArturFreitas.pdf]
- [inference] The recurring orchestration patterns for SKM systems are planner or orchestrator control, worker specialization, registry-mediated discovery, capability-described tool invocation, and explicit supervisor or interrupt paths for approval, repair, or conflict resolution.[source: https://www.anthropic.com/research/building-effective-agents; https://modelcontextprotocol.io/docs/learn/architecture; https://microsoft.github.io/multi-agent-reference-architecture/docs/reference-architecture/Reference-Architecture.html; https://davidamitchell.github.io/Research/research/2026-05-21-dynamic-resource-discovery-context-ontology.html]
- [inference] Semantic interoperability is not only a data-model concern, because a usable SKM runtime needs both W3C semantic standards for knowledge representation and discovery standards such as MCP for tool and resource invocation.[source: https://www.w3.org/TR/rdf11-concepts/; https://www.w3.org/TR/owl2-overview/; https://www.w3.org/TR/sparql11-query/; https://modelcontextprotocol.io/introduction; https://modelcontextprotocol.io/docs/learn/architecture]

#### 2.6 Governance, roles, and operating model

- [fact] Microsoft's governance guidance for multi-agent systems recommends a cross-functional governance committee, explicit Responsible Artificial Intelligence (RAI) policies, guardrails, role-based access control (RBAC), structured logging, evaluation, red-teaming, and training.[source: https://microsoft.github.io/multi-agent-reference-architecture/docs/governance/Governance.html]
- [fact] metaphactory explicitly positions semantic knowledge modeling as collaborative work among business users, domain experts, subject matter experts, ontology engineers, and taxonomists.[source: https://metaphacts.com/solutions/semantic-knowledge-modeling]
- [fact] The CMMI ecosystem includes dedicated appraisal, instruction, and improvement roles, which shows that maturity programs are sustained by institutional responsibilities rather than only by platform features.[source: https://cmmiinstitute.com/; https://cmmiinstitute.com/learning/appraisals/levels]
- [inference] The minimum operating model for SKM therefore needs at least five role families: domain or knowledge owners, ontology and knowledge engineers, orchestration and platform engineers, governance and evaluation owners, and improvement or appraisal leads.[source: https://metaphacts.com/solutions/semantic-knowledge-modeling; https://microsoft.github.io/multi-agent-reference-architecture/docs/governance/Governance.html; https://cmmiinstitute.com/learning/appraisals/levels]

#### 2.7 Derived capability hierarchy and maturity rubric

- [inference] The minimum complete SKM capability model has six top-level domains: knowledge acquisition and extraction; semantic modeling and graph operations; runtime context and memory; reasoning and orchestration; interoperability and discovery; and governance with continuous improvement.[source: https://arxiv.org/abs/2404.16130; https://www.w3.org/TR/rdf11-concepts/; https://www.w3.org/TR/owl2-overview/; https://www.w3.org/TR/sparql11-query/; https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents; https://modelcontextprotocol.io/docs/learn/architecture; https://docs.langchain.com/oss/python/langgraph/overview; https://microsoft.github.io/multi-agent-reference-architecture/docs/governance/Governance.html]
- [inference] The first domain, knowledge acquisition and extraction, includes source registration, harvesting, parsing or extraction, semantic normalization, provenance capture, refresh triggers, and publication handoff into the semantic layer.[source: https://arxiv.org/abs/2404.16130; https://docs.stardog.com/virtual-graphs/; https://davidamitchell.github.io/Research/research/2026-05-12-knowledge-graph-lifecycle-management-agentic.html]
- [inference] The second domain, semantic modeling and graph operations, includes ontology and taxonomy design, mapping or virtualization, validation and reasoning, SPARQL or equivalent query surfaces, entity and schema lifecycle control, and semantic search or federated retrieval.[source: https://www.w3.org/TR/rdf11-concepts/; https://www.w3.org/TR/owl2-overview/; https://www.w3.org/TR/sparql11-query/; https://metaphacts.com/solutions/semantic-knowledge-modeling; https://docs.stardog.com/virtual-graphs/; https://docs.stardog.com/inference-engine/]
- [inference] The third domain, runtime context and memory, includes just-in-time context retrieval, checkpointed thread state, short-term working memory, long-term namespace memory, resumability, interrupt handling, and context-pruning or compression rules.[source: https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents; https://docs.langchain.com/oss/python/langgraph/durable-execution; https://docs.langchain.com/oss/python/langgraph/persistence; https://docs.langchain.com/oss/python/concepts/memory; https://docs.langchain.com/oss/python/langgraph/interrupts]
- [inference] The fourth and fifth domains, reasoning and orchestration plus interoperability and discovery, include routing, task decomposition, worker supervision, tool and prompt invocation, capability description, registries, open protocols, and late binding between agents, tools, and semantic stores.[source: https://www.anthropic.com/research/building-effective-agents; https://modelcontextprotocol.io/introduction; https://modelcontextprotocol.io/docs/learn/architecture; https://microsoft.github.io/multi-agent-reference-architecture/docs/reference-architecture/Reference-Architecture.html; https://davidamitchell.github.io/Research/research/2026-05-21-dynamic-resource-discovery-context-ontology.html]
- [inference] The sixth domain, governance with continuous improvement, includes role design, approval controls, access control, provenance policy, evaluation, red-teaming, training, quantitative monitoring, and formal improvement cycles.[source: https://microsoft.github.io/multi-agent-reference-architecture/docs/governance/Governance.html; https://cmmiinstitute.com/learning/appraisals/levels; https://davidamitchell.github.io/Research/research/2026-05-20-agentic-km-5-pillar-capability-model.html]
- [inference] The maturity rubric is best adapted as five levels: Initial, static documents and manual graph updates with no durable runtime state; Repeatable, scheduled ingestion and explicit schema or tool catalogs; Managed, organization-wide semantic standards, versioned graph lifecycle, checkpointed orchestration, and role separation; Quantitatively Managed, service levels and metrics for freshness, latency, failure, and evaluation quality; Optimizing, dynamic discovery, automated quality checks, and continuous human-supervised improvement.[source: https://cmmiinstitute.com/learning/appraisals/levels; https://docs.langchain.com/oss/python/langgraph/persistence; https://docs.stardog.com/inference-engine/; https://microsoft.github.io/multi-agent-reference-architecture/docs/governance/Governance.html]
- [inference] In this rubric, "repeatable" maps to project-level managed practice and "managed" maps to organization-wide defined and governed practice, because that translation preserves the spirit of CMMI while fitting the maturity labels requested for this item.[source: https://cmmiinstitute.com/learning/appraisals/levels]

### §3 Reasoning

- [fact] The strongest direct evidence in this item comes from standards and official runtime documentation: RDF for graph structure, OWL for semantic expressiveness, SPARQL for query behavior, MCP for tool and resource discovery, and LangGraph for persistence and memory behavior.[source: https://www.w3.org/TR/rdf11-concepts/; https://www.w3.org/TR/owl2-overview/; https://www.w3.org/TR/sparql11-query/; https://modelcontextprotocol.io/docs/learn/architecture; https://docs.langchain.com/oss/python/langgraph/persistence]
- [fact] Public platform documents from metaphactory and Stardog directly support the need for collaborative modeling, virtualization, and query-time reasoning, but they describe product capabilities rather than comparative outcome benchmarks.[source: https://metaphacts.com/solutions/semantic-knowledge-modeling; https://docs.stardog.com/virtual-graphs/; https://docs.stardog.com/inference-engine/]
- [inference] The six-domain capability model is a synthesis across standards, runtime frameworks, and prior completed items, because no single consulted source publishes the full hierarchy in one place.[source: https://cmmiinstitute.com/learning/appraisals/levels; https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents; https://microsoft.github.io/multi-agent-reference-architecture/docs/reference-architecture/Reference-Architecture.html; https://davidamitchell.github.io/Research/research/2026-05-20-agentic-km-5-pillar-capability-model.html]
- [inference] The maturity rubric is therefore medium confidence rather than high confidence, because its stages are adapted from CMMI and then specialized with semantic-graph and agent-runtime evidence instead of being lifted from a published SKM maturity standard.[source: https://cmmiinstitute.com/learning/appraisals/levels; https://docs.langchain.com/oss/python/langgraph/persistence; https://microsoft.github.io/multi-agent-reference-architecture/docs/governance/Governance.html]
- [assumption] Vendor and framework documentation describes real platform surfaces that are stable enough to use for capability taxonomy even when the sources do not independently quantify comparative performance or adoption depth.[source: https://metaphacts.com/solutions/semantic-knowledge-modeling; https://docs.stardog.com/virtual-graphs/; https://docs.langchain.com/oss/python/langgraph/overview; https://microsoft.github.io/multi-agent-reference-architecture/docs/reference-architecture/Reference-Architecture.html]

### §4 Consistency Check

- [fact] No direct contradiction appeared across the consulted standards about the roles of RDF, OWL, and SPARQL, because the documents describe complementary layers of the same semantic stack rather than rival models.[source: https://www.w3.org/TR/rdf11-concepts/; https://www.w3.org/TR/owl2-overview/; https://www.w3.org/TR/sparql11-query/]
- [inference] The main design tension is between pre-generated graph summaries, as in GraphRAG, and just-in-time retrieval, as in Anthropic context engineering, and the tension resolves cleanly when summaries are treated as one retrieval artifact among several rather than as the sole runtime context surface.[source: https://arxiv.org/abs/2404.16130; https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents]
- [inference] The role model is internally consistent with the capability model, because each top-level domain implies a distinct accountability surface, semantic modeling, runtime orchestration, governance, or improvement, rather than collapsing all work into a generic "AI engineer" function.[source: https://metaphacts.com/solutions/semantic-knowledge-modeling; https://microsoft.github.io/multi-agent-reference-architecture/docs/governance/Governance.html; https://cmmiinstitute.com/learning/appraisals/levels]

### §5 Depth and Breadth Expansion

- [inference] Technical lens: the most important architectural boundary is between the semantic substrate and the orchestration runtime, because semantic correctness, freshness, and versioning are not the same problem as routing, checkpointing, and tool invocation.[source: https://docs.stardog.com/inference-engine/; https://docs.langchain.com/oss/python/langgraph/overview; https://davidamitchell.github.io/Research/research/2026-05-12-knowledge-graph-agentic-runtime-dependency.html]
- [inference] Governance lens: the capability model is not credible unless approval, logging, access control, and evaluation are designed as capabilities, because multi-agent systems increase autonomy and therefore increase the need for accountable boundaries.[source: https://microsoft.github.io/multi-agent-reference-architecture/docs/governance/Governance.html; https://docs.langchain.com/oss/python/langgraph/interrupts]
- [inference] Economic and operating lens: virtualization, just-in-time retrieval, and checkpointed replay reduce unnecessary materialization and repeated work, which makes them operating-model choices as much as technical ones.[source: https://docs.stardog.com/virtual-graphs/; https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents; https://docs.langchain.com/oss/python/langgraph/durable-execution]
- [inference] Behavioral lens: human-in-the-loop design is not an optional safety ornament, because it changes how agents recover from uncertainty, policy-sensitive actions, and incomplete context by creating explicit pause and review points.[source: https://docs.langchain.com/oss/python/langgraph/interrupts; https://microsoft.github.io/multi-agent-reference-architecture/docs/governance/Governance.html]

### §6 Synthesis

**Executive summary**

- [inference] A complete SKM capability model requires six separable domains, and this six-domain structure is best read as an extension of the earlier repository five-pillar model, because it splits knowledge foundations into acquisition versus semantic operations and promotes interoperability and discovery to an explicit control surface.[source: https://davidamitchell.github.io/Research/research/2026-05-20-agentic-km-5-pillar-capability-model.html; https://arxiv.org/abs/2404.16130; https://modelcontextprotocol.io/docs/learn/architecture; https://microsoft.github.io/multi-agent-reference-architecture/docs/governance/Governance.html]
- [inference] The recurring architecture is a layered stack in which harvested or virtualized sources feed an RDF and OWL semantic layer queried through SPARQL, while an orchestrator manages dynamic capability discovery, checkpointed state, memory recall, and tool invocation through open protocols such as MCP.[source: https://docs.stardog.com/virtual-graphs/; https://docs.stardog.com/inference-engine/; https://www.w3.org/TR/rdf11-concepts/; https://www.w3.org/TR/owl2-overview/; https://www.w3.org/TR/sparql11-query/; https://modelcontextprotocol.io/docs/learn/architecture; https://microsoft.github.io/multi-agent-reference-architecture/docs/reference-architecture/Reference-Architecture.html]
- [inference] Maturity is best understood as the movement from manual and static practices toward versioned semantic models, persistent and interruptible runtime state, governed discovery, and quantitative improvement loops adapted from CMMI-style staging.[source: https://cmmiinstitute.com/learning/appraisals/levels; https://docs.langchain.com/oss/python/langgraph/persistence; https://microsoft.github.io/multi-agent-reference-architecture/docs/governance/Governance.html]
- [inference] The evidence base is strongest for semantic, orchestration, and governance capabilities, and weaker for publicly accessible classical KM taxonomies, so the final hierarchy is best treated as a medium-confidence synthesis rather than a settled industry standard.[source: https://cmmiinstitute.com/learning/appraisals/levels; https://www.w3.org/TR/rdf11-concepts/; https://www.anthropic.com/research/building-effective-agents; https://davidamitchell.github.io/Research/research/2026-05-20-agentic-km-5-pillar-capability-model.html]

**Key findings**

1. [inference] The minimum complete SKM model needs six top-level capability domains, and this is a bounded extension of the earlier five-pillar repository model, because acquisition versus semantic operations and interoperability versus orchestration expose materially different control surfaces, failure modes, and ownership boundaries.[source: https://davidamitchell.github.io/Research/research/2026-05-20-agentic-km-5-pillar-capability-model.html; https://arxiv.org/abs/2404.16130; https://modelcontextprotocol.io/docs/learn/architecture; https://microsoft.github.io/multi-agent-reference-architecture/docs/governance/Governance.html]
2. [inference] Semantic-layer maturity depends on explicit RDF datasets, OWL ontologies, SPARQL query surfaces, collaborative semantic modeling, and query-time reasoning or validation, because these capabilities recur across standards and enterprise semantic platforms and collectively define the semantic control surface of an SKM system.[source: https://www.w3.org/TR/rdf11-concepts/; https://www.w3.org/TR/owl2-overview/; https://www.w3.org/TR/sparql11-query/; https://metaphacts.com/solutions/semantic-knowledge-modeling; https://docs.stardog.com/inference-engine/]
3. [inference] Harvesting and extraction capability must cover both document-derived graph construction and live source virtualization, because GraphRAG-style pipelines and Stardog-style virtual graphs solve complementary parts of the knowledge acquisition problem.[source: https://arxiv.org/abs/2404.16130; https://docs.stardog.com/virtual-graphs/; https://davidamitchell.github.io/Research/research/2026-05-12-knowledge-graph-lifecycle-management-agentic.html]
4. [inference] Dynamic context and memory capability is best modeled through just-in-time retrieval, thread-scoped short-term state, namespace-scoped long-term memory, checkpointed replay, and resumable interrupts, because those primitives together cover the runtime state-management problems described in current context-engineering and orchestration documentation.[source: https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents; https://docs.langchain.com/oss/python/langgraph/durable-execution; https://docs.langchain.com/oss/python/langgraph/persistence; https://docs.langchain.com/oss/python/concepts/memory; https://docs.langchain.com/oss/python/langgraph/interrupts]
5. [inference] Reasoning and orchestration maturity is marked by progression from fixed workflows to planner or supervisor coordination with worker specialization, because public agent guidance and reference architectures repeatedly separate routing, decomposition, supervision, and recovery concerns.[source: https://www.anthropic.com/research/building-effective-agents; https://microsoft.github.io/multi-agent-reference-architecture/docs/reference-architecture/Reference-Architecture.html; https://smart-pucrs.github.io/publications/pdf/ao2017ArturFreitas.pdf]
6. [inference] Interoperability should be treated as a first-class capability domain, because usable SKM systems need both semantic standards for data and discovery standards for tools, with MCP exposing discoverable tools, resources, and prompts through explicit list and get methods.[source: https://www.w3.org/TR/rdf11-concepts/; https://www.w3.org/TR/owl2-overview/; https://www.w3.org/TR/sparql11-query/; https://modelcontextprotocol.io/introduction; https://modelcontextprotocol.io/docs/learn/architecture]
7. [inference] The minimum operating model requires domain owners, ontology and knowledge engineers, orchestration and platform engineers, governance and evaluation owners, and formal improvement roles, because semantic modeling, runtime control, and maturity assurance are documented as different human workstreams.[source: https://metaphacts.com/solutions/semantic-knowledge-modeling; https://microsoft.github.io/multi-agent-reference-architecture/docs/governance/Governance.html; https://cmmiinstitute.com/learning/appraisals/levels]
8. [inference] A practical maturity rubric for SKM systems runs from Initial through Repeatable, Managed, Quantitatively Managed, and Optimizing, with the transitions driven by versioned semantics, persistent runtime state, governed discovery, and measurable control loops rather than by model size alone.[source: https://cmmiinstitute.com/learning/appraisals/levels; https://docs.langchain.com/oss/python/langgraph/persistence; https://docs.stardog.com/inference-engine/; https://microsoft.github.io/multi-agent-reference-architecture/docs/governance/Governance.html]

**Evidence map**

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [inference] SKM requires six top-level capability domains as an extension of the earlier five-pillar repository model. | https://davidamitchell.github.io/Research/research/2026-05-20-agentic-km-5-pillar-capability-model.html; https://arxiv.org/abs/2404.16130; https://modelcontextprotocol.io/docs/learn/architecture; https://microsoft.github.io/multi-agent-reference-architecture/docs/governance/Governance.html | medium | cross-item synthesis |
| [inference] Semantic-layer capability depends on RDF, OWL, SPARQL, collaborative modeling, and query-time reasoning. | https://www.w3.org/TR/rdf11-concepts/; https://www.w3.org/TR/owl2-overview/; https://www.w3.org/TR/sparql11-query/; https://metaphacts.com/solutions/semantic-knowledge-modeling; https://docs.stardog.com/inference-engine/ | medium | taxonomy synthesis |
| [inference] Harvesting and extraction must include both graph construction and live virtualization. | https://arxiv.org/abs/2404.16130; https://docs.stardog.com/virtual-graphs/; https://davidamitchell.github.io/Research/research/2026-05-12-knowledge-graph-lifecycle-management-agentic.html | medium | complementary patterns |
| [inference] Runtime context and memory capability is best modeled through just-in-time retrieval, checkpointing, short-term state, long-term memory, and interrupts. | https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents; https://docs.langchain.com/oss/python/langgraph/durable-execution; https://docs.langchain.com/oss/python/langgraph/persistence; https://docs.langchain.com/oss/python/concepts/memory; https://docs.langchain.com/oss/python/langgraph/interrupts | medium | runtime synthesis |
| [inference] Orchestration maturity progresses toward planner or supervisor coordination with worker specialization. | https://www.anthropic.com/research/building-effective-agents; https://microsoft.github.io/multi-agent-reference-architecture/docs/reference-architecture/Reference-Architecture.html; https://smart-pucrs.github.io/publications/pdf/ao2017ArturFreitas.pdf | medium | architecture synthesis |
| [inference] Interoperability is a distinct capability domain because semantic and tool standards solve different interfaces. | https://www.w3.org/TR/rdf11-concepts/; https://www.w3.org/TR/owl2-overview/; https://www.w3.org/TR/sparql11-query/; https://modelcontextprotocol.io/introduction; https://modelcontextprotocol.io/docs/learn/architecture | medium | taxonomy synthesis |
| [inference] The minimum operating model needs five role families across modeling, runtime, governance, and improvement. | https://metaphacts.com/solutions/semantic-knowledge-modeling; https://microsoft.github.io/multi-agent-reference-architecture/docs/governance/Governance.html; https://cmmiinstitute.com/learning/appraisals/levels | medium | role synthesis |
| [inference] A five-level maturity rubric is the most practical staging model for SKM capability growth. | https://cmmiinstitute.com/learning/appraisals/levels; https://docs.langchain.com/oss/python/langgraph/persistence; https://docs.stardog.com/inference-engine/; https://microsoft.github.io/multi-agent-reference-architecture/docs/governance/Governance.html | medium | adapted staging |

**Assumptions**

- [assumption] Public product and framework documentation is adequate for capability taxonomy even when it does not provide comparative benchmark data, because this item asks what capabilities and patterns exist, not which vendor performs best.[source: https://metaphacts.com/solutions/semantic-knowledge-modeling; https://docs.stardog.com/virtual-graphs/; https://docs.langchain.com/oss/python/langgraph/overview; https://microsoft.github.io/multi-agent-reference-architecture/docs/reference-architecture/Reference-Architecture.html]
- [assumption] Translating the requested "repeatable" maturity label to the project-level control stage represented by CMMI's managed practices is acceptable for this item, because the operational difference that matters here is project-local repeatability versus organization-wide governed practice.[source: https://cmmiinstitute.com/learning/appraisals/levels]

**Analysis**

- [inference] The cleanest architecture boundary is to treat the semantic layer as the authoritative structure for meaning and traceability, while the orchestration layer owns routing, planning, state persistence, and tool invocation.[source: https://docs.stardog.com/inference-engine/; https://docs.langchain.com/oss/python/langgraph/overview; https://microsoft.github.io/multi-agent-reference-architecture/docs/reference-architecture/Reference-Architecture.html]
- [inference] This boundary explains why SKM systems need both ontology-native capabilities and agent-runtime capabilities, because semantic correctness does not automatically provide resumability, approval flows, or fault-tolerant task execution.[source: https://www.w3.org/TR/owl2-overview/; https://docs.langchain.com/oss/python/langgraph/durable-execution; https://docs.langchain.com/oss/python/langgraph/interrupts]
- [inference] The capability hierarchy is therefore best interpreted as a control-surface map: acquisition governs what enters the system, semantic operations govern what it means, runtime context governs what is currently visible, orchestration governs what acts next, interoperability governs what can be connected, and governance governs what is allowed and improved.[source: https://arxiv.org/abs/2404.16130; https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents; https://modelcontextprotocol.io/docs/learn/architecture; https://microsoft.github.io/multi-agent-reference-architecture/docs/governance/Governance.html]
- [inference] The maturity rubric follows this same logic, because organizations move from isolated technical features toward integrated controls, durable state, cross-functional roles, and measurable improvement rather than simply adding more tools or more semantic expressiveness.[source: https://cmmiinstitute.com/learning/appraisals/levels; https://docs.langchain.com/oss/python/langgraph/persistence; https://microsoft.github.io/multi-agent-reference-architecture/docs/governance/Governance.html]

**Risks, gaps, uncertainties**

- [inference] Public evidence on semantic and runtime capabilities is materially stronger than public evidence on classic KM capability taxonomies, so the semantic and orchestration parts of the model are better supported than the legacy-KM comparison layer.[source: https://cmmiinstitute.com/learning/appraisals/levels; https://www.w3.org/TR/rdf11-concepts/; https://www.anthropic.com/research/building-effective-agents]
- [inference] Vendor platform pages establish feature surfaces but not comparative effectiveness, so choices about which sub-capability bundles matter most in production still require environment-specific validation.[source: https://metaphacts.com/solutions/semantic-knowledge-modeling; https://docs.stardog.com/virtual-graphs/]
- [inference] The sources describe checkpointed state, durable identifiers, and retrievable long-term memory primitives, but they do not converge on one canonical term for that bundle, so this item uses plain language rather than claiming a settled industry label.[source: https://docs.langchain.com/oss/python/langgraph/persistence; https://docs.langchain.com/oss/python/concepts/memory; https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents]

**Open questions**

- Which metrics best measure SKM semantic quality at runtime, beyond generic latency and failure metrics?
- What is the lightest-weight governance pattern that still preserves auditability for low-risk internal SKM agents?
- How should graph-derived summaries be invalidated when source documents change frequently?
- Which benchmark or case-study design would best test whether the six-domain model predicts better production outcomes than a simpler five-pillar variant?

### §7 Recursive Review

review_result: pass

acronym_audit: passed

domain_term_audit: passed

claim_label_audit: passed

source_url_audit: passed

findings_synthesis_parity: passed

prior_work_rescan: completed

confidence: medium

---

## Findings

### Executive Summary

Tool-using, semi-autonomous Semantic Knowledge Management (SKM) systems require six separable capability domains, and this six-domain structure is best read as an extension of the earlier repository five-pillar model, because it splits knowledge foundations into acquisition versus semantic operations and promotes interoperability and discovery to an explicit control surface.[inference; source: https://davidamitchell.github.io/Research/research/2026-05-20-agentic-km-5-pillar-capability-model.html; https://arxiv.org/abs/2404.16130; https://modelcontextprotocol.io/docs/learn/architecture; https://microsoft.github.io/multi-agent-reference-architecture/docs/governance/Governance.html]

The recurring architecture is a layered stack in which harvested or virtualized sources feed an RDF and OWL semantic layer queried through SPARQL, while an orchestrator manages dynamic capability discovery, checkpointed state, memory recall, and tool invocation through open protocols such as MCP.[inference; source: https://docs.stardog.com/virtual-graphs/; https://docs.stardog.com/inference-engine/; https://www.w3.org/TR/rdf11-concepts/; https://www.w3.org/TR/owl2-overview/; https://www.w3.org/TR/sparql11-query/; https://modelcontextprotocol.io/docs/learn/architecture; https://microsoft.github.io/multi-agent-reference-architecture/docs/reference-architecture/Reference-Architecture.html]

Practical maturity increases when teams move from manual and static practices to versioned semantic models, persistent and interruptible runtime state, governed discovery, and quantitative improvement loops adapted from Capability Maturity Model Integration (CMMI) staging.[inference; source: https://cmmiinstitute.com/learning/appraisals/levels; https://docs.langchain.com/oss/python/langgraph/persistence; https://microsoft.github.io/multi-agent-reference-architecture/docs/governance/Governance.html]

The evidence base is strongest for semantic, orchestration, and governance capabilities, and weaker for publicly accessible classical Knowledge Management (KM) taxonomies, so the resulting hierarchy is best treated as a medium-confidence synthesis rather than a settled industry standard.[inference; source: https://cmmiinstitute.com/learning/appraisals/levels; https://www.w3.org/TR/rdf11-concepts/; https://www.anthropic.com/research/building-effective-agents; https://davidamitchell.github.io/Research/research/2026-05-20-agentic-km-5-pillar-capability-model.html]

### Key Findings

1. **The minimum complete SKM model needs six top-level capability domains, and this is a bounded extension of the earlier five-pillar repository model, because acquisition versus semantic operations and interoperability versus orchestration expose materially different control surfaces, failure modes, and ownership boundaries.** ([inference]; medium confidence; source: https://davidamitchell.github.io/Research/research/2026-05-20-agentic-km-5-pillar-capability-model.html; https://arxiv.org/abs/2404.16130; https://modelcontextprotocol.io/docs/learn/architecture; https://microsoft.github.io/multi-agent-reference-architecture/docs/governance/Governance.html)
2. **Semantic-layer maturity depends on explicit RDF datasets, OWL ontologies, SPARQL query surfaces, collaborative semantic modeling, and query-time reasoning or validation, because these capabilities recur across standards and enterprise semantic platforms and collectively define the semantic control surface of an SKM system.** ([inference]; medium confidence; source: https://www.w3.org/TR/rdf11-concepts/; https://www.w3.org/TR/owl2-overview/; https://www.w3.org/TR/sparql11-query/; https://metaphacts.com/solutions/semantic-knowledge-modeling; https://docs.stardog.com/inference-engine/)
3. **Harvesting and extraction capability must cover both document-derived graph construction and live source virtualization, because GraphRAG-style pipelines and Stardog-style virtual graphs solve complementary parts of the knowledge acquisition problem.** ([inference]; medium confidence; source: https://arxiv.org/abs/2404.16130; https://docs.stardog.com/virtual-graphs/; https://davidamitchell.github.io/Research/research/2026-05-12-knowledge-graph-lifecycle-management-agentic.html)
4. **Dynamic context and memory capability is best modeled through just-in-time retrieval, thread-scoped short-term state, namespace-scoped long-term memory, checkpointed replay, and resumable interrupts, because those primitives together cover the runtime state-management problems described in current context-engineering and orchestration documentation.** ([inference]; medium confidence; source: https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents; https://docs.langchain.com/oss/python/langgraph/durable-execution; https://docs.langchain.com/oss/python/langgraph/persistence; https://docs.langchain.com/oss/python/concepts/memory; https://docs.langchain.com/oss/python/langgraph/interrupts)
5. **Reasoning and orchestration maturity is marked by progression from fixed workflows to planner or supervisor coordination with worker specialization, because public agent guidance and reference architectures repeatedly separate routing, decomposition, supervision, and recovery concerns.** ([inference]; medium confidence; source: https://www.anthropic.com/research/building-effective-agents; https://microsoft.github.io/multi-agent-reference-architecture/docs/reference-architecture/Reference-Architecture.html; https://smart-pucrs.github.io/publications/pdf/ao2017ArturFreitas.pdf)
6. **Interoperability should be treated as a first-class capability domain, because usable SKM systems need both semantic standards for data and discovery standards for tools, with MCP exposing discoverable tools, resources, and prompts through explicit list and get methods.** ([inference]; medium confidence; source: https://www.w3.org/TR/rdf11-concepts/; https://www.w3.org/TR/owl2-overview/; https://www.w3.org/TR/sparql11-query/; https://modelcontextprotocol.io/introduction; https://modelcontextprotocol.io/docs/learn/architecture)
7. **The minimum operating model requires domain owners, ontology and knowledge engineers, orchestration and platform engineers, governance and evaluation owners, and formal improvement roles, because semantic modeling, runtime control, and maturity assurance are documented as different human workstreams.** ([inference]; medium confidence; source: https://metaphacts.com/solutions/semantic-knowledge-modeling; https://microsoft.github.io/multi-agent-reference-architecture/docs/governance/Governance.html; https://cmmiinstitute.com/learning/appraisals/levels)
8. **A practical maturity rubric for SKM systems runs from Initial through Repeatable, Managed, Quantitatively Managed, and Optimizing, with the transitions driven by versioned semantics, persistent runtime state, governed discovery, and measurable control loops rather than by model size alone.** ([inference]; medium confidence; source: https://cmmiinstitute.com/learning/appraisals/levels; https://docs.langchain.com/oss/python/langgraph/persistence; https://docs.stardog.com/inference-engine/; https://microsoft.github.io/multi-agent-reference-architecture/docs/governance/Governance.html)

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [inference] SKM requires six top-level capability domains as an extension of the earlier five-pillar repository model. | https://davidamitchell.github.io/Research/research/2026-05-20-agentic-km-5-pillar-capability-model.html; https://arxiv.org/abs/2404.16130; https://modelcontextprotocol.io/docs/learn/architecture; https://microsoft.github.io/multi-agent-reference-architecture/docs/governance/Governance.html | medium | cross-item synthesis |
| [inference] Semantic-layer capability depends on RDF, OWL, SPARQL, collaborative modeling, and query-time reasoning. | https://www.w3.org/TR/rdf11-concepts/; https://www.w3.org/TR/owl2-overview/; https://www.w3.org/TR/sparql11-query/; https://metaphacts.com/solutions/semantic-knowledge-modeling; https://docs.stardog.com/inference-engine/ | medium | taxonomy synthesis |
| [inference] Harvesting and extraction must include both graph construction and live virtualization. | https://arxiv.org/abs/2404.16130; https://docs.stardog.com/virtual-graphs/; https://davidamitchell.github.io/Research/research/2026-05-12-knowledge-graph-lifecycle-management-agentic.html | medium | complementary patterns |
| [inference] Runtime context and memory capability is best modeled through just-in-time retrieval, checkpointing, short-term state, long-term memory, and interrupts. | https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents; https://docs.langchain.com/oss/python/langgraph/durable-execution; https://docs.langchain.com/oss/python/langgraph/persistence; https://docs.langchain.com/oss/python/concepts/memory; https://docs.langchain.com/oss/python/langgraph/interrupts | medium | runtime synthesis |
| [inference] Orchestration maturity progresses toward planner or supervisor coordination with worker specialization. | https://www.anthropic.com/research/building-effective-agents; https://microsoft.github.io/multi-agent-reference-architecture/docs/reference-architecture/Reference-Architecture.html; https://smart-pucrs.github.io/publications/pdf/ao2017ArturFreitas.pdf | medium | architecture synthesis |
| [inference] Interoperability is a distinct capability domain because semantic and tool standards solve different interfaces. | https://www.w3.org/TR/rdf11-concepts/; https://www.w3.org/TR/owl2-overview/; https://www.w3.org/TR/sparql11-query/; https://modelcontextprotocol.io/introduction; https://modelcontextprotocol.io/docs/learn/architecture | medium | taxonomy synthesis |
| [inference] The minimum operating model needs five role families across modeling, runtime, governance, and improvement. | https://metaphacts.com/solutions/semantic-knowledge-modeling; https://microsoft.github.io/multi-agent-reference-architecture/docs/governance/Governance.html; https://cmmiinstitute.com/learning/appraisals/levels | medium | role synthesis |
| [inference] A five-level maturity rubric is the most practical staging model for SKM capability growth. | https://cmmiinstitute.com/learning/appraisals/levels; https://docs.langchain.com/oss/python/langgraph/persistence; https://docs.stardog.com/inference-engine/; https://microsoft.github.io/multi-agent-reference-architecture/docs/governance/Governance.html | medium | adapted staging |

### Assumptions

- **Assumption:** Public product and framework documentation is adequate for capability taxonomy even when it does not provide comparative benchmark data. **Justification:** This item asks what capabilities and patterns exist, not which vendor performs best. [assumption; source: https://metaphacts.com/solutions/semantic-knowledge-modeling; https://docs.stardog.com/virtual-graphs/; https://docs.langchain.com/oss/python/langgraph/overview; https://microsoft.github.io/multi-agent-reference-architecture/docs/reference-architecture/Reference-Architecture.html]
- **Assumption:** Translating the requested "repeatable" maturity label to the project-level control stage represented by CMMI's managed practices is acceptable for this item. **Justification:** The operational difference that matters here is project-local repeatability versus organization-wide governed practice. [assumption; source: https://cmmiinstitute.com/learning/appraisals/levels]

### Analysis

The cleanest architecture boundary is to treat the semantic layer as the authoritative structure for meaning and traceability, while the orchestration layer owns routing, planning, state persistence, and tool invocation.[inference; source: https://docs.stardog.com/inference-engine/; https://docs.langchain.com/oss/python/langgraph/overview; https://microsoft.github.io/multi-agent-reference-architecture/docs/reference-architecture/Reference-Architecture.html]

This boundary explains why SKM systems need both ontology-native capabilities and agent-runtime capabilities, because semantic correctness does not automatically provide resumability, approval flows, or fault-tolerant task execution.[inference; source: https://www.w3.org/TR/owl2-overview/; https://docs.langchain.com/oss/python/langgraph/durable-execution; https://docs.langchain.com/oss/python/langgraph/interrupts]

The minimum complete hierarchy is therefore: knowledge acquisition and extraction; semantic modeling and graph operations; runtime context and memory; reasoning and orchestration; interoperability and discovery; governance with continuous improvement.[inference; source: https://arxiv.org/abs/2404.16130; https://www.w3.org/TR/rdf11-concepts/; https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents; https://modelcontextprotocol.io/docs/learn/architecture; https://microsoft.github.io/multi-agent-reference-architecture/docs/governance/Governance.html]

The core sub-capabilities under those domains are source registration, harvesting, parsing, semantic normalization, provenance capture, ontology and taxonomy design, mapping and virtualization, validation and reasoning, query and federation, checkpointed thread state, long-term memory stores, routing, decomposition, worker supervision, registry-mediated discovery, open capability description, approval controls, evaluation, and formal improvement loops.[inference; source: https://arxiv.org/abs/2404.16130; https://docs.stardog.com/virtual-graphs/; https://docs.langchain.com/oss/python/langgraph/persistence; https://modelcontextprotocol.io/docs/learn/architecture; https://microsoft.github.io/multi-agent-reference-architecture/docs/governance/Governance.html]

The adapted maturity rubric is: Initial, static documents and manual graph updates with no durable runtime state; Repeatable, scheduled ingestion and explicit schema or tool catalogs; Managed, organization-wide semantic standards, versioned graph lifecycle, checkpointed orchestration, and role separation; Quantitatively Managed, service levels and metrics for freshness, latency, failure, and evaluation quality; Optimizing, dynamic discovery, automated quality checks, and continuous human-supervised improvement.[inference; source: https://cmmiinstitute.com/learning/appraisals/levels; https://docs.langchain.com/oss/python/langgraph/persistence; https://docs.stardog.com/inference-engine/; https://microsoft.github.io/multi-agent-reference-architecture/docs/governance/Governance.html]

### Risks, Gaps, and Uncertainties

Public evidence on semantic and runtime capabilities is materially stronger than public evidence on classic KM capability taxonomies, so the semantic and orchestration parts of the model are better supported than the legacy-KM comparison layer.[inference; source: https://cmmiinstitute.com/learning/appraisals/levels; https://www.w3.org/TR/rdf11-concepts/; https://www.anthropic.com/research/building-effective-agents]

Vendor platform pages establish feature surfaces but not comparative effectiveness, so choices about which sub-capability bundles matter most in production still require environment-specific validation.[inference; source: https://metaphacts.com/solutions/semantic-knowledge-modeling; https://docs.stardog.com/virtual-graphs/]

The sources describe checkpointed state, durable identifiers, and retrievable long-term memory primitives, but they do not converge on one canonical term for that bundle, so this item uses plain language rather than claiming a settled industry label.[inference; source: https://docs.langchain.com/oss/python/langgraph/persistence; https://docs.langchain.com/oss/python/concepts/memory; https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents]

### Open Questions

- Which metrics best measure SKM semantic quality at runtime, beyond generic latency and failure metrics?
- What is the lightest-weight governance pattern that still preserves auditability for low-risk internal SKM agents?
- How should graph-derived summaries be invalidated when source documents change frequently?
- Which benchmark or case-study design would best test whether the six-domain model predicts better production outcomes than a simpler five-pillar variant?

---

## Output

- Type: knowledge
- Description: Capability hierarchy and maturity rubric for tool-using, semi-autonomous Semantic Knowledge Management systems, grounded in semantic-web standards, agent-runtime documentation, and adjacent repository synthesis.[inference; source: https://www.w3.org/TR/rdf11-concepts/; https://docs.langchain.com/oss/python/langgraph/overview; https://davidamitchell.github.io/Research/research/2026-05-20-agentic-km-5-pillar-capability-model.html]
- Links:
  - https://www.w3.org/TR/rdf11-concepts/
  - https://modelcontextprotocol.io/docs/learn/architecture
  - https://docs.langchain.com/oss/python/langgraph/persistence
