# 2026-04-27 -- Research Loop (out-of-band-policy-invalidation-remediation)

**Completed:**

Research item:
- `Research/completed/2026-04-27-out-of-band-policy-invalidation-remediation.md` -- completed; the item concludes that policy invalidation for already-operating assets is a partition-time control decision, not a pure synchronization problem. It recommends consistency-first invalidation for Layer 1 regulatory and CIA-High confidentiality or integrity triggers, a signed revocation-state design patterned on CRL and OCSP semantics, and external containment paths for non-cooperative or bypassed assets.

Sources consulted:
- https://www.comp.nus.edu.sg/~gilbert/pubs/BrewersConjecture-SigAct.pdf (formal CAP theorem proof)
- https://www.rfc-editor.org/rfc/rfc6960 (OCSP freshness and responder semantics)
- https://doi.org/10.6028/NIST.SP.800-53r5 (incident handling and integrity controls)

## Mini-Retro

1. **Did the process work?** Yes, the research loop worked end to end: gather sources, draft, run review, fix issues, re-run review, then complete the item.
2. **What slowed down or went wrong?** Review iterations caught first-use term-definition issues and confidence-level overclaims after the core argument was already sound.
3. **What single change would prevent this next time?** Nothing new, the existing acronym and domain-term self-review checks were the right control and just need to be applied more aggressively before the first draft push.
4. **Is this a pattern?** Yes, it matches the repo's known recurring pattern around first-use expansion and definition discipline rather than revealing a new failure class.
