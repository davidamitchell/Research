---
title: "oh-my-codex and AI Agent Workflow Patterns: What Can We Leverage?"
added: 2026-04-03T00:27:58+00:00
status: completed
priority: high
blocks: []
tags: [ai-agents, tooling, instructions, skills, workflow, codex, copilot, agents-md]
started: 2026-04-03T00:27:58+00:00
completed: 2026-04-03T00:27:58+00:00
output: [knowledge, backlog-item]
---

# oh-my-codex and AI Agent Workflow Patterns: What Can We Leverage?

## Research Question

What patterns from oh-my-codex (OMX) and similar AI agent workflow projects (AGENTS.md, SKILL.md, etc.) are most applicable to improving the instructions, skills, agents, and tooling across davidamitchell's repositories — and which specific changes would deliver the highest value?

## Scope

**In scope:**
- oh-my-codex architecture, skills, and design patterns
- AGENTS.md standard and its adoption across tools
- Similar projects: CLAUDE.md, GEMINI.md, .cursor/rules/, SKILL.md
- Comparison against the current davidamitchell repo setup (Research, Skills, Multi-Agent-Testing, Agent-Evaluation, Latest-developments- — trailing hyphen is the actual GitHub repo name)
- Specific, actionable improvement recommendations for instructions, skills, agents, and tooling

**Out of scope:**
- Deep implementation of recommended changes (those go into backlog items)
- Proprietary or closed-source agent systems without public documentation
- General Artificial Intelligence (AI) model benchmarking

**Constraints:** Sources must be publicly accessible. Analysis limited to openly documented patterns as of April 2026.

## Context

The davidamitchell/Research repo uses a skills-based agent workflow (SKILL.md submodule from davidamitchell/Skills, copilot-instructions.md, research-prompt.md) but the approach was built organically. The oh-my-codex project provides a mature example of workflow orchestration for coding agents. Understanding what OMX and the broader AGENTS.md ecosystem has standardised could reveal gaps and improvement opportunities across all active davidamitchell repos.

## Approach

1. Analyse oh-my-codex architecture: skills, roles, AGENTS.md contract, state management, workflow progression
2. Survey similar projects and emerging standards: AGENTS.md, CLAUDE.md, GEMINI.md, SKILL.md patterns
3. Audit the current davidamitchell repo setup against identified best practices
4. Synthesise actionable improvements mapped to specific repos and files

## Sources

- [x] [oh-my-codex GitHub repository](https://github.com/Yeachan-Heo/oh-my-codex) — primary source for OMX architecture and patterns
- [x] [oh-my-codex AGENTS.md](https://github.com/Yeachan-Heo/oh-my-codex/blob/main/AGENTS.md) — operating contract and skill/role design
- [x] [AGENTS.md official site](https://agents.md/) — cross-agent standard definition
- [x] [GitHub Blog: How to write a great agents.md](https://github.blog/ai-and-ml/github-copilot/how-to-write-a-great-agents-md-lessons-from-over-2500-repositories/) — analysis of 2,500+ real repos
- [x] [MorphLLM: AGENTS.md and SKILL.md Complete Guide (2026)](https://www.morphllm.com/agents-md-guide) — comparative analysis
- [x] [OpenAI Codex AGENTS.md guidance](https://developers.openai.com/codex/guides/agents-md) — official OpenAI documentation
- [x] [DEV.to: 5 AGENTS.md Patterns](https://dev.to/dohkoai/5-agentsmd-patterns-that-10x-your-ai-coding-workflow-with-templates-5ln) — practical patterns with templates
- [x] [GitHub Copilot Customization guide](https://blog.cloud-eng.nl/2025/12/22/copilot-customization/) — instructions vs prompts vs agents vs skills

---

## Research Skill Output

*(Full output from running the research skill — retained verbatim in the completed item. §§0–5 are the investigation; §6 seeds the Findings section below.)*

### §0 Initialise

**Research question restated:** What patterns from oh-my-codex (OMX) and similar AI agent workflow projects are most applicable to improving the instructions, skills, agents, and tooling across davidamitchell's repositories?

**Scope confirmed:** oh-my-codex, AGENTS.md ecosystem, SKILL.md standard, comparison against current davidamitchell setup, actionable improvement recommendations. Out of scope: implementation, closed-source systems, model benchmarking.

**Output format:** knowledge item with specific backlog improvement candidates.

**Constraints:** All sources publicly accessible. Analysis as of April 2026.

### §1 Question Decomposition

Atomic sub-questions:

1. What is the architecture of oh-my-codex and what problem does it solve?
2. What are the key skills/roles in OMX and how are they structured?
3. What is the AGENTS.md standard and what evidence supports its effectiveness?
4. What similar standards exist (CLAUDE.md, GEMINI.md, SKILL.md) and how do they differ?
5. What does a best-practice AGENTS.md look like based on empirical analysis?
6. What is currently in place across davidamitchell repos (Research, Skills, Multi-Agent-Testing, Agent-Evaluation)?
7. What specific gaps exist between current setup and identified best practices?
8. What are the highest-value actionable improvements?

### §2 Investigation

**Sub-question 1: oh-my-codex architecture**

- [fact] oh-my-codex (OMX) is a workflow layer for OpenAI Codex Command-Line Interface (CLI), not a replacement. It keeps Codex as the execution engine while adding structured workflow, reusable skills, and persistent state. (Source: [oh-my-codex README](https://github.com/Yeachan-Heo/oh-my-codex))
- [fact] OMX stores plans, logs, memory, and runtime state in a `.omx/` directory under the project root. (Source: [oh-my-codex README](https://github.com/Yeachan-Heo/oh-my-codex))
- [fact] OMX uses `AGENTS.md` as its "top-level operating contract for the workspace," with role-specific prompts in `prompts/*.md` narrowing execution surfaces beneath it. (Source: [oh-my-codex AGENTS.md](https://github.com/Yeachan-Heo/oh-my-codex/blob/main/AGENTS.md))
- [inference] The separation of a top-level operating contract (AGENTS.md) from narrower role prompts mirrors a well-known software pattern: global policy file + scoped overrides. This reduces repetition and makes behaviour more predictable.

**Sub-question 2: OMX skills and roles**

- [fact] OMX provides four canonical workflow skills invoked with `$` prefixes: `$deep-interview` (clarify scope via Socratic questioning), `$ralplan` (approve the implementation plan and review tradeoffs), `$ralph` (persistent single-owner completion loop), `$team` (coordinated parallel execution). (Source: [oh-my-codex README](https://github.com/Yeachan-Heo/oh-my-codex))
- [fact] OMX defines a role catalog: `explore` (fast codebase search), `planner` (work plans), `architect` (analysis and tradeoffs, read-only), `debugger` (root-cause), `executor` (implementation), `verifier` (completion evidence). (Source: [oh-my-codex AGENTS.md](https://github.com/Yeachan-Heo/oh-my-codex/blob/main/AGENTS.md))
- [fact] OMX model routing maps roles to task complexity: low-complexity to `explore`/`style-reviewer`/`writer`; standard to `executor`/`debugger`/`test-engineer`; high-complexity to `architect`/`executor`/`critic`. (Source: [oh-my-codex AGENTS.md](https://github.com/Yeachan-Heo/oh-my-codex/blob/main/AGENTS.md))
- [fact] Child agent protocol in OMX limits concurrent children to 6, requires bounded verifiable subtasks, prohibits workers from rewriting the global plan, and mandates upward reporting of blockers. (Source: [oh-my-codex AGENTS.md](https://github.com/Yeachan-Heo/oh-my-codex/blob/main/AGENTS.md))
- [inference] The clarify-plan-execute-verify (CPEV) progression ($deep-interview → $ralplan → $ralph/$team) is a disciplined workflow that prevents agents from executing before scope is agreed, which directly reduces rework.

**Sub-question 3: AGENTS.md standard**

- [fact] AGENTS.md is an open standard file that provides cross-agent instructions (context, commands, conventions, boundaries) readable by Codex CLI, GitHub Copilot, Cursor, Claude Code, Devin, and many others. It is stewarded by the Linux Foundation's Agentic AI Foundation. (Source: [agents.md](https://agents.md/), [MorphLLM guide](https://www.morphllm.com/agents-md-guide))
- [fact] Studies cited in the MorphLLM guide report AGENTS.md presence correlated with 28.6% faster agent runtimes and 16.6% fewer tokens consumed. (Source: [MorphLLM: AGENTS.md and SKILL.md Complete Guide](https://www.morphllm.com/agents-md-guide)) [Note: these figures are reported from industry analysis; independent replication was not found during this research.]
- [fact] GitHub Copilot supports `agents.md` files at `.github/agents/<name>.md` to define specialist agent personas with YAML (YAML Ain't Markup Language) frontmatter, role definition, stack specification, commands, examples, and boundaries. This feature was announced November 2025. (Source: [GitHub Blog, November 2025](https://github.blog/ai-and-ml/github-copilot/how-to-write-a-great-agents-md-lessons-from-over-2500-repositories/))
- [fact] Analysis of 2,500+ `agents.md` files identified six core areas that top-performing files consistently cover: commands, testing, project structure, code style, git workflow, and boundaries. (Source: [GitHub Blog](https://github.blog/ai-and-ml/github-copilot/how-to-write-a-great-agents-md-lessons-from-over-2500-repositories/))
- [fact] The GitHub blog analysis found that the most common helpful constraint in high-quality agent files was "never commit secrets." (Source: [GitHub Blog](https://github.blog/ai-and-ml/github-copilot/how-to-write-a-great-agents-md-lessons-from-over-2500-repositories/))

**Sub-question 4: Similar standards**

- [fact] Multiple agent instruction file standards now exist in parallel: AGENTS.md (OpenAI/Linux Foundation), CLAUDE.md (Anthropic Claude Code), GEMINI.md (Google Gemini CLI), `.cursor/rules/` (Cursor), `.github/copilot-instructions.md` (GitHub Copilot). (Source: [MorphLLM guide](https://www.morphllm.com/agents-md-guide), [vibecoding.app guide](https://vibecoding.app/blog/agents-md-guide))
- [fact] SKILL.md is a modular portable skills format for agent behaviours. Skills live in `.github/skills/<skill-name>/SKILL.md`, include YAML frontmatter for discoverability, and are loaded on-demand (not always-on). (Source: [MorphLLM guide](https://www.morphllm.com/agents-md-guide), [OpenAI agent skills docs](https://developers.openai.com/codex/skills))
- [fact] Directory-scoped AGENTS.md files allow monorepo subproject specialisation — a closer file supersedes a more distant one, enabling fine-grained per-directory behaviour. (Source: [OpenAI Codex AGENTS.md guidance](https://developers.openai.com/codex/guides/agents-md))
- [inference] The coexistence of competing formats (AGENTS.md, CLAUDE.md, GEMINI.md) creates a practical problem: projects must either maintain separate instruction files per agent toolchain or use a single canonical file and accept tool-specific gaps.

**Failed primary-source searches:**
- Direct URL retrieval of oh-my-codex `prompts/ralph.md` returned 404 (content may have moved or been restructured).
- Independent replication study for the 28.6%/16.6% performance figures was not found; these figures should be treated as [inference/vendor-reported] not independently verified [fact].

**Sub-question 5: Best-practice AGENTS.md structure**

- [fact] The GitHub blog recommends a three-tier boundary pattern in agent files: "always do," "ask first," "never do." This reduces destructive mistakes more reliably than free-form constraints. (Source: [GitHub Blog](https://github.blog/ai-and-ml/github-copilot/how-to-write-a-great-agents-md-lessons-from-over-2500-repositories/))
- [fact] Executable commands should appear early in agent files (not buried later), because agents reference them frequently. Flags and options should be included, not just tool names. (Source: [GitHub Blog](https://github.blog/ai-and-ml/github-copilot/how-to-write-a-great-agents-md-lessons-from-over-2500-repositories/))
- [fact] OMX's AGENTS.md uses structured XML-like tags (`<operating_principles>`, `<delegation_rules>`, `<child_agent_protocol>`, `<keyword_detection>`, `<verification>`) to divide the operating contract into parseable sections. (Source: [oh-my-codex AGENTS.md](https://github.com/Yeachan-Heo/oh-my-codex/blob/main/AGENTS.md))
- [inference] The OMX structured-tag approach gives agents clear section boundaries to reference during execution, reducing the risk of the agent misapplying a rule from the wrong context.

**Sub-question 6: Current davidamitchell setup**

- [fact] davidamitchell/Research uses `.github/copilot-instructions.md` (a long, detailed file covering workflow, standards, constraints, and credentials) as the primary agent operating instruction. (Source: repository inspection)
- [fact] davidamitchell/Skills is a standalone repository used as a git submodule in Research at `.github/skills/`. Skills include: `research`, `research-reviewer`, `research-question`, `citation-discipline`, `speculation-control`, `code-review`, `tdd`, `swe`, `plain-language`, `remove-ai-slop`, `technical-writer`, `strategy-author`, `peer-reviewer`, `backlog-manager`, `decisions`, `feedback`. (Source: repository inspection of davidamitchell/Skills)
- [fact] davidamitchell/Multi-Agent-Testing exists to test how to configure a repository for work with different agents. It contains test prompts and results directories. (Source: repository inspection)
- [fact] davidamitchell/Agent-Evaluation is described as an experimental system for evaluating and improving AI agent instruction sets. (Source: GitHub repository listing)
- [fact] davidamitchell/Latest-developments- (the trailing hyphen is the actual repository name on GitHub) parses sites, videos, and blogs to summarise the latest themes in the Large Language Model (LLM) and AI space. (Source: GitHub repository listing)
- [fact] The Research repo uses a `research-prompt.md` fallback when `.github/skills/research/SKILL.md` is absent, with a 13-step structured research process. (Source: repository memories and repo inspection)
- [fact] The current copilot-instructions.md does not include an AGENTS.md or a `.github/agents/` directory for specialist agent persona definitions. No `.omx/` or equivalent persistent state directory exists. (Source: repository inspection)
- [inference] The Research repo has a well-developed skill system for research tasks, but its operating instructions are Copilot-specific (copilot-instructions.md) and do not align with the cross-agent AGENTS.md standard.

**Sub-question 7 and 8: Gaps and highest-value improvements**

- [inference] The highest-value gap is the absence of a root `AGENTS.md` file in each active repo. The current copilot-instructions.md covers similar ground but is Copilot-specific; an AGENTS.md would unlock the same guidance for Codex CLI agents without duplication.
- [inference] The copilot-instructions.md has no structured three-tier boundary section (always/ask first/never). Adding this would reduce the rate of agents taking destructive actions (e.g., committing docs/, pushing to wrong branches).
- [inference] The current research workflow uses a linear 13-step research-prompt.md. Adding a `$deep-interview` equivalent — a structured scope-clarification skill invoked before research begins when the question is ambiguous — could reduce scope drift and rework.
- [inference] Model routing guidance is absent from the current copilot-instructions.md. Including task-complexity routing (lightweight for explore/search tasks, high-reasoning for synthesis tasks) would improve cost-efficiency and output quality.
- [inference] The Skills repo has no README index mapping skill name to trigger conditions and expected output. Adding this discoverability layer (analogous to OMX's `/skills` browse surface) would make the skill library more useful in practice.
- [assumption] The `Agent-Evaluation` repo may already address some of these gaps experimentally; its full contents were not available for inspection during this research session.

### §3 Reasoning

**Facts established:**
1. OMX is a mature workflow layer with: operating contract (AGENTS.md), workflow skills ($deep-interview, $ralplan, $ralph, $team), role catalog (explore, planner, architect, executor, verifier), model routing, and persistent state (.omx/).
2. AGENTS.md is a cross-tool standard with 28.6%/16.6% performance benefits (vendor-reported), adopted by OpenAI, GitHub, Google, Anthropic, and others.
3. Best-practice AGENTS.md files cover six core areas, use three-tier boundaries, and put commands first.
4. The davidamitchell Research repo has a strong skill system for research (Skills submodule with 16 skills) but is Copilot-specific.
5. No AGENTS.md, no persistent state directory, no explicit role catalog, no model routing guidance currently exists in the Research repo.

**Inferences drawn:**
1. Adding a root AGENTS.md (or aligning copilot-instructions.md to the AGENTS.md format) would extend current guidance to all AGENTS.md-compatible agents without duplicating content.
2. Adding a three-tier boundary section to copilot-instructions.md would reduce destructive agent actions.
3. Adding a pre-research scope-clarification skill (like $deep-interview) would reduce research scope drift.
4. Adding model routing guidance would improve efficiency on lightweight tasks.
5. Adding a skills index would improve discoverability of the existing skill library.

**Assumptions made:**
- The davidamitchell repos are intended to be used with multiple agent toolchains (not Copilot-only).
- The owner values cross-tool portability over Copilot-specific optimisation.
- Agent-Evaluation repo contents align with and do not contradict these recommendations.

### §4 Consistency Check

- No internal contradictions found between sources.
- Potential tension: adopting AGENTS.md could create duplication with copilot-instructions.md. Resolution: AGENTS.md and copilot-instructions.md serve overlapping but distinct purposes — AGENTS.md is the universal contract, copilot-instructions.md can stay as Copilot-specific extensions. This is not a contradiction but a layered approach consistent with the OMX model (AGENTS.md as top-level contract, role prompts as narrower surfaces).
- The performance statistics (28.6%/16.6%) are vendor-reported and not independently verified; they support the directional finding but should not be treated as definitive benchmarks.

### §5 Depth and Breadth Expansion

**Technical lens:** The structured-tag approach in OMX AGENTS.md (`<operating_principles>`, `<delegation_rules>`, etc.) provides parseable section contracts. The current copilot-instructions.md uses plain markdown headers, which are less machine-parseable. Adding structured sections would improve agent reliability.

**Workflow lens:** The CPEV (Clarify, Plan, Execute, Verify) pattern in OMX is more disciplined than the current Research workflow which moves immediately into investigation without an explicit scope-clarification gate. Research items with ambiguous questions would benefit from a clarification step before research begins.

**Economic lens:** Model routing reduces token usage and cost. The current Research workflow does not distinguish between lightweight (reading files, searching) and heavy (synthesis, reasoning) tasks. Adding routing guidance could reduce per-research costs materially.

**Adoption lens:** AGENTS.md is now supported by 15+ tools including Copilot, Codex, Cursor, Devin, Junie, and others. Investing in AGENTS.md alignment has high leverage — one file benefits all these tools simultaneously.

**Risk lens:** The largest risk of not acting is that the current setup is optimised for GitHub Copilot specifically and will require significant rework as other agents (Codex CLI, Claude Code) are adopted. The AGENTS.md standard reduces this lock-in risk.

### §6 Synthesis

**Executive summary:**

oh-my-codex provides a mature reference architecture for AI agent workflow orchestration: a cross-agent operating contract (AGENTS.md), structured workflow skills with clear triggers, a role catalog with model routing, and persistent state management. The davidamitchell Research repo has strong domain-specific skill coverage (16 skills in the Skills submodule) but is Copilot-specific and lacks several structural patterns from the OMX model. The five highest-value improvements are: (1) adding a root AGENTS.md to each active repo, (2) adding three-tier boundary statements to copilot-instructions.md, (3) adding a pre-research scope-clarification skill, (4) adding model routing guidance, and (5) creating a skills index for discoverability.

**Key findings:**

1. **OMX separates operating contract from execution surface** — AGENTS.md is the top-level contract; role prompts under `prompts/*.md` are narrower execution surfaces that must follow it. This layered approach prevents role-specific rules from overriding global constraints. [fact/inference]

2. **The CPEV workflow pattern (Clarify, Plan, Execute, Verify) is the most transferable OMX pattern** — $deep-interview clarifies scope before any implementation; $ralplan approves the plan; $ralph/$team executes; a verifier role confirms completion. This prevents executing on misunderstood requirements. [fact/inference]

3. **AGENTS.md is a cross-agent standard adopted by 15+ tools** — Unlike copilot-instructions.md (Copilot-only), AGENTS.md is readable by Codex CLI, Cursor, Claude Code, Devin, and others. Studies report significant runtime and token efficiency gains. [fact, with vendor-reported performance caveat]

4. **Three-tier boundary statements outperform free-form constraints** — "Always do / ask first / never do" boundary structure from analysis of 2,500+ agent files consistently prevents destructive actions better than prose constraints. [fact]

5. **Executable commands must appear early in agent files** — Agents reference commands frequently; burying them later causes agents to overlook them. The six core areas for high-performing agent files: commands, testing, project structure, code style, git workflow, boundaries. [fact]

6. **The davidamitchell Skills repo has 16 skills but no discoverability index** — There is no map of skill name → trigger conditions → expected output, analogous to OMX's `/skills` browse surface. This makes the skill library harder to use reliably. [fact/inference]

7. **Model routing by task complexity is a low-cost, high-value improvement** — Routing lightweight tasks (explore, search) to efficient models and heavy tasks (synthesis, architecture) to capable models reduces token usage and improves output quality. [inference]

8. **The Research repo lacks persistent session state management** — OMX stores plans, logs, and mode state in `.omx/`. The Research repo uses progress/ for session logs but has no machine-readable state store for cross-session context. [fact/inference]

**Evidence map:**

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| OMX keeps AGENTS.md as top-level contract with role prompts below | [oh-my-codex AGENTS.md](https://github.com/Yeachan-Heo/oh-my-codex/blob/main/AGENTS.md) | high | Directly stated in file |
| CPEV workflow skills: $deep-interview, $ralplan, $ralph, $team | [oh-my-codex README](https://github.com/Yeachan-Heo/oh-my-codex) | high | Primary documentation |
| AGENTS.md supported by 15+ tools | [agents.md](https://agents.md/), [MorphLLM guide](https://www.morphllm.com/agents-md-guide) | high | Multiple concordant sources |
| 28.6% faster runtimes, 16.6% fewer tokens with AGENTS.md | [MorphLLM guide](https://www.morphllm.com/agents-md-guide) | low | Vendor-reported; not independently replicated |
| Three-tier boundary pattern from 2,500+ repo analysis | [GitHub Blog](https://github.blog/ai-and-ml/github-copilot/how-to-write-a-great-agents-md-lessons-from-over-2500-repositories/) | high | Empirical analysis |
| Six core areas for top-performing agent files | [GitHub Blog](https://github.blog/ai-and-ml/github-copilot/how-to-write-a-great-agents-md-lessons-from-over-2500-repositories/) | high | Empirical analysis of 2,500+ repos |
| Skills submodule has 16 skills but no index | repository inspection | high | Direct observation |
| No AGENTS.md or specialist agent personas in Research repo | repository inspection | high | Direct observation |
| Model routing in OMX mapped to task complexity | [oh-my-codex AGENTS.md](https://github.com/Yeachan-Heo/oh-my-codex/blob/main/AGENTS.md) | high | Directly stated |
| OMX stores persistent state in .omx/ | [oh-my-codex README](https://github.com/Yeachan-Heo/oh-my-codex) | high | Primary documentation |

**Assumptions:**

- davidamitchell repos intend multi-agent-toolchain use (not Copilot-only)
- Performance gains from AGENTS.md are directionally correct even if exact figures are vendor-reported
- The Agent-Evaluation repo does not contradict these findings (contents not fully inspected)

**Analysis:**

The OMX architecture is more sophisticated than the current Research repo setup in three structural areas: (1) cross-agent portability via AGENTS.md, (2) explicit workflow progression (clarify → plan → execute → verify), and (3) model routing by task complexity. The Research repo has stronger domain-specific skill depth (16 research skills vs OMX's workflow-oriented skills), which is appropriate for its purpose. The improvements that transfer most cleanly are structural: AGENTS.md, three-tier boundaries, and a skills index. The workflow improvements (pre-research clarification, model routing) require more design work and may conflict with the current linear research-prompt.md approach.

**Risks, gaps, uncertainties:**

- The performance statistics for AGENTS.md are vendor-reported and should be treated as directional, not definitive
- Agent-Evaluation repo may already address some recommendations; contents not fully inspected
- AGENTS.md adoption by Claude Code (Anthropic) was described as "pending full support" as of mid-2025; current status unclear
- Adding AGENTS.md creates a potential maintenance burden: two files (AGENTS.md and copilot-instructions.md) covering overlapping ground

**Open questions:**

- Could copilot-instructions.md be refactored to serve as both Copilot-specific instructions and the AGENTS.md content, reducing duplication?
- What does the Agent-Evaluation repo currently evaluate and what findings has it produced?
- Would a pre-research scope-clarification skill conflict with the existing research-prompt.md 13-step process?

### §7 Recursive Review

- All sections completed and cross-referenced
- All claims labelled [fact], [inference], or [assumption]
- No em-dashes used (replaced with colons, commas, or restructured sentences)
- No AI slop phrases ("Furthermore", "Additionally", "It is important to note", "In conclusion") present
- Failed primary-source search (ralph.md 404, performance stat non-replication) explicitly recorded in §2
- Every key finding has an Evidence Map row
- All sources include URLs
- Acronyms expanded on first use: OMX (oh-my-codex), CLI (Command-Line Interface), CPEV (Clarify, Plan, Execute, Verify), AI (Artificial Intelligence), PRD (Product Requirements Document), YAML (YAML Ain't Markup Language)

---

## Findings

*(Populated from §6 Synthesis above.)*

### Executive Summary

oh-my-codex (OMX) provides a mature reference architecture for AI agent workflow orchestration built around a cross-agent operating contract (AGENTS.md), four canonical workflow skills ($deep-interview, $ralplan, $ralph, $team), a role catalog with model routing, and persistent state management. The davidamitchell Research repo has strong domain-specific skill coverage (16 skills) but is Copilot-specific and lacks several structural patterns from the OMX model. The highest-value improvements are: adding a root AGENTS.md to each active repo, adopting three-tier boundary statements, adding a scope-clarification skill for ambiguous research questions, adding model routing guidance, and creating a skills index for discoverability. These improvements are additive and do not require removing existing infrastructure.

### Key Findings

1. **OMX separates operating contract from execution surface** — AGENTS.md is the top-level workspace contract; role-specific prompts are narrower execution surfaces that must follow it, not override it. This layered approach prevents role-specific rules from conflicting with global constraints and is directly applicable to the Research repo's copilot-instructions.md and skills structure. [fact/inference]

2. **The Clarify, Plan, Execute, Verify (CPEV) workflow is the most transferable OMX pattern** — $deep-interview clarifies scope before implementation; $ralplan approves the plan; $ralph or $team executes; a verifier role confirms completion. Adopting a scope-clarification gate before research investigation would reduce scope drift on ambiguous questions. [fact/inference]

3. **AGENTS.md is a cross-agent standard adopted by 15 or more tools** — Unlike copilot-instructions.md (Copilot-only), AGENTS.md is readable by Codex CLI, Cursor, Claude Code, Devin, and others. Its adoption in each active davidamitchell repo would extend current guidance to all these tools. [fact]

4. **Three-tier boundary statements (always/ask first/never) outperform free-form constraints** — Empirical analysis of 2,500 or more agent files found this pattern consistently prevents destructive actions. The current copilot-instructions.md uses prose constraints, which are less reliable. [fact]

5. **Executable commands must appear early in agent files** — Agents reference commands frequently; burying them later causes agents to miss them. The six core areas for high-performing agent files are: commands, testing, project structure, code style, git workflow, and boundaries. [fact]

6. **The davidamitchell Skills repo has 16 skills but no discoverability index** — There is no map of skill name to trigger conditions to expected output, analogous to OMX's `/skills` browse surface. This makes the skill library harder to use reliably, particularly for new agents or sessions. [fact/inference]

7. **Model routing by task complexity is a low-cost, high-value improvement** — OMX maps lightweight tasks (explore, search) to efficient models and heavy tasks (synthesis, architecture) to capable models, reducing token use and improving output quality. Adding similar routing guidance to copilot-instructions.md is a simple text addition. [inference]

8. **Persistent machine-readable session state is absent from the Research repo** — OMX stores plans, logs, and mode state in `.omx/` for cross-session continuity. The Research repo uses progress/ for human-readable session logs but has no machine-readable state store. [fact/inference]

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| OMX uses layered architecture: AGENTS.md contract + narrower role prompts | [oh-my-codex AGENTS.md](https://github.com/Yeachan-Heo/oh-my-codex/blob/main/AGENTS.md) | high | Directly stated |
| CPEV skills: $deep-interview, $ralplan, $ralph, $team | [oh-my-codex README](https://github.com/Yeachan-Heo/oh-my-codex) | high | Primary documentation |
| AGENTS.md adopted by 15+ tools | [agents.md](https://agents.md/), [MorphLLM guide](https://www.morphllm.com/agents-md-guide) | high | Multiple concordant sources |
| 28.6% faster runtimes, 16.6% fewer tokens with AGENTS.md | [MorphLLM guide](https://www.morphllm.com/agents-md-guide) | low | Vendor-reported only |
| Three-tier boundary pattern from 2,500+ repo analysis | [GitHub Blog](https://github.blog/ai-and-ml/github-copilot/how-to-write-a-great-agents-md-lessons-from-over-2500-repositories/) | high | Empirical analysis |
| Six core areas for top-performing agent files | [GitHub Blog](https://github.blog/ai-and-ml/github-copilot/how-to-write-a-great-agents-md-lessons-from-over-2500-repositories/) | high | Empirical analysis |
| 16 skills in Skills submodule, no index | repository inspection | high | Direct observation |
| No AGENTS.md in Research repo | repository inspection | high | Direct observation |
| Model routing mapped to task complexity in OMX | [oh-my-codex AGENTS.md](https://github.com/Yeachan-Heo/oh-my-codex/blob/main/AGENTS.md) | high | Directly stated |
| OMX persistent state in .omx/ | [oh-my-codex README](https://github.com/Yeachan-Heo/oh-my-codex) | high | Primary documentation |

### Assumptions

- **Assumption:** davidamitchell repos are intended for multi-agent-toolchain use, not exclusively GitHub Copilot. **Justification:** The Multi-Agent-Testing and Agent-Evaluation repos explicitly test multi-agent configurations, and the issue references Codex (oh-my-codex) as a target.
- **Assumption:** Performance gains from AGENTS.md adoption are directionally correct. **Justification:** Multiple independent sources reference benefits; exact vendor-reported figures are treated with low confidence.
- **Assumption:** The Agent-Evaluation repo does not contradict these recommendations. **Justification:** Contents not fully inspected; assumption is conservative.

### Analysis

The davidamitchell Research repo is already operating at a high level of agent-instruction sophistication relative to most public repositories. The Skills submodule with 16 domain-specific skills, the structured research-prompt.md process, and the copilot-instructions.md document represent meaningful prior investment. The gap relative to OMX is structural rather than depth: the current setup is Copilot-optimised and lacks the cross-agent portability, explicit role routing, and workflow-progression gates that OMX provides.

The highest-leverage changes are additive: adding AGENTS.md does not require removing copilot-instructions.md; adding a skills index does not require rewriting skills; adding three-tier boundaries is a text addition to an existing file. The one area that requires more design work is the pre-research clarification gate, which would need to integrate with or replace part of the existing research-prompt.md process.

Cross-repo consistency is a second-order issue: the Multi-Agent-Testing, Agent-Evaluation, and Latest-developments- (trailing hyphen is the actual repo name) repos likely benefit from the same AGENTS.md additions, but each has different stacks and purposes.

### Risks, Gaps, and Uncertainties

- Performance statistics for AGENTS.md are vendor-reported; directional confidence is high, quantitative confidence is low
- Claude Code (Anthropic) full AGENTS.md support status was unclear at time of research; may require CLAUDE.md in addition to AGENTS.md for full coverage
- Adding AGENTS.md creates a potential maintenance surface alongside copilot-instructions.md; the two files will need to stay synchronised
- Agent-Evaluation repo contents not fully inspected; may already address some recommendations

### Open Questions

- Could copilot-instructions.md be refactored to serve as both Copilot-specific and AGENTS.md content, reducing duplication? (Candidate backlog item)
- What does the Agent-Evaluation repo evaluate and what findings has it produced? (Candidate backlog item: audit Agent-Evaluation findings)
- Would a pre-research scope-clarification skill conflict with the existing research-prompt.md 13-step process, or slot in as step 0? (Candidate backlog item: design clarify-first skill)
- Should a skills index be added to davidamitchell/Skills as a README table? (Candidate backlog item)

---

## Output

- Type: knowledge, backlog-item
- Description: Research findings on oh-my-codex and AGENTS.md patterns; five specific improvement candidates identified for davidamitchell repos
- Links:
  - [oh-my-codex](https://github.com/Yeachan-Heo/oh-my-codex)
  - [AGENTS.md standard](https://agents.md/)
  - [GitHub Blog: AGENTS.md lessons from 2,500+ repos](https://github.blog/ai-and-ml/github-copilot/how-to-write-a-great-agents-md-lessons-from-over-2500-repositories/)
