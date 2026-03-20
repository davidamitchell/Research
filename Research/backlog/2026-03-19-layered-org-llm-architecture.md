---
title: "Layered Organisation Large Language Model: Feasibility and Architecture of Organisation-Customised LLMs"
added: 2026-03-19
status: backlog  # backlog | in-progress | reviewing | completed
priority: high  # low | medium | high
blocks: []
tags: [llm, rag, fine-tuning, enterprise-ai, knowledge-management, organisational-context, architecture, feasibility, concept-generation, customisation, layered-llm, retrieval-augmented-generation, parameter-efficient-fine-tuning]
started: ~
completed: ~
output: [knowledge]
---

# Layered Organisation Large Language Model: Feasibility and Architecture of Organisation-Customised LLMs

## Research Question

Is it technically feasible and economically viable for an organisation to build a customised Large Language Model (LLM) layer that injects and optimises over organisation-specific context — internal knowledge, regulatory domain, and competitive landscape — while operating in tandem with base foundation models? If so, what architectural patterns (layered, tandem, adversarial) best address this problem, who is already doing it, and does concept generation offer a viable path beyond Retrieval-Augmented Generation (RAG)?

Supporting questions:
- What is the gap between what base LLMs know (public internet) and what an organisation needs them to know (internal context + salient external context)?
- What are the current state-of-the-art approaches to organisation-specific LLM adaptation: RAG, fine-tuning, parameter-efficient fine-tuning (PEFT), Mixture of Experts (MoE), retrieval-augmented fine-tuning, and knowledge distillation?
- What is the feasibility — technology maturity, cost, time to value, and skill requirements — of each approach for a mid-to-large enterprise?
- What does a "layered" architecture look like in practice — an org-specific adapter or model layer sitting on top of or beside a base foundation model?
- What does a "tandem" or "adversarial" architecture look like — can two models (one general, one org-specific) collaborate or check each other?
- Who is already building organisation-customised LLM systems, and what architectural choices have they made?
- Does concept generation (generative synthesis of org-specific domain concepts from internal corpora) offer a viable path that RAG alone cannot deliver?
- What are the specific failure modes of RAG that motivate exploring customised or fine-tuned models for org context?

## Scope

**In scope:**
- Architectural patterns for organisation-specific LLM customisation: RAG, fine-tuning (full and PEFT), domain-adaptive pretraining, knowledge graph augmentation, mixture-of-experts routing, model merging / model soup, and layered/tandem/adversarial multi-model architectures
- Feasibility dimensions: technology readiness level, compute and data cost estimates, time-to-value for each approach, and skill/team requirements for a typical mid-to-large enterprise
- Organisations and vendors already doing this: Bloomberg GPT, MedPaLM, Harvey AI, Morgan Stanley OpenAI deployment, Glean, Notion AI, enterprise RAG platforms (Cohere, Vertex AI Search, AWS Bedrock Knowledge Bases)
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

**Constraints:** Publicly accessible sources. Vendor documentation, technical blog posts, arXiv preprints, and open-access papers (2022–2026). Web search at retrieval time for the most current vendor and research state, as the enterprise LLM customisation landscape is evolving rapidly.

## Context

Base foundation models are trained on the public internet. They encode broad world knowledge but have two structural gaps for organisational use:

1. **Internal context gap** — the model has no knowledge of the organisation's data, decisions, processes, history, or artefacts. RAG addresses this partially: retrieve relevant internal documents and inject them into the prompt. But RAG has a ceiling: it retrieves based on surface similarity, not organisational salience; it cannot internalise the conceptual vocabulary, domain ontology, or decision heuristics that an expert in the organisation holds.

2. **Salient external context gap** — even for public information, an organisation operates within a narrower context than "the whole internet": specific regulators, specific competitors, specific markets, specific jurisdictions. A base model treats all public knowledge as equally relevant; an org-specific model should weight the org's regulatory environment, competitive landscape, and domain knowledge above general knowledge.

The issue that seeds this item asks a pointed question: is it *possible and feasible* (technology, time, money, skill) to have a customised LLM that addresses both gaps and works with, not instead of, base models? Three architectural framings are proposed in the issue — **layered** (org model on top of base model), **tandem** (org model alongside base model), and **adversarial** (org model checking or critiquing base model output) — and asks whether concept generation offers a path.

This is not a purely theoretical question: Bloomberg GPT, Harvey AI, and Morgan Stanley's OpenAI deployment all represent real enterprise bets on org-specific LLM customisation. The architectural choices they made, and the lessons learned, are part of the answer.

The prior research in this repository on context compression, context layers, and memory systems establishes that the context management problem is well understood at the prompt level. This item explores whether the problem requires going deeper — into the weights of the model itself.

## Approach

1. **Define the gap precisely** — articulate the internal context gap and salient external context gap in concrete terms. What does a model need to "know" that RAG cannot deliver? What does "org-salient external context" mean operationally (e.g., jurisdiction-specific regulation, named competitor filings, industry-specific terminology)? Use this to establish why org-customised LLMs are worth exploring beyond RAG.
2. **Map the adaptation landscape** — survey the full range of approaches from lightest to heaviest: prompt engineering and few-shot prompting → RAG → PEFT (Low-Rank Adaptation (LoRA), QLoRA, prefix tuning, adapters) → full fine-tuning → domain-adaptive pretraining → model merging / model soup → training a domain-specific model from scratch. For each: what does it require in data, compute, and skill? What org-context problems does it solve that lighter approaches cannot?
3. **Case study audit** — examine real enterprise deployments:
   - Bloomberg GPT — domain-adaptive pretraining on financial text
   - MedPaLM / Med-Gemini — medical domain adaptation
   - Harvey AI — legal domain LLM on top of GPT-4
   - Morgan Stanley + OpenAI — enterprise RAG at scale with fine-tuned retrieval
   - Glean — enterprise search and knowledge graph over internal data
   - Legal, financial, and healthcare sector examples where regulatory context is critical
   For each: what architectural approach was used, what was the stated rationale, and what are the reported outcomes or failure modes?
4. **Layered / tandem / adversarial architecture deep dive** — examine multi-model architectural patterns where one model specialises in org context while another provides general capability:
   - Layered: adapter layers, LoRA on top of frozen base, prompt/prefix injection
   - Tandem: routing (which model answers this query?), ensemble, Mixture-of-Agents (MoA)
   - Adversarial: Constitutional AI debate, model-as-critic, chain-of-verification (CoVe), self-consistency
   What is the latency, cost, and complexity overhead of each? When is each warranted?
5. **Concept generation assessment** — investigate whether generative synthesis of org-specific concepts from internal corpora is a viable path. Does training (or fine-tuning) on org data to generate a domain concept library or synthetic domain corpus create a richer representation than RAG alone? What research supports or challenges this? Is this closer to knowledge distillation, synthetic data generation, or ontology extraction?
6. **Feasibility matrix** — produce a structured feasibility assessment across the key adaptation approaches, covering: technology readiness (production-ready, early-adopter, research-only), cost range, data requirements (volume, quality, labelling), time-to-value estimate, and skill requirements (data science team, MLOps, domain experts).
7. **Synthesis** — produce Executive Summary, Key Findings, Evidence Map, and Feasibility Matrix.

## Sources

- [ ] Bloomberg GPT paper — Wu, S. et al. (2023) — "BloombergGPT: A Large Language Model for Finance" — arXiv:2303.17564
- [ ] MedPaLM paper — Singhal, K. et al. (2023) — "Large Language Models Encode Clinical Knowledge" — *Nature* — arXiv:2212.13138
- [ ] Harvey AI — public blog posts and technical writing on legal LLM deployment (2023–2026)
- [ ] Morgan Stanley + OpenAI — public case study and technical posts on enterprise RAG with fine-tuning (2023–2026)
- [ ] LoRA paper — Hu, E. et al. (2021) — "LoRA: Low-Rank Adaptation of Large Language Models" — arXiv:2106.09685
- [ ] QLoRA paper — Dettmers, T. et al. (2023) — "QLoRA: Efficient Finetuning of Quantized LLMs" — arXiv:2305.14314
- [ ] PEFT survey — Ding, N. et al. (2023) — "Parameter-Efficient Fine-Tuning of Large-Scale Pre-Trained Language Models" — *Nature Machine Intelligence*
- [ ] Domain-adaptive pretraining — Gururangan, S. et al. (2020) — "Don't Stop Pretraining: Adapt Language Models to Domains and Tasks" — ACL 2020 — arXiv:2004.10964
- [ ] Mixture-of-Agents (MoA) — Wang, J. et al. (2024) — "Mixture-of-Agents Enhances Large Language Model Capabilities" — arXiv:2406.04692
- [ ] Chain-of-Verification (CoVe) — Dhuliawala, S. et al. (2023) — "Chain-of-Verification Reduces Hallucination in Large Language Models" — arXiv:2309.11495
- [ ] Constitutional AI — Bai, Y. et al. (2022) — "Constitutional AI: Harmlessness from AI Feedback" — arXiv:2212.08073
- [ ] RAG limitations survey — Barnett, S. et al. (2024) — "Seven Failure Points When Engineering a Retrieval Augmented Generation System" — arXiv:2401.05856
- [ ] Enterprise RAG at scale — Glean technical blog and documentation (2024–2026) — https://glean.com
- [ ] Cohere enterprise RAG — Cohere documentation and technical posts (2024–2026) — https://cohere.com
- [ ] Vertex AI Search — Google Cloud documentation (2024–2026) — https://cloud.google.com/vertex-ai-search
- [ ] AWS Bedrock Knowledge Bases — AWS documentation (2024–2026) — https://aws.amazon.com/bedrock/knowledge-bases/
- [ ] Synthetic data generation for domain adaptation — Gunasekar, S. et al. (2023) — "Textbooks Are All You Need" (phi-1) — arXiv:2306.11644
- [ ] Model merging / model soup — Wortsman, M. et al. (2022) — "Model Soups: Averaging Weights of Multiple Fine-tuned Models Improves Accuracy without Increasing Inference Time" — arXiv:2203.05482
- [ ] Prior completed research: `2026-03-15-context-compression-rag-enterprise-knowledge`
- [ ] Prior completed research: `2026-03-15-context-layers-aligned-decisions-synthesis`
- [ ] Prior completed research: `2026-03-02-agent-memory-management-context-injection`
- [ ] Prior backlog item: `2026-03-17-ai-memory-systems-rag-neuroscience`
- [ ] Prior backlog item: `2026-03-18-api-context-hubs-rag-mcp`

---

## Research Skill Output

*(Full output from running the research skill — retained verbatim in the completed item. §§0–5 are the investigation; §6 seeds the Findings section below.)*

### §0 Initialise

Restate the research question. Confirm scope, constraints, and output format.

-

### §1 Question Decomposition

Approach sub-questions broken into atomic questions — each answerable with a single evidence-based claim.

-

### §2 Investigation

Evidence gathered per atomic question. Label each claim: **[fact]**, **[inference]**, or **[assumption]** with source.

-

### §3 Reasoning

Facts, inferences, and assumptions explicitly separated. No unsupported generalisations or narrative leaps.

-

### §4 Consistency Check

Internal contradictions identified and resolved (or explicitly flagged where unresolvable).

-

### §5 Depth and Breadth Expansion

Findings re-examined through relevant lenses (technical, regulatory, economic, historical, behavioural).

-

### §6 Synthesis

*(This section seeds the Findings below.)*

**Executive summary:**

**Key findings:**

**Evidence map:**

**Assumptions:**

**Analysis:**

**Risks, gaps, uncertainties:**

**Open questions:**

### §7 Recursive Review

Final pass: every section justified, all threads synthesised, every claim sourced or labelled, all uncertainties explicit.

-

---

## Findings

*(Populated from §6 Synthesis above.)*

### Executive Summary

3–5 sentences. What is the answer to the research question? State the key conclusion directly.

### Key Findings

Ordered list. Each finding is a specific, evidence-backed claim.

1.
2.

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| | | high / medium / low | |

### Assumptions

Explicit assumptions made during the investigation and the justification for each.

- **Assumption:** ... **Justification:** ...

### Analysis

How the evidence was weighed, what trade-offs were identified, and how competing interpretations were resolved.

### Risks, Gaps, and Uncertainties

What is still unknown? Where does the evidence fall short? What could change the conclusion?

-

### Open Questions

Questions that surfaced during research but are out of scope for this item. Each may become a new backlog item.

-

---

## Output

*(Fill in when completing — what was produced as a result of this research?)*

- Type: knowledge
- Description:
- Links:
