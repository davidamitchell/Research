# 2026-04-27 -- Research Loop (pip-invariant-anomaly-detection)

**Completed:**

Research item:
- `Research/completed/2026-04-27-pip-invariant-anomaly-detection.md` -- completed; the item concludes that the Policy Information Point (PIP) should combine deterministic contradiction checks with a Bayesian-style surprise layer to detect when transient framing suppresses permanent invariants. It separates passive, active, and adversarial suppression, uses Cynefin as a prior-adjustment signal rather than a standalone control, and defines a typed signal for the Policy Decision Point (PDP) that supports explainable monitoring and escalation.

Sources consulted:
- https://docs.oasis-open.org/xacml/3.0/xacml-3.0-core-spec-os-en.html (authoritative role definitions for PAP, PIP, PDP, and PEP)
- https://genai.owasp.org/llmrisk/llm01-prompt-injection/ (prompt injection mechanics, impacts, and mitigations)
- https://pmc.ncbi.nlm.nih.gov/articles/PMC2782645/ (formal definition of Bayesian surprise as posterior-vs-prior belief shift)

## Mini-Retro

1. **Did the process work?** Yes; the item moved cleanly through draft, review, revision, completion, and synthesis updates.
2. **What slowed down or went wrong?** The first review pass failed on non-standard epistemic labels, and the second pass surfaced a few claims that were stronger than the evidence justified.
3. **What single change would prevent this next time?** Nothing beyond following the existing prompt more literally; the current prompt already says to use only `[fact]`, `[inference]`, or `[assumption]` and to avoid overclaiming.
4. **Is this a pattern?** Yes; it matches the known review pattern that research items fail quickly when they drift from the accepted epistemic labels or claim-strength discipline.
