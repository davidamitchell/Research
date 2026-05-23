---
review_count: 2
title: "RQ 3.1: Large Language Models as Statistical Optimisers, Token Distribution vs. Invariant Causal Models of Reality"
added: 2026-05-18T19:40:00+00:00
status: completed
priority: high
blocks:
  - 2026-05-18-rq3-2-stochastic-parrot-ood
started: 2026-05-19T09:59:12+00:00
completed: 2026-05-19T10:30:14+00:00
output: [knowledge]
themes: [llm-reasoning, benchmarks-eval, ai-architecture, causal-representation-learning, epistemology-of-ai]
cites:
  - 2026-05-18-rq2-4-causal-hierarchy-formal-limits
  - 2026-05-18-rq2-1-erm-causal-blindness
  - 2026-05-09-orthogonality-thesis-llm-training-posttraining-enterprise-risk
related:
  - 2026-04-30-orthogonality-thesis-ai-alignment-interpretability
  - 2026-05-18-rq3-2-stochastic-parrot-ood
  - 2026-05-18-rq3-3-cot-counterfactual-limits
superseded_by: ~
supersedes: ~
item_type: primary
confidence: medium
versions:
  - version: "1.0"
    sha: e5e657155f303c282654bfc384f2110a16a1d5b0
    changed: 2026-05-19
    progress: progress/2026-05-19-rq3-1-llm-statistical-vs-causal.md
    summary: "Initial completion"
---

# RQ 3.1: Large Language Models as Statistical Optimisers, Token Distribution vs. Invariant Causal Models of Reality

## Research Question

To what extent do Large Language Models (LLMs) optimise strictly for linguistic form and statistical token distribution rather than constructing internal, invariant causal models of reality?

## Scope

**In scope:**
- Distributional semantics, including J. R. Firth's hypothesis that "you shall know a word by the company it keeps", as the theoretical basis of LLM training
- Spurious correlations in high-dimensional text spaces as a natural consequence of token-level optimisation
- The Linear Representation Hypothesis: what geometry of internal representations would be necessary for causal reasoning?
- Empirical evidence for and against LLMs constructing invariant causal representations
- Connection to Phase 2's Empirical Risk Minimisation (ERM) and causal hierarchy analysis

**Out of scope:**
- Fine-tuning, Reinforcement Learning from Human Feedback (RLHF), and alignment techniques
- Specific LLM architectures, Transformer internals are supporting context, not the primary focus

**Constraints:** Builds directly on Phase 2, especially Research Question 2.4 on Pearl's Causal Hierarchy theorem, and must ground claims in formal properties rather than anecdote.

## Context

Phase 2 established the formal impossibility that a model trained on observational data cannot acquire interventional or counterfactual reasoning without additional causal structure. [fact; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq2-1-erm-causal-blindness.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq2-4-causal-hierarchy-formal-limits.md]

Phase 3 now applies that result to Large Language Models (LLMs), which are trained on large text corpora through next-token prediction, a Level 1 associational task on Pearl's ladder. [fact; source: https://arxiv.org/abs/2005.14165; https://web.stanford.edu/~jurafsky/slp3/ed3book.pdf; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq2-4-causal-hierarchy-formal-limits.md]

This item asks whether scale and architecture are enough to cross that formal barrier, or whether current evidence still places LLMs mainly on the observational side of the hierarchy. [inference; source: https://arxiv.org/abs/2403.04121; https://aclanthology.org/2024.emnlp-main.381/; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq2-4-causal-hierarchy-formal-limits.md]

## Approach

1. Characterise LLM training as an ERM problem over token distributions, formally, minimise next-token log loss or cross-entropy.
2. Apply Firth's Hypothesis: the distributional semantic signal available from text corpora is inherently Level 1 (association, not intervention).
3. Examine the Linear Representation Hypothesis: would linear probes for causal structure in LLM activations constitute evidence of causal modelling?
4. Survey empirical studies testing whether LLMs acquire causal representations (e.g., do they learn physical laws, or lexical proxies for them?).
5. Summarise: where does the evidence place LLMs on Pearl's causal hierarchy?

## Sources

- [ ] [Bender et al. (2021) On the Dangers of Stochastic Parrots: Can Language Models Be Too Big?](https://doi.org/10.1145/3442188.3445922) - seeded primary source; DOI landing checked, but not consulted for claim extraction.
- [ ] [Firth (1957) A Synopsis of Linguistic Theory 1930-1955](https://archive.org/details/papersinlinguist0000jrfi) - locator for the original distributional-semantics source; used as a bibliographic anchor, not for claim extraction.
- [x] [Brown et al. (2020) Language Models are Few-Shot Learners, Generative Pre-trained Transformer 3 (GPT-3)](https://arxiv.org/abs/2005.14165) - primary source confirming GPT-3 as an autoregressive language model trained on large text corpora.
- [x] [Jurafsky and Martin (2026) Speech and Language Processing, draft](https://web.stanford.edu/~jurafsky/slp3/ed3book.pdf) - accessible source for distributional semantics and next-token language-model framing.
- [x] [Brunila and LaViolette (2022) What company do words keep? Revisiting the distributional semantics of J.R. Firth and Zellig Harris](https://arxiv.org/abs/2205.07750) - open discussion of Firth's distributional hypothesis and its relation to modern Natural Language Processing (NLP).
- [x] [Bereska and Gavves (2024) Mechanistic Interpretability for Artificial Intelligence (AI) Safety: A Review](https://arxiv.org/abs/2404.14082) - review distinguishing observational probes from interventional methods in mechanistic interpretability.
- [x] [Nanda et al. (2023) Progress Measures for Grokking via Mechanistic Interpretability](https://arxiv.org/abs/2301.05217) - mechanistic-interpretability evidence that small transformers can learn structured algorithms.
- [x] [Kambhampati (2024) Can Large Language Models Reason and Plan?](https://arxiv.org/abs/2403.04121) - accessible preprint for the seeded review article.
- [x] [Yang et al. (2024) A Critical Review of Causal Reasoning Benchmarks for Large Language Models](https://arxiv.org/abs/2407.08029) - review arguing that many benchmark successes can be explained by retrieval of domain knowledge.
- [x] [Wang et al. (2024) CausalBench: A Comprehensive Benchmark for Evaluating Causal Reasoning Capabilities of Large Language Models](https://aclanthology.org/2024.sighan-1.17/) - benchmark designed to separate causal understanding from chance or narrow textual cueing.
- [x] [Chen et al. (2024) Causal Evaluation of Language Models](https://arxiv.org/abs/2405.00622) - large-scale benchmark plus project site documenting failure as causal complexity rises.
- [x] [OpenCausalLab (2024) CaLM project findings](https://opencausalab.github.io/CaLM) - accessible summary page reporting that causal-task performance declines sharply as task complexity increases.
- [x] [Kiciman et al. (2025) Causal Reasoning and Large Language Models: Opening a New Frontier for Causality](https://openreview.net/forum?id=mqoxLkX210) - evidence that LLMs can generate strong causal arguments from textual metadata while still showing unpredictable failure modes.
- [x] [Microsoft Research (2025) Causal Reasoning and Large Language Models: Opening a New Frontier for Causality](https://www.microsoft.com/en-us/research/publication/causal-reasoning-and-large-language-models-opening-a-new-frontier-for-causality/) - accessible abstract mirror for the same result.
- [x] [Gendron et al. (2024) Can Large Language Models Learn Independent Causal Mechanisms?](https://aclanthology.org/2024.emnlp-main.381/) - evidence that explicit causal constraints improve out-of-distribution behaviour relative to default language-model training.
- [x] [Research repo (2026-05-19) Research Question 2.1: Empirical Risk Minimisation's Causal Blindness and the Limits of In-Distribution Guarantees](https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq2-1-erm-causal-blindness.md) - prior item on observational risk minimisation and shortcut learning.
- [x] [Research repo (2026-05-19) Research Question 2.4: Pearl's Causal Hierarchy and the formal limits of observational data for intervention and counterfactual reasoning](https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq2-4-causal-hierarchy-formal-limits.md) - prior item on the formal observational ceiling.
- [x] [Research repo (2026-05-09) Orthogonality thesis under modern Large Language Model training and post-training: implications for enterprise tool-using workload risk](https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-09-orthogonality-thesis-llm-training-posttraining-enterprise-risk.md) - prior item on mechanistic-interpretability limits in production-scale models.

---

## Research Skill Output

*(Full output from running the research skill, retained verbatim in the completed item. Sections 0 to 5 are the investigation; Section 6 seeds the Findings section below.)*

### §0 Initialise

- Question: To what extent do Large Language Models optimise token prediction over textual distributions rather than learn invariant causal models of reality?
- Scope: distributional semantics, token-level Empirical Risk Minimisation framing, representational geometry, mechanistic interpretability, causal benchmarks, and placement on Pearl's causal hierarchy.
- Constraints: full mode, direct dependency on Research Questions 2.1 and 2.4, URL-backed sources only, and formal claims preferred over anecdote.
- Output: knowledge item with executive summary, key findings, evidence map, assumptions, analysis, risks, gaps, uncertainties, and open questions.
- Prior completed items consulted: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq2-1-erm-causal-blindness.md ; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq2-4-causal-hierarchy-formal-limits.md ; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-09-orthogonality-thesis-llm-training-posttraining-enterprise-risk.md

### §1 Question Decomposition

1. Training objective
   1.1 What objective does large-scale autoregressive language-model pre-training optimise?
   1.2 Why is that objective an observational or associational objective rather than an interventional one?
2. Distributional signal
   2.1 What does Firthian distributional semantics say about how meaning is learned from text?
   2.2 What kind of information is available in text corpora if the learner only sees token co-occurrence?
3. Formal barrier
   3.1 How do Research Questions 2.1 and 2.4 constrain what can be learned from observational text alone?
   3.2 Can scale or architecture alone dissolve the causal-hierarchy barrier?
4. Internal representation
   4.1 What would count as evidence that an internal representation is causal rather than merely decodable?
   4.2 Do linear probes or mechanistic-interpretability findings establish causal modelling?
5. Empirical performance
   5.1 What do current causal benchmarks say about Large Language Model performance on associational, interventional, and counterfactual tasks?
   5.2 What evidence suggests proxy use, benchmark retrieval, or poor out-of-distribution generalisation?
   5.3 What evidence suggests partial causal abstraction or useful latent structure?
6. Synthesis
   6.1 Is the best-supported answer that Large Language Models are strictly statistical, or that they are statistically trained systems with limited emergent abstractions?
   6.2 Where does that place them on Pearl's hierarchy?

### §2 Investigation

#### Access notes

- Access note: seeded Association for Computational Linguistics (ACL) Anthology URL -> unrelated 2020 International Conference on Computational Linguistics (COLING) paper; replaced with Internet Archive locator plus accessible modern discussions.
- Access note: seeded Bender and Kambhampati DOI landings -> 403 in this runtime; Kambhampati consulted via arXiv; Bender retained as identified but not consulted.

#### A. What the pre-training objective actually optimises

- [fact] Brown et al. describe Generative Pre-trained Transformer 3 (GPT-3) as an autoregressive language model trained on large corpora. [source: https://arxiv.org/abs/2005.14165]
- [inference] That training setup fits the continuation of token sequences rather than directly estimating intervention effects in a structural world model. [source: https://arxiv.org/abs/2005.14165; https://web.stanford.edu/~jurafsky/slp3/ed3book.pdf]
- [fact] Jurafsky and Martin describe language modelling as predicting upcoming words or tokens from prior words or tokens, and they present next-token prediction as the basic large-language-model task. [source: https://web.stanford.edu/~jurafsky/slp3/ed3book.pdf]
- [inference] Framed in the language of Research Question 2.1, this objective is an Empirical Risk Minimisation objective over textual observations, because the learner is rewarded for lowering predictive token loss on observed sequences rather than for preserving invariant mechanisms under intervention. [source: https://web.stanford.edu/~jurafsky/slp3/ed3book.pdf; https://arxiv.org/abs/2005.14165; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq2-1-erm-causal-blindness.md]

#### B. What text corpora make available to that objective

- [fact] Jurafsky and Martin state that the distributional hypothesis links similarity of meaning to similarity of context, and they explicitly place modern neural language models inside that tradition. [source: https://web.stanford.edu/~jurafsky/slp3/ed3book.pdf]
- [fact] Brunila and LaViolette note that the standard invocation of Firth in Natural Language Processing is the idea that words can be known by the company they keep, meaning by their co-occurrence patterns and contextual distribution. [source: https://arxiv.org/abs/2205.07750]
- [inference] Text therefore gives the model dense evidence about associations, regularities, genre cues, discourse patterns, and culturally repeated explanations, but it does not by itself provide the intervention semantics that Pearl's hierarchy requires for answering "what if we do X?" questions. [source: https://arxiv.org/abs/2205.07750; https://web.stanford.edu/~jurafsky/slp3/ed3book.pdf; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq2-4-causal-hierarchy-formal-limits.md]

#### C. Why Phase 2's formal limit still applies

- [fact] Research Question 2.1 concluded that Empirical Risk Minimisation can fit an observed distribution while remaining blind to the invariant cause-and-effect relations needed when the environment changes. [source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq2-1-erm-causal-blindness.md]
- [fact] Research Question 2.4 concluded that observational data generically do not determine interventional or counterfactual answers, and that Pearl's Causal Hierarchy almost never collapses from Level 2 to Level 1 or from Level 3 to Level 2. [source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq2-4-causal-hierarchy-formal-limits.md]
- [inference] Scaling a learner that still receives only Level 1 evidence can improve compression and pattern recovery without nullifying the information-theoretic barrier established in Research Question 2.4, because the missing intervention semantics are not created merely by increasing parameter count. [source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq2-4-causal-hierarchy-formal-limits.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq2-1-erm-causal-blindness.md; https://arxiv.org/abs/2403.04121]

#### D. What would count as evidence of causal modelling internally

- [fact] Bereska and Gavves distinguish observational interpretability methods, such as structured probes, from interventional methods, such as activation patching, and they state that interventional methods are the causal side of mechanistic interpretability. [source: https://arxiv.org/abs/2404.14082]
- [fact] The same review says observational approaches analyse existing representations without direct manipulation, whereas interventional approaches perturb model components to establish causal relationships. [source: https://arxiv.org/abs/2404.14082]
- [fact] Nanda et al. show that a small transformer trained on modular addition can be reverse engineered into a structured algorithm. [source: https://arxiv.org/abs/2301.05217]
- [inference] That result is evidence that neural networks can sometimes learn compact mechanistic structure in narrow controlled settings. [source: https://arxiv.org/abs/2301.05217]
- [fact] Bereska and Gavves treat the linear representation hypothesis as a useful simplification, but also note limits and counterexamples to assuming that important structure is always linearly encoded. [source: https://arxiv.org/abs/2404.14082]
- [inference] A successful linear probe for a causal variable is therefore evidence that information about that variable is decodable from activations, but not decisive evidence that the model uses an invariant causal model in producing its behaviour. [source: https://arxiv.org/abs/2404.14082; https://arxiv.org/abs/2301.05217]

#### E. What current causal evaluations show against strong causal-model claims

- [fact] Yang et al. review causal benchmarks for Large Language Models and argue that many of them can likely be solved through retrieval of domain knowledge. [source: https://arxiv.org/abs/2407.08029]
- [inference] That critique means benchmark success alone does not establish causal understanding. [source: https://arxiv.org/abs/2407.08029]
- [fact] Wang et al. introduce CausalBench to address the limitation that earlier textual benchmarks did not adequately distinguish genuine causal understanding from narrow cause-to-effect guessing, and they extend evaluation to intervention-style variants across text, mathematics, and code. [source: https://aclanthology.org/2024.sighan-1.17/]
- [fact] Chen et al. present Causal Evaluation of Language Models (CaLM) as a comprehensive benchmark for causal reasoning and report fifty high-level empirical findings across many models, tasks, and adaptation settings rather than a single headline score. [source: https://arxiv.org/abs/2405.00622]
- [fact] The CaLM project summary states that language models struggle on sophisticated causal reasoning tasks and that performance progressively deteriorates as causal complexity increases, eventually approaching zero on the hardest settings. [source: https://opencausalab.github.io/CaLM]
- [inference] Taken together, these sources indicate that many apparent causal successes by Large Language Models are fragile with respect to benchmark design, distribution shift, or escalation from association to intervention and counterfactual structure. [source: https://arxiv.org/abs/2407.08029; https://aclanthology.org/2024.sighan-1.17/; https://arxiv.org/abs/2405.00622; https://opencausalab.github.io/CaLM]

#### F. What current evidence shows in favour of partial causal competence

- [fact] Kiciman et al. report that Generative Pre-trained Transformer (GPT) family models, including GPT-3.5 and GPT-4, outperform earlier methods on pairwise causal discovery, counterfactual reasoning, and event-causality tasks, and they say these results cannot be explained by dataset memorisation alone. [source: https://openreview.net/forum?id=mqoxLkX210; https://www.microsoft.com/en-us/research/publication/causal-reasoning-and-large-language-models-opening-a-new-frontier-for-causality/]
- [fact] The same study also says that these models operate on text metadata, ignore the actual data, and exhibit unpredictable failure modes. [source: https://openreview.net/forum?id=mqoxLkX210; https://www.microsoft.com/en-us/research/publication/causal-reasoning-and-large-language-models-opening-a-new-frontier-for-causality/]
- [inference] That is why the authors recommend combining Large Language Models with existing causal techniques rather than treating them as complete causal engines. [source: https://openreview.net/forum?id=mqoxLkX210; https://www.microsoft.com/en-us/research/publication/causal-reasoning-and-large-language-models-opening-a-new-frontier-for-causality/]
- [fact] Gendron et al. say that standard Large Language Models fall short in uncommon settings and under distribution shifts, while architectures with sparsely interacting modules and explicit causal constraints improve out-of-distribution performance on abstract and causal reasoning tasks. [source: https://aclanthology.org/2024.emnlp-main.381/]
- [inference] These studies support a narrower claim than "Large Language Models learn invariant causal models of reality": they support that textual pre-training can leave models with useful abstractions and causal-language competence, but that robustness improves when extra causal structure is imposed explicitly. [source: https://openreview.net/forum?id=mqoxLkX210; https://aclanthology.org/2024.emnlp-main.381/]

#### G. Cross-item integration

- [fact] The prior enterprise-risk orthogonality item concluded that mechanistic interpretability can recover local circuits and useful features without yet extracting stable model-wide objectives from production-scale models. [source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-09-orthogonality-thesis-llm-training-posttraining-enterprise-risk.md]
- [inference] That conclusion reinforces the present item's narrower point that current evidence for internal structure in Large Language Models should not be over-read as proof that they possess explicit, invariant causal world models. [source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-09-orthogonality-thesis-llm-training-posttraining-enterprise-risk.md; https://arxiv.org/abs/2404.14082]

### §3 Reasoning

- [inference] The strongest evidence for the "statistical optimiser" side of the question comes from the training objective and the observational-information limit, not from any claim that Large Language Models never encode structured abstractions. [source: https://arxiv.org/abs/2005.14165; https://web.stanford.edu/~jurafsky/slp3/ed3book.pdf; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq2-4-causal-hierarchy-formal-limits.md]
- [inference] The right contrast is therefore not "purely shallow statistics" versus "fully formed causal world models", but "models trained on statistics of text that may internalise useful regularities without thereby earning the status of invariant causal models". [source: https://arxiv.org/abs/2407.08029; https://openreview.net/forum?id=mqoxLkX210; https://aclanthology.org/2024.emnlp-main.381/]
- [inference] Evidence from probes and benchmark outputs must be discounted when it only shows decodability or text-level success, because both can arise from correlations in language or stored world knowledge rather than from intervention-grounded causal structure. [source: https://arxiv.org/abs/2404.14082; https://arxiv.org/abs/2407.08029]

### §4 Consistency Check

- [fact] Tension: Kiciman et al. report strong performance on several causal-argument tasks. [source: https://openreview.net/forum?id=mqoxLkX210]
- [inference] Resolution: the same study says the models operate on text metadata, ignore actual data, and still show unpredictable failure modes, so the result supports useful causal-language competence without proving invariant causal modelling. [source: https://openreview.net/forum?id=mqoxLkX210; https://www.microsoft.com/en-us/research/publication/causal-reasoning-and-large-language-models-opening-a-new-frontier-for-causality/]
- [fact] Tension: mechanistic-interpretability work can sometimes recover real algorithms from neural networks. [source: https://arxiv.org/abs/2301.05217]
- [inference] Resolution: recovery in small controlled tasks does not overturn the broader observational-versus-interventional distinction, and current reviews still place causal claims on stronger footing when interventions rather than probes do the work. [source: https://arxiv.org/abs/2301.05217; https://arxiv.org/abs/2404.14082]
- [fact] Tension: causal constraints and modularity can improve out-of-distribution performance in language models. [source: https://aclanthology.org/2024.emnlp-main.381/]
- [inference] Resolution: this strengthens rather than weakens the main argument, because it suggests default next-token objectives do not already provide the invariances that explicit causal constraints add. [source: https://aclanthology.org/2024.emnlp-main.381/]

### §5 Depth and Breadth Expansion

- [inference] Technical lens: the key technical boundary is between observably decodable structure and intervention-stable mechanism, because only the latter supports reliable answers when context or environment shifts. [source: https://arxiv.org/abs/2404.14082; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq2-4-causal-hierarchy-formal-limits.md]
- [fact] Historical lens: distributional semantics long predates Large Language Models, so the present training recipe extends an association-based tradition rather than introducing a fundamentally new source of intervention data. [source: https://arxiv.org/abs/2205.07750; https://web.stanford.edu/~jurafsky/slp3/ed3book.pdf]
- [inference] Behavioural lens: benchmark evidence shows that performance is strongest where causal problems can be answered from textual regularities or familiar patterns and weaker where genuine intervention or counterfactual discipline is required. [source: https://arxiv.org/abs/2407.08029; https://opencausalab.github.io/CaLM; https://aclanthology.org/2024.sighan-1.17/]
- [inference] Methodological lens: if stronger causal behaviour appears only after adding architectural modularity, explicit causal constraints, tool use, or external causal methods, then the base pre-training signal should be treated as insufficient rather than automatically self-transcending at scale. [source: https://aclanthology.org/2024.emnlp-main.381; https://openreview.net/forum?id=mqoxLkX210]

### §6 Synthesis

**Executive summary:**

Present-day Large Language Models are systems trained to optimise predictive fit over textual token distributions, and current evidence does not show that they learn invariant causal models of reality. [inference; source: https://arxiv.org/abs/2005.14165; https://web.stanford.edu/~jurafsky/slp3/ed3book.pdf; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq2-1-erm-causal-blindness.md]

Current evidence does not support the stronger claim that scale and architecture alone let text-only pre-training cross Pearl's observational ceiling, because Phase 2's causal-hierarchy argument still applies and current causal benchmarks remain fragile under harder intervention and counterfactual settings. [inference; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq2-4-causal-hierarchy-formal-limits.md; https://arxiv.org/abs/2405.00622; https://opencausalab.github.io/CaLM; https://arxiv.org/abs/2407.08029]

The strongest contrary evidence is narrower: some models can generate good causal arguments from text metadata, and some controlled interpretability studies recover structured internal algorithms, which suggests partial abstraction rather than mere bag-of-words shallowness. [inference; source: https://openreview.net/forum?id=mqoxLkX210; https://arxiv.org/abs/2301.05217]

But those results still fall short of proving invariant causal world models, because probe-based evidence is not the same as interventional proof, and robustness improves when explicit causal constraints are added. [inference; source: https://arxiv.org/abs/2404.14082; https://aclanthology.org/2024.emnlp-main.381/]

The best-supported placement is therefore that present-day Large Language Models are predominantly Level 1 systems on Pearl's causal hierarchy, the framework that separates association, intervention, and counterfactual reasoning, with limited and uneven Level 2 or Level 3 competence reconstructed from textual regularities, stored world knowledge, and task scaffolding rather than from a verified invariant causal model. [inference; source: https://web.cs.ucla.edu/~kaoru/3-layer-causal-hierarchy.pdf; https://causalai.net/r60.pdf; https://openreview.net/forum?id=mqoxLkX210; https://opencausalab.github.io/CaLM]

**Key findings:**

1. Large Language Model pre-training is defined by autoregressive next-token prediction over observed text sequences, so the base optimisation target is predictive compression of token distributions rather than direct estimation of intervention-stable mechanisms. ([inference]; high confidence; source: https://arxiv.org/abs/2005.14165; https://web.stanford.edu/~jurafsky/slp3/ed3book.pdf)
2. Firthian distributional semantics, the view that words derive meaning from surrounding context, gives this training regime dense associational signal from co-occurrence and context, but that signal remains observational because text records patterns in language use rather than controlled interventions on the world. ([inference]; high confidence; source: https://web.stanford.edu/~jurafsky/slp3/ed3book.pdf; https://arxiv.org/abs/2205.07750)
3. Phase 2's Empirical Risk Minimisation and Pearl's causal hierarchy results imply that a model trained only on observational text cannot be assumed to recover Level 2 intervention semantics or Level 3 counterfactual structure merely by scaling the same observational objective. ([inference]; medium confidence; source: https://causalai.net/r60.pdf; https://arxiv.org/abs/1801.04016; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq2-1-erm-causal-blindness.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq2-4-causal-hierarchy-formal-limits.md)
4. Linear probes and other observational interpretability tools can show that causal or world-structured information is decodable from activations, but current reviews do not treat that as sufficient proof that the model is causally relying on an invariant internal world model. ([inference]; medium confidence; source: https://arxiv.org/abs/2404.14082; https://arxiv.org/abs/2301.05217)
5. Current causal benchmarks repeatedly show that Large Language Model performance degrades as tasks move from simpler causal association or familiar textual patterns toward harder intervention and counterfactual settings, which is the pattern expected from systems strongest at Level 1. ([inference]; medium confidence; source: https://arxiv.org/abs/2405.00622; https://opencausalab.github.io/CaLM; https://aclanthology.org/2024.sighan-1.17/)
6. Benchmark success on causal tasks cannot be taken at face value as proof of causal modelling because recent reviews argue that many tasks remain solvable through domain-knowledge retrieval or lexical regularities rather than through genuine intervention-grounded reasoning. ([fact]; medium confidence; source: https://arxiv.org/abs/2407.08029; https://aclanthology.org/2024.sighan-1.17/)
7. The best evidence for partial causal competence is that Generative Pre-trained Transformer family models can generate strong causal arguments on some tasks and generalise beyond training-cutoff datasets, but those same studies report unpredictable failure modes and explicitly recommend combining Large Language Models with external causal methods. ([inference]; medium confidence; source: https://openreview.net/forum?id=mqoxLkX210; https://www.microsoft.com/en-us/research/publication/causal-reasoning-and-large-language-models-opening-a-new-frontier-for-causality/)
8. Evidence that explicit causal constraints and sparsely interacting modules improve out-of-distribution performance suggests that default next-token language modelling does not already provide the invariant causal mechanisms that stronger causal robustness would require. ([inference]; medium confidence; source: https://aclanthology.org/2024.emnlp-main.381/)
9. The strongest overall conclusion is that Large Language Models do learn abstractions, but present evidence supports statistical and text-mediated abstractions more strongly than verified invariant causal models of reality. ([inference]; medium confidence; source: https://arxiv.org/abs/2407.08029; https://openreview.net/forum?id=mqoxLkX210; https://aclanthology.org/2024.emnlp-main.381/; https://arxiv.org/abs/2404.14082)

**Evidence map:**

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [fact] Base Large Language Model pre-training optimises next-token prediction over text. | https://arxiv.org/abs/2005.14165 ; https://web.stanford.edu/~jurafsky/slp3/ed3book.pdf | high | Training-objective claim. |
| [fact] Distributional semantics grounds meaning in contextual co-occurrence. | https://web.stanford.edu/~jurafsky/slp3/ed3book.pdf ; https://arxiv.org/abs/2205.07750 | high | Firthian background. |
| [inference] Observational text-only learning does not erase Phase 2's causal barrier. | https://causalai.net/r60.pdf ; https://arxiv.org/abs/1801.04016 ; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq2-1-erm-causal-blindness.md ; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq2-4-causal-hierarchy-formal-limits.md | medium | Cross-item dependence plus primary causal-theory support. |
| [inference] Probe success is weaker evidence than interventional mechanistic proof. | https://arxiv.org/abs/2404.14082 ; https://arxiv.org/abs/2301.05217 | medium | Distinguishes decodability from use. |
| [fact] Causal-task performance deteriorates as causal complexity increases. | https://arxiv.org/abs/2405.00622 ; https://opencausalab.github.io/CaLM ; https://aclanthology.org/2024.sighan-1.17/ | medium | Benchmark family evidence. |
| [fact] Many causal benchmarks can be solved by retrieval or familiar textual knowledge. | https://arxiv.org/abs/2407.08029 ; https://aclanthology.org/2024.sighan-1.17/ | medium | Qualification on benchmark interpretation. |
| [fact] Some Large Language Models can still produce strong causal arguments from text metadata. | https://openreview.net/forum?id=mqoxLkX210 ; https://www.microsoft.com/en-us/research/publication/causal-reasoning-and-large-language-models-opening-a-new-frontier-for-causality/ | medium | Partial positive evidence. |
| [inference] Explicit causal constraints improve robustness because the default objective is insufficient. | https://aclanthology.org/2024.emnlp-main.381/ | medium | Improvement under added causal structure. |
| [inference] Present-day Large Language Models are mainly Level 1 systems with uneven higher-level competence. | https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq2-4-causal-hierarchy-formal-limits.md ; https://opencausalab.github.io/CaLM ; https://openreview.net/forum?id=mqoxLkX210 | medium | Final placement claim. |

**Assumptions:**

- [assumption] Text corpora do not contain enough implicit intervention structure to overturn Pearl's generic observational ceiling without additional architectural or data assumptions, because no consulted source demonstrates such a collapse for present-day Large Language Models. [source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq2-4-causal-hierarchy-formal-limits.md; https://aclanthology.org/2024.emnlp-main.381/]
- [assumption] Benchmark performance is a usable but incomplete proxy for underlying causal competence, because latent-model structure cannot currently be read off directly at scale and benchmark reviews explicitly question surface-score interpretations. [source: https://arxiv.org/abs/2407.08029; https://arxiv.org/abs/2404.14082]

**Analysis:**

The evidence is strongest where the question is about objective and information source, because both are directly specified. [inference; source: https://arxiv.org/abs/2005.14165; https://web.stanford.edu/~jurafsky/slp3/ed3book.pdf]

The more speculative step is moving from "trained on token prediction" to "cannot learn any useful abstraction", and the consulted evidence does not justify that stronger negative claim. [inference; source: https://arxiv.org/abs/2301.05217; https://openreview.net/forum?id=mqoxLkX210]

The right synthesis is therefore asymmetric: the training objective and causal hierarchy justify scepticism about invariant causal modelling, while benchmark and interpretability evidence justify acknowledging partial abstraction and partial causal competence. [inference; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq2-4-causal-hierarchy-formal-limits.md; https://arxiv.org/abs/2404.14082; https://openreview.net/forum?id=mqoxLkX210]

Alternative explanations remain live. [fact; source: https://aclanthology.org/2024.emnlp-main.381; https://arxiv.org/abs/2407.08029]

One alternative is that causal competence is mostly benchmark artefact or retrieval from text. [inference; source: https://arxiv.org/abs/2407.08029]

Another is that some causal abstractions do emerge, but only weakly or incompletely under the default objective and become more robust when explicit causal structure is added. [inference; source: https://aclanthology.org/2024.emnlp-main.381; https://openreview.net/forum?id=mqoxLkX210]

The consulted evidence supports the second explanation more strongly than the first, because there is repeated positive evidence for some causal-task competence, but not for full intervention-stable world modelling. [inference; source: https://openreview.net/forum?id=mqoxLkX210; https://opencausalab.github.io/CaLM; https://aclanthology.org/2024.emnlp-main.381/]

**Risks, gaps, uncertainties:**

- Direct inspection of production-scale model internals remains limited, so the conclusion is partly constrained by what current mechanistic-interpretability tools can test rather than by a full latent-state ground truth. [inference; source: https://arxiv.org/abs/2404.14082; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-09-orthogonality-thesis-llm-training-posttraining-enterprise-risk.md]
- Most empirical studies evaluate behaviour on tasks rather than intervention-grounded world interaction, which limits how strongly benchmark outcomes can be translated into claims about internal causal world models. [inference; source: https://arxiv.org/abs/2405.00622; https://arxiv.org/abs/2407.08029]

**Open questions:**

- What changes when language models are trained with explicit interaction data, simulator interventions, or multimodal world grounding rather than text alone?
- Can future interventional interpretability methods distinguish decodable causal variables from truly mechanism-governing internal representations at frontier scale?
- Which observed causal-task gains come from stored textual world knowledge, which come from learned abstraction, and which require external tool scaffolding?

### §7 Recursive Review

- Review result: pass
- Acronym audit: Large Language Model (LLM), Empirical Risk Minimisation (ERM), Reinforcement Learning from Human Feedback (RLHF), Natural Language Processing (NLP), Artificial Intelligence (AI)
- Claim audit: all visible claims in Research Skill Output labeled as fact, inference, or assumption, except pure workflow metadata in Section 0 and review metadata here
- Cross-item audit: direct dependence on Research Questions 2.1 and 2.4 and thematic link to the orthogonality item are reflected in frontmatter and cited prose
- Findings parity: Section 6 and Findings use the same substantive conclusions, confidence levels, and source families

---

## Findings

*(Populated from §6 Synthesis above.)*

### Executive Summary

Present-day Large Language Models are systems trained to optimise predictive fit over textual token distributions, and current evidence does not show that they learn invariant causal models of reality. [inference; source: https://arxiv.org/abs/2005.14165; https://web.stanford.edu/~jurafsky/slp3/ed3book.pdf; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq2-1-erm-causal-blindness.md]

Current evidence does not support the stronger claim that scale and architecture alone let text-only pre-training cross Pearl's observational ceiling, because Phase 2's causal-hierarchy argument still applies and current causal benchmarks remain fragile under harder intervention and counterfactual settings. [inference; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq2-4-causal-hierarchy-formal-limits.md; https://arxiv.org/abs/2405.00622; https://opencausalab.github.io/CaLM; https://arxiv.org/abs/2407.08029]

The strongest contrary evidence is narrower: some models can generate good causal arguments from text metadata, and some controlled interpretability studies recover structured internal algorithms, which suggests partial abstraction rather than mere bag-of-words shallowness. [inference; source: https://openreview.net/forum?id=mqoxLkX210; https://arxiv.org/abs/2301.05217]

But those results still fall short of proving invariant causal world models, because probe-based evidence is not the same as interventional proof, and robustness improves when explicit causal constraints are added. [inference; source: https://arxiv.org/abs/2404.14082; https://aclanthology.org/2024.emnlp-main.381/]

The best-supported placement is therefore that present-day Large Language Models are predominantly Level 1 systems on Pearl's causal hierarchy, the framework that separates association, intervention, and counterfactual reasoning, with limited and uneven Level 2 or Level 3 competence reconstructed from textual regularities, stored world knowledge, and task scaffolding rather than from a verified invariant causal model. [inference; source: https://web.cs.ucla.edu/~kaoru/3-layer-causal-hierarchy.pdf; https://causalai.net/r60.pdf; https://openreview.net/forum?id=mqoxLkX210; https://opencausalab.github.io/CaLM]

### Key Findings

1. **Large Language Model pre-training is defined by autoregressive next-token prediction over observed text sequences, so the base optimisation target is predictive compression of token distributions rather than direct estimation of intervention-stable mechanisms.** ([inference]; high confidence; source: https://arxiv.org/abs/2005.14165; https://web.stanford.edu/~jurafsky/slp3/ed3book.pdf)
2. **Firthian distributional semantics, the view that words derive meaning from surrounding context, gives this training regime dense associational signal from co-occurrence and context, but that signal remains observational because text records patterns in language use rather than controlled interventions on the world.** ([inference]; high confidence; source: https://web.stanford.edu/~jurafsky/slp3/ed3book.pdf; https://arxiv.org/abs/2205.07750)
3. **Phase 2's Empirical Risk Minimisation and Pearl's causal hierarchy results imply that a model trained only on observational text cannot be assumed to recover Level 2 intervention semantics or Level 3 counterfactual structure merely by scaling the same observational objective.** ([inference]; medium confidence; source: https://causalai.net/r60.pdf; https://arxiv.org/abs/1801.04016; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq2-1-erm-causal-blindness.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq2-4-causal-hierarchy-formal-limits.md)
4. **Linear probes and other observational interpretability tools can show that causal or world-structured information is decodable from activations, but current reviews do not treat that as sufficient proof that the model is causally relying on an invariant internal world model.** ([inference]; medium confidence; source: https://arxiv.org/abs/2404.14082; https://arxiv.org/abs/2301.05217)
5. **Current causal benchmarks repeatedly show that Large Language Model performance degrades as tasks move from simpler causal association or familiar textual patterns toward harder intervention and counterfactual settings, which is the pattern expected from systems strongest at Level 1.** ([inference]; medium confidence; source: https://arxiv.org/abs/2405.00622; https://opencausalab.github.io/CaLM; https://aclanthology.org/2024.sighan-1.17/)
6. **Benchmark success on causal tasks cannot be taken at face value as proof of causal modelling because recent reviews argue that many tasks remain solvable through domain-knowledge retrieval or lexical regularities rather than through genuine intervention-grounded reasoning.** ([fact]; medium confidence; source: https://arxiv.org/abs/2407.08029; https://aclanthology.org/2024.sighan-1.17/)
7. **The best evidence for partial causal competence is that Generative Pre-trained Transformer family models can generate strong causal arguments on some tasks and generalise beyond training-cutoff datasets, but those same studies report unpredictable failure modes and explicitly recommend combining Large Language Models with external causal methods.** ([inference]; medium confidence; source: https://openreview.net/forum?id=mqoxLkX210; https://www.microsoft.com/en-us/research/publication/causal-reasoning-and-large-language-models-opening-a-new-frontier-for-causality/)
8. **Evidence that explicit causal constraints and sparsely interacting modules improve out-of-distribution performance suggests that default next-token language modelling does not already provide the invariant causal mechanisms that stronger causal robustness would require.** ([inference]; medium confidence; source: https://aclanthology.org/2024.emnlp-main.381/)
9. **The strongest overall conclusion is that Large Language Models do learn abstractions, but present evidence supports statistical and text-mediated abstractions more strongly than verified invariant causal models of reality.** ([inference]; medium confidence; source: https://arxiv.org/abs/2407.08029; https://openreview.net/forum?id=mqoxLkX210; https://aclanthology.org/2024.emnlp-main.381/; https://arxiv.org/abs/2404.14082)

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [fact] Base Large Language Model pre-training optimises next-token prediction over text. | https://arxiv.org/abs/2005.14165 ; https://web.stanford.edu/~jurafsky/slp3/ed3book.pdf | high | Training-objective claim. |
| [fact] Distributional semantics grounds meaning in contextual co-occurrence. | https://web.stanford.edu/~jurafsky/slp3/ed3book.pdf ; https://arxiv.org/abs/2205.07750 | high | Firthian background. |
| [inference] Observational text-only learning does not erase Phase 2's causal barrier. | https://causalai.net/r60.pdf ; https://arxiv.org/abs/1801.04016 ; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq2-1-erm-causal-blindness.md ; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq2-4-causal-hierarchy-formal-limits.md | medium | Cross-item dependence plus primary causal-theory support. |
| [inference] Probe success is weaker evidence than interventional mechanistic proof. | https://arxiv.org/abs/2404.14082 ; https://arxiv.org/abs/2301.05217 | medium | Distinguishes decodability from use. |
| [fact] Causal-task performance deteriorates as causal complexity increases. | https://arxiv.org/abs/2405.00622 ; https://opencausalab.github.io/CaLM ; https://aclanthology.org/2024.sighan-1.17/ | medium | Benchmark family evidence. |
| [fact] Many causal benchmarks can be solved by retrieval or familiar textual knowledge. | https://arxiv.org/abs/2407.08029 ; https://aclanthology.org/2024.sighan-1.17/ | medium | Qualification on benchmark interpretation. |
| [fact] Some Large Language Models can still produce strong causal arguments from text metadata. | https://openreview.net/forum?id=mqoxLkX210 ; https://www.microsoft.com/en-us/research/publication/causal-reasoning-and-large-language-models-opening-a-new-frontier-for-causality/ | medium | Partial positive evidence. |
| [inference] Explicit causal constraints improve robustness because the default objective is insufficient. | https://aclanthology.org/2024.emnlp-main.381/ | medium | Improvement under added causal structure. |
| [inference] Present-day Large Language Models are mainly Level 1 systems with uneven higher-level competence. | https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq2-4-causal-hierarchy-formal-limits.md ; https://opencausalab.github.io/CaLM ; https://openreview.net/forum?id=mqoxLkX210 | medium | Final placement claim. |

### Assumptions

- [assumption] Text corpora do not contain enough implicit intervention structure to overturn Pearl's generic observational ceiling without additional architectural or data assumptions, because no consulted source demonstrates such a collapse for present-day Large Language Models. [source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq2-4-causal-hierarchy-formal-limits.md; https://aclanthology.org/2024.emnlp-main.381/]
- [assumption] Benchmark performance is a usable but incomplete proxy for underlying causal competence, because latent-model structure cannot currently be read off directly at scale and benchmark reviews explicitly question surface-score interpretations. [source: https://arxiv.org/abs/2407.08029; https://arxiv.org/abs/2404.14082]

### Analysis

The evidence is strongest where the question is about objective and information source, because both are directly specified. [inference; source: https://arxiv.org/abs/2005.14165; https://web.stanford.edu/~jurafsky/slp3/ed3book.pdf]

The more speculative step is moving from "trained on token prediction" to "cannot learn any useful abstraction", and the consulted evidence does not justify that stronger negative claim. [inference; source: https://arxiv.org/abs/2301.05217; https://openreview.net/forum?id=mqoxLkX210]

The right synthesis is therefore asymmetric: the training objective and causal hierarchy justify scepticism about invariant causal modelling, while benchmark and interpretability evidence justify acknowledging partial abstraction and partial causal competence. [inference; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq2-4-causal-hierarchy-formal-limits.md; https://arxiv.org/abs/2404.14082; https://openreview.net/forum?id=mqoxLkX210]

Alternative explanations remain live. [fact; source: https://aclanthology.org/2024.emnlp-main.381/; https://arxiv.org/abs/2407.08029]

One alternative is that causal competence is mostly benchmark artefact or retrieval from text. [inference; source: https://arxiv.org/abs/2407.08029]

Another is that some causal abstractions do emerge, but only weakly or incompletely under the default objective and become more robust when explicit causal structure is added. [inference; source: https://aclanthology.org/2024.emnlp-main.381/; https://openreview.net/forum?id=mqoxLkX210]

The consulted evidence supports the second explanation more strongly than the first, because there is repeated positive evidence for some causal-task competence, but not for full intervention-stable world modelling. [inference; source: https://openreview.net/forum?id=mqoxLkX210; https://opencausalab.github.io/CaLM; https://aclanthology.org/2024.emnlp-main.381/]

### Risks, Gaps, and Uncertainties

- Direct inspection of production-scale model internals remains limited, so the conclusion is partly constrained by what current mechanistic-interpretability tools can test rather than by a full latent-state ground truth. [inference; source: https://arxiv.org/abs/2404.14082; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-09-orthogonality-thesis-llm-training-posttraining-enterprise-risk.md]
- Most empirical studies evaluate behaviour on tasks rather than intervention-grounded world interaction, which limits how strongly benchmark outcomes can be translated into claims about internal causal world models. [inference; source: https://arxiv.org/abs/2405.00622; https://arxiv.org/abs/2407.08029]

### Open Questions

- What changes when language models are trained with explicit interaction data, simulator interventions, or multimodal world grounding rather than text alone?
- Can future interventional interpretability methods distinguish decodable causal variables from truly mechanism-governing internal representations at frontier scale?
- Which observed causal-task gains come from stored textual world knowledge, which come from learned abstraction, and which require external tool scaffolding?

---

## Output

- Type: knowledge
- Description: Present-day Large Language Models are best supported as statistical text optimisers with partial and uneven causal competence, not as verified invariant causal world models. [inference; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq2-4-causal-hierarchy-formal-limits.md; https://openreview.net/forum?id=mqoxLkX210; https://opencausalab.github.io/CaLM]
- Links:
  - https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq2-4-causal-hierarchy-formal-limits.md
  - https://arxiv.org/abs/2404.14082
  - https://openreview.net/forum?id=mqoxLkX210
