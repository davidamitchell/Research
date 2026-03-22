---
title: "Agents as finishers and synthesisers: optimising AI agents to complement ideation-strong, execution-weak humans"
added: 2026-03-22
status: backlog  # backlog | in-progress | reviewing | completed
priority: high  # low | medium | high
blocks: []
tags: [agents, human-ai-collaboration, productivity, finishing, synthesis, orchestration, cognitive-styles]
started: ~
completed: ~
output: [knowledge, backlog-item]
---

# Agents as finishers and synthesisers: optimising AI agents to complement ideation-strong, execution-weak humans

## Research Question

What agent configurations, prompt strategies, orchestration patterns, and tooling choices allow an AI agent (or agent team) to act as a reliable *finisher* and *synthesiser* — completing work that a human has started but not followed through on — and what are the practical limits of this complementary model?

Supporting questions:
- What cognitive or productivity frameworks describe the "ideas person / weak finisher" profile, and how does that map to AI agent capabilities?
- Which agent roles (planner, executor, reviewer, synthesiser, organiser) are most effective at compensating for execution and organisation weaknesses?
- What prompt patterns and agent instructions produce reliable task completion rather than a new layer of partial ideas?
- How should a human-agent handoff be structured so the agent can pick up unfinished work without losing context?
- What are the failure modes when using agents as finishers (e.g. hallucinated completions, loss of original intent, over-generalisation)?
- Are there published agent frameworks, research papers, or real-world case studies that specifically address human–AI cognitive complementarity?
- What tooling (GitHub Copilot Agent, AutoGen, CrewAI, LangGraph, etc.) is best suited to a "finishing and synthesising" use case in a no-local-IDE environment?

## Scope

**In scope:**
- Agent roles explicitly designed to finish, organise, or synthesise: task completion agents, summarisation agents, project management agents, note-to-action agents
- Human–AI cognitive complementarity research — divergent thinking (ideation) vs. convergent thinking (execution, synthesis)
- Prompt engineering patterns for handoff, context preservation, and completion
- Orchestration frameworks available without a local IDE (GitHub Copilot Agent, GitHub Actions-based agents, API-accessible agents)
- Failure modes and mitigations specific to "finishing" use cases
- Practical patterns already used in this repo (research-loop workflow, copilot-instructions.md, skills) that could be extended

**Out of scope:**
- General Large Language Model (LLM) capability benchmarks not related to finishing or synthesis
- VS Code or local IDE extensions (owner has no local IDE)
- Research on pure automation (no human in the loop)
- Credentials or services not listed in the approved credentials table

**Constraints:** GitHub website and iOS app only — no local IDE. Agent work must be triggerable from a browser or mobile.

## Context

The owner has identified a personal superpower (ideation, pattern recognition, abstraction) and a corresponding weakness (finishing, following through, organisation). The question is whether AI agents can be configured and orchestrated to fill exactly those gaps — acting as a persistent, context-aware execution layer on top of a human's ideas.

This is not a generic "how do I use AI" question. It is a specific design challenge: how do you structure a human–agent system where the human provides direction and insight while the agent provides completion and coherence? Getting this wrong leads to more half-finished ideas managed by an agent rather than fewer. Getting it right could dramatically increase throughput.

The question is high-priority because it directly shapes how this Research repo and its workflows should evolve — including whether agent skills, the research-loop workflow, or new tooling should be added.

## Approach

1. **Map the human profile to agent capabilities** — research cognitive frameworks for divergent vs. convergent thinking and identify where agents currently perform well on convergent tasks (summarising, organising, completing, structuring).
2. **Survey agent roles and orchestration patterns** — catalogue "finisher" and "synthesiser" agent roles from existing frameworks (CrewAI, AutoGen, LangGraph, GitHub Copilot Agent). Note which roles are available without a local IDE.
3. **Identify prompt and instruction patterns** — find published or community-documented prompt patterns for task handoff, context preservation, and completion. Evaluate against the failure modes (hallucination, intent drift).
4. **Review failure modes and mitigations** — identify what goes wrong when agents are used as finishers and what structural or prompt-level interventions reduce those failures.
5. **Assess tooling fit** — evaluate which agent frameworks and tools are usable given the no-local-IDE constraint and the approved credentials table.
6. **Produce concrete recommendations** — output: a knowledge summary of what works and why, plus concrete backlog items for changes to this repo's agent configuration, skills, or workflows.

## Sources

- [ ] "Thinking, Fast and Slow" — Kahneman on System 1 / System 2 thinking as a framework for ideation vs. execution — https://en.wikipedia.org/wiki/Thinking,_Fast_and_Slow
- [ ] CrewAI documentation on agent roles and task assignment — https://docs.crewai.com/concepts/agents
- [ ] AutoGen documentation on multi-agent conversation patterns — https://microsoft.github.io/autogen/
- [ ] LangGraph documentation on agent orchestration — https://langchain-ai.github.io/langgraph/
- [ ] GitHub Copilot Coding Agent documentation — https://docs.github.com/en/copilot/using-github-copilot/using-claude-sonnet-in-github-copilot
- [ ] "The Divergence-Convergence Model" (Double Diamond, IDEO) — academic and practitioner use of divergent/convergent phases — https://www.designcouncil.org.uk/our-resources/the-double-diamond/
- [ ] Anthropic research on agentic task completion and reliability — https://www.anthropic.com/research
- [ ] "Cognitive offloading" literature — using external tools to compensate for working memory or executive function limits — search via Tavily
- [ ] Community discussions on using agents for GTD (Getting Things Done) and personal knowledge management — search via Tavily
- [ ] Existing skills and workflows in this repo — `.github/skills/`, `.github/workflows/research-loop.yml`, `research-prompt.md`

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

- Type: knowledge, backlog-item
- Description:
- Links:
