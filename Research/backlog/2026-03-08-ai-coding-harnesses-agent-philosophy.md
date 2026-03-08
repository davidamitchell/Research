---
title: "AI coding harnesses: agent execution model, memory, and context management across commercial and OSS tools"
added: 2026-03-08
status: backlog
priority: high
blocks: []
tags: [ai-agents, coding, ide, anthropic, openai, cursor, opencode, aider, cline, context-management, memory, state-management, oss]
started: ~
completed: ~
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

- [ ] https://youtu.be/09sFAO7pklo — primary jump-off point (agent philosophy talk)
- [ ] https://www.anthropic.com/research/building-effective-agents — Anthropic "Building effective agents" (Dec 2024)
- [ ] https://docs.anthropic.com/en/docs/build-with-claude/computer-use — Anthropic computer use documentation
- [ ] https://modelspec.anthropic.com — Anthropic Model Spec (operator/user/assistant hierarchy)
- [ ] https://platform.openai.com/docs/guides/agents — OpenAI Agents documentation
- [ ] https://openai.com/index/openai-codex — OpenAI Codex agent design
- [ ] https://cursor.com/blog — Cursor blog (agent mode philosophy)
- [ ] https://docs.github.com/en/copilot/using-github-copilot/using-github-copilot-in-your-ide/using-copilot-edits — GitHub Copilot agent/edits mode
- [ ] https://github.com/sst/opencode — Opencode OSS terminal coding agent (README, architecture, changelog)
- [ ] https://ampcode.com — AMP by Sourcegraph (docs and blog)
- [ ] https://aider.chat — Aider: AI pair programming in the terminal (design philosophy, docs)
- [ ] https://github.com/cline/cline — Cline: autonomous coding agent for VS Code (README, docs, GitHub issues)
- [ ] https://continue.dev/docs — Continue.dev OSS coding assistant (architecture docs)
- [ ] https://zed.dev/blog — Zed AI (blog posts on agent and assistant design)
- [ ] Any arXiv papers cited in the primary video

---

## Research Skill Output

*(Full output from running the research skill — retained verbatim in the completed item. §§0–5 are the investigation; §6 seeds the Findings section below.)*

### §0 Initialise

Restate the research question. Confirm scope, constraints, and output format.

-

### §1 Question Decomposition

Approach sub-questions broken into atomic questions — each answerable with a single evidence-based claim.

-

### §2 Investigation

Evidence gathered per atomic question. Label each claim: **[fact]**, **[inference]**, or **[assumption]** with source.

-

### §3 Reasoning

Facts, inferences, and assumptions explicitly separated. No unsupported generalisations or narrative leaps.

-

### §4 Consistency Check

Internal contradictions identified and resolved (or explicitly flagged where unresolvable).

-

### §5 Depth and Breadth Expansion

Findings re-examined through relevant lenses (technical, regulatory, economic, historical, behavioural).

-

### §6 Synthesis

*(This section seeds the Findings below.)*

**Executive summary:**

**Key findings:**

**Evidence map:**

**Assumptions:**

**Analysis:**

**Risks, gaps, uncertainties:**

**Open questions:**

### §7 Recursive Review

Final pass: every section justified, all threads synthesised, every claim sourced or labelled, all uncertainties explicit.

-

---

## Findings

*(Populated from §6 Synthesis above.)*

### Executive Summary

3–5 sentences. What is the answer to the research question? State the key conclusion directly.

### Key Findings

Ordered list. Each finding is a specific, evidence-backed claim.

1.
2.

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| | | high / medium / low | |

### Assumptions

Explicit assumptions made during the investigation and the justification for each.

- **Assumption:** ... **Justification:** ...

### Analysis

How the evidence was weighed, what trade-offs were identified, and how competing interpretations were resolved.

### Risks, Gaps, and Uncertainties

What is still unknown? Where does the evidence fall short? What could change the conclusion?

-

### Open Questions

Questions that surfaced during research but are out of scope for this item. Each may become a new backlog item.

-

---

## Output

*(Fill in when completing — what was produced as a result of this research?)*

- Type: knowledge
- Description:
- Links:
