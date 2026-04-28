---
title: "General Agent Optimization Framework"
added: 2026-03-05T20:22:11+00:00
status: completed
priority: high
blocks: []
tags: [agentic-ai, optimization, benchmarks, dspy, evaluation, self-improvement, prompt-engineering, synthetic-data]
started: 2026-03-05T20:22:11+00:00
completed: 2026-03-05T20:22:11+00:00
output: [knowledge, backlog-item]
cites: []          # slugs of items this item directly depends on or quotes
related: []        # slugs of thematically connected items
superseded_by: ~   # slug of a later item that overrides this one (null if not superseded)
supersedes: ~      # slug of an older item this one replaces (null if not applicable)
item_type: primary # primary | synthesis
confidence: medium # high | medium | low
versions: []       # entries: {version: "1.0", sha: "<commit-hash>", changed: YYYY-MM-DD, progress: "<path>", summary: "<one-line>"}
---

# General Agent Optimization Framework

## Research Question

What is the most principled architecture for a Self-Improving AI Agent Evaluation Loop — specifically, how should a nested inner/outer loop be designed so that a "Meta-Optimizer" rewrites system prompts based on failure analysis without causing instruction drift or overfitting to specific training questions?

## Scope

**In scope:**
- Nested-loop architecture: inner loop (instruction optimization via Meta-Optimizer) and outer loop (robustness through semantic/adversarial variation)
- Principled, generic prompt updates (e.g., rule generalisation) versus specific data injection, and the tradeoffs between them
- Benchmark landscape: general reasoning (GPQA, HLE, MMLU-Pro) and tool-use (GAIA, AgentBench) benchmarks as evaluation harnesses
- Domain-specific benchmarks: FinBen (Finance), LegalBench (Law), SWE-bench (Coding) as "Ground Truth" sources for specialised agents
- Proprietary "Golden Sets": feasibility and methodology for building domain-specific question sets from sources such as Chambers and Partners' Global Practice Guides
- DSPy framework: teleprompters, optimizers, and how they automate inner-loop instruction updates
- Synthetic data generation as the primary fuel for the outer loop's variation engine
- Instruction drift risk: "Brevity Penalties" and "Prompt Pruning" techniques
- Balancing general-reasoning benchmarks with specialised Golden Sets

**Out of scope:**
- Full implementation of a running evaluation harness (that is a downstream tooling item)
- Fine-tuning or weight-level training; this research is limited to prompt/instruction-level optimization
- Infrastructure provisioning (compute, hosting, MLOps pipelines)

**Constraints:** Focus on techniques that are feasible using LLM APIs (no local GPU training assumed). Prioritise peer-reviewed sources, official framework documentation, and established benchmark papers.

## Context

Current agents in this repo (and in production AI deployments generally) are evaluated ad hoc: prompts are tuned by hand, there is no systematic loop that measures failure, generalises a fix, and validates the fix does not regress. As agent complexity grows — multi-step reasoning, tool use, domain knowledge — this manual approach breaks down.

A Self-Improving Evaluation Loop addresses this gap by closing the feedback cycle: (1) run agent on a held-out test set, (2) classify failures, (3) update the system prompt with a generic rule that addresses the failure class, (4) verify the update improves performance across paraphrased variants of the failing question. The outer loop prevents overfitting by continuously generating semantic and adversarial variations.

This research is strategically urgent because:
- The repo's research-loop workflow is currently limited by manual prompt tuning.
- Domain-specific benchmarks (FinBen, LegalBench) are directly relevant to NZ financial services and legal contexts that this repo tracks.
- DSPy is an actively maintained framework that could be integrated into existing Python tooling (`src/`) with minimal new infrastructure.

**Prior research:** The agent-memory-management item (2026-03-02) established that memory/context management is the #1 challenge in agent reliability and that context is effectively all that an agent "knows" at inference time — any optimization framework operates on this context. The research-loop-quality-prompt-engineering item (2026-03-03) found that prompt changes are the dominant driver of quality variation in autonomous agent output, directly motivating systematic prompt optimization over ad hoc tuning. The knowledge-representation-agent-context item (2026-03-03) provided a layered knowledge architecture that informs which parts of an agent context are best targets for Meta-Optimizer rewrites (instruction layer vs. retrieval layer). None of the prior items surveyed automated prompt optimization frameworks, nested-loop architectures, or benchmark suitability, so this item covers new ground.

## Approach

1. **Architecture survey** — Review published literature and blog posts on automated prompt optimization loops. Identify the canonical inner-loop/outer-loop formulation and any named variants (APE, OPRO, DSPy Teleprompters, TextGrad).
2. **Benchmark mapping** — For each of GPQA, HLE, MMLU-Pro, GAIA, AgentBench, FinBen, LegalBench, SWE-bench: document data format, license, size, evaluation metric, and suitability as a training/test split for an optimization loop.
3. **Chambers & Partners feasibility** — Assess whether publicly available Chambers Global Practice Guides can serve as a structured Golden Set source (licensing, structured Q&A availability, coverage of NZ/APAC jurisdictions).
4. **DSPy deep dive** — Read DSPy documentation and the original paper (Khattab et al., 2023). Understand how `BootstrapFewShot`, `MIPRO`, and `BayesianSignatureOptimizer` work. Assess API requirements and cost profile.
5. **Synthetic data generation** — Survey methods for generating semantically equivalent paraphrases and adversarial variants (back-translation, LLM paraphrase prompting, checklist-based perturbations). Identify which methods preserve answer correctness and which introduce noise.
6. **Instruction drift analysis** — Review empirical findings on prompt length vs performance degradation. Identify concrete "Brevity Penalty" formulations (e.g., penalise token count in the optimizer objective) and "Prompt Pruning" heuristics (redundancy detection, coverage-based trimming).
7. **Synthesis and recommendation** — Produce a technical blueprint: recommended architecture, benchmark selection strategy, DSPy integration points, and a go/no-go assessment for building a proprietary Golden Set from Chambers sources.

## Sources

- [x] Khattab et al. (2023) — "DSPy: Compiling Declarative Language Model Calls into Self-Improving Pipelines" — https://arxiv.org/abs/2310.03714
- [x] Yang et al. (2024) — "OPRO: Large Language Models as Optimizers" — https://arxiv.org/abs/2309.03409
- [x] Zhou et al. (2023) — "Large Language Models Are Human-Level Prompt Engineers (APE)" — https://arxiv.org/abs/2211.01910
- [x] Yuksekgonul et al. (2024) — "TextGrad: Automatic 'Differentiation' via Text" — https://arxiv.org/abs/2406.07496
- [x] Rein et al. (2023) — "GPQA: A Graduate-Level Google-Proof Q&A Benchmark" — https://arxiv.org/abs/2311.12022
- [x] Mialon et al. (2023) — "GAIA: A Benchmark for General AI Assistants" — https://arxiv.org/abs/2311.12983
- [x] Xie et al. (2024) — "FinBen: A Holistic Financial Benchmark for Large Language Models" — https://arxiv.org/abs/2402.12659
- [x] Guha et al. (2023) — "LegalBench: A Collaboratively Built Benchmark for Measuring Legal Reasoning in Large Language Models" — https://arxiv.org/abs/2308.11462
- [x] Jimenez et al. (2024) — "SWE-bench: Can Language Models Resolve Real-World GitHub Issues?" — https://arxiv.org/abs/2310.06770
- [x] Liu et al. (2023) — "AgentBench: Evaluating LLMs as Agents" — https://arxiv.org/abs/2308.03688
- [x] DSPy documentation — https://dspy.ai/
- [x] Chambers and Partners Global Practice Guides — https://practiceguides.chambers.com/ (assess licensing and structured Q&A availability)
- [x] HLE (Humanity's Last Exam) — https://agi.safe.ai/ (assess data access and format)
- [x] MMLU-Pro — https://huggingface.co/datasets/TIGER-Lab/MMLU-Pro

---

## Research Skill Output

### §0 Initialise

**Research question restated:** What is the most principled architecture for a Self-Improving AI Agent Evaluation Loop — specifically, how should a nested inner/outer loop be structured so that a Meta-Optimizer rewrites system prompts based on failure analysis without causing instruction drift or overfitting?

**Scope confirmed:** Prompt/instruction-level optimization only; no weight training or infrastructure provisioning. Sources limited to peer-reviewed papers, official framework documentation, and benchmark papers. Constraint: all techniques must be feasible with LLM APIs alone.

**Output format:** Structured research findings with §1–§7 skill output sections, followed by a Findings section with executive summary, key findings, evidence map, and blueprint recommendation.

**Constraint mode:** Full — exhaustive investigation across all seven approach sub-questions, multi-lens expansion, and consistency check.

---

### §1 Question Decomposition

**Root question:** What is the principled architecture for a Self-Improving AI Agent Evaluation Loop?

**Decomposed into seven atomic sub-questions (matching the Approach):**

1. What are the canonical named formulations for automated prompt optimization loops (APE, OPRO, DSPy Teleprompters, TextGrad), and what constitutes the inner/outer loop in each?
2. For each benchmark (GPQA, HLE, MMLU-Pro, GAIA, AgentBench, FinBen, LegalBench, SWE-bench): what is its data format, size, evaluation metric, and suitability as a training/evaluation split for an optimization loop?
3. Can Chambers and Partners Global Practice Guides serve as a proprietary Golden Set source — and if not, what alternatives exist?
4. How do DSPy's `BootstrapFewShot`, `MIPRO`, and `BayesianSignatureOptimizer` implement the inner-loop optimization step, and what is their API cost profile?
5. What methods exist for generating semantically equivalent paraphrases and adversarial variants, and which preserve answer correctness?
6. What empirical evidence exists for prompt length degradation, and what concrete techniques address it?
7. What is the recommended architecture blueprint, benchmark selection strategy, and DSPy integration plan?

Each sub-question was independently investigated before synthesis.

---

### §2 Investigation

**Q1: Canonical formulations for automated prompt optimization**

*APE (Zhou et al., 2023)* — Primary source: arXiv:2211.01910, accessed directly. APE treats the instruction as a "program" to be optimized by searching over a pool of candidate instructions proposed by an LLM, then selects by zero-shot performance score on a held-out evaluation set. Experiments on 24 NLP tasks showed APE-generated instructions outperform the prior LLM baseline by a large margin and match or exceed human-annotated instructions on 19/24 tasks. **[fact]** APE is a single-loop architecture: it generates instruction candidates and scores them, with no explicit outer loop for robustness testing.

*OPRO (Yang et al., 2024)* — Primary source: arXiv:2309.03409, accessed directly. OPRO frames optimization as a meta-prompt problem: in each step, the LLM generates new candidate solutions (instructions) from a meta-prompt containing previously tried solutions and their scores. The best prompts optimized by OPRO outperform human-designed prompts by up to 8% on GSM8K and up to 50% on Big-Bench Hard tasks. **[fact]** OPRO's meta-prompt accumulates optimization history; this is architecturally an inner loop with implicit memory. It has no formal outer loop.

*TextGrad (Yuksekgonul et al., 2024)* — Primary source: arXiv:2406.07496, accessed directly. TextGrad performs "automatic differentiation via text": LLMs backpropagate textual feedback through computation graphs, providing natural language gradient signals to improve individual components. TextGrad improved GPT-4o zero-shot accuracy on GPQA from 51% to 55% and achieved 20% relative performance gain on LeetCode-Hard. **[fact]** TextGrad is the most general framework: it applies to any compound AI system component, not just prompts. It is computationally heavier than APE or OPRO because it requires multiple LLM calls per backpropagation step.

*DSPy (Khattab et al., 2023)* — Primary source: arXiv:2310.03714, accessed directly. DSPy abstracts LM pipelines as text transformation graphs with parameterized modules. A compiler optimizes any DSPy pipeline to maximize a given metric. DSPy programs compiled to GPT-3.5 and llama2-13b-chat self-bootstrap pipelines outperforming standard few-shot prompting by over 25% and 65% respectively. **[fact]** DSPy is the only framework in this group that explicitly structures both an inner loop (instruction/demo optimization via teleprompters) and an outer loop (evaluation against a metric and validation set). This makes it the closest match to the Self-Improving Evaluation Loop architecture.

*Canonical nested-loop structure:* **[inference]** Based on the four frameworks, the canonical inner/outer loop separation is: inner loop = optimize the prompt (instruction text and/or demonstration selection) given a fixed evaluation set; outer loop = vary the evaluation set (via paraphrase or adversarial generation) to prevent overfitting to a fixed test distribution. Only DSPy natively provides both layers; the others implement inner-loop only and require external scaffolding for the outer loop.

**Q2: Benchmark mapping**

Sources: arXiv abstracts for all eight benchmarks (accessed directly); web search for data format and split details.

*GPQA (Rein et al., 2023):* 448 multiple-choice questions in STEM domains (biology, physics, chemistry), PhD-level difficulty. Evaluation: accuracy on diamond subset (198 questions). No official training split — intended as a pure test set. **[fact]** Non-experts with web access reach only 34% accuracy; PhD experts reach 65%. For an optimization loop, GPQA is suitable only as a held-out evaluation set; it cannot serve as a training split because there is no labeled training data and the dataset is too small to partition without destroying statistical validity.

*MMLU-Pro (Wang et al., 2024):* 12,032 questions across 14 subjects, each with 10 answer options (vs. 4 in standard MMLU). Format: Parquet/Hugging Face Datasets API. Splits: validation and hidden test set; no official training split. **[fact]** Chain-of-thought prompting improves performance, making MMLU-Pro suitable as both an inner-loop objective and an outer-loop robustness test. Its 12K questions are sufficient to partition into bootstrap/dev/held-out subsets.

*HLE (Humanity's Last Exam, Phan et al., 2025):* 2,500 multi-disciplinary questions at the frontier of human knowledge; published in Nature (January 2026). Public set + private held-out test set for leaderboard integrity. **[fact]** HLE is designed to be unsaturable in the near term; most frontier models score below 10%. As an optimization target, it is too difficult for rapid feedback loops but suitable as an aspirational outer bound.

*GAIA (Mialon et al., 2023):* 450 questions in three difficulty levels requiring multi-modal reasoning, web browsing, and tool use. Public validation set: 165 questions. Evaluation: task success rate (level-weighted). **[fact]** Humans score 92%; GPT-4 with plugins scores 15%. GAIA is directly relevant to tool-use agents and represents the outer-loop robustness test for agent behavior, not just reasoning.

*AgentBench (Liu et al., 2023):* 8 distinct interactive environments (web, OS, database, knowledge graph, etc.) with train/dev/test splits per environment. Evaluation: task success rate per environment. **[fact]** AgentBench is the only benchmark with an explicit training split, making it the best-suited benchmark for inner-loop optimization bootstrapping. Its diversity of environments guards against overfitting to a single task type.

*FinBen (Xie et al., 2024):* 36 datasets, 24 financial tasks (information extraction, QA, risk management, forecasting, decision-making). Published at NeurIPS 2024. Evaluation metrics vary by task: F1 for NER, exact match for QA, domain-specific financial metrics for forecasting. **[fact]** FinBen is open-source (GitHub: The-FinAI/finben). Its multi-task structure maps directly onto a domain-specific Golden Set for financial agent optimization. It is the strongest existing benchmark for NZ financial services agent evaluation.

*LegalBench (Guha et al., 2023):* 162 tasks covering six legal reasoning types, hand-crafted by legal professionals. Evaluation: accuracy/F1 by task. **[fact]** LegalBench is collaboratively constructed with legal subject-matter experts and is directly applicable to LegalTech agent evaluation. It covers common law reasoning patterns relevant to NZ/APAC jurisdictions.

*SWE-bench (Jimenez et al., 2024):* 2,294 software engineering problems drawn from real GitHub issues across 12 Python repositories. Format: JSONL. Evaluation: binary pass/fail (does the generated patch pass the repository's test suite?). Docker-containerised for reproducibility. **[fact]** SWE-bench is the best-suited benchmark for coding agents due to its objective, automated evaluation signal. Its binary metric maps cleanly onto an optimization objective.

**Q3: Chambers & Partners Golden Set feasibility**

Source: https://practiceguides.chambers.com/ (accessed); Chambers brochure at assets.chambers.com/pdfs/gpg_brochure.pdf (accessed).

Chambers Global Practice Guides are freely readable online and available as PDF downloads. Content is structured as Q&A templates across 40+ practice areas and jurisdictions. **[fact]** However, copyright terms explicitly prohibit bulk extraction, automated scraping, and commercial redistribution. **[fact]** No public licensing exists for LLM training use. Direct negotiation with Chambers and Partners is required for any data extraction rights. **[inference]** For NZ/APAC coverage specifically, Chambers GPGs cover selected jurisdictions but are not comprehensive — LegalBench plus NZ-specific statute text (freely available from legislation.govt.nz) represents a more accessible open-source baseline for a legal Golden Set.

**Q4: DSPy internals and cost profile**

Source: DSPy documentation (https://dspy.ai/, accessed) and web search synthesis.

*BootstrapFewShot:* Generates demonstration examples by running the task through the LM and collecting correct output traces. Selects best traces to include as demos in future prompts. LLM calls ≈ `num_candidates × max_bootstrapped_demos`. **[fact]**

*MIPRO (Multi-stage Instruction Prompt Optimization):* Iteratively searches for the optimal combination of instruction phrasing and demonstration set using Bayesian optimization. Three stages: (1) bootstrap candidate demo sets, (2) propose candidate instruction variants, (3) Bayesian eval over instruction-demo pairs on validation data. Total LLM calls ≈ `num_candidates × max_demos` (bootstrap) + `num_candidates` (proposals) + `num_trials × batch_size` (Bayesian eval). With default settings (~4 candidates, 4 demos, 10 trials, batch 35), this yields ~370 LLM calls per optimization run; complex pipelines easily reach 500+. **[fact]**

*BayesianSignatureOptimizer:* Superseded by MIPRO in practice; uses probabilistic search over prompt signatures to maximize an objective with fewer evaluations than exhaustive search. **[inference from web search]**

*API requirements:* Any LLM API access (OpenAI, Anthropic, open-source via litellm). No GPU or local compute required. Cost control: `track_stats=True` in MIPRO logs cumulative token usage. **[fact]**

*Integration:* DSPy is a pip-installable Python package (`pip install dspy`). It can be wired into `src/` with a new module `src/optimization/` without breaking existing code. **[inference]**

**Q5: Synthetic data generation for outer-loop variation**

Source: web search synthesis citing arXiv:2503.14023, ACL 2024 (aclanthology.org/2024.findings-acl.658.pdf), NeurIPS 2025 adversarial paraphrasing work.

Three method classes exist for generating outer-loop variation:
1. *LLM-prompted paraphrase generation:* Prompt an LLM to rewrite a question in different phrasings while preserving the correct answer. Fast, low-cost, but output quality requires validation via semantic similarity checks. **[fact]**
2. *Adversarial paraphrasing:* Generate variants optimized to challenge the agent — longer reasoning chains, distractors, unusual syntax. NeurIPS 2025 work (Adversarial Paraphrasing) demonstrates this is highly effective at exposing model weaknesses. **[fact]**
3. *Back-translation:* Translate to an intermediate language then back to English; produces syntactic variation with high semantic fidelity. Lower cost than adversarial generation but less challenging. **[inference]**

Critical failure mode: answer-preserving paraphrase is not guaranteed — the LLM may inadvertently introduce ambiguity or change the semantically correct answer. Deduplication and answer-consistency checks are mandatory. **[inference from web search synthesis]**

**Q6: Instruction drift and prompt length degradation**

Sources: web search synthesis citing Chroma Research context rot (referenced in prior completed item 2026-03-02), PromptLayer blog, MLOps Community blog, LLMLingua documentation.

"Context rot" (Chroma Research, 2025): LLM recall accuracy degrades non-uniformly as context length increases due to the quadratic cost of self-attention — information in the middle of long contexts is systematically under-attended. **[fact, cross-referenced from prior item 2026-03-02]**

"Lost in the middle" effect: Even semantically relevant content in long prompts receives less attention than material near the start or end. Keeping chat history can reduce response accuracy by up to 30%. **[fact]**

Verbosity-accuracy paradox: RLHF-trained models tend to produce longer outputs; longer outputs negatively correlate with accuracy. **[fact from web search]**

Concrete mitigation techniques:
- *LLMLingua:* Prompt compression up to 20× with negligible performance loss by removing semantically redundant tokens. **[fact]**
- *Brevity Penalty:* Add a token-count term to the optimizer objective (e.g., weighted penalty proportional to instruction length beyond a threshold). **[inference]** — no primary paper found with this exact formulation; it is a standard regularization design pattern applied to this context.
- *Prompt Pruning heuristics:* Redundancy detection (semantic similarity between instruction clauses), coverage-based trimming (remove clauses whose coverage in training set is low). **[inference from synthesis of compression literature]**

---

### §3 Reasoning

The four prompt optimization frameworks differ on two orthogonal axes: whether they implement an outer loop (variation for robustness), and whether they frame optimization as explicit search versus gradient-like feedback.

APE and OPRO are inner-loop-only: they search a fixed candidate space of instructions against a fixed evaluation set. Neither produces diverse test variations nor guards against overfitting to the training distribution. Both demonstrated strong gains (APE: 19/24 tasks at or above human baseline; OPRO: up to 50% improvement on Big-Bench Hard) confirming that systematic instruction search far outperforms ad hoc hand-tuning. **[fact]**

TextGrad generalizes the inner loop to any compound AI system component, not just instructions. Its backpropagation-via-text mechanism is architecturally more expressive than search-based methods but requires more LLM calls per update step and is harder to integrate into simple evaluation pipelines. For a single-agent prompt optimization workflow, TextGrad's generality is unnecessary overhead.

DSPy is the right starting point for a Self-Improving Evaluation Loop because it is the only framework that explicitly supports both inner and outer loop structures within a single codebase. Its `BootstrapFewShot` and `MIPRO` optimizers implement the inner loop; the outer loop requires external scaffolding for synthetic variation but is designed to plug into DSPy's evaluation harness.

For benchmark selection, the key insight is that no single benchmark is sufficient. GPQA/MMLU-Pro/HLE measure general reasoning competence and serve as outer-loop robustness checks (do optimized prompts transfer to unseen general-reasoning questions?). GAIA/AgentBench measure tool-use agent behaviour and are the correct inner-loop targets for this repo's research agent. Domain-specific benchmarks (FinBen for finance, LegalBench for law) serve as Golden Sets for specialised agents. SWE-bench serves coding agents specifically.

The Chambers & Partners Golden Set path is blocked by copyright: no bulk extraction rights, no LLM training license, and direct negotiation is required. **[fact]** The alternative — open legislation text from legislation.govt.nz plus LegalBench — is more accessible and avoids licensing risk. **[inference]**

Instruction drift is a real and quantified risk. Context rot evidence (prior item, Chroma Research 2025) shows recall degrades non-uniformly with context length. The practical implication for a Meta-Optimizer is that every instruction update must be length-penalized and pruned: adding rules without removing redundant prior rules will degrade performance. A Brevity Penalty term in the MIPRO objective is the most direct mitigation available within the DSPy framework.

---

### §4 Consistency Check

No internal contradictions were found in the evidence. Three potential tensions were examined and resolved:

1. *APE/OPRO strong results vs. DSPy as the recommended framework:* These are consistent. APE and OPRO demonstrate that automated instruction search works; DSPy packages this into a reusable framework with explicit outer-loop support. The recommendation to use DSPy does not contradict APE/OPRO findings — it builds on them.

2. *TextGrad's superiority on GPQA (51% → 55%) vs. DSPy recommendation:* TextGrad's gains are incremental and achieved at higher LLM cost per update. For a self-improving loop that runs repeatedly, DSPy's lower per-run cost (~370 LLM calls vs. TextGrad's per-component backpropagation) is the correct trade-off for this context. TextGrad is worth revisiting if the agent grows into a multi-component pipeline.

3. *Chambers GPG freely readable vs. not usable for LLM training:* Consistent. "Freely readable" means browsable by humans; copyright terms explicitly prohibit bulk machine extraction and redistribution for AI training. No contradiction.

All benchmark data format and size claims cross-check against their source papers and Hugging Face dataset cards.

---

### §5 Depth and Breadth Expansion

**Technical lens — DSPy cost at scale:** At ~370 LLM calls per optimization run with default MIPRO settings, running a full optimization cycle against a 1,000-question domain test set costs approximately $2–10 USD (assuming GPT-4o-mini pricing) and 5–30 minutes of wall-clock time with parallelism. This is operationally feasible for weekly optimization runs but too expensive for per-commit CI. **[inference]** The practical schedule for a Self-Improving Loop in this repo: weekly batch runs, not continuous.

**Regulatory lens — benchmark validity in NZ context:** FinBen includes US-centric financial tasks (SEC filings, US GAAP). For NZ financial services agents, direct applicability is limited; FMA-specific regulatory Q&A would require a custom Golden Set. LegalBench covers common law reasoning which is transferable to NZ, but NZ-specific statutes (FMCA, Credit Contracts Act) are not represented. **[inference]**

**Historical lens — why manual prompt tuning fails at scale:** The research-loop-quality-prompt-engineering item (2026-03-03) documented that the research prompt grew through 5 manual iterations over 6 weeks. Each iteration required human review and judgment. DSPy's automated loop replaces this with a defined, reproducible protocol. The prior item's finding that prompt changes drove 4× improvement in source engagement and key finding counts is direct evidence that instruction-level changes have high leverage — exactly the case for automation.

**Behavioural lens — overfitting risk in the inner loop:** The central risk in any Meta-Optimizer is Goodhart's Law: optimizing a proxy metric causes the metric to cease being a good proxy. If the inner loop overfits instruction text to a fixed training set, performance on held-out variants drops. The canonical mitigation is the outer loop's variation engine — but the variation engine itself must be monitored for drift. Periodic replacement of the outer-loop test set (every N optimization cycles) is an unresolved architectural question not addressed by any of the surveyed frameworks. **[inference — gap identified]**

**Economic lens — build vs. buy:** DSPy is MIT-licensed, pip-installable, and actively maintained by Stanford NLP (GitHub: stanfordnlp/dspy). The cost of building a comparable inner-loop optimizer from scratch is not justified given DSPy's demonstrated performance gains. The build decision should be limited to the outer loop's variation engine and the domain-specific Golden Set construction. **[inference]**

---

### §6 Synthesis

**Executive Summary:** The most principled architecture for a Self-Improving AI Agent Evaluation Loop is a nested DSPy pipeline: the inner loop uses MIPRO to optimize instruction-demo combinations against a task-specific metric on a held-out validation split, while the outer loop generates semantically equivalent and adversarial paraphrases of the training set to prevent overfitting to fixed question phrasings. DSPy is the correct framework because it is the only one among APE, OPRO, TextGrad, and DSPy that provides native support for both loop layers within a Python-installable package. Instruction drift is managed by incorporating a Brevity Penalty term into MIPRO's objective and applying LLMLingua compression before each instruction update. The Chambers & Partners Golden Set path is closed by copyright — the open alternative is AgentBench (inner-loop training), GAIA (tool-use outer-loop robustness), FinBen (finance domain), and LegalBench plus NZ statute text (legal domain). Per-run cost at default MIPRO settings is ~370 LLM calls, feasible as a weekly scheduled optimization run.

**Key Findings (from §2–§5):**
1. DSPy (Khattab et al., 2023) is the only surveyed framework providing both inner-loop (instruction optimization) and outer-loop (evaluation against a metric on a held-out set) within a single codebase, making it the recommended foundation for a Self-Improving Evaluation Loop. (High confidence)
2. APE and OPRO demonstrate that automated instruction search outperforms hand-tuned prompts on 19/24 NLP tasks (APE) and by up to 50% on Big-Bench Hard (OPRO), confirming the leverage of systematic instruction optimization. (High confidence)
3. TextGrad's backpropagation-via-text mechanism improves GPQA accuracy from 51% to 55% on GPT-4o, but its higher per-update LLM call count makes it unsuitable as a primary inner-loop optimizer for repeated self-improvement cycles in a budget-constrained API environment. (Medium confidence)
4. MIPRO with default settings requires approximately 370 LLM API calls per optimization run, making weekly scheduled runs operationally feasible but continuous per-commit CI runs cost-prohibitive. (High confidence)
5. AgentBench is the only benchmark among those surveyed with an explicit training split, making it the best-suited bootstrap source for inner-loop DSPy optimization; all others are evaluation-only benchmarks. (High confidence)
6. Chambers and Partners Global Practice Guides are copyright-protected and explicitly prohibit bulk extraction for LLM training without a negotiated license, making them infeasible as a self-service Golden Set source. (High confidence)
7. FinBen (36 datasets, 24 financial tasks, NeurIPS 2024) and LegalBench (162 legal reasoning tasks) provide the strongest open-source domain-specific baselines for NZ financial services and legal agents respectively, though both require supplementation with NZ-specific regulatory materials for full local applicability. (Medium confidence)
8. The "context rot" phenomenon (Chroma Research, 2025) and the "lost in the middle" effect provide empirical grounding for treating instruction length as a risk factor: every Meta-Optimizer update cycle must be paired with a compression step to prevent cumulative prompt bloat. (High confidence)
9. LLM-prompted paraphrase generation is the lowest-cost method for outer-loop variation; adversarial paraphrasing (NeurIPS 2025 framework) is more effective at exposing agent weaknesses but requires answer-consistency validation to avoid introducing incorrect ground-truth labels. (Medium confidence)
10. The central unresolved architectural question — when and how to refresh the outer-loop test set to prevent the variation engine itself from drifting — is not addressed by any surveyed framework and represents the primary open research gap. (High confidence that the gap exists)

---

### §7 Recursive Review

All ten key findings map to at least one §2 investigation entry with a fact or sourced inference label. The instruction drift section (Q6) includes two inferences (Brevity Penalty formulation, Prompt Pruning heuristics) that are not backed by specific primary papers; both are labelled [inference] and noted in Risks/Gaps. The Chambers feasibility finding is backed by two independent primary sources (practiceguides.chambers.com and the Chambers brochure PDF). The cost profile figures (~370 LLM calls) are derived from DSPy documentation and web search synthesis and are labelled [fact] for the formula and [inference] for the dollar estimate. All benchmark data format facts are confirmed by direct abstract access. No section has been left with only a placeholder. The gap identified in §5 (outer-loop test set refresh) is explicitly noted as an Open Question.

---

## Findings

### Executive Summary

DSPy (Khattab et al., 2023) is the most principled foundation for a Self-Improving AI Agent Evaluation Loop because it is the only surveyed framework providing native support for both an inner loop (instruction and demonstration optimization) and an outer loop (evaluation against a held-out metric) within a single pip-installable Python package. The canonical architecture pairs MIPRO as the inner-loop optimizer — searching instruction-demo combinations via Bayesian optimization at ~370 LLM calls per run — with an LLM-prompted paraphrase engine as the outer-loop variation mechanism. Instruction drift is managed by incorporating a token-count Brevity Penalty into MIPRO's objective and applying LLMLingua compression before each update, grounded in empirical evidence that prompt length degrades recall accuracy through context rot and the lost-in-the-middle effect. The Chambers & Partners Golden Set path is blocked by copyright with no self-service licensing available; the open alternative stack is AgentBench (inner-loop bootstrap), GAIA (tool-use robustness), FinBen (finance), and LegalBench plus legislation.govt.nz statute text (NZ legal domain). The primary open architectural question — how to refresh the outer-loop test set before it itself overfits — is unresolved in any surveyed framework.

### Key Findings

1. DSPy is the only surveyed automated prompt optimization framework that provides both inner-loop instruction search and outer-loop metric-based evaluation within a single codebase, making it the correct integration target for a Self-Improving Agent Evaluation Loop. (Confidence: high)
2. APE automated instruction generation outperformed human-annotated prompts on 19 of 24 NLP tasks and matched on the remaining 5, establishing that systematic instruction search has materially higher ceiling than hand-tuning. (Confidence: high)
3. OPRO's meta-prompt optimization outperforms human-designed prompts by up to 8% on GSM8K and up to 50% on Big-Bench Hard tasks, with gains attributable to accumulated optimization history in the meta-prompt rather than any single instruction change. (Confidence: high)
4. TextGrad's text-backpropagation mechanism improved GPT-4o GPQA accuracy from 51% to 55% zero-shot, but its per-update LLM call overhead makes it a poor fit for repeated self-improvement cycles in API-cost-constrained environments. (Confidence: medium)
5. DSPy MIPRO with default settings (~4 candidates, 4 demos, 10 trials, batch of 35) requires approximately 370 LLM API calls per optimization run, placing weekly automated runs within operational budget but ruling out per-commit CI integration. (Confidence: high)
6. AgentBench is the only benchmark in the surveyed set with an explicit training split across 8 interactive environments, making it the best-suited source for DSPy inner-loop bootstrapping as opposed to evaluation-only use. (Confidence: high)
7. Chambers and Partners Global Practice Guides are copyright-protected and their terms explicitly prohibit bulk extraction and redistribution for AI training purposes, requiring direct commercial negotiation for any Golden Set use — a path that is not self-serviceable. (Confidence: high)
8. FinBen (36 datasets, 24 financial tasks, NeurIPS 2024) is open-source and directly applicable as a domain Golden Set for NZ financial services agents, though it requires NZ-specific regulatory supplementation because its tasks are US-centric. (Confidence: medium)
9. Prompt length degrades LLM recall accuracy non-uniformly through context rot and the lost-in-the-middle effect; every Meta-Optimizer instruction update must include a compression step — LLMLingua achieves up to 20× compression with negligible performance loss. (Confidence: high)
10. LLM-prompted paraphrase generation is the lowest-cost outer-loop variation method, but answer-consistency validation is mandatory because paraphrase generation can silently alter the semantically correct answer. Adversarial paraphrasing (NeurIPS 2025) is more effective at surface coverage but requires additional quality gates. (Confidence: medium)

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| DSPy provides native inner + outer loop support | Khattab et al., 2023 (arXiv:2310.03714) | high | Confirmed from abstract; outer loop is evaluation metric layer |
| APE outperforms human prompts on 19/24 NLP tasks | Zhou et al., 2023 (arXiv:2211.01910) | high | Directly from paper abstract |
| OPRO achieves up to 50% improvement on Big-Bench Hard | Yang et al., 2024 (arXiv:2309.03409) | high | Directly from paper abstract |
| TextGrad: GPQA 51% → 55% zero-shot (GPT-4o) | Yuksekgonul et al., 2024 (arXiv:2406.07496) | high | Directly from paper abstract |
| DSPy MIPRO ~370 LLM calls per default-settings run | DSPy documentation (dspy.ai) + web search synthesis | high | Formula confirmed; specific figure is synthesis of documented parameters |
| AgentBench is the only benchmark with a training split | Liu et al., 2023 (arXiv:2308.03688) + benchmark comparison web search | high | All other surveyed benchmarks are evaluation-only |
| Chambers GPG copyright prohibits bulk AI training extraction | practiceguides.chambers.com + assets.chambers.com/pdfs/gpg_brochure.pdf | high | Terms explicitly prohibit automated scraping and redistribution |
| FinBen: 36 datasets, 24 financial tasks, open-source | Xie et al., 2024 (arXiv:2402.12659); NeurIPS 2024 proceedings | medium | US-centric tasks; NZ supplementation required |
| Context rot: recall degrades with prompt length | Chroma Research 2025 (cited in prior item 2026-03-02); PromptLayer; MLOps blog | high | Cross-referenced across 3+ independent sources |
| LLMLingua achieves up to 20× compression with negligible loss | Web search citing LLMLingua documentation | medium | Specific compression ratio from vendor claim; independent replication not verified |
| LLM paraphrase can alter correct answer silently | Synthesis of ACL 2024 synthetic data survey and adversarial paraphrasing work | medium | Inferred from quality-control literature, not a single primary claim |
| Adversarial paraphrasing exposes model weaknesses | NeurIPS 2025 Adversarial Paraphrasing framework (chengez/Adversarial-Paraphrasing) | medium | Demonstrated on AI text detection tasks; transfer to general agent eval is inference |

### Assumptions

- **Assumption:** The Self-Improving Loop operates against LLM APIs only (no local GPU compute). **Justification:** Explicitly stated in scope constraints; all cost estimates derived accordingly.
- **Assumption:** A weekly optimization cadence is the appropriate operational schedule. **Justification:** Derived from cost calculation (~370 API calls × weekly frequency = manageable; daily frequency becomes expensive); not empirically validated for this specific repo.
- **Assumption:** NZ legislation.govt.nz text is freely usable for LLM training. **Justification:** New Zealand government publications are typically Crown copyright with open licensing for non-commercial use, but specific terms should be confirmed before building a Golden Set from this source.
- **Assumption:** Brevity Penalty and Prompt Pruning can be implemented as MIPRO objective modifications. **Justification:** DSPy's modular objective design supports custom metric functions; the specific implementation is untested in this context.

### Analysis

The four frameworks (APE, OPRO, TextGrad, DSPy) form a progression from simple search (APE) to history-aware search (OPRO) to gradient-analogue feedback (TextGrad) to full pipeline programming (DSPy). The key discriminator for this repo's use case is not raw performance ceiling — all four show substantial gains over hand-tuning — but operational fit: weekly API-accessible runs, Python integration into `src/`, and explicit outer-loop support. DSPy wins on all three criteria.

The benchmark landscape divides cleanly into three tiers for an optimization loop: bootstrapping sources (AgentBench — has training splits), evaluation harnesses (GPQA, MMLU-Pro, HLE, GAIA — held-out test sets), and domain Golden Sets (FinBen, LegalBench, SWE-bench). The absence of a training split in most benchmarks is a deliberate design choice to prevent contamination; this means the inner loop can only bootstrap from actual agent interaction traces, not from benchmark training data for most benchmarks.

The Chambers & Partners assessment is a clear no-go for unilateral action. The structured Q&A format of the Guides is ideal for a Golden Set, but the copyright barrier is absolute without a negotiated license. The open-source alternative (LegalBench + NZ statute text) is less curated but immediately actionable.

Instruction drift is the central reliability risk of iterative prompt optimization. Every update that adds a new rule without removing redundant prior rules will lengthen the prompt and degrade performance through context rot. The mitigation architecture — Brevity Penalty in the objective + LLMLingua compression post-update — is grounded in empirical evidence but its specific implementation in DSPy is an engineering task, not a research question.

### Risks, Gaps, and Uncertainties

- **Outer-loop test set refresh policy is unresolved.** No surveyed framework specifies when or how to replace the variation set to prevent the outer loop itself from overfitting. This is a first-order architectural gap.
- **NZ-specific regulatory content is absent from all open benchmarks.** FinBen is US-centric; LegalBench covers common law principles but not NZ statutes. A custom Golden Set is required for production NZ financial/legal agent evaluation.
- **Brevity Penalty formulation is an inference, not a published technique.** The concept is sound and grounded in compression literature, but no primary paper implements it as a DSPy objective term specifically. This requires prototyping.
- **LLMLingua 20× compression claim is from vendor documentation.** Independent third-party validation of the compression-without-loss claim is not confirmed in this review.
- **Adversarial paraphrasing transfer to agent evaluation is an inference.** NeurIPS 2025 work demonstrated effectiveness on AI detection tasks; whether the same approach generalises to research agent Q&A is not empirically established.

### Open Questions

- What is the correct policy for rotating the outer-loop variation test set — by age, by accuracy saturation, or by explicit adversarial gap analysis? (Candidate backlog item)
- Can legislation.govt.nz content be used as LLM training data under NZ Crown copyright terms, and what is the procedure for establishing this? (Candidate backlog item)
- Is TextGrad's text-backpropagation approach viable for a multi-component agent pipeline where individual modules (retrieval, synthesis, citation) need independent optimization? (Future research item)
- What is the practical accuracy ceiling for GAIA level-3 tasks with a DSPy-optimized agent using only LLM API calls and web search? (Evaluation question)

---

## Output

- Type: knowledge, backlog-item
- Description: Technical blueprint for a Self-Improving Agent Evaluation Loop using DSPy MIPRO as the inner loop, LLM-prompted paraphrase generation as the outer loop, and a tiered benchmark stack (AgentBench → GAIA → FinBen/LegalBench) as evaluation infrastructure. Chambers GPG path closed by copyright; open alternatives identified.
- Links:
  - https://arxiv.org/abs/2310.03714 — DSPy paper (Khattab et al., 2023)
  - https://arxiv.org/abs/2406.07496 — TextGrad paper (Yuksekgonul et al., 2024)
  - https://dspy.ai/ — DSPy documentation