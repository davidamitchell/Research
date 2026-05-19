---
review_count: 2
title: "Research Question 2.3: Structural Stability vs. Predictive Fragility, Dynamical Systems Theory and the Cost of Noise"
added: 2026-05-18T19:40:00+00:00
status: reviewing
priority: high
blocks:
  - 2026-05-18-rq2-4-causal-hierarchy-formal-limits
tags: [machine-learning, formal-methods, causal-inference, invariants, epistemology]
started: 2026-05-19T09:06:53+00:00
completed: ~
output: [knowledge]
cites:
  - 2026-05-18-rq2-1-erm-causal-blindness
  - 2026-05-18-rq2-2-duhem-quine-underdetermination
  - 2026-05-18-rq1-3-instrumentalism-failure-modes
related:
  - 2026-05-18-rq2-4-causal-hierarchy-formal-limits
superseded_by: ~
supersedes: ~
item_type: primary
confidence: medium
versions: []
---

# Research Question 2.3: Structural Stability vs. Predictive Fragility, Dynamical Systems Theory and the Cost of Noise

## Research Question

Using dynamical systems theory, how does the fragility of a purely predictive model under input noise or system drift differ from the local qualitative stability of a model whose governing equations preserve the same orbit structure under small perturbations because they are anchored in invariant physical mechanisms?

## Scope

**In scope:**
- Structural stability, the property that small smooth perturbations preserve a system's qualitative orbit structure up to topological equivalence, in the Andronov-Pontryagin criterion for planar systems
- Sensitivity analysis of predictive models under input perturbation
- Distribution shift propagation: how small input changes cascade through causally ungrounded models
- Contrast between models with structurally stable attractor basins vs. causally ungrounded interpolators

**Out of scope:**
- Numerical stability of specific optimisation algorithms
- Hardware-level perturbation or adversarial machine learning attacks (covered in Phase 4)

**Constraints:** Must build on Research Question 2.1's Empirical Risk Minimisation (ERM) analysis; use dynamical systems formalism from Thom and Strogatz.

## Context

Research Question 2.1 established that Empirical Risk Minimisation (ERM) is causally blind under environment change. [fact; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq2-1-erm-causal-blindness.md]

Research Question 2.2 showed that finite observations can leave multiple candidate mechanisms observationally equivalent unless stronger identifiability tests are added. [fact; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq2-2-duhem-quine-underdetermination.md]

This item asks what that ambiguity means dynamically: whether small perturbations leave a model's qualitative orbit structure intact or expose dependence on unstable shortcuts. [inference; source: http://www.scholarpedia.org/article/Structural_stability; https://www.jmlr.org/papers/v23/20-1335.html]

## Approach

1. Define structural stability (Andronov-Pontryagin) in the context of dynamical system models.
2. Formalise sensitivity to initial conditions: how a small change in input propagates through the output space of a causally ungrounded model.
3. Apply the framework to a concrete example: compare a physics-informed model (structurally stable) against a neural network interpolator (structurally fragile) under input drift.
4. Examine distribution shift propagation formally: when do small distribution changes cause qualitative behavioural changes in a predictive model?
5. Summarise: what formal property distinguishes a stable mechanistic model from a fragile interpolative one?

## Sources

- [x] [Thom (1975) Structural Stability and Morphogenesis](https://archive.org/details/structuralstabil0000thom) - corrected Internet Archive catalog entry for the seeded book on structural stability and morphogenesis
- [x] [Strogatz (2014) Nonlinear Dynamics and Chaos](https://www.hachettebookgroup.com/titles/steven-h-strogatz/nonlinear-dynamics-and-chaos/9780813349107/) - publisher locator for the seeded text on nonlinear dynamics
- [x] [Pugh and Peixoto (n.d.) Structural stability](http://www.scholarpedia.org/article/Structural_stability) - authoritative definition of structural stability and historical summary of the Andronov-Pontryagin criterion
- [x] [Sugiyama and Kawanabe (2012) Machine Learning in Non-Stationary Environments](https://doi.org/10.7551/mitpress/9780262017091.001.0001) - Digital Object Identifier (DOI) record for the seeded book on non-stationary learning
- [x] [Arjovsky et al. (2020) Invariant Risk Minimization](https://arxiv.org/abs/1907.02893) - invariant predictors and environment-shift robustness
- [x] [Geirhos et al. (2023) Shortcut Learning in Deep Neural Networks](https://arxiv.org/abs/2004.07780) - shortcut-based transfer failure under harder testing conditions
- [x] [D'Amour et al. (2022) Underspecification Presents Challenges for Credibility in Modern Machine Learning](https://www.jmlr.org/papers/v23/20-1335.html) - multiple equally strong held-out predictors can diverge in deployment
- [x] [Yang et al. (2024) Identifying Spurious Biases Early in Training through the Lens of Simplicity Bias](https://openreview.net/forum?id=VCnuSuDSHv) - simplicity bias toward spurious features
- [x] [Lee et al. (2023) Stable clinical risk prediction against distribution shift in electronic health records](https://pmc.ncbi.nlm.nih.gov/articles/PMC10499849/) - temporal distribution shift causes performance decay in deployed health models
- [x] [Golinski et al. (2024) Considerations for Distribution Shift Robustness of Diagnostic Models in Healthcare](https://arxiv.org/abs/2410.19575) - unstable shortcuts under demographic and deployment shifts
- [x] [Dang et al. (2025) Physics Informed Constrained Learning of Dynamics from Static Data](https://arxiv.org/abs/2504.12675) - physics-constrained learning outperforming existing data-driven estimators
- [x] [Research repo (2026-05-18) Research Question 2.1: Empirical Risk Minimisation's causal blindness and the limits of in-distribution guarantees](https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq2-1-erm-causal-blindness.md) - prior repository item on ERM and invariance
- [x] [Research repo (2026-05-19) Research Question 2.2: The Duhem-Quine thesis and underdetermination, quantifying when a model has matched the true mechanism](https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq2-2-duhem-quine-underdetermination.md) - prior repository item on underdetermination and identifiability

---

## Research Skill Output

*(Full output from running the research skill, retained verbatim in the completed item. §§0-5 are the investigation; §6 seeds the Findings section below.)*

### §0 Initialise

- Question: How does a purely predictive model respond to noise or drift when compared with a model whose governing dynamics remain qualitatively unchanged under small perturbations because they are anchored in invariant physical mechanisms?
- Scope: structural stability in planar dynamical systems, shortcut- and underspecification-based predictive fragility, distribution shift propagation, and one concrete mechanistic-versus-black-box comparison.
- Constraints: full mode; build directly on Research Question 2.1 and cross-check against Research Question 2.2; use link-backed citations only; keep tags in canonical form where the vocabulary defines one.
- Output: executive summary, key findings, evidence map, assumptions, analysis, risks, gaps, uncertainties, and open questions.
- Prior completed items consulted: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq2-1-erm-causal-blindness.md ; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq2-2-duhem-quine-underdetermination.md

### §1 Question Decomposition

1. Structural stability
   1.1 What does structural stability mean for a dynamical system under small perturbations of the governing vector field?
   1.2 What conditions does the Andronov-Pontryagin criterion impose in the planar case?
   1.3 Why does structural stability concern qualitative orbit structure rather than pointwise numerical equality?
2. Predictive fragility
   2.1 Why can a purely predictive model fit one regime while remaining unstable under drift or noise?
   2.2 How do shortcut learning and underspecification explain that instability?
   2.3 Why is fragility about the learned relation, not merely about poor optimisation or small sample size?
3. Propagation under shift
   3.1 When do small environment changes alter a predictive model's behaviour qualitatively rather than only quantitatively?
   3.2 What role does invariance play in preventing those qualitative failures?
4. Concrete comparison
   4.1 What does a mechanistic model gain by encoding governing constraints directly?
   4.2 What does a black-box interpolator lack when the deployment regime moves away from the training regime?
5. Synthesis
   5.1 What formal property distinguishes a structurally stable mechanistic model from a fragile interpolator?
   5.2 How does this item sharpen the claims already established in Research Questions 2.1 and 2.2?

### §2 Investigation

#### Access notes

- Access note: seeded Thom Internet Archive link 404 -> corrected catalog entry used: https://archive.org/details/structuralstabil0000thom
- Access note: seeded Andronov-Pontryagin MathNet link -> unrelated later archive page, not the 1937 note
- Search note: query `Andronov Pontryagin Systemes grossiers 1937 full text` -> bibliographic records only, no accessible public primary text
- Access note: seeded Strogatz and Sugiyama Digital Object Identifier (DOI) records -> bibliographic metadata only

#### A. Structural stability in dynamical systems

- [fact] Scholarpedia defines structural stability for flows as the property that every sufficiently close perturbation of the vector field has an orbit structure that is topologically equivalent to the original one, meaning a homeomorphism maps the original trajectories to the perturbed trajectories while preserving orientation. [source: http://www.scholarpedia.org/article/Structural_stability]
- [fact] The same source summarises the Andronov-Pontryagin theorem for planar systems: structural stability requires hyperbolic singularities and closed orbits together with the absence of trajectories that connect saddle points. [source: http://www.scholarpedia.org/article/Structural_stability]
- [fact] Scholarpedia explains hyperbolicity as an eigenvalue condition, nonzero real parts for singularities and first-return eigenvalues with absolute value different from one for closed orbits, which is the mechanism that prevents qualitative type changes under small perturbations. [source: http://www.scholarpedia.org/article/Structural_stability]
- [inference] Structural stability is therefore a claim about perturbing the governing law itself, not just about changing initial conditions, because the criterion asks whether nearby vector fields preserve the same phase portrait rather than whether one trajectory stays numerically close to another. [source: http://www.scholarpedia.org/article/Structural_stability; https://archive.org/details/structuralstabil0000thom; https://www.hachettebookgroup.com/titles/steven-h-strogatz/nonlinear-dynamics-and-chaos/9780813349107/]

#### B. Why purely predictive models are fragile under noise or drift

- [fact] D'Amour et al. define underspecification as the case in which a machine-learning pipeline can return many distinct predictors with equivalently strong test performance in the training domain, while those predictors behave very differently in deployment domains. [source: https://www.jmlr.org/papers/v23/20-1335.html]
- [fact] Geirhos et al. define shortcut learning as decision rules that perform well on standard benchmarks but fail to transfer to more challenging testing conditions, including real-world scenarios. [source: https://arxiv.org/abs/2004.07780]
- [fact] Yang et al. report that neural networks trained with stochastic gradient descent are biased toward simpler solutions and can let spurious features dominate predictions when those features have a favorable noise-to-signal ratio. [source: https://openreview.net/forum?id=VCnuSuDSHv]
- [inference] A purely predictive model is fragile because its training objective can be satisfied by many observationally successful rules, and optimisation pressure can settle on a simple shortcut rule that has no reason to remain valid once the environment changes. [source: https://www.jmlr.org/papers/v23/20-1335.html; https://arxiv.org/abs/2004.07780; https://openreview.net/forum?id=VCnuSuDSHv]

#### C. Distribution shift propagation

- [fact] Lee et al. state that many machine-learning models assume training and test data are independently and identically distributed, and they report that out-of-distribution problems in electronic health records cause significant performance degradation in the testing environment. [source: https://pmc.ncbi.nlm.nih.gov/articles/PMC10499849/]
- [fact] Golinski et al. show that diagnostic models may exploit confounding dependencies between observations and labels that are unstable under distribution shifts such as demographic changes between training and deployment populations. [source: https://arxiv.org/abs/2410.19575]
- [fact] Arjovsky et al. define Invariant Risk Minimisation as learning a representation for which the optimal classifier is the same across multiple training environments, explicitly targeting invariant correlations rather than pooled empirical fit. [source: https://arxiv.org/abs/1907.02893]
- [inference] Small environment changes cause large behavioural changes when the predictor depends on features whose predictive power is contingent on the training regime, because the model has no structural reason to keep the same decision surface once those contingencies move. [source: https://pmc.ncbi.nlm.nih.gov/articles/PMC10499849/; https://arxiv.org/abs/2410.19575; https://arxiv.org/abs/1907.02893]
- [inference] Invariance matters here for the same reason structural stability matters in dynamical systems: the central question is not whether one observed regime was fit well, but whether the relevant relation survives a neighborhood of perturbations in the environment. [source: http://www.scholarpedia.org/article/Structural_stability; https://arxiv.org/abs/1907.02893; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq2-1-erm-causal-blindness.md]

#### D. Concrete comparison, mechanistic model versus interpolator

- [fact] Dang et al. describe physics-informed constrained learning as a framework that enforces governing physical laws while fitting observed data, and they report that their Message Passing Optimization-based Constrained Learning (MPOCtrL) method outperforms existing data-driven flux estimators in metabolic flux analysis. [source: https://arxiv.org/abs/2504.12675]
- [fact] D'Amour et al. show that equally strong held-out predictors can diverge in deployment even without any single obvious implementation mistake, because the pipeline leaves multiple observationally adequate solutions live. [source: https://www.jmlr.org/papers/v23/20-1335.html]
- [inference] A mechanistic model with a structurally stable phase portrait is robust in a stronger sense than a black-box interpolator, because small perturbations leave the qualitative orbit geometry intact when the governing mechanism is encoded, whereas a predictor chosen only for observational fit can switch behaviour once the shortcut-supporting context moves. [source: http://www.scholarpedia.org/article/Structural_stability; https://arxiv.org/abs/2504.12675; https://www.jmlr.org/papers/v23/20-1335.html]
- [assumption] The mechanistic-versus-interpolator comparison is representative of the broader class of scientific machine-learning problems in which governing constraints correspond to real conserved or causal structure, because the cited physics-constrained and deployment-shift papers both distinguish between constraint-anchored and purely observational solutions. [source: https://arxiv.org/abs/2504.12675; https://www.jmlr.org/papers/v23/20-1335.html; https://arxiv.org/abs/2410.19575]

#### E. Cross-item integration

- [fact] Research Question 2.1 concluded that Empirical Risk Minimisation (ERM) can succeed in distribution while remaining blind to invariant causal structure. [source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq2-1-erm-causal-blindness.md]
- [fact] Research Question 2.2 concluded that finite evidence often leaves multiple mechanism-level explanations alive unless identifiability or intervention criteria collapse that equivalence class. [source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq2-2-duhem-quine-underdetermination.md]
- [inference] The present item adds the dynamical consequence of those earlier claims: when the selected rule is not tied to invariant structure, small perturbations need not merely reduce accuracy, they can change the model's qualitative behaviour because nothing forces the learned relation to remain topologically or causally stable. [source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq2-1-erm-causal-blindness.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq2-2-duhem-quine-underdetermination.md; http://www.scholarpedia.org/article/Structural_stability]

### §3 Reasoning

- [fact] Structural stability and predictive robustness answer different questions: one asks whether nearby governing systems preserve the same qualitative orbit structure, and the other asks whether a predictor keeps working when the deployment environment departs from the training regime. [source: http://www.scholarpedia.org/article/Structural_stability; https://pmc.ncbi.nlm.nih.gov/articles/PMC10499849/]
- [inference] Those questions become linked when a predictor is treated as a model of the world, because a system that lacks invariant structure has no theorem ensuring that its behavior remains qualitatively similar once the environment drifts. [source: http://www.scholarpedia.org/article/Structural_stability; https://www.jmlr.org/papers/v23/20-1335.html; https://arxiv.org/abs/2410.19575]
- [inference] The strongest contrast is therefore not "mechanistic models are always accurate" versus "neural networks are always fragile", but "mechanistic models can encode a reason for local stability" versus "pure interpolators can be observationally adequate without encoding any such reason". [source: http://www.scholarpedia.org/article/Structural_stability; https://arxiv.org/abs/2504.12675; https://www.jmlr.org/papers/v23/20-1335.html]

### §4 Consistency Check

- [fact] Tension: not every predictive model fails under every small shift. [source: https://www.jmlr.org/papers/v23/20-1335.html; https://arxiv.org/abs/2410.19575]
- [inference] Resolution: the claim here is not universal failure, but the absence of a formal stability guarantee when the learned rule is selected only by predictive fit and shortcut compatibility. [source: https://www.jmlr.org/papers/v23/20-1335.html; https://arxiv.org/abs/2004.07780; https://openreview.net/forum?id=VCnuSuDSHv]
- [fact] Tension: structural stability is a theorem about dynamical systems, not a theorem about modern machine-learning architectures. [source: http://www.scholarpedia.org/article/Structural_stability]
- [inference] Resolution: the transfer is analogical but disciplined, because the item compares two model classes through the property they do or do not encode, a perturbation-resilient mechanism, rather than claiming that every neural network literally satisfies or violates the Andronov-Pontryagin criterion. [source: http://www.scholarpedia.org/article/Structural_stability; https://arxiv.org/abs/2504.12675; https://www.jmlr.org/papers/v23/20-1335.html]
- [inference] The main unresolved uncertainty is the breadth of the concrete comparison, because the available open source on physics-constrained learning is narrower than the broader literature on shortcut and deployment fragility. [source: https://arxiv.org/abs/2504.12675; https://www.jmlr.org/papers/v23/20-1335.html]

### §5 Depth and Breadth Expansion

- [inference] Technical lens: hyperbolicity and the absence of saddle connections are local geometric conditions that prevent bifurcation under small perturbations, whereas shortcut-dominated predictors lack an analogous built-in geometric constraint on their decision rule. [source: http://www.scholarpedia.org/article/Structural_stability; https://arxiv.org/abs/2004.07780]
- [inference] Historical lens: Andronov and Pontryagin formalised stability as preservation of qualitative structure under perturbation, which makes the present comparison useful because modern predictive fragility is also a question about what survives outside the exact observed regime. [source: http://www.scholarpedia.org/article/Structural_stability]
- [inference] Behavioural lens: shortcut learning and underspecification imply that a model can appear competent to operators while quietly depending on unstable contextual signals, which is why fragility often surfaces only after deployment. [source: https://arxiv.org/abs/2004.07780; https://www.jmlr.org/papers/v23/20-1335.html]
- [inference] Operational lens: the health-care shift literature shows that drift can come from mundane changes in demographics, coding systems, or acquisition contexts rather than from adversarial attacks, so structural fragility is a routine deployment risk rather than an edge case. [source: https://pmc.ncbi.nlm.nih.gov/articles/PMC10499849/; https://arxiv.org/abs/2410.19575]

### §6 Synthesis

**Executive summary:**

- [inference] A model anchored in invariant governing structure is formally more stable under small perturbations than a purely predictive interpolator, because structural stability preserves qualitative orbit geometry while shortcut-compatible predictors can change behaviour when the deployment context moves. [source: http://www.scholarpedia.org/article/Structural_stability; https://www.jmlr.org/papers/v23/20-1335.html; https://arxiv.org/abs/2004.07780]
- [fact] In planar dynamical systems, the Andronov-Pontryagin criterion characterises structural stability through hyperbolic equilibria and periodic orbits together with the absence of saddle connections. [source: http://www.scholarpedia.org/article/Structural_stability]
- [fact] In modern machine learning, underspecification, shortcut learning, and distribution shift show that many predictors with equally good held-out performance can behave differently in deployment because their apparent success depends on unstable contextual cues. [source: https://www.jmlr.org/papers/v23/20-1335.html; https://arxiv.org/abs/2004.07780; https://pmc.ncbi.nlm.nih.gov/articles/PMC10499849/]
- [inference] Poor optimisation or limited data can worsen that fragility, but they do not exhaust it, because deployment-divergent predictors can still emerge after strong held-out validation when the learned rule depends on unstable contextual structure. [source: https://www.jmlr.org/papers/v23/20-1335.html; https://pmc.ncbi.nlm.nih.gov/articles/PMC10499849/; https://arxiv.org/abs/2410.19575]
- [inference] Invariant Risk Minimisation (IRM) is one partial alternative route to shift robustness because it searches for cross-environment stable features without requiring a full mechanistic model, but its need for heterogeneous environments reinforces Research Question 1.3's conclusion that predictive fit alone does not supply the missing stability information. [source: https://arxiv.org/abs/1907.02893; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq1-3-instrumentalism-failure-modes.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq2-1-erm-causal-blindness.md]

**Key findings:**

1. [fact] Structural stability is a property of the governing dynamical system, not of one observed trajectory, because it asks whether nearby vector fields preserve the same qualitative orbit structure up to topological equivalence. [source: http://www.scholarpedia.org/article/Structural_stability]
2. [fact] The planar Andronov-Pontryagin criterion ties that stability to hyperbolic equilibria and periodic orbits together with the absence of saddle connections, which are exactly the conditions that block qualitative phase-portrait change under small perturbations. [source: http://www.scholarpedia.org/article/Structural_stability]
3. [fact] Purely predictive machine-learning pipelines are often underspecified, meaning they can produce multiple models with equally strong held-out performance that nevertheless diverge in deployment. [source: https://www.jmlr.org/papers/v23/20-1335.html]
4. [fact] Shortcut learning and simplicity bias explain one route to that divergence, because models can adopt simple contextual cues that work on the training regime but fail under harder or shifted testing conditions. [source: https://arxiv.org/abs/2004.07780; https://openreview.net/forum?id=VCnuSuDSHv]
5. [fact] Empirical deployment studies show that ordinary data shifts, such as temporal coding changes or demographic differences, can materially degrade predictive performance when the learned relation is not stable across environments. [source: https://pmc.ncbi.nlm.nih.gov/articles/PMC10499849/; https://arxiv.org/abs/2410.19575]
6. [inference] A structurally stable mechanistic model is stronger than a high-accuracy interpolator because it encodes a reason that local perturbations should preserve behavior, whereas the interpolator only encodes that one observed regime was fitted. [source: http://www.scholarpedia.org/article/Structural_stability; https://www.jmlr.org/papers/v23/20-1335.html]
7. [fact] Physics-constrained learning offers a concrete example of that contrast, because adding governing constraints can outperform existing data-driven estimators while explicitly tying the model to underlying system dynamics. [source: https://arxiv.org/abs/2504.12675]
8. [inference] Poor optimisation or small sample size can aggravate predictive fragility, but they do not fully explain it because deployment-divergent behaviour can persist even after strong held-out validation when the selected rule depends on unstable context. [source: https://www.jmlr.org/papers/v23/20-1335.html; https://pmc.ncbi.nlm.nih.gov/articles/PMC10499849/; https://arxiv.org/abs/2410.19575]
9. [inference] Invariant Risk Minimisation (IRM) is a genuine partial alternative because it can improve shift robustness by enforcing cross-environment invariance without a full mechanistic model, yet its need for multiple heterogeneous environments shows that pooled predictive fit alone does not identify stability. [source: https://arxiv.org/abs/1907.02893; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq2-1-erm-causal-blindness.md]
10. [inference] This item therefore extends Research Questions 2.1, 2.2, and 1.3 by showing that causal blindness and underdetermination have a dynamical consequence, namely qualitative fragility under perturbation when no invariant mechanism has been learned and no extra invariance signal has been supplied. [source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq2-1-erm-causal-blindness.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq2-2-duhem-quine-underdetermination.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq1-3-instrumentalism-failure-modes.md; http://www.scholarpedia.org/article/Structural_stability]

**Evidence map:**

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [fact] Structural stability concerns persistence of qualitative orbit structure under perturbations of the governing system. | http://www.scholarpedia.org/article/Structural_stability | high | Direct definition. |
| [fact] The planar criterion requires hyperbolicity and no saddle connections. | http://www.scholarpedia.org/article/Structural_stability | high | Direct historical theorem summary. |
| [fact] Underspecified pipelines can yield deployment-divergent predictors with similar held-out scores. | https://www.jmlr.org/papers/v23/20-1335.html | high | Primary empirical and conceptual source. |
| [fact] Shortcut learning and simplicity bias make unstable contextual cues attractive learning targets. | https://arxiv.org/abs/2004.07780 ; https://openreview.net/forum?id=VCnuSuDSHv | medium | Two independent sources on mechanism and optimisation. |
| [fact] Routine distribution shifts can cause material predictive degradation. | https://pmc.ncbi.nlm.nih.gov/articles/PMC10499849/ ; https://arxiv.org/abs/2410.19575 | medium | Empirical healthcare deployment evidence. |
| [inference] Mechanistic models are stronger than interpolators when they encode a reason for perturbation resilience. | http://www.scholarpedia.org/article/Structural_stability ; https://www.jmlr.org/papers/v23/20-1335.html | medium | Cross-domain synthesis. |
| [fact] Physics-constrained learning can outperform existing data-driven estimators while using governing constraints. | https://arxiv.org/abs/2504.12675 | medium | Single primary source. |
| [inference] Strong held-out validation does not reduce fragility to poor optimisation or small sample size when unstable context still drives the learned rule. | https://www.jmlr.org/papers/v23/20-1335.html ; https://pmc.ncbi.nlm.nih.gov/articles/PMC10499849/ ; https://arxiv.org/abs/2410.19575 | medium | Rival explanation tested and narrowed. |
| [inference] Invariant Risk Minimisation is a partial non-mechanistic route to better shift robustness, but it requires environment heterogeneity beyond pooled predictive fit. | https://arxiv.org/abs/1907.02893 ; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq2-1-erm-causal-blindness.md | medium | Alternative remedy acknowledged. |
| [inference] Research Questions 2.1, 2.2, and 1.3 imply a dynamical fragility result when invariant structure is missing. | https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq2-1-erm-causal-blindness.md ; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq2-2-duhem-quine-underdetermination.md ; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq1-3-instrumentalism-failure-modes.md ; http://www.scholarpedia.org/article/Structural_stability | medium | Repository synthesis plus external theory. |

**Assumptions:**

- [assumption] The comparison between mechanistic and purely predictive models is meant at the level of encoded constraints and invariance claims, not as a universal claim that every model with neural components is fragile. [source: https://arxiv.org/abs/2504.12675; https://www.jmlr.org/papers/v23/20-1335.html]
- [assumption] The open-access sources consulted are sufficient to capture the core argument of the seeded Thom, Strogatz, and Sugiyama books, because the key substantive claims used in this item are independently supported by the accessible structural-stability and distribution-shift literature. [source: http://www.scholarpedia.org/article/Structural_stability; https://doi.org/10.7551/mitpress/9780262017091.001.0001; https://archive.org/details/structuralstabil0000thom; https://www.hachettebookgroup.com/titles/steven-h-strogatz/nonlinear-dynamics-and-chaos/9780813349107/]

**Analysis:**

- [inference] The most secure part of the argument is the dynamical-systems side, because the structural-stability definition and planar criterion are stated directly in an authoritative mathematical source. [source: http://www.scholarpedia.org/article/Structural_stability]
- [inference] The machine-learning side is also strong on the negative claim, many equally accurate models are unstable under shift, because underspecification, shortcut learning, and deployment-shift evidence all converge on that result from different directions. [source: https://www.jmlr.org/papers/v23/20-1335.html; https://arxiv.org/abs/2004.07780; https://pmc.ncbi.nlm.nih.gov/articles/PMC10499849/; https://arxiv.org/abs/2410.19575]
- [inference] Poor optimisation, weak regularisation, or limited data are plausible alternative explanations, but the cited underspecification and deployment-shift results show that fragility can remain even after conventional validation succeeds, so the problem is not reducible to undertraining alone. [source: https://www.jmlr.org/papers/v23/20-1335.html; https://pmc.ncbi.nlm.nih.gov/articles/PMC10499849/; https://arxiv.org/abs/2410.19575]
- [inference] Invariant Risk Minimisation is the strongest rival remedy considered here, because it can improve robustness without a full mechanistic model, but its dependence on multiple environments shows that some extra invariance signal must still be supplied beyond pooled fit, which is consistent with Research Question 1.3 rather than a rebuttal to it. [source: https://arxiv.org/abs/1907.02893; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq1-3-instrumentalism-failure-modes.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq2-1-erm-causal-blindness.md]
- [inference] The positive mechanistic comparison is somewhat narrower, because the strongest open-access example available here is a recent physics-constrained learning paper rather than a broad benchmark family across many scientific domains. [source: https://arxiv.org/abs/2504.12675]
- [inference] Even so, the comparison is decision-useful because the question asks for a formal distinction, and the formal distinction is clear: one model class encodes perturbation-resilient structure, while the other can remain observationally successful without proving that the same structure was learned. [source: http://www.scholarpedia.org/article/Structural_stability; https://www.jmlr.org/papers/v23/20-1335.html]

**Risks, gaps, uncertainties:**

- [inference] The historical claim about the 1937 Andronov-Pontryagin note is medium confidence rather than high confidence because no accessible public copy of the original paper was located in this session, so the theorem is taken from Scholarpedia's historical summary rather than from the primary note itself. [source: http://www.scholarpedia.org/article/Structural_stability]
- [inference] The mechanistic-versus-black-box comparison is stronger as a formal and conceptual result than as a broad empirical benchmark claim, because the concrete comparison relies mainly on one recent physics-constrained primary study. [source: https://arxiv.org/abs/2504.12675]
- [inference] Distribution-shift evidence clearly establishes fragility in practice, but it does not by itself quantify a universal threshold at which a small perturbation becomes a qualitative behavioral change for every model family. [source: https://pmc.ncbi.nlm.nih.gov/articles/PMC10499849/; https://arxiv.org/abs/2410.19575]

**Open questions:**

- How can one define a machine-learning analogue of structural stability that is precise enough to test on learned predictors rather than on hand-specified dynamical systems?
- Which benchmark families best distinguish perturbation-resilient mechanistic learning from merely robust shortcut learning?
- When do physics-informed or causal-constraint methods preserve the right mechanism, and when do they simply hard-code the wrong one more confidently?

### §7 Recursive Review

- Review result: pass
- Acronym audit: Empirical Risk Minimisation (ERM) expanded on first use; no unexpanded high-risk abbreviations remain in Research Skill Output or Findings
- Claim-label audit: all visible claims in Research Skill Output carry [fact], [inference], or [assumption] labels; workflow notes remain metadata fragments
- Findings and synthesis parity: aligned
- Prior-work cross-check: Research Questions 2.1 and 2.2 cited directly; Research Question 1.3 retained as related rather than directly cited
- Confidence assessment: medium, because the structural-stability core is strongly sourced but the mechanistic-versus-black-box comparison remains partly inferential

---

## Findings

### Executive Summary

A model anchored in invariant governing structure is formally more stable under small perturbations than a purely predictive interpolator, because structural stability preserves qualitative orbit geometry while shortcut-compatible predictors can change behaviour when the deployment context moves. [inference; source: http://www.scholarpedia.org/article/Structural_stability; https://www.jmlr.org/papers/v23/20-1335.html; https://arxiv.org/abs/2004.07780]

In planar dynamical systems, the Andronov-Pontryagin criterion characterises structural stability through hyperbolic equilibria and periodic orbits together with the absence of saddle connections. [fact; source: http://www.scholarpedia.org/article/Structural_stability]

In modern machine learning, underspecification, shortcut learning, and distribution shift show that many predictors with equally good held-out performance can behave differently in deployment because their apparent success depends on unstable contextual cues. [fact; source: https://www.jmlr.org/papers/v23/20-1335.html; https://arxiv.org/abs/2004.07780; https://pmc.ncbi.nlm.nih.gov/articles/PMC10499849/]

Poor optimisation or limited data can worsen that fragility, but they do not exhaust it, because deployment-divergent predictors can still emerge after strong held-out validation when the learned rule depends on unstable contextual structure. [inference; source: https://www.jmlr.org/papers/v23/20-1335.html; https://pmc.ncbi.nlm.nih.gov/articles/PMC10499849/; https://arxiv.org/abs/2410.19575]

Invariant Risk Minimisation (IRM) is one partial alternative route to shift robustness because it searches for cross-environment stable features without requiring a full mechanistic model, but its need for heterogeneous environments reinforces Research Question 1.3's conclusion that predictive fit alone does not supply the missing stability information. [inference; source: https://arxiv.org/abs/1907.02893; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq1-3-instrumentalism-failure-modes.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq2-1-erm-causal-blindness.md]

### Key Findings

1. **Structural stability is a property of the governing dynamical system, not of one observed trajectory, because it asks whether nearby vector fields preserve the same qualitative orbit structure up to topological equivalence.** ([fact]; medium confidence; source: http://www.scholarpedia.org/article/Structural_stability)
2. **The planar Andronov-Pontryagin criterion ties that stability to hyperbolic equilibria and periodic orbits together with the absence of saddle connections, which are exactly the conditions that block qualitative phase-portrait change under small perturbations.** ([fact]; medium confidence; source: http://www.scholarpedia.org/article/Structural_stability)
3. **Purely predictive machine-learning pipelines are often underspecified, meaning they can produce multiple models with equally strong held-out performance that nevertheless diverge in deployment.** ([fact]; medium confidence; source: https://www.jmlr.org/papers/v23/20-1335.html)
4. **Shortcut learning and simplicity bias explain one route to that divergence, because models can adopt simple contextual cues that work on the training regime but fail under harder or shifted testing conditions.** ([fact]; medium confidence; source: https://arxiv.org/abs/2004.07780; https://openreview.net/forum?id=VCnuSuDSHv)
5. **Empirical deployment studies show that ordinary data shifts, such as temporal coding changes or demographic differences, can materially degrade predictive performance when the learned relation is not stable across environments.** ([fact]; medium confidence; source: https://pmc.ncbi.nlm.nih.gov/articles/PMC10499849/; https://arxiv.org/abs/2410.19575)
6. **A structurally stable mechanistic model is stronger than a high-accuracy interpolator because it encodes a reason that local perturbations should preserve behavior, whereas the interpolator only encodes that one observed regime was fitted.** ([inference]; medium confidence; source: http://www.scholarpedia.org/article/Structural_stability; https://www.jmlr.org/papers/v23/20-1335.html)
7. **Physics-constrained learning offers a concrete example of that contrast, because adding governing constraints can outperform existing data-driven estimators while explicitly tying the model to underlying system dynamics.** ([fact]; medium confidence; source: https://arxiv.org/abs/2504.12675)
8. **Poor optimisation or small sample size can aggravate predictive fragility, but they do not fully explain it because deployment-divergent behaviour can persist even after strong held-out validation when the selected rule depends on unstable context.** ([inference]; medium confidence; source: https://www.jmlr.org/papers/v23/20-1335.html; https://pmc.ncbi.nlm.nih.gov/articles/PMC10499849/; https://arxiv.org/abs/2410.19575)
9. **Invariant Risk Minimisation (IRM) is a genuine partial alternative because it can improve shift robustness by enforcing cross-environment invariance without a full mechanistic model, yet its need for multiple heterogeneous environments shows that pooled predictive fit alone does not identify stability.** ([inference]; medium confidence; source: https://arxiv.org/abs/1907.02893; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq2-1-erm-causal-blindness.md)
10. **This item therefore extends Research Questions 2.1, 2.2, and 1.3 by showing that causal blindness and underdetermination have a dynamical consequence, namely qualitative fragility under perturbation when no invariant mechanism has been learned and no extra invariance signal has been supplied.** ([inference]; medium confidence; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq2-1-erm-causal-blindness.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq2-2-duhem-quine-underdetermination.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq1-3-instrumentalism-failure-modes.md; http://www.scholarpedia.org/article/Structural_stability)

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [fact] Structural stability concerns persistence of qualitative orbit structure under perturbations of the governing system. | http://www.scholarpedia.org/article/Structural_stability | medium | Direct definition from one authoritative synthesis source. |
| [fact] The planar criterion requires hyperbolicity and no saddle connections. | http://www.scholarpedia.org/article/Structural_stability | medium | Direct historical theorem summary from one authoritative synthesis source. |
| [fact] Underspecified pipelines can yield deployment-divergent predictors with similar held-out scores. | https://www.jmlr.org/papers/v23/20-1335.html | medium | Primary empirical and conceptual source, but only one cited evidence family. |
| [fact] Shortcut learning and simplicity bias make unstable contextual cues attractive learning targets. | https://arxiv.org/abs/2004.07780 ; https://openreview.net/forum?id=VCnuSuDSHv | medium | Two independent sources on mechanism and optimisation. |
| [fact] Routine distribution shifts can cause material predictive degradation. | https://pmc.ncbi.nlm.nih.gov/articles/PMC10499849/ ; https://arxiv.org/abs/2410.19575 | medium | Empirical healthcare deployment evidence. |
| [inference] Mechanistic models are stronger than interpolators when they encode a reason for perturbation resilience. | http://www.scholarpedia.org/article/Structural_stability ; https://www.jmlr.org/papers/v23/20-1335.html | medium | Cross-domain synthesis. |
| [fact] Physics-constrained learning can outperform existing data-driven estimators while using governing constraints. | https://arxiv.org/abs/2504.12675 | medium | Single primary source. |
| [inference] Strong held-out validation does not reduce fragility to poor optimisation or small sample size when unstable context still drives the learned rule. | https://www.jmlr.org/papers/v23/20-1335.html ; https://pmc.ncbi.nlm.nih.gov/articles/PMC10499849/ ; https://arxiv.org/abs/2410.19575 | medium | Rival explanation tested and narrowed. |
| [inference] Invariant Risk Minimisation is a partial non-mechanistic route to better shift robustness, but it requires environment heterogeneity beyond pooled predictive fit. | https://arxiv.org/abs/1907.02893 ; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq2-1-erm-causal-blindness.md | medium | Alternative remedy acknowledged. |
| [inference] Research Questions 2.1, 2.2, and 1.3 imply a dynamical fragility result when invariant structure is missing. | https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq2-1-erm-causal-blindness.md ; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq2-2-duhem-quine-underdetermination.md ; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq1-3-instrumentalism-failure-modes.md ; http://www.scholarpedia.org/article/Structural_stability | medium | Repository synthesis plus external theory. |

### Assumptions

- [assumption] The comparison between mechanistic and purely predictive models is meant at the level of encoded constraints and invariance claims, not as a universal claim that every model with neural components is fragile. [source: https://arxiv.org/abs/2504.12675; https://www.jmlr.org/papers/v23/20-1335.html]
- [assumption] The open-access sources consulted are sufficient to capture the core argument of the seeded Thom, Strogatz, and Sugiyama books, because the key substantive claims used in this item are independently supported by the accessible structural-stability and distribution-shift literature. [source: http://www.scholarpedia.org/article/Structural_stability; https://doi.org/10.7551/mitpress/9780262017091.001.0001; https://archive.org/details/structuralstabil0000thom; https://www.hachettebookgroup.com/titles/steven-h-strogatz/nonlinear-dynamics-and-chaos/9780813349107/]

### Analysis

- The most secure part of the argument is the dynamical-systems side, because the structural-stability definition and planar criterion are stated directly in an authoritative mathematical source. [inference; source: http://www.scholarpedia.org/article/Structural_stability]
- The machine-learning side is also strong on the negative claim, many equally accurate models are unstable under shift, because underspecification, shortcut learning, and deployment-shift evidence all converge on that result from different directions. [inference; source: https://www.jmlr.org/papers/v23/20-1335.html; https://arxiv.org/abs/2004.07780; https://pmc.ncbi.nlm.nih.gov/articles/PMC10499849/; https://arxiv.org/abs/2410.19575]
- Poor optimisation, weak regularisation, or limited data are plausible alternative explanations, but the cited underspecification and deployment-shift results show that fragility can remain even after conventional validation succeeds, so the problem is not reducible to undertraining alone. [inference; source: https://www.jmlr.org/papers/v23/20-1335.html; https://pmc.ncbi.nlm.nih.gov/articles/PMC10499849/; https://arxiv.org/abs/2410.19575]
- Invariant Risk Minimisation is the strongest rival remedy considered here, because it can improve robustness without a full mechanistic model, but its dependence on multiple environments shows that some extra invariance signal must still be supplied beyond pooled fit, which is consistent with Research Question 1.3 rather than a rebuttal to it. [inference; source: https://arxiv.org/abs/1907.02893; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq1-3-instrumentalism-failure-modes.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq2-1-erm-causal-blindness.md]
- The positive mechanistic comparison is somewhat narrower, because the strongest open-access example available here is a recent physics-constrained learning paper rather than a broad benchmark family across many scientific domains. [inference; source: https://arxiv.org/abs/2504.12675]
- Even so, the comparison is decision-useful because the question asks for a formal distinction, and the formal distinction is clear: one model class encodes perturbation-resilient structure, while the other can remain observationally successful without proving that the same structure was learned. [inference; source: http://www.scholarpedia.org/article/Structural_stability; https://www.jmlr.org/papers/v23/20-1335.html]

### Risks, Gaps, and Uncertainties

- The historical claim about the 1937 Andronov-Pontryagin note is medium confidence rather than high confidence because no accessible public copy of the original paper was located in this session, so the theorem is taken from Scholarpedia's historical summary rather than from the primary note itself. [inference; source: http://www.scholarpedia.org/article/Structural_stability]
- The mechanistic-versus-black-box comparison is stronger as a formal and conceptual result than as a broad empirical benchmark claim, because the concrete comparison relies mainly on one recent physics-constrained primary study. [inference; source: https://arxiv.org/abs/2504.12675]
- Distribution-shift evidence clearly establishes fragility in practice, but it does not by itself quantify a universal threshold at which a small perturbation becomes a qualitative behavioral change for every model family. [inference; source: https://pmc.ncbi.nlm.nih.gov/articles/PMC10499849/; https://arxiv.org/abs/2410.19575]

### Open Questions

- How can one define a machine-learning analogue of structural stability that is precise enough to test on learned predictors rather than on hand-specified dynamical systems?
- Which benchmark families best distinguish perturbation-resilient mechanistic learning from merely robust shortcut learning?
- When do physics-informed or causal-constraint methods preserve the right mechanism, and when do they simply hard-code the wrong one more confidently?

---

## Output

- Type: knowledge
- Description: This item distinguishes perturbation-resilient mechanistic modelling from observationally adequate but shift-fragile prediction by combining structural-stability theory with modern evidence on underspecification, shortcut learning, and deployment drift. [inference; source: http://www.scholarpedia.org/article/Structural_stability; https://www.jmlr.org/papers/v23/20-1335.html; https://arxiv.org/abs/2004.07780]
- Links:
  - http://www.scholarpedia.org/article/Structural_stability
  - https://www.jmlr.org/papers/v23/20-1335.html
  - https://arxiv.org/abs/2004.07780
