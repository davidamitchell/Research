# Research

This directory holds all research items in three states.

---

## Structure

```
Research/
├── _template.md        # Copy this to create a new item
├── backlog/            # Items not yet started
├── in-progress/        # Items actively being researched
└── completed/          # Finished research with findings
```

---

## Workflow

### Adding a new item (Quick)

```bash
cp Research/_template.md Research/backlog/$(date +%Y-%m-%d)-short-title.md
# Edit the file, fill in title, question, context
git add Research/backlog/ && git commit -m "research: add backlog item - <short title>"
```

### Starting an item

```bash
mv Research/backlog/YYYY-MM-DD-title.md Research/in-progress/
# Update status: field to in-progress and set started: date
git add Research/ && git commit -m "research: start - <short title>"
```

### Completing an item

```bash
mv Research/in-progress/YYYY-MM-DD-title.md Research/completed/
# Fill in ## Findings and ## Output sections
# Update status: to completed and set completed: date
git add Research/ && git commit -m "research: complete - <short title>"
```

---

## File Naming Convention

`YYYY-MM-DD-short-descriptive-title.md`

Examples:
- `2026-02-27-youtube-transcript-fetching.md`
- `2026-03-01-information-synthesis-entropy.md`

---

## Output Types

Research can produce one or more outputs. Record in the `output:` field of the item:

| Output type | Description |
|---|---|
| `skill` | A new skill for `davidamitchell/Skills` |
| `tool` | A new or updated tool in `src/` |
| `agent` | A new agent configuration |
| `knowledge` | A structured note or ADR |
| `backlog-item` | Spawns one or more items in `BACKLOG.md` |

---

## Separating Research Backlog from Repo Improvement Backlog

- **`Research/backlog/`** — *what to research* (questions, topics, hypotheses)
- **`BACKLOG.md`** — *how to improve this repo* (code, tooling, structure)

Never mix these. A research item may *produce* a backlog item (e.g. "after researching SQLite, we decide to use it → add backlog item 3.2"), but the research item itself lives here.
