# Copilot Instructions

For AI coding agents working on this repository.

> **Quick Reference — most frequently missed rules:**
> 1. Every session ends with a Mini-Retro in `progress/YYYY-MM-DD-{slug}.md` — not optional.
> 2. Expand ALL acronyms on first use in research items: `Full Name (ABBR)`. This is the #1 cause of review failures.
> 3. Never edit `.github/skills/` directly — all skill changes go to `davidamitchell/Skills` (open a PR there). The weekly `sync-skills.yml` workflow copies updated skills into `.github/skills/` automatically.
> 4. Never assume credentials or capabilities exist — STOP and ask if not listed in the credentials table.
> 5. When something goes wrong twice: name the class, fix the root cause, update the Known Recurring Patterns table.

---

## Project Overview

A research tracking and tooling repository. It has two distinct purposes:

1. **Research tracking** — `Research/` holds individual research items in four states (`backlog/`, `in-progress/`, `completed/`). Items in `reviewing` status stay in `in-progress/` — the status field in frontmatter is the state machine; directory moves happen only on `start` (backlog → in-progress) and `complete` (in-progress → completed). This is a file-based Kanban board for research.
2. **Research tooling** — `src/` contains Python code for fetching, processing, and indexing research content (YouTube transcripts, papers, web pages, etc.).

These two concerns are intentionally separate. Research items in `Research/` are not code; they are structured Markdown notes. The code in `src/` is the machinery that helps produce and process those notes.

---

## Non-Negotiable Constraints

- **Never commit secrets.** API keys and credentials live in environment variables / GitHub Secrets. The `.env` file is gitignored.
- **Keep research backlog (`Research/backlog/`) separate from repo improvement backlog (`BACKLOG.md`).** One is about *what to research*; the other is about *improvements to this repo's code and structure*.
- **No breaking changes to research item format** without updating `Research/_template.md` and the ADR that documents the format choice.
- **Every code slice must be end-to-end runnable** before being marked complete in `BACKLOG.md`.
- **Log every meaningful session** by creating a file in `progress/YYYY-MM-DD-{slug}.md` where `{slug}` is a short hyphenated identifier for the session (e.g. `fix-wiki-links`, `w-0032-mcp-cleanup`, `ai-strategy`). Do not edit `PROGRESS.md` — it is now static by design.
- **DO NOT ASSUME OR GUESS facts about the environment.** If you do not know whether a credential exists, whether a service is available, or whether a tool is capable of something — **STOP. Ask the owner before proceeding.** Guessing and being wrong wastes cycles and breaks trust. The cost of asking is zero. The cost of guessing wrong is not.
- **DO NOT introduce new external services or credentials without explicit owner approval.** If your design requires something not already listed in the "Available credentials and services" table below, that is a hard stop — surface the gap and ask, do not proceed.
- **Treat undocumented capabilities as unknown.** If a credential, service, or tool is in the approved table but its Notes column does not explicitly state it can do what your design requires, apply the same hard stop as for an unlisted item — do not assume, do not proceed, ask first.
- **Never edit `.github/skills/` directly.** Skill files are copied into `.github/skills/` by the weekly `sync-skills.yml` workflow from `davidamitchell/Skills`. Edits made here are overwritten on every sync. All skill changes go to `davidamitchell/Skills` (open a PR there).

---

## Working Environment

These constraints are fixed. Every agent working on this repository **must** respect them.

- **The owner interacts exclusively via the GitHub website or iOS GitHub app.** There is no local IDE, no `git clone`, and no terminal.
- **All coding is done by the agent.** The owner does not write or edit code directly.
- **Codespaces is not in use.** Do not rely on Codespaces features, devcontainers, or `$CODESPACE_*` environment variables.
- **GitHub Copilot Spaces and GitHub Projects are fine to use if helpful**, but are not a requirement. Suggest them only when they add clear value.
- **Agent interactions happen via PR comments, issue comments, or by starting a new agent task/session.** The owner may also trigger operations by clicking buttons on the GitHub website (e.g., the Actions tab "Run workflow" button).

### Available credentials and services

The following table is the ground truth. Do not guess what exists outside this table.

| Credential / Service | Available | Notes |
|---|---|---|
| `GITHUB_TOKEN` | ✅ Yes | Auto-provided by GitHub Actions; scoped to the current repo and its wiki (requires `permissions: contents: write`); cannot push to other repos |
| `COPILOT_GITHUB_TOKEN` | ✅ Yes (add once) | GitHub PAT; required for Copilot CLI and direct `main` pushes |
| `YOUTUBE_DATA_API` | ✅ Yes | YouTube video metadata |
| `TAVILY_API_KEY` | ✅ Yes | Web search via Tavily API and `tavily-mcp` MCP server |
| Any other credential | ❓ Unknown | **STOP. Ask the owner before designing anything that requires it.** |

If a workflow you are designing requires a credential not in this table, **ask before building**. Do not proceed on the assumption it exists or can be easily added.

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
- **Apply the testing pyramid to external service configuration.** Configuration that wires up an external service (MCP servers, API clients, credentials) is production code and must be proven to work at each relevant layer:
  - **Unit** — verify config file well-formedness (JSON validity, required fields, correct env var names). These tests prove the *file is correct*; they do NOT prove the *service works*.
  - **Integration** — call the actual service with the actual credential. This is the only test that proves the configuration works end-to-end. Mark with `pytest.mark.skipif(not os.getenv("KEY"), reason="KEY not set")` so they skip when credentials are absent, and expose the secret in `ci.yml` so they run in CI.
  - A config change that adds or modifies an external service entry is **not done** until the integration test exists and passes in CI. The absence of a credential is a blocker on shipping the change, not a reason to fall back to unit tests alone.

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
├── copilot-instructions.md  # Agent instructions (this file)
├── mcp.json                 # MCP servers for GitHub Copilot Agent
├── skills/                  # Agent skills (submodule: davidamitchell/Skills)
└── workflows/
    ├── ci.yml
    └── sync-skills.yml

state/
└── index.json          # URL deduplication state (written by StateStore; gitignored content)

progress/               # Per-session logs (one file per session; no conflicts)
└── YYYY-MM-DD-{slug}.md

tests/
```

---

## Research Item Workflow

### Adding a New Research Item

1. Copy `Research/_template.md` to `Research/backlog/YYYY-MM-DD-short-title.md`
2. Fill in: title, added date, priority, tags, question/hypothesis, and any initial context
3. Create `progress/YYYY-MM-DD-{slug}.md` — note the new backlog item
4. Commit with message: `research: add backlog item - <short title>`

### Starting Research

1. Run the CLI command to move the item and stamp the `started` date automatically:
   ```bash
   python -m src.main research start <filename>
   ```
2. Add an entry to `progress/YYYY-MM-DD-{slug}.md` — note the item has moved to in-progress
3. Commit with message: `research: start - <short title>`

### Conducting Research

Once the item is in `Research/in-progress/`, run the **`research` skill** in full and use available **MCP tools**.

**Invoke the research skill:**
- **GitHub Copilot Agent:** Open `.github/skills/research/SKILL.md` and follow its process step by step as the agent
- **Fallback (submodule not initialised):** Follow Steps 3–7 of `research-prompt.md`, which mirrors the skill process in full

**Write the full skill output into `## Research Skill Output` as you work through each section:**
- **§0** — restate the question, confirm scope and constraints
- **§1** — decompose Approach sub-questions into atomic questions
- **§2** — gather evidence iteratively; label each claim **[fact]**, **[inference]**, or **[assumption]** with source
- **§3** — separate facts from inferences and assumptions explicitly
- **§4** — identify and resolve internal contradictions
- **§5** — re-examine findings through relevant lenses (technical, regulatory, economic, historical, behavioural)
- **§6** — write the synthesis (executive summary, key findings, evidence map, assumptions, analysis, risks, open questions)
- **§7** — validate the full output; confirm every claim is sourced or labelled

The `## Research Skill Output` section is **retained verbatim** in the completed item.

**Use MCP tools throughout the investigation** (full reference: [Using MCP in research tasks](#using-mcp-in-research-tasks)):
- `tavily` — discover sources, verify claims, and find current information
- `fetch` — retrieve full page content from each source URL
- `arxiv` — locate and fetch academic papers referenced in Sources
- `sequential_thinking` — plan the synthesis structure before writing Findings
- `time` — get today's date for `started` and `completed` timestamps
- `filesystem` — read the item file and write Research Skill Output and Findings directly
- `memory` — persist state if the investigation spans multiple sessions
- `github` — read issue or PR context when the item was spawned from one

**Seed `## Findings` from `## Research Skill Output §6`:** Once §6 Synthesis is written, copy and expand it into the structured Findings subsections (Executive Summary, Key Findings, Evidence Map, Assumptions, Analysis, Risks/Gaps, Open Questions, Output). No new claims may appear in Findings that are not already in the Research Skill Output.

### Completing Research

1. Run the CLI command to mark the item as ready for automated review:
   ```bash
   python -m src.main research draft <filename>
   ```
   This updates `status: reviewing` in frontmatter but **does not move the file** — it stays in `Research/in-progress/`.
2. Commit and trigger the automated review workflow:
   ```bash
   git add Research/in-progress/<filename>
   git commit -m "research: draft - <short title>"
   git push origin main
   gh workflow run research-review.yml --field item_path=Research/in-progress/<filename>
   ```
3. If the review fails (a GitHub issue labelled `research-review` is opened), address the violations and loop back to Conducting Research, then re-run `research draft`.
4. Once the review passes, close the review issue if one was opened, then move the item to completed:
   ```bash
   python -m src.main research complete <filename>
   ```
5. Check `learnings.md` — if any key finding from this item adds signal to an existing cross-cutting thread, update that thread now. If the item establishes a genuinely new cross-cutting theme, add a new numbered thread entry.
6. Create `progress/YYYY-MM-DD-{slug}.md` — record findings summary and any outputs produced
7. Commit with message: `research: complete - <short title>`

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
6. Update `BACKLOG.md` (mark slice done) and create `progress/YYYY-MM-DD-{slug}.md`

---

## Adding an ADR

ADRs follow the [MADR format](https://adr.github.io/madr/). File naming: `docs/adr/NNNN-short-title.md` (zero-padded 4 digits). Update `docs/adr/README.md` after adding.

Status values: `proposed` → `accepted` → `superseded` / `deprecated`

### When to write an ADR (required)

An ADR **must** be written any time a change involves one or more of the following:

| Trigger | Examples |
|---|---|
| New external dependency or third-party API | Adding a new pip/npm package to production code; integrating a new cloud API |
| New GitHub Actions workflow with autonomous side-effects | Workflows that commit to `main`, modify issues/PRs, or call external APIs |
| Delivery or publication channel for research content | How completed items are published (wiki, Pages, email, MCP); index format choices |
| Storage or indexing approach | How processed-item state is persisted; choice of DB vs flat file vs YAML index |
| Research item format or schema change | Adding or renaming YAML front-matter fields; changing the directory layout |
| Reversal cost > 1 hour | Any architectural decision where undoing the choice requires significant rework |

### When NOT to write an ADR

Do not write an ADR for routine work:

- Bug fixes that don't change the architecture
- Adding a new Python module or test file within an existing pattern
- Updating a workflow that already exists (e.g., changing a schedule or dropdown value)
- Completing or moving a research item through the `backlog → in-progress → reviewing → completed` lifecycle
- Updating documentation, comments, or session logs in `progress/`

### Checklist before closing a slice

If your change touches any "when to write" trigger above, the slice is not done until the ADR exists, is `accepted`, and is linked in `docs/adr/README.md`.

---

## Agent Skills

`.github/skills/` is a git submodule tracking [`davidamitchell/Skills`](https://github.com/davidamitchell/Skills).

A weekly workflow (`.github/workflows/sync-skills.yml`) advances the submodule pointer to the latest commit.

> **Setup required:** After a standard `git clone`, the skills directory is empty. Run `git submodule update --init` from the repository root to populate it before using any skill.

| Skill | When it applies | GitHub Copilot |
|---|---|---|
| `backlog-manager` | Adding, prioritising, or reviewing backlog items | read `SKILL.md` and apply manually |
| `citation-discipline` | Ensuring claims are sourced and referenced | read `SKILL.md` and apply manually |
| `remove-ai-slop` | Reviewing output for hollow filler language | read `SKILL.md` and apply manually |
| `research` | Conducting structured research on a topic | read `SKILL.md` and apply manually |
| `speculation-control` | Flagging uncertain claims vs established facts | read `SKILL.md` and apply manually |
| `strategic-persuasion` | Building audience-targeted persuasive content | read `SKILL.md` and apply manually |
| `strategy-author` | Producing or reviewing strategy documents | read `SKILL.md` and apply manually |

### Invoking skills

**GitHub Copilot:** Skills in `.github/skills/` are readable as context files. Read the relevant `SKILL.md` directly (e.g., open `.github/skills/research/SKILL.md` in your context window) and follow its process step by step as the agent — no user action required.

**Fallback (any agent, submodule not initialised):** Note the gap in `BACKLOG.md`. Proceed without synthesising a substitute skill. Do not halt work.

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
| `arxiv` | `python -m arxiv_mcp_server` | Search and fetch arXiv papers for academic sourcing | none |
| `github` | `npx @modelcontextprotocol/server-github` | Read GitHub issues, PRs, and repo data | `GITHUB_PERSONAL_ACCESS_TOKEN` (repository secret or `.env`) |
| `tavily` | `npx tavily-mcp@latest` | Real-time web search, extraction, mapping, and crawl via Tavily API | `TAVILY_API_KEY` (repository secret or `.env`) |

### Session-start MCP availability check

At the start of each session, note which configured MCP servers are actually running. If a configured server is unavailable, log it and fall back to built-in equivalents rather than attempting tool calls that will fail silently.

| Environment | Typically available | Typically unavailable |
|---|---|---|
| GitHub Copilot agent (cloud runner) | `fetch`, `git`, `github` (built-in) | `arxiv`, `filesystem`, `memory`, `sequential_thinking`, `tavily` |
| Local dev / other agent runtime | all 9 servers (if pip/npm packages installed and secrets set) | servers with missing secrets (`github`, `tavily`) |

Substitutions when MCP servers are unavailable (use whatever equivalent capability your runtime provides):
- `tavily` → built-in web search (e.g., `web_search` tool in Copilot/Claude)
- `arxiv` → fetch arxiv.org URLs directly using available HTTP/fetch tools
- `filesystem` → built-in file read/write tools (bash, view, edit, create tools)
- `memory` → session notes; record key facts in a `progress/` session log
- `sequential_thinking` → inline chain-of-thought reasoning

### Python MCP servers — installation

`fetch`, `time`, `git`, and `arxiv` are Python packages (the npm packages were removed from the registry). Install them in the project virtualenv or Codespaces environment:

```bash
pip install mcp-server-fetch mcp-server-time mcp-server-git arxiv-mcp-server
```

### npx MCP servers — Node.js requirement

`sequential_thinking`, `memory`, `filesystem`, `github`, and `tavily` use `npx` to run. **Node.js (v18 or higher) must be installed.** It is pre-installed on:

- GitHub Actions runners (all standard runner images)
- The devcontainer base image (`mcr.microsoft.com/devcontainers/python:3.11`)

For local dev outside these environments, install Node.js from [nodejs.org](https://nodejs.org/) if `npx --version` returns an error.

The `-y` flag in each config entry (`npx -y <package>`) auto-accepts the one-time package download — no separate `npm install` step is needed.

### Using MCP in research tasks

When executing the `research` skill or conducting a research item end-to-end:

- Use **`fetch`** to retrieve raw web page content from a known URL (replaces manual `web_fetch` calls when the MCP server is running).
- Use **`tavily`** for web discovery and structured content extraction (requires `TAVILY_API_KEY`). Use `tavily-search` to find relevant sources and links; use `tavily-extract` to get clean, structured text from a URL (higher fidelity than `fetch` for content-heavy pages).
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
- **Research loop: `.github/workflows/research-loop.yml`** — autonomous research backlog worker; feeds `research-prompt.md` to the GitHub Copilot CLI in a loop, one fresh session per item, commits directly to `main`. Runs automatically on weekday mornings (3 items/day) and on demand via `workflow_dispatch`. Requires `COPILOT_GITHUB_TOKEN` repository secret (GitHub PAT with Copilot access). See ADR-0004 for safety controls.
- **Transcript fetch: `.github/workflows/fetch-transcript.yml`** — manually triggered (`workflow_dispatch`); fetches YouTube auto-generated captions via `yt-dlp` and commits a plain-text file to `Research/transcripts/<video-id>.txt`. If YouTube blocks the request (cloud IP restriction), the workflow commits step-by-step instructions for adding the transcript manually via the GitHub website.

### Research loop — setup and usage (no IDE required)

**One-time setup:** Add a GitHub PAT as a repository secret:
1. Create a Personal Access Token at [github.com/settings/tokens](https://github.com/settings/tokens) with `repo` scope and Copilot access enabled
2. Settings → Secrets and variables → Actions → New repository secret → name: `COPILOT_GITHUB_TOKEN`, value: your PAT

**How the loop works:**
- Each run processes one or more backlog items.
- Each item gets a **fresh Copilot session** (new context window) — matching the Ralph Wiggum pattern.
- Copilot reads `research-prompt.md`, picks the highest-priority backlog item, researches it, marks it as a draft, triggers the quality review workflow (and waits for it), then completes the item and commits it + a new `progress/` session log directly to `main`.
- The outer `while` loop restarts Copilot for the next item until `max_items` is reached or the backlog is empty.

**Automatic schedule:** Runs weekdays at 07:00 UTC, processes 3 items per day.

**Manual trigger:**
1. Go to the repository on GitHub
2. Click the **Actions** tab
3. Click **"Research Loop"** in the left sidebar
4. Click **"Run workflow"** → select `max_items` from the dropdown (default `1`) → click **"Run workflow"**

**Safety controls:** The loop has multiple runaway-loop guards — see ADR-0004 for full details. Conservative defaults: max 1 item per manual run, max 3 per scheduled run, 90-minute job timeout, 10-iteration hard ceiling, 30-second inter-iteration sleep, abort after 2 consecutive Copilot failures.

**Tuning:** Edit `research-prompt.md` to adjust what Copilot looks for, how findings are structured, or which items to prioritise. The prompt is the only lever — no code changes needed.

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
- [ ] Session log created in `progress/YYYY-MM-DD-{slug}.md`
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
- `progress/` is the handoff document. A new session reading the latest file there should know exactly where to pick up.

---

## Continuous Improvement & Learning

> Complete the work. Improve the system. If something was hard, slow, or confusing — fix it, document it, or raise it.

### Identity as Architect

You are the **Architect** of this repository, not just a user.
Your role is to complete work *and* to improve the system doing the work.
If something was hard, slow, or confusing — fix it, document it, or raise it.
Always ask: *"Is this the best version of this system, or just a working one?"*

These standards are self-applied. The owner should not need to request a mini-retro, an ADR, a CHANGELOG entry, or a progress log. If you are waiting to be asked — the process has failed.

### Every Session Ends with a Mini-Retro

Before closing any session or completing any PR, add a **Mini-Retro** to the session log in `progress/YYYY-MM-DD-{slug}.md`.
It is **not optional**. It is how the system learns.

Answer these four questions — briefly, honestly:

1. **Did the process work?** Was the approach sound? Did the plan hold?
2. **What slowed down or went wrong?** No blame — just facts.
3. **What single change would prevent this next time?** If nothing: say so.
4. **Is this a pattern?** Have you seen this friction before? If yes, it deserves a fix, not just a note.

> Do not just answer — make the change. If the answer is "document it", document it now. If it is "add a backlog item", add it now.

### Improvement Comes in Classes — Look for the Class, Not Just the Instance

When something goes wrong or goes right, resist the urge to fix *just this case*.
Ask: **what class of problem is this?**

| Signal | Class to consider |
|---|---|
| You had to look something up that should be documented | → Add it to the agent instructions or a skill |
| A step was manual that could be automated | → Raise a backlog item or add a workflow |
| A decision was unclear or had to be re-made | → Write an ADR |
| A note or file was out of date | → Mark it `superseded_by`, don't delete it |
| The same friction appears in two retros | → It's a pattern. Prioritise fixing the root cause |
| Missing skill | Add to backlog; do not synthesise a substitute |

### Known Recurring Failure Patterns

The following patterns have appeared **three or more times** across sessions. If you see one occurring again, treat it as a class problem — not a one-off — and fix it at the root.

| Pattern | Impact | Root fix in place |
|---|---|---|
| Acronym not expanded on first use (LLM, CLI, SDK, PAT, MCP, RAG, etc.) | Every automated research review fails citation-discipline for this reason | Inline acronym audit added to `research-prompt.md` Step 6 |
| Editing `.github/skills/` files directly | Submodule content is overwritten on every `sync-skills.yml` run; edits are silently lost | "Read-only submodule" rule added to Non-Negotiable Constraints |
| `web search synthesis` used as a citation | Not a verifiable source; fails citation-discipline pre-output check | Explicitly prohibited in `research-prompt.md` Step 6 companion skill checks |
| Surface evaluation (self-inspection only, no external benchmarking) | Misses factual errors, architectural flaws, and gaps that are only visible when compared to published best practices or observable system behaviour | Evaluation protocol: always (1) search external best practices, (2) audit facts against actual files, (3) use open issues as evidence |

When you identify a **new** recurring pattern (same friction in two or more sessions), add it to this table as part of the Mini-Retro for that session.

### Knowledge Graphing — Every Write Earns Its Place

Every time you create or significantly update a file:
1. Search for 3 related existing files and link them in a `## Related` section.
2. Check for contradictions — supersede, don't delete.
3. Tag accurately in ADRs and docs.

### Proactive Maintenance — Leave It Better

You are permitted — and expected — to improve structure, conventions, and these instructions.
You are **not** permitted to delete history or introduce new structure without documenting why.

### The Improvement Flywheel

```
Do the work → Run the retro (what class of problem appeared?) → Fix or raise the root cause → Next session starts with a slightly better system
```

**When evaluating the system itself**, follow this protocol — do not self-inspect only:
1. Search for published best practices on the relevant topic (agent instructions, workflow design, etc.)
2. Audit factual claims in the instructions against the actual file contents and workflow behavior
3. Use open GitHub issues and repository state as evidence of what is not working in practice

### What "Done" Means

- [ ] The work is complete
- [ ] Session log in `progress/` is updated with a Mini-Retro
- [ ] Any new decisions are recorded as ADRs
- [ ] Any structural improvements spotted are raised in the backlog
- [ ] `CHANGELOG.md` updated if behaviour changed
- [ ] `remove-ai-slop` run on committed prose

---

## Chain-of-Thought Reasoning

Before acting on any research task in this repo, reason explicitly through these steps:

1. **Source credibility first** — Before citing or building on a source, ask: "Who produced this? What incentives do they have? Is this primary research, a secondary summary, or opinion?" Weight primary sources higher. Flag opinion and vendor-produced content clearly.

2. **Triangulation** — Ask: "Is this finding corroborated by at least one independent source?" A single source is a lead, not a conclusion. If only one source supports a claim, note that explicitly rather than presenting it as established fact.

3. **Signal vs noise** — Ask: "Does this piece of information change what we'd recommend or decide? Or is it interesting but inconsequential?" Research that doesn't influence decisions is noise. Prioritise signal.

4. **Knowledge gap identification** — As you research, actively track what is *not* known. Ask: "What is the most important thing this research does not answer?" Unanswered questions are as valuable as answers — record them explicitly.

5. **Recency** — Ask: "When was this produced? Is this field moving fast enough that a 12-month-old source may already be outdated?" Flag recency risk on fast-moving topics.

6. **Synthesis over accumulation** — The goal is not to collect sources; it is to synthesise insight. Ask: "What is the single most important thing this body of research tells us, and why?" Lead with that.

7. **Improvement implication** — Does this session reveal a gap in research methodology, a missing source type, or a question that should become a standing research topic? Raise it in the Mini-Retro.

---

## When the Backlog Is Empty

When `BACKLOG.md` has no pending items (all are `done` or `archived`):

1. Review `Research/backlog/` — pick up a research item that hasn't been started.
2. Review open GitHub issues — propose a new Epic based on project state and issue content.
3. If neither applies, surface the question to the owner: describe the current state and ask what to prioritise next.

Do not invent work. Do not silently loop. Surface the state and ask.
