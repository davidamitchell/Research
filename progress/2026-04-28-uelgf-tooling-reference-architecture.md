# 2026-04-28 -- Research Loop (uelgf-tooling-reference-architecture)

**Completed:**

Research item:
- `Research/completed/2026-04-28-uelgf-tooling-reference-architecture.md` -- completed; the item concludes that a deployable Universal Entity Lifecycle Governance Framework (UELGF) rail in a regulated financial institution is best implemented as a central policy-and-evidence hub with local enforcement spokes. It specifies signed Open Policy Agent (OPA) bundles for policy publication and decision traceability, OpenTelemetry (OTel) Collectors for telemetry transport, and centrally minted short-lived workload credentials plus Policy Enforcement Point (PEP)-side deny hooks as the practical containment backbone, while treating Cedar, SPIFFE, and Vault as optional hardening layers rather than mandatory first-release components.

Sources consulted:
- https://www.openpolicyagent.org/docs/management-bundles (policy bundle distribution and activation semantics)
- https://opentelemetry.io/docs/collector/architecture/ (collector pipeline model for the evidence plane)
- https://developer.hashicorp.com/vault/docs/concepts/lease (leased credentials and revocation mechanics)

## Mini-Retro

1. **Did the process work?** Yes; the research workflow plus automated review converged on a defensible architecture after one substantive revision cycle.
2. **What slowed down or went wrong?** The strict review gate flagged a few places where confidence language and rollout recommendations were stronger than the external evidence actually justified.
3. **What single change would prevent this next time?** Nothing new beyond the current checklist; the existing confidence-evidence alignment rules already pointed at the right fixes.
4. **Is this a pattern?** Yes; it matches the known pattern that comparative claims and high-confidence labels often outrun the independence of the supporting sources.
