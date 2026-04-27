---
title: "Invariant-based anomaly detection in the Policy Information Point (PIP): detecting permanent-invariant suppression through transient operating context and the decision signal to the Policy Decision Point (PDP)"
added: 2026-04-27T00:55:35+00:00
status: backlog
priority: high
blocks: [2026-04-27-cryptographic-intent-preservation-runtime-evaluation]
tags: [pbac, pip, pdp, invariant, anomaly-detection, agentic-ai, intent-alignment, prompt-injection, cynefin, bayesian-reasoning, reward-hacking, context-synthesis]
started: ~
completed: ~
output: [knowledge]
---

# Invariant-based anomaly detection in the Policy Information Point (PIP): detecting permanent-invariant suppression through transient operating context and the decision signal to the Policy Decision Point (PDP)

## Research Question

How can the Policy Information Point (PIP) detect when a governed asset's transient operating context is being used — intentionally or through task creep — to suppress or obscure a permanent invariant, and what decision signal should the PIP surface to the Policy Decision Point (PDP) when that suppression pattern is detected?

## Scope

**In scope:**
- The anomaly detection mechanism by which the PIP synthesises permanent invariants (registered at Getting Started, Layer 3 Asset Metadata) against transient Task Intent (Layer 8) to detect improbable combinations
- Taxonomy of invariant-shadowing: passive suppression (task framing genuinely excludes invariant-relevant operations) vs. active suppression (task framing excludes invariant-relevant operations but requested tool calls would trigger them)
- The Bayesian surprise score model: given the asset's invariant set, the prior probability of the declared Task Intent being legitimate; low-probability combinations surfaced as anomalous
- The decision signal the PIP surfaces to the PDP: signal type, confidence score, routing to the correct remediation path
- Cynefin framework applied to task complexity declaration: detecting when a task is framed as Simple or Clear to avoid triggering Personally Identifiable Information (PII) or financial-transaction invariant checks
- Prompt injection as the primary mechanism for adversarial context substitution: the PIP's suppression detection treating injected context with the same suspicion as adversarially crafted task framing
- The neurological context management research as the architectural analogue: prior-weighted relevance filtering formalised as a PIP mechanism

**Out of scope:**
- Invariant registration mechanism (covered by RQ1)
- Ensuring the invariant set the PIP checks is current (covered by RQ2)
- Kill-switch and remediation protocols (covered by RQ3)
- Cryptographic binding of original intent (covered by RQ5)
- Full prompt injection threat taxonomy (the scoped concern is only the PIP's detection of injected context substitution)

**Constraints:**
- Depends on RQ1 (invariant registration mechanism) and RQ2 (ensuring the invariant set the PIP checks is current)
- The detection problem is anomaly detection, not conflict resolution — invariants win by definition; the research must address the detection mechanism, not the priority ordering
- The active suppression case (tool calls would trigger invariant-relevant operations despite framing) is the priority concern; passive suppression may be a valid operating state
- The PIP signal must be typed so the PDP can route it to the correct remediation path — signal typing is a required output

## Context

Invariants win by definition in any correctly designed system. The interesting problem is not conflict resolution but detection: when a task is framed in a way that appears to exclude invariant-relevant operations, but the tool calls requested would in fact trigger them, the PIP must recognise the mismatch.

This is an anomaly detection problem with an adversarial dimension. Prompt injection is the primary mechanism by which transient context is maliciously substituted to suppress invariant checks. The formal intent specification and reward hacking research establishes that intent mismatch and reward hacking share a structural root — an agent finding a path through the intent specification that satisfies local conditions while violating global ones. The PIP's suppression detection problem is the runtime manifestation of this.

The 8-layer context architecture (Aligned Decision-Making framework) defines the layers the PIP must synthesise — invariants sit at Layer 3 (Asset Metadata), Task Intent at Layer 8. The failure mode taxonomy classifies the suppression pattern as an intent-alignment failure distinct from hallucination or capability failure — the PIP signal must be typed accordingly.

## Approach

1. **Invariant-shadowing taxonomy:** Define the taxonomy of suppression patterns. Distinguish: (a) passive suppression — task framing genuinely excludes invariant-relevant operations (legitimate); (b) active suppression — task framing excludes invariant-relevant operations but the tool calls requested would trigger them (anomalous); (c) adversarial suppression — task framing is deliberately constructed to avoid invariant checks (malicious). Define detection indicators for each class.
2. **Bayesian surprise score model:** Construct the anomaly detection model. For each invariant class, define: (a) the prior probability distribution over legitimate task intents given that invariant; (b) the likelihood function for the observed (task-framing, tool-calls-requested) pair; (c) the surprise score as a Bayesian update; (d) the threshold above which the PIP raises a signal.
3. **Cynefin × invariant matrix:** Construct the matrix of Cynefin complexity domains (Clear, Complicated, Complex, Chaotic) against invariant classes. For each cell, define the expected PIP signal: e.g., a Personally Identifiable Information (PII)-handling asset declaring a Clear task with no data-access justification is anomalous; the same asset declaring a Complex task with data-access scope is expected.
4. **Prompt injection as context substitution:** Characterise prompt injection as a specific mechanism of active suppression. Define the PIP's detection indicators for injected context: anomalous authority claims, out-of-band instruction patterns, context that contradicts registered asset metadata.
5. **Neurological context management analogue:** Draw on the neurological context management research to formalise the prior-weighted relevance filtering mechanism. Map the human working-memory model to the PIP architecture: what is the equivalent of salience weighting for invariant-context synthesis?
6. **PDP signal specification:** Define the signal the PIP surfaces to the PDP: (a) signal type (passive-suppression, active-suppression, adversarial-suppression); (b) confidence score; (c) the invariant(s) involved; (d) the recommended PDP response for each signal type. Ensure the signal is typed so the PDP can route it to the correct remediation path without ambiguity.
7. **Synthesis:** Produce a PIP anomaly detection specification, a worked example for a PII-handling agent declaring a Simple task with financial tool calls, and a signal taxonomy for PDP implementors.

## Sources

- [ ] [Aligned Decision-Making 8-layer context architecture — completed item](https://davidamitchell.github.io/Research/research/2026-03-15-context-layers-aligned-decisions-synthesis.html) — Layer 3 (Asset Metadata) and Layer 8 (Task Intent) that the PIP must synthesise
- [ ] [Formal intent specification and reward hacking — completed item](https://davidamitchell.github.io/Research/research/2026-03-10-formal-spec-intent-alignment-agentic-coding.html) — structural root shared by intent mismatch and reward hacking; PIP detection as the runtime manifestation
- [ ] [Prompt injection threat landscape — completed item](https://davidamitchell.github.io/Research/research/2026-03-15-prompt-injection-threat-landscape.html) — primary adversarial mechanism for transient context substitution
- [ ] [Failure mode taxonomy expansion — completed item](https://davidamitchell.github.io/Research/research/2026-03-12-failure-mode-taxonomy-expansion.html) — suppression pattern classified as intent-alignment failure; PIP signal must be typed accordingly
- [ ] [Neurological context management — completed item](https://davidamitchell.github.io/Research/research/2026-03-15-neurological-context-management.html) — prior-weighted relevance filtering as the architectural analogue for PIP anomaly detection
- [ ] [Cynefin framework — Snowden and Boone original paper](https://hbr.org/2007/11/a-leaders-framework-for-decision-making) — complexity domain taxonomy for task framing analysis
- [ ] [Bayesian surprise and anomaly detection — survey literature](https://en.wikipedia.org/wiki/Bayesian_inference) — formal basis for the surprise score model
- [ ] [NIST SP 800-53 Rev 5 — SI-4 (System Monitoring) and AU-6 (Audit Record Review)](https://csrc.nist.gov/pubs/sp/800/53/r5/final) — regulatory basis for anomaly detection and signal surfacing requirements
- [ ] [OWASP Top 10 for Large Language Model (LLM) Applications — LLM01 Prompt Injection](https://owasp.org/www-project-top-10-for-large-language-model-applications/) — prompt injection characterisation for PIP detection design

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
