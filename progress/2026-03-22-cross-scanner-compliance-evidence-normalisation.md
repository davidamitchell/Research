# 2026-03-22 — Research Loop (cross-scanner-compliance-evidence-normalisation)

**Completed:**

Research item:
- `Research/completed/2026-03-22-cross-scanner-compliance-evidence-normalisation.md` — completed; the item concludes that heterogeneous compliance scanners in GitHub Actions should be unified through a SARIF-aligned evidence contract, split severity dimensions, and a central waiver registry rather than through a single flattened severity field or tool-native suppressions alone. It also recommends layered GitHub presentation surfaces: code scanning for SARIF-capable location-aware findings, checks and annotations for tools like GraphQL Inspector, and summaries or adapters for tools such as SQLFluff.

Sources consulted:
- https://docs.oasis-open.org/sarif/sarif/v2.1.0/sarif-v2.1.0.html (SARIF 2.1.0 interchange model, suppression concepts, and result correlation)
- https://docs.github.com/en/code-security/reference/code-scanning/sarif-files/sarif-support-for-code-scanning (GitHub SARIF ingestion, fingerprinting, path stability, and display constraints)
- https://the-guild.dev/graphql/inspector/docs/products/action (GraphQL Inspector action behavior, annotations, change output, and breaking-change gating)

## Mini-Retro

1. **Did the process work?** Yes. The repo workflow for draft review and completion worked end-to-end, and the two-pass review loop caught citation-discipline issues before final completion.
2. **What slowed down or went wrong?** The main slowdown was review strictness around meta-claims and acronym expansion, especially where shorthand citations like `Basis: §2.1-§2.5` were not accepted.
3. **What single change would prevent this next time?** Default to URL-level citations even for synthesis and consistency-check bullets, and avoid negative meta-claims about the whole source set unless they are phrased as source-based inferences.
4. **Is this a pattern?** Yes. It matches the known recurring pattern in the instructions that research review treats claim-bearing tables, synthesis, and consistency-check prose as full citation-discipline scope rather than as informal commentary.
