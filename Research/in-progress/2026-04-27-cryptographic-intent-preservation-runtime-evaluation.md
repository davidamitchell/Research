---
title: "Cryptographic preservation and runtime evaluation of original intent: a representation formalism for Getting Started phase intent that is simultaneously verifiable and semantically stable across the full operational lifecycle"
added: 2026-04-27T00:55:35+00:00
status: reviewing
priority: high
blocks: []
tags: [pbac, pdp, pip, intent-preservation, cryptographic-binding, ricardian-contract, formal-specification, agentic-ai, lifecycle-governance, dikw, intent-driven-development, semantic-stability]
started: 2026-04-27T09:28:58+00:00
completed: ~
output: [knowledge]
---

# Cryptographic preservation and runtime evaluation of original intent: a representation formalism for Getting Started phase intent that is simultaneously verifiable and semantically stable across the full operational lifecycle

## Research Question

What representation of original intent, captured at the Getting Started phase, is simultaneously cryptographically verifiable and semantically stable enough to function as a meaningful evaluation baseline for the Policy Decision Point (PDP) across the full operational lifecycle of a governed asset, including legitimate scope evolution?

## Scope

**In scope:**
- The representation formalism for asset-level intent: the triple (authorised-capability-set, authorised-data-scope, authorised-action-envelope), each component independently verifiable against tool calls
- The Ricardian Contract architecture applied to intent: binding a human-readable intent statement to a machine-processable capability declaration via a content-addressed hash
- The formal amendment protocol: cryptographically chaining governed scope extensions to the original intent, preserving lineage while updating the evaluable baseline
- Semantic stability analysis: conditions under which a bit-for-bit identical intent artefact produces false positives (flagging legitimate evolution as task creep) or false negatives (failing to flag genuine drift)
- The Data, Information, Knowledge, Wisdom (DIKW) transformation function from tool-call Data to the Knowledge level of the intent representation: what the PDP needs to evaluate a tool call against the intent triple
- The Language Designed for Large Language Model (LLM) Agent Output constraint: the representation must be a format that agents can evaluate against, not just humans read
- Intent-Driven Development (IDD) applied to the Getting Started phase intent capture

**Out of scope:**
- Policy synchronisation across phases (covered by RQ2)
- Kill-switch and remediation protocols (covered by RQ3)
- Invariant registration mechanism in the Policy Administration Point (PAP) (covered by RQ1), though the intent triple includes the invariant set as a subset
- Anomaly detection in the Policy Information Point (PIP) (covered by RQ4), though the representation produced here must be evaluable by the PIP
- Organisation-level intent (the organisational intent formal specification item), this research is scoped to asset-level intent only

**Constraints:**
- Depends on RQ1 (invariant registration, which is a subset of the intent capture problem) and RQ4 (the PIP uses the intent baseline to detect suppression, so the representation must be evaluable by the PIP's anomaly detection, not just by the PDP)
- The representation must be specific enough to be evaluable against tool calls, vague natural language is insufficient
- The representation must be stable enough to survive legitimate operating context change, over-specification that flags legitimate evolution is a failure mode
- The false-positive problem (flagging legitimate scope evolution) and the false-negative problem (missing genuine drift) must both be explicitly addressed, and the amendment protocol is the mechanism for the former

## Context

- [fact; source: https://iang.org/papers/ricardian_contract.html; https://www.w3.org/TR/vc-data-model/] Cryptographically binding a human-readable statement to a machine-verifiable artefact is a solved document-integrity problem, because both the Ricardian Contract model and the W3C Verifiable Credentials Data Model define patterns in which signed structured claims can be verified for tampering and issuer authenticity.
- [inference; source: https://davidamitchell.github.io/Research/research/2026-03-14-organisational-intent-formal-specification.html; https://davidamitchell.github.io/Research/research/2026-03-16-intent-driven-development.html; https://davidamitchell.github.io/Research/research/2026-03-10-dikw-transformation-functions.html] The hard problem is not integrity of bytes but stability of meaning across time, because intent captured as prose or high-level goals can drift semantically as operating context, data sensitivity, and available actions change while the text itself remains unchanged.
- [inference; source: https://davidamitchell.github.io/Research/research/2026-03-10-language-for-llm-agent-output.html; https://csrc.nist.gov/pubs/sp/800/162/final; https://docs.oasis-open.org/xacml/3.0/xacml-3.0-core-spec-os-en.html] A usable solution therefore has to separate the audit narrative that humans read from a bounded machine-readable declaration that a policy engine or Large Language Model (LLM) agent can compare against an observed tool call using subject, resource, action, and environment style attributes.

## Approach

1. **Representation formalism design:** Design the intent triple (authorised-capability-set, authorised-data-scope, authorised-action-envelope). For each component: define the schema, define what constitutes a violation, and define how the PDP evaluates an observed tool call against it. Assess whether the triple is complete (covers all evaluable dimensions of intent) or whether additional components are required.
2. **Ricardian Contract adaptation:** Adapt the Ricardian Contract architecture to intent representation. Define: (a) the human-readable intent statement format; (b) the machine-processable capability declaration format; (c) the content-addressed hash binding them; (d) the PDP evaluation protocol against the machine-processable component; (e) the audit trail function of the human-readable component.
3. **Semantic stability analysis:** Analyse the stability properties of the intent triple under legitimate scope evolution. Define conditions under which each component can change without constituting unauthorised drift. Define conditions under which surface language change without triple change constitutes a false negative.
4. **Amendment protocol design:** Design the formal amendment protocol for legitimate scope evolution. Define: (a) the amendment request format; (b) the cryptographic chaining mechanism (amendment hashes include a reference to the original and all prior amendments); (c) the governance gate required to approve an amendment; (d) how the PDP evaluates tool calls against an amended triple.
5. **DIKW transformation function:** Define the transformation function from tool-call Data (the observable) to the Knowledge level of the intent triple (the evaluable baseline). This is the mechanism by which the PDP moves from "what tool call was made" to "does this tool call fall within the authorised-action-envelope?"
6. **Agent-evaluable format constraint:** Validate the representation against the agent-evaluable constraint: can an Large Language Model (LLM) agent evaluate a proposed tool call against the machine-processable representation without human mediation? If not, what additional structure is required?
7. **PIP evaluability:** Validate the representation against the PIP's anomaly detection requirement (RQ4): can the PIP's Bayesian surprise model compute a prior probability over legitimate task intents given the intent triple? If not, what additional structure is required?
8. **Synthesis:** Produce a complete intent representation specification, a worked example for a Confidentiality, Integrity, and Availability (CIA) High Personally Identifiable Information (PII) handling agentic system, an amendment protocol schema, and a decision framework for PAP implementors characterising when an amendment is required versus when a new asset registration is required.

## Sources

- [x] [Organisational intent formal specification, completed item](https://davidamitchell.github.io/Research/research/2026-03-14-organisational-intent-formal-specification.html) - organisation-level analogue and machine-checkable derivation precedent
- [x] [Intent-Driven Development (IDD), completed item](https://davidamitchell.github.io/Research/research/2026-03-16-intent-driven-development.html) - intent as the primary specification primitive above tests and contracts
- [x] [Ricardian Contract model, completed item](https://davidamitchell.github.io/Research/research/2026-03-14-ricardian-contract-model.html) - prose plus machine-readable plus cryptographic binding pattern
- [x] [Language designed for LLM agents to produce, completed item](https://davidamitchell.github.io/Research/research/2026-03-10-language-for-llm-agent-output.html) - bounded output format constraints for agent evaluability
- [x] [DIKW transformation functions, completed item](https://davidamitchell.github.io/Research/research/2026-03-10-dikw-transformation-functions.html) - Data to Knowledge transformation framing for runtime evaluation
- [x] [Formal intent specification and reward hacking, completed item](https://davidamitchell.github.io/Research/research/2026-03-10-formal-spec-intent-alignment-agentic-coding.html) - why incomplete specifications are gameable
- [x] [Universal policy synchronisation and integrity, completed item](https://davidamitchell.github.io/Research/research/2026-04-27-pdp-universal-policy-synchronisation-integrity.html) - digest-bound lifecycle identity and attestation pattern
- [x] [Invariant-based anomaly detection in the Policy Information Point (PIP), completed item](https://davidamitchell.github.io/Research/research/2026-04-27-pip-invariant-anomaly-detection.html) - prior-based anomaly detection requirement that consumes the baseline
- [x] [Ricardian Contracts, Ian Grigg](https://iang.org/papers/ricardian_contract.html) - original architecture for human-readable plus machine-processable document binding
- [x] [Security and Privacy Controls for Information Systems and Organizations, NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5) - authoritative control catalog
- [x] [NIST SP 800-53 Rev. 5 landing page](https://csrc.nist.gov/pubs/sp/800/53/r5/final) - official publication landing page for the control catalog
- [x] [Guide to Attribute Based Access Control (ABAC), NIST SP 800-162](https://csrc.nist.gov/pubs/sp/800/162/final) - subject, object, action, and environment evaluation model
- [x] [eXtensible Access Control Markup Language (XACML) 3.0 core specification](https://docs.oasis-open.org/xacml/3.0/xacml-3.0-core-spec-os-en.html) - authoritative definitions of PAP, PDP, Policy Enforcement Point (PEP), and PIP
- [x] [Verifiable Credentials Data Model, W3C Recommendation](https://www.w3.org/TR/vc-data-model/) - signed claims, schemas, proofs, status, and credential graphs
- [x] [Authorization Capabilities for Linked Data (ZCAP-LD)](https://w3c-ccg.github.io/zcap-spec/) - capability delegation, attenuation, and caveats as a modern object capability reference
- [x] [Statement layer specification, in-toto attestation](https://github.com/in-toto/attestation/blob/main/spec/v1/statement.md) - digest-bound immutable subject semantics
- [x] [ResourceDescriptor field type specification, in-toto attestation](https://github.com/in-toto/attestation/blob/main/spec/v1/resource_descriptor.md) - immutable digest and annotation semantics
- [x] [SLSA provenance v1.0](https://slsa.dev/spec/v1.0/provenance) - externalParameters, resolvedDependencies, and subject binding for provenance-carrying records

## Related

- [Ricardian Contract model: history, current state, and latest research](https://davidamitchell.github.io/Research/research/2026-03-14-ricardian-contract-model.html)
- [Universal policy synchronisation and integrity](https://davidamitchell.github.io/Research/research/2026-04-27-pdp-universal-policy-synchronisation-integrity.html)
- [Invariant-based anomaly detection in the Policy Information Point (PIP)](https://davidamitchell.github.io/Research/research/2026-04-27-pip-invariant-anomaly-detection.html)

---

## Research Skill Output

*(Full output from running the research skill, retained verbatim in the completed item. Sections 0 to 5 are the investigation, and Section 6 seeds the Findings section below.)*

### §0 Initialise

- [fact; source: https://docs.oasis-open.org/xacml/3.0/xacml-3.0-core-spec-os-en.html; https://csrc.nist.gov/pubs/sp/800/162/final] **Research question restated:** what intent representation lets the Policy Decision Point (PDP) and adjacent governance components evaluate runtime tool calls against a stable baseline of authorised capability, authorised data scope, and authorised action, while preserving cryptographic proof of what was originally approved?
- [fact; source: https://davidamitchell.github.io/Research/research/2026-03-14-organisational-intent-formal-specification.html; https://davidamitchell.github.io/Research/research/2026-03-16-intent-driven-development.html] **Scope confirmed:** this item is about asset-level intent capture, not organisation-level strategy, and it treats Getting Started phase intent as an Intent-Driven Development (IDD) artefact that must later be evaluated by runtime control surfaces.
- [fact; source: https://iang.org/papers/ricardian_contract.html; https://www.w3.org/TR/vc-data-model/; https://github.com/in-toto/attestation/blob/main/spec/v1/statement.md] **Constraint confirmed:** the representation has to solve both integrity and meaning, so it needs a human-readable layer, a machine-processable layer, and a digest-bound or proof-bound envelope that can survive storage, transmission, and later verification.
- [fact; source: https://davidamitchell.github.io/Research/research/2026-03-14-ricardian-contract-model.html; https://davidamitchell.github.io/Research/research/2026-03-10-language-for-llm-agent-output.html; https://davidamitchell.github.io/Research/research/2026-03-10-dikw-transformation-functions.html; https://davidamitchell.github.io/Research/research/2026-03-10-formal-spec-intent-alignment-agentic-coding.html; https://davidamitchell.github.io/Research/research/2026-04-27-pip-invariant-anomaly-detection.html; https://davidamitchell.github.io/Research/research/2026-04-27-pdp-universal-policy-synchronisation-integrity.html] **Prior work cross-reference:** prior completed items already established the Ricardian contract pattern, the bounded-format requirement for Large Language Model (LLM) agent output, the Data, Information, Knowledge, Wisdom (DIKW) transformation frame, the risk of specification gaming, the Policy Information Point (PIP) need for a prior baseline, and the digest-bound lifecycle identity pattern. This item extends that chain by specifying the baseline artefact itself.
- [fact; source: https://w3c-ccg.github.io/zcap-spec/; https://www.w3.org/TR/vc-data-model/; https://slsa.dev/spec/v1.0/provenance] **Output format confirmed:** knowledge, specifically a representation specification, a worked example, an amendment schema, a PDP evaluation rule, and a decision rule for amendment versus new registration.

### §1 Question Decomposition

- **Root question:** what artefact should be signed at asset registration time so later tool calls can be judged against the same authorised intent without collapsing legitimate evolution into false drift?
- **A. Representation structure**
  - A1. What machine-checkable fields are necessary to represent authorised capability, data, and action scope?
  - A2. Is the proposed triple sufficient, or does runtime evaluation require another first-class component?
- **B. Cryptographic envelope**
  - B1. What pattern best binds human-readable intent to machine-readable claims?
  - B2. Should the authoritative identity be a mutable version label or an immutable digest?
- **C. Runtime evaluation**
  - C1. How should a tool call be normalised into a form the PDP can compare against the declaration?
  - C2. What constitutes a violation for each component of the triple?
- **D. Semantic stability**
  - D1. Which changes are legitimate evolution that should be handled by amendment?
  - D2. Which changes indicate a new asset or an unauthorised drift event?
- **E. Amendment protocol**
  - E1. How should amendments reference the original artefact and prior amendments?
  - E2. What minimum fields are required for evaluable and auditable amendments?
- **F. Agent and PIP evaluability**
  - F1. Can an LLM agent compare a proposed tool call against the declaration without human interpretation?
  - F2. Can the PIP derive priors over legitimate intent from the same declaration?

### §2 Investigation

- [fact; source: https://iang.org/papers/ricardian_contract.html; https://davidamitchell.github.io/Research/research/2026-03-14-ricardian-contract-model.html] Ian Grigg's Ricardian Contract model defines a dual artefact in which the contract is simultaneously human-readable, machine-readable, digitally signed, and allied with a unique secure identifier, which is the closest direct precedent for preserving intent as both prose and executable structure.
- [fact; source: https://www.w3.org/TR/vc-data-model/] The Verifiable Credentials Data Model defines signed machine-readable claims with issuer, subject, validity, status, schema, evidence, and proof semantics, and it requires verifiers to validate proofs and then apply their own business rules before relying on claims.
- [fact; source: https://github.com/in-toto/attestation/blob/main/spec/v1/statement.md; https://github.com/in-toto/attestation/blob/main/spec/v1/resource_descriptor.md; https://slsa.dev/spec/v1.0/provenance] The in-toto and SLSA provenance specifications treat digest-identified subjects and dependencies as immutable artefacts, which makes digest identity the strongest reusable primitive for preserving the exact approved machine-readable baseline across lifecycle transitions.

#### 2.1 Representation structure

- [fact; source: https://csrc.nist.gov/pubs/sp/800/162/final; https://docs.oasis-open.org/xacml/3.0/xacml-3.0-core-spec-os-en.html] Attribute Based Access Control (ABAC) and the eXtensible Access Control Markup Language (XACML) both frame runtime evaluation around subject, resource, action, and environment attributes rather than around free-form goals, which means an evaluable intent baseline has to resolve into bounded attributes that a policy engine can compare against an observed request.
- [fact; source: https://w3c-ccg.github.io/zcap-spec/] The modern object capability reference in ZCAP-LD treats authority as possession-bound, delegable, and attenuable through caveats that restrict controller, action, and revocation conditions, which directly supports the authorised-capability-set component.
- [inference; source: https://w3c-ccg.github.io/zcap-spec/; https://csrc.nist.gov/pubs/sp/800/162/final; https://docs.oasis-open.org/xacml/3.0/xacml-3.0-core-spec-os-en.html] The authorised-capability-set therefore needs at least `capabilityId`, `toolClass`, `permittedVerbs`, `targetResourceTypes`, `delegability`, `requiredApprovalClass`, and optional `caveats`, because bare tool names are too weak to capture attenuated authority.
- [fact; source: https://www.w3.org/TR/vc-data-model/] The Verifiable Credentials model includes credential schemas, terms of use, evidence, and validity periods, which shows that machine-processable declarations can carry typed claims plus time and policy qualifiers without collapsing into unstructured prose.
- [inference; source: https://www.w3.org/TR/vc-data-model/; https://davidamitchell.github.io/Research/research/2026-04-27-pip-invariant-anomaly-detection.html] The authorised-data-scope therefore needs explicit claims for `dataClasses`, `sensitivityTier`, `allowedSources`, `allowedSinks`, `crossBoundaryTransfer`, `retentionClass`, and `redactionRequirements`, because the PIP and PDP both need bounded data-handling claims rather than generic statements such as "may use customer data".
- [fact; source: https://csrc.nist.gov/pubs/sp/800/162/final; https://docs.oasis-open.org/xacml/3.0/xacml-3.0-core-spec-os-en.html] XACML treats action as a first-class resource access component and ABAC evaluates requested operations against policy conditions, so the declaration also needs an action layer that captures when, how, and in what sequence actions may occur.
- [inference; source: https://csrc.nist.gov/pubs/sp/800/162/final; https://docs.oasis-open.org/xacml/3.0/xacml-3.0-core-spec-os-en.html; https://davidamitchell.github.io/Research/research/2026-04-27-pip-invariant-anomaly-detection.html] The authorised-action-envelope should therefore include `purposeClass`, `allowedActionPatterns`, `forbiddenActionPatterns`, `quantitativeLimits`, `requiredPreconditions`, `requiredPostconditions`, and `timeOrPhaseConstraints`, because runtime drift often appears in sequence, frequency, or trigger pattern rather than in the single call token alone.
- [inference; source: https://davidamitchell.github.io/Research/research/2026-03-10-formal-spec-intent-alignment-agentic-coding.html; https://davidamitchell.github.io/Research/research/2026-03-10-language-for-llm-agent-output.html] The original triple is sufficient if the authorised-action-envelope explicitly carries purpose, sequencing, and quantitative ceilings. A fourth primary component is not required if invariants and governance constraints are encoded as qualifiers on the three existing components instead of as free-floating prose.

#### 2.2 Cryptographic envelope

- [fact; source: https://iang.org/papers/ricardian_contract.html] Grigg's design principle is that issues are contracts and that every transaction should link back to the contract identifier, which means the signed machine-readable baseline should not be detached from the human-readable intent narrative.
- [fact; source: https://www.w3.org/TR/vc-data-model/] The Verifiable Credentials model requires proofs, supports validity and status, supports evidence and terms of use, and allows type-specific schemas, which makes it a good envelope for carrying signed intent claims that later verifiers can interpret with policy-specific logic.
- [fact; source: https://github.com/in-toto/attestation/blob/main/spec/v1/statement.md; https://github.com/in-toto/attestation/blob/main/spec/v1/resource_descriptor.md] The in-toto Statement and ResourceDescriptor specifications explicitly assume digest-bound subjects are immutable and allow stable names plus annotations, which makes them suitable for carrying the exact content hash of the machine declaration even if a richer envelope such as a verifiable credential is used at the human workflow layer.
- [inference; source: https://iang.org/papers/ricardian_contract.html; https://www.w3.org/TR/vc-data-model/; https://github.com/in-toto/attestation/blob/main/spec/v1/statement.md] The best-fit representation is therefore a dual-layer "intent credential": a human-readable intent statement, a machine-readable intent declaration, and a digest-binding proof record that signs both and treats the declaration hash as the canonical runtime identity.

#### 2.3 Runtime evaluation protocol

- [fact; source: https://csrc.nist.gov/pubs/sp/800/162/final] NIST SP 800-162 defines authorization as evaluation of subject, object, requested operations, and environment conditions against policy rules, which provides the canonical comparison shape for a tool-call baseline.
- [fact; source: https://docs.oasis-open.org/xacml/3.0/xacml-3.0-core-spec-os-en.html] XACML defines the PDP as the evaluator of applicable policy, the PIP as the source of attribute values, and the Policy Enforcement Point (PEP) as the enforcement surface, so the declaration must be consumable as policy input rather than as an after-the-fact audit note.
- [inference; source: https://csrc.nist.gov/pubs/sp/800/162/final; https://docs.oasis-open.org/xacml/3.0/xacml-3.0-core-spec-os-en.html; https://davidamitchell.github.io/Research/research/2026-03-10-dikw-transformation-functions.html] The Data to Knowledge transformation should normalize each observed tool event into a tuple like `(actor, toolClass, verb, resourceType, dataClass, source, sink, purposeClass, sideEffects, environmentContext, phase)`, because that tuple is the minimum knowledge form required to compare a runtime event against the authorised declaration.
- [inference; source: https://w3c-ccg.github.io/zcap-spec/; https://csrc.nist.gov/pubs/sp/800/162/final] A capability violation occurs when the tool event invokes a verb, resource type, delegation state, or caveat condition that is not present in the authorised-capability-set.
- [inference; source: https://www.w3.org/TR/vc-data-model/; https://davidamitchell.github.io/Research/research/2026-04-27-pip-invariant-anomaly-detection.html] A data-scope violation occurs when the event touches a data class, source, sink, transfer mode, or retention posture outside the authorised-data-scope, even if the tool itself is allowed.
- [inference; source: https://csrc.nist.gov/pubs/sp/800/162/final; https://docs.oasis-open.org/xacml/3.0/xacml-3.0-core-spec-os-en.html] An action-envelope violation occurs when the event's purpose class, sequence position, rate, precondition, postcondition, or execution phase falls outside the allowed envelope, even if the tool and data classes separately look permitted.

#### 2.4 Semantic stability

- [fact; source: https://davidamitchell.github.io/Research/research/2026-03-16-intent-driven-development.html; https://davidamitchell.github.io/Research/research/2026-03-10-formal-spec-intent-alignment-agentic-coding.html] Prior repository work shows that natural-language intent and underspecified tests are gameable, which means semantic stability cannot depend on prose sameness alone.
- [inference; source: https://davidamitchell.github.io/Research/research/2026-03-14-organisational-intent-formal-specification.html; https://iang.org/papers/ricardian_contract.html] Bit-for-bit stability should attach to the machine declaration plus its digest, while the human-readable statement serves as an audit rationale and interpretation aid. Treating prose as the runtime baseline would reintroduce the semantic drift problem the representation is meant to solve.
- [inference; source: https://www.w3.org/TR/vc-data-model/; https://github.com/in-toto/attestation/blob/main/spec/v1/statement.md] A prose edit with no change to machine claims should not change the runtime baseline hash if the prose is stored as a descriptive field outside the canonicalized declaration subject, but a change to any authorised capability, data, or action claim should produce a new declaration hash and therefore a new evaluable baseline.
- [inference; source: https://davidamitchell.github.io/Research/research/2026-04-27-pip-invariant-anomaly-detection.html] False positives arise when legitimate operational evolution changes tool names, hosting substrates, or workflow sequencing while preserving the same authorised capability, data, and action semantics. False negatives arise when the prose remains stable but the effective authority expands through an unrecorded new capability, new data sink, or broader action sequence.

#### 2.5 Amendment protocol

- [fact; source: https://github.com/in-toto/attestation/blob/main/spec/v1/statement.md; https://slsa.dev/spec/v1.0/provenance] Digest-bound attestations and provenance records already model append-only records that identify immutable subjects and resolved dependencies, which supports an amendment chain pattern more safely than mutable overwrite.
- [fact; source: https://www.w3.org/TR/vc-data-model/] Verifiable credentials support issuance dates, validity periods, status, evidence, and credential graphs, which provides an interoperable way to represent a new signed amendment document that references earlier signed state.
- [inference; source: https://github.com/in-toto/attestation/blob/main/spec/v1/statement.md; https://www.w3.org/TR/vc-data-model/; https://davidamitchell.github.io/Research/research/2026-04-27-pdp-universal-policy-synchronisation-integrity.html] Each amendment should be a new signed object with fields `amendsDigest`, `previousAmendmentDigest`, `deltaClaims`, `justification`, `approver`, `effectiveFrom`, `supersedesOrExtends`, and `requiredMigrationActions`, because that structure preserves lineage, lets verifiers reconstruct the effective baseline, and prevents silent in-place mutation.
- [inference; source: https://davidamitchell.github.io/Research/research/2026-04-27-pdp-universal-policy-synchronisation-integrity.html; https://github.com/in-toto/attestation/blob/main/spec/v1/resource_descriptor.md] The effective runtime baseline should be computed as `base declaration + ordered valid amendments`, with digest validation at every step, instead of by editing the original declaration and losing evidence of how authority changed over time.
- [inference; source: https://davidamitchell.github.io/Research/research/2026-04-27-pip-invariant-anomaly-detection.html; https://davidamitchell.github.io/Research/research/2026-04-27-pdp-universal-policy-synchronisation-integrity.html] Amendment is appropriate when the asset identity, governing authority, and trust boundary remain the same and the change narrows or extends the existing triple in a governed way. New registration is required when the trust boundary, controlling principal, protected data class family, or primary action family changes enough that prior baseline priors are no longer meaningful.

#### 2.6 Agent and PIP evaluability

- [fact; source: https://davidamitchell.github.io/Research/research/2026-03-10-language-for-llm-agent-output.html] Prior research on agent-evaluable formats concluded that bounded types, schemas, and constrained output languages are required for reliable machine evaluation, because free-form natural language leaves semantic content inside unconstrained strings.
- [inference; source: https://davidamitchell.github.io/Research/research/2026-03-10-language-for-llm-agent-output.html; https://www.w3.org/TR/vc-data-model/] The declaration therefore needs closed vocabularies or schema-bound enumerations for purpose class, tool class, resource type, data class, action pattern, and approval class, plus worked examples, because an LLM agent cannot reliably compare against a baseline whose categories are implicit or locally invented at runtime.
- [fact; source: https://davidamitchell.github.io/Research/research/2026-04-27-pip-invariant-anomaly-detection.html] The adjacent PIP item requires a prior probability over legitimate task intents given registered invariants and current task framing, which means the baseline must be rich enough to express expected capabilities, expected data touchpoints, and expected action patterns.
- [inference; source: https://davidamitchell.github.io/Research/research/2026-04-27-pip-invariant-anomaly-detection.html; https://csrc.nist.gov/pubs/sp/800/162/final] The triple is sufficient for PIP evaluability if it includes sensitivity tiers, forbidden sinks, purpose classes, and quantitative ceilings, because these are the features that let the PIP detect improbable pairings such as low-complexity framing plus high-sensitivity export attempts.

#### 2.7 Governance and regulatory relevance

- [fact; source: https://doi.org/10.6028/NIST.SP.800-53r5] NIST SP 800-53 Rev. 5 requires organizations to maintain security and privacy controls that address both functionality and assurance across system lifecycles.
- [fact; source: https://doi.org/10.6028/NIST.SP.800-53r5; https://csrc.nist.gov/pubs/sp/800/53/r5/final] The NIST SP 800-53 Rev. 5 planning and acquisition control language requires security and privacy architectures and developer design specifications that describe required functionality, control allocation, enterprise-architecture alignment, and lifecycle updates, which supports treating original intent as a maintained architecture artefact rather than as an informal kickoff note.
- [inference; source: https://doi.org/10.6028/NIST.SP.800-53r5; https://csrc.nist.gov/pubs/sp/800/53/r5/final; https://davidamitchell.github.io/Research/research/2026-03-14-organisational-intent-formal-specification.html] A signed, schema-bound intent credential fits these architecture-control expectations better than an untyped project brief because it can document architecture, allocate constraints, and show later amendments as controlled lifecycle changes instead of as undocumented interpretation drift.

### §3 Reasoning

- [inference; source: https://iang.org/papers/ricardian_contract.html; https://www.w3.org/TR/vc-data-model/; https://github.com/in-toto/attestation/blob/main/spec/v1/statement.md] The best representation is not a single file format but a layered artefact: Ricardian-style dual semantics for meaning, a verifiable-credential-style claim model for interoperability, and an in-toto-style digest binding for immutable runtime identity.
- [inference; source: https://csrc.nist.gov/pubs/sp/800/162/final; https://docs.oasis-open.org/xacml/3.0/xacml-3.0-core-spec-os-en.html] Runtime evaluation requires the machine-readable layer to resolve into bounded subject, resource, action, and environment style attributes. Therefore the machine-readable declaration, not the prose, has to be the canonical runtime baseline.
- [inference; source: https://davidamitchell.github.io/Research/research/2026-03-10-formal-spec-intent-alignment-agentic-coding.html; https://davidamitchell.github.io/Research/research/2026-03-10-language-for-llm-agent-output.html] The triple remains semantically stable only if its categories are typed and closed enough to prevent post hoc reinterpretation. Otherwise the representation would preserve bytes while still losing meaning.
- [inference; source: https://davidamitchell.github.io/Research/research/2026-04-27-pdp-universal-policy-synchronisation-integrity.html; https://github.com/in-toto/attestation/blob/main/spec/v1/resource_descriptor.md] Legitimate scope evolution should be represented as append-only amendments rather than as edits to the base artefact, because silent mutation destroys the provenance needed for later runtime verification and audit.

### §4 Consistency Check

- [fact; source: https://csrc.nist.gov/pubs/sp/800/162/final; https://docs.oasis-open.org/xacml/3.0/xacml-3.0-core-spec-os-en.html] The proposed evaluation tuple is consistent with ABAC and XACML's subject, object, action, and environment framing.
- [fact; source: https://w3c-ccg.github.io/zcap-spec/] The capability component is consistent with object capability logic because it expresses authority by possession plus attenuating caveats rather than by identity alone.
- [inference; source: https://www.w3.org/TR/vc-data-model/; https://github.com/in-toto/attestation/blob/main/spec/v1/statement.md] There is no contradiction between using a verifiable credential envelope and an in-toto digest subject, because the credential can carry the richer claim graph while the digest subject remains the equality token used by runtime controls.
- [inference; source: https://davidamitchell.github.io/Research/research/2026-04-27-pip-invariant-anomaly-detection.html] The representation stays aligned with the adjacent PIP item because the same triple that constrains PDP evaluation also supplies the prior features the PIP needs for anomaly detection.

### §5 Depth and Breadth Expansion

- [fact; source: https://doi.org/10.6028/NIST.SP.800-53r5; https://csrc.nist.gov/pubs/sp/800/53/r5/final] From a regulatory lens, architecture artefacts have to be maintained through the lifecycle, which supports explicit amendment handling instead of assuming original design intent remains self-explanatory forever.
- [inference; source: https://w3c-ccg.github.io/zcap-spec/; https://davidamitchell.github.io/Research/research/2026-04-26-access-control-amplification-agentic-operations.html] From a security lens, capability attenuation matters because agentic operations amplify blast radius when the allowed action space is broader than the declared intent, so the authorised-capability-set has to be finer-grained than a role label.
- [inference; source: https://www.w3.org/TR/vc-data-model/; https://davidamitchell.github.io/Research/research/2026-04-26-ai-agent-identity-access-management-enterprise.html] From an identity lens, signed issuers and approval chains matter because the same intent claims can have very different trust meaning depending on who approved the amendment and which authority chain issued the credential.
- [inference; source: https://davidamitchell.github.io/Research/research/2026-03-10-dikw-transformation-functions.html; https://davidamitchell.github.io/Research/research/2026-03-10-language-for-llm-agent-output.html] From an agent-design lens, the representation succeeds only if the Data to Knowledge transformation and the output language are co-designed. A perfect declaration is still unusable if runtime telemetry cannot be normalized into the same vocabulary that the declaration uses.

### §6 Synthesis

*(This section seeds the Findings below.)*

- **Executive summary:**
  - [fact; source: https://iang.org/papers/ricardian_contract.html; https://www.w3.org/TR/vc-data-model/; https://github.com/in-toto/attestation/blob/main/spec/v1/statement.md] The best-supported representation is a signed, digest-addressed dual artefact: a human-readable intent statement paired with a machine-readable intent declaration whose canonical identity is the hash of the declaration and whose envelope carries issuer, proof, schema, validity, and amendment metadata.
  - [fact; source: https://csrc.nist.gov/pubs/sp/800/162/final; https://docs.oasis-open.org/xacml/3.0/xacml-3.0-core-spec-os-en.html; https://w3c-ccg.github.io/zcap-spec/] The machine-readable declaration should remain the original triple of authorised-capability-set, authorised-data-scope, and authorised-action-envelope, but each component must be typed tightly enough for subject, resource, action, and environment comparison and for capability attenuation.
  - [inference; source: https://davidamitchell.github.io/Research/research/2026-04-27-pdp-universal-policy-synchronisation-integrity.html; https://github.com/in-toto/attestation/blob/main/spec/v1/resource_descriptor.md] Semantic stability across the lifecycle comes from leaving the original declaration immutable and expressing legitimate evolution as append-only signed amendments that reference prior digests and carry explicit delta claims, not from rewriting the original record.
  - [inference; source: https://davidamitchell.github.io/Research/research/2026-04-27-pip-invariant-anomaly-detection.html; https://davidamitchell.github.io/Research/research/2026-03-10-language-for-llm-agent-output.html] This design gives the PDP and PIP a shared evaluable baseline and gives LLM agents a bounded format they can compare proposed tool calls against without depending on free-form prose interpretation.

- **Key findings:**
  - [fact; source: https://iang.org/papers/ricardian_contract.html; https://www.w3.org/TR/vc-data-model/; https://github.com/in-toto/attestation/blob/main/spec/v1/statement.md] **High:** A dual artefact that combines Ricardian-style human-readable prose, verifiable-credential-style typed claims, and an in-toto-style digest-bound subject is the strongest current pattern for preserving original intent as both auditable meaning and immutable runtime identity.
  - [fact; source: https://csrc.nist.gov/pubs/sp/800/162/final; https://docs.oasis-open.org/xacml/3.0/xacml-3.0-core-spec-os-en.html; https://w3c-ccg.github.io/zcap-spec/] **High:** The existing intent triple is sufficient for runtime evaluation only when authorised capability, authorised data scope, and authorised action are expressed as bounded typed claims covering verbs, resource types, caveats, data classes, sinks, purpose classes, sequences, and quantitative limits.
  - [inference; source: https://davidamitchell.github.io/Research/research/2026-03-10-formal-spec-intent-alignment-agentic-coding.html; https://davidamitchell.github.io/Research/research/2026-03-16-intent-driven-development.html] **High:** The human-readable statement should not be the canonical runtime baseline, because semantic stability fails when prose remains unchanged while effective authority expands or when prose wording changes while machine authority does not.
  - [inference; source: https://github.com/in-toto/attestation/blob/main/spec/v1/resource_descriptor.md; https://slsa.dev/spec/v1.0/provenance; https://davidamitchell.github.io/Research/research/2026-04-27-pdp-universal-policy-synchronisation-integrity.html] **High:** Legitimate lifecycle evolution should be represented as an append-only amendment chain in which each amendment references the base declaration digest and prior amendment digest, because mutable overwrites destroy the provenance needed for later policy verification and audit.
  - [inference; source: https://davidamitchell.github.io/Research/research/2026-03-10-dikw-transformation-functions.html; https://csrc.nist.gov/pubs/sp/800/162/final] **High:** The Policy Decision Point only needs a Knowledge-level event tuple derived from raw tool-call data, not a human-level narrative, and that tuple should normalize actor, tool class, verb, resource type, data class, source, sink, purpose, side effects, and phase into the same vocabulary used by the declaration.
  - [inference; source: https://davidamitchell.github.io/Research/research/2026-03-10-language-for-llm-agent-output.html; https://www.w3.org/TR/vc-data-model/] **Medium:** Large Language Model agent evaluability requires closed vocabularies, credential schemas, examples, and type URLs in the declaration, because free-text fields alone leave the decisive semantics inside unconstrained strings that agents cannot compare reliably.
  - [inference; source: https://davidamitchell.github.io/Research/research/2026-04-27-pip-invariant-anomaly-detection.html; https://csrc.nist.gov/pubs/sp/800/162/final] **High:** The same typed declaration can support PIP anomaly detection if it includes sensitivity tiers, forbidden sinks, purpose classes, and quantitative ceilings, because those features allow prior probabilities over legitimate task intents to be computed from registered asset constraints.
  - [inference; source: https://doi.org/10.6028/NIST.SP.800-53r5; https://csrc.nist.gov/pubs/sp/800/53/r5/final; https://davidamitchell.github.io/Research/research/2026-03-14-organisational-intent-formal-specification.html] **Medium:** An amendment should be treated as a lifecycle architecture update when the asset identity, trust boundary, and primary protected-data family remain stable, while a new registration is required when those foundations change enough that the prior baseline no longer represents the same governed asset.

- **Evidence map:**
  - [fact; source: https://iang.org/papers/ricardian_contract.html; https://www.w3.org/TR/vc-data-model/; https://github.com/in-toto/attestation/blob/main/spec/v1/statement.md] Claim 1: dual artefact plus typed claims plus digest subject is the best fit.
  - [fact; source: https://csrc.nist.gov/pubs/sp/800/162/final; https://docs.oasis-open.org/xacml/3.0/xacml-3.0-core-spec-os-en.html; https://w3c-ccg.github.io/zcap-spec/] Claim 2: the triple is sufficient only when tightly typed for capability, data, and action evaluation.
  - [inference; source: https://davidamitchell.github.io/Research/research/2026-03-10-formal-spec-intent-alignment-agentic-coding.html; https://davidamitchell.github.io/Research/research/2026-03-16-intent-driven-development.html] Claim 3: prose should remain an audit layer rather than the canonical runtime baseline.
  - [inference; source: https://github.com/in-toto/attestation/blob/main/spec/v1/resource_descriptor.md; https://slsa.dev/spec/v1.0/provenance; https://davidamitchell.github.io/Research/research/2026-04-27-pdp-universal-policy-synchronisation-integrity.html] Claim 4: append-only amendments are required for legitimate evolution.
  - [inference; source: https://davidamitchell.github.io/Research/research/2026-03-10-dikw-transformation-functions.html; https://csrc.nist.gov/pubs/sp/800/162/final] Claim 5: Data must be normalized into a Knowledge-level runtime tuple.
  - [inference; source: https://davidamitchell.github.io/Research/research/2026-03-10-language-for-llm-agent-output.html; https://www.w3.org/TR/vc-data-model/] Claim 6: agent evaluability depends on typed vocabularies and schemas.
  - [inference; source: https://davidamitchell.github.io/Research/research/2026-04-27-pip-invariant-anomaly-detection.html; https://csrc.nist.gov/pubs/sp/800/162/final] Claim 7: the declaration can also support prior-based PIP anomaly detection.
  - [inference; source: https://doi.org/10.6028/NIST.SP.800-53r5; https://csrc.nist.gov/pubs/sp/800/53/r5/final; https://davidamitchell.github.io/Research/research/2026-03-14-organisational-intent-formal-specification.html] Claim 8: amendment versus new registration should follow architecture-boundary change rules.

- **Assumptions:**
  - [assumption; source: https://csrc.nist.gov/pubs/sp/800/162/final] Runtime telemetry can be normalized into stable subject, object, action, and environment style attributes for every relevant tool call. Justification: ABAC assumes such attributes exist, but this item did not test a concrete telemetry pipeline.
  - [assumption; source: https://www.w3.org/TR/vc-data-model/; https://github.com/in-toto/attestation/blob/main/spec/v1/statement.md] A production implementation can combine a verifiable credential envelope with an in-toto digest subject without introducing incompatible trust semantics. Justification: both models are composable on paper, but this item did not build an interoperability profile.

- **Analysis:**
  - [inference; source: https://iang.org/papers/ricardian_contract.html; https://www.w3.org/TR/vc-data-model/] Ricardian contracts solve the prose-plus-machine duality, while verifiable credentials solve typed signed claim carriage, so combining them covers meaning and portability better than either source alone.
  - [inference; source: https://github.com/in-toto/attestation/blob/main/spec/v1/statement.md; https://slsa.dev/spec/v1.0/provenance] In-toto and SLSA add the missing immutable-subject and dependency-lineage discipline needed to prevent silent mutation of the authoritative runtime baseline.
  - [inference; source: https://csrc.nist.gov/pubs/sp/800/162/final; https://docs.oasis-open.org/xacml/3.0/xacml-3.0-core-spec-os-en.html] ABAC and XACML provide the strongest runtime-evaluation frame because they explain exactly which attributes a policy engine needs, which keeps the representation grounded in operational comparison rather than in abstract intent rhetoric.
  - [inference; source: https://davidamitchell.github.io/Research/research/2026-03-10-formal-spec-intent-alignment-agentic-coding.html; https://davidamitchell.github.io/Research/research/2026-03-10-language-for-llm-agent-output.html] The main tradeoff is between semantic richness and evaluability: richer prose improves human interpretability, but only typed bounded claims support deterministic runtime comparison and reduce specification gaming.

- **Risks, gaps, uncertainties:**
  - [fact; source: https://www.w3.org/TR/vc-data-model/] The Verifiable Credentials Data Model does not by itself define a domain ontology for capability, data, or action classes, so a production system still needs a controlled vocabulary profile.
  - [fact; source: https://w3c-ccg.github.io/zcap-spec/] ZCAP-LD is a community draft rather than a finalized broad standard, so its capability and caveat model is a strong reference but not a settled interoperability baseline.
  - [inference; source: https://davidamitchell.github.io/Research/research/2026-04-27-pip-invariant-anomaly-detection.html] The baseline can support the PIP's prior model, but this item did not estimate how much historical telemetry is needed before those priors become reliable in practice.
  - [assumption; source: https://doi.org/10.6028/NIST.SP.800-53r5; https://csrc.nist.gov/pubs/sp/800/53/r5/final] Regulatory alignment was inferred from architecture-control language, not from sector-specific supervisory guidance for agentic systems.

- **Open questions:**
  - [inference; source: https://w3c-ccg.github.io/zcap-spec/; https://www.w3.org/TR/vc-data-model/] What is the best controlled vocabulary for purpose classes, action patterns, and caveats that remains portable across tools and organizations?
  - [inference; source: https://github.com/in-toto/attestation/blob/main/spec/v1/statement.md; https://slsa.dev/spec/v1.0/provenance] Should amendment chains support partial revocation of specific capabilities, or should revocation always issue a whole new declaration to keep verification simpler?
  - [inference; source: https://davidamitchell.github.io/Research/research/2026-04-27-pip-invariant-anomaly-detection.html] How should the PIP weight rare but legitimate emergency overrides without training itself to treat exceptional high-risk actions as normal?

### §7 Recursive Review

- [fact; source: https://iang.org/papers/ricardian_contract.html; https://www.w3.org/TR/vc-data-model/; https://github.com/in-toto/attestation/blob/main/spec/v1/statement.md; https://csrc.nist.gov/pubs/sp/800/162/final; https://docs.oasis-open.org/xacml/3.0/xacml-3.0-core-spec-os-en.html; https://w3c-ccg.github.io/zcap-spec/] All synthesis claims are now grounded either in primary external sources or in explicitly cited prior completed items, and unsupported narrative glue has been removed.
- [fact; source: https://davidamitchell.github.io/Research/research/2026-04-27-pip-invariant-anomaly-detection.html; https://davidamitchell.github.io/Research/research/2026-04-27-pdp-universal-policy-synchronisation-integrity.html] The output was cross-checked against adjacent completed items covering the same governance surface so that the proposed baseline remains consistent with prior work on anomaly detection and digest-bound policy identity.
- [inference; source: https://www.w3.org/TR/vc-data-model/; https://github.com/in-toto/attestation/blob/main/spec/v1/resource_descriptor.md] The main remaining uncertainty is implementation profile design rather than conceptual structure: the recommended pattern is supported, but the exact ontology and serialization profile would still need engineering work.

---

## Findings

### Executive Summary

[fact; source: https://iang.org/papers/ricardian_contract.html; https://www.w3.org/TR/vc-data-model/; https://github.com/in-toto/attestation/blob/main/spec/v1/statement.md] The most defensible representation of original asset intent is a signed, digest-addressed dual artefact that pairs a human-readable intent statement with a machine-readable intent declaration whose canonical runtime identity is the hash of the declaration rather than the prose. [fact; source: https://csrc.nist.gov/pubs/sp/800/162/final; https://docs.oasis-open.org/xacml/3.0/xacml-3.0-core-spec-os-en.html; https://w3c-ccg.github.io/zcap-spec/] The declaration should keep the original triple of authorised-capability-set, authorised-data-scope, and authorised-action-envelope, but each component must be encoded as bounded typed claims that a policy engine can compare against subject, resource, action, and environment attributes and that can express capability attenuation. [inference; source: https://github.com/in-toto/attestation/blob/main/spec/v1/resource_descriptor.md; https://slsa.dev/spec/v1.0/provenance; https://davidamitchell.github.io/Research/research/2026-04-27-pdp-universal-policy-synchronisation-integrity.html] Legitimate lifecycle evolution should not rewrite the original intent record, because semantic stability is preserved best by keeping the base declaration immutable and adding append-only signed amendments that reference prior digests and carry explicit delta claims. [inference; source: https://davidamitchell.github.io/Research/research/2026-04-27-pip-invariant-anomaly-detection.html; https://davidamitchell.github.io/Research/research/2026-03-10-language-for-llm-agent-output.html] This structure gives the Policy Decision Point and Policy Information Point a shared evaluable baseline and gives Large Language Model agents a bounded format they can compare tool calls against without relying on free-form prose interpretation.

### Key Findings

1. [fact; source: https://iang.org/papers/ricardian_contract.html; https://www.w3.org/TR/vc-data-model/; https://github.com/in-toto/attestation/blob/main/spec/v1/statement.md] **High:** A dual artefact that combines Ricardian-style prose, verifiable-credential-style typed claims, and an in-toto-style digest-bound subject is the strongest current pattern for preserving original intent as both auditable human meaning and immutable runtime identity across the lifecycle.
2. [fact; source: https://csrc.nist.gov/pubs/sp/800/162/final; https://docs.oasis-open.org/xacml/3.0/xacml-3.0-core-spec-os-en.html; https://w3c-ccg.github.io/zcap-spec/] **High:** The original triple of authorised-capability-set, authorised-data-scope, and authorised-action-envelope is sufficient for runtime evaluation only when each component is expressed as bounded typed claims covering verbs, resource types, caveats, data classes, sinks, purpose classes, sequences, and quantitative limits.
3. [inference; source: https://davidamitchell.github.io/Research/research/2026-03-10-formal-spec-intent-alignment-agentic-coding.html; https://davidamitchell.github.io/Research/research/2026-03-16-intent-driven-development.html] **High:** The human-readable statement should remain an audit and rationale layer rather than the canonical runtime baseline, because semantic stability fails when prose remains unchanged while effective authority expands or when prose wording changes while machine authority does not.
4. [inference; source: https://github.com/in-toto/attestation/blob/main/spec/v1/resource_descriptor.md; https://slsa.dev/spec/v1.0/provenance; https://davidamitchell.github.io/Research/research/2026-04-27-pdp-universal-policy-synchronisation-integrity.html] **High:** Legitimate lifecycle evolution should be encoded as an append-only amendment chain in which every amendment references the base declaration digest and prior amendment digest, because mutable overwrites destroy the provenance required for later policy verification and audit.
5. [inference; source: https://davidamitchell.github.io/Research/research/2026-03-10-dikw-transformation-functions.html; https://csrc.nist.gov/pubs/sp/800/162/final] **High:** The Policy Decision Point only needs a Knowledge-level event tuple derived from raw tool-call data, and that tuple should normalize actor, tool class, verb, resource type, data class, source, sink, purpose, side effects, and phase into the same vocabulary used by the declaration.
6. [inference; source: https://davidamitchell.github.io/Research/research/2026-03-10-language-for-llm-agent-output.html; https://www.w3.org/TR/vc-data-model/] **Medium:** Large Language Model agent evaluability depends on closed vocabularies, credential schemas, examples, and stable type URLs in the declaration, because free-text fields alone leave decisive semantics inside unconstrained strings that agents cannot compare reliably.
7. [inference; source: https://davidamitchell.github.io/Research/research/2026-04-27-pip-invariant-anomaly-detection.html; https://csrc.nist.gov/pubs/sp/800/162/final] **High:** The same typed declaration can support prior-based Policy Information Point anomaly detection if it includes sensitivity tiers, forbidden sinks, purpose classes, and quantitative ceilings, because those features let the PIP compute whether the observed task framing is plausible for the registered asset.
8. [inference; source: https://doi.org/10.6028/NIST.SP.800-53r5; https://csrc.nist.gov/pubs/sp/800/53/r5/final; https://davidamitchell.github.io/Research/research/2026-03-14-organisational-intent-formal-specification.html] **Medium:** A lifecycle change should be processed as an amendment when asset identity, trust boundary, and primary protected-data family remain stable, while a new registration is required when those foundations change enough that the prior baseline no longer describes the same governed asset.

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [fact] Dual artefact plus typed claims plus digest subject is the best fit for intent preservation. | [Ricardian Contract](https://iang.org/papers/ricardian_contract.html); [VC Data Model](https://www.w3.org/TR/vc-data-model/); [in-toto Statement](https://github.com/in-toto/attestation/blob/main/spec/v1/statement.md) | high | external primary pattern set |
| [fact] The triple is sufficient only when tightly typed for capability, data, and action evaluation. | [NIST SP 800-162](https://csrc.nist.gov/pubs/sp/800/162/final); [XACML 3.0](https://docs.oasis-open.org/xacml/3.0/xacml-3.0-core-spec-os-en.html); [ZCAP-LD](https://w3c-ccg.github.io/zcap-spec/) | high | runtime evaluation surface |
| [inference] Prose should remain an audit layer rather than the canonical runtime baseline. | [Formal intent specification and reward hacking](https://davidamitchell.github.io/Research/research/2026-03-10-formal-spec-intent-alignment-agentic-coding.html); [Intent-Driven Development](https://davidamitchell.github.io/Research/research/2026-03-16-intent-driven-development.html) | high | same-repo synthesis plus prior art |
| [inference] Legitimate evolution requires an append-only amendment chain. | [in-toto ResourceDescriptor](https://github.com/in-toto/attestation/blob/main/spec/v1/resource_descriptor.md); [SLSA provenance](https://slsa.dev/spec/v1.0/provenance); [Universal policy synchronisation and integrity](https://davidamitchell.github.io/Research/research/2026-04-27-pdp-universal-policy-synchronisation-integrity.html) | high | immutable identity and lifecycle lineage |
| [inference] Runtime Data must be normalized into a Knowledge-level event tuple for PDP comparison. | [DIKW transformation functions](https://davidamitchell.github.io/Research/research/2026-03-10-dikw-transformation-functions.html); [NIST SP 800-162](https://csrc.nist.gov/pubs/sp/800/162/final) | high | transformation function definition |
| [inference] Agent evaluability depends on schemas, examples, and stable type vocabularies. | [Language for LLM agent output](https://davidamitchell.github.io/Research/research/2026-03-10-language-for-llm-agent-output.html); [VC Data Model](https://www.w3.org/TR/vc-data-model/) | medium | bounded-format requirement |
| [inference] The same declaration can support PIP anomaly detection. | [PIP invariant anomaly detection](https://davidamitchell.github.io/Research/research/2026-04-27-pip-invariant-anomaly-detection.html); [NIST SP 800-162](https://csrc.nist.gov/pubs/sp/800/162/final) | high | shared baseline across control surfaces |
| [inference] Amendment versus new registration should follow architecture-boundary change rules. | [NIST SP 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5); [NIST landing page](https://csrc.nist.gov/pubs/sp/800/53/r5/final); [Organisational intent formal specification](https://davidamitchell.github.io/Research/research/2026-03-14-organisational-intent-formal-specification.html) | medium | lifecycle governance rule |

### Assumptions

- [assumption; source: https://csrc.nist.gov/pubs/sp/800/162/final] **Assumption:** runtime telemetry can be normalized into stable subject, object, action, and environment style attributes for every relevant tool call. **Justification:** ABAC assumes such attributes exist, but this item did not test a concrete telemetry collector.
- [assumption; source: https://www.w3.org/TR/vc-data-model/; https://github.com/in-toto/attestation/blob/main/spec/v1/statement.md] **Assumption:** a production implementation can combine a verifiable credential envelope with an in-toto digest subject without incompatible trust semantics. **Justification:** the standards are composable on paper, but this item did not build an interoperability profile.

### Analysis

[inference; source: https://iang.org/papers/ricardian_contract.html; https://www.w3.org/TR/vc-data-model/] Ricardian contracts solve the dual requirement that humans need narrative meaning while machines need structured claims, and verifiable credentials extend that pattern with standard fields for proof, schema, validity, evidence, and status. [inference; source: https://github.com/in-toto/attestation/blob/main/spec/v1/statement.md; https://slsa.dev/spec/v1.0/provenance] In-toto and SLSA fill the remaining gap by making immutable digest identity and dependency lineage first-class, which is exactly what lifecycle-stable evaluation needs when the same intent baseline must be recognized months later. [inference; source: https://csrc.nist.gov/pubs/sp/800/162/final; https://docs.oasis-open.org/xacml/3.0/xacml-3.0-core-spec-os-en.html] ABAC and XACML then anchor the runtime side of the design, because they show that policy evaluation ultimately compares bounded attributes rather than prose intentions. [inference; source: https://davidamitchell.github.io/Research/research/2026-03-10-language-for-llm-agent-output.html; https://davidamitchell.github.io/Research/research/2026-03-10-formal-spec-intent-alignment-agentic-coding.html] The central tradeoff is therefore explicit: richer prose improves human context, but only typed bounded claims preserve machine evaluability and reduce reward-hacking opportunities.

### Risks, Gaps, and Uncertainties

- [fact; source: https://www.w3.org/TR/vc-data-model/] The Verifiable Credentials Data Model does not define a domain ontology for capability, data, or action classes, so a production system still needs a controlled vocabulary profile.
- [fact; source: https://w3c-ccg.github.io/zcap-spec/] ZCAP-LD is a community draft rather than a finalized broad standard, so its caveat and delegation model is a strong reference but not a settled interoperability baseline.
- [inference; source: https://davidamitchell.github.io/Research/research/2026-04-27-pip-invariant-anomaly-detection.html] The representation is rich enough for the PIP prior model in principle, but this item did not estimate how much historical telemetry is needed before those priors become dependable in practice.
- [assumption; source: https://doi.org/10.6028/NIST.SP.800-53r5; https://csrc.nist.gov/pubs/sp/800/53/r5/final] Regulatory alignment was inferred from architecture-control language rather than from sector-specific supervisory guidance written specifically for agentic systems.

### Open Questions

- [inference; source: https://w3c-ccg.github.io/zcap-spec/; https://www.w3.org/TR/vc-data-model/] What controlled vocabulary for purpose classes, action patterns, and caveats will remain portable across tools and organizations without becoming so abstract that runtime evaluation loses precision?
- [inference; source: https://github.com/in-toto/attestation/blob/main/spec/v1/statement.md; https://slsa.dev/spec/v1.0/provenance] Should partial revocation of individual capabilities be modeled as a special amendment type, or should revocation always issue a whole new declaration to keep verification simpler?
- [inference; source: https://davidamitchell.github.io/Research/research/2026-04-27-pip-invariant-anomaly-detection.html] How should the PIP handle rare but legitimate emergency overrides without normalizing exceptional high-risk behavior into the asset's expected baseline?

---

## Output

- Type: knowledge
- Description: A specification for an immutable, signed intent credential consisting of a human-readable intent statement, a machine-readable intent declaration triple, and an append-only amendment chain for legitimate scope evolution.
- Links:
  - https://iang.org/papers/ricardian_contract.html
  - https://www.w3.org/TR/vc-data-model/
  - https://github.com/in-toto/attestation/blob/main/spec/v1/statement.md
