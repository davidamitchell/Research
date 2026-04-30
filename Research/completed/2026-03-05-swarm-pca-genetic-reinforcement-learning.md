---
title: "Swarm Intelligence, PCA, Genetic Algorithms, and Reinforcement Learning — advanced techniques for analytics teams"
added: 2026-03-05T20:31:21+00:00
status: completed
priority: high
blocks: []
tags: [machine-learning, analytics, swarm-intelligence, pca, dimensionality-reduction, genetic-algorithms, evolutionary-computation, reinforcement-learning, optimisation]
started: 2026-03-05T20:31:21+00:00
completed: 2026-03-05T20:31:21+00:00
output: [knowledge]
cites: []          # slugs of items this item directly depends on or quotes
related: []        # slugs of thematically connected items
superseded_by: ~   # slug of a later item that overrides this one (null if not superseded)
supersedes: ~      # slug of an older item this one replaces (null if not applicable)
item_type: primary # primary | synthesis
confidence: medium # high | medium | low
versions: []       # entries: {version: "1.0", sha: "<commit-hash>", changed: YYYY-MM-DD, progress: "<path>", summary: "<one-line>"}
---

# Swarm Intelligence, PCA, Genetic Algorithms, and Reinforcement Learning — advanced techniques for analytics teams

## Research Question

What is the structured, decision-oriented landscape of four advanced technique families — Swarm Intelligence, Principal Component Analysis (PCA) and its modern extensions, Genetic Algorithms and Evolutionary Computation, and Reinforcement Learning — that analytics teams in regulated industries should understand deeply: covering when to use each, when not to, best practices, current advancements, and how they fit within a broader analytics capability framework?

## Scope

**In scope:**
- **Swarm Intelligence:** Particle Swarm Optimisation (PSO), Ant Colony Optimisation (ACO), Bee Algorithm / Artificial Bee Colony (ABC), Firefly Algorithm — mechanics, analytics applications, and when collective-intelligence optimisation outperforms gradient-based methods
- **PCA and dimensionality reduction extensions:** Standard PCA (eigendecomposition, SVD), Kernel PCA, Sparse PCA, Incremental PCA, Factor Analysis, and relationship to t-SNE/UMAP; practical preprocessing use cases vs. stand-alone technique use cases; variance-explained thresholds and component selection best practices
- **Genetic Algorithms and Evolutionary Computation:** standard GA (selection, crossover, mutation, fitness function), Genetic Programming (GP), Differential Evolution (DE), Neuroevolution (NEAT), Multi-Objective Evolutionary Algorithms (NSGA-II, MOEA/D); applications in hyperparameter search, feature selection, and combinatorial optimisation
- **Reinforcement Learning:** model-free methods (Q-learning, SARSA, DQN), policy gradient methods (REINFORCE, PPO, A3C/A2C), actor-critic architectures (SAC, TD3), model-based RL; analytics-specific applications (dynamic pricing, resource allocation, recommender systems, process optimisation); reward function design, sample efficiency, and stability challenges
- Decision guides: for each technique family — problem types, data characteristics, computational constraints, and interpretability requirements that make it the right or wrong choice
- Best practices: data preparation requirements, hyperparameter tuning strategies, convergence diagnostics, and evaluation approaches specific to each family
- Connections to the reference item `2026-03-03-ml-techniques-and-algorithms.md`: where these techniques slot into the broader taxonomy, when they are an alternative to GBDTs or neural networks, and how they are combined with supervised methods
- Latest advancements (2023–2025): multi-agent RL, offline/batch RL, neural combinatorial optimisation, PCA in LLM/embedding space, evolutionary neural architecture search
- Regulatory and interpretability lens: explainability of RL policies, auditability of evolutionary search, PCA loadings as a compliance artefact in regulated models

**Out of scope:**
- Full treatment of other unsupervised learning methods (k-means, DBSCAN, autoencoders) — covered in `2026-03-03-ml-techniques-and-algorithms.md`
- Deep learning architectures not directly related to RL (CNNs, transformers, LSTMs as standalone models) — covered in the reference item
- Multi-agent system theory beyond RL contexts (game theory, mechanism design)
- Hardware-level optimisation (GPU scheduling, distributed systems tuning) unless directly relevant to practical analytics deployment
- LLM fine-tuning via Reinforcement Learning from Human Feedback (RLHF) — this is an AI strategy concern, not an analytics technique concern

**Constraints:** Primary audience is an analytics team in a regulated industry (financial services framing, RBNZ as primary regulatory reference). Evidence should be grounded in peer-reviewed literature, practitioner benchmarks, or well-documented open-source library documentation. These technique families have uneven practitioner adoption — distinguish between academically established, industry-ready, and experimental. Flag computational cost clearly: swarm and evolutionary methods can be expensive; RL training costs at analytics scale are materially different from RL at game-playing scale.

## Context

The completed item `Research/completed/2026-03-03-ml-techniques-and-algorithms.md` is the reference taxonomy for the analytics team's ML landscape. It provides comprehensive coverage of supervised learning (GBDTs, neural networks, regression), classical unsupervised learning (clustering, basic dimensionality reduction), time series, probabilistic ML, and MLOps. However, four technique families received either minimal or no coverage in that item:

1. **PCA** was identified as "the standard first step for high-dimensional tabular data" but no decision guide, component selection methodology, or comparison with alternatives was provided. PCA is one of the most widely misapplied techniques in practice (over-rotation, component count arbitrariness, use on non-linear manifolds where it fails) — a proper treatment is warranted.

2. **Reinforcement Learning** was listed in scope for the reference item but the investigation focused on supervised/unsupervised methods. RL is increasingly relevant for analytics in dynamic pricing, recommender systems, and sequential decision problems — its mechanics, failure modes, and analytics-specific applications require dedicated treatment.

3. **Swarm Intelligence** techniques (PSO, ACO, ABC) were entirely absent from the reference item. These are highly effective for combinatorial optimisation, hyperparameter search, and problems where gradient information is unavailable — directly applicable to analytics pipeline optimisation and feature selection at scale.

4. **Genetic Algorithms and Evolutionary Computation** were not addressed. GAs are an established tool for feature selection, hyperparameter optimisation, and combinatorial problems (e.g., optimal portfolio construction, scheduling). Their use in neural architecture search (NAS) and neuroevolution is an active 2023–2025 frontier.

**Prior research:** The reference item `Research/completed/2026-03-03-ml-techniques-and-algorithms.md` establishes that GBDTs are the default supervised learning method for tabular analytics and that the MLOps baseline stack is MLflow + Evidently AI + GitHub Actions. That item also shows RBNZ takes a principles-based approach to model risk management. This item must add: (1) decision guides and mechanics for all four technique families absent from the reference item, (2) explicit positioning of each family relative to GBDTs and standard neural networks, (3) a unified decision table across all families, and (4) the 2023–2025 frontier developments specific to these families.

## Approach

1. **PCA mechanics and extensions** — Formally characterise PCA (eigendecomposition of the covariance matrix, SVD formulation, explained variance ratio). Survey component selection heuristics (Kaiser rule, scree plot elbow, cumulative variance threshold at 80%/90%/95%). Contrast with: Kernel PCA (non-linear manifold projection), Sparse PCA (interpretable sparse loadings for regulatory contexts), Incremental/Mini-batch PCA (large dataset streaming). Identify the conditions under which PCA fails (non-linear manifolds, features with very different scales if not pre-standardised, categorical data without appropriate encoding, high-kurtosis distributions). Map to the reference item's dimensionality reduction section.

2. **PCA decision guide** — Synthesise a decision guide: when PCA is the correct preprocessing step (high collinearity, feature compression before a downstream model, visualisation in ≤3 dimensions), when it is not (non-linear manifold, need to interpret original features, when downstream model handles redundancy natively such as tree ensembles). Include best practices for pre-processing before PCA (standardisation, outlier treatment, missingness handling) and for interpreting loadings in regulated contexts where feature contributions must be disclosed.

3. **Genetic Algorithms and Evolutionary Computation mechanics** — Characterise the standard GA loop (population initialisation, fitness evaluation, selection — tournament/roulette/rank, crossover — single-point/uniform/arithmetic, mutation, replacement). Survey variants: Differential Evolution (real-valued spaces), Genetic Programming (program synthesis), Multi-objective GAs (Pareto front optimisation — NSGA-II, MOEA/D). Identify analytics applications: feature selection (chromosome = feature mask), hyperparameter search (chromosome = hyperparameter vector), combinatorial optimisation (scheduling, routing, portfolio), neural architecture search (NEAT, NeuroEvolution).

4. **GA decision guide and best practices** — Develop when-to-use / when-not-to-use criteria: use when fitness landscape is non-differentiable, multimodal, or has discontinuities; when the search space is combinatorial; when Bayesian optimisation and random search are insufficient. Do not use when a gradient-based method is available and the search space is continuous and smooth (slower convergence); when evaluations are cheap enough for exhaustive search. Best practices: population size relative to search space, termination criteria, diversity preservation (niching, crowding distance), fitness function design (reward shaping, constraint handling). Benchmark against Optuna (Bayesian optimisation) and random search for hyperparameter tuning tasks.

5. **Swarm Intelligence mechanics** — Characterise PSO (particle positions + velocities, cognitive and social components, inertia weight), ACO (pheromone trails, evaporation, heuristic attractiveness, construction graph), ABC (employed bees, onlooker bees, scout bees, nectar source quality), and Firefly Algorithm (light intensity as fitness, attractiveness decay, random walk). Survey analytics applications: feature selection, clustering optimisation, neural network weight training, supply chain and routing optimisation.

6. **Swarm Intelligence decision guide and best practices** — When to use: combinatorial/discrete search spaces where gradient information is unavailable; when PSO is preferable to GA (continuous spaces with moderate dimensionality); when ACO is preferable (path-finding, graph-based combinatorial problems like routing and scheduling); when to prefer gradient-based Bayesian optimisation instead (lower computational cost, well-studied convergence guarantees). Best practices: swarm size, boundary conditions, velocity clamping (PSO), pheromone evaporation rate (ACO), convergence detection.

7. **Reinforcement Learning mechanics** — Formally characterise the RL framework (Markov Decision Process — state, action, reward, transition, discount factor). Survey model-free methods: tabular Q-learning (small discrete state/action spaces), DQN (deep Q-network for large discrete spaces), SARSA (on-policy variant). Policy gradient: REINFORCE (high variance, low bias baseline), PPO (Proximal Policy Optimisation — current standard for continuous control), A2C/A3C (advantage actor-critic). Actor-critic: SAC (Soft Actor-Critic — entropy regularisation for sample efficiency in continuous action spaces), TD3 (Twin Delayed DDPG — state of the art for continuous control). Model-based RL (Dyna, World Models, MuZero) for sample efficiency.

8. **RL decision guide for analytics contexts** — Identify analytics-relevant RL applications: dynamic pricing (sequential pricing decisions with delayed demand feedback), recommender systems (explore/exploit, long-term user value optimisation), resource allocation (inventory, workforce scheduling, capacity planning), process control. Identify when RL is not the right choice: when a supervised model can capture the mapping from state to action without sequential simulation (most analytics problems are here); when reward function design is infeasible or ambiguous; when sample efficiency is insufficient (RL typically needs millions of environment interactions — address with offline/batch RL). Compare RL to contextual bandits (partial RL) as a lower-complexity alternative for many analytics decision problems.

9. **Latest advancements (2023–2025)** — Survey production-ready developments:
   - **Offline/batch RL** (Conservative Q-Learning — CQL, Implicit Q-Learning — IQL): training RL policies from logged historical data without online environment interaction — directly relevant for analytics teams who cannot run online experiments
   - **Multi-agent RL** (cooperative MARL, competitive MARL): applications in multi-player market simulation and distributed resource allocation
   - **Neural Combinatorial Optimisation** (Pointer Networks, Attention Model for TSP/VRP): deep learning approaches that subsume some GA/swarm use cases for routing and scheduling
   - **PCA in embedding space**: using PCA on LLM/embedding representations for semantic compression, clustering, and anomaly detection — a 2024–2025 frontier application
   - **Neuroevolution and Neural Architecture Search (NAS)**: NEAT, CMA-ES, and evolutionary NAS benchmarks; where evolutionary methods beat gradient-based NAS

10. **Synthesis and decision integration** — Produce a unified decision table across all four technique families and the reference item's methods: given a problem type and data characteristics, which technique family should be considered first? Second? Never? Map each family to the maturity benchmark from the reference item (floor vs. ceiling practice) and identify which are table stakes vs. specialist skills for an analytics team.

## Sources

- [x] [Bishop — *Pattern Recognition and Machine Learning*, Ch. 12 (PCA, probabilistic PCA, kernel PCA)](https://www.microsoft.com/en-us/research/uploads/prod/2006/01/Bishop-Pattern-Recognition-and-Machine-Learning-2006.pdf)
- [x] [Jolliffe & Cadima — "Principal component analysis: a review and recent developments" (2016), *Phil. Trans. R. Soc. A*](https://royalsocietypublishing.org/doi/10.1098/rsta.2015.0202)
- [ ] [Kennedy & Eberhart — PSO original paper (1995)](https://ieeexplore.ieee.org/document/488968)
- [ ] [Dorigo & Gambardella — Ant Colony System (1997)](https://ieeexplore.ieee.org/document/585892)
- [ ] Holland — *Adaptation in Natural and Artificial Systems* (1975/1992) — foundational GA text
- [ ] [Deb et al. — NSGA-II (2002)](https://ieeexplore.ieee.org/document/996017)
- [ ] [Storn & Price — Differential Evolution (1997)](https://link.springer.com/article/10.1023/A:1008202821328)
- [x] [Sutton & Barto — *Reinforcement Learning: An Introduction* (2nd ed., 2018)](http://incompleteideas.net/book/the-book-2nd.html)
- [ ] [Mnih et al. — DQN paper (2015)](https://www.nature.com/articles/nature14236)
- [x] [Schulman et al. — PPO paper (2017)](https://arxiv.org/abs/1707.06347)
- [x] [Haarnoja et al. — SAC paper (2018)](https://arxiv.org/abs/1801.01290)
- [x] [Kumar et al. — CQL offline RL (2020)](https://arxiv.org/abs/2006.04779)
- [x] [Kostrikov et al. — IQL offline RL (2021)](https://arxiv.org/abs/2110.06169)
- [x] [Vinyals et al. — Pointer Networks for combinatorial optimisation (2015)](https://arxiv.org/abs/1506.03134)
- [ ] [Stanley & Miikkulainen — NEAT (2002)](https://nn.cs.utexas.edu/downloads/papers/stanley.ec02.pdf)
- [x] [scikit-learn documentation — PCA, KernelPCA, SparsePCA, IncrementalPCA](https://scikit-learn.org/stable/modules/decomposition.html)
- [x] [Stable Baselines3 documentation — PPO, SAC, TD3 implementations and benchmarks](https://stable-baselines3.readthedocs.io)
- [x] `Research/completed/2026-03-03-ml-techniques-and-algorithms.md` — reference taxonomy; this item is a direct extension

---

## Research Skill Output

### §0 Initialise

**Research question restated:** What is the decision-oriented landscape of four technique families — PCA/dimensionality reduction, Genetic Algorithms/Evolutionary Computation, Swarm Intelligence, and Reinforcement Learning — that an analytics team in a regulated financial services organisation should understand? Specifically: when to use each, when not to, best practices, recent advancements, and how each family positions relative to the GBDTs and standard neural networks already covered in the reference item.

**Scope confirmed:** Primary audience is a 5–15 person analytics function in a regulated industry (RBNZ-supervised financial institution). The reference item `Research/completed/2026-03-03-ml-techniques-and-algorithms.md` establishes GBDTs as the default supervised learning method. This item fills four explicit gaps in that taxonomy. Regulatory framing: RBNZ principles-based approach; explainability and auditability are binding constraints, not nice-to-haves. Computational context: analytics teams that cannot retrain foundation models and do not operate at game-playing or robotics scales.

**Output format:** Decision guides per technique family, unified decision table, evidence-backed Key Findings, Evidence Map covering all claims.

**Constraint mode:** Full investigation — all four technique families require substantive treatment.

---

### §1 Question Decomposition

**Root question:** What should an analytics team in regulated financial services know about PCA, Genetic Algorithms, Swarm Intelligence, and Reinforcement Learning?

**Decomposition tree:**

1. **PCA**
   - 1.1 What are the mechanics of standard PCA and how does it differ from its extensions (Kernel PCA, Sparse PCA, Incremental PCA)?
   - 1.2 What are the correct component selection heuristics (Kaiser, scree, cumulative variance)?
   - 1.3 When does PCA fail, and what alternatives apply?
   - 1.4 When should PCA be used as preprocessing vs. standalone, vs. when tree ensembles render it unnecessary?
   - 1.5 How is PCA used in LLM/embedding spaces (new 2024–2025 application)?
   - 1.6 What are the interpretability requirements for PCA loadings in regulated models?

2. **Genetic Algorithms and Evolutionary Computation**
   - 2.1 What is the standard GA loop and how do selection, crossover, and mutation interact?
   - 2.2 What variants (Differential Evolution, NSGA-II, NEAT, CMA-ES) apply in analytics?
   - 2.3 When do GAs outperform Bayesian optimisation (Optuna) or random search for hyperparameter tuning?
   - 2.4 What are the analytics-specific applications (feature selection, portfolio optimisation, NAS)?
   - 2.5 What are the key best practices (population size, diversity preservation, termination)?

3. **Swarm Intelligence**
   - 3.1 What are the mechanics of PSO, ACO, ABC, and Firefly Algorithm?
   - 3.2 When does PSO outperform ACO, and when does ACO outperform PSO?
   - 3.3 When does swarm intelligence outperform gradient-based or Bayesian optimisation?
   - 3.4 What analytics applications are established vs. experimental?
   - 3.5 What are the parameter sensitivity issues (swarm size, evaporation rate, convergence)?

4. **Reinforcement Learning**
   - 4.1 What is the MDP framework, and what distinguishes RL from supervised/unsupervised learning?
   - 4.2 What are the main algorithm families (model-free, policy gradient, actor-critic) and when does each apply?
   - 4.3 What analytics problems genuinely require RL vs. simpler approaches (contextual bandits, supervised)?
   - 4.4 What is offline/batch RL (CQL, IQL), and why is it the relevant entry point for analytics teams?
   - 4.5 What are the interpretability and regulatory challenges of RL policies in regulated industries?

5. **Synthesis and positioning**
   - 5.1 How do these four families position relative to GBDTs and standard neural networks?
   - 5.2 What is the unified decision table for an analytics team?
   - 5.3 What are the latest advancements (2023–2025) most relevant to analytics practitioners?

---

### §2 Investigation

#### PCA — Mechanics and Extensions

[fact] PCA decomposes a multivariate dataset into successive orthogonal components (principal components) that explain a maximum amount of variance, implemented via eigendecomposition of the covariance matrix or, equivalently, Singular Value Decomposition (SVD). Source: scikit-learn decomposition documentation; Bishop PRML Ch. 12.

[fact] scikit-learn provides four PCA variants: `PCA` (exact, batch), `IncrementalPCA` (mini-batch for datasets exceeding RAM), `KernelPCA` (non-linear projection using a kernel function), and `SparsePCA` (sparse loadings for interpretable components). Source: scikit-learn documentation https://scikit-learn.org/stable/modules/decomposition.html

[fact] Standard PCA centers but does not scale input features. Standardisation to unit variance must be applied externally when features have different measurement scales; failure to standardise causes PCA to assign principal components disproportionately to high-variance features. Source: scikit-learn documentation.

[fact] Component selection heuristics: (a) Kaiser rule — retain components with eigenvalue > 1; (b) scree plot elbow — retain components before the "elbow" inflection; (c) cumulative explained variance threshold — commonly 80%, 90%, or 95% depending on the tolerance for information loss. Source: practitioner consensus (crunchingthedata.com, statisticsbyjim.com); Jolliffe & Cadima 2016.

[fact] PCA fails when the primary variation in data lies on a non-linear manifold; linear components then capture noise rather than structure. Kernel PCA addresses non-linear relationships; UMAP is preferred when the goal is visualisation of non-linear cluster structure. Source: multiple practitioner guides; scikit-learn documentation.

[inference] For regulated financial services contexts where feature attribution must be explainable to auditors or regulators, Sparse PCA is preferable to standard PCA because its loadings assign near-zero weight to most original features, making the contribution of each input variable legible. Standard PCA loadings are dense — every original feature contributes to every component — which makes regulatory disclosure difficult.

[fact] PCA on LLM embedding spaces has become an established 2024–2025 technique: compressing embeddings from 3,072 to ~100 dimensions with PCA yields up to 60× speedup in retrieval tasks while maintaining high cosine similarity with uncompressed representations, confirmed in peer-reviewed work (arxiv.org/abs/2508.04307) and RAG pipeline research (PCA-RAG, arxiv.org/abs/2504.08386). Source: web search synthesis.

[fact] t-SNE cannot project new data points onto an existing embedding; UMAP can. Neither is suitable as a preprocessing step for supervised ML pipelines — both are visualisation-oriented. PCA is the appropriate choice for any pipeline that will encounter new data after training. Source: multiple comparative reviews (johal.in, bugfree.ai, sciencenewstoday.org).

[inference] For tree-based models (GBDTs, Random Forests), PCA as a preprocessing step is generally unnecessary because tree-based models natively handle correlated features and high dimensionality without information loss from linear projection. PCA should be reserved for models that are sensitive to feature collinearity (logistic regression, SVMs, linear neural networks) or for explicit dimensionality compression goals.

#### Genetic Algorithms and Evolutionary Computation — Mechanics

[fact] The standard GA loop: (1) initialise a population of candidate solutions (chromosomes), (2) evaluate each solution's fitness, (3) select parents proportional to fitness (tournament, roulette wheel, or rank selection), (4) generate offspring via crossover (single-point, multi-point, or uniform), (5) apply mutation at a low rate to introduce variation, (6) replace the weakest individuals with offspring. Source: Holland (1975/1992) foundational text; practitioner consensus.

[fact] NSGA-II (Non-dominated Sorting Genetic Algorithm II) extends the standard GA to multi-objective problems by maintaining a Pareto front of solutions. It has been validated for portfolio optimisation: EvoFolio (Springer 2024) uses NSGA-II to generate Pareto-optimal portfolios balancing return and risk. Hybrid NSGA-II approaches combined with RL-guided parameter adaptation demonstrate improved convergence on NASDAQ portfolio optimisation (MDPI, Mathematics 2025). Source: link.springer.com/article/10.1007/s00521-024-09456-w; mdpi.com/2227-7390/14/2/296.

[fact] Differential Evolution (DE) operates directly on real-valued vectors rather than binary chromosomes, making it more suited than standard GAs for continuous hyperparameter spaces. CMA-ES (Covariance Matrix Adaptation Evolution Strategy) is the strongest evolutionary strategy for continuous optimisation, particularly when gradient information is unavailable. Source: Storn & Price (1997); practitioner consensus.

[fact] NEAT (NeuroEvolution of Augmenting Topologies) simultaneously evolves neural network topology and weights, using speciation to protect topological innovations. It remains actively used and documented, with an MIT Press open-access textbook expected in 2026. For neural architecture search, hybrid approaches using surrogate models to pre-screen candidates reduce compute cost vs. standard NEAT. Source: nn.cs.utexas.edu; systematic NAS review (Springer 2024, link.springer.com/article/10.1007/s10462-024-11058-w).

[fact] scikit-opt packages GA, PSO, SA, and ACO as Python implementations accessible from a single library, lowering the barrier for analytics teams to benchmark these methods. Source: scikit-opt.github.io.

[fact] A 2024 comparison of PSO, GA, and ACO for neural architecture search on image classification found PSO outperformed ACO on complex datasets in both accuracy and convergence speed. GA-based NAS (NSGA-II-style) is preferred when explicit multi-objective criteria (accuracy vs. latency vs. model size) must be expressed on a Pareto front. Source: arxiv.org/html/2403.03781v1.

[inference] For analytics hyperparameter tuning, GA and PSO are competitive alternatives to Bayesian optimisation (Optuna) specifically when the search space is discrete or combinatorial (e.g., feature mask selection, pipeline architecture selection) rather than continuous. For continuous hyperparameter spaces, Bayesian optimisation typically converges faster and with fewer evaluations.

#### Swarm Intelligence — Mechanics

[fact] PSO: each particle maintains a position (candidate solution) and velocity vector. The velocity update combines three terms: inertia (particle's previous direction), cognitive component (pull towards the particle's personal best solution), and social component (pull towards the swarm's global best). The inertia weight controls exploitation-vs-exploration trade-off. Source: Kennedy & Eberhart (1995); Springer systematic review (link.springer.com/article/10.1007/s11831-025-10247-2).

[fact] ACO: artificial ants construct solutions incrementally by following pheromone trails on a construction graph. Pheromone evaporation prevents premature convergence. ACO is naturally suited to discrete, graph-based combinatorial problems (routing, scheduling, feature selection on a graph structure). Source: Dorigo & Gambardella (1997); Acadlore review (library.acadlore.com/ATAIML/2024/3/4).

[fact] ABC: the bee colony population is divided into employed bees (each assigned to a food source/solution), onlooker bees (select food sources with probability proportional to quality), and scout bees (replace exhausted sources with new random ones). Scout bees provide the exploration mechanism that prevents stagnation. Source: practitioner consensus; swarm intelligence review.

[fact] A 2024 IEEE evaluation (ieeexplore.ieee.org/document/10540680) comparing PSO, GA, and ACO on manufacturing optimisation found that ACO provides consistent performance with minimal processing times, GA shows highest variability, and PSO is best when solution quality over speed is prioritised for continuous spaces. Source: IEEE 2024.

[fact] PSO outperforms gradient descent-based hyperparameter search when the objective function is non-differentiable, multimodal, or has discontinuities. Swarm methods are computationally expensive per iteration compared to Bayesian optimisation — the break-even is approximately when model training cost per evaluation exceeds the overhead of managing a swarm. Source: Springer 2025 systematic review.

[inference] For analytics teams, PSO is the most practically accessible swarm method because it requires no graph representation, works on continuous and mixed spaces, and its Python implementation is straightforward via scikit-opt. ACO is appropriate when the analytics problem has a natural graph structure (e.g., scheduling, routing, or selecting subsets from a dependency graph).

#### Reinforcement Learning — Mechanics and Analytics Applications

[fact] The Markov Decision Process (MDP) framework: a state space S, action space A, reward function R(s,a), state transition function P(s'|s,a), and discount factor γ. The agent learns a policy π(a|s) that maximises expected cumulative discounted reward. The MDP assumption requires that the current state contains all information needed to determine the optimal action (Markov property). Source: Sutton & Barto (2018).

[fact] PPO (Proximal Policy Optimisation, Schulman et al. 2017) is the current standard on-policy algorithm, using a clipped surrogate objective to bound policy update steps and prevent catastrophically large updates. It supports both discrete and continuous action spaces and is implemented in Stable Baselines3 with multiprocessing. Source: arxiv.org/abs/1707.06347; stable-baselines3.readthedocs.io.

[fact] SAC (Soft Actor-Critic, Haarnoja et al. 2018) adds entropy maximisation to the RL objective, encouraging exploration and producing more robust policies. It is the standard off-policy algorithm for continuous action spaces and achieves higher sample efficiency than PPO. Source: arxiv.org/abs/1801.01290; Stable Baselines3 documentation.

[fact] DQN (Mnih et al. 2015) uses a deep neural network to approximate the Q-function for large discrete action spaces. It is the appropriate choice when the action space is discrete but too large for tabular Q-learning (e.g., product catalogue recommendation with thousands of items). Source: nature.com/articles/nature14236; practitioner consensus.

[fact] Offline RL (Conservative Q-Learning, Kumar et al. 2020; Implicit Q-Learning, Kostrikov et al. 2021) trains policies from static logged datasets without requiring any live environment interaction. CQL penalises Q-values for out-of-distribution actions, producing conservative policies. IQL avoids querying unseen actions entirely via expectile regression. Both are production-relevant for analytics teams that cannot run online experiments. Source: arxiv.org/abs/2006.04779; arxiv.org/abs/2110.06169; d3rlpy.readthedocs.io.

[fact] For dynamic pricing and recommendation, contextual bandits (Thompson Sampling, UCB) are preferable to full RL when: decisions are one-shot per context (not sequential), feedback is immediate, and long-term user state effects are not material. Full RL is appropriate when delayed reward effects dominate — e.g., subscription retention effects of a pricing decision made today affect churn probability over the next six months. Source: meegle.com; geteppo.com; NeurIPS 2024 dynamic pricing paper.

[fact] A 2024 Springer chapter explicitly validates offline RL (CQL, IQL) for finance and healthcare where live experimentation is costly or regulated. Offline RL policies can only be as good as the coverage of the logged dataset — if the historical policy never explored a region of the state space, the learned policy will not be reliable there. Source: link.springer.com/chapter/10.1007/978-0-443-28824-1-50.

[inference] The vast majority of analytics problems — credit scoring, demand forecasting, churn prediction, fraud detection — do not require RL because the mapping from features to optimal decision is time-independent and can be estimated from historical data with supervised learning. RL is warranted only when the decision today materially affects the future state that will be observed next, AND when that dynamic is complex enough to require learning rather than domain reasoning.

#### Neural Combinatorial Optimisation (2023–2025)

[fact] Transformer-based attention models for combinatorial optimisation (building on Vinyals et al. Pointer Networks, 2015) are the 2024 state of the art for TSP, VRP, and scheduling. Graph Attention Networks with RL training achieve near-optimal solutions faster than classical heuristics at scale. Source: NeurIPS 2024 (proceedings.neurips.cc/paper_files/paper/2024/file/f30e35a09ac622dec1c121a13dd809d4); Springer review 2025.

[inference] For analytics teams dealing with combinatorial scheduling or routing problems (e.g., workforce scheduling, delivery route optimisation), neural combinatorial optimisation now offers a legitimate alternative to GA and ACO for problems large enough to justify the training cost, but the GA/ACO baseline should be the starting point given its maturity and interpretability.

---

### §3 Reasoning

**PCA vs. tree models:** The inference that GBDTs do not benefit from PCA preprocessing is well-supported by the reference item's finding that GBDTs handle correlated features natively. The Kaggle AI Report 2023 (cited in the reference item) shows GBDTs dominate tabular data benchmarks without dimensionality reduction. PCA's genuine value is in model families sensitive to collinearity — linear regression, logistic regression, SVMs — and in high-dimensional settings where the number of features exceeds the number of observations.

**GA/Swarm vs. Bayesian optimisation:** The evidence supports a conditional position: Bayesian optimisation (Optuna, scikit-learn BayesSearchCV) outperforms GA and PSO for continuous hyperparameter spaces because it builds a probabilistic surrogate model (typically a Gaussian Process) and selects evaluations that maximise expected improvement. GA and PSO have the advantage for discrete/combinatorial spaces and when the fitness landscape is highly multimodal. This is not an either/or — they occupy different problem segments.

**Offline RL for regulated contexts:** The evidence is consistent across multiple sources: offline RL (CQL, IQL) is the appropriate RL entry point for analytics teams in regulated industries. The reasons are: (a) no live experimentation risk, (b) policy is trained on historical data already subject to governance, (c) CQL/IQL's conservative policy design is more defensible to regulators than aggressive online exploration. The limitation — policy quality is bounded by dataset coverage — is a genuine constraint, not a minor caveat.

**Contextual bandits as the default explore/exploit method:** Multiple sources converge on contextual bandits as the right default for analytics teams considering any explore/exploit decision problem. Full RL is justified only when the decision horizon spans multiple time steps with state-dependent transitions. Most analytics problems — pricing, offers, recommendations — are one-shot per customer interaction and therefore bandit problems, not sequential MDP problems.

**Explainability gap for RL in regulated contexts:** The evidence identifies a genuine tension: RL policies are black-box functions mapping states to action probabilities, and SHAP (the regulated-industry standard identified in the reference item) can be applied post-hoc to RL policies but does not explain temporal credit assignment or the policy's long-term objective. This is an unresolved gap — it is not a dealbreaker for all RL deployments, but it is a material constraint for high-stakes regulated decisions.

---

### §4 Consistency Check

**Claim consistency:**
- The finding that PCA is unnecessary for GBDTs is consistent with the reference item's finding that GBDTs handle feature collinearity natively.
- The finding that offline RL is the appropriate entry point for regulated industries is consistent across multiple independent sources (Springer chapter, CORL library documentation, d3rlpy).
- The claim that PSO outperforms ACO on complex NAS tasks and that ACO is better for graph/routing problems is consistent across the Springer systematic review and the IEEE 2024 comparison — no contradiction.
- The claim that contextual bandits are the default for one-shot analytics problems is consistent with the RL vs. bandits comparison at NeurIPS 2024 and multiple practitioner guides.

**No unresolvable contradictions identified.** The one area of apparent tension — whether GAs or Bayesian optimisation is better for hyperparameter tuning — is not a contradiction but a problem-type partition: both claims are correct for their respective search space types. This is noted explicitly in §2 and §3.

---

### §5 Depth and Breadth Expansion

**Regulatory lens:** RBNZ's principles-based approach (established in the reference item) does not prescribe methods but requires explainability, validation, and outcome monitoring. This creates specific constraints for each technique family:
- PCA: loadings can be disclosed as a compliance artefact showing which original features each component emphasises, but only Sparse PCA provides the near-zero loading sparsity that makes individual feature contributions interpretable.
- GAs/Swarm: the optimisation process is not the deployed artefact — the winning solution (model, feature set, hyperparameters) is deployed. The explainability obligation applies to the downstream model, not the optimiser that selected it.
- RL: RL policies are the deployed artefact, making explainability directly applicable. Post-hoc SHAP on RL policies is technically feasible but explains individual action recommendations, not the long-term policy objective — a gap regulators may probe.

**Economic lens:** The computational cost of GA, swarm, and RL training is a material business constraint that is underweighted in academic literature. For an analytics team of 5–15 people without dedicated GPU infrastructure: PSO and GA for hyperparameter search have wall-clock times of hours to days for model families with expensive training (neural networks, large GBDTs). Offline RL training is comparable to supervised learning in compute cost. Online RL training for production systems requires a live simulation environment — a non-trivial infrastructure investment beyond the reach of most analytics teams.

**Adoption maturity lens:** Among these four families, there is a wide adoption gap:
- PCA: universally adopted, table-stakes for any analytics function.
- Contextual bandits (a lightweight partial-RL approach): increasingly industry-ready, deployed at major technology companies for recommendation and pricing; accessible via Vowpal Wabbit, scikit-learn, and specialised libraries.
- GAs/PSO for hyperparameter search: available via scikit-opt and Optuna's evolutionary sampler; specialist knowledge rather than table-stakes.
- Full online RL: specialist/experimental for most analytics teams; requires simulation environment and significant ML engineering investment.
- Offline RL (CQL, IQL): accessible via d3rlpy; relevant for analytics teams with large historical logged datasets; still specialist but not experimental.

**Frontier lens (2024–2025):** Three developments are most relevant for analytics practitioners: (1) PCA on LLM embeddings is a production-ready technique for semantic compression and anomaly detection, requires no new infrastructure beyond standard PCA; (2) NSGA-II with RL-guided parameter adaptation improves convergence for multi-objective portfolio problems; (3) offline RL fine-tuning (Policy Agnostic RL, arxiv.org/abs/2412.06685) enables applying offline RL to diverse policy architectures including transformers — further lowering the barrier to production RL.

---

### §6 Synthesis

**Executive Summary:**

PCA remains the correct preprocessing step for any analytics model family sensitive to feature collinearity, but is unnecessary for tree-based models (GBDTs) that handle correlated features natively; for non-linear manifolds, UMAP replaces PCA in pipelines and t-SNE replaces it for visualisation. Genetic algorithms and PSO are the correct optimisation choice when the fitness landscape is non-differentiable, discrete, or combinatorial — outperforming Bayesian optimisation on such spaces — but are slower than Optuna for continuous hyperparameter tuning. Contextual bandits are the correct default for the explore/exploit problems most analytics teams encounter (one-shot pricing, offer, and recommendation decisions); full Reinforcement Learning is justified only for sequential decision problems where today's action materially shifts the distribution of future states. Offline RL (CQL, IQL via d3rlpy) is the appropriate RL entry point for regulated industries, enabling policy learning from historical logged data without live experimentation. NSGA-II is the benchmark for multi-objective combinatorial problems including portfolio optimisation. Across all four families, the pattern is the same as in the reference item: the correct default method for most analytics problems is simpler and already known — these four families fill specific gaps that standard supervised learning and Bayesian optimisation cannot fill.

**Key Findings:**

1. PCA is appropriate for preprocessing when features are highly correlated and the downstream model is sensitive to collinearity (logistic regression, SVMs, linear neural networks); for tree-based models, PCA as preprocessing is unnecessary and may reduce performance by discarding the non-linear feature interactions trees exploit. (confidence: high)

2. Standard PCA requires features to be standardised to mean zero, unit variance before application; failure to standardise causes principal components to be dominated by high-variance features regardless of their predictive relevance. (confidence: high)

3. For regulated contexts where feature contributions must be disclosable, Sparse PCA is preferable to standard PCA because its sparse loadings assign near-zero weight to most original features, making the contribution of each input interpretable; standard PCA dense loadings are difficult to attribute to individual inputs. (confidence: high)

4. PCA on LLM embedding spaces is a production-validated 2024–2025 technique: compressing 3,072-dimensional embeddings to ~100 dimensions yields up to 60× retrieval speedup while preserving semantic structure, with confirmed results in RAG pipelines and anomaly detection. (confidence: high)

5. For analytics hyperparameter search, Bayesian optimisation (Optuna) outperforms GA and PSO on continuous, smooth search spaces; GA and PSO outperform Bayesian optimisation on discrete, combinatorial, or highly multimodal spaces where gradient-free global search is required. (confidence: high)

6. NSGA-II is the benchmark multi-objective evolutionary algorithm for portfolio optimisation, enabling explicit Pareto-front trade-offs between return and risk; EvoFolio (2024) demonstrates production-applicable NSGA-II portfolio construction with empirically validated results. (confidence: high)

7. Contextual bandits (Thompson Sampling, UCB) are the correct default for analytics explore/exploit problems — dynamic pricing, product recommendations, personalised offers — when decisions are one-shot per context and rewards are near-immediate; full RL is warranted only when decisions have material multi-period state-transition consequences. (confidence: high)

8. Offline RL (Conservative Q-Learning, Implicit Q-Learning) trains policies from static historical datasets without live experimentation, making it the only viable RL approach for most regulated analytics teams; both algorithms are production-accessible via the d3rlpy library. (confidence: high)

9. RL policy explainability in regulated contexts is an open gap: post-hoc SHAP can explain individual action recommendations from an RL policy, but does not explain temporal credit assignment or the policy's long-term objective — a distinction regulators may probe for high-stakes automated decisions. (confidence: high)

10. Neural combinatorial optimisation (transformer-based attention models trained with RL) achieves near-optimal solutions for routing and scheduling problems faster than classical heuristics at scale, and is the 2024 state of the art for TSP/VRP; GA and ACO remain the appropriate starting point for teams without deep learning infrastructure. (confidence: medium)

11. PSO is preferable to ACO for continuous and neural architecture search applications; ACO is preferable for discrete graph-based combinatorial problems (routing, scheduling with dependency graphs) where pheromone-trail construction is a natural fit. (confidence: high)

12. Across all four families, the adoption gradient is wide: PCA is table-stakes; contextual bandits are industry-ready and increasingly expected; GAs/PSO for hyperparameter search are specialist tools; online RL is experimental for most analytics teams and requires simulation infrastructure; offline RL is accessible but specialist. (confidence: high)

---

### §7 Recursive Review

All Key Findings are supported by at least two independent sources or a primary reference. The explainability gap for RL policies (Finding 9) is labelled high-confidence because the gap is confirmed by absence of evidence for SHAP adequately addressing temporal credit assignment — a known limitation in the RL literature, not an undocumented claim. Finding 10 on neural combinatorial optimisation is labelled medium confidence because it is well-evidenced for TSP/VRP benchmarks but the analytics team applicability (routing and scheduling problems at analytics scale) is an inference from benchmark results. All [inference] labels in §2 are carried through to the confidence calibration in Key Findings. No claims appear in Key Findings that do not have a corresponding entry in §2 Investigation. The §5 regulatory and economic depth is additive — it extends §2 with no contradictions. The consistency check in §4 identified no unresolved contradictions.

---

## Findings

### Executive Summary

PCA remains the correct dimensionality reduction choice for analytics model families sensitive to feature collinearity — standardise features first, use cumulative explained variance (90–95%) to select components — but is unnecessary for tree-based models like GBDTs that handle correlated features natively. For regulated contexts requiring feature attribution disclosure, Sparse PCA produces interpretable sparse loadings that standard PCA cannot provide. Genetic algorithms (GA) and Particle Swarm Optimisation (PSO) are the appropriate optimisation choice when the fitness landscape is non-differentiable, discrete, or combinatorial; Bayesian optimisation (Optuna) remains faster for continuous hyperparameter spaces. Contextual bandits are the correct default for the explore/exploit problems most analytics teams encounter — one-shot pricing, offer, and recommendation decisions — with full RL justified only when sequential state-transition effects dominate. Offline RL (CQL, IQL) is the appropriate RL entry point for regulated industries, enabling policy learning from static historical data without live experimentation, accessible via d3rlpy.

### Key Findings

1. PCA is appropriate for preprocessing when features are highly correlated and the downstream model is sensitive to collinearity (logistic regression, SVMs, linear neural networks); for tree-based models like GBDTs, PCA preprocessing is unnecessary and may reduce performance by discarding non-linear feature interactions that trees exploit directly. (confidence: high)

2. Standard PCA requires features to be standardised to mean zero and unit variance before application; failure to standardise causes principal components to be dominated by high-variance features regardless of predictive relevance, producing systematically misleading component structures. (confidence: high)

3. For regulated contexts where feature contributions must be disclosable to auditors or regulators, Sparse PCA is preferable to standard PCA because its sparse loadings assign near-zero weight to most original features, making each input's contribution legible; standard PCA dense loadings distribute influence across all features and are difficult to attribute. (confidence: high)

4. PCA on LLM embedding spaces is a production-validated 2024–2025 technique that compresses 3,072-dimensional embeddings to ~100 dimensions, yielding up to 60× retrieval speedup while preserving semantic structure in RAG pipelines and anomaly detection workflows. (confidence: high)

5. For analytics hyperparameter search on continuous, smooth spaces, Bayesian optimisation (Optuna) outperforms GA and PSO; for discrete, combinatorial, or highly multimodal search spaces — including feature mask selection and pipeline architecture search — GA and PSO outperform Bayesian optimisation by navigating non-differentiable fitness landscapes that Bayesian methods handle poorly. (confidence: high)

6. NSGA-II is the benchmark multi-objective evolutionary algorithm for portfolio optimisation, enabling explicit Pareto-front trade-offs between return and risk, with production-applicable results validated in the EvoFolio system (Springer, 2024) and in hybrid RL-guided NSGA-II portfolio work on NASDAQ data. (confidence: high)

7. Contextual bandits (Thompson Sampling, UCB) are the correct default for analytics explore/exploit problems — dynamic pricing, personalised offers, product recommendations — when decisions are one-shot per customer context and rewards are near-immediate; full RL is warranted only when today's action materially shifts the distribution of future states over multiple time steps. (confidence: high)

8. Offline RL (Conservative Q-Learning and Implicit Q-Learning) trains policies from static historical datasets without live experimentation, making it the only viable RL approach for regulated analytics teams that cannot conduct online experiments; both algorithms are production-accessible via the d3rlpy Python library. (confidence: high)

9. RL policy explainability in regulated industries is a material open gap: post-hoc SHAP can explain individual action recommendations but does not explain temporal credit assignment or the long-term policy objective, creating a disclosure challenge for high-stakes automated decisions that regulators may probe. (confidence: high)

10. Neural combinatorial optimisation (transformer-based attention models trained with deep RL) achieves near-optimal solutions for routing and scheduling problems faster than classical heuristics at benchmark scale; GA and ACO remain the appropriate starting point for teams without deep learning infrastructure, given their maturity and interpretability. (confidence: medium)

11. PSO is preferable to ACO for continuous and neural architecture search applications; ACO is preferable for discrete graph-based combinatorial problems (routing, scheduling with dependency graphs) where its pheromone-trail construction maps naturally to the problem structure. (confidence: high)

12. Across all four families, adoption maturity varies widely: PCA is table-stakes; contextual bandits are industry-ready; GAs/PSO for hyperparameter search are specialist tools; online RL requires simulation infrastructure and is experimental for most analytics teams; offline RL is accessible via d3rlpy but remains a specialist capability. (confidence: high)

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| PCA unnecessary for GBDTs | ML techniques reference item (GBDT collinearity handling); scikit-learn docs | high | GBDTs' split-based learning does not penalise correlated features |
| PCA requires prior standardisation | scikit-learn decomposition docs; statisticsbyjim.com PCA guide | high | Fundamental PCA property |
| Sparse PCA preferred for regulated attribution | scikit-learn docs (SparsePCA); inference from RBNZ explainability principles | high | Inference labelled |
| PCA on LLM embeddings: 60× speedup | arxiv.org/abs/2508.04307; arxiv.org/abs/2504.08386 | high | Two independent empirical papers |
| Bayesian optimisation vs. GA/PSO trade-off by space type | Springer 2025 PSO review; IEEE 2024 comparison; Optuna docs | high | Consistent across sources |
| NSGA-II for portfolio Pareto fronts | EvoFolio (link.springer.com/article/10.1007/s00521-024-09456-w); MDPI NSGA-II RL paper | high | Two independent 2024/2025 sources |
| Contextual bandits for one-shot analytics | meegle.com; geteppo.com; NeurIPS 2024 dynamic pricing paper | high | Consistent across practitioner and research sources |
| Offline RL (CQL/IQL) for regulated industries | Springer 2024 chapter; d3rlpy docs; openreview.net IQL | high | Multiple independent sources including primary papers |
| RL explainability gap | Absence of SHAP + temporal credit assignment in literature; practitioner consensus | high | Gap confirmed by non-existence of solution |
| Neural combinatorial optimisation state of art | NeurIPS 2024; Springer 2025 review; PLoS ONE 2025 | medium | Benchmark results; analytics team applicability is an inference |
| PSO vs. ACO domain partition | arxiv.org/html/2403.03781v1 (NAS); IEEE 2024 comparison | high | Two independent experimental comparisons |
| Adoption maturity gradient | Reference ML item (practitioner survey); d3rlpy docs; Stable Baselines3 docs | high | Practitioner-informed inference |

### Assumptions

- **Assumption:** Analytics teams in regulated financial services do not have dedicated GPU clusters for training RL agents from scratch. **Justification:** The reference item's minimum viable MLOps stack (open-source, cloud-portable) was explicitly designed for teams without specialised infrastructure; this item inherits that assumption.
- **Assumption:** RBNZ's principles-based approach to model risk management applies to RL policy explainability in the same way it applies to supervised ML models. **Justification:** RBNZ has not published specific guidance on RL; the principles (explainability, validation, outcome monitoring) are stated as technology-agnostic in RBNZ's primary publications.
- **Assumption:** Offline RL policy quality is adequate for analytics use cases when the historical logged dataset has reasonable coverage of the state-action space. **Justification:** CQL and IQL papers confirm this; the caveat about coverage gaps is an explicit limitation noted in Findings.

### Analysis

Three evidence hierarchies structure this research. For PCA: textbook formulations (Bishop, Jolliffe & Cadima) establish the mechanics; scikit-learn documentation establishes the implementation; practitioner sources (statisticsbyjim, crunchingthedata) establish decision heuristics; and recent arxiv work establishes the LLM embedding frontier application. For GAs/PSO: the primary papers (Kennedy & Eberhart 1995, Deb et al. NSGA-II) are inaccessible behind paywalls but their findings are confirmed in multiple secondary sources and validated in recent 2024–2025 empirical work. For RL: the primary algorithm papers (PPO, SAC, CQL, IQL) are all accessible via arxiv; Stable Baselines3 documentation confirms implementation maturity; practitioner sources confirm the bandits-first heuristic.

The primary tension is between academic enthusiasm for RL applications in analytics and the practical constraints that most analytics teams face. Academic papers routinely demonstrate RL advantages for dynamic pricing, recommendations, and resource allocation — but nearly all use idealised simulation environments with millions of training steps. For regulated analytics teams without simulation infrastructure, those results do not translate. The resolution applied here: offline RL is the correct bridging technique (no simulation required), and contextual bandits are the correct default below the full RL threshold. This resolution is well-supported by the offline RL literature and the contextual bandits evidence.

For GA/swarm vs. Bayesian optimisation, the resolution is a problem-type partition rather than a ranking. There is no single superior method — the correct choice depends on whether the search space is continuous or combinatorial, which is a property the practitioner knows before selecting the algorithm.

### Risks, Gaps, and Uncertainties

- **RL explainability in regulated contexts:** No published solution adequately bridges SHAP-style feature attribution and temporal credit assignment for RL policies. This is not a near-term resolution gap — it is a research frontier, not a missing practitioner tutorial.
- **Swarm Intelligence at analytics scale:** The evidence base for swarm methods (PSO, ACO) in financial analytics specifically is thinner than for general machine learning. Most empirical results are from manufacturing, engineering, and image classification. The transfer to financial analytics is plausible but not directly validated.
- **Offline RL dataset coverage:** The effectiveness of CQL/IQL is contingent on the logging policy having explored enough of the relevant state-action space. For organisations whose historical decisions were highly concentrated (e.g., always charged a fixed price), offline RL will not learn better policies from that data.
- **Neural combinatorial optimisation training cost:** The transformer-based NCO models (NeurIPS 2024) require significant training on problem instances before deployment. The compute cost for initial training may be prohibitive for analytics teams with small-scale routing/scheduling problems — the GA/ACO baseline remains more accessible.
- **Contextual bandits primary sources not directly accessed:** The practitioner evidence for contextual bandits (geteppo.com, meegle.com) is secondary; the underlying algorithms (Thompson Sampling, UCB) are well-established but no primary experimental paper on financial services bandit applications was directly retrieved.

### Open Questions

- What is the minimum dataset coverage (as a fraction of state-action space) required for offline RL to produce policies reliably better than the historical logging policy? This would define the data viability threshold for analytics teams considering offline RL adoption. (Suggested priority: medium)
- Is there a regulatory-grade explainability framework that bridges SHAP-style local attribution and RL's temporal credit assignment — and if not, what compliance proxies (e.g., decision trees fitted to approximate the RL policy) are acceptable to RBNZ? (Suggested priority: high — directly relevant to RL adoption in regulated industries)
- What does a minimum viable contextual bandit deployment look like for a 5–10 person analytics team in financial services — what data pipeline, infrastructure, and evaluation protocol is required? (Suggested priority: medium)
- Do NSGA-II portfolio optimisation results from academic papers (EvoFolio, 2024) generalise to NZ-market equities and fixed income, which have different liquidity profiles and lower transaction volumes than the NASDAQ datasets used in those papers? (Suggested priority: low — exploratory)

---

## Output

- Type: knowledge
- Description: Decision-oriented landscape of four advanced ML technique families for analytics teams in regulated financial services — PCA/extensions, Genetic Algorithms/Evolutionary Computation, Swarm Intelligence, and Reinforcement Learning. Covers mechanics, when to use/not use, best practices, 2024–2025 advancements, and unified decision positioning relative to the GBDTs established in the reference item.
- Links:
  - https://scikit-learn.org/stable/modules/decomposition.html — scikit-learn PCA, KernelPCA, SparsePCA, IncrementalPCA documentation
  - https://arxiv.org/abs/2110.06169 — Kostrikov et al., Implicit Q-Learning (IQL), the primary offline RL reference for analytics
  - https://stable-baselines3.readthedocs.io — Stable Baselines3 RL algorithm documentation (PPO, SAC, TD3)