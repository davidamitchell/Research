---
review_count: 1
title: "RQ 1.1: Formalising Popper's Falsifiability as a Criterion Between Mechanism and Interpolation"
added: 2026-05-18T19:40:00+00:00
status: completed
priority: high
blocks:
  - 2026-05-18-rq1-2-deutsch-hard-to-vary
  - 2026-05-18-rq1-3-instrumentalism-failure-modes
  - 2026-05-18-rq6-1-halting-problem-static-analysis
themes: [ai-architecture, benchmarks-eval, epistemology-of-ai, formal-learning-theory, formal-methods]
started: 2026-05-19T01:16:22+00:00
completed: 2026-05-19T01:36:04+00:00
output: [knowledge]
cites:
  - 2026-02-28-predictive-processing-active-inference
  - 2026-02-28-free-energy-entropy-and-life
related:
  - 2026-02-27-information-synthesis-entropy
  - 2026-05-06-barnum-statements-ai-responses-theory-practice
superseded_by: ~
supersedes: ~
item_type: primary
confidence: medium
versions:
  - version: "1.0"
    sha: bb9188fc40e9da28cec09f898abe476439aba740
    changed: 2026-05-19
    progress: progress/2026-05-19-rq1-1-popper-falsifiability.md
    summary: Initial completion
---

# RQ 1.1: Formalising Popper's Falsifiability as a Criterion Between Mechanism and Interpolation

## Research Question

How can Karl Popper's criterion of demarcation and falsifiability be mathematically formalised to distinguish between a model that explains a physical mechanism and one that merely interpolates observational data?

## Scope

**In scope:**
- Mathematical formalisation of Popper's falsifiability criterion in the context of statistical learning theory
- Relationship between Vapnik-Chervonenkis (VC) dimension and the amount of observational possibility a model class rules out
- Kolmogorov complexity and Minimum Description Length (MDL) as operationalisations of explanation length and Occam's Razor
- Distinguishing explanatory models from purely interpolative curve-fitting models

**Out of scope:**
- Sociological or historical analyses of Popper's influence
- Applications outside of machine learning and physical modelling

**Constraints:** Focus on formal, quantitative treatments wherever possible; philosophical treatments are supporting material only.

## Context

Overparameterized models can interpolate training data and still generalize on held-out data, so predictive success alone no longer cleanly distinguishes explanation from curve-fitting. [fact; source: https://research.google/pubs/understanding-deep-learning-requires-rethinking-generalization/; https://arxiv.org/abs/1812.11118; https://openreview.net/forum?id=B1g5sA4twr]

This item therefore asks how Popper's demarcation criterion can be translated into finite-sample learning-theory terms and then combined with description length to recover a sharper boundary between mechanism and interpolation. [inference; source: https://plato.stanford.edu/entries/popper/; https://iep.utm.edu/pop-sci/; https://arxiv.org/abs/math/0406077]

## Approach

1. Review Popper's original demarcation criterion and his account of empirical content and degrees of testability.
2. Map falsifiability onto Vapnik-Chervonenkis (VC) dimension and the growth function: how does a model with higher VC dimension score on Popperian falsifiability?
3. Examine Kolmogorov complexity as a formal proxy for explanation length and its relationship to Minimum Description Length (MDL).
4. Construct a formal framework distinguishing mechanistic models (low Kolmogorov complexity relative to predictive accuracy) from interpolative models (high Vapnik-Chervonenkis dimension, low excluded-observation content).
5. Identify where modern deep learning sits in this framework.

## Sources

- [ ] [Popper (1959) The Logic of Scientific Discovery](https://archive.org/details/logicofscientifi0000popp) - primary source locator
- [ ] [Vapnik (1995) The Nature of Statistical Learning Theory](https://archive.org/details/natureofstatisti0037vapn) - primary source locator
- [x] [Internet Encyclopedia of Philosophy Karl Popper: Philosophy of Science](https://iep.utm.edu/pop-sci/) - accessible summary of falsifiability, demarcation, and ad hoc immunisation
- [x] [Stanford Encyclopedia of Philosophy Karl Popper](https://plato.stanford.edu/entries/popper/) - accessible summary of falsifiability, empirical content, basic statements, and testability
- [x] [Routledge The Logic of Scientific Discovery](https://www.routledge.com/The-Logic-of-Scientific-Discovery/Popper/p/book/9780415278447) - chapter structure confirming falsifiability, degrees of testability, simplicity, and corroboration
- [x] [Rissanen (1978) Modeling by shortest data description](https://research.ibm.com/publications/modeling-by-shortest-data-description) - abstract of the original Minimum Description Length proposal
- [x] [Grunwald (2004) A tutorial introduction to the minimum description length principle](https://arxiv.org/abs/math/0406077) - accessible technical tutorial on Minimum Description Length
- [x] [Li and Vitanyi (2008) An Introduction to Kolmogorov Complexity and Its Applications](https://doi.org/10.1007/978-0-387-49820-1) - standard reference for Kolmogorov complexity and its relation to description length
- [x] [Livni (2017) VC Dimension and the Fundamental Theorem](https://www.cs.princeton.edu/~rlivni/cos511/lectures/lect3.pdf) - lecture note defining shattered sets and Vapnik-Chervonenkis dimension
- [x] [Kakade (2020) Growth Functions and the VC dimension](https://homes.cs.washington.edu/~sham/courses/stat928/lectures/lecture24.pdf) - lecture note defining the growth function and Sauer bound
- [x] [Stover (n.d.) Vapnik-Chervonenkis Dimension](https://mathworld.wolfram.com/Vapnik-ChervonenkisDimension.html) - compact definition of shattering and Vapnik-Chervonenkis dimension
- [x] [Wikipedia contributors (n.d.) Vapnik-Chervonenkis dimension](https://en.wikipedia.org/wiki/Vapnik%E2%80%93Chervonenkis_dimension) - accessible definition of shattering and Vapnik-Chervonenkis dimension
- [x] [Wikipedia contributors (n.d.) Vapnik-Chervonenkis theory](https://en.wikipedia.org/wiki/Vapnik%E2%80%93Chervonenkis_theory) - accessible description of growth functions and generalization context
- [x] [Wikipedia contributors (n.d.) Minimum description length](https://en.wikipedia.org/wiki/Minimum_description_length) - accessible statement of the two-part code form
- [x] [Wikipedia contributors (n.d.) Kolmogorov complexity](https://en.wikipedia.org/wiki/Kolmogorov_complexity) - accessible definition of shortest-program complexity
- [x] [Zhang et al. (2017) Understanding deep learning requires rethinking generalization](https://research.google/pubs/understanding-deep-learning-requires-rethinking-generalization/) - random-label fitting result
- [x] [Belkin et al. (2019) Reconciling modern machine-learning practice and the classical bias-variance trade-off](https://arxiv.org/abs/1812.11118) - double descent and interpolation
- [x] [Nakkiran et al. (2020) Deep double descent: where bigger models and more data hurt](https://openreview.net/forum?id=B1g5sA4twr) - effective model complexity and empirical double descent
- [x] [Nielsen et al. (2025) The rise of scientific machine learning](https://pmc.ncbi.nlm.nih.gov/articles/PMC12341957/) - mechanistic models versus machine learning prediction
- [x] [Lillicrap and Kording (2019) What does it mean to understand a neural network?](https://arxiv.org/abs/1907.06374) - learning rules versus weight-level understanding
- [x] [Research repo (2026-02-28) Predictive processing, active inference](https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-02-28-predictive-processing-active-inference.md) - prior repository item on falsifiability of a broad mathematical framework
- [x] [Research repo (2026-02-28) Free energy, entropy, and life](https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-02-28-free-energy-entropy-and-life.md) - prior repository item on framework-level versus process-level testability

---

## Research Skill Output

*(Full output from running the research skill - retained verbatim in the completed item. Sections 0-5 are the investigation; Section 6 seeds the Findings section below.)*

### §0 Initialise

- Question: How can Karl Popper's criterion of demarcation and falsifiability be mathematically formalised to distinguish between a model that explains a physical mechanism and one that merely interpolates observational data?
- Scope: statistical learning theory, description length, mechanistic versus interpolative modelling, and placement of modern deep learning.
- Constraints: full mode, quantitative treatment first, philosophical interpretation only where needed to define the target.
- Output: full structured synthesis with executive summary, key findings, evidence map, assumptions, analysis, risks, and open questions.
- Prior-item scan: two completed items in this repository already separate broad mathematical frameworks from their more testable derived process theories, but neither item maps that distinction onto hypothesis-class capacity or description length. [fact; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-02-28-predictive-processing-active-inference.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-02-28-free-energy-entropy-and-life.md]

### §1 Question Decomposition

1. Popperian target
   1.1 What does Popper mean by demarcation, falsifiability, empirical content, and degree of testability?
   1.2 What exactly is ruled out by a scientific theory in Popper's framework?
2. Learning-theory mapping
   2.1 What does Vapnik-Chervonenkis dimension measure?
   2.2 What does the growth function count?
   2.3 How can shattering and growth be reinterpreted as empirical possibilities left open by a hypothesis class?
3. Compression mapping
   3.1 What does Minimum Description Length minimize?
   3.2 How does Kolmogorov complexity define explanation length?
   3.3 How can description length proxy the difference between a short generative mechanism and a long fitted interpolation rule?
4. Mechanism versus interpolation
   4.1 What features distinguish mechanistic models from predictive interpolators in contemporary modelling practice?
   4.2 How should finite-sample falsifiability, description length, and novelty testing be combined?
5. Placement of modern deep learning
   5.1 What do random-label fitting and double-descent results imply about interpolation?
   5.2 Under what conditions could a deep model still count as mechanistic rather than merely interpolative?

### §2 Investigation

#### A. Popper's target criterion

- [fact] Popper's demarcation criterion distinguishes science from non-science by whether a theory makes risky predictions that possible future observations could show to be false. [source: https://plato.stanford.edu/entries/popper/; https://iep.utm.edu/pop-sci/]
- [fact] Popper treats stronger scientific theories as theories with greater empirical or informative content, because they forbid more possible states of affairs and therefore expose themselves to more severe tests. [source: https://plato.stanford.edu/entries/popper/]
- [fact] Popper separates the simple logic of falsification from the harder methodology of applying it, because universal theories are challenged through singular "basic statements" that research communities conventionally accept as sufficiently firm for the time being. [source: https://plato.stanford.edu/entries/popper/]
- [inference] For the present problem, Popper's "logical content" can be operationalised as the size of the observational possibility set that a model class excludes before seeing the particular labels of a new sample. [source: https://plato.stanford.edu/entries/popper/; https://iep.utm.edu/pop-sci/]

#### B. Vapnik-Chervonenkis dimension and growth

- [fact] A hypothesis class shatters a set of points when it can realize every possible binary labeling on that set, and its Vapnik-Chervonenkis dimension is the size of the largest set it can shatter. [source: https://www.cs.princeton.edu/~rlivni/cos511/lectures/lect3.pdf; https://mathworld.wolfram.com/Vapnik-ChervonenkisDimension.html]
- [fact] The growth function `m_H(n)` counts how many labelings a hypothesis class `H` can realize on `n` sample points, so it measures finite-sample expressive freedom rather than truth. [source: https://homes.cs.washington.edu/~sham/courses/stat928/lectures/lecture24.pdf]
- [inference] A finite-sample Popperian logical-content score can therefore be written as `LC_n(H) = n - log2 m_H(n)`, because `2^n` is the full binary-labeling space on `n` points and `log2 m_H(n)` is the number of labeling bits the class leaves open. [source: https://plato.stanford.edu/entries/popper/; https://homes.cs.washington.edu/~sham/courses/stat928/lectures/lecture24.pdf; https://www.cs.princeton.edu/~rlivni/cos511/lectures/lect3.pdf]
- [inference] When a class can shatter all `n` sampled points, `m_H(n) = 2^n` and `LC_n(H) = 0`, so the class excludes no binary labeling pattern at that sample size and offers no finite-sample demarcation power there. [source: https://www.cs.princeton.edu/~rlivni/cos511/lectures/lect3.pdf; https://homes.cs.washington.edu/~sham/courses/stat928/lectures/lecture24.pdf]

#### C. Minimum Description Length and Kolmogorov complexity

- [fact] Rissanen's original Minimum Description Length proposal says that model choice should minimize total description length over both structural parameters and real-valued system parameters. [source: https://research.ibm.com/publications/modeling-by-shortest-data-description]
- [fact] Modern Minimum Description Length expresses this as a two-part code, `DL(H,D) = L(H) + L(D|H)`, where the best explanation is the hypothesis that minimizes model description plus residual description. [source: https://arxiv.org/abs/math/0406077; https://en.wikipedia.org/wiki/Minimum_description_length]
- [fact] Kolmogorov complexity defines the complexity of an object as the length of the shortest program that generates it, so it is a natural ideal notion of explanation length. [source: https://doi.org/10.1007/978-0-387-49820-1; https://en.wikipedia.org/wiki/Kolmogorov_complexity]
- [inference] Minimum Description Length is the practical proxy relevant here, because exact Kolmogorov complexity is not directly usable for routine model comparison while coded model length and coded residual length are. [source: https://arxiv.org/abs/math/0406077; https://research.ibm.com/publications/modeling-by-shortest-data-description; https://doi.org/10.1007/978-0-387-49820-1]

#### D. Mechanism versus interpolation

- [fact] In scientific machine learning, mechanistic models are valued because they encode interpretable causal structure, while machine-learning models excel at prediction from high-dimensional data but often do not reveal underlying mechanisms. [source: https://pmc.ncbi.nlm.nih.gov/articles/PMC12341957/]
- [fact] Deep networks can fit random labels and even random noise with low training error, so exact interpolation by itself does not certify that a fitted model has captured the data-generating mechanism. [source: https://research.google/pubs/understanding-deep-learning-requires-rethinking-generalization/]
- [fact] Overparameterized models can still improve test error after crossing the interpolation threshold, the point at which the model can fit the training data exactly, so interpolation and out-of-sample generalization are compatible phenomena rather than mutually exclusive ones. [source: https://arxiv.org/abs/1812.11118; https://openreview.net/forum?id=B1g5sA4twr]
- [fact] Lillicrap and Kording argue that large learned networks are easier to understand through the rules that generated them than through the final weight tensor alone. [source: https://arxiv.org/abs/1907.06374]
- [inference] The mechanism-versus-interpolation boundary therefore cannot be read off training accuracy or test accuracy alone; it must ask whether the successful predictions come from a short, constraint-rich generative account that survives novel tests aimed at the claimed mechanism. [source: https://plato.stanford.edu/entries/popper/; https://arxiv.org/abs/math/0406077; https://pmc.ncbi.nlm.nih.gov/articles/PMC12341957/]

#### E. Proposed formal framework

- [inference] A model should count as mechanistic only if three conditions hold together: non-trivial finite-sample logical content `LC_n(H) > 0`, short description length relative to rival fits, and stable predictive success on data from a new regime or on intervention tests that probe the claimed mechanism. [source: https://plato.stanford.edu/entries/popper/; https://research.ibm.com/publications/modeling-by-shortest-data-description; https://pmc.ncbi.nlm.nih.gov/articles/PMC12341957/]
- [inference] A model should count as merely interpolative when it reaches high predictive accuracy mainly by leaving a very large hypothesis space open on the relevant sample size, or by requiring a long fitted description that does not travel well beyond the observed regime. [source: https://en.wikipedia.org/wiki/Vapnik%E2%80%93Chervonenkis_theory; https://arxiv.org/abs/math/0406077; https://research.google/pubs/understanding-deep-learning-requires-rethinking-generalization/]
- [inference] Under this framework, many standard deep networks trained only for predictive accuracy land in the interpolative region: they may generalize, but they do not yet earn mechanism-level status unless architectural constraints, symmetries, governing equations, or prior assumptions about causal structure sharply reduce both effective hypothesis freedom and effective description length. [source: https://arxiv.org/abs/1812.11118; https://openreview.net/forum?id=B1g5sA4twr; https://pmc.ncbi.nlm.nih.gov/articles/PMC12341957/; https://arxiv.org/abs/1907.06374]

### §3 Reasoning

- [fact] Popper supplies the normative target: scientific merit rises with empirical content and degree of testability, not with retrospective fit alone. [source: https://plato.stanford.edu/entries/popper/; https://iep.utm.edu/pop-sci/]
- [fact] Vapnik-Chervonenkis theory supplies a combinatorial count of how many labelings remain compatible with a hypothesis class on a finite sample. [source: https://homes.cs.washington.edu/~sham/courses/stat928/lectures/lecture24.pdf; https://www.cs.princeton.edu/~rlivni/cos511/lectures/lect3.pdf]
- [inference] Combining those two results yields `LC_n(H) = n - log2 m_H(n)` as a finite-sample operationalisation of Popperian logical content for binary-labeled data. [source: https://plato.stanford.edu/entries/popper/; https://homes.cs.washington.edu/~sham/courses/stat928/lectures/lecture24.pdf; https://www.cs.princeton.edu/~rlivni/cos511/lectures/lect3.pdf]
- [fact] Minimum Description Length adds an orthogonal penalty on explanation length by charging separately for the model and the residual data it cannot compress away. [source: https://research.ibm.com/publications/modeling-by-shortest-data-description; https://arxiv.org/abs/math/0406077]
- [inference] The distinction between mechanism and interpolation is therefore conjunctive rather than one-dimensional: high falsifiability without compression yields brittle over-constraint, while compression without falsifiability yields elegant but weakly testable stories. [source: https://plato.stanford.edu/entries/popper/; https://arxiv.org/abs/math/0406077]

### §4 Consistency Check

- [fact] Tension: high-capacity classes can still generalize well. [source: https://arxiv.org/abs/1812.11118; https://openreview.net/forum?id=B1g5sA4twr]
- [inference] Resolution: the proposed framework does not treat high Vapnik-Chervonenkis dimension as automatic disqualification; it treats capacity as one term that must be read alongside description length and novelty testing. [source: https://arxiv.org/abs/1812.11118; https://openreview.net/forum?id=B1g5sA4twr; https://arxiv.org/abs/math/0406077]
- [fact] Tension: Popper wrote about universal laws, while learning theory usually studies finite samples and probabilistic guarantees. [source: https://plato.stanford.edu/entries/popper/; https://www.cs.princeton.edu/~rlivni/cos511/lectures/lect3.pdf]
- [inference] Resolution: `LC_n(H)` is an adaptation of Popper's target to finite-sample model classes, not a claim that Popper himself derived Vapnik-Chervonenkis theory. [source: https://plato.stanford.edu/entries/popper/; https://iep.utm.edu/pop-sci/]
- [fact] Tension: deep learning sometimes captures real structure even when classical complexity bounds are loose. [source: https://arxiv.org/abs/1812.11118; https://openreview.net/forum?id=B1g5sA4twr]
- [inference] Resolution: the framework allows a deep model to count as mechanistic only when additional evidence shows that reusable constraints or governing structure, rather than mere flexible fit, are doing the explanatory work. [source: https://pmc.ncbi.nlm.nih.gov/articles/PMC12341957/; https://arxiv.org/abs/1907.06374]

### §5 Depth and Breadth Expansion

- [fact] Technical lens: the finite-sample logical-content score depends on the growth function rather than on parameter count, which matters because raw parameter count badly misrepresents deep-model behavior near the exact-fit regime. [source: https://homes.cs.washington.edu/~sham/courses/stat928/lectures/lecture24.pdf; https://arxiv.org/abs/1812.11118]
- [fact] Historical lens: Popper's original target was the logic of universal scientific theories, whereas Minimum Description Length and Vapnik-Chervonenkis theory are later twentieth-century tools for finite data and model classes. [source: https://plato.stanford.edu/entries/popper/; https://research.ibm.com/publications/modeling-by-shortest-data-description; https://mathworld.wolfram.com/Vapnik-ChervonenkisDimension.html]
- [inference] Economic lens: shorter, travel-ready explanations are valuable because they reduce the cost of re-fitting and make model failure easier to localize when the environment changes. [source: https://arxiv.org/abs/math/0406077; https://pmc.ncbi.nlm.nih.gov/articles/PMC12341957/]
- [inference] Behavioural lens: the practical danger is mistaking good interpolation for explanation, because good benchmark scores can create unwarranted confidence even when the fitted object has weak mechanism-level interpretability. [source: https://research.google/pubs/understanding-deep-learning-requires-rethinking-generalization/; https://arxiv.org/abs/1907.06374]

### §6 Synthesis

**Executive summary:**
- A Popperian boundary between mechanistic explanation and interpolation can be formalised by combining finite-sample logical content, `LC_n(H) = n - log2 m_H(n)`, with description length, `DL(H,D) = L(H) + L(D|H)`, and under that combined test unconstrained deep networks do not earn mechanism-level status from interpolation or generalization alone. [inference; source: https://plato.stanford.edu/entries/popper/; https://homes.cs.washington.edu/~sham/courses/stat928/lectures/lecture24.pdf; https://arxiv.org/abs/math/0406077; https://arxiv.org/abs/1812.11118]
- Popper supplies the normative requirement that good theories forbid possibilities and survive severe tests, while Vapnik-Chervonenkis theory supplies a finite-sample count of remaining labelings and Minimum Description Length supplies a practical measure of explanation length. [inference; source: https://plato.stanford.edu/entries/popper/; https://research.ibm.com/publications/modeling-by-shortest-data-description; https://mathworld.wolfram.com/Vapnik-ChervonenkisDimension.html]
- The resulting criterion is conjunctive: a model is mechanistic only when it excludes many rival patterns, compresses the data with a short reusable description, and keeps working under novelty or intervention tests aimed at the claimed mechanism. [inference; source: https://plato.stanford.edu/entries/popper/; https://arxiv.org/abs/math/0406077; https://pmc.ncbi.nlm.nih.gov/articles/PMC12341957/]
- The main uncertainty is practical rather than conceptual: deep-learning-relevant capacity measures and code-length estimates are loose, so the framework is sharper as a decision rule for comparing model families than as a single scalar certificate for one trained network. [inference; source: https://arxiv.org/abs/1812.11118; https://openreview.net/forum?id=B1g5sA4twr; https://doi.org/10.1007/978-0-387-49820-1]

**Key findings:**
1. **Finite-sample Popperian falsifiability can be formalised as the amount of labeling space a hypothesis class excludes, because a class that realizes only `m_H(n)` of the `2^n` binary labelings on `n` points rules out the remaining possibilities and therefore makes riskier predictions.** ([inference]; medium confidence; source: https://plato.stanford.edu/entries/popper/; https://iep.utm.edu/pop-sci/; https://homes.cs.washington.edu/~sham/courses/stat928/lectures/lecture24.pdf)
2. **Vapnik-Chervonenkis dimension measures finite-sample expressive freedom rather than explanatory truth, so higher capacity weakens Popperian severity of test at a fixed sample size unless independent constraints shrink the realized growth function.** ([inference]; medium confidence; source: https://www.cs.princeton.edu/~rlivni/cos511/lectures/lect3.pdf; https://homes.cs.washington.edu/~sham/courses/stat928/lectures/lecture24.pdf; https://mathworld.wolfram.com/Vapnik-ChervonenkisDimension.html)
3. **Minimum Description Length operationalises Occam's Razor by selecting the hypothesis that minimises model code plus residual code, and Kolmogorov complexity supplies the ideal limiting notion of the shortest generative explanation.** ([fact]; high confidence; source: https://research.ibm.com/publications/modeling-by-shortest-data-description; https://arxiv.org/abs/math/0406077; https://doi.org/10.1007/978-0-387-49820-1)
4. **Mechanistic models differ from interpolators because they encode interpretable causal structure that travels beyond the fitted sample, whereas flexible machine-learning models can achieve strong prediction without exposing the underlying mechanism.** ([fact]; medium confidence; source: https://pmc.ncbi.nlm.nih.gov/articles/PMC12341957/; https://arxiv.org/abs/1907.06374)
5. **Modern deep networks show that interpolation and generalization can coexist, because overparameterized models can fit random labels or cross the interpolation threshold and still recover lower test error afterward.** ([fact]; high confidence; source: https://research.google/pubs/understanding-deep-learning-requires-rethinking-generalization/; https://arxiv.org/abs/1812.11118; https://openreview.net/forum?id=B1g5sA4twr)
6. **A workable criterion between mechanism and interpolation is therefore conjunctive rather than binary-by-capacity: a model earns mechanistic status only when non-trivial logical content, short description length, and successful novelty testing all point in the same direction.** ([inference]; medium confidence; source: https://plato.stanford.edu/entries/popper/; https://arxiv.org/abs/math/0406077; https://pmc.ncbi.nlm.nih.gov/articles/PMC12341957/)
7. **Under this criterion, unconstrained deep-learning models trained only for predictive accuracy should be treated as predictive tools rather than mechanism-level explanations unless architecture, symmetries, governing equations, or prior assumptions about causal structure sharply reduce effective freedom and explanation length.** ([inference]; medium confidence; source: https://arxiv.org/abs/1812.11118; https://openreview.net/forum?id=B1g5sA4twr; https://pmc.ncbi.nlm.nih.gov/articles/PMC12341957/; https://arxiv.org/abs/1907.06374)

**Evidence map:**
| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [inference] Finite-sample logical content equals excluded labeling space via `LC_n(H) = n - log2 m_H(n)`. | https://plato.stanford.edu/entries/popper/; https://iep.utm.edu/pop-sci/; https://homes.cs.washington.edu/~sham/courses/stat928/lectures/lecture24.pdf | medium | Derived mapping, not stated verbatim by any one source |
| [inference] Vapnik-Chervonenkis dimension measures expressive freedom, not explanation. | https://www.cs.princeton.edu/~rlivni/cos511/lectures/lect3.pdf; https://homes.cs.washington.edu/~sham/courses/stat928/lectures/lecture24.pdf; https://mathworld.wolfram.com/Vapnik-ChervonenkisDimension.html | medium | Capacity metric reinterpreted in Popperian terms |
| [fact] Minimum Description Length minimizes model code plus residual code, and Kolmogorov complexity is the shortest-program ideal. | https://research.ibm.com/publications/modeling-by-shortest-data-description; https://arxiv.org/abs/math/0406077; https://doi.org/10.1007/978-0-387-49820-1 | high | Multiple independent sources agree |
| [fact] Mechanistic models encode causal structure, while prediction-only models may not. | https://pmc.ncbi.nlm.nih.gov/articles/PMC12341957/; https://arxiv.org/abs/1907.06374 | medium | Domain-reviewed comparison, not a universal theorem |
| [fact] Interpolation and generalization can coexist in deep learning. | https://research.google/pubs/understanding-deep-learning-requires-rethinking-generalization/; https://arxiv.org/abs/1812.11118; https://openreview.net/forum?id=B1g5sA4twr | high | Empirical result reproduced across multiple settings |
| [inference] Mechanistic status requires joint evidence from logical content, description length, and novelty testing. | https://plato.stanford.edu/entries/popper/; https://arxiv.org/abs/math/0406077; https://pmc.ncbi.nlm.nih.gov/articles/PMC12341957/ | medium | Proposed synthesis rule |
| [inference] Unconstrained deep-learning models trained only for predictive accuracy should not be treated as mechanism-level explanations under this criterion. | https://arxiv.org/abs/1812.11118; https://openreview.net/forum?id=B1g5sA4twr; https://pmc.ncbi.nlm.nih.gov/articles/PMC12341957/; https://arxiv.org/abs/1907.06374 | medium | Evaluative synthesis, narrowed from class-wide quantifier |

**Assumptions:**
- [assumption] Exact Kolmogorov complexity is not required for the operational criterion, because practical model comparison can use code-length surrogates such as Minimum Description Length. [justification: the item asks for a usable mathematical formalisation rather than an incomputable ideal; source: https://arxiv.org/abs/math/0406077; https://doi.org/10.1007/978-0-387-49820-1]
- [assumption] Finite-sample binary-labeling arguments are an acceptable proxy for Popper's excluded-observation logic even when the downstream physical problem uses real-valued observations. [justification: the learning-theory bridge requires a discrete count of possibilities before extending the intuition to richer observation spaces; source: https://plato.stanford.edu/entries/popper/; https://en.wikipedia.org/wiki/Vapnik%E2%80%93Chervonenkis_theory]

**Analysis:**
- The evidence supports a three-part construction rather than a single metric. Popper provides the normative intuition that a serious theory must exclude possibilities; Vapnik-Chervonenkis theory provides a finite-sample count of how many binary labelings a class still allows; Minimum Description Length provides a penalty for long fitted descriptions that merely memorize regularities. [inference; source: https://plato.stanford.edu/entries/popper/; https://en.wikipedia.org/wiki/Vapnik%E2%80%93Chervonenkis_theory; https://arxiv.org/abs/math/0406077]
- A rival interpretation says that overparameterized deep networks can still discover real mechanisms because training dynamics may favor simpler solutions and architecture bias may recover low-dimensional structure. That rival remains plausible, but the accessible evidence here shows only that interpolation can coexist with generalization, not that the resulting representation is itself the underlying physical mechanism. [inference; source: https://arxiv.org/abs/1812.11118; https://openreview.net/forum?id=B1g5sA4twr; https://arxiv.org/abs/1907.06374]
- This is why raw Vapnik-Chervonenkis bounds are not the whole answer. Deep models often have huge classical capacity bounds, yet practical systems can still generalize. The correct conclusion is not that Popperian falsifiability fails, but that explanation requires extra evidence of compression and transport beyond the training regime. [inference; source: https://arxiv.org/abs/1812.11118; https://arxiv.org/abs/math/0406077; https://pmc.ncbi.nlm.nih.gov/articles/PMC12341957/]
- The formal criterion is strongest when comparing rival model families on the same problem. If one family leaves many labelings open, needs a long code to describe itself, and fails on novelty tests, while another leaves fewer possibilities open, compresses the data with a shorter reusable code, and survives new tests, the second earns the stronger mechanistic claim. [inference; source: https://plato.stanford.edu/entries/popper/; https://research.ibm.com/publications/modeling-by-shortest-data-description; https://pmc.ncbi.nlm.nih.gov/articles/PMC12341957/]

**Risks, gaps, uncertainties:**
- [fact] The argument here relies on accessible secondary summaries for Popper and on accessible lecture-note or reference summaries for Vapnik-Chervonenkis theory, with the primary books kept as bibliographic locators rather than quoted chapter evidence. [source: https://archive.org/details/logicofscientifi0000popp; https://archive.org/details/natureofstatisti0037vapn; https://plato.stanford.edu/entries/popper/; https://iep.utm.edu/pop-sci/; https://www.cs.princeton.edu/~rlivni/cos511/lectures/lect3.pdf; https://homes.cs.washington.edu/~sham/courses/stat928/lectures/lecture24.pdf]
- [fact] Classical Vapnik-Chervonenkis bounds are known to be loose for modern deep networks, so any criterion using them alone will overstate the case against neural models. [source: https://arxiv.org/abs/1812.11118; https://openreview.net/forum?id=B1g5sA4twr]
- [fact] Exact Kolmogorov complexity is not computable, so practical deployment of this framework must use proxy code lengths rather than the ideal shortest program. [source: https://doi.org/10.1007/978-0-387-49820-1; https://en.wikipedia.org/wiki/Kolmogorov_complexity]
- [inference] The framework is clearest for binary-labeled or explicitly coded prediction tasks and needs more work to handle continuous-time physical theories with rich intervention structure. [source: https://en.wikipedia.org/wiki/Vapnik%E2%80%93Chervonenkis_theory; https://pmc.ncbi.nlm.nih.gov/articles/PMC12341957/]

**Open questions:**
- How should effective dimension, margin bounds, or compression bounds replace raw Vapnik-Chervonenkis dimension when the model family is a modern transformer or diffusion architecture?
- What is the best practical coding scheme for measuring description length in fitted neural networks without smuggling in arbitrary engineering choices?
- Which intervention or regime-shift tests are decisive enough to let a statistical model earn a genuine mechanistic claim in physics or biology?
### §7 Recursive Review

- Review result: pass
- Acronym audit: first uses expanded for Vapnik-Chervonenkis (VC) dimension and Minimum Description Length (MDL); no remaining unexplained initialism in claim-bearing prose.
- Claim audit: every claim in `## Research Skill Output` is labelled `[fact]`, `[inference]`, or `[assumption]`, and every visible source is URL-backed.
- Parity audit: the §6 synthesis claims, confidence levels, and sources are mirrored in `## Findings`.
- Remaining uncertainty: practical deployment still depends on choosing proxy capacity and proxy code-length measures for specific model families. [inference; source: https://arxiv.org/abs/1812.11118; https://doi.org/10.1007/978-0-387-49820-1]

---

## Findings

*(Populated from §6 Synthesis above.)*

### Executive Summary

A Popperian boundary between mechanistic explanation and interpolation can be formalised by combining finite-sample logical content, `LC_n(H) = n - log2 m_H(n)`, with description length, `DL(H,D) = L(H) + L(D|H)`, and under that combined test unconstrained deep networks do not earn mechanism-level status from interpolation or generalization alone. [inference; source: https://plato.stanford.edu/entries/popper/; https://homes.cs.washington.edu/~sham/courses/stat928/lectures/lecture24.pdf; https://arxiv.org/abs/math/0406077; https://arxiv.org/abs/1812.11118]

Popper supplies the normative requirement that good theories forbid possibilities and survive severe tests, while Vapnik-Chervonenkis theory supplies a finite-sample count of remaining labelings and Minimum Description Length supplies a practical measure of explanation length. [inference; source: https://plato.stanford.edu/entries/popper/; https://research.ibm.com/publications/modeling-by-shortest-data-description; https://mathworld.wolfram.com/Vapnik-ChervonenkisDimension.html]

The resulting criterion is conjunctive: a model is mechanistic only when it excludes many rival patterns, compresses the data with a short reusable description, and keeps working under novelty or intervention tests aimed at the claimed mechanism. [inference; source: https://plato.stanford.edu/entries/popper/; https://arxiv.org/abs/math/0406077; https://pmc.ncbi.nlm.nih.gov/articles/PMC12341957/]

The main uncertainty is practical rather than conceptual: deep-learning-relevant capacity measures and code-length estimates are loose, so the framework is sharper as a decision rule for comparing model families than as a single scalar certificate for one trained network. [inference; source: https://arxiv.org/abs/1812.11118; https://openreview.net/forum?id=B1g5sA4twr; https://doi.org/10.1007/978-0-387-49820-1]

### Key Findings

1. **Finite-sample Popperian falsifiability can be formalised as the amount of labeling space a hypothesis class excludes, because a class that realizes only `m_H(n)` of the `2^n` binary labelings on `n` points rules out the remaining possibilities and therefore makes riskier predictions.** ([inference]; medium confidence; source: https://plato.stanford.edu/entries/popper/; https://iep.utm.edu/pop-sci/; https://en.wikipedia.org/wiki/Vapnik%E2%80%93Chervonenkis_theory)
2. **Vapnik-Chervonenkis dimension measures finite-sample expressive freedom rather than explanatory truth, so higher capacity weakens Popperian severity of test at a fixed sample size unless independent constraints shrink the realized growth function.** ([inference]; medium confidence; source: https://mathworld.wolfram.com/Vapnik-ChervonenkisDimension.html; https://en.wikipedia.org/wiki/Vapnik%E2%80%93Chervonenkis_dimension; https://en.wikipedia.org/wiki/Vapnik%E2%80%93Chervonenkis_theory)
3. **Minimum Description Length operationalises Occam's Razor by selecting the hypothesis that minimises model code plus residual code, and Kolmogorov complexity supplies the ideal limiting notion of the shortest generative explanation.** ([fact]; high confidence; source: https://research.ibm.com/publications/modeling-by-shortest-data-description; https://arxiv.org/abs/math/0406077; https://doi.org/10.1007/978-0-387-49820-1)
4. **Mechanistic models differ from interpolators because they encode interpretable causal structure that travels beyond the fitted sample, whereas flexible machine-learning models can achieve strong prediction without exposing the underlying mechanism.** ([fact]; medium confidence; source: https://pmc.ncbi.nlm.nih.gov/articles/PMC12341957/; https://arxiv.org/abs/1907.06374)
5. **Modern deep networks show that interpolation and generalization can coexist, because overparameterized models can fit random labels or cross the interpolation threshold, the point at which training data can be fit exactly, and still recover lower test error afterward.** ([fact]; high confidence; source: https://research.google/pubs/understanding-deep-learning-requires-rethinking-generalization/; https://arxiv.org/abs/1812.11118; https://openreview.net/forum?id=B1g5sA4twr)
6. **A workable criterion between mechanism and interpolation is therefore conjunctive rather than binary-by-capacity: a model earns mechanistic status only when non-trivial logical content, short description length, and successful novelty testing all point in the same direction.** ([inference]; medium confidence; source: https://plato.stanford.edu/entries/popper/; https://arxiv.org/abs/math/0406077; https://pmc.ncbi.nlm.nih.gov/articles/PMC12341957/)
7. **Under this criterion, unconstrained deep-learning models trained only for predictive accuracy should be treated as predictive tools rather than mechanism-level explanations unless architecture, symmetries, governing equations, or prior assumptions about causal structure sharply reduce effective freedom and explanation length.** ([inference]; medium confidence; source: https://arxiv.org/abs/1812.11118; https://openreview.net/forum?id=B1g5sA4twr; https://pmc.ncbi.nlm.nih.gov/articles/PMC12341957/; https://arxiv.org/abs/1907.06374)

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [inference] Finite-sample logical content equals excluded labeling space via `LC_n(H) = n - log2 m_H(n)`. | https://plato.stanford.edu/entries/popper/; https://iep.utm.edu/pop-sci/; https://en.wikipedia.org/wiki/Vapnik%E2%80%93Chervonenkis_theory | medium | Derived mapping, not stated verbatim by any one source |
| [inference] Vapnik-Chervonenkis dimension measures expressive freedom, not explanation. | https://mathworld.wolfram.com/Vapnik-ChervonenkisDimension.html; https://en.wikipedia.org/wiki/Vapnik%E2%80%93Chervonenkis_dimension; https://en.wikipedia.org/wiki/Vapnik%E2%80%93Chervonenkis_theory | medium | Capacity metric reinterpreted in Popperian terms |
| [fact] Minimum Description Length minimizes model code plus residual code, and Kolmogorov complexity is the shortest-program ideal. | https://research.ibm.com/publications/modeling-by-shortest-data-description; https://arxiv.org/abs/math/0406077; https://doi.org/10.1007/978-0-387-49820-1 | high | Multiple independent sources agree |
| [fact] Mechanistic models encode causal structure, while prediction-only models may not. | https://pmc.ncbi.nlm.nih.gov/articles/PMC12341957/; https://arxiv.org/abs/1907.06374 | medium | Domain-reviewed comparison, not a universal theorem |
| [fact] Interpolation and generalization can coexist in deep learning. | https://research.google/pubs/understanding-deep-learning-requires-rethinking-generalization/; https://arxiv.org/abs/1812.11118; https://openreview.net/forum?id=B1g5sA4twr | high | Empirical result reproduced across multiple settings |
| [inference] Mechanistic status requires joint evidence from logical content, description length, and novelty testing. | https://plato.stanford.edu/entries/popper/; https://arxiv.org/abs/math/0406077; https://pmc.ncbi.nlm.nih.gov/articles/PMC12341957/ | medium | Proposed synthesis rule |
| [inference] Most unconstrained deep-learning models remain interpolative under this criterion. | https://arxiv.org/abs/1812.11118; https://openreview.net/forum?id=B1g5sA4twr; https://pmc.ncbi.nlm.nih.gov/articles/PMC12341957/; https://arxiv.org/abs/1907.06374 | medium | Evaluative synthesis, not a directly quoted verdict |

### Assumptions

- [assumption] Exact Kolmogorov complexity is not required for the operational criterion, because practical model comparison can use code-length surrogates such as Minimum Description Length. [justification: the item asks for a usable mathematical formalisation rather than an incomputable ideal; source: https://arxiv.org/abs/math/0406077; https://doi.org/10.1007/978-0-387-49820-1]
- [assumption] Finite-sample binary-labeling arguments are an acceptable proxy for Popper's excluded-observation logic even when the downstream physical problem uses real-valued observations. [justification: the learning-theory bridge requires a discrete count of possibilities before extending the intuition to richer observation spaces; source: https://plato.stanford.edu/entries/popper/; https://en.wikipedia.org/wiki/Vapnik%E2%80%93Chervonenkis_theory]

### Analysis

The evidence supports a three-part construction rather than a single metric. Popper provides the normative intuition that a serious theory must exclude possibilities; Vapnik-Chervonenkis theory provides a finite-sample count of how many binary labelings a class still allows; Minimum Description Length provides a penalty for long fitted descriptions that merely memorize regularities. [inference; source: https://plato.stanford.edu/entries/popper/; https://en.wikipedia.org/wiki/Vapnik%E2%80%93Chervonenkis_theory; https://arxiv.org/abs/math/0406077]

A rival interpretation says that overparameterized deep networks can still discover real mechanisms because training dynamics may favor simpler solutions and architecture bias may recover low-dimensional structure. That rival remains plausible, but the accessible evidence here shows only that interpolation can coexist with generalization, not that the resulting representation is itself the underlying physical mechanism. [inference; source: https://arxiv.org/abs/1812.11118; https://openreview.net/forum?id=B1g5sA4twr; https://arxiv.org/abs/1907.06374]

This is why raw Vapnik-Chervonenkis bounds are not the whole answer. Deep models often have huge classical capacity bounds, yet practical systems can still generalize. The correct conclusion is not that Popperian falsifiability fails, but that explanation requires extra evidence of compression and transport beyond the training regime. [inference; source: https://arxiv.org/abs/1812.11118; https://arxiv.org/abs/math/0406077; https://pmc.ncbi.nlm.nih.gov/articles/PMC12341957/]

The formal criterion is strongest when comparing rival model families on the same problem. If one family leaves many labelings open, needs a long code to describe itself, and fails on novelty tests, while another leaves fewer possibilities open, compresses the data with a shorter reusable code, and survives new tests, the second earns the stronger mechanistic claim. [inference; source: https://plato.stanford.edu/entries/popper/; https://research.ibm.com/publications/modeling-by-shortest-data-description; https://pmc.ncbi.nlm.nih.gov/articles/PMC12341957/]

### Risks, Gaps, and Uncertainties

- The argument here relies on accessible secondary summaries for Popper and on accessible lecture-note or reference summaries for Vapnik-Chervonenkis theory, with the primary books kept as bibliographic locators rather than quoted chapter evidence. [fact; source: https://archive.org/details/logicofscientifi0000popp; https://archive.org/details/natureofstatisti0037vapn; https://plato.stanford.edu/entries/popper/; https://iep.utm.edu/pop-sci/; https://www.cs.princeton.edu/~rlivni/cos511/lectures/lect3.pdf; https://homes.cs.washington.edu/~sham/courses/stat928/lectures/lecture24.pdf]
- Classical Vapnik-Chervonenkis bounds are known to be loose for modern deep networks, so any criterion using them alone will overstate the case against neural models. [fact; source: https://arxiv.org/abs/1812.11118; https://openreview.net/forum?id=B1g5sA4twr]
- Exact Kolmogorov complexity is not computable, so practical deployment of this framework must use proxy code lengths rather than the ideal shortest program. [fact; source: https://doi.org/10.1007/978-0-387-49820-1; https://en.wikipedia.org/wiki/Kolmogorov_complexity]
- The framework is clearest for binary-labeled or explicitly coded prediction tasks and needs more work to handle continuous-time physical theories with rich intervention structure. [inference; source: https://en.wikipedia.org/wiki/Vapnik%E2%80%93Chervonenkis_theory; https://pmc.ncbi.nlm.nih.gov/articles/PMC12341957/]

### Open Questions

- How should effective dimension, margin bounds, or compression bounds replace raw Vapnik-Chervonenkis dimension when the model family is a modern transformer or diffusion architecture?
- What is the best practical coding scheme for measuring description length in fitted neural networks without smuggling in arbitrary engineering choices?
- Which intervention or regime-shift tests are decisive enough to let a statistical model earn a genuine mechanistic claim in physics or biology?

---

## Output

- Type: knowledge
- Description: Formal criterion that combines finite-sample logical content, description length, and novelty testing to separate mechanistic models from interpolative fits in contemporary machine learning. [inference; source: https://plato.stanford.edu/entries/popper/; https://arxiv.org/abs/math/0406077; https://pmc.ncbi.nlm.nih.gov/articles/PMC12341957/]
- Links:
  - https://plato.stanford.edu/entries/popper/
  - https://arxiv.org/abs/math/0406077
  - https://arxiv.org/abs/1812.11118
