---
title: "Are Human Brains Just Prediction Machines? Comparing Predictive Processing and Large Language Model Next-Token Generation"
added: 2026-03-18
status: backlog  # backlog | in-progress | reviewing | completed
priority: medium  # low | medium | high
blocks: []
tags: [neuroscience, cognitive-science, llm, predictive-processing, predictive-coding, next-token-prediction, world-models, consciousness, free-energy-principle]
started: ~
completed: ~
output: [knowledge]
---

# Are Human Brains Just Prediction Machines? Comparing Predictive Processing and Large Language Model Next-Token Generation

## Research Question

What is the fundamental difference between the predictive processing account of human cognition — in which the brain continuously generates and updates a generative model of the world — and Large Language Model (LLM) next-token prediction, and does this difference matter for understanding intelligence, meaning, and consciousness?

Supporting questions:
- What does the Predictive Processing (PP) / Predictive Coding (PC) framework say about how the brain works, and how well is it supported by neuroscience evidence?
- How does LLM next-token generation actually work, and in what specific ways does it differ from the PP account?
- Is "generating a model of the world" meaningfully different from "predicting the next token in a sequence"?
- What role does embodiment, action, and the Free Energy Principle (FEP) play in the PP account that has no analogue in LLMs?
- What do the similarities and differences imply about consciousness, understanding, and the plausibility of general intelligence emerging from next-token prediction?

## Scope

**In scope:**
- The Predictive Processing / Predictive Coding framework (Helmholtz, Friston, Clark, Seth) — the claim that perception and cognition are fundamentally generative model-based prediction
- Karl Friston's Free Energy Principle (FEP) as the unifying mathematical framework for PP
- Andy Clark's "Surfing Uncertainty" / "Being There" framing of PP and embodied cognition
- Anil Seth's work on "controlled hallucination" and the beast machine thesis
- LLM next-token generation mechanics: autoregressive Transformer (AT) architecture, self-supervised pre-training, temperature/sampling, emergent capabilities
- Mechanistic interpretability research bearing on whether LLMs develop internal world models (Nanda et al., Grokking, linear representation probes)
- The "stochastic parrot" critique (Bender et al., 2021) and responses to it
- Philosophical framing: symbol grounding, intentionality, understanding vs. prediction

**Out of scope:**
- Reinforcement learning from human feedback (RLHF) or instruction tuning mechanics (unless directly relevant to the world-model question)
- Detailed implementation of specific LLM architectures beyond what is needed to contrast with PP
- Clinical neurology, pharmacology, or pathological cases unless they illuminate the core question
- The engineering question of "how to build better AI" — this is a conceptual/scientific research item

**Constraints:** Publicly accessible sources. Neuroscience and cognitive science literature (Friston, Clark, Seth, Helmholtz). LLM mechanistic interpretability papers (arXiv, 2020–2026). Web search for recent debate and synthesis pieces.

## Context

The issue that seeds this item draws a sharp contrast: LLMs are "random next token generators" while humans "constantly generate models of the world." This intuition maps onto a genuine scientific debate.

The Predictive Processing (PP) framework, developed by Karl Friston and popularised by Andy Clark and Anil Seth, claims that the brain is fundamentally a generative model that predicts sensory inputs and updates itself based on prediction error. Under this view, perception is not passive reception — it is active hypothesis testing. The brain hallucinates a best guess about reality and is corrected by surprise.

LLMs are trained to minimise next-token prediction loss across massive text corpora. They learn statistical regularities in language. A surface reading says: "that's just autocomplete." A more careful reading asks: what representations must a model develop to predict text well at scale? Mechanistic interpretability research has found evidence for linear world-model features in LLMs — structured internal representations of entities, spatial relations, and temporal states. This is not nothing.

The question is whether these are the same phenomenon at different scales and substrates, superficially similar but fundamentally different, or somewhere between those poles. The answer has implications for how we think about intelligence, meaning, and the plausibility of understanding emerging from prediction.

This item connects to prior work on AI memory (`2026-03-17-ai-memory-systems-rag-neuroscience`) and neurological context management (`2026-03-15-neurological-context-management`), but its core focus is the conceptual and scientific gap between the two prediction paradigms.

## Approach

1. **PP framework summary** — survey the Predictive Processing / Predictive Coding literature. What is the core claim? What evidence supports it? How does the Free Energy Principle (FEP) unify perception, action, and learning under a single mathematical framework? Draw on Friston (2010), Clark (2016), Seth (2021).
2. **LLM mechanics summary** — describe next-token prediction in autoregressive Transformers. What is the training objective? What representations emerge? What does the evidence from mechanistic interpretability say about internal world models in LLMs?
3. **Structural comparison** — identify the key architectural and functional differences: embodiment and action-orientation in PP vs. passive text generation in LLMs; continuous online learning and prediction error minimisation in PP vs. batch pre-training in LLMs; hierarchical generative models in PP vs. attention-based sequence models in LLMs.
4. **World-model question** — what does it mean to "generate a model of the world"? Is LLM in-context reasoning a form of world modelling? What is the evidence for and against LLMs having grounded, structured world models?
5. **Consciousness and understanding** — what does the PP account say about consciousness (Seth's "controlled hallucination")? Does the PP framework imply that a sufficiently good predictive model could be conscious? What are the implications for LLMs?
6. **Synthesis** — produce Executive Summary, Key Findings, and Evidence Map.

## Sources

- [ ] Karl Friston (2010) — "The free-energy principle: a unified brain theory?" — *Nature Reviews Neuroscience* — https://doi.org/10.1038/nrn2787
- [ ] Andy Clark (2016) — *Surfing Uncertainty: Prediction, Action, and the Embodied Mind* — Oxford University Press
- [ ] Anil Seth (2021) — *Being You: A New Science of Consciousness* — Dutton
- [ ] Jakob Hohwy (2013) — *The Predictive Mind* — Oxford University Press
- [ ] Rao & Ballard (1999) — "Predictive coding in the visual cortex" — *Nature Neuroscience* — seminal PP paper
- [ ] Bender et al. (2021) — "On the Dangers of Stochastic Parrots" — FAccT 2021 — the "no understanding" critique
- [ ] Nanda et al. (2023) — "Progress measures for grokking via mechanistic interpretability" — arXiv:2301.05217 — evidence for internal structure in LLMs
- [ ] Gurnee & Tegmark (2023) — "Language Models Represent Space and Time" — arXiv:2310.02207 — world-model features in LLMs
- [ ] Kambhampati et al. (2024) — "Can LLMs Plan?" — debate on whether LLMs have genuine world models
- [ ] Recent web search: current state of mechanistic interpretability evidence for LLM world models (2024–2026)
- [ ] Prior backlog item: `2026-03-17-ai-memory-systems-rag-neuroscience`
- [ ] Prior backlog item: `2026-03-15-neurological-context-management`

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
