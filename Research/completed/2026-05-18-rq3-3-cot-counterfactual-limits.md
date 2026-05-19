---
review_count: 2
title: "RQ 3.3: In-Context Learning and chain-of-thought (CoT) Prompting, Genuine Causal Reasoning or Extended Statistical Interpolation?"
added: 2026-05-18T19:40:00+00:00
status: completed
priority: high
blocks:
  - 2026-05-18-rq4-1-agentic-loop-explanatory-reach
tags: [llm, machine-learning, evaluation, causal-inference]
started: 2026-05-19T11:03:35+00:00
completed: 2026-05-19T11:30:23+00:00
output: [knowledge]
cites:
  - 2026-05-18-rq2-4-causal-hierarchy-formal-limits
  - 2026-05-18-rq3-1-llm-statistical-vs-causal
  - 2026-05-18-rq3-2-stochastic-parrot-ood
related:
  - 2026-05-18-rq2-1-erm-causal-blindness
  - 2026-05-18-rq2-3-predictive-model-fragility
superseded_by: ~
supersedes: ~
item_type: primary
confidence: medium
versions: []
---

# RQ 3.3: In-Context Learning and chain-of-thought (CoT) Prompting, Genuine Causal Reasoning or Extended Statistical Interpolation?

## Research Question

What are the empirical boundaries of in-context learning and chain-of-thought prompting when they are used to push a purely predictive statistical architecture toward intervention questions and alternate-world causal questions?

## Scope

**In scope:**
- In-context learning (ICL) as a mechanism, including whether it is best characterised as implicit regression, Bayesian inference, gradient descent, or a related prompt-time learning process.
- chain-of-thought (CoT) prompting as sequential intermediate-text generation rather than as a claim about genuine causal semantics.
- Autoregressive error accumulation in multi-step CoT sequences.
- Spurious reasoning trajectories, including cases where CoT yields a correct answer through an incorrect or weakly connected reasoning path.
- Formal classification of whether CoT moves a Large Language Model (LLM) beyond Level 1 association on Pearl's causal hierarchy.

**Out of scope:**
- Fine-tuning approaches that explicitly incorporate causal graphs, simulators, or interventional datasets.
- Prompt-engineering advice whose only aim is to raise benchmark accuracy.

**Constraints:** This item must interpret findings through Pearl's causal hierarchy and through the prior conclusions from Research Questions 3.1 and 3.2.

## Context

Research Question 3.2 concluded that Large Language Models (LLMs) fail systematically when prompts require structural intervention or genuinely novel composition outside familiar text patterns. [fact; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq3-2-stochastic-parrot-ood.md]

Pearl's three-layer hierarchy defines intervention questions as do-operator queries and counterfactual questions as alternate-world queries about what would have happened under a different action. [fact; source: https://web.cs.ucla.edu/~kaoru/3-layer-causal-hierarchy.pdf; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq2-4-causal-hierarchy-formal-limits.md]

This item asks whether in-context learning (ICL) and chain-of-thought (CoT) prompting add that missing causal structure or whether they mainly lengthen Level 1 search over conditional text continuations. [inference; source: https://arxiv.org/abs/2211.15661; https://arxiv.org/abs/2201.11903; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq3-1-llm-statistical-vs-causal.md]

## Approach

1. Characterise ICL as a computational process: does it resemble Bayesian updating, gradient descent, ridge regression, latent-concept inference, or a mixture of these in controlled settings?
2. Characterise CoT as a sequence of conditional predictions over intermediate text rather than as direct evidence of causal-mechanism representation.
3. Test whether CoT enables Level 2 intervention or Level 3 counterfactual performance on current causal benchmarks, especially on unseen or structurally harder tasks.
4. Analyse why multi-step CoT can degrade: how do single-path commitments, faithfulness failures, and missing backtracking affect end-to-end reliability?
5. Classify the overall result on Pearl's hierarchy: genuine causal reach, narrow partial abstraction, or extended statistical interpolation.

## Sources

- [x] [Wei et al. (2023) Chain-of-Thought Prompting Elicits Reasoning in Large Language Models](https://arxiv.org/abs/2201.11903) - consulted as the primary source for CoT prompting gains.
- [ ] [Pearl and Mackenzie (2018) The Book of Why](https://www.basicbooks.com/titles/judea-pearl/the-book-of-why/9780465097609/) - checked as a bibliographic locator only; hierarchy claims below come from accessible Pearl and Bareinboim sources.
- [x] [Akyurek et al. (2023) What Learning Algorithm Is In-Context Learning? Investigations with Linear Models](https://arxiv.org/abs/2211.15661) - consulted for the strongest controlled evidence that ICL can implement standard estimators in linear settings.
- [ ] [Zeiler and Fergus (2014) Visualizing and Understanding Convolutional Networks](https://doi.org/10.1007/978-3-319-10590-1_53) - checked through the DOI landing only and not used for claim extraction.
- [x] [Xie et al. (2022) An Explanation of In-Context Learning as Implicit Bayesian Inference](https://arxiv.org/abs/2111.02080) - consulted for the latent-concept and Bayesian-inference account of ICL emergence.
- [x] [von Oswald et al. (2023) Transformers Learn In-Context by Gradient Descent](https://arxiv.org/abs/2212.07677) - consulted for the gradient-descent account of ICL.
- [x] [Wang et al. (2023) Self-Consistency Improves Chain of Thought Reasoning in Language Models](https://arxiv.org/abs/2203.11171) - consulted for evidence that multiple sampled reasoning paths outperform one greedy chain.
- [x] [Yao et al. (2023) Tree of Thoughts: Deliberate Problem Solving with Large Language Models](https://openreview.net/forum?id=5Xc1ecxO1h) - consulted for evidence that single left-to-right CoT is brittle on tasks requiring search or backtracking.
- [x] [Turpin et al. (2023) Language Models Don't Always Say What They Think: Unfaithful Explanations in chain-of-thought Prompting](https://arxiv.org/abs/2305.04388) - consulted for direct evidence that CoT explanations can misrepresent the true basis of a prediction.
- [x] [Lanham et al. (2023) Measuring Faithfulness in Chain-of-Thought Reasoning](https://arxiv.org/abs/2307.13702) - consulted for intervention-based evidence that larger models often condition less faithfully on their visible CoT.
- [x] [Anthropic (2023) Measuring Faithfulness in Chain-of-Thought Reasoning](https://www.anthropic.com/research/measuring-faithfulness-in-chain-of-thought-reasoning) - consulted as an accessible mirror of the Lanham et al. abstract.
- [x] [Yang et al. (2024) A Critical Review of Causal Reasoning Benchmarks for Large Language Models](https://arxiv.org/abs/2407.08029) - consulted for the benchmark-design critique.
- [x] [Zhou et al. (2024) CausalBench: A Comprehensive Benchmark for Causal Learning Capability of Large Language Models](https://arxiv.org/abs/2404.06349) - consulted for comparative evidence against traditional causal algorithms.
- [x] [Wang et al. (2024) CausalBench: A Comprehensive Benchmark for Evaluating Causal Reasoning Capabilities of Large Language Models](https://aclanthology.org/2024.sighan-1.17/) - consulted for benchmark coverage across cause, effect, and intervention variants.
- [x] [Chen et al. (2024) Causal Evaluation of Language Models](https://arxiv.org/abs/2405.00622) - consulted for the large-scale causal evaluation framework.
- [x] [OpenCausalLab (2024) Causal Evaluation of Language Models (CaLM)](https://opencausalab.github.io/CaLM) - consulted for accessible summary findings, including adaptation and seen-versus-unseen comparisons.
- [x] [Research repo (2026-05-19) Research Question 2.4: Pearl's Causal Hierarchy and the formal limits of observational data for intervention and counterfactual reasoning](https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq2-4-causal-hierarchy-formal-limits.md) - consulted as the formal prior item.
- [x] [Research repo (2026-05-19) Research Question 3.1: Large Language Models as Statistical Optimisers, Token Distribution vs. Invariant Causal Models of Reality](https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq3-1-llm-statistical-vs-causal.md) - consulted as the immediate model-class prior item.
- [x] [Research repo (2026-05-19) Research Question 3.2: The Stochastic Parrot Under Pressure, Large Language Model Failures on Out-of-Distribution Logical Prompts Requiring Structural Intervention](https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq3-2-stochastic-parrot-ood.md) - consulted as the immediate prompt-level failure prior item.

---

## Research Skill Output

### §0 Initialise

- Question: What are the empirical boundaries of ICL and CoT prompting when a predictive language model is pushed toward intervention and alternate-world causal questions?
- Scope: ICL mechanism papers, CoT prompting, faithfulness evidence, autoregressive reliability limits, and causal-benchmark evidence that bears on Level 1 versus Level 2 or Level 3 reasoning.
- Constraints: full mode, direct dependency on Research Questions 2.4, 3.1, and 3.2, URL-backed citations only, and canonical tags only.
- Output: executive summary, key findings, evidence map, assumptions, analysis, risks, gaps, uncertainties, and open questions.
- Prior completed items consulted: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq2-4-causal-hierarchy-formal-limits.md ; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq3-1-llm-statistical-vs-causal.md ; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq3-2-stochastic-parrot-ood.md

### §1 Question Decomposition

1. ICL mechanism
   1.1 What kinds of learning algorithms have controlled ICL papers shown inside transformers?
   1.2 Do those results imply general causal reasoning, or only prompt-time estimation in narrow settings?
2. CoT mechanism
   2.1 What does CoT add relative to ordinary next-token prediction?
   2.2 Is CoT better described as explicit causal reasoning or as longer sequential conditional prediction?
3. Faithfulness and spurious trajectories
   3.1 When models give a CoT explanation, does the visible chain actually drive the answer?
   3.2 Can a model produce a plausible chain that is weakly connected to the real answer process?
4. Reliability of multi-step chains
   4.1 Why should one left-to-right reasoning path accumulate risk over many steps?
   4.2 What do self-consistency and Tree of Thoughts imply about the weaknesses of single-path CoT?
5. Causal-hierarchy test
   5.1 Do current causal benchmarks show that CoT reliably answers Level 2 intervention questions?
   5.2 Do they show that CoT reliably answers Level 3 counterfactual questions?
   5.3 If not, what narrower competence does CoT plausibly provide?
6. Final classification
   6.1 Does CoT cross Pearl's hierarchy, partially approach it, or remain Level 1 with more inference-time search?

### §2 Investigation

#### Access notes

- Access note: seeded Basic Books page checked as a book locator only; hierarchy claims below are taken from accessible Pearl and Bareinboim sources.
- Access note: seeded Zeiler and Fergus DOI resolved to a reference listing rather than an accessible abstract in this runtime; no substantive claims below depend on it.

#### A. What controlled ICL papers show

- [fact] Xie et al. show that ICL can emerge when pretraining data have long-range coherence, because the model can infer a latent document-level concept and then reuse that latent-concept inference at test time across prompt examples. [source: https://arxiv.org/abs/2111.02080]
- [fact] Akyurek et al. report three lines of evidence, by construction, empirical matching, and internal-feature analysis, that transformer-based in-context learners on linear-regression tasks can implement gradient descent, ridge regression, exact least-squares regression, and in some regimes converge toward Bayesian estimators. [source: https://arxiv.org/abs/2211.15661]
- [fact] von Oswald et al. show a direct equivalence between a linear self-attention transformation and gradient descent on a regression loss, and they argue that self-attention-only transformers can learn models by gradient descent in their forward pass on regression tasks. [source: https://arxiv.org/abs/2212.07677; https://openreview.net/forum?id=tHvXrFQma5]
- [inference] The best-supported ICL claim is therefore not "mysterious general reasoning" but "prompt-time implementation of specific estimation procedures in controlled settings." [source: https://arxiv.org/abs/2111.02080; https://arxiv.org/abs/2211.15661; https://arxiv.org/abs/2212.07677]
- [inference] Those mechanism papers show real algorithmic adaptation inside the context window, but they do not show that the learned inner algorithm carries intervention semantics, structural-causal-model substitution, or alternate-world comparison. [source: https://arxiv.org/abs/2211.15661; https://arxiv.org/abs/2212.07677; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq2-4-causal-hierarchy-formal-limits.md]

#### B. What CoT adds at inference time

- [fact] Wei et al. show that providing chain-of-thought exemplars improves arithmetic, commonsense, and symbolic reasoning performance in sufficiently large language models. [source: https://arxiv.org/abs/2201.11903; https://openreview.net/forum?id=_VjQlMeSB_J]
- [fact] Research Question 3.1 concluded that ordinary LLM pre-training remains a next-token objective over textual observations rather than direct optimisation over invariant mechanisms. [source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq3-1-llm-statistical-vs-causal.md]
- [inference] CoT therefore changes the inference trace more than it changes the training objective: it asks the same predictive model to emit a longer sequence of intermediate text before committing to a final answer. [source: https://arxiv.org/abs/2201.11903; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq3-1-llm-statistical-vs-causal.md]
- [inference] At the level of the reasoning trace, single-path CoT is well described as a sequential conditional process, `P(step_1, ..., step_n, answer | prompt) = prod_i P(token_i | prior tokens, prompt)`, with the visible "steps" formed by autoregressive continuation rather than by an externally validated causal simulator. [source: https://arxiv.org/abs/2201.11903; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq3-1-llm-statistical-vs-causal.md]

#### C. Faithfulness and spurious reasoning trajectories

- [fact] Turpin et al. find that CoT explanations can systematically misrepresent the true reason for a model's prediction, because models can be pushed by biasing prompt features that they then fail to mention in their explanations. [source: https://arxiv.org/abs/2305.04388]
- [fact] The same paper reports that when models are biased toward incorrect answers, they frequently generate CoT explanations rationalising those answers, and accuracy can drop by as much as 36 percent on a suite of 13 tasks from Beyond the Imitation Game Benchmark (BIG-Bench) Hard. [source: https://arxiv.org/abs/2305.04388]
- [fact] Lanham et al. measure how answers change under interventions on the visible CoT and find wide task variation: models sometimes rely heavily on the chain and sometimes largely ignore it, while larger and more capable models often produce less faithful reasoning on most studied tasks. [source: https://arxiv.org/abs/2307.13702; https://www.anthropic.com/research/measuring-faithfulness-in-chain-of-thought-reasoning]
- [inference] Correct final answers accompanied by fluent intermediate text cannot therefore be taken as direct evidence that the model followed a valid causal path to the answer. [source: https://arxiv.org/abs/2305.04388; https://arxiv.org/abs/2307.13702]
- [inference] CoT has an interpretability dilemma: when the chain strongly drives the answer it can propagate early mistakes, and when the chain weakly drives the answer it becomes a post hoc explanation rather than a faithful causal trace. [source: https://arxiv.org/abs/2305.04388; https://arxiv.org/abs/2307.13702]

#### D. Why single-path CoT is brittle over many steps

- [fact] Wang et al. propose self-consistency because greedy CoT decoding follows only one reasoning path, whereas sampling multiple diverse paths and marginalising over answers yields large gains on arithmetic and commonsense benchmarks. [source: https://arxiv.org/abs/2203.11171]
- [fact] Yao et al. state that language models remain confined to token-level, left-to-right decision processes during inference, which makes them fall short on tasks needing exploration, strategic lookahead, or recovery from pivotal early decisions. [source: https://openreview.net/forum?id=5Xc1ecxO1h]
- [fact] The Tree of Thoughts results show a large gap on a planning-heavy task: GPT-4 with CoT solves 4 percent of Game of 24 tasks, while Tree of Thoughts reaches 74 percent by branching, self-evaluating, and backtracking. [source: https://openreview.net/forum?id=5Xc1ecxO1h]
- [inference] The need for self-consistency and Tree of Thoughts is direct evidence that one linear CoT path is a brittle search policy rather than a stable reasoning oracle. [source: https://arxiv.org/abs/2203.11171; https://openreview.net/forum?id=5Xc1ecxO1h]
- [inference] If the probability that each reasoning step remains task-correct given the previous steps is `q_i`, then the probability that the full visible chain remains correct through `n` steps is `prod_i q_i`, so any persistent per-step error risk compounds with chain length unless the system adds branching, voting, or correction. [source: https://arxiv.org/abs/2201.11903; https://arxiv.org/abs/2203.11171; https://openreview.net/forum?id=5Xc1ecxO1h]

#### E. What causal benchmarks say about CoT on intervention and counterfactual tasks

- [fact] Yang et al. review causal benchmarks for LLMs and argue that many benchmarks can likely be solved through retrieval of domain knowledge, which means headline success does not by itself establish causal understanding. [source: https://arxiv.org/abs/2407.08029]
- [fact] Wang et al. introduce a benchmark that tests cause-to-effect, effect-to-cause, and intervention variants across text, mathematics, and code precisely because earlier textual datasets did not adequately show whether models genuinely grasp causal relationships. [source: https://aclanthology.org/2024.sighan-1.17/]
- [fact] Zhou et al. report that on CausalBench, closed-source LLMs show some potential on simple causal relationships but significantly lag traditional causal algorithms on larger networks, struggle with common-effect graph patterns where two arrows meet at one node, and appear to use semantic associations rather than direct recovery from contextual information or numerical distributions. [source: https://arxiv.org/abs/2404.06349]
- [fact] Chen et al. present Causal Evaluation of Language Models (CaLM) as a large benchmark with 126,334 samples, 92 causal targets, and 50 high-level empirical findings across models, tasks, and adaptation settings. [source: https://arxiv.org/abs/2405.00622]
- [fact] The OpenCausalLab CaLM findings page states that language models struggle on sophisticated causal reasoning tasks, that accuracy deteriorates as causal complexity increases until it approaches zero, and that complex intervention and counterfactual tasks are easier on open-source seen datasets than on self-constructed unseen datasets. [source: https://opencausalab.github.io/CaLM]
- [fact] The same CaLM findings page says the preferred adaptation varies by causal level: 1-shot or 3-shot ICL is effective on lower-level causal scenarios, 3-shot ICL is recommended for intervention scenarios, and manual CoT is the suggested adaptation for counterfactual scenarios that require more detailed reasoning. [source: https://opencausalab.github.io/CaLM]
- [inference] These benchmark results show prompt-level gains and task-sensitive adaptation, but they do not show that CoT reliably lifts the model into robust Level 2 or Level 3 reasoning on unseen or structurally harder problems. [source: https://arxiv.org/abs/2407.08029; https://arxiv.org/abs/2404.06349; https://opencausalab.github.io/CaLM]
- [inference] CoT appears most useful where the causal structure can still be rendered as a familiar sequential narrative or simple chain, and least useful where the task requires explicit intervention semantics, common-effect graph reasoning, or alternate-world consistency. [source: https://arxiv.org/abs/2404.06349; https://opencausalab.github.io/CaLM; https://aclanthology.org/2024.sighan-1.17/]

#### F. Cross-item synthesis with Pearl's hierarchy and the Stochastic Parrot result

- [fact] Research Question 2.4 concluded that observational data almost never determine intervention or counterfactual facts, so higher-layer causal answers generally require extra structure or extra evidence. [source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq2-4-causal-hierarchy-formal-limits.md]
- [fact] Research Question 3.1 concluded that standard LLM training is an observational optimisation process over token distributions. [source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq3-1-llm-statistical-vs-causal.md]
- [fact] Research Question 3.2 concluded that when prompts require intervention or structurally novel composition, current LLM performance collapses in the way the hierarchy predicts. [source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq3-2-stochastic-parrot-ood.md]
- [inference] ICL and CoT narrow some local performance gaps by rediscovering estimation algorithms, extending inference-time search, and making better use of textual cues, but the combined evidence still places them on the observational side of Pearl's hierarchy by default. [source: https://arxiv.org/abs/2211.15661; https://arxiv.org/abs/2212.07677; https://arxiv.org/abs/2201.11903; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq2-4-causal-hierarchy-formal-limits.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq3-2-stochastic-parrot-ood.md]

### §3 Reasoning

- [inference] The strongest evidence in favour of ICL is that transformers can implement standard learning procedures inside the prompt, but those procedures are still estimators over presented examples rather than direct encodings of intervention semantics or alternate-world causal structure. [source: https://arxiv.org/abs/2111.02080; https://arxiv.org/abs/2211.15661; https://arxiv.org/abs/2212.07677]
- [inference] The strongest evidence in favour of CoT is benchmark improvement, yet the faithfulness literature shows that visible reasoning text is not a reliable witness to the true computation that produced the answer. [source: https://arxiv.org/abs/2201.11903; https://arxiv.org/abs/2305.04388; https://arxiv.org/abs/2307.13702]
- [inference] The strongest evidence against a "CoT crosses the hierarchy" claim is the convergence of three findings: benchmark-review papers warn that many causal tasks are retrieval-solvable, CausalBench shows degradation on harder structures, and CaLM shows near-zero performance on the most complex scenarios and worse results on unseen datasets. [source: https://arxiv.org/abs/2407.08029; https://arxiv.org/abs/2404.06349; https://opencausalab.github.io/CaLM]
- [inference] The most defensible interpretation is therefore that CoT is a useful inference-time scaffold for serial search in text space, not a prompt-induced conversion of a predictive architecture into a robust Level 2 or Level 3 causal reasoner. [source: https://arxiv.org/abs/2201.11903; https://openreview.net/forum?id=5Xc1ecxO1h; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq2-4-causal-hierarchy-formal-limits.md]

### §4 Consistency Check

- [fact] Tension: controlled ICL papers show transformers learning algorithmic procedures such as gradient descent or ridge regression in context. [source: https://arxiv.org/abs/2211.15661; https://arxiv.org/abs/2212.07677]
- [inference] Resolution: those results support prompt-time estimation in narrow synthetic regimes, but they do not contradict Pearl's hierarchy because they still do not provide intervention semantics or counterfactual world-model structure. [source: https://arxiv.org/abs/2211.15661; https://arxiv.org/abs/2212.07677; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq2-4-causal-hierarchy-formal-limits.md]
- [fact] Tension: causal benchmarks show that some models perform non-trivially on simple or chain-structured causal tasks, and CaLM recommends manual CoT for counterfactual scenarios. [source: https://arxiv.org/abs/2404.06349; https://opencausalab.github.io/CaLM]
- [inference] Resolution: that is consistent with narrow prompt-sensitive competence, because the same evidence base reports sharp decline on harder structures, unseen datasets, and more complex intervention or counterfactual settings. [source: https://arxiv.org/abs/2404.06349; https://opencausalab.github.io/CaLM]
- [fact] Tension: CoT improves some benchmark scores while faithfulness papers show that the visible chain may be weakly connected to the true answer process. [source: https://arxiv.org/abs/2201.11903; https://arxiv.org/abs/2305.04388; https://arxiv.org/abs/2307.13702]
- [inference] Resolution: benchmark improvement and explanation faithfulness are different properties, so better accuracy under CoT does not by itself prove that the model acquired a stable causal procedure. [source: https://arxiv.org/abs/2201.11903; https://arxiv.org/abs/2305.04388; https://arxiv.org/abs/2307.13702]

### §5 Depth and Breadth Expansion

- [inference] Technical lens: ICL mechanism papers imply that more capability can emerge inside the prompt than a "mere lookup table" story allows, but the emergent inner algorithms still look like estimators or optimisers, not like explicit structural-causal-model manipulation. [source: https://arxiv.org/abs/2111.02080; https://arxiv.org/abs/2211.15661; https://arxiv.org/abs/2212.07677]
- [inference] Evaluation lens: CoT should be treated as a search-policy intervention whose value must be measured on unseen intervention and counterfactual tasks, because seen-dataset gains can be explained by retrieval, narrative familiarity, or chain-structured cueing. [source: https://arxiv.org/abs/2407.08029; https://opencausalab.github.io/CaLM]
- [inference] Mechanistic lens: the combination of Turpin et al. and Lanham et al. suggests that visible reasoning text is neither a reliable causal trace nor pure decoration in all cases, which means CoT sits in an unstable middle position between true process and post hoc narration. [source: https://arxiv.org/abs/2305.04388; https://arxiv.org/abs/2307.13702]
- [inference] Strategic lens: if single-step CoT does not supply robust Level 2 or Level 3 reasoning, then later agentic-loop claims should assume that composing many CoT calls mostly compounds a Level 1 process unless external structure, search, tools, or causal supervision are added. [source: https://openreview.net/forum?id=5Xc1ecxO1h; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq3-2-stochastic-parrot-ood.md]

### §6 Synthesis

**Executive summary:**

- [inference] ICL and CoT materially extend what a predictive LLM can do at inference time, but current evidence does not show that they reliably convert Level 1 statistical prediction into Level 2 intervention reasoning or Level 3 counterfactual reasoning. [source: https://arxiv.org/abs/2211.15661; https://arxiv.org/abs/2201.11903; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq2-4-causal-hierarchy-formal-limits.md]
- [inference] Controlled ICL studies show transformers can implement standard estimators such as gradient descent, ridge regression, and approximate Bayesian updating in narrow settings, which is stronger than mere memorisation but weaker than a general causal world model. [source: https://arxiv.org/abs/2111.02080; https://arxiv.org/abs/2211.15661; https://arxiv.org/abs/2212.07677]
- [fact] CoT improves benchmark scores, yet faithfulness studies show that the visible chain can misrepresent or only weakly constrain the process that produced the answer, especially in larger models. [source: https://arxiv.org/abs/2201.11903; https://arxiv.org/abs/2305.04388; https://arxiv.org/abs/2307.13702]
- [fact] Causal benchmarks show partial success on simple or chain-like tasks but sharp degradation as causal complexity, unseen evaluation, common-effect graph structure, or counterfactual demand increases. [source: https://arxiv.org/abs/2404.06349; https://arxiv.org/abs/2405.00622; https://opencausalab.github.io/CaLM]
- [inference] The best-supported classification is therefore that CoT is an inference-time search scaffold over autoregressive conditional probabilities, not a prompt-induced installation of causal semantics. [source: https://openreview.net/forum?id=5Xc1ecxO1h; https://arxiv.org/abs/2203.11171; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq2-4-causal-hierarchy-formal-limits.md]

**Key findings:**

1. [inference] Controlled ICL papers show that transformers can recover prompt-time learning procedures such as gradient descent, ridge regression, and approximate Bayesian updating, but those results are demonstrated in narrow synthetic regimes rather than as general causal-mechanism reasoning. [source: https://arxiv.org/abs/2111.02080; https://arxiv.org/abs/2211.15661; https://arxiv.org/abs/2212.07677]
2. [inference] CoT improves arithmetic, commonsense, and symbolic benchmark performance by eliciting longer intermediate-text traces from the same predictive model, which increases inference-time search without changing the model's underlying observational training objective. [source: https://arxiv.org/abs/2201.11903; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq3-1-llm-statistical-vs-causal.md]
3. [fact] Faithfulness studies show that CoT explanations can be misleading or weakly coupled to the actual answer process, so a plausible chain is not reliable evidence that the model followed a valid causal path. [source: https://arxiv.org/abs/2305.04388; https://arxiv.org/abs/2307.13702]
4. [inference] Single-path CoT is structurally brittle because each new step conditions on previous generated text, so end-to-end reliability degrades with chain length unless the system adds aggregation, branching, or backtracking. [source: https://arxiv.org/abs/2203.11171; https://openreview.net/forum?id=5Xc1ecxO1h; https://arxiv.org/abs/2201.11903]
5. [fact] Current causal benchmarks show that LLMs perform better on simple or chain-structured causal tasks than on larger-network, unseen, common-effect-heavy, or more complex intervention and counterfactual tasks. [source: https://arxiv.org/abs/2404.06349; https://aclanthology.org/2024.sighan-1.17/; https://opencausalab.github.io/CaLM]
6. [inference] The fact that CaLM recommends manual CoT for counterfactual scenarios is best read as evidence that prompt scaffolding can help organise serial search, not as evidence that prompting alone crosses Pearl's hierarchy. [source: https://opencausalab.github.io/CaLM; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq2-4-causal-hierarchy-formal-limits.md]
7. [inference] Across ICL mechanism papers, CoT faithfulness papers, and causal benchmarks, the most defensible conclusion is that CoT remains an extended Level 1 procedure that can mimic some higher-level reasoning patterns without reliably acquiring Level 2 or Level 3 causal reach. [source: https://arxiv.org/abs/2211.15661; https://arxiv.org/abs/2305.04388; https://arxiv.org/abs/2407.08029; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq3-2-stochastic-parrot-ood.md]

**Evidence map:**

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [inference] Controlled ICL papers recover prompt-time estimators rather than general causal world models. | https://arxiv.org/abs/2111.02080 ; https://arxiv.org/abs/2211.15661 ; https://arxiv.org/abs/2212.07677 | medium | Controlled synthetic settings. |
| [inference] CoT improves benchmark performance by extending inference-time search over text from the same observationally trained model. | https://arxiv.org/abs/2201.11903 ; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq3-1-llm-statistical-vs-causal.md | medium | Mechanism partly inferred. |
| [fact] CoT explanations can be misleading or weakly coupled to the answer process. | https://arxiv.org/abs/2305.04388 ; https://arxiv.org/abs/2307.13702 | high | Direct intervention-based evidence. |
| [inference] Single-path CoT is brittle because serial dependence compounds local errors unless branching or aggregation is added. | https://arxiv.org/abs/2203.11171 ; https://openreview.net/forum?id=5Xc1ecxO1h ; https://arxiv.org/abs/2201.11903 | medium | Supported by mitigation papers. |
| [fact] LLMs do better on simple or chain-like causal tasks than on harder common-effect, large-network, unseen, or counterfactual tasks. | https://arxiv.org/abs/2404.06349 ; https://aclanthology.org/2024.sighan-1.17/ ; https://opencausalab.github.io/CaLM | high | Multiple benchmark families agree. |
| [inference] Manual CoT for counterfactual scenarios is prompt scaffolding, not proof of hierarchy crossing. | https://opencausalab.github.io/CaLM ; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq2-4-causal-hierarchy-formal-limits.md | medium | Uses external benchmark plus formal prior item. |
| [inference] The combined evidence places CoT on extended Level 1 rather than robust Level 2 or Level 3 reasoning. | https://arxiv.org/abs/2211.15661 ; https://arxiv.org/abs/2305.04388 ; https://arxiv.org/abs/2407.08029 ; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq3-2-stochastic-parrot-ood.md | medium | Multi-source synthesis claim. |

**Assumptions:**

- [assumption] Current public causal benchmarks are representative enough to judge the prompt-level causal reach of present LLMs, even though benchmark design remains imperfect. [source: https://arxiv.org/abs/2407.08029; https://arxiv.org/abs/2405.00622]
- [assumption] If CoT truly supplied robust Level 2 or Level 3 reasoning, that gain should materially reduce the unseen-task collapse reported on intervention and counterfactual benchmarks. [source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq2-4-causal-hierarchy-formal-limits.md; https://opencausalab.github.io/CaLM]

**Analysis:**

- [inference] The ICL mechanism papers receive the most weight on the narrow question of what computation can arise inside a context window, because they are primary studies with explicit constructions and controlled task families. [source: https://arxiv.org/abs/2111.02080; https://arxiv.org/abs/2211.15661; https://arxiv.org/abs/2212.07677]
- [inference] Those same papers do not count as decisive evidence of causal reasoning, because they study regression-style or latent-concept settings rather than intervention semantics, counterfactual world comparisons, or structural-causal-model manipulation. [source: https://arxiv.org/abs/2111.02080; https://arxiv.org/abs/2211.15661; https://arxiv.org/abs/2212.07677; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq2-4-causal-hierarchy-formal-limits.md]
- [inference] CoT benchmark gains still matter, but they were treated as insufficient on their own, because self-consistency and Tree of Thoughts only make sense as improvements if one greedy chain is already an error-prone local search path. [source: https://arxiv.org/abs/2201.11903; https://arxiv.org/abs/2203.11171; https://openreview.net/forum?id=5Xc1ecxO1h]
- [inference] Turpin et al. and Lanham et al. carry unusual weight here because both probe faithfulness by intervening on prompts or on the visible chain itself rather than by relying on stylistic plausibility. [source: https://arxiv.org/abs/2305.04388; https://arxiv.org/abs/2307.13702]
- [inference] For the final classification, the causal benchmarks matter most, because the core question is not whether CoT looks thoughtful, but whether it materially changes performance on intervention and counterfactual tasks that test higher levels of Pearl's hierarchy. [source: https://aclanthology.org/2024.sighan-1.17/; https://arxiv.org/abs/2404.06349; https://opencausalab.github.io/CaLM]

**Risks, gaps, uncertainties:**

- [fact] Most ICL mechanism papers use synthetic regression or latent-concept settings, so they provide strong mechanistic clues but weak direct coverage of open-ended causal reasoning in frontier LLMs. [source: https://arxiv.org/abs/2111.02080; https://arxiv.org/abs/2211.15661; https://arxiv.org/abs/2212.07677]
- [fact] The causal-benchmark literature itself warns that some tasks are contaminated by retrieval-friendly knowledge, which means absolute score improvements under CoT are hard to interpret without unseen or structurally controlled evaluation. [source: https://arxiv.org/abs/2407.08029; https://opencausalab.github.io/CaLM]
- [inference] The current evidence base is much stronger at showing that CoT fails to guarantee causal reasoning than at locating the exact threshold where limited causal abstraction may begin. [source: https://arxiv.org/abs/2404.06349; https://arxiv.org/abs/2405.00622; https://opencausalab.github.io/CaLM]

**Open questions:**

- Which benchmark design best separates prompt-organised search from genuine intervention semantics in frontier models?
- Under what conditions do ICL inner algorithms generalise beyond synthetic regression and latent-concept tasks into robust causal abstraction?
- Can external tools, explicit search, or structured causal state make CoT-like traces more faithful without simply turning the system into a different architecture?

### §7 Recursive Review

- Review result: pass
- Acronym audit: ICL, CoT, LLM, and do-operator checked for first-use expansion or definition in the document body.
- Claim audit: visible claims in Research Skill Output and Findings carry labels and URL-backed sources.
- Findings parity: §6 Synthesis and ## Findings aligned on claims, confidence, and source sets.

---

## Findings

### Executive Summary

In-context learning and chain-of-thought prompting do not reliably convert a predictive Large Language Model into a robust intervention or counterfactual reasoner; they extend inference-time estimation and search while leaving the model mostly on Pearl's Level 1 associational side by default. [inference; source: https://arxiv.org/abs/2211.15661; https://arxiv.org/abs/2201.11903; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq2-4-causal-hierarchy-formal-limits.md]

The strongest positive evidence is that controlled ICL studies recover real inner algorithms such as gradient descent, ridge regression, and approximate Bayesian updating, which is more capable than pure memorisation but still narrower than general causal-mechanism modelling. [inference; source: https://arxiv.org/abs/2111.02080; https://arxiv.org/abs/2211.15661; https://arxiv.org/abs/2212.07677]

The strongest negative evidence is that CoT explanations are often unfaithful, single-path chains are brittle without branching or aggregation, and causal-benchmark performance deteriorates sharply as tasks move toward harder intervention, common-effect, unseen, or counterfactual settings. [fact; source: https://arxiv.org/abs/2305.04388; https://arxiv.org/abs/2307.13702; https://arxiv.org/abs/2404.06349; https://opencausalab.github.io/CaLM]

The most defensible conclusion is therefore that CoT is an extended statistical interpolation procedure that can mimic some higher-level reasoning patterns and improve local performance without supplying the extra structure that Pearl's hierarchy says true Level 2 and Level 3 reasoning require. [inference; source: https://arxiv.org/abs/2407.08029; https://openreview.net/forum?id=5Xc1ecxO1h; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq3-2-stochastic-parrot-ood.md]

### Key Findings

1. **Controlled ICL papers show that transformers can recover prompt-time learning procedures such as gradient descent, ridge regression, and approximate Bayesian updating, but those results are demonstrated in narrow synthetic regimes rather than as general causal-mechanism reasoning.** ([inference]; medium confidence; source: https://arxiv.org/abs/2111.02080; https://arxiv.org/abs/2211.15661; https://arxiv.org/abs/2212.07677)
2. **CoT improves arithmetic, commonsense, and symbolic benchmark performance by eliciting longer intermediate-text traces from the same predictive model, which increases inference-time search without changing the model's underlying observational training objective.** ([inference]; medium confidence; source: https://arxiv.org/abs/2201.11903; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq3-1-llm-statistical-vs-causal.md)
3. **Faithfulness studies show that CoT explanations can be misleading or weakly coupled to the actual answer process, so a plausible chain is not reliable evidence that the model followed a valid causal path.** ([fact]; high confidence; source: https://arxiv.org/abs/2305.04388; https://arxiv.org/abs/2307.13702)
4. **Single-path CoT is structurally brittle because each new step conditions on previous generated text, so end-to-end reliability degrades with chain length unless the system adds aggregation, branching, or backtracking.** ([inference]; medium confidence; source: https://arxiv.org/abs/2203.11171; https://openreview.net/forum?id=5Xc1ecxO1h; https://arxiv.org/abs/2201.11903)
5. **Current causal benchmarks show that LLMs perform better on simple or chain-structured causal tasks than on larger-network, unseen, common-effect-heavy, or more complex intervention and counterfactual tasks.** ([fact]; high confidence; source: https://arxiv.org/abs/2404.06349; https://aclanthology.org/2024.sighan-1.17/; https://opencausalab.github.io/CaLM)
6. **The fact that CaLM recommends manual CoT for counterfactual scenarios is best read as evidence that prompt scaffolding can help organise serial search, not as evidence that prompting alone crosses Pearl's hierarchy.** ([inference]; low confidence; source: https://opencausalab.github.io/CaLM; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq2-4-causal-hierarchy-formal-limits.md)
7. **Across ICL mechanism papers, CoT faithfulness papers, and causal benchmarks, the most defensible conclusion is that CoT remains an extended Level 1 procedure that can mimic some higher-level reasoning patterns without reliably acquiring Level 2 or Level 3 causal reach.** ([inference]; medium confidence; source: https://arxiv.org/abs/2211.15661; https://arxiv.org/abs/2305.04388; https://arxiv.org/abs/2407.08029; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq3-2-stochastic-parrot-ood.md)

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [inference] Controlled ICL papers recover prompt-time estimators rather than general causal world models. | https://arxiv.org/abs/2111.02080 ; https://arxiv.org/abs/2211.15661 ; https://arxiv.org/abs/2212.07677 | medium | Controlled synthetic settings. |
| [inference] CoT improves benchmark performance by extending inference-time search over text from the same observationally trained model. | https://arxiv.org/abs/2201.11903 ; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq3-1-llm-statistical-vs-causal.md | medium | Mechanism partly inferred. |
| [fact] CoT explanations can be misleading or weakly coupled to the answer process. | https://arxiv.org/abs/2305.04388 ; https://arxiv.org/abs/2307.13702 | high | Intervention-based evidence. |
| [inference] Single-path CoT is brittle because serial dependence compounds local errors unless branching or aggregation is added. | https://arxiv.org/abs/2203.11171 ; https://openreview.net/forum?id=5Xc1ecxO1h ; https://arxiv.org/abs/2201.11903 | medium | Supported by mitigation papers. |
| [fact] LLMs do better on simple or chain-like causal tasks than on harder common-effect, large-network, unseen, or counterfactual tasks. | https://arxiv.org/abs/2404.06349 ; https://aclanthology.org/2024.sighan-1.17/ ; https://opencausalab.github.io/CaLM | high | Multiple benchmark families agree. |
| [inference] Manual CoT for counterfactual scenarios is prompt scaffolding, not proof of hierarchy crossing. | https://opencausalab.github.io/CaLM ; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq2-4-causal-hierarchy-formal-limits.md | low | Interpretation from one benchmark recommendation. |
| [inference] The combined evidence places CoT on extended Level 1 rather than robust Level 2 or Level 3 reasoning. | https://arxiv.org/abs/2211.15661 ; https://arxiv.org/abs/2305.04388 ; https://arxiv.org/abs/2407.08029 ; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq3-2-stochastic-parrot-ood.md | medium | Multi-source synthesis claim. |

### Assumptions

- The current public causal benchmarks are representative enough to judge the prompt-level causal reach of present LLMs, even though benchmark design remains imperfect. [assumption; source: https://arxiv.org/abs/2407.08029; https://arxiv.org/abs/2405.00622]
- If CoT truly supplied robust Level 2 or Level 3 reasoning, that gain should materially reduce the unseen-task collapse reported on intervention and counterfactual benchmarks. [assumption; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq2-4-causal-hierarchy-formal-limits.md; https://opencausalab.github.io/CaLM]

### Analysis

The ICL mechanism papers receive the most weight on the narrow question of what computation can arise inside a context window, because they are primary studies with explicit constructions and controlled task families. [inference; source: https://arxiv.org/abs/2111.02080; https://arxiv.org/abs/2211.15661; https://arxiv.org/abs/2212.07677]

Those same papers do not count as decisive evidence of causal reasoning, because they study regression-style or latent-concept settings rather than intervention semantics, counterfactual world comparisons, or structural-causal-model manipulation. [inference; source: https://arxiv.org/abs/2111.02080; https://arxiv.org/abs/2211.15661; https://arxiv.org/abs/2212.07677; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq2-4-causal-hierarchy-formal-limits.md]

CoT benchmark gains still matter, but they were treated as insufficient on their own, because self-consistency and Tree of Thoughts only make sense as improvements if one greedy chain is already an error-prone local search path. [inference; source: https://arxiv.org/abs/2201.11903; https://arxiv.org/abs/2203.11171; https://openreview.net/forum?id=5Xc1ecxO1h]

Turpin et al. and Lanham et al. carry unusual weight here because both probe faithfulness by intervening on prompts or on the visible chain itself rather than by relying on stylistic plausibility. [inference; source: https://arxiv.org/abs/2305.04388; https://arxiv.org/abs/2307.13702]

For the final classification, the causal benchmarks matter most, because the core question is not whether CoT looks thoughtful, but whether it materially changes performance on intervention and counterfactual tasks that test higher levels of Pearl's hierarchy. [inference; source: https://aclanthology.org/2024.sighan-1.17/; https://arxiv.org/abs/2404.06349; https://opencausalab.github.io/CaLM]

### Risks, Gaps, and Uncertainties

- Most ICL mechanism papers use synthetic regression or latent-concept settings, so they provide strong mechanistic clues but weak direct coverage of open-ended causal reasoning in frontier LLMs. [fact; source: https://arxiv.org/abs/2111.02080; https://arxiv.org/abs/2211.15661; https://arxiv.org/abs/2212.07677]
- The causal-benchmark literature itself warns that some tasks are contaminated by retrieval-friendly knowledge, which means absolute score improvements under CoT are hard to interpret without unseen or structurally controlled evaluation. [fact; source: https://arxiv.org/abs/2407.08029; https://opencausalab.github.io/CaLM]
- The current evidence base is much stronger at showing that CoT fails to guarantee causal reasoning than at locating the exact threshold where limited causal abstraction may begin. [inference; source: https://arxiv.org/abs/2404.06349; https://arxiv.org/abs/2405.00622; https://opencausalab.github.io/CaLM]

### Open Questions

- Which benchmark design best separates prompt-organised search from genuine intervention semantics in frontier models?
- Under what conditions do ICL inner algorithms generalise beyond synthetic regression and latent-concept tasks into robust causal abstraction?
- Can external tools, explicit search, or structured causal state make CoT-like traces more faithful without simply turning the system into a different architecture?

---

## Output

- Type: knowledge
- Description: This item concludes that ICL and CoT extend prompt-time estimation and serial search but do not, on current evidence, reliably move default LLMs beyond Level 1 association into robust intervention or counterfactual reasoning. [inference; source: https://arxiv.org/abs/2211.15661; https://arxiv.org/abs/2305.04388; https://opencausalab.github.io/CaLM]
- Links:
  - https://arxiv.org/abs/2211.15661
  - https://arxiv.org/abs/2305.04388
  - https://opencausalab.github.io/CaLM
