---
title: "Exploration-synthesis gap: why people in explore mode fail to synthesise others' work, and whether agent synthesis can close the gap"
added: 2026-03-12
status: backlog  # backlog | in-progress | reviewing | completed
priority: high
blocks: []
tags: [cognition, exploration, synthesis, knowledge-sharing, incentives, ego, agentic-systems, organisational-behaviour, psychology]
started: ~
completed: ~
output: [knowledge]
---

# Exploration-synthesis gap: why people in explore mode fail to synthesise others' work, and whether agent synthesis can close the gap

## Research Question

During periods of rapid exploration — such as the current wave of Artificial Intelligence (AI) / Large Language Model (LLM) adoption inside organisations — individuals and teams routinely duplicate effort rather than building on what colleagues have already built or learned. What are the cognitive, genetic, incentive-level, and ego-driven mechanisms that produce this pattern? And given that the exploratory work itself is increasingly done by AI agents (meaning the human may not be able to explain or articulate what was built), is human-to-human synthesis still the right mechanism, or should synthesis be delegated to agents?

## Scope

**In scope:**
- The cognitive and evolutionary basis for preferring independent exploration over reusing others' knowledge during periods of high novelty (the "explore mode" dynamic)
- Incentive system design: how individual reward structures (recognition, career progression, learning credit) actively discourage synthesis and knowledge-sharing in organisations
- Ego and identity: how personal investment in the act of discovery makes borrowing feel like a threat to identity or competence
- The agent-mediated knowledge gap: when AI agents do the work, humans often lack the tacit knowledge to explain or transfer it — and what this means for traditional knowledge-sharing mechanisms
- Whether agent-to-agent synthesis (an agent reading and synthesising another agent's work product) is a more viable route than human knowledge transfer in agentic work contexts
- Practical signals and structural interventions that have demonstrated success in closing exploration-synthesis gaps in organisations

**Out of scope:**
- General knowledge management system design (covered separately)
- Tool-level implementation of an agent synthesis pipeline (that is an engineering backlog item; this item produces the knowledge to motivate it)
- Detailed AI/LLM model architecture

**Constraints:** Evidence must span at least two of: evolutionary biology / behavioural genetics, organisational psychology, incentive design, and agentic systems. Inference labelling required throughout.

## Context

Inside organisations adopting AI, a recognisable pattern is emerging: multiple teams or individuals independently build, test, and explore similar things (prompting approaches, agent architectures, tool integrations) without systematically reviewing what others have done. This is partially rational — exploration has high individual learning value — but it also produces organisational waste, inconsistency, and missed leverage from accumulated experience.

The problem has a second layer that is new and under-examined: much of the exploratory work is now performed by AI agents, not the human. The human supervised the exploration but did not write the code, did not trace the reasoning, and may not be able to reproduce or explain the output. The traditional knowledge transfer mechanism — a human who learned something explains it to colleagues — is breaking down. The agent did the learning; the human is a spectator with a vague memory of the outcome.

This suggests the synthesis bottleneck may need to move: rather than improving human knowledge-sharing behaviour, the intervention might be agent-mediated synthesis — an agent that reads other agents' outputs, identifies overlaps, gaps, and reusable patterns, and produces a synthesised view that humans can act on.

This research item investigates the root causes of the exploration-synthesis gap and the design space of interventions, including whether the right long-run answer is human behaviour change or architectural delegation to agents.

## Approach

1. **Evolutionary and genetic basis** — Investigate what is known about the human drive for independent discovery: intrinsic motivation research (Deci and Ryan's Self-Determination Theory (SDT)), curiosity as a foraging behaviour, and any behavioural genetics evidence on individual variation in novelty-seeking versus synthesis orientation (e.g. Dopamine Receptor D4 (DRD4) gene and dopamine receptor variation in novelty-seeking; exploration–exploitation trade-off in neuroscience).

2. **Incentive systems analysis** — Survey organisational psychology and management research on how performance management, credit attribution, and innovation incentives affect knowledge-sharing behaviour. Identify the specific incentive failure modes that produce "everyone explores independently": credit not accruing to the synthesiser; exploration being visible while synthesis is invisible; reuse being perceived as lower status than origination.

3. **Ego and identity mechanisms** — Examine the psychological literature on NIH (Not Invented Here) syndrome, identity-based resistance to reuse, and the role of competence signalling. How does the act of independent discovery function as an identity claim, and what makes reuse feel threatening?

4. **Agent-mediated knowledge gap** — Investigate the emerging dynamic where agents perform exploratory work that humans cannot fully articulate. What is the state of the literature on tacit knowledge, learning transfer, and the "knowing-explaining gap"? How does agent-mediated work change the knowledge transfer problem in principle?

5. **Agent synthesis as an intervention** — Evaluate whether agent-to-agent synthesis is technically and organisationally viable: can an agent read another agent's output (code, transcripts, decision logs), identify what was learned, and produce a synthesised artefact that other humans or agents can consume? What are the prerequisites, failure modes, and design constraints?

6. **Synthesis and intervention design** — Produce a prioritised set of interventions, distinguishing: (a) structural interventions that change incentive systems; (b) process interventions that create synthesis checkpoints; (c) architectural interventions that delegate synthesis to agents. Assess which interventions are feasible given the current state of agentic tooling.

## Sources

- [ ] Deci, E. L., & Ryan, R. M. (2000) — Self-determination theory and intrinsic motivation: https://selfdeterminationtheory.org/theory/
- [ ] Berlyne, D. E. (1960) — Curiosity and exploration as foraging behaviour (foundational behavioural psychology)
- [ ] Ebstein, R. P. et al. (1996) — DRD4 exon III polymorphism and novelty-seeking: https://pubmed.ncbi.nlm.nih.gov/8700901/
- [ ] Sutton, R. S., & Barto, A. G. (2018) — Exploration–exploitation trade-off in reinforcement learning (Chapter 2): https://incompleteideas.net/book/the-book.html
- [ ] Katz, R., & Allen, T. J. (1982) — Not Invented Here (NIH) syndrome in R&D: https://www.sciencedirect.com/science/article/pii/0048733382900111
- [ ] Cross, R., & Sproull, L. (2004) — More than an answer: information relationships for actionable knowledge: https://journals.sagepub.com/doi/10.1287/orsc.1040.0075
- [ ] Szulanski, G. (1996) — Exploring internal stickiness: impediments to the transfer of best practice within the firm: https://www.jstor.org/stable/2486989
- [ ] Nonaka, I., & Takeuchi, H. (1995) — The Knowledge-Creating Company: tacit vs. explicit knowledge and knowledge transfer (HBR)
- [ ] Wang, S., & Noe, R. A. (2010) — Knowledge-sharing antecedents and outcomes review: https://www.sciencedirect.com/science/article/pii/S0001879109001018
- [ ] Davenport, T. H., & Prusak, L. (1998) — Working Knowledge: how organisations manage what they know (Chapter 4: knowledge transfer)
- [ ] Andrews, K. M., & Delahaye, B. L. (2000) — Influences on knowledge processes in organisational learning: the psychosocial filter
- [ ] OWASP / practitioner reports on agentic work artefact traceability (agent decision logging, explainability)

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

- Type: # skill | tool | agent | knowledge | backlog-item
- Description:
- Links:
