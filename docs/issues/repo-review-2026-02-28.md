# Repo Review — 2026-02-28

Issues raised by Claude during a structured review of the repository.
These are ready to be created as GitHub issues.

---

## Issue 1: MCP tools are partially available and environment references are inconsistent

**Labels:** `bug`, `infrastructure`

### Summary

`.mcp.json` configures 9 MCP servers, but only 3 are actually running in the
standard Claude Code web environment (memory, brave_search, github). The
remaining 6 are unavailable. The configuration also contains Codespaces-specific
assumptions that contradict the documented working environment.

### What's working

| Server | Status |
|---|---|
| `memory` | ✅ Running |
| `brave_search` | ✅ Running (requires BRAVE_API_KEY) |
| `github` | ✅ Running — but note: the MCP GitHub server cannot reach api.github.com in the Claude Code web environment (network issue, not a config issue). Confirmed during this review session. |
| `fetch` | ❌ Not available |
| `sequential_thinking` | ❌ Not available |
| `time` | ❌ Not available |
| `git` | ❌ Not available |
| `filesystem` | ❌ Not available (also has wrong path — see below) |
| `arxiv` | ❌ Not available |

### Specific problems

**1. Codespaces contradiction**

`AGENTS.md` states explicitly: *"Codespaces is not in use."*

Yet the MCP server reference table in `AGENTS.md` labels environment variables
as `BRAVE_API_KEY (Codespaces secret)` and `GITHUB_PERSONAL_ACCESS_TOKEN
(Codespaces secret)`. These need updating to reflect the actual environment
(repository secrets for GitHub Actions, or `.env` for local use).

**2. `filesystem` server hardcodes the Codespaces workspace path**

```json
"filesystem": {
  "command": "npx",
  "args": ["-y", "@modelcontextprotocol/server-filesystem", "/workspaces/Research"]
}
```

The actual working directory is `/home/user/Research`. This path never resolves
correctly outside Codespaces, making the filesystem MCP server non-functional
even if it were running.

**3. No agent guidance on tool availability verification**

Agents have no instruction to check which MCP tools are actually running at
session start, or to flag gaps before attempting to use a tool that isn't
available. This causes silent fallback to built-in tools without the agent or
user knowing.

### Suggested improvements

1. Fix the `filesystem` server path — use a relative path or an environment
   variable (e.g. `$WORKSPACE_PATH`) so it works outside Codespaces.
2. Update `AGENTS.md` secret references — replace "Codespaces secret" with
   "repository/environment secret" throughout.
3. Add a **session-start MCP check** to `AGENTS.md`: at the start of each
   session agents should note which MCP tools are available and flag configured
   servers that are not running.
4. Document which servers are expected in the Claude Code web environment vs.
   which require additional setup (local install, Codespaces, etc.).

### Files to update

- `.mcp.json` — fix filesystem path
- `.github/mcp.json` — fix filesystem path (keep `"type": "stdio"` entries)
- `AGENTS.md` — update secret references, add tool availability section,
  add session-start check instruction

---

## Issue 2: Agent skills are inaccessible and the invocation model is undefined

**Labels:** `enhancement`, `documentation`

### Summary

The seven skills listed in `AGENTS.md` (backlog-manager, citation-discipline,
remove-ai-slop, research, speculation-control, strategic-persuasion,
strategy-author) are not accessible to agents in practice. The submodules are
empty in the standard clone, and `AGENTS.md` does not explain how to invoke
skills in Claude Code's `/skill-name` model.

### Specific problems

**1. Submodules are empty without explicit initialisation**

Both `.github/skills/` and `.claude/skills/` are git submodule directories
that point to `davidamitchell/Skills`, but they contain no files in a standard
`git clone`. Without `git submodule update --init`, agents cannot read any
skill files.

Neither `README.md` nor `AGENTS.md` mentions this requirement prominently.
A cloning agent would see empty skill directories and have no instructions
about what to do.

**2. The invocation mechanism is not documented**

`AGENTS.md` lists skills in a table but does not explain:
- How Claude Code discovers skills (it reads `.claude/skills/*.md` files and
  exposes them as `/skill-name` slash commands)
- How to invoke a skill within a session (type `/skill-name` in the prompt)
- What format skill files must follow to be recognised

A GitHub Copilot agent has no equivalent mechanism at all — skills in
`.github/skills/` are not a standard Copilot feature, so the table in
`AGENTS.md` misleads Copilot agents about capability it doesn't have.

**3. No fallback behaviour defined**

When skills are unavailable (submodule not initialised, or running under
Copilot), agents have no instruction on how to proceed. Should they note the
gap? Attempt equivalent behaviour inline? The current instructions are silent.

### Suggested improvements

1. Add a **Quick start** step to `README.md`: `git submodule update --init`
   after cloning.
2. Add a **Skills invocation** section to `AGENTS.md` explaining:
   - Skills are invoked in Claude Code via `/skill-name`
   - Skill files live in `.claude/skills/*.md`
   - GitHub Copilot does not support the same mechanism (explain equivalent
     behaviour or remove the Copilot skills table)
3. Add fallback instructions: when a skill is not available, the agent should
   note this and proceed with inline equivalent behaviour (e.g. run
   citation-discipline logic manually).
4. Consider whether the Copilot skills table in `AGENTS.md` should be
   replaced with Copilot-specific guidance instead.

### Files to update

- `README.md` — add `git submodule update --init` to quick-start steps
- `AGENTS.md` — add skills invocation section, clarify Copilot vs Claude Code
  differences, add fallback behaviour

---

## Issue 3: Instructions lack a self-improvement loop and have documentation maintenance gaps

**Labels:** `enhancement`, `documentation`

### Summary

The Mini-Retro framework in `AGENTS.md` is a strong foundation for continuous
improvement, but there is no explicit instruction to feed Mini-Retro findings
back into `AGENTS.md` itself or into new `BACKLOG.md` items. Additionally,
`BACKLOG.md` currently has no future work items (all 26 are done), with no
guidance on what happens next. Several parts of the directory structure are
also undocumented.

### Specific problems

**1. Mini-Retro findings have no pathway back into the system**

`AGENTS.md` defines a Mini-Retro with three questions:
> "What went wrong? What caused it? How can the instructions be improved?"

But there is no instruction stating:
- **Update `AGENTS.md`** when a new convention would prevent the problem from
  recurring
- **Add a `BACKLOG.md` item** when a systemic issue needs a code or
  infrastructure fix
- **Update `PROGRESS.md`** with the retro outcome so the next agent sees the
  learning

Without these explicit steps, retro findings accumulate only in `PROGRESS.md`
session notes and are likely forgotten.

**2. `BACKLOG.md` has no future work and no next-step guidance**

All 26 work items (W-0001 to W-0026) are complete. `AGENTS.md` is silent on
what to do when the backlog is empty:
- Should agents generate a new Epic proposal?
- Should agents move items from `Research/backlog/` into code work?
- Should agents prompt the user to define the next phase?

The system needs a "what next" instruction for the empty-backlog state.

**3. `AGENTS.md` itself has no update protocol**

There is no instruction saying when or how `AGENTS.md` should be updated.
Every other document has a defined update trigger:
- `PROGRESS.md` — after every meaningful commit
- `BACKLOG.md` — at slice completion checklist
- ADRs — when a significant architectural decision is made

`AGENTS.md` (the most important document in the repo) has none. An agent
discovering a new pattern or tool capability has no guidance to update it.

**4. Directory layout in `AGENTS.md` is incomplete**

The documented layout in `AGENTS.md` is missing:
- `Research/transcripts/` — created by the `fetch-transcript` GitHub Actions
  workflow and confirmed in `fetch-transcript.yml`
- `state/` — the JSON state store directory used by `StateStore` in `src/state.py`

These missing entries mean agents reading the layout will not know where
transcripts or state files live.

### Suggested improvements

1. **Extend the Mini-Retro section** to explicitly state:
   > "If a new convention would have prevented this problem, add it to
   > `AGENTS.md` now. If a systemic fix is needed, add a `BACKLOG.md` item."

2. **Add an empty-backlog protocol**: when `BACKLOG.md` has no pending items,
   agents should: (a) review `Research/backlog/` for items to start, (b)
   propose a new Epic based on project state, or (c) prompt the user for
   direction.

3. **Add an `AGENTS.md` update trigger**: document should be updated when:
   - A new MCP server, skill, or tool is added or removed
   - A new convention is established via Mini-Retro
   - The project structure changes materially

4. **Fix the directory layout** in `AGENTS.md` to include `Research/transcripts/`
   and `state/`.

5. **Consider adding**: a periodic instruction (e.g. at the start of every
   fifth session) to do a full doc-currency pass — check that `README.md`,
   `AGENTS.md`, `BACKLOG.md`, and `PROGRESS.md` accurately reflect current
   project state.

### Files to update

- `AGENTS.md` — Mini-Retro extension, empty-backlog protocol, update trigger,
  directory layout fix
- `PROGRESS.md` — record these findings in the next session log

---

*Review conducted by Claude (claude-sonnet-4-6) on 2026-02-28.*
*Branch: `claude/github-issue-creation-E3gLT`*
