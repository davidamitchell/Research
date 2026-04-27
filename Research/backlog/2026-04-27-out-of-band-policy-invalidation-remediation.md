---
title: "Out-of-band policy invalidation and remediation: consistency model for Policy Administration Point (PAP)-to-Policy Enforcement Point (PEP) propagation and minimum viable kill-switch architecture"
added: 2026-04-27T00:55:35+00:00
status: backlog
priority: high
blocks: []
tags: [pbac, pap, pep, policy-invalidation, kill-switch, distributed-systems, cap-theorem, consistency-model, agentic-ai, cia-classification, operational-risk, lifecycle-governance]
started: ~
completed: ~
output: [knowledge]
---

# Out-of-band policy invalidation and remediation: consistency model for Policy Administration Point (PAP)-to-Policy Enforcement Point (PEP) propagation and minimum viable kill-switch architecture

## Research Question

What consistency model governs Policy Administration Point (PAP)-to-Policy Enforcement Point (PEP) policy propagation for assets already in Delivery or Operation, under what conditions does synchronous invalidation override eventual consistency guarantees, and what is the minimum viable kill-switch architecture that satisfies those conditions without producing a liveness failure in the operational system?

## Scope

**In scope:**
- Characterisation of the CAP theorem (Consistency, Availability, Partition tolerance) tradeoff for policy propagation: when to choose Consistency + Partition tolerance (CP) vs. Availability + Partition tolerance (AP)
- Conditions — by regulatory trigger type (Layer 1 Regulatory, Layer 2 Values), Confidentiality, Integrity, and Availability (CIA) rating, and invariant class — under which the system must collapse to synchronous invalidation regardless of liveness cost
- Conditions under which eventual consistency is an acceptable policy propagation model
- Kill-switch architecture design: revocation certificate model (analogous to X.509 Certificate Revocation List (CRL)/Online Certificate Status Protocol (OCSP)), signed revocation issuance, PEP revocation-status checking, configurable staleness tolerance by CIA class
- Grace period protocol: restricted operating mode on invalidation (reduced permission scope, mandatory human-in-the-loop on consequential actions) as an alternative to hard termination
- The operational population the kill-switch must reach: Shadow IT assets, Zombie Agents, and assets that bypassed the deployment pipeline entirely
- Adversarial non-cooperation: what happens when the asset being invalidated does not cooperate, and the operational PEP enforcing it may be unreachable

**Out of scope:**
- Policy synchronisation for assets still in Development (covered by RQ2)
- The PAP mapping function (covered by RQ1)
- Anomaly detection in the Policy Information Point (PIP) (covered by RQ4)
- Detailed cryptographic binding of original intent (covered by RQ5)
- Jurisdiction-specific legal analysis beyond what is needed to characterise the regulatory trigger taxonomy

**Constraints:**
- Depends on RQ1 (PEP topology) and RQ2 (synchronisation baseline to detect when out-of-band propagation is needed)
- The kill-switch architecture must work around assets that bypassed the deployment pipeline entirely — the pipeline cannot be assumed as the propagation channel for out-of-band invalidation
- The liveness cost of synchronous invalidation must be explicitly quantified, not dismissed; the research must produce a decision framework that a risk committee can apply
- The adversarial element must be explicitly addressed: the asset being invalidated may not cooperate

## Context

When a Layer 1 (Regulatory) or Layer 2 (Values) policy changes, the PAP must reach already-deployed assets. This is a distributed systems consistency problem with an adversarial element. The tradeoff is fundamental: strong consistency means operational PEPs block until propagation confirms (liveness risk); eventual consistency means a window exists where assets operate under invalidated policy (safety risk).

Shadow IT sprawl and Zombie Agent findings establish the operational population the kill-switch must reach — including assets the organisation may not have full visibility over. The deployment pipeline as the only enforceable control gate item establishes that out-of-band invalidation must work around assets that bypassed the pipeline entirely. The access control amplification finding establishes the safety argument for why synchronous invalidation must be possible for CIA-High assets: the blast radius of an agent operating under invalidated policy is not bounded by human attention.

## Approach

1. **CAP theorem mapping:** Explicitly map the kill-switch design space using the CAP theorem. For CIA-High assets under Layer 1 regulatory triggers, characterise the CP choice and its liveness implications. For lower-risk assets under Layer 5 operational triggers, characterise the AP choice and the acceptable eventual consistency window.
2. **Revocation certificate architecture:** Design the kill-switch as a revocation certificate system. Define: (a) the PAP revocation issuance protocol (signed revocation with asset identifier, invalidation timestamp, and replacement policy reference); (b) the PEP revocation-status checking protocol; (c) configurable staleness tolerance parameters by CIA class; (d) the behaviour of a PEP that cannot reach the revocation service.
3. **Grace period protocol:** Define the grace period protocol for assets that cannot be hard-terminated without liveness failure. Specify: (a) the restricted operating mode (what operations remain permitted, what require human-in-the-loop); (b) the grace period duration by CIA class and trigger type; (c) the escalation path when the grace period expires without remediation.
4. **Unreachable and non-cooperative asset handling:** Define the response protocol for assets that are unreachable (network partition) or non-cooperative (adversarially resisting invalidation). Draw on X.509 Certificate Revocation List (CRL) and Online Certificate Status Protocol (OCSP) stapling models for the offline-revocation-check analogue.
5. **Shadow IT and pipeline-bypass population:** Characterise the kill-switch reach problem for assets that bypassed the deployment pipeline. Define what alternative propagation channels exist (network-layer controls, runtime intercept, platform-level revocation) and their reliability.
6. **Systems-thinking liveness model:** Apply the backpressure and Theory of Constraints framing to model the liveness cost of synchronous invalidation as a deliberate constraint injection. Quantify the throughput impact and define the operational conditions under which the cost is acceptable.
7. **Synthesis:** Produce a decision framework mapping (trigger-type × CIA-rating × invariant-class) to (consistency-model × kill-switch-mechanism × grace-period), a revocation certificate schema, and an incident response protocol for out-of-band invalidation events.

## Sources

- [ ] [Shadow IT sprawl and Zombie Agent findings — completed item](https://davidamitchell.github.io/Research/research/2026-04-26-systems-capability-debt-agentic-ai-risk-synthesis.html) — operational population the kill-switch must reach
- [ ] [Business-led low-code agent governance — completed item](https://davidamitchell.github.io/Research/research/2026-04-24-business-led-low-code-agent-governance.html) — Zombie Agent population and visibility gap
- [ ] [Deployment pipeline as governed control gate — completed item](https://davidamitchell.github.io/Research/research/2026-04-26-deployment-pipeline-citizen-development-governed-gate.html) — pipeline as the only reliable enforcement point; out-of-band invalidation must work around assets that bypassed it
- [ ] [Access control amplification under agentic operations — completed item](https://davidamitchell.github.io/Research/research/2026-04-26-access-control-amplification-agentic-operations.html) — safety argument for synchronous invalidation of CIA-High assets
- [ ] [Backpressure and Theory of Constraints — completed item](https://davidamitchell.github.io/Research/research/2026-04-01-backpressure-theory-of-constraints.html) — systems-thinking language for liveness cost of synchronous invalidation
- [ ] [CAP theorem — Brewer's original conjecture and Gilbert-Lynch proof](https://dl.acm.org/doi/10.1145/564585.564601) — formal basis for consistency/availability tradeoff characterisation
- [ ] [X.509 Certificate Revocation List (CRL) and Online Certificate Status Protocol (OCSP) — RFC 5280 and RFC 6960](https://www.rfc-editor.org/rfc/rfc5280) — revocation certificate architecture analogue
- [ ] [NIST SP 800-53 Rev 5 — SI-7 (Software, Firmware, and Information Integrity) and IR-4 (Incident Handling)](https://csrc.nist.gov/pubs/sp/800/53/r5/final) — regulatory basis for invalidation and incident response requirements
- [ ] [DORA — Regulation (EU) 2022/2554 — Chapter II ICT risk management and Article 17 ICT-related incident management](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32022R2554) — regulatory trigger characterisation for Layer 1 invalidation requirements

---

## Research Skill Output

*(Full output from running the research skill — retained verbatim in the completed item. §§0–5 are the investigation; §6 seeds the Findings section below.)*

### §0 Initialise

-

### §1 Question Decomposition

-

### §2 Investigation

-

### §3 Reasoning

-

### §4 Consistency Check

-

### §5 Depth and Breadth Expansion

-

### §6 Synthesis

*(This section seeds the Findings below.)*

**Executive summary:**

**Key findings:**

**Evidence map:**

**Assumptions:**

**Analysis:**

**Risks, gaps, uncertainties:**

**Open questions:**

### §7 Recursive Review

-

---

## Findings

*(Populated from §6 Synthesis above.)*

### Executive Summary

### Key Findings

1.
2.

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| | | high / medium / low | |

### Assumptions

- **Assumption:** ... **Justification:** ...

### Analysis

### Risks, Gaps, and Uncertainties

-

### Open Questions

-

---

## Output

*(Fill in when completing — what was produced as a result of this research?)*

- Type: knowledge
- Description:
- Links:
