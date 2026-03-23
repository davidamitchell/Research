# ADR-0010: GitHub Pages Static Site as Research Delivery Channel

Date: 2026-03-23
Status: Accepted
Supersedes: [ADR-0005](0005-github-wiki-publishing-approach.md) (GitHub wiki as primary channel)

## Context

ADR-0005 adopted the GitHub wiki as the primary research content delivery channel, with
GitHub Pages listed as a rejected alternative due to build complexity at the then-current
corpus size (tens of items). That decision included a migration trigger:

> "Migrate from GitHub wiki to GitHub Pages if any of the following become true:
> - The wiki's flat page structure makes navigation unwieldy (e.g., > 200 completed items
>   without meaningful grouping).
> - The owner needs full-text search across research content.
> - Custom theming or layout is required for sharing research externally."

All three conditions have since been met:
1. The completed-items corpus has grown past the point where the flat wiki structure
   provides useful navigation. Items are only differentiated by date prefix.
2. Full-text search across research content is a core access pattern.
3. Custom theming (dark monospace design) and structured navigation (threads, tags,
   related items) are required for external sharing and corpus-level scanning.

A static site generator (`scripts/build_site.py` + `scripts/extract_metadata.py`) was
built to address these needs, producing a self-contained HTML/JS site in `docs/`.

## Decision

Adopt the GitHub Pages static site (generated from `docs/`) as the primary research
content delivery channel, published via GitHub Actions on every push that touches
`Research/completed/**`.

### Architecture

**Two-step pipeline:**

1. `scripts/extract_metadata.py` — reads all qualifying `Research/completed/*.md` files
   and writes `state/content_metadata.json` with extracted key claims, named concepts,
   and source URLs per item. This feeds the search index and key-claims display.

2. `scripts/build_site.py` — reads the same completed items plus `content_metadata.json`
   and generates `docs/` with:
   - `docs/index.html` — landing page: stats block, featured threads/topics, search preview
   - `docs/browse.html` — filterable card grid (all items)
   - `docs/research/<slug>.html` — individual item pages with related items, prev/next
   - `docs/tags/index.html` — full tag list with filter input
   - `docs/tags/<tag>.html` — per-tag pages
   - `docs/threads.html` — threads listing
   - `docs/threads/<slug>.html` — per-thread pages
   - `docs/search.html` — full-text search page (client-side JSON index)
   - `docs/search-index.json` — search index for client-side JavaScript
   - `docs/threads-index.json` — thread data for JavaScript

**Filtering:**
- Items predating `2026-02-28` are excluded (consistent with ADR-0009 qualifying criteria).
- Filenames containing `meta` or `infra` are excluded.
- Singleton tags (appear on only one item that has other multi-item tags) are dropped.

**Navigation structure:**
- Fixed top nav: brand ("Research"), Threads, Tags, Search, GitHub repo link.
- No Browse tab in the nav; the browse page exists for deep-linking and tag-page
  back-navigation but is not a primary nav entry.
- Thread and tag groupings are the primary discovery mechanisms.

**Search:**
- Client-side JavaScript search using a JSON index (`search-index.json`).
- No server-side dependencies; the entire site is static.

**Relationship graph:**
- Items sharing ≥ 2 tags are considered related; top-5 related items shown per page.
- Explicit threads via `thread:` frontmatter field; implicit threads from tag clusters
  (≥ 3 shared tags).

**Credentials:**
- `GITHUB_TOKEN` with `permissions: contents: write` — sufficient to push to `docs/`
  and trigger Pages deployment. No Personal Access Token (PAT) needed.

### Qualifying criteria (same as ADR-0009)

- `added` date ≥ `2026-02-28`
- Filename does not contain `meta` or `infra`

## Consequences

### Positive

- Full-text client-side search across all research content.
- Structured navigation: threads, tags, related items, prev/next within items.
- Custom dark monospace design appropriate for sharing research externally.
- Key claims, named concepts, and source URLs extracted and surfaced per item.
- Idempotent full rebuild on every push; stale pages removed automatically.
- No new hosting infrastructure or credentials — GitHub Pages is built into the repo.
- The wiki channel remains available in parallel; both are updated from the same source.

### Negative / Trade-offs

- Build step adds latency to the research publish pipeline (seconds, not minutes).
- `docs/` directory accumulates generated HTML committed to the repository. Git history
  for `docs/` grows with each publish. This is acceptable given publish frequency.
- `scripts/build_site.py` and `scripts/extract_metadata.py` are not covered by the
  standard `tests/` pytest suite (they are build tools, not library code). Correctness
  is validated by running the build and inspecting output.
- The site is served from `/Research/` path prefix (GitHub Pages project site). All
  internal links must use the `/Research/` prefix.

### Neutral

- The `browse.html` page is not in the primary navigation but remains reachable via
  deep links and search results. Items pages no longer include a Browse breadcrumb.
- Tag pages link back to the tags index (`/Research/tags/`) rather than Browse.
- The GitHub wiki and GitHub Pages serve different audiences: the wiki is optimised
  for reading from the GitHub website and iOS app; the Pages site is optimised for
  browsing, search, and external sharing.
