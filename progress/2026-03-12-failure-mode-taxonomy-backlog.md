# Session: failure-mode-taxonomy-backlog

**Date:** 2026-03-12
**Task:** Add backlog item expanding Q5 — Failure mode taxonomy from the AI concept classification taxonomy, with full cross-links to prior completed research.

## What was done

Created `Research/backlog/2026-03-12-failure-mode-taxonomy-expansion.md`.

The item expands on the five-layer failure mode taxonomy introduced in Q5 of `2026-03-10-ai-concept-classification-taxonomy.md`. The taxonomy (Layer 1 generation, Layer 2 goal, Layer 3 alignment, Layer 4 safety/security, Layer 5 operational) was classified as complete in the parent item but explicitly flagged empirical frequency, causal mechanism depth, and cascade analysis as open questions.

## Prior research cross-linked

All cross-links were verified against actual completed research files:

| Layer | Research item(s) |
|---|---|
| Layer 1 — Generation (hallucination, sycophancy) | `2026-03-05-llm-hallucination-mechanisms`, `2026-03-05-h-neurons-in-llms`, `2026-03-05-h-neuron-over-compliance`, `2026-03-05-h-neurons-synthesis`, `2026-03-05-h-neuron-pretraining-origins`, `2026-02-28-controlled-hallucination-perception-as-construction` |
| Layer 2 — Goal (intent mismatch, under-specification, goal drift) | `2026-03-10-formal-spec-intent-alignment-agentic-coding`, `2026-03-08-context-engineering-first-principles` |
| Layer 3 — Alignment (reward hacking, specification gaming) | `2026-03-10-formal-spec-intent-alignment-agentic-coding` |
| Layer 4 — Safety/security (prompt injection, guardrail bypass, excessive agency) | `2026-03-01-agent-lsp-policy-enforcement`, `2026-02-28-ai-line-1-line-2-risk-agents` |
| Layer 5 — Operational (context overflow, instruction conflict, unbounded consumption) | `2026-03-08-context-engineering-first-principles` |
| Parent taxonomy | `2026-03-10-ai-concept-classification-taxonomy` |

## Scope of new item

The backlog item frames six investigation threads:
1. Empirical frequency survey (which layers are most common in production?)
2. Causal mechanism depth per layer (drawing on prior research, with fresh investigation for Layers 4–5)
3. Detection signal identification (output-, trace-, and system-observable signals per failure type)
4. Cascade analysis (directed failure cascade graph across layers)
5. Control mapping extension (which detection signal triggers which control; control failure modes)
6. Synthesis into a prioritised failure mode register (frequency × impact × detectability)
