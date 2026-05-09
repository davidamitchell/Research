# 2026-05-09 -- Research Loop (hybrid-architecture-probabilistic-llm-deterministic-governance)

**Completed:**

Research item:
- `Research/completed/2026-05-09-hybrid-architecture-probabilistic-llm-deterministic-governance.md` -- completed; the item concludes that enterprise hybrid architectures should let the Large Language Model (LLM) interpret and propose through structured outputs while deterministic guardrails, policy engines, approvals, and human stop rights make the final governance decision. It also identifies the key boundary requirements: schema-constrained handoff objects, pre-inference and post-inference controls, joined model plus policy audit logs, and fail-closed escalation when policy or intent checks are ambiguous.

Sources consulted:
- https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-how.html (pre-inference and post-inference guardrail behavior)
- https://learn.microsoft.com/en-us/azure/ai-services/content-safety/concepts/task-adherence (tool-intent misalignment detection and escalation)
- https://www.openpolicyagent.org/docs/latest/ (decoupled policy decision layer for deterministic enforcement)

## Mini-Retro

1. **Did the process work?** Yes. The seeded sources plus the review workflow were enough to build and tighten the item into a clean completed result.
2. **What slowed down or went wrong?** The main friction was epistemic labeling on broadened architecture recommendations, where statements that felt obviously correct still had to be downgraded from fact to inference unless the exact generalized claim was directly supported.
3. **What single change would prevent this next time?** Nothing. The existing review loop already catches this class of issue quickly enough.
4. **Is this a pattern?** Yes, but it matches the existing citation-discipline and confidence-alignment patterns already documented in the repo instructions rather than a new failure class.
