# ADR-0009: Consolidate Research Workflow

Date: 2026-03-17
Status: Accepted

## Context

As the `Research/completed/` directory grows, there is no single place to survey all
completed research together — its questions, findings, and key decisions. Reading each
file individually does not scale; the GitHub wiki provides navigation but not a consolidated
view for scanning across the entire corpus in one document.

Two access patterns motivated this decision:

1. **Corpus-wide scanning** — the owner wants to review all completed research questions and
   high-signal findings without opening tens of individual files.
2. **Shareability** — a single Markdown file is easy to copy, export, or attach to a discussion
   without requiring repository access.

Constraints:
- No Python dependency in the consolidation step; the workflow must run with only standard
  Unix tools (bash, awk, sed, grep) to keep it fast and simple.
- The output must be idempotent — repeated runs produce the same file and the workflow
  commits only when content actually changes.
- Items predating 2026-02-28 were added before the research quality standards were
  established and should not appear in the consolidated view.

## Decision

Introduce a GitHub Actions workflow (`consolidate_research.yml`) that generates
`Research/Research_Master.md` — a single consolidated Markdown file from all qualifying
completed research items.

### Qualifying criteria

- `added` date ≥ `2026-02-28` (items added before this date are excluded)
- Filename does not contain `meta` or `infra` (infrastructure and meta items are excluded)

### Output structure per item

1. **Title** — from the `title` frontmatter field (not the filename)
2. **Tags** — from the `tags` frontmatter field
3. **Link** — canonical GitHub URL to the source file
4. **Research question** — extracted from `## Research Question` (current format) or
   `## Question / Hypothesis` (legacy format)
5. **High-signal sections** — `## Methodology`, `## Implementation Logic`,
   `## Decision Log`, `## Strategic Choice`, `## Technical Architecture`,
   `## Findings`, `## Schema`

### Output location

`Research/Research_Master.md` — inside the `Research/` directory alongside the item
subdirectories, making it a first-class part of the research corpus.

### Ordering

Reverse chronological (newest first) — the most recent research appears at the top of
the table of contents and the content body.

### Trigger

- Push to `main` touching `Research/completed/**`
- `workflow_dispatch` (manual trigger from the Actions tab)

### Implementation approach

A pure-shell two-pass script:
1. First pass builds the table of contents (titles, not filenames)
2. Second pass extracts and writes the per-item content

A `get_frontmatter(file, field)` helper parses YAML frontmatter using `awk` + `grep`
without any Python or external dependencies. Anchors use the filename (not the title) for
stable, unambiguous TOC link resolution regardless of title content.

## Consequences

### Positive

- Single document covering all qualifying completed research in one place.
- Titles and research questions are surfaced without opening individual files.
- Idempotent — safe to re-run; commits only on actual content change.
- No new dependencies — pure bash + standard Unix tools.
- Automatic on every push to `Research/completed/`; also manually triggerable.

### Negative / Trade-offs

- The consolidated document is a generated artefact committed to the repo. It will
  appear in git history and diffs. The `[skip ci]` commit message tag prevents
  re-triggering the workflow in a loop.
- The shell `get_frontmatter` helper uses lexicographic string comparison for dates.
  This is correct only if dates are in ISO `YYYY-MM-DD` format, which is enforced by
  the research item template and the CLI tooling.

### Neutral

- `Research_Master.md` is not listed in `Research/_template.md` or the item lifecycle;
  it is a read-only output and should not be edited manually.
- `permissions: contents: write` with `GITHUB_TOKEN` is sufficient — no PAT needed
  (consistent with `publish-wiki.yml`).
