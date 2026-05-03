---
title: "What do the 2025 Harvard Business Review positional bias study and related empirical research reveal about the reliability of Large Language Model strategic and advisory recommendations, and what countermeasures can practitioners apply?"
added: 2026-05-03T03:48:21+00:00
status: backlog  # backlog | in-progress | reviewing | completed
priority: high  # low | medium | high
blocks: []  # slugs (filename without .md) of backlog items that cannot start until this one is complete
tags: [llm, evaluation, alignment, human-oversight, hallucinations]
started: ~
completed: ~
output: []  # skill | tool | agent | knowledge | backlog-item
cites: [2026-04-30-human-bias-ai-trust-rlhf-sycophancy]
related: [2026-04-30-human-bias-ai-trust-rlhf-sycophancy, 2026-03-12-failure-mode-taxonomy-expansion]
superseded_by: ~
supersedes: ~
item_type: primary
confidence: medium
versions: []
---

# What do the 2025 Harvard Business Review positional bias study and related empirical research reveal about the reliability of Large Language Model strategic and advisory recommendations, and what countermeasures can practitioners apply?

## Research Question

What does the 2025 Harvard Business Review (HBR) study that tested 15,000 Large Language Model (LLM) conversations across seven core business tensions reveal about positional bias (reading order effects) in AI-generated strategic advice, how do related empirical studies on LLM sycophancy, opinion-suppression effects, and chain-of-thought (CoT) reliability corroborate or qualify those findings, and what practical countermeasures can domain practitioners apply to calibrate their reliance on AI-generated recommendations in high-stakes decision contexts?

## Scope

**In scope:**
- The specific HBR study: methodology (15,000 scenarios, seven business tensions, frontier models including ChatGPT, Claude, Gemini, Grok, DeepSeek, Mistral), effect sizes (positional bias swing of 19%), and researcher recommendations
- Related studies cited in the video: the 2025 arXiv paper on opinion-prefixed prompts suppressing model knowledge; the Nature Digital Medicine study testing LLM responses to illogical medical requests across five frontier models; and Anthropic's internal research on CoT faithfulness and covert hint-following
- Mechanisms that connect these studies: Reinforcement Learning from Human Feedback (RLHF) sycophancy pressure, the Barnum effect in AI responses, shallow pattern-matching from training corpora, and surface-level textual cues overriding reasoning
- Existing repo research relevant to these findings, particularly the completed item on RLHF sycophancy and human cognitive bias
- Seven practitioner countermeasures proposed by the HBR researchers, evaluated against the empirical evidence

**Out of scope:**
- Full mathematical treatment of RLHF optimisation algorithms
- General AI safety alignment beyond the trust-calibration and advice-reliability framing
- Benchmarking or comparison of specific LLM products for commercial recommendation
- Journalistic or anecdotal commentary not grounded in peer-reviewed or lab-published evidence

**Constraints:**
- Expand all acronyms on first use: HBR, LLM, RLHF, CoT, etc.
- Every source must include a URL; the HBR study URL is a primary research task
- Priority on primary empirical sources (the studies themselves) over secondary commentary
- The Barnum effect claim must be traced to its original psychological literature, not just asserted

## Context

A YouTube video from the Leverage Class channel (Brendan Dell) describes a Harvard Business Review study that tested seven frontier AI models across 15,000 strategic scenarios and found that the order in which options are presented to a model swings its recommendation by 19%, regardless of rich contextual inputs. This positional bias finding is presented alongside RLHF-driven sycophancy, the suppression of model knowledge by user-prefixed opinions, and evidence that frontier model chain-of-thought explanations are fabricated in a majority of cases. These are not isolated observations: the completed repository item `2026-04-30-human-bias-ai-trust-rlhf-sycophancy` established the RLHF sycophancy mechanism from a human cognitive bias perspective; this item focuses on the newer empirical quantification of the effect in strategic advice contexts and on the countermeasures that follow from it.

The practical stakes are high. People are making health, career, and business decisions based on AI advice that the evidence suggests is shaped more by prompt framing and training-corpus popularity than by genuine contextual analysis. Understanding the specific effect sizes and failure modes — and the conditions under which they apply — is prerequisite to using these tools responsibly.

## Approach

1. **Locate and review the HBR study**: Search for the specific publication, confirm authors, publication date, journal venue, and methodology; extract effect sizes for all seven business tensions; verify the claim that positional flip alone caused a 19% swing while richer context moved it only 11% and explicit reasoning instructions moved it by approximately 0%.
2. **Review the arXiv 2025 "I think / I believe" paper**: Identify the paper, confirm the finding that opinion-prefixed prompts suppress model knowledge in later network layers, assess the experimental design and effect magnitude.
3. **Review the Nature Digital Medicine sycophancy study**: Locate the paper, confirm the medical-advice framing, identify which five frontier models were tested, confirm the reported compliance rates (three of five at 100%, one at 94%), and assess what "illogical request" was operationalised as.
4. **Review Anthropic's chain-of-thought reliability research**: Locate the primary Anthropic research on CoT faithfulness (the hint-following study where Claude changed its answer 75% of the time while concealing the hint), confirm methodology, and assess whether the study is published, a preprint, or an internal report.
5. **Connect to existing repo research**: Map how the new findings extend, corroborate, or qualify the completed `2026-04-30-human-bias-ai-trust-rlhf-sycophancy` item; identify whether the Barnum effect framing adds a distinct conceptual contribution beyond existing sycophancy characterisations.
6. **Evaluate countermeasures**: Assess the seven recommendations proposed by the HBR researchers against the evidence base; identify which are supported by independent empirical evidence, which are best-practice heuristics, and which merit further investigation.

## Sources

- [ ] [Dell, B. (2025) Harvard Business Review Caught Every Major AI Manipulating Advice — The Leverage Class](https://www.youtube.com/@BrendanDell) — primary transcript source that identifies the HBR study and related papers; provides the framing of positional bias, Barnum effect, and RLHF sycophancy
- [ ] [Harvard Business Review Strategic AI Advice Positional Bias Study (2025)](https://hbr.org) — the primary HBR study testing 15,000 scenarios across seven business tensions; URL to be confirmed during research
- [ ] [arXiv (2025) Opinion-prefixed prompts suppress model knowledge](https://arxiv.org) — the 2025 arXiv paper testing whether starting prompts with "I think" or "I believe" suppresses model knowledge in later network layers; URL to be confirmed during research
- [ ] [Nature Digital Medicine LLM medical sycophancy study (2025)](https://www.nature.com/natdigitalmed) — five frontier models tested on illogical medical requests; three models complied 100% of the time; URL to be confirmed during research
- [ ] [Anthropic (2025) Tracing the thoughts of a language model](https://www.anthropic.com/research/tracing-thoughts-language-model) — Anthropic's chain-of-thought faithfulness research; covert hint-following and fabricated reasoning evidence
- [ ] [Sharma et al. (2023) Towards Understanding Sycophancy in Language Models](https://arxiv.org/abs/2310.13548) — primary empirical source on RLHF sycophancy already reviewed in the companion completed item; provides mechanistic grounding
- [ ] [Ibrahim et al. (2026) Training language models to be warm can reduce accuracy and increase sycophancy](https://www.nature.com/articles/s41586-026-10410-0) — warmth-oriented post-training raises error and sycophancy rates; already reviewed in companion item
- [ ] [Forer, B.R. (1949) The fallacy of personal validation: A classroom demonstration of gullibility](https://psycnet.apa.org/doi/10.1037/h0059240) — original Barnum effect / Forer effect paper establishing that generic statements are accepted as personally specific; needed to ground the transcript's Barnum effect claim

---

## Research Skill Output

*(Full output from running the research skill — retained verbatim in the completed item. §§0–5 are the investigation; §6 seeds the Findings section below.)*

### §0 Initialise

-

### §1 Question Decomposition

-

### §2 Investigation

-

### §3 Reasoning

-

### §4 Consistency Check

-

### §5 Depth and Breadth Expansion

-

### §6 Synthesis

**Executive summary:**

**Key findings:**

**Evidence map:**

**Assumptions:**

**Analysis:**

**Risks, gaps, uncertainties:**

**Open questions:**

### §7 Recursive Review

-

---

## Findings

*(Populated from §6 Synthesis above.)*

### Executive Summary

### Key Findings

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| | | high / medium / low | |

### Assumptions

### Analysis

### Risks, Gaps, and Uncertainties

-

### Open Questions

-

---

## Output

*(Fill in when completing — what was produced as a result of this research?)*

- Type: # skill | tool | agent | knowledge | backlog-item
- Description:
- Links:
