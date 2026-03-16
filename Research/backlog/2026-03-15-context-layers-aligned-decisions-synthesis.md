---
title: "Aligned Decision-Making: Context Architecture for AI Agents in Organisations"
added: 2026-03-15
status: backlog  # backlog | in-progress | reviewing | completed
priority: high  # low | medium | high
blocks: []  # slugs (filename without .md) of backlog items that cannot start until this one is complete
tags: [context-architecture, alignment, decision-making, enterprise-ai, rag, knowledge-management, organisational-strategy, synthesis]
started: ~
completed: ~
output: [knowledge]
---

# Aligned Decision-Making: Context Architecture for AI Agents in Organisations

## Research Question

What framework should an organisation adopt to ensure that AI agents making or supporting decisions have access to the right layered organisational context — spanning regulatory boundaries, values and purpose, vision and mission, strategy, policies and standards, current operating position, and immediate task intent — without relying on an impractically large context window?

What insights from cognitive science and state-of-the-art context-management techniques (Retrieval-Augmented Generation (RAG), compression, context architecture) inform the design and sequencing of that framework?

## Scope

**In scope:**
- The full hierarchy of organisational context layers required for aligned decision-making: regulations, values/purpose, vision/mission, strategy, policies/standards/frameworks/guidelines, current operating position (budget, work in flight, priorities, dates), intent, and immediate task
- Synthesis of findings from the two prerequisite items:
  - `2026-03-15-context-compression-rag-enterprise-knowledge` — RAG, context compression, and context architecture techniques
  - `2026-03-15-neurological-context-management` — neurological basis of human contextual reasoning
- Existing enterprise knowledge management frameworks (e.g., TOGAF, Cynefin, Wardley Maps) insofar as they address context layering for decision-making
- AI alignment literature addressing the challenge of instilling values and purpose into agents operating within organisations
- Practical architectures: how to represent, store, retrieve, compress, and compose multi-layer context for AI decision support
- Identification of the remaining gaps and open research questions that this framework does not yet resolve

**Out of scope:**
- Detailed implementation of RAG pipelines (covered in the prerequisite item)
- Detailed neuroscience beyond what was synthesised in the prerequisite item
- Political or ethical analysis of corporate governance beyond how it shapes context requirements
- Specific enterprise software product comparisons

**Constraints:** Builds primarily on findings from the two prerequisite backlog items above, supplemented by any directly relevant literature not covered there. Publicly accessible sources only.

## Context

Every non-trivial decision made within an organisation is implicitly shaped by multiple layers of context: the regulatory environment sets hard constraints; organisational values and purpose define what "good" means; vision and mission set the direction; strategy narrows the options; policies and standards govern how work gets done; current operating position (budget, projects in flight, market conditions, priorities) sets the feasible envelope; and finally the immediate task and intent define what the decision actually needs to accomplish.

Human decision-makers carry all of this — compressed, indexed, and selectively retrieved — in their heads. AI agents do not have this luxury: they operate from an explicit context window of finite size, and the challenge of constructing that window is non-trivial. Naively concatenating all relevant organisational documents would produce a context that is too large, too noisy, and too undifferentiated to drive high-quality reasoning.

This synthesis item is the capstone of a three-item cluster. It draws on:
1. The technical landscape of RAG, compression, and context architecture techniques (`2026-03-15-context-compression-rag-enterprise-knowledge`).
2. The cognitive science of how human brains layer and filter context (`2026-03-15-neurological-context-management`).

The goal is to produce actionable insights and a working framework: how should an organisation structure, store, and serve its multi-layer context to AI agents so that those agents can make decisions that are genuinely aligned — not just stylistically consistent, but substantively coherent with what the organisation is, where it is going, and what it currently needs?

## Approach

1. Synthesise the context-layer hierarchy: define each layer (regulatory, values/purpose, vision/mission, strategy, policies, current state, priorities, intent, task), its update frequency, its typical volume, and its relevance profile (when is each layer critical vs. background noise?).
2. Map findings from the RAG/compression item onto each layer: which retrieval and compression techniques are best suited to each layer given its characteristics (static vs. dynamic, dense vs. sparse, authoritative vs. advisory)?
3. Map findings from the neuroscience item onto the architecture: which cognitive mechanisms (schema compression, hierarchical attention, PFC gating) have direct analogues in context management design, and what design principles follow?
4. Survey existing enterprise knowledge management and AI alignment frameworks for relevant structural insights.
5. Identify the key design tensions: completeness vs. focus, timeliness vs. stability, general values vs. specific task constraints — and propose resolution strategies.
6. Draft a reference framework: a layered context architecture with recommendations for representation, storage, retrieval, compression, and composition at each layer.
7. Explicitly state what remains unknown, what the framework cannot yet resolve, and what the next research questions are.

## Sources

- [ ] Findings from `2026-03-15-context-compression-rag-enterprise-knowledge` (prerequisite — must be completed first)
- [ ] Findings from `2026-03-15-neurological-context-management` (prerequisite — must be completed first)
- [ ] Anthropic — "Constitutional AI: Harmlessness from AI Feedback" (arXiv:2212.08073) — values/purpose instillation approach
- [ ] OpenAI — "Aligning Language Models to Follow Instructions" (InstructGPT paper, arXiv:2203.02155) — intent alignment
- [ ] TOGAF 10 standard overview (open sections) — enterprise architecture context layers
- [ ] Cynefin framework documentation (Cognitive Edge) — context and decision complexity
- [ ] Wardley Maps introduction (Simon Wardley) — strategic context and situational awareness
- [ ] https://arxiv.org/abs/2309.11206 — "AgentBench: Evaluating LLMs as Agents" — empirical grounding for agent decision quality
- [ ] Recent ACL/NeurIPS/ICLR papers on context window management and long-context reasoning (search at retrieval time for latest, post-2024)

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
