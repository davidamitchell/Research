# Architecture Decision Records

This directory contains Architecture Decision Records (ADRs) for the Research project.

ADRs document significant design decisions, the context in which they were made, and the trade-offs considered. They are immutable history — when a decision changes, a new ADR is written that supersedes the old one.

Format: [MADR (Markdown Architectural Decision Records)](https://adr.github.io/madr/)

---

## Index

| ADR | Title | Status | Date |
|---|---|---|---|
| [0001](0001-use-python-as-primary-language.md) | Use Python as primary language | Accepted | 2026-02-27 |

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
