# ADR-0005: GitHub Wiki as the Research Content Delivery Channel

Date: 2026-03-02
Status: accepted

## Context

Completed research items accumulate in `Research/completed/` as Markdown files with YAML
front-matter. They are well-structured for agents and git history, but not easily browsable
by the owner, who reads exclusively via the GitHub website and iOS GitHub app.

Three delivery options were evaluated:

1. **GitHub wiki** — a separate, flat git repository (`{repo}.wiki.git`) accessible from the
   **Wiki** tab on the GitHub website and iOS app; renders Markdown natively; no additional
   hosting required.
2. **GitHub Pages (static site)** — Jekyll or MkDocs site generated into `docs/` or a `gh-pages`
   branch; supports full navigation and theming.
3. **README or index file in the repo** — a Markdown index committed alongside the research
   items; browsable on GitHub but requires navigating file trees.

Research item `Research/completed/2026-03-01-github-wiki-research-content.md` contains the
full evidence map and analysis behind this decision.

## Decision

Publish completed research items to the **GitHub wiki** using a full-rebuild GitHub Actions
workflow (`publish-wiki.yml`).

### Publishing approach: full rebuild

On each trigger, the wiki repository is wiped and rebuilt from scratch using
`src/wiki/publish.py`. Every completed `.md` file (excluding `README.md`) is published as a
wiki page with its YAML front-matter stripped. Two navigation pages are generated:

- **`Home.md`** — date-sorted index table of all completed items with title, date, and tags.
- **`_Sidebar.md`** — tag-grouped navigation list linking to individual pages.

### Credentials

The workflow uses the built-in `GITHUB_TOKEN` with `permissions: contents: write`. No
personal access token or additional repository secret is required.

### Trigger

The workflow runs on:
- Push to `main` that touches `Research/completed/**` (automatic, zero-friction)
- `workflow_dispatch` (manual trigger from the Actions tab)

## Rejected Alternatives

**GitHub Pages (static site)** — Jekyll or MkDocs produce better navigation and theming but
require a build step, a separate branch or directory for output, and either a third-party
theme or custom CSS. The additional complexity is not justified at the current research corpus
size (tens of items). The GitHub wiki is natively accessible on mobile and requires no build
configuration.

**README or index file in the repo** — browsable on GitHub but forces the reader to navigate
file trees to reach individual items. Front-matter is visible in raw files. Not a meaningful
improvement over the status quo.

**Incremental wiki updates** — tracking which items have changed since the last push would
reduce the amount of git history written to the wiki repository, but adds stateful logic
(hash tracking or mtime comparison) that is not justified at the current volume. A full
rebuild takes milliseconds.

## Consequences

### Positive

- Zero new credentials or secrets required — `GITHUB_TOKEN` is auto-provided by GitHub Actions.
- No additional hosting, build tooling, or external services.
- Readable on the GitHub website and iOS app from the Wiki tab.
- Full-rebuild approach is stateless and self-correcting: renames, deletions, and status
  changes in `Research/completed/` are handled automatically on the next push.
- `src/wiki/publish.py` is a plain Python module with no new runtime dependencies beyond
  `PyYAML` (already a project dependency).

### Negative / Trade-offs

- **One-time manual setup required.** The owner must enable the wiki once in repository
  Settings → Features → Wikis. The workflow cannot enable it programmatically.
- **Pages are flat** — the GitHub wiki does not support subdirectories. All research items
  appear at the same level, differentiated only by the date-prefixed filename convention.
- **Wiki history accumulates.** Each rebuild is a separate commit to the wiki repository.
  Over time this creates a large wiki git history. This is acceptable given the low publish
  frequency (at most a few times per day from the research loop).

### Neutral

- Internal wiki links use `[[Page-Name|Display Text]]` syntax. Pipe characters inside
  Markdown table cells must be escaped as `\|`. The `wiki_link(in_table=True)` helper in
  `src/wiki/publish.py` encapsulates this.

## Migration Trigger

Migrate from GitHub wiki to GitHub Pages if any of the following become true:
- The wiki's flat page structure makes navigation unwieldy (e.g., > 200 completed items
  without meaningful grouping).
- The owner needs full-text search across research content.
- Custom theming or layout is required for sharing research externally.
