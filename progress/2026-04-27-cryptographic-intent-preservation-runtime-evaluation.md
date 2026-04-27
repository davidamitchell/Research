# 2026-04-27 -- Research Loop (cryptographic-intent-preservation-runtime-evaluation)

**Completed:**

Research item:
- `Research/completed/2026-04-27-cryptographic-intent-preservation-runtime-evaluation.md` -- completed; the item concludes that original asset intent is preserved best by a dual artefact: a human-readable intent statement plus a digest-addressed machine-readable declaration that remains the canonical runtime identity. It also concludes that legitimate lifecycle change should be modeled through append-only signed amendments, so policy evaluation, anomaly detection, and governance all reference the same immutable baseline.

Sources consulted:
- https://iang.org/papers/ricardian_contract.html (Ricardian Contract model for human-readable plus machine-readable agreement structure)
- https://www.w3.org/TR/vc-data-model/ (Verifiable Credentials Data Model for typed claims and interoperable credential structure)
- https://github.com/in-toto/attestation/blob/main/spec/v1/statement.md (in-toto statement model for digest-bound subject identity and attestable lineage)

## Mini-Retro

1. **Did the process work?** Yes, the two-pass review loop caught exactly the places where synthesis claims had outrun their evidence and forced the item back into source-calibrated language.
2. **What slowed down or went wrong?** The main slowdown was review-fix iteration around confidence calibration and around `§7`, where process-status prose looked like externally supported claims instead of document metadata.
3. **What single change would prevent this next time?** Nothing new; the current prompt already tells authors to rewrite `§7` into metadata fragments and to downgrade synthesis claims when the evidence is mostly compositional.
4. **Is this a pattern?** Yes, but it matches existing recurring patterns already covered in the instructions: acronym expansion, confidence overstatement on synthesis claims, and self-referential review prose.
