---
review_count: 2
title: "Data product ontology: definition, adoption, and current relevance"
added: 2026-05-12T08:17:21+00:00
status: completed
priority: medium
blocks: []
tags: [knowledge-graph, governance, organisation]
started: 2026-05-12T18:10:49+00:00
completed: 2026-05-12T18:36:22+00:00
output: [knowledge]
cites:
  - 2026-05-12-web-ontologies-production-knowledge-graph-agentic
related:
  - 2026-05-12-graph-db-saas-knowledge-ontology
  - 2026-05-09-data-governance-standards-ai-agentic-applicability
superseded_by: ~
supersedes: ~
item_type: primary
confidence: medium
versions:
  - version: "1.0"
    sha: af44ec4caa089c357f8e5bed20fd93736d76ba47
    changed: 2026-05-12
    progress: progress/2026-05-12-data-product-ontology.md
    summary: "Initial completion"
---

# Data product ontology: definition, adoption, and current relevance

## Research Question

What is the data product ontology, which organisations and communities use it, how is it applied in practice within data mesh and data management architectures, and is it still current relative to competing and complementary standards?

## Scope

**In scope:**
- Definition and structure of the data product ontology, its core classes, properties, and design intent
- Known implementations: the Data Product Ontology (DPROD) from the Enterprise Knowledge Graph Forum (EKGF) and Object Management Group (OMG), and any related academic or industry-produced ontologies
- Adopters: organisations, vendors, and standards bodies that reference or implement the ontology
- Usage patterns: how the ontology is applied (tooling, catalogues, data contracts, data mesh governance)
- Currency: date of last substantive update, maintenance status, and community activity level
- Related standards and vocabularies: Data Catalog Vocabulary (DCAT), Data Privacy Vocabulary (DPV), schema.org Dataset, Data Product Descriptor Specification (DPDS), and relevant International Organization for Standardization (ISO) data-quality standards such as ISO 8000
- Comparison: where the data product ontology overlaps with or defers to related standards

**Out of scope:**
- General data mesh architecture (except as context for ontology adoption)
- Implementation of a specific data product ontology in this repository
- Vendor-proprietary data product schemas not grounded in a public ontology
- Full tutorial on ontology languages (Resource Description Framework (RDF), Web Ontology Language (OWL), SPARQL)

**Constraints:**
- Sources must be publicly accessible documentation, standards bodies, peer-reviewed papers, or independently authored technical articles, with no vendor marketing-only sources
- Assess currency as of 2024-2026; flag any sources older than three years

## Context

Data mesh literature, a decentralized domain-owned approach to data architecture, treats a data product as a unit with interfaces, lifecycle responsibilities, and explicit contracts, rather than as an unmanaged table or file alone. [inference; source: https://dpds.opendatamesh.org/specifications/dpds/1.0.0/; https://docs.open-metadata.org/v1.12.x/how-to-guides/data-governance/domains-&-data-products]

Machine-readable vocabularies matter when catalogues, marketplaces, and governance tools need to exchange descriptions of datasets, services, ownership, policy, and lifecycle state across organisational boundaries. [fact; source: https://www.w3.org/TR/vocab-dcat-3/; https://www.go-fair.org/fair-principles/]

Before adopting a data product ontology in tooling, the decision-relevant questions are whether a canonical ontology exists, whether its publication state is stable, and whether public implementations extend beyond its originating workgroup. [inference; source: https://www.omg.org/spec/DPROD/; http://production.omgsysml.org/news/releases/pr2024/09-24-24.htm; https://github.com/EKGF/dprod/blob/develop/README.md]

## Approach

1. Identify candidate data product ontologies and vocabularies, starting with DPROD from EKGF and OMG, World Wide Web Consortium (W3C) standards it reuses, and relevant public technical literature from 2020-2026.
2. For each candidate, document: scope, core classes and properties, formal status (draft, published, deprecated), and the publishing body or author.
3. Establish which organisations and communities have adopted each, looking for references in catalogue tools such as Apache Atlas, DataHub, OpenMetadata, and Collibra, plus public repositories and standards registries.
4. Document usage patterns: how is the ontology used in practice, including data contract definition, lineage, catalogue interoperability, and policy enforcement?
5. Assess currency: when was each ontology last meaningfully updated? Is the community actively maintaining it? Are there open issues or active Working Groups?
6. Map relationships to adjacent standards: DCAT-3, Data Privacy Vocabulary (DPV), schema.org Dataset, Data Product Descriptor Specification (DPDS), Findable, Accessible, Interoperable, and Reusable (FAIR) principles, and relevant Object Management Group (OMG) materials.
7. Synthesise a verdict: which data product ontology, if any, has achieved consensus adoption; which is most current; and what are the realistic alternatives if none has achieved critical mass?

## Sources

- [x] [Object Management Group (2024) DPROD public comment announcement](http://production.omgsysml.org/news/releases/pr2024/09-24-24.htm)
- [x] [Object Management Group (n.d.) DPROD specification index](https://www.omg.org/spec/DPROD/)
- [x] [EKGF (n.d.) DPROD specification site](https://ekgf.github.io/dprod/)
- [x] [EKGF (n.d.) Adopt DPROD](https://ekgf.org/dprod/adopt/)
- [x] [EKGF dprod README](https://github.com/EKGF/dprod/blob/develop/README.md)
- [x] [EKGF dprod ontology on develop branch](https://github.com/EKGF/dprod/blob/develop/ontology/dprod/dprod-ontology.ttl)
- [x] [EKGF dprod commit ed07bf2 (2026-05-07)](https://github.com/EKGF/dprod/commit/ed07bf2c472d2e4951d270b894c7799e064f0065)
- [x] [EKGF dprod commit bf2eec0 (2026-05-07)](https://github.com/EKGF/dprod/commit/bf2eec01ea01f4fa4ced8c16b861a0c547df2eed)
- [x] [Object Management Group (2024) DPROD ontology TTL](https://www.omg.org/spec/DPROD/dprod-ontology.ttl)
- [x] [Object Management Group (2024) DPROD shapes TTL](https://www.omg.org/spec/DPROD/dprod-shapes.ttl)
- [x] [W3C (2024) Data Catalog Vocabulary (DCAT) Version 3](https://www.w3.org/TR/vocab-dcat-3/)
- [x] [W3C (2024) DCAT 3 Turtle vocabulary](https://www.w3.org/ns/dcat.ttl)
- [x] [W3C (2017) Shapes Constraint Language (SHACL)](https://www.w3.org/TR/shacl/)
- [x] [W3C (n.d.) Data Privacy Vocabularies and Controls Community Group](https://www.w3.org/community/dpvcg/)
- [x] [schema.org (n.d.) Dataset](https://schema.org/Dataset)
- [x] [GO FAIR (n.d.) FAIR Principles](https://www.go-fair.org/fair-principles/)
- [x] [Open Data Mesh Initiative (n.d.) Data Product Descriptor Specification 1.0.0](https://dpds.opendatamesh.org/specifications/dpds/1.0.0/)
- [x] [EKGF dprod ontology README](https://github.com/EKGF/dprod/blob/develop/ontology/dprod/README.md)
- [x] [EKGF dprod examples README](https://github.com/EKGF/dprod/blob/develop/examples/README.md)
- [x] [EKGF dprod concept README](https://github.com/EKGF/dprod/blob/develop/concept/README.md)
- [x] [DataHub (n.d.) Metadata Standards](https://docs.datahub.com/docs/metadata-standards)
- [x] [DataHub (n.d.) Extending the metadata model](https://docs.datahub.com/docs/metadata-modeling/extending-the-metadata-model)
- [x] [OpenMetadata (n.d.) Domains and Data Products overview](https://docs.open-metadata.org/v1.12.x/how-to-guides/data-governance/domains-&-data-products)
- [x] [OpenMetadata (n.d.) Adding Data Products](https://docs.open-metadata.org/v1.12.x/how-to-guides/data-governance/domains-&-data-products/data-products)
- [x] [OpenMetadata (n.d.) Data Products API reference](https://docs.open-metadata.org/v1.11.x/api-reference/governance/data-products)
- [x] [OpenMetadata ontology file with DPROD-aligned section](https://github.com/open-metadata/OpenMetadata/blob/b8018ab65e87bc7090315d22eb2023c01e592aa3/openmetadata-spec/src/main/resources/rdf/ontology/openmetadata.ttl)
- [x] [Collibra (2025) About data products](https://docs.collibra.com/Content/Assets/DataProducts/co_data-product.htm)
- [x] [Collibra (2025) Configuring and building data products](https://docs.collibra.com/Content/Assets/DataProducts/ta_conf-data-product.htm)
- [x] [Apache Atlas (2020) Type System](https://atlas.apache.org/2.0.0/TypeSystem.html)
- [x] [Zazuko rdf-vocabularies DPROD prefix metadata](https://github.com/zazuko/rdf-vocabularies/blob/59c06d8df355ab3da9b7f78f3262bfa786b2d23c/ontologies/dprod/meta.nt)
- [x] [hyprcat example using DPROD prefix](https://github.com/markjspivey-xwisee/hyprcat/blob/f742b3f0fe6a9f49dc77117d984300fa5092a85c/ex.ttl)
- [x] [ISO (n.d.) ISO 8000 overview page](https://www.iso.org/standard/81745.html)
- [x] [Mitchell (2026) Web ontologies in production Knowledge Graphs for multi-step Artificial Intelligence agents](https://davidamitchell.github.io/Research/research/2026-05-12-web-ontologies-production-knowledge-graph-agentic.html)

---

## Research Skill Output

*(Full output from running the research skill, retained verbatim in the completed item. Sections 0-5 are the investigation, and section 6 seeds the Findings section below.)*

### §0 Initialise

- Question: determine what the data product ontology is, who publishes and maintains it, how it is applied in practice, which organisations reference it, and whether it remains current relative to adjacent standards.
- Scope: DPROD, its public machine-readable artifacts, adjacent standards, public implementation signals, and catalog tooling references are in scope; repository-local implementation work and a full data mesh tutorial are out of scope.
- Constraints: public sources only, primary standards and repository artifacts preferred, 2024-2026 currency emphasized, and every factual or inferential claim labeled explicitly.
- Output format: full section 0 to section 7 research record plus Findings with Executive Summary, Key Findings, Evidence Map, Assumptions, Analysis, Risks, Gaps, Uncertainties, Open Questions, and Output.
- [inference] Prior repository work most relevant to this item is Mitchell (2026) on web ontologies in production Knowledge Graphs because DPROD is built from the same Resource Description Framework (RDF), Web Ontology Language (OWL), Data Catalog Vocabulary (DCAT), and Shapes Constraint Language (SHACL) stack, but narrowed to the data-product surface. [source: https://davidamitchell.github.io/Research/research/2026-05-12-web-ontologies-production-knowledge-graph-agentic.html; https://www.w3.org/TR/vocab-dcat-3/; https://www.w3.org/TR/shacl/]
- [fact] The consulted primary publication surfaces now place DPROD under the Object Management Group (OMG) and Enterprise Knowledge Graph Forum (EKGF) rather than under the Semantic Interoperability Community (SEMIC) or a World Wide Web Consortium (W3C) working group. [source: https://www.omg.org/spec/DPROD/; http://production.omgsysml.org/news/releases/pr2024/09-24-24.htm; https://ekgf.github.io/dprod/]
- [fact] DPROD is presented as a profile or extension of DCAT for describing data products and data services in decentralized data ecosystems. [source: https://ekgf.github.io/dprod/; https://www.omg.org/spec/DPROD/dprod-ontology.ttl]

### §1 Question Decomposition

- A. Candidate ontology surface
  - A1. Which public machine-readable vocabulary is explicitly dedicated to data products?
  - A2. Which adjacent standards model neighboring concerns without being dedicated data product ontologies?
- B. DPROD structure
  - B1. What classes does DPROD define?
  - B2. What object properties and datatype properties does DPROD define?
  - B3. How does DPROD reuse DCAT, SHACL, and other external vocabularies?
- C. DPROD publication and currency
  - C1. Who publishes DPROD on the official publication surfaces?
  - C2. What do those surfaces say about version status, namespace, and modification history?
  - C3. Is the repository still active in 2026?
- D. Usage patterns
  - D1. How do the official examples apply DPROD in practice?
  - D2. Which practical concerns are delegated to complementary vocabularies rather than encoded directly in DPROD?
- E. Adoption
  - E1. Which public repositories or products reference DPROD outside the core EKGF repository?
  - E2. Do major catalog products expose DPROD natively or mainly use their own data-product models?
- F. Comparative relevance
  - F1. Where does DPROD overlap with DCAT, schema.org Dataset, Data Privacy Vocabulary (DPV), and the Findable, Accessible, Interoperable, and Reusable (FAIR) principles?
  - F2. What role does the Data Product Descriptor Specification (DPDS) play relative to DPROD?
  - F3. Has any ontology reached clear consensus adoption across the public ecosystem?

### §2 Investigation

#### 2.1 Candidate ontology landscape

- [fact] In the consulted evidence, DPROD is the only public machine-readable ontology explicitly dedicated to describing data products as first-class resources. [source: https://www.omg.org/spec/DPROD/dprod-ontology.ttl; https://ekgf.github.io/dprod/; https://www.w3.org/TR/vocab-dcat-3/; https://www.w3.org/community/dpvcg/; https://schema.org/Dataset; https://dpds.opendatamesh.org/specifications/dpds/1.0.0/]
- [fact] DCAT is an RDF vocabulary for catalogues, datasets, distributions, and data services, not a dedicated data product ontology. [source: https://www.w3.org/TR/vocab-dcat-3/; https://www.w3.org/ns/dcat.ttl]
- [fact] DPV is a vocabulary and ontology family for privacy, data protection, law, and technology concepts rather than for modeling a data product as a distributable asset. [source: https://www.w3.org/community/dpvcg/]
- [fact] schema.org Dataset provides broad web-discovery metadata for datasets, including distribution and inclusion in data catalogues, but it does not define a dedicated data product type. [source: https://schema.org/Dataset]
- [fact] FAIR principles require machine-actionable metadata, formal representation languages, qualified references, provenance, and community standards, but they are principles rather than an ontology schema. [source: https://www.go-fair.org/fair-principles/]
- [fact] DPDS is a declarative specification for data product descriptor documents, including ports, promises, expectations, contracts, and internal components, rather than an RDF or OWL ontology. [source: https://dpds.opendatamesh.org/specifications/dpds/1.0.0/]
- [inference] The realistic comparison set is therefore one dedicated ontology candidate, DPROD, plus several complementary standards that cover catalog exchange, privacy, discovery, interoperability, or descriptor structure. [source: https://www.omg.org/spec/DPROD/dprod-ontology.ttl; https://www.w3.org/TR/vocab-dcat-3/; https://www.w3.org/community/dpvcg/; https://schema.org/Dataset; https://www.go-fair.org/fair-principles/; https://dpds.opendatamesh.org/specifications/dpds/1.0.0/]

#### 2.2 DPROD structure and design intent

- [fact] The published DPROD ontology declares `dprod:DataProduct` as a subclass of `dcat:Resource`, not as a replacement for `dcat:Dataset` or `dcat:Catalog`. [source: https://www.omg.org/spec/DPROD/dprod-ontology.ttl]
- [fact] The published ontology defines `dprod:DataProductLifecycleStatus`, `dprod:InformationSensitivityClassification`, `dprod:Enumeration`, `dprod:Protocol`, and `dprod:SecuritySchemaType` as classes in addition to `dprod:DataProduct`. [source: https://www.omg.org/spec/DPROD/dprod-ontology.ttl]
- [fact] The published ontology defines properties for owner, lifecycle status, purpose, domain, input port, output port, input dataset, output dataset, distribution inversion, access-service inversion, protocol, and security schema type. [source: https://www.omg.org/spec/DPROD/dprod-ontology.ttl]
- [fact] The published SHACL shapes target `dprod:DataProduct`, `dcat:DataService`, `dcat:Distribution`, and `dcat:Dataset`, which means DPROD validation is intentionally built around reused DCAT classes rather than a fully separate object model. [source: https://www.omg.org/spec/DPROD/dprod-shapes.ttl; https://www.w3.org/TR/shacl/]
- [fact] The DPROD specification site states that DPROD is a profile of DCAT designed to describe data products and to facilitate decentralized publishing, discoverability, and federated search across data marketplaces. [source: https://ekgf.github.io/dprod/]
- [inference] DPROD's design intent is to add just enough domain-specific semantics for a data product while leaving dataset, distribution, and service mechanics to DCAT and conformance checking to SHACL. [source: https://ekgf.github.io/dprod/; https://www.omg.org/spec/DPROD/dprod-ontology.ttl; https://www.omg.org/spec/DPROD/dprod-shapes.ttl; https://www.w3.org/TR/vocab-dcat-3/; https://www.w3.org/TR/shacl/]

#### 2.3 Publication state, namespace, and maintenance

- [fact] The OMG specification index lists DPROD under `https://www.omg.org/spec/DPROD/` and shows version `1.0 beta` with adoption date `Jan 2025` in the "In Process Versions" table. [source: https://www.omg.org/spec/DPROD/]
- [fact] The same OMG index exposes normative machine-readable documents at `DPROD/dprod-ontology.ttl` and `DPROD/dprod-shapes.ttl`. [source: https://www.omg.org/spec/DPROD/]
- [fact] The public comment announcement from September 2024 described DPROD as a proposed specification open for comments before OMG finalization. [source: http://production.omgsysml.org/news/releases/pr2024/09-24-24.htm]
- [fact] The machine-readable ontology currently published under `https://www.omg.org/spec/DPROD/dprod-ontology.ttl` still uses the base URI `https://ekgf.github.io/dprod/` and the version note `OMG Request For Comments Errata 2`. [source: https://www.omg.org/spec/DPROD/dprod-ontology.ttl]
- [fact] The current EKGF repository `develop` branch and the EKGF adoption page use the namespace `https://www.omg.org/spec/DPROD/` and instruct readers to cite `Data Product Ontology (DPROD), Version 1.0`. [source: https://github.com/EKGF/dprod/blob/develop/ontology/dprod/dprod-ontology.ttl; https://ekgf.org/dprod/adopt/]
- [fact] The repository README still describes DPROD as a proposed OMG standard under industry review until December 2024, which is older than the current adoption and specification pages. [source: https://github.com/EKGF/dprod/blob/develop/README.md]
- [fact] The public repository has visible commits in April and May 2026, including `ed07bf2` and `bf2eec0`, which indicates active maintenance after the 2024 public-comment round. [source: https://github.com/EKGF/dprod/commit/ed07bf2c472d2e4951d270b894c7799e064f0065; https://github.com/EKGF/dprod/commit/bf2eec01ea01f4fa4ced8c16b861a0c547df2eed]
- [inference] DPROD is current in the sense of active maintenance and live publication, but its public publication surfaces still show a transitional state rather than one fully settled canonical release narrative. [source: https://www.omg.org/spec/DPROD/; https://www.omg.org/spec/DPROD/dprod-ontology.ttl; https://ekgf.org/dprod/adopt/; https://github.com/EKGF/dprod/blob/develop/README.md; https://github.com/EKGF/dprod/commit/ed07bf2c472d2e4951d270b894c7799e064f0065]

#### 2.4 Usage patterns in the official materials

- [fact] The ontology README says the DPROD ontology is mainly based on the Data Product Descriptor Specification and that the generated artifacts include both ontology terms and SHACL validation shapes. [source: https://github.com/EKGF/dprod/blob/develop/ontology/dprod/README.md; https://dpds.opendatamesh.org/specifications/dpds/1.0.0/]
- [fact] The examples README lists worked examples for data lineage, data rights, data quality, data schema, observability ports, and core extensions, which shows DPROD is intended to be composed with the Provenance Ontology (PROV), Open Digital Rights Language (ODRL), Data Quality Vocabulary (DQV), and SHACL rather than replacing them. [source: https://github.com/EKGF/dprod/blob/develop/examples/README.md; https://www.w3.org/TR/shacl/]
- [fact] The concepts README defines five data product port types in the broader conceptual model, input, output, discovery, observability, and control, and presents DPROD as the public semantic layer over a broader DPDS descriptor model. [source: https://github.com/EKGF/dprod/blob/develop/concept/README.md; https://dpds.opendatamesh.org/specifications/dpds/1.0.0/]
- [inference] In practice, DPROD is used less as a monolithic ontology and more as a semantic profile that binds together DCAT resource descriptions, SHACL validation, and specialized companion vocabularies for policy, quality, lineage, and observability. [source: https://github.com/EKGF/dprod/blob/develop/examples/README.md; https://github.com/EKGF/dprod/blob/develop/concept/README.md; https://www.omg.org/spec/DPROD/dprod-ontology.ttl; https://www.omg.org/spec/DPROD/dprod-shapes.ttl]

#### 2.5 Public implementation and adoption signals

- [fact] Zazuko's public RDF vocabularies repository includes DPROD prefix metadata pointing to the DPROD namespace and ontology file, which is a public reuse signal at the vocabulary-registry layer. [source: https://github.com/zazuko/rdf-vocabularies/blob/59c06d8df355ab3da9b7f78f3262bfa786b2d23c/ontologies/dprod/meta.nt]
- [fact] The public `hyprcat` repository includes a Turtle example that instantiates `dprod:DataProduct` and `dprod:DataProductLifecycleStatus`, which is a public downstream usage example outside the core DPROD repository. [source: https://github.com/markjspivey-xwisee/hyprcat/blob/f742b3f0fe6a9f49dc77117d984300fa5092a85c/ex.ttl]
- [fact] OpenMetadata's ontology file contains a section labeled "Data Product Properties (DPROD aligned)" and subclasses OpenMetadata concepts from `dprod:` terms. [source: https://github.com/open-metadata/OpenMetadata/blob/b8018ab65e87bc7090315d22eb2023c01e592aa3/openmetadata-spec/src/main/resources/rdf/ontology/openmetadata.ttl]
- [fact] OpenMetadata's product documentation and Application Programming Interface (API) reference describe data products as curated domain-scoped collections with ownership and input or output ports. [source: https://docs.open-metadata.org/v1.12.x/how-to-guides/data-governance/domains-&-data-products; https://docs.open-metadata.org/v1.12.x/how-to-guides/data-governance/domains-&-data-products/data-products; https://docs.open-metadata.org/v1.11.x/api-reference/governance/data-products]
- [fact] Collibra's product documentation models data products as assets with context, data, and access components, plus data product ports and data contracts. [source: https://docs.collibra.com/Content/Assets/DataProducts/co_data-product.htm; https://docs.collibra.com/Content/Assets/DataProducts/ta_conf-data-product.htm]
- [fact] DataHub documents its own living metadata model as a de-facto standard and emphasizes extensibility rather than adoption of an external data-product ontology. [source: https://docs.datahub.com/docs/metadata-standards; https://docs.datahub.com/docs/metadata-modeling/extending-the-metadata-model]
- [fact] Apache Atlas documents an extensible type system that allows custom entity modeling, which means DPROD-like concepts can be represented there, but Atlas does not document DPROD as a native standard. [source: https://atlas.apache.org/2.0.0/TypeSystem.html]
- [inference] Public adoption exists, but it is thin and heterogeneous: some projects reference or align with DPROD, while the major catalog products primarily expose their own operating models and extension points instead of native DPROD support. [source: https://github.com/open-metadata/OpenMetadata/blob/b8018ab65e87bc7090315d22eb2023c01e592aa3/openmetadata-spec/src/main/resources/rdf/ontology/openmetadata.ttl; https://docs.open-metadata.org/v1.12.x/how-to-guides/data-governance/domains-&-data-products; https://docs.collibra.com/Content/Assets/DataProducts/co_data-product.htm; https://docs.datahub.com/docs/metadata-standards; https://atlas.apache.org/2.0.0/TypeSystem.html; https://github.com/markjspivey-xwisee/hyprcat/blob/f742b3f0fe6a9f49dc77117d984300fa5092a85c/ex.ttl; https://github.com/zazuko/rdf-vocabularies/blob/59c06d8df355ab3da9b7f78f3262bfa786b2d23c/ontologies/dprod/meta.nt]

#### 2.6 Relationship to adjacent standards

- [fact] DCAT already defines datasets, distributions, data services, catalog resources, versioning properties, and federated catalog interoperability, which is why DPROD reuses DCAT rather than replacing it. [source: https://www.w3.org/TR/vocab-dcat-3/; https://www.w3.org/ns/dcat.ttl; https://ekgf.github.io/dprod/]
- [fact] DPROD's own specification text says it treats ports as DCAT data services and datasets as DCAT datasets, and uses DCAT's `conformsTo` property for publishers to reference their own data-description rules. [source: https://ekgf.github.io/dprod/]
- [fact] DPV provides machine-readable concepts for personal-data processing, legal bases, technologies, and related privacy concepts, which makes it a complementary vocabulary for data-product governance rather than a substitute for DPROD. [source: https://www.w3.org/community/dpvcg/]
- [fact] FAIR principles require rich metadata, searchable registration, formal knowledge-representation languages, qualified references, and provenance, which align with DPROD's interoperability goals but do not themselves define product classes or port properties. [source: https://www.go-fair.org/fair-principles/]
- [fact] schema.org Dataset supports broad web-facing dataset discovery and distribution metadata, but its model is much narrower than DPROD's owner, lifecycle, and port semantics for data products. [source: https://schema.org/Dataset; https://www.omg.org/spec/DPROD/dprod-ontology.ttl]
- [fact] The consulted ISO 8000 overview page did not expose enough clause-level or semantic detail to evaluate it as a direct ontology competitor in this item. [source: https://www.iso.org/standard/81745.html]
- [inference] DPROD is best understood as a domain-specific semantic profile that sits above DCAT and beside DPV, FAIR, and schema.org, while DPDS remains a broader descriptor specification that informs DPROD's conceptual model. [source: https://ekgf.github.io/dprod/; https://www.w3.org/TR/vocab-dcat-3/; https://www.w3.org/community/dpvcg/; https://schema.org/Dataset; https://www.go-fair.org/fair-principles/; https://dpds.opendatamesh.org/specifications/dpds/1.0.0/]

### §3 Reasoning

- [inference] The strongest evidence in this item comes from primary publication surfaces, OMG specification pages, machine-readable ontology and shapes files, and public product documentation. [source: https://www.omg.org/spec/DPROD/; https://www.omg.org/spec/DPROD/dprod-ontology.ttl; https://www.omg.org/spec/DPROD/dprod-shapes.ttl; https://docs.open-metadata.org/v1.11.x/api-reference/governance/data-products; https://docs.collibra.com/Content/Assets/DataProducts/co_data-product.htm]
- [inference] Claims about DPROD's design intent and its place relative to adjacent standards are justified because the ontology, shapes, concept notes, and example catalog all point in the same direction: reuse DCAT for catalog mechanics and compose specialized vocabularies for governance details. [source: https://www.omg.org/spec/DPROD/dprod-ontology.ttl; https://www.omg.org/spec/DPROD/dprod-shapes.ttl; https://github.com/EKGF/dprod/blob/develop/examples/README.md; https://github.com/EKGF/dprod/blob/develop/concept/README.md]
- [inference] Claims about limited consensus adoption are moderate rather than strong because the public evidence base contains some downstream references, but not a broad set of production case studies or native integrations by the dominant open-source and commercial catalog tools. [source: https://github.com/open-metadata/OpenMetadata/blob/b8018ab65e87bc7090315d22eb2023c01e592aa3/openmetadata-spec/src/main/resources/rdf/ontology/openmetadata.ttl; https://docs.datahub.com/docs/metadata-standards; https://docs.collibra.com/Content/Assets/DataProducts/co_data-product.htm; https://atlas.apache.org/2.0.0/TypeSystem.html; https://github.com/markjspivey-xwisee/hyprcat/blob/f742b3f0fe6a9f49dc77117d984300fa5092a85c/ex.ttl]
- [assumption] Public documentation is a reasonable proxy for visible ecosystem adoption in this item because native support for an ontology standard would usually be decision-relevant enough to appear in product docs, API docs, or public examples. [source: https://docs.datahub.com/docs/metadata-standards; https://docs.open-metadata.org/v1.11.x/api-reference/governance/data-products; https://docs.collibra.com/Content/Assets/DataProducts/ta_conf-data-product.htm; https://atlas.apache.org/2.0.0/TypeSystem.html]

### §4 Consistency Check

- [fact] The consulted DPROD publication surfaces are internally inconsistent on version state and namespace: the OMG index says `1.0 beta`, the OMG machine-readable TTL still uses the EKGF namespace and RFC wording, the EKGF adoption page says `Version 1.0`, and the repository README still says proposed standard under review. [source: https://www.omg.org/spec/DPROD/; https://www.omg.org/spec/DPROD/dprod-ontology.ttl; https://ekgf.org/dprod/adopt/; https://github.com/EKGF/dprod/blob/develop/README.md]
- [inference] Because those contradictions cannot be resolved from the consulted primary sources alone, the item treats DPROD as current and actively maintained but stops short of calling its publication state fully settled. [source: https://www.omg.org/spec/DPROD/; https://ekgf.org/dprod/adopt/; https://github.com/EKGF/dprod/commit/ed07bf2c472d2e4951d270b894c7799e064f0065]
- [fact] OpenMetadata's "DPROD aligned" ontology section references `dprod:` terms such as `dprod:InputPort` and `dprod:hasInputPort`, while the currently published official ontology file models ports through `inputPort` and `outputPort` properties to `dcat:DataService`. [source: https://github.com/open-metadata/OpenMetadata/blob/b8018ab65e87bc7090315d22eb2023c01e592aa3/openmetadata-spec/src/main/resources/rdf/ontology/openmetadata.ttl; https://www.omg.org/spec/DPROD/dprod-ontology.ttl]
- [inference] That mismatch is best read as conceptual alignment or adaptation rather than as proof of strict wire-level conformance to the current official ontology file. [source: https://github.com/open-metadata/OpenMetadata/blob/b8018ab65e87bc7090315d22eb2023c01e592aa3/openmetadata-spec/src/main/resources/rdf/ontology/openmetadata.ttl; https://www.omg.org/spec/DPROD/dprod-ontology.ttl]

### §5 Depth and Breadth Expansion

- [inference] Technical lens: DPROD appears operationally lightweight because it adds a small number of semantic terms above DCAT and relies on SHACL for validation rather than introducing a large new inference-heavy ontology stack. [source: https://www.omg.org/spec/DPROD/dprod-ontology.ttl; https://www.omg.org/spec/DPROD/dprod-shapes.ttl]
- [inference] Governance lens: DPROD's explicit owner, lifecycle, sensitivity, and policy hooks make it more governance-ready than plain dataset catalog metadata, even when downstream platforms still need local mapping layers. [source: https://www.omg.org/spec/DPROD/dprod-ontology.ttl; https://docs.collibra.com/Content/Assets/DataProducts/ta_conf-data-product.htm; https://docs.open-metadata.org/v1.11.x/api-reference/governance/data-products]
- [fact] Historical lens: the conceptual lineage runs from Data Product Descriptor Specification ideas about ports and contracts toward a DCAT-profiled ontology intended for interoperable marketplaces and federated search. [source: https://dpds.opendatamesh.org/specifications/dpds/1.0.0/; https://github.com/EKGF/dprod/blob/develop/concept/README.md; https://ekgf.github.io/dprod/]
- [inference] Ecosystem lens: the strongest near-term value of DPROD is as a lingua franca for semantic exchange between tools, not as the internal canonical model of every major metadata platform. [source: https://docs.datahub.com/docs/metadata-standards; https://docs.open-metadata.org/v1.11.x/api-reference/governance/data-products; https://docs.collibra.com/Content/Assets/DataProducts/co_data-product.htm; https://atlas.apache.org/2.0.0/TypeSystem.html; https://github.com/markjspivey-xwisee/hyprcat/blob/f742b3f0fe6a9f49dc77117d984300fa5092a85c/ex.ttl]
- [inference] Organisational lens: adopters that already run RDF, DCAT, SHACL, or knowledge-graph infrastructure will face lower integration cost than teams whose current platforms are schema-first but not ontology-first. [source: https://davidamitchell.github.io/Research/research/2026-05-12-web-ontologies-production-knowledge-graph-agentic.html; https://www.w3.org/TR/vocab-dcat-3/; https://www.w3.org/TR/shacl/; https://docs.datahub.com/docs/metadata-standards]

### §6 Synthesis

**Executive summary:**

DPROD is the most explicit public ontology for data products in the consulted evidence, but it has not achieved broad consensus adoption across mainstream metadata platforms. [inference; source: https://www.omg.org/spec/DPROD/dprod-ontology.ttl; https://docs.datahub.com/docs/metadata-standards; https://docs.collibra.com/Content/Assets/DataProducts/co_data-product.htm; https://docs.open-metadata.org/v1.11.x/api-reference/governance/data-products]

Its technical model is current because the repository is active in 2026 and the ontology remains published on OMG surfaces, but the publication story is still transitional because the public pages disagree on whether DPROD is a beta, a finalized 1.0 release, or still carrying request-for-comments wording. [inference; source: https://www.omg.org/spec/DPROD/; https://www.omg.org/spec/DPROD/dprod-ontology.ttl; https://ekgf.org/dprod/adopt/; https://github.com/EKGF/dprod/blob/develop/README.md; https://github.com/EKGF/dprod/commit/ed07bf2c472d2e4951d270b894c7799e064f0065]

DPROD is best viewed as a DCAT-based semantic profile for data products that composes with SHACL, Data Privacy Vocabulary (DPV), policy vocabularies, and Data Product Descriptor Specification concepts rather than replacing those neighboring standards. [inference; source: https://ekgf.github.io/dprod/; https://www.omg.org/spec/DPROD/dprod-shapes.ttl; https://www.w3.org/TR/vocab-dcat-3/; https://www.w3.org/community/dpvcg/; https://dpds.opendatamesh.org/specifications/dpds/1.0.0/]

For organisations deciding what to adopt, DPROD is relevant and promising for interoperable semantic exchange, but production adoption still requires mapping work into platform-specific models such as OpenMetadata, Collibra, DataHub, or Apache Atlas. [inference; source: https://docs.open-metadata.org/v1.11.x/api-reference/governance/data-products; https://docs.collibra.com/Content/Assets/DataProducts/ta_conf-data-product.htm; https://docs.datahub.com/docs/metadata-standards; https://atlas.apache.org/2.0.0/TypeSystem.html]

**Key findings:**

1. **DPROD is the only dedicated public RDF and OWL ontology for data products found in the consulted evidence, while the other reviewed artifacts are complementary catalog, privacy, interoperability, or descriptor standards rather than competing ontologies.** ([fact]; high confidence; source: https://www.omg.org/spec/DPROD/dprod-ontology.ttl; https://www.w3.org/TR/vocab-dcat-3/; https://www.w3.org/community/dpvcg/; https://schema.org/Dataset; https://dpds.opendatamesh.org/specifications/dpds/1.0.0/)
2. **The published DPROD model is intentionally narrow and reuses DCAT classes for resources, datasets, distributions, and data services, while adding data-product-specific semantics for owner, lifecycle, purpose, domain, ports, datasets, protocol, and security schema type.** ([fact]; high confidence; source: https://www.omg.org/spec/DPROD/dprod-ontology.ttl; https://www.omg.org/spec/DPROD/dprod-shapes.ttl; https://www.w3.org/TR/vocab-dcat-3/)
3. **DPROD remains current in 2026 because its public repository shows active maintenance and the OMG spec index is live, but the standard's publication state is still ambiguous because the official surfaces disagree about whether the release is beta, final 1.0, or still in request-for-comments form.** ([inference]; medium confidence; source: https://www.omg.org/spec/DPROD/; https://www.omg.org/spec/DPROD/dprod-ontology.ttl; https://ekgf.org/dprod/adopt/; https://github.com/EKGF/dprod/blob/develop/README.md; https://github.com/EKGF/dprod/commit/ed07bf2c472d2e4951d270b894c7799e064f0065)
4. **The official DPROD materials use the ontology as a composition layer for real operating concerns, with examples for lineage, data rights, quality, schema, observability, and extensions, which indicates that DPROD is meant to work alongside specialized vocabularies instead of encoding every governance concern directly.** ([inference]; medium confidence; source: https://github.com/EKGF/dprod/blob/develop/examples/README.md; https://github.com/EKGF/dprod/blob/develop/ontology/dprod/README.md; https://github.com/EKGF/dprod/blob/develop/concept/README.md; https://www.w3.org/TR/shacl/)
5. **Public adoption signals exist outside the originating workgroup, including a Zazuko vocabulary entry, a downstream Turtle example repository, and an OpenMetadata ontology alignment, but those signals are still sparse and do not demonstrate broad native ecosystem conformance.** ([inference]; medium confidence; source: https://github.com/zazuko/rdf-vocabularies/blob/59c06d8df355ab3da9b7f78f3262bfa786b2d23c/ontologies/dprod/meta.nt; https://github.com/markjspivey-xwisee/hyprcat/blob/f742b3f0fe6a9f49dc77117d984300fa5092a85c/ex.ttl; https://github.com/open-metadata/OpenMetadata/blob/b8018ab65e87bc7090315d22eb2023c01e592aa3/openmetadata-spec/src/main/resources/rdf/ontology/openmetadata.ttl)
6. **Major catalog platforms publicly document their own data-product operating models or extensible metadata systems, which indicates that DPROD is currently more of an interoperation target than the native internal schema of the dominant tools.** ([inference]; medium confidence; source: https://docs.open-metadata.org/v1.11.x/api-reference/governance/data-products; https://docs.collibra.com/Content/Assets/DataProducts/co_data-product.htm; https://docs.collibra.com/Content/Assets/DataProducts/ta_conf-data-product.htm; https://docs.datahub.com/docs/metadata-standards; https://atlas.apache.org/2.0.0/TypeSystem.html)
7. **Adjacent standards collectively provide the main alternative capability set to DPROD in the consulted evidence, with DCAT handling catalog exchange, DPV handling privacy semantics, schema.org supporting web discovery, FAIR stating interoperability requirements, and DPDS capturing broader descriptor structure and contracts.** ([inference]; medium confidence; source: https://www.w3.org/TR/vocab-dcat-3/; https://www.w3.org/community/dpvcg/; https://schema.org/Dataset; https://www.go-fair.org/fair-principles/; https://dpds.opendatamesh.org/specifications/dpds/1.0.0/)
8. **DPROD remains relevant as the most current dedicated semantic candidate for data-product interoperability, but organisations should expect local mapping work because no public evidence in this item shows industry-wide consensus or out-of-the-box support across the leading catalog products.** ([inference]; medium confidence; source: https://www.omg.org/spec/DPROD/dprod-ontology.ttl; https://github.com/EKGF/dprod/commit/ed07bf2c472d2e4951d270b894c7799e064f0065; https://docs.open-metadata.org/v1.11.x/api-reference/governance/data-products; https://docs.collibra.com/Content/Assets/DataProducts/co_data-product.htm; https://docs.datahub.com/docs/metadata-standards; https://atlas.apache.org/2.0.0/TypeSystem.html)

**Evidence map:**

| claim | source | confidence | notes |
|---|---|---|---|
| [fact] DPROD is the only dedicated public ontology candidate in the consulted set. | https://www.omg.org/spec/DPROD/dprod-ontology.ttl; https://www.w3.org/TR/vocab-dcat-3/; https://www.w3.org/community/dpvcg/; https://schema.org/Dataset; https://dpds.opendatamesh.org/specifications/dpds/1.0.0/ | high | Compared against complementary standards |
| [fact] DPROD reuses DCAT classes and adds a narrow set of product-specific semantics. | https://www.omg.org/spec/DPROD/dprod-ontology.ttl; https://www.omg.org/spec/DPROD/dprod-shapes.ttl; https://www.w3.org/TR/vocab-dcat-3/ | high | Core model structure |
| [inference] DPROD is current, but publication state is inconsistent across official surfaces. | https://www.omg.org/spec/DPROD/; https://www.omg.org/spec/DPROD/dprod-ontology.ttl; https://ekgf.org/dprod/adopt/; https://github.com/EKGF/dprod/blob/develop/README.md; https://github.com/EKGF/dprod/commit/ed07bf2c472d2e4951d270b894c7799e064f0065 | medium | Namespace and status mismatch |
| [fact] Official examples position DPROD as a composition layer for lineage, rights, quality, schema, and observability. | https://github.com/EKGF/dprod/blob/develop/examples/README.md; https://github.com/EKGF/dprod/blob/develop/concept/README.md; https://github.com/EKGF/dprod/blob/develop/ontology/dprod/README.md | high | Practical usage patterns |
| [inference] Public downstream references exist, but they are still sparse within the consulted evidence base. | https://github.com/zazuko/rdf-vocabularies/blob/59c06d8df355ab3da9b7f78f3262bfa786b2d23c/ontologies/dprod/meta.nt; https://github.com/markjspivey-xwisee/hyprcat/blob/f742b3f0fe6a9f49dc77117d984300fa5092a85c/ex.ttl; https://github.com/open-metadata/OpenMetadata/blob/b8018ab65e87bc7090315d22eb2023c01e592aa3/openmetadata-spec/src/main/resources/rdf/ontology/openmetadata.ttl | medium | Limited independent sample size |
| [fact] Major catalog tools use native models or extension systems rather than documented native DPROD support. | https://docs.open-metadata.org/v1.11.x/api-reference/governance/data-products; https://docs.collibra.com/Content/Assets/DataProducts/co_data-product.htm; https://docs.datahub.com/docs/metadata-standards; https://atlas.apache.org/2.0.0/TypeSystem.html | high | Platform-specific modeling dominates |
| [inference] Adjacent standards collectively provide the main alternative capability set to DPROD in the consulted evidence. | https://www.w3.org/TR/vocab-dcat-3/; https://www.w3.org/community/dpvcg/; https://schema.org/Dataset; https://www.go-fair.org/fair-principles/; https://dpds.opendatamesh.org/specifications/dpds/1.0.0/ | medium | Each covers a different control surface |
| [inference] DPROD is relevant for interoperability, but adoption still requires local mapping work. | https://www.omg.org/spec/DPROD/dprod-ontology.ttl; https://docs.open-metadata.org/v1.11.x/api-reference/governance/data-products; https://docs.collibra.com/Content/Assets/DataProducts/ta_conf-data-product.htm; https://docs.datahub.com/docs/metadata-standards; https://atlas.apache.org/2.0.0/TypeSystem.html | medium | No consensus native implementation |

**Assumptions:**

- [assumption] Public product documentation is a reasonable indicator of whether a catalog platform treats DPROD as a first-class supported standard. **Justification:** ontology-native support would normally affect platform entity design, documentation, or API references. [source: https://docs.datahub.com/docs/metadata-standards; https://docs.open-metadata.org/v1.11.x/api-reference/governance/data-products; https://docs.collibra.com/Content/Assets/DataProducts/ta_conf-data-product.htm; https://atlas.apache.org/2.0.0/TypeSystem.html]

**Analysis:**

The evidence weighs most strongly toward DPROD being the leading dedicated semantic candidate because it is the only reviewed artifact that actually publishes an ontology and shapes for data products, rather than only product documentation or a descriptor template. [inference; source: https://www.omg.org/spec/DPROD/dprod-ontology.ttl; https://www.omg.org/spec/DPROD/dprod-shapes.ttl; https://dpds.opendatamesh.org/specifications/dpds/1.0.0/]

The competing interpretation is that mainstream tool adoption currently favors product-local models over shared ontologies, and the consulted DataHub, OpenMetadata, Collibra, and Atlas sources are consistent with that reading. [inference; source: https://docs.datahub.com/docs/metadata-standards; https://docs.open-metadata.org/v1.11.x/api-reference/governance/data-products; https://docs.collibra.com/Content/Assets/DataProducts/co_data-product.htm; https://atlas.apache.org/2.0.0/TypeSystem.html]

That rival interpretation does not displace DPROD, because the same evidence also shows those tools expose extension points, data-product concepts, or alignment hooks rather than a competing public ontology with comparable semantic scope. [inference; source: https://docs.datahub.com/docs/metadata-modeling/extending-the-metadata-model; https://docs.open-metadata.org/v1.11.x/api-reference/governance/data-products; https://github.com/open-metadata/OpenMetadata/blob/b8018ab65e87bc7090315d22eb2023c01e592aa3/openmetadata-spec/src/main/resources/rdf/ontology/openmetadata.ttl; https://docs.collibra.com/Content/Assets/DataProducts/ta_conf-data-product.htm; https://atlas.apache.org/2.0.0/TypeSystem.html]

The strongest challenge to treating DPROD as settled is not technical weakness but publication inconsistency, because the namespace and version story diverges across official surfaces. [inference; source: https://www.omg.org/spec/DPROD/; https://www.omg.org/spec/DPROD/dprod-ontology.ttl; https://ekgf.org/dprod/adopt/; https://github.com/EKGF/dprod/blob/develop/README.md]

That inconsistency lowers confidence in claims about formal status, but it does not overturn the central conclusion that DPROD is current and relevant as an interoperability profile built from the same semantic-web stack described in Mitchell (2026) on production web ontologies. [inference; source: https://www.omg.org/spec/DPROD/dprod-ontology.ttl; https://davidamitchell.github.io/Research/research/2026-05-12-web-ontologies-production-knowledge-graph-agentic.html]

**Risks, gaps, uncertainties:**

- Public independent case studies naming production DPROD deployments remain sparse. [inference; source: https://github.com/zazuko/rdf-vocabularies/blob/59c06d8df355ab3da9b7f78f3262bfa786b2d23c/ontologies/dprod/meta.nt; https://github.com/markjspivey-xwisee/hyprcat/blob/f742b3f0fe6a9f49dc77117d984300fa5092a85c/ex.ttl; https://github.com/open-metadata/OpenMetadata/blob/b8018ab65e87bc7090315d22eb2023c01e592aa3/openmetadata-spec/src/main/resources/rdf/ontology/openmetadata.ttl]
- The consulted official publication surfaces do not fully agree on canonical namespace and release state. [fact; source: https://www.omg.org/spec/DPROD/; https://www.omg.org/spec/DPROD/dprod-ontology.ttl; https://ekgf.org/dprod/adopt/; https://github.com/EKGF/dprod/blob/develop/README.md]
- OpenMetadata's DPROD-aligned ontology section appears broader than the currently published official ontology file, which creates uncertainty about strict conformance. [inference; source: https://github.com/open-metadata/OpenMetadata/blob/b8018ab65e87bc7090315d22eb2023c01e592aa3/openmetadata-spec/src/main/resources/rdf/ontology/openmetadata.ttl; https://www.omg.org/spec/DPROD/dprod-ontology.ttl]
- This item does not make a clause-level comparison to ISO 8000 because the consulted public ISO 8000 overview page did not provide enough semantic detail to justify one. [assumption; source: https://www.iso.org/standard/81745.html]

**Open questions:**

- Will OMG stabilize the canonical namespace and release narrative around DPROD 1.0 in a way that removes the current beta versus final ambiguity?
- Will DPROD remain narrowly aligned to DCAT resource, dataset, and service semantics, or expand toward richer port and contract classes closer to DPDS?
- Which major catalog vendors, if any, will publish native DPROD import, export, or mapping support rather than platform-specific models?
- Would a future DCAT profile or W3C-hosted profile reduce adoption friction more effectively than a standalone OMG-centered publication path?

### §7 Recursive Review

- Review result: pass
- Acronym audit: DPROD, EKGF, OMG, W3C, DCAT, RDF, OWL, SHACL, DPV, FAIR, DPDS, API checked and expanded on first use
- Claim audit: findings and research record claims labeled and source-bound
- Cross-item audit: prior related ontology item integrated and cited
- Remaining uncertainty: publication-state inconsistency retained explicitly in Findings and Risks

---

## Findings

*(Populated from §6 Synthesis above.)*

### Executive Summary

DPROD is the most explicit public ontology for data products in the consulted evidence, but it has not achieved broad consensus adoption across mainstream metadata platforms. [inference; source: https://www.omg.org/spec/DPROD/dprod-ontology.ttl; https://docs.datahub.com/docs/metadata-standards; https://docs.collibra.com/Content/Assets/DataProducts/co_data-product.htm; https://docs.open-metadata.org/v1.11.x/api-reference/governance/data-products]

Its technical model is current because the repository is active in 2026 and the ontology remains published on OMG surfaces, but the publication story is still transitional because the public pages disagree on whether DPROD is a beta, a finalized 1.0 release, or still carrying request-for-comments wording. [inference; source: https://www.omg.org/spec/DPROD/; https://www.omg.org/spec/DPROD/dprod-ontology.ttl; https://ekgf.org/dprod/adopt/; https://github.com/EKGF/dprod/blob/develop/README.md; https://github.com/EKGF/dprod/commit/ed07bf2c472d2e4951d270b894c7799e064f0065]

DPROD is best viewed as a DCAT-based semantic profile for data products that composes with SHACL, DPV, policy vocabularies, and DPDS concepts rather than replacing those neighboring standards. [inference; source: https://ekgf.github.io/dprod/; https://www.omg.org/spec/DPROD/dprod-shapes.ttl; https://www.w3.org/TR/vocab-dcat-3/; https://www.w3.org/community/dpvcg/; https://dpds.opendatamesh.org/specifications/dpds/1.0.0/]

For organisations deciding what to adopt, DPROD is relevant and promising for interoperable semantic exchange, but production adoption still requires mapping work into platform-specific models such as OpenMetadata, Collibra, DataHub, or Apache Atlas. [inference; source: https://docs.open-metadata.org/v1.11.x/api-reference/governance/data-products; https://docs.collibra.com/Content/Assets/DataProducts/ta_conf-data-product.htm; https://docs.datahub.com/docs/metadata-standards; https://atlas.apache.org/2.0.0/TypeSystem.html]

### Key Findings

1. **DPROD is the only dedicated public RDF and OWL ontology for data products found in the consulted evidence, while the other reviewed artifacts are complementary catalog, privacy, interoperability, or descriptor standards rather than competing ontologies.** ([fact]; high confidence; source: https://www.omg.org/spec/DPROD/dprod-ontology.ttl; https://www.w3.org/TR/vocab-dcat-3/; https://www.w3.org/community/dpvcg/; https://schema.org/Dataset; https://dpds.opendatamesh.org/specifications/dpds/1.0.0/)
2. **The published DPROD model is intentionally narrow and reuses DCAT classes for resources, datasets, distributions, and data services, while adding data-product-specific semantics for owner, lifecycle, purpose, domain, ports, datasets, protocol, and security schema type.** ([fact]; high confidence; source: https://www.omg.org/spec/DPROD/dprod-ontology.ttl; https://www.omg.org/spec/DPROD/dprod-shapes.ttl; https://www.w3.org/TR/vocab-dcat-3/)
3. **DPROD remains current in 2026 because its public repository shows active maintenance and the OMG spec index is live, but the standard's publication state is still ambiguous because the official surfaces disagree about whether the release is beta, final 1.0, or still in request-for-comments form.** ([inference]; medium confidence; source: https://www.omg.org/spec/DPROD/; https://www.omg.org/spec/DPROD/dprod-ontology.ttl; https://ekgf.org/dprod/adopt/; https://github.com/EKGF/dprod/blob/develop/README.md; https://github.com/EKGF/dprod/commit/ed07bf2c472d2e4951d270b894c7799e064f0065)
4. **The official DPROD materials use the ontology as a composition layer for real operating concerns, with examples for lineage, data rights, quality, schema, and observability, which indicates that DPROD is meant to work alongside specialized vocabularies instead of encoding every governance concern directly.** ([inference]; medium confidence; source: https://github.com/EKGF/dprod/blob/develop/examples/README.md; https://github.com/EKGF/dprod/blob/develop/ontology/dprod/README.md; https://github.com/EKGF/dprod/blob/develop/concept/README.md; https://www.w3.org/TR/shacl/)
5. **Public adoption signals exist outside the originating workgroup, including a Zazuko vocabulary entry, a downstream Turtle example repository, and an OpenMetadata ontology alignment, but those signals are still sparse and do not demonstrate broad native ecosystem conformance.** ([inference]; medium confidence; source: https://github.com/zazuko/rdf-vocabularies/blob/59c06d8df355ab3da9b7f78f3262bfa786b2d23c/ontologies/dprod/meta.nt; https://github.com/markjspivey-xwisee/hyprcat/blob/f742b3f0fe6a9f49dc77117d984300fa5092a85c/ex.ttl; https://github.com/open-metadata/OpenMetadata/blob/b8018ab65e87bc7090315d22eb2023c01e592aa3/openmetadata-spec/src/main/resources/rdf/ontology/openmetadata.ttl)
6. **Major catalog platforms publicly document their own data-product operating models or extensible metadata systems, which indicates that DPROD is currently more of an interoperation target than the native internal schema of the dominant tools.** ([inference]; medium confidence; source: https://docs.open-metadata.org/v1.11.x/api-reference/governance/data-products; https://docs.collibra.com/Content/Assets/DataProducts/co_data-product.htm; https://docs.collibra.com/Content/Assets/DataProducts/ta_conf-data-product.htm; https://docs.datahub.com/docs/metadata-standards; https://atlas.apache.org/2.0.0/TypeSystem.html)
7. **Adjacent standards collectively provide the main alternative capability set to DPROD in the consulted evidence, with DCAT handling catalog exchange, DPV handling privacy semantics, schema.org supporting web discovery, FAIR stating interoperability requirements, and DPDS capturing broader descriptor structure and contracts.** ([inference]; medium confidence; source: https://www.w3.org/TR/vocab-dcat-3/; https://www.w3.org/community/dpvcg/; https://schema.org/Dataset; https://www.go-fair.org/fair-principles/; https://dpds.opendatamesh.org/specifications/dpds/1.0.0/)
8. **DPROD remains relevant as the most current dedicated semantic candidate for data-product interoperability, but organisations should expect local mapping work because no public evidence in this item shows industry-wide consensus or out-of-the-box support across the leading catalog products.** ([inference]; medium confidence; source: https://www.omg.org/spec/DPROD/dprod-ontology.ttl; https://github.com/EKGF/dprod/commit/ed07bf2c472d2e4951d270b894c7799e064f0065; https://docs.open-metadata.org/v1.11.x/api-reference/governance/data-products; https://docs.collibra.com/Content/Assets/DataProducts/co_data-product.htm; https://docs.datahub.com/docs/metadata-standards; https://atlas.apache.org/2.0.0/TypeSystem.html)

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [fact] DPROD is the only dedicated public ontology candidate in the consulted set. | https://www.omg.org/spec/DPROD/dprod-ontology.ttl; https://www.w3.org/TR/vocab-dcat-3/; https://www.w3.org/community/dpvcg/; https://schema.org/Dataset; https://dpds.opendatamesh.org/specifications/dpds/1.0.0/ | high | Compared against complementary standards |
| [fact] DPROD reuses DCAT classes and adds a narrow set of product-specific semantics. | https://www.omg.org/spec/DPROD/dprod-ontology.ttl; https://www.omg.org/spec/DPROD/dprod-shapes.ttl; https://www.w3.org/TR/vocab-dcat-3/ | high | Core model structure |
| [inference] DPROD is current, but publication state is inconsistent across official surfaces. | https://www.omg.org/spec/DPROD/; https://www.omg.org/spec/DPROD/dprod-ontology.ttl; https://ekgf.org/dprod/adopt/; https://github.com/EKGF/dprod/blob/develop/README.md; https://github.com/EKGF/dprod/commit/ed07bf2c472d2e4951d270b894c7799e064f0065 | medium | Namespace and status mismatch |
| [inference] Official examples position DPROD as a composition layer for lineage, rights, quality, schema, and observability. | https://github.com/EKGF/dprod/blob/develop/examples/README.md; https://github.com/EKGF/dprod/blob/develop/concept/README.md; https://github.com/EKGF/dprod/blob/develop/ontology/dprod/README.md | medium | Support comes mainly from one source family |
| [inference] Public downstream references exist, but they are still sparse within the consulted evidence base. | https://github.com/zazuko/rdf-vocabularies/blob/59c06d8df355ab3da9b7f78f3262bfa786b2d23c/ontologies/dprod/meta.nt; https://github.com/markjspivey-xwisee/hyprcat/blob/f742b3f0fe6a9f49dc77117d984300fa5092a85c/ex.ttl; https://github.com/open-metadata/OpenMetadata/blob/b8018ab65e87bc7090315d22eb2023c01e592aa3/openmetadata-spec/src/main/resources/rdf/ontology/openmetadata.ttl | medium | Limited independent sample size |
| [inference] Major catalog tools use native models or extension systems, so DPROD appears to function more as an interoperation target than as their native internal schema. | https://docs.open-metadata.org/v1.11.x/api-reference/governance/data-products; https://docs.collibra.com/Content/Assets/DataProducts/co_data-product.htm; https://docs.datahub.com/docs/metadata-standards; https://atlas.apache.org/2.0.0/TypeSystem.html | medium | Platform-specific modeling dominates |
| [inference] Adjacent standards collectively provide the main alternative capability set to DPROD in the consulted evidence. | https://www.w3.org/TR/vocab-dcat-3/; https://www.w3.org/community/dpvcg/; https://schema.org/Dataset; https://www.go-fair.org/fair-principles/; https://dpds.opendatamesh.org/specifications/dpds/1.0.0/ | medium | Each covers a different control surface |
| [inference] DPROD is relevant for interoperability, but adoption still requires local mapping work. | https://www.omg.org/spec/DPROD/dprod-ontology.ttl; https://docs.open-metadata.org/v1.11.x/api-reference/governance/data-products; https://docs.collibra.com/Content/Assets/DataProducts/ta_conf-data-product.htm; https://docs.datahub.com/docs/metadata-standards; https://atlas.apache.org/2.0.0/TypeSystem.html | medium | No consensus native implementation |

### Assumptions

- **Assumption:** Public product documentation is a reasonable indicator of whether a catalog platform treats DPROD as a first-class supported standard. **Justification:** Ontology-native support would normally affect platform entity design, documentation, or API references. [assumption; source: https://docs.datahub.com/docs/metadata-standards; https://docs.open-metadata.org/v1.11.x/api-reference/governance/data-products; https://docs.collibra.com/Content/Assets/DataProducts/ta_conf-data-product.htm; https://atlas.apache.org/2.0.0/TypeSystem.html]

### Analysis

The evidence weighs most strongly toward DPROD being the leading dedicated semantic candidate because it is the only reviewed artifact that actually publishes an ontology and shapes for data products, rather than only product documentation or a descriptor template. [inference; source: https://www.omg.org/spec/DPROD/dprod-ontology.ttl; https://www.omg.org/spec/DPROD/dprod-shapes.ttl; https://dpds.opendatamesh.org/specifications/dpds/1.0.0/]

The competing interpretation is that mainstream tool adoption currently favors product-local models over shared ontologies, and the consulted DataHub, OpenMetadata, Collibra, and Atlas sources are consistent with that reading. [inference; source: https://docs.datahub.com/docs/metadata-standards; https://docs.open-metadata.org/v1.11.x/api-reference/governance/data-products; https://docs.collibra.com/Content/Assets/DataProducts/co_data-product.htm; https://atlas.apache.org/2.0.0/TypeSystem.html]

That rival interpretation does not displace DPROD, because the same evidence also shows those tools expose extension points, data-product concepts, or alignment hooks rather than a competing public ontology with comparable semantic scope. [inference; source: https://docs.datahub.com/docs/metadata-modeling/extending-the-metadata-model; https://docs.open-metadata.org/v1.11.x/api-reference/governance/data-products; https://github.com/open-metadata/OpenMetadata/blob/b8018ab65e87bc7090315d22eb2023c01e592aa3/openmetadata-spec/src/main/resources/rdf/ontology/openmetadata.ttl; https://docs.collibra.com/Content/Assets/DataProducts/ta_conf-data-product.htm; https://atlas.apache.org/2.0.0/TypeSystem.html]

The strongest challenge to treating DPROD as settled is not technical weakness but publication inconsistency, because the namespace and version story diverges across official surfaces. [inference; source: https://www.omg.org/spec/DPROD/; https://www.omg.org/spec/DPROD/dprod-ontology.ttl; https://ekgf.org/dprod/adopt/; https://github.com/EKGF/dprod/blob/develop/README.md]

That inconsistency lowers confidence in claims about formal status, but it does not overturn the central conclusion that DPROD is current and relevant as an interoperability profile built from the same semantic-web stack described in Mitchell (2026) on production web ontologies. [inference; source: https://www.omg.org/spec/DPROD/dprod-ontology.ttl; https://davidamitchell.github.io/Research/research/2026-05-12-web-ontologies-production-knowledge-graph-agentic.html]

### Risks, Gaps, and Uncertainties

- Public independent case studies naming production DPROD deployments remain sparse. [inference; source: https://github.com/zazuko/rdf-vocabularies/blob/59c06d8df355ab3da9b7f78f3262bfa786b2d23c/ontologies/dprod/meta.nt; https://github.com/markjspivey-xwisee/hyprcat/blob/f742b3f0fe6a9f49dc77117d984300fa5092a85c/ex.ttl; https://github.com/open-metadata/OpenMetadata/blob/b8018ab65e87bc7090315d22eb2023c01e592aa3/openmetadata-spec/src/main/resources/rdf/ontology/openmetadata.ttl]
- The consulted official publication surfaces do not fully agree on canonical namespace and release state. [fact; source: https://www.omg.org/spec/DPROD/; https://www.omg.org/spec/DPROD/dprod-ontology.ttl; https://ekgf.org/dprod/adopt/; https://github.com/EKGF/dprod/blob/develop/README.md]
- OpenMetadata's DPROD-aligned ontology section appears broader than the currently published official ontology file, which creates uncertainty about strict conformance. [inference; source: https://github.com/open-metadata/OpenMetadata/blob/b8018ab65e87bc7090315d22eb2023c01e592aa3/openmetadata-spec/src/main/resources/rdf/ontology/openmetadata.ttl; https://www.omg.org/spec/DPROD/dprod-ontology.ttl]
- This item does not make a clause-level comparison to ISO 8000 because the consulted public ISO 8000 overview page did not provide enough semantic detail to justify one. [assumption; source: https://www.iso.org/standard/81745.html]

### Open Questions

- Will OMG stabilize the canonical namespace and release narrative around DPROD 1.0 in a way that removes the current beta versus final ambiguity?
- Will DPROD remain narrowly aligned to DCAT resource, dataset, and service semantics, or expand toward richer port and contract classes closer to DPDS?
- Which major catalog vendors, if any, will publish native DPROD import, export, or mapping support rather than platform-specific models?
- Would a future DCAT profile or W3C-hosted profile reduce adoption friction more effectively than a standalone OMG-centered publication path?

---

## Output

*(Fill in when completing, what was produced as a result of this research?)*

- Type: knowledge
- Description: This item documents DPROD's current structure, publication state, adoption signals, and relationship to DCAT, DPV, schema.org, FAIR, DPDS, and major catalog-platform models. [fact; source: https://www.omg.org/spec/DPROD/dprod-ontology.ttl; https://www.w3.org/TR/vocab-dcat-3/; https://www.w3.org/community/dpvcg/; https://schema.org/Dataset; https://www.go-fair.org/fair-principles/; https://dpds.opendatamesh.org/specifications/dpds/1.0.0/]
- Links:
  - https://www.omg.org/spec/DPROD/
  - https://www.omg.org/spec/DPROD/dprod-ontology.ttl
  - https://www.w3.org/TR/vocab-dcat-3/
