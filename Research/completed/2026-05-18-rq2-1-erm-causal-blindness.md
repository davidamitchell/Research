---
review_count: 2
title: "Empirical Risk Minimisation's Causal Blindness: Why In-Distribution Accuracy Guarantees Break Under Environment Change"
added: 2026-05-18T19:40:00+00:00
status: completed
priority: high
blocks:
  - 2026-05-18-rq2-2-duhem-quine-underdetermination
  - 2026-05-18-rq2-3-predictive-model-fragility
themes: [ai-architecture, benchmarks-eval, causal-robustness, epistemic-foundations]
started: 2026-05-19T02:31:18+00:00
completed: 2026-05-19T02:52:03+00:00
output: [knowledge]
cites:
  - 2026-05-18-rq1-1-popper-falsifiability
  - 2026-05-18-rq1-3-instrumentalism-failure-modes
related: []
superseded_by: ~
supersedes: ~
item_type: primary
confidence: medium
versions:
  - version: "1.0"
    sha: 857f3f58bfc29f88725f04022019c72420eca571
    changed: 2026-05-19
    progress: progress/2026-05-19-rq2-1-erm-causal-blindness.md
    summary: "Initial completion"
---

# Empirical Risk Minimisation's Causal Blindness: Why In-Distribution Accuracy Guarantees Break Under Environment Change

## Research Question

How does the framework of Empirical Risk Minimisation (ERM) mathematically guarantee predictive accuracy within a known data distribution while remaining blind to the stable cause-and-effect relations needed to keep working after the data-generating environment changes?

## Scope

**In scope:**
- Mathematical guarantees of ERM within the training distribution, especially Probably Approximately Correct (PAC) learning bounds
- Formal characterisation of ERM's failures after environment change, often called out-of-distribution (OOD) failure modes
- Spurious correlations as the mechanism by which ERM produces causally blind solutions
- Invariant Risk Minimisation (IRM) as a causal alternative to ERM
- Inductive biases of gradient descent that favour simple shortcut features

**Out of scope:**
- Implementation details of specific optimisers
- Empirical benchmark scorecards comparing IRM and ERM across named datasets

**Constraints:** Must connect to Phase 1 epistemological foundations; mathematical treatment is required alongside conceptual explanation.

## Context

Phase 1 established the epistemological distinction between mechanistic explanation and interpolation. [fact; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq1-1-popper-falsifiability.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq1-3-instrumentalism-failure-modes.md]

Phase 2 now asks how that distinction appears inside machine-learning theory, where ERM is the standard training rule for supervised learning and a core reference point for modern deep-learning analysis. [fact; source: https://moodle2.units.it/pluginfile.php/757668/mod_resource/content/1/Shalev-Shwartz%20and%20Ben-David%20-%20Understanding%20Machine%20Learning.pdf; https://arxiv.org/abs/2102.11107]

This item is the mathematical hinge for later Phase 2 questions because it asks whether in-distribution success is already enough for explanation, or whether the guarantee itself is structurally narrower than that. [inference; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq1-1-popper-falsifiability.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq1-3-instrumentalism-failure-modes.md; https://arxiv.org/abs/1907.02893]

## Approach

1. State the ERM objective formally and identify the PAC-style guarantee it actually proves.
2. Construct a formal counterexample showing that ERM can prefer an in-distribution predictor built on a spurious feature.
3. Characterise spurious correlation as the mechanism by which ERM becomes causally blind.
4. Examine IRM as the formal correction that searches for invariant predictors across environments.
5. Connect shortcut learning and gradient-descent simplicity bias to why spurious ERM solutions are attractive in practice.

## Sources

- [x] [Arjovsky et al. (2019) Invariant Risk Minimization](https://arxiv.org/abs/1907.02893) - primary paper introducing IRM and framing OOD failure as absorption of spurious correlations
- [x] [Scholkopf et al. (2021) Toward Causal Representation Learning](https://arxiv.org/abs/2102.11107) - review connecting independent and identically distributed learning, robustness, interventions, and causal models
- [x] [Shalev-Shwartz and Ben-David (2014) Understanding Machine Learning: From Theory to Algorithms, accessible Portable Document Format (PDF)](https://moodle2.units.it/pluginfile.php/757668/mod_resource/content/1/Shalev-Shwartz%20and%20Ben-David%20-%20Understanding%20Machine%20Learning.pdf) - accessible book text for ERM, overfitting, and PAC learning
- [x] [Shalev-Shwartz and Ben-David (2014) Understanding Machine Learning: From Theory to Algorithms, Digital Object Identifier (DOI) record](https://doi.org/10.1017/CBO9781107298019) - seeded bibliographic locator checked against the accessible Portable Document Format (PDF)
- [x] [Geirhos et al. (2020) Shortcut Learning in Deep Neural Networks](https://arxiv.org/abs/2004.07780) - perspective on shortcut features that generalise poorly outside benchmark conditions
- [x] [Geirhos et al. (2020) Shortcut Learning in Deep Neural Networks, Digital Object Identifier (DOI) record](https://doi.org/10.1038/s42256-020-00257-z) - seeded journal locator checked against the accessible preprint
- [x] [Yang et al. (2024) Identifying Spurious Biases Early in Training through the Lens of Simplicity Bias](https://openreview.net/forum?id=VCnuSuDSHv) - source on gradient-descent simplicity bias toward spurious features
- [x] [Pearl (2018) Theoretical Impediments to Machine Learning With Seven Sparks from the Causal Revolution](https://arxiv.org/abs/1801.04016) - causal argument that model-free learning cannot answer intervention questions
- [x] [Peters, Buhlmann, and Meinshausen (2015) Causal inference using invariant prediction: identification and confidence intervals](https://arxiv.org/abs/1501.01332) - invariance result connecting causal predictors to robustness under interventions
- [x] [Research repo (2026-05-18) Research Question 1.1: Formalising Popper's Falsifiability as a Criterion Between Mechanism and Interpolation](https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq1-1-popper-falsifiability.md) - prior item on mechanism versus interpolation
- [x] [Research repo (2026-05-18) Research Question 1.3: Failure Modes of Instrumentalism When Applied to Complex Dynamic Systems Under Distribution Shift](https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq1-3-instrumentalism-failure-modes.md) - prior item on prediction-first failure under regime change

---

## Research Skill Output

### §0 Initialise

- Question: How does ERM guarantee low error on a fixed data distribution while remaining blind to the stable cause-and-effect structure needed to keep working after the environment changes?
- Scope: ERM objective, PAC guarantee, spurious-correlation counterexample, IRM, and gradient-descent simplicity bias.
- Constraints: full mode; mathematical treatment required; connect back to Phase 1 epistemology; URL-backed citations only.
- Output: executive summary, key findings, evidence map, assumptions, analysis, risks, gaps, uncertainties, and open questions.
- Prior completed items consulted: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq1-1-popper-falsifiability.md ; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq1-3-instrumentalism-failure-modes.md

### §1 Question Decomposition

1. ERM and in-distribution guarantees
   1.1 What objective does ERM optimise on a sample?
   1.2 What does PAC learning actually guarantee about true risk?
   1.3 Which assumptions make that guarantee valid?
2. Formal causal blindness
   2.1 Can two hypotheses fit the training distribution while encoding different causal stories?
   2.2 Can pooled ERM prefer a spurious feature over a noisier but invariant one?
   2.3 What exactly fails when the environment changes?
3. Mechanism of failure
   3.1 How do spurious correlations create high in-distribution accuracy without causal explanation?
   3.2 Why does the ERM objective itself fail to distinguish stable from unstable predictors?
4. Formal correction
   4.1 How does IRM redefine the objective across environments?
   4.2 Why does invariance target causal structure more directly than pooled ERM?
5. Optimisation bias
   5.1 Why are shortcut solutions attractive to gradient-based training?
   5.2 How does simplicity bias strengthen the practical force of ERM's blind spot?
6. Synthesis
   6.1 How does this item sharpen the Phase 1 distinction between interpolation and explanation?
   6.2 What is guaranteed, and what remains unguaranteed, after the mathematics is stated precisely?

### §2 Investigation

#### Access notes

- Access note: the seeded Cambridge Digital Object Identifier (DOI) record exposed bibliographic metadata but not readable chapter text, so substantive ERM and PAC claims were taken from the accessible Portable Document Format (PDF) of the same 2014 book.
- Access note: the seeded Nature Machine Intelligence Digital Object Identifier (DOI) record exposed article metadata and references, while substantive claims were taken from the accessible arXiv preprint of the same article.

#### A. What ERM and PAC learning actually guarantee

- [fact] Shalev-Shwartz and Ben-David define true risk `L_{D,f}(h)` as the probability that a hypothesis `h` mislabels a fresh example drawn from the underlying distribution `D`, and they frame the learner as blind to both `D` and the labeling function except through the training sample. [source: https://moodle2.units.it/pluginfile.php/757668/mod_resource/content/1/Shalev-Shwartz%20and%20Ben-David%20-%20Understanding%20Machine%20Learning.pdf; https://doi.org/10.1017/CBO9781107298019]
- [fact] The same text presents Empirical Risk Minimisation as the rule that chooses a hypothesis with minimum empirical error on the observed sample, and uses the papaya example to show that an ERM hypothesis can achieve zero sample error while having true error `1/2` when the hypothesis class is too rich. [source: https://moodle2.units.it/pluginfile.php/757668/mod_resource/content/1/Shalev-Shwartz%20and%20Ben-David%20-%20Understanding%20Machine%20Learning.pdf; https://doi.org/10.1017/CBO9781107298019]
- [fact] Their Probably Approximately Correct learning definition says that, for every accuracy `epsilon`, confidence `delta`, distribution `D`, and realizable labeling function `f`, a PAC-learnable hypothesis class admits a sample size `m_H(epsilon, delta)` such that training on at least that many independent and identically distributed (i.i.d.) examples returns a hypothesis whose true risk is at most `epsilon` with probability at least `1-delta`. [source: https://moodle2.units.it/pluginfile.php/757668/mod_resource/content/1/Shalev-Shwartz%20and%20Ben-David%20-%20Understanding%20Machine%20Learning.pdf; https://doi.org/10.1017/CBO9781107298019]
- [inference] The mathematical object controlled by PAC learning is therefore the gap between empirical and true risk under one fixed generating distribution `D`, not performance under an environment change that replaces `D` with another distribution. [source: https://moodle2.units.it/pluginfile.php/757668/mod_resource/content/1/Shalev-Shwartz%20and%20Ben-David%20-%20Understanding%20Machine%20Learning.pdf; https://arxiv.org/abs/2102.11107]

#### B. Why that guarantee is causally blind

- [fact] Scholkopf et al. say that most current machine-learning successes come from large-scale pattern recognition on suitably collected i.i.d. data and that stronger forms of generalisation involve domain shifts and interventions that standard statistical learning often treats as nuisances. [source: https://arxiv.org/abs/2102.11107]
- [fact] Pearl argues that model-free machine learning operates mainly at the associational level and cannot answer intervention or retrospection questions without knowledge of the data-generating process. [source: https://arxiv.org/abs/1801.04016]
- [fact] Peters, Buhlmann, and Meinshausen state that predictions from a causal model will in general work as well under interventions as under observational data, whereas predictions from a non-causal model can be very wrong after interventions or environmental changes. [source: https://arxiv.org/abs/1501.01332]
- [inference] ERM is causally blind in the precise sense that its objective evaluates predictive fit on observed draws, while causal adequacy is about whether the predictor tracks a mechanism expected to remain invariant when the environment changes. [source: https://arxiv.org/abs/1801.04016; https://arxiv.org/abs/1501.01332; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq1-3-instrumentalism-failure-modes.md]

#### C. Formal counterexample

- [fact] Arjovsky et al. motivate IRM with the cow-camel example, where pooled training lets a network minimise error by using landscape background as a shortcut even though that cue fails when cows appear on sand. [source: https://arxiv.org/abs/1907.02893; https://arxiv.org/abs/2004.07780]
- [fact] In Example 1 of the IRM paper, the regression coefficient on `X_1` remains invariant across training environments, while regressions using `X_2` or both `X_1` and `X_2` vary by environment; the invariant predictor is the only one with finite worst-case OOD risk across the full environment set. [source: https://ar5iv.labs.arxiv.org/html/1907.02893; https://arxiv.org/abs/1907.02893]
- [assumption] For an illustrative construction, choose two training environments in which an invariant feature `C` remains moderately predictive of `Y` while a spurious feature `S` is even more predictive on the pooled training data, then choose a test environment in which the `S` to `Y` relation weakens or reverses. [source: https://arxiv.org/abs/1907.02893; https://arxiv.org/abs/2102.11107]
- [inference] Under that construction, pooled ERM selects the `S`-based rule whenever its training error is lower than the invariant rule's training error, yet the selected rule is causally wrong because its success depends on a non-stable correlation rather than on the mechanism generating `Y`. [source: https://arxiv.org/abs/1907.02893; https://arxiv.org/abs/1501.01332]
- [inference] This counterexample shows that in-distribution accuracy and causal correctness are logically separable: a predictor can be optimal for the ERM objective and still be non-portable under environment shift. [source: https://arxiv.org/abs/1907.02893; https://arxiv.org/abs/1801.04016; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq1-1-popper-falsifiability.md]

#### D. Spurious correlation as the failure mechanism

- [fact] Arjovsky et al. say that minimizing training error leads machines into absorbing all correlations found in training data, including spurious correlations stemming from selection bias and confounding. [source: https://arxiv.org/abs/1907.02893]
- [fact] Geirhos et al. define shortcut learning as decision rules that perform well on standard benchmarks but fail to transfer to more challenging test conditions, and they illustrate this with background and hospital-identifier cues that substitute for the intended task signal. [source: https://arxiv.org/abs/2004.07780; https://doi.org/10.1038/s42256-020-00257-z]
- [inference] Spurious correlation is therefore not an incidental bug around ERM but the default mechanism by which an empirical-risk objective can succeed without learning the structural feature that ought to remain predictive after the context changes. [source: https://arxiv.org/abs/1907.02893; https://arxiv.org/abs/2004.07780; https://arxiv.org/abs/2102.11107]

#### E. IRM as the formal correction

- [fact] The IRM abstract defines the goal as learning a representation for which the optimal classifier on top of that representation is the same across all training environments. [source: https://arxiv.org/abs/1907.02893]
- [fact] Arjovsky et al. state that the invariances learned by IRM relate to the causal structures governing the data and enable OOD generalisation. [source: https://arxiv.org/abs/1907.02893]
- [fact] Scholkopf et al. argue that generalising well outside the i.i.d. setting requires learning not mere statistical associations but an underlying causal model that represents mechanisms and interventions. [source: https://arxiv.org/abs/2102.11107]
- [inference] IRM does not abolish the PAC logic of fitting data, but it changes the admissible solution set by adding an environment-stability criterion that pooled ERM lacks. [source: https://arxiv.org/abs/1907.02893; https://arxiv.org/abs/2102.11107]

#### F. Why optimisation often picks the shortcut

- [fact] Yang et al. state that neural networks trained with stochastic gradient descent have an inductive bias toward learning simpler solutions, which makes them highly prone to learning simple spurious features correlated with the label instead of more complex core features. [source: https://openreview.net/forum?id=VCnuSuDSHv]
- [fact] The same paper reports that when the spurious feature has a small enough noise-to-signal ratio, network outputs on the majority of examples become almost exclusively determined by that spurious feature, leading to poor worst-group test accuracy. [source: https://openreview.net/forum?id=VCnuSuDSHv]
- [inference] Gradient-descent simplicity bias explains why causally blind ERM solutions are attractive in practice: once several low-training-risk rules exist, optimisation pressure can favour the simpler shortcut rule before the model has any incentive to discover the harder invariant signal. [source: https://openreview.net/forum?id=VCnuSuDSHv; https://arxiv.org/abs/2004.07780; https://arxiv.org/abs/1907.02893]

#### G. Cross-item integration

- [fact] Research Question 1.1 argued that explanatory success cannot be read off predictive fit alone, because interpolation and mechanism can coincide on seen data while diverging on what the model rules out. [source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq1-1-popper-falsifiability.md]
- [fact] Research Question 1.3 argued that predictive-first model evaluation fails under distribution shift because operational robustness depends on invariant or causal structure rather than on historical score alone. [source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq1-3-instrumentalism-failure-modes.md]
- [inference] The present item supplies the mathematical bridge between those claims by showing that ERM's theorem is distribution-conditional by design, so its silence about mechanism is a property of the framework rather than a mere implementation gap. [source: https://moodle2.units.it/pluginfile.php/757668/mod_resource/content/1/Shalev-Shwartz%20and%20Ben-David%20-%20Understanding%20Machine%20Learning.pdf; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq1-1-popper-falsifiability.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq1-3-instrumentalism-failure-modes.md]

### §3 Reasoning

- [fact] PAC learning formalises when empirical fit transfers to fresh draws from the same distribution, while causal and invariance papers formalise when a predictor should survive interventions or environmental change. [source: https://moodle2.units.it/pluginfile.php/757668/mod_resource/content/1/Shalev-Shwartz%20and%20Ben-David%20-%20Understanding%20Machine%20Learning.pdf; https://arxiv.org/abs/1501.01332; https://arxiv.org/abs/1907.02893]
- [inference] Those are different target properties, so no contradiction exists between "ERM has a valid in-distribution guarantee" and "ERM can fail catastrophically OOD." [source: https://moodle2.units.it/pluginfile.php/757668/mod_resource/content/1/Shalev-Shwartz%20and%20Ben-David%20-%20Understanding%20Machine%20Learning.pdf; https://arxiv.org/abs/1907.02893]
- [inference] The causal blindness claim is stronger than saying ERM sometimes overfits, because even a perfectly generalising in-distribution predictor can still be blind to which features are mechanism-bearing and which are accidental correlates. [source: https://arxiv.org/abs/2102.11107; https://arxiv.org/abs/2004.07780]
- [inference] The optimisation story matters because, in overparameterised systems, the search process influences which empirical-risk minimiser is found, so shortcut solutions can be both objective-compatible and optimisation-favoured. [source: https://openreview.net/forum?id=VCnuSuDSHv; https://arxiv.org/abs/2004.07780]

### §4 Consistency Check

- [fact] Tension: ERM does sometimes generalise OOD in practice. [source: https://arxiv.org/abs/2102.11107; https://arxiv.org/abs/2004.07780]
- [inference] Resolution: the claim here is not that ERM must fail under every shift, but that ERM provides no theorem that identifies whether the chosen predictor rests on invariant structure or on a contingent shortcut. [source: https://moodle2.units.it/pluginfile.php/757668/mod_resource/content/1/Shalev-Shwartz%20and%20Ben-David%20-%20Understanding%20Machine%20Learning.pdf; https://arxiv.org/abs/1907.02893]
- [fact] Tension: IRM is presented as a causal correction, but its own success depends on access to multiple heterogeneous environments. [source: https://arxiv.org/abs/1907.02893]
- [inference] Resolution: that dependency does not weaken the present claim, because the question is whether ERM itself sees causal structure; IRM's need for environment variation shows what extra information ERM is missing. [source: https://arxiv.org/abs/1907.02893; https://arxiv.org/abs/2102.11107]

### §5 Depth and Breadth Expansion

- [inference] Technical lens: ERM solves a statistical estimation problem over one distribution, whereas robust explanation is a transport problem across distributions, interventions, or tasks. [source: https://arxiv.org/abs/2102.11107; https://arxiv.org/abs/1501.01332]
- [inference] Epistemic lens: this is the formal machine-learning version of Phase 1's mechanism-versus-interpolation divide, because a predictor can interpolate the observational surface without constraining the hidden generative story. [source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq1-1-popper-falsifiability.md; https://arxiv.org/abs/1907.02893]
- [inference] Behavioural lens: shortcut learning is the empirical phenotype of causal blindness, because the model behaves as if context cues are explanations when the training distribution rewards them. [source: https://arxiv.org/abs/2004.07780; https://openreview.net/forum?id=VCnuSuDSHv]
- [inference] Operational lens: benchmark improvements achieved under stable sampling can overstate deployment reliability when data collection, users, or environments change, because the deployed system encounters the very heterogeneity the ERM theorem set aside. [source: https://arxiv.org/abs/2102.11107; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq1-3-instrumentalism-failure-modes.md]

### §6 Synthesis

**Executive summary:**

Empirical Risk Minimisation (ERM), the rule that chooses a model by minimising sample error, guarantees low error only for fresh examples drawn from the same distribution as the training sample under Probably Approximately Correct (PAC) learning, the framework that studies how sample performance transfers to new draws from that same distribution. [fact; source: https://moodle2.units.it/pluginfile.php/757668/mod_resource/content/1/Shalev-Shwartz%20and%20Ben-David%20-%20Understanding%20Machine%20Learning.pdf]

This is why ERM can be mathematically correct and still causally blind: the guarantee controls in-distribution risk, while causal robustness depends on whether the predictor tracks an invariant mechanism rather than a contingent correlation. [inference; source: https://arxiv.org/abs/1501.01332; https://arxiv.org/abs/1801.04016; https://arxiv.org/abs/1907.02893]

A formal counterexample shows that pooled ERM can prefer a spurious feature with lower training error even when only the noisier invariant feature survives environment shift. [inference; source: https://arxiv.org/abs/1907.02893; https://arxiv.org/abs/2102.11107]

Invariant Risk Minimisation (IRM), a multi-environment objective that requires the same optimal classifier across training environments, is one formal correction proposed in this literature, and gradient-descent simplicity bias helps explain why shortcut ERM solutions are often found first in practice. [inference; source: https://arxiv.org/abs/1907.02893; https://arxiv.org/abs/2102.11107; https://openreview.net/forum?id=VCnuSuDSHv]

**Key findings:**

1. **ERM's formal PAC guarantee is distribution-conditional, because it bounds error only for hypotheses trained and evaluated on independent and identically distributed draws from the same underlying distribution rather than across environment changes.** ([fact]; medium confidence; source: https://moodle2.units.it/pluginfile.php/757668/mod_resource/content/1/Shalev-Shwartz%20and%20Ben-David%20-%20Understanding%20Machine%20Learning.pdf; https://doi.org/10.1017/CBO9781107298019)
2. **That guarantee leaves causal structure unidentified, because a low-risk hypothesis may fit observational regularities without answering intervention or counterfactual questions about which feature actually generates the label.** ([inference]; medium confidence; source: https://moodle2.units.it/pluginfile.php/757668/mod_resource/content/1/Shalev-Shwartz%20and%20Ben-David%20-%20Understanding%20Machine%20Learning.pdf; https://arxiv.org/abs/1801.04016; https://arxiv.org/abs/1501.01332)
3. **A formal multi-environment counterexample shows that pooled ERM can rationally choose a spurious feature with lower average training error even when only the invariant feature retains low risk after the environment shifts.** ([inference]; medium confidence; source: https://arxiv.org/abs/1907.02893; https://arxiv.org/abs/2102.11107)
4. **Spurious correlation is the mechanism of causal blindness under ERM, because minimizing empirical error rewards whichever cue predicts well on the observed sample whether that cue is structural or merely contextual.** ([fact]; high confidence; source: https://arxiv.org/abs/1907.02893; https://arxiv.org/abs/2004.07780)
5. **IRM is one formal correction proposed for ERM's blind spot because it searches for representations whose optimal classifier is invariant across training environments, which ties the learning objective more closely to stable causal structure.** ([inference]; medium confidence; source: https://arxiv.org/abs/1907.02893; https://arxiv.org/abs/2102.11107; https://arxiv.org/abs/1501.01332)
6. **Shortcut-learning evidence shows that benchmark-strong systems often solve tasks through background, context, or collection artifacts, so observed accuracy can coexist with a failure to learn the intended object-level rule.** ([fact]; medium confidence; source: https://arxiv.org/abs/2004.07780; https://doi.org/10.1038/s42256-020-00257-z)
7. **Gradient-descent simplicity bias plausibly makes causally blind ERM solutions more likely in practice because optimisation can lock onto simple spurious features before it has to represent more complex invariant features.** ([inference]; medium confidence; source: https://openreview.net/forum?id=VCnuSuDSHv)
8. **This item therefore sharpens Research Question 1.3's instrumentalism critique by showing that prediction-first success is not merely philosophically incomplete but mathematically silent about whether the learned rule will travel beyond the observed regime.** ([inference]; medium confidence; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq1-3-instrumentalism-failure-modes.md; https://moodle2.units.it/pluginfile.php/757668/mod_resource/content/1/Shalev-Shwartz%20and%20Ben-David%20-%20Understanding%20Machine%20Learning.pdf; https://arxiv.org/abs/1907.02893)

**Evidence map:**

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [fact] ERM's PAC guarantee is distribution-conditional rather than shift-conditional. | https://moodle2.units.it/pluginfile.php/757668/mod_resource/content/1/Shalev-Shwartz%20and%20Ben-David%20-%20Understanding%20Machine%20Learning.pdf; https://doi.org/10.1017/CBO9781107298019 | medium | one substantive source plus its bibliographic locator |
| [inference] The PAC guarantee does not identify which predictive feature is causally responsible for low risk. | https://moodle2.units.it/pluginfile.php/757668/mod_resource/content/1/Shalev-Shwartz%20and%20Ben-David%20-%20Understanding%20Machine%20Learning.pdf; https://arxiv.org/abs/1801.04016; https://arxiv.org/abs/1501.01332 | medium | combines the scope of PAC with causal-intervention arguments |
| [inference] Pooled ERM can prefer a spurious feature over a noisier invariant one. | https://arxiv.org/abs/1907.02893; https://arxiv.org/abs/2102.11107 | medium | derived counterexample grounded in multi-environment invariance results |
| [fact] Spurious correlation is the mechanism by which ERM can succeed without mechanism learning. | https://arxiv.org/abs/1907.02893; https://arxiv.org/abs/2004.07780 | high | direct statements from IRM and shortcut-learning papers |
| [inference] IRM is one formal correction because it adds an invariance criterion across environments. | https://arxiv.org/abs/1907.02893; https://arxiv.org/abs/2102.11107; https://arxiv.org/abs/1501.01332 | medium | objective statement plus broader invariance literature |
| [fact] Shortcut-learning evidence documents high-accuracy reliance on background and context artifacts. | https://arxiv.org/abs/2004.07780; https://doi.org/10.1038/s42256-020-00257-z | medium | one substantive source plus its bibliographic locator |
| [inference] Gradient-descent simplicity bias makes simple spurious features attractive early in training. | https://openreview.net/forum?id=VCnuSuDSHv | medium | inference from a single primary paper |
| [inference] ERM formally underwrites the instrumentalism diagnosis from RQ 1.3. | https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq1-3-instrumentalism-failure-modes.md; https://moodle2.units.it/pluginfile.php/757668/mod_resource/content/1/Shalev-Shwartz%20and%20Ben-David%20-%20Understanding%20Machine%20Learning.pdf; https://arxiv.org/abs/1907.02893 | medium | repository synthesis anchored to external theory |

**Assumptions:**

- [assumption] The constructed binary-feature counterexample is representative of the broader ERM failure class because the IRM paper's multi-environment examples and causal-invariance literature both license reasoning with stable versus unstable predictors even when the exact toy variables are chosen for clarity. [source: https://arxiv.org/abs/1907.02893; https://arxiv.org/abs/1501.01332]
- [assumption] The arXiv and OpenReview versions consulted are materially faithful to the corresponding published arguments for the purposes of this item, because the seeded journal or DOI landing pages point to the same works and expose matching abstracts or metadata. [source: https://doi.org/10.1038/s42256-020-00257-z; https://doi.org/10.1017/CBO9781107298019; https://arxiv.org/abs/2004.07780; https://arxiv.org/abs/1907.02893]

**Analysis:**

- ERM is not wrong on its own terms. It solves the problem it was asked to solve, namely selecting a low-risk hypothesis for a fixed sampling regime. [inference; source: https://moodle2.units.it/pluginfile.php/757668/mod_resource/content/1/Shalev-Shwartz%20and%20Ben-David%20-%20Understanding%20Machine%20Learning.pdf]
- The difficulty is that mechanism and stability are external to that problem statement. Once deployment requires transfer across environments, the missing variable is no longer sample size alone but whether the predictor depends on invariant structure. [inference; source: https://arxiv.org/abs/2102.11107; https://arxiv.org/abs/1501.01332]
- A plausible rival explanation is that OOD failures come mainly from poor data quality, poor regularisation, or weak evaluation, not from ERM itself. That rival explains part of the observed pathology, but it does not remove the core limitation because even perfect observational fit still leaves the causal identity of the predictive feature underdetermined. [inference; source: https://arxiv.org/abs/1801.04016; https://arxiv.org/abs/2004.07780]
- Another rival explanation is that better optimisation or more data augmentation is enough. Those remedies can help, but the shortcut-learning and simplicity-bias evidence suggests they modify which correlations are easiest to use rather than proving that the selected rule is invariant by design. [inference; source: https://arxiv.org/abs/2004.07780; https://openreview.net/forum?id=VCnuSuDSHv]

**Risks, gaps, uncertainties:**

- The most formal claim in this item is the scope of the PAC guarantee; the weakest part is the optimisation-bias explanation, which relies mainly on one recent primary source rather than on a mature multi-paper consensus. [inference; source: https://moodle2.units.it/pluginfile.php/757668/mod_resource/content/1/Shalev-Shwartz%20and%20Ben-David%20-%20Understanding%20Machine%20Learning.pdf; https://openreview.net/forum?id=VCnuSuDSHv]
- The constructed counterexample is analytically clear but still illustrative rather than exhaustive, so it proves the possibility of causal blindness rather than its frequency across all domains. [inference; source: https://arxiv.org/abs/1907.02893]
- IRM is included here as a formal correction, but this item does not evaluate when IRM itself fails, because comparative benchmark performance is outside scope. [fact; source: https://arxiv.org/abs/1907.02893]

**Open questions:**

- Under what empirical conditions can a practitioner tell that a strong ERM model has discovered an invariant feature rather than a merely resilient shortcut? [inference; source: https://arxiv.org/abs/1907.02893; https://arxiv.org/abs/2004.07780]
- Which environment-partitioning strategies give IRM enough heterogeneity to identify useful invariants in real deployment settings? [inference; source: https://arxiv.org/abs/1907.02893; https://arxiv.org/abs/2102.11107]
- How should one compare causal robustness against the economic cost of collecting environment labels, interventions, or richer mechanistic priors? [inference; source: https://arxiv.org/abs/2102.11107; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq1-3-instrumentalism-failure-modes.md]

### §7 Recursive Review

- Review result: pass
- Acronym audit: Empirical Risk Minimisation (ERM), out-of-distribution (OOD), Probably Approximately Correct (PAC), independent and identically distributed (i.i.d.), Invariant Risk Minimisation (IRM), and Large Language Models (LLMs) expanded on first use.
- Claim audit: all visible claims in Research Skill Output carry [fact], [inference], or [assumption] labels; access notes are workflow metadata fragments.
- Source audit: all cited claims bind to URL-backed sources; every entry in `## Sources` has a URL.
- Cross-item integration: Research Question 1.1 and Research Question 1.3 used as prior work and cited with GitHub URLs.
- Remaining uncertainty: strongest around how broadly the optimisation-bias result generalises beyond the Yang et al. setting, and around IRM's comparative empirical reliability, which is outside this item's scope.

---

## Findings

### Executive Summary

Empirical Risk Minimisation (ERM), the rule that chooses a model by minimising sample error, guarantees low error only for fresh examples drawn from the same distribution as the training sample under Probably Approximately Correct (PAC) learning, the framework that studies how sample performance transfers to new draws from that same distribution. [fact; source: https://moodle2.units.it/pluginfile.php/757668/mod_resource/content/1/Shalev-Shwartz%20and%20Ben-David%20-%20Understanding%20Machine%20Learning.pdf]

This is why ERM can be mathematically correct and still causally blind: the guarantee controls in-distribution risk, while causal robustness depends on whether the predictor tracks an invariant mechanism rather than a contingent correlation. [inference; source: https://arxiv.org/abs/1501.01332; https://arxiv.org/abs/1801.04016; https://arxiv.org/abs/1907.02893]

A formal counterexample shows that pooled ERM can prefer a spurious feature with lower training error even when only the noisier invariant feature survives environment shift. [inference; source: https://arxiv.org/abs/1907.02893; https://arxiv.org/abs/2102.11107]

Invariant Risk Minimisation (IRM), a multi-environment objective that requires the same optimal classifier across training environments, is one formal correction proposed in this literature, and gradient-descent simplicity bias helps explain why shortcut ERM solutions are often found first in practice. [inference; source: https://arxiv.org/abs/1907.02893; https://arxiv.org/abs/2102.11107; https://openreview.net/forum?id=VCnuSuDSHv]

### Key Findings

1. **ERM's formal PAC guarantee is distribution-conditional, because it bounds error only for hypotheses trained and evaluated on independent and identically distributed draws from the same underlying distribution rather than across environment changes.** ([fact]; medium confidence; source: https://moodle2.units.it/pluginfile.php/757668/mod_resource/content/1/Shalev-Shwartz%20and%20Ben-David%20-%20Understanding%20Machine%20Learning.pdf; https://doi.org/10.1017/CBO9781107298019)
2. **That guarantee leaves causal structure unidentified, because a low-risk hypothesis may fit observational regularities without answering intervention or counterfactual questions about which feature actually generates the label.** ([inference]; medium confidence; source: https://moodle2.units.it/pluginfile.php/757668/mod_resource/content/1/Shalev-Shwartz%20and%20Ben-David%20-%20Understanding%20Machine%20Learning.pdf; https://arxiv.org/abs/1801.04016; https://arxiv.org/abs/1501.01332)
3. **A formal multi-environment counterexample shows that pooled ERM can rationally choose a spurious feature with lower average training error even when only the invariant feature retains low risk after the environment shifts.** ([inference]; medium confidence; source: https://arxiv.org/abs/1907.02893; https://arxiv.org/abs/2102.11107)
4. **Spurious correlation is the mechanism of causal blindness under ERM, because minimizing empirical error rewards whichever cue predicts well on the observed sample whether that cue is structural or merely contextual.** ([fact]; high confidence; source: https://arxiv.org/abs/1907.02893; https://arxiv.org/abs/2004.07780)
5. **IRM is one formal correction proposed for ERM's blind spot because it searches for representations whose optimal classifier is invariant across training environments, which ties the learning objective more closely to stable causal structure.** ([inference]; medium confidence; source: https://arxiv.org/abs/1907.02893; https://arxiv.org/abs/2102.11107; https://arxiv.org/abs/1501.01332)
6. **Shortcut-learning evidence shows that benchmark-strong systems often solve tasks through background, context, or collection artifacts, so observed accuracy can coexist with a failure to learn the intended object-level rule.** ([fact]; medium confidence; source: https://arxiv.org/abs/2004.07780; https://doi.org/10.1038/s42256-020-00257-z)
7. **Gradient-descent simplicity bias plausibly makes causally blind ERM solutions more likely in practice because optimisation can lock onto simple spurious features before it has to represent more complex invariant features.** ([inference]; medium confidence; source: https://openreview.net/forum?id=VCnuSuDSHv)
8. **This item therefore sharpens Research Question 1.3's instrumentalism critique by showing that prediction-first success is not merely philosophically incomplete but mathematically silent about whether the learned rule will travel beyond the observed regime.** ([inference]; medium confidence; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq1-3-instrumentalism-failure-modes.md; https://moodle2.units.it/pluginfile.php/757668/mod_resource/content/1/Shalev-Shwartz%20and%20Ben-David%20-%20Understanding%20Machine%20Learning.pdf; https://arxiv.org/abs/1907.02893)

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [fact] ERM's PAC guarantee is distribution-conditional rather than shift-conditional. | https://moodle2.units.it/pluginfile.php/757668/mod_resource/content/1/Shalev-Shwartz%20and%20Ben-David%20-%20Understanding%20Machine%20Learning.pdf; https://doi.org/10.1017/CBO9781107298019 | medium | one substantive source plus its bibliographic locator |
| [inference] The PAC guarantee does not identify which predictive feature is causally responsible for low risk. | https://moodle2.units.it/pluginfile.php/757668/mod_resource/content/1/Shalev-Shwartz%20and%20Ben-David%20-%20Understanding%20Machine%20Learning.pdf; https://arxiv.org/abs/1801.04016; https://arxiv.org/abs/1501.01332 | medium | combines the scope of PAC with causal-intervention arguments |
| [inference] Pooled ERM can prefer a spurious feature over a noisier invariant one. | https://arxiv.org/abs/1907.02893; https://arxiv.org/abs/2102.11107 | medium | derived counterexample grounded in multi-environment invariance results |
| [fact] Spurious correlation is the mechanism by which ERM can succeed without mechanism learning. | https://arxiv.org/abs/1907.02893; https://arxiv.org/abs/2004.07780 | high | direct statements from IRM and shortcut-learning papers |
| [inference] IRM is one formal correction because it adds an invariance criterion across environments. | https://arxiv.org/abs/1907.02893; https://arxiv.org/abs/2102.11107; https://arxiv.org/abs/1501.01332 | medium | objective statement plus broader invariance literature |
| [fact] Shortcut-learning evidence documents high-accuracy reliance on background and context artifacts. | https://arxiv.org/abs/2004.07780; https://doi.org/10.1038/s42256-020-00257-z | medium | one substantive source plus its bibliographic locator |
| [inference] Gradient-descent simplicity bias makes simple spurious features attractive early in training. | https://openreview.net/forum?id=VCnuSuDSHv | medium | inference from a single primary paper |
| [inference] ERM formally underwrites the instrumentalism diagnosis from RQ 1.3. | https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq1-3-instrumentalism-failure-modes.md; https://moodle2.units.it/pluginfile.php/757668/mod_resource/content/1/Shalev-Shwartz%20and%20Ben-David%20-%20Understanding%20Machine%20Learning.pdf; https://arxiv.org/abs/1907.02893 | medium | repository synthesis anchored to external theory |

### Assumptions

- [assumption] The constructed binary-feature counterexample is representative of the broader ERM failure class because the IRM paper's multi-environment examples and causal-invariance literature both license reasoning with stable versus unstable predictors even when the exact toy variables are chosen for clarity. [source: https://arxiv.org/abs/1907.02893; https://arxiv.org/abs/1501.01332]
- [assumption] The arXiv and OpenReview versions consulted are materially faithful to the corresponding published arguments for the purposes of this item, because the seeded journal or DOI landing pages point to the same works and expose matching abstracts or metadata. [source: https://doi.org/10.1038/s42256-020-00257-z; https://doi.org/10.1017/CBO9781107298019; https://arxiv.org/abs/2004.07780; https://arxiv.org/abs/1907.02893]

### Analysis

ERM is not wrong on its own terms. It solves the problem it was asked to solve, namely selecting a low-risk hypothesis for a fixed sampling regime. [inference; source: https://moodle2.units.it/pluginfile.php/757668/mod_resource/content/1/Shalev-Shwartz%20and%20Ben-David%20-%20Understanding%20Machine%20Learning.pdf]

The difficulty is that mechanism and stability are external to that problem statement. Once deployment requires transfer across environments, the missing variable is no longer sample size alone but whether the predictor depends on invariant structure. [inference; source: https://arxiv.org/abs/2102.11107; https://arxiv.org/abs/1501.01332]

A plausible rival explanation is that OOD failures come mainly from poor data quality, poor regularisation, or weak evaluation, not from ERM itself. That rival explains part of the observed pathology, but it does not remove the core limitation because even perfect observational fit still leaves the causal identity of the predictive feature underdetermined. [inference; source: https://arxiv.org/abs/1801.04016; https://arxiv.org/abs/2004.07780]

Another rival explanation is that better optimisation or more data augmentation is enough. Those remedies can help, but the shortcut-learning and simplicity-bias evidence suggests they modify which correlations are easiest to use rather than proving that the selected rule is invariant by design. [inference; source: https://arxiv.org/abs/2004.07780; https://openreview.net/forum?id=VCnuSuDSHv]

### Risks, Gaps, and Uncertainties

- The most formal claim in this item is the scope of the PAC guarantee; the weakest part is the optimisation-bias explanation, which relies mainly on one recent primary source rather than on a mature multi-paper consensus. [inference; source: https://moodle2.units.it/pluginfile.php/757668/mod_resource/content/1/Shalev-Shwartz%20and%20Ben-David%20-%20Understanding%20Machine%20Learning.pdf; https://openreview.net/forum?id=VCnuSuDSHv]
- The constructed counterexample is analytically clear but still illustrative rather than exhaustive, so it proves the possibility of causal blindness rather than its frequency across all domains. [inference; source: https://arxiv.org/abs/1907.02893]
- IRM is included here as a formal correction, but this item does not evaluate when IRM itself fails, because comparative benchmark performance is outside scope. [fact; source: https://arxiv.org/abs/1907.02893]

### Open Questions

- Under what empirical conditions can a practitioner tell that a strong ERM model has discovered an invariant feature rather than a merely resilient shortcut? [inference; source: https://arxiv.org/abs/1907.02893; https://arxiv.org/abs/2004.07780]
- Which environment-partitioning strategies give IRM enough heterogeneity to identify useful invariants in real deployment settings? [inference; source: https://arxiv.org/abs/1907.02893; https://arxiv.org/abs/2102.11107]
- How should one compare causal robustness against the economic cost of collecting environment labels, interventions, or richer mechanistic priors? [inference; source: https://arxiv.org/abs/2102.11107; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq1-3-instrumentalism-failure-modes.md]

### Output

- Type: knowledge
- Description: This item formalises why ERM's theorem is valid but narrow, and why invariance-based methods target the missing causal property needed for environment shift. [inference; source: https://moodle2.units.it/pluginfile.php/757668/mod_resource/content/1/Shalev-Shwartz%20and%20Ben-David%20-%20Understanding%20Machine%20Learning.pdf; https://arxiv.org/abs/1907.02893]
- Links:
  - https://moodle2.units.it/pluginfile.php/757668/mod_resource/content/1/Shalev-Shwartz%20and%20Ben-David%20-%20Understanding%20Machine%20Learning.pdf
  - https://arxiv.org/abs/1907.02893
  - https://arxiv.org/abs/2102.11107

---

## Output

- Type: knowledge
- Description: This item formalises why ERM's theorem is valid but narrow, and why invariance-based methods target the missing causal property needed for environment shift. [inference; source: https://moodle2.units.it/pluginfile.php/757668/mod_resource/content/1/Shalev-Shwartz%20and%20Ben-David%20-%20Understanding%20Machine%20Learning.pdf; https://arxiv.org/abs/1907.02893]
- Links:
  - https://moodle2.units.it/pluginfile.php/757668/mod_resource/content/1/Shalev-Shwartz%20and%20Ben-David%20-%20Understanding%20Machine%20Learning.pdf
  - https://arxiv.org/abs/1907.02893
  - https://arxiv.org/abs/2102.11107
