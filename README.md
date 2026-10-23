# Research

A place to hold a backlog of research to be done, research underway, and completed work. Also the home for research tooling built to support that process.

---

## What's Here

| Directory / File | Purpose |
|---|---|
| `Research/` | Research items in three states: `backlog/`, `in-progress/`, `completed/` |
| `Research/Research_Master.md` | Auto-generated consolidated view of all completed research (titles, questions, tags, findings) |
| `src/` | Python tooling to support research (transcript fetcher, indexing, etc.) |
| `tests/` | Tests for `src/` |
| `scripts/` | Site build pipeline (`build_site.py`, `extract_metadata.py`) — edit these to change the site |
| `config/` | Configuration for sources and tooling |
| `docs/` | **Auto-generated.** Static GitHub Pages site — built by the `build_site.yml` workflow. Do not edit files here directly; changes will be overwritten on the next build. Edit `scripts/build_site.py` instead. |
| `docs-adr/` | Architecture Decision Records |
| `.github/copilot-instructions.md` | Instructions for all AI coding agents |
| `BACKLOG.md` | Repo improvement backlog (separate from research item backlog) |
| `PROGRESS.md` | Session-by-session progress log |
| `CHANGELOG.md` | User-facing change history (Keep-a-Changelog format) |

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

The primary owner path is to create a GitHub issue with the full research question and any
seeds or context in its body, then assign it to Copilot. Copilot applies the `research-question`
skill, creates a structured item under `Research/backlog/`, and opens a pull request (PR).
After that PR is merged, the `research-loop` workflow can process the item on its weekday
schedule or when manually triggered from the Actions tab; merging the PR does not trigger the
loop automatically.

See [Research/README.md](Research/README.md) for the question-quality criteria, full workflow,
and agent/tooling path.

---

## Repo Improvement Backlog

Tracked in `BACKLOG.md`. This is distinct from the research item backlog in `Research/backlog/`.

---

## Agent Instructions

All coding conventions, standards, and working methodology are in `.github/copilot-instructions.md`. Every AI agent (GitHub Copilot, Claude Code, etc.) reads that file first.

---

## Environment Variables

Copy `.env.example` to `.env` and fill in values. Never commit `.env`.

## Related

- [Research workflow guide](Research/README.md) — owner intake, question quality, and item lifecycle
- [Research item template](Research/_template.md) — structure for backlog items
- [Copilot instructions](.github/copilot-instructions.md) — agent workflow and repository conventions
- [Latest Developments](https://github.com/davidamitchell/Latest-developments-) — daily AI/ML digest pipeline; YouTube transcript fetcher code lives there and will be ported here
- [Skills](https://github.com/davidamitchell/Skills) — shared agent skills submodule
