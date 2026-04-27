---
title: "Universal Entity Lifecycle Governance Framework (UELGF): policy architecture — PAP, PDP, PEP, PIP component design, the 8-layer organisational context model, policy independence guarantee, scope boundary mechanism, and kill switch"
added: 2026-04-27T01:28:25+00:00
status: backlog
priority: high
blocks: [2026-04-27-uelgf-synthesis-complete-framework]
tags: [uelgf, policy-architecture, pap, pdp, pep, pip, policy-independence, scope-boundary, kill-switch, organisational-context, policy-as-code, regulated-banking, xacml, opa]
started: ~
completed: ~
output: [knowledge]
---

# Universal Entity Lifecycle Governance Framework (UELGF): policy architecture — PAP, PDP, PEP, PIP component design, the 8-layer organisational context model, policy independence guarantee, scope boundary mechanism, and kill switch

## Research Question

What policy architecture — covering Policy Administration Point (PAP), Policy Decision Point (PDP), Policy Enforcement Point (PEP), and Policy Information Point (PIP) — and what 8-layer organisational context model should the UELGF specify to provide architecturally enforced policy independence (policy lifecycle entirely separate from entity lifecycle), a machine-checkable scope boundary mechanism replacing intent-based reasoning, and a kill switch operable at single-entity, entity-class, and entity-type levels?

## Scope

**In scope:**
- Formal specification of the four policy architecture components (PAP, PDP, PEP, PIP) and the architectural mandate for their separation: PAP as authoritative policy source, PDP as stateless evaluator, PEP as runtime enforcement point, PIP as entity registry and runtime signal store
- The mechanism by which policy changes in the PAP propagate immediately to the PDP and become active for all entities without any action by entity owners — the policy independence guarantee
- The 8-layer organisational context model: Layer 1 Regulatory, Layer 2 Risk Appetite, Layer 3 Values, Layer 4 Strategy, Layer 5 Standards, Layer 6 Patterns, Layer 7 Procedures, Layer 8 Scope (the entity's declared scope boundary)
- The scope boundary mechanism: how declared scope at scaffold generation is formalised as a machine-checkable specification, how the PDP evaluates whether a specific action is within that scope, and why out-of-scope actions are scope violations requiring escalation rather than simple policy denials
- The kill switch mechanism: process for immediate licence-to-operate suspension at single entity, entity class, or entity type and CIA tier levels; automated consequences (credential revocation, action queue draining, dependency notification, owner alert)
- The policy independence guarantee under Layer 1 regulatory change: mechanism by which a new regulatory obligation immediately revokes the licence to operate of any entity whose current behaviour would violate it
- The relationship between the 8-layer context model and the CIA governance profile: which layers apply as hard constraints for each CIA tier

**Out of scope:**
- Entity taxonomy and CIA classification (covered by `2026-04-27-uelgf-entity-taxonomy-cia-classification`)
- Rail interface specifications and scaffold generation (covered by `2026-04-27-uelgf-governed-golden-rails`)
- Runtime feedback loop signal processing (covered by `2026-04-27-uelgf-runtime-feedback-loop`) — though the PEP/PIP interaction is in scope
- Foundational principles (covered by `2026-04-27-uelgf-foundational-definitions-principles`)

**Constraints:**
- The PAP/PDP/PEP/PIP architecture must be specified at sufficient precision to serve as an engineering specification for implementation — not just a conceptual model
- The policy independence guarantee must be architecturally enforced, not procedurally relied upon — the specification must identify the mechanism, not merely state the requirement
- The scope boundary mechanism must be machine-checkable: a human intent statement is not sufficient; the specification must produce a format that a PDP can evaluate deterministically
- The kill switch must operate within a defined maximum latency from trigger to effect — the specification must state the latency requirement and how it is achieved

## Context

The policy architecture is the infrastructure beneath all rails. Every PEP enforcement event, every licence-to-operate evaluation, every kill switch activation, and every policy change propagation depends on this architecture functioning correctly. The PAP/PDP/PEP/PIP separation is a foundational pattern from XACML and has analogues in modern policy-as-code tooling (Open Policy Agent, AWS Verified Permissions, Cedar), but the UELGF specification must go beyond architectural pattern to operational requirement: what does "policy independence" mean precisely, how is it verified, what is the latency budget, and what happens when the PDP is unavailable?

The 8-layer context model is the organisational knowledge structure that the PDP draws on. Without explicit layering, policy conflicts are unresolvable (is a strategic initiative that would violate a regulatory obligation permitted?). The layer ordering establishes precedence. Layer 8 (entity scope) is the only layer that varies per entity — the other seven are organisational constants that apply to all entities equally.

Prior completed research directly informs this item:
- [Adaptive policy authorisation and compliance](https://davidamitchell.github.io/Research/research/2026-03-19-adaptive-policy-authorization-compliance.html) — policy engine architecture patterns
- [AI and low-code governance enforcement architecture](https://davidamitchell.github.io/Research/research/2026-04-26-ai-lowcode-governance-enforcement-architecture.html) — enforcement architecture in practice
- [Policy coherence as machine-checkable prerequisite](https://davidamitchell.github.io/Research/research/2026-04-26-policy-coherence-machine-checkable-prerequisite.html) — the prerequisite condition for the PDP to function correctly

## Approach

1. **PAP/PDP/PEP/PIP architecture specification:** Survey the XACML 3.0 specification, Open Policy Agent architecture, AWS Cedar and Verified Permissions, and Azure Policy to produce a formal component specification for each of the four policy architecture components. For each component, specify: responsibilities, interfaces, state model (stateless vs stateful), dependency relationships, and failure modes.
2. **Policy independence mechanism:** Identify the architectural mechanism(s) that enforce policy independence — the property that a policy change in the PAP activates immediately for all entities without any entity owner action. Survey how this is achieved in event-driven policy architectures (OPA with bundle polling, AWS Config with remediation automations, Cedar policy stores with push distribution). Specify the propagation latency requirement and the mechanism to achieve it.
3. **8-layer context model formalisation:** Survey whether existing context models in policy-as-code tooling (OPA context data, XACML environment attributes, ABAC attribute hierarchies) provide structural analogues for the 8-layer model. For each layer, specify: the type of policy content it holds, who is responsible for authoring it, the update frequency, and the precedence rule governing conflicts with adjacent layers.
4. **Scope boundary as machine-checkable specification:** Survey existing machine-checkable scope representations — OAuth 2.0 scope strings, XACML resource attributes, AWS IAM (Identity and Access Management) policy conditions, SPIFFE/SPIRE SVID (Secure Production Identity Framework for Everyone / SPIFFE Verifiable Identity Document) workload identities — to determine which representations are precise enough to support deterministic PDP evaluation. Produce the scope specification format for the UELGF, distinguishing scope violations (action within policy but outside entity's registered scope) from policy denials (action prohibited by organisational policy regardless of scope).
5. **Kill switch mechanism specification:** Survey how emergency suspension mechanisms work in comparable systems: OAuth 2.0 token revocation (RFC 7009), certificate revocation (Online Certificate Status Protocol (OCSP) and Certificate Revocation List (CRL)), AWS IAM policy boundary removal. Specify the UELGF kill switch as a sequence of operations with latency budget for each operation and a rollback mechanism.
6. **Layer 1 regulatory change propagation:** Specify the mechanism by which a Layer 1 regulatory change — authored in the PAP — immediately evaluates all currently licensed entities against the new requirement and suspends those whose behaviour would violate it. This is the policy independence guarantee under regulatory change and must be specified as an automated process, not a manual review.

## Sources

- [ ] [OASIS XACML 3.0 Core Specification](https://docs.oasis-open.org/xacml/3.0/xacml-3.0-core-spec-os-en.html) — canonical PAP/PDP/PEP/PIP architecture definition
- [ ] [Open Policy Agent — architecture documentation](https://www.openpolicyagent.org/docs/latest/philosophy/) — policy-as-code implementation of policy independence
- [ ] [AWS Cedar — policy language specification](https://docs.cedarpolicy.com/) — machine-checkable scope boundary in practice
- [ ] [AWS Verified Permissions documentation](https://docs.aws.amazon.com/verifiedpermissions/latest/userguide/what-is-avp.html) — PDP-as-a-service implementation
- [ ] [RFC 7009 — OAuth 2.0 Token Revocation](https://datatracker.ietf.org/doc/html/rfc7009) — credential revocation mechanism for kill switch
- [ ] [NIST SP 800-162 — Guide to Attribute Based Access Control (ABAC) Definition and Considerations](https://csrc.nist.gov/pubs/sp/800/162/final) — attribute-based policy evaluation model
- [ ] [Adaptive policy authorisation and compliance — completed item](https://davidamitchell.github.io/Research/research/2026-03-19-adaptive-policy-authorization-compliance.html) — policy engine architecture patterns
- [ ] [AI and low-code governance enforcement architecture — completed item](https://davidamitchell.github.io/Research/research/2026-04-26-ai-lowcode-governance-enforcement-architecture.html) — enforcement architecture evidence
- [ ] [Policy coherence as machine-checkable prerequisite — completed item](https://davidamitchell.github.io/Research/research/2026-04-26-policy-coherence-machine-checkable-prerequisite.html) — prerequisite conditions for PDP function
- [ ] [SPIFFE/SPIRE workload identity specification](https://spiffe.io/docs/latest/spiffe-about/overview/) — machine identity as the foundation for scope boundary evaluation
- [ ] [NIST SP 800-207 Zero Trust Architecture — policy engine design](https://csrc.nist.gov/pubs/sp/800/207/final) — zero trust policy engine as architectural analogue

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
