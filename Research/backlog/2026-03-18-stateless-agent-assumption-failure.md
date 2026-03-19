---
title: "Stateless-agent assumption failure: causes, detection, and recovery patterns for orphaned state in multi-session agentic workflows"
added: 2026-03-18
status: backlog
priority: high
blocks: []
tags: [failure-modes, agentic-systems, operational-failures, layer-5, state-management, idempotency, checkpoint-resume, multi-session, workflow]
started: ~
completed: ~
output: [knowledge]
---

# Stateless-agent assumption failure: causes, causes, detection, and recovery patterns for orphaned state in multi-session agentic workflows

## Research Question

When an agentic workflow spans multiple session boundaries — each session starting with a fresh context window and no memory of prior runs — what are the mechanisms by which external state becomes orphaned, how frequently does this failure mode occur in production systems, what signals reliably detect it before it compounds, and what design patterns reliably prevent or recover from it?

## Scope

**In scope:**
- Definition and precise characterisation of the stateless-agent assumption failure as a subtype of Layer 5 operational failure (as classified in `2026-03-12-failure-mode-taxonomy-expansion.md`)
- Root cause analysis: why agents built on fresh-context-per-session architectures implicitly assume a clean initial world state
- Taxonomy of orphaned-state subtypes: partially-completed work items, externally-triggered side effects (workflow runs, commits) that were never confirmed, counter/flag fields written by one session but never read by the next
- Empirical evidence: how common is this failure in production agentic systems? (incident reports, post-mortems, practitioner accounts)
- Detection signals: what observable indicators (file system state, git log patterns, workflow run history, frontmatter fields) allow a new session to discover and classify orphaned state
- Recovery patterns: at-least-once vs exactly-once semantics, idempotent operations, checkpoint-resume, external state registers, re-entrant prompt design
- Comparison with analogous distributed systems patterns: at-most-once delivery, two-phase commit, saga pattern, dead-letter queues
- Evaluation of tradeoffs: complexity of recovery logic vs risk of orphan accumulation under different workflow topologies

**Out of scope:**
- Context overflow as a failure mode (covered in `2026-03-08-context-engineering-first-principles.md`)
- Multi-agent coordination failures where agents have concurrent sessions (the focus here is sequential sessions with no shared live context)
- Hardware or infrastructure failures not caused by agent design
- Full implementation of mitigation tooling (follow-on engineering item)

## Context

This item is motivated by a concrete observed failure in the `davidamitchell/Research` agentic research loop: the loop's `research-prompt.md` Step 1 only examined `Research/backlog/` when selecting the next item to work on. Any item that had been moved to `Research/in-progress/` by a prior session — but not yet completed — was invisible to subsequent sessions. The new session would pick a fresh backlog item, leaving the in-progress item permanently orphaned. The fix (checking `in-progress/` first) was straightforward once identified, but the failure had persisted across 29 draft commits and multiple sessions without being detected.

The failure belongs to the Layer 5 operational failure class in the taxonomy from `2026-03-12-failure-mode-taxonomy-expansion.md`, but represents a distinct subtype not fully elaborated there: the implicit assumption by a stateless agent that the external world begins in a clean state at the start of each session.

Structurally, this is identical to a distributed worker that crashes after dequeuing a task but before acknowledging completion: the task is neither in the queue nor marked done. The distributed systems literature has well-developed patterns for this (idempotent consumers, saga compensating transactions, at-least-once with deduplication). The question is how those patterns translate — or fail to translate — into the agentic/LLM context, where the "worker" is a fresh context window with no persistent memory and the "task state" is scattered across git history, file system, and external service state.

## Approach

1. **Characterise the failure class precisely** — distinguish stateless-agent assumption failure from adjacent Layer 5 failures (context overflow, instruction conflict). Produce a precise definition with necessary and sufficient conditions. Cross-reference the taxonomy item.

2. **Map the failure's state space** — enumerate the ways external state can become orphaned in a multi-session agent: incomplete file moves, uncommitted edits, triggered-but-unconfirmed side effects, counter fields written but never read. Use the Research loop as a concrete worked example but generalise beyond it.

3. **Survey empirical evidence** — search production incident reports, agent framework post-mortems, and practitioner accounts for this failure class. How common is it? Does it have a recognised name in the agentic systems community?

4. **Identify detection signals** — what can a new session observe, without prior context, that indicates the world is not in a clean state? Distinguish: (a) file-system-observable signals; (b) git-history signals; (c) external service state (workflow runs, issue trackers); (d) frontmatter / metadata fields as explicit checkpoints.

5. **Survey recovery patterns from distributed systems** — at-least-once vs exactly-once, saga pattern, two-phase commit, dead-letter queues, idempotent operations. Evaluate how each maps to the agentic context and where the analogies break down.

6. **Derive design principles** — what structural properties must an agentic prompt or workflow have to be resilient to session-boundary state orphaning? Evaluate tradeoffs between recovery complexity and failure probability under different workflow topologies (linear, branching, looping).

## Sources

- `Research/completed/2026-03-12-failure-mode-taxonomy-expansion.md` — parent taxonomy; Layer 5 operational failures
- `Research/completed/2026-03-08-context-engineering-first-principles.md` — context overflow and instruction conflict as adjacent Layer 5 subtypes
- `Research/completed/2026-03-01-github-specify-ralph-loop-lisa-planning.md` — prior work on the research loop architecture
- `Research/completed/2026-03-03-research-loop-quality-prompt-engineering.md` — prompt engineering for loop reliability
- Distributed systems literature: saga pattern, two-phase commit, at-least-once delivery, idempotent consumers
- Agentic framework documentation and incident reports: LangChain, AutoGPT, CrewAI, OpenAI Swarm post-mortems
- METR task evaluation data on agent reliability in multi-step workflows
