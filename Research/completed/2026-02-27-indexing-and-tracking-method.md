---
title: "Indexing and tracking method for research content"
added: 2026-02-27
status: completed
priority: high
tags: [indexing, tracking, database, organisation]
started: 2026-02-28
completed: 2026-02-28
output: [knowledge, backlog-item]
---

# Indexing and tracking method for research content

## Question / Hypothesis

What is the best method for indexing and tracking research content (transcripts, papers, notes) given the constraints of a git-based, local-first repo?

## Context

As the research corpus grows, a flat directory of Markdown files becomes harder to query and navigate. We need a way to:
- Track which items have been processed / indexed
- Find related content across sources (transcript + paper on same topic)
- Avoid reprocessing already-seen content (deduplication)
- Keep the approach simple enough to run locally without a server

Options range from simple (JSON state file, CSV index) to complex (SQLite, vector store, full-text search engine).

## Scope

**In scope:**
- Local, file-based or embedded-database options
- Git-friendly (diffs should be readable, not binary blobs for small state)
- Trade-offs: JSON state file vs SQLite vs YAML index vs vector store

**Out of scope:**
- Server-based databases (Postgres, Elasticsearch) unless strongly justified
- Cloud-only solutions

## Approach

1. Survey how similar research tools solve this (Obsidian, Zotero, Dendron, Logseq)
2. Evaluate JSON state file (like Latest-developments-) vs SQLite vs vector store
3. Write ADR with recommendation
4. Implement in Epic 3

## Sources

- [ ] `davidamitchell/Latest-developments-/src/state.py` — URL-based dedup with JSON
- [ ] Zotero architecture: https://www.zotero.org/support/dev/client_coding/direct_sqlite_database_access
- [ ] Obsidian graph approach
- [ ] ChromaDB / sqlite-vss for vector search

## Findings

### Executive Summary

For a git-based, local-first research corpus at the scale anticipated here (hundreds, not millions, of items), a **JSON state file** for URL-based deduplication combined with **YAML front-matter** in Markdown research item files is the correct approach. This mirrors the `davidamitchell/Latest-developments-` pattern that already underpins this repository's fetcher design, remains fully git-diffable, requires no additional server or binary dependency, and is easy to inspect and edit by hand. SQLite becomes the right migration point only once the corpus exceeds a few hundred items and query performance degrades noticeably. Vector stores (ChromaDB, sqlite-vss) are deferred to a future search slice.

### Key Findings

1. **Obsidian, Logseq, and Dendron all converge on plain-Markdown + flat files** for git-friendliness. None use a custom binary index at the data layer; instead, they keep metadata in YAML front-matter and build in-memory indices at runtime. This is directly applicable: the Research item files already use YAML front-matter, giving us the metadata layer for free.

2. **Zotero's SQLite approach is powerful but inappropriate here.** Zotero uses a 10+ table relational schema (items, itemData, itemDataValues, creators, tags, relations, fulltext*). It is robust for academic reference management but is a binary file, impossible to diff in git, and requires Zotero's migration tooling to evolve the schema. Its complexity is justified by managing tens of thousands of heterogeneous item types — which is not our use case.

3. **JSON state file is git-friendly and sufficient for URL-based deduplication at this scale.** The pattern (`load state.json → check URL → process → save state.json`) is O(n) for lookup but acceptable up to ~10,000 entries. Converting the URL set to a Python `set` at runtime eliminates duplicate lookups during a single run. `state/index.json` already exists in this repo (currently `{}`), confirming the infrastructure is in place.

4. **SQLite offers ACID transactions, efficient indexing, and `INSERT OR IGNORE` deduplication, but at the cost of git-diffability.** SQLite database files are binary blobs: a single row change produces a completely different file in `git diff`. This is acceptable only if the state file is treated as a runtime artefact that is never reviewed in pull requests. For this repo — where the owner reviews all changes via the GitHub website — losing readable diffs is a meaningful cost.

5. **Vector stores (ChromaDB, sqlite-vss/sqlite-vec) solve a different problem: semantic search, not deduplication.** ChromaDB is production-grade but runs as a server process, adding operational complexity. sqlite-vss is single-file but still binary. Both are appropriate only once the `Research/completed/` directory has enough items (>50) to make semantic search over findings worthwhile. This is a future-state capability, not a current need.

6. **The two concerns — deduplication/processing state and research-item metadata — should remain separate.** Processing state (which URLs have been fetched) belongs in `state/index.json`. Research-item metadata (title, status, tags, started/completed dates) belongs in the YAML front-matter of each `Research/*.md` file. Mixing them would couple the pipeline to the research workflow unnecessarily.

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| Obsidian/Logseq/Dendron use plain Markdown + YAML front-matter | Obsidian docs; Logseq docs; Dendron docs (via web search) | high | All three use `.md` files with front-matter for metadata |
| Zotero uses SQLite (binary, not git-diffable) | [Zotero SQLite docs](https://www.zotero.org/support/dev/client_coding/direct_sqlite_database_access); [Zotero schema repo](https://github.com/zotero/zotero-schema) | high | Confirmed by official documentation |
| JSON state file is O(n) lookup but sufficient <10,000 entries | General Python data structures; [DLT state docs](https://dlthub.com/docs/general-usage/state) | high | Set-based runtime lookup is O(1); serialisation to list for JSON is standard practice |
| SQLite produces binary diffs in git | [JSON Showdown: Dolt vs SQLite](https://www.dolthub.com/blog/2024-11-18-json-sqlite-vs-dolt/); web search synthesis | high | Well-established limitation; multiple independent sources confirm |
| ChromaDB and sqlite-vss are designed for vector search, not dedup | [sqlite-vss GitHub](https://github.com/asg017/sqlite-vss); [ChromaDB guide](https://airbyte.com/data-engineering-resources/chroma-db-vector-embeddings); [SQLite vs Chroma](https://stephencollins.tech/posts/sqlite-vs-chroma-comparative-analysis) | high | Both tools explicitly positioned for embedding similarity search |
| `state/index.json` already exists in this repo | Local file inspection (`state/index.json` = `{}`) | high | Confirmed by direct inspection |

### Assumptions

- **Assumption:** The research corpus will remain below 10,000 processed items for the foreseeable future. **Justification:** This is a personal research tracking repo for a single owner; growth to 10,000 items would represent years of sustained activity. The JSON approach can be migrated to SQLite incrementally if this assumption is violated.
- **Assumption:** Semantic search over completed research items is a future-state feature, not a current requirement. **Justification:** There are currently zero items in `Research/completed/`. Vector search is not useful until a meaningful corpus exists.
- **Assumption:** The owner will review state file changes via git diffs on the GitHub website. **Justification:** This is stated explicitly in `AGENTS.md`: the owner uses the GitHub website exclusively. A binary state file would be invisible to this review workflow.

### Analysis

The key trade-off is between **query power / performance** (favouring SQLite) and **transparency / git-diffability** (favouring JSON). Given the stated constraints — git-first, local, owner reviews via GitHub website — transparency wins. The query performance of JSON is sufficient at this scale, and any performance concern can be addressed by migrating the state file to SQLite at a later point without changing the research-item format.

The comparison with Obsidian, Logseq, and Dendron is instructive but not directly applicable: those tools index at query-time (in-memory graph construction on startup), a luxury we cannot easily replicate in a CI/CD pipeline. However, their shared reliance on YAML front-matter for metadata validates the approach already in use for research items.

Zotero's complexity is not a model to emulate — it is the product of having to manage thousands of heterogeneous reference types, institutional group libraries, and offline sync. Its schema is instructive as an upper bound of what relational complexity buys, but it is far beyond the needs of this repo.

The two-layer approach (YAML front-matter for research metadata + JSON for processing state) maps cleanly onto the existing codebase:
- `src/research/item.py` already reads/writes YAML front-matter
- `state/index.json` already exists
- The `FetchedItem.url` field is the natural deduplication key

### Risks, Gaps, and Uncertainties

- **Concurrent write risk on JSON:** If multiple pipeline runs execute simultaneously (e.g., parallel GitHub Actions jobs), both could read the same `state/index.json`, process duplicate items, and write conflicting updates. Mitigation: use atomic writes (write to a temp file then `os.replace`), and ensure the fetch workflow is not triggered in parallel.
- **JSON file growth:** A single `state/index.json` with thousands of entries will grow large. If performance degrades, the mitigation is to switch to SQLite (see W-0021 scope note).
- **No schema validation on `state/index.json`:** The current file is `{}`. If the schema is not defined before implementation, it will drift. Recommendation: define the schema in an ADR before implementing Epic 3.

### Open Questions

- Should `state/index.json` store only the URL (set of strings) or richer metadata (fetch timestamp, title, content hash)? Content hash would enable detecting when a source has been updated and needs reprocessing. This is a scope question for W-0021.
- At what corpus size does the JSON approach become noticeably slow in practice? The threshold is likely corpus-dependent (number of URLs × read latency). Consider benchmarking at 1,000 and 10,000 entries.
- Is there value in a YAML index file (e.g., `state/completed.yaml`) that lists all completed research items with their key metadata, as a human-readable companion to `state/index.json`? This would make the state layer more navigable without a GUI.

---

## Output

- Type: knowledge, backlog-item
- Description: ADR-0003 documenting the JSON state file + YAML front-matter approach for Epic 3; W-0021 scope refined to implement JSON state with atomic writes and a defined schema.
- Links: `docs/adr/0003-indexing-and-tracking-approach.md` (to be created as part of W-0020)
