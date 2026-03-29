---
title: "Agent instruction loading and skills access: Copilot coding agent, Claude iOS code feature, and the role of AGENTS.md"
added: 2026-03-28
status: backlog
priority: high
blocks: [2026-03-28-environment-setup-consistency]
tags: [copilot, claude, ios, agents-md, skills, instructions, github-issues]
started: ~
completed: ~
output: [knowledge, backlog-item]
---

# Agent instruction loading and skills access: Copilot coding agent, Claude iOS code feature, and the role of AGENTS.md

## Question / Hypothesis

Given the current repo setup — instructions in `.github/copilot-instructions.md`, skills submodule at `.github/skills/`, no `AGENTS.md` at root, no `CLAUDE.md` at root — what does each agent actually load at the point it starts work, and does it have access to the skills?

### Q1 — GitHub Copilot coding agent (GitHub issue → assign to Copilot → draft PR)

- When a GitHub issue is assigned to Copilot via the GitHub Issues UI, which files does it read before starting planning? Does it read `.github/copilot-instructions.md` automatically? Does it read `.github/skills/`? Does it look for `AGENTS.md` at the repo root?
- What is the confirmed loading order: does `.github/copilot-instructions.md` take priority over a root `AGENTS.md` if both exist?
- Does the Copilot coding agent materialise the skills submodule (run `git submodule update`) before reading `.github/skills/`, or does it see an empty directory?

### Q2 — Claude iOS app (`code` section / feature)

- When the Research repo is opened in Claude's iOS `code` feature, which files does Claude load into context? Does it look for `CLAUDE.md`, `AGENTS.md`, or `.github/copilot-instructions.md`? Does it read any of them automatically?
- Can Claude iOS access `.github/skills/`? What path does it scan for instructions?
- Does the `code` feature on iOS behave identically to Claude Code CLI in terms of file-loading behaviour, or is it a different surface with different rules?

### Q3 — The role of `AGENTS.md` for both agents

- `AGENTS.md` is the emerging cross-tool convergence format (supported by Copilot, Claude Code, Cursor, Aider, Codex, Gemini CLI). Architecture Decision Record (ADR)-0006 deleted it from this repo in favour of `.github/copilot-instructions.md`. Does the Copilot coding agent read `AGENTS.md` at the repo root when assigned a GitHub issue? Does Claude iOS?
- If both agents read `AGENTS.md`, is the right answer to restore it as a thin pointer to `.github/copilot-instructions.md`, or to move content back to `AGENTS.md` and have `copilot-instructions.md` point to it?
- Does restoring `AGENTS.md` break ADR-0006 or supersede it?

## Context

This repo's primary agent entry points are: (1) assigning a GitHub issue to the Copilot coding agent via the GitHub Issues UI, and (2) using the Claude iOS app's `code` feature to work directly against the repo. Neither involves a local IDE or Claude Code CLI. ADR-0006 (2026-03-07) removed `AGENTS.md` and `.claude/CLAUDE.md` on the assumption that `.github/copilot-instructions.md` was sufficient for all agents. That assumption is unverified for these two specific entry points.

Prior research: `Research/completed/2026-03-08-ai-coding-harnesses-agent-philosophy.md` documents `AGENTS.md` as the cross-vendor standard supported by Copilot, Claude Code, and others. `Research/completed/2026-03-04-sdlc-ai-prompt-patterns.md` (Software Development Life Cycle (SDLC) prompt patterns) documents the fragmented context file ecosystem. ADR-0006 is in `docs-adr/0006-standardise-agent-instructions.md`.

## Assumptions

- **Assumption:** The Copilot coding agent reads `.github/copilot-instructions.md` automatically when assigned an issue. **Justification:** GitHub documentation states this file provides repository custom instructions for Copilot. Needs verification for the coding agent specifically.
- **Assumption:** Claude iOS `code` feature has the same context file loading behaviour as Claude Code CLI. **Justification:** Both are Anthropic products. Unverified — Claude iOS is a distinct surface.

## Analysis

*(Research agent to complete)*

## Risks, Gaps, and Uncertainties

- Anthropic documentation for the Claude iOS `code` feature may be sparse or absent.
- GitHub documentation may not distinguish between Copilot chat and the Copilot coding agent for instruction file loading.
- The answer may vary by Copilot plan tier.

## Open Questions

- Does the Copilot coding agent run `git submodule update --init` before reading `.github/skills/`?
- Does `AGENTS.md` take precedence over `.github/copilot-instructions.md` or vice versa for the Copilot coding agent?
- Does Claude iOS `code` feature recursively scan parent directories for `CLAUDE.md` the same way Claude Code CLI does?

---

## Research Skill Output

*(Research agent to complete)*

## Findings

*(Research agent to complete)*

## Output

- Type: knowledge, backlog-item
- Description: Confirmed loading behaviour for both agents; ADR updated or superseded if needed; backlog items W-0035 and W-0036 informed by findings.
- Links:
