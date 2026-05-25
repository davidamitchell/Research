---
title: "LLM reasoning in mathematics and programming tasks"
added: 2026-05-25T08:00:17+00:00
status: backlog
priority: medium
blocks: []
themes: [llm-reasoning, software-engineering, formal-methods]
started: ~
completed: ~
output: []
cites: [2026-03-10-language-for-llm-agent-output, 2026-03-10-formal-spec-intent-alignment-agentic-coding]
related: [2026-05-18-rq6-1-halting-problem-static-analysis, 2026-03-18-formal-proof-engineering-leanstral, 2026-04-26-llm-verifiability-asymmetry-code-world-action]
superseded_by: ~
supersedes: ~
item_type: primary
confidence: medium
versions: []
---

# LLM reasoning in mathematics and programming tasks

## Research Question

To what extent is the claim true that mathematics and programming are especially strong use cases for LLMs (Large Language Models) because both rely on formal symbolic languages that may align with model reasoning behavior?

## Scope

**In scope:**
- Evidence on LLM performance characteristics in mathematics and programming tasks.
- Mechanistic or empirical explanations for why formal symbolic domains may be favorable for LLM use.
- Prior repository learnings that can be reused to frame or test this claim.

**Out of scope:**
- Building new benchmarks or running fresh model evaluations.
- Broader claims about all non-math and non-programming domains.
- Product recommendations for a specific vendor or model family.

**Constraints:** (time, source types, access)
- Use publicly accessible sources and existing repository learnings first.
- Distinguish benchmark score evidence from causal explanation claims.

## Context

This question informs whether future research and implementation effort in this repository should prioritize mathematics and programming workflows as high-leverage domains for LLM-assisted reasoning, while grounding the claim in prior learnings before adding new assumptions.

## Approach

1. What prior findings in this repository already address language structure, formal specification, and LLM reasoning limits relevant to mathematics and programming?
2. What benchmark-level evidence supports or challenges the idea that math and code tasks are comparatively strong LLM use cases?
3. What mechanisms are proposed in the literature for why symbolic/formal language tasks may align with LLM behavior?
4. Where do current findings indicate limits, failure modes, or over-claims in this framing?

## Sources

- [ ] [davidamitchell/Research learnings.md](https://github.com/davidamitchell/Research/blob/main/learnings.md) — prior cross-item learnings to reuse before new investigation.
- [ ] [davidamitchell/Research 2026-03-10 language-for-llm-agent-output](https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-10-language-for-llm-agent-output.md) — prior item on language structure and LLM output constraints.
- [ ] [davidamitchell/Research 2026-03-10 formal-spec-intent-alignment-agentic-coding](https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-10-formal-spec-intent-alignment-agentic-coding.md) — prior item linking formal methods and agentic coding reliability.
- [ ] [Hendrycks et al. (2021) Measuring Mathematical Problem Solving With the MATH Dataset](https://arxiv.org/abs/2103.03874) — benchmark framing for mathematical reasoning evaluation.
- [ ] [Chen et al. (2021) Evaluating Large Language Models Trained on Code](https://arxiv.org/abs/2107.03374) — benchmark framing for programming task performance.
- [ ] [Wei et al. (2022) Chain-of-Thought Prompting Elicits Reasoning in Large Language Models](https://arxiv.org/abs/2201.11903) — evidence on reasoning behavior in language models.

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

3–5 sentences. What is the answer to the research question? State the key conclusion directly. Write plain prose — no prefix labels. Bind sources as trailing inline citations: `Claim text. [inference; source: https://url]`

### Key Findings

Ordered list. Each finding is a specific, evidence-backed claim with confidence and source as a trailing parenthetical. Use **suffix style** — source at the end of the claim, not at the beginning.

1. **Claim text as a complete sentence.** (high confidence; source: https://url)
2. **Claim text as a complete sentence.** (medium confidence; source: https://url1; https://url2)

Source URLs must exactly match URLs in the `## Sources` section so the generated site can render `Author (Year)` citation links. List the primary source URL(s) from `## Sources` here.

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
