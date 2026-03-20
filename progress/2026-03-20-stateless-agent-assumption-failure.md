# 2026-03-20 — Research Loop (stateless-agent-assumption-failure)

**Completed:**

Research item:
- `Research/completed/2026-03-18-stateless-agent-assumption-failure.md` — completed; the item defines stateless-agent assumption failure as a Layer 5 continuity failure caused by fresh-session agents acting on durable external state without reconciliation. It concludes that the most reliable controls are startup reconciliation across all authoritative state surfaces, idempotent retry plus checkpoint-resume as the default recovery baseline, and compensation or manual quarantine for non-atomic multi-step side effects.

Sources consulted:
- https://docs.langchain.com/oss/python/langgraph/durable-execution (official durable execution and replay requirements for long-running agent workflows)
- https://docs.temporal.io/workflow-execution (official durable workflow execution and replay semantics)
- https://aws-samples.github.io/eda-on-aws/concepts/idempotency/ (idempotency and duplicate-processing guidance for distributed systems)

## Mini-Retro

1. **Did the process work?** Yes. The loop selected the correct item, the review workflow surfaced concrete quality issues, and the second pass reached the completion threshold.
2. **What slowed down or went wrong?** The review workflow is strict about claim-level labeling and source binding in both `## Research Skill Output` and `## Findings`, and it also flags near-verbatim repetition between §6 Synthesis and `## Findings`, so the first draft needed a focused rewrite.
3. **What single change would prevent this next time?** Start with a more compact §6 Synthesis and a more expanded, citation-bearing `## Findings` section so the two sections are complementary rather than lightly rephrased duplicates.
4. **Is this a pattern?** Yes. It matches the repo's known pattern that research reviews most often fail on citation discipline and output-structure issues rather than on lack of substantive investigation.
