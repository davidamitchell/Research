---
title: "The role of AGENTS.md in a repo using .github/copilot-instructions.md as the sole instructions source"
added: 2026-03-28
status: backlog
priority: medium
blocks: []
tags: [agents-md, copilot, claude, instructions, cross-agent, consistency]
started: ~
completed: ~
output: [knowledge, backlog-item]
---

# The role of AGENTS.md in a repo using .github/copilot-instructions.md as the sole instructions source

## Question / Hypothesis

`AGENTS.md` has emerged as the cross-tool convergence format for agent project instructions, supported by OpenAI Codex, GitHub Copilot, Claude Code, Cursor, Aider, Gemini CLI, and others. This repo deleted `AGENTS.md` in Architecture Decision Record (ADR)-0006 (2026-03-07) in favour of `.github/copilot-instructions.md` as the single source of truth. Is that the right call? What does each tool actually read, and should `AGENTS.md` be restored — as content, as a pointer, or not at all?

### Q1 — What tools read `AGENTS.md` vs `.github/copilot-instructions.md`

- For the tools used in this repo (Copilot coding agent via GitHub Issues, Claude iOS `code` feature, the `research-loop.yml` Copilot CLI workflow): which of these read `AGENTS.md` at the repo root? Which read `.github/copilot-instructions.md`? Do any read both?
- Is there a confirmed loading order or priority between the two files for any of these tools?
- Does the `agents.md` specification define a standard for where the file must live (root only, or directory-scoped)?

### Q2 — The pointer pattern vs content duplication

- If `AGENTS.md` needs to exist for cross-tool compatibility but `.github/copilot-instructions.md` holds the content, is the correct pattern a one-line `AGENTS.md` that says "see `.github/copilot-instructions.md`"?
- Do agents (Copilot, Claude) follow pointer/import patterns in instruction files, or do they treat the file content literally?
- What did the previous `AGENTS.md` contain before ADR-0006 deleted it? Is any of that content now absent from `copilot-instructions.md`?

### Q3 — Consistency with other repos in the davidamitchell organisation

- Do `davidamitchell/Latest-developments-`, `davidamitchell/Agent-Evaluation`, `davidamitchell/Personal-Assistant-`, `davidamitchell/Memory-System`, and `davidamitchell/Policy-LSP` have an `AGENTS.md` at root?
- Is the current Research repo setup (no `AGENTS.md`, no `CLAUDE.md`) consistent with the rest of the organisation, or is it an outlier?
- What is the correct organisation-wide standard: `AGENTS.md` as primary with `copilot-instructions.md` pointing to it, or `copilot-instructions.md` as primary with `AGENTS.md` optionally pointing to it?

## Context

ADR-0006 recorded that deleting `AGENTS.md` was a deliberate choice: it noted as a trade-off that "Claude Code no longer has a `.claude/` directory; it must use `.github/copilot-instructions.md` directly." Prior research (`Research/completed/2026-03-08-ai-coding-harnesses-agent-philosophy.md`) documents `AGENTS.md` as the cross-vendor standard. Prior research (`Research/completed/2026-03-22-using-awesome-copilot-across-repos.md`) notes that GitHub web already reads `AGENTS.md` and that it outranks workflows and plugins for improving agent behaviour. The Research repo is the only repo in the organisation confirmed to have deleted `AGENTS.md`.

## Assumptions

- **Assumption:** Other repos in the organisation have `AGENTS.md`. **Justification:** Prior research references `AGENTS.md` in `Latest-developments-` and `awesome-copilot`. Needs verification across all repos.
- **Assumption:** A thin pointer `AGENTS.md` (one line referencing `copilot-instructions.md`) is sufficient for cross-tool compatibility. **Justification:** Plausible but unverified — agents may not follow file pointers.

## Analysis

*(Research agent to complete)*

## Risks, Gaps, and Uncertainties

- If `AGENTS.md` is not read by the primary tools used in this repo (Copilot coding agent, Claude iOS), restoring it adds no value.
- If the pointer pattern does not work (agents read the file literally), restoring `AGENTS.md` with a pointer creates silent context loss.

## Open Questions

- Does the Copilot coding agent read `AGENTS.md` at the repo root when assigned a GitHub issue?
- Does Claude iOS `code` feature read `AGENTS.md`?
- Do any of the other davidamitchell repos have `AGENTS.md` today?

---

## Research Skill Output

*(Research agent to complete)*

## Findings

*(Research agent to complete)*

## Output

- Type: knowledge, backlog-item
- Description: Confirmed role of AGENTS.md for this repo's tools; organisation-wide consistency assessment; recommendation on whether to restore AGENTS.md and in what form.
- Links:
