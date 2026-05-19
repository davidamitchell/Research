---
review_count: 2
title: "Research Question 1.3: Failure Modes of Instrumentalism When Applied to Complex Dynamic Systems Under Distribution Shift"
added: 2026-05-18T19:40:00+00:00
status: completed
priority: high
blocks:
  - 2026-05-18-rq2-1-erm-causal-blindness
tags: [epistemology, philosophy-of-science, machine-learning, causal-inference, invariants]
started: 2026-05-19T02:01:31+00:00
completed: 2026-05-19T02:29:39+00:00
output: [knowledge]
cites:
  - 2026-05-18-rq1-1-popper-falsifiability
  - 2026-05-18-rq1-2-deutsch-hard-to-vary
related: []
superseded_by: ~
supersedes: ~
item_type: primary
confidence: medium
versions: []
---

# Research Question 1.3: Failure Modes of Instrumentalism When Applied to Complex Dynamic Systems Under Distribution Shift

## Research Question

What are the operational failure modes of an epistemic framework that prioritises instrumentalism, treating predictive performance as the primary criterion, over explanatory reach when applied to complex dynamic systems undergoing distribution shift, changes in the data-generating environment or relationship structure?

## Scope

**In scope:**
- Instrumentalism versus scientific realism as competing epistemic frameworks for model evaluation
- Goodhart's Law in the context of model optimisation and metric gaming
- Structural break detection and distribution shift as empirical stress tests of purely predictive models
- Documented real-world failure cases where instrumentalist models collapsed under distribution shift

**Out of scope:**
- Theoretical philosophy of science beyond directly applicable framings
- Cases where instrumentalist models succeeded under shift, though counter-evidence is noted where it materially qualifies a claim

**Constraints:** Must draw on the formal treatments from Research Question 1.1 and Research Question 1.2, and illustrative failures must be grounded in documented cases with Uniform Resource Locator (URL)-backed sources.

## Context

This item extends Research Question 1.1 and Research Question 1.2 from criteria for explanation quality to the operational consequences of dropping those criteria and selecting models by predictive fit instead. [fact; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq1-1-popper-falsifiability.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq1-2-deutsch-hard-to-vary.md]

The framing matters for later items on empirical risk minimisation, large language models, and agentic systems because those items depend on whether prediction without causal or mechanistic structure remains reliable when the environment changes. [inference; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq1-1-popper-falsifiability.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq1-2-deutsch-hard-to-vary.md; https://arxiv.org/abs/1501.01332]

## Approach

1. Characterise the instrumentalist position in machine learning as selecting models mainly by predictive accuracy on the training or recently observed distribution.
2. Apply Goodhart's Law: when predictive metrics become targets, they cease to be reliable measures of the underlying objective.
3. Survey structural break scenarios: economic forecasting failures around the 2007-08 financial crisis, epidemiological forecasting failures during COVID-19, and recommendation-system failures under preference drift.
4. Formalise the failure mode: show how distribution shift exposes the absence of invariant causal structure.
5. Connect the result to Judea Pearl's causal hierarchy and later invariance literature as an explanation of why instrumentalist models need continual repair instead of portable understanding.

## Sources

- [x] [Friedman (1953) Essays in Positive Economics, Internet Archive record](https://archive.org/details/essaysinpositive00milt)
- [x] [Hausman (2018) Philosophy of Economics](https://plato.stanford.edu/entries/economics/)
- [x] [Essays in Positive Economics - Wikipedia](https://en.wikipedia.org/wiki/Essays_in_Positive_Economics)
- [x] [Goodhart (1975) Problems of Monetary Management: The United Kingdom Experience, EconBiz record](https://www.econbiz.de/10002525062)
- [x] [Reserve Bank of Australia (1990) Conference volumes bibliography note on the origin of Goodhart's Law](https://www.rba.gov.au/publications/rdp/1990/9013/conference-volumes.html)
- [x] [Goodhart's law - Wikipedia](https://en.wikipedia.org/wiki/Goodhart%27s_law)
- [x] [Pearl (2009) Causality excerpts](https://bayes.cs.ucla.edu/BOOK-2K/)
- [x] [Pearl (2009) Causal inference in statistics: An overview](https://ftp.cs.ucla.edu/pub/stat_ser/r350-reprint.pdf)
- [x] [Pearl (2018) Theoretical Impediments to Machine Learning With Seven Sparks from the Causal Revolution](https://arxiv.org/abs/1801.04016)
- [x] [Shpitser and Pearl (2008) Complete Identification Methods for the Causal Hierarchy](https://jmlr.org/papers/v9/shpitser08a.html)
- [x] [Peters, Buhlmann, and Meinshausen (2015) Causal inference using invariant prediction: identification and confidence intervals](https://arxiv.org/abs/1501.01332)
- [x] [Buhlmann (2018) Invariance, Causality and Robustness](https://arxiv.org/abs/1812.08233)
- [x] [Arjovsky et al. (2019) Invariant Risk Minimization](https://arxiv.org/abs/1907.02893)
- [x] [Parascandolo et al. (2020) Learning explanations that are hard to vary](https://arxiv.org/abs/2009.00329)
- [x] [Sugihara et al. (2012) Detecting Causality in Complex Ecosystems](https://cdanfort.w3.uvm.edu/csc-reading-group/sugihara-causality-science-2012.pdf)
- [x] [Casini and Perron (2018) Structural Breaks in Time Series](https://www.bu.edu/econ/files/2019/01/structural-change-oxford.pdf)
- [x] [Rossi (2021) Forecasting in the Presence of Instabilities: How We Know Whether Models Predict Well and How to Improve Them](https://www.aeaweb.org/articles?id=10.1257/jel.20201479)
- [x] [Bank for International Settlements (2008) Quarterly Review overview, December 2008](https://www.bis.org/publ/qtrpdf/r_qt0812.htm)
- [x] [Shah et al. (2024) Accuracy of United States Centers for Disease Control and Prevention (US CDC) COVID-19 forecasting models](https://www.frontiersin.org/journals/public-health/articles/10.3389/fpubh.2024.1359368/full)
- [x] [Nixon et al. (2022) Real-time COVID-19 forecasting: challenges and opportunities of model performance and translation](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9499327/)
- [x] [Hinder et al. (2024) One or two things we know about concept drift](https://www.frontiersin.org/journals/artificial-intelligence/articles/10.3389/frai.2024.1330258/full)
- [x] [Hartatik, Heryawan, and Pulungan (2025) Trust Decay-Based Temporal Learning for Dynamic Recommender Systems with Concept Drift Adaptation](https://doaj.org/article/903ba595bbe544899ee16fc8513b93f0)
- [x] [Research Question 1.1 completed item](https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq1-1-popper-falsifiability.md)
- [x] [Research Question 1.2 completed item](https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq1-2-deutsch-hard-to-vary.md)

---

## Research Skill Output

### §0 Initialise

- Question: What operationally breaks when model choice privileges predictive performance over explanatory reach in complex dynamic systems that later undergo distribution shift?
- Scope: instrumentalism, Goodhart's Law, structural breaks, causal hierarchy, causal invariance, and three empirical case classes, economics, epidemiology, and recommendation systems.
- Constraints: full mode; URL-backed sources only; integrate Research Question 1.1 and Research Question 1.2; no repository-relative citations.
- Output: full synthesis with executive summary, key findings, evidence map, assumptions, analysis, risks, and open questions.
- Prior completed items consulted: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq1-1-popper-falsifiability.md ; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq1-2-deutsch-hard-to-vary.md
- [assumption] For this item, instrumentalism means selecting or defending a model mainly by predictive success even when its assumptions are unrealistic or its internal structure is not explanatory. [source: https://plato.stanford.edu/entries/economics/; https://archive.org/details/essaysinpositive00milt; https://en.wikipedia.org/wiki/Essays_in_Positive_Economics]
- [assumption] For this item, distribution shift means a change in the data-generating environment or relationship structure that can invalidate previously reliable correlations. [source: https://www.frontiersin.org/journals/artificial-intelligence/articles/10.3389/frai.2024.1330258/full; https://www.aeaweb.org/articles?id=10.1257/jel.20201479]

### §1 Question Decomposition

1. Instrumentalism
   1.1 What does the accessible evidence say Friedman's methodological instrumentalism treats as the right test of a theory?
   1.2 What operational stance follows if predictive success is treated as decisive even when assumptions are unrealistic?
2. Metric-target deformation
   2.1 What is the first accessible trace of Goodhart's Law?
   2.2 How does Goodhart's Law convert a score or proxy into a failure mechanism?
3. Causal hierarchy and invariance
   3.1 What does Pearl's hierarchy say prediction alone cannot answer?
   3.2 Why do causal or invariant predictors travel better across interventions and shifted environments?
4. Dynamic-system failure mechanics
   4.1 How do nonlinear systems produce misleading correlation or prediction signals?
   4.2 What specific failure modes appear when structural change arrives?
5. Empirical cases
   5.1 What do crisis-era economic forecasting sources show about instability?
   5.2 What do COVID-19 forecasting evaluations show about model degradation under changing interventions and behavior?
   5.3 What do recommendation-system drift sources show about preference-shift degradation?
6. Synthesis
   6.1 Which failure modes recur across domains?
   6.2 Which rival explanation, poor data quality or insufficient model governance, must be addressed before concluding that instrumentalism itself is the core problem?

### §2 Investigation

#### Access notes

- Access note: seeded source URL `https://doi.org/10.7208/chicago/9780226264011.001.0001` returned 404; search query `Methodology of Positive Economics 1953` used Internet Archive record plus the Essays in Positive Economics summary page.
- Access note: seeded source URL `https://www.rba.gov.au/publications/confs/1975/pdf/goodhart.pdf` returned 404; search query `Goodhart Problems of Monetary Management United Kingdom Experience Reserve Bank of Australia` used the EconBiz record, the Reserve Bank of Australia bibliography page, and an accessible summary page quoting the formula.
- Access note: seeded source URL `https://doi.org/10.1126/science.1227079` returned 403; search query `Sugihara Detecting Causality in Complex Ecosystems pdf` used a mirrored PDF hosted at `cdanfort.w3.uvm.edu`.

#### A. Instrumentalism as predictive sufficiency

- [fact] The Internet Archive record confirms that Essays in Positive Economics is a 1953 University of Chicago Press volume whose lead essay is "The Methodology of Positive Economics" and that the essay is concerned with methodological problems in deciding whether a suggested hypothesis should be tentatively accepted. [source: https://archive.org/details/essaysinpositive00milt]
- [fact] Hausman's Stanford Encyclopedia of Philosophy entry says Friedman drew the radical conclusion that theories should be appraised exclusively by the accuracy of their predictions for the class of phenomena they are meant to explain, not by the realism of their assumptions. [source: https://plato.stanford.edu/entries/economics/]
- [fact] The accessible summary page for Essays in Positive Economics describes Friedman's position as treating unrealistic assumptions as acceptable when a theory delivers significant predictions, and as judging theories by simplicity and fruitfulness rather than realism of assumptions. [source: https://en.wikipedia.org/wiki/Essays_in_Positive_Economics]
- [inference] Operationally, this stance evaluates models by whether they predict well enough on the observed regime, not by whether they expose the mechanism that would explain why the prediction should remain valid after the regime changes. [source: https://en.wikipedia.org/wiki/Essays_in_Positive_Economics; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq1-1-popper-falsifiability.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq1-2-deutsch-hard-to-vary.md]

#### B. Goodhart's Law as a failure mechanism

- [fact] The EconBiz record identifies Charles Goodhart's "Problems of Monetary Management: The United Kingdom Experience" as a 1975 article in Papers in Monetary Economics. [source: https://www.econbiz.de/10002525062]
- [fact] The Reserve Bank of Australia bibliography page states that Goodhart's 1975 paper contains the first reference to what became known as Goodhart's Law. [source: https://www.rba.gov.au/publications/rdp/1990/9013/conference-volumes.html]
- [fact] The accessible Goodhart's Law summary page quotes the formulation "Any observed statistical regularity will tend to collapse once pressure is placed upon it for control purposes" and generalises the point as the warning that measures cease to function well once they become targets. [source: https://en.wikipedia.org/wiki/Goodhart%27s_law]
- [inference] When predictive score becomes the target of model development, policy control, or organisational evaluation, optimisation pressure can deform the process being measured and thereby destroy the reliability of the score itself. [source: https://en.wikipedia.org/wiki/Goodhart%27s_law; https://www.rba.gov.au/publications/rdp/1990/9013/conference-volumes.html]

#### C. Why causal structure matters under shift

- [fact] Pearl's overview states that causal questions, especially questions about interventions and counterfactuals, require knowledge of the data-generating process and cannot be computed from observational data alone. [source: https://ftp.cs.ucla.edu/pub/stat_ser/r350-reprint.pdf]
- [fact] Pearl's 2018 paper on machine learning says current machine learning systems operate almost exclusively in a statistical or model-free mode and cannot reason about interventions or retrospection. [source: https://arxiv.org/abs/1801.04016]
- [fact] Shpitser and Pearl describe a hierarchy in which associative relationships come from observational distributions, cause-effect relationships come from intervention distributions, and counterfactuals require still more detailed information. [source: https://jmlr.org/papers/v9/shpitser08a.html]
- [fact] Peters, Buhlmann, and Meinshausen state that predictions from a causal model will in general work as well under interventions as for observational data, whereas predictions from a non-causal model can be very wrong if one intervenes on variables or changes the environment. [source: https://arxiv.org/abs/1501.01332]
- [fact] Buhlmann frames predictive robustness as a problem of probabilistic invariance or stability, and Arjovsky et al. propose Invariant Risk Minimization as a way to learn invariant correlations that support out-of-distribution generalization. [source: https://arxiv.org/abs/1812.08233; https://arxiv.org/abs/1907.02893]
- [inference] Instrumentalism fails under distribution shift because it is satisfied with association-level fit, while shift robustness depends on invariant structure that survives intervention or heterogeneous environments. [source: https://arxiv.org/abs/1801.04016; https://jmlr.org/papers/v9/shpitser08a.html; https://arxiv.org/abs/1501.01332; https://arxiv.org/abs/1812.08233; https://arxiv.org/abs/1907.02893]

#### D. Nonlinear systems and mirage correlations

- [fact] Sugihara et al. introduce convergent cross mapping as a method that can distinguish causality from correlation in nonseparable weakly connected dynamic systems. [source: https://cdanfort.w3.uvm.edu/csc-reading-group/sugihara-causality-science-2012.pdf]
- [fact] Sugihara et al. explicitly describe "mirage" correlations as common in coupled nonlinear systems, so correlation can alternate between positive, negative, and zero even when the system is dynamically linked. [source: https://cdanfort.w3.uvm.edu/csc-reading-group/sugihara-causality-science-2012.pdf]
- [inference] In complex dynamic systems, predictive or correlational success inside one observation window can therefore reflect transient synchrony or shared forcing rather than a portable mechanism. [source: https://cdanfort.w3.uvm.edu/csc-reading-group/sugihara-causality-science-2012.pdf; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq1-1-popper-falsifiability.md]

#### E. Economic forecasting under structural breaks

- [fact] Casini and Perron's review of structural change methods treats testing for changes in forecast accuracy as a practical problem within models involving structural changes. [source: https://www.bu.edu/econ/files/2019/01/structural-change-oxford.pdf]
- [fact] Rossi's Journal of Economic Literature abstract says instabilities are widespread in economic time series, names prediction of the 2007-08 financial crisis as an empirically relevant example, and argues that local measures of forecasting performance are more appropriate than average measures. [source: https://www.aeaweb.org/articles?id=10.1257/jel.20201479]
- [fact] The Bank for International Settlements overview for December 2008 describes the period as the financial crisis alongside unprecedented policy actions. [source: https://www.bis.org/publ/qtrpdf/r_qt0812.htm]
- [inference] The economic failure mode is regime brittleness: a model that looks competent on average historical fit can become unreliable when the regime changes, and average backtest performance can hide that deterioration until the break is already underway. [source: https://www.aeaweb.org/articles?id=10.1257/jel.20201479; https://www.bu.edu/econ/files/2019/01/structural-change-oxford.pdf; https://www.bis.org/publ/qtrpdf/r_qt0812.htm]

#### F. Coronavirus Disease 2019 (COVID-19) forecasting under changing interventions and behavior

- [fact] Shah et al. find that around two-thirds of the evaluated United States Centers for Disease Control and Prevention (US CDC) COVID-19 case forecasting models fail to outperform a static baseline, one-third fail to outperform a linear-trend baseline, and errors increased over time during the pandemic. [source: https://www.frontiersin.org/journals/public-health/articles/10.3389/fpubh.2024.1359368/full]
- [fact] Nixon et al. state that cases and hospitalisations are difficult to predict accurately, that data quality and reporting idiosyncrasies affect both training and evaluation, and that rapidly changing behavior and interventions complicate forecasting. [source: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9499327/]
- [fact] Shah et al. document that many US CDC-submitted models assumed current interventions would not change during the forecast period, which bound the forecast to continuation assumptions that could quickly fail. [source: https://www.frontiersin.org/journals/public-health/articles/10.3389/fpubh.2024.1359368/full]
- [inference] The epidemiological failure mode is assumption lock-in: models trained on a recent intervention regime can degrade as soon as policy, reporting behavior, or variant dynamics move outside the assumed continuation path. [source: https://www.frontiersin.org/journals/public-health/articles/10.3389/fpubh.2024.1359368/full; https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9499327/]

#### G. Recommendation systems and preference drift

- [fact] Hinder et al. define concept drift as a change in the data-generating distribution and argue that such changes require models either to adapt or to alert operators so that action can be taken. [source: https://www.frontiersin.org/journals/artificial-intelligence/articles/10.3389/frai.2024.1330258/full]
- [fact] Hartatik, Heryawan, and Pulungan argue that recommendation systems operate under user-preference drift, data sparsity, and non-stationarity, and propose an explicitly drift-aware adaptation framework to stabilize matrix factorization models. [source: https://doaj.org/article/903ba595bbe544899ee16fc8513b93f0]
- [inference] The recommendation-system failure mode is silent quality decay: correlations that supported yesterday's recommendations erode as preferences shift, and performance holds only if the system explicitly models temporal drift or reweights evidence. [source: https://www.frontiersin.org/journals/artificial-intelligence/articles/10.3389/frai.2024.1330258/full; https://doaj.org/article/903ba595bbe544899ee16fc8513b93f0]

#### H. Cross-item integration with earlier completed work

- [fact] Research Question 1.1 formalised explanation quality through excluded possibilities and novelty testing rather than retrospective fit alone. [source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq1-1-popper-falsifiability.md]
- [fact] Research Question 1.2 formalised hard-to-vary explanations as internally constrained explanations that recur across environments and resist patchwork variation. [source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq1-2-deutsch-hard-to-vary.md]
- [inference] This item extends those two completed items by showing the operational consequence of dropping both filters: once a model is chosen for fit alone, its failure under shift appears as metric gaming, regime brittleness, causal blindness, and expensive continual repair. [source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq1-1-popper-falsifiability.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq1-2-deutsch-hard-to-vary.md; https://arxiv.org/abs/1501.01332; https://en.wikipedia.org/wiki/Goodhart%27s_law]

### §3 Reasoning

- [fact] Instrumentalism privileges predictive fruitfulness over realism of assumptions, Goodhart's Law warns that optimisation pressure can deform measured relationships, and causal-invariance literature shows that robustness under change depends on mechanisms that survive interventions. [source: https://en.wikipedia.org/wiki/Essays_in_Positive_Economics; https://en.wikipedia.org/wiki/Goodhart%27s_law; https://arxiv.org/abs/1501.01332; https://arxiv.org/abs/1812.08233]
- [inference] Together these strands imply a common failure chain: a model is selected for observational score, the score or environment changes, the learned correlation no longer tracks the governing mechanism, and operators must improvise recalibration because the model does not say what should remain invariant. [source: https://en.wikipedia.org/wiki/Goodhart%27s_law; https://jmlr.org/papers/v9/shpitser08a.html; https://arxiv.org/abs/1501.01332; https://arxiv.org/abs/1812.08233]
- [inference] The empirical cases matter because they show the chain in live systems rather than only in methodology: crisis forecasting, outbreak forecasting, and recommendation systems all degrade when the environment or behavior changes faster than correlation-based fit can track. [source: https://www.aeaweb.org/articles?id=10.1257/jel.20201479; https://www.frontiersin.org/journals/public-health/articles/10.3389/fpubh.2024.1359368/full; https://www.frontiersin.org/journals/artificial-intelligence/articles/10.3389/frai.2024.1330258/full; https://doaj.org/article/903ba595bbe544899ee16fc8513b93f0]
- [assumption] The three case classes, economics, epidemiology, and recommendation systems, are treated as representative examples of dynamic systems under distribution shift rather than as an exhaustive census of every domain where instrumentalism fails. [source: https://www.aeaweb.org/articles?id=10.1257/jel.20201479; https://www.frontiersin.org/journals/public-health/articles/10.3389/fpubh.2024.1359368/full; https://www.frontiersin.org/journals/artificial-intelligence/articles/10.3389/frai.2024.1330258/full]

### §4 Consistency Check

- [fact] Tension: some predictive systems remain useful under shift if they are continuously retrained, ensembled, or equipped with explicit drift adaptation. [source: https://www.frontiersin.org/journals/public-health/articles/10.3389/fpubh.2024.1359368/full; https://www.frontiersin.org/journals/artificial-intelligence/articles/10.3389/frai.2024.1330258/full; https://doaj.org/article/903ba595bbe544899ee16fc8513b93f0]
- [inference] Resolution: that does not vindicate pure instrumentalism, because the operational burden has shifted from explanation to continual monitoring, drift detection, and repair; the model remains portable only with extra governance machinery. [source: https://www.frontiersin.org/journals/artificial-intelligence/articles/10.3389/frai.2024.1330258/full; https://doaj.org/article/903ba595bbe544899ee16fc8513b93f0; https://arxiv.org/abs/1812.08233]
- [fact] Tension: some observed failures also reflect weak data infrastructure, delayed reporting, or poor measurement rather than lack of causal structure alone. [source: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9499327/; https://www.frontiersin.org/journals/public-health/articles/10.3389/fpubh.2024.1359368/full]
- [inference] Resolution: better data can reduce forecast error, but it does not by itself solve the intervention problem identified by Pearl, Shpitser, and Peters, namely that association-level fit does not guarantee stability when the environment is changed. [source: https://ftp.cs.ucla.edu/pub/stat_ser/r350-reprint.pdf; https://jmlr.org/papers/v9/shpitser08a.html; https://arxiv.org/abs/1501.01332]

### §5 Depth and Breadth Expansion

- [fact] Technical lens: causal hierarchy and invariance work explain portability as a property of stable mechanisms, not as a side effect of high predictive score on one observational regime. [source: https://jmlr.org/papers/v9/shpitser08a.html; https://arxiv.org/abs/1501.01332; https://arxiv.org/abs/1812.08233]
- [fact] Economic lens: once instability is expected, forecast evaluation has to become local and regime-aware rather than average and retrospective. [source: https://www.aeaweb.org/articles?id=10.1257/jel.20201479; https://www.bu.edu/econ/files/2019/01/structural-change-oxford.pdf]
- [fact] Behavioural lens: once a measure becomes a control target, the people or institutions responding to it can change the process itself, creating a reflexive failure that a score-only model will not explain. [source: https://en.wikipedia.org/wiki/Goodhart%27s_law; https://www.rba.gov.au/publications/rdp/1990/9013/conference-volumes.html]
- [fact] Historical lens: the financial crisis and the COVID-19 pandemic each combined abrupt environmental change with extraordinary policy response, conditions that are particularly hostile to models whose validity depends on continuity of historical regularities. [source: https://www.bis.org/publ/qtrpdf/r_qt0812.htm; https://www.aeaweb.org/articles?id=10.1257/jel.20201479; https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9499327/]
- [inference] Governance lens: explanatory structure is operationally valuable because it narrows what should trigger investigation, what should remain invariant, and what kind of repair is needed when performance drops. [source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq1-2-deutsch-hard-to-vary.md; https://arxiv.org/abs/1501.01332; https://www.frontiersin.org/journals/artificial-intelligence/articles/10.3389/frai.2024.1330258/full]

### §6 Synthesis

**Executive summary:**
- An instrumentalist modeling stance, which treats predictive fruitfulness as sufficient for accepting a model without requiring realistic assumptions or mechanistic explanation, fails in complex dynamic systems because predictive success without causal or mechanistic structure does not remain reliable when interventions, structural breaks, or adaptive gaming change the environment. [inference; source: https://plato.stanford.edu/entries/economics/; https://archive.org/details/essaysinpositive00milt; https://arxiv.org/abs/1501.01332; https://arxiv.org/abs/1812.08233; https://en.wikipedia.org/wiki/Goodhart%27s_law]
- The common failure modes are metric-target deformation, regime brittleness, causal blindness, assumption lock-in, and silent quality decay, all of which appear when a model's score is treated as sufficient evidence that the model has captured what matters. [inference; source: https://en.wikipedia.org/wiki/Goodhart%27s_law; https://www.aeaweb.org/articles?id=10.1257/jel.20201479; https://www.frontiersin.org/journals/public-health/articles/10.3389/fpubh.2024.1359368/full; https://www.frontiersin.org/journals/artificial-intelligence/articles/10.3389/frai.2024.1330258/full]
- The strongest support for that conclusion comes from causal hierarchy and invariance research, which shows that association-level success does not license confidence about interventions or shifted environments. [inference; source: https://jmlr.org/papers/v9/shpitser08a.html; https://arxiv.org/abs/1501.01332; https://arxiv.org/abs/1907.02893]
- The case studies do not show that every predictive model fails under shift, but they do show that prediction-only success pushes more operational work into monitoring and recalibration because the model does not specify what should remain stable. [inference; source: https://www.aeaweb.org/articles?id=10.1257/jel.20201479; https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9499327/; https://doaj.org/article/903ba595bbe544899ee16fc8513b93f0]

**Key findings:**
1. **Accessible summaries of Friedman's methodology treat predictive fruitfulness, not realism of assumptions, as the decisive test of a theory, which makes instrumentalism an epistemic rule for accepting models that predict well without requiring them to explain the underlying mechanism.** ([fact]; low confidence; source: https://archive.org/details/essaysinpositive00milt; https://plato.stanford.edu/entries/economics/; https://en.wikipedia.org/wiki/Essays_in_Positive_Economics)
2. **Goodhart's Law shows that once an observed regularity is pressed into service as a control target, optimisation pressure can change the underlying process and collapse the regularity, so score-maximisation itself becomes a source of model failure rather than proof of model adequacy.** ([inference]; medium confidence; source: https://www.econbiz.de/10002525062; https://www.rba.gov.au/publications/rdp/1990/9013/conference-volumes.html; https://en.wikipedia.org/wiki/Goodhart%27s_law)
3. **Pearl's causal hierarchy and later invariance work jointly imply that observationally successful non-causal predictors can become badly wrong under intervention or environmental change, because only causal or invariant structure is expected to travel across such shifts.** ([fact]; high confidence; source: https://jmlr.org/papers/v9/shpitser08a.html; https://ftp.cs.ucla.edu/pub/stat_ser/r350-reprint.pdf; https://arxiv.org/abs/1501.01332; https://arxiv.org/abs/1812.08233)
4. **Sugihara et al. show that nonlinear dynamic systems can exhibit mirage correlations and require tools stronger than correlation or one-step predictability to detect causation, which means short-run predictive success in such systems can conceal causal misidentification.** ([fact]; medium confidence; source: https://cdanfort.w3.uvm.edu/csc-reading-group/sugihara-causality-science-2012.pdf)
5. **Economic forecasting under structural instability fails through regime brittleness, because crisis periods such as 2007-08 invalidate the assumption that average historical performance is still informative, and instability-aware evaluation must replace simple retrospective scorekeeping.** ([inference]; medium confidence; source: https://www.aeaweb.org/articles?id=10.1257/jel.20201479; https://www.bu.edu/econ/files/2019/01/structural-change-oxford.pdf; https://www.bis.org/publ/qtrpdf/r_qt0812.htm)
6. **Coronavirus Disease 2019 (COVID-19) case forecasting exposed assumption lock-in, because many official-hub models failed to beat simple baselines and were built around continuation assumptions about interventions or behavior that became unreliable as policy, reporting, and variant conditions changed.** ([inference]; medium confidence; source: https://www.frontiersin.org/journals/public-health/articles/10.3389/fpubh.2024.1359368/full; https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9499327/)
7. **Recommendation systems exhibit silent quality decay under preference drift, because yesterday's successful correlations degrade in non-stationary user environments unless the system explicitly models drift, reweights evidence, or equips operators to intervene.** ([inference]; medium confidence; source: https://www.frontiersin.org/journals/artificial-intelligence/articles/10.3389/frai.2024.1330258/full; https://doaj.org/article/903ba595bbe544899ee16fc8513b93f0)
8. **The operational value of explanation is therefore that it makes diagnosis and repair more directed, because mechanistic or invariant accounts narrow what should remain stable, whereas instrumentalist systems rely more heavily on continual monitoring, recalibration, and governance after failure signals appear.** ([inference]; low confidence; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq1-1-popper-falsifiability.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq1-2-deutsch-hard-to-vary.md; https://arxiv.org/abs/1812.08233; https://www.frontiersin.org/journals/artificial-intelligence/articles/10.3389/frai.2024.1330258/full)

**Evidence map:**
| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [fact] Instrumentalism accepts predictive fruitfulness as the main test even when assumptions are unrealistic. | https://archive.org/details/essaysinpositive00milt; https://plato.stanford.edu/entries/economics/; https://en.wikipedia.org/wiki/Essays_in_Positive_Economics | low | secondary summaries only |
| [inference] Turning a score into a target can collapse the regularity that made the score useful. | https://www.econbiz.de/10002525062; https://www.rba.gov.au/publications/rdp/1990/9013/conference-volumes.html; https://en.wikipedia.org/wiki/Goodhart%27s_law | medium | origin corroborated; accessible formulation secondary |
| [fact] Causal or invariant predictors are expected to travel better under interventions and environmental change than non-causal predictors. | https://jmlr.org/papers/v9/shpitser08a.html; https://ftp.cs.ucla.edu/pub/stat_ser/r350-reprint.pdf; https://arxiv.org/abs/1501.01332; https://arxiv.org/abs/1812.08233 | high | multiple primary and methodological sources |
| [fact] Nonlinear dynamic systems can display mirage correlations that make correlation or short-run prediction a poor proxy for causation. | https://cdanfort.w3.uvm.edu/csc-reading-group/sugihara-causality-science-2012.pdf | medium | single primary paper |
| [inference] Structural instability makes average historical forecast performance an unreliable guide during crises. | https://www.aeaweb.org/articles?id=10.1257/jel.20201479; https://www.bu.edu/econ/files/2019/01/structural-change-oxford.pdf; https://www.bis.org/publ/qtrpdf/r_qt0812.htm | medium | cross-source synthesis |
| [inference] COVID-19 case forecasting showed assumption lock-in because many official-hub models failed to beat simple baselines while depending on continuation assumptions about interventions or behavior. | https://www.frontiersin.org/journals/public-health/articles/10.3389/fpubh.2024.1359368/full; https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9499327/ | medium | baseline failure plus interpretive diagnosis |
| [inference] Recommendation quality decays under preference drift unless drift is explicitly modeled or acted on. | https://www.frontiersin.org/journals/artificial-intelligence/articles/10.3389/frai.2024.1330258/full; https://doaj.org/article/903ba595bbe544899ee16fc8513b93f0 | medium | general drift survey plus recommender paper |
| [inference] Explanation can make diagnosis and repair more directed by identifying what should persist across regime change. | https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq1-1-popper-falsifiability.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq1-2-deutsch-hard-to-vary.md; https://arxiv.org/abs/1812.08233; https://www.frontiersin.org/journals/artificial-intelligence/articles/10.3389/frai.2024.1330258/full | low | cross-item synthesis; no direct comparative cost evidence |

**Assumptions:**
- [assumption] The accessible secondary summaries of Friedman's essay and Goodhart's formulation are sufficient to characterise the methodological stance at issue because the original works are uniquely identified and the summaries track the relevant methodological claims closely enough for this item's level of analysis. [source: https://plato.stanford.edu/entries/economics/; https://archive.org/details/essaysinpositive00milt; https://en.wikipedia.org/wiki/Essays_in_Positive_Economics; https://www.econbiz.de/10002525062; https://www.rba.gov.au/publications/rdp/1990/9013/conference-volumes.html; https://en.wikipedia.org/wiki/Goodhart%27s_law]
- [assumption] The selected economic, epidemiological, and recommendation-system cases are representative enough to illustrate recurring operational failure classes without claiming identical proximal causes in every domain. [source: https://www.aeaweb.org/articles?id=10.1257/jel.20201479; https://www.frontiersin.org/journals/public-health/articles/10.3389/fpubh.2024.1359368/full; https://www.frontiersin.org/journals/artificial-intelligence/articles/10.3389/frai.2024.1330258/full]

**Analysis:**
- Instrumentalism and explanatory evaluation fail differently under stress. A predictive model can look successful on one regime because it compresses observed regularities, but that success does not reveal whether the regularity is causal, merely correlative, or already being distorted by the target-seeking behavior of institutions and users. [inference; source: https://en.wikipedia.org/wiki/Essays_in_Positive_Economics; https://en.wikipedia.org/wiki/Goodhart%27s_law; https://cdanfort.w3.uvm.edu/csc-reading-group/sugihara-causality-science-2012.pdf]
- The strongest theoretical reason to expect failure under distribution shift comes from the causal hierarchy and invariance literature, not from any single case study. Those sources say that intervention robustness requires information above association-level fit, which supports the inference that distribution shift exposes exactly what instrumentalism declines to model. [inference; source: https://jmlr.org/papers/v9/shpitser08a.html; https://ftp.cs.ucla.edu/pub/stat_ser/r350-reprint.pdf; https://arxiv.org/abs/1501.01332; https://arxiv.org/abs/1812.08233]
- A plausible rival explanation is that the observed failures came mainly from poor data quality or weak operations rather than from the epistemic stance of instrumentalism itself. That rival explanation is partly correct for COVID-19 and crisis forecasting, but it is incomplete because even perfect observational data do not answer intervention or counterfactual questions unless the model represents causal structure or stable invariants. [inference; source: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9499327/; https://www.aeaweb.org/articles?id=10.1257/jel.20201479; https://arxiv.org/abs/1501.01332]
- Another rival explanation is that continuous retraining, ensembles, or drift-aware adaptation make explanation unnecessary. Those remedies help, but they move the operational burden into ongoing monitoring and repair, which means they mitigate failure without showing that score-first modeling has captured the mechanism. [inference; source: https://www.frontiersin.org/journals/public-health/articles/10.3389/fpubh.2024.1359368/full; https://www.frontiersin.org/journals/artificial-intelligence/articles/10.3389/frai.2024.1330258/full; https://doaj.org/article/903ba595bbe544899ee16fc8513b93f0]

**Risks, gaps, uncertainties:**
- The accessible evidence for Friedman's and Goodhart's original texts is weaker than the evidence for Pearl, Peters, Buhlmann, COVID-19 forecasting, and concept drift, because the seeded primary landing pages were unavailable and the argument depends partly on high-quality secondary summaries. [fact; source: https://archive.org/details/essaysinpositive00milt; https://www.econbiz.de/10002525062; https://www.rba.gov.au/publications/rdp/1990/9013/conference-volumes.html; https://en.wikipedia.org/wiki/Essays_in_Positive_Economics; https://en.wikipedia.org/wiki/Goodhart%27s_law]
- The economic case evidence is strongest on instability and evaluation method, not on a single universally agreed post-mortem that names instrumentalism as the sole cause of 2007-08 forecast failure. [inference; source: https://www.aeaweb.org/articles?id=10.1257/jel.20201479; https://www.bu.edu/econ/files/2019/01/structural-change-oxford.pdf; https://www.bis.org/publ/qtrpdf/r_qt0812.htm]
- Sugihara et al. establish why correlation can mislead in nonlinear systems, but that paper is an ecological causality paper rather than a direct study of economic or epidemiological forecasting operations. [fact; source: https://cdanfort.w3.uvm.edu/csc-reading-group/sugihara-causality-science-2012.pdf]
- The recommendation-system evidence shows drift-aware adaptation is useful, but it does not by itself quantify the exact share of degradation attributable to causal blindness versus interface, catalogue, or product changes. [inference; source: https://www.frontiersin.org/journals/artificial-intelligence/articles/10.3389/frai.2024.1330258/full; https://doaj.org/article/903ba595bbe544899ee16fc8513b93f0]

**Open questions:**
- Which practical metrics best distinguish harmless recalibration from evidence that a model has lost contact with an invariant mechanism? [inference; source: https://arxiv.org/abs/1812.08233; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq1-2-deutsch-hard-to-vary.md]
- How much explanatory structure is enough for operational robustness in settings where fully causal models are infeasible but pure prediction is brittle? [inference; source: https://arxiv.org/abs/1907.02893; https://arxiv.org/abs/2009.00329]
- What governance pattern is cheapest in practice: building more structural explanation into the model, or accepting instrumentalism and funding continual drift detection and repair? [inference; source: https://www.frontiersin.org/journals/artificial-intelligence/articles/10.3389/frai.2024.1330258/full; https://www.aeaweb.org/articles?id=10.1257/jel.20201479]

### §7 Recursive Review

- Review result: pass
- Acronym audit: United States Centers for Disease Control and Prevention (US CDC) expanded on first use; no unexpanded Large Language Model (LLM), Application Programming Interface (API), Command Line Interface (CLI), Software Development Kit (SDK), Personal Access Token (PAT), Model Context Protocol (MCP), Retrieval-Augmented Generation (RAG), chain-of-thought (CoT), Site Reliability Engineering (SRE), Information Technology Service Management (ITSM), Platform as a Service (PaaS), or pull request (PR) abbreviations remain in the drafted prose.
- Claim audit: all visible claims in Research Skill Output carry [fact], [inference], or [assumption] labels; access notes are metadata fragments.
- Source audit: all cited claims bind to URL-backed sources; all entries in Sources include URLs.
- Cross-item integration: Research Question 1.1 and Research Question 1.2 cited in §0, §2, §3, §5, §6, and Findings.
- Remaining uncertainty: strongest around direct access to Friedman's and Goodhart's primary texts, and around how much of each empirical failure is caused by epistemic stance versus data and governance quality.

---

## Findings

### Executive Summary

An instrumentalist modeling stance, which treats predictive fruitfulness as sufficient for accepting a model without requiring realistic assumptions or mechanistic explanation, fails in complex dynamic systems because predictive success without causal or mechanistic structure does not remain reliable when interventions, structural breaks, or adaptive gaming change the environment. [inference; source: https://plato.stanford.edu/entries/economics/; https://archive.org/details/essaysinpositive00milt; https://arxiv.org/abs/1501.01332; https://arxiv.org/abs/1812.08233; https://en.wikipedia.org/wiki/Goodhart%27s_law]

The recurring operational failure modes are metric-target deformation, regime brittleness, causal blindness, assumption lock-in, and silent quality decay. [inference; source: https://en.wikipedia.org/wiki/Goodhart%27s_law; https://www.aeaweb.org/articles?id=10.1257/jel.20201479; https://www.frontiersin.org/journals/public-health/articles/10.3389/fpubh.2024.1359368/full; https://www.frontiersin.org/journals/artificial-intelligence/articles/10.3389/frai.2024.1330258/full]

The strongest support for that conclusion comes from causal hierarchy and invariance research, which shows that association-level success does not license confidence about interventions or shifted environments. [inference; source: https://jmlr.org/papers/v9/shpitser08a.html; https://arxiv.org/abs/1501.01332; https://arxiv.org/abs/1907.02893]

The case studies do not show that every predictive model fails under shift, but they do show that prediction-only success pushes more operational work into monitoring and recalibration because the model does not specify what should remain stable. [inference; source: https://www.aeaweb.org/articles?id=10.1257/jel.20201479; https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9499327/; https://doaj.org/article/903ba595bbe544899ee16fc8513b93f0]

### Key Findings

1. **Accessible summaries of Friedman's methodology treat predictive fruitfulness, not realism of assumptions, as the decisive test of a theory, which makes instrumentalism an epistemic rule for accepting models that predict well without requiring them to explain the underlying mechanism.** ([fact]; low confidence; source: https://archive.org/details/essaysinpositive00milt; https://plato.stanford.edu/entries/economics/; https://en.wikipedia.org/wiki/Essays_in_Positive_Economics)
2. **Goodhart's Law shows that once an observed regularity is pressed into service as a control target, optimisation pressure can change the underlying process and collapse the regularity, so score-maximisation itself becomes a source of model failure rather than proof of model adequacy.** ([inference]; medium confidence; source: https://www.econbiz.de/10002525062; https://www.rba.gov.au/publications/rdp/1990/9013/conference-volumes.html; https://en.wikipedia.org/wiki/Goodhart%27s_law)
3. **Pearl's causal hierarchy and later invariance work jointly imply that observationally successful non-causal predictors can become badly wrong under intervention or environmental change, because only causal or invariant structure is expected to travel across such shifts.** ([fact]; high confidence; source: https://jmlr.org/papers/v9/shpitser08a.html; https://ftp.cs.ucla.edu/pub/stat_ser/r350-reprint.pdf; https://arxiv.org/abs/1501.01332; https://arxiv.org/abs/1812.08233)
4. **Sugihara et al. show that nonlinear dynamic systems can exhibit mirage correlations and require tools stronger than correlation or one-step predictability to detect causation, which means short-run predictive success in such systems can conceal causal misidentification.** ([fact]; medium confidence; source: https://cdanfort.w3.uvm.edu/csc-reading-group/sugihara-causality-science-2012.pdf)
5. **Economic forecasting under structural instability fails through regime brittleness, because crisis periods such as 2007-08 invalidate the assumption that average historical performance is still informative, and instability-aware evaluation must replace simple retrospective scorekeeping.** ([inference]; medium confidence; source: https://www.aeaweb.org/articles?id=10.1257/jel.20201479; https://www.bu.edu/econ/files/2019/01/structural-change-oxford.pdf; https://www.bis.org/publ/qtrpdf/r_qt0812.htm)
6. **Coronavirus Disease 2019 (COVID-19) case forecasting exposed assumption lock-in, because many official-hub models failed to beat simple baselines and were built around continuation assumptions about interventions or behavior that became unreliable as policy, reporting, and variant conditions changed.** ([inference]; medium confidence; source: https://www.frontiersin.org/journals/public-health/articles/10.3389/fpubh.2024.1359368/full; https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9499327/)
7. **Recommendation systems exhibit silent quality decay under preference drift, because yesterday's successful correlations degrade in non-stationary user environments unless the system explicitly models drift, reweights evidence, or equips operators to intervene.** ([inference]; medium confidence; source: https://www.frontiersin.org/journals/artificial-intelligence/articles/10.3389/frai.2024.1330258/full; https://doaj.org/article/903ba595bbe544899ee16fc8513b93f0)
8. **The operational value of explanation is therefore that it makes diagnosis and repair more directed, because mechanistic or invariant accounts narrow what should remain stable, whereas instrumentalist systems rely more heavily on continual monitoring, recalibration, and governance after failure signals appear.** ([inference]; low confidence; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq1-1-popper-falsifiability.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq1-2-deutsch-hard-to-vary.md; https://arxiv.org/abs/1812.08233; https://www.frontiersin.org/journals/artificial-intelligence/articles/10.3389/frai.2024.1330258/full)

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [fact] Instrumentalism accepts predictive fruitfulness as the main test even when assumptions are unrealistic. | https://archive.org/details/essaysinpositive00milt; https://plato.stanford.edu/entries/economics/; https://en.wikipedia.org/wiki/Essays_in_Positive_Economics | low | secondary summaries only |
| [inference] Turning a score into a target can collapse the regularity that made the score useful. | https://www.econbiz.de/10002525062; https://www.rba.gov.au/publications/rdp/1990/9013/conference-volumes.html; https://en.wikipedia.org/wiki/Goodhart%27s_law | medium | origin corroborated; accessible formulation secondary |
| [fact] Causal or invariant predictors are expected to travel better under interventions and environmental change than non-causal predictors. | https://jmlr.org/papers/v9/shpitser08a.html; https://ftp.cs.ucla.edu/pub/stat_ser/r350-reprint.pdf; https://arxiv.org/abs/1501.01332; https://arxiv.org/abs/1812.08233 | high | multiple primary and methodological sources |
| [fact] Nonlinear dynamic systems can display mirage correlations that make correlation or short-run prediction a poor proxy for causation. | https://cdanfort.w3.uvm.edu/csc-reading-group/sugihara-causality-science-2012.pdf | medium | single primary paper |
| [inference] Structural instability makes average historical forecast performance an unreliable guide during crises. | https://www.aeaweb.org/articles?id=10.1257/jel.20201479; https://www.bu.edu/econ/files/2019/01/structural-change-oxford.pdf; https://www.bis.org/publ/qtrpdf/r_qt0812.htm | medium | cross-source synthesis |
| [inference] COVID-19 case forecasting showed assumption lock-in because many official-hub models failed to beat simple baselines while depending on continuation assumptions about interventions or behavior. | https://www.frontiersin.org/journals/public-health/articles/10.3389/fpubh.2024.1359368/full; https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9499327/ | medium | baseline failure plus interpretive diagnosis |
| [inference] Recommendation quality decays under preference drift unless drift is explicitly modeled or acted on. | https://www.frontiersin.org/journals/artificial-intelligence/articles/10.3389/frai.2024.1330258/full; https://doaj.org/article/903ba595bbe544899ee16fc8513b93f0 | medium | general drift survey plus recommender paper |
| [inference] Explanation can make diagnosis and repair more directed by identifying what should persist across regime change. | https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq1-1-popper-falsifiability.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq1-2-deutsch-hard-to-vary.md; https://arxiv.org/abs/1812.08233; https://www.frontiersin.org/journals/artificial-intelligence/articles/10.3389/frai.2024.1330258/full | low | cross-item synthesis; no direct comparative cost evidence |

### Assumptions

- The accessible secondary summaries of Friedman's essay and Goodhart's formulation are sufficient to characterise the methodological stance at issue because the original works are uniquely identified and the summaries track the relevant methodological claims closely enough for this item's level of analysis. [assumption; source: https://archive.org/details/essaysinpositive00milt; https://en.wikipedia.org/wiki/Essays_in_Positive_Economics; https://www.econbiz.de/10002525062; https://www.rba.gov.au/publications/rdp/1990/9013/conference-volumes.html; https://en.wikipedia.org/wiki/Goodhart%27s_law]
- The selected economic, epidemiological, and recommendation-system cases are representative enough to illustrate recurring operational failure classes without claiming identical proximal causes in every domain. [assumption; source: https://www.aeaweb.org/articles?id=10.1257/jel.20201479; https://www.frontiersin.org/journals/public-health/articles/10.3389/fpubh.2024.1359368/full; https://www.frontiersin.org/journals/artificial-intelligence/articles/10.3389/frai.2024.1330258/full]

### Analysis

Instrumentalism and explanatory evaluation fail differently under stress. A predictive model can look successful on one regime because it compresses observed regularities, but that success does not reveal whether the regularity is causal, merely correlative, or already being distorted by target-seeking behavior. [inference; source: https://en.wikipedia.org/wiki/Essays_in_Positive_Economics; https://en.wikipedia.org/wiki/Goodhart%27s_law; https://cdanfort.w3.uvm.edu/csc-reading-group/sugihara-causality-science-2012.pdf]

The strongest theoretical reason to expect failure under distribution shift comes from the causal hierarchy and invariance literature, not from any single case study. Those sources say that intervention robustness requires information above association-level fit, which supports the inference that distribution shift exposes exactly what instrumentalism declines to model. [inference; source: https://jmlr.org/papers/v9/shpitser08a.html; https://ftp.cs.ucla.edu/pub/stat_ser/r350-reprint.pdf; https://arxiv.org/abs/1501.01332; https://arxiv.org/abs/1812.08233]

A plausible rival explanation is that the observed failures came mainly from poor data quality or weak operations rather than from the epistemic stance of instrumentalism itself. That rival explanation is partly correct for COVID-19 and crisis forecasting, but it is incomplete because even perfect observational data do not answer intervention or counterfactual questions unless the model represents causal structure or stable invariants. [inference; source: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9499327/; https://www.aeaweb.org/articles?id=10.1257/jel.20201479; https://arxiv.org/abs/1501.01332]

Another rival explanation is that continuous retraining, ensembles, or drift-aware adaptation make explanation unnecessary. Those remedies help, but they move the operational burden into ongoing monitoring and repair, which means they mitigate failure without showing that score-first modeling has captured the mechanism. [inference; source: https://www.frontiersin.org/journals/public-health/articles/10.3389/fpubh.2024.1359368/full; https://www.frontiersin.org/journals/artificial-intelligence/articles/10.3389/frai.2024.1330258/full; https://doaj.org/article/903ba595bbe544899ee16fc8513b93f0]

### Risks, Gaps, and Uncertainties

- The accessible evidence for Friedman's and Goodhart's original texts is weaker than the evidence for Pearl, Peters, Buhlmann, COVID-19 forecasting, and concept drift, because the seeded primary landing pages were unavailable and the argument depends partly on high-quality secondary summaries. [fact; source: https://archive.org/details/essaysinpositive00milt; https://www.econbiz.de/10002525062; https://www.rba.gov.au/publications/rdp/1990/9013/conference-volumes.html; https://en.wikipedia.org/wiki/Essays_in_Positive_Economics; https://en.wikipedia.org/wiki/Goodhart%27s_law]
- The economic case evidence is strongest on instability and evaluation method, not on a single universally agreed post-mortem that names instrumentalism as the sole cause of 2007-08 forecast failure. [inference; source: https://www.aeaweb.org/articles?id=10.1257/jel.20201479; https://www.bu.edu/econ/files/2019/01/structural-change-oxford.pdf; https://www.bis.org/publ/qtrpdf/r_qt0812.htm]
- Sugihara et al. establish why correlation can mislead in nonlinear systems, but that paper is an ecological causality paper rather than a direct study of economic or epidemiological forecasting operations. [fact; source: https://cdanfort.w3.uvm.edu/csc-reading-group/sugihara-causality-science-2012.pdf]
- The recommendation-system evidence shows drift-aware adaptation is useful, but it does not by itself quantify the exact share of degradation attributable to causal blindness versus interface, catalogue, or product changes. [inference; source: https://www.frontiersin.org/journals/artificial-intelligence/articles/10.3389/frai.2024.1330258/full; https://doaj.org/article/903ba595bbe544899ee16fc8513b93f0]

### Open Questions

- Which practical metrics best distinguish harmless recalibration from evidence that a model has lost contact with an invariant mechanism? [inference; source: https://arxiv.org/abs/1812.08233; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq1-2-deutsch-hard-to-vary.md]
- How much explanatory structure is enough for operational robustness in settings where fully causal models are infeasible but pure prediction is brittle? [inference; source: https://arxiv.org/abs/1907.02893; https://arxiv.org/abs/2009.00329]
- What governance pattern is cheaper in practice: building more structural explanation into the model, or accepting instrumentalism and funding continual drift detection and repair? [inference; source: https://www.frontiersin.org/journals/artificial-intelligence/articles/10.3389/frai.2024.1330258/full; https://www.aeaweb.org/articles?id=10.1257/jel.20201479]

---

## Output

- Type: knowledge
- Description: This item concludes that predictive performance alone is an unstable acceptance criterion in complex dynamic systems, because robustness under shift depends on causal or invariant structure plus governance that can detect when the environment has changed. [inference; source: https://arxiv.org/abs/1501.01332; https://arxiv.org/abs/1812.08233; https://www.frontiersin.org/journals/artificial-intelligence/articles/10.3389/frai.2024.1330258/full]
- Links:
  - https://arxiv.org/abs/1501.01332
  - https://www.aeaweb.org/articles?id=10.1257/jel.20201479
  - https://www.frontiersin.org/journals/public-health/articles/10.3389/fpubh.2024.1359368/full
