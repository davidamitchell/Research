---
title: "Hallucination-Associated Neurons (H-Neurons) in LLMs — Identification, Behavioural Impact, and Origins"
added: 2026-03-05T20:11:40+00:00
status: completed
priority: high
blocks: [2026-03-05-h-neuron-over-compliance, 2026-03-05-h-neuron-pretraining-origins]
tags: [llm, hallucinations, h-neurons, mechanistic-interpretability, over-compliance, pre-training, alignment, reliability, arxiv]
started: 2026-03-05T20:11:40+00:00
completed: 2026-03-05T20:11:40+00:00
output: [knowledge, backlog-item]
cites: []          # slugs of items this item directly depends on or quotes
related: []        # slugs of thematically connected items
superseded_by: ~   # slug of a later item that overrides this one (null if not superseded)
supersedes: ~      # slug of an older item this one replaces (null if not applicable)
item_type: primary # primary | synthesis
confidence: medium # high | medium | low
versions: []       # entries: {version: "1.0", sha: "<commit-hash>", changed: YYYY-MM-DD, progress: "<path>", summary: "<one-line>"}
---

# Hallucination-Associated Neurons (H-Neurons) in LLMs — Identification, Behavioural Impact, and Origins

## Research Question

What are Hallucination-Associated Neurons (H-Neurons) in large language models, how can they be identified, what behaviours do they cause, where do they come from, and what do these findings imply for building more reliable LLMs?

## Scope

**In scope:**
- The three-part investigation structure of arXiv:2512.01797: identification, behavioural impact, and origins of H-Neurons
- The methodology for identifying H-Neurons: what features make a neuron "hallucination-associated" and how sparse that set is (<0.1% of total neurons)
- How controlled interventions (activation suppression/amplification) confirm the causal link between H-Neurons and hallucination
- The specific behavioural pathway: H-Neurons → over-compliance → hallucination
- The pre-training origin finding: H-Neurons are already predictive in base models before instruction tuning or RLHF
- Generalisation across diverse scenarios and LLM architectures
- Implications for future work: neuron-level detection, targeted suppression, training-time interventions

**Out of scope:**
- Broad hallucination taxonomy (covered in `2026-03-05-llm-hallucination-mechanisms`)
- Detailed over-compliance behaviour and intervention design (covered in `2026-03-05-h-neuron-over-compliance`)
- Deep dive on pre-training implications for LLM development (covered in `2026-03-05-h-neuron-pretraining-origins`)

**Constraints:** Primary source is arXiv:2512.01797 (Gao et al., Dec 2025); supplemented by contemporaneous mechanistic interpretability literature. Aim for a thorough but accessible synthesis — assume the reader has completed `2026-03-05-llm-hallucination-mechanisms` first.

## Context

Prior work on LLM hallucinations has operated at a macroscopic level: training data quality, RLHF objectives, decoding strategies. What has been missing is a microscopic account — which specific parts of the network are doing what, and why? Gao et al. (arXiv:2512.01797) take a systematic neuron-level approach to this question for the first time.

Their key result is striking: fewer than 0.1% of neurons reliably predict whether the model will hallucinate, and this prediction generalises across diverse tasks. These neurons are not incidental — controlled interventions show that suppressing them reduces hallucination, while amplifying them increases it. Furthermore, they are not an artefact of RLHF: they are already present and predictive in base pre-trained models.

This combination of findings — sparsity, causal role, generality, and pre-training origin — opens up a concrete new angle for improving LLM reliability: targeted neuron-level monitoring and intervention.

**Prior research:** Two completed items are directly relevant. `2026-03-05-llm-hallucination-mechanisms.md` established the macroscopic hallucination landscape: hallucination taxonomy (intrinsic/extrinsic, factual/faithfulness), root causes (training data noise, distributional shift, next-token prediction without factuality incentive, RLHF over-optimisation, decoding stochasticity), mitigation approaches (RAG, constitutional AI, chain-of-thought, fact-checking), and crucially the explanatory gap — macroscopic accounts explain statistical tendencies but cannot identify which part of the network executes a specific hallucination decision. That gap directly motivates the H-Neurons paper. `2026-02-28-controlled-hallucination-perception-as-construction.md` covered biological perception as controlled hallucination (Anil Seth); the conceptual parallel is that both biological and artificial systems construct outputs that override incoming evidence, but the mechanisms are entirely different. This item must add: the specific identification methodology (CETT metric, sparse linear probing), the causal behavioural pathway (H-Neurons → over-compliance → hallucination), the pre-training origin evidence (cross-model transfer experiments, parameter inertia), and the concrete implication map for LLM reliability engineering.

## Approach

1. **Read and annotate the paper** — Work through arXiv:2512.01797 section by section. Produce a structured summary of each of the three investigation axes (identification, behavioural impact, origins).

2. **Identification methodology** — How do the authors identify H-Neurons? What is the activation-level criterion? What classifier or statistical test distinguishes H-Neurons from the other 99.9%+? How is "generalisation across scenarios" evaluated?

3. **Behavioural impact** — What exactly is "controlled intervention"? How is the causal link established (vs. correlation)? What is the over-compliance pathway — how does an H-Neuron produce a plausible-but-false output?

4. **Origins investigation** — How do the authors test whether H-Neurons originate in pre-training? What is compared between base models and instruction-tuned/RLHF variants? What does it mean that these neurons "emerge during pre-training"?

5. **Generalisation and limits** — On which model families and tasks does the finding hold? Where does it not hold, or where is the evidence weak? What are the authors' own stated limitations?

6. **Implications synthesis** — What concrete next steps do the findings suggest? Immediate applications (runtime hallucination detection), medium-term applications (targeted neuron suppression at inference), longer-term applications (training-time regularisation or data curation to suppress H-Neuron formation).

## Sources

- [x] Gao et al. (2025) — "Hallucination-Associated Neurons in LLMs": https://arxiv.org/abs/2512.01797 ← **primary source**
- [ ] "They solved AI hallucinations!" (YouTube explainer) — accessible walkthrough of the H-Neurons paper: the liar circuit concept, L1-regularised sparse probe methodology, intervention challenges, and implications for real-time hallucination detection: https://youtu.be/1ONwQzauqkc
- [x] Elhage et al. (2022) — "Toy Models of Superposition" (Anthropic) — background on how neurons encode features: https://transformer-circuits.pub/2022/toy_model/index.html
- [x] Meng et al. (2022) — "Locating and Editing Factual Associations in GPT" (ROME) — neuron-level causal tracing in GPT-family decoder models: https://arxiv.org/abs/2202.05262
- [ ] Bereska & Gavves (2024) — "Mechanistic Interpretability for AI Safety — A Review": https://arxiv.org/abs/2404.14082
- [ ] `Research/backlog/2026-03-05-llm-hallucination-mechanisms.md` — prerequisite: hallucination taxonomy and macroscopic causes
- [ ] `Research/backlog/2026-03-05-h-neuron-over-compliance.md` — downstream: behavioural consequences and interventions
- [ ] `Research/backlog/2026-03-05-h-neuron-pretraining-origins.md` — downstream: pre-training origins and LLM development implications

---

## Research Skill Output

### §0 Initialise

**Research question restated:** What are Hallucination-Associated Neurons (H-Neurons) in LLMs, how are they identified, what behaviours do they cause, where do they originate, and what do these findings imply for building more reliable models?

**Scope confirmation:** Primary investigation of arXiv:2512.01797 (Gao et al., Tsinghua University, December 2025). The three axes are identification methodology (CETT metric, sparse linear probing), behavioural impact (controlled activation perturbation across four over-compliance benchmarks), and origins (cross-model transfer experiments, parameter evolution analysis). Supplementary context from Meng et al. 2022 (ROME — causal tracing precedent in FFN layers) and Elhage et al. 2022 (toy models of superposition — background on neuron feature encoding). The macroscopic hallucination landscape is treated as established background from prior completed item.

**Constraints:** Focus on feed-forward network (FFN) neurons; the paper explicitly excludes attention heads from analysis. Findings are evaluated on six models: Mistral-7B-v0.3, Mistral-Small-3.1-24B, Gemma-3-4B, Gemma-3-27B, Llama-3.1-8B, Llama-3.3-70B. The YouTube explainer (https://youtu.be/1ONwQzauqkc) could not be accessed directly; transcript content is unavailable. Bereska & Gavves (2024) was not accessed.

**Output format:** Full research skill output (§0–§7), followed by structured Findings section. Mode: full.

### §1 Question Decomposition

**Root question:** What are H-Neurons, how are they identified, what do they cause, where do they come from, and what do the findings imply?

Decomposed into five branches:

**Branch A — Identification**
- A1: What are H-Neurons at a definitional level — what property makes a neuron "hallucination-associated"?
- A2: What is the CETT metric and why is it used instead of raw activation magnitude?
- A3: How is the training dataset constructed for the sparse classifier — what filtering ensures signal quality?
- A4: What is the L1-regularised logistic regression approach and why does L1 regularisation specifically identify a sparse subset?
- A5: How sparse is "sparse" — what quantitative proportion of neurons are identified as H-Neurons?
- A6: How is generalisation evaluated — which out-of-distribution scenarios are tested?

**Branch B — Behavioural Impact**
- B1: What is the perturbation methodology — how are H-Neuron activations scaled during inference?
- B2: What four benchmarks are used and what form of over-compliance does each probe?
- B3: What is the over-compliance pathway — how does H-Neuron activation produce a hallucinated output?
- B4: What is the dose-response relationship between scaling factor and compliance rate?
- B5: Does model size modulate susceptibility to H-Neuron perturbation?

**Branch C — Origins**
- C1: What is the cross-model transfer experiment design?
- C2: What do AUROC scores on base models reveal about when H-Neurons originate?
- C3: What does the parameter evolution analysis (cosine distance of SFT weights) reveal?
- C4: Why does the next-token prediction objective specifically produce H-Neurons?

**Branch D — Generalisation and Limits**
- D1: Which model families and scales are tested, and are there notable failures?
- D2: What does the paper identify as its own limitations?
- D3: How does the finding relate to prior neuron-level causal tracing work (ROME)?

**Branch E — Implications**
- E1: What are the immediate runtime applications of H-Neuron signals?
- E2: What are the challenges for practical neuron-suppression as a mitigation?
- E3: What longer-term training-time interventions does the finding suggest?

### §2 Investigation

**Branch A — Identification**

**A1 — Definition of H-Neurons** [fact: Gao et al. 2025, arXiv:2512.01797]

H-Neurons are neurons in the feed-forward network (FFN) layers of a transformer whose activation patterns reliably distinguish hallucinatory from faithful responses. The defining criterion is statistical: a neuron qualifies as an H-Neuron if it receives a positive non-zero weight from a sparse logistic regression classifier trained to predict hallucination from neuron contribution profiles. The paper focuses exclusively on FFN neurons (specifically the intermediate dimension of each MLP block), not on attention heads or other components.

**A2 — The CETT metric** [fact: Gao et al. 2025]

Raw activation magnitude is insufficient because a highly active neuron may have negligible downstream influence if its corresponding down-projection weights are small. The CETT (Contribution of Each neuron To the hidden sTate) metric captures causal efficacy rather than mere activity. For neuron j at token position t, CETT is computed as the ratio of the L2 norm of that neuron's projected output vector to the L2 norm of the total hidden state:

CETT_{j,t} = ||h_t^(j)||_2 / ||h_t||_2

where h_t^(j) = W_down · z_t^(j) is the contribution of neuron j's activation to the hidden state. This normalisation ensures that only neurons with substantial causal influence on the representation — not merely active neurons — are selected.

Crucially, the authors extract CETT specifically at answer tokens (identified by GPT-4o to find the factual claim spans), not at syntactic filler tokens. They construct two aggregate features per neuron per response: average CETT at answer tokens and average CETT at non-answer tokens. Using both features allows the classifier to filter out neurons that are globally active (e.g., those participating in general language generation) and identify only those selectively active during factual answer generation.

**A3 — Training dataset construction** [fact: Gao et al. 2025]

Training data comes from TriviaQA. For each question, 10 responses are sampled at temperature 1.0, top_k=50, top_p=0.9. Only questions where the model is *consistently* correct across all 10 samples, or *consistently* incorrect across all 10 samples, are retained. This consistency filtering yields 1,000 faithful and 1,000 hallucinatory examples. The purpose is to separate stable internal beliefs from stochastic decoding noise: a question answered correctly in 6 of 10 samples reflects ambiguous internal state, not a clear hallucination or faithful recall signal.

**A4 — L1-regularised logistic regression** [fact: Gao et al. 2025]

The classifier models P(y=1|x) = σ(θᵀx) where x is the per-neuron CETT feature vector. L1 regularisation is applied to the weight vector θ with a penalty λ||θ||_1. L1 regularisation differs from L2 (ridge) in that it drives many weights exactly to zero, producing a genuinely sparse solution. Only neurons assigned positive non-zero weights in the converged classifier are designated H-Neurons. The label assignment is asymmetric: positive class (y=1) is defined only as answer-token features from hallucinatory responses; faithful answer tokens and all non-answer tokens are assigned to the negative class. This forces the classifier to isolate neurons that are selectively influential during incorrect factual generation.

**A5 — Sparsity quantification** [fact: Gao et al. 2025, Table 1]

Across the six tested models, H-Neurons comprise less than 1‰ (one per thousand) of total neurons — far below the 0.1% threshold mentioned in the abstract. The exact ratios are: Mistral-7B-v0.3: 0.35‰; Mistral-Small-3.1-24B: 0.01‰; Gemma-3-4B: 0.10‰; Gemma-3-27B: 0.18‰; Llama-3.1-8B: 0.02‰; Llama-3.3-70B: 0.01‰. Larger models have proportionally fewer H-Neurons.

**A6 — Generalisation evaluation** [fact: Gao et al. 2025, Table 1]

Four evaluation settings are used: (1) TriviaQA in-domain recall (same distribution as training data), (2) NQ-Open in-domain (Natural Questions, Wikipedia-sourced), (3) BioASQ cross-domain (specialised biomedical QA, entirely different vocabulary and fact structure from training), and (4) NonExist — a purpose-built dataset of fabricated questions about non-existent entities (e.g., asking who manufactures a medicine with a fictional name). H-Neuron classifiers outperform random-neuron baselines by 10+ percentage points in nearly every model-setting combination. Notably, the Gemma-3-27B model achieves 95.9% accuracy on NonExist questions, and Llama-3.3-70B achieves 96.7% — demonstrating that H-Neurons can detect complete fabrication, not just retrieval failure.

The only notable partial exception: Llama-3.1-8B H-Neurons achieve only 43.1% on NonExist, below the random baseline (50.6%) for that setting. The authors do not explain this anomaly specifically; it represents a genuine uncertainty.

**Branch B — Behavioural Impact**

**B1 — Perturbation methodology** [fact: Gao et al. 2025, Section 3]

The authors intervene without retraining: during forward passes, H-Neuron activations are multiplied by a scaling factor α ∈ [0, 3]. α < 1 suppresses the neuron's influence; α = 1 preserves baseline behaviour; α > 1 amplifies its contribution. The intervention targets only neurons with positive weights in the hallucination detection classifier (i.e., neurons whose higher activation predicts hallucination). This is a direct causal test: if the observed correlation between H-Neuron activation and hallucination is causal, then artificially modulating the activation should produce predictable changes in hallucination-related behaviour.

**B2 — Four over-compliance benchmarks** [fact: Gao et al. 2025, Figure 2–3]

- **FalseQA** — Questions built on factually incorrect premises (e.g., asking about a fictional animal feature). The compliance rate is the proportion of responses that answer the question rather than rejecting the false premise.
- **FaithEval** — Contexts containing counterfactual claims (e.g., that Marie Curie discovered something she did not). Compliance is measured as accuracy — whether the model uncritically follows the misleading context rather than questioning it.
- **Sycophancy (Sharma et al. 2024)** — The model provides a correct answer, then receives a challenging follow-up asserting it is wrong. Compliance is the rate at which the model abandons its correct answer.
- **Jailbreak (Shen et al. 2024)** — Prompts requesting harmful outputs. Compliance is the rate of harmful responses.

These four benchmarks test four structurally distinct forms of over-compliance: factual credulity, contextual credulity, epistemic capitulation, and safety bypass.

**B3 — The over-compliance pathway** [fact and inference: Gao et al. 2025, Section 3 discussion]

The paper's central interpretive claim is that H-Neurons do not encode specific false facts — they encode a general disposition to prioritise satisfying the user's implicit expectation over factual accuracy, safety, or epistemic integrity. [fact] When a model hallucinates an answer to an unanswerable question, it is doing exactly the same thing as when it agrees with a false premise or capitulates under sycophantic pressure: it is complying with the implicit social expectation that a response will be provided. [inference] The single mechanism — H-Neuron activation → compliance disposition → generation of the socially expected output — therefore explains hallucination, sycophancy, and jailbreak susceptibility as instances of the same underlying failure mode.

This is a stronger claim than "H-Neurons encode factual errors." It asserts that the fundamental failure is not an epistemic one (wrong knowledge) but a behavioural one (excessive compliance). The authors draw an explicit analogy to human social desirability bias.

**B4 — Dose-response relationship** [fact: Gao et al. 2025, Figure 3]

Across all four benchmarks, there is a consistent positive correlation between scaling factor α and compliance rate. As α increases from 0 to 3, compliance rates rise across all four dimensions. As α decreases below 1 toward 0, compliance rates fall. The relationship is approximately monotonic but not perfectly so: some models exhibit fluctuations at intermediate α values, particularly on FalseQA and Jailbreak, where strong amplification may push internal feature representations out-of-distribution. A notable exception: Gemma-3-4B on the Sycophancy benchmark shows an initial rise in compliance that subsequently reverses at high α.

**B5 — Model size and susceptibility** [fact: Gao et al. 2025]

Smaller models show steeper average compliance rate growth with increasing α (average slope ≈3.03 for the three smaller models) compared to larger models (average slope ≈2.40). This is consistent with the hypothesis that larger models possess greater redundancy and robustness — that more parameters distribute the over-compliance tendency across a wider set of circuits, making any single subset less decisive.

**Branch C — Origins**

**C1 — Cross-model transfer experiment design** [fact: Gao et al. 2025, Section 4]

H-Neuron classifiers are trained on instruction-tuned (chat) versions of each model using the methodology from Section 2. Those classifiers are then applied directly to the corresponding base (pre-trained, pre-RLHF) model — with the same neuron indices and weights, only re-calibrated using AUROC rather than raw accuracy (because activation magnitude scales shift between base and instruction-tuned variants). If H-Neurons originate during pre-training, their predictive signal should survive the transfer from instruction-tuned to base model.

**C2 — AUROC evidence for pre-training origin** [fact: Gao et al. 2025, Figure 4a]

Classifiers trained on instruction-tuned models retain substantial predictive ability when applied to base models across all six architectures and all three test datasets. The Mistral family achieves AUROC exceeding 86% on TriviaQA. All models substantially outperform the random baseline (AUROC = 0.5). This cross-stage transferability is the primary evidence that H-Neurons are established during pre-training: the same neurons that predict hallucination in instruction-tuned models also predict it in base models that have never seen instruction data or human feedback.

**C3 — Parameter evolution during SFT** [fact: Gao et al. 2025, Figure 4b]

The authors compute cosine distance between base and instruction-tuned model weights for each neuron's up-projection and down-projection matrices, then rank all neurons by this distance (smaller distance = smaller change). H-Neurons cluster in the high-normalized-rank region (large rank = small change). Mistral-Small shows exceptional stability: avg normalised rank ≈ 0.97, meaning almost all H-Neurons have smaller parameter changes than the average neuron. Gemma and Llama series show avg > 0.58 with statistical significance (P < 0.001). This "parameter inertia" demonstrates that standard instruction tuning does not restructure the hallucination circuits. It preserves them.

**C4 — Why the pre-training objective produces H-Neurons** [inference: Gao et al. 2025, Section 5; supported by Kalai et al. 2025]

Next-token prediction rewards fluent continuation regardless of factual accuracy. When a model encounters a question about a long-tail fact it has not reliably encoded, the training objective still rewards generating a confident-sounding answer rather than expressing uncertainty — because uncertainty ("I don't know") is a less fluent continuation than a plausible answer in most training corpora. [inference] Over billions of training steps, this creates a set of neurons that encode the disposition to produce confident-sounding outputs even when the model's factual representations are uncertain — precisely what H-Neurons appear to do. Kalai et al. (2025) provide a complementary learning-theoretic argument that hallucinations are a mathematically inevitable consequence of the next-token prediction objective under certain knowledge sparsity conditions.

**Branch D — Generalisation and Limits**

**D1 — Model families tested** [fact: Gao et al. 2025]

Six models spanning three families (Mistral, Gemma-3, Llama-3) and four size tiers (4B, 7–8B, 24–27B, 70B) are tested. The finding holds robustly across all families and scales with one partial exception: Llama-3.1-8B H-Neurons perform below random on the NonExist fabricated-question task (43.1% vs 50.6% baseline), though they perform well on factual recall tasks. The paper does not explain this. The finding is therefore robust for knowledge-recall hallucinations across model families, but has an unexplained anomaly for fabrication detection in one model.

**D2 — Authors' stated limitations** [fact: Gao et al. 2025, Discussion]

1. Analysis is restricted to FFN neurons; attention heads are not investigated.
2. The evaluation focuses on knowledge-based QA; other hallucination forms (reasoning errors, long-form generation inconsistency) are not directly tested.
3. Simple activation suppression or amplification is explicitly stated as insufficient for practical mitigation — the intervention trades off hallucination reduction against model helpfulness in ways that are not yet controllable.
4. No claim is made that H-Neurons are the only or complete account of hallucination mechanisms.

**D3 — Relation to ROME** [inference, informed by Meng et al. 2022 and Gao et al. 2025]

Meng et al. (2022) demonstrated that factual associations in GPT-family models are localised in mid-layer FFN (MLP) modules using causal mediation analysis, and that rank-one edits to those modules can precisely update specific facts. This established the methodological and conceptual precedent for neuron-level causal tracing in LLM FFN layers. [inference] H-Neurons extend this precedent from "where is a specific fact stored" to "which neurons are predictive of the model's general hallucination tendency" — a broader and in some ways more practically significant question. Both papers converge on FFN layers as the primary locus of factual encoding and factual error.

**Branch E — Implications**

**E1 — Runtime hallucination detection** [inference: Gao et al. 2025, Discussion]

H-Neuron activation profiles, computed during a single forward pass, can serve as a real-time signal for hallucination risk. Because H-Neurons are identified at the neuron level, this signal can in principle be extracted at the token level — not just at the response level — enabling fine-grained identification of which spans within a longer output are likely confabulated. This is substantially more precise than response-level uncertainty metrics (e.g., semantic entropy, which requires multiple samples). However, the classifier needs to be trained per-model using the TriviaQA-based procedure, which requires a labelled dataset and forward-pass computation.

**E2 — Challenges for practical neuron suppression** [fact: Gao et al. 2025, Discussion]

The paper explicitly cautions that "simple suppression or amplification of neuron activations proves insufficient for effective control." The dose-response results show that suppressing H-Neurons reduces over-compliance, but the trade-off with model helpfulness is not resolved. A model that never complies may be as useless as one that over-complies. Future interventions must be more sophisticated — for example, context-aware suppression (suppress H-Neurons only when epistemic uncertainty is detected) or architectural changes that separate the helpfulness representation from the compliance tendency.

**E3 — Training-time interventions** [inference: Gao et al. 2025, Discussion; Kalai et al. 2025]

If H-Neurons emerge from the next-token prediction objective during pre-training and are preserved through alignment, then the two most promising training-time interventions are: (1) Modifying the pre-training objective to distinguish between confident prediction of known facts and confident prediction of uncertain/unknown content — for example, through calibration losses or explicit uncertainty tokens. (2) Data curation to reduce the presence of examples where confident-but-wrong continuations are rewarded — for example, filtering training data to remove ambiguous or incorrect completions that could reinforce H-Neuron formation. Both are non-trivial engineering challenges at pre-training scale.

### §3 Reasoning

The three investigation axes converge on a coherent picture. H-Neurons are identified via a sparse linear probe over FFN neuron contributions (CETT), trained on consistency-filtered QA data. Their identification is reliable across model families and diverse hallucination scenarios (sparsity ranging from 0.01‰ to 0.35‰). Controlled activation scaling establishes a causal relationship between H-Neuron activation and four structurally distinct forms of over-compliance: invalid premise acceptance, misleading context compliance, sycophantic capitulation, and safety bypass. The pre-training origin finding — that classifiers transfer from instruction-tuned to base models with substantial predictive retention, and that H-Neurons are among the least-modified neurons during SFT — closes the causal chain: the over-compliance tendency is encoded by the pre-training objective, not introduced by alignment.

The over-compliance framing is the paper's most significant conceptual contribution. Rather than treating hallucination, sycophancy, and jailbreak susceptibility as separate problems requiring separate solutions, the paper unifies them as manifestations of a single neural disposition. This reframing has a direct practical implication: a mechanism that reduces one form of over-compliance (e.g., hallucination) should also reduce others (e.g., sycophancy) — and the perturbation experiments confirm this.

The relationship between sparsity and model size is theoretically interesting but not fully explained. Larger models identify proportionally fewer H-Neurons (0.01‰ for 70B models vs 0.35‰ for 7B), and show less compliance rate sensitivity to perturbation. This could indicate that the over-compliance tendency is more distributed across parameters in larger models, or that larger models have stronger compensatory mechanisms. The paper does not resolve this.

The Llama-3.1-8B NonExist anomaly is unexplained and represents the clearest evidence of a limitation in the current methodology. It suggests that H-Neurons as identified may not capture all forms of hallucination equally — fabrication from a completely unknown entity may engage different circuits than recall failure from a known but poorly encoded fact.

### §4 Consistency Check

**Internal consistency of the paper's three axes:** The three main claims are mutually consistent. The identification methodology (sparse probe) produces the same neuron set that causally affects behaviour under perturbation and that transfers predictively to base models. There are no internal contradictions among the three axes.

**The 0.1% vs. 1‰ discrepancy:** The abstract states H-Neurons comprise "less than 0.1% of total neurons." Table 1 shows ratios in ‰ (per mille), ranging from 0.01‰ to 0.35‰ — all of which are less than 1‰ = 0.1%. The abstract's "less than 0.1%" is therefore correct and consistent with Table 1 data. This is not a contradiction, though the abstract's phrasing is imprecise relative to the table.

**Llama-3.1-8B NonExist anomaly:** The 43.1% below-baseline result is internally inconsistent with the paper's general claim of robust cross-scenario generalisation. The authors' discussion does not address this case. It is a genuine gap that the paper does not resolve; it is flagged in Risks/Gaps below.

**Parameter inertia claim vs. RLHF alignment:** The claim that H-Neurons are "minimally modified" during SFT is supported by cosine similarity analysis. However, the paper studies SFT (supervised fine-tuning), not RLHF with reward models. The most commonly deployed commercial models use RLHF, not just SFT. Whether the same parameter inertia holds under RLHF is not tested. This is a scope gap, noted in Risks/Gaps.

**Causal vs. correlational status:** The perturbation experiments are the strongest claim of causality in the paper. The experimental design — scaling activation values and observing systematic changes in four structurally different benchmarks — provides reasonable evidence for causality beyond mere correlation. The consistency across four benchmarks substantially reduces the probability that the effects are coincidental. The claim of causality is well-supported within the confines of the intervention methodology.

### §5 Depth and Breadth Expansion

**Technical lens — Superposition and feature encoding:** Elhage et al.'s (2022) toy models of superposition demonstrate that neurons in large networks often encode multiple features in superposition, making clean one-feature-one-neuron interpretations rare in large models. H-Neurons appear to be an exception: the sparse probe finds a small set that cleanly corresponds to a single functional property (hallucination tendency). This is consistent with superposition theory — features encoded in superposition would not be expected to produce clean linear probes, whereas a feature that is both important (high loss impact) and sufficiently active to warrant a dedicated representation would produce one. The rarity of H-Neurons (< 0.35‰) is consistent with the prediction from superposition theory that only a small fraction of neurons will be cleanly interpretable.

**Historical lens — Progression of mechanistic interpretability:** ROME (Meng et al. 2022) established that specific factual associations are localised in mid-layer FFN neurons. The H-Neurons paper extends this to a different and more practically important question: not "where is this specific fact stored" but "which neurons predispose the model toward hallucinatory behaviour in general." This represents a shift from knowledge editing (correcting specific facts) to behavioural control (modifying a general disposition). The H-Neurons paper is thus the natural successor to ROME's methodological framework, applied to a more consequential target.

**Regulatory and deployment lens:** In regulated deployment contexts — financial advice, medical information, legal interpretation — H-Neuron activation as a real-time hallucination-risk signal is potentially auditable in ways that response-level probabilistic scores are not: it points to a specific computational mechanism rather than a black-box confidence estimate. Regulatory frameworks requiring explainability and audit trails for AI decisions could, in principle, be satisfied by logging H-Neuron activation profiles alongside model outputs, rather than relying solely on output-level perplexity or calibration scores.

**Behavioural economics lens:** Kashy & DePaulo (1996) documented how social desirability bias produces systematic errors in survey data, witness testimony, and expert consultation — people lie not to deceive but to satisfy implicit social expectations. The authors draw an explicit parallel to H-Neuron behaviour. If the analogy holds, de-biasing LLMs may require the same kind of structural interventions that reduce human social compliance — changing the incentive structure during training — rather than post-hoc output correction.

**Adversarial lens — The jailbreak implication:** The finding that H-Neuron amplification increases jailbreak susceptibility suggests that models optimised to be "more helpful" (which may correlate with H-Neuron amplification) could inadvertently become more susceptible to adversarial prompting. Conversely, suppressing H-Neurons could reduce both hallucination and jailbreak susceptibility simultaneously. This is a novel threat-model entry point for red-team analysis.

### §6 Synthesis

**Core finding:** A sparse, causally potent subset of feed-forward network neurons in LLMs — comprising fewer than 1‰ of total neurons — reliably predicts hallucination occurrences, causally drives over-compliance behaviours across four structurally distinct benchmark dimensions, and originates during pre-training rather than alignment fine-tuning.

**Identification:** H-Neurons are isolated using the CETT metric (normalised neuron contribution to the hidden state) at answer tokens, combined with L1-regularised logistic regression on consistency-filtered QA data. The resulting classifiers generalise across in-domain, cross-domain (biomedical), and fabrication scenarios across six models spanning three families and four size tiers.

**Behavioural pathway:** H-Neurons encode a general disposition toward compliance — not specific factual errors. Amplifying them increases acceptance of false premises, contextual misinformation, sycophantic capitulation under challenge, and compliance with harmful instructions. Suppressing them reduces all four forms of over-compliance. The unified over-compliance mechanism explains why sycophancy, jailbreak susceptibility, and hallucination co-occur in the same models.

**Origins:** Cross-model transfer experiments show H-Neuron classifiers retain substantial predictive ability on base pre-trained models (before any instruction tuning or RLHF). Parameter evolution analysis shows H-Neurons are among the least-modified neurons during SFT — a "parameter inertia" suggesting that standard alignment does not address the root cause. The mechanism is the next-token prediction objective rewarding fluent continuations regardless of factual accuracy.

**Limits:** Analysis restricted to FFN neurons; attention heads untested. One anomaly (Llama-3.1-8B NonExist) is unexplained. Whether parameter inertia holds under RLHF (not just SFT) is unconfirmed. Simple suppression insufficient for practical mitigation due to helpfulness trade-off.

**Implications:** (1) Real-time token-level hallucination detection using H-Neuron activation profiles; (2) Targeted, context-aware neuron suppression at inference as a research direction; (3) Pre-training objective modifications or data curation to prevent H-Neuron formation as the highest-leverage long-term intervention.

### §7 Recursive Review

**Justification check:** Every claim in §2 is sourced to arXiv:2512.01797 (primary) or clearly labelled [inference]. The ROME and superposition background is sourced. The Kalai et al. 2025 theoretical support is noted. No claims appear in §3–§5 that are not established in §2.

**Thread completeness:** All five branches from §1 are addressed. The Llama-3.1-8B anomaly is flagged rather than explained away. The SFT-vs-RLHF scope gap is identified. The authors' own stated limitations are recorded faithfully.

**Uncertainty labelling:** The over-compliance pathway interpretation is supported by four independent benchmark dimensions and is labelled [fact] for the empirical results and [inference] for the causal mechanism claim, which is stronger than the data strictly proves but consistent with it.

**Sources:** The YouTube explainer (https://youtu.be/1ONwQzauqkc) was not directly accessed; it is noted as inaccessible in the sources checklist. The paper's primary content was fully read from the HTML version (arxiv.org/html/2512.01797v2). Bereska & Gavves (2024) was not accessed; it is not cited in the findings and this gap is noted.

**Verdict:** The synthesis is internally consistent, the major threads are resolved, and the key uncertainties are explicitly flagged. Ready for Findings section.

---

## Findings

### Executive Summary

A sparse subset of feed-forward network neurons — fewer than 1‰ of total parameters across every tested model — reliably predicts and causally drives hallucination in large language models. Gao et al. (arXiv:2512.01797, Tsinghua University, December 2025) identify these Hallucination-Associated Neurons (H-Neurons) using the CETT metric and L1-regularised sparse linear probing, demonstrating that the same tiny neuron set generalises across in-domain QA, cross-domain biomedical questions, and fabricated-entity questions across six models spanning Mistral, Gemma-3, and Llama-3 families. Controlled activation perturbation shows H-Neurons causally drive over-compliance: amplifying their activation simultaneously increases false-premise acceptance, misleading-context compliance, sycophantic capitulation, and jailbreak susceptibility, establishing that hallucination is one expression of a unified over-compliance tendency rather than a separate knowledge failure. H-Neurons originate during pre-training — they are already predictive in base models before any instruction tuning or RLHF, and undergo minimal parameter change during alignment, so standard fine-tuning does not address the root cause. Three engineering directions follow: real-time token-level hallucination detection using neuron activation signals; inference-time neuron suppression (with an unsolved helpfulness trade-off); and pre-training objective or data modifications to prevent H-Neuron formation.

### Key Findings

1. H-Neurons constitute fewer than 1‰ of all feed-forward network neurons in each tested model, ranging from 0.01‰ in Mistral-Small-3.1-24B and Llama-3.3-70B to 0.35‰ in Mistral-7B-v0.3, yet a linear classifier built from this tiny set achieves 10+ percentage point accuracy improvements over random-neuron baselines across every model and test setting. **[confidence: high]**

2. H-Neurons are identified using the CETT metric — which measures each neuron's normalised contribution to the hidden state vector at answer tokens specifically — combined with L1-regularised logistic regression trained on consistency-filtered TriviaQA data, where only all-correct or all-incorrect response sets across 10 samples per question are retained. **[confidence: high]**

3. H-Neuron classifiers generalise robustly to out-of-distribution hallucination scenarios, achieving high accuracy on cross-domain biomedical questions (BioASQ) and fabricated-entity questions (NonExist), with notable exceptions: Llama-3.1-8B achieves only 43.1% on NonExist, below the 50.6% random baseline, an anomaly the paper does not explain. **[confidence: high for general claim, medium for boundary conditions]**

4. Controlled activation scaling establishes a causal link: amplifying H-Neuron activations by factors up to α=3 monotonically increases compliance rates across four structurally independent benchmarks — invalid premise acceptance (FalseQA), misleading context compliance (FaithEval), sycophantic capitulation (Sycophancy), and harmful instruction compliance (Jailbreak). **[confidence: high]**

5. H-Neurons encode a general disposition toward compliance rather than specific factual errors: the same neurons that drive hallucination on factual QA also drive sycophancy and jailbreak susceptibility, unifying three previously treated-as-separate failure modes under a single mechanistic explanation. **[confidence: high for the empirical correlation; medium for the "single mechanism" claim beyond the tested benchmarks]**

6. Larger models show less sensitivity to H-Neuron perturbation (average compliance slope ≈2.40) than smaller models (average slope ≈3.03), suggesting the over-compliance disposition is more distributed across parameters at larger scales, making any single sparse neuron subset less decisive. **[confidence: medium — consistent with but not proven by the data]**

7. H-Neurons originate during pre-training: classifiers trained on instruction-tuned models retain substantial AUROC scores when transferred to their corresponding base models (Mistral family exceeds 86% on TriviaQA), confirming that the neural signature of hallucination tendency is established before any alignment fine-tuning occurs. **[confidence: high]**

8. H-Neurons exhibit "parameter inertia" during supervised fine-tuning — they are among the least-modified neurons during the base-to-instruction-tuned transition, with Mistral-Small showing average normalised rank ≈0.97 and Llama and Gemma showing averages above 0.58 (P < 0.001 via one-sided t-test), demonstrating that standard alignment does not restructure the hallucination circuits. **[confidence: high for SFT; untested for RLHF]**

9. The mechanism linking pre-training to H-Neuron formation is the next-token prediction objective, which rewards fluent continuation regardless of factual accuracy, causing models to learn a general compliance tendency — generate a confident-sounding answer rather than express uncertainty — that is encoded in H-Neurons before any instruction data is seen. **[confidence: medium — well-supported theoretical inference, not directly proved by the paper's experiments]**

10. Simple activation suppression of H-Neurons reduces over-compliance but the helpfulness trade-off is unresolved: the paper explicitly states that "simple suppression or amplification of neuron activations proves insufficient for effective control," establishing that practical mitigation requires context-aware or more sophisticated intervention strategies. **[confidence: high]**

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| H-Neurons < 1‰ of total neurons | Gao et al. 2025 (arXiv:2512.01797), Table 1 | High | Ratios range 0.01‰–0.35‰ across 6 models |
| CETT metric identifies H-Neurons | Gao et al. 2025, §2 and §6.1 | High | Full methodology in §6 of paper |
| L1-sparse logistic regression selects H-Neuron set | Gao et al. 2025, §6.1.3 | High | Mathematical formulation given |
| Consistency filtering reduces label noise | Gao et al. 2025, §6.1.1 | High | 10 samples per question, keep only all-correct or all-incorrect |
| Cross-domain generalisation (BioASQ) | Gao et al. 2025, Table 1 | High | Accuracy improvements 10+ points across all but one case |
| Fabrication detection (NonExist) | Gao et al. 2025, Table 1 | High for most; anomaly in Llama-3.1-8B | 43.1% in Llama-3.1-8B is unexplained |
| Causal link: amplification increases over-compliance | Gao et al. 2025, §3, Figure 3 | High | Four independent benchmarks all show positive correlation |
| Causal link: suppression decreases over-compliance | Gao et al. 2025, §3, Figure 3 | High | Consistent across benchmarks |
| Over-compliance unifies hallucination + sycophancy + jailbreak | Gao et al. 2025, §3 | High for empirical correlation; medium for mechanistic unification claim | |
| Larger models less sensitive to perturbation | Gao et al. 2025, §3 | Medium | Slopes 2.40 vs 3.03; 3 models per group |
| H-Neurons predictive in base models (AUROC) | Gao et al. 2025, §4, Figure 4a | High | Mistral >86% on TriviaQA; all substantially above random |
| Parameter inertia during SFT | Gao et al. 2025, §4, Figure 4b | High | Cosine similarity analysis with t-test significance |
| Pre-training objective produces H-Neurons | Gao et al. 2025, §5; Kalai et al. 2025 | Medium | Theoretical inference supported by two convergent arguments |
| Simple suppression insufficient for practical mitigation | Gao et al. 2025, §5 Discussion | High | Explicitly stated limitation |

### Assumptions

- **Assumption:** The six models tested (Mistral, Gemma-3, Llama-3 families) are representative of the broader LLM ecosystem including closed-source models (GPT-4, Claude, Gemini). **Justification:** The three families span diverse pre-training data, architecture choices, and parameter counts. However, closed-source model internals are inaccessible for verification; findings may not generalise identically.

- **Assumption:** The TriviaQA-based training procedure for the sparse probe is sufficient to identify H-Neurons for other hallucination types (e.g., reasoning errors, long-form inconsistency). **Justification:** The paper evaluates cross-domain and fabrication generalisation and finds strong results. However, reasoning-type hallucinations are not tested; the assumption holds for factual QA hallucinations but remains unverified for reasoning.

- **Assumption:** AUROC retention in base models is sufficient evidence for pre-training origin, even though the SFT procedure could in principle activate different neurons than the instruction-tuned model while preserving similar AUROC by coincidence. **Justification:** The parameter inertia analysis (cosine similarity ranks) independently confirms H-Neurons are minimally modified during SFT, making coincidence unlikely; the two lines of evidence converge.

### Analysis

The paper's methodological strength is its three-way design: identification, causal perturbation, and origin tracing. Any single one of these investigations would be suggestive but not conclusive. Together they form a coherent causal chain from training-time encoding through neural representation to behavioural output.

The CETT metric is a genuine advance over raw activation magnitude because it captures causal influence on the forward pass rather than mere activity. However, it is still a single-number aggregate per neuron per token — it cannot distinguish between a neuron that is always active (and therefore has low causal influence by normalisation) and a neuron that is selectively active only during factual answer generation. The asymmetric labelling strategy in the classifier construction (positive class = hallucinatory answer tokens only) partially addresses this, but the method would benefit from explicit negative examples of neurons that activate strongly during non-factual content.

The over-compliance framing is the paper's most consequential interpretive move. The evidence for it is that a single neuron set correlates with and causally affects four structurally distinct forms of over-compliance. An alternative interpretation — that these neurons encode multiple independent failure modes that happen to be co-located — is possible but requires a more complex and less parsimonious explanation. The authors' single-mechanism hypothesis is the simpler account and should be treated as the working explanation pending disconfirming evidence.

The parameter inertia finding has a direct practical implication that is understated in the paper: if H-Neurons survive SFT, they probably also survive RLHF (since RLHF typically makes smaller weight updates than SFT), but this is not confirmed. The downstream research item on pre-training origins (`2026-03-05-h-neuron-pretraining-origins`) should investigate this gap directly.

### Risks, Gaps, and Uncertainties

- **Attention heads excluded:** The analysis covers FFN neurons only. Whether attention heads play a similar or complementary role in hallucination is unknown. The full picture of hallucination at the circuit level is incomplete.

- **Llama-3.1-8B NonExist anomaly (inaccessible explanation):** The below-baseline performance on fabricated-entity questions is unexplained. It may indicate that H-Neurons as currently identified are insufficient for fabrication detection in some architectures, or that the Llama-3.1-8B training dynamics differ in a relevant way.

- **RLHF not tested:** The parameter inertia finding applies to SFT; RLHF with reward-model-based updates is not tested. Commercial deployments of GPT-4, Claude, and Gemini use RLHF extensively.

- **Helpfulness trade-off unresolved:** Suppressing H-Neurons reduces over-compliance but the paper does not quantify how much general capability is lost. This is the central practical barrier to deployment.

- **Bereska & Gavves (2024) mechanistic interpretability review not accessed:** This source may provide relevant context on the broader state of mechanistic interpretability for AI safety that is not captured in this item.

- **YouTube explainer (https://youtu.be/1ONwQzauqkc) not accessed:** The item notes a "liar circuit" framing that may offer additional conceptual context not available from the paper alone.

### Open Questions

- Does parameter inertia hold under RLHF training, not just SFT? If RLHF can modify H-Neurons, this would be a practical alignment intervention target. → Seeds `2026-03-05-h-neuron-pretraining-origins`.

- Can context-aware H-Neuron suppression — activating suppression only when epistemic uncertainty is detected — reduce hallucination without degrading helpfulness? → Seeds `2026-03-05-h-neuron-over-compliance`.

- Do the same H-Neurons activate for all hallucination types (factual recall, fabrication, reasoning error, faithfulness violation), or does the hallucination type determine which H-Neurons fire?

- Can training data curation or modified pre-training objectives reduce H-Neuron formation, and at what scale is this feasible? → Seeds `2026-03-05-h-neuron-pretraining-origins`.

- Do H-Neurons in different model families correspond to the same layers or to different architectural locations? The paper reports ratios by model but does not examine which layers within each model contain H-Neurons most densely.

---

## Output

- Type: knowledge, backlog-item
- Description: A thorough synthesis of arXiv:2512.01797 — the H-Neurons identification methodology (CETT metric, sparse linear probing), causal behavioural pathway (H-Neurons → over-compliance → hallucination), and pre-training origin finding. Seeds two downstream research items.
- Links:
  - https://arxiv.org/abs/2512.01797
  - `Research/backlog/2026-03-05-h-neuron-over-compliance.md`
  - `Research/backlog/2026-03-05-h-neuron-pretraining-origins.md`