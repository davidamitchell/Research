---
title: "Web ontologies in production Knowledge Graphs for multi-step Artificial Intelligence (AI) agents: Resource Description Framework (RDF), Web Ontology Language (OWL), RDF Schema (RDFS), Simple Knowledge Organization System (SKOS), and Schema.org best practices"
added: 2026-05-12T08:21:48+00:00
status: completed
review_count: 2
priority: high
blocks: []
tags: [knowledge-graph, agentic-ai, governance, llm]
started: 2026-05-12T11:04:03+00:00
completed: 2026-05-12T11:25:01+00:00
output: [knowledge]
cites:
  - 2026-05-12-knowledge-graph-agentic-runtime-dependency
  - 2026-05-12-knowledge-graph-lifecycle-management-agentic
  - 2026-05-12-graph-db-saas-knowledge-ontology
  - 2026-04-22-knowledge-curation-governance-for-regulated-ai
related:
  - 2026-05-02-knowledge-graph-schema-cross-session-research-mcp
  - 2026-03-03-knowledge-representation-agent-context
superseded_by: ~
supersedes: ~
item_type: primary
confidence: medium
versions:
  - version: "1.0"
    sha: bcf2fca20a157dd592d32588a69094567953a4be
    changed: 2026-05-12
    progress: progress/2026-05-12-web-ontologies-production-knowledge-graph-agentic.md
    summary: Initial completion
---

# Web ontologies in production Knowledge Graphs for multi-step Artificial Intelligence (AI) agents: Resource Description Framework (RDF), Web Ontology Language (OWL), RDF Schema (RDFS), Simple Knowledge Organization System (SKOS), and Schema.org best practices

## Research Question

How should web ontologies, Resource Description Framework (RDF), Web Ontology Language (OWL), RDF Schema (RDFS), Simple Knowledge Organization System (SKOS), and Schema.org, be selected, composed, and applied when designing and operating a Knowledge Graph (KG), a structured graph of entities and relationships, used by multi-step Artificial Intelligence (AI) agents, and what are the trade-offs between expressivity, runtime performance, and agent comprehensibility?

## Scope

**In scope:**
- Overview and comparison of RDF, RDFS, OWL 2 profiles, SKOS, and Schema.org
- Selection criteria for choosing the right ontology layer or combination for a given multi-step Artificial Intelligence (AI) agent use case
- Best practices for ontology composition, including reuse of existing vocabularies versus custom extensions
- Reasoner and inference options at production scale, including OWL 2 EL for large class hierarchies, OWL 2 QL for query rewriting over relational data, OWL 2 RL for rule-based reasoning, SPARQL Protocol and RDF Query Language (SPARQL)-based inference, and materialization versus query-time inference
- Impact of ontology expressivity on query latency and downstream answer quality
- Ontology governance, including ownership, change approval, deployment, deprecation, and backward compatibility
- Relationship between ontology choices and common serializations, including Turtle, JSON for Linked Data (JSON-LD), RDF/XML, the XML syntax for RDF, and TriG

**Out of scope:**
- Open Digital Rights Language (ODRL) policies
- Graph database platform selection as a standalone procurement decision
- Data product ownership and contract design
- Pure description-logics research with no production operating implications

**Constraints:**
- Focus on production-relevant OWL usage; treat OWL 2 Description Logic (OWL 2 DL) and OWL 2 Full as exceptional rather than default choices for live systems
- Prefer World Wide Web Consortium (W3C) specifications, public governance documentation, and published ontology-engineering guidance over vendor marketing

## Context

RDF-based ontologies give Knowledge Graphs a shared vocabulary that software systems can query, extend, and exchange across documents and services.[fact; source: https://www.w3.org/TR/rdf12-concepts/; https://www.w3.org/TR/rdf12-schema/]

OWL adds formal semantics above RDF and RDFS, while SKOS provides a lighter model for thesauri and taxonomies rather than full formal axioms.[fact; source: https://www.w3.org/TR/owl2-primer/; https://www.w3.org/TR/skos-reference/]

In this item, multi-step Artificial Intelligence (AI) agents means systems that plan, retrieve, or call tools across several steps rather than producing one isolated answer.[inference; source: https://arxiv.org/abs/2306.08302; https://arxiv.org/abs/2404.16130]

Without clear ontology choices, those systems must rely on implicit term meanings, which weakens auditability and makes later governance and change control harder.[inference; source: https://www.w3.org/TR/prov-o/; https://www.w3.org/TR/dwbp/; https://arxiv.org/abs/2306.08302]

## Approach

1. Survey the W3C ontology stack, RDF, RDFS, OWL 2 profiles, SKOS, and Schema.org, and map each layer to its typical production role.
2. Review linked-data and ontology-engineering guidance, especially Best Practice Recipes for Publishing RDF Vocabularies, Ontology Development 101, Ontology Design Patterns (ODPs), and the LOT methodology.
3. Investigate ontology expressivity versus runtime inference, including materialization versus query-time inference and the production implications of OWL 2 EL, OWL 2 QL, and OWL 2 RL.
4. Examine ontology governance models in public systems, especially Schema.org and Wikidata, then connect them to enterprise ontology governance practice.
5. Identify practical reuse patterns for public vocabularies such as Dublin Core Terms, Friend of a Friend (FOAF), the Provenance Ontology (PROV-O), OWL-Time, and Data Catalog Vocabulary (DCAT).
6. Assess how Large Language Model (LLM) agents consume ontological knowledge through SPARQL, serialized graph fragments, and graph-derived summaries.
7. Synthesize a decision guide that recommends which ontology layer to use for which production need and what governance process should accompany it.

## Sources

- [x] [W3C RDF 1.2 Concepts (2024)](https://www.w3.org/TR/rdf12-concepts/)
- [x] [W3C RDF 1.2 Schema (2025 Working Draft)](https://www.w3.org/TR/rdf12-schema/)
- [x] [W3C OWL 2 Web Ontology Language Primer (2012)](https://www.w3.org/TR/owl2-primer/)
- [x] [W3C OWL 2 Profiles (2012)](https://www.w3.org/TR/owl2-profiles/)
- [x] [W3C SKOS Simple Knowledge Organization System Reference (2009)](https://www.w3.org/TR/skos-reference/)
- [x] [W3C Data on the Web Best Practices (2017)](https://www.w3.org/TR/dwbp/)
- [x] [W3C Best Practice Recipes for Publishing RDF Vocabularies (2008)](https://www.w3.org/TR/swbp-vocab-pub/)
- [x] [Schema.org About](https://schema.org/docs/about.html)
- [x] [Schema.org How We Work](https://schema.org/docs/howwework.html)
- [x] [Noy and McGuinness (2001) Ontology Development 101: A Guide to Creating Your First Ontology](https://protege.stanford.edu/publications/ontology_development/ontology101-noy-mcguinness.html)
- [x] [Hogan et al. (2021) Knowledge Graphs](https://arxiv.org/abs/2003.02320)
- [x] [LOT methodology site](https://lot.linkeddata.es/)
- [ ] [Poveda-Villalón et al. (2022) LOT: An industrial oriented ontology engineering framework](https://doi.org/10.1016/j.engappai.2022.104755)
- [x] [OntologyDesignPatterns.org portal](http://ontologydesignpatterns.org)
- [x] [Wikidata Property proposal](https://www.wikidata.org/wiki/Wikidata:Property_proposal)
- [x] [Wikidata Creating a property proposal](https://www.wikidata.org/wiki/Wikidata:Creating_a_property_proposal)
- [x] [Wikidata WikiProject Ontology](https://www.wikidata.org/wiki/Wikidata:WikiProject_Ontology)
- [x] [W3C PROV-O (2013)](https://www.w3.org/TR/prov-o/)
- [x] [W3C OWL-Time (2023 Candidate Recommendation Draft)](https://www.w3.org/TR/owl-time/)
- [x] [W3C DCAT 3 (2024)](https://www.w3.org/TR/vocab-dcat-3/)
- [x] [FOAF specification](https://xmlns.com/foaf/spec/)
- [x] [Stardog Reasoning and Inference documentation](https://docs.stardog.com/inference-engine/)
- [ ] [Ontotext GraphDB Inferencing documentation](https://graphdb.ontotext.com/documentation/11.0/inference.html)
- [x] [Luo et al. (2024) Unifying Large Language Models and Knowledge Graphs: A Roadmap](https://arxiv.org/abs/2306.08302)
- [x] [Edge et al. (2025) From Local to Global: A GraphRAG Approach to Query-Focused Summarization](https://arxiv.org/abs/2404.16130)
- [x] [W3C JSON-LD 1.1](https://www.w3.org/TR/json-ld11/)
- [x] [W3C Turtle](https://www.w3.org/TR/turtle/)
- [x] [W3C TriG](https://www.w3.org/TR/trig/)
- [x] [W3C RDF/XML Syntax Specification](https://www.w3.org/TR/rdf-syntax-grammar/)
- [x] [Mitchell (2026) Knowledge Graph in the live execution path of multi-step Large Language Model systems: architecture and failure modes](https://davidamitchell.github.io/Research/research/2026-05-12-knowledge-graph-agentic-runtime-dependency.html)
- [x] [Mitchell (2026) Knowledge Graph lifecycle management for multi-step software agents: schema versioning, entity resolution, and knowledge freshness](https://davidamitchell.github.io/Research/research/2026-05-12-knowledge-graph-lifecycle-management-agentic.html)
- [x] [Mitchell (2026) Hosted Software-as-a-Service graph database options for knowledge ontology](https://davidamitchell.github.io/Research/research/2026-05-12-graph-db-saas-knowledge-ontology.html)
- [x] [Mitchell (2026) Knowledge curation governance as an enterprise AI capability in regulated financial institutions](https://davidamitchell.github.io/Research/research/2026-04-22-knowledge-curation-governance-for-regulated-ai.html)
- [x] [Mitchell (2026) What entity-relation schema and write-query patterns best support cross-session research provenance and concept reuse for an Artificial Intelligence agent using the Model Context Protocol memory server?](https://davidamitchell.github.io/Research/research/2026-05-02-knowledge-graph-schema-cross-session-research-mcp.html)

---

## Research Skill Output

*(Full output from running the research skill, retained verbatim in the completed item. Sections 0-5 are the investigation, and section 6 seeds the Findings section below.)*

### §0 Initialise

- Question: determine how RDF, RDFS, OWL, SKOS, and Schema.org should be combined in a production Knowledge Graph for multi-step Artificial Intelligence (AI) agents, and identify the trade-offs between semantic expressivity, runtime inference cost, and agent-facing usability.
- Scope: ontology-layer selection, reuse, inference strategy, governance, serializations, and agent-consumption paths are in scope; policy languages, standalone database procurement, and purely academic description-logics work are out of scope.
- Constraints: prefer W3C standards, public governance pages, and published ontology-engineering guidance; keep conclusions production-oriented; expand acronyms on first use; use URL-backed citations only.
- Output format: full section 0 to section 7 investigation plus Findings with Executive Summary, Key Findings, Evidence Map, Assumptions, Analysis, Risks, Gaps, Uncertainties, Open Questions, and Output.
- [inference] Prior completed items most relevant here are the runtime-dependency item, the lifecycle-management item, the hosted graph-platform item, the knowledge-curation-governance item, and the schema-cross-session item, because they already cover serving semantics, versioning, graph-platform reasoning behavior, governance ownership, and provenance-aware modeling. [source: https://davidamitchell.github.io/Research/research/2026-05-12-knowledge-graph-agentic-runtime-dependency.html; https://davidamitchell.github.io/Research/research/2026-05-12-knowledge-graph-lifecycle-management-agentic.html; https://davidamitchell.github.io/Research/research/2026-05-12-graph-db-saas-knowledge-ontology.html; https://davidamitchell.github.io/Research/research/2026-04-22-knowledge-curation-governance-for-regulated-ai.html; https://davidamitchell.github.io/Research/research/2026-05-02-knowledge-graph-schema-cross-session-research-mcp.html]
- [fact] RDF is the core graph data model, RDFS is its lightweight schema vocabulary, OWL adds richer formal semantics, SKOS models concept schemes and taxonomies, and Schema.org provides a collaboratively governed vocabulary for structured web data. [source: https://www.w3.org/TR/rdf12-concepts/; https://www.w3.org/TR/rdf12-schema/; https://www.w3.org/TR/owl2-primer/; https://www.w3.org/TR/skos-reference/; https://schema.org/docs/about.html]
- [inference] Working definition for this item: a production ontology stack is the combination of vocabularies, inference rules, publication patterns, and governance controls that keep a Knowledge Graph interoperable for software while remaining understandable enough for operators and downstream AI agents to use safely. [source: https://www.w3.org/TR/dwbp/; https://www.w3.org/TR/swbp-vocab-pub/; https://lot.linkeddata.es/]

### §1 Question Decomposition

- A. Baseline modeling layer
  - A1. What does RDF contribute that every ontology stack needs?
  - A2. What does RDFS contribute before OWL is introduced?
  - A3. Which serializations matter operationally for exchanging the same graph model?
- B. Additional semantic layers
  - B1. When is OWL needed instead of RDFS alone?
  - B2. Which production use cases favor OWL 2 EL, OWL 2 QL, or OWL 2 RL?
  - B3. When should OWL 2 Description Logic or OWL 2 Full be kept off the live critical path?
- C. Lightweight vocabularies
  - C1. When is SKOS the right choice instead of a formal domain ontology?
  - C2. When is Schema.org useful, and where is it insufficient as the only internal model?
- D. Composition and reuse
  - D1. What published guidance says about reusing existing vocabularies before creating new terms?
  - D2. Which widely used support vocabularies, such as PROV-O, OWL-Time, DCAT, and FOAF, solve common cross-cutting needs?
- E. Governance and lifecycle
  - E1. How do public ontology programs approve, version, and deprecate changes?
  - E2. What governance controls are needed in enterprise or production settings?
- F. Runtime inference and agent consumption
  - F1. How do materialization and query-time reasoning trade freshness for latency and operational simplicity?
  - F2. How do multi-step AI agents consume ontology-backed knowledge in practice?
- G. Synthesis
  - G1. What is the minimal safe ontology stack for most production Knowledge Graphs?
  - G2. What governance process should accompany that stack?

### §2 Investigation

#### 2.0 Identified but not consulted

- [ ] Poveda-Villalón et al. (2022) journal article DOI page for LOT, identified; direct article text not consulted.
- [ ] Ontotext GraphDB Inferencing documentation, identified; documentation body not consulted.

#### 2.1 RDF, RDFS, and serialization surfaces

- [fact] RDF graphs are sets of subject-predicate-object triples, and RDF datasets add a default graph plus zero or more named graphs, which makes RDF the base data model underneath RDF-based ontology languages. [source: https://www.w3.org/TR/rdf12-concepts/]
- [fact] RDF Schema provides a lightweight ontology vocabulary, including classes, properties, subclass relations, subproperty relations, and domain and range mechanisms. [source: https://www.w3.org/TR/rdf12-schema/]
- [fact] Turtle is a compact textual syntax for RDF graphs, TriG extends Turtle to represent complete RDF datasets with named graphs, JSON-LD is a JSON-based serialization of Linked Data intended for web programming environments, and RDF/XML defines an XML syntax for RDF graphs. [source: https://www.w3.org/TR/turtle/; https://www.w3.org/TR/trig/; https://www.w3.org/TR/json-ld11/; https://www.w3.org/TR/rdf-syntax-grammar/]
- [inference] RDF plus RDFS is the minimum interoperable ontology layer for production systems that need typed entities and extensible vocabularies but do not need expensive logical inference, because the standards already provide class, property, hierarchy, and dataset structure without the additional reasoning burden of OWL. [source: https://www.w3.org/TR/rdf12-concepts/; https://www.w3.org/TR/rdf12-schema/; https://www.w3.org/TR/owl2-primer/]
- [inference] Turtle and JSON-LD are usually more comprehensible to developers and prompt-building systems than RDF/XML, because Turtle is explicitly designed as a compact natural text form and JSON-LD is designed to integrate with deployed JSON systems, whereas RDF/XML exists primarily as an XML encoding of the graph model. [source: https://www.w3.org/TR/turtle/; https://www.w3.org/TR/json-ld11/; https://www.w3.org/TR/rdf-syntax-grammar/]

#### 2.2 OWL scope and profile selection

- [fact] OWL is a computational logic-based language that allows computer programs to verify consistency and make implicit knowledge explicit from formally defined ontologies. [source: https://www.w3.org/TR/owl2-primer/]
- [fact] OWL 2 EL targets ontologies with very large numbers of classes or properties and supports polynomial-time reasoning. [source: https://www.w3.org/TR/owl2-profiles/]
- [fact] OWL 2 QL targets very large instance datasets where conjunctive query answering is the dominant task and can be implemented by rewriting queries into standard relational query systems. [source: https://www.w3.org/TR/owl2-profiles/]
- [fact] OWL 2 RL targets scalable rule-based reasoning engines and is intended for applications that want more expressivity than RDF(S) without paying the full cost of unrestricted OWL reasoning. [source: https://www.w3.org/TR/owl2-profiles/]
- [inference] OWL 2 EL and OWL 2 RL are the most natural defaults for production Knowledge Graph inference, while OWL 2 QL is a specialized fit for ontology-based data access over relational data, because the W3C profile definitions align those profiles to scalable hierarchy reasoning, rule engines, and query rewriting respectively. [source: https://www.w3.org/TR/owl2-profiles/; https://www.w3.org/TR/owl2-primer/]
- [inference] OWL 2 DL and OWL 2 Full should usually stay off the live critical path for multi-step AI agents, because the production-friendly W3C guidance focuses on tractable profiles for implementability and the item's scope explicitly excludes undecidable-at-scale reasoning as a default operating posture. [source: https://www.w3.org/TR/owl2-profiles/; https://www.w3.org/TR/owl2-primer/]

#### 2.3 SKOS and Schema.org as lighter semantic layers

- [fact] SKOS is a common data model for concept schemes such as thesauri, classification schemes, subject heading systems, and taxonomies, and the specification states that SKOS is not a formal knowledge representation language. [source: https://www.w3.org/TR/skos-reference/]
- [fact] Schema.org is a collaborative activity that creates and maintains schemas for structured data on the Internet, with day-to-day operations handled by a steering group and change discussions handled through the W3C community group and GitHub. [source: https://schema.org/docs/about.html; https://schema.org/docs/howwework.html]
- [fact] Schema.org publishes named releases, preserves dated snapshots, exposes a `schemaVersion` property, and rarely removes terms without leaving a `supersededBy` relation. [source: https://schema.org/docs/howwework.html]
- [inference] SKOS is the right layer for navigational taxonomies, labels, mappings, and concept-scheme maintenance, but it is the wrong layer for constraints or rich domain axioms, because the specification explicitly positions SKOS as an informal bridge for knowledge-organization systems rather than as a formal ontology language. [source: https://www.w3.org/TR/skos-reference/]
- [inference] Schema.org is strongest at external interchange boundaries, public metadata publication, and web-facing interoperability, but it is usually too broad and consensus-shaped to serve as the only internal canonical ontology for production operations, because its governance optimizes shared web vocabulary evolution rather than tight domain constraints. [source: https://schema.org/docs/about.html; https://schema.org/docs/howwework.html; https://www.w3.org/TR/dwbp/]

#### 2.4 Ontology composition and reuse

- [fact] Ontology Development 101 argues that ontology development is iterative, that there is no single correct model for a domain, and that concepts should stay close to the objects and relationships in the target domain. [source: https://protege.stanford.edu/publications/ontology_development/ontology101-noy-mcguinness.html]
- [fact] The LOT methodology structures ontology engineering into requirements specification, iterative implementation sprints, ontology reuse, evaluation, publication, and maintenance. [source: https://lot.linkeddata.es/]
- [fact] OntologyDesignPatterns.org is a portal dedicated to Ontology Design Patterns and catalogs patterns, modeling issues, and training material for modular ontology modeling. [source: http://ontologydesignpatterns.org]
- [fact] PROV-O is a lightweight provenance ontology that can be specialized for application-specific provenance modeling and conforms almost entirely to the OWL RL profile. [source: https://www.w3.org/TR/prov-o/]
- [fact] OWL-Time provides a reusable ontology for temporal concepts such as instants, intervals, durations, and temporal relations. [source: https://www.w3.org/TR/owl-time/]
- [fact] DCAT is an RDF vocabulary designed to facilitate interoperability between data catalogs and dataset metadata published on the Web. [source: https://www.w3.org/TR/vocab-dcat-3/]
- [fact] FOAF provides a vocabulary for agents, persons, groups, organizations, documents, and online accounts. [source: https://xmlns.com/foaf/spec/]
- [fact] W3C best-practice guidance for publishing RDF vocabularies recommends stable vocabulary Uniform Resource Identifiers (URIs), content negotiation, and separate human-readable and machine-processable representations where appropriate. [source: https://www.w3.org/TR/swbp-vocab-pub/]
- [inference] The strongest composition pattern is a small domain ontology plus reused support vocabularies for provenance, time, catalogs, and actors, because that keeps the core ontology narrow while reusing mature community semantics for cross-cutting concerns. [source: https://www.w3.org/TR/prov-o/; https://www.w3.org/TR/owl-time/; https://www.w3.org/TR/vocab-dcat-3/; https://xmlns.com/foaf/spec/; https://lot.linkeddata.es/]
- [inference] Custom terms should be added only where published vocabularies leave a genuine domain gap, because Ontology Development 101, LOT, and ODP guidance all push ontology teams toward iterative reuse before extension. [source: https://protege.stanford.edu/publications/ontology_development/ontology101-noy-mcguinness.html; https://lot.linkeddata.es/; http://ontologydesignpatterns.org]

#### 2.5 Governance and lifecycle control

- [fact] Wikidata manages ontology evolution through community property proposals, proposal-writing guidance, and WikiProject Ontology coordination rather than through a single central design authority. [source: https://www.wikidata.org/wiki/Wikidata:Property_proposal; https://www.wikidata.org/wiki/Wikidata:Creating_a_property_proposal; https://www.wikidata.org/wiki/Wikidata:WikiProject_Ontology]
- [fact] Data on the Web Best Practices recommends explicit data provenance, identifiers, versioning, vocabularies, and discoverable metadata for web-published data. [source: https://www.w3.org/TR/dwbp/]
- [fact] Schema.org change control uses public discussion, steering-group approval, release snapshots, and term-level supersession metadata. [source: https://schema.org/docs/howwework.html]
- [fact] The repository's knowledge-curation-governance item concluded that authoritative knowledge capability needs named ownership, validation, publication, correction, and retirement stages. [source: https://davidamitchell.github.io/Research/research/2026-04-22-knowledge-curation-governance-for-regulated-ai.html]
- [inference] Production ontology governance should therefore include named owners, a public or at least reviewable proposal path, additive-first change, explicit deprecation, release metadata, and rollback-friendly publication surfaces rather than silent in-place redefinition. [source: https://www.w3.org/TR/dwbp/; https://schema.org/docs/howwework.html; https://www.wikidata.org/wiki/Wikidata:Property_proposal; https://davidamitchell.github.io/Research/research/2026-04-22-knowledge-curation-governance-for-regulated-ai.html]

#### 2.6 Runtime inference and performance trade-offs

- [fact] Stardog performs reasoning in a lazy late-binding fashion, does not materialize inferences, and rewrites queries with respect to the schema at query time. [source: https://docs.stardog.com/inference-engine/]
- [fact] Stardog documents data freshness, data size, fixed-schema rigidity, and truth-maintenance cost as disadvantages of materialization. [source: https://docs.stardog.com/inference-engine/]
- [fact] The repository's hosted graph-platform item established that GraphDB documents forward-chaining materialized reasoning while Stardog documents query-time reasoning. [source: https://davidamitchell.github.io/Research/research/2026-05-12-graph-db-saas-knowledge-ontology.html]
- [fact] The runtime-dependency item found that graph-derived caches and summaries need explicit freshness controls because propagation lag and rebuild lag are normal operational conditions. [source: https://davidamitchell.github.io/Research/research/2026-05-12-knowledge-graph-agentic-runtime-dependency.html]
- [inference] Query-time reasoning is better suited to evolving schemas, virtual graphs, and infrequently used higher-order entailments, while materialization is better suited to stable schemas and repeated low-latency reads over the same entailments. [source: https://docs.stardog.com/inference-engine/; https://davidamitchell.github.io/Research/research/2026-05-12-graph-db-saas-knowledge-ontology.html]
- [inference] For live multi-step AI agents, the safest compromise is to precompute cheap RDFS or OWL RL entailments when they are repeatedly needed, but keep heavier OWL reasoning off the synchronous control path unless the extra semantic precision changes a high-value decision. [source: https://www.w3.org/TR/owl2-profiles/; https://docs.stardog.com/inference-engine/; https://davidamitchell.github.io/Research/research/2026-05-12-knowledge-graph-agentic-runtime-dependency.html]

#### 2.7 Agent-facing consumption patterns

- [fact] Luo et al. describe three broad integration modes between Large Language Models and Knowledge Graphs: KG-enhanced LLMs, LLM-augmented KGs, and synergized systems where both play equal roles. [source: https://arxiv.org/abs/2306.08302]
- [fact] GraphRAG builds an entity Knowledge Graph from source documents and pregenerates community summaries that are later used to answer questions over the corpus. [source: https://arxiv.org/abs/2404.16130]
- [fact] JSON-LD is primarily intended for web-based programming environments and interoperable web services. [source: https://www.w3.org/TR/json-ld11/]
- [inference] Multi-step AI agents consume ontology-backed knowledge through three main surfaces: generated SPARQL over a live graph, serialized graph fragments such as JSON-LD or Turtle placed in context, and graph-derived natural-language summaries such as GraphRAG community reports. [source: https://arxiv.org/abs/2306.08302; https://arxiv.org/abs/2404.16130; https://www.w3.org/TR/json-ld11/; https://www.w3.org/TR/turtle/]
- [inference] Agent comprehensibility usually benefits more from well-labeled, moderately shallow ontologies with stable names and clear documentation than from exposing the full logical detail of an OWL-heavy backend inside prompts, because GraphRAG-style summary systems and web-oriented serializations already separate machine reasoning from human-readable or agent-readable presentation. [source: https://arxiv.org/abs/2404.16130; https://www.w3.org/TR/json-ld11/; https://www.w3.org/TR/skos-reference/; https://schema.org/docs/howwework.html]

#### 2.8 Cross-item integration

- [fact] The lifecycle-management item concluded that additive publication, provenance, and explicit freshness metadata are safer than silent mutation for graph-dependent systems. [source: https://davidamitchell.github.io/Research/research/2026-05-12-knowledge-graph-lifecycle-management-agentic.html]
- [fact] The schema-cross-session item argued for a small curated provenance-aware graph rather than maximal extraction. [source: https://davidamitchell.github.io/Research/research/2026-05-02-knowledge-graph-schema-cross-session-research-mcp.html]
- [inference] Those adjacent items sharpen the current conclusion: the ontology stack should stay minimal on the live path, because governance, provenance, freshness, and serving reliability all get harder as the graph becomes more semantically dense and operationally broad. [source: https://davidamitchell.github.io/Research/research/2026-05-12-knowledge-graph-lifecycle-management-agentic.html; https://davidamitchell.github.io/Research/research/2026-05-12-knowledge-graph-agentic-runtime-dependency.html; https://davidamitchell.github.io/Research/research/2026-05-02-knowledge-graph-schema-cross-session-research-mcp.html]

### §3 Reasoning

- [inference] The strongest evidence in this item comes from W3C specifications and public governance pages, because they directly define the modeling layers, profile purposes, and publication mechanics under discussion. [source: https://www.w3.org/TR/rdf12-concepts/; https://www.w3.org/TR/rdf12-schema/; https://www.w3.org/TR/owl2-profiles/; https://www.w3.org/TR/skos-reference/; https://www.w3.org/TR/dwbp/]
- [inference] The main synthesis step is not deciding whether one standard replaces the others, but determining which layer should own which concern: RDF and RDFS for the base graph model, OWL for bounded formal inference, SKOS for concept schemes, and Schema.org for external web-facing interchange. [source: https://www.w3.org/TR/rdf12-schema/; https://www.w3.org/TR/owl2-primer/; https://www.w3.org/TR/skos-reference/; https://schema.org/docs/about.html]
- [assumption] Most production teams can keep backend reasoning and prompt-facing representation as separate design surfaces, even when both surfaces are derived from the same underlying graph. [source: https://arxiv.org/abs/2404.16130; https://www.w3.org/TR/json-ld11/; https://docs.stardog.com/inference-engine/]

### §4 Consistency Check

- [inference] No consulted source contradicted the basic division of roles between RDF, RDFS, OWL, SKOS, and Schema.org; the disagreement is about implementation emphasis, not about whether those layers exist. [source: https://www.w3.org/TR/rdf12-concepts/; https://www.w3.org/TR/rdf12-schema/; https://www.w3.org/TR/owl2-primer/; https://www.w3.org/TR/skos-reference/; https://schema.org/docs/about.html]
- [inference] The most important unresolved gap is direct public benchmarking of how different ontology serializations or expressivity levels affect downstream AI-agent answer quality, because the accessible sources document architecture and semantics more clearly than controlled end-user performance outcomes. [source: https://arxiv.org/abs/2306.08302; https://arxiv.org/abs/2404.16130; https://www.w3.org/TR/json-ld11/]
- [inference] A repeated cross-item scan found no completed repository item that materially contradicted the conclusion that smaller, provenance-aware, versioned graph layers are safer than a maximally expressive live ontology stack. [source: https://davidamitchell.github.io/Research/research/2026-05-12-knowledge-graph-agentic-runtime-dependency.html; https://davidamitchell.github.io/Research/research/2026-05-12-knowledge-graph-lifecycle-management-agentic.html; https://davidamitchell.github.io/Research/research/2026-05-02-knowledge-graph-schema-cross-session-research-mcp.html]
- [inference] Overall confidence remains medium because the standards and governance evidence are strong, but several agent-comprehensibility conclusions still rely on architectural inference rather than on head-to-head public benchmarks. [source: https://www.w3.org/TR/owl2-profiles/; https://arxiv.org/abs/2306.08302; https://arxiv.org/abs/2404.16130]

### §5 Depth and Breadth Expansion

- [inference] Technical lens: ontology expressivity is valuable when it automates validation, subsumption, or rule application that would otherwise be coded manually, but it becomes a liability when every live query must traverse heavy reasoning to answer routine operational questions. [source: https://www.w3.org/TR/owl2-profiles/; https://docs.stardog.com/inference-engine/]
- [inference] Economic lens: vocabulary reuse and lightweight profiles lower long-run operating cost because they reduce custom modeling, reasoning overhead, and migration effort when teams need to publish or exchange graph data across tools. [source: https://lot.linkeddata.es/; https://www.w3.org/TR/dwbp/; https://www.w3.org/TR/swbp-vocab-pub/]
- [inference] Governance lens: ontology change control is not a documentation nicety but a production control surface, because release cadence, deprecation policy, and proposal review determine whether downstream services can trust identifiers and term meanings over time. [source: https://schema.org/docs/howwework.html; https://www.wikidata.org/wiki/Wikidata:Property_proposal; https://www.w3.org/TR/dwbp/]
- [inference] Historical lens: the stack evolved by accretion rather than replacement, so teams should compose it deliberately instead of expecting one standard to cover taxonomies, formal constraints, public web markup, provenance, and temporal modeling equally well. [source: https://www.w3.org/TR/rdf12-schema/; https://www.w3.org/TR/owl2-primer/; https://www.w3.org/TR/skos-reference/; https://schema.org/docs/about.html]
- [inference] Behavioral lens: prompt-facing systems handle simpler labels, hierarchies, and summaries more reliably than raw formal axioms, so ontology teams should keep a human-readable or agent-readable presentation layer alongside the richer backend semantics. [source: https://arxiv.org/abs/2404.16130; https://www.w3.org/TR/json-ld11/; https://www.w3.org/TR/skos-reference/]

### §6 Synthesis

**Executive summary:**

Use RDF and RDFS as the default production ontology layer, add SKOS for controlled vocabularies and Schema.org for external web-facing interchange, and introduce OWL only where a bounded inference benefit justifies the operational cost.[inference; source: https://www.w3.org/TR/rdf12-concepts/; https://www.w3.org/TR/rdf12-schema/; https://www.w3.org/TR/owl2-profiles/; https://www.w3.org/TR/skos-reference/; https://schema.org/docs/about.html]

Among OWL profiles, OWL 2 EL fits large hierarchical domain models, OWL 2 QL fits semantic access over relational data, and OWL 2 RL fits rule-engine-style production reasoning, while heavier OWL semantics should usually stay off the live agent control path.[inference; source: https://www.w3.org/TR/owl2-profiles/]

Ontology composition should start with reuse, not invention, by combining a small domain ontology with support vocabularies such as PROV-O, OWL-Time, DCAT, and FOAF, then publishing the result with stable URIs, version metadata, and deprecation discipline.[inference; source: https://www.w3.org/TR/prov-o/; https://www.w3.org/TR/owl-time/; https://www.w3.org/TR/vocab-dcat-3/; https://xmlns.com/foaf/spec/; https://www.w3.org/TR/swbp-vocab-pub/]

For multi-step AI agents, simpler serializations and graph-derived summaries are usually more usable at the interface layer than raw formal axioms, so teams should separate backend semantic rigor from prompt-facing representation and governance.[inference; source: https://www.w3.org/TR/json-ld11/; https://www.w3.org/TR/turtle/; https://arxiv.org/abs/2404.16130; https://schema.org/docs/howwework.html]

**Key findings:**

1. **RDF and RDFS provide the baseline graph and schema functions that many interoperable operational Knowledge Graphs need before any richer logic is added, including the graph model, reusable vocabulary terms, hierarchy mechanisms, and named-graph structure.** ([inference]; medium confidence; source: https://www.w3.org/TR/rdf12-concepts/; https://www.w3.org/TR/rdf12-schema/)
2. **OWL is most defensible when tied to a specific reasoning requirement rather than treated as one undifferentiated layer, because the W3C profiles divide production-oriented use into large-hierarchy reasoning in OWL 2 EL, query rewriting in OWL 2 QL, and rule-engine reasoning in OWL 2 RL.** ([inference]; medium confidence; source: https://www.w3.org/TR/owl2-profiles/; https://www.w3.org/TR/owl2-primer/)
3. **SKOS is the right semantic layer for thesauri, taxonomies, labels, and concept mappings, but it is not a substitute for a formal domain ontology when the system needs constraints or logically grounded inference.** ([inference]; medium confidence; source: https://www.w3.org/TR/skos-reference/)
4. **Schema.org is most useful at publication and interchange boundaries, because its governance, release process, and supersession model are optimized for broad web consensus and structured-data compatibility rather than for tightly constrained internal operational semantics.** ([inference]; medium confidence; source: https://schema.org/docs/about.html; https://schema.org/docs/howwework.html)
5. **Ontology composition should begin with reuse of support vocabularies such as PROV-O, OWL-Time, DCAT, and FOAF, because those vocabularies already solve common provenance, temporal, catalog, and actor-modeling problems that otherwise become costly custom extensions.** ([inference]; high confidence; source: https://www.w3.org/TR/prov-o/; https://www.w3.org/TR/owl-time/; https://www.w3.org/TR/vocab-dcat-3/; https://xmlns.com/foaf/spec/; https://lot.linkeddata.es/)
6. **Production ontology governance needs named owners, proposal review, additive-first change, explicit deprecation, and versioned publication surfaces, because both Schema.org and Wikidata evolve through visible community or steering-group processes instead of silent term redefinition.** ([inference]; medium confidence; source: https://schema.org/docs/howwework.html; https://www.wikidata.org/wiki/Wikidata:Property_proposal; https://www.wikidata.org/wiki/Wikidata:Creating_a_property_proposal; https://www.w3.org/TR/dwbp/)
7. **The right inference strategy depends on freshness and latency demands, because query-time reasoning is more flexible for evolving schemas while materialization is better for repeated low-latency reads over stable entailments.** ([inference]; medium confidence; source: https://docs.stardog.com/inference-engine/; https://davidamitchell.github.io/Research/research/2026-05-12-graph-db-saas-knowledge-ontology.html; https://davidamitchell.github.io/Research/research/2026-05-12-knowledge-graph-agentic-runtime-dependency.html)
8. **Multi-step AI agents usually consume ontology-backed knowledge through SPARQL, serialized graph fragments such as JSON-LD or Turtle, or graph-derived summaries, which means prompt-facing comprehensibility often depends more on presentation choices than on the full backend logical expressivity.** ([inference]; medium confidence; source: https://arxiv.org/abs/2306.08302; https://arxiv.org/abs/2404.16130; https://www.w3.org/TR/json-ld11/; https://www.w3.org/TR/turtle/)

**Evidence map:**

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [inference] RDF and RDFS provide the baseline graph and schema functions many operational graph systems need before any richer logic is added. | https://www.w3.org/TR/rdf12-concepts/; https://www.w3.org/TR/rdf12-schema/ | medium | Baseline modeling layer |
| [inference] OWL is best justified through profile-specific operating needs, because OWL 2 EL, OWL 2 QL, and OWL 2 RL target different reasoning modes. | https://www.w3.org/TR/owl2-profiles/; https://www.w3.org/TR/owl2-primer/ | medium | Profile-specific role split |
| [inference] SKOS fits concept schemes and mappings better than formal domain constraints or rich operational axioms. | https://www.w3.org/TR/skos-reference/ | medium | Based on the specification's explicit scope boundary |
| [inference] Schema.org is best used at interchange boundaries rather than as the only internal canonical ontology. | https://schema.org/docs/about.html; https://schema.org/docs/howwework.html | medium | Governance and scope shape the inference |
| [inference] Reusing PROV-O, OWL-Time, DCAT, and FOAF is cheaper and safer than rebuilding those cross-cutting semantics in a custom ontology. | https://www.w3.org/TR/prov-o/; https://www.w3.org/TR/owl-time/; https://www.w3.org/TR/vocab-dcat-3/; https://xmlns.com/foaf/spec/; https://lot.linkeddata.es/ | high | Reuse-first composition pattern |
| [inference] Ontology governance should use proposal review, versioning, and explicit deprecation because public ontology programs already rely on those controls. | https://schema.org/docs/howwework.html; https://www.wikidata.org/wiki/Wikidata:Property_proposal; https://www.wikidata.org/wiki/Wikidata:Creating_a_property_proposal; https://www.w3.org/TR/dwbp/ | medium | Governance-surface synthesis |
| [inference] Query-time reasoning suits evolving schemas, while materialization suits stable, repeated low-latency entailments. | https://docs.stardog.com/inference-engine/; https://davidamitchell.github.io/Research/research/2026-05-12-graph-db-saas-knowledge-ontology.html; https://davidamitchell.github.io/Research/research/2026-05-12-knowledge-graph-agentic-runtime-dependency.html | medium | Runtime trade-off rather than single-source rule |
| [inference] Agent-facing consumption usually happens through SPARQL, serialized graph fragments, or graph-derived summaries rather than through direct exposure to the full formal ontology. | https://arxiv.org/abs/2306.08302; https://arxiv.org/abs/2404.16130; https://www.w3.org/TR/json-ld11/; https://www.w3.org/TR/turtle/ | medium | Interface-layer synthesis |

**Assumptions:**

- [assumption] Most production teams can keep backend semantic reasoning and prompt-facing graph presentation as separate design surfaces. [source: https://arxiv.org/abs/2404.16130; https://www.w3.org/TR/json-ld11/]
- [assumption] For live multi-step AI agents, latency and freshness usually matter more than extracting every logically possible entailment from an expressive ontology. [source: https://docs.stardog.com/inference-engine/; https://davidamitchell.github.io/Research/research/2026-05-12-knowledge-graph-agentic-runtime-dependency.html]

**Analysis:**

The evidence supports a layered stack rather than a one-standard answer, because the consulted specifications divide responsibilities cleanly between graph representation, lightweight schema, formal inference, concept schemes, and web-scale publication vocabularies.[inference; source: https://www.w3.org/TR/rdf12-concepts/; https://www.w3.org/TR/rdf12-schema/; https://www.w3.org/TR/owl2-profiles/; https://www.w3.org/TR/skos-reference/; https://schema.org/docs/about.html]

The practical decision is therefore not "OWL or not" but which concern deserves formal reasoning, which concern only needs controlled labels or mappings, and which concern belongs to public interchange rather than to the internal canonical model.[inference; source: https://www.w3.org/TR/owl2-primer/; https://www.w3.org/TR/skos-reference/; https://schema.org/docs/howwework.html]

The main trade-off is semantic rigor versus operational friction: heavier reasoning and custom ontologies can encode more precise meaning, but they raise query cost, publication complexity, and change-management burden, while a narrower reuse-first stack stays easier to operate and explain.[inference; source: https://www.w3.org/TR/owl2-profiles/; https://lot.linkeddata.es/; https://docs.stardog.com/inference-engine/; https://www.w3.org/TR/swbp-vocab-pub/]

Alternative approaches, such as using Schema.org alone or exposing a richly axiomatized OWL backend directly to prompts, remain possible, but the consulted evidence gives stronger support to a split design where formal semantics power validation and inference behind the scenes while simpler labels, serializations, and summaries power agent interaction.[inference; source: https://schema.org/docs/howwework.html; https://arxiv.org/abs/2404.16130; https://www.w3.org/TR/json-ld11/; https://www.w3.org/TR/skos-reference/]

**Risks, gaps, uncertainties:**

- Direct public benchmarks comparing agent performance across Turtle, JSON-LD, RDF/XML, and other serializations remain thin, so the agent-comprehensibility conclusions here are architectural inferences rather than experimentally settled facts.[inference; source: https://www.w3.org/TR/json-ld11/; https://www.w3.org/TR/turtle/; https://www.w3.org/TR/rdf-syntax-grammar/; https://arxiv.org/abs/2404.16130]
- The materialization side of the reasoning trade-off relies more on prior repository synthesis and indirect documentation than on directly consulted primary materialization documentation in this item, so platform-specific detail is less certain than the broader architectural trade-off.[inference; source: https://davidamitchell.github.io/Research/research/2026-05-12-graph-db-saas-knowledge-ontology.html; https://docs.stardog.com/inference-engine/]
- The LOT process evidence in this item comes from the official methodology site and DOI metadata rather than from a full article text, so enterprise-framework detail is thinner than the standards and governance evidence elsewhere in the item.[inference; source: https://lot.linkeddata.es/; https://doi.org/10.1016/j.engappai.2022.104755]

**Open questions:**

- What is the best prompt-formatting pattern for exposing graph fragments to LLM agents while preserving provenance and minimizing token cost?
- How much practical answer-quality gain do OWL 2 RL or OWL 2 EL entailments deliver over plain RDF and RDFS in live agent workflows?
- Which ontology-diff and deprecation tools best support additive-first release management for small Knowledge Graph teams?

### §7 Recursive Review

```text
review_result: recorded
acronym_audit: completed
domain_term_audit: completed
claim_audit: completed
source_audit: completed
cross_item_sweep: completed
```

---

## Findings

### Executive Summary

Start a production Knowledge Graph for multi-step Artificial Intelligence (AI) agents with RDF and RDFS, then layer in SKOS, Schema.org, or OWL only when a specific taxonomy, interchange, or reasoning need appears.[inference; source: https://www.w3.org/TR/rdf12-concepts/; https://www.w3.org/TR/rdf12-schema/; https://www.w3.org/TR/owl2-profiles/; https://www.w3.org/TR/skos-reference/; https://schema.org/docs/about.html]

That usually means SKOS for concept navigation, Schema.org at publication edges, and OWL only where formal entailment materially improves validation, subsumption, or rule execution.[inference; source: https://www.w3.org/TR/skos-reference/; https://schema.org/docs/howwework.html; https://www.w3.org/TR/owl2-primer/]

Teams usually get a more durable design by reusing support vocabularies such as PROV-O, OWL-Time, DCAT, and FOAF instead of rebuilding common provenance, time, catalog, and actor semantics from scratch.[inference; source: https://www.w3.org/TR/prov-o/; https://www.w3.org/TR/owl-time/; https://www.w3.org/TR/vocab-dcat-3/; https://xmlns.com/foaf/spec/; https://lot.linkeddata.es/]

Prompt-facing workflows generally work better with bounded graph fragments, serializations, or graph-derived summaries than with raw axioms, so most semantic complexity should remain behind the interaction layer.[inference; source: https://www.w3.org/TR/json-ld11/; https://www.w3.org/TR/turtle/; https://arxiv.org/abs/2404.16130; https://arxiv.org/abs/2306.08302]

### Key Findings

1. **RDF plus RDFS already cover the baseline graph and schema functions that many operational Knowledge Graphs need, including reusable vocabulary terms, lightweight hierarchy semantics, and named-graph structure, before any heavier reasoning layer is introduced.** ([inference]; medium confidence; source: https://www.w3.org/TR/rdf12-concepts/; https://www.w3.org/TR/rdf12-schema/)
2. **OWL is easiest to justify when attached to a specific reasoning requirement, because its tractable profiles correspond to different execution patterns: OWL 2 EL for large hierarchies, OWL 2 QL for relational query rewriting, and OWL 2 RL for scalable rule application.** ([inference]; medium confidence; source: https://www.w3.org/TR/owl2-profiles/; https://www.w3.org/TR/owl2-primer/)
3. **SKOS is strongest for organizing concepts, labels, broader-narrower links, and vocabulary mappings, but once a graph needs formal constraints or richer entailment, a domain ontology layer has to carry that extra semantic load.** ([inference]; medium confidence; source: https://www.w3.org/TR/skos-reference/)
4. **Schema.org delivers the most value at web publication boundaries, where broad ecosystem recognition matters, but its consensus-oriented release model makes it a loose interchange vocabulary rather than a precise internal source of truth for operational entities.** ([inference]; medium confidence; source: https://schema.org/docs/about.html; https://schema.org/docs/howwework.html)
5. **A small domain ontology usually stays maintainable longer when it imports support vocabularies instead of recreating them, because PROV-O, OWL-Time, DCAT, and FOAF already cover recurring provenance, temporal, catalog, and actor semantics.** ([inference]; high confidence; source: https://www.w3.org/TR/prov-o/; https://www.w3.org/TR/owl-time/; https://www.w3.org/TR/vocab-dcat-3/; https://xmlns.com/foaf/spec/; https://lot.linkeddata.es/)
6. **Once graph terms affect live systems, ontology governance has to behave like release management, with named ownership, proposal review, additive evolution, explicit deprecation, and published versions rather than silent semantic drift.** ([inference]; medium confidence; source: https://schema.org/docs/howwework.html; https://www.wikidata.org/wiki/Wikidata:Property_proposal; https://www.wikidata.org/wiki/Wikidata:Creating_a_property_proposal; https://www.w3.org/TR/dwbp/)
7. **Reasoning strategy should be selected from workload shape rather than ontology purity, because query-time inference helps when schemas change often, while materialized entailments make more sense when the same derived facts are read repeatedly under tight latency targets.** ([inference]; medium confidence; source: https://docs.stardog.com/inference-engine/; https://davidamitchell.github.io/Research/research/2026-05-12-graph-db-saas-knowledge-ontology.html; https://davidamitchell.github.io/Research/research/2026-05-12-knowledge-graph-agentic-runtime-dependency.html)
8. **Application-facing agents rarely need raw axioms directly, because they usually perform better with query results, bounded graph fragments, or graph-derived summaries than with the ontology's full formal machinery exposed at prompt time.** ([inference]; medium confidence; source: https://arxiv.org/abs/2306.08302; https://arxiv.org/abs/2404.16130; https://www.w3.org/TR/json-ld11/; https://www.w3.org/TR/turtle/)

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [inference] RDF and RDFS provide the baseline graph and schema functions many operational graph systems need before any richer logic is added. | https://www.w3.org/TR/rdf12-concepts/; https://www.w3.org/TR/rdf12-schema/ | medium | Baseline modeling layer |
| [inference] OWL is best justified through profile-specific operating needs, because OWL 2 EL, OWL 2 QL, and OWL 2 RL target different reasoning modes. | https://www.w3.org/TR/owl2-profiles/; https://www.w3.org/TR/owl2-primer/ | medium | Profile-specific role split |
| [inference] SKOS fits concept schemes and mappings better than formal domain constraints or rich operational axioms. | https://www.w3.org/TR/skos-reference/ | medium | Based on the specification's explicit scope boundary |
| [inference] Schema.org is best used at interchange boundaries rather than as the only internal canonical ontology. | https://schema.org/docs/about.html; https://schema.org/docs/howwework.html | medium | Governance and scope shape the inference |
| [inference] Reusing PROV-O, OWL-Time, DCAT, and FOAF is cheaper and safer than rebuilding those cross-cutting semantics in a custom ontology. | https://www.w3.org/TR/prov-o/; https://www.w3.org/TR/owl-time/; https://www.w3.org/TR/vocab-dcat-3/; https://xmlns.com/foaf/spec/; https://lot.linkeddata.es/ | high | Reuse-first composition pattern |
| [inference] Ontology governance should use proposal review, versioning, and explicit deprecation because public ontology programs already rely on those controls. | https://schema.org/docs/howwework.html; https://www.wikidata.org/wiki/Wikidata:Property_proposal; https://www.wikidata.org/wiki/Wikidata:Creating_a_property_proposal; https://www.w3.org/TR/dwbp/ | medium | Governance-surface synthesis |
| [inference] Query-time reasoning suits evolving schemas, while materialization suits stable, repeated low-latency entailments. | https://docs.stardog.com/inference-engine/; https://davidamitchell.github.io/Research/research/2026-05-12-graph-db-saas-knowledge-ontology.html; https://davidamitchell.github.io/Research/research/2026-05-12-knowledge-graph-agentic-runtime-dependency.html | medium | Runtime trade-off rather than single-source rule |
| [inference] Agent-facing consumption usually happens through SPARQL, serialized graph fragments, or graph-derived summaries rather than through direct exposure to the full formal ontology. | https://arxiv.org/abs/2306.08302; https://arxiv.org/abs/2404.16130; https://www.w3.org/TR/json-ld11/; https://www.w3.org/TR/turtle/ | medium | Interface-layer synthesis |

### Assumptions

- [assumption] Most production teams can keep backend semantic reasoning and prompt-facing graph presentation as separate design surfaces. **Justification:** GraphRAG and JSON-LD both assume a representational layer that is not identical to the full internal graph semantics. [source: https://arxiv.org/abs/2404.16130; https://www.w3.org/TR/json-ld11/]
- [assumption] For live multi-step AI agents, latency and freshness usually matter more than extracting every logically possible entailment from an expressive ontology. **Justification:** the consulted runtime and reasoning sources document explicit freshness and query-cost trade-offs but do not argue for maximal live entailment as a universal default. [source: https://docs.stardog.com/inference-engine/; https://davidamitchell.github.io/Research/research/2026-05-12-knowledge-graph-agentic-runtime-dependency.html]

### Analysis

The standards evidence points to deliberate layering, not semantic maximalism, because RDF, RDFS, OWL, SKOS, and Schema.org each solve a different modeling problem and none of the consulted primary sources claims to replace all of the others.[inference; source: https://www.w3.org/TR/rdf12-concepts/; https://www.w3.org/TR/rdf12-schema/; https://www.w3.org/TR/owl2-primer/; https://www.w3.org/TR/skos-reference/; https://schema.org/docs/about.html]

That makes ontology choice a systems-design problem rather than a standards-loyalty problem.[inference; source: https://www.w3.org/TR/owl2-profiles/; https://www.w3.org/TR/dwbp/]

If the graph needs only shared identifiers, labels, and lightweight hierarchy, RDF plus RDFS, with optional SKOS, is enough.[inference; source: https://www.w3.org/TR/rdf12-schema/; https://www.w3.org/TR/skos-reference/]

If the graph must support formal validation, subsumption, or reusable rule patterns, OWL belongs in the design, but usually through a tractable profile and often behind a cache, materialization job, or query-rewriting layer rather than inside every live agent step.[inference; source: https://www.w3.org/TR/owl2-profiles/; https://docs.stardog.com/inference-engine/; https://davidamitchell.github.io/Research/research/2026-05-12-knowledge-graph-agentic-runtime-dependency.html]

The governance conclusion follows the same logic: once identifiers and term meanings become operational dependencies, ontology change must move through visible review, release, and deprecation controls rather than through ad hoc edits.[inference; source: https://schema.org/docs/howwework.html; https://www.wikidata.org/wiki/Wikidata:Property_proposal; https://www.w3.org/TR/dwbp/]

### Risks, Gaps, and Uncertainties

- Public evidence directly comparing agent answer quality across different ontology serializations remains limited, so the prompt-facing serialization guidance here rests on architecture and tooling evidence rather than on large benchmark suites.[inference; source: https://www.w3.org/TR/json-ld11/; https://www.w3.org/TR/turtle/; https://arxiv.org/abs/2404.16130]
- The materialization side of the reasoning trade-off is supported here partly through a prior repository synthesis rather than through a directly consulted public GraphDB inferencing page, which lowers confidence in platform-specific detail even though the broader trade-off remains well grounded.[inference; source: https://davidamitchell.github.io/Research/research/2026-05-12-graph-db-saas-knowledge-ontology.html; https://docs.stardog.com/inference-engine/]
- The accessible LOT evidence comes from the official methodology site rather than from a full direct reading of the journal article, so its process claims should be treated as official-framework guidance rather than as a line-by-line paper synthesis.[inference; source: https://lot.linkeddata.es/; https://doi.org/10.1016/j.engappai.2022.104755]

### Open Questions

- Which ontology-diff and deprecation tools are most effective for small Knowledge Graph teams that do not have a dedicated ontology platform?
- What is the best token-efficient format for exposing provenance-rich graph fragments to LLM agents?
- Under what workload does precomputed OWL RL inference outperform lightweight query rewriting for live agent workflows?

---

## Output

- Type: knowledge
- Description: Decision guide for selecting and governing RDF, RDFS, OWL, SKOS, and Schema.org layers in a production Knowledge Graph used by multi-step AI agents.[inference; source: https://www.w3.org/TR/owl2-profiles/; https://www.w3.org/TR/skos-reference/; https://schema.org/docs/howwework.html]
- Links:
  - https://www.w3.org/TR/owl2-profiles/
  - https://www.w3.org/TR/skos-reference/
  - https://schema.org/docs/howwework.html
