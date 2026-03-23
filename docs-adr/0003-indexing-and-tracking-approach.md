# ADR-0003: JSON State File + YAML Front-matter for Indexing and Tracking

Date: 2026-02-28
Status: accepted

## Context

As the research corpus grows, we need a way to:

1. Track which source URLs have been fetched and processed (deduplication across pipeline runs)
2. Find research items by status, tag, or date (navigation and querying)
3. Keep the approach simple, git-friendly, and operable without a server

The options evaluated were:

1. **JSON state file** (`state/index.json`) for URL-based dedup + YAML front-matter in `.md` files for item metadata
2. **SQLite** (`state/index.db`) — embedded database, ACID transactions, efficient querying
3. **YAML index file** — a separate YAML file listing all items with metadata, maintained alongside the `.md` files
4. **Vector store** (ChromaDB or sqlite-vss) — semantic similarity search over content embeddings

Research item `Research/completed/2026-02-27-indexing-and-tracking-method.md` contains the full evidence map and analysis behind this decision.

## Decision

Use **two separate, complementary layers**:

### Layer 1 — Processing state: `state/index.json`

A JSON file that tracks which source URLs have been fetched, preventing duplicate processing across pipeline runs. Schema:

```json
{
  "processed": {
    "<url>": {
      "fetched_at": "ISO-8601 timestamp",
      "title": "string",
      "source_id": "string"
    }
  }
}
```

Written atomically (write to temp file, then `os.replace`) to prevent corruption on interrupted runs.

### Layer 2 — Research item metadata: YAML front-matter

Each `Research/**/*.md` file carries its own metadata in YAML front-matter (title, status, priority, tags, started, completed). The `src/research/item.py` module already reads and writes this front-matter. No separate index file is needed; the files _are_ the index.

## Rejected Alternatives

**SQLite** — offers ACID transactions and efficient querying but produces binary files that cannot be reviewed in `git diff` on the GitHub website. Since the owner reviews all changes exclusively via the GitHub website, losing readable diffs is a significant usability cost that outweighs the query performance benefit at the anticipated corpus size.

**YAML index file** — duplicates metadata already present in the front-matter of each `.md` file. Keeping two copies in sync introduces a new category of inconsistency bug.

**Vector store** — solves semantic search, not deduplication. Both ChromaDB (server-based) and sqlite-vss (binary file) add operational complexity before a minimum viable search capability is justified. Deferred to a future slice once `Research/completed/` contains enough items to make semantic search useful.

## Consequences

- **Positive:** `state/index.json` is a plain-text, human-readable, git-diffable file. Changes are visible in pull request diffs on the GitHub website.
- **Positive:** No new runtime dependency. Standard library `json` and `pathlib` are sufficient.
- **Positive:** Consistent with the `davidamitchell/Latest-developments-` pattern already familiar to the codebase.
- **Positive:** Migration path to SQLite is straightforward if the corpus grows beyond a few thousand entries and query latency becomes problematic — the state schema is minimal and the interface is an internal module boundary.
- **Negative:** JSON state lookup is O(n) when reading the file; runtime lookup uses a Python `dict` (O(1)), so this only matters at file-load time for large state files.
- **Negative:** No built-in support for complex queries (e.g., "all URLs fetched from source X in the last 30 days"). These queries are not needed yet; if they become needed, migrate to SQLite at that point.

## Migration Trigger

Migrate from JSON to SQLite when any of the following are true:
- `state/index.json` exceeds 5 MB, **or**
- Pipeline startup time is noticeably degraded by state-file loading, **or**
- A query requirement emerges that cannot be served by iterating the JSON structure.
