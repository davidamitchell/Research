# Architecture Decision Records

This directory contains Architecture Decision Records (ADRs) for the Research project.

ADRs document significant design decisions, the context in which they were made, and the trade-offs considered. They are immutable history — when a decision changes, a new ADR is written that supersedes the old one.

Format: [MADR (Markdown Architectural Decision Records)](https://adr.github.io/madr/)

---

## Index

| ADR | Title | Status | Date |
|---|---|---|---|
| [0001](0001-use-python-as-primary-language.md) | Use Python as primary language | Accepted | 2026-02-27 |
| [0002](0002-agent-skills-submodule.md) | Agent skills as a git submodule | Accepted | 2026-02-28 |
| [0003](0003-indexing-and-tracking-approach.md) | JSON state file + YAML front-matter for indexing and tracking | Accepted | 2026-02-28 |
| [0004](0004-autonomous-research-loop.md) | Autonomous research loop design and safety controls | Accepted | 2026-03-02 |
| [0005](0005-github-wiki-publishing-approach.md) | GitHub wiki as the research content delivery channel | Accepted | 2026-03-02 |
| [0006](0006-standardise-agent-instructions.md) | Standardise agent instruction files | Accepted | 2026-03-07 |
| [0007](0007-reviewing-state-and-dispatch-trigger.md) | Reviewing state and workflow_dispatch trigger for research review | Accepted | 2026-03-11 |
| [0009](0009-consolidate-research-workflow.md) | Consolidate Research Workflow | Accepted | 2026-03-17 |
| [0010](0010-github-pages-static-site.md) | GitHub Pages static site as research delivery channel | Accepted | 2026-03-23 |
| [0011](0011-git-index-staging-in-cli-file-moves.md) | Git-index staging in CLI file-move commands | Accepted | 2026-03-29 |
| [0012](0012-research-loop-safety-control-value-uplift.md) | Research loop safety control value uplift | Accepted | 2026-04-27 |
| [0013](0013-research-item-frontmatter-schema-extension.md) | Research item frontmatter schema extension (W-0044 to W-0049) | Accepted | 2026-04-28 |
| [0014](0014-knowledge-synthesis-directory.md) | Knowledge/ synthesis directory and schema | Accepted | 2026-05-05 |

---

## When to write an ADR

- A new tool, dependency, or external service is adopted
- A file format, naming convention, or workflow is established
- A non-trivial architectural choice is made that would be costly to reverse

Use the `decisions` skill in `.github/skills/decisions/SKILL.md` when writing ADRs.

---

## How to Add an ADR

1. Copy the template below into a new file `NNNN-short-title.md` (zero-padded, sequential)
2. Fill in all sections
3. Update the index table above
4. Commit with message: `docs: add ADR-NNNN <short title>`

### Template

```markdown
# ADR-NNNN: Title

Date: YYYY-MM-DD
Status: proposed | accepted | superseded by [ADR-XXXX] | deprecated

## Context

What is the problem or situation forcing a decision?

## Decision

What have we decided to do?

## Consequences

### Positive
- ...

### Negative / Trade-offs
- ...

### Neutral
- ...
```
