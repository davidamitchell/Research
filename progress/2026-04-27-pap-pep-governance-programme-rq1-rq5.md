# 2026-04-27 -- Add backlog items: PAP/PEP governance programme (RQ1–RQ5)

**Completed:**
- `Research/backlog/2026-04-27-pap-dynamic-policy-profiling-proportionality.md` — added from issue; asks how a Policy Administration Point (PAP) can dynamically map a governed asset's invariants and Confidentiality, Integrity, and Availability (CIA) ratings to a proportional and lifecycle-aware Policy Enforcement Point (PEP) topology, formalised as a monotone lattice mapping function
- `Research/backlog/2026-04-27-pdp-universal-policy-synchronisation-integrity.md` — added from issue; asks what mechanism ensures the Policy Decision Point (PDP) evaluates a governed asset against logically identical policy at every lifecycle phase, preventing silent Governance Decay via content-addressed policy bundles
- `Research/backlog/2026-04-27-out-of-band-policy-invalidation-remediation.md` — added from issue; asks what consistency model governs PAP-to-PEP policy propagation for assets already in Delivery or Operation and defines the minimum viable kill-switch architecture
- `Research/backlog/2026-04-27-pip-invariant-anomaly-detection.md` — added from issue; asks how the Policy Information Point (PIP) can detect when a governed asset's transient operating context is suppressing a permanent invariant and what decision signal it surfaces to the Policy Decision Point (PDP)
- `Research/backlog/2026-04-27-cryptographic-intent-preservation-runtime-evaluation.md` — added from issue; asks what representation of original intent captured at Getting Started is simultaneously cryptographically verifiable and semantically stable enough to function as a meaningful evaluation baseline across the full operational lifecycle

**Dependency ordering encoded:**
- RQ1 (PAP dynamic profiling) blocks RQ2, RQ3, and RQ4 — it is the foundational item; all downstream RQs require the PEP topology and invariant registration it produces
- RQ2 (policy synchronisation) additionally blocks RQ3 and RQ4 — RQ3 needs the synchronisation baseline to detect when out-of-band propagation is needed; RQ4 needs assurance that the invariant set it checks is current
- RQ4 (PIP anomaly detection) blocks RQ5 — the intent representation produced by RQ5 must be evaluable by the PIP's anomaly detection model

## Mini-Retro

1. **Did the process work?** Yes. The five research questions were well-scoped and self-contained in the issue, with explicit dependency ordering and seed directions. The structured format translated cleanly into the backlog template. All acronyms expanded on first use in each item.

2. **What slowed down or went wrong?** Nothing significant. The issue was unusually well-specified, with cross-references, seed directions, and dependency declarations all provided. The only judgement call was encoding the `blocks` field correctly from the stated dependency ordering (which the issue expressed as "Depends on" rather than "Blocks").

3. **What single change would prevent this next time?** Nothing to prevent — this was smooth. If there were a pattern to watch: issues with multiple questions should always check whether the questions form a dependency graph (as here) or are independent, and encode that graph in `blocks` before committing.

4. **Is this a pattern?** The multi-question issue with internal dependency ordering is a distinct issue type from a single research request. The handling here (one backlog item per question, dependency graph in `blocks`) is the right approach and worth keeping consistent.

5. **Does any documentation need updating?** No documentation changes required. The process followed the instructions exactly.

6. **Do the default instructions need updating?** No updates required. The instructions already handle this case correctly: "When assigned to a new research request issue: apply the `research-question` skill, add a backlog item, open a PR — stop."
