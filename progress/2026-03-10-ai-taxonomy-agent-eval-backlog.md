# Session: AI taxonomy and agent evaluation backlog items

**Date:** 2026-03-10
**Slug:** ai-taxonomy-agent-eval-backlog

## What was done

Added two new research backlog items in response to the issue requesting:
1. A classification taxonomy for AI-related concepts
2. A better evaluation mechanism for agents, grounded in cross-repo analysis

### Items created

**`Research/backlog/2026-03-10-ai-concept-classification-taxonomy.md`**
- Priority: high
- Tags: taxonomy, classification, prompt-engineering, context-engineering, intent-engineering, memory, failure-modes, guardrails, skills, tools, agents
- Covers: prompt types, instruction types, the three engineering disciplines (prompt/content/intent), memory taxonomy, failure mode taxonomy, controls and guardrails taxonomy, skills vs tools vs agents distinction, problem domain map
- Blocks: the agent evaluation item (needs shared vocabulary first)

**`Research/backlog/2026-03-10-agent-evaluation-cross-repo-analysis.md`**
- Priority: high
- Tags: agents, evaluation, benchmarking, cross-repo-analysis, pattern-analysis, regression, effectiveness
- Covers: survey of 8–12 agent repos/frameworks, pattern extraction using the taxonomy, idiomaticity analysis, effectiveness signals survey, regression framework design
- Blocks-on: `2026-03-10-ai-concept-classification-taxonomy` (dependency made explicit in frontmatter)

## Related completed research surfaced

- `2026-03-04-sdlc-ai-prompt-patterns.md` — prompt patterns in SDLC contexts
- `2026-03-08-context-engineering-first-principles.md` — token-level vs goal-level steering
- `2026-03-02-agent-memory-management-context-injection.md` — memory taxonomy
- `2026-03-02-integrative-framework-agent-decision-making.md` — DIKW decision-making
- `2026-03-10-formal-spec-intent-alignment-agentic-coding.md` — intent specification hierarchy
- `2026-03-08-ai-coding-harnesses-agent-philosophy.md` — agent harnesses and philosophy
- `2026-03-05-general-agent-optimization-framework.md` — optimisation frameworks

## Notes

The taxonomy item must complete before the evaluation item starts — this is encoded in the `blocks` field of the evaluation item. The evaluation framework item produces both `knowledge` and a `backlog-item` output (the backlog item being a potential follow-on for actually building the evaluation tooling once the framework is specified).
