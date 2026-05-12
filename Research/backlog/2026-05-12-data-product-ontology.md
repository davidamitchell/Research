---
title: "Data product ontology: definition, adoption, and current relevance"
added: 2026-05-12T08:17:21+00:00
status: backlog
priority: medium
blocks: []
tags: [knowledge-graph, governance, data-product]
started: ~
completed: ~
output: []
cites: []
related: []
superseded_by: ~
supersedes: ~
item_type: primary
confidence: medium
versions: []
---

# Data product ontology: definition, adoption, and current relevance

## Research Question

What is the data product ontology, which organisations and communities use it, how is it applied in practice within data mesh and data management architectures, and is it still current relative to competing and complementary standards?

## Scope

**In scope:**
- Definition and structure of the data product ontology — its core classes, properties, and design intent
- Known implementations: the Data Product Vocabulary (DPROD) from the Semantic Interoperability Community (SEMIC) / W3C community group, and any related academic or industry-produced ontologies
- Adopters: organisations, vendors, and standards bodies that reference or implement the ontology
- Usage patterns: how the ontology is applied (tooling, catalogues, data contracts, data mesh governance)
- Currency: date of last substantive update, maintenance status, and community activity level
- Related standards and vocabularies: Data Catalog Vocabulary (DCAT), Data Privacy Vocabulary (DPV), schema.org Dataset, Open Data Model (ODM), and relevant ISO/IEC standards (e.g. ISO 8000)
- Comparison: where the data product ontology overlaps with or defers to related standards

**Out of scope:**
- General data mesh architecture (except as context for ontology adoption)
- Implementation of a specific data product ontology in this repository
- Vendor-proprietary data product schemas not grounded in a public ontology
- Full tutorial on ontology languages (Resource Description Framework (RDF), Web Ontology Language (OWL), SPARQL)

**Constraints:**
- Sources must be publicly accessible documentation, standards bodies, peer-reviewed papers, or independently authored technical articles — no vendor marketing-only sources
- Assess currency as of 2024–2026; flag any sources older than three years

## Context

Data products have become a central concept in data mesh architectures and modern data governance. Several groups have attempted to formalise the concept as a machine-readable ontology or vocabulary to enable interoperability between data catalogues, marketplaces, and governance tools. Before adopting or referencing such an ontology in any tooling, it is important to understand which ontology is canonical (if any), who maintains it, and whether it has achieved meaningful industry adoption or been superseded by later work.

## Approach

1. Identify candidate data product ontologies and vocabularies — starting with DPROD (SEMIC/W3C), any W3C Working Group or Community Group outputs, and relevant academic literature from 2020–2026.
2. For each candidate, document: scope, core classes and properties, formal status (draft, published, deprecated), and the publishing body or author.
3. Establish which organisations and communities have adopted each — look for references in catalogue tools (e.g. Apache Atlas, DataHub, OpenMetadata, Collibra), data mesh publications, and conference proceedings.
4. Document usage patterns: how is the ontology used in practice — data contract definition, lineage, catalogue interoperability, policy enforcement?
5. Assess currency: when was each ontology last meaningfully updated? Is the community actively maintaining it? Are there open issues or active Working Groups?
6. Map relationships to adjacent standards: DCAT-3, Data Privacy Vocabulary (DPV), schema.org Dataset, ISO 8000 (Data Quality), FAIR Data Principles, and any relevant Object Management Group (OMG) standards.
7. Synthesise a verdict: which data product ontology, if any, has achieved consensus adoption; which is most current; and what are the realistic alternatives if none has achieved critical mass?

## Sources

- [ ] [DPROD — Data Product Vocabulary (W3C Community Group)](https://ekgf.github.io/dprod/) — primary W3C community group specification for data product vocabulary
- [ ] [SEMIC Data Product Vocabulary GitHub repository](https://github.com/SEMICeu/DPROD) — source repository and issue tracker for the DPROD specification
- [ ] [W3C DCAT-3 specification](https://www.w3.org/TR/vocab-dcat-3/) — Data Catalog Vocabulary (DCAT) version 3; closely related to data product description
- [ ] [Data Mesh by Zhamak Dehghani (O'Reilly, 2022)](https://www.oreilly.com/library/view/data-mesh/9781492092384/) — foundational data mesh text that motivates the data product concept
- [ ] [FAIR Data Principles](https://www.go-fair.org/fair-principles/) — Findable, Accessible, Interoperable, Reusable (FAIR) principles; context for interoperability requirements
- [ ] [ISO 8000 Data Quality standard overview](https://www.iso.org/standard/81745.html) — ISO standard for data quality; relevant as a complementary governance standard

---

## Research Skill Output

*(Full output from running the research skill — retained verbatim in the completed item. §§0–5 are the investigation; §6 seeds the Findings section below.)*

### §0 Initialise

-

### §1 Question Decomposition

-

### §2 Investigation

-

### §3 Reasoning

-

### §4 Consistency Check

-

### §5 Depth and Breadth Expansion

-

### §6 Synthesis

**Executive summary:**

**Key findings:**

**Evidence map:**

**Assumptions:**

**Analysis:**

**Risks, gaps, uncertainties:**

**Open questions:**

### §7 Recursive Review

-

---

## Findings

*(Populated from §6 Synthesis above.)*

### Executive Summary

### Key Findings

1.
2.

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| | | high / medium / low | |

### Assumptions

- **Assumption:** ... **Justification:** ...

### Analysis

### Risks, Gaps, and Uncertainties

-

### Open Questions

-

---

## Output

*(Fill in when completing — what was produced as a result of this research?)*

- Type: # skill | tool | agent | knowledge | backlog-item
- Description:
- Links:
