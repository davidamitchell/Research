---
title: "ML techniques, algorithms, and advanced analytics — a systematic reference for analytics teams"
added: 2026-03-03
status: backlog
priority: high
tags: [machine-learning, analytics, algorithms, statistics, deep-learning, advanced-analytics, best-practices, model-selection]
started: ~
completed: ~
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

- [ ] Kaggle — "State of Data Science and Machine Learning" annual survey: https://www.kaggle.com/kaggle-survey
- [ ] Papers with Code — ML benchmarks and leaderboards: https://paperswithcode.com
- [ ] Hastie, Tibshirani & Friedman — *The Elements of Statistical Learning* (2nd ed.): https://web.stanford.edu/~hastie/ElemStatLearn/
- [ ] Bishop — *Pattern Recognition and Machine Learning* (Microsoft Research, 2006)
- [ ] Geron — *Hands-On Machine Learning with Scikit-Learn, Keras & TensorFlow* (3rd ed., O'Reilly, 2022)
- [ ] Chen & Guestrin — XGBoost paper (2016): https://arxiv.org/abs/1603.02754
- [ ] Ke et al. — LightGBM paper (2017): https://papers.nips.cc/paper/2017/hash/6449f44a102fde848669bdd9eb6b76fa-Abstract.html
- [ ] Prokhorenkova et al. — CatBoost paper (2018): https://arxiv.org/abs/1706.09516
- [ ] Lundberg & Lee — SHAP paper (2017): https://arxiv.org/abs/1705.07874
- [ ] Ribeiro et al. — LIME paper (2016): https://arxiv.org/abs/1602.04938
- [ ] Hollmann et al. — TabPFN (2022): https://arxiv.org/abs/2207.01848
- [ ] Lim et al. — Temporal Fusion Transformer (2021): https://arxiv.org/abs/1912.09363
- [ ] Oreshkin et al. — N-BEATS (2020): https://arxiv.org/abs/1905.10437
- [ ] Peters et al. — DoWhy causal ML: https://github.com/py-why/dowhy
- [ ] Microsoft — EconML causal ML: https://econml.azurewebsites.net
- [ ] Angelopoulos & Bates — Conformal prediction tutorial: https://arxiv.org/abs/2107.07511
- [ ] Google — Rules of Machine Learning best practices: https://developers.google.com/machine-learning/guides/rules-of-ml
- [ ] O'Reilly AI & ML survey (2023–2024)
- [ ] MLflow documentation — experiment tracking and model registry: https://mlflow.org/docs/latest/index.html
- [ ] Sculley et al. — "Hidden Technical Debt in Machine Learning Systems" (NIPS 2015): https://proceedings.neurips.cc/paper/2015/file/86df7dcfd896fcaf2674f757a2463eba-Paper.pdf
- [ ] RBNZ — Model risk management guidance (BS11 / related guidance): https://www.rbnz.govt.nz
- [ ] Mitchell et al. — Model Cards for Model Reporting: https://arxiv.org/abs/1810.03993
- [ ] `Research/backlog/2026-03-02-ai-not-a-data-problem.md` — organisational context for analytics/AI separation
- [ ] `Research/backlog/2026-02-28-ai-strategy-security-focus.md` — regulatory framing

---

## Findings

*(Fill in when completing. Follow the research skill synthesis structure.)*

### Executive Summary

3–5 sentences. What is the answer to the research question? State the key conclusion directly.

### Key Findings

Ordered list. Each finding is a specific, evidence-backed claim.

1.
2.

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| | | high / medium / low | |

### Assumptions

Explicit assumptions made during the investigation and the justification for each.

- **Assumption:** ... **Justification:** ...

### Analysis

How the evidence was weighed, what trade-offs were identified, and how competing interpretations were resolved.

### Risks, Gaps, and Uncertainties

What is still unknown? Where does the evidence fall short? What could change the conclusion?

-

### Open Questions

Questions that surfaced during research but are out of scope for this item. Each may become a new backlog item.

- How should an analytics team prioritise capability investment when the technique landscape is evolving rapidly (foundation models vs. classical ML)?
- What does a regulated-industry model governance framework look like in practice, and what artefacts does it require?
- Is AutoML (H2O, AutoGluon, FLAML) mature enough to replace manual model construction for routine analytics tasks?
- What are the organisational and skills implications of adopting causal ML, and what is the minimum viable causality literacy for an analytics team?
- How should uncertainty quantification (Bayesian methods, conformal prediction) be communicated to non-technical stakeholders and decision-makers?

---

## Output

- Type: knowledge, backlog-item
- Description: A structured reference taxonomy of ML techniques with decision guides (when to use / not to use), best practices, capability maturity benchmarks, and a self-assessment framework for analytics teams; may spawn follow-on items on causal ML, MLOps implementation, or probabilistic modelling practices
- Links:
  - `Research/backlog/2026-03-02-ai-not-a-data-problem.md`
  - `Research/backlog/2026-02-28-ai-strategy-security-focus.md`
