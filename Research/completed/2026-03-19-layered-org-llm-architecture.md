---
review_count: 2
title: "Layered Organisation Large Language Model: Feasibility and Architecture of Organisation-Customised LLMs"
added: 2026-03-19
status: completed
priority: high  # low | medium | high
blocks: []
tags: [llm, rag, fine-tuning, enterprise-ai, knowledge-management, organisational-context, architecture, feasibility, concept-generation, customisation, layered-llm, retrieval-augmented-generation, parameter-efficient-fine-tuning]
started: 2026-03-22
completed: 2026-03-22
output: [knowledge]
---

# Layered Organisation Large Language Model: Feasibility and Architecture of Organisation-Customised LLMs

## Research Question

Is it technically feasible and economically viable for an organisation to build a customised Large Language Model (LLM) layer that injects and optimises over organisation-specific context - internal knowledge, regulatory domain, and competitive landscape - while operating in tandem with base foundation models? If so, what architectural patterns (layered, tandem, adversarial) best address this problem, who is already doing it, and does concept generation offer a viable path beyond Retrieval-Augmented Generation (RAG)?

Supporting questions:

This item treats enterprise Artificial Intelligence (AI) customisation as the core problem space, and Generative Pre-trained Transformer (GPT) models appear as named examples within that broader landscape.

- What is the gap between what base LLMs know (public internet) and what an organisation needs them to know (internal context + salient external context)?
- What are the current state-of-the-art approaches to organisation-specific LLM adaptation: RAG, fine-tuning, parameter-efficient fine-tuning (PEFT), Mixture of Experts (MoE), retrieval-augmented fine-tuning, and knowledge distillation?
- What is the feasibility - technology maturity, cost, time to value, and skill requirements - of each approach for a mid-to-large enterprise?
- What does a "layered" architecture look like in practice - an org-specific adapter or model layer sitting on top of or beside a base foundation model?
- What does a "tandem" or "adversarial" architecture look like - can two models (one general, one org-specific) collaborate or check each other?
- Who is already building organisation-customised LLM systems, and what architectural choices have they made?
- Does concept generation (generative synthesis of org-specific domain concepts from internal corpora) offer a viable path that RAG alone cannot deliver?
- What are the specific failure modes of RAG that motivate exploring customised or fine-tuned models for org context?

## Scope

**In scope:**
- Architectural patterns for organisation-specific LLM customisation: RAG, fine-tuning (full and PEFT), domain-adaptive pretraining, knowledge graph augmentation, mixture-of-experts routing, model merging / model soup, and layered/tandem/adversarial multi-model architectures
- Feasibility dimensions: technology readiness level, compute and data cost estimates, time-to-value for each approach, and skill/team requirements for a typical mid-to-large enterprise
- Organisations and vendors already doing this: Bloomberg GPT, MedPaLM, Harvey AI, Morgan Stanley OpenAI deployment, Glean, Notion AI, enterprise RAG platforms (Cohere, Vertex AI Search, Amazon Web Services (AWS) Bedrock Knowledge Bases)
- RAG failure modes and limitations that motivate going beyond RAG: knowledge boundary problems, retrieval precision ceilings, context window constraints, latency, and cost at scale
- Concept generation as an alternative or complement: generating a synthetic domain vocabulary, concept library, or training corpus from org-specific data
- Adversarial and tandem multi-model architectures: Constitutional AI, Mixture-of-Agents (MoA), debate-based reasoning, model routing
- Prior completed research in this repository directly adjacent to this item: `2026-03-15-context-compression-rag-enterprise-knowledge`, `2026-03-15-context-layers-aligned-decisions-synthesis`, `2026-03-02-agent-memory-management-context-injection`
- Prior backlog items: `2026-03-17-ai-memory-systems-rag-neuroscience`, `2026-03-18-api-context-hubs-rag-mcp`

**Out of scope:**
- Implementation of a specific customised LLM for a specific organisation (this is a research item)
- Benchmarking specific vector databases or embedding models (infrastructure detail, not architecture)
- Security and data governance of org-specific training data (a related but separate concern; surface as open question if encountered)
- Multi-modal organisation context (images, audio, video) unless it arises naturally from an architectural review
- General LLM evaluation benchmarks not tied to org-context customisation

**Constraints:** Publicly accessible sources. Vendor documentation, technical blog posts, arXiv preprints, and open-access papers (2022-2026). Web search at retrieval time for the most current vendor and research state, as the enterprise LLM customisation landscape is evolving rapidly.

## Context

Base foundation models are trained on the public internet. They encode broad world knowledge but have two structural gaps for organisational use:

1. **Internal context gap** - the model has no knowledge of the organisation's data, decisions, processes, history, or artefacts. RAG addresses this partially: retrieve relevant internal documents and inject them into the prompt. But RAG has a ceiling: it retrieves based on surface similarity, not organisational salience; it cannot internalise the conceptual vocabulary, domain ontology, or decision heuristics that an expert in the organisation holds.

2. **Salient external context gap** - even for public information, an organisation operates within a narrower context than "the whole internet": specific regulators, specific competitors, specific markets, specific jurisdictions. A base model treats all public knowledge as equally relevant; an org-specific model should weight the org's regulatory environment, competitive landscape, and domain knowledge above general knowledge.

The issue that seeds this item asks a pointed question: is it *possible and feasible* (technology, time, money, skill) to have a customised LLM that addresses both gaps and works with, not instead of, base models? Three architectural framings are proposed in the issue - **layered** (org model on top of base model), **tandem** (org model alongside base model), and **adversarial** (org model checking or critiquing base model output) - and asks whether concept generation offers a path.

This is not a purely theoretical question: BloombergGPT, Harvey AI, and Morgan Stanley's OpenAI deployment all represent public enterprise efforts to customise Large Language Model (LLM) systems for domain-specific work. The architectural choices they made, and the lessons learned, are part of the answer. (Sources: `https://arxiv.org/abs/2303.17564`; `https://www.harvey.ai/blog/expanding-harveys-model-offerings`; `https://www.zenml.io/llmops-database/enterprise-knowledge-management-with-llms-morgan-stanley-s-gpt-4-implementation`)

The prior research in this repository on context compression, context layers, and memory systems establishes that the context management problem is well understood at the prompt level. This item explores whether the problem requires going deeper - into the weights of the model itself.

## Approach

1. **Define the gap precisely** - articulate the internal context gap and salient external context gap in concrete terms. What does a model need to "know" that RAG cannot deliver? What does "org-salient external context" mean operationally (e.g., jurisdiction-specific regulation, named competitor filings, industry-specific terminology)? Use this to establish why org-customised LLMs are worth exploring beyond RAG.
2. **Map the adaptation landscape** - survey the full range of approaches from lightest to heaviest: prompt engineering and few-shot prompting -> RAG -> PEFT (Low-Rank Adaptation (LoRA), Quantized Low-Rank Adaptation (QLoRA), prefix tuning, adapters) -> full fine-tuning -> domain-adaptive pretraining -> model merging / model soup -> training a domain-specific model from scratch. For each: what does it require in data, compute, and skill? What org-context problems does it solve that lighter approaches cannot?
3. **Case study audit** - examine real enterprise deployments:
   - Bloomberg GPT - domain-adaptive pretraining on financial text
   - MedPaLM / Med-Gemini - medical domain adaptation
   - Harvey AI - legal domain LLM on top of GPT-4
   - Morgan Stanley + OpenAI - enterprise RAG at scale with fine-tuned retrieval
   - Glean - enterprise search and knowledge graph over internal data
   - Legal, financial, and healthcare sector examples where regulatory context is critical
   For each: what architectural approach was used, what was the stated rationale, and what are the reported outcomes or failure modes?
4. **Layered / tandem / adversarial architecture deep dive** - examine multi-model architectural patterns where one model specialises in org context while another provides general capability:
   - Layered: adapter layers, LoRA on top of frozen base, prompt/prefix injection
   - Tandem: routing (which model answers this query?), ensemble, Mixture-of-Agents (MoA)
   - Adversarial: Constitutional AI debate, model-as-critic, chain-of-verification (CoVe), self-consistency
   What is the latency, cost, and complexity overhead of each? When is each warranted?
5. **Concept generation assessment** - investigate whether generative synthesis of org-specific concepts from internal corpora is a viable path. Does training (or fine-tuning) on org data to generate a domain concept library or synthetic domain corpus create a richer representation than RAG alone? What research supports or challenges this? Is this closer to knowledge distillation, synthetic data generation, or ontology extraction?
6. **Feasibility matrix** - produce a structured feasibility assessment across the key adaptation approaches, covering: technology readiness (production-ready, early-adopter, research-only), cost range, data requirements (volume, quality, labelling), time-to-value estimate, and skill requirements (data science team, Machine Learning Operations (MLOps), domain experts).
7. **Synthesis** - produce Executive Summary, Key Findings, Evidence Map, and Feasibility Matrix.

## Sources

- [x] BloombergGPT paper - Wu, S. et al. (2023) - "BloombergGPT: A Large Language Model for Finance" - https://arxiv.org/abs/2303.17564
- [x] Med-PaLM paper - Singhal, K. et al. (2023) - "Large Language Models Encode Clinical Knowledge" - https://arxiv.org/abs/2212.13138
- [x] Harvey AI - "Expanding Harvey's Model Offerings" - https://www.harvey.ai/blog/expanding-harveys-model-offerings
- [x] Harvey AI Microsoft case study - https://www.microsoft.com/en/customers/story/19750-harvey-azure-open-ai-service
- [x] Morgan Stanley enterprise knowledge management case study summarising the OpenAI deployment - https://www.zenml.io/llmops-database/enterprise-knowledge-management-with-llms-morgan-stanley-s-gpt-4-implementation
- [x] LoRA paper - Hu, E. et al. (2021) - "LoRA: Low-Rank Adaptation of Large Language Models" - https://arxiv.org/abs/2106.09685
- [x] Quantized Low-Rank Adaptation (QLoRA) paper - Dettmers, T. et al. (2023) - "QLoRA: Efficient Finetuning of Quantized LLMs" - https://arxiv.org/abs/2305.14314
- [x] PEFT survey - Ding, N. et al. (2023) - "Parameter-efficient fine-tuning of large-scale pre-trained language models" - https://www.nature.com/articles/s42256-023-00626-4
- [x] Domain-adaptive pretraining - Gururangan, S. et al. (2020) - "Don't Stop Pretraining: Adapt Language Models to Domains and Tasks" - https://arxiv.org/abs/2004.10964
- [x] Mixture-of-Agents (MoA) - Wang, J. et al. (2024) - "Mixture-of-Agents Enhances Large Language Model Capabilities" - https://arxiv.org/abs/2406.04692
- [x] Chain-of-Verification (CoVe) - Dhuliawala, S. et al. (2023) - "Chain-of-Verification Reduces Hallucination in Large Language Models" - https://arxiv.org/abs/2309.11495
- [x] Constitutional AI - Bai, Y. et al. (2022) - "Constitutional AI: Harmlessness from AI Feedback" - https://arxiv.org/abs/2212.08073
- [x] RAG limitations survey - Barnett, S. et al. (2024) - "Seven Failure Points When Engineering a Retrieval-Augmented Generation System" - https://arxiv.org/abs/2401.05856
- [x] Glean knowledge graph guide - https://www.glean.com/resources/guides/glean-knowledge-graph
- [x] Glean + Google Cloud architecture blog - https://cloud.google.com/blog/products/data-analytics/glean-uses-bigquery-and-google-ai-to-enhance-enterprise-search
- [x] Cohere RAG documentation - https://docs.cohere.com/docs/retrieval-augmented-generation-rag
- [x] Vertex AI RAG Engine overview - https://cloud.google.com/vertex-ai/generative-ai/docs/rag-overview
- [x] AWS Bedrock Knowledge Bases overview - https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base.html
- [x] Synthetic domain corpus generation precedent - Gunasekar, S. et al. (2023) - "Textbooks Are All You Need" - https://arxiv.org/abs/2306.11644
- [x] Model merging / model soup - Wortsman, M. et al. (2022) - "Model Soups" - https://arxiv.org/abs/2203.05482
- [x] Concept extraction with LLMs - Norouzi, E. et al. (2025) - "ConExion: Concept Extraction with Large Language Models" - https://arxiv.org/abs/2504.12915
- [x] Prior completed research: `Research/completed/2026-03-15-context-compression-rag-enterprise-knowledge.md`
- [x] Prior completed research: `Research/completed/2026-03-15-context-layers-aligned-decisions-synthesis.md`
- [x] Prior completed research: `Research/completed/2026-03-02-agent-memory-management-context-injection.md`
- [x] Prior completed research: `Research/completed/2026-03-15-latent-concept-extraction-confluence.md`
- [x] Prior completed research: `Research/completed/2026-03-18-api-context-hubs-rag-mcp.md`

---

## Research Skill Output

*(Full output from running the research skill - retained verbatim in the completed item. Sections 0-5 are the investigation; Section 6 seeds the Findings section below.)*

### §0 Initialise

- **[fact]** The research question is whether an organisation can economically justify an organisation-customised Large Language Model (LLM) layer that sits above or beside a general foundation model, and which combination of Retrieval-Augmented Generation (RAG), parameter-efficient fine-tuning (PEFT), domain-adaptive pretraining, routing, and verification makes that viable. Source: this item's Research Question.
- **[fact]** In scope are architecture patterns, enterprise case studies, RAG limits, concept generation, and a feasibility matrix; out of scope are detailed infrastructure selection, security programme design, and implementing a specific enterprise system. Source: this item's Scope.
- **[fact]** The investigation is constrained to public sources, with emphasis on open papers, vendor documentation, and completed repository research that already covered context architecture and agent memory. Source: this item's Constraints.
- **[assumption]** The missing `.github/skills/research/SKILL.md` file means the fallback process in `research-prompt.md` is the operative research skill for this run. **Justification:** the repository currently lacks the named skill file, and `research-prompt.md` explicitly defines the same sectioned workflow. Source: `research-prompt.md`.
- **[fact]** Prior completed repository work already established three adjacent conclusions that matter here: RAG is retrieval rather than a full memory architecture; layered organisational context is necessary for aligned decisions; and context quality, not raw token volume, dominates agent performance. Sources: `Research/completed/2026-03-02-agent-memory-management-context-injection.md`; `Research/completed/2026-03-15-context-layers-aligned-decisions-synthesis.md`; `Research/completed/2026-03-15-context-compression-rag-enterprise-knowledge.md`.

### §1 Question Decomposition

- **Branch A - Gap definition**
  - A1. What exactly is missing when a base foundation model faces private organisational knowledge?
  - A2. What additional gap exists for organisation-salient public knowledge such as specific regulators, competitors, and jurisdictions?
  - A3. Which parts of that gap can RAG solve, and which parts remain unsolved?
- **Branch B - Adaptation landscape**
  - B1. What do LoRA, QLoRA, and broader PEFT methods change economically versus full fine-tuning?
  - B2. When does domain-adaptive pretraining become justified?
  - B3. What is the status of model merging and other heavier adaptation methods?
- **Branch C - Real deployments**
  - C1. What architecture did BloombergGPT use, and what did it gain?
  - C2. What architecture did Med-PaLM use, and what limits remained?
  - C3. How do Harvey, Morgan Stanley, and Glean currently combine retrieval, adaptation, and orchestration?
- **Branch D - Layered, tandem, and adversarial patterns**
  - D1. What does a layered architecture mean operationally?
  - D2. When do tandem or routing architectures improve outcomes?
  - D3. When do critic or verifier models add value?
- **Branch E - Concept generation**
  - E1. Is concept extraction or synthetic corpus generation a credible complement to RAG?
  - E2. Is concept generation better understood as ontology extraction, synthetic supervision, or full replacement for retrieval?
- **Branch F - Feasibility synthesis**
  - F.1 Which approaches are production-ready, early-adopter, or still research-only for a mid-to-large enterprise?
  - F.2 What skill, data, and evaluation stack is required for each?

### §2 Investigation

#### Source marking and evidence weighting

- **[fact]** Primary sources used here are academic papers and official vendor documentation: BloombergGPT, Med-PaLM, LoRA, QLoRA, PEFT survey, domain-adaptive pretraining, Mixture-of-Agents (MoA), chain-of-verification (CoVe), Constitutional AI, Barnett's RAG failure paper, and official documentation from Harvey, Microsoft, Glean, Cohere, Google Cloud, Vertex AI, and AWS Bedrock. Sources: URLs in the Sources section above.
- **[fact]** Secondary sources used here are repository-completed research items and the ZenML summary of Morgan Stanley's GPT-4 deployment, because Morgan Stanley's official OpenAI case study was not directly fetchable from this environment. Sources: `Research/completed/2026-03-02-agent-memory-management-context-injection.md`; `Research/completed/2026-03-15-context-compression-rag-enterprise-knowledge.md`; `https://www.zenml.io/llmops-database/enterprise-knowledge-management-with-llms-morgan-stanley-s-gpt-4-implementation`.

#### A. The gap between base models and organisational use

- **[fact]** Vertex AI RAG Engine documentation states that large language models do not understand private knowledge - specifically an organisation's own data - and that context augmentation is needed to reduce hallucination and improve answer quality. Source: `https://cloud.google.com/vertex-ai/generative-ai/docs/rag-overview`
- **[fact]** AWS Bedrock Knowledge Bases documentation makes the same distinction: foundation models have general knowledge, but proprietary information must be retrieved from enterprise data sources and injected into the response workflow. Source: `https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base.html`
- **[fact]** Cohere's RAG documentation shows the same baseline pattern operationally: retrieve documents, ground the answer on those documents, and emit inline citations tied to those documents. Source: `https://docs.cohere.com/docs/retrieval-augmented-generation-rag`
- **[inference]** The first gap is therefore not controversial: enterprise systems already assume that base models lack private organisational context and must be supplemented at inference time with external knowledge.
- **[fact]** Barnett et al. identify seven failure points in RAG systems and conclude that validation is only feasible during operation and that robustness evolves rather than being fully designed in at the start. Source: `https://arxiv.org/abs/2401.05856`
- **[inference]** RAG solves document access and freshness better than weight updates, but it does not fully solve salience, ontology internalisation, or the problem of repeatedly re-explaining the same domain vocabulary and decision heuristics on every query.
- **[fact]** Prior repository work concluded that RAG is a retrieval mechanism, not a memory architecture, and that governance and layered context remain unsolved if retrieval is treated as the whole answer. Source: `Research/completed/2026-03-02-agent-memory-management-context-injection.md`

#### B. What the adaptation landscape changes

- **[fact]** LoRA freezes pretrained weights and injects trainable low-rank matrices, reducing trainable parameters by up to 10,000 times and cutting graphics processing unit (GPU) memory requirements by 3 times relative to full fine-tuning in the GPT-3 example, without adding inference latency. Source: `https://arxiv.org/abs/2106.09685`
- **[fact]** QLoRA shows that a 65-billion-parameter model can be fine-tuned on a single 48 GB GPU by backpropagating through a frozen 4-bit-quantised base model into LoRA adapters, while preserving full fine-tuning task performance. Source: `https://arxiv.org/abs/2305.14314`
- **[fact]** The Nature Machine Intelligence PEFT survey argues that full parameter fine-tuning becomes impractical for large pretrained language models because of deployment and storage cost, and presents PEFT or delta-tuning as the practical adaptation branch for large models. Source: `https://www.nature.com/articles/s42256-023-00626-4`
- **[fact]** The same survey reports that only about 0.5-4% of sampled recent natural-language-processing papers practically adopted large pretrained language models in experiments, which is direct evidence that model scale creates a real adoption barrier. Source: `https://www.nature.com/articles/s42256-023-00626-4`
- **[fact]** Gururangan et al. show that domain-adaptive pretraining delivers performance gains across biomedical, computer-science, news, and review domains, and that task-adaptive pretraining can improve further even after domain adaptation. Source: `https://arxiv.org/abs/2004.10964`
- **[fact]** Model soups improve accuracy and robustness by averaging weights of multiple fine-tuned models without increasing inference or memory cost, but the evidence base is benchmark-oriented rather than enterprise-deployment-oriented. Source: `https://arxiv.org/abs/2203.05482`
- **[inference]** The economic break is therefore clear: PEFT makes enterprise-specific weight adaptation feasible for teams that could not justify full fine-tuning, while domain-adaptive pretraining remains materially heavier and is best reserved for large, stable, high-value domains rather than typical single-enterprise deployments.

#### C. Enterprise and sector deployments already in market

- **[fact]** BloombergGPT is a 50-billion-parameter model trained on 363 billion tokens of financial data plus 345 billion tokens of general-purpose data, and the paper reports that the mixed dataset improves finance tasks without sacrificing general-language-benchmark performance. Source: `https://arxiv.org/abs/2303.17564`
- **[fact]** Med-PaLM uses instruction prompt tuning to align a base medical model to new-domain evaluation tasks, improves medical reasoning over earlier baselines, but the paper explicitly states that the resulting model remains inferior to clinicians and still exhibits important limitations. Source: `https://arxiv.org/abs/2212.13138`
- **[fact]** Harvey states that it is incorporating Anthropic and Google foundation models into its legal platform, auto-routing users to the best model systems for legal work and focusing optimisation on task execution, firm knowledge, and user collaboration rather than baseline reasoning alone. Source: `https://www.harvey.ai/blog/expanding-harveys-model-offerings`
- **[fact]** Harvey's Microsoft case study states that the platform runs on Azure AI infrastructure using multiple models and supports legal tasks such as due diligence, document comparison, and case-law referencing across hundreds of law firms and legal teams. Source: `https://www.microsoft.com/en/customers/story/19750-harvey-azure-open-ai-service`
- **[fact]** The Morgan Stanley GPT-4 case study summary describes an internal assistant over a corpus that grew from about 7,000 questions to 100,000 documents, describes the system as retrieval-augmented, and reports a daily regression suite plus human review for generated summaries and debrief outputs. Source: `https://www.zenml.io/llmops-database/enterprise-knowledge-management-with-llms-morgan-stanley-s-gpt-4-implementation`
- **[fact]** Glean's knowledge graph guide describes a system with 100-plus connectors that builds a customer-specific knowledge graph weighing content, people, and activity signals to power hybrid search and generative Artificial Intelligence (AI). Source: `https://www.glean.com/resources/guides/glean-knowledge-graph`
- **[fact]** Google Cloud's architecture write-up on Glean states that Glean uses enterprise-corpus-derived training data for domain-adaptive pretraining and task-specific fine-tuning on large-scale models, while also using vector search, embeddings, and relevance signals for retrieval. Source: `https://cloud.google.com/blog/products/data-analytics/glean-uses-bigquery-and-google-ai-to-enhance-enterprise-search`
- **[inference]** The strongest real-world pattern is therefore hybrid rather than singular: Morgan Stanley represents retrieval-first customisation; Harvey represents multi-model routing plus domain-specific optimisation; Glean represents knowledge graph plus retrieval plus domain-adapted models; BloombergGPT and Med-PaLM represent sector-scale weight adaptation where the corpus and economic stakes justify it.

#### D. Layered, tandem, and adversarial patterns

- **[fact]** Mixture-of-Agents proposes a layered architecture in which each layer contains multiple agents and each downstream agent consumes the upstream outputs as auxiliary information, improving benchmark performance relative to single-model baselines. Source: `https://arxiv.org/abs/2406.04692`
- **[fact]** Chain-of-Verification reduces hallucination by using a four-stage workflow: draft, generate verification questions, answer those questions independently, and then produce a revised verified response. Source: `https://arxiv.org/abs/2309.11495`
- **[fact]** Constitutional AI trains a model to critique and revise its own outputs against a list of principles and then uses preference optimisation without requiring human harm labels for every case. Source: `https://arxiv.org/abs/2212.08073`
- **[inference]** Layered enterprise architecture maps cleanly onto these patterns: the foundation model handles broad generation, an organisation-specific layer handles local corpus or domain reasoning, and a verifier or policy layer checks output quality, safety, or compliance before the answer is trusted.
- **[inference]** Tandem and adversarial patterns are technically feasible today, but they are best justified as reliability and routing overlays around a retrieval-plus-adaptation core rather than as a full substitute for that core, because none of these verifier patterns solves private-knowledge ingestion by itself.

#### E. Concept generation beyond prompt-time retrieval

- **[fact]** The phi-1 paper shows that a small code model can achieve strong downstream performance using a mixture of textbook-quality web data and synthetically generated textbooks and exercises, which is a direct precedent for synthetic domain corpus generation as an adaptation path. Source: `https://arxiv.org/abs/2306.11644`
- **[fact]** ConExion shows that pretrained large language models can extract domain concepts beyond keyphrases and improve F1 score (F1) against prior techniques, specifically for concept extraction intended to support ontology learning and domain coverage evaluation. Source: `https://arxiv.org/abs/2504.12915`
- **[fact]** Prior repository research on latent concept extraction concluded that the convergent architecture for organisational corpora is dense embeddings plus a knowledge graph plus graph-traversal reasoning rather than dense retrieval alone. Source: `Research/completed/2026-03-15-latent-concept-extraction-confluence.md`
- **[inference]** Concept generation is therefore viable, but mainly in three forms: extracting a domain ontology or concept library, generating synthetic task data for fine-tuning, or distilling domain vocabulary into rankers and adapters. The evidence does not support treating concept generation as a direct replacement for retrieval when fresh source-grounded answers are required.

#### F. Feasibility matrix

- **[inference]** The evidence supports the following feasibility matrix for a mid-to-large enterprise:

| Approach | Readiness | Relative cost | Data requirement | Time-to-value | Best fit | Main limit |
|---|---|---|---|---|---|---|
| Prompting plus RAG | production-ready | low to moderate | existing docs and metadata | weeks | broad private knowledge access | retrieval ceiling and latency |
| RAG plus knowledge graph / better rankers | production-ready | moderate | connected systems plus relevance signals | weeks to months | cross-system enterprise search | index complexity and evaluation burden |
| PEFT with LoRA / QLoRA | production-ready to early-adopter | moderate | curated exemplars, evaluation set, stable task distribution | 1-3 months | repeated domain tasks, terminology internalisation | still needs MLOps and evaluation discipline |
| Full fine-tuning | early-adopter | high | larger curated dataset and deployment budget | several months | narrow, repeated workloads at high scale | model management and storage cost |
| Domain-adaptive pretraining | early-adopter for very large domains | high to very high | massive stable corpus | several months to a year | finance, medicine, legal research, enterprise platforms | heavy data, compute, and talent demand |
| Training from scratch | uncommon outside frontier or sector-scale actors | very high | enormous corpus and compute | long horizon | vendor or sector-scale foundation efforts | uneconomic for most single enterprises |
| Tandem / critic layers | production-ready as overlay | moderate | evaluation prompts, policies, routing logic | weeks to months | compliance-sensitive or high-risk answers | added latency and orchestration complexity |

- **[inference]** This matrix makes the central economic point explicit: the viable enterprise path is not a monolithic organisation-trained model, but a layered system that uses retrieval for freshness, lightweight adaptation for internalised vocabulary or repeated tasks, and verifier layers where mistakes are expensive.

### §3 Reasoning

- **[inference]** I weigh vendor RAG documentation, the RAG failure paper, and the enterprise case studies together rather than separately because the key question is not whether RAG works at all, but where its performance ceiling appears in practice.
- **[inference]** The deployment evidence is strongest for retrieval-first systems because AWS Bedrock, Vertex AI RAG Engine, Cohere, Morgan Stanley, and Glean all treat private knowledge retrieval as the default enterprise starting point.
- **[inference]** I treat BloombergGPT and Med-PaLM as proof that weight-level domain adaptation can work, but not as proof that a typical single enterprise should build its own domain model, because both examples sit closer to sector-scale corpus economics than to ordinary enterprise budgets.
- **[inference]** Harvey and Glean are more informative for the organisational-customisation question because both show that the market frontier is hybrid: multiple base models, retrieval, routing, and domain optimisation coexist in one stack.
- **[inference]** The most defensible interpretation of concept generation is as an enrichment layer that changes what the system can retrieve, rank, or learn from, not as a clean alternative to source-grounded retrieval.

### §4 Consistency Check

- **[fact]** There is an apparent tension between vendor documentation that presents RAG as a practical grounding solution and Barnett et al.'s paper that documents seven failure points in RAG systems. Sources: `https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base.html`; `https://cloud.google.com/vertex-ai/generative-ai/docs/rag-overview`; `https://arxiv.org/abs/2401.05856`
- **[inference]** The tension is resolved by scope: vendor docs show that RAG is the easiest way to connect private data today, while Barnett et al. show that once RAG is deployed, retrieval, evaluation, and robustness remain live engineering problems.
- **[fact]** There is also an apparent tension between describing Glean as a retrieval-and-knowledge-graph system and describing it as a domain-adapted and task-fine-tuned model stack. Sources: `https://www.glean.com/resources/guides/glean-knowledge-graph`; `https://cloud.google.com/blog/products/data-analytics/glean-uses-bigquery-and-google-ai-to-enhance-enterprise-search`
- **[inference]** That second tension is resolved by recognising that hybrid enterprise systems already combine retrieval with adapted embeddings and fine-tuned submodels; the apparent contradiction is actually evidence for the layered answer.
- **[fact]** Med-PaLM improves domain performance but remains inferior to clinicians, while BloombergGPT improves finance tasks without giving up general performance. Sources: `https://arxiv.org/abs/2212.13138`; `https://arxiv.org/abs/2303.17564`
- **[inference]** These outcomes are consistent with the broader conclusion that model adaptation helps but does not remove the need for retrieval, evaluation, and human or procedural oversight in high-stakes domains.

### §5 Depth and Breadth Expansion

**Technical lens**

- **[inference]** The technical frontier is not choosing between retrieval and model customisation, but deciding which knowledge should stay external and fresh versus which repeated patterns should be internalised into adapters, rankers, or domain-tuned models.

**Economic lens**

- **[fact]** PEFT and QLoRA materially reduce the memory and deployment barrier relative to full fine-tuning, while domain-adaptive pretraining still assumes a large corpus and substantial compute. Sources: `https://arxiv.org/abs/2106.09685`; `https://arxiv.org/abs/2305.14314`; `https://arxiv.org/abs/2004.10964`
- **[inference]** Economically, that means most enterprises should spend first on retrieval quality, evaluation infrastructure, and narrow PEFT experiments before considering heavier training regimes.

**Regulatory lens**

- **[fact]** The strongest public case studies all come from regulated or knowledge-dense sectors such as finance, medicine, and legal services. Sources: `https://arxiv.org/abs/2303.17564`; `https://arxiv.org/abs/2212.13138`; `https://www.microsoft.com/en/customers/story/19750-harvey-azure-open-ai-service`; `https://www.zenml.io/llmops-database/enterprise-knowledge-management-with-llms-morgan-stanley-s-gpt-4-implementation`
- **[inference]** These sectors favour layered architectures because retrieval preserves provenance and freshness, while verification overlays and human review preserve auditability.

**Behavioural and organisational lens**

- **[inference]** Organisation-customised intelligence is not only a model problem; it is an expert-knowledge capture problem. Subject-matter experts still have to define evaluation sets, mark authoritative sources, and decide which heuristics deserve to be baked into the system rather than retrieved ad hoc.

**Historical lens**

- **[inference]** The field is moving along a familiar sequence: search over enterprise content, then RAG over enterprise content, then hybrid systems that selectively internalise repeated domain structure while keeping fresh evidence external.

### §6 Synthesis

**Executive summary:**

- **[inference]** A mid-to-large enterprise can build a useful organisation-customised Large Language Model (LLM) layer today, but the economically viable design is a layered system built on top of a base foundation model with Retrieval-Augmented Generation (RAG), selective parameter-efficient adaptation, and optional verifier layers rather than a standalone organisation-trained model.
- **[inference]** Public case materials point to the same design direction across different industries: a retrieval-first assistant in Morgan Stanley's published case summary, a layered multi-model legal stack at Harvey, and a knowledge-graph-plus-search stack at Glean all extend base models instead of replacing them wholesale. Sources: `https://www.zenml.io/llmops-database/enterprise-knowledge-management-with-llms-morgan-stanley-s-gpt-4-implementation`; `https://www.harvey.ai/blog/expanding-harveys-model-offerings`; `https://cloud.google.com/blog/products/data-analytics/glean-uses-bigquery-and-google-ai-to-enhance-enterprise-search`; `https://www.glean.com/resources/guides/glean-knowledge-graph`
- **[inference]** The main reason to go beyond pure RAG is not that retrieval has failed completely, but that repeated domain vocabulary, concept structure, routing logic, and verification requirements create a performance ceiling that retrieval alone does not remove.
- **[inference]** Concept generation is best treated as an enrichment technique for ontology extraction, synthetic supervision, or concept distillation, not as a substitute for source-grounded retrieval at answer time. Sources: `https://arxiv.org/abs/2306.11644`; `https://arxiv.org/abs/2504.12915`

**Key findings:**

1. **[fact]** Production enterprise customisation still starts with retrieval because all major current platform docs and the Morgan Stanley deployment treat proprietary context injection as the default answer to the private-knowledge gap rather than immediate weight-level retraining. Sources: `https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base.html`; `https://cloud.google.com/vertex-ai/generative-ai/docs/rag-overview`; `https://docs.cohere.com/docs/retrieval-augmented-generation-rag`; `https://www.zenml.io/llmops-database/enterprise-knowledge-management-with-llms-morgan-stanley-s-gpt-4-implementation`
2. **[fact]** Parameter-efficient fine-tuning makes organisation-specific weight adaptation technically feasible for enterprises that could not justify full fine-tuning, because LoRA and QLoRA dramatically reduce trainable-parameter and memory requirements while preserving strong downstream task performance. Sources: `https://arxiv.org/abs/2106.09685`; `https://arxiv.org/abs/2305.14314`; `https://www.nature.com/articles/s42256-023-00626-4`
3. **[inference]** Domain-adaptive pretraining is viable when the corpus is very large and stable, but the strongest public examples sit at sector scale or vendor-platform scale rather than at the scale of a typical single enterprise. Sources: `https://arxiv.org/abs/2303.17564`; `https://arxiv.org/abs/2212.13138`; `https://arxiv.org/abs/2004.10964`; `https://cloud.google.com/blog/products/data-analytics/glean-uses-bigquery-and-google-ai-to-enhance-enterprise-search`
4. **[fact]** Real enterprise leaders already use layered or tandem architectures instead of a single custom model, with Harvey routing across multiple foundation models and Glean combining retrieval, a knowledge graph, and adapted models inside one product stack. Sources: `https://www.harvey.ai/blog/expanding-harveys-model-offerings`; `https://www.microsoft.com/en/customers/story/19750-harvey-azure-open-ai-service`; `https://www.glean.com/resources/guides/glean-knowledge-graph`; `https://cloud.google.com/blog/products/data-analytics/glean-uses-bigquery-and-google-ai-to-enhance-enterprise-search`
5. **[fact]** RAG has structural failure modes - including retrieval mismatch, robustness drift, and validation burdens during operation - which is why a retrieval-only answer has a ceiling even though RAG remains the fastest path to value. Source: `https://arxiv.org/abs/2401.05856`
6. **[inference]** Tandem and adversarial patterns are already technically available as control layers, because Mixture-of-Agents, chain-of-verification, and Constitutional AI show that routing, critique, and self-checking can be layered around a base answerer to improve reliability. Sources: `https://arxiv.org/abs/2406.04692`; `https://arxiv.org/abs/2309.11495`; `https://arxiv.org/abs/2212.08073`
7. **[inference]** Concept generation offers value when it creates reusable structure - ontology terms, synthetic exemplars, or distilled concept libraries - that can improve ranking, supervision, or adapters, but the available evidence does not support replacing fresh evidence retrieval with generated concepts alone. Sources: `https://arxiv.org/abs/2306.11644`; `https://arxiv.org/abs/2504.12915`
8. **[inference]** The practical escalation rule is to improve retrieval and relevance first, add adapters when repeated high-value tasks justify internalisation, and reserve full domain pretraining or new-model training for unusually large, stable, and well-funded domains rather than ordinary enterprise deployments. Sources: `https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base.html`; `https://cloud.google.com/vertex-ai/generative-ai/docs/rag-overview`; `https://arxiv.org/abs/2106.09685`; `https://arxiv.org/abs/2305.14314`; `https://arxiv.org/abs/2303.17564`; `https://arxiv.org/abs/2212.13138`

**Evidence map:**

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [fact] Retrieval is the default production answer to private organisational knowledge | `https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base.html`; `https://cloud.google.com/vertex-ai/generative-ai/docs/rag-overview`; `https://docs.cohere.com/docs/retrieval-augmented-generation-rag`; `https://www.zenml.io/llmops-database/enterprise-knowledge-management-with-llms-morgan-stanley-s-gpt-4-implementation` | high | Independent vendor docs and a deployment case agree |
| [fact] LoRA and QLoRA materially lower adaptation cost | `https://arxiv.org/abs/2106.09685`; `https://arxiv.org/abs/2305.14314`; `https://www.nature.com/articles/s42256-023-00626-4` | high | Primary papers and survey agree |
| [inference] Domain-adaptive pretraining is better suited to sector-scale or platform-scale corpora than ordinary single-enterprise use | `https://arxiv.org/abs/2303.17564`; `https://arxiv.org/abs/2212.13138`; `https://arxiv.org/abs/2004.10964`; `https://cloud.google.com/blog/products/data-analytics/glean-uses-bigquery-and-google-ai-to-enhance-enterprise-search` | medium | Strong evidence of effectiveness, medium evidence of economic boundary |
| [fact] Harvey and Glean already implement layered or tandem enterprise stacks | `https://www.harvey.ai/blog/expanding-harveys-model-offerings`; `https://www.microsoft.com/en/customers/story/19750-harvey-azure-open-ai-service`; `https://www.glean.com/resources/guides/glean-knowledge-graph`; `https://cloud.google.com/blog/products/data-analytics/glean-uses-bigquery-and-google-ai-to-enhance-enterprise-search` | high | Official vendor materials are explicit |
| [fact] RAG has recurring engineering failure points even when it improves grounding | `https://arxiv.org/abs/2401.05856` | high | Primary survey and experience report |
| [fact] Verifier and critic patterns can be layered around base generation | `https://arxiv.org/abs/2406.04692`; `https://arxiv.org/abs/2309.11495`; `https://arxiv.org/abs/2212.08073` | high | Academic papers establish technical feasibility |
| [inference] Concept generation is most useful as enrichment, not as full retrieval replacement | `https://arxiv.org/abs/2306.11644`; `https://arxiv.org/abs/2504.12915` | medium | Direct evidence supports ontology and synthetic-supervision uses, but not full replacement |
| [inference] Enterprises should escalate from retrieval improvements to adapters before considering heavy pretraining or new-model training | `https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base.html`; `https://cloud.google.com/vertex-ai/generative-ai/docs/rag-overview`; `https://arxiv.org/abs/2106.09685`; `https://arxiv.org/abs/2305.14314`; `https://arxiv.org/abs/2303.17564`; `https://arxiv.org/abs/2212.13138` | high | The evidence converges on staged escalation rather than immediate deep custom training |

**Assumptions:**

- **[assumption]** The ZenML Morgan Stanley write-up is a fair secondary summary of the underlying OpenAI case study. **Justification:** it provides concrete implementation details and evaluation practices consistent with other public references to the deployment, but the official OpenAI page was not directly fetchable from this environment.
- **[assumption]** Glean's public Google Cloud architecture post is representative of the architecture direction of its enterprise product rather than a one-off cloud-marketing example. **Justification:** it is co-authored with Glean leadership and matches Glean's own knowledge graph materials.
- **[assumption]** Mid-to-large enterprise here means an organisation that can already sustain modern data-platform, retrieval, and evaluation work, but not frontier-foundation-model training budgets. **Justification:** the prompt asks for enterprise feasibility rather than laboratory or hyperscaler feasibility.

**Analysis:**

- **[inference]** The decisive trade-off is freshness versus internalisation. Retrieval keeps answers tied to current documents and citations, while weight adaptation internalises repeated vocabulary, style, and decision patterns that would otherwise have to be re-explained on every request.
- **[inference]** The case studies suggest a practical ordering: start with retrieval because private knowledge changes quickly, add graph or relevance signals when retrieval quality plateaus, add PEFT when repeated high-value tasks justify internalisation, and add verifier layers where mistakes are materially costly.
- **[inference]** BloombergGPT and Med-PaLM show that going deeper into weights works when the domain is rich enough and the corpus is large enough, but Harvey, Morgan Stanley, and Glean show that most enterprise value arrives sooner from hybrid orchestration than from building a wholly new model.
- **[inference]** Feasibility is therefore more organisational than mathematical: enterprises need authoritative corpora, evaluation sets, routing logic, and subject-matter ownership at least as much as they need graphics processing unit (GPU) budget.

**Risks, gaps, uncertainties:**

- **[fact]** The most direct official Morgan Stanley and OpenAI case-study page was not directly fetchable from this environment, so Morgan Stanley-specific details rely on a secondary summary rather than the original page. Source: failed fetch of `https://openai.com/index/morgan-stanley/`
- **[inference]** Public vendor material may understate operational failures, so the architectural conclusions should weight the RAG failure literature more heavily than product marketing on claims of completeness. Sources: `https://arxiv.org/abs/2401.05856`; `https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base.html`; `https://cloud.google.com/vertex-ai/generative-ai/docs/rag-overview`
- **[inference]** The consulted public literature does not provide a clean cost curve for when parameter-efficient fine-tuning (PEFT) overtakes retrieval economics for a given enterprise corpus and query volume, so the economic crossover point remains uncertain. Sources: `https://www.nature.com/articles/s42256-023-00626-4`; `https://arxiv.org/abs/2106.09685`; `https://arxiv.org/abs/2305.14314`
- **[inference]** Concept generation remains under-evidenced at enterprise deployment scale relative to retrieval and PEFT, even though the component techniques are promising. Sources: `https://arxiv.org/abs/2306.11644`; `https://arxiv.org/abs/2504.12915`
- **[assumption]** The security and governance implications of training on private enterprise data remain a separate blocker for some architectures. **Justification:** the enterprise platform materials emphasise controlled access, connected data sources, and governance for retrieval systems, while this item did not investigate legal, policy, or privacy controls for weight-level training. Sources: `https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base.html`; `https://cloud.google.com/vertex-ai/generative-ai/docs/rag-overview`

**Open questions:**

- **[inference]** What measurable threshold tells an enterprise that retrieval quality has plateaued enough to justify adapter training rather than another round of retrieval engineering?
- **[inference]** Which parts of organisational knowledge should remain permanently external for provenance reasons even if they could be internalised technically?
- **[inference]** Can synthetic domain corpora be made auditable enough for regulated industries to trust them as part of a production adaptation pipeline?
- **[inference]** What evaluation harness best measures a layered enterprise stack that combines retrieval, adapters, routing, and critic models rather than evaluating those pieces in isolation?

### §7 Recursive Review

- **[fact]** Coverage check: the investigation addressed the private-knowledge gap, the adaptation landscape, the named case studies, layered and verifier architectures, concept generation, and the required feasibility matrix.
- **[fact]** Source check: every factual claim in the investigation maps to a cited academic paper, vendor document, or explicitly identified repository-completed item, with the Morgan Stanley case clearly marked as secondary evidence.
- **[fact]** Claim-labelling check: the investigation, reasoning, consistency check, depth expansion, and synthesis sections explicitly label claims as `[fact]`, `[inference]`, or `[assumption]`.
- **[fact]** Findings check: every claim in `## Findings` below is carried over from the synthesis above and does not introduce a new factual assertion.
- **[inference]** Final judgement: the evidence supports a layered-hybrid conclusion much more strongly than either a retrieval-only conclusion or a train-your-own-model conclusion.

**Acronym expansion audit (mandatory inline):**

| Abbreviation | First use location | Expanded? |
|---|---|---|
| LLM | Research Question | Large Language Model (LLM) - yes |
| RAG | Research Question | Retrieval-Augmented Generation (RAG) - yes |
| PEFT | Research Question | parameter-efficient fine-tuning (PEFT) - yes |
| MoE | Research Question | Mixture of Experts (MoE) - yes |
| LoRA | Approach 2 | Low-Rank Adaptation (LoRA) - yes |
| CoVe | Approach 4 | chain-of-verification (CoVe) - yes |
| AI | Supporting questions preface | Artificial Intelligence (AI) - yes |
| GPT | Supporting questions preface | Generative Pre-trained Transformer (GPT) - yes |
| QLoRA | Approach 2 | Quantized Low-Rank Adaptation (QLoRA) - yes |
| AWS | Scope | Amazon Web Services (AWS) - yes |
| MLOps | Approach 6 | Machine Learning Operations (MLOps) - yes |
| GPU | Investigation B | graphics processing unit (GPU) - yes |
| API | not used in body as standalone abbreviation | not applicable |
| CLI | not used | not applicable |
| SDK | not used | not applicable |
| PAT | not used | not applicable |
| MCP | not used | not applicable |
| PR | not used | not applicable |

---

## Findings

### Executive Summary

[inference] A mid-to-large enterprise can build a useful organisation-customised Large Language Model (LLM) layer today, but the economically viable design is a layered system built on top of a base foundation model with Retrieval-Augmented Generation (RAG), selective parameter-efficient adaptation, and optional verifier layers rather than a standalone organisation-trained model. (Sources: `https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base.html`; `https://cloud.google.com/vertex-ai/generative-ai/docs/rag-overview`; `https://arxiv.org/abs/2106.09685`; `https://arxiv.org/abs/2305.14314`)

[inference] The public cases show that enterprises are customising the surrounding system stack - retrieval, routing, and knowledge structures - more often than they are building wholly new standalone models. (Sources: `https://www.zenml.io/llmops-database/enterprise-knowledge-management-with-llms-morgan-stanley-s-gpt-4-implementation`; `https://www.harvey.ai/blog/expanding-harveys-model-offerings`; `https://cloud.google.com/blog/products/data-analytics/glean-uses-bigquery-and-google-ai-to-enhance-enterprise-search`; `https://www.glean.com/resources/guides/glean-knowledge-graph`)

[inference] The main reason to go beyond pure RAG is not that retrieval has failed completely, but that repeated domain vocabulary, concept structure, routing logic, and verification requirements create a performance ceiling that retrieval alone does not remove. (Sources: `https://arxiv.org/abs/2401.05856`; `https://arxiv.org/abs/2106.09685`; `https://arxiv.org/abs/2305.14314`)

[inference] This makes concept generation a supporting technique for representation and supervision, while live answer quality still depends on access to current source material. (Sources: `https://arxiv.org/abs/2306.11644`; `https://arxiv.org/abs/2504.12915`)

### Key Findings

1. [fact] Production enterprise customisation still starts with retrieval because all major current platform docs and the Morgan Stanley deployment treat proprietary context injection as the default answer to the private-knowledge gap rather than immediate weight-level retraining. (Sources: `https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base.html`; `https://cloud.google.com/vertex-ai/generative-ai/docs/rag-overview`; `https://docs.cohere.com/docs/retrieval-augmented-generation-rag`; `https://www.zenml.io/llmops-database/enterprise-knowledge-management-with-llms-morgan-stanley-s-gpt-4-implementation`) [confidence: high]
2. [fact] Parameter-efficient fine-tuning makes organisation-specific weight adaptation technically feasible for enterprises that could not justify full fine-tuning, because LoRA and QLoRA dramatically reduce trainable-parameter and memory requirements while preserving strong downstream task performance. (Sources: `https://arxiv.org/abs/2106.09685`; `https://arxiv.org/abs/2305.14314`; `https://www.nature.com/articles/s42256-023-00626-4`) [confidence: high]
3. [inference] Domain-adaptive pretraining is viable when the corpus is very large and stable, but the strongest public examples sit at sector scale or vendor-platform scale rather than at the scale of a typical single enterprise. (Sources: `https://arxiv.org/abs/2303.17564`; `https://arxiv.org/abs/2212.13138`; `https://arxiv.org/abs/2004.10964`; `https://cloud.google.com/blog/products/data-analytics/glean-uses-bigquery-and-google-ai-to-enhance-enterprise-search`) [confidence: medium]
4. [fact] Real enterprise leaders already use layered or tandem architectures instead of a single custom model, with Harvey routing across multiple foundation models and Glean combining retrieval, a knowledge graph, and adapted models inside one product stack. (Sources: `https://www.harvey.ai/blog/expanding-harveys-model-offerings`; `https://www.microsoft.com/en/customers/story/19750-harvey-azure-open-ai-service`; `https://www.glean.com/resources/guides/glean-knowledge-graph`; `https://cloud.google.com/blog/products/data-analytics/glean-uses-bigquery-and-google-ai-to-enhance-enterprise-search`) [confidence: high]
5. [fact] Retrieval-Augmented Generation has structural failure modes - including retrieval mismatch, robustness drift, and validation burdens during operation - which is why a retrieval-only answer has a ceiling even though Retrieval-Augmented Generation remains the fastest path to value. (Sources: `https://arxiv.org/abs/2401.05856`) [confidence: high]
6. [inference] Tandem and adversarial patterns are already technically available as control layers, because Mixture-of-Agents, chain-of-verification, and Constitutional AI show that routing, critique, and self-checking can be layered around a base answerer to improve reliability. (Sources: `https://arxiv.org/abs/2406.04692`; `https://arxiv.org/abs/2309.11495`; `https://arxiv.org/abs/2212.08073`) [confidence: high]
7. [inference] Concept generation offers value when it creates reusable structure - ontology terms, synthetic exemplars, or distilled concept libraries - that can improve ranking, supervision, or adapters, but the available evidence does not support replacing fresh evidence retrieval with generated concepts alone. (Sources: `https://arxiv.org/abs/2306.11644`; `https://arxiv.org/abs/2504.12915`) [confidence: medium]
8. [inference] The practical escalation rule is to improve retrieval and relevance first, add adapters when repeated high-value tasks justify internalisation, and reserve full domain pretraining or new-model training for unusually large, stable, and well-funded domains rather than ordinary enterprise deployments. (Sources: `https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base.html`; `https://cloud.google.com/vertex-ai/generative-ai/docs/rag-overview`; `https://arxiv.org/abs/2106.09685`; `https://arxiv.org/abs/2305.14314`; `https://arxiv.org/abs/2303.17564`; `https://arxiv.org/abs/2212.13138`) [confidence: high]

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [fact] Retrieval is the default production answer to private organisational knowledge | `https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base.html`; `https://cloud.google.com/vertex-ai/generative-ai/docs/rag-overview`; `https://docs.cohere.com/docs/retrieval-augmented-generation-rag`; `https://www.zenml.io/llmops-database/enterprise-knowledge-management-with-llms-morgan-stanley-s-gpt-4-implementation` | high | Independent vendor docs and a deployment case agree |
| [fact] LoRA and QLoRA materially lower adaptation cost | `https://arxiv.org/abs/2106.09685`; `https://arxiv.org/abs/2305.14314`; `https://www.nature.com/articles/s42256-023-00626-4` | high | Primary papers and survey agree |
| [inference] Domain-adaptive pretraining is better suited to sector-scale or platform-scale corpora than ordinary single-enterprise use | `https://arxiv.org/abs/2303.17564`; `https://arxiv.org/abs/2212.13138`; `https://arxiv.org/abs/2004.10964`; `https://cloud.google.com/blog/products/data-analytics/glean-uses-bigquery-and-google-ai-to-enhance-enterprise-search` | medium | Strong evidence of effectiveness, medium evidence of economic boundary |
| [fact] Harvey and Glean already implement layered or tandem enterprise stacks | `https://www.harvey.ai/blog/expanding-harveys-model-offerings`; `https://www.microsoft.com/en/customers/story/19750-harvey-azure-open-ai-service`; `https://www.glean.com/resources/guides/glean-knowledge-graph`; `https://cloud.google.com/blog/products/data-analytics/glean-uses-bigquery-and-google-ai-to-enhance-enterprise-search` | high | Official vendor materials are explicit |
| [fact] Retrieval-Augmented Generation has recurring engineering failure points even when it improves grounding | `https://arxiv.org/abs/2401.05856` | high | Primary survey and experience report |
| [fact] Verifier and critic patterns can be layered around base generation | `https://arxiv.org/abs/2406.04692`; `https://arxiv.org/abs/2309.11495`; `https://arxiv.org/abs/2212.08073` | high | Academic papers establish technical feasibility |
| [inference] Concept generation is most useful as enrichment, not as full retrieval replacement | `https://arxiv.org/abs/2306.11644`; `https://arxiv.org/abs/2504.12915` | medium | Direct evidence supports ontology and synthetic-supervision uses, but not full replacement |
| [inference] Enterprises should escalate from retrieval improvements to adapters before considering heavy pretraining or new-model training | `https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base.html`; `https://cloud.google.com/vertex-ai/generative-ai/docs/rag-overview`; `https://arxiv.org/abs/2106.09685`; `https://arxiv.org/abs/2305.14314`; `https://arxiv.org/abs/2303.17564`; `https://arxiv.org/abs/2212.13138` | high | The evidence converges on staged escalation rather than immediate deep custom training |

### Assumptions

- [assumption] The ZenML Morgan Stanley write-up is a fair secondary summary of the underlying OpenAI case study. **Justification:** it provides concrete implementation details and evaluation practices consistent with other public references to the deployment, but the official OpenAI page was not directly fetchable from this environment. (Sources: `https://www.zenml.io/llmops-database/enterprise-knowledge-management-with-llms-morgan-stanley-s-gpt-4-implementation`; `https://openai.com/index/morgan-stanley/`)
- [assumption] Glean's public Google Cloud architecture post is representative of the architecture direction of its enterprise product rather than a one-off cloud-marketing example. **Justification:** it is co-authored with Glean leadership and matches Glean's own knowledge graph materials. (Sources: `https://cloud.google.com/blog/products/data-analytics/glean-uses-bigquery-and-google-ai-to-enhance-enterprise-search`; `https://www.glean.com/resources/guides/glean-knowledge-graph`)
- [assumption] Mid-to-large enterprise here means an organisation that can already sustain modern data-platform, retrieval, and evaluation work, but not frontier-foundation-model training budgets. **Justification:** the prompt asks for enterprise feasibility rather than laboratory or hyperscaler feasibility. (Sources: `https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base.html`; `https://cloud.google.com/vertex-ai/generative-ai/docs/rag-overview`; `https://www.nature.com/articles/s42256-023-00626-4`)

### Analysis

[inference] The decisive trade-off is freshness versus internalisation. Retrieval keeps answers tied to current documents and citations, while weight adaptation internalises repeated vocabulary, style, and decision patterns that would otherwise have to be re-explained on every request. (Sources: `https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base.html`; `https://arxiv.org/abs/2106.09685`; `https://arxiv.org/abs/2305.14314`)

[inference] The case studies suggest a practical ordering: start with retrieval because private knowledge changes quickly, add graph or relevance signals when retrieval quality plateaus, add parameter-efficient fine-tuning when repeated high-value tasks justify internalisation, and add verifier layers where mistakes are materially costly. (Sources: `https://www.zenml.io/llmops-database/enterprise-knowledge-management-with-llms-morgan-stanley-s-gpt-4-implementation`; `https://www.glean.com/resources/guides/glean-knowledge-graph`; `https://www.harvey.ai/blog/expanding-harveys-model-offerings`; `https://arxiv.org/abs/2406.04692`; `https://arxiv.org/abs/2309.11495`)

[inference] BloombergGPT and Med-PaLM show that going deeper into weights works when the domain is rich enough and the corpus is large enough, but Harvey, Morgan Stanley, and Glean show that most enterprise value arrives sooner from hybrid orchestration than from building a wholly new model. (Sources: `https://arxiv.org/abs/2303.17564`; `https://arxiv.org/abs/2212.13138`; `https://www.harvey.ai/blog/expanding-harveys-model-offerings`; `https://www.zenml.io/llmops-database/enterprise-knowledge-management-with-llms-morgan-stanley-s-gpt-4-implementation`; `https://cloud.google.com/blog/products/data-analytics/glean-uses-bigquery-and-google-ai-to-enhance-enterprise-search`)

[inference] Feasibility is therefore more organisational than mathematical: enterprises need authoritative corpora, evaluation sets, routing logic, and subject-matter ownership at least as much as they need graphics processing unit (GPU) budget. (Sources: `https://arxiv.org/abs/2401.05856`; `https://www.nature.com/articles/s42256-023-00626-4`)

**Feasibility Matrix**

[inference] The following matrix is a synthesis table. Each readiness, cost, time-to-value, and skill judgment is an inferential estimate drawn from the cited sources for that row.

| Approach | Claim type | Readiness | Relative cost | Data requirement | Time-to-value | Skill requirement | Sources |
|---|---|---|---|---|---|---|---|
| Prompting plus RAG | [inference] | production-ready | low to moderate | existing authoritative content | weeks | application engineers plus search / retrieval competence | `https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base.html`; `https://cloud.google.com/vertex-ai/generative-ai/docs/rag-overview`; `https://docs.cohere.com/docs/retrieval-augmented-generation-rag` |
| RAG plus knowledge graph / better rankers | [inference] | production-ready | moderate | connected systems plus relevance signals | weeks to months | search engineers plus knowledge architecture skills | `https://www.glean.com/resources/guides/glean-knowledge-graph`; `https://cloud.google.com/blog/products/data-analytics/glean-uses-bigquery-and-google-ai-to-enhance-enterprise-search`; `https://arxiv.org/abs/2401.05856` |
| PEFT with LoRA / QLoRA | [inference] | production-ready to early-adopter | moderate | curated exemplars and evaluation set | 1-3 months | machine-learning engineer, Machine Learning Operations (MLOps), subject-matter experts | `https://arxiv.org/abs/2106.09685`; `https://arxiv.org/abs/2305.14314`; `https://www.nature.com/articles/s42256-023-00626-4` |
| Full fine-tuning | [inference] | early-adopter | high | larger curated dataset | several months | stronger Machine Learning (ML) platform and evaluation capability | `https://www.nature.com/articles/s42256-023-00626-4`; `https://arxiv.org/abs/2106.09685`; `https://arxiv.org/abs/2305.14314` |
| Domain-adaptive pretraining | [inference] | early-adopter for very large domains | high to very high | massive stable corpus | several months to a year | dedicated data science, Machine Learning platform, and domain-expert support | `https://arxiv.org/abs/2303.17564`; `https://arxiv.org/abs/2212.13138`; `https://arxiv.org/abs/2004.10964` |
| Training from scratch | [inference] | uncommon outside frontier or sector-scale actors | very high | enormous corpus and compute | long horizon | frontier-model training capability | `https://arxiv.org/abs/2303.17564`; `https://arxiv.org/abs/2212.13138` |
| Tandem / critic layers | [inference] | production-ready as overlay | moderate | policies, eval prompts, routing logic | weeks to months | orchestration, prompt, and evaluation engineering | `https://arxiv.org/abs/2406.04692`; `https://arxiv.org/abs/2309.11495`; `https://arxiv.org/abs/2212.08073` |

### Risks, Gaps, and Uncertainties

- [fact] The most direct official Morgan Stanley and OpenAI case-study page was not directly fetchable from this environment, so Morgan Stanley-specific details rely on a secondary summary rather than the original page. (Source: failed fetch of `https://openai.com/index/morgan-stanley/`)
- [inference] Public vendor material may understate operational failures, so the architectural conclusions should weight the RAG failure literature more heavily than product marketing on claims of completeness. (Sources: `https://arxiv.org/abs/2401.05856`; `https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base.html`; `https://cloud.google.com/vertex-ai/generative-ai/docs/rag-overview`)
- [inference] The consulted public literature does not provide a clean cost curve for when parameter-efficient fine-tuning (PEFT) overtakes retrieval economics for a given enterprise corpus and query volume, so the economic crossover point remains uncertain. (Sources: `https://www.nature.com/articles/s42256-023-00626-4`; `https://arxiv.org/abs/2106.09685`; `https://arxiv.org/abs/2305.14314`)
- [inference] Concept generation remains under-evidenced at enterprise deployment scale relative to retrieval and PEFT, even though the component techniques are promising. (Sources: `https://arxiv.org/abs/2306.11644`; `https://arxiv.org/abs/2504.12915`)
- [assumption] The security and governance implications of training on private enterprise data remain a separate blocker for some architectures. **Justification:** the enterprise platform materials emphasise controlled access, connected data sources, and governance for retrieval systems, while this item did not investigate legal, policy, or privacy controls for weight-level training. (Sources: `https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base.html`; `https://cloud.google.com/vertex-ai/generative-ai/docs/rag-overview`)

### Open Questions

- [inference] What measurable threshold tells an enterprise that retrieval quality has plateaued enough to justify adapter training rather than another round of retrieval engineering?
- [inference] Which parts of organisational knowledge should remain permanently external for provenance reasons even if they could be internalised technically?
- [inference] Can synthetic domain corpora be made auditable enough for regulated industries to trust them as part of a production adaptation pipeline?
- [inference] What evaluation harness best measures a layered enterprise stack that combines retrieval, adapters, routing, and critic models rather than evaluating those pieces in isolation?

---

## Output

- Type: knowledge
- Description: Research on the feasibility and architecture of organisation-customised Large Language Model layers, concluding that the viable enterprise design is a layered hybrid stack combining retrieval, selective adaptation, and verifier patterns rather than a standalone organisation-trained model.
- Links:
  - https://arxiv.org/abs/2303.17564
  - https://arxiv.org/abs/2401.05856
  - https://www.harvey.ai/blog/expanding-harveys-model-offerings