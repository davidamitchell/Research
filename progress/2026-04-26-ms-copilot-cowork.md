# 2026-04-26 -- Research Loop (ms-copilot-cowork)

**Completed:**

Research item:
- `Research/completed/2026-04-26-ms-copilot-cowork.md` -- completed; the item concludes that Microsoft 365 Copilot Cowork is a preview, action-taking Microsoft agent whose main enterprise risk is shadow automation built on existing permissions rather than a brand-new extensibility stack. It also distinguishes Cowork's per-user `SKILL.md` model from formal Microsoft Copilot extensibility and identifies Anthropic regional constraints plus the uploaded-file DLP gap as the two most important legal-control caveats.

Sources consulted:
- https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/cowork-admin-governance (official admin controls and rollout model)
- https://learn.microsoft.com/en-us/microsoft-365/copilot/connect-to-ai-subprocessor (Anthropic subprocessor, regional defaults, and exclusions)
- https://learn.microsoft.com/en-us/purview/dlp-microsoft365-copilot-location-learn-about (DLP controls and uploaded-file gap)

## Mini-Retro

1. **Did the process work?** Yes, the repo workflow worked end to end and the review job caught evidence-discipline issues before completion.
2. **What slowed down or went wrong?** Preview-source contradictions and the reviewer's treatment of `Access note:` bullets created avoidable churn even after the substantive research was sound.
3. **What single change would prevent this next time?** Make the prompt explicitly require `Access note:` bullets to be written as metadata fragments rather than full declarative sentences.
4. **Is this a pattern?** Yes, it is the same citation-discipline class as prior review failures: small formatting ambiguities around evidence labels create unnecessary second-pass reviews.

## Applied improvements

- `research-prompt.md` -- clarified that `Access note:` bullets in §2 must be written as metadata fragments, not full declarative sentences, to reduce citation-discipline review failures.
