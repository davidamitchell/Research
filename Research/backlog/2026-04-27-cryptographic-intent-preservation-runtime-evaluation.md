---
title: "Cryptographic preservation and runtime evaluation of original intent: a representation formalism for Getting Started phase intent that is simultaneously verifiable and semantically stable across the full operational lifecycle"
added: 2026-04-27T00:55:35+00:00
status: backlog
priority: high
blocks: []
tags: [pbac, pdp, pip, intent-preservation, cryptographic-binding, ricardian-contract, formal-specification, agentic-ai, lifecycle-governance, dikw, intent-driven-development, semantic-stability]
started: ~
completed: ~
output: [knowledge]
---

# Cryptographic preservation and runtime evaluation of original intent: a representation formalism for Getting Started phase intent that is simultaneously verifiable and semantically stable across the full operational lifecycle

## Research Question

What representation of original intent — captured at the Getting Started phase — is simultaneously cryptographically verifiable and semantically stable enough to function as a meaningful evaluation baseline for the Policy Decision Point (PDP) across the full operational lifecycle of a governed asset, including legitimate scope evolution?

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
- Invariant registration mechanism in the PAP (covered by RQ1) — though the intent triple includes the invariant set as a subset
- Anomaly detection in the PIP (covered by RQ4) — though the representation produced here must be evaluable by the PIP
- Organisation-level intent (the organisational intent formal specification item) — this research is scoped to asset-level intent only

**Constraints:**
- Depends on RQ1 (invariant registration, which is a subset of the intent capture problem) and RQ4 (the PIP uses the intent baseline to detect suppression — the representation must be evaluable by the PIP's anomaly detection, not just by the PDP)
- The representation must be specific enough to be evaluable against tool calls — vague natural language is insufficient
- The representation must be stable enough to survive legitimate operating context change — over-specification that flags legitimate evolution is a failure mode
- The false-positive problem (flagging legitimate scope evolution) and the false-negative problem (missing genuine drift) must both be explicitly addressed — the amendment protocol is the mechanism for the former

## Context

Hash-binding a natural language intent document is trivial. The hard problem is that intent expressed in natural language or structured goals drifts in meaning as context changes, even when the artefact is bit-for-bit identical. A statement of intent authored eighteen months ago may produce false positives (flagging legitimate scope evolution as task creep) or false negatives (failing to flag genuine drift because the surface language has not changed).

The organisational intent formal specification item asks whether organisational intent can be expressed as a formally structured specification from which human-readable artefacts are derived and against which Objectives and Key Results (OKRs) can be continuously checked — this research applies the same discipline to asset-level intent. Intent-Driven Development (IDD) proposes intent as the primary specification primitive above Test-Driven Development (TDD) and Specification-Driven Development (SDD) — the Getting Started phase intent capture is IDD applied to governed assets. The Ricardian Contract model demonstrates a working architecture for binding a human-readable document to a machine-processable form via cryptographic hash, with the hash serving as the canonical reference — the intent preservation problem is structurally identical.

## Approach

1. **Representation formalism design:** Design the intent triple (authorised-capability-set, authorised-data-scope, authorised-action-envelope). For each component: define the schema, define what constitutes a violation, and define how the PDP evaluates an observed tool call against it. Assess whether the triple is complete (covers all evaluable dimensions of intent) or whether additional components are required.
2. **Ricardian Contract adaptation:** Adapt the Ricardian Contract architecture to intent representation. Define: (a) the human-readable intent statement format; (b) the machine-processable capability declaration format; (c) the content-addressed hash binding them; (d) the PDP evaluation protocol against the machine-processable component; (e) the audit trail function of the human-readable component.
3. **Semantic stability analysis:** Analyse the stability properties of the intent triple under legitimate scope evolution. Define conditions under which each component can change without constituting unauthorised drift. Define conditions under which surface language change without triple change constitutes a false negative.
4. **Amendment protocol design:** Design the formal amendment protocol for legitimate scope evolution. Define: (a) the amendment request format; (b) the cryptographic chaining mechanism (amendment hashes include a reference to the original and all prior amendments); (c) the governance gate required to approve an amendment; (d) how the PDP evaluates tool calls against an amended triple.
5. **DIKW transformation function:** Define the transformation function from tool-call Data (the observable) to the Knowledge level of the intent triple (the evaluable baseline). This is the mechanism by which the PDP moves from "what tool call was made" to "does this tool call fall within the authorised-action-envelope?"
6. **Agent-evaluable format constraint:** Validate the representation against the agent-evaluable constraint: can an Large Language Model (LLM) agent evaluate a proposed tool call against the machine-processable representation without human mediation? If not, what additional structure is required?
7. **PIP evaluability:** Validate the representation against the PIP's anomaly detection requirement (RQ4): can the PIP's Bayesian surprise model compute a prior probability over legitimate task intents given the intent triple? If not, what additional structure is required?
8. **Synthesis:** Produce a complete intent representation specification, a worked example for a CIA-High PII-handling agentic system, an amendment protocol schema, and a decision framework for PAP implementors characterising when an amendment is required vs. when a new asset registration is required.

## Sources

- [ ] [Organisational intent formal specification — completed item](https://davidamitchell.github.io/Research/research/2026-03-14-organisational-intent-formal-specification.html) — organisation-level analogue; same discipline applied to asset-level intent
- [ ] [Intent-Driven Development (IDD) — completed item](https://davidamitchell.github.io/Research/research/2026-03-16-intent-driven-development.html) — intent as the primary specification primitive; Getting Started intent capture as IDD applied to governed assets
- [ ] [Ricardian Contract model — completed item](https://davidamitchell.github.io/Research/research/2026-03-14-ricardian-contract-model.html) — binding human-readable document to machine-processable form via cryptographic hash; direct architectural analogue
- [ ] [Language designed for LLM agents to produce — completed item](https://davidamitchell.github.io/Research/research/2026-03-10-language-for-llm-agent-output.html) — structured output format that agents can evaluate against; constraint on the representation design
- [ ] [DIKW transformation functions — completed item](https://davidamitchell.github.io/Research/research/2026-03-10-dikw-transformation-functions.html) — theoretical frame: intent at Getting Started is Knowledge; PDP evaluates tool calls (Data) against it; the transformation function is the representation problem
- [ ] [Formal intent specification and reward hacking — completed item](https://davidamitchell.github.io/Research/research/2026-03-10-formal-spec-intent-alignment-agentic-coding.html) — formal specification as defence against reward hacking; intent triple must be robust to specification gaming
- [ ] [Ricardian Contracts — original Grigg paper](https://iang.org/papers/ricardian_contract.html) — original architecture for human-readable + machine-processable document binding
- [ ] [NIST SP 800-53 Rev 5 — PL-8 (Security and Privacy Architectures) and SA-17 (Developer Security and Privacy Architecture)](https://csrc.nist.gov/pubs/sp/800/53/r5/final) — regulatory basis for intent documentation and architecture specification requirements
- [ ] [W3C Verifiable Credentials Data Model](https://www.w3.org/TR/vc-data-model/) — machine-processable, cryptographically verifiable credential architecture as a reference for the intent representation format
- [ ] [Object Capability (OCAP) model literature](https://en.wikipedia.org/wiki/Object-capability_model) — capability-based security theory for the authorised-capability-set component of the intent triple

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
