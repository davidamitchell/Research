---
title: "Information synthesis: non-lossy compression, entropy, and information theory"
added: 2026-03-02T08:16:39+00:00
status: completed
priority: high
tags: [synthesis, information-theory, entropy, compression, ai]
started: 2026-03-02T08:16:39+00:00
completed: 2026-03-02T08:16:39+00:00
output: [knowledge, skill]
cites: []          # slugs of items this item directly depends on or quotes
related: []        # slugs of thematically connected items
superseded_by: ~   # slug of a later item that overrides this one (null if not superseded)
supersedes: ~      # slug of an older item this one replaces (null if not applicable)
item_type: primary # primary | synthesis
confidence: medium # high | medium | low
versions: []       # entries: {version: "1.0", sha: "<commit-hash>", changed: YYYY-MM-DD, progress: "<path>", summary: "<one-line>"}
---

# Information synthesis: non-lossy compression, entropy, and information theory

## Question / Hypothesis

What is the best way to synthesise information from multiple sources in a manner that is minimally lossy — preserving the most signal while compressing volume — drawing on information theory, entropy, and compression research?

## Context

The core challenge of research is not gathering information but synthesising it. As research corpus grows, naive summarisation (LLM summary of each source) loses context and introduces hallucination. Better approaches exist:

- **Information theory**: measure the entropy of a document; high-entropy sections carry more information and should be preserved
- **Semantic compression**: identify redundancy across sources; only keep deltas
- **Chain-of-density** prompting: iteratively compress while tracking what is dropped
- **Graph-based synthesis**: model claims as nodes, evidence as edges

This is a foundational research question that should inform how we build the synthesis layer of the tooling.

## Scope

**In scope:**
- Literature review of information-theoretic approaches to text compression
- Survey of LLM prompting techniques for synthesis (chain-of-density, compression prompting)
- Evaluation of semantic deduplication approaches

**Out of scope:**
- Implementation of a full synthesis pipeline (that is Epic 4+)

## Approach

1. Review Shannon entropy and its application to text
2. Review chain-of-density and related prompting techniques
3. Review graph-based synthesis (knowledge graphs)
4. Synthesise recommendations into an ADR or knowledge note

## Sources

- [ ] Shannon, C.E. (1948). A Mathematical Theory of Communication
- [ ] Adams et al. (2023). From Sparse to Dense: GPT-4 Summarization with Chain of Density Prompting — https://arxiv.org/abs/2309.04269
- [ ] Meng et al. (2022). ROME / knowledge editing in transformers
- [ ] Information bottleneck method (Tishby et al.)

## Findings

### Executive Summary

No single technique achieves minimally-lossy synthesis across multiple sources; the best approach combines three layers: entropy-guided extraction (preserve high-entropy, high-information sections), semantic deduplication (remove cross-source redundancy, keep only deltas), and graph-structured synthesis (model claims as nodes, evidence as edges for multi-hop reasoning). Chain of Density (CoD) prompting is the most directly applicable LLM technique — it iteratively compresses while adding entity density, producing summaries that human raters prefer over vanilla GPT-4 summaries. Naive per-source LLM summarisation is the worst option: it accumulates hallucinations and loses cross-source context as corpus size grows. The theoretical foundation (Shannon entropy, Information Bottleneck, MDL) all converge on the same principle: discard what is predictable/redundant, preserve what is novel and causally relevant.

### Key Findings

1. **Shannon entropy identifies information-dense text.** High-entropy sections are less predictable and carry more signal; low-entropy sections are repetitive and safe to compress. Entropy can be computed per-sentence or per-paragraph to guide extractive summarisation, selecting sentences that contribute most to document entropy.

2. **Chain of Density (CoD) prompting is the leading LLM-native synthesis technique.** Adams et al. (2023) demonstrate that iteratively rewriting a summary to add 1–3 missed salient entities per pass — without increasing length — produces summaries rated more informative and faithful than baseline GPT-4. Human preference peaks at a mid-density level that matches human-written reference summaries; beyond that, density harms readability.

3. **The Information Bottleneck (IB) method provides formal grounding for the compression–relevance trade-off.** Tishby et al. formalise synthesis as finding a compressed representation T of input X that maximises mutual information with the target variable Y while minimising I(X;T). This captures exactly the problem: keep what is predictive of meaning, discard the rest. The β parameter controls the compression–fidelity trade-off.

4. **Minimum Description Length (MDL) frames summarisation as lossless coding.** A summary is optimal under MDL when the sum of (summary length + reconstruction model length) is minimised. This is equivalent to finding the most compressible representation of the source — exploiting regularities (grammar, redundancy) while preserving unique content.

5. **Semantic deduplication is a prerequisite for cross-source synthesis.** String/hash-based deduplication misses paraphrases. Embedding-based methods (SemDeDup, MinHash/LSH) cluster semantically equivalent content across documents and suppress it before synthesis, preventing diluted or repeated outputs. Cross-document topic-aligned chunking (2025 arxiv) extends this by aligning semantically similar chunks across sources before retrieval.

6. **Graph-based synthesis (GraphRAG) outperforms flat retrieval for multi-source reasoning.** Microsoft's GraphRAG constructs a knowledge graph from an LLM-processed corpus, with entities as nodes and relationships as edges, then uses community-level summarisation to answer queries that span multiple documents. It outperforms naive RAG on complex, multi-hop queries that require integrating evidence from different sources.

7. **Naive per-source LLM summarisation introduces compounding errors.** Hallucinations in LLM summaries arise from limited context windows, exposure bias, and noisy training data. When each source is summarised independently and summaries are concatenated, errors compound and cross-source context is permanently lost. RAG with grounded retrieval is consistently found to reduce hallucination rates versus independent summarisation.

8. **ROME/MEMIT (Meng 2022) shows that factual knowledge is localised in transformer mid-layer feed-forward modules.** While this is primarily a knowledge-editing result, it implies that LLMs store facts in structured, addressable representations — supporting the view that synthesis quality can in principle be improved by intervening at the representation level, not just at the prompt level.

9. **There is a density sweet spot; over-compression degrades faithfulness.** CoD human preference studies show that beyond approximately 3–4 rounds of densification, summaries become harder to follow and introduce factual errors. This matches the IB framework's prediction: compression beyond the optimal β introduces distortion. Synthesis pipelines must expose a tunable compression parameter.

10. **Two-phase deduplication (intra-document then cross-document) is the current best practice for RAG pipelines.** Production RAG systems (lucidRAG, cross-document chunking literature) decouple deduplication at ingestion (within a document) from deduplication at retrieval (across documents). The two phases serve different purposes: intra-document removes formatting noise; cross-document removes redundant claims.

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| High-entropy text sections carry more information and should be preserved | Shannon (1948); Wikipedia Entropy (information theory); MDPI "Entropy of Digital Texts" | high | Well-established information theory result |
| CoD prompting produces human-preferred summaries vs vanilla GPT-4 | Adams et al. (2023) arxiv:2309.04269 | high | 500 human-annotated summaries, 5000 unannotated; direct experimental evidence |
| IB method formalises compression–relevance trade-off as min I(X;T) – β·I(T;Y) | Tishby et al. (1999/2000); Wikipedia Information Bottleneck | high | Foundational theoretical result; widely cited |
| MDL frames summarisation as lossless coding: summary is optimal when description length is minimised | Wikipedia MDL; liambai.com "From Kolmogorov to LLMs" | high | Standard information theory result; well-sourced |
| Semantic deduplication via embeddings outperforms hash-based dedup for paraphrases | SemDeDup (NeurIPS 2023); Fraunhofer evaluation 2024 | high | Multiple independent sources corroborate |
| GraphRAG outperforms naive RAG on complex multi-source queries | Microsoft Research GraphRAG blog; machinelearningplus.com GraphRAG guide | medium | Performance claims are from Microsoft's own evaluation; independent replication limited |
| Naive per-source LLM summarisation introduces compounding hallucinations | Survey on LLM hallucination (2024, arxiv:2401.01313); Nature (2025) hallucination survey | high | Multiple independent surveys consistently identify this failure mode |
| Factual knowledge is localised in mid-layer transformer feed-forward modules | Meng et al. (2022) arxiv:2202.05262 (ROME) | high | Verified via causal tracing; replicated in subsequent work |
| Density sweet spot exists; over-compression degrades faithfulness | Adams et al. (2023) CoD human preference study | high | Direct experimental finding from the same paper |
| Two-phase dedup (intra then cross-document) is best practice | Cross-Document Topic-Aligned Chunking arxiv:2601.05265; lucidRAG blog | medium | Emerging consensus; fewer than 5 independent published results |

### Assumptions

- **Assumption:** The research tooling corpus is multi-source (YouTube transcripts, papers, web pages) with significant topical overlap between sources. **Justification:** This is explicit in the project context; the tooling already has YouTube, web, and paper fetchers.
- **Assumption:** The synthesis problem is primarily about knowledge retention, not style fidelity. **Justification:** The research question asks for "minimally lossy" in terms of signal, not verbatim reconstruction.
- **Assumption:** LLM token context limits will remain a binding constraint at synthesis time. **Justification:** Even with expanding context windows (128k–1M tokens), multi-source corpora in this system can exceed practical limits.

### Analysis

Shannon entropy, IB, and MDL all converge on the same principle from different angles: identify what is novel and preserve it; discard what is predictable. This theoretical convergence is strong evidence that the principle is sound, even though direct application to synthesis pipelines varies.

CoD prompting is the most immediately implementable technique. It requires no special infrastructure — only a well-designed prompt — and produces measurably better outputs than naive summarisation. Its limitation is that it operates at the single-document level; it does not address cross-source redundancy.

GraphRAG addresses cross-source synthesis but requires a knowledge graph construction step that has non-trivial cost and complexity. It is the right architecture for a mature synthesis pipeline but is not the right first step.

The practical recommendation for this project's synthesis layer is a three-stage approach:
1. **Extract** high-entropy/high-information chunks from each source (entropy scoring or sentence-level scoring).
2. **Deduplicate** cross-source at the semantic level (embedding similarity clustering).
3. **Synthesise** the deduplicated, high-signal chunks using CoD-style prompting (iterative densification with entity tracking).

This sequence mirrors what information theory recommends: exploit within-source structure first, then remove cross-source redundancy, then compress the remainder.

ROME/MEMIT is directionally interesting (factual knowledge is structured in LLMs) but is a knowledge-editing technique, not a synthesis technique. Its relevance is that it suggests future work on synthesis might involve targeted representation intervention rather than only prompting — this is speculative and out of scope.

The IB framework's β parameter is an important insight: synthesis pipelines should expose a tunable trade-off between compression ratio and fidelity. A fixed compression target is wrong; the right compression level depends on the downstream use case.

### Risks, Gaps, and Uncertainties

- **GraphRAG performance claims are primarily from Microsoft's own evaluations.** Independent replication is limited. The approach may not generalise to smaller corpora or domain-specific content.
- **Entropy scoring for text requires a language model.** Character-level or word-level entropy underestimates semantic entropy (two paraphrases have identical information content but different surface-level entropy). A model-based perplexity score is needed for sentence-level entropy, adding a dependency.
- **CoD prompting was evaluated on news articles (CNN/DailyMail).** Generalisability to academic papers, YouTube transcripts, and web pages is not established experimentally.
- **Two-phase deduplication thresholds are not standardised.** Similarity cutoffs for semantic dedup vary widely across papers; there is no consensus on the right threshold for research synthesis.
- **The IB framework has not been directly applied to document synthesis in practice.** Most IB work is on neural network compression, not text summarisation pipelines. The translation from theory to practice requires engineering work not covered in the literature.

### Open Questions

- What perplexity scoring method (which model, what granularity) best approximates semantic entropy for the sources in this system?
- Should synthesis operate over the full document or only extracted high-entropy chunks? What is the information loss from pre-filtering?
- Is there an existing open-source tool that implements semantic deduplication at the paragraph/chunk level suitable for use in this pipeline?
- Can CoD prompting be adapted for multi-document input (rather than single-source), or does it require a pre-merged input?
- What is the right compression ratio target for research synthesis — what portion of a source's content should survive synthesis?

---

## Output

- Type: knowledge
- Description: Synthesis approach recommendation documenting three-stage pipeline (entropy extraction → semantic dedup → CoD synthesis) grounded in information theory. Foundational input for Epic 4+ synthesis layer design.
- Sources:
  - https://arxiv.org/abs/2309.04269 — Chain of Density prompting paper (Adams et al., 2023)
  - https://en.wikipedia.org/wiki/Information_bottleneck_method — Information Bottleneck method overview
  - https://www.microsoft.com/en-us/research/blog/graphrag-unlocking-llm-discovery-on-narrative-private-data/ — GraphRAG (Microsoft Research)