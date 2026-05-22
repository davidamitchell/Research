---
review_count: 1
title: "Theory and mechanisms of prompt and program optimization in Language Models"
added: 2026-05-21T18:44:50+00:00
status: reviewing
priority: medium
blocks: []
tags: [llm, dspy, optimization, prompt-engineering, evaluation]
started: 2026-05-22T07:25:55+00:00
completed: ~
output: []
cites:
  - 2026-03-05-general-agent-optimization-framework
  - 2026-05-02-storm-perspective-discovery-multi-perspective-question-generation
related:
  - 2026-03-03-research-loop-quality-prompt-engineering
  - 2026-05-02-storm-perspective-discovery-multi-perspective-question-generation
superseded_by: ~
supersedes: ~
item_type: primary
confidence: medium
versions: []
---

# Theory and mechanisms of prompt and program optimization in Language Models

## Research Question

What theory best explains why prompt and program optimization methods can outperform baseline prompting and Reinforcement Learning (RL) in Language Model (LM) pipelines, and how do the methods in the listed papers operationalize that theory?

## Scope

**In scope:**
- Theoretical assumptions shared across the listed papers, for example search over instructions, demonstrations, retrieval context, constraints, and lightweight program structure
- Mechanistic descriptions of how each method works, including optimization loop, objective, and feedback signal
- Comparative mapping across Reflective Prompt Evolution, Declarative Self-improving Python (DSPy), DSPy Assertions, BetterTogether, Demonstrate-Search-Predict (DSP), and adjacent prompt or program optimization methods
- The role of retrieval and demonstrations in DSP, Infer-Retrieve-Rank, and multi-stage language model programs

**Out of scope:**
- Reproducing benchmark results or running new experiments in this item
- Full implementation tutorials for each framework
- General Large Language Model (LLM) history outside the listed papers

**Constraints:**
- Use publicly accessible sources with URLs
- Prioritize primary paper sources and official project documentation
- Focus on conceptual theory and algorithmic mechanism, not marketing summaries

## Context

Decision context: this item narrows the broader architecture question framed in the General Agent Optimization Framework item to the specific theory and mechanism of prompt and program optimization. [fact; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-05-general-agent-optimization-framework.md]

## Approach

1. Identify each paper's optimization object, for example prompt text, demonstrations, retrieval state, assertions, program structure, or tuning parameters, and its objective function.
2. Decompose each method's optimization loop into initialization, search or update step, evaluation signal, and stopping condition.
3. Compare the role of supervision across methods, including in-context, reflective, retrieval-based, constraint-based, and fine-tuning-assisted supervision.
4. Synthesize a unifying theory that explains why these methods can improve performance relative to baseline prompting and Reinforcement Learning.
5. Extract practical decision criteria for selecting an approach by task type, compute budget, and reliability requirements.

## Sources

- [x] [Agrawal et al. (2025) Genetic-Pareto (GEPA): Reflective Prompt Evolution Can Outperform Reinforcement Learning](https://arxiv.org/abs/2507.19457)
- [x] [Opsahl-Ong et al. (2024) Optimizing Instructions and Demonstrations for Multi-Stage Language Model Programs](https://arxiv.org/abs/2406.11695)
- [x] [Khattab et al. (2023) Declarative Self-improving Python (DSPy): Compiling Declarative Language Model Calls into Self-Improving Pipelines](https://arxiv.org/abs/2310.03714)
- [x] [Soylu et al. (2024) Fine-Tuning and Prompt Optimization: Two Great Steps that Work Better Together](https://arxiv.org/abs/2407.10930)
- [x] [Xian et al. (2024) Prompts as Auto-Optimized Training Hyperparameters: Training Best-in-Class Information Retrieval Models from Scratch with 10 Gold Labels](https://arxiv.org/abs/2406.11706)
- [x] [Shao et al. (2024) Assisting in Writing Wikipedia-like Articles From Scratch with Large Language Models](https://arxiv.org/abs/2402.14207)
- [x] [D'Oosterlinck et al. (2024) In-Context Learning for Extreme Multi-Label Classification](https://arxiv.org/abs/2401.12178)
- [x] [Singhvi et al. (2023) DSPy Assertions: Computational Constraints for Self-Refining Language Model Pipelines](https://arxiv.org/abs/2312.13382)
- [x] [Khattab et al. (2023) Demonstrate-Search-Predict (DSP): Composing Retrieval and Language Models for Knowledge-Intensive Natural Language Processing](https://arxiv.org/abs/2212.14024)
- [x] [DSPy Optimizers Documentation](https://dspy.ai/learn/optimization/optimizers/)
- [x] [DSPy Frequently Asked Questions: Assertions and Optimizer Mechanics](https://github.com/stanfordnlp/dspy/blob/main/docs/docs/faqs.md)
- [x] [General Agent Optimization Framework](https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-05-general-agent-optimization-framework.md)
- [x] [STORM Perspective Discovery and Multi-perspective Question Generation](https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-02-storm-perspective-discovery-multi-perspective-question-generation.md)
- [x] [Evaluating and Improving Autonomous Research Loop Quality: Prompt Engineering and Output Assessment](https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-03-research-loop-quality-prompt-engineering.md)

---

## Research Skill Output

### §0 Initialise

- research_question: What theory best explains why prompt and program optimization methods can outperform baseline prompting and Reinforcement Learning in language model pipelines, and how do the surveyed methods operationalize that theory?
- scope: mechanism and theory only, with comparison across GEPA, DSPy, DSPy Assertions, BetterTogether, DSP, Infer-Retrieve-Rank, and adjacent multi-stage systems
- constraints: public URL-backed sources, primary papers and official documentation first, no new experiments
- output_format: full structured synthesis with executive summary, key findings, evidence map, assumptions, analysis, risks, and open questions
- constraint_mode: full
- prior_work:
  - [fact] The General Agent Optimization Framework item recommended DSPy inside a broader self-improving evaluation architecture, but it did not compare the internal mechanism of GEPA, Multi-Stage Instruction Prompt Optimization (MIPRO), DSPy Assertions, BetterTogether, DSP, and related methods directly. [source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-05-general-agent-optimization-framework.md]
  - [fact] The research-loop-quality-prompt-engineering item established that prompt changes materially change output quality, which supports the practical importance of systematic prompt optimization without itself explaining these optimizer families. [source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-03-research-loop-quality-prompt-engineering.md]

### §1 Question Decomposition

**Root question:** Why do prompt and program optimization methods beat baseline prompting and sometimes beat Reinforcement Learning, and how do their mechanisms differ?

**Decomposition tree:**

1. **Optimization object**
   - 1.1 Which parts of the system are treated as tunable variables: instructions, demonstrations, retrieval state, assertions, program structure, or weights?
   - 1.2 What downstream metric or proxy objective guides improvement?
2. **Update mechanism**
   - 2.1 How does GEPA update prompts from trajectories and reflections?
   - 2.2 How does Multi-Stage Instruction Prompt Optimization (MIPRO) update instructions and demonstrations in multi-stage programs?
   - 2.3 How does DSPy frame programs so optimizers can search over them?
   - 2.4 How do DSPy Assertions turn constraints into optimization signals?
   - 2.5 How does BetterTogether alternate prompt and weight updates?
3. **Supervision and information flow**
   - 3.1 What role do demonstrations play in DSPy, MIPRO, and Infer-Retrieve-Rank?
   - 3.2 What role does retrieval play in DSP, Infer-Retrieve-Rank, and STORM, Synthesis of Topic Outlines through Retrieval and Multi-perspective Question Asking?
   - 3.3 Why is natural-language feedback richer than sparse scalar reward in some settings?
4. **Theoretical synthesis**
   - 4.1 What shared theory explains gains over baseline prompting?
   - 4.2 Under what conditions can prompt or program optimization outperform Reinforcement Learning?
5. **Selection criteria**
   - 5.1 Which method fits trajectory-rich reasoning tasks?
   - 5.2 Which method fits modular pipelines with measurable metrics?
   - 5.3 Which method fits knowledge-intensive retrieval tasks or scarce-label settings?

### §2 Investigation

#### 2.1 Optimization object and objective

- [fact] GEPA treats one or more Large Language Model prompts inside an Artificial Intelligence (AI) system as the optimization object, samples trajectories including reasoning and tool traces, and updates prompts to improve downstream task performance against observed trial outcomes. [source: https://arxiv.org/abs/2507.19457]
- [fact] MIPRO treats free-form instructions and few-shot demonstrations for every module in a multi-stage language model program as the optimization object and aims to maximize a downstream metric without module-level labels or gradients. [source: https://arxiv.org/abs/2406.11695]
- [fact] DSPy treats a program's signatures, modules, demonstrations, prompts, and optionally weights as tunable parameters under an optimizer that maximizes a user-specified metric. [source: https://arxiv.org/abs/2310.03714; https://dspy.ai/learn/optimization/optimizers/]
- [fact] DSPy Assertions add computational constraints, expressed as assertions or suggestions, to the optimization object so that compilation and self-refinement can target both rule compliance and downstream task quality. [source: https://arxiv.org/abs/2312.13382; https://github.com/stanfordnlp/dspy/blob/main/docs/docs/faqs.md]
- [fact] BetterTogether treats prompt parameters and language model weights as complementary optimization targets and alternates between them to maximize a shared downstream task metric in modular pipelines. [source: https://arxiv.org/abs/2407.10930]
- [fact] Prompts as Auto-Optimized Training Hyperparameters treats the synthetic-data-generation prompt as a training hyperparameter whose value is judged by the quality of the downstream information retrieval model trained on the generated queries. [source: https://arxiv.org/abs/2406.11706]

#### 2.2 Update mechanism and loop structure

- [fact] GEPA operationalizes update search by sampling trajectories, reflecting on them in natural language to diagnose failure modes, proposing prompt updates, testing those updates, and combining complementary lessons from high-performing attempts. [source: https://arxiv.org/abs/2507.19457]
- [fact] GEPA reports that this reflective loop outperforms Group Relative Policy Optimization (GRPO) by 6 percent on average, by up to 20 percent on individual tasks, while using up to 35 times fewer rollouts. [source: https://arxiv.org/abs/2507.19457]
- [fact] MIPRO operationalizes update search in three stages: bootstrapping candidate demonstrations from traces, generating program-aware and data-aware instruction proposals, and using stochastic mini-batch evaluation plus a surrogate model to search over instruction and demonstration combinations. [source: https://arxiv.org/abs/2406.11695; https://dspy.ai/learn/optimization/optimizers/]
- [fact] DSPy documents MIPROv2 as an optimizer that first collects traces, then drafts grounded instruction proposals, then runs discrete search with mini-batch evaluation and surrogate-model updates over prompt configurations. [source: https://dspy.ai/learn/optimization/optimizers/]
- [fact] DSPy documents BootstrapFewShot as an optimizer that generates demonstrations with a teacher program and retains only demonstrations that pass the task metric, which means demonstration selection is itself metric-guided optimization rather than manual prompt curation. [source: https://dspy.ai/learn/optimization/optimizers/]
- [fact] DSPy Assertions operationalizes constraints at two points: compile time, where prompts can be optimized to satisfy assertions more reliably, and inference time, where self-refinement retries can backtrack when an assertion fails. [source: https://arxiv.org/abs/2312.13382; https://github.com/stanfordnlp/dspy/blob/main/docs/docs/faqs.md]
- [fact] BetterTogether alternates prompt optimization and weight optimization so that prompt search can discover better decompositions or reasoning patterns and weight updates can then internalize them more efficiently. [source: https://arxiv.org/abs/2407.10930; https://dspy.ai/learn/optimization/optimizers/]

#### 2.3 Retrieval, demonstrations, and staged structure

- [fact] DSP frames knowledge-intensive tasks as a pipeline in which natural-language outputs from one step, including demonstrations and retrieved passages, become inputs to later steps, rather than as a single retrieve-then-read prompt. [source: https://arxiv.org/abs/2212.14024]
- [fact] DSP reports that this staged retrieval-plus-demonstration design yields large relative gains over both a vanilla language model and a standard retrieve-then-read baseline on open-domain, multi-hop, and conversational question answering tasks. [source: https://arxiv.org/abs/2212.14024]
- [fact] Infer-Retrieve-Rank uses DSPy plus optimizer-tuned traces to handle extreme multi-label classification, where it is infeasible to demonstrate every class directly in one prompt, by decomposing the task into inference, retrieval, and ranking stages. [source: https://arxiv.org/abs/2401.12178]
- [fact] STORM is not itself a prompt optimizer, but it shows that retrieval-backed, perspective-diverse intermediate artifacts and outlines can improve grounded long-form writing compared with a flatter retrieval-augmented generation baseline. [source: https://arxiv.org/abs/2402.14207; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-02-storm-perspective-discovery-multi-perspective-question-generation.md]
- [inference] Across DSP, Infer-Retrieve-Rank, and STORM, retrieval and demonstrations function as controllable external memory and task-structure variables, which means optimization can act on information routing and stage design instead of only on final answer wording. [source: https://arxiv.org/abs/2212.14024; https://arxiv.org/abs/2401.12178; https://arxiv.org/abs/2402.14207; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-02-storm-perspective-discovery-multi-perspective-question-generation.md]

#### 2.4 Why these methods beat baseline prompting and sometimes beat Reinforcement Learning

- [fact] GEPA explicitly argues that language is a richer learning medium than sparse scalar reward and attributes its gains over Reinforcement Learning to natural-language reflection over trajectories rather than pure policy-gradient updates. [source: https://arxiv.org/abs/2507.19457]
- [fact] DSPy reports that compiled programs for Generative Pre-trained Transformer 3.5 (GPT-3.5) and llama2-13b-chat outperform standard few-shot prompting by over 25 percent and 65 percent respectively, which shows that modular prompt and demonstration optimization can materially outperform baseline prompting. [source: https://arxiv.org/abs/2310.03714]
- [fact] MIPRO outperforms baseline optimizers on five of seven multi-stage language model programs by as much as 13 percent accuracy, which supports the view that data-aware and program-aware search improves module coordination beyond manual prompt editing. [source: https://arxiv.org/abs/2406.11695]
- [fact] BetterTogether reports that alternating prompt and weight optimization beats optimizing weights alone by up to 60 percent and prompts alone by up to 6 percent across several modular tasks, which shows that prompt optimization remains valuable even when fine-tuning is available. [source: https://arxiv.org/abs/2407.10930]
- [fact] Prompts as Auto-Optimized Training Hyperparameters shows that optimizing the prompt used to generate synthetic queries can train small information retrieval models that outperform much larger baselines trained with far more labels, which isolates prompt optimization as a high-leverage upstream control variable. [source: https://arxiv.org/abs/2406.11706]
- [inference] The shared gain mechanism is that these methods replace single-shot prompt authoring with repeated metric-guided search over interpretable interface parameters, so they receive denser and more localizable feedback than baseline prompting and, in some settings, richer supervision than sparse-reward Reinforcement Learning. [source: https://arxiv.org/abs/2507.19457; https://arxiv.org/abs/2406.11695; https://arxiv.org/abs/2310.03714; https://arxiv.org/abs/2407.10930]

#### 2.5 Practical selection criteria

- [inference] GEPA is best aligned to tasks where full trajectories, tool traces, or reasoning traces are available and rollout budget matters, because its core advantage comes from turning a small number of trajectory observations into high-level natural-language update rules. [source: https://arxiv.org/abs/2507.19457]
- [inference] DSPy and MIPRO are best aligned to modular pipelines with explicit evaluation metrics, because they search over per-module instructions and demonstrations while preserving program structure. [source: https://arxiv.org/abs/2406.11695; https://arxiv.org/abs/2310.03714; https://dspy.ai/learn/optimization/optimizers/]
- [inference] DSPy Assertions are most useful when reliability requirements can be expressed as explicit output or process constraints, because assertion failures become additional optimization and repair signals. [source: https://arxiv.org/abs/2312.13382; https://github.com/stanfordnlp/dspy/blob/main/docs/docs/faqs.md]
- [inference] BetterTogether is best aligned to settings with enough budget and data to support alternating prompt search and fine-tuning, because its advantage depends on prompt updates and weight updates reinforcing one another. [source: https://arxiv.org/abs/2407.10930; https://dspy.ai/learn/optimization/optimizers/]
- [inference] DSP, Infer-Retrieve-Rank, and STORM are strongest where the bottleneck is missing knowledge, class coverage, or information organization rather than a single flat instruction, because their staged retrieval and intermediate artifacts change the information available to later modules. [source: https://arxiv.org/abs/2212.14024; https://arxiv.org/abs/2401.12178; https://arxiv.org/abs/2402.14207]

### §3 Reasoning

- [fact] Mechanism claims about GEPA, MIPRO, DSPy, DSPy Assertions, BetterTogether, DSP, and Infer-Retrieve-Rank were taken from primary paper abstracts and official DSPy documentation rather than from tertiary summaries. [source: https://arxiv.org/abs/2507.19457; https://arxiv.org/abs/2406.11695; https://arxiv.org/abs/2310.03714; https://arxiv.org/abs/2407.10930; https://arxiv.org/abs/2406.11706; https://arxiv.org/abs/2312.13382; https://arxiv.org/abs/2212.14024; https://arxiv.org/abs/2401.12178; https://dspy.ai/learn/optimization/optimizers/]
- [inference] The unifying theory is an inference rather than a direct fact because no single source compares all surveyed methods under one theoretical frame; it emerges from their common treatment of prompts, demonstrations, retrieval context, constraints, and lightweight program structure as search variables tied to downstream metrics. [source: https://arxiv.org/abs/2507.19457; https://arxiv.org/abs/2406.11695; https://arxiv.org/abs/2310.03714; https://arxiv.org/abs/2407.10930]
- [inference] STORM is used as adjacent evidence for the value of staged retrieved intermediate artifacts, not as direct evidence about optimizer design, because its contribution is pre-writing decomposition rather than prompt search. [source: https://arxiv.org/abs/2402.14207; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-02-storm-perspective-discovery-multi-perspective-question-generation.md]
- [assumption] Current DSPy documentation is a valid source for present optimizer names and interfaces, even though the underlying papers and docs span 2023 through 2026, because the documentation explicitly maps MIPROv2, GEPA, BootstrapFewShot, and BetterTogether back to their paper families. [source: https://dspy.ai/learn/optimization/optimizers/; https://arxiv.org/abs/2406.11695; https://arxiv.org/abs/2507.19457; https://arxiv.org/abs/2407.10930]

### §4 Consistency Check

- [fact] GEPA and MIPRO describe different search procedures, reflection-guided prompt revision versus surrogate-guided instruction and demonstration search, but both remain consistent with the same higher-level idea of metric-guided search over interpretable prompt-program variables. [source: https://arxiv.org/abs/2507.19457; https://arxiv.org/abs/2406.11695]
- [fact] BetterTogether does not contradict prompt-first optimizers, because it keeps prompt optimization in the loop and argues that prompt and weight updates can be sequenced to reinforce each other rather than treated as substitutes. [source: https://arxiv.org/abs/2407.10930; https://dspy.ai/learn/optimization/optimizers/]
- [fact] DSP, Infer-Retrieve-Rank, and STORM all support the claim that staged retrieval or intermediate artifact design matters, even though only DSP and Infer-Retrieve-Rank are directly optimizer-adjacent methods. [source: https://arxiv.org/abs/2212.14024; https://arxiv.org/abs/2401.12178; https://arxiv.org/abs/2402.14207]
- [inference] No material contradiction remains after separating direct optimizer papers from adjacent staged-pipeline evidence, because the adjacent papers are used only to support the role of intermediate structure and retrieved context. [source: https://arxiv.org/abs/2402.14207; https://arxiv.org/abs/2212.14024; https://arxiv.org/abs/2401.12178]

### §5 Depth and Breadth Expansion

- [inference] **Technical lens:** prompt and program optimization is strongest where the task can be decomposed into interpretable modules or explicit traces, because search can then localize change to a prompt, demo set, retrieval hop, or constraint boundary rather than perturbing the whole model. [source: https://arxiv.org/abs/2406.11695; https://arxiv.org/abs/2310.03714; https://arxiv.org/abs/2212.14024]
- [inference] **Economic lens:** these methods are especially attractive when labels, gradients, or local training infrastructure are scarce, because they shift adaptation effort toward prompt search, synthetic data, and metric-guided compilation. [source: https://arxiv.org/abs/2407.10930; https://arxiv.org/abs/2406.11706; https://dspy.ai/learn/optimization/optimizers/]
- [inference] **Historical lens:** the sequence DSP to DSPy to MIPRO, Assertions, GEPA, and BetterTogether shows a widening search space, from retrieval-composed prompt pipelines toward explicit optimization over demonstrations, constraints, prompt text, and finally model weights. [source: https://arxiv.org/abs/2212.14024; https://arxiv.org/abs/2310.03714; https://arxiv.org/abs/2406.11695; https://arxiv.org/abs/2312.13382; https://arxiv.org/abs/2507.19457; https://arxiv.org/abs/2407.10930]
- [inference] **Behavioural lens:** demonstrations and assertions help stabilize optimization because they express expected behaviour in concrete examples or checks, which reduces the risk that search improves one metric by silently changing the intended task. [source: https://arxiv.org/abs/2312.13382; https://dspy.ai/learn/optimization/optimizers/; https://arxiv.org/abs/2401.12178]

### §6 Synthesis

**Executive Summary**

Prompt and program optimization are best explained as metric-guided search over interpretable interface parameters, instructions, demonstrations, retrieval state, constraints, and lightweight program structure, rather than as one-shot prompt writing or pure reward-maximizing policy updates. [inference; source: https://arxiv.org/abs/2507.19457; https://arxiv.org/abs/2406.11695; https://arxiv.org/abs/2310.03714; https://arxiv.org/abs/2407.10930] These methods outperform baseline prompting because they repeatedly test and revise concrete control variables against downstream task metrics instead of relying on a static prompt chosen once by hand. [inference; source: https://arxiv.org/abs/2406.11695; https://arxiv.org/abs/2310.03714; https://arxiv.org/abs/2406.11706] Part of the reported gain also comes from added task structure, retrieval decomposition, and search budget, but the common pattern across the papers is that these structural changes matter when they are turned into searchable program variables rather than left fixed. [inference; source: https://arxiv.org/abs/2212.14024; https://arxiv.org/abs/2401.12178; https://arxiv.org/abs/2402.14207; https://arxiv.org/abs/2406.11695] These methods can outperform Reinforcement Learning when natural-language reflections, module traces, assertion failures, or retrieval-stage outputs provide richer and more localizable supervision than sparse scalar rewards. [inference; source: https://arxiv.org/abs/2507.19457; https://arxiv.org/abs/2312.13382; https://arxiv.org/abs/2212.14024] Among the surveyed families, GEPA specializes this theory around trajectory reflection, DSPy and MIPRO specialize it around modular program compilation and surrogate-guided search, Assertions specialize it around explicit reliability constraints, BetterTogether specializes it around alternating prompt and weight updates, and DSP-style retrieval programs specialize it around information routing. [inference; source: https://arxiv.org/abs/2507.19457; https://arxiv.org/abs/2406.11695; https://arxiv.org/abs/2310.03714; https://arxiv.org/abs/2312.13382; https://arxiv.org/abs/2407.10930; https://arxiv.org/abs/2212.14024] The practical consequence is that optimizer choice should be driven by where the task exposes useful feedback, full trajectories, modular metrics, explicit constraints, or retrieval bottlenecks, rather than by a generic belief that one method is globally best. [inference; source: https://arxiv.org/abs/2507.19457; https://arxiv.org/abs/2406.11695; https://arxiv.org/abs/2407.10930; https://arxiv.org/abs/2401.12178]

**Key Findings**

1. **Prompt and program optimization outperform baseline prompting because they convert instructions, demonstrations, retrieval context, constraints, and lightweight program structure into explicit search variables, and many of the gains attributed to better prompts are really gains from making those structural choices searchable instead of fixed.** ([inference]; high confidence; source: https://arxiv.org/abs/2406.11695; https://arxiv.org/abs/2310.03714; https://arxiv.org/abs/2212.14024; https://arxiv.org/abs/2406.11706)
2. **These methods can outperform Reinforcement Learning when the system exposes richer supervision than sparse scalar reward, but where gains come mainly from added retrieval stages or larger search budgets the advantage is structural rather than proof that natural-language feedback is always superior.** ([inference]; medium confidence; source: https://arxiv.org/abs/2507.19457; https://arxiv.org/abs/2312.13382; https://arxiv.org/abs/2212.14024; https://arxiv.org/abs/2401.12178)
3. **GEPA operationalizes this theory through trajectory sampling, natural-language diagnosis, prompt revision, and combination of complementary high-performing updates, and the paper reports average gains over Group Relative Policy Optimization with far fewer rollouts.** ([fact]; medium confidence; source: https://arxiv.org/abs/2507.19457)
4. **MIPRO operationalizes the same theory for modular pipelines by bootstrapping demonstrations, drafting program-aware and data-aware instructions, and using stochastic mini-batch search with a surrogate model over instruction and demonstration bundles.** ([fact]; medium confidence; source: https://arxiv.org/abs/2406.11695; https://dspy.ai/learn/optimization/optimizers/)
5. **DSPy broadens prompt optimization into program optimization by representing a language model pipeline as typed modules and signatures whose prompts, demonstrations, and optionally weights can all be compiled against a user-specified metric rather than tuned as brittle prompt strings.** ([fact]; medium confidence; source: https://arxiv.org/abs/2310.03714; https://dspy.ai/learn/optimization/optimizers/)
6. **DSPy Assertions extend optimization beyond accuracy by turning explicit computational constraints into compile-time and inference-time self-refinement signals, which lets the system optimize for both task success and rule compliance together.** ([fact]; medium confidence; source: https://arxiv.org/abs/2312.13382; https://github.com/stanfordnlp/dspy/blob/main/docs/docs/faqs.md)
7. **Retrieval-centered methods such as DSP and Infer-Retrieve-Rank work because they optimize information routing and class coverage through staged retrieval and demonstrations, which is especially valuable when missing knowledge or huge label spaces are the real bottleneck rather than raw model capability.** ([inference]; high confidence; source: https://arxiv.org/abs/2212.14024; https://arxiv.org/abs/2401.12178)
8. **BetterTogether and prompt-as-hyperparameter work indicate that prompt optimization can complement weight optimization or synthetic-data generation in some modular settings, because prompt search can discover useful decompositions or data-creation procedures that later training exploits.** ([inference]; medium confidence; source: https://arxiv.org/abs/2407.10930; https://arxiv.org/abs/2406.11706)
9. **The best method depends on where useful feedback lives: GEPA fits trajectory-rich reasoning or tool tasks, DSPy and MIPRO fit modular pipelines with explicit metrics, Assertions fit reliability-constrained systems, and DSP-style retrieval programs fit knowledge-intensive tasks with information-routing bottlenecks.** ([inference]; medium confidence; source: https://arxiv.org/abs/2507.19457; https://arxiv.org/abs/2406.11695; https://arxiv.org/abs/2312.13382; https://arxiv.org/abs/2212.14024)

**Evidence Map**

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [inference] Prompt and program optimization work by turning interface variables into search variables tied to metrics. | https://arxiv.org/abs/2406.11695; https://arxiv.org/abs/2310.03714; https://arxiv.org/abs/2406.11706 | high | Shared mechanism |
| [inference] Rich trajectory or constraint feedback can beat sparse-reward optimization in some settings. | https://arxiv.org/abs/2507.19457; https://arxiv.org/abs/2312.13382; https://dspy.ai/learn/optimization/optimizers/ | medium | Cross-paper synthesis |
| [fact] GEPA uses reflection-guided prompt revision and reports rollout-efficient gains over GRPO. | https://arxiv.org/abs/2507.19457 | medium | Single paper |
| [fact] MIPRO uses bootstrapping, grounded proposals, and surrogate-guided search over instruction and demo bundles. | https://arxiv.org/abs/2406.11695; https://dspy.ai/learn/optimization/optimizers/ | medium | Paper plus project docs |
| [fact] DSPy exposes modular program structure so prompts, demos, and weights can be compiled against metrics. | https://arxiv.org/abs/2310.03714; https://dspy.ai/learn/optimization/optimizers/ | medium | Paper plus project docs |
| [fact] DSPy Assertions turn explicit constraints into optimization and self-refinement signals. | https://arxiv.org/abs/2312.13382; https://github.com/stanfordnlp/dspy/blob/main/docs/docs/faqs.md | medium | Paper plus project docs |
| [inference] Retrieval-centered methods improve performance by optimizing information routing and class coverage, not only final answer wording. | https://arxiv.org/abs/2212.14024; https://arxiv.org/abs/2401.12178; https://arxiv.org/abs/2402.14207 | high | Staged retrieval evidence |
| [inference] BetterTogether and prompt-as-hyperparameter work indicate prompt search can complement weight or data optimization in some settings. | https://arxiv.org/abs/2407.10930; https://arxiv.org/abs/2406.11706 | medium | Task-specific evidence |
| [inference] Method choice should follow the task's feedback surface, not a single universal ranking. | https://arxiv.org/abs/2507.19457; https://arxiv.org/abs/2406.11695; https://arxiv.org/abs/2312.13382; https://arxiv.org/abs/2212.14024 | medium | Selection synthesis |

**Assumptions**

- [assumption] Comparing mechanism-level theory from abstracts and official documentation is sufficient for this item because the question asks how the methods work conceptually, not for a re-analysis of every experimental appendix or ablation table. **Justification:** the required objects, loops, and feedback signals are stated directly in the paper abstracts and optimizer docs used here. [source: https://arxiv.org/abs/2507.19457; https://arxiv.org/abs/2406.11695; https://arxiv.org/abs/2310.03714; https://dspy.ai/learn/optimization/optimizers/]
- [assumption] Current DSPy documentation can be used alongside the 2023 and 2024 papers when extracting selection criteria because the docs explicitly map current optimizer names and stages back to the paper-defined mechanisms. **Justification:** the optimizer documentation cross-links MIPROv2, GEPA, and BetterTogether to their corresponding papers. [source: https://dspy.ai/learn/optimization/optimizers/; https://arxiv.org/abs/2406.11695; https://arxiv.org/abs/2507.19457; https://arxiv.org/abs/2407.10930]

**Analysis**

The strongest common thread across the surveyed work is not "better prompts" in the casual prompt-engineering sense, but repeated search over interpretable control variables that sit at the interface between modules and the model. [inference; source: https://arxiv.org/abs/2406.11695; https://arxiv.org/abs/2310.03714; https://arxiv.org/abs/2406.11706] A plausible rival explanation is that gains come mainly from extra task structure, retrieval decomposition, or larger search budgets rather than from feedback richness itself. [inference; source: https://arxiv.org/abs/2212.14024; https://arxiv.org/abs/2401.12178; https://arxiv.org/abs/2402.14207; https://arxiv.org/abs/2406.11695] The evidence here suggests those are not separate rival mechanisms so much as the concrete surfaces on which search operates, because the reported improvements appear when those added stages are exposed as optimizable prompts, demonstrations, retrieval hops, or constraints. [inference; source: https://arxiv.org/abs/2406.11695; https://arxiv.org/abs/2212.14024; https://arxiv.org/abs/2401.12178; https://arxiv.org/abs/2312.13382] GEPA and MIPRO differ mainly in how they do credit assignment, GEPA reads complete trajectories and writes natural-language update rules, while MIPRO decomposes a pipeline into modules and searches over instruction and demonstration bundles with surrogate-guided evaluation. [inference; source: https://arxiv.org/abs/2507.19457; https://arxiv.org/abs/2406.11695] DSPy and DSPy Assertions matter because they expose program structure and explicit constraints, which creates more places for optimization to receive informative feedback than a single flat prompt can provide. [inference; source: https://arxiv.org/abs/2310.03714; https://arxiv.org/abs/2312.13382] This sharpens the broader recommendation in the General Agent Optimization Framework item: DSPy remains the best base framework, but the reason is its exposure of modular search variables and measurable optimization loops rather than packaging convenience alone. [inference; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-05-general-agent-optimization-framework.md; https://arxiv.org/abs/2310.03714; https://dspy.ai/learn/optimization/optimizers/]

**Risks, gaps, uncertainties**

- The unifying theory is a synthesis across papers, not a single published theorem, so the highest-confidence claims are about individual mechanisms rather than about one formally proved general law. [inference; source: https://arxiv.org/abs/2507.19457; https://arxiv.org/abs/2406.11695; https://arxiv.org/abs/2310.03714]
- GEPA is very recent, so the evidence for its superiority over Reinforcement Learning comes mainly from its own paper rather than from a broad replication literature. [fact; source: https://arxiv.org/abs/2507.19457]
- BetterTogether and prompt-as-hyperparameter results are task-specific, so the complementarity of prompt and weight optimization is well supported for the reported settings but not yet guaranteed for every pipeline shape. [inference; source: https://arxiv.org/abs/2407.10930; https://arxiv.org/abs/2406.11706]
- STORM is adjacent evidence about staged retrieved artifacts rather than a direct optimizer comparison, so it should qualify the information-routing argument rather than carry the core optimizer claim by itself. [fact; source: https://arxiv.org/abs/2402.14207; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-02-storm-perspective-discovery-multi-perspective-question-generation.md]

**Open Questions**

- When both are available inside DSPy, what empirical threshold should trigger GEPA instead of MIPROv2 for a modular program with tool traces? [inference; source: https://arxiv.org/abs/2507.19457; https://dspy.ai/learn/optimization/optimizers/]
- Can assertions, retrieval policy, and weight updates be optimized jointly without destabilizing search or creating conflicting objectives? [inference; source: https://arxiv.org/abs/2312.13382; https://arxiv.org/abs/2407.10930]
- What evaluation metric best captures reliability when constraint satisfaction and task accuracy trade off against each other in self-refining pipelines? [inference; source: https://arxiv.org/abs/2312.13382; https://dspy.ai/learn/optimization/optimizers/]

### §7 Recursive Review

```yaml
review_result: pass
checks:
  - acronym expansion verified
  - claim labels verified
  - URL-backed citations verified
  - cross-item integration verified
  - synthesis-findings parity verified
```

---

## Findings

### Executive Summary

Prompt and program optimization are best explained as metric-guided search over interpretable interface parameters, instructions, demonstrations, retrieval state, constraints, and lightweight program structure, rather than as one-shot prompt writing or pure reward-maximizing policy updates. [inference; source: https://arxiv.org/abs/2507.19457; https://arxiv.org/abs/2406.11695; https://arxiv.org/abs/2310.03714; https://arxiv.org/abs/2407.10930] These methods outperform baseline prompting because they repeatedly test and revise concrete control variables against downstream task metrics instead of relying on a static prompt chosen once by hand. [inference; source: https://arxiv.org/abs/2406.11695; https://arxiv.org/abs/2310.03714; https://arxiv.org/abs/2406.11706] Part of the reported gain also comes from added task structure, retrieval decomposition, and search budget, but the common pattern across the papers is that these structural changes matter when they are turned into searchable program variables rather than left fixed. [inference; source: https://arxiv.org/abs/2212.14024; https://arxiv.org/abs/2401.12178; https://arxiv.org/abs/2402.14207; https://arxiv.org/abs/2406.11695] These methods can outperform Reinforcement Learning when natural-language reflections, module traces, assertion failures, or retrieval-stage outputs provide richer and more localizable supervision than sparse scalar rewards. [inference; source: https://arxiv.org/abs/2507.19457; https://arxiv.org/abs/2312.13382; https://arxiv.org/abs/2212.14024] Among the surveyed families, GEPA specializes this theory around trajectory reflection, DSPy and MIPRO specialize it around modular program compilation and surrogate-guided search, Assertions specialize it around explicit reliability constraints, BetterTogether specializes it around alternating prompt and weight updates, and DSP-style retrieval programs specialize it around information routing. [inference; source: https://arxiv.org/abs/2507.19457; https://arxiv.org/abs/2406.11695; https://arxiv.org/abs/2310.03714; https://arxiv.org/abs/2312.13382; https://arxiv.org/abs/2407.10930; https://arxiv.org/abs/2212.14024] The practical consequence is that optimizer choice should be driven by where the task exposes useful feedback, full trajectories, modular metrics, explicit constraints, or retrieval bottlenecks, rather than by a generic belief that one method is globally best. [inference; source: https://arxiv.org/abs/2507.19457; https://arxiv.org/abs/2406.11695; https://arxiv.org/abs/2407.10930; https://arxiv.org/abs/2401.12178]

### Key Findings

1. **Prompt and program optimization outperform baseline prompting because they convert instructions, demonstrations, retrieval context, constraints, and lightweight program structure into explicit search variables, and many of the gains attributed to better prompts are really gains from making those structural choices searchable instead of fixed.** ([inference]; high confidence; source: https://arxiv.org/abs/2406.11695; https://arxiv.org/abs/2310.03714; https://arxiv.org/abs/2212.14024; https://arxiv.org/abs/2406.11706)
2. **These methods can outperform Reinforcement Learning when the system exposes richer supervision than sparse scalar reward, but where gains come mainly from added retrieval stages or larger search budgets the advantage is structural rather than proof that natural-language feedback is always superior.** ([inference]; medium confidence; source: https://arxiv.org/abs/2507.19457; https://arxiv.org/abs/2312.13382; https://arxiv.org/abs/2212.14024; https://arxiv.org/abs/2401.12178)
3. **GEPA operationalizes this theory through trajectory sampling, natural-language diagnosis, prompt revision, and combination of complementary high-performing updates, and the paper reports average gains over Group Relative Policy Optimization with far fewer rollouts.** ([fact]; medium confidence; source: https://arxiv.org/abs/2507.19457)
4. **MIPRO operationalizes the same theory for modular pipelines by bootstrapping demonstrations, drafting program-aware and data-aware instructions, and using stochastic mini-batch search with a surrogate model over instruction and demonstration bundles.** ([fact]; medium confidence; source: https://arxiv.org/abs/2406.11695; https://dspy.ai/learn/optimization/optimizers/)
5. **DSPy broadens prompt optimization into program optimization by representing a language model pipeline as typed modules and signatures whose prompts, demonstrations, and optionally weights can all be compiled against a user-specified metric rather than tuned as brittle prompt strings.** ([fact]; medium confidence; source: https://arxiv.org/abs/2310.03714; https://dspy.ai/learn/optimization/optimizers/)
6. **DSPy Assertions extend optimization beyond accuracy by turning explicit computational constraints into compile-time and inference-time self-refinement signals, which lets the system optimize for both task success and rule compliance together.** ([fact]; medium confidence; source: https://arxiv.org/abs/2312.13382; https://github.com/stanfordnlp/dspy/blob/main/docs/docs/faqs.md)
7. **Retrieval-centered methods such as DSP and Infer-Retrieve-Rank work because they optimize information routing and class coverage through staged retrieval and demonstrations, which is especially valuable when missing knowledge or huge label spaces are the real bottleneck rather than raw model capability.** ([inference]; high confidence; source: https://arxiv.org/abs/2212.14024; https://arxiv.org/abs/2401.12178)
8. **BetterTogether and prompt-as-hyperparameter work indicate that prompt optimization can complement weight optimization or synthetic-data generation in some modular settings, because prompt search can discover useful decompositions or data-creation procedures that later training exploits.** ([inference]; medium confidence; source: https://arxiv.org/abs/2407.10930; https://arxiv.org/abs/2406.11706)
9. **The best method depends on where useful feedback lives: GEPA fits trajectory-rich reasoning or tool tasks, DSPy and MIPRO fit modular pipelines with explicit metrics, Assertions fit reliability-constrained systems, and DSP-style retrieval programs fit knowledge-intensive tasks with information-routing bottlenecks.** ([inference]; medium confidence; source: https://arxiv.org/abs/2507.19457; https://arxiv.org/abs/2406.11695; https://arxiv.org/abs/2312.13382; https://arxiv.org/abs/2212.14024)

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [inference] Prompt and program optimization work by turning interface variables into search variables tied to metrics. | https://arxiv.org/abs/2406.11695; https://arxiv.org/abs/2310.03714; https://arxiv.org/abs/2406.11706 | high | Shared mechanism |
| [inference] Rich trajectory or constraint feedback can beat sparse-reward optimization in some settings. | https://arxiv.org/abs/2507.19457; https://arxiv.org/abs/2312.13382; https://dspy.ai/learn/optimization/optimizers/ | medium | Cross-paper synthesis |
| [fact] GEPA uses reflection-guided prompt revision and reports rollout-efficient gains over GRPO. | https://arxiv.org/abs/2507.19457 | medium | Single paper |
| [fact] MIPRO uses bootstrapping, grounded proposals, and surrogate-guided search over instruction and demo bundles. | https://arxiv.org/abs/2406.11695; https://dspy.ai/learn/optimization/optimizers/ | medium | Paper plus project docs |
| [fact] DSPy exposes modular program structure so prompts, demos, and weights can be compiled against metrics. | https://arxiv.org/abs/2310.03714; https://dspy.ai/learn/optimization/optimizers/ | medium | Paper plus project docs |
| [fact] DSPy Assertions turn explicit constraints into optimization and self-refinement signals. | https://arxiv.org/abs/2312.13382; https://github.com/stanfordnlp/dspy/blob/main/docs/docs/faqs.md | medium | Paper plus project docs |
| [inference] Retrieval-centered methods improve performance by optimizing information routing and class coverage, not only final answer wording. | https://arxiv.org/abs/2212.14024; https://arxiv.org/abs/2401.12178; https://arxiv.org/abs/2402.14207 | high | Staged retrieval evidence |
| [inference] BetterTogether and prompt-as-hyperparameter work indicate prompt search can complement weight or data optimization in some settings. | https://arxiv.org/abs/2407.10930; https://arxiv.org/abs/2406.11706 | medium | Task-specific evidence |
| [inference] Method choice should follow the task's feedback surface, not a single universal ranking. | https://arxiv.org/abs/2507.19457; https://arxiv.org/abs/2406.11695; https://arxiv.org/abs/2312.13382; https://arxiv.org/abs/2212.14024 | medium | Selection synthesis |

### Assumptions

- [assumption] Comparing mechanism-level theory from abstracts and official documentation is sufficient for this item because the question asks how the methods work conceptually, not for a re-analysis of every experimental appendix or ablation table. **Justification:** the required objects, loops, and feedback signals are stated directly in the paper abstracts and optimizer docs used here. [source: https://arxiv.org/abs/2507.19457; https://arxiv.org/abs/2406.11695; https://arxiv.org/abs/2310.03714; https://dspy.ai/learn/optimization/optimizers/]
- [assumption] Current DSPy documentation can be used alongside the 2023 and 2024 papers when extracting selection criteria because the docs explicitly map current optimizer names and stages back to the paper-defined mechanisms. **Justification:** the optimizer documentation cross-links MIPROv2, GEPA, and BetterTogether to their corresponding papers. [source: https://dspy.ai/learn/optimization/optimizers/; https://arxiv.org/abs/2406.11695; https://arxiv.org/abs/2507.19457; https://arxiv.org/abs/2407.10930]

### Analysis

The strongest common thread across the surveyed work is not "better prompts" in the casual prompt-engineering sense, but repeated search over interpretable control variables that sit at the interface between modules and the model. [inference; source: https://arxiv.org/abs/2406.11695; https://arxiv.org/abs/2310.03714; https://arxiv.org/abs/2406.11706] A plausible rival explanation is that gains come mainly from extra task structure, retrieval decomposition, or larger search budgets rather than from feedback richness itself. [inference; source: https://arxiv.org/abs/2212.14024; https://arxiv.org/abs/2401.12178; https://arxiv.org/abs/2402.14207; https://arxiv.org/abs/2406.11695] The evidence here suggests those are not separate rival mechanisms so much as the concrete surfaces on which search operates, because the reported improvements appear when those added stages are exposed as optimizable prompts, demonstrations, retrieval hops, or constraints. [inference; source: https://arxiv.org/abs/2406.11695; https://arxiv.org/abs/2212.14024; https://arxiv.org/abs/2401.12178; https://arxiv.org/abs/2312.13382] GEPA and MIPRO differ mainly in how they do credit assignment, GEPA reads complete trajectories and writes natural-language update rules, while MIPRO decomposes a pipeline into modules and searches over instruction and demonstration bundles with surrogate-guided evaluation. [inference; source: https://arxiv.org/abs/2507.19457; https://arxiv.org/abs/2406.11695] DSPy and DSPy Assertions matter because they expose program structure and explicit constraints, which creates more places for optimization to receive informative feedback than a single flat prompt can provide. [inference; source: https://arxiv.org/abs/2310.03714; https://arxiv.org/abs/2312.13382] This sharpens the broader recommendation in the General Agent Optimization Framework item: DSPy remains the best base framework, but the reason is its exposure of modular search variables and measurable optimization loops rather than packaging convenience alone. [inference; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-05-general-agent-optimization-framework.md; https://arxiv.org/abs/2310.03714; https://dspy.ai/learn/optimization/optimizers/]

### Risks, Gaps, and Uncertainties

- The unifying theory is a synthesis across papers, not a single published theorem, so the highest-confidence claims are about individual mechanisms rather than about one formally proved general law. [inference; source: https://arxiv.org/abs/2507.19457; https://arxiv.org/abs/2406.11695; https://arxiv.org/abs/2310.03714]
- GEPA is very recent, so the evidence for its superiority over Reinforcement Learning comes mainly from its own paper rather than from a broad replication literature. [fact; source: https://arxiv.org/abs/2507.19457]
- BetterTogether and prompt-as-hyperparameter results are task-specific, so the complementarity of prompt and weight optimization is well supported for the reported settings but not yet guaranteed for every pipeline shape. [inference; source: https://arxiv.org/abs/2407.10930; https://arxiv.org/abs/2406.11706]
- STORM is adjacent evidence about staged retrieved artifacts rather than a direct optimizer comparison, so it should qualify the information-routing argument rather than carry the core optimizer claim by itself. [fact; source: https://arxiv.org/abs/2402.14207; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-02-storm-perspective-discovery-multi-perspective-question-generation.md]

### Open Questions

- When both are available inside DSPy, what empirical threshold should trigger GEPA instead of MIPROv2 for a modular program with tool traces? [inference; source: https://arxiv.org/abs/2507.19457; https://dspy.ai/learn/optimization/optimizers/]
- Can assertions, retrieval policy, and weight updates be optimized jointly without destabilizing search or creating conflicting objectives? [inference; source: https://arxiv.org/abs/2312.13382; https://arxiv.org/abs/2407.10930]
- What evaluation metric best captures reliability when constraint satisfaction and task accuracy trade off against each other in self-refining pipelines? [inference; source: https://arxiv.org/abs/2312.13382; https://dspy.ai/learn/optimization/optimizers/]

---

## Output

- Type: knowledge
- Description: This item produces a theory-level comparison of GEPA, MIPRO, DSPy, DSPy Assertions, BetterTogether, DSP, Infer-Retrieve-Rank, and STORM, and extracts practical selection criteria for future language model pipeline design. [inference; source: https://arxiv.org/abs/2507.19457; https://arxiv.org/abs/2406.11695; https://arxiv.org/abs/2310.03714; https://arxiv.org/abs/2407.10930; https://arxiv.org/abs/2212.14024]
- Links:
  - https://arxiv.org/abs/2507.19457
  - https://arxiv.org/abs/2406.11695
  - https://arxiv.org/abs/2310.03714
