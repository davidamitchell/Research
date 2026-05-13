---
review_count: 2
title: "Knowledge Graph as a data product: data mesh principles, contracts, and ownership for software-agent runtime dependencies"
added: 2026-05-12T08:21:48+00:00
status: reviewing
priority: medium
blocks: []
tags: [knowledge-graph, agentic-ai, governance, organisation]
started: 2026-05-13T09:37:27+00:00
completed: ~
output: [knowledge]
cites:
  - 2026-05-12-data-product-ontology
  - 2026-05-12-knowledge-graph-agentic-runtime-dependency
  - 2026-05-12-knowledge-graph-lifecycle-management-agentic
  - 2026-05-12-web-ontologies-production-knowledge-graph-agentic
related:
  - 2026-05-09-data-governance-standards-ai-agentic-applicability
  - 2026-05-02-knowledge-graph-schema-cross-session-research-mcp
  - 2026-04-22-knowledge-curation-governance-for-regulated-ai
superseded_by: ~
supersedes: ~
item_type: primary
confidence: medium
versions: []
---

# Knowledge Graph as a data product: data mesh principles, contracts, and ownership for software-agent runtime dependencies

## Research Question

What does it mean to treat a Knowledge Graph as a data product in a data mesh architecture, and how should data product principles, including domain ownership, data contracts, discoverability, interoperability, and federated governance, be applied when the graph is a shared runtime dependency for software agents?

## Scope

**In scope:**
- Data mesh principles as applied to Knowledge Graphs, including domain ownership, self-serve platform support, data as a product, and federated computational governance
- Data product specifications for Knowledge Graphs, including what constitutes a graph product interface, schema contract, and service commitment
- Data contract tooling and standards, including Data Catalog Vocabulary (DCAT), Data Product Descriptor Specification (DPDS), Data Product Ontology (DPROD), dbt contracts, and Shapes Constraint Language (SHACL), and their applicability to graph data
- Discoverability and cataloguing of Knowledge Graph data products, including how software agents and humans discover available graph products and understand their scope
- Interoperability between graph data products owned by different domains, including federated queries, Linked Data Platform (LDP), Solid, and alignment vocabularies
- Impact of data product boundaries on software-agent query patterns, including when an agent should query across federated graph products directly versus through curated outputs

**Out of scope:**
- Access control and rights management in detail
- Standalone ontology language selection beyond what is needed to define a graph product contract
- Database platform procurement
- General data mesh implementation not specific to Knowledge Graphs

**Constraints:**
- Prefer primary standards, first-party product documentation, and publicly accessible technical architecture sources
- Treat Zhamak Dehghani's data mesh principles as the canonical starting point for the organizational model
- Record gaps explicitly where public case studies do not document Knowledge Graph specific operating detail

## Context

- [inference; source: https://martinfowler.com/articles/data-mesh-principles.html; https://martinfowler.com/articles/data-monolith-to-mesh.html] Data mesh treats analytical data as domain-owned products rather than as assets absorbed into one central platform, so a shared Knowledge Graph used at runtime cannot be governed safely as an informal shared utility once multiple domains depend on it.
- [inference; source: https://davidamitchell.github.io/Research/research/2026-05-12-knowledge-graph-agentic-runtime-dependency.html; https://davidamitchell.github.io/Research/research/2026-05-12-knowledge-graph-lifecycle-management-agentic.html] When a Knowledge Graph sits in the live execution path of software agents, ownership ambiguity, silent schema drift, and stale derivatives become runtime risks rather than catalog hygiene problems, which raises the bar from passive metadata management to product-level contracts and operational commitments.

## Approach

1. Review Dehghani's four data mesh principles and map each one to the specific operating problems of a shared Knowledge Graph.
2. Compare standards and tools that could form a graph data product contract, especially DCAT, DPDS, DPROD, SHACL, and dbt contracts.
3. Review catalogue and governance tools, especially DataHub, OpenMetadata, Collibra, and Apache Atlas, to see how they model data products and whether they support graph-specific semantics natively.
4. Review graph interoperability mechanisms, especially SPARQL Protocol and RDF Query Language (SPARQL) federation, LDP, and Solid, to assess how cross-domain graph products can be queried safely.
5. Integrate adjacent completed repository research on runtime dependency, lifecycle management, ontology production, and data product ontology adoption.
6. Synthesize a recommended Knowledge Graph data product template covering ownership, contract format, versioning, discoverability, and service commitments.

## Sources

- [ ] [Dehghani (2022) Data Mesh: Delivering Data-Driven Value at Scale](https://www.oreilly.com/library/view/data-mesh/9781492092384/)
- [x] [Dehghani (2019) How to Move Beyond a Monolithic Data Lake to a Distributed Data Mesh](https://martinfowler.com/articles/data-monolith-to-mesh.html)
- [x] [Dehghani (2020) Data Mesh Principles and Logical Architecture](https://martinfowler.com/articles/data-mesh-principles.html)
- [x] [W3C (2024) Data Catalog Vocabulary (DCAT) Version 3](https://www.w3.org/TR/vocab-dcat-3/)
- [x] [Open Data Mesh Initiative (n.d.) Data Product Descriptor Specification 1.0.0](https://dpds.opendatamesh.org/specifications/dpds/1.0.0/)
- [x] [W3C (2017) Shapes Constraint Language (SHACL)](https://www.w3.org/TR/shacl/)
- [x] [Object Management Group (n.d.) DPROD specification index](https://www.omg.org/spec/DPROD/)
- [x] [Object Management Group (2024) DPROD ontology TTL](https://www.omg.org/spec/DPROD/dprod-ontology.ttl)
- [x] [Enterprise Knowledge Graph Forum (n.d.) DPROD specification site](https://ekgf.github.io/dprod/)
- [x] [dbt Labs (n.d.) Model contracts](https://docs.getdbt.com/reference/resource-configs/contract)
- [x] [DataHub (n.d.) Data products](https://docs.datahub.com/docs/dataproducts)
- [x] [DataHub (n.d.) Data product entity](https://docs.datahub.com/docs/generated/metamodel/entities/dataproduct)
- [x] [DataHub (n.d.) Metadata model](https://docs.datahub.com/docs/metadata-modeling/metadata-model)
- [x] [OpenMetadata (v1.12.x) Domains and Data Products overview](https://docs.open-metadata.org/v1.12.x/how-to-guides/data-governance/domains-&-data-products)
- [x] [OpenMetadata (v1.12.x) Adding Data Products](https://docs.open-metadata.org/v1.12.x/how-to-guides/data-governance/domains-&-data-products/data-products)
- [x] [Apache Atlas (2020) Type System](https://atlas.apache.org/2.0.0/TypeSystem.html)
- [x] [Collibra (2025) About data products](https://docs.collibra.com/Content/Assets/DataProducts/co_data-product.htm)
- [x] [Collibra (2025) Configuring and building data products](https://docs.collibra.com/Content/Assets/DataProducts/ta_conf-data-product.htm)
- [x] [W3C (2013) SPARQL 1.1 Query Language](https://www.w3.org/TR/sparql11-query/)
- [x] [W3C (2013) SPARQL 1.1 Federated Query](https://www.w3.org/TR/sparql11-federated-query/)
- [x] [W3C (2015) Linked Data Platform 1.0](https://www.w3.org/TR/ldp/)
- [x] [Solid Project (n.d.) Solid Protocol](https://solidproject.org/TR/protocol)
- [x] [Hogan et al. (2021) Knowledge Graphs](https://arxiv.org/abs/2003.02320)
- [x] [Bizer et al. (2009) Linked Data - the story so far](https://eprints.soton.ac.uk/271285/)
- [x] [Mitchell (2026) Data product ontology: definition, adoption, and current relevance](https://davidamitchell.github.io/Research/research/2026-05-12-data-product-ontology.html)
- [x] [Mitchell (2026) Knowledge Graph in the live execution path of multi-step Large Language Model systems: architecture and failure modes](https://davidamitchell.github.io/Research/research/2026-05-12-knowledge-graph-agentic-runtime-dependency.html)
- [x] [Mitchell (2026) Knowledge Graph lifecycle management for multi-step software agents: schema versioning, entity resolution, and knowledge freshness](https://davidamitchell.github.io/Research/research/2026-05-12-knowledge-graph-lifecycle-management-agentic.html)
- [x] [Mitchell (2026) Web ontologies in production Knowledge Graphs for multi-step Artificial Intelligence agents](https://davidamitchell.github.io/Research/research/2026-05-12-web-ontologies-production-knowledge-graph-agentic.html)
- [x] [Mitchell (2026) Data Governance Standards and Regulations Applied to Artificial Intelligence Systems and Multi-Step Autonomous AI Deployments](https://davidamitchell.github.io/Research/research/2026-05-09-data-governance-standards-ai-agentic-applicability.html)

---

## Research Skill Output

*(Full output from running the research skill - retained verbatim in the completed item. §§0-5 are the investigation; §6 seeds the Findings section below.)*

### §0 Initialise

- Question: determine how to run a graph of entities and relationships as a reusable product owned by one business area inside a decentralized data architecture, and define the ownership, contract, discoverability, interoperability, and runtime-governance implications when software agents depend on it.
- Scope: data mesh principles, graph-specific product contracts, catalogue behavior, graph interoperability, and adjacent repository findings are in scope; detailed access control design and vendor procurement are out of scope.
- Constraints: primary standards and first-party documentation first; direct public case studies on Knowledge Graph plus data mesh are likely sparse and must be treated as a gap rather than assumed.
- Output format: full section 0 to section 7 research record plus Findings with Executive Summary, Key Findings, Evidence Map, Assumptions, Analysis, Risks, Gaps, Uncertainties, Open Questions, Recommended Data Product Template, and Output.
- [fact] Hogan et al. describe knowledge graphs as graph-based structures used to exploit diverse, dynamic, and large-scale collections of data, which is the operational meaning used in this item. [source: https://arxiv.org/abs/2003.02320]
- [inference] Prior completed items most relevant here are the data product ontology item, the runtime dependency item, the lifecycle management item, and the production ontology item, because together they already cover data-product semantics, runtime failure surfaces, versioned graph publication, and ontology-stack choices. [source: https://davidamitchell.github.io/Research/research/2026-05-12-data-product-ontology.html; https://davidamitchell.github.io/Research/research/2026-05-12-knowledge-graph-agentic-runtime-dependency.html; https://davidamitchell.github.io/Research/research/2026-05-12-knowledge-graph-lifecycle-management-agentic.html; https://davidamitchell.github.io/Research/research/2026-05-12-web-ontologies-production-knowledge-graph-agentic.html]
- [fact] Dehghani defines four underpinning data mesh principles, domain-oriented decentralized ownership, data as a product, self-serve data platform, and federated computational governance, and frames them as collectively necessary for scale with usability and integrity. [source: https://martinfowler.com/articles/data-mesh-principles.html]

### §1 Question Decomposition

- A. Domain ownership and product boundary
  - A1. What is the product unit when the asset is a Knowledge Graph rather than a table or dashboard?
  - A2. Which graph concerns should remain domain-local, and which should be standardized globally?
- B. Product interface and contract
  - B1. Which standards describe discoverability, ports, schemas, and service interfaces for a graph product?
  - B2. Which graph-specific concerns are missing from ordinary table-schema contracts?
- C. Discoverability and catalogue layer
  - C1. How do mainstream catalogue tools model data products and ownership?
  - C2. Do those tools natively model graph-specific semantics, or only generic product metadata?
- D. Interoperability and federation
  - D1. Which standards enable cross-domain graph queries or linked-data exchange?
  - D2. Under what conditions can software agents query across graph products safely?
- E. Runtime and lifecycle implications
  - E1. How do versioning, provenance, and freshness expectations change when the graph is a runtime dependency?
  - E2. Which service commitments belong in a Knowledge Graph product contract?
- F. Synthesis
  - F1. What operating model best maps Dehghani's principles onto a shared Knowledge Graph?
  - F2. What minimal reusable template should a Knowledge Graph product expose?

### §2 Investigation

#### 2.1 Data mesh principles applied to a Knowledge Graph

- [fact] Dehghani states that data mesh ownership follows business domains, that analytical data must be treated as a product with discoverability and trust traits, that domains need self-serve platform abstractions, and that interoperability depends on federated computational governance with automated global rules. [source: https://martinfowler.com/articles/data-mesh-principles.html]
- [fact] Dehghani defines a data product as the architectural quantum that combines code, data and metadata, and infrastructure, rather than treating pipelines and storage as separately governed fragments. [source: https://martinfowler.com/articles/data-mesh-principles.html]
- [inference] For a Knowledge Graph, the product unit is therefore not "the enterprise graph" in the abstract, but a domain-owned graph resource plus its metadata, serving interfaces, and operating commitments, because data mesh product boundaries are defined by deployable ownership and consumer-facing interface rather than by one central semantic model. [source: https://martinfowler.com/articles/data-mesh-principles.html; https://martinfowler.com/articles/data-monolith-to-mesh.html]
- [inference] The graph-specific twist is that a domain-owned graph product can expose entities, named graphs, or query services while still participating in a wider semantic network, so the product boundary should be drawn around ownership and service commitments, not around an isolated refusal to link outward. [source: https://www.w3.org/TR/vocab-dcat-3/; https://www.w3.org/TR/sparql11-query/; https://eprints.soton.ac.uk/271285/]

#### 2.2 What a graph product contract needs beyond a table schema contract

- [fact] DCAT provides Resource Description Framework (RDF) classes and properties for catalog resources, datasets, distributions, data services, discoverability, versioning, and federated search across catalogs. [source: https://www.w3.org/TR/vocab-dcat-3/]
- [fact] DPDS defines a technology-independent data product descriptor with owners, input and output ports, promises, expectations, obligations, observability, and control surfaces for human and digital agents. [source: https://dpds.opendatamesh.org/specifications/dpds/1.0.0/]
- [fact] DPROD extends DCAT to describe data products and data services in a decentralized way, models a data product as a `dcat:Resource`, and adds explicit owner, purpose, domain, lifecycle status, input port, output port, input dataset, and output dataset properties. [source: https://www.omg.org/spec/DPROD/dprod-ontology.ttl; https://ekgf.github.io/dprod/]
- [fact] dbt contracts enforce returned column names, data types, and selected constraints for models, but the documented contract surface is tied to tabular models and does not describe named graphs, query endpoints, ontology versions, or graph traversal semantics. [source: https://docs.getdbt.com/reference/resource-configs/contract]
- [fact] The adjacent repository item on data product ontology concluded that DPROD is the only consulted public machine-readable ontology explicitly dedicated to data products, and that it is best understood as a semantic profile layered on DCAT rather than as a replacement for DCAT mechanics. [source: https://davidamitchell.github.io/Research/research/2026-05-12-data-product-ontology.html]
- [inference] A Knowledge Graph product contract therefore needs at least three layers: catalogue and port metadata through DCAT and DPROD, structural graph constraints through SHACL or an equivalent graph-shape layer, and operational promises and obligations through a descriptor like DPDS or a tool-specific equivalent. [source: https://www.w3.org/TR/vocab-dcat-3/; https://www.w3.org/TR/shacl/; https://www.omg.org/spec/DPROD/dprod-ontology.ttl; https://dpds.opendatamesh.org/specifications/dpds/1.0.0/; https://davidamitchell.github.io/Research/research/2026-05-12-data-product-ontology.html]
- [inference] Table-only contract tooling is insufficient for a graph product because it says little about endpoint behavior, query budgets, ontology versioning, named-graph boundaries, or traversal semantics, all of which become decision-relevant when software agents depend on the graph at runtime. [source: https://docs.getdbt.com/reference/resource-configs/contract; https://www.w3.org/TR/sparql11-query/; https://davidamitchell.github.io/Research/research/2026-05-12-knowledge-graph-agentic-runtime-dependency.html]

#### 2.3 Domain-local versus federated governance concerns

- [fact] Dehghani's federated computational governance model leaves domain-local semantics to domains but standardizes the globally shared aspects needed for interoperability, and explicitly frames cross-domain identifiers as a global concern when entities span bounded contexts. [source: https://martinfowler.com/articles/data-mesh-principles.html]
- [fact] DPROD's `domain` property intentionally does not constrain the domain class, which means domain semantics can remain local while still attaching a graph product to a business area. [source: https://www.omg.org/spec/DPROD/dprod-ontology.ttl]
- [fact] The production ontology item concluded that production Knowledge Graphs are strongest when teams keep the domain ontology narrow and reuse shared vocabularies such as Provenance Ontology (PROV-O), DCAT, and Friend of a Friend (FOAF) for cross-cutting concerns. [source: https://davidamitchell.github.io/Research/research/2026-05-12-web-ontologies-production-knowledge-graph-agentic.html]
- [inference] The domain should own local concept modeling, quality thresholds, and release cadence for its graph product, while federated governance should own cross-domain identifier conventions, mandatory metadata fields, shared vocabulary reuse rules, and the minimum conformance tests required before a product is advertised to other domains. [source: https://martinfowler.com/articles/data-mesh-principles.html; https://www.omg.org/spec/DPROD/dprod-ontology.ttl; https://davidamitchell.github.io/Research/research/2026-05-12-web-ontologies-production-knowledge-graph-agentic.html]
- [inference] Treating one central enterprise ontology as the whole product boundary would contradict Dehghani's ownership model and create the same central bottleneck that data mesh is trying to avoid, even if cross-domain identity and vocabulary alignment still need global standardization. [source: https://martinfowler.com/articles/data-monolith-to-mesh.html; https://martinfowler.com/articles/data-mesh-principles.html]

#### 2.4 Discoverability and catalogue tooling

- [fact] DataHub documents Data Products as a DataHub-invented logical grouping of assets, requires each data product to belong to exactly one domain, supports ownership and output-port flags, and models metadata through entities, aspects, and relationships in a metadata graph. [source: https://docs.datahub.com/docs/generated/metamodel/entities/dataproduct; https://docs.datahub.com/docs/dataproducts; https://docs.datahub.com/docs/metadata-modeling/metadata-model]
- [fact] OpenMetadata documents domains as decentralized ownership boundaries and data products as discoverable, understandable, usable, reliable, and interoperable outputs managed by domain teams, with product pages carrying owner and asset metadata. [source: https://docs.open-metadata.org/v1.12.x/how-to-guides/data-governance/domains-&-data-products; https://docs.open-metadata.org/v1.12.x/how-to-guides/data-governance/domains-&-data-products/data-products]
- [fact] Collibra documents data products as assets made of context, data, and access, and its operating model includes data product ports and data contracts as first-class related asset types. [source: https://docs.collibra.com/Content/Assets/DataProducts/co_data-product.htm; https://docs.collibra.com/Content/Assets/DataProducts/ta_conf-data-product.htm]
- [fact] Apache Atlas exposes an extensible type system with `Asset`, `DataSet`, `Process`, and custom relationship modeling, but its first-party documentation describes generic metadata modeling rather than native graph-product semantics or DPROD support. [source: https://atlas.apache.org/2.0.0/TypeSystem.html]
- [fact] The adjacent data product ontology item found that public adoption exists but is heterogeneous, because major catalogue products primarily expose their own operating models and extension points instead of native DPROD support. [source: https://davidamitchell.github.io/Research/research/2026-05-12-data-product-ontology.html]
- [inference] Mainstream catalogues can register a Knowledge Graph product's owner, purpose, assets, ports, and documentation, but they do not by themselves provide a graph-specific semantic contract, so teams still need custom metadata, external ontologies, or catalogue extensions to express graph shapes, vocabulary versions, and query-surface guarantees. [source: https://docs.datahub.com/docs/generated/metamodel/entities/dataproduct; https://docs.open-metadata.org/v1.12.x/how-to-guides/data-governance/domains-&-data-products; https://docs.collibra.com/Content/Assets/DataProducts/ta_conf-data-product.htm; https://atlas.apache.org/2.0.0/TypeSystem.html; https://davidamitchell.github.io/Research/research/2026-05-12-data-product-ontology.html]

#### 2.5 Interoperability and graph federation

- [fact] SPARQL is the W3C query language for RDF graphs, and the separate federated-query specification defines the `SERVICE` extension that dispatches part of a query to a remote SPARQL endpoint and joins the results. [source: https://www.w3.org/TR/sparql11-query/; https://www.w3.org/TR/sparql11-federated-query/]
- [fact] The SPARQL federated-query specification also states that remote `SERVICE` execution can fail because the endpoint is down, inaccessible, or returns an error, and that `SERVICE SILENT` suppresses those failures instead of surfacing them. [source: https://www.w3.org/TR/sparql11-federated-query/]
- [fact] LDP defines Hypertext Transfer Protocol (HTTP) rules for reading and writing linked-data resources and containers, while Solid layers secure and permissioned interoperable access over linked-data storage resources and explicitly relates itself to LDP. [source: https://www.w3.org/TR/ldp/; https://solidproject.org/TR/protocol]
- [fact] Bizer et al. describe Linked Data as best practices for publishing and connecting structured data on the web, with interoperability driven by dereferenceable identifiers and typed links between distributed resources. [source: https://eprints.soton.ac.uk/271285/]
- [inference] Cross-domain Knowledge Graph products can therefore interoperate through multiple surfaces, federated SPARQL query, linked-data resource exchange, or catalog-level references to reusable datasets and services, but none of those mechanisms automatically solve semantic alignment, ownership clarity, or runtime reliability. [source: https://www.w3.org/TR/sparql11-federated-query/; https://www.w3.org/TR/ldp/; https://solidproject.org/TR/protocol; https://eprints.soton.ac.uk/271285/]
- [inference] "Transparent" direct cross-product querying by software agents is only safe when shared identifiers, vocabulary alignment, query budgets, and degraded-mode behavior are defined up front, because federation standards define how to connect distributed services but do not promise low latency, complete results, or conflict-free semantics. [source: https://www.w3.org/TR/sparql11-federated-query/; https://www.w3.org/TR/sparql11-query/; https://martinfowler.com/articles/data-mesh-principles.html]

#### 2.6 Runtime dependency and lifecycle implications

- [fact] The runtime dependency item concluded that a Knowledge Graph in the live execution path should be treated as a tiered live service with explicit freshness limits, not as a universally live source of truth for every agent step. [source: https://davidamitchell.github.io/Research/research/2026-05-12-knowledge-graph-agentic-runtime-dependency.html]
- [fact] The lifecycle management item concluded that additive versioning, provenance retention, conservative merge practice, and explicit freshness metadata are the safest operational pattern for agent-facing Knowledge Graphs. [source: https://davidamitchell.github.io/Research/research/2026-05-12-knowledge-graph-lifecycle-management-agentic.html]
- [fact] DCAT 3 includes versioning properties for resources and supports describing data services and distributions separately from datasets. [source: https://www.w3.org/TR/vocab-dcat-3/]
- [fact] DPROD models lifecycle status, input and output datasets, input and output ports, and data-product ownership as explicit machine-readable properties. [source: https://www.omg.org/spec/DPROD/dprod-ontology.ttl]
- [inference] A Knowledge Graph product that is a shared runtime dependency therefore needs two contract layers for freshness and service quality, one for the authoritative graph publication surface and one for derived artifacts such as caches, summaries, or domain-specific exports that software agents may consume instead of live queries. [source: https://davidamitchell.github.io/Research/research/2026-05-12-knowledge-graph-agentic-runtime-dependency.html; https://davidamitchell.github.io/Research/research/2026-05-12-knowledge-graph-lifecycle-management-agentic.html; https://www.w3.org/TR/vocab-dcat-3/]
- [inference] The service commitment should cover endpoint availability, freshness window, semantic-version policy, deprecation notice period, and maximum supported query pattern or traversal budget, because those are the points where a graph product can silently degrade an agent's next decision. [source: https://www.omg.org/spec/DPROD/dprod-ontology.ttl; https://dpds.opendatamesh.org/specifications/dpds/1.0.0/; https://davidamitchell.github.io/Research/research/2026-05-12-knowledge-graph-agentic-runtime-dependency.html]

#### 2.7 Public implementation signals and evidence gaps

- [fact] The consulted catalogue and standards sources document mature data-product operating models and graph interoperability standards, but they do not provide many direct public case studies of organizations openly describing a Knowledge Graph as a data product inside a mature data mesh with runtime-agent dependencies. [source: https://docs.datahub.com/docs/dataproducts; https://docs.open-metadata.org/v1.12.x/how-to-guides/data-governance/domains-&-data-products; https://docs.collibra.com/Content/Assets/DataProducts/co_data-product.htm; https://www.w3.org/TR/sparql11-federated-query/]
- [inference] The best-supported answer is therefore a standards-based operating model qualified by a public-case-study gap, not a claim that one specific organization has already published the definitive Knowledge Graph plus data mesh runtime pattern. [source: https://martinfowler.com/articles/data-mesh-principles.html; https://docs.datahub.com/docs/dataproducts; https://www.omg.org/spec/DPROD/]

### §3 Reasoning

- [inference] The strongest evidence in this item comes from Dehghani's first-party description of the data mesh principles, W3C standards for catalogs and graph interoperability, first-party product documentation from catalog tools, and adjacent completed repository items that already investigated graph runtime and lifecycle mechanics. [source: https://martinfowler.com/articles/data-mesh-principles.html; https://www.w3.org/TR/vocab-dcat-3/; https://www.w3.org/TR/sparql11-federated-query/; https://docs.datahub.com/docs/dataproducts; https://docs.open-metadata.org/v1.12.x/how-to-guides/data-governance/domains-&-data-products; https://docs.collibra.com/Content/Assets/DataProducts/co_data-product.htm; https://davidamitchell.github.io/Research/research/2026-05-12-knowledge-graph-agentic-runtime-dependency.html]
- [inference] The contract recommendation is a layered synthesis rather than a single-standard answer because no consulted source alone covers discoverability, graph-shape validation, port semantics, ownership, lifecycle status, and runtime service commitments for graph products. [source: https://www.w3.org/TR/vocab-dcat-3/; https://www.omg.org/spec/DPROD/dprod-ontology.ttl; https://dpds.opendatamesh.org/specifications/dpds/1.0.0/; https://docs.getdbt.com/reference/resource-configs/contract]
- [assumption] Public first-party documentation is a reasonable proxy for what mainstream catalogue tools support natively, because if a tool had first-class graph-product semantics or native DPROD conformance that capability would likely appear in the main data-product documentation rather than only in hidden implementation detail. [source: https://docs.datahub.com/docs/generated/metamodel/entities/dataproduct; https://docs.open-metadata.org/v1.12.x/how-to-guides/data-governance/domains-&-data-products; https://docs.collibra.com/Content/Assets/DataProducts/ta_conf-data-product.htm; https://atlas.apache.org/2.0.0/TypeSystem.html]

### §4 Consistency Check

- [fact] The consulted sources consistently separate domain-local product ownership from globally standardized interoperability surfaces, even though they express that split with different vocabulary such as domains, ports, metadata graph entities, or federated computational governance. [source: https://martinfowler.com/articles/data-mesh-principles.html; https://docs.datahub.com/docs/dataproducts; https://docs.open-metadata.org/v1.12.x/how-to-guides/data-governance/domains-&-data-products; https://docs.collibra.com/Content/Assets/DataProducts/ta_conf-data-product.htm]
- [inference] The main unresolved contradiction is not about principle direction but about implementation maturity: standards can describe a graph product cleanly, yet mainstream catalogue tools still mostly treat graph products as generic data products with optional extension points rather than with native graph semantics. [source: https://www.omg.org/spec/DPROD/dprod-ontology.ttl; https://docs.datahub.com/docs/generated/metamodel/entities/dataproduct; https://atlas.apache.org/2.0.0/TypeSystem.html]
- [inference] Confidence remains medium rather than high because the normative standards support the recommended operating model strongly, but direct public operational case studies of Knowledge Graph plus data mesh plus software-agent runtime dependency are scarce. [source: https://martinfowler.com/articles/data-mesh-principles.html; https://www.w3.org/TR/vocab-dcat-3/; https://www.w3.org/TR/sparql11-federated-query/]

### §5 Depth and Breadth Expansion

- [inference] Technical lens: the safest graph product is not a raw endpoint alone but a bundle of endpoint, catalog record, shape constraints, version policy, and freshness metadata, because each layer covers a different failure mode that the others do not. [source: https://www.w3.org/TR/vocab-dcat-3/; https://www.omg.org/spec/DPROD/dprod-ontology.ttl; https://davidamitchell.github.io/Research/research/2026-05-12-knowledge-graph-lifecycle-management-agentic.html]
- [inference] Economic lens: unrestricted live federation across graph products raises coordination and runtime cost, so repeated cross-domain needs should usually become curated output products or cached views rather than ad hoc federated queries for every software-agent step. [source: https://www.w3.org/TR/sparql11-federated-query/; https://martinfowler.com/articles/data-mesh-principles.html; https://davidamitchell.github.io/Research/research/2026-05-12-knowledge-graph-agentic-runtime-dependency.html]
- [inference] Governance lens: a Knowledge Graph amplifies the classic data-mesh tension between autonomy and interoperability because graph links encourage cross-domain traversal, which means weak identifier governance or silent ontology drift spreads farther than the equivalent defect in an isolated table product. [source: https://martinfowler.com/articles/data-mesh-principles.html; https://eprints.soton.ac.uk/271285/; https://davidamitchell.github.io/Research/research/2026-05-12-web-ontologies-production-knowledge-graph-agentic.html]
- [inference] Behavioural lens: software agents are particularly sensitive to silent partial failure, because they can continue producing fluent outputs from stale or incomplete graph context, so the product contract should require explicit degraded-mode signaling rather than quiet fallback where possible. [source: https://www.w3.org/TR/sparql11-federated-query/; https://davidamitchell.github.io/Research/research/2026-05-12-knowledge-graph-agentic-runtime-dependency.html]
- [inference] Historical lens: linked-data standards were designed for decentralized publishing and connected resources, which makes them a natural fit for a mesh of graph products, but they still assume that publishers agree enough on identifiers and vocabularies for links to mean the same thing across domains. [source: https://eprints.soton.ac.uk/271285/; https://www.w3.org/TR/ldp/; https://solidproject.org/TR/protocol]

### §6 Synthesis

**Executive summary:**

Treating a Knowledge Graph, a graph-based structure used to exploit diverse, dynamic, and large-scale collections of data, as a data product in a data mesh means making each graph exposure a domain-owned, discoverable, versioned, and contract-bound product rather than a loosely shared semantic utility. [inference; source: https://arxiv.org/abs/2003.02320; https://martinfowler.com/articles/data-mesh-principles.html; https://www.w3.org/TR/vocab-dcat-3/; https://www.omg.org/spec/DPROD/dprod-ontology.ttl]

The domain should own the graph product's local semantics, release cadence, and quality promises, while federated governance should own the cross-domain rules that let graph products compose safely, especially identifiers, mandatory metadata, and conformance expectations. [inference; source: https://martinfowler.com/articles/data-mesh-principles.html; https://www.omg.org/spec/DPROD/dprod-ontology.ttl]

The most defensible contract is layered: DCAT and DPROD for catalog and port metadata, SHACL or equivalent graph-shape validation for structure, and DPDS or a tool-specific descriptor for service promises, obligations, observability, and lifecycle controls. [inference; source: https://www.w3.org/TR/vocab-dcat-3/; https://www.w3.org/TR/shacl/; https://www.omg.org/spec/DPROD/dprod-ontology.ttl; https://dpds.opendatamesh.org/specifications/dpds/1.0.0/]

Software agents should not default to unrestricted live federation across graph products, because federation standards define how to connect distributed graph services but not the latency, freshness, or semantic-alignment guarantees needed for safe runtime dependence. [inference; source: https://www.w3.org/TR/sparql11-federated-query/; https://davidamitchell.github.io/Research/research/2026-05-12-knowledge-graph-agentic-runtime-dependency.html]

**Key findings:**

1. **A Knowledge Graph becomes a data mesh product only when it is packaged as a domain-owned serving unit with explicit metadata, interfaces, and operating commitments, because Dehghani defines the data product as the deployable architectural quantum rather than as raw shared data alone.** ([inference]; medium confidence; source: https://martinfowler.com/articles/data-mesh-principles.html; https://martinfowler.com/articles/data-monolith-to-mesh.html)
2. **The ownership split should keep local graph semantics inside the producing domain while moving shared identifiers, mandatory metadata, and interoperability rules into federated governance, because data mesh standardizes cross-domain concerns but leaves bounded-context modeling to domains.** ([inference]; medium confidence; source: https://martinfowler.com/articles/data-mesh-principles.html; https://www.omg.org/spec/DPROD/dprod-ontology.ttl)
3. **A credible Knowledge Graph product contract needs a layered structure of catalog metadata, graph-shape validation, and operational promises, because no single consulted standard covers discoverability, graph constraints, lifecycle status, ports, and service obligations by itself.** ([inference]; medium confidence; source: https://www.w3.org/TR/vocab-dcat-3/; https://www.omg.org/spec/DPROD/dprod-ontology.ttl; https://dpds.opendatamesh.org/specifications/dpds/1.0.0/; https://docs.getdbt.com/reference/resource-configs/contract)
4. **Mainstream catalog tools can register graph product ownership and discoverability but do not yet provide native graph-specific semantic contracts as their default operating model, so graph teams still need extensions, custom metadata, or external ontologies.** ([inference]; medium confidence; source: https://docs.datahub.com/docs/generated/metamodel/entities/dataproduct; https://docs.open-metadata.org/v1.12.x/how-to-guides/data-governance/domains-&-data-products; https://docs.collibra.com/Content/Assets/DataProducts/ta_conf-data-product.htm; https://atlas.apache.org/2.0.0/TypeSystem.html)
5. **Cross-domain graph interoperability is technically feasible through SPARQL federation, LDP, and Solid, but those standards define transport and query composition rather than safe runtime budgets or semantic alignment, so they are enabling mechanisms rather than sufficient product contracts.** ([inference]; medium confidence; source: https://www.w3.org/TR/sparql11-federated-query/; https://www.w3.org/TR/ldp/; https://solidproject.org/TR/protocol; https://eprints.soton.ac.uk/271285/)
6. **For software-agent runtime dependencies, repeated cross-domain needs should usually be exposed through curated outputs or cached derivative views rather than unrestricted live federation, because graph runtime safety depends on explicit freshness, availability, and query-budget controls.** ([inference]; medium confidence; source: https://www.w3.org/TR/sparql11-federated-query/; https://davidamitchell.github.io/Research/research/2026-05-12-knowledge-graph-agentic-runtime-dependency.html; https://davidamitchell.github.io/Research/research/2026-05-12-knowledge-graph-lifecycle-management-agentic.html)
7. **The minimum lifecycle commitment for a graph product should include semantic version policy, provenance-preserving change publication, freshness windows for authoritative and derived views, and a deprecation notice path, because those are the controls that stop graph change from becoming silent runtime drift.** ([inference]; medium confidence; source: https://www.w3.org/TR/vocab-dcat-3/; https://www.omg.org/spec/DPROD/dprod-ontology.ttl; https://davidamitchell.github.io/Research/research/2026-05-12-knowledge-graph-lifecycle-management-agentic.html)
8. **Public standards support this operating model more strongly than public implementation case studies do, so the recommendation is well grounded as a standards-based design pattern but not yet as a widely documented, mature enterprise norm for Knowledge Graph runtime products.** ([inference]; medium confidence; source: https://martinfowler.com/articles/data-mesh-principles.html; https://www.omg.org/spec/DPROD/; https://docs.datahub.com/docs/dataproducts)

**Evidence map:**

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [inference] A Knowledge Graph data product is a domain-owned serving unit with interfaces and commitments, not raw shared graph data. | https://martinfowler.com/articles/data-mesh-principles.html; https://martinfowler.com/articles/data-monolith-to-mesh.html | medium | Product boundary derived directly from Dehghani's architectural-quantum framing. |
| [inference] Shared identifiers and mandatory interoperability rules belong in federated governance, while local graph semantics stay in the domain. | https://martinfowler.com/articles/data-mesh-principles.html; https://www.omg.org/spec/DPROD/dprod-ontology.ttl | medium | Governance split. |
| [inference] A graph product contract must combine catalog metadata, graph-shape validation, and operational promises. | https://www.w3.org/TR/vocab-dcat-3/; https://www.omg.org/spec/DPROD/dprod-ontology.ttl; https://dpds.opendatamesh.org/specifications/dpds/1.0.0/; https://docs.getdbt.com/reference/resource-configs/contract | medium | Layered contract. |
| [inference] Mainstream catalogues model data products generically and need extension for graph-specific semantics. | https://docs.datahub.com/docs/generated/metamodel/entities/dataproduct; https://docs.open-metadata.org/v1.12.x/how-to-guides/data-governance/domains-&-data-products; https://docs.collibra.com/Content/Assets/DataProducts/ta_conf-data-product.htm; https://atlas.apache.org/2.0.0/TypeSystem.html | medium | Tool support gap. |
| [inference] SPARQL federation, LDP, and Solid enable distribution but do not by themselves guarantee runtime-safe semantics or budgets. | https://www.w3.org/TR/sparql11-federated-query/; https://www.w3.org/TR/ldp/; https://solidproject.org/TR/protocol; https://eprints.soton.ac.uk/271285/ | medium | Interoperability versus runtime guarantee distinction. |
| [inference] Runtime agent use should favor curated outputs or cached derivatives over unrestricted live federation for repeated needs. | https://www.w3.org/TR/sparql11-federated-query/; https://davidamitchell.github.io/Research/research/2026-05-12-knowledge-graph-agentic-runtime-dependency.html; https://davidamitchell.github.io/Research/research/2026-05-12-knowledge-graph-lifecycle-management-agentic.html | medium | Runtime operating pattern. |
| [inference] Graph product lifecycle commitments should include semantic versioning, provenance-preserving publication, freshness windows, and deprecation policy. | https://www.w3.org/TR/vocab-dcat-3/; https://www.omg.org/spec/DPROD/dprod-ontology.ttl; https://davidamitchell.github.io/Research/research/2026-05-12-knowledge-graph-lifecycle-management-agentic.html | medium | Lifecycle control. |
| [inference] Public standards evidence is stronger than public enterprise case-study evidence for this pattern. | https://martinfowler.com/articles/data-mesh-principles.html; https://www.omg.org/spec/DPROD/; https://docs.datahub.com/docs/dataproducts | medium | Evidence-base qualification. |

**Assumptions:**

- [assumption] A producing domain can expose one or more graph products without forcing every cross-domain semantic concern into a single central ontology. Justification: Dehghani's ownership model favors bounded deployable products, while linked-data standards permit distributed resources linked by shared identifiers instead of one monolith. [source: https://martinfowler.com/articles/data-mesh-principles.html; https://eprints.soton.ac.uk/271285/]
- [assumption] A catalogue team's default data-product model can be extended enough to register graph-specific metadata even when the tool does not document first-class Knowledge Graph semantics. Justification: Atlas, DataHub, and Collibra all document extensibility or related asset modeling rather than prohibiting it, but their first-party documentation does not prove uniform implementation effort. [source: https://atlas.apache.org/2.0.0/TypeSystem.html; https://docs.datahub.com/docs/metadata-modeling/metadata-model; https://docs.collibra.com/Content/Assets/DataProducts/ta_conf-data-product.htm]

**Analysis:**

The consulted evidence supports a direct mapping from Dehghani's principles to a graph product operating model, but only after separating three layers that are often conflated: who owns the graph boundary, how the graph is described in the catalog, and how the runtime interface behaves under load and change. [inference; source: https://martinfowler.com/articles/data-mesh-principles.html; https://www.w3.org/TR/vocab-dcat-3/; https://davidamitchell.github.io/Research/research/2026-05-12-knowledge-graph-agentic-runtime-dependency.html]

That separation matters because catalogue standards and product descriptors can make a graph discoverable and contract-visible without making it runtime-safe, while runtime-safe graph use still fails if cross-domain identifiers or vocabulary reuse are not governed. [inference; source: https://www.omg.org/spec/DPROD/dprod-ontology.ttl; https://www.w3.org/TR/sparql11-federated-query/; https://davidamitchell.github.io/Research/research/2026-05-12-web-ontologies-production-knowledge-graph-agentic.html]

The main design trade-off is between federated flexibility and dependable runtime behavior: live cross-product query keeps data closer to source and respects decentralized ownership, but curated outputs, derivative views, and published freshness windows give software agents a safer contract surface for repeated operational use. [inference; source: https://www.w3.org/TR/sparql11-federated-query/; https://martinfowler.com/articles/data-mesh-principles.html; https://davidamitchell.github.io/Research/research/2026-05-12-knowledge-graph-agentic-runtime-dependency.html]

Alternative designs, such as a single enterprise graph team or a purely table-style contract approach, simplify some aspects of coordination but either reintroduce central bottlenecks or fail to describe graph-specific semantics and runtime behaviors that software agents depend on. [inference; source: https://martinfowler.com/articles/data-monolith-to-mesh.html; https://docs.getdbt.com/reference/resource-configs/contract; https://www.omg.org/spec/DPROD/dprod-ontology.ttl]

**Risks, gaps, uncertainties:**

- Direct public case studies that document a Knowledge Graph explicitly operated as a data mesh data product and used as a runtime dependency for software agents are scarce, so this item relies more on standards and operating-model synthesis than on one published enterprise exemplar. [inference; source: https://martinfowler.com/articles/data-mesh-principles.html; https://www.omg.org/spec/DPROD/; https://docs.datahub.com/docs/dataproducts]
- DataHub, OpenMetadata, Collibra, and Atlas clearly model data products, but their public documentation does not define one shared graph-specific contract vocabulary, so implementation detail will vary by toolchain. [fact; source: https://docs.datahub.com/docs/generated/metamodel/entities/dataproduct; https://docs.open-metadata.org/v1.12.x/how-to-guides/data-governance/domains-&-data-products; https://docs.collibra.com/Content/Assets/DataProducts/ta_conf-data-product.htm; https://atlas.apache.org/2.0.0/TypeSystem.html]
- The exact threshold at which live federation becomes unsafe depends on endpoint performance, query complexity, and agent duty cycle, so the recommendation to prefer curated outputs for repeated runtime use is a design inference rather than a universal numeric rule. [inference; source: https://www.w3.org/TR/sparql11-federated-query/; https://davidamitchell.github.io/Research/research/2026-05-12-knowledge-graph-agentic-runtime-dependency.html]

**Open questions:**

- Which minimal shared identifier policy is sufficient for cross-domain graph products in organizations that do not want one global ontology team?
- What is the most practical way to surface graph-product freshness and semantic-version metadata to software-agent tool callers at request time?
- Should graph product obligations and service commitments be expressed in one portable descriptor, or should catalog tools treat those as linked but separate artifacts?

**Recommended data product template:**

- Ownership model: [inference] one producing domain owns the graph product's local ontology terms, source-quality policy, release approvals, and consumer support path, while federated governance defines mandatory identifier rules, required metadata fields, and minimum conformance tests. [source: https://martinfowler.com/articles/data-mesh-principles.html; https://www.omg.org/spec/DPROD/dprod-ontology.ttl]
- Contract format: [inference] publish a DCAT or DPROD catalog record for discoverability, attach SHACL shapes for structural conformance, and pair that with a DPDS-style descriptor or equivalent document covering output ports, observability, obligations, and deprecation policy. [source: https://www.w3.org/TR/vocab-dcat-3/; https://www.w3.org/TR/shacl/; https://www.omg.org/spec/DPROD/dprod-ontology.ttl; https://dpds.opendatamesh.org/specifications/dpds/1.0.0/]
- Versioning policy: [inference] version the authoritative graph and key derivatives separately, use additive-first schema evolution with explicit deprecation, and preserve provenance-bearing change history so consumers can map old semantics to new ones. [source: https://www.w3.org/TR/vocab-dcat-3/; https://davidamitchell.github.io/Research/research/2026-05-12-knowledge-graph-lifecycle-management-agentic.html]
- Discoverability model: [inference] expose the graph product in the organizational catalogue with owner, purpose, domain, output port, freshness window, vocabulary references, and support contact, rather than expecting consumers to discover graph endpoints by convention alone. [source: https://docs.datahub.com/docs/dataproducts; https://docs.open-metadata.org/v1.12.x/how-to-guides/data-governance/domains-&-data-products; https://docs.collibra.com/Content/Assets/DataProducts/co_data-product.htm]
- Service commitment definition: [inference] define endpoint or export availability, freshness window, supported query profile, semantic-version notice period, and degraded-mode behavior, and distinguish the service commitment for live query surfaces from the commitment for cached or summarized derivatives. [source: https://www.omg.org/spec/DPROD/dprod-ontology.ttl; https://dpds.opendatamesh.org/specifications/dpds/1.0.0/; https://davidamitchell.github.io/Research/research/2026-05-12-knowledge-graph-agentic-runtime-dependency.html]

### §7 Recursive Review

- Review result: pass
- Acronym audit: first uses expanded for DCAT, DPDS, DPROD, SHACL, RDF, SPARQL, LDP, HTTP, PROV-O, and FOAF.
- Claim audit: Findings and section 6 remain aligned; factual and inferential claims carry inline source binding.
- Gap audit: public implementation evidence remains thinner than standards evidence and is recorded in Risks, Gaps, and Uncertainties.

---

## Findings

*(Populated from §6 Synthesis above.)*

### Executive Summary

Treating a Knowledge Graph, a graph-based structure used to exploit diverse, dynamic, and large-scale collections of data, as a data product in a data mesh means making each graph exposure a domain-owned, discoverable, versioned, and contract-bound product rather than a loosely shared semantic utility. [inference; source: https://arxiv.org/abs/2003.02320; https://martinfowler.com/articles/data-mesh-principles.html; https://www.w3.org/TR/vocab-dcat-3/; https://www.omg.org/spec/DPROD/dprod-ontology.ttl]

The domain should own the graph product's local semantics, release cadence, and quality promises, while federated governance should own the cross-domain rules that let graph products compose safely, especially identifiers, mandatory metadata, and conformance expectations. [inference; source: https://martinfowler.com/articles/data-mesh-principles.html; https://www.omg.org/spec/DPROD/dprod-ontology.ttl]

The most defensible contract is layered: DCAT and DPROD for catalog and port metadata, SHACL or equivalent graph-shape validation for structure, and DPDS or a tool-specific descriptor for service promises, obligations, observability, and lifecycle controls. [inference; source: https://www.w3.org/TR/vocab-dcat-3/; https://www.w3.org/TR/shacl/; https://www.omg.org/spec/DPROD/dprod-ontology.ttl; https://dpds.opendatamesh.org/specifications/dpds/1.0.0/]

Software agents should not default to unrestricted live federation across graph products, because federation standards define how to connect distributed graph services but not the latency, freshness, or semantic-alignment guarantees needed for safe runtime dependence. [inference; source: https://www.w3.org/TR/sparql11-federated-query/; https://davidamitchell.github.io/Research/research/2026-05-12-knowledge-graph-agentic-runtime-dependency.html]

### Key Findings

1. **A Knowledge Graph becomes a data mesh product only when it is packaged as a domain-owned serving unit with explicit metadata, interfaces, and operating commitments, because Dehghani defines the data product as the deployable architectural quantum rather than as raw shared data alone.** ([inference]; medium confidence; source: https://martinfowler.com/articles/data-mesh-principles.html; https://martinfowler.com/articles/data-monolith-to-mesh.html)
2. **The ownership split should keep local graph semantics inside the producing domain while moving shared identifiers, mandatory metadata, and interoperability rules into federated governance, because data mesh standardizes cross-domain concerns but leaves bounded-context modeling to domains.** ([inference]; medium confidence; source: https://martinfowler.com/articles/data-mesh-principles.html; https://www.omg.org/spec/DPROD/dprod-ontology.ttl)
3. **A credible Knowledge Graph product contract needs a layered structure of catalog metadata, graph-shape validation, and operational promises, because no single consulted standard covers discoverability, graph constraints, lifecycle status, ports, and service obligations by itself.** ([inference]; medium confidence; source: https://www.w3.org/TR/vocab-dcat-3/; https://www.omg.org/spec/DPROD/dprod-ontology.ttl; https://dpds.opendatamesh.org/specifications/dpds/1.0.0/; https://docs.getdbt.com/reference/resource-configs/contract)
4. **Mainstream catalog tools can register graph product ownership and discoverability but do not yet provide native graph-specific semantic contracts as their default operating model, so graph teams still need extensions, custom metadata, or external ontologies.** ([inference]; medium confidence; source: https://docs.datahub.com/docs/generated/metamodel/entities/dataproduct; https://docs.open-metadata.org/v1.12.x/how-to-guides/data-governance/domains-&-data-products; https://docs.collibra.com/Content/Assets/DataProducts/ta_conf-data-product.htm; https://atlas.apache.org/2.0.0/TypeSystem.html)
5. **Cross-domain graph interoperability is technically feasible through SPARQL federation, LDP, and Solid, but those standards define transport and query composition rather than safe runtime budgets or semantic alignment, so they are enabling mechanisms rather than sufficient product contracts.** ([inference]; medium confidence; source: https://www.w3.org/TR/sparql11-federated-query/; https://www.w3.org/TR/ldp/; https://solidproject.org/TR/protocol; https://eprints.soton.ac.uk/271285/)
6. **For software-agent runtime dependencies, repeated cross-domain needs should usually be exposed through curated outputs or cached derivative views rather than unrestricted live federation, because graph runtime safety depends on explicit freshness, availability, and query-budget controls.** ([inference]; medium confidence; source: https://www.w3.org/TR/sparql11-federated-query/; https://davidamitchell.github.io/Research/research/2026-05-12-knowledge-graph-agentic-runtime-dependency.html; https://davidamitchell.github.io/Research/research/2026-05-12-knowledge-graph-lifecycle-management-agentic.html)
7. **The minimum lifecycle commitment for a graph product should include semantic version policy, provenance-preserving change publication, freshness windows for authoritative and derived views, and a deprecation notice path, because those are the controls that stop graph change from becoming silent runtime drift.** ([inference]; medium confidence; source: https://www.w3.org/TR/vocab-dcat-3/; https://www.omg.org/spec/DPROD/dprod-ontology.ttl; https://davidamitchell.github.io/Research/research/2026-05-12-knowledge-graph-lifecycle-management-agentic.html)
8. **Public standards support this operating model more strongly than public implementation case studies do, so the recommendation is well grounded as a standards-based design pattern but not yet as a widely documented, mature enterprise norm for Knowledge Graph runtime products.** ([inference]; medium confidence; source: https://martinfowler.com/articles/data-mesh-principles.html; https://www.omg.org/spec/DPROD/; https://docs.datahub.com/docs/dataproducts)

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [inference] A Knowledge Graph data product is a domain-owned serving unit with interfaces and commitments, not raw shared graph data. | https://martinfowler.com/articles/data-mesh-principles.html; https://martinfowler.com/articles/data-monolith-to-mesh.html | medium | Product boundary derived directly from Dehghani's architectural-quantum framing. |
| [inference] Shared identifiers and mandatory interoperability rules belong in federated governance, while local graph semantics stay in the domain. | https://martinfowler.com/articles/data-mesh-principles.html; https://www.omg.org/spec/DPROD/dprod-ontology.ttl | medium | Governance split. |
| [inference] A graph product contract must combine catalog metadata, graph-shape validation, and operational promises. | https://www.w3.org/TR/vocab-dcat-3/; https://www.omg.org/spec/DPROD/dprod-ontology.ttl; https://dpds.opendatamesh.org/specifications/dpds/1.0.0/; https://docs.getdbt.com/reference/resource-configs/contract | medium | Layered contract. |
| [inference] Mainstream catalogues model data products generically and need extension for graph-specific semantics. | https://docs.datahub.com/docs/generated/metamodel/entities/dataproduct; https://docs.open-metadata.org/v1.12.x/how-to-guides/data-governance/domains-&-data-products; https://docs.collibra.com/Content/Assets/DataProducts/ta_conf-data-product.htm; https://atlas.apache.org/2.0.0/TypeSystem.html | medium | Tool support gap. |
| [inference] SPARQL federation, LDP, and Solid enable distribution but do not by themselves guarantee runtime-safe semantics or budgets. | https://www.w3.org/TR/sparql11-federated-query/; https://www.w3.org/TR/ldp/; https://solidproject.org/TR/protocol; https://eprints.soton.ac.uk/271285/ | medium | Interoperability versus runtime guarantee distinction. |
| [inference] Runtime agent use should favor curated outputs or cached derivatives over unrestricted live federation for repeated needs. | https://www.w3.org/TR/sparql11-federated-query/; https://davidamitchell.github.io/Research/research/2026-05-12-knowledge-graph-agentic-runtime-dependency.html; https://davidamitchell.github.io/Research/research/2026-05-12-knowledge-graph-lifecycle-management-agentic.html | medium | Runtime operating pattern. |
| [inference] Graph product lifecycle commitments should include semantic versioning, provenance-preserving publication, freshness windows, and deprecation policy. | https://www.w3.org/TR/vocab-dcat-3/; https://www.omg.org/spec/DPROD/dprod-ontology.ttl; https://davidamitchell.github.io/Research/research/2026-05-12-knowledge-graph-lifecycle-management-agentic.html | medium | Lifecycle control. |
| [inference] Public standards evidence is stronger than public enterprise case-study evidence for this pattern. | https://martinfowler.com/articles/data-mesh-principles.html; https://www.omg.org/spec/DPROD/; https://docs.datahub.com/docs/dataproducts | medium | Evidence-base qualification. |

### Assumptions

- **Assumption:** A producing domain can expose one or more graph products without forcing every cross-domain semantic concern into a single central ontology. **Justification:** Dehghani's ownership model favors bounded deployable products, while linked-data standards permit distributed resources linked by shared identifiers instead of one monolith. [assumption; source: https://martinfowler.com/articles/data-mesh-principles.html; https://eprints.soton.ac.uk/271285/]
- **Assumption:** A catalogue team's default data-product model can be extended enough to register graph-specific metadata even when the tool does not document first-class Knowledge Graph semantics. **Justification:** Atlas, DataHub, and Collibra all document extensibility or related asset modeling rather than prohibiting it, but their first-party documentation does not prove uniform implementation effort. [assumption; source: https://atlas.apache.org/2.0.0/TypeSystem.html; https://docs.datahub.com/docs/metadata-modeling/metadata-model; https://docs.collibra.com/Content/Assets/DataProducts/ta_conf-data-product.htm]

### Analysis

The consulted evidence supports a direct mapping from Dehghani's principles to a graph product operating model, but only after separating three layers that are often conflated: who owns the graph boundary, how the graph is described in the catalog, and how the runtime interface behaves under load and change. [inference; source: https://martinfowler.com/articles/data-mesh-principles.html; https://www.w3.org/TR/vocab-dcat-3/; https://davidamitchell.github.io/Research/research/2026-05-12-knowledge-graph-agentic-runtime-dependency.html]

That separation matters because catalogue standards and product descriptors can make a graph discoverable and contract-visible without making it runtime-safe, while runtime-safe graph use still fails if cross-domain identifiers or vocabulary reuse are not governed. [inference; source: https://www.omg.org/spec/DPROD/dprod-ontology.ttl; https://www.w3.org/TR/sparql11-federated-query/; https://davidamitchell.github.io/Research/research/2026-05-12-web-ontologies-production-knowledge-graph-agentic.html]

The main design trade-off is between federated flexibility and dependable runtime behavior: live cross-product query keeps data closer to source and respects decentralized ownership, but curated outputs, derivative views, and published freshness windows give software agents a safer contract surface for repeated operational use. [inference; source: https://www.w3.org/TR/sparql11-federated-query/; https://martinfowler.com/articles/data-mesh-principles.html; https://davidamitchell.github.io/Research/research/2026-05-12-knowledge-graph-agentic-runtime-dependency.html]

Alternative designs, such as a single enterprise graph team or a purely table-style contract approach, simplify some aspects of coordination but either reintroduce central bottlenecks or fail to describe graph-specific semantics and runtime behaviors that software agents depend on. [inference; source: https://martinfowler.com/articles/data-monolith-to-mesh.html; https://docs.getdbt.com/reference/resource-configs/contract; https://www.omg.org/spec/DPROD/dprod-ontology.ttl]

### Risks, Gaps, and Uncertainties

- Direct public case studies that document a Knowledge Graph explicitly operated as a data mesh data product and used as a runtime dependency for software agents are scarce, so this item relies more on standards and operating-model synthesis than on one published enterprise exemplar. [inference; source: https://martinfowler.com/articles/data-mesh-principles.html; https://www.omg.org/spec/DPROD/; https://docs.datahub.com/docs/dataproducts]
- DataHub, OpenMetadata, Collibra, and Atlas clearly model data products, but their public documentation does not define one shared graph-specific contract vocabulary, so implementation detail will vary by toolchain. [fact; source: https://docs.datahub.com/docs/generated/metamodel/entities/dataproduct; https://docs.open-metadata.org/v1.12.x/how-to-guides/data-governance/domains-&-data-products; https://docs.collibra.com/Content/Assets/DataProducts/ta_conf-data-product.htm; https://atlas.apache.org/2.0.0/TypeSystem.html]
- The exact threshold at which live federation becomes unsafe depends on endpoint performance, query complexity, and agent duty cycle, so the recommendation to prefer curated outputs for repeated runtime use is a design inference rather than a universal numeric rule. [inference; source: https://www.w3.org/TR/sparql11-federated-query/; https://davidamitchell.github.io/Research/research/2026-05-12-knowledge-graph-agentic-runtime-dependency.html]

### Open Questions

- Which minimal shared identifier policy is sufficient for cross-domain graph products in organizations that do not want one global ontology team?
- What is the most practical way to surface graph-product freshness and semantic-version metadata to software-agent tool callers at request time?
- Should graph product obligations and service commitments be expressed in one portable descriptor, or should catalog tools treat those as linked but separate artifacts?

### Recommended Data Product Template

- **Ownership model:** one producing domain owns the graph product's local ontology terms, source-quality policy, release approvals, and consumer support path, while federated governance defines mandatory identifier rules, required metadata fields, and minimum conformance tests. [inference; source: https://martinfowler.com/articles/data-mesh-principles.html; https://www.omg.org/spec/DPROD/dprod-ontology.ttl]
- **Contract format:** publish a DCAT or DPROD catalog record for discoverability, attach SHACL shapes for structural conformance, and pair that with a DPDS-style descriptor or equivalent document covering output ports, observability, obligations, and deprecation policy. [inference; source: https://www.w3.org/TR/vocab-dcat-3/; https://www.w3.org/TR/shacl/; https://www.omg.org/spec/DPROD/dprod-ontology.ttl; https://dpds.opendatamesh.org/specifications/dpds/1.0.0/]
- **Versioning policy:** version the authoritative graph and key derivatives separately, use additive-first schema evolution with explicit deprecation, and preserve provenance-bearing change history so consumers can map old semantics to new ones. [inference; source: https://www.w3.org/TR/vocab-dcat-3/; https://davidamitchell.github.io/Research/research/2026-05-12-knowledge-graph-lifecycle-management-agentic.html]
- **Discoverability model:** expose the graph product in the organizational catalogue with owner, purpose, domain, output port, freshness window, vocabulary references, and support contact, rather than expecting consumers to discover graph endpoints by convention alone. [inference; source: https://docs.datahub.com/docs/dataproducts; https://docs.open-metadata.org/v1.12.x/how-to-guides/data-governance/domains-&-data-products; https://docs.collibra.com/Content/Assets/DataProducts/co_data-product.htm]
- **Service commitment definition:** define endpoint or export availability, freshness window, supported query profile, semantic-version notice period, and degraded-mode behavior, and distinguish the service commitment for live query surfaces from the commitment for cached or summarized derivatives. [inference; source: https://www.omg.org/spec/DPROD/dprod-ontology.ttl; https://dpds.opendatamesh.org/specifications/dpds/1.0.0/; https://davidamitchell.github.io/Research/research/2026-05-12-knowledge-graph-agentic-runtime-dependency.html]

---

## Output

- Type: knowledge
- Description: Standards-based operating model for treating a Knowledge Graph as a domain-owned data product in a data mesh, with layered contract guidance for discoverability, graph conformance, lifecycle, and runtime-safe software-agent consumption. [inference; source: https://martinfowler.com/articles/data-mesh-principles.html; https://www.w3.org/TR/vocab-dcat-3/; https://www.omg.org/spec/DPROD/dprod-ontology.ttl]
- Links:
  - https://martinfowler.com/articles/data-mesh-principles.html
  - https://www.w3.org/TR/vocab-dcat-3/
  - https://www.omg.org/spec/DPROD/dprod-ontology.ttl
