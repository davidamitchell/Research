# 2026-04-27 -- Research Loop (pap-dynamic-policy-profiling-proportionality)

**Completed:**

Research item:
- `Research/completed/2026-04-27-pap-dynamic-policy-profiling-proportionality.md` -- completed; the item concludes that existing Attribute-Based Access Control (ABAC) and eXtensible Access Control Markup Language (XACML) models are already dynamic at request time, so the real gap is not dynamic authorization itself but a missing explicit Policy Administration Point (PAP) rule for mapping invariants and Confidentiality, Integrity, and Availability (CIA) labels to lifecycle-specific enforcement topology. It proposes a monotone partial-order mapping that distributes gates across registration, development, delivery, runtime authorization, rate control, and stop authority rather than collapsing proportionality into one linear score or one runtime checkpoint.

Sources consulted:
- https://csrc.nist.gov/pubs/sp/800/162/final (National Institute of Standards and Technology (NIST) Attribute-Based Access Control guide)
- https://docs.oasis-open.org/xacml/3.0/xacml-3.0-core-spec-os-en.html (OASIS XACML 3.0 core specification)
- https://csf.tools/reference/nist-sp-800-53/r5/ac/ac-24/ (NIST SP 800-53 AC-24 access control reference)

## Mini-Retro

1. **Did the process work?** Yes, the research-loop workflow worked as intended: draft, automated review, targeted fixes, completion, and synthesis back into `learnings.md`.
2. **What slowed down or went wrong?** The main friction was review-sensitive labeling, where standards-compatible synthesis claims initially read like direct facts and had to be downgraded to inferences with lower confidence.
3. **What single change would prevent this next time?** Nothing new needs to change in the prompt, because the existing self-review already covers this class of issue; the fix was to apply that rule more strictly before triggering review.
4. **Is this a pattern?** Mildly, but it matches an existing pattern in the instructions: synthesis claims around governance surfaces often need stricter `[inference]` labeling than they first appear to require.
