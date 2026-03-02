---
title: "Agent Memory Management and Context Injection"
added: 2026-03-02
status: backlog
priority: high
tags: [memory, context-injection, rag, agents, knowledge-management, architecture, governance]
started: ~
completed: ~
output: [knowledge]
---

# Agent Memory Management and Context Injection

## Research Question

What is the current state of agent memory management systems — beyond RAG — and which approaches best address the real constraints of latency, knowledge freshness, scoping, governance, quality, and distribution without degenerating into an ungardened wiki?

## Scope

**In scope:**
- Taxonomy of memory types used by agents: in-context (working memory), external retrieval (vector, graph, relational), episodic, semantic, procedural, and their trade-offs
- Latency: read/write costs at different memory layers and how systems mitigate them in hot-path inference
- Knowledge ranking, accuracy, and freshness: how systems decide what is current, what is authoritative, and how stale or conflicting knowledge is handled
- Scoping mechanisms: how knowledge is partitioned by problem domain, team, repo, session, technology, person, role, task, and other dimensions — and whether fine-grained scoping is achievable without combinatorial explosion
- Governance: who can write to shared memory, audit trails, access control, and provenance tracking
- Quality testing: how the accuracy and usefulness of retrieved knowledge is measured and improved over time
- Distribution: how the recall tooling itself and the underlying knowledge base are deployed across teams, infrastructure, or regions
- The "ungardened wiki" failure mode: why memory systems accumulate noise without active curation, and which architectures or incentive structures resist this
- RAG as a partial answer: what RAG solves well, where it falls short, and what alternatives (MemGPT, Zep, Mem0, Letta, knowledge graphs, symbolic memory) address the gaps
- Production deployments or credible prototypes, not purely academic proposals

**Out of scope:**
- Fine-tuning and model weight updates as a form of memory (parametric memory) — separate concern
- Pure document retrieval (search engines, BM25) without agent-specific integration
- General vector database benchmarks unrelated to agent memory use cases

**Constraints:** Focus on agent memory in the context of coding agents, research agents, and enterprise knowledge workers. Prefer systems with observable production use or active open-source traction over vaporware.

## Context

A new generation of memory systems for AI agents is emerging — MemGPT, Zep, Mem0, Letta, LangMem, and others — but the space is immature and fragmented. The core problems are not fully solved:

1. **RAG is a retrieval mechanism, not a memory architecture.** It answers "find text similar to this query" but does not address staleness, conflicting knowledge, scoping by role or context, or the provenance and governance of what gets stored.
2. **Latency tension:** richer memory structures (graphs, ranked indices, multi-hop retrieval) are slower; shallow in-context stuffing is fast but does not scale.
3. **Scoping is hard:** a memory item useful in one context (a specific repo, a specific person's working style, a transient task) may be noise or actively harmful in another. Current systems have crude scoping.
4. **The wiki failure mode:** without a curator ("gardener"), any shared memory store accumulates outdated, duplicated, or contradictory entries. This is the same failure mode as every enterprise wiki before it, now accelerated by agents that write at machine speed.
5. **Governance is largely absent:** most open-source agent memory systems have no access control, audit trail, or quality feedback loop beyond cosine similarity.

This research is high priority because the correct architecture for memory will shape how agents are deployed at scale in enterprise contexts, and getting it wrong early means compounding technical debt.

## Approach

1. **Taxonomy of memory architectures** — Identify and classify the major approaches: in-context stuffing, vector retrieval (RAG), episodic memory stores, knowledge graphs, hybrid (vector + graph), structured memory (MemGPT/Letta paging model), session/long-term split. For each: latency profile, scoping capability, governance support, freshness handling.
2. **RAG gap analysis** — Document precisely what RAG solves and what it does not. Focus on: semantic drift over time, conflicting knowledge, lack of structured relationships, no write-path governance. Identify whether "GraphRAG" or "agentic RAG" closes these gaps or introduces new ones.
3. **Survey of emerging systems** — Review MemGPT/Letta, Zep, Mem0, LangMem, Cognee, Graphiti, and any others with active development. For each: what problem it primarily solves, maturity, scoping mechanisms, governance features, distribution model.
4. **Scoping mechanisms** — Deep-dive on how knowledge is scoped: by session, by user, by team, by repo, by task type, by technology stack. Which systems support multi-dimensional scoping, and at what cost?
5. **The gardener problem** — Investigate what happens to agent memory stores over time without curation. Are there architectures (TTL, confidence decay, conflict resolution, provenance-weighted retrieval) that resist wiki rot? Are there incentive or workflow designs that ensure curation happens?
6. **Governance and quality** — How do production teams test that their memory system is returning accurate, useful knowledge? What does a memory quality benchmark look like? Who has built one?
7. **Gap summary and recommendations** — Synthesise findings into a recommendation on which approach (or combination) is most appropriate for the near term, with explicit caveats about what remains unsolved.

## Sources

- [ ] MemGPT / Letta paper and repo: https://arxiv.org/abs/2310.08560 — the original paging model for LLM memory
- [ ] Zep: https://github.com/getzep/zep — temporal knowledge graph for agent memory
- [ ] Mem0: https://github.com/mem0ai/mem0 — personalized memory layer
- [ ] LangMem (LangChain): https://langchain-ai.github.io/langmem/ — long-term memory for agents
- [ ] Cognee / Graphiti: knowledge graph approaches to agent memory
- [ ] GraphRAG (Microsoft): https://microsoft.github.io/graphrag/ — community-structured graph retrieval
- [ ] "Beyond RAG" survey papers on arXiv — search "agent memory long-term"
- [ ] Koala / MemoryOS and any 2025–2026 agent memory benchmarks
- [ ] Enterprise wiki failure post-mortems — Confluence, Notion, Sharepoint usage studies on knowledge rot
- [ ] A16Z "The New Language Model Stack" or equivalent architectural overviews mentioning memory tiers
- [ ] Production case studies: how teams at scale (Cursor, GitHub Copilot, Devin) handle persistent agent memory

---

## Findings

*(Fill in when completing.)*

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

- Type: knowledge
- Description:
- Links:
