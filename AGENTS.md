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

## Working Environment

These constraints are fixed. Every agent working on this repository **must** respect them.

- **The owner interacts exclusively via the GitHub website or iOS GitHub app.** There is no local IDE, no `git clone`, and no terminal.
- **All coding is done by the agent.** The owner does not write or edit code directly.
- **Codespaces is not in use.** Do not rely on Codespaces features, devcontainers, or `$CODESPACE_*` environment variables.
- **GitHub Copilot Spaces and GitHub Projects are fine to use if helpful**, but are not a requirement. Suggest them only when they add clear value.
- **Agent interactions happen via PR comments, issue comments, or by starting a new agent task/session.** The owner may also trigger operations by clicking buttons on the GitHub website (e.g., the Actions tab "Run workflow" button).

### Consequences for tooling design

- **Prefer fully automated pipelines** (scheduled or event-triggered workflows) over requiring the owner to manually trigger anything. If a manual trigger is unavoidable, `workflow_dispatch` is the acceptable fallback — it surfaces as a "Run workflow" button on the Actions tab, accessible from the website and iOS app.
- Do not require Codespaces secrets for production workflows — use repository secrets (Settings → Secrets and variables → Actions) instead.
- Any manual step in a process should be achievable entirely through the GitHub website: creating files, triggering workflows, commenting on PRs.

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
├── completed/          # Finished research with findings
└── transcripts/        # Plain-text transcripts committed by fetch-transcript workflow

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

state/
└── index.json          # URL deduplication state (written by StateStore; gitignored content)

tests/
```

---

## Research Item Workflow

### Adding a New Research Item

1. Copy `Research/_template.md` to `Research/backlog/YYYY-MM-DD-short-title.md`
2. Fill in: title, added date, priority, tags, question/hypothesis, and any initial context
3. Update `PROGRESS.md` — add an entry to the Work Log noting the new backlog item
4. Commit with message: `research: add backlog item - <short title>`

### Starting Research

1. Move the file from `Research/backlog/` to `Research/in-progress/`
2. Update the `status` field to `in-progress` and set `started` date
3. Update `PROGRESS.md` — note the item has moved to in-progress
4. Commit with message: `research: start - <short title>`

### Completing Research

1. Move the file from `Research/in-progress/` to `Research/completed/`
2. Fill in the `## Findings` and `## Output` sections
3. Update `status` to `completed` and set `completed` date
4. Update `PROGRESS.md` — record findings summary and any outputs produced
5. Commit with message: `research: complete - <short title>`

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

> **Setup required:** After a standard `git clone`, skill directories are empty. Run `git submodule update --init` from the repository root to populate them before using any skill.

| Skill | When it applies | Claude Code | GitHub Copilot |
|---|---|---|---|
| `backlog-manager` | Adding, prioritising, or reviewing backlog items | `/backlog-manager` | read `SKILL.md` and apply manually |
| `citation-discipline` | Ensuring claims are sourced and referenced | `/citation-discipline` | read `SKILL.md` and apply manually |
| `remove-ai-slop` | Reviewing output for hollow filler language | `/remove-ai-slop` | read `SKILL.md` and apply manually |
| `research` | Conducting structured research on a topic | `/research` | read `SKILL.md` and apply manually |
| `speculation-control` | Flagging uncertain claims vs established facts | `/speculation-control` | read `SKILL.md` and apply manually |
| `strategic-persuasion` | Building audience-targeted persuasive content | `/strategic-persuasion` | read `SKILL.md` and apply manually |
| `strategy-author` | Producing or reviewing strategy documents | `/strategy-author` | read `SKILL.md` and apply manually |

### Invoking skills

**Claude Code:** Skills in `.claude/skills/` are available as `/skill-name` slash commands once the submodule is initialised. Example: `/research` to start a structured research session.

**GitHub Copilot:** Skills in `.github/skills/` are readable as context files but are not invokable as slash commands. Read the relevant `SKILL.md` directly (e.g., open `.github/skills/research/SKILL.md` in your context window) and follow its process step by step as the agent — no user action required.

**Fallback (any agent, submodule not initialised):** Note the gap in the session log. Proceed with equivalent inline behaviour — apply the skill's logic from memory or from the issue context. Do not halt work because a skill file is unavailable.

To add a new skill: add it to the Skills repo first; it will be picked up on the next sync.

---

## MCP Configuration

MCP server configs are defined in:
- `.github/mcp.json` — GitHub Copilot Agent (requires `type: "stdio"` on each entry)
- `.mcp.json` — Claude Code and other agents

Both files must stay in sync. The following 9 servers are configured in both files.

### Server Reference

| Server | Runtime | Purpose | Secrets required |
|---|---|---|---|
| `fetch` | `python -m mcp_server_fetch` | Fetch web pages and URLs for research sourcing | none |
| `sequential_thinking` | `npx @modelcontextprotocol/server-sequential-thinking` | Step-by-step reasoning for complex research synthesis | none |
| `time` | `python -m mcp_server_time` | Current date/time for timestamping research items | none |
| `memory` | `npx @modelcontextprotocol/server-memory` | Persistent knowledge graph across sessions | none |
| `git` | `python -m mcp_server_git` | Read git history, diffs, and commit context | none |
| `filesystem` | `npx @modelcontextprotocol/server-filesystem` | Read/write research files in the current working directory (repo root) | none |
| `brave_search` | `npx @modelcontextprotocol/server-brave-search` | Web search for research sourcing and fact-checking | `BRAVE_API_KEY` (repository secret or `.env`) |
| `arxiv` | `python -m arxiv_mcp_server` | Search and fetch arXiv papers for academic sourcing | none |
| `github` | `npx @modelcontextprotocol/server-github` | Read GitHub issues, PRs, and repo data | `GITHUB_PERSONAL_ACCESS_TOKEN` (repository secret or `.env`) |

### Session-start MCP availability check

At the start of each session, note which configured MCP servers are actually running. If a configured server is unavailable, log it and fall back to built-in equivalents rather than attempting tool calls that will fail silently.

| Environment | Typically available | Typically unavailable |
|---|---|---|
| GitHub Copilot agent (cloud runner) | `fetch`, `git`, `github` (built-in) | `brave_search`, `arxiv`, `filesystem`, `memory`, `sequential_thinking` |
| Claude Code (local / Codespaces) | all 9 servers (if pip/npm packages installed) | any server whose package is missing |
| Local dev | all 9 servers (if packages installed and secrets set) | servers with missing secrets (`brave_search`, `github`) |

Substitutions when MCP servers are unavailable (use whatever equivalent capability your runtime provides):
- `brave_search` → built-in web search (e.g., `web_search` tool in Copilot/Claude)
- `arxiv` → fetch arxiv.org URLs directly using available HTTP/fetch tools
- `filesystem` → built-in file read/write tools (bash, view, edit, create tools)
- `memory` → session notes; record key facts in `PROGRESS.md`
- `sequential_thinking` → inline chain-of-thought reasoning

### Python MCP servers — installation

`fetch`, `time`, `git`, and `arxiv` are Python packages (the npm packages were removed from the registry). Install them in the project virtualenv or Codespaces environment:

```bash
pip install mcp-server-fetch mcp-server-time mcp-server-git arxiv-mcp-server
```

### Using MCP in research tasks

When executing the `research` skill or conducting a research item end-to-end:

- Use **`fetch`** to retrieve web pages for source content (replaces manual `web_fetch` calls when the MCP server is running).
- Use **`brave_search`** to discover sources (requires `BRAVE_API_KEY` repository secret or `.env`).
- Use **`arxiv`** to locate and fetch academic papers referenced by a research item.
- Use **`sequential_thinking`** to plan multi-step research synthesis before writing findings.
- Use **`memory`** to persist cross-session state about ongoing research threads.
- Use **`filesystem`** to read/write research Markdown files directly (serves the current working directory).
- Use **`git`** to inspect commit history when reviewing what has already been processed.
- Use **`time`** to stamp `added`, `started`, and `completed` dates correctly.
- Use **`github`** to read issue/PR context when a research item was spawned from an issue.

---

## GitHub Actions / Codespaces

- CI: `.github/workflows/ci.yml` — lint + test on every push/PR
- Skills sync: `.github/workflows/sync-skills.yml` — weekly Monday 06:00 UTC
- **Transcript fetch: `.github/workflows/fetch-transcript.yml`** — manually triggered (`workflow_dispatch`); fetches YouTube auto-generated captions via `yt-dlp` and commits a plain-text file to `Research/transcripts/<video-id>.txt`. If YouTube blocks the request (cloud IP restriction), the workflow commits step-by-step instructions for adding the transcript manually via the GitHub website.

### How to trigger the transcript workflow (no IDE required)

1. Go to the repository on GitHub
2. Click the **Actions** tab
3. Click **"Fetch YouTube Transcript"** in the left sidebar
4. Click **"Run workflow"** → select the branch → paste the video URL → click **"Run workflow"**
5. If `yt-dlp` succeeds, the transcript is committed automatically
6. If it fails (YouTube blocks the cloud IP), open `Research/transcripts/<video-id>-README.md` for manual instructions

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

After answering these questions, close the loop:
- If a new convention would have prevented this problem, **add it to `AGENTS.md` now**.
- If a systemic fix is needed (code, tooling, or infrastructure), **add a `BACKLOG.md` item**.
- **Record the outcome in `PROGRESS.md`** so the next session sees the learning.

---

## When to Update AGENTS.md

Update `AGENTS.md` when:
- A new MCP server, skill, or tool is added or removed.
- A new convention is established (via Mini-Retro or otherwise).
- The project structure changes materially (new top-level directories, new workflows, new external integrations).
- A documented process is found to be wrong or incomplete.

Do not wait until the end of a session — update it at the point of discovery.

---

## When the Backlog Is Empty

When `BACKLOG.md` has no pending items (all are `done` or `archived`):

1. Review `Research/backlog/` — pick up a research item that hasn't been started.
2. Review open GitHub issues — propose a new Epic based on project state and issue content.
3. If neither applies, surface the question to the owner: describe the current state and ask what to prioritise next.

Do not invent work. Do not silently loop. Surface the state and ask.
