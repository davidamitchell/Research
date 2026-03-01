# Research

A place to hold a backlog of research to be done, research underway, and completed work. Also the home for research tooling built to support that process.

---

## What's Here

| Directory / File | Purpose |
|---|---|
| `Research/` | Research items in three states: `backlog/`, `in-progress/`, `completed/` |
| `src/` | Python tooling to support research (transcript fetcher, indexing, etc.) |
| `tests/` | Tests for `src/` |
| `config/` | Configuration for sources and tooling |
| `docs/adr/` | Architecture Decision Records |
| `AGENTS.md` | Instructions for all AI coding agents |
| `BACKLOG.md` | Repo improvement backlog (separate from research item backlog) |
| `PROGRESS.md` | Session-by-session progress log |

---

## Quick Start

```bash
# Set up development environment
pip install -e ".[dev]"
cp .env.example .env   # fill in real values
git submodule update --init  # populate agent skills

# Run checks
make check

# Run tests
make test
```

---

## Research Workflow

1. **Add** a new item: copy `Research/_template.md` to `Research/backlog/YYYY-MM-DD-short-title.md`
2. **Start** an item: move the file from `backlog/` to `in-progress/`; update status in the file
3. **Complete** an item: move the file from `in-progress/` to `completed/`; fill in findings

See `Research/README.md` for the full workflow and template details.

---

## Repo Improvement Backlog

Tracked in `BACKLOG.md`. This is distinct from the research item backlog in `Research/backlog/`.

---

## Agent Instructions

All coding conventions, standards, and working methodology are in `AGENTS.md`. Every AI agent (GitHub Copilot, Claude Code, etc.) reads that file first.

---

## Environment Variables

Copy `.env.example` to `.env` and fill in values. Never commit `.env`.

## Related

- [Latest Developments](https://github.com/davidamitchell/Latest-developments-) — daily AI/ML digest pipeline; YouTube transcript fetcher code lives there and will be ported here
- [Skills](https://github.com/davidamitchell/Skills) — shared agent skills submodule
