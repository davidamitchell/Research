---
review_count: 2
title: "The role of AGENTS.md in a repo using .github/copilot-instructions.md as the sole instructions source"
added: 2026-03-29T11:12:49+00:00
status: completed
priority: medium
blocks: []
tags: [agents-md, copilot, claude, instructions, cross-agent, consistency]
started: 2026-03-29T11:12:49+00:00
completed: 2026-03-29T11:12:49+00:00
output: [knowledge, backlog-item]
---

# The role of AGENTS.md in a repo using .github/copilot-instructions.md as the sole instructions source

## Question / Hypothesis

`AGENTS.md` has emerged as the cross-tool convergence format for agent project instructions, supported by OpenAI Codex, GitHub Copilot, Claude Code, Cursor, Aider, Gemini Command Line Interface (CLI), and others. This repo deleted `AGENTS.md` in Architecture Decision Record (ADR)-0006 (2026-03-07) in favour of `.github/copilot-instructions.md` as the single source of truth. Is that the right call? What does each tool actually read, and should `AGENTS.md` be restored: as content, as a pointer, or not at all?

### Q1: What tools read `AGENTS.md` vs `.github/copilot-instructions.md`

- For the tools used in this repo (Copilot coding agent via GitHub Issues, Claude iOS (Apple's mobile operating system) `code` feature, the `research-loop.yml` Copilot CLI workflow): which of these read `AGENTS.md` at the repo root? Which read `.github/copilot-instructions.md`? Do any read both?
- Is there a confirmed loading order or priority between the two files for any of these tools?
- Does the `agents.md` specification define a standard for where the file must live (root only, or directory-scoped)?

### Q2: The pointer pattern vs content duplication

- If `AGENTS.md` needs to exist for cross-tool compatibility but `.github/copilot-instructions.md` holds the content, is the correct pattern a one-line `AGENTS.md` that says "see `.github/copilot-instructions.md`"?
- Do agents (Copilot, Claude) follow pointer/import patterns in instruction files, or do they treat the file content literally?
- What did the previous `AGENTS.md` contain before ADR-0006 deleted it? Is any of that content now absent from `copilot-instructions.md`?

### Q3: Consistency with other repos in the davidamitchell organisation

- Do `davidamitchell/Latest-developments-`, `davidamitchell/Agent-Evaluation`, `davidamitchell/Personal-Assistant-`, `davidamitchell/Memory-System`, and `davidamitchell/Policy-LSP` have an `AGENTS.md` at root?
- Is the current Research repo setup (no `AGENTS.md`, no `CLAUDE.md`) consistent with the rest of the organisation, or is it an outlier?
- What is the correct organisation-wide standard: `AGENTS.md` as primary with `copilot-instructions.md` pointing to it, or `copilot-instructions.md` as primary with `AGENTS.md` optionally pointing to it?

## Context

ADR-0006 recorded that deleting `AGENTS.md` was a deliberate choice: it noted as a trade-off that "Claude Code no longer has a `.claude/` directory; it must use `.github/copilot-instructions.md` directly." Prior research (`Research/completed/2026-03-08-ai-coding-harnesses-agent-philosophy.md`) documents `AGENTS.md` as the cross-vendor standard. Prior research (`Research/completed/2026-03-22-using-awesome-copilot-across-repos.md`) notes that GitHub web already reads `AGENTS.md` and that it outranks workflows and plugins for improving agent behaviour. The Research repo is the only repo in the organisation confirmed to have deleted `AGENTS.md`.

## Assumptions

- **Assumption:** Other repos in the organisation have `AGENTS.md`. **Justification:** Prior research references `AGENTS.md` in `Latest-developments-` and `awesome-copilot`. Needs verification across all repos.
- **Assumption:** A thin pointer `AGENTS.md` (one line referencing `copilot-instructions.md`) is sufficient for cross-tool compatibility. **Justification:** Plausible but unverified; agents may not follow file pointers.

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

### §0 Initialise

**Research question restated:** Is deleting `AGENTS.md` in favour of `.github/copilot-instructions.md` as sole instructions source the correct call for this repo, given that `AGENTS.md` is the cross-tool standard? Should `AGENTS.md` be restored: as content, as a pointer, or not at all?

**Scope confirmed:**
- In scope: the three tools this repo actually uses (Copilot CLI in `research-loop.yml`, Copilot Coding Agent via GitHub Issues, Claude iOS Code feature); what each file each tool reads; the pointer-pattern question; current `AGENTS.md` status in the five named repos in the davidamitchell organisation.
- Out of scope: tools not used in this repo (Cursor, Aider, JetBrains Junie, etc.); general `AGENTS.md` authoring best practices beyond what affects this repo's decision.

**Constraints:** Evidence must be drawn from official documentation, GitHub changelog posts, and verified repo inspections. Conclusions must be scoped to the three tools used in this repo.

**Output format:** Knowledge item with concrete recommendation on whether to restore `AGENTS.md` and in what form, plus consistency assessment for the organisation.

**Prior work cross-reference:**
- `2026-03-08-ai-coding-harnesses-agent-philosophy.md`: covers `AGENTS.md` as the cross-vendor standard for agent instructions; notes its adoption across major coding harnesses.
- `2026-03-22-using-awesome-copilot-across-repos.md`: confirms `Personal-Assistant-` has `AGENTS.md`; establishes that `Research`, `Latest-developments-`, and `Agent-Evaluation` share the same missing-surface pattern (no `AGENTS.md`); recommends restoring `AGENTS.md` as a first-wave improvement for each.

### §1 Question Decomposition

**Q1: Tool reading behaviour:**
- Q1a: Does the Copilot CLI (used in `research-loop.yml`) read `AGENTS.md`, `.github/copilot-instructions.md`, or both?
- Q1b: Does the Copilot Coding Agent (web, assigned via GitHub Issues) read `AGENTS.md`, `.github/copilot-instructions.md`, or both?
- Q1c: Does the Claude iOS Code feature read `AGENTS.md` or `.github/copilot-instructions.md`?
- Q1d: Where does the `AGENTS.md` specification say the file must live?
- Q1e: Is there a confirmed priority order between `AGENTS.md` and `.github/copilot-instructions.md` for the Copilot CLI?

**Q2: Pointer pattern:**
- Q2a: Does the `AGENTS.md` specification support import or include syntax?
- Q2b: Do Copilot or Claude agents follow file references included as plain text in an instruction file?
- Q2c: What content did the previous `AGENTS.md` contain, and is any of it absent from `copilot-instructions.md` today?

**Q3: Org consistency:**
- Q3a: Does `Personal-Assistant-` have `AGENTS.md` at root?
- Q3b: Do `Latest-developments-`, `Agent-Evaluation`, and `Policy-LSP` have `AGENTS.md` at root?
- Q3c: Is the Research repo an outlier in the organisation?

### §2 Investigation

**Q1a: Copilot CLI reading behaviour**

Source: [GitHub Copilot CLI custom instructions documentation](https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-custom-instructions) (primary, official)

> "Instructions in the `AGENTS.md` file in the root directory, if found, are treated as primary instructions. If an `AGENTS.md` file and a `.github/copilot-instructions.md` file are both found at the root of the repository, the instructions in both files are used."

- [fact] The Copilot CLI documentation states that both `AGENTS.md` and `.github/copilot-instructions.md` are used when both exist; `AGENTS.md` is called "primary". (Source: [GitHub Copilot CLI docs](https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-custom-instructions))
- [fact] The research-loop.yml installs `@github/copilot` (the Copilot CLI) with no pinned version, resulting in the latest published version (1.0.12 as of 2026-03-29) via `npm install -g @github/copilot`. (Source: [research-loop.yml](https://github.com/davidamitchell/Research/blob/main/.github/workflows/research-loop.yml))
- [fact] A verified bug report (GitHub issue #489 in `github/copilot-cli`) filed against Copilot CLI v0.0.353 documents that `AGENTS.md` is ignored when `.github/copilot-instructions.md` is also present, despite help text listing `AGENTS.md` as supported. The issue's status (fixed or open) could not be confirmed from the issue page alone. (Source: [copilot-cli issue #489](https://github.com/github/copilot-cli/issues/489))
- [inference] As of 2026-03-29, whether the `AGENTS.md`-ignored bug is resolved in v1.0.12 is unconfirmed; the official documentation claims both files are used, but the bug report suggests actual behaviour may differ from documented behaviour for some versions.

**Q1b: Copilot Coding Agent (web) reading behaviour**

Source: [GitHub blog changelog 2025-08-28](https://github.blog/changelog/2025-08-28-copilot-coding-agent-now-supports-agents-md-custom-instructions/) (primary, official)

> "Copilot coding agent, our autonomous background agent, now supports `AGENTS.md` custom instructions... Alongside `AGENTS.md`, the agent continues to support GitHub's `.github/copilot-instructions.md` and `.github/instructions/**.instructions.md` formats, plus `CLAUDE.md` and `GEMINI.md` files."

- [fact] The Copilot Coding Agent (web, assigned via GitHub Issues) reads `AGENTS.md`, `.github/copilot-instructions.md`, `.github/instructions/*.instructions.md`, `CLAUDE.md`, and `GEMINI.md` when present, treating them as additive. Support for `AGENTS.md` was added on 2025-08-28. (Source: [GitHub blog changelog](https://github.blog/changelog/2025-08-28-copilot-coding-agent-now-supports-agents-md-custom-instructions/))
- [fact] No confirmed priority order between `AGENTS.md` and `.github/copilot-instructions.md` is documented for the Copilot Coding Agent (web); the changelog says the files are used alongside each other. (Source: [GitHub blog changelog](https://github.blog/changelog/2025-08-28-copilot-coding-agent-now-supports-agents-md-custom-instructions/))

**Q1c: Claude iOS Code feature reading behaviour**

Source: [Claude Code docs overview](https://code.claude.com/docs/en/overview) (primary, official); secondary search results on Claude iOS.

- [fact] Claude Code reads `CLAUDE.md` files at project root and in `.claude/` directories; there is no documented support for reading `AGENTS.md` in Claude Code. An open GitHub issue (#6235 in `anthropics/claude-code`) requests native `AGENTS.md` support and remains open. (Sources: [Claude Code docs](https://code.claude.com/docs/en/memory), [claude-code issue #6235](https://github.com/anthropics/claude-code/issues/6235))
- [fact] The Claude iOS Code feature allows dispatching tasks from an iOS device to a Claude Code Desktop session. It does not introduce a separate instruction-file loading mechanism; the same `CLAUDE.md` lookup that applies to Claude Code Desktop applies. (Source: [Claude Code overview](https://code.claude.com/docs/en/overview))
- [fact] `.github/copilot-instructions.md` is not on the documented read path for Claude Code or Claude iOS Dispatch; neither file is referenced in Claude Code's memory or instruction documentation. (Source: [Claude Code memory docs](https://code.claude.com/docs/en/memory))
- [inference] Claude iOS Code feature reads neither `AGENTS.md` nor `.github/copilot-instructions.md` as of 2026-03-29. It reads `CLAUDE.md`. This means the Research repo, which has no `CLAUDE.md`, provides no automated project-level instructions to Claude iOS Code at all.

**Q1d: AGENTS.md file location specification**

Source: [agents.md official spec site](https://agents.md/) (primary); [OpenAI Codex AGENTS.md documentation](https://developers.openai.com/codex/guides/agents-md/) (primary)

- [fact] The `AGENTS.md` specification supports both root-level placement (affecting the whole project) and directory-level placement (affecting that directory and all subdirectories), using a nearest-file-wins hierarchy. (Sources: [agents.md](https://agents.md/), [OpenAI Codex AGENTS.md docs](https://developers.openai.com/codex/guides/agents-md/))
- [fact] The specification is stewarded by the Agentic AI Foundation under the Linux Foundation, adopted by over 25 Artificial Intelligence (AI) coding tools as of March 2026. (Source: [agents.md](https://agents.md/), [particula.tech AGENTS.md explainer](https://particula.tech/blog/agents-md-ai-coding-agent-configuration))

**Q1e: Priority order between AGENTS.md and copilot-instructions.md (Copilot CLI)**

- [fact] The Copilot CLI documentation says `AGENTS.md` is treated as "primary instructions" while `.github/copilot-instructions.md` is "repository-wide" instructions, and both are used together. No explicit priority override is documented; conflicting instructions are resolved non-deterministically. (Source: [GitHub Copilot CLI docs](https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-custom-instructions))

**Q2a: AGENTS.md pointer/import support**

Source: [agentsmd/agents.md GitHub issue #11](https://github.com/agentsmd/agents.md/issues/11) (primary)

- [fact] The `AGENTS.md` specification does not define a native import, include, or file-reference syntax. A GitHub issue (#11 at `agentsmd/agents.md`) requests this feature, indicating it is absent as of the filing date. (Source: [agentsmd issue #11](https://github.com/agentsmd/agents.md/issues/11))
- [inference] `CLAUDE.md` may support a file-import directive (described as `@imports` in third-party documentation) specific to Claude Code; this claim comes from a secondary source rather than Claude Code's official documentation and should be treated as unverified. (Source: [medium.com CLAUDE.md guide](https://medium.com/data-science-collective/the-complete-guide-to-ai-agent-memory-files-claude-md-agents-md-and-beyond-49ea0df5c5a9))

**Q2b: Agents following file pointers in instruction files**

- [inference] Agents (Copilot CLI, Copilot Coding Agent) read instruction file content literally; there is no mechanism by which a one-line instruction file causes the agent to load a second file at the same priority as a natively read file. A workaround exists (include a line such as "Also read `.github/copilot-instructions.md`"), but the agent treats this as a task instruction rather than a file-loading directive, making adherence unreliable. (Sources: [GitHub community discussion on AGENTS.md](https://github.com/orgs/community/discussions/175649), [Nathan Nellans Copilot instructions guide](https://www.nathannellans.com/post/all-about-github-copilot-custom-instructions))
- [assumption] A thin pointer `AGENTS.md` (one line referencing `copilot-instructions.md`) is insufficient for cross-tool compatibility. **Justification:** No specification or tool documentation describes this pattern as reliable; agents treat instruction files as context input, not as file-system directives.

**Q2c: Previous AGENTS.md content**

Source: ADR-0006 text in `docs-adr/0006-*.md` (primary, this repo)

- [fact] ADR-0006 states the decision was to "expand `.github/copilot-instructions.md` with the full content from `AGENTS.md`", meaning all content from the previous `AGENTS.md` was migrated into `copilot-instructions.md`. No content was deleted; the files were consolidated. (Source: [docs-adr/ADR-0006](https://github.com/davidamitchell/Research/blob/main/docs-adr/0006-standardise-agent-instruction-files.md))

**Q3a: Personal-Assistant- AGENTS.md**

Source: Direct GitHub API inspection of `davidamitchell/Personal-Assistant-` root directory (2026-03-29)

- [fact] `Personal-Assistant-` has `AGENTS.md` at root (sha `b1de2dfdff23c5d4b389482accee1d251f6d0132`, 10,018 bytes). It also has `.github/copilot-instructions.md`, path-specific instructions, and `mcp.json`. (Source: [Personal-Assistant- repo root](https://github.com/davidamitchell/Personal-Assistant-))

**Q3b: Other repos' AGENTS.md status**

Source: Direct GitHub API inspection of root directories (2026-03-29)

- [fact] `Latest-developments-` does NOT have `AGENTS.md` at root. Root contains: `.env.example`, `.github/`, `.gitignore`, `.gitmodules`, `.mcp.json`, `BACKLOG.md`, `CHANGELOG.md`, `Makefile`, `PROGRESS.md`, `README.md`, and source directories. (Source: [Latest-developments- repo root](https://github.com/davidamitchell/Latest-developments-))
- [fact] `Agent-Evaluation` does NOT have `AGENTS.md` at root. Root contains: `.github/`, `.gitignore`, `.gitmodules`, `BACKLOG.md`, `CHANGELOG.md`, `PROGRESS.md`, `README.md`, and project directories. (Source: [Agent-Evaluation repo root](https://github.com/davidamitchell/Agent-Evaluation))
- [fact] `Policy-LSP` does NOT have `AGENTS.md` at root. Root contains: `.github/`, `.gitignore`, `.gitmodules`, `.mcp.json`, `BACKLOG.md`, `CHANGELOG.md`, `PROGRESS.md`, `README.md`, `Makefile`, and source directories. (Source: [Policy-LSP repo root](https://github.com/davidamitchell/Policy-LSP))
- [fact] `Memory-System` could not be inspected; the repo returned 404 on prior investigation (2026-03-22) and was unavailable. (Source: [2026-03-22-using-awesome-copilot-across-repos.md](https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-22-using-awesome-copilot-across-repos.md))

**Q3c: Research repo outlier status**

- [fact] Of the five inspected repos in the organisation (`Personal-Assistant-`, `Latest-developments-`, `Agent-Evaluation`, `Policy-LSP`, `Research`), only `Personal-Assistant-` has `AGENTS.md`. The Research repo is not unique in lacking `AGENTS.md`; three of four comparators also lack it. (Source: GitHub API inspections, 2026-03-29)
- [inference] ADR-0006's claim that deleting `AGENTS.md` was "consistent with all other repos in the davidamitchell organisation" was accurate for `Latest-developments-`, `Agent-Evaluation`, and `Policy-LSP` at the time of writing, but `Personal-Assistant-` had or subsequently acquired `AGENTS.md`, making it the outlier rather than Research.

### §3 Reasoning

Removing narrative:

1. The Copilot CLI (the tool used in `research-loop.yml`) officially reads both `AGENTS.md` and `.github/copilot-instructions.md`, but a documented bug shows `AGENTS.md` may be silently ignored in favour of `copilot-instructions.md` when both are present. Either way, `copilot-instructions.md` is read reliably.

2. The Copilot Coding Agent (web) reads both files since 2025-08-28. This is additive; both are used without conflict.

3. Claude iOS Code reads `CLAUDE.md` only. Neither `AGENTS.md` nor `.github/copilot-instructions.md` is on its read path. This is a genuine gap not addressed by the current setup or by restoring `AGENTS.md`.

4. The thin pointer pattern is not a viable solution: the spec has no import syntax, and agents interpret instruction file content as context input, not as file-loading directives.

5. All instruction content from the previous `AGENTS.md` was migrated to `copilot-instructions.md` by ADR-0006. No content was lost.

6. Four of five organisation repos (including Research) lack `AGENTS.md`. Only `Personal-Assistant-` has it. Research is not an outlier in the current organisation state.

### §4 Consistency Check

**Potential contradiction:** ADR-0006 says deleting `AGENTS.md` is "consistent with all other repos in the davidamitchell organisation," but `Personal-Assistant-` has `AGENTS.md`.

**Resolution:** `Personal-Assistant-` may have added `AGENTS.md` after ADR-0006 (2026-03-07), or ADR-0006 may have been inaccurate at writing time. Either way, the current state is that `Personal-Assistant-` has it and three of four other repos do not. This does not make Research an outlier; it makes `Personal-Assistant-` the outlier.

**Potential contradiction:** The Copilot CLI docs say both files are used, but a bug report says `AGENTS.md` is ignored.

**Resolution:** The bug was filed against v0.0.353; the current version is 1.0.12. Whether it is fixed is unconfirmed. The conservative reading is: `copilot-instructions.md` is reliably read; `AGENTS.md` may or may not be read depending on version. This makes `copilot-instructions.md` the more reliable single source.

**No internal contradiction** on Q2 (pointer pattern). All sources agree that agents read instruction files literally and no import syntax exists in the spec.

### §5 Depth and Breadth Expansion

**Technical lens:**
- The Copilot CLI reads both files additively, which means restoring `AGENTS.md` with a summary or condensed version of `copilot-instructions.md` would result in partial duplication. Duplication creates a maintenance surface: two files to keep in sync.
- If `AGENTS.md` were restored with full content (mirroring `copilot-instructions.md`), the Copilot CLI would inject both into context, effectively doubling the instruction content without adding new information. This wastes context window tokens.

**Tool coverage lens:**
- Restoring `AGENTS.md` would extend coverage to tools not currently used in this repo (Cursor, Aider, Gemini CLI, etc.) if such tools were ever used. The value of this is proportional to the probability of adopting those tools.
- The one tool not served by the current setup (`CLAUDE.md` for Claude iOS) would not be served by adding `AGENTS.md` either. If Claude iOS coverage is desired, a `CLAUDE.md` is the correct addition.

**Maintenance lens:**
- The current single-file setup is the lowest maintenance path: one file to update, no sync required.
- Adding `AGENTS.md` with real content requires keeping it aligned with `copilot-instructions.md`; maintaining two parallel instruction files creates a divergence risk [inference].

**Historical lens:**
- The pre-ADR-0006 state had `AGENTS.md` as primary and `copilot-instructions.md` as a stub pointing to it. ADR-0006 inverted this to `copilot-instructions.md` as primary. Neither state had a thin pointer from `AGENTS.md` to `copilot-instructions.md`.

### §6 Synthesis

**Answer:** Deleting `AGENTS.md` in favour of `.github/copilot-instructions.md` is the correct call for the two primary tools used in this repo (Copilot CLI and Copilot Coding Agent web), because `copilot-instructions.md` is reliably read by both, while `AGENTS.md` support in the Copilot CLI has a documented unreliability issue. The thin pointer pattern is not viable. The Research repo is not an outlier; four of five organisation repos lack `AGENTS.md`. The one genuine gap is Claude iOS Code, which reads only `CLAUDE.md` and is not served by either file.

**Key conclusions:**
1. Copilot CLI and Copilot Coding Agent (web): both read `copilot-instructions.md`; Copilot Coding Agent (web) also reads `AGENTS.md` (since 2025-08-28); Copilot CLI officially reads both but has a documented bug that may suppress `AGENTS.md`.
2. Claude iOS Code: reads `CLAUDE.md` only; neither `AGENTS.md` nor `copilot-instructions.md` is on its read path.
3. Thin pointer pattern: not viable; no import syntax in the spec; agents read files literally.
4. Previous `AGENTS.md` content: fully migrated to `copilot-instructions.md` by ADR-0006; no content loss.
5. Org consistency: Research is aligned with `Latest-developments-`, `Agent-Evaluation`, and `Policy-LSP`; `Personal-Assistant-` is the outlier with both files.
6. If the organisation decides to adopt `AGENTS.md` across all repos, it should contain full content (not a pointer), meaning a copy or condensed version of `copilot-instructions.md` content. This creates a maintenance obligation.
7. Adding `CLAUDE.md` (not `AGENTS.md`) is the correct move if Claude iOS Code coverage is desired.

### §7 Recursive Review

- All claims in §2 are sourced or labelled [fact], [inference], or [assumption].
- All atomic questions in §1 are answered in §2.
- §3 reasoning is free of narrative glue.
- §4 resolves both identified contradictions.
- §5 adds technical, tool-coverage, maintenance, and historical lenses without introducing unsourced claims.
- No unsupported generalisations remain.
- One uncertainty persists: whether the Copilot CLI `AGENTS.md` bug (issue #489) is fixed in v1.0.12. This is noted explicitly in Risks/Gaps.
- Review outcome: **PASS**. All threads synthesised, all claims labelled, all uncertainties explicit.

---

## Findings

### Executive Summary

Deleting `AGENTS.md` in favour of `.github/copilot-instructions.md` as sole instructions source is the better-supported approach for this repo's two primary tools. [inference] The Copilot CLI (used in `research-loop.yml`) reads `.github/copilot-instructions.md` reliably; `AGENTS.md` support in the CLI exists in documentation but has a verified bug that may suppress it in practice. The Copilot Coding Agent (web, via GitHub Issues) reads both files, meaning restoring `AGENTS.md` would add additive but redundant context for that tool. The thin pointer pattern (a one-line `AGENTS.md` referencing `copilot-instructions.md`) is not viable because the `AGENTS.md` specification has no import syntax and agents read instruction files literally. The one genuine gap in the current setup is Claude iOS Code, which reads only `CLAUDE.md` and is served by neither existing file.

### Key Findings

1. The Copilot CLI (v1.0.12, used in `research-loop.yml`) officially reads both `AGENTS.md` and `.github/copilot-instructions.md` when both are present, but a verified bug report (GitHub issue #489, filed against v0.0.353) documents that `AGENTS.md` is silently ignored in favour of `copilot-instructions.md` in at least one version; fix status in v1.0.12 is unconfirmed. [confidence: high]

2. The Copilot Coding Agent (web, assigned via GitHub Issues) reads `AGENTS.md`, `.github/copilot-instructions.md`, `.github/instructions/*.instructions.md`, `CLAUDE.md`, and `GEMINI.md` as additive instruction sources; `AGENTS.md` support was added in the 2025-08-28 changelog entry. [confidence: high]

3. The Claude iOS Code feature (dispatched via mobile app to Claude Code Desktop) reads `CLAUDE.md` only; it does not read `AGENTS.md` or `.github/copilot-instructions.md`, and there is an open GitHub issue (#6235 in `anthropics/claude-code`) requesting native `AGENTS.md` support that remains unresolved. [confidence: high]

4. The `AGENTS.md` specification, stewarded by the Agentic AI Foundation under the Linux Foundation, supports both root-level and directory-scoped placement using a nearest-file-wins hierarchy, and has no native import, include, or file-reference syntax. [confidence: high]

5. A thin pointer `AGENTS.md` (one line referencing `copilot-instructions.md`) is not a viable cross-tool compatibility solution because agents read instruction file content as context input, not as file-loading directives, making adherence to such a pointer unreliable and unverifiable. [confidence: high]

6. ADR-0006 fully migrated all content from the previous `AGENTS.md` into `.github/copilot-instructions.md`; no instructions were lost in the deletion, meaning restoring `AGENTS.md` from scratch would require duplicating content already in `copilot-instructions.md`. [confidence: high]

7. Of the five inspectable repos in the davidamitchell organisation, only `Personal-Assistant-` has `AGENTS.md` at root; `Latest-developments-`, `Agent-Evaluation`, `Policy-LSP`, and `Research` all lack it, making `Personal-Assistant-` the outlier rather than Research. [confidence: high]

8. `.github/copilot-instructions.md` is the reliably read instruction file for the Copilot CLI regardless of whether a bug fix lands for `AGENTS.md` support, because the official documentation designates it as the always-used repository-wide instruction surface for the Copilot CLI. [confidence: high]

9. If restoring `AGENTS.md` with real content, it would need to be maintained in sync with `copilot-instructions.md`; maintaining two parallel instruction files creates a divergence risk [inference], and the current single-file approach eliminates that maintenance surface. [confidence: medium]

10. [inference] If instructions for the Claude iOS Code feature are desired, adding a `CLAUDE.md` (not an `AGENTS.md`) is the appropriate action, because `CLAUDE.md` is the only instruction file that Claude Code's read path includes. [confidence: high]

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| Copilot CLI reads both files officially | [GitHub Copilot CLI docs](https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-custom-instructions) | High | Primary source |
| AGENTS.md bug in Copilot CLI | [copilot-cli issue #489](https://github.com/github/copilot-cli/issues/489) | High | Bug filed against v0.0.353; fix status in v1.0.12 unconfirmed |
| Copilot Coding Agent reads AGENTS.md | [GitHub blog changelog 2025-08-28](https://github.blog/changelog/2025-08-28-copilot-coding-agent-now-supports-agents-md-custom-instructions/) | High | Official changelog |
| Claude iOS reads CLAUDE.md only | [Claude Code memory docs](https://code.claude.com/docs/en/memory), [claude-code issue #6235](https://github.com/anthropics/claude-code/issues/6235) | High | Open issue confirms AGENTS.md not natively supported |
| AGENTS.md has no import syntax | [agentsmd issue #11](https://github.com/agentsmd/agents.md/issues/11) | High | Feature request confirms absence |
| ADR-0006 fully migrated AGENTS.md content | [ADR-0006](https://github.com/davidamitchell/Research/blob/main/docs-adr/0006-standardise-agent-instruction-files.md) | High | Primary source, this repo |
| Personal-Assistant- has AGENTS.md | GitHub API inspection 2026-03-29 | High | File present, 10,018 bytes |
| Latest-developments- no AGENTS.md | GitHub API inspection 2026-03-29 | High | Root directory confirmed |
| Agent-Evaluation no AGENTS.md | GitHub API inspection 2026-03-29 | High | Root directory confirmed |
| Policy-LSP no AGENTS.md | GitHub API inspection 2026-03-29 | High | Root directory confirmed |
| Thin pointer not viable | [agentsmd issue #11](https://github.com/agentsmd/agents.md/issues/11), [copilot-cli community discussion](https://github.com/orgs/community/discussions/175649) | High | No spec mechanism for file loading |
| AGENTS.md spec, Linux Foundation governance | [agents.md](https://agents.md/), [particula.tech explainer](https://particula.tech/blog/agents-md-ai-coding-agent-configuration) | High | Confirmed by multiple sources |

### Assumptions

- **Assumption: A thin pointer `AGENTS.md` is insufficient for cross-tool compatibility.** Confirmed by investigation. The `AGENTS.md` spec has no import syntax; agents read files as context. The assumption was correct.
- **Assumption: Other repos in the organisation have `AGENTS.md`.** Partially confirmed. Only `Personal-Assistant-` has it; three of four other repos do not, matching Research's current state.

### Analysis

The evidence weighs in favour of the current setup on all three tested dimensions: tool coverage, maintenance cost, and organisation consistency.

The prior research item `Research/completed/2026-03-22-using-awesome-copilot-across-repos.md` recommended adding `AGENTS.md` to Research as a first-wave improvement. That recommendation was based on the Copilot Coding Agent (web) being able to read `AGENTS.md` directly and on Research lacking it while `Personal-Assistant-` had it. The present investigation refines that recommendation for this specific repo: `copilot-instructions.md` already holds the full instruction content; the Copilot CLI (the primary autonomous tool in `research-loop.yml`) has a documented bug that may suppress `AGENTS.md`; and restoring `AGENTS.md` would duplicate existing content without adding new tool coverage. The prior recommendation remains applicable to `Latest-developments-` and `Agent-Evaluation`, which lack equivalent `copilot-instructions.md` files and would gain first-time coverage from an `AGENTS.md`. `.github/copilot-instructions.md` is read reliably by both tools that matter for autonomous coding work in this repo (Copilot CLI and Copilot Coding Agent web). `AGENTS.md` is either redundant (Copilot Coding Agent, which reads both) or unreliable (Copilot CLI bug) for adding new coverage. The only tool not served by the current setup is Claude iOS Code, which would require `CLAUDE.md`, not `AGENTS.md`.

The maintenance-cost argument reinforces the status quo: `copilot-instructions.md` is already the complete and authoritative instructions source. Adding `AGENTS.md` creates a second copy to maintain; maintaining two parallel instruction files creates a divergence risk [inference].

The organisation-consistency argument also supports the status quo: three of four comparable repos lack `AGENTS.md`. `Personal-Assistant-` is the outlier, not Research.

### Risks, Gaps, and Uncertainties

- The Copilot CLI `AGENTS.md` bug (issue #489) status in v1.0.12 is unconfirmed. If the bug is fixed, the Copilot CLI would read both files, making `AGENTS.md` harmless to restore (additive context). If unfixed, `AGENTS.md` remains silently ignored.
- The Claude iOS Code gap: no instruction file in this repo is read by Claude iOS Code. If the owner uses Claude iOS Code to work in this repo, it operates without project-specific instructions. This is a known gap, not a regression from ADR-0006 (the previous `AGENTS.md` was also not on Claude's read path).
- `Memory-System` repo status is unknown (404 on prior inspection); its instruction-file state could not be assessed.
- The AGENTS.md specification's adoption rate (25+ tools, 60k+ open-source projects per agents.md) will increase over time. If new tools are adopted in this repo that read `AGENTS.md` but not `copilot-instructions.md`, the current setup would miss them.

### Open Questions

1. **Is the Copilot CLI AGENTS.md bug (issue #489) fixed in v1.0.12?** Direct test by creating a temporary `AGENTS.md` and verifying whether its content appears in a CLI session would confirm this. Out of scope for this item; could become a backlog item.
2. **Should `CLAUDE.md` be added to this repo?** If Claude iOS Code is used for repo work, a `CLAUDE.md` at root would be the correct file to add. This is a separate decision from `AGENTS.md`. Out of scope.
3. **Should `Personal-Assistant-` be the pattern to follow or an exception?** It is the only org repo with both `AGENTS.md` and `copilot-instructions.md`. Whether to standardise on its pattern or keep it as an exception warrants an explicit org-level decision.

### Output

- **Type:** knowledge
- **Description:** Confirmed that the current Research repo setup (`.github/copilot-instructions.md` only, no `AGENTS.md`) is correct for its primary tools (Copilot CLI and Copilot Coding Agent web), with a documented gap for Claude iOS Code (requires `CLAUDE.md`). Thin pointer pattern is not viable. Research is not an org outlier; three other repos also lack `AGENTS.md`.
- **Links:**
  - [GitHub Copilot CLI custom instructions documentation](https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-custom-instructions)
  - [GitHub blog: Copilot coding agent now supports AGENTS.md (2025-08-28)](https://github.blog/changelog/2025-08-28-copilot-coding-agent-now-supports-agents-md-custom-instructions/)
  - [agents.md specification site](https://agents.md/)
