---
review_count: 2
title: "Research Question 1.2: Deutsch's criterion for explanations whose details cannot be changed without loss of coherence"
added: 2026-05-18T19:40:00+00:00
status: completed
priority: high
blocks:
  - 2026-05-18-rq1-3-instrumentalism-failure-modes
tags: [epistemology, philosophy-of-science, machine-learning, formal-methods, invariants]
started: 2026-05-19T01:38:17+00:00
completed: 2026-05-19T01:59:55+00:00
output: [knowledge]
cites:
  - 2026-05-18-rq1-1-popper-falsifiability
related:
  - 2026-05-18-rq1-1-popper-falsifiability
  - 2026-05-18-rq1-3-instrumentalism-failure-modes
superseded_by: ~
supersedes: ~
item_type: primary
confidence: medium
versions:
  - version: "1.0"
    sha: "f0637b125266fafe630d6f88694777784432e042"
    changed: 2026-05-19
    progress: progress/2026-05-19-rq1-2-deutsch-hard-to-vary.md
    summary: "Initial completion"
---

# Research Question 1.2: Deutsch's criterion for explanations whose details cannot be changed without loss of coherence

## Research Question

Using David Deutsch's hard-to-vary criterion, meaning an explanation whose details cannot be changed without losing explanatory force, what formal criteria can measure the internal logical constraints of an explanatory mechanism, and how does varying those constraints expose structural fragility before empirical testing occurs?

## Scope

**In scope:**
- Formalisation of Deutsch's "hard-to-vary" criterion as a pre-empirical filter for model quality
- Functional interdependence and invariance under parameter mutation as measurable properties
- Sensitivity analysis applied to model topologies to expose structural fragility
- Relationship to Popper's falsifiability established in Research Question 1.1 (RQ 1.1)

**Out of scope:**
- Deutsch's broader philosophical claims about the nature of knowledge beyond the hard-to-vary criterion
- Empirical validation of specific physical models

**Constraints:** Must build on Research Question 1.1 (RQ 1.1)'s formalisation of falsifiability; seek quantitative treatments alongside conceptual ones.

## Context

Popper's falsifiability criterion, formalised in Research Question 1.1 (RQ 1.1), tests a model after confrontation with evidence by asking what observations the model excludes. [fact; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq1-1-popper-falsifiability.md; https://plato.stanford.edu/entries/popper/]

This item asks for the complementary pre-empirical screen: whether the explanation's internal parts are mutually constraining enough that arbitrary local changes destroy coherence before new data are collected. [inference; source: https://arxiv.org/abs/2009.00329; https://www.penguin.com.au/books/the-beginning-of-infinity-9780140278163]

## Approach

1. Summarise Deutsch's "hard-to-vary" criterion from *The Beginning of Infinity* (Chapters 1 & 2).
2. Identify formal analogues in the machine learning literature: functional interdependence of parameters, sensitivity analysis, invariance conditions.
3. Examine Parascandolo et al. (2020) "Learning explanations that are hard to vary" for mathematical operationalisation.
4. Propose a formal measure of "hard-to-vary-ness" as a function of parameter interdependence and prediction sensitivity.
5. Apply the measure to contrast a mechanistic model (hard-to-vary) against a deep neural network (easy-to-vary components).

## Sources

- [x] [Deutsch (2011) The Beginning of Infinity](https://www.penguin.com.au/books/the-beginning-of-infinity-9780140278163) - publisher page used as the primary locator for the book that introduced the hard-to-vary criterion.
- [x] [Parascandolo et al. (2020) Learning Explanations That Are Hard to Vary](https://arxiv.org/abs/2009.00329) - direct mathematical operationalisation of the criterion through consistency across environments.
- [x] [Saltelli et al. (2008) Global Sensitivity Analysis: The Primer](https://www.wiley.com/en-us/Global+Sensitivity+Analysis%3A+The+Primer-p-9780470059975) - official Wiley landing page for the seeded sensitivity-analysis book.
- [x] [Saltelli et al. (2010) Variance based sensitivity analysis of model output. Design and estimator for the total sensitivity index](https://publications.jrc.ec.europa.eu/repository/handle/JRC52955) - primary summary of first-order and total-effect variance decomposition.
- [x] [Becker et al. (2017) Exploring the weighting effects of composite indicators](https://pmc.ncbi.nlm.nih.gov/articles/PMC5473177/) - accessible treatment of the correlation ratio as a first-order sensitivity index and of conditional variance reduction.
- [x] [Gutenkunst et al. (2007) Universally Sloppy Parameter Sensitivities in Systems Biology Models](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.0030189) - classic statement of sloppy and stiff parameter directions.
- [x] [Jagadeesan et al. (2023) Sloppiness: fundamental study, new formalism and quantification](https://pmc.ncbi.nlm.nih.gov/articles/PMC9994762/) - explicit connection among sloppiness, structural identifiability, and nearly identical prediction regions.
- [x] [Dufresne et al. (2018) The geometry of sloppiness](https://arxiv.org/abs/1608.05679) - formal treatment of sloppiness via an induced premetric on parameter space.
- [x] [Nielsen et al. (2025) The rise of scientific machine learning](https://pmc.ncbi.nlm.nih.gov/articles/PMC12341957/) - current review on mechanistic models, machine learning, and hybrid scientific machine learning systems.
- [x] [Research repo (2026) Research Question 1.1 (RQ 1.1): Formalising Popper's Falsifiability as a Criterion Between Mechanism and Interpolation](https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq1-1-popper-falsifiability.md) - directly preceding item that formalised the post-empirical filter this item extends.

---

## Research Skill Output

*(Full output from running the research skill, retained verbatim in the completed item. Sections 0-5 are the investigation; Section 6 seeds the Findings section below.)*

### §0 Initialise

- Question: Using David Deutsch's hard-to-vary criterion, what formal criteria can measure internal logical constraint in an explanatory mechanism, and how does varying those constraints expose structural fragility before empirical testing?
- Scope: pre-empirical explanatory constraint, cross-environment invariance, variance-based sensitivity, parameter-geometry fragility, and contrast between mechanistic models and flexible neural models.
- Constraints: full mode, quantitative treatment first, build directly on the completed Research Question 1.1 (RQ 1.1) Popper item, and use accessible sources for every operational claim.
- Output: full structured synthesis with executive summary, key findings, evidence map, assumptions, analysis, risks, and open questions.
- Prior-item scan: the completed Research Question 1.1 (RQ 1.1) item already formalises Popper's post-empirical filter in terms of excluded possibilities, description length, and novelty testing, so this item can treat Deutsch's criterion as a complementary pre-empirical filter rather than a rival demarcation test. [fact; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq1-1-popper-falsifiability.md]

### §1 Question Decomposition

1. Philosophical target
   1.1 What does Deutsch mean by a hard-to-vary explanation?
   1.2 How does that differ from the Popperian criterion already formalised in Research Question 1.1 (RQ 1.1)?
2. Operational bridge
   2.1 What formal property in modern machine-learning literature most closely matches "hard to vary"?
   2.2 How does Parascandolo et al. define consistency and Invariant Learning Consistency?
3. Constraint measurement
   3.1 Which sensitivity-analysis quantities distinguish isolated parameter effects from jointly constrained effects?
   3.2 Which geometric or identifiability quantities distinguish small admissible variation regions from large easy-to-vary regions?
4. Composite criterion
   4.1 How can cross-environment consistency, interaction dominance, and admissible-variation volume be combined into one usable score?
   4.2 What failure modes does that score reveal before new empirical testing?
5. Comparative application
   5.1 Why should a mechanistic model score differently from a flexible deep neural network trained only for prediction?
   5.2 Under what conditions could a structured scientific machine learning system count as hard to vary rather than easy to vary?

### §2 Investigation

#### A. Deutsch's target and the relation to Popper

- [inference] Deutsch's hard-to-vary criterion targets the internal replaceability of explanatory parts, not only the external testability of predictions, so it asks whether an explanation would stop making sense if its internal details were changed arbitrarily. [source: https://arxiv.org/abs/2009.00329; https://www.penguin.com.au/books/the-beginning-of-infinity-9780140278163]
- [fact] The completed Research Question 1.1 (RQ 1.1) item formalised Popper's criterion as a post-empirical check on excluded possibilities and novelty testing rather than as a direct measure of internal explanatory coupling. [source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq1-1-popper-falsifiability.md]
- [inference] The two criteria therefore act on different stages of model assessment: Popper asks what evidence could refute the theory, while Deutsch asks whether the explanation already contains enough coordinated internal constraint to deserve serious empirical testing. [source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq1-1-popper-falsifiability.md; https://arxiv.org/abs/2009.00329]
- [inference] The consulted public publisher page confirms the book and its focus on explanations, but the phrase-level operational account used here relies on Parascandolo's accessible quotation and restatement of Deutsch's dictum rather than on a directly viewable chapter excerpt. [source: https://www.penguin.com.au/books/the-beginning-of-infinity-9780140278163; https://arxiv.org/abs/2009.00329]

#### B. Parascandolo's operationalisation of hard-to-vary explanations

- [fact] Parascandolo et al. argue that averaging gradients across examples behaves like a logical OR of patterns and can favor memorization or patchwork solutions instead of invariant explanations. [source: https://arxiv.org/abs/2009.00329]
- [fact] The paper formalises a notion of consistency for a minimum of the loss surface, intended to capture the extent to which the same solution appears when examples from different environments are pooled and when they are considered separately. [source: https://arxiv.org/abs/2009.00329]
- [fact] Minima with low consistency are described as patchwork solutions that sew together distinct strategies and should not be expected to generalize out of distribution. [source: https://arxiv.org/abs/2009.00329]
- [fact] Invariant Learning Consistency (ILC) is the expected consistency of the solution found by a learning algorithm on a given hypothesis class. [source: https://arxiv.org/abs/2009.00329]
- [inference] Parascandolo's contribution gives the first directly usable formal bridge from Deutsch's philosophical criterion to a measurable machine-learning property, namely stability of the same explanatory minimum across environments. [source: https://arxiv.org/abs/2009.00329]

#### C. Variance-based sensitivity as a measure of internal coupling

- [fact] Variance-based sensitivity analysis, the family of methods that decomposes model-output variance into contributions from individual input factors and from their interactions, is often implemented through first-order effects together with total effects. [source: https://publications.jrc.ec.europa.eu/repository/handle/JRC52955; https://www.wiley.com/en-us/Global+Sensitivity+Analysis%3A+The+Primer-p-9780470059975]
- [fact] Becker et al. define the correlation ratio, also known as the first-order sensitivity index or main-effect index, as the expected reduction in output variance when one variable is fixed. [source: https://pmc.ncbi.nlm.nih.gov/articles/PMC5473177/]
- [fact] Saltelli et al. describe total-effect indices as synthetic summaries that include a factor's own effect together with its interactions with other factors. [source: https://publications.jrc.ec.europa.eu/repository/handle/JRC52955]
- [inference] The interaction share `ST_i - S_i`, where `S_i` is the first-order index and `ST_i` is the total-effect index, is therefore a usable proxy for how much a component's contribution depends on coordinated adjustment with other components rather than on isolated main effects. [source: https://publications.jrc.ec.europa.eu/repository/handle/JRC52955; https://pmc.ncbi.nlm.nih.gov/articles/PMC5473177/]
- [inference] High interaction share fits Deutsch's intuition better than raw sensitivity alone, because a component that matters only jointly with others is more constrained by the rest of the explanation than a component whose effect can be tuned independently. [source: https://arxiv.org/abs/2009.00329; https://publications.jrc.ec.europa.eu/repository/handle/JRC52955; https://pmc.ncbi.nlm.nih.gov/articles/PMC5473177/]

#### D. Sloppiness, identifiability, and admissible variation volume

- [fact] Gutenkunst et al. report that sloppy models, models whose parameter-sensitivity spectra span many decades so that a few stiff parameter combinations matter far more than many broad easy-to-move directions, are common in systems biology. [source: https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.0030189]
- [fact] Jagadeesan et al. describe sloppiness as the presence of large regions in parameter space over which model predictions are nearly identical, while stiff directions are directions where prediction changes clearly with parameter variation. [source: https://pmc.ncbi.nlm.nih.gov/articles/PMC9994762/]
- [fact] Jagadeesan et al. also state that checking structural identifiability, whether the model structure permits a unique parameter solution under ideal conditions, before parameter estimation is imperative because structural unidentifiability yields multiple solutions to the estimation problem. [source: https://pmc.ncbi.nlm.nih.gov/articles/PMC9994762/]
- [fact] Dufresne et al. redefine sloppiness as a comparison between the premetric on parameter space induced by measurement noise and a reference metric, rather than only through infinitesimal Fisher Information Matrix eigenvalues. [source: https://arxiv.org/abs/1608.05679]
- [inference] These results make the admissible volume of explanation-preserving parameter settings a second usable hard-to-vary criterion: the larger the region of parameters that leave the explanation effectively unchanged, the easier the explanation is to vary without loss. [source: https://pmc.ncbi.nlm.nih.gov/articles/PMC9994762/; https://arxiv.org/abs/1608.05679; https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.0030189]

#### E. Proposed formal measure and comparative interpretation

- [inference] A practical hard-to-vary (HTV) score for an explanatory mechanism `M` can be written as `HTV(M) = C(M) x I(M) x V(M)`, where `C(M)` is a normalized cross-environment consistency term, `I(M) = (1/d) sum_i ((ST_i - S_i) / max(ST_i, epsilon))` is mean interaction dominance across `d` components, and `V(M) = 1 - log Vol(A_delta(M)) / log Vol(Theta)` measures how small the admissible explanation-preserving region `A_delta(M)` is within the plausible parameter space `Theta`. [source: https://arxiv.org/abs/2009.00329; https://publications.jrc.ec.europa.eu/repository/handle/JRC52955; https://pmc.ncbi.nlm.nih.gov/articles/PMC5473177/; https://pmc.ncbi.nlm.nih.gov/articles/PMC9994762/; https://arxiv.org/abs/1608.05679]
- [inference] Under this construction, an explanation is hard to vary when the same minimum recurs across environments, when most component influence is joint rather than separable, and when only a small parameter region preserves explanatory coherence. [source: https://arxiv.org/abs/2009.00329; https://publications.jrc.ec.europa.eu/repository/handle/JRC52955; https://pmc.ncbi.nlm.nih.gov/articles/PMC9994762/]
- [inference] Structural fragility appears before new empirical testing when one or more of these terms collapses, because low consistency signals patchwork solutions, low interaction dominance signals independently tunable parts, and large admissible volume signals many easy compensating variations. [source: https://arxiv.org/abs/2009.00329; https://pmc.ncbi.nlm.nih.gov/articles/PMC5473177/; https://pmc.ncbi.nlm.nih.gov/articles/PMC9994762/]
- [fact] Mechanistic models remain attractive in scientific machine learning because they encode interpretable causal or rule-based structure, while unconstrained machine-learning models can achieve strong prediction without revealing the underlying mechanism. [source: https://pmc.ncbi.nlm.nih.gov/articles/PMC12341957/]
- [inference] In the contrast reviewed here, a compact mechanistic model would often be expected to score higher on `HTV` than a flexible deep neural network trained only for predictive fit, unless the neural model is itself strongly structured by governing equations, sparse biological constraints, or environment-level invariances. [source: https://pmc.ncbi.nlm.nih.gov/articles/PMC12341957/; https://arxiv.org/abs/2009.00329]

### §3 Reasoning

- [fact] Parascandolo supplies a directly relevant operational criterion by measuring whether the same explanation recurs across environments rather than only whether a loss minimum exists. [source: https://arxiv.org/abs/2009.00329]
- [fact] Variance-based sensitivity analysis distinguishes isolated main effects from interaction effects, which makes it suitable for measuring how tightly explanatory parts depend on one another. [source: https://publications.jrc.ec.europa.eu/repository/handle/JRC52955; https://pmc.ncbi.nlm.nih.gov/articles/PMC5473177/]
- [fact] Sloppiness and identifiability work distinguish narrow, stiff, explanation-preserving regions from broad, nearly equivalent regions in parameter space. [source: https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.0030189; https://pmc.ncbi.nlm.nih.gov/articles/PMC9994762/; https://arxiv.org/abs/1608.05679]
- [inference] Combining those three strands yields a better formalisation of Deutsch's criterion than any single strand alone: consistency captures recurrence of the same mechanism, interaction dominance captures logical coupling among parts, and admissible-volume geometry captures ease of compensating variation. [source: https://arxiv.org/abs/2009.00329; https://publications.jrc.ec.europa.eu/repository/handle/JRC52955; https://pmc.ncbi.nlm.nih.gov/articles/PMC9994762/]
- [inference] The resulting test complements the completed Popper item by screening explanations for internal constraint before empirical confrontation, while leaving the final post-empirical verdict to falsification and novelty testing. [source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq1-1-popper-falsifiability.md; https://plato.stanford.edu/entries/popper/; https://arxiv.org/abs/2009.00329]

### §4 Consistency Check

- [fact] Tension: a model can be highly sensitive in one direction and still be easy to vary overall if many other directions admit compensating changes. [source: https://pmc.ncbi.nlm.nih.gov/articles/PMC9994762/; https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.0030189]
- [inference] Resolution: raw sensitivity should not be treated as hard-to-vary by itself, so the proposed score uses interaction dominance and admissible-volume restriction rather than gradient magnitude alone. [source: https://publications.jrc.ec.europa.eu/repository/handle/JRC52955; https://pmc.ncbi.nlm.nih.gov/articles/PMC9994762/]
- [fact] Tension: mechanistic models can also be sloppy in nuisance parameters, which means a low identifiability result does not automatically destroy explanatory value. [source: https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.0030189; https://pmc.ncbi.nlm.nih.gov/articles/PMC12341957/]
- [inference] Resolution: the score should be read comparatively and on explanation-relevant outputs, not as a claim that every parameter in a mechanistic model must be individually stiff. [source: https://pmc.ncbi.nlm.nih.gov/articles/PMC12341957/; https://arxiv.org/abs/1608.05679]
- [fact] Tension: some structured scientific machine learning systems intentionally impose mechanistic constraints on neural models. [source: https://pmc.ncbi.nlm.nih.gov/articles/PMC12341957/]
- [inference] Resolution: the mechanistic-versus-neural contrast in this item applies to unconstrained predictive deep networks by default, not to all hybrid or equation-informed neural architectures. [source: https://pmc.ncbi.nlm.nih.gov/articles/PMC12341957/]

### §5 Depth and Breadth Expansion

- [fact] Technical lens: the difference between first-order and total-effect indices measures how much explanatory work is carried by interactions, which makes it directly useful for separating tightly coupled mechanisms from independently tunable parameter collections. [source: https://publications.jrc.ec.europa.eu/repository/handle/JRC52955; https://pmc.ncbi.nlm.nih.gov/articles/PMC5473177/]
- [fact] Historical lens: RQ 1.1 treated explanation quality mainly through excluded possibilities after empirical confrontation, while this item adds a prior screen on internal coordination among explanatory parts. [source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq1-1-popper-falsifiability.md]
- [inference] Behavioural lens: a pre-empirical hard-to-vary screen is useful because it can prevent researchers from spending experimental effort on patchwork models that already display low cross-environment consistency or very large admissible variation regions. [source: https://arxiv.org/abs/2009.00329; https://pmc.ncbi.nlm.nih.gov/articles/PMC9994762/]
- [inference] Engineering lens: hybrid scientific machine learning systems are the main counterexample to a simplistic mechanistic-versus-neural dichotomy, because architecture-level constraints, sparse connections, and governing equations can raise consistency and reduce easy compensating variation inside otherwise flexible models. [source: https://pmc.ncbi.nlm.nih.gov/articles/PMC12341957/]

### §6 Synthesis

**Executive summary:**
- [inference] Deutsch's hard-to-vary criterion can be formalised as a joint test of cross-environment consistency, interaction-dominated sensitivity, and small explanation-preserving parameter volume, rather than as any single metric taken in isolation. [source: https://arxiv.org/abs/2009.00329; https://publications.jrc.ec.europa.eu/repository/handle/JRC52955; https://pmc.ncbi.nlm.nih.gov/articles/PMC9994762/]
- [inference] An explanation is hard to vary when the same minimum or mechanism recurs across environments, when most component influence is carried by interactions with other components, and when only a small region of plausible parameter space preserves explanatory coherence. [source: https://arxiv.org/abs/2009.00329; https://pmc.ncbi.nlm.nih.gov/articles/PMC5473177/; https://arxiv.org/abs/1608.05679]
- [inference] Varying those internal constraints exposes structural fragility before new empirical testing because low consistency reveals patchwork solutions, low interaction dominance reveals independently tunable parts, and large admissible variation regions reveal many compensating rewrites that leave current fit intact. [source: https://arxiv.org/abs/2009.00329; https://publications.jrc.ec.europa.eu/repository/handle/JRC52955; https://pmc.ncbi.nlm.nih.gov/articles/PMC9994762/]
- [inference] This criterion complements rather than replaces the Popperian filter in RQ 1.1: Popper still decides the post-empirical standing of a theory, while the hard-to-vary score decides whether the explanation is internally constrained enough to justify serious empirical investment. [source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq1-1-popper-falsifiability.md; https://plato.stanford.edu/entries/popper/; https://arxiv.org/abs/2009.00329]

**Key findings:**
1. **Deutsch's hard-to-vary criterion complements the Popperian filter formalised in RQ 1.1 because it evaluates internal explanatory constraint before new evidence is gathered, whereas Popper evaluates excluded observations and risky tests after confrontation with data.** ([inference]; medium confidence; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq1-1-popper-falsifiability.md; https://plato.stanford.edu/entries/popper/; https://arxiv.org/abs/2009.00329)
2. **Parascandolo et al. operationalise Deutsch's idea by defining consistency for minima across environments and by treating low-consistency minima as patchwork solutions that are likely to memorise rather than capture invariant mechanisms.** ([fact]; medium confidence; source: https://arxiv.org/abs/2009.00329)
3. **Variance-based sensitivity analysis supplies a measurable notion of internal logical coupling because the gap between a component's total effect and first-order effect quantifies how much explanatory work depends on coordinated interaction with other components.** ([inference]; medium confidence; source: https://publications.jrc.ec.europa.eu/repository/handle/JRC52955; https://pmc.ncbi.nlm.nih.gov/articles/PMC5473177/)
4. **Research on sloppiness, broad parameter directions that leave predictions nearly unchanged, and on structural identifiability, whether a model structure permits a unique parameter solution, shows that easy variation appears as broad parameter regions, whereas hard-to-vary explanations occupy comparatively small stiff regions.** ([inference]; medium confidence; source: https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.0030189; https://pmc.ncbi.nlm.nih.gov/articles/PMC9994762/; https://arxiv.org/abs/1608.05679)
5. **A usable formal score for hard-to-vary-ness is therefore a composite of cross-environment consistency, interaction dominance, and admissible-variation volume, because no one of those quantities alone distinguishes genuine explanatory constraint from mere brittleness or mere good fit.** ([inference]; medium confidence; source: https://arxiv.org/abs/2009.00329; https://publications.jrc.ec.europa.eu/repository/handle/JRC52955; https://pmc.ncbi.nlm.nih.gov/articles/PMC9994762/)
6. **Varying internal constraints exposes structural fragility before empirical testing when the same fitted model can be rewritten through many compensating parameter changes, when minima disappear outside pooled data, or when component influence remains mostly separable rather than jointly constrained.** ([inference]; medium confidence; source: https://arxiv.org/abs/2009.00329; https://pmc.ncbi.nlm.nih.gov/articles/PMC5473177/; https://pmc.ncbi.nlm.nih.gov/articles/PMC9994762/)
7. **In the contrast reviewed here, flexible deep neural networks trained only for prediction are more likely than compact mechanistic models to score lower on this criterion, while hybrid scientific machine learning systems can raise their score when architecture and training explicitly enforce governing structure or cross-environment invariance.** ([inference]; low confidence; source: https://pmc.ncbi.nlm.nih.gov/articles/PMC12341957/; https://arxiv.org/abs/2009.00329)

**Evidence map:**
| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [inference] Deutsch's criterion is a pre-empirical complement to the post-empirical Popperian filter in RQ 1.1. | https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq1-1-popper-falsifiability.md; https://plato.stanford.edu/entries/popper/; https://arxiv.org/abs/2009.00329 | medium | Cross-item synthesis rather than a single-source claim |
| [fact] Parascandolo operationalises hard-to-vary explanations through consistency across environments and treats low-consistency minima as patchwork solutions. | https://arxiv.org/abs/2009.00329 | medium | Directly stated by the paper, but supported here by a single source |
| [inference] The interaction share `ST_i - S_i` is a usable proxy for internal logical coupling among explanatory components. | https://publications.jrc.ec.europa.eu/repository/handle/JRC52955; https://pmc.ncbi.nlm.nih.gov/articles/PMC5473177/ | medium | Derived from first-order and total-effect definitions |
| [inference] Easy variation corresponds to broad admissible parameter regions, while hard-to-vary explanations occupy smaller stiff regions. | https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.0030189; https://pmc.ncbi.nlm.nih.gov/articles/PMC9994762/; https://arxiv.org/abs/1608.05679 | medium | Geometric synthesis across the sloppiness literature |
| [inference] A composite score using consistency, interaction dominance, and admissible-volume restriction better captures hard-to-vary-ness than any single metric. | https://arxiv.org/abs/2009.00329; https://publications.jrc.ec.europa.eu/repository/handle/JRC52955; https://pmc.ncbi.nlm.nih.gov/articles/PMC9994762/ | medium | Proposed synthesis rule for this item |
| [inference] Low consistency, separable effects, and broad admissible regions reveal structural fragility before new empirical tests are run. | https://arxiv.org/abs/2009.00329; https://pmc.ncbi.nlm.nih.gov/articles/PMC5473177/; https://pmc.ncbi.nlm.nih.gov/articles/PMC9994762/ | medium | Failure-mechanism synthesis |
| [inference] In the reviewed contrast, flexible predictive deep neural networks are more likely than compact mechanistic models to score lower on this criterion, while strongly structured hybrid models can score higher. | https://pmc.ncbi.nlm.nih.gov/articles/PMC12341957/; https://arxiv.org/abs/2009.00329 | low | Broad cross-model comparison, kept inferential and low confidence |

**Assumptions:**
- [assumption] The consistency term `C(M)` can be approximated by environment splits or other meaningful partitions of data rather than by access to every possible deployment environment. [justification: Parascandolo's operationalisation already uses multiple environments as the relevant testbed for invariance; source: https://arxiv.org/abs/2009.00329]
- [assumption] The admissible-volume term `V(M)` can be estimated with local Fisher or Hessian geometry and identifiability diagnostics even when the exact global volume is computationally impractical to calculate. [justification: the sloppiness literature treats induced local geometry as a practical route to diagnosing broad versus narrow parameter directions; source: https://arxiv.org/abs/1608.05679; https://pmc.ncbi.nlm.nih.gov/articles/PMC9994762/]
- [assumption] Interaction dominance from variance-based sensitivity indices is an acceptable proxy for internal logical coupling, even though logical dependence in the philosophical sense is richer than variance decomposition alone. [justification: the sensitivity literature measures whether factor influence is isolated or interaction-mediated, which is the operational distinction needed for this item; source: https://publications.jrc.ec.europa.eu/repository/handle/JRC52955; https://pmc.ncbi.nlm.nih.gov/articles/PMC5473177/]

**Analysis:**
- [inference] The evidence supports a three-part criterion rather than a single statistic, because cross-environment recurrence, interaction-mediated dependence, and small admissible variation regions each capture a different way in which an explanation resists arbitrary rewriting. [source: https://arxiv.org/abs/2009.00329; https://publications.jrc.ec.europa.eu/repository/handle/JRC52955; https://pmc.ncbi.nlm.nih.gov/articles/PMC9994762/]
- [inference] A rival interpretation says that any model with high local sensitivity is already hard to vary, but that interpretation confuses brittleness with explanatory constraint because a one-parameter unstable fit can still be easy to rewrite elsewhere in parameter space. [source: https://pmc.ncbi.nlm.nih.gov/articles/PMC5473177/; https://pmc.ncbi.nlm.nih.gov/articles/PMC9994762/]
- [inference] Another rival interpretation says that mechanistic models are always hard to vary and neural models are always easy to vary, but the scientific machine learning literature shows that hybrid models can acquire genuine internal constraint when sparse architecture, governing equations, or prior structure limit arbitrary rewrites. [source: https://pmc.ncbi.nlm.nih.gov/articles/PMC12341957/]
- [inference] The proposed `HTV` score should therefore be used comparatively across rival model families or rival training setups, not as a metaphysical certificate that one fitted parameter vector has captured reality once and for all. [source: https://arxiv.org/abs/2009.00329; https://arxiv.org/abs/1608.05679; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq1-1-popper-falsifiability.md]

**Risks, gaps, uncertainties:**
- [fact] The consulted public source for Deutsch's book is a publisher page that confirms the work and its focus on explanations, but it does not expose the chapter text, so phrase-level interpretation depends on Parascandolo's accessible quotation of the criterion. [source: https://www.penguin.com.au/books/the-beginning-of-infinity-9780140278163; https://arxiv.org/abs/2009.00329]
- [fact] Variance-based sensitivity metrics depend on the chosen output variable and on the assumed input-distribution or uncertainty structure, so the same mechanism can receive different interaction scores under different formal problem statements. [source: https://www.wiley.com/en-us/Global+Sensitivity+Analysis%3A+The+Primer-p-9780470059975; https://publications.jrc.ec.europa.eu/repository/handle/JRC52955]
- [fact] Local sloppiness geometry can miss non-local compensating variations, so practical estimation of admissible volume is an approximation rather than a complete global certificate. [source: https://arxiv.org/abs/1608.05679; https://pmc.ncbi.nlm.nih.gov/articles/PMC9994762/]
- [inference] The proposed score is sharper for comparing rival explanatory models on the same task than for assigning a universally meaningful absolute threshold that separates explanation from non-explanation across all domains. [source: https://arxiv.org/abs/2009.00329; https://pmc.ncbi.nlm.nih.gov/articles/PMC12341957/]

**Open questions:**
- What is the best practical estimator for admissible explanation-preserving volume in large neural systems where the local Hessian badly under-represents the global solution manifold?
- How should the interaction term be adapted for explanations whose key constraints are structural or symbolic rather than parametrically differentiable?
- Which intervention or regime-shift tests are stringent enough to convert a high pre-empirical `HTV` score into the stronger post-empirical status formalised in RQ 1.1?

### §7 Recursive Review

- Metadata:
  - acronym expansion checked, including Invariant Learning Consistency (ILC)
  - claim labels checked in `## Research Skill Output`
  - citation URLs checked
  - synthesis and findings parity checked
  - remaining uncertainty: task-specific output definitions; admissible-volume approximation choices

---

## Findings

*(Populated from §6 Synthesis above.)*

### Executive Summary

Deutsch's hard-to-vary criterion can be formalised as a joint test of cross-environment consistency, interaction-dominated sensitivity, and small explanation-preserving parameter volume, rather than as any single metric taken in isolation. [inference; source: https://arxiv.org/abs/2009.00329; https://publications.jrc.ec.europa.eu/repository/handle/JRC52955; https://pmc.ncbi.nlm.nih.gov/articles/PMC9994762/]

An explanation is hard to vary when the same minimum or mechanism recurs across environments, when most component influence is carried by interactions with other components, and when only a small region of plausible parameter space preserves explanatory coherence. [inference; source: https://arxiv.org/abs/2009.00329; https://pmc.ncbi.nlm.nih.gov/articles/PMC5473177/; https://arxiv.org/abs/1608.05679]

Varying those internal constraints exposes structural fragility before new empirical testing because low consistency reveals patchwork solutions, low interaction dominance reveals independently tunable parts, and large admissible variation regions reveal many compensating rewrites that leave current fit intact. [inference; source: https://arxiv.org/abs/2009.00329; https://publications.jrc.ec.europa.eu/repository/handle/JRC52955; https://pmc.ncbi.nlm.nih.gov/articles/PMC9994762/]

This criterion complements rather than replaces the Popperian filter in RQ 1.1: Popper still decides the post-empirical standing of a theory, while the hard-to-vary score decides whether the explanation is internally constrained enough to justify serious empirical investment. [inference; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq1-1-popper-falsifiability.md; https://plato.stanford.edu/entries/popper/; https://arxiv.org/abs/2009.00329]

### Key Findings

1. **Deutsch's hard-to-vary criterion complements the Popperian filter formalised in RQ 1.1 because it evaluates internal explanatory constraint before new evidence is gathered, whereas Popper evaluates excluded observations and risky tests after confrontation with data.** ([inference]; medium confidence; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq1-1-popper-falsifiability.md; https://plato.stanford.edu/entries/popper/; https://arxiv.org/abs/2009.00329)
2. **Parascandolo et al. operationalise Deutsch's idea by defining consistency for minima across environments and by treating low-consistency minima as patchwork solutions that are likely to memorise rather than capture invariant mechanisms.** ([fact]; medium confidence; source: https://arxiv.org/abs/2009.00329)
3. **Variance-based sensitivity analysis supplies a measurable notion of internal logical coupling because the gap between a component's total effect and first-order effect quantifies how much explanatory work depends on coordinated interaction with other components.** ([inference]; medium confidence; source: https://publications.jrc.ec.europa.eu/repository/handle/JRC52955; https://pmc.ncbi.nlm.nih.gov/articles/PMC5473177/)
4. **Research on sloppiness, broad parameter directions that leave predictions nearly unchanged, and on structural identifiability, whether a model structure permits a unique parameter solution, shows that easy variation appears as broad parameter regions, whereas hard-to-vary explanations occupy comparatively small stiff regions.** ([inference]; medium confidence; source: https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.0030189; https://pmc.ncbi.nlm.nih.gov/articles/PMC9994762/; https://arxiv.org/abs/1608.05679)
5. **A usable formal score for hard-to-vary-ness is therefore a composite of cross-environment consistency, interaction dominance, and admissible-variation volume, because no one of those quantities alone distinguishes genuine explanatory constraint from mere brittleness or mere good fit.** ([inference]; medium confidence; source: https://arxiv.org/abs/2009.00329; https://publications.jrc.ec.europa.eu/repository/handle/JRC52955; https://pmc.ncbi.nlm.nih.gov/articles/PMC9994762/)
6. **Varying internal constraints exposes structural fragility before empirical testing when the same fitted model can be rewritten through many compensating parameter changes, when minima disappear outside pooled data, or when component influence remains mostly separable rather than jointly constrained.** ([inference]; medium confidence; source: https://arxiv.org/abs/2009.00329; https://pmc.ncbi.nlm.nih.gov/articles/PMC5473177/; https://pmc.ncbi.nlm.nih.gov/articles/PMC9994762/)
7. **In the contrast reviewed here, flexible deep neural networks trained only for prediction are more likely than compact mechanistic models to score lower on this criterion, while hybrid scientific machine learning systems can raise their score when architecture and training explicitly enforce governing structure or cross-environment invariance.** ([inference]; low confidence; source: https://pmc.ncbi.nlm.nih.gov/articles/PMC12341957/; https://arxiv.org/abs/2009.00329)

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [inference] Deutsch's criterion is a pre-empirical complement to the post-empirical Popperian filter in RQ 1.1. | https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq1-1-popper-falsifiability.md; https://plato.stanford.edu/entries/popper/; https://arxiv.org/abs/2009.00329 | medium | Cross-item synthesis rather than a single-source claim |
| [fact] Parascandolo operationalises hard-to-vary explanations through consistency across environments and treats low-consistency minima as patchwork solutions. | https://arxiv.org/abs/2009.00329 | medium | Directly stated by the paper, but supported here by a single source |
| [inference] The interaction share `ST_i - S_i` is a usable proxy for internal logical coupling among explanatory components. | https://publications.jrc.ec.europa.eu/repository/handle/JRC52955; https://pmc.ncbi.nlm.nih.gov/articles/PMC5473177/ | medium | Derived from first-order and total-effect definitions |
| [inference] Easy variation corresponds to broad admissible parameter regions, while hard-to-vary explanations occupy smaller stiff regions. | https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.0030189; https://pmc.ncbi.nlm.nih.gov/articles/PMC9994762/; https://arxiv.org/abs/1608.05679 | medium | Geometric synthesis across the sloppiness literature |
| [inference] A composite score using consistency, interaction dominance, and admissible-volume restriction better captures hard-to-vary-ness than any single metric. | https://arxiv.org/abs/2009.00329; https://publications.jrc.ec.europa.eu/repository/handle/JRC52955; https://pmc.ncbi.nlm.nih.gov/articles/PMC9994762/ | medium | Proposed synthesis rule for this item |
| [inference] Low consistency, separable effects, and broad admissible regions reveal structural fragility before new empirical tests are run. | https://arxiv.org/abs/2009.00329; https://pmc.ncbi.nlm.nih.gov/articles/PMC5473177/; https://pmc.ncbi.nlm.nih.gov/articles/PMC9994762/ | medium | Failure-mechanism synthesis |
| [inference] In the reviewed contrast, flexible predictive deep neural networks are more likely than compact mechanistic models to score lower on this criterion, while strongly structured hybrid models can score higher. | https://pmc.ncbi.nlm.nih.gov/articles/PMC12341957/; https://arxiv.org/abs/2009.00329 | low | Broad cross-model comparison, kept inferential and low confidence |

### Assumptions

- [assumption] The consistency term `C(M)` can be approximated by environment splits or other meaningful partitions of data rather than by access to every possible deployment environment. [justification: Parascandolo's operationalisation already uses multiple environments as the relevant testbed for invariance; source: https://arxiv.org/abs/2009.00329]
- [assumption] The admissible-volume term `V(M)` can be estimated with local Fisher or Hessian geometry and identifiability diagnostics even when the exact global volume is computationally impractical to calculate. [justification: the sloppiness literature treats induced local geometry as a practical route to diagnosing broad versus narrow parameter directions; source: https://arxiv.org/abs/1608.05679; https://pmc.ncbi.nlm.nih.gov/articles/PMC9994762/]
- [assumption] Interaction dominance from variance-based sensitivity indices is an acceptable proxy for internal logical coupling, even though logical dependence in the philosophical sense is richer than variance decomposition alone. [justification: the sensitivity literature measures whether factor influence is isolated or interaction-mediated, which is the operational distinction needed for this item; source: https://publications.jrc.ec.europa.eu/repository/handle/JRC52955; https://pmc.ncbi.nlm.nih.gov/articles/PMC5473177/]

### Analysis

The evidence supports a three-part criterion rather than a single statistic, because cross-environment recurrence, interaction-mediated dependence, and small admissible variation regions each capture a different way in which an explanation resists arbitrary rewriting. [inference; source: https://arxiv.org/abs/2009.00329; https://publications.jrc.ec.europa.eu/repository/handle/JRC52955; https://pmc.ncbi.nlm.nih.gov/articles/PMC9994762/]

A rival interpretation says that any model with high local sensitivity is already hard to vary, but that interpretation confuses brittleness with explanatory constraint because a one-parameter unstable fit can still be easy to rewrite elsewhere in parameter space. [inference; source: https://pmc.ncbi.nlm.nih.gov/articles/PMC5473177/; https://pmc.ncbi.nlm.nih.gov/articles/PMC9994762/]

Another rival interpretation says that mechanistic models are always hard to vary and neural models are always easy to vary, but the scientific machine learning literature shows that hybrid models can acquire genuine internal constraint when sparse architecture, governing equations, or prior structure limit arbitrary rewrites. [inference; source: https://pmc.ncbi.nlm.nih.gov/articles/PMC12341957/]

The proposed `HTV` score should therefore be used comparatively across rival model families or rival training setups, not as a metaphysical certificate that one fitted parameter vector has captured reality once and for all. [inference; source: https://arxiv.org/abs/2009.00329; https://arxiv.org/abs/1608.05679; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq1-1-popper-falsifiability.md]

### Risks, Gaps, and Uncertainties

- The consulted public source for Deutsch's book is a publisher page that confirms the work and its focus on explanations, but it does not expose the chapter text, so phrase-level interpretation depends on Parascandolo's accessible quotation of the criterion. [fact; source: https://www.penguin.com.au/books/the-beginning-of-infinity-9780140278163; https://arxiv.org/abs/2009.00329]
- Variance-based sensitivity metrics depend on the chosen output variable and on the assumed input-distribution or uncertainty structure, so the same mechanism can receive different interaction scores under different formal problem statements. [fact; source: https://www.wiley.com/en-us/Global+Sensitivity+Analysis%3A+The+Primer-p-9780470059975; https://publications.jrc.ec.europa.eu/repository/handle/JRC52955]
- Local sloppiness geometry can miss non-local compensating variations, so practical estimation of admissible volume is an approximation rather than a complete global certificate. [fact; source: https://arxiv.org/abs/1608.05679; https://pmc.ncbi.nlm.nih.gov/articles/PMC9994762/]
- The proposed score is sharper for comparing rival explanatory models on the same task than for assigning a universally meaningful absolute threshold that separates explanation from non-explanation across all domains. [inference; source: https://arxiv.org/abs/2009.00329; https://pmc.ncbi.nlm.nih.gov/articles/PMC12341957/]

### Open Questions

- What is the best practical estimator for admissible explanation-preserving volume in large neural systems where the local Hessian badly under-represents the global solution manifold?
- How should the interaction term be adapted for explanations whose key constraints are structural or symbolic rather than parametrically differentiable?
- Which intervention or regime-shift tests are stringent enough to convert a high pre-empirical `HTV` score into the stronger post-empirical status formalised in RQ 1.1?

---

## Output

- Type: knowledge
- Description: Formal criterion that combines cross-environment consistency, interaction-dominated sensitivity, and admissible-variation volume to detect whether an explanation is internally constrained enough to resist arbitrary rewriting before new empirical tests are run. [inference; source: https://arxiv.org/abs/2009.00329; https://publications.jrc.ec.europa.eu/repository/handle/JRC52955; https://pmc.ncbi.nlm.nih.gov/articles/PMC9994762/]
- Links:
  - https://arxiv.org/abs/2009.00329
  - https://publications.jrc.ec.europa.eu/repository/handle/JRC52955
  - https://pmc.ncbi.nlm.nih.gov/articles/PMC9994762/
