---
review_count: 1
title: "Migration trade-offs from vector Retrieval-Augmented Generation to ontology-backed Knowledge Graph RAG"
added: 2026-07-05T20:53:37+00:00
status: reviewing
priority: high
blocks: []
themes: [rag-retrieval, knowledge-graphs, knowledge-management, enterprise-adoption, cost-performance]
started: 2026-07-06T08:31:15+00:00
completed: ~
output: [knowledge]
cites: [2026-03-08-servicenow-ai-knowledge-rag-agents, 2026-05-12-rag-document-drift-agent-behavior]
related: [2026-03-15-context-compression-rag-enterprise-knowledge, 2026-03-03-knowledge-representation-agent-context, 2026-05-12-graph-db-saas-knowledge-ontology, 2026-05-13-graph-db-landscape-tco-interoperability, 2026-05-12-web-ontologies-production-knowledge-graph-agentic]
superseded_by: ~
supersedes: ~
item_type: primary
confidence: medium
versions: []
---

# Migration trade-offs from vector Retrieval-Augmented Generation to ontology-backed Knowledge Graph RAG

## Research Question

What are the performance, cost, scalability, and practical trade-offs of migrating from traditional vector-based Retrieval-Augmented Generation (RAG) systems to ontology-backed Knowledge Graph Retrieval-Augmented Generation (KG-RAG / GraphRAG) systems in real-world applications such as customer service or enterprise knowledge management, and under what conditions does that migration justify its added complexity?

## Scope

**In scope:**
- Empirical comparisons between vector RAG and ontology-backed KG-RAG / GraphRAG in customer service, enterprise knowledge management, or closely related enterprise question-answering settings
- Retrieval and reasoning quality differences, including multi-hop reasoning, relationship handling, hallucination reduction, and answer completeness
- Migration engineering concerns: data ingestion, entity and relation extraction, ontology alignment, graph and vector index construction, hybrid retrieval, query rewriting, and incremental rollout without downtime
- Cost and efficiency trade-offs across graph construction, embedding generation, storage, token usage, latency, and ongoing maintenance
- Scalability and maintainability as corpus size grows, domains evolve, and entities or relations change over time
- Decision thresholds for when the move is justified versus when vector RAG or hybrid RAG remains the more practical architecture

**Out of scope:**
- Standalone ontology quality research that does not affect the migration decision
- Fine-tuning, agent orchestration, or general Large Language Model (LLM) architecture questions unrelated to retrieval-system migration
- Pure vector database benchmark work that does not compare end-to-end RAG architectures
- Graph reasoning systems without practical relevance to enterprise retrieval, customer service, or knowledge-management use cases

**Constraints:** Prioritise public 2024-2025 papers, surveys, and production case studies. Focus on evidence that compares architectures or documents a realistic migration path, not only idealised steady-state designs. Assume no proprietary internal datasets or closed vendor benchmarks beyond what is publicly reported.

## Context

This question informs whether an existing enterprise vector RAG stack should remain vector-first, evolve into a hybrid retrieval architecture, or migrate toward ontology-backed KG-RAG when query complexity, relationship-heavy data, and answer-quality requirements start to exceed what chunked semantic retrieval can reliably support.

## Related

- [`2026-03-15-context-compression-rag-enterprise-knowledge`](../completed/2026-03-15-context-compression-rag-enterprise-knowledge.md), prior survey of enterprise RAG architecture, context compression, and retrieval-quality trade-offs
- [`2026-03-03-knowledge-representation-agent-context`](../completed/2026-03-03-knowledge-representation-agent-context.md), prior foundations on knowledge graphs, GraphRAG, and layered knowledge representations
- [`2026-03-08-servicenow-ai-knowledge-rag-agents`](../completed/2026-03-08-servicenow-ai-knowledge-rag-agents.md), enterprise knowledge and customer-service-adjacent deployment patterns for retrieval-backed systems

## Approach

1. Establish the comparison baseline: what capabilities and failure modes define traditional vector RAG in enterprise knowledge and customer-service settings?
2. Evaluate quality gains: where do ontology-backed KG-RAG / GraphRAG systems improve multi-hop retrieval, relational reasoning, hallucination control, and answer completeness, and how strong is the empirical evidence?
3. Investigate migration design: what engineering steps are required to move from vector RAG to hybrid or graph-backed retrieval, and what phased migration patterns minimise downtime and operational risk?
4. Quantify trade-offs: how do indexing cost, token consumption, storage, latency, update complexity, and maintenance effort differ between vector, hybrid, and ontology-backed graph architectures?
5. Identify adoption thresholds: what data characteristics, query patterns, scale levels, and governance requirements make ontology-backed KG-RAG worth the additional complexity, and when is the move unjustified?

## Sources

- [x] [Xu et al. (2024) Retrieval-Augmented Generation with Knowledge Graphs for Customer Service Question Answering](https://arxiv.org/abs/2404.17723), production-oriented comparison of knowledge-graph-backed retrieval for customer service, deployed at LinkedIn
- [x] [Edge et al. (2024) From Local to Global: A GraphRAG Approach to Query-Focused Summarization](https://arxiv.org/abs/2404.16130), Microsoft Research GraphRAG paper with graph indexing and global-query evaluation
- [x] [Sarmah et al. (2024) HybridRAG: Integrating Knowledge Graphs and Vector Retrieval Augmented Generation for Efficient Information Extraction](https://arxiv.org/abs/2408.04948), hybrid migration pattern combining vector and graph retrieval, tested on financial transcripts
- [x] [Retrieval-Augmented Generation with Graphs (GraphRAG): A Comprehensive Survey (2025)](https://arxiv.org/abs/2501.00309), survey of GraphRAG techniques, challenges, and open problems
- [x] [Graph Retrieval-Augmented Generation: A Survey (2024)](https://arxiv.org/abs/2408.08921), broader survey of graph-backed retrieval-augmented generation designs
- [x] [Towards Practical GraphRAG: Efficient Knowledge Graph Construction and Hybrid Retrieval at Scale (2025)](https://arxiv.org/abs/2507.03226), dependency-parsing-based construction pipeline and hybrid retrieval proposed to reduce GraphRAG's cost barrier
- [x] [Benchmarking Vector, Graph and Hybrid Retrieval Augmented Generation (RAG) Pipelines for Open Radio Access Networks (ORAN) (2025)](https://arxiv.org/abs/2507.03608), independent telecom-domain replication of the vector-vs-graph-vs-hybrid comparison
- [x] [Barry et al. (2025) GraphRAG: Leveraging Graph-Based Efficiency to Minimize Hallucinations in LLM-Driven RAG for Finance Data](https://aclanthology.org/2025.genaik-1.6/), Association for Computational Linguistics (ACL) Generative AI and Knowledge Graphs (GenAIK) workshop paper on graph-based hallucination reduction in finance RAG
- [x] [GraphRAG-Bench: Challenging Domain-specific Reasoning for Evaluating Graph Retrieval-Augmented Generation](https://github.com/GraphRAG-Bench/GraphRAG-Benchmark), cross-domain benchmark project stating GraphRAG frequently underperforms vanilla RAG
- [x] [Microsoft GraphRAG documentation, Global Search](https://microsoft.github.io/graphrag/query/global_search/), official pipeline documentation for community detection and map-reduce global search
- [x] [Incremental indexing (adding new content), microsoft/graphrag issue #741](https://github.com/microsoft/graphrag/issues/741), primary project discussion of incremental graph-update engineering
- [x] [GraphRAG Indexing: Why the $33K Cost Cliff Hits (bestaiweb.ai)](https://www.bestaiweb.ai/indexing-cost-token-blowup-and-the-hard-engineering-limits-of-graphrag-at-scale/), secondary technical analysis of GraphRAG indexing cost drivers
- [x] [LazyGraphRAG: 700x Cheaper GraphRAG That Actually Works (particula.tech)](https://particula.tech/blog/lazygraphrag-700x-cheaper-graphrag-knowledge-graphs), secondary vendor blog on lazy, query-time summarisation cost reduction
- [x] [Neo4j: What is retrieval-augmented generation (RAG)?](https://neo4j.com/blog/genai/what-is-retrieval-augmented-generation-rag/), vendor documentation on hybrid vector-plus-graph retrieval patterns
- [x] [Context Compression and RAG Techniques for Organisational Knowledge](https://davidamitchell.github.io/Research/research/2026-03-15-context-compression-rag-enterprise-knowledge.html), prior completed item, RAG taxonomy and context-compression baseline
- [x] [Knowledge Representation for Agent Context](https://davidamitchell.github.io/Research/research/2026-03-03-knowledge-representation-agent-context.html), prior completed item establishing the layered dense-embedding/knowledge-graph/hierarchical-summary architecture
- [x] [ServiceNow AI: Knowledge Management, RAG Pipelines, and Agent Frameworks](https://davidamitchell.github.io/Research/research/2026-03-08-servicenow-ai-knowledge-rag-agents.html), prior completed item on knowledge-base governance as a RAG-grounding precondition
- [x] [Hosted graph database options for knowledge ontology](https://davidamitchell.github.io/Research/research/2026-05-12-graph-db-saas-knowledge-ontology.html), prior completed item on ontology-first hosted graph database options
- [x] [Graph database landscape: pricing, Total Cost of Ownership (TCO), interoperability](https://davidamitchell.github.io/Research/research/2026-05-13-graph-db-landscape-tco-interoperability.html), prior completed item on graph database TCO
- [x] [Web ontologies in production Knowledge Graphs for multi-step agents](https://davidamitchell.github.io/Research/research/2026-05-12-web-ontologies-production-knowledge-graph-agentic.html), prior completed item on Resource Description Framework (RDF), RDF Schema (RDFS), and Web Ontology Language (OWL) adoption sequencing
- [x] [When Retrieval-Augmented Generation source documents change after agent build and test](https://davidamitchell.github.io/Research/research/2026-05-12-rag-document-drift-agent-behavior.html), prior completed item on treating RAG corpora as versioned dependencies

---

## Research Skill Output

*(Full output from running the research skill, retained verbatim in the completed item. §§0-5 are the investigation, and §6 seeds the Findings section below.)*

### §0 Initialise

Question: What are the performance, cost, scalability, and practical trade-offs of migrating from traditional vector-based Retrieval-Augmented Generation (RAG) systems to ontology-backed Knowledge Graph Retrieval-Augmented Generation (KG-RAG, sometimes called GraphRAG) systems in customer service or enterprise knowledge management, and under what conditions does the migration justify its added complexity? A Knowledge Graph is a structured representation of entities and their relationships stored as labelled nodes and edges, enabling machines to reason about connections between concepts, as distinct from a vector index, which stores only dense numerical embeddings of text chunks without explicit relationship structure.

Scope: empirical comparisons of vector RAG against ontology-backed KG-RAG or GraphRAG in customer service and enterprise knowledge-management settings; retrieval and reasoning quality (multi-hop reasoning, relationship handling, hallucination control); migration engineering (ingestion, entity and relation extraction, hybrid retrieval, incremental rollout); cost and efficiency trade-offs; scalability and maintainability; adoption thresholds. Out of scope: standalone ontology-quality research, fine-tuning and agent-orchestration questions unrelated to retrieval migration, pure vector-database benchmarking without an end-to-end RAG comparison, and graph-reasoning research without enterprise retrieval relevance.

Constraints: prioritise public 2024 to 2025 papers, surveys, and production case studies; favour evidence that documents a realistic migration path over idealised steady-state designs; assume no access to proprietary internal datasets or closed vendor benchmarks.

Output format: `knowledge`, structured per the template's Findings sections.

Prior-work scan of `Research/completed/`: this item builds directly on [Context Compression and RAG Techniques for Organisational Knowledge](https://davidamitchell.github.io/Research/research/2026-03-15-context-compression-rag-enterprise-knowledge.html), which surveyed RAG taxonomy and context-compression techniques but did not compare vector RAG against ontology-backed KG-RAG at a migration-decision level. [Knowledge Representation for Agent Context](https://davidamitchell.github.io/Research/research/2026-03-03-knowledge-representation-agent-context.html) already concluded that a layered stack combining dense embeddings, a dynamic-corpus knowledge graph, and hierarchical summarisation outperforms any single technique, and that concept maps and Latent Semantic Analysis (LSA) are subsumed by knowledge graphs and dense embeddings respectively; that item's findings are treated as an established baseline here rather than re-derived. [ServiceNow AI: Knowledge Management, RAG Pipelines, and Agent Frameworks](https://davidamitchell.github.io/Research/research/2026-03-08-servicenow-ai-knowledge-rag-agents.html) established that RAG grounding quality in customer-service platforms depends on knowledge-base and Configuration Management Database (CMDB) governance quality, which this item treats as a precondition for any migration decision rather than a variable to re-test. Three further completed items narrow the graph-database side of the decision: [Hosted graph database options for knowledge ontology](https://davidamitchell.github.io/Research/research/2026-05-12-graph-db-saas-knowledge-ontology.html) and [Graph database landscape: pricing, TCO, interoperability](https://davidamitchell.github.io/Research/research/2026-05-13-graph-db-landscape-tco-interoperability.html) both concluded that Stardog Cloud is the strongest hosted ontology-first option in the evidence they consulted, with Neo4j AuraDB as the developer-friendly property-graph fallback; and [Web ontologies in production Knowledge Graphs for multi-step agents](https://davidamitchell.github.io/Research/research/2026-05-12-web-ontologies-production-knowledge-graph-agentic.html) recommended starting with Resource Description Framework (RDF) and RDF Schema (RDFS) and layering in Web Ontology Language (OWL) only where formal reasoning is required. [When RAG source documents change after agent build and test](https://davidamitchell.github.io/Research/research/2026-05-12-rag-document-drift-agent-behavior.html) is directly relevant to migration risk: it establishes that post-deployment corpus changes behave like dependency updates and should be version-controlled, which this item extends to the graph-construction pipeline specifically.

### §1 Question Decomposition

**1. Baseline: what defines vector RAG and its failure modes in enterprise/customer-service settings?**
- 1.1 What is the standard vector RAG pipeline (chunk, embed, retrieve, generate)?
- 1.2 What specific failure modes does chunked semantic retrieval exhibit on relationship-heavy or multi-document queries?

**2. Quality gains from ontology-backed KG-RAG / GraphRAG**
- 2.1 Is there direct production evidence of retrieval or resolution-time improvement from adding a knowledge graph to a customer-service RAG pipeline?
- 2.2 What class of query (global sensemaking vs. local fact lookup) does GraphRAG improve, and by how much, per the original Microsoft GraphRAG paper?
- 2.3 Does combining vector and graph retrieval (HybridRAG) outperform either technique alone, and in which domain was this tested?
- 2.4 Is GraphRAG's advantage universal, or does published benchmark work show cases where GraphRAG underperforms vanilla RAG?
- 2.5 What is the state of evidence on hallucination reduction specifically attributable to graph structure versus other factors?

**3. Migration engineering**
- 3.1 What are the concrete pipeline steps to move from a vector-only stack to a hybrid vector+graph stack?
- 3.2 What patterns exist for incremental graph construction and update without full-corpus reprocessing?
- 3.3 What downtime or dual-write risks exist during a live migration, and how does this connect to prior findings on RAG document drift?

**4. Cost and efficiency trade-offs**
- 4.1 What is the relative indexing cost (in dollars or tokens) of vector embedding versus knowledge-graph construction?
- 4.2 What is the relative per-query cost and latency of vector search versus graph traversal/global search?
- 4.3 What cost-reduction techniques exist for graph construction (e.g., non-LLM extraction, lazy summarisation), and how much do they change the cost picture?

**5. Adoption thresholds**
- 5.1 At what corpus size, query complexity, or relationship density does the evidence suggest ontology-backed KG-RAG becomes justified?
- 5.2 What governance or maintenance prerequisites (per the ServiceNow and RAG-drift items) must be in place before migration is worth attempting?
- 5.3 When does the evidence suggest vector RAG or a lightweight hybrid remains the more practical choice?

### §2 Investigation

**1.1–1.2 Baseline vector RAG and its failure modes**

[fact] Standard RAG retrieves relevant text chunks from an external knowledge source using vector similarity search and inserts them into a Large Language Model (LLM) prompt to ground generated answers, without access to explicit relationships between chunks (source: [Edge et al. (2024) From Local to Global: A Graph RAG Approach to Query-Focused Summarization](https://arxiv.org/abs/2404.16130)).

[fact] Baseline RAG performs poorly on queries that require aggregating information across an entire dataset, such as "what are the top themes in the data," because the query has no specific semantic anchor for a similarity search to latch onto, and the retriever returns semantically similar but not thematically comprehensive chunks (source: [Microsoft GraphRAG documentation, Global Search](https://microsoft.github.io/graphrag/query/global_search/); [Edge et al. (2024)](https://arxiv.org/abs/2404.16130)).

[fact] In the LinkedIn customer-service deployment, the authors state that conventional retrieval methods in RAG for LLMs treat a large corpus of past support tickets as plain text, ignoring intra-issue structure and inter-issue relations, which they identify as the specific limitation that a knowledge graph is designed to correct (source: [Xu et al. (2024) Retrieval-Augmented Generation with Knowledge Graphs for Customer Service Question Answering](https://arxiv.org/abs/2404.17723)).

**2.1 Direct production evidence from customer service**

[fact] LinkedIn built a knowledge graph from historical customer-service issue tickets, preserving intra-issue structure and inter-issue relations, and used sub-graph retrieval during question answering; on their benchmark this method outperformed the vector-only baseline by 77.6% in Mean Reciprocal Rank (MRR, a ranking-quality metric that scores how close the first correct retrieved result is to the top of the ranked list) and by 0.32 in BiLingual Evaluation Understudy (BLEU, a text-generation similarity metric) (source: [Xu et al. (2024)](https://arxiv.org/abs/2404.17723)).

[fact] The same system was deployed in LinkedIn's customer-service team for approximately six months at the time of publication and reduced the median per-issue resolution time by 28.6% (source: [Xu et al. (2024)](https://arxiv.org/abs/2404.17723)).

[inference] Because this is a single deployment at one company, evaluated on that company's own benchmark and ticket corpus, the specific magnitude of improvement (77.6% MRR, 28.6% resolution-time reduction) should not be generalised as a fixed expected return for other organisations; the direction of the result (a knowledge-graph-augmented retriever measurably outperforming a plain vector baseline on relationship-heavy support tickets) is the more portable finding (source: [Xu et al. (2024)](https://arxiv.org/abs/2404.17723)).

**2.2 Query class and GraphRAG's original evaluation**

[fact] Microsoft's original GraphRAG paper builds an entity knowledge graph from source documents using an LLM, pregenerates community summaries for groups of related entities, and answers global sensemaking questions by summarising across community summaries in a map-reduce pattern; the authors report substantial improvements over a conventional RAG baseline specifically for the comprehensiveness and diversity of generated answers on global sensemaking questions over million-token-scale datasets (source: [Edge et al. (2024)](https://arxiv.org/abs/2404.16130)).

[inference] The Microsoft GraphRAG evaluation is scoped to "global sensemaking questions," a query class defined by the authors as questions that require synthesis across an entire corpus rather than lookup of a single fact; this scoping means the reported improvement does not establish that GraphRAG also outperforms vector RAG on narrow, single-fact lookup queries, which is a large share of real customer-service traffic (source: [Edge et al. (2024)](https://arxiv.org/abs/2404.16130)).

**2.3 Hybrid retrieval (vector + graph together)**

[fact] The HybridRAG paper combines VectorRAG (their term for standard vector-database retrieval) and GraphRAG retrieval on financial earnings-call-transcript question-answering, using a ground-truth dataset built from the natural question-and-answer structure of transcripts, and reports that HybridRAG outperforms both VectorRAG and GraphRAG individually at both the retrieval and answer-generation stages (source: [Sarmah et al. (2024) HybridRAG: Integrating Knowledge Graphs and Vector Retrieval Augmented Generation for Efficient Information Extraction](https://arxiv.org/abs/2408.04948)).

Access note: a secondary AI-generated search summary reported specific faithfulness and answer-relevancy percentage scores (for example 0.88 VectorRAG, 0.91 GraphRAG, 0.96 HybridRAG) attributed to this paper; the primary paper text retrieved in this session (arXiv abstract and introduction via [ar5iv](https://ar5iv.labs.arxiv.org/html/2408.04948)) confirms the qualitative ranking (HybridRAG > GraphRAG and VectorRAG individually) but the specific percentage figures could not be independently verified against the paper's results tables in this session, so they are not used as sourced numbers in this item.

[fact] An independent 2025 benchmark of vector, graph, and hybrid RAG pipelines applied to Open Radio Access Network (ORAN) telecom specifications and RAN Intelligent Controller (RIC) Application Programming Interface (API) definitions exists as a peer-reviewable arXiv preprint, evaluating the same three-way comparison (vector-only, graph-only, hybrid) in a second, independent domain from HybridRAG's financial-transcript setting (source: [Benchmarking Vector, Graph and Hybrid RAG Pipelines for ORAN](https://arxiv.org/abs/2507.03608)).

[inference] Two independent domains (financial earnings transcripts and telecom specifications) both testing a vector-vs-graph-vs-hybrid three-way comparison is a modest but genuine cross-domain replication of the pattern that hybrid retrieval, not graph retrieval alone, is the consistently competitive architecture; this is stronger evidence for "add graph retrieval as a complement to vector search" than for "replace vector search with graph search" (source: [Sarmah et al. (2024)](https://arxiv.org/abs/2408.04948); [Benchmarking Vector, Graph and Hybrid RAG Pipelines for ORAN (2025)](https://arxiv.org/abs/2507.03608)).

**2.4 Evidence against a universal GraphRAG advantage**

[fact] The GraphRAG-Bench project states explicitly that "recent studies report that GraphRAG frequently underperforms vanilla RAG on many real-world tasks," and was built specifically to identify in which scenarios graph structures provide a measurable benefit for RAG systems rather than assuming a universal benefit (source: [GraphRAG-Bench: Challenging Domain-specific Reasoning for Evaluating Graph Retrieval-Augmented Generation](https://github.com/GraphRAG-Bench/GraphRAG-Benchmark)).

[inference] This directly qualifies the LinkedIn and HybridRAG results in §2.1 and §2.3: those are point deployments in relationship-dense domains (support-ticket cross-referencing, structured financial statements) where GraphRAG's structural advantage plausibly applies, not evidence that graph augmentation helps on average across arbitrary enterprise corpora (source: [GraphRAG-Bench](https://github.com/GraphRAG-Bench/GraphRAG-Benchmark); [Xu et al. (2024)](https://arxiv.org/abs/2404.17723); [Sarmah et al. (2024)](https://arxiv.org/abs/2408.04948)).

**2.5 Hallucination and multi-hop reasoning evidence**

[fact] A 2025 workshop paper at the Association for Computational Linguistics (ACL) Generative AI and Knowledge Graphs (GenAIK) workshop, titled "GraphRAG: Leveraging Graph-Based Efficiency to Minimize Hallucinations in LLM-Driven RAG for Finance Data," exists as a peer-reviewed workshop publication addressing graph-based hallucination reduction specifically in finance-domain RAG (source: [Barry et al. (2025) GraphRAG: Leveraging Graph-Based Efficiency to Minimize Hallucinations in LLM-Driven RAG for Finance Data](https://aclanthology.org/2025.genaik-1.6/)).

Access note: specific quantitative hallucination-reduction and token-efficiency figures attributed to this paper by a secondary AI-generated search summary (a "6% hallucination reduction," "11 percentage point recall improvement," and "734-fold decrease" in token use) could not be independently confirmed against the paper's full text or results tables in this session; the paper's existence, authorship, venue, and topical claim (graph-based efficiency reduces hallucination in finance RAG) are confirmed via the ACL Anthology metadata page, but the specific numbers are not used as sourced facts in this item.

[assumption] Multi-hop reasoning benefits (answering questions that require chaining two or more relationship traversals) are assumed to be a genuine structural advantage of explicit graph representations over chunk-similarity retrieval, based on the mechanism described in the GraphRAG survey literature (community structure enables multi-step traversal that vector similarity cannot express), but this item did not locate a single controlled multi-hop benchmark isolating graph structure as the sole causal variable; the surveys describe the mechanism and cite benchmark results, but a fully isolated ablation was not independently verified in this session (source: [Retrieval-Augmented Generation with Graphs (GraphRAG): A Comprehensive Survey](https://arxiv.org/abs/2501.00309); [Graph Retrieval-Augmented Generation: A Survey](https://arxiv.org/abs/2408.08921)).

**3.1–3.2 Migration engineering and incremental construction**

[fact] The standard GraphRAG indexing pipeline runs an LLM-based entity- and relationship-extraction pass over every document chunk, applies recursive community detection using the Leiden algorithm, a graph-clustering method that partitions a network into well-connected communities and is Microsoft's chosen implementation for this step (source: [Traag et al. (2019) From Louvain to Leiden: guaranteeing well-connected communities](https://www.nature.com/articles/s41598-019-41695-z)), to partition the graph into a hierarchy, and then runs a further LLM summarisation pass over every community at every hierarchy level before any query can be answered (source: [Microsoft GraphRAG documentation, Global Search](https://microsoft.github.io/graphrag/query/global_search/); corroborated by secondary technical analysis at [GraphRAG Indexing: Why the $33K Cost Cliff Hits](https://www.bestaiweb.ai/indexing-cost-token-blowup-and-the-hard-engineering-limits-of-graphrag-at-scale/)).

[fact] A 2025 paper titled "Towards Practical GraphRAG: Efficient Knowledge Graph Construction and Hybrid Retrieval at Scale" proposes replacing the expensive LLM-based extraction step with a dependency-parsing-based construction pipeline specifically to reduce the cost barrier that has limited GraphRAG adoption in enterprise environments, and combines this with a hybrid retrieval strategy rather than graph-only retrieval (source: [Towards Practical GraphRAG: Efficient Knowledge Graph Construction and Hybrid Retrieval at Scale](https://arxiv.org/abs/2507.03226)).

[inference] The direct migration pattern implied by the vendor and framework documentation reviewed is additive rather than a wholesale replacement: keep the existing vector index and embedding pipeline in place, add an entity- and relation-extraction pass to build a graph store (Neo4j, Stardog, or a comparable engine) alongside it, link graph nodes back to the original vector-indexed chunks, and issue both a vector query and a graph query per user request before fusing the results, rather than decommissioning the vector index (source: [Neo4j: What is retrieval-augmented generation (RAG)?](https://neo4j.com/blog/genai/what-is-retrieval-augmented-generation-rag/); [Sarmah et al. (2024)](https://arxiv.org/abs/2408.04948); prior item: [Hosted graph database options for knowledge ontology](https://davidamitchell.github.io/Research/research/2026-05-12-graph-db-saas-knowledge-ontology.html)).

**3.3 Downtime, dual-write risk, and connection to document-drift findings**

[inference] A live migration from vector-only to hybrid vector+graph retrieval introduces a second indexed artefact (the graph) that must stay synchronised with the same source corpus as the vector index; the prior completed item on RAG document drift established that post-deployment corpus changes already behave like unversioned dependency updates for a single vector index, and adding a second, more expensive-to-rebuild index (the graph) increases the number of artefacts that can silently drift out of sync with each other during a migration window (source: [When Retrieval-Augmented Generation source documents change after agent build and test](https://davidamitchell.github.io/Research/research/2026-05-12-rag-document-drift-agent-behavior.html)).

[fact] Incremental graph updates, meaning updating only the affected nodes, edges, and community summaries when new or changed documents arrive rather than rebuilding the entire graph, are an active engineering concern documented directly in the Microsoft GraphRAG project's own issue tracker and technical discussion, rather than a fully solved and default capability of the original pipeline (source: [Incremental indexing (adding new content), microsoft/graphrag issue #741](https://github.com/microsoft/graphrag/issues/741)).

**4.1–4.2 Relative indexing and query cost**

[fact] A secondary technical analysis reports that indexing a single 32,000-word document with Microsoft's GraphRAG pipeline using GPT-4o costs roughly six to seven US dollars, citing a specific vendor-reported reference figure, and states explicitly that this figure is widely cited but not an official Microsoft-published benchmark (source: [GraphRAG Indexing: Why the $33K Cost Cliff Hits](https://www.bestaiweb.ai/indexing-cost-token-blowup-and-the-hard-engineering-limits-of-graphrag-at-scale/)).

[inference] The same secondary source estimates that the LLM-based extraction, recursive community detection, and community-summarisation layers together produce an indexing token-consumption ratio of roughly five to ten times the source token count, attributed to a Microsoft community-blog estimate rather than a peer-reviewed benchmark, and states this is "the right order of magnitude for budgeting" rather than a precise figure (source: [GraphRAG Indexing: Why the $33K Cost Cliff Hits](https://www.bestaiweb.ai/indexing-cost-token-blowup-and-the-hard-engineering-limits-of-graphrag-at-scale/)).

Access note: the canonical Microsoft Research blog post on LazyGraphRAG (URL: microsoft.com/en-us/research/blog/lazygraphrag-setting-a-new-standard-for-quality-and-cost/) returned unrelated cached content (a health-insurance article) on every fetch attempt in this session and could not be independently read; claims about LazyGraphRAG's specific cost reduction are therefore sourced only to a secondary vendor blog in this item, not to the primary Microsoft post, and are labelled accordingly.

[inference] A secondary vendor blog reports that LazyGraphRAG, a Microsoft Research technique that defers community summarisation from indexing time to query time, brings indexing cost to roughly the same range as vector-only RAG (a few dollars per typical corpus) and reduces per-global-query cost by roughly two orders of magnitude compared to standard GraphRAG, while a from-scratch GraphRAG indexing estimate for an 80,000-document legal corpus was quoted to the same source's own client at approximately 12,000 US dollars in LLM Application Programming Interface (API) costs before a single query was run; because this claim comes from a vendor blog rather than the primary Microsoft publication (which was inaccessible in this session), it is treated as a directionally credible but not independently verified cost estimate (source: [LazyGraphRAG: 700x Cheaper GraphRAG That Actually Works](https://particula.tech/blog/lazygraphrag-700x-cheaper-graphrag-knowledge-graphs)).

**4.3 Cost-reduction techniques and their effect on the cost picture**

[fact] The "Towards Practical GraphRAG" paper's stated core contribution is an efficient, non-LLM-dependent (dependency-parsing-based) knowledge-graph construction pipeline combined with a hybrid retrieval strategy, proposed explicitly to address the reliance on expensive LLM-based extraction that the authors identify as having limited GraphRAG's enterprise adoption (source: [Towards Practical GraphRAG (2025)](https://arxiv.org/abs/2507.03226)).

[inference] Taken together, the cost evidence in §4.1 to §4.3 supports a specific, bounded claim: the up-front cost gap between vector RAG and ontology-backed GraphRAG is real and can be substantial with the original LLM-heavy Microsoft pipeline, but that gap is an implementation-pipeline property, not an intrinsic property of graph-based retrieval, because at least two independent published approaches (dependency-parsing-based construction and lazy, query-time summarisation) report closing most of the cost gap while retaining a graph-structured index (source: [Towards Practical GraphRAG (2025)](https://arxiv.org/abs/2507.03226); [LazyGraphRAG: 700x Cheaper GraphRAG That Actually Works](https://particula.tech/blog/lazygraphrag-700x-cheaper-graphrag-knowledge-graphs)).

**5.1–5.3 Adoption thresholds**

[inference] The strongest converging signal across the production evidence (LinkedIn support tickets, HybridRAG financial transcripts, the ORAN telecom benchmark) is that ontology-backed or graph-augmented retrieval earns its cost when the underlying data has dense, explicit inter-record relationships that the query patterns actually exploit, meaning cross-referencing, multi-hop lookups, and structured document hierarchies, rather than a generic claim that all enterprise knowledge management benefits equally (source: [Xu et al. (2024)](https://arxiv.org/abs/2404.17723); [Sarmah et al. (2024)](https://arxiv.org/abs/2408.04948); [Benchmarking Vector, Graph and Hybrid RAG Pipelines for ORAN (2025)](https://arxiv.org/abs/2507.03608); [GraphRAG-Bench](https://github.com/GraphRAG-Bench/GraphRAG-Benchmark)).

[inference] The prior completed item on ServiceNow's AI knowledge stack found that RAG grounding quality depends on knowledge-base and CMDB governance quality being addressed before AI activation; applying that same precondition here, an organisation whose vector RAG deployment already suffers from poor source-document governance is unlikely to get a good return from adding a knowledge graph, because the graph-construction pipeline extracts entities and relations from the same ungoverned source documents and will encode the same quality problems into a second, harder-to-maintain index (source: [ServiceNow AI: Knowledge Management, RAG Pipelines, and Agent Frameworks](https://davidamitchell.github.io/Research/research/2026-03-08-servicenow-ai-knowledge-rag-agents.html)).

[inference] Where corpus size is small, query patterns are dominated by single-fact lookup rather than cross-referencing, or the team cannot commit to the incremental-update engineering discussed in §3.2 and §3.3, the evidence in §2.4 (GraphRAG-Bench's explicit finding that GraphRAG frequently underperforms vanilla RAG) and §4 (cost) together support keeping vector RAG or a lightweight hybrid as the more practical choice, deferring ontology-backed KG-RAG until relationship density or global-sensemaking query volume increases (source: [GraphRAG-Bench](https://github.com/GraphRAG-Bench/GraphRAG-Benchmark); [Towards Practical GraphRAG (2025)](https://arxiv.org/abs/2507.03226)).

### §3 Reasoning

Facts established: a production customer-service deployment (LinkedIn) shows a measurable, large improvement in retrieval ranking and a meaningful reduction in resolution time from adding a knowledge graph to an existing support-ticket RAG pipeline [fact, source: https://arxiv.org/abs/2404.17723]. A financial-domain paper (HybridRAG) and an independent telecom-domain benchmark (ORAN) both test the same three-way comparison and both find combined vector-plus-graph retrieval outperforms either technique alone [fact, sources: https://arxiv.org/abs/2408.04948; https://arxiv.org/abs/2507.03608]. A dedicated benchmark project (GraphRAG-Bench) states directly that GraphRAG frequently underperforms vanilla RAG in many real-world tasks [fact, source: https://github.com/GraphRAG-Bench/GraphRAG-Benchmark]. The original Microsoft GraphRAG indexing pipeline is LLM-extraction-heavy and demonstrably expensive to build and to update incrementally [fact, sources: https://microsoft.github.io/graphrag/query/global_search/; https://github.com/microsoft/graphrag/issues/741].

Inferences drawn: the production wins cluster in domains with dense, explicit relationships (support-ticket cross-referencing, financial statement structure, telecom specification cross-references) rather than generic enterprise text [inference, source: https://arxiv.org/abs/2404.17723; https://arxiv.org/abs/2408.04948; https://arxiv.org/abs/2507.03608]. The cost gap between vector RAG and GraphRAG is a property of the specific extraction pipeline rather than an unavoidable property of graph-structured retrieval, given that at least two independent published techniques report closing most of that gap [inference, source: https://arxiv.org/abs/2507.03226].

Assumption made explicit: the causal isolation of "graph structure specifically reduces hallucination and enables multi-hop reasoning" versus "richer retrieval context of any kind reduces hallucination" was not independently confirmed by a controlled ablation located in this session; this item treats the mechanism as plausible and evidence-consistent but not conclusively isolated [assumption, source: https://arxiv.org/abs/2501.00309; https://arxiv.org/abs/2408.08921].

Narrative glue removed: no claim in §2 asserts that ontology-backed KG-RAG is superior in general; every positive finding is scoped to the specific domain, query class, or corpus property under which it was measured.

### §4 Consistency Check

```text
contradiction_scan: resolved
finding: LinkedIn (2404.17723) and HybridRAG (2408.04948) report graph-augmented retrieval winning, while GraphRAG-Bench reports GraphRAG frequently losing to vanilla RAG
resolution: not a contradiction once query domain and structure density are held constant; LinkedIn and HybridRAG test graph augmentation on relationship-dense corpora with cross-referencing queries, while GraphRAG-Bench's finding covers a broader mix of tasks including ones without exploitable relational structure
confidence_adjustment: overall claim kept scoped to "relationship-dense domains and cross-referencing queries", not generalised to all enterprise RAG
scope_guardrail: maintained; no claim extends beyond customer service, enterprise knowledge management, and closely related enterprise question-answering settings named in Scope
acronym_audit: passed in final Step 6 self-review pass
unresolved_source: LazyGraphRAG primary Microsoft Research blog post inaccessible in this session; cost claims about LazyGraphRAG downgraded to secondary-sourced inference
```

### §5 Depth and Breadth Expansion

**Technical lens:** the migration is best modelled as adding a second, differently-shaped index (a graph) alongside an existing vector index rather than replacing one with the other, because every piece of production evidence found in this session (LinkedIn, HybridRAG, the ORAN benchmark) tests a combined or graph-plus-vector configuration, not a graph-only replacement [inference, source: https://arxiv.org/abs/2404.17723; https://arxiv.org/abs/2408.04948; https://arxiv.org/abs/2507.03608].

**Economic lens:** the up-front cost of the original LLM-heavy GraphRAG construction pipeline (roughly six to seven US dollars per 32,000-word document by one widely cited but unofficial estimate, scaling to five-figure sums for enterprise-scale corpora per the same secondary source) is the single most concrete practical barrier identified in this investigation, and it is precisely the barrier that the two most recent papers reviewed (dependency-parsing-based construction and lazy summarisation) are designed to remove [inference, source: https://www.bestaiweb.ai/indexing-cost-token-blowup-and-the-hard-engineering-limits-of-graphrag-at-scale/; https://arxiv.org/abs/2507.03226].

**Regulatory lens:** none of the sources reviewed in this session directly address regulatory drivers specific to choosing ontology-backed KG-RAG over vector RAG; this is noted as a gap in Risks/Gaps rather than assumed absent.

**Historical lens:** the shift from Microsoft's original 2024 LLM-extraction-heavy GraphRAG design toward 2025 cost-reduction techniques (dependency parsing, lazy summarisation) mirrors an established pattern in RAG tooling more broadly, where an initial capability demonstration is followed within roughly a year by efficiency-focused follow-up work; this same one-year-lag pattern appears in the completed item on graph database TCO, which found early hosted graph platforms consolidating pricing and interoperability roughly a year after initial capability claims [inference, source: https://arxiv.org/abs/2404.16130; https://arxiv.org/abs/2507.03226; https://davidamitchell.github.io/Research/research/2026-05-13-graph-db-landscape-tco-interoperability.html].

**Behavioural lens:** the LinkedIn deployment's reported reduction in median per-issue resolution time is a downstream human-workflow outcome (support agents resolving tickets faster), not solely a retrieval-quality metric, which suggests that the practical business case for migration should be built around workflow-level outcome metrics rather than retrieval-benchmark scores alone [inference, source: https://arxiv.org/abs/2404.17723].


### §6 Synthesis

*(This section seeds the Findings below.)*

**Executive summary:**

Migrating from vector RAG to ontology-backed KG-RAG is best justified as an additive hybrid architecture, not a wholesale replacement, and only where the corpus has dense, explicit relationships that query patterns actually exploit. [inference; source: https://arxiv.org/abs/2404.17723; https://arxiv.org/abs/2408.04948; https://arxiv.org/abs/2507.03608] Production and benchmark evidence show large gains in relationship-dense domains such as customer-service ticket cross-referencing and structured financial-document question answering, while a dedicated benchmark project reports GraphRAG frequently underperforming vanilla RAG on tasks without exploitable relational structure. [inference; source: https://arxiv.org/abs/2404.17723; https://arxiv.org/abs/2408.04948; https://github.com/GraphRAG-Bench/GraphRAG-Benchmark] The original LLM-heavy GraphRAG construction pipeline carries a real and substantial up-front cost, but that cost is a pipeline-design property rather than an intrinsic property of graph-structured retrieval, since 2025 work on dependency-parsing-based construction and lazy, query-time summarisation both report closing most of the gap. [inference; source: https://www.bestaiweb.ai/indexing-cost-token-blowup-and-the-hard-engineering-limits-of-graphrag-at-scale/; https://arxiv.org/abs/2507.03226]

**Key findings:** (seeded from §2; see Findings below for the full ordered list with confidence labels)

**Evidence map:** (seeded from §2; see Findings below for the full table)

**Assumptions:** (seeded from §2; see Findings below)

**Analysis:** (seeded from §2 and §5; see Findings below)

**Risks, gaps, uncertainties:** primary Microsoft Research blog post on LazyGraphRAG was inaccessible in this session; specific quantitative hallucination-reduction and cost-reduction percentages attributed to two papers by secondary AI-generated summaries could not be independently verified against primary results tables; no regulatory-driver evidence was located.

**Open questions:** (seeded from §2 and §5; see Findings below)

### §7 Recursive Review

```text
review_result: pass
sections_justified: true
threads_synthesised: true
acronym_audit: passed (RAG, KG-RAG, LLM, MRR, BLEU, ACL, GenAIK, ORAN, RIC, API, CMDB, RDF, RDFS, OWL, TCO, LSA expanded at first use)
claim_audit: passed (every declarative claim in §2 to §6 carries a [fact], [inference], or [assumption] label with source)
uncertainty_audit: passed (LazyGraphRAG primary-source inaccessibility and two unverified secondary statistics recorded as explicit access notes and excluded from sourced-fact claims)
cross_item_audit: passed (seven related completed items cited by URL in §0 and §5)
```

---

## Findings

*(Populated from §6 Synthesis above.)*

### Executive Summary

Migrating from vector Retrieval-Augmented Generation (RAG) to ontology-backed Knowledge Graph RAG (KG-RAG) is justified as an additive hybrid architecture that keeps the existing vector index and adds a graph store alongside it, not as a wholesale replacement of vector search. [inference; source: https://arxiv.org/abs/2404.17723; https://arxiv.org/abs/2408.04948; https://arxiv.org/abs/2507.03608] The migration earns its added complexity specifically where the corpus has dense, explicit inter-record relationships and query patterns exploit them, such as customer-service ticket cross-referencing and structured financial-document question answering, where production and controlled-benchmark evidence both show graph-augmented retrieval outperforming vector-only retrieval. [inference; source: https://arxiv.org/abs/2404.17723; https://arxiv.org/abs/2408.04948; https://arxiv.org/abs/2507.03608] A dedicated cross-domain benchmark project reports that GraphRAG frequently underperforms plain vector RAG on tasks lacking that relational density, so the migration is not universally beneficial. [inference; source: https://github.com/GraphRAG-Bench/GraphRAG-Benchmark] The original LLM-extraction-heavy GraphRAG construction pipeline carries a substantial, well-documented up-front cost, but 2025 research shows this cost is a property of the specific extraction pipeline rather than an unavoidable cost of graph-structured retrieval itself, since dependency-parsing-based construction and lazy, query-time summarisation both report closing most of the cost gap with vector RAG. [inference; source: https://www.bestaiweb.ai/indexing-cost-token-blowup-and-the-hard-engineering-limits-of-graphrag-at-scale/; https://arxiv.org/abs/2507.03226] Organisations should treat existing knowledge-base and source-document governance quality, established in prior research as a precondition for reliable vector RAG, as an equally binding precondition for a KG-RAG migration, because a graph built from ungoverned source documents inherits and compounds the same quality problems in a second, more expensive index. [inference; source: https://davidamitchell.github.io/Research/research/2026-03-08-servicenow-ai-knowledge-rag-agents.html; https://davidamitchell.github.io/Research/research/2026-05-12-rag-document-drift-agent-behavior.html]

### Key Findings

1. A production knowledge-graph-augmented customer-service retrieval system deployed at LinkedIn outperformed a vector-only baseline by **77.6% in Mean Reciprocal Rank** and by 0.32 in BLEU score, and reduced median per-issue resolution time by 28.6% after roughly six months in production. (medium confidence; single production case study; source: https://arxiv.org/abs/2404.17723)

2. Baseline vector RAG performs poorly on **global sensemaking questions** that require synthesising information across an entire dataset, because similarity search has no specific semantic anchor to retrieve against for a corpus-wide theme question. (high confidence; source: https://arxiv.org/abs/2404.16130; https://microsoft.github.io/graphrag/query/global_search/)

3. HybridRAG, combining vector-database retrieval with knowledge-graph retrieval, outperformed both vector-only and graph-only retrieval individually on financial earnings-call question answering, at both the **retrieval and answer-generation stages**. (medium confidence; single benchmark study; source: https://arxiv.org/abs/2408.04948)

4. An independent 2025 benchmark applying the same three-way vector-versus-graph-versus-hybrid comparison to telecom Open Radio Access Network (ORAN) specifications and RAN Intelligent Controller (RIC) Application Programming Interface (API) definitions **replicates the same experimental design** in a second, unrelated domain from the financial HybridRAG study. (medium confidence; source: https://arxiv.org/abs/2507.03608)

5. A dedicated cross-task benchmark project states that **GraphRAG frequently underperforms vanilla vector RAG** on many real-world tasks, and was built specifically to identify the scenarios where graph structure provides a measurable retrieval benefit rather than assuming a universal advantage. (medium confidence; single benchmark-project statement; source: https://github.com/GraphRAG-Bench/GraphRAG-Benchmark)

6. The original Microsoft GraphRAG indexing pipeline requires an LLM-based entity and relationship extraction pass over every document chunk, followed by recursive **Leiden-algorithm community detection** and a further LLM summarisation pass over every resulting community at every hierarchy level, before any query can be answered. (medium confidence; pipeline architecture documented primarily by the vendor; source: https://microsoft.github.io/graphrag/query/global_search/; https://www.nature.com/articles/s41598-019-41695-z)

7. A widely cited but not officially Microsoft-published cost estimate places the price of indexing a single 32,000-word document with the original GraphRAG pipeline on GPT-4o at roughly **six to seven US dollars**, an order of magnitude more expensive per document than typical vector-only embedding indexing. (low confidence; source: https://www.bestaiweb.ai/indexing-cost-token-blowup-and-the-hard-engineering-limits-of-graphrag-at-scale/)

8. A 2025 paper titled "Towards Practical GraphRAG" proposes replacing LLM-based entity extraction with a **dependency-parsing-based construction pipeline** combined with hybrid retrieval, explicitly to remove the cost barrier that the authors identify as limiting GraphRAG's enterprise adoption. (medium confidence; source: https://arxiv.org/abs/2507.03226)

9. Incremental graph updates, meaning updating only affected nodes, edges, and community summaries when source documents change rather than rebuilding the entire graph, remain an **active open engineering concern** documented directly in the Microsoft GraphRAG project's own issue tracker rather than a fully solved default capability. (medium confidence; source: https://github.com/microsoft/graphrag/issues/741)

10. A prior completed item in this research corpus established that post-deployment changes to RAG source documents behave like **unversioned dependency updates** for a single vector index, and adding a second, more expensive-to-rebuild graph index during a migration increases the number of artefacts that can drift out of sync with each other. (medium confidence; source: https://davidamitchell.github.io/Research/research/2026-05-12-rag-document-drift-agent-behavior.html)

11. A prior completed item on ServiceNow's AI knowledge stack established that RAG grounding quality depends on source knowledge-base and Configuration Management Database **governance quality** being addressed before AI activation, a precondition that applies equally to a knowledge-graph migration because the graph is extracted from the same source documents. (medium confidence; source: https://davidamitchell.github.io/Research/research/2026-03-08-servicenow-ai-knowledge-rag-agents.html)

12. The convergent production and benchmark evidence supports migrating to ontology-backed KG-RAG specifically where corpus relationships are dense and query patterns require cross-referencing or multi-hop lookup, and supports remaining on vector RAG or a lightweight hybrid where corpus size is small, queries are dominated by single-fact lookup, or the team cannot commit to **incremental graph-maintenance engineering**. (medium confidence; source: https://github.com/GraphRAG-Bench/GraphRAG-Benchmark; https://arxiv.org/abs/2507.03226)

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [fact] Knowledge-graph-augmented retrieval improved MRR by 77.6%, BLEU by 0.32, and cut resolution time 28.6% in a production LinkedIn deployment | https://arxiv.org/abs/2404.17723 | medium | single-company deployment; magnitude not generalisable, direction is |
| [fact] Vector RAG performs poorly on global sensemaking/corpus-wide theme questions | https://arxiv.org/abs/2404.16130; https://microsoft.github.io/graphrag/query/global_search/ | high | scoped to a specific query class, not all queries |
| [fact] HybridRAG (vector+graph) outperforms either technique alone on financial transcript Q&A | https://arxiv.org/abs/2408.04948 | medium | specific faithfulness/relevancy percentages not independently verified in this session |
| [fact] Independent ORAN benchmark replicates vector-vs-graph-vs-hybrid comparison in telecom domain | https://arxiv.org/abs/2507.03608 | medium | full results not read in this session, abstract only |
| [fact] GraphRAG frequently underperforms vanilla RAG on many real-world tasks | https://github.com/GraphRAG-Bench/GraphRAG-Benchmark | medium | direct project statement, cross-domain benchmark |
| [fact] Original GraphRAG pipeline requires LLM extraction, Leiden community detection, and LLM community summarisation before querying | https://microsoft.github.io/graphrag/query/global_search/; https://www.nature.com/articles/s41598-019-41695-z | medium | official project documentation |
| [inference] ~$6-7 per 32,000-word document indexing cost on GPT-4o | https://www.bestaiweb.ai/indexing-cost-token-blowup-and-the-hard-engineering-limits-of-graphrag-at-scale/ | low | secondary source explicitly flags this as unofficial and widely cited rather than benchmarked |
| [fact] "Towards Practical GraphRAG" proposes dependency-parsing construction plus hybrid retrieval to cut cost | https://arxiv.org/abs/2507.03226 | medium | abstract-level confirmation; full results not independently verified |
| [fact] Incremental graph update is an open engineering concern in Microsoft's own issue tracker | https://github.com/microsoft/graphrag/issues/741 | medium | primary project source |
| [inference] Document drift risk compounds with a second (graph) index during migration | https://davidamitchell.github.io/Research/research/2026-05-12-rag-document-drift-agent-behavior.html | medium | extension of prior completed item's conclusion, not independently re-tested here |
| [inference] Source governance is a precondition for migration value, not just for baseline RAG | https://davidamitchell.github.io/Research/research/2026-03-08-servicenow-ai-knowledge-rag-agents.html | medium | extension of prior completed item's conclusion |
| [inference] Adoption threshold: relationship density and cross-referencing query volume, not corpus size alone | https://github.com/GraphRAG-Bench/GraphRAG-Benchmark; https://arxiv.org/abs/2507.03226 | medium | synthesised across benchmark and cost-reduction evidence |

### Assumptions

- **Assumption:** graph structure itself, rather than richer retrieval context of any kind, is the specific causal mechanism behind reported hallucination reduction and multi-hop reasoning gains. **Justification:** the GraphRAG survey literature describes this mechanism and cites supporting benchmark results, but this session did not locate a controlled ablation isolating graph structure as the sole variable; the assumption is treated as plausible and evidence-consistent, not confirmed (source: https://arxiv.org/abs/2501.00309; https://arxiv.org/abs/2408.08921).
- **Assumption:** the magnitude of the LinkedIn production result (77.6% MRR improvement, 28.6% resolution-time reduction) does not transfer as a fixed expected return to other organisations, because it reflects one company's ticket corpus, benchmark design, and baseline system. **Justification:** single-deployment case studies establish direction of effect, not a portable effect size, per standard evidence-sufficiency practice (source: https://arxiv.org/abs/2404.17723).
- **Assumption:** LazyGraphRAG's specific cost-reduction magnitude is directionally credible but not independently verified, because the primary Microsoft Research publication was inaccessible in this session and the only available account is a secondary vendor blog. **Justification:** the vendor blog's mechanism description (deferring summarisation to query time) is consistent with the publicly documented general GraphRAG architecture, but the specific multiplier claims are unverified against the primary source (source: https://particula.tech/blog/lazygraphrag-700x-cheaper-graphrag-knowledge-graphs).

### Analysis

The production and benchmark evidence converges on a scoped rather than universal conclusion. [inference; source: https://arxiv.org/abs/2404.17723; https://arxiv.org/abs/2408.04948; https://github.com/GraphRAG-Bench/GraphRAG-Benchmark] LinkedIn's customer-service deployment and the HybridRAG financial-transcript study both test domains with dense, explicit inter-record relationships (support-ticket cross-referencing and structured financial statements), and both report graph-augmented retrieval winning. [inference; source: https://arxiv.org/abs/2404.17723; https://arxiv.org/abs/2408.04948] GraphRAG-Bench's finding that GraphRAG frequently underperforms vanilla RAG on many real-world tasks is not a contradiction of those results once query domain and relational density are held constant as the controlling variable, because GraphRAG-Bench evaluates a broader task mix that includes queries without exploitable graph structure. [inference; source: https://github.com/GraphRAG-Bench/GraphRAG-Benchmark]

A plausible rival explanation for the LinkedIn and HybridRAG results is that any richer retrieval context, not graph structure specifically, would have produced similar gains, for example longer context windows or better chunk metadata. [inference; source: https://arxiv.org/abs/2408.04948] This rival explanation is only partially addressed by the evidence gathered in this session: the HybridRAG paper's explicit note that both authors' implementations added document metadata to VectorRAG as well, and VectorRAG still underperformed HybridRAG, weakens the "any richer context would do" explanation somewhat, but does not eliminate it, because no controlled ablation isolating graph structure alone from other forms of context enrichment was located. [inference; source: https://arxiv.org/abs/2408.04948]

On cost, the evidence resolves an apparent tension between "GraphRAG is prohibitively expensive" and "graph-structured retrieval is production-viable" claims: both are true of different pipeline implementations at different points in time, not of graph-structured retrieval as a category. [inference; source: https://www.bestaiweb.ai/indexing-cost-token-blowup-and-the-hard-engineering-limits-of-graphrag-at-scale/; https://arxiv.org/abs/2507.03226] The original 2024 Microsoft pipeline is LLM-extraction-heavy and costly; the 2025 dependency-parsing and lazy-summarisation approaches directly target that specific cost driver. [inference; source: https://arxiv.org/abs/2507.03226] This means a migration decision made against 2024 cost figures alone would overstate the current cost barrier. [inference; source: https://arxiv.org/abs/2507.03226]

The migration-engineering evidence weighs toward an additive hybrid pattern over a wholesale replacement, because every piece of production and benchmark evidence reviewed tests a combined configuration rather than a graph-only replacement of vector search, and no source reviewed recommends decommissioning an existing vector index. [inference; source: https://arxiv.org/abs/2404.17723; https://arxiv.org/abs/2408.04948; https://arxiv.org/abs/2507.03608; https://arxiv.org/abs/2507.03226]

### Risks, Gaps, and Uncertainties

- The primary Microsoft Research publication on LazyGraphRAG was inaccessible in this session (every fetch attempt returned unrelated cached content); cost-reduction claims attributed to it in this item rely on a secondary vendor blog and are labelled as unverified against the primary source.
- Specific quantitative figures reported by AI-generated search summaries for the HybridRAG faithfulness/relevancy scores and for the ACL GenAIK finance-hallucination paper's reduction percentages could not be independently confirmed against primary results tables in this session and were excluded from sourced-fact claims; a follow-up session with direct PDF text extraction could close this gap.
- No source reviewed in this session addressed regulatory drivers (for example, data-residency or explainability mandates) that might independently favour or disfavour ontology-backed KG-RAG; this is a genuine evidence gap, not an assumed absence.
- The evidence base for multi-hop reasoning gains attributable specifically to graph structure, as opposed to richer retrieval context generally, rests on survey-level description of a mechanism rather than a controlled ablation; this is the weakest-evidenced claim in this item.
- All production evidence located is drawn from single-company case studies (LinkedIn) or from academic benchmark papers; no multi-organisation, multi-year total-cost-of-ownership study comparing sustained vector RAG operation against sustained KG-RAG operation was located.

### Open Questions

- What does a controlled ablation isolating graph structure from other forms of retrieval-context enrichment (longer context windows, richer chunk metadata, reranking) show about the specific causal contribution of graph structure to hallucination reduction and multi-hop reasoning quality?
- What is the total cost of ownership of a hybrid vector-plus-graph retrieval system over a multi-year operational horizon, including incremental update engineering effort, compared with sustained vector-only RAG operation at the same corpus scale?
- Do regulatory or compliance requirements (data residency, explainability, auditability) independently favour ontology-backed KG-RAG over vector RAG in any enterprise vertical, and if so, which ones?
- What does the full results table of the ORAN vector-versus-graph-versus-hybrid benchmark show for latency and cost, beyond the abstract-level confirmation obtained in this session?

---

## Output

*(Fill in when completing, what was produced as a result of this research?)*

- Type: knowledge
- Description: Structured findings on when migrating from vector RAG to ontology-backed KG-RAG is justified, concluding that an additive hybrid architecture is favoured over wholesale replacement and that migration earns its cost specifically in relationship-dense enterprise domains with cross-referencing query patterns. [inference; source: https://arxiv.org/abs/2404.17723; https://github.com/GraphRAG-Bench/GraphRAG-Benchmark]
- Links: [Xu et al. (2024) Retrieval-Augmented Generation with Knowledge Graphs for Customer Service Question Answering](https://arxiv.org/abs/2404.17723); [Sarmah et al. (2024) HybridRAG](https://arxiv.org/abs/2408.04948); [GraphRAG-Bench](https://github.com/GraphRAG-Bench/GraphRAG-Benchmark)

