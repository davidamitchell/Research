---
review_count: 1
title: "Optionality and Control Across AI Model Consumption Stages"
added: 2026-10-17T07:35:56+00:00
status: reviewing
priority: medium
blocks: []
themes: [enterprise-adoption, ai-architecture, cost-performance, regulatory-compliance, benchmarks-eval]
started: 2026-10-18T03:45:29+00:00
completed: ~
output: [knowledge]
cites: [2026-08-13-llm-consumption-maturity-ladder, 2026-03-19-layered-org-llm-architecture]
related: []
superseded_by: ~
supersedes: ~
item_type: primary
confidence: medium
versions: []
---

# Optionality and Control Across AI Model Consumption Stages

## Research Question

When an organisation progresses from Artificial Intelligence (AI) capabilities embedded in vendor subscriptions, through managed model platforms, to self-hosting model weights on infrastructure it controls, how do model choice, per-request selection, and operational and data controls change? Which capabilities become available at each stage, and does model tuning begin on managed platforms or require self-hosting?

## Scope

**In scope:**
- Compare model optionality, per-request selection, control of weights, serving, data paths, and change cadence across subscription, managed-platform, and self-hosted stages; test whether the stages stack or replace one another.
- Identify evaluation, routing, confidence, escalation, and data-classification prerequisites for dynamic model selection.
- Verify platform-native fine-tuning, custom-weight import for serverless serving, and dedicated managed-endpoint paths on Amazon Bedrock, Microsoft Foundry, and Google Vertex AI, including regional availability.
- Compare retrieval, prompting, tuning, and smaller domain-specific models for policy question answering, compliance checking, classification, and extraction.
- Find independent self-hosting cost evidence; model break-even and sensitivity to workload and operating assumptions, including multi-agent orchestration.
- Assess named evidence for regulated organisations' self-hosting decisions, relevant residency and extraterritorial-access laws, exit planning, open-weight licensing and provenance, and model-risk governance.

**Out of scope:**
- Re-deriving the maturity-model mapping and routing survey covered by the cited research.
- Harness and runtime concerns.

**Constraints:** Use primary vendor documentation and pricing, statutes, regulator publications, and peer-reviewed or disclosed-methodology cost studies. Treat the three named managed platforms as representative examples, not an exhaustive survey. Bound legal analysis to the United States, European Union, and United Kingdom, adding another jurisdiction only where direct case evidence warrants it. Report source dates and regional availability explicitly.

## Context

The cited maturity-ladder research found that consumption stages can be mixed and that routing can bridge managed and self-hosted models, but left open independent cost evidence, regulated-organisation case evidence, and whether tuning is actually a self-hosting capability. This research informs where organisations should place stage boundaries and what capabilities, controls, and costs they take on when choosing a model-consumption path.

## Approach

1. Compare optionality, control, and responsibilities across the three stages.
   1a. Which models and vendors can be selected at each stage, and can selection vary per request?
   1b. Which controls over model weights, serving, data paths, and change cadence become available at each stage?
   1c. What team responsibilities and capabilities does each stage require?
   1d. Does evidence show that stages stack, preserving frontier-model access, or that moving stages replaces prior options?
2. Establish prerequisites and constraints for dynamic selection.
   2a. What workload-specific evaluation datasets, human-calibrated model judges, and regression gates are needed before routing can be trusted?
   2b. What evidence supports calibrated confidence and escalation from smaller models to frontier models?
   2c. How should data classification and regional inference restrictions constrain eligible models and routes?
3. Locate where tuning begins on managed platforms.
   3a. Which of the three named platforms offer platform-native fine-tuning, for which models and regions?
   3b. Which support importing externally trained custom weights for serverless serving, and where?
   3c. Which offer dedicated managed endpoints, and what control and operating responsibilities do they leave with the customer?
   3d. Where do these paths sit on the optionality and control axes, and does imported-weight serving count as platform use or self-hosting?
4. Compare tuning with retrieval, prompting, and smaller models.
   4a. For the four specified regulated-industry workloads, what evidence and criteria favor retrieval or prompting over tuning?
   4b. When do domain-specific smaller models outperform frontier models on cost and quality?
5. Estimate self-hosting break-even with independent evidence.
   5a. What independent cost studies and disclosed assumptions exist beyond the study in the cited item?
   5b. What break-even formula captures monthly tokens, input/output ratio, cache hit rate, batch share, graphics processing unit (GPU) hourly cost, throughput per GPU, utilisation, and operations-staff cost?
   5c. How do sensitivity scenarios and multi-agent orchestration alter the estimate?
6. Examine regulatory, licensing, and model-risk drivers.
   6a. Is there named, sourced case evidence that regulated organisations self-host for residency, extraterritorial data-access, or exit-planning reasons rather than cost?
   6b. How do applicable statutes and regulator guidance shape the control required at each stage?
   6c. How do open-weight licence and provenance obligations change across managed and self-hosted use?
   6d. What model-risk management controls apply when models inform consequential decisions?

## Sources

Starting points from prior repository research:

- [How Do Enterprise Artificial Intelligence (AI) Maturity Frameworks Map onto the Large Language Model (LLM) Consumption Ladder?](https://davidamitchell.github.io/Research/research/2026-08-13-llm-consumption-maturity-ladder.html) — prior work on consumption stages, routing, and self-hosting economics.
- [Layered Organisation Large Language Model: Feasibility and Architecture of Organisation-Customised LLMs](https://davidamitchell.github.io/Research/research/2026-03-19-layered-org-llm-architecture.html) — prior work on organisation-customised models and adaptation.
- [Amazon Web Services (AWS) Bedrock capabilities](https://davidamitchell.github.io/Research/research/2026-05-17-aws-bedrock-capabilities.html) — starting point for managed-platform capability evidence.

Managed-platform documentation (retrieved 2026-10-18):

- [Amazon Bedrock Custom Models and Fine-Tuning Documentation](https://docs.aws.amazon.com/bedrock/latest/userguide/custom-model-fine-tuning.html)
- [Amazon Bedrock Provisioned Throughput Documentation](https://docs.aws.amazon.com/bedrock/latest/userguide/prov-throughput.html)
- [Amazon Bedrock Custom Model Import Documentation](https://docs.aws.amazon.com/bedrock/latest/userguide/model-customization-import-model.html)
- [Amazon Bedrock Cross-Region Inference Documentation](https://docs.aws.amazon.com/bedrock/latest/userguide/cross-region-inference.html)
- [Microsoft Foundry Fine-Tuning Overview](https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/fine-tuning-overview)
- [Microsoft Foundry Models Sold Directly by Azure](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/concepts/models)
- [Microsoft Foundry Deployment Types](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-models/concepts/deployment-types)
- [Microsoft Foundry Deployments Overview](https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/deployments-overview)
- [Microsoft Foundry Import Custom Models with Fireworks](https://learn.microsoft.com/en-us/azure/foundry/how-to/fireworks/import-custom-models)
- [Microsoft Foundry Fireworks Models Enablement](https://learn.microsoft.com/en-us/azure/foundry/how-to/fireworks/enable-fireworks-models)
- [Google Vertex AI Tuning Introduction](https://cloud.google.com/vertex-ai/generative-ai/docs/models/tune-models)
- [Google Vertex AI Gemini Supervised Tuning](https://cloud.google.com/vertex-ai/generative-ai/docs/models/gemini-supervised-tuning)
- [Google Vertex AI Choose an Endpoint Type](https://cloud.google.com/vertex-ai/docs/predictions/choose-endpoint-type)
- [Google Vertex AI Deploy Models with Custom Weights](https://cloud.google.com/vertex-ai/generative-ai/docs/model-garden/deploy-models-with-custom-weights)
- [Google Vertex AI Use Open Models](https://cloud.google.com/vertex-ai/generative-ai/docs/open-models/use-open-models)

Cost, routing, and adaptation evidence:

- [Pan et al. (2025) Cost-Benefit Analysis of On-Premise LLM Deployment](https://arxiv.org/abs/2509.18101)
- [Knoop and Holtmann (2026) Consumer Blackwell GPU Inference Economics](https://arxiv.org/abs/2601.09527)
- [Jiang et al. (2026) AgentCARD Heterogeneous Agent Teams](https://arxiv.org/abs/2606.20629)
- [Skurikhin et al. (2026) Tokenomics of Small Language Model Ensembles](https://arxiv.org/abs/2610.00954)
- [Chen, Zaharia and Zou (2023) FrugalGPT](https://arxiv.org/abs/2305.05176)
- [Ong et al. (2024) RouteLLM](https://arxiv.org/abs/2406.18665)
- [LMSYS RouteLLM Repository](https://github.com/lm-sys/RouteLLM)
- [Zheng et al. (2023) Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena](https://arxiv.org/abs/2306.05685)
- [Ovadia et al. (2023) Fine-Tuning or Retrieval? Comparing Knowledge Injection in LLMs](https://arxiv.org/abs/2312.05934)
- [Soudani et al. (2024) Fine Tuning vs. Retrieval Augmented Generation for Less Popular Knowledge](https://arxiv.org/abs/2403.01432)
- [Belcak et al. (2025) Small Language Models are the Future of Agentic AI](https://arxiv.org/abs/2506.02153)

Statutes, regulator guidance, and licences:

- [United States Code (2018) 18 U.S.C. 2713 Required Preservation and Disclosure of Communications and Records](https://www.law.cornell.edu/uscode/text/18/2713)
- [European Union (2022) Regulation 2022/2554 Digital Operational Resilience Act](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32022R2554)
- [European Union (2023) Regulation 2023/2854 Data Act](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32023R2854)
- [European Union (2016) Regulation 2016/679 General Data Protection Regulation](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32016R0679)
- [Court of Justice of the European Union (2020) Case C-311/18 Schrems II](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:62018CJ0311)
- [European Union (2024) Regulation 2024/1689 Artificial Intelligence Act](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32024R1689)
- [Board of Governors of the Federal Reserve System and Office of the Comptroller of the Currency (2011) SR 11-7 Supervisory Guidance on Model Risk Management](https://www.federalreserve.gov/boarddocs/srletters/2011/sr1107a1.pdf)
- [Prudential Regulation Authority (2023) SS1/23 Model Risk Management Principles for Banks](https://www.bankofengland.co.uk/prudential-regulation/publication/2023/may/model-risk-management-principles-for-banks-ss)
- [Meta (2024) Llama 3.3 Community License Agreement](https://github.com/meta-llama/llama-models/blob/main/models/llama3_3/LICENSE)
- [Open Source Initiative (2024) The Open Source AI Definition 1.0](https://opensource.org/ai/open-source-ai-definition)

---

## Research Skill Output

*(Full output from running the research skill — retained verbatim in the completed item. §§0–5 are the investigation; §6 seeds the Findings section below.)*

### §0 Initialise

Restate the research question. Confirm scope, constraints, and output format.

- Question restated: how do model choice, per-request selection, and operational and data controls change across subscription, managed-platform, and self-hosted stages, and does tuning begin on managed platforms or require self-hosting? [fact; source: https://davidamitchell.github.io/Research/research/2026-08-13-llm-consumption-maturity-ladder.html]
- Scope guardrail: legal analysis is bounded to the United States (US), European Union (EU), and United Kingdom (UK); the three named platforms are representative examples only. [assumption; source: https://davidamitchell.github.io/Research/research/2026-08-13-llm-consumption-maturity-ladder.html]
- Prior work applied: the cited consumption-ladder item found that stages can be mixed and routing can bridge managed and self-hosted models, and left cost, regulated-case, and tuning questions open. [fact; source: https://davidamitchell.github.io/Research/research/2026-08-13-llm-consumption-maturity-ladder.html]
- Prior work applied: the layered organisation item scopes adaptation approaches from prompting and retrieval through parameter-efficient tuning to full fine-tuning, which frames sub-question 4. [fact; source: https://davidamitchell.github.io/Research/research/2026-03-19-layered-org-llm-architecture.html]
- Output format: knowledge item with Findings mirrored from §6. [assumption; source: https://davidamitchell.github.io/Research/research/2026-08-13-llm-consumption-maturity-ladder.html]

### §1 Question Decomposition

Approach sub-questions broken into atomic questions — each answerable with a single evidence-based claim.

```text
Q1 stages: 1a selectable models per stage; 1b controls per stage; 1c team duties; 1d stack vs replace
Q2 prerequisites: 2a evaluation sets and judges; 2b calibrated escalation; 2c classification and region limits
Q3 tuning location: 3a native fine-tuning; 3b custom-weight import; 3c dedicated endpoints; 3d classification of imported-weight serving
Q4 adaptation choice: 4a retrieval or prompting vs tuning for four workloads; 4b smaller models
Q5 break-even: 5a independent cost studies; 5b formula; 5c sensitivity and multi-agent
Q6 drivers: 6a named regulated cases; 6b statutes; 6c licensing; 6d model-risk governance
```

### §2 Investigation

Evidence gathered per atomic question. Label each claim: **[fact]**, **[inference]**, or **[assumption]** with source.

**2.Q3 Tuning location on managed platforms (retrieved 2026-10-18).**

Amazon Bedrock offers platform-native fine-tuning for Amazon Nova, Titan image and multimodal embedding models, Claude 3 Haiku, and several Meta Llama 3.x sizes, with the Claude and Llama models listed in us-west-2 and the Nova models in us-east-1. [fact; source: https://docs.aws.amazon.com/bedrock/latest/userguide/custom-model-fine-tuning.html]

A customised Bedrock model cannot be invoked on demand; it requires purchased Provisioned Throughput, billed hourly per model unit with no-commitment, one-month, and six-month terms. [fact; source: https://docs.aws.amazon.com/bedrock/latest/userguide/prov-throughput.html]

Bedrock Custom Model Import accepts weights customised elsewhere, serves them through the same invocation interface with on-demand throughput, lists eu-central-1, us-east-1, us-east-2, and us-west-2, excludes batch inference and CloudFormation, and tells users to comply with the model licences. [fact; source: https://docs.aws.amazon.com/bedrock/latest/userguide/model-customization-import-model.html]

Microsoft Foundry offers two fine-tuning modalities: serverless, priced by consumption, and managed compute, where the customer supplies virtual machines and quota and OpenAI models are excluded. [fact; source: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/fine-tuning-overview]

Foundry supervised fine-tuning (SFT) covers Generative Pre-trained Transformer (GPT) 4o, GPT-4.1 variants, Llama 3.1, Phi-4, and Mistral models, and Direct Preference Optimization (DPO) and Reinforcement Fine-Tuning (RFT) are also offered for selected models. [fact; source: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/fine-tuning-overview]

The Foundry models page, last updated 2026-10-08, lists managed fine-tuning for Llama-3.3-70B and Qwen3-32B and states that global training is cheaper per token but does not offer data residency. [fact; source: https://learn.microsoft.com/en-us/azure/ai-foundry/openai/concepts/models]

Foundry deployment types span global, data-zone (US, EU, Asia-Pacific), and regional variants across standard, provisioned, and batch, and a Developer type for evaluating fine-tuned models has a 24-hour lifetime with no service-level agreement or residency guarantee. [fact; source: https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-models/concepts/deployment-types]

Foundry managed compute is dedicated compute billed per core hour, is the path for Hugging Face, NVIDIA Inference Microservices, and custom models, and carries no content filtering. [fact; source: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/deployments-overview]

Foundry custom-model import runs through the Fireworks integration: it accepts full weights, plus Low-Rank Adaptation (LoRA) adapters and draft models in preview, and deploys to Fireworks inference infrastructure in all global Azure regions except Azure Government. [fact; source: https://learn.microsoft.com/en-us/azure/foundry/how-to/fireworks/import-custom-models]

The Foundry Fireworks documentation states that data is shared between Microsoft and Fireworks AI, that Fireworks on Foundry is excluded from EU Data Boundary commitments, and that customers must assess their own compliance. [fact; source: https://learn.microsoft.com/en-us/azure/foundry/how-to/fireworks/enable-fireworks-models]

Vertex AI supports supervised tuning for Gemini 3.5 Flash, 3.1 Flash-Lite, 2.5 Pro, 2.5 Flash, and 2.5 Flash-Lite, and preference tuning for 2.5 Flash and Flash-Lite. [fact; source: https://cloud.google.com/vertex-ai/generative-ai/docs/models/tune-models]

Gemini tuning jobs run in us-central1 and europe-west4, with compute possibly offloaded to other US or EU regions, and tuned models are served from us and eu multi-region endpoints only. [fact; source: https://cloud.google.com/vertex-ai/generative-ai/docs/models/gemini-supervised-tuning]

Tuned Gemini models can be deployed only to shared public endpoints. [fact; source: https://cloud.google.com/vertex-ai/docs/predictions/choose-endpoint-type]

Vertex custom-weights deployment, in Preview, imports open models such as Llama, Gemma, and Qwen from a Cloud Storage bucket and serves them in any Model Garden region on customer-selected accelerators, with Virtual Private Cloud (VPC) Service Controls support. [fact; source: https://cloud.google.com/vertex-ai/generative-ai/docs/model-garden/deploy-models-with-custom-weights]

Self-deployed partner models on Vertex cannot have their weights exported. [fact; source: https://cloud.google.com/vertex-ai/generative-ai/docs/open-models/use-open-models]

Tuning therefore begins on managed platforms at all three vendors, while the weights of vendor frontier models stay with the vendor. [inference; source: https://docs.aws.amazon.com/bedrock/latest/userguide/custom-model-fine-tuning.html; https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/fine-tuning-overview; https://cloud.google.com/vertex-ai/generative-ai/docs/models/tune-models]

Imported-weight serving is best classed as managed-platform use with self-hosted-style weight control, because the customer owns the weights but the vendor operates the serving infrastructure. [inference; source: https://docs.aws.amazon.com/bedrock/latest/userguide/model-customization-import-model.html; https://learn.microsoft.com/en-us/azure/foundry/how-to/fireworks/import-custom-models]

Access note: Bedrock custom-model-import supported-architecture sub-pages, empty fetch result, coverage partial [assumption; source: https://docs.aws.amazon.com/bedrock/latest/userguide/model-customization-import-model.html]

**2.Q1 Stage optionality and stacking.**

The cited ladder item reports that consumption stages can be mixed and that routing can bridge managed and self-hosted models. [fact; source: https://davidamitchell.github.io/Research/research/2026-08-13-llm-consumption-maturity-ladder.html]

Stages stack rather than replace each other, because Bedrock serves imported weights through the same invocation interface as catalogue models, so one application can address a frontier model and a customer-owned model side by side. [inference; source: https://docs.aws.amazon.com/bedrock/latest/userguide/model-customization-import-model.html; https://davidamitchell.github.io/Research/research/2026-08-13-llm-consumption-maturity-ladder.html]

Control over weights, serving, and data path rises from the subscription stage to the self-hosted stage, and so does the operating burden, since the customer supplies accelerators, quota, and operations at the dedicated-endpoint and self-hosted levels. [inference; source: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/fine-tuning-overview; https://cloud.google.com/vertex-ai/generative-ai/docs/model-garden/deploy-models-with-custom-weights]

Access note: subscription-product documentation not fetched, stage claims rest on prior item [assumption; source: https://davidamitchell.github.io/Research/research/2026-08-13-llm-consumption-maturity-ladder.html]

**2.Q2 Prerequisites for dynamic selection.**

Large Language Model (LLM) judges reach over 80 percent agreement with human preferences but show position, verbosity, and self-enhancement biases. [fact; source: https://arxiv.org/abs/2306.05685]

FrugalGPT reports up to 98 percent cost reduction at GPT-4 parity, or about 4 percent higher accuracy at equal cost, by cascading across models. [fact; source: https://arxiv.org/abs/2305.05176]

The RouteLLM repository reports up to 85 percent cost reduction while keeping 95 percent of GPT-4 performance on the MT Bench multi-turn conversation benchmark, and recommends calibrating each routing threshold on a sample of the organisation's own incoming queries. [fact; source: https://github.com/lm-sys/RouteLLM]

Trusting a router therefore needs a workload-specific evaluation set, a judge validated against human labels, and a regression gate, because published savings come from public benchmarks rather than the organisation's traffic. [inference; source: https://arxiv.org/abs/2306.05685; https://github.com/lm-sys/RouteLLM]

Bedrock geographic cross-Region inference profiles pick a commercial Region inside a chosen geography such as the US or EU, whereas global profiles may use any Region. [fact; source: https://docs.aws.amazon.com/bedrock/latest/userguide/cross-region-inference.html]

Data classification should therefore restrict the set of eligible models and routes, with restricted data limited to geographic or single-Region profiles. [inference; source: https://docs.aws.amazon.com/bedrock/latest/userguide/cross-region-inference.html; https://learn.microsoft.com/en-us/azure/ai-foundry/openai/concepts/models]

Access note: RouteLLM paper figures not re-derived, repository statement used [assumption; source: https://github.com/lm-sys/RouteLLM]

**2.Q4 Retrieval, prompting, tuning, and smaller models.**

Retrieval-augmented generation (RAG) consistently outperformed unsupervised fine-tuning for injecting knowledge, both for existing and new facts. [fact; source: https://arxiv.org/abs/2312.05934]

RAG beats fine-tuning by a large margin on less popular knowledge, although fine-tuning also helps across popularity levels. [fact; source: https://arxiv.org/abs/2403.01432]

Policy question answering and compliance checking depend on frequently changing, citable text, so retrieval and prompting should come before tuning for those two workloads. [inference; source: https://arxiv.org/abs/2312.05934; https://arxiv.org/abs/2403.01432]

Classification and extraction depend on stable output formats and label boundaries rather than on injected facts, so tuning a smaller model is a plausible fit, but no study fetched here tests these two regulated workloads. [assumption; source: https://arxiv.org/abs/2506.02153]

Small language models are argued to be sufficient for many repetitive agentic subtasks, with heterogeneous systems the natural design. [fact; source: https://arxiv.org/abs/2506.02153]

An ensemble of small models judged by a small model reached 97.34 percent strict prompt accuracy on the 541-prompt Instruction-Following Evaluation (IFEval) benchmark, 5.81 points above gpt-5.4, at lower cost but with additional test-time tokens. [fact; source: https://arxiv.org/abs/2610.00954]

**2.Q5 Self-hosting cost and break-even.**

The cited study reports break-even in months for small models, about two years for medium models, and about five years for large models, with viability above roughly 50 million tokens per month or under strict residency requirements. [fact; source: https://arxiv.org/abs/2509.18101]

A consumer-GPU study reports electricity-only cost of 0.001 to 0.04 dollars per million tokens and hardware break-even in under four months at 30 million tokens per day, with 2 to 4 percent quality loss from four-bit quantisation. [fact; source: https://arxiv.org/abs/2601.09527]

The consumer-GPU result excludes staff, redundancy, and enterprise hardware, so it bounds the optimistic end rather than representing regulated-enterprise cost. [inference; source: https://arxiv.org/abs/2601.09527]

Break-even formula: monthly Application Programming Interface (API) cost is T x [(1 - r) x p_in x (1 - c x d) + r x p_out] x (1 - b x s), where T is monthly tokens, r the output share, p_in and p_out the per-million-token prices, c the cache-hit rate, d the cache discount, b the batch share, and s the batch discount; monthly self-hosting cost is ceil(T / (q x u x 2,629,800)) x h x 730 + O, where q is sustained tokens per second per GPU, u utilisation, h the GPU hourly cost, and O the operations-staff cost. [inference; source: https://arxiv.org/abs/2509.18101]

Illustrative case with assumed inputs, not observed prices: blended API price 2 dollars per million tokens, h = 4 dollars, q = 3,000, u = 0.4, O = 15,000 dollars per month gives per-token self-hosting cost of about 0.93 dollars per million and break-even near 14 billion tokens per month. [assumption; source: https://arxiv.org/abs/2509.18101]

In the same illustration, halving q to 1,500 raises per-token cost to about 1.85 dollars per million and moves break-even to roughly 100 billion tokens per month, which shows that cost per token at the margin, not fixed staff cost, decides viability. [assumption; source: https://arxiv.org/abs/2509.18101]

The illustrative break-even is orders of magnitude above the roughly 50 million tokens per month in the cited study, so the threshold is dominated by assumed prices, model size, and utilisation and cannot be transferred between studies. [inference; source: https://arxiv.org/abs/2509.18101; https://arxiv.org/abs/2601.09527]

Heterogeneous agent teams reach up to 44 percent higher accuracy at equal cost, or up to 12 times lower per-task cost, under a unified cost model spanning APIs and self-hosted models. [fact; source: https://arxiv.org/abs/2606.20629]

Multi-agent orchestration raises tokens per task, which pushes volume towards break-even, while hybrid placement of cheap roles on self-hosted models and hard roles on APIs captures part of the saving without full self-hosting. [inference; source: https://arxiv.org/abs/2606.20629; https://arxiv.org/abs/2610.00954]

**2.Q6 Regulatory, licensing, and model-risk drivers.**

18 U.S.C. 2713 obliges providers of electronic communication or remote computing services to preserve and disclose data in their possession, custody, or control regardless of whether it is located inside or outside the United States. [fact; source: https://www.law.cornell.edu/uscode/text/18/2713]

The EU Data Act has a chapter on unlawful international governmental access to non-personal data and requires data-processing service providers to describe measures preventing access that conflicts with Union or Member State law. [fact; source: https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32023R2854]

The Data Act recitals state that switching charges should be abolished three years after entry into force, which lowers exit cost for services in scope. [fact; source: https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32023R2854]

The General Data Protection Regulation (GDPR) sets a general principle for transfers of personal data to third countries. [fact; source: https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32016R0679]

The Court of Justice of the EU held the Privacy Shield decision invalid in Schrems II. [fact; source: https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:62018CJ0311]

Data location alone does not settle jurisdictional exposure, since a US-headquartered provider's data held in the EU remains within the statutory reach of 18 U.S.C. 2713, while customer-operated hardware outside any provider is not a provider's data. [inference; source: https://www.law.cornell.edu/uscode/text/18/2713; https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:62018CJ0311]

The Digital Operational Resilience Act (DORA), Article 28(8), requires financial entities to put exit strategies in place for Information and Communication Technology (ICT) services supporting critical or important functions. [fact; source: https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32022R2554]

The Federal Reserve and Office of the Comptroller of the Currency guidance SR 11-7 requires vendor models to be validated like in-house models, expects banks to hold in-house knowledge in case a vendor stops supporting a model, and expects contingency plans for vendor-model unavailability. [fact; source: https://www.federalreserve.gov/boarddocs/srletters/2011/sr1107a1.pdf]

The Prudential Regulation Authority's SS1/23 applies to models developed in-house or externally, including vendor models, with the current version effective 23 April 2026. [fact; source: https://www.bankofengland.co.uk/prudential-regulation/publication/2023/may/model-risk-management-principles-for-banks-ss]

Exit planning and model-risk validation therefore apply at every stage, so they do not by themselves require self-hosting. [inference; source: https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32022R2554; https://www.federalreserve.gov/boarddocs/srletters/2011/sr1107a1.pdf]

The Artificial Intelligence Act recitals state that a party making a substantial modification to a high-risk system, or changing the intended purpose of a general-purpose system so that it becomes high-risk, takes on provider obligations. [fact; source: https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32024R1689]

Tuning a model for a high-risk use may therefore shift provider obligations onto the tuning organisation at any stage. [inference; source: https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32024R1689]

The Llama 3.3 licence grants use, modification, and distribution rights, requires "Built with Llama" attribution on distribution, binds use to an acceptable use policy, requires a separate licence above 700 million monthly active users, and leaves ownership of customer-made derivatives with the customer. [fact; source: https://github.com/meta-llama/llama-models/blob/main/models/llama3_3/LICENSE]

The Open Source Initiative definition requires data information, training code, and parameters under approved terms before a model counts as open source, so open weights under a bespoke licence fall short of it. [inference; source: https://opensource.org/ai/open-source-ai-definition; https://github.com/meta-llama/llama-models/blob/main/models/llama3_3/LICENSE]

Licence obligations travel with the weights across managed import and self-hosting, and Bedrock tells importers to comply with model licences. [inference; source: https://docs.aws.amazon.com/bedrock/latest/userguide/model-customization-import-model.html; https://github.com/meta-llama/llama-models/blob/main/models/llama3_3/LICENSE]

The cited ladder item reports no named regulated-organisation self-hosting case. [fact; source: https://davidamitchell.github.io/Research/research/2026-08-13-llm-consumption-maturity-ladder.html]

Access note: BNP Paribas press pages on an in-house LLM service and a Mistral partnership, fetch blocked, no named-case claim made [assumption; source: https://davidamitchell.github.io/Research/research/2026-08-13-llm-consumption-maturity-ladder.html]

Access note: web search for a named bank exit or United States CLOUD Act conflict case, no named case found, anonymous vendor case study not used [assumption; source: https://davidamitchell.github.io/Research/research/2026-08-13-llm-consumption-maturity-ladder.html]

### §3 Reasoning

Facts, inferences, and assumptions explicitly separated. No unsupported generalisations or narrative leaps.

1. Vendor documentation establishes that native tuning, custom-weight import, and dedicated endpoints exist on all three platforms. [fact; source: https://docs.aws.amazon.com/bedrock/latest/userguide/custom-model-fine-tuning.html; https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/fine-tuning-overview; https://cloud.google.com/vertex-ai/generative-ai/docs/models/tune-models]
2. Tuning is therefore a managed-platform capability and not a self-hosting privilege, while ownership of weights is what self-hosting adds. [inference; source: https://cloud.google.com/vertex-ai/generative-ai/docs/open-models/use-open-models; https://docs.aws.amazon.com/bedrock/latest/userguide/model-customization-import-model.html]
3. Break-even depends on cost per token at the margin, which depends on assumed throughput and utilisation. [inference; source: https://arxiv.org/abs/2509.18101; https://arxiv.org/abs/2601.09527]
4. The statutes and guidance fetched require exit planning, validation, and transfer controls at every stage, so they raise the cost of lock-in without mandating self-hosting. [inference; source: https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32022R2554; https://www.federalreserve.gov/boarddocs/srletters/2011/sr1107a1.pdf; https://www.bankofengland.co.uk/prudential-regulation/publication/2023/may/model-risk-management-principles-for-banks-ss]
5. Named regulated-organisation self-hosting evidence could not be verified, so residency and sovereignty motives are supported by law, not by cases. [inference; source: https://davidamitchell.github.io/Research/research/2026-08-13-llm-consumption-maturity-ladder.html]

### §4 Consistency Check

Internal contradictions identified and resolved (or explicitly flagged where unresolvable).

```text
contradiction_scan: resolved
tension: cited study break-even near 50M tokens/month vs illustrative 14B tokens/month; resolved as differing assumed prices, model size, utilisation
tension: tuning described as managed capability vs ladder item treating tuning as self-hosting; resolved by platform documentation
confidence_adjustment: break-even kept at medium; regulated-case evidence flagged as gap
scope_guardrail: maintained
```

### §5 Depth and Breadth Expansion

Findings re-examined through relevant lenses (technical, regulatory, economic, historical, behavioural).

Technical lens: dedicated endpoints trade convenience for duties, since Foundry managed compute has no content filtering and leaves capacity with the customer. [fact; source: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/deployments-overview]

Technical lens: regional availability is uneven, with Bedrock Claude and Llama tuning in us-west-2, Nova in us-east-1, and Gemini tuning in us-central1 and europe-west4. [fact; source: https://docs.aws.amazon.com/bedrock/latest/userguide/custom-model-fine-tuning.html; https://cloud.google.com/vertex-ai/generative-ai/docs/models/gemini-supervised-tuning]

Regulatory lens: a European organisation tuning in us-west-2 may breach residency requirements, so tuning region must be checked against data classification. [inference; source: https://docs.aws.amazon.com/bedrock/latest/userguide/custom-model-fine-tuning.html; https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32016R0679]

Economic lens: a multi-year hardware commitment competes with falling API prices and new model generations, which the cited study treats through scenario ranges. [inference; source: https://arxiv.org/abs/2509.18101]

Economic lens: provisioned capacity on managed platforms bills hourly even when idle, which resembles self-hosting fixed cost without ownership of hardware. [inference; source: https://docs.aws.amazon.com/bedrock/latest/userguide/prov-throughput.html]

Behavioural lens: rival model, that self-hosting should be the default for regulated firms, is weakened because exit-planning and validation duties apply equally to vendors. [inference; source: https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32022R2554; https://www.federalreserve.gov/boarddocs/srletters/2011/sr1107a1.pdf]

Behavioural lens: rival model, that managed platforms are always sufficient, is weakened by the Fireworks data-sharing and EU Data Boundary exclusion for imported weights on Foundry. [inference; source: https://learn.microsoft.com/en-us/azure/foundry/how-to/fireworks/enable-fireworks-models]

### §6 Synthesis

*(This section seeds the Findings below.)*

**Executive summary:**

Model tuning begins on managed platforms, not at self-hosting, because Amazon Bedrock, Microsoft Foundry, and Google Vertex AI each offer native fine-tuning, and self-hosting adds ownership of the weights and serving path rather than the ability to tune. [inference; source: https://docs.aws.amazon.com/bedrock/latest/userguide/custom-model-fine-tuning.html; https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/fine-tuning-overview; https://cloud.google.com/vertex-ai/generative-ai/docs/models/tune-models]
The stages stack rather than replace one another, since imported weights can be served beside catalogue models through one interface and routing can bridge them. [inference; source: https://docs.aws.amazon.com/bedrock/latest/userguide/model-customization-import-model.html; https://davidamitchell.github.io/Research/research/2026-08-13-llm-consumption-maturity-ladder.html]
Self-hosting break-even is dominated by assumed throughput, utilisation, and price, with published estimates ranging from months to years. [inference; source: https://arxiv.org/abs/2509.18101; https://arxiv.org/abs/2601.09527]
Residency, extraterritorial access, exit planning, and model risk each raise the control needed at every stage without mandating self-hosting. [inference; source: https://www.law.cornell.edu/uscode/text/18/2713; https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32022R2554; https://www.federalreserve.gov/boarddocs/srletters/2011/sr1107a1.pdf]
The primary uncertainty is that no named regulated organisation's self-hosting decision was verified. [inference; source: https://davidamitchell.github.io/Research/research/2026-08-13-llm-consumption-maturity-ladder.html]

**Key findings:**

1. Amazon Bedrock, Microsoft Foundry, and Google Vertex AI each provide platform-native supervised fine-tuning for selected models, so tuning is available before any self-hosting step. ([fact]; high confidence; source: https://docs.aws.amazon.com/bedrock/latest/userguide/custom-model-fine-tuning.html; https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/fine-tuning-overview; https://cloud.google.com/vertex-ai/generative-ai/docs/models/tune-models)
2. Tuned models stay inside platform serving constraints: Bedrock requires purchased Provisioned Throughput for customised models and Vertex deploys tuned Gemini models only to shared public endpoints. ([fact]; high confidence; source: https://docs.aws.amazon.com/bedrock/latest/userguide/prov-throughput.html; https://cloud.google.com/vertex-ai/docs/predictions/choose-endpoint-type)
3. All three platforms accept externally trained weights, through Bedrock Custom Model Import, the Foundry Fireworks integration, and Vertex custom weights in Preview, but regions and data terms differ, including a Foundry exclusion from EU Data Boundary commitments. ([fact]; high confidence; source: https://docs.aws.amazon.com/bedrock/latest/userguide/model-customization-import-model.html; https://learn.microsoft.com/en-us/azure/foundry/how-to/fireworks/enable-fireworks-models; https://cloud.google.com/vertex-ai/generative-ai/docs/model-garden/deploy-models-with-custom-weights)
4. Imported-weight serving is best classed as managed-platform use with self-hosted-style weight control, and stages stack because one interface can address both catalogue and customer-owned models. ([inference]; medium confidence; source: https://docs.aws.amazon.com/bedrock/latest/userguide/model-customization-import-model.html; https://davidamitchell.github.io/Research/research/2026-08-13-llm-consumption-maturity-ladder.html)
5. Trusting dynamic routing requires a workload-specific evaluation set, a human-validated judge, and calibrated thresholds, because public-benchmark savings and judge agreement above 80 percent come with documented biases. ([inference]; medium confidence; source: https://arxiv.org/abs/2306.05685; https://github.com/lm-sys/RouteLLM; https://arxiv.org/abs/2305.05176)
6. Retrieval and prompting should precede tuning for policy question answering and compliance checking, because two independent studies find retrieval beats fine-tuning for knowledge injection. ([inference]; medium confidence; source: https://arxiv.org/abs/2312.05934; https://arxiv.org/abs/2403.01432)
7. Self-hosting break-even is set by cost per token at the margin, so halving assumed GPU throughput in an illustrative case moves break-even from near 14 billion to roughly 100 billion tokens per month. ([assumption]; medium confidence; source: https://arxiv.org/abs/2509.18101; https://arxiv.org/abs/2601.09527)
8. Independent cost evidence ranges from months to about five years to break even, and the optimistic consumer-GPU result excludes staff and redundancy, so no single threshold transfers between organisations. ([inference]; medium confidence; source: https://arxiv.org/abs/2509.18101; https://arxiv.org/abs/2601.09527)
9. Hybrid placement of cheap agent roles on self-hosted models and hard roles on APIs lowered per-task cost by up to 12 times in one study, which suggests partial self-hosting can capture savings before full break-even. ([inference]; medium confidence; source: https://arxiv.org/abs/2606.20629; https://arxiv.org/abs/2610.00954)
10. Exit planning under the Digital Operational Resilience Act and vendor-model validation under SR 11-7 and SS1/23 apply to vendor services at every stage, so these duties raise lock-in cost without requiring self-hosting. ([inference]; high confidence; source: https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32022R2554; https://www.federalreserve.gov/boarddocs/srletters/2011/sr1107a1.pdf; https://www.bankofengland.co.uk/prudential-regulation/publication/2023/may/model-risk-management-principles-for-banks-ss)
11. Data location alone does not settle jurisdictional exposure, because 18 U.S.C. 2713 reaches provider-held data wherever it is stored, so sovereignty depends on who operates the infrastructure. ([inference]; medium confidence; source: https://www.law.cornell.edu/uscode/text/18/2713; https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32023R2854)
12. Open-weight licence obligations such as attribution, an acceptable use policy, and a 700 million monthly-user clause travel with the weights across managed import and self-hosting, and bespoke licences do not meet the Open Source Initiative definition. ([inference]; medium confidence; source: https://github.com/meta-llama/llama-models/blob/main/models/llama3_3/LICENSE; https://opensource.org/ai/open-source-ai-definition)

**Evidence map:**

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [fact] Native fine-tuning exists on all three platforms | https://docs.aws.amazon.com/bedrock/latest/userguide/custom-model-fine-tuning.html; https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/fine-tuning-overview; https://cloud.google.com/vertex-ai/generative-ai/docs/models/tune-models | high | vendor docs, retrieved 2026-10-18 |
| [fact] Tuned-model serving constraints on Bedrock and Vertex | https://docs.aws.amazon.com/bedrock/latest/userguide/prov-throughput.html; https://cloud.google.com/vertex-ai/docs/predictions/choose-endpoint-type | high | vendor docs |
| [fact] Custom-weight import on all three platforms | https://docs.aws.amazon.com/bedrock/latest/userguide/model-customization-import-model.html; https://learn.microsoft.com/en-us/azure/foundry/how-to/fireworks/import-custom-models; https://cloud.google.com/vertex-ai/generative-ai/docs/model-garden/deploy-models-with-custom-weights | high | Vertex in Preview |
| [inference] Stages stack and imported serving is platform use | https://docs.aws.amazon.com/bedrock/latest/userguide/model-customization-import-model.html; https://davidamitchell.github.io/Research/research/2026-08-13-llm-consumption-maturity-ladder.html | medium | classification is a judgment |
| [inference] Routing prerequisites | https://arxiv.org/abs/2306.05685; https://github.com/lm-sys/RouteLLM; https://arxiv.org/abs/2305.05176 | medium | public benchmarks |
| [inference] Retrieval before tuning for knowledge tasks | https://arxiv.org/abs/2312.05934; https://arxiv.org/abs/2403.01432 | medium | mapped to workloads by inference |
| [assumption] Break-even sensitivity illustration | https://arxiv.org/abs/2509.18101; https://arxiv.org/abs/2601.09527 | medium | inputs are invented |
| [inference] Cost evidence ranges widely | https://arxiv.org/abs/2509.18101; https://arxiv.org/abs/2601.09527 | medium | differing assumptions |
| [inference] Hybrid placement lowers per-task cost | https://arxiv.org/abs/2606.20629; https://arxiv.org/abs/2610.00954 | medium | benchmark settings |
| [inference] Exit and validation duties apply at every stage | https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32022R2554; https://www.federalreserve.gov/boarddocs/srletters/2011/sr1107a1.pdf; https://www.bankofengland.co.uk/prudential-regulation/publication/2023/may/model-risk-management-principles-for-banks-ss | high | three regulators |
| [inference] Location does not settle jurisdiction | https://www.law.cornell.edu/uscode/text/18/2713; https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32023R2854 | medium | legal reading |
| [inference] Licence obligations travel with weights | https://github.com/meta-llama/llama-models/blob/main/models/llama3_3/LICENSE; https://opensource.org/ai/open-source-ai-definition | medium | one licence examined |

**Assumptions:**

Classification and extraction workloads are assumed to depend on stable formats rather than injected facts. [assumption; source: https://arxiv.org/abs/2506.02153] That assumption is reasonable because small-model arguments focus on repetitive, scoped subtasks, but no fetched study tests these workloads in regulated settings. [assumption; source: https://arxiv.org/abs/2506.02153]

Break-even inputs of 2 dollars per million tokens, 4 dollars per GPU-hour, 3,000 tokens per second, 40 percent utilisation, and 15,000 dollars monthly operations cost are illustrative values only. [assumption; source: https://arxiv.org/abs/2509.18101] They are chosen to show the formula's sensitivity and are not observed prices from any vendor. [assumption; source: https://arxiv.org/abs/2509.18101]

Subscription-stage selection limits are assumed to match the ladder item's description, because no subscription product documentation was fetched. [assumption; source: https://davidamitchell.github.io/Research/research/2026-08-13-llm-consumption-maturity-ladder.html] The ladder item is the only prior source in this repository that characterises that stage. [assumption; source: https://davidamitchell.github.io/Research/research/2026-08-13-llm-consumption-maturity-ladder.html]

**Analysis:**

Vendor documentation was weighted as definitive for what each platform offers on the retrieval date and as silent on future availability. [inference; source: https://learn.microsoft.com/en-us/azure/ai-foundry/openai/concepts/models] Peer-reviewed or preprint cost studies were weighted above vendor total-cost-of-ownership blogs, which were excluded as non-independent. [inference; source: https://arxiv.org/abs/2509.18101]
The layered organisation item frames adaptation as a spectrum from prompting and retrieval to fine-tuning, and the platform evidence places the early part of that spectrum on managed platforms. [inference; source: https://davidamitchell.github.io/Research/research/2026-03-19-layered-org-llm-architecture.html; https://cloud.google.com/vertex-ai/generative-ai/docs/models/tune-models]
The rival view that regulated firms should self-host by default is weakened because exit planning and validation duties apply equally to vendor services. [inference; source: https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32022R2554; https://www.federalreserve.gov/boarddocs/srletters/2011/sr1107a1.pdf]
The rival view that managed platforms always suffice is weakened by the Fireworks data-sharing terms and the EU Data Boundary exclusion for imported weights on Foundry. [inference; source: https://learn.microsoft.com/en-us/azure/foundry/how-to/fireworks/enable-fireworks-models]
Sovereignty is a stronger driver of self-hosting than cost for firms exposed to extraterritorial access, though this item verifies the law and not any firm's decision. [inference; source: https://www.law.cornell.edu/uscode/text/18/2713; https://davidamitchell.github.io/Research/research/2026-08-13-llm-consumption-maturity-ladder.html]

**Risks, gaps, uncertainties:**

- No named regulated organisation's self-hosting rationale was verified, because primary BNP Paribas pages were not retrievable and searches found no named case. [inference; source: https://davidamitchell.github.io/Research/research/2026-08-13-llm-consumption-maturity-ladder.html]
- Independent production cost evidence is limited to preprints with benchmark or consumer-hardware settings, and the worked break-even uses assumed inputs. [inference; source: https://arxiv.org/abs/2509.18101; https://arxiv.org/abs/2601.09527]
- Platform features change quickly and some paths are Preview or classic-documentation only, so regional availability should be rechecked before design decisions. [inference; source: https://cloud.google.com/vertex-ai/generative-ai/docs/model-garden/deploy-models-with-custom-weights; https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/deployments-overview]
- Only one open-weight licence was read, so licensing conclusions may not extend to Apache 2.0 or other terms. [inference; source: https://github.com/meta-llama/llama-models/blob/main/models/llama3_3/LICENSE]
- Legal readings are engineering interpretations and not legal advice, and UK data-protection law after the 2025 reforms was not analysed. [assumption; source: https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32016R0679]

**Open questions:**

- Which named regulated organisations have disclosed self-hosting for residency or sovereignty reasons?
- How do tuned small models compare with retrieval on regulated classification and extraction tasks in controlled studies?
- How do Apache 2.0 and other open-weight licences differ from the Llama licence in obligations on derivatives?

### §7 Recursive Review

Final pass: every section justified, all threads synthesised, every claim sourced or labelled, all uncertainties explicit.

```text
review_result: pass
acronym_audit: passed
parity_check: passed
source_audit: every cited URL listed in Sources
gap_record: named regulated case unverified; BNP Paribas pages blocked
```

---

## Findings

*(Populated from §6 Synthesis above.)*

### Executive Summary

Model tuning begins on managed platforms, not at self-hosting, because Amazon Bedrock, Microsoft Foundry, and Google Vertex AI each offer native fine-tuning, and self-hosting adds ownership of the weights and serving path rather than the ability to tune. [inference; source: https://docs.aws.amazon.com/bedrock/latest/userguide/custom-model-fine-tuning.html; https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/fine-tuning-overview; https://cloud.google.com/vertex-ai/generative-ai/docs/models/tune-models]
The stages stack rather than replace one another, since imported weights can be served beside catalogue models through one interface and routing can bridge them. [inference; source: https://docs.aws.amazon.com/bedrock/latest/userguide/model-customization-import-model.html; https://davidamitchell.github.io/Research/research/2026-08-13-llm-consumption-maturity-ladder.html]
Self-hosting break-even is dominated by assumed throughput, utilisation, and price, with published estimates ranging from months to years. [inference; source: https://arxiv.org/abs/2509.18101; https://arxiv.org/abs/2601.09527]
Residency, extraterritorial access, exit planning, and model risk each raise the control needed at every stage without mandating self-hosting. [inference; source: https://www.law.cornell.edu/uscode/text/18/2713; https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32022R2554; https://www.federalreserve.gov/boarddocs/srletters/2011/sr1107a1.pdf]
The primary uncertainty is that no named regulated organisation's self-hosting decision was verified. [inference; source: https://davidamitchell.github.io/Research/research/2026-08-13-llm-consumption-maturity-ladder.html]

### Key Findings

1. Amazon Bedrock, Microsoft Foundry, and Google Vertex AI each provide platform-native supervised fine-tuning for selected models, so tuning is available before any self-hosting step. ([fact]; high confidence; source: https://docs.aws.amazon.com/bedrock/latest/userguide/custom-model-fine-tuning.html; https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/fine-tuning-overview; https://cloud.google.com/vertex-ai/generative-ai/docs/models/tune-models)
2. Tuned models stay inside platform serving constraints: Bedrock requires purchased Provisioned Throughput for customised models and Vertex deploys tuned Gemini models only to shared public endpoints. ([fact]; high confidence; source: https://docs.aws.amazon.com/bedrock/latest/userguide/prov-throughput.html; https://cloud.google.com/vertex-ai/docs/predictions/choose-endpoint-type)
3. All three platforms accept externally trained weights, through Bedrock Custom Model Import, the Foundry Fireworks integration, and Vertex custom weights in Preview, but regions and data terms differ, including a Foundry exclusion from EU Data Boundary commitments. ([fact]; high confidence; source: https://docs.aws.amazon.com/bedrock/latest/userguide/model-customization-import-model.html; https://learn.microsoft.com/en-us/azure/foundry/how-to/fireworks/enable-fireworks-models; https://cloud.google.com/vertex-ai/generative-ai/docs/model-garden/deploy-models-with-custom-weights)
4. Imported-weight serving is best classed as managed-platform use with self-hosted-style weight control, and stages stack because one interface can address both catalogue and customer-owned models. ([inference]; medium confidence; source: https://docs.aws.amazon.com/bedrock/latest/userguide/model-customization-import-model.html; https://davidamitchell.github.io/Research/research/2026-08-13-llm-consumption-maturity-ladder.html)
5. Trusting dynamic routing requires a workload-specific evaluation set, a human-validated judge, and calibrated thresholds, because public-benchmark savings and judge agreement above 80 percent come with documented biases. ([inference]; medium confidence; source: https://arxiv.org/abs/2306.05685; https://github.com/lm-sys/RouteLLM; https://arxiv.org/abs/2305.05176)
6. Retrieval and prompting should precede tuning for policy question answering and compliance checking, because two independent studies find retrieval beats fine-tuning for knowledge injection. ([inference]; medium confidence; source: https://arxiv.org/abs/2312.05934; https://arxiv.org/abs/2403.01432)
7. Self-hosting break-even is set by cost per token at the margin, so halving assumed GPU throughput in an illustrative case moves break-even from near 14 billion to roughly 100 billion tokens per month. ([assumption]; medium confidence; source: https://arxiv.org/abs/2509.18101; https://arxiv.org/abs/2601.09527)
8. Independent cost evidence ranges from months to about five years to break even, and the optimistic consumer-GPU result excludes staff and redundancy, so no single threshold transfers between organisations. ([inference]; medium confidence; source: https://arxiv.org/abs/2509.18101; https://arxiv.org/abs/2601.09527)
9. Hybrid placement of cheap agent roles on self-hosted models and hard roles on APIs lowered per-task cost by up to 12 times in one study, which suggests partial self-hosting can capture savings before full break-even. ([inference]; medium confidence; source: https://arxiv.org/abs/2606.20629; https://arxiv.org/abs/2610.00954)
10. Exit planning under the Digital Operational Resilience Act and vendor-model validation under SR 11-7 and SS1/23 apply to vendor services at every stage, so these duties raise lock-in cost without requiring self-hosting. ([inference]; high confidence; source: https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32022R2554; https://www.federalreserve.gov/boarddocs/srletters/2011/sr1107a1.pdf; https://www.bankofengland.co.uk/prudential-regulation/publication/2023/may/model-risk-management-principles-for-banks-ss)
11. Data location alone does not settle jurisdictional exposure, because 18 U.S.C. 2713 reaches provider-held data wherever it is stored, so sovereignty depends on who operates the infrastructure. ([inference]; medium confidence; source: https://www.law.cornell.edu/uscode/text/18/2713; https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32023R2854)
12. Open-weight licence obligations such as attribution, an acceptable use policy, and a 700 million monthly-user clause travel with the weights across managed import and self-hosting, and bespoke licences do not meet the Open Source Initiative definition. ([inference]; medium confidence; source: https://github.com/meta-llama/llama-models/blob/main/models/llama3_3/LICENSE; https://opensource.org/ai/open-source-ai-definition)

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [fact] Native fine-tuning exists on all three platforms | https://docs.aws.amazon.com/bedrock/latest/userguide/custom-model-fine-tuning.html; https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/fine-tuning-overview; https://cloud.google.com/vertex-ai/generative-ai/docs/models/tune-models | high | vendor docs, retrieved 2026-10-18 |
| [fact] Tuned-model serving constraints on Bedrock and Vertex | https://docs.aws.amazon.com/bedrock/latest/userguide/prov-throughput.html; https://cloud.google.com/vertex-ai/docs/predictions/choose-endpoint-type | high | vendor docs |
| [fact] Custom-weight import on all three platforms | https://docs.aws.amazon.com/bedrock/latest/userguide/model-customization-import-model.html; https://learn.microsoft.com/en-us/azure/foundry/how-to/fireworks/import-custom-models; https://cloud.google.com/vertex-ai/generative-ai/docs/model-garden/deploy-models-with-custom-weights | high | Vertex in Preview |
| [inference] Stages stack and imported serving is platform use | https://docs.aws.amazon.com/bedrock/latest/userguide/model-customization-import-model.html; https://davidamitchell.github.io/Research/research/2026-08-13-llm-consumption-maturity-ladder.html | medium | classification is a judgment |
| [inference] Routing prerequisites | https://arxiv.org/abs/2306.05685; https://github.com/lm-sys/RouteLLM; https://arxiv.org/abs/2305.05176 | medium | public benchmarks |
| [inference] Retrieval before tuning for knowledge tasks | https://arxiv.org/abs/2312.05934; https://arxiv.org/abs/2403.01432 | medium | mapped to workloads by inference |
| [assumption] Break-even sensitivity illustration | https://arxiv.org/abs/2509.18101; https://arxiv.org/abs/2601.09527 | medium | inputs are invented |
| [inference] Cost evidence ranges widely | https://arxiv.org/abs/2509.18101; https://arxiv.org/abs/2601.09527 | medium | differing assumptions |
| [inference] Hybrid placement lowers per-task cost | https://arxiv.org/abs/2606.20629; https://arxiv.org/abs/2610.00954 | medium | benchmark settings |
| [inference] Exit and validation duties apply at every stage | https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32022R2554; https://www.federalreserve.gov/boarddocs/srletters/2011/sr1107a1.pdf; https://www.bankofengland.co.uk/prudential-regulation/publication/2023/may/model-risk-management-principles-for-banks-ss | high | three regulators |
| [inference] Location does not settle jurisdiction | https://www.law.cornell.edu/uscode/text/18/2713; https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32023R2854 | medium | legal reading |
| [inference] Licence obligations travel with weights | https://github.com/meta-llama/llama-models/blob/main/models/llama3_3/LICENSE; https://opensource.org/ai/open-source-ai-definition | medium | one licence examined |

### Assumptions

Classification and extraction workloads are assumed to depend on stable formats rather than injected facts. [assumption; source: https://arxiv.org/abs/2506.02153] That assumption is reasonable because small-model arguments focus on repetitive, scoped subtasks, but no fetched study tests these workloads in regulated settings. [assumption; source: https://arxiv.org/abs/2506.02153]

Break-even inputs of 2 dollars per million tokens, 4 dollars per GPU-hour, 3,000 tokens per second, 40 percent utilisation, and 15,000 dollars monthly operations cost are illustrative values only. [assumption; source: https://arxiv.org/abs/2509.18101] They are chosen to show the formula's sensitivity and are not observed prices from any vendor. [assumption; source: https://arxiv.org/abs/2509.18101]

Subscription-stage selection limits are assumed to match the ladder item's description, because no subscription product documentation was fetched. [assumption; source: https://davidamitchell.github.io/Research/research/2026-08-13-llm-consumption-maturity-ladder.html] The ladder item is the only prior source in this repository that characterises that stage. [assumption; source: https://davidamitchell.github.io/Research/research/2026-08-13-llm-consumption-maturity-ladder.html]

### Analysis

Vendor documentation was weighted as definitive for what each platform offers on the retrieval date and as silent on future availability. [inference; source: https://learn.microsoft.com/en-us/azure/ai-foundry/openai/concepts/models] Peer-reviewed or preprint cost studies were weighted above vendor total-cost-of-ownership blogs, which were excluded as non-independent. [inference; source: https://arxiv.org/abs/2509.18101]
The layered organisation item frames adaptation as a spectrum from prompting and retrieval to fine-tuning, and the platform evidence places the early part of that spectrum on managed platforms. [inference; source: https://davidamitchell.github.io/Research/research/2026-03-19-layered-org-llm-architecture.html; https://cloud.google.com/vertex-ai/generative-ai/docs/models/tune-models]
The rival view that regulated firms should self-host by default is weakened because exit planning and validation duties apply equally to vendor services. [inference; source: https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32022R2554; https://www.federalreserve.gov/boarddocs/srletters/2011/sr1107a1.pdf]
The rival view that managed platforms always suffice is weakened by the Fireworks data-sharing terms and the EU Data Boundary exclusion for imported weights on Foundry. [inference; source: https://learn.microsoft.com/en-us/azure/foundry/how-to/fireworks/enable-fireworks-models]
Sovereignty is a stronger driver of self-hosting than cost for firms exposed to extraterritorial access, though this item verifies the law and not any firm's decision. [inference; source: https://www.law.cornell.edu/uscode/text/18/2713; https://davidamitchell.github.io/Research/research/2026-08-13-llm-consumption-maturity-ladder.html]

### Risks, Gaps, and Uncertainties

- No named regulated organisation's self-hosting rationale was verified, because primary BNP Paribas pages were not retrievable and searches found no named case. [inference; source: https://davidamitchell.github.io/Research/research/2026-08-13-llm-consumption-maturity-ladder.html]
- Independent production cost evidence is limited to preprints with benchmark or consumer-hardware settings, and the worked break-even uses assumed inputs. [inference; source: https://arxiv.org/abs/2509.18101; https://arxiv.org/abs/2601.09527]
- Platform features change quickly and some paths are Preview or classic-documentation only, so regional availability should be rechecked before design decisions. [inference; source: https://cloud.google.com/vertex-ai/generative-ai/docs/model-garden/deploy-models-with-custom-weights; https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/deployments-overview]
- Only one open-weight licence was read, so licensing conclusions may not extend to Apache 2.0 or other terms. [inference; source: https://github.com/meta-llama/llama-models/blob/main/models/llama3_3/LICENSE]
- Legal readings are engineering interpretations and not legal advice, and UK data-protection law after the 2025 reforms was not analysed. [assumption; source: https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32016R0679]

### Open Questions

- Which named regulated organisations have disclosed self-hosting for residency or sovereignty reasons?
- How do tuned small models compare with retrieval on regulated classification and extraction tasks in controlled studies?
- How do Apache 2.0 and other open-weight licences differ from the Llama licence in obligations on derivatives?

---

## Output

*(Fill in when completing — what was produced as a result of this research?)*

- Type: knowledge
- Description: Comparison of optionality and control across subscription, managed-platform, and self-hosted model stages, locating tuning on managed platforms and bounding self-hosting economics and regulatory drivers. [inference; source: https://docs.aws.amazon.com/bedrock/latest/userguide/custom-model-fine-tuning.html; https://arxiv.org/abs/2509.18101]
- Links: https://docs.aws.amazon.com/bedrock/latest/userguide/custom-model-fine-tuning.html; https://arxiv.org/abs/2509.18101; https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32022R2554
