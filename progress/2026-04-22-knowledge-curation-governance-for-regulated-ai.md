# 2026-04-22 -- Add backlog item (knowledge-curation-governance-for-regulated-ai)

**Completed:**
- `/home/runner/work/Research/Research/Research/backlog/2026-04-22-knowledge-curation-governance-for-regulated-ai.md` - added from issue #370; frames the research question on operational governance models for authoritative AI knowledge in regulated financial services.

## Mini-Retro

1. **Did the process work?** Yes. The issue provided a strong initial question and scope, so the backlog template could be populated directly with only light normalisation.
2. **What slowed down or went wrong?** Baseline local validation initially failed because dev tooling (`ruff`, `pytest`) was not installed in the fresh environment.
3. **What single change would prevent this next time?** Keep using `pip install -e ".[dev]"` early in fresh sessions before running repository checks.
4. **Is this a pattern?** Yes. Fresh clones frequently need explicit dependency bootstrapping before lint/test commands succeed.
