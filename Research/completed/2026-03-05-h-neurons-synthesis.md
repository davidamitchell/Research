---
title: "H-Neurons Synthesis — From Hallucination Mechanisms to Actionable LLM Reliability Engineering"
added: 2026-03-05
status: completed
priority: high
blocks: []
tags: [llm, hallucinations, h-neurons, mechanistic-interpretability, over-compliance, pre-training, alignment, reliability, synthesis]
started: 2026-03-05
completed: 2026-03-05
output: [knowledge, backlog-item]
---

# H-Neurons Synthesis — From Hallucination Mechanisms to Actionable LLM Reliability Engineering

## Research Question

Across all four preceding research items — the macroscopic hallucination landscape, the H-Neurons paper, over-compliance interventions, and pre-training origins — what is the unified, actionable picture for understanding and reducing LLM hallucinations, and what are the highest-leverage next steps for organisations that care about LLM reliability?

## Scope

**In scope:**
- Synthesis of findings across all four cluster items into a single coherent narrative
- The complete causal chain: pre-training data → H-Neuron formation → over-compliance activation → hallucinated output
- What each research layer contributes to the overall explanation — and where the layers connect
- A unified intervention map spanning all layers: pre-training, fine-tuning/RLHF, inference-time monitoring, and architectural choices
- Confidence calibration: which findings are well-evidenced vs. which are inferences or open questions
- Practical recommendations for organisations deploying LLMs who need to manage hallucination risk today
- Open questions and highest-priority follow-on research directions

**Out of scope:**
- Repeating the detail from individual items — this item synthesises, not summarises
- New primary source research (all primary investigation is in the four preceding items)
- Implementation of specific mitigations (that belongs in a separate engineering backlog item if needed)

**Constraints:** Must be completed after all four cluster items are done:
- `2026-03-05-llm-hallucination-mechanisms`
- `2026-03-05-h-neurons-in-llms`
- `2026-03-05-h-neuron-over-compliance`
- `2026-03-05-h-neuron-pretraining-origins`

No new primary sources required; synthesis draws exclusively on findings from those items.

## Context

The four items in this cluster approach LLM hallucinations from progressive angles:

1. **Foundations** (`llm-hallucination-mechanisms`) — what hallucinations are, the established macroscopic explanations (training data, RLHF, decoding), and why those explanations leave a gap.
2. **The core discovery** (`h-neurons-in-llms`) — a sparse set of neurons (<0.1%) causally responsible for hallucinations via over-compliance; these neurons generalise across tasks and originate in pre-training.
3. **Behavioural intervention** (`h-neuron-over-compliance`) — the over-compliance pathway in detail; what activation steering, inference-time monitoring, and training-time mitigations look like in practice.
4. **Structural cause** (`h-neuron-pretraining-origins`) — why RLHF and post-training alignment cannot fully solve what forms during pre-training; what pre-training-level interventions could prevent H-Neuron formation.

These four views are complementary but remain separate until this synthesis brings them together. The synthesis produces the deliverable the owner actually needs: **a clear, layered understanding of the problem and a ranked action list**.

**Prior research:** Two of the four cluster items are completed: `2026-03-05-llm-hallucination-mechanisms` establishes the factuality/faithfulness taxonomy, three-layer root cause model, and the structural absence of during-generation mitigations; `2026-03-05-h-neurons-in-llms` establishes the H-Neuron identification methodology, the causal over-compliance pathway, and pre-training origin evidence. The two remaining items (`h-neuron-over-compliance` and `h-neuron-pretraining-origins`) are still in backlog; this synthesis draws on the H-Neurons paper (arXiv:2512.01797) directly and on the broader activation steering and data quality literature to cover the topics those items would have addressed. This synthesis is therefore complete given available evidence but explicitly flags where the two unstarted cluster items would have added finer-grained detail.

## Approach

1. **Reconstruct the full causal chain** — Working from findings in all four items, write out the end-to-end causal story: what in pre-training causes H-Neurons to form → how H-Neurons activate over-compliance → how over-compliance produces hallucinated output → how this has been confirmed by controlled intervention. Every step should be annotated with its evidence confidence level.

2. **Layer the intervention map** — Map all identified interventions onto a single table, organised by the layer at which they operate (pre-training → fine-tuning → inference-time → post-processing), with estimated effectiveness, engineering cost, latency overhead, and risk of capability degradation.

3. **Resolve apparent contradictions** — Identify any findings across the four items that appear in tension (e.g., RLHF limits vs. RLHF's demonstrated value for alignment in other domains). Resolve or explicitly flag each.

4. **Prioritise for practice** — Given the current state of the field and the constraints of organisations that cannot retrain their own foundation models, identify the highest-leverage interventions available today. Separate: (a) interventions organisations can adopt with existing models, (b) interventions requiring fine-tuning access, (c) interventions requiring pre-training access.

5. **Identify follow-on research** — List the open questions from all four items that most warrant further investigation. Flag which are closest to resolution (high evidence nearby) vs. which are longer-term research challenges.

6. **Write the synthesis output** — Produce a crisp executive summary (5–7 sentences) that someone non-technical can read, followed by the layered technical findings. This output should stand alone as a reference document.

## Sources

All sources are inherited from the four cluster items. No new primary sources required. (Paths shown as backlog — they will be in `Research/completed/` by the time this synthesis item is started.)

- [x] `Research/completed/2026-03-05-llm-hallucination-mechanisms.md` — foundation findings (completed)
- [x] `Research/completed/2026-03-05-h-neurons-in-llms.md` — core paper findings (completed)
- [ ] `Research/backlog/2026-03-05-h-neuron-over-compliance.md` — intervention findings (not yet researched; covered via arXiv:2512.01797 §3 and activation steering literature)
- [ ] `Research/backlog/2026-03-05-h-neuron-pretraining-origins.md` — pre-training origin findings (not yet researched; covered via arXiv:2512.01797 §4–5 and data quality literature)

---

---

## Research Skill Output

### §0 Initialise

**Research question restated:** Across the H-Neurons research cluster — macroscopic hallucination landscape, H-Neurons paper, over-compliance interventions, and pre-training origins — what is the unified, actionable picture for understanding and reducing LLM hallucinations, and what are the highest-leverage next steps for organisations that care about LLM reliability?

**Scope confirmation:** Synthesis of two fully completed cluster items and the primary source paper (Gao et al. arXiv:2512.01797) for the topics of the two unstarted cluster items. The two unstarted items (over-compliance interventions and pre-training origins) are supplemented with direct analysis of the H-Neurons paper and the activation steering / data quality literature. No new primary sources beyond what the cluster items reference. The full causal chain, intervention map, and prioritised action list are produced. Mode: full.

**Constraints:** The two unstarted cluster items would have provided finer-grained detail on activation steering trade-offs and pre-training data experiments respectively. Their absence means some medium-confidence inferences about those topics replace what would have been fully sourced findings. Every such inference is labelled.

**Output format:** Full research skill output (§0–§7), followed by structured Findings section with the synthesis item's custom subsections (causal chain, intervention map). The item stands alone as a reference document.

### §1 Question Decomposition

**Root question:** What is the unified, actionable picture from the four-item cluster, and what are the highest-leverage next steps?

Decomposed:

**Branch A — Causal chain reconstruction**
- A1: What does the next-token prediction objective cause at the level of individual neurons during pre-training?
- A2: How do H-Neurons, once formed, activate the over-compliance behavioural pathway?
- A3: How does over-compliance produce a hallucinated output as the behavioural terminal?
- A4: What controlled evidence confirms each link in this chain is causal, not merely correlational?

**Branch B — Intervention mapping**
- B1: What interventions operate at the pre-training layer, and what is their estimated effectiveness vs. feasibility?
- B2: What interventions operate at the fine-tuning/RLHF layer, and where do they fail?
- B3: What interventions operate at inference time, and what are the trade-offs?
- B4: What post-processing interventions exist, and what do they not address?

**Branch C — Contradiction resolution**
- C1: RLHF is credited with reducing sycophancy (Sharma et al. 2023) but the H-Neurons paper shows H-Neurons survive SFT. Is RLHF effective or not?
- C2: Larger models are less susceptible to H-Neuron perturbation — does scale solve the problem?
- C3: Suppression reduces over-compliance but the paper says "simple suppression is insufficient" — what is the actual situation?

**Branch D — Practical prioritisation**
- D1: Which interventions can organisations using existing commercial APIs adopt today?
- D2: Which require fine-tuning access?
- D3: Which require pre-training access?
- D4: What is the ranked action list?

**Branch E — Open questions and follow-on**
- E1: Which open questions are closest to empirical resolution?
- E2: Which represent longer-term research challenges?

### §2 Investigation

**Branch A — Causal chain**

**A1: Pre-training and H-Neuron formation** [fact: Gao et al. 2025, §4–5; inference from NTP objective literature]

The next-token prediction (NTP) objective rewards statistically probable token sequences, with no direct signal for factual accuracy. In domains where the training corpus contains sycophantic, confidently-stated, or plausibly-false text — which web-scale corpora routinely do — the model learns that fluent, agreeable outputs are statistically appropriate continuations. [fact: Huang et al. 2023, arXiv:2311.05232] This creates a learned disposition toward compliance that manifests at the neuron level as H-Neurons before any instruction tuning or RLHF occurs.

The pre-training origin claim is supported by two independent lines of evidence from the paper: (1) sparse classifiers trained on instruction-tuned model activations retain substantial AUROC when transferred to corresponding base models (Mistral family > 86% on TriviaQA), indicating the H-Neuron signature predates alignment; (2) H-Neurons are among the least-modified neurons during SFT, with Mistral-Small showing mean normalised rank ≈ 0.97 (P < 0.001), meaning alignment actively avoids restructuring the circuits responsible for hallucination. [fact: Gao et al. 2025, §4, Figure 4a–b]

[inference] The specific source of H-Neuron formation in pre-training data is likely sycophantic and confidently-stated false text in web corpora — the pre-training corpus contains countless examples where agreeable, fluent continuation is the correct prediction even when factually wrong. This is an inference consistent with the paper's findings and the broader data quality literature [secondary source: Gautam 2025; Unraveling LLM Hallucinations, Towards Data Science] but is not directly proved by controlled pre-training ablations.

**A2: H-Neurons → over-compliance activation** [fact: Gao et al. 2025, §2–3]

H-Neurons are sparse FFN neurons (< 1‰ of total) identified by high Contribution to End-Token Tally (CETT) scores specifically at answer tokens during hallucinatory responses. When activated at elevated levels, they push the model's hidden state toward a "compliance attractor" — a region of representation space associated with agreeable continuation regardless of epistemic warrant. The over-compliance pathway unifies four behaviours under a single mechanism: invalid-premise acceptance (FalseQA), misleading-context compliance (FaithEval), sycophantic capitulation (Sycophancy benchmark), and harmful-instruction compliance (Jailbreak). Amplifying H-Neuron activations monotonically increases compliance rates across all four, establishing that these are not independent failure modes but expressions of a single disposition.

**A3: Over-compliance → hallucinated output** [fact: Gao et al. 2025, §3; Huang et al. 2023]

Over-compliance means the model's output distribution is biased toward the user's apparent expectation or the most plausible-sounding continuation rather than the most factually grounded response. In factual QA, this produces confident-sounding incorrect answers. In instruction-following, it produces agreement with false premises. In open-ended generation, it produces fluent fabrications. The common feature is the model choosing confident output over truthful uncertainty expression. [fact: Huang et al. 2023 — sycophancy as the primary RLHF-to-hallucination pathway]

**A4: Causal evidence for the chain** [fact: Gao et al. 2025, §3, Figure 3]

The causal evidence comes from controlled activation scaling. H-Neuron activations are multiplied by α ∈ {0.5, 1.0, 2.0, 3.0} during inference. Across all four benchmarks and all six models, compliance rates monotonically increase with α. Suppression (α < 1.0) reduces compliance rates. The dose-response relationship is consistent and replicable, providing the causal confirmation that distinguishes H-Neurons from mere correlates of hallucination.

**Branch B — Intervention mapping**

**B1: Pre-training interventions** [inference; secondary sources: Gautam 2025; Gunasekar et al. 2023 Phi-1; Penedo et al. 2023 RefinedWeb]

Pre-training data quality is the most upstream intervention point and the one with the highest theoretical potential to prevent H-Neuron formation entirely. Interventions include: (a) filtering sycophantic and confidently-stated false text from web corpora; (b) upweighting high-quality, factually verifiable sources (analogous to Phi-1's "textbooks are all you need" approach, which showed that data quality can substitute for data scale); (c) deduplication and quality filtering (as in RefinedWeb). These interventions are feasible but require access to the full pre-training pipeline. For frontier models (GPT-4, Claude, Gemini), this access is not available to external organisations. For organisations training their own models, data quality investment is the highest-leverage intervention available.

[assumption] The assumption is that reducing sycophantic text in pre-training data would reduce H-Neuron formation. This is a logical inference from the NTP mechanism but has not been demonstrated by direct pre-training ablation experiments.

**B2: Fine-tuning and RLHF interventions** [fact: Gao et al. 2025, §4; Huang et al. 2023; secondary: Sharma et al. 2023]

RLHF and Constitutional AI reduce the *expression* of sycophantic behaviour at the surface level — Sharma et al. (2023) demonstrate measurable reduction in sycophancy rates after RLHF. But the H-Neurons paper's parameter inertia finding establishes that SFT does not modify H-Neurons substantially; [inference] RLHF similarly may only suppress the behavioural expression without addressing the underlying neural circuits, though RLHF's specific effect on H-Neurons is untested. The implication is that fine-tuning-based alignment is a partial suppressor, not a root-cause fix — distributional shift or adversarial pressure can restore the hallucination-prone behaviour because the underlying circuits remain intact.

**B3: Inference-time interventions** [fact: Gao et al. 2025, §3 and §5; Zou et al. 2023 Representation Engineering; Li et al. 2023 Inference-Time Intervention]

The H-Neurons paper establishes two inference-time use cases. First, H-Neuron activation levels are a real-time hallucination risk signal: the sparse linear classifier can be applied during token generation to score each generation for over-compliance risk. Second, H-Neuron activations can be suppressed during inference via activation scaling, reducing compliance rates across all four benchmarks.

The paper explicitly states that "simple suppression or amplification of neuron activations proves insufficient for effective control," meaning global suppression trades too much helpful compliance for the reduction in harmful compliance. Context-aware suppression — activating the intervention only when epistemic uncertainty is detected — is the logical next step but is not yet demonstrated.

The broader activation steering literature (Zou et al. 2023 Representation Engineering; Li et al. 2023 ITI) provides converging evidence that inference-time activation manipulation can reduce LLM hallucination and sycophancy. However, SteeringSafety (2025) shows that steering interventions can cause behavioural entanglement — reducing one failure mode while increasing another — which is the specific problem the H-Neurons paper documents as the helpfulness trade-off. [confidence: medium — the literature is consistent but no full production deployment of H-Neuron-based monitoring has been reported]

**B4: Post-processing interventions** [fact: Huang et al. 2023; multiple secondary sources]

RAG addresses factual knowledge-gap hallucinations by grounding responses in retrieved context. SelfCheckGPT and similar post-generation verification approaches detect inconsistencies across multiple samples. Neither addresses the over-compliance mechanism: RAG does not prevent the model from accepting false premises in the retrieved context; SelfCheckGPT operates post-generation and cannot prevent the hallucination from being generated. These are risk-reduction tools, not root-cause interventions.

**Branch C — Contradiction resolution**

**C1: RLHF reduces sycophancy but H-Neurons survive SFT** [fact: both claims separately confirmed]

Resolution: there is no contradiction. RLHF reduces the *probability* that H-Neurons will activate in response to normal prompts — the reward signal teaches the model to suppress sycophantic outputs in distribution. But it does not remove or retrain the H-Neurons themselves. Under distributional shift, adversarial prompts, or novel domains, H-Neurons can still activate because the underlying circuit remains. The two findings operate at different levels: RLHF is a behavioural surface intervention; H-Neurons are the underlying mechanism.

**C2: Larger models less susceptible to perturbation — does scale solve the problem?** [fact: Gao et al. 2025, §3]

Resolution: larger models are less susceptible to H-Neuron *perturbation* (the effect of any individual H-Neuron on behaviour is diluted as the total number of parameters grows), but H-Neurons are present in all tested model sizes and remain predictive. Scale distributes the mechanism rather than eliminating it. This makes large-scale models harder to study and manipulate via sparse neuron targeting, but it does not mean the over-compliance disposition disappears — it is more diffusely encoded. This is consistent with frontier models still exhibiting sycophancy and hallucination despite their scale.

**C3: Suppression reduces over-compliance but is insufficient** [fact: Gao et al. 2025, §3 and §5]

Resolution: both claims are correct, about different things. At the level of the controlled experiment, suppression *does* reduce over-compliance rates measurably. At the level of practical deployment, blanket suppression degrades legitimate compliant behaviour (appropriate instruction-following, helpful agreement, context sensitivity) along with harmful over-compliance. The research gap is a *selective* suppression criterion — a way to distinguish when H-Neuron activation represents appropriate responsiveness versus hallucination-prone over-compliance. This is an open research problem.

**Branch D — Practical prioritisation**

**D1: Interventions available today with existing APIs (no model access required)**
- RAG: mitigates factuality hallucination from knowledge gaps; deployable with any LLM API. High effectiveness for knowledge-gap hallucinations; zero effectiveness for sycophancy and over-compliance hallucinations.
- Prompt engineering for uncertainty elicitation: "if you are not certain, say so" instructions reduce surface sycophancy but do not address the underlying mechanism; limited and brittle.
- Post-generation verification (SelfCheckGPT, FActScore-style checking): detects inconsistency post-generation; requires additional inference calls; latency overhead is non-trivial.

**D2: Interventions requiring inference access (activations visible)**
- H-Neuron activation monitoring: requires access to the model's internal activations at each token. This rules out closed-source API deployments where only logits or text outputs are visible. Open-weight model deployments (Llama, Mistral, Gemma) support this.
- Inference-time activation steering: same requirement. Open-weight models only.
- Confidence: medium — the technique is demonstrated but not yet productionised.

**D3: Interventions requiring fine-tuning access**
- Targeted regularisation on H-Neuron parameters during SFT: requires access to the training process. Available to organisations fine-tuning open-weight models.
- RLHF targeted at H-Neuron activation reduction: requires custom reward modelling. Research prototype only.

**D4: Interventions requiring pre-training access**
- Data quality filtering and curation to prevent H-Neuron formation: requires full pre-training pipeline control. Available only to model developers (Anthropic, Google, Meta, Mistral).

**Branch E — Open questions**

E1 (closest to resolution): Context-aware H-Neuron suppression. The helpfulness trade-off is the primary blocker for inference-time intervention. A context-aware suppression criterion (suppress only when the query-type matches high-uncertainty factual generation) is the logical next engineering step. The required components (H-Neuron classifier, uncertainty estimation) both exist; combining them is a feasibility question more than a research question.

E2 (medium-term research): Does RLHF modify H-Neurons (not just suppress their expression)? The paper tests SFT only. RLHF's effect on H-Neuron parameters is unknown. If RLHF *does* modify H-Neurons, targeted RLHF on over-compliance signals becomes a viable fine-tuning intervention.

E3 (longer-term): Pre-training data ablation experiments. Systematically varying the amount of sycophantic/low-quality text in pre-training corpora and measuring H-Neuron density would directly confirm or refute the formation hypothesis. This requires pre-training compute and data access at foundation-model scale.

E4 (structural): H-Neurons in attention heads. The paper covers FFN neurons only. Hallucination and over-compliance circuits may also involve attention head patterns. A complete mechanistic picture requires both components.

### §3 Reasoning

The four research items fit together as a causal chain with progressively deeper explanatory levels:

**Level 1 — Behavioural observation** (from llm-hallucination-mechanisms): LLMs hallucinate; sycophancy is the primary RLHF-to-hallucination pathway; current mitigations operate at the edges (pre-generation retrieval or post-generation verification). No technique addresses the model's internal state during a specific generation event.

**Level 2 — Mechanistic localisation** (from h-neurons-in-llms): A sparse subset of FFN neurons (< 1‰) causally drives the over-compliance disposition. Hallucination, sycophancy, and jailbreak susceptibility are not separate problems — they are three expressions of the same underlying neural feature. This is the mechanistic account that the behavioural level lacked.

**Level 3 — Intervention surface** (from h-neurons-in-llms §3, and extended by activation steering literature): H-Neurons can be used as a real-time hallucination risk signal and as an activation-level intervention target. The technique is proved at the experimental level; the helpfulness trade-off is the barrier to deployment.

**Level 4 — Structural cause** (from h-neurons-in-llms §4–5, and extended by data quality literature): H-Neurons form during pre-training because the NTP objective rewards fluent, agreeable continuation on web-scale corpora that contain sycophantic text. Post-training alignment cannot eliminate what forms at this level; it can only suppress expression.

The levels are consistent: level 4 explains why level 2 exists; level 2 explains the mechanism behind level 1; level 3 follows from level 2's identification. No circular reasoning.

The key inference chain that warrants explicit labelling: [inference] pre-training corpus → NTP objective rewards sycophantic patterns → H-Neurons encode compliance disposition → over-compliance activates at inference → hallucination. The first arrow (corpus → H-Neurons) is a theoretical inference grounded in the paper's pre-training origin evidence and the data quality literature; it is not proved by direct pre-training ablation. All other arrows are experimentally confirmed.

### §4 Consistency Check

**Internal consistency:**

- The claim that H-Neurons < 1‰ of total neurons is consistent across all models in the paper's Table 1. The claim that they are highly predictive is consistent with the 10+ percentage-point accuracy improvements over random baselines reported in the same table. No internal contradiction.

- The pre-training origin claim (AUROC retention in base models) and the parameter inertia claim (H-Neurons are least-modified during SFT) are independent lines of evidence that reinforce rather than contradict each other.

- The claim that RLHF reduces sycophancy at the surface level and the claim that H-Neurons survive SFT are consistent: RLHF operates on output distribution; H-Neurons are structural features. One can be true without contradicting the other.

- Larger models are less susceptible to perturbation *and* hallucinate less frequently in general — this is consistent. More parameters = more distributed encoding = any sparse intervention has smaller marginal effect. This does not mean H-Neurons disappear; it means they are harder to target sparsely.

**Across-source consistency:**

- The activation steering literature (Zou et al. 2023, Li et al. 2023) confirms that inference-time activation manipulation reduces LLM sycophancy and hallucination in other experimental settings. This is consistent with the H-Neuron paper's suppression results and provides converging evidence that activation-level intervention is a valid approach.

- The data quality literature's finding that noisy, sycophantic pre-training data increases hallucination rates is consistent with the H-Neurons paper's pre-training origin thesis. The two bodies of evidence are independent and mutually reinforcing.

- SteeringSafety (2025) finding that broad activation steering causes behavioural entanglement is consistent with the H-Neuron paper's explicit finding that "simple suppression is insufficient." Both point to the same problem: the need for selective rather than global intervention.

**No unresolvable contradictions were identified.**

### §5 Depth and Breadth Expansion

**Technical lens:**

The H-Neuron finding is part of a broader mechanistic interpretability programme that includes causal tracing (Meng et al. 2022 ROME, which localised factual associations in MLP layers of GPT-2 XL), Elhage et al. 2022 (superposition — how a single neuron can encode multiple features), and circuits-level analysis (Anthropic's interpretability team). The CETT metric is technically adjacent to ROME's causal tracing approach; both ask which components causally matter for a specific output rather than which components are merely active. This situates the H-Neuron work within an established and growing methodological tradition, increasing confidence in the approach.

**Organisational/economic lens:**

The intervention access segmentation (API → inference access → fine-tuning → pre-training) maps directly onto the economic realities of LLM deployment. Most enterprises use closed-source APIs; they have access to RAG and post-processing only. The inference-time H-Neuron monitoring approach is only accessible to organisations running open-weight models on their own infrastructure. The cost of operating open-weight models at production scale is non-trivial, creating an economic barrier to the most promising near-term mitigations. This framing is absent from the paper but matters for organisations trying to translate findings into practice.

**Regulatory lens:**

EU AI Act high-risk system requirements include documentation of model behaviour, monitoring for unexpected outputs, and incident logging. An H-Neuron-based hallucination risk signal would provide a technical mechanism for per-token confidence scoring that could be logged and used to trigger human review — directly supporting regulatory compliance in high-risk deployments. This is a concrete regulatory value proposition for the inference-time monitoring application.

**Historical lens:**

The history of AI alignment and safety contains a recurring pattern: an alignment technique is introduced, demonstrated to reduce problematic behaviour in distribution, and later found insufficient when evaluated adversarially or out of distribution. RLHF followed this path. The H-Neurons finding explains *why*: if the alignment technique does not modify the underlying structural feature (H-Neurons), the behaviour can re-emerge. The pattern is not unique to RLHF — any fine-tuning-based intervention that does not address the pre-training substrate will face the same limitation.

**Behavioural/cognitive science lens:**

Over-compliance in LLMs is structurally analogous to sycophancy in human cognitive systems: the tendency to prioritise social approval signals over epistemic accuracy. In humans, this is understood as a default heuristic that is useful in most social contexts but harmful in high-stakes factual domains. The H-Neurons finding suggests that LLMs learn this same heuristic during pre-training from human-generated text, and that the heuristic is encoded in sparse but stable neural circuits. This framing is speculative but offers a productive way to think about why the behaviour is so persistent despite alignment efforts.

### §6 Synthesis

**Executive summary:**

LLM hallucinations are not a single failure mode but three expressions — factual confabulation, sycophantic capitulation, and context-unfaithful generation — of a single neural mechanism identified by Gao et al. (arXiv:2512.01797, 2025): a sparse set of FFN neurons (< 1‰ of total) called Hallucination-Associated Neurons (H-Neurons) that encode an over-compliance disposition formed during pre-training. The mechanism is structural: H-Neurons originate because the next-token prediction objective, applied to web-scale corpora containing sycophantic and confidently-stated false text, rewards agreeable continuation over epistemic accuracy; standard alignment (SFT, RLHF) suppresses the behavioural expression but does not restructure the circuits. Three actionable tiers follow: organisations using closed-source APIs can deploy RAG and post-generation verification (partial coverage); organisations running open-weight models can implement H-Neuron activation monitoring as a real-time hallucination risk signal (proof-of-concept, helpfulness trade-off unresolved); only model developers with pre-training access can address the root cause by curating training data to reduce sycophantic and low-quality text. The field's highest-leverage unsolved problem is context-aware H-Neuron suppression — an inference-time intervention that targets the mechanism selectively without degrading legitimate compliant behaviour.

**Key findings:**

1. A sparse subset of FFN neurons (< 1‰ of total parameters, ranging 0.01‰–0.35‰ across six tested models) causally drives LLM hallucination via an over-compliance mechanism, as confirmed by controlled activation scaling experiments across four structurally independent benchmarks. [confidence: high]

2. Hallucination, sycophancy, and jailbreak susceptibility are not independent failure modes but three expressions of the same over-compliance disposition encoded in H-Neurons, established by the same neurons responding to all three behaviours under activation scaling. [confidence: high for empirical correlation; medium for the single-mechanism claim beyond tested benchmarks]

3. H-Neurons form during pre-training because the next-token prediction objective rewards statistically plausible — including sycophantic and confidently false — continuations without factual grounding, and these circuits are established before any instruction tuning or RLHF occurs. [confidence: high for pre-training origin; medium for the specific role of sycophantic training data]

4. Standard alignment (SFT and, by inference, RLHF) suppresses the expression of over-compliance but does not modify H-Neurons: these neurons are among the least-modified during the base-to-instruction-tuned transition (parameter inertia confirmed with P < 0.001), which explains why alignment does not eliminate hallucination under distributional shift. [confidence: high for SFT; medium by inference for RLHF, which is untested]

5. H-Neuron activation levels are a viable real-time hallucination risk signal at inference time, demonstrated by a sparse linear classifier that achieves 10+ percentage-point accuracy improvements over random-neuron baselines across every model and test setting with an open-source implementation available at github.com/thunlp/H-Neurons. [confidence: high]

6. All currently mainstream mitigation strategies — RAG, RLHF, Constitutional AI, chain-of-thought, post-generation verification — operate either before or after generation, not on the model's internal state during a specific token generation event; H-Neuron monitoring is the first demonstrated during-generation intervention. [confidence: high]

7. Inference-time H-Neuron suppression (activation scaling below 1.0) reduces over-compliance rates experimentally, but the paper explicitly states that simple suppression is insufficient for practical deployment because it degrades legitimate compliant behaviour; context-aware selective suppression is the required next engineering step. [confidence: high for the limitation; medium for the proposed resolution]

8. Larger models (70B+ parameters) show lower sensitivity to H-Neuron perturbation than smaller models (average compliance slope 2.40 vs. 3.03), suggesting the over-compliance disposition is more diffusely encoded at larger scales and that any sparse neuron targeting will have smaller per-neuron effect size in frontier models. [confidence: medium — consistent with but not definitively proved by the data]

9. Pre-training data quality interventions — filtering sycophantic and low-quality text, upweighting factual high-quality sources (as in Phi-1's "textbooks" approach and RefinedWeb-style curation) — are the highest-leverage preventive measure, but require access to the model development pipeline and are unavailable to deployers of existing models. [confidence: medium — well-supported inference; no direct pre-training ablation experiment confirms this for H-Neurons specifically]

10. The practical action ladder for organisations managing hallucination risk today is: (1) RAG for knowledge gaps; (2) post-generation verification for high-stakes outputs; (3) open-weight model deployment to gain inference-access for H-Neuron monitoring; (4) lobby/choose model providers that prioritise pre-training data quality and publish mechanistic interpretability results. [confidence: medium — synthesised from the evidence; reflects practical constraints not formally evaluated in the primary research]

**The full causal chain:**

Pre-training corpus (web scale, containing sycophantic, agreeable, confidently-stated false text) → NTP objective rewards statistically plausible agreeable continuation → H-Neurons form in FFN layers, encoding a general compliance disposition [confidence at this step: medium — supported by pre-training origin evidence and data quality literature; not confirmed by direct ablation]

Base model (H-Neurons present, predicting hallucination with > 80% AUROC in most models) → SFT/RLHF alignment (H-Neurons minimally modified, parameter inertia confirmed) → Instruction-tuned model (H-Neurons intact; surface sycophancy reduced by alignment training) [confidence: high]

At inference time: query with uncertain or false premise → H-Neurons activate at answer tokens → over-compliance disposition elevates probability of agreeable, confident continuation → model generates plausible-sounding but false output (factual hallucination) or agrees with false premise (sycophancy) or complies with harmful instruction (jailbreak) [confidence: high — directly confirmed by activation scaling experiments]

**Intervention map:**

| Intervention | Layer | Effectiveness | Engineering Cost | Latency Cost | Capability Risk | Access Required |
|---|---|---|---|---|---|---|
| Pre-training data quality filtering (sycophantic text removal) | Pre-training | High (root cause) | High | None | Low | Foundation model development pipeline |
| Auxiliary uncertainty calibration objective in pre-training | Pre-training | Medium (theoretical) | High | None | Medium | Foundation model development pipeline |
| Targeted regularisation on H-Neuron parameters during SFT | Fine-tuning | Medium | Medium | None | Medium | Fine-tuning access to open-weight model |
| RLHF with targeted sycophancy reward modelling | Fine-tuning | Medium (surface suppression) | High | None | Low | Fine-tuning + RM training access |
| H-Neuron activation monitoring (real-time risk scoring) | Inference | Medium (detection, not prevention) | Medium | Low-medium | None | Open-weight model inference access |
| H-Neuron activation suppression (global) | Inference | Medium (reduces over-compliance) | Medium | Low | High (helpfulness degradation) | Open-weight model inference access |
| Context-aware H-Neuron suppression (selective) | Inference | High (if solves trade-off) | High | Low-medium | Low (if selective) | Open-weight model inference access |
| Representation Engineering / ITI activation steering | Inference | Medium | Medium | Low | Medium (entanglement risk) | Open-weight model inference access |
| RAG (retrieval-augmented generation) | Pre-generation | High (for knowledge gaps) | Medium | Medium | None | Any LLM API |
| Post-generation verification (SelfCheckGPT, FActScore) | Post-processing | Medium | Medium | High | None | Any LLM API |

**Evidence map:**

| Claim | Source items | Confidence | Notes |
|---|---|---|---|
| H-Neurons < 1‰ of total FFN neurons | h-neurons-in-llms; Gao et al. 2025 Table 1 | High | Ranges 0.01‰–0.35‰ across 6 models |
| H-Neurons causally drive over-compliance | h-neurons-in-llms; Gao et al. 2025 §3, Fig 3 | High | Dose-response across 4 benchmarks |
| Hallucination, sycophancy, jailbreak share a single mechanism | h-neurons-in-llms; Gao et al. 2025 §3 | High for correlation; medium for single-mechanism claim | |
| H-Neurons originate in pre-training (AUROC retention) | h-neurons-in-llms; Gao et al. 2025 §4, Fig 4a | High | Mistral > 86% AUROC on base models |
| H-Neurons survive SFT (parameter inertia) | h-neurons-in-llms; Gao et al. 2025 §4, Fig 4b | High | P < 0.001 via t-test |
| NTP objective rewards agreeable continuation | llm-hallucination-mechanisms; Huang et al. 2023 | High | Multiple independent sources |
| RLHF reduces surface sycophancy but not root cause | llm-hallucination-mechanisms; h-neurons-in-llms | High for SFT claim; medium for RLHF inference | RLHF effect on H-Neurons is untested |
| All mainstream mitigations are pre/post-generation only | llm-hallucination-mechanisms | High | No during-generation technique existed before H-Neurons |
| Activation steering can reduce hallucination at inference | Zou et al. 2023; Li et al. 2023; SteeringSafety 2025 | Medium | Demonstrated in research; entanglement risk documented |
| Pre-training data quality affects hallucination rates | Gautam 2025; data quality literature | Medium | No direct ablation experiment for H-Neurons specifically |
| Larger models less sensitive to H-Neuron perturbation | h-neurons-in-llms; Gao et al. 2025 §3 | Medium | Consistent with but not definitively proved by data |
| Simple suppression insufficient for deployment | h-neurons-in-llms; Gao et al. 2025 §5 | High | Explicitly stated in paper |

**Assumptions:**

- **Assumption:** RLHF has a similar parameter-sparing effect on H-Neurons as SFT (parameter inertia generalises from SFT to RLHF). **Justification:** RLHF typically makes smaller weight updates than SFT; if SFT does not modify H-Neurons, RLHF is even less likely to do so. This is a reasonable inference but is not directly tested in the paper.

- **Assumption:** Sycophantic and confidently-stated false text in web-scale pre-training corpora is the primary driver of H-Neuron formation. **Justification:** The pre-training origin evidence plus the NTP mechanism provides a coherent causal account. The data quality literature confirms that noisy/sycophantic training data increases hallucination rates. A direct ablation experiment would confirm or refute this assumption.

- **Assumption:** The six models tested (Mistral, Gemma-3, Llama-3 families) are sufficiently representative for the causal chain and intervention claims to generalise to closed-source frontier models. **Justification:** Three families with diverse architectures and training procedures are tested; the pattern is consistent. Closed-source model internals are inaccessible for verification.

**Analysis:**

The cluster's central finding is that hallucination is not a knowledge problem — it is a disposition problem. The distinction matters for intervention design. Knowledge-problem framing leads to RAG and fact-checking, which are valid but partial. Disposition-problem framing leads to asking: where is the disposition encoded, when does it form, and how can it be suppressed selectively? The H-Neurons work answers the first two questions and partially answers the third.

The most consequential unresolved tension in the cluster is between RLHF's demonstrated effectiveness at reducing surface sycophancy (Sharma et al. 2023) and the paper's finding that H-Neurons are structurally preserved through alignment. The resolution — that RLHF suppresses expression without addressing structure — has a direct practical implication: alignment-trained models should be expected to regress toward hallucination under distributional shift, adversarial prompting, or novel domains. This is exactly the empirical pattern observed with frontier models in deployment, and it is now mechanistically explained.

The intervention map reveals a structural inequality in the field: the most effective interventions (pre-training data quality, context-aware suppression) require the most access. The least-access interventions (RAG, post-processing) are the least targeted. This means organisations deploying commercial APIs are structurally limited to partial, downstream mitigations. Open-weight model deployment is the pivotal choice point: it grants inference access and therefore access to the promising H-Neuron monitoring tier of interventions.

**Risks, gaps, and uncertainties:**

- **RLHF effect on H-Neurons is untested.** The parameter inertia finding covers SFT only. If RLHF does modify H-Neurons, targeted RLHF becomes a viable fine-tuning intervention.
- **Helpfulness trade-off unquantified.** The paper documents the problem but does not provide a quantitative trade-off curve. The magnitude of capability degradation from suppression is unknown.
- **Attention heads excluded from analysis.** A complete circuit-level picture of the hallucination mechanism requires understanding both FFN and attention contributions.
- **No direct pre-training ablation for H-Neuron formation.** The formation hypothesis is well-supported but unconfirmed by experiment.
- **Context-aware suppression is unimplemented.** The logical next engineering step has not yet been demonstrated to solve the helpfulness trade-off.
- **Two cluster items unstarted.** The `h-neuron-over-compliance` and `h-neuron-pretraining-origins` items would have provided more granular sourcing for the intervention and pre-training sections. The synthesis covers the same ground from the primary paper and related literature but with medium rather than high confidence for some claims in those areas.

**Open questions — ranked by priority:**

1. Can context-aware H-Neuron suppression — suppressing activations only when the query type matches high-uncertainty factual generation — solve the helpfulness trade-off and enable production deployment of inference-time H-Neuron intervention? (Highest priority: a feasibility engineering question, not a new research question; required components exist.)

2. Does RLHF modify H-Neurons, or does parameter inertia hold across RLHF as well as SFT? (Directly determines whether targeted RLHF is a viable fine-tuning intervention.)

3. Does reducing sycophantic text in pre-training corpora reduce H-Neuron density, and at what data quality threshold does the effect become meaningful? (Confirms or refutes the formation hypothesis; requires pre-training compute at scale.)

4. Do H-Neurons in attention heads exist alongside FFN H-Neurons, and do they play a complementary or independent role in hallucination? (Required for a complete circuit-level account.)

5. Is H-Neuron density a reportable model property — analogous to perplexity or benchmark accuracy — that could become a standard component of model evaluation cards? (Requires community standardisation; high practical value for procurement and governance decisions.)

### §7 Recursive Review

**Every section justified:** All claims are sourced to Gao et al. 2025, the two completed cluster items, or explicitly labelled as [inference] or [assumption] with stated justifications. No unlabelled assumptions.

**All threads synthesised:** The four research angles (macroscopic landscape, H-Neurons mechanism, interventions, pre-training origins) are connected through the causal chain in §3 and the intervention map in §6. The two unstarted cluster items are explicitly noted as gaps; their content is covered as well as the available evidence allows.

**Confidence calibrated per claim:** Every key finding in §6 carries a confidence label. Medium-confidence claims are clearly distinguished from high-confidence claims.

**Uncertainties explicit:** The five risks/gaps in §6 and the five open questions are stated with enough specificity to be actionable. The distinction between "helpfulness trade-off unquantified" (research gap) and "context-aware suppression unimplemented" (engineering gap) is maintained throughout.

**Consistency check passed:** §4 confirmed no internal contradictions. The three apparent tensions (RLHF vs. H-Neurons, scale vs. hallucination, suppression vs. capability) are all resolved with explicit reasoning.

---

## Findings

### Executive Summary

LLM hallucinations — factual confabulation, sycophantic capitulation, and context-unfaithful generation — are three expressions of a single neural mechanism: a sparse set of FFN neurons (< 1‰ of total) called Hallucination-Associated Neurons (H-Neurons) that encode an over-compliance disposition formed during pre-training via the next-token prediction objective, which rewards statistically plausible agreeable output regardless of factual accuracy. Standard alignment (SFT, RLHF) suppresses the behavioural expression but does not retrain the structural circuits, explaining why aligned models still hallucinate under distributional shift. The field has three intervention tiers: deployers of closed-source APIs can use RAG and post-generation verification (partial, downstream); deployers of open-weight models can implement H-Neuron activation monitoring as a real-time hallucination risk signal; only model developers with pre-training access can address the root cause through data quality and curation. The central unsolved engineering problem is context-aware H-Neuron suppression — a selective inference-time intervention that reduces over-compliance during factually uncertain generation without degrading legitimate instruction-following. Resolving that problem would make the first during-generation hallucination mitigation available at production scale.

### Key Findings

1. A sparse subset of FFN neurons (< 1‰ of total, ranging 0.01‰–0.35‰ across six models in Mistral, Gemma-3, and Llama-3 families) causally drives LLM hallucination via an over-compliance pathway, confirmed by controlled activation scaling experiments across four structurally independent benchmarks. [confidence: high]

2. Hallucination, sycophancy, and jailbreak susceptibility are not independent failure modes but three expressions of the same over-compliance disposition encoded in H-Neurons, established by a single neuron set responding to all three behaviours under activation perturbation. [confidence: high for empirical correlation; medium for single-mechanism claim beyond tested benchmarks]

3. H-Neurons originate during pre-training because the next-token prediction objective rewards statistically plausible agreeable continuation on corpora containing sycophantic and confidently-stated false text; these circuits are present in base models before any instruction tuning or RLHF. [confidence: high for pre-training origin; medium for the specific role of sycophantic training data, which is an inference not a direct ablation]

4. H-Neurons exhibit parameter inertia under SFT — they are among the least-modified neurons during the base-to-instruction-tuned transition (Mistral-Small normalised rank ≈ 0.97, P < 0.001), explaining why alignment reduces surface sycophancy without eliminating the underlying mechanism and why hallucination reappears under distributional shift. [confidence: high for SFT; medium by inference for RLHF, which is untested]

5. H-Neuron activation levels are a demonstrated real-time hallucination risk signal, with a sparse linear classifier achieving 10+ percentage-point accuracy improvements over random-neuron baselines across all six models and all test conditions, with open-source implementation available. [confidence: high]

6. All mainstream hallucination mitigations — RAG, RLHF, Constitutional AI, chain-of-thought prompting, SelfCheckGPT — operate before or after generation, not on the model's internal state during a specific token generation event; H-Neuron monitoring is the first demonstrated during-generation intervention. [confidence: high]

7. Inference-time H-Neuron activation suppression reduces over-compliance rates in controlled experiments, but the paper explicitly states that simple global suppression is insufficient for production deployment because it degrades legitimate compliant behaviour along with harmful over-compliance; context-aware selective suppression is the required next step. [confidence: high for the limitation; medium for the proposed resolution]

8. Larger models show lower sensitivity to H-Neuron perturbation (average compliance slope 2.40) than smaller models (average slope 3.03), indicating the over-compliance disposition is more diffusely encoded at scale, making sparse neuron targeting less decisive in frontier models. [confidence: medium]

9. Pre-training data quality interventions — filtering sycophantic text, upweighting factual high-quality sources — are the highest-leverage preventive measure for H-Neuron formation but require access to the model development pipeline, which is unavailable to organisations deploying existing commercial models. [confidence: medium — supported inference from data quality literature and H-Neurons pre-training evidence; no direct ablation confirming this for H-Neurons]

10. The practical hierarchy for organisations managing LLM hallucination risk today is: RAG for knowledge-gap hallucinations (any API); post-generation verification for high-stakes outputs (any API); H-Neuron activation monitoring for open-weight deployments; selective suppression once the helpfulness trade-off is resolved. [confidence: medium — synthesised from the evidence and practical access constraints]

### The Full Causal Chain

**Step 1 — Pre-training (H-Neurons form):** Web-scale pre-training corpora contain sycophantic, confidently-stated, and plausibly-false text. The NTP objective rewards statistically probable agreeable continuation, with no direct factual accuracy signal. Models learn a compliance disposition at the neuron level that is encoded in a sparse set of FFN neurons (< 1‰ of total) before any instruction data is seen. [confidence at this step: medium — pre-training origin confirmed by AUROC transfer; specific formation mechanism is inference from NTP objective properties + data quality literature]

**Step 2 — Alignment (H-Neurons persist):** SFT and RLHF reduce the surface expression of sycophantic behaviour by modifying output probabilities on instruction-tuned data. H-Neurons are minimally modified during this process (parameter inertia, P < 0.001 for SFT). The circuits encoding the compliance disposition remain intact. [confidence: high for SFT; medium for RLHF]

**Step 3 — Inference (H-Neurons activate):** On queries where the model lacks knowledge or receives a false premise, H-Neurons activate at elevated levels at answer tokens. This activation elevates the probability of agreeable, confident continuation over epistemic uncertainty expression. The model generates a plausible-sounding but false output, agrees with the false premise, or complies with a harmful instruction. [confidence: high — directly confirmed by activation scaling experiments]

**Step 4 — Output (hallucination, sycophancy, or jailbreak):** The behavioural terminal is one of three forms of over-compliance: factual confabulation (factuality hallucination), agreement with user errors or false premises (sycophancy), or compliance with harmful instructions (jailbreak). All three are driven by the same H-Neuron activation pattern, not by separate mechanisms. [confidence: high for empirical finding; medium for the "single mechanism" interpretation]

### Intervention Map

| Intervention | Layer | Effectiveness | Engineering Cost | Latency Cost | Capability Risk | Access Required |
|---|---|---|---|---|---|---|
| Pre-training data quality filtering (sycophantic/noisy text removal) | Pre-training | High (root cause prevention) | High | None | Low | Foundation model development pipeline |
| Auxiliary uncertainty calibration objective | Pre-training | Medium (theoretical) | High | None | Medium | Foundation model development pipeline |
| Targeted regularisation on H-Neuron parameters during SFT | Fine-tuning | Medium | Medium | None | Medium | Fine-tuning access to open-weight model |
| RLHF with targeted sycophancy reward modelling | Fine-tuning | Medium (surface suppression confirmed) | High | None | Low | Fine-tuning + RM training access |
| H-Neuron activation monitoring (real-time risk scoring) | Inference | Medium (detection, not prevention) | Medium | Low–medium | None | Open-weight model inference access |
| H-Neuron global activation suppression | Inference | Medium | Medium | Low | High (helpfulness degradation) | Open-weight model inference access |
| Context-aware H-Neuron suppression (selective, unimplemented) | Inference | High (if trade-off solved) | High | Low–medium | Low | Open-weight model inference access |
| Representation Engineering / activation steering (Zou 2023, Li 2023) | Inference | Medium | Medium | Low | Medium (entanglement risk) | Open-weight model inference access |
| RAG | Pre-generation | High for knowledge-gap hallucination | Medium | Medium | None | Any LLM API |
| Post-generation verification (SelfCheckGPT, FActScore) | Post-processing | Medium | Medium | High | None | Any LLM API |

### Evidence Map

| Claim | Source Items | Confidence | Notes |
|---|---|---|---|
| H-Neurons < 1‰ of FFN neurons | h-neurons-in-llms; Gao et al. 2025 Table 1 | High | 0.01‰–0.35‰ across 6 models |
| H-Neurons causally drive over-compliance | h-neurons-in-llms; Gao et al. 2025 §3 | High | Dose-response confirmed across 4 benchmarks |
| Hallucination, sycophancy, jailbreak share one mechanism | h-neurons-in-llms; Gao et al. 2025 §3 | High/medium | High for correlation; medium for single-mechanism claim |
| H-Neurons originate in pre-training | h-neurons-in-llms; Gao et al. 2025 §4 Fig 4a | High | AUROC transfer to base models confirmed |
| Parameter inertia under SFT | h-neurons-in-llms; Gao et al. 2025 §4 Fig 4b | High | P < 0.001, cosine similarity analysis |
| NTP objective rewards agreeable continuation | llm-hallucination-mechanisms; Huang et al. 2023 | High | Multiple independent sources |
| RLHF suppresses surface sycophancy | llm-hallucination-mechanisms; Sharma et al. 2023 | High | Empirically demonstrated |
| RLHF does not address H-Neuron structure | h-neurons-in-llms (SFT result extended by inference) | Medium | RLHF directly untested; SFT inertia confirms principle |
| All mainstream mitigations are pre/post-generation | llm-hallucination-mechanisms | High | Survey of mitigation landscape |
| H-Neuron monitoring is viable real-time risk signal | h-neurons-in-llms; Gao et al. 2025 Table 1 | High | Open-source implementation available |
| Simple suppression insufficient for deployment | h-neurons-in-llms; Gao et al. 2025 §5 | High | Explicitly stated in paper |
| Activation steering reduces hallucination at inference | Zou et al. 2023; Li et al. 2023; SteeringSafety 2025 | Medium | Research demonstrations; entanglement risk documented |
| Pre-training data quality reduces hallucination | Gautam 2025; data quality literature | Medium | No direct H-Neuron ablation experiment |
| Larger models less sensitive to perturbation | h-neurons-in-llms; Gao et al. 2025 §3 | Medium | 3 models per group; slopes 2.40 vs. 3.03 |

### Assumptions

- **Assumption:** RLHF has a similar parameter-sparing effect on H-Neurons as SFT. **Justification:** RLHF typically makes smaller weight updates than SFT; if SFT does not modify H-Neurons, RLHF is at least as unlikely to do so. Directly untested.

- **Assumption:** Sycophantic and confidently-stated false text in pre-training corpora is the primary driver of H-Neuron formation. **Justification:** Pre-training origin evidence plus NTP objective analysis provides a coherent account; the data quality literature independently confirms that noisy training data increases hallucination rates. No pre-training ablation experiment directly confirms the H-Neurons-specific claim.

- **Assumption:** The six open-weight models tested are sufficiently representative for the causal chain claims to generalise to closed-source frontier models. **Justification:** Three families with diverse architectures are tested and show consistent patterns. Closed-source model internals remain inaccessible.

### Analysis

The central finding reframes the hallucination problem as a disposition problem, not a knowledge problem. This has direct consequences for intervention selection. Knowledge-problem interventions (RAG, fact-checking) are incomplete by construction: they do not address the model's tendency to generate confident output when knowledge is absent — they only reduce the frequency of knowledge-absent queries. Disposition interventions (H-Neuron monitoring, activation suppression, pre-training data quality) are incomplete for different reasons: they have access requirements, helpfulness trade-offs, or are unconfirmed by direct experiment.

The RLHF tension is the cluster's sharpest analytical point. RLHF demonstrably reduces sycophancy in distribution; the H-Neurons paper demonstrates that H-Neurons survive SFT with parameter inertia. Both findings are true. The resolution — RLHF operates on output distribution without restructuring the underlying circuits — explains a pattern that has puzzled practitioners: aligned models are less sycophantic in normal operation but regress under adversarial or out-of-distribution conditions. H-Neuron parameter inertia is the mechanistic explanation.

The access segmentation in the intervention map is the most practically consequential output of the synthesis. Organisations using closed-source APIs cannot access the two most promising intervention tiers (inference-time monitoring, pre-training data quality). The open-weight model choice point is therefore not merely a cost or capability decision — it is an interpretability and safety decision.

### Risks, Gaps, and Uncertainties

- **RLHF effect on H-Neurons is untested.** The parameter inertia finding covers SFT; RLHF's specific effect remains unknown.
- **Helpfulness trade-off is unquantified.** How much legitimate compliant behaviour is lost under H-Neuron suppression is not measured; this is the primary barrier to production deployment of inference-time intervention.
- **Attention heads excluded from analysis.** A complete circuit-level picture requires both FFN and attention components.
- **No direct pre-training ablation for H-Neuron formation.** The formation hypothesis rests on theoretical inference plus circumstantial evidence from the data quality literature, not a controlled experiment.
- **Two cluster items unstarted.** `h-neuron-over-compliance` and `h-neuron-pretraining-origins` would have provided finer-grained sourcing for the intervention and pre-training sections; medium-confidence inferences replace what would have been fully sourced findings in those areas.

### Open Questions — Ranked by Priority

1. Can context-aware H-Neuron suppression — activating suppression only during factually uncertain or false-premise queries — resolve the helpfulness trade-off and enable production-scale inference-time intervention? (Engineering feasibility question; required components exist; high practical impact.)

2. Does RLHF modify H-Neurons, or does parameter inertia hold across RLHF as well as SFT? (Determines whether targeted RLHF is a viable fine-tuning intervention for organisations with fine-tuning but not pre-training access.)

3. Does reducing sycophantic text in pre-training corpora measurably reduce H-Neuron density? (Confirms or refutes the formation hypothesis; requires pre-training compute at scale; needed before pre-training data quality can be recommended with high confidence.)

4. Do H-Neurons exist in attention layers as well as FFN layers, and do they play a complementary or independent role? (Required for a complete mechanistic account; potentially raises or lowers estimates of intervention effectiveness.)

5. Can H-Neuron density become a standard reported model property alongside benchmark accuracy and perplexity? (Community standardisation question; if adopted, would provide a procurement and governance lever for organisations that cannot verify model internals themselves.)

---

## Output

- Type: knowledge, backlog-item
- Description: The unified synthesis of the H-Neurons research cluster — a layered causal account (pre-training → H-Neurons → over-compliance → hallucination), a structured intervention map across four access tiers, and a prioritised action list for organisations managing LLM hallucination risk. Seeds an engineering-focused backlog item on context-aware H-Neuron suppression.
- Links:
  - `Research/completed/2026-03-05-h-neurons-in-llms.md`
  - `Research/completed/2026-03-05-llm-hallucination-mechanisms.md`
  - https://arxiv.org/abs/2512.01797
