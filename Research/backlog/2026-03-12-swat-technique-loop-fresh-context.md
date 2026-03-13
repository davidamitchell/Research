---
title: "SWAT technique in a fresh-context loop: reliability, drift, and the effect of web search and org RAG on blind-acceptance outcomes"
added: 2026-03-12
status: backlog
priority: medium
blocks: []
tags: [swat, prompting-techniques, agentic-systems, rag, web-search, hallucination, context-window, loop-reliability, grounding]
started: ~
completed: ~
output: [knowledge]
---

# SWAT technique in a fresh-context loop: reliability, drift, and the effect of web search and org RAG on blind-acceptance outcomes

## Research Question

When the SWAT (Strengths, Weaknesses, Assumptions, Threats) technique is executed repeatedly in a loop where each invocation uses a fresh LLM context window and the caller blindly accepts every result, what systematic failure modes emerge — and does access to web search or organisation-specific Retrieval-Augmented Generation (RAG) materially change those failure modes or their severity?

## Scope

**In scope:**
- What the SWAT technique is and the assumptions it relies on (structured critique, adversarial framing, expert prior)
- Failure modes introduced specifically by running SWAT in a stateless loop (fresh context each iteration, no memory carry-over)
- The effect of blind acceptance: how cumulative error, drift, and hallucination propagate across iterations when no human review gate exists
- Whether web search as a tool changes reliability: grounding, recency bias, retrieval quality, and new failure modes web search introduces
- Whether organisation-specific RAG changes reliability: domain grounding, retrieval precision, staleness, and new failure modes RAG introduces
- Comparison of the three conditions (no tool / web search / org RAG) on the same failure mode dimensions

**Out of scope:**
- Full implementation of a SWAT loop (this is an analysis item, not an engineering item)
- Benchmarking specific LLM models against each other on SWAT quality
- Retrieval-Augmented Generation (RAG) architecture design (covered elsewhere in the corpus)

**Constraints:** Claims about failure modes must be grounded in mechanistic reasoning or empirical evidence; unverified assertions must be labelled **[inference]** or **[assumption]**.

## Context

The SWAT technique applies a structured four-quadrant critique to a subject (Strengths, Weaknesses, Assumptions, Threats). When used with a human in the loop it functions as a deliberate adversarial check. The interesting question arises when it is delegated entirely to an LLM agent running in a loop:

- **Fresh context window each iteration** — the model has no memory of previous runs; it cannot detect drift or contradictions across iterations; each pass is independent.
- **Blind acceptance** — there is no human review gate; whatever the model outputs is treated as ground truth and fed forward (e.g. stored, acted on, or used as input to the next iteration).

This combination creates conditions that are similar to those analysed in the existing research corpus around hallucination propagation, sycophancy, and operational failure modes. The three sub-questions address the practical mitigation potential of two grounding approaches — web search and organisation RAG — that are increasingly available to agentic systems.

Related completed research that is likely directly relevant:
- `2026-03-05-llm-hallucination-mechanisms.md` — hallucination types and their propagation
- `2026-03-08-context-engineering-first-principles.md` — context window limits and instruction conflict
- `2026-03-12-failure-mode-taxonomy-expansion.md` (backlog) — failure mode taxonomy including operational failures

## Approach

1. **Characterise the baseline SWAT loop** — Define the minimal SWAT loop: input subject → LLM SWAT critique → output accepted → (optionally) used as next input. Identify the invariants (fresh context, blind acceptance) and which failure modes are structurally guaranteed to arise from those invariants alone.

2. **Map failure modes to loop mechanics** — For each failure mode class (hallucination, goal drift, sycophancy, consistency collapse, compounding error), determine whether fresh context amplifies, suppresses, or is neutral to the failure. Determine whether blind acceptance amplifies failures that would otherwise be self-correcting.

3. **Web search condition** — Re-examine each identified failure mode under the assumption that the LLM has live web search. Identify which failure modes are genuinely reduced by grounding, which are unchanged, and which new failure modes web search introduces (e.g. retrieval of outdated or low-quality sources, inconsistency across retrieved pages across iterations).

4. **Org RAG condition** — Re-examine each identified failure mode under the assumption that the LLM has access to an organisation-specific RAG index. Identify which failure modes are reduced, which are unchanged, and which new failure modes org RAG introduces (e.g. index staleness, retrieval precision gaps, false confidence from in-domain retrieval).

5. **Comparison and prioritisation** — Produce a three-column comparison table (no tool / web search / org RAG) for each failure mode dimension. Identify the highest-risk combination and the most effective mitigation available within each condition.

## Sources

- [ ] `Research/completed/2026-03-05-llm-hallucination-mechanisms.md` — hallucination propagation and types
- [ ] `Research/completed/2026-03-08-context-engineering-first-principles.md` — context window mechanics and instruction conflict
- [ ] `Research/backlog/2026-03-12-failure-mode-taxonomy-expansion.md` — failure mode taxonomy (or completed version if available)
- [ ] Lewis et al. (2020) — Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks: https://arxiv.org/abs/2005.11401
- [ ] Shuster et al. (2021) — Retrieval Augmentation Reduces Hallucination in Conversation: https://arxiv.org/abs/2104.07567
- [ ] Perez et al. (2022) — Sycophancy in AI assistants: https://arxiv.org/abs/2310.13548

---

## Research Skill Output

*(To be filled in when the research skill is run.)*

---

## Findings

*(To be populated from §6 Synthesis when the research skill is run.)*

### Executive Summary

### Key Findings

1.
2.

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| | | high / medium / low | |

### Assumptions

- **Assumption:** ... **Justification:** ...

### Analysis

### Risks, Gaps, and Uncertainties

-

### Open Questions

-

---

## Output

*(Fill in when completing — what was produced as a result of this research?)*

- Type: knowledge
- Description:
- Links:
