---
review_count: 2
title: "Are Multi-Step Large Language Model-Based Systems Inherently Less Explainable Than Equivalently Scoped Deterministic Software Systems?"
added: 2026-05-18T19:40:00+00:00
status: completed
priority: high
blocks:
  - 2026-05-18-agentic-production-tradeoffs
tags: [agentic-ai, llm, governance, evaluation]
themes: [agentic-ai, ai-architecture, governance-policy, mlops-deployment, explainability-transparency]
started: 2026-05-19T00:54:38+00:00
completed: 2026-05-19T01:14:38+00:00
output: [knowledge]
cites:
  - 2026-04-26-ai-lowcode-observability-telemetry-governance
  - 2026-04-30-explainable-ai-xai-regulation-governance
  - 2026-05-09-governance-policy-determinism-vs-stochastic-llm
  - 2026-05-09-hybrid-architecture-probabilistic-llm-deterministic-governance
  - 2026-05-09-llm-determinism-limits-temperature-zero
related:
  - 2026-04-26-systems-capability-debt-agentic-ai-risk-synthesis
superseded_by: ~
supersedes: ~
item_type: synthesis
confidence: medium
versions: []
---

# Are Multi-Step Large Language Model-Based Systems Inherently Less Explainable Than Equivalently Scoped Deterministic Software Systems?

## Research Question

Are multi-step Large Language Model (LLM)-based systems inherently less explainable than equivalently scoped deterministic software systems, or does production-scale distributed-system complexity make both classes practically equally opaque?

## Scope

**In scope:**
- A formal comparison of explainability across local explainability, explaining one concrete output, global explainability, explaining overall system behaviour, and contrastive explainability, explaining why one outcome occurred instead of another
- Whether deterministic distributed software loses enough practical transparency at production scale to approach the opacity of LLM-based systems
- Whether any explainability gap is structural, present before scaling, or mainly contingent on tooling, observability, and system design
- Governance and audit implications where explainability is needed for reconstruction, contestability, and accountability

**Out of scope:**
- Technique-by-technique implementation guidance for SHapley Additive exPlanations (SHAP), Local Interpretable Model-agnostic Explanations (LIME), attention visualization, or internal-circuit tracing tools
- Product recommendations for improving explainability in either class

**Constraints:** This is a synthesis item. The question must be answered as a structural comparison, not as a generic statement that all complex systems are hard to understand.

## Context

- Explainability in the reviewed literature is not one property, because formal sources distinguish meaningful explanation, explanation accuracy, knowledge limits, transparency, post hoc explanation, and contrastive usefulness. [fact; source: https://arxiv.org/abs/1702.08608; https://arxiv.org/abs/1606.03490; https://arxiv.org/abs/1711.00399; https://www.nist.gov/publications/four-principles-explainable-artificial-intelligence]
- Present-day LLM services remain only partially reproducible even under stabilization controls, so one part of the comparison is whether that residual variation creates a structural explainability disadvantage. [fact; source: https://learn.microsoft.com/en-us/azure/ai-foundry/openai/how-to/reproducible-output; https://arxiv.org/abs/2408.04667; https://arxiv.org/abs/2502.20747]
- Large deterministic distributed systems also require observability, monitoring, and post hoc reconstruction because direct inspection of the whole system becomes impractical as dependencies, state, and runtime interactions expand. [inference; source: https://doi.org/10.1007/s11229-008-9435-2; https://sre.google/sre-book/monitoring-distributed-systems/; https://www.routledge.com/Drift-into-Failure/Dekker/p/book/9781409422211]

## Approach

1. Define explainability using formal literature that distinguishes transparency, post hoc explanation, and contrastive explanation.
2. Test whether multi-step LLM-based systems have a structural local explainability disadvantage before scale is introduced.
3. Test how far deterministic software loses explainability once it becomes a production-scale distributed system.
4. Compare where the two classes converge, especially in global and post hoc explainability.
5. Produce a verdict about whether the gap is erased, narrowed, or persistent across dimensions.

## Sources

- [x] [Doshi-Velez and Kim (2017) Towards A Rigorous Science of Interpretable Machine Learning](https://arxiv.org/abs/1702.08608)
- [x] [Lipton (2017) The Mythos of Model Interpretability](https://arxiv.org/abs/1606.03490)
- [x] [Wachter et al. (2018) Counterfactual Explanations without Opening the Black Box](https://arxiv.org/abs/1711.00399)
- [x] [Phillips et al. (2021) Four Principles of Explainable Artificial Intelligence](https://www.nist.gov/publications/four-principles-explainable-artificial-intelligence)
- [x] [Humphreys (2009) The philosophical novelty of computer simulation methods](https://doi.org/10.1007/s11229-008-9435-2)
- [x] [Dekker (2011) Drift into Failure](https://www.routledge.com/Drift-into-Failure/Dekker/p/book/9781409422211)
- [x] [Microsoft Learn How to generate reproducible output with Azure OpenAI](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/how-to/reproducible-output)
- [x] [Atil et al. (2025) Non-Determinism of "Deterministic" LLM Settings](https://arxiv.org/abs/2408.04667)
- [x] [Denisov-Blanch et al. (2025) Measuring Determinism in Large Language Models for Software Code Review](https://arxiv.org/abs/2502.20747)
- [x] [Google Site Reliability Engineering (SRE) Book Monitoring Distributed Systems](https://sre.google/sre-book/monitoring-distributed-systems/)
- [x] [What observability and telemetry model is required to govern Artificial Intelligence and low-code systems at scale?](https://davidamitchell.github.io/Research/research/2026-04-26-ai-lowcode-observability-telemetry-governance.html)
- [x] [Explainable Artificial Intelligence (XAI): current research state, leading institutions, and regulatory intersection in heavily regulated industries](https://davidamitchell.github.io/Research/research/2026-04-30-explainable-ai-xai-regulation-governance.html)
- [x] [Governance Policy Application: Deterministic Requirements vs Stochastic Large Language Model Elements](https://davidamitchell.github.io/Research/research/2026-05-09-governance-policy-determinism-vs-stochastic-llm.html)
- [x] [Hybrid Architecture Design: Probabilistic Large Language Models for Interpretation, Deterministic Layers for Governance Enforcement](https://davidamitchell.github.io/Research/research/2026-05-09-hybrid-architecture-probabilistic-llm-deterministic-governance.html)
- [x] [Practical Limits of Large Language Model Determinism: Temperature Zero, Fixed Seeds, and Constrained Prompts](https://davidamitchell.github.io/Research/research/2026-05-09-llm-determinism-limits-temperature-zero.html)

## Related

- [Explainable Artificial Intelligence (XAI): current research state, leading institutions, and regulatory intersection in heavily regulated industries](https://davidamitchell.github.io/Research/research/2026-04-30-explainable-ai-xai-regulation-governance.html)
- [Governance Policy Application: Deterministic Requirements vs Stochastic Large Language Model Elements](https://davidamitchell.github.io/Research/research/2026-05-09-governance-policy-determinism-vs-stochastic-llm.html)
- [Hybrid Architecture Design: Probabilistic Large Language Models for Interpretation, Deterministic Layers for Governance Enforcement](https://davidamitchell.github.io/Research/research/2026-05-09-hybrid-architecture-probabilistic-llm-deterministic-governance.html)
- [Practical Limits of Large Language Model Determinism: Temperature Zero, Fixed Seeds, and Constrained Prompts](https://davidamitchell.github.io/Research/research/2026-05-09-llm-determinism-limits-temperature-zero.html)
- [What observability and telemetry model is required to govern Artificial Intelligence and low-code systems at scale?](https://davidamitchell.github.io/Research/research/2026-04-26-ai-lowcode-observability-telemetry-governance.html)

---

## Research Skill Output

*(Full output from running the research skill, retained verbatim in the completed item. Sections 0 to 5 are the investigation, and section 6 seeds the Findings section below.)*

### §0 Initialise

- Question: are multi-step LLM-based systems inherently less explainable than equivalently scoped deterministic software systems, or does production-scale distributed-system complexity make both classes practically equally opaque?
- Scope: local, global, and contrastive explainability; stochastic LLM behavior; deterministic distributed-software opacity; governance and audit implications.
- Constraints: primary and quasi-primary formal sources first, then production documentation and prior completed repository items for cross-item synthesis.
- Output: knowledge.
- [fact; source: https://davidamitchell.github.io/Research/research/2026-04-30-explainable-ai-xai-regulation-governance.html; https://davidamitchell.github.io/Research/research/2026-05-09-governance-policy-determinism-vs-stochastic-llm.html; https://davidamitchell.github.io/Research/research/2026-05-09-hybrid-architecture-probabilistic-llm-deterministic-governance.html; https://davidamitchell.github.io/Research/research/2026-05-09-llm-determinism-limits-temperature-zero.html] Prior completed items in this repository already showed that regulation treats explainability largely as a governance capability and that deterministic control layers remain useful around probabilistic models, so this item tests whether distributed deterministic software is ultimately just as opaque once scale is introduced.

### §1 Question Decomposition

- **Root question:** does large-scale deterministic software lose enough explainability to erase the structural explainability gap between it and multi-step LLM-based systems?
- **A. Formal definition**
  - A1. What do the formal explainability sources say explainability consists of?
  - A2. Which dimensions are relevant for a cross-class comparison?
- **B. LLM-based systems at small scope**
  - B1. Do current LLM systems remain only partially reproducible under controlled settings?
  - B2. Does that variability weaken local explanation and exact replay before scale is considered?
- **C. Deterministic software at production scale**
  - C1. What makes large deterministic distributed systems hard to explain globally?
  - C2. Does observability solve that opacity or only manage it after the fact?
- **D. Contrastive explanation**
  - D1. Can both classes provide useful counterfactual or outcome-level explanations without full internal transparency?
  - D2. Does that narrow the explainability gap more for one class than the other?
- **E. Verdict**
  - E1. Which explainability dimensions converge at scale?
  - E2. Which dimensions remain structurally asymmetric?

### §2 Investigation

#### A. Formal explainability is multi-dimensional rather than unitary

- [fact; source: https://arxiv.org/abs/1702.08608] Doshi-Velez and Kim say there is little consensus about what interpretable machine learning is and how it should be measured, and they frame interpretability as a property that requires rigorous evaluation rather than intuitive labeling.
- [fact; source: https://arxiv.org/abs/1606.03490] Lipton says motivations for interpretability are diverse and sometimes discordant, and he distinguishes transparency to humans from post hoc explanation as competing notions rather than one single property.
- [fact; source: https://www.nist.gov/publications/four-principles-explainable-artificial-intelligence] The National Institute of Standards and Technology (NIST) defines explainable Artificial Intelligence (AI) through explanation, meaningful explanation, explanation accuracy, and knowledge limits.
- [fact; source: https://arxiv.org/abs/1711.00399] Wachter et al. argue that useful explanations for automated decisions can be contrastive and action-guiding, because they can tell an affected person what would need to change to obtain a different outcome without exposing the whole internal logic.
- [inference; source: https://arxiv.org/abs/1702.08608; https://arxiv.org/abs/1606.03490; https://arxiv.org/abs/1711.00399; https://www.nist.gov/publications/four-principles-explainable-artificial-intelligence] The relevant comparison for this item is therefore not a single explainability score but a structured comparison across local explanation, global explanation, and contrastive explanation.

#### B. Multi-step LLM-based systems have a structural local explainability disadvantage before production scale is introduced

- [fact; source: https://learn.microsoft.com/en-us/azure/ai-foundry/openai/how-to/reproducible-output] Microsoft says identical Azure OpenAI calls are nondeterministic by default and that determinism is still not guaranteed even when the `seed` parameter and `system_fingerprint` are the same.
- [fact; source: https://arxiv.org/abs/2408.04667] Atil et al. report that five LLMs configured to be deterministic still showed accuracy variation up to 15 percent across natural reruns and did not consistently reproduce identical output strings.
- [fact; source: https://arxiv.org/abs/2502.20747] Denisov-Blanch et al. found response variation across repeated temperature-zero code-review prompts in every model family they tested.
- [fact; source: https://arxiv.org/abs/1606.03490; https://www.nist.gov/publications/four-principles-explainable-artificial-intelligence] Lipton and NIST both treat post hoc explanation as distinct from transparent internal process inspection, which means an intelligible narrative is not the same thing as a faithful replay of how the model arrived at that output.
- [inference; source: https://learn.microsoft.com/en-us/azure/ai-foundry/openai/how-to/reproducible-output; https://arxiv.org/abs/2408.04667; https://arxiv.org/abs/2502.20747; https://arxiv.org/abs/1606.03490; https://www.nist.gov/publications/four-principles-explainable-artificial-intelligence] Multi-step LLM-based systems therefore carry a structural local explainability disadvantage even at modest scope, because exact replay of one decision path is weak and the available explanation surface is usually post hoc rather than direct internal transparency.

#### C. Deterministic software retains replayable steps more readily than LLM-based systems, but it loses global transparency as scale grows

- [fact; source: https://doi.org/10.1007/s11229-008-9435-2] Humphreys argues that computation introduces epistemological novelty because a cognitive agent cannot know all epistemically relevant elements of a complex computational process directly.
- [fact; source: https://sre.google/sre-book/monitoring-distributed-systems/] Google Site Reliability Engineering says monitoring a complex application is itself a significant engineering endeavor, that teams prefer simpler alerting with stronger post hoc analysis, and that they have only limited success with complex dependency hierarchies.
- [fact; source: https://sre.google/sre-book/monitoring-distributed-systems/] The same Google Site Reliability Engineering source says white-box monitoring is essential for debugging because engineers otherwise cannot distinguish a slow dependency from a network or integration problem.
- [fact; source: https://www.routledge.com/Drift-into-Failure/Dekker/p/book/9781409422211] The publisher summary of Dekker's book describes complex-system failure as drift produced by many locally reasonable decisions in dynamic environments rather than by one isolated broken component.
- [inference; source: https://doi.org/10.1007/s11229-008-9435-2; https://sre.google/sre-book/monitoring-distributed-systems/; https://www.routledge.com/Drift-into-Failure/Dekker/p/book/9781409422211] Large deterministic distributed systems therefore remain easier to replay at individual component and rule boundaries than LLM-based systems, but they are not globally transparent in practice because investigators still depend on logs, traces, and post hoc reconstruction once the dependency graph becomes large.

#### D. Contrastive explanation narrows the gap more than local step-by-step explanation

- [fact; source: https://arxiv.org/abs/1711.00399] Wachter et al. say explanations can support understanding, contesting a decision, and identifying what would need to change for a different future outcome without opening the black box.
- [fact; source: https://www.nist.gov/publications/four-principles-explainable-artificial-intelligence] NIST's meaningful-explanation and knowledge-limits principles also imply that a useful explanation can be audience-fit and bounded rather than a complete internal causal dump.
- [inference; source: https://arxiv.org/abs/1711.00399; https://www.nist.gov/publications/four-principles-explainable-artificial-intelligence] Wachter's counterfactual framework and NIST's audience-fit explanation principles support a narrower claim: useful outcome-level explanation does not always require full internal transparency.
- [inference; source: https://arxiv.org/abs/1711.00399; https://www.nist.gov/publications/four-principles-explainable-artificial-intelligence; https://arxiv.org/abs/1606.03490] Contrastive explanation therefore matters most as a bounded explanation surface for contesting or understanding outcomes, not as proof that a system is fully transparent.

#### E. Prior completed items sharpen the practical comparison

- [fact; source: https://davidamitchell.github.io/Research/research/2026-04-30-explainable-ai-xai-regulation-governance.html] The completed XAI item in this repository concluded that regulated explainability is usually implemented through governance artefacts, documentation, logging, and accountability rather than through any single explainability technique.
- [fact; source: https://davidamitchell.github.io/Research/research/2026-05-09-governance-policy-determinism-vs-stochastic-llm.html; https://davidamitchell.github.io/Research/research/2026-05-09-hybrid-architecture-probabilistic-llm-deterministic-governance.html] The completed governance and hybrid-architecture items concluded that deterministic authority is most defensible at the final control surface while probabilistic models remain upstream.
- [fact; source: https://davidamitchell.github.io/Research/research/2026-05-09-llm-determinism-limits-temperature-zero.html] The completed determinism item assembled vendor guidance and repeated-run evidence showing that current LLM systems do not become fully replayable under fixed seeds and constrained settings.
- [inference; source: https://davidamitchell.github.io/Research/research/2026-04-30-explainable-ai-xai-regulation-governance.html; https://davidamitchell.github.io/Research/research/2026-05-09-governance-policy-determinism-vs-stochastic-llm.html; https://davidamitchell.github.io/Research/research/2026-05-09-hybrid-architecture-probabilistic-llm-deterministic-governance.html; https://davidamitchell.github.io/Research/research/2026-05-09-llm-determinism-limits-temperature-zero.html; https://sre.google/sre-book/monitoring-distributed-systems/] Those items make the practical comparison clearer: both classes rely on governance and observability artefacts at scale, but deterministic systems still keep a stronger claim to local replayability wherever explicit rules and stable dependencies exist.

### §3 Reasoning

- [inference; source: https://arxiv.org/abs/1702.08608; https://arxiv.org/abs/1606.03490; https://arxiv.org/abs/1711.00399; https://www.nist.gov/publications/four-principles-explainable-artificial-intelligence] The comparison must be dimension-specific, because treating explainability as one scalar property would blur the difference between exact local replay, useful outcome explanation, and global system understanding.
- [inference; source: https://doi.org/10.1007/s11229-008-9435-2; https://sre.google/sre-book/monitoring-distributed-systems/] Production scale erodes global explainability for deterministic software because humans stop understanding the whole system directly and instead reason from observability artefacts and reconstruction work.
- [inference; source: https://learn.microsoft.com/en-us/azure/ai-foundry/openai/how-to/reproducible-output; https://arxiv.org/abs/2408.04667; https://arxiv.org/abs/2502.20747] Present-day LLM-based systems still add one more explainability burden, because even tightly controlled reruns can diverge before distributed-system complexity is introduced.
- [inference; source: https://arxiv.org/abs/1711.00399; https://www.nist.gov/publications/four-principles-explainable-artificial-intelligence] Contrastive and audience-fit explanations show that some explanation tasks can be satisfied without revealing every internal operation.

### §4 Consistency Check

- [inference; source: https://doi.org/10.1007/s11229-008-9435-2; https://sre.google/sre-book/monitoring-distributed-systems/] No reviewed source supports the claim that large deterministic distributed systems remain fully transparent once production-scale complexity is reached.
- [inference; source: https://learn.microsoft.com/en-us/azure/ai-foundry/openai/how-to/reproducible-output; https://arxiv.org/abs/2408.04667; https://arxiv.org/abs/2502.20747] No reviewed source supports the stronger rival claim that present-day LLM systems can be stabilized enough to erase their local replay and local explanation deficit.
- [inference; source: https://arxiv.org/abs/1711.00399; https://www.nist.gov/publications/four-principles-explainable-artificial-intelligence] Wachter's contrastive account does not contradict the opacity findings, because it offers bounded useful explanation without claiming complete internal transparency.
- [inference; source: https://davidamitchell.github.io/Research/research/2026-04-30-explainable-ai-xai-regulation-governance.html; https://davidamitchell.github.io/Research/research/2026-05-09-governance-policy-determinism-vs-stochastic-llm.html; https://davidamitchell.github.io/Research/research/2026-05-09-hybrid-architecture-probabilistic-llm-deterministic-governance.html; https://sre.google/sre-book/monitoring-distributed-systems/] The repository's prior governance conclusions remain consistent with the external evidence, because the decisive explanation surface for consequential systems is often the log, rule, trace, and review boundary rather than the full internal mechanism.

### §5 Depth and Breadth Expansion

- [inference; source: https://learn.microsoft.com/en-us/azure/ai-foundry/openai/how-to/reproducible-output; https://arxiv.org/abs/2408.04667; https://arxiv.org/abs/2502.20747; https://sre.google/sre-book/monitoring-distributed-systems/] **Technical lens:** deterministic distributed software and LLM-based systems both become operationally opaque, but LLM-based systems add residual run-to-run variation on top of the ordinary observability burden.
- [inference; source: https://www.nist.gov/publications/four-principles-explainable-artificial-intelligence; https://arxiv.org/abs/1711.00399; https://davidamitchell.github.io/Research/research/2026-04-30-explainable-ai-xai-regulation-governance.html] **Regulatory lens:** the most decision-useful explanation for governance often concerns contestability, justification, and evidence quality rather than a perfect disclosure of every hidden computation.
- [inference; source: https://sre.google/sre-book/monitoring-distributed-systems/; https://www.routledge.com/Drift-into-Failure/Dekker/p/book/9781409422211] **Behavioural lens:** deterministic systems create a false sense of automatic understandability, but production investigation still depends on disciplined monitoring, triage, and reconstruction.
- [inference; source: https://davidamitchell.github.io/Research/research/2026-05-09-governance-policy-determinism-vs-stochastic-llm.html; https://davidamitchell.github.io/Research/research/2026-05-09-hybrid-architecture-probabilistic-llm-deterministic-governance.html; https://sre.google/sre-book/monitoring-distributed-systems/] **Organisational lens:** the most durable explainability advantage comes from explicit control boundaries, versioned rules, and well-instrumented evidence trails, not from assuming one architecture class is inherently self-explaining.

### §6 Synthesis

**Executive summary:**

Multi-step Large Language Model-based systems are not equally explainable to equivalently scoped deterministic software systems, because they add model-internal opacity and residual run-to-run variation before production-scale complexity is even considered. [inference; source: https://arxiv.org/abs/1606.03490; https://learn.microsoft.com/en-us/azure/ai-foundry/openai/how-to/reproducible-output; https://arxiv.org/abs/2408.04667; https://arxiv.org/abs/2502.20747]
Production-scale distributed-system complexity does narrow the gap, because large deterministic systems also become epistemically opaque and depend on monitoring, observability, and post hoc reconstruction rather than direct whole-system inspection. [inference; source: https://doi.org/10.1007/s11229-008-9435-2; https://sre.google/sre-book/monitoring-distributed-systems/; https://www.routledge.com/Drift-into-Failure/Dekker/p/book/9781409422211]
The convergence is therefore partial rather than total: deterministic systems keep an advantage in local replayability and explicit rule-bound explanation, while both classes are weak in global end-to-end explainability at high scale. [inference; source: https://learn.microsoft.com/en-us/azure/ai-foundry/openai/how-to/reproducible-output; https://arxiv.org/abs/2408.04667; https://arxiv.org/abs/2502.20747; https://doi.org/10.1007/s11229-008-9435-2; https://sre.google/sre-book/monitoring-distributed-systems/]
For governance and audit use cases, the most defensible explanation surface in both classes is usually the boundary artefact, the logs, rules, traces, counterfactual conditions, and approvals that reconstruct the decision, not a claim of full internal transparency. [inference; source: https://arxiv.org/abs/1711.00399; https://www.nist.gov/publications/four-principles-explainable-artificial-intelligence; https://davidamitchell.github.io/Research/research/2026-04-26-ai-lowcode-observability-telemetry-governance.html; https://davidamitchell.github.io/Research/research/2026-04-30-explainable-ai-xai-regulation-governance.html; https://davidamitchell.github.io/Research/research/2026-05-09-hybrid-architecture-probabilistic-llm-deterministic-governance.html]

**Key findings:**

1. **Explainability in the reviewed literature is multi-dimensional rather than unitary, because formal sources distinguish meaningful explanation, explanation accuracy, transparency, post hoc explanation, and contrastive usefulness instead of treating explainability as one property.** ([inference]; high confidence; source: https://arxiv.org/abs/1702.08608; https://arxiv.org/abs/1606.03490; https://arxiv.org/abs/1711.00399; https://www.nist.gov/publications/four-principles-explainable-artificial-intelligence)
2. **Present-day Large Language Model systems should be treated as having a local explainability deficit even before scaling, because repeated calls can diverge under fixed settings and exact replay of one decision path is not guaranteed.** ([inference]; high confidence; source: https://learn.microsoft.com/en-us/azure/ai-foundry/openai/how-to/reproducible-output; https://arxiv.org/abs/2408.04667; https://arxiv.org/abs/2502.20747)
3. **Equivalently scoped deterministic software usually offers better local replayability and clearer bounded causal inspection than a Large Language Model system, because explicit rules, code paths, and logged state can often be rerun and inspected when dependencies are controlled.** ([inference]; medium confidence; source: https://sre.google/sre-book/monitoring-distributed-systems/; https://doi.org/10.1007/s11229-008-9435-2; https://davidamitchell.github.io/Research/research/2026-05-09-hybrid-architecture-probabilistic-llm-deterministic-governance.html)
4. **Production-scale deterministic distributed systems are not globally transparent, because engineers depend on monitoring, white-box telemetry, and post hoc analysis precisely when direct understanding of the whole dependency graph fails.** ([inference]; high confidence; source: https://sre.google/sre-book/monitoring-distributed-systems/; https://doi.org/10.1007/s11229-008-9435-2)
5. **Useful outcome-level explanation does not always require full internal transparency, because counterfactual explanation can identify what would need to change for a different result without exposing the entire internal mechanism.** ([inference]; medium confidence; source: https://arxiv.org/abs/1711.00399; https://www.nist.gov/publications/four-principles-explainable-artificial-intelligence)
6. **The explainability gap therefore converges but does not disappear at scale, because deterministic architectures lose global transparency while Large Language Model systems keep additional opacity from learned representations and residual non-determinism.** ([inference]; medium confidence; source: https://arxiv.org/abs/1606.03490; https://learn.microsoft.com/en-us/azure/ai-foundry/openai/how-to/reproducible-output; https://arxiv.org/abs/2408.04667; https://arxiv.org/abs/2502.20747; https://doi.org/10.1007/s11229-008-9435-2; https://sre.google/sre-book/monitoring-distributed-systems/)
7. **For governance and audit use cases, the most decision-useful explanation surface in both classes is usually the boundary artefact, logs, rules, traces, approvals, and counterfactual outcome conditions, rather than a full internal causal narrative.** ([inference]; medium confidence; source: https://arxiv.org/abs/1711.00399; https://www.nist.gov/publications/four-principles-explainable-artificial-intelligence; https://davidamitchell.github.io/Research/research/2026-04-26-ai-lowcode-observability-telemetry-governance.html; https://davidamitchell.github.io/Research/research/2026-04-30-explainable-ai-xai-regulation-governance.html; https://davidamitchell.github.io/Research/research/2026-05-09-governance-policy-determinism-vs-stochastic-llm.html; https://davidamitchell.github.io/Research/research/2026-05-09-hybrid-architecture-probabilistic-llm-deterministic-governance.html)

**Evidence map:**

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [inference] Explainability is multi-dimensional, not one property. | https://arxiv.org/abs/1702.08608 ; https://arxiv.org/abs/1606.03490 ; https://arxiv.org/abs/1711.00399 ; https://www.nist.gov/publications/four-principles-explainable-artificial-intelligence | high | formal definitions |
| [inference] Present-day LLM systems should be treated as having a local explainability deficit before scaling because controlled reruns still diverge. | https://learn.microsoft.com/en-us/azure/ai-foundry/openai/how-to/reproducible-output ; https://arxiv.org/abs/2408.04667 ; https://arxiv.org/abs/2502.20747 | high | residual variance |
| [inference] Deterministic software usually preserves better bounded local replayability than LLM-based systems. | https://sre.google/sre-book/monitoring-distributed-systems/ ; https://doi.org/10.1007/s11229-008-9435-2 ; https://davidamitchell.github.io/Research/research/2026-05-09-hybrid-architecture-probabilistic-llm-deterministic-governance.html | medium | explicit rules and logs |
| [inference] Large deterministic distributed systems are not globally transparent in practice. | https://sre.google/sre-book/monitoring-distributed-systems/ ; https://doi.org/10.1007/s11229-008-9435-2 | high | observability burden |
| [inference] Useful outcome-level explanation does not always require full internal transparency. | https://arxiv.org/abs/1711.00399 ; https://www.nist.gov/publications/four-principles-explainable-artificial-intelligence | medium | bounded outcome explanations |
| [inference] Scale narrows but does not erase the explainability gap between the two classes. | https://arxiv.org/abs/1606.03490 ; https://learn.microsoft.com/en-us/azure/ai-foundry/openai/how-to/reproducible-output ; https://arxiv.org/abs/2408.04667 ; https://arxiv.org/abs/2502.20747 ; https://doi.org/10.1007/s11229-008-9435-2 ; https://sre.google/sre-book/monitoring-distributed-systems/ | medium | convergence, not equivalence |
| [inference] Governance and audit explanations rely mainly on boundary artefacts rather than full internal transparency. | https://arxiv.org/abs/1711.00399 ; https://www.nist.gov/publications/four-principles-explainable-artificial-intelligence ; https://davidamitchell.github.io/Research/research/2026-04-26-ai-lowcode-observability-telemetry-governance.html ; https://davidamitchell.github.io/Research/research/2026-04-30-explainable-ai-xai-regulation-governance.html ; https://davidamitchell.github.io/Research/research/2026-05-09-governance-policy-determinism-vs-stochastic-llm.html ; https://davidamitchell.github.io/Research/research/2026-05-09-hybrid-architecture-probabilistic-llm-deterministic-governance.html | medium | governance surface |

**Assumptions:**

- [assumption; source: https://arxiv.org/abs/1702.08608; https://davidamitchell.github.io/Research/research/2026-05-09-hybrid-architecture-probabilistic-llm-deterministic-governance.html] "Equivalently scoped" is treated here as comparable task boundary, side-effect authority, and integration burden rather than identical code size or identical user interface. Justification: the explainability comparison is only meaningful when both systems are asked to do the same class of work at the same governance boundary.
- [assumption; source: https://sre.google/sre-book/monitoring-distributed-systems/; https://doi.org/10.1007/s11229-008-9435-2] Deterministic software is treated as replayable within a controlled environment, even though production drift, hidden dependencies, and infrastructure changes can weaken that property in practice. Justification: the comparison needs a baseline notion of deterministic execution before asking what scale does to it.

**Analysis:**

The weight of evidence favored formal explainability sources for the definition work and production engineering sources for the classical-system side, because this question turns on both what counts as explanation and what investigators can actually reconstruct in live systems. [inference; source: https://arxiv.org/abs/1702.08608; https://arxiv.org/abs/1606.03490; https://arxiv.org/abs/1711.00399; https://www.nist.gov/publications/four-principles-explainable-artificial-intelligence; https://sre.google/sre-book/monitoring-distributed-systems/]
One rival interpretation is that enough observability investment can erase the gap completely. The reviewed sources do not support that stronger claim, because Google Site Reliability Engineering still treats post hoc reconstruction as an ongoing discipline for complex deterministic systems while Microsoft and repeated-run studies still leave residual LLM variance under stabilization controls. [inference; source: https://sre.google/sre-book/monitoring-distributed-systems/; https://learn.microsoft.com/en-us/azure/ai-foundry/openai/how-to/reproducible-output; https://arxiv.org/abs/2408.04667; https://arxiv.org/abs/2502.20747]
Another rival interpretation is that counterfactual explanation makes internal transparency unnecessary. Wachter supports the practical value of that approach, but NIST and Lipton still distinguish useful explanation from faithful internal transparency, so counterfactuals help with some explanation tasks without solving the full explainability problem. [inference; source: https://arxiv.org/abs/1711.00399; https://www.nist.gov/publications/four-principles-explainable-artificial-intelligence; https://arxiv.org/abs/1606.03490]
The resulting judgment is therefore a bounded one: classical complexity makes deterministic systems far less transparent than their source code alone suggests, but present-day LLM-based systems still remain structurally worse on local replay and local internal explanation. [inference; source: https://doi.org/10.1007/s11229-008-9435-2; https://sre.google/sre-book/monitoring-distributed-systems/; https://learn.microsoft.com/en-us/azure/ai-foundry/openai/how-to/reproducible-output; https://arxiv.org/abs/2408.04667; https://arxiv.org/abs/2502.20747]

**Risks, gaps, uncertainties:**

- [inference; source: https://www.routledge.com/Drift-into-Failure/Dekker/p/book/9781409422211] The accessible Dekker source in this session is the publisher page rather than the full book text, so the item uses it only for bounded systems-theory framing, not for clause-level empirical claims.
- [inference; source: https://arxiv.org/abs/1606.03490; https://arxiv.org/abs/1702.08608] The formal explainability literature is richer on machine-learning models than on deterministic distributed software, so part of the cross-class comparison is necessarily inferential rather than explicitly stated in one source.
- [inference; source: https://sre.google/sre-book/monitoring-distributed-systems/; https://learn.microsoft.com/en-us/azure/ai-foundry/openai/how-to/reproducible-output] The strongest practical comparison evidence comes from production engineering documentation rather than from one head-to-head benchmark that measures explainability across both system classes under the same task boundary.

**Open questions:**

- Under what conditions does a deterministic distributed system become so dependency-heavy that its practical local replay advantage also disappears?
- Which governance artefacts, traces, rules, approvals, or counterfactual explanations, are most useful to non-specialist reviewers in each system class?
- How much could advances in tracing internal model circuits reduce the local explainability deficit for multi-step LLM-based systems without eliminating their residual variance?

### §7 Recursive Review

- [fact; source: https://github.com/davidamitchell/Research/blob/main/Research/in-progress/2026-05-18-agentic-explainability-vs-traditional.md] Recursive review metadata for this draft is recorded in this section after the final edit pass.
- [fact; source: https://github.com/davidamitchell/Research/blob/main/Research/in-progress/2026-05-18-agentic-explainability-vs-traditional.md] Acronym expansion, claim labeling, and synthesis-findings parity were re-checked after the last change.
- [inference; source: https://github.com/davidamitchell/Research/blob/main/Research/in-progress/2026-05-18-agentic-explainability-vs-traditional.md] No unresolved internal contradiction remains within the current draft.

---

## Findings

### Executive Summary

Multi-step Large Language Model-based systems are not equally explainable to equivalently scoped deterministic software systems, because they add model-internal opacity and residual run-to-run variation before production-scale complexity is even considered. [inference; source: https://arxiv.org/abs/1606.03490; https://learn.microsoft.com/en-us/azure/ai-foundry/openai/how-to/reproducible-output; https://arxiv.org/abs/2408.04667; https://arxiv.org/abs/2502.20747]
Production-scale distributed-system complexity does narrow the gap, because large deterministic systems also become epistemically opaque and depend on monitoring, observability, and post hoc reconstruction rather than direct whole-system inspection. [inference; source: https://doi.org/10.1007/s11229-008-9435-2; https://sre.google/sre-book/monitoring-distributed-systems/; https://www.routledge.com/Drift-into-Failure/Dekker/p/book/9781409422211]
The convergence is therefore partial rather than total: deterministic systems keep an advantage in local replayability and explicit rule-bound explanation, while both classes are weak in global end-to-end explainability at high scale. [inference; source: https://learn.microsoft.com/en-us/azure/ai-foundry/openai/how-to/reproducible-output; https://arxiv.org/abs/2408.04667; https://arxiv.org/abs/2502.20747; https://doi.org/10.1007/s11229-008-9435-2; https://sre.google/sre-book/monitoring-distributed-systems/]
For governance and audit use cases, the most defensible explanation surface in both classes is usually the boundary artefact, the logs, rules, traces, counterfactual conditions, and approvals that reconstruct the decision, not a claim of full internal transparency. [inference; source: https://arxiv.org/abs/1711.00399; https://www.nist.gov/publications/four-principles-explainable-artificial-intelligence; https://davidamitchell.github.io/Research/research/2026-04-26-ai-lowcode-observability-telemetry-governance.html; https://davidamitchell.github.io/Research/research/2026-04-30-explainable-ai-xai-regulation-governance.html; https://davidamitchell.github.io/Research/research/2026-05-09-hybrid-architecture-probabilistic-llm-deterministic-governance.html]

### Key Findings

1. **Explainability in the reviewed literature is multi-dimensional rather than unitary, because formal sources distinguish meaningful explanation, explanation accuracy, transparency, post hoc explanation, and contrastive usefulness instead of treating explainability as one property.** ([inference]; high confidence; source: https://arxiv.org/abs/1702.08608; https://arxiv.org/abs/1606.03490; https://arxiv.org/abs/1711.00399; https://www.nist.gov/publications/four-principles-explainable-artificial-intelligence)
2. **Present-day Large Language Model systems should be treated as having a local explainability deficit even before scaling, because repeated calls can diverge under fixed settings and exact replay of one decision path is not guaranteed.** ([inference]; high confidence; source: https://learn.microsoft.com/en-us/azure/ai-foundry/openai/how-to/reproducible-output; https://arxiv.org/abs/2408.04667; https://arxiv.org/abs/2502.20747)
3. **Equivalently scoped deterministic software usually offers better local replayability and clearer bounded causal inspection than a Large Language Model system, because explicit rules, code paths, and logged state can often be rerun and inspected when dependencies are controlled.** ([inference]; medium confidence; source: https://sre.google/sre-book/monitoring-distributed-systems/; https://doi.org/10.1007/s11229-008-9435-2; https://davidamitchell.github.io/Research/research/2026-05-09-hybrid-architecture-probabilistic-llm-deterministic-governance.html)
4. **Production-scale deterministic distributed systems are not globally transparent, because engineers depend on monitoring, white-box telemetry, and post hoc analysis precisely when direct understanding of the whole dependency graph fails.** ([inference]; high confidence; source: https://sre.google/sre-book/monitoring-distributed-systems/; https://doi.org/10.1007/s11229-008-9435-2)
5. **Useful outcome-level explanation does not always require full internal transparency, because counterfactual explanation can identify what would need to change for a different result without exposing the entire internal mechanism.** ([inference]; medium confidence; source: https://arxiv.org/abs/1711.00399; https://www.nist.gov/publications/four-principles-explainable-artificial-intelligence)
6. **The explainability gap therefore converges but does not disappear at scale, because deterministic architectures lose global transparency while Large Language Model systems keep additional opacity from learned representations and residual non-determinism.** ([inference]; medium confidence; source: https://arxiv.org/abs/1606.03490; https://learn.microsoft.com/en-us/azure/ai-foundry/openai/how-to/reproducible-output; https://arxiv.org/abs/2408.04667; https://arxiv.org/abs/2502.20747; https://doi.org/10.1007/s11229-008-9435-2; https://sre.google/sre-book/monitoring-distributed-systems/)
7. **For governance and audit use cases, the most decision-useful explanation surface in both classes is usually the boundary artefact, logs, rules, traces, approvals, and counterfactual outcome conditions, rather than a full internal causal narrative.** ([inference]; medium confidence; source: https://arxiv.org/abs/1711.00399; https://www.nist.gov/publications/four-principles-explainable-artificial-intelligence; https://davidamitchell.github.io/Research/research/2026-04-26-ai-lowcode-observability-telemetry-governance.html; https://davidamitchell.github.io/Research/research/2026-04-30-explainable-ai-xai-regulation-governance.html; https://davidamitchell.github.io/Research/research/2026-05-09-governance-policy-determinism-vs-stochastic-llm.html; https://davidamitchell.github.io/Research/research/2026-05-09-hybrid-architecture-probabilistic-llm-deterministic-governance.html)

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [inference] Explainability is multi-dimensional, not one property. | https://arxiv.org/abs/1702.08608 ; https://arxiv.org/abs/1606.03490 ; https://arxiv.org/abs/1711.00399 ; https://www.nist.gov/publications/four-principles-explainable-artificial-intelligence | high | formal definitions |
| [inference] Present-day LLM systems should be treated as having a local explainability deficit before scaling because controlled reruns still diverge. | https://learn.microsoft.com/en-us/azure/ai-foundry/openai/how-to/reproducible-output ; https://arxiv.org/abs/2408.04667 ; https://arxiv.org/abs/2502.20747 | high | residual variance |
| [inference] Deterministic software usually preserves better bounded local replayability than LLM-based systems. | https://sre.google/sre-book/monitoring-distributed-systems/ ; https://doi.org/10.1007/s11229-008-9435-2 ; https://davidamitchell.github.io/Research/research/2026-05-09-hybrid-architecture-probabilistic-llm-deterministic-governance.html | medium | explicit rules and logs |
| [inference] Large deterministic distributed systems are not globally transparent in practice. | https://sre.google/sre-book/monitoring-distributed-systems/ ; https://doi.org/10.1007/s11229-008-9435-2 | high | observability burden |
| [inference] Useful outcome-level explanation does not always require full internal transparency. | https://arxiv.org/abs/1711.00399 ; https://www.nist.gov/publications/four-principles-explainable-artificial-intelligence | medium | bounded outcome explanations |
| [inference] Scale narrows but does not erase the explainability gap between the two classes. | https://arxiv.org/abs/1606.03490 ; https://learn.microsoft.com/en-us/azure/ai-foundry/openai/how-to/reproducible-output ; https://arxiv.org/abs/2408.04667 ; https://arxiv.org/abs/2502.20747 ; https://doi.org/10.1007/s11229-008-9435-2 ; https://sre.google/sre-book/monitoring-distributed-systems/ | medium | convergence, not equivalence |
| [inference] Governance and audit explanations rely mainly on boundary artefacts rather than full internal transparency. | https://arxiv.org/abs/1711.00399 ; https://www.nist.gov/publications/four-principles-explainable-artificial-intelligence ; https://davidamitchell.github.io/Research/research/2026-04-26-ai-lowcode-observability-telemetry-governance.html ; https://davidamitchell.github.io/Research/research/2026-04-30-explainable-ai-xai-regulation-governance.html ; https://davidamitchell.github.io/Research/research/2026-05-09-governance-policy-determinism-vs-stochastic-llm.html ; https://davidamitchell.github.io/Research/research/2026-05-09-hybrid-architecture-probabilistic-llm-deterministic-governance.html | medium | governance surface |

### Assumptions

- [assumption; source: https://arxiv.org/abs/1702.08608; https://davidamitchell.github.io/Research/research/2026-05-09-hybrid-architecture-probabilistic-llm-deterministic-governance.html] "Equivalently scoped" is treated here as comparable task boundary, side-effect authority, and integration burden rather than identical code size or identical user interface. Justification: the explainability comparison is only meaningful when both systems are asked to do the same class of work at the same governance boundary.
- [assumption; source: https://sre.google/sre-book/monitoring-distributed-systems/; https://doi.org/10.1007/s11229-008-9435-2] Deterministic software is treated as replayable within a controlled environment, even though production drift, hidden dependencies, and infrastructure changes can weaken that property in practice. Justification: the comparison needs a baseline notion of deterministic execution before asking what scale does to it.

### Analysis

The weight of evidence favored formal explainability sources for the definition work and production engineering sources for the classical-system side, because this question turns on both what counts as explanation and what investigators can actually reconstruct in live systems. [inference; source: https://arxiv.org/abs/1702.08608; https://arxiv.org/abs/1606.03490; https://arxiv.org/abs/1711.00399; https://www.nist.gov/publications/four-principles-explainable-artificial-intelligence; https://sre.google/sre-book/monitoring-distributed-systems/]
One rival interpretation is that enough observability investment can erase the gap completely. The reviewed sources do not support that stronger claim, because Google Site Reliability Engineering still treats post hoc reconstruction as an ongoing discipline for complex deterministic systems while Microsoft and repeated-run studies still leave residual LLM variance under stabilization controls. [inference; source: https://sre.google/sre-book/monitoring-distributed-systems/; https://learn.microsoft.com/en-us/azure/ai-foundry/openai/how-to/reproducible-output; https://arxiv.org/abs/2408.04667; https://arxiv.org/abs/2502.20747]
Another rival interpretation is that counterfactual explanation makes internal transparency unnecessary. Wachter supports the practical value of that approach, but NIST and Lipton still distinguish useful explanation from faithful internal transparency, so counterfactuals help with some explanation tasks without solving the full explainability problem. [inference; source: https://arxiv.org/abs/1711.00399; https://www.nist.gov/publications/four-principles-explainable-artificial-intelligence; https://arxiv.org/abs/1606.03490]
The resulting judgment is therefore a bounded one: classical complexity makes deterministic systems far less transparent than their source code alone suggests, but present-day LLM-based systems still remain structurally worse on local replay and local internal explanation. [inference; source: https://doi.org/10.1007/s11229-008-9435-2; https://sre.google/sre-book/monitoring-distributed-systems/; https://learn.microsoft.com/en-us/azure/ai-foundry/openai/how-to/reproducible-output; https://arxiv.org/abs/2408.04667; https://arxiv.org/abs/2502.20747]

### Risks, Gaps, and Uncertainties

- [inference; source: https://www.routledge.com/Drift-into-Failure/Dekker/p/book/9781409422211] The accessible Dekker source in this session is the publisher page rather than the full book text, so the item uses it only for bounded systems-theory framing, not for clause-level empirical claims.
- [inference; source: https://arxiv.org/abs/1606.03490; https://arxiv.org/abs/1702.08608] The formal explainability literature is richer on machine-learning models than on deterministic distributed software, so part of the cross-class comparison is necessarily inferential rather than explicitly stated in one source.
- [inference; source: https://sre.google/sre-book/monitoring-distributed-systems/; https://learn.microsoft.com/en-us/azure/ai-foundry/openai/how-to/reproducible-output] The strongest practical comparison evidence comes from production engineering documentation rather than from one head-to-head benchmark that measures explainability across both system classes under the same task boundary.

### Open Questions

- Under what conditions does a deterministic distributed system become so dependency-heavy that its practical local replay advantage also disappears?
- Which governance artefacts, traces, rules, approvals, or counterfactual explanations, are most useful to non-specialist reviewers in each system class?
- How much could advances in tracing internal model circuits reduce the local explainability deficit for multi-step LLM-based systems without eliminating their residual variance?

---

## Output

- Type: knowledge
- Description: Structured comparison of where explainability diverges and converges between multi-step Large Language Model-based systems and deterministic software systems, with emphasis on local replay, global opacity, and governance-grade explanation surfaces. [inference; source: https://arxiv.org/abs/1702.08608; https://sre.google/sre-book/monitoring-distributed-systems/; https://learn.microsoft.com/en-us/azure/ai-foundry/openai/how-to/reproducible-output]
- Links:
  - https://arxiv.org/abs/1702.08608
  - https://arxiv.org/abs/1711.00399
  - https://sre.google/sre-book/monitoring-distributed-systems/
