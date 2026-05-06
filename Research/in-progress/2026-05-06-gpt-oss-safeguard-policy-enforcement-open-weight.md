---
title: "How do open-weight policy enforcement reasoning models, exemplified by OpenAI's gpt-oss-safeguard, classify text against customizable policies, and what are their deployment trade-offs compared to rule-based and closed Application Programming Interface (API) guardrail approaches?"
added: 2026-05-06T09:49:53+00:00
status: reviewing
priority: high
blocks: [2026-05-06-fact-checking-tools-research-quality-improvement]
tags: [llm, evaluation, workflow, agentic-ai]
started: 2026-05-06T12:26:01+00:00
completed: ~
output: [knowledge]
cites: [2026-04-26-policy-coherence-machine-checkable-prerequisite, 2026-04-26-deployment-pipeline-citizen-development-governed-gate, 2026-05-02-hitl-review-volume-bottleneck-rubber-stamp]
related: [2026-03-02-research-quality-assurance-methodology, 2026-04-28-llm-as-judge-pipeline-validation-checkpoints, 2026-05-02-adversarial-review-methods-ai-research-quality, 2026-05-06-openfactcheck-ai-fact-checking-pipeline, 2026-05-06-loki-fact-checking-journalists-moderation, 2026-05-06-factscore-precision-scoring-atomic-claims, 2026-05-06-barnum-statements-ai-responses-theory-practice, 2026-05-06-fact-checking-tools-research-quality-improvement]
superseded_by: ~
supersedes: ~
item_type: primary
confidence: medium
versions: []
---

# How do open-weight policy enforcement reasoning models, exemplified by OpenAI's gpt-oss-safeguard, classify text against customizable policies, and what are their deployment trade-offs compared to rule-based and closed Application Programming Interface (API) guardrail approaches?

## Research Question

How do open-weight, meaning released-weight and self-hostable, policy enforcement reasoning models, exemplified by OpenAI's gpt-oss-safeguard, classify text against strict, customizable policies, and what are their capabilities, deployment models, and trade-offs compared to rule-based classifiers and closed Application Programming Interface (API) guardrail approaches for enforcing quality and content standards on Artificial Intelligence (AI)-generated research text?

## Scope

**In scope:**
- gpt-oss-safeguard architecture: how it is packaged, what policy specification format it accepts, how it reasons about compliance, and what outputs it is designed to produce
- Comparison with rule-based classifiers, such as keyword and regular-expression filters, and with closed-API guardrails, such as OpenAI Moderation and Anthropic Constitutional AI related safety controls, on customizability, latency, accuracy claims, and deployment model
- Open-weight licensing implications: ability to self-host, inspect, and adapt policies without sending text to a third-party moderation endpoint
- Policy specification: how policies are defined, what constraint types are supported, and what official guidance exists on policy length, examples, categories, and output schemas
- Evaluation: what precision, recall, F1, benchmark, and failure-mode evidence is publicly available in accessible official materials
- Deployment patterns: inference requirements, quantized local deployment guidance, and feasibility inside a GitHub Actions review pipeline
- Failure modes: policy types that official materials say degrade accuracy, and which parts of the repository's research review rubric remain beyond machine-checkable enforcement

**Out of scope:**
- General Large Language Model (LLM) safety research unrelated to policy classification
- Human-only moderation programs
- Broader legal or regulatory compliance frameworks beyond what is needed to reason about deployment trade-offs

**Constraints:**
- The item must resolve the exact model identity before using the name gpt-oss-safeguard as an evidence-bearing term
- Primary sources should dominate: official OpenAI repository, OpenAI guides, official documentation, and official papers
- Where official public materials omit numeric evaluation detail, the gap must be stated explicitly rather than filled with secondary summaries

## Context

- [fact; source: https://davidamitchell.github.io/Research/research/2026-04-26-policy-coherence-machine-checkable-prerequisite.html; https://davidamitchell.github.io/Research/research/2026-04-26-deployment-pipeline-citizen-development-governed-gate.html] Prior completed items in this corpus establish that machine-checkable governance works best when policies are explicit and the deployment pipeline is the strongest enforceable control surface.
- [fact; source: https://davidamitchell.github.io/Research/research/2026-05-02-hitl-review-volume-bottleneck-rubber-stamp.html] Prior work on human-in-the-loop review shows that line-by-line human checking breaks down at volume, which makes selective automation and risk-tiered escalation relevant to any proposed policy-enforcement layer.
- [inference; source: https://cookbook.openai.com/articles/gpt-oss-safeguard-guide; https://github.com/openai/gpt-oss-safeguard/blob/main/README.md; https://developers.openai.com/api/docs/guides/moderation] This item therefore tests whether an open-weight policy reasoner can occupy the middle layer between cheap structural checks and expensive human review, while still fitting the latency and hosting constraints of this repository's review workflow.

## Approach

1. **Model identification and disambiguation:** Resolve whether gpt-oss-safeguard is an official released model family and document its exact package surfaces.
2. **Architecture and policy format:** Extract how the model is presented, invoked, prompted, and configured, including Harmony format and reasoning-effort controls.
3. **Evaluation and failure modes:** Record any official metrics, benchmark statements, and explicit degradation conditions available in accessible public materials.
4. **Comparison with alternatives:** Compare gpt-oss-safeguard with rule-based filters, OpenAI Moderation, Anthropic Constitutional AI related controls, Llama Guard, and NeMo Guardrails.
5. **Deployment feasibility:** Assess whether default GitHub-hosted runners can run the model and what hosting patterns are realistic instead.
6. **Research review applicability:** Map the repository's review rubric into machine-checkable rules, policy-reasoning rules, and residual human-judgment checks.

## Sources

- [x] [OpenAI gpt-oss-safeguard repository README](https://github.com/openai/gpt-oss-safeguard/blob/main/README.md) - official model family description, parameter counts, Harmony requirement, and positioning
- [x] [OpenAI (2025) gpt-oss-safeguard guide](https://cookbook.openai.com/articles/gpt-oss-safeguard-guide) - official policy-writing guidance, deployment patterns, and latency trade-off guidance
- [x] [OpenAI (2025) gpt-oss-safeguard-20b model card README](https://huggingface.co/openai/gpt-oss-safeguard-20b/raw/main/README.md) - official 20B model details, 16 GB Virtual Random Access Memory (VRAM) guidance, and Apache 2.0 metadata
- [x] [OpenAI (2025) gpt-oss-safeguard-120b model card README](https://huggingface.co/openai/gpt-oss-safeguard-120b/raw/main/README.md) - official 120B model details and single H100 guidance
- [x] [OpenAI gpt-oss-safeguard spam policy example](https://github.com/openai/gpt-oss-safeguard/blob/main/example_policies/spam/policy.txt) - official example of policy structure, escalation rules, and output labels
- [x] [OpenAI gpt-oss-safeguard spam golden dataset](https://github.com/openai/gpt-oss-safeguard/blob/main/example_policies/spam/golden_dataset.csv) - official example dataset with public accuracy, precision, recall, and F1
- [x] [OpenAI Moderation guide](https://developers.openai.com/api/docs/guides/moderation) - official fixed-category closed-API moderation surface
- [x] [OpenAI (2025) Run gpt-oss locally with Ollama](https://cookbook.openai.com/articles/gpt-oss/run-locally-ollama) - official consumer-hardware and offload guidance
- [x] [OpenAI (2025) Run gpt-oss with LM Studio](https://cookbook.openai.com/articles/gpt-oss/run-locally-lmstudio) - official local hardware guidance
- [x] [Inan et al. (2023) Llama Guard: LLM-based Input-Output Safeguard for Human-AI Conversations](https://arxiv.org/abs/2312.06674) - open-weight safeguard baseline and comparison source
- [x] [Rebedea et al. (2023) NeMo Guardrails: A Toolkit for Controllable and Safe LLM Applications](https://arxiv.org/abs/2310.10501) - programmable runtime guardrails baseline
- [x] [Anthropic (2022) Constitutional AI: Harmlessness from AI Feedback](https://www.anthropic.com/research/constitutional-ai-harmlessness-from-ai-feedback) - official Constitutional AI method description
- [x] [Anthropic Claude's Constitution](https://www.anthropic.com/constitution) - official published constitution and design philosophy
- [x] [GitHub-hosted runners reference](https://docs.github.com/en/actions/reference/runners/github-hosted-runners) - official default runner hardware and Graphics Processing Unit (GPU) availability
- [x] [Mitchell (2026) Policy coherence as a machine-checkable prerequisite](https://davidamitchell.github.io/Research/research/2026-04-26-policy-coherence-machine-checkable-prerequisite.html) - prior repository evidence on machine-checkable policy preconditions
- [x] [Mitchell (2026) Deployment pipeline as the only enforceable control gate](https://davidamitchell.github.io/Research/research/2026-04-26-deployment-pipeline-citizen-development-governed-gate.html) - prior repository evidence on pipeline enforcement
- [x] [Mitchell (2026) How should human-in-the-loop design be adapted when AI review volume makes human reviewers a bottleneck or causes rubber-stamping?](https://davidamitchell.github.io/Research/research/2026-05-02-hitl-review-volume-bottleneck-rubber-stamp.html) - prior repository evidence on selective intervention and review overload

## Related

- [Mitchell (2026) Policy coherence as a machine-checkable prerequisite](https://davidamitchell.github.io/Research/research/2026-04-26-policy-coherence-machine-checkable-prerequisite.html)
- [Mitchell (2026) Deployment pipeline as the only enforceable control gate](https://davidamitchell.github.io/Research/research/2026-04-26-deployment-pipeline-citizen-development-governed-gate.html)
- [Mitchell (2026) Large Language Model as judge as pipeline validation checkpoints](https://davidamitchell.github.io/Research/research/2026-04-28-llm-as-judge-pipeline-validation-checkpoints.html)

---

## Research Skill Output

### §0 Initialise

- Question: How do OpenAI's gpt-oss-safeguard models classify text against developer-supplied policies, and when are they preferable to rule-based filters or closed-API guardrails?
- Scope: Model identity, policy format, accessible evaluation evidence, deployment constraints, and fit for this repository's review workflow.
- Constraints: Use accessible official materials; do not invent benchmark numbers absent from public sources.
- Output: knowledge
- [fact; source: https://github.com/openai/gpt-oss-safeguard/blob/main/README.md; https://huggingface.co/openai/gpt-oss-safeguard-20b/raw/main/README.md; https://huggingface.co/openai/gpt-oss-safeguard-120b/raw/main/README.md] The exact model name resolves cleanly to an official OpenAI repository plus two released model surfaces, gpt-oss-safeguard-20b and gpt-oss-safeguard-120b, so no fallback disambiguation was required.
- [fact; source: https://davidamitchell.github.io/Research/research/2026-04-26-policy-coherence-machine-checkable-prerequisite.html; https://davidamitchell.github.io/Research/research/2026-04-26-deployment-pipeline-citizen-development-governed-gate.html; https://davidamitchell.github.io/Research/research/2026-05-02-hitl-review-volume-bottleneck-rubber-stamp.html] Prior completed work already establishes the relevant governance surfaces, explicit policy structure, pipeline gating, and human-review bottlenecks, so this item focuses on whether a released-weight policy reasoner can be a practical enforcement component inside that existing control stack.

### §1 Question Decomposition

- **Root question:** What does gpt-oss-safeguard actually do, and what trade-offs follow from using it as a policy-enforcement layer?
  - **A. Model identity and architecture**
    - A1. What official artifacts define the model family?
    - A2. What sizes, parameter counts, and inference interfaces are documented?
  - **B. Policy specification and outputs**
    - B1. How is a developer-supplied policy represented?
    - B2. What output schemas and reasoning controls are supported?
    - B3. What policy-length and multi-policy limits are documented?
  - **C. Evaluation evidence**
    - C1. Which public metrics are directly accessible?
    - C2. Which failure or degradation conditions are acknowledged in official materials?
  - **D. Comparison with alternatives**
    - D1. How does it compare with traditional classifiers and rule-based filters?
    - D2. How does it compare with closed moderation APIs?
    - D3. How does it compare with other open-weight safeguard approaches?
  - **E. Deployment and workflow fit**
    - E1. Can default GitHub-hosted runners run it directly?
    - E2. Which parts of this repository's review rubric are machine-checkable, policy-reasonable, or still judgment-heavy?

### §2 Investigation

#### A. Model identity and architecture

- [fact; source: https://github.com/openai/gpt-oss-safeguard/blob/main/README.md; https://huggingface.co/openai/gpt-oss-safeguard-20b/raw/main/README.md; https://huggingface.co/openai/gpt-oss-safeguard-120b/raw/main/README.md] OpenAI officially publishes gpt-oss-safeguard as two safety reasoning models built on gpt-oss: a 21B-parameter model with 3.6B active parameters and a 117B-parameter model with 5.1B active parameters.
- [fact; source: https://github.com/openai/gpt-oss-safeguard/blob/main/README.md; https://huggingface.co/openai/gpt-oss-safeguard-20b/raw/main/README.md; https://huggingface.co/openai/gpt-oss-safeguard-120b/raw/main/README.md] The official positioning is classification against safety policies supplied by the developer, not general-purpose chat, and the repository explicitly recommends ordinary gpt-oss models for non-safety use cases.
- [fact; source: https://github.com/openai/gpt-oss-safeguard/blob/main/README.md; https://cookbook.openai.com/articles/gpt-oss-safeguard-guide] Both models require OpenAI's Harmony prompt format and are documented as not working correctly without it.
- [fact; source: https://huggingface.co/openai/gpt-oss-safeguard-20b/raw/main/README.md; https://huggingface.co/openai/gpt-oss-safeguard-120b/raw/main/README.md] The released model cards expose Apache 2.0 licensing metadata and identify the models as fine-tunes of the open gpt-oss base models, which is the core evidence that the models are released-weight and self-hostable.

#### B. Policy specification and outputs

- [fact; source: https://cookbook.openai.com/articles/gpt-oss-safeguard-guide] OpenAI's guide says gpt-oss-safeguard is a bring-your-own-policy model that follows explicit written policies supplied in the system message and classifies the target content supplied in the user message.
- [fact; source: https://cookbook.openai.com/articles/gpt-oss-safeguard-guide; https://github.com/openai/gpt-oss-safeguard/blob/main/example_policies/spam/policy.txt] The official guidance recommends four policy sections, Instruction, Definitions, Criteria, and Examples, and the repository's spam policy example instantiates that pattern with severity tiers, escalation rules, and labeled examples near the decision boundary.
- [fact; source: https://cookbook.openai.com/articles/gpt-oss-safeguard-guide] The official guide says developers can choose binary outputs, policy-referencing outputs, or outputs that include a brief rationale, policy category, rule identifiers, and confidence.
- [fact; source: https://cookbook.openai.com/articles/gpt-oss-safeguard-guide] The guide documents a `reasoning_effort` control with low, medium, and high settings, and states that higher reasoning effort improves handling of complex interactions at higher latency cost.
- [fact; source: https://cookbook.openai.com/articles/gpt-oss-safeguard-guide] OpenAI's public guidance says policies of about 400 to 600 tokens are the observed sweet spot, that the model can still produce reasonable output with policies near 10,000 tokens, and that adding multiple policies causes small but meaningful accuracy degradation.

#### C. Evaluation evidence and explicit limitations

- [fact; source: https://github.com/openai/gpt-oss-safeguard/blob/main/example_policies/spam/golden_dataset.csv] The only directly accessible official numeric evaluation artifact found in public source files is the repository's spam golden dataset, which reports accuracy 0.9, precision 1.0, recall 0.8, and F1 0.8888888889 for that example policy.
- [fact; source: https://cookbook.openai.com/articles/gpt-oss-safeguard-guide] OpenAI's accessible public guide does not publish a broad benchmark table with false-positive or false-negative rates by policy family, but it does state that traditional classifiers trained on thousands of examples will likely outperform gpt-oss-safeguard on a single narrow task.
- [fact; source: https://cookbook.openai.com/articles/gpt-oss-safeguard-guide] The same guide states that traditional classifiers have lower latency and lower sampling cost than gpt-oss-safeguard, and that OpenAI uses small high-recall classifiers to pre-filter domain-relevant content before sending it to gpt-oss-safeguard.
- [inference; source: https://cookbook.openai.com/articles/gpt-oss-safeguard-guide; https://github.com/openai/gpt-oss-safeguard/blob/main/example_policies/spam/golden_dataset.csv] The accessible official evidence supports the model's qualitative value proposition, policy flexibility and reasoned classification, more strongly than it supports a claim of universally superior standalone accuracy.

#### D. Comparison with rule-based and traditional classifiers

- [fact; source: https://cookbook.openai.com/articles/gpt-oss-safeguard-guide] OpenAI explicitly contrasts gpt-oss-safeguard with "traditional classifiers" on latency, cost, and narrow-task performance, recommending the smaller classifiers as a first-stage pre-filter rather than claiming the safeguard model should replace them everywhere.
- [fact; source: https://davidamitchell.github.io/Research/research/2026-04-26-policy-coherence-machine-checkable-prerequisite.html; https://davidamitchell.github.io/Research/research/2026-04-26-deployment-pipeline-citizen-development-governed-gate.html] Prior repository work shows that exact-structure requirements, such as mandatory URLs, fixed label vocabularies, and required sections, are machine-checkable before any policy reasoning is needed.
- [inference; source: https://cookbook.openai.com/articles/gpt-oss-safeguard-guide; https://davidamitchell.github.io/Research/research/2026-04-26-policy-coherence-machine-checkable-prerequisite.html] Rule-based checks remain the best fit for deterministic surface constraints, while gpt-oss-safeguard is better suited to contextual and compositional rules, such as whether a sentence functionally makes a claim, whether a cited rationale matches a rule, or whether a borderline example falls inside a textual policy definition.

#### E. Comparison with closed-API guardrails

- [fact; source: https://developers.openai.com/api/docs/guides/moderation] OpenAI Moderation exposes a closed Application Programming Interface with fixed categories, category scores, and category-level flags, including a warning that downstream custom policies tied to the scores may need recalibration as the underlying model is upgraded.
- [fact; source: https://arxiv.org/abs/2312.06674; https://developers.openai.com/api/docs/guides/moderation] The Llama Guard paper explicitly characterizes tools such as the OpenAI Moderation API as fixed-policy and API-only moderation tools, which is the clearest official comparison source for the customization gap that gpt-oss-safeguard tries to close.
- [fact; source: https://www.anthropic.com/research/constitutional-ai-harmlessness-from-ai-feedback; https://www.anthropic.com/constitution] Anthropic's Constitutional AI approach publishes a constitution of principles for training and guiding Claude, but the public material describes alignment of Anthropic's own deployed model behavior rather than a released-weight, self-hosted classifier that lets downstream developers swap policy text at inference.
- [inference; source: https://developers.openai.com/api/docs/guides/moderation; https://www.anthropic.com/research/constitutional-ai-harmlessness-from-ai-feedback; https://cookbook.openai.com/articles/gpt-oss-safeguard-guide] Closed-API guardrails optimize for managed service simplicity and lab-maintained policy surfaces, while gpt-oss-safeguard optimizes for local control of policy text, hosting, and auditability.

#### F. Comparison with open-weight alternatives

- [fact; source: https://arxiv.org/abs/2312.06674] Llama Guard is an instruction-tuned 7B safeguard model that accepts a taxonomy in the input, separates prompt classification from response classification, and reports performance matching or exceeding available moderation tools on the OpenAI Moderation Evaluation dataset and ToxicChat.
- [fact; source: https://arxiv.org/abs/2312.06674] The same paper says Llama Guard customization works through zero-shot or few-shot prompting with different taxonomies, and potentially through further fine-tuning, which makes it the closest published open-weight precedent to gpt-oss-safeguard.
- [fact; source: https://arxiv.org/abs/2310.10501] NeMo Guardrails is not primarily a classifier model; it is an open-source toolkit for adding programmable, interpretable rails around Large Language Model applications, independent of the underlying model provider.
- [inference; source: https://arxiv.org/abs/2312.06674; https://arxiv.org/abs/2310.10501; https://cookbook.openai.com/articles/gpt-oss-safeguard-guide] gpt-oss-safeguard sits between Llama Guard and NeMo Guardrails: it is closer to Llama Guard in being a policy-conditioned classifier, but it borrows some of NeMo's value proposition, explicit policy programmability, without becoming a full runtime orchestration framework.

#### G. Deployment feasibility and repository applicability

- [fact; source: https://huggingface.co/openai/gpt-oss-safeguard-20b/raw/main/README.md; https://huggingface.co/openai/gpt-oss-safeguard-120b/raw/main/README.md; https://cookbook.openai.com/articles/gpt-oss/run-locally-ollama; https://cookbook.openai.com/articles/gpt-oss/run-locally-lmstudio] OpenAI's public deployment guidance places the 20B model at about 16 GB VRAM and the 120B model at a single H100 class device or about 60 GB VRAM or more on local stacks, with Central Processing Unit (CPU) offload possible but slower.
- [fact; source: https://docs.github.com/en/actions/reference/runners/github-hosted-runners] Standard GitHub-hosted Linux runners provide 8 to 16 GB Random Access Memory (RAM) and no Graphics Processing Unit (GPU), while GPU availability exists only on larger runners.
- [inference; source: https://docs.github.com/en/actions/reference/runners/github-hosted-runners; https://huggingface.co/openai/gpt-oss-safeguard-20b/raw/main/README.md; https://huggingface.co/openai/gpt-oss-safeguard-120b/raw/main/README.md] Direct first-class inference of gpt-oss-safeguard inside this repository's default GitHub Actions environment is not realistic on standard runners; the plausible deployment patterns are a self-hosted or larger GPU runner, a separate internal inference service, or a local pre-commit or review-sidecar workflow.
- [fact; source: https://cookbook.openai.com/articles/gpt-oss-safeguard-guide; https://github.com/openai/gpt-oss-safeguard/blob/main/example_policies/spam/policy.txt] The official policy design supports categorical outputs, rule identifiers, escalation markers, and rationales, which means the model can be asked to return repository-specific labels and rule references rather than only unsafe or safe scores.
- [inference; source: https://davidamitchell.github.io/Research/research/2026-04-26-policy-coherence-machine-checkable-prerequisite.html; https://davidamitchell.github.io/Research/research/2026-05-02-hitl-review-volume-bottleneck-rubber-stamp.html; https://cookbook.openai.com/articles/gpt-oss-safeguard-guide] For this repository's review rubric, the model is well suited to rules that require context-sensitive reading of prose against an explicit written policy, but it should sit behind cheap structural checks and ahead of sampled or exception-based human review rather than replace both.
- [inference; source: https://davidamitchell.github.io/Research/research/2026-04-26-policy-coherence-machine-checkable-prerequisite.html; https://davidamitchell.github.io/Research/research/2026-04-26-deployment-pipeline-citizen-development-governed-gate.html; https://davidamitchell.github.io/Research/research/2026-05-02-hitl-review-volume-bottleneck-rubber-stamp.html] Machine-checkable rules include URL presence, exact epistemic label vocabulary, prohibited stock phrases, and output-schema completeness; policy-reasoning rules include whether a sentence is actually a claim, whether the cited rule matches the violation, and whether a borderline sentence belongs to a policy category; judgment-heavy checks, such as whether the synthesis genuinely changes a decision or whether a nuanced claim is materially misleading despite formal compliance, still need agentic review or sampled human challenge.

### §3 Reasoning

- [fact; source: https://github.com/openai/gpt-oss-safeguard/blob/main/README.md; https://cookbook.openai.com/articles/gpt-oss-safeguard-guide; https://developers.openai.com/api/docs/guides/moderation] The direct evidence establishes three hard differences: gpt-oss-safeguard is self-hostable and policy-conditioned, OpenAI Moderation is fixed-category and API-mediated, and Anthropic Constitutional AI is a training-and-governance approach for Anthropic's own models rather than a released-weight policy classifier.
- [fact; source: https://github.com/openai/gpt-oss-safeguard/blob/main/example_policies/spam/golden_dataset.csv] The only accessible official quantitative evidence is example-policy level, not a broad benchmark suite, so any strong claim that the model is broadly more accurate than alternatives would exceed the public evidence base used here.
- [inference; source: https://cookbook.openai.com/articles/gpt-oss-safeguard-guide; https://docs.github.com/en/actions/reference/runners/github-hosted-runners] The most defensible deployment recommendation is a cascade, deterministic checks first, gpt-oss-safeguard for contextual policy judgment second, and sampled human or high-cost adversarial review third, because that arrangement matches both OpenAI's own pre-filter guidance and GitHub Actions hardware limits.
- [assumption; source: https://github.com/openai/gpt-oss-safeguard/blob/main/example_policies/spam/golden_dataset.csv; https://cookbook.openai.com/articles/gpt-oss-safeguard-guide] The public spam example is treated as illustrative of how OpenAI expects users to evaluate custom policies, not as evidence that all policy domains will obtain comparable accuracy.

### §4 Consistency Check

- [fact; source: https://github.com/openai/gpt-oss-safeguard/blob/main/README.md; https://huggingface.co/openai/gpt-oss-safeguard-20b/raw/main/README.md; https://huggingface.co/openai/gpt-oss-safeguard-120b/raw/main/README.md] The repository README and both model-card READMEs are internally consistent on model identity, parameter counts, Harmony dependence, and release positioning.
- [fact; source: https://cookbook.openai.com/articles/gpt-oss-safeguard-guide; https://developers.openai.com/api/docs/guides/moderation] The comparison between safeguard and Moderation is not contradictory: the guide claims policy flexibility and richer reasoning for safeguard, while Moderation docs describe fixed categories and managed scores.
- [inference; source: https://cookbook.openai.com/articles/gpt-oss-safeguard-guide; https://arxiv.org/abs/2312.06674] The apparent tension between "traditional classifiers often perform better on a narrow task" and "policy-conditioned reasoning is more flexible" resolves as a scope trade-off, not a disagreement about the same target objective.
- [fact; source: https://docs.github.com/en/actions/reference/runners/github-hosted-runners; https://cookbook.openai.com/articles/gpt-oss/run-locally-ollama; https://cookbook.openai.com/articles/gpt-oss/run-locally-lmstudio] The deployment conclusion is grounded in documented runner resources versus documented VRAM guidance rather than in undocumented assumptions about this repository's specific runner image.

### §5 Depth and Breadth Expansion

- [inference; source: https://cookbook.openai.com/articles/gpt-oss-safeguard-guide; https://developers.openai.com/api/docs/guides/moderation] Technical lens: the strongest practical design is layered, because a closed moderation endpoint or deterministic filter can cheaply screen obvious cases while gpt-oss-safeguard handles the ambiguous policy-heavy tail.
- [inference; source: https://huggingface.co/openai/gpt-oss-safeguard-20b/raw/main/README.md; https://huggingface.co/openai/gpt-oss-safeguard-120b/raw/main/README.md; https://docs.github.com/en/actions/reference/runners/github-hosted-runners] Economic lens: self-hosting avoids sending review text to an external moderation API, but it shifts cost into scarce GPU capacity that the default GitHub pipeline does not currently have.
- [inference; source: https://www.anthropic.com/constitution; https://cookbook.openai.com/articles/gpt-oss-safeguard-guide; https://arxiv.org/abs/2310.10501] Governance lens: gpt-oss-safeguard is attractive where an organization wants its own written policy to remain the governing artifact, while Constitutional AI favors provider-owned constitutional judgment and NeMo favors explicit runtime rails around another model.
- [inference; source: https://davidamitchell.github.io/Research/research/2026-05-02-hitl-review-volume-bottleneck-rubber-stamp.html; https://cookbook.openai.com/articles/gpt-oss-safeguard-guide] Behavioral lens: exposing model reasoning can reduce moderator effort and help policy debugging, but it can also increase reviewer over-trust unless escalation thresholds and sampling checks remain in place.

### §6 Synthesis

**Executive summary:**

- [inference; source: https://github.com/openai/gpt-oss-safeguard/blob/main/README.md; https://cookbook.openai.com/articles/gpt-oss-safeguard-guide; https://developers.openai.com/api/docs/guides/moderation] gpt-oss-safeguard is best understood as an open-weight, policy-conditioned safety classifier that trades raw latency and narrow-task specialization for self-hosting, explicit policy control, and inspectable reasoning.
- [fact; source: https://huggingface.co/openai/gpt-oss-safeguard-20b/raw/main/README.md; https://huggingface.co/openai/gpt-oss-safeguard-120b/raw/main/README.md; https://docs.github.com/en/actions/reference/runners/github-hosted-runners] The model family is not a practical drop-in for standard GitHub-hosted Actions runners, because the documented 20B and 120B hardware requirements exceed the default runner's no-GPU profile.
- [inference; source: https://cookbook.openai.com/articles/gpt-oss-safeguard-guide; https://davidamitchell.github.io/Research/research/2026-04-26-policy-coherence-machine-checkable-prerequisite.html; https://davidamitchell.github.io/Research/research/2026-05-02-hitl-review-volume-bottleneck-rubber-stamp.html] For this repository's research-review pipeline, the strongest fit is a hybrid control pattern, deterministic linting first, policy-conditioned reasoning second, and sampled human or adversarial challenge third.
- [fact; source: https://github.com/openai/gpt-oss-safeguard/blob/main/example_policies/spam/golden_dataset.csv; https://cookbook.openai.com/articles/gpt-oss-safeguard-guide] Public official evidence is strong enough to support the model's design and deployment trade-offs, but not strong enough to claim broadly published false-positive or false-negative performance across many policy families.

**Key findings:**

1. [fact; source: https://github.com/openai/gpt-oss-safeguard/blob/main/README.md; https://huggingface.co/openai/gpt-oss-safeguard-20b/raw/main/README.md; https://huggingface.co/openai/gpt-oss-safeguard-120b/raw/main/README.md] OpenAI officially publishes gpt-oss-safeguard as two released-weight safety reasoning models, 20B and 120B, built on gpt-oss and intended specifically for developer-supplied policy classification rather than general assistant use.
2. [fact; source: https://cookbook.openai.com/articles/gpt-oss-safeguard-guide; https://github.com/openai/gpt-oss-safeguard/blob/main/example_policies/spam/policy.txt] The model's policy interface is genuinely customizable, because OpenAI documents free-form written policies with instructions, definitions, criteria, examples, output schemas, and reasoning-effort controls rather than a fixed built-in moderation taxonomy.
3. [fact; source: https://github.com/openai/gpt-oss-safeguard/blob/main/example_policies/spam/golden_dataset.csv; https://cookbook.openai.com/articles/gpt-oss-safeguard-guide] The accessible public evaluation evidence is narrow rather than comprehensive, with an official spam example reporting 0.9 accuracy, 1.0 precision, 0.8 recall, and 0.8888888889 F1, while broader public benchmark tables are not exposed in the accessible official materials used here.
4. [inference; source: https://cookbook.openai.com/articles/gpt-oss-safeguard-guide; https://davidamitchell.github.io/Research/research/2026-04-26-policy-coherence-machine-checkable-prerequisite.html] Rule-based and traditional classifiers remain superior for deterministic or narrowly trained checks because OpenAI itself describes them as cheaper and faster, so gpt-oss-safeguard is better treated as a second-stage policy reasoner than as a universal first-stage filter.
5. [fact; source: https://developers.openai.com/api/docs/guides/moderation; https://www.anthropic.com/research/constitutional-ai-harmlessness-from-ai-feedback; https://www.anthropic.com/constitution] Compared with closed-API guardrails, gpt-oss-safeguard offers more local control over hosting and policy text, while OpenAI Moderation exposes fixed managed categories and Anthropic Constitutional AI exposes provider-owned constitutional training and governance rather than a self-hosted classifier surface.
6. [inference; source: https://arxiv.org/abs/2312.06674; https://arxiv.org/abs/2310.10501; https://cookbook.openai.com/articles/gpt-oss-safeguard-guide] Compared with other open approaches, gpt-oss-safeguard is closest to Llama Guard in policy-conditioned classification, but it occupies a middle position between Llama Guard style classifiers and NeMo Guardrails style runtime rails.
7. [fact; source: https://huggingface.co/openai/gpt-oss-safeguard-20b/raw/main/README.md; https://huggingface.co/openai/gpt-oss-safeguard-120b/raw/main/README.md; https://docs.github.com/en/actions/reference/runners/github-hosted-runners] The model family is not a realistic direct dependency for this repository's default GitHub Actions pipeline, because standard runners have no GPU and only 8 to 16 GB RAM, while the documented model deployments assume at least 16 GB VRAM for 20B and H100 class hardware or about 60 GB VRAM for 120B.
8. [inference; source: https://davidamitchell.github.io/Research/research/2026-04-26-deployment-pipeline-citizen-development-governed-gate.html; https://davidamitchell.github.io/Research/research/2026-05-02-hitl-review-volume-bottleneck-rubber-stamp.html; https://cookbook.openai.com/articles/gpt-oss-safeguard-guide] The repository's review rubric can partly be enforced by a safeguard model, especially context-sensitive policy checks on prose, but the most decision-critical synthesis and judgment checks still require a higher-cost review layer rather than pure automated classification.

**Evidence map:**

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [fact] OpenAI officially publishes two gpt-oss-safeguard models for policy classification. | https://github.com/openai/gpt-oss-safeguard/blob/main/README.md; https://huggingface.co/openai/gpt-oss-safeguard-20b/raw/main/README.md; https://huggingface.co/openai/gpt-oss-safeguard-120b/raw/main/README.md | high | official repo and model cards |
| [fact] The policy interface is customizable through written policy documents and output schemas. | https://cookbook.openai.com/articles/gpt-oss-safeguard-guide; https://github.com/openai/gpt-oss-safeguard/blob/main/example_policies/spam/policy.txt | high | official prompt guide and sample policy |
| [fact] Accessible public numeric evaluation is narrow and example-policy based. | https://github.com/openai/gpt-oss-safeguard/blob/main/example_policies/spam/golden_dataset.csv; https://cookbook.openai.com/articles/gpt-oss-safeguard-guide | medium | one public metric file, no broad table |
| [inference] Traditional classifiers should remain first-stage filters, with safeguard as a second-stage policy reasoner. | https://cookbook.openai.com/articles/gpt-oss-safeguard-guide; https://davidamitchell.github.io/Research/research/2026-04-26-policy-coherence-machine-checkable-prerequisite.html | high | directly supported by OpenAI guidance plus repo control design |
| [fact] Closed-API guardrails and Constitutional AI expose different control surfaces from safeguard. | https://developers.openai.com/api/docs/guides/moderation; https://www.anthropic.com/research/constitutional-ai-harmlessness-from-ai-feedback; https://www.anthropic.com/constitution | high | official docs on each surface |
| [inference] gpt-oss-safeguard occupies a middle position between Llama Guard and NeMo Guardrails. | https://arxiv.org/abs/2312.06674; https://arxiv.org/abs/2310.10501; https://cookbook.openai.com/articles/gpt-oss-safeguard-guide | medium | cross-source product-positioning inference |
| [fact] Standard GitHub-hosted runners cannot realistically host the model directly. | https://huggingface.co/openai/gpt-oss-safeguard-20b/raw/main/README.md; https://huggingface.co/openai/gpt-oss-safeguard-120b/raw/main/README.md; https://docs.github.com/en/actions/reference/runners/github-hosted-runners | high | documented hardware mismatch |
| [inference] The research-review rubric is only partly suitable for safeguard-based automation. | https://davidamitchell.github.io/Research/research/2026-04-26-deployment-pipeline-citizen-development-governed-gate.html; https://davidamitchell.github.io/Research/research/2026-05-02-hitl-review-volume-bottleneck-rubber-stamp.html; https://cookbook.openai.com/articles/gpt-oss-safeguard-guide | medium | workflow-fit synthesis |

**Assumptions:**

- [assumption; source: https://github.com/openai/gpt-oss-safeguard/blob/main/example_policies/spam/golden_dataset.csv; https://cookbook.openai.com/articles/gpt-oss-safeguard-guide] The public spam example is representative of how OpenAI expects custom-policy evaluation to be staged, even though it is not a broad external benchmark suite.
- [assumption; source: https://developers.openai.com/api/docs/guides/moderation; https://www.anthropic.com/constitution; https://cookbook.openai.com/articles/gpt-oss-safeguard-guide] The most relevant comparison surface for this repository is not generic content safety alone, but whether the system lets developers supply, host, and revise organization-specific written policies.

**Analysis:**

- [inference; source: https://cookbook.openai.com/articles/gpt-oss-safeguard-guide; https://developers.openai.com/api/docs/guides/moderation] The most important trade-off is not "open versus closed" in the abstract, but fixed managed categories versus developer-owned policy text plus self-hosting responsibility.
- [inference; source: https://cookbook.openai.com/articles/gpt-oss-safeguard-guide; https://github.com/openai/gpt-oss-safeguard/blob/main/example_policies/spam/policy.txt] gpt-oss-safeguard is strongest where a rule cannot be reduced to a simple pattern match, yet can still be written down clearly enough for a model to reason against it.
- [inference; source: https://davidamitchell.github.io/Research/research/2026-04-26-deployment-pipeline-citizen-development-governed-gate.html; https://davidamitchell.github.io/Research/research/2026-05-02-hitl-review-volume-bottleneck-rubber-stamp.html; https://docs.github.com/en/actions/reference/runners/github-hosted-runners] Keeping full per-item human review is the main rival remedy for judgment-heavy research checks, but prior repository evidence on review overload and the runner hardware mismatch together imply that a purely human path is capacity-bound while a purely on-runner safeguard path is infrastructure-bound.
- [inference; source: https://cookbook.openai.com/articles/gpt-oss-safeguard-guide; https://davidamitchell.github.io/Research/research/2026-04-26-policy-coherence-machine-checkable-prerequisite.html] Stronger deterministic linting is another rival remedy, but it only covers the machine-checkable subset of the rubric and therefore cannot replace contextual classification of prose against policy text.
- [inference; source: https://www.anthropic.com/constitution; https://developers.openai.com/api/docs/guides/moderation; https://cookbook.openai.com/articles/gpt-oss-safeguard-guide] Stronger closed-provider guardrails are a third rival remedy, but they solve a different problem, managed generic safety, and do not provide the same degree of organization-specific policy control or local auditability.

**Risks, gaps, uncertainties:**

- [fact; source: https://github.com/openai/gpt-oss-safeguard/blob/main/example_policies/spam/golden_dataset.csv; https://cookbook.openai.com/articles/gpt-oss-safeguard-guide] Accessible official public materials do not expose a full benchmark table by policy type, so confidence on broad accuracy claims should remain below high.
- [fact; source: https://cookbook.openai.com/articles/gpt-oss-safeguard-guide] OpenAI explicitly notes that multiple simultaneous policies degrade accuracy, which matters for any attempt to encode the repository's entire review rubric into one large policy.
- [inference; source: https://cookbook.openai.com/articles/gpt-oss-safeguard-guide; https://docs.github.com/en/actions/reference/runners/github-hosted-runners] Even if the policy design proves strong, infrastructure cost remains a real blocker unless the review workflow gains GPU access or an internal inference endpoint.

**Open questions:**

- [inference; source: https://cookbook.openai.com/articles/gpt-oss-safeguard-guide; https://github.com/openai/gpt-oss-safeguard/blob/main/example_policies/spam/golden_dataset.csv] How much accuracy is lost when the repository's review rubric is split into several short policies versus one long composite policy?
- [inference; source: https://cookbook.openai.com/articles/gpt-oss-safeguard-guide; https://davidamitchell.github.io/Research/research/2026-05-02-hitl-review-volume-bottleneck-rubber-stamp.html] What escalation thresholds and sampling design would prevent reviewers from over-trusting the model's rationale output?
- [inference; source: https://developers.openai.com/api/docs/guides/moderation; https://cookbook.openai.com/articles/gpt-oss-safeguard-guide] For this repository's needs, is a hybrid stack of closed moderation for obvious harms plus open-weight policy reasoning for rubric compliance better than an all-open or all-closed design?

### §7 Recursive Review

- Claim-label audit: complete
- Acronym expansion audit: complete
- Findings and synthesis parity: aligned
- URL-backed source audit: complete
- Confidence setting: medium
- Unresolved uncertainty: broad public benchmark depth remains limited

---

## Findings

### Executive Summary

gpt-oss-safeguard is best understood as an open-weight, policy-conditioned safety classifier that trades raw latency and narrow-task specialization for self-hosting, explicit policy control, and inspectable reasoning. [inference; source: https://github.com/openai/gpt-oss-safeguard/blob/main/README.md; https://cookbook.openai.com/articles/gpt-oss-safeguard-guide; https://developers.openai.com/api/docs/guides/moderation]

The model family is not a practical drop-in for standard GitHub-hosted Actions runners, because the documented 20B and 120B hardware requirements exceed the default runner's no-GPU profile. [fact; source: https://huggingface.co/openai/gpt-oss-safeguard-20b/raw/main/README.md; https://huggingface.co/openai/gpt-oss-safeguard-120b/raw/main/README.md; https://docs.github.com/en/actions/reference/runners/github-hosted-runners]

For this repository's research-review pipeline, the strongest fit is a hybrid control pattern, deterministic linting first, policy-conditioned reasoning second, and sampled human or adversarial challenge third. [inference; source: https://cookbook.openai.com/articles/gpt-oss-safeguard-guide; https://davidamitchell.github.io/Research/research/2026-04-26-policy-coherence-machine-checkable-prerequisite.html; https://davidamitchell.github.io/Research/research/2026-05-02-hitl-review-volume-bottleneck-rubber-stamp.html]

Public official evidence is strong enough to support the model's design and deployment trade-offs, but not strong enough to claim broadly published false-positive or false-negative performance across many policy families. [fact; source: https://github.com/openai/gpt-oss-safeguard/blob/main/example_policies/spam/golden_dataset.csv; https://cookbook.openai.com/articles/gpt-oss-safeguard-guide]

### Key Findings

1. **OpenAI officially publishes gpt-oss-safeguard as two released-weight safety reasoning models, 20B and 120B, built on gpt-oss and intended specifically for developer-supplied policy classification rather than general assistant use.** ([fact]; high confidence; source: https://github.com/openai/gpt-oss-safeguard/blob/main/README.md; https://huggingface.co/openai/gpt-oss-safeguard-20b/raw/main/README.md; https://huggingface.co/openai/gpt-oss-safeguard-120b/raw/main/README.md)
2. **The model's policy interface is genuinely customizable, because OpenAI documents free-form written policies with instructions, definitions, criteria, examples, output schemas, and reasoning-effort controls rather than a fixed built-in moderation taxonomy.** ([fact]; high confidence; source: https://cookbook.openai.com/articles/gpt-oss-safeguard-guide; https://github.com/openai/gpt-oss-safeguard/blob/main/example_policies/spam/policy.txt)
3. **The accessible public evaluation evidence is narrow rather than comprehensive, with an official spam example reporting 0.9 accuracy, 1.0 precision, 0.8 recall, and 0.8888888889 F1, while broader public benchmark tables are not exposed in the accessible official materials used here.** ([fact]; medium confidence; source: https://github.com/openai/gpt-oss-safeguard/blob/main/example_policies/spam/golden_dataset.csv; https://cookbook.openai.com/articles/gpt-oss-safeguard-guide)
4. **Rule-based and traditional classifiers remain superior for deterministic or narrowly trained checks because OpenAI itself describes them as cheaper and faster, so gpt-oss-safeguard is better treated as a second-stage policy reasoner than as a universal first-stage filter.** ([inference]; high confidence; source: https://cookbook.openai.com/articles/gpt-oss-safeguard-guide; https://davidamitchell.github.io/Research/research/2026-04-26-policy-coherence-machine-checkable-prerequisite.html)
5. **Compared with closed-API guardrails, gpt-oss-safeguard offers more local control over hosting and policy text, while OpenAI Moderation exposes fixed managed categories and Anthropic Constitutional AI exposes provider-owned constitutional training and governance rather than a self-hosted classifier surface.** ([fact]; high confidence; source: https://developers.openai.com/api/docs/guides/moderation; https://www.anthropic.com/research/constitutional-ai-harmlessness-from-ai-feedback; https://www.anthropic.com/constitution)
6. **Compared with other open approaches, gpt-oss-safeguard is closest to Llama Guard in policy-conditioned classification, but it occupies a middle position between Llama Guard style classifiers and NeMo Guardrails style runtime rails.** ([inference]; medium confidence; source: https://arxiv.org/abs/2312.06674; https://arxiv.org/abs/2310.10501; https://cookbook.openai.com/articles/gpt-oss-safeguard-guide)
7. **The model family is not a realistic direct dependency for this repository's default GitHub Actions pipeline, because standard runners have no GPU and only 8 to 16 GB RAM, while the documented model deployments assume at least 16 GB VRAM for 20B and H100 class hardware or about 60 GB VRAM for 120B.** ([fact]; high confidence; source: https://huggingface.co/openai/gpt-oss-safeguard-20b/raw/main/README.md; https://huggingface.co/openai/gpt-oss-safeguard-120b/raw/main/README.md; https://docs.github.com/en/actions/reference/runners/github-hosted-runners)
8. **The repository's review rubric can partly be enforced by a safeguard model, especially context-sensitive policy checks on prose, but the most decision-critical synthesis and judgment checks still require a higher-cost review layer rather than pure automated classification.** ([inference]; medium confidence; source: https://davidamitchell.github.io/Research/research/2026-04-26-deployment-pipeline-citizen-development-governed-gate.html; https://davidamitchell.github.io/Research/research/2026-05-02-hitl-review-volume-bottleneck-rubber-stamp.html; https://cookbook.openai.com/articles/gpt-oss-safeguard-guide)

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [fact] OpenAI officially publishes two gpt-oss-safeguard models for policy classification. | https://github.com/openai/gpt-oss-safeguard/blob/main/README.md; https://huggingface.co/openai/gpt-oss-safeguard-20b/raw/main/README.md; https://huggingface.co/openai/gpt-oss-safeguard-120b/raw/main/README.md | high | official repo and model cards |
| [fact] The policy interface is customizable through written policy documents and output schemas. | https://cookbook.openai.com/articles/gpt-oss-safeguard-guide; https://github.com/openai/gpt-oss-safeguard/blob/main/example_policies/spam/policy.txt | high | official prompt guide and sample policy |
| [fact] Accessible public numeric evaluation is narrow and example-policy based. | https://github.com/openai/gpt-oss-safeguard/blob/main/example_policies/spam/golden_dataset.csv; https://cookbook.openai.com/articles/gpt-oss-safeguard-guide | medium | one public metric file, no broad table |
| [inference] Traditional classifiers should remain first-stage filters, with safeguard as a second-stage policy reasoner. | https://cookbook.openai.com/articles/gpt-oss-safeguard-guide; https://davidamitchell.github.io/Research/research/2026-04-26-policy-coherence-machine-checkable-prerequisite.html | high | direct guidance plus repo control logic |
| [fact] Closed-API guardrails and Constitutional AI expose different control surfaces from safeguard. | https://developers.openai.com/api/docs/guides/moderation; https://www.anthropic.com/research/constitutional-ai-harmlessness-from-ai-feedback; https://www.anthropic.com/constitution | high | official docs on each surface |
| [inference] gpt-oss-safeguard occupies a middle position between Llama Guard and NeMo Guardrails. | https://arxiv.org/abs/2312.06674; https://arxiv.org/abs/2310.10501; https://cookbook.openai.com/articles/gpt-oss-safeguard-guide | medium | cross-source product-positioning inference |
| [fact] Standard GitHub-hosted runners cannot realistically host the model directly. | https://huggingface.co/openai/gpt-oss-safeguard-20b/raw/main/README.md; https://huggingface.co/openai/gpt-oss-safeguard-120b/raw/main/README.md; https://docs.github.com/en/actions/reference/runners/github-hosted-runners | high | documented hardware mismatch |
| [inference] The research-review rubric is only partly suitable for safeguard-based automation. | https://davidamitchell.github.io/Research/research/2026-04-26-deployment-pipeline-citizen-development-governed-gate.html; https://davidamitchell.github.io/Research/research/2026-05-02-hitl-review-volume-bottleneck-rubber-stamp.html; https://cookbook.openai.com/articles/gpt-oss-safeguard-guide | medium | workflow-fit synthesis |

### Assumptions

- **Assumption:** The public spam example is representative of how OpenAI expects custom-policy evaluation to be staged, even though it is not a broad external benchmark suite. **Justification:** It is the only accessible official numeric evaluation artifact in the released repository and is paired with the official policy-writing guide. [assumption; source: https://github.com/openai/gpt-oss-safeguard/blob/main/example_policies/spam/golden_dataset.csv; https://cookbook.openai.com/articles/gpt-oss-safeguard-guide]
- **Assumption:** The comparison surface that matters most for this repository is organization-specific policy control rather than generic harmful-content detection alone. **Justification:** The repository's review process is driven by explicit rubric rules rather than by generic consumer-safety categories. [assumption; source: https://developers.openai.com/api/docs/guides/moderation; https://www.anthropic.com/constitution; https://cookbook.openai.com/articles/gpt-oss-safeguard-guide]

### Analysis

The most important trade-off is not "open versus closed" in the abstract, but fixed managed categories versus developer-owned policy text plus self-hosting responsibility. [inference; source: https://cookbook.openai.com/articles/gpt-oss-safeguard-guide; https://developers.openai.com/api/docs/guides/moderation]

gpt-oss-safeguard is strongest where a rule cannot be reduced to a simple pattern match, yet can still be written down clearly enough for a model to reason against it. [inference; source: https://cookbook.openai.com/articles/gpt-oss-safeguard-guide; https://github.com/openai/gpt-oss-safeguard/blob/main/example_policies/spam/policy.txt]

Keeping full per-item human review is the main rival remedy for judgment-heavy research checks, but prior repository evidence on review overload and the runner hardware mismatch together imply that a purely human path is capacity-bound while a purely on-runner safeguard path is infrastructure-bound. [inference; source: https://davidamitchell.github.io/Research/research/2026-04-26-deployment-pipeline-citizen-development-governed-gate.html; https://davidamitchell.github.io/Research/research/2026-05-02-hitl-review-volume-bottleneck-rubber-stamp.html; https://docs.github.com/en/actions/reference/runners/github-hosted-runners]

Stronger deterministic linting is another rival remedy, but it only covers the machine-checkable subset of the rubric and therefore cannot replace contextual classification of prose against policy text. [inference; source: https://cookbook.openai.com/articles/gpt-oss-safeguard-guide; https://davidamitchell.github.io/Research/research/2026-04-26-policy-coherence-machine-checkable-prerequisite.html]

Stronger closed-provider guardrails are a third rival remedy, but they solve a different problem, managed generic safety, and do not provide the same degree of organization-specific policy control or local auditability. [inference; source: https://www.anthropic.com/constitution; https://developers.openai.com/api/docs/guides/moderation; https://cookbook.openai.com/articles/gpt-oss-safeguard-guide]

### Risks, Gaps, and Uncertainties

- Accessible official public materials do not expose a full benchmark table by policy type, so confidence on broad accuracy claims should remain below high. [fact; source: https://github.com/openai/gpt-oss-safeguard/blob/main/example_policies/spam/golden_dataset.csv; https://cookbook.openai.com/articles/gpt-oss-safeguard-guide]
- OpenAI explicitly notes that multiple simultaneous policies degrade accuracy, which matters for any attempt to encode the repository's entire review rubric into one large policy. [fact; source: https://cookbook.openai.com/articles/gpt-oss-safeguard-guide]
- Even if the policy design proves strong, infrastructure cost remains a real blocker unless the review workflow gains GPU access or an internal inference endpoint. [inference; source: https://cookbook.openai.com/articles/gpt-oss-safeguard-guide; https://docs.github.com/en/actions/reference/runners/github-hosted-runners]

### Open Questions

- How much accuracy is lost when the repository's review rubric is split into several short policies versus one long composite policy? [inference; source: https://cookbook.openai.com/articles/gpt-oss-safeguard-guide; https://github.com/openai/gpt-oss-safeguard/blob/main/example_policies/spam/golden_dataset.csv]
- What escalation thresholds and sampling design would prevent reviewers from over-trusting the model's rationale output? [inference; source: https://cookbook.openai.com/articles/gpt-oss-safeguard-guide; https://davidamitchell.github.io/Research/research/2026-05-02-hitl-review-volume-bottleneck-rubber-stamp.html]
- For this repository's needs, is a hybrid stack of closed moderation for obvious harms plus open-weight policy reasoning for rubric compliance better than an all-open or all-closed design? [inference; source: https://developers.openai.com/api/docs/guides/moderation; https://cookbook.openai.com/articles/gpt-oss-safeguard-guide]

---

## Output

- Type: knowledge
- Description: This item establishes that gpt-oss-safeguard is a released-weight policy reasoner best used as a second-stage classifier inside a layered review pipeline, not as a direct replacement for deterministic linting or human judgment. [inference; source: https://github.com/openai/gpt-oss-safeguard/blob/main/README.md; https://cookbook.openai.com/articles/gpt-oss-safeguard-guide; https://docs.github.com/en/actions/reference/runners/github-hosted-runners]
- Links:
  - https://github.com/openai/gpt-oss-safeguard/blob/main/README.md
  - https://cookbook.openai.com/articles/gpt-oss-safeguard-guide
  - https://docs.github.com/en/actions/reference/runners/github-hosted-runners
