---
title: "Local database: requirements and technology choice"
added: 2026-02-27
status: backlog
priority: medium
tags: [database, sqlite, storage, local]
started: ~
completed: ~
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

- [ ] SQLite docs: https://sqlite.org
- [ ] sqlite-vec: https://github.com/asg017/sqlite-vec
- [ ] DuckDB: https://duckdb.org
- [ ] ChromaDB: https://docs.trychroma.com
- [ ] LanceDB: https://lancedb.github.io/lancedb/

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

- Type: knowledge, backlog-item
- Description: Technology choice ADR; schema design; Epic 3 backlog items
