# Session: Add research questions to consolidate-research workflow

**Date:** 2026-03-17
**Slug:** add-research-questions-to-consolidate

## What was done

Updated `.github/workflows/consolidate_research.yml` to address five new requirements
from the issue:

### Changes made

1. **Research questions extracted** — Both `## Research Question` (newer format) and
   `## Question / Hypothesis` (older format) are now extracted and included per item.

2. **Title as section header** — The frontmatter `title` field is used as the `## Heading`
   for each item (replacing the old `## Source: filename` format).

3. **TOC uses title** — Table of contents entries now show the human-readable title,
   not the filename.

4. **Tags included** — The frontmatter `tags` field is displayed as `**Tags:** [...]`
   below each section heading.

5. **Date cutoff at 2026-02-28** — Items with `added` date before `2026-02-28` are
   excluded. Missing/malformed `added` fields are also excluded.

6. **Reverse chronological order** — Both TOC and content sections are generated
   newest-first using `printf '%s\n' ... | sort -r`.

### Key technical notes

- Added `get_frontmatter(file, field)` helper using `awk` + `grep` pipeline to parse
  YAML frontmatter without any Python dependency. Uses `|| true` to handle files without
  frontmatter (like `README.md`) under `set -euo pipefail`.
- Replaced `for file in glob` loops with `while IFS= read -r file; do ... done < <(...)`
  to support piped input from `sort -r`.
- Anchors still use filenames for stability and reliable TOC link resolution.
- The `|| true` on `get_frontmatter` is intentional — `grep` exits 1 when no match is
  found, which would otherwise abort the script under `set -euo pipefail`.

## Files changed

- `.github/workflows/consolidate_research.yml` — updated
- `progress/2026-03-17-add-research-questions-to-consolidate.md` — this log
