---
title: "Semantic and full-text search over the research corpus"
added: 2026-03-02
status: backlog
priority: high
tags: [search, semantic-search, full-text-search, vector-search, embeddings, indexing, rag]
started: ~
completed: ~
output: [knowledge, tool, backlog-item]
---

# Semantic and full-text search over the research corpus

## Research Question

What combination of full-text search (keyword/BM25) and semantic search (embeddings/vector) is most appropriate for querying the `Research/completed/` corpus, given the constraints of a git-based, local-first, single-owner repository with tens to hundreds of items, and what is the simplest implementation path?

## Scope

**In scope:**
- Full-text search options: SQLite FTS5 (BM25), ripgrep-as-search-backend, Python `whoosh`/`tantivy`
- Semantic search options: sentence-transformers + sqlite-vec, OpenAI embeddings + local index, LanceDB, ChromaDB
- Hybrid approaches: BM25 + vector + Reciprocal Rank Fusion (RRF), as described in the context-mode research
- CLI interface for search: `python -m src.main research search "<query>"`
- What fields to index: title, tags, findings, executive summary, key findings
- Integration with the existing YAML front-matter metadata in research item files
- Performance and dependency trade-offs at the scale of this repo (tens to hundreds of items)

**Out of scope:**
- Server-based search engines (Elasticsearch, OpenSearch, Meilisearch) — must remain local/embedded
- Indexing sources other than `Research/completed/` Markdown files
- UI beyond CLI (covered by `2026-02-27-interface-and-delivery.md` and `2026-03-02-chat-conversational-interface.md`)

**Constraints:** Must run in CI (GitHub Actions), require no external service, and remain git-friendly. Embedding model must be small enough to run in an Actions runner or be optional (API-key-gated).

## Context

The `2026-02-27-indexing-and-tracking-method.md` research (completed) established that JSON state + YAML front-matter is the correct approach for processing-state and item metadata at current scale. It explicitly deferred vector search as a "future-state capability" once the corpus exceeds ~50 items. The `2026-02-27-local-database.md` backlog item covers the underlying database technology choice but is scoped to storage, not search UX or capability design.

The `2026-03-01-context-mode-llm-context-compression.md` research (completed) contains a directly relevant finding (Key Finding 6): a practitioner built a hybrid BM25 + Model2Vec (256-dim, potion-base-8M) + sqlite-vec + RRF retriever over a 15,800-file Obsidian vault (49,746 chunks, 83 MB) and found BM25 alone underperforms on structured data (JSON, tables, config files). The hybrid approach with incremental hash-based re-indexing under 10 seconds is the documented state of the art for this use case.

The `2026-03-01-github-wiki-research-content.md` research (completed) confirmed `Research/completed/` items follow a predictable Markdown + YAML front-matter structure, which simplifies chunking and indexing.

The corpus currently has ~12 completed items. The right time to implement search is before the corpus becomes hard to navigate manually — approximately 30–50 items.

## Approach

1. **Identify the query patterns** — What kinds of queries will be issued? Tag-based ("all items tagged `ai-strategy`"), keyword ("find items mentioning active inference"), topic-based ("what do I know about memory management for agents?"), recency-based. Classify as structural (metadata) vs. content (full-text) vs. semantic (meaning).

2. **Evaluate full-text-only path** — SQLite FTS5 is already a known option (used by Context Mode's knowledge base). Assess: is BM25 over the findings and executive summary sections sufficient for the query patterns? What are the false-negative failure modes?

3. **Evaluate semantic search path** — Survey embedding model options that run locally without an API key: sentence-transformers (all-MiniLM-L6-v2, 22M params), Model2Vec (potion-base-8M, 8M params). Assess: size, inference speed on a standard Actions runner CPU, index size for 100 items.

4. **Evaluate hybrid path** — Combine BM25 (SQLite FTS5) and vector search (sqlite-vec) with RRF, following the pattern from the context-mode finding. What is the complexity cost vs. the quality improvement for this corpus size?

5. **Design the index structure** — Which chunks to index: title + tags + executive summary (small, high-signal), or title + all findings sections (larger, more complete)? Hash-based incremental re-indexing to avoid full rebuilds on each query.

6. **CLI integration** — Define the command: `python -m src.main research search "<query>"` returning a ranked list of research items with title, date, tags, and a matched snippet. Assess whether the output format feeds into the conversational interface (`2026-03-02-chat-conversational-interface.md`).

7. **Produce an ADR** — If semantic search (embeddings) is adopted, an ADR is required (new external dependency, new storage approach beyond `state/index.json`).

## Sources

- [ ] `Research/completed/2026-02-27-indexing-and-tracking-method.md` — prior decision: JSON + YAML front-matter; deferred vector search (Key Finding 5)
- [ ] `Research/completed/2026-03-01-context-mode-llm-context-compression.md` — hybrid BM25+Model2Vec+sqlite-vec+RRF pattern (Key Finding 6)
- [ ] `Research/backlog/2026-02-27-local-database.md` — database technology options including sqlite-vec, ChromaDB, LanceDB
- [ ] sqlite-vec: https://github.com/asg017/sqlite-vec — vector search extension for SQLite
- [ ] SQLite FTS5: https://www.sqlite.org/fts5.html — full-text search
- [ ] sentence-transformers (all-MiniLM-L6-v2): https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2
- [ ] Model2Vec (potion-base-8M): https://github.com/MinishLab/model2vec — small, fast, static sentence embeddings
- [ ] `tantivy` Python bindings: https://github.com/quickwit-oss/tantivy — Rust-based BM25 search library
- [ ] LanceDB: https://lancedb.github.io/lancedb/ — embedded vector store with full-text search

---

## Findings

*(Fill in when completing. Follow the research skill synthesis structure.)*

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

- Type: knowledge, tool, backlog-item
- Description: Search capability recommendation (BM25-only vs. hybrid); ADR if embeddings adopted; implementation backlog slice for `src/search/`; CLI command design
- Links:
  - `Research/completed/2026-02-27-indexing-and-tracking-method.md` (prior indexing decision)
  - `Research/completed/2026-03-01-context-mode-llm-context-compression.md` (hybrid retrieval pattern)
  - `Research/backlog/2026-02-27-local-database.md` (database technology options)
  - `Research/backlog/2026-03-02-chat-conversational-interface.md` (downstream consumer of search)
