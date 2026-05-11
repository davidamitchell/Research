# 2026-05-11 -- Research Loop (m365-copilot-sensitive-data-security-governance-risks)

**Completed:**

Research item:
- `Research/completed/2026-05-10-m365-copilot-sensitive-data-security-governance-risks.md` -- completed; the item found that Microsoft 365 Copilot's main regulated-environment risk is inherited-access amplification over already-overshared tenant data, not a separate hidden authorization path. It also found that the practical control stack is permissions remediation, sensitivity labels, DLP, restricted discovery, auditability, and sovereign deployment where the data class requires it.

Sources consulted:
- https://learn.microsoft.com/en-us/copilot/microsoft-365/microsoft-365-copilot-privacy (Copilot Graph access, storage, and privacy boundary)
- https://learn.microsoft.com/en-us/microsoft-365/copilot/microsoft-365-copilot-architecture-data-protection-auditing (Copilot label handling, access controls, and auditing)
- https://learn.microsoft.com/en-us/purview/dlp-microsoft365-copilot-location-learn-about (DLP controls and blind spots for Copilot)

## Applied improvements

- Updated `research-prompt.md` to state explicitly that multiple sources from the same vendor do not justify `high` confidence by themselves, and that evaluative words such as "useful", "strongest", "dominant", and "unsafe" should default to `[inference]` unless the source makes that judgment directly.

## Mini-Retro

1. **Did the process work?** Yes, the research and review loop converged cleanly once the item's epistemic labels and confidence levels were aligned with the reviewer's stricter heuristics.
2. **What slowed down or went wrong?** The review workflow enforced a narrower distinction between factual platform behavior and evaluative synthesis language than the prompt stated explicitly, so one extra pass was needed.
3. **What single change would prevent this next time?** The prompt now says that same-vendor sources do not earn `high` confidence on their own and that evaluative adjectives should default to `[inference]`.
4. **Is this a pattern?** Yes, it matches the existing confidence-evidence-alignment and comparative-claim review themes rather than a brand-new failure class.
