---
review_count: 2
title: "Agent orchestration patterns: lessons from Anvil, Max, and Burke Holland's multi-model orchestration gist"
added: 2026-03-23
status: completed
priority: high  # low | medium | high
blocks: []
tags: [agents, orchestration, personal-assistant, multi-model, copilot-sdk, verification, adversarial-review, skills]
started: 2026-03-24
completed: 2026-03-24
output: [knowledge, backlog-item]
---

# Agent orchestration patterns: lessons from Anvil, Max, and Burke Holland's multi-model orchestration gist

## Research Question

What agent orchestration patterns, verification strategies, and multi-model delegation techniques are demonstrated by Burke Holland's Anvil, Max, and the orchestrator/planner/coder/designer multi-agent gist — and which of these can be directly applied or adapted to build a personal AI assistant that operates without a local IDE?

Supporting questions:
- How does Anvil's "prove it, don't promise it" philosophy (SQL (Structured Query Language) verification ledger, baseline snapshots, adversarial multi-model review) differ from simpler single-agent coding loops, and what does that mean for trust in autonomous agents?
- What is the Orchestrator->Planner->Coder->Designer delegation pattern in the multi-agent gist, and how does parallelisation by file-disjoint phases work in practice?
- How does Max's persistent-daemon model — spinning up GitHub Copilot CLI (Command-Line Interface) workers, routing tasks, learning skills from skills.sh — differ from session-scoped agent invocations?
- What design choices would allow a personal assistant inspired by Max to work entirely through GitHub website interactions and mobile (no local IDE, no Codespace)?
- What are the failure modes and trust boundaries of adversarial multi-model review (as used in Anvil's "Forge" step)?
- How does session memory backed by SQL (as in Anvil and Max) compare to in-context memory for long-running autonomous tasks?

## Scope

**In scope:**
- Anvil's architecture: adversarial review loop, SQL verification ledger, baseline-vs-after snapshots, git autopilot, session memory
  — Source: https://burkeholland.github.io/anvil/
- Burke Holland's multi-agent gist: orchestrator/planner/coder/designer roles, model assignment (Claude Opus 4.6, GPT (Generative Pre-trained Transformer)-5.3-Codex, Gemini 3 Pro), parallelisation by file-disjoint phases
  — Source: https://gist.github.com/burkeholland/0e68481f96e94bbb98134fa6efd00436
- Max's architecture: persistent daemon, Copilot SDK (Software Development Kit) worker dispatch, Telegram interface, skills.sh integration, auto model routing, SQLite memory
  — Sources: https://burkeholland.github.io/max/ and https://github.com/burkeholland/max
- Cross-cutting orchestration patterns: task decomposition, role specialisation, verification-before-delivery, memory persistence
- Practical adaptation for a no-local-IDE environment (GitHub website + iOS app only)
- Connections to existing research in this repo (finishing/synthesising agents, coding AI agent skills survey)

**Out of scope:**
- Full reimplementation of Anvil or Max — the goal is to extract transferable patterns, not reproduce the tools
- Local IDE extensions or Codespace-dependent features
- General LLM (Large Language Model) capability benchmarks unrelated to orchestration
- Credentials or services not listed in the approved credentials table

**Constraints:** Owner interacts via GitHub website and iOS app only. Any personal-assistant design must be triggerable without a terminal or local IDE.

## Context

[fact] Burke Holland's published materials cover three closely related artefacts relevant to multi-agent orchestration in software work. Sources: https://burkeholland.github.io/anvil/ ; https://burkeholland.github.io/max/ ; https://gist.github.com/burkeholland/0e68481f96e94bbb98134fa6efd00436

1. [fact] **Anvil** is a GitHub Copilot Command Line Interface (CLI) chat mode built around verified completion rather than unverified assertions. Its Structured Query Language (SQL) ledger and adversarial review loop are documented as evidence-first controls. Source: https://burkeholland.github.io/anvil/

2. [fact] **The multi-agent gist** is a minimal orchestrator/planner/coder/designer system for Visual Studio Code (VS Code). The orchestrator is instructed to delegate, parallelize, and integrate rather than write code directly, while specialist files define role-specific model assignments. Sources: https://gist.githubusercontent.com/burkeholland/0e68481f96e94bbb98134fa6efd00436/raw/orchestrator.agent.md ; https://gist.githubusercontent.com/burkeholland/0e68481f96e94bbb98134fa6efd00436/raw/coder.agent.md ; https://gist.githubusercontent.com/burkeholland/0e68481f96e94bbb98134fa6efd00436/raw/designer.agent.md

3. [fact] **Max** is a persistent personal Artificial Intelligence (AI) assistant that uses the GitHub Copilot Software Development Kit (SDK) and CLI as its execution substrate. Its public documentation describes a daemon process, worker dispatch, Telegram integration, and on-demand skill learning from skills.sh. Sources: https://burkeholland.github.io/max/docs.html ; https://raw.githubusercontent.com/burkeholland/max/main/README.md

[inference] Taken together, these artefacts provide unusually concrete implementation references for this repository's assistant-design questions because they cover verification, delegation, and continuity as separate but compatible layers. Sources: https://burkeholland.github.io/anvil/ ; https://gist.githubusercontent.com/burkeholland/0e68481f96e94bbb98134fa6efd00436/raw/orchestrator.agent.md ; https://burkeholland.github.io/max/docs.html

[fact] This topic is also adjacent to the repository's prior completed item on agents as finishers and synthesisers, which asked a closely related orchestration question from a different angle. Source: https://raw.githubusercontent.com/davidamitchell/Research/main/Research/completed/2026-03-22-agents-as-finishers-and-synthesisers.md

## Approach

Decompose into the following sub-questions for investigation:

1. **Verification and trust** — How does Anvil's ledger-based evidence bundle change agent accountability? What are the minimum viable verification steps for a no-IDE personal assistant?
2. **Role specialisation and model routing** — Why does the gist assign Opus to orchestration/planning, Codex to code, and Gemini to design? Is model-to-role matching a general principle or project-specific?
3. **Parallelisation strategy** — How does the orchestrator parse file-disjoint phases? What are the limits of this approach for non-code tasks (research, writing, planning)?
4. **Persistence and memory** — Compare SQL-backed memory (Max/Anvil) with in-context memory for a long-running personal assistant. What does Max remember across sessions, and how is retrieval triggered?
5. **Skill learning** — How does Max's `learn_skill` pattern from skills.sh compare to the skills submodule approach in this repo? Are they compatible?
6. **No-IDE adaptation** — Which parts of Max (daemon, worker dispatch, Telegram) are adaptable to a pure GitHub-website workflow? What are the irreducible constraints?

Investigation methods:
- Close reading of Anvil site, Max site, Max GitHub repo, and multi-agent gist source files
- Review of GitHub Copilot SDK documentation (https://docs.github.com/en/copilot/how-tos/copilot-sdk/sdk-getting-started)
- Cross-reference with existing completed research in this repo (coding AI agent skills survey, technology capability models, layered org LLM architecture)
- Identify transferable patterns as candidate backlog items or skills

## Sources

- [x] Anvil project site: https://burkeholland.github.io/anvil/
- [x] Multi-agent orchestration gist (overview page): https://gist.github.com/burkeholland/0e68481f96e94bbb98134fa6efd00436
- [x] Raw orchestrator agent file: https://gist.githubusercontent.com/burkeholland/0e68481f96e94bbb98134fa6efd00436/raw/orchestrator.agent.md
- [x] Raw planner agent file: https://gist.githubusercontent.com/burkeholland/0e68481f96e94bbb98134fa6efd00436/raw/planner.agent.md
- [x] Raw coder agent file: https://gist.githubusercontent.com/burkeholland/0e68481f96e94bbb98134fa6efd00436/raw/coder.agent.md
- [x] Raw designer agent file: https://gist.githubusercontent.com/burkeholland/0e68481f96e94bbb98134fa6efd00436/raw/designer.agent.md
- [x] Max project site: https://burkeholland.github.io/max/
- [x] Max documentation page: https://burkeholland.github.io/max/docs.html
- [x] Max README: https://raw.githubusercontent.com/burkeholland/max/main/README.md
- [x] GitHub Copilot SDK getting started: https://docs.github.com/en/copilot/how-tos/copilot-sdk/sdk-getting-started
- [x] GitHub Copilot Chat in GitHub: https://docs.github.com/en/copilot/how-tos/chat-with-copilot/chat-in-github
- [x] GitHub Copilot Chat in GitHub Mobile: https://docs.github.com/en/copilot/how-tos/chat-with-copilot/chat-in-mobile
- [x] GitHub Copilot coding agent create a pull request (PR): https://docs.github.com/en/copilot/how-tos/use-copilot-agents/coding-agent/create-a-pr
- [x] GitHub Copilot custom instructions on GitHub: https://docs.github.com/en/copilot/how-tos/configure-custom-instructions/add-repository-instructions
- [x] GitHub Copilot custom agents: https://docs.github.com/en/copilot/how-tos/use-copilot-agents/coding-agent/create-custom-agents
- [x] GitHub Copilot skills: https://docs.github.com/en/copilot/how-tos/use-copilot-agents/coding-agent/create-skills
- [x] skills.sh docs: https://skills.sh/docs
- [x] Vercel guide to agent skills: https://vercel.com/kb/guide/agent-skills-creating-installing-and-sharing-reusable-agent-context
- [x] Repo instructions URL: https://raw.githubusercontent.com/davidamitchell/Research/main/.github/copilot-instructions.md
- [x] Prior completed research: https://raw.githubusercontent.com/davidamitchell/Research/main/Research/completed/2026-03-22-coding-ai-agent-skills-survey.md
- [x] Prior completed research: https://raw.githubusercontent.com/davidamitchell/Research/main/Research/completed/2026-03-22-agents-as-finishers-and-synthesisers.md
- [x] Prior completed research: https://raw.githubusercontent.com/davidamitchell/Research/main/Research/completed/2026-03-19-layered-org-llm-architecture.md
- [x] Prior completed research: https://raw.githubusercontent.com/davidamitchell/Research/main/Research/completed/2026-03-08-ai-coding-harnesses-agent-philosophy.md
- [x] Prior completed research: https://raw.githubusercontent.com/davidamitchell/Research/main/Research/completed/2026-03-18-stateless-agent-assumption-failure.md

## Research Skill Output

*(Full output from running the research skill - retained verbatim in the completed item. Sections 0-7 are the investigation; Section 6 seeds the Findings section below.)*

### §0 Initialise

- [fact] Research question restated: the task is to determine which orchestration, verification, memory, and skill patterns from Anvil, Max, and Burke Holland's four-agent gist are transferable to a personal assistant that must operate through GitHub website surfaces and iOS rather than through a local Integrated Development Environment (IDE). Source: https://raw.githubusercontent.com/davidamitchell/Research/main/Research/in-progress/2026-03-23-agent-orchestration-anvil-max.md
- [fact] Scope confirmed: the investigation covers Anvil's verification loop, the gist's role delegation and file-disjoint parallelism, Max's daemon and memory design, skills.sh packaging, and GitHub-native interaction surfaces that can replace local-terminal assumptions. Sources: https://raw.githubusercontent.com/davidamitchell/Research/main/Research/in-progress/2026-03-23-agent-orchestration-anvil-max.md ; https://burkeholland.github.io/anvil/ ; https://burkeholland.github.io/max/ ; https://docs.github.com/en/copilot/how-tos/chat-with-copilot/chat-in-github ; https://docs.github.com/en/copilot/how-tos/chat-with-copilot/chat-in-mobile
- [fact] Constraint confirmed: the owner operates only through GitHub website and iOS app, and the repository instructions explicitly prohibit designs that depend on undocumented credentials, local IDE use, or Codespaces assumptions. Source: https://raw.githubusercontent.com/davidamitchell/Research/main/.github/copilot-instructions.md
- [fact] Prior-work cross-reference completed before external investigation. The most relevant completed items were the skills survey, agents-as-finishers study, layered organisation Large Language Model (LLM) architecture item, Artificial Intelligence (AI) coding harnesses survey, and stateless-agent assumption failure item. Sources: https://raw.githubusercontent.com/davidamitchell/Research/main/Research/completed/2026-03-22-coding-ai-agent-skills-survey.md ; https://raw.githubusercontent.com/davidamitchell/Research/main/Research/completed/2026-03-22-agents-as-finishers-and-synthesisers.md ; https://raw.githubusercontent.com/davidamitchell/Research/main/Research/completed/2026-03-19-layered-org-llm-architecture.md ; https://raw.githubusercontent.com/davidamitchell/Research/main/Research/completed/2026-03-08-ai-coding-harnesses-agent-philosophy.md ; https://raw.githubusercontent.com/davidamitchell/Research/main/Research/completed/2026-03-18-stateless-agent-assumption-failure.md
- [assumption] The absent `.github/skills/research/SKILL.md` submodule file means `research-prompt.md` is the effective procedural fallback for this run. Justification: the repository instructions explicitly document that fallback and the file is publicly present in the repository. Sources: https://raw.githubusercontent.com/davidamitchell/Research/main/.github/copilot-instructions.md ; https://raw.githubusercontent.com/davidamitchell/Research/main/research-prompt.md
- [fact] Output format confirmed: write §§0-7 in the item, then seed Findings directly from §6 without adding new claims. Source: https://raw.githubusercontent.com/davidamitchell/Research/main/research-prompt.md

### §1 Question Decomposition

- [fact] Root question: which parts of Anvil, Max, and the Orchestrator/Planner/Coder/Designer design are generally useful patterns, and which parts are artifacts of a local-machine setup that do not survive the repository's operating constraints? Source: https://raw.githubusercontent.com/davidamitchell/Research/main/Research/in-progress/2026-03-23-agent-orchestration-anvil-max.md
- [fact] Branch A - Verification and trust.
  - A1. What concrete verification mechanisms does Anvil add beyond a normal single-agent coding loop?
  - A2. Which of those mechanisms depend on a local Command-Line Interface (CLI) runtime, and which are portable to a GitHub-first workflow?
  - A3. What failure modes remain even when adversarial review is present?
- [fact] Branch B - Role specialization and delegation.
  - B1. What is the explicit contract of the Orchestrator, Planner, Coder, and Designer agents?
  - B2. How does the gist decide when parallel work is safe?
  - B3. Is model-to-role assignment a durable principle or only a worked example?
- [fact] Branch C - Persistence and memory.
  - C1. What does Max persist in long-running sessions, long-term memory, and conversation logs?
  - C2. How does that compare with in-context memory alone?
  - C3. Which memory layers are necessary for a browser-first assistant?
- [fact] Branch D - Skills and packaging.
  - D1. How does Max learn and install skills?
  - D2. How do skills.sh and GitHub Copilot skills package skills?
  - D3. Is that packaging compatible with this repository's read-only skills-submodule model?
- [fact] Branch E - No-local-IDE adaptation.
  - E1. Which GitHub surfaces already support chat, issue assignment, custom agents, and skills from the web or mobile?
  - E2. Which Max features can be replaced by durable repository state and GitHub workflows?
  - E3. Which features cannot be transferred without introducing unapproved credentials or an always-on local machine?

### §2 Investigation

#### 2.1 Verification and trust

Sources consulted:
- Primary: https://burkeholland.github.io/anvil/
- Primary: https://raw.githubusercontent.com/davidamitchell/Research/main/Research/completed/2026-03-08-ai-coding-harnesses-agent-philosophy.md
- Primary: https://raw.githubusercontent.com/davidamitchell/Research/main/Research/completed/2026-03-18-stateless-agent-assumption-failure.md

Claims:
- [fact] Anvil's homepage says every task is run through the same loop: understand and recall, survey and pushback, baseline, implement, forge, and evidence and commit. Source: https://burkeholland.github.io/anvil/
- [fact] Anvil records build, test, lint, and review results in a SQLite ledger and presents the final evidence bundle as a query result rather than as free-form prose. Source: https://burkeholland.github.io/anvil/
- [fact] Anvil snapshots the project's baseline state before editing and compares after-change results against that baseline so regressions are visible as a before-versus-after delta. Source: https://burkeholland.github.io/anvil/
- [fact] Anvil's "Forge" step combines executable checks with up to three reviewing models that try to find bugs, security holes, and logic errors. Source: https://burkeholland.github.io/anvil/
- [inference] The main trust shift in Anvil is not "multiple models" by itself; it is the combination of executable proof, recorded evidence, and adversarial review, which makes unsupported success claims easier to detect. Sources: https://burkeholland.github.io/anvil/ ; https://raw.githubusercontent.com/davidamitchell/Research/main/Research/completed/2026-03-18-stateless-agent-assumption-failure.md
- [inference] A no-local-IDE assistant can copy Anvil's structure without copying its exact runtime by replacing local terminal evidence with GitHub-native evidence surfaces such as workflow logs, status checks, diff artifacts, and state-bearing files committed back to the repository. Sources: https://burkeholland.github.io/anvil/ ; https://docs.github.com/en/copilot/how-tos/use-copilot-agents/coding-agent/create-a-pr ; https://raw.githubusercontent.com/davidamitchell/Research/main/.github/copilot-instructions.md
- [inference] Adversarial review alone is insufficient for trust because reviewers can still share blind spots, rely on the same incomplete context, or critique code that was never actually executed in the intended environment. Sources: https://burkeholland.github.io/anvil/ ; https://raw.githubusercontent.com/davidamitchell/Research/main/Research/completed/2026-03-18-stateless-agent-assumption-failure.md

#### 2.2 Role specialization and model routing

Sources consulted:
- Primary: https://gist.githubusercontent.com/burkeholland/0e68481f96e94bbb98134fa6efd00436/raw/orchestrator.agent.md
- Primary: https://gist.githubusercontent.com/burkeholland/0e68481f96e94bbb98134fa6efd00436/raw/planner.agent.md
- Primary: https://gist.githubusercontent.com/burkeholland/0e68481f96e94bbb98134fa6efd00436/raw/coder.agent.md
- Primary: https://gist.githubusercontent.com/burkeholland/0e68481f96e94bbb98134fa6efd00436/raw/designer.agent.md
- Primary: https://gist.github.com/burkeholland/0e68481f96e94bbb98134fa6efd00436

Claims:
- [fact] The Orchestrator agent is instructed to coordinate work, never implement directly, obtain a plan from the Planner, parse that plan into phases, run file-disjoint tasks in parallel, and verify that the final output hangs together. Sources: https://gist.githubusercontent.com/burkeholland/0e68481f96e94bbb98134fa6efd00436/raw/orchestrator.agent.md ; https://gist.github.com/burkeholland/0e68481f96e94bbb98134fa6efd00436
- [fact] The Planner agent is explicitly limited to research, verification, edge-case identification, and plan output; it is told not to write code. Source: https://gist.githubusercontent.com/burkeholland/0e68481f96e94bbb98134fa6efd00436/raw/planner.agent.md
- [fact] The Coder agent is configured with GPT-5.3-Codex, broad tool access, and mandatory coding principles focused on explicit structure, low coupling, testability, and regenerability. Source: https://gist.githubusercontent.com/burkeholland/0e68481f96e94bbb98134fa6efd00436/raw/coder.agent.md
- [fact] The Designer agent is configured with Gemini 3.1 Pro and is instructed to prioritize usability, accessibility, and aesthetics rather than defer to engineering preferences. Source: https://gist.githubusercontent.com/burkeholland/0e68481f96e94bbb98134fa6efd00436/raw/designer.agent.md
- [fact] The gist's parallelization rule is file-disjoint phasing: tasks with no overlapping files can run in the same phase, while tasks with overlapping files or explicit dependencies must be sequenced. Sources: https://gist.githubusercontent.com/burkeholland/0e68481f96e94bbb98134fa6efd00436/raw/orchestrator.agent.md ; https://gist.github.com/burkeholland/0e68481f96e94bbb98134fa6efd00436
- [inference] The durable principle is role-to-workload matching, not the exact named model mapping. The pattern assigns high-context planning to a reasoning-oriented model, code change execution to a tool-centric model, and design work to a visually and ergonomically opinionated model. Sources: https://gist.githubusercontent.com/burkeholland/0e68481f96e94bbb98134fa6efd00436/raw/orchestrator.agent.md ; https://gist.githubusercontent.com/burkeholland/0e68481f96e94bbb98134fa6efd00436/raw/planner.agent.md ; https://gist.githubusercontent.com/burkeholland/0e68481f96e94bbb98134fa6efd00436/raw/coder.agent.md ; https://gist.githubusercontent.com/burkeholland/0e68481f96e94bbb98134fa6efd00436/raw/designer.agent.md
- [inference] File-disjoint phasing transfers cleanly to software tasks with explicit file boundaries but transfers weakly to research, writing, and synthesis tasks where outputs may be stored in different files yet still depend on shared concepts and argument structure. Sources: https://gist.githubusercontent.com/burkeholland/0e68481f96e94bbb98134fa6efd00436/raw/orchestrator.agent.md ; https://raw.githubusercontent.com/davidamitchell/Research/main/Research/completed/2026-03-22-agents-as-finishers-and-synthesisers.md

#### 2.3 Persistence and memory

Sources consulted:
- Primary: https://burkeholland.github.io/max/
- Primary: https://burkeholland.github.io/max/docs.html
- Primary: https://raw.githubusercontent.com/burkeholland/max/main/README.md
- Primary: https://docs.github.com/en/copilot/how-tos/copilot-sdk/sdk-getting-started
- Primary: https://raw.githubusercontent.com/davidamitchell/Research/main/Research/completed/2026-03-18-stateless-agent-assumption-failure.md

Claims:
- [fact] Max is described as a persistent daemon that keeps an orchestrator session running, spawns worker Copilot CLI sessions for coding tasks, and can be reached from Telegram or a local terminal user interface. Sources: https://burkeholland.github.io/max/ ; https://raw.githubusercontent.com/burkeholland/max/main/README.md
- [fact] Max's documentation defines a three-layer memory system: a persistent orchestrator session using the Copilot Software Development Kit (SDK) infinite sessions, a long-term SQLite memories table, and a SQLite conversation log that records messages across channels. Source: https://burkeholland.github.io/max/docs.html
- [fact] Max documentation says long-term memory stores categories such as preference, fact, project, person, and routine, and those memories are injected into Max's system prompt. Source: https://burkeholland.github.io/max/docs.html
- [fact] The Copilot SDK getting-started guide confirms that the SDK creates and manages sessions programmatically, supports streaming responses, and depends on Copilot CLI authentication. Source: https://docs.github.com/en/copilot/how-tos/copilot-sdk/sdk-getting-started
- [inference] Max's architecture distinguishes between continuity that should stay in the live session, continuity that should survive a full restart, and activity logs that support cross-channel awareness. That is structurally stronger than relying on the current context window alone. Sources: https://burkeholland.github.io/max/docs.html ; https://raw.githubusercontent.com/burkeholland/max/main/README.md
- [inference] For long-running autonomous tasks, Structured Query Language (SQL)-backed memory is more reliable than in-context memory because it survives session resets, makes retrieval explicit, and allows state to be re-read before action, which directly addresses the orphaned-state failure mode identified in prior repository research. Sources: https://burkeholland.github.io/max/docs.html ; https://raw.githubusercontent.com/davidamitchell/Research/main/Research/completed/2026-03-18-stateless-agent-assumption-failure.md
- [inference] A browser-first assistant still needs all three memory functions, but the persistent-session layer does not have to be a daemon on the owner's machine if durable repository state, workflow runs, and service-side session history can play the continuity role. Sources: https://burkeholland.github.io/max/docs.html ; https://docs.github.com/en/copilot/how-tos/chat-with-copilot/chat-in-github ; https://docs.github.com/en/copilot/how-tos/chat-with-copilot/chat-in-mobile ; https://docs.github.com/en/copilot/how-tos/use-copilot-agents/coding-agent/create-a-pr

#### 2.4 Skills and packaging

Sources consulted:
- Primary: https://skills.sh/docs
- Primary: https://vercel.com/kb/guide/agent-skills-creating-installing-and-sharing-reusable-agent-context
- Primary: https://docs.github.com/en/copilot/how-tos/use-copilot-agents/coding-agent/create-skills
- Primary: https://raw.githubusercontent.com/davidamitchell/Research/main/.github/copilot-instructions.md
- Primary: https://burkeholland.github.io/max/docs.html

Claims:
- [fact] skills.sh describes skills as reusable capabilities for Artificial Intelligence (AI) agents, distributed through an open-source `skills` Command-Line Interface (CLI) and ranked through anonymous install telemetry. Source: https://skills.sh/docs
- [fact] Vercel's agent-skills guide defines a skill as a folder containing `SKILL.md` plus optional supporting files, distinguishes passive always-on context from active on-demand context, and recommends using `AGENTS.md` for always-applicable rules and skills for specialized workflows. Source: https://vercel.com/kb/guide/agent-skills-creating-installing-and-sharing-reusable-agent-context
- [fact] GitHub Copilot's skills documentation defines agent skills in almost the same structural terms: a `SKILL.md` file with YAML frontmatter, optional scripts or resources, and project-level placement under `.github/skills` or personal placement under `~/.copilot/skills`. Source: https://docs.github.com/en/copilot/how-tos/use-copilot-agents/coding-agent/create-skills
- [fact] Max documentation says skills are Markdown instruction files stored in `~/.max/skills/`, that Max can learn a skill by researching available CLI tools and writing a `SKILL.md`, and that it can also discover and install community skills. Source: https://burkeholland.github.io/max/docs.html
- [fact] This repository's instructions explicitly say `.github/skills/` is a read-only submodule and that all skill changes must go to `davidamitchell/Skills` before the submodule pointer is advanced. Source: https://raw.githubusercontent.com/davidamitchell/Research/main/.github/copilot-instructions.md
- [inference] skills.sh, GitHub Copilot skills, and Max's skill mechanism are structurally compatible at the packaging layer because they all converge on directory-scoped `SKILL.md` instructions with optional auxiliary files and routing descriptions. Sources: https://skills.sh/docs ; https://vercel.com/kb/guide/agent-skills-creating-installing-and-sharing-reusable-agent-context ; https://docs.github.com/en/copilot/how-tos/use-copilot-agents/coding-agent/create-skills ; https://burkeholland.github.io/max/docs.html
- [inference] The incompatibility is operational, not conceptual. Max assumes it can learn and write skills dynamically into a user-controlled local directory, while this repository intentionally curates project skills through a separate upstream submodule repository and does not allow ad hoc in-repo skill mutation. Sources: https://burkeholland.github.io/max/docs.html ; https://raw.githubusercontent.com/davidamitchell/Research/main/.github/copilot-instructions.md

#### 2.5 No-local-IDE adaptation

Sources consulted:
- Primary: https://docs.github.com/en/copilot/how-tos/chat-with-copilot/chat-in-github
- Primary: https://docs.github.com/en/copilot/how-tos/chat-with-copilot/chat-in-mobile
- Primary: https://docs.github.com/en/copilot/how-tos/use-copilot-agents/coding-agent/create-a-pr
- Primary: https://docs.github.com/en/copilot/how-tos/use-copilot-agents/coding-agent/create-custom-agents
- Primary: https://docs.github.com/en/copilot/how-tos/configure-custom-instructions/add-repository-instructions
- Primary: https://raw.githubusercontent.com/davidamitchell/Research/main/.github/copilot-instructions.md
- Primary: https://burkeholland.github.io/max/docs.html

Claims:
- [fact] GitHub Copilot Chat on GitHub can be invoked from any GitHub page, keeps recent conversations, supports repository context, and can use web search-backed answers depending on settings. Source: https://docs.github.com/en/copilot/how-tos/chat-with-copilot/chat-in-github
- [fact] GitHub Copilot Chat in GitHub Mobile can answer general and repository-specific questions, but repository-quality answers depend on indexing and the mobile app cannot itself trigger repository indexing. Source: https://docs.github.com/en/copilot/how-tos/chat-with-copilot/chat-in-mobile
- [fact] GitHub's coding-agent create-a-PR documentation says Copilot can be started from issues, the agents panel, Copilot Chat on GitHub.com, GitHub Mobile, GitHub CLI, or agentic tools with Model Context Protocol (MCP) support. Source: https://docs.github.com/en/copilot/how-tos/use-copilot-agents/coding-agent/create-a-pr
- [fact] GitHub custom-agents documentation allows repository-scoped `.github/agents/*.agent.md` profiles with defined tools, prompts, optional model settings, and optional Model Context Protocol (MCP) server configuration. Source: https://docs.github.com/en/copilot/how-tos/use-copilot-agents/coding-agent/create-custom-agents
- [fact] GitHub custom-instructions documentation supports repository-wide `.github/copilot-instructions.md`, path-scoped instruction files, and `AGENTS.md` agent-instruction files. Source: https://docs.github.com/en/copilot/how-tos/configure-custom-instructions/add-repository-instructions
- [fact] Max's Telegram integration requires a Telegram bot token and an authorized user identifier, and its daemon assumes a local machine where `max start` can keep running. Source: https://burkeholland.github.io/max/docs.html
- [inference] The closest browser-first analogue to Max is not a daemon on the owner's laptop; it is a repository-centered assistant built from durable instructions, custom agents, skills, issue assignment, and workflow-driven state transitions that can be launched from GitHub web or mobile. Sources: https://docs.github.com/en/copilot/how-tos/chat-with-copilot/chat-in-github ; https://docs.github.com/en/copilot/how-tos/chat-with-copilot/chat-in-mobile ; https://docs.github.com/en/copilot/how-tos/use-copilot-agents/coding-agent/create-custom-agents ; https://docs.github.com/en/copilot/how-tos/use-copilot-agents/coding-agent/create-a-pr ; https://docs.github.com/en/copilot/how-tos/configure-custom-instructions/add-repository-instructions
- [inference] Telegram-style remote control is not transferable under the repository's documented credential table because no Telegram credential is approved, and the instructions explicitly prohibit assuming new credentials or undocumented capabilities. Sources: https://burkeholland.github.io/max/docs.html ; https://raw.githubusercontent.com/davidamitchell/Research/main/.github/copilot-instructions.md
- [inference] The irreducible constraint of the no-local-IDE environment is that any "always on" continuity must live in GitHub-managed state or repository state, not in a process that depends on the owner keeping a personal machine online. Sources: https://raw.githubusercontent.com/davidamitchell/Research/main/.github/copilot-instructions.md ; https://docs.github.com/en/copilot/how-tos/chat-with-copilot/chat-in-github ; https://docs.github.com/en/copilot/how-tos/chat-with-copilot/chat-in-mobile ; https://docs.github.com/en/copilot/how-tos/use-copilot-agents/coding-agent/create-a-pr

### §3 Reasoning

- [inference] Anvil, Max, and the gist are best treated as three layers of one design space rather than three unrelated tools. Anvil contributes the trust layer, the gist contributes the delegation layer, and Max contributes the continuity layer. Sources: https://burkeholland.github.io/anvil/ ; https://gist.githubusercontent.com/burkeholland/0e68481f96e94bbb98134fa6efd00436/raw/orchestrator.agent.md ; https://burkeholland.github.io/max/docs.html
- [inference] The most portable lesson from Anvil is "evidence before assertion," because that principle remains valid whether the assistant works locally, in GitHub Actions, or through issue-driven coding-agent runs. Sources: https://burkeholland.github.io/anvil/ ; https://docs.github.com/en/copilot/how-tos/use-copilot-agents/coding-agent/create-a-pr
- [inference] The most portable lesson from the gist is that an orchestrator should manage decomposition and integration rather than also being the main implementer, because that makes planning, phase boundaries, and conflict avoidance explicit. Sources: https://gist.githubusercontent.com/burkeholland/0e68481f96e94bbb98134fa6efd00436/raw/orchestrator.agent.md ; https://gist.githubusercontent.com/burkeholland/0e68481f96e94bbb98134fa6efd00436/raw/planner.agent.md
- [inference] The most portable lesson from Max is layered memory, not the daemon itself. The daemon is one implementation choice for continuity, but the general pattern is to separate live context, durable memory, and operational logs. Sources: https://burkeholland.github.io/max/docs.html ; https://raw.githubusercontent.com/burkeholland/max/main/README.md
- [inference] The strongest practical adaptation for this repository is therefore a GitHub-native orchestration stack: repository instructions and `AGENTS.md` for always-on policy, project skills for specialized workflows, issue or agents-panel entry points, and explicit verification artifacts written to the repository or workflow logs. Sources: https://docs.github.com/en/copilot/how-tos/configure-custom-instructions/add-repository-instructions ; https://docs.github.com/en/copilot/how-tos/use-copilot-agents/coding-agent/create-custom-agents ; https://docs.github.com/en/copilot/how-tos/use-copilot-agents/coding-agent/create-skills ; https://docs.github.com/en/copilot/how-tos/use-copilot-agents/coding-agent/create-a-pr
- [inference] Model-to-role mapping should be treated as a routing heuristic rather than as a dogma, because the gist itself encodes task-appropriate specialization rather than a universal law that one vendor model always owns one class of work. Sources: https://gist.githubusercontent.com/burkeholland/0e68481f96e94bbb98134fa6efd00436/raw/orchestrator.agent.md ; https://gist.githubusercontent.com/burkeholland/0e68481f96e94bbb98134fa6efd00436/raw/planner.agent.md ; https://gist.githubusercontent.com/burkeholland/0e68481f96e94bbb98134fa6efd00436/raw/coder.agent.md ; https://gist.githubusercontent.com/burkeholland/0e68481f96e94bbb98134fa6efd00436/raw/designer.agent.md

### §4 Consistency Check

- [fact] Cross-check completed: the claim that Max uses three memory layers matches the Max docs page's explicit sections on persistent session, long-term SQLite memory, and conversation log. Source: https://burkeholland.github.io/max/docs.html
- [fact] Cross-check completed: the claim that the gist parallelizes by non-overlapping files matches both the gist overview and the raw orchestrator file. Sources: https://gist.github.com/burkeholland/0e68481f96e94bbb98134fa6efd00436 ; https://gist.githubusercontent.com/burkeholland/0e68481f96e94bbb98134fa6efd00436/raw/orchestrator.agent.md
- [fact] Cross-check completed: the claim that GitHub surfaces can launch Copilot work from mobile and web is directly stated in the create-a-PR documentation and reinforced by the chat-in-GitHub and chat-in-mobile guides. Sources: https://docs.github.com/en/copilot/how-tos/use-copilot-agents/coding-agent/create-a-pr ; https://docs.github.com/en/copilot/how-tos/chat-with-copilot/chat-in-github ; https://docs.github.com/en/copilot/how-tos/chat-with-copilot/chat-in-mobile
- [inference] The main unresolved tension is that Max demonstrates richer personal-assistant behavior than today's documented GitHub web and mobile surfaces expose, but that does not invalidate the adaptation conclusion because the question asks which patterns transfer, not whether GitHub already provides an identical packaged assistant. Sources: https://burkeholland.github.io/max/docs.html ; https://docs.github.com/en/copilot/how-tos/chat-with-copilot/chat-in-github ; https://docs.github.com/en/copilot/how-tos/chat-with-copilot/chat-in-mobile ; https://docs.github.com/en/copilot/how-tos/use-copilot-agents/coding-agent/create-a-pr
- [inference] No contradiction remains between the skills findings, because structural compatibility at the `SKILL.md` packaging layer can coexist with operational incompatibility in how and where skills are authored and installed. Sources: https://vercel.com/kb/guide/agent-skills-creating-installing-and-sharing-reusable-agent-context ; https://docs.github.com/en/copilot/how-tos/use-copilot-agents/coding-agent/create-skills ; https://burkeholland.github.io/max/docs.html ; https://raw.githubusercontent.com/davidamitchell/Research/main/.github/copilot-instructions.md

### §5 Depth and Breadth Expansion

- [inference] Technical lens: file-disjoint phasing is a strong optimization for code changes but weak for research synthesis, policy writing, or strategy documents, so a browser-first assistant should parallelize mainly where merge boundaries are objective and machine-checkable. Sources: https://gist.githubusercontent.com/burkeholland/0e68481f96e94bbb98134fa6efd00436/raw/orchestrator.agent.md ; https://raw.githubusercontent.com/davidamitchell/Research/main/.github/copilot-instructions.md
- [inference] Operational lens: Anvil's baseline and evidence bundle pattern is especially valuable in web-triggered workflows because stateless session boundaries increase the need for durable proof surfaces and re-entry checkpoints. Sources: https://burkeholland.github.io/anvil/ ; https://raw.githubusercontent.com/davidamitchell/Research/main/Research/completed/2026-03-18-stateless-agent-assumption-failure.md
- [inference] Economic lens: the gist's role split and Max's auto-routing both imply a cost-control principle - reserve premium reasoning for orchestration or complex analysis, and use cheaper or more tool-effective models for bounded execution tasks. Sources: https://gist.githubusercontent.com/burkeholland/0e68481f96e94bbb98134fa6efd00436/raw/coder.agent.md ; https://gist.githubusercontent.com/burkeholland/0e68481f96e94bbb98134fa6efd00436/raw/designer.agent.md ; https://burkeholland.github.io/max/docs.html
- [inference] Behavioral lens: Max's persistent memory and multi-channel design reduce the human's need to restate preferences and context, which is precisely the complementarity pattern identified in the repository's finishers-and-synthesisers research. Sources: https://burkeholland.github.io/max/docs.html ; https://raw.githubusercontent.com/davidamitchell/Research/main/Research/completed/2026-03-22-agents-as-finishers-and-synthesisers.md
- [inference] Governance lens: this repository's explicit credential table and read-only skills submodule mean the right adaptation is a constrained assistant with auditable state transitions, not an open-ended personal daemon that can quietly accrete new capabilities or tokens over time. Source: https://raw.githubusercontent.com/davidamitchell/Research/main/.github/copilot-instructions.md
- [inference] Historical lens: these artefacts show a progression from prompt-centric single-session agents toward systems that externalize planning, memory, and verification into first-class runtime structures. That aligns with the repository's broader research arc on context engineering, stateful workflows, and durable agent harnesses. Sources: https://burkeholland.github.io/anvil/ ; https://gist.githubusercontent.com/burkeholland/0e68481f96e94bbb98134fa6efd00436/raw/orchestrator.agent.md ; https://burkeholland.github.io/max/docs.html ; https://raw.githubusercontent.com/davidamitchell/Research/main/Research/completed/2026-03-22-coding-ai-agent-skills-survey.md ; https://raw.githubusercontent.com/davidamitchell/Research/main/Research/completed/2026-03-22-agents-as-finishers-and-synthesisers.md ; https://raw.githubusercontent.com/davidamitchell/Research/main/Research/completed/2026-03-18-stateless-agent-assumption-failure.md

### §6 Synthesis

- [inference] **Executive summary draft:** The best-fit adaptation for this repository is a GitHub-native assistant that borrows Anvil's verification discipline, the gist's role separation, and Max's layered continuity model, while dropping Max's local-daemon and Telegram assumptions. That conclusion follows because the transferable value lies in explicit proof, explicit delegation, and durable memory, whereas the non-transferable parts depend on a continuously running personal machine and credentials that the repository does not approve. Sources: https://burkeholland.github.io/anvil/ ; https://gist.githubusercontent.com/burkeholland/0e68481f96e94bbb98134fa6efd00436/raw/orchestrator.agent.md ; https://burkeholland.github.io/max/docs.html ; https://raw.githubusercontent.com/davidamitchell/Research/main/.github/copilot-instructions.md
- [inference] **Key findings draft:**
  1. [inference] Anvil's most important contribution is a trust architecture in which builds, tests, lint checks, baselines, and reviewer verdicts are recorded as durable evidence rather than summarized as model-written assurances. Sources: https://burkeholland.github.io/anvil/ ; https://raw.githubusercontent.com/davidamitchell/Research/main/Research/completed/2026-03-18-stateless-agent-assumption-failure.md
  2. [fact] Burke Holland's four-agent gist demonstrates a clean delegation contract in which the orchestrator never codes, the planner researches and decomposes, and safe parallelism is defined by non-overlapping file ownership. Sources: https://gist.githubusercontent.com/burkeholland/0e68481f96e94bbb98134fa6efd00436/raw/orchestrator.agent.md ; https://gist.githubusercontent.com/burkeholland/0e68481f96e94bbb98134fa6efd00436/raw/planner.agent.md
  3. [inference] The gist's model assignment is best read as role-specialized routing guidance rather than as a universal fixed mapping from one vendor model to one type of work. Sources: https://gist.githubusercontent.com/burkeholland/0e68481f96e94bbb98134fa6efd00436/raw/coder.agent.md ; https://gist.githubusercontent.com/burkeholland/0e68481f96e94bbb98134fa6efd00436/raw/designer.agent.md
  4. [inference] Max's strongest architectural lesson is layered continuity - persistent live session, SQLite long-term memory, and conversation logging - because each layer solves a different failure mode that in-context memory alone cannot solve. Sources: https://burkeholland.github.io/max/docs.html ; https://raw.githubusercontent.com/burkeholland/max/main/README.md
  5. [inference] skills.sh, GitHub Copilot skills, and Max's learn-skill mechanism converge on the same `SKILL.md` packaging idea, so the repository can reuse community skill patterns without abandoning its curated submodule model. Sources: https://skills.sh/docs ; https://vercel.com/kb/guide/agent-skills-creating-installing-and-sharing-reusable-agent-context ; https://docs.github.com/en/copilot/how-tos/use-copilot-agents/coding-agent/create-skills ; https://raw.githubusercontent.com/davidamitchell/Research/main/.github/copilot-instructions.md
  6. [inference] A browser-first adaptation should treat GitHub issues, the agents panel, web chat, mobile chat, custom agents, repository instructions, and skills as the assistant's control plane, because those are the documented surfaces the owner can actually use. Sources: https://docs.github.com/en/copilot/how-tos/use-copilot-agents/coding-agent/create-a-pr ; https://docs.github.com/en/copilot/how-tos/chat-with-copilot/chat-in-github ; https://docs.github.com/en/copilot/how-tos/chat-with-copilot/chat-in-mobile ; https://docs.github.com/en/copilot/how-tos/use-copilot-agents/coding-agent/create-custom-agents ; https://docs.github.com/en/copilot/how-tos/configure-custom-instructions/add-repository-instructions
  7. [inference] Max's local daemon and Telegram interface are not directly transferable to this repository's operating model because they assume a continuously running personal machine and credentials that are not in the repository's approved table. Sources: https://burkeholland.github.io/max/docs.html ; https://raw.githubusercontent.com/davidamitchell/Research/main/.github/copilot-instructions.md
  8. [inference] Adversarial multi-model review should be used as a critique layer after execution, not as a substitute for execution, because reviewers can disagree productively yet still miss environment-specific or state-specific failures that only real verification exposes. Sources: https://burkeholland.github.io/anvil/ ; https://raw.githubusercontent.com/davidamitchell/Research/main/Research/completed/2026-03-18-stateless-agent-assumption-failure.md
- [fact] **Evidence map draft:** the Findings section below binds each key finding to one or more public URLs in the Evidence Map table. Source: https://raw.githubusercontent.com/davidamitchell/Research/main/Research/in-progress/2026-03-23-agent-orchestration-anvil-max.md
- [assumption] **Assumptions draft:** the main operating assumption is that GitHub web, mobile, and coding-agent surfaces remain the owner's primary interaction points because that constraint is explicitly documented and no new credentials are approved. Source: https://raw.githubusercontent.com/davidamitchell/Research/main/.github/copilot-instructions.md
- [inference] **Analysis draft:** deployability in this repository should be judged primarily against GitHub-documented control surfaces and repository constraints, then secondarily against the richer but less portable features in Max's local-daemon model. Sources: https://docs.github.com/en/copilot/how-tos/use-copilot-agents/coding-agent/create-a-pr ; https://docs.github.com/en/copilot/how-tos/chat-with-copilot/chat-in-github ; https://docs.github.com/en/copilot/how-tos/chat-with-copilot/chat-in-mobile ; https://burkeholland.github.io/max/docs.html ; https://raw.githubusercontent.com/davidamitchell/Research/main/.github/copilot-instructions.md
- [fact] **Risks and gaps draft:** Max's published docs describe architecture and behavior but do not expose all internal implementation details, and Anvil's public site documents the verification philosophy more strongly than its concrete file layout or source code. Sources: https://burkeholland.github.io/max/docs.html ; https://burkeholland.github.io/anvil/
- [inference] **Open questions draft:** the remaining open design question is how much of Max-like continuity can be reproduced through GitHub-native workflows alone before a dedicated service becomes necessary. Sources: https://docs.github.com/en/copilot/how-tos/use-copilot-agents/coding-agent/create-a-pr ; https://docs.github.com/en/copilot/how-tos/chat-with-copilot/chat-in-github ; https://raw.githubusercontent.com/davidamitchell/Research/main/.github/copilot-instructions.md

### §7 Recursive Review

- [inference] The current draft now binds each major claim in §§0-6 either to public URLs or to explicit inference and assumption labels, based on a manual audit of this document's source-bound sentences. Source: https://raw.githubusercontent.com/davidamitchell/Research/main/Research/in-progress/2026-03-23-agent-orchestration-anvil-max.md
- [inference] The synthesis remains within scope because it compares transferability and adaptation choices rather than proposing a full reimplementation of Anvil or Max. Sources: https://raw.githubusercontent.com/davidamitchell/Research/main/Research/in-progress/2026-03-23-agent-orchestration-anvil-max.md ; https://raw.githubusercontent.com/davidamitchell/Research/main/.github/copilot-instructions.md
- [inference] Residual uncertainty is concentrated in unpublished Max internals and in the unresolved boundary between GitHub-native orchestration and a dedicated long-running service. Sources: https://burkeholland.github.io/max/docs.html ; https://raw.githubusercontent.com/davidamitchell/Research/main/.github/copilot-instructions.md
- [inference] The item is ready to seed Findings because §6 already states the answer, the claim set, the evidence logic, the assumptions, and the remaining gap. Source: https://raw.githubusercontent.com/davidamitchell/Research/main/Research/in-progress/2026-03-23-agent-orchestration-anvil-max.md

## Findings

### Executive Summary

[inference] The best-fit architecture for this repository is a GitHub-native assistant that uses durable verification artifacts, specialist delegation, and persistent external memory instead of a laptop-resident Max-style daemon. Sources: https://docs.github.com/en/copilot/how-tos/use-copilot-agents/coding-agent/create-a-pr ; https://docs.github.com/en/copilot/how-tos/chat-with-copilot/chat-in-github ; https://burkeholland.github.io/max/docs.html ; https://raw.githubusercontent.com/davidamitchell/Research/main/.github/copilot-instructions.md

[fact] Anvil's published design centers trust on recorded checks, baseline-versus-after comparison, and a SQLite evidence bundle rather than on unverified agent prose. Source: https://burkeholland.github.io/anvil/

[fact] Burke Holland's four-agent gist separates orchestration, planning, coding, and design, and it only parallelizes work when file ownership does not overlap. Sources: https://gist.githubusercontent.com/burkeholland/0e68481f96e94bbb98134fa6efd00436/raw/orchestrator.agent.md ; https://gist.githubusercontent.com/burkeholland/0e68481f96e94bbb98134fa6efd00436/raw/planner.agent.md

[inference] Max shows that long-running assistants need layered continuity, but this repository must realize that continuity through GitHub-managed surfaces, repository state, and approved credentials rather than through an always-on personal machine. Sources: https://burkeholland.github.io/max/docs.html ; https://docs.github.com/en/copilot/how-tos/chat-with-copilot/chat-in-mobile ; https://raw.githubusercontent.com/davidamitchell/Research/main/.github/copilot-instructions.md

### Key Findings

1. **[high]** [inference] Anvil demonstrates that an autonomous assistant becomes more trustworthy when it records builds, tests, lint checks, baselines, and reviewer verdicts as durable evidence artifacts that can be inspected independently of the model's narrative summary. Sources: https://burkeholland.github.io/anvil/ ; https://raw.githubusercontent.com/davidamitchell/Research/main/Research/completed/2026-03-18-stateless-agent-assumption-failure.md
2. **[high]** [fact] Burke Holland's four-agent gist enforces a delegation boundary in which the orchestrator coordinates phases and conflict avoidance, the planner researches and decomposes, and the specialists execute within explicitly scoped domains and files. Sources: https://gist.githubusercontent.com/burkeholland/0e68481f96e94bbb98134fa6efd00436/raw/orchestrator.agent.md ; https://gist.githubusercontent.com/burkeholland/0e68481f96e94bbb98134fa6efd00436/raw/planner.agent.md
3. **[medium]** [inference] The gist's assignment of Claude Opus to orchestration, GPT-5.3-Codex to coding, and Gemini to design should be treated as a role-routing heuristic tied to workload shape rather than as a universal fixed mapping for every repository. Sources: https://gist.githubusercontent.com/burkeholland/0e68481f96e94bbb98134fa6efd00436/raw/coder.agent.md ; https://gist.githubusercontent.com/burkeholland/0e68481f96e94bbb98134fa6efd00436/raw/designer.agent.md
4. **[high]** [inference] Max's three-layer continuity model of persistent live session, SQLite long-term memory, and conversation logging addresses different failure modes, making it more robust for long-running work than relying on in-context memory alone. Sources: https://burkeholland.github.io/max/docs.html ; https://raw.githubusercontent.com/burkeholland/max/main/README.md
5. **[high]** [inference] skills.sh, GitHub Copilot skills, and Max's learn-skill mechanism all converge on `SKILL.md`-based packaging, which means the repository can adopt community skill structure while still curating actual project skills through its separate upstream submodule. Sources: https://skills.sh/docs ; https://vercel.com/kb/guide/agent-skills-creating-installing-and-sharing-reusable-agent-context ; https://docs.github.com/en/copilot/how-tos/use-copilot-agents/coding-agent/create-skills ; https://raw.githubusercontent.com/davidamitchell/Research/main/.github/copilot-instructions.md
6. **[high]** [fact] The repository's browser-first operating model already exposes documented assistant entry points in GitHub issues, the agents panel, GitHub web chat, GitHub Mobile chat, repository instructions, custom agents, and project skills. Sources: https://docs.github.com/en/copilot/how-tos/use-copilot-agents/coding-agent/create-a-pr ; https://docs.github.com/en/copilot/how-tos/chat-with-copilot/chat-in-github ; https://docs.github.com/en/copilot/how-tos/chat-with-copilot/chat-in-mobile ; https://docs.github.com/en/copilot/how-tos/use-copilot-agents/coding-agent/create-custom-agents ; https://docs.github.com/en/copilot/how-tos/configure-custom-instructions/add-repository-instructions
7. **[high]** [inference] Max's local daemon and Telegram bot are not directly portable to this repository because they depend on a continuously running machine and credentials that are outside the repository's approved credential table. Sources: https://burkeholland.github.io/max/docs.html ; https://raw.githubusercontent.com/davidamitchell/Research/main/.github/copilot-instructions.md
8. **[medium]** [inference] Adversarial multi-model review is a valuable critique layer after execution, but it cannot replace executable verification because reviewers can still miss state-specific, environment-specific, or integration-specific failures that only real checks expose. Sources: https://burkeholland.github.io/anvil/ ; https://raw.githubusercontent.com/davidamitchell/Research/main/Research/completed/2026-03-18-stateless-agent-assumption-failure.md

### Evidence Map

| claim | source | confidence | notes |
| --- | --- | --- | --- |
| [fact] Anvil increases trust by recording objective evidence instead of relying on prose. | https://burkeholland.github.io/anvil/ | high | The site explicitly describes the SQLite ledger, baseline snapshots, and evidence bundle. |
| [fact] The gist enforces non-coding orchestration plus file-disjoint parallel phases. | https://gist.githubusercontent.com/burkeholland/0e68481f96e94bbb98134fa6efd00436/raw/orchestrator.agent.md | high | The orchestrator instructions define planner-first delegation and file-overlap rules. |
| [inference] Model assignment in the gist is heuristic role routing, not a universal law. | https://gist.githubusercontent.com/burkeholland/0e68481f96e94bbb98134fa6efd00436/raw/coder.agent.md ; https://gist.githubusercontent.com/burkeholland/0e68481f96e94bbb98134fa6efd00436/raw/designer.agent.md | medium | The files show explicit role-to-model choices, but generalization beyond the example is inferential. |
| [fact] Max uses layered continuity rather than only live context. | https://burkeholland.github.io/max/docs.html ; https://raw.githubusercontent.com/burkeholland/max/main/README.md | high | The docs explicitly define persistent session, SQLite memory, and conversation logging. |
| [fact] `SKILL.md` packaging is shared across skills.sh, GitHub Copilot skills, and Max. | https://skills.sh/docs ; https://vercel.com/kb/guide/agent-skills-creating-installing-and-sharing-reusable-agent-context ; https://docs.github.com/en/copilot/how-tos/use-copilot-agents/coding-agent/create-skills ; https://burkeholland.github.io/max/docs.html | high | The packaging convergence is directly documented across all three systems. |
| [fact] GitHub web and mobile already expose owner-usable assistant entry points. | https://docs.github.com/en/copilot/how-tos/use-copilot-agents/coding-agent/create-a-pr ; https://docs.github.com/en/copilot/how-tos/chat-with-copilot/chat-in-github ; https://docs.github.com/en/copilot/how-tos/chat-with-copilot/chat-in-mobile | high | The docs explicitly list web, mobile, issues, agents panel, and chat entry points. |
| [fact] Max's daemon and Telegram model conflict with this repository's documented operating constraints. | https://burkeholland.github.io/max/docs.html ; https://raw.githubusercontent.com/davidamitchell/Research/main/.github/copilot-instructions.md | high | Max requires local runtime and optional Telegram credentials; the repo forbids assuming unlisted credentials and local-IDE assumptions. |
| [inference] Adversarial review should follow execution rather than replace it. | https://burkeholland.github.io/anvil/ ; https://raw.githubusercontent.com/davidamitchell/Research/main/Research/completed/2026-03-18-stateless-agent-assumption-failure.md | medium | Anvil itself pairs review with executable proof; the stronger claim about failure coverage is inferential but well grounded. |

### Assumptions

- [assumption] The repository's published operating constraints remain authoritative during implementation planning, especially the owner's GitHub-website-plus-iOS workflow and the approved-credentials table. Source: https://raw.githubusercontent.com/davidamitchell/Research/main/.github/copilot-instructions.md
- [assumption] GitHub's documented web and mobile surfaces are sufficient as the user-facing control plane for an assistant even if they are less feature-rich than Max's daemon-plus-Telegram experience. Sources: https://docs.github.com/en/copilot/how-tos/chat-with-copilot/chat-in-github ; https://docs.github.com/en/copilot/how-tos/chat-with-copilot/chat-in-mobile ; https://burkeholland.github.io/max/docs.html

### Analysis

- [inference] Deployability should be weighted more heavily than feature richness in this repository, because the owner's fixed control surfaces are GitHub web and iOS rather than a continuously running personal machine. Sources: https://raw.githubusercontent.com/davidamitchell/Research/main/.github/copilot-instructions.md ; https://docs.github.com/en/copilot/how-tos/chat-with-copilot/chat-in-github ; https://docs.github.com/en/copilot/how-tos/chat-with-copilot/chat-in-mobile
- [inference] Anvil's verification pattern deserves priority over sophisticated model routing, because evidence artifacts mitigate session-boundary and trust risks more directly than choosing among specialist models does. Sources: https://burkeholland.github.io/anvil/ ; https://raw.githubusercontent.com/davidamitchell/Research/main/Research/completed/2026-03-18-stateless-agent-assumption-failure.md
- [inference] Max's continuity design is worth adapting only at the durable-state layer, because GitHub-native surfaces can reproduce instruction, memory, and workflow state without reproducing a laptop daemon's ambient presence. Sources: https://burkeholland.github.io/max/docs.html ; https://docs.github.com/en/copilot/how-tos/use-copilot-agents/coding-agent/create-a-pr ; https://raw.githubusercontent.com/davidamitchell/Research/main/.github/copilot-instructions.md

### Risks, Gaps, and Uncertainties

- [fact] Max's public documentation is sufficient to establish the architecture pattern but not every internal implementation detail, so claims about exact internal routing logic or storage schema would overreach the available evidence. Source: https://burkeholland.github.io/max/docs.html
- [fact] Anvil's public site documents the philosophy and loop structure strongly, but deeper implementation details beyond the published description were not required to answer the transferability question. Source: https://burkeholland.github.io/anvil/
- [fact] GitHub Mobile has documented limitations around repository indexing and context quality, so a browser-first assistant may need repository preparation work to get the best possible answers in mobile contexts. Source: https://docs.github.com/en/copilot/how-tos/chat-with-copilot/chat-in-mobile
- [inference] The exact boundary where GitHub-native workflows stop being sufficient and a dedicated long-running service becomes necessary remains unresolved and depends on how proactive or cross-channel the desired assistant must become. Sources: https://docs.github.com/en/copilot/how-tos/use-copilot-agents/coding-agent/create-a-pr ; https://raw.githubusercontent.com/davidamitchell/Research/main/.github/copilot-instructions.md

### Open Questions

- [inference] At what point does a GitHub-native assistant need a dedicated service layer for proactive reminders, scheduled follow-up, or cross-repository memory instead of repository and workflow state alone? Sources: https://docs.github.com/en/copilot/how-tos/use-copilot-agents/coding-agent/create-a-pr ; https://raw.githubusercontent.com/davidamitchell/Research/main/.github/copilot-instructions.md
- [inference] Which assistant functions should be encoded as project skills versus repository instructions versus custom agents so that the system stays discoverable without becoming brittle? Sources: https://docs.github.com/en/copilot/how-tos/use-copilot-agents/coding-agent/create-skills ; https://docs.github.com/en/copilot/how-tos/configure-custom-instructions/add-repository-instructions ; https://docs.github.com/en/copilot/how-tos/use-copilot-agents/coding-agent/create-custom-agents
- [inference] Can Anvil-style evidence bundles be expressed as a reusable GitHub workflow or skill pattern for this repository without adding new credentials or external infrastructure? Sources: https://burkeholland.github.io/anvil/ ; https://docs.github.com/en/copilot/how-tos/use-copilot-agents/coding-agent/create-skills ; https://raw.githubusercontent.com/davidamitchell/Research/main/.github/copilot-instructions.md

### Output

- **Type:** knowledge
- **Description:** Transferable design patterns from Anvil, Max, and Burke Holland's multi-agent gist, with a concrete recommendation to implement a GitHub-native assistant that uses evidence-first verification, explicit role delegation, and durable external memory rather than a local daemon.
- **Links:** https://burkeholland.github.io/anvil/ ; https://burkeholland.github.io/max/docs.html ; https://gist.githubusercontent.com/burkeholland/0e68481f96e94bbb98134fa6efd00436/raw/orchestrator.agent.md

## Output

- **Type:** knowledge, backlog-item
- **Description:** Distilled orchestration patterns, verification strategies, and memory/skill architectures from Anvil, Max, and the multi-agent gist, with a practical assessment of which apply to a no-local-IDE personal assistant setup.
- **Links:** https://burkeholland.github.io/anvil/ ; https://burkeholland.github.io/max/docs.html ; https://gist.githubusercontent.com/burkeholland/0e68481f96e94bbb98134fa6efd00436/raw/orchestrator.agent.md
