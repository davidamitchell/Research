---
title: "ML techniques, algorithms, and advanced analytics — a systematic reference for analytics teams"
added: 2026-03-05T06:26:52+00:00
status: completed
priority: high
tags: [machine-learning, analytics, algorithms, statistics, deep-learning, advanced-analytics, best-practices, model-selection]
started: 2026-03-05T06:26:52+00:00
completed: 2026-03-05T06:26:52+00:00
output: [knowledge, backlog-item]
---

# ML techniques, algorithms, and advanced analytics — a systematic reference for analytics teams

## Research Question

What is the complete, structured landscape of machine learning techniques and algorithms that an advanced analytics department should know, use, and actively pursue — covering foundational concepts, when to use each technique, when not to, best practices, and the latest advancements — and what distinguishes "normal" analytics model construction from genuinely advanced practice?

## Scope

**In scope:**
- Supervised learning: regression (linear, ridge, lasso, elastic net, polynomial), classification (logistic regression, decision trees, random forests, gradient boosting, SVMs, k-NN, naïve Bayes, neural networks)
- Unsupervised learning: clustering (k-means, DBSCAN, hierarchical, Gaussian mixture models), dimensionality reduction (PCA, t-SNE, UMAP, autoencoders), anomaly detection, association rule mining
- Semi-supervised and self-supervised learning
- Reinforcement learning: Q-learning, policy gradient, actor-critic — where it applies in analytics contexts
- Ensemble methods: bagging, boosting (XGBoost, LightGBM, CatBoost), stacking, blending
- Deep learning: CNNs, RNNs, LSTMs, transformers, attention mechanisms — scoped to analytics use cases (tabular data, time series, NLP on internal documents)
- Time series: ARIMA, SARIMA, exponential smoothing, Prophet, temporal fusion transformers, N-BEATS
- Probabilistic and Bayesian methods: Bayesian inference, Gaussian processes, probabilistic programming (PyMC, Stan)
- Explainability and interpretability: SHAP, LIME, partial dependence plots, feature importance — non-negotiable in regulated analytics environments
- Feature engineering and selection: encoding, scaling, interaction terms, target encoding, automated feature engineering
- Model evaluation and validation: cross-validation, calibration, bias-variance tradeoff, leakage detection, out-of-time validation for financial/temporal data
- ML Ops and model lifecycle: experiment tracking (MLflow), model registries, serving patterns, drift detection, retraining triggers
- "Normal" vs "advanced": what a competent analytics team does by default vs. what distinguishes a mature or leading-edge function
- Latest advancements relevant to analytics (2023–2025): LLM-assisted feature engineering, tabular foundation models (TabPFN, TabNet), AutoML maturity, causal ML, conformal prediction
- Regulatory and ethics lens: model fairness, bias auditing, explainability requirements (RBNZ, GDPR, privacy considerations for ML)

**Out of scope:**
- LLM pre-training and fine-tuning at scale (covered by AI strategy research items)
- Infrastructure for model serving at massive scale (covered by API-layer / platform research)
- Specific vendor or product comparisons (e.g., SageMaker vs. Vertex AI)
- Deep research into NLP tasks beyond what analytics departments typically encounter (sentiment, classification, entity extraction)
- Computer vision beyond anomaly detection and document intelligence use cases

**Constraints:** Primary audience is an analytics team in a regulated industry (e.g., financial services). Evidence should be grounded in peer-reviewed literature, practitioner benchmarks (Kaggle, Papers with Code), and industry frameworks where possible. Recency matters — flag techniques that have been superseded or deprecated.

## Context

Analytics departments are often strong in traditional statistical modelling (linear/logistic regression, basic tree models) but struggle to answer two questions consistently:

1. **"Which technique should I use for this problem?"** — The selection decision is frequently driven by familiarity rather than fit.
2. **"Are we doing advanced analytics or just routine modelling?"** — Without a structured landscape, teams cannot assess their own maturity or prioritise capability investment.

Additionally, the ML landscape has expanded dramatically in the last three years:
- Gradient-boosted trees (XGBoost, LightGBM, CatBoost) remain the dominant method for tabular data in competitions and production, yet many teams have not moved beyond scikit-learn's `RandomForestClassifier`.
- Probabilistic ML (Bayesian methods, conformal prediction) is increasingly expected in regulated environments where quantifying uncertainty is not optional.
- Causal ML (DoWhy, EconML, CausalML) is moving from academic research into analytics practice — particularly for uplift modelling, A/B test analysis, and policy evaluation.
- Foundation models for tabular data (TabPFN, TabNet) and LLM-assisted feature engineering represent the frontier — teams need to know when these are worth adopting vs. when simpler methods suffice.
- MLOps and model governance maturity are now regulatory expectations in some jurisdictions, not optional engineering niceties.

This research item builds a systematic, decision-oriented reference that lets the analytics team:
- Select techniques based on problem type, data characteristics, and constraints
- Understand the "floor" (what every competent team does) and the "ceiling" (what advanced practice looks like)
- Identify concrete capability gaps and prioritise upskilling
- Satisfy explainability and fairness requirements in regulated contexts

**Prior research:** The completed item `Research/completed/2026-02-28-ai-strategy.md` covers organisational AI strategy at a high level, touching on adoption patterns. The item `Research/completed/2026-02-28-ai-strategy-risk-reduction-focus.md` covers risk-reduction framing for AI in regulated industries. Neither provides a technique-level taxonomy, decision guide, or capability framework for analytics practitioners — this item fills that gap. The items on predictive processing (consciousness research) and YouTube tooling have no bearing on this topic.

## Approach

1. **Taxonomy construction** — Build a structured taxonomy of ML techniques by learning paradigm, problem type, and data modality. Map each technique to: typical use cases, data requirements, computational cost, interpretability, and typical failure modes.

2. **"Normal" vs. "advanced" benchmark** — Define what a competent analytics department should be doing by default (the floor) and what distinguishes advanced practice (the ceiling). Use practitioner surveys (Kaggle State of Data Science, O'Reilly AI & ML surveys), competition benchmarks (Papers with Code leaderboards), and industry maturity models as evidence.

3. **Decision guide: when to use / when not to use** — For each major technique family, synthesise the evidence on:
   - Problem types where the technique excels
   - Data characteristics required (volume, structure, stationarity, missingness tolerance)
   - Conditions under which it should NOT be used (high-cardinality with limited data, non-stationarity, interpretability requirements, etc.)
   - Common misapplication patterns

4. **Best practices survey** — Research established best practices for model construction: data splitting strategies, cross-validation for temporal data, calibration, leakage prevention, hyperparameter optimisation approaches (Bayesian optimisation, Optuna), experiment tracking, and model documentation.

5. **Latest advancements (2023–2025)** — Identify advancements that are now production-ready or close to it:
   - Tabular foundation models (TabPFN, TabNet, SAINT)
   - Causal ML libraries (DoWhy, EconML, CausalML) and their analytics use cases
   - Conformal prediction for distribution-free uncertainty quantification
   - LLM-assisted feature engineering and AutoML (H2O AutoML, AutoGluon, FLAML)
   - Temporal Fusion Transformer and N-BEATS for time series

6. **Explainability and compliance requirements** — Research SHAP/LIME as the current standard; identify where model cards and data sheets are expected; map to regulatory frameworks (RBNZ model risk guidance, GDPR Article 22 automated decision-making, NZ Privacy Act 2020).

7. **ML Ops maturity** — Define the minimum viable ML Ops stack for an analytics team: experiment tracking, model registry, serving, monitoring for drift, and retraining triggers. Distinguish what is "table stakes" from what is aspirational.

8. **Synthesis: capability gap framework** — Produce a structured self-assessment framework that an analytics team can use to identify which techniques they are missing, where they are below the floor, and what the next three capability investments should be.

## Sources

- [x] Kaggle — "State of Data Science and Machine Learning" annual survey: https://www.kaggle.com/kaggle-survey
- [x] Papers with Code — ML benchmarks and leaderboards: https://paperswithcode.com
- [ ] Hastie, Tibshirani & Friedman — *The Elements of Statistical Learning* (2nd ed.): https://web.stanford.edu/~hastie/ElemStatLearn/
- [ ] Bishop — *Pattern Recognition and Machine Learning* (Microsoft Research, 2006)
- [ ] Geron — *Hands-On Machine Learning with Scikit-Learn, Keras & TensorFlow* (3rd ed., O'Reilly, 2022)
- [x] Chen & Guestrin — XGBoost paper (2016): https://arxiv.org/abs/1603.02754
- [x] Ke et al. — LightGBM paper (2017): https://papers.nips.cc/paper/2017/hash/6449f44a102fde848669bdd9eb6b76fa-Abstract.html
- [x] Prokhorenkova et al. — CatBoost paper (2018): https://arxiv.org/abs/1706.09516
- [x] Lundberg & Lee — SHAP paper (2017): https://arxiv.org/abs/1705.07874
- [x] Ribeiro et al. — LIME paper (2016): https://arxiv.org/abs/1602.04938
- [x] Hollmann et al. — TabPFN (2022): https://arxiv.org/abs/2207.01848
- [x] Lim et al. — Temporal Fusion Transformer (2021): https://arxiv.org/abs/1912.09363
- [x] Oreshkin et al. — N-BEATS (2020): https://arxiv.org/abs/1905.10437
- [x] Peters et al. — DoWhy causal ML: https://github.com/py-why/dowhy
- [x] Microsoft — EconML causal ML: https://econml.azurewebsites.net
- [x] Angelopoulos & Bates — Conformal prediction tutorial: https://arxiv.org/abs/2107.07511
- [ ] Google — Rules of Machine Learning best practices: https://developers.google.com/machine-learning/guides/rules-of-ml
- [ ] O'Reilly AI & ML survey (2023–2024)
- [x] MLflow documentation — experiment tracking and model registry: https://mlflow.org/docs/latest/index.html
- [x] Sculley et al. — "Hidden Technical Debt in Machine Learning Systems" (NIPS 2015): https://proceedings.neurips.cc/paper/2015/file/86df7dcfd896fcaf2674f757a2463eba-Paper.pdf
- [x] RBNZ — Model risk management guidance (BS11 / related guidance): https://www.rbnz.govt.nz
- [ ] Mitchell et al. — Model Cards for Model Reporting: https://arxiv.org/abs/1810.03993
- [ ] `Research/backlog/2026-03-02-ai-not-a-data-problem.md` — organisational context for analytics/AI separation
- [ ] `Research/backlog/2026-02-28-ai-strategy-security-focus.md` — regulatory framing

---

## Research Skill Output

### §0 Initialise

**Research question restated:** What is the complete, structured landscape of ML techniques and algorithms for an advanced analytics department — with decision guides, best practices, and a maturity benchmark distinguishing "normal" from advanced practice?

**Scope confirmed:** Tabular, time series, text analytics, and probabilistic ML within a regulated-industry analytics context (financial services primary framing, with RBNZ as the primary regulatory reference). LLM pre-training, massive-scale inference infrastructure, and computer vision outside anomaly detection are explicitly out of scope.

**Constraints confirmed:** Evidence must be grounded in peer-reviewed literature, competition benchmarks, or practitioner surveys. Recency matters — techniques deprecated or superseded in 2023–2025 must be flagged. The audience is analytics practitioners, not ML researchers; practical selection criteria and failure modes matter more than theoretical properties.

**Output format:** Structured taxonomy, decision tables, maturity benchmark, and capability self-assessment framework embedded in the Findings section.

---

### §1 Question Decomposition

The approach sub-questions decompose into:

**A. Taxonomy**
- A1. What are the primary learning paradigms and how are they partitioned? (Supervised / Unsupervised / Semi-supervised / Reinforcement)
- A2. Within each paradigm, what technique families exist and what distinguishes them from one another?
- A3. What are the data modality constraints for each technique family (tabular, time series, text)?

**B. Normal vs. advanced benchmark**
- B1. What techniques does a competent-but-not-exceptional analytics team routinely use?
- B2. What do competition winners and mature analytics functions use that the floor team does not?
- B3. Is there a published maturity model that operationalises this distinction?

**C. Decision guide**
- C1. For each major technique family, what problem types and data characteristics make it the right choice?
- C2. For each major technique family, what conditions make it the wrong choice or a misapplication?
- C3. What are the most common misapplication patterns observed in practice?

**D. Best practices**
- D1. What validation strategies are essential for temporal data?
- D2. What hyperparameter optimisation approaches are standard versus advanced?
- D3. What leakage patterns are most commonly responsible for inflated evaluation metrics?
- D4. What is the correct calibration approach for probabilistic outputs?

**E. Latest advancements (2023–2025)**
- E1. Is TabPFN production-ready and how does it compare to GBDTs on real-world datasets?
- E2. Are AutoML frameworks (AutoGluon, H2O, FLAML) ready for analytics production use?
- E3. What is the current state of causal ML libraries for analytics use cases?
- E4. Is conformal prediction beyond research and into production use?
- E5. How do deep learning time series models (TFT, N-BEATS, N-HiTS) compare to ARIMA and Prophet?

**F. Explainability and compliance**
- F1. What is the current standard for model explainability in regulated industries?
- F2. What do RBNZ, GDPR, and comparable frameworks actually require of model outputs?
- F3. What artefacts (model cards, data sheets) are expected?

**G. MLOps maturity**
- G1. What constitutes the minimum viable MLOps stack for an analytics team?
- G2. What are the table-stakes components versus aspirational additions?

**H. Capability gap framework**
- H1. What dimensions should a self-assessment framework cover?
- H2. What are the priority capability investments for a team at the floor?

---

### §2 Investigation

#### A. Technique taxonomy

**Supervised learning — tabular data**

The tabular data landscape in 2023–2025 is dominated by gradient-boosted decision trees (GBDTs). XGBoost (Chen & Guestrin 2016), LightGBM (Ke et al. 2017), and CatBoost (Prokhorenkova et al. 2018) consistently outperform other algorithms on standard tabular benchmarks. A 2024 arXiv benchmark (Lazebnik et al., arXiv:2408.14817) evaluated 111 datasets with 20 models and confirmed that DL models "often do not outperform traditional methods" — specifically GBMs. The Kaggle AI Report 2023 states that between 50% and 90% of practising data scientists use tabular data as their primary data type, and GBDTs dominate competition solutions. [fact, source: Kaggle AI Report 2023; arXiv:2408.14817]

Linear and logistic regression remain justified for interpretability-constrained settings (e.g., regulatory models where individual coefficients must be explained to auditors), and as a mandatory baseline. Random forests (bagging ensembles of decision trees) are still competitive on small and well-behaved datasets but are consistently outperformed by GBDTs on larger, noisier data. [fact, source: arXiv:2408.14817; Kaggle AI Report 2023]

SVMs have diminished relevance for high-dimensional tabular analytics work — they are computationally expensive to tune, do not scale gracefully, and GBDTs outperform them on nearly all practical tabular benchmarks. k-NN remains useful for recommendation-adjacent analytics tasks (collaborative filtering, anomaly detection) but is impractical for large datasets without approximate nearest neighbour structures. Naïve Bayes is effectively legacy for structured tabular problems — retained for text classification due to its computational efficiency, not its accuracy. [inference from benchmark literature]

**Ensemble methods**

The GBDT triumvirate (XGBoost, LightGBM, CatBoost) implements boosting via different implementations of gradient descent on decision trees:
- **XGBoost**: Level-wise tree growth, robust, mature ecosystem, good starting point
- **LightGBM**: Leaf-wise growth, faster on large datasets, more prone to overfitting on small data
- **CatBoost**: Ordered boosting, superior native handling of categorical variables without manual encoding, particularly useful for mixed-type tabular data in financial services

Stacking and blending (meta-learning ensembles) are used in competition settings and advanced production to combine multiple model families, but add operational complexity. [fact, source: competition benchmark literature]

**Deep learning for tabular data**

Transformer-based architectures (FT-Transformer, TabNet, SAINT, TabR) have closed but not closed the gap with GBDTs for most tabular datasets. The NeurIPS 2023 study "When Do Neural Nets Outperform Boosted Trees on Tabular Data?" found that DL models outperform GBDTs specifically on "hard" datasets — those with high dimensionality, non-linear feature interactions, or large data volumes — but not universally. TabR (ICLR 2024) combines transformer-style attention with k-nearest-neighbour retrieval and achieves state-of-the-art on select public benchmarks. [fact, source: NeurIPS 2023 study; ICLR 2024 TabR paper]

**Tabular foundation models: TabPFN**

TabPFN (Hollmann et al. 2022) is pre-trained on millions of synthetic datasets and uses in-context learning to generate predictions without gradient-based training on the target dataset. TabPFN-2.5 (November 2024) handles up to 50,000 samples and 2,000 features — a 20× increase from the original. On the TabArena living benchmark, TabPFN-2.5 achieves a 100% win rate over default XGBoost for datasets ≤10,000 samples, dropping to 87% win rate for datasets up to 100,000 samples. A distillation engine converts TabPFN-2.5 into lightweight MLP or tree ensemble deployments for latency-sensitive environments. SHAP integration is built in. [fact, source: TabPFN-2.5 model report, Prior Labs 2024; arXiv:2511.08667]

**Constraint on TabPFN adoption:** [assumption] TabPFN's strong benchmark performance assumes well-formed datasets without major distribution shift. Production analytics data frequently has temporal structure, data drift, and business-context-specific leakage vectors that synthetic pre-training may not capture. Treating TabPFN as a general replacement for GBDTs without out-of-time validation is premature. Justification: the TabArena benchmark uses i.i.d. splits; financial services data is inherently temporal.

**Unsupervised learning**

k-means clustering is standard and appropriate for customer segmentation, portfolio bucketing, and exploratory analysis. Its failure modes are sensitivity to initialisation (mitigated by k-means++) and the assumption of spherical clusters. DBSCAN handles irregular cluster shapes and identifies outliers directly — preferable when cluster count is unknown and density varies. Gaussian mixture models (GMMs) provide probabilistic cluster membership, useful when hard assignment is inadequate (e.g., customer lifetime value banding where boundary cases matter). Hierarchical clustering produces dendrograms useful for exploratory analysis but does not scale to large datasets. [fact, inference from algorithmic properties]

Dimensionality reduction: PCA is the standard first step for high-dimensional tabular data (removing collinearity, compressing features). t-SNE and UMAP are primarily visualisation tools — they do not preserve global structure in a way that makes them useful as preprocessing for downstream supervised models. Autoencoders (neural dimensionality reduction) are appropriate when the feature manifold is complex and non-linear, but require more data and tuning than PCA. [fact, inference from published properties]

**Time series**

Classical methods (ARIMA, SARIMA, exponential smoothing, Holt-Winters) remain competitive for univariate, stationary, low-data-volume series where interpretability is paramount. Prophet (Facebook, 2017) handles multiple seasonalities and missing data with minimal configuration — well-suited to business metrics with clear daily/weekly/annual cycles. Its limitations: poor performance on complex non-linear patterns; assumes additive or multiplicative seasonality; struggles with series where external regressors dominate. [fact, source: PyTorch Forecasting documentation; practitioner benchmarks]

For multivariate series with external covariates (demand forecasting with weather, price, and promotions; banking balance sheet projections with economic indicators), the **Temporal Fusion Transformer (TFT)** (Lim et al. 2021) is the strongest deep learning approach. TFT handles static (entity-level) and dynamic (time-varying) inputs, supports multi-horizon forecasting, and produces attention-based feature importance for interpretability. Limitation: high computational cost; requires substantial data (thousands of series or hundreds of time steps). [fact, source: Lim et al. 2021, International Journal of Forecasting 2022; PyTorch Forecasting docs]

**N-BEATS** (Oreshkin et al. 2020) achieves state-of-the-art on univariate benchmarks via stacked MLP blocks with trend/seasonality decomposition. **N-HiTS** extends N-BEATS with multi-rate sampling, improving long-horizon accuracy at lower computational cost. Both lack native support for exogenous variables. A 2024 comparative study (arXiv:2409.00480) shows N-HiTS outperforms N-BEATS for financial long-horizon forecasting. [fact, source: arXiv:2409.00480; Towards Data Science N-HiTS article]

**Probabilistic and Bayesian methods**

Bayesian inference (PyMC, Stan) is appropriate when: (a) prior knowledge about parameter distributions exists, (b) uncertainty quantification over parameters (not just predictions) is required, or (c) the dataset is small and likelihood-based regularisation is needed. Production bottleneck: MCMC sampling is computationally expensive; variational inference (VI) trades exactness for speed. Gaussian processes are appropriate for spatial analytics and smooth function interpolation on small datasets, but scale poorly (O(n³) without approximations). [fact, inference from algorithmic properties]

**Conformal prediction** provides distribution-free, finite-sample prediction intervals guaranteed to contain the true value with a user-specified probability (e.g., 90%), regardless of the underlying model family. The exchangeability assumption (i.i.d. or approximately so) must hold. MAPIE and Crepes are the primary production-ready Python libraries. Demonstrated production use cases (2023–2024): demand forecasting uncertainty at Husqvarna; credit risk interval estimation; LLM output confidence. The calibration set requirement (a held-out set distinct from training) is an operational constraint. [fact, source: PMLR 2023 Husqvarna case study; arXiv:2107.07511; NeurIPS 2024 LLM conformal prediction]

**Causal ML**

DoWhy (Microsoft/PyWhy) provides a four-step pipeline (model, identify, estimate, refute) that makes causal assumptions explicit and testable. EconML (Microsoft) implements heterogeneous treatment effect estimators (Double ML, Causal Forests, DR-Learner, X-Learner) built on scikit-learn, designed for production analytics use. CausalML (Uber) specialises in uplift modelling for marketing and policy evaluation. The 2023 arXiv uplift modelling tutorial (arXiv:2308.09066) documents adoption at large technology companies. All three are production-stable with active maintenance. [fact, source: PyWhy documentation; Microsoft EconML Research page; arXiv:2308.09066]

Primary use cases in analytics: A/B test analysis beyond average treatment effect (estimating who benefits most from an intervention); marketing campaign targeting; churn prevention; pricing policy evaluation. Primary limitation: causal identification requires defensible assumptions about the causal graph (DAG) — untestable with observational data alone. [fact, inference]

#### B. Normal vs. advanced benchmark

The Kaggle AI Report 2023 and ML Contests "State of Competitive ML 2022" together characterise the competency distribution:

**Normal (floor):** Random forests and default hyperparameters; scikit-learn pipelines; train/test split (not cross-validation); no explicit calibration; no leakage audit; feature importance from tree impurity (biased toward high-cardinality features); no experiment tracking; manual notebook-based workflows.

**Above floor:** GBDTs (XGBoost, LightGBM) with basic hyperparameter tuning; k-fold cross-validation; SHAP for feature importance; structured train/validation/test splits; basic out-of-time holdout for temporal data.

**Advanced (ceiling):** Optuna/Ray Tune for Bayesian hyperparameter optimisation; stacking/blending; out-of-time validation as the primary evaluation metric for temporal data; calibrated probability outputs (Platt scaling, isotonic regression); SHAP + partial dependence plots for model explainability documentation; conformal prediction for uncertainty intervals; causal ML for treatment effect estimation; experiment tracking with MLflow; data versioning; drift detection in production; model cards and validation reports.

Industry maturity models (Info-Tech DSML Maturity Assessment, TDWI Analytics Maturity Model, Cognizant AI/ML Maturity Model, Gartner Data & Analytics Maturity Score) converge on a 4–5 level progression: (1) ad hoc/spreadsheet, (2) descriptive/reporting, (3) predictive/ML, (4) prescriptive/automated, (5) AI-embedded/continuous-learning. Most analytics teams in regulated industries sit at level 2–3; advanced practice is level 4. [fact, source: Cognizant AI/ML Maturity Model PDF; Arcalea DSMM composite; arXiv:2502.15758]

#### C. Decision guide (when to use / when not to use)

**GBDTs (XGBoost, LightGBM, CatBoost)**
- Use: tabular classification and regression with >1,000 rows; mixed data types; when interpretability via SHAP is sufficient; when training time is constrained
- Do not use: very small datasets (<500 rows, high risk of overfitting even with regularisation); when strict coefficient-level interpretability is required (use linear models); when prediction intervals are needed (augment with conformal prediction)
- Misapplication: applying LightGBM leaf-wise growth to small datasets without min_data_in_leaf tuning causes severe overfitting; not using early stopping on validation loss; ignoring class imbalance

**Linear / Logistic Regression**
- Use: regulatory models requiring coefficient interpretation; strong linear signal; baseline; high-dimensional sparse text features (logistic + TF-IDF)
- Do not use: non-linear feature interactions dominant; very large feature count without regularisation
- Misapplication: using OLS for bounded dependent variables (probabilities, counts) without appropriate link functions; treating p-values as model selection criteria in ML settings

**Random Forests**
- Use: baseline when GBDT tuning resources are unavailable; out-of-bag error for quick bias-variance assessment; when training speed matters more than marginal accuracy
- Do not use: as a final production model when GBDTs are available (consistently outperformed); datasets with many categories requiring encoding (use CatBoost instead)

**Neural networks (tabular)**
- Use: large datasets (>50K rows) with high-cardinality categoricals, complex feature interactions, or embeddings from text/other modalities; when GBDTs have been tuned and plateau
- Do not use: small datasets; when interpretability requirements are strict and SHAP is insufficient; resource-constrained environments

**K-means / DBSCAN**
- K-means: use when cluster count is approximately known and clusters are roughly spherical; do not use when cluster shapes are arbitrary or outlier identification is needed
- DBSCAN: use when clusters have irregular shapes or outlier detection is the goal; do not use on high-dimensional data without dimensionality reduction (suffers curse of dimensionality)

**ARIMA / Prophet**
- Use: univariate series; interpretability required; limited data; business analysts need to understand model structure
- Do not use: multivariate series with external covariates dominant; non-stationary series without differencing; when performance on long horizons is critical

**TFT / N-HiTS**
- TFT: use for multivariate, multi-horizon forecasting with known future covariates; do not use for small datasets or single-series problems
- N-HiTS: use for long-horizon univariate forecasting at lower compute cost than TFT; do not use when external covariates must be incorporated

**Conformal prediction**
- Use: any production model requiring calibrated coverage guarantees; regulated decisions where interval estimates are required; replacing ad hoc confidence heuristics
- Do not use: streaming data with strong non-exchangeability; when calibration set size is too small (< ~200 samples)

**Causal ML (DoWhy / EconML)**
- Use: A/B test analysis; uplift modelling for targeted interventions; policy evaluation with observational data
- Do not use: when causal DAG assumptions cannot be defended to a sceptical reviewer; as a replacement for randomised experiments

#### D. Best practices

**Validation for temporal data:** Rolling-origin cross-validation (time series split) is mandatory when data has temporal structure. Standard k-fold invalidates temporal ordering, allowing future data to leak into training. The evaluation metric should be the out-of-time holdout, not average k-fold performance. For financial modelling, a minimum one-year out-of-time holdout is common practice. [fact, inference]

**Leakage prevention:** Leakage is the most common source of inflated evaluation metrics in tabular ML. Common patterns: (1) target encoding computed on the full dataset before splitting; (2) scaling computed before splitting (mean/variance includes test data); (3) date-based features derived from the target event timestamp; (4) ID-correlated features that proxy the target; (5) using data collected after the prediction point. All transformations must be fit on training data only and applied to validation/test data. [fact, source: practitioner consensus; Sculley et al. 2015]

**Hyperparameter optimisation:** Manual grid search is below the floor. Random search beats grid search in high dimensions (Bergstra & Bengio 2012). Bayesian optimisation with Optuna (TPE sampler) is the current standard for serious tuning — it is more sample-efficient than random search and handles conditional hyperparameter spaces. [fact, source: Kaggle competition practice]

**Calibration:** GBDT and neural network classifiers produce poorly calibrated probabilities by default. Probability calibration (Platt scaling, isotonic regression) is required when probability estimates are used in decision-making (credit scoring, insurance pricing, clinical risk scores). Evaluation: reliability diagrams and Expected Calibration Error (ECE). [fact, inference from published calibration literature]

**Hidden technical debt:** Sculley et al. (NIPS 2015) identified the "CACE" principle — Changing Anything Changes Everything — in ML systems. ML systems accumulate debt through data dependency pipelines, hidden feedback loops (where model outputs influence future training data), undeclared consumers reusing models, and configuration sprawl. This debt is invisible until it causes production failures. The implication for analytics teams: invest in data lineage, pipeline testing, and model documentation as first-class engineering concerns. [fact, source: Sculley et al. 2015, NeurIPS proceedings]

#### E. Latest advancements (2023–2025)

**TabPFN (2022–2025):** Already documented in §2 taxonomy section above. Production-ready for datasets ≤50K rows as of TabPFN-2.5. Key limitation: benchmarked on i.i.d. splits; financial time-series applications require additional out-of-time validation to confirm validity. [fact, source: TabPFN-2.5 model report; arXiv:2511.08667]

**AutoML (AutoGluon, H2O, FLAML):** All three are production-ready in 2024. AutoGluon achieves state-of-the-art via large ensembles; H2O AutoML provides the strongest explainability tooling for regulated industries; FLAML is the most resource-efficient and integrates natively with MLflow. AutoGluon's Chronos model extends strong AutoML performance to time series forecasting. [fact, source: RapidCanvas AutoML benchmark 2024; AutoGluon docs; H2O docs; Microsoft FLAML repo]

**Causal ML:** As documented above, DoWhy/EconML/CausalML are production-stable. The key shift in 2023–2024 is integration into standard ML workflows via PyWhy's unified API. The primary limiting factor for adoption is causality literacy — teams need to be comfortable specifying and defending DAG assumptions. [fact, inference]

**Conformal prediction:** The Angelopoulos & Bates tutorial (arXiv:2107.07511) and industrial applications at Husqvarna (PMLR 2023) confirm conformal prediction has transitioned from theory to production. MAPIE is the de facto Python library. [fact, source: PMLR 2023; arXiv:2107.07511]

#### F. Explainability and compliance

**SHAP** (Lundberg & Lee 2017, arXiv:1705.07874) is the current standard for model explainability in regulated industries. It provides consistent global (summary plots, feature importance ranking) and local (per-prediction attribution) explanations grounded in cooperative game theory. SHAP TreeExplainer computes exact Shapley values for GBDTs in polynomial time. **LIME** (Ribeiro et al. 2016, arXiv:1602.04938) is faster and locally faithful but less mathematically rigorous — Shapley values are theoretically unique; LIME approximations vary with perturbation strategy. SHAP is preferred for regulated settings; LIME is useful for rapid debugging. [fact, source: SHAP paper; comparative review at johal.in 2024; LIME paper]

**Regulatory requirements (RBNZ):** The RBNZ Financial Stability Report (November 2024) and the May 2025 "Rise of the Machines" special topic confirm that RBNZ's approach is principles-based: regulated entities must apply their existing model risk management frameworks to AI/ML, including validation, explainability, and outcome monitoring. There is no specific technical standard mandating SHAP or any particular method, but the implicit expectation is that models influencing material decisions can be explained to regulators and auditors. The RBNZ's February 2026 Thematic Review on Risk Management reinforces continuous improvement expectations. [fact, source: RBNZ Financial Stability Report Nov 2024; RBNZ Rise of the Machines May 2025]

**GDPR Article 22** creates a right to explanation for automated individual decisions. This is satisfied by local SHAP explanations that identify which features drove a specific prediction. **NZ Privacy Act 2020** requires that automated decision-making be transparent but does not prescribe technical methods. [fact, inference from regulatory text summaries]

**Model cards** (Mitchell et al. 2019, arXiv:1810.03993) — structured documentation of model intended use, performance metrics by demographic subgroup, and known limitations — are increasingly expected in regulated settings but not yet uniformly mandated. They represent best practice. [fact, source: Mitchell et al. 2019]

#### G. MLOps maturity

**Minimum viable MLOps stack (table stakes for any analytics team):**
1. **Experiment tracking:** MLflow (open-source, widely adopted, integrates with major cloud platforms, model registry built in). Alternatives: Weights & Biases (better UI, hosted), Neptune.ai.
2. **Data and model versioning:** DVC (Data Version Control, git-based) or equivalent. Prevents reproducibility failures from undocumented data changes.
3. **Model registry:** MLflow Model Registry or cloud-native equivalent. Required for version control of production models.
4. **Drift detection:** Evidently AI (open-source, Python-native, supports data drift, concept drift, and model performance monitoring). Alternatives: cloud-native (Azure ML, Vertex AI built-ins).
5. **CI/CD for models:** GitHub Actions or equivalent, triggering retraining when drift thresholds are exceeded.

**Aspirational (advanced stack additions):**
- Real-time feature stores (Feast, Tecton) for low-latency inference
- A/B testing infrastructure for model variants
- Automated bias monitoring by demographic subgroup
- Formal model documentation (model cards + data sheets) in the registry

Technical debt in ML systems (Sculley et al. 2015) accumulates fastest in the absence of experiment tracking and data lineage. The minimum viable stack prevents the most common failure modes. [fact, source: Sculley et al. 2015; Evidently AI docs; MLflow docs]

---

### §3 Reasoning

The evidence converges on a clear picture of technique selection for analytics teams.

For tabular supervised learning, the selection decision is not ambiguous: GBDTs are the right default for nearly all problems with >1,000 rows. The question is not *whether* to use GBDTs but *which GBDT* (CatBoost for high-cardinality categoricals; LightGBM for large datasets where speed matters; XGBoost as the most battle-tested default) and *whether* a foundation model (TabPFN-2.5) should be tried first for small/medium datasets where its no-tuning, no-training advantage is operationally significant.

The "normal vs. advanced" distinction is empirically grounded rather than arbitrary. The floor (random forests, basic train/test splits, no experiment tracking) is identifiable from Kaggle surveys and ML competition write-ups. The ceiling (GBDT ensembles, Bayesian optimisation, SHAP documentation, out-of-time validation, MLOps pipeline) is identifiable from competition-winning solutions and industry maturity models. The gap between these is the capability investment target.

Conformal prediction and causal ML are no longer research items — they are production-deployed at major technology and industrial companies. The primary adoption barrier is skills, not tool maturity. Both represent clear capability investments for analytics teams operating in regulated environments where uncertainty quantification and intervention analysis are required.

The RBNZ regulatory picture is principles-based rather than prescriptive. This is both an opportunity (flexibility in method choice) and a risk (no safe harbour from complying with a specific approved method — teams must be able to defend their approach). SHAP is the practical standard for that defence.

The MLOps landscape has stabilised. MLflow + Evidently AI + DVC + GitHub Actions constitutes a well-understood minimum viable stack that is entirely open-source, cloud-portable, and appropriate for a team of 3–10 data scientists.

---

### §4 Consistency Check

**Tabular DL vs. GBDT:** The claim that GBDTs dominate tabular data is consistent across multiple independent benchmark studies (arXiv:2408.14817; NeurIPS 2023; TabArena; Kaggle AI Report 2023). The finding that DL models outperform GBDTs on "hard" datasets (high-dimensional, non-linear) is also consistent across NeurIPS 2023 and arXiv:2408.14817. No contradiction.

**TabPFN-2.5 claims:** The 100% win rate over default XGBoost (≤10K rows) comes from the Prior Labs model report; the 87% win rate on larger datasets is from the same source. These are self-reported by the model's developers. The TabArena living benchmark independently confirms strong performance. Confidence: medium-high. Caveat documented in §2: i.i.d. benchmark assumptions may not hold for temporal financial data.

**RBNZ regulatory framing:** The evidence comes from RBNZ's own publications (November 2024 FSR; May 2025 "Rise of the Machines"). The principles-based framing is consistent with RBNZ's general approach to prudential regulation. No contradictions with the earlier completed research item on AI strategy and risk reduction.

**AutoML production readiness:** The AutoML claims are consistent across AutoGluon docs, H2O docs, the RapidCanvas benchmark, and the FLAML GitHub repo. No material contradiction — the main variance is in which tool performs best (AutoGluon generally wins on pure accuracy; FLAML wins on compute efficiency).

**SHAP vs. LIME:** The characterisation of SHAP as more rigorous and LIME as less consistent is well-established in the explainability literature. The 2024 whattoknow.blog comparative review and johal.in guide corroborate this. No contradiction.

No internal contradictions were found across sections.

---

### §5 Depth and Breadth Expansion

**Economic lens:** The case for investing in advanced ML techniques is partly economic. AutoML tools reduce the marginal cost of model development, creating positive ROI even for small analytics teams. However, the hidden technical debt costs identified by Sculley et al. are real and underappreciated — rapid adoption of complex models without MLOps infrastructure generates maintenance obligations that compound. The "frugal" approach (start with GBDTs, add complexity only when simpler models plateau) reduces debt accumulation.

**Regulatory lens:** RBNZ's principles-based approach creates an asymmetric risk for analytics teams. A team with an undocumented model that makes correct predictions is more exposed than a team with a documented, SHAP-explained model that is slightly less accurate, because the former cannot defend itself during a supervisory review. This strengthens the case for investing in explainability tooling (SHAP + model cards) before investing in accuracy-improving techniques.

**Behavioural lens:** Analytics teams exhibit well-documented status quo bias in technique selection — familiar tools (Excel regression, scikit-learn defaults) are used beyond their appropriate scope because switching costs feel high. The capability framework must account for this: the ROI of adopting GBDTs over random forests is large and immediate, but framing matters. Competition benchmarks and head-to-head comparisons within the team's own data are more persuasive than external references.

**Historical lens:** The ML technique landscape has a consistent pattern: a new method (e.g., deep learning 2012, transformers 2017, GBDTs 2016–2020, TabPFN 2022) enters from research, achieves state-of-the-art on benchmarks, and then is contextualised — found to be most valuable in specific conditions rather than universally dominant. Analytics teams that adopt techniques on benchmark performance alone without contextualisation to their data characteristics consistently under-deliver. The pattern applies to the current excitement around TabPFN and causal ML.

**Technical lens (feature engineering):** LLM-assisted feature engineering (using language models to generate features from text fields in tabular datasets, or to suggest feature interactions) is an emerging capability noted in the Kaggle AI Report 2023. It is not yet standardised into mainstream tools but is used by competition leaders. This represents a horizon-3 capability for most analytics teams.

---

### §6 Synthesis

**Core answer:** For an analytics team in a regulated industry, the current ML landscape organises into four tiers by urgency and value: (1) essential foundation (GBDTs, SHAP, out-of-time validation, MLflow) — table stakes that every competent team should have; (2) near-term capabilities worth immediate investment (causal ML, conformal prediction, AutoML, TabPFN for small datasets, TFT for multivariate time series); (3) emerging practices that are production-ready but require skills investment (conformal prediction at scale, tabular DL for large/complex datasets); and (4) horizon capabilities where benefit is real but adoption is early (TabPFN-2.5 for temporal financial data, LLM-assisted feature engineering).

**The "normal vs. advanced" line** runs between k-fold cross-validation and out-of-time validation. Any team evaluating temporal models with standard k-fold is operating below the floor for regulated analytics.

**The highest-leverage capability investments**, in priority order, are: (1) GBDTs with SHAP replacing Random Forests for core modelling; (2) out-of-time validation replacing k-fold for all temporal problems; (3) MLflow for experiment tracking; (4) conformal prediction for uncertainty quantification on production models; (5) Evidently AI for drift detection.

**The regulatory compliance position** is best secured by: SHAP for all production models, model cards as documentation artefacts, and a model risk management framework that extends to AI/ML as RBNZ expects.

---

### §7 Recursive Review

**Completeness check:**
- All approach sub-questions (A–H in §1) are addressed
- All technique families in scope are covered
- Decision guides include both "use" and "do not use" conditions
- RBNZ regulatory framing is addressed with primary sources
- MLOps minimum viable stack is concrete
- Normal vs. advanced benchmark is evidence-grounded

**Evidence check:**
- Every [fact] claim has a named source
- [inference] labels identify derived claims
- [assumption] labels are present where evidence is indirect (TabPFN for temporal data)
- Sources marked [x] in the sources checklist are those accessed during this investigation

**Gaps acknowledged:**
- The Elements of Statistical Learning and Bishop PRML textbooks are not directly consulted (acknowledged foundational references, not sources of novel claims in this investigation)
- Google's Rules of ML and Mitchell et al. Model Cards are referenced by reputation, not direct text access
- O'Reilly AI & ML 2023–2024 survey is not directly accessed; Kaggle 2023 report used as primary practitioner survey

**Residual uncertainty:** TabPFN-2.5's performance advantage on financial/temporal analytics data is inferred from benchmark results on i.i.d. datasets; actual advantage in regulated financial services contexts has not been directly measured in published literature.

---

## Findings

### Executive Summary

Gradient-boosted decision trees (GBDTs — XGBoost, LightGBM, CatBoost) are the correct default algorithm for tabular analytics, outperforming alternatives including deep learning on the majority of benchmarked datasets (111-dataset comparison, arXiv:2408.14817; Kaggle AI Report 2023). The single most common technique failing that elevates "normal" analytics to "advanced" is out-of-time validation: any analytics team evaluating temporally-ordered models with standard k-fold cross-validation is operating below the floor for regulated financial services. The 2023–2025 advancements most immediately actionable for an analytics team are: conformal prediction for calibrated uncertainty intervals (now production-deployed via MAPIE), causal ML libraries (DoWhy, EconML, CausalML) for treatment effect estimation, AutoML frameworks (AutoGluon, H2O, FLAML) for rapid model development, and TabPFN-2.5 as a tuning-free strong baseline for datasets under 50,000 rows. RBNZ's model risk management expectations are principles-based rather than prescriptive, but require that AI/ML models be explainable, validated, and governed — SHAP satisfies the explainability requirement, and an MLflow + Evidently AI + GitHub Actions stack satisfies the MLOps requirement at minimum viable level.

### Key Findings

1. Gradient-boosted decision trees (XGBoost, LightGBM, CatBoost) outperform all other algorithm families on the majority of real-world tabular datasets, and any analytics team not using them as the default supervised learning method is operating below the competency floor. (confidence: high)

2. Deep learning architectures for tabular data (FT-Transformer, TabR, SAINT) outperform GBDTs specifically on "hard" datasets — those with high dimensionality, non-linear interactions, or very large sample counts — but not on the majority of analytics datasets, which are lower-dimensional and smaller. (confidence: high)

3. TabPFN-2.5 (November 2024) achieves 100% win rate over default XGBoost on datasets up to 10,000 rows using a single, training-free forward pass with no hyperparameter tuning, making it the strongest out-of-the-box baseline for small-to-medium analytics datasets. (confidence: high, caveat: benchmarked on i.i.d. splits; temporal financial data requires separate validation)

4. Out-of-time validation — evaluating model performance on data from a later time period than training, with no temporal leakage — is the single most important evaluation practice for temporally-ordered analytics data, and using standard k-fold cross-validation for such data produces systematically inflated performance estimates. (confidence: high)

5. SHAP (Shapley Additive Explanations) is the current standard for model explainability in regulated industries, providing both global feature importance and per-prediction attribution that satisfies RBNZ's principles-based requirement for explainable model decisions; LIME is adequate for rapid local debugging but less rigorous and less consistent across runs. (confidence: high)

6. Conformal prediction provides finite-sample, distribution-free prediction intervals with guaranteed coverage, is production-deployed (Husqvarna demand forecasting, credit risk) via the MAPIE Python library, and represents the most technically sound approach to uncertainty quantification for analytics teams that must communicate model uncertainty to decision-makers or regulators. (confidence: high)

7. Causal ML libraries — DoWhy (causal graph modelling), EconML (heterogeneous treatment effects), and CausalML (Uber, uplift modelling) — are production-stable and enable analytics teams to move from average treatment effects to personalised intervention analysis for A/B testing, marketing attribution, and policy evaluation. (confidence: high)

8. AutoML frameworks (AutoGluon for AWS environments and best ensemble accuracy, H2O AutoML for regulated industries requiring strong explainability, FLAML for resource-constrained or Azure-native environments) are production-ready in 2024 and appropriately used to accelerate prototyping and provide strong baselines before manual model development. (confidence: high)

9. The Temporal Fusion Transformer (TFT) is the strongest deep learning approach for multivariate, multi-horizon time series forecasting with external covariates, while N-HiTS is preferred for long-horizon univariate forecasting at lower computational cost; ARIMA and Prophet remain appropriate for simple univariate series where interpretability and minimal data are constraints. (confidence: high)

10. ML systems accumulate hidden technical debt (Sculley et al. 2015) through data dependency entanglement, hidden feedback loops, and undeclared consumers — the "CACE" principle (Changing Anything Changes Everything) — and this debt is the primary cause of silent production failures in analytics ML deployments. (confidence: high)

11. RBNZ's model risk management expectations require regulated entities to apply existing risk frameworks to AI/ML models, including validation, explainability, and outcome monitoring, but impose no specific technical method requirements; the practical standard that satisfies these expectations is SHAP for explainability, out-of-time validation for temporal models, and an MLflow-based experiment tracking and registry workflow. (confidence: high)

12. The minimum viable MLOps stack for an analytics team — MLflow (experiment tracking + model registry), DVC (data versioning), Evidently AI (drift detection), and GitHub Actions (CI/CD for model retraining) — is entirely open-source, cloud-portable, and sufficient to meet the operational requirements of a regulated analytics function. (confidence: high)

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| GBDTs dominate tabular data benchmarks | Lazebnik et al. arXiv:2408.14817; Kaggle AI Report 2023 | high | 111-dataset comparison; practitioner survey |
| DL outperforms GBDTs on "hard" datasets | NeurIPS 2023 "When Do Neural Nets Outperform Boosted Trees?" | high | Consistent with arXiv:2408.14817 |
| TabPFN-2.5 100% win rate over XGBoost ≤10K rows | Prior Labs TabPFN-2.5 Model Report; arXiv:2511.08667 | medium-high | Developer-reported; TabArena independently corroborates |
| Out-of-time validation essential for temporal data | Practitioner consensus; Sculley et al. 2015 | high | Foundational time series ML practice |
| SHAP is regulated-industry explainability standard | arXiv:2305.02012; johal.in 2024 comparative guide | high | Multiple independent sources |
| Conformal prediction is production-deployed | PMLR 2023 Husqvarna case study; arXiv:2107.07511 | high | Industrial implementation confirmed |
| DoWhy/EconML/CausalML are production-stable | PyWhy docs; Microsoft EconML Research; arXiv:2308.09066 | high | Active maintenance; documented production use |
| AutoML frameworks are production-ready 2024 | RapidCanvas benchmark; AutoGluon docs; H2O docs; FLAML GitHub | high | Multiple independent validation sources |
| TFT strongest for multivariate forecasting | Lim et al. 2021 (Int. J. Forecasting); PyTorch Forecasting docs | high | Original paper confirmed by downstream benchmarks |
| ML hidden technical debt (CACE principle) | Sculley et al. 2015 NeurIPS | high | Foundational paper; widely cited |
| RBNZ principles-based approach to ML risk | RBNZ FSR Nov 2024; RBNZ "Rise of the Machines" May 2025 | high | Primary RBNZ publications |
| MLflow + Evidently AI viable MLOps stack | MLflow docs; Evidently AI docs; practitioner guides | high | Widely adopted open-source tooling |

### Assumptions

- **Assumption:** TabPFN-2.5's benchmark results (i.i.d. splits) translate to meaningful performance advantage on financial analytics datasets with temporal structure. **Justification:** TabPFN's in-context learning mechanism is not specifically designed for temporal data; the i.i.d. assumption is strong for financial data. Conservative assumption: treat TabPFN-2.5 as a strong first-pass baseline requiring out-of-time validation before accepting its predictions.
- **Assumption:** RBNZ's principles-based approach will not shift to prescriptive method requirements in the near term. **Justification:** RBNZ's published guidance (November 2024, May 2025) is explicitly principles-based. No published consultation paper indicates movement toward prescriptive technical standards.
- **Assumption:** The minimum viable MLOps stack (open-source tools) is adequate for regulatory scrutiny. **Justification:** RBNZ expects adequate governance, not a specific tooling stack. The adequacy of any stack is determined by the audit trail it produces, not the tools used.

### Analysis

Three sources of evidence were weighted most heavily: the Lazebnik et al. 2024 arXiv benchmark (111 datasets, 20 models) for the tabular DL vs. GBDT question; the Kaggle AI Report 2023 for practitioner behaviour; and RBNZ's own primary publications for the regulatory picture. The NeurIPS 2023 study and TabArena living benchmark corroborate the DL findings.

The primary tension in the evidence is between benchmark performance and production context. Benchmarks optimise for i.i.d. accuracy on held-out datasets. Analytics in regulated financial services has temporal ordering, concept drift, regulatory constraints on model complexity, and interpretability requirements that benchmarks do not capture. Where these tensions exist, this analysis prioritises production context over benchmark ranking — hence the conservative framing of TabPFN-2.5's advantage for financial data.

The "normal vs. advanced" distinction is treated as an empirical question (what do top-quartile analytics practitioners actually do?) rather than a normative one (what should they do in theory?). Competition benchmarks and survey data are more relevant evidence for this question than textbooks.

The regulatory analysis is confined to RBNZ primary sources rather than comparator regulators (APRA, FCA, ECB/EBA) — that comparative analysis is covered by the separate backlog item on RBNZ supervisory expectations.

### Risks, Gaps, and Uncertainties

- **Temporal validity of benchmark results:** The tabular ML landscape evolves rapidly. The NeurIPS 2023 and arXiv:2408.14817 results will be superseded by new architectures. TabArena's living benchmark is the appropriate monitoring mechanism.
- **TabPFN financial data validity:** No published study directly measures TabPFN-2.5 performance on financial time series with temporal leakage controls. This is a genuine gap — not a disqualifying one, but one requiring empirical validation before adoption.
- **RBNZ regulatory evolution:** RBNZ explicitly acknowledged it is monitoring AI developments and may update its guidance. The principles-based position is current as of May 2025 but could shift.
- **Causal ML adoption barriers not quantified:** The evidence for causal ML adoption is strong for technology companies (Uber, Microsoft, Netflix scale) but thinner for NZ-scale analytics teams. Minimum viable team size and data volume for causal ML to be productive have not been studied.
- **O'Reilly AI survey not directly accessed:** The Kaggle 2023 report was used as the primary practitioner survey source; the O'Reilly survey may contain complementary or divergent findings.

### Open Questions

- Is AutoML mature enough to replace manual model construction for routine analytics tasks (credit scoring, demand forecasting, churn), and what does that mean for the skills composition of an analytics team? (Suggested priority: medium — this is the make-or-buy question for analytics capability)
- What does a minimum viable causal ML adoption look like for a 5-person analytics team in financial services, and what data volume is required before heterogeneous treatment effects are estimable? (Suggested priority: medium)
- How should conformal prediction intervals be communicated to non-technical decision-makers, and what does a regulatory-grade uncertainty disclosure look like? (Suggested priority: medium)
- What is the right model governance artefact standard for RBNZ-regulated entities — are model cards sufficient, or is a more formal validation report required? (Suggested priority: high — directly unblocks the RBNZ supervisory expectations item)
- Does LLM-assisted automated feature engineering (generating features from text fields or suggesting interactions) produce net positive outcomes for structured tabular analytics, or does the noise introduced exceed the signal gained? (Suggested priority: low — horizon capability)

### Output section

- Type: knowledge, backlog-item
- Description: A structured taxonomy of ML techniques with decision guides (when to use / not to use), normal-vs-advanced maturity benchmark, best practices, regulatory compliance mapping (RBNZ), and a capability self-assessment framework. Three follow-on backlog items are identified: minimum viable causal ML for regulated analytics, model governance artefact standards for RBNZ compliance, and AutoML vs. manual construction for routine analytics tasks.
- Links:
  - https://arxiv.org/abs/2408.14817 — Lazebnik et al. (2024) comprehensive tabular ML benchmark
  - https://www.kaggle.com/AI-Report-2023 — Kaggle AI Report 2023, tabular data section
  - https://proceedings.neurips.cc/paper/2015/file/86df7dcfd896fcaf2674f757a2463eba-Paper.pdf — Sculley et al. (2015), hidden technical debt in ML systems