---
title: "Context Compression and RAG Techniques for Organisational Knowledge"
added: 2026-03-15
status: backlog  # backlog | in-progress | reviewing | completed
priority: high  # low | medium | high
blocks: [2026-03-15-context-layers-aligned-decisions-synthesis]  # slugs (filename without .md) of backlog items that cannot start until this one is complete
tags: [rag, context-management, compression, llm, knowledge-architecture, enterprise-ai, context-window]
started: ~
completed: ~
output: [knowledge]
---

# Context Compression and RAG Techniques for Organisational Knowledge

## Research Question

What are the current best practices and bleeding-edge techniques — including Retrieval-Augmented Generation (RAG), context compression, and context architecture — for selectively surfacing the right slice of a large organisational knowledge corpus (regulations, policies, strategy, current state) into a Large Language Model (LLM) context window at decision time?

## Scope

**In scope:**
- Retrieval-Augmented Generation (RAG) architectures: standard RAG, advanced RAG (re-ranking, hybrid search, contextual chunking), and modular RAG
- Context compression techniques: summarisation-based compression, LLMLingua-style token pruning, map-reduce, hierarchical summarisation
- Context window management strategies: context distillation, sliding windows, memory-augmented transformers
- Frameworks specifically designed for multi-layer organisational knowledge (regulations → strategy → policy → current state → task)
- Academic and industry research published or updated within the last 24 months
- Practical tooling: LangChain, LlamaIndex, Haystack, and comparable frameworks — what patterns they support
- Evaluation criteria: faithfulness, relevance, latency, cost

**Out of scope:**
- General LLM benchmarking unrelated to retrieval or context management
- Fine-tuning as a substitute for context injection
- Vector database implementation internals beyond what is needed to assess RAG quality

**Constraints:** Publicly accessible papers (arXiv, ACL Anthology), blog posts, documentation, and GitHub repositories. No paywalled journals unless abstracts are sufficient.

## Context

Making aligned decisions — decisions consistent with an organisation's regulations, values, strategy, and current operating context — requires an AI agent to have access to a layered set of knowledge that can span thousands of pages. A typical LLM context window (even at 128k–1M tokens) cannot accommodate all relevant organisational context simultaneously, and stuffing the window with undifferentiated text degrades reasoning quality. The key engineering challenge is: given a specific decision or task, how do you retrieve the right context layers (and only those layers), compress them appropriately, and compose them into a coherent context window that enables a high-quality, aligned response? This item surveys the technical landscape for that challenge. Its findings directly feed the synthesis item on aligned decision-making context architecture.

## Approach

1. Survey RAG taxonomy: standard vs. advanced vs. modular RAG — what does each variant add and when is each appropriate for hierarchical organisational knowledge?
2. Investigate context compression techniques: LLMLingua and descendants, summarisation pipelines, map-reduce patterns — what are the fidelity/compression trade-offs?
3. Examine memory-augmented and long-context transformer architectures (MemGPT, Memorizing Transformers, etc.) — how do they address the context-limit problem?
4. Identify academic frameworks for multi-layer or hierarchical knowledge retrieval — are there published approaches that treat regulatory, strategic, and operational knowledge as distinct tiers?
5. Survey practical open-source tooling (LangChain, LlamaIndex, Haystack) for multi-tier context pipelines — what patterns are available out of the box vs. custom-build?
6. Synthesise: what is the current state of the art, what gaps remain, and what recommendations emerge for an organisation building context-aware AI decision support?

## Sources

- [ ] https://arxiv.org/abs/2312.10997 — "Retrieval-Augmented Generation for Large Language Models: A Survey"
- [ ] https://arxiv.org/abs/2310.06025 — LLMLingua: Compressing Prompts for Accelerated Inference
- [ ] https://arxiv.org/abs/2304.01373 — MemGPT: Towards LLMs as Operating Systems
- [ ] https://arxiv.org/abs/2305.14788 — Augmented Large Language Models with Parametric Knowledge Guiding
- [ ] https://docs.llamaindex.ai/en/stable/ — LlamaIndex documentation on advanced RAG patterns
- [ ] https://python.langchain.com/docs/concepts/rag/ — LangChain RAG conceptual overview

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
