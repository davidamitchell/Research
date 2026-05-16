# 2026-05-16 -- Add backlog items (thesis-rq-backlog-split)

**Completed:**
- `Research/backlog/2026-05-16-agent-operational-cost-vs-gap-closure-cost.md` — added RQ1 as a scoped backlog item with cost-model framing and URL-backed starter sources.
- `Research/backlog/2026-05-16-external-dependency-surface-taxonomy-for-production-llm-agents.md` — added RQ2 as a dependency-surface taxonomy item with failure-mode focus and URL-backed starter sources.
- `Research/backlog/2026-05-16-do-mode-demand-persistence-and-build-mode-displacement.md` — added RQ3 as a displacement and persistence evidence item with URL-backed starter sources.
- `Research/backlog/2026-05-16-variance-control-comparison-across-delivery-modes.md` — added RQ4 as a variance-control comparison item with URL-backed starter sources.
- `Research/backlog/2026-05-16-it-throughput-constraint-magnitude-and-debt-accumulation-rate.md` — added RQ5 as an Information Technology (IT) throughput and debt-accumulation item with URL-backed starter sources.
- `Research/backlog/2026-05-16-decommission-trigger-design-for-do-mode-agents.md` — added RQ6 as a decommission-trigger design item with URL-backed starter sources.

## Mini-Retro

1. **Did the process work?** Yes. The issue already contained six well-formed research questions, so converting each into a separate backlog item was direct and low-risk.
2. **What slowed down or went wrong?** Initial local checks failed because development dependencies were not yet installed (`ruff` missing), which added setup time before validation.
3. **What single change would prevent this next time?** In fresh clones, run `pip install -e ".[dev]"` before the first validation command to avoid missing-tool failures.
4. **Is this a pattern?** Yes. Fresh runner environments regularly need dependency bootstrap before `make check` can run.
5. **Does any documentation need updating?** No. Existing instructions already require URL-backed sources and backlog-item intake structure; this session followed those conventions without introducing new behavior.
6. **Do the default instructions need updating?** No. The current instructions already captured the key constraints that mattered for this task.
