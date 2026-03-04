---
title: "Emergent Patterns in Software Engineering Prompts and SDLC Guidance"
added: 2026-03-04
status: in-progress
priority: high
blocks: []
tags: [ai-agents, prompts, sdlc, software-engineering, best-practices, prompt-engineering, developer-tooling]
started: 2026-03-04
completed: ~
output: [knowledge, backlog-item]
---

# Emergent Patterns in Software Engineering Prompts and SDLC Guidance

## Research Question

What are the current and emergent best practices for crafting AI agent prompts and tooling guidance tailored to each phase of the Software Development Life Cycle (SDLC) — covering discovery, requirements, design, planning, building, testing, reviewing, and iteration — and how can a structured prompt framework improve AI-assisted SDLC efficiency?

## Scope

**In scope:**
- Prompt patterns and strategies for each SDLC phase: Discovery/Research, Requirements, Design, Planning, Building, Testing, Reviewing, Iteration/Loop
- Best practices for structuring AI agent prompts in software engineering contexts (role prompting, chain-of-thought, few-shot, structured output)
- Emergent and adopted strategies from practitioner communities (GitHub Copilot Workspace, Cursor, Aider, Claude Code, etc.)
- Aligned tooling approaches that provide precise, actionable phase-specific guidance
- Practical examples and templates/frameworks from real-world implementations
- Mapping of AI-assisted systems to SDLC efficiency gains

**Out of scope:**
- LLM pre-training, fine-tuning, or model selection (covered by AI strategy items)
- Infrastructure for deploying AI coding tools at enterprise scale
- Non-software domains (e.g., prompt engineering for marketing or customer service)
- Deep evaluation of specific IDE plugins or vendor products

**Constraints:** Focus on evidence grounded in practitioner publications, open-source tooling documentation, research papers, and well-documented real-world implementations. Recency matters — prioritise 2023–2025 sources.

## Context

AI coding assistants and agents are now integrated into every major IDE and development workflow. However, the quality and specificity of prompts used at each SDLC phase varies enormously. Ad hoc prompting leads to inconsistent outputs, missed context, and hallucinated code. The opportunity is to establish structured, phase-aware prompt patterns that:

1. Give agents the right context at the right phase (e.g., requirements elicitation prompts differ fundamentally from code review prompts)
2. Enable tooling to provide automatic, phase-specific guidance rather than relying on individual developers to craft good prompts
3. Encode emergent community practices into reusable, shareable templates

This item directly supports the `davidamitchell/Skills` submodule, which provides agent skills for this repository and may be extended with SDLC-phase-specific skills.

## Approach

1. **SDLC phase taxonomy** — Define the eight target phases clearly (Discovery, Requirements, Design, Planning, Building, Testing, Reviewing, Iteration) and the key AI tasks within each phase (e.g., in Testing: generate unit tests, generate edge-case scenarios, review test coverage, mutate tests).

2. **Prompt pattern survey** — Survey existing prompt engineering literature and practitioner guides for patterns applicable to each SDLC phase:
   - Role/persona prompting (e.g., "Act as a senior security reviewer…")
   - Chain-of-thought and structured reasoning prompts
   - Few-shot examples for code generation and review
   - Constraint-framing prompts for requirements and design
   - Iterative/loop prompts for refinement

3. **Emergent strategies in production** — Investigate how leading tools and communities have operationalised phase-aware prompting:
   - GitHub Copilot Workspace (phase-aware task decomposition)
   - Cursor (context-window management, codebase-aware prompts)
   - Claude Code / Copilot Coding Agent (skills, AGENTS.md, structured instructions)
   - Aider (commit-oriented prompting)
   - OpenAI Codex successor patterns

4. **Tooling alignment** — Research how tooling can encode prompt guidance:
   - `.github/copilot-instructions.md`, `AGENTS.md`, `.cursorrules`, `.aider.conf` as persistent context files
   - MCP (Model Context Protocol) servers as tooling scaffolds
   - CI/CD-integrated review prompts (automated PR review, test generation triggers)

5. **Template/framework construction** — Draft a structured framework mapping prompt types to SDLC phases, with example prompts for each phase and guidance on when to use each pattern.

6. **Efficiency mapping** — Synthesise evidence on where AI-assisted prompting has measurably improved SDLC outcomes (velocity, defect rates, review quality) and where gaps remain.

## Sources

- [ ] GitHub Blog — "GitHub Copilot Workspace: Welcome to the beginning of a new era": https://github.blog/news-insights/product-news/github-copilot-workspace/
- [ ] Anthropic — "Claude's extended thinking": https://docs.anthropic.com/en/docs/build-with-claude/extended-thinking
- [ ] OpenAI — Prompt engineering guide: https://platform.openai.com/docs/guides/prompt-engineering
- [ ] Google DeepMind — "Gemini for Google Workspace" developer guide
- [ ] Wei et al. — "Chain-of-Thought Prompting Elicits Reasoning in Large Language Models" (2022): https://arxiv.org/abs/2201.11903
- [ ] White et al. — "A Prompt Pattern Catalog to Enhance Prompt Engineering with ChatGPT" (2023): https://arxiv.org/abs/2302.11382
- [ ] Cursor documentation — rules for AI, context management: https://docs.cursor.com
- [ ] Aider documentation — best practices for prompting: https://aider.chat/docs/
- [ ] Microsoft — "The Rise and Potential of Large Language Model Based Agents: A Survey" (2023): https://arxiv.org/abs/2309.07864
- [ ] Vaithilingam et al. — "Expectation vs. Experience: Evaluating the Usability of Code Generation Tools" (CHI 2022)
- [ ] Barke et al. — "Grounded Copilot: How Programmers Interact with Code-Generating Models" (OOPSLA 2023): https://arxiv.org/abs/2206.15000
- [ ] Peng et al. — "The Impact of AI on Developer Productivity: Evidence from GitHub Copilot" (2023): https://arxiv.org/abs/2302.06590
- [ ] DORA — State of DevOps Report 2024 (AI and software delivery performance)
- [ ] Thoughtworks Technology Radar — AI-assisted development entries (2023–2024)
- [ ] Stack Overflow Developer Survey 2024 — AI tool usage in development workflows
- [ ] `AGENTS.md` — this repo's own structured agent instructions as a real-world example
- [ ] `.github/mcp.json` — MCP server configuration as tooling alignment example
- [ ] `Research/completed/` — prior research on agent skills and output types

---

## Findings

*(Fill in when completing. Follow the research skill synthesis structure.)*

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

- How do phase-specific prompt patterns interact with context-window constraints in long-running agent sessions?
- What is the optimal granularity for SDLC phase decomposition in an autonomous agent loop (8 phases vs. coarser or finer splits)?
- Are there measurable defect-rate or velocity improvements attributable specifically to phase-aware prompting vs. baseline Copilot usage?
- How should prompt templates be versioned and evolved as underlying model capabilities change?

---

## Output

- Type: knowledge, backlog-item
- Description: A structured framework of prompt patterns for each SDLC phase, with templates, real-world examples, and an efficiency map; may spawn follow-on items on tooling integration (MCP servers, CI prompts) or skills development for specific phases
- Links:
  - `AGENTS.md`
  - `.github/mcp.json`
