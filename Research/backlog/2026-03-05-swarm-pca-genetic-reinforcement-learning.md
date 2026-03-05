---
title: "Swarm Intelligence, PCA, Genetic Algorithms, and Reinforcement Learning — advanced techniques for analytics teams"
added: 2026-03-05
status: backlog
priority: high
blocks: []
tags: [machine-learning, analytics, swarm-intelligence, pca, dimensionality-reduction, genetic-algorithms, evolutionary-computation, reinforcement-learning, optimisation, advanced-analytics]
started: ~
completed: ~
output: [knowledge]
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

This item fills those four gaps with the same structure — decision guide, best practices, current advancements — as the reference item, and explicitly cross-references where these techniques integrate with or substitute for methods already covered.

**Why now:** Analytics teams that have mastered GBDTs and basic MLOps are increasingly encountering problems where gradient-based optimisation fails (non-differentiable objectives, combinatorial search spaces), where dimensionality reduction is mishandled (PCA misuse causing information loss or spurious compression), and where sequential decision problems cannot be solved by static supervised models (RL territory). This item provides the decision vocabulary to engage with those situations correctly.

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

- [ ] Bishop — *Pattern Recognition and Machine Learning*, Ch. 12 (PCA, probabilistic PCA, kernel PCA): https://www.microsoft.com/en-us/research/uploads/prod/2006/01/Bishop-Pattern-Recognition-and-Machine-Learning-2006.pdf
- [ ] Jolliffe & Cadima — "Principal component analysis: a review and recent developments" (2016), *Phil. Trans. R. Soc. A*: https://royalsocietypublishing.org/doi/10.1098/rsta.2015.0202
- [ ] Kennedy & Eberhart — PSO original paper (1995): https://ieeexplore.ieee.org/document/488968
- [ ] Dorigo & Gambardella — Ant Colony System (1997): https://ieeexplore.ieee.org/document/585892
- [ ] Holland — *Adaptation in Natural and Artificial Systems* (1975/1992) — foundational GA text
- [ ] Deb et al. — NSGA-II (2002): https://ieeexplore.ieee.org/document/996017
- [ ] Storn & Price — Differential Evolution (1997): https://link.springer.com/article/10.1023/A:1008202821328
- [ ] Sutton & Barto — *Reinforcement Learning: An Introduction* (2nd ed., 2018): http://incompleteideas.net/book/the-book-2nd.html
- [ ] Mnih et al. — DQN paper (2015): https://www.nature.com/articles/nature14236
- [ ] Schulman et al. — PPO paper (2017): https://arxiv.org/abs/1707.06347
- [ ] Haarnoja et al. — SAC paper (2018): https://arxiv.org/abs/1801.01290
- [ ] Kumar et al. — CQL offline RL (2020): https://arxiv.org/abs/2006.04779
- [ ] Kostrikov et al. — IQL offline RL (2021): https://arxiv.org/abs/2110.06169
- [ ] Vinyals et al. — Pointer Networks for combinatorial optimisation (2015): https://arxiv.org/abs/1506.03134
- [ ] Stanley & Miikkulainen — NEAT (2002): https://nn.cs.utexas.edu/downloads/papers/stanley.ec02.pdf
- [ ] scikit-learn documentation — PCA, KernelPCA, SparsePCA, IncrementalPCA: https://scikit-learn.org/stable/modules/decomposition.html
- [ ] Stable Baselines3 documentation — PPO, SAC, TD3 implementations and benchmarks: https://stable-baselines3.readthedocs.io
- [ ] `Research/completed/2026-03-03-ml-techniques-and-algorithms.md` — reference taxonomy; this item is a direct extension

---

## Findings

*(Fill in when completing.)*

### Executive Summary

### Key Findings

1.
2.

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| | | high / medium / low | |

### Assumptions

- **Assumption:** ... **Justification:** ...

### Analysis

### Risks, Gaps, and Uncertainties

-

### Open Questions

-

---

## Output

- Type: knowledge
- Description:
- Links:
