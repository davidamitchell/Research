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

The primary way to submit a research question is through a GitHub issue:

1. The owner creates an issue and puts the full research question, plus any seeds or context, in its body.
2. The owner assigns the issue to Copilot.
3. Copilot applies the `research-question` skill, creates a structured item under `Research/backlog/`, and opens a pull request (PR). This step scopes the question; it does not conduct the research.
4. After the PR is merged, the `research-loop` workflow processes the backlog item. It runs on weekdays or can be triggered manually from the Actions tab.

See [What makes a good research question?](#what-makes-a-good-research-question) for guidance on framing the question and useful seeds.

### What makes a good research question?

A question is ready when it is:

- **Specific** — identifies the subject, comparison or evaluation, and context.
- **Answerable** — can be resolved with evidence that could be obtained.
- **Scoped** — makes clear what is in and out of scope.
- **Motivated** — says what decision or problem the answer should inform.
- **Decomposable** — can be broken into at least two atomic sub-questions.

When a question is too broad, the `research-question` skill uses this rewriting pattern:

> What is the [best / most appropriate / correct] [X] for [purpose] given [constraints]?

The owner prefers questions to include useful seeds where available: starting points, related prior research items, concrete sources, or examples. Seeds add context for scoping and investigation; they do not replace a clear question.

### Agent/tooling path: create a backlog item directly

The following file-copy workflow is available for agents or other direct repository work; it is not the primary owner submission path:

1. **Add** an item by copying `Research/_template.md` to `Research/backlog/YYYY-MM-DD-short-title.md` and filling it in.
2. **Start** an item: run `python -m src.main research start <filename>` to move it from `backlog/` to `in-progress/` and update its status.
3. **Complete** an item: after research and review, run `python -m src.main research complete <filename>` to move it to `completed/`.

See `Research/README.md` for the full workflow and template details.

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

- [Research workflow and question guidance](Research/README.md)
- [Research item template](Research/_template.md)
- [Copilot instructions](.github/copilot-instructions.md)
- [Latest Developments](https://github.com/davidamitchell/Latest-developments-) — daily AI/ML digest pipeline; YouTube transcript fetcher code lives there and will be ported here
- [Skills](https://github.com/davidamitchell/Skills) — shared agent skills submodule
