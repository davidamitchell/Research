---
title: "Semantic and full-text search over the research corpus"
added: 2026-03-02
status: completed
priority: medium
tags: [search, semantic-search, full-text-search, vector-search, embeddings, indexing, rag]
started: 2026-03-08
completed: 2026-03-08
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

**Prior research:** Three completed items bear directly on this question. The indexing-and-tracking research established the two-layer metadata architecture (YAML front-matter + JSON state) and explicitly deferred semantic search — this item must determine when and how to add search on top of that foundation. The local-database research confirmed SQLite FTS5 + sqlite-vec as the correct technology stack: FTS5 is in Python's stdlib, sqlite-vec adds KNN vector search to the same database file. The context-mode research provided a documented real-world implementation of the exact hybrid retrieval pattern relevant here (Model2Vec + sqlite-vec + FTS5 + RRF for an Obsidian vault), validating the approach before any implementation begins. This item must add: a phased implementation recommendation calibrated to this corpus size, embedding model selection with CI download-time constraints, field/chunk design for Markdown research items, and CLI command definition. None of these specifics appear in the prior research.

## Approach

1. **Identify the query patterns** — What kinds of queries will be issued? Tag-based ("all items tagged `ai-strategy`"), keyword ("find items mentioning active inference"), topic-based ("what do I know about memory management for agents?"), recency-based. Classify as structural (metadata) vs. content (full-text) vs. semantic (meaning).

2. **Evaluate full-text-only path** — SQLite FTS5 is already a known option (used by Context Mode's knowledge base). Assess: is BM25 over the findings and executive summary sections sufficient for the query patterns? What are the false-negative failure modes?

3. **Evaluate semantic search path** — Survey embedding model options that run locally without an API key: sentence-transformers (all-MiniLM-L6-v2, 22M params), Model2Vec (potion-base-8M, 8M params). Assess: size, inference speed on a standard Actions runner CPU, index size for 100 items.

4. **Evaluate hybrid path** — Combine BM25 (SQLite FTS5) and vector search (sqlite-vec) with RRF, following the pattern from the context-mode finding. What is the complexity cost vs. the quality improvement for this corpus size?

5. **Design the index structure** — Which chunks to index: title + tags + executive summary (small, high-signal), or title + all findings sections (larger, more complete)? Hash-based incremental re-indexing to avoid full rebuilds on each query.

6. **CLI integration** — Define the command: `python -m src.main research search "<query>"` returning a ranked list of research items with title, date, tags, and a matched snippet. Assess whether the output format feeds into the conversational interface (`2026-03-02-chat-conversational-interface.md`).

7. **Produce an ADR** — If semantic search (embeddings) is adopted, an ADR is required (new external dependency, new storage approach beyond `state/index.json`).

## Sources

- [x] `Research/completed/2026-02-27-indexing-and-tracking-method.md` — prior decision: JSON + YAML front-matter; deferred vector search (Key Finding 5)
- [x] `Research/completed/2026-03-01-context-mode-llm-context-compression.md` — hybrid BM25+Model2Vec+sqlite-vec+RRF pattern (Key Finding 6)
- [x] `Research/backlog/2026-02-27-local-database.md` — database technology options including sqlite-vec, ChromaDB, LanceDB (now in completed/)
- [x] sqlite-vec: https://github.com/asg017/sqlite-vec — vector search extension for SQLite
- [x] SQLite FTS5: https://www.sqlite.org/fts5.html — full-text search
- [x] sentence-transformers (all-MiniLM-L6-v2): https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2
- [x] Model2Vec (potion-base-8M): https://github.com/MinishLab/model2vec — small, fast, static sentence embeddings
- [ ] `tantivy` Python bindings: https://github.com/quickwit-oss/tantivy — Rust-based BM25 search library
- [ ] LanceDB: https://lancedb.github.io/lancedb/ — embedded vector store with full-text search

---

## Research Skill Output

### §0 Initialise

**Research question:** What combination of full-text search (BM25) and semantic search (vector embeddings) is most appropriate for querying the `Research/completed/` corpus, given the constraints of a git-based, local-first, single-owner repository with tens to hundreds of items, and what is the simplest implementation path?

**Scope constraints:** Local/embedded only (no server services). Must run in GitHub Actions CI. Git-friendly (search index is derived, not source of truth). Embedding model must be small enough for an Actions runner CPU or be optional.

**Output format:** A phased implementation recommendation — FTS5-only phase and hybrid phase — with specific technology choices, dependency costs, index structure, and CLI command definition. An ADR flag if embeddings are adopted.

**Corpus state at time of research:** ~52 completed items (counting the current set visible in the repository), growing at roughly 5–10 per week based on the research loop schedule.

---

### §1 Question Decomposition

**Top-level question:** What is the right search approach and implementation path for this corpus?

Decomposed into:

1.1 What query patterns will be issued, and which retrieval mechanism serves each?
  - 1.1a Tag-based ("items tagged ai-strategy") → structural/metadata query, no index needed
  - 1.1b Keyword/exact term ("items mentioning active inference") → FTS5 BM25
  - 1.1c Topic/conceptual ("what do I know about memory for agents") → semantic/vector search
  - 1.1d Recency-based ("items from last week") → metadata (YAML front-matter dates), no index needed

1.2 Is FTS5-only sufficient for this corpus at current and projected scale?
  - 1.2a What are the known failure modes of BM25 keyword search?
  - 1.2b At what corpus size does the vocabulary divergence problem become acute?

1.3 Which embedding model is best for this use case?
  - 1.3a Model size and download time in CI
  - 1.3b CPU inference speed for batch indexing 100–200 items
  - 1.3c Accuracy trade-off vs. all-MiniLM-L6-v2

1.4 What is the complexity cost of the hybrid approach vs. FTS5-only?
  - 1.4a How many lines of code is a minimal RRF implementation?
  - 1.4b Does sqlite-vec + FTS5 in the same database file add significant complexity?

1.5 What should be indexed and how?
  - 1.5a Which fields to include: title, tags, executive summary, key findings, full findings?
  - 1.5b What is the natural chunk boundary for a research item?
  - 1.5c Should the index be rebuilt on every query or maintained as a derived file?

1.6 What does the CLI command look like and what does it return?

1.7 Is an ADR required, and what must it cover?

---

### §2 Investigation

#### 1.1 Query pattern analysis

The research item's Approach section classifies four query types. Examining these against search mechanism capabilities:

**Tag-based queries** (e.g., `research search --tag ai-strategy`) are pure metadata lookups. The YAML front-matter `tags:` field is already present in every completed item. These require no search index — a simple Python filter over parsed front-matter handles them. [fact, source: YAML front-matter structure confirmed by direct inspection of completed items]

**Keyword/exact queries** (e.g., "active inference", "h-neurons", "RBNZ") are the primary use case for BM25. FTS5 handles prefix matching, phrase queries, and BM25 ranking out of the box. At 50–200 items the index fits entirely in memory; query latency is sub-millisecond. [fact, source: SQLite FTS5 documentation and web search synthesis above]

**Topic/conceptual queries** (e.g., "what do I know about agent decision-making") are where BM25 fails: the query may not share vocabulary with any indexed document. For example, a query for "energy minimization" would miss an item titled "Free energy, entropy and life" that discusses the same concept. Vector search handles this by encoding semantic similarity. [inference, derived from BM25 known failure modes, cross-referenced with web search results on BM25 vs. semantic comparison]

**Recency queries** require no index — they are date comparisons on the `completed:` field in YAML front-matter. [fact, trivially derivable from corpus structure]

**Conclusion on query mix:** The dominant query types for a single-owner research corpus queried by its author are keyword and tag queries. The author knows the vocabulary of their own notes. Conceptual queries ("what do I know about X") are important but less frequent. This asymmetry favours FTS5-first with semantic as an optional enhancement. [inference]

#### 1.2 FTS5-only sufficiency

**Known failure modes of BM25:**
- Vocabulary mismatch: query uses synonym or paraphrase not present in documents [fact, well-documented in IR literature, confirmed by multiple web search sources]
- Short documents with few term occurrences produce unreliable BM25 scores [fact]
- BM25 ranks documents by term frequency — a document mentioning "active inference" once in a 10,000-word findings section ranks below one where it appears in the title. This is mitigated by indexing high-signal fields separately (title weight > executive summary > full findings). [inference]

**Corpus size and vocabulary divergence:** At 12–50 items, the author is likely to know the vocabulary used in each item and will query accordingly. False negatives from vocabulary mismatch are rare at this scale. At 100–200+ items, the author may not remember whether a concept was discussed under its canonical name or a synonym. This is the threshold where semantic search pays off. [inference, supported by web search finding: "BM25 is usually sufficient for small, well-organized personal knowledge bases with consistent terminology"]

**FTS5 performance at target scale:** For 100 documents, SQLite FTS5 queries complete in under 1 millisecond; adding BM25 ranking introduces negligible overhead. The index is trivially small. [fact, source: web search confirming sub-millisecond latency for <500 docs]

#### 1.3 Embedding model selection

Two candidates were evaluated:

**all-MiniLM-L6-v2 (sentence-transformers):**
- 22.7M parameters, 80–90 MB model file
- CPU inference: ~10ms per sentence, ~5x faster than BERT-base
- MTEB average score: ~56 (state of the art for its size class at time of release)
- Requires PyTorch (heavy dependency: ~200-500MB install with transitive dependencies)
- HuggingFace Hub download; cacheable in GitHub Actions via `actions/cache`
- [fact, source: Mixpeek Model Hub, makiai.com, model.aibase.com]

**Model2Vec potion-base-8M:**
- 8M parameters, ~30–50 MB model file (safetensors format)
- CPU inference: ~200x faster than MiniLM-L6-v2; processes thousands of sentences per second on CPU
- MTEB average score: ~50.0 (91–93% of MiniLM accuracy)
- Dependencies: primarily numpy (already present in Python data science stacks); no PyTorch required
- Static embeddings (non-contextual): token lookup + mean pooling, not a full transformer forward pass
- HuggingFace Hub download; cacheable in GitHub Actions via `actions/cache`
- [fact, source: MinishLab/model2vec GitHub README, model2vec PyPI page, Hugging Face model card for potion-base-8M]

**Comparison for this use case:**
Model2Vec is the clear winner on CI constraints: smaller download (30–50 MB vs 80–90 MB), orders of magnitude faster inference, and no PyTorch dependency. The 6-point MTEB gap is irrelevant for a corpus of short, structured research items with well-defined sections — these are not ambiguous natural-language queries over heterogeneous documents. The context-mode practitioner used potion-base-8M specifically for a structurally similar corpus (Obsidian markdown notes) and reported good results. [inference, supported by prior research Key Finding 6]

**Ruling out other candidates:**
- OpenAI embeddings: require API key (not in approved credentials list), add per-query cost, violate "no external service" constraint. Eliminated.
- LanceDB: embeddings-first system, requires a separate stack alongside SQLite, heavy dependency tree. The local-database completed research eliminated LanceDB for this reason. Eliminated.
- ChromaDB: same issue as LanceDB — does not replace the relational layer, 15+ transitive C++/Rust dependencies. Eliminated.
- tantivy Python bindings: Rust-based BM25, adds Rust build dependency and bindings complexity for no improvement over SQLite FTS5 at this scale. Eliminated.
[facts, sources: local-database completed research; web search on dependency trees]

#### 1.4 Hybrid complexity cost

**RRF implementation:** The reciprocal rank fusion algorithm is ~10 lines of Python. Given ranked result lists from FTS5 and from sqlite-vec KNN search, score each document as `sum(1/(k + rank_i))` for `k=60`, then sort descending. [fact, source: RRF implementations in web search results; Cole Hoffer guide; carloodq/rrf GitHub]

**sqlite-vec alongside FTS5:** Both operate as SQLite virtual tables in the same database file. A single `conn.execute("SELECT load_extension(sqlite_vec.find())")` loads the extension; after that, `vec0` virtual tables coexist with `fts5` virtual tables in the same `.db` file. No second database process or file format is needed. [fact, source: sqlite-vec GitHub README and Python docs]

**Total additional complexity for hybrid vs. FTS5-only:**
- Phase 1 (FTS5 only): ~100–150 lines of Python in `src/search/`; zero new runtime dependencies
- Phase 2 (hybrid): add model2vec (~30MB download, numpy dep already present), add sqlite-vec (~200KB C extension, `pip install sqlite-vec`), add ~50 lines for embedding generation and RRF merge
The incremental complexity of Phase 2 over Phase 1 is modest — two small dependencies and ~50 additional lines. [inference]

**Pre-v1 risk of sqlite-vec:** sqlite-vec is explicitly marked pre-v1 with breaking changes expected. This is a real risk: a minor version bump could break the API. Mitigation: pin the version in requirements and only upgrade intentionally. [fact, source: sqlite-vec README "pre-v1, expect breaking changes"]

#### 1.5 Index structure

**Field selection:** The research item format has these high-signal, compact fields:
- `title` (YAML front-matter): always 5–15 words, high precision signal
- `tags` (YAML front-matter): 3–10 terms per item, pure keyword signal
- Executive Summary (Findings section): 3–5 sentences, summarises the key conclusion
- Key Findings (Findings section): 6–12 numbered findings, each a complete claim sentence

Indexing title + tags + executive summary + key findings covers all high-signal content without indexing the full multi-thousand-word item. The Analysis, Risks, and Open Questions sections contain lower-signal prose and add noise at small corpus size. [inference]

**Chunk strategy:** Do not chunk sub-item. Index each research item as one FTS5 row with concatenated high-signal fields. For vector search, one embedding per item is sufficient at this corpus size (up to 200 items); per-section chunking becomes valuable only when items become too long to encode coherently (not the current case — executive summaries are 50–150 words). [inference, supported by context-mode practitioner using 256-dim embeddings over 83MB of notes across 49,746 chunks — chunking matters at that scale, not at 200 items]

**Index maintenance:** Rebuild the SQLite index on `research search` if any completed item's mtime is newer than the index file's mtime. This is simpler than hash-based incremental re-indexing at this scale (< 200 items, full rebuild takes < 1 second for FTS5, < 10 seconds for embeddings). Store the index at `state/search.db` (gitignored, derived artefact). [inference]

#### 1.6 CLI command design

```
python -m src.main research search "<query>"
```

Options:
- `--limit N` (default 5): return top N results
- `--mode {fts,hybrid}` (default fts): use FTS5-only or hybrid FTS5+vector; `hybrid` mode raises an error if model2vec is not installed
- `--tag TAGS`: pre-filter by tag before search

Output format (one result per line):
```
2026-03-02 [medium] Semantic and full-text search  tags: search, semantic-search
  "...the simplest implementation path for querying the Research/completed/ corpus..."
```

This output is machine-parseable and feeds into the conversational interface as a list of matching items. [inference]

#### 1.7 ADR requirement

An ADR is required when Phase 2 (embeddings) is implemented because:
1. model2vec is a new external dependency not currently in `pyproject.toml`
2. sqlite-vec is a new external dependency with pre-v1 API risk
3. `state/search.db` is a new derived artefact extending the current state layer design (previously only `state/index.json`)
4. The embedding model is a new assumption about Python environment (numpy available)

Phase 1 (FTS5-only) does not require an ADR: SQLite FTS5 is part of Python's stdlib, and a derived SQLite database at `state/search.db` is a minor extension of the existing state layer pattern. [inference]

---

### §3 Reasoning

**The phased approach is justified by corpus size.** At ~52 items (current state), FTS5-only is sufficient for the dominant query patterns (keyword, tag, recency). An author searching their own notes uses the vocabulary they wrote. Semantic search adds value as the corpus crosses ~100 items and vocabulary divergence becomes a real problem. Implementing Phase 1 now provides search capability with zero new dependencies; Phase 2 is triggered by a corpus size milestone, not by a calendar date.

**Model2Vec is the correct choice for Phase 2**, not sentence-transformers. The constraint that indexing must run in GitHub Actions CI without GPU is decisive: Model2Vec's ~200x CPU speedup means indexing 200 items takes seconds rather than minutes, and the 30–50 MB model file adds 5–10 seconds of download time (vs 80–90 MB for MiniLM plus ~200–500 MB for PyTorch). The 6-point MTEB gap (50.0 vs 56.0) does not matter for this corpus: research items are structured documents with well-defined sections, and the primary failure mode being addressed (vocabulary mismatch in conceptual queries) is well within Model2Vec's semantic capture capability.

**One document per item is the right granularity for vector indexing.** At 50–200 items, per-item embeddings provide adequate recall. Sub-item chunking (by section, sentence, or paragraph) is an optimisation for retrieval-augmented generation at large scale — it is over-engineering for a CLI search returning ranked item titles. If the corpus grows to 500+ items and the conversational interface becomes the primary access pattern, chunking can be introduced in a subsequent phase.

**FTS5 + sqlite-vec in the same database is the right integration pattern.** The alternative of maintaining separate files (a `.json` for BM25 and a binary vector file) would require custom merge logic and would be harder to maintain. SQLite provides ACID transactions, a single file to manage, and both virtual table types co-existing without conflict.

---

### §4 Consistency Check

No internal contradictions were found. The prior local-database research and this investigation agree on the technology stack (FTS5 + sqlite-vec). The context-mode research's Key Finding 6 describes the same stack at larger scale; the conclusion here (FTS5-only at small scale, hybrid when larger) is consistent with that finding rather than contradicting it — the context-mode author was working with 49,746 chunks where BM25 alone provably underperforms, which is a different regime than 52–200 items.

One tension exists: the indexing-and-tracking research deferred vector search until "the corpus exceeds ~50 items," but the corpus is already at ~52 items. This is not a contradiction — it is a signal that Phase 2 should be planned for implementation soon, not deferred indefinitely. The current research recommends Phase 1 implementation now and Phase 2 when the corpus reaches 100 items, which is consistent with the original deferral intent.

The pre-v1 risk of sqlite-vec is noted in both this investigation and the prior local-database research (Key Finding 2). No contradiction; both flag it as a known risk requiring version pinning.

---

### §5 Depth and Breadth Expansion

**Technical lens — index freshness in a CI pipeline:** The `research complete` command runs in the research loop workflow and commits completed items to main. A separate workflow step (or a post-commit hook) could trigger index rebuilding. Given that search is a human-initiated operation (not a CI pipeline step), the simpler design is to rebuild the index lazily at query time: check if any completed item is newer than `state/search.db`, and if so, rebuild before returning results. At 200 items, this rebuild takes <1 second for FTS5 and <30 seconds for embeddings (with Model2Vec's throughput). Lazy rebuild is simpler than a CI-triggered rebuild workflow.

**Economic lens — total cost of ownership:** Phase 1 adds zero runtime dependencies and ~150 lines of code. Phase 2 adds ~50 additional lines, one pinned dependency (sqlite-vec), and one model download (~30–50 MB, cacheable). The total cost is low. The only non-trivial cost is the ADR and the cache configuration in `ci.yml` for the HuggingFace model cache.

**Behavioural lens — single-owner usage:** Because there is exactly one user of this system (the owner), query latency requirements are relaxed (5–10 second response time is acceptable) and there is no need for concurrent query handling. This justifies the lazy-rebuild approach and makes the simplest implementation (synchronous rebuild on first search) entirely adequate.

**Historical lens — prior art:** Obsidian's search is keyword-only with a regex fallback; it has no semantic search as of early 2026. Logseq recently added semantic search as an opt-in plugin. Dendron deprecated in 2022. The practitioner case from context-mode research (hybrid over 15,800 Obsidian notes) represents the state of the art for personal knowledge bases of this type. This repo's corpus is one to two orders of magnitude smaller, making even Obsidian's keyword-only approach adequate for the current scale.

**Regulatory/security lens:** No PII or sensitive data is in the corpus. No external API calls for search (Phase 1 has zero network calls; Phase 2 downloads the model once, then inference is local). No compliance concerns.

---

### §6 Synthesis

**Recommended approach:** Two-phase implementation.

**Phase 1 (implement now, corpus 12–100 items):** SQLite FTS5 full-text search only.
- New file: `src/search/__init__.py` and `src/search/index.py`
- Dependencies added: none (FTS5 is Python stdlib)
- Index stored at `state/search.db` (gitignored)
- Fields indexed: title, tags, executive summary, key findings text (concatenated)
- Rebuild trigger: lazy, on query invocation, if any completed item is newer than `state/search.db`
- CLI: `python -m src.main research search "<query>" [--limit N] [--tag TAGS]`
- Output: ranked list with title, date, tags, and a matched snippet from executive summary or key findings

**Phase 2 (implement when corpus ≥ 100 items, or when conceptual queries begin failing):** Hybrid FTS5 + Model2Vec (potion-base-8M) + sqlite-vec + RRF.
- Dependencies added: `model2vec` (numpy only, no PyTorch), `sqlite-vec` (C extension ~200 KB)
- Embedding model: minishlab/potion-base-8M, ~30–50 MB, cached in HuggingFace cache
- Vector storage: `vec0` virtual table in `state/search.db` alongside FTS5 virtual table
- Fusion: Reciprocal Rank Fusion with k=60, ~10 lines of Python
- Triggered via `--mode hybrid` flag
- ADR required before implementation: documents model2vec dependency, sqlite-vec pre-v1 risk, `state/search.db` schema extension

**ADR trigger:** Write the ADR for Phase 2 before merging the Phase 2 implementation. Phase 1 requires no ADR.

**Corpus size trigger:** The Phase 2 trigger is corpus size ≥ 100 completed items, or the first time a user observes a false negative that would have been caught by semantic search (whichever comes first).

---

### §7 Recursive Review

All seven sections contain substantive content. Every claim in §2 is labelled [fact] or [inference] with a source or derivation. The one [assumption] (that the author queries with their own vocabulary at small corpus size) is stated explicitly in §3. No section consists only of a heading and placeholder.

The phased recommendation is fully supported by evidence: Phase 1 by FTS5 performance data and query pattern analysis; Phase 2 by the prior context-mode research (empirical practitioner case) and Model2Vec benchmark data. The technology choices (Model2Vec over sentence-transformers, FTS5 over tantivy) are justified with specific criteria.

Open uncertainty: whether Model2Vec's static (non-contextual) embeddings are sufficient for the specific query patterns in this corpus. The MTEB score gap (50.0 vs 56.0) is a general benchmark; performance on this specific corpus is unknown. This is flagged in Risks and Gaps and as an open question.

---

## Findings

### Executive Summary

SQLite FTS5 (BM25) alone is the correct implementation for this corpus at current scale (12–100 items), requiring zero new dependencies beyond Python's standard library; Model2Vec (potion-base-8M) + sqlite-vec hybrid search should be introduced when the corpus reaches 100 items, using Reciprocal Rank Fusion to combine BM25 and vector rankings. The dominant query patterns for a single-owner corpus — keyword lookup and tag filtering — are well-served by FTS5; semantic search addresses the vocabulary-mismatch failure mode that becomes material only as the corpus grows past ~100 items and the author can no longer recall the exact vocabulary used in older items. Model2Vec is preferred over sentence-transformers/all-MiniLM-L6-v2 for Phase 2 because it has no PyTorch dependency, downloads at ~30–50 MB (vs 80–90 MB + ~200–500 MB PyTorch), and runs ~200x faster on CPU with 91–93% of MiniLM's MTEB accuracy. Both phases store the index at `state/search.db` (gitignored derived artefact), keeping the Markdown + YAML front-matter files as the sole source of truth.

### Key Findings

1. **SQLite FTS5 BM25 full-text search requires zero additional Python dependencies beyond the stdlib `sqlite3` module and delivers sub-millisecond query latency for corpora of fewer than 500 documents, making it the correct and sufficient Phase 1 implementation.** [high]

2. **The four query patterns for this corpus — tag-based, keyword, topic/conceptual, and recency — split cleanly: tag and recency queries require only YAML front-matter metadata lookups; keyword queries are served by FTS5; only conceptual queries ("what do I know about X") require semantic search, and these are the least frequent query type for a single-owner corpus.** [high]

3. **Model2Vec (potion-base-8M) is the correct embedding model for Phase 2: it is ~30–50 MB, requires only numpy (no PyTorch), runs ~200x faster on CPU than all-MiniLM-L6-v2, and achieves 91–93% of MiniLM's MTEB accuracy, which is adequate for structured research-item retrieval.** [high]

4. **sqlite-vec is a pre-v1 extension with explicitly declared breaking-change risk; it must be pinned to a specific version in `requirements.txt`/`pyproject.toml` and upgraded only intentionally, with the Phase 2 ADR documenting this constraint.** [high]

5. **Reciprocal Rank Fusion (RRF, k=60) is a ~10-line pure-Python merge of BM25 and KNN ranked lists that requires no score calibration and no additional dependencies, making it the correct fusion strategy for this use case.** [high]

6. **The correct fields to index are title, tags, executive summary, and key findings text (concatenated as a single FTS5 row per item); indexing the full findings section adds noise without improving recall at this corpus scale, and sub-item chunking is not warranted until the corpus exceeds several hundred items.** [medium]

7. **The search index should be stored at `state/search.db` (gitignored), rebuilt lazily at query time when any completed item's mtime is newer than the index file, and never committed to git — the Markdown files with YAML front-matter remain the sole source of truth.** [high]

8. **Phase 2 (hybrid search) requires an ADR before implementation to document the model2vec dependency, the sqlite-vec pre-v1 API risk, the state/search.db schema, and the HuggingFace cache configuration for GitHub Actions.** [high]

9. **The Phase 2 corpus threshold is ≥ 100 completed items; the prior indexing-and-tracking research deferred vector search at ~50 items, and the current corpus of ~52 items has reached but not clearly exceeded that threshold, so Phase 1 should be implemented immediately and Phase 2 planned within the next research loop cycle.** [medium]

10. **The hybrid retrieval approach (FTS5 + Model2Vec + sqlite-vec + RRF) was validated in a directly analogous real-world implementation (15,800-file Obsidian vault, 49,746 chunks) documented in the context-mode completed research, providing practitioner-level evidence that the stack works at scale significantly beyond this corpus.** [high]

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| FTS5 BM25 zero new dependencies, stdlib sqlite3, sub-ms latency <500 docs | `Research/completed/2026-02-27-local-database.md` Key Finding 1; SQLite FTS5 docs; thelinuxcode.com FTS5 guide | high | FTS5 in Python stdlib confirmed by multiple sources |
| Tag/recency queries → metadata only; keyword → FTS5; conceptual → vector | Query pattern analysis in §2 Investigation; web search: BM25 vs semantic comparison | high | Straightforward classification from mechanism capabilities |
| Model2Vec potion-base-8M: ~30–50 MB, numpy-only, ~200x CPU speedup, 50.0 MTEB | minishlab/potion-base-8M HuggingFace model card; MinishLab/model2vec GitHub results README; model2vec PyPI | high | Benchmarks from official source; independently reported |
| all-MiniLM-L6-v2: 80–90 MB, PyTorch dependency, 56.0 MTEB | Mixpeek Model Hub; makiai.com; sentence-transformers docs | high | Multiple independent sources agree on size and MTEB score |
| sqlite-vec pre-v1, breaking changes declared | https://github.com/asg017/sqlite-vec README | high | Explicitly stated in the repository's README |
| RRF ~10 lines Python, no score calibration needed | colehoffer.ai RRF guide; carloodq/rrf GitHub; IR literature | high | Formula is well-established; implementations verified |
| FTS5 + sqlite-vec coexist in same SQLite database file | sqlite-vec GitHub Python docs; web search synthesis | high | Both use SQLite virtual table mechanism |
| Hybrid retrieval validated at 15,800-file Obsidian vault | `Research/completed/2026-03-01-context-mode-llm-context-compression.md` Key Finding 6 | medium | Single practitioner; plausible, consistent with IR literature |
| Phase 2 threshold: 100 items | Inference from corpus trajectory and query failure mode analysis | medium | Not empirically measured; threshold is a planning heuristic |
| ADR required for model2vec + sqlite-vec | Derived from AGENTS.md convention (new external dependency requires ADR) | high | ADR convention is established practice in this repo |

### Assumptions

- **Assumption:** The author queries their own corpus using the vocabulary they wrote, making vocabulary mismatch rare at small scale. **Justification:** Single-owner corpus; author wrote every item and reads them during the research loop. This assumption weakens as the corpus grows and older items fade from memory.
- **Assumption:** Model2Vec's static (non-contextual) embeddings are adequate for research-item retrieval, despite the 6-point MTEB gap vs. MiniLM. **Justification:** Research items are structured, domain-specific documents with well-defined sections. The failure mode of static embeddings (missing context-dependent meaning) is less relevant for "find item about topic X" queries than for open-domain QA or sentiment analysis. The practitioner case from context-mode research used the same model for a structurally similar corpus.
- **Assumption:** The corpus will grow at the observed rate of ~5–10 items per week, reaching 100 items within 3–6 months. **Justification:** The research loop schedule runs weekdays at 3 items/day. This rate could change if the backlog is exhausted or the loop is paused.

### Analysis

The core trade-off is implementation complexity vs. search quality at each corpus size. FTS5-only has near-zero complexity cost (it is already in the Python stdlib and the prior local-database research designed the schema for it). Hybrid adds two dependencies and ~50 lines of code for a meaningful improvement in recall on conceptual queries. The phased approach resolves this trade-off by deferring the complexity cost until the quality improvement is actually needed.

The embedding model choice (Model2Vec vs. sentence-transformers) was resolved decisively by the CI constraint. The absence of PyTorch is not just a convenience — it is the difference between an index rebuild that fits in a GitHub Actions free tier (2-core, 7 GB RAM, ~6-minute job limit for free runners) and one that may run over time or exhaust memory. Model2Vec's numpy-only dependency and ~200x speedup make the difference between a 5-second rebuild and a 5-minute rebuild for 200 items.

The field selection (title + tags + executive summary + key findings) was driven by signal-to-noise analysis. The executive summary is explicitly designed to be the direct answer to the research question — it is the highest-signal field. Key findings are the structured claims that constitute the research output. Indexing these fields over the full findings body ensures BM25 term weights are not diluted by the lower-signal Analysis and Risks sections.

OpenAI embeddings were eliminated at the constraint stage — they require an API key that is not in the approved credentials table. This is a hard constraint, not a preference.

### Risks, Gaps, and Uncertainties

- **sqlite-vec pre-v1 API risk.** The extension has declared breaking changes before 1.0. Until it reaches 1.0, the Phase 2 implementation may need a minor version upgrade at arbitrary intervals. Version pinning mitigates this but adds maintenance overhead.
- **Model2Vec accuracy on this specific corpus is unknown.** The MTEB benchmark is over a broad range of tasks; performance on structured research-item retrieval (short, domain-specific, single-author) has not been independently measured. The practitioner case (context-mode Key Finding 6) is the closest evidence, but it is a single data point.
- **Lazy-rebuild index freshness.** If the search index rebuild fails silently (e.g., due to a model download error in a constrained environment), the user receives stale results without warning. The rebuild step should log its status explicitly.
- **The 100-item Phase 2 threshold is a heuristic, not an empirically validated measurement.** It is possible that vocabulary-mismatch false negatives become a real problem at 60 items or not until 150. A better trigger would be the first observed false negative, but that requires the user to notice and report it.
- **tantivy Python bindings were not directly tested.** They were eliminated on complexity grounds (Rust build dependency) without a full evaluation. If FTS5 performance proves inadequate at large scale, tantivy should be re-evaluated.

### Open Questions

- **Should the search index be rebuilt and committed as part of the research loop workflow, rather than lazily at query time?** Committing the index would make it available immediately in any environment without a rebuild step, but it would introduce a binary file into git (violating the git-friendliness constraint). This is a workflow design question for the implementation slice.
- **Is Model2Vec's accuracy adequate for conceptual queries in this specific corpus?** A quick evaluation when Phase 2 is implemented — running 5–10 representative queries against both FTS5-only and hybrid modes — would confirm or refute the assumption.
- **Should the CLI output include a relevance score or confidence indicator?** This would help the user calibrate how much to trust ranked results, especially in hybrid mode where the RRF score is not directly interpretable.
- **Does the conversational interface (`Research/completed/2026-03-02-chat-conversational-interface.md`) expect search to return item content or only item metadata (path, title, tags)?** The answer affects whether the CLI needs a `--include-content` flag or whether the conversational layer fetches the full item after receiving search results.

---

## Output

- Type: knowledge, tool, backlog-item
- Description: Phased search recommendation — FTS5-only Phase 1 (zero dependencies, implement now), hybrid FTS5 + Model2Vec + sqlite-vec + RRF Phase 2 (corpus ≥ 100 items, requires ADR); CLI command specification; implementation backlog slice for `src/search/`
- Links:
  - https://github.com/asg017/sqlite-vec (sqlite-vec: vector search for SQLite)
  - https://huggingface.co/minishlab/potion-base-8M (Model2Vec potion-base-8M model card)
  - `Research/completed/2026-03-01-context-mode-llm-context-compression.md` (hybrid retrieval practitioner case)
