---
title: "Superpowers integration analysis: how and if obra/superpowers can be used across davidamitchell repos"
added: 2026-03-12
status: completed
priority: high
blocks: []
tags: [superpowers, skills, claude-code, github-copilot, agent-tooling, tdd, workflow, integration]
started: 2026-03-12
completed: 2026-03-12
output: [knowledge, backlog-item]
---

# Superpowers integration analysis: how and if obra/superpowers can be used across davidamitchell repos

## Research Question

Can `davidamitchell/superpowers` (a fork of `obra/superpowers`) be integrated into `davidamitchell/Latest-developments-`, `davidamitchell/Agent-Evaluation`, `davidamitchell/Memory-System`, and `davidamitchell/Research`? What integration path is available for each repo, and what is the net gain over the `davidamitchell/Skills` submodule already in place?

## Scope

**In scope:**
- What superpowers is and how it works
- Current state of `.github/skills/` and agent tooling across each target repo
- Compatibility with the owner's actual workflow (GitHub Copilot Agent, GitHub website / iOS app; not local IDE)
- Per-repo integration assessment: value add, integration path, effort
- Overlap analysis with `davidamitchell/Skills`
- Concrete recommended next steps

**Out of scope:**
- Implementation of any integration (this is a research item; recommendations go to backlog)
- Evaluation of every superpowers skill in detail
- Comparison with other plugin systems (Cursor plugins, etc.)

**Constraints:** Evidence based on current repo state as of 2026-03-12. `davidamitchell/Memory-System` does not exist (GitHub 404); cannot be assessed.

## Context

The owner forked `obra/superpowers` into `davidamitchell/superpowers` but has not yet integrated it into any repository. The question is whether and how to do so. All repos the owner actively maintains (`Latest-developments-`, `Agent-Evaluation`, `Research`) already use `davidamitchell/Skills` as a `.github/skills/` submodule, providing skills oriented toward research, knowledge work, and software engineering principles. Superpowers is a complementary skills system oriented toward **software development workflow enforcement** (TDD, debugging, planning, code review). Understanding whether to absorb superpowers content into `davidamitchell/Skills`, install it as a Claude Code plugin, or pursue another path is the core decision this research informs.

## Approach

1. Characterise superpowers: purpose, architecture, platform support, skill catalogue
2. Audit target repos: agent tooling stack, existing skills, platform compatibility
3. Compare superpowers skills against `davidamitchell/Skills` skills to identify gaps
4. Assess integration paths and their prerequisites
5. Produce per-repo recommendations

## Sources

- [x] `davidamitchell/superpowers` — README, plugin.json, skill catalogue, commit history
- [x] `davidamitchell/Latest-developments-` — repo root, .github/
- [x] `davidamitchell/Agent-Evaluation` — repo root, .github/
- [x] `davidamitchell/Memory-System` — 404 Not Found
- [x] `davidamitchell/Research` — local clone, .github/skills/, copilot-instructions.md
- [x] `davidamitchell/Skills` — local submodule (via Research repo clone)

---

## Research Skill Output

### §0 Initialise

**Research question**: Can `davidamitchell/superpowers` be integrated into the target repos, and should it be?

**Scope**: Assessment of fit and integration path for four repos. Recommendations as backlog items.

**Constraints**: `Memory-System` is non-existent. Owner's primary agent interface is GitHub Copilot Agent (not Claude Code). Skills must be compatible with the `davidamitchell/Skills` submodule pattern or the Claude Code plugin system.

### §1 Question Decomposition

1. What is superpowers and what does it provide that `davidamitchell/Skills` does not?
2. What is the current agent tooling state of each target repo?
3. Is superpowers compatible with the owner's GitHub Copilot Agent workflow?
4. What are the viable integration paths and their costs/benefits?
5. What is the specific recommendation for each repo?

### §2 Investigation

**What superpowers is** [fact]:
`davidamitchell/superpowers` is a straight fork of `obra/superpowers` with zero owner customisations. All commits are authored by Jesse Vincent (`obra`). It is the upstream project as of v5.0.2 (2026-03-12). The fork exists as a tracking point — the owner has not diverged from upstream.

Superpowers provides a skills library for **interactive coding session agents**: Claude Code (primary, with official plugin marketplace listing), Cursor, Codex, and OpenCode. It is installed as a per-agent plugin, not a per-repo configuration. Once installed, skills fire automatically when context is appropriate — they are mandatory workflows, not optional suggestions.

**Superpowers skill catalogue** [fact]:
- `brainstorming` — Socratic design refinement before writing code
- `writing-plans` — Break design into bite-sized, verifiable tasks
- `executing-plans` — Batch execution with human checkpoints
- `subagent-driven-development` — Delegate to fresh subagents per task with two-stage review
- `dispatching-parallel-agents` — Concurrent subagent workflows
- `test-driven-development` — Strict RED-GREEN-REFACTOR with "Iron Law": no production code without a failing test first
- `systematic-debugging` — 4-phase root cause process
- `verification-before-completion` — Verify the fix actually works
- `requesting-code-review` — Pre-review checklist
- `receiving-code-review` — Structured response to review feedback
- `using-git-worktrees` — Isolated workspace per branch
- `finishing-a-development-branch` — Merge/PR/keep/discard decision workflow
- `writing-skills` — Creating new skills
- `using-superpowers` — Introduction to the system

**Current `davidamitchell/Skills` catalogue** [fact]:
`backlog-manager`, `bbc-author`, `citation-discipline`, `code-review`, `feedback`, `plain-language`, `remove-ai-slop`, `research`, `research-question`, `research-reviewer`, `speculation-control`, `strategic-persuasion`, `strategy-author`, `swe`, `technical-writer`.

**Target repo agent tooling audit** [fact]:
All three active target repos share an identical `.github/skills/` entry pointing to `davidamitchell/Skills` (SHA `d0daf6b46cce45cd03000d1a91d1ccb1eb32c029`):
- `davidamitchell/Latest-developments-`: `.github/copilot-instructions.md`, `.github/mcp.json`, `.github/skills/` (davidamitchell/Skills submodule), `.github/workflows/`
- `davidamitchell/Agent-Evaluation`: `.github/copilot-instructions.md`, `.github/skills/` (davidamitchell/Skills submodule), `.github/workflows/`
- `davidamitchell/Research`: `.github/copilot-instructions.md`, `.github/mcp.json`, `.github/skills/` (davidamitchell/Skills submodule), `.github/workflows/`
- `davidamitchell/Memory-System`: **does not exist** — GitHub returns 404

**Platform compatibility** [fact]:
The owner's agent workflow is GitHub Copilot Agent, triggered via GitHub issues, PRs, and problem statements. The owner interacts exclusively via the GitHub website and iOS app. There is no local IDE, no Codespaces, and no terminal. Superpowers is designed for **interactive CLI/IDE sessions** (Claude Code, Cursor, Codex, OpenCode) where the agent runs locally against a checked-out repo. GitHub Copilot Agent in Spaces mode is not a Claude Code session. Therefore, the superpowers plugin system (`.claude-plugin/`, `.cursor-plugin/`, etc.) **cannot be directly installed or invoked in the owner's primary workflow**.

**Skills format comparison** [fact]:
- `davidamitchell/Skills` skills use YAML frontmatter (`name`, `version`, `description`, `theoretical_foundations`) and structured Markdown bodies with "When Not to Use", "Interaction Protocol", "Inputs and Outputs" sections
- Superpowers skills use minimal YAML frontmatter (`name`, `description`) and highly prescriptive Markdown with visual flow diagrams, checklists, red-flag lists, and direct imperative language

**Gap analysis between superpowers and davidamitchell/Skills** [inference]:
Superpowers has skills with no equivalent in `davidamitchell/Skills`:
- `test-driven-development` — `swe` touches TDD in passing but does not enforce it with an Iron Law or RED-GREEN-REFACTOR checklist
- `systematic-debugging` — not covered
- `verification-before-completion` — not covered
- `writing-plans` — not covered (different from `strategy-author` which is high-level strategy, not task granularity)
- `brainstorming` — partially covered by `feedback` + `swe` but not as a dedicated pre-code exploration skill
- `subagent-driven-development` — not covered; highly relevant to multi-agent architectures

Superpowers skills with equivalent coverage in `davidamitchell/Skills`:
- `requesting-code-review` / `receiving-code-review` → `code-review`
- `writing-skills` → no direct equivalent but low priority
- `using-git-worktrees` → infrastructure skill, not applicable to Copilot Agent workflow

### §3 Reasoning

**Claim 1**: Superpowers cannot be directly integrated into any target repo as a plugin, because the owner's agent is GitHub Copilot Agent, not Claude Code/Cursor/Codex. [fact-based]

**Claim 2**: The most viable integration path is to port selected superpowers skills into `davidamitchell/Skills` using that submodule's format, so they become available to GitHub Copilot Agent in all repos that include the submodule. [inference based on current architecture]

**Claim 3**: The skills that would deliver the most value are `test-driven-development` and `systematic-debugging` — they address concrete, recurring workflow gaps in Python development (Latest-developments-, Agent-Evaluation, Research/src/) that are not covered by existing skills. [inference]

**Claim 4**: `subagent-driven-development` is particularly relevant to `Agent-Evaluation`, which explicitly builds multi-agent evaluation pipelines, but requires GitHub Copilot Agent to have sub-agent invocation capability. Whether that is currently available in Copilot Agent is an open question. [assumption: sub-agent capability not confirmed]

**Claim 5**: The `davidamitchell/superpowers` fork as-is provides a useful **reference implementation** of software development workflow skills. The content is high-quality and battle-tested. Porting rather than writing from scratch is the efficient path. [inference]

**Claim 6**: If the owner ever uses Claude Code (even occasionally), installing superpowers via the official marketplace (`/plugin install superpowers@claude-plugins-official`) is a zero-configuration, immediate-value path that requires no per-repo changes. [fact]

### §4 Consistency Check

No internal contradictions identified. The fork-with-no-customisations finding is consistent with the repo being a clean upstream tracking point, not an attempt to integrate it anywhere yet.

One open question: does "how and if we could use this in the repos" include the interpretation that superpowers is used via the plugin marketplace in Claude Code sessions that the owner may run alongside GitHub Copilot Agent? This seems unlikely given the stated working environment (GitHub website only, no IDE), but is worth flagging.

### §5 Depth and Breadth Expansion

**Technical lens**: The superpowers TDD skill enforces an "Iron Law" — no production code without a failing test first. This is more prescriptive than the existing `swe` skill. The existing `Research/src/` codebase already has `pytest` and a test suite; adding a TDD skill would reinforce this practice rather than introduce it.

**Process lens**: The superpowers workflow (brainstorm → plan → TDD implementation → subagent delegation → code review) is a complete SDLC loop. The `davidamitchell/Skills` catalogue addresses knowledge work and software engineering principles but does not prescribe a sequenced development workflow. Superpowers fills this gap for software development tasks.

**Architectural lens**: The `subagent-driven-development` skill is architecturally significant: it describes how to dispatch isolated subagents for individual tasks, preventing context pollution between tasks. This maps directly to how GitHub Copilot Agent is currently used (each PR is a fresh agent session), and documents the coordination pattern explicitly.

**Risk lens**: Porting superpowers content into `davidamitchell/Skills` creates a maintenance burden: upstream skill updates must be manually tracked and merged. Using the superpowers fork as a submodule reference and periodically updating the fork from upstream would be one mitigation.

### §6 Synthesis

**Executive summary:**
`davidamitchell/superpowers` is a clean upstream fork of `obra/superpowers` with no owner customisations. It cannot be directly installed in the target repos because the owner's workflow is GitHub Copilot Agent (web/iOS), not Claude Code or Cursor. However, the superpowers skills library contains high-quality content — particularly `test-driven-development`, `systematic-debugging`, and `subagent-driven-development` — that addresses genuine gaps in `davidamitchell/Skills`. The recommended path is to port these three skills into `davidamitchell/Skills` (opening PRs to that repo), which would immediately benefit all three target repos via their existing submodule. If the owner ever uses Claude Code directly, installing superpowers via the official marketplace is a zero-config immediate win.

**Key findings:**
1. [fact] `davidamitchell/superpowers` is an uncustomised fork of `obra/superpowers` v5.0.2. No per-repo integration has been done.
2. [fact] Superpowers is a plugin for **interactive CLI/IDE agents** (Claude Code, Cursor, Codex, OpenCode). It cannot be installed in a GitHub Copilot Agent workflow.
3. [fact] All three active target repos already use `davidamitchell/Skills` as `.github/skills/` submodule. Memory-System does not exist.
4. [inference] Three superpowers skills have no equivalent in `davidamitchell/Skills` and high applicability to Python development in the target repos: `test-driven-development`, `systematic-debugging`, `subagent-driven-development`.
5. [inference] Porting these three skills to `davidamitchell/Skills` is the highest-value, lowest-friction integration path — it benefits all three repos without any per-repo configuration.
6. [fact] The official Claude Code marketplace install (`/plugin install superpowers@claude-plugins-official`) is a zero-config option if the owner uses Claude Code directly.

**Evidence map:**

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| superpowers fork has zero customisations | commit log: all commits by obra/Jesse Vincent | high | |
| superpowers requires interactive CLI/IDE agent | README, plugin.json, .claude-plugin/ structure | high | |
| All target repos have Skills submodule | .github/ listings for all three repos | high | Memory-System is 404 |
| TDD/debugging not covered in davidamitchell/Skills | skills/ directory listing, swe SKILL.md review | high | swe touches TDD but is not prescriptive |
| Porting to Skills is lowest-friction path | architecture analysis | medium | Assumes owner doesn't use Claude Code locally |

**Assumptions:**
- **Assumption:** Owner does not use Claude Code locally. **Justification:** copilot-instructions.md states "GitHub website or iOS GitHub app only; no local IDE."
- **Assumption:** GitHub Copilot Agent can invoke skills from `.github/skills/` for coding tasks (not just knowledge work). **Justification:** Agent-Evaluation and Latest-developments- both have the Skills submodule; this is the established pattern.
- **Assumption:** `davidamitchell/Memory-System` remains non-existent at time of action. **Justification:** GitHub returns 404 as of 2026-03-12.

**Risks, gaps, uncertainties:**
- Does GitHub Copilot Agent have sub-agent invocation? If not, `subagent-driven-development` is only useful as guidance, not executable workflow.
- Maintenance burden of ported skills drifting from upstream superpowers.
- The owner may have plans for Memory-System that are not yet on GitHub.

**Open questions:**
- Does GitHub Copilot Agent support explicit sub-agent dispatch? (relevant to `subagent-driven-development` utility)
- Should the `davidamitchell/superpowers` fork be kept in sync with upstream via a scheduled action, or archived as reference?
- Are there other superpowers skills worth porting (`brainstorming`, `writing-plans`) or is the three-skill portfolio sufficient?

### §7 Recursive Review

Every claim is grounded in direct inspection of the relevant repos. The key recommendation (port three skills to `davidamitchell/Skills`) follows directly from the gap analysis and is the only integration path compatible with the owner's stated working environment. Memory-System absence is documented. The "use Claude Code marketplace" option is surfaced as an alternative but not the primary recommendation. Open questions are explicitly flagged.

---

## Findings

### Executive Summary

`davidamitchell/superpowers` is an uncustomised fork of `obra/superpowers` — an agent skills plugin for Claude Code, Cursor, Codex, and OpenCode. It cannot be directly installed in the target repos because the owner's workflow is GitHub Copilot Agent via the web/iOS, not an interactive IDE. The highest-value integration path is to port three superpowers skills — `test-driven-development`, `systematic-debugging`, and `subagent-driven-development` — into `davidamitchell/Skills`, where they will be immediately available to all three active target repos via the existing submodule. `Memory-System` does not exist on GitHub and cannot be assessed.

### Key Findings

1. Superpowers is not installable in a GitHub Copilot Agent workflow — it requires an interactive session agent (Claude Code, Cursor, Codex, OpenCode). The owner's repos cannot use it as a plugin.
2. All three active target repos (`Latest-developments-`, `Agent-Evaluation`, `Research`) already share the `davidamitchell/Skills` submodule at `.github/skills/`.
3. Three superpowers skills fill genuine gaps in `davidamitchell/Skills`: `test-driven-development` (prescriptive TDD enforcement), `systematic-debugging` (4-phase root-cause process), `subagent-driven-development` (multi-agent coordination pattern).
4. Porting these three skills to `davidamitchell/Skills` — opening PRs to that repo — is the recommended integration path. It requires zero per-repo changes to the target repos.
5. `Memory-System` does not exist (GitHub 404 as of 2026-03-12). Cannot be assessed.
6. If the owner ever uses Claude Code directly, the zero-configuration option is `/plugin install superpowers@claude-plugins-official` — no per-repo setup required.

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| superpowers is a CLI/IDE plugin only | README, .claude-plugin/plugin.json | high | |
| All target repos share Skills submodule | GitHub .github/ listings | high | Memory-System is 404 |
| TDD skill not in davidamitchell/Skills | Skills submodule directory listing | high | |
| Systematic debugging not in davidamitchell/Skills | Skills submodule directory listing | high | |
| subagent-driven-development not in davidamitchell/Skills | Skills submodule directory listing | high | |
| Port to Skills is viable | established submodule pattern across repos | medium | |

### Assumptions

- **Assumption:** Owner does not use Claude Code locally. **Justification:** copilot-instructions.md states "GitHub website or iOS GitHub app only; no local IDE, no Codespaces."
- **Assumption:** Ported skills in `davidamitchell/Skills` will be loadable by GitHub Copilot Agent for coding tasks. **Justification:** Skills submodule is already in place across all repos and used for coding-adjacent skills (`swe`, `code-review`).

### Analysis

The superpowers plugin system and the `davidamitchell/Skills` submodule are compatible at the **content level** but incompatible at the **delivery level**. Superpowers delivers skills via IDE plugin auto-triggering; `davidamitchell/Skills` delivers skills via named invocation in GitHub Copilot Agent sessions. The content of the most valuable superpowers skills — TDD enforcement, debugging process, multi-agent coordination — can be adapted to the Skills format (YAML frontmatter + structured Markdown) and added to the `davidamitchell/Skills` repo.

The three highest-priority skills to port are selected on the basis of:
- **Coverage gap**: not currently in `davidamitchell/Skills`
- **Applicability**: all three target repos have Python code with tests; multi-agent patterns are directly relevant to Agent-Evaluation
- **Quality**: superpowers TDD and debugging skills are well-tested, comprehensive, and include explicit anti-patterns and rationalisation-busting checklists

The remaining superpowers skills (`brainstorming`, `writing-plans`, `executing-plans`, `using-git-worktrees`, `finishing-a-development-branch`) are lower priority because: (a) git-worktree commands do not apply to Copilot Agent sessions, (b) `writing-plans` and `brainstorming` are partially covered by `swe` and `strategy-author`, and (c) `executing-plans` is redundant given the agent autonomy model.

### Risks, Gaps, and Uncertainties

- **Maintenance drift**: Ported skills will diverge from upstream superpowers over time unless a sync process is established. Mitigation: keep `davidamitchell/superpowers` fork in sync with upstream via a scheduled GitHub Action, and reference the fork as the canonical source when re-porting.
- **Sub-agent capability**: `subagent-driven-development` is most valuable if GitHub Copilot Agent supports explicit sub-agent dispatch. If it does not, the skill still provides useful guidance but cannot be invoked as a workflow.
- **Memory-System**: If this repo is created in the future, the same integration path applies — add `davidamitchell/Skills` as a `.github/skills/` submodule.

### Open Questions

- Does GitHub Copilot Agent in Spaces mode support sub-agent dispatch? If yes, `subagent-driven-development` becomes a first-class skill.
- Should the superpowers fork be kept in sync with upstream via a scheduled workflow, or is it adequate to treat it as a point-in-time reference?
- Of the remaining superpowers skills, should `brainstorming` be adapted into Skills to complement `swe` and `strategy-author` for software design conversations?

---

## Output

- Type: knowledge, backlog-item
- Description: Superpowers cannot be directly installed in the target repos (wrong platform). Recommended action: port three skills (`test-driven-development`, `systematic-debugging`, `subagent-driven-development`) to `davidamitchell/Skills` via PRs to that repo. This benefits all three active target repos via their existing submodule with zero per-repo changes.
- Links:
  - https://github.com/davidamitchell/superpowers
  - https://github.com/obra/superpowers
  - https://github.com/davidamitchell/Skills
  - https://github.com/davidamitchell/Latest-developments-
  - https://github.com/davidamitchell/Agent-Evaluation
