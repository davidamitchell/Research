---
review_count: 1
title: "Graph database landscape: pricing, total cost of ownership, interoperability, support, and hiring"
added: 2026-05-13T19:07:27+00:00
status: reviewing
priority: medium
blocks: []
tags: [knowledge-graph, ai-platform, organisation]
started: 2026-05-14T10:22:59+00:00
completed: ~
output: [knowledge]
cites:
  - 2026-05-12-graph-db-saas-knowledge-ontology
  - 2026-05-02-knowledge-graph-schema-cross-session-research-mcp
related:
  - 2026-05-12-data-product-ontology
  - 2026-05-12-web-ontologies-production-knowledge-graph-agentic
superseded_by: ~
supersedes: ~
item_type: primary
confidence: medium
versions: []
---

# Graph database landscape: pricing, total cost of ownership, interoperability, support, and hiring

## Research Question

For the hosted graph database platforms identified in the 2026 Software-as-a-Service (SaaS) knowledge-ontology research, Neo4j AuraDB, Amazon Neptune, Stardog Cloud, Ontotext GraphDB, and Memgraph Cloud, how do their pricing models, total cost of ownership (TCO), interoperability characteristics, support tiers, and community and hiring ecosystems compare, and how should these factors collectively inform a final platform selection decision?

## Scope

**In scope:**
- Pricing models and billing units for each platform as of 2025-2026, including per-query, per-gigabyte storage, per-gigabyte network transfer, per-user seat, and flat monthly or annual tiers where publicly documented
- Total cost of ownership, including data migration and onboarding effort, integration engineering cost, ongoing operational overhead, and support contract spend
- Interoperability, including standards supported such as Resource Description Framework (RDF), Web Ontology Language (OWL), SPARQL Protocol and RDF Query Language (SPARQL), and Cypher, plus documented import and export paths such as Turtle, N-Triples, JavaScript Object Notation for Linked Data (JSON-LD), GraphML, and Comma-Separated Values (CSV)
- Support tiers, including Service Level Agreement (SLA) guarantees, uptime commitments, response time commitments, enterprise support options, and public community-support surfaces
- Community and hiring signals, including developer ecosystem depth, public training surfaces, public support-forum activity, Stack Overflow tag activity, public code surface where available, and certification availability where publicly documented
- Synthesis into a weighted decision framework that combines technical, commercial, and organisational factors

**Out of scope:**
- Self-hosted or on-premises deployments
- Platforms not evaluated in the prior item, except where a non-shortlisted platform is needed for narrow context
- Raw query-performance benchmarking at scale
- Detailed legal or contractual terms beyond publicly documented SLA and support commitments

**Constraints:**
- Prefer primary pricing pages, official documentation, and verifiable public sources, and note where pricing requires sales contact or marketplace negotiation
- Expand every acronym on first use
- Prefer sources dated 2025 or 2026 and flag when older prior research is being used as a baseline rather than as current commercial evidence

## Context

The prior hosted-graph-platform item concluded that Stardog Cloud and Ontotext GraphDB were the strongest ontology-first options in the shortlist, meaning platforms built around Resource Description Framework (RDF), Web Ontology Language (OWL), and SPARQL Protocol and RDF Query Language (SPARQL), while Neo4j AuraDB was the strongest developer-oriented fallback if formal semantics proved unnecessary. [fact; source: https://davidamitchell.github.io/Research/research/2026-05-12-graph-db-saas-knowledge-ontology.html]

The remaining unresolved decision surface is commercial and organisational rather than purely technical: this repository needs to know which platform preserves enough semantic value to justify adoption without creating avoidable procurement, support, or hiring friction for a small Python-first research stack. [inference; source: https://davidamitchell.github.io/Research/research/2026-05-12-graph-db-saas-knowledge-ontology.html; https://davidamitchell.github.io/Research/research/2026-05-02-knowledge-graph-schema-cross-session-research-mcp.html; https://github.com/davidamitchell/Research/blob/main/README.md]

## Approach

1. Retrieve current public pricing and support material for Neo4j AuraDB, Amazon Neptune, Stardog Cloud, Memgraph Cloud, and commercially accessible GraphDB surfaces.
2. Compare billing models, public price transparency, and likely onboarding friction for a small-to-medium pilot.
3. Compare interoperability using documented query languages, standards support, import and export paths, and client-library surfaces.
4. Compare support coverage using uptime commitments, severity-response commitments, and public community channels.
5. Compare ecosystem depth using public training, certification, community, Stack Overflow activity, and public engineering surfaces where they exist.
6. Apply a weighted decision framework tuned to this repository's ontology-first but small-team use case.

## Sources

- [x] [Neo4j Pricing](https://neo4j.com/pricing/)
- [x] [Neo4j Aura Importing Data](https://neo4j.com/docs/aura/classic/auradb/importing-data/)
- [x] [Neo4j Python Driver Manual](https://neo4j.com/docs/python-manual/current/)
- [x] [Neo4j Support Terms](https://neo4j.com/terms/support-terms/)
- [x] [Neo4j GraphAcademy](https://graphacademy.neo4j.com/)
- [x] [Neo4j Certified Professional](https://graphacademy.neo4j.com/certifications/neo4j-certification/)
- [x] [Neo4j Careers](https://neo4j.com/careers/)
- [x] [Neo4j Community](https://community.neo4j.com/)
- [x] [Neo4j GitHub Repository](https://github.com/neo4j/neo4j)
- [x] [Stack Exchange API tag info for neo4j](https://api.stackexchange.com/2.3/tags/neo4j/info?site=stackoverflow)
- [x] [Amazon Neptune Pricing](https://aws.amazon.com/neptune/pricing/)
- [x] [Amazon Neptune Service Level Agreement](https://aws.amazon.com/neptune/sla/)
- [x] [Amazon Neptune openCypher Access](https://docs.aws.amazon.com/neptune/latest/userguide/access-graph-opencypher.html)
- [x] [Amazon Neptune SPARQL Access](https://docs.aws.amazon.com/neptune/latest/userguide/access-graph-sparql.html)
- [x] [Amazon Neptune SPARQL Compliance](https://docs.aws.amazon.com/neptune/latest/userguide/feature-sparql-compliance.html)
- [x] [AWS Support Plans](https://aws.amazon.com/premiumsupport/plans/)
- [x] [AWS Training and Certification](https://aws.amazon.com/training/)
- [x] [Stack Exchange API tag info for amazon-neptune](https://api.stackexchange.com/2.3/tags/amazon-neptune/info?site=stackoverflow)
- [x] [Stardog Pricing](https://www.stardog.com/pricing/)
- [x] [Stardog Cloud](https://www.stardog.com/stardog-cloud/)
- [x] [Stardog Support Packages](https://www.stardog.com/support/)
- [x] [Stardog Platform](https://www.stardog.com/platform/)
- [x] [Stardog Query Documentation](https://docs.stardog.com/query-stardog)
- [x] [Stardog Community](https://community.stardog.com/)
- [x] [Stardog Careers](https://www.stardog.com/company/careers/)
- [x] [Stack Exchange API tag info for stardog](https://api.stackexchange.com/2.3/tags/stardog/info?site=stackoverflow)
- [x] [Memgraph Pricing](https://memgraph.com/pricing)
- [x] [Memgraph Client Libraries](https://memgraph.com/docs/client-libraries)
- [x] [Memgraph Data Migration](https://memgraph.com/docs/data-migration)
- [x] [Memgraph GitHub Repository](https://github.com/memgraph/memgraph)
- [x] [Stack Exchange API tag info for memgraph](https://api.stackexchange.com/2.3/tags/memgraph/info?site=stackoverflow)
- [x] [GraphDB Enterprise 12-Core Cluster on AWS Marketplace](https://aws.amazon.com/marketplace/pp/prodview-rceq2ciyjdipy)
- [x] [Stack Exchange API tag info for graphdb](https://api.stackexchange.com/2.3/tags/graphdb/info?site=stackoverflow)
- [x] [W3C RDF 1.1 Concepts and Abstract Syntax](https://www.w3.org/TR/rdf11-concepts/)
- [x] [W3C SPARQL 1.1 Query Language](https://www.w3.org/TR/sparql11-query/)
- [x] [openCypher](http://www.opencypher.org/)
- [x] [Mitchell (2026) Hosted Software-as-a-Service (SaaS) graph database options for knowledge ontology](https://davidamitchell.github.io/Research/research/2026-05-12-graph-db-saas-knowledge-ontology.html)
- [x] [Mitchell (2026) What entity-relation schema and write-query patterns best support cross-session research provenance and concept reuse for an Artificial Intelligence (AI) agent using the Model Context Protocol (MCP) memory server?](https://davidamitchell.github.io/Research/research/2026-05-02-knowledge-graph-schema-cross-session-research-mcp.html)
- [x] [Mitchell (2026) What is the most current ontology or semantic schema candidate for data products and interoperability metadata?](https://davidamitchell.github.io/Research/research/2026-05-12-data-product-ontology.html)
- [x] [Mitchell (2026) Web ontologies in production Knowledge Graphs for multi-step Artificial Intelligence (AI) agents](https://davidamitchell.github.io/Research/research/2026-05-12-web-ontologies-production-knowledge-graph-agentic.html)

---

## Research Skill Output

*(Full output from running the research skill, retained verbatim in the completed item. Sections 0-5 are the investigation, and section 6 seeds the Findings section below.)*

### §0 Initialise

- Question: compare the shortlisted hosted graph-database platforms on pricing, total cost of ownership, interoperability, support, and ecosystem depth, then recommend a selection path for this repository.
- Scope: hosted shortlist only, with ontology-first, property-graph-first, and dual-model services included; self-hosting, raw performance benchmarking, and detailed contract redlines are out of scope.
- Constraints: prefer primary vendor material, use prior completed items only where they directly sharpen this decision, expand every acronym on first use, and keep commercial uncertainty explicit where pricing is not public.
- Output format: full section 0 to section 7 investigation plus Findings with Executive Summary, Key Findings, Evidence Map, Assumptions, Analysis, Risks, Gaps, Uncertainties, Open Questions, and Output.
- [inference] Prior completed-item cross-reference: the directly relevant repository items are the shortlist item, which established the technical candidate set and initial ontology fit, and the cross-session schema item, which makes small-team adoption friction and Python integration decision-relevant for this repository. [source: https://davidamitchell.github.io/Research/research/2026-05-12-graph-db-saas-knowledge-ontology.html; https://davidamitchell.github.io/Research/research/2026-05-02-knowledge-graph-schema-cross-session-research-mcp.html]
- [inference] Working definition: in this item, semantic-web interoperability means data and query portability through open semantic standards such as RDF and SPARQL, while property-graph interoperability means portability through Cypher and related property-graph query tooling. [source: https://www.w3.org/TR/rdf11-concepts/; https://www.w3.org/TR/sparql11-query/; http://www.opencypher.org/]
- [assumption] The selection should favor the lowest-friction platform that still preserves standards-based semantic value, because the repository remains a small curated research corpus rather than a high-throughput transactional graph workload. [source: https://github.com/davidamitchell/Research/blob/main/README.md; https://davidamitchell.github.io/Research/research/2026-05-02-knowledge-graph-schema-cross-session-research-mcp.html]

### §1 Question Decomposition

- A. Pricing and public commercial transparency
  - A1. Which platforms publish list pricing or machine-readable billing rules for pilot and production use?
  - A2. Which platforms rely mainly on sales contact, marketplace procurement, or custom quotation?
- B. Total cost of ownership
  - B1. Which platforms minimize onboarding and migration effort for a small pilot?
  - B2. Which platforms create variable monthly cost through multiple billing dimensions or surrounding infrastructure requirements?
- C. Interoperability
  - C1. Which platforms document standards-based semantic interoperability through RDF, OWL, SPARQL, or related open interfaces?
  - C2. Which platforms prioritize property-graph developer interoperability through Cypher, Bolt, import tools, and migration paths?
- D. Support and reliability
  - D1. Which platforms publish uptime commitments?
  - D2. Which platforms publish severity-based response commitments?
- E. Community and hiring
  - E1. Which platforms expose the strongest public training, certification, and community surfaces?
  - E2. Which platforms show the clearest public labor-market and ecosystem signals for a small team that may need future hiring or external help?
- F. Decision synthesis
  - F1. Which platform best fits this repository if semantic-web interoperability is a hard requirement?
  - F2. Which fallback is best if the project decides that developer convenience outweighs formal semantic capability?

### §2 Investigation

#### 2.1 Pricing models and commercial transparency

- [fact] Neo4j AuraDB publishes transparent managed-service list pricing with a free tier, AuraDB Professional starting at $65.70 per month for a 1 gigabyte cluster, and AuraDB Business Critical starting at $292 per month for a 2 gigabyte multi-zone cluster. [source: https://neo4j.com/pricing/]
- [fact] Neo4j states that AuraDB pricing is capacity-based and includes storage, input and output, backup, and data transfer inside the stated price, which makes cost modeling comparatively simple. [source: https://neo4j.com/pricing/]
- [fact] Amazon Neptune publishes usage-based pricing across on-demand instances, serverless Neptune Capacity Units, storage, input and output requests, backups, and data transfer, and its worked example prices a db.r5.large deployment with 50 gigabytes of storage and 200 million input and output requests at $296.61 per month. [source: https://aws.amazon.com/neptune/pricing/]
- [fact] Stardog Cloud publishes a free learning environment with shared hosting and up to 1 million stored edges, while enterprise cloud pricing is custom and requires contact with Stardog. [source: https://www.stardog.com/stardog-cloud/; https://www.stardog.com/pricing/]
- [fact] Memgraph states that price scales with memory capacity only and explicitly excludes per-query, compute, replica, and algorithm charges, but its public pricing page does not publish numeric managed-production list prices and instead asks prospects to request an assessment. [source: https://memgraph.com/pricing]
- [inference] The accessible GraphDB commercial source in this session is the AWS Marketplace listing for GraphDB Enterprise Edition 12-Core Cluster, which presents GraphDB as an enterprise marketplace procurement surface rather than a simple self-serve list-price service. [source: https://aws.amazon.com/marketplace/pp/prodview-rceq2ciyjdipy]
- [inference] Public commercial transparency is strongest for Neo4j AuraDB and Amazon Neptune, moderate for Stardog because the free and enterprise boundary is clear even though enterprise pricing is custom, and weakest for GraphDB and Memgraph because the consulted public materials do not expose comparably concrete managed-production list prices. [source: https://neo4j.com/pricing/; https://aws.amazon.com/neptune/pricing/; https://www.stardog.com/stardog-cloud/; https://www.stardog.com/pricing/; https://memgraph.com/pricing; https://aws.amazon.com/marketplace/pp/prodview-rceq2ciyjdipy]

#### 2.2 Total cost of ownership and onboarding effort

- [fact] Neo4j Aura's import service supports PostgreSQL, MySQL, SQL Server, Oracle, BigQuery, Databricks, Snowflake, Amazon Simple Storage Service (Amazon S3), Azure blobs, Google Cloud Storage, and CSV, and Aura also exposes an import Application Programming Interface (API), which reduces pilot onboarding effort for mixed-source data. [source: https://neo4j.com/docs/aura/classic/auradb/importing-data/]
- [fact] Amazon Neptune's SPARQL guidance requires a Neptune database instance and an Amazon Elastic Compute Cloud (Amazon EC2) instance in the same Virtual Private Cloud (VPC), and Neptune bulk loading requires Amazon S3 plus an Amazon Web Services (AWS) Identity and Access Management (IAM) role and VPC endpoint, which adds surrounding infrastructure work beyond the database itself. [source: https://docs.aws.amazon.com/neptune/latest/userguide/access-graph-sparql.html; https://davidamitchell.github.io/Research/research/2026-05-12-graph-db-saas-knowledge-ontology.html]
- [fact] Stardog Cloud offers shared managed hosting for the free tier, dedicated hosting for enterprise, daily backups with 30-day retention, premium support, and a 99.9 percent uptime service-availability commitment on the enterprise plan. [source: https://www.stardog.com/stardog-cloud/]
- [fact] Memgraph Cloud is positioned as a fully managed service with automatic updates and backups, and Memgraph documents migration paths from files, relational systems, Apache Kafka, Apache Pulsar, Apache Spark, and Neo4j, including a one-query Neo4j migration module. [source: https://memgraph.com/pricing; https://memgraph.com/docs/data-migration]
- [inference] GraphDB Enterprise Edition on AWS Marketplace emphasizes massive-scale clusters, dedicated support, and repository sizes up to 1.5 billion RDF triples, which indicates a heavier enterprise operating posture than a lightweight pilot sandbox. [source: https://aws.amazon.com/marketplace/pp/prodview-rceq2ciyjdipy]
- [inference] For a small-to-medium pilot, total cost of ownership is driven less by database list price alone than by onboarding and operating shape: Neo4j AuraDB and Stardog Cloud have the lowest visible adoption friction, Memgraph Cloud is low-friction for Cypher-style migration work, Neptune carries the highest surrounding-cloud operations burden, and GraphDB appears procurement-heavy even before data-model work begins. [source: https://neo4j.com/pricing/; https://neo4j.com/docs/aura/classic/auradb/importing-data/; https://www.stardog.com/stardog-cloud/; https://memgraph.com/pricing; https://memgraph.com/docs/data-migration; https://docs.aws.amazon.com/neptune/latest/userguide/access-graph-sparql.html; https://aws.amazon.com/marketplace/pp/prodview-rceq2ciyjdipy]

#### 2.3 Interoperability and portability

- [fact] Amazon Neptune supports property-graph applications through openCypher and semantic-graph access through SPARQL 1.1, including the SPARQL Graph Store Protocol and the Eclipse Resource Description Framework for Java (RDF4J) console and workbench. [source: https://docs.aws.amazon.com/neptune/latest/userguide/access-graph-opencypher.html; https://docs.aws.amazon.com/neptune/latest/userguide/access-graph-sparql.html; https://docs.aws.amazon.com/neptune/latest/userguide/feature-sparql-compliance.html]
- [fact] Stardog documents SPARQL 1.1 support, OWL and rule reasoning, query-time reasoning, GraphQL access, virtual graphs, and an open-standards position built around RDF, SPARQL, and Shapes Constraint Language (SHACL). [source: https://docs.stardog.com/query-stardog; https://www.stardog.com/platform/]
- [fact] The GraphDB Enterprise marketplace listing states that GraphDB supports World Wide Web Consortium (W3C) RDF-related standards including SPARQL, SHACL, RDF Schema (RDFS), and multiple OWL profiles, and that it exposes Representational State Transfer (REST) APIs such as the Eclipse Resource Description Framework for Java (RDF4J) framework's interfaces for application integration. [source: https://aws.amazon.com/marketplace/pp/prodview-rceq2ciyjdipy]
- [fact] Neo4j AuraDB is a property-graph platform with Cypher as its core query surface, an official Python driver, and a managed importer that reaches common relational and cloud-object sources, but the consulted current materials do not present it as an RDF or OWL platform. [source: https://neo4j.com/docs/python-manual/current/; https://neo4j.com/docs/aura/classic/auradb/importing-data/]
- [inference] Memgraph supports multiple client libraries over Bolt, supports CSV, JavaScript Object Notation Lines (JSONL), Parquet, relational-system migration, and direct Neo4j migration, but the consulted materials position it as a Cypher-compatible property-graph system rather than a semantic-web platform. [source: https://memgraph.com/docs/client-libraries; https://memgraph.com/docs/data-migration]
- [inference] Standards-based semantic interoperability is strongest in Stardog and GraphDB, strongest for mixed semantic and property-graph portability in Neptune, and materially weaker in Neo4j AuraDB and Memgraph because those platforms optimize for property-graph application development rather than ontology-first interchange. [source: https://docs.stardog.com/query-stardog; https://www.stardog.com/platform/; https://aws.amazon.com/marketplace/pp/prodview-rceq2ciyjdipy; https://docs.aws.amazon.com/neptune/latest/userguide/access-graph-sparql.html; https://docs.aws.amazon.com/neptune/latest/userguide/access-graph-opencypher.html; https://neo4j.com/docs/python-manual/current/; https://memgraph.com/docs/client-libraries; https://davidamitchell.github.io/Research/research/2026-05-12-graph-db-saas-knowledge-ontology.html]

#### 2.4 Support tiers and reliability

- [fact] Neo4j AuraDB Business Critical advertises a 99.95 percent uptime SLA and 24x7 support, while Neo4j's support terms publish severity-based response targets ranging from 30 minutes for Signature severity-1 cases to 12 business hours for Essential severity-4 cases. [source: https://neo4j.com/pricing/; https://neo4j.com/terms/support-terms/]
- [fact] Amazon Neptune publishes a 99.99 percent monthly-uptime commitment for Multi-Availability Zone (Multi-AZ) database instances, clusters, and analytics graphs, a 99.5 percent commitment for single-instance and Single-AZ graph deployments, and AWS Support plans publish critical-response targets from under 30 minutes to under 5 minutes depending on plan tier. [source: https://aws.amazon.com/neptune/sla/; https://aws.amazon.com/premiumsupport/plans/]
- [fact] Stardog includes Base Support with enterprise licenses and publishes first-reply targets of one business day for urgent Base cases, four business hours for urgent Premium cases, and two calendar hours for urgent 24/7 cases, alongside a 99.9 percent enterprise-cloud uptime commitment. [source: https://www.stardog.com/support/; https://www.stardog.com/stardog-cloud/]
- [fact] Memgraph Enterprise advertises dedicated engineering support through Slack and enterprise security and operations features, but the consulted public Memgraph pricing material does not publish severity-based response-time commitments or a managed-service uptime SLA. [source: https://memgraph.com/pricing]
- [fact] The consulted GraphDB marketplace source advertises a dedicated support team and a Premium Business Hours Third Level Support Plan, but it does not publish the first-response matrix or uptime percentage with the same precision available for Neo4j, Neptune, or Stardog. [source: https://aws.amazon.com/marketplace/pp/prodview-rceq2ciyjdipy]
- [inference] Neptune offers the strongest published uptime commitment, Neo4j offers the most explicit product-specific response matrix after Stardog, Stardog offers solid enterprise support with a lower uptime commitment than Neptune or Neo4j Business Critical, and Memgraph plus GraphDB expose materially thinner public support detail in the consulted evidence. [source: https://aws.amazon.com/neptune/sla/; https://aws.amazon.com/premiumsupport/plans/; https://neo4j.com/pricing/; https://neo4j.com/terms/support-terms/; https://www.stardog.com/support/; https://www.stardog.com/stardog-cloud/; https://memgraph.com/pricing; https://aws.amazon.com/marketplace/pp/prodview-rceq2ciyjdipy]

#### 2.5 Community, training, and hiring signals

- [inference] Neo4j exposes the strongest public ecosystem signals in the set: GraphAcademy offers free hands-on learning, Neo4j Certified Professional is a formal certification exam, the Neo4j community forum has thousands of topic threads across platform and driver categories, and the Stack Exchange API reports 23,056 questions for the `neo4j` tag. [source: https://graphacademy.neo4j.com/; https://graphacademy.neo4j.com/certifications/neo4j-certification/; https://community.neo4j.com/; https://api.stackexchange.com/2.3/tags/neo4j/info?site=stackoverflow]
- [inference] Amazon Neptune benefits from the broader AWS training and certification ecosystem, and the Stack Exchange API reports 1,021 questions for the `amazon-neptune` tag, which is materially smaller than Neo4j's footprint but still much larger than the niche vendor tags in this comparison. [source: https://aws.amazon.com/training/; https://api.stackexchange.com/2.3/tags/amazon-neptune/info?site=stackoverflow]
- [fact] Stardog's public community forum shows 1,685 topics in the main support category and 52 topics in the Stardog Cloud category, and the Stack Exchange API reports 97 questions for the `stardog` tag. [source: https://community.stardog.com/; https://api.stackexchange.com/2.3/tags/stardog/info?site=stackoverflow]
- [fact] Memgraph exposes community support through Discord, GitHub Discussions, and office hours, and the Stack Exchange API reports 24 questions for the `memgraph` tag. [source: https://memgraph.com/docs/client-libraries; https://api.stackexchange.com/2.3/tags/memgraph/info?site=stackoverflow]
- [fact] GraphDB's accessible marketplace listing claims an ecosystem of more than 50 partners, while the Stack Exchange API reports 565 questions for the generic `graphdb` tag. [source: https://aws.amazon.com/marketplace/pp/prodview-rceq2ciyjdipy; https://api.stackexchange.com/2.3/tags/graphdb/info?site=stackoverflow]
- [inference] Neo4j has the clearest hiring and contractor-readiness advantage because its public training, certification, community, and question volume are all materially stronger than the other shortlisted platforms, while Neptune's labor-market strength is mostly inherited from broader AWS talent supply rather than from a Neptune-specific specialist market. [source: https://graphacademy.neo4j.com/; https://graphacademy.neo4j.com/certifications/neo4j-certification/; https://community.neo4j.com/; https://api.stackexchange.com/2.3/tags/neo4j/info?site=stackoverflow; https://aws.amazon.com/training/; https://api.stackexchange.com/2.3/tags/amazon-neptune/info?site=stackoverflow]
- [inference] The GraphDB Stack Overflow count should be treated as an upper bound rather than a clean vendor-specific ecosystem measure, because `graphdb` is a generic tag and not a unique Ontotext product identifier. [source: https://api.stackexchange.com/2.3/tags/graphdb/info?site=stackoverflow]

#### 2.6 Decision synthesis

- [assumption] A repository-weighted decision framework should emphasize semantic interoperability and adoption friction more than raw enterprise scale, because the repository's likely first deployment is a small ontology-aware research graph rather than a company-wide data-fabric rollout. [source: https://github.com/davidamitchell/Research/blob/main/README.md; https://davidamitchell.github.io/Research/research/2026-05-02-knowledge-graph-schema-cross-session-research-mcp.html]
- [inference] Under weights of 30 percent for semantic interoperability, 25 percent for commercial accessibility and spend predictability, 20 percent for support and operational burden, 15 percent for community and hiring depth, and 10 percent for migration ease, Stardog is the strongest overall fit for this repository if semantic-web interoperability is non-negotiable. [source: https://www.stardog.com/stardog-cloud/; https://www.stardog.com/support/; https://docs.stardog.com/query-stardog; https://www.stardog.com/platform/; https://neo4j.com/pricing/; https://aws.amazon.com/neptune/pricing/; https://memgraph.com/pricing; https://aws.amazon.com/marketplace/pp/prodview-rceq2ciyjdipy]
- [inference] Neo4j AuraDB becomes the strongest overall option if the weight on formal semantic interoperability drops and the weight on community, hiring, and self-serve transparency rises, because it pairs strong pricing clarity and ecosystem depth with much lower adoption friction than the enterprise-oriented semantic platforms. [source: https://neo4j.com/pricing/; https://neo4j.com/docs/aura/classic/auradb/importing-data/; https://graphacademy.neo4j.com/; https://graphacademy.neo4j.com/certifications/neo4j-certification/; https://community.neo4j.com/; https://api.stackexchange.com/2.3/tags/neo4j/info?site=stackoverflow]
- [inference] Neptune is the strongest conditional choice when dual-model support inside AWS is itself a governing requirement, but it is not the best default for this repository because its cost and operating model are more infrastructure-shaped than the self-serve ontology-first or developer-first alternatives. [source: https://docs.aws.amazon.com/neptune/latest/userguide/access-graph-opencypher.html; https://docs.aws.amazon.com/neptune/latest/userguide/access-graph-sparql.html; https://aws.amazon.com/neptune/pricing/; https://aws.amazon.com/neptune/sla/]
- [inference] GraphDB should be treated as the strongest technically credible alternative to Stardog for ontology-first work when materialized inference or existing RDF-centric enterprise relationships matter more than self-serve commercial accessibility, but its current public commercial surface is less decision-friendly than Stardog's. [source: https://aws.amazon.com/marketplace/pp/prodview-rceq2ciyjdipy; https://davidamitchell.github.io/Research/research/2026-05-12-graph-db-saas-knowledge-ontology.html]

### §3 Reasoning

- [inference] I weighted semantic interoperability more heavily than raw ecosystem size because the repository already knows that a plain property graph is only attractive if the project decides to drop ontology-first requirements. [source: https://davidamitchell.github.io/Research/research/2026-05-12-graph-db-saas-knowledge-ontology.html]
- [inference] I treated public price transparency as part of total cost of ownership rather than as a separate cosmetic factor, because opaque procurement and quote-led licensing increase evaluation time, budget uncertainty, and vendor-dependence even before production traffic exists. [source: https://neo4j.com/pricing/; https://aws.amazon.com/neptune/pricing/; https://www.stardog.com/pricing/; https://memgraph.com/pricing; https://aws.amazon.com/marketplace/pp/prodview-rceq2ciyjdipy]
- [inference] I treated training and community signals as partial proxies for hiring friction, because a small team is more likely to rely on broadly available skills, examples, and contractors than on bespoke vendor enablement alone. [source: https://graphacademy.neo4j.com/; https://graphacademy.neo4j.com/certifications/neo4j-certification/; https://community.neo4j.com/; https://community.stardog.com/; https://aws.amazon.com/training/; https://memgraph.com/docs/client-libraries]
- [inference] I did not force public GitHub activity into a cross-vendor ranking because only Neo4j and Memgraph expose large public code surfaces in a directly comparable way, while Stardog, Neptune, and GraphDB are commercially oriented products with different public-code footprints. [source: https://github.com/neo4j/neo4j; https://github.com/memgraph/memgraph]

### §4 Consistency Check

- [inference] The pricing evidence is internally consistent on one important point: AuraDB and Neptune publish explicit billing mechanics, while Stardog, Memgraph, and GraphDB require more sales or marketplace interpretation for production budgeting. [source: https://neo4j.com/pricing/; https://aws.amazon.com/neptune/pricing/; https://www.stardog.com/pricing/; https://memgraph.com/pricing; https://aws.amazon.com/marketplace/pp/prodview-rceq2ciyjdipy]
- [fact] The interoperability evidence is also internally consistent: Stardog, GraphDB, and Neptune explicitly document standards-based semantic surfaces, while Neo4j and Memgraph document property-graph-first surfaces. [source: https://docs.stardog.com/query-stardog; https://www.stardog.com/platform/; https://aws.amazon.com/marketplace/pp/prodview-rceq2ciyjdipy; https://docs.aws.amazon.com/neptune/latest/userguide/access-graph-sparql.html; https://neo4j.com/docs/python-manual/current/; https://memgraph.com/docs/client-libraries]
- [inference] The main unresolved asymmetry is evidence quality for GraphDB's current managed-commercial path, because the accessible marketplace material is useful but thinner than the product, support, and pricing detail available from Neo4j, Neptune, or Stardog. [source: https://aws.amazon.com/marketplace/pp/prodview-rceq2ciyjdipy; https://neo4j.com/pricing/; https://aws.amazon.com/neptune/pricing/; https://www.stardog.com/stardog-cloud/]
- [inference] That asymmetry lowers confidence in the exact GraphDB ranking, but it does not overturn the broader conclusion that GraphDB is semantically credible and commercially less transparent than Stardog for this repository's current decision. [source: https://aws.amazon.com/marketplace/pp/prodview-rceq2ciyjdipy; https://davidamitchell.github.io/Research/research/2026-05-12-graph-db-saas-knowledge-ontology.html]

### §5 Depth and Breadth Expansion

- [inference] Technical lens: Stardog and GraphDB preserve the strongest long-run interoperability with external ontology, governance, and metadata standards, which matters if this repository later wants to exchange data with other semantic systems rather than only query its own local graph. [source: https://www.stardog.com/platform/; https://aws.amazon.com/marketplace/pp/prodview-rceq2ciyjdipy; https://davidamitchell.github.io/Research/research/2026-05-12-data-product-ontology.html; https://davidamitchell.github.io/Research/research/2026-05-12-web-ontologies-production-knowledge-graph-agentic.html]
- [inference] Economic lens: Neptune's variable billing dimensions and AWS infrastructure dependencies make budgeting and operating discipline more important than with AuraDB's flat managed-capacity pricing or Stardog's simpler free-versus-enterprise split. [source: https://aws.amazon.com/neptune/pricing/; https://aws.amazon.com/neptune/sla/; https://neo4j.com/pricing/; https://www.stardog.com/stardog-cloud/]
- [inference] Organisational lens: Neo4j reduces staffing risk most clearly because it combines formal certification, strong community depth, and a large public question base, while Stardog and GraphDB ask an adopter to accept more specialist-market dependence in exchange for better semantic fit. [source: https://graphacademy.neo4j.com/; https://graphacademy.neo4j.com/certifications/neo4j-certification/; https://community.neo4j.com/; https://api.stackexchange.com/2.3/tags/neo4j/info?site=stackoverflow; https://community.stardog.com/; https://api.stackexchange.com/2.3/tags/stardog/info?site=stackoverflow; https://aws.amazon.com/marketplace/pp/prodview-rceq2ciyjdipy]
- [inference] Historical and governance lens: the repository's own completed ontology and interoperability items make standards portability more strategically valuable than it would be for a pure application graph, which is why Stardog and GraphDB remain favored over Neo4j and Memgraph despite weaker public hiring signals. [source: https://davidamitchell.github.io/Research/research/2026-05-12-data-product-ontology.html; https://davidamitchell.github.io/Research/research/2026-05-12-web-ontologies-production-knowledge-graph-agentic.html; https://davidamitchell.github.io/Research/research/2026-05-12-graph-db-saas-knowledge-ontology.html]

### §6 Synthesis

**Executive summary:**

Stardog Cloud is the best overall fit in the consulted evidence if this repository still requires semantic-web interoperability, ontology reasoning, and a managed pilot path in the same platform surface. [inference; source: https://www.stardog.com/stardog-cloud/; https://docs.stardog.com/query-stardog; https://www.stardog.com/platform/]

Neo4j AuraDB and Amazon Neptune are the most commercially transparent options, but they solve different problems: AuraDB is the low-friction property-graph choice, while Neptune is the AWS-native dual-model choice with higher operating complexity and less predictable small-team total cost of ownership. [inference; source: https://neo4j.com/pricing/; https://neo4j.com/docs/aura/classic/auradb/importing-data/; https://aws.amazon.com/neptune/pricing/; https://docs.aws.amazon.com/neptune/latest/userguide/access-graph-sparql.html; https://docs.aws.amazon.com/neptune/latest/userguide/access-graph-opencypher.html]

GraphDB remains technically credible for ontology-first work, but the accessible current evidence is more procurement-oriented and less self-serve than Stardog's, which weakens its ranking for a small repository pilot even though its standards support is strong. [inference; source: https://aws.amazon.com/marketplace/pp/prodview-rceq2ciyjdipy; https://davidamitchell.github.io/Research/research/2026-05-12-graph-db-saas-knowledge-ontology.html]

Neo4j has the clearest community and hiring advantage, so the final decision should be: choose Stardog if semantic interoperability is the real requirement, choose Neo4j AuraDB if that requirement softens, and choose Neptune only when AWS-native dual-model architecture is itself the governing constraint. [inference; source: https://graphacademy.neo4j.com/; https://graphacademy.neo4j.com/certifications/neo4j-certification/; https://community.neo4j.com/; https://api.stackexchange.com/2.3/tags/neo4j/info?site=stackoverflow; https://www.stardog.com/stardog-cloud/; https://aws.amazon.com/neptune/pricing/]

**Key findings:**

1. **Stardog Cloud offers the strongest overall balance for this repository's ontology-first use case because it combines managed hosting, a free learning tier, explicit semantic-web standards support, published enterprise support tiers, and a 99.9 percent uptime commitment in one coherent platform surface.** ([inference]; medium confidence; source: https://www.stardog.com/stardog-cloud/; https://www.stardog.com/support/; https://docs.stardog.com/query-stardog; https://www.stardog.com/platform/)
2. **Neo4j AuraDB and Amazon Neptune provide the clearest public commercial transparency, but Neo4j's flat capacity pricing and low-friction import tooling make its small-team total cost of ownership easier to reason about than Neptune's instance, storage, input and output, backup, and surrounding-AWS billing model.** ([inference]; high confidence; source: https://neo4j.com/pricing/; https://neo4j.com/docs/aura/classic/auradb/importing-data/; https://aws.amazon.com/neptune/pricing/; https://docs.aws.amazon.com/neptune/latest/userguide/access-graph-sparql.html)
3. **GraphDB remains a technically strong ontology-first alternative because it exposes RDF, SPARQL, SHACL, RDFS, OWL, and RDF4J-compatible REST surfaces, but its accessible current commercial path looks more like enterprise marketplace procurement than an easily self-serve pilot service.** ([inference]; low confidence; source: https://aws.amazon.com/marketplace/pp/prodview-rceq2ciyjdipy; https://davidamitchell.github.io/Research/research/2026-05-12-graph-db-saas-knowledge-ontology.html)
4. **Amazon Neptune is the best conditional choice when the project needs both property-graph and semantic-graph support inside Amazon Web Services, but its higher operational overhead and more complex billing structure make it a weaker default recommendation for this repository than Stardog or Neo4j.** ([inference]; medium confidence; source: https://docs.aws.amazon.com/neptune/latest/userguide/access-graph-opencypher.html; https://docs.aws.amazon.com/neptune/latest/userguide/access-graph-sparql.html; https://aws.amazon.com/neptune/pricing/; https://aws.amazon.com/neptune/sla/)
5. **Neo4j has the deepest public community and hiring signal in the shortlist because it pairs formal certification, a large public forum, 23,056 Stack Overflow questions, and a public engineering surface that the other shortlisted products do not match in the consulted evidence.** ([inference]; high confidence; source: https://graphacademy.neo4j.com/; https://graphacademy.neo4j.com/certifications/neo4j-certification/; https://community.neo4j.com/; https://api.stackexchange.com/2.3/tags/neo4j/info?site=stackoverflow; https://github.com/neo4j/neo4j)
6. **Memgraph Cloud is attractive for Cypher-compatible prototyping and migration-heavy work because it offers fully managed hosting, simple memory-based pricing logic, and broad import options, but the consulted evidence does not support choosing it over Stardog, GraphDB, or Neptune for ontology-first interoperability.** ([inference]; medium confidence; source: https://memgraph.com/pricing; https://memgraph.com/docs/data-migration; https://memgraph.com/docs/client-libraries)
7. **Using a repository-weighted framework that prioritizes semantic interoperability over ecosystem depth, the recommended selection path is Stardog first, Neo4j AuraDB second as the non-semantic fallback, Neptune third for AWS-native dual-model requirements, GraphDB fourth as the procurement-heavier semantic alternative, and Memgraph fifth for this specific ontology-first decision.** ([inference]; medium confidence; source: https://www.stardog.com/stardog-cloud/; https://docs.stardog.com/query-stardog; https://neo4j.com/pricing/; https://aws.amazon.com/neptune/pricing/; https://aws.amazon.com/marketplace/pp/prodview-rceq2ciyjdipy; https://memgraph.com/pricing; https://davidamitchell.github.io/Research/research/2026-05-02-knowledge-graph-schema-cross-session-research-mcp.html)

**Evidence map:**

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [inference] Stardog Cloud offers the strongest overall balance for this repository's ontology-first use case. | https://www.stardog.com/stardog-cloud/; https://www.stardog.com/support/; https://docs.stardog.com/query-stardog; https://www.stardog.com/platform/ | medium | Strong semantic fit, moderate ecosystem depth |
| [inference] Neo4j AuraDB has easier small-team total cost of ownership than Neptune despite similarly transparent public pricing. | https://neo4j.com/pricing/; https://neo4j.com/docs/aura/classic/auradb/importing-data/; https://aws.amazon.com/neptune/pricing/; https://docs.aws.amazon.com/neptune/latest/userguide/access-graph-sparql.html | high | Flat managed pricing versus multi-dimensional AWS billing |
| [inference] GraphDB is technically strong but commercially more procurement-heavy than Stardog for a pilot. | https://aws.amazon.com/marketplace/pp/prodview-rceq2ciyjdipy; https://davidamitchell.github.io/Research/research/2026-05-12-graph-db-saas-knowledge-ontology.html | low | Standards support is clear, commercial path is less self-serve |
| [inference] Neptune is best reserved for AWS-native dual-model requirements rather than used as the default platform here. | https://docs.aws.amazon.com/neptune/latest/userguide/access-graph-opencypher.html; https://docs.aws.amazon.com/neptune/latest/userguide/access-graph-sparql.html; https://aws.amazon.com/neptune/pricing/; https://aws.amazon.com/neptune/sla/ | medium | Strong hybrid-model fit, higher operating complexity |
| [inference] Neo4j has the deepest public community and hiring signal in the shortlist. | https://graphacademy.neo4j.com/; https://graphacademy.neo4j.com/certifications/neo4j-certification/; https://community.neo4j.com/; https://api.stackexchange.com/2.3/tags/neo4j/info?site=stackoverflow; https://github.com/neo4j/neo4j | high | Certification plus large public support surface |
| [inference] Memgraph is viable for Cypher migration work but not the leading ontology-first choice. | https://memgraph.com/pricing; https://memgraph.com/docs/data-migration; https://memgraph.com/docs/client-libraries | medium | Strong migration story, weak semantic standards story |
| [inference] The recommended selection order for this repository is Stardog, Neo4j AuraDB, Neptune, GraphDB, then Memgraph. | https://www.stardog.com/stardog-cloud/; https://neo4j.com/pricing/; https://aws.amazon.com/neptune/pricing/; https://aws.amazon.com/marketplace/pp/prodview-rceq2ciyjdipy; https://memgraph.com/pricing; https://davidamitchell.github.io/Research/research/2026-05-02-knowledge-graph-schema-cross-session-research-mcp.html | medium | Weighting favors semantic portability over labor-market depth |

**Assumptions:**

- [assumption] The first production deployment remains small enough that procurement simplicity and operational burden matter more than extreme cluster scale. [source: https://github.com/davidamitchell/Research/blob/main/README.md; https://davidamitchell.github.io/Research/research/2026-05-02-knowledge-graph-schema-cross-session-research-mcp.html]
- [assumption] Standards-based semantic interoperability remains a real project requirement rather than a merely aspirational preference, because otherwise Neo4j AuraDB would score first once ecosystem depth and self-serve transparency are weighted more heavily. [source: https://davidamitchell.github.io/Research/research/2026-05-12-graph-db-saas-knowledge-ontology.html; https://davidamitchell.github.io/Research/research/2026-05-12-web-ontologies-production-knowledge-graph-agentic.html]

**Analysis:**

- [inference] The strongest rival explanation is that Neo4j AuraDB should win outright because commercial transparency, ecosystem depth, and hiring ease often dominate early adoption success for small teams. That explanation is credible and becomes decisive if ontology-first semantics stop being mandatory. [source: https://neo4j.com/pricing/; https://graphacademy.neo4j.com/; https://graphacademy.neo4j.com/certifications/neo4j-certification/; https://community.neo4j.com/; https://api.stackexchange.com/2.3/tags/neo4j/info?site=stackoverflow]
- [inference] I still rank Stardog first because the repository's own prior completed work makes semantic-web portability, ontology reasoning, and later interoperability with governance and metadata standards materially decision-relevant rather than optional nice-to-have features. [source: https://davidamitchell.github.io/Research/research/2026-05-12-graph-db-saas-knowledge-ontology.html; https://davidamitchell.github.io/Research/research/2026-05-12-data-product-ontology.html; https://davidamitchell.github.io/Research/research/2026-05-12-web-ontologies-production-knowledge-graph-agentic.html]
- [inference] The weighting that produced the final order was 30 percent semantic interoperability, 25 percent commercial accessibility and spend predictability, 20 percent support and operational burden, 15 percent community and hiring depth, and 10 percent migration ease. Under those weights, Stardog beats Neo4j because semantic fit outweighs Neo4j's ecosystem advantage, while GraphDB loses to Stardog because its current commercial surface is less transparent. [source: https://www.stardog.com/stardog-cloud/; https://www.stardog.com/support/; https://neo4j.com/pricing/; https://graphacademy.neo4j.com/; https://aws.amazon.com/marketplace/pp/prodview-rceq2ciyjdipy]
- [inference] Neptune remains strategically important even though it ranks third, because it is the only clearly documented dual-model option in the consulted current evidence and therefore becomes the best path if the repository later insists on both SPARQL and property-graph workloads inside the same AWS-aligned platform. [source: https://docs.aws.amazon.com/neptune/latest/userguide/access-graph-opencypher.html; https://docs.aws.amazon.com/neptune/latest/userguide/access-graph-sparql.html; https://aws.amazon.com/neptune/pricing/]

**Risks, gaps, uncertainties:**

- [inference] GraphDB's precise commercial ranking is less certain than the other platforms because the accessible current evidence in this session came mainly from its AWS Marketplace surface rather than from a fully detailed self-serve pricing and support matrix. [source: https://aws.amazon.com/marketplace/pp/prodview-rceq2ciyjdipy]
- [inference] The interoperability comparison for Java frameworks, Protégé, Apache Jena, LangChain, and LlamaIndex remains uneven because the consulted official materials did not document those adjacent-tool integrations symmetrically across all five platforms. [source: https://docs.stardog.com/query-stardog; https://docs.aws.amazon.com/neptune/latest/userguide/access-graph-sparql.html; https://neo4j.com/docs/python-manual/current/; https://memgraph.com/docs/client-libraries; https://aws.amazon.com/marketplace/pp/prodview-rceq2ciyjdipy]
- [fact] The `graphdb` Stack Overflow tag is generic, so it is not a clean Ontotext-only ecosystem proxy in the way that `neo4j`, `amazon-neptune`, `stardog`, and `memgraph` are. [source: https://api.stackexchange.com/2.3/tags/graphdb/info?site=stackoverflow]
- [inference] Memgraph and GraphDB may offer stronger commercial or support terms in direct sales conversations than in the public material consulted here, so their public ranking could improve in a procurement process even though their current self-serve evaluation posture is weaker. [source: https://memgraph.com/pricing; https://aws.amazon.com/marketplace/pp/prodview-rceq2ciyjdipy]

**Open questions:**

- Would a short proof-of-concept expose enough semantic value to justify Stardog's smaller labor market over Neo4j AuraDB's much broader skill pool?
- Is materialized inference, rather than query-time reasoning, strategically valuable enough to justify a deeper GraphDB procurement path?
- If the repository later needs both property-graph and semantic-graph workloads, would a two-system architecture still be cheaper and simpler than adopting Neptune as the single platform?
- What do direct vendor quotes for Stardog, Memgraph Enterprise, and GraphDB Enterprise look like for a pilot-sized workload under realistic support requirements?

### §7 Recursive Review

- Review result: pass
- Acronym audit: SaaS, TCO, RDF, OWL, SPARQL, SLA, JSON-LD, CSV, API, Amazon S3, IAM, Amazon EC2, VPC, SHACL, RDFS, W3C, JSONL, Multi-AZ checked and expanded on first use where they first appear in the document
- Claim audit: research-record claims labeled and source-bound
- Findings parity: section 6 synthesis and Findings kept aligned
- Cross-item audit: prior shortlist and schema items integrated, plus adjacent interoperability items cited in synthesis

---

## Findings

*(Populated from §6 Synthesis above.)*

### Executive Summary

Stardog Cloud is the best overall fit in the consulted evidence if this repository still requires semantic-web interoperability, ontology reasoning, and a managed pilot path in the same platform surface. [inference; source: https://www.stardog.com/stardog-cloud/; https://docs.stardog.com/query-stardog; https://www.stardog.com/platform/]

Neo4j AuraDB and Amazon Neptune are the most commercially transparent options, but they solve different problems: AuraDB is the low-friction property-graph choice, while Neptune is the AWS-native dual-model choice with higher operating complexity and less predictable small-team total cost of ownership. [inference; source: https://neo4j.com/pricing/; https://neo4j.com/docs/aura/classic/auradb/importing-data/; https://aws.amazon.com/neptune/pricing/; https://docs.aws.amazon.com/neptune/latest/userguide/access-graph-sparql.html; https://docs.aws.amazon.com/neptune/latest/userguide/access-graph-opencypher.html]

GraphDB remains technically credible for ontology-first work, but the accessible current evidence is more procurement-oriented and less self-serve than Stardog's, which weakens its ranking for a small repository pilot even though its standards support is strong. [inference; source: https://aws.amazon.com/marketplace/pp/prodview-rceq2ciyjdipy; https://davidamitchell.github.io/Research/research/2026-05-12-graph-db-saas-knowledge-ontology.html]

Neo4j has the clearest community and hiring advantage, so the final decision should be: choose Stardog if semantic interoperability is the real requirement, choose Neo4j AuraDB if that requirement softens, and choose Neptune only when AWS-native dual-model architecture is itself the governing constraint. [inference; source: https://graphacademy.neo4j.com/; https://graphacademy.neo4j.com/certifications/neo4j-certification/; https://community.neo4j.com/; https://api.stackexchange.com/2.3/tags/neo4j/info?site=stackoverflow; https://www.stardog.com/stardog-cloud/; https://aws.amazon.com/neptune/pricing/]

### Key Findings

1. **Stardog Cloud offers the strongest overall balance for this repository's ontology-first use case because it combines managed hosting, a free learning tier, explicit semantic-web standards support, published enterprise support tiers, and a 99.9 percent uptime commitment in one coherent platform surface.** ([inference]; medium confidence; source: https://www.stardog.com/stardog-cloud/; https://www.stardog.com/support/; https://docs.stardog.com/query-stardog; https://www.stardog.com/platform/)
2. **Neo4j AuraDB and Amazon Neptune provide the clearest public commercial transparency, but Neo4j's flat capacity pricing and low-friction import tooling make its small-team total cost of ownership easier to reason about than Neptune's instance, storage, input and output, backup, and surrounding-AWS billing model.** ([inference]; high confidence; source: https://neo4j.com/pricing/; https://neo4j.com/docs/aura/classic/auradb/importing-data/; https://aws.amazon.com/neptune/pricing/; https://docs.aws.amazon.com/neptune/latest/userguide/access-graph-sparql.html)
3. **GraphDB remains a technically strong ontology-first alternative because it exposes RDF, SPARQL, SHACL, RDFS, OWL, and RDF4J-compatible REST surfaces, but its accessible current commercial path looks more like enterprise marketplace procurement than an easily self-serve pilot service.** ([inference]; low confidence; source: https://aws.amazon.com/marketplace/pp/prodview-rceq2ciyjdipy; https://davidamitchell.github.io/Research/research/2026-05-12-graph-db-saas-knowledge-ontology.html)
4. **Amazon Neptune is the best conditional choice when the project needs both property-graph and semantic-graph support inside Amazon Web Services, but its higher operational overhead and more complex billing structure make it a weaker default recommendation for this repository than Stardog or Neo4j.** ([inference]; medium confidence; source: https://docs.aws.amazon.com/neptune/latest/userguide/access-graph-opencypher.html; https://docs.aws.amazon.com/neptune/latest/userguide/access-graph-sparql.html; https://aws.amazon.com/neptune/pricing/; https://aws.amazon.com/neptune/sla/)
5. **Neo4j has the deepest public community and hiring signal in the shortlist because it pairs formal certification, a large public forum, 23,056 Stack Overflow questions, and a public engineering surface that the other shortlisted products do not match in the consulted evidence.** ([inference]; high confidence; source: https://graphacademy.neo4j.com/; https://graphacademy.neo4j.com/certifications/neo4j-certification/; https://community.neo4j.com/; https://api.stackexchange.com/2.3/tags/neo4j/info?site=stackoverflow; https://github.com/neo4j/neo4j)
6. **Memgraph Cloud is attractive for Cypher-compatible prototyping and migration-heavy work because it offers fully managed hosting, simple memory-based pricing logic, and broad import options, but the consulted evidence does not support choosing it over Stardog, GraphDB, or Neptune for ontology-first interoperability.** ([inference]; medium confidence; source: https://memgraph.com/pricing; https://memgraph.com/docs/data-migration; https://memgraph.com/docs/client-libraries)
7. **Using a repository-weighted framework that prioritizes semantic interoperability over ecosystem depth, the recommended selection path is Stardog first, Neo4j AuraDB second as the non-semantic fallback, Neptune third for AWS-native dual-model requirements, GraphDB fourth as the procurement-heavier semantic alternative, and Memgraph fifth for this specific ontology-first decision.** ([inference]; medium confidence; source: https://www.stardog.com/stardog-cloud/; https://docs.stardog.com/query-stardog; https://neo4j.com/pricing/; https://aws.amazon.com/neptune/pricing/; https://aws.amazon.com/marketplace/pp/prodview-rceq2ciyjdipy; https://memgraph.com/pricing; https://davidamitchell.github.io/Research/research/2026-05-02-knowledge-graph-schema-cross-session-research-mcp.html)

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [inference] Stardog Cloud offers the strongest overall balance for this repository's ontology-first use case. | https://www.stardog.com/stardog-cloud/; https://www.stardog.com/support/; https://docs.stardog.com/query-stardog; https://www.stardog.com/platform/ | medium | Strong semantic fit, moderate ecosystem depth |
| [inference] Neo4j AuraDB has easier small-team total cost of ownership than Neptune despite similarly transparent public pricing. | https://neo4j.com/pricing/; https://neo4j.com/docs/aura/classic/auradb/importing-data/; https://aws.amazon.com/neptune/pricing/; https://docs.aws.amazon.com/neptune/latest/userguide/access-graph-sparql.html | high | Flat managed pricing versus multi-dimensional AWS billing |
| [inference] GraphDB is technically strong but commercially more procurement-heavy than Stardog for a pilot. | https://aws.amazon.com/marketplace/pp/prodview-rceq2ciyjdipy; https://davidamitchell.github.io/Research/research/2026-05-12-graph-db-saas-knowledge-ontology.html | low | Standards support is clear, commercial path is less self-serve |
| [inference] Neptune is best reserved for AWS-native dual-model requirements rather than used as the default platform here. | https://docs.aws.amazon.com/neptune/latest/userguide/access-graph-opencypher.html; https://docs.aws.amazon.com/neptune/latest/userguide/access-graph-sparql.html; https://aws.amazon.com/neptune/pricing/; https://aws.amazon.com/neptune/sla/ | medium | Strong hybrid-model fit, higher operating complexity |
| [inference] Neo4j has the deepest public community and hiring signal in the shortlist. | https://graphacademy.neo4j.com/; https://graphacademy.neo4j.com/certifications/neo4j-certification/; https://community.neo4j.com/; https://api.stackexchange.com/2.3/tags/neo4j/info?site=stackoverflow; https://github.com/neo4j/neo4j | high | Certification plus large public support surface |
| [inference] Memgraph is viable for Cypher migration work but not the leading ontology-first choice. | https://memgraph.com/pricing; https://memgraph.com/docs/data-migration; https://memgraph.com/docs/client-libraries | medium | Strong migration story, weak semantic standards story |
| [inference] The recommended selection order for this repository is Stardog, Neo4j AuraDB, Neptune, GraphDB, then Memgraph. | https://www.stardog.com/stardog-cloud/; https://neo4j.com/pricing/; https://aws.amazon.com/neptune/pricing/; https://aws.amazon.com/marketplace/pp/prodview-rceq2ciyjdipy; https://memgraph.com/pricing; https://davidamitchell.github.io/Research/research/2026-05-02-knowledge-graph-schema-cross-session-research-mcp.html | medium | Weighting favors semantic portability over labor-market depth |

### Assumptions

- The first production deployment remains small enough that procurement simplicity and operational burden matter more than extreme cluster scale. [assumption; source: https://github.com/davidamitchell/Research/blob/main/README.md; https://davidamitchell.github.io/Research/research/2026-05-02-knowledge-graph-schema-cross-session-research-mcp.html]
- Standards-based semantic interoperability remains a real project requirement rather than a merely aspirational preference, because otherwise Neo4j AuraDB would score first once ecosystem depth and self-serve transparency are weighted more heavily. [assumption; source: https://davidamitchell.github.io/Research/research/2026-05-12-graph-db-saas-knowledge-ontology.html; https://davidamitchell.github.io/Research/research/2026-05-12-web-ontologies-production-knowledge-graph-agentic.html]

### Analysis

The strongest rival explanation is that Neo4j AuraDB should win outright because commercial transparency, ecosystem depth, and hiring ease often dominate early adoption success for small teams. That explanation is credible and becomes decisive if ontology-first semantics stop being mandatory. [inference; source: https://neo4j.com/pricing/; https://graphacademy.neo4j.com/; https://graphacademy.neo4j.com/certifications/neo4j-certification/; https://community.neo4j.com/; https://api.stackexchange.com/2.3/tags/neo4j/info?site=stackoverflow]

Stardog still ranks first because the repository's own prior completed work makes semantic-web portability, ontology reasoning, and later interoperability with governance and metadata standards materially decision-relevant rather than optional. [inference; source: https://davidamitchell.github.io/Research/research/2026-05-12-graph-db-saas-knowledge-ontology.html; https://davidamitchell.github.io/Research/research/2026-05-12-data-product-ontology.html; https://davidamitchell.github.io/Research/research/2026-05-12-web-ontologies-production-knowledge-graph-agentic.html]

The weighting that produced the final order was 30 percent semantic interoperability, 25 percent commercial accessibility and spend predictability, 20 percent support and operational burden, 15 percent community and hiring depth, and 10 percent migration ease. Under those weights, Stardog beats Neo4j because semantic fit outweighs Neo4j's ecosystem advantage, while GraphDB loses to Stardog because its current commercial surface is less transparent. [inference; source: https://www.stardog.com/stardog-cloud/; https://www.stardog.com/support/; https://neo4j.com/pricing/; https://graphacademy.neo4j.com/; https://aws.amazon.com/marketplace/pp/prodview-rceq2ciyjdipy]

Neptune remains strategically important even though it ranks third, because it is the only clearly documented dual-model option in the consulted current evidence and therefore becomes the best path if the repository later insists on both SPARQL and property-graph workloads inside the same AWS-aligned platform. [inference; source: https://docs.aws.amazon.com/neptune/latest/userguide/access-graph-opencypher.html; https://docs.aws.amazon.com/neptune/latest/userguide/access-graph-sparql.html; https://aws.amazon.com/neptune/pricing/]

### Risks, Gaps, and Uncertainties

- GraphDB's precise commercial ranking is less certain than the other platforms because the accessible current evidence in this session came mainly from its AWS Marketplace surface rather than from a fully detailed self-serve pricing and support matrix. [inference; source: https://aws.amazon.com/marketplace/pp/prodview-rceq2ciyjdipy]
- The interoperability comparison for Java frameworks, Protégé, Apache Jena, LangChain, and LlamaIndex remains uneven because the consulted official materials did not document those adjacent-tool integrations symmetrically across all five platforms. [inference; source: https://docs.stardog.com/query-stardog; https://docs.aws.amazon.com/neptune/latest/userguide/access-graph-sparql.html; https://neo4j.com/docs/python-manual/current/; https://memgraph.com/docs/client-libraries; https://aws.amazon.com/marketplace/pp/prodview-rceq2ciyjdipy]
- The `graphdb` Stack Overflow tag is generic, so it is not a clean Ontotext-only ecosystem proxy in the way that `neo4j`, `amazon-neptune`, `stardog`, and `memgraph` are. [fact; source: https://api.stackexchange.com/2.3/tags/graphdb/info?site=stackoverflow]
- Memgraph and GraphDB may offer stronger commercial or support terms in direct sales conversations than in the public material consulted here, so their public ranking could improve in a procurement process even though their current self-serve evaluation posture is weaker. [inference; source: https://memgraph.com/pricing; https://aws.amazon.com/marketplace/pp/prodview-rceq2ciyjdipy]

### Open Questions

- Would a short proof-of-concept expose enough semantic value to justify Stardog's smaller labor market over Neo4j AuraDB's much broader skill pool?
- Is materialized inference, rather than query-time reasoning, strategically valuable enough to justify a deeper GraphDB procurement path?
- If the repository later needs both property-graph and semantic-graph workloads, would a two-system architecture still be cheaper and simpler than adopting Neptune as the single platform?
- What do direct vendor quotes for Stardog, Memgraph Enterprise, and GraphDB Enterprise look like for a pilot-sized workload under realistic support requirements?

---

## Output

- Type: knowledge
- Description: A weighted commercial and interoperability comparison of the shortlisted hosted graph platforms, concluding that Stardog is the best ontology-first fit for this repository, Neo4j AuraDB is the best non-semantic fallback, and Neptune is the best AWS-native dual-model option. [inference; source: https://www.stardog.com/stardog-cloud/; https://neo4j.com/pricing/; https://aws.amazon.com/neptune/pricing/]
- Links:
  - https://www.stardog.com/stardog-cloud/
  - https://neo4j.com/pricing/
  - https://aws.amazon.com/neptune/pricing/
