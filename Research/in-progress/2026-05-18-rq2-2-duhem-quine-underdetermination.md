---
review_count: 1
title: "Research Question 2.2: The Duhem-Quine thesis and underdetermination, quantifying when a model has matched the true mechanism"
added: 2026-05-18T19:40:00+00:00
status: reviewing
priority: high
blocks:
  - 2026-05-18-rq2-4-causal-hierarchy-formal-limits
tags: [epistemology, philosophy-of-science, machine-learning, causal-inference, invariants]
started: 2026-05-19T08:32:59+00:00
completed: ~
output: [knowledge]
cites:
  - 2026-05-18-rq2-1-erm-causal-blindness
  - 2026-05-18-rq1-1-popper-falsifiability
  - 2026-05-18-rq1-3-instrumentalism-failure-modes
related:
  - 2026-05-18-rq2-3-predictive-model-fragility
  - 2026-05-18-rq2-4-causal-hierarchy-formal-limits
superseded_by: ~
supersedes: ~
item_type: primary
confidence: medium
versions: []
---

# Research Question 2.2: The Duhem-Quine thesis and underdetermination, quantifying when a model has matched the true mechanism

## Research Question

How can the phenomenon of multiple distinct functions perfectly interpolating identical data points be formalised through the lens of the Duhem-Quine thesis, underdetermination of theory by data, and what are the quantitative metrics for evaluating when a model has matched the true mechanism rather than an observationally equivalent proxy?

## Scope

**In scope:**
- Duhem-Quine underdetermination as a formal characterisation of the model-selection problem
- Observational equivalence in dynamical systems, multiple models producing identical outputs from identical inputs
- Structural identifiability as a formal criterion for distinguishing true mechanisms from proxies
- Quantitative metrics and identifiability conditions for mechanism matching

**Out of scope:**
- General philosophy of science debates about scientific realism
- Practical model-selection heuristics without formal grounding

**Constraints:** Builds directly on Research Question 2.1's Empirical Risk Minimisation (ERM) analysis; must provide quantitative criteria rather than a purely philosophical framing.

## Context

Research Question 2.1 established that Empirical Risk Minimisation (ERM) can select predictors that are observationally accurate inside the training distribution while remaining causally wrong under environment change. [fact; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq2-1-erm-causal-blindness.md]

This item asks when that empirical ambiguity should be understood as a general underdetermination problem, namely when the available observations fail to identify a unique mechanism among observationally equivalent alternatives. [inference; source: https://plato.stanford.edu/entries/scientific-underdetermination/; https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1891254/; https://opus.bibliothek.uni-augsburg.de/opus4/files/113236/113236.pdf]

The practical goal is to state quantitative criteria for "mechanism matched" rather than "curve-fit matched", and to test whether standard deep-learning models satisfy those criteria by default. [inference; source: https://opus.bibliothek.uni-augsburg.de/opus4/files/113236/113236.pdf; https://arxiv.org/abs/1801.04016; https://arxiv.org/abs/2112.12982]

## Approach

1. State the Duhem-Quine thesis formally: for any finite dataset, many theories are consistent with the data.
2. Formalise observational equivalence in dynamical systems using the Bongard-Lipson framework.
3. Survey structural identifiability theory: under what conditions does a dynamical system's parameters uniquely determine its observable outputs, and vice versa?
4. Develop quantitative criteria for mechanism identification beyond observational accuracy.
5. Apply the framework: can deep-learning models satisfy structural identifiability conditions?

## Sources

- [x] [Quine (1951) Two Dogmas of Empiricism, accessible text](https://www.theologie.uzh.ch/dam/jcr:ffffffff-fbd6-1538-0000-000070cf64bc/Quine51.pdf) - primary source for Quine's confirmation holism, especially the claim that statements face experience as a corporate body.
- [x] [Stanford Encyclopedia of Philosophy (2017) Scientific Underdetermination](https://plato.stanford.edu/entries/scientific-underdetermination/) - authoritative secondary source distinguishing holist and contrastive underdetermination and locating Duhem and Quine within that debate.
- [x] [Bongard and Lipson (2007) Automated reverse engineering of nonlinear dynamical systems](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1891254/) - accessible full text for active probing, candidate-model disagreement, and symbolic mechanism discovery in nonlinear ordinary differential equation (ODE) systems.
- [x] [Raue et al. (2009) Structural and practical identifiability analysis of partially observed dynamical models by exploiting the profile likelihood](https://opus.bibliothek.uni-augsburg.de/opus4/files/113236/113236.pdf) - accessible full text for structural identifiability, practical identifiability, and finite confidence-interval criteria.
- [x] [Peters, Buhlmann, and Meinshausen (2015) Causal inference using invariant prediction: identification and confidence intervals](https://arxiv.org/abs/1501.01332) - accessible source for invariance as a mechanism-sensitive criterion under interventions and environment change.
- [x] [Pearl (2018) Theoretical Impediments to Machine Learning With Seven Sparks from the Causal Revolution](https://arxiv.org/abs/1801.04016) - accessible source on the limit of purely associational learning for intervention questions.
- [x] [Scholkopf et al. (2021) Toward Causal Representation Learning](https://arxiv.org/abs/2102.11107) - accessible review connecting independently and identically distributed (i.i.d.) learning, interventions, and causal mechanisms.
- [x] [Bona-Pellissier et al. (2023) Parameter identifiability of a deep feedforward rectified linear unit (ReLU) neural network](https://arxiv.org/abs/2112.12982) - accessible source on when deep-network parameters are identifiable modulo known symmetries.
- [x] [Shen (2024) Exploring the Complexity of Deep Neural Networks through Functional Equivalence](https://proceedings.mlr.press/v235/shen24a.html) - accessible source showing that different parameterisations can implement the same neural-network function.
- [x] [Jensen (2024) Computational Methods lecture notes, polynomial interpolation](https://maxjensen.github.io/Computational_Methods_lecture_notes/4.1_interpolation.html) - accessible source for the existence and uniqueness theorem inside the restricted polynomial class.
- [x] [Research repo (2026-05-18) Research Question 2.1: Empirical Risk Minimisation's causal blindness and the limits of in-distribution guarantees](https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq2-1-erm-causal-blindness.md) - directly preceding item that this question sharpens.
- [x] [Research repo (2026-05-18) Research Question 1.1: Formalising Popper's falsifiability as a criterion between mechanism and interpolation](https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq1-1-popper-falsifiability.md) - prior repository item on mechanism versus interpolation.
- [x] [Research repo (2026-05-18) Research Question 1.3: Failure modes of instrumentalism when applied to complex dynamic systems under distribution shift](https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq1-3-instrumentalism-failure-modes.md) - prior repository item on predictive success without mechanistic robustness.

---

## Research Skill Output

### §0 Initialise

- Question: When do identical observations underdetermine the underlying mechanism, and what quantitative tests justify the stronger claim that a model has matched the true mechanism?
- Scope: Duhem-Quine underdetermination, observational equivalence in dynamical systems, structural and practical identifiability, invariance-based causal criteria, and applicability to deep learning.
- Constraints: mathematical treatment required; must connect to Research Question 2.1; URL-backed citations only; canonical tags only.
- Output: executive summary, key findings, evidence map, assumptions, analysis, risks, gaps, uncertainties, and open questions.
- Prior completed items consulted: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq2-1-erm-causal-blindness.md ; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq1-1-popper-falsifiability.md ; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq1-3-instrumentalism-failure-modes.md

### §1 Question Decomposition

1. Duhem-Quine formalisation
   1.1 What does Quine's confirmation holism say about testing hypotheses?
   1.2 How does the underdetermination literature distinguish holist and contrastive forms?
   1.3 How does finite interpolation ambiguity instantiate contrastive underdetermination?
2. Observational equivalence in dynamical systems
   2.1 When can multiple candidate mechanisms explain the same observed trajectories?
   2.2 What role do perturbations and extra observables play in separating those candidates?
3. Quantitative mechanism criteria
   3.1 What is structural identifiability?
   3.2 What is practical identifiability?
   3.3 Which confidence or invariance tests matter for mechanism claims?
4. Causal adequacy beyond fit
   4.1 Why is observational accuracy insufficient for mechanism matching?
   4.2 Which intervention or multi-environment conditions make a stronger claim possible?
5. Deep-learning applicability
   5.1 Do standard deep neural networks have unique mechanism-bearing parameters?
   5.2 Under what restrictions can deep models become identifiable, and what remains unresolved?

### §2 Investigation

#### Access notes

- Seeded Quine Digital Object Identifier (DOI), inaccessible; substituted accessible text: https://www.theologie.uzh.ch/dam/jcr:ffffffff-fbd6-1538-0000-000070cf64bc/Quine51.pdf
- Seeded Bongard Digital Object Identifier (DOI), inaccessible; substituted accessible full text: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1891254/
- Seeded Raue Digital Object Identifier (DOI), inaccessible; substituted accessible repository file: https://opus.bibliothek.uni-augsburg.de/opus4/files/113236/113236.pdf
- Seeded Peters, Janzing, and Schölkopf book locator verified at https://is.mpg.de/publications/petjansch17 ; linked open-access book file unavailable in this runtime; causal identifiability claims below are drawn from accessible Peters et al. (2015), Pearl (2018), and Scholkopf et al. (2021) sources.

#### A. Duhem-Quine underdetermination and finite interpolation

- [fact] Quine argues that statements about the external world face the tribunal of sense experience "not individually but only as a corporate body", which is the canonical statement of confirmation holism used in the Duhem-Quine tradition. [source: https://www.theologie.uzh.ch/dam/jcr:ffffffff-fbd6-1538-0000-000070cf64bc/Quine51.pdf]
- [fact] The Stanford Encyclopedia of Philosophy distinguishes holist underdetermination, failed predictions leave multiple background assumptions available for revision, from contrastive underdetermination, the same evidence can equally support rival theories. [source: https://plato.stanford.edu/entries/scientific-underdetermination/]
- [fact] Jensen's interpolation notes prove that for `n+1` distinct nodes there exists a unique interpolating polynomial only inside the restricted class of polynomials of degree at most `n`. [source: https://maxjensen.github.io/Computational_Methods_lecture_notes/4.1_interpolation.html]
- [inference] Finite interpolation therefore fits the Duhem-Quine picture in two layers: the data pick out at most one member of a chosen restricted hypothesis class, but they do not by themselves justify that restriction or eliminate alternative functional forms that agree on the sampled points. [source: https://maxjensen.github.io/Computational_Methods_lecture_notes/4.1_interpolation.html; https://plato.stanford.edu/entries/scientific-underdetermination/; https://www.theologie.uzh.ch/dam/jcr:ffffffff-fbd6-1538-0000-000070cf64bc/Quine51.pdf]

#### B. Observational equivalence in dynamical systems

- [fact] Bongard and Lipson present an automated discovery loop that synthesises candidate symbolic ordinary differential equations (ODEs) to explain observed behaviour and then searches for new tests that maximise disagreement among those candidate models. [source: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1891254/]
- [fact] The same paper states that the method assumes that the possibly noisy time series of all variables are observable and argues that symbolic models have explanatory value beyond purely numerical fit. [source: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1891254/]
- [inference] Candidate-mechanism disagreement after equally good fit to current data is an operational form of observational equivalence: several mechanisms survive the current evidence until richer perturbations or broader observability break the tie. [source: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1891254/; https://opus.bibliothek.uni-augsburg.de/opus4/files/113236/113236.pdf]

#### C. Structural and practical identifiability as quantitative criteria

- [fact] Raue et al. define a parameter as identifiable when its confidence interval is finite and define structural non-identifiability as redundant parameterisation that leaves the observables unchanged while preserving the objective value. [source: https://opus.bibliothek.uni-augsburg.de/opus4/files/113236/113236.pdf]
- [fact] Raue et al. define practical non-identifiability as a case in which the likelihood has a unique minimum but the likelihood-based confidence region remains infinitely extended in at least one parameter direction because the available data are insufficient. [source: https://opus.bibliothek.uni-augsburg.de/opus4/files/113236/113236.pdf]
- [fact] The same paper states that structural non-identifiability requires qualitatively new measurements that alter the mapping from internal states to observables, whereas practical non-identifiability can be reduced by improving the amount, quality, or timing of measurements. [source: https://opus.bibliothek.uni-augsburg.de/opus4/files/113236/113236.pdf]
- [inference] In parametric dynamical models, "matched the true mechanism" requires at minimum that mechanism-bearing parameters are structurally identifiable and practically bounded over the experimental regime relevant to the intended claims. [source: https://opus.bibliothek.uni-augsburg.de/opus4/files/113236/113236.pdf]

#### D. Causal criteria beyond observational fit

- [fact] Pearl argues that model-free machine learning operates primarily at the associational level and cannot answer intervention or retrospection questions without additional knowledge of the data-generating process. [source: https://arxiv.org/abs/1801.04016]
- [fact] Peters, Buhlmann, and Meinshausen state that predictions from a causal model will generally remain valid under interventions, whereas predictions from a non-causal model can become seriously wrong after interventions or environmental changes. [source: https://arxiv.org/abs/1501.01332]
- [fact] Scholkopf et al. argue that generalising outside the independently and identically distributed (i.i.d.) setting requires learning underlying mechanisms rather than relying only on observed statistical associations. [source: https://arxiv.org/abs/2102.11107]
- [inference] Mechanism matching therefore requires at least one criterion that observational interpolation alone cannot supply, for example intervention identifiability, invariance across environments, or experimentally justified observability of all mechanism-relevant state variables. [source: https://arxiv.org/abs/1501.01332; https://arxiv.org/abs/1801.04016; https://arxiv.org/abs/2102.11107; https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1891254/]

#### E. Applicability to deep learning

- [fact] Bona-Pellissier et al. provide conditions under which a deep fully connected feedforward rectified linear unit (ReLU) neural network is identifiable from its realised function on part of the input space, but only modulo permutation and positive rescaling symmetries. [source: https://arxiv.org/abs/2112.12982]
- [fact] Shen's functional-equivalence analysis states that different neural-network parameterisations can yield the same network function and that this equivalence changes the effective complexity of the parameter space. [source: https://proceedings.mlr.press/v235/shen24a.html]
- [inference] Standard deep neural networks therefore do not satisfy structural identifiability by default: even when a function is fixed, multiple parameter realisations can remain observationally equivalent because of known symmetry classes. [source: https://arxiv.org/abs/2112.12982; https://proceedings.mlr.press/v235/shen24a.html]
- [inference] Deep models can approach mechanism recovery only under strong restrictions, such as architecture-specific identifiability results, input coverage rich enough to excite the relevant degrees of freedom, and causal or multi-environment evidence that rules out proxy solutions with the same observational loss. [source: https://arxiv.org/abs/2112.12982; https://arxiv.org/abs/1501.01332; https://arxiv.org/abs/2102.11107]

#### F. Cross-item integration

- [fact] Research Question 2.1 concluded that ERM can achieve strong in-distribution performance while remaining blind to stable causal structure under environment change. [source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq2-1-erm-causal-blindness.md]
- [fact] Research Question 1.1 concluded that predictive agreement on seen cases does not by itself establish explanatory mechanism. [source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq1-1-popper-falsifiability.md]
- [fact] Research Question 1.3 concluded that predictive-first evaluation fails under distribution shift when the learned relation is not tied to invariant structure. [source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq1-3-instrumentalism-failure-modes.md]
- [inference] The present item supplies the theoretical bridge between those earlier results by showing that the ambiguity is not merely an optimisation accident: finite evidence often leaves an equivalence class of theories alive until identifiability and invariance conditions are imposed. [source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq2-1-erm-causal-blindness.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq1-1-popper-falsifiability.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq1-3-instrumentalism-failure-modes.md; https://plato.stanford.edu/entries/scientific-underdetermination/; https://opus.bibliothek.uni-augsburg.de/opus4/files/113236/113236.pdf]

### §3 Reasoning

- [fact] Quine and the underdetermination literature locate the problem at the level of evidence-to-theory mapping: the same evidence can leave multiple revisions or rival theories available. [source: https://www.theologie.uzh.ch/dam/jcr:ffffffff-fbd6-1538-0000-000070cf64bc/Quine51.pdf; https://plato.stanford.edu/entries/scientific-underdetermination/]
- [fact] Raue et al. locate the quantitative version of that problem in the map from model parameters to observables, where non-identifiability means that multiple parameter settings remain compatible with the same observations. [source: https://opus.bibliothek.uni-augsburg.de/opus4/files/113236/113236.pdf]
- [inference] These are the same structure stated at different levels: underdetermination in philosophy becomes non-identifiability in applied modelling once the theories are parameterised and tied to observables. [source: https://plato.stanford.edu/entries/scientific-underdetermination/; https://opus.bibliothek.uni-augsburg.de/opus4/files/113236/113236.pdf]
- [inference] A model has matched the true mechanism only when the evidence has collapsed the relevant equivalence class far enough that neither parameter symmetries nor intervention-sensitive rival explanations remain live for the target claim. [source: https://opus.bibliothek.uni-augsburg.de/opus4/files/113236/113236.pdf; https://arxiv.org/abs/1501.01332; https://arxiv.org/abs/2112.12982]

### §4 Consistency Check

- [inference] The sources align on the core asymmetry between observational success and mechanistic adequacy: Quine and the underdetermination literature emphasise evidential plurality, Raue quantifies parameter-level plurality, and Pearl and Peters et al. explain why interventions expose the difference. [source: https://www.theologie.uzh.ch/dam/jcr:ffffffff-fbd6-1538-0000-000070cf64bc/Quine51.pdf; https://plato.stanford.edu/entries/scientific-underdetermination/; https://opus.bibliothek.uni-augsburg.de/opus4/files/113236/113236.pdf; https://arxiv.org/abs/1801.04016; https://arxiv.org/abs/1501.01332]
- [inference] No contradiction remains between "a model interpolates the data" and "the mechanism is still unknown", because the first claim is about fit on an evidence surface and the second is about whether rival explanations have been ruled out. [source: https://maxjensen.github.io/Computational_Methods_lecture_notes/4.1_interpolation.html; https://opus.bibliothek.uni-augsburg.de/opus4/files/113236/113236.pdf; https://plato.stanford.edu/entries/scientific-underdetermination/]
- [inference] The strongest unresolved uncertainty concerns the deep-learning application, where identifiable special cases exist but do not by themselves show that practical large-scale training regimes recover causal mechanisms rather than symmetry-equivalent or proxy solutions. [source: https://arxiv.org/abs/2112.12982; https://proceedings.mlr.press/v235/shen24a.html; https://arxiv.org/abs/2102.11107]

### §5 Depth and Breadth Expansion

- [fact] Historically, Quine extends Duhem's point from local hypothesis testing in physics to broader webs of belief, which strengthens the relevance of underdetermination beyond any single modelling domain. [source: https://plato.stanford.edu/entries/scientific-underdetermination/; https://www.theologie.uzh.ch/dam/jcr:ffffffff-fbd6-1538-0000-000070cf64bc/Quine51.pdf]
- [inference] Technically, Bongard and Lipson's active probing and Raue et al.'s measurement-design discussion imply that mechanism discovery is as much an experimental-design problem as a fitting problem, because observability and perturbation choice decide whether equivalence classes can be broken. [source: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1891254/; https://opus.bibliothek.uni-augsburg.de/opus4/files/113236/113236.pdf]
- [inference] For machine learning practice, benchmark interpolation on a fixed train-validation split is a narrow test of observational adequacy, while mechanism claims require additional environment variation, intervention logic, or architecture-level identifiability guarantees. [source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq2-1-erm-causal-blindness.md; https://arxiv.org/abs/1501.01332; https://arxiv.org/abs/2112.12982]

### §6 Synthesis

**Executive summary:**

- [inference] Finite observational data do not justify the claim that a model has matched the true mechanism; they justify at most that the model belongs to an equivalence class of theories consistent with the observed traces unless identifiability and invariance conditions are also satisfied. [source: https://plato.stanford.edu/entries/scientific-underdetermination/; https://www.theologie.uzh.ch/dam/jcr:ffffffff-fbd6-1538-0000-000070cf64bc/Quine51.pdf; https://opus.bibliothek.uni-augsburg.de/opus4/files/113236/113236.pdf]
- [fact] In dynamical systems, structural identifiability asks whether distinct parameter settings can leave observables unchanged, while practical identifiability asks whether finite noisy data leave profile-likelihood confidence regions unbounded. [source: https://opus.bibliothek.uni-augsburg.de/opus4/files/113236/113236.pdf]
- [inference] A model counts as mechanism matched only when mechanism-bearing parameters are structurally identifiable, practically constrained, and supported by intervention or multi-environment evidence that rules out observationally equivalent proxies. [source: https://opus.bibliothek.uni-augsburg.de/opus4/files/113236/113236.pdf; https://arxiv.org/abs/1501.01332; https://arxiv.org/abs/1801.04016; https://arxiv.org/abs/2102.11107]
- [inference] Standard deep-learning models trained on passive data usually fail that standard by default because functional and parameter symmetries leave equivalent fits alive and observational risk alone does not certify causal structure. [source: https://arxiv.org/abs/2112.12982; https://proceedings.mlr.press/v235/shen24a.html; https://arxiv.org/abs/1801.04016]

**Key findings:**

1. [inference] The Duhem-Quine thesis maps directly onto model selection because finite evidence constrains a web of hypotheses rather than selecting a unique mechanism, so several rival theories can remain compatible with exactly the same observations. [source: https://www.theologie.uzh.ch/dam/jcr:ffffffff-fbd6-1538-0000-000070cf64bc/Quine51.pdf; https://plato.stanford.edu/entries/scientific-underdetermination/]
2. [fact] Polynomial interpolation is unique only inside a restricted hypothesis class, degree at most `n` polynomials for `n+1` nodes, which shows that uniqueness comes from model-class assumptions rather than from the observations alone. [source: https://maxjensen.github.io/Computational_Methods_lecture_notes/4.1_interpolation.html]
3. [fact] Bongard and Lipson's active-probing framework shows that candidate dynamical models can fit the same current observations and only become distinguishable after new perturbations or broader observability reveal divergent predictions. [source: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1891254/]
4. [fact] Raue et al. provide a quantitative test by defining structural non-identifiability as unchanged observables under redundant parameterisations and practical non-identifiability as unbounded likelihood-based confidence regions caused by insufficient data. [source: https://opus.bibliothek.uni-augsburg.de/opus4/files/113236/113236.pdf]
5. [inference] A model has matched the true mechanism only if mechanism-bearing parameters are structurally identifiable and practically bounded, and if interventions or environment changes fail to expose a rival predictor with the same observational fit. [source: https://opus.bibliothek.uni-augsburg.de/opus4/files/113236/113236.pdf; https://arxiv.org/abs/1501.01332; https://arxiv.org/abs/1801.04016]
6. [fact] Causal-invariance results explain why low observational risk is insufficient, because predictors built on non-causal associations can match training data while breaking under interventions or distribution shift. [source: https://arxiv.org/abs/1501.01332; https://arxiv.org/abs/1801.04016; https://arxiv.org/abs/2102.11107]
7. [fact] Standard deep neural networks do not guarantee mechanism recovery by default because multiple parameterisations can implement the same function, and even identified networks are only unique up to permutation and positive rescaling under strong architectural conditions. [source: https://arxiv.org/abs/2112.12982; https://proceedings.mlr.press/v235/shen24a.html]
8. [inference] Deep learning can approach mechanism identification only when passive fitting is supplemented by restrictive architecture, sufficient excitation of relevant inputs, and multi-environment or interventional evidence that breaks proxy equivalence classes. [source: https://arxiv.org/abs/2112.12982; https://arxiv.org/abs/1501.01332; https://arxiv.org/abs/2102.11107; https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1891254/]

**Evidence map:**

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [inference] Finite evidence leaves multiple mechanism-level theories live. | https://www.theologie.uzh.ch/dam/jcr:ffffffff-fbd6-1538-0000-000070cf64bc/Quine51.pdf ; https://plato.stanford.edu/entries/scientific-underdetermination/ | medium | Holism plus contrast. |
| [fact] Interpolation uniqueness is restricted to a chosen low-degree polynomial class. | https://maxjensen.github.io/Computational_Methods_lecture_notes/4.1_interpolation.html | medium | Class-restricted uniqueness. |
| [fact] Candidate dynamical models can agree on current traces and diverge under new probes. | https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1891254/ | medium | Active probing. |
| [fact] Structural and practical identifiability provide quantitative non-equivalence tests. | https://opus.bibliothek.uni-augsburg.de/opus4/files/113236/113236.pdf | medium | Definitions plus criteria. |
| [inference] Mechanism matching requires identifiability plus failed rival exposure under interventions or shifts. | https://opus.bibliothek.uni-augsburg.de/opus4/files/113236/113236.pdf ; https://arxiv.org/abs/1501.01332 ; https://arxiv.org/abs/1801.04016 | medium | Stronger than fit. |
| [fact] Observationally accurate but non-causal predictors can fail after interventions or environment change. | https://arxiv.org/abs/1501.01332 ; https://arxiv.org/abs/1801.04016 ; https://arxiv.org/abs/2102.11107 | high | Invariance criterion. |
| [fact] Deep neural networks admit symmetry-equivalent parameterisations. | https://arxiv.org/abs/2112.12982 ; https://proceedings.mlr.press/v235/shen24a.html | medium | Function fixed, parameters not. |
| [inference] Deep-learning mechanism claims need extra architectural and causal restrictions. | https://arxiv.org/abs/2112.12982 ; https://arxiv.org/abs/1501.01332 ; https://arxiv.org/abs/2102.11107 ; https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1891254/ | medium | Restrictive conditions. |

**Assumptions:**

- [assumption] "Mechanism-bearing parameters" means the subset of parameters whose variation changes intervention-relevant or environment-invariant behaviour, not merely a redundant reparameterisation of the same observational map. [source: https://opus.bibliothek.uni-augsburg.de/opus4/files/113236/113236.pdf; https://arxiv.org/abs/1501.01332; https://arxiv.org/abs/1801.04016]
- [assumption] The target mechanism is representable within the candidate model class being evaluated, because identifiability results cannot recover a mechanism that the class cannot express. [source: https://opus.bibliothek.uni-augsburg.de/opus4/files/113236/113236.pdf; https://arxiv.org/abs/2112.12982]

**Analysis:**

- [inference] The evidence weighs most strongly on the negative claim, observational fit alone is insufficient, because Quine, Raue, Pearl, Peters et al., and Scholkopf et al. all converge on the same asymmetry between observed agreement and mechanism-level warrant. [source: https://www.theologie.uzh.ch/dam/jcr:ffffffff-fbd6-1538-0000-000070cf64bc/Quine51.pdf; https://opus.bibliothek.uni-augsburg.de/opus4/files/113236/113236.pdf; https://arxiv.org/abs/1801.04016; https://arxiv.org/abs/1501.01332; https://arxiv.org/abs/2102.11107]
- [inference] The positive criterion must therefore be conjunctive rather than singular: identifiability without intervention sensitivity can still miss proxy mechanisms, while invariance claims without identifiability can still hide redundant parameterisations. [source: https://opus.bibliothek.uni-augsburg.de/opus4/files/113236/113236.pdf; https://arxiv.org/abs/1501.01332]
- [inference] Bongard and Lipson sharpen this by showing that experiment design, not just loss minimisation, determines whether rival mechanisms remain observationally equivalent, which makes active probing part of the epistemic test rather than a downstream optimisation detail. [source: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1891254/]
- [inference] The deep-learning case remains more conditional than the dynamical-systems case because the identifiable special results are architecture-specific and symmetry-bounded, whereas large practical training pipelines rarely satisfy those restrictive premises transparently. [source: https://arxiv.org/abs/2112.12982; https://proceedings.mlr.press/v235/shen24a.html; https://arxiv.org/abs/2102.11107]

**Risks, gaps, uncertainties:**

- [inference] Structural identifiability is model-class relative, so a model can be identifiable inside a misspecified class and still fail to capture the real-world mechanism outside that class. [source: https://opus.bibliothek.uni-augsburg.de/opus4/files/113236/113236.pdf]
- [inference] The deep-learning conclusion is medium confidence rather than high confidence because the cited identifiability results cover restricted network families, not the full range of contemporary large-scale training settings. [source: https://arxiv.org/abs/2112.12982; https://proceedings.mlr.press/v235/shen24a.html]
- [inference] Intervention-based criteria are strongest when feasible, but many practical domains still rely on partial observability or limited perturbation budgets, which leaves some equivalence classes unresolved even after careful measurement design. [source: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1891254/; https://opus.bibliothek.uni-augsburg.de/opus4/files/113236/113236.pdf]

**Open questions:**

- Which practical benchmark family best measures mechanism identification, rather than interpolation, in modern deep-learning systems?
- How should identifiability be defined when the target is a latent causal representation rather than an explicit ODE or graph parameter set?
- What minimum intervention or environment-variation budget is sufficient to break the most important proxy equivalence classes in foundation-model settings?

### §7 Recursive Review

- Review result: pass
- Acronym audit: pass
- Claim-label audit: pass
- Findings and synthesis parity: aligned
- Confidence assessment: medium, because the core identifiability definitions are strongly sourced but the extension to standard deep-learning practice remains partly inferential.

---

## Findings

### Executive Summary

Finite observational data do not justify the claim that a model has matched the true mechanism; they justify at most that the model belongs to an equivalence class of theories consistent with the observed traces unless identifiability and invariance conditions are also satisfied. [inference; source: https://plato.stanford.edu/entries/scientific-underdetermination/; https://www.theologie.uzh.ch/dam/jcr:ffffffff-fbd6-1538-0000-000070cf64bc/Quine51.pdf; https://opus.bibliothek.uni-augsburg.de/opus4/files/113236/113236.pdf]

In dynamical systems, structural identifiability asks whether distinct parameter settings can leave observables unchanged, while practical identifiability asks whether finite noisy data leave profile-likelihood confidence regions unbounded. [fact; source: https://opus.bibliothek.uni-augsburg.de/opus4/files/113236/113236.pdf]

A model counts as mechanism matched only when mechanism-bearing parameters are structurally identifiable, practically constrained, and supported by intervention or multi-environment evidence that rules out observationally equivalent proxies. [inference; source: https://opus.bibliothek.uni-augsburg.de/opus4/files/113236/113236.pdf; https://arxiv.org/abs/1501.01332; https://arxiv.org/abs/1801.04016; https://arxiv.org/abs/2102.11107]

Standard deep-learning models trained on passive data usually fail that standard by default because functional and parameter symmetries leave equivalent fits alive and observational risk alone does not certify causal structure. [inference; source: https://arxiv.org/abs/2112.12982; https://proceedings.mlr.press/v235/shen24a.html; https://arxiv.org/abs/1801.04016]

### Key Findings

1. **The Duhem-Quine thesis maps directly onto model selection because finite evidence constrains a web of hypotheses rather than selecting a unique mechanism, so several rival theories can remain compatible with exactly the same observations.** ([inference]; medium confidence; source: https://www.theologie.uzh.ch/dam/jcr:ffffffff-fbd6-1538-0000-000070cf64bc/Quine51.pdf; https://plato.stanford.edu/entries/scientific-underdetermination/)
2. **Polynomial interpolation is unique only inside a restricted hypothesis class, degree at most `n` polynomials for `n+1` nodes, which shows that uniqueness comes from model-class assumptions rather than from the observations alone.** ([fact]; medium confidence; source: https://maxjensen.github.io/Computational_Methods_lecture_notes/4.1_interpolation.html)
3. **Bongard and Lipson's active-probing framework shows that candidate dynamical models can fit the same current observations and only become distinguishable after new perturbations or broader observability reveal divergent predictions.** ([fact]; medium confidence; source: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1891254/)
4. **Raue et al. provide a quantitative test by defining structural non-identifiability as unchanged observables under redundant parameterisations and practical non-identifiability as unbounded likelihood-based confidence regions caused by insufficient data.** ([fact]; medium confidence; source: https://opus.bibliothek.uni-augsburg.de/opus4/files/113236/113236.pdf)
5. **A model has matched the true mechanism only if mechanism-bearing parameters are structurally identifiable and practically bounded, and if interventions or environment changes fail to expose a rival predictor with the same observational fit.** ([inference]; medium confidence; source: https://opus.bibliothek.uni-augsburg.de/opus4/files/113236/113236.pdf; https://arxiv.org/abs/1501.01332; https://arxiv.org/abs/1801.04016)
6. **Causal-invariance results explain why low observational risk is insufficient, because predictors built on non-causal associations can match training data while breaking under interventions or distribution shift.** ([fact]; high confidence; source: https://arxiv.org/abs/1501.01332; https://arxiv.org/abs/1801.04016; https://arxiv.org/abs/2102.11107)
7. **Standard deep neural networks do not guarantee mechanism recovery by default because multiple parameterisations can implement the same function, and even identified networks are only unique up to permutation and positive rescaling under strong architectural conditions.** ([fact]; medium confidence; source: https://arxiv.org/abs/2112.12982; https://proceedings.mlr.press/v235/shen24a.html)
8. **Deep learning can approach mechanism identification only when passive fitting is supplemented by restrictive architecture, sufficient excitation of relevant inputs, and multi-environment or interventional evidence that breaks proxy equivalence classes.** ([inference]; medium confidence; source: https://arxiv.org/abs/2112.12982; https://arxiv.org/abs/1501.01332; https://arxiv.org/abs/2102.11107; https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1891254/)

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [inference] Finite evidence leaves multiple mechanism-level theories live. | https://www.theologie.uzh.ch/dam/jcr:ffffffff-fbd6-1538-0000-000070cf64bc/Quine51.pdf ; https://plato.stanford.edu/entries/scientific-underdetermination/ | medium | Holism plus contrast. |
| [fact] Interpolation uniqueness is restricted to a chosen low-degree polynomial class. | https://maxjensen.github.io/Computational_Methods_lecture_notes/4.1_interpolation.html | medium | Class-restricted uniqueness. |
| [fact] Candidate dynamical models can agree on current traces and diverge under new probes. | https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1891254/ | medium | Active probing. |
| [fact] Structural and practical identifiability provide quantitative non-equivalence tests. | https://opus.bibliothek.uni-augsburg.de/opus4/files/113236/113236.pdf | medium | Definitions plus criteria. |
| [inference] Mechanism matching requires identifiability plus failed rival exposure under interventions or shifts. | https://opus.bibliothek.uni-augsburg.de/opus4/files/113236/113236.pdf ; https://arxiv.org/abs/1501.01332 ; https://arxiv.org/abs/1801.04016 | medium | Stronger than fit. |
| [fact] Observationally accurate but non-causal predictors can fail after interventions or environment change. | https://arxiv.org/abs/1501.01332 ; https://arxiv.org/abs/1801.04016 ; https://arxiv.org/abs/2102.11107 | high | Invariance criterion. |
| [fact] Deep neural networks admit symmetry-equivalent parameterisations. | https://arxiv.org/abs/2112.12982 ; https://proceedings.mlr.press/v235/shen24a.html | medium | Function fixed, parameters not. |
| [inference] Deep-learning mechanism claims need extra architectural and causal restrictions. | https://arxiv.org/abs/2112.12982 ; https://arxiv.org/abs/1501.01332 ; https://arxiv.org/abs/2102.11107 ; https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1891254/ | medium | Restrictive conditions. |

### Assumptions

- "Mechanism-bearing parameters" means the subset of parameters whose variation changes intervention-relevant or environment-invariant behaviour, not merely a redundant reparameterisation of the same observational map. [assumption; source: https://opus.bibliothek.uni-augsburg.de/opus4/files/113236/113236.pdf; https://arxiv.org/abs/1501.01332; https://arxiv.org/abs/1801.04016]
- The target mechanism is representable within the candidate model class being evaluated, because identifiability results cannot recover a mechanism that the class cannot express. [assumption; source: https://opus.bibliothek.uni-augsburg.de/opus4/files/113236/113236.pdf; https://arxiv.org/abs/2112.12982]

### Analysis

The evidence weighs most strongly on the negative claim, observational fit alone is insufficient, because Quine, Raue, Pearl, Peters et al., and Scholkopf et al. all converge on the same asymmetry between observed agreement and mechanism-level warrant. [inference; source: https://www.theologie.uzh.ch/dam/jcr:ffffffff-fbd6-1538-0000-000070cf64bc/Quine51.pdf; https://opus.bibliothek.uni-augsburg.de/opus4/files/113236/113236.pdf; https://arxiv.org/abs/1801.04016; https://arxiv.org/abs/1501.01332; https://arxiv.org/abs/2102.11107]

The positive criterion must therefore be conjunctive rather than singular: identifiability without intervention sensitivity can still miss proxy mechanisms, while invariance claims without identifiability can still hide redundant parameterisations. [inference; source: https://opus.bibliothek.uni-augsburg.de/opus4/files/113236/113236.pdf; https://arxiv.org/abs/1501.01332]

Bongard and Lipson sharpen this by showing that experiment design, not just loss minimisation, determines whether rival mechanisms remain observationally equivalent, which makes active probing part of the epistemic test rather than a downstream optimisation detail. [inference; source: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1891254/]

The deep-learning case remains more conditional than the dynamical-systems case because the identifiable special results are architecture-specific and symmetry-bounded, whereas large practical training pipelines rarely satisfy those restrictive premises transparently. [inference; source: https://arxiv.org/abs/2112.12982; https://proceedings.mlr.press/v235/shen24a.html; https://arxiv.org/abs/2102.11107]

### Risks, Gaps, and Uncertainties

- Structural identifiability is model-class relative, so a model can be identifiable inside a misspecified class and still fail to capture the real-world mechanism outside that class. [inference; source: https://opus.bibliothek.uni-augsburg.de/opus4/files/113236/113236.pdf]
- The deep-learning conclusion is medium confidence rather than high confidence because the cited identifiability results cover restricted network families, not the full range of contemporary large-scale training settings. [inference; source: https://arxiv.org/abs/2112.12982; https://proceedings.mlr.press/v235/shen24a.html]
- Intervention-based criteria are strongest when feasible, but many practical domains still rely on partial observability or limited perturbation budgets, which leaves some equivalence classes unresolved even after careful measurement design. [inference; source: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1891254/; https://opus.bibliothek.uni-augsburg.de/opus4/files/113236/113236.pdf]

### Open Questions

- Which practical benchmark family best measures mechanism identification, rather than interpolation, in modern deep-learning systems?
- How should identifiability be defined when the target is a latent causal representation rather than an explicit ordinary differential equation or graph parameter set?
- What minimum intervention or environment-variation budget is sufficient to break the most important proxy equivalence classes in foundation-model settings?

---

## Output

- Type: knowledge
- Description: This item defines mechanism matching as the conjunction of identifiability and invariance checks, rather than as observational fit alone. [inference; source: https://opus.bibliothek.uni-augsburg.de/opus4/files/113236/113236.pdf; https://arxiv.org/abs/1501.01332; https://arxiv.org/abs/1801.04016]
- Links:
  - https://opus.bibliothek.uni-augsburg.de/opus4/files/113236/113236.pdf
  - https://arxiv.org/abs/1501.01332
  - https://plato.stanford.edu/entries/scientific-underdetermination/
