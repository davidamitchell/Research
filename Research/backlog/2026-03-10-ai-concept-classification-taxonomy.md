---
title: "AI concept classification taxonomy: prompts, instructions, memory, failure modes, controls, and problem domains"
added: 2026-03-10
status: backlog
priority: high
blocks: [2026-03-10-agent-evaluation-cross-repo-analysis]
tags: [taxonomy, classification, prompt-engineering, context-engineering, intent-engineering, memory, failure-modes, guardrails, skills, tools, agents, agentic-systems]
started: ~
completed: ~
output: [knowledge]
---

# AI concept classification taxonomy: prompts, instructions, memory, failure modes, controls, and problem domains

## Research Question

What is a coherent, internally consistent classification taxonomy for the core concepts in AI-assisted and agentic systems — covering prompt types, instruction types, prompt/content/intent engineering approaches, memory types, failure modes, controls and guardrails, skills, tools, and problem domains — such that any given concept maps to exactly one primary category and the taxonomy is stable enough to use as a shared vocabulary across research items and system designs?

## Scope

**In scope:**
- Classification of prompt types (system, user, assistant, tool-call, few-shot examples, chain-of-thought, meta-prompts, etc.)
- Classification of instruction types (declarative goals, procedural steps, constraints, examples, persona definitions, format directives, safety rails, etc.)
- Distinctions between prompt engineering, content engineering, and intent engineering as disciplines — what each optimises for, what its unit of work is, and where the three overlap
- Memory type taxonomy: in-context (working), external (retrieval), parametric (model weights), episodic (session), semantic (fact store), procedural (skill store)
- Failure mode taxonomy: hallucination, reward hacking, intent mismatch, goal drift, context overflow, over-compliance, under-specification, instruction conflict, tool misuse, guardrail bypass
- Controls and guardrails taxonomy: structural (schema/type constraints), semantic (content filters, classifiers), procedural (confirmation gates, escalation paths), architectural (sandboxing, scoping, permission models)
- Skills taxonomy: what distinguishes a skill from a tool, from an agent, from an instruction set — and how skills compose
- Tools taxonomy: categories of tools available to agents (retrieval, execution, communication, stateful vs stateless, read-only vs write, sandboxed vs ambient)
- Problem domain map: what classes of problems benefit from agentic approaches vs simpler pipelines
- Cross-cutting concerns: how taxonomy categories compose (e.g. a skill may use several tool types and depend on a specific memory type)

**Out of scope:**
- Implementation of any taxonomy as code or schema (a separate backlog item)
- Fine-grained evaluation of specific prompt patterns (covered by `2026-03-04-sdlc-ai-prompt-patterns.md`)
- First-principles derivation of context engineering mechanisms (covered by `2026-03-08-context-engineering-first-principles.md`)
- Memory system implementation details (covered by `2026-03-02-agent-memory-management-context-injection.md`)

**Constraints:** Taxonomy must be derivable from published practitioner literature, academic papers, and existing repo research. No empirical experiments required.

## Context

The research corpus has grown to cover prompts, memory, controls, agents, tools, and failure modes — but each item developed its own local vocabulary. There is no single shared classification that lets a new research item or system design state "this uses a Type-2 memory, a procedural guardrail, and an intent-engineering approach" and have that be unambiguous. Without a stable taxonomy, cross-item synthesis is harder, agent designs are inconsistently described, and evaluation criteria cannot be agreed upon.

This taxonomy is the prerequisite for the companion item on agent evaluation (`2026-03-10-agent-evaluation-cross-repo-analysis.md`): you cannot compare agents across repos without a shared vocabulary for what they are doing and why.

Completed items that constrain the taxonomy:
- `2026-03-04-sdlc-ai-prompt-patterns.md` — identifies emergent prompt patterns in SDLC contexts
- `2026-03-08-context-engineering-first-principles.md` — defines token-level vs goal-level steering; distinguishes prompt engineering from context engineering
- `2026-03-02-agent-memory-management-context-injection.md` — taxonomy of memory approaches
- `2026-03-02-integrative-framework-agent-decision-making.md` — DIKW-aligned decision-making framework
- `2026-03-10-formal-spec-intent-alignment-agentic-coding.md` — intent specification hierarchy
- `2026-02-28-ai-control-testing-and-assurance.md` — controls and assurance landscape

## Approach

1. Audit existing research corpus for locally-defined vocabularies and taxonomies; collect all candidate category definitions
2. Survey published AI/ML taxonomy literature (e.g. prompt pattern catalogues, LLM failure mode surveys, agent architecture surveys)
3. For each candidate taxonomy domain (prompts, instructions, memory, failure modes, controls, skills, tools, problem domains): identify dimensions, enumerate categories, test mutual exclusivity and exhaustiveness (MECE)
4. Identify cross-cutting concerns and define composition rules (how categories from different domains relate)
5. Validate the taxonomy against 5–10 existing completed research items: can each item's core concepts be unambiguously labelled?
6. Produce the taxonomy as a structured artefact: a set of named, defined, and cross-referenced categories per domain

## Sources

- [ ] `Research/completed/2026-03-04-sdlc-ai-prompt-patterns.md`
- [ ] `Research/completed/2026-03-08-context-engineering-first-principles.md`
- [ ] `Research/completed/2026-03-02-agent-memory-management-context-injection.md`
- [ ] `Research/completed/2026-03-02-integrative-framework-agent-decision-making.md`
- [ ] `Research/completed/2026-03-10-formal-spec-intent-alignment-agentic-coding.md`
- [ ] Prompt pattern catalogues: "Prompt Patterns as a Means for Evaluating and Improving Prompt Engineering" (White et al., 2023)
- [ ] LLM failure mode surveys: "A Survey of Hallucination in Large Language Models" (Ji et al., 2023)
- [ ] Agent architecture surveys: "A Survey on Large Language Model based Autonomous Agents" (Wang et al., 2023)
- [ ] Anthropic Responsible Scaling Policy and Claude usage guidelines (guardrails vocabulary)
- [ ] OWASP Top 10 for LLM Applications (failure modes and controls vocabulary)
- [ ] LangChain, CrewAI, and AutoGen documentation (tools and skills vocabulary)
