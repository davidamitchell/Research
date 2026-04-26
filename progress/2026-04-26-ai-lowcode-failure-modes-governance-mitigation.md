# 2026-04-26 -- Research Loop (ai-lowcode-failure-modes-governance-mitigation)

**Completed:**

Research item:
- `Research/completed/2026-04-26-ai-lowcode-failure-modes-governance-mitigation.md` -- completed; the item concludes that the recurring enterprise failures across Artificial Intelligence (AI) and low-code systems are boundary-crossing failures such as prompt injection, excessive delegated authority, unmanaged publication, and broken audit chains. It also shows that those failures become more frequent and more severe when the surrounding estate already has systems-capability debt, weak identity design, access-control amplification, information-architecture incoherence, and missing corrective controls such as rollback, quarantine, and explicit rate limits.

Sources consulted:
- https://www.microsoft.com/en-us/msrc/blog/2025/07/how-microsoft-defends-against-indirect-prompt-injection-attacks (Microsoft production guidance on indirect prompt injection and layered mitigations)
- https://aisel.aisnet.org/misqe/vol23/iss3/6 (MIS Quarterly Executive article on governing citizen development in low-code environments)
- https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report (DORA report summary on delivery performance and control maturity)

## Mini-Retro

1. **Did the process work?** Yes, the draft-review loop worked and the external review surfaced the missing qualifiers and adjacent completed-item links that the first self-review missed.
2. **What slowed down or went wrong?** The first draft under-linked related completed items across neighboring governance surfaces, so the review cycle had to do work that should have been caught during self-review.
3. **What single change would prevent this next time?** Add a mandatory repository cross-reference sweep before draft commit for any Key Finding that touches a governance surface already covered elsewhere in `Research/completed/`.
4. **Is this a pattern?** Yes, this is a recurring pattern on cross-cutting governance items: adjacent completed work often materially sharpens or qualifies the same claim, and missing those links is avoidable.

## Applied improvements

- Updated `research-prompt.md` to require a repeated related-item scan before Findings and a dedicated repository cross-reference sweep during self-review.

## Pending skill improvements

- Mirror the new repository cross-reference sweep into the `research` skill checklist in `.github/skills/` so the same guardrail exists in the skill, not only in the fallback prompt.
