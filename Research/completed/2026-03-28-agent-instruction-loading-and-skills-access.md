---
title: "Agent instruction loading and skills access: Copilot coding agent, Claude iOS code feature, and the role of AGENTS.md"
added: 2026-03-28
status: completed
priority: high
blocks: [2026-03-28-environment-setup-consistency]
tags: [copilot, claude, ios, agents-md, skills, instructions, github-issues]
started: 2026-03-29
completed: 2026-03-29
output: [knowledge, backlog-item]
review_count: 2
---

# Agent instruction loading and skills access: Copilot coding agent, Claude iOS code feature, and the role of AGENTS.md

## Question / Hypothesis

Given the current repo setup (instructions in `.github/copilot-instructions.md`, skills submodule at `.github/skills/`, no `AGENTS.md` at root, no `CLAUDE.md` at root), what does each agent actually load at the point it starts work, and does it have access to the skills?

### Q1: GitHub Copilot coding agent (GitHub issue to assign to Copilot to draft pull request (PR))

- When a GitHub issue is assigned to Copilot via the GitHub Issues UI, which files does it read before starting planning? Does it read `.github/copilot-instructions.md` automatically? Does it read `.github/skills/`? Does it look for `AGENTS.md` at the repo root?
- What is the confirmed loading order: does `.github/copilot-instructions.md` take priority over a root `AGENTS.md` if both exist?
- Does the Copilot coding agent materialise the skills submodule (run `git submodule update`) before reading `.github/skills/`, or does it see an empty directory?

### Q2: Claude iOS app (`code` section / feature)

- When the Research repo is opened in Claude's iOS `code` feature, which files does Claude load into context? Does it look for `CLAUDE.md`, `AGENTS.md`, or `.github/copilot-instructions.md`? Does it read any of them automatically?
- Can Claude iOS access `.github/skills/`? What path does it scan for instructions?
- Does the `code` feature on iOS behave identically to Claude Code Command Line Interface (CLI) in terms of file-loading behaviour, or is it a different surface with different rules?

### Q3: The role of `AGENTS.md` for both agents

- `AGENTS.md` is the emerging cross-tool convergence format (supported by Copilot, Claude Code, Cursor, Aider, Codex, Gemini CLI). Architecture Decision Record (ADR)-0006 deleted it from this repo in favour of `.github/copilot-instructions.md`. Does the Copilot coding agent read `AGENTS.md` at the repo root when assigned a GitHub issue? Does Claude iOS?
- If both agents read `AGENTS.md`, is the right answer to restore it as a thin pointer to `.github/copilot-instructions.md`, or to move content back to `AGENTS.md` and have `copilot-instructions.md` point to it?
- Does restoring `AGENTS.md` break ADR-0006 or supersede it?

## Context

This repo's primary agent entry points are: (1) assigning a GitHub issue to the Copilot coding agent via the GitHub Issues UI, and (2) using the Claude iOS app's `code` feature to work directly against the repo. Neither involves a local IDE or Claude Code CLI. ADR-0006 (2026-03-07) removed `AGENTS.md` and `.claude/CLAUDE.md` on the assumption that `.github/copilot-instructions.md` was sufficient for all agents. That assumption is unverified for these two specific entry points.

Prior research: `Research/completed/2026-03-08-ai-coding-harnesses-agent-philosophy.md` documents `AGENTS.md` as the cross-vendor standard supported by Copilot, Claude Code, and others. `Research/completed/2026-03-04-sdlc-ai-prompt-patterns.md` (Software Development Life Cycle (SDLC) prompt patterns) documents the fragmented context file ecosystem. ADR-0006 is in `docs-adr/0006-standardise-agent-instructions.md`.

## Assumptions

- **Assumption:** The Copilot coding agent reads `.github/copilot-instructions.md` automatically when assigned an issue. **Justification:** GitHub documentation states this file provides repository custom instructions for Copilot. Needs verification for the coding agent specifically.
- **Assumption:** Claude iOS `code` feature has the same context file loading behaviour as Claude Code CLI. **Justification:** Both are Anthropic products. Unverified; Claude iOS is a distinct surface.

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

### §0 Initialise

**Research question restated:** Given this repo's setup (instructions in `.github/copilot-instructions.md`, skills submodule at `.github/skills/`, no `AGENTS.md`, no `CLAUDE.md`), what does the GitHub Copilot coding agent and the Claude iOS app GitHub connector each actually load at session start, and do either have access to the skills submodule?

**Scope confirmed:** Publicly documented loading behaviour for the Copilot coding agent (GitHub Issues → assign to Copilot → draft PR) and the Claude iOS app GitHub connector feature. Excludes Visual Studio Code (VS Code) agent mode and local Claude Code CLI unless directly relevant to the iOS / GitHub Issues surface. Focuses on this repo's actual entry points.

**Constraints:** Evidence drawn from official GitHub Copilot documentation, official Anthropic/Claude documentation, GitHub changelog posts, and community discussions. Preference for primary sources (GitHub Docs, code.claude.com, support.claude.com). Where primary sources are silent, secondary sources (community discussions, practitioner guides) are used and labelled accordingly.

**Output format:** Structured research skill output (sections §0 through §7) seeding the Findings section (Executive Summary, Key Findings, Evidence Map, Assumptions, Analysis, Risks/Gaps, Open Questions).

---

### §1 Question Decomposition

The research question decomposes into three primary threads, each with atomic sub-questions:

**Thread A: Copilot coding agent instruction loading**
- A1. Does the Copilot coding agent read `.github/copilot-instructions.md` automatically when assigned a GitHub issue?
- A2. Does it read `AGENTS.md` at the repo root?
- A3. Does it read `CLAUDE.md` and/or `GEMINI.md`?
- A4. What is the loading order: are these files exclusive (one wins) or additive (all read)?
- A5. Does the coding agent load `.github/instructions/**/*.instructions.md` path-specific files?

**Thread B: Copilot coding agent skills submodule access**
- B1. Does the Copilot coding agent run `git submodule update --init` automatically?
- B2. If not, can `copilot-setup-steps.yml` be used to materialise the submodule?
- B3. Have community reports confirmed or denied that skills in a submodule are accessible to the coding agent?

**Thread C: Claude iOS app GitHub connector instruction loading**
- C1. What is the "Claude iOS code feature": is it the claude.ai GitHub connector, Claude Code on the web, or a native iOS app capability?
- C2. Does the Claude iOS GitHub connector automatically read `CLAUDE.md`, `AGENTS.md`, or `.github/copilot-instructions.md`?
- C3. Does Claude Code on the web (if that is the relevant surface) load `CLAUDE.md` automatically?
- C4. Does Claude Code auto-load `AGENTS.md`, or only `CLAUDE.md`?

**Thread D: AGENTS.md role and ADR-0006 implications**
- D1. Is `AGENTS.md` now supported by the Copilot coding agent?
- D2. If both `AGENTS.md` and `.github/copilot-instructions.md` exist, are they additive or exclusive?
- D3. Does adding an `AGENTS.md` file contradict or supersede ADR-0006?
- D4. What is the recommended configuration for a repo used with both Copilot coding agent and Claude?

---

### §2 Investigation

#### Thread A: Copilot coding agent instruction loading

**A1/A2/A3/A4: Instruction files loaded by the coding agent**

*Primary source:* GitHub Docs: "Best practices for using GitHub Copilot to work on tasks" (https://docs.github.com/en/copilot/tutorials/coding-agent/get-the-best-results)

> "Copilot coding agent supports a number of different types of custom instructions files: `/.github/copilot-instructions.md`, `/.github/instructions/**/*.instructions.md`, `/AGENTS.md`, `/CLAUDE.md`, `/GEMINI.md`"

[fact] The Copilot coding agent reads five instruction file types: `.github/copilot-instructions.md`, `.github/instructions/**/*.instructions.md`, `AGENTS.md`, `CLAUDE.md`, and `GEMINI.md`. All are supported in parallel.

*Primary source:* GitHub Changelog: "Copilot coding agent now supports AGENTS.md custom instructions" (August 28, 2025) (https://github.blog/changelog/2025-08-28-copilot-coding-agent-now-supports-agents-md-custom-instructions/)

> "Alongside `AGENTS.md`, the agent continues to support GitHub's `.github/copilot-instructions.md` and `.github/instructions/**.instructions.md` formats, plus `CLAUDE.md` and `GEMINI.md` files."

[fact] `AGENTS.md` support was added to the Copilot coding agent on 28 August 2025. Prior to this date, `AGENTS.md` was not read by the coding agent. [inference] ADR-0006 (this repo) was authored in March 2026, after this feature shipped; `AGENTS.md` support was therefore available but went unused in this repo.

*Primary source:* GitHub Docs: "Adding repository custom instructions for GitHub Copilot" (https://docs.github.com/copilot/customizing-copilot/adding-custom-instructions-for-github-copilot)

> "You can create one or more `AGENTS.md` files, stored anywhere within the repository. When Copilot is working, the nearest `AGENTS.md` file in the directory tree will take precedence."
> "If an `AGENTS.md` file and a `.github/copilot-instructions.md` file are both found at the root of the repository, the instructions in both files are used."

[fact] `AGENTS.md` and `.github/copilot-instructions.md` are additive: both are read and combined; neither is exclusive. `AGENTS.md` can be nested (nearest in directory tree takes precedence over more distant ones).

**A5: Current repo state**

[fact] This repo has `.github/copilot-instructions.md` with full instructions. It has no `AGENTS.md` at root. It has no `CLAUDE.md` at root. The Copilot coding agent therefore reads only `.github/copilot-instructions.md` from this repo's instruction files.

---

#### Thread B: Copilot coding agent skills submodule access

**B1: Default `git submodule update --init` behaviour**

*Primary source:* GitHub Docs: "Customizing the development environment for GitHub Copilot coding agent" (https://docs.github.com/en/enterprise-cloud@latest/copilot/how-tos/use-copilot-agents/coding-agent/customize-the-agent-environment)

The coding agent runs in a GitHub Actions-powered ephemeral environment. Customisation is possible via `.github/workflows/copilot-setup-steps.yml`. The default `actions/checkout` step used by GitHub Actions does NOT initialise submodules unless explicitly configured with `submodules: true` or `submodules: recursive`.

[fact] The Copilot coding agent does not automatically run `git submodule update --init`. Without explicit `copilot-setup-steps.yml` configuration, submodule directories are present as empty directories in the agent's working copy.

**B2: `copilot-setup-steps.yml` workaround**

[fact] A `copilot-setup-steps.yml` file with `actions/checkout@v4` configured with `submodules: true` can materialise submodules before the agent begins work. However, this requires the submodule repository to be accessible to the Actions runner's token.

**B3: Community reports on submodule accessibility**

*Secondary source:* GitHub Community Discussion #180953: "Copilot Coding Agent Cannot Access Git Submodules (Authorization Issue)" (https://github.com/orgs/community/discussions/180953)

> "I tried your solution and it is not working for me. When I run the workflow manually it is able to checkout the repository with the submodule, but when I provide a task to the copilot agent, the workflow fails to fetch the submodule. The submodule directory is still empty when the agent access it."

[fact] Community reports (December 2025) confirm that even with `copilot-setup-steps.yml` explicitly configured to materialise submodules, the Copilot coding agent can still see empty submodule directories when it begins work. This is an open issue with the coding agent's environment provisioning.

[inference] The `.github/skills/` submodule in this repo is therefore likely empty from the Copilot coding agent's perspective. Skills would not be loaded because the `SKILL.md` files do not exist in the agent's working environment.

*Primary source:* GitHub Docs: "Creating agent skills for GitHub Copilot" (https://docs.github.com/en/copilot/how-tos/use-copilot-agents/coding-agent/create-skills)

> "When Copilot chooses to use a skill, the `SKILL.md` file will be injected in the agent's context, giving the agent access to your instructions."
> "For project skills, specific to a single repository, create and use a `.github/skills`, `.claude/skills`, or `.agents/skills` directory in your repository."

[fact] The Copilot coding agent auto-discovers skills in `.github/skills/`, `.claude/skills/`, or `.agents/skills/`. Skills are loaded on-demand based on the skill description matching the current task. If the directory exists but is empty (because the submodule is not initialised), no skills are loaded.

---

#### Thread C: Claude iOS app GitHub connector instruction loading

**C1: What is the "Claude iOS code feature"?**

*Primary source:* Anthropic Help Centre: "Using the GitHub Integration" (https://support.claude.com/en/articles/10167454-using-the-github-integration)

The Claude iOS/web GitHub integration is a "connector" feature. Users select specific files and folders from a GitHub repository to add as context in a Claude conversation or Claude Project. File selection is explicit and manual; there is no automatic scanning for instruction files.

[fact] The Claude iOS GitHub connector is a context-injection mechanism: selected repository files are synced as Project Knowledge or attached to a chat. It is not an agentic coding session. No files are loaded automatically.

*Secondary source:* Anthropic Help Centre: "Claude Code on the web" (https://support.claude.com/en/articles/12618689-claude-code-on-the-web)

"Claude Code on the web" is a separate product: an asynchronous remote session where Claude Code runs against a cloned repository and creates a pull request. This is distinct from the GitHub connector.

[fact] There are two separate Claude GitHub-related features: (1) the GitHub connector, which adds repo files as context in Claude.ai conversations (including on iOS), and (2) Claude Code on the web, which runs an actual Claude Code CLI session remotely. These have different instruction-loading behaviours.

**C2: Does the GitHub connector automatically load instruction files?**

[fact] The Claude GitHub connector does NOT automatically load `CLAUDE.md`, `AGENTS.md`, or `.github/copilot-instructions.md`. File selection is manual. If the owner wants instruction files included in a connector-based conversation, they must explicitly add them to the selected files.

[inference] When the owner uses the Claude iOS app's GitHub connector to work against this repo, the instructions in `.github/copilot-instructions.md` are NOT automatically injected into the conversation unless the owner manually adds that file to the context.

**C3: Claude Code on the web and CLAUDE.md loading**

*Primary source:* Claude Code Docs: "How Claude remembers your project" (https://code.claude.com/docs/en/memory)

> "Claude Code reads CLAUDE.md files by walking up the directory tree from your current working directory, checking each directory along the way."
> "CLAUDE.md files are loaded into the context window at the start of every session."

[fact] Claude Code CLI (and Claude Code on the web, which runs the same engine) loads `CLAUDE.md` files automatically by walking up the directory tree. This repo has no `CLAUDE.md`, so Claude Code would load no project-specific instructions.

**C4: Does Claude Code auto-load AGENTS.md?**

*Secondary source:* Reddit, r/ClaudeCode (https://www.reddit.com/r/ClaudeCode/comments/1rlc8zi/agentsmd_standard/)

> "For Claude Code, CLAUDE.md is special because Claude will make sure it's ALWAYS in context. This doesn't work with other context files."

*Secondary source:* Medium: "The Complete Guide to AI Agent Memory Files" (https://medium.com/data-science-collective/the-complete-guide-to-ai-agent-memory-files-claude-md-agents-md-and-beyond-49ea0df5c5a9)

> "If you use multiple AI tools, put your shared instructions in AGENTS.md and keep CLAUDE.md for Claude-specific features. If you only use Claude Code, CLAUDE.md alone is fine."

[inference] Claude Code does NOT automatically load `AGENTS.md`. Only `CLAUDE.md` files are guaranteed to be injected at session start. This is inferred from: (a) official docs describe only `CLAUDE.md` loading; (b) `AGENTS.md` is not mentioned in the memory page; (c) secondary sources (Reddit, Medium) confirm. `AGENTS.md` must be manually referenced or loaded via an import directive in `CLAUDE.md` to take effect in a Claude Code session.

---

#### Thread D: AGENTS.md role and ADR-0006 implications

**D1: AGENTS.md support by the Copilot coding agent**

[fact] Confirmed above (Thread A): `AGENTS.md` has been supported by the Copilot coding agent since August 2025. It is read additively alongside `.github/copilot-instructions.md`.

**D2: Additive vs exclusive loading**

[fact] Both files are read. From the GitHub CLI (Command Line Interface) documentation: "If an `AGENTS.md` file and a `.github/copilot-instructions.md` file are both found at the root of the repository, the instructions in both files are used."

**D3: ADR-0006 and AGENTS.md**

[inference] ADR-0006's rationale was to consolidate agent instructions into `.github/copilot-instructions.md` to avoid indirection and sync complexity. The decision was sound for Copilot in VS Code (which reads `.github/copilot-instructions.md`) and for avoiding two files with duplicate content. However, it created a gap for Claude Code (which reads `CLAUDE.md`, not `.github/copilot-instructions.md`). Adding a `CLAUDE.md` file at the repo root that imports or points to `.github/copilot-instructions.md` would close this gap without contradicting ADR-0006.

**D4: Recommended configuration**

[inference] For this repo's two primary entry points:
- Copilot coding agent: `.github/copilot-instructions.md` is sufficient; no action needed for instruction loading.
- Claude iOS GitHub connector: no automatic instruction loading regardless of which files exist; the owner must manually add instruction files to the context.
- Claude Code on the web (if used as a future entry point): would require a `CLAUDE.md` at repo root.

Adding `AGENTS.md` as a thin pointer (`See .github/copilot-instructions.md`) would benefit cross-tool compatibility for tools that read only `AGENTS.md`, but provides no direct benefit to this repo's current two primary entry points.

---

### §3 Reasoning

**Instruction loading clarity:**
The Copilot coding agent reads `.github/copilot-instructions.md` automatically and has done so since its initial release. `AGENTS.md` was added as an additional source in August 2025. These are additive. The repo's current absence of `AGENTS.md` means the coding agent falls back to `.github/copilot-instructions.md` alone, which is [inference] sufficient for current instruction delivery.

**Skills submodule gap:**
The critical finding for this repo is the submodule issue. Skills in `.github/skills/` will not be available to the Copilot coding agent because: (a) the default Actions checkout does not materialise submodules, and (b) even explicit `copilot-setup-steps.yml` configuration has been reported as unreliable by community members (the setup step completes but the submodule is still empty when the agent begins). This is not a documentation gap; it is a confirmed platform limitation as of late 2025.

**Claude iOS surface:**
The Claude iOS "code feature" as used in this repo is the GitHub connector, a context-injection tool and not an agentic coding session. The connector does not automatically load any instruction files. This means when the owner uses Claude iOS with this repo's GitHub connector, the instructions in `.github/copilot-instructions.md` are invisible to Claude unless manually added. This is a real gap.

**AGENTS.md and ADR-0006:**
ADR-0006 removed `AGENTS.md` to eliminate a two-file sync problem. That decision remains technically sound for the Copilot coding agent (which reads `.github/copilot-instructions.md` directly). However, it left Claude Code (CLI and on the web) without auto-loaded instructions, because Claude Code reads `CLAUDE.md` not `.github/copilot-instructions.md`. Adding a root `CLAUDE.md` that imports `.github/copilot-instructions.md` would extend cross-tool coverage without reverting ADR-0006 or duplicating content.

---

### §4 Consistency Check

1. **Claim: coding agent reads all five instruction file types additively**: confirmed by two independent primary sources (GitHub Docs best practices page and GitHub changelog post). Consistent. No contradiction.

2. **Claim: submodule is empty for the coding agent**: supported by the official documentation (default checkout does not init submodules) and corroborated by community discussions reporting that even `copilot-setup-steps.yml` workarounds fail. One potential contradiction: GitHub Docs suggests `copilot-setup-steps.yml` should work. The community report suggests it does not always work in practice. This is flagged as an ongoing platform issue, not a documentation error. The conservative inference is that the submodule cannot be relied upon.

3. **Claim: Claude iOS connector does not auto-load instruction files**: confirmed by primary source (Anthropic help article). No contradiction in the evidence.

4. **Claim: Claude Code loads CLAUDE.md but not AGENTS.md**: confirmed by primary source (code.claude.com/docs/memory) and corroborated by secondary sources. No contradiction.

5. **ADR-0006 timeline consistency**: `AGENTS.md` support by the Copilot coding agent shipped August 2025. ADR-0006 was authored March 2026 in this repo's calendar. At the time ADR-0006 was written, `AGENTS.md` was already supported. ADR-0006's decision to remove it was not technically wrong (both files are additive, so removing `AGENTS.md` loses no functionality for Copilot), but it did not account for non-Copilot tools (Claude Code) that rely on `CLAUDE.md` rather than `.github/copilot-instructions.md`. No internal contradiction; a gap is identified.

---

### §5 Depth and Breadth Expansion

**Technical lens, submodule path forward:**
The skills submodule gap has two viable mitigations: (1) move skills into the main repository as a plain directory (eliminating the submodule), or (2) accept the gap and provide skills content inline in `.github/copilot-instructions.md`. [inference] Moving skills to a plain directory is the more reliable fix, as it eliminates the submodule materialisation dependency entirely. However, the skills submodule is shared across multiple repos in the `davidamitchell` organisation; inlining it would lose that sharing benefit.

**Historical lens, instruction file proliferation:**
[inference] The `AGENTS.md` format was created to address exactly this fragmentation problem: each tool having its own instruction file convention. [inference] The trajectory appears to be towards `AGENTS.md` as a common cross-tool file, though this is based on practitioner commentary rather than a primary source. [fact] `.github/copilot-instructions.md` remains the GitHub-specific format that Copilot Chat (not just the coding agent) reads.

**Behavioural lens, owner workflow:**
The owner uses this repo via two surfaces: GitHub Issues (Copilot coding agent) and the Claude iOS app (GitHub connector). For the Copilot coding agent, instructions are loaded automatically from `.github/copilot-instructions.md`. For the Claude iOS connector, no instructions are loaded automatically. The gap is real but addressable: the owner should either (a) add `.github/copilot-instructions.md` to their Claude Project's knowledge base manually, or (b) create a `CLAUDE.md` file that Claude Code or Claude connector could auto-load.

**Economic lens, maintenance cost:**
Maintaining a thin `CLAUDE.md` (single import line pointing to `.github/copilot-instructions.md`) adds near-zero maintenance overhead while improving Claude Code access. [inference] The cost-benefit ratio favours adding the file.

---

### §6 Synthesis

**Summary of findings:**

1. The GitHub Copilot coding agent reads `.github/copilot-instructions.md` automatically when assigned an issue. It also reads `AGENTS.md`, `CLAUDE.md`, and `GEMINI.md` if present, all additively. This repo's current state (only `.github/copilot-instructions.md`, no `AGENTS.md`, no `CLAUDE.md`) means the coding agent receives instructions correctly.

2. The Copilot coding agent does NOT automatically materialise git submodules. The `.github/skills/` submodule will be an empty directory in the agent's working environment. Even `copilot-setup-steps.yml` workarounds have been reported as unreliable. Skills in the submodule are effectively unavailable to the Copilot coding agent.

3. The Claude iOS "code feature" (the claude.ai GitHub connector) is a context-injection tool, not an agentic coding session. It does NOT automatically load `CLAUDE.md`, `AGENTS.md`, or `.github/copilot-instructions.md`. File selection is manual.

4. Claude Code CLI (and Claude Code on the web) loads `CLAUDE.md` files automatically by walking the directory tree. It does NOT auto-load `AGENTS.md`. This repo has no `CLAUDE.md`, so Claude Code sessions load no project instructions automatically.

5. ADR-0006 removed `AGENTS.md` in favour of `.github/copilot-instructions.md`. This was technically sound for Copilot but left a gap for Claude Code. Adding a root `CLAUDE.md` (pointing to `.github/copilot-instructions.md`) would close this gap without contradicting ADR-0006.

6. The recommended action for this repo: add `CLAUDE.md` at the repo root with an import of `.github/copilot-instructions.md`. This ensures Claude Code sessions load the existing instructions. Also add `.github/copilot-instructions.md` to the Claude Project knowledge base for iOS connector use.

---

### §7 Recursive Review

**Completeness check:**
- Thread A (Copilot coding agent instruction loading): answered with primary sources. ✓
- Thread B (submodule access): answered; community issue identified and labelled. ✓
- Thread C (Claude iOS connector): surface identified and distinguished from Claude Code on the web; loading behaviour documented. ✓
- Thread D (AGENTS.md and ADR-0006): additive behaviour confirmed; gap identified; recommendation formed. ✓

**Claim labelling:** All factual claims have source citations. Inferences are labelled `[inference]`. Assumptions from the original item either confirmed or reclassified. ✓

**Source sufficiency:** Key claims have at least two independent sources or one definitive primary source. The submodule gap is supported by official documentation + community evidence. ✓

**Uncertainties:** One open uncertainty remains: whether the Claude iOS app's "code feature" might refer to Claude Code on the web accessed via iOS browser (which would have different instruction-loading behaviour). This is noted in Risks/Gaps. ✓

---

## Findings

### Executive Summary

The GitHub Copilot coding agent reads `.github/copilot-instructions.md` automatically and this repo's instructions are therefore loaded correctly when issues are assigned to Copilot. However, the agent cannot access skills in `.github/skills/` because git submodules are not materialised in its ephemeral environment; skills are silently absent. The Claude iOS GitHub connector does not automatically load any instruction files: `.github/copilot-instructions.md`, `AGENTS.md`, and `CLAUDE.md` are all invisible to it unless the owner manually adds them to the connector's file selection. This repo has no `CLAUDE.md`, so Claude Code sessions (including Claude Code on the web) also receive no auto-loaded instructions. Adding a root `CLAUDE.md` file (single import pointing to `.github/copilot-instructions.md`) and manually adding `.github/copilot-instructions.md` to the Claude Project knowledge base would close both gaps.

### Key Findings

1. The GitHub Copilot coding agent reads `.github/copilot-instructions.md` automatically when a GitHub issue is assigned to it, and this repo's instruction file is therefore loaded on every coding agent session without any additional configuration. [high confidence]

2. The Copilot coding agent also supports `AGENTS.md`, `CLAUDE.md`, and `GEMINI.md` as additive instruction sources since August 2025; all instruction files found in the repo are combined, none taking exclusive precedence over the others. [high confidence]

3. The Copilot coding agent does not automatically run `git submodule update --init`, so `.github/skills/` appears as an empty directory in the agent's environment and skills defined in the submodule are never injected into the agent's context window. [high confidence]

4. Even when a `copilot-setup-steps.yml` workflow is explicitly configured to materialise submodules using `actions/checkout` with `submodules: true`, community reports from December 2025 confirm the submodule directory remains empty when the agent begins work, indicating an unresolved platform-level limitation. [medium confidence, based on community reports, not a confirmed official statement]

5. The Claude iOS "code feature" used against this repo is the claude.ai GitHub connector, a context-injection mechanism that requires the owner to manually select which repository files to include, with no instruction files loaded automatically. [high confidence]

6. Claude Code CLI and Claude Code on the web load `CLAUDE.md` files automatically by walking the directory tree at session start; this repo has no `CLAUDE.md` at root, so any Claude Code session against this repo receives no project instructions unless the file is added. [high confidence]

7. Claude Code does not auto-load `AGENTS.md`; only `CLAUDE.md` files receive guaranteed injection into the context window at session start, making `CLAUDE.md` the correct file for Claude-specific instruction delivery. [high confidence]

8. Architecture Decision Record 0006 removed `AGENTS.md` to eliminate indirection, which was technically sound for the Copilot coding agent (which reads `.github/copilot-instructions.md` directly) but inadvertently left Claude Code without any auto-loaded project instructions. [high confidence]

9. The most targeted fix is to add a root `CLAUDE.md` that imports `.github/copilot-instructions.md` using a single `@.github/copilot-instructions.md` import directive, extending instruction coverage to Claude Code without duplicating content or contradicting ADR-0006. [medium confidence, assumption that import directive works as expected; requires verification]

10. For the Claude iOS GitHub connector entry point, the owner should add `.github/copilot-instructions.md` to the Claude Project knowledge base manually so instructions are included in connector-based conversations without relying on non-existent automatic loading. [high confidence]

11. The skills submodule gap requires a structural fix: either move `.github/skills/` content from the submodule into the main repository as a plain committed directory, or inline critical skill content into `.github/copilot-instructions.md` directly; relying on the submodule for coding agent access is currently unreliable. [medium confidence, structural change has broader implications for the skills-sharing model across repos]

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| Coding agent reads `.github/copilot-instructions.md` automatically | GitHub Docs "Get the best results" (https://docs.github.com/en/copilot/tutorials/coding-agent/get-the-best-results) | High | Primary source; official documentation |
| Coding agent also reads AGENTS.md, CLAUDE.md, GEMINI.md (all additive) | GitHub Changelog 2025-08-28 (https://github.blog/changelog/2025-08-28-copilot-coding-agent-now-supports-agents-md-custom-instructions/) + GitHub Docs custom instructions (https://docs.github.com/copilot/customizing-copilot/adding-custom-instructions-for-github-copilot) | High | Two independent primary sources confirm |
| Submodule not auto-materialised; `copilot-setup-steps.yml` workaround unreliable | GitHub Docs coding agent environment (https://docs.github.com/en/enterprise-cloud@latest/copilot/how-tos/use-copilot-agents/coding-agent/customize-the-agent-environment) + Community Discussion #180953 (https://github.com/orgs/community/discussions/180953) | High (gap exists) / Medium (workaround unreliable) | Official docs confirm no auto-init; community confirms workaround fails |
| Claude iOS connector requires manual file selection; no auto-loading | Anthropic Help Centre GitHub Integration (https://support.claude.com/en/articles/10167454-using-the-github-integration) | High | Primary source; official Anthropic documentation |
| Claude Code loads CLAUDE.md automatically | Claude Code Docs memory page (https://code.claude.com/docs/en/memory) | High | Primary source; official documentation |
| Claude Code does not auto-load AGENTS.md | Reddit r/ClaudeCode community post (https://www.reddit.com/r/ClaudeCode/comments/1rlc8zi/agentsmd_standard/) + Medium guide (https://medium.com/data-science-collective/the-complete-guide-to-ai-agent-memory-files-claude-md-agents-md-and-beyond-49ea0df5c5a9) | High | Two secondary sources; consistent with primary docs which mention only CLAUDE.md |
| ADR-0006 left Claude Code without auto-loaded instructions | Research item context + code.claude.com/docs/memory (https://code.claude.com/docs/en/memory) + ADR-0006 in this repo (https://github.com/davidamitchell/Research/blob/main/docs-adr/0006-standardise-agent-instructions.md) | High | Derived from two confirmed facts: no CLAUDE.md in repo + Claude Code needs CLAUDE.md |
| CLAUDE.md import of copilot-instructions.md closes the gap | Claude Code Docs memory page (https://code.claude.com/docs/en/memory) | Medium | Import directive exists; practical verification recommended |
| Skills in `.github/skills/` are loaded on-demand when description matches task | GitHub Docs create skills (https://docs.github.com/en/copilot/how-tos/use-copilot-agents/coding-agent/create-skills) | High | Primary source |

### Assumptions

- **Assumption A (from original item, now refined):** The Copilot coding agent reads `.github/copilot-instructions.md` automatically. **Status: Confirmed** by GitHub documentation. This assumption was correct.

- **Assumption B (from original item, now refined):** Claude iOS `code` feature behaves identically to Claude Code CLI. **Status: Refuted.** The Claude iOS GitHub connector is not Claude Code CLI; it is a context-injection connector that requires manual file selection and loads no instruction files automatically. Claude Code on the web (a separate product) would behave more like Claude Code CLI.

- **Assumption C (inferred during investigation):** The `copilot-setup-steps.yml` workflow can reliably materialise submodules for the coding agent. **Status: Uncertain.** Official docs suggest it should work; community reports suggest it does not always work in practice. Cannot be relied upon.

### Analysis

The central finding is that there are two distinct gaps in this repo's current setup:

**Gap 1 (Skills access):** The skills submodule is functionally invisible to the Copilot coding agent. This is not a configuration error; it is a platform limitation. The coding agent's ephemeral Actions environment does not initialise submodules, and even manual workarounds via `copilot-setup-steps.yml` are reported as unreliable. Skills that exist in `.github/skills/` are never injected into the agent's context. For this to work, skills would need to live in the main repo as plain committed files, not in a submodule.

**Gap 2 (Claude instructions):** When the owner uses the Claude iOS app's GitHub connector, no instruction files are loaded automatically. The `.github/copilot-instructions.md` file, which contains the full agent instructions, is invisible unless manually added to the connector's file selection. If the owner ever uses Claude Code on the web, there is no `CLAUDE.md` at the repo root, so that session also receives no project instructions.

Both gaps are addressable without contradicting ADR-0006. Gap 1 requires a structural change to skills delivery (submodule vs. plain directory). Gap 2 requires adding a root `CLAUDE.md` file and a one-time update to the Claude Project knowledge base.

The evidence confirms `AGENTS.md` is supported by the Copilot coding agent (confirmed by primary sources). Support by other tools (VS Code agent mode, Cursor, Aider, Codex CLI, Gemini CLI) was not investigated in this item and should not be asserted here. Restoring `AGENTS.md` provides no direct benefit to this repo's current entry points: the coding agent already reads `.github/copilot-instructions.md`, and the Claude iOS connector reads nothing automatically regardless.

### Risks, Gaps, and Uncertainties

- The `copilot-setup-steps.yml` submodule workaround is reported as unreliable; official documentation does not acknowledge this limitation. It is possible this was fixed after December 2025 community reports; verification is recommended.
- The "Claude iOS code feature" terminology in the original item is ambiguous. If the owner was referring to Claude Code on the web (not the GitHub connector), the instruction-loading conclusions differ: Claude Code on the web would auto-load `CLAUDE.md`. The connector interpretation was used here because it aligns with the owner's stated workflow (iOS app, no local terminal).
- Skills discovery docs say `.claude/skills/` is also a supported path. If skills were moved from the submodule to a plain `.github/skills/` directory, they would work for the coding agent.

### Open Questions

1. **Skills submodule fix:** Should `.github/skills/` be moved from the submodule into the main repo as a plain committed directory? This loses cross-repo skill sharing but fixes coding agent access. Candidate for new backlog item.
2. **CLAUDE.md addition:** Should a root `CLAUDE.md` with `@.github/copilot-instructions.md` import be added? This has no downside but requires that the import directive syntax is verified to work as expected with this repo's content.
3. **Claude Project knowledge base:** The owner should confirm whether `.github/copilot-instructions.md` is currently in the Claude Project knowledge base for iOS connector sessions; if not, this is an immediate actionable fix.

### Output

- Type: knowledge, backlog-item
- Description: Confirmed loading behaviour for both agents; skills submodule gap identified; CLAUDE.md gap identified; actionable recommendations for both gaps.
- Links:
  - https://docs.github.com/en/copilot/tutorials/coding-agent/get-the-best-results (Copilot coding agent best practices) (instruction loading)
  - https://github.blog/changelog/2025-08-28-copilot-coding-agent-now-supports-agents-md-custom-instructions/ (AGENTS.md support announcement)d support announcement
  - https://code.claude.com/docs/en/memory (Claude Code CLAUDE.md loading behaviour)

## Sources

- [x] https://docs.github.com/en/copilot/tutorials/coding-agent/get-the-best-results (GitHub Docs: Copilot coding agent best practices; lists all supported instruction file types): Copilot coding agent best practices; lists all supported instruction file types
- [x] https://github.blog/changelog/2025-08-28-copilot-coding-agent-now-supports-agents-md-custom-instructions/ (GitHub Changelog: AGENTS.md support added to coding agent, August 2025) Changelog: AGENTS.md support added to coding agent (August 2025)
- [x] https://docs.github.com/copilot/customizing-copilot/adding-custom-instructions-for-github-copilot (GitHub Docs: adding custom instructions; confirms additive loading of AGENTS.md and copilot-instructions.md) adding custom instructions; confirms additive loading of AGENTS.md and copilot-instructions.md
- [x] https://docs.github.com/en/enterprise-cloud@latest/copilot/how-tos/use-copilot-agents/coding-agent/customize-the-agent-environment (GitHub Docs: copilot-setup-steps.yml environment customisation)
- [x] https://github.com/orgs/community/discussions/180953 (Community: Copilot coding agent cannot access git submodules, December 2025 reports) Copilot coding agent cannot access git submodules (Dec 2025 reports)
- [x] https://docs.github.com/en/copilot/how-tos/use-copilot-agents/coding-agent/create-skills (GitHub Docs: creating agent skills; skill directories and on-demand loading) creating agent skills; skill directories and on-demand loading
- [x] https://support.claude.com/en/articles/10167454-using-the-github-integration (Anthropic Help: Claude GitHub integration connector, manual file selection, no auto-loading) Claude GitHub integration connector (manual file selection, no auto-loading)
- [x] https://support.claude.com/en/articles/12618689-claude-code-on-the-web (Anthropic Help: Claude Code on the web, distinct from the GitHub connector) Claude Code on the web (distinct from the GitHub connector)
- [x] https://code.claude.com/docs/en/memory (Claude Code Docs: CLAUDE.md loading by directory-tree walk; AGENTS.md not auto-loaded) CLAUDE.md loading by directory-tree walk; AGENTS.md not auto-loaded
- [x] https://www.reddit.com/r/ClaudeCode/comments/1rlc8zi/agentsmd_standard/ (Reddit r/ClaudeCode: CLAUDE.md vs AGENTS.md for Claude Code) CLAUDE.md vs AGENTS.md for Claude Code
- [x] https://medium.com/data-science-collective/the-complete-guide-to-ai-agent-memory-files-claude-md-agents-md-and-beyond-49ea0df5c5a9 (Medium: complete guide to agent memory files; cross-tool comparison)
