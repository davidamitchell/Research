# 2026-04-26 -- Research Loop (deployment-pipeline-citizen-development-governed-gate)

**Completed:**

Research item:
- `Research/completed/2026-04-26-deployment-pipeline-citizen-development-governed-gate.md` -- completed; the item concludes that the deployment pipeline is the best composite promotion gate for citizen-developed agents, but not the only enforceable control in a Microsoft low-code estate. It also finds that pipeline gating is bypassable by default and becomes credible only after direct publication, unmanaged changes, and production write paths are narrowed through environment, role, and delegated-deployment controls.

Sources consulted:
- https://learn.microsoft.com/en-us/power-platform/alm/extend-pipelines (native Power Platform gate hook points)
- https://learn.microsoft.com/en-us/power-platform/alm/block-unmanaged-customizations (production lock-down and Copilot Studio publish blocking)
- https://learn.microsoft.com/en-us/microsoft-copilot-studio/guidance/sec-gov-phase2 (Microsoft zoned governance model)

## Mini-Retro

1. **Did the process work?** Yes. The research workflow, review loop, and completion commands all worked end to end.
2. **What slowed down or went wrong?** The first review pass caught claim-label mismatches where synthesized judgments were written as facts and one claim mentioned role-based access without binding the supporting environment-security sources at the claim site.
3. **What single change would prevent this next time?** Nothing new is needed in the prompt; the existing rules already cover these failure modes, and the fix was to apply them more strictly in the first draft.
4. **Is this a pattern?** No new pattern. This was ordinary first-pass review tightening, not a new recurring class beyond the repo's existing citation-discipline guidance.
