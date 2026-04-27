---
title: "Policy Administration Point (PAP) dynamic policy profiling and proportionality: mapping asset metadata to a lifecycle-aware Policy Enforcement Point (PEP) topology scaled by inherent risk"
added: 2026-04-27T00:55:35+00:00
status: backlog
priority: high
blocks: [2026-04-27-pdp-universal-policy-synchronisation-integrity, 2026-04-27-out-of-band-policy-invalidation-remediation, 2026-04-27-pip-invariant-anomaly-detection]
tags: [pbac, pap, pep, policy-enforcement, agentic-ai, cia-classification, lifecycle-governance, lattice-access-control, capability-security, proportionality]
started: ~
completed: ~
output: [knowledge]
---

# Policy Administration Point (PAP) dynamic policy profiling and proportionality: mapping asset metadata to a lifecycle-aware Policy Enforcement Point (PEP) topology scaled by inherent risk

## Research Question

How can a Policy Administration Point (PAP) dynamically map a governed asset's metadata — specifically its invariants and Confidentiality, Integrity, and Availability (CIA) ratings — to a proportional and lifecycle-aware set of Policy Enforcement Points (PEPs), such that the depth of governance applied scales with the asset's inherent risk profile rather than being applied uniformly?

## Scope

**In scope:**
- The computational mechanism by which the PAP reads an asset's declared invariants (e.g. "handles Personally Identifiable Information (PII)", "executes financial transactions") and CIA classification
- Derivation of a differentiated PEP topology across the four lifecycle phases: Getting Started, Development, Delivery, and Operation
- Formalisation of the mapping function from (invariant-set × CIA-rating × lifecycle-phase) to PEP-topology
- Conditions under which CIA-High agentic systems face hard gates at Getting Started and Operation that low-risk utility agents do not
- Lattice-based access control theory (Bell-LaPadula extensions) as a candidate formalisation framework
- Capability-based security theory applied to invariant declarations for deriving minimum required PEP coverage
- Policy-Based Access Control (PBAC) literature review scoped to the static-vs-dynamic policy selection gap

**Out of scope:**
- Implementation of a specific PAP product or vendor solution
- Detailed runtime enforcement mechanics (covered by downstream RQ3)
- Policy synchronisation across phases (covered by RQ2)
- Anomaly detection in the Policy Information Point (PIP) (covered by RQ4)

**Constraints:**
- The mapping function must be defined, not merely described as a desired outcome — formalisation is required
- The research must ground the proportionality argument in empirical evidence, not just theoretical assertion; use the Systems Capability Debt framing where available
- This is the foundational Research Question (RQ) — all other RQs in this set depend on the invariant registration and PEP topology produced here

## Context

Current Policy-Based Access Control (PBAC) literature treats policy selection as static configuration: an administrator assigns policies to assets at setup time and the system applies them uniformly regardless of the asset's actual risk profile. The gap is the computational mechanism by which a PAP reads an asset's declared invariants and CIA classification at registration time, then derives — dynamically and differentially — the correct PEP topology for each lifecycle phase.

This gap matters because agentic AI systems inherit worst-case permission sets without the natural human rate-limiting that previously bounded blast radius, making CIA-High agents qualitatively more dangerous than equivalent human-operated systems. Uniform gate application either over-governs low-risk utilities (delivery cost) or under-governs high-risk agents (safety failure). The mapping function is the mechanism that resolves this tradeoff.

The research directly builds on the Aligned Decision-Making framework and the 8-layer context architecture it defines. It is the foundational item in a five-question programme on Policy Administration Point (PAP) and Policy Enforcement Point (PEP) governance for agentic AI.

## Approach

1. **PBAC literature gap analysis:** Survey current PBAC literature to confirm the static-configuration characterisation and identify any partial solutions (dynamic policy selection, risk-adaptive access control, attribute-based systems). Locate the specific gap in the mapping function.
2. **Lattice formalisation:** Model the mapping function as a monotone lattice over (invariant-set × CIA-rating × lifecycle-phase) → PEP-topology, drawing on Bell-LaPadula extensions and lattice-based access control (LBAC). Define the partial ordering over invariant sets and the monotonicity requirement (higher CIA rating implies richer PEP topology).
3. **Capability-based derivation:** Treat invariants as capability declarations. Apply capability-based security theory to derive the minimum required PEP coverage for each invariant class. Identify which invariants trigger hard gates and which permit soft gates.
4. **Lifecycle-phase gate specification:** For each combination of CIA rating and invariant class, specify the PEP topology at each lifecycle phase (Getting Started, Development, Delivery, Operation). Identify the conditions under which a phase transition requires a hard gate.
5. **Empirical grounding:** Use the Systems Capability Debt (SCD) framing to quantify the governance gap when proportionality is absent — draw on the empirical evidence from the completed SCD items to ground why uniform gates fail in practice.
6. **Synthesis:** Produce a formal specification of the mapping function, a worked example for a CIA-High PII-handling agentic system, and decision criteria for PAP implementors.

## Sources

- [ ] [NIST SP 800-162 — Guide to Attribute-Based Access Control (ABAC)](https://csrc.nist.gov/pubs/sp/800/162/final) — foundational ABAC/PBAC reference for current state of dynamic policy selection
- [ ] [NIST SP 800-53 Rev 5 — Security and Privacy Controls](https://csrc.nist.gov/pubs/sp/800/53/r5/final) — AC-2, AC-3, AC-6 (least privilege) and PM-17 controls relevant to proportional enforcement
- [ ] [Bell-LaPadula model — original papers and lattice-based access control extensions](https://en.wikipedia.org/wiki/Bell%E2%80%93LaPadula_model) — lattice ordering theory for formalising the mapping function
- [ ] [Capability-based security — literature survey](https://en.wikipedia.org/wiki/Capability-based_security) — capability model for deriving minimum PEP coverage from invariant declarations
- [ ] [Aligned Decision-Making framework — completed item](https://davidamitchell.github.io/Research/research/2026-03-15-context-layers-aligned-decisions-synthesis.html) — 8-layer context architecture the mapping function must encode
- [ ] [Access control amplification under agentic operations — completed item](https://davidamitchell.github.io/Research/research/2026-04-26-access-control-amplification-agentic-operations.html) — establishes why CIA-High agents require disproportionate PEP coverage
- [ ] [Implicit rate-limiting controls removed by agentic AI — completed item](https://davidamitchell.github.io/Research/research/2026-04-26-implicit-rate-limiting-controls-agentic-ai-removal.html) — blast radius argument for proportional gating
- [ ] [Regulatory preconditions for agentic AI — completed item](https://davidamitchell.github.io/Research/research/2026-04-26-agentic-ai-regulatory-preconditions-control-failure-assessment.html) — APRA CPS 230, DORA, PCI-DSS, NIST non-negotiable hard gate requirements
- [ ] [Adaptive Policy-Based Authorization (APBA) — completed item](https://davidamitchell.github.io/Research/research/2026-03-16-adaptive-policy-authorization-compliance.html) — NIST SP 800-53 dynamic access control as the closest existing architectural analogue
- [ ] [Systems Capability Debt empirical evidence — completed item](https://davidamitchell.github.io/Research/research/2026-04-26-systems-capability-debt-citizen-development-empirical-evidence.html) — empirical grounding for uniform-gate failure

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
