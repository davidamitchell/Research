---
title: "Practical Limits of Large Language Model (LLM) Determinism: Temperature Zero, Fixed Seeds, and Constrained Prompts"
added: 2026-05-09T22:44:23+00:00
status: reviewing
priority: high
blocks: []
tags: [llm, governance, agentic-ai, evaluation, ai-governance]
started: 2026-05-11T10:30:26+00:00
completed: ~
output: [knowledge]
cites:
  - 2026-05-09-governance-policy-determinism-vs-stochastic-llm
  - 2026-05-09-hybrid-architecture-probabilistic-llm-deterministic-governance
  - 2026-05-09-compliance-risks-stochastic-llm-governance-decisions
related:
  - 2026-05-09-policy-as-code-guardrails-regulatory-ai-governance
  - 2026-04-30-deterministic-crr-mlr2017-risk-scoring
  - 2026-04-26-ai-lowcode-governance-enforcement-architecture
superseded_by: ~
supersedes: ~
item_type: primary
confidence: medium
versions: []
---

# Practical Limits of Large Language Model (LLM) Determinism: Temperature Zero, Fixed Seeds, and Constrained Prompts

## Research Question

What are the practical limits of making LLM (Large Language Model)-based decisions or policy enforcement deterministic, even with temperature=0, fixed seeds, and constrained prompts?

## Scope

**In scope:**
- Empirical evidence on LLM output variability at temperature=0 and with fixed random seeds
- Sources of non-determinism beyond temperature, including floating-point hardware variation, batching, model versioning, and Application Programming Interface (API) infrastructure changes
- Structural prompt-engineering techniques, including constrained output formats, JavaScript Object Notation (JSON) Schema enforcement, grammar-constrained decoding, and function calling, and their effect on reproducibility
- Implications for governance and compliance use cases requiring auditability

**Out of scope:**
- Theoretical machine-learning proofs of stochasticity; focus is applied and empirical evidence
- Non-LLM probabilistic systems except where they clarify a deterministic comparison point

**Constraints:** Focus on production-grade hosted and self-hosted LLM services from OpenAI, Anthropic, and widely used open-source inference stacks; prefer official documentation and empirical studies.

## Context

- Temperature zero and fixed seeds are often presented as the practical recipe for stable LLM behavior, but current vendor guidance already frames reproducibility as best effort rather than as a hard guarantee. [fact; source: https://cookbook.openai.com/examples/reproducible_outputs_with_the_seed_parameter; https://learn.microsoft.com/en-us/azure/ai-foundry/openai/how-to/reproducible-output]
- The operational causes of residual variation appear to sit outside prompt text alone, because serving-path batching, numerical precision, backend configuration, and model-version changes all alter the computation path seen by the same prompt. [inference; source: https://thinkingmachines.ai/blog/defeating-nondeterminism-in-llm-inference/; https://docs.vllm.ai/en/v0.7.0/getting_started/faq.html; https://pytorch.org/docs/2.11/notes/randomness.html; https://docs.anthropic.com/en/docs/about-claude/model-deprecations]
- Prior completed items in this repository already concluded that governance-grade control is strongest when model output is separated from deterministic enforcement, so this item tests how strongly current reproducibility evidence supports that architectural boundary. [fact; source: https://davidamitchell.github.io/Research/research/2026-05-09-governance-policy-determinism-vs-stochastic-llm.html; https://davidamitchell.github.io/Research/research/2026-05-09-hybrid-architecture-probabilistic-llm-deterministic-governance.html; https://davidamitchell.github.io/Research/research/2026-05-09-compliance-risks-stochastic-llm-governance-decisions.html]

## Approach

1. Review empirical studies and vendor guidance on repeated-output variability at temperature zero and under fixed-seed settings.
2. Identify residual non-determinism sources in deployed inference stacks, especially batching, floating-point behavior, model versioning, and backend changes.
3. Assess what constrained outputs, strict tool schemas, and grammar-based decoding actually guarantee, and what they do not.
4. Synthesize a practical taxonomy of determinism levels and derive governance implications for policy enforcement.

## Sources

- [x] [OpenAI Cookbook Reproducible outputs with the seed parameter](https://cookbook.openai.com/examples/reproducible_outputs_with_the_seed_parameter)
- [x] [Microsoft Learn How to generate reproducible output with Azure OpenAI](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/how-to/reproducible-output)
- [x] [Anthropic Tool use overview](https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/overview)
- [x] [Anthropic Models overview](https://docs.anthropic.com/en/docs/about-claude/models/overview)
- [x] [Anthropic Model deprecations](https://docs.anthropic.com/en/docs/about-claude/model-deprecations)
- [x] [PyTorch Reproducibility notes](https://pytorch.org/docs/2.11/notes/randomness.html)
- [x] [vLLM FAQ](https://docs.vllm.ai/en/v0.7.0/getting_started/faq.html)
- [x] [SGLang FAQ](https://docs.sglang.ai/references/faq.html)
- [x] [Thinking Machines Lab (2025) Defeating nondeterminism in LLM inference](https://thinkingmachines.ai/blog/defeating-nondeterminism-in-llm-inference/)
- [x] [Atil et al. (2025) Non-Determinism of "Deterministic" LLM Settings](https://arxiv.org/abs/2408.04667)
- [x] [Denisov-Blanch et al. (2025) Measuring Determinism in Large Language Models for Software Code Review](https://arxiv.org/abs/2502.20747)
- [x] [Nicholson (2026) Quantifying non-deterministic drift in large language models](https://arxiv.org/abs/2601.19934)
- [x] [OpenAI Developers Structured Outputs guide](https://developers.openai.com/api/docs/guides/structured-outputs)
- [x] [Microsoft Learn Structured outputs with Azure OpenAI](https://learn.microsoft.com/en-us/azure/foundry/openai/how-to/structured-outputs)
- [x] [Beurer-Kellner et al. (2023) Prompting Is Programming: A Query Language for Large Language Models](https://arxiv.org/abs/2212.06094)
- [x] [Language Model Query Language (LMQL) constraints guide](https://lmql.ai/docs/language/constraints.html)
- [x] [Geng et al. (2024) Grammar-Constrained Decoding for Structured NLP Tasks without Finetuning](https://arxiv.org/abs/2305.13971)
- [x] [Ouyang et al. (2022) Training language models to follow instructions with human feedback](https://arxiv.org/abs/2203.02155)
- [x] [Tamkin et al. (2021) Understanding the capabilities, limitations, and societal impact of Large Language Models](https://arxiv.org/abs/2102.02503)

## Related

- [Governance Policy Application: Deterministic Requirements vs Stochastic Large Language Model Elements](https://davidamitchell.github.io/Research/research/2026-05-09-governance-policy-determinism-vs-stochastic-llm.html)
- [Hybrid Architecture Design: Probabilistic Large Language Models for Interpretation, Deterministic Layers for Governance Enforcement](https://davidamitchell.github.io/Research/research/2026-05-09-hybrid-architecture-probabilistic-llm-deterministic-governance.html)
- [Compliance Risks of Relying on Stochastic Large Language Model Outputs for Governance, Privacy, and Regulatory Decisions](https://davidamitchell.github.io/Research/research/2026-05-09-compliance-risks-stochastic-llm-governance-decisions.html)

---

## Research Skill Output

*(Full output from running the research skill, retained verbatim in the completed item. Sections 0 to 5 are the investigation, and section 6 seeds the Findings section below.)*

### §0 Initialise

- Question: what are the practical limits of making LLM-based decisions or policy enforcement deterministic with temperature zero, fixed seeds, and constrained prompts?
- Scope: repeated-output stability, residual infrastructure nondeterminism, structured-output controls, and governance implications for authoritative decisions.
- Constraints: official vendor documentation and empirical studies first, then supporting engineering analysis and prior completed repository items for governance interpretation.
- Output: knowledge.
- [fact; source: https://davidamitchell.github.io/Research/research/2026-05-09-governance-policy-determinism-vs-stochastic-llm.html; https://davidamitchell.github.io/Research/research/2026-05-09-hybrid-architecture-probabilistic-llm-deterministic-governance.html; https://davidamitchell.github.io/Research/research/2026-05-09-compliance-risks-stochastic-llm-governance-decisions.html] Prior completed items in this repository already argue that deterministic enforcement and audit evidence should sit outside probabilistic model output, so this item tests whether current reproducibility evidence makes that pattern optional or necessary.

### §1 Question Decomposition

- **Root question:** how deterministic can present-day LLM systems become before residual serving-path and model-update effects reintroduce variation?
- **A. Output repeatability**
  - A1. Do current vendor documents say temperature zero or fixed seeds are fully deterministic?
  - A2. What do repeated-run empirical studies report when prompts are held constant?
- **B. Residual nondeterminism sources**
  - B1. Which mechanisms still change outputs after greedy decoding is selected?
  - B2. How do backend changes, batching, hardware paths, and model versioning affect replayability?
- **C. Constrained-output controls**
  - C1. What do structured outputs, strict tool schemas, and grammar-constrained decoding guarantee?
  - C2. Which forms of variation remain even when the output format is tightly constrained?
- **D. Governance interpretation**
  - D1. Which decision surfaces can tolerate bounded stochasticity?
  - D2. Which decision surfaces still require deterministic external enforcement?
- **E. Synthesis**
  - E1. What determinism taxonomy best fits the reviewed evidence?
  - E2. What design rule follows for policy and compliance workflows?

### §2 Investigation

#### A. Temperature zero and fixed seeds reduce variance but do not eliminate it

- [fact; source: https://cookbook.openai.com/examples/reproducible_outputs_with_the_seed_parameter] OpenAI's cookbook states that chat completions are non-deterministic by default, that `seed` offers only mostly consistent outputs, and that there remains a small chance of different responses even when the seed, parameters, and `system_fingerprint` match.
- [fact; source: https://learn.microsoft.com/en-us/azure/ai-foundry/openai/how-to/reproducible-output] Microsoft says identical Azure OpenAI calls are nondeterministic by default, that `seed` makes a best effort toward more deterministic outputs, and that determinism is still not guaranteed even when both `seed` and `system_fingerprint` stay constant.
- [fact; source: https://learn.microsoft.com/en-us/azure/ai-foundry/openai/how-to/reproducible-output] Microsoft also says longer generations generally become less deterministic, which means residual variance compounds over longer output trajectories instead of disappearing once the first token is fixed.
- [fact; source: https://arxiv.org/abs/2408.04667] Atil et al. report that five LLMs run under supposedly deterministic settings across eight tasks still showed accuracy variation up to 15 percent across natural reruns, with best-versus-worst performance gaps up to 70 percent and no model consistently reproducing identical strings.
- [fact; source: https://arxiv.org/abs/2502.20747] Denisov-Blanch et al. repeated temperature-zero code-review prompts five times across four leading models and found output variation in every model family they tested, despite clearing context and holding prompts constant.
- [fact; source: https://arxiv.org/abs/2601.19934] Nicholson reports repeated-run experiments at temperature 0.0 and 0.7 and finds that nondeterministic drift persists even at temperature 0.0, with different variability patterns by model, deployment type, and prompt category.
- [inference; source: https://cookbook.openai.com/examples/reproducible_outputs_with_the_seed_parameter; https://learn.microsoft.com/en-us/azure/ai-foundry/openai/how-to/reproducible-output; https://arxiv.org/abs/2408.04667; https://arxiv.org/abs/2502.20747; https://arxiv.org/abs/2601.19934] The shared conclusion across vendor guidance and repeated-run studies is that temperature zero and fixed seeds narrow the output distribution, but they do not create a hard identical-output guarantee for present-day LLM services.

#### B. Residual nondeterminism is driven by serving-path behavior, numerical precision, and model-change surfaces

- [fact; source: https://thinkingmachines.ai/blog/defeating-nondeterminism-in-llm-inference/] Thinking Machines Lab says LLM Application Programming Interface services and common open-source inference libraries remain non-deterministic in practice even with greedy decoding, and argues that batch-sensitive serving behavior is the main practical source of variance rather than sampling alone.
- [fact; source: https://docs.vllm.ai/en/v0.7.0/getting_started/faq.html] The vLLM FAQ says the same request can vary across runs because output log probabilities can change when batching changes, speculative decoding expands batches, or concurrent traffic alters the batch composition seen by the request.
- [fact; source: https://docs.sglang.ai/references/faq.html] The SGLang FAQ says temperature-zero requests can still diverge because dynamic batching and prefix caching dispatch different kernels, and it recommends disabling cache features and sending one request at a time to get only mostly deterministic behavior.
- [fact; source: https://pytorch.org/docs/2.11/notes/randomness.html] PyTorch says completely reproducible results are not guaranteed across releases, commits, platforms, or even central processing unit versus graphics processing unit runs with identical seeds, and also notes that deterministic modes usually reduce performance.
- [fact; source: https://cookbook.openai.com/examples/reproducible_outputs_with_the_seed_parameter; https://learn.microsoft.com/en-us/azure/ai-foundry/openai/how-to/reproducible-output] OpenAI and Microsoft both expose `system_fingerprint` precisely because backend configuration changes can alter repeatability even when prompts and seed values stay fixed.
- [fact; source: https://docs.anthropic.com/en/docs/about-claude/models/overview; https://docs.anthropic.com/en/docs/about-claude/model-deprecations] Anthropic says model identifiers are pinned snapshots or alias pointers depending on model generation, and it documents routine model deprecations and migrations, which means provider-side model lifecycle management is itself a reproducibility boundary over time.
- [inference; source: https://thinkingmachines.ai/blog/defeating-nondeterminism-in-llm-inference/; https://docs.vllm.ai/en/v0.7.0/getting_started/faq.html; https://docs.sglang.ai/references/faq.html; https://pytorch.org/docs/2.11/notes/randomness.html; https://docs.anthropic.com/en/docs/about-claude/model-deprecations] Practical replayability therefore depends on freezing more than prompt text and seeds: it also depends on batch shape, numerical pathway, software version, model snapshot, and provider update cadence.

#### C. Constrained outputs can guarantee structure, not unique meaning

- [fact; source: https://developers.openai.com/api/docs/guides/structured-outputs] OpenAI says Structured Outputs guarantee that responses adhere to the supplied JSON Schema, unlike older JSON mode which guarantees valid JSON but not schema adherence.
- [fact; source: https://learn.microsoft.com/en-us/azure/foundry/openai/how-to/structured-outputs] Microsoft says structured outputs make a model follow a supplied JSON Schema definition and recommends strict schema enforcement for function calling and complex multi-step workflows.
- [fact; source: https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/overview] Anthropic says `strict: true` in tool definitions ensures Claude tool calls match the declared schema exactly, which constrains the allowed action envelope at the tool-call boundary.
- [fact; source: https://lmql.ai/docs/language/constraints.html] The Language Model Query Language (LMQL) constraints guide says constraints are evaluated eagerly on each generated token and translated into token masks so that invalid branches fail early during generation rather than only after the full response is produced.
- [fact; source: https://arxiv.org/abs/2305.13971] Geng et al. say grammar-constrained decoding guarantees that model output follows the supplied structure and demonstrate that constrained models outperform unconstrained models on several structured natural-language-processing tasks.
- [fact; source: https://arxiv.org/abs/2212.06094] Beurer-Kellner et al. say LMQL allows constraints over model output and combines prompting with control flow so that structured decoding can be expressed as a higher-level program.
- [inference; source: https://developers.openai.com/api/docs/guides/structured-outputs; https://learn.microsoft.com/en-us/azure/foundry/openai/how-to/structured-outputs; https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/overview; https://lmql.ai/docs/language/constraints.html; https://arxiv.org/abs/2305.13971] These controls reliably improve output-structure stability by forcing responses into a typed or grammatical envelope, but they do not by themselves guarantee that the same semantic judgment, rationale, or classification will be chosen on every run.
- [inference; source: https://developers.openai.com/api/docs/guides/structured-outputs; https://arxiv.org/abs/2305.13971; https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/overview] Constrained prompting is therefore best understood as a boundary-hardening mechanism that reduces parser failures and invalid actions, not as a substitute for deterministic decision logic.

#### D. Seeded background sources frame the control problem but do not settle reproducibility on their own

- [fact; source: https://arxiv.org/abs/2203.02155] Ouyang et al. show that instruction-tuned models can improve preferred behavior and reduce some obvious failures, but the paper also says the resulting systems still make simple mistakes, which is consistent with the idea that alignment improves usefulness without creating perfect replayability.
- [fact; source: https://arxiv.org/abs/2102.02503] Tamkin et al. review the capabilities and limitations of Large Language Models and sharpen the broader case that deployment controls matter, but the paper does not provide direct repeated-run evidence about temperature-zero reproducibility.
- [inference; source: https://arxiv.org/abs/2203.02155; https://arxiv.org/abs/2102.02503] These seeded papers are useful as model-behavior background, but the determinism question depends much more directly on serving-stack evidence and repeated-run measurements than on general alignment or capability surveys.

#### E. Governance implications favor deterministic authority outside the model

- [inference; source: https://cookbook.openai.com/examples/reproducible_outputs_with_the_seed_parameter; https://learn.microsoft.com/en-us/azure/ai-foundry/openai/how-to/reproducible-output; https://arxiv.org/abs/2408.04667; https://arxiv.org/abs/2502.20747; https://arxiv.org/abs/2601.19934] Because current LLM systems still show residual variance under the very settings meant to stabilize them, policy enforcement tasks that require exact replay, contestability, or threshold-stable outcomes should not treat raw model output as the final authoritative decision.
- [inference; source: https://davidamitchell.github.io/Research/research/2026-05-09-hybrid-architecture-probabilistic-llm-deterministic-governance.html; https://davidamitchell.github.io/Research/research/2026-05-09-governance-policy-determinism-vs-stochastic-llm.html; https://davidamitchell.github.io/Research/research/2026-05-09-compliance-risks-stochastic-llm-governance-decisions.html; https://developers.openai.com/api/docs/guides/structured-outputs; https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/overview] This strengthens prior repository findings that the safest role for an LLM in governance is interpretation, extraction, summarization, or proposal generation inside a tightly constrained interface, followed by deterministic validation, policy evaluation, or explicit human approval.
- [inference; source: https://davidamitchell.github.io/Research/research/2026-05-09-policy-as-code-guardrails-regulatory-ai-governance.html; https://davidamitchell.github.io/Research/research/2026-04-30-deterministic-crr-mlr2017-risk-scoring.html; https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/overview; https://developers.openai.com/api/docs/guides/structured-outputs] The comparison point is not full-model determinism versus no control: it is whether stochastic model output is bounded strongly enough that deterministic code, versioned policy, or auditable human review still owns the side effect.

### §3 Reasoning

- [fact; source: https://cookbook.openai.com/examples/reproducible_outputs_with_the_seed_parameter; https://learn.microsoft.com/en-us/azure/ai-foundry/openai/how-to/reproducible-output; https://arxiv.org/abs/2408.04667; https://arxiv.org/abs/2502.20747; https://arxiv.org/abs/2601.19934] The strongest direct evidence says present-day LLM determinism is best-effort rather than guaranteed, even under temperature-zero and fixed-seed settings.
- [fact; source: https://thinkingmachines.ai/blog/defeating-nondeterminism-in-llm-inference/; https://docs.vllm.ai/en/v0.7.0/getting_started/faq.html; https://docs.sglang.ai/references/faq.html; https://pytorch.org/docs/2.11/notes/randomness.html] The main residual causes sit in the inference pathway, especially batching, numerical precision, cache behavior, and platform variation, which means prompt tightening alone cannot remove them.
- [fact; source: https://developers.openai.com/api/docs/guides/structured-outputs; https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/overview; https://arxiv.org/abs/2305.13971] Structured-output controls can reliably guarantee syntax or schema membership, but the reviewed sources stop short of claiming that such controls make decision content unique across runs.
- [inference; source: https://developers.openai.com/api/docs/guides/structured-outputs; https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/overview; https://cookbook.openai.com/examples/reproducible_outputs_with_the_seed_parameter; https://learn.microsoft.com/en-us/azure/ai-foundry/openai/how-to/reproducible-output] The determinism problem is therefore layered: exact same-token replay is the weakest property, stable schema-conforming structure is stronger, and fully deterministic control of side effects only becomes robust when authority sits in deterministic systems outside the model.

### §4 Consistency Check

- [fact; source: https://cookbook.openai.com/examples/reproducible_outputs_with_the_seed_parameter; https://learn.microsoft.com/en-us/azure/ai-foundry/openai/how-to/reproducible-output] No reviewed primary vendor source promises hard identical-output guarantees for hosted LLM services under temperature zero or fixed seeds.
- [fact; source: https://arxiv.org/abs/2408.04667; https://arxiv.org/abs/2502.20747; https://arxiv.org/abs/2601.19934] The repeated-run studies are consistent with the vendor best-effort language rather than contradicting it, because they document residual variance under supposedly deterministic settings.
- [fact; source: https://developers.openai.com/api/docs/guides/structured-outputs; https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/overview; https://arxiv.org/abs/2305.13971] The constrained-output sources claim structural guarantees, not unique semantic replay, so there is no unresolved contradiction between stronger format guarantees and weaker decision-content determinism.
- [inference; source: https://cookbook.openai.com/examples/reproducible_outputs_with_the_seed_parameter; https://developers.openai.com/api/docs/guides/structured-outputs; https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/overview] The remaining tension is not factual disagreement but control-layer mismatch: developers often ask prompt controls to deliver a property that only whole-system architecture can provide.

### §5 Depth and Breadth Expansion

- [inference; source: https://developers.openai.com/api/docs/guides/structured-outputs; https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/overview; https://arxiv.org/abs/2305.13971] **Technical lens:** constrained outputs move some failures from parsing time to classification time, because the system can reject malformed structure while still needing deterministic logic to decide whether a well-formed proposal should be accepted.
- [inference; source: https://cookbook.openai.com/examples/reproducible_outputs_with_the_seed_parameter; https://learn.microsoft.com/en-us/azure/ai-foundry/openai/how-to/reproducible-output; https://docs.anthropic.com/en/docs/about-claude/models/overview] **Operational lens:** audit-ready replay requires storing not only prompts and outputs but also seed, model snapshot or alias resolution, schema version, and provider metadata such as `system_fingerprint`.
- [inference; source: https://docs.sglang.ai/references/faq.html; https://docs.vllm.ai/en/v0.7.0/getting_started/faq.html; https://pytorch.org/docs/2.11/notes/randomness.html] **Economic lens:** stronger reproducibility usually trades against throughput, because single-request execution, deterministic modes, stricter numeric precision, and disabled caching reduce the batching efficiencies modern inference servers rely on.
- [inference; source: https://davidamitchell.github.io/Research/research/2026-05-09-governance-policy-determinism-vs-stochastic-llm.html; https://davidamitchell.github.io/Research/research/2026-05-09-hybrid-architecture-probabilistic-llm-deterministic-governance.html; https://davidamitchell.github.io/Research/research/2026-05-09-compliance-risks-stochastic-llm-governance-decisions.html] **Governance lens:** the reviewed evidence supports a division of labor in which LLMs can remain useful in non-authoritative interpretive stages, while deterministic policy layers and human override preserve contestability and auditability at the decision boundary.
- [inference; source: https://developers.openai.com/api/docs/guides/structured-outputs; https://learn.microsoft.com/en-us/azure/foundry/openai/how-to/structured-outputs] **Behavioral lens:** highly stable structured output can create false confidence, because a valid schema can make the system look repeatable even when the underlying classification or rationale still drifts across runs.

### §6 Synthesis

**Executive summary:**

- [fact; source: https://cookbook.openai.com/examples/reproducible_outputs_with_the_seed_parameter; https://learn.microsoft.com/en-us/azure/ai-foundry/openai/how-to/reproducible-output; https://arxiv.org/abs/2408.04667; https://arxiv.org/abs/2502.20747; https://arxiv.org/abs/2601.19934] Current LLM systems cannot be made fully deterministic for authoritative decisions just by setting temperature to zero, fixing seeds, or tightening prompts, because both vendor guidance and repeated-run studies still show residual output variance.
- [fact; source: https://thinkingmachines.ai/blog/defeating-nondeterminism-in-llm-inference/; https://docs.vllm.ai/en/v0.7.0/getting_started/faq.html; https://docs.sglang.ai/references/faq.html; https://pytorch.org/docs/2.11/notes/randomness.html] The hard limit comes from the wider inference system, especially dynamic batching, numerical precision effects, cache behavior, hardware and platform differences, and provider-controlled model or backend changes.
- [inference; source: https://developers.openai.com/api/docs/guides/structured-outputs; https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/overview; https://arxiv.org/abs/2305.13971] Constrained outputs do materially improve output-structure stability by forcing schema or grammar conformance, but they do not guarantee that the same semantic decision or rationale will be generated every time.
- [inference; source: https://davidamitchell.github.io/Research/research/2026-05-09-governance-policy-determinism-vs-stochastic-llm.html; https://davidamitchell.github.io/Research/research/2026-05-09-hybrid-architecture-probabilistic-llm-deterministic-governance.html; https://davidamitchell.github.io/Research/research/2026-05-09-compliance-risks-stochastic-llm-governance-decisions.html; https://developers.openai.com/api/docs/guides/structured-outputs] The practical design rule is therefore to keep LLMs in proposal, interpretation, or extraction roles and reserve final enforcement, thresholding, and side-effect authorization for deterministic code, versioned policy engines, or explicit human review.

**Key findings:**

1. [fact; source: https://cookbook.openai.com/examples/reproducible_outputs_with_the_seed_parameter; https://learn.microsoft.com/en-us/azure/ai-foundry/openai/how-to/reproducible-output; https://arxiv.org/abs/2408.04667; https://arxiv.org/abs/2502.20747; https://arxiv.org/abs/2601.19934] Temperature zero and fixed seeds reduce output variance in present-day LLM systems, but they do not deliver a hard identical-output guarantee across repeated runs in either vendor documentation or empirical studies.
2. [fact; source: https://thinkingmachines.ai/blog/defeating-nondeterminism-in-llm-inference/; https://docs.vllm.ai/en/v0.7.0/getting_started/faq.html; https://docs.sglang.ai/references/faq.html; https://pytorch.org/docs/2.11/notes/randomness.html] Residual nondeterminism comes from serving-path behavior and platform effects, especially batching, precision, cache use, and software or hardware differences, not only from token-sampling randomness.
3. [fact; source: https://cookbook.openai.com/examples/reproducible_outputs_with_the_seed_parameter; https://learn.microsoft.com/en-us/azure/ai-foundry/openai/how-to/reproducible-output; https://docs.anthropic.com/en/docs/about-claude/models/overview; https://docs.anthropic.com/en/docs/about-claude/model-deprecations] Provider metadata and version pinning improve traceability, but backend configuration changes, alias behavior, and routine model retirement still limit long-horizon reproducibility.
4. [fact; source: https://developers.openai.com/api/docs/guides/structured-outputs; https://learn.microsoft.com/en-us/azure/foundry/openai/how-to/structured-outputs; https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/overview; https://arxiv.org/abs/2305.13971] Structured outputs, strict tool schemas, and grammar-constrained decoding can guarantee valid structure or schema adherence, which materially narrows the action surface exposed to downstream systems.
5. [inference; source: https://developers.openai.com/api/docs/guides/structured-outputs; https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/overview; https://lmql.ai/docs/language/constraints.html; https://arxiv.org/abs/2305.13971] Structural guarantees do not imply semantic determinism, because multiple different classifications, rationales, or recommendations can still satisfy the same schema or grammar.
6. [inference; source: https://docs.sglang.ai/references/faq.html; https://docs.vllm.ai/en/v0.7.0/getting_started/faq.html; https://pytorch.org/docs/2.11/notes/randomness.html] Stronger reproducibility is achievable only by controlling the wider inference environment, often by sacrificing throughput through single-request execution, deterministic modes, stricter numeric settings, or disabled caching.
7. [inference; source: https://davidamitchell.github.io/Research/research/2026-05-09-hybrid-architecture-probabilistic-llm-deterministic-governance.html; https://davidamitchell.github.io/Research/research/2026-05-09-policy-as-code-guardrails-regulatory-ai-governance.html; https://developers.openai.com/api/docs/guides/structured-outputs; https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/overview] Governance-grade designs should therefore treat the LLM as a bounded proposal engine whose outputs are validated, normalized, and then passed to deterministic rules or human approval before any authoritative side effect occurs.
8. [inference; source: https://davidamitchell.github.io/Research/research/2026-05-09-governance-policy-determinism-vs-stochastic-llm.html; https://davidamitchell.github.io/Research/research/2026-05-09-compliance-risks-stochastic-llm-governance-decisions.html; https://arxiv.org/abs/2408.04667; https://arxiv.org/abs/2601.19934] The most useful practical taxonomy separates exact same-token replay, stable schema-conforming structure, and deterministic control of side effects, with current tools improving the second far more reliably than the first and deterministic external enforcement remaining the only robust route to the third.

**Evidence map:**

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [fact] Temperature zero and fixed seeds do not guarantee identical outputs across repeated runs. | https://cookbook.openai.com/examples/reproducible_outputs_with_the_seed_parameter; https://learn.microsoft.com/en-us/azure/ai-foundry/openai/how-to/reproducible-output; https://arxiv.org/abs/2408.04667; https://arxiv.org/abs/2502.20747; https://arxiv.org/abs/2601.19934 | high | Vendor guidance plus repeated-run studies |
| [fact] Residual nondeterminism is driven by serving-path and platform effects, not only sampling randomness. | https://thinkingmachines.ai/blog/defeating-nondeterminism-in-llm-inference/; https://docs.vllm.ai/en/v0.7.0/getting_started/faq.html; https://docs.sglang.ai/references/faq.html; https://pytorch.org/docs/2.11/notes/randomness.html | high | Strong multi-source convergence |
| [fact] Provider metadata and model versioning improve traceability but do not freeze long-horizon reproducibility. | https://cookbook.openai.com/examples/reproducible_outputs_with_the_seed_parameter; https://learn.microsoft.com/en-us/azure/ai-foundry/openai/how-to/reproducible-output; https://docs.anthropic.com/en/docs/about-claude/models/overview; https://docs.anthropic.com/en/docs/about-claude/model-deprecations | high | Backend and lifecycle evidence |
| [fact] Structured outputs and grammar constraints guarantee structure or schema adherence. | https://developers.openai.com/api/docs/guides/structured-outputs; https://learn.microsoft.com/en-us/azure/foundry/openai/how-to/structured-outputs; https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/overview; https://arxiv.org/abs/2305.13971 | high | Direct documentation plus paper |
| [inference] Structural guarantees do not guarantee the same semantic decision on every run. | https://developers.openai.com/api/docs/guides/structured-outputs; https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/overview; https://lmql.ai/docs/language/constraints.html; https://arxiv.org/abs/2305.13971 | medium | Derived from scope of guarantees |
| [inference] Stronger reproducibility requires controlling the full inference environment and usually reduces throughput. | https://docs.sglang.ai/references/faq.html; https://docs.vllm.ai/en/v0.7.0/getting_started/faq.html; https://pytorch.org/docs/2.11/notes/randomness.html | medium | Operational trade-off inference |
| [inference] Governance workflows should keep LLMs at the proposal layer and route authority through deterministic validation or review. | https://davidamitchell.github.io/Research/research/2026-05-09-hybrid-architecture-probabilistic-llm-deterministic-governance.html; https://davidamitchell.github.io/Research/research/2026-05-09-policy-as-code-guardrails-regulatory-ai-governance.html; https://developers.openai.com/api/docs/guides/structured-outputs; https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/overview | medium | External evidence plus repository synthesis |
| [inference] Stable schema-conforming structure is more achievable than exact same-token replay, while deterministic side-effect control still depends on deterministic external systems. | https://davidamitchell.github.io/Research/research/2026-05-09-governance-policy-determinism-vs-stochastic-llm.html; https://davidamitchell.github.io/Research/research/2026-05-09-compliance-risks-stochastic-llm-governance-decisions.html; https://arxiv.org/abs/2408.04667; https://arxiv.org/abs/2601.19934 | medium | Taxonomy synthesis |

**Assumptions:**

- [assumption; source: https://cookbook.openai.com/examples/reproducible_outputs_with_the_seed_parameter; https://learn.microsoft.com/en-us/azure/ai-foundry/openai/how-to/reproducible-output; https://docs.vllm.ai/en/v0.7.0/getting_started/faq.html; https://docs.sglang.ai/references/faq.html] This item assumes that vendor-hosted and self-hosted inference systems can be compared at the mechanism level because both expose similar failure patterns around batching, backend drift, and numeric precision, even though their exact implementations differ.
- [assumption; source: https://developers.openai.com/api/docs/guides/structured-outputs; https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/overview; https://arxiv.org/abs/2305.13971] This item assumes that semantic variation within a valid schema remains operationally relevant for governance decisions, even when the constrained-output sources primarily prove structural rather than semantic properties.

**Analysis:**

- [inference; source: https://cookbook.openai.com/examples/reproducible_outputs_with_the_seed_parameter; https://learn.microsoft.com/en-us/azure/ai-foundry/openai/how-to/reproducible-output; https://arxiv.org/abs/2408.04667; https://arxiv.org/abs/2502.20747; https://arxiv.org/abs/2601.19934] The evidence weighs heavily against a simple prompt-level fix, because the sources that directly measure or document repeated outputs all stop at best-effort stability rather than guaranteeing identical replay.
- [inference; source: https://thinkingmachines.ai/blog/defeating-nondeterminism-in-llm-inference/; https://docs.vllm.ai/en/v0.7.0/getting_started/faq.html; https://docs.sglang.ai/references/faq.html; https://pytorch.org/docs/2.11/notes/randomness.html] The causal story is strongest when serving-stack and framework evidence are combined: numerical drift matters, but it becomes practically visible because modern inference systems optimize for shared throughput rather than isolated single-request determinism.
- [inference; source: https://developers.openai.com/api/docs/guides/structured-outputs; https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/overview; https://arxiv.org/abs/2305.13971] Structured outputs still matter operationally, because they convert a broad natural-language response space into a typed proposal surface that can be deterministically validated, logged, rejected, or escalated by downstream systems.
- [inference; source: https://davidamitchell.github.io/Research/research/2026-05-09-hybrid-architecture-probabilistic-llm-deterministic-governance.html; https://davidamitchell.github.io/Research/research/2026-05-09-policy-as-code-guardrails-regulatory-ai-governance.html; https://davidamitchell.github.io/Research/research/2026-05-09-governance-policy-determinism-vs-stochastic-llm.html] The most defensible architectural response is therefore layered control: stabilize what can be stabilized, constrain the proposal shape, and move final authority to deterministic policy logic or accountable human review where replay and contestability actually matter.

**Risks, gaps, uncertainties:**

- [inference; source: https://cookbook.openai.com/examples/reproducible_outputs_with_the_seed_parameter; https://learn.microsoft.com/en-us/azure/ai-foundry/openai/how-to/reproducible-output] The major vendors reviewed here document best-effort reproducibility, but they do not publish a hard service-level guarantee for identical outputs under controlled settings, so the exact upper bound of reproducibility remains unspecified.
- [inference; source: https://arxiv.org/abs/2408.04667; https://arxiv.org/abs/2502.20747; https://arxiv.org/abs/2601.19934] The empirical literature on temperature-zero drift is still young and concentrated in benchmark or repeated-run settings rather than in long-lived enterprise production workloads.
- [inference; source: https://docs.sglang.ai/references/faq.html; https://docs.vllm.ai/en/v0.7.0/getting_started/faq.html] Open-source inference stacks are evolving quickly, including newly introduced deterministic modes, so some practical limits described here may improve as server implementations mature.
- [inference; source: https://developers.openai.com/api/docs/guides/structured-outputs; https://arxiv.org/abs/2305.13971] The reviewed structured-output sources prove structural validity more clearly than they prove decision-quality stability, so semantic determinism under schema constraints remains an open empirical question.

**Open questions:**

- [inference; source: https://docs.sglang.ai/references/faq.html; https://docs.vllm.ai/en/v0.7.0/getting_started/faq.html] How close can modern deterministic inference modes get to stable semantic classifications under realistic concurrent enterprise workloads rather than single-request laboratory conditions?
- [inference; source: https://developers.openai.com/api/docs/guides/structured-outputs; https://arxiv.org/abs/2305.13971] Which constrained-decoding patterns most effectively reduce semantic drift in policy-classification tasks, not just parser failures or malformed tool calls?
- [inference; source: https://cookbook.openai.com/examples/reproducible_outputs_with_the_seed_parameter; https://docs.anthropic.com/en/docs/about-claude/model-deprecations] What provider controls, if any, will emerge for regulated workloads that need longer-lived reproducibility guarantees across backend and model lifecycle changes?

### §7 Recursive Review

```text
review_result: ready-for-workflow-review
checked:
  - prior-work sweep
  - acronym expansion
  - claim labels
  - findings parity
confidence: medium
```

---

## Findings

### Executive Summary

Current LLM policy or compliance decisions cannot be made fully deterministic just by setting temperature to zero, fixing seeds, or tightening prompts. [fact; source: https://cookbook.openai.com/examples/reproducible_outputs_with_the_seed_parameter; https://learn.microsoft.com/en-us/azure/ai-foundry/openai/how-to/reproducible-output; https://arxiv.org/abs/2408.04667; https://arxiv.org/abs/2502.20747; https://arxiv.org/abs/2601.19934]

Official OpenAI and Microsoft guidance describe reproducibility controls as best effort, and repeated-run studies report residual variance even when prompts are held constant under temperature-zero or fixed-seed settings. [fact; source: https://cookbook.openai.com/examples/reproducible_outputs_with_the_seed_parameter; https://learn.microsoft.com/en-us/azure/ai-foundry/openai/how-to/reproducible-output; https://arxiv.org/abs/2408.04667; https://arxiv.org/abs/2502.20747; https://arxiv.org/abs/2601.19934]

Constrained outputs, strict tool schemas, and grammar-constrained decoding materially improve structural consistency by forcing valid schemas or grammars, but they do not guarantee that the same semantic judgment or rationale will recur on every run. [inference; source: https://developers.openai.com/api/docs/guides/structured-outputs; https://learn.microsoft.com/en-us/azure/foundry/openai/how-to/structured-outputs; https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/overview; https://arxiv.org/abs/2305.13971]

For governance use cases, the practical boundary is to keep LLMs at the proposal or interpretation layer and route final enforcement through deterministic rules, versioned policy engines, or explicit human approval. [inference; source: https://davidamitchell.github.io/Research/research/2026-05-09-governance-policy-determinism-vs-stochastic-llm.html; https://davidamitchell.github.io/Research/research/2026-05-09-hybrid-architecture-probabilistic-llm-deterministic-governance.html; https://davidamitchell.github.io/Research/research/2026-05-09-compliance-risks-stochastic-llm-governance-decisions.html; https://developers.openai.com/api/docs/guides/structured-outputs]

### Key Findings

1. **Temperature zero and fixed seeds reduce output variance in present-day LLM systems, but they do not deliver a hard identical-output guarantee across repeated runs in either vendor documentation or empirical studies.** ([fact]; high confidence; source: https://cookbook.openai.com/examples/reproducible_outputs_with_the_seed_parameter; https://learn.microsoft.com/en-us/azure/ai-foundry/openai/how-to/reproducible-output; https://arxiv.org/abs/2408.04667; https://arxiv.org/abs/2502.20747; https://arxiv.org/abs/2601.19934)
2. **Residual nondeterminism comes from serving-path behavior and platform effects, especially batching, numerical precision, cache use, and software or hardware differences, not only from token-sampling randomness.** ([fact]; high confidence; source: https://thinkingmachines.ai/blog/defeating-nondeterminism-in-llm-inference/; https://docs.vllm.ai/en/v0.7.0/getting_started/faq.html; https://docs.sglang.ai/references/faq.html; https://pytorch.org/docs/2.11/notes/randomness.html)
3. **Provider metadata and version pinning improve traceability, but backend configuration changes, alias behavior, and routine model retirement still limit long-horizon reproducibility.** ([fact]; high confidence; source: https://cookbook.openai.com/examples/reproducible_outputs_with_the_seed_parameter; https://learn.microsoft.com/en-us/azure/ai-foundry/openai/how-to/reproducible-output; https://docs.anthropic.com/en/docs/about-claude/models/overview; https://docs.anthropic.com/en/docs/about-claude/model-deprecations)
4. **Structured outputs, strict tool schemas, and grammar-constrained decoding can guarantee valid structure or schema adherence, which materially narrows the action surface exposed to downstream systems.** ([fact]; high confidence; source: https://developers.openai.com/api/docs/guides/structured-outputs; https://learn.microsoft.com/en-us/azure/foundry/openai/how-to/structured-outputs; https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/overview; https://arxiv.org/abs/2305.13971)
5. **Structural guarantees do not imply semantic determinism, because multiple different classifications, rationales, or recommendations can still satisfy the same schema or grammar.** ([inference]; medium confidence; source: https://developers.openai.com/api/docs/guides/structured-outputs; https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/overview; https://lmql.ai/docs/language/constraints.html; https://arxiv.org/abs/2305.13971)
6. **Stronger reproducibility is achievable only by controlling the wider inference environment, often by sacrificing throughput through single-request execution, deterministic modes, stricter numeric settings, or disabled caching.** ([inference]; medium confidence; source: https://docs.sglang.ai/references/faq.html; https://docs.vllm.ai/en/v0.7.0/getting_started/faq.html; https://pytorch.org/docs/2.11/notes/randomness.html)
7. **Governance-grade designs should therefore treat the LLM as a bounded proposal engine whose outputs are validated, normalized, and then passed to deterministic rules or human approval before any authoritative side effect occurs.** ([inference]; medium confidence; source: https://davidamitchell.github.io/Research/research/2026-05-09-hybrid-architecture-probabilistic-llm-deterministic-governance.html; https://davidamitchell.github.io/Research/research/2026-05-09-policy-as-code-guardrails-regulatory-ai-governance.html; https://developers.openai.com/api/docs/guides/structured-outputs; https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/overview)
8. **The most useful practical taxonomy separates exact same-token replay, stable schema-conforming structure, and deterministic control of side effects, with current tools improving the second far more reliably than the first and deterministic external enforcement remaining the only robust route to the third.** ([inference]; medium confidence; source: https://davidamitchell.github.io/Research/research/2026-05-09-governance-policy-determinism-vs-stochastic-llm.html; https://davidamitchell.github.io/Research/research/2026-05-09-compliance-risks-stochastic-llm-governance-decisions.html; https://arxiv.org/abs/2408.04667; https://arxiv.org/abs/2601.19934)

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [fact] Temperature zero and fixed seeds do not guarantee identical outputs across repeated runs. | https://cookbook.openai.com/examples/reproducible_outputs_with_the_seed_parameter; https://learn.microsoft.com/en-us/azure/ai-foundry/openai/how-to/reproducible-output; https://arxiv.org/abs/2408.04667; https://arxiv.org/abs/2502.20747; https://arxiv.org/abs/2601.19934 | high | Vendor guidance plus repeated-run studies |
| [fact] Residual nondeterminism is driven by serving-path and platform effects, not only sampling randomness. | https://thinkingmachines.ai/blog/defeating-nondeterminism-in-llm-inference/; https://docs.vllm.ai/en/v0.7.0/getting_started/faq.html; https://docs.sglang.ai/references/faq.html; https://pytorch.org/docs/2.11/notes/randomness.html | high | Strong multi-source convergence |
| [fact] Provider metadata and model versioning improve traceability but do not freeze long-horizon reproducibility. | https://cookbook.openai.com/examples/reproducible_outputs_with_the_seed_parameter; https://learn.microsoft.com/en-us/azure/ai-foundry/openai/how-to/reproducible-output; https://docs.anthropic.com/en/docs/about-claude/models/overview; https://docs.anthropic.com/en/docs/about-claude/model-deprecations | high | Backend and lifecycle evidence |
| [fact] Structured outputs and grammar constraints guarantee structure or schema adherence. | https://developers.openai.com/api/docs/guides/structured-outputs; https://learn.microsoft.com/en-us/azure/foundry/openai/how-to/structured-outputs; https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/overview; https://arxiv.org/abs/2305.13971 | high | Direct documentation plus paper |
| [inference] Structural guarantees do not guarantee the same semantic decision on every run. | https://developers.openai.com/api/docs/guides/structured-outputs; https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/overview; https://lmql.ai/docs/language/constraints.html; https://arxiv.org/abs/2305.13971 | medium | Derived from scope of guarantees |
| [inference] Stronger reproducibility requires controlling the full inference environment and usually reduces throughput. | https://docs.sglang.ai/references/faq.html; https://docs.vllm.ai/en/v0.7.0/getting_started/faq.html; https://pytorch.org/docs/2.11/notes/randomness.html | medium | Operational trade-off inference |
| [inference] Governance workflows should keep LLMs at the proposal layer and route authority through deterministic validation or review. | https://davidamitchell.github.io/Research/research/2026-05-09-hybrid-architecture-probabilistic-llm-deterministic-governance.html; https://davidamitchell.github.io/Research/research/2026-05-09-policy-as-code-guardrails-regulatory-ai-governance.html; https://developers.openai.com/api/docs/guides/structured-outputs; https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/overview | medium | External evidence plus repository synthesis |
| [inference] Stable schema-conforming structure is more achievable than exact same-token replay, while deterministic side-effect control still depends on deterministic external systems. | https://davidamitchell.github.io/Research/research/2026-05-09-governance-policy-determinism-vs-stochastic-llm.html; https://davidamitchell.github.io/Research/research/2026-05-09-compliance-risks-stochastic-llm-governance-decisions.html; https://arxiv.org/abs/2408.04667; https://arxiv.org/abs/2601.19934 | medium | Taxonomy synthesis |

### Assumptions

- Cross-provider hosted and self-hosted systems are compared at the mechanism level in this item, so the synthesis assumes that shared failure patterns around batching, backend drift, and numeric precision are comparable enough to support a practical governance conclusion. [assumption; source: https://cookbook.openai.com/examples/reproducible_outputs_with_the_seed_parameter; https://learn.microsoft.com/en-us/azure/ai-foundry/openai/how-to/reproducible-output; https://docs.vllm.ai/en/v0.7.0/getting_started/faq.html; https://docs.sglang.ai/references/faq.html]
- Semantic variation inside a valid schema is treated as operationally material for governance decisions, even though the structured-output sources mainly prove structural rather than semantic properties. [assumption; source: https://developers.openai.com/api/docs/guides/structured-outputs; https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/overview; https://arxiv.org/abs/2305.13971]

### Analysis

The direct evidence weighs against a prompt-only solution, because both vendor guidance and repeated-run studies stop at best-effort stability rather than promising identical replay. [inference; source: https://cookbook.openai.com/examples/reproducible_outputs_with_the_seed_parameter; https://learn.microsoft.com/en-us/azure/ai-foundry/openai/how-to/reproducible-output; https://arxiv.org/abs/2408.04667; https://arxiv.org/abs/2502.20747; https://arxiv.org/abs/2601.19934]

The causal explanation is strongest when serving-stack and framework sources are combined, because numerical drift becomes practically visible only through throughput-oriented batching, cache behavior, and platform selection inside modern inference systems. [inference; source: https://thinkingmachines.ai/blog/defeating-nondeterminism-in-llm-inference/; https://docs.vllm.ai/en/v0.7.0/getting_started/faq.html; https://docs.sglang.ai/references/faq.html; https://pytorch.org/docs/2.11/notes/randomness.html]

Structured outputs still matter, because they turn free-form model responses into typed proposals that downstream deterministic systems can validate, reject, escalate, or log consistently even when the model itself remains partially stochastic. [inference; source: https://developers.openai.com/api/docs/guides/structured-outputs; https://learn.microsoft.com/en-us/azure/foundry/openai/how-to/structured-outputs; https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/overview]

This item therefore sharpens rather than overturns prior repository work: stabilize what can be stabilized, constrain the proposal shape, and move final authority to deterministic policy logic or accountable human review where replay and contestability actually matter. [inference; source: https://davidamitchell.github.io/Research/research/2026-05-09-governance-policy-determinism-vs-stochastic-llm.html; https://davidamitchell.github.io/Research/research/2026-05-09-hybrid-architecture-probabilistic-llm-deterministic-governance.html; https://davidamitchell.github.io/Research/research/2026-05-09-policy-as-code-guardrails-regulatory-ai-governance.html]

### Risks, Gaps, and Uncertainties

- Major vendors document best-effort reproducibility, but the reviewed primary sources do not publish a hard service-level guarantee for identical outputs under controlled settings, so the exact reproducibility ceiling remains unspecified. [inference; source: https://cookbook.openai.com/examples/reproducible_outputs_with_the_seed_parameter; https://learn.microsoft.com/en-us/azure/ai-foundry/openai/how-to/reproducible-output]
- The empirical literature on temperature-zero drift is still young and concentrated in repeated-run experiments rather than long-lived enterprise production workloads, so operational variance under real policy traffic remains only partially mapped. [inference; source: https://arxiv.org/abs/2408.04667; https://arxiv.org/abs/2502.20747; https://arxiv.org/abs/2601.19934]
- Open-source inference stacks are evolving quickly, including newly introduced deterministic modes, so some current practical limits may shift as server implementations mature. [inference; source: https://docs.sglang.ai/references/faq.html; https://docs.vllm.ai/en/v0.7.0/getting_started/faq.html]
- The reviewed structured-output sources prove structural validity more clearly than decision-quality stability, so semantic determinism under schema constraints remains an open empirical question. [inference; source: https://developers.openai.com/api/docs/guides/structured-outputs; https://arxiv.org/abs/2305.13971]

### Open Questions

- How close can current deterministic inference modes get to stable semantic classifications under realistic concurrent enterprise workloads rather than single-request laboratory conditions? [inference; source: https://docs.sglang.ai/references/faq.html; https://docs.vllm.ai/en/v0.7.0/getting_started/faq.html]
- Which constrained-decoding patterns most effectively reduce semantic drift in policy-classification tasks, not just malformed output or invalid tool calls? [inference; source: https://developers.openai.com/api/docs/guides/structured-outputs; https://arxiv.org/abs/2305.13971]
- What provider controls, if any, will emerge for regulated workloads that need longer-lived reproducibility guarantees across backend and model lifecycle changes? [inference; source: https://cookbook.openai.com/examples/reproducible_outputs_with_the_seed_parameter; https://docs.anthropic.com/en/docs/about-claude/model-deprecations]

---

## Output

- Type: knowledge
- Description: This item establishes a practical determinism taxonomy for LLM systems and concludes that current controls improve replayability and structural validity but still require deterministic external enforcement for authoritative policy decisions. [inference; source: https://arxiv.org/abs/2408.04667; https://developers.openai.com/api/docs/guides/structured-outputs; https://davidamitchell.github.io/Research/research/2026-05-09-hybrid-architecture-probabilistic-llm-deterministic-governance.html]
- Links:
  - https://learn.microsoft.com/en-us/azure/ai-foundry/openai/how-to/reproducible-output
  - https://cookbook.openai.com/examples/reproducible_outputs_with_the_seed_parameter
  - https://thinkingmachines.ai/blog/defeating-nondeterminism-in-llm-inference/
