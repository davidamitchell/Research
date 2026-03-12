# 2026-03-12 — Add hosting options research item

## What was done

- Fixed a duplicate `draft` subparser registration in `src/research/cli.py` (lines 261–263 were an exact duplicate of lines 253–255, causing `ArgumentError: conflicting subparser: draft` on every CLI invocation).
- Added research backlog item: `Research/backlog/2026-03-12-hosting-options-for-the-research-repo.md`
  - Priority: medium
  - Tags: hosting, static-site, search, vector-db, infrastructure, free-tier
  - Output: knowledge, backlog-item
  - Question: What is the best free or very-low-cost hosting option for this research repository that supports full-text search, and optionally vector/graph database capabilities?
  - Scope captures owner's stated constraints (no SEO, no DNS, no auth; free/near-free; search required; vector/graph DB optional; static site with JS filtering acceptable)
  - Approach covers static hosting platforms, SSGs, client-side search (Pagefind, Orama), vector DB free tiers (LanceDB, Qdrant), and graph DB free tiers (Neo4j AuraDB)
  - Sources pre-populated with 11 starting points

## Files changed

- `src/research/cli.py` — removed duplicate draft subparser block
- `Research/backlog/2026-03-12-hosting-options-for-the-research-repo.md` — new research item
- `progress/2026-03-12-hosting-options-backlog.md` — this file
