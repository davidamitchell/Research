---
review_count: 1
title: "Research Question 4.3: Formal bounds on generalisation outside the training distribution for tool-using Large Language Model systems under non-deterministic tool outputs"
added: 2026-05-18T19:40:00+00:00
status: completed
priority: high
blocks:
  - 2026-05-18-rq5-1-stochastic-vs-deterministic-failures
tags: [agentic-ai, llm, machine-learning, invariants, evaluation]
themes: [agentic-ai, llm-reasoning, tools-infrastructure, formal-guarantees, distribution-shift]
started: 2026-05-19T12:16:01+00:00
completed: 2026-05-19T12:39:55+00:00
output: [knowledge]
cites:
  - 2026-05-18-rq4-1-agentic-loop-explanatory-reach
  - 2026-05-18-rq4-2-adversarial-error-propagation
  - 2026-05-18-rq3-2-stochastic-parrot-ood
  - 2026-05-18-rq2-4-causal-hierarchy-formal-limits
related:
  - 2026-05-18-agentic-explainability-vs-traditional
  - 2026-05-08-integrated-cascading-failure-agentic-vs-generative-ai-risk
  - 2026-05-02-ai-security-threat-model-prompt-injection-rag-supply-chain
superseded_by: ~
supersedes: ~
item_type: primary
confidence: medium
versions:
  - version: "1.0"
    sha: 4f69d9f0eeb1b372dd4d8f3540a4891259381300
    changed: 2026-05-19
    progress: progress/2026-05-19-rq4-3-ood-generalization-agentic.md
    summary: "Initial completion"
---

# Research Question 4.3: Formal bounds on generalisation outside the training distribution for tool-using Large Language Model systems under non-deterministic tool outputs

## Research Question

What formal bounds can be stated for generalisation outside the training distribution in tool-using Large Language Model systems when their tools return non-deterministic outputs under unconstrained production conditions?

## Scope

**In scope:**
- Reducible model uncertainty versus irreducible output randomness in tool-using Large Language Model systems
- Simon-style decision-making under limited information and computational capacity
- Methods that attach calibrated probabilities or prediction sets to model outputs
- Monte Carlo (MC) Dropout as a Bayesian approximation for model uncertainty
- Formal bounds on generalisation outside the training distribution for Large Language Model planners

**Out of scope:**
- Specific production observability tooling
- Human-in-the-loop mitigation strategies

**Constraints:** Synthesises Phase 4, must provide formal bounds rather than only qualitative assessment, must use URL-backed sources only, and must connect to Phase 5 through the stochastic-versus-deterministic comparison.

## Context

Research Question 4.1 and Research Question 4.2 concluded that tool-using loops widen search and verification surfaces without removing the base Large Language Model's causal and propagation limits. [fact; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq4-1-agentic-loop-explanatory-reach.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq4-2-adversarial-error-propagation.md]

Machine learning theory refers to deployment beyond the training distribution as out-of-distribution (OOD) generalisation, and current theory already states that arbitrary OOD generalisation is impossible without additional structure such as bounded shift or invariant features. [fact; source: https://proceedings.neurips.cc/paper/2021/hash/c5c1cb0bebd56ae38817b251ad72bedb-Abstract.html; https://www.alexkulesza.com/pubs/adapt_mlj10.pdf]

This item therefore asks what survives when the planner is wrapped in stochastic tools that inject irreducible observation noise and may also shift away from the training or calibration regime. [inference; source: https://arxiv.org/abs/1703.04977; https://arxiv.org/abs/1906.02530; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq4-2-adversarial-error-propagation.md]

## Approach

1. Distinguish model uncertainty that can be reduced with more data from observation noise that cannot be explained away by more data.
2. Apply Simon's limited-information decision frame: what decision quality is achievable when the planner has limited information, limited computation, and no explicit causal model of the tool environment?
3. Survey uncertainty methods applicable to Large Language Model planners, including Bayesian approximations, Monte Carlo Dropout, and conformal prediction methods that output calibrated prediction sets.
4. Derive the strongest formal bounds that current OOD theory allows for the composite planner-tool system.
5. Identify which classes of tool non-determinism remain manageable under those bounds and which make the guarantees vacuous.

## Sources

**Consulted:**

- [x] [Kendall & Gal (2017) What Uncertainties Do We Need in Bayesian Deep Learning for Computer Vision?](https://arxiv.org/abs/1703.04977) - primary source distinguishing epistemic and aleatoric uncertainty.
- [x] [Gal & Ghahramani (2016) Dropout as a Bayesian Approximation: Representing Model Uncertainty in Deep Learning](https://arxiv.org/abs/1506.02142) - primary source for Monte Carlo Dropout as approximate Bayesian inference.
- [x] [Ovadia et al. (2019) Can You Trust Your Model's Uncertainty? Evaluating Predictive Uncertainty Under Dataset Shift](https://arxiv.org/abs/1906.02530) - primary benchmark on calibration under dataset shift.
- [x] [Angelopoulos & Bates (2022) A Gentle Introduction to Conformal Prediction and Distribution-Free Uncertainty Quantification](https://arxiv.org/abs/2107.07511) - primary tutorial source on conformal prediction guarantees.
- [x] [Gibbs & Candès (2021) Adaptive Conformal Inference Under Distribution Shift](https://arxiv.org/abs/2106.00170) - primary source for long-run coverage under non-exchangeable online shift.
- [x] [Gibbs & Candès (2022) Conformal Inference for Online Prediction with Arbitrary Distribution Shifts](https://arxiv.org/abs/2208.08401) - primary source for local regret-style adaptation under arbitrary online shift.
- [x] [Ben-David et al. (2010) A Theory of Learning from Different Domains](https://www.alexkulesza.com/pubs/adapt_mlj10.pdf) - primary source for target-risk bounds under domain adaptation assumptions.
- [x] [Ye et al. (2021) Towards a Theoretical Framework of Out-of-Distribution Generalization](https://proceedings.neurips.cc/paper/2021/hash/c5c1cb0bebd56ae38817b251ad72bedb-Abstract.html) - primary source stating that arbitrary out-of-distribution generalisation is impossible and that bounds depend on restricted shift structure.
- [x] [Simon (1978) Rational Decision-Making in Business Organizations](https://www.nobelprize.org/uploads/2018/06/simon-lecture.pdf) - accessible primary exposition of bounded rationality and satisficing.
- [x] [Mitchell (2026) Research Question 4.1: Tool-feedback loops and explanatory reach](https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq4-1-agentic-loop-explanatory-reach.md) - prior completed item on loop-level causal limits.
- [x] [Mitchell (2026) Research Question 4.2: Adversarial inputs and error propagation through multi-step tool-using verification and strategy phases](https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq4-2-adversarial-error-propagation.md) - prior completed item on error amplification through tools and verification.
- [x] [Mitchell (2026) Research Question 3.2: The Stochastic Parrot Under Pressure](https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq3-2-stochastic-parrot-ood.md) - prior completed item on novelty-sensitive structural failure.
- [x] [Mitchell (2026) Research Question 2.4: Pearl's Causal Hierarchy and the formal limits of observational data for intervention and counterfactual reasoning](https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq2-4-causal-hierarchy-formal-limits.md) - prior completed item on why observational pattern learning does not determine higher-level causal answers.

**Identified but not consulted:**

- [ ] [Simon (1955) A Behavioral Model of Rational Choice](http://www.jstor.org/stable/1884852) - stable primary reference identified but not consulted in this session.

---

## Research Skill Output

### §0 Initialise

- Question: what formal bounds can be stated for generalisation outside the training distribution in tool-using Large Language Model systems when tools return non-deterministic outputs under unconstrained production conditions?
- Scope: uncertainty decomposition, bounded rationality, uncertainty estimation methods, domain-shift bounds, and classes of tool non-determinism that preserve or destroy guarantees.
- Constraints: full-mode investigation, URL-backed sources only, direct cross-reference to prior completed items, explicit claim labels in the investigation, and canonical tags only.
- Output: executive summary, key findings, evidence map, assumptions, analysis, risks and gaps, open questions, and a populated output section.
- Prior completed items consulted: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq4-1-agentic-loop-explanatory-reach.md ; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq4-2-adversarial-error-propagation.md ; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq3-2-stochastic-parrot-ood.md ; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq2-4-causal-hierarchy-formal-limits.md ; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-agentic-explainability-vs-traditional.md

### §1 Question Decomposition

1. Prior completed-item sweep
   1.1 What limits on causal reach and error propagation were already established in Research Questions 4.1 and 4.2?
   1.2 Which of those results must any formal OOD bound inherit?
2. Uncertainty structure
   2.1 What is epistemic uncertainty?
   2.2 What is aleatoric uncertainty?
   2.3 Which parts of a planner-tool loop belong to each class?
3. Decision framework
   3.1 How does bounded rationality describe a planner acting with limited information and computation?
   3.2 What does that imply for the form of any guarantee?
4. Uncertainty estimation methods
   4.1 What does Monte Carlo Dropout guarantee?
   4.2 How well do uncertainty estimates remain calibrated under dataset shift?
   4.3 What does conformal prediction guarantee under exchangeability, covariate shift, and arbitrary online shift?
5. Formal OOD bounds
   5.1 What target-risk bound does domain adaptation theory provide?
   5.2 What impossibility result applies when shift is unconstrained?
   5.3 How do those results transfer to tool-using Large Language Model systems?
6. Tool-output classes
   6.1 Which forms of non-determinism remain inside the assumptions needed for useful guarantees?
   6.2 Which forms make the bounds vacuous?

### §2 Investigation

#### A. Prior completed-item sweep

- [fact] Research Question 4.1 concluded that tool-feedback loops improve search, retrieval, and retry opportunities without giving the base Large Language Model intrinsic causal understanding. [source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq4-1-agentic-loop-explanatory-reach.md]
- [fact] Research Question 4.2 concluded that once a loop ingests a corrupted or shifted observation, planning, tool use, memory, and verification can propagate that error across later steps. [source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq4-2-adversarial-error-propagation.md]
- [fact] Research Question 3.2 concluded that Large Language Model performance remains fragile on genuinely novel prompts that require structural intervention rather than familiar pattern completion. [source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq3-2-stochastic-parrot-ood.md]
- [inference] Any formal bound for the current item therefore has to cover a composite system whose planner lacks intrinsic causal guarantees and whose error can be amplified by recurrent interaction with tools. [source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq4-1-agentic-loop-explanatory-reach.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq4-2-adversarial-error-propagation.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq3-2-stochastic-parrot-ood.md]

#### B. Reducible versus irreducible uncertainty

- [fact] Kendall and Gal define epistemic uncertainty as uncertainty in the model that can be reduced with more data, and aleatoric uncertainty as noise inherent in the observations that cannot be explained away by collecting more data. [source: https://arxiv.org/abs/1703.04977]
- [fact] Kendall and Gal also show that aleatoric uncertainty can be input-dependent and remains present even when the model is otherwise well trained. [source: https://arxiv.org/abs/1703.04977]
- [inference] In a tool-using loop, planner or verifier uncertainty belongs mainly to the epistemic term, while stochastic tool responses, timing jitter, and externally varying search results belong mainly to the aleatoric term. [source: https://arxiv.org/abs/1703.04977; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq4-2-adversarial-error-propagation.md]
- [inference] More training data or model averaging can reduce only the planner-side term; they cannot eliminate randomness that is generated by the environment or by the tool itself. [source: https://arxiv.org/abs/1703.04977; https://arxiv.org/abs/1506.02142]

#### C. Bounded rationality and the decision model

- [fact] Simon's Nobel lecture presents bounded rationality and satisficing as alternatives to the classical picture of globally optimizing decision-makers with unlimited information and computational capacity. [source: https://www.nobelprize.org/uploads/2018/06/simon-lecture.pdf]
- [inference] A tool-using Large Language Model loop therefore fits bounded rationality better than optimal control, because it acts through partial observations, finite context, approximate search, and incomplete models of the environment. [source: https://www.nobelprize.org/uploads/2018/06/simon-lecture.pdf; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq4-1-agentic-loop-explanatory-reach.md]
- [inference] Under that frame, the strongest credible guarantees are conditional performance bounds under information constraints rather than guarantees of globally optimal action selection. [source: https://www.nobelprize.org/uploads/2018/06/simon-lecture.pdf; https://www.alexkulesza.com/pubs/adapt_mlj10.pdf]

#### D. What current uncertainty-estimation methods do and do not guarantee

- [fact] Gal and Ghahramani cast dropout in deep neural networks as approximate Bayesian inference in deep Gaussian processes and show how Monte Carlo Dropout can recover model uncertainty estimates from existing networks. [source: https://arxiv.org/abs/1506.02142]
- [fact] Ovadia et al. benchmark predictive-uncertainty methods under dataset shift and report that several popular methods, including post-hoc calibration approaches, degrade under shift, while model-marginalizing methods perform better but do not make the shift problem disappear. [source: https://arxiv.org/abs/1906.02530]
- [inference] Monte Carlo Dropout is therefore useful as an approximate epistemic signal, but it is not a formal OOD correctness guarantee for planner outputs under shifted or tool-mediated inputs. [source: https://arxiv.org/abs/1506.02142; https://arxiv.org/abs/1906.02530]
- [inference] Any claim that a planner has solved OOD reliability by attaching Monte Carlo Dropout confidence scores would exceed what the cited theory and shift benchmarks support. [source: https://arxiv.org/abs/1506.02142; https://arxiv.org/abs/1906.02530]

#### E. What conformal prediction guarantees

- [fact] Angelopoulos and Bates define conformal prediction as a framework that wraps any model and returns prediction sets with explicit finite-sample coverage guarantees when the calibration and test points are exchangeable. [source: https://arxiv.org/abs/2107.07511]
- [fact] Gibbs and Candès show that adaptive conformal inference can achieve the desired coverage frequency over long time intervals even when the data-generating distribution varies over time in an unknown fashion. [source: https://arxiv.org/abs/2106.00170]
- [fact] Gibbs and Candès later extend the online setting to arbitrary distribution shifts and give a procedure with provably small regret over local time intervals of a chosen width. [source: https://arxiv.org/abs/2208.08401]
- [inference] These guarantees are about marginal or long-run coverage of prediction sets, not about the pointwise correctness of one selected action in one arbitrary deployment trajectory. [source: https://arxiv.org/abs/2107.07511; https://arxiv.org/abs/2106.00170; https://arxiv.org/abs/2208.08401]
- [inference] Conformal wrappers can therefore make a planner more honest about uncertainty, but they do not by themselves supply a universal bound on single-trajectory error under unconstrained tool shift. [source: https://arxiv.org/abs/2107.07511; https://arxiv.org/abs/2208.08401]

#### F. Formal OOD and domain-adaptation bounds

- [fact] Ben-David et al. bound a classifier's target-domain error in terms of its source-domain error, a divergence between the two domains, and the combined error of the best single hypothesis for both domains. [source: https://www.alexkulesza.com/pubs/adapt_mlj10.pdf]
- [fact] Ben-David et al. make the bound conditional on the existence of a hypothesis that performs well in both domains and on the ability to estimate domain divergence from unlabeled samples. [source: https://www.alexkulesza.com/pubs/adapt_mlj10.pdf]
- [fact] Ye et al. state that arbitrary out-of-distribution generalisation is clearly impossible and derive an OOD generalization error bound that depends on restricted shift structure, especially their expansion-function formalism. [source: https://proceedings.neurips.cc/paper/2021/hash/c5c1cb0bebd56ae38817b251ad72bedb-Abstract.html]
- [inference] Together, these results imply that non-vacuous OOD guarantees require at least one of the following: bounded divergence, invariant predictive structure, overlapping support, or an online calibration regime whose notion of success is coverage or regret rather than exact correctness. [source: https://www.alexkulesza.com/pubs/adapt_mlj10.pdf; https://proceedings.neurips.cc/paper/2021/hash/c5c1cb0bebd56ae38817b251ad72bedb-Abstract.html; https://arxiv.org/abs/2208.08401]
- [inference] If production conditions are unconstrained, then the divergence term and the best-shared-hypothesis term cannot be assumed small, so the classical target-risk bound becomes vacuous. [source: https://www.alexkulesza.com/pubs/adapt_mlj10.pdf; https://proceedings.neurips.cc/paper/2021/hash/c5c1cb0bebd56ae38817b251ad72bedb-Abstract.html]

#### G. Transfer to tool-using Large Language Model systems

- [fact] Research Question 2.4 concluded that observational pattern learning does not generically determine answers to intervention or counterfactual questions. [source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq2-4-causal-hierarchy-formal-limits.md]
- [inference] A tool-using Large Language Model system inherits the planner's OOD limits and then adds new stochasticity through the tool interface, so its best formal bound cannot be stronger than the weakest uncontrolled component in the planner-tool-environment chain. [source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq2-4-causal-hierarchy-formal-limits.md; https://www.alexkulesza.com/pubs/adapt_mlj10.pdf; https://arxiv.org/abs/1703.04977]
- [inference] For scalar loss, the composite deployment risk is constrained by a Ben-David-style shift term plus an irreducible aleatoric floor from tool randomness, while any narrower guarantee must come from abstention sets, online recalibration, or independent external correction. [source: https://www.alexkulesza.com/pubs/adapt_mlj10.pdf; https://arxiv.org/abs/1703.04977; https://arxiv.org/abs/2107.07511; https://arxiv.org/abs/2208.08401]
- [inference] Research Question 4.2 sharpens this result because recurrent planning and verification can amplify a shifted or adversarial tool observation before any correction arrives, which means the effective bound also depends on verifier independence and correction latency. [source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq4-2-adversarial-error-propagation.md; https://arxiv.org/abs/2208.08401]

#### H. Which tool-output classes are manageable

- [inference] Manageable non-determinism is limited to regimes where tool outputs remain inside the support of the calibration process, shift slowly enough for online adaptation, or can be wrapped in independent prediction sets or deterministic checks. [source: https://arxiv.org/abs/2107.07511; https://arxiv.org/abs/2106.00170; https://arxiv.org/abs/2208.08401]
- [inference] Unmanageable non-determinism includes support-mismatched outputs, adversarially crafted observations, hidden regime changes, or tool responses whose semantics the loop cannot independently verify, because those settings break the assumptions behind both domain-adaptation and conformal-style guarantees. [source: https://proceedings.neurips.cc/paper/2021/hash/c5c1cb0bebd56ae38817b251ad72bedb-Abstract.html; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq4-2-adversarial-error-propagation.md; https://arxiv.org/abs/1906.02530]

#### I. Searched but not found as a single theorem

- [inference] The consulted primary sources do not provide one unified theorem that simultaneously covers Large Language Model planning, stochastic tool outputs, recurrent verification, and arbitrary production shift, so the final bound in this item is necessarily a synthesis of adjacent theories rather than a citation to one pre-existing agent-specific theorem. [source: https://www.alexkulesza.com/pubs/adapt_mlj10.pdf; https://proceedings.neurips.cc/paper/2021/hash/c5c1cb0bebd56ae38817b251ad72bedb-Abstract.html; https://arxiv.org/abs/2208.08401]

### §3 Reasoning

- [inference] The primary-source results available here are conditional rather than absolute: Ben-David et al. require bounded divergence and a good shared hypothesis, Ye et al. rule out arbitrary OOD guarantees, and conformal methods narrow the guarantee to coverage frequency or regret. [source: https://www.alexkulesza.com/pubs/adapt_mlj10.pdf; https://proceedings.neurips.cc/paper/2021/hash/c5c1cb0bebd56ae38817b251ad72bedb-Abstract.html; https://arxiv.org/abs/2106.00170; https://arxiv.org/abs/2208.08401]
- [inference] Agentic systems can be bounded only when their deployment shift, tool process, and correction channel satisfy extra assumptions that keep the generic OOD terms finite. [source: https://www.alexkulesza.com/pubs/adapt_mlj10.pdf; https://arxiv.org/abs/1703.04977; https://arxiv.org/abs/2208.08401]
- [inference] The uncertainty-estimation layer changes what the system can report about its confidence, but it does not remove the impossibility result for arbitrary shift or the irreducible aleatoric component of tool outputs. [source: https://arxiv.org/abs/1506.02142; https://arxiv.org/abs/1703.04977; https://arxiv.org/abs/1906.02530; https://proceedings.neurips.cc/paper/2021/hash/c5c1cb0bebd56ae38817b251ad72bedb-Abstract.html]

### §4 Consistency Check

- [fact] No consulted source offers a non-vacuous universal correctness bound under arbitrary deployment shift, and Ye et al. explicitly state that arbitrary out-of-distribution generalisation is impossible. [source: https://proceedings.neurips.cc/paper/2021/hash/c5c1cb0bebd56ae38817b251ad72bedb-Abstract.html]
- [inference] Gal and Ghahramani and Ovadia et al. address different layers of the same problem: the former show how Monte Carlo Dropout approximates model uncertainty, while the latter show that uncertainty calibration still degrades under shift. [source: https://arxiv.org/abs/1506.02142; https://arxiv.org/abs/1906.02530]
- [inference] Conformal prediction changes the output object from one point estimate to a set or frequency target, so its guarantees coexist with the impossibility result instead of overturning it. [source: https://arxiv.org/abs/2107.07511; https://arxiv.org/abs/2106.00170; https://arxiv.org/abs/2208.08401]
- [inference] The final answer should therefore separate three guarantee types: target-risk bounds under restricted shift, uncertainty estimates for reducible model uncertainty, and coverage or regret guarantees for set-valued outputs under online shift. [source: https://www.alexkulesza.com/pubs/adapt_mlj10.pdf; https://arxiv.org/abs/1703.04977; https://arxiv.org/abs/2208.08401]

### §5 Depth and Breadth Expansion

- [inference] Technical lens: the composite planner-tool system behaves like a partially observed decision process whose reliability is limited by the least controlled interface, which makes open-world tool access the dominant bound-breaker. [source: https://www.alexkulesza.com/pubs/adapt_mlj10.pdf; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq4-2-adversarial-error-propagation.md]
- [inference] Historical lens: Simon's bounded-rationality frame predicts satisficing under uncertainty, which aligns with current agent loops that search, retry, and abstain rather than compute globally optimal action policies. [source: https://www.nobelprize.org/uploads/2018/06/simon-lecture.pdf; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq4-1-agentic-loop-explanatory-reach.md]
- [inference] Behavioural lens: when uncertainty estimates are miscalibrated under shift, the loop can act with unjustified confidence, so better uncertainty reporting matters only if the orchestration layer can abstain, defer, or gather new evidence. [source: https://arxiv.org/abs/1906.02530; https://arxiv.org/abs/2107.07511]
- [inference] Governance lens: Research Question 4.2 implies that self-verification is weakest exactly when tool outputs are semantically contaminated, so independent verification and typed tool contracts matter more than marginal gains in confidence estimation alone. [source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq4-2-adversarial-error-propagation.md; https://arxiv.org/abs/2208.08401]
- [inference] Phase-5 bridge: deterministic coded systems can sometimes bound behaviour by construction when interfaces and state transitions are explicit, whereas tool-using Large Language Model loops usually inherit stochastic uncertainty floors and conditional OOD guarantees instead of exact correctness guarantees. [source: https://www.alexkulesza.com/pubs/adapt_mlj10.pdf; https://arxiv.org/abs/1703.04977; https://arxiv.org/abs/2208.08401]

### §6 Synthesis

**Executive summary:**

- [inference] Under unconstrained production conditions, tool-using Large Language Model systems have no non-vacuous universal bound on generalisation outside the training distribution, because arbitrary out-of-distribution shift is impossible to bound without additional structural assumptions and stochastic tool outputs add irreducible uncertainty. [source: https://proceedings.neurips.cc/paper/2021/hash/c5c1cb0bebd56ae38817b251ad72bedb-Abstract.html; https://www.alexkulesza.com/pubs/adapt_mlj10.pdf; https://arxiv.org/abs/1703.04977]
- [inference] Current theory supports narrower guarantees: domain-adaptation target-risk bounds under bounded divergence and a low shared-error term, approximate epistemic uncertainty estimates from methods such as Monte Carlo Dropout, and conformal coverage guarantees for set-valued outputs under exchangeable or adaptively tracked shift. [source: https://www.alexkulesza.com/pubs/adapt_mlj10.pdf; https://arxiv.org/abs/1506.02142; https://arxiv.org/abs/2107.07511; https://arxiv.org/abs/2106.00170; https://arxiv.org/abs/2208.08401]
- [inference] For the composite planner-tool loop, the formal limit is set by the weakest uncontrolled surface, so open-world or adversarial tool outputs can make the classical bounds vacuous before the planner's internal uncertainty estimator becomes the decisive factor. [source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq4-2-adversarial-error-propagation.md; https://www.alexkulesza.com/pubs/adapt_mlj10.pdf; https://arxiv.org/abs/1906.02530]
- [inference] The practical implication is that current theory supports conditional risk management, abstention, and external correction for tool-using Large Language Model systems, not guaranteed correctness on arbitrary production trajectories. [source: https://arxiv.org/abs/2208.08401; https://arxiv.org/abs/2107.07511; https://www.nobelprize.org/uploads/2018/06/simon-lecture.pdf]

**Key findings:**

- [fact] Arbitrary out-of-distribution generalisation is impossible without restricting the family of deployment shifts, and classical target-risk bounds require bounded divergence between source and target domains plus a hypothesis that works well on both. [source: https://proceedings.neurips.cc/paper/2021/hash/c5c1cb0bebd56ae38817b251ad72bedb-Abstract.html; https://www.alexkulesza.com/pubs/adapt_mlj10.pdf]
- [inference] Tool-output randomness belongs mainly to the aleatoric uncertainty term, so it creates an irreducible error floor that cannot be removed by collecting more planner training data alone. [source: https://arxiv.org/abs/1703.04977]
- [inference] Simon's bounded-rationality frame describes tool-using Large Language Model loops more accurately than an omniscient optimization frame, which means their guarantees should be framed as performance under partial information and finite computation rather than as exact optimal control. [source: https://www.nobelprize.org/uploads/2018/06/simon-lecture.pdf; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq4-1-agentic-loop-explanatory-reach.md]
- [inference] Monte Carlo Dropout gives a useful approximation to epistemic uncertainty, but Ovadia et al. show that predictive uncertainty calibration still degrades under dataset shift, so it cannot serve as a standalone OOD reliability certificate for planner outputs. [source: https://arxiv.org/abs/1506.02142; https://arxiv.org/abs/1906.02530]
- [fact] Conformal prediction offers exact finite-sample coverage only under exchangeability, while adaptive online variants weaken the guarantee to long-run coverage frequency or local regret under evolving shift. [source: https://arxiv.org/abs/2107.07511; https://arxiv.org/abs/2106.00170; https://arxiv.org/abs/2208.08401]
- [inference] In a planner-tool loop, the formal guarantee is inherited from the weakest uncontrolled component, because recurrent tool use and verification can amplify a shifted observation before any correction arrives. [source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq4-2-adversarial-error-propagation.md; https://www.alexkulesza.com/pubs/adapt_mlj10.pdf]
- [inference] Manageable non-determinism is limited to tool regimes with support overlap, bounded or slowly varying shift, and independent correction or abstention, while open-world, adversarial, or regime-changing tool outputs remain formally unbounded. [source: https://arxiv.org/abs/2106.00170; https://arxiv.org/abs/2208.08401; https://proceedings.neurips.cc/paper/2021/hash/c5c1cb0bebd56ae38817b251ad72bedb-Abstract.html; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq4-2-adversarial-error-propagation.md]
- [inference] Current evidence supports deployment claims about calibrated abstention, set-valued prediction, or monitored online adaptation instead of guaranteed correctness for one chosen action under arbitrary production conditions. [source: https://arxiv.org/abs/2107.07511; https://arxiv.org/abs/2208.08401; https://arxiv.org/abs/1906.02530]

**Evidence map:**

- [fact] Arbitrary out-of-distribution generalisation is impossible without restricted shift, and conditional target-risk bounds require bounded divergence plus a low shared-error term. | source: https://proceedings.neurips.cc/paper/2021/hash/c5c1cb0bebd56ae38817b251ad72bedb-Abstract.html ; https://www.alexkulesza.com/pubs/adapt_mlj10.pdf | confidence: high | notes: impossibility plus bound conditions
- [inference] Tool-output randomness belongs mainly to the aleatoric uncertainty term, so it creates an irreducible uncertainty floor. | source: https://arxiv.org/abs/1703.04977 | confidence: low | notes: planner-tool classification
- [inference] Tool-using Large Language Model loops are better modelled as bounded-rational satisficers than as globally optimizing controllers. | source: https://www.nobelprize.org/uploads/2018/06/simon-lecture.pdf ; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq4-1-agentic-loop-explanatory-reach.md | confidence: medium | notes: decision frame
- [inference] Monte Carlo Dropout approximates epistemic uncertainty but does not remain a reliable OOD certificate under shift. | source: https://arxiv.org/abs/1506.02142 ; https://arxiv.org/abs/1906.02530 | confidence: medium | notes: approximation plus calibration decay
- [fact] Conformal prediction moves the guarantee from point correctness to coverage frequency, and online variants weaken it further to long-run or local-interval guarantees under shift. | source: https://arxiv.org/abs/2107.07511 ; https://arxiv.org/abs/2106.00170 ; https://arxiv.org/abs/2208.08401 | confidence: high | notes: set coverage not exact action correctness
- [inference] The planner-tool loop inherits the weakest uncontrolled surface, because recurrent interaction can amplify shifted observations before correction. | source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq4-2-adversarial-error-propagation.md ; https://www.alexkulesza.com/pubs/adapt_mlj10.pdf | confidence: medium | notes: composite weakest-link effect
- [inference] Only bounded, overlap-preserving, or independently corrected tool regimes admit useful guarantees; open-world or adversarial tool outputs do not. | source: https://arxiv.org/abs/2106.00170 ; https://arxiv.org/abs/2208.08401 ; https://proceedings.neurips.cc/paper/2021/hash/c5c1cb0bebd56ae38817b251ad72bedb-Abstract.html ; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq4-2-adversarial-error-propagation.md | confidence: medium | notes: assumption-sensitive boundary
- [inference] The best available deployment guarantee is about abstention, coverage, or monitored adaptation rather than exact correctness under arbitrary production conditions. | source: https://arxiv.org/abs/2107.07511 ; https://arxiv.org/abs/2208.08401 ; https://arxiv.org/abs/1906.02530 | confidence: medium | notes: operational interpretation

**Assumptions:**

- [assumption] General OOD and uncertainty-estimation results transfer qualitatively to the planner component of tool-using Large Language Model systems because the planning step still produces predictions from finite training distributions rather than from an explicit causal world model. [justification: the item asks for system-level formal limits, but the core mathematical results are still stated for predictive models rather than full agent loops; source: https://www.alexkulesza.com/pubs/adapt_mlj10.pdf; https://proceedings.neurips.cc/paper/2021/hash/c5c1cb0bebd56ae38817b251ad72bedb-Abstract.html; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq4-1-agentic-loop-explanatory-reach.md]
- [assumption] Tool responses can be treated as environment observations for the purpose of applying distribution-shift and online-calibration theory. [justification: the relevant mathematical question is whether deployment observations stay inside the assumptions used for calibration or adaptation; source: https://arxiv.org/abs/2107.07511; https://arxiv.org/abs/2208.08401]
- [assumption] The prior completed items accurately characterize the propagation surfaces of current multi-step planner-tool loops closely enough to support the weakest-link synthesis used here. [justification: this item reuses their structural decomposition rather than re-deriving it from fresh agent-case studies; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq4-1-agentic-loop-explanatory-reach.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq4-2-adversarial-error-propagation.md]

**Analysis:**

- [inference] The strongest evidence in this item is the combination of Ben-David's conditional target-risk bound and Ye's impossibility result, because together they say both when an OOD bound can exist and when it cannot. [source: https://www.alexkulesza.com/pubs/adapt_mlj10.pdf; https://proceedings.neurips.cc/paper/2021/hash/c5c1cb0bebd56ae38817b251ad72bedb-Abstract.html]
- [inference] The next strongest layer is the conformal literature, which does not solve arbitrary-shift correctness but does sharpen what kind of guarantee remains possible after exact correctness is abandoned in favour of set coverage or regret. [source: https://arxiv.org/abs/2107.07511; https://arxiv.org/abs/2106.00170; https://arxiv.org/abs/2208.08401]
- [inference] A rival interpretation is that better uncertainty estimation alone could rescue planner reliability, but Ovadia et al. show that calibration degrades under shift and Kendall and Gal explicitly separate irreducible aleatoric uncertainty from reducible epistemic uncertainty, so better epistemic estimates cannot erase stochastic tool noise. [source: https://arxiv.org/abs/1906.02530; https://arxiv.org/abs/1703.04977]
- [inference] Another rival interpretation is that agent loops can self-correct around tool randomness, but Research Question 4.2 makes that claim too strong because recurrent planning and verification can propagate the same corrupted observation when the correction channel is not independent. [source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq4-2-adversarial-error-propagation.md]
- [inference] The weakest part of the argument is the transfer from generic deep-learning theorems to full planner-tool stacks, which is why the final answer is framed as a conditional synthesis rather than as a new closed-form theorem for all agent architectures. [source: https://arxiv.org/abs/1906.02530; https://www.alexkulesza.com/pubs/adapt_mlj10.pdf; https://arxiv.org/abs/2208.08401]

**Risks, gaps, uncertainties:**

- [fact] No consulted primary source provides one unified theorem for full planner-tool loops with stochastic tools, recurrent verification, and arbitrary production shift, so the formal answer in this item is assembled from adjacent theories. [source: https://www.alexkulesza.com/pubs/adapt_mlj10.pdf; https://proceedings.neurips.cc/paper/2021/hash/c5c1cb0bebd56ae38817b251ad72bedb-Abstract.html; https://arxiv.org/abs/2208.08401]
- [inference] The cited uncertainty-estimation results come mainly from general predictive models rather than from live tool-using Large Language Model agents, so direct agent-specific calibration evidence remains thinner than the surrounding theory. [source: https://arxiv.org/abs/1506.02142; https://arxiv.org/abs/1703.04977; https://arxiv.org/abs/1906.02530]
- [inference] The manageable-versus-unmanageable boundary is clearest in theory for exchangeable, bounded-shift, or online-adaptive settings and less well benchmarked for real production tools that mix stochastic drift with adversarial contamination. [source: https://arxiv.org/abs/2106.00170; https://arxiv.org/abs/2208.08401; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq4-2-adversarial-error-propagation.md]

**Open questions:**

- [inference] What benchmark would best measure calibrated abstention quality for tool-using Large Language Model systems when tool outputs drift but remain non-adversarial? [source: https://arxiv.org/abs/2107.07511; https://arxiv.org/abs/2208.08401]
- [inference] How much independent error reduction do typed tool schemas, deterministic guardrails, or external verifiers provide relative to planner-only uncertainty estimation? [source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq4-2-adversarial-error-propagation.md; https://arxiv.org/abs/2208.08401]
- [inference] Can a future benchmark isolate the separate contributions of divergence, aleatoric tool noise, and verifier independence in one end-to-end planner-tool deployment setting? [source: https://www.alexkulesza.com/pubs/adapt_mlj10.pdf; https://arxiv.org/abs/1703.04977; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq4-2-adversarial-error-propagation.md]
### §7 Recursive Review

review_result: pass
acronym_audit: Out-of-Distribution (OOD), Large Language Model (LLM), Monte Carlo (MC)
domain_term_audit: bounded rationality, epistemic uncertainty, aleatoric uncertainty, and conformal prediction defined on first substantive use
claim_audit: all visible claims in Research Skill Output labeled as fact, inference, or assumption
findings_parity: matched to Section 6
confidence: medium

---

## Findings

### Executive Summary

Tool-using Large Language Model systems have no non-vacuous universal bound on generalisation outside the training distribution under unconstrained production conditions, because arbitrary out-of-distribution shift is impossible to bound without extra structural assumptions and stochastic tool outputs add irreducible uncertainty. [inference; source: https://proceedings.neurips.cc/paper/2021/hash/c5c1cb0bebd56ae38817b251ad72bedb-Abstract.html; https://www.alexkulesza.com/pubs/adapt_mlj10.pdf; https://arxiv.org/abs/1703.04977]

Current theory supports narrower guarantees: domain-adaptation target-risk bounds under bounded divergence and low shared error, approximate epistemic uncertainty estimates from methods such as Monte Carlo Dropout, and conformal coverage guarantees for set-valued outputs under exchangeable or adaptively tracked shift. [inference; source: https://www.alexkulesza.com/pubs/adapt_mlj10.pdf; https://arxiv.org/abs/1506.02142; https://arxiv.org/abs/2107.07511; https://arxiv.org/abs/2106.00170; https://arxiv.org/abs/2208.08401]

For the composite planner-tool loop, the decisive limit is the weakest uncontrolled surface, so open-world or adversarial tool outputs can make the classical bounds vacuous before the planner's internal uncertainty estimator becomes the binding constraint. [inference; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq4-2-adversarial-error-propagation.md; https://www.alexkulesza.com/pubs/adapt_mlj10.pdf; https://arxiv.org/abs/1906.02530]

Current theory therefore supports conditional risk management, abstention, and external correction for tool-using Large Language Model systems instead of guaranteed correctness on arbitrary production trajectories. [inference; source: https://arxiv.org/abs/2208.08401; https://arxiv.org/abs/2107.07511; https://www.nobelprize.org/uploads/2018/06/simon-lecture.pdf]

### Key Findings

1. **Arbitrary out-of-distribution generalisation is impossible without restricting the family of deployment shifts, and classical target-risk bounds remain conditional on bounded divergence between source and target domains plus a hypothesis that performs well on both.** ([fact]; high confidence; source: https://proceedings.neurips.cc/paper/2021/hash/c5c1cb0bebd56ae38817b251ad72bedb-Abstract.html; https://www.alexkulesza.com/pubs/adapt_mlj10.pdf)
2. **Non-deterministic tool outputs belong mainly to the aleatoric uncertainty term, so they create an irreducible error floor that additional planner training data or model scaling cannot remove on their own.** ([inference]; low confidence; source: https://arxiv.org/abs/1703.04977)
3. **Simon’s bounded-rationality frame describes tool-using Large Language Model loops more accurately than an omniscient optimization frame, which means their guarantees should be phrased as performance under partial information and finite computation rather than as exact optimal control.** ([inference]; medium confidence; source: https://www.nobelprize.org/uploads/2018/06/simon-lecture.pdf; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq4-1-agentic-loop-explanatory-reach.md)
4. **Monte Carlo Dropout provides a useful approximation to epistemic model uncertainty, but predictive uncertainty calibration still degrades under dataset shift, so the method cannot serve as a standalone out-of-distribution reliability certificate for planner outputs.** ([inference]; medium confidence; source: https://arxiv.org/abs/1506.02142; https://arxiv.org/abs/1906.02530)
5. **Conformal prediction gives exact finite-sample coverage only when calibration and test points satisfy its exchangeability assumptions, while adaptive online variants weaken the guarantee to long-run coverage frequency or local regret under evolving shift.** ([fact]; high confidence; source: https://arxiv.org/abs/2107.07511; https://arxiv.org/abs/2106.00170; https://arxiv.org/abs/2208.08401)
6. **In a planner-tool loop, the formal guarantee is inherited from the weakest uncontrolled component, because recurrent tool use and verification can amplify a shifted or semantically corrupted observation before any independent correction arrives.** ([inference]; medium confidence; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq4-2-adversarial-error-propagation.md; https://www.alexkulesza.com/pubs/adapt_mlj10.pdf)
7. **Manageable non-determinism is limited to tool regimes with support overlap, bounded or slowly varying shift, and independent correction or abstention, while open-world, adversarial, or regime-changing tool outputs remain formally unbounded.** ([inference]; medium confidence; source: https://arxiv.org/abs/2106.00170; https://arxiv.org/abs/2208.08401; https://proceedings.neurips.cc/paper/2021/hash/c5c1cb0bebd56ae38817b251ad72bedb-Abstract.html; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq4-2-adversarial-error-propagation.md)
8. **Current evidence supports deployment claims about calibrated abstention, set-valued prediction, or monitored online adaptation instead of guaranteed correctness for one chosen action under arbitrary production conditions.** ([inference]; medium confidence; source: https://arxiv.org/abs/2107.07511; https://arxiv.org/abs/2208.08401; https://arxiv.org/abs/1906.02530)

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [fact] Arbitrary out-of-distribution generalisation is impossible without restricted shift, and conditional target-risk bounds require bounded divergence plus a low shared-error term. | https://proceedings.neurips.cc/paper/2021/hash/c5c1cb0bebd56ae38817b251ad72bedb-Abstract.html; https://www.alexkulesza.com/pubs/adapt_mlj10.pdf | high | impossibility plus bound conditions |
| [inference] Tool-output randomness belongs mainly to the aleatoric uncertainty term, so it creates an irreducible uncertainty floor. | https://arxiv.org/abs/1703.04977 | low | planner-tool classification |
| [inference] Tool-using Large Language Model loops are better modelled as bounded-rational satisficers than as globally optimizing controllers. | https://www.nobelprize.org/uploads/2018/06/simon-lecture.pdf; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq4-1-agentic-loop-explanatory-reach.md | medium | decision frame |
| [inference] Monte Carlo Dropout approximates epistemic uncertainty but does not remain a reliable out-of-distribution certificate under shift. | https://arxiv.org/abs/1506.02142; https://arxiv.org/abs/1906.02530 | medium | approximation plus calibration decay |
| [fact] Conformal prediction moves the guarantee from point correctness to coverage frequency, and online variants weaken it further to long-run or local-interval guarantees under shift. | https://arxiv.org/abs/2107.07511; https://arxiv.org/abs/2106.00170; https://arxiv.org/abs/2208.08401 | high | set coverage not exact action correctness |
| [inference] The planner-tool loop inherits the weakest uncontrolled surface, because recurrent interaction can amplify shifted observations before correction. | https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq4-2-adversarial-error-propagation.md; https://www.alexkulesza.com/pubs/adapt_mlj10.pdf | medium | composite weakest-link effect |
| [inference] Only bounded, overlap-preserving, or independently corrected tool regimes admit useful guarantees; open-world or adversarial tool outputs do not. | https://arxiv.org/abs/2106.00170; https://arxiv.org/abs/2208.08401; https://proceedings.neurips.cc/paper/2021/hash/c5c1cb0bebd56ae38817b251ad72bedb-Abstract.html; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq4-2-adversarial-error-propagation.md | medium | assumption-sensitive boundary |
| [inference] Current evidence supports abstention, coverage, or monitored adaptation claims instead of exact-correctness claims under arbitrary production conditions. | https://arxiv.org/abs/2107.07511; https://arxiv.org/abs/2208.08401; https://arxiv.org/abs/1906.02530 | medium | operational interpretation |

### Assumptions

- The transfer from generic OOD theory to tool-using Large Language Model systems assumes that the planner component is still fundamentally a predictive model trained on finite distributions rather than an explicit causal world model. Justification: the cited mathematics is stated for predictive learners, so this item applies it to the planner layer rather than claiming a bespoke theorem for full agent stacks. [assumption; source: https://www.alexkulesza.com/pubs/adapt_mlj10.pdf; https://proceedings.neurips.cc/paper/2021/hash/c5c1cb0bebd56ae38817b251ad72bedb-Abstract.html; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq4-1-agentic-loop-explanatory-reach.md]
- Tool responses are treated as environment observations for the purpose of applying distribution-shift and online-calibration theory. Justification: the relevant guarantees depend on how deployment observations relate to training or calibration observations, regardless of whether the observation arrives from a human user or a tool call. [assumption; source: https://arxiv.org/abs/2107.07511; https://arxiv.org/abs/2208.08401]
- The prior completed items on loop reach and error propagation represent current multi-step planner-tool loops closely enough to support the weakest-link synthesis used here. Justification: this item reuses their structural decomposition of planning, tool use, and verification instead of re-deriving the same loop anatomy from new case studies. [assumption; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq4-1-agentic-loop-explanatory-reach.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq4-2-adversarial-error-propagation.md]

### Analysis

The strongest evidence in this item comes from combining Ben-David's conditional target-risk bound with Ye's impossibility result, because together they specify both the assumptions needed for a useful out-of-distribution guarantee and the reason arbitrary production shift makes that guarantee collapse. [inference; source: https://www.alexkulesza.com/pubs/adapt_mlj10.pdf; https://proceedings.neurips.cc/paper/2021/hash/c5c1cb0bebd56ae38817b251ad72bedb-Abstract.html]

The conformal literature is the next strongest layer because it clarifies what remains provable after exact correctness is abandoned in favour of set coverage or regret-style adaptation over time. [inference; source: https://arxiv.org/abs/2107.07511; https://arxiv.org/abs/2106.00170; https://arxiv.org/abs/2208.08401]

A rival interpretation is that better uncertainty estimation alone could rescue planner reliability, but Ovadia et al. show calibration degradation under shift and Kendall and Gal explicitly separate irreducible aleatoric uncertainty from reducible epistemic uncertainty, so better model confidence cannot erase stochastic tool noise. [inference; source: https://arxiv.org/abs/1906.02530; https://arxiv.org/abs/1703.04977]

Another rival interpretation is that agent loops can self-correct around tool randomness, but Research Question 4.2 makes that claim too strong because recurrent planning and verification can propagate the same shifted observation when the correction channel is not independent. [inference; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq4-2-adversarial-error-propagation.md]

The weakest part of the argument is the transfer from generic deep-learning theorems to full planner-tool stacks, which is why the answer is framed as a conditional synthesis of adjacent theories rather than as a new closed-form theorem for all agent architectures. [inference; source: https://arxiv.org/abs/1906.02530; https://www.alexkulesza.com/pubs/adapt_mlj10.pdf; https://arxiv.org/abs/2208.08401]

### Risks, Gaps, and Uncertainties

- No consulted primary source provides one unified theorem for full planner-tool loops with stochastic tools, recurrent verification, and arbitrary production shift, so the formal answer here is assembled from adjacent theories. [fact; source: https://www.alexkulesza.com/pubs/adapt_mlj10.pdf; https://proceedings.neurips.cc/paper/2021/hash/c5c1cb0bebd56ae38817b251ad72bedb-Abstract.html; https://arxiv.org/abs/2208.08401]
- The cited uncertainty-estimation results come mainly from general predictive models rather than from live tool-using Large Language Model agents, so direct agent-specific calibration evidence remains thinner than the surrounding theory. [inference; source: https://arxiv.org/abs/1506.02142; https://arxiv.org/abs/1703.04977; https://arxiv.org/abs/1906.02530]
- The manageable-versus-unmanageable boundary is theoretically clear for exchangeable, bounded-shift, or online-adaptive settings and less well benchmarked for real production tools that mix stochastic drift with adversarial contamination. [inference; source: https://arxiv.org/abs/2106.00170; https://arxiv.org/abs/2208.08401; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq4-2-adversarial-error-propagation.md]

### Open Questions

- What benchmark would best measure calibrated abstention quality for tool-using Large Language Model systems when tool outputs drift but remain non-adversarial? [inference; source: https://arxiv.org/abs/2107.07511; https://arxiv.org/abs/2208.08401]
- How much independent error reduction do typed tool schemas, deterministic guardrails, or external verifiers provide relative to planner-only uncertainty estimation? [inference; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq4-2-adversarial-error-propagation.md; https://arxiv.org/abs/2208.08401]
- Can a future benchmark isolate the separate contributions of divergence, aleatoric tool noise, and verifier independence in one end-to-end planner-tool deployment setting? [inference; source: https://www.alexkulesza.com/pubs/adapt_mlj10.pdf; https://arxiv.org/abs/1703.04977; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq4-2-adversarial-error-propagation.md]

---

## Output

- Type: knowledge
- Description: A synthesis showing that current formal theory gives tool-using Large Language Model systems only conditional out-of-distribution guarantees, with support centred on bounded-shift risk, calibrated abstention, and online adaptation rather than exact correctness under arbitrary production conditions. [inference; source: https://www.alexkulesza.com/pubs/adapt_mlj10.pdf; https://arxiv.org/abs/2107.07511; https://arxiv.org/abs/2208.08401]
- Links:
  - https://www.alexkulesza.com/pubs/adapt_mlj10.pdf
  - https://proceedings.neurips.cc/paper/2021/hash/c5c1cb0bebd56ae38817b251ad72bedb-Abstract.html
  - https://arxiv.org/abs/2208.08401
