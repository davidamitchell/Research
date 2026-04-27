---
title: "Universal policy synchronisation and integrity: ensuring the Policy Decision Point (PDP) evaluates governed assets against logically identical policy across all lifecycle phases"
added: 2026-04-27T00:55:35+00:00
status: backlog
priority: high
blocks: [2026-04-27-out-of-band-policy-invalidation-remediation, 2026-04-27-pip-invariant-anomaly-detection]
tags: [pbac, pdp, pap, policy-synchronisation, lifecycle-governance, versioning, content-addressing, policy-lsp, governance-decay, agentic-ai]
started: ~
completed: ~
output: [knowledge]
---

# Universal policy synchronisation and integrity: ensuring the Policy Decision Point (PDP) evaluates governed assets against logically identical policy across all lifecycle phases

## Research Question

What mechanism ensures that the Policy Decision Point (PDP) evaluates a governed asset against logically identical policy at every lifecycle phase, such that a soft gate in Development and a hard gate in Operation are guaranteed to be derived from the same Policy Administration Point (PAP) source, and a policy change between phases is detected and surfaced rather than silently permitting inconsistency?

## Scope

**In scope:**
- The synchronisation protocol between PAP and all downstream PDPs across Getting Started, Development, Delivery, and Operation phases
- Content-addressed policy bundle design: compilation of policy to a deterministic hash, PDP pinning behaviour, PAP version graph maintenance
- The detection mechanism for in-flight assets whose development-time policy snapshot no longer matches the current PAP state (Governance Decay detection)
- The Delivery pipeline as the mandatory re-synchronisation point: policy diff before promotion from Development to Delivery, promotion failure on material divergence
- Treatment of policy version as a first-class attribute of asset identity — embedding, carrying, and validating the policy hash at each phase transition
- Policy versioning protocols: semantic versioning vs content-addressing, version graph structure, rollback and forward-patch behaviour
- The Language Server Protocol (LSP) as the Development-phase surface for real-time conformance guidance (scoped to its role in the synchronisation architecture, not its full capability set)

**Out of scope:**
- Out-of-band policy invalidation for assets already in Operation (covered by RQ3)
- The PAP mapping function itself (covered by RQ1)
- Anomaly detection in the Policy Information Point (PIP) (covered by RQ4)
- Intent preservation and cryptographic binding (covered by RQ5)
- Jurisdiction-specific legal analysis beyond what is needed to characterise Governance Decay as a regulatory risk

**Constraints:**
- Depends on RQ1: a defined PEP topology is required to know which PDPs must be synchronised
- The synchronisation protocol must be implementable without requiring continuous connectivity between PAP and PDPs — offline and intermittently-connected deployment contexts must be supported
- The Governance Decay failure mode must be characterised precisely: the research must distinguish silent inconsistency (the dangerous case) from detected inconsistency (the recoverable case)

## Context

The failure mode this research addresses is Governance Decay: a developer satisfies a diagnostic check at Development time, the PAP is updated before the asset reaches Operation, and the runtime PEP enforces a materially different policy without anyone being aware the baseline shifted. This is not a theoretical risk — the practical failure of heterogeneous gate implementations producing inconsistent evidence across the compliance scanning items demonstrates the same symptom at smaller scale.

The Policy-LSP concept (real-time diagnostics via Language Server Protocol) provides the Development-phase surface. The compliance scanning and cross-scanner normalisation items demonstrate the practical failure of heterogeneous gate implementations producing inconsistent evidence — the exact symptom this research aims to structurally prevent.

Treating policy as a formally versioned artefact — from which phase-specific gate configurations are derived and against which phase transitions can be checked — is the architectural discipline required. The content-addressed approach (policy compiled to a deterministic hash, PDPs pin the hash, PAP maintains a version graph) makes Governance Decay detectable rather than silent.

## Approach

1. **Governance Decay failure mode characterisation:** Define the failure mode precisely. Enumerate the conditions under which Governance Decay occurs silently vs. detectably. Survey the compliance scanning and cross-scanner normalisation items for empirical evidence of the symptom.
2. **Content-addressed policy bundle design:** Design the content-addressed policy bundle architecture. Define: (a) the compilation from PAP policy to deterministic hash; (b) PDP pinning behaviour; (c) PAP version graph structure; (d) the detection signal when a PDP is operating on a stale hash.
3. **Phase-transition synchronisation protocol:** Define the synchronisation protocol for each phase transition. For Development → Delivery: mandatory policy diff, promotion failure on material divergence, definition of "material divergence". For Delivery → Operation: final hash validation before deployment.
4. **Policy hash as asset identity attribute:** Define how the policy hash is embedded in the asset's metadata at Getting Started, carried forward through each phase, and validated at each phase transition. Specify what constitutes a policy hash mismatch and the required response.
5. **LSP integration surface:** Specify the Development-phase surface: how the Policy-LSP consults the pinned policy snapshot, how it detects PAP divergence in real time, and what signal it surfaces to the developer.
6. **Orphaned snapshot handling:** Analyse the state-orphaning risk (analogous to stateless-agent assumption failure across session boundaries) applied to policy snapshots across lifecycle boundaries. Define the recovery protocol for orphaned snapshots.
7. **Synthesis:** Produce a synchronisation protocol specification, a version graph schema, and a decision framework for PAP implementors characterising when synchronous vs. asynchronous synchronisation is required.

## Sources

- [ ] [Policy-LSP / Guiding Headless Agents — completed item](https://davidamitchell.github.io/Research/research/2026-03-01-agent-lsp-policy-enforcement.html) — LSP-like mechanisms as the right architectural pattern for real-time conformance guidance; does not address synchronisation across lifecycle phases
- [ ] [Compliance scanning GitHub Actions — completed item](https://davidamitchell.github.io/Research/research/2026-03-22-compliance-scanning-gh-actions.html) — empirical evidence of heterogeneous gate failure producing inconsistent evidence
- [ ] [Cross-scanner compliance evidence normalisation — completed item](https://davidamitchell.github.io/Research/research/2026-03-22-cross-scanner-compliance-evidence-normalisation.html) — cross-scanner inconsistency as the symptom this architecture prevents
- [ ] [Organisational intent formal specification — completed item](https://davidamitchell.github.io/Research/research/2026-03-14-organisational-intent-formal-specification.html) — treating intent as a formally versioned artefact; same discipline applied to policy produces content-addressed bundles
- [ ] [Stateless-agent assumption failure — completed item](https://davidamitchell.github.io/Research/research/2026-03-18-stateless-agent-assumption-failure.html) — state orphaning across session boundaries; policy snapshots face the same risk across lifecycle boundaries
- [ ] [NIST SP 800-162 — Guide to Attribute-Based Access Control (ABAC)](https://csrc.nist.gov/pubs/sp/800/162/final) — policy administration and decision point architecture reference
- [ ] [Open Policy Agent (OPA) documentation — policy versioning and bundle distribution](https://www.openpolicyagent.org/docs/latest/management-bundles/) — practical content-addressed bundle distribution reference implementation
- [ ] [Sigstore / in-toto attestation frameworks](https://www.sigstore.dev/) — content-addressed artefact signing as an analogue for policy bundle integrity
- [ ] [Git content-addressable storage model](https://git-scm.com/book/en/v2/Git-Internals-Git-Objects) — content-addressing reference for version graph design

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
