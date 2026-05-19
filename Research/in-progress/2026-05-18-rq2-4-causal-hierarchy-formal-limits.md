---
title: "Research Question 2.4: Pearl's Causal Hierarchy and the formal limits of observational data for intervention and counterfactual reasoning"
added: 2026-05-18T19:40:00+00:00
status: reviewing
priority: high
blocks:
  - 2026-05-18-rq3-1-llm-statistical-vs-causal
tags: [causal-inference, machine-learning, formal-methods, epistemology, invariants]
started: 2026-05-19T09:32:53+00:00
completed: ~
output: [knowledge]
cites:
  - 2026-05-18-rq2-1-erm-causal-blindness
  - 2026-05-18-rq2-2-duhem-quine-underdetermination
  - 2026-05-18-rq2-3-predictive-model-fragility
related:
  - 2026-05-18-rq1-1-popper-falsifiability
  - 2026-05-18-rq1-3-instrumentalism-failure-modes
superseded_by: ~
supersedes: ~
item_type: synthesis
confidence: medium
versions: []
---

# Research Question 2.4: Pearl's Causal Hierarchy and the formal limits of observational data for intervention and counterfactual reasoning

## Research Question

What are the formal information-theoretic boundaries that prevent a model trained exclusively on observational data (Level 1 on Pearl's Ladder of Causation) from ever executing or predicting the outcomes of structural interventions (Level 2) or counterfactuals (Level 3)?

## Scope

**In scope:**
- Pearl's Ladder of Causation: Association (Level 1), Intervention (Level 2), Counterfactuals (Level 3)
- The Causal Hierarchy Theorem and its formal proof
- Information-theoretic lower bounds on what observational data can determine
- Observational vs. interventional distributions and the do-calculus
- Confounding bias as a mechanism preventing Level 1 to Level 2 inference

**Out of scope:**
- Practical causal discovery algorithms such as PC or Fast Causal Inference
- Specific applications of causal inference to medical trials or policy evaluation

**Constraints:** This is the synthesis item for Phase 2; it must integrate findings from Research Questions 2.1, 2.2, and 2.3 into one formal statement about the limits of observational learning.

## Context

Research Questions 2.1, 2.2, and 2.3 established that Empirical Risk Minimisation (ERM) can fit observational data while remaining blind to invariant structure, that finite evidence can leave multiple mechanisms observationally equivalent, and that proxy rules chosen under those conditions become fragile under perturbation. [fact; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq2-1-erm-causal-blindness.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq2-2-duhem-quine-underdetermination.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq2-3-predictive-model-fragility.md]

Pearl's Causal Hierarchy is the formal framework that separates those limits into three distinct query classes: observational, interventional, and counterfactual. [fact; source: https://causalai.net/r60.pdf; https://web.cs.ucla.edu/~kaoru/3-layer-causal-hierarchy.pdf]

This item therefore asks for the theorem-level synthesis of Phase 2: whether passive observational learning alone can determine the effects of actions or hypothetical alternatives, or whether extra structural assumptions and higher-layer evidence are required. [inference; source: https://causalai.net/r60.pdf; https://arxiv.org/abs/1801.04016; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq2-1-erm-causal-blindness.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq2-2-duhem-quine-underdetermination.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq2-3-predictive-model-fragility.md]

## Approach

1. Formally define all three levels of Pearl's Ladder of Causation: `P(Y | X)`, `P(Y | do(X))`, and counterfactual quantities such as `P(Y_x | X', Y')`.
2. State the Causal Hierarchy Theorem and identify what it proves about observational underdetermination of interventional and counterfactual distributions.
3. Characterise confounding bias as a concrete mechanism by which observational conditioning can mislead intervention prediction.
4. Formalise do-calculus, Pearl's three-rule system for converting intervention queries into observational ones when the graph makes that possible.
5. Apply the theorem to modern machine learning by locating passive ERM training at Level 1 and showing why higher-level answers require extra structure or extra data.

## Sources

- [x] [Bareinboim et al. (2022) On Pearl's Hierarchy and the Foundations of Causal Inference](https://causalai.net/r60.pdf) - primary source for the hierarchy definitions, the Causal Hierarchy Theorem, and the Markovian special case.
- [x] [Pearl (n.d.) The Three Layer Causal Hierarchy](https://web.cs.ucla.edu/~kaoru/3-layer-causal-hierarchy.pdf) - concise official table of Level 1, Level 2, and Level 3 query forms.
- [x] [Pearl (2018) Theoretical Impediments to Machine Learning With Seven Sparks from the Causal Revolution](https://arxiv.org/abs/1801.04016) - primary source on the limits of model-free learning for intervention and retrospection.
- [x] [Huang and Valtorta (2006) Pearl's Calculus of Intervention Is Complete](https://arxiv.org/pdf/1206.6831v1) - primary source proving the completeness of do-calculus for identifiable causal effects.
- [x] [Peters, Janzing, and Scholkopf (2017) Elements of Causal Inference](https://library.oapen.org/bitstream/id/056a11be-ce3a-44b9-8987-a6c68fce8d9b/11283.pdf) - open-access book used for intervention semantics and independent mechanisms.
- [x] [Research repo (2026-05-19) Research Question 2.1: Empirical Risk Minimisation's Causal Blindness and the Limits of In-Distribution Guarantees](https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq2-1-erm-causal-blindness.md) - prior repository item on ERM, invariance, and observational training limits.
- [x] [Research repo (2026-05-19) Research Question 2.2: The Duhem-Quine Thesis and Underdetermination, Quantifying When a Model Has Matched the True Mechanism](https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq2-2-duhem-quine-underdetermination.md) - prior repository item on observational equivalence and identifiability.
- [x] [Research repo (2026-05-19) Research Question 2.3: Structural Stability vs. Predictive Fragility, Dynamical Systems Theory and the Cost of Noise](https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq2-3-predictive-model-fragility.md) - prior repository item on perturbation fragility when invariant structure is missing.

---

## Research Skill Output

### §0 Initialise

- Question: What formal boundary separates observational learning from valid reasoning about interventions and counterfactuals?
- Scope: Pearl's three-layer hierarchy, the Causal Hierarchy Theorem, confounding, do-calculus, and the implication for passive machine learning.
- Constraints: full mode; this item must synthesise Research Questions 2.1, 2.2, and 2.3; every cited claim must have a URL-backed source.
- Output: executive summary, key findings, evidence map, assumptions, analysis, risks, gaps, uncertainties, and open questions.
- Prior completed items consulted: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq2-1-erm-causal-blindness.md ; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq2-2-duhem-quine-underdetermination.md ; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq2-3-predictive-model-fragility.md

### §1 Question Decomposition

1. Hierarchy definition
   1.1 What exactly is a Level 1 observational query?
   1.2 What exactly is a Level 2 intervention query?
   1.3 What exactly is a Level 3 counterfactual query?
2. Formal non-collapse
   2.1 What does the Causal Hierarchy Theorem state informally?
   2.2 What does the formal measure-zero statement add?
   2.3 What specific non-collapse claim holds between Level 1 and Level 2?
   2.4 What specific non-collapse claim holds between Level 2 and Level 3?
3. Obstruction mechanism
   3.1 Why can `P(Y | X)` differ from `P(Y | do(X))`?
   3.2 What role does unobserved confounding play in that difference?
   3.3 When does observational information become sufficient after all?
4. Cross-layer bridge
   4.1 What is do-calculus?
   4.2 What does it mean for do-calculus to be complete?
   4.3 What does completeness imply about the limits of pure observational data?
5. Phase 2 synthesis
   5.1 How does this theorem subsume Research Question 2.1 on ERM?
   5.2 How does this theorem subsume Research Question 2.2 on underdetermination?
   5.3 How does this theorem subsume Research Question 2.3 on fragility under perturbation?

### §2 Investigation

#### Access notes

- Access note: the seeded MIT Press bibliographic locator for *Elements of Causal Inference* was checked, and substantive claims were taken from the official open-access book file.
- Access note: the seeded Cambridge bibliographic locator for *Causality* and the seeded Basic Books page for *The Book of Why* were checked as book locators only; hierarchy and intervention claims below are taken from accessible Pearl, Bareinboim et al., Huang and Valtorta, and Peters et al. sources.

#### A. The three levels of the hierarchy

- [fact] Bareinboim et al. define Pearl's Causal Hierarchy as a three-level ordering of observational, interventional, and counterfactual concepts emerging from a Structural Causal Model (SCM). [source: https://causalai.net/r60.pdf]
- [fact] Their chapter states that Level 1 concerns purely observational information, Level 2 concerns what would happen under interventions, and Level 3 concerns what would have happened under hypothetical alternatives given what actually occurred. [source: https://causalai.net/r60.pdf]
- [fact] Pearl's UCLA note gives the canonical forms `P(y|x)` for association, `P(y|do(x), z)` for intervention, and `P(y_x|x', y')` for counterfactuals, while mapping them to the activities of seeing, doing, and imagining. [source: https://web.cs.ucla.edu/~kaoru/3-layer-causal-hierarchy.pdf]
- [fact] Bareinboim et al. define the interventional distribution by replacing the mechanism for `X` with a constant `x`, which severs the ordinary causes of `X` and makes `P(Y_x)` distinct from ordinary conditioning. [source: https://causalai.net/r60.pdf]
- [inference] The hierarchy is therefore not just a taxonomy of questions; it is a taxonomy of how much structure about the world must be known to answer those questions. [source: https://causalai.net/r60.pdf; https://web.cs.ucla.edu/~kaoru/3-layer-causal-hierarchy.pdf]

#### B. The Causal Hierarchy Theorem

- [fact] Bareinboim et al. state the Causal Hierarchy Theorem informally as the claim that the hierarchy almost never collapses, meaning that for almost any SCM the layers remain distinct. [source: https://causalai.net/r60.pdf]
- [fact] The same chapter states that the theorem's formal version says the subset of SCMs in which any collapse of the hierarchy occurs has measure zero with respect to the relevant encoding of Level 3 equivalence classes. [source: https://causalai.net/r60.pdf]
- [fact] Bareinboim et al. further state that Layer 2 never collapses to Layer 1, because for any SCM there is another SCM with the same Level 1 theory but a different Level 2 theory. [source: https://causalai.net/r60.pdf]
- [fact] They also argue that Level 3 almost never collapses to Level 2, so interventional information still generally underdetermines counterfactual structure. [source: https://causalai.net/r60.pdf]
- [inference] The theorem is an information-theoretic barrier because it says lower-layer data are generically insufficient even before one talks about a particular algorithm, parameterisation, or optimisation method. [source: https://causalai.net/r60.pdf]

#### C. Confounding and the observational/interventional gap

- [fact] Bareinboim et al. show in their treatment example that observational and interventional effects can differ in sign: `P(Y = 1 | X = 1) - P(Y = 1 | X = 0)` is positive while `P(Y = 1 | do(X = 1)) - P(Y = 1 | do(X = 0))` is negative. [source: https://causalai.net/r60.pdf]
- [fact] Pearl states that confounding, the presence of unobserved common causes, is the main obstacle to drawing causal conclusions from data, and that back-door adjustment and do-calculus are the tools for controlling it when the graph permits. [source: https://arxiv.org/abs/1801.04016]
- [fact] Bareinboim et al. prove that in Markovian models, meaning models without unobserved confounding, any interventional distribution is identifiable from Level 1 quantities through truncated factorization. [source: https://causalai.net/r60.pdf]
- [inference] Confounding is therefore not a peripheral nuisance around the hierarchy; it is the standard reason why ordinary observational conditioning fails to recover intervention effects. [source: https://causalai.net/r60.pdf; https://arxiv.org/abs/1801.04016]
- [inference] The no-unobserved-confounding case is a structured exception to the general theorem rather than a refutation of it, because it adds exactly the extra structural information the theorem says lower-layer data need. [source: https://causalai.net/r60.pdf]

#### D. Do-calculus as the bridge when identification is possible

- [fact] Huang and Valtorta define do-calculus as Pearl's three inference rules for transforming intervention expressions under graphical separation conditions. [source: https://arxiv.org/pdf/1206.6831v1]
- [fact] Their abstract states that if a causal effect is identifiable, then there exists a sequence of applications of the do-calculus rules that transforms the intervention formula into one containing only observational quantities. [source: https://arxiv.org/pdf/1206.6831v1]
- [fact] Their conclusion states that the three do-calculus rules, together with standard probability manipulations, are complete for determining identifiability of all effects `P_T(S)`. [source: https://arxiv.org/pdf/1206.6831v1]
- [fact] Bareinboim et al. explicitly describe do-calculus as the graphical structure that can bridge lower and higher layers when partial knowledge of the underlying model is available. [source: https://causalai.net/r60.pdf]
- [inference] Completeness means that when Level 2 information can be recovered from Level 1 information at all, the recovery depends on structural assumptions encoded in the graph, not on observational data alone. [source: https://arxiv.org/pdf/1206.6831v1; https://causalai.net/r60.pdf]

#### E. Relation to causal mechanisms and invariance

- [fact] Peters, Janzing, and Scholkopf argue that causal direction becomes plausible when interventions can change the distribution of a cause without changing the mechanism that maps cause to effect. [source: https://library.oapen.org/bitstream/id/056a11be-ce3a-44b9-8987-a6c68fce8d9b/11283.pdf]
- [fact] The same source states the principle of independent mechanisms: the causal generative process is composed of autonomous modules that do not inform or influence each other. [source: https://library.oapen.org/bitstream/id/056a11be-ce3a-44b9-8987-a6c68fce8d9b/11283.pdf]
- [fact] Pearl argues that current model-free machine learning systems operate almost exclusively in a statistical mode and cannot reason about interventions and retrospection. [source: https://arxiv.org/abs/1801.04016]
- [inference] A passive learner trained only on logged observations therefore receives Level 1 constraints on associations but not the mechanism-replacement semantics required for Level 2 or the alternate-world comparisons required for Level 3. [source: https://library.oapen.org/bitstream/id/056a11be-ce3a-44b9-8987-a6c68fce8d9b/11283.pdf; https://arxiv.org/abs/1801.04016; https://causalai.net/r60.pdf]

#### F. Cross-item integration with Phase 2

- [fact] Research Question 2.1 concluded that ERM controls prediction error under one observed distribution while remaining blind to the stable cause-and-effect relations needed after environment change. [source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq2-1-erm-causal-blindness.md]
- [fact] Research Question 2.2 concluded that finite observations can leave several rival mechanisms observationally equivalent until identifiability or intervention criteria break the tie. [source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq2-2-duhem-quine-underdetermination.md]
- [fact] Research Question 2.3 concluded that when the learned rule is not tied to invariant structure, perturbations can expose qualitative fragility rather than merely small numeric degradation. [source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq2-3-predictive-model-fragility.md]
- [inference] The Causal Hierarchy Theorem subsumes those three results in one formal statement: ERM's blindness, underdetermination, and perturbation fragility are all expected consequences of learning from Level 1 information without enough extra structure to identify higher-layer facts. [source: https://causalai.net/r60.pdf; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq2-1-erm-causal-blindness.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq2-2-duhem-quine-underdetermination.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq2-3-predictive-model-fragility.md]

### §3 Reasoning

- [fact] The Causal Hierarchy Theorem is not a universal impossibility theorem for all causal inference, because Bareinboim et al. also prove special cases in which graphical structure plus lower-layer data do identify intervention effects. [source: https://causalai.net/r60.pdf]
- [inference] The correct conclusion is therefore not that observational data are useless, but that observational data need additional structure before they can answer higher-layer questions. [source: https://causalai.net/r60.pdf; https://arxiv.org/pdf/1206.6831v1]
- [inference] The treatment-sign reversal example shows why the central distinction is semantic rather than numeric: conditioning reports how outcomes co-vary with observed treatment, while intervention reports what would happen if the treatment mechanism were replaced. [source: https://causalai.net/r60.pdf]
- [inference] This distinction explains why passive machine learning can appear highly successful on logged data and still be formally under-informed about the consequences of actions or counterfactual alternatives. [source: https://arxiv.org/abs/1801.04016; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq2-1-erm-causal-blindness.md]

### §4 Consistency Check

- [fact] Tension: Markovian models allow Level 1 data to identify Level 2 intervention distributions. [source: https://causalai.net/r60.pdf]
- [inference] Resolution: this does not contradict the Causal Hierarchy Theorem, because Markovianity removes unobserved confounding and supplies exactly the extra structural constraint that generic observational learning lacks. [source: https://causalai.net/r60.pdf; https://arxiv.org/abs/1801.04016]
- [fact] Tension: do-calculus can sometimes convert intervention queries into observational formulas. [source: https://arxiv.org/pdf/1206.6831v1]
- [inference] Resolution: completeness strengthens rather than weakens the main claim, because it says every successful reduction depends on structural conditions, and failure to satisfy those conditions leaves the higher-layer query unidentified. [source: https://arxiv.org/pdf/1206.6831v1; https://causalai.net/r60.pdf]
- [inference] Remaining uncertainty: the theorem locates what passive data cannot determine in principle, but it does not by itself specify how much multi-environment or experimental evidence is enough in any particular modern machine-learning system. [source: https://causalai.net/r60.pdf; https://library.oapen.org/bitstream/id/056a11be-ce3a-44b9-8987-a6c68fce8d9b/11283.pdf]

### §5 Depth and Breadth Expansion

- [inference] Technical lens: the hierarchy separates three different probability objects, `P(y|x)`, `P(y|do(x))`, and `P(y_x|x', y')`, so an apparently small notation change actually changes the information required to answer the question. [source: https://web.cs.ucla.edu/~kaoru/3-layer-causal-hierarchy.pdf; https://causalai.net/r60.pdf]
- [inference] Historical lens: Pearl's presentation of seeing, doing, and imagining makes the theorem intelligible because it ties formal probability objects to increasingly demanding cognitive tasks. [source: https://web.cs.ucla.edu/~kaoru/3-layer-causal-hierarchy.pdf]
- [inference] Epistemic lens: Research Questions 2.1, 2.2, and 2.3 can be re-read as special cases of one broader identifiability problem, namely that observational success does not certify action-sensitive or counterfactual truth. [source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq2-1-erm-causal-blindness.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq2-2-duhem-quine-underdetermination.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq2-3-predictive-model-fragility.md; https://causalai.net/r60.pdf]
- [inference] Operational lens: any deployment pipeline that trains only on passive logs inherits a formal capability ceiling unless it also injects structural assumptions, intervention data, or environment variation rich enough to identify higher-layer relations. [source: https://arxiv.org/abs/1801.04016; https://arxiv.org/pdf/1206.6831v1; https://library.oapen.org/bitstream/id/056a11be-ce3a-44b9-8987-a6c68fce8d9b/11283.pdf]

### §6 Synthesis

**Executive summary:**

- [inference] Observational data alone do not determine intervention or counterfactual answers in general; Pearl's Causal Hierarchy makes that limit theorem-level by showing that lower-layer data almost always underdetermine higher-layer facts. [source: https://causalai.net/r60.pdf]
- [fact] The hierarchy distinguishes association, intervention, and counterfactual reasoning through the probability objects `P(y|x)`, `P(y|do(x), z)`, and `P(y_x|x', y')`, each of which requires strictly richer structural information than the previous one in the generic case. [source: https://web.cs.ucla.edu/~kaoru/3-layer-causal-hierarchy.pdf; https://causalai.net/r60.pdf]
- [fact] Unobserved confounding is the standard mechanism behind the gap between conditioning and intervention, while Markovian no-confounding models and do-calculus identify the exceptional cases in which the gap can be bridged. [source: https://causalai.net/r60.pdf; https://arxiv.org/abs/1801.04016; https://arxiv.org/pdf/1206.6831v1]
- [inference] This theorem unifies Research Questions 2.1, 2.2, and 2.3 because ERM's causal blindness, observational underdetermination, and perturbation fragility are all what one should expect from learning that never leaves Level 1. [source: https://causalai.net/r60.pdf; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq2-1-erm-causal-blindness.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq2-2-duhem-quine-underdetermination.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq2-3-predictive-model-fragility.md]

**Key findings:**

1. [fact] High confidence: Pearl's Causal Hierarchy distinguishes three query classes, association, intervention, and counterfactuals, by the forms `P(y|x)`, `P(y|do(x), z)`, and `P(y_x|x', y')`, and each class corresponds to a different kind of causal information. [source: https://web.cs.ucla.edu/~kaoru/3-layer-causal-hierarchy.pdf; https://causalai.net/r60.pdf]
2. [fact] High confidence: the Causal Hierarchy Theorem states that the hierarchy almost never collapses, and formally that the subset of Structural Causal Models in which any collapse occurs has measure zero. [source: https://causalai.net/r60.pdf]
3. [fact] High confidence: Level 2 never collapses to Level 1, because for any Structural Causal Model there exists another model with the same observational theory but a different intervention theory. [source: https://causalai.net/r60.pdf]
4. [fact] Medium confidence: Level 3 almost never collapses to Level 2, so even interventional information generally underdetermines counterfactual structure unless additional assumptions are supplied. [source: https://causalai.net/r60.pdf]
5. [fact] High confidence: unobserved confounding can make observational conditioning disagree with intervention effects, including reversing the apparent sign of treatment benefit in the worked example given by Bareinboim et al. [source: https://causalai.net/r60.pdf]
6. [fact] High confidence: do-calculus is complete for identifiable causal effects, meaning every successful reduction of an intervention query to observational quantities can be derived by Pearl's three rules together with standard probability manipulations. [source: https://arxiv.org/pdf/1206.6831v1]
7. [inference] Medium confidence: passive machine-learning systems trained only on logged observations are normally confined to Level 1 unless they are given extra structural assumptions, intervention data, or sufficiently rich environment variation. [source: https://arxiv.org/abs/1801.04016; https://library.oapen.org/bitstream/id/056a11be-ce3a-44b9-8987-a6c68fce8d9b/11283.pdf; https://arxiv.org/pdf/1206.6831v1]
8. [inference] Medium confidence: Research Question 2.1's result on ERM follows as the learning-theoretic face of the theorem, because observational risk control does not identify intervention-sensitive structure. [source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq2-1-erm-causal-blindness.md; https://causalai.net/r60.pdf]
9. [inference] Medium confidence: Research Question 2.2's underdetermination result follows as the epistemic face of the theorem, because observational equivalence classes persist whenever higher-layer facts are not identified. [source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq2-2-duhem-quine-underdetermination.md; https://causalai.net/r60.pdf]
10. [inference] Medium confidence: Research Question 2.3's fragility result follows as the dynamical face of the theorem, because rules chosen from Level 1 information alone can remain observationally adequate while failing once interventions or perturbations expose the missing mechanism. [source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq2-3-predictive-model-fragility.md; https://causalai.net/r60.pdf]

**Evidence map:**

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [fact] The hierarchy is formally divided into association, intervention, and counterfactual query classes. | https://web.cs.ucla.edu/~kaoru/3-layer-causal-hierarchy.pdf ; https://causalai.net/r60.pdf | high | Definitions |
| [fact] The Causal Hierarchy Theorem says hierarchy collapse occurs only on a measure-zero subset of models. | https://causalai.net/r60.pdf | high | Formal theorem |
| [fact] Level 2 never collapses to Level 1. | https://causalai.net/r60.pdf | high | Stronger special-case statement |
| [fact] Level 3 almost never collapses to Level 2. | https://causalai.net/r60.pdf | medium | Generic non-collapse |
| [fact] Confounding can reverse the sign between observational and interventional treatment effects. | https://causalai.net/r60.pdf | high | Worked example |
| [fact] Do-calculus is complete for identifiable causal effects. | https://arxiv.org/pdf/1206.6831v1 | high | Completeness proof |
| [inference] Passive machine learning is usually confined to Level 1 without extra structural information. | https://arxiv.org/abs/1801.04016 ; https://library.oapen.org/bitstream/id/056a11be-ce3a-44b9-8987-a6c68fce8d9b/11283.pdf ; https://arxiv.org/pdf/1206.6831v1 | medium | Synthesis across causal and learning sources |
| [inference] Research Question 2.1 is the ERM expression of the theorem. | https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq2-1-erm-causal-blindness.md ; https://causalai.net/r60.pdf | medium | Cross-item integration |
| [inference] Research Question 2.2 is the underdetermination expression of the theorem. | https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq2-2-duhem-quine-underdetermination.md ; https://causalai.net/r60.pdf | medium | Cross-item integration |
| [inference] Research Question 2.3 is the fragility expression of the theorem. | https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq2-3-predictive-model-fragility.md ; https://causalai.net/r60.pdf | medium | Cross-item integration |

**Assumptions:**

- [assumption] The passive machine-learning application in this item is about systems trained only on observational traces and evaluated without explicit intervention semantics, not about every possible interactive learning setup. [source: https://arxiv.org/abs/1801.04016; https://library.oapen.org/bitstream/id/056a11be-ce3a-44b9-8987-a6c68fce8d9b/11283.pdf]
- [assumption] The prior repository items correctly represent the portions of Phase 2 they summarise here, because this item uses them as completed syntheses rather than re-deriving every subordinate proof from scratch. [source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq2-1-erm-causal-blindness.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq2-2-duhem-quine-underdetermination.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq2-3-predictive-model-fragility.md]

**Analysis:**

- [inference] The strongest part of the case is the negative theorem-level claim, because the hierarchy definitions, the Causal Hierarchy Theorem, the Markovian exception, and the completeness of do-calculus all come from primary technical sources. [source: https://causalai.net/r60.pdf; https://arxiv.org/pdf/1206.6831v1]
- [inference] The key trade-off is between generic impossibility and structured identifiability: without assumptions the hierarchy does not collapse, but with the right graphical constraints some intervention queries do become observationally identifiable. [source: https://causalai.net/r60.pdf; https://arxiv.org/pdf/1206.6831v1]
- [inference] A rival interpretation would say that better optimisation, bigger models, or more data might dissolve the barrier, but the theorem blocks that move because it is about what lower-layer information determines, not about how efficiently an algorithm uses it. [source: https://causalai.net/r60.pdf; https://arxiv.org/abs/1801.04016]
- [inference] The Phase 2 synthesis is therefore coherent: ERM's blind spot, observational underdetermination, and perturbation fragility are not three unrelated failures, but one generic consequence of trying to answer higher-layer questions with lower-layer evidence. [source: https://causalai.net/r60.pdf; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq2-1-erm-causal-blindness.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq2-2-duhem-quine-underdetermination.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq2-3-predictive-model-fragility.md]

**Risks, gaps, uncertainties:**

- [inference] The exact size of the practical evidence budget needed to identify a higher-layer query in any specific machine-learning application remains outside this item's scope, because the theorem gives a generic non-collapse result rather than a task-by-task sample-complexity bound. [source: https://causalai.net/r60.pdf]
- [inference] The machine-learning conclusion is medium confidence rather than high confidence because it combines the theorem with broader learning-theory interpretation, even though Pearl's paper strongly supports the negative direction. [source: https://arxiv.org/abs/1801.04016; https://causalai.net/r60.pdf]
- [inference] The counterfactual non-collapse claim is strong at the theorem level but thinner at the worked-example level in this item, because the main accessible source is the theorem chapter rather than a separate family of open-access counterfactual case studies. [source: https://causalai.net/r60.pdf]

**Open questions:**

- What minimum combination of interventions, environment changes, or structural assumptions is enough to identify action-relevant structure in current foundation-model systems?
- Which benchmark family best distinguishes genuine Level 2 competence from improved Level 1 pattern matching under richer observational coverage?
- How should one measure partial progress toward Level 3 counterfactual competence in systems that can answer some intervention queries but still lack stable unit-level counterfactual grounding?

### §7 Recursive Review

- Review result: pass
- Acronym audit: pass
- Claim-label audit: pass
- Findings and synthesis parity: aligned
- Prior-work cross-check: Research Questions 2.1, 2.2, and 2.3 cited directly; Research Questions 1.1 and 1.3 retained as related context only
- Confidence assessment: medium, because the theorem-level results are strong but the machine-learning application remains partly inferential

---

## Findings

### Executive Summary

Observational data alone do not determine intervention or counterfactual answers in general, because Pearl's Causal Hierarchy shows that lower-layer data almost always underdetermine higher-layer facts. [inference; source: https://causalai.net/r60.pdf]

The hierarchy distinguishes association, intervention, and counterfactual reasoning through the probability objects `P(y|x)`, `P(y|do(x), z)`, and `P(y_x|x', y')`, and those objects require progressively richer structural information in the generic case. [fact; source: https://web.cs.ucla.edu/~kaoru/3-layer-causal-hierarchy.pdf; https://causalai.net/r60.pdf]

Unobserved confounding is the standard mechanism behind the gap between conditioning and intervention, while Markovian no-confounding models and do-calculus identify the exceptional cases in which that gap can be bridged. [fact; source: https://causalai.net/r60.pdf; https://arxiv.org/abs/1801.04016; https://arxiv.org/pdf/1206.6831v1]

This theorem unifies Research Questions 2.1, 2.2, and 2.3 because ERM's causal blindness, observational underdetermination, and perturbation fragility are all what one should expect from learning that never leaves Level 1. [inference; source: https://causalai.net/r60.pdf; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq2-1-erm-causal-blindness.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq2-2-duhem-quine-underdetermination.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq2-3-predictive-model-fragility.md]

### Key Findings

1. **Pearl's Causal Hierarchy distinguishes three query classes, association, intervention, and counterfactuals, by the forms `P(y|x)`, `P(y|do(x), z)`, and `P(y_x|x', y')`, and each class corresponds to a different kind of causal information rather than a different notation for the same information.** ([fact]; high confidence; source: https://web.cs.ucla.edu/~kaoru/3-layer-causal-hierarchy.pdf; https://causalai.net/r60.pdf)
2. **The Causal Hierarchy Theorem states that the hierarchy almost never collapses, and formally that the subset of Structural Causal Models in which any collapse occurs has measure zero, so lower-layer data generically fail to determine higher-layer facts.** ([fact]; high confidence; source: https://causalai.net/r60.pdf)
3. **Level 2 never collapses to Level 1, because for any Structural Causal Model there exists another model with the same observational theory but a different intervention theory, which means observational equivalence is never enough to fix causal effects by itself.** ([fact]; high confidence; source: https://causalai.net/r60.pdf)
4. **Level 3 almost never collapses to Level 2, so even a system that knows intervention distributions still generally lacks enough information to answer unit-level alternate-world questions without additional assumptions or richer model structure.** ([fact]; medium confidence; source: https://causalai.net/r60.pdf)
5. **Unobserved confounding can make observational conditioning disagree with intervention effects, including reversing the apparent sign of treatment benefit in Bareinboim et al.'s worked example, which shows that `P(Y|X)` and `P(Y|do(X))` are not interchangeable objects.** ([fact]; high confidence; source: https://causalai.net/r60.pdf)
6. **Do-calculus is complete for identifiable causal effects, meaning every successful reduction of an intervention query to observational quantities can be derived by Pearl's three rules together with standard probability manipulations, so identifiability depends on structure rather than on ad hoc algebraic tricks.** ([fact]; high confidence; source: https://arxiv.org/pdf/1206.6831v1)
7. **Passive machine-learning systems trained only on logged observations are normally confined to Level 1 unless they are given extra structural assumptions, intervention data, or sufficiently rich environment variation, because passive fitting does not itself supply mechanism-replacement semantics or counterfactual world comparisons.** ([inference]; medium confidence; source: https://arxiv.org/abs/1801.04016; https://library.oapen.org/bitstream/id/056a11be-ce3a-44b9-8987-a6c68fce8d9b/11283.pdf; https://arxiv.org/pdf/1206.6831v1)
8. **Research Question 2.1's result on ERM follows as the learning-theoretic face of the theorem, because controlling observational risk under one distribution does not identify the intervention-sensitive structure needed to remain correct when the environment changes.** ([inference]; medium confidence; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq2-1-erm-causal-blindness.md; https://causalai.net/r60.pdf)
9. **Research Question 2.2's underdetermination result follows as the epistemic face of the theorem, because observational equivalence classes persist whenever higher-layer facts are not identified and several mechanisms remain compatible with the same traces.** ([inference]; medium confidence; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq2-2-duhem-quine-underdetermination.md; https://causalai.net/r60.pdf)
10. **Research Question 2.3's fragility result follows as the dynamical face of the theorem, because rules chosen from Level 1 information alone can remain observationally adequate while failing once interventions or perturbations expose the missing mechanism that the learner never had enough information to recover.** ([inference]; medium confidence; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq2-3-predictive-model-fragility.md; https://causalai.net/r60.pdf)

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [fact] The hierarchy is formally divided into association, intervention, and counterfactual query classes. | https://web.cs.ucla.edu/~kaoru/3-layer-causal-hierarchy.pdf ; https://causalai.net/r60.pdf | high | Definitions |
| [fact] The Causal Hierarchy Theorem says hierarchy collapse occurs only on a measure-zero subset of models. | https://causalai.net/r60.pdf | high | Formal theorem |
| [fact] Level 2 never collapses to Level 1. | https://causalai.net/r60.pdf | high | Stronger special-case statement |
| [fact] Level 3 almost never collapses to Level 2. | https://causalai.net/r60.pdf | medium | Generic non-collapse |
| [fact] Confounding can reverse the sign between observational and interventional treatment effects. | https://causalai.net/r60.pdf | high | Worked example |
| [fact] Do-calculus is complete for identifiable causal effects. | https://arxiv.org/pdf/1206.6831v1 | high | Completeness proof |
| [inference] Passive machine learning is usually confined to Level 1 without extra structural information. | https://arxiv.org/abs/1801.04016 ; https://library.oapen.org/bitstream/id/056a11be-ce3a-44b9-8987-a6c68fce8d9b/11283.pdf ; https://arxiv.org/pdf/1206.6831v1 | medium | Cross-source synthesis |
| [inference] Research Question 2.1 is the ERM expression of the theorem. | https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq2-1-erm-causal-blindness.md ; https://causalai.net/r60.pdf | medium | Cross-item integration |
| [inference] Research Question 2.2 is the underdetermination expression of the theorem. | https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq2-2-duhem-quine-underdetermination.md ; https://causalai.net/r60.pdf | medium | Cross-item integration |
| [inference] Research Question 2.3 is the fragility expression of the theorem. | https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq2-3-predictive-model-fragility.md ; https://causalai.net/r60.pdf | medium | Cross-item integration |

### Assumptions

- The passive machine-learning application in this item is about systems trained only on observational traces and evaluated without explicit intervention semantics, not about every possible interactive learning setup. [assumption; source: https://arxiv.org/abs/1801.04016; https://library.oapen.org/bitstream/id/056a11be-ce3a-44b9-8987-a6c68fce8d9b/11283.pdf]
- The prior repository items correctly represent the portions of Phase 2 they summarise here, because this item uses them as completed syntheses rather than re-deriving every subordinate proof from scratch. [assumption; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq2-1-erm-causal-blindness.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq2-2-duhem-quine-underdetermination.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq2-3-predictive-model-fragility.md]

### Analysis

The strongest part of the case is the negative theorem-level claim, because the hierarchy definitions, the Causal Hierarchy Theorem, the Markovian exception, and the completeness of do-calculus all come from primary technical sources. [inference; source: https://causalai.net/r60.pdf; https://arxiv.org/pdf/1206.6831v1]

The central trade-off is between generic impossibility and structured identifiability: without assumptions the hierarchy does not collapse, but with the right graphical constraints some intervention queries do become observationally identifiable. [inference; source: https://causalai.net/r60.pdf; https://arxiv.org/pdf/1206.6831v1]

A rival interpretation would say that better optimisation, larger models, or more data might dissolve the barrier, but the theorem blocks that move because it is about what lower-layer information determines, not about how efficiently an algorithm uses that information. [inference; source: https://causalai.net/r60.pdf; https://arxiv.org/abs/1801.04016]

The Phase 2 synthesis is therefore coherent: ERM's blind spot, observational underdetermination, and perturbation fragility are not three unrelated failures, but one generic consequence of trying to answer higher-layer questions with lower-layer evidence. [inference; source: https://causalai.net/r60.pdf; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq2-1-erm-causal-blindness.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq2-2-duhem-quine-underdetermination.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq2-3-predictive-model-fragility.md]

### Risks, Gaps, and Uncertainties

- The exact size of the practical evidence budget needed to identify a higher-layer query in any specific machine-learning application remains outside this item's scope, because the theorem gives a generic non-collapse result rather than a task-by-task sample-complexity bound. [inference; source: https://causalai.net/r60.pdf]
- The machine-learning conclusion is medium confidence rather than high confidence because it combines the theorem with broader learning-theory interpretation, even though Pearl's paper strongly supports the negative direction. [inference; source: https://arxiv.org/abs/1801.04016; https://causalai.net/r60.pdf]
- The counterfactual non-collapse claim is strong at the theorem level but thinner at the worked-example level in this item, because the main accessible source is the theorem chapter rather than a separate family of open-access counterfactual case studies. [inference; source: https://causalai.net/r60.pdf]

### Open Questions

- What minimum combination of interventions, environment changes, or structural assumptions is enough to identify action-relevant structure in current foundation-model systems?
- Which benchmark family best distinguishes genuine Level 2 competence from improved Level 1 pattern matching under richer observational coverage?
- How should one measure partial progress toward Level 3 counterfactual competence in systems that can answer some intervention queries but still lack stable unit-level counterfactual grounding?

---

## Output

- Type: knowledge
- Description: Formal synthesis showing that Pearl's hierarchy makes the limits of passive observational learning theorem-level rather than intuitive, and that Research Questions 2.1, 2.2, and 2.3 are three faces of the same lower-layer information barrier. [inference; source: https://causalai.net/r60.pdf; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq2-1-erm-causal-blindness.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq2-2-duhem-quine-underdetermination.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq2-3-predictive-model-fragility.md]
- Links:
  - https://causalai.net/r60.pdf
  - https://arxiv.org/pdf/1206.6831v1
  - https://web.cs.ucla.edu/~kaoru/3-layer-causal-hierarchy.pdf
