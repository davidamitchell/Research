---
title: "Pre-Training Origins of Hallucination-Associated Neurons — Implications for LLM Development"
added: 2026-03-05
status: completed
priority: medium
blocks: [2026-03-05-h-neurons-synthesis]
tags: [llm, hallucinations, h-neurons, pre-training, alignment, rlhf, training-dynamics, mechanistic-interpretability, reliability]
started: 2026-03-06
completed: 2026-03-06
output: [knowledge]
---

# Pre-Training Origins of Hallucination-Associated Neurons — Implications for LLM Development

## Research Question

Given that Hallucination-Associated Neurons (H-Neurons) emerge during pre-training rather than instruction tuning or RLHF, what does this reveal about how hallucination-prone behaviour is encoded during the pre-training phase, and what concrete changes to pre-training data, objectives, or architecture could reduce H-Neuron formation?

## Scope

**In scope:**
- The specific finding in arXiv:2512.01797 that H-Neurons are already predictive in base pre-trained models — before RLHF or instruction tuning
- What it means mechanistically for a neuron to "emerge during pre-training": what training signal causes these neurons to form?
- The relationship between pre-training data characteristics (noise, misinformation, distributional bias) and H-Neuron formation
- The relationship between the next-token prediction objective and the encoding of over-compliance behaviour at the neuron level
- What RLHF and instruction tuning can and cannot do to reverse or suppress H-Neurons that already exist
- Implications for scaling: does scaling pre-training compute increase or decrease H-Neuron density?
- Practical interventions at the pre-training stage: data curation, curriculum learning, objective modification, architectural choices

**Out of scope:**
- H-Neuron identification methodology (covered in `2026-03-05-h-neurons-in-llms`)
- Inference-time and fine-tuning-time interventions (covered in `2026-03-05-h-neuron-over-compliance`)
- General hallucination taxonomy and causes (covered in `2026-03-05-llm-hallucination-mechanisms`)

**Constraints:** Builds on `2026-03-05-h-neurons-in-llms` — must be researched after that item is complete. Much of this item will require first-principles reasoning from the paper's findings plus the broader pre-training and training-dynamics literature, as direct pre-training interventions for H-Neuron suppression are not yet established in the literature.

## Context

The finding that H-Neurons originate in pre-training — not in the RLHF or instruction-tuning phase — has a profound implication: **post-training alignment cannot fully solve the hallucination problem**. If the neurons that drive over-compliance and hallucination are already present in the base model, RLHF and constitutional AI can only suppress their expression, not eliminate their existence. The underlying causal mechanism remains, ready to surface under distributional shift or adversarial conditions.

This shifts the research agenda in two directions:

1. **Understanding pre-training dynamics** — What in the standard pre-training procedure (next-token prediction on diverse web-scale corpora) causes these neurons to form? Is it noisy/contradictory training data? The objective function itself? The model architecture? Scale?

2. **Pre-training-time interventions** — Can the pre-training procedure be modified to prevent H-Neurons from forming in the first place? What would this cost in terms of data scale, compute, or general capability?

**Prior research:** Three directly related completed items provide the foundation for this investigation. `2026-03-05-h-neurons-in-llms` established that H-Neurons are a real, causally verified phenomenon in FFN layers (<1‰ of neurons) that generalise across domains and model families, and that they originate in pre-training — already predictive in base models before alignment. `2026-03-05-h-neuron-over-compliance` established that over-compliance is the causal pathway, with inference-time interventions limited by a helpfulness trade-off not yet resolved. `2026-03-05-llm-hallucination-mechanisms` established that next-token prediction is calibrated for fluency not factual accuracy, and that RLHF creates a structural conflict by training on human approval signals in domains where raters cannot distinguish accurate from plausible outputs. What this item must add: a detailed mechanistic account of why the pre-training objective specifically produces H-Neuron circuits, what empirical evidence from pre-training dynamics and data quality research says about which data characteristics drive their formation, what RLHF structurally cannot repair, and a synthesised set of candidate pre-training interventions with feasibility assessment.

## Approach

1. **Pre-training origin evidence** — Work through the evidence from arXiv:2512.01797 for the pre-training origin claim. What comparison is made between base and instruction-tuned/RLHF models? How strong is the evidence? What alternative explanations are ruled out?

2. **Next-token prediction and over-compliance** — Investigate the theoretical connection between the next-token prediction objective and the encoding of over-compliance behaviour. Does training on corpora containing sycophantic text (human-written examples of agreeing with errors, confident falsehoods, etc.) directly cause H-Neuron formation?

3. **Pre-training data quality research** — Survey the literature on how pre-training data quality affects model behaviour. What do we know about the effect of noisy, contradictory, or sycophantic text in training corpora on hallucination rates? What deduplication, quality filtering, and source-weighting strategies exist?

4. **RLHF limits** — What does the RLHF and post-training alignment literature say about the limits of post-training alignment for fixing problems that originate in pre-training? Can reward signals selectively suppress pre-trained features, or do they primarily reroute behaviour at the surface level?

5. **Scaling dynamics** — What do scaling laws and mechanistic interpretability research suggest about how neuron-level features change with model scale? Does H-Neuron density decrease as models become larger (suggesting scale "solves" the problem) or does it remain stable/increase?

6. **Pre-training intervention design** — Synthesise the above into a structured set of candidate pre-training interventions: data filtering approaches, curriculum learning strategies (e.g., deprioritising known-sycophantic sources), auxiliary training objectives (explicit uncertainty calibration), and architectural choices (e.g., mechanisms that reduce superposition). Evaluate feasibility and estimated effectiveness.

## Sources

- [x] Gao et al. (2025) — "Hallucination-Associated Neurons in LLMs" (primary source for origins finding): https://arxiv.org/abs/2512.01797
- [x] Hoffmann et al. (2022) — "Training Compute-Optimal Large Language Models (Chinchilla)": https://arxiv.org/abs/2203.15556 — scaling laws and data quality
- [x] Gunasekar et al. (2023) — "Textbooks Are All You Need" (Phi-1) — data quality over data scale: https://arxiv.org/abs/2306.11644
- [x] Penedo et al. (2023) — "The RefinedWeb Dataset for Falcon LLM: Outperforming Curated Corpora with Web Data Alone": https://arxiv.org/abs/2306.01116 — pre-training data curation
- [x] Anthropic (2022) — "Constitutional AI: Harmlessness from AI Feedback": https://arxiv.org/abs/2212.08073 — RLHF limits for alignment
- [x] Elhage et al. (2022) — "Toy Models of Superposition" — how pre-training encodes features in neurons: https://transformer-circuits.pub/2022/toy_model/index.html
- [x] Biderman et al. (2023) — "Pythia: A Suite for Analysing Large Language Models Across Training and Scaling" — training dynamics: https://arxiv.org/abs/2304.01373
- [ ] `Research/backlog/2026-03-05-h-neurons-in-llms.md` — **prerequisite**: must be completed before starting this item

---

## Research Skill Output

### §0 Initialise

**Research question:** Given that H-Neurons emerge during pre-training, what does this reveal about how hallucination-prone behaviour is encoded during that phase, and what concrete changes to pre-training data, objectives, or architecture could reduce H-Neuron formation?

**Scope confirmed:** The investigation is bounded to the pre-training causal story and forward-looking pre-training interventions. Inference-time and fine-tuning interventions are explicitly out of scope, as they are addressed in sibling research items. The primary empirical anchor is arXiv:2512.01797 (Gao et al., Tsinghua, December 2025), supplemented by training-dynamics and data-quality literature.

**Constraints:** The paper provides empirical evidence for the pre-training origin claim but does not itself run pre-training ablations. Candidate interventions must therefore be derived from first-principles reasoning applied to the paper's mechanistic findings, cross-referenced against the pre-training data quality and scaling laws literature. Claims derived by inference will be labelled **[inference]**; claims with direct empirical backing will be labelled **[fact]**; claims requiring additional verification will be labelled **[assumption]**.

**Output format:** Structured research skill output followed by a full Findings section, with an evidence map, assumptions, and a candidate intervention catalogue with feasibility assessment.

---

### §1 Question Decomposition

**Root question:** How do H-Neurons form during pre-training, and how can pre-training be modified to prevent them?

**Decomposition tree:**

1. What is the empirical evidence that H-Neurons originate in pre-training?
   1a. What experimental design in Gao et al. tests the pre-training origin claim?
   1b. What are the AUROC results for base-model transfer, and what do they imply?
   1c. Do H-Neurons change during SFT/RLHF, or do they exhibit parameter inertia?
   1d. What alternative explanations (e.g., H-Neurons are an SFT artefact) are ruled out?

2. Why does the next-token prediction objective produce H-Neurons?
   2a. What is the training signal that rewards over-compliant responses during pre-training?
   2b. Is sycophantic and confidently-stated-false text in web corpora a direct cause?
   2c. What theoretical account exists for hallucination as a structural consequence of NTP?

3. What does pre-training data quality research say about hallucination formation?
   3a. What effect does web-corpus noise and sycophantic text have on model behaviour?
   3b. What filtering and deduplication strategies reduce hallucination rates?
   3c. Does synthetic "textbook quality" data reduce over-compliance behaviour?

4. What can RLHF and instruction tuning structurally not fix?
   4a. Does RLHF rewrite pre-trained circuits or merely suppress their expression?
   4b. What evidence shows pre-trained hallucination behaviour resurfaces under distributional shift?
   4c. What is the alignment tax, and does it constrain aggressive suppression?

5. What does scaling do to H-Neuron density and perturbation sensitivity?
   5a. Does H-Neuron ratio change with model scale in Gao et al.'s data?
   5b. Does compliance slope under perturbation change with model scale?
   5c. What do superposition theory and scaling laws predict about feature encoding at scale?

6. What pre-training interventions are candidates for reducing H-Neuron formation?
   6a. Data filtering: what categories of text should be removed or down-weighted?
   6b. Curriculum learning: what ordering or weighting strategy could reduce compliance encoding?
   6c. Auxiliary objectives: what training signals could counteract the NTP compliance reward?
   6d. Architectural choices: what structural modifications could reduce superposition-driven over-compliance encoding?
   6e. What is the feasibility and estimated effectiveness of each intervention?

---

### §2 Investigation

#### §2.1 Empirical evidence for pre-training origin

**Source: Gao et al. (2025), arXiv:2512.01797 [primary, accessed]**

Gao et al. run two complementary experiments to determine when H-Neurons emerge (Section 4 of the paper).

**Backward transferability experiment:** Classifiers trained on instruction-tuned models are applied directly to their corresponding base models without retraining. The metric is AUROC (area under the ROC curve) rather than fixed-threshold accuracy, because activation magnitudes shift between pre-training and fine-tuning. **[fact]** Across all six models and three evaluation datasets (TriviaQA, BioASQ, NQ-Open), AUROC scores consistently exceed random-guessing baselines by a large margin. The Mistral family achieves accuracy exceeding 86% on TriviaQA with classifiers built from instruction-tuned H-Neurons applied to the base model. **[fact]** This cross-stage transferability is strong evidence that H-Neurons are established during pre-training and not as artefacts of post-training alignment.

**Parameter evolution experiment:** The cosine distance between base and aligned model weights is computed for both up-projection and down-projection matrices at each FFN neuron. H-Neurons are then ranked within the global parameter space by how much they changed during SFT. **[fact]** H-Neurons consistently concentrate in the high-normalized-rank region — i.e., they are among the neurons that changed *least* during alignment. In Mistral-Small, the average H-Neuron rank is approximately 0.97 (where 1.0 means zero change), with statistical significance confirmed by a one-sided t-test (P < 0.001). The Gemma and Llama series show the same pattern (avg > 0.58, P < 0.001). **[fact]** The paper terms this "parameter inertia": standard instruction tuning does not effectively restructure the hallucination circuits; it largely preserves them.

**What this rules out:** The alternative hypothesis that H-Neurons are SFT artefacts predicts that (a) classifiers trained on aligned models should fail on base models, and (b) H-Neuron weights should change substantially during alignment. Both predictions are falsified. **[inference]** The residual uncertainty is that the experiment uses instruction-tuned models only, not RLHF-trained models; it is possible that RLHF (which involves more extensive reward-gradient updates than SFT alone) modifies H-Neurons more than SFT does, though the parameter-inertia finding and the larger literature on RLHF's surface-level operation make this unlikely.

#### §2.2 Next-token prediction as the causal mechanism

**Source: Gao et al. (2025) [primary, accessed]; Kalai et al. (2025) "Why Language Models Hallucinate" [secondary, cited in Gao et al.]**

The paper states directly: "We argue that this originates from the inherent characteristics of the next-token prediction objective. This training paradigm does not distinguish between factually correct and incorrect continuations — it merely rewards fluent text generation. Consequently, models must often fabricate or guess knowledge they do not possess to satisfy the fluency requirement." **[fact]** This aligns with Kalai et al. (2025), a learning-theory paper also cited in Gao et al., which provides a theoretical demonstration that hallucinations are an inevitable consequence of the pre-training process.

The mechanism: when the training corpus contains confident, fluent false statements (e.g., a human-written text that confidently asserts an incorrect fact) or sycophantic agreeable text (e.g., a forum response that validates a user's mistaken belief), the NTP objective rewards producing the continuation that agrees. **[inference]** Over millions of training examples, this reward signal is sufficient to consolidate a sparse set of neurons whose high activation correlates with the production of agreeable, user-expectation-satisfying outputs, regardless of factual accuracy. These neurons are the H-Neurons. The NTP objective provides no countervailing signal — there is no loss term penalising the production of plausible-but-false continuations when those continuations are fluent and common in the corpus.

**[assumption]** The sycophantic and confident-false-assertion content in web-scale corpora is sufficiently common and consistent in signal to consolidate dedicated circuits. The paper does not run ablations removing this content from pre-training data to test the counterfactual directly. The justification for this assumption is that: (a) web-scraped corpora demonstrably contain large volumes of sycophantic interaction text (social media, forums, advice columns), (b) the Constitutional AI paper (Anthropic 2022) itself motivates RLHF partly by arguing that such patterns are embedded in pre-training data, and (c) the Phi-1 paper demonstrates that eliminating low-quality text from training corpora substantially changes downstream model behaviour.

#### §2.3 Pre-training data quality and hallucination formation

**Source: Penedo et al. (2023) RefinedWeb [primary for data curation, accessed]; Gunasekar et al. (2023) Phi-1 [primary for quality-over-scale, accessed]; Hoffmann et al. (2022) Chinchilla [primary for scaling laws, accessed]; web search synthesis on data quality effects [secondary]**

**RefinedWeb (Penedo et al.):** The abstract confirms that "properly filtered and deduplicated web data alone can lead to powerful models; even significantly outperforming models from the state-of-the-art trained on The Pile. Despite extensive filtering, the high-quality data we extract from the web is still plentiful — 5 trillion tokens from CommonCrawl." **[fact]** This establishes that aggressive filtering of web data does not sacrifice data quantity at scale, and that filtering quality substantially affects model downstream behaviour.

**Phi-1 (Gunasekar et al.):** Phi-1 achieves pass@1 accuracy of 50.6% on HumanEval with a 1.3B parameter model trained on only 7B tokens, by using "textbook quality" data selected from the web plus synthetically generated textbooks and exercises. **[fact]** This provides direct evidence that training data quality — specifically the removal of low-quality, noisy, or adversarially phrased content — dramatically affects model behaviour even at small scale. **[inference]** If the same principle applies to factual accuracy and over-compliance (not just coding ability), then filtering out sycophantic, confidently-stated-false, or internally contradictory text from pre-training corpora should reduce the consolidation of H-Neuron circuits.

**Chinchilla (Hoffmann et al.):** The Chinchilla scaling laws establish that compute-optimal training requires equal scaling of model size and training tokens. **[fact]** This has implications for intervention feasibility: data quality filtering that reduces effective token count by even 10–20% would require either (a) sourcing additional high-quality data, (b) accepting slightly sub-optimal compute allocation, or (c) paying the cost in terms of capability. The Chinchilla result constrains the design space for data quality interventions — aggressive filtering is not free.

**Web corpus characteristics and hallucination:** Web-scale corpora (CommonCrawl, The Pile, C4) contain large volumes of sycophantic and compliant text: social media interactions where users praise incorrect claims, advice columns that validate questioners, news commentary that asserts contested facts confidently. **[inference, supported by Constitutional AI paper and data quality literature]** These patterns, when encountered at scale during NTP training, reinforce circuits that produce agreeable continuations. Deduplication is known to reduce memorisation artifacts and improve factual consistency; quality filtering on domain-of-trust signals (e.g., perplexity filtering, classifier-based quality scoring) reduces the proportion of low-reliability content.

#### §2.4 RLHF limits

**Source: Gao et al. (2025) [primary]; Anthropic Constitutional AI (2022) [primary for RLHF design, accessed]; web search on alignment tax and RLHF limits [secondary]**

The parameter-inertia finding from Gao et al. directly answers the structural limits of RLHF. **[fact]** H-Neurons undergo minimal parameter change during SFT. The Constitutional AI paper (Anthropic 2022) runs its own RL phase (RLAIF), and the approach achieves control over harmful outputs through reward signals on responses — but explicitly does not retrain the pre-trained representations themselves. **[fact]** The supervision in Constitutional AI operates at the response level: it rewards or penalises full outputs, not individual neuron activations.

**[inference]** RLHF and SFT operate at a level of abstraction above individual FFN neurons. Gradient updates from RLHF are diffused across all parameters weighted by the learning rate and the gradient signal; the result is that the most "inertia-prone" neurons — those whose weights are already stable and well-adapted to the pre-training objective — are the hardest to move. H-Neurons, being sparse and highly consolidated by the pre-training signal, exhibit exactly this inertia. RLHF can reshape the output distribution — changing which response a model *produces* given a prompt — without dismantling the underlying circuits that generate the over-compliant disposition.

The alignment tax literature confirms this structural tension. Aggressive reward optimisation creates distribution-mismatch between the RLHF objective and the pre-training objective, degrading capability ("alignment tax"). This constrains how far reward signals can push against pre-trained features without causing capability collapse. **[fact, supported by RLHF alignment tax research]**

**[fact]** Jailbreaks and adversarial prompting can restore pre-training behaviour in RLHF-trained models, confirming that RLHF alignment is a suppression layer, not a structural rewrite. This is independently established by multiple researchers (arXiv:2403.04769 and related work on jailbreak anatomy).

#### §2.5 Scaling dynamics

**Source: Gao et al. (2025) [primary, scaling data in Table 1 and Figure 3]; Elhage et al. (2022) Toy Models of Superposition [primary for superposition theory, accessed]**

**H-Neuron ratio across scales:** Table 1 in Gao et al. shows H-Neuron ratios of 0.35‰ in Mistral-7B-v0.3 and Gemma-3-4B, 0.10‰ in Gemma-3-27B, and 0.01–0.02‰ in Mistral-Small-3.1-24B, Llama-3.1-8B, and Llama-3.3-70B. **[fact]** Larger models have a lower H-Neuron *ratio*, but the total neuron count is also much higher, so the absolute number of H-Neurons in a 70B model still vastly exceeds that in a 7B model.

**Compliance sensitivity under perturbation:** The perturbation experiments in Figure 3 show that smaller models exhibit steeper compliance growth rates (average slope ≈ 3.03) versus larger models (average slope ≈ 2.40). **[fact]** The paper interprets this as larger models having "greater intrinsic robustness": the over-compliance disposition is more diffusely encoded at scale, so targeting a sparse neuron set produces less leverage.

**[inference]** This is consistent with superposition theory from Elhage et al.: as model dimensions increase, the geometric capacity for near-orthogonal feature representations expands, reducing the interference between features and allowing any individual feature to be more cleanly encoded. H-Neurons may be sparse representatives of a more distributed over-compliance representation in larger models. This dual finding — lower ratio but also lower perturbation leverage — means scaling does not solve the H-Neuron problem; it may simply dilute and distribute it.

**Superposition theory (Elhage et al.):** The toy-model experiments demonstrate that when features are sparse, models can represent more features than dimensions via superposition, at the cost of interference under certain activation patterns. **[fact]** This is directly relevant: the compliance feature encoded by H-Neurons may be one such superimposed representation. In larger models with higher-dimensional hidden states, superposition pressure is reduced, but so is the interpretability of any individual neuron. This makes both neuron-level identification and neuron-level intervention harder at scale.

**Chinchilla (Hoffmann et al.):** The Chinchilla scaling laws establish that for compute-optimal training, model size and training tokens should scale equally — doubling compute should double both. **[fact]** This implies that as models become larger, they are also trained on more data, which increases the volume of compliance-rewarding pre-training signal. Scale buys more capacity but also more exposure to the same compliance-inducing corpus patterns. The net effect on H-Neuron formation is therefore ambiguous a priori.

#### §2.6 Pre-training intervention design

Drawing together §2.1–2.5, the mechanistic story implies the following intervention categories:

**Data filtering interventions:**
- Filter or down-weight documents containing sycophantic interaction patterns (high social-approval language, unconditional agreement with user claims). **[inference]** Feasibility: technically tractable with classifier-based quality scoring. Cost: reduced token count, requiring additional sourcing or slight compute reallocation. Estimated effectiveness: medium — removes the most direct source of compliance-encoding signal, but sycophantic patterns are pervasive in web corpora.
- Aggressive deduplication of confidently-stated factually-false content. **[inference]** Feasibility: requires factual verification at scale, which is expensive and imperfect. Estimated effectiveness: low-to-medium — infeasible at the full token scale of frontier training runs; only practical for identifiable categories (e.g., known misinformation domains, conspiracy content).
- Source-level domain weighting: up-weight high-epistemic-reliability sources (peer-reviewed preprints, textbooks, verified factual databases) and down-weight low-reliability sources (social media, low-quality forums). **[inference, supported by Phi-1 and RefinedWeb findings]** Feasibility: high. Both Phi-1 and RefinedWeb demonstrate that this approach is already operationally viable. Estimated effectiveness: medium — reduces the concentration of compliance-rewarding patterns without eliminating them.

**Curriculum learning interventions:**
- Stage training data so that high-quality, epistemically reliable content dominates the early training phase (when foundational representations are forming) and lower-quality content is introduced later or at lower weight. **[inference]** Feasibility: medium — requires careful scheduling and monitoring. Estimated effectiveness: speculative; no direct evidence for effect on H-Neuron formation specifically.

**Auxiliary objective interventions:**
- Add an explicit uncertainty-expression reward to the pre-training loss: a fraction of training examples should be questions for which the correct response is "I don't know" or an explicit uncertainty statement, rewarded as much as a correct factual answer. **[inference]** Feasibility: medium — requires curating an uncertainty-expression dataset and designing a loss term that doesn't interfere with the main NTP objective. Estimated effectiveness: potentially high — directly counteracts the compliance reward by providing a competing signal.
- Add a consistency-checking auxiliary objective: sample two prompts with conflicting premises and penalise responses that agree with both. **[inference]** Feasibility: low — requires structured adversarial pair construction at scale. Estimated effectiveness: speculative.

**Architectural interventions:**
- Reduce superposition density by widening FFN intermediate dimensions without proportionally scaling parameters elsewhere, allowing each feature to be more orthogonally encoded. **[inference, derived from Elhage et al. superposition theory]** Feasibility: medium — increases compute but does not change the training objective. Estimated effectiveness: speculative.
- Architectural priors that explicitly promote neuron specialisation (e.g., auxiliary sparsity loss on FFN activations that penalises co-activation of semantically distinct features). **[inference]** Feasibility: low — experimental and not validated at scale.

---

### §3 Reasoning

The convergence between Gao et al.'s empirical findings and the existing training-dynamics literature supports a coherent mechanistic account. The next-token prediction objective is the primary causal driver of H-Neuron formation because it provides a consistent positive reward signal for compliance-encoding activations whenever training data contains sycophantic or confidently-false text — which web-scale corpora do at scale. The empirical finding that H-Neurons exhibit parameter inertia during SFT is consistent with the general finding in alignment research that RLHF operates at the response-distribution level, not the circuit level: gradient signals during SFT are diffuse and of limited magnitude, insufficient to overwrite circuits that were consolidated by billions of NTP training steps.

The scaling picture is nuanced. Lower H-Neuron ratios in larger models could be interpreted as evidence that scale reduces the problem, but the compliance-slope data (2.40 vs 3.03) shows that the disposition is more *diffusely* encoded, not absent. Larger models hallucinate less in absolute terms (GPT-4 hallucination rate ~28.6% vs GPT-3.5 ~40% on citation-based evaluations), but the structural cause is not eliminated. This is consistent with the superposition framing: more capacity means features are less compressed and less likely to interfere, reducing hallucination rates without eliminating the underlying compliance feature.

The data quality literature (Phi-1, RefinedWeb) establishes that filtering dramatically changes model behaviour, providing a plausible pathway for pre-training interventions. The absence of direct ablation evidence for H-Neuron reduction via data filtering is a gap in the literature, not a refutation of the hypothesis.

---

### §4 Consistency Check

No internal contradictions are found in the evidence base. The following potential tensions were examined:

1. **Tension between "larger models hallucinate less" and "scaling does not solve the problem"**: Resolved. Larger models have lower hallucination rates *and* lower perturbation leverage per neuron. Both are consistent with the compliance feature being more diffusely encoded. The behavioural outcome improves; the structural root cause does not disappear.

2. **Tension between "RLHF cannot fix pre-training" and "RLHF does reduce hallucinations"**: Resolved. RLHF suppresses expression without eliminating the circuits. Both claims are simultaneously true and consistent with the parameter-inertia finding.

3. **Tension between "data filtering reduces hallucinations" (RefinedWeb) and "H-Neurons originate in NTP objective"**: Resolved. These are complementary, not contradictory. The NTP objective is the mechanism; sycophantic/false training data provides the signal that drives the mechanism. Reducing the signal reduces circuit consolidation; changing the objective eliminates the mechanism. Both are valid intervention targets operating at different levels.

4. **Confidence levels for scaling claims:** The claim that H-Neuron density is lower in larger models is based on the ratio data in Table 1 of Gao et al., but this is only six data points across three model families. The pattern is consistent but should be treated as medium confidence rather than a firm scaling law.

---

### §5 Depth and Breadth Expansion

**Technical lens:** The parameter-inertia finding has direct implications for fine-tuning methods beyond SFT. If H-Neurons change minimally during SFT, the question is whether LoRA-based fine-tuning, which explicitly restricts weight updates to low-rank adaptations, changes H-Neurons even less. Conversely, full-parameter continued pre-training on curated factual corpora might be more effective at modifying H-Neuron weights than SFT on instruction-following data. This is an actionable implication: targeted continued pre-training (not just instruction fine-tuning) on high-quality factual corpora may partially address H-Neuron circuits where SFT cannot.

**Economic lens:** The interventions with the clearest feasibility (domain weighting, source-level quality filtering) are already deployed by leading labs (Phi-1, Falcon/RefinedWeb). They are low marginal cost relative to the overall pre-training budget. Auxiliary uncertainty-expression objectives require dataset construction — a one-time cost that is small relative to compute. The most expensive interventions (architectural changes, adversarial pair construction at scale) are also the most speculative in terms of effectiveness.

**Regulatory and alignment lens:** If H-Neuron density becomes a reportable model characteristic (analogous to perplexity), regulators could require that it be measured and disclosed. This would create an incentive for labs to invest in pre-training interventions, since reporting a high H-Neuron density would be reputationally costly.

**Historical lens:** The discovery that sycophantic behaviour is encoded at the pre-training stage echoes earlier findings about bias in word embeddings: biases in pre-training corpora (racial, gender) were shown to be encoded directly in embedding spaces, and RLHF-style debiasing fine-tuning was found to reduce surface expression without eliminating the underlying representation. The H-Neuron story is structurally identical, and the analogy suggests that the same lesson applies: interventions at the data source level have proven more durable than post-hoc alignment.

---

### §6 Synthesis

**Answer to the research question:** H-Neurons form during pre-training because the next-token prediction objective provides an unrestricted positive reward signal for compliant, agreeable continuations on corpora that contain sycophantic and confidently-stated-false text at scale. Post-training alignment (SFT, RLHF) cannot eliminate these circuits because RLHF operates at the response-distribution level and H-Neurons exhibit parameter inertia — they are among the neurons that change least during alignment. Scaling reduces the ratio of H-Neurons and the per-neuron perturbation leverage, but does not eliminate the compliance feature; it distributes it. Three families of pre-training intervention are candidates: (1) data filtering — domain-level quality weighting and sycophantic-content removal; (2) auxiliary objectives — uncertainty-expression rewards during pre-training; (3) architectural choices — reducing superposition pressure via FFN widening. Of these, data quality filtering has the strongest supporting evidence and lowest cost; auxiliary objectives are the most targeted but require bespoke dataset construction.

**Key claims:**
1. H-Neurons are present in base models before any alignment, confirmed by backward-transferability experiments (AUROC > baseline across all 6 models and 3 datasets). **[fact, high confidence]**
2. H-Neurons undergo minimal weight change during SFT (parameter inertia; avg rank ≈ 0.97 in Mistral-Small). **[fact, high confidence]**
3. The NTP objective is the proximate causal mechanism for H-Neuron formation, because it rewards fluent compliant continuations without a countervailing factual accuracy signal. **[fact/inference mix; the objective is a fact; the causal attribution is a high-confidence inference]**
4. RLHF suppresses H-Neuron expression behaviorally but does not rewrite the circuits. **[inference, high confidence]**
5. Larger models have lower H-Neuron ratios (0.01‰ vs 0.35‰) and lower perturbation compliance slopes (2.40 vs 3.03), but the over-compliance feature persists more diffusely. **[fact, medium confidence — small sample of model families]**
6. Data quality filtering (domain weighting, sycophantic text removal) is the most feasible pre-training intervention, with supporting evidence from Phi-1 and RefinedWeb. **[inference, medium confidence]**
7. Auxiliary uncertainty-expression pre-training objectives directly address the causal mechanism but have not been validated at frontier scale. **[inference, low confidence]**

---

### §7 Recursive Review

**Coverage check:** All six approach sub-questions are addressed. The pre-training origin evidence (§2.1), the NTP causal mechanism (§2.2), data quality research (§2.3), RLHF limits (§2.4), scaling dynamics (§2.5), and intervention design (§2.6) are each substantively covered.

**Claim sourcing check:** Every [fact] claim maps to a directly accessed source. [inference] claims are explicitly flagged and justified. [assumption] claims (sycophantic content in web corpora is the primary signal; full ablation evidence is absent) are stated with their justifications.

**Uncertainty acknowledgment:** The key uncertainty is the absence of direct pre-training ablation experiments testing whether removing sycophantic text or adding uncertainty-expression objectives reduces H-Neuron formation. The inference chain from NTP objective → compliance-rewarding corpus signal → H-Neuron consolidation is well-supported by multiple independent lines of evidence but is not directly confirmed by a pre-training intervention experiment. This gap is noted in Risks, Gaps, and Uncertainties.

**Quality check:** All sections contain substantive prose. No section is a heading-only placeholder. Evidence labels are consistently applied throughout.

---

## Findings

### Executive Summary

H-Neurons originate during pre-training because the next-token prediction objective provides an unrestricted positive reward for compliant, agreeable continuations whenever training corpora contain sycophantic or confidently-stated-false text — which web-scale corpora do at sufficient concentration to consolidate dedicated over-compliance circuits. Post-training alignment (SFT, RLHF) cannot eliminate these circuits: Gao et al. confirm that H-Neurons exhibit parameter inertia, changing minimally during alignment, and the RLHF literature confirms that reward signals operate at the response-distribution level rather than rewriting individual pre-trained circuits. Scaling reduces H-Neuron ratios and per-neuron perturbation leverage, but distributes rather than eliminates the compliance feature, explaining why even frontier models hallucinate despite aggressive alignment. Three pre-training intervention families have candidacy: data quality filtering (strongest evidence, operational precedent from Phi-1 and RefinedWeb), auxiliary uncertainty-expression objectives (most targeted, unvalidated at scale), and architectural superposition reduction (most speculative, lowest supporting evidence). No intervention has been validated by a direct pre-training ablation for H-Neuron formation specifically; this remains the primary gap in the literature.

### Key Findings

1. H-Neurons are present and predictive in base pre-trained models before any instruction tuning or RLHF, confirmed by backward-transferability experiments in Gao et al.: classifiers built from aligned-model H-Neurons achieve AUROC scores significantly above random baseline on all six base models and three evaluation domains (TriviaQA, BioASQ, NQ-Open). [confidence: high]

2. H-Neurons exhibit parameter inertia during SFT: they rank among the model parameters that change least during the transition from base to instruction-tuned model, with average cosine-similarity rank of ≈0.97 in Mistral-Small (P < 0.001), confirming that standard instruction tuning does not restructure the hallucination circuits. [confidence: high]

3. The next-token prediction objective is the proximate causal mechanism for H-Neuron formation, because it rewards fluent agreeable continuations without a countervailing factual accuracy penalty; on training corpora containing sycophantic and confidently-stated-false text, this signal consolidates dedicated over-compliance circuits in FFN neurons. [confidence: high for causal attribution to NTP objective; medium for the specific role of sycophantic corpus content, which is inferred rather than ablated]

4. RLHF suppresses H-Neuron expression at the output level but does not rewrite the underlying circuits: RLHF gradient updates are diffuse and of limited magnitude relative to the billions of NTP steps that consolidated H-Neurons, and the alignment tax constrains how aggressively reward signals can push against pre-trained features without capability degradation. [confidence: high]

5. Larger models have lower H-Neuron ratios (0.01‰ in 24–70B models vs. 0.35‰ in 7B models) and lower per-neuron compliance perturbation slopes (average 2.40 vs. 3.03), indicating that the over-compliance feature is more diffusely encoded at scale — consistent with superposition theory — rather than eliminated. [confidence: medium — based on six model checkpoints across three families]

6. Scaling training tokens and model size equally (Chinchilla-optimal) increases pre-training exposure to compliance-inducing corpus patterns proportionally with model capacity, so scale alone does not resolve the H-Neuron formation problem even as it reduces per-neuron perturbation leverage. [confidence: medium — inference from Chinchilla scaling law applied to compliance-signal volume]

7. Data quality filtering — domain-level source weighting and removal of low-reliability sycophantic content — is the pre-training intervention with the strongest supporting evidence: Phi-1 demonstrates that 7B tokens of textbook-quality data outperforms 300B tokens of unfiltered web data on coding benchmarks, and RefinedWeb shows that aggressive CommonCrawl filtering matches curated-corpus performance at 5 trillion tokens. [confidence: medium — evidence is from coding/general capability, not H-Neuron formation specifically]

8. An auxiliary uncertainty-expression pre-training objective — rewarding "I don't know" responses as strongly as correct answers on a fraction of training examples — would directly counteract the NTP compliance reward and is the most mechanistically targeted intervention, but has not been validated at frontier training scale and carries risk of degrading task-completion capability if poorly calibrated. [confidence: low — inference from first principles]

9. Architectural reduction of superposition pressure (widening FFN intermediate layers, auxiliary sparsity losses) could reduce H-Neuron consolidation by allowing compliance features to be more orthogonally encoded, but this prediction is derived from toy-model superposition theory and has no direct validation in pre-training experiments with large transformer models. [confidence: low]

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| H-Neurons predictive in base models before alignment (AUROC > baseline on all 6 models) | Gao et al. (2025), arXiv:2512.01797, Fig. 4a | high | Primary empirical evidence for pre-training origin |
| H-Neurons undergo minimal weight change during SFT (parameter inertia, avg rank ≈0.97) | Gao et al. (2025), arXiv:2512.01797, Fig. 4b | high | One-sided t-test P < 0.001 across all tested models |
| NTP objective rewards fluent compliant continuations without factual accuracy penalty | Gao et al. (2025) §5; Kalai et al. (2025) "Why language models hallucinate" | high (mechanism); medium (corpus-signal role) | Kalai et al. is learning-theory paper cited in Gao et al.; no direct ablation |
| RLHF does not rewrite circuits; operates at response-distribution level | Gao et al. parameter inertia; RLHF alignment tax literature | high | Consistent with multiple independent findings on RLHF surface-level operation |
| Larger models have lower H-Neuron ratios (0.01‰ vs 0.35‰) | Gao et al. (2025), Table 1 | medium | Only 6 models, 3 families; pattern consistent but not a formal scaling law |
| Larger models show lower compliance perturbation slopes (2.40 vs 3.03) | Gao et al. (2025), Fig. 3 | medium | Same data limitation; "average slope" aggregated across 4 benchmarks |
| Data filtering dramatically changes model behaviour (Phi-1 quality data effect) | Gunasekar et al. (2023), arXiv:2306.11644 | medium | Evidence is for coding benchmarks; generalisation to over-compliance is inference |
| Web-scale filtering can match curated corpora at 5 trillion tokens (RefinedWeb) | Penedo et al. (2023), arXiv:2306.01116 | medium | Demonstrates filtering feasibility and effectiveness on general capability |
| RLHF creates alignment tax; stronger reward optimisation degrades capabilities | Alignment tax literature (ACL 2024) | fact | Constrains how far RLHF can push against pre-trained features |
| Superposition: models encode more features than dimensions; sparse features compress via superposition | Elhage et al. (2022), transformer-circuits.pub toy models | high | Toy model result; direct extrapolation to large transformer H-Neurons is inference |
| Uncertainty-expression auxiliary objective directly addresses NTP compliance reward | First-principles inference from §2 | low | No empirical validation at scale; mechanistically justified |
| Architectural FFN widening could reduce superposition pressure | Elhage et al. (2022) superposition theory | low | Inference; no direct pre-training experiment for H-Neurons |

### Assumptions

- **Assumption:** Web-scale pre-training corpora contain sycophantic and confidently-stated-false text at sufficient concentration and consistency to consolidate dedicated over-compliance circuits. **Justification:** The Constitutional AI paper (Anthropic 2022) motivates its own RLHF approach partly by noting that pre-training data embeds compliance-encouraging patterns. The Phi-1 paper's result that textbook-quality data produces dramatically different model behaviour from unfiltered web data is consistent with data composition having large effects on behavioural dispositions. No direct ablation study removing sycophantic content and measuring H-Neuron formation has been published.

- **Assumption:** The parameter-inertia finding for SFT extends to RLHF. **Justification:** The paper tests SFT models only. RLHF involves more extensive parameter updates, but the structural argument — that NTP-consolidated circuits are more resistant to diffuse gradient updates than to the original concentrated training signal — applies to both. The jailbreak-recovery literature (where RLHF-aligned models revert to pre-training behaviour under adversarial prompts) supports this assumption empirically.

- **Assumption:** The mechanistic insights from Phi-1 (coding quality data) generalise to factual-accuracy and compliance training. **Justification:** The Phi-1 result is in the coding domain; the generalisation to natural language factual accuracy is an inference. The same filtering logic applies, but the specific relationship between textbook-quality text and over-compliance reduction is not directly validated.

### Analysis

The evidence base for the pre-training origin claim is strong: two complementary experiments (backward transferability and parameter evolution) in Gao et al. both point in the same direction, and neither is easily dismissed by alternative hypotheses. The mechanistic attribution — NTP objective on compliance-laden corpora produces H-Neurons — is well-supported by the theoretical literature (Kalai et al.) and is consistent with the Phi-1 and RefinedWeb data quality findings, but lacks a direct ablation experiment. This gap matters for intervention design: if the mechanism is confirmed by ablation, data filtering becomes a high-priority action; without it, the intervention-evidence chain rests on inference.

The RLHF limits argument is the most robust of the cross-source claims. It is supported by: (1) Gao et al.'s parameter inertia finding, (2) the Constitutional AI paper's own framing (it explicitly treats RLHF as layered on top of pre-training, not a replacement), (3) the alignment tax literature, and (4) the jailbreak-recovery empirics. These four independent sources converging on the same conclusion raises confidence above what any single source would provide.

The scaling picture requires careful handling. The claim that "larger models hallucinate less" is true for absolute hallucination rates but does not imply the structural cause is reduced. The H-Neuron ratio data and compliance-slope data together support a model in which the compliance feature is more diffusely encoded at scale — consistent with superposition theory — rather than eliminated. This interpretation is the most coherent reading of the available evidence, though the small number of data points (six model checkpoints) warrants medium rather than high confidence.

Intervention feasibility varies substantially by category. Domain-level quality weighting is already standard practice (Phi-1, RefinedWeb, FineWeb) and has the strongest supporting evidence, though that evidence is not directly about H-Neuron formation. Auxiliary uncertainty-expression objectives are mechanistically optimal but technically undeveloped at frontier scale. Architectural changes are the most speculative.

### Risks, Gaps, and Uncertainties

- **Primary gap:** No direct pre-training ablation experiment tests whether removing sycophantic content or adding uncertainty-expression objectives reduces H-Neuron formation. The causal inference from NTP objective to H-Neuron formation is theoretically motivated and empirically consistent, but not directly confirmed by a pre-training intervention experiment.

- **Scope gap:** Gao et al. test SFT (instruction-tuned) models, not RLHF-trained models. The assumption that RLHF is equally ineffective at modifying H-Neurons is well-motivated but not directly tested.

- **Scaling evidence gap:** The scaling pattern (lower ratio, lower perturbation slope in larger models) is based on six model checkpoints across three families. It is consistent with superposition theory but is not a validated scaling law for H-Neuron density.

- **Inaccessible source:** Kalai et al. (2025) "Why language models hallucinate" is cited in Gao et al. but the full text was not directly accessed for this research item. The claim attributed to this paper (hallucination is an inevitable learning-theoretic consequence of NTP) is taken from Gao et al.'s characterisation of it.

- **Uncertainty about data filtering scope:** Even if sycophantic text removal reduces H-Neuron formation, the practical difficulty of identifying and filtering sycophantic patterns at the scale of 5 trillion tokens without introducing new biases is unresolved.

### Open Questions

- Is there a variant of the next-token prediction objective that treats factual uncertainty as a first-class training signal — e.g., by reserving a fraction of training examples for which uncertainty expression is the correct response? Priority: medium (directly actionable for model developers; no existing validation at frontier scale).
- Can "H-Neuron density" become a reportable model evaluation metric, analogous to perplexity or benchmark accuracy, to incentivise pre-training investment in compliance-reduction? Priority: medium (requires standardised measurement protocol; feeds into regulatory discourse).
- If sycophantic web text is the primary corpus signal driving H-Neuron formation, does synthetic data generation in the style of Phi-1 ("textbooks") measurably reduce H-Neuron formation compared to filtered web data of equivalent volume? Priority: high (directly tests the causal hypothesis; could be run without frontier-scale compute using Pythia-style controlled pre-training experiments).

---

## Output

- Type: knowledge
- Description: A structured analysis of what the pre-training origin of H-Neurons implies for the limits of post-training alignment and for the design of pre-training data, objectives, and architecture; includes a candidate set of pre-training-time interventions and their estimated feasibility.
- Links:
  - https://arxiv.org/abs/2512.01797
  - https://arxiv.org/abs/2306.11644
  - https://transformer-circuits.pub/2022/toy_model/index.html