---
title: "Indexing and tracking method for research content"
added: 2026-02-27
status: backlog
priority: high
tags: [indexing, tracking, database, organisation]
started: ~
completed: ~
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
- Description: ADR-0002 on indexing approach; Epic 3 backlog items
