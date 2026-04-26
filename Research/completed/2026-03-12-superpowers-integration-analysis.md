---
title: "Superpowers as inspiration: what obra/superpowers can teach us about improving agent workflows across davidamitchell repos"
added: 2026-03-12T07:50:21+00:00
status: completed
priority: high
blocks: []
tags: [superpowers, skills, claude-code, github-copilot, agent-tooling, tdd, workflow, inspiration]
started: 2026-03-12T07:50:21+00:00
completed: 2026-03-12T07:50:21+00:00
output: [knowledge, backlog-item]
---

# Superpowers as inspiration: what obra/superpowers can teach us about improving agent workflows across davidamitchell repos

## Research Question

What ideas, patterns, and workflow practices from `davidamitchell/superpowers` (a fork of `obra/superpowers`) can be used as inspiration for improving agent tooling in `davidamitchell/Latest-developments-`, `davidamitchell/Agent-Evaluation`, `davidamitchell/Memory-System`, and `davidamitchell/Research`? Specifically: which superpowers concepts fill genuine gaps in the current `davidamitchell/Skills` library, and how could those ideas be adapted to the owner's actual workflow?

## Scope

**In scope:**
- What superpowers is and what workflow philosophy it embodies
- Current state of `.github/skills/` and agent tooling across each target repo
- Identifying ideas and patterns from superpowers that are absent from `davidamitchell/Skills`
- Per-repo assessment: which superpowers concepts would most improve agent quality in that repo
- Concrete recommended next steps (as backlog items for `davidamitchell/Skills`)

**Out of scope:**
- Direct installation of superpowers as a plugin (the owner's workflow is GitHub Copilot Agent, not Claude Code/Cursor)
- Evaluation of every superpowers skill in exhaustive detail
- Comparison with other plugin systems (Cursor plugins, etc.)

**Constraints:** Evidence based on current repo state as of 2026-03-12. `davidamitchell/Memory-System` does not exist (GitHub 404); cannot be assessed.

## Context

The owner forked `obra/superpowers` as a reference point. Superpowers embeds a mature, battle-tested set of software development workflow disciplines — TDD, systematic debugging, multi-agent coordination, structured planning — that have been refined in production Claude Code sessions. The question is not whether to install superpowers (it is incompatible with the owner's GitHub Copilot Agent workflow) but what ideas it contains that are worth borrowing. All repos the owner actively maintains (`Latest-developments-`, `Agent-Evaluation`, `Research`) use `davidamitchell/Skills` as a `.github/skills/` submodule. That library is strong on knowledge work and software engineering principles but does not prescribe a sequenced development workflow, TDD discipline, or debugging process. Superpowers can serve as an inspiration and reference for filling those gaps.

## Approach

1. Characterise superpowers: purpose, philosophy, and skill catalogue
2. Audit target repos: existing skills and their coverage
3. Compare superpowers philosophy against `davidamitchell/Skills` to identify the most valuable ideas to borrow
4. Per-repo assessment: which borrowed ideas would improve agent quality most
5. Produce recommendations as concrete backlog items for `davidamitchell/Skills`

## Sources

- [x] `davidamitchell/superpowers` — README, plugin.json, skill catalogue, commit history — https://github.com/davidamitchell/superpowers
- [x] `davidamitchell/Latest-developments-` — repo root, .github/ — https://github.com/davidamitchell/Latest-developments-
- [x] `davidamitchell/Agent-Evaluation` — repo root, .github/ — https://github.com/davidamitchell/Agent-Evaluation
- [x] `davidamitchell/Memory-System` — 404 Not Found — https://github.com/davidamitchell/Memory-System
- [x] `davidamitchell/Research` — local clone, .github/skills/, copilot-instructions.md — https://github.com/davidamitchell/Research
- [x] `davidamitchell/Skills` — local submodule (via Research repo clone) — https://github.com/davidamitchell/Skills

---

## Research Skill Output

### §0 Initialise

**Research question**: What ideas and patterns from `davidamitchell/superpowers` can inspire improvements to agent workflows and skills across the target repos?

**Scope**: Identify the most valuable superpowers concepts to borrow, assess their fit to each repo's context, and produce concrete recommendations for `davidamitchell/Skills`.

**Constraints**: `Memory-System` is non-existent. Direct plugin installation is not the goal — the aim is inspiration and adaptation. Skills must be adaptable to the `davidamitchell/Skills` submodule format (YAML frontmatter + structured Markdown).

### §1 Question Decomposition

1. What is the superpowers philosophy, and what software development disciplines does it embody?
2. What skills and workflow patterns does superpowers contain that are absent from `davidamitchell/Skills`?
3. Which of those missing patterns would most improve agent quality across the target repos?
4. How would the most valuable patterns be adapted from superpowers' format into `davidamitchell/Skills` format?
5. What is the specific recommendation per repo?

### §2 Investigation

**What superpowers is and the philosophy it embodies** [fact]:
`davidamitchell/superpowers` is a straight fork of `obra/superpowers` with zero owner customisations. All commits are authored by Jesse Vincent (`obra`). It is the upstream project as of v5.0.2 (2026-03-12). The fork exists as a reference and tracking point.

Superpowers is a skills library for **interactive coding session agents**: Claude Code (primary), Cursor, Codex, and OpenCode. Its core philosophy is that **software development disciplines should be mandatory, not optional**: TDD is an Iron Law, debugging follows a fixed 4-phase process, code review is a pre-review checklist, plans break work into tasks small enough for a junior engineer with no judgment. The library was built by observing what disciplines agents skip when left to their own devices, and encoding the correction as a non-negotiable skill that fires automatically.

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

**Skills format comparison** [fact]:
- `davidamitchell/Skills` skills use YAML frontmatter (`name`, `version`, `description`, `theoretical_foundations`) and structured Markdown bodies with "When Not to Use", "Interaction Protocol", "Inputs and Outputs" sections
- Superpowers skills use minimal YAML frontmatter (`name`, `description`) and highly prescriptive Markdown with visual flow diagrams, checklists, red-flag lists, and direct imperative language

**Concepts in superpowers with no equivalent in `davidamitchell/Skills`** [inference]:
- `test-driven-development` — `swe` touches TDD in passing but does not enforce it with an Iron Law or RED-GREEN-REFACTOR checklist. The superpowers TDD skill includes rationalisation-busting countermeasures, a red-flag list, and a verification checklist — all missing from `swe`.
- `systematic-debugging` — not covered anywhere in Skills. The 4-phase root-cause process (observe → hypothesise → test → fix) is a generalisable discipline any Python repo can benefit from.
- `subagent-driven-development` — not covered; describes how a coordinating agent dispatches isolated subagents per task, ensuring context isolation. Directly relevant to `Agent-Evaluation`, which builds multi-agent evaluation pipelines.
- `writing-plans` — not covered. Different from `strategy-author` (high-level strategy) — this is about decomposing agreed designs into atomic, independently verifiable engineering tasks.
- `brainstorming` — partially covered by `feedback` + `swe` but not as a dedicated pre-implementation exploration skill with Socratic design refinement.

Superpowers concepts with adequate coverage in `davidamitchell/Skills`:
- `requesting-code-review` / `receiving-code-review` → `code-review`
- `writing-skills` → no direct equivalent but low priority
- `using-git-worktrees` → infrastructure skill, not applicable to Copilot Agent workflow

### §3 Reasoning

**Claim 1**: The most valuable inspiration from superpowers is not the plugin delivery mechanism but the underlying philosophy: **encode missing disciplines as non-negotiable skills before agents skip them**. This is exactly the gap in `davidamitchell/Skills`. [inference]

**Claim 2**: The most valuable superpowers ideas to borrow are `test-driven-development`, `systematic-debugging`, and `subagent-driven-development` — these address concrete, recurring workflow gaps in Python development (Latest-developments-, Agent-Evaluation, Research/src/) and multi-agent coordination (Agent-Evaluation). [inference]

**Claim 3**: Adapting these ideas into the `davidamitchell/Skills` format (YAML frontmatter + structured Markdown) is feasible. The Skills format is expressive enough to capture prescriptive checklists, red-flag lists, and step-by-step protocols. The superpowers content is the reference; the adaptation is the work. [inference based on Skills format review]

**Claim 4**: `subagent-driven-development` is conceptually relevant even if Copilot Agent doesn't support explicit sub-agent dispatch today — it documents a coordination pattern the owner may want to apply manually or in future tooling. [assumption: sub-agent dispatch capability not confirmed]

**Claim 5**: The `davidamitchell/superpowers` fork serves as a **living reference**: keeping it in sync with upstream means the owner always has the latest version of superpowers' thinking available as a source of ideas. [inference]

### §4 Consistency Check

No internal contradictions identified. The fork-with-no-customisations finding is consistent with the repo being a reference and tracking point, not an integration attempt.

The reframe from "direct use" to "inspiration" is consistent with the evidence: the plugin delivery system is the wrong layer to engage with, but the workflow disciplines and skill content are genuinely valuable ideas worth borrowing.

### §5 Depth and Breadth Expansion

**Technical lens**: The superpowers TDD skill enforces an "Iron Law" — no production code without a failing test first. This is more prescriptive than the existing `swe` skill. The existing `Research/src/` codebase already has `pytest` and a test suite; a TDD skill adapted from superpowers would reinforce this practice rather than introduce it, and give the agent explicit countermeasures against common rationalisations for skipping tests.

**Process lens**: The superpowers workflow (brainstorm → plan → TDD implementation → subagent delegation → code review) is a complete SDLC loop. The `davidamitchell/Skills` catalogue addresses knowledge work and software engineering principles but does not prescribe a sequenced development workflow. Borrowing superpowers' SDLC sequencing as inspiration for improving `swe` or adding adjacent skills would fill this gap.

**Architectural lens**: The `subagent-driven-development` skill describes how to dispatch isolated subagents for individual tasks, preventing context pollution between tasks. Even if not directly executable by Copilot Agent today, this documents a coordination pattern that directly models how the owner already uses Copilot Agent (each PR = fresh agent session). Encoding it as a skill makes the pattern explicit and improvable.

**Risk lens**: Skills adapted from superpowers into `davidamitchell/Skills` will drift from the original over time. Keeping the `davidamitchell/superpowers` fork in sync with upstream (e.g. via a scheduled GitHub Action that pulls from `obra/superpowers`) ensures the reference stays current.

### §6 Synthesis

**Executive summary:**
`davidamitchell/superpowers` is a clean upstream fork of `obra/superpowers` — a plugin system for interactive IDE agents (Claude Code, Cursor, Codex). The right way to use it is not to install it directly (incompatible with the owner's GitHub Copilot Agent workflow) but as a **source of inspiration**: its skill content embeds battle-tested software development disciplines that are genuinely absent from `davidamitchell/Skills`. Adapting three superpowers skills — `test-driven-development`, `systematic-debugging`, and `subagent-driven-development` — into `davidamitchell/Skills` via PRs to that repo would immediately improve agent quality across all three active target repos with zero per-repo changes.

**Key findings:**
1. [fact] `davidamitchell/superpowers` is an uncustomised fork of `obra/superpowers` v5.0.2. It is a reference and tracking point.
2. [fact] Superpowers is a plugin for interactive CLI/IDE agents. Direct installation in a GitHub Copilot Agent workflow is not applicable.
3. [fact] All three active target repos already use `davidamitchell/Skills` as `.github/skills/` submodule. Memory-System does not exist.
4. [inference] Three superpowers concepts have no equivalent in `davidamitchell/Skills` and high applicability to Python development in the target repos: `test-driven-development`, `systematic-debugging`, `subagent-driven-development`.
5. [inference] Adapting these three concepts into `davidamitchell/Skills` format — opening PRs to that repo — is the highest-value path forward. It benefits all three repos without any per-repo configuration.
6. [inference] The superpowers philosophy (encode missing disciplines as non-negotiable skills) is itself valuable inspiration for how to approach gaps in `davidamitchell/Skills` more broadly.

**Evidence map:**

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| superpowers fork has zero customisations | commit log: all commits by obra/Jesse Vincent | high | |
| superpowers requires interactive CLI/IDE agent | README, plugin.json, .claude-plugin/ structure | high | |
| All target repos have Skills submodule | .github/ listings for all three repos | high | Memory-System is 404 |
| TDD/debugging not covered in davidamitchell/Skills | skills/ directory listing, swe SKILL.md review | high | swe touches TDD but is not prescriptive |
| Skills format is expressive enough to capture prescriptive checklists | swe SKILL.md, code-review SKILL.md | high | |

**Assumptions:**
- **Assumption:** Owner's primary agent is GitHub Copilot Agent, not Claude Code. **Justification:** copilot-instructions.md states "GitHub website or iOS GitHub app only; no local IDE."
- **Assumption:** GitHub Copilot Agent can invoke skills from `.github/skills/` for coding tasks. **Justification:** Agent-Evaluation and Latest-developments- both have the Skills submodule; this is the established pattern.
- **Assumption:** `davidamitchell/Memory-System` remains non-existent at time of action. **Justification:** GitHub returns 404 as of 2026-03-12.

**Risks, gaps, uncertainties:**
- Skills adapted from superpowers will drift from upstream unless the fork is kept current.
- Does GitHub Copilot Agent support explicit sub-agent dispatch? If not, `subagent-driven-development` is guidance rather than executable workflow — still useful, but the framing matters.
- The owner may have plans for Memory-System that are not yet on GitHub.

**Open questions:**
- Does GitHub Copilot Agent support explicit sub-agent dispatch? (relevant to how `subagent-driven-development` is framed in the adapted skill)
- Should the `davidamitchell/superpowers` fork be kept in sync with upstream via a scheduled action, to ensure the reference remains current?
- Are there further superpowers ideas worth borrowing beyond the three priority skills (`brainstorming`, `writing-plans`)?

### §7 Recursive Review

Every claim is grounded in direct inspection of the relevant repos. The key recommendation (adapt three superpowers concepts into `davidamitchell/Skills`) follows directly from the gap analysis. The reframe from "integrate directly" to "use as inspiration" is the correct framing: superpowers' value is in the quality of its thinking, not its delivery mechanism. Memory-System absence is documented. Open questions are explicitly flagged.

---

## Findings

### Executive Summary

`davidamitchell/superpowers` is a clean upstream fork of `obra/superpowers` — a plugin system for interactive IDE agents. The value is not in installing it (incompatible with the GitHub Copilot Agent workflow) but in using it as **inspiration**: superpowers embeds mature, battle-tested software development disciplines that are absent from `davidamitchell/Skills`. Three concepts deserve adaptation: `test-driven-development` (prescriptive TDD with Iron Law and rationalisation countermeasures), `systematic-debugging` (4-phase root-cause process), and `subagent-driven-development` (multi-agent coordination pattern). Adapting these into `davidamitchell/Skills` via PRs to that repo would immediately improve agent quality across all three active target repos. `Memory-System` does not exist on GitHub and cannot be assessed.

### Key Findings

1. Superpowers is a plugin for interactive session agents (Claude Code, Cursor, Codex). Using it as a plugin is not the right path — using its ideas as inspiration is.
2. All three active target repos (`Latest-developments-`, `Agent-Evaluation`, `Research`) already share the `davidamitchell/Skills` submodule at `.github/skills/`.
3. Three superpowers concepts fill genuine gaps in `davidamitchell/Skills` and are worth adapting: `test-driven-development` (prescriptive TDD enforcement with Iron Law), `systematic-debugging` (4-phase root-cause process), `subagent-driven-development` (multi-agent task coordination with context isolation).
4. Adapting these three concepts into `davidamitchell/Skills` format — opening PRs to that repo — is the recommended path. It requires zero per-repo changes to the target repos.
5. `Memory-System` does not exist (GitHub 404 as of 2026-03-12). Cannot be assessed.
6. The superpowers philosophy — **encode missing disciplines as non-negotiable skills** — is itself worth borrowing as a principle when identifying future gaps in `davidamitchell/Skills`.

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| superpowers is a CLI/IDE plugin — inspiration, not installation | README, .claude-plugin/plugin.json | high | |
| All target repos share Skills submodule | GitHub .github/ listings | high | Memory-System is 404 |
| TDD skill not in davidamitchell/Skills | Skills submodule directory listing | high | |
| Systematic debugging not in davidamitchell/Skills | Skills submodule directory listing | high | |
| subagent-driven-development not in davidamitchell/Skills | Skills submodule directory listing | high | |
| Skills format can represent prescriptive checklists | swe SKILL.md, code-review SKILL.md | high | |

### Assumptions

- **Assumption:** Owner's primary agent is GitHub Copilot Agent, not Claude Code. **Justification:** copilot-instructions.md states "GitHub website or iOS GitHub app only; no local IDE, no Codespaces."
- **Assumption:** Adapted skills in `davidamitchell/Skills` will be loadable by GitHub Copilot Agent for coding tasks. **Justification:** Skills submodule is already in place across all repos and used for coding-adjacent skills (`swe`, `code-review`).

### Analysis

Superpowers and `davidamitchell/Skills` serve different delivery models but are compatible at the **idea level**. Superpowers auto-triggers skills in interactive IDE sessions; Skills are named and invoked in GitHub Copilot Agent sessions. The workflow disciplines in superpowers — TDD enforcement, root-cause debugging, multi-agent coordination — translate naturally into the Skills format and will be just as valuable when invoked explicitly.

The three highest-priority adaptations are chosen on the basis of:
- **Coverage gap**: not currently in `davidamitchell/Skills`
- **Applicability**: all three target repos have Python code under test; multi-agent patterns are directly relevant to Agent-Evaluation
- **Quality of the source material**: superpowers TDD and debugging skills are comprehensive, include explicit anti-patterns and rationalisation-busting checklists, and have been refined in production sessions

The remaining superpowers skills (`brainstorming`, `writing-plans`, `executing-plans`, `using-git-worktrees`, `finishing-a-development-branch`) are lower priority: git-worktree commands don't apply to Copilot Agent; `writing-plans` and `brainstorming` are partially covered by `swe` and `strategy-author`; `executing-plans` is redundant given the agent autonomy model. They remain available in the fork as inspiration for future work.

### Risks, Gaps, and Uncertainties

- **Content drift**: Skills adapted from superpowers will diverge from upstream over time. Keeping `davidamitchell/superpowers` in sync with upstream `obra/superpowers` (e.g. via a scheduled GitHub Action) ensures the reference stays current for future inspiration.
- **Sub-agent capability**: If Copilot Agent gains explicit sub-agent dispatch, `subagent-driven-development` becomes more directly executable. The adapted skill should be written to be useful as guidance today and executable as a workflow tomorrow.
- **Memory-System**: If created in the future, the same path applies — add `davidamitchell/Skills` as a `.github/skills/` submodule, inheriting any adapted skills automatically.

### Open Questions

- Does GitHub Copilot Agent support explicit sub-agent dispatch? This affects how `subagent-driven-development` is framed in the adaptation.
- Should the superpowers fork be kept in sync with upstream via a scheduled workflow, or is periodic manual update sufficient?
- Of the secondary superpowers skills, is `brainstorming` worth adapting to complement `swe` and `strategy-author` for software design conversations?

---

## Output

- Type: knowledge, backlog-item
- Description: Use `davidamitchell/superpowers` as inspiration, not as a direct install. Adapt three skills into `davidamitchell/Skills` via PRs: `test-driven-development`, `systematic-debugging`, `subagent-driven-development`. Benefits all three active target repos via existing submodule with zero per-repo changes.
- Links:
  - https://github.com/davidamitchell/superpowers
  - https://github.com/obra/superpowers
  - https://github.com/davidamitchell/Skills
  - https://github.com/davidamitchell/Latest-developments-
  - https://github.com/davidamitchell/Agent-Evaluation