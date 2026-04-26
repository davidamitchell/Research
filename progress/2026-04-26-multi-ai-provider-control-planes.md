# 2026-04-26 -- Research Loop (multi-ai-provider-control-planes)

**Completed:**

Research item:
- `Research/completed/2026-04-26-multi-ai-provider-control-planes.md` -- completed; the item concludes that no single reviewed product currently provides one shared management layer across Microsoft, Amazon Web Services (AWS), and developer-tool copilot surfaces. The strongest current pattern is layered: vendor-native administration for content and entitlement, a cross-provider gateway for runtime routing and cost control, and a separate enterprise identity and compliance layer above both.

Sources consulted:
- https://learn.microsoft.com/en-us/azure/foundry/control-plane/overview (Microsoft Foundry Control Plane overview)
- https://docs.github.com/en/copilot/how-tos/administer-copilot/manage-for-enterprise/review-audit-logs (GitHub Copilot enterprise audit limits)
- https://cloud.google.com/solutions/apigee-ai (Apigee AI gateway and governance overview)

## Applied improvements

- Updated `research-prompt.md` to require parity between `§6 Synthesis` and `## Findings` after any post-review edit so mirrored sections cannot drift during revision loops.

## Mini-Retro

1. **Did the process work?** Yes; the research loop worked end to end, and the automated review surfaced useful evidence-discipline and wording issues before completion.
2. **What slowed down or went wrong?** Post-review edits were applied to `## Findings` first, and one mirrored `§6 Synthesis` block stayed stale until a later consistency pass caught it.
3. **What single change would prevent this next time?** Add an explicit self-review rule that any post-review change in `## Findings` must be mirrored back into `§6 Synthesis` before proceeding.
4. **Is this a pattern?** Not yet, but it is adjacent to known review-loop failures where mirrored or repeated sections drift during manual fixes.
