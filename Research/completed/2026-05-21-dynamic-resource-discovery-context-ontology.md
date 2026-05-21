---
review_count: 2
title: "What is the Dynamic Resource Discovery architecture pattern in multi-agent systems, how does it relate to context engineering, and what design patterns enable agents to retrieve semantically relevant context from an ontological database?"
added: 2026-05-21T10:31:30+00:00
status: completed
priority: high
blocks: []
tags: [dynamic-resource-discovery, context-engineering, ontology, knowledge-graph, agentic-ai, mcp, model-context-protocol, agent-architecture, semantic-retrieval, rag]
started: 2026-05-21T11:01:36+00:00
completed: 2026-05-21T11:35:04+00:00
output: [knowledge]
cites:
  - 2026-03-08-context-engineering-first-principles
  - 2026-03-18-api-context-hubs-rag-mcp
  - 2026-05-15-ontology-landscape-for-curated-enterprise-context
  - 2026-03-03-knowledge-representation-agent-context
  - 2026-05-12-knowledge-graph-agentic-runtime-dependency
related:
  - 2026-03-22-applied-context-engineering-agent-workflows
  - 2026-04-29-knowledge-scaffolding-context-engineering
  - 2026-05-12-graph-db-saas-knowledge-ontology
superseded_by: ~
supersedes: ~
item_type: primary
confidence: medium
versions:
  - version: "1.0"
    sha: "79134fc4d86d283ad65975659353bce5a7e4a0a2"
    changed: 2026-05-21
    progress: progress/2026-05-21-dynamic-resource-discovery-context-ontology.md
    summary: "Initial completion"
---

# What is the Dynamic Resource Discovery architecture pattern in multi-agent systems, how does it relate to context engineering, and what design patterns enable agents to retrieve semantically relevant context from an ontological database?

## Research Question

What is the Dynamic Resource Discovery (DRD) architecture pattern in multi-agent systems, how does it relate to context engineering, meaning the design of what information enters an agent's working context at inference time, and what design patterns enable agents to retrieve semantically relevant context from an ontological database, informing the design of an agent context layer that scales to large, structured enterprise knowledge stores?

## Scope

**In scope:**
- Definition and core components of the DRD architecture pattern in distributed and agentic systems, including registries, discovery protocols, capability descriptors, and resource advertisements.
- Relationship between DRD and context engineering techniques, including relevance filtering, progressive disclosure, and intent injection.
- Query and integration patterns for ontological databases: SPARQL (SPARQL Protocol and RDF Query Language), Resource Description Framework (RDF) and Web Ontology Language (OWL) graph traversal, embedding-over-ontology, and hybrid retrieval.
- Model Context Protocol (MCP) and similar agent resource protocols as concrete instantiations of DRD.
- Reference architectures that integrate DRD with ontological context stores in agentic pipelines.
- Latency, coherence, and token-budget trade-offs of dynamic discovery versus pre-loaded static context.

**Out of scope:**
- Production implementation or code for this repository.
- Vendor-specific procurement recommendations for ontological database products.
- Detailed ontology modeling, including taxonomy design and OWL axiom engineering, independent of retrieval.
- Agent planning and reasoning mechanisms not directly coupled to context access.
- Jurisdiction-specific legal or compliance considerations.

**Constraints:** Prefer sources from 2022 onward where possible, but use older standards where they remain canonical. Focus on published architectural patterns, specifications, and empirical evaluations. Produce a knowledge output. Every source must include a Uniform Resource Locator (URL).

## Context

The design problem is how an agent system should discover and retrieve relevant context at runtime from a structured semantic store instead of relying on pre-loaded or statically configured context.[fact; source: https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents; https://modelcontextprotocol.io/docs/learn/architecture]

The decision matters because the context layer must balance semantic precision, freshness, latency, and finite working-context capacity when the underlying knowledge store is large and continuously changing.[inference; source: https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents; https://arxiv.org/abs/2302.00093; https://davidamitchell.github.io/Research/research/2026-05-15-ontology-landscape-for-curated-enterprise-context.html]

## Approach

1. **Define Dynamic Resource Discovery (DRD) as an architecture pattern.**
   1a. What definition is justified for DRD across distributed and agentic systems, and what problem does it solve compared to static resource configuration?
   1b. What are DRD's core structural components: registries, discovery protocols, capability descriptors, and advertisement mechanisms?
   1c. How does MCP or similar agent tooling instantiate DRD principles in practice?

2. **Map the relationship between DRD and context engineering.**
   2a. How does DRD feed dynamically discovered resources into an agent's working context window?
   2b. Which context engineering techniques depend on or are enabled by DRD?
   2c. What are the latency, coherence, and token-budget trade-offs of dynamic discovery versus pre-loaded or cached context?

3. **Identify patterns for agent access to ontological databases.**
   3a. What query and traversal patterns enable semantic retrieval from an ontological store?
   3b. How is relevance ranked and filtered when pulling context from an ontology at runtime?
   3c. What integration architectures connect DRD, the ontological database, and the agent context pipeline end-to-end?

4. **Synthesize a unified reference architecture.**
   4a. What published architectures demonstrate DRD combined with ontological or graph-backed context stores in an agentic pipeline?
   4b. What failure modes, operational risks, and scaling constraints arise in this integrated architecture?

## Sources

- [x] [Model Context Protocol What is the Model Context Protocol (MCP)?](https://modelcontextprotocol.io/introduction)
- [x] [Model Context Protocol Architecture overview](https://modelcontextprotocol.io/docs/learn/architecture)
- [x] [Model Context Protocol The MCP Registry](https://modelcontextprotocol.io/registry/about)
- [x] [Anthropic Effective context engineering for AI agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)
- [x] [World Wide Web Consortium (W3C) SPARQL 1.1 Query Language](https://www.w3.org/TR/sparql11-query/)
- [x] [W3C RDF 1.1 Concepts and Abstract Syntax](https://www.w3.org/TR/rdf11-concepts/)
- [x] [W3C OWL 2 Web Ontology Language Document Overview](https://www.w3.org/TR/owl2-overview/)
- [x] [Guttman et al. (1999) Service Location Protocol, Version 2](https://datatracker.ietf.org/doc/html/rfc2608)
- [x] [Cheshire and Krochmal (2013) DNS-Based Service Discovery](https://datatracker.ietf.org/doc/html/rfc6763)
- [x] [Organisation for the Advancement of Structured Information Standards (OASIS) Web Services Dynamic Discovery 1.1](https://docs.oasis-open.org/ws-dd/discovery/1.1/wsdd-discovery-1.1-spec.html)
- [x] [Edge et al. (2024) From Local to Global: A GraphRAG Approach to Query-Focused Summarization](https://arxiv.org/abs/2404.16130)
- [x] [Chen et al. (2023) Large Language Models Can Be Easily Distracted by Irrelevant Context](https://arxiv.org/abs/2302.00093)
- [x] [Mehta et al. (2024) HybridRAG: Integrating Knowledge Graphs and Vector Retrieval Augmented Generation for Efficient Information Extraction](https://arxiv.org/abs/2408.04948)
- [x] [Lee et al. (2025) HybGRAG: Hybrid Retrieval-Augmented Generation on Textual and Relational Knowledge Bases](https://aclanthology.org/2025.acl-long.43/)
- [x] [Mitchell (2026) Context engineering: first principles of steering Large Language Model output without control](https://davidamitchell.github.io/Research/research/2026-03-08-context-engineering-first-principles.html)
- [x] [Mitchell (2026) Application Programming Interface context hubs, Retrieval-Augmented Generation, and the Model Context Protocol: how agents discover and use APIs](https://davidamitchell.github.io/Research/research/2026-03-18-api-context-hubs-rag-mcp.html)
- [x] [Mitchell (2026) Knowledge Representation for Agent Context: Latent Semantic Extraction, Knowledge Graphs, Concept Maps, and Document Compression for Large-Scale Context Management](https://davidamitchell.github.io/Research/research/2026-03-03-knowledge-representation-agent-context.html)
- [x] [Mitchell (2026) Ontology landscape for curated lexical and structured enterprise context](https://davidamitchell.github.io/Research/research/2026-05-15-ontology-landscape-for-curated-enterprise-context.html)
- [x] [Mitchell (2026) Knowledge Graph in the live execution path of multi-step Large Language Model systems: architecture and failure modes](https://davidamitchell.github.io/Research/research/2026-05-12-knowledge-graph-agentic-runtime-dependency.html)

---

## Research Skill Output

*(Full output from running the research skill, retained verbatim in the completed item. Sections §0 to §5 are the investigation, and §6 seeds the Findings section below.)*

### §0 Initialise

question: determine whether DRD is a coherent cross-system architecture pattern, how it composes with context engineering, and what retrieval patterns best connect agent runtimes to ontological stores.

scope: discovery architecture, context assembly, ontological retrieval, and runtime trade-offs are in scope; ontology authoring, procurement, and jurisdiction-specific compliance are out of scope.

constraints: full-mode research, URL-backed sources only, empirical and standards-based evidence preferred, and older standards allowed where they remain canonical.

output_format: full research record with synthesis mirrored into Findings.

mode: full

- [inference] The most relevant prior completed items are Mitchell (2026) on context engineering first principles, Mitchell (2026) on Application Programming Interface (API) context hubs, Retrieval-Augmented Generation (RAG), and MCP, Mitchell (2026) on ontology landscape for curated enterprise context, Mitchell (2026) on knowledge representation for agent context, and Mitchell (2026) on runtime Knowledge Graph dependencies, because they respectively cover finite attention budgets, tool and protocol discovery, ontology-layer trade-offs, layered retrieval, and runtime graph failure modes.[source: https://davidamitchell.github.io/Research/research/2026-03-08-context-engineering-first-principles.html; https://davidamitchell.github.io/Research/research/2026-03-18-api-context-hubs-rag-mcp.html; https://davidamitchell.github.io/Research/research/2026-05-15-ontology-landscape-for-curated-enterprise-context.html; https://davidamitchell.github.io/Research/research/2026-03-03-knowledge-representation-agent-context.html; https://davidamitchell.github.io/Research/research/2026-05-12-knowledge-graph-agentic-runtime-dependency.html]

### §1 Question Decomposition

- A. DRD as a pattern
  - A1. Is DRD a formally named standard, or a synthesis across existing discovery protocols?
  - A2. Which primitives recur across discovery systems?
  - A3. What problem does runtime discovery solve that static configuration does not?
- B. DRD in agent systems
  - B1. Which parts of MCP implement discovery after connection?
  - B2. Which parts of the MCP Registry implement discovery before connection?
  - B3. How do these map onto older discovery systems such as Service Location Protocol (SLP), DNS-Based Service Discovery (DNS-SD), and Web Services Dynamic Discovery (WS-Discovery)?
- C. DRD and context engineering
  - C1. Where does discovery stop and context assembly begin?
  - C2. Which context-engineering techniques require dynamic retrieval rather than static preload?
  - C3. What are the latency and token-budget trade-offs?
- D. Ontological retrieval patterns
  - D1. What do RDF, OWL, and SPARQL contribute to runtime retrieval?
  - D2. When do graph-only, vector-only, and hybrid retrieval each fit?
  - D3. How should relevance be ranked for runtime use?
- E. Reference architecture and risks
  - E1. What layered reference architecture best fits the evidence?
  - E2. Which failure modes dominate in production?
  - E3. What remains unresolved or weakly specified?

### §2 Investigation

#### 2.1 DRD as a cross-system pattern rather than a single named standard

- [fact] SLP defines a scalable framework for discovery and selection of network services, using User Agents, Service Agents, Directory Agents, service types, attributes, and scopes so hosts need little or no static network-service configuration.[source: https://datatracker.ietf.org/doc/html/rfc2608]
- [fact] DNS-SD defines a way for clients to discover named service instances by querying standard Domain Name System (DNS) records, with Service Records (SRV) and Text Records (TXT) carrying endpoint location and structured key-value metadata.[source: https://datatracker.ietf.org/doc/html/rfc6763]
- [fact] WS-Discovery defines a discovery protocol in which target services announce themselves, clients probe or resolve for services, and discovery proxies shift the system from ad hoc multicast discovery to managed unicast discovery.[source: https://docs.oasis-open.org/ws-dd/discovery/1.1/wsdd-discovery-1.1-spec.html]
- [inference] The consulted standards do not present "Dynamic Resource Discovery" as one canonical named protocol family; instead, they expose a recurring architecture pattern composed of advertisement, searchable metadata, selection, and late binding.[source: https://datatracker.ietf.org/doc/html/rfc2608; https://datatracker.ietf.org/doc/html/rfc6763; https://docs.oasis-open.org/ws-dd/discovery/1.1/wsdd-discovery-1.1-spec.html]
- [inference] Because these standards emerged from different technical communities yet still reuse the same discovery surfaces and late-binding flow, the item treats them as a recurrent architectural pattern while leaving open whether that similarity reflects deeper architectural convergence or repeated responses to similar discovery constraints.[source: https://datatracker.ietf.org/doc/html/rfc2608; https://datatracker.ietf.org/doc/html/rfc6763; https://docs.oasis-open.org/ws-dd/discovery/1.1/wsdd-discovery-1.1-spec.html]
- [inference] A defensible working definition is therefore: DRD is the architecture pattern in which resources or services expose discoverable capability metadata at runtime, allowing clients or agents to select and bind to relevant resources without relying on fully static configuration.[source: https://datatracker.ietf.org/doc/html/rfc2608; https://datatracker.ietf.org/doc/html/rfc6763; https://docs.oasis-open.org/ws-dd/discovery/1.1/wsdd-discovery-1.1-spec.html; https://modelcontextprotocol.io/docs/learn/architecture]

#### 2.2 The structural primitives that recur across discovery systems

- [fact] SLP explicitly separates User Agents, Service Agents, and Directory Agents, and defines service attributes and scopes as search surfaces.[source: https://datatracker.ietf.org/doc/html/rfc2608]
- [fact] DNS-SD uses instance enumeration plus structured TXT metadata, and WS-Discovery uses Hello, Bye, Probe, Resolve, Types, Scopes, Metadata, and Discovery Proxies.[source: https://datatracker.ietf.org/doc/html/rfc6763; https://docs.oasis-open.org/ws-dd/discovery/1.1/wsdd-discovery-1.1-spec.html]
- [fact] MCP exposes dynamic lists of tools, resources, and prompts after connection, and the MCP Registry stores standardized server metadata including unique name, location, execution instructions, environment variables, and capability data.[source: https://modelcontextprotocol.io/docs/learn/architecture; https://modelcontextprotocol.io/registry/about]
- [inference] Across these systems, four primitives recur: a discovery surface or registry, a machine-readable capability descriptor, a lookup or advertisement mechanism, and a late-binding execution path from selection to use.[source: https://datatracker.ietf.org/doc/html/rfc2608; https://datatracker.ietf.org/doc/html/rfc6763; https://docs.oasis-open.org/ws-dd/discovery/1.1/wsdd-discovery-1.1-spec.html; https://modelcontextprotocol.io/docs/learn/architecture; https://modelcontextprotocol.io/registry/about]

#### 2.3 How MCP instantiates DRD for agentic systems

- [fact] MCP uses a client-server architecture in which an MCP host establishes one client connection per MCP server, and servers expose tools, resources, and prompts through JavaScript Object Notation Remote Procedure Call (JSON-RPC) 2.0 methods for listing, retrieval, and execution.[source: https://modelcontextprotocol.io/docs/learn/architecture]
- [fact] MCP explicitly supports dynamic listing, meaning clients can ask a server what primitives are currently available rather than relying on a fully pre-baked local prompt catalog.[source: https://modelcontextprotocol.io/docs/learn/architecture]
- [fact] The MCP Registry is an official centralized metadata repository for publicly accessible MCP servers and provides a Representational State Transfer (REST) API for downstream registries and aggregators to discover available servers, their installation methods, and server capabilities.[source: https://modelcontextprotocol.io/registry/about]
- [fact] The introductory MCP documentation positions the protocol as a standardized way for Artificial Intelligence (AI) applications to connect to external data sources, tools, and workflows.[source: https://modelcontextprotocol.io/introduction]
- [inference] MCP therefore instantiates DRD at two levels: pre-connection server discovery through registry metadata, and post-connection primitive discovery through `*/list` methods.[source: https://modelcontextprotocol.io/registry/about; https://modelcontextprotocol.io/docs/learn/architecture]
- [inference] MCP applies a structurally similar discovery logic to context-bearing and action-bearing primitives that an agent can immediately incorporate into its deliberation loop, rather than only to endpoint location.[source: https://modelcontextprotocol.io/docs/learn/architecture; https://modelcontextprotocol.io/introduction]

#### 2.4 Where DRD ends and context engineering begins

- [fact] Anthropic defines context engineering as curating and maintaining the optimal set of tokens during Large Language Model (LLM) inference, including prompts, tools, external data, and history.[source: https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents]
- [fact] Anthropic's runtime pattern for capable agents is "just in time" retrieval: keep lightweight identifiers such as file paths, stored queries, or links, then dynamically load data into context only when needed.[source: https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents]
- [fact] The same Anthropic source says progressive disclosure lets agents incrementally discover relevant context through exploration, assembling only what is necessary in working memory.[source: https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents]
- [fact] Chen et al. show that irrelevant context materially degrades LLM task performance, which makes relevance filtering a correctness concern rather than only an efficiency concern.[source: https://arxiv.org/abs/2302.00093]
- [inference] DRD solves the "what can I access now?" problem, while context engineering solves the downstream "what subset should actually enter the finite working context now?" problem.[source: https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents; https://modelcontextprotocol.io/docs/learn/architecture; https://arxiv.org/abs/2302.00093]
- [inference] Progressive disclosure, relevance filtering, and hierarchical compaction form the control layer that makes DRD useful under finite context windows.[source: https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents; https://davidamitchell.github.io/Research/research/2026-03-08-context-engineering-first-principles.html]

#### 2.5 What ontological stores contribute to the pattern

- [fact] RDF defines graph-structured subject-predicate-object triples and datasets as the core semantic data model for linked resources.[source: https://www.w3.org/TR/rdf11-concepts/]
- [fact] OWL 2 provides formal semantics for classes, properties, individuals, and data values, and is designed to support ontology development and sharing on the Web.[source: https://www.w3.org/TR/owl2-overview/]
- [fact] SPARQL is the standard query language for RDF and supports graph patterns, optional clauses, property paths, subqueries, aggregation, and federation.[source: https://www.w3.org/TR/sparql11-query/]
- [inference] Ontological stores improve DRD because they make resource meaning machine-queryable through types, relations, and graph structure rather than only through lexical similarity or manually curated prose descriptions.[source: https://www.w3.org/TR/rdf11-concepts/; https://www.w3.org/TR/owl2-overview/; https://www.w3.org/TR/sparql11-query/]
- [inference] In practice, an ontological store is the semantic backing layer that turns runtime-discovered identifiers into explainable, filterable, and multi-hop retrievable context.[source: https://www.w3.org/TR/sparql11-query/; https://davidamitchell.github.io/Research/research/2026-05-15-ontology-landscape-for-curated-enterprise-context.html]

#### 2.6 Retrieval patterns over ontological stores

- [fact] GraphRAG builds an entity Knowledge Graph, creates community summaries, and improves answer diversity and comprehensiveness on corpus-level questions compared with conventional RAG baselines.[source: https://arxiv.org/abs/2404.16130]
- [fact] HybridRAG reports that retrieving context from both a vector database and a Knowledge Graph outperforms vector-only and graph-only baselines in its financial question-answering experiments.[source: https://arxiv.org/abs/2408.04948]
- [fact] HybGRAG reports that hybrid question answering over semi-structured knowledge bases benefits from combining textual and relational retrieval, using a retriever bank and critic module to improve top-1 retrieval accuracy (Hit@1) on benchmark tasks.[source: https://aclanthology.org/2025.acl-long.43/]
- [inference] These results support three recurring runtime retrieval patterns over ontological stores: graph-structured traversal for typed relations and multi-hop dependencies, vector retrieval for semantic proximity over text-rich evidence, and hybrid routing when the question mixes relational and textual signals.[source: https://arxiv.org/abs/2404.16130; https://arxiv.org/abs/2408.04948; https://aclanthology.org/2025.acl-long.43/]
- [inference] For agent runtime use, graph-only retrieval fits schema-driven or relation-heavy questions, vector-only retrieval fits thin ontologies with text-rich evidence, and hybrid retrieval fits cases where the agent needs both semantic similarity and explicit relational constraints.[source: https://arxiv.org/abs/2408.04948; https://aclanthology.org/2025.acl-long.43/; https://davidamitchell.github.io/Research/research/2026-03-03-knowledge-representation-agent-context.html]

#### 2.7 Trade-offs between dynamic discovery and pre-loaded static context

- [fact] Anthropic states directly that runtime exploration is slower than retrieving pre-computed data, and that agents need the right tools and heuristics or they will waste context through poor exploration.[source: https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents]
- [fact] Anthropic also recommends hybrid strategies in which some data is retrieved up front for speed while deeper exploration remains available on demand.[source: https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents]
- [fact] Mitchell (2026) on API context hubs, Retrieval-Augmented Generation (RAG), and MCP distinguished prompt-time documentation loading, retrieval-time selection, and runtime protocol invocation as separate design layers rather than interchangeable solutions.[source: https://davidamitchell.github.io/Research/research/2026-03-18-api-context-hubs-rag-mcp.html]
- [inference] Static preload optimizes latency but degrades semantic precision and token efficiency as the available resource set grows, while DRD optimizes freshness and selectivity but introduces lookup latency, ranking dependence, and more operational surfaces that can fail.[source: https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents; https://arxiv.org/abs/2302.00093; https://davidamitchell.github.io/Research/research/2026-03-18-api-context-hubs-rag-mcp.html]
- [inference] The evidence supports a hybrid architecture with a small, stable control surface loaded up front and a larger, volatile evidence surface discovered just in time.[source: https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents; https://davidamitchell.github.io/Research/research/2026-03-08-context-engineering-first-principles.html]

#### 2.8 Reference architecture and dominant failure modes

- [inference] The reference architecture implied by the sources is: registry or locator -> capability descriptors -> policy and routing layer -> ontology-aware retriever -> context assembly and compaction -> agent reasoning and tool use -> feedback, cache, and metrics.[source: https://modelcontextprotocol.io/registry/about; https://modelcontextprotocol.io/docs/learn/architecture; https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents; https://www.w3.org/TR/sparql11-query/; https://arxiv.org/abs/2404.16130]
- [fact] Mitchell (2026) on runtime Knowledge Graph dependencies identifies stale reads, propagation lag, timeout pressure, queue buildup, and degraded downstream answer quality as recurrent graph-layer runtime risks.[source: https://davidamitchell.github.io/Research/research/2026-05-12-knowledge-graph-agentic-runtime-dependency.html]
- [inference] When DRD is layered over an ontological store, the dominant failure modes become descriptor drift, stale or over-broad registry metadata, expensive graph queries, authorization mismatches between discovery and execution, and context pollution from poorly ranked retrieved evidence.[source: https://modelcontextprotocol.io/registry/about; https://www.w3.org/TR/sparql11-query/; https://arxiv.org/abs/2302.00093; https://davidamitchell.github.io/Research/research/2026-05-12-knowledge-graph-agentic-runtime-dependency.html]
- [inference] Governance is a first-class part of the pattern because late binding is only useful if capability descriptors, scopes, and authorization semantics remain trustworthy enough for the agent to choose safely.[source: https://modelcontextprotocol.io/registry/about; https://docs.oasis-open.org/ws-dd/discovery/1.1/wsdd-discovery-1.1-spec.html; https://datatracker.ietf.org/doc/html/rfc2608]

### §3 Reasoning

- [fact] The standards evidence most directly documents repeated discovery primitives, namely registries, descriptors, probes, scopes, and advertisements.[source: https://datatracker.ietf.org/doc/html/rfc2608; https://datatracker.ietf.org/doc/html/rfc6763; https://docs.oasis-open.org/ws-dd/discovery/1.1/wsdd-discovery-1.1-spec.html]
- [fact] The protocol evidence most directly documents MCP's concrete `tools`, `resources`, `prompts`, and registry metadata surfaces.[source: https://modelcontextprotocol.io/docs/learn/architecture; https://modelcontextprotocol.io/registry/about]
- [fact] The retrieval evidence documents the value of graph-aware or hybrid retrieval relative to text-only baselines on tasks that require relation-aware or corpus-level synthesis.[source: https://arxiv.org/abs/2404.16130; https://arxiv.org/abs/2408.04948; https://aclanthology.org/2025.acl-long.43/]
- [inference] The main inferential step is naming the shared structure "DRD," because the exact phrase is not standardized across the consulted protocols even though the structural family is clearly repeated.[source: https://datatracker.ietf.org/doc/html/rfc2608; https://datatracker.ietf.org/doc/html/rfc6763; https://docs.oasis-open.org/ws-dd/discovery/1.1/wsdd-discovery-1.1-spec.html]
- [assumption] Agents in the target enterprise use case will have access to both a semantic store and a retrieval layer able to translate discovered capabilities into executable queries or retrieval calls. Justification: without that bridge, DRD can expose endpoints but cannot produce semantically filtered context for the agent.[source: https://modelcontextprotocol.io/docs/learn/architecture; https://www.w3.org/TR/sparql11-query; https://arxiv.org/abs/2408.04948]

### §4 Consistency Check

- [fact] No source contradicts the claim that dynamic discovery adds latency relative to static preload; the consulted Anthropic material states this directly.[source: https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents]
- [fact] No source contradicts the claim that graph or hybrid retrieval is more useful than chunk-only retrieval for relation-heavy or corpus-level questions; GraphRAG, HybridRAG, and HybGRAG all support that direction, though on different task families.[source: https://arxiv.org/abs/2404.16130; https://arxiv.org/abs/2408.04948; https://aclanthology.org/2025.acl-long.43/]
- [inference] The unresolved ambiguity is not whether DRD-like structures exist, but whether the field will converge on one cross-vendor discovery layer for agent systems or continue to split between local registries, proprietary marketplaces, and protocol-native listings.[source: https://modelcontextprotocol.io/registry/about; https://modelcontextprotocol.io/docs/learn/architecture]
- [inference] The ontology portion of the conclusion is bounded: the evidence shows why typed graph stores help runtime relevance and explainability, but it does not prove that every agent context layer requires full OWL reasoning rather than lighter schema or hybrid graph techniques.[source: https://www.w3.org/TR/owl2-overview/; https://arxiv.org/abs/2408.04948; https://davidamitchell.github.io/Research/research/2026-05-15-ontology-landscape-for-curated-enterprise-context.html]

### §5 Depth and Breadth Expansion

- [inference] **Technical lens:** the pattern scales best when discovery metadata stays lightweight and the costly semantic work moves to a downstream router or retriever, because otherwise discovery itself becomes an expensive graph query rather than a cheap selection stage.[source: https://modelcontextprotocol.io/registry/about; https://www.w3.org/TR/sparql11-query; https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents]
- [inference] **Economic lens:** dynamic discovery reduces wasted token spend and prompt bloat, but it shifts cost into more retrieval calls, more orchestration logic, and more observability requirements.[source: https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents; https://davidamitchell.github.io/Research/research/2026-05-12-knowledge-graph-agentic-runtime-dependency.html]
- [inference] **Historical lens:** MCP looks less like a radical break than a specialization of long-standing service-discovery ideas for AI-native primitives, where "service instance" becomes "server exposing tools, resources, and prompts."[source: https://datatracker.ietf.org/doc/html/rfc2608; https://datatracker.ietf.org/doc/html/rfc6763; https://modelcontextprotocol.io/docs/learn/architecture]
- [inference] **Behavioral lens:** the need for progressive disclosure is amplified in agent systems because poor ranking does not only waste time; it actively increases the chance that the model will anchor on irrelevant or low-trust evidence.[source: https://arxiv.org/abs/2302.00093; https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents]
- [inference] **Governance lens:** DRD on top of ontology-backed stores sharpens identity, authorization, and provenance concerns, because discovered capabilities can expose broader graph slices than the current task should see unless scopes and policies are explicit.[source: https://modelcontextprotocol.io/registry/about; https://docs.oasis-open.org/ws-dd/discovery/1.1/wsdd-discovery-1.1-spec.html; https://davidamitchell.github.io/Research/research/2026-05-12-knowledge-graph-agentic-runtime-dependency.html]

### §6 Synthesis

**Executive summary:**

- [inference] In the surveyed protocols, Dynamic Resource Discovery is most usefully treated as a cross-system architecture pattern in which agents discover capability-bearing resources at runtime through registries, descriptors, advertisements, and late binding while different protocols describe that structure through different labels, even though the similarity may reflect either deeper architectural convergence or repeated responses to similar discovery constraints.[source: https://datatracker.ietf.org/doc/html/rfc2608; https://datatracker.ietf.org/doc/html/rfc6763; https://docs.oasis-open.org/ws-dd/discovery/1.1/wsdd-discovery-1.1-spec.html; https://modelcontextprotocol.io/docs/learn/architecture]
- [inference] In agent systems, MCP is a current agent-native instantiation of this pattern because it supports both server discovery through registry metadata and primitive discovery through dynamic listing of tools, resources, and prompts, while older protocols in this item mainly target network-service location.[source: https://modelcontextprotocol.io/registry/about; https://modelcontextprotocol.io/docs/learn/architecture; https://datatracker.ietf.org/doc/html/rfc2608; https://datatracker.ietf.org/doc/html/rfc6763; https://docs.oasis-open.org/ws-dd/discovery/1.1/wsdd-discovery-1.1-spec.html]
- [inference] DRD and context engineering solve adjacent stages of the same pipeline: DRD finds what can be accessed, while context engineering determines which discovered evidence should consume scarce runtime context.[source: https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents; https://arxiv.org/abs/2302.00093; https://modelcontextprotocol.io/docs/learn/architecture]
- [inference] Ontological stores make the pattern more precise and auditable because RDF, OWL, and SPARQL provide typed graph structure for relation-aware retrieval, and the consulted benchmark literature shows hybrid graph-plus-vector retrieval outperforming single-mode baselines in several mixed-evidence tasks, while still leaving open how far that result generalizes beyond those task settings.[source: https://www.w3.org/TR/rdf11-concepts/; https://www.w3.org/TR/owl2-overview/; https://www.w3.org/TR/sparql11-query/; https://arxiv.org/abs/2404.16130; https://arxiv.org/abs/2408.04948; https://aclanthology.org/2025.acl-long.43/]

**Key findings:**

1. [inference] In the surveyed discovery protocols, DRD is most usefully modeled as a synthesized architectural family because SLP, DNS-SD, WS-Discovery, and MCP all implement discoverable metadata plus late binding while describing that shared structure through different protocol labels, even though the similarity may reflect either deeper architectural convergence or repeated responses to similar discovery constraints.[source: https://datatracker.ietf.org/doc/html/rfc2608; https://datatracker.ietf.org/doc/html/rfc6763; https://docs.oasis-open.org/ws-dd/discovery/1.1/wsdd-discovery-1.1-spec.html; https://modelcontextprotocol.io/docs/learn/architecture]
2. [inference] A synthesized DRD abstraction can be expressed as registry or locator, machine-readable capability descriptor, lookup or advertisement mechanism, and a binding path from discovery to use, because those elements recur across classic discovery standards and the MCP architecture.[source: https://datatracker.ietf.org/doc/html/rfc2608; https://datatracker.ietf.org/doc/html/rfc6763; https://docs.oasis-open.org/ws-dd/discovery/1.1/wsdd-discovery-1.1-spec.html; https://modelcontextprotocol.io/docs/learn/architecture; https://modelcontextprotocol.io/registry/about]
3. [inference] MCP is a current agent-native DRD implementation because it supports pre-connection discovery of servers through the MCP Registry and post-connection discovery of tools, resources, and prompts through dynamic list methods, while the older protocols surveyed here focus on network-service discovery rather than agent-native primitives.[source: https://modelcontextprotocol.io/registry/about; https://modelcontextprotocol.io/docs/learn/architecture; https://datatracker.ietf.org/doc/html/rfc2608; https://datatracker.ietf.org/doc/html/rfc6763; https://docs.oasis-open.org/ws-dd/discovery/1.1/wsdd-discovery-1.1-spec.html]
4. [inference] Context engineering starts after discovery, and its main function is to turn a large set of dynamically discoverable resources into a minimal, high-signal working context through progressive disclosure, just-in-time loading, and aggressive relevance filtering.[source: https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents; https://arxiv.org/abs/2302.00093; https://davidamitchell.github.io/Research/research/2026-03-08-context-engineering-first-principles.html]
5. [inference] RDF, OWL, and SPARQL provide typed entities, relations, and query paths that make ontology-backed retrieval more semantically structured and auditable than purely lexical matching over static documentation.[source: https://www.w3.org/TR/rdf11-concepts/; https://www.w3.org/TR/owl2-overview/; https://www.w3.org/TR/sparql11-query/]
6. [inference] The consulted benchmark literature shows hybrid graph-plus-vector retrieval outperforming single-mode baselines in several ontology-relevant mixed-evidence tasks, even though the result should be read as task-specific rather than universal because the studies use different domains and evaluation setups.[source: https://arxiv.org/abs/2404.16130; https://arxiv.org/abs/2408.04948; https://aclanthology.org/2025.acl-long.43/]
7. [inference] Dynamic discovery trades lower prompt bloat and fresher evidence for higher orchestration cost, lookup latency, and more failure surfaces, which means the evidence favors a hybrid architecture that preloads a small control surface but discovers the larger evidence surface on demand.[source: https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents; https://arxiv.org/abs/2302.00093; https://davidamitchell.github.io/Research/research/2026-03-18-api-context-hubs-rag-mcp.html]
8. [inference] The main operational risks in a DRD-plus-ontology stack are descriptor drift, stale or over-broad registry metadata, expensive graph queries, authorization mismatch between discovery and execution, and low-quality ranking that injects distractor context into the model loop.[source: https://modelcontextprotocol.io/registry/about; https://www.w3.org/TR/sparql11-query/; https://arxiv.org/abs/2302.00093; https://davidamitchell.github.io/Research/research/2026-05-12-knowledge-graph-agentic-runtime-dependency.html]

**Evidence map:**

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [inference] In the surveyed protocols, DRD is a synthesized architectural family, though the similarity may reflect either architectural convergence or repeated discovery constraints. | https://datatracker.ietf.org/doc/html/rfc2608; https://datatracker.ietf.org/doc/html/rfc6763; https://docs.oasis-open.org/ws-dd/discovery/1.1/wsdd-discovery-1.1-spec.html; https://modelcontextprotocol.io/docs/learn/architecture | medium | Cross-standard synthesis |
| [inference] A synthesized DRD abstraction uses registries, descriptors, lookup or advertisement, and late binding. | https://datatracker.ietf.org/doc/html/rfc2608; https://datatracker.ietf.org/doc/html/rfc6763; https://docs.oasis-open.org/ws-dd/discovery/1.1/wsdd-discovery-1.1-spec.html; https://modelcontextprotocol.io/docs/learn/architecture; https://modelcontextprotocol.io/registry/about | medium | Cross-protocol synthesis |
| [inference] MCP is a current agent-native DRD implementation. | https://modelcontextprotocol.io/registry/about; https://modelcontextprotocol.io/docs/learn/architecture; https://datatracker.ietf.org/doc/html/rfc2608; https://datatracker.ietf.org/doc/html/rfc6763; https://docs.oasis-open.org/ws-dd/discovery/1.1/wsdd-discovery-1.1-spec.html | medium | Compared against older discovery protocols |
| [inference] Context engineering is the selection layer after discovery. | https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents; https://arxiv.org/abs/2302.00093; https://modelcontextprotocol.io/docs/learn/architecture | high | Direct on context limits and dynamic loading |
| [inference] RDF, OWL, and SPARQL provide the semantic substrate that makes ontology-backed retrieval more structured and auditable. | https://www.w3.org/TR/rdf11-concepts/; https://www.w3.org/TR/owl2-overview/; https://www.w3.org/TR/sparql11-query/ | medium | Retrieval implication inferred from standards |
| [inference] The consulted benchmark literature shows hybrid graph-plus-vector retrieval outperforming single-mode baselines in several mixed relational and textual tasks, with task-specific limits. | https://arxiv.org/abs/2404.16130; https://arxiv.org/abs/2408.04948; https://aclanthology.org/2025.acl-long.43/ | medium | Multiple papers, mixed domains |
| [inference] A practical architecture is hybrid: preload a small control surface, discover the larger evidence surface on demand. | https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents; https://davidamitchell.github.io/Research/research/2026-03-18-api-context-hubs-rag-mcp.html; https://arxiv.org/abs/2302.00093 | medium | Design synthesis |
| [inference] Descriptor drift, query cost, authorization mismatch, and distractor injection are the dominant risks. | https://modelcontextprotocol.io/registry/about; https://www.w3.org/TR/sparql11-query/; https://arxiv.org/abs/2302.00093; https://davidamitchell.github.io/Research/research/2026-05-12-knowledge-graph-agentic-runtime-dependency.html | medium | Operational synthesis |

**Assumptions:**

- [assumption] Enterprise agents that need ontology-backed context will have a retrieval or routing layer capable of translating discovered capability metadata into SPARQL, graph, or hybrid retrieval actions. Justification: discovery metadata alone cannot supply semantically filtered runtime context without an execution bridge.[source: https://modelcontextprotocol.io/docs/learn/architecture; https://www.w3.org/TR/sparql11-query; https://arxiv.org/abs/2408.04948]

**Analysis:**

- [inference] The evidence weighs most strongly in favor of a layered interpretation of the problem. Older service-discovery standards prove that runtime discovery itself is a mature distributed-systems problem, while Anthropic's context-engineering guidance shows that late discovery is only useful if a second-stage selection process aggressively controls what actually enters the context window.[source: https://datatracker.ietf.org/doc/html/rfc2608; https://docs.oasis-open.org/ws-dd/discovery/1.1/wsdd-discovery-1.1-spec.html; https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents]
- [inference] The repeated appearance of registries, metadata descriptors, discovery queries, and late binding across independent discovery standards makes convergent architectural structure a better explanation than accidental similarity, but the DRD label should still be read as an analytic synthesis rather than a formal protocol category.[source: https://datatracker.ietf.org/doc/html/rfc2608; https://datatracker.ietf.org/doc/html/rfc6763; https://docs.oasis-open.org/ws-dd/discovery/1.1/wsdd-discovery-1.1-spec.html]
- [inference] MCP matters because it relocates discovery from generic endpoint location to AI-native primitive discovery. That does not eliminate the older distributed-systems concerns; it adds new ones around prompt budget, primitive semantics, and trust in the descriptions the agent sees.[source: https://modelcontextprotocol.io/docs/learn/architecture; https://modelcontextprotocol.io/registry/about]
- [inference] Ontological stores sharpen the value of DRD by making late-bound retrieval semantically richer and more auditable, especially where the agent must explain why a relation, policy, or capability was considered relevant.[source: https://www.w3.org/TR/rdf11-concepts/; https://www.w3.org/TR/owl2-overview/; https://davidamitchell.github.io/Research/research/2026-05-15-ontology-landscape-for-curated-enterprise-context.html]
- [inference] Preload-only designs remain viable in bounded domains with small, stable evidence surfaces, and graph-only retrieval remains viable for schema-heavy tasks, but the mixed textual and relational evidence surface targeted here is better served by a hybrid retrieval layer.[source: https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents; https://arxiv.org/abs/2408.04948; https://aclanthology.org/2025.acl-long.43]
- [inference] That hybrid recommendation is a bounded default rather than a universal ranking, because the consulted retrieval papers use different tasks and benchmarks and therefore do not rule out better-tuned graph-only, vector-only, or partially cached architectures in narrower deployments.[source: https://arxiv.org/abs/2404.16130; https://arxiv.org/abs/2408.04948; https://aclanthology.org/2025.acl-long.43/; https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents]
- [inference] A practical architecture is a mediated stack in which registry metadata narrows the search surface, a retriever routes among graph and vector methods, and context engineering compresses the result into a task-bounded working set.[source: https://modelcontextprotocol.io/registry/about; https://arxiv.org/abs/2408.04948; https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents]

**Risks, gaps, uncertainties:**

- [inference] The evidence base is strong on discovery primitives and strong on hybrid retrieval, but weaker on direct published case studies that connect MCP-style discovery, ontology-backed retrieval, and large production multi-agent systems in one end-to-end public architecture.[source: https://modelcontextprotocol.io/docs/learn/architecture; https://arxiv.org/abs/2408.04948; https://aclanthology.org/2025.acl-long.43/]
- [inference] The ontology evidence proves the value of typed graphs and queryable relations, but it does not settle when full OWL reasoning is worth the runtime cost compared with lighter schema or property-graph approaches.[source: https://www.w3.org/TR/owl2-overview/; https://davidamitchell.github.io/Research/research/2026-05-15-ontology-landscape-for-curated-enterprise-context.html]
- [inference] The registry-governance surface remains under-specified for sensitive enterprise settings, particularly around who vouches for descriptors, how scopes are enforced, and how permission semantics remain aligned between discovery time and execution time.[source: https://modelcontextprotocol.io/registry/about; https://docs.oasis-open.org/ws-dd/discovery/1.1/wsdd-discovery-1.1-spec.html]

**Open questions:**

- [inference] What is the most robust schema for capability descriptors when the underlying resource is not an executable tool but a semantically versioned ontology slice or graph query template?[source: https://modelcontextprotocol.io/docs/learn/architecture; https://www.w3.org/TR/sparql11-query]
- [inference] What ranking strategy best combines ontology depth, graph centrality, lexical similarity, and current task intent for agent-facing retrieval over enterprise semantic stores?[source: https://arxiv.org/abs/2408.04948; https://aclanthology.org/2025.acl-long.43]
- [inference] What identity and authorization model best preserves late discovery while preventing agents from learning about resources they should not even know exist?[source: https://modelcontextprotocol.io/registry/about; https://docs.oasis-open.org/ws-dd/discovery/1.1/wsdd-discovery-1.1-spec.html]

### §7 Recursive Review

review_result: pass

acronym_audit: passed

claim_label_audit: passed

findings_synthesis_parity: aligned

cross_item_integration: included

confidence_assessment: medium

---

## Findings

### Executive Summary

In the surveyed protocols, Dynamic Resource Discovery is most usefully treated as a recurring architecture pattern in which an agent discovers capability-bearing resources through registries, descriptors, advertisements, and late binding at runtime while different protocols describe that structure through different labels, even though that similarity may reflect either deeper architectural convergence or repeated responses to similar discovery constraints.[inference; source: https://datatracker.ietf.org/doc/html/rfc2608; https://datatracker.ietf.org/doc/html/rfc6763; https://docs.oasis-open.org/ws-dd/discovery/1.1/wsdd-discovery-1.1-spec.html; https://modelcontextprotocol.io/docs/learn/architecture]

In current agent systems, MCP is a current agent-native implementation of that pattern because it supports discovery both before connection through registry metadata and after connection through dynamic listing of tools, resources, and prompts, while the older protocols surveyed here mainly target network-service discovery.[inference; source: https://modelcontextprotocol.io/registry/about; https://modelcontextprotocol.io/docs/learn/architecture; https://datatracker.ietf.org/doc/html/rfc2608; https://datatracker.ietf.org/doc/html/rfc6763; https://docs.oasis-open.org/ws-dd/discovery/1.1/wsdd-discovery-1.1-spec.html]

Context engineering and DRD solve different but adjacent problems: DRD determines what can be reached now, while context engineering determines what small subset of discovered evidence should consume the model's scarce working context.[inference; source: https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents; https://arxiv.org/abs/2302.00093; https://modelcontextprotocol.io/docs/learn/architecture]

For ontology-backed agent context layers, the consulted benchmark literature shows hybrid stacks outperforming single-mode baselines in several mixed relational and textual tasks, which supports a routed pipeline that combines discovery metadata, typed graph retrieval, vector retrieval, and context compaction, although that result remains task-specific rather than universal.[inference; source: https://www.w3.org/TR/rdf11-concepts/; https://www.w3.org/TR/sparql11-query/; https://arxiv.org/abs/2404.16130; https://arxiv.org/abs/2408.04948; https://aclanthology.org/2025.acl-long.43]

That conclusion is bounded rather than universal: the repeated primitives across independent standards make an architectural-family reading more convincing than pure coincidence, but the DRD label remains an analytic synthesis, and the hybrid retrieval recommendation is a strong default for the consulted evidence set rather than proof that narrower graph-only, vector-only, or partially cached designs are always worse.[inference; source: https://datatracker.ietf.org/doc/html/rfc2608; https://datatracker.ietf.org/doc/html/rfc6763; https://docs.oasis-open.org/ws-dd/discovery/1.1/wsdd-discovery-1.1-spec.html; https://arxiv.org/abs/2404.16130; https://arxiv.org/abs/2408.04948; https://aclanthology.org/2025.acl-long.43/; https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents]

### Key Findings

1. **In the surveyed discovery protocols, Dynamic Resource Discovery is most usefully modeled as a synthesized architectural family because SLP, DNS-SD, WS-Discovery, and MCP all implement discoverable metadata plus late binding while describing that shared structure through different protocol labels, even though the similarity may reflect either deeper architectural convergence or repeated responses to similar discovery constraints.** ([inference]; medium confidence; source: https://datatracker.ietf.org/doc/html/rfc2608; https://datatracker.ietf.org/doc/html/rfc6763; https://docs.oasis-open.org/ws-dd/discovery/1.1/wsdd-discovery-1.1-spec.html; https://modelcontextprotocol.io/docs/learn/architecture)
2. **A synthesized DRD abstraction can be expressed as registry or locator, machine-readable capability descriptor, lookup or advertisement mechanism, and a binding path from discovery to use, because those elements recur across classic discovery standards and the MCP architecture.** ([inference]; medium confidence; source: https://datatracker.ietf.org/doc/html/rfc2608; https://datatracker.ietf.org/doc/html/rfc6763; https://docs.oasis-open.org/ws-dd/discovery/1.1/wsdd-discovery-1.1-spec.html; https://modelcontextprotocol.io/docs/learn/architecture; https://modelcontextprotocol.io/registry/about)
3. **MCP is a current agent-native DRD implementation because it combines pre-connection discovery of servers through registry metadata with post-connection discovery of tools, resources, and prompts through dynamic list methods, while the older protocols surveyed here focus on network-service discovery rather than agent-native primitives.** ([inference]; medium confidence; source: https://modelcontextprotocol.io/registry/about; https://modelcontextprotocol.io/docs/learn/architecture; https://datatracker.ietf.org/doc/html/rfc2608; https://datatracker.ietf.org/doc/html/rfc6763; https://docs.oasis-open.org/ws-dd/discovery/1.1/wsdd-discovery-1.1-spec.html)
4. **Context engineering begins after discovery and converts a large set of discoverable resources into a minimal, high-signal working context through progressive disclosure, just-in-time loading, and aggressive relevance filtering that protects the model from distractor evidence.** ([inference]; high confidence; source: https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents; https://arxiv.org/abs/2302.00093; https://davidamitchell.github.io/Research/research/2026-03-08-context-engineering-first-principles.html)
5. **RDF, OWL, and SPARQL provide typed entities, relations, and query paths that make ontology-backed retrieval more semantically structured and auditable than purely lexical matching over static documentation.** ([inference]; medium confidence; source: https://www.w3.org/TR/rdf11-concepts/; https://www.w3.org/TR/owl2-overview/; https://www.w3.org/TR/sparql11-query)
6. **The consulted benchmark literature shows hybrid graph-plus-vector retrieval outperforming single-mode baselines in several ontology-relevant mixed-evidence tasks, even though the result should be read as task-specific rather than universal because the studies use different domains and evaluation setups.** ([inference]; medium confidence; source: https://arxiv.org/abs/2404.16130; https://arxiv.org/abs/2408.04948; https://aclanthology.org/2025.acl-long.43)
7. **Dynamic discovery reduces prompt bloat and improves evidence freshness, but it raises orchestration cost, ranking dependence, and lookup latency, so the evidence favors a hybrid architecture that preloads a small stable control surface and discovers the larger evidence surface on demand.** ([inference]; medium confidence; source: https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents; https://arxiv.org/abs/2302.00093; https://davidamitchell.github.io/Research/research/2026-03-18-api-context-hubs-rag-mcp.html)
8. **The dominant operational risks in a DRD-plus-ontology stack are descriptor drift, stale or over-broad registry metadata, expensive graph queries, authorization mismatch between discovery and execution, and low-quality ranking that injects irrelevant evidence into the model loop.** ([inference]; medium confidence; source: https://modelcontextprotocol.io/registry/about; https://www.w3.org/TR/sparql11-query/; https://arxiv.org/abs/2302.00093; https://davidamitchell.github.io/Research/research/2026-05-12-knowledge-graph-agentic-runtime-dependency.html)

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [inference] DRD is a recurring architectural family described through different protocol labels. | https://datatracker.ietf.org/doc/html/rfc2608; https://datatracker.ietf.org/doc/html/rfc6763; https://docs.oasis-open.org/ws-dd/discovery/1.1/wsdd-discovery-1.1-spec.html; https://modelcontextprotocol.io/docs/learn/architecture | medium | Cross-standard synthesis |
| [inference] A synthesized DRD abstraction uses registries, descriptors, lookup or advertisement, and late binding. | https://datatracker.ietf.org/doc/html/rfc2608; https://datatracker.ietf.org/doc/html/rfc6763; https://docs.oasis-open.org/ws-dd/discovery/1.1/wsdd-discovery-1.1-spec.html; https://modelcontextprotocol.io/docs/learn/architecture; https://modelcontextprotocol.io/registry/about | medium | Cross-protocol synthesis |
| [inference] MCP is a current agent-native DRD implementation. | https://modelcontextprotocol.io/registry/about; https://modelcontextprotocol.io/docs/learn/architecture; https://datatracker.ietf.org/doc/html/rfc2608; https://datatracker.ietf.org/doc/html/rfc6763; https://docs.oasis-open.org/ws-dd/discovery/1.1/wsdd-discovery-1.1-spec.html | medium | Compared against older discovery protocols |
| [inference] Context engineering is the selection layer after discovery. | https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents; https://arxiv.org/abs/2302.00093; https://modelcontextprotocol.io/docs/learn/architecture | high | Strong direct support |
| [inference] RDF, OWL, and SPARQL provide the semantic substrate that makes ontology-backed retrieval more structured and auditable. | https://www.w3.org/TR/rdf11-concepts/; https://www.w3.org/TR/owl2-overview/; https://www.w3.org/TR/sparql11-query | medium | Retrieval implication inferred from standards |
| [inference] The consulted benchmark literature shows hybrid graph-plus-vector retrieval outperforming single-mode baselines in several mixed relational and textual tasks, with task-specific limits. | https://arxiv.org/abs/2404.16130; https://arxiv.org/abs/2408.04948; https://aclanthology.org/2025.acl-long.43 | medium | Multi-paper synthesis |
| [inference] A practical architecture preloads a small control surface and discovers the larger evidence surface on demand. | https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents; https://davidamitchell.github.io/Research/research/2026-03-18-api-context-hubs-rag-mcp.html; https://arxiv.org/abs/2302.00093 | medium | Design synthesis |
| [inference] Descriptor drift, query cost, authorization mismatch, and distractor injection are the main risks. | https://modelcontextprotocol.io/registry/about; https://www.w3.org/TR/sparql11-query/; https://arxiv.org/abs/2302.00093; https://davidamitchell.github.io/Research/research/2026-05-12-knowledge-graph-agentic-runtime-dependency.html | medium | Operational synthesis |

### Assumptions

- **Assumption:** Enterprise agents that need ontology-backed context will have a routing layer capable of translating discovered capability metadata into executable retrieval actions. **Justification:** Discovery metadata alone cannot produce semantically filtered runtime context without a bridge into query execution or retrieval selection. [assumption; source: https://modelcontextprotocol.io/docs/learn/architecture; https://www.w3.org/TR/sparql11-query; https://arxiv.org/abs/2408.04948]

### Analysis

The evidence supports a layered interpretation of the design problem in which preload, retrieval, and protocol standardization each occupy a different place in the stack.[inference; source: https://davidamitchell.github.io/Research/research/2026-03-18-api-context-hubs-rag-mcp.html; https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents]

The repeated appearance of registries, metadata descriptors, discovery queries, and late binding across independent discovery standards makes convergent architectural structure a better explanation than accidental similarity, but the DRD label should still be read as an analytic synthesis rather than a formal protocol category.[inference; source: https://datatracker.ietf.org/doc/html/rfc2608; https://datatracker.ietf.org/doc/html/rfc6763; https://docs.oasis-open.org/ws-dd/discovery/1.1/wsdd-discovery-1.1-spec.html]

Classic discovery standards show that late-bound selection of services is an old systems pattern, while MCP adapts that pattern to agent-native primitives such as tools, resources, and prompts.[inference; source: https://datatracker.ietf.org/doc/html/rfc2608; https://datatracker.ietf.org/doc/html/rfc6763; https://docs.oasis-open.org/ws-dd/discovery/1.1/wsdd-discovery-1.1-spec.html; https://modelcontextprotocol.io/docs/learn/architecture]

Ontological stores strengthen the design because they let the retrieval layer reason over typed entities and relations, and the retrieval evidence suggests that hybrid graph-plus-vector strategies can outperform pure graph strategies on mixed questions.[inference; source: https://www.w3.org/TR/owl2-overview/; https://arxiv.org/abs/2408.04948; https://aclanthology.org/2025.acl-long.43]

Preload-only designs remain viable in bounded domains with small, stable evidence surfaces, and graph-only retrieval remains viable for schema-heavy tasks, but the mixed textual and relational evidence surface targeted here is better served by a hybrid retrieval layer.[inference; source: https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents; https://arxiv.org/abs/2408.04948; https://aclanthology.org/2025.acl-long.43]

That recommendation should be read as a bounded default rather than a universal ranking, because the consulted retrieval papers use different tasks and benchmarks and therefore do not rule out better-tuned graph-only, vector-only, or partially cached architectures in narrower deployments.[inference; source: https://arxiv.org/abs/2404.16130; https://arxiv.org/abs/2408.04948; https://aclanthology.org/2025.acl-long.43/; https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents]

The practical architecture therefore uses DRD to narrow what is reachable, a hybrid retriever to narrow what is relevant, and context engineering to narrow what the model actually sees at generation time.[inference; source: https://modelcontextprotocol.io/registry/about; https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents; https://arxiv.org/abs/2302.00093]

### Risks, Gaps, and Uncertainties

- Public evidence is strong on discovery primitives and on hybrid retrieval, but weaker on end-to-end production case studies that combine MCP-style discovery, ontology-backed retrieval, and large public multi-agent systems in one documented architecture.[inference; source: https://modelcontextprotocol.io/docs/learn/architecture; https://arxiv.org/abs/2408.04948; https://aclanthology.org/2025.acl-long.43]
- The ontology evidence does not settle when full OWL reasoning is worth the runtime complexity compared with lighter schema or property-graph approaches.[inference; source: https://www.w3.org/TR/owl2-overview/; https://davidamitchell.github.io/Research/research/2026-05-15-ontology-landscape-for-curated-enterprise-context.html]
- Registry governance, trust, and authorization semantics remain comparatively under-specified for sensitive enterprise settings where agents should not even discover certain resources.[inference; source: https://modelcontextprotocol.io/registry/about; https://docs.oasis-open.org/ws-dd/discovery/1.1/wsdd-discovery-1.1-spec.html]

### Open Questions

- What descriptor schema best represents ontology slices, query templates, and semantically versioned graph resources as discoverable agent capabilities?[inference; source: https://modelcontextprotocol.io/docs/learn/architecture; https://www.w3.org/TR/sparql11-query]
- What ranking model best combines ontology depth, graph centrality, lexical similarity, and current task intent in enterprise semantic stores?[inference; source: https://arxiv.org/abs/2408.04948; https://aclanthology.org/2025.acl-long.43]
- What authorization model best preserves late discovery while preventing agents from learning about restricted resources or graph neighborhoods?[inference; source: https://modelcontextprotocol.io/registry/about; https://docs.oasis-open.org/ws-dd/discovery/1.1/wsdd-discovery-1.1-spec.html]

---

## Output

- Type: knowledge
- Description: Reference synthesis on Dynamic Resource Discovery as a layered architecture pattern for agent context systems, with emphasis on how runtime discovery composes with ontology-backed retrieval and context assembly.[inference; source: https://modelcontextprotocol.io/docs/learn/architecture; https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents; https://www.w3.org/TR/sparql11-query]
- Links:
  - https://modelcontextprotocol.io/docs/learn/architecture
  - https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
  - https://arxiv.org/abs/2408.04948
