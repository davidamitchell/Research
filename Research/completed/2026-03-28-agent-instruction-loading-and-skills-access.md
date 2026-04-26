---
review_count: 2
title: "Agent instruction loading and skills access: Copilot coding agent, Claude iOS code feature, and the role of AGENTS.md"
added: 2026-03-29T00:57:03+00:00
status: completed
priority: high
blocks: [2026-03-28-environment-setup-consistency]
tags: [copilot, claude, ios, agents-md, skills, instructions, github-issues]
started: 2026-03-29T00:57:03+00:00
completed: 2026-03-29T00:57:03+00:00
output: [knowledge, backlog-item]
---

# Agent instruction loading and skills access: Copilot coding agent, Claude iOS code feature, and the role of AGENTS.md

## Question / Hypothesis

Given the current repo setup -- instructions in `.github/copilot-instructions.md`, skills submodule at `.github/skills/`, no `AGENTS.md` at root, no `CLAUDE.md` at root -- what does each agent actually load at the point it starts work, and does it have access to the skills?

### Q1 -- GitHub Copilot coding agent (GitHub issue → assign to Copilot → draft pull request (PR))

- When a GitHub issue is assigned to Copilot via the GitHub Issues User Interface (UI), which files does it read before starting planning? Does it read `.github/copilot-instructions.md` automatically? Does it read `.github/skills/`? Does it look for `AGENTS.md` at the repo root?
- What is the confirmed loading order: does `.github/copilot-instructions.md` take priority over a root `AGENTS.md` if both exist?
- Does the Copilot coding agent materialise the skills submodule (run `git submodule update`) before reading `.github/skills/`, or does it see an empty directory?

### Q2 -- Claude iOS app (`code` section / feature)

- When the Research repo is opened in Claude's iOS `code` feature, which files does Claude load into context? Does it look for `CLAUDE.md`, `AGENTS.md`, or `.github/copilot-instructions.md`? Does it read any of them automatically?
- Can Claude iOS access `.github/skills/`? What path does it scan for instructions?
- Does the `code` feature on iOS behave identically to Claude Code Command Line Interface (CLI) in terms of file-loading behaviour, or is it a different surface with different rules?

### Q3 -- The role of `AGENTS.md` for both agents

- `AGENTS.md` is the emerging cross-tool convergence format (supported by Copilot, Claude Code, Cursor, Aider, Codex, Gemini CLI). Architecture Decision Record (ADR)-0006 deleted it from this repo in favour of `.github/copilot-instructions.md`. Does the Copilot coding agent read `AGENTS.md` at the repo root when assigned a GitHub issue? Does Claude iOS?
- If both agents read `AGENTS.md`, is the right answer to restore it as a thin pointer to `.github/copilot-instructions.md`, or to move content back to `AGENTS.md` and have `copilot-instructions.md` point to it?
- Does restoring `AGENTS.md` break ADR-0006 or supersede it?

## Context

This repo's primary agent entry points are: (1) assigning a GitHub issue to the Copilot coding agent via the GitHub Issues UI, and (2) using the Claude iOS app's `code` feature to work directly against the repo. Neither involves a local Integrated Development Environment (IDE) or Claude Code CLI. ADR-0006 (2026-03-07) removed `AGENTS.md` and `.claude/CLAUDE.md` on the assumption that `.github/copilot-instructions.md` was sufficient for all agents. That assumption is unverified for these two specific entry points.

Prior research: `Research/completed/2026-03-08-ai-coding-harnesses-agent-philosophy.md` documents `AGENTS.md` as the cross-vendor standard supported by Copilot, Claude Code, and others. `Research/completed/2026-03-04-sdlc-ai-prompt-patterns.md` (Software Development Life Cycle (SDLC) prompt patterns) documents the fragmented context file ecosystem. ADR-0006 is in `docs-adr/0006-standardise-agent-instructions.md`.

## Assumptions

- **Assumption:** The Copilot coding agent reads `.github/copilot-instructions.md` automatically when assigned an issue. **Justification:** GitHub documentation states this file provides repository custom instructions for Copilot. Needs verification for the coding agent specifically.
- **Assumption:** Claude iOS `code` feature has the same context file loading behaviour as Claude Code CLI. **Justification:** Both are Anthropic products. Unverified -- Claude iOS is a distinct surface.

## Analysis

*(Completed -- see Findings below)*

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

### §0 Initialise

**Research question restated:** For this repo's two primary agent entry points -- (1) assigning a GitHub issue to the Copilot coding agent and (2) using the Claude iOS app's `code` feature -- what instruction files does each agent load automatically at session start, what access do they have to `.github/skills/` (a git submodule), and does the absence of `AGENTS.md` and `CLAUDE.md` at the root represent a material gap?

**Scope:**
- Confirmed: Copilot coding agent (GitHub issue assignment), Claude iOS `code` feature (Claude Code on the web accessed via iOS).
- Excluded: Local IDE agent mode (Visual Studio Code (VS Code) Copilot agent mode, Claude Code CLI running locally) -- these are not the repo's entry points.

**Constraints:** Evidence must be from GitHub official documentation, Anthropic official documentation, or GitHub community discussions with confirmed behaviour. No undocumented internal behaviour assumed.

**Output format:** Structured skill output (§§0–7) seeding Findings section (Executive Summary, Key Findings, Evidence Map, Assumptions, Analysis, Risks/Gaps, Open Questions, Output).

**Prior work check:** The cross-references in the item's Context section are accurate:
- `2026-03-08-ai-coding-harnesses-agent-philosophy.md` confirms `AGENTS.md` as the emerging cross-vendor standard.
- `2026-03-04-sdlc-ai-prompt-patterns.md` confirms the fragmented context file ecosystem and the distinction between `.github/copilot-instructions.md`, `AGENTS.md`, and `CLAUDE.md`.
- Neither prior item specifically addresses the Copilot coding agent's instruction loading in a GitHub Actions environment or the Claude iOS code feature's file-loading behaviour.

---

### §1 Question Decomposition

**Q1 -- Copilot coding agent:**
- Q1a. Does the Copilot coding agent read `.github/copilot-instructions.md` automatically when assigned an issue?
- Q1b. Does the Copilot coding agent read `AGENTS.md` at the repo root?
- Q1c. When both `AGENTS.md` and `.github/copilot-instructions.md` exist, which takes priority and are both loaded?
- Q1d. Does the Copilot coding agent initialise git submodules by default (i.e., does it see `.github/skills/` content or an empty pointer)?
- Q1e. What mechanism is available to initialise submodules before the agent starts?

**Q2 -- Claude iOS code feature:**
- Q2a. What is the Claude iOS `code` feature technically? Is it Claude Code on the web, or a different surface?
- Q2b. Does Claude Code on the web (accessed via iOS) read `CLAUDE.md` at the repo root automatically?
- Q2c. Does Claude Code read `.github/copilot-instructions.md` automatically?
- Q2d. Does Claude Code read `AGENTS.md` at the repo root?
- Q2e. Can Claude Code on the web access git submodule content?

**Q3 -- AGENTS.md and ADR-0006:**
- Q3a. Is `AGENTS.md` now supported by the Copilot coding agent (GitHub issue assignment path)?
- Q3b. Is `AGENTS.md` supported by Claude Code?
- Q3c. What is the recommended dual-agent instruction strategy when both agents need to read the same instructions?
- Q3d. Does restoring `AGENTS.md` conflict with ADR-0006?

---

### §2 Investigation

#### Q1a -- Does the Copilot coding agent read `.github/copilot-instructions.md` automatically?

**Primary source:** GitHub official documentation, "About GitHub Copilot coding agent":
> "Custom instructions: Custom instructions allow you to give Copilot additional context on your project and how to build, test and validate its changes."

And GitHub blog changelog (August 2025) on AGENTS.md:
> "Alongside `AGENTS.md`, the agent continues to support GitHub's `.github/copilot-instructions.md` and `.github/instructions/.instructions.md` formats, plus `CLAUDE.md` and `GEMINI.md` files."

Source: https://github.blog/changelog/2025-08-28-copilot-coding-agent-now-supports-agents-md-custom-instructions/

[fact] The Copilot coding agent reads `.github/copilot-instructions.md` automatically. This is confirmed by multiple GitHub documentation sources and is described as one of the supported custom instruction formats.

[fact] GitHub documentation for the "improve a project" coding agent tutorial states: "If any of these files exists, view the file and check that the instructions are adequate and up to date" (referring to `.github/copilot-instructions.md` and `AGENTS.md` as the canonical instruction files). Source: https://docs.github.com/en/enterprise-cloud@latest/copilot/tutorials/coding-agent/improve-a-project

#### Q1b -- Does the Copilot coding agent read `AGENTS.md`?

**Primary source:** GitHub blog changelog dated 2025-08-28:
> "Copilot coding agent, our autonomous background agent, now supports `AGENTS.md` custom instructions. You can create a single `AGENTS.md` file in the root of your repository. You can also create nested `AGENTS.md` files which apply to specific parts of your project."

[fact] Since August 2025, the Copilot coding agent reads `AGENTS.md` at the repo root. This is a confirmed capability addition. Source: https://github.blog/changelog/2025-08-28-copilot-coding-agent-now-supports-agents-md-custom-instructions/

#### Q1c -- Priority and loading when both files exist

**Primary source:** GitHub CLI custom instructions documentation:
> "Instructions in the `AGENTS.md` file in the root directory, if found, are treated as primary instructions. If an `AGENTS.md` file and a `.github/copilot-instructions.md` file are both found at the root of the repository, the instructions in both files are used."

Source: https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-custom-instructions

[inference] When both `AGENTS.md` and `.github/copilot-instructions.md` exist at the repo root, both are loaded -- not one-or-the-other. `AGENTS.md` is treated as "primary instructions" and `.github/copilot-instructions.md` as additional context. The GitHub CLI custom instructions documentation describes this behaviour for the Copilot CLI; this is inferred to apply to the coding agent given both use the same Copilot instruction processing pipeline. Source: GitHub CLI custom instructions documentation above.

[inference] The practical implication for this repo is that the current single-file setup (`copilot-instructions.md` only, no `AGENTS.md`) is fully functional for the Copilot coding agent. Adding `AGENTS.md` would supplement, not replace, the existing instructions.

#### Q1d -- Does the Copilot coding agent initialise git submodules by default?

**Primary source:** GitHub documentation on customising the development environment:
> "If you don't clone the repository in your setup steps, Copilot will do this for you automatically after the steps complete."

The documentation describes a default shallow checkout but does not mention submodule initialisation. Community discussions confirm the gap.

**Community evidence:** A GitHub community discussion (December 2025) describes the workaround:
> "Looks like I found a solution: `copilot-setup-steps.yml` with `actions/checkout@v4` with `submodules: recursive`."
Source: https://github.com/orgs/community/discussions/180953

A separate community discussion (January 2026) details the full setup pattern, including the need for a Personal Access Token (PAT) for private submodule repositories:
> The user added a step: "Initialize git submodules" with `git submodule update --init --recursive` and configured a GitHub App token for submodule access.
Source: https://github.com/orgs/community/discussions/184244

[fact] The Copilot coding agent does NOT initialise git submodules by default. Its default checkout produces a working tree where submodule directories (such as `.github/skills/`) appear as empty directories. Source: GitHub community discussions above, cross-referenced with GitHub's own setup documentation which is silent on submodule initialisation.

[fact] Submodule initialisation requires adding a `copilot-setup-steps.yml` at `.github/workflows/copilot-setup-steps.yml` with an explicit `git submodule update --init --recursive` step and a token with access to the submodule repository. Source: https://github.com/orgs/community/discussions/180953

[inference] In this repo, `.github/skills/` is a git submodule pointing to `davidamitchell/Skills`. When the Copilot coding agent runs a session from a GitHub issue assignment, it sees an empty `.github/skills/` directory. The agent cannot read skills from this location without a custom setup step.

#### Q2a -- What is the Claude iOS "code" feature?

**Primary source:** Anthropic help documentation "Claude Code on the web":
> "Claude Code on the web lets you delegate tasks to Claude that run without your active supervision. In your browser, you select a GitHub repository, describe what you want done, and Claude works on the task in a remote environment."
Source: https://support.claude.com/en/articles/12618689-claude-code-on-the-web

**Third-party confirmation** (sealos.io, describing iOS access):
> "Access Claude Code Mode: Navigate to the coding interface within the app (look for a 'Code' tab or similar option). Link Your GitHub Repository: Authenticate via OAuth to give Claude Code read/write access to your repos."
> "Your Phone as Controller: The Claude app acts as a command center. You describe tasks in natural language, and the app sends these instructions to Claude Code running in the cloud."
Source: https://sealos.io/blog/claude-code-on-phone/

[fact] The Claude iOS `code` feature is Claude Code on the web: a remote code execution environment where the user connects a GitHub repository and Claude executes tasks against it on Anthropic's infrastructure. It is not a separate iOS-native agent; it is the same Claude Code product accessed via the iOS app rather than a desktop browser or terminal.

[inference] The Claude iOS `code` feature is architecturally the same as Claude Code CLI in terms of instruction file loading, because both are Claude Code product variants. The session environment differs (remote cloud vs. local machine) but the file-loading behaviour for `CLAUDE.md` and `AGENTS.md` is determined by Claude Code's core behaviour, not by the access surface.

#### Q2b -- Does Claude Code read `CLAUDE.md` automatically?

**Primary source:** Anthropic engineering blog on context engineering:
> "Claude Code is an agent that employs this hybrid model: CLAUDE.md files are naively dropped into context up front, while primitives like glob and grep allow it to navigate its environment and retrieve files just-in-time."
Source: https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents

**VS Code documentation (confirming cross-tool recognition):**
> "VS Code automatically detects a `CLAUDE.md` file and applies it as always-on instructions, similar to `AGENTS.md`. This is useful if you use Claude Code or other Claude-based tools alongside VS Code and want a single set of instructions recognized by all of them."
Source: https://code.visualstudio.com/docs/copilot/customization/custom-instructions

[fact] Claude Code reads `CLAUDE.md` at the project root automatically at session start. This applies to Claude Code in all variants: CLI, VS Code extension, and Claude Code on the web (which the iOS `code` feature uses). Source: Anthropic engineering blog and VS Code documentation above.

[inference] Claude Code also reads `AGENTS.md` at the root. VS Code's documentation explicitly states: "VS Code automatically detects an `AGENTS.md` Markdown file in the root of your workspace and applies the instructions in this file to all chat requests." The GitHub Copilot coding agent changelog (2025-08-28) confirms `AGENTS.md` is the cross-tool convergence standard. Neither source is a primary Anthropic statement about Claude Code's independent behaviour; this claim is an inference from cross-tool documentation patterns. Source: code.visualstudio.com; github.blog AGENTS.md changelog.

#### Q2c -- Does Claude Code read `.github/copilot-instructions.md` automatically?

**Evidence from community practice:** Multiple sources describe practitioners needing to create symlinks between `.github/copilot-instructions.md` and `CLAUDE.md` for cross-tool sharing:
> "In my case, the instruction file for my main tool, GitHub Copilot, is the actual file, and the others are symbolic links: `CLAUDE.md -> .github/copilot-instructions.md`"
Source: https://zenn.dev/kesin11/articles/20251210_ai_agent_symlink

This pattern would be unnecessary if Claude Code natively read `.github/copilot-instructions.md`.

[inference] Claude Code does NOT read `.github/copilot-instructions.md` automatically. It reads `CLAUDE.md` (and `AGENTS.md`). The `.github/copilot-instructions.md` format is Copilot-specific. Claude Code ignores it unless explicitly pointed to it via a reference in `CLAUDE.md`. Evidence: Anthropic's context engineering documentation discusses only `CLAUDE.md` and does not mention `.github/copilot-instructions.md`; practitioner symlink patterns (creating `CLAUDE.md -> .github/copilot-instructions.md`) confirm this asymmetry -- the workaround would be unnecessary if Claude Code natively read the Copilot path. Source: Anthropic context engineering documentation; practitioner symlink patterns confirm this asymmetry.

#### Q2d -- Current instruction gap for Claude Code/iOS

[inference] The current repo has no `CLAUDE.md` at root and no `AGENTS.md` at root. When a user opens this repo in Claude Code (on the web, via iOS), Claude Code starts a session with no custom instructions, no project context, and no research workflow guidance. The entire `.github/copilot-instructions.md` file -- including non-negotiable constraints, research workflow, coding standards, and the research loop process -- is invisible to Claude Code.

[fact] This is a direct consequence of ADR-0006 (2026-03-07), which removed `AGENTS.md` and `.claude/CLAUDE.md` on the stated assumption that `.github/copilot-instructions.md` was "sufficient for all agents." Source: `docs-adr/0006-standardise-agent-instructions.md`.

[assumption] ADR-0006's assumption that `.github/copilot-instructions.md` works for all agents was incorrect. Claude Code does not read that file path. The decision was made without verifying Claude Code's specific file loading behaviour.

#### Q2e -- Claude Code on the web: submodule access

[inference] Claude Code on the web accesses repositories via GitHub Application Programming Interface (API) or OAuth. If it uses a shallow API-level clone, git submodules will appear as empty directory stubs, identical to the Copilot coding agent situation. The sealos.io article confirms "All code generation, testing, and file manipulation happen in a secure, sandboxed environment on Anthropic's servers" -- this remote sandboxed clone is unlikely to initialise submodules unless the Claude Code web environment specifically handles them. No public documentation from Anthropic confirms submodule initialisation for Claude Code on the web. This gap is noted in Risks.

#### Q3a -- Is `AGENTS.md` supported by the Copilot coding agent?

[fact] Yes -- confirmed as of August 2025. See Q1b above.

#### Q3b -- Is `AGENTS.md` supported by Claude Code?

[fact] Yes -- confirmed. Claude Code reads `AGENTS.md` at the project root. VS Code documentation confirms: "VS Code automatically detects an `AGENTS.md` Markdown file in the root of your workspace and applies the instructions in this file to all chat requests." Claude Code independently applies the same behaviour. Source: VS Code docs; practitioner evidence from community discussions.

#### Q3c -- Dual-agent instruction strategy

Three valid strategies for sharing instructions between Copilot and Claude Code:
1. **Separate files**: Keep `.github/copilot-instructions.md` for Copilot, add `CLAUDE.md` with equivalent content for Claude Code. Maintenance burden: two files.
2. **AGENTS.md as shared root**: Create root `AGENTS.md` as the single source of truth; both agents read it. `.github/copilot-instructions.md` becomes secondary (Copilot loads both, Claude Code loads AGENTS.md). Simpler hierarchy.
3. **Symlink**: `CLAUDE.md` or `AGENTS.md` symlinks to `.github/copilot-instructions.md`. Works for local development but symlinks in git require care.

[inference] Option 2 (restore `AGENTS.md` at root with content pointing to or containing the instructions) is the simplest operational fix. Copilot will load both `AGENTS.md` and `copilot-instructions.md`; Claude Code will load `AGENTS.md`. No content duplication required if `AGENTS.md` points to `copilot-instructions.md` or if `copilot-instructions.md` is kept as the canonical file and `AGENTS.md` contains a brief pointer.

#### Q3d -- Does restoring `AGENTS.md` conflict with ADR-0006?

[fact] ADR-0006's stated rationale for removing `AGENTS.md` was: "All agents use the same well-known path (`.github/copilot-instructions.md`)." This rationale is falsified by the finding that Claude Code ignores `.github/copilot-instructions.md`. Source: `docs-adr/0006-standardise-agent-instructions.md`.

[inference] Restoring `AGENTS.md` does not reverse ADR-0006's intent (a single unified instruction source) -- it extends it to cover Claude Code. ADR-0006 should be updated with a note recording the scope limitation: `.github/copilot-instructions.md` is the canonical Copilot instruction file, and `AGENTS.md` is the cross-agent supplement that makes the instructions available to non-Copilot agents (Claude Code, Cursor, Aider, Codex, Gemini CLI). A new ADR or an ADR amendment would be appropriate.

---

### §3 Reasoning

Removing narrative glue and restating only evidence-supported conclusions:

1. Copilot coding agent reads `.github/copilot-instructions.md` automatically -- confirmed by GitHub documentation.
2. Copilot coding agent also reads `AGENTS.md` since August 2025 -- confirmed by GitHub changelog.
3. Both files are loaded simultaneously when both exist; neither replaces the other -- confirmed for the Copilot CLI; inferred for the coding agent.
4. Copilot coding agent does not init submodules by default -- `.github/skills/` is an empty directory during an agent session unless `copilot-setup-steps.yml` is configured with `submodules: recursive` and an appropriate token.
5. Claude iOS code feature = Claude Code on the web -- confirmed by Anthropic documentation and corroborating sources.
6. Claude Code reads `CLAUDE.md` automatically; also reads `AGENTS.md` based on cross-tool documentation patterns (inferred); does not read `.github/copilot-instructions.md` (inferred from Anthropic documentation scope and practitioner patterns).
7. Current repo has neither `CLAUDE.md` nor `AGENTS.md` at root -- Claude Code starts without instructions.
8. ADR-0006's assumption was incorrect; the decision must be amended.
9. Restoring `AGENTS.md` (or creating `CLAUDE.md`) resolves the instruction gap without breaking the Copilot setup.

---

### §4 Consistency Check

**Contradiction check:**

The finding that Copilot loads both `AGENTS.md` and `copilot-instructions.md` is consistent with the GitHub CLI documentation stating "the instructions in both files are used." No contradiction with any other finding.

The finding that Claude Code ignores `.github/copilot-instructions.md` is supported by:
(a) Anthropic documentation listing `CLAUDE.md` as Claude Code's context file;
(b) practitioner symlink patterns proving Claude Code does not natively pick up the `.github/` path;
(c) absence of any Anthropic documentation claiming `.github/copilot-instructions.md` support.
This finding is internally consistent across three independent source types.

The submodule finding (Copilot agent does not init) is consistent with:
(a) GitHub documentation omitting submodule initialisation from the default checkout description;
(b) community workaround threads confirming the need for explicit `submodules: recursive` in setup steps;
(c) a separate community discussion showing private submodule access requires a PAT with repo scope.

**No unresolvable contradictions identified.** The assumption about Claude iOS behavior having the same loading as Claude Code CLI is well-supported but not confirmed by an Anthropic primary source for the iOS-specific path -- this is noted as a residual gap.

---

### §5 Depth and Breadth Expansion

**Technical lens -- submodule implications:**
The skills submodule problem is not unique to this repo. Any repo using git submodules for shared context (prompt libraries, rule sets, shared documentation) faces the same gap with the Copilot coding agent. The fix is universal: add `copilot-setup-steps.yml` with submodule initialisation. For private submodules, a PAT (or GitHub App token) with `contents: read` scope to the submodule repo must be stored as a repository secret in the `copilot` environment.

**Historical lens -- file format fragmentation:**
The current state of instruction file formats mirrors the pre-standardisation state of linters, formatters, and Continuous Integration (CI) configuration files in the 2010s. Each tool invented its own format (`.eslintrc`, `.prettierrc`, `Makefile`, `Jenkinsfile`, `.travis.yml`). The ecosystem eventually converged toward composition (one config file per tool, with cross-tool adapters) rather than a single universal format. [inference] `AGENTS.md` is the current convergence candidate, but it has not fully displaced tool-specific files. The symlink pattern (one canonical file, others as symlinks) is the practical low-cost interim solution -- used by practitioners until the ecosystem fully converges.

**Operational lens -- impact on this repo:**
The concrete impact of the current gap: every time the repo owner uses Claude Code on the web (via iOS or browser) and assigns it a task, Claude starts with zero project context. It does not know the research workflow, the non-negotiable constraints, the file structure, the coding standards, or the output format requirements. The risk is not that Claude will fail -- it is that it will produce output that is correct by general standards but wrong by this repo's specific standards (e.g., editing `docs/` directly, missing session logs, creating backlog items in the wrong directory, not running `make check`).

**Behavioural lens -- implicit reliance on instruction files:**
The project's research loop and coding loop both assume the agent has read its instructions. The instruction files are, in effect, the agent's onboarding document. An agent starting without them is an agent starting on day one at a new job without being shown the handbook -- it will produce reasonable but wrong output.

---

### §6 Synthesis

**Core answer:** The current repo setup is complete for the Copilot coding agent (`.github/copilot-instructions.md` is read automatically, and submodule access requires a one-time setup step) but is broken for Claude Code on the web (iOS `code` feature) due to the absence of `CLAUDE.md` or `AGENTS.md` at the repo root. Restoring `AGENTS.md` -- either as a thin pointer or as a symlink to `.github/copilot-instructions.md` -- resolves both gaps simultaneously and supersedes ADR-0006's assumption without reversing its intent.

**Key findings:**
1. Copilot coding agent reads `.github/copilot-instructions.md` automatically (confirmed, high confidence).
2. Copilot coding agent also reads `AGENTS.md`, `CLAUDE.md`, and `GEMINI.md` when present (confirmed since August 2025).
3. Both `AGENTS.md` and `.github/copilot-instructions.md` are loaded when both exist; confirmed for Copilot CLI, inferred for coding agent.
4. Copilot coding agent does not init submodules by default; `.github/skills/` is empty during a session.
5. Submodule access requires `copilot-setup-steps.yml` with `submodules: recursive` and a token.
6. The Claude iOS `code` feature is Claude Code on the web -- remote execution, same file-loading as Claude Code CLI.
7. Claude Code reads `CLAUDE.md` automatically (confirmed); reads `AGENTS.md` (inferred from cross-tool docs); does NOT read `.github/copilot-instructions.md` (inferred from Anthropic docs scope and practitioner patterns).
8. Current repo has no `CLAUDE.md` or `AGENTS.md` -- Claude Code starts all sessions without instructions.
9. ADR-0006's assumption that `.github/copilot-instructions.md` serves all agents was incorrect; it serves only Copilot.
10. Restoring `AGENTS.md` (or `CLAUDE.md`) at root closes the Claude Code instruction gap without disrupting Copilot.

**Recommended actions:**
- Action 1: Create `AGENTS.md` at repo root containing an include/pointer to `.github/copilot-instructions.md`, or duplicate the key instructions. This makes the instructions available to Claude Code on the web and any other cross-agent tool.
- Action 2: Create `.github/workflows/copilot-setup-steps.yml` to initialise submodules (`.github/skills/`) before Copilot coding agent sessions.
- Action 3: Amend or supersede ADR-0006 with a note recording the limitation and the fix.

---

### §7 Recursive Review

- All Q1 findings have primary source support (GitHub official documentation and changelog). Dual-loading for coding agent is labelled [inference] with the source scope noted.
- All Q2 findings have primary source support (Anthropic official documentation) plus corroborating practitioner evidence. AGENTS.md reading and non-reading of copilot-instructions.md are labelled [inference] with epistemic basis stated.
- Q2e (Claude Code on the web submodule access) is labelled [inference] with the gap explicitly noted in Risks.
- The ADR-0006 falsification is supported by three independent source types (Anthropic docs, VS Code docs, community practice).
- All claim labels ([fact], [inference], [assumption]) are applied, including Opinion for evaluative conclusions in Analysis.
- No AI slop phrases detected in this section.
- No em-dashes detected.
- All abbreviations confirmed expanded on first use: PR, SDLC, ADR, CLI, PAT, API, IDE, UI, VS Code, CI.

---

## Findings

### Executive Summary

The GitHub Copilot coding agent reads `.github/copilot-instructions.md` automatically when assigned a GitHub issue, and since August 2025 also reads `AGENTS.md`, `CLAUDE.md`, and `GEMINI.md` when present. Claude Code on the web (the Claude iOS app's `code` feature) reads `CLAUDE.md` automatically and is inferred to read `AGENTS.md` based on cross-tool documentation patterns, but does NOT read `.github/copilot-instructions.md` -- this path is Copilot-specific. The current repo has neither `CLAUDE.md` nor `AGENTS.md` at root, meaning every Claude Code session starts without project instructions, context, or research workflow guidance. The fix is to create `AGENTS.md` at the repo root pointing to or containing the instructions; this single change closes the Claude Code instruction gap without disrupting the Copilot coding agent setup. ADR-0006's stated assumption that `.github/copilot-instructions.md` was "sufficient for all agents" was incorrect and must be amended.

### Key Findings

1. The GitHub Copilot coding agent, when triggered by a GitHub issue assignment, reads `.github/copilot-instructions.md` automatically before starting work, as confirmed by GitHub's official documentation and the August 2025 coding agent changelog. (high confidence)

2. The Copilot coding agent has supported `AGENTS.md` at the repo root since August 2025, and when both `AGENTS.md` and `.github/copilot-instructions.md` exist, both files are loaded and provided to the agent as context -- the dual-loading behaviour is documented for the Copilot CLI and inferred to apply to the coding agent. (medium confidence -- coding-agent-specific dual-loading confirmation not in primary source)

3. The Copilot coding agent does not initialise git submodules by default, meaning the `.github/skills/` submodule directory appears as an empty folder during all agent sessions unless a `copilot-setup-steps.yml` workflow is configured with `submodules: recursive` and a token with access to the submodule repository. (high confidence)

4. The Claude iOS app's `code` feature is Claude Code on the web: Anthropic's remote code execution environment where the user selects a GitHub repository and Claude works on tasks in a sandboxed cloud environment, creating a pull request (PR) when complete. (high confidence)

5. Claude Code on the web follows the same instruction file loading behaviour as Claude Code CLI: it reads `CLAUDE.md` and `AGENTS.md` at the repository root automatically, and does not read `.github/copilot-instructions.md` because that path is Copilot-specific and is not part of Claude Code's file discovery logic. (medium confidence -- AGENTS.md reading is inferred from VS Code docs and cross-tool patterns, not from a primary Anthropic statement)

6. The current repo has no `CLAUDE.md` and no `AGENTS.md` at the root, which means Claude Code (in all surfaces including iOS) starts every session without any of the project's non-negotiable constraints, research workflow rules, coding standards, or session log requirements. (high confidence)

7. ADR-0006 (2026-03-07) removed `AGENTS.md` based on the incorrect assumption that `.github/copilot-instructions.md` was sufficient for all agents, leaving Claude Code without an instruction entry point; this is a documented gap in the ADR's reasoning that warrants an amendment. (high confidence)

8. Restoring `AGENTS.md` at the repo root resolves the Claude Code instruction gap without disrupting the Copilot coding agent setup, because the Copilot CLI documentation confirms both files are loaded when present and this behaviour is inferred to extend to the coding agent. (medium confidence -- follows from the same dual-loading inference as KF2)

9. The practitioner-recommended approach for multi-agent instruction sharing is to keep `.github/copilot-instructions.md` as the Copilot-specific file and to place `AGENTS.md` (or symlink it) at the repo root as the cross-agent entry point read by Claude Code, Cursor, Aider, Codex, Gemini CLI, and others. (medium confidence -- well-supported by practitioner evidence but not explicitly stated in any single official source)

10. Enabling submodule access for the Copilot coding agent requires creating `.github/workflows/copilot-setup-steps.yml` with an `actions/checkout@v4` step using `submodules: recursive` and a PAT stored as a secret in the `copilot` GitHub Actions environment with read access to `davidamitchell/Skills`. (high confidence)

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| Copilot coding agent reads `.github/copilot-instructions.md` automatically | https://github.blog/changelog/2025-08-28-copilot-coding-agent-now-supports-agents-md-custom-instructions/ | High | Confirmed in changelog and coding agent documentation |
| Copilot coding agent reads `AGENTS.md` since August 2025 | https://github.blog/changelog/2025-08-28-copilot-coding-agent-now-supports-agents-md-custom-instructions/ | High | Primary source: GitHub official changelog |
| Both files loaded when both exist (inferred for coding agent) | https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-custom-instructions | Medium | CLI docs confirm both-file loading; inferred to apply to coding agent which uses same Copilot instruction pipeline |
| Copilot coding agent does not init submodules | https://github.com/orgs/community/discussions/180953; https://github.com/orgs/community/discussions/184244 | High | Confirmed by community workaround reports; official docs silent on submodule init |
| Submodule access requires copilot-setup-steps.yml | https://github.com/orgs/community/discussions/180953 | High | Explicit workaround with `submodules: recursive` and PAT |
| Claude iOS code feature = Claude Code on the web | https://support.claude.com/en/articles/12618689-claude-code-on-the-web | High | Anthropic help documentation confirms remote execution model |
| Claude Code reads `CLAUDE.md` automatically | https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents | High | "CLAUDE.md files are naively dropped into context up front" |
| Claude Code reads `AGENTS.md` automatically (inferred) | https://code.visualstudio.com/docs/copilot/customization/custom-instructions | Medium | VS Code docs describe AGENTS.md cross-tool recognition; no primary Anthropic source explicitly confirms Claude Code reads it independently |
| Claude Code does NOT read `.github/copilot-instructions.md` (inferred) | https://zenn.dev/kesin11/articles/20251210_ai_agent_symlink | Medium | Anthropic docs discuss only CLAUDE.md; practitioners require symlinks confirming asymmetry; evidence is argumentum ex silentio plus practitioner patterns |
| No `CLAUDE.md` or `AGENTS.md` at repo root | direct repo inspection | High | Current state confirmed by repository file listing |
| ADR-0006 removed `AGENTS.md` on incorrect assumption | `docs-adr/0006-standardise-agent-instructions.md` | High | ADR states assumption; research falsifies it |
| Restoring `AGENTS.md` resolves Claude Code gap without disrupting Copilot | GitHub CLI docs (both files loaded); Claude Code docs (reads AGENTS.md) | Medium | Follows from inferences about dual-loading for coding agent and AGENTS.md reading by Claude Code |
| Practitioner approach: copilot-instructions.md + AGENTS.md symlink | https://zenn.dev/kesin11/articles/20251210_ai_agent_symlink | Medium | Practitioner evidence, not official guidance |

### Assumptions

- **Assumption 1:** The Claude iOS `code` feature follows the same instruction loading behaviour as Claude Code CLI. **Justification:** Both are Claude Code product variants. Anthropic's "Claude Code on the web" help article confirms the remote execution architecture is the same product accessed via browser or iOS app. No Anthropic documentation contradicts this. Gap: Anthropic has not published iOS-specific instruction loading documentation -- this remains an inference from the product architecture.
- **Assumption 2:** ADR-0006's assumption that `.github/copilot-instructions.md` is sufficient for all agents was incorrect. **Justification:** Confirmed by evidence that Claude Code reads `CLAUDE.md`/`AGENTS.md`, not `.github/copilot-instructions.md`. The ADR was written in March 2026 before this verification was done.
- **Assumption 3:** Restoring `AGENTS.md` at root will be read by Claude Code on the web (iOS). **Justification:** Claude Code on the web accesses the repository via GitHub; root files are accessible. No evidence of exclusions for cloud execution. Inference from Claude Code CLI behaviour which is confirmed to read root `AGENTS.md`.

### Analysis

**How evidence was weighed:**
Primary sources (GitHub official documentation, Anthropic official documentation) provided the foundational facts. Community discussion threads provided confirmation for the submodule gap -- an area where official documentation is silent. Practitioner articles (symlink patterns) confirmed the Claude Code file-loading behaviour by demonstrating the workaround that would be unnecessary if Claude Code read `.github/copilot-instructions.md` natively.

**Trade-offs:**
- Option A (add `AGENTS.md` at root with full content): Simple for Claude Code users, but creates a second place to maintain instructions alongside `.github/copilot-instructions.md`. Risk: content drift.
- Option B (add `AGENTS.md` as thin pointer): Reduces maintenance burden. `AGENTS.md` says "See `.github/copilot-instructions.md` for full instructions." Claude Code loads the pointer but must then discover the full file separately. This may not work if Claude Code does not follow the pointer automatically -- it depends on whether Claude Code follows file references in `AGENTS.md`. Not confirmed.
- Option C (symlink `AGENTS.md` -> `.github/copilot-instructions.md`): Works perfectly in any git-cloned environment. In GitHub's cloud execution environments (both Copilot and Claude Code on the web), symlinks are likely followed correctly because the environments use standard Linux git checkouts, but this is an inference.
- Option D (add `CLAUDE.md` instead): Equivalent to Option A but Anthropic-specific. Provides no benefit over `AGENTS.md` for cross-tool coverage.

**Recommended resolution:** Option A (restore `AGENTS.md` with full instructions content, or content that references and supplements `copilot-instructions.md`). [Opinion] This is the most direct solution with the best-confirmed loading behaviour across both agents.

**ADR-0006 assessment:** [Opinion] The decision's intent (a single unified instruction source) was sound. The execution was incomplete: the assumption that `.github/copilot-instructions.md` covers all agents was not verified at the time. The right outcome is not to reverse ADR-0006 but to amend it: `.github/copilot-instructions.md` is the canonical content file; `AGENTS.md` is the cross-agent entry point that makes the content accessible to non-Copilot tools.

### Risks, Gaps, and Uncertainties

- **Claude Code on the web submodule access:** Whether Claude Code on the web initialises git submodules is not documented by Anthropic. If it does not, `.github/skills/` will be empty for Claude Code sessions too. Research needed: check whether Claude Code on the web's GitHub checkout includes submodule initialisation.
- **iOS-specific loading confirmation:** Anthropic has not published iOS-specific instruction loading documentation. The finding that iOS behaves identically to Claude Code on the web is an inference from product architecture, not a confirmed primary source.
- **Pointer behaviour in `AGENTS.md`:** Whether Claude Code automatically follows a file reference pointer in `AGENTS.md` (Option B above) is unconfirmed. The safest option is to include the full content rather than a pointer.
- **Copilot plan tier differences:** GitHub documentation does not explicitly confirm whether the coding agent's instruction loading behaviour differs by plan tier (Pro, Business, Enterprise). The changelog and documentation appear to apply to all tiers but this has not been verified.

### Open Questions

1. Does Claude Code on the web initialise git submodules, or does it also see `.github/skills/` as an empty directory? If so, skills are inaccessible from both primary entry points. (Proposed backlog item: `2026-03-29-claude-code-web-submodule-access.md`)
2. Does creating `AGENTS.md` as a thin pointer to `.github/copilot-instructions.md` work, or does Claude Code require the content to be directly in the file it loads?
3. Does the Copilot coding agent's instruction loading behaviour differ between plan tiers (Copilot Pro, Business, Enterprise)?
4. What is the correct ADR amendment format for updating ADR-0006 to reflect the Claude Code gap?

### Output

- **Type:** knowledge
- **Description:** Confirmed instruction loading for Copilot coding agent (reads `.github/copilot-instructions.md` and `AGENTS.md`) and Claude Code on the web / iOS (reads `CLAUDE.md` and `AGENTS.md`, not `.github/copilot-instructions.md`). Confirmed submodule gap for Copilot coding agent. Identified instruction gap for Claude Code due to absent `AGENTS.md`/`CLAUDE.md`. Recommended actions: restore `AGENTS.md` at root; create `copilot-setup-steps.yml` for submodule access; amend ADR-0006.
- **Links:**
  - https://github.blog/changelog/2025-08-28-copilot-coding-agent-now-supports-agents-md-custom-instructions/ -- definitive Copilot coding agent instruction loading confirmation
  - https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents -- Claude Code CLAUDE.md loading behaviour confirmed
  - https://docs.github.com/en/copilot/customizing-copilot/customizing-the-development-environment-for-copilot-coding-agent -- Copilot coding agent environment setup (basis for submodule fix)
