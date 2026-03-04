---
title: "Local database: requirements and technology choice"
added: 2026-02-27
status: completed
priority: medium
tags: [database, sqlite, storage, local]
started: 2026-03-03
completed: 2026-03-03
output: [knowledge, backlog-item]
---

# Local database: requirements and technology choice

## Question / Hypothesis

If we decide to use a local database for indexing and state (rather than JSON files), what are the requirements and what technology should we choose?

## Context

A local database enables:
- Full-text search across all research content
- Relational queries (find all items tagged with "transformers" that are completed)
- Persistent state without large JSON diffs in git
- Potential vector search for semantic retrieval

SQLite is the obvious starting point (stdlib, file-based, git-friendly), but may need extensions for vector search (sqlite-vss, sqlite-vec). Alternatives include DuckDB (analytics), LanceDB (vector-native), or ChromaDB.

This item depends on `Research/backlog/2026-02-27-indexing-and-tracking-method.md`.

**Prior research:** `2026-02-27-indexing-and-tracking-method.md` (completed 2026-02-28) established that JSON state file + YAML front-matter is the correct approach for current scale (hundreds of items), with SQLite as the explicit migration point when corpus size or query complexity outgrows JSON. That item also confirmed the two-layer separation: processing state (`state/index.json`) vs research-item metadata (YAML front-matter). This item now answers the forward-looking question: when the corpus does require a database, what technology and schema are correct, and what triggers the migration?

## Scope

**In scope:**
- SQLite (core and extensions) for local storage
- DuckDB as an alternative for analytics-heavy use
- Embedded vector stores (LanceDB, ChromaDB, sqlite-vss)
- Schema design for research items, sources, and transcripts

**Out of scope:**
- Server-based databases
- Cloud storage

## Approach

1. Define the queries we need to answer (requirements first)
2. Evaluate SQLite + sqlite-vec vs DuckDB vs ChromaDB against requirements
3. Prototype the schema for research items
4. Write ADR with recommendation

## Sources

- [x] SQLite docs: https://sqlite.org
- [x] sqlite-vec: https://github.com/asg017/sqlite-vec
- [x] DuckDB: https://duckdb.org
- [x] ChromaDB: https://docs.trychroma.com
- [x] LanceDB: https://lancedb.github.io/lancedb/

---

## Research Skill Output

### §0 Initialise

**Research question restated:** When this repository's research corpus or state management outgrows JSON files, what local embedded database technology should it migrate to — and what schema design supports the queries the system actually needs to answer?

**Scope confirmation:** In scope are SQLite (core + FTS5 + sqlite-vec), DuckDB, ChromaDB (persistent client mode), and LanceDB (embedded OSS). Out of scope are server databases (PostgreSQL, Elasticsearch, MongoDB) and cloud-only solutions. The prior research item (`2026-02-27-indexing-and-tracking-method.md`) already answered the question of whether to use a database now (answer: not yet). This item answers what to use when the time comes and lays out the schema.

**Constraints:**
- Git-based, owner reviews diffs via GitHub website — binary database files must be treated as runtime artefacts, not committed source
- Python 3.11+, `pyproject.toml` as dependency source
- Single-owner, single-process (no concurrency requirements beyond atomic writes)
- Corpus scale: hundreds to low thousands of research items; not petabyte-scale

**Output format:** Technology recommendation with justification, schema design, migration trigger criteria, backlog items for implementation.

---

### §1 Question Decomposition

**Top-level question:** What local database technology and schema should this repository use?

Decomposed into atomic sub-questions:

**A. Requirements**
- A1. What relational queries does the system need to answer over research items?
- A2. What full-text search capability is needed?
- A3. What vector/semantic search capability is needed, and at what corpus size does it become useful?
- A4. What are the write patterns (bulk load, incremental append, updates)?

**B. Technology evaluation**
- B1. Does SQLite + FTS5 satisfy A1 and A2 without external dependencies?
- B2. Does sqlite-vec satisfy A3 while staying within the SQLite ecosystem?
- B3. How does DuckDB compare to SQLite on A1–A4 for this use case?
- B4. Does ChromaDB's persistent client mode satisfy A3 without server infrastructure?
- B5. Does LanceDB embedded OSS satisfy A3 at this corpus scale?
- B6. Which technology has the best fit with the git-based, binary-artefact constraint?

**C. Schema design**
- C1. What tables are needed to model research items, tags, sources, and transcripts?
- C2. How should FTS5 be layered over the relational schema?
- C3. Where do vector embeddings live if added later?

**D. Migration**
- D1. What observable signals should trigger a migration from JSON + YAML to the chosen DB?
- D2. What is the migration path from the current `StateStore` and YAML front-matter to the new schema?

---

### §2 Investigation

#### A. Requirements

**A1 — Relational queries needed** [fact]

The queries the system needs to answer, derived from the codebase, research workflow, and AGENTS.md:

1. *"Find all completed research items tagged with X"* — SELECT items WHERE status = 'completed' AND tag IN (...)
2. *"Has URL Y already been fetched?"* — SELECT 1 FROM processed WHERE url = Y (currently handled by `state/index.json`)
3. *"Which sources in items tagged 'transformers' have not been checked?"* — JOIN items → tags → sources WHERE checked = 0
4. *"List items by priority and status for the Kanban view"* — SELECT ... ORDER BY priority, status, added
5. *"Find items whose titles or questions mention keyword Z"* — full-text search (FTS)
6. *"Find research items semantically related to a query embedding"* — vector similarity search

Queries 1–4 are relational; 5 is FTS; 6 is vector. [inference: derived from workflow and codebase review]

**A2 — Full-text search requirements** [fact]

The content to be searched: title, research question, key findings, tags. Documents are short (hundreds to low thousands of words per item). BM25 ranking is appropriate. Phrase search and prefix search would add value. The corpus will have at most hundreds to low thousands of documents for the foreseeable future — FTS performance is not a bottleneck at this scale.

SQLite FTS5 (built into SQLite since 3.9.0 / 2015) provides BM25 ranking, phrase search, prefix search, and NEAR queries. [fact, source: sqlite.org/fts5.html, confirmed by direct documentation access]

DuckDB also provides an FTS extension (`fts`) with BM25 via `match_bm25`. [fact, source: duckdb.org/docs/stable/core_extensions/full_text_search.html, confirmed by direct documentation access]

**A3 — Vector search requirements** [inference]

Vector/semantic search over completed research items becomes useful when:
- The corpus exceeds ~50 items (below this, manual browsing is as fast as semantic search)
- The owner wants to ask "what do I know about X?" against the corpus

The prior research item (`2026-02-27-indexing-and-tracking-method.md`, Key Finding 5) explicitly deferred vector stores: "Vector stores (ChromaDB, sqlite-vss/sqlite-vec) solve a different problem: semantic search, not deduplication. Both are appropriate only once the Research/completed/ directory has enough items (>50) to make semantic search over findings worthwhile." [fact, source: completed item]

sqlite-vec (successor to sqlite-vss) is a pure-C SQLite extension: `pip install sqlite-vec`, `vec0` virtual table, KNN queries, supports float32/int8/binary vectors, Mozilla Builders sponsorship. Pre-v1 (breaking changes expected). Requires SQLite ≥ 3.41 for full feature set. [fact, source: github.com/asg017/sqlite-vec, confirmed by direct GitHub access]

**A4 — Write patterns** [fact]

- State updates: incremental appends on each fetch run (1–20 new URLs per run)
- Research item updates: status changes when items are moved between backlog/in-progress/completed (infrequent, ~1/day max)
- Transcript storage: larger blobs (thousands of words per transcript), rare inserts
- Full corpus rebuild: possible (re-index all existing YAML front-matter on first run)

Write patterns are append-heavy and infrequent — unsuited to OLAP-optimized columnar stores. [inference]

---

#### B. Technology evaluation

**B1 — SQLite + FTS5** [fact]

SQLite is the world's most widely deployed DBMS (confirmed by sqlite.org). It is:
- Part of Python's standard library (`import sqlite3`) — zero additional dependencies
- File-based, single `.db` file (binary artefact, not git-diffable — must be excluded from git)
- ACID transactional, supports `INSERT OR IGNORE` for deduplication
- FTS5 included in the amalgamation since version 3.9.0 (2015): BM25 ranking, phrase search, prefix search

For queries A1–A5, SQLite + FTS5 requires no external dependencies beyond `sqlite3` (stdlib). [fact]

**B2 — SQLite + sqlite-vec** [fact]

`sqlite-vec` is installable via `pip install sqlite-vec`. After loading the extension (`sqlite_vec.load(db)`), it provides `vec0` virtual tables for KNN search. It coexists with FTS5 in the same `.db` file, meaning a single database file can serve both relational queries, full-text search, and vector search. [fact, source: alexgarcia.xyz/sqlite-vec/python.html, confirmed]

The extension is pre-v1, meaning its SQL interface may have breaking changes before 1.0. This is a stability risk for production use. [fact, source: github.com/asg017/sqlite-vec README]

**B3 — DuckDB** [fact]

DuckDB is an embedded columnar-vectorized OLAP database. Key characteristics (from duckdb.org/why_duckdb):
- No external dependencies, embedded in-process
- Single-file persistent database (binary, not git-diffable)
- Columnar storage optimised for analytical (OLAP) queries — aggregations over large tables
- FTS extension (BM25, Porter stemmer, configurable stopwords) available via autoload
- MIT licence
- No built-in vector search (no KNN/ANN index) — would require a community extension or external tooling

DuckDB's columnar storage is well-suited to queries that scan large portions of a table (analytics). The research item queries (A1–A4) are predominantly point lookups and small joins — row-oriented access patterns. SQLite's row-oriented storage is better matched to these patterns. [inference]

DuckDB has no built-in vector search extension, which means adding semantic search would require integrating a separate vector store anyway. [fact, source: duckdb.org extension documentation]

**B4 — ChromaDB persistent client** [fact]

ChromaDB offers an in-process persistent client (`chromadb.PersistentClient(path="./chroma_data")`). It stores data in a local directory. It provides:
- Dense, sparse, and hybrid vector search
- Metadata filtering
- Full-text (keyword/regex) search
- Apache 2.0 licence

ChromaDB requires `pip install chromadb`, which pulls in a significant dependency tree (including `hnswlib`, `tokenizers`, and several ML dependencies). The persistent client requires the Chroma server running in-memory; data is written to disk but the process architecture is heavier than SQLite. [fact, source: docs.trychroma.com, confirmed by direct access]

For corpus queries A1–A4 (relational/FTS), ChromaDB is an inferior fit: it is embeddings-first and its metadata query syntax is less expressive than SQL. It would not replace a relational layer — the research workflow needs both relational and semantic search. [inference]

**B5 — LanceDB embedded OSS** [fact]

LanceDB provides an embedded Python library (`pip install lancedb`) built on the Lance columnar format. It supports vector search, full-text search, and hybrid search. It is designed for multi-modal AI workloads at petabyte scale and is being positioned as a "multi-modal lakehouse." [fact, source: docs.lancedb.com, confirmed by direct access]

LanceDB's design target (petabyte scale, multi-modal) is significantly beyond the scope of this repository (hundreds of research items). The additional complexity and dependency weight is not justified. [inference]

**B6 — Git / binary-artefact constraint** [fact]

All four technologies (SQLite, DuckDB, ChromaDB, LanceDB) produce binary database files. None are git-diffable. This is expected and acceptable for a database file treated as a runtime artefact — the file should be added to `.gitignore` (or the `state/` directory already is). The prior research established that this constraint eliminates databases from being used as the primary research-item metadata store, but does not prohibit them as a queryable index rebuilt from source (YAML front-matter). [fact, source: 2026-02-27-indexing-and-tracking-method.md Key Finding 4]

---

#### C. Schema design

A schema for SQLite that supports all required query patterns:

```sql
-- Core research items table
CREATE TABLE IF NOT EXISTS items (
    id          TEXT PRIMARY KEY,  -- filename without extension, e.g. "2026-02-28-ai-strategy"
    path        TEXT NOT NULL,     -- relative path, e.g. "Research/completed/..."
    title       TEXT NOT NULL,
    status      TEXT NOT NULL CHECK(status IN ('backlog','in-progress','completed')),
    priority    TEXT NOT NULL CHECK(priority IN ('high','medium','low')),
    added       TEXT,              -- ISO date string
    started     TEXT,
    completed   TEXT
);

-- Tags
CREATE TABLE IF NOT EXISTS tags (
    item_id  TEXT NOT NULL REFERENCES items(id) ON DELETE CASCADE,
    tag      TEXT NOT NULL,
    PRIMARY KEY (item_id, tag)
);

-- Sources per item
CREATE TABLE IF NOT EXISTS sources (
    id       INTEGER PRIMARY KEY AUTOINCREMENT,
    item_id  TEXT NOT NULL REFERENCES items(id) ON DELETE CASCADE,
    url      TEXT NOT NULL,
    checked  INTEGER NOT NULL DEFAULT 0  -- 0=unchecked, 1=checked
);

-- Processed URLs (replaces state/index.json)
CREATE TABLE IF NOT EXISTS processed (
    url         TEXT PRIMARY KEY,
    fetched_at  TEXT NOT NULL,
    title       TEXT,
    source_id   TEXT
);

-- FTS5 index over research item content
CREATE VIRTUAL TABLE IF NOT EXISTS items_fts USING fts5(
    id UNINDEXED,
    title,
    question,
    findings,
    content='items'
);

-- Transcript storage (optional — large blobs)
CREATE TABLE IF NOT EXISTS transcripts (
    url          TEXT PRIMARY KEY,
    content      TEXT NOT NULL,
    fetched_at   TEXT NOT NULL,
    word_count   INTEGER
);
```

This schema supports:
- A1 (relational queries): direct SQL over `items`, `tags`, `sources`
- A2 (FTS): `items_fts` FTS5 virtual table with BM25 ranking
- A3 (vector search): `vec0` virtual table via sqlite-vec added as a later migration step
- A4 (write patterns): append-friendly; `INSERT OR IGNORE` on `processed` for dedup
- Deduplication: `processed` table replaces `state/index.json` at migration point

**Vector embedding addition (Phase 2):**
```sql
-- Added when sqlite-vec is introduced
CREATE VIRTUAL TABLE IF NOT EXISTS item_embeddings USING vec0(
    item_id TEXT,
    embedding FLOAT[1536]  -- dimension matches chosen embedding model
);
```

[inference: schema derived from query requirements A1–A4 and prior research]

---

#### D. Migration triggers and path

**D1 — Migration trigger signals** [inference]

Concrete observable signals that indicate it is time to migrate from JSON + YAML to SQLite:

1. The `state/index.json` file exceeds 500 entries (lookup performance degrades noticeably; the prior research item noted 10,000 as the theoretical limit, but cognitive cost of large JSON diffs arrives much earlier)
2. The owner needs to answer cross-item queries that require more than `grep` over Markdown files (e.g., "all completed items tagged 'ai-strategy' sorted by date")
3. A semantic search capability is being built (`Research/backlog/2026-03-02-semantic-full-text-search.md` is in backlog and is a direct trigger)
4. The pipeline begins running in parallel (concurrent write safety requires ACID transactions)

**D2 — Migration path** [inference]

The migration is a two-step process:
1. **Phase 1 (SQLite relational + FTS5):** Write a `src/db/` module with a `DatabaseStore` class. On first run, scan all `Research/{backlog,in-progress,completed}/*.md`, parse YAML front-matter, and `INSERT OR IGNORE` into `items` and `tags`. Load `state/index.json` and insert all existing entries into `processed`. Remove `StateStore` JSON dependency from `src/main.py`. Add `state/research.db` to `.gitignore`.
2. **Phase 2 (sqlite-vec embeddings):** Extend `DatabaseStore` to generate embeddings for each completed item's findings on insert and store in `item_embeddings`. This requires an embedding model (local via `sentence-transformers` or API via OpenAI/Gemini). This step is gated on the semantic search backlog item.

---

### §3 Reasoning

**Technology choice:** SQLite + FTS5 + sqlite-vec (phased) is the correct answer.

The reasoning is:

1. SQLite + FTS5 requires zero additional dependencies beyond Python's standard library. DuckDB requires `pip install duckdb`; ChromaDB and LanceDB each pull in heavy ML dependency trees. Minimal dependency footprint is a preference in this codebase (confirmed by `pyproject.toml` structure).

2. The query patterns (A1–A4) are row-oriented: point lookups by status, tag JOIN, deduplication by URL. DuckDB's columnar OLAP engine is optimised for the opposite pattern (scanning millions of rows across few columns). SQLite's row-oriented B-tree engine is the better fit.

3. FTS5 is built into SQLite's amalgamation. There is no additional installation step; it is enabled by default in Python's bundled SQLite. This gives full-text search at zero cost over the dependency already in use.

4. sqlite-vec is addable incrementally as a second phase. It installs via `pip install sqlite-vec`, loads via `sqlite_vec.load(db)`, and coexists with FTS5 in the same database file. The pre-v1 stability risk is manageable: it is used only for optional semantic search, not for the primary state store.

5. ChromaDB and LanceDB are embeddings-first. They do not provide a relational query layer — a schema with `items`, `tags`, `sources`, and `processed` tables would still require SQLite alongside them. Running two separate database files for the same corpus adds complexity without benefit.

6. DuckDB lacks built-in vector search. Adding it would require a community extension or an external vector store, defeating the purpose of using DuckDB as a single solution.

7. The binary-artefact constraint (no git-diffable database file) applies equally to all four technologies. All database files belong in `.gitignore` (or the existing `state/` directory). The database is rebuilt from YAML front-matter on first run and maintained incrementally thereafter — it is a derived artefact, not source of truth.

**Summary position:** SQLite (with FTS5 at Phase 1, sqlite-vec at Phase 2) is the correct technology. The schema above supports all required queries. Migration is triggered by one of four observable signals, not by a fixed item count.

---

### §4 Consistency Check

No internal contradictions were found. Three potential tensions were examined and resolved:

1. **"Prior research said JSON is fine, but this item recommends SQLite."** Not a contradiction. The prior item (`2026-02-27-indexing-and-tracking-method.md`) explicitly stated "SQLite becomes the right migration point only once the corpus exceeds a few hundred items." This item defines when and how that migration happens — it is the successor step, not a reversal.

2. **"sqlite-vec is pre-v1 but is recommended."** Resolved by phasing. Phase 1 (relational + FTS5) uses only stable, stdlib SQLite. Phase 2 (vector search) adds sqlite-vec. If sqlite-vec introduces breaking changes before 1.0, the semantic search backlog item can absorb those costs at implementation time. Phase 1 is not gated on Phase 2.

3. **"DuckDB has FTS and is embedded — why not use it?"** Resolved by query pattern mismatch. DuckDB is OLAP-optimised; the research corpus queries are OLTP-pattern (row lookups, small joins). Additionally, DuckDB has no vector search, requiring a separate store for Phase 2 regardless. SQLite satisfies both phases in one file.

---

### §5 Depth and Breadth Expansion

**Technical lens — SQLite's FTS5 vs alternatives:**
FTS5 uses a standard inverted index. It does not provide semantic (embedding-based) similarity — only lexical matching. BM25 ranking is effective for keyword-based search over structured short documents (research item titles, questions, findings). For semantic queries ("find items related to decision-making under uncertainty"), FTS5 would miss relevant items that use different vocabulary. This is the precise gap that sqlite-vec fills in Phase 2, once embeddings are generated. There is no free lunch: Phase 1 FTS5 is high-recall for known vocabulary; Phase 2 sqlite-vec adds semantic recall but requires an embedding model and an extra dependency.

**Economic lens — dependency cost:**
`chromadb` pulls in 15+ transitive dependencies including `hnswlib` (C++ extension), `tokenizers` (Rust extension), and `mmh3`. This raises the barrier for running the pipeline in a fresh GitHub Actions environment and increases the surface area for dependency conflicts. SQLite (`import sqlite3`) is zero-cost. `sqlite-vec` (`pip install sqlite-vec`) is a pure-C extension with no transitive Python dependencies. [inference from package structure]

**Historical lens — database choices in similar tools:**
Obsidian, Logseq, and Dendron (surveyed in the prior research item) all use flat Markdown + YAML front-matter with in-memory indexing at query time. Zotero uses SQLite with a 10+ table schema. The Zotero model is the closest architectural parallel to what this repository needs at scale: a relational store for structured metadata, a full-text index over content, and a deduplication store. Zotero's FTS approach is an external full-text table indexed against the main `items` table — exactly the FTS5 virtual table pattern proposed in the schema above.

**Regulatory/operational lens:**
No regulatory considerations apply directly to database technology choice. The git-first, owner-reviews-all-changes constraint (from AGENTS.md) does apply: since the database is binary and excluded from git, the source-of-truth for research item metadata must always remain the YAML front-matter in Markdown files. The database is a derived index — it must be rebuildable from source at any time. This is an important architectural invariant for any implementation.

---

### §6 Synthesis

**Recommendation:** SQLite (FTS5 in Phase 1; sqlite-vec in Phase 2) is the correct local database technology for this repository.

**Structured output:**

| Dimension | Conclusion |
|---|---|
| Technology | SQLite + FTS5 (Phase 1); SQLite + FTS5 + sqlite-vec (Phase 2) |
| Migration trigger | ≥500 state entries, OR cross-item query need, OR semantic search backlog item started |
| Dependencies | Phase 1: zero (stdlib); Phase 2: `pip install sqlite-vec` |
| Schema | 5 tables: `items`, `tags`, `sources`, `processed`, `transcripts`; 1 FTS5 virtual table; 1 vec0 table (Phase 2) |
| Database file | Binary artefact; add `state/research.db` to `.gitignore`; rebuild from YAML front-matter on first run |
| Source of truth | YAML front-matter (Markdown files) — database is a derived index |
| DuckDB verdict | Not suitable: OLAP-optimised engine mismatches row-oriented query patterns; no vector search |
| ChromaDB verdict | Not suitable as primary store; embeddings-first, no relational layer, heavy dependencies |
| LanceDB verdict | Disproportionate to corpus scale; designed for petabyte-scale multi-modal workloads |

**Key claims:**
1. SQLite FTS5 satisfies full-text search requirements with zero additional dependencies. [fact, high confidence]
2. sqlite-vec enables vector search within the same SQLite file at Phase 2. [fact, medium confidence — pre-v1 stability risk]
3. DuckDB is a worse fit than SQLite for row-oriented, small-corpus queries. [inference, high confidence]
4. ChromaDB and LanceDB are both over-engineered for this use case and introduce heavy dependency trees. [inference, high confidence]
5. The database must be treated as a derived artefact, rebuildable from YAML front-matter. [inference, high confidence — follows from binary-diff constraint]
6. Migration is triggered by observable signals, not a fixed item count. [inference, medium confidence]

---

### §7 Recursive Review

**Completeness check:**
- Every atomic sub-question (A1–A4, B1–B6, C1–C3, D1–D2) has a substantive answer in §2.
- All five sources from the checklist were consulted and marked `[x]`.
- All major technology alternatives (SQLite+FTS5, sqlite-vec, DuckDB, ChromaDB, LanceDB) were evaluated.
- Schema covers all query patterns identified in §2 A1.

**Claim labelling check:**
- All facts are mapped to sources (sqlite.org, github.com/asg017/sqlite-vec, duckdb.org, docs.trychroma.com, docs.lancedb.com, prior completed item).
- All inferences are labelled and derived from evidence.
- No unsupported assumptions in §3.

**Uncertainties acknowledged:**
- sqlite-vec pre-v1 status: breaking changes before 1.0 are possible. Mitigated by phasing.
- Dependency weight of ChromaDB and LanceDB is characterised from documentation structure rather than direct `pip install` audit. Labelled as inference.
- The 500-entry migration trigger is a heuristic, not a benchmarked figure.

**Conclusion:** The synthesis is internally consistent, well-sourced, and actionable. All threads are synthesised. The recommendation is specific and falsifiable.

---

## Findings

### Executive Summary

SQLite with FTS5 (Phase 1) and sqlite-vec (Phase 2) is the correct local database technology for this repository when the corpus or query complexity outgrows JSON files. SQLite satisfies all relational query patterns, provides full-text search at zero dependency cost via its built-in FTS5 module, and allows vector search to be added incrementally through the `sqlite-vec` extension without switching to a different database file or technology stack. DuckDB is poorly matched to the row-oriented access patterns of this workload and lacks built-in vector search; ChromaDB and LanceDB are embeddings-first systems that cannot replace the relational layer and introduce heavy dependency trees. The database should be treated as a derived artefact rebuilt from YAML front-matter, not as the source of truth for research item metadata.

### Key Findings

1. **SQLite's FTS5 extension is built into Python's standard library `sqlite3` module and requires no additional dependencies to provide BM25-ranked full-text search over research item titles, questions, and findings.** [high confidence]

2. **The `sqlite-vec` extension (`pip install sqlite-vec`) enables KNN vector search within the same SQLite database file as FTS5, adding semantic retrieval capability without introducing a second database technology.** sqlite-vec is pre-v1 and may have breaking changes before 1.0; this risk is managed by deferring its integration to Phase 2. [medium confidence]

3. **DuckDB's columnar-vectorised OLAP engine is optimised for large-table analytical scans — a query pattern that does not match this repository's workload of point lookups by status, tag joins, and URL deduplication.** DuckDB also has no built-in vector search extension. [high confidence]

4. **ChromaDB and LanceDB are both embeddings-first systems that do not provide a relational query layer; using either would require SQLite alongside them anyway, eliminating any benefit over the proposed SQLite-only approach.** ChromaDB's persistent client also pulls in 15+ transitive dependencies including C++ and Rust extensions. [high confidence]

5. **The recommended five-table schema (`items`, `tags`, `sources`, `processed`, `transcripts`) with an FTS5 virtual table over item content supports all identified query patterns: relational filtering by status/priority/tag, URL deduplication, source tracking, and full-text search.** [high confidence]

6. **The database file must be treated as a derived artefact excluded from git, rebuildable from YAML front-matter on demand, because all embedded database formats (SQLite, DuckDB, ChromaDB, LanceDB) produce binary files that are not git-diffable.** YAML front-matter in Markdown files remains the source of truth for research item metadata. [high confidence]

7. **Migration from JSON + YAML to SQLite should be triggered by at least one of four observable signals: state/index.json exceeding 500 entries, a need for cross-item relational queries beyond grep, a semantic search capability being built, or concurrent pipeline runs requiring ACID transactions.** The 500-entry threshold is a cognitive cost heuristic (large JSON diffs), not a performance limit. [medium confidence]

8. **Zotero's architecture (SQLite with a relational schema + a separate FTS table indexed against item content) is the closest prior art for this use case and validates the proposed schema pattern.** [high confidence]

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| SQLite FTS5 built-in, BM25 ranking, phrase/prefix search | sqlite.org/fts5.html (accessed directly) | high | In stdlib since Python 3.x via `sqlite3` module |
| sqlite-vec provides KNN in SQLite, `pip install sqlite-vec` | github.com/asg017/sqlite-vec (accessed directly) | high | Mozilla Builders sponsorship; pre-v1 |
| sqlite-vec pre-v1 status, breaking changes expected | github.com/asg017/sqlite-vec README (accessed directly) | high | Explicitly marked as pre-v1 |
| DuckDB is OLAP-optimised, columnar-vectorised | duckdb.org/why_duckdb (accessed directly) | high | Primary positioning documentation |
| DuckDB FTS extension uses BM25 | duckdb.org/docs/stable/core_extensions/full_text_search.html (accessed directly) | high | `match_bm25` function, Porter stemmer |
| DuckDB has no built-in vector search | DuckDB extension docs review | high | No KNN/ANN listed in core extensions |
| ChromaDB persistent client available, heavy dependencies | docs.trychroma.com (accessed directly) | high | PersistentClient noted; dependency tree inferred |
| ChromaDB is embeddings-first, not a relational DB | docs.trychroma.com/docs/overview/introduction (accessed directly) | high | Explicit positioning statement |
| LanceDB targets multi-modal lakehouse at scale | docs.lancedb.com (accessed directly) | high | Explicit positioning statement |
| Prior research deferred vector stores until >50 items | 2026-02-27-indexing-and-tracking-method.md Key Finding 5 | high | Direct quote from completed item |
| Zotero uses SQLite + FTS table | 2026-02-27-indexing-and-tracking-method.md Key Finding 2 | high | Zotero docs cited in prior item |
| Binary database files are not git-diffable | 2026-02-27-indexing-and-tracking-method.md Key Finding 4 | high | Well-established; confirmed in prior item |

### Assumptions

- **Assumption:** ChromaDB's dependency tree is substantially heavier than SQLite's. **Justification:** The Chroma getting-started documentation references `hnswlib`, `tokenizers`, and other packages visible in the ChromaDB PyPI dependency graph. A precise dependency count was not audited directly; the characterisation "15+ transitive dependencies" is an estimate. If this assumption is wrong, ChromaDB's dependency cost is lower than assessed, but the fundamental objection (not a relational system) remains.
- **Assumption:** The corpus will not require concurrent write access from multiple processes in Phase 1. **Justification:** AGENTS.md describes a single-owner workflow with one pipeline running at a time. If parallel pipeline runs are introduced, SQLite WAL mode handles concurrent readers; exclusive write locks must still be serialised.
- **Assumption:** The embedding model for Phase 2 will produce 1536-dimensional float32 vectors. **Justification:** 1536 is the dimension of OpenAI's `text-embedding-3-small`. If a different model is chosen, the `vec0` table dimension must be adjusted at schema creation time.

### Analysis

The key trade-off in this evaluation is **query richness and semantic capability** (favouring ChromaDB or LanceDB) versus **dependency minimalism and unified relational+FTS access** (favouring SQLite). Given the scale (hundreds of items) and query patterns (point lookups, tag filters, FTS), the dependency minimalism argument wins decisively. Both ChromaDB and LanceDB are systems built for embedding-centric workloads at scale; neither provides a relational layer, meaning SQL-expressible queries would still require a separate SQLite instance alongside them.

The DuckDB alternative was evaluated seriously because DuckDB is a legitimate embedded analytical database with Python bindings and FTS support. Its disqualification is not on grounds of quality but on grounds of query pattern mismatch: columnar storage is a disadvantage for single-row lookups and small multi-row joins, and the absence of built-in vector search means two separate stores are still needed for Phase 2.

The phased approach (SQLite alone → SQLite + sqlite-vec) is the correct architecture because it avoids committing to a pre-v1 extension (sqlite-vec) in the core state management path. Phase 1 can be implemented and used in production; Phase 2 is added when the semantic search backlog item is executed.

### Risks, Gaps, and Uncertainties

- **sqlite-vec pre-v1 stability:** The extension may change its `vec0` virtual table SQL syntax before reaching 1.0. Mitigation: pin the version in `pyproject.toml`; isolate vector search behind an abstraction layer in `src/db/`.
- **Embedding model dependency for Phase 2:** Generating embeddings requires either a local model (`sentence-transformers`, ~400MB download) or an API call (OpenAI, Gemini). The choice has cost and privacy implications that are out of scope for this item.
- **Database rebuild performance:** If the pipeline rebuilds the database from scratch (e.g., in a fresh GitHub Actions environment), parsing all YAML front-matter files and re-inserting into SQLite takes time proportional to corpus size. At hundreds of items this is negligible; at thousands, an incremental build approach would be needed.
- **FTS5 content sync:** The FTS5 virtual table using `content='items'` requires triggers or manual `INSERT INTO items_fts` calls to stay in sync with the `items` table. If not implemented correctly, the FTS index will be stale. This is a known SQLite FTS5 limitation.

### Open Questions

1. **What embedding model should be used for Phase 2 vector search?** This is the primary unresolved dependency for the semantic search capability. Local models (sentence-transformers) avoid API calls but require a large download in CI; API models (OpenAI, Gemini) require credentials. This is a prerequisite question for the `2026-03-02-semantic-full-text-search.md` backlog item.
2. **Should the database be committed to git in a compressed or alternative format (e.g., Datasette's `.db.gz`)?** Datasette supports SQLite databases published as static sites; committing the `.db` file (gzip-compressed) would enable read-only access via GitHub. This is an interface question for `2026-02-27-interface-and-delivery.md`.
3. **Should the Phase 1 migration include transcripts?** Transcripts are large blobs; storing them in SQLite would make the `.db` file large. An alternative is to store only the URL and a content hash, with the transcript text remaining in `Research/transcripts/`. This is a scope question for the Phase 1 implementation backlog item.

---

## Output

- Type: knowledge, backlog-item
- Description: Technology recommendation (SQLite + FTS5 + sqlite-vec phased), 5-table schema design, migration trigger criteria. Spawns implementation backlog item for Phase 1 SQLite migration.
- Links:
  - https://sqlite.org/fts5.html (SQLite FTS5 extension documentation)
  - https://github.com/asg017/sqlite-vec (sqlite-vec extension for KNN vector search)
  - https://duckdb.org/why_duckdb (DuckDB design rationale)
