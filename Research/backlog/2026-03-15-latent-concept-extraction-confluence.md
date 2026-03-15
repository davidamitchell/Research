---
title: "Latent Concept Extraction from Confluence: Embeddings, Knowledge Graphs, and Epistemic Evaluation"
added: 2026-03-15
status: backlog  # backlog | in-progress | reviewing | completed
priority: high  # low | medium | high
blocks: []  # slugs (filename without .md) of backlog items that cannot start until this one is complete
tags: [confluence, embeddings, vector-db, knowledge-graph, nlp, epistemics, rag, latent-concepts]
started: ~
completed: ~
output: [knowledge]
---

# Latent Concept Extraction from Confluence: Embeddings, Knowledge Graphs, and Epistemic Evaluation

## Research Question

What are the best approaches for extracting latent concepts from a Confluence wiki, representing them as word embeddings in a vector database (VDB) and as a knowledge graph, and how can the resulting knowledge base be evaluated for truth and utility — and is there a meaningful distinction between the two?

## Scope

**In scope:**
- Techniques for latent concept extraction from unstructured and semi-structured wiki content (Confluence pages, page hierarchies, labels, links)
- Word embedding models suitable for technical/organisational knowledge: dense retrieval encoders (e.g. sentence-transformers), sparse models (BM25, SPLADE), and hybrid approaches
- Vector database (VDB) options for storing and querying embeddings at wiki scale: Qdrant, Weaviate, Chroma, pgvector
- Knowledge graph construction from extracted concepts: entity recognition, relation extraction, and graph schema design (e.g. RDF, property graphs)
- Epistemics of a knowledge base: what does it mean for a claim to be "true" in this context vs. merely "useful", and practical methods for capturing confidence, provenance, and recency metadata
- Retrieval-Augmented Generation (RAG) as the primary downstream consumer of the resulting knowledge store

**Out of scope:**
- Full implementation or deployment guide (this is a research item, not an engineering spec)
- Confluence-specific API authentication mechanics (assume API access is available)
- Deep coverage of graph query languages (Cypher, SPARQL) beyond their relevance to retrieval

**Constraints:** Publicly available papers, blog posts, open-source repositories, and documentation accessible without paywalls or institutional login.

## Context

A Confluence wiki is a dense organisational knowledge store, but its value is locked in unstructured prose. Extracting latent concepts — implicit topics, entities, relationships — and storing them in a queryable form (VDB + knowledge graph) enables downstream uses: semantic search, question-answering agents, automated gap analysis, and knowledge auditing. The epistemics question is the hardest part: once concepts are extracted and indexed, the system needs a principled way to distinguish claims that are factually grounded from claims that are merely operationally useful. This distinction matters when the knowledge base is used to answer questions or drive automated decisions.

## Approach

1. Survey latent concept extraction techniques for wiki-scale text: topic modelling (Latent Dirichlet Allocation (LDA), BERTopic), named entity recognition (NER), and implicit relation extraction — what works at the scale and style of a Confluence wiki?
2. Evaluate embedding strategies: which sentence-transformer or domain-adapted models produce the most coherent concept clusters for technical organisational prose?
3. Map the embedding pipeline: chunking strategy → embedding model → VDB schema → retrieval query design.
4. Survey knowledge graph construction from the same source material: how are entities and relations extracted, what graph schema is appropriate, and how does the graph complement (rather than duplicate) the VDB?
5. Investigate the epistemics question: what frameworks exist for scoring claim "truth" (factual accuracy, source provenance, recency) vs. "utility" (relevance to a task, adoption frequency, operational impact) — and is the distinction philosophically and practically meaningful in an organisational knowledge base?
6. Synthesise a recommended architecture: extraction pipeline → VDB → knowledge graph → RAG consumer, with explicit handling of epistemic metadata.

## Sources

- [ ] BERTopic paper and documentation: https://maartengr.github.io/BERTopic/
- [ ] Sentence-Transformers library: https://www.sbert.net/
- [ ] Qdrant documentation: https://qdrant.tech/documentation/
- [ ] LangChain / LlamaIndex knowledge graph integration guides
- [ ] "From Documents to Knowledge Graphs" — survey papers on information extraction pipelines
- [ ] Atlassian Confluence REST API documentation: https://developer.atlassian.com/cloud/confluence/rest/v2/
- [ ] RAG survey: "Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks" (Lewis et al., 2020)
- [ ] Epistemic frameworks: "Veritistic value" (Goldman) vs. pragmatic theories of truth — introductory survey

---

## Research Skill Output

*(Full output from running the research skill — retained verbatim in the completed item. §§0–5 are the investigation; §6 seeds the Findings section below.)*

### §0 Initialise

Restate the research question. Confirm scope, constraints, and output format.

-

### §1 Question Decomposition

Approach sub-questions broken into atomic questions — each answerable with a single evidence-based claim.

-

### §2 Investigation

Evidence gathered per atomic question. Label each claim: **[fact]**, **[inference]**, or **[assumption]** with source.

-

### §3 Reasoning

Facts, inferences, and assumptions explicitly separated. No unsupported generalisations or narrative leaps.

-

### §4 Consistency Check

Internal contradictions identified and resolved (or explicitly flagged where unresolvable).

-

### §5 Depth and Breadth Expansion

Findings re-examined through relevant lenses (technical, regulatory, economic, historical, behavioural).

-

### §6 Synthesis

*(This section seeds the Findings below.)*

**Executive summary:**

**Key findings:**

**Evidence map:**

**Assumptions:**

**Analysis:**

**Risks, gaps, uncertainties:**

**Open questions:**

### §7 Recursive Review

Final pass: every section justified, all threads synthesised, every claim sourced or labelled, all uncertainties explicit.

-

---

## Findings

*(Populated from §6 Synthesis above.)*

### Executive Summary

3–5 sentences. What is the answer to the research question? State the key conclusion directly.

### Key Findings

Ordered list. Each finding is a specific, evidence-backed claim.

1.
2.

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| | | high / medium / low | |

### Assumptions

Explicit assumptions made during the investigation and the justification for each.

- **Assumption:** ... **Justification:** ...

### Analysis

How the evidence was weighed, what trade-offs were identified, and how competing interpretations were resolved.

### Risks, Gaps, and Uncertainties

What is still unknown? Where does the evidence fall short? What could change the conclusion?

-

### Open Questions

Questions that surfaced during research but are out of scope for this item. Each may become a new backlog item.

-

---

## Output

*(Fill in when completing — what was produced as a result of this research?)*

- Type: knowledge
- Description:
- Links:
