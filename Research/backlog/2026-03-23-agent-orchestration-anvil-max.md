---
title: "Agent orchestration patterns: lessons from Anvil, Max, and Burke Holland's multi-model orchestration gist"
added: 2026-03-23
status: backlog  # backlog | in-progress | reviewing | completed
priority: high  # low | medium | high
blocks: []
tags: [agents, orchestration, personal-assistant, multi-model, copilot-sdk, verification, adversarial-review, skills]
started: ~
completed: ~
output: [knowledge, backlog-item]
---

# Agent orchestration patterns: lessons from Anvil, Max, and Burke Holland's multi-model orchestration gist

## Research Question

What agent orchestration patterns, verification strategies, and multi-model delegation techniques are demonstrated by Burke Holland's Anvil, Max, and the orchestrator/planner/coder/designer multi-agent gist — and which of these can be directly applied or adapted to build a personal AI assistant that operates without a local IDE?

Supporting questions:
- How does Anvil's "prove it, don't promise it" philosophy (SQL (Structured Query Language) verification ledger, baseline snapshots, adversarial multi-model review) differ from simpler single-agent coding loops, and what does that mean for trust in autonomous agents?
- What is the Orchestrator→Planner→Coder→Designer delegation pattern in the multi-agent gist, and how does parallelisation by file-disjoint phases work in practice?
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

Burke Holland (Developer Advocate at GitHub) has published three complementary artefacts that together represent an unusually concrete and practical take on multi-agent orchestration:

1. **Anvil** is a GitHub Copilot CLI chat mode that addresses a core failure of AI coding agents — claiming completion without verification. Its SQL ledger and adversarial review loop (up to three models attacking each change) shift the trust model: evidence replaces prose assertions.

2. **The multi-agent gist** is a minimal but fully wired orchestrator/planner/coder/designer system for Visual Studio Code (VS Code). The orchestrator (Opus) never writes code itself; it delegates, parallelises, and integrates. Each specialist runs the best-fit model for its role.

3. **Max** is a persistent personal AI assistant that uses the GitHub Copilot Software Development Kit (SDK) and CLI as its execution substrate. It runs as a daemon, dispatches workers, integrates with Telegram for mobile interaction, and learns new skills on demand from skills.sh. This is the closest published example of the "always-on personal assistant" pattern relevant to this research repo's broader goals.

These three artefacts are closely related to the existing backlog item on agents-as-finishers-and-synthesisers. They offer concrete implementation reference points rather than abstract frameworks.

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

- Anvil project site: https://burkeholland.github.io/anvil/
- Anvil GitHub repository: https://github.com/burkeholland/anvil/tree/main
- Multi-agent orchestration gist (Orchestrator/Planner/Coder/Designer): https://gist.github.com/burkeholland/0e68481f96e94bbb98134fa6efd00436
- Max project site: https://burkeholland.github.io/max/
- Max GitHub repository: https://github.com/burkeholland/max
- GitHub Copilot SDK documentation: https://docs.github.com/en/copilot/how-tos/copilot-sdk/sdk-getting-started
- GitHub Copilot CLI documentation: https://docs.github.com/en/copilot/how-tos/copilot-cli
- skills.sh community library: https://skills.sh

## Research Skill Output

_To be completed when this item moves to in-progress._

## Findings

_To be completed when this item moves to in-progress._

## Output

- **Type:** knowledge, backlog-item
- **Description:** Distilled orchestration patterns, verification strategies, and memory/skill architectures from Anvil, Max, and the multi-agent gist — with a practical assessment of which apply to a no-local-IDE personal assistant setup.
- **Links:** _To be populated on completion._
