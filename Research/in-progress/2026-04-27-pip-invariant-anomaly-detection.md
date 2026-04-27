---
review_count: 2
title: "Invariant-based anomaly detection in the Policy Information Point (PIP): detecting permanent-invariant suppression through transient operating context and the decision signal to the Policy Decision Point (PDP)"
added: 2026-04-27T00:55:35+00:00
status: reviewing
priority: high
blocks: [2026-04-27-cryptographic-intent-preservation-runtime-evaluation]
tags: [pbac, pip, pdp, invariant, anomaly-detection, agentic-ai, intent-alignment, prompt-injection, cynefin, bayesian-reasoning, reward-hacking, context-synthesis]
started: 2026-04-27T04:33:32+00:00
completed: ~
output: [knowledge]
---

# Invariant-based anomaly detection in the Policy Information Point (PIP): detecting permanent-invariant suppression through transient operating context and the decision signal to the Policy Decision Point (PDP)

## Research Question

How can the Policy Information Point (PIP) detect when a governed asset's transient operating context is being used, intentionally or through task creep, to suppress or obscure a permanent invariant, and what decision signal should the PIP surface to the Policy Decision Point (PDP) when that suppression pattern is detected?

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
- The detection problem is anomaly detection, not conflict resolution - invariants win by definition; the research must address the detection mechanism, not the priority ordering
- The active suppression case (tool calls would trigger invariant-relevant operations despite framing) is the priority concern; passive suppression may be a valid operating state
- The PIP signal must be typed so the PDP can route it to the correct remediation path - signal typing is a required output

## Context

- [fact; source: https://davidamitchell.github.io/Research/research/2026-03-15-context-layers-aligned-decisions-synthesis.html; https://davidamitchell.github.io/Research/research/2026-03-12-failure-mode-taxonomy-expansion.html] The relevant control surface in this repository is the synthesis of Layer 3 Asset Metadata and Layer 8 Task Intent from the aligned decision-making architecture, and the suppression pattern belongs to the intent-alignment family of failures rather than to pure generation error.
- [fact; source: https://davidamitchell.github.io/Research/research/2026-03-15-prompt-injection-threat-landscape.html; https://genai.owasp.org/llmrisk/llm01-prompt-injection/] Prompt injection is the primary adversarial mechanism in scope because it lets untrusted external content substitute transient operating context in ways that can influence privileged decisions and connected tool use.
- [inference; source: https://davidamitchell.github.io/Research/research/2026-03-15-neurological-context-management.html; https://pmc.ncbi.nlm.nih.gov/articles/PMC2782645/] The design problem is therefore a relevance-filtering problem: permanent invariants must stay as high-authority priors even when transient context is novel, urgent-sounding, or crafted to pull attention away from those invariants.

## Approach

1. **Invariant-shadowing taxonomy:** Define the taxonomy of suppression patterns. Distinguish: (a) passive suppression - task framing genuinely excludes invariant-relevant operations (legitimate); (b) active suppression - task framing excludes invariant-relevant operations but the tool calls requested would trigger them (anomalous); (c) adversarial suppression - task framing is deliberately constructed to avoid invariant checks (malicious). Define detection indicators for each class.
2. **Bayesian surprise score model:** Construct the anomaly detection model. For each invariant class, define: (a) the prior probability distribution over legitimate task intents given that invariant; (b) the likelihood function for the observed (task-framing, tool-calls-requested) pair; (c) the surprise score as a Bayesian update; (d) the threshold above which the PIP raises a signal.
3. **Cynefin × invariant matrix:** Construct the matrix of Cynefin complexity domains (Clear, Complicated, Complex, Chaotic) against invariant classes. For each cell, define the expected PIP signal: e.g., a Personally Identifiable Information (PII)-handling asset declaring a Clear task with no data-access justification is anomalous; the same asset declaring a Complex task with data-access scope is expected.
4. **Prompt injection as context substitution:** Characterise prompt injection as a specific mechanism of active suppression. Define the PIP's detection indicators for injected context: anomalous authority claims, out-of-band instruction patterns, context that contradicts registered asset metadata.
5. **Neurological context management analogue:** Draw on the neurological context management research to formalise the prior-weighted relevance filtering mechanism. Map the human working-memory model to the PIP architecture: what is the equivalent of salience weighting for invariant-context synthesis?
6. **PDP signal specification:** Define the signal the PIP surfaces to the PDP: (a) signal type (passive-suppression, active-suppression, adversarial-suppression); (b) confidence score; (c) the invariant(s) involved; (d) the recommended PDP response for each signal type. Ensure the signal is typed so the PDP can route it to the correct remediation path without ambiguity.
7. **Synthesis:** Produce a PIP anomaly detection specification, a worked example for a PII-handling agent declaring a Simple task with financial tool calls, and a signal taxonomy for PDP implementors.

## Sources

- [x] [Aligned Decision-Making 8-layer context architecture - completed item](https://davidamitchell.github.io/Research/research/2026-03-15-context-layers-aligned-decisions-synthesis.html) - Layer 3 (Asset Metadata) and Layer 8 (Task Intent) that the PIP must synthesise
- [x] [Formal intent specification and reward hacking - completed item](https://davidamitchell.github.io/Research/research/2026-03-10-formal-spec-intent-alignment-agentic-coding.html) - structural root shared by intent mismatch and reward hacking; PIP detection as the runtime manifestation
- [x] [Prompt injection threat landscape - completed item](https://davidamitchell.github.io/Research/research/2026-03-15-prompt-injection-threat-landscape.html) - primary adversarial mechanism for transient context substitution
- [x] [Failure mode taxonomy expansion - completed item](https://davidamitchell.github.io/Research/research/2026-03-12-failure-mode-taxonomy-expansion.html) - suppression pattern classified as intent-alignment failure; PIP signal must be typed accordingly
- [x] [Neurological context management - completed item](https://davidamitchell.github.io/Research/research/2026-03-15-neurological-context-management.html) - prior-weighted relevance filtering as the architectural analogue for PIP anomaly detection
- [x] [Cynefin framework - Snowden and Boone original article](https://hbr.org/2007/11/a-leaders-framework-for-decision-making) - mainstream reference for the framework
- [x] [The Cynefin Co overview of the Cynefin framework](https://thecynefin.co/effective-decision-making-support-tool/) - accessible domain definitions and response logics
- [x] [Bayesian inference background](https://en.wikipedia.org/wiki/Bayesian_inference) - seed background reference checked during investigation
- [x] [Itti and Baldi, Bayesian Surprise Attracts Human Attention](https://pmc.ncbi.nlm.nih.gov/articles/PMC2782645/) - formal basis for surprise as posterior-vs-prior belief shift
- [x] [National Institute of Standards and Technology (NIST) Special Publication (SP) 800-53 Rev. 5 landing page](https://csrc.nist.gov/pubs/sp/800/53/r5/final) - control-catalog anchor
- [x] [NIST SP 800-53 control extract, SI-4 (System Monitoring)](https://csf.tools/reference/nist-sp-800-53/r5/si/si-4/) - monitoring, anomaly analysis, and alerting requirements
- [x] [NIST SP 800-53 control extract, AU-6 (Audit Record Review, Analysis, and Reporting)](https://csf.tools/reference/nist-sp-800-53/r5/au/au-6/) - review, correlation, reporting, and risk-adjusted audit analysis
- [x] [eXtensible Access Control Markup Language (XACML) 3.0 core specification](https://docs.oasis-open.org/xacml/3.0/xacml-3.0-core-spec-os-en.html) - authoritative definitions of the Policy Administration Point (PAP), Policy Decision Point (PDP), Policy Enforcement Point (PEP), and Policy Information Point (PIP)
- [x] [Open Worldwide Application Security Project (OWASP) Top 10 for Large Language Model (LLM) Applications](https://owasp.org/www-project-top-10-for-large-language-model-applications/) - project overview and LLM01 linkage
- [x] [Open Worldwide Application Security Project (OWASP) LLM01 Prompt Injection](https://genai.owasp.org/llmrisk/llm01-prompt-injection/) - prompt injection characterisation for PIP detection design
- [x] [PAP dynamic policy profiling and proportionality - completed item](https://davidamitchell.github.io/Research/research/2026-04-27-pap-dynamic-policy-profiling-proportionality.html) - adjacent Policy-Based Access Control (PBAC) control-topology derivation
- [x] [Universal policy synchronisation and integrity - completed item](https://davidamitchell.github.io/Research/research/2026-04-27-pdp-universal-policy-synchronisation-integrity.html) - adjacent lifecycle policy-integrity surface
- [x] [Access control amplification under agentic operations - completed item](https://davidamitchell.github.io/Research/research/2026-04-26-access-control-amplification-agentic-operations.html) - operational blast-radius consequence when invariant checks are suppressed
- [x] [Artificial Intelligence (AI) agent identity and access management - completed item](https://davidamitchell.github.io/Research/research/2026-04-26-ai-agent-identity-access-management-enterprise.html) - machine-identity and bounded-delegation implications for routing

## Related

- [Aligned Decision-Making: Context Architecture for AI Agents in Organisations](https://davidamitchell.github.io/Research/research/2026-03-15-context-layers-aligned-decisions-synthesis.html)
- [Policy Administration Point (PAP) dynamic policy profiling and proportionality](https://davidamitchell.github.io/Research/research/2026-04-27-pap-dynamic-policy-profiling-proportionality.html)
- [Universal policy synchronisation and integrity](https://davidamitchell.github.io/Research/research/2026-04-27-pdp-universal-policy-synchronisation-integrity.html)
- [Prompt injection threat landscape: exploits, defences, and active research in agentic artificial intelligence (AI) systems](https://davidamitchell.github.io/Research/research/2026-03-15-prompt-injection-threat-landscape.html)

---

## Research Skill Output

*(Full output from running the research skill - retained verbatim in the completed item. Sections 0 to 5 are the investigation, and Section 6 seeds the Findings section below.)*

### §0 Initialise

- [fact; source: https://docs.oasis-open.org/xacml/3.0/xacml-3.0-core-spec-os-en.html; https://davidamitchell.github.io/Research/research/2026-03-15-context-layers-aligned-decisions-synthesis.html] **Research question restated:** how should a Policy Information Point (PIP) detect that transient task framing or injected operating context is suppressing a permanent invariant registered against the asset, and what typed decision signal should it surface to the Policy Decision Point (PDP) when that anomaly appears?
- [fact; source: https://davidamitchell.github.io/Research/research/2026-04-27-pap-dynamic-policy-profiling-proportionality.html; https://davidamitchell.github.io/Research/research/2026-04-27-pdp-universal-policy-synchronisation-integrity.html] **Scope confirmed:** the item covers taxonomy, anomaly scoring, Cynefin-based task-framing interpretation, prompt-injection-driven context substitution, a neurological analogue for relevance filtering, and a typed runtime signal; it does not redesign invariant registration, policy freshness, remediation workflows, or cryptographic intent binding.
- [fact; source: https://davidamitchell.github.io/Research/research/2026-03-10-formal-spec-intent-alignment-agentic-coding.html; https://genai.owasp.org/llmrisk/llm01-prompt-injection/] **Constraints confirmed:** invariants win by definition, so the problem is detection rather than conflict resolution; the active-suppression case is the priority; prompt injection is treated as one mechanism of context substitution, not as the whole problem; and the output must remain machine-routable.
- [fact; source: https://davidamitchell.github.io/Research/research/2026-03-15-context-layers-aligned-decisions-synthesis.html; https://davidamitchell.github.io/Research/research/2026-03-10-formal-spec-intent-alignment-agentic-coding.html; https://davidamitchell.github.io/Research/research/2026-03-15-prompt-injection-threat-landscape.html; https://davidamitchell.github.io/Research/research/2026-03-12-failure-mode-taxonomy-expansion.html; https://davidamitchell.github.io/Research/research/2026-03-15-neurological-context-management.html; https://davidamitchell.github.io/Research/research/2026-04-27-pap-dynamic-policy-profiling-proportionality.html; https://davidamitchell.github.io/Research/research/2026-04-27-pdp-universal-policy-synchronisation-integrity.html] **Prior work cross-reference:** adjacent completed items already define the eight-layer context model, the formal-specification view of intent mismatch and reward hacking, the prompt-injection threat model, the failure-mode typing, the neurological relevance-filtering analogue, the PAP-side proportional topology rule, and the PDP-side policy-integrity rule. This item extends that chain by specifying the missing runtime anomaly detector between registered invariants and policy decision routing.
- [fact; source: https://csf.tools/reference/nist-sp-800-53/r5/si/si-4/; https://csf.tools/reference/nist-sp-800-53/r5/au/au-6/] **Output format confirmed:** knowledge, specifically a suppression taxonomy, a Bayesian-style surprise score, a Cynefin-by-invariant interpretation rule, a worked example, and a typed PIP-to-PDP signal specification.

### §1 Question Decomposition

- **Root question:** how should the PIP detect and classify suppression of permanent invariants by transient context before the PDP renders or enforces a decision?
- **A. Taxonomy**
  - A1. What observable patterns distinguish passive suppression, active suppression, and adversarial suppression?
  - A2. Which signals come from framing, tool requests, provenance, and asset metadata?
- **B. Bayesian surprise model**
  - B1. What prior should exist over legitimate task intents for a given invariant set?
  - B2. What likelihood terms should be computed from framing, tool sequence, and context provenance?
  - B3. What thresholding rule turns surprise into a typed anomaly class?
- **C. Cynefin interaction**
  - C1. How should task declarations in the Clear, Complicated, Complex, and Chaotic domains alter the expected prior?
  - C2. Which combinations of domain declaration and requested actions are improbable for high-invariant assets?
- **D. Prompt injection as context substitution**
  - D1. Which injected-context indicators should increase suspicion?
  - D2. When does suspicious context plus action mismatch become adversarial suppression rather than merely active suppression?
- **E. Neurological analogue**
  - E1. What does prior-weighted relevance filtering imply for how invariants should be kept active?
  - E2. What is the functional equivalent of salience weighting inside the PIP?
- **F. PDP signal**
  - F1. Which fields must the signal include so the PDP can route it unambiguously?
  - F2. What response path should correspond to each suppression class?

### §2 Investigation

- [fact; source: https://docs.oasis-open.org/xacml/3.0/xacml-3.0-core-spec-os-en.html; https://csf.tools/reference/nist-sp-800-53/r5/si/si-4/; https://csf.tools/reference/nist-sp-800-53/r5/au/au-6/; https://genai.owasp.org/llmrisk/llm01-prompt-injection/] **Source classes:** primary external sources in this item are XACML role definitions, NIST monitoring and audit controls, and OWASP prompt-injection guidance; repository completed items are internal syntheses used only where they materially qualify the same runtime control surface.

#### 2.1 Why the PIP is the correct detection surface

- [fact; source: https://docs.oasis-open.org/xacml/3.0/xacml-3.0-core-spec-os-en.html] XACML defines the PIP as the system entity that acts as a source of attribute values, the PDP as the evaluator of applicable policy, and the PEP as the enforcer of authorization decisions.
- [fact; source: https://davidamitchell.github.io/Research/research/2026-03-15-context-layers-aligned-decisions-synthesis.html] The aligned decision-making item places stable asset characteristics in Layer 3 Asset Metadata and immediate task framing in Layer 8 Task Intent, making their synthesis the decisive runtime comparison for this question.
- [inference; source: https://docs.oasis-open.org/xacml/3.0/xacml-3.0-core-spec-os-en.html; https://davidamitchell.github.io/Research/research/2026-03-15-context-layers-aligned-decisions-synthesis.html] The PIP is therefore the correct place to detect suppression because it already owns the job of assembling the attributes that the PDP will consume; adding anomaly scoring there does not collapse the PAP, PIP, PDP, and PEP roles into one component.

#### 2.2 Taxonomy of invariant-shadowing

- [fact; source: https://davidamitchell.github.io/Research/research/2026-03-12-failure-mode-taxonomy-expansion.html; https://davidamitchell.github.io/Research/research/2026-03-10-formal-spec-intent-alignment-agentic-coding.html] Prior repository work distinguishes intent mismatch and reward hacking from generation error, and treats the failure as one in which local optimisation can satisfy stated framing while violating the governing objective.
- [inference; source: https://davidamitchell.github.io/Research/research/2026-03-10-formal-spec-intent-alignment-agentic-coding.html; https://docs.oasis-open.org/xacml/3.0/xacml-3.0-core-spec-os-en.html] **Passive suppression** is the case where task framing excludes invariant-relevant operations and the requested tools, scopes, and side effects also exclude them, so the invariant stays inactive for legitimate reasons.
- [inference; source: https://davidamitchell.github.io/Research/research/2026-03-10-formal-spec-intent-alignment-agentic-coding.html; https://davidamitchell.github.io/Research/research/2026-04-26-access-control-amplification-agentic-operations.html] **Active suppression** is the case where task framing excludes invariant-relevant operations but the requested tools, data scopes, or side effects would in fact touch invariant-bearing resources, creating a framing-to-action contradiction.
- [inference; source: https://genai.owasp.org/llmrisk/llm01-prompt-injection/; https://davidamitchell.github.io/Research/research/2026-03-15-prompt-injection-threat-landscape.html] **Adversarial suppression** is active suppression plus evidence that the framing was shifted by untrusted or hostile context, such as indirect prompt injection, override patterns, out-of-band authority claims, or instructions to ignore existing rules.
- [inference; source: https://genai.owasp.org/llmrisk/llm01-prompt-injection/; https://davidamitchell.github.io/Research/research/2026-04-26-ai-agent-identity-access-management-enterprise.html] The core detection indicators are therefore: declared task scope, declared task complexity, requested tool sequence, requested data scopes, external-context provenance, and whether the machine identity would exercise authority that the framing denies.

#### 2.3 Bayesian surprise score model

- [fact; source: https://pmc.ncbi.nlm.nih.gov/articles/PMC2782645/] Itti and Baldi define Bayesian surprise as the degree to which new observations shift an observer's beliefs, measured as the difference between posterior and prior belief distributions rather than as raw rarity alone.
- [fact; source: https://davidamitchell.github.io/Research/research/2026-03-15-neurological-context-management.html] The neurological context-management item concludes that higher-order goals and schemas should remain active priors that shape what counts as salient error or surprise during decision-making.
- [inference; source: https://pmc.ncbi.nlm.nih.gov/articles/PMC2782645/; https://davidamitchell.github.io/Research/research/2026-03-15-neurological-context-management.html; https://davidamitchell.github.io/Research/research/2026-03-15-context-layers-aligned-decisions-synthesis.html] For the PIP, the prior should be a distribution over legitimate task-intent classes conditioned on the asset's invariant set, asset type, lifecycle phase, and previously approved usage patterns for comparable assets.
- [inference; source: https://pmc.ncbi.nlm.nih.gov/articles/PMC2782645/; https://genai.owasp.org/llmrisk/llm01-prompt-injection/] The likelihood should be computed from the observed tuple `(declared task framing F, declared Cynefin class C, requested tool/action set U, requested data scope D, external-context provenance X)` given the invariant set `I`.
- [inference; source: https://pmc.ncbi.nlm.nih.gov/articles/PMC2782645/] A suitable surprise score is `S = D_KL(P(L | I,F,C,U,D,X) || P(L | I))`, where `D_KL` denotes Kullback-Leibler (KL) divergence and `L` is the latent class of legitimate uses for that asset; operationally, the same idea can be approximated by `-log P(F,C,U,D,X | I)` when the full posterior is impractical.
- [inference; source: https://genai.owasp.org/llmrisk/llm01-prompt-injection/; https://davidamitchell.github.io/Research/research/2026-03-15-prompt-injection-threat-landscape.html] The score should then be adjusted upward by explicit contradiction terms: action mismatch, provenance risk, and authority-override cues from injected context, because prompt-injection evidence is not merely rare text but evidence of hostile context substitution.
- [inference; source: https://davidamitchell.github.io/Research/research/2026-03-10-formal-spec-intent-alignment-agentic-coding.html; https://pmc.ncbi.nlm.nih.gov/articles/PMC2782645/] The thresholding rule follows the taxonomy: low surprise plus no action mismatch implies passive suppression; high surprise plus action mismatch implies active suppression; high surprise plus action mismatch plus hostile-context indicators implies adversarial suppression.
- [assumption; source: https://davidamitchell.github.io/Research/research/2026-04-27-pap-dynamic-policy-profiling-proportionality.html] Historical approved-use data or approved invariant-class templates are available to seed the prior. **Justification:** without some baseline of normal use, Bayesian surprise collapses into pure rule counting; if no empirical history exists, the PAP-side invariant profiles must provide the bootstrap prior.

#### 2.4 Cynefin by invariant matrix

- [fact; source: https://thecynefin.co/effective-decision-making-support-tool/; https://hbr.org/2007/11/a-leaders-framework-for-decision-making] The Cynefin framework distinguishes Clear situations, where cause and effect are well understood and best practices apply, from Complicated situations requiring expert analysis, Complex situations where patterns emerge only in hindsight, and Chaotic situations requiring immediate stabilising action.
- [inference; source: https://thecynefin.co/effective-decision-making-support-tool/; https://davidamitchell.github.io/Research/research/2026-04-27-pap-dynamic-policy-profiling-proportionality.html] A Clear declaration should lower the expected probability of broad data access, privilege elevation, or cross-system side effects for assets carrying Personally Identifiable Information (PII), financial-transaction, or privileged-control invariants, because Clear work implies known routine procedures rather than exploratory or exceptional handling.
- [inference; source: https://thecynefin.co/effective-decision-making-support-tool/; https://davidamitchell.github.io/Research/research/2026-04-27-pap-dynamic-policy-profiling-proportionality.html] A Complicated declaration is more consistent with regulated-data analysis, diagnostic review, or bounded exception handling, because expert analysis can legitimately require more context and deeper inspection without implying policy bypass.
- [inference; source: https://thecynefin.co/effective-decision-making-support-tool/; https://davidamitchell.github.io/Research/research/2026-03-15-context-layers-aligned-decisions-synthesis.html] A Complex declaration should not relax invariants; it should instead increase the need for provenance capture and richer justification because the task admits uncertainty and experimentation rather than routine execution.
- [inference; source: https://thecynefin.co/effective-decision-making-support-tool/; https://csf.tools/reference/nist-sp-800-53/r5/si/si-4/] A Chaotic declaration can justify rapid escalation and emergency routing, but precisely because it signals instability it should raise, not lower, monitoring and review requirements for high-invariant assets.

#### 2.5 Prompt injection as context substitution

- [fact; source: https://genai.owasp.org/llmrisk/llm01-prompt-injection/] OWASP states that prompt injection can be direct or indirect, that indirect injection arrives through external sources such as webpages or files, and that successful prompt injection can influence critical decision-making, reveal sensitive information, provide unauthorized function access, or execute arbitrary commands in connected systems.
- [fact; source: https://davidamitchell.github.io/Research/research/2026-03-15-prompt-injection-threat-landscape.html] The prior repository item on prompt injection concludes that indirect prompt injection becomes materially more dangerous when the model sits inside tool-using loops with memory, private context, and real-world side effects.
- [inference; source: https://genai.owasp.org/llmrisk/llm01-prompt-injection/; https://davidamitchell.github.io/Research/research/2026-03-15-prompt-injection-threat-landscape.html] The PIP should therefore treat untrusted external content as a competing authority source and increase suspicion when that content contains override phrases, requests to ignore prior instructions, new authority claims, or instructions that contradict registered asset metadata.
- [inference; source: https://genai.owasp.org/llmrisk/llm01-prompt-injection/; https://davidamitchell.github.io/Research/research/2026-04-26-access-control-amplification-agentic-operations.html] When suspicious context coincides with requests for invariant-relevant tools or data scopes that the task framing denies, the anomaly is not merely "strange input" but evidence that transient context is attempting to suppress the very invariant checks that would normally fire.

#### 2.6 Neurological analogue and salience-weighting rule

- [fact; source: https://davidamitchell.github.io/Research/research/2026-03-15-neurological-context-management.html] The neurological item argues for explicit gating, limited active context, and retrieval policies that favour high-authority priors plus situational deltas over undifferentiated bulk context.
- [fact; source: https://pmc.ncbi.nlm.nih.gov/articles/PMC2782645/] Itti and Baldi further argue that surprise is observer-relative and matters when new data materially changes the observer's beliefs, not merely when the data looks rare in isolation.
- [inference; source: https://davidamitchell.github.io/Research/research/2026-03-15-neurological-context-management.html; https://pmc.ncbi.nlm.nih.gov/articles/PMC2782645/] The functional analogue for the PIP is to keep permanent invariants in a non-evictable high-salience set, then score transient context by how much it would change the legitimacy estimate of the requested action, not by prompt length, urgency language, or novelty alone.
- [inference; source: https://davidamitchell.github.io/Research/research/2026-03-15-neurological-context-management.html; https://genai.owasp.org/llmrisk/llm01-prompt-injection/] This implies that a long prompt that stays within expected invariant boundaries should not by itself trigger, while a short external instruction that reframes a financial or PII-bearing asset as "routine" while requesting export or transaction tools should receive very high salience.

#### 2.7 PDP signal specification and worked example

- [fact; source: https://csf.tools/reference/nist-sp-800-53/r5/si/si-4/; https://csf.tools/reference/nist-sp-800-53/r5/au/au-6/] NIST SI-4 requires organizations to detect attacks and indicators of potential attacks, analyze detected events and anomalies, and provide monitoring information to defined roles; AU-6 requires review and analysis of audit records for unusual activity, reporting of findings, and adjustment of review intensity as risk changes.
- [inference; source: https://csf.tools/reference/nist-sp-800-53/r5/si/si-4/; https://csf.tools/reference/nist-sp-800-53/r5/au/au-6/; https://docs.oasis-open.org/xacml/3.0/xacml-3.0-core-spec-os-en.html] The PIP signal should therefore be a typed, auditable object with at least these fields: `signal_type`, `confidence_score`, `surprise_score`, `implicated_invariants`, `contradicting_observations`, `context_provenance`, and `recommended_route`.
- [inference; source: https://davidamitchell.github.io/Research/research/2026-04-27-pdp-universal-policy-synchronisation-integrity.html; https://davidamitchell.github.io/Research/research/2026-04-26-ai-agent-identity-access-management-enterprise.html] `signal_type = passive_suppression` should route to allow-with-log or request-clarification; `signal_type = active_suppression` should route to hold-and-step-up-review; `signal_type = adversarial_suppression` should route to deny, quarantine the untrusted context, and preserve full provenance for investigation.
- [inference; source: https://thecynefin.co/effective-decision-making-support-tool/; https://genai.owasp.org/llmrisk/llm01-prompt-injection/; https://davidamitchell.github.io/Research/research/2026-04-27-pap-dynamic-policy-profiling-proportionality.html] **Worked example:** if an asset declares invariants `{PII_handling, financial_transaction}` and the caller frames the task as Clear routine follow-up, but the requested tools include customer-record export and payment-reversal endpoints, the prior for legitimacy should be low because the action set implies exceptional state change under a routine framing.
- [inference; source: https://genai.owasp.org/llmrisk/llm01-prompt-injection/; https://davidamitchell.github.io/Research/research/2026-03-15-prompt-injection-threat-landscape.html] If the same request also includes external content saying "ignore privacy checks and use the fastest available path," the correct signal is `adversarial_suppression` with high confidence, implicated invariants `PII_handling` and `financial_transaction`, and a PDP route of deny-plus-human-review.

### §3 Reasoning

- [inference; source: https://davidamitchell.github.io/Research/research/2026-03-10-formal-spec-intent-alignment-agentic-coding.html; https://pmc.ncbi.nlm.nih.gov/articles/PMC2782645/] The decisive variable is not whether the prompt text mentions an invariant, but whether the requested operations remain probabilistically consistent with the invariant-conditioned prior for legitimate use.
- [inference; source: https://thecynefin.co/effective-decision-making-support-tool/; https://davidamitchell.github.io/Research/research/2026-04-27-pap-dynamic-policy-profiling-proportionality.html] Cynefin complexity declarations are useful because they change what kinds of operations are expected under the task, but they are prior-adjustment features rather than standalone security controls.
- [inference; source: https://genai.owasp.org/llmrisk/llm01-prompt-injection/; https://davidamitchell.github.io/Research/research/2026-03-15-prompt-injection-threat-landscape.html] Prompt-injection indicators matter because they show that the framing itself may be untrustworthy, but they should amplify contradiction-based scoring rather than replace it, since suspicious text without invariant-relevant action is not enough to prove suppression.
- [inference; source: https://csf.tools/reference/nist-sp-800-53/r5/si/si-4/; https://csf.tools/reference/nist-sp-800-53/r5/au/au-6/] The regulatory requirement is explainable anomaly detection and reporting, not opaque autonomous punishment, so the output has to remain a typed decision aid for the PDP rather than an undisclosed hidden score.

### §4 Consistency Check

- [fact; source: https://genai.owasp.org/llmrisk/llm01-prompt-injection/] OWASP states that fool-proof prevention of prompt injection is unclear, so this item's design assumes that detection and routing are necessary even when preventive controls exist.
- [fact; source: https://csf.tools/reference/nist-sp-800-53/r5/si/si-4/; https://csf.tools/reference/nist-sp-800-53/r5/au/au-6/] NIST SI-4 and AU-6 justify monitoring, anomaly analysis, correlation, and reporting, but they do not themselves prescribe that every anomaly must produce the same enforcement action.
- [inference; source: https://genai.owasp.org/llmrisk/llm01-prompt-injection/; https://csf.tools/reference/nist-sp-800-53/r5/si/si-4/] The taxonomy therefore remains internally consistent only if passive suppression is allowed as a legitimate state, active suppression becomes a policy-routing event, and adversarial suppression becomes a security-routing event.
- [inference; source: https://davidamitchell.github.io/Research/research/2026-04-27-pap-dynamic-policy-profiling-proportionality.html; https://davidamitchell.github.io/Research/research/2026-04-27-pdp-universal-policy-synchronisation-integrity.html] This also stays consistent with the adjacent PAP and PDP items because those items govern what controls exist and which policy is current, while this item governs when transient context is trying to avoid those controls at runtime.

### §5 Depth and Breadth Expansion

- [inference; source: https://davidamitchell.github.io/Research/research/2026-03-15-neurological-context-management.html; https://pmc.ncbi.nlm.nih.gov/articles/PMC2782645/] Technically, the cleanest architecture is to keep invariant summaries in a non-evictable context tier and compute anomaly features from deltas between those summaries and requested actions, because this mirrors the prior-plus-surprise logic rather than naive prompt concatenation.
- [inference; source: https://csf.tools/reference/nist-sp-800-53/r5/si/si-4/; https://csf.tools/reference/nist-sp-800-53/r5/au/au-6/] From a control and audit perspective, the signal must be explainable enough to support correlation across monitoring repositories, central review, and stepped-up analysis when risk changes.
- [inference; source: https://davidamitchell.github.io/Research/research/2026-04-27-pap-dynamic-policy-profiling-proportionality.html] Proportional routing matters economically because a design that sends every low-probability prompt to the highest-friction review path recreates the uniform-control failure that the PAP item argues against.
- [inference; source: https://thecynefin.co/effective-decision-making-support-tool/; https://davidamitchell.github.io/Research/research/2026-03-10-formal-spec-intent-alignment-agentic-coding.html] Behaviourally, users and attackers both have an incentive to down-classify work as routine or Clear in order to get speed, so complexity declaration itself must be treated as an input that can be gamed.
- [inference; source: https://davidamitchell.github.io/Research/research/2026-04-27-pdp-universal-policy-synchronisation-integrity.html; https://davidamitchell.github.io/Research/research/2026-04-26-ai-agent-identity-access-management-enterprise.html] Governance-wise, the anomaly object becomes materially more useful when it carries policy-version and machine-identity context, because the PDP can then distinguish a suspicious task from one executed under stale policy or under the wrong workload identity.

### §6 Synthesis

*(This section seeds the Findings below.)*

**Executive summary:**

- [inference; source: https://pmc.ncbi.nlm.nih.gov/articles/PMC2782645/; https://davidamitchell.github.io/Research/research/2026-03-15-context-layers-aligned-decisions-synthesis.html; https://docs.oasis-open.org/xacml/3.0/xacml-3.0-core-spec-os-en.html] The PIP should detect invariant suppression by computing a Bayesian-style surprise score over the joint mismatch between permanent invariant metadata and transient task signals, then surface a typed anomaly object to the PDP rather than trying to resolve the policy conflict itself.
- [inference; source: https://genai.owasp.org/llmrisk/llm01-prompt-injection/; https://davidamitchell.github.io/Research/research/2026-03-15-prompt-injection-threat-landscape.html] The highest-value distinction is between passive suppression, where framing and requested actions agree that invariants are not in play, and active or adversarial suppression, where the requested actions would touch invariant-bearing resources despite framing that says otherwise.
- [inference; source: https://thecynefin.co/effective-decision-making-support-tool/; https://davidamitchell.github.io/Research/research/2026-04-27-pap-dynamic-policy-profiling-proportionality.html] Cynefin task-complexity declarations should be used as prior-adjustment signals, because high-invariant assets declaring Clear routine work while requesting broad data access or state-changing tools are lower-probability combinations than comparable tasks declared as Complicated or Complex.
- [inference; source: https://csf.tools/reference/nist-sp-800-53/r5/si/si-4/; https://csf.tools/reference/nist-sp-800-53/r5/au/au-6/] The PIP output should include `signal_type`, `confidence_score`, `surprise_score`, implicated invariants, contradictory observations, provenance, and a recommended routing path so that monitoring, audit review, and PDP remediation remain explainable and risk-proportionate.

**Key findings:**

1. **High confidence.** [inference; source: https://docs.oasis-open.org/xacml/3.0/xacml-3.0-core-spec-os-en.html; https://davidamitchell.github.io/Research/research/2026-03-15-context-layers-aligned-decisions-synthesis.html] The PIP is the correct runtime detection surface because it already synthesises the attribute values that connect Layer 3 Asset Metadata to Layer 8 Task Intent before the PDP evaluates policy.
2. **High confidence.** [inference; source: https://davidamitchell.github.io/Research/research/2026-03-10-formal-spec-intent-alignment-agentic-coding.html; https://davidamitchell.github.io/Research/research/2026-04-26-access-control-amplification-agentic-operations.html] Invariant-shadowing should be typed into passive, active, and adversarial classes, because the operational response depends on whether the framing-to-action mismatch is absent, accidental, or linked to hostile context substitution.
3. **High confidence.** [inference; source: https://pmc.ncbi.nlm.nih.gov/articles/PMC2782645/; https://davidamitchell.github.io/Research/research/2026-03-15-neurological-context-management.html] Bayesian surprise is a better core scoring model than raw rule counting because the anomaly is defined by how much the observed task tuple shifts legitimacy beliefs for that invariant-bearing asset, not by rarity in the abstract.
4. **Medium confidence.** [inference; source: https://thecynefin.co/effective-decision-making-support-tool/; https://hbr.org/2007/11/a-leaders-framework-for-decision-making] Cynefin domain declarations should be treated as probabilistic context features, with Clear declarations lowering the expected probability of broad access or state change for high-invariant assets and Chaotic declarations increasing review pressure rather than relaxing control.
5. **High confidence.** [inference; source: https://genai.owasp.org/llmrisk/llm01-prompt-injection/; https://davidamitchell.github.io/Research/research/2026-03-15-prompt-injection-threat-landscape.html] Prompt injection should be modelled inside the PIP as hostile context substitution, and not merely as suspicious text, because the security-relevant event is the attempt to make transient input outrank registered invariant metadata.
6. **High confidence.** [inference; source: https://csf.tools/reference/nist-sp-800-53/r5/si/si-4/; https://csf.tools/reference/nist-sp-800-53/r5/au/au-6/] The PIP-to-PDP signal should be a typed and explainable anomaly object carrying score, confidence, implicated invariants, provenance, and recommended routing so that monitoring and audit review remain actionable.
7. **Medium confidence.** [inference; source: https://davidamitchell.github.io/Research/research/2026-04-27-pap-dynamic-policy-profiling-proportionality.html; https://davidamitchell.github.io/Research/research/2026-04-27-pdp-universal-policy-synchronisation-integrity.html; https://davidamitchell.github.io/Research/research/2026-04-26-ai-agent-identity-access-management-enterprise.html] The anomaly object becomes materially stronger when it also carries lifecycle policy-version and machine-identity context, because adjacent governance failures can otherwise masquerade as task-framing anomalies.

**Evidence map:**

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [inference] The PIP is the correct runtime detection surface because it already assembles the attributes used by the PDP to evaluate policy. | https://docs.oasis-open.org/xacml/3.0/xacml-3.0-core-spec-os-en.html ; https://davidamitchell.github.io/Research/research/2026-03-15-context-layers-aligned-decisions-synthesis.html | high | Ties XACML role definitions to the repository's Layer 3 to Layer 8 architecture. |
| [inference] Invariant-shadowing should be typed into passive, active, and adversarial classes because the remediation path depends on whether contradiction and hostile context are present. | https://davidamitchell.github.io/Research/research/2026-03-10-formal-spec-intent-alignment-agentic-coding.html ; https://davidamitchell.github.io/Research/research/2026-04-26-access-control-amplification-agentic-operations.html ; https://genai.owasp.org/llmrisk/llm01-prompt-injection/ | high | Distinguishes legitimate non-activation from risky mismatch and hostile substitution. |
| [inference] Bayesian surprise is the right scoring core because the anomaly is a belief shift about legitimacy conditioned on invariants, not mere rarity. | https://pmc.ncbi.nlm.nih.gov/articles/PMC2782645/ ; https://davidamitchell.github.io/Research/research/2026-03-15-neurological-context-management.html | high | Connects formal surprise to prior-weighted relevance filtering. |
| [inference] Cynefin declarations should change the prior over legitimate operations, with Clear routine framing making broad access or state change less probable for high-invariant assets. | https://thecynefin.co/effective-decision-making-support-tool/ ; https://hbr.org/2007/11/a-leaders-framework-for-decision-making ; https://davidamitchell.github.io/Research/research/2026-04-27-pap-dynamic-policy-profiling-proportionality.html | medium | Useful as a prior-adjustment feature, not sufficient alone. |
| [inference] Prompt injection should be modelled as hostile context substitution because it tries to make untrusted external content outrank registered invariant metadata and tool constraints. | https://genai.owasp.org/llmrisk/llm01-prompt-injection/ ; https://davidamitchell.github.io/Research/research/2026-03-15-prompt-injection-threat-landscape.html | high | Converts a text-security issue into a policy-routing issue. |
| [inference] The PIP signal should be typed, auditable, and explainable, carrying score, confidence, implicated invariants, provenance, and recommended route. | https://csf.tools/reference/nist-sp-800-53/r5/si/si-4/ ; https://csf.tools/reference/nist-sp-800-53/r5/au/au-6/ ; https://docs.oasis-open.org/xacml/3.0/xacml-3.0-core-spec-os-en.html | high | Directly grounded in monitoring, review, and role-separation requirements. |
| [inference] Policy-version and machine-identity context strengthen suppression detection by separating runtime framing anomalies from adjacent governance failures. | https://davidamitchell.github.io/Research/research/2026-04-27-pdp-universal-policy-synchronisation-integrity.html ; https://davidamitchell.github.io/Research/research/2026-04-26-ai-agent-identity-access-management-enterprise.html ; https://davidamitchell.github.io/Research/research/2026-04-27-pap-dynamic-policy-profiling-proportionality.html | medium | Cross-item synthesis across lifecycle integrity, identity, and proportional control depth. |

**Assumptions:**

- [assumption; source: https://davidamitchell.github.io/Research/research/2026-04-27-pap-dynamic-policy-profiling-proportionality.html] The PAP or asset-registration process produces enough invariant-class structure to seed priors for newly created assets. **Justification:** a surprise score needs a baseline, and new assets otherwise lack historical usage.
- [assumption; source: https://davidamitchell.github.io/Research/research/2026-04-26-ai-agent-identity-access-management-enterprise.html] Requested tools and data scopes are visible to the PIP before the PDP renders a final decision. **Justification:** active suppression cannot be detected if the PIP only sees the free-form prompt and not the planned operations.
- [assumption; source: https://thecynefin.co/effective-decision-making-support-tool/] The calling context provides either an explicit Cynefin-style task declaration or enough structured metadata for the platform to infer one. **Justification:** the Cynefin-by-invariant matrix cannot influence priors without a complexity signal.

**Analysis:**

- [inference; source: https://pmc.ncbi.nlm.nih.gov/articles/PMC2782645/; https://davidamitchell.github.io/Research/research/2026-03-15-neurological-context-management.html] The evidence weighs in favour of surprise-based scoring because both the formal theory of surprise and the neurological analogue emphasise belief shift against prior expectations, which matches the control problem more closely than simple keyword or rule triggers.
- [inference; source: https://genai.owasp.org/llmrisk/llm01-prompt-injection/; https://davidamitchell.github.io/Research/research/2026-03-15-prompt-injection-threat-landscape.html] OWASP and the prior prompt-injection item justify treating provenance and hostile override patterns as score multipliers, but they do not justify equating every suspicious string with active suppression, so action mismatch remains the decisive discriminator.
- [inference; source: https://thecynefin.co/effective-decision-making-support-tool/; https://hbr.org/2007/11/a-leaders-framework-for-decision-making] The Cynefin framework helps because it changes what "normal" looks like for the task, but it remains a contextual prior rather than direct proof, so its contribution is medium-confidence and subordinate to invariant-action contradiction.
- [inference; source: https://csf.tools/reference/nist-sp-800-53/r5/si/si-4/; https://csf.tools/reference/nist-sp-800-53/r5/au/au-6/] NIST monitoring controls tilt the design toward typed, explainable routing objects rather than hidden scores, because anomaly detection that cannot be reviewed, correlated, or reported cleanly would fail the stated monitoring purpose.
- [inference; source: https://davidamitchell.github.io/Research/research/2026-04-27-pap-dynamic-policy-profiling-proportionality.html; https://davidamitchell.github.io/Research/research/2026-04-27-pdp-universal-policy-synchronisation-integrity.html] Adjacent PBAC items sharpen the trade-off: low-risk assets need low-friction monitoring, while high-invariant assets need higher-confidence escalation paths, so the signal must remain typed and proportional rather than binary.

**Risks, gaps, uncertainties:**

- [inference; source: https://pmc.ncbi.nlm.nih.gov/articles/PMC2782645/] The surprise formula is well founded conceptually, but this item does not establish production calibration thresholds for specific invariant classes, so implementation still needs empirical tuning.
- [inference; source: https://thecynefin.co/effective-decision-making-support-tool/] Cynefin declarations are partly behavioural and can be gamed or misclassified, so they should influence priors but should not be treated as authoritative evidence on their own.
- [inference; source: https://genai.owasp.org/llmrisk/llm01-prompt-injection/] Prompt injection remains a partly unsolved prevention problem, so adversarial suppression detection will necessarily produce some false positives and false negatives.
- [inference; source: https://davidamitchell.github.io/Research/research/2026-04-26-ai-agent-identity-access-management-enterprise.html] If tool plans are assembled late or outside the PIP's visibility boundary, active suppression may only be partially detectable at the point this item targets.

**Open questions:**

- How should invariant-class priors be learned and refreshed without letting manipulated traffic poison the baseline?
- What is the minimum structured tool-plan representation the PIP must receive to detect active suppression before execution begins?
- How should policy-version drift and suppression anomalies be jointly handled when both appear in the same request path?
- Which invariant classes deserve hard fail-closed thresholds versus step-up review thresholds?
- How should multimodal prompt injection alter the provenance-risk term for assets that ingest images, audio, or Portable Document Format (PDF) documents?

### §7 Recursive Review

- [fact; source: https://pmc.ncbi.nlm.nih.gov/articles/PMC2782645/; https://thecynefin.co/effective-decision-making-support-tool/; https://genai.owasp.org/llmrisk/llm01-prompt-injection/; https://csf.tools/reference/nist-sp-800-53/r5/si/si-4/; https://csf.tools/reference/nist-sp-800-53/r5/au/au-6/] Every substantive claim in Sections 0 to 6 is either source-bound as fact, derived as an inference from cited sources, or declared as an assumption with justification.
- [fact; source: https://davidamitchell.github.io/Research/research/2026-03-15-context-layers-aligned-decisions-synthesis.html; https://davidamitchell.github.io/Research/research/2026-03-10-formal-spec-intent-alignment-agentic-coding.html; https://davidamitchell.github.io/Research/research/2026-03-15-prompt-injection-threat-landscape.html; https://davidamitchell.github.io/Research/research/2026-03-15-neurological-context-management.html] The synthesis integrates all required repository threads: context layering, intent mismatch, prompt injection, and prior-weighted relevance filtering.
- [inference; source: https://csf.tools/reference/nist-sp-800-53/r5/si/si-4/; https://csf.tools/reference/nist-sp-800-53/r5/au/au-6/] The remaining uncertainty is threshold calibration and operational implementation, not the core architectural conclusion that the PIP should emit a typed anomaly object rather than silently suppressing or directly resolving the conflict.

---

## Findings

*(Populated from §6 Synthesis above.)*

### Executive Summary

[inference; source: https://pmc.ncbi.nlm.nih.gov/articles/PMC2782645/; https://davidamitchell.github.io/Research/research/2026-03-15-context-layers-aligned-decisions-synthesis.html; https://docs.oasis-open.org/xacml/3.0/xacml-3.0-core-spec-os-en.html] The PIP should detect invariant suppression by computing a Bayesian-style surprise score over the mismatch between permanent invariant metadata and transient task signals, then surface a typed anomaly object to the PDP instead of trying to resolve the policy conflict itself. [inference; source: https://genai.owasp.org/llmrisk/llm01-prompt-injection/; https://davidamitchell.github.io/Research/research/2026-03-15-prompt-injection-threat-landscape.html] The decisive distinction is between passive suppression, where framing and requested actions agree that invariants are not in play, and active or adversarial suppression, where the requested actions would touch invariant-bearing resources despite framing that says otherwise. [inference; source: https://thecynefin.co/effective-decision-making-support-tool/; https://davidamitchell.github.io/Research/research/2026-04-27-pap-dynamic-policy-profiling-proportionality.html] Cynefin task-complexity declarations should modify the prior because high-invariant assets declaring Clear routine work while requesting broad access or state-changing tools are lower-probability combinations than comparable tasks declared as Complicated or Complex. [inference; source: https://csf.tools/reference/nist-sp-800-53/r5/si/si-4/; https://csf.tools/reference/nist-sp-800-53/r5/au/au-6/] The PIP output should therefore carry `signal_type`, `confidence_score`, `surprise_score`, implicated invariants, contradictory observations, provenance, and a recommended routing path so that monitoring, audit review, and remediation remain explainable and proportionate.

### Key Findings

1. **High confidence.** [inference; source: https://docs.oasis-open.org/xacml/3.0/xacml-3.0-core-spec-os-en.html; https://davidamitchell.github.io/Research/research/2026-03-15-context-layers-aligned-decisions-synthesis.html] The PIP is the correct runtime detection surface because it already synthesises the attribute values that connect Layer 3 Asset Metadata to Layer 8 Task Intent before the PDP evaluates policy.
2. **High confidence.** [inference; source: https://davidamitchell.github.io/Research/research/2026-03-10-formal-spec-intent-alignment-agentic-coding.html; https://davidamitchell.github.io/Research/research/2026-04-26-access-control-amplification-agentic-operations.html] Invariant-shadowing should be typed into passive, active, and adversarial classes, because the operational response depends on whether the framing-to-action mismatch is absent, accidental, or linked to hostile context substitution.
3. **High confidence.** [inference; source: https://pmc.ncbi.nlm.nih.gov/articles/PMC2782645/; https://davidamitchell.github.io/Research/research/2026-03-15-neurological-context-management.html] Bayesian surprise is a better core scoring model than raw rule counting because the anomaly is defined by how much the observed task tuple shifts legitimacy beliefs for that invariant-bearing asset, not by rarity in the abstract.
4. **Medium confidence.** [inference; source: https://thecynefin.co/effective-decision-making-support-tool/; https://hbr.org/2007/11/a-leaders-framework-for-decision-making] Cynefin domain declarations should be treated as probabilistic context features, with Clear declarations lowering the expected probability of broad access or state change for high-invariant assets and Chaotic declarations increasing review pressure rather than relaxing control.
5. **High confidence.** [inference; source: https://genai.owasp.org/llmrisk/llm01-prompt-injection/; https://davidamitchell.github.io/Research/research/2026-03-15-prompt-injection-threat-landscape.html] Prompt injection should be modelled inside the PIP as hostile context substitution, and not merely as suspicious text, because the security-relevant event is the attempt to make transient input outrank registered invariant metadata.
6. **High confidence.** [inference; source: https://csf.tools/reference/nist-sp-800-53/r5/si/si-4/; https://csf.tools/reference/nist-sp-800-53/r5/au/au-6/] The PIP-to-PDP signal should be a typed and explainable anomaly object carrying score, confidence, implicated invariants, provenance, and recommended routing so that monitoring and audit review remain actionable.
7. **Medium confidence.** [inference; source: https://davidamitchell.github.io/Research/research/2026-04-27-pap-dynamic-policy-profiling-proportionality.html; https://davidamitchell.github.io/Research/research/2026-04-27-pdp-universal-policy-synchronisation-integrity.html; https://davidamitchell.github.io/Research/research/2026-04-26-ai-agent-identity-access-management-enterprise.html] The anomaly object becomes materially stronger when it also carries lifecycle policy-version and machine-identity context, because adjacent governance failures can otherwise masquerade as task-framing anomalies.

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [inference] The PIP is the correct runtime detection surface because it already assembles the attributes used by the PDP to evaluate policy. | https://docs.oasis-open.org/xacml/3.0/xacml-3.0-core-spec-os-en.html ; https://davidamitchell.github.io/Research/research/2026-03-15-context-layers-aligned-decisions-synthesis.html | high | Ties XACML role definitions to the repository's Layer 3 to Layer 8 architecture. |
| [inference] Invariant-shadowing should be typed into passive, active, and adversarial classes because the remediation path depends on whether contradiction and hostile context are present. | https://davidamitchell.github.io/Research/research/2026-03-10-formal-spec-intent-alignment-agentic-coding.html ; https://davidamitchell.github.io/Research/research/2026-04-26-access-control-amplification-agentic-operations.html ; https://genai.owasp.org/llmrisk/llm01-prompt-injection/ | high | Distinguishes legitimate non-activation from risky mismatch and hostile substitution. |
| [inference] Bayesian surprise is the right scoring core because the anomaly is a belief shift about legitimacy conditioned on invariants, not mere rarity. | https://pmc.ncbi.nlm.nih.gov/articles/PMC2782645/ ; https://davidamitchell.github.io/Research/research/2026-03-15-neurological-context-management.html | high | Connects formal surprise to prior-weighted relevance filtering. |
| [inference] Cynefin declarations should change the prior over legitimate operations, with Clear routine framing making broad access or state change less probable for high-invariant assets. | https://thecynefin.co/effective-decision-making-support-tool/ ; https://hbr.org/2007/11/a-leaders-framework-for-decision-making ; https://davidamitchell.github.io/Research/research/2026-04-27-pap-dynamic-policy-profiling-proportionality.html | medium | Useful as a prior-adjustment feature, not sufficient alone. |
| [inference] Prompt injection should be modelled as hostile context substitution because it tries to make untrusted external content outrank registered invariant metadata and tool constraints. | https://genai.owasp.org/llmrisk/llm01-prompt-injection/ ; https://davidamitchell.github.io/Research/research/2026-03-15-prompt-injection-threat-landscape.html | high | Converts a text-security issue into a policy-routing issue. |
| [inference] The PIP signal should be typed, auditable, and explainable, carrying score, confidence, implicated invariants, provenance, and recommended route. | https://csf.tools/reference/nist-sp-800-53/r5/si/si-4/ ; https://csf.tools/reference/nist-sp-800-53/r5/au/au-6/ ; https://docs.oasis-open.org/xacml/3.0/xacml-3.0-core-spec-os-en.html | high | Directly grounded in monitoring, review, and role-separation requirements. |
| [inference] Policy-version and machine-identity context strengthen suppression detection by separating runtime framing anomalies from adjacent governance failures. | https://davidamitchell.github.io/Research/research/2026-04-27-pdp-universal-policy-synchronisation-integrity.html ; https://davidamitchell.github.io/Research/research/2026-04-26-ai-agent-identity-access-management-enterprise.html ; https://davidamitchell.github.io/Research/research/2026-04-27-pap-dynamic-policy-profiling-proportionality.html | medium | Cross-item synthesis across lifecycle integrity, identity, and proportional control depth. |

### Assumptions

- [assumption; source: https://davidamitchell.github.io/Research/research/2026-04-27-pap-dynamic-policy-profiling-proportionality.html] The PAP or asset-registration process produces enough invariant-class structure to seed priors for newly created assets. **Justification:** a surprise score needs a baseline, and new assets otherwise lack historical usage.
- [assumption; source: https://davidamitchell.github.io/Research/research/2026-04-26-ai-agent-identity-access-management-enterprise.html] Requested tools and data scopes are visible to the PIP before the PDP renders a final decision. **Justification:** active suppression cannot be detected if the PIP only sees the free-form prompt and not the planned operations.
- [assumption; source: https://thecynefin.co/effective-decision-making-support-tool/] The calling context provides either an explicit Cynefin-style task declaration or enough structured metadata for the platform to infer one. **Justification:** the Cynefin-by-invariant matrix cannot influence priors without a complexity signal.

### Analysis

- [inference; source: https://pmc.ncbi.nlm.nih.gov/articles/PMC2782645/; https://davidamitchell.github.io/Research/research/2026-03-15-neurological-context-management.html] The evidence weighs in favour of surprise-based scoring because both the formal theory of surprise and the neurological analogue emphasise belief shift against prior expectations, which matches the control problem more closely than simple keyword or rule triggers.
- [inference; source: https://genai.owasp.org/llmrisk/llm01-prompt-injection/; https://davidamitchell.github.io/Research/research/2026-03-15-prompt-injection-threat-landscape.html] OWASP and the prior prompt-injection item justify treating provenance and hostile override patterns as score multipliers, but they do not justify equating every suspicious string with active suppression, so action mismatch remains the decisive discriminator.
- [inference; source: https://thecynefin.co/effective-decision-making-support-tool/; https://hbr.org/2007/11/a-leaders-framework-for-decision-making] The Cynefin framework helps because it changes what "normal" looks like for the task, but it remains a contextual prior rather than direct proof, so its contribution is medium-confidence and subordinate to invariant-action contradiction.
- [inference; source: https://csf.tools/reference/nist-sp-800-53/r5/si/si-4/; https://csf.tools/reference/nist-sp-800-53/r5/au/au-6/] NIST monitoring controls tilt the design toward typed, explainable routing objects rather than hidden scores, because anomaly detection that cannot be reviewed, correlated, or reported cleanly would fail the stated monitoring purpose.
- [inference; source: https://davidamitchell.github.io/Research/research/2026-04-27-pap-dynamic-policy-profiling-proportionality.html; https://davidamitchell.github.io/Research/research/2026-04-27-pdp-universal-policy-synchronisation-integrity.html] Adjacent PBAC items sharpen the trade-off: low-risk assets need low-friction monitoring, while high-invariant assets need higher-confidence escalation paths, so the signal must remain typed and proportional rather than binary.

### Risks, Gaps, and Uncertainties

- [inference; source: https://pmc.ncbi.nlm.nih.gov/articles/PMC2782645/] The surprise formula is well founded conceptually, but this item does not establish production calibration thresholds for specific invariant classes, so implementation still needs empirical tuning.
- [inference; source: https://thecynefin.co/effective-decision-making-support-tool/] Cynefin declarations are partly behavioural and can be gamed or misclassified, so they should influence priors but should not be treated as authoritative evidence on their own.
- [inference; source: https://genai.owasp.org/llmrisk/llm01-prompt-injection/] Prompt injection remains a partly unsolved prevention problem, so adversarial suppression detection will necessarily produce some false positives and false negatives.
- [inference; source: https://davidamitchell.github.io/Research/research/2026-04-26-ai-agent-identity-access-management-enterprise.html] If tool plans are assembled late or outside the PIP's visibility boundary, active suppression may only be partially detectable at the point this item targets.

### Open Questions

- How should invariant-class priors be learned and refreshed without letting manipulated traffic poison the baseline?
- What is the minimum structured tool-plan representation the PIP must receive to detect active suppression before execution begins?
- How should policy-version drift and suppression anomalies be jointly handled when both appear in the same request path?
- Which invariant classes deserve hard fail-closed thresholds versus step-up review thresholds?
- How should multimodal prompt injection alter the provenance-risk term for assets that ingest images, audio, or Portable Document Format (PDF) documents?

---

## Output

*(Fill in when completing - what was produced as a result of this research?)*

- Type: knowledge
- Description: A runtime anomaly-detection specification for the Policy Information Point (PIP), including a passive-active-adversarial suppression taxonomy, a Bayesian-style surprise score, a Cynefin-by-invariant interpretation rule, and a typed PIP-to-PDP signal object with a worked example.
- Links:
- https://genai.owasp.org/llmrisk/llm01-prompt-injection/
- https://csf.tools/reference/nist-sp-800-53/r5/si/si-4/
- https://pmc.ncbi.nlm.nih.gov/articles/PMC2782645/
