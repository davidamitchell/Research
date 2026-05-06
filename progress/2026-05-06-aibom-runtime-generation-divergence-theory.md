# 2026-05-06 -- Research Loop (aibom-runtime-generation-divergence-theory)

**Completed:**

Research item:
- `Research/completed/2026-05-06-aibom-runtime-generation-divergence-theory.md` - completed; the item concludes that a runtime-observed Artificial Intelligence Bill of Materials (AIBOM) should be modelled as an event-sourced provenance graph plus decision-point state snapshots rather than as a flat inventory. It also defines the main divergence surfaces between declared and observed AIBOMs, especially retrieval, memory, authority, topology, and control-policy divergence, and explains why evidence-preserving replay is stronger than live behavioural re-execution for audit.

Sources consulted:
- https://www.w3.org/TR/prov-overview/ (provenance model and reproducibility concepts)
- https://opentelemetry.io/docs/concepts/signals/traces/ (trace, span, and correlation model)
- https://docs.aws.amazon.com/bedrock/latest/userguide/trace-events.html (production agent trace schema example)

## Mini-Retro

1. **Did the process work?** Yes. The two-pass review loop caught a few over-strong synthesis labels and a mirrored-section miss before completion.
2. **What slowed down or went wrong?** The seeded provenance paper titles did not resolve to retrievable primary sources, and one Analysis fix was applied only in Findings before the mirror in `§6 Synthesis`.
3. **What single change would prevent this next time?** Nothing new is needed in the prompt; the existing parity and search-note rules were sufficient once followed strictly.
4. **Is this a pattern?** Partly. It matches the existing pattern that synthesis claims and mirrored sections need stricter self-audit than direct evidence bullets.
