# Agent Instructions

For AI coding agents (Claude Code, Copilot Workspace, etc.) working on this repository.

---

## Project Overview

A research tracking and tooling repository. It has two distinct purposes:

1. **Research tracking** — `Research/` holds individual research items in three states (`backlog/`, `in-progress/`, `completed/`). This is a file-based Kanban board for research.
2. **Research tooling** — `src/` contains Python code for fetching, processing, and indexing research content (YouTube transcripts, papers, web pages, etc.).

These two concerns are intentionally separate. Research items in `Research/` are not code; they are structured Markdown notes. The code in `src/` is the machinery that helps produce and process those notes.

---

## Non-Negotiable Constraints

- **Never commit secrets.** API keys and credentials live in environment variables / GitHub Secrets. The `.env` file is gitignored.
- **Keep research backlog (`Research/backlog/`) separate from repo improvement backlog (`BACKLOG.md`).** One is about *what to research*; the other is about *improvements to this repo's code and structure*.
- **No breaking changes to research item format** without updating `Research/_template.md` and the ADR that documents the format choice.
- **Every code slice must be end-to-end runnable** before being marked complete in `BACKLOG.md`.
- **Keep PROGRESS.md updated** after every meaningful commit.

---

## Coding Standards

### Language & Runtime
- Python 3.11+
- Type hints on all public functions and class methods
- `pyproject.toml` is the source of truth for dependencies and tool config

### Style
- `ruff` for linting and formatting (line length 100)
- Run `make check` before committing
- No unused imports; no bare `except:` clauses

### Logging
- Use the project logger (`src/logger.py`) — never `print()` in production code
- Log levels: `DEBUG` for per-item detail, `INFO` for pipeline stages, `WARNING` for skipped/degraded paths, `ERROR` for failures

### Error Handling
- Fetcher failures for a single source must not abort the entire run — log and continue
- Network errors must be retried with exponential backoff (max 3 attempts)

### Testing
- Tests live in `tests/`; use `pytest`
- Mock all network calls
- Unit tests on all business logic
- **Bug fixes must start with a failing test.** Write the test first, confirm it fails, then fix and confirm it passes.

---

## Repository Layout

```
Research/
├── README.md           # Research workflow documentation
├── _template.md        # Template for a new research item
├── backlog/            # Items not yet started
├── in-progress/        # Items actively being researched
└── completed/          # Finished research with findings

src/
├── main.py             # CLI entry point
├── fetchers/
│   ├── __init__.py     # Fetcher protocol and FetchedItem dataclass
│   └── youtube.py      # YouTube transcript fetcher
├── research/
│   ├── __init__.py
│   └── item.py         # ResearchItem dataclass and file I/O
├── logger.py           # Logging setup
└── config.py           # Load and validate config

config/
└── sources.yaml        # Source configuration

docs/
└── adr/                # Architecture Decision Records
    ├── README.md        # ADR index
    └── NNNN-title.md

.github/
├── copilot-instructions.md  # Thin stub pointing here
├── mcp.json                 # MCP servers for GitHub Copilot Agent
├── skills/                  # Agent skills (submodule: davidamitchell/Skills)
└── workflows/
    ├── ci.yml
    └── sync-skills.yml

.claude/
└── skills/             # Agent skills for Claude Code (same submodule)

tests/
```

---

## Research Item Workflow

### Adding a New Research Item

1. Copy `Research/_template.md` to `Research/backlog/YYYY-MM-DD-short-title.md`
2. Fill in: title, added date, priority, tags, question/hypothesis, and any initial context
3. Commit with message: `research: add backlog item - <short title>`

### Starting Research

1. Move the file from `Research/backlog/` to `Research/in-progress/`
2. Update the `status` field to `in-progress` and set `started` date
3. Commit with message: `research: start - <short title>`

### Completing Research

1. Move the file from `Research/in-progress/` to `Research/completed/`
2. Fill in the `## Findings` and `## Output` sections
3. Update `status` to `completed` and set `completed` date
4. Commit with message: `research: complete - <short title>`

### Output Types

Research can produce one or more of the following outputs (record in the `output` field of the template):
- **skill** — a new skill for the `davidamitchell/Skills` repo
- **tool** — a new or updated tool in `src/`
- **agent** — a new agent configuration
- **knowledge** — a structured note or ADR
- **backlog-item** — spawns one or more new repo improvement items in `BACKLOG.md`

---

## Adding a New Source Type (Code)

1. Create `src/fetchers/<source>.py` implementing the `Fetcher` protocol
2. Add config schema to `config/sources.yaml`
3. Register in `src/main.py`
4. Write unit tests in `tests/test_fetchers_<source>.py`
5. Write an ADR in `docs/adr/` if the approach involves a significant design decision
6. Update `BACKLOG.md` (mark slice done) and `PROGRESS.md`

---

## Adding an ADR

ADRs follow the [MADR format](https://adr.github.io/madr/). File naming: `docs/adr/NNNN-short-title.md` (zero-padded 4 digits). Update `docs/adr/README.md` after adding.

Status values: `proposed` → `accepted` → `superseded` / `deprecated`

An ADR **must** be written any time a change involves:
- Introducing a new external dependency or third-party API
- Changing the research item format or tracking method
- Choosing an indexing or storage approach
- Any decision that would be hard to reverse

---

## Agent Skills

`.github/skills/` and `.claude/skills/` are git submodules tracking [`davidamitchell/Skills`](https://github.com/davidamitchell/Skills).

A weekly workflow (`.github/workflows/sync-skills.yml`) advances both submodule pointers to the latest commit.

| Skill | When it applies |
|---|---|
| `backlog-manager` | Adding, prioritising, or reviewing backlog items |
| `citation-discipline` | Ensuring claims are sourced and referenced |
| `remove-ai-slop` | Reviewing output for hollow filler language |
| `research` | Conducting structured research on a topic |
| `speculation-control` | Flagging uncertain claims vs established facts |
| `strategic-persuasion` | Building audience-targeted persuasive content |
| `strategy-author` | Producing or reviewing strategy documents |

To add a new skill: add it to the Skills repo first; it will be picked up on the next sync.

---

## MCP Configuration

MCP server configs are defined in:
- `.github/mcp.json` — GitHub Copilot Agent
- `.mcp.json` — Claude Code and other agents

Servers available: `fetch`, `sequential_thinking`, `time`, `memory`, `git`, `filesystem`, `brave_search`, `arxiv`, `github`

---

## GitHub Actions / Codespaces

- CI: `.github/workflows/ci.yml` — lint + test on every push/PR
- Skills sync: `.github/workflows/sync-skills.yml` — weekly Monday 06:00 UTC

---

## Slice Completion Checklist

Before marking a backlog slice as done:

- [ ] Code merged to the development branch
- [ ] `make check` passes (ruff lint + format)
- [ ] `make test` passes
- [ ] `PROGRESS.md` updated
- [ ] Any new ADRs written and indexed
- [ ] README updated if user-facing behaviour changed

---

## Working Methodology

### Root cause before action

When something is broken or unclear, spend time on *why* before reaching for a fix.

Most problems fall into one of three categories:

**Context gap** — the information needed to do the right thing was never provided. Surface the missing information; don't guess.

**Model error** — the mental model of how the system works is wrong. Update the model first, then re-derive the solution.

**Prompt/specification error** — the task was stated in a way that made the wrong solution look right. Re-examine framing before retrying.

### Before writing code

- State what you understand the problem to be. If the statement is fuzzy, stop and sharpen it.
- Identify what you don't know. Missing information is better surfaced early.
- Note any assumptions explicitly.

### When an attempt fails

- Do not retry the same thing. Understand why it failed first.
- "It didn't work" is not a diagnosis. "It didn't work because X was Y when I expected Z" is.

### Progress and documentation

Update documentation before context degrades, not after.

- After each meaningful unit of work: commit, update status, note what changed and why.
- `PROGRESS.md` is the handoff document. A new session reading it should know exactly where to pick up.

---

## Mini-Retro — After Each Piece of Work

1. **Did the process work?** Was there a test-first cycle where required?
2. **What broke the process?** Identify the exact moment — the assumption, the missing context, the skipped step.
3. **How can the instructions be improved?** If a convention would have prevented the problem, add it to this file *now*.
4. **Is this a pattern?** Has this class of issue appeared before?

The goal: the next agent should not be able to make the same class of mistake.
