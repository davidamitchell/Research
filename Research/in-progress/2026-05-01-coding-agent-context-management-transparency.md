---
review_count: 2
title: "What are best practices for transparent, user-controlled context management in Artificial Intelligence coding agent harnesses?"
added: 2026-05-01T08:17:39+00:00
status: reviewing
priority: high
blocks: []
tags: [agentic-ai, agentic-coding, llm, agent-tooling, workflow]
started: 2026-05-01T21:12:35+00:00
completed: ~
output: [knowledge]
cites: [2026-03-02-agent-memory-management-context-injection, 2026-03-03-knowledge-representation-agent-context, 2026-03-15-context-layers-aligned-decisions-synthesis, 2026-03-22-applied-context-engineering-agent-workflows, 2026-04-29-knowledge-scaffolding-context-engineering, 2026-05-01-appropriate-task-selection-coding-agents]
related: [2026-05-01-ai-coding-harness-quality-benchmarks, 2026-03-08-ai-coding-harnesses-agent-philosophy, 2026-04-20-harness-selection-tools-agents-skills-prompts-instructions]
superseded_by: ~
supersedes: ~
item_type: primary
confidence: medium
versions: []
---

# What are best practices for transparent, user-controlled context management in Artificial Intelligence coding agent harnesses?

## Research Question

What are the best practices for transparent, deterministic, and user-controlled context management in Large Language Model (LLM) coding agent harnesses, and what are the demonstrable harms of opaque context manipulation on agent reliability and user trust?

## Scope

**In scope:**
- Context management operations that affect agent behavior: system prompt content, tool definitions, mid-session injected reminders, compaction and pruning strategies, and context window overflow handling
- Evidence of how undisclosed context manipulation affects model behavior and user trust
- Design patterns for transparent context management: stable or versioned system prompts, explicit compaction policies, user-visible context summaries, and configurable context providers
- Observability tooling: what information should be surfaced to the user about what is in the agent's context
- Trade-offs between context richness and context pollution

**Out of scope:**
- Detailed treatment of specific commercial products beyond illustrative examples
- Training-time context effects
- Persistent memory systems beyond the current session, except where a source uses note-taking or file-based memory as part of session continuity

**Constraints:**
- Distinguish between published research, first-party product documentation, and practitioner observation
- Flag where claims rely on a single practitioner source

## Context

Mario Zechner's public talk transcript and later Pi materials describe a failure mode in which the harness, rather than the user, controls what enters the model context: prompts and tool definitions change across releases, reminders are inserted without clear user consent, and visibility into those changes is weak. [fact; source: https://github.com/The-Focus-AI/youtube-feed/blob/main/ai-engineer/videos/RjfbvDXpFls.json; https://mariozechner.at/posts/2025-11-30-pi-coding-agent/]

Anthropic's own product documentation confirms that claude.ai uses a periodically updated system prompt, while its context-engineering guidance treats compaction, note-taking, and selective retrieval as first-order design choices rather than invisible implementation details. [fact; source: https://platform.claude.com/docs/en/release-notes/system-prompts; https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents]

The practical question is therefore not whether context engineering exists, but what a coding-agent harness should guarantee to keep that engineering legible, stable enough to debug, and controllable enough to earn calibrated user trust. [inference; source: https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents; https://docs.langchain.com/oss/python/langchain/context-engineering; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-22-applied-context-engineering-agent-workflows.md]

## Approach

1. **Catalogue context manipulation types** - identify concrete categories of context manipulation in deployed harnesses: prompt mutation, tool mutation, injected reminders, retrieval, compaction, pruning, note-taking, and lifecycle middleware.
2. **Effects on model behavior** - review evidence on how distractors, excess context, pruning, and hidden context changes affect output consistency and reliability.
3. **Design patterns for transparency** - inspect open and configurable harnesses, especially Pi, Aider, Continue, LangChain, and Anthropic's own public guidance, for patterns that make context management explicit and controllable.
4. **Observability requirements** - derive the minimum viable interface for surfacing context state to users.
5. **Trade-offs** - identify where automation is genuinely useful, where hidden automation becomes harmful, and what hybrid policy best balances convenience with predictability.

## Sources

- [x] [The Focus AI archive (2026) Building pi in a World of Slop - Mario Zechner transcript](https://github.com/The-Focus-AI/youtube-feed/blob/main/ai-engineer/videos/RjfbvDXpFls.json)
- [x] [Zechner (2025) What I learned building an opinionated and minimal coding agent](https://mariozechner.at/posts/2025-11-30-pi-coding-agent/)
- [x] [badlogic/pi-mono repository](https://github.com/badlogic/pi-mono)
- [x] [Anthropic (2025) Effective context engineering for AI agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)
- [x] [Anthropic Claude system prompt release notes](https://platform.claude.com/docs/en/release-notes/system-prompts)
- [x] [Anthropic prompt engineering guide](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/system-prompts)
- [x] [Anthropic (2024) Building effective agents](https://www.anthropic.com/research/building-effective-agents)
- [x] [Aider usage documentation](https://aider.chat/docs/usage.html)
- [x] [Aider in-chat commands documentation](https://aider.chat/docs/usage/commands.html)
- [x] [Aider prompt caching documentation](https://aider.chat/docs/usage/caching.html)
- [x] [Aider copy and paste context documentation](https://aider.chat/docs/usage/copypaste.html)
- [x] [Continue custom context providers documentation](https://docs.continue.dev/customize/custom-providers)
- [x] [Continue config.yaml reference](https://docs.continue.dev/reference)
- [x] [LangChain context engineering documentation](https://docs.langchain.com/oss/python/langchain/context-engineering)
- [x] [Chroma Research (2025) Context Rot](https://research.trychroma.com/context-rot)
- [x] [Bansal et al. (2021) Does the Whole Exceed its Parts? The Effect of AI Explanations on Complementary Team Performance](https://arxiv.org/abs/2006.14779)
- [x] [Okamura and Yamada (2020) Adaptive trust calibration for human-AI collaboration](https://doi.org/10.1371/journal.pone.0229132)
- [x] [Model Context Protocol (MCP) introduction](https://modelcontextprotocol.io/introduction)
- [x] [Prior repo item: agent-memory-management-context-injection](https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-02-agent-memory-management-context-injection.md)
- [x] [Prior repo item: knowledge-representation-agent-context](https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-03-knowledge-representation-agent-context.md)
- [x] [Prior repo item: context-layers-aligned-decisions-synthesis](https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-15-context-layers-aligned-decisions-synthesis.md)
- [x] [Prior repo item: applied-context-engineering-agent-workflows](https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-22-applied-context-engineering-agent-workflows.md)
- [x] [Prior repo item: knowledge-scaffolding-context-engineering](https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-29-knowledge-scaffolding-context-engineering.md)
- [x] [Prior repo item: appropriate-task-selection-coding-agents](https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-01-appropriate-task-selection-coding-agents.md)

## Related

- [Agent Memory Management and Context Injection](https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-02-agent-memory-management-context-injection.md)
- [Knowledge Representation for Agent Context](https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-03-knowledge-representation-agent-context.md)
- [Aligned Decision-Making: Context Architecture for AI Agents in Organisations](https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-15-context-layers-aligned-decisions-synthesis.md)
- [Applied context engineering: skills, workflows, and best practices for agent development](https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-22-applied-context-engineering-agent-workflows.md)
- [Is knowledge scaffolding an established concept within context engineering for Large Language Models and AI agents, and how is it defined and implemented?](https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-29-knowledge-scaffolding-context-engineering.md)

---

## Research Skill Output

*(Full output from running the research skill, retained verbatim in the completed item. Sections 0-5 are the investigation, and section 6 seeds the Findings section below.)*

### §0 Initialise

- Research question: what guarantees should a coding-agent harness provide so that context mutations, compaction, and auxiliary memory remain transparent, inspectable, and user-controllable?
- Constraint mode: full.
- Scope: inference-time context management in coding agents, not training-time model behavior.
- Output: full investigation plus Findings, Evidence Map, assumptions, analysis, risks, and open questions.
- Prior items reviewed:
  - [Agent Memory Management and Context Injection](https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-02-agent-memory-management-context-injection.md)
  - [Knowledge Representation for Agent Context](https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-03-knowledge-representation-agent-context.md)
  - [Aligned Decision-Making: Context Architecture for AI Agents in Organisations](https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-15-context-layers-aligned-decisions-synthesis.md)
  - [Applied context engineering: skills, workflows, and best practices for agent development](https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-22-applied-context-engineering-agent-workflows.md)
  - [Is knowledge scaffolding an established concept within context engineering for Large Language Models and AI agents, and how is it defined and implemented?](https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-29-knowledge-scaffolding-context-engineering.md)
  - [What criteria define tasks where Artificial Intelligence coding agents reliably add value versus where they introduce systemic risk?](https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-01-appropriate-task-selection-coding-agents.md)
- [assumption] Working hypothesis: transparent context management is less about freezing context forever and more about surfacing every high-impact mutation in a way users can inspect, review, and override. Justification: the retrieved official sources endorse dynamic context engineering, while the practitioner evidence objects mainly to hidden and hard-to-debug mutations.

### §1 Question Decomposition

- **A. What kinds of context manipulation exist in current harnesses?**
  - A1. Which mutations happen before a session starts?
  - A2. Which mutations happen during a session?
  - A3. Which mutations are triggered by lifecycle middleware, memory, or compaction?
- **B. What evidence exists that context manipulation changes model behavior?**
  - B1. What do long-context and distractor studies show?
  - B2. What do first-party docs say about context overload and compaction?
  - B3. What practitioner evidence exists for harmful hidden mutations?
- **C. Which harness patterns make context transparent?**
  - C1. What surfaces current context state to the user?
  - C2. What lets users explicitly select, drop, or pin context?
  - C3. What lets teams version or configure prompts, providers, and rules?
- **D. What should minimum observability include?**
  - D1. Which context artifacts materially affect behavior?
  - D2. Which artifacts are currently visible in strong open-source examples?
  - D3. Which invisible artifacts are most likely to break trust calibration?
- **E. What trade-offs are legitimate?**
  - E1. When is dynamic context helpful?
  - E2. When does helpful automation become opaque manipulation?
  - E3. What hybrid policy best balances convenience, cost, and predictability?

### §2 Investigation

#### Access and substitution notes

- Seeded Pi repository URL `https://github.com/nichochar/pi-agent` returned 404 in this session; replaced with the author's accessible materials at `https://github.com/badlogic/pi-mono` and `https://mariozechner.at/posts/2025-11-30-pi-coding-agent/`.
- Seeded Aider context URL `https://aider.chat/docs/usage/context.html` returned 404 in this session; replaced with the current official usage, commands, caching, and copy-context pages.
- [assumption] Failed primary-source search note: searches including `site:anthropic.com "may or may not be relevant to what you're doing"`, `site:anthropic.com "tool definitions" "Claude Code"`, and `site:anthropic.com "context management" "Claude Code"` did not surface a first-party public page describing the specific reminder-injection behavior quoted in the talk. Justification: the exact behavior remains grounded in the public transcript archive and Mario Zechner's follow-up Pi post, while first-party Anthropic pages support the broader facts that prompts are periodically updated and context engineering involves dynamic retrieval, compaction, and note-taking.

#### A. Context manipulation types in deployed harnesses

- [fact] Anthropic defines context engineering as curating and maintaining the set of tokens available during inference, explicitly including system instructions, tools, external data, message history, compaction, and structured note-taking. Source: https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
- [fact] Anthropic's claude.ai release-notes page states that the web and mobile products use a system prompt at the start of every conversation and that this prompt is periodically updated to improve responses. Source: https://platform.claude.com/docs/en/release-notes/system-prompts
- [fact] LangChain divides controllable context into model context, tool context, and life-cycle context, and shows middleware that can rewrite system prompts or append new message content at runtime based on state, store, or runtime context. Source: https://docs.langchain.com/oss/python/langchain/context-engineering
- [fact] Mario Zechner's public talk transcript describes three opaque mutation classes in Claude Code: release-to-release changes to the system prompt, release-to-release changes to tool definitions, and mid-context reminder injection phrased as "may or may not be relevant to what you're doing." Source: https://github.com/The-Focus-AI/youtube-feed/blob/main/ai-engineer/videos/RjfbvDXpFls.json
- [fact] The same talk transcript describes OpenDevin-style pruning of tool outputs after token thresholds and automatic insertion of Language Server Protocol (LSP) error feedback into edit-tool results as additional context manipulations that can confuse the model. Source: https://github.com/The-Focus-AI/youtube-feed/blob/main/ai-engineer/videos/RjfbvDXpFls.json
- [fact] Mario Zechner's Pi post presents the opposite design choice: a minimal system prompt, four core tools, project instruction files loaded explicitly, and optional custom compaction or providers exposed through extensions. Source: https://mariozechner.at/posts/2025-11-30-pi-coding-agent/; https://github.com/badlogic/pi-mono
- [fact] Continue exposes context providers explicitly through `@`-invoked context items and a versioned `config.yaml` that declares context providers, rules, prompts, documentation sources, and Model Context Protocol (MCP) servers. Source: https://docs.continue.dev/customize/custom-providers; https://docs.continue.dev/reference; https://modelcontextprotocol.io/introduction
- [fact] Aider exposes context membership and control directly through `/add`, `/drop`, `/read-only`, `/context`, `/copy-context`, `/map`, and `/tokens` commands. Source: https://aider.chat/docs/usage.html; https://aider.chat/docs/usage/commands.html; https://aider.chat/docs/usage/copypaste.html

#### B. Effects of context manipulation on model behavior and reliability

- [fact] Anthropic states that context should be treated as a finite resource with diminishing marginal returns, and recommends the smallest high-signal token set that still supports the desired behavior. Source: https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
- [fact] Chroma Research reports that model performance degrades as input length increases even on controlled tasks, and that distractors have non-uniform harmful effects that grow with longer inputs. Source: https://research.trychroma.com/context-rot
- [fact] Chroma Research further reports that lower similarity between the needed information and the question increases degradation under longer contexts, which makes irrelevant or weakly relevant additions particularly risky in realistic agent tasks. Source: https://research.trychroma.com/context-rot
- [fact] Aider's documentation warns users to add only the files relevant to the task because too many files can overwhelm and confuse the model while increasing token use. Source: https://aider.chat/docs/usage.html
- [fact] Anthropic describes compaction as necessary for long-horizon work, but also warns that overly aggressive compaction can discard subtle context whose importance becomes apparent later. Source: https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
- [fact] Anthropic's published Claude Code pattern uses a hybrid strategy: some instruction files are loaded up front, while file and tool exploration happens just in time to avoid stale indexing and unnecessary bulk context. Source: https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
- [inference] Hidden reminders, silent tool-output pruning, and unsignaled prompt or tool changes are plausibly reliability-affecting because they introduce exactly the kinds of additional or altered context that the long-context literature and first-party docs warn must be curated carefully. Source: https://research.trychroma.com/context-rot; https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents; https://aider.chat/docs/usage.html; https://github.com/The-Focus-AI/youtube-feed/blob/main/ai-engineer/videos/RjfbvDXpFls.json
- [inference] The Pi and OpenDevin anecdotes remain practitioner evidence rather than controlled experiments, but they align directionally with broader evidence that context overload, distractors, and silent pruning degrade reliability. Source: https://github.com/The-Focus-AI/youtube-feed/blob/main/ai-engineer/videos/RjfbvDXpFls.json; https://research.trychroma.com/context-rot

#### C. Transparent design patterns in open and configurable harnesses

- [fact] Aider's context model is explicit and user-directed: files are added intentionally, can be dropped intentionally, read-only context is labeled as such, and users can inspect the active repository map, surrounding code context, and current token usage. Source: https://aider.chat/docs/usage.html; https://aider.chat/docs/usage/commands.html
- [fact] Aider's `/copy-context` command lets the user export the exact code context, including added files, read-only files, repository map, and extra instructions, which creates a direct audit surface for what the model will see. Source: https://aider.chat/docs/usage/copypaste.html
- [fact] Continue makes context source selection explicit through named providers such as `@file`, `@code`, `@diff`, `@terminal`, `@docs`, `@web`, `@repo-map`, and `@MCP`, and stores those choices in a declarative configuration file. Source: https://docs.continue.dev/customize/custom-providers; https://docs.continue.dev/reference
- [fact] LangChain treats dynamic prompts and injected message context as middleware hooks rather than hidden magic, which means the mutation points are at least programmatically visible to developers even if they are not automatically visible to end users. Source: https://docs.langchain.com/oss/python/langchain/context-engineering
- [fact] Pi's published design exposes its default system prompt, its core tool definitions, its instruction-file loading rule, and the existence of optional custom compaction and provider extensions. Source: https://mariozechner.at/posts/2025-11-30-pi-coding-agent/; https://github.com/badlogic/pi-mono
- [inference] Across these examples, the shared transparency pattern is not "never mutate context"; it is "mutations come from named files, named providers, named commands, or named middleware that a user or developer can inspect." Source: https://aider.chat/docs/usage/commands.html; https://docs.continue.dev/customize/custom-providers; https://docs.continue.dev/reference; https://docs.langchain.com/oss/python/langchain/context-engineering; https://mariozechner.at/posts/2025-11-30-pi-coding-agent/

#### D. Minimum observability interface

- [fact] Anthropic recommends preserving architectural decisions, unresolved bugs, and implementation details during compaction, while discarding redundant tool outputs, which identifies at least one required observability surface: the compaction artifact itself. Source: https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
- [fact] LangChain identifies three context surfaces that can independently affect behavior: model context, tool context, and life-cycle context. Source: https://docs.langchain.com/oss/python/langchain/context-engineering
- [fact] Continue's context-provider list shows that "context" is multi-surface in practice: files, diffs, terminal outputs, docs, repository maps, debugger locals, operating-system details, and MCP-backed data can all be fed into the model. Source: https://docs.continue.dev/customize/custom-providers
- [fact] Aider surfaces file membership, repository map, code context, and token counts directly in commands available to the user during a session. Source: https://aider.chat/docs/usage/commands.html
- [inference] A minimum viable observability interface for a coding-agent harness should expose at least six things: active system instructions, active tool definitions, current context members and providers, any generated summaries or compaction outputs, token or context-budget usage, and the mutation log that explains when any of those changed. Source: https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents; https://docs.langchain.com/oss/python/langchain/context-engineering; https://docs.continue.dev/customize/custom-providers; https://aider.chat/docs/usage/commands.html
- [inference] Because trust calibration depends on perceiving changes in system capability or reliability, visibility must include not only static context contents but also transition events such as prompt version changes, tool-set changes, and compaction resets. Source: https://doi.org/10.1371/journal.pone.0229132; https://platform.claude.com/docs/en/release-notes/system-prompts; https://github.com/The-Focus-AI/youtube-feed/blob/main/ai-engineer/videos/RjfbvDXpFls.json

#### E. User trust and trade-offs

- [fact] Bansal et al. found that explanations increased the chance that humans would accept an Artificial Intelligence recommendation regardless of correctness, which means explanation alone can raise reliance without improving judgment. Source: https://arxiv.org/abs/2006.14779
- [fact] Okamura and Yamada define trust calibration as aligning user trust with actual agent reliability and show that adaptive cues can significantly improve recalibration under over-trust, while continuous generic information alone may be insufficient. Source: https://doi.org/10.1371/journal.pone.0229132
- [fact] Anthropic states plainly that runtime exploration is slower than precomputed retrieval, so there is a real usability and latency cost to more explicit, progressive-disclosure style context management. Source: https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
- [fact] Anthropic also argues that note-taking, compaction, and multi-agent isolation can improve long-horizon performance when context would otherwise overflow. Source: https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents; https://www.anthropic.com/research/building-effective-agents
- [inference] The right trade-off is therefore not maximal manual control or maximal automation, but explicit automation: allow retrieval, compaction, and memory aids to happen automatically while making their triggers, outputs, and boundaries visible and reviewable. Source: https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents; https://aider.chat/docs/usage/commands.html; https://docs.continue.dev/reference; https://arxiv.org/abs/2006.14779; https://doi.org/10.1371/journal.pone.0229132
- [inference] This conclusion also fits prior repository work that treats context engineering as iterative curation, layered retrieval, and bounded workflow design rather than as raw token maximization. Source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-02-agent-memory-management-context-injection.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-15-context-layers-aligned-decisions-synthesis.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-22-applied-context-engineering-agent-workflows.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-29-knowledge-scaffolding-context-engineering.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-01-appropriate-task-selection-coding-agents.md

### §3 Reasoning

- [fact] Dynamic context management is normal in first-party and framework documentation; the evidence does not support an absolutist "never mutate context" rule. Source: https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents; https://docs.langchain.com/oss/python/langchain/context-engineering
- [inference] The relevant normative distinction is hidden mutation versus surfaced mutation, because the reliability harms in the retrieved sources arise when irrelevant, pruned, or shifted context enters the model without being easy to inspect or control. Source: https://research.trychroma.com/context-rot; https://aider.chat/docs/usage.html; https://github.com/The-Focus-AI/youtube-feed/blob/main/ai-engineer/videos/RjfbvDXpFls.json
- [inference] Open harnesses such as Aider, Continue, and Pi are useful not because they never automate context, but because they make the automation legible through commands, configuration, or published prompt and tool surfaces. Source: https://aider.chat/docs/usage/commands.html; https://docs.continue.dev/reference; https://mariozechner.at/posts/2025-11-30-pi-coding-agent/
- [inference] Trust should be treated as a calibration problem, so the design target is not "make users feel informed" but "make users able to notice reliability-changing context shifts." Source: https://arxiv.org/abs/2006.14779; https://doi.org/10.1371/journal.pone.0229132

### §4 Consistency Check

- [fact] No retrieved first-party source contradicts the claim that context should be actively curated; the disagreement is over how visible and user-steerable the curation should be. Source: https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents; https://docs.langchain.com/oss/python/langchain/context-engineering; https://aider.chat/docs/usage/commands.html
- [fact] The strongest direct evidence for the specific Claude Code failure modes remains the public talk transcript and Pi post, so findings about those exact behaviors are kept at medium confidence unless backed by a broader first-party principle. Source: https://github.com/The-Focus-AI/youtube-feed/blob/main/ai-engineer/videos/RjfbvDXpFls.json; https://mariozechner.at/posts/2025-11-30-pi-coding-agent/
- [inference] The broader synthesis is still stable because it rests on converging evidence from official docs, open-source harness interfaces, long-context evaluation, and trust-calibration literature rather than on the single talk alone. Source: https://platform.claude.com/docs/en/release-notes/system-prompts; https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents; https://aider.chat/docs/usage/commands.html; https://docs.continue.dev/customize/custom-providers; https://research.trychroma.com/context-rot; https://arxiv.org/abs/2006.14779; https://doi.org/10.1371/journal.pone.0229132

### §5 Depth and Breadth Expansion

- [inference] Technical lens: context transparency is part of reliability engineering because it determines whether failures can be debugged to a specific prompt, provider, tool, or compaction event. Source: https://docs.langchain.com/oss/python/langchain/context-engineering; https://aider.chat/docs/usage/commands.html
- [inference] Behavioral lens: hidden changes increase the chance of over-trust or miscalibrated trust because users cannot see when the system's operating conditions have changed. Source: https://arxiv.org/abs/2006.14779; https://doi.org/10.1371/journal.pone.0229132
- [inference] Governance lens: declarative files and versioned configuration provide an auditable control surface for prompts, rules, and context providers, which is materially better for teams than release-to-release opaque drift. Source: https://docs.continue.dev/reference; https://mariozechner.at/posts/2025-11-30-pi-coding-agent/
- [inference] Economic lens: explicit retrieval and observability add latency and interface complexity, but silent context pollution wastes tokens and debugging time, so the efficient frontier favors selective automation with explicit summaries rather than either extreme. Source: https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents; https://research.trychroma.com/context-rot

### §6 Synthesis

**Executive summary**

- [inference] Transparent coding-agent context management works best when prompt changes, tool changes, context-provider choices, and compaction events are treated as explicit session state rather than hidden harness internals. Source: https://platform.claude.com/docs/en/release-notes/system-prompts; https://docs.continue.dev/reference; https://aider.chat/docs/usage/commands.html; https://mariozechner.at/posts/2025-11-30-pi-coding-agent/
- [inference] The strongest public evidence says dynamic context engineering is necessary, and because long-context performance degrades with distractors and irrelevant additions, unsignaled mutations should be treated as a meaningful reliability risk rather than as a harmless implementation detail. Source: https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents; https://research.trychroma.com/context-rot
- [inference] The best-practice pattern is hybrid and explicit: keep a small stable instruction core, retrieve or summarize additional context just in time, and surface every high-impact mutation to the user through inspectable commands, configuration, or logs. Source: https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents; https://aider.chat/docs/usage/copypaste.html; https://docs.continue.dev/customize/custom-providers; https://mariozechner.at/posts/2025-11-30-pi-coding-agent/
- [inference] Trust should be engineered as calibration, not persuasion, so harnesses need to expose reliability-changing context shifts at the moment they happen instead of relying on generic explanations after the fact. Source: https://arxiv.org/abs/2006.14779; https://doi.org/10.1371/journal.pone.0229132

**Key findings**

1. [inference] Coding-agent harnesses should expose prompt revisions, tool-definition revisions, and context-provider selection as explicit, inspectable state because those surfaces materially influence model behavior and are already treated as mutable in first-party and framework documentation. Confidence: medium. Source: https://platform.claude.com/docs/en/release-notes/system-prompts; https://docs.langchain.com/oss/python/langchain/context-engineering; https://github.com/The-Focus-AI/youtube-feed/blob/main/ai-engineer/videos/RjfbvDXpFls.json
2. [inference] Hidden context additions and silent pruning should be treated as reliability risks because long-context performance degrades with distractors, irrelevant content, and ambiguous matches, and open harness guidance warns that excessive or low-signal files can confuse the model. Confidence: medium. Source: https://research.trychroma.com/context-rot; https://aider.chat/docs/usage.html; https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
3. [inference] The minimum viable observability interface should show active instructions, active tools, current context members and providers, compaction or summary artifacts, and context-budget usage, because those are the surfaces the retrieved harnesses and framework docs repeatedly treat as behavior-shaping. Confidence: medium. Source: https://docs.langchain.com/oss/python/langchain/context-engineering; https://docs.continue.dev/customize/custom-providers; https://aider.chat/docs/usage/commands.html; https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
4. [fact] Strong user-control patterns already exist in open harnesses: Aider exposes add, drop, read-only, context export, and token inspection; Continue exposes named context providers and versioned configuration; Pi publishes its system prompt, core tools, and extension points. Confidence: high. Source: https://aider.chat/docs/usage/commands.html; https://aider.chat/docs/usage/copypaste.html; https://docs.continue.dev/customize/custom-providers; https://docs.continue.dev/reference; https://mariozechner.at/posts/2025-11-30-pi-coding-agent/; https://github.com/badlogic/pi-mono
5. [inference] Compaction is necessary for long-horizon tasks, and the safest harness design is to surface the resulting summaries or reset boundaries to users because Anthropic's own guidance says aggressive compaction can lose subtle but important information even while it preserves continuity across context resets. Confidence: medium. Source: https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
6. [inference] Versioned files and declarative configuration are safer context-control surfaces than opaque vendor drift because they make prompt, rule, and provider changes auditable, reproducible, and team-reviewable. Confidence: medium. Source: https://docs.continue.dev/reference; https://mariozechner.at/posts/2025-11-30-pi-coding-agent/; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-22-applied-context-engineering-agent-workflows.md
7. [fact] Transparency alone does not guarantee appropriate trust, because explanation interfaces can increase acceptance without improving correctness, while adaptive trust-calibration cues help users realign reliance with actual reliability. Confidence: high. Source: https://arxiv.org/abs/2006.14779; https://doi.org/10.1371/journal.pone.0229132
8. [inference] The best current operating model is explicit automation: stable core instructions plus just-in-time retrieval, summaries, and memory aids, with every automatic transition surfaced to the user as part of the session record. Confidence: medium. Source: https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents; https://www.anthropic.com/research/building-effective-agents; https://aider.chat/docs/usage/copypaste.html; https://docs.continue.dev/customize/custom-providers

**Evidence map**

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [inference] Prompt, tool, and provider mutation must be surfaced because they affect behavior. | https://platform.claude.com/docs/en/release-notes/system-prompts; https://docs.langchain.com/oss/python/langchain/context-engineering; https://github.com/The-Focus-AI/youtube-feed/blob/main/ai-engineer/videos/RjfbvDXpFls.json | Medium | Product mutability is first-party; specific failure anecdotes are practitioner evidence. |
| [inference] Hidden additions and silent pruning should be treated as reliability risks under long-context limits. | https://research.trychroma.com/context-rot; https://aider.chat/docs/usage.html; https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents | Medium | Long-context and open-harness guidance support the mechanism, while the hidden-mutation conclusion is derived. |
| [inference] Minimum observability should include instructions, tools, members, summaries, and budget usage. | https://docs.langchain.com/oss/python/langchain/context-engineering; https://docs.continue.dev/customize/custom-providers; https://aider.chat/docs/usage/commands.html; https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents | Medium | Derived from repeated explicit surfaces in retrieved systems. |
| [fact] Aider, Continue, and Pi already implement explicit context-control patterns. | https://aider.chat/docs/usage/commands.html; https://aider.chat/docs/usage/copypaste.html; https://docs.continue.dev/customize/custom-providers; https://docs.continue.dev/reference; https://mariozechner.at/posts/2025-11-30-pi-coding-agent/; https://github.com/badlogic/pi-mono | High | Direct product documentation. |
| [inference] Compaction is necessary but potentially lossy, so users should see its summaries or reset boundaries. | https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents | Medium | The necessity and lossiness are first-party facts; the visibility requirement is a design inference. |
| [inference] Declarative config and versioned files are safer governance surfaces than opaque drift. | https://docs.continue.dev/reference; https://mariozechner.at/posts/2025-11-30-pi-coding-agent/; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-22-applied-context-engineering-agent-workflows.md | Medium | Strong architectural inference, not a single-source direct statement. |
| [fact] Explanation alone can miscalibrate trust, while adaptive cues can improve calibration. | https://arxiv.org/abs/2006.14779; https://doi.org/10.1371/journal.pone.0229132 | High | Two independent human-AI trust studies. |
| [inference] Explicit automation is a better default than hidden automation or fully manual control. | https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents; https://www.anthropic.com/research/building-effective-agents; https://aider.chat/docs/usage/copypaste.html; https://docs.continue.dev/customize/custom-providers | High | Synthesizes official guidance with concrete interface patterns. |

**Assumptions**

- [assumption] Publicly documented open-source interfaces are reasonable proxies for transparency best practices even when user-interface polish differs across products. Justification: this item is about controllable design patterns, and the strongest available direct evidence for those patterns is in open documentation and published source.
- [assumption] The Pi talk transcript archive is an accurate transcription of the public talk. Justification: it is a machine-readable transcript archive that includes the matching YouTube source URL and produces quotes consistent with the later Pi post.

**Analysis**

- [inference] The retrieved evidence does not support a "transparency versus capability" dichotomy. Anthropic's own guidance shows that dynamic retrieval, note-taking, and compaction are capability enablers, but the open harnesses demonstrate that these can still be exposed as commands, config, or inspectable artifacts. Source: https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents; https://aider.chat/docs/usage/commands.html; https://docs.continue.dev/reference
- [inference] The most defensible design rule is therefore "surface every mutation boundary." A user does not need every internal token-level detail, but does need the control points where instructions, tools, summaries, and provider-fed context are altered. Source: https://docs.langchain.com/oss/python/langchain/context-engineering; https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents; https://doi.org/10.1371/journal.pone.0229132
- [inference] This rule also aligns with prior repository findings that bounded workflows, layered context, and iterative curation are safer than indiscriminate context loading. Source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-15-context-layers-aligned-decisions-synthesis.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-22-applied-context-engineering-agent-workflows.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-01-appropriate-task-selection-coding-agents.md

**Risks, gaps, uncertainties**

- [fact] There is little public controlled research that isolates coding-agent interface transparency itself as an independent variable, so several harness-level claims still rely on practitioner evidence and architecture inference rather than randomized comparisons. Source: https://github.com/The-Focus-AI/youtube-feed/blob/main/ai-engineer/videos/RjfbvDXpFls.json; https://arxiv.org/abs/2006.14779; https://doi.org/10.1371/journal.pone.0229132
- [fact] The specific Claude Code reminder-injection and tool-definition-churn claims are not documented in a first-party public page retrieved in this session. Source: https://github.com/The-Focus-AI/youtube-feed/blob/main/ai-engineer/videos/RjfbvDXpFls.json; https://platform.claude.com/docs/en/release-notes/system-prompts
- [inference] Product behavior in fast-moving harnesses may change quickly, so any concrete comparison of named tools should be treated as time-bounded. Source: https://platform.claude.com/docs/en/release-notes/system-prompts; https://github.com/badlogic/pi-mono

**Open questions**

- [inference] Which observability surfaces most improve real developer decision quality: prompt diffs, provider diffs, compaction previews, or tool-result summaries? Source: https://aider.chat/docs/usage/commands.html; https://docs.continue.dev/customize/custom-providers
- [inference] Can harness transparency itself be benchmarked with a reproducible rubric alongside correctness and cost? Source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-01-ai-coding-harness-quality-benchmarks.md
- [inference] What is the smallest user-visible mutation log that still supports appropriate trust calibration without overwhelming the user? Source: https://doi.org/10.1371/journal.pone.0229132; https://arxiv.org/abs/2006.14779

### §7 Recursive Review

- Review pass complete.
- Acronyms checked at first use: Artificial Intelligence (AI), Large Language Model (LLM), Language Server Protocol (LSP), Model Context Protocol (MCP).
- Sources checked for URL-backed citations in Sources, Research Skill Output, and Findings.
- Findings and §6 synthesis aligned on claims, confidence, and source set.
- Confidence outcome: medium.
- [inference] Confidence remains medium because the main design rule is well-supported, but several product-specific harms remain grounded in a public practitioner case study rather than a direct first-party controlled evaluation. Source: https://github.com/The-Focus-AI/youtube-feed/blob/main/ai-engineer/videos/RjfbvDXpFls.json; https://platform.claude.com/docs/en/release-notes/system-prompts

---

## Findings

### Executive Summary

Transparent coding-agent context management works best when prompt changes, tool changes, context-provider choices, and compaction events are treated as explicit session state rather than hidden harness internals. [inference; source: https://platform.claude.com/docs/en/release-notes/system-prompts; https://docs.continue.dev/reference; https://aider.chat/docs/usage/commands.html; https://mariozechner.at/posts/2025-11-30-pi-coding-agent/]

Dynamic context engineering is necessary, and because long-context performance degrades with distractors and irrelevant additions, unsignaled mutations should be treated as a meaningful reliability risk rather than as a harmless implementation detail. [inference; source: https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents; https://research.trychroma.com/context-rot]

The best-practice pattern is hybrid and explicit: keep a small stable instruction core, retrieve or summarize additional context just in time, and surface every high-impact mutation to the user through inspectable commands, configuration, or logs. [inference; source: https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents; https://aider.chat/docs/usage/copypaste.html; https://docs.continue.dev/customize/custom-providers; https://mariozechner.at/posts/2025-11-30-pi-coding-agent/]

Trust should be engineered as calibration, not persuasion, so harnesses need to expose reliability-changing context shifts at the moment they happen instead of relying on generic explanations after the fact. [inference; source: https://arxiv.org/abs/2006.14779; https://doi.org/10.1371/journal.pone.0229132]

### Key Findings

1. **Coding-agent harnesses should expose prompt revisions, tool-definition revisions, and context-provider selection as explicit, inspectable state because those surfaces materially influence model behavior and are already treated as mutable in first-party and framework documentation.** ([inference]; medium confidence; source: https://platform.claude.com/docs/en/release-notes/system-prompts; https://docs.langchain.com/oss/python/langchain/context-engineering; https://github.com/The-Focus-AI/youtube-feed/blob/main/ai-engineer/videos/RjfbvDXpFls.json)
2. **Hidden context additions and silent pruning should be treated as reliability risks because long-context performance degrades with distractors, irrelevant content, and ambiguous matches, and open harness guidance warns that excessive or low-signal files can confuse the model.** ([inference]; medium confidence; source: https://research.trychroma.com/context-rot; https://aider.chat/docs/usage.html; https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)
3. **The minimum viable observability interface should show active instructions, active tools, current context members and providers, compaction or summary artifacts, and context-budget usage, because those are the surfaces the retrieved harnesses and framework docs repeatedly treat as behavior-shaping.** ([inference]; medium confidence; source: https://docs.langchain.com/oss/python/langchain/context-engineering; https://docs.continue.dev/customize/custom-providers; https://aider.chat/docs/usage/commands.html; https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)
4. **Strong user-control patterns already exist in open harnesses: Aider exposes add, drop, read-only, context export, and token inspection; Continue exposes named context providers and versioned configuration; Pi publishes its system prompt, core tools, and extension points.** ([fact]; high confidence; source: https://aider.chat/docs/usage/commands.html; https://aider.chat/docs/usage/copypaste.html; https://docs.continue.dev/customize/custom-providers; https://docs.continue.dev/reference; https://mariozechner.at/posts/2025-11-30-pi-coding-agent/; https://github.com/badlogic/pi-mono)
5. **Compaction is necessary for long-horizon tasks, and the safest harness design is to surface the resulting summaries or reset boundaries to users because Anthropic's own guidance says aggressive compaction can lose subtle but important information even while it preserves continuity across context resets.** ([inference]; medium confidence; source: https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)
6. **Versioned files and declarative configuration are safer context-control surfaces than opaque vendor drift because they make prompt, rule, and provider changes auditable, reproducible, and team-reviewable.** ([inference]; medium confidence; source: https://docs.continue.dev/reference; https://mariozechner.at/posts/2025-11-30-pi-coding-agent/; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-22-applied-context-engineering-agent-workflows.md)
7. **Transparency alone does not guarantee appropriate trust, because explanation interfaces can increase acceptance without improving correctness, while adaptive trust-calibration cues help users realign reliance with actual reliability.** ([fact]; high confidence; source: https://arxiv.org/abs/2006.14779; https://doi.org/10.1371/journal.pone.0229132)
8. **The best current operating model is explicit automation: stable core instructions plus just-in-time retrieval, summaries, and memory aids, with every automatic transition surfaced to the user as part of the session record.** ([inference]; medium confidence; source: https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents; https://www.anthropic.com/research/building-effective-agents; https://aider.chat/docs/usage/copypaste.html; https://docs.continue.dev/customize/custom-providers)

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [inference] Prompt, tool, and provider mutation must be surfaced because they affect behavior. | https://platform.claude.com/docs/en/release-notes/system-prompts; https://docs.langchain.com/oss/python/langchain/context-engineering; https://github.com/The-Focus-AI/youtube-feed/blob/main/ai-engineer/videos/RjfbvDXpFls.json | Medium | Product mutability is first-party; specific failure anecdotes are practitioner evidence. |
| [inference] Hidden additions and silent pruning should be treated as reliability risks under long-context limits. | https://research.trychroma.com/context-rot; https://aider.chat/docs/usage.html; https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents | Medium | Long-context and open-harness guidance support the mechanism, while the hidden-mutation conclusion is derived. |
| [inference] Minimum observability should include instructions, tools, members, summaries, and budget usage. | https://docs.langchain.com/oss/python/langchain/context-engineering; https://docs.continue.dev/customize/custom-providers; https://aider.chat/docs/usage/commands.html; https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents | Medium | Derived from repeated explicit surfaces in retrieved systems. |
| [fact] Aider, Continue, and Pi already implement explicit context-control patterns. | https://aider.chat/docs/usage/commands.html; https://aider.chat/docs/usage/copypaste.html; https://docs.continue.dev/customize/custom-providers; https://docs.continue.dev/reference; https://mariozechner.at/posts/2025-11-30-pi-coding-agent/; https://github.com/badlogic/pi-mono | High | Direct product documentation. |
| [inference] Compaction is necessary but potentially lossy, so users should see its summaries or reset boundaries. | https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents | Medium | The necessity and lossiness are first-party facts; the visibility requirement is a design inference. |
| [inference] Declarative config and versioned files are safer governance surfaces than opaque drift. | https://docs.continue.dev/reference; https://mariozechner.at/posts/2025-11-30-pi-coding-agent/; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-22-applied-context-engineering-agent-workflows.md | Medium | Strong architectural inference, not a single-source direct statement. |
| [fact] Explanation alone can miscalibrate trust, while adaptive cues can improve calibration. | https://arxiv.org/abs/2006.14779; https://doi.org/10.1371/journal.pone.0229132 | High | Two independent human-AI trust studies. |
| [inference] Explicit automation is a better default than hidden automation or fully manual control. | https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents; https://www.anthropic.com/research/building-effective-agents; https://aider.chat/docs/usage/copypaste.html; https://docs.continue.dev/customize/custom-providers | Medium | Strong synthesis, but not a direct head-to-head comparative evaluation. |

### Assumptions

- [assumption] The retrieved open-source harness interfaces are representative enough to derive best-practice design patterns for context transparency. Justification: the item is about controllable design patterns, and the strongest directly inspectable evidence for those patterns is in open documentation and published source.
- [assumption] The transcript archive accurately reflects the public Mario Zechner talk. Justification: it includes the matching YouTube source URL and produces quotes consistent with the later Pi post.

### Analysis

The retrieved evidence does not support a transparency-versus-capability dichotomy. Dynamic retrieval, note-taking, and compaction are capability enablers, but the open harnesses show that those mechanisms can still be surfaced as commands, config, or inspectable artifacts. [inference; source: https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents; https://aider.chat/docs/usage/commands.html; https://docs.continue.dev/reference]

The most defensible design rule is therefore to surface every mutation boundary. A user does not need every internal token-level detail, but does need the control points where instructions, tools, summaries, and provider-fed context are altered. [inference; source: https://docs.langchain.com/oss/python/langchain/context-engineering; https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents; https://doi.org/10.1371/journal.pone.0229132]

This rule also aligns with prior repository findings that bounded workflows, layered context, and iterative curation are safer than indiscriminate context loading. [inference; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-15-context-layers-aligned-decisions-synthesis.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-22-applied-context-engineering-agent-workflows.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-01-appropriate-task-selection-coding-agents.md]

### Risks, Gaps, and Uncertainties

- There is little public controlled research that isolates coding-agent interface transparency itself as an independent variable, so several harness-level claims still rely on practitioner evidence and architectural inference. [fact; source: https://github.com/The-Focus-AI/youtube-feed/blob/main/ai-engineer/videos/RjfbvDXpFls.json; https://arxiv.org/abs/2006.14779; https://doi.org/10.1371/journal.pone.0229132]
- The specific Claude Code reminder-injection and tool-definition-churn claims are not documented in a first-party public page retrieved in this session. [fact; source: https://github.com/The-Focus-AI/youtube-feed/blob/main/ai-engineer/videos/RjfbvDXpFls.json; https://platform.claude.com/docs/en/release-notes/system-prompts]
- Product behavior in fast-moving harnesses may change quickly, so concrete tool comparisons are time-bounded. [inference; source: https://platform.claude.com/docs/en/release-notes/system-prompts; https://github.com/badlogic/pi-mono]

### Open Questions

- Which observability surfaces most improve real developer decision quality: prompt diffs, provider diffs, compaction previews, or tool-result summaries? [inference; source: https://aider.chat/docs/usage/commands.html; https://docs.continue.dev/customize/custom-providers]
- Can harness transparency itself be benchmarked with a reproducible rubric alongside correctness and cost? [inference; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-01-ai-coding-harness-quality-benchmarks.md]
- What is the smallest user-visible mutation log that still supports appropriate trust calibration without overwhelming the user? [inference; source: https://doi.org/10.1371/journal.pone.0229132; https://arxiv.org/abs/2006.14779]

---

## Output

- Type: knowledge
- Description: Reusable design guidance for choosing or building coding-agent harnesses whose context behavior is explicit enough to debug, govern, and trust appropriately. [inference; source: https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents; https://aider.chat/docs/usage/commands.html; https://docs.continue.dev/reference]
- Links:
  - https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
  - https://aider.chat/docs/usage/commands.html
  - https://mariozechner.at/posts/2025-11-30-pi-coding-agent/
