# Progress

Last updated: 2026-03-06 (h-neuron-over-compliance)
Last updated: 2026-03-05 (llm-hallucination-mechanisms)
Last updated: 2026-03-05 (controlled-hallucination-perception-as-construction)
Last updated: 2026-03-05 (general-agent-optimization-framework backlog item)
Last updated: 2026-03-05 (hard-problem-vs-real-problem-consciousness)
Last updated: 2026-03-04 (W-0032: remove brave_search, fix Tavily env var, add MCP config tests)
Last updated: 2026-03-03 (research-agenda-curation-coverage)
Last updated: 2026-03-03 (ml-techniques-and-algorithms backlog item)
Last updated: 2026-03-03 (research-output-types)
Last updated: 2026-03-03 (research system: add Research Notes section, follow skill in full)
Last updated: 2026-03-03 (meta-research backlog items — improve research and knowledge integration)
Last updated: 2026-03-03 (ai-strategy-risk-reduction-focus)
Last updated: 2026-03-03 (ai-line-1-line-2-risk-agents)
Last updated: 2026-03-03 (ai-control-testing-and-assurance)
Last updated: 2026-03-02 (wiki publishing implementation — W-0030)
Last updated: 2026-03-02 (research-review-ci-step)
Last updated: 2026-03-02 (ai-not-a-data-problem backlog item)
Last updated: 2026-03-02 (search-interaction-distribution backlog items)
Last updated: 2026-03-02 (transaction-costs)
Last updated: 2026-03-02 (integrative-framework-agent-decision-making backlog item)
Last updated: 2026-03-03 (ai-control-testing-and-assurance)

---

## Current Status

**Phase:** Issue consolidation (AGENTS.md + config improvements)
**Next phase:** Group B — Skills repo improvements (#8, #9) via PR to `davidamitchell/Skills`
**Branch:** `copilot/add-research-review-ci-step`

---

| Epic | Title | Status | Complete |
|---|---|---|---|
| 0 | Foundation | Done | 10 / 10 slices |
| 1 | Research Item Process | Done | 5 / 5 slices |
| 2 | YouTube Transcript Fetcher | Done | 4 / 4 slices |
| 3 | Indexing and Tracking | Done | 3 / 3 slices |

---

## Work Log

### 2026-03-06 — Research Loop (h-neuron-over-compliance)

**Completed:**

Research item:
- `Research/completed/2026-03-05-h-neuron-over-compliance.md` — completed; over-compliance is the causal pathway from H-Neurons to hallucination, sycophancy, and jailbreak, confirmed via activation scaling across four benchmarks; global H-Neuron suppression is insufficient for production deployment because it reduces both inappropriate and appropriate compliance (the helpfulness trade-off), and context-aware suppression remains unimplemented; H-Neuron activation monitoring without suppression is the most immediately deployable application.

Sources consulted:
- https://arxiv.org/abs/2512.01797 (Gao et al. 2025 — over-compliance causal mechanism, activation scaling experiments, C parameter optimisation)
- https://arxiv.org/abs/2310.01405 (Zou et al. 2023 — Representation Engineering: reading vectors, honesty and harmlessness control)
- https://arxiv.org/abs/2306.03341 (Li et al. 2023 — Inference-Time Intervention: +32.6 pp TruthfulQA, truthfulness-helpfulness trade-off)

### 2026-03-05 — Research Loop (h-neurons-synthesis)

**Completed:**

Research item:
- `Research/completed/2026-03-05-h-neurons-synthesis.md` — completed; LLM hallucinations are three expressions (factual confabulation, sycophancy, jailbreak) of a single over-compliance mechanism encoded in sparse FFN neurons (< 1‰) that form during pre-training via the NTP objective and survive SFT/RLHF via parameter inertia; interventions span four access tiers from RAG (any API) to pre-training data curation (model developers only), with inference-time H-Neuron monitoring the key near-term opportunity for open-weight deployments.

Sources consulted:
- https://arxiv.org/abs/2512.01797 (Gao et al. 2025 — H-Neurons: identification, causal mechanism, pre-training origin)
- Research/completed/2026-03-05-h-neurons-in-llms.md (H-Neurons paper detailed findings)
- Research/completed/2026-03-05-llm-hallucination-mechanisms.md (macroscopic hallucination taxonomy and mitigation landscape)

---

### 2026-03-05 — Research Loop (swarm-pca-genetic-reinforcement-learning)

**Completed:**

Research item:
- `Research/completed/2026-03-05-swarm-pca-genetic-reinforcement-learning.md` — completed; PCA is the correct dimensionality reduction step for collinearity-sensitive models but unnecessary for GBDTs; contextual bandits are the correct default for one-shot explore/exploit analytics problems with full RL reserved for sequential state-transition problems; offline RL (CQL/IQL via d3rlpy) is the appropriate regulated-industry RL entry point; NSGA-II is the benchmark for multi-objective portfolio optimisation; GA/PSO outperform Bayesian optimisation on combinatorial/discrete search spaces.

Sources consulted:
- https://scikit-learn.org/stable/modules/decomposition.html (scikit-learn PCA, KernelPCA, SparsePCA, IncrementalPCA documentation)
- https://arxiv.org/abs/2110.06169 (Kostrikov et al., Implicit Q-Learning offline RL)
- https://stable-baselines3.readthedocs.io (Stable Baselines3 RL algorithms)

---

### 2026-03-05 — Research Loop (general-agent-optimization-framework)

**Completed:**

Research item:
- `Research/completed/2026-03-05-general-agent-optimization-framework.md` — completed; DSPy (Khattab et al. 2023) identified as the only surveyed framework providing native inner-loop (MIPRO instruction optimization, ~370 LLM calls per run) and outer-loop (evaluation harness) support; Chambers & Partners Golden Set path closed by copyright; open stack recommended as AgentBench → GAIA → FinBen/LegalBench; instruction drift mitigated via Brevity Penalty + LLMLingua compression.

Sources consulted:
- https://arxiv.org/abs/2310.03714 (Khattab et al. 2023 — DSPy: Compiling Declarative Language Model Calls into Self-Improving Pipelines)
- https://arxiv.org/abs/2406.07496 (Yuksekgonul et al. 2024 — TextGrad: Automatic Differentiation via Text)
- https://dspy.ai/ (DSPy documentation — optimizers, cost profile, integration)

### 2026-03-05 — Research Loop (h-neurons-in-llms)

**Completed:**

Research item:
- `Research/completed/2026-03-05-h-neurons-in-llms.md` — completed; Gao et al. (arXiv:2512.01797) identify fewer than 1‰ of FFN neurons as H-Neurons using the CETT metric and L1-sparse linear probing; controlled activation perturbation shows these neurons causally drive over-compliance across four independent benchmarks (false premises, misleading context, sycophantic capitulation, jailbreak); and cross-model transfer experiments confirm H-Neurons originate during pre-training and survive SFT with minimal parameter change, meaning standard alignment does not address the root cause.

Sources consulted:
- https://arxiv.org/abs/2512.01797 (Gao et al. 2025 — H-Neurons: On the Existence, Impact, and Origin of Hallucination-Associated Neurons in LLMs)
- https://arxiv.org/abs/2202.05262 (Meng et al. 2022 — Locating and Editing Factual Associations in GPT / ROME)
- https://transformer-circuits.pub/2022/toy_model/index.html (Elhage et al. 2022 — Toy Models of Superposition)

### 2026-03-05 — Research Loop (llm-hallucination-mechanisms)

**Completed:**

Research item:
- `Research/completed/2026-03-05-llm-hallucination-mechanisms.md` — completed; established the factuality/faithfulness taxonomy (Huang et al. 2023) as the operationally correct framework for LLM hallucination, with root causes spanning data (noisy pretraining, knowledge gaps), training (next-token fluency objective, RLHF-induced sycophancy), and inference (decoding randomness); all mainstream mitigations (RAG, RLHF, CoT, Constitutional AI) operate pre- or post-generation, leaving a gap at the during-generation level that neuron-level approaches (H-Neurons paper) are positioned to fill.

Sources consulted:
- https://arxiv.org/abs/2311.05232 (Huang et al. 2023 — A Survey on Hallucination in Large Language Models)
- https://arxiv.org/abs/2202.03629 (Ji et al. 2023 — Survey of Hallucination in Natural Language Generation)
- https://lilianweng.github.io/posts/2024-07-07-hallucination/ (Weng 2024 — Extrinsic Hallucinations in LLMs)

### 2026-03-05 — New backlog item (swarm-pca-genetic-reinforcement-learning)
### 2026-03-05 — New backlog item (general-agent-optimization-framework)

**Added:**

- `Research/backlog/2026-03-05-general-agent-optimization-framework.md` — new high-priority backlog item for designing a Self-Improving AI Agent Evaluation Loop with a nested inner/outer loop architecture, Meta-Optimizer prompt rewriting, benchmark mapping (GPQA, HLE, GAIA, FinBen, LegalBench, SWE-bench), DSPy integration, synthetic data generation, and instruction-drift mitigation.

### 2026-03-05 — Research Loop (hard-problem-vs-real-problem-consciousness)

**Completed:**

Research item:
- `Research/completed/2026-02-28-hard-problem-vs-real-problem-consciousness.md` — completed; Seth's "real problem" is a principled deferment of Chalmers' "hard problem," not a dissolution — it asks which brain patterns correlate with which specific experiences, whereas the hard problem asks why any physical process gives rise to experience at all; Frankish's illusionism (denying robust qualia) and Goff's panpsychism (treating consciousness as fundamental) are the two positions that engage the hard problem more directly, and no current position closes Chalmers' explanatory gap.

Sources consulted:
- https://en.wikipedia.org/wiki/Hard_problem_of_consciousness (Chalmers' formulation, PhilPapers survey data)
- https://en.wikipedia.org/wiki/Being_You (Seth's real problem and reviews)
- https://en.wikipedia.org/wiki/Keith_Frankish (illusionism)

### 2026-03-05 — Research Loop (free-energy-entropy-and-life)

**Completed:**

Research item:
- `Research/completed/2026-02-28-free-energy-entropy-and-life.md` — completed; the three-layer chain from Schrödinger's negentropy (1944) through Friston's variational free energy (FEP) to Seth's beast machine thesis is logically coherent but transitions between layers are motivated conjectures not deductive entailments; the mathematical bridge between Shannon/Boltzmann entropy and Friston's VFE is formal (structural identity via information geometry), not merely analogical; Seth explicitly frames FEP as not a theory of consciousness — it explains why brains predict, while his extra condition (biological, interoceptive, survival-oriented prediction) is what localises consciousness.

Sources consulted:
- https://www.quantamagazine.org/anil-seth-finds-consciousness-in-lifes-push-against-entropy-20210930/ (Seth, Quanta Magazine 2021 — primary source, direct quotes)
- https://arxiv.org/abs/2201.06387 (Friston et al. 2022 — "The free energy principle made simpler but not too simple")
- https://en.wikipedia.org/wiki/Free_energy_principle (Wikipedia FEP — VFE formulation and Markov blanket argument)

### 2026-03-05 — Research Loop (exploit-explore-ai-portfolio-framework)

**Completed:**

Research item:
- `Research/backlog/2026-03-05-swarm-pca-genetic-reinforcement-learning.md` — new high-priority backlog item created; expands on four technique families not covered in detail in `2026-03-03-ml-techniques-and-algorithms.md`: Swarm Intelligence (PSO, ACO, ABC), PCA and its modern extensions (Kernel PCA, Sparse PCA, Incremental PCA), Genetic Algorithms and Evolutionary Computation (GA, GP, DE, NSGA-II), and Reinforcement Learning (DQN, PPO, SAC, offline RL via CQL/IQL); includes full decision guides, best practices, latest 2023–2025 advancements, and synthesis decision table across all four families and the reference item's methods.
- `Research/completed/2026-02-28-exploit-explore-ai-portfolio-framework.md` — completed; five observable dimensions (solution maturity, market novelty, evidence basis, milestone horizon, capability requirement) form the STEM-C diagnostic instrument for classifying AI investments as exploit, adjacent explore, or transformational explore at investment review; the 70/20/10 portfolio benchmark (exploit/adjacent/transformational) is confirmed by two independent sources (McKinsey Three Horizons, Nagji & Tuff HBR 2012) with Nagji & Tuff's counterintuitive finding that the 10% transformational investment generates ~70% of long-run innovation value; BCG's 2024 finding that 74% of organisations fail to scale AI value is consistent with the theoretical prediction that exploitation-only portfolios hit a value ceiling.

Sources consulted:
- https://umbrex.com/resources/frameworks/organization-frameworks/ambidextrous-innovation-portfolio-explore-exploit-matrix/ (Ambidextrous Portfolio Matrix — scoring rubric and governance model)
- https://hbr.org/2012/05/managing-your-innovation-portfolio (Nagji & Tuff Innovation Ambition Matrix, 70/20/10 benchmark)
- https://www.bcg.com/publications/2024/wheres-value-in-ai (BCG "Where's the Value in AI?" 2024 — 74% scaling failure statistic)

### 2026-03-05 — Research Loop (controlled-hallucination-perception-as-construction)

**Completed:**

Research item:
- `Research/completed/2026-02-28-controlled-hallucination-perception-as-construction.md` — completed; perception is a generative, top-down process established across four independent paradigms (rubber hand illusion, binocular rivalry, mismatch negativity, observer-relative colour illusions), mechanistically grounded in Rao & Ballard's (1999) predictive coding architecture; Seth's "controlled hallucination" framing is accurate — ordinary perception and pathological hallucination share the same computational mechanism and differ only in degree of sensory constraint; the strongest philosophical objections (naive realism, Gibson's direct perception) are coherent but empirically costly when forced to account for the full evidence base.

Sources consulted:
- https://www.nature.com/articles/nn0199_79.pdf (Rao & Ballard 1999 — predictive coding in visual cortex, foundational paper)
- https://www.nature.com/articles/35784.pdf (Botvinick & Cohen 1998 — rubber hand illusion original Nature paper)
- https://www.technologyreview.com/2021/08/25/1032121/brains-controlled-hallucination/ (MIT Technology Review — Seth's controlled hallucination, 2021)

### 2026-03-05 — Research Loop (ai-strategy-swe-focus)

**Completed:**

Research item:
- `Research/completed/2026-02-28-ai-strategy-swe-focus.md` — completed; individual productivity gains of 40–55% on bounded coding tasks are real and consistent across RCT and enterprise deployments (GitHub Copilot RCT, ANZ Bank), but DORA 2024 shows higher AI adoption associates with worse delivery stability (–7.2%) unless workflows are redesigned; the enterprise state is Type 2 (agentic builder, human-gated) not Type 3 (autonomous deployment), and autonomous coding agent benchmarks (SWE-bench: 14% in 2024 → ~80% curated by 2026) overstate generalised capability due to clustering on solved problems.

Sources consulted:
- https://arxiv.org/abs/2302.06590 (GitHub/MIT/Microsoft controlled experiment — 55.8% faster task completion)
- https://cloud.google.com/blog/products/devops-sre/announcing-the-2024-dora-report (Google DORA 2024 — delivery stability decline with AI adoption)
- https://www.swebench.com/ (SWE-bench leaderboard — autonomous coding agent benchmark trajectory)

### 2026-03-05 — Research Loop (ai-strategy-security-focus)

**Completed:**

Research item:
- `Research/completed/2026-02-28-ai-strategy-security-focus.md` — completed; AI security strategy requires parallel governance for two distinct vectors: AI-enhanced attacks (1,265% phishing volume increase, $2.7B BEC losses in 2024, 82% of phishing AI-generated in 2025) and AI systems as attack surfaces (prompt injection the highest-severity risk, no complete architectural fix); NZ NCSC published joint guidance with 14 international agencies in January 2024 and October 2025 minimum standards apply to AI systems; FMA and RBNZ flag AI security risks but have issued no mandatory AI-specific controls.

Sources consulted:
- https://atlas.mitre.org/ (MITRE ATLAS — adversarial threat landscape for AI systems, 66+ techniques)
- https://www.ncsc.govt.nz/protect-your-organisation/engaging-with-artificial-intelligence/ (NZ NCSC Engaging with AI, January 2024)
- https://csrc.nist.gov/pubs/ai/100/2/e2023/final (NIST AI 100-2e2023 adversarial ML taxonomy)

### 2026-03-05 — Research Loop (sources-of-research)

**Completed:**

Research item:
- `Research/completed/2026-02-27-sources-of-research.md` — completed; seven RSS feeds confirmed accessible from GitHub Actions runner IPs and added to `config/sources.yaml` (HF Blog, Lil'Log, DeepMind Blog, The Gradient, BAIR Blog, Sebastian Raschka, Simon Willison); YouTube channel Atom feeds are blocked from runner IPs and `youtube.channels` remains empty pending a fix; arXiv RSS works but requires keyword filtering before automated ingestion is practical — the existing arxiv-mcp-server is the right tool for targeted paper queries.

Sources consulted:
- https://export.arxiv.org/rss/cs.AI (arXiv RSS feed — confirmed accessible, 348 papers/day)
- https://huggingface.co/blog/feed.xml (Hugging Face Blog RSS — confirmed accessible)
- https://lilianweng.github.io/index.xml (Lil'Log — confirmed accessible)

### 2026-03-05 — Research Loop (ml-techniques-and-algorithms)

**Completed:**

Research item:
- `Research/completed/2026-03-03-ml-techniques-and-algorithms.md` — completed; gradient-boosted decision trees (XGBoost, LightGBM, CatBoost) are confirmed as the correct default for tabular analytics; the single most diagnostic gap between normal and advanced practice is out-of-time validation; conformal prediction, causal ML (DoWhy/EconML/CausalML), AutoML (AutoGluon/H2O/FLAML), and TabPFN-2.5 are all production-ready in 2024; RBNZ's principles-based model risk management expectations are satisfiable with SHAP + MLflow + Evidently AI.

Sources consulted:
- https://arxiv.org/abs/2408.14817 (Lazebnik et al. 2024 — comprehensive 111-dataset tabular ML benchmark)
- https://www.kaggle.com/AI-Report-2023 (Kaggle AI Report 2023 — practitioner tabular data survey)
- https://proceedings.neurips.cc/paper/2015/file/86df7dcfd896fcaf2674f757a2463eba-Paper.pdf (Sculley et al. 2015 — hidden technical debt in ML systems)
- https://arxiv.org/abs/2511.08667 (TabPFN-2.5 — tabular foundation model report 2024)
- https://www.rbnz.govt.nz/hub/publications/financial-stability-report/2025/may/ai-pre-release/rise-of-the-machines (RBNZ Rise of the Machines — May 2025 AI supervisory expectations)

### 2026-03-04 — Session (sdlc-ai-prompt-patterns: add and start research item)

**Completed:**

Research item:
- `Research/in-progress/2026-03-04-sdlc-ai-prompt-patterns.md` — added and immediately moved to in-progress; item covers emergent patterns in AI agent prompting across all eight SDLC phases (Discovery, Requirements, Design, Planning, Building, Testing, Reviewing, Iteration), best practices for phase-aware prompt engineering, emergent strategies from production tooling (GitHub Copilot Workspace, Cursor, Claude Code, Aider), and a framework for structured prompt templates.

### 2026-03-04 — Session (W-0032: MCP config cleanup)

**Completed:**

Repo improvement:
- `.github/mcp.json` — removed `brave_search` entry (no `BRAVE_API_KEY` in approved credentials table)
- `.mcp.json` — removed `brave_search` entry (same reason)
- `AGENTS.md` — updated MCP Configuration section: server count 10→9, removed `brave_search` from Server Reference table, availability check table, npx server list, and research task instructions; confirmed `TAVILY_API_KEY` is the correct env var for `tavily-mcp@latest`; `tavily` is now the sole web search MCP server
- `tests/test_mcp_config.py` — 15 new tests: JSON validity, brave_search absent, TAVILY_API_KEY correct, both files in sync, smoke test for expected server list
- `BACKLOG.md` — W-0032 marked done

### 2026-03-03 — Session (MCP config cleanup backlog — W-0032)

**Completed:**

Repo improvement:
- `BACKLOG.md` — added W-0032: remove `brave_search` MCP from both `.github/mcp.json` and `.mcp.json`, and investigate/fix the Tavily API key env var name so `tavily-mcp@latest` starts cleanly.

### 2026-03-03 — Research Loop (research-agenda-curation-coverage)
### 2026-03-03 — Research Loop (research-output-types)

**Completed:**

Research item:
- `Research/completed/2026-02-27-research-output-types.md` — completed; confirmed the five-type output taxonomy (skill, tool, agent, knowledge, backlog-item) is sufficient and consistently defined across AGENTS.md, Research/README.md, and the template; identified that `tool`, `knowledge`, and `backlog-item` have well-documented handling procedures while `skill` and `agent` are under-specified; no additional types warranted.

Sources consulted:
- `AGENTS.md` § Output Types (primary definition source)
- `Research/README.md` § Output Types (secondary enumeration)
- https://github.com/davidamitchell/Skills (Skills repo — directory structure for skill outputs)

---

### 2026-03-03 — Research Loop (local-index-vs-reference)

**Completed:**

Research item:
- `Research/completed/2026-02-27-local-index-vs-reference.md` — completed; derived a three-criteria decision framework (re-fetchability, link rot risk, file format) to determine per-content-type storage policy. YouTube transcripts store as local text files, arXiv papers remain reference-only, web page key passages are pasted inline, and notes are always local. Git LFS is not warranted at current scale.

Sources consulted:
- https://en.wikipedia.org/wiki/Link_rot (link rot statistics — 38% of 2013 pages gone by 2023, Pew Research)
- https://docs.github.com/en/repositories/working-with-files/managing-large-files/about-large-files-on-github (GitHub file size limits: 50 MiB warning, 100 MiB block)
- https://arxiv.org/help/arxiv_identifier (arXiv permanent URL scheme documentation)

---

### 2026-03-03 — Research Loop (local-database)

**Completed:**

Research item:
- `Research/completed/2026-02-27-local-database.md` — completed; SQLite + FTS5 (Phase 1) and sqlite-vec (Phase 2) is the correct local database technology; five-table schema (`items`, `tags`, `sources`, `processed`, `transcripts`) with FTS5 virtual table supports all required query patterns; migration is triggered by observable signals (≥500 state entries, cross-item query need, semantic search backlog, or concurrent writes) rather than a fixed item count.

Sources consulted:
- https://sqlite.org/fts5.html (SQLite FTS5 extension documentation — BM25, phrase search, prefix search)
- https://github.com/asg017/sqlite-vec (sqlite-vec KNN vector search extension — pure C, pip install, pre-v1)
- https://duckdb.org/why_duckdb (DuckDB design rationale — OLAP-optimised, columnar, no built-in vector search)

---

### 2026-03-03 — Research Loop (research-loop-quality-prompt-engineering)

**Completed:**

Research item:
- `Research/completed/2026-03-03-research-loop-quality-prompt-engineering.md` — completed; corpus audit of 20 items shows quality variation is prompt-caused (Research Skill Output section lifted source engagement from avg 3.1 to 12.8 per item); five targeted additions made to `research-prompt.md` addressing prior-research cross-referencing, explicit source-marking discipline, executive summary specificity, anti-formulaic constraints, and minimum finding size; four-check shell quality gate designed.

Sources consulted:
- `Research/completed/` corpus (primary — 20 items audited directly)
- https://arxiv.org/abs/2406.06608 (The Prompt Report: systematic survey of 58+ LLM prompting techniques)
- https://github.com/danielmiessler/fabric (Fabric extract_wisdom pattern — structured output and minimum output count approach)



**Completed:**

Research item:
- `Research/completed/2026-03-03-research-agenda-curation-coverage.md` — completed; the research backlog suffers from priority inflation (88% rated medium) and domain drift (44% of backlog in Research Tooling); the remedy is a five-domain taxonomy, a four-dimension prioritisation rubric (decision dependency, dependency unblocking, gap severity, input availability; scored 1–3 each; 10–12 = high), a 40%-concentration drift detection threshold, and a monthly agenda review triggered by workflow_dispatch; a `research agenda` CLI command can be implemented without new dependencies by extending src/research/cli.py.

Sources consulted:
- https://fortelabs.com/blog/para/ (PARA method — actionability-based prioritisation principle)
- https://mrx.sivoinsights.com/blog/how-jobs-to-be-done-connects-research-strategy-and-execution (JTBD — outcome-based priority framework)
- https://www.rand.org/content/dam/rand/pubs/research_briefs/RB10000/RB10036/RAND_RB10036.pdf (RAND research portfolio evaluation — drift detection and coverage balance)

### 2026-03-03 — Research Loop (knowledge-retention-active-recall)

**Completed:**

Research item:
- `Research/completed/2026-03-03-knowledge-retention-active-recall.md` — completed; knowledge from completed research items decays without re-engagement even given the deeper encoding that research-writing provides; the highest-priority fix is adding a "Prior Research" step to `research-prompt.md` (zero infrastructure cost); a weekly GitHub Actions digest workflow posting 3–5 items as a GitHub issue is the lowest-friction passive delivery mechanism; spaced repetition principles (7/30/90 day intervals) apply at research item level using fixed intervals as a pragmatic SM-2 adaptation.

Sources consulted:
- https://en.wikipedia.org/wiki/Testing_effect (retrieval practice evidence base — Roediger, Pashler et al.)
- https://en.wikipedia.org/wiki/Levels_of_processing_effect (Craik & Lockhart 1972 — encoding depth and knowledge durability)
- https://en.wikipedia.org/wiki/Spaced_repetition (spacing effect and SM-2 applicability)

### 2026-03-03 — Research Loop (knowledge-representation-agent-context)

**Completed:**

Research item:
- `Research/completed/2026-03-03-knowledge-representation-agent-context.md` — completed; LSA is superseded by dense embeddings for agent retrieval; a five-layer knowledge architecture (raw → extractive → abstractive → graph nodes → domain schema) maps onto the Letta context-engineering framework; for dynamic corpora, LightRAG is preferred over GraphRAG due to incremental update support; RAPTOR hierarchical summarisation (+20pp on QuALITY benchmark) has the highest immediate value for this research corpus because Layers 0–2 already exist in every completed item; concept maps do not constitute a separate agent-accessible layer.

Sources consulted:
- https://arxiv.org/abs/2404.16130 (GraphRAG — Edge et al. 2024, Microsoft Research)
- https://arxiv.org/abs/2410.05779 (LightRAG — Guo et al. 2024, EMNLP 2025)
- https://arxiv.org/abs/2401.18059 (RAPTOR — Sarthi et al. 2024, ICLR 2024)

### 2026-03-03 — Research Loop (cross-item-synthesis-meta-insights)

**Completed:**

Research item:
- `Research/completed/2026-03-03-cross-item-synthesis-meta-insights.md` — completed; cross-item synthesis requires: a methodology distinguishing synthesis (claims crossing document boundaries) from summary (concatenation), a three-tier thematic clustering method (tags → edge store → manual), a `Research/synthesis/` directory with ADR, and a `synthesise.yml` `workflow_dispatch` workflow following the research-loop pattern. The false-consensus failure mode (LLM generating conclusions not supported by source items) is guarded by requiring explicit source-item citations for every synthesis claim. The 19-item corpus already has 4 identifiable clusters; the AI strategy/governance cluster (6 items) is the highest-value initial synthesis target.

Sources consulted:
- https://en.wikipedia.org/wiki/Systematic_review (narrative synthesis vs. meta-analysis — academic methodology grounding)
- https://github.com/danielmiessler/fabric (extract_wisdom and extract_insights patterns — single-source synthesis pipeline design)
- `Research/completed/2026-03-03-knowledge-linking-connected-corpus.md` (edge store design and tag-overlap clustering signal)

### 2026-03-03 — Research Loop (knowledge-linking-connected-corpus)

**Completed:**

Research item:
- `Research/completed/2026-03-03-knowledge-linking-connected-corpus.md` — completed; the minimum viable approach to a connected corpus is a `## Related Items` section with typed relative Markdown links, a committed JSON edge store at `state/links.json` auto-generated from those sections, and a Python tool that regenerates the index and suggests unlinked relationships via tag overlap and shared source URLs. Backlinks must be derived by file scanning (never written into referenced files), following the Obsidian/Logseq pattern. Five relationship types (`extends`, `contradicts`, `depends-on`, `spawned-from`, `see-also`) cover observed corpus usage.

Sources consulted:
- https://zettelkasten.de/introduction/ (Zettelkasten core principles — connection over collection, fixed addresses)
- https://jackiexiao.github.io/obsidian-docs/en/How%20to/Working%20with%20backlinks/ (Obsidian backlinks — non-intrusive scan-to-derive pattern)
- https://bellingcat.gitbook.io/toolkit/more/all-tools/logseq (Logseq bidirectional linking — independent confirmation of non-intrusive backlink pattern)

### 2026-03-03 — Research system: full skill output retained, seeds Findings

Replaced `## Research Notes` with `## Research Skill Output` in `Research/_template.md`. The new section has explicit subsections for every research skill step (§§0–7): §0 Initialise, §1 Question Decomposition, §2 Investigation, §3 Reasoning, §4 Consistency Check, §5 Depth and Breadth Expansion, §6 Synthesis, §7 Recursive Review. The full output is retained verbatim in the completed item. §6 Synthesis seeds the `## Findings` section (which keeps the existing structured subsections). Updated `research-prompt.md` steps 4–5 and `AGENTS.md` Conducting Research to match.

### 2026-03-03 — Research system: add Research Notes section and explicit skill follow-through

Added `## Research Notes` section to `Research/_template.md` (between Sources and Findings). This section captures the raw output of following the research skill (question decomposition, evidence and observations, consistency and lens check) and is retained verbatim in completed items. Updated `research-prompt.md` steps 4–5 to explicitly follow the research SKILL.md process (§§0–7) and write investigation output into Research Notes before deriving the Findings synthesis from it. Updated `AGENTS.md` Conducting Research section to match.

### 2026-03-03 — Reprioritise backlog so 5 new meta-research items are picked up next

Lowered the 15 existing `high`-priority backlog items to `medium`. Raised the 2 new `medium` items (`research-agenda-curation`, `knowledge-retention`) to `high`. Result: the 5 new meta-research items are now the only `high`-priority items in the backlog and will be the first 5 items the research loop picks up.

### 2026-03-03 — Meta-research backlog items (improve research and knowledge integration)

**Completed:**

Research items added to `Research/backlog/`:
- `2026-03-03-knowledge-linking-connected-corpus.md` — How to make the research corpus a connected knowledge network via explicit cross-references, a backlink index, and Zettelkasten-style linking. Prerequisite for cross-item synthesis and the conversational interface's cross-reference navigation.
- `2026-03-03-research-loop-quality-prompt-engineering.md` — How to systematically evaluate and improve the quality of items produced by the autonomous research loop, including a corpus audit, prompt engineering techniques, and a lightweight CI quality gate design.
- `2026-03-03-cross-item-synthesis-meta-insights.md` — Methodology and tooling for synthesising across multiple completed items into thematic reports, contradiction maps, and actionable insight summaries. Includes design for a `synthesis` skill and a `synthesise.yml` workflow.
- `2026-03-03-research-agenda-curation-coverage.md` — How to maintain a balanced research agenda: domain map, coverage metrics, drift detection, prioritisation framework, and a `research agenda` CLI command.
- `2026-03-03-knowledge-retention-active-recall.md` — Mechanisms for ensuring completed research is recalled and applied: spaced repetition applicability, contextual recall, periodic digest workflow, retention state tracking, and an agent recall instruction for `research-prompt.md`.

These five items form a coherent set addressing both meta-research process improvement (loop quality, agenda curation) and knowledge integration (linking, synthesis, retention).

---
### 2026-03-03 — Research Loop (ai-strategy-risk-reduction-focus)

**Completed:**

Research item:
- `Research/completed/2026-02-28-ai-strategy-risk-reduction-focus.md` — completed; HSBC and JPMorgan are the best-documented cases (60–95% false positive reductions in AML/fraud); SR 11-7 remains the global reference framework for AI model risk, augmented for AI with explainability, bias testing, and drift monitoring requirements; RBNZ has no AI-specific supervisory guidance as of early 2025 and NZ banks default to BS11 for outsourced AI and BPR capital requirements for model governance; the dominant failure modes are training-data bias (CFPB enforcement guidance 2022–2023) and concept drift under economic stress.

Sources consulted:
- https://www.hsbc.com/news-and-views/views/hsbc-views/harnessing-the-power-of-ai-to-fight-financial-crime (HSBC AML AI outcomes)
- https://www.bis.org/fsi/publ/insights63.pdf (BIS FSI Insights No. 63: Regulating AI in the financial sector, Dec 2024)
- https://www.consumerfinance.gov/about-us/newsroom/cfpb-issues-guidance-on-credit-denials-by-lenders-using-artificial-intelligence/ (CFPB AI credit denial guidance)

### 2026-03-03 — Research Loop (ai-strategy-business-efficiency-examples)

**Completed:**

Research item:
- `Research/completed/2026-02-28-ai-strategy-business-efficiency-examples.md` — completed; only 26% of organisations globally have scaled AI to visible business value; the dominant failure modes are data poverty, absence of change management, and pilot-itis (failure to scale beyond proof-of-concept); ANZ Bank is the best-documented near-peer case study in the region with $1.9B productivity savings since 2019; NZ-specific data shows 91% of businesses report efficiency improvements but 68% of SMEs have no AI plans, representing structural risk to NZ's $76B GDP projection.

Sources consulted:
- https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai-2024 (McKinsey State of AI 2024 — adoption rates, productivity outcomes)
- https://www.bcg.com/press/24october2024-ai-adoption-in-2024-74-of-companies-struggle-to-achieve-and-scale-value (BCG AI Adoption 2024 — 74% struggle to scale; AI leaders benchmarks)
- https://aiforum.org.nz/reports/ai-in-action-key-findings-from-new-zealands-third-ai-productivity-report/ (AI Forum NZ Third AI Productivity Report — NZ-specific efficiency data)

### 2026-03-03 — Research Loop (ai-line-1-line-2-risk-agents)

**Completed:**

Research item:
- `Research/completed/2026-02-28-ai-line-1-line-2-risk-agents.md` — completed; commercial vendor platforms (NICE Actimize SURVEIL-X, Behavox, Nasdaq, IBM OpenPages) dominate line 2 AI agent deployment in financial services; all current deployments use a "human reviewer accountable" architecture where agents produce flags and humans retain final accountability; no regulator (FCA/PRA, APRA, BIS, RBNZ) has published agent-specific guidance for line 1/line 2 oversight functions, and the nominal-review accountability problem remains unaddressed.

Sources consulted:
- https://www.mckinsey.com/capabilities/risk-and-resilience/our-insights/how-agentic-ai-can-change-the-way-banks-fight-financial-crime (McKinsey: agentic AI in financial crime compliance)
- https://www.nice.com/press-releases/nice-actimize-empowers-surveil-x-with-generative-ai-launching-a-new-era-in-market-abuse-and-conduct-risk-detection (NICE Actimize SURVEIL-X generative AI launch, 2024)
- https://www.bis.org/fsi/publ/insights63.pdf (BIS FSI Insights: Regulating AI in the financial sector)

### 2026-03-03 — New backlog item: knowledge-representation-agent-context

**Completed:**

Research items:
- `Research/backlog/2026-03-03-knowledge-representation-agent-context.md` — new high-priority backlog item covering latent semantic extraction (LSE/LSA), knowledge graphs (GraphRAG), concept maps, document compression, and knowledge layering as techniques for managing large knowledge corpora under agent context-window constraints. Directly addresses the "1000s of files of context" problem: how to represent, compress, and prioritise knowledge so agents retrieve the right level of abstraction for a given intent.
- `Research/backlog/2026-03-02-integrative-framework-agent-decision-making.md` — extended Context section and Sources list to reference the new knowledge-representation item as a dependency; the knowledge-layer foundation must be established before the DIKW integration and conflict-resolution mechanisms in that item can be fully operationalised.

### 2026-03-03 — Research Loop (ai-line-1-line-2-risk-agents)

**Completed:**

Research item:
- `Research/completed/2026-02-28-ai-line-1-line-2-risk-agents.md` — completed; Behavox and NICE Actimize dominate the commercial line 2 surveillance market, serving most G-SIBs; JPMorgan, HSBC, and ING are the most publicly disclosed deployers of scale AI agents in line 1/2 functions; the universal architecture treats agent output as a tool (human reviews) not a determination, but at billion-transaction scale human review becomes nominal, and no regulator has defined when nominally compliant review becomes meaningless accountability.

Sources consulted:
- https://www.jpmorganchase.com/about/technology/news/ai-and-model-risk-governance (JPMorgan Model Risk Governance disclosure)
- https://www.bis.org/fsi/publ/insights63.pdf (BIS FSI Insights #63 — Regulating AI in the financial sector)
- https://www.moodys.com/web/en/us/insights/ai/navigating-the-shift-how-agentic-ai-is-reshaping-risk-and-compliance.html (Moody's: agentic AI reshaping risk and compliance)

### 2026-03-03 — Research Loop (ai-control-testing-and-assurance)

**Completed:**

Research item:
- `Research/completed/2026-02-28-ai-control-testing-and-assurance.md` — completed; AI-assisted control testing is production-ready across all major GRC platforms and Big-4 audit firms; AI-generated evidence is acceptable under IAASB/PCAOB standards provided it is validated and subject to human professional judgment; the primary open governance question is Type 3 agents making final control effectiveness determinations without human review.

Sources consulted:
- https://www.iaasb.org/news-events/2024-10/iaasb-unveils-new-technology-position-shape-future-audit-and-assurance-standards (IAASB Technology Position October 2024)
- https://www.rbnz.govt.nz/hub/publications/financial-stability-report/2025/may/ai-pre-release/rise-of-the-machines (RBNZ May 2025 Financial Stability Report — AI systemic risk)
- https://www.theiia.org/globalassets/site/content/tools/professional/aiframework-sept-2024-update.pdf (IIA AI Auditing Framework September 2024)

### 2026-03-02 — Extend research item with four threads from owner feedback on wiki rot / memory ranking (agent-memory-management-context-injection)

**Owner raised four threads in PR comment: (1) outcome-based utility over temporal decay, (2) goal-achievement and transaction-cost as memory signals, (3) human memory as flawed blueprint, (4) model-version-aware re-assessment. All four researched and added as Findings 27–30.**

1. **Outcome-based utility ranking over temporal decay (Finding 27)** — TTL/last-accessed are weak proxies. Strong signals: Goal Completion Rate (GCR), transaction cost reduction, task success. EMG-RAG (EMNLP 2024, arXiv:2409.19401) uses RL on Editable Memory Graph; AssoMem (arXiv:2510.10397) fuses importance + recency + similarity. No production memory system closes this feedback loop by default.

2. **Memory-R1 — RL-trained outcome-driven memory (Finding 28)** — arXiv:2508.19828 (Aug 2025): dual-agent RL (Memory Manager + Answer Agent) trained end-to-end on answer correctness using PPO/GRPO. Memory Manager learns ADD/UPDATE/DELETE/NOOP based on downstream task success. First production-adjacent implementation of "did this memory help my goal?" as the training signal.

3. **Human memory anti-patterns for AI design (Finding 29)** — arXiv:2503.10248: LLM agents display human biases (recency, availability) but via different mechanisms and without compensatory corrections. Anti-patterns to avoid: availability bias (frequency ≠ relevance), maladaptive forgetting, recency over-weighting. Design principle: test human memory heuristics against outcome signals rather than copying them.

4. **Model-version-aware memory re-assessment (Finding 30)** — arXiv:2512.13564, Yodaplus 2025, dev.to drift framework: memory staleness has two dimensions — world-state change AND model interpretation shift. When base models update, stored memories may be interpreted differently. Solution: tag entries with model version at write time; run re-assessment diff on model updates. No production system implements this.

Sources added: 11 new (Memory-R1 arXiv, EMG-RAG arXiv, AssoMem arXiv, Outcome-Oriented Evaluation arXiv, LLM Biases arXiv, AI Biases Frontiers, Memory in AI Agents survey arXiv:2512.13564, Memory Refresh Cycles Yodaplus, Model Drift framework dev.to, M-RAG ACL 2024, utility_weighted_memory GitHub).

### 2026-03-02 — Extend research item with four self-initiated deep-dive threads (agent-memory-management-context-injection)

**Extended findings from four open threads identified as most valuable from the current research:**

1. **KGoT + MindMap: convergent architecture has concrete implementations (Finding 23)** — Knowledge Graph of Thoughts (ETH Zurich thesis) maintains a live KG that the GoT controller reads/writes during reasoning; MindMap (ACL 2024) induces GoT-style reasoning through KG-aware prompting. Minimum viable stack: Neo4j + text-embedding-3-small + PyPI graph-of-thoughts + frontier LLM.

2. **Obsidian Smart Connections as production PKM→agent memory bridge (Finding 24)** — Open-source plugin (brianpetro/obsidian-smart-connections) converts Obsidian vault to a live agent memory system using local AI embeddings (bge-micro-v2), semantic retrieval sidebar, Smart Chat, and Smart Context. Local-first, zero vendor lock-in, user-as-curator solves wiki rot.

3. **Write-path governance gap beginning to close (Finding 25)** — Three emerging approaches: Constitutional Memory (GitHub open-source, explicit write policy rules + GDPR right-to-erasure), OpenPort Protocol (arXiv:2602.20196, policy-gated writes + immutable SHA-256 audit logs + human-in-the-loop for high-risk writes), Agentic Trust Framework (CSA Feb 2026, Zero Trust staged autonomy tiers). None yet integrated into Zep/Mem0/LangMem.

4. **XAI as knowledge→wisdom bridge, closing the DIKW loop (Finding 26)** — Springer 2025 chapter identifies XAI as the mechanism enabling the knowledge→wisdom transition. Key insight: auditable reasoning graph (from GoT+KG) satisfies both governance requirements (Finding 25) AND wisdom-level memory requirements (Finding 26) — one data structure, two payoffs.

Sources added: 11 new sources covering KGoT, MindMap ACL 2024, text+KG embeddings in RAG, Constitutional Memory, OpenPort Protocol, Agentic Trust Framework, Smart Connections, DIKW+XAI Springer 2025, IEEE DIKW 2025.

### 2026-03-02 — Extend research item with four additional threads (agent-memory-management-context-injection)

**Extended findings from comment feedback requesting four additional research threads:**

1. **Memory portability** — MCP RFC #2043 (Memory Interchange Format / MIF) proposes portable JSON/JSONL/YAML export including embeddings and KG snapshots; Google A2A protocol addresses cross-vendor agent context handoff; GDPR Article 20 establishes legal expectation for memory portability in EU. No production-ready open standard exists as of 2025.

2. **DIKW progression (Data → Information → Knowledge → Wisdom)** — applied as an evaluative lens for agent memory design. Current systems optimise for data→information transition (vector retrieval) and partially for information→knowledge (KGs). The knowledge→wisdom gap is the hardest: wisdom requires value-aligned judgment in novel contexts. Design implication: prefer knowledge-form storage (distilled insights, rules, verified inferences) over log-form (raw conversation history). Maps to progressive summarisation (Forte) and evergreen note principles (Matuschak).

3. **Obsidian/PKM principles** — atomic notes, bi-directional linking, evergreen notes (Matuschak), progressive summarisation (Forte), Maps of Content — all map structurally to agent memory architecture. Obsidian's storage model (local Markdown + Git) is exactly what GitHub Copilot and Claude Code use in production. Key insight: knowledge value comes from connection density, not entry volume — same insight behind KG retrieval outperforming flat vector search on multi-hop tasks.

4. **Word embeddings + knowledge graphs + Graph of Thoughts (GoT)** — convergent architecture: embeddings provide semantic retrieval index into the KG; KG provides relational structure embeddings lack; GoT (ETH Zurich, AAAI 2024, arXiv:2308.09687) provides reasoning framework for traversing and synthesising KG paths, with reasoning traces becoming storable memory artefacts. 62% quality improvement, 31% cost reduction over Tree of Thoughts. No documented production deployment of full convergent architecture yet.

Sources added: 12 new sources covering MCP RFC #2043, A2A protocol, New America OTI brief, Springer DIKW in AI (2024), MDPI Digital Twin DIKW, Andy Matuschak Evergreen Notes, Obsidian PKM forum, PKM at scale analysis, GoT arXiv paper, Springer KGE survey, Milvus KG/embedding explainer.

### 2026-03-02 — Extend research item with video threads (agent-memory-management-context-injection)

**Extended findings from Apoorva Joshi (MongoDB) "Building Agents That Learn" video (https://youtu.be/2JiMmye2ezg) and related sources:**

New threads followed and integrated:
1. **"Memory is context engineering" reframe** — Letta + Anthropic independently reach the same conclusion: memory design is not about database selection but about which tokens are in the context window at each inference step. The design question is: Write/Select/Compress/Isolate strategies.
2. **LangChain's four context engineering operations** (Write/Select/Compress/Isolate) — a practical taxonomy that unifies all memory techniques and maps to four failure modes: context poisoning, context distraction, context confusion, context clash.
3. **Context rot (Chroma Research 2025)** — LLM accuracy degrades non-uniformly as context length increases, even before the window limit. All major model families affected. Larger context windows are not a substitute for good context engineering.
4. **Cognition "Don't Build Multi-Agents" vs Anthropic multi-agent** — Both camps independently identified memory/context management as the #1 agent reliability challenge. Cognition: context engineering is #1 job for agent engineers. MongoDB synthesis: both are right for different use cases (deep research vs coding/dialogue).
5. **Sleep-time compute (Letta + UC Berkeley, arXiv:2504.13171)** — asynchronous background memory consolidation, 5x cost reduction, 18% accuracy improvement on stateful benchmarks. Most architecturally novel 2025 advance.
6. **MemoryOS (BAI-LAB, EMNLP 2025 Oral, arXiv:2506.06326)** — three-tier OS-inspired hierarchy, +49.11% F1 / +46.18% BLEU-1 on LoCoMo vs GPT-4o-mini. Largest absolute improvement of any evaluated system.
7. **Claude Code's hybrid production pattern** — CLAUDE.md up-front (procedural memory) + just-in-time grep/glob retrieval + auto-compact at 95% context. Current production gold standard for coding agents.

Sources added: 9 new sources including the MongoDB article, Letta blog, Anthropic context engineering article, LangChain context engineering blog, Cognition blog, Chroma context rot paper, sleep-time compute arXiv paper, MemoryOS arXiv paper, and the video itself.

### 2026-03-02 — Complete research item (agent-memory-management-context-injection)

**Completed:**

Research item:
- `Research/completed/2026-03-02-agent-memory-management-context-injection.md` — completed; structured findings covering: full taxonomy of five memory architecture tiers (in-context, vector/RAG, episodic/temporal graph, hybrid, structured paging); RAG gap analysis — statelessness, staleness, conflicting knowledge, absent write-path governance; survey of six major systems (Zep/Graphiti, Mem0, LangMem, MemGPT/Letta, Cognee, GraphRAG) with maturity, scoping, and governance assessment; latency/cost profiles (in-context linear growth vs vector 1–50ms vs graph 10–100ms); scoping mechanisms (isolation vs namespace filtering, trade-offs); the wiki rot failure mode and TTL/temporal validity as countermeasures; governance gap — no open-source system has write-path access control or audit trails; production deployment patterns (GitHub Copilot repo-scoped opt-in memory, Cursor memory-bank markdown files, Devin structured memory folders); quality benchmark landscape (LOCOMO, LongMemEval, EverMemOS 92.3%, Zep 94.8% DMR).

Sources consulted:
- https://arxiv.org/abs/2310.08560 (MemGPT/Letta paging model paper)
- https://arxiv.org/abs/2501.13956 (Zep temporal knowledge graph paper, Jan 2025)
- https://arxiv.org/abs/2504.19413 (Mem0 paper, Apr 2025)
- https://arxiv.org/abs/2410.10813 (LongMemEval benchmark)
- https://github.com/snap-research/LoCoMo (LoCoMo benchmark)
- https://github.blog/ai-and-ml/github-copilot/building-an-agentic-memory-system-for-github-copilot/ (GitHub Copilot agentic memory)
- https://aws.amazon.com/blogs/security/the-agentic-ai-security-scoping-matrix-a-framework-for-securing-autonomous-ai-systems/ (AWS governance framework)
- https://microsoft.github.io/graphrag/ (GraphRAG)
- https://langchain-ai.github.io/langmem/ (LangMem SDK)
- Atlassian Confluence lifecycle management and knowledge rot community sources

### 2026-03-02 — Start research item (agent-memory-management-context-injection)

**Started:**

- `Research/in-progress/2026-03-02-agent-memory-management-context-injection.md` — moved from backlog to in-progress. Covers the full landscape of agent memory architectures beyond RAG: latency trade-offs, knowledge scoping (session/team/repo/role/task), governance and provenance, quality testing, distribution of recall tooling, and the "ungardened wiki" failure mode. Systems to survey: MemGPT/Letta, Zep, Mem0, LangMem, Cognee/Graphiti, and GraphRAG.
### 2026-03-02 — New backlog item (research-review-ci-step) and new research item (research-quality-assurance-methodology)

**Added:**

- `BACKLOG.md` W-0031 — open item for a research review CI step. The step will apply citation-discipline, speculation-control, and remove-ai-slop skills as automated gates on completed research items. Blocked on the research item below providing the automatable-vs-agent-reasoning split and design guidance.
- `Research/backlog/2026-03-02-research-quality-assurance-methodology.md` — high-priority research item. Question: what methodology moves research reliably from information gathering through to applied knowledge and wisdom, and which steps can be automated in CI? Covers: skills gap analysis (what existing skills miss), peer review as a distinct quality dimension, integration skill (cross-item synthesis), the information→knowledge→wisdom pipeline (DIKW, Nonaka SECI, Bloom's taxonomy), applicability testing, CI pipeline design (automatable vs agent-reasoning vs human-only), and whether `peer-review` and `integration` skills should be added to `davidamitchell/Skills`. The two items reference each other: W-0031 depends on findings from this research item; this item calls out W-0031 as the downstream consumer.

### 2026-03-02 — New backlog item: AI capability is not a data problem

**Added:**

- `Research/backlog/2026-03-02-ai-not-a-data-problem.md` — High-priority research item making the case that organisational AI capability should not be owned by or coupled to the data/analytics department or data platform. Covers: technical NFR mismatch (HADR, fine-grained authz, operational SLAs), API layer as the correct agent integration point (MCP, API gateways, STS token exchange, DID, zero-trust), knowledge vs. data distinction, organisational design (cross-functional AI capability spanning IT/business/HR/legal/regulatory), skills gap between data/analytics and API/platform engineering disciplines, and a structured tradeoff analysis of coupled vs. decoupled models. Sources span Martin Fowler/Data Mesh, NIST AI RMF, RBNZ, OAuth 2.0 RFC 8693, W3C DID spec, CNCF Zero Trust, OWASP API Security, and McKinsey/Gartner organisational AI research.
### 2026-03-02 — New backlog item (integrative-framework-agent-decision-making)

**Added:**

- `Research/backlog/2026-03-02-integrative-framework-agent-decision-making.md` — **high priority**. Integrative framework for agent decision-making. Covers: operationalising the DIKW (Data → Information → Knowledge → Wisdom) hierarchy in agentic systems; intent as a structured construct (goals, objectives, constraints, desired outcomes) and mechanisms for prioritising conflicting intents; catalogue of enterprise knowledge domains agents must integrate (regulations, government policy, organisational mission and values, BU strategy, technical/financial constraints, risk tolerance, policies, standards, guardrails, processes); conflict resolution mechanisms (precedence hierarchies, confidence-weighted arbitration, explainable justification traces); integration with memory architecture findings; alignment principles ensuring components reinforce intent-driven decisions; practical playbook for operationalising agents as decision-support systems. Depends on: `2026-03-02-agent-memory-management-context-injection.md` (memory architecture) and `2026-03-01-agent-lsp-policy-enforcement.md` (policy guardrails). Cross-references: DIKW literature (Ackoff 1989, Rowley 2007), Nonaka & Takeuchi SECI model, Simon bounded rationality, NIST AI RMF, EU AI Act, Constitutional AI, GraphRAG.

**Existing items cross-referenced (not duplicated):**
- `Research/backlog/2026-03-02-agent-memory-management-context-injection.md` — memory architecture dependency; findings to be integrated when complete
- `Research/completed/2026-03-01-agent-lsp-policy-enforcement.md` — prior findings on policy guardrails and governance enforcement
### 2026-03-03 — Research Loop (ai-control-testing-and-assurance)

**Completed:**

Research item:
- `Research/completed/2026-02-28-ai-control-testing-and-assurance.md` — completed; AI-assisted control testing is commercially active in 2024–2025 with a tiered vendor landscape (AuditBoard, ServiceNow, KPMG Clara, EY.ai). Disclosed outcomes include 60% faster audit cycles and 90% documentation burden reductions. Regulatory standard-setters (IAASB, PCAOB, IIA) are updating frameworks but have not yet unconditionally accepted AI-generated assurance evidence as sufficient; human oversight remains mandatory. The RBNZ has flagged AI financial stability risks but published no AI-specific assurance guidance, leaving existing BS11 outsourcing and operational risk frameworks as the applicable NZ regime.

Sources consulted:
- https://www.iaasb.org/publications/technology-position-statement (IAASB Technology Position Statement, October 2024)
- https://auditboard.com/blog/auditboard-launches-accelerate-delivering-enterprise-grade-ai-automation-for-grc-teams (AuditBoard Accelerate GRC AI launch)
- https://www.rbnz.govt.nz/hub/publications/financial-stability-report/2025/may/ai-pre-release/rise-of-the-machines (RBNZ FSR AI pre-release, May 2025)

---

### 2026-03-03 — Research Loop (youtube-transcript-fetcher)

**Completed:**

Research item:
- `Research/completed/2026-02-27-youtube-transcript-fetcher.md` — completed; the YouTube transcript fetcher port is fully operational with Atom-feed-based channel discovery (no API key required), a three-tier transcript fallback chain, and 18 passing unit tests. The `fetch-transcript.yml` workflow handles disk persistence for the owner's web-only access pattern. Bulk historical backlog fetch beyond the Atom feed's ~15-video window remains an open gap addressed by separate backlog items.

Sources consulted:
- https://github.com/jdepoix/youtube-transcript-api (library documentation)
- https://github.com/davidamitchell/Research/blob/main/src/fetchers/youtube.py (ported implementation)
- https://github.com/davidamitchell/Research/blob/main/.github/workflows/fetch-transcript.yml (workflow for disk persistence)

---

### 2026-03-02 — New backlog items (search, interaction, and distribution)

**Added:**

Four new backlog items covering the gaps in indexing/search improvements, interaction methods, and distribution of research results:

- `Research/backlog/2026-03-02-semantic-full-text-search.md` — **high priority**. Semantic and full-text search over the research corpus. Covers: SQLite FTS5 (BM25), hybrid BM25 + Model2Vec + sqlite-vec + RRF (following the pattern identified in `2026-03-01-context-mode-llm-context-compression.md`), CLI `research search` command, chunking strategy for research items, incremental hash-based re-indexing. Cross-references: `2026-02-27-indexing-and-tracking-method.md` (prior indexing decision; vector search explicitly deferred), `2026-02-27-local-database.md` (database options), `2026-03-01-context-mode-llm-context-compression.md` (hybrid retrieval pattern Key Finding 6).

- `Research/backlog/2026-03-02-chat-conversational-interface.md` — **high priority**. Conversational/chat interface for querying the research corpus. Covers: MCP server with `search_research` + `get_research_item` tools, GitHub Copilot extension approach, CLI chatbot wrapping the search layer, grounding and hallucination prevention, cross-reference navigation. Depends on: `2026-03-02-semantic-full-text-search.md` (search layer). Cross-references: `2026-02-27-interface-and-delivery.md` (upstream item; MCP mentioned but not designed), `2026-03-01-context-mode-llm-context-compression.md` (MCP server design pattern: compact summary + queryable store + drill-down tools).

- `Research/backlog/2026-03-02-slack-msteams-research-integration.md` — **medium priority**. Slack and MS Teams integration for research delivery and capture. Covers: outbound delivery via Incoming Webhooks (GitHub Actions step triggered by `Research/completed/**` push), digest mode (weekly summary), inbound capture via slash commands or Power Automate flows, query integration with the conversational interface. Note: new secrets (`SLACK_WEBHOOK_URL` or `TEAMS_WEBHOOK_URL`) will require owner approval per AGENTS.md constraints. Cross-references: `2026-02-27-interface-and-delivery.md`, `2026-03-01-github-wiki-research-content.md` (same trigger pattern to reuse).

- `Research/backlog/2026-03-02-ios-shortcuts-research.md` — **medium priority**. iOS Shortcuts for research capture and query. Covers: Share Sheet shortcut to add a URL or title to the backlog (GitHub API direct file creation vs. issue creation), Siri hands-free dictation, wiki quick-access shortcut, search/query shortcut via `workflow_dispatch`. Authentication via fine-grained PAT in iOS Keychain. Cross-references: `2026-02-27-simple-process-for-adding-research-item.md` (existing capture paths; iOS Shortcuts is the missing third path), `2026-03-01-github-wiki-research-content.md` (wiki as readable iOS delivery channel).

**Existing items cross-referenced (not duplicated):**
- `Research/backlog/2026-02-27-interface-and-delivery.md` — broader interface question; new items are focused sub-topics
- `Research/backlog/2026-02-27-local-database.md` — database technology choice; `semantic-full-text-search` is the search UX layer on top
- `Research/backlog/2026-02-27-local-index-vs-reference.md` — storage policy; upstream of search
### 2026-03-02 — New research item (transaction-costs)

**Completed:**

- `Research/completed/2026-03-02-transaction-costs.md` — completed; structured findings covering: Coase (1937, 1960) — firm as transaction-cost-minimising institution, the Coase Theorem; Williamson (1975, 1985) — asset specificity, uncertainty, frequency as transaction dimensions, governance-structure choice (market / hybrid / hierarchy), bounded rationality and opportunism; North (1990) — institutions as "rules of the game", path dependence in institutional change; Ostrom (1990) — 8 design principles for commons governance, polycentric governance; Munger — politics as a transaction-cost environment. Speculative integration: SWE (make-vs-buy as Williamson governance choice, code review transaction costs, specification as incomplete contract), AI agent design (single-agent firm vs multi-agent market, Ostrom's principles for agent memory, North's path dependence in training distributions), knowledge management (documentation as commons, Ostrom design principles for wikis, informal vs formal institutions), context engineering (Coase Theorem restated for context construction, asset specificity of session context, RAG/memory/full-context as market/hybrid/hierarchy governance choice, Munger political lens on system-prompt control).

### 2026-03-02 — New backlog item (agent-memory-management-context-injection)

**Added:**

- `Research/backlog/2026-03-02-agent-memory-management-context-injection.md` — new high-priority backlog item. Covers the full landscape of agent memory architectures beyond RAG: latency trade-offs, knowledge scoping (session/team/repo/role/task), governance and provenance, quality testing, distribution of recall tooling, and the "ungardened wiki" failure mode. Systems surveyed include MemGPT/Letta, Zep, Mem0, LangMem, Cognee/Graphiti, and GraphRAG.
### 2026-03-02 — Session 15 (GitHub wiki publishing — W-0030)

**Completed:**

Research item:
- `Research/completed/2026-03-01-github-wiki-research-content.md` — completed; findings establish: GitHub wiki is a separate git repo (`{repo}.wiki.git`); `GITHUB_TOKEN` with `contents: write` is sufficient (no PAT); pages are flat (no subdirectories); `Home.md`, `_Sidebar.md`, `_Footer.md` are the navigation primitives; full-rebuild approach (delete all pages, regenerate) is correct at current volume; YAML front-matter must be stripped before publishing.

Implementation (W-0030):
- `src/wiki/__init__.py` — wiki module init
- `src/wiki/publish.py` — `load_frontmatter`, `strip_frontmatter`, `page_name`, `generate_home`, `generate_sidebar`, `publish`; full-rebuild approach; callable as `python -m src.wiki.publish <completed_dir> <wiki_dir>`
- `.github/workflows/publish-wiki.yml` — triggers on push to `main` (paths: `Research/completed/**`) and `workflow_dispatch`; checks out wiki with `GITHUB_TOKEN`; runs publish script; commits and pushes
- `tests/test_wiki.py` — 24 tests covering all functions and integration
- `BACKLOG.md` — W-0030 added as done
- `PROGRESS.md` — updated

**Setup required:** Owner must enable the wiki once via repository Settings → Features → Wikis before the first workflow push will succeed.

### 2026-03-02 — Research Loop (simple-process-for-adding-research-item)

**Completed:**

Research item:
- `Research/completed/2026-02-27-simple-process-for-adding-research-item.md` — completed; two capture paths identified: `python -m src.main research add "<title>"` (already implemented) for agents, and a GitHub issue form + Actions workflow for the owner who operates via GitHub website/iOS app only. The Zettelkasten capture-first principle validates deferring all metadata except title to the start step.

Sources consulted:
- https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests/syntax-for-issue-forms (GitHub issue form syntax for mobile-friendly capture)
- https://deepread.com/the-simple-zettelkasten/ (Zettelkasten inbox and minimum-friction capture principles)
- https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests/configuring-issue-templates-for-your-repository (GitHub issue template configuration)

### 2026-03-02 — Research Loop (research-backlog-vs-repo-improvement-backlog)

**Completed:**

Research item:
- `Research/completed/2026-02-27-research-backlog-vs-repo-improvement-backlog.md` — completed; two-location file system separation (`Research/backlog/` + `BACKLOG.md`) confirmed as the correct design for keeping research questions separate from repo improvement work. Convention is documented at three levels: file system location, header notes in each file, and AGENTS.md Non-Negotiable Constraints. Cross-reference mechanism flows one-way via the `output: [backlog-item]` field.

Sources consulted:
- https://github.com/davidamitchell/Research/blob/main/BACKLOG.md (repo improvement backlog format and header note)
- https://github.com/davidamitchell/Research/blob/main/Research/README.md (research workflow and separation documentation)
- https://github.com/davidamitchell/Latest-developments-/blob/main/BACKLOG.md (comparison: single-type backlog in a pipeline repo)

### 2026-03-02 — Research Loop (information-synthesis-entropy)

**Completed:**

Research item:
- `Research/completed/2026-02-27-information-synthesis-entropy.md` — completed; three-stage synthesis pipeline recommended: entropy-guided extraction → semantic deduplication → Chain of Density prompting. Shannon entropy, Information Bottleneck, and MDL all converge on the same principle: discard the predictable, preserve the novel. GraphRAG is the right architecture for multi-source synthesis at scale; CoD prompting is the immediately implementable technique.

Sources consulted:
- https://arxiv.org/abs/2309.04269 (Adams et al. 2023 — Chain of Density prompting paper)
- https://en.wikipedia.org/wiki/Information_bottleneck_method (Information Bottleneck method overview)
- https://www.microsoft.com/en-us/research/blog/graphrag-unlocking-llm-discovery-on-narrative-private-data/ (GraphRAG — Microsoft Research)

### 2026-03-02 — Session 14 (Research loop safety controls + COPILOT_GITHUB_TOKEN)

**Completed:**

- W-0029: Added runaway loop safety controls to `.github/workflows/research-loop.yml`:
  - Renamed secret `GH_TOKEN` → `COPILOT_GITHUB_TOKEN` (owner confirmed secret is set with this name)
  - Added `timeout-minutes: 90` hard ceiling on the job
  - Changed `max_items` from free-text to constrained dropdown (choices 1–5)
  - Added `HARD_MAX_ITERATIONS=10` shell guard (independent of `max_items`)
  - Added consecutive-failure abort (`FAILURE_THRESHOLD=2`)
  - Added 30-second inter-iteration sleep (`INTER_ITERATION_SLEEP=30`)
  - Added `set -euo pipefail` for fail-fast shell behaviour
- `tests/test_research_loop.py`: 25 tests proving workflow structure, safety controls, prompt content, backlog counting logic, and end-to-end loop cycle
- `docs/adr/0004-autonomous-research-loop.md`: ADR documenting design decisions, safety controls, and rejected alternatives (Claude Code CLI, unlimited `max_items`, PR-per-item model)
- `docs/adr/README.md`: ADR index updated with ADR-0004
- `AGENTS.md`: Updated credentials table (`COPILOT_GITHUB_TOKEN`), research loop docs, safety controls summary
- `BACKLOG.md`: W-0029 added as done

### 2026-03-02 — Session 13 (GitHub Specify / Ralph loop / Lisa planning research)

**Completed:**

Research item:
- `Research/completed/2026-03-01-github-specify-ralph-loop-lisa-planning.md` — completed; structured findings covering: Ralph Wiggum Technique origin (Geoffrey Huntley, July 2025, viral Dec 2025); three-phase workflow (Specify→Plan→Build); spec format (one Markdown per Topic of Concern, "one sentence without and" test); context management discipline (one task per loop, 40-60% smart zone, main agent as scheduler + subagents for expensive work); back-pressure as proof (tests/lint must pass before commit; dual-condition exit gate in frankbria implementation); Lisa as planning + persistent memory archetype solving the Groundhog Day Problem (knowledge graph via Graphiti + MCP + Neo4j, Claude Code hooks for session-start/stop extraction); GitHub Copilot Agent mode as the practical entry point for this repo's owner (issue assignment → draft PR, no local shell needed); evolutionary framing (Ralph = (1,1) evolutionary strategy, LLM mutation, tests as fitness); active inference structural equivalence (spec = prior, test result = observation, loop = action until surprise = 0)

Sources consulted:
- https://ghuntley.com/ralph/ (primary source — Geoffrey Huntley's original article)
- https://github.com/ClaytonFarr/ralph-playbook (community playbook with detailed loop mechanics)
- https://github.com/frankbria/ralph-claude-code (Claude Code implementation with dual-condition exit gate, v0.11.5)
- https://aibit.im/blog/post/deploying-the-ralph-wiggum-technique-a-step-by-step-tutorial (step-by-step tutorial with prompt templates)
- https://dev.to/tonycasey/why-ralph-wiggum-needs-lisa-23nm (Lisa motivation: Groundhog Day Problem + knowledge graph architecture)
- https://ianreppel.org/ralph-wiggum-as-a-degenerate-evolutionary-search/ (evolutionary framing; (1,1) strategy analysis)
- https://github.blog/changelog/2025-12-18-github-copilot-now-supports-agent-skills/ (GitHub Agent Skills announcement)
- https://github.blog/news-insights/product-news/github-copilot-meet-the-new-coding-agent/ (Copilot coding agent announcement)

**Key insight for this repo:** This repo's `AGENTS.md` + `.github/skills/` + `tests/` + `pyproject.toml` already satisfies the Ralph prerequisites. The only gaps are `specs/` folder (specs per JTBD topic), `IMPLEMENTATION_PLAN.md` (task list), and `loop.sh` (outer bash loop). For the GitHub-only owner, Copilot Agent mode (assign detailed issue → Copilot opens draft PR) is the practical entry point — no local shell or `--dangerously-skip-permissions` required.

### 2026-03-01 — Session 12 (Context Mode research)

**Completed:**

Research item:
- `Research/completed/2026-03-01-context-mode-llm-context-compression.md` — completed; structured findings covering: the two-sided context consumption problem (Cloudflare Code Mode for definitions vs Context Mode for outputs); Context Mode's architecture (sandboxed subprocess execution, SQLite FTS5 + BM25 knowledge base, subagent routing, progressive search throttling); quantified compression ratios (315 KB → 5.4 KB, 98% reduction; sessions from ~30 min to ~3 hours); the hard architectural boundary — Context Mode cannot intercept MCP tool responses (JSON-RPC bypass, no PostToolUse hook, empirically confirmed by HN commenter); BM25 limitation for structured tool output and hybrid retrieval improvement (Model2Vec + sqlite-vec + FTS5 + RRF); prompt cache preservation argument; broader context management frontier (backtracking, context trees, subprocess isolation, agentic self-management)

Sources consulted:
- https://mksg.lu/blog/context-mode (primary article)
- https://news.ycombinator.com/item?id=47193064 (HN discussion, empirical MCP interception test)
- https://github.com/mksglu/claude-context-mode (GitHub README, architecture detail)
- https://blog.cloudflare.com/code-mode-mcp/ (Code Mode input-side compression reference)

**Key insight for this repo:** This repo uses 10 MCP servers. Context Mode cannot intercept any of their outputs — MCP responses (filesystem, memory, git, arxiv, etc.) go directly to model context via JSON-RPC. For Claude Code sessions on this repo, output compression requires server-side implementation in each MCP server or reliance on built-in tool compression only.
### 2026-03-01 — Session 12 (new backlog item — agent LSP policy enforcement)

**Completed:**

- `Research/backlog/2026-03-01-agent-lsp-policy-enforcement.md` — research item on guiding headless autonomous agents via LSP-like mechanisms for org policy conformance (security, architectural, engineering standards); key focus: identifying the "LSAP"/"LASP" acronym and protocol, surveying whether headless agents can act as LSP clients, mapping the gap between CI/pre-commit gates and in-loop real-time feedback; priority high
### 2026-03-01 — Session 12 (GitHub wiki backlog item)

**Completed:**

- `Research/backlog/2026-03-01-github-wiki-research-content.md` — new backlog item: researching how to publish completed research items to the GitHub wiki for easier reading on the GitHub website and iOS app. Covers: GitHub wiki constraints, publish pipeline design (Actions workflow, front-matter stripping, index generation), incremental vs full-rebuild approach, and navigation structure (tag index, date-sorted, topic groups). Priority: medium. Output types: tool, knowledge, backlog-item.
### 2026-03-01 — Session 12 (Research backlog item — GitHub Specify / Ralph loops / Lisa planning)

**Completed:**

Research items:
- `Research/backlog/2026-03-01-github-specify-ralph-loop-lisa-planning.md` — added backlog item covering: GitHub's "Specify" concept (spec-first AI development), the Ralph Wiggum Technique (autonomous implementation loop), Lisa planning (planning subagent pattern), proof-driven development as the unifying methodology, and the connection to active inference / free energy minimisation. Approach decomposes into six sub-questions; seven primary sources identified (ghuntley/how-to-ralph-wiggum, ClaytonFarr/ralph-playbook, frankbria/ralph-claude-code, Geoffrey Huntley writing, GitHub Copilot Agent docs, GitHub blog).

---

### 2026-03-01 — Session 11 (Tavily MCP integration)

**Completed:**

- `.mcp.json` — added `tavily` server entry (`npx -y tavily-mcp@latest`, `TAVILY_API_KEY` env var)
- `.github/mcp.json` — added `tavily` server entry (same, with `type: "stdio"`)
- `.env.example` — added `TAVILY_API_KEY=tvly-...` entry under Search section
- `AGENTS.md` — Server Reference table: added `tavily` row (10 servers now); updated session-start availability table to include `tavily` in unavailable list for cloud/Copilot runner and in "missing secrets" list for local dev; updated substitutions note (`brave_search` / `tavily` → built-in web search); added `tavily` to "Using MCP in research tasks" section with guidance on when to prefer it over `brave_search` (extracted content vs links)

Tavily MCP provides: `tavily-search` (real-time web search), `tavily-extract` (content extraction from URLs), `tavily-map` (structured site map), `tavily-crawl` (systematic site crawl). Requires `TAVILY_API_KEY` repository secret.

---

### 2026-03-01 — Session 10 (Issue consolidation — Group A: #11, #12, #13)

**Completed:**

Group A — AGENTS.md + config improvements (all changes in one PR per consolidation recommendation):

- `.mcp.json` and `.github/mcp.json` — replaced hardcoded `/workspaces/Research` filesystem path with `"."` (current working directory); works across Codespaces, agent runners, and local dev without env var config (#11, Bug 1)
- `AGENTS.md` — Repository Layout section: added `Research/transcripts/` (fetch-transcript workflow output) and `state/` (StateStore JSON file) entries (#13, Gap 4)
- `AGENTS.md` — Agent Skills section: expanded table to include per-agent invocation column (Claude Code slash commands vs Copilot by-reference); added submodule setup note (`git submodule update --init`); added Skills Invocation section covering Claude Code, Copilot, and fallback behaviour (#12)
- `AGENTS.md` — MCP server table: replaced "Codespaces secret" with "repository secret or `.env`" for `brave_search` and `github` (#11, Bug 2)
- `AGENTS.md` — MCP section: added Session-start MCP availability check section with per-environment availability table and substitution guide (#11, Bug 3)
- `AGENTS.md` — MCP "Using MCP in research tasks": removed Codespaces-specific language; updated filesystem note to reflect `"."` path (#11)
- `AGENTS.md` — Mini-Retro section: added feedback loop steps — update AGENTS.md, add BACKLOG.md item, record in PROGRESS.md (#13, Gap 1)
- `AGENTS.md` — Added "When to Update AGENTS.md" section (new) (#13, Gap 3)
- `AGENTS.md` — Added "When the Backlog Is Empty" section (new) (#13, Gap 2)
- `README.md` — added `git submodule update --init` to Quick Start (#12)

Issues closed or addressed:
- #10 — already closed (incorporated into #11); confirmed
- #11 — all three bugs fixed
- #12 — all four problems addressed (README setup step, invocation section, agent-specific notes, fallback instruction)
- #13 — all four gaps addressed (Mini-Retro loop, empty-backlog protocol, update trigger, directory layout)

**Remaining (Group B — separate PR to `davidamitchell/Skills`):**
- #8 — Research skill improvements (7 gaps identified post AI strategy research)
- #9 — Strategy-author skill improvements (7 gaps identified)

These require changes to the `davidamitchell/Skills` repository and cannot be addressed in this repo's PR.

### 2026-02-28 — Session 9 (AI Strategy research)

**Completed:**

Research items:
- `Research/completed/2026-02-28-ai-strategy.md` — completed; structured findings covering: global AI strategy survey (8 common pillars, six jurisdictions); NZ "Investing with Confidence" strategy (July 2025, MBIE-led, light-touch, $76B GDP estimate); NZ agency landscape (MBIE, DIA, RBNZ, Privacy Commissioner — fragmented, no single AI regulator); NZ political positions (National-led: pro-growth light-touch; Labour: cautious rights-based; Greens: strong safeguards); NZ case law status (thin — Wikeley v Kea Investments [2024] NZCA 609; no binding case on automated government decisions); policy framework comparison (EU AI Act / NIST AI RMF / ISO 42001 / DORA); use-case typology (4 types: augmentation → fully agentic BUs); exploit/explore strategic framing

New backlog items added:
- `Research/backlog/2026-02-28-ai-strategy-business-efficiency-examples.md` — examples of AI strategies focused on business efficiency outcomes
- `Research/backlog/2026-02-28-ai-strategy-swe-focus.md` — AI strategies targeting software engineering productivity
- `Research/backlog/2026-02-28-ai-strategy-risk-reduction-focus.md` — AI strategies with risk reduction as primary objective
- `Research/backlog/2026-02-28-ai-strategy-security-focus.md` — AI strategies focused on security (AI-enhanced threats + AI system security)
- `Research/backlog/2026-02-28-rbnz-ai-supervisory-expectations.md` — RBNZ's specific AI supervisory stance and gap analysis vs comparators
- `Research/backlog/2026-02-28-exploit-explore-ai-portfolio-framework.md` — practical decision framework for exploit vs explore AI portfolio classification
- `Research/backlog/2026-02-28-ai-control-testing-and-assurance.md` — AI automating control testing, control gap identification, and policies/standards reviews; vendor and regulatory landscape
- `Research/backlog/2026-02-28-ai-line-1-line-2-risk-agents.md` — who is building line 1 and line 2 risk agents; architecture, governance, and accountability patterns

GitHub issues raised:
- Issue #8: Research skill retro and improvement suggestions (post AI strategy research)
- Issue #9: Strategy-author skill improvement suggestions
- Issue #10: MCP servers unavailable in agent environment (brave_search, arxiv, filesystem, memory, sequential_thinking)
- Skills submodules re-initialised (`git submodule update --init`); research, strategy-author, and remove-ai-slop skills applied
- MCP servers (brave_search, arxiv, filesystem, sequential_thinking, memory) not available in this agent environment; web_search used as substitute
- Raised GitHub issues for MCP availability gaps

**Notes:**
- All outputs reviewed against remove-ai-slop skill: predictable transitions removed, structural variety applied, alignment padding eliminated, direct declarative language used throughout
- Research skill methodology applied: recursive decomposition, evidence sufficiency check, consistency loop, multi-lens analysis (technical, regulatory, economic, political, behavioural)

### 2026-02-28 — Session 8 (Epic 3 implementation — W-0021, W-0022)

**Completed:**

- `src/state.py` — `StateStore` class:
  - `is_processed(url)` — O(1) lookup in in-memory dict
  - `record(item)` — stores `fetched_at`, `title`, `source_id`; writes atomically via `tempfile.mkstemp` + `os.replace`
  - `processed_urls()` — returns full set of processed URLs
  - Corrupt / missing state file is handled gracefully (starts empty, logs warning)
- `src/main.py` — `_fetch_youtube` now instantiates `StateStore`, skips already-processed URLs (`[skip]` message), records new items after printing
- `tests/test_state.py` — 12 tests: empty store, load existing, corrupt file, is_processed, record (disk + dir creation + multiple + overwrite), round-trip reload
- `BACKLOG.md` — W-0021 and W-0022 marked done
- `PROGRESS.md` — Epic 3 status: Done (3/3 slices)

Research items:
- `Research/completed/2026-02-28-jevons-paradox.md` — completed; structured findings covering: Jevons (1865) coal/steam mechanics; historical sector evidence (lighting, automobiles, computing); counter-examples (CFCs, leaded petrol, saturated markets); current AI coding commentary (Proxify, MomoView, Kamiwaza); speculative 1/5/10-year framework for code production (explicitly labelled as inference/speculation)
- `Research/completed/2026-02-28-predictive-processing-active-inference.md` — completed; findings covering: Rao & Ballard (1999) bidirectional cortical model; Clark (2016) PP thesis; active inference as prediction fulfillment; precision weighting as attention; Friston's FEP — empirical status (well-supported as modelling toolkit; contested as grand unified theory); falsifiability objection; applications in computational psychiatry and AI

**Notes:**
- 68 tests pass; `make check` clean
- `python -m src.main fetch youtube --video <url>` now deduplicates automatically; re-running shows `[skip]` for each already-processed item

---



**Completed:**

Research items:
- `Research/completed/2026-02-27-indexing-and-tracking-method.md` — completed; findings recommend JSON state file (`state/index.json`) for URL-based deduplication + YAML front-matter for item metadata; SQLite and vector stores deferred with clear migration trigger criteria

System improvements:
- `docs/adr/0003-indexing-and-tracking-approach.md` — ADR documenting the chosen approach, rejected alternatives, and migration trigger; unblocks Epic 3
- `docs/adr/README.md` — index updated
- `BACKLOG.md` — W-0020 marked done
- `PROGRESS.md` — Epic 3 status updated to "In Progress (1/3 slices)"

**MCP/Skills status:**
- Skills submodules initialized via `git submodule update --init`; `research` skill read and applied for evidence gathering and synthesis structure
- `web_search` used for research (analogous to `brave_search` MCP); `web_fetch` available
- `brave_search`, `arxiv`, `filesystem`, `sequential_thinking`, and `memory` MCP servers are not available in this agent environment (no Codespaces, no API keys); noted below in Next Steps

**Notes:**
- Epic 3 (indexing) is now unblocked: W-0021 (implement JSON state) and W-0022 (dedup logic) can proceed
- Skills submodules require `git submodule update --init` after a fresh clone in this CI environment; they are not auto-initialized

---

### 2026-02-27 — Session 1

**Completed:**
- `README.md` — updated with project description and quick start
- `AGENTS.md` — comprehensive agent instructions adapted from `davidamitchell/Latest-developments-`; research-specific workflow (add/start/complete items), output types, skills table, MCP config notes
- `BACKLOG.md` — repo improvement backlog, separate from research item backlog
- `PROGRESS.md` — this file
- `pyproject.toml`, `requirements.txt`, `.python-version` — Python 3.11 project config
- `.env.example` — example env vars
- `Makefile` — dev targets matching reference repo
- `.gitmodules` — skills submodule references (`davidamitchell/Skills`)
- `.github/copilot-instructions.md` — thin stub pointing to `AGENTS.md`
- `.github/mcp.json` — MCP server config for GitHub Copilot Agent
- `.mcp.json` — MCP server config for Claude Code and other agents
- `.devcontainer/devcontainer.json` — Codespaces setup
- `.github/workflows/ci.yml` — lint + test CI
- `.github/workflows/sync-skills.yml` — weekly skills submodule sync
- `docs/adr/README.md` — ADR index with template
- `docs/adr/0001-use-python-as-primary-language.md` — first ADR
- `Research/README.md` — research workflow documentation
- `Research/_template.md` — template for a new research item
- `Research/backlog/` — 9 research items added from the project backlog
- `Research/in-progress/` — placeholder
- `Research/completed/` — placeholder
- `src/main.py`, `src/logger.py`, `src/research/item.py`, `src/fetchers/__init__.py` — source skeleton
- `tests/conftest.py` — test skeleton
- `config/sources.yaml` — sources config stub

### 2026-02-28 — Session 2 (kickoff backlog work)

**Completed:**

Epic 1 — Research Item Process (W-0011 to W-0015):
- `src/research/cli.py` — `add`, `list`, `start`, `complete` commands
- `src/main.py` — wired research and fetch sub-commands
- `tests/test_research_cli.py` — full test coverage of all CLI commands

Epic 2 — YouTube Transcript Fetcher (W-0016 to W-0019):
- `src/fetchers/youtube.py` — `YouTubeFetcher` implementing the `Fetcher` protocol; supports channel feeds and individual video URLs; transcript fallback to description
- `src/config.py` — `load_config()` with schema validation for all sections
- `config/sources.yaml` — updated schema: `youtube.channels` + `youtube.videos`; added `https://youtu.be/HYUoS0GkGCs` as first video to process
- `tests/test_fetchers_youtube.py` — 15 tests with all network calls mocked
- `tests/test_config.py` — 9 tests for config loading and validation

Research items:
- `Research/backlog/2026-02-28-youtube-video-HYUoS0GkGCs-concepts.md` — research item for the video

**Notes:**
- 52 tests pass, `make check` clean
- `python -m src.main fetch youtube --video https://youtu.be/HYUoS0GkGCs` is the command to pull the transcript (requires network access to YouTube)
- Epic 3 (indexing) is blocked until `Research/backlog/2026-02-27-indexing-and-tracking-method.md` is completed

---

### 2026-02-28 — Session 6 (skills submodules — W-0026)

**Completed:**

- `.github/skills` — git submodule properly initialised, pointing to `davidamitchell/Skills` at `7095c41e842f036e2241ad9ae3aa1360db04be83` (latest)
- `.claude/skills` — same submodule added for Claude Code
- `.claude/CLAUDE.md` — thin stub pointing to `AGENTS.md` (matches `Latest-developments-` pattern)
- `docs/adr/0002-agent-skills-submodule.md` — ADR documenting the submodule decision
- `docs/adr/README.md` — index updated
- `BACKLOG.md` — W-0026 added and marked done

**Root cause of the gap:** The `.gitmodules` file was created manually in Session 1 (the entries were written as plain text) but `git submodule add` was never run, so no gitlink entries were committed into the tree. The skill directories did not exist and agents had no access to the skill files.

**Notes:**
- `sync-skills.yml` already handles both submodule paths — no changes needed there
- `AGENTS.md` already documents both submodule paths and the skills table correctly — no changes needed
- Weekly Monday sync will keep both pointers current without manual intervention

---

### 2026-02-28 — Session 5 (AI Strategy backlog item — government/opposition coverage)

**Completed:**

Research items:
- `Research/backlog/2026-02-28-ai-strategy.md` — enhanced to explicitly cover NZ current government (National-led coalition) and opposition (Labour, Green Party) AI policy positions; added Approach step 3 and corresponding source entry

---

### 2026-02-28 — Session 4 (AI Strategy backlog item)

**Completed:**

Research items:
- `Research/backlog/2026-02-28-ai-strategy.md` — AI strategy research item covering global/NZ examples, NZ regulatory and policy landscape (RBNZ, DIA, MBIE, PNZ), relevant case law, policy frameworks and categorisation schemas, DORA AI capability model, use-case typology (augmentation → agentic BUs), and the exploit vs explore distinction

---

### 2026-02-28 — Session 3 (Jevons Paradox backlog item)

**Completed:**

Research items:
- `Research/backlog/2026-02-28-jevons-paradox.md` — deep-dive on Jevons Paradox mechanics, historical sector examples, counter-examples, current SWE/code-cost commentary, and a 1/5/10-year speculative framework

System improvements:
- `AGENTS.md` — added explicit "Update PROGRESS.md" step to the Research Item Workflow (add/start/complete) so agents cannot skip it
- `Research/README.md` — same update to the quick-command workflow section

---

### 2026-03-05 — H-Neurons research cluster (arXiv:2512.01797)

**Completed:**

Research items — 5-item progressive cluster branching from Gao et al. (2025) "Hallucination-Associated Neurons in LLMs":
- `Research/backlog/2026-03-05-llm-hallucination-mechanisms.md` — **foundation**: LLM hallucination types, causes, and current mitigations; must be researched before the core paper item; blocks `2026-03-05-h-neurons-in-llms`
- `Research/backlog/2026-03-05-h-neurons-in-llms.md` — **core**: the paper itself — H-Neuron identification methodology, behavioural impact (over-compliance pathway), and pre-training origins; blocks the two branch items; source list includes YouTube explainer "They solved AI hallucinations!" (https://youtu.be/1ONwQzauqkc)
- `Research/backlog/2026-03-05-h-neuron-over-compliance.md` — **branch A**: over-compliance behaviour, activation steering, inference-time monitoring, and training-time interventions; blocks `2026-03-05-h-neurons-synthesis`
- `Research/backlog/2026-03-05-h-neuron-pretraining-origins.md` — **branch B**: why H-Neurons emerge during pre-training, limits of post-training alignment, and candidate pre-training-time mitigations; blocks `2026-03-05-h-neurons-synthesis`
- `Research/backlog/2026-03-05-h-neurons-synthesis.md` — **synthesis**: unified causal chain, layered intervention map, confidence-calibrated findings, and prioritised action list for LLM reliability engineering

Dependency chain (research in this order): hallucination-mechanisms → h-neurons-in-llms → [over-compliance | pretraining-origins] → synthesis

---

## Next Steps

1. Run `python -m src.main fetch youtube --video https://youtu.be/HYUoS0GkGCs` in a networked environment to pull the transcript
2. Extract concepts from the transcript and create per-concept deep-dive research items
3. Complete each concept research item, then synthesise findings back in `2026-02-28-youtube-video-HYUoS0GkGCs-concepts.md`
4. Epic 3 — decide on indexing approach once the indexing research item is completed
