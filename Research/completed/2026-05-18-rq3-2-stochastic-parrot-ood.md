---
review_count: 2
title: "RQ 3.2: The Stochastic Parrot Under Pressure, Large Language Model Failures on Out-of-Distribution Logical Prompts Requiring Structural Intervention"
added: 2026-05-18T19:40:00+00:00
status: completed
priority: high
blocks:
  - 2026-05-18-rq3-3-cot-counterfactual-limits
tags: [llm, machine-learning, evaluation, hallucinations, causal-inference]
started: 2026-05-19T10:32:06+00:00
completed: 2026-05-19T11:01:20+00:00
output: [knowledge]
cites:
  - 2026-05-18-rq3-1-llm-statistical-vs-causal
  - 2026-05-18-rq2-4-causal-hierarchy-formal-limits
  - 2026-05-18-rq2-1-erm-causal-blindness
related:
  - 2026-05-18-rq2-3-predictive-model-fragility
superseded_by: ~
supersedes: ~
item_type: primary
confidence: medium
versions: []
---

# RQ 3.2: The Stochastic Parrot Under Pressure, Large Language Model Failures on Out-of-Distribution Logical Prompts Requiring Structural Intervention

## Research Question

How does the Stochastic Parrot hypothesis, the claim that Large Language Models (LLMs) reproduce linguistic form more readily than grounded structural understanding, manifest when an LLM is presented with Out-of-Distribution (OOD) logical prompts that require structural interventions rather than high-dimensional text interpolation?

## Scope

**In scope:**
- Empirical characterisation of LLM failure modes on OOD logical prompts, especially arithmetic, logical reasoning, causal reasoning, and novel composition.
- Data memorisation versus algorithmic generalisation as competing explanations for LLM capability.
- Grokking, delayed generalisation after apparent overfitting, and what it reveals about the distinction between memorisation and genuine algorithmic learning.
- The combinatorial growth of OOD state spaces as a limit on interpolation-based success.

**Out of scope:**
- General benchmarking of LLM performance on standard in-distribution reasoning tasks.
- Alignment or safety concerns beyond this specific OOD reasoning failure mode.

**Constraints:** This item must build on Research Question 3.1 and on Pearl's causal hierarchy, so OOD is defined here not just as distribution shift, but as prompts whose correct answer depends on intervention or counterfactual structure, or on genuinely novel compositional combinations.

## Context

Research Question 3.1 concluded that next-token training places Large Language Models on an observational optimisation objective and does not, by itself, provide invariant causal structure. [fact; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq3-1-llm-statistical-vs-causal.md]

Research Question 2.4 concluded that intervention and counterfactual queries generically require information that does not collapse out of observational data alone, so prompts that ask what would happen under a changed mechanism are not merely harder samples from the same distribution. [fact; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq2-4-causal-hierarchy-formal-limits.md]

Bender et al.'s "Stochastic Parrot" critique framed the central risk as fluent surface modelling without grounded understanding, and this item tests whether modern OOD reasoning evidence is best read as an empirical instantiation of that critique. [inference; source: https://treasures.scss.tcd.ie/miscellany/TCD-SCSS-X.20121208.002/AI-fabrications-related-articles/20210201-StochasticParrots-Proc2021ACM.pdf; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq3-1-llm-statistical-vs-causal.md]

## Approach

1. Define OOD logical prompts formally as prompts that require Level 2 or Level 3 reasoning on Pearl's ladder, or that combine familiar operators in genuinely novel ways that cannot be solved by local interpolation.
2. Survey empirical studies of LLM failures on novel arithmetic, logical puzzles, causal counterfactuals, and compositional tasks.
3. Examine the memorisation versus generalisation distinction through Zhang et al. on deep learning generalisation and Power et al. on grokking.
4. Characterise the combinatorial-growth argument for why OOD state spaces outrun any finite training corpus.
5. Evaluate whether the total evidence better supports the Stochastic Parrot hypothesis, narrow emergent abstraction, or a hybrid view.

## Sources

- [x] [Zhang et al. (2017) Understanding deep learning requires rethinking generalization](https://arxiv.org/abs/1611.03530) - consulted for evidence that overparameterised neural networks can fit random labels and noise, so memorisation cannot be ruled out from benchmark success alone.
- [x] [Power et al. (2022) Grokking: Generalization Beyond Overfitting on Small Algorithmic Datasets](https://arxiv.org/abs/2201.02177) - consulted for delayed generalisation in small synthetic settings.
- [x] [Bender et al. (2021) On the Dangers of Stochastic Parrots: Can Language Models Be Too Big?](https://treasures.scss.tcd.ie/miscellany/TCD-SCSS-X.20121208.002/AI-fabrications-related-articles/20210201-StochasticParrots-Proc2021ACM.pdf) - consulted via accessible PDF mirror for the original Stochastic Parrot framing and abstract.
- [x] [Webb et al. (2023) Emergent Analogical Reasoning in Large Language Models](https://arxiv.org/abs/2212.09196) - consulted as counterevidence showing strong abstract analogy performance.
- [x] [Lake and Baroni (2018) Generalization without systematicity](https://arxiv.org/abs/1711.00350) - consulted for systematic compositional failure under SCAN-style splits.
- [x] [Yang et al. (2024) Exploring Compositional Generalization of Large Language Models](https://aclanthology.org/2024.naacl-srw.3/) - consulted for evidence that models trained on simple instructions do not generalise reliably to more compositional instructions.
- [x] [Xu et al. (2024) Do Large Language Models Have Compositional Ability? An Investigation into Limitations and Scalability](https://arxiv.org/abs/2407.15720) - consulted for evidence that multi-step composite tasks remain weak even with larger models.
- [x] [Mirzadeh et al. (2024) GSM-Symbolic: Understanding the Limitations of Mathematical Reasoning in Large Language Models](https://arxiv.org/abs/2410.05229) - consulted for arithmetic fragility under small perturbations and irrelevant clauses.
- [x] [Pirozelli et al. (2023) Assessing Logical Reasoning Capabilities of Encoder-Only Transformer Models](https://arxiv.org/abs/2312.11720) - consulted for evidence that apparent logical skill transfers poorly across datasets.
- [x] [Yang et al. (2024) A Critical Review of Causal Reasoning Benchmarks for Large Language Models](https://arxiv.org/abs/2407.08029) - consulted for the benchmark-design critique that many causal tasks can be solved by retrieval.
- [x] [Zhou et al. (2024) CausalBench: A Comprehensive Benchmark for Causal Learning Capability of Large Language Models](https://arxiv.org/abs/2404.06349) - consulted for comparative evidence that LLMs lag traditional causal algorithms on harder structures.
- [x] [Chen et al. (2024) Causal Evaluation of Language Models](https://arxiv.org/abs/2405.00622) - consulted for large-scale evidence that performance falls as causal complexity rises.
- [x] [Wang et al. (2024) CausalBench: A Comprehensive Benchmark for Evaluating Causal Reasoning Capabilities of Large Language Models](https://aclanthology.org/2024.sighan-1.17/) - consulted for intervention-style evaluation across text, mathematics, and code.
- [x] [OpenCausalLab (2024) Causal Evaluation of Language Models (CaLM) project findings](https://opencausalab.github.io/CaLM) - consulted for accessible benchmark summaries and the seen-versus-unseen comparison.
- [x] [Research repo (2026-05-19) Research Question 3.1: Large Language Models as Statistical Optimisers, Token Distribution vs. Invariant Causal Models of Reality](https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq3-1-llm-statistical-vs-causal.md) - consulted as the immediate prior item.
- [x] [Research repo (2026-05-19) Research Question 2.4: Pearl's Causal Hierarchy and the formal limits of observational data for intervention and counterfactual reasoning](https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq2-4-causal-hierarchy-formal-limits.md) - consulted for the formal definition of intervention and counterfactual limits.
- [x] [Research repo (2026-05-19) Research Question 2.1: Empirical Risk Minimisation's Causal Blindness and the Limits of In-Distribution Guarantees](https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq2-1-erm-causal-blindness.md) - consulted for the Empirical Risk Minimisation (ERM) framing used in the analysis.
- [x] [Pearl (n.d.) The Three Layer Causal Hierarchy](https://web.cs.ucla.edu/~kaoru/3-layer-causal-hierarchy.pdf) - consulted as the authoritative definition source for intervention and counterfactual terms.

---

## Research Skill Output

### §0 Initialise

- Question: How does the Stochastic Parrot hypothesis manifest when Large Language Models face Out-of-Distribution logical prompts that require structural intervention rather than nearby textual interpolation?
- Scope: OOD arithmetic, logical, compositional, and causal-reasoning evidence; memorisation versus generalisation; grokking as counterevidence; and the implication for Stochastic Parrot style interpretation.
- Constraints: full mode, build directly on Research Questions 3.1 and 2.4, use URL-backed sources only, and prefer primary benchmark or paper sources over commentary.
- Output: knowledge item with executive summary, key findings, evidence map, assumptions, analysis, risks, gaps, uncertainties, and open questions.
- Prior completed items consulted: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq3-1-llm-statistical-vs-causal.md ; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq2-4-causal-hierarchy-formal-limits.md ; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq2-1-erm-causal-blindness.md ; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq2-3-predictive-model-fragility.md

### §1 Question Decomposition

1. Stochastic Parrot framing
   1.1 What does the Stochastic Parrot thesis actually claim about language-model competence?
   1.2 What empirical pattern would count as support for that thesis on modern reasoning tasks?
2. Formal definition of OOD prompts
   2.1 What makes a prompt OOD in this item, beyond generic distribution shift?
   2.2 Why do Level 2 and Level 3 prompts on Pearl's ladder require more than observational fitting?
3. Memorisation versus generalisation
   3.1 What does deep-learning evidence show about memorisation capacity?
   3.2 What would genuine algorithmic generalisation look like instead?
   3.3 What does grokking show, and what does it not show?
4. Empirical OOD performance
   4.1 How do LLMs perform on compositional generalisation tasks?
   4.2 How do LLMs perform on perturbed arithmetic tasks?
   4.3 How do LLMs perform on logical reasoning tasks outside their evaluation dataset?
   4.4 How do LLMs perform on intervention and counterfactual causal benchmarks?
5. Counterevidence and synthesis
   5.1 Do any results suggest genuine structural abstraction?
   5.2 Does that counterevidence overturn, qualify, or merely narrow the Stochastic Parrot claim?
   5.3 What is the best-supported final answer?

### §2 Investigation

#### A. What the Stochastic Parrot frame predicts

- [fact] Bender et al. describe the recent language-model trajectory as one that pushes benchmark performance through scale while raising the question of whether fluent form is being mistaken for grounded capability. [source: https://treasures.scss.tcd.ie/miscellany/TCD-SCSS-X.20121208.002/AI-fabrications-related-articles/20210201-StochasticParrots-Proc2021ACM.pdf]
- [inference] Read narrowly for this item, the Stochastic Parrot thesis predicts failure when the prompt requires structural understanding that cannot be recovered from surface regularities alone. [source: https://treasures.scss.tcd.ie/miscellany/TCD-SCSS-X.20121208.002/AI-fabrications-related-articles/20210201-StochasticParrots-Proc2021ACM.pdf; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq3-1-llm-statistical-vs-causal.md]

#### B. Why OOD structural intervention is the relevant test

- [fact] Research Question 2.4 concluded that observational data generically do not determine intervention or counterfactual answers, where intervention means a do-operator query and counterfactual means an alternate-world query on Pearl's three-layer hierarchy, so higher-layer causal questions require extra structure beyond passive observation. [source: https://web.cs.ucla.edu/~kaoru/3-layer-causal-hierarchy.pdf; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq2-4-causal-hierarchy-formal-limits.md]
- [fact] Research Question 3.1 concluded that standard Large Language Model training is an observational optimisation problem over token distributions rather than direct optimisation over invariant mechanisms. [source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq3-1-llm-statistical-vs-causal.md]
- [inference] In this item, an OOD logical prompt is therefore not merely an unfamiliar wording pattern; it is a prompt whose correct answer depends on intervention semantics defined by do-operator queries, counterfactual structure defined by alternate-world queries, or a genuinely novel multi-step composition that nearby textual interpolation cannot guarantee. [source: https://web.cs.ucla.edu/~kaoru/3-layer-causal-hierarchy.pdf; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq2-4-causal-hierarchy-formal-limits.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq3-1-llm-statistical-vs-causal.md; https://arxiv.org/abs/2407.15720]

#### C. What memorisation evidence says about apparent success

- [fact] Zhang et al. show that state-of-the-art deep networks can fit random labels and even random noise while still achieving small train-test gaps on ordinary benchmarks. [source: https://arxiv.org/abs/1611.03530]
- [inference] This result weakens the claim that good benchmark performance by itself is evidence of an algorithmic rule, because high-capacity networks can absorb idiosyncratic data structure without learning a portable mechanism. [source: https://arxiv.org/abs/1611.03530; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq2-1-erm-causal-blindness.md]

#### D. What grokking shows, and its boundary

- [fact] Power et al. report that in small algorithmically generated datasets, neural networks can move from chance-level generalisation to perfect generalisation long after overfitting, a phenomenon they call grokking. [source: https://arxiv.org/abs/2201.02177]
- [fact] Their experiments are intentionally small, synthetic, and algorithmically generated so that memorisation and genuine generalisation can be separated cleanly. [source: https://arxiv.org/abs/2201.02177]
- [inference] Grokking is therefore strong evidence that neural networks can learn genuine algorithms under some training regimes, but it is not direct evidence that current Large Language Models trained on open-ended internet-scale text have already done so for broad causal reasoning. [source: https://arxiv.org/abs/2201.02177; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq3-1-llm-statistical-vs-causal.md]

#### E. OOD compositional and logical generalisation evidence

- [fact] Lake and Baroni show that sequence models can succeed when test commands differ only slightly from training commands, yet fail spectacularly when zero-shot generalisation requires systematic compositional skills. [source: https://arxiv.org/abs/1711.00350]
- [fact] Yang et al. report that training on higher-order compositional instructions improves performance on lower-order instructions, but training on simple instructions does not reliably generalise upward to more compositional ones. [source: https://aclanthology.org/2024.naacl-srw.3/]
- [fact] Xu et al. find that Large Language Models handle simpler composite tasks reasonably well, but typically underperform on more complex multi-step composite tasks, and scaling up generally provides no improvement there. [source: https://arxiv.org/abs/2407.15720]
- [fact] Pirozelli et al. find that encoder-only transformer models can be trained to determine logical validity on specific datasets, yet cross-probing shows difficulty transferring that ability, which suggests reliance on dataset-specific features rather than a general logical capability. [source: https://arxiv.org/abs/2312.11720]
- [inference] Across these studies, the recurring failure mode is not total inability to continue familiar patterns, but brittleness when the same primitive operations must be recombined under a novel structural demand. [source: https://arxiv.org/abs/1711.00350; https://aclanthology.org/2024.naacl-srw.3/; https://arxiv.org/abs/2407.15720; https://arxiv.org/abs/2312.11720]

#### F. OOD arithmetic fragility evidence

- [fact] Mirzadeh et al. introduce GSM-Symbolic to test whether mathematical-reasoning gains reflect genuine reasoning rather than benchmark familiarity. [source: https://arxiv.org/abs/2410.05229]
- [fact] They report that performance declines when only the numerical values in a question are changed, and that adding a single clause that appears relevant but is logically unnecessary can reduce performance by up to 65 percent across state-of-the-art models. [source: https://arxiv.org/abs/2410.05229]
- [inference] That pattern is strong evidence against a robust algorithmic arithmetic procedure in current models, because a genuine procedure should be stable to value substitution and to irrelevant descriptive clutter. [source: https://arxiv.org/abs/2410.05229]

#### G. Causal, interventional, and counterfactual benchmark evidence

- [fact] Yang et al. review recent causal benchmarks and argue that many can likely be solved through retrieval of domain knowledge, so benchmark success alone does not establish causal understanding. [source: https://arxiv.org/abs/2407.08029]
- [fact] Zhou et al. evaluate 19 leading Large Language Models on CausalBench and report that while closed-source models show potential on simple causal relationships, they significantly lag traditional causal algorithms on larger causal networks and struggle especially with collider structures. [source: https://arxiv.org/abs/2404.06349]
- [fact] Wang et al. introduce a benchmark that explicitly evaluates cause-to-effect, effect-to-cause, and intervention variants across text, mathematics, and code, because earlier textual tasks did not adequately test whether models genuinely grasp causal structure. [source: https://aclanthology.org/2024.sighan-1.17/]
- [fact] Chen et al. introduce Causal Evaluation of Language Models (CaLM) with 126,334 samples and 50 high-level empirical findings across models, tasks, and error types. [source: https://arxiv.org/abs/2405.00622]
- [fact] The OpenCausalLab CaLM findings page states that language models struggle on sophisticated causal reasoning tasks, and that accuracy progressively deteriorates as causal complexity increases, eventually falling almost to zero. [source: https://opencausalab.github.io/CaLM]
- [fact] The same CaLM findings page reports that for more complex tasks at the intervention and counterfactual levels, models tend to perform better on open-source datasets than on self-constructed unseen datasets. [source: https://opencausalab.github.io/CaLM]
- [inference] Together, these results indicate that current LLM competence is much stronger on semantically familiar or retrieval-friendly causal questions than on genuinely novel tasks that require mechanism-preserving intervention or counterfactual reasoning. [source: https://arxiv.org/abs/2407.08029; https://arxiv.org/abs/2404.06349; https://arxiv.org/abs/2405.00622; https://opencausalab.github.io/CaLM; https://aclanthology.org/2024.sighan-1.17/]

#### H. Counterevidence for emergent abstraction

- [fact] Webb et al. report that the text-davinci-003 variant of Generative Pre-trained Transformer 3 (GPT-3) showed a surprisingly strong capacity for abstract pattern induction on a range of analogical tasks, matching or surpassing human performance in most tested settings, and that preliminary tests of Generative Pre-trained Transformer 4 (GPT-4) were stronger still. [source: https://arxiv.org/abs/2212.09196]
- [inference] This is real counterevidence to the strongest form of the Stochastic Parrot thesis, because it shows that scale can produce non-trivial abstract pattern induction on some zero-shot tasks. [source: https://arxiv.org/abs/2212.09196]
- [inference] However, Webb et al. test a specific family of analogy tasks, whereas the broader OOD record above shows repeated collapse on compositional, arithmetic, logical-transfer, and causal-intervention tasks, so the best-supported reading is partial abstraction rather than general structural mastery. [source: https://arxiv.org/abs/2212.09196; https://arxiv.org/abs/2410.05229; https://arxiv.org/abs/2407.15720; https://opencausalab.github.io/CaLM]

#### I. Combinatorial-growth argument

- [inference] Once tasks require novel combinations of reusable operators, values, and relations, the number of possible OOD instances grows combinatorially, so any finite corpus can cover only a tiny fraction of the relevant state space. [source: https://arxiv.org/abs/1711.00350; https://aclanthology.org/2024.naacl-srw.3/; https://arxiv.org/abs/2407.15720]
- [inference] That combinatorial asymmetry explains why interpolation can continue to improve on benchmark families while still failing when prompts demand structurally new compositions or interventions. [source: https://arxiv.org/abs/1711.00350; https://arxiv.org/abs/2410.05229; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq2-3-predictive-model-fragility.md]

### §3 Reasoning

- [inference] The evidence does not justify the claim that Large Language Models never form abstractions, because grokking and analogical-reasoning results show that neural systems can, under some conditions, learn structure that generalises beyond memorised examples. [source: https://arxiv.org/abs/2201.02177; https://arxiv.org/abs/2212.09196]
- [inference] The evidence also does not justify the opposite claim that strong OOD benchmark scores automatically prove structural understanding, because several causal-benchmark papers were designed precisely to reduce retrieval shortcuts and still find large drops under harder or unseen settings. [source: https://arxiv.org/abs/2407.08029; https://arxiv.org/abs/2405.00622; https://opencausalab.github.io/CaLM]
- [inference] The most defensible synthesis is a hybrid view in which scale induces useful abstractions, while current Large Language Models still behave mainly as distribution learners whose abstractions are fragile and task-local rather than reliably mechanism-level. [source: https://arxiv.org/abs/2212.09196; https://arxiv.org/abs/2407.15720; https://arxiv.org/abs/2410.05229; https://arxiv.org/abs/2404.06349]

### §4 Consistency Check

- [fact] Tension: Webb et al. report strong zero-shot analogy performance. [source: https://arxiv.org/abs/2212.09196]
- [inference] Resolution: analogy success shows some abstract pattern induction, but it does not resolve the repeated failures on intervention, counterfactual, arithmetic-perturbation, and compositional-transfer tasks, so it narrows the Stochastic Parrot claim rather than falsifying it. [source: https://arxiv.org/abs/2212.09196; https://arxiv.org/abs/2410.05229; https://arxiv.org/abs/2405.00622]
- [fact] Tension: grokking shows perfect generalisation after overfitting in some neural-network settings. [source: https://arxiv.org/abs/2201.02177]
- [inference] Resolution: grokking demonstrates possibility, not default realised capability, because its evidence comes from narrow synthetic settings rather than from open-domain language-model pre-training. [source: https://arxiv.org/abs/2201.02177]
- [fact] Tension: some causal benchmarks show useful performance on simple or semantically familiar tasks. [source: https://arxiv.org/abs/2404.06349; https://opencausalab.github.io/CaLM]
- [inference] Resolution: this is compatible with a hybrid account in which models recover many regularities and heuristics from text, yet still fail when benchmark design removes shortcut routes and increases structural novelty. [source: https://arxiv.org/abs/2407.08029; https://opencausalab.github.io/CaLM]

### §5 Depth and Breadth Expansion

- [inference] Technical lens: the strongest single empirical pattern is brittleness under structurally irrelevant perturbation, because changing only values or adding a distractor clause should not defeat a robust algorithm, yet it does in GSM-Symbolic. [source: https://arxiv.org/abs/2410.05229]
- [inference] Historical lens: this result continues an older neural-network pattern identified by Lake and Baroni, where systems exploit local composition when train and test are nearby, but fail when systematic recombination is demanded. [source: https://arxiv.org/abs/1711.00350]
- [inference] Epistemic lens: the formal result from Research Question 2.4 gives the causal-benchmark failures more weight than a generic benchmark miss, because the hardest prompts are precisely the ones predicted to be underdetermined by observational training. [source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq2-4-causal-hierarchy-formal-limits.md; https://opencausalab.github.io/CaLM]
- [inference] Behavioural lens: the OOD record suggests that many apparent reasoning wins are best understood as competence over familiar representational templates rather than stable possession of a portable reasoning procedure. [source: https://arxiv.org/abs/2407.15720; https://arxiv.org/abs/2410.05229; https://arxiv.org/abs/2404.06349]

### §6 Synthesis

#### Executive Summary

Large Language Models trained on token continuation show a consistent breakdown on tasks that require structural intervention, meaning do-operator style reasoning, counterfactual reasoning, meaning alternate-world reasoning about what would have happened otherwise, or novel multi-step composition, and that pattern is better explained by the Stochastic Parrot framing of fluent surface modelling without grounded understanding than by robust algorithmic generalisation. [inference; source: https://web.cs.ucla.edu/~kaoru/3-layer-causal-hierarchy.pdf; https://treasures.scss.tcd.ie/miscellany/TCD-SCSS-X.20121208.002/AI-fabrications-related-articles/20210201-StochasticParrots-Proc2021ACM.pdf; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq3-1-llm-statistical-vs-causal.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq2-4-causal-hierarchy-formal-limits.md; https://arxiv.org/abs/2407.15720; https://arxiv.org/abs/2410.05229; https://opencausalab.github.io/CaLM]

This conclusion is strongest on causal and counterfactual prompts, where dedicated benchmarks report that accuracy deteriorates as task complexity rises and is often weaker on unseen or intervention-heavy settings than on simpler or more retrieval-friendly ones. [inference; source: https://arxiv.org/abs/2405.00622; https://opencausalab.github.io/CaLM; https://arxiv.org/abs/2404.06349; https://aclanthology.org/2024.sighan-1.17/]

Counterevidence exists: Power et al. report delayed generalisation in narrow synthetic regimes, and Webb et al. report strong zero-shot analogy performance in large language models. [fact; source: https://arxiv.org/abs/2201.02177; https://arxiv.org/abs/2212.09196]

The best-supported answer is that Large Language Models do form some abstractions, but those abstractions remain fragile and task-local, so OOD prompts that require mechanism-preserving intervention still expose them primarily as distribution learners rather than reliable structural reasoners. [inference; source: https://arxiv.org/abs/2212.09196; https://arxiv.org/abs/2407.15720; https://arxiv.org/abs/2410.05229; https://opencausalab.github.io/CaLM]

#### Key Findings

1. **Standard Large Language Model training optimises prediction over observed token sequences, so prompts that require intervention semantics defined by do-operator queries or counterfactual structure defined by alternate-world queries push the model beyond the regime directly supervised by that training objective.** ([inference]; medium confidence; source: https://web.cs.ucla.edu/~kaoru/3-layer-causal-hierarchy.pdf; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq3-1-llm-statistical-vs-causal.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq2-4-causal-hierarchy-formal-limits.md)
2. **Evidence from deep learning generalisation theory shows that high-capacity neural networks can fit arbitrary labels and noise, so raw benchmark success alone does not establish portable algorithmic generalisation.** ([inference]; medium confidence; source: https://arxiv.org/abs/1611.03530)
3. **Grokking demonstrates that neural networks can eventually reach genuine algorithmic generalisation on small synthetic tasks, but that result is a possibility proof under narrow conditions rather than evidence that broad language-model pre-training has solved OOD reasoning.** ([inference]; medium confidence; source: https://arxiv.org/abs/2201.02177; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq3-1-llm-statistical-vs-causal.md)
4. **Compositional-generalisation studies repeatedly show that models trained on simple or nearby patterns do not reliably generalise to structurally richer combinations.** ([fact]; high confidence; source: https://arxiv.org/abs/1711.00350; https://aclanthology.org/2024.naacl-srw.3/; https://arxiv.org/abs/2407.15720)
5. **Arithmetic robustness studies show that changing only numerical values or inserting an irrelevant but plausible clause can sharply degrade performance under modest OOD perturbation.** ([fact]; medium confidence; source: https://arxiv.org/abs/2410.05229)
6. **Causal benchmark evidence shows that Large Language Models perform better on simpler or semantically familiar causal tasks than on intervention-heavy, counterfactual, or larger-structure settings, and they still lag specialised causal algorithms on harder cases.** ([fact]; high confidence; source: https://arxiv.org/abs/2404.06349; https://arxiv.org/abs/2405.00622; https://opencausalab.github.io/CaLM; https://aclanthology.org/2024.sighan-1.17/)
7. **The strongest counterevidence comes from analogical-reasoning results showing that scale can induce non-trivial abstract pattern induction, but that evidence narrows the Stochastic Parrot thesis more than it overturns the broader OOD failure record.** ([inference]; medium confidence; source: https://arxiv.org/abs/2212.09196; https://arxiv.org/abs/2410.05229; https://opencausalab.github.io/CaLM)
8. **The most defensible synthesis is a hybrid one in which current Large Language Models possess some partial abstractions, yet still behave mainly as high-capacity distribution learners when prompts demand genuinely novel compositions or structural interventions.** ([inference]; medium confidence; source: https://arxiv.org/abs/2212.09196; https://arxiv.org/abs/2407.15720; https://arxiv.org/abs/2410.05229; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq3-1-llm-statistical-vs-causal.md)

#### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [inference] Standard LLM training leaves intervention and counterfactual queries outside the regime directly identified by observational token prediction. | https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq3-1-llm-statistical-vs-causal.md ; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq2-4-causal-hierarchy-formal-limits.md | Medium | Prior-item synthesis, formal dependency. |
| [inference] High-capacity neural networks can fit random labels and noise, so benchmark success alone does not prove portable generalisation. | https://arxiv.org/abs/1611.03530 | Medium | Single primary source plus interpretive step. |
| [inference] Grokking proves possibility of algorithmic emergence, but only under narrow synthetic conditions. | https://arxiv.org/abs/2201.02177 ; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq3-1-llm-statistical-vs-causal.md | Medium | Possibility proof, not broad deployment proof. |
| [fact] Compositional-generalisation studies show repeated failure when simple learned pieces must be recombined into richer novel tasks. | https://arxiv.org/abs/1711.00350 ; https://aclanthology.org/2024.naacl-srw.3/ ; https://arxiv.org/abs/2407.15720 ; https://arxiv.org/abs/2312.11720 | High | Multiple independent task families. |
| [fact] Arithmetic reasoning quality drops under modest perturbations such as value substitution or irrelevant added clauses. | https://arxiv.org/abs/2410.05229 | Medium | Single primary source, direct benchmark result. |
| [fact] Causal benchmark performance deteriorates as causal complexity rises and remains weaker on intervention-heavy or unseen settings. | https://arxiv.org/abs/2405.00622 ; https://opencausalab.github.io/CaLM ; https://arxiv.org/abs/2404.06349 ; https://aclanthology.org/2024.sighan-1.17/ | High | Multiple benchmark families. |
| [inference] Strong analogy performance shows partial abstraction, but not general structural mastery across OOD reasoning domains. | https://arxiv.org/abs/2212.09196 ; https://arxiv.org/abs/2410.05229 ; https://opencausalab.github.io/CaLM | Medium | Counterevidence integrated rather than dismissed. |
| [inference] The total evidence best supports a hybrid view: partial abstractions inside a predominantly distributional reasoning regime. | https://arxiv.org/abs/2212.09196 ; https://arxiv.org/abs/2407.15720 ; https://arxiv.org/abs/2410.05229 ; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq3-1-llm-statistical-vs-causal.md | Medium | Final synthesis. |

#### Assumptions

- [assumption] Text benchmarks that explicitly ask about interventions or counterfactuals are reasonable operational proxies for Level 2 and Level 3 reasoning, even though they remain text interfaces rather than real-world interventions. [source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq2-4-causal-hierarchy-formal-limits.md; https://arxiv.org/abs/2407.08029]
- [assumption] The current benchmark set is representative enough to support a medium-confidence conclusion about present-day Large Language Model behaviour, even though specific frontier models and prompting regimes continue to change. [source: https://arxiv.org/abs/2405.00622; https://opencausalab.github.io/CaLM; https://arxiv.org/abs/2404.06349]

#### Analysis

The decisive question is whether a local abstraction survives when the task moves from familiar surface regularities to structurally novel demands. [inference; source: https://arxiv.org/abs/2212.09196; https://arxiv.org/abs/2407.15720]

On that test, the strongest evidence comes from perturbation-sensitive and intervention-sensitive evaluations, because those are the settings where a memorised template should fail and a genuine mechanism should remain stable. [inference; source: https://arxiv.org/abs/2410.05229; https://opencausalab.github.io/CaLM]

The grokking and analogy results matter because they prevent an overclaim. [inference; source: https://arxiv.org/abs/2201.02177; https://arxiv.org/abs/2212.09196]

They show that neural systems can learn abstract structure and that some current language models already do so on particular task families, so the shallowest "mere autocomplete" description misses part of the evidence. [inference; source: https://arxiv.org/abs/2201.02177; https://arxiv.org/abs/2212.09196]

The rival interpretation is that scale, careful prompting, or benchmark contamination explains most apparent failure, and that stronger future models will wash the pattern away. [inference; source: https://arxiv.org/abs/2407.08029]

That rival cannot be dismissed, but the best current evidence still weighs against it because newer causal and arithmetic benchmarks were designed to reduce shortcut routes and still report sharp degradation under structural novelty. [inference; source: https://arxiv.org/abs/2405.00622; https://arxiv.org/abs/2410.05229; https://aclanthology.org/2024.sighan-1.17/]

#### Risks, Gaps, and Uncertainties

- Evidence for strong failure is broader than evidence for strong success, but the exact boundary between "partial abstraction" and "reliable mechanism learning" remains unsettled. [inference; source: https://arxiv.org/abs/2212.09196; https://opencausalab.github.io/CaLM]
- The benchmark literature is still moving, so some currently observed failures may shrink as architectures, tool use, or training curricula change. [inference; source: https://arxiv.org/abs/2405.00622; https://arxiv.org/abs/2410.05229]
- The item relies on textual proxies for intervention and counterfactual reasoning rather than on embodied or simulator-based interventions. [assumption; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq2-4-causal-hierarchy-formal-limits.md; https://arxiv.org/abs/2407.08029]
- Webb et al. supply genuine counterevidence for abstraction, so any absolute claim that LLMs only parrot without learning structure would overstate the record. [fact; source: https://arxiv.org/abs/2212.09196]

#### Open Questions

1. Which training or post-training interventions most reliably convert narrow grokking-like emergence into broad OOD structural reasoning across arithmetic, logic, and causality?
2. How much of current OOD fragility comes from architecture, how much from objective function, and how much from benchmark contamination or prompt mismatch?
3. Would tool-augmented systems actually solve the structural problem, or do they mainly externalise it into a verifier or executor that performs the missing intervention logic?
4. What benchmark family best separates abstract analogy from truly intervention-capable reasoning, so that partial abstraction is not mistaken for full causal competence?

### §7 Recursive Review

- Review result: pass
- Acronym audit: Large Language Models (LLMs), Out-of-Distribution (OOD), Empirical Risk Minimisation (ERM), and Generative Pre-trained Transformer 3 (GPT-3) / Generative Pre-trained Transformer 4 (GPT-4) expanded on first use.
- Claim audit: visible claims in §§2 to 6 carry [fact], [inference], or [assumption] labels, and findings prose uses suffix citations.
- Cross-item integration: Research Questions 3.1, 2.4, 2.1, and 2.3 incorporated where directly relevant.
- Remaining uncertainty: confidence stays medium because the evidence supports robust OOD fragility, but the analogy and grokking counterexamples prevent a stronger all-or-nothing conclusion.

---

## Findings

### Executive Summary

Large Language Models trained on token continuation show a consistent breakdown on tasks that require structural intervention, meaning do-operator style reasoning, counterfactual reasoning, meaning alternate-world reasoning about what would have happened otherwise, or novel multi-step composition, and that pattern is better explained by the Stochastic Parrot framing of fluent surface modelling without grounded understanding than by robust algorithmic generalisation. [inference; source: https://web.cs.ucla.edu/~kaoru/3-layer-causal-hierarchy.pdf; https://treasures.scss.tcd.ie/miscellany/TCD-SCSS-X.20121208.002/AI-fabrications-related-articles/20210201-StochasticParrots-Proc2021ACM.pdf; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq3-1-llm-statistical-vs-causal.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq2-4-causal-hierarchy-formal-limits.md; https://arxiv.org/abs/2407.15720; https://arxiv.org/abs/2410.05229; https://opencausalab.github.io/CaLM]

This conclusion is strongest on causal and counterfactual prompts, where dedicated benchmarks report that accuracy deteriorates as task complexity rises and is often weaker on unseen or intervention-heavy settings than on simpler or more retrieval-friendly ones. [inference; source: https://arxiv.org/abs/2405.00622; https://opencausalab.github.io/CaLM; https://arxiv.org/abs/2404.06349; https://aclanthology.org/2024.sighan-1.17/]

Counterevidence exists: Power et al. report delayed generalisation in narrow synthetic regimes, and Webb et al. report strong zero-shot analogy performance in large language models. [fact; source: https://arxiv.org/abs/2201.02177; https://arxiv.org/abs/2212.09196]

The best-supported answer is that Large Language Models do form some abstractions, but those abstractions remain fragile and task-local, so OOD prompts that require mechanism-preserving intervention still expose them primarily as distribution learners rather than reliable structural reasoners. [inference; source: https://arxiv.org/abs/2212.09196; https://arxiv.org/abs/2407.15720; https://arxiv.org/abs/2410.05229; https://opencausalab.github.io/CaLM]

### Key Findings

1. **Standard Large Language Model training optimises prediction over observed token sequences, so prompts that require intervention semantics defined by do-operator queries or counterfactual structure defined by alternate-world queries push the model beyond the regime directly supervised by that training objective.** ([inference]; medium confidence; source: https://web.cs.ucla.edu/~kaoru/3-layer-causal-hierarchy.pdf; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq3-1-llm-statistical-vs-causal.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq2-4-causal-hierarchy-formal-limits.md)
2. **Evidence from deep learning generalisation theory shows that high-capacity neural networks can fit arbitrary labels and noise, so raw benchmark success alone does not establish portable algorithmic generalisation.** ([inference]; medium confidence; source: https://arxiv.org/abs/1611.03530)
3. **Grokking demonstrates that neural networks can eventually reach genuine algorithmic generalisation on small synthetic tasks, but that result is a possibility proof under narrow conditions rather than evidence that broad language-model pre-training has solved OOD reasoning.** ([inference]; medium confidence; source: https://arxiv.org/abs/2201.02177; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq3-1-llm-statistical-vs-causal.md)
4. **Compositional-generalisation studies repeatedly show that models trained on simple or nearby patterns do not reliably generalise to structurally richer combinations.** ([fact]; high confidence; source: https://arxiv.org/abs/1711.00350; https://aclanthology.org/2024.naacl-srw.3/; https://arxiv.org/abs/2407.15720)
5. **Arithmetic robustness studies show that changing only numerical values or inserting an irrelevant but plausible clause can sharply degrade performance under modest OOD perturbation.** ([fact]; medium confidence; source: https://arxiv.org/abs/2410.05229)
6. **Causal benchmark evidence shows that Large Language Models perform better on simpler or semantically familiar causal tasks than on intervention-heavy, counterfactual, or larger-structure settings, and they still lag specialised causal algorithms on harder cases.** ([fact]; high confidence; source: https://arxiv.org/abs/2404.06349; https://arxiv.org/abs/2405.00622; https://opencausalab.github.io/CaLM; https://aclanthology.org/2024.sighan-1.17/)
7. **The strongest counterevidence comes from analogical-reasoning results showing that scale can induce non-trivial abstract pattern induction, but that evidence narrows the Stochastic Parrot thesis more than it overturns the broader OOD failure record.** ([inference]; medium confidence; source: https://arxiv.org/abs/2212.09196; https://arxiv.org/abs/2410.05229; https://opencausalab.github.io/CaLM)
8. **The most defensible synthesis is a hybrid one in which current Large Language Models possess some partial abstractions, yet still behave mainly as high-capacity distribution learners when prompts demand genuinely novel compositions or structural interventions.** ([inference]; medium confidence; source: https://arxiv.org/abs/2212.09196; https://arxiv.org/abs/2407.15720; https://arxiv.org/abs/2410.05229; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq3-1-llm-statistical-vs-causal.md)

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [inference] Standard LLM training leaves intervention and counterfactual queries outside the regime directly identified by observational token prediction. | https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq3-1-llm-statistical-vs-causal.md ; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq2-4-causal-hierarchy-formal-limits.md | Medium | Prior-item synthesis, formal dependency. |
| [inference] High-capacity neural networks can fit random labels and noise, so benchmark success alone does not prove portable generalisation. | https://arxiv.org/abs/1611.03530 | Medium | Single primary source plus interpretive step. |
| [inference] Grokking proves possibility of algorithmic emergence, but only under narrow synthetic conditions. | https://arxiv.org/abs/2201.02177 ; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq3-1-llm-statistical-vs-causal.md | Medium | Possibility proof, not broad deployment proof. |
| [fact] Compositional-generalisation studies show repeated failure when simple learned pieces must be recombined into richer novel tasks. | https://arxiv.org/abs/1711.00350 ; https://aclanthology.org/2024.naacl-srw.3/ ; https://arxiv.org/abs/2407.15720 ; https://arxiv.org/abs/2312.11720 | High | Multiple independent task families. |
| [fact] Arithmetic reasoning quality drops under modest perturbations such as value substitution or irrelevant added clauses. | https://arxiv.org/abs/2410.05229 | Medium | Single primary source, large reported effect. |
| [fact] Causal benchmark performance deteriorates as causal complexity rises and remains weaker on intervention-heavy or unseen settings. | https://arxiv.org/abs/2405.00622 ; https://opencausalab.github.io/CaLM ; https://arxiv.org/abs/2404.06349 ; https://aclanthology.org/2024.sighan-1.17/ | High | Multiple benchmark families. |
| [inference] Strong analogy performance shows partial abstraction, but not general structural mastery across OOD reasoning domains. | https://arxiv.org/abs/2212.09196 ; https://arxiv.org/abs/2410.05229 ; https://opencausalab.github.io/CaLM | Medium | Counterevidence integrated rather than dismissed. |
| [inference] The total evidence best supports a hybrid view: partial abstractions inside a predominantly distributional reasoning regime. | https://arxiv.org/abs/2212.09196 ; https://arxiv.org/abs/2407.15720 ; https://arxiv.org/abs/2410.05229 ; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq3-1-llm-statistical-vs-causal.md | Medium | Final synthesis. |

### Assumptions

- [assumption] Text benchmarks that explicitly ask about interventions or counterfactuals are reasonable operational proxies for Level 2 and Level 3 reasoning, even though they remain text interfaces rather than real-world interventions. [source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq2-4-causal-hierarchy-formal-limits.md; https://arxiv.org/abs/2407.08029]
- [assumption] The current benchmark set is representative enough to support a medium-confidence conclusion about present-day Large Language Model behaviour, even though specific frontier models and prompting regimes continue to change. [source: https://arxiv.org/abs/2405.00622; https://opencausalab.github.io/CaLM; https://arxiv.org/abs/2404.06349]

### Analysis

The decisive question is whether a local abstraction survives when the task moves from familiar surface regularities to structurally novel demands. [inference; source: https://arxiv.org/abs/2212.09196; https://arxiv.org/abs/2407.15720]

On that test, the strongest evidence comes from perturbation-sensitive and intervention-sensitive evaluations, because those are the settings where a memorised template should fail and a genuine mechanism should remain stable. [inference; source: https://arxiv.org/abs/2410.05229; https://opencausalab.github.io/CaLM]

The grokking and analogy results matter because they prevent an overclaim. [inference; source: https://arxiv.org/abs/2201.02177; https://arxiv.org/abs/2212.09196]

They show that neural systems can learn abstract structure and that some current language models already do so on particular task families, so the shallowest "mere autocomplete" description misses part of the evidence. [inference; source: https://arxiv.org/abs/2201.02177; https://arxiv.org/abs/2212.09196]

The rival interpretation is that scale, careful prompting, or benchmark contamination explains most apparent failure, and that stronger future models will wash the pattern away. [inference; source: https://arxiv.org/abs/2407.08029]

That rival cannot be dismissed, but the best current evidence still weighs against it because newer causal and arithmetic benchmarks were designed to reduce shortcut routes and still report sharp degradation under structural novelty. [inference; source: https://arxiv.org/abs/2405.00622; https://arxiv.org/abs/2410.05229; https://aclanthology.org/2024.sighan-1.17/]

### Risks, Gaps, and Uncertainties

- Evidence for strong failure is broader than evidence for strong success, but the exact boundary between "partial abstraction" and "reliable mechanism learning" remains unsettled. [inference; source: https://arxiv.org/abs/2212.09196; https://opencausalab.github.io/CaLM]
- The benchmark literature is still moving, so some currently observed failures may shrink as architectures, tool use, or training curricula change. [inference; source: https://arxiv.org/abs/2405.00622; https://arxiv.org/abs/2410.05229]
- The item relies on textual proxies for intervention and counterfactual reasoning rather than on embodied or simulator-based interventions. [assumption; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq2-4-causal-hierarchy-formal-limits.md; https://arxiv.org/abs/2407.08029]
- Webb et al. supply genuine counterevidence for abstraction, so any absolute claim that LLMs only parrot without learning structure would overstate the record. [fact; source: https://arxiv.org/abs/2212.09196]

### Open Questions

1. Which training or post-training interventions most reliably convert narrow grokking-like emergence into broad OOD structural reasoning across arithmetic, logic, and causality?
2. How much of current OOD fragility comes from architecture, how much from objective function, and how much from benchmark contamination or prompt mismatch?
3. Would tool-augmented systems actually solve the structural problem, or do they mainly externalise it into a verifier or executor that performs the missing intervention logic?
4. What benchmark family best separates abstract analogy from truly intervention-capable reasoning, so that partial abstraction is not mistaken for full causal competence?

---

## Output

- Type: knowledge
- Description: This item concludes that current Large Language Models show repeated OOD fragility on structural-intervention tasks, while still leaving room for narrower emergent abstractions on selected analogy-style problems. [inference; source: https://arxiv.org/abs/2212.09196; https://arxiv.org/abs/2410.05229; https://opencausalab.github.io/CaLM]
- Links:
  - https://arxiv.org/abs/2410.05229
  - https://arxiv.org/abs/2405.00622
  - https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq3-1-llm-statistical-vs-causal.md
