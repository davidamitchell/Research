---
title: "Agent evaluation framework: cross-repo pattern analysis, commonality detection, and regression identification"
added: 2026-03-10
status: backlog
priority: high
blocks: []
tags: [agents, evaluation, benchmarking, cross-repo-analysis, pattern-analysis, agentic-systems, metrics, regression, effectiveness, taxonomy]
started: ~
completed: ~
output: [knowledge, backlog-item]
---

# Agent evaluation framework: cross-repo pattern analysis, commonality detection, and regression identification

## Research Question

What evaluation framework allows systematic comparison of agent implementations across multiple repositories — identifying what problems each is solving, whether concepts are used idiomatically or in novel ways, whether the agent is effective, and how to detect whether a change to an agent made it better or worse — and what would a minimal viable implementation of such a framework look like?

## Scope

**In scope:**
- Survey of agent implementations across a set of public repos (GitHub Copilot, AutoGen, CrewAI, LangGraph, Pydantic AI, Agno, Claude Code, Cursor, and others) — what are they doing, how are they structured, what problems are they solving
- Identification of common patterns: what structures, flows, and mechanisms appear across multiple unrelated codebases
- Idiomaticity analysis: are agents using established concepts (e.g. tool-calling, RAG, memory injection) in the expected way, or diverging in novel but under-documented ways
- Novelty detection: which agent designs introduce genuinely new mechanisms not seen in other implementations
- Effectiveness criteria: what does "working" mean for an agent? What signals (task completion rate, error rate, user feedback, cost, latency, output quality) are used in practice across these repos
- Regression identification: what mechanisms exist (or should exist) to determine whether a change to an agent made it better or worse — test harnesses, evals, benchmarks, shadow runs, A/B patterns
- Dependency on taxonomy: this item uses the vocabulary from `2026-03-10-ai-concept-classification-taxonomy.md` to label what each repo's agent is doing

**Out of scope:**
- Building a fully automated cross-repo analysis pipeline (a separate backlog item if the framework warrants it)
- Formal benchmarking infrastructure (e.g. HumanEval, SWE-Bench) — these are reference points but not the focus
- Agent implementation for this repository (separate backlog item)
- Evaluating non-agentic LLM applications

**Constraints:** Analysis must be possible from public documentation, repos, and papers. No access to private repos or internal systems required. The taxonomy from `2026-03-10-ai-concept-classification-taxonomy.md` must be completed first; this item blocks on it.

## Context

The agent space is crowded and fast-moving. Every repo has its own vocabulary for what its "agents" do, how they use tools, how they handle memory, and how they fail. Without a cross-repo comparison grounded in a shared taxonomy, it is impossible to say whether a new agent design is genuinely novel, whether it is solving the same problem as an existing approach, or whether it is simply repackaging known patterns with new names.

The deeper problem is evaluation: how do you know if your agent is any good? And specifically, how do you know if the change you just made made it better or worse? This is unsolved in most repos. Tests are often absent, evals are hand-crafted and narrow, and there is no agreed-upon framework for what "better" means. The goal of this research is to synthesise the state of practice and identify what a workable evaluation framework would need to include.

Related completed research:
- `2026-03-08-ai-coding-harnesses-agent-philosophy.md` — agent harnesses, scaffolding, and philosophy
- `2026-03-05-general-agent-optimization-framework.md` — general optimisation approaches
- `2026-03-04-sdlc-ai-prompt-patterns.md` — patterns in prompt use across SDLC
- `2026-03-02-integrative-framework-agent-decision-making.md` — decision-making frameworks
- `2026-03-10-formal-spec-intent-alignment-agentic-coding.md` — intent alignment and reward hacking

This item also directly supports the goal of improving agent implementations in this repository itself, including the research loop agent.

## Approach

1. **Repo survey**: Select 8–12 representative agent repos/frameworks. For each: document the problem domain, architectural pattern, memory approach, tool use, and any evaluation mechanisms present
2. **Pattern extraction**: Apply the taxonomy from `2026-03-10-ai-concept-classification-taxonomy.md` to label each repo's design. Identify which patterns are shared across ≥3 repos (common) vs appearing in only one (novel)
3. **Idiomaticity analysis**: For each common pattern, assess whether implementations match the canonical definition or deviate — document deviations and their apparent rationale
4. **Effectiveness signals survey**: What metrics, evals, or tests do these repos use to measure agent quality? What is absent? Identify the gap between what practitioners want to measure and what they actually measure
5. **Regression framework design**: Synthesise from the survey what a minimal regression detection framework requires: input/output capture, evaluation rubric, comparison protocol, rollback signal
6. **Framework specification**: Produce a structured framework document — not an implementation, but a specification that could inform one — covering: evaluation dimensions, measurement approaches, regression thresholds, and tooling options

## Sources

- [ ] `Research/completed/2026-03-08-ai-coding-harnesses-agent-philosophy.md`
- [ ] `Research/completed/2026-03-05-general-agent-optimization-framework.md`
- [ ] `Research/completed/2026-03-04-sdlc-ai-prompt-patterns.md`
- [ ] `Research/completed/2026-03-10-formal-spec-intent-alignment-agentic-coding.md`
- [ ] AutoGen repo: https://github.com/microsoft/autogen — multi-agent conversation framework
- [ ] CrewAI repo: https://github.com/crewAIInc/crewAI — role-based agent orchestration
- [ ] LangGraph repo: https://github.com/langchain-ai/langgraph — stateful agent graphs
- [ ] Pydantic AI repo: https://github.com/pydantic/pydantic-ai — type-safe agent framework
- [ ] Agno repo: https://github.com/agno-agi/agno — multi-modal agent framework
- [ ] OpenHands (previously OpenDevin): https://github.com/All-Hands-AI/OpenHands — software engineering agents
- [ ] SWE-bench: https://github.com/princeton-nlp/SWE-bench — benchmark for software engineering agents
- [ ] "Evaluating Large Language Model Agents" — survey of LLM agent evaluation approaches
- [ ] Anthropic evals library and methodology documentation
- [ ] METR (Model Evaluation and Threat Research) task standard: https://github.com/METR/task-standard
