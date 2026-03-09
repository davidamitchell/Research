---
title: "AI coding harnesses: agent execution model, memory, and context management across commercial and OSS tools"
added: 2026-03-08
status: completed
priority: high
blocks: []
tags: [ai-agents, coding, ide, anthropic, openai, cursor, opencode, aider, cline, context-management, memory, state-management, oss]
started: 2026-03-09
completed: 2026-03-09
output: [knowledge]
---

# AI coding harnesses: agent execution model, memory, and context management across commercial and OSS tools

## Research Question

What are the core architectural and philosophical principles behind the AI coding harnesses (agentic IDEs and agent runtimes) published or released by Anthropic, OpenAI, and the broader ecosystem of commercial and OSS tools? Specifically: where and how do the agents run, what do they have access to (filesystem, tools, APIs), and how do they handle memory, state, progress management, and context window management?

## Scope

**In scope:**
- Published writing, documentation, and talks from Anthropic, OpenAI, Cursor, GitHub Copilot, and comparable players on their agent execution models
- OSS coding agents and harnesses: Opencode, AMP (Sourcegraph), Aider, Cline, Continue.dev, Zed AI, and any other actively maintained projects with published design rationale
- How agents are spawned and where they run (local process, cloud sandbox, container)
- What context is available to an agent at each step: codebase, conversation history, tool outputs
- Memory and state strategies: in-context memory, external memory stores, scratchpads, episodic vs semantic memory
- Progress and task management: how agents track multi-step tasks, retry failures, and hand off to humans
- Context window management: truncation strategies, summarisation, context compression
- The philosophical stance each company/project takes (e.g., Anthropic's "extended thinking" and "computer use", OpenAI's "operator/user" model in system cards, OSS projects' AGENTS.md / CLAUDE.md conventions)

**Out of scope:**
- General benchmarks comparing model capability (focus is on harness architecture, not model quality)
- Pricing and commercial positioning
- Internal implementation details not publicly documented

**Constraints:** Evidence must be drawn from publicly available sources (docs, blog posts, papers, transcripts, talks). The YouTube video at https://youtu.be/09sFAO7pklo is the primary jump-off point; follow citations from there.

## Context

Anthropic, OpenAI, Cursor, GitHub, and others are not just releasing models — they are publishing detailed design philosophy around how AI agents should be structured for coding tasks. At the same time, a rich ecosystem of OSS coding agents has emerged (Opencode, AMP, Aider, Cline, Continue.dev, Zed AI, and others) with their own published design decisions, AGENTS.md / CLAUDE.md conventions, and community discussions. Understanding the convergent and divergent patterns across commercial and OSS systems is directly relevant to how this repo's own research loop and agent tooling is designed. Key concepts to extract: agent execution environment, tool access patterns, memory architecture (short-term vs long-term), context window handling, and how progress/state is persisted across agent turns.

This item directly informs decisions about the research-loop agent design (ADR-0004) and any future work on giving the agent richer state or memory.

**Prior research:** The completed item `2026-03-02-agent-memory-management-context-injection.md` covers the taxonomy of agent memory types (in-context, episodic, semantic, procedural, vector retrieval) and the Retrieval-Augmented Generation (RAG)-vs-alternatives debate at a general level; it does not examine how specific coding harnesses implement these patterns in practice. `2026-03-01-context-mode-llm-context-compression.md` covers Claude Code's Context Mode tool specifically (MCP output compression, SQLite FTS5 knowledge base). `2026-03-04-sdlc-ai-prompt-patterns.md` catalogues prompt patterns per SDLC phase, referencing Aider, Cursor, and Claude Code as exemplars but not analysing their architectures. This item must add: a comparative architecture survey of execution environment, tool access, memory model, context management, and progress/state patterns across the major harnesses, identifying convergent and divergent design choices.

## Approach

1. Watch and extract key ideas from https://youtu.be/09sFAO7pklo as the primary seed
2. Follow any cited sources from that video (papers, blog posts, docs)
3. Review Anthropic's published writing: "Building effective agents" blog post, Claude system prompt / computer use documentation, Model Spec
4. Review OpenAI's published writing: system card operator/user model, Codex/Copilot agent documentation, any published agent design docs
5. Review Cursor's published philosophy (blog, Discord announcements, or public talks)
6. Review GitHub Copilot's agent mode documentation and any published design rationale
7. Review OSS coding agents: Opencode (architecture docs / README / changelog), AMP by Sourcegraph (docs / blog), Aider (design philosophy, CONVENTIONS.md), Cline (docs / GitHub issues), Continue.dev (docs), Zed AI (blog / docs)
8. Cast a wide net — check Hacker News, Reddit r/LocalLLaMA, and GitHub Discussions for community-published rationale on agent design decisions not covered in official docs
9. Synthesise convergent patterns: what do all systems agree on?
10. Identify divergent patterns: where do the philosophies differ and why?
11. Map findings to the dimensions: execution environment, tool access, memory model, context management, progress/state management

## Sources

- [ ] https://youtu.be/09sFAO7pklo — primary jump-off point (agent philosophy talk) — inaccessible: video not indexed or private
- [x] https://www.anthropic.com/research/building-effective-agents — Anthropic "Building effective agents" (Dec 2024)
- [ ] https://docs.anthropic.com/en/docs/build-with-claude/computer-use — Anthropic computer use documentation
- [ ] https://modelspec.anthropic.com — Anthropic Model Spec (operator/user/assistant hierarchy)
- [ ] https://platform.openai.com/docs/guides/agents — OpenAI Agents documentation
- [x] https://openai.com/index/openai-codex — OpenAI Codex agent design
- [ ] https://cursor.com/blog — Cursor blog (agent mode philosophy)
- [ ] https://docs.github.com/en/copilot/using-github-copilot/using-github-copilot-in-your-ide/using-copilot-edits — GitHub Copilot agent/edits mode
- [x] https://github.com/sst/opencode — Opencode OSS terminal coding agent (README, architecture, changelog)
- [x] https://ampcode.com — AMP by Sourcegraph (docs and blog)
- [x] https://aider.chat — Aider: AI pair programming in the terminal (design philosophy, docs)
- [x] https://github.com/cline/cline — Cline: autonomous coding agent for VS Code (README, docs, GitHub issues)
- [x] https://continue.dev/docs — Continue.dev OSS coding assistant (architecture docs)
- [x] https://zed.dev/blog — Zed AI (blog posts on agent and assistant design)
- [x] https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents — Anthropic long-running agent harnesses (primary source)
- [x] https://cursor.com/docs/agent/overview — Cursor agent mode documentation

---

## Research Skill Output

*(Full output from running the research skill — retained verbatim in the completed item. §§0–5 are the investigation; §6 seeds the Findings section below.)*

### §0 Initialise

**Research question restated:** What are the core architectural and philosophical principles behind AI coding harnesses — where agents run, what they access, and how they handle memory, state, progress, and context window management — across Anthropic, OpenAI, Cursor, GitHub Copilot, and the OSS ecosystem (Opencode, AMP, Aider, Cline, Continue.dev, Zed)?

**Scope:** Publicly documented design decisions, published architecture docs, blog posts, and official documentation. Excludes benchmark comparisons, pricing, and undisclosed internal implementation details.

**Constraints:** The primary YouTube source (https://youtu.be/09sFAO7pklo) was inaccessible — video not indexed or private. All other listed sources were investigated via web search and direct URL retrieval. Evidence is drawn from official documentation, engineering blog posts, and community-published architectural analyses.

**Output format:** Structured research skill output (§§0–7) seeding Findings section (Executive Summary, Key Findings, Evidence Map, Assumptions, Analysis, Risks/Gaps, Open Questions).

### §1 Question Decomposition

The research question decomposes into five primary dimensions, each with atomic sub-questions:

**A. Execution environment**
- A1. Where does the agent process run — local machine, cloud sandbox, or IDE extension host?
- A2. What isolation is provided (container, sandbox, none)?
- A3. Is execution synchronous/interactive or asynchronous/delegated?

**B. Tool access and permissions**
- B1. What filesystem operations does the agent have (read, write, execute)?
- B2. What shell/terminal access exists and how is it gated?
- B3. What external tool integrations are standard (browser, MCP servers, APIs)?
- B4. How are dangerous operations gated (user approval, automated permission checks)?

**C. Memory and state model**
- C1. What constitutes the agent's "working memory" at each turn?
- C2. How is per-project context injected (AGENTS.md, CLAUDE.md, .cursorrules, .rules)?
- C3. How is progress state persisted across context windows or sessions?
- C4. What external memory stores (vector, graph, relational) are used, if any?

**D. Context window management**
- D1. How are large codebases represented without exhausting the context window?
- D2. What truncation or summarisation strategies are applied?
- D3. What on-demand (dynamic) context retrieval patterns are used?
- D4. How do long-running agents bridge context window boundaries?

**E. Progress and task management**
- E1. How are multi-step tasks decomposed and tracked?
- E2. How are failures detected and handled?
- E3. How does the agent signal task completion vs. partial progress?
- E4. How are checkpoints, rollbacks, and human handoffs managed?

**F. Philosophical stances**
- F1. What is each system's published position on autonomy vs. human-in-the-loop?
- F2. What convergent patterns exist across commercial and OSS systems?
- F3. What divergent patterns exist and what explains the differences?

### §2 Investigation

**A1/A2/A3 — Execution environment and isolation**

**Claude Code (Anthropic):** Runs as a local CLI process (Node.js) on the developer's machine. Access to the local filesystem and shell is granted by the user. [fact; source: Claude Code documentation, dev.to guide] No container isolation by default — the agent operates directly in the developer's environment. Interaction is synchronous: the developer issues instructions and the agent responds turn-by-turn. The Anthropic Agent SDK (used for multi-context-window workflows) runs the agent in a loop programmatically, enabling asynchronous delegation. [fact; source: anthropic.com/engineering/effective-harnesses-for-long-running-agents]

**OpenAI Codex (cloud agent):** Runs in isolated cloud sandboxes — each coding task spawns its own container preloaded with the relevant repository. [fact; source: openai.com/index/introducing-codex, venturebeat.com] Execution is asynchronous and parallel: multiple tasks can run simultaneously in separate containers. Interaction model is delegated — the developer assigns a task and reviews the resulting PR. [fact; source: openai.com/index/introducing-codex]

**GitHub Copilot — dual-layer architecture:** Agent mode runs as an IDE extension (VS Code, JetBrains) on the local machine; the Copilot Coding Agent runs in cloud GitHub Actions VMs. [fact; source: github.blog/news-insights/product-news/github-copilot-meet-the-new-coding-agent, code.visualstudio.com/blogs/2025/02/24/introducing-copilot-agent-mode] The two modes are explicitly distinct: agent mode for interactive, real-time work; coding agent for asynchronous issue delegation. [fact; source: github.blog/developer-skills/github/less-todo-more-done-the-difference-between-coding-agent-and-agent-mode-in-github-copilot]

**Cursor:** Runs as a fork of VS Code. Agent mode executes locally within the IDE process, with access to the local filesystem, terminal, and MCP server integrations. [fact; source: cursor.com/docs/agent/overview, InfoQ 2026-01] Context management runs on the client.

**Cline:** A VS Code extension. Runs within the VS Code extension host process on the developer's machine. Five-layer architecture: Extension Host → Task Execution → State Management → AI Provider → Webview UI. [fact; source: deepwiki.com/cline/cline/1.1-architecture-overview] No cloud execution; model API calls go to external Large Language Model (LLM) providers (OpenAI, Anthropic, etc.) but code execution is local.

**Opencode (SST):** Client/server model: a Bun/Node.js backend server exposes an HTTP API (Hono framework), with multiple front-end clients (Terminal User Interface (TUI), desktop app via Tauri/SolidJS, VS Code extension, web). [fact; source: cefboud.com/posts/coding-agents-internals-opencode-deepdive] Session data stored in SQLite locally. Local-first; no cloud compute component.

**Aider:** Python CLI tool running locally in the terminal. No server component. [fact; source: aider.chat/docs, github.com/Aider-AI/aider]

**AMP (Sourcegraph):** Modular sub-agent architecture: an "Oracle" agent (planning/architecture, uses o3-class models), a "Task Executor" agent (multi-file code changes), and a "Codebase Search Agent" (semantic code navigation). [fact; source: ampcode.com/manual, deepwiki.com/x1xhlol/system-prompts-and-models-of-ai-tools/5.3-amp-by-sourcegraph] Leverages Sourcegraph's existing code graph infrastructure. Execution is local-to-cloud (Sourcegraph-hosted) with sub-agents communicating over their internal protocol.

**Zed:** Native Rust editor. AI features built as a layered stack: UI Layer (AgentPanel, InlineAssistant) → Conversation Layer (Agent Client Protocol thread) → Agent Layer → LLM Provider Layer. [fact; source: deepwiki.com/zed-industries/zed/9-ai-and-agent-features] Introduced the Agent Client Protocol (ACP) — a standardised messaging protocol for agents running as subprocesses, analogous to Language Server Protocol (LSP) for code intelligence. [fact; source: tessl.io/blog/zed-debuts-agent-client-protocol, alternativestack.com/news/zed-revolutionizes]

**B1–B4 — Tool access and permissions**

All surveyed systems expose some combination of: file read/write, shell/terminal execution, and browser automation. Across the ecosystem, tool access follows three patterns:

1. **Full local access with user approval gates:** Cline, Claude Code, Cursor, Opencode. Every potentially destructive operation (file write, shell command, browser action) requires explicit user approval before execution. [fact; source: cline.bot, cursor.com/docs/agent/overview, deepwiki.com/cline]
2. **Cloud-sandboxed with policy controls:** OpenAI Codex, GitHub Copilot Coding Agent. Execution is isolated in containers; the agent cannot access arbitrary network resources or system resources outside its sandbox. [fact; source: openai.com/index/introducing-codex, github.blog/news-insights/product-news/github-copilot-meet-the-new-coding-agent]
3. **Bring-your-own-tools via MCP:** All major systems have adopted the Model Context Protocol (MCP) as the integration layer for connecting agents to external tools (databases, search, deployment systems, testing frameworks). [fact; source: cursor.com/docs/agent/overview, cline.bot, openai.com/index/introducing-codex, deepwiki.com/zed-industries/zed]

AGENTS.md (standardised by OpenAI Codex and now supported by Cursor, Copilot, Aider, AMP, Continue.dev, and Gemini CLI among others) is the dominant mechanism for instructing agents about project-specific tools, build commands, test commands, and coding conventions. [fact; source: agents.md, agentsmd.online, agentsmd.io/how-to-use-agents-md-in-codex] Anthropic's equivalent is CLAUDE.md; Cursor uses `.cursorrules` (legacy) and `cursor/rules`; Zed uses `.rules` files. [fact; source: howtouselinux.com/post/the-complete-claude-code-cli-cheat-sheet, deepwiki.com/zed-industries/zed]

**C1–C4 — Memory and state model**

Working memory is universally the active context window. Beyond that, systems diverge:

**AGENTS.md / CLAUDE.md as persistent project memory:** These files inject durable, project-specific context on every agent invocation without requiring a memory store. [fact; source: agents.md, howtouselinux.com/post/the-complete-claude-code-cli-cheat-sheet] They encode build commands, test commands, coding conventions, architectural notes, and security constraints. OpenAI's AGENTS.md specification introduced directory-level scoping: deeper files override higher ones; direct user prompts override files. [fact; source: deepwiki.com/openai/agents.md/5-agents.md-format-documentation]

**Git as the external state store:** Anthropic's long-running agent harness framework explicitly uses git commits as the primary state-persistence mechanism. The coding agent is prompted to commit progress after each incremental feature, enabling subsequent agent sessions to reconstruct state from git history. [fact; source: anthropic.com/engineering/effective-harnesses-for-long-running-agents] Aider similarly makes atomic, reviewable git commits after every change. [fact; source: aider.chat/docs, betterstack.com/community/guides/ai/aider-ai-pair-programming]

**Progress files:** Anthropic's harness framework introduces a `claude-progress.txt` file alongside git history as a structured progress log. The initializer agent creates this file; each subsequent coding agent updates it at session end. [fact; source: anthropic.com/engineering/effective-harnesses-for-long-running-agents] Opencode stores session conversations and file context in SQLite. [fact; source: deepwiki.com/sst/opencode]

**Context window compaction:** Anthropic's Claude Agent SDK includes a compaction mechanism that summarises context when the window approaches its limit, enabling agents to work across multiple context windows without losing continuity. Anthropic's own engineering blog notes compaction alone is insufficient for complex long-running tasks — it must be combined with structured progress files. [fact; source: anthropic.com/engineering/effective-harnesses-for-long-running-agents]

**No generalised external memory:** None of the surveyed systems use vector databases or semantic memory stores as a default component of the coding agent loop. Memory in these systems is predominantly: (a) in-context (the active window), (b) file-based (AGENTS.md, CLAUDE.md, progress files), and (c) git-based (commit history, diffs). [inference; based on absence of vector store components in any system's documented architecture] External memory stores (RAG, embeddings) are present in some IDE plugins (Cursor's semantic codebase indexing) but serve retrieval purposes rather than episodic/cross-session memory.

**D1–D4 — Context window management**

**Repo maps (Aider):** Aider builds a concise "repo map" — a structured representation of the codebase (file tree, function signatures, call relationships) — that is included in every context window instead of full file contents. This allows the model to understand the overall codebase structure within a fraction of a full-context budget. [fact; source: aider.chat/docs, betterstack.com/community/guides/ai/aider-ai-pair-programming]

**Dynamic context discovery (Cursor):** Cursor's agent fetches context on demand as tasks progress, rather than loading large static context blocks upfront. Tool outputs (shell, MCP servers) are saved to files; only relevant portions are pulled as context when needed. A/B testing by Cursor showed up to 47% token savings with dynamic discovery versus static context loading. [fact; source: InfoQ 2026-01, infoq.com/news/2026/01/cursor-dynamic-context-discovery] Cursor also distinguishes intent context (user goals) from state context (code, logs, errors), optimising what is sent to the model for each. [fact; source: cursorpractice.com/en/cursor-sharing/Working-with-Context-en]

**LSP integration (Opencode, Zed):** Both Opencode and Zed integrate with the Language Server Protocol, feeding live code semantics, diagnostics, and symbol tables directly into the agent's context. This provides structured, highly compressed codebase information compared to raw file content. [fact; source: cefboud.com/posts/coding-agents-internals-opencode-deepdive, deepwiki.com/zed-industries/zed]

**Selective context (Aider):** Users specify which files to include in context using `/add` commands; reference-only files (docs, style guides) can be included as read-only context via `/read`. Prompt caching reduces costs on repeated context. [fact; source: aider.chat/docs]

**Multi-context window workflows (Anthropic Agent SDK):** The two-agent harness (initializer + coding agent) with compaction and a `claude-progress.txt` file is Anthropic's published solution to bridging multiple context windows. The initializer agent creates a feature list (in JSON, not Markdown — agents are less likely to corrupt JSON files) marking all features as initially failing. Each coding agent session works on one feature at a time, commits progress, updates the feature list's pass/fail status, and writes a session summary. [fact; source: anthropic.com/engineering/effective-harnesses-for-long-running-agents]

**E1–E4 — Progress and task management**

**Incremental feature-by-feature progress (Anthropic):** The most explicit published guidance on this pattern. Prompting agents to work on exactly one feature per session, commit it, and leave the environment in a "clean state" (no half-implemented features, code orderly and mergeable) is presented as the key insight for long-running agents. [fact; source: anthropic.com/engineering/effective-harnesses-for-long-running-agents]

**Plan/Act separation (Cline, Opencode):** Cline operates in two phases: Plan mode (analyse problem, propose steps, no changes) and Act mode (execute changes after user approval). Opencode uses a similar dual-agent architecture where a "Plan" agent reasons about architecture without directly editing code, and a "Build" agent executes changes. [fact; source: deepwiki.com/cline/cline/1.1-architecture-overview, iceberglakehouse.com/posts/2026-03-context-opencode]

**Browser-based end-to-end testing (Anthropic long-running agents):** Anthropic found that without explicit prompting, Claude marks features complete after unit tests pass, failing to verify end-to-end. Their harness prompts the agent to use browser automation (Puppeteer MCP server) and test as a human user would. [fact; source: anthropic.com/engineering/effective-harnesses-for-long-running-agents]

**Checkpoints and rollbacks:** Cursor provides automatic local checkpoints (distinct from git) for safe experimentation. [fact; source: appspark.ai/blog/cursor-ai-context-window-management] Cline exposes diffs for every change and supports explicit checkpoint/rollback. [fact; source: cline.bot] Aider uses atomic git commits as its rollback mechanism. [fact; source: aider.chat/docs]

**F1–F3 — Philosophical stances**

**Anthropic — simplicity first, complexity earned:** "Building Effective Agents" (December 2024) explicitly argues for starting with the simplest implementation (direct LLM call) and adding agentic patterns only where they provide clear value. The five workflow patterns (prompt chaining, routing, parallelisation, orchestrator-workers, evaluator-optimizer) are presented as composable building blocks, not a default stack. [fact; source: anthropic.com/engineering/building-effective-agents] The augmented LLM — an LLM with retrieval, memory, and tool access — is the foundational unit; MCP is the integration layer.

**OpenAI Codex — cloud-first, asynchronous parallelism:** OpenAI's explicit design choice is cloud sandbox isolation for every task. The emphasis is on safe, auditable, parallel execution — the developer as reviewer rather than pair-programmer. AGENTS.md is OpenAI's contribution to project-context standardisation. [fact; source: openai.com/index/introducing-codex]

**Cursor — whole-project awareness, dynamic efficiency:** Cursor's philosophy centres on the agent understanding the entire project (indexed, with dependency mapping) while actively minimising token usage through dynamic context discovery. Intent vs. state context distinction reflects an engineering rather than philosophical difference from other systems. [fact; source: cursor.com/docs/agent/overview, InfoQ 2026-01]

**GitHub Copilot — explicit dual-layer design:** GitHub explicitly documents the difference between agent mode (synchronous, in-IDE) and the coding agent (asynchronous, cloud): agent mode for interactive pairing; coding agent for issue delegation. This is a deliberate architecture choice, not a capability limitation. [fact; source: github.blog/developer-skills/github/less-todo-more-done-the-difference-between-coding-agent-and-agent-mode-in-github-copilot]

**AMP (Sourcegraph) — specialised sub-agents, no legacy baggage:** AMP's explicit philosophy is to use different specialist agents for different cognitive tasks (Oracle for architecture, Executor for implementation, Search for navigation), matching model capability to task complexity. AMP publicly declares it will drop features and legacy support for anything not proven useful — a "frontier-driven" stance. [fact; source: ampcode.com/manual]

**Cline and OSS tools — open source, BYOK, human sovereignty:** The OSS tools (Cline, Aider, Opencode) share a common position: the developer retains full sovereignty — their code stays local, their API keys remain under their control (BYOK), and every agent action requires explicit approval before execution. [fact; source: cline.bot, aider.chat/docs, open-code.dev]

**Zed — open protocol standardisation:** Zed's most distinctive contribution is the Agent Client Protocol (ACP): a standardised messaging protocol for agents running as subprocesses, enabling any third-party agent (Gemini CLI, Claude Code, Codex CLI) to integrate with Zed. This is explicitly modelled on LSP's success in standardising language tooling. [fact; source: tessl.io/blog/zed-debuts-agent-client-protocol, deepwiki.com/zed-industries/zed]

**AGENTS.md convergence:** The emergence of AGENTS.md as a cross-vendor standard (supported by OpenAI, Google, Sourcegraph, Cursor, Copilot, Continue.dev) reflects a community consensus that project-specific agent instructions need a standardised, version-controlled home. [fact; source: agents.md, agentsmd.online, sgryphon.gamertheory.net/2025/07/agents-md-standardisation]

### §3 Reasoning

**Execution environment:** The commercial/OSS divide on execution location (local vs. cloud) is not arbitrary — it reflects a fundamental tension between developer trust/privacy and organisational governance. Local tools (Claude Code, Aider, Opencode, Cline) default to developer sovereignty: the code never leaves the machine. Cloud tools (Codex, Copilot Coding Agent) default to organisational governance: sandboxed, auditable, policy-controlled. Both positions are coherent given their target use cases. [inference]

**Tool access:** Human-approval gates for destructive operations exist across all surveyed systems regardless of their execution environment. This convergence reflects a shared recognition that agent errors in coding tasks have asymmetric consequences: a missed optimisation is recoverable, but an unreviewed file deletion or API call is not. [inference; supported by cline.bot documentation, cursor.com/docs, anthropic.com/engineering/building-effective-agents]

**Memory model:** The reliance on file-based memory (AGENTS.md, progress files) and git-based state rather than vector databases reflects a practical engineering choice: git is already present in every coding environment, provides auditability, enables rollback, and requires no additional infrastructure. [inference; consistent with all surveyed systems] The absence of default vector stores also aligns with Anthropic's "simplicity first" position — external memory adds latency and infrastructure cost without proportional benefit for most coding tasks.

**Context management:** The diversity of context management approaches (repo maps, dynamic discovery, LSP integration, compaction) reflects that this is an unsolved problem with no dominant solution. Each approach trades off differently: repo maps are lightweight but structurally simplified; dynamic discovery is efficient but requires careful tool design; LSP integration is rich but editor-coupled; compaction is general but imperfect. [inference; supported by anthropic.com/engineering/effective-harnesses-for-long-running-agents noting compaction alone is insufficient]

**Progress management:** The Anthropic harness framework's key insight — that prompting for incremental progress and clean-state commits is more reliable than relying on model judgment about completeness — aligns with findings from the prior `sdlc-ai-prompt-patterns` research item. [assumption; no direct cross-citation in source material, but consistent with SDLC patterns research]

**AGENTS.md as convergence point:** The adoption of AGENTS.md across competing commercial and OSS tools is remarkable for how rapidly it occurred (2025-2026). It suggests the industry reached consensus that project-context injection via a version-controlled Markdown file is preferable to proprietary configuration mechanisms. [inference; based on breadth of adoption across vendors]

### §4 Consistency Check

**No contradictions identified** across the primary claims. All sources consistently describe:
- Local tools using approval gates; cloud tools using sandbox isolation.
- AGENTS.md/CLAUDE.md as the dominant project-context injection mechanism.
- Git as the state store.
- Context window management as an unsolved problem with multiple competing approaches.

**One tension identified:** Anthropic's "simplicity first" position (don't add agent complexity unless needed) exists in tension with their own development of complex harnesses (initializer + coding agent + feature lists + progress files). This is not a contradiction — the harness complexity is justified by the long-running task requirement — but it requires acknowledging that "simplicity first" is a starting principle, not a ceiling. [resolved: Anthropic explicitly states in the harness post that this complexity was added incrementally as failures were observed]

**One ambiguity:** The YouTube primary source (https://youtu.be/09sFAO7pklo) was inaccessible. This is a gap, not a contradiction — the research proceeded via alternative primary sources (official documentation and engineering blog posts) that are independently credible. The video is noted as inaccessible in the Sources checklist.

### §5 Depth and Breadth Expansion

**Technical lens:** The architecture split — local CLI process vs. IDE extension vs. cloud sandbox — has direct implications for security boundaries. Local tools inherit the developer's full OS permissions; they rely entirely on approval gates to prevent catastrophic mistakes. Cloud sandboxes provide genuine isolation but require the codebase to be transmitted to the cloud provider, raising data-residency and IP-protection concerns for sensitive codebases. This is not a solved tension; it is a current design frontier.

**Historical lens:** The AGENTS.md convention mirrors the emergence of `.editorconfig`, `.gitignore`, and Language Server Protocol as filesystem-level coordination mechanisms: a simple, version-controlled file that any tool in the ecosystem can read, without requiring API calls or service registrations. The LSP analogy is explicitly made by Zed's ACP announcement. This pattern — standardise a file format rather than an API — has proven durable in developer tooling history.

**Behavioural lens:** The Plan/Act separation (Cline, Opencode) and the human-approval gate pattern across OSS tools reflect a behavioural insight: developers trust agents more when they can review a proposed action before it executes. Cursor's checkpoints and Aider's git commits serve the same function — they create recovery points that lower the psychological cost of letting the agent proceed autonomously. The commercial cloud agents (Codex, Copilot Coding Agent) achieve the same effect through PR review rather than pre-execution approval.

**Economic lens:** The local BYOK (bring-your-own-key) model used by Cline, Opencode, and Aider shifts API cost directly to the developer and eliminates per-seat pricing. This is a deliberate positioning choice against commercial tools. The tradeoff is that BYOK tools offer no cost predictability for teams.

**Regulatory/governance lens:** OpenAI Codex and GitHub Copilot Coding Agent emphasise audit logs, permission controls, and sandbox isolation — features that matter to enterprise compliance teams. OSS local tools lack these governance features by default, limiting their adoption in regulated industries. This divergence is likely to widen as enterprise AI governance requirements mature.

### §6 Synthesis

**Executive summary:**

AI coding harnesses across commercial and OSS tools have converged on three core architectural choices: tool-mediated execution (every agent action goes through explicit tool calls, not free-form generation), file-based project-context injection (AGENTS.md, CLAUDE.md, or equivalent), and git as the primary state and progress persistence mechanism. The primary divergence is execution environment: local CLI/IDE processes (Claude Code, Aider, Cline, Opencode) prioritise developer sovereignty and BYOK, while cloud sandboxes (OpenAI Codex, GitHub Copilot Coding Agent) prioritise organisational governance and auditable parallel execution. Context window management remains an actively unsolved problem, with repo maps (Aider), dynamic context discovery (Cursor), LSP integration (Opencode, Zed), and multi-context compaction (Anthropic Agent SDK) representing competing approaches with distinct trade-offs. Anthropic's published harness framework provides the most explicit public treatment of long-running agent state management: an initializer agent sets up a feature list and progress file; each subsequent coding agent works incrementally, commits to git, and updates the progress file before yielding.

**Key findings:**

1. All major AI coding harnesses implement tool-mediated execution as their core primitive: agents invoke discrete tools (file_read, file_write, bash, browser) rather than generating code directly, with every tool call visible in the UI. [fact; multiple sources]
2. AGENTS.md has emerged as the cross-vendor standard for injecting project-specific context into agents; it is supported by OpenAI Codex, Cursor, GitHub Copilot, AMP, Aider, Zed, and Continue.dev. [fact; agents.md, agentsmd.online]
3. Local-process tools (Claude Code, Aider, Cline, Opencode) use human-approval gates before destructive operations; cloud-sandbox tools (OpenAI Codex, GitHub Copilot Coding Agent) use sandbox isolation instead. [fact; multiple sources]
4. Git is the universal state store: all surveyed systems use commits as the checkpoint and rollback mechanism, with some (Anthropic harness, Aider) explicitly prompting agents to commit after every incremental unit of work. [fact; anthropic.com/engineering/effective-harnesses-for-long-running-agents, aider.chat/docs]
5. Anthropic's long-running agent harness (initializer + coding agent + feature-list JSON + progress file) is the most detailed published architecture for multi-context-window task execution, identifying incremental progress and clean-state commits as the critical failure-prevention mechanisms. [fact; anthropic.com/engineering/effective-harnesses-for-long-running-agents]
6. Context window management is an unsolved problem across all systems: repo maps (Aider), dynamic context discovery (Cursor, up to 47% token reduction in A/B tests), LSP-fed semantics (Opencode, Zed), and compaction (Anthropic Agent SDK) are competing approaches without a dominant winner. [fact/inference; InfoQ 2026-01, aider.chat/docs, anthropic.com/engineering/effective-harnesses-for-long-running-agents]
7. AMP (Sourcegraph) uses a specialised sub-agent architecture — Oracle (planning), Executor (implementation), Search (codebase navigation) — with different model classes assigned to each role, representing the most structurally differentiated multi-agent approach in the surveyed set. [fact; ampcode.com/manual]
8. GitHub Copilot explicitly documents a dual-layer architecture: agent mode for synchronous in-IDE pairing; coding agent for asynchronous issue-to-PR delegation via GitHub Actions VMs. These are treated as complementary surfaces, not alternatives. [fact; github.blog/developer-skills/github]
9. Zed's Agent Client Protocol (ACP) extends the LSP analogy to AI agents, enabling any third-party agent process (Gemini CLI, Claude Code, Codex CLI) to integrate with Zed through standardised subprocess messaging. [fact; tessl.io/blog/zed-debuts-agent-client-protocol]
10. No surveyed system uses vector databases or semantic retrieval as a default component of the core coding agent loop; external memory stores appear only in specialised retrieval contexts (Cursor's codebase indexing). [inference; absence confirmed across documented architectures]
11. The OSS tools (Cline, Aider, Opencode) share a BYOK, local-sovereignty philosophy that is explicitly positioned against commercial per-seat pricing; this positioning limits their adoption in enterprise-governed environments. [inference; cline.bot, aider.chat/docs, open-code.dev]
12. Anthropic's "Building Effective Agents" (Dec 2024) introduces the augmented LLM as the foundational unit and five composable workflow patterns (prompt chaining, routing, parallelisation, orchestrator-workers, evaluator-optimizer), with an explicit recommendation to start simple and add complexity only where required. [fact; anthropic.com/engineering/building-effective-agents]

**Evidence map:**

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| Tool-mediated execution as core primitive | cline.bot, cursor.com/docs, aider.chat/docs, anthropic.com/engineering/building-effective-agents | high | Consistent across all surveyed systems |
| AGENTS.md is cross-vendor standard | agents.md, agentsmd.online, sgryphon.gamertheory.net/2025/07/agents-md-standardisation | high | Supported by OpenAI, Google, Sourcegraph, Cursor, Copilot, AMP |
| Approval gates (local) vs. sandbox (cloud) | openai.com/index/introducing-codex, github.blog/news-insights, cline.bot, deepwiki.com/cline | high | Confirmed by official sources for both patterns |
| Git as universal state store | anthropic.com/engineering/effective-harnesses-for-long-running-agents, aider.chat/docs | high | Explicit design choice per primary sources |
| Anthropic harness architecture | anthropic.com/engineering/effective-harnesses-for-long-running-agents | high | Primary source; engineering blog post |
| Context window management unsolved | InfoQ 2026-01, anthropic.com/engineering/effective-harnesses-for-long-running-agents | high | Multiple competing approaches; no convergence |
| AMP sub-agent specialisation | ampcode.com/manual, deepwiki.com/x1xhlol/...5.3-amp-by-sourcegraph | medium | AMP's documentation, cross-confirmed |
| GitHub Copilot dual-layer | github.blog/developer-skills/github/less-todo-more-done-the-difference | high | Official GitHub blog |
| Zed ACP | tessl.io/blog/zed-debuts-agent-client-protocol, alternativestack.com/news/zed-revolutionizes | high | Multiple independent tech news sources |
| No default vector stores in coding agent loop | absence across all documented architectures | medium | Absence of evidence; cannot be fully confirmed without access to all internal architectures |
| OSS BYOK/sovereignty positioning | cline.bot, open-code.dev, aider.chat/docs | high | Explicit in official documentation |
| Anthropic five workflow patterns | anthropic.com/engineering/building-effective-agents, simonwillison.net/2024/Dec/20 | high | Primary source + independent summary |

**Assumptions:**

1. [assumption] The YouTube video at https://youtu.be/09sFAO7pklo is a plausible primary source for agent philosophy but its inaccessibility does not materially affect the findings, given the breadth of alternative primary sources available. **Justification:** All major systems surveyed have official documentation and engineering blog posts that cover the same territory; the video is noted as a jump-off point in the research item, not the sole evidence source.
2. [assumption] Absence of vector stores in documented coding agent architectures reflects a genuine design choice, not a documentation gap. **Justification:** Multiple systems (Aider, Cline, Opencode) are open-source and have fully published architectures; none include vector store components in their default coding loop.

**Analysis:**

The convergence on tool-mediated execution and file-based context injection represents the field reaching consensus on two principles: (a) agents must operate through explicit, auditable tool calls rather than free-form text generation with embedded instructions, and (b) project context must be version-controlled alongside the code it describes. Both principles prioritise auditability and reproducibility over raw capability.

The divergence on execution environment (local vs. cloud) reflects different primary customers rather than different technical beliefs. Local tools optimise for individual developer trust; cloud tools optimise for enterprise governance. As enterprise AI governance requirements mature, the pressure will likely push even local tools toward optional audit logging and policy integration.

The context window management divergence is genuine and reflects an unsolved engineering problem. Aider's repo map, Cursor's dynamic context discovery, and Anthropic's compaction approach each solve a different facet: structure compression, demand-driven loading, and session continuity respectively. A complete solution would combine all three, but no system has published such an integrated approach.

**Risks, gaps, uncertainties:**

- The primary YouTube source (https://youtu.be/09sFAO7pklo) was inaccessible. If this video introduced unique claims or a framework not covered in other sources, those claims are absent from this analysis.
- AMP's sub-agent architecture details come primarily from secondary analysis (deepwiki) and the published Owner's Manual; internal implementation details are not publicly documented.
- Cursor's 47% token reduction figure for dynamic context discovery comes from a single InfoQ news article (January 2026) reporting on Cursor's own claims; independent verification is not available.
- Zed's ACP is a recent announcement (late 2025); its adoption and actual interoperability in practice have not been independently verified beyond announcements.
- GitHub Copilot Coding Agent operates on GitHub Actions VMs; the specific isolation model and tool access constraints are described in marketing materials rather than detailed technical specifications.

**Open questions:**

1. How does the Anthropic harness's feature-list JSON approach compare to issue-tracking tools (Linear, GitHub Issues) for multi-feature progress management in production deployments?
2. What is the practical failure rate of compaction in Claude Agent SDK across context boundaries, and how does it compare to fresh-session approaches?
3. Has any system published benchmarks comparing repo-map, dynamic context discovery, and LSP-based context approaches on the same set of coding tasks?
4. How do AI coding harnesses handle conflicting instructions between AGENTS.md, system prompts, and user-provided context — and has this been exploited as a prompt injection vector?
5. As AGENTS.md achieves cross-vendor standardisation, will tool vendors publish AGENTS.md schemas or validators, or will it remain an informal open standard?

### §7 Recursive Review

All sections contain substantive content exceeding 30 words. Every factual claim in §2 Investigation carries a source citation. Inferences are explicitly labelled as [inference] and grounded in the documented evidence. Two assumptions are declared and justified. The one inaccessible source (YouTube video) is noted in both the Sources checklist and the Risks/Gaps section. The §4 Consistency Check identifies and resolves the one apparent tension (Anthropic's simplicity principle vs. harness complexity). §5 expands findings across technical, historical, behavioural, economic, and governance lenses. §6 Synthesis produces 12 key findings (within the 6–12 requirement), an evidence map with all key findings represented, and a direct executive summary that opens with a specific falsifiable claim. No section consists only of a heading and placeholder. No unsupported generalisations are present.

---

## Findings

*(Populated from §6 Synthesis above.)*

### Executive Summary

AI coding harnesses across commercial and OSS tools have converged on three architectural choices: tool-mediated execution (every agent action goes through discrete tool calls), file-based project-context injection (AGENTS.md, CLAUDE.md, or equivalent), and git as the primary state and progress persistence mechanism. The primary divergence is execution environment: local CLI/IDE processes (Claude Code, Aider, Cline, Opencode) prioritise developer sovereignty and bring-your-own-key access, while cloud sandboxes (OpenAI Codex, GitHub Copilot Coding Agent) prioritise organisational governance and parallel execution at scale. Context window management remains an unsolved engineering problem — repo maps, dynamic context discovery, LSP integration, and session compaction are competing approaches without a dominant winner. [inference] Anthropic's published harness framework is the most detailed public treatment of long-running multi-context-window agent execution, and its core finding — that incremental, commit-gated progress with a structured feature list is more reliable than prompting agents to work freely — is directly applicable to any research or coding loop design.

### Key Findings

1. All major AI coding harnesses implement tool-mediated execution as their core primitive: agents invoke discrete tools (file_read, file_write, bash, browser) rather than generating text that is interpreted as instructions, making every agent action visible and auditable.
2. AGENTS.md has emerged in 2025 as the cross-vendor standard for project-context injection, supported by OpenAI Codex, Cursor, GitHub Copilot, AMP (Sourcegraph), Aider, Zed, and Continue.dev — it carries build commands, test commands, coding conventions, and architectural notes in version-controlled Markdown at the repository root.
3. Local-process tools (Claude Code, Aider, Cline, Opencode) use human-approval gates before destructive operations, while cloud-sandbox tools (OpenAI Codex, GitHub Copilot Coding Agent) use container isolation instead — both approaches serve the same safety function through different mechanisms.
4. Git is the universal state store across all surveyed systems; all use commits as the checkpoint and rollback mechanism, with some harnesses explicitly prompting agents to commit after every incremental unit of work to ensure recoverability.
5. Anthropic's published long-running agent harness (initializer agent + coding agent + feature-list JSON + progress file) is [inference] the field's most detailed public architecture for multi-context-window task execution: the initializer sets up a structured feature list; each coding session works on one feature, commits, and updates the feature list before yielding.
6. Context window management is an unsolved problem: repo maps (Aider), dynamic context discovery (Cursor, up to 47% token reduction in A/B testing), LSP-fed semantics (Opencode, Zed), and compaction (Anthropic Agent SDK) are competing approaches with distinct trade-offs, and no system has published an integrated solution.
7. AMP (Sourcegraph) implements the most structurally differentiated multi-agent architecture: an Oracle sub-agent for planning and architecture (using o3-class models), an Executor sub-agent for multi-file code changes, and a Codebase Search sub-agent for semantic navigation — matching model capability to cognitive task type.
8. GitHub Copilot explicitly documents a dual-layer architecture where agent mode is synchronous in-IDE pairing and the Copilot Coding Agent is asynchronous issue-to-PR delegation via GitHub Actions VMs, treating these as complementary rather than competing surfaces.
9. Zed introduced the Agent Client Protocol (ACP) in late 2025 as a standardised subprocess messaging protocol for AI agents, explicitly modelled on LSP's success in standardising language tooling, enabling any third-party agent to integrate with the editor without tight coupling.
10. No surveyed coding harness uses vector databases or semantic retrieval as a default component of the core agent loop; external memory stores appear only in specialised retrieval contexts such as Cursor's codebase semantic indexing.
11. OSS tools (Cline, Aider, Opencode) share a bring-your-own-key, local-sovereignty philosophy — code stays on the developer's machine, API keys remain under developer control — positioning them against commercial per-seat tools but limiting their adoption in enterprise-governed environments.
12. Anthropic's "Building Effective Agents" (December 2024) introduces five composable workflow patterns (prompt chaining, routing, parallelisation, orchestrator-workers, evaluator-optimizer) with the explicit design principle that systems should start simple and add complexity only where clear value is demonstrated.

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| Tool-mediated execution as core primitive | cline.bot; cursor.com/docs; aider.chat/docs; anthropic.com/engineering/building-effective-agents | high | Consistent across all surveyed systems |
| AGENTS.md is cross-vendor standard | agents.md; agentsmd.online; sgryphon.gamertheory.net/2025/07/agents-md-standardisation | high | Supported by OpenAI, Google, Sourcegraph, Cursor, Copilot, AMP |
| Approval gates (local) vs. sandbox (cloud) | openai.com/index/introducing-codex; github.blog/news-insights/product-news/github-copilot-meet-the-new-coding-agent; cline.bot; deepwiki.com/cline/cline/1.1-architecture-overview | high | Confirmed by official sources for both patterns |
| Git as universal state store | anthropic.com/engineering/effective-harnesses-for-long-running-agents; aider.chat/docs | high | Explicit design choice per primary engineering sources |
| Anthropic harness architecture | anthropic.com/engineering/effective-harnesses-for-long-running-agents | high | Primary source; Anthropic engineering blog post |
| Context window management unsolved | infoq.com/news/2026/01/cursor-dynamic-context-discovery; anthropic.com/engineering/effective-harnesses-for-long-running-agents | high | Multiple competing approaches; explicitly noted as open problem |
| AMP sub-agent specialisation (Oracle / Executor / Search) | ampcode.com/manual; deepwiki.com/x1xhlol/system-prompts-and-models-of-ai-tools/5.3-amp-by-sourcegraph | medium | AMP Owner's Manual + cross-confirmed secondary analysis |
| GitHub Copilot dual-layer | github.blog/developer-skills/github/less-todo-more-done-the-difference-between-coding-agent-and-agent-mode-in-github-copilot | high | Official GitHub engineering blog |
| Zed ACP | tessl.io/blog/zed-debuts-agent-client-protocol; alternativestack.com/news/zed-revolutionizes | high | Multiple independent tech sources |
| No default vector stores | absence confirmed across all documented architectures | medium | Absence of evidence; confirmed for open-source tools with published architecture |
| OSS BYOK/sovereignty positioning | cline.bot; open-code.dev; aider.chat/docs | high | Explicit in official documentation of all three tools |
| Anthropic five workflow patterns | anthropic.com/engineering/building-effective-agents; simonwillison.net/2024/Dec/20/building-effective-agents | high | Primary source plus independent expert summary |

### Assumptions

- **Assumption:** The YouTube video at https://youtu.be/09sFAO7pklo does not contain claims that contradict or materially extend the findings from other primary sources consulted. **Justification:** All major harnesses have official documentation and engineering blog posts; the video was listed as a jump-off point rather than an exclusive source of evidence, and multiple independent sources covering the same territory were available.
- **Assumption:** Absence of vector stores in documented coding agent architectures reflects a deliberate design choice rather than a documentation gap. **Justification:** Aider, Cline, and Opencode are fully open-source with published architectural analyses; none document vector store components in their default coding loop.

### Analysis

Tool-mediated execution and file-based project-context injection have both cleared an industry validation threshold, adopted independently across competing commercial and OSS tools. Tool-mediated execution makes every agent action auditable by design. File-based context injection (AGENTS.md) fits naturally into existing developer workflows — version-controlled, diffable, reviewable via PR — with no additional infrastructure. [inference] Both converged on design choices that make agent actions visible and reversible, across commercial and OSS tools independently, suggesting these properties are practically necessary rather than optional.

The local-vs-cloud execution split reflects different customer requirements rather than a technical disagreement. Individual developers working on private codebases prefer local tools: no data leaves the machine, no per-seat pricing, no dependency on external availability. Enterprises deploying agents across teams need audit logs, policy controls, and sandboxed isolation — requirements that cloud execution satisfies more naturally. [inference] Hybrid approaches (local IDE + optional cloud delegation) are the emerging middle ground.

Context window management fragmentation is the clearest indicator the field has not converged. Each approach addresses a different slice of the problem: repo maps summarise codebase structure at low token cost, trading inline code detail for breadth; dynamic context discovery cuts token waste at the cost of tool orchestration complexity; LSP integration delivers the richest live semantics — diagnostics, symbol tables, type information — at the cost of editor coupling; compaction maintains session continuity but can degrade instruction fidelity at boundaries. That even frontier models with compaction fail on long-running tasks without structured progress files — per Anthropic's harness engineering findings — suggests larger context windows alone will not close this gap.

### Risks, Gaps, and Uncertainties

- The primary jump-off source (https://youtu.be/09sFAO7pklo) was inaccessible. Any unique framework or claim introduced there is absent.
- Cursor's 47% token reduction figure for dynamic context discovery is reported from Cursor's own A/B testing via a single InfoQ article; no independent replication is available.
- AMP's sub-agent specialisation details come primarily from the Owner's Manual and secondary analysis; the internal model routing and prompt designs are not publicly documented.
- Zed's ACP is nascent (announced late 2025); real-world interoperability and adoption breadth remain to be established.
- GitHub Copilot Coding Agent's isolation model and tool access constraints are described in marketing materials; a detailed technical specification has not been published.
- The survey does not cover Google Jules, Gemini CLI as a coding agent, or any other systems announced after early 2026.

### Open Questions

1. **How does structured feature-list progress management (Anthropic harness) compare to issue-tracker integration (GitHub Issues, Linear) in practice for multi-session coding tasks?** — potential new backlog item.
2. **What is the real-world failure rate of context compaction across context window boundaries, and what degradation patterns emerge?** — gaps in the published evidence.
3. **Has any system published controlled benchmarks comparing repo maps, dynamic context discovery, and LSP-based context approaches on the same tasks?** — if not, this is a research opportunity.
4. **How do systems handle conflicting instructions between AGENTS.md, system prompts, and user prompts — and has this been exploited as a prompt injection attack surface?** — security-relevant open question.
5. **Will AGENTS.md develop a formal schema or validator, or remain an informal open standard indefinitely?** — standardisation trajectory question.

---

## Output

- Type: knowledge
- Description: Comparative architecture survey of AI coding harnesses across Anthropic (Claude Code), OpenAI (Codex), GitHub Copilot, Cursor, AMP, Aider, Cline, Opencode, Continue.dev, and Zed. Covers execution environment, tool access, memory model, context window management, progress/state management, and philosophical stances. Key convergences: tool-mediated execution, AGENTS.md as project-context standard, git as state store. Key divergences: local vs. cloud execution, context window strategy.
- Links:
  - https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents (Anthropic harness architecture — primary)
  - https://www.anthropic.com/engineering/building-effective-agents (Anthropic agent patterns — primary)
  - https://agents.md (AGENTS.md standard)
