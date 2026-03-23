# ADR-0002: Agent Skills as a Git Submodule

Date: 2026-02-28
Status: accepted

## Context

Multiple AI agents work in this repository: GitHub Copilot Agent (reads `.github/`), Claude Code (reads `.claude/`), and future agents. Each agent needs access to a shared set of behavioural skills — focused instruction files that tell the agent *how* to perform specific tasks (e.g., `research`, `backlog-manager`, `citation-discipline`).

The skills are maintained in a separate repository ([`davidamitchell/Skills`](https://github.com/davidamitchell/Skills)) and shared across multiple repositories owned by the same author (this repo and `davidamitchell/Latest-developments-`).

The options considered were:

1. **Copy skill files directly** into this repo — simple, but creates duplicates and divergence risk.
2. **Reference skills by URL in AGENTS.md** — no file access at all; relies on agents fetching URLs, which is unreliable.
3. **Git submodule** — a pinned pointer to a specific commit in the Skills repo; updated on a schedule.

## Decision

Use git submodules to embed the Skills repo at two paths:

- `.github/skills/` — available to GitHub Copilot Agent (reads under `.github/`)
- `.claude/skills/` — available to Claude Code (reads under `.claude/`)

Both paths point to the same upstream repo (`davidamitchell/Skills`) and are pinned to the same commit SHA. A weekly GitHub Actions workflow (`.github/workflows/sync-skills.yml`) advances both pointers to the latest upstream commit on Mondays at 06:00 UTC.

The `.claude/CLAUDE.md` file is a thin stub pointing to `AGENTS.md` — matching the `Latest-developments-` pattern so that Claude Code picks up the full project instructions from the single source of truth.

## Consequences

### Positive
- Skills are versioned and reproducible — every clone gets the exact same skill files.
- A single weekly sync workflow keeps both submodules current without manual intervention.
- Skills are available as local files, so agents can read them without network calls.
- Adding or updating a skill requires only a change to `davidamitchell/Skills`; it propagates here on the next sync.

### Negative / Trade-offs
- Cloning the repo requires `--recurse-submodules` (or a follow-up `git submodule update --init`) to materialise the skill files.
- The weekly sync is a moving target — a new skill appears in agents' context only after the Monday sync or a manual workflow dispatch.

### Neutral
- The submodule SHA is pinned; if the Skills repo breaks, this repo is unaffected until the next sync.
