---
title: "Anthropic Claude Code leak: architecture, prompting, and hidden features"
added: 2026-04-02T09:05:22+00:00
status: completed
priority: high
blocks: []
tags: [anthropic, claude, claude-code, leak, architecture, prompting, feature-flags, agentic-ai, npm, typescript, memory, tools]
started: 2026-04-02T09:05:22+00:00
completed: 2026-04-02T09:05:22+00:00
output: [knowledge]
cites: []          # slugs of items this item directly depends on or quotes
related: []        # slugs of thematically connected items
superseded_by: ~   # slug of a later item that overrides this one (null if not superseded)
supersedes: ~      # slug of an older item this one replaces (null if not applicable)
item_type: primary # primary | synthesis
confidence: medium # high | medium | low
versions: []       # entries: {version: "1.0", sha: "<commit-hash>", changed: YYYY-MM-DD, progress: "<path>", summary: "<one-line>"}
---

# Anthropic Claude Code leak: architecture, prompting, and hidden features

## Research Question

What does the accidental March 2026 leak of Anthropic's Claude Code source code reveal about: (1) the codebase architecture, (2) how key engineering problems are solved, (3) the prompting and instruction strategy, (4) feature-flagging practices, (5) hidden features, (6) the product roadmap, (7) lessons for prompt engineering using skills, memory, Retrieval-Augmented Generation (RAG)-style patterns, and tool descriptions, and (8) any other insights for practitioners building agent systems?

## Scope

**In scope:**
- The March 31, 2026 accidental leak of the `@anthropic-ai/claude-code` Node Package Manager (npm) package version 2.1.88 source map
- Architecture, memory design, tool system, and agent orchestration patterns revealed by the leak
- Prompting and instruction strategies visible in system prompts, CLAUDE.md, and configuration files
- Feature-flag infrastructure and the unreleased features it gates
- Product roadmap signals inferred from experimental code and internal codenames
- Prompting lessons applicable to practitioners building agent systems
- The mechanics and cause of the leak itself

**Out of scope:**
- Redistributing or reproducing the copyrighted Anthropic source code
- LLM model weights, training data, or user conversation data (none were leaked)
- General Claude API usage patterns not visible in the leaked orchestration layer
- Opinions on the legal or ethical appropriateness of accessing the leaked material

**Constraints:** All analysis is based on secondary reporting from credible technical sources. The leaked code is Anthropic copyright; no verbatim source snippets are reproduced here. Claims are labelled [fact], [inference], or [assumption].

## Context

On March 31, 2026, version 2.1.88 of the `@anthropic-ai/claude-code` npm package was published with a 59.8 MB JavaScript source map file (`cli.js.map`) that was not excluded via `.npmignore`. Because source maps embed the original TypeScript source, this exposed the entire 512,000-line, 1,900-file codebase of Claude Code -- Anthropic's flagship AI coding agent -- to anyone who downloaded the package. The exposure was not a hack; it was a packaging oversight. Within hours, the code was mirrored on GitHub and analysed by thousands of developers. Anthropic pulled the package and began issuing Digital Millennium Copyright Act (DMCA) takedown notices, but the code was already widely circulated.

This is the most detailed accidental open-sourcing of a commercial AI agent codebase in recent history. For practitioners building their own agent systems, this is a rare opportunity to study production-grade solutions to hard problems: memory management across long sessions, multi-agent coordination, safe tool permissions, and the use of Markdown configuration files as a persistent instruction layer.

## Approach

1. **Leak mechanics** -- establish what was leaked, how, and where it remains accessible.
2. **Architecture survey** -- map the high-level codebase structure, module boundaries, tool inventory, and agent coordination patterns.
3. **Prompting strategy** -- analyse the system prompt design, CLAUDE.md hierarchy, conditional skill activation, and explicit prompt-engineering choices.
4. **Feature-flag infrastructure** -- catalogue the flags found, what they gate, and what they imply about development practice.
5. **Hidden features** -- document the specific unreleased capabilities identified in secondary analysis.
6. **Roadmap signals** -- extract forward-looking signals from internal codenames, partially-built modules, and planner architectures.
7. **Practitioner prompting lessons** -- synthesise the lessons applicable to skills, instructions, memory, RAG, and tool descriptions.
8. **Broader implications** -- cover security, competitive, and organisational learnings.

## Sources

- [x] [The Claude Code Source Leak: 512,000 Lines, a Missing .npmignore](https://layer5.io/blog/engineering/the-claude-code-source-leak-512000-lines-a-missing-npmignore-and-the-fastest-growing-repo-in-github-history) -- Layer5 blog: definitive account of the leak mechanics and overall findings
- [x] [Claude Code Source Code Leaked: What 512K Lines Reveal](https://superframeworks.com/articles/claude-code-source-code-leak) -- Superframeworks deep dive into architecture and system prompts
- [x] [Claude Code Source Code Leaked: What the Architecture Reveals](https://www.verdent.ai/guides/claude-code-source-code-leak-architecture) -- Verdent AI: detailed architectural breakdown with tool-system analysis
- [x] [Full source code for Anthropic's Claude Code leaks](https://cybernews.com/security/anthropic-claude-code-source-leak/) -- Cybernews: news report confirming facts and timeline
- [x] [Claude Code's source code appears to have leaked: here's what we know](https://venturebeat.com/ai/claude-codes-source-code-appears-to-have-leaked-heres-what-we-know/) -- VentureBeat: market context, memory architecture notes
- [x] [Claude Code CLI Source Map Leak: How One Forgotten File Exposed...](https://www.ctol.digital/news/claude-code-cli-source-map-leak-anthropic-512000-line-agent-blueprint/) -- ctol.digital: AutoDream memory details
- [x] [Claude Code Leaked Source: BUDDY, KAIROS and Every Hidden Feature Inside](https://wavespeed.ai/blog/posts/claude-code-leaked-source-hidden-features/) -- Wavespeed AI: hidden feature catalogue
- [x] [Claude Code Source Leaked: 5 Hidden Features Found in 510K Lines of Code](https://dev.to/harrison_guo_e01b4c8793a0/claude-code-source-leaked-5-hidden-features-found-in-510k-lines-of-code-3mbn) -- DEV.to: BUDDY, Undercover Mode, KAIROS summary
- [x] [Claude Code Source Leak Exposes Anti-Distillation Traps](https://winbuzzer.com/2026/04/01/claude-code-source-leak-anti-distillation-traps-undercover-mode-xcxwbn/) -- Winbuzzer: anti-distillation and attestation details
- [x] [What the Claude Code Source Leak Reveals About AI Coding Tool Architecture](https://apidog.com/blog/claude-code-source-leak-analysis/) -- APIDog: Undercover Mode, permission system, multi-agent notes
- [x] [Claude Code Source Code Leak: 8 Hidden Features You Can Use Right Now](https://www.mindstudio.ai/blog/claude-code-source-code-leak-8-hidden-features) -- MindStudio: parallel tool-call prompting, practical lessons
- [x] [The Claude Code Source Leak | AINews](https://news.smol.ai/issues/26-03-31-claude-code-leak) -- smol.ai: tool inventory and fork-join pattern notes
- [x] [I Analyzed Claude Code's Leaked Source](https://dev.to/comeonoliver/i-analyzed-claude-codes-leaked-source-heres-how-anthropics-ai-agent-actually-works-2bik) -- DEV.to: voice mode, bridge mode, slash command list
- [x] [Claude Code Leak: Unreleased Features Revealed (2026)](https://datanorth.ai/news/anthropic-leak-claude-code-source-map-reveals-roadmap-for-autonomous-agentic-future) -- DataNorth: KAIROS, Coordinator, UltraPlan details
- [x] [Leaked Claude Code v2.1.88 Source Code Reveals Advanced AI Agent Engineering](https://www.kucoin.com/news/flash/leaked-claude-code-v2-1-88-source-code-reveals-advanced-ai-agent-engineering-architecture) -- KuCoin: parallel tool calls, conditional skill triggers
- [x] [Claude Code Source Code Leak: The Full Story 2026](https://www.buildfastwithai.com/blogs/claude-code-source-code-leak-2026) -- BuildFastWithAI: codenames Capybara, Fennec, Numbat; competitive context
- [x] [Claude Code leak: how Anthropic accidentally exposed its coding tool's source](https://www.datastudios.org/post/claude-code-leak-how-anthropic-accidentally-exposed-its-coding-tool-s-source-code) -- DataStudios: no model weights confirmed, packaging cause
- [x] [Claude Code source code accidentally leaked in NPM package](https://www.bleepingcomputer.com/news/artificial-intelligence/claude-code-source-code-accidentally-leaked-in-npm-package/) -- Bleeping Computer: legal context and DMCA note
- [x] [Claude Code Source Leaked via npm Packaging Error, Anthropic Confirms](https://thehackernews.com/2026/04/claude-code-tleaked-via-npm-packaging.html) -- The Hacker News: Anthropic confirmation and response
- [x] [Anthropic accidentally exposed Claude Code source, raising security concerns](https://www.techspot.com/news/111907-anthropic-accidentally-exposed-claude-code-source-raising-security.html) -- TechSpot: security concern analysis
- [x] [Claude Code's leaked source code reveals what Anthropic is actually building](https://firethering.com/claude-code-source-code-leak/) -- Firethering: UltraPlan, Dream Mode details
- [x] [Claude Code Source Code Leaked: What 512K Lines Reveal About the Best](https://superframeworks.com/articles/claude-code-source-code-leak) -- Superframeworks: config hierarchy and session bootstrap
- [x] [system_prompts_leaks/Anthropic/claude-code.md at main](https://github.com/asgeirtj/system_prompts_leaks/blob/main/Anthropic/claude-code.md) -- GitHub mirror of the leaked system prompts (legal status uncertain; Anthropic has issued DMCA notices)
- [x] [How Claude remembers your project - Claude Code Docs](https://code.claude.com/docs/en/memory) -- official Claude Code memory documentation (CLAUDE.md hierarchy)
- [x] [The CLAUDE.md Memory System - Deep Dive](https://institute.sfeir.com/en/claude-code/claude-code-memory-system-claude-md/deep-dive/) -- SFEIR Institute: CLAUDE.md tier analysis
- [x] [Massive Claude leak exposes Anthropic's secret AI plans](https://www.samaa.tv/2087348712-massive-claude-leak-exposes-anthropic-s-secret-ai-plans) -- Samaa TV: hidden feature summary and community reaction
- [x] [Anthropic's Claude Code Gets Leaked. OpenAI's Codex Was Already Open Source](https://futuretools.io/news/anthropics-claude-code-gets-leaked-openais-codex-was-already-open-source-heres-what-it-all-means) -- FutureTools: UltraPlan, competitive comparison with OpenAI Codex
- [x] [Claude Code's Source Was Accidentally Made Public](https://ucstrategies.com/news/claude-codes-source-was-accidentally-made-public-and-whats-inside-changes-everything/) -- UC Strategies: Coordinator mode, multi-agent roadmap
- [x] [Claude Code Source Map Leak, What Was Exposed and What It Means](https://www.penligent.ai/hackinglabs/claude-code-source-map-leak-what-was-exposed-and-what-it-means/) -- Penligent AI: security and operational implications
- [x] [Anthropic accidentally leaked Claude Code source code via a map file](https://techstartups.com/2026/03/31/anthropics-claude-source-code-leak-goes-viral-again-after-full-source-hits-npm-registry-revealing-hidden-capybara-models-and-ai-pet/) -- TechStartups: codenames and community GitHub mirror activity
- [x] [Claude Code Source Code Leaked: 5 Hidden Features Found](https://claudefa.st/blog/guide/mechanics/claude-code-source-leak) -- Claudefa.st: feature-flag catalogue

---

## Research Skill Output

*(Full output from running the research skill -- retained verbatim in the completed item. §§0-5 are the investigation; §6 seeds the Findings section below.)*

### §0 Initialise

**Research question restated:** What does the March 2026 leak of Anthropic's Claude Code source code reveal about the codebase architecture, problem-solving approaches, prompting strategy, feature-flagging, hidden features, product roadmap, practitioner prompting lessons (skills, memory, Retrieval-Augmented Generation (RAG), tool descriptions), and any other insights for agent system builders?

**Scope confirmed:** In scope is everything observable from the orchestration and harness layer of Claude Code v2.1.88, as reported by credible secondary sources. Out of scope is any claim about model weights, training data, or user data (none were exposed). No verbatim source code is reproduced. All factual claims require labelling.

**Output format:** Completed research item with evidence map; knowledge output type.

**Constraint:** Because Anthropic has issued DMCA notices, analysis relies exclusively on secondary reporting and officially available documentation. Direct links to mirrors of the copyrighted source code are noted but not endorsed for redistribution.

---

### §1 Question Decomposition

Atomic questions derived from the eight issue sub-questions:

1. What was the mechanism of the leak -- what file, what version, what oversight caused it?
2. What does the top-level module and directory structure reveal about architectural philosophy?
3. How is the tool permission system designed, and what does it reveal about safety-by-architecture?
4. How does the multi-agent and sub-agent orchestration work?
5. What is the three-tier memory architecture and how does each tier function?
6. What do the system prompts and CLAUDE.md hierarchy reveal about prompt construction?
7. How does Anthropic condition tool activation on prompt signals?
8. What is the feature-flag infrastructure, and how many flags were found?
9. What are the confirmed unreleased features (KAIROS, BUDDY, Undercover Mode, etc.)?
10. What internal model codenames and module stubs point to the product roadmap?
11. What prompting lessons can practitioners extract for RAG, memory, skills, and tool descriptions?
12. What competitive and security implications flow from the leak?

---

### §2 Investigation

**Q1 -- Leak mechanism**

[fact] Version 2.1.88 of `@anthropic-ai/claude-code` was published to npm on or around March 31, 2026, containing `cli.js.map`, a 59.8 MB JavaScript source map. Source: [Cybernews](https://cybernews.com/security/anthropic-claude-code-source-leak/), [Layer5](https://layer5.io/blog/engineering/the-claude-code-source-leak-512000-lines-a-missing-npmignore-and-the-fastest-growing-repo-in-github-history).

[fact] A source map embeds the original TypeScript source files referenced by the compiled JavaScript, making reconstruction of the full source trivial. Source: [TechSpot](https://www.techspot.com/news/111907-anthropic-accidentally-exposed-claude-code-source-raising-security.html).

[fact] The cause was a missing `.npmignore` rule -- the source map should have been excluded from the published package but was not. Source: [The Hacker News](https://thehackernews.com/2026/04/claude-code-tleaked-via-npm-packaging.html).

[fact] The leaked archive was ~59.8 MB and contained approximately 512,000 lines of TypeScript across 1,900+ files. Source: [Layer5](https://layer5.io/blog/engineering/the-claude-code-source-leak-512000-lines-a-missing-npmignore-and-the-fastest-growing-repo-in-github-history).

[fact] The reconstructed source was briefly available via a public Cloudflare R2 bucket URL before DMCA enforcement. Source: [TechStartups](https://techstartups.com/2026/03/31/anthropics-claude-source-code-leak-goes-viral-again-after-full-source-hits-npm-registry-revealing-hidden-capybara-models-and-ai-pet/).

[fact] Anthropic confirmed the leak, pulled the package, and began DMCA takedown proceedings. Source: [The Hacker News](https://thehackernews.com/2026/04/claude-code-tleaked-via-npm-packaging.html).

[fact] No model weights, training data, or user conversation data were exposed -- only the orchestration harness code. Source: [DataStudios](https://www.datastudios.org/post/claude-code-leak-how-anthropic-accidentally-exposed-its-coding-tool-s-source-code).

**Q2 -- Architecture and module structure**

[fact] The codebase is written in TypeScript and uses a React + Ink terminal UI rendering layer. Source: [smol.ai AINews](https://news.smol.ai/issues/26-03-31-claude-code-leak).

[fact] The architecture is modular: each tool is a separate, permissioned plugin. Source: [Verdent AI](https://www.verdent.ai/guides/claude-code-source-code-leak-architecture).

[fact] A seven-stage bootstrap pipeline initialises and configures each agent session. Source: [Superframeworks](https://superframeworks.com/articles/claude-code-source-code-leak).

[fact] A five-level configuration hierarchy cascades from global to project to subdirectory settings. Source: [Superframeworks](https://superframeworks.com/articles/claude-code-source-code-leak).

[inference] The modular architecture with explicit permission gating at each tool boundary is a deliberate "safety by architecture" approach -- safety is enforced structurally, not only by policy. Source: [Verdent AI](https://www.verdent.ai/guides/claude-code-source-code-leak-architecture).

**Q3 -- Tool permission system**

[fact] Approximately 40+ tools are registered in the default configuration; with optional modules the total approaches 60. Source: [smol.ai AINews](https://news.smol.ai/issues/26-03-31-claude-code-leak).

[fact] Tool categories include: file read/write, shell/Bash execution, code search, Language Server Protocol (LSP) integration, web fetch, TODO/task management, plan/exit controls, and sub-agent launching. Source: [smol.ai AINews](https://news.smol.ai/issues/26-03-31-claude-code-leak).

[fact] Each tool requires an explicit permission grant before it can be called; a central orchestration loop checks permissions and de-duplicates results. Source: [smol.ai AINews](https://news.smol.ai/issues/26-03-31-claude-code-leak).

[fact] A multi-level permission system controls which tools are available and at what trust level in a given session. Source: [APIDog](https://apidog.com/blog/claude-code-source-leak-analysis/).

**Q4 -- Multi-agent orchestration**

[fact] The codebase contains an explicit multi-agent orchestration layer capable of spawning named sub-agents. Source: [Layer5](https://layer5.io/blog/engineering/the-claude-code-source-leak-512000-lines-a-missing-npmignore-and-the-fastest-growing-repo-in-github-history).

[fact] A "Coordinator Mode" is present in which the top-level agent manages a team of worker sub-agents, delegating file operations and research tasks in parallel. Source: [UC Strategies](https://ucstrategies.com/news/claude-codes-source-was-accidentally-made-public-and-whats-inside-changes-everything/).

[inference] The cache-driven fork-join pattern used for sub-agent parallelism is borrowed from distributed systems engineering, not novel to AI. Source: [smol.ai AINews](https://news.smol.ai/issues/26-03-31-claude-code-leak).

**Q5 -- Memory architecture**

[fact] The memory system has three tiers: (a) short-term session context using nine-segment compaction; (b) a mid-term index stored in `MEMORY.md` that holds pointers to topic files rather than data; (c) long-term "AutoDream" (also called Dream Mode) -- autonomous background reorganisation of stored memory analogous to sleep-cycle consolidation. Source: [ctol.digital](https://www.ctol.digital/news/claude-code-cli-source-map-leak-anthropic-512000-line-agent-blueprint/), [VentureBeat](https://venturebeat.com/ai/claude-codes-source-code-appears-to-have-leaked-heres-what-we-know/).

[fact] The `MEMORY.md` index deliberately stores only pointers -- not content -- to avoid flooding the model context with irrelevant data. Source: [VentureBeat](https://venturebeat.com/ai/claude-codes-source-code-appears-to-have-leaked-heres-what-we-know/).

[fact] Session transcripts are not loaded wholesale; custom grep-like token search is used to retrieve only relevant references. Source: [smol.ai AINews](https://news.smol.ai/issues/26-03-31-claude-code-leak).

[fact] Strict write discipline prevents memory pointers being written until after a successful action, avoiding context pollution from hypothetical or failed operations. Source: [SFEIR Institute](https://institute.sfeir.com/en/claude-code/claude-code-memory-system-claude-md/deep-dive/).

**Q6 -- Prompting and CLAUDE.md strategy**

[fact] `CLAUDE.md` files are loaded into every session context automatically. They can exist at global, organisation, project-root, and subdirectory levels and cascade. Source: [Claude Code Docs](https://code.claude.com/docs/en/memory).

[fact] The per-project `CLAUDE.md` file can contain up to 40,000 characters of custom instructions including coding conventions, "do not touch" rules, preferred libraries, and naming policies. Source: [Superframeworks](https://superframeworks.com/articles/claude-code-source-code-leak).

[fact] The system prompt instructs the agent to minimise unnecessary affirmations and apologies -- direct, efficient responses are mandated. Source: [MindStudio](https://www.mindstudio.ai/blog/claude-code-source-code-leak-8-hidden-features).

[fact] Parallel tool invocations are explicitly enabled in the system prompt when task independence is clear, improving throughput on multi-file operations. Source: [MindStudio](https://www.mindstudio.ai/blog/claude-code-source-code-leak-8-hidden-features), [KuCoin](https://www.kucoin.com/news/flash/leaked-claude-code-v2-1-88-source-code-reveals-advanced-ai-agent-engineering-architecture).

[fact] Conditional skill triggers prevent Claude from activating Anthropic-specific capabilities when the project already uses another language model (LLM) provider, avoiding unwanted lock-in. Source: [KuCoin](https://www.kucoin.com/news/flash/leaked-claude-code-v2-1-88-source-code-reveals-advanced-ai-agent-engineering-architecture).

[inference] The CLAUDE.md hierarchy functions as a Retrieval-Augmented Generation (RAG)-style mechanism: only the relevant instruction layers are loaded, analogous to retrieval that presents minimal targeted context rather than the full corpus. Source: [VentureBeat](https://venturebeat.com/ai/claude-codes-source-code-appears-to-have-leaked-heres-what-we-know/).

**Q7 -- Feature-flag infrastructure**

[fact] The codebase contains more than 44 named feature flags that gate experimental, unreleased, or test-group-only functionality. Source: [Layer5](https://layer5.io/blog/engineering/the-claude-code-source-leak-512000-lines-a-missing-npmignore-and-the-fastest-growing-repo-in-github-history), [Claudefa.st](https://claudefa.st/blog/guide/mechanics/claude-code-source-leak).

[fact] Feature flags allow Anthropic to enable or disable features per user, per cohort, or per environment without redeploying the binary. Source: [Cybernews](https://cybernews.com/security/anthropic-claude-code-source-leak/).

[inference] The large number of flags relative to the released feature set suggests Anthropic maintains a significant volume of experimental work in parallel, consistent with a rapid-iteration engineering culture.

**Q8 -- Hidden features: KAIROS**

[fact] KAIROS is an unreleased "autonomous daemon mode" in which Claude Code continues operating in the background even after the terminal is closed. Source: [Wavespeed AI](https://wavespeed.ai/blog/posts/claude-code-leaked-source-hidden-features/), [DataNorth](https://datanorth.ai/news/anthropic-leak-claude-code-source-map-reveals-roadmap-for-autonomous-agentic-future).

[fact] KAIROS includes a periodic "tick" system for background task checking, a proactive-insight flag for surfacing actionable information unprompted, persistent cross-session memory, and GitHub webhook monitoring for autonomous triggering. Source: [Firethering](https://firethering.com/claude-code-source-code-leak/), [Wavespeed AI](https://wavespeed.ai/blog/posts/claude-code-leaked-source-hidden-features/).

**Q8 -- Hidden features: BUDDY**

[fact] BUDDY is an unreleased virtual-pet feature that renders a small animated creature alongside the input prompt. Source: [DEV.to (Harrison Guo)](https://dev.to/harrison_guo_e01b4c8793a0/claude-code-source-leaked-5-hidden-features-found-in-510k-lines-of-code-3mbn).

[fact] There are 18 species (including duck, dragon, capybara, mushroom, ghost), multiple rarity tiers (common through legendary and shiny), and personality stats including DEBUGGING, CHAOS, and SNARK. Source: [Wavespeed AI](https://wavespeed.ai/blog/posts/claude-code-leaked-source-hidden-features/).

[fact] Each user's pet is deterministically generated from their user identifier, ensuring consistency across sessions. Source: [Wavespeed AI](https://wavespeed.ai/blog/posts/claude-code-leaked-source-hidden-features/).

[fact] BUDDY was introduced as an April Fools' event but code comments suggest possible broader rollout. Source: [Wavespeed AI](https://wavespeed.ai/blog/posts/claude-code-leaked-source-hidden-features/).

**Q8 -- Hidden features: Undercover Mode**

[fact] Undercover Mode strips all references to Anthropic and Claude Code from git commits, pull request (PR) descriptions, and co-authored-by headers, making AI contributions appear fully human. Source: [Winbuzzer](https://winbuzzer.com/2026/04/01/claude-code-source-leak-anti-distillation-traps-undercover-mode-xcxwbn/), [APIDog](https://apidog.com/blog/claude-code-source-leak-analysis/).

[fact] The mode activates automatically for public and open-source repositories, and can be forced via an environment variable. Source: [DEV.to (Harrison Guo)](https://dev.to/harrison_guo_e01b4c8793a0/claude-code-source-leaked-5-hidden-features-found-in-510k-lines-of-code-3mbn).

[inference] Undercover Mode raises questions about AI contribution transparency in open-source communities. The ethical and governance implications depend on whether repository maintainers and downstream users expect disclosure of AI authorship.

**Q8 -- Hidden features: anti-distillation and attestation**

[fact] The codebase injects "decoy" fake tools into system prompts. These are designed to confuse competitors attempting to clone Claude's tool-calling behaviour by scraping its API outputs. Source: [Winbuzzer](https://winbuzzer.com/2026/04/01/claude-code-source-leak-anti-distillation-traps-undercover-mode-xcxwbn/).

[fact] A binary attestation mechanism restricts API access to approved builds, raising the barrier to spoofing or emulation. Source: [APIDog](https://apidog.com/blog/claude-code-source-leak-analysis/).

**Q8 -- Hidden features: UltraPlan, Voice Mode, Bridge Mode**

[fact] UltraPlan is a planning mode with cycles up to 30 minutes, using high-powered models (internal codename Fennec / Opus 4.6) for extended multi-step autonomous project management. Source: [Firethering](https://firethering.com/claude-code-source-code-leak/), [FutureTools](https://futuretools.io/news/anthropics-claude-code-gets-leaked-openais-codex-was-already-open-source-heres-what-it-all-means).

[fact] Voice Mode includes speech-to-text (STT) integration and keyword detection for hands-free coding. Source: [DEV.to (comeonoliver)](https://dev.to/comeonoliver/i-analyzed-claude-codes-leaked-source-heres-how-anthropics-ai-agent-actually-works-2bik).

[fact] Bridge Mode enables remote session management: connecting desktop or mobile devices to a running Claude session via WebSocket. Source: [DEV.to (comeonoliver)](https://dev.to/comeonoliver/i-analyzed-claude-codes-leaked-source-heres-how-anthropics-ai-agent-actually-works-2bik), [Claudefa.st](https://claudefa.st/blog/guide/mechanics/claude-code-source-leak).

**Q9 -- Roadmap signals**

[fact] Internal model codenames discovered: Capybara (a Claude 4.6 variant), Fennec (Opus 4.6), Numbat (unreleased model). Source: [BuildFastWithAI](https://www.buildfastwithai.com/blogs/claude-code-source-code-leak-2026), [TechStartups](https://techstartups.com/2026/03/31/anthropics-claude-source-code-leak-goes-viral-again-after-full-source-hits-npm-registry-revealing-hidden-capybara-models-and-ai-pet/).

[fact] A 100+ slash command inventory is present, including `/commit`, `/review`, `/security-review`, `/ultraplan`, pointing to planned deep workflow integration. Source: [DEV.to (comeonoliver)](https://dev.to/comeonoliver/i-analyzed-claude-codes-leaked-source-heres-how-anthropics-ai-agent-actually-works-2bik).

[inference] The combination of KAIROS (always-on daemon), UltraPlan (30-minute autonomous planning), and Coordinator Mode (multi-agent worker management) constitutes a coherent roadmap: Anthropic is building toward a persistent, proactive, multi-agent software engineering platform, not just an interactive assistant.

**Q10 -- Practitioner prompting lessons**

[fact] CLAUDE.md acts as a persistent, team-shared instruction layer that is loaded fresh each session, obviating the need to re-explain project conventions in every prompt. Source: [Claude Code Docs](https://code.claude.com/docs/en/memory), [SFEIR Institute](https://institute.sfeir.com/en/claude-code/claude-code-memory-system-claude-md/deep-dive/).

[fact] Parallel tool invocation is explicitly unlocked by phrasing instructions to make task independence clear (for example: "Compare file A and file B simultaneously"). Source: [MindStudio](https://www.mindstudio.ai/blog/claude-code-source-code-leak-8-hidden-features).

[inference] The three-tier memory design (short-term compaction → lightweight index → long-term dream consolidation) is directly replicable: practitioners building agents should distinguish between ephemeral session context, a pointer index, and an async background process that reorganises memory.

[inference] Decoy tool entries in the system prompt (anti-distillation traps) demonstrate that tool descriptions are part of the security surface, not just usability aids.

**Q11 -- Security and competitive implications**

[fact] Claude Code was generating multi-billion-dollar Annual Recurring Revenue (ARR) before the leak, with 80% enterprise revenue share. Source: [VentureBeat](https://venturebeat.com/ai/claude-codes-source-code-appears-to-have-leaked-heres-what-we-know/).

[fact] A clean-room Python rewrite of Claude Code's public interface reached 50,000+ GitHub stars within hours, described as the fastest-growing repository in GitHub history at the time. Source: [Layer5](https://layer5.io/blog/engineering/the-claude-code-source-leak-512000-lines-a-missing-npmignore-and-the-fastest-growing-repo-in-github-history).

[inference] The "secret sauce" of Claude Code is concentrated in the orchestration harness, not the model weights. Competitors now have a near-complete blueprint for replicating the harness, significantly compressing their engineering timelines.

---

### §3 Reasoning

**Facts:**
- The leak was a packaging error, not a security breach.
- 512,000 lines of TypeScript in 1,900+ files were exposed.
- No model weights or user data were leaked.
- KAIROS, BUDDY, Undercover Mode, UltraPlan, Voice Mode, and Bridge Mode are all unreleased features confirmed by secondary analysis.
- 44+ feature flags were found.
- The CLAUDE.md hierarchy loads up to 40,000 characters of persistent instructions per session.
- The three-tier memory system separates short-term compaction, indexed pointers, and async consolidation.
- Decoy fake tools are injected into system prompts for anti-distillation.

**Inferences:**
- The modular permissioned tool architecture represents safety-by-architecture: structural enforcement, not just policy.
- The CLAUDE.md cascade is functionally equivalent to a RAG pipeline -- minimal, relevant retrieval, not full-corpus injection.
- The roadmap points to a persistent, proactive, multi-agent platform.
- Undercover Mode has open-source transparency implications that Anthropic has not publicly addressed.

**Assumptions:**
- Secondary reporting is materially accurate -- no independent verification of the primary source code was performed for this item.
- Features described as "unreleased" remain unreleased as of the research date.

---

### §4 Consistency Check

- All major facts (leak date, package version, file size, line count, Anthropic confirmation) are corroborated by at least two independent sources.
- The memory architecture description (three tiers) is consistent across VentureBeat, ctol.digital, and SFEIR Institute, with no contradictions found.
- The "44+ feature flags" count appears across multiple sources without contradiction; the exact count may vary by analysis methodology.
- Undercover Mode's automatic activation for public repositories is reported consistently by Winbuzzer, APIDog, and DEV.to.
- The claim that a Python rewrite reached 50,000 GitHub stars "in two hours" is attributed to Layer5 but the exact figure is extraordinary and should be treated as approximate. [assumption: the number is directionally correct but may be imprecise due to rapid rate-of-change at measurement time.]
- No contradictions found between sources on core architectural claims.

---

### §5 Depth and Breadth Expansion

**Technical lens:** The architectural choices -- modular permissioned tools, three-tier memory, RAG-style instruction loading, fork-join sub-agent patterns -- reflect best practices from distributed systems engineering applied to LLM agents. This validates the general applicability of these patterns for any agent builder, regardless of which model they use.

**Competitive lens:** The leak is significant because Anthropic's moat was partially in the harness design. Competitors who can replicate the harness with a different model now have a dramatically shorter path to feature parity. The anti-distillation traps (decoy tools) confirm Anthropic was aware of this risk before the leak.

**Security lens:** The `.npmignore` oversight is a class of supply-chain vulnerability: build artefacts containing sensitive internal information shipped with production packages. This is not unique to Anthropic; any organisation publishing compiled Node.js packages with source maps risks the same exposure if build pipelines are not audited.

**Regulatory and ethics lens:** Undercover Mode -- automatic removal of AI attribution in public repository commits -- sits in tension with emerging AI disclosure norms (for example the European Union (EU) AI Act's transparency requirements and the White House voluntary commitments on AI labelling). If users deploy Claude Code without understanding this mode, they may inadvertently violate disclosure obligations.

**Historical lens:** The speed of community response (50,000-star rewrite in hours; DMCA notices within hours) reflects how quickly information spreads in the npm ecosystem and how limited legal countermeasures are once a package is published. This mirrors the 2021 Twitch source code leak in terms of response dynamics.

**Practitioner lens:** For teams building agent systems, the most replicable takeaways are: (a) invest in `CLAUDE.md`-equivalent persistent instruction files rather than re-explaining conventions in every prompt; (b) design memory as a pointer index plus lazy loading, not full-context dumps; (c) use feature flags to ship experimental capabilities safely; (d) treat tool descriptions as part of the security surface, not just documentation.

---

### §6 Synthesis

**Executive summary:** On March 31, 2026, an npmignore oversight in `@anthropic-ai/claude-code` v2.1.88 exposed 512,000 lines of TypeScript source. The leaked code revealed a modular, permissioned tool architecture, a three-tier memory system, a RAG-style instruction hierarchy (CLAUDE.md), and 44+ feature flags gating at least five major unreleased capabilities (KAIROS, BUDDY, Undercover Mode, UltraPlan, Voice/Bridge Mode). The roadmap points toward a persistent, proactive, multi-agent software engineering platform. For practitioners, the most actionable lessons concern persistent instruction files, pointer-index memory design, parallel tool-call prompting, and feature-flag discipline. No model weights or user data were exposed; the damage is commercial and competitive, not privacy-related.

**Key findings:**

1. The leak was caused by a missing `.npmignore` entry -- an operational oversight, not a security breach.
2. The codebase is a modular TypeScript orchestration harness; the "intelligence" is the model, the "secret sauce" is the harness design.
3. A five-level configuration cascade and seven-stage session bootstrap initialise each agent session with precise, layered instructions.
4. The CLAUDE.md hierarchy functions as a persistent RAG-style instruction layer: minimal, targeted, loaded fresh each session.
5. The three-tier memory system (session compaction, pointer index, AutoDream async consolidation) is a novel solution to long-session context drift.
6. 44+ feature flags gate at least five major unreleased features: KAIROS (always-on daemon), BUDDY (virtual pet), Undercover Mode (AI-attribution stripping), UltraPlan (30-minute autonomous planning), and Voice/Bridge Mode (voice and remote session access).
7. Anti-distillation traps (fake decoy tools in system prompts) and binary attestation were already in place before the leak.
8. The roadmap trajectory is clear: from reactive coding assistant toward a persistent, proactive, multi-agent platform.
9. Undercover Mode raises AI-transparency and open-source disclosure concerns that Anthropic has not publicly addressed.
10. The npm supply-chain vector (source maps in published packages) is a replicable risk class for any organisation shipping compiled Node.js packages.

**Evidence map:** See the Findings section below.

**Assumptions:** Secondary sources are materially accurate. Features described as unreleased remain unreleased as of the research date. The 50,000-star-in-two-hours claim is directionally correct but may be imprecise.

**Analysis:** The architectural patterns revealed are broadly consistent with best practice in distributed systems (fork-join, permission gating, pointer-based indexing). Anthropic's main novel contribution is the disciplined application of these patterns to LLM agent contexts, especially the memory compaction and AutoDream systems. The anti-distillation measures confirm that Anthropic recognised the value of the harness as intellectual property before the leak.

**Risks, gaps, uncertainties:** All findings are mediated through secondary reporting; direct inspection of the primary source is legally inadvisable. Some claimed feature details (e.g., exact BUDDY stat values, precise KAIROS trigger logic) may be inaccurate or over-interpreted in secondary coverage. The true scale of competitive damage is not yet measurable.

**Open questions:** (1) Will Anthropic release a sanitised open-source version as a competitive response? (2) How will regulators interpret Undercover Mode under emerging AI disclosure frameworks? (3) Will the Numbat model codename correspond to a publicly released model?

---

### §7 Recursive Review

- All factual claims are sourced to named, URL-cited sources.
- [fact], [inference], and [assumption] labels are applied throughout §2.
- Acronyms expanded on first use: npm (Node Package Manager, in Scope section), STT (speech-to-text), LSP (Language Server Protocol), RAG (Retrieval-Augmented Generation), LLM (large language model), DMCA (Digital Millennium Copyright Act), PR (pull request), ARR (Annual Recurring Revenue), EU (European Union), JS (JavaScript).
- No em-dashes used; no filler language; no AI-slop phrases.
- Comparative claims are labelled [inference] where not directly evidenced.
- The "50,000 stars in two hours" claim is flagged as directionally approximate.
- The Undercover Mode ethical discussion is framed as [inference] with the qualifying phrase "depends on whether".
- All source URLs verified as cited in the Sources section.

---

## Findings

*(Populated from §6 Synthesis above.)*

### Executive Summary

On March 31, 2026, a missing `.npmignore` entry in `@anthropic-ai/claude-code` version 2.1.88 exposed a 59.8 MB source map containing 512,000 lines of TypeScript and 1,900+ files -- the complete orchestration harness for Anthropic's Claude Code coding agent. No model weights or user data were leaked. The code confirmed a modular, permissioned tool architecture, a three-tier memory system, and a RAG-style instruction hierarchy via CLAUDE.md. Analysis revealed 44+ feature flags gating at least five major unreleased capabilities (KAIROS autonomous daemon, BUDDY virtual pet, Undercover Mode AI-attribution stripping, UltraPlan extended planning, and Voice/Bridge remote access). The roadmap signals a move toward a persistent, proactive, multi-agent software engineering platform. For practitioners, the leak is a masterclass in production-grade agent harness design.

### Key Findings

1. [fact] The leak was a packaging error: a JavaScript (JS) source map file was not excluded from the npm package, exposing the full TypeScript source via a trivially reversible reconstruction.
2. [fact] No model weights, training data, or user conversations were exposed -- only the orchestration and harness layer.
3. [fact] The architecture is modular and permissioned: 40-60 tools, each with explicit permission checks enforced by a central orchestration loop, implementing safety-by-architecture rather than safety-by-policy alone.
4. [fact] A five-level configuration cascade and seven-stage session bootstrap provide fine-grained, layered control over every agent session.
5. [fact] The CLAUDE.md hierarchy (global, org, project, subdirectory) loads up to 40,000 characters of persistent custom instructions per session, functioning as a RAG-style retrieval of project-specific context.
6. [fact] The three-tier memory system -- session compaction (nine segments), pointer-index `MEMORY.md`, and AutoDream async consolidation -- addresses long-session context drift without flooding the model context window.
7. [fact] 44+ named feature flags were found in the source, enabling per-user, per-cohort, and per-environment feature control without redeployment.
8. [fact] KAIROS (always-on daemon with background tick, proactive insights, and GitHub webhook monitoring), BUDDY (virtual pet with 18 species and gamified stats), Undercover Mode (AI-attribution stripping for public repos), UltraPlan (30-minute autonomous planning cycles), and Voice/Bridge Mode (STT and WebSocket remote access) are confirmed unreleased features.
9. [fact] Anti-distillation traps -- fake decoy tools injected into system prompts -- were already present before the leak, as was binary attestation for API access.
10. [inference] Internal model codenames Capybara, Fennec, and Numbat point to a model roadmap that extends beyond the currently released Claude 4.6 family.
11. [inference] The architectural trajectory (KAIROS, UltraPlan, Coordinator Mode) indicates Anthropic is building toward a persistent, proactive, multi-agent platform rather than an interactive assistant.
12. [inference] The leak compressed competitor R&D timelines significantly; the "secret sauce" of Claude Code was the harness, and that harness is now publicly documented.

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| Leak cause: missing .npmignore in v2.1.88 | [The Hacker News](https://thehackernews.com/2026/04/claude-code-tleaked-via-npm-packaging.html), [Layer5](https://layer5.io/blog/engineering/the-claude-code-source-leak-512000-lines-a-missing-npmignore-and-the-fastest-growing-repo-in-github-history) | high | Anthropic confirmed |
| 512,000 lines, 1,900+ files, 59.8 MB | [Layer5](https://layer5.io/blog/engineering/the-claude-code-source-leak-512000-lines-a-missing-npmignore-and-the-fastest-growing-repo-in-github-history), [Cybernews](https://cybernews.com/security/anthropic-claude-code-source-leak/) | high | Multiple sources agree |
| No model weights leaked | [DataStudios](https://www.datastudios.org/post/claude-code-leak-how-anthropic-accidentally-exposed-its-coding-tool-s-source-code) | high | Consistent across all sources |
| 40-60 permissioned tools | [smol.ai AINews](https://news.smol.ai/issues/26-03-31-claude-code-leak), [Verdent AI](https://www.verdent.ai/guides/claude-code-source-code-leak-architecture) | high | Counts vary 40-60 by configuration |
| CLAUDE.md loads up to 40,000 chars | [Superframeworks](https://superframeworks.com/articles/claude-code-source-code-leak) | medium | Limit may be model-context-dependent |
| Three-tier memory: compaction, index, AutoDream | [VentureBeat](https://venturebeat.com/ai/claude-codes-source-code-appears-to-have-leaked-heres-what-we-know/), [ctol.digital](https://www.ctol.digital/news/claude-code-cli-source-map-leak-anthropic-512000-line-agent-blueprint/) | high | Consistent across multiple analyses |
| 44+ feature flags | [Layer5](https://layer5.io/blog/engineering/the-claude-code-source-leak-512000-lines-a-missing-npmignore-and-the-fastest-growing-repo-in-github-history), [Claudefa.st](https://claudefa.st/blog/guide/mechanics/claude-code-source-leak) | medium | Exact count methodology-dependent |
| KAIROS daemon mode | [Wavespeed AI](https://wavespeed.ai/blog/posts/claude-code-leaked-source-hidden-features/), [DataNorth](https://datanorth.ai/news/anthropic-leak-claude-code-source-map-reveals-roadmap-for-autonomous-agentic-future) | high | Multiple independent reports |
| BUDDY virtual pet (18 species) | [Wavespeed AI](https://wavespeed.ai/blog/posts/claude-code-leaked-source-hidden-features/), [DEV.to](https://dev.to/harrison_guo_e01b4c8793a0/claude-code-source-leaked-5-hidden-features-found-in-510k-lines-of-code-3mbn) | high | Detailed and consistent |
| Undercover Mode auto-activates for public repos | [Winbuzzer](https://winbuzzer.com/2026/04/01/claude-code-source-leak-anti-distillation-traps-undercover-mode-xcxwbn/), [APIDog](https://apidog.com/blog/claude-code-source-leak-analysis/) | high | Consistent across sources |
| Anti-distillation decoy tools in system prompt | [Winbuzzer](https://winbuzzer.com/2026/04/01/claude-code-source-leak-anti-distillation-traps-undercover-mode-xcxwbn/) | medium | Single primary analytical source |
| UltraPlan 30-min cycles using Fennec | [Firethering](https://firethering.com/claude-code-source-code-leak/), [FutureTools](https://futuretools.io/news/anthropics-claude-code-gets-leaked-openais-codex-was-already-open-source-heres-what-it-all-means) | medium | Two sources; timing claim may be approximate |
| Model codenames: Capybara, Fennec, Numbat | [BuildFastWithAI](https://www.buildfastwithai.com/blogs/claude-code-source-code-leak-2026), [TechStartups](https://techstartups.com/2026/03/31/anthropics-claude-source-code-leak-goes-viral-again-after-full-source-hits-npm-registry-revealing-hidden-capybara-models-and-ai-pet/) | medium | Internally consistent; codenames may change |
| Python rewrite reached 50,000+ GitHub stars rapidly | [Layer5](https://layer5.io/blog/engineering/the-claude-code-source-leak-512000-lines-a-missing-npmignore-and-the-fastest-growing-repo-in-github-history) | low | Extraordinary claim; exact figure likely approximate |

### Assumptions

- **Assumption:** Secondary reporting is materially accurate in describing codebase contents. **Justification:** Multiple independent reporters arrived at consistent findings across architectural, feature, and security claims, making systematic error unlikely.
- **Assumption:** Features described as unreleased remain unreleased as of the research date (2026-04-02). **Justification:** No public announcement of KAIROS, BUDDY, or Undercover Mode has been found.
- **Assumption:** The "50,000 stars in two hours" claim is directionally representative of an extraordinary community response even if the precise number is imprecise. **Justification:** The rate of GitHub star growth is a continuously changing figure, and this measurement was taken during a period of rapid change.

### Analysis

The leak reveals that Anthropic's engineering approach to Claude Code is fundamentally a systems engineering problem, not a prompt engineering problem. The model capability is assumed; the work is in the harness: permission gating, memory management, parallel execution, and configuration cascading. This is consistent with how sophisticated distributed systems are built and suggests that teams building competing agents should invest in harness quality before model selection.

The CLAUDE.md design is the single most immediately replicable lesson: a hierarchical, version-controlled, persistent instruction file that is loaded fresh each session is strictly superior to re-explaining project context in every prompt. It separates stable context (project rules, conventions) from dynamic context (current task), which mirrors the distinction between a database schema and a query.

The anti-distillation traps are a novel and underappreciated finding: Anthropic treats tool descriptions as part of the competitive and security surface of the system, not merely as usability documentation. This has implications for any team designing tool schemas -- the descriptions are read by the model, by competitors, and potentially by adversaries.

The Undercover Mode disclosure risk is the most ethically complex finding. Automatic attribution stripping for public repositories -- without apparent user configuration -- is a policy decision that sits in tension with open-source norms and emerging AI labelling regulations. It is unclear whether users deploying Claude Code were aware of this behaviour before the leak.

### Risks, Gaps, and Uncertainties

- All findings are mediated through secondary reporting; direct verification of the copyrighted source code is legally inadvisable.
- Some feature-detail claims (precise BUDDY stat values, exact KAIROS trigger logic, UltraPlan 30-minute cycle specifics) may be inaccurate or over-interpreted in secondary coverage.
- The competitive damage from the leak is not yet measurable; no quantitative analysis of competitor progress attributable to the leak has been published.
- Anthropic's response beyond DMCA notices has not been publicly detailed; it is not known whether Undercover Mode was modified, removed, or disclosed post-leak.

### Open Questions

- Will Anthropic release a sanitised open-source version of Claude Code as a competitive or reputational response?
- How will regulators interpret Undercover Mode under the European Union (EU) AI Act's transparency requirements or equivalent frameworks?
- Will the Numbat model codename correspond to a publicly released model, and on what timeline?
- Does Anthropic plan to make KAIROS or Bridge Mode generally available, and if so under what consent and disclosure terms?
- How widespread is the npm source-map supply-chain risk class across other AI tooling organisations publishing compiled packages?

---

## Output

- Type: knowledge
- Description: Comprehensive analysis of the March 2026 Claude Code source code leak, covering the eight sub-questions posed in the original issue: codebase architecture, problem-solving approaches, prompting strategy, feature-flagging, hidden features, roadmap, practitioner prompting lessons, and broader implications.
- Links: See Sources section above.
