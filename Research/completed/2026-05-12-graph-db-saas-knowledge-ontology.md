---
review_count: 2
title: "Hosted Software-as-a-Service (SaaS) graph database options for knowledge ontology"
added: 2026-05-12T03:22:49+00:00
status: completed
priority: medium
blocks: []
tags: [knowledge-graph]
started: 2026-05-12T09:30:23+00:00
completed: 2026-05-12T10:00:47+00:00
output: [knowledge]
cites:
  - 2026-05-02-knowledge-graph-schema-cross-session-research-mcp
  - 2026-03-03-knowledge-representation-agent-context
  - 2026-03-12-hosting-options-for-the-research-repo
related:
  - 2026-03-03-knowledge-linking-connected-corpus
  - 2026-04-29-knowledge-scaffolding-context-engineering
superseded_by: ~
supersedes: ~
item_type: primary
confidence: medium
versions:
  - version: "1.0"
    sha: fc0d011cf1e4cc81311228510f6ec75f78cfea02
    changed: 2026-05-12
    progress: progress/2026-05-12-graph-db-saas-knowledge-ontology.md
    summary: Initial completion
---

# Hosted Software-as-a-Service (SaaS) graph database options for knowledge ontology

## Research Question

Which hosted Software-as-a-Service (SaaS) graph database platforms are suitable for building and querying a knowledge ontology, and how do they compare on data model support, query language, pricing, and integration options?

## Scope

**In scope:**
- Hosted graph database platforms available in 2025-2026, with no infrastructure to manage directly
- Both property graph systems, meaning nodes and edges with key-value properties, and Resource Description Framework (RDF) or Web Ontology Language (OWL) systems, meaning triple-based semantic graph stores and formal ontology vocabularies
- Comparison on query language support, including SPARQL Protocol and RDF Query Language (SPARQL), ontology reasoning support, pricing tier shape, scale limits, authentication model, Application Programming Interface (API) access, and Python Software Development Kit (SDK) or driver availability
- Data import and export support relevant to bootstrapping or migrating an ontology

**Out of scope:**
- Self-hosted or on-premises graph database deployments
- Relational databases with graph extensions
- General-purpose document or vector stores that are not graph-first
- Graph analytics and business intelligence platforms whose primary value is large-scale analytical processing rather than ontology management, including TigerGraph as an evaluation target for final recommendation

**Constraints:**
- Focus on managed offerings with a hosted experience; developer trials or free tiers are preferred for initial evaluation
- Prefer primary documentation and official product materials, with independent interpretation only where the documentation leaves trade-offs implicit

## Context

The repository currently manages research as Markdown files plus Python tooling rather than as a formal graph store. [fact; source: https://github.com/davidamitchell/Research/blob/main/README.md]

The prior cross-session schema item concluded that a small curated knowledge graph can improve provenance and concept reuse, which makes the choice of hosted graph platform decision-relevant for future tooling. [inference; source: https://davidamitchell.github.io/Research/research/2026-05-02-knowledge-graph-schema-cross-session-research-mcp.html]

## Approach

1. Enumerate current hosted graph platforms that materially fit ontology or knowledge graph work.
2. Separate ontology-first platforms from property-graph-first platforms and dual-model platforms.
3. Compare supported data models and query languages.
4. Compare reasoning support, especially native RDF Schema (RDFS) or OWL support.
5. Compare pricing shape, free-tier availability, and integration friction.
6. Compare import, export, and Python integration paths.
7. Recommend the best platform for this repository's current research-tracking use case.

## Sources

- [x] [Neo4j AuraDB product page](https://neo4j.com/cloud/platform/aura-graph-database/)
- [x] [Neo4j Aura importing data](https://neo4j.com/docs/aura/classic/auradb/importing-data/)
- [x] [Neo4j Python driver manual](https://neo4j.com/docs/python-manual/current/)
- [x] [Neo4j Cypher LOAD CSV clause](https://neo4j.com/docs/cypher-manual/current/clauses/load-csv/)
- [x] [Amazon Neptune introduction](https://docs.aws.amazon.com/neptune/latest/userguide/intro.html)
- [x] [Amazon Neptune bulk loader](https://docs.aws.amazon.com/neptune/latest/userguide/bulk-load.html)
- [x] [Amazon Neptune IAM authentication](https://docs.aws.amazon.com/neptune/latest/userguide/iam-auth.html)
- [x] [Amazon Neptune pricing](https://aws.amazon.com/neptune/pricing/)
- [x] [Stardog Cloud](https://www.stardog.com/stardog-cloud/)
- [x] [Stardog query documentation](https://docs.stardog.com/query-stardog)
- [x] [Stardog inference engine documentation](https://docs.stardog.com/inference-engine)
- [x] [Ontotext GraphDB OWL compliance](https://graphdb.ontotext.com/documentation/11.0/owl-compliance.html)
- [x] [Ontotext GraphDB reasoning](https://graphdb.ontotext.com/documentation/master/reasoning.html)
- [x] [Ontotext GraphDB loading and querying data](https://graphdb.ontotext.com/documentation/11.0/loading-querying-data.html)
- [x] [Ontotext GraphDB loading and updating data](https://graphdb.ontotext.com/documentation/10.1/loading-and-updating-data.html)
- [x] [TigerGraph pricing](https://www.tigergraph.com/pricing/)
- [x] [TigerGraph Savanna overview](https://docs.tigergraph.com/savanna/main/overview/)
- [x] [TigerGraph query language page](https://www.tigergraph.com/gsql/)
- [x] [Memgraph pricing](https://memgraph.com/pricing)
- [x] [Memgraph data migration](https://memgraph.com/docs/data-migration)
- [x] [Memgraph client libraries](https://memgraph.com/docs/client-libraries)
- [x] [Memgraph differences in Cypher implementations](https://memgraph.com/docs/querying/differences-in-cypher-implementations)
- [x] [World Wide Web Consortium (W3C) SKOS reference](https://www.w3.org/TR/skos-reference/)
- [x] [World Wide Web Consortium (W3C) SHACL recommendation](https://www.w3.org/TR/shacl/)
- [x] [metaphacts product page](https://www.metaphacts.com/product)
- [x] [Mitchell (2026) What entity-relation schema and write/query patterns best support cross-session research provenance and concept reuse for an Artificial Intelligence (AI) agent using the Model Context Protocol (MCP) memory server?](https://davidamitchell.github.io/Research/research/2026-05-02-knowledge-graph-schema-cross-session-research-mcp.html)
- [x] [Mitchell (2026) Knowledge Representation for Agent Context: LSE, Knowledge Graphs, Concept Maps, and Document Compression for Large-Scale Context Management](https://davidamitchell.github.io/Research/research/2026-03-03-knowledge-representation-agent-context.html)
- [x] [Mitchell (2026) Hosting options for the Research repo](https://davidamitchell.github.io/Research/research/2026-03-12-hosting-options-for-the-research-repo.html)

---

## Research Skill Output

*(Full output from running the research skill, retained verbatim in the completed item. Sections 0-5 are the investigation, and section 6 seeds the Findings section below.)*

### §0 Initialise

- Question: determine which hosted graph database platforms are suitable for a knowledge ontology, and compare them on data model support, query language, pricing, reasoning, and integration.
- Scope: hosted graph databases only; ontology-first, property-graph-first, and dual-model managed services are in scope; self-hosted systems, relational graph extensions, and analytics-first platforms as final recommendations are out of scope.
- Constraints: prefer primary documentation; prioritize managed services with low-friction trials when possible; expand every acronym on first use.
- Output format: full section 0 to section 7 investigation plus Findings with Executive Summary, Key Findings, Evidence Map, Assumptions, Analysis, Risks, Gaps, Uncertainties, Open Questions, and Output.
- [inference] Prior completed-item cross-reference: the most relevant repository items are the cross-session schema item, which argues for a small curated graph with strong provenance, the knowledge-representation item, which separates property-graph retrieval from more formal semantic layers, and the hosting-options item, which already treated managed graph services as a deployment trade-off for this repository. [source: https://davidamitchell.github.io/Research/research/2026-05-02-knowledge-graph-schema-cross-session-research-mcp.html; https://davidamitchell.github.io/Research/research/2026-03-03-knowledge-representation-agent-context.html; https://davidamitchell.github.io/Research/research/2026-03-12-hosting-options-for-the-research-repo.html]
- [inference] Working definition: for this item, a suitable ontology platform is a hosted graph database or semantic graph service that can store a reusable domain model, represent typed entities and relationships, and support standards-based or clearly documented query paths for later integration from Python services. [source: https://docs.aws.amazon.com/neptune/latest/userguide/intro.html; https://www.stardog.com/platform/; https://graphdb.ontotext.com/documentation/11.0/loading-querying-data.html]

### §1 Question Decomposition

- A. Platform fit
  - A1. Which hosted services are property-graph-first, ontology-first, or dual-model?
  - A2. Which services are adjacent knowledge-graph applications rather than core graph databases?
- B. Data model and query surface
  - B1. Which services support property graphs, and which support RDF or OWL?
  - B2. Which query languages are first-class for each service?
- C. Reasoning and ontology support
  - C1. Which services explicitly document native RDF Schema (RDFS) or OWL reasoning?
  - C2. Which services expose graph traversal but not formal ontology reasoning?
- D. Cost and access
  - D1. Which services have a documented free tier or trial?
  - D2. Which services expose transparent public pricing versus quote-based enterprise pricing?
- E. Integration and portability
  - E1. Which services have direct Python integration or standards-based remote query endpoints?
  - E2. Which services support import and export paths suitable for ontology bootstrapping or migration?
- F. Recommendation
  - F1. Which platform is the best ontology-first fit for this repository?
  - F2. Which alternative is best if formal ontology reasoning proves unnecessary?

### §2 Investigation

#### 2.1 Use-case criteria and prior repository context

- [fact] The prior repository schema item recommends a curated, provenance-aware graph rather than a maximal enterprise knowledge store, which makes early-stage developer access, manageable pricing, and standards clarity more important than extreme scale for this repository's first hosted graph choice. [source: https://davidamitchell.github.io/Research/research/2026-05-02-knowledge-graph-schema-cross-session-research-mcp.html]
- [fact] The prior knowledge-representation item distinguishes property graphs from more formal semantic layers and argues that different abstractions suit different retrieval needs, which is directly relevant to choosing between Cypher-first platforms and RDF or OWL platforms here. [source: https://davidamitchell.github.io/Research/research/2026-03-03-knowledge-representation-agent-context.html]
- [assumption] The first production use of a hosted graph for this repository will remain modest in scale and Python-driven, because the current corpus is a research repository rather than a transaction-heavy enterprise system and the current tooling stack is Python-first. [source: https://github.com/davidamitchell/Research/blob/main/README.md; https://davidamitchell.github.io/Research/research/2026-05-02-knowledge-graph-schema-cross-session-research-mcp.html]

#### 2.2 Property-graph-first managed services

- [fact] Neo4j AuraDB is a fully managed native property graph service that emphasizes Cypher, flexible schema, graph algorithms, backups, multi-cloud deployment, and official language drivers including Python. [source: https://neo4j.com/cloud/platform/aura-graph-database/; https://neo4j.com/docs/python-manual/current/]
- [fact] Neo4j Aura exposes managed import paths through its data importer, supports CSV import, supports API-driven import jobs in Aura, and documents `LOAD CSV` for remote CSV ingestion. [source: https://neo4j.com/docs/aura/classic/auradb/importing-data/; https://neo4j.com/docs/cypher-manual/current/clauses/load-csv/]
- [inference] Neo4j Aura is strong for application-centric property graphs and developer ergonomics, but the consulted official material does not position it as an ontology-first platform with native OWL or RDFS reasoning, so it is a weaker fit where formal ontology semantics are a hard requirement. [source: https://neo4j.com/cloud/platform/aura-graph-database/; https://neo4j.com/docs/python-manual/current/]
- [fact] Memgraph Cloud is a managed graph offering for developers and small teams, with fully managed hosting, automatic backups and updates, and instance sizes from 1 GB to 32 GB RAM; the broader Memgraph platform uses openCypher-style querying and exposes Python client access through its documented client libraries. [source: https://memgraph.com/pricing; https://memgraph.com/docs/client-libraries; https://memgraph.com/docs/querying/differences-in-cypher-implementations]
- [fact] Memgraph documents import and migration support for CSV, JSON Lines (JSONL), Parquet, S3-backed data, relational systems, and direct Neo4j migration, which gives it stronger raw ingestion flexibility than most of the other property-graph-first platforms in this review. [source: https://memgraph.com/docs/data-migration]
- [inference] Memgraph Cloud is well suited to Cypher-compatible graph application prototyping and migration from Neo4j, but the consulted documentation does not establish native ontology reasoning or RDF-first semantics, so it is not an ontology-first recommendation. [source: https://memgraph.com/pricing; https://memgraph.com/docs/data-migration; https://memgraph.com/docs/querying/differences-in-cypher-implementations]
- [fact] TigerGraph Savanna is a managed cloud graph service with public pricing, TigerGraph's own query language, Cypher, and Graph Query Language (GQL) support, hybrid graph and vector search, large workspaces, and high-availability enterprise positioning. [source: https://www.tigergraph.com/pricing/; https://www.tigergraph.com/gsql/; https://docs.tigergraph.com/savanna/main/overview/]
- [inference] TigerGraph remains outside the final shortlist for this item because its current official positioning centers enterprise-scale graph analytics and analytical workspaces more than ontology engineering, and the item scope explicitly excludes analytics-first platforms from the final recommendation. [source: https://www.tigergraph.com/pricing/; https://www.tigergraph.com/gsql/]

#### 2.3 Dual-model managed service

- [fact] Amazon Neptune is a fully managed graph database that supports property graphs through Gremlin and openCypher, and RDF graphs through SPARQL, which makes it the only clearly documented dual-model managed service in the consulted evidence set. [source: https://docs.aws.amazon.com/neptune/latest/userguide/intro.html]
- [fact] Neptune bulk loading requires Amazon Simple Storage Service (Amazon S3), an AWS Identity and Access Management (IAM) role, and a Virtual Private Cloud (VPC) endpoint, and supports RDF and Gremlin-oriented bulk formats through the Neptune loader path. [source: https://docs.aws.amazon.com/neptune/latest/userguide/bulk-load.html]
- [fact] Neptune authentication can use IAM-signed requests, and Neptune pricing is usage-based across instance hours, storage, input and output operations, backups, and serverless capacity, with a 30-day Amazon Web Services (AWS) free-trial allowance rather than a permanent self-serve free tier. [source: https://docs.aws.amazon.com/neptune/latest/userguide/iam-auth.html; https://aws.amazon.com/neptune/pricing/]
- [inference] Neptune is compelling where dual-model support and AWS integration matter more than self-serve developer simplicity, but the consulted official material emphasizes model and query support rather than explicit native OWL or RDFS reasoning, so its ontology story is weaker than dedicated semantic platforms. [source: https://docs.aws.amazon.com/neptune/latest/userguide/intro.html; https://docs.aws.amazon.com/neptune/latest/userguide/bulk-load.html]

#### 2.4 Ontology-first managed services

- [fact] Stardog Cloud is offered as a managed semantic platform with a free learning environment, shared hosting, up to 1 million stored edges on the free plan, and a custom-priced enterprise tier with dedicated hosting and broader authentication options. [source: https://www.stardog.com/stardog-cloud/]
- [fact] Stardog documents SPARQL 1.1 support, OWL and rule reasoning, and query-time inference, where inferences are computed at query time instead of materialized into stored triples. [source: https://docs.stardog.com/query-stardog; https://docs.stardog.com/inference-engine]
- [fact] Stardog's broader platform documentation emphasizes RDF open standards, SPARQL, GraphQL, data virtualization, and an inference engine designed for explainable knowledge-graph use cases. [source: https://www.stardog.com/platform/]
- [inference] Stardog is the strongest ontology-first managed fit in the accessible evidence because it combines explicit ontology and rule reasoning, open standards, a documented managed cloud offering, and a free entry path for pilot work. [source: https://www.stardog.com/stardog-cloud/; https://docs.stardog.com/query-stardog; https://docs.stardog.com/inference-engine]
- [fact] Ontotext GraphDB documents support for OWL-Horst, OWL-Max, OWL2 QL, and OWL2 RL profiles, plus forward-chaining materialization, where inferences are generated during loading so later queries run against explicit and inferred statements together. [source: https://graphdb.ontotext.com/documentation/11.0/owl-compliance.html; https://graphdb.ontotext.com/documentation/master/reasoning.html]
- [fact] GraphDB also documents SPARQL querying, RDF loading and updating workflows, and loading or querying data as first-class operational concerns, which confirms that it is an ontology-first triplestore rather than a property-graph overlay. [source: https://graphdb.ontotext.com/documentation/11.0/loading-querying-data.html; https://graphdb.ontotext.com/documentation/10.1/loading-and-updating-data.html]
- [inference] GraphDB is a strong ontology-first database alternative to Stardog, especially where materialized reasoning is preferred over query-time reasoning, but the consulted evidence established GraphDB's semantic behavior more clearly than its managed-service access model. [source: https://graphdb.ontotext.com/documentation/11.0/owl-compliance.html; https://graphdb.ontotext.com/documentation/master/reasoning.html; https://graphdb.ontotext.com/documentation/11.0/loading-querying-data.html]

#### 2.5 Adjacent managed knowledge-graph application layer

- [fact] metaphactory is marketed as an enterprise knowledge-graph platform built on RDF, OWL, Simple Knowledge Organization System (SKOS), a W3C data model for thesauri and taxonomies expressed as machine-readable RDF data, Shapes Constraint Language (SHACL), a W3C language for validating RDF graphs against declared constraints, SPARQL, and Representational State Transfer (REST) APIs, with human-in-the-loop modeling, semantic application building, and explainable Artificial Intelligence (AI) positioning. [source: https://www.metaphacts.com/product; https://www.w3.org/TR/skos-reference/; https://www.w3.org/TR/shacl/]
- [inference] metaphactory is better understood as an application and workbench layer over semantic graph infrastructure than as the core hosted graph database choice itself, so it is adjacent to this decision rather than a direct replacement for Stardog, GraphDB, Neptune, or Neo4j. [source: https://www.metaphacts.com/product]

#### 2.6 Cross-platform comparison and recommendation logic

- [inference] The candidate set splits into three practical groups: ontology-first semantic platforms, meaning Stardog and GraphDB; property-graph-first developer platforms, meaning Neo4j Aura and Memgraph Cloud; and a dual-model infrastructure service, meaning Amazon Neptune. [source: https://www.stardog.com/stardog-cloud/; https://graphdb.ontotext.com/documentation/11.0/owl-compliance.html; https://neo4j.com/cloud/platform/aura-graph-database/; https://memgraph.com/pricing; https://docs.aws.amazon.com/neptune/latest/userguide/intro.html]
- [inference] If the repository needs a formal ontology with standard semantic-web interoperability, ontology reasoning, and SPARQL-first querying, Stardog and GraphDB are materially better aligned than Neo4j Aura or Memgraph Cloud, because only Stardog and GraphDB explicitly document OWL reasoning behavior in the consulted evidence. [source: https://docs.stardog.com/inference-engine; https://graphdb.ontotext.com/documentation/11.0/owl-compliance.html; https://neo4j.com/cloud/platform/aura-graph-database/; https://memgraph.com/docs/querying/differences-in-cypher-implementations]
- [inference] If the repository later decides that ontology reasoning is unnecessary and that linked traversal and Python application ergonomics matter more, Neo4j Aura becomes the strongest alternative because its driver, import, and managed-service experience are better documented and less enterprise-procurement-heavy than the ontology-first platforms. [source: https://neo4j.com/docs/python-manual/current/; https://neo4j.com/docs/aura/classic/auradb/importing-data/; https://neo4j.com/cloud/platform/aura-graph-database/]

### §3 Reasoning

- [inference] I weighted explicit reasoning documentation more heavily than broad marketing language, because the core decision criterion is ontology support rather than generic graph capability. [source: https://docs.stardog.com/inference-engine; https://graphdb.ontotext.com/documentation/master/reasoning.html; https://docs.aws.amazon.com/neptune/latest/userguide/intro.html]
- [inference] I treated public pricing transparency and self-serve trial access as meaningful evaluation criteria because the item explicitly prefers developer trials or free tiers for initial evaluation. [source: https://www.stardog.com/stardog-cloud/; https://aws.amazon.com/neptune/pricing/; https://memgraph.com/pricing; https://www.tigergraph.com/pricing/]
- [inference] I did not promote TigerGraph into the final shortlist even though it is a hosted graph platform because the official materials consulted emphasize analytics and large analytical workspaces more than ontology engineering, and the item scope explicitly excludes analytics-first platforms from the final recommendation. [source: https://www.tigergraph.com/pricing/; https://www.tigergraph.com/gsql/]
- [inference] I treated Neptune's ontology fit as medium rather than high because dual-model support is clearly documented, but explicit OWL reasoning behavior was not established in the consulted Neptune materials. [source: https://docs.aws.amazon.com/neptune/latest/userguide/intro.html; https://docs.aws.amazon.com/neptune/latest/userguide/bulk-load.html]

### §4 Consistency Check

- [fact] No direct contradiction appeared between the ontology-first sources: Stardog documents query-time reasoning, while GraphDB documents materialized forward-chaining reasoning, and those are different implementation choices rather than conflicting claims about semantic capability. [source: https://docs.stardog.com/inference-engine; https://graphdb.ontotext.com/documentation/master/reasoning.html]
- [inference] The largest remaining uncertainty is not semantic capability but commercial accessibility, because Stardog's managed-cloud entry tier is transparent while the consulted GraphDB sources establish ontology capabilities more clearly than a comparable self-serve access path. [source: https://www.stardog.com/stardog-cloud/; https://graphdb.ontotext.com/documentation/11.0/loading-querying-data.html; https://graphdb.ontotext.com/documentation/11.0/owl-compliance.html]
- [fact] The recommendation stays internally consistent with prior repository work because the earlier schema item advocated a small curated graph, which is better matched to a semantic managed service with clear reasoning behavior than to a high-scale analytics-first platform. [source: https://davidamitchell.github.io/Research/research/2026-05-02-knowledge-graph-schema-cross-session-research-mcp.html]

### §5 Depth and Breadth Expansion

- [inference] Technical lens: query-time reasoning in Stardog is operationally attractive when ontologies change frequently, because it avoids full re-materialization cycles, while GraphDB's forward-chaining materialization is attractive when predictable query performance over stable ontologies matters more. [source: https://docs.stardog.com/inference-engine; https://graphdb.ontotext.com/documentation/master/reasoning.html]
- [inference] Economic lens: Neo4j Aura and Stardog have the cleanest publicly documented low-friction entry paths for pilot work in the consulted evidence, whereas Neptune introduces AWS infrastructure primitives and GraphDB appears to require more enterprise-style commercial engagement. [source: https://www.stardog.com/stardog-cloud/; https://aws.amazon.com/neptune/pricing/; https://neo4j.com/cloud/platform/aura-graph-database/]
- [inference] Behavioral and workflow lens: standards-heavy semantic platforms reduce later lock-in for ontology work, but they also demand more semantic-web discipline from developers than Cypher-first platforms, so the right choice depends on whether the project wants formal semantics or simply graph-shaped application data. [source: https://www.stardog.com/platform/; https://graphdb.ontotext.com/documentation/11.0/owl-compliance.html; https://neo4j.com/cloud/platform/aura-graph-database/]

### §6 Synthesis

**Executive summary:**

- [inference] Stardog Cloud is the only evaluated option whose consulted evidence directly established both managed delivery and ontology-first reasoning, which makes it the clearest hosted starting point for this repository. Ontotext GraphDB remains a strong ontology-first database alternative, but the consulted evidence established its semantic capabilities more clearly than its hosted-service model. [source: https://www.stardog.com/stardog-cloud/; https://docs.stardog.com/query-stardog; https://docs.stardog.com/inference-engine; https://graphdb.ontotext.com/documentation/11.0/owl-compliance.html; https://graphdb.ontotext.com/documentation/master/reasoning.html]
- [inference] Amazon Neptune is the best hybrid choice when the project needs both property graph and RDF support inside Amazon Web Services (AWS), but it is a weaker ontology-first recommendation because the consulted material established dual-model support more clearly than formal OWL reasoning. [source: https://docs.aws.amazon.com/neptune/latest/userguide/intro.html; https://docs.aws.amazon.com/neptune/latest/userguide/bulk-load.html; https://aws.amazon.com/neptune/pricing/]
- [inference] Neo4j AuraDB is the strongest fallback if the project ultimately wants a developer-friendly managed property graph rather than a formal ontology platform, while Memgraph Cloud fits similar Cypher-style prototyping but with less evidence of ontology-oriented features. [source: https://neo4j.com/cloud/platform/aura-graph-database/; https://neo4j.com/docs/python-manual/current/; https://memgraph.com/pricing; https://memgraph.com/docs/data-migration]
- [inference] metaphactory is adjacent rather than primary for this decision because it is best treated as a semantic application layer on top of a graph store, not as the first database choice itself. [source: https://www.metaphacts.com/product]

**Key findings:**

1. **[inference] Stardog Cloud is the strongest hosted ontology-first starting point in the evaluated set because it combines managed cloud delivery, a documented free tier up to 1 million edges, SPARQL-first querying, and explicit OWL and rule reasoning in one product surface.** (medium confidence; source: https://www.stardog.com/stardog-cloud/; https://docs.stardog.com/query-stardog; https://docs.stardog.com/inference-engine)
2. **[inference] Ontotext GraphDB is a credible ontology-first database alternative because its official documentation explicitly supports multiple OWL profiles, forward-chaining materialized inference, SPARQL querying, and RDF loading workflows that fit formal knowledge-ontology work.** (medium confidence; source: https://graphdb.ontotext.com/documentation/11.0/owl-compliance.html; https://graphdb.ontotext.com/documentation/master/reasoning.html; https://graphdb.ontotext.com/documentation/10.1/loading-and-updating-data.html)
3. **[inference] Amazon Neptune is the best dual-model hosted option because it supports property-graph querying through Gremlin and openCypher and semantic querying through SPARQL, but its hosted experience is more infrastructure-shaped than software-as-a-service-shaped for a small pilot.** (medium confidence; source: https://docs.aws.amazon.com/neptune/latest/userguide/intro.html; https://docs.aws.amazon.com/neptune/latest/userguide/bulk-load.html; https://docs.aws.amazon.com/neptune/latest/userguide/iam-auth.html; https://aws.amazon.com/neptune/pricing/)
4. **[inference] Neo4j AuraDB is the strongest developer-experience alternative when formal ontology reasoning is not required, because its managed property-graph service, Python driver, and import tooling are all explicitly documented in the consulted official material.** (medium confidence; source: https://neo4j.com/cloud/platform/aura-graph-database/; https://neo4j.com/docs/python-manual/current/; https://neo4j.com/docs/aura/classic/auradb/importing-data/; https://neo4j.com/docs/cypher-manual/current/clauses/load-csv/)
5. **[inference] Memgraph Cloud is suitable for Cypher-compatible graph application prototypes and migration-heavy pilots, but the consulted official material supports a property-graph and migration story rather than a formal ontology and semantic-reasoning story.** (medium confidence; source: https://memgraph.com/pricing; https://memgraph.com/docs/data-migration; https://memgraph.com/docs/client-libraries; https://memgraph.com/docs/querying/differences-in-cypher-implementations)
6. **[inference] TigerGraph Savanna should not be the first recommendation for this repository's ontology use case because its current official positioning focuses on enterprise graph analytics, analytical workspaces, and proprietary-query-language-centered scale rather than ontology engineering and semantic-web standards.** (medium confidence; source: https://www.tigergraph.com/pricing/; https://www.tigergraph.com/gsql/; https://docs.tigergraph.com/savanna/main/overview/)
7. **[inference] metaphactory belongs later in the architecture, if at all, because its official product description reads as a semantic application and workbench layer over RDF, OWL, Simple Knowledge Organization System (SKOS), Shapes Constraint Language (SHACL), and SPARQL rather than as the primary managed graph database substrate.** (medium confidence; source: https://www.metaphacts.com/product; https://www.w3.org/TR/skos-reference/; https://www.w3.org/TR/shacl/)
8. **[inference] For this repository's current use case, the decision boundary is semantic rigor versus developer convenience: choose Stardog Cloud if ontology reasoning and semantic-web interoperability are central, and choose Neo4j AuraDB only if the project reduces the goal to linked property-graph navigation without formal ontology semantics.** (medium confidence; source: https://www.stardog.com/stardog-cloud/; https://docs.stardog.com/inference-engine; https://neo4j.com/cloud/platform/aura-graph-database/; https://davidamitchell.github.io/Research/research/2026-05-02-knowledge-graph-schema-cross-session-research-mcp.html)

**Evidence map:**

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [inference] Stardog Cloud is the strongest hosted ontology-first starting point because it combines managed cloud delivery, a documented free tier, SPARQL, and explicit reasoning. | https://www.stardog.com/stardog-cloud/; https://docs.stardog.com/query-stardog; https://docs.stardog.com/inference-engine | medium | Query-time reasoning and free-tier transparency both matter for pilot fit. |
| [inference] Ontotext GraphDB is a credible ontology-first database alternative because it documents OWL profiles, materialized inference, SPARQL, and RDF loading. | https://graphdb.ontotext.com/documentation/11.0/owl-compliance.html; https://graphdb.ontotext.com/documentation/master/reasoning.html; https://graphdb.ontotext.com/documentation/10.1/loading-and-updating-data.html | medium | Strong semantic capability; hosted-service accessibility remains an evidence gap. |
| [inference] Amazon Neptune is the best dual-model hosted option, but its setup is more infrastructure-shaped than simple self-serve SaaS for a small pilot. | https://docs.aws.amazon.com/neptune/latest/userguide/intro.html; https://docs.aws.amazon.com/neptune/latest/userguide/bulk-load.html; https://docs.aws.amazon.com/neptune/latest/userguide/iam-auth.html; https://aws.amazon.com/neptune/pricing/ | medium | Dual-model support is clear; ontology reasoning strength is less explicit. |
| [inference] Neo4j AuraDB is the strongest developer-experience alternative when formal ontology reasoning is not required because its managed service, Python driver, and import tooling are explicitly documented in the consulted material. | https://neo4j.com/cloud/platform/aura-graph-database/; https://neo4j.com/docs/python-manual/current/; https://neo4j.com/docs/aura/classic/auradb/importing-data/; https://neo4j.com/docs/cypher-manual/current/clauses/load-csv/ | medium | This row stays within Neo4j-specific evidence scope. |
| [inference] Memgraph Cloud suits Cypher-compatible prototypes and migrations more than ontology-centric semantic work. | https://memgraph.com/pricing; https://memgraph.com/docs/data-migration; https://memgraph.com/docs/client-libraries; https://memgraph.com/docs/querying/differences-in-cypher-implementations | medium | Strong ingestion story, weak formal ontology story in the consulted material. |
| [inference] TigerGraph Savanna is not the right first recommendation for this repository because official positioning centers analytics-first scale rather than ontology engineering. | https://www.tigergraph.com/pricing/; https://www.tigergraph.com/gsql/; https://docs.tigergraph.com/savanna/main/overview/ | medium | Scope exclusion and product positioning point in the same direction. |
| [inference] metaphactory is an application layer rather than the core database substrate for this decision. | https://www.metaphacts.com/product; https://www.w3.org/TR/skos-reference/; https://www.w3.org/TR/shacl/ | medium | W3C sources define the standards terms used in the claim. |
| [inference] The core decision boundary for this repository is semantic rigor versus developer convenience. | https://www.stardog.com/stardog-cloud/; https://docs.stardog.com/inference-engine; https://neo4j.com/cloud/platform/aura-graph-database/; https://davidamitchell.github.io/Research/research/2026-05-02-knowledge-graph-schema-cross-session-research-mcp.html | medium | This is a synthesis claim connecting product evidence to repo needs. |

**Assumptions:**

- [assumption] The first hosted graph deployment for this repository will stay small enough that trial access and manageable integration overhead matter more than extreme horizontal scale. Justification: the current repository and prior schema work describe a curated research graph rather than an enterprise transaction graph. [source: https://github.com/davidamitchell/Research/blob/main/README.md; https://davidamitchell.github.io/Research/research/2026-05-02-knowledge-graph-schema-cross-session-research-mcp.html]
- [assumption] Python integration is a practical requirement for any recommended platform because the repository's tooling stack is Python-first and the decision is meant to inform future repository tooling. Justification: current repo tooling is implemented in Python, so standards-only endpoints without a practical Python path would raise adoption friction. [source: https://github.com/davidamitchell/Research/blob/main/README.md]

**Analysis:**

- [inference] The evidence divides the market cleanly: ontology-first platforms document semantic standards and reasoning; property-graph-first platforms document Cypher, traversal, and application ergonomics; Neptune documents both data models but asks the user to operate within AWS infrastructure patterns. [source: https://docs.stardog.com/inference-engine; https://graphdb.ontotext.com/documentation/11.0/owl-compliance.html; https://neo4j.com/cloud/platform/aura-graph-database/; https://memgraph.com/docs/data-migration; https://docs.aws.amazon.com/neptune/latest/userguide/intro.html]
- [inference] For a knowledge ontology, reasoning behavior is the decisive differentiator because the repository would otherwise gain little from paying the semantic-web complexity cost. Stardog and GraphDB clear that bar explicitly, Neptune only partially clears it in the consulted material, and Neo4j Aura plus Memgraph Cloud do not clear it at all. [source: https://docs.stardog.com/inference-engine; https://graphdb.ontotext.com/documentation/master/reasoning.html; https://docs.aws.amazon.com/neptune/latest/userguide/intro.html; https://neo4j.com/cloud/platform/aura-graph-database/; https://memgraph.com/docs/querying/differences-in-cypher-implementations]
- [inference] Stardog edges out GraphDB for this repository not because GraphDB is less capable, but because Stardog's managed-cloud entry path, free plan, and reasoning story are clearer in the public material, which lowers evaluation friction for a small pilot. [source: https://www.stardog.com/stardog-cloud/; https://docs.stardog.com/inference-engine; https://graphdb.ontotext.com/documentation/11.0/owl-compliance.html]
- [inference] Neo4j Aura remains strategically relevant because the repository may later decide that a lightweight linked research graph is sufficient without full ontology semantics, in which case its Python driver and import ergonomics would likely produce faster implementation time than the semantic platforms. [source: https://neo4j.com/docs/python-manual/current/; https://neo4j.com/docs/aura/classic/auradb/importing-data/; https://davidamitchell.github.io/Research/research/2026-05-02-knowledge-graph-schema-cross-session-research-mcp.html]

**Risks, gaps, uncertainties:**

- [inference] The consulted evidence did not establish a public hosted-pricing or self-serve managed-entry path for GraphDB with the same clarity available for Stardog, Neo4j Aura, Memgraph Cloud, or TigerGraph Savanna, which lowers confidence in cost and access ranking for GraphDB specifically. [source: https://www.stardog.com/stardog-cloud/; https://neo4j.com/cloud/platform/aura-graph-database/; https://memgraph.com/pricing; https://www.tigergraph.com/pricing/; https://graphdb.ontotext.com/documentation/11.0/loading-querying-data.html]
- [inference] Neptune's exact ontology-reasoning story remains less certain than its query-language story because the consulted official material established RDF and SPARQL support clearly but did not establish native OWL reasoning with the same precision. [source: https://docs.aws.amazon.com/neptune/latest/userguide/intro.html; https://docs.aws.amazon.com/neptune/latest/userguide/bulk-load.html]
- [inference] Language-specific integration detail is deeper in the Neo4j and Memgraph evidence than in the Stardog and GraphDB evidence, which means the Python-developer-experience comparison is directionally sound but not perfectly symmetrical. [source: https://neo4j.com/docs/python-manual/current/; https://memgraph.com/docs/client-libraries; https://docs.stardog.com/query-stardog; https://graphdb.ontotext.com/documentation/11.0/loading-querying-data.html]

**Open questions:**

- [inference] Should the repository prefer query-time reasoning, as in Stardog, or materialized reasoning, as in GraphDB, for its expected ontology-edit frequency and read pattern? [source: https://docs.stardog.com/inference-engine; https://graphdb.ontotext.com/documentation/master/reasoning.html]
- [inference] Is the eventual target a formal semantic knowledge graph, or a lighter-weight property graph with provenance and link traversal only? [source: https://davidamitchell.github.io/Research/research/2026-05-02-knowledge-graph-schema-cross-session-research-mcp.html; https://neo4j.com/cloud/platform/aura-graph-database/]
- [inference] Would a semantic application layer such as metaphactory add enough value to justify a two-layer architecture, or should the project start with a database-only evaluation? [source: https://www.metaphacts.com/product]

### §7 Recursive Review

- Review result: pass
- Acronym audit: SaaS, RDF, OWL, API, SDK, SPARQL, AI, AWS, IAM, VPC, SKOS, SHACL, GQL, and MCP expanded on first use
- Claim audit: factual and inferential claims labeled throughout Research Skill Output
- Cross-item integration: prior completed items cited in section 0, section 2, synthesis, and analysis
- Remaining uncertainty: GraphDB commercial entry friction and Neptune ontology depth remain medium-confidence rather than high-confidence threads

---

## Findings

### Executive Summary

Stardog Cloud is the only evaluated option whose consulted evidence directly established both managed delivery and ontology-first reasoning, which makes it the clearest hosted starting point for this repository. Ontotext GraphDB remains a strong ontology-first database alternative, but the consulted evidence established its semantic capabilities more clearly than its hosted-service model. [inference; source: https://www.stardog.com/stardog-cloud/; https://docs.stardog.com/query-stardog; https://docs.stardog.com/inference-engine; https://graphdb.ontotext.com/documentation/11.0/owl-compliance.html; https://graphdb.ontotext.com/documentation/master/reasoning.html]

Amazon Neptune is the best hybrid choice when the project needs both property-graph and RDF support inside Amazon Web Services (AWS), but it is a weaker ontology-first recommendation because the consulted material established dual-model support more clearly than formal OWL reasoning. [inference; source: https://docs.aws.amazon.com/neptune/latest/userguide/intro.html; https://docs.aws.amazon.com/neptune/latest/userguide/bulk-load.html; https://aws.amazon.com/neptune/pricing/]

Neo4j AuraDB is the strongest fallback if the repository ultimately wants a developer-friendly managed property graph rather than a formal ontology platform, while Memgraph Cloud fits a similar Cypher-style prototype niche with less evidence of ontology-oriented features. [inference; source: https://neo4j.com/cloud/platform/aura-graph-database/; https://neo4j.com/docs/python-manual/current/; https://memgraph.com/pricing; https://memgraph.com/docs/data-migration]

The practical recommendation is therefore conditional but clear: start with Stardog Cloud if formal ontology semantics matter, and pivot to Neo4j AuraDB only if the problem definition collapses to linked property-graph navigation without semantic-web interoperability. [inference; source: https://www.stardog.com/stardog-cloud/; https://docs.stardog.com/inference-engine; https://neo4j.com/cloud/platform/aura-graph-database/; https://davidamitchell.github.io/Research/research/2026-05-02-knowledge-graph-schema-cross-session-research-mcp.html]

### Key Findings

1. **Stardog Cloud is the strongest hosted ontology-first starting point in the evaluated set because it combines managed cloud delivery, a documented free tier up to 1 million edges, SPARQL-first querying, and explicit OWL and rule reasoning in one product surface.** ([inference]; medium confidence; source: https://www.stardog.com/stardog-cloud/; https://docs.stardog.com/query-stardog; https://docs.stardog.com/inference-engine)
2. **Ontotext GraphDB is a credible ontology-first database alternative because its official documentation explicitly supports multiple OWL profiles, forward-chaining materialized inference, SPARQL querying, and RDF loading workflows that fit formal knowledge-ontology work.** ([inference]; medium confidence; source: https://graphdb.ontotext.com/documentation/11.0/owl-compliance.html; https://graphdb.ontotext.com/documentation/master/reasoning.html; https://graphdb.ontotext.com/documentation/10.1/loading-and-updating-data.html)
3. **Amazon Neptune is the best dual-model hosted option because it supports property-graph querying through Gremlin and openCypher and semantic querying through SPARQL, but its hosted experience is more infrastructure-shaped than software-as-a-service-shaped for a small pilot.** ([inference]; medium confidence; source: https://docs.aws.amazon.com/neptune/latest/userguide/intro.html; https://docs.aws.amazon.com/neptune/latest/userguide/bulk-load.html; https://docs.aws.amazon.com/neptune/latest/userguide/iam-auth.html; https://aws.amazon.com/neptune/pricing/)
4. **Neo4j AuraDB is the strongest developer-experience alternative when formal ontology reasoning is not required, because its managed property-graph service, Python driver, and import tooling are all explicitly documented in the consulted official material.** ([inference]; medium confidence; source: https://neo4j.com/cloud/platform/aura-graph-database/; https://neo4j.com/docs/python-manual/current/; https://neo4j.com/docs/aura/classic/auradb/importing-data/; https://neo4j.com/docs/cypher-manual/current/clauses/load-csv/)
5. **Memgraph Cloud is suitable for Cypher-compatible graph application prototypes and migration-heavy pilots, but the consulted official material supports a property-graph and migration story rather than a formal ontology and semantic-reasoning story.** ([inference]; medium confidence; source: https://memgraph.com/pricing; https://memgraph.com/docs/data-migration; https://memgraph.com/docs/client-libraries; https://memgraph.com/docs/querying/differences-in-cypher-implementations)
6. **TigerGraph Savanna should not be the first recommendation for this repository's ontology use case because its current official positioning focuses on enterprise graph analytics, analytical workspaces, and proprietary-query-language-centered scale rather than ontology engineering and semantic-web standards.** ([inference]; medium confidence; source: https://www.tigergraph.com/pricing/; https://www.tigergraph.com/gsql/; https://docs.tigergraph.com/savanna/main/overview/)
7. **metaphactory belongs later in the architecture, if at all, because its official product description reads as a semantic application and workbench layer over RDF, OWL, Simple Knowledge Organization System (SKOS), Shapes Constraint Language (SHACL), and SPARQL rather than as the primary managed graph database substrate.** ([inference]; medium confidence; source: https://www.metaphacts.com/product; https://www.w3.org/TR/skos-reference/; https://www.w3.org/TR/shacl/)
8. **For this repository's current use case, the decision boundary is semantic rigor versus developer convenience: choose Stardog Cloud if ontology reasoning and semantic-web interoperability are central, and choose Neo4j AuraDB only if the project reduces the goal to linked property-graph navigation without formal ontology semantics.** ([inference]; medium confidence; source: https://www.stardog.com/stardog-cloud/; https://docs.stardog.com/inference-engine; https://neo4j.com/cloud/platform/aura-graph-database/; https://davidamitchell.github.io/Research/research/2026-05-02-knowledge-graph-schema-cross-session-research-mcp.html)

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [inference] Stardog Cloud is the strongest hosted ontology-first starting point because it combines managed cloud delivery, a documented free tier, SPARQL, and explicit reasoning. | https://www.stardog.com/stardog-cloud/; https://docs.stardog.com/query-stardog; https://docs.stardog.com/inference-engine | medium | Query-time reasoning and free-tier transparency both matter for pilot fit. |
| [inference] Ontotext GraphDB is a credible ontology-first database alternative because it documents OWL profiles, materialized inference, SPARQL, and RDF loading. | https://graphdb.ontotext.com/documentation/11.0/owl-compliance.html; https://graphdb.ontotext.com/documentation/master/reasoning.html; https://graphdb.ontotext.com/documentation/10.1/loading-and-updating-data.html | medium | Strong semantic capability; hosted-service accessibility remains an evidence gap. |
| [inference] Amazon Neptune is the best dual-model hosted option, but its setup is more infrastructure-shaped than simple self-serve SaaS for a small pilot. | https://docs.aws.amazon.com/neptune/latest/userguide/intro.html; https://docs.aws.amazon.com/neptune/latest/userguide/bulk-load.html; https://docs.aws.amazon.com/neptune/latest/userguide/iam-auth.html; https://aws.amazon.com/neptune/pricing/ | medium | Dual-model support is clear; ontology reasoning strength is less explicit. |
| [inference] Neo4j AuraDB is the strongest developer-experience alternative when formal ontology reasoning is not required because its managed service, Python driver, and import tooling are explicitly documented in the consulted material. | https://neo4j.com/cloud/platform/aura-graph-database/; https://neo4j.com/docs/python-manual/current/; https://neo4j.com/docs/aura/classic/auradb/importing-data/; https://neo4j.com/docs/cypher-manual/current/clauses/load-csv/ | medium | This row stays within Neo4j-specific evidence scope. |
| [inference] Memgraph Cloud suits Cypher-compatible prototypes and migrations more than ontology-centric semantic work. | https://memgraph.com/pricing; https://memgraph.com/docs/data-migration; https://memgraph.com/docs/client-libraries; https://memgraph.com/docs/querying/differences-in-cypher-implementations | medium | Strong ingestion story, weak formal ontology story in the consulted material. |
| [inference] TigerGraph Savanna is not the right first recommendation for this repository because official positioning centers analytics-first scale rather than ontology engineering. | https://www.tigergraph.com/pricing/; https://www.tigergraph.com/gsql/; https://docs.tigergraph.com/savanna/main/overview/ | medium | Scope exclusion and product positioning point in the same direction. |
| [inference] metaphactory is an application layer rather than the core database substrate for this decision. | https://www.metaphacts.com/product; https://www.w3.org/TR/skos-reference/; https://www.w3.org/TR/shacl/ | medium | W3C sources define the standards terms used in the claim. |
| [inference] The core decision boundary for this repository is semantic rigor versus developer convenience. | https://www.stardog.com/stardog-cloud/; https://docs.stardog.com/inference-engine; https://neo4j.com/cloud/platform/aura-graph-database/; https://davidamitchell.github.io/Research/research/2026-05-02-knowledge-graph-schema-cross-session-research-mcp.html | medium | This is a synthesis claim connecting product evidence to repo needs. |

### Assumptions

- **Assumption:** The first hosted graph deployment for this repository will stay small enough that trial access and manageable integration overhead matter more than extreme horizontal scale. **Justification:** The current repository and prior schema work describe a curated research graph rather than an enterprise transaction graph. [assumption; source: https://github.com/davidamitchell/Research/blob/main/README.md; https://davidamitchell.github.io/Research/research/2026-05-02-knowledge-graph-schema-cross-session-research-mcp.html]
- **Assumption:** Python integration is a practical requirement for any recommended platform because the repository's tooling stack is Python-first and the decision is meant to inform future repository tooling. **Justification:** Current repo tooling is implemented in Python, so standards-only endpoints without a practical Python path would raise adoption friction. [assumption; source: https://github.com/davidamitchell/Research/blob/main/README.md]

### Analysis

The evidence divides the market cleanly: ontology-first platforms document semantic standards and reasoning; property-graph-first platforms document Cypher, traversal, and application ergonomics; Neptune documents both data models but asks the user to operate within Amazon Web Services (AWS) infrastructure patterns. [inference; source: https://docs.stardog.com/inference-engine; https://graphdb.ontotext.com/documentation/11.0/owl-compliance.html; https://neo4j.com/cloud/platform/aura-graph-database/; https://memgraph.com/docs/data-migration; https://docs.aws.amazon.com/neptune/latest/userguide/intro.html]

For a knowledge ontology, reasoning behavior is the decisive differentiator because the repository would otherwise gain little from paying the semantic-web complexity cost. Stardog and GraphDB clear that bar explicitly, Neptune only partially clears it in the consulted material, and Neo4j Aura plus Memgraph Cloud do not clear it at all. [inference; source: https://docs.stardog.com/inference-engine; https://graphdb.ontotext.com/documentation/master/reasoning.html; https://docs.aws.amazon.com/neptune/latest/userguide/intro.html; https://neo4j.com/cloud/platform/aura-graph-database/; https://memgraph.com/docs/querying/differences-in-cypher-implementations]

Stardog edges out GraphDB for this repository not because GraphDB is less capable, but because Stardog's managed-cloud entry path, free plan, and reasoning story are clearer in the public material, which lowers evaluation friction for a small pilot. [inference; source: https://www.stardog.com/stardog-cloud/; https://docs.stardog.com/inference-engine; https://graphdb.ontotext.com/documentation/11.0/owl-compliance.html]

Neo4j Aura remains strategically relevant because the repository may later decide that a lightweight linked research graph is sufficient without full ontology semantics, in which case its Python driver and import ergonomics would likely produce faster implementation time than the semantic platforms. [inference; source: https://neo4j.com/docs/python-manual/current/; https://neo4j.com/docs/aura/classic/auradb/importing-data/; https://davidamitchell.github.io/Research/research/2026-05-02-knowledge-graph-schema-cross-session-research-mcp.html]

### Risks, Gaps, and Uncertainties

- The consulted evidence did not establish a public hosted-pricing or self-serve managed-entry path for GraphDB with the same clarity available for Stardog, Neo4j Aura, Memgraph Cloud, or TigerGraph Savanna, which lowers confidence in cost and access ranking for GraphDB specifically. [inference; source: https://www.stardog.com/stardog-cloud/; https://neo4j.com/cloud/platform/aura-graph-database/; https://memgraph.com/pricing; https://www.tigergraph.com/pricing/; https://graphdb.ontotext.com/documentation/11.0/loading-querying-data.html]
- Neptune's exact ontology-reasoning story remains less certain than its query-language story because the consulted official material established RDF and SPARQL support clearly but did not establish native OWL reasoning with the same precision. [inference; source: https://docs.aws.amazon.com/neptune/latest/userguide/intro.html; https://docs.aws.amazon.com/neptune/latest/userguide/bulk-load.html]
- Language-specific integration detail is deeper in the Neo4j and Memgraph evidence than in the Stardog and GraphDB evidence, which means the Python-developer-experience comparison is directionally sound but not perfectly symmetrical. [inference; source: https://neo4j.com/docs/python-manual/current/; https://memgraph.com/docs/client-libraries; https://docs.stardog.com/query-stardog; https://graphdb.ontotext.com/documentation/11.0/loading-querying-data.html]

### Open Questions

- Should the repository prefer query-time reasoning, as in Stardog, or materialized reasoning, as in GraphDB, for its expected ontology-edit frequency and read pattern? [inference; source: https://docs.stardog.com/inference-engine; https://graphdb.ontotext.com/documentation/master/reasoning.html]
- Is the eventual target a formal semantic knowledge graph, or a lighter-weight property graph with provenance and link traversal only? [inference; source: https://davidamitchell.github.io/Research/research/2026-05-02-knowledge-graph-schema-cross-session-research-mcp.html; https://neo4j.com/cloud/platform/aura-graph-database/]
- Would a semantic application layer such as metaphactory add enough value to justify a two-layer architecture, or should the project start with a database-only evaluation? [inference; source: https://www.metaphacts.com/product]

---

## Output

- Type: knowledge
- Description: A hosted graph-platform comparison and recommendation for ontology-oriented research tooling, with Stardog Cloud recommended first for formal semantic work and Neo4j AuraDB recommended only for a reduced property-graph use case. [inference; source: https://www.stardog.com/stardog-cloud/; https://docs.stardog.com/inference-engine; https://neo4j.com/cloud/platform/aura-graph-database/]
- Links:
  - https://www.stardog.com/stardog-cloud/
  - https://graphdb.ontotext.com/documentation/11.0/owl-compliance.html
  - https://docs.aws.amazon.com/neptune/latest/userguide/intro.html
