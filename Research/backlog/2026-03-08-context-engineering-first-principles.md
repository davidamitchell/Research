---
title: "Context engineering: first principles of steering LLM output without control"
added: 2026-03-08
status: backlog
priority: high
blocks: []
tags: [context-engineering, prompt-engineering, llm, token-prediction, first-principles, steering, goal-alignment, rag, agent-instructions, compliance]
started: ~
completed: ~
output: [knowledge]
---

# Context engineering: first principles of steering LLM output without control

## Research Question

What are the first principles of context engineering — and what novel approaches emerge when it is understood as two distinct but coupled mechanisms: (1) making the next predicted token more likely to be the desired one (steering token probability toward compliance, coherence, and truthfulness), and (2) making the overall outcome more likely to achieve the goal?

## Scope

**In scope:**
- First-principles decomposition of context engineering: what it is, what it is not, and how it differs from prompt engineering as commonly understood
- The two-mechanism model: token-level steering (compliance, coherence, truthfulness) vs goal-level steering (outcome alignment)
- All modalities of context that can be engineered: system prompts, user instructions, agent instructions, tool definitions, RAG retrieval, examples (few-shot), conversation history, structured output constraints, and memory injection
- The "steering without control" analogy: parallels between influencing LLM behaviour and influencing human behaviour through framing, priming, and context-setting — without direct coercive control
- First-principles frameworks from adjacent fields: information theory (entropy reduction), control theory (open-loop vs closed-loop steering), cognitive science (priming, framing), and linguistics (pragmatics, presupposition)
- Novel approaches: under-explored or non-obvious context engineering techniques not yet mainstream in practitioner literature
- Failure modes: when context engineering produces compliance without goal achievement, or goal achievement without reliable compliance

**Out of scope:**
- Fine-tuning, RLHF, or model weights modification (these change the model, not the context)
- Prompt injection attacks (adversarial context manipulation is a separate concern)
- Cost or latency optimisation of context (covered in `2026-03-01-context-mode-llm-context-compression.md`)
- Tool or agent orchestration frameworks (implementation detail, not first principles)

**Constraints:** Focus on novel, first-principles thinking — not a survey of existing prompt engineering best practices already well-documented elsewhere. Practitioner "tips" lists are explicitly out of scope; the goal is conceptual clarity and novel insight.

## Context

The working hypothesis (from the problem statement) is that context engineering has two coupled purposes:

1. **Token-level compliance:** Making the next predicted token — and the sequence that follows — more likely to be the token we want: compliant, truthful, coherent, and cohesive. The context shapes the probability distribution over the vocabulary at each generation step.

2. **Goal-level outcome:** Making it more likely that the interaction achieves its intended purpose, independent of moment-to-moment token quality. A response can be fluent and compliant yet fail to solve the problem.

These are not identical. A system prompt that produces very polite, coherent responses may fail to achieve the task goal. A terse, direct system prompt may achieve the goal while producing abrupt outputs. Understanding this distinction at the first-principles level has practical implications for every context engineering decision.

The "steering without control" framing is central: we cannot directly set the model's output. We can only shape the probability distribution it samples from. This is structurally identical to how humans influence other humans — through framing, priming, social context, and incentive design — without being able to directly control their choices. Understanding this shared structure may surface novel techniques borrowed from persuasion theory, behavioural economics, and cognitive linguistics.

Cross-references (to be updated once this item is completed):
- `Research/completed/2026-02-28-ai-control-testing-and-assurance.md` — compliance and assurance framing; the control-testing lens is relevant to verifying that context engineering achieves both compliance and goal outcomes
- `Research/completed/2026-03-01-context-mode-llm-context-compression.md` — context compression is a downstream application of context engineering; understanding what context matters for token steering informs what to compress
- `Research/completed/2026-03-04-sdlc-ai-prompt-patterns.md` — emergent prompt patterns in software engineering; many patterns described there are implicit context engineering techniques that this research can explain at first-principles level
- `Research/completed/2026-03-03-research-loop-quality-prompt-engineering.md` — the research loop prompt is itself a context engineering artefact; first-principles analysis may reveal why certain prompt changes improved quality
- `Research/completed/2026-02-28-predictive-processing-active-inference.md` — the brain-as-prediction-machine framework is structurally analogous to the LLM token-prediction model; active inference (minimising prediction error) maps onto context engineering as a way of reducing the model's uncertainty about desired outputs
- `Research/completed/2026-02-28-controlled-hallucination-perception-as-construction.md` — perception as active construction rather than passive reception directly parallels LLM output as active construction from context; the "controlled hallucination" frame offers a novel angle on why context engineering works
- `Research/completed/2026-03-05-general-agent-optimization-framework.md` — agent optimisation and context engineering are coupled; the general framework likely assumes context as an input parameter without theorising about how it works

## Approach

1. **First-principles decomposition** — define context engineering from first principles: what is "context" in the technical sense (the token sequence the model conditions on), what does "engineering" mean in this setting (deliberate shaping of that sequence to influence the output distribution), and why this is fundamentally different from programming
2. **The two-mechanism model** — investigate whether the token-level (compliance) and goal-level (outcome) mechanisms are genuinely separable, how they interact, and what happens when they are optimised independently vs jointly
3. **The steering-without-control analogy** — examine the structural parallel to human influence (framing, priming, social proof, presupposition, conversational implicature) and identify which techniques transfer to LLM context engineering
4. **Adjacent field frameworks** — survey information theory (entropy over the vocabulary), control theory (open-loop context setting vs closed-loop feedback via multi-turn), cognitive linguistics (pragmatics, presupposition, framing), and behavioural economics (default effects, anchoring) for first-principles insights
5. **Novel approaches** — identify context engineering techniques that are under-explored or non-obvious: structured presuppositions in system prompts, negative constraint framing, entropy-weighted example selection, retrieval relevance as probability shaping, tool schema as implicit instruction
6. **Failure mode analysis** — characterise the ways context engineering can fail: compliance without outcome, outcome without coherence, context that activates wrong capability clusters, and context that produces sycophantic compliance masking goal failure
7. **Synthesis** — unify findings into a first-principles model of context engineering with practical implications for each modality (system prompt, RAG, tools, examples, memory)

## Sources

- [ ] `Research/completed/2026-02-28-predictive-processing-active-inference.md` — brain-as-prediction-machine analogy
- [ ] `Research/completed/2026-02-28-controlled-hallucination-perception-as-construction.md` — perception as active construction; directly maps to LLM output as construction
- [ ] `Research/completed/2026-03-04-sdlc-ai-prompt-patterns.md` — empirical prompt patterns to explain at first-principles level
- [ ] `Research/completed/2026-03-03-research-loop-quality-prompt-engineering.md` — prompt quality improvement evidence
- [ ] `Research/completed/2026-03-01-context-mode-llm-context-compression.md` — context compression; what context matters
- [ ] `Research/completed/2026-02-28-ai-control-testing-and-assurance.md` — compliance and assurance framing
- [ ] `Research/completed/2026-03-05-general-agent-optimization-framework.md` — agent optimisation and context as input
- [ ] Anthropic prompt engineering documentation: https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview
- [ ] OpenAI prompt engineering guide: https://platform.openai.com/docs/guides/prompt-engineering
- [ ] Kambhampati et al. on LLMs and planning/reasoning: https://arxiv.org/abs/2404.11584
- [ ] Shannon information theory and entropy — original 1948 paper or accessible treatment
- [ ] Kahneman / Tversky framing effects literature (behavioural economics angle on steering without control)

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
