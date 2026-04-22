# 2026-04-22 -- Add backlog item (enterprise-ai-use-case-routing-frameworks-backlog)

**Completed:**
- `Research/backlog/2026-04-22-enterprise-ai-use-case-routing-frameworks.md` — added from issue request; scopes an enterprise Artificial Intelligence (AI) use-case routing framework question across platform pattern selection and risk-tier governance checkpoints.

## Mini-Retro

1. **Did the process work?** Yes. The issue statement was specific enough to convert directly into a scoped backlog question, with clear in-scope routing paths and governance checkpoints.
2. **What slowed down or went wrong?** Baseline checks surfaced one pre-existing environment-only failure (`TAVILY_API_KEY` missing), which does not affect this backlog-item documentation change.
3. **What single change would prevent this next time?** No workflow change needed for this item; handling secret-gated test failures as environment constraints remains the right approach.
4. **Is this a pattern?** Yes. Local runs in sandbox environments often lack optional secrets used by live integration checks.
