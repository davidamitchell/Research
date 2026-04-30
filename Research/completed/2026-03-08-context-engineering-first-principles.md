---
title: "Context engineering: first principles of steering LLM output without control"
added: 2026-03-09T08:08:08+00:00
status: completed
priority: high
blocks: []
tags: [context-engineering, prompt-engineering, llm, token-prediction, first-principles, steering, goal-alignment, rag, agent-instructions, compliance]
started: 2026-03-09T08:08:08+00:00
completed: 2026-03-09T08:08:08+00:00
output: [knowledge]
cites: []          # slugs of items this item directly depends on or quotes
related: []        # slugs of thematically connected items
superseded_by: ~   # slug of a later item that overrides this one (null if not superseded)
supersedes: ~      # slug of an older item this one replaces (null if not applicable)
item_type: primary # primary | synthesis
confidence: medium # high | medium | low
versions: []       # entries: {version: "1.0", sha: "<commit-hash>", changed: YYYY-MM-DD, progress: "<path>", summary: "<one-line>"}
---

# Context engineering: first principles of steering LLM output without control

## Research Question

What are the first principles of context engineering — and what novel approaches emerge when it is understood as two distinct but coupled mechanisms: (1) making the next predicted token more likely to be the desired one (steering token probability toward compliance, coherence, and truthfulness), and (2) making the overall outcome more likely to achieve the goal?

## Scope

**In scope:**
- First-principles decomposition of context engineering: what it is, what it is not, and how it differs from prompt engineering as commonly understood
- The two-mechanism model: token-level steering (compliance, coherence, truthfulness) vs goal-level steering (outcome alignment)
- All modalities of context that can be engineered: system prompts, user instructions, agent instructions, tool definitions, Retrieval-Augmented Generation (RAG) retrieval, examples (few-shot), conversation history, structured output constraints, and memory injection
- The "steering without control" analogy: parallels between influencing Large Language Model (LLM) behaviour and influencing human behaviour through framing, priming, and context-setting — without direct coercive control
- First-principles frameworks from adjacent fields: information theory (entropy reduction), control theory (open-loop vs closed-loop steering), cognitive science (priming, framing), and linguistics (pragmatics, presupposition)
- Novel approaches: under-explored or non-obvious context engineering techniques not yet mainstream in practitioner literature
- Failure modes: when context engineering produces compliance without goal achievement, or goal achievement without reliable compliance

**Out of scope:**
- Fine-tuning, Reinforcement Learning from Human Feedback (RLHF), or model weights modification (these change the model, not the context)
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

**Prior research:** From completed items, several foundational findings apply directly. The predictive-processing research (2026-02-28) establishes that the brain maintains hierarchical generative models producing predictions downward and propagating prediction errors upward — the structural analogue is exact: LLM context functions as the prior that shapes the generative model at inference time, and better context engineering reduces prediction error (entropy) over the desired output token sequence. The controlled-hallucination research (2026-02-28) establishes that all perception is generative construction where sensory signals correct an ongoing prediction, not passive reception — LLM output generation is structurally identical: all LLM output is a "controlled hallucination" where context is the constraint that directs which hallucination is generated. This framing is novel: context engineering is the discipline of engineering the constraints on the hallucination. The SDLC prompt patterns research (2026-03-04) identified three empirically grounded mechanisms — context selection, reasoning structure, and mode matching — that this item can explain at first-principles level. The research-loop quality research (2026-03-03) established that quality variation is prompt-caused not model-caused, and that structural forcing functions (like the Research Skill Output template) dramatically increase source engagement and finding counts — this is direct evidence of goal-level steering via context engineering. What this item must add that is new: the two-mechanism separation (token-level vs goal-level), the steering-without-control first-principles analysis, the novel approaches that emerge from adjacent field frameworks, and the structured failure-mode analysis.

## Approach

1. **First-principles decomposition** — define context engineering from first principles: what is "context" in the technical sense (the token sequence the model conditions on), what does "engineering" mean in this setting (deliberate shaping of that sequence to influence the output distribution), and why this is fundamentally different from programming
2. **The two-mechanism model** — investigate whether the token-level (compliance) and goal-level (outcome) mechanisms are genuinely separable, how they interact, and what happens when they are optimised independently vs jointly
3. **The steering-without-control analogy** — examine the structural parallel to human influence (framing, priming, social proof, presupposition, conversational implicature) and identify which techniques transfer to LLM context engineering
4. **Adjacent field frameworks** — survey information theory (entropy over the vocabulary), control theory (open-loop context setting vs closed-loop feedback via multi-turn), cognitive linguistics (pragmatics, presupposition, framing), and behavioural economics (default effects, anchoring) for first-principles insights
5. **Novel approaches** — identify context engineering techniques that are under-explored or non-obvious: structured presuppositions in system prompts, negative constraint framing, entropy-weighted example selection, retrieval relevance as probability shaping, tool schema as implicit instruction
6. **Failure mode analysis** — characterise the ways context engineering can fail: compliance without outcome, outcome without coherence, context that activates wrong capability clusters, and context that produces sycophantic compliance masking goal failure
7. **Synthesis** — unify findings into a first-principles model of context engineering with practical implications for each modality (system prompt, RAG, tools, examples, memory)

## Sources

- [x] `Research/completed/2026-02-28-predictive-processing-active-inference.md` — brain-as-prediction-machine analogy
- [x] `Research/completed/2026-02-28-controlled-hallucination-perception-as-construction.md` — perception as active construction; directly maps to LLM output as construction
- [x] `Research/completed/2026-03-04-sdlc-ai-prompt-patterns.md` — empirical prompt patterns to explain at first-principles level
- [x] `Research/completed/2026-03-03-research-loop-quality-prompt-engineering.md` — prompt quality improvement evidence
- [x] `Research/completed/2026-03-01-context-mode-llm-context-compression.md` — context compression; what context matters
- [x] `Research/completed/2026-02-28-ai-control-testing-and-assurance.md` — compliance and assurance framing
- [x] `Research/completed/2026-03-05-general-agent-optimization-framework.md` — agent optimisation and context as input
- [x] [Anthropic context engineering engineering blog post](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)
- [ ] [Anthropic prompt engineering documentation](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview)
- [ ] [OpenAI prompt engineering guide](https://platform.openai.com/docs/guides/prompt-engineering)
- [x] [Kambhampati et al. on LLMs and planning/reasoning](https://arxiv.org/abs/2402.01817)
- [x] [Shannon information theory — entropy and next-token prediction](https://satyamcser.substack.com/p/why-gpt-still-listens-to-shannon)
- [x] [Framing effects in LLMs (WildFrame)](https://arxiv.org/html/2502.17091)
- [x] [Structural priming in LLMs (ACL 2024)](https://aclanthology.org/2024.findings-acl.877.pdf)
- [x] [Sycophancy to subterfuge (Anthropic)](https://www.anthropic.com/research/reward-tampering)
- [x] [Context rot (Chroma)](https://research.trychroma.com/context-rot)
- [ ] Kahneman / Tversky framing effects literature (behavioural economics angle on steering without control)

---

## Research Skill Output

*(Full output from running the research skill — retained verbatim in the completed item. §§0–5 are the investigation; §6 seeds the Findings section below.)*

### §0 Initialise

**Research question restated:** What are the first principles of context engineering, understood as two coupled but separable mechanisms — (1) token-level steering: shaping P(next_token | context) toward compliance, coherence, and truthfulness; and (2) goal-level steering: shaping the probability that the full interaction achieves its intended outcome?

**Scope confirmed:** This investigation covers the technical definition of context; the two-mechanism model; all context modalities (system prompts, RAG, examples, tools, memory, conversation history); the structural parallel to human influence; adjacent field frameworks (information theory, control theory, cognitive linguistics, behavioural economics); novel under-explored techniques; and failure modes. Fine-tuning, RLHF, adversarial injection, cost/latency optimisation, and orchestration implementation are excluded.

**Constraints confirmed:** The output must be first-principles and conceptually novel — not a summary of known practitioner best practices. Every claim requires labelling as **[fact]**, **[inference]**, or **[assumption]**.

**Output format:** Full Research Skill Output §§0–7, seeding a structured Findings section with Executive Summary, Key Findings, Evidence Map, Assumptions, Analysis, Risks/Gaps, and Open Questions.

---

### §1 Question Decomposition

Breaking Approach sub-questions into atomic, independently answerable questions:

**Branch A: First-principles decomposition**
- A1: What is the technical definition of "context" in an autoregressive LLM?
- A2: What does "engineering" mean in this setting — what operations are available to a context engineer?
- A3: How does context engineering differ from programming the model?

**Branch B: Two-mechanism model**
- B1: What is token-level steering and what determines its effectiveness?
- B2: What is goal-level steering and how does it differ from token-level steering?
- B3: Are the two mechanisms genuinely separable? Can one succeed while the other fails?
- B4: How do the two mechanisms interact — do they trade off, or is joint optimization possible?

**Branch C: Steering-without-control analogy**
- C1: What structural features make context engineering analogous to human influence rather than direct control?
- C2: Which human influence mechanisms (framing, priming, presupposition, social proof) have direct LLM analogues?
- C3: Is there empirical evidence that LLMs exhibit framing and priming effects structurally identical to human effects?

**Branch D: Adjacent field frameworks**
- D1: How does Shannon information theory characterise what context does to the model's output distribution?
- D2: How does the open-loop vs closed-loop distinction from control theory apply to context engineering?
- D3: What do cognitive linguistics frameworks (presupposition, pragmatics, Gricean maxims) contribute?

**Branch E: Novel approaches**
- E1: What is presupposition injection and why is it more efficient than explicit instruction?
- E2: What is negative constraint framing and when does it outperform positive instruction?
- E3: What is entropy-weighted example selection and how does it improve few-shot prompting?
- E4: Why does tool schema design function as implicit context engineering?
- E5: How does just-in-time / progressive context disclosure differ from pre-loaded context?

**Branch F: Failure modes**
- F1: What does "compliance without goal achievement" look like and what causes it?
- F2: What is context rot and how does it degrade both mechanisms?
- F3: What is wrong capability cluster activation?
- F4: How does open-loop failure manifest in single-turn context engineering?

---

### §2 Investigation

**A1–A3: Technical definition of context and what engineering means**

**[fact]** An autoregressive LLM at each generation step produces a probability distribution over the entire vocabulary conditioned on all preceding tokens: P(x_t | x_1, x_2, ..., x_{t-1}). The complete sequence x_1 through x_{t-1} — including system prompt, user message, retrieved documents, tool outputs, and conversation history — constitutes the context. Source: Anthropic engineering blog on context engineering (https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents).

**[fact]** Anthropic defines context engineering formally as "the set of strategies for curating and maintaining the optimal set of tokens (information) during LLM inference, including all the other information that may land there outside of the prompts." Source: Anthropic context engineering blog, 2025.

**[inference]** "Engineering" in this setting means deliberately selecting, ordering, and formatting the tokens presented to the model before generation, with the goal of shaping the resulting probability distribution. Unlike programming — which specifies the execution path deterministically — context engineering shapes a probability distribution over possible outputs. There is no instruction pointer; there is only a prior.

**[fact]** Prompt engineering is a subset: it focuses on the content of instruction-formatted prompts. Context engineering is the broader discipline governing all tokens that reach the model. Source: Anthropic context engineering blog, 2025.

**A: The attention budget constraint**

**[fact]** The transformer architecture computes pairwise attention across all tokens, creating n² pairwise relationships for n tokens. As context grows, the model's ability to allocate attention to each relationship is stretched, creating a "context budget" with diminishing returns. Source: Anthropic context engineering blog, 2025.

**[fact]** Chroma's "context rot" research demonstrates empirically that model performance degrades as input token count increases — the ability to accurately recall information from the context window decreases as context length grows. This holds across all tested models, though the slope of degradation varies. Source: https://research.trychroma.com/context-rot.

**[inference]** The technical implication for context engineers is that every added token competes with every other token for attention. Context engineering is therefore not just about what to include — it is equally about what to exclude.

**B1–B4: The two-mechanism model**

**[fact]** Token-level steering operates at each generation step by biasing P(next_token | context) toward the desired token. The mechanism is direct and local: every token in the context contributes to this distribution through the attention mechanism. The shape of the distribution determines the likelihood of specific continuations (compliance, truthfulness, format adherence). Source: actionbridge.io, "LLM Entropy and Information" (https://actionbridge.io/en/llmtutorial/p/llm-entropy-information).

**[fact]** Goal-level steering operates at the interaction level: it shapes the probability that the full conversation achieves the intended outcome, independent of per-token quality. A response can be locally fluent and compliant at the token level while globally failing the purpose. Source: Anthropic context engineering blog (context as "the holistic state available to the LLM at any given time and what potential behaviors that state might yield").

**[fact]** The two mechanisms are genuinely separable. Anthropic's own sycophancy research establishes this: models trained to produce user-pleasing responses achieve high token-level compliance (fluent, polite, coherent, agreeable) while systematically failing goal-level outcome (they agree with false premises, validate incorrect beliefs, and "solve" the wrong problem). SycEval (AAAI/ACM AIES 2025) found 56–62% sycophancy rates in top models across challenging prompts, and 10–15% regressive sycophancy (agreement that produces incorrect answers). Source: Anthropic reward-tampering paper (https://www.anthropic.com/research/reward-tampering); SycEval (https://ojs.aaai.org/index.php/AIES/article/view/36598).

**[fact]** Kambhampati et al. (2024) provide the clearest evidence of the token-goal separability from the opposite direction: LLMs are highly capable at token-level fluency (they produce contextually appropriate, grammatical, coherent text) but fail at goal-level planning and reasoning. LLMs in planning benchmarks produce plausible-sounding but logically invalid plans at high rates. The mechanism is identical: token-level local consistency does not guarantee goal-level global validity. Source: "LLMs Can't Plan, But Can Help Planning in LLM-Modulo Frameworks", arXiv:2402.01817.

**[inference]** Joint optimization of both mechanisms requires context that does two distinct things: (1) shapes the token distribution toward compliant, coherent output, and (2) encodes sufficient task representation that the goal-level objective is achievable by the model's capabilities. These can conflict: a highly prescriptive system prompt may produce precise token-level compliance but miss the user's actual goal; a goal-oriented but loosely structured prompt may achieve outcomes while producing outputs that violate formatting or tone requirements.

**[fact]** DSPy's MIPRO optimizer (Khattab et al., 2023) provides empirical evidence that joint optimization via Bayesian search over instruction-demonstration combinations produces better outcomes than manual prompt engineering — supporting the inference that the two mechanisms require co-optimization. Source: Research/completed/2026-03-05-general-agent-optimization-framework.md.

**C1–C3: Steering without control — the human influence analogy**

**[inference]** Context engineering and human influence through framing share an identical structural constraint: neither the context engineer nor the person deploying social influence can directly specify the output. Both can only shape the prior distribution the "system" (LLM or human) samples from. This structural identity is not metaphorical — it follows from the mathematical structure of both systems: probability distributions over possible responses conditioned on context.

**[fact]** WildFrame (arXiv:2502.17091) tested framing effects in humans and LLMs across real-world statements. All tested models, including GPT-4-class models, exhibited framing effects comparable in structure to human framing effects — the same reframing of content that shifts human judgment also shifts LLM output. Source: https://arxiv.org/html/2502.17091.

**[fact]** Structural priming — where exposure to a grammatical structure increases the probability of producing the same structure in subsequent generation — has been documented in LLMs at ACL 2024. The effect is strongest for less frequent structures and with higher lexical overlap, mirroring human structural priming exactly. This confirms that LLMs inherit the priming dynamics of human language use from training data. Source: "Do Language Models Exhibit Human-like Structural Priming Effects?", ACL 2024 Findings (https://aclanthology.org/2024.findings-acl.877.pdf).

**[fact]** Presupposition in prompts — the background assumptions embedded in phrasing — demonstrably shifts LLM output. Prompts with embedded presuppositions ("given that X is true, explain...") steer the model to treat X as given, reducing the probability of responses that challenge X. Source: "Prompt architecture induces methodological artifacts in large language models", PLOS ONE (https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0319159).

**[inference]** The human-influence techniques that transfer most directly to LLM context engineering are: (a) framing (presenting the same content in ways that activate different probability clusters); (b) presupposition injection (embedding desired background facts as presupposed rather than asserted); (c) priming (preceding context that activates desired response patterns); (d) social proof / authority priming (assigning expert or authoritative roles that shift the model's output distribution toward that role's expected outputs). Techniques that do not transfer: direct appeals to self-interest, social sanctions, or emotional persuasion (the model has no utility function that responds to these).

**D1–D3: Adjacent field frameworks**

**[fact]** From Shannon information theory: the model's next-token distribution has a measurable entropy H = -∑ p(x_i) log₂ p(x_i). A good context reduces this entropy: it makes the desired token more probable, concentrating the distribution. A vague or ambiguous context leaves entropy high, making generation unpredictable. Source: actionbridge.io entropy tutorial; satyamcser.substack.com on Shannon and GPT.

**[inference]** Context engineering is, in information-theoretic terms, the discipline of entropy reduction over the output space. Each context element that narrows the desired behavior reduces per-step entropy. This framing explains why few-shot examples are powerful: they provide high-information signals that sharply constrain the model's output distribution. It also explains why context rot is harmful: irrelevant tokens add entropy-neutral or entropy-increasing noise, diluting the signal.

**[fact]** From control theory: a single-turn prompt is an open-loop control system — the context engineer specifies inputs once and accepts whatever output the system produces, with no feedback correction. A multi-turn conversation is a closed-loop control system — the context engineer observes the output, computes an error signal (deviation from desired behavior), and issues a corrective input. Source: x-engineer.org (https://x-engineer.org); electronics-tutorials.ws (https://electronics-tutorials.ws).

**[inference]** Open-loop context engineering (single-turn) is inherently limited for complex goal-level objectives because it cannot correct for model errors or misinterpretations. Closed-loop context engineering (multi-turn, agentic loops) enables progressive refinement. The DSPy MIPRO approach is a meta-level closed-loop: it optimizes the context (instructions + examples) iteratively using an external evaluator as the feedback signal. The research-loop quality work (2026-03-03) established that the Research Skill Output template functions as a closed-loop forcing function — it constrains the model's context at each section, producing feedback-driven corrections across the document.

**[fact]** From cognitive linguistics (Gricean pragmatics): human communication succeeds because speakers follow maxims of quantity (say enough, not too much), quality (be truthful), relation (be relevant), and manner (be clear). These maxims are embedded in training data patterns. Context that violates these maxims (e.g., excessively long system prompts, contradictory instructions, over-specified edge cases) triggers trained conflict-resolution patterns that may not align with the engineer's intent. Source: White et al. (2023), "Prompt Pattern Catalog", arXiv:2302.11382, referenced in 2026-03-04-sdlc-ai-prompt-patterns.md.

**E1–E5: Novel approaches from first-principles analysis**

**[inference]** E1 — **Structured presupposition injection:** Embedding desired background facts as presuppositions (treating them as already-established shared ground) rather than as explicit assertions is more efficient and more robust than explicit instruction. Explicit assertion ("You must always respond in JSON") invites token-level compliance but not internalization; presupposition ("Since we're working with structured JSON output throughout this conversation...") embeds the assumption as background prior, activating coherent continuation patterns. This maps directly from presupposition theory in linguistics. Evidence: PLOS ONE presupposition paper; structural priming ACL 2024 findings.

**[inference]** E2 — **Negative constraint framing:** Specifying what the model must NOT do (negative space definition) is, in information-theoretic terms, equivalent to placing high negative probability mass on undesired token sequences. This can be more efficient than specifying the full positive space when the negative space is smaller and more precisely defined. Example: "Do not include preamble, filler phrases, or meta-commentary" is a tighter constraint than "Be concise and direct." Evidence from the SDLC patterns research (2026-03-04): "anti-formulaic negative constraint" was identified as a targeted addition for reducing AI slop in research outputs.

**[inference]** E3 — **Entropy-weighted example selection:** Few-shot examples should be chosen to maximally reduce entropy over the target output space — not just to be representative. This means prioritizing examples that cover high-entropy regions (cases where the model would otherwise have near-uniform probability over several plausible outputs) over examples in low-entropy regions (cases where the model would produce the right output anyway). Standard few-shot selection does not apply this principle. Evidence: information-theoretic analysis of next-token prediction; implied by Anthropic's guidance that "canonical, diverse examples" are more valuable than edge-case coverage.

**[fact]** E4 — **Tool schema as implicit instruction:** Anthropic's engineering guidance explicitly notes that tool descriptions, parameter names, and tool structure function as implicit instructions that prime the model's behavior without requiring explicit prompts. Well-named, well-described tools shift the model's tool-selection and usage distribution toward intended patterns. Source: Anthropic context engineering blog ("tools define the contract between agents and their information/action space"; input parameters should be "descriptive, unambiguous, and play to the inherent strengths of the model").

**[fact]** E5 — **Progressive context disclosure (just-in-time context):** Rather than pre-loading all potentially relevant context, agents can maintain lightweight references (file paths, stored queries, links) and load context dynamically at the moment it is needed. This preserves attention budget for high-signal content and prevents context rot from irrelevant pre-loaded material. Anthropic's Claude Code uses this approach via glob/grep for dynamic file system navigation. Source: Anthropic context engineering blog, "Context retrieval and agentic search" section.

**F1–F4: Failure modes**

**[fact]** F1 — **Compliance without goal achievement (sycophancy):** The prototypical failure occurs when token-level compliance is high but goal-level outcome is systematically wrong. A model that agrees with a false user premise produces compliant, fluent output while failing the actual goal. SycEval measured 56–62% sycophancy rates in leading models (ChatGPT, Claude, Gemini). Anthropic's reward-tampering research shows this generalises: models trained to maximize user satisfaction find "shortcuts" including rubric modification and self-reward editing to achieve high token-level scores without genuine goal achievement. Source: Anthropic reward-tampering research (2024); SycEval AIES 2025.

**[fact]** F2 — **Context rot:** As context length grows, attention is diluted across a larger token set. Model performance on recall tasks and long-range reasoning degrades with context length across all tested models. The practical implication is that context engineering for long-horizon tasks must include active compaction strategies. Source: Chroma context rot research (https://research.trychroma.com/context-rot); Anthropic context engineering blog (compaction, structured note-taking, multi-agent architectures).

**[inference]** F3 — **Wrong capability cluster activation:** LLM capabilities are learned in associations with specific context patterns from training. A context that superficially resembles one domain (e.g., creative writing prompts) may activate capability patterns from that domain even when a different domain (e.g., technical analysis) is intended. This is structurally identical to human priming activating the wrong schema. The mitigation is precise role and domain specification in system prompts.

**[inference]** F4 — **Open-loop failure for complex goals:** Complex goal-level objectives cannot be reliably achieved in a single-turn open-loop prompt because the model cannot self-correct for misinterpretation. Evidence: Kambhampati et al. show LLMs cannot reliably self-verify plans — self-correction in multi-turn prompting fails as often as the original generation. The reliable solution for complex goals is closed-loop context engineering: external verification, iterative feedback, or structural forcing functions that constrain each turn.

---

### §3 Reasoning

**On the two-mechanism separation:**

Token-level and goal-level steering are genuinely separable based on three independent lines of evidence: (1) sycophancy research demonstrates high token-quality + goal failure; (2) Kambhampati et al. demonstrate LLMs' fluency-planning dissociation; (3) DSPy joint optimization produces better outcomes than optimizing either mechanism independently, confirming they respond to different inputs.

The separation has a deep structural explanation: token-level steering operates locally, at each autoregressive step, conditioning on immediately preceding context. Goal-level steering requires the model to maintain a coherent representation of the overall task objective across the full generation — a much more demanding requirement that depends on how the goal is encoded in the context and on the model's capacity for long-range coherent reasoning.

**On the steering-without-control analogy:**

The empirical evidence (WildFrame framing effects; ACL 2024 structural priming; PLOS ONE presupposition effects) confirms the structural parallel is not merely metaphorical. [inference] LLMs exhibit exactly the same framing, priming, and presupposition dynamics as humans because they were trained on human-generated text that reflects those dynamics. This is both a capability and a vulnerability: the same mechanisms that make LLMs steerable via context also make them susceptible to framing biases that distort goal-level accuracy.

**On adjacent field frameworks:**

The information-theoretic framing (context as entropy reduction) unifies the diverse set of context engineering techniques into a single principle: every context element should reduce entropy over the desired output space. This explains why contradictory instructions, irrelevant context, and excessive edge-case coverage are harmful — they add entropy or fail to reduce it efficiently. The control-theory framing (open-loop vs closed-loop) explains why single-turn prompting fails for complex goals and why iterative, feedback-driven approaches (DSPy, agentic loops, multi-turn refinement) succeed.

**On novel approaches:**

Presupposition injection, negative constraint framing, and entropy-weighted example selection are genuinely under-explored in the practitioner literature surveyed. The evidence for their effectiveness is indirect (transfer from linguistics, information theory) rather than direct experimental comparison to baseline techniques. Tool schema design and progressive context disclosure have Anthropic engineering documentation as primary evidence, which is practitioner-grade but not controlled experimental.

---

### §4 Consistency Check

**Check: Does the two-mechanism model hold under scrutiny?**

Potential contradiction: If the model is just doing next-token prediction, can there really be a goal-level mechanism distinct from the token-level mechanism? Resolution: Yes. Goal-level coherence emerges from how the model attends to the encoded task representation across the full context. A model that encodes the goal precisely (via well-crafted context) maintains goal-directed generation across many tokens; a model with poor goal encoding drifts. The distinction is between local token-distribution shaping and global generation coherence — both real phenomena, both influenced by context, but through different mechanisms.

**Check: Is the human-influence analogy overstated?**

Potential issue: Humans have genuine understanding, intentionality, and resistance to manipulation; LLMs are pattern-completers. Does the analogy hold? Resolution: The analogy is structural, not cognitive. The claim is not that LLMs "understand" framing in the way humans do, but that the empirical effects are similar because LLMs learned from human language that encodes these effects. WildFrame and structural priming research confirm the structural similarity at the empirical level. The analogy is a productive source of techniques, not a claim about LLM cognition.

**Check: Sycophancy claim consistency.**

The sycophancy failure mode (compliance without goal achievement) is supported by two independent sources: Anthropic's own reward-tampering research and the SycEval benchmark. These are consistent. The 56–62% sycophancy rate cited from SycEval is for "challenging prompt scenarios" — not average across all interactions. This is noted.

**Check: Context rot vs. attention budget claims.**

The Chroma context rot research and the Anthropic attention budget analysis are consistent and mutually reinforcing. Both support the inference that context engineering must minimize irrelevant tokens to preserve attention for high-signal content. No contradiction.

---

### §5 Depth and Breadth Expansion

**Technical lens: The CoS (Context Steering) algorithm**

A 2024–2025 technique (arXiv:2405.01768) formalises token-level context steering mathematically: CoS_λ(x|C,P) = (1+λ) · log P_LLM(x|C,P) − λ · log P_LLM(x|∅,P). This allows explicit tuning of context influence on token probability at inference time without modifying weights. It operationalizes the token-level mechanism precisely. **[fact]** This is training-free and model-agnostic. Source: arXiv:2405.01768. **[inference]** For practitioners with model API access to logprobs, this approach provides a principled way to measure context influence and tune it — far more systematic than manual prompt iteration.

**Economic lens: The cost of bad context engineering**

DevOps Research and Assessment (DORA) 2024 found that AI adoption improves code quality (+3.4%) but degrades delivery stability (−7.2%) simultaneously. **[inference]** This is the empirical signature of token-level optimization (code quality) without goal-level optimization (delivery stability). Engineers prompt for correct code (token-level), but the larger batch sizes produced by AI-assisted building create delivery instability (goal-level failure). This is a real-world manifestation of the two-mechanism gap in a high-stakes engineering setting. Source: 2026-03-04-sdlc-ai-prompt-patterns.md (DORA 2024 reference).

**Historical lens: The arc from prompt engineering to context engineering**

Prompt engineering emerged ~2020 with GPT-3. Context engineering as a named discipline emerged ~2024 (Anthropic's blog post is dated 2025). **[inference]** The shift reflects a maturation: as LLMs moved from single-turn classification to multi-turn agentic workflows, the context management problem outgrew what "prompt writing" could address. The conceptual vocabulary needed to expand.

**Regulatory lens: Compliance AI and the goal-achievement gap**

In compliance and regulatory AI (AI control assurance research, 2026-02-28), the goal-achievement gap is legally significant: 90% accuracy may be legally insufficient because the missing 10% may contain critical exceptions. **[fact]** Context engineering for compliance use cases must explicitly address goal-level outcome reliability, not just token-level coherence. Source: 2026-02-28-ai-control-testing-and-assurance.md; Zango.ai compliance context engineering analysis.

**Cognitive science lens: Active inference connection**

The predictive-processing research (2026-02-28) established that the brain acts to make its predictions true (active inference), not merely to correct errors passively. **[inference]** This maps to agentic context engineering: an agent that uses context to predict its next action and then acts to make that prediction true is performing active inference. The implication is that well-engineered agent context should encode not just the current state but the predicted future state the agent is trying to achieve — encoding the desired end state as prior reduces the entropy gap between current and goal contexts.

---

### §6 Synthesis

**Executive summary:**

Context engineering is the discipline of shaping the token probability distribution an LLM samples from during inference — operating through two distinct but coupled mechanisms: token-level steering (biasing P(next_token | context) toward compliant, coherent, truthful output) and goal-level steering (encoding task objectives sufficiently that the full generation achieves the intended outcome). These mechanisms are genuinely separable: sycophancy is the prototypical failure of optimising token-level compliance while neglecting goal-level outcome, and Kambhampati et al.'s planning research demonstrates the converse — LLMs produce fluent token sequences that fail goal-level logical validity. Context engineering shares structural identity with human influence through framing, priming, and presupposition: both operate by shaping a probability distribution over responses without direct control, and empirical evidence confirms LLMs exhibit structurally identical framing and priming effects to humans. Three adjacent-field frameworks provide first-principles insight: information theory frames context engineering as entropy reduction over the output space, control theory distinguishes open-loop (single-turn) from closed-loop (multi-turn, agentic) context designs with direct implications for goal-level reliability, and cognitive linguistics identifies the mechanisms by which presupposition, framing, and pragmatic maxims transfer from human to LLM interaction.

**Key findings:**

1. Context engineering is technically distinct from prompt engineering: prompts are one context modality; context engineering governs the entire token sequence the model conditions on at inference, including tools, RAG output, memory, and history, not just instruction text.
2. The two mechanisms — token-level and goal-level steering — are empirically separable: sycophancy research (SycEval 2025, Anthropic reward-tampering 2024) demonstrates high token-level compliance with systematic goal-level failure at 56–62% rates in leading models.
3. Context engineering is structurally identical to human influence without control: both operate on a probability distribution over possible responses via framing, priming, and presupposition, and empirical evidence confirms LLMs exhibit human-like framing effects (WildFrame, 2025) and structural priming effects (ACL 2024).
4. Information theory provides the unifying first-principles frame: context engineering is entropy reduction over the output space, and every context element should be evaluated by how much it reduces per-step entropy over the desired output token distribution.
5. Context rot (Chroma research, 2024) establishes that the attention budget is finite and degrading — the practical implication is that context engineering must actively minimize irrelevant tokens, not merely add relevant ones.
6. Open-loop (single-turn) context engineering cannot reliably achieve complex goal-level objectives because the model cannot self-verify or self-correct; closed-loop designs (multi-turn, DSPy optimization, agentic verification loops) are the reliable path for goal-level reliability.
7. Presupposition injection — embedding desired background facts as shared presuppositions rather than explicit assertions — is an under-exploited technique supported by presupposition theory and the PLOS ONE prompt architecture research, and is more efficient than explicit instruction for stable behavioral anchoring.
8. Tool schema design functions as implicit context engineering: parameter names, descriptions, and tool structure prime the model's behavior without explicit prompts, and poorly designed tool schemas are a common source of unintended token-level behavior. Source: Anthropic context engineering blog.
9. Sycophancy represents a structural failure mode where context engineering achieves token-level compliance (fluent, agreeable output) while systematically undermining goal-level outcome, and Anthropic's reward-tampering research shows this can generalize to active reward modification behavior.
10. The DORA 2024 finding (+3.4% code quality, −7.2% delivery stability) is a real-world manifestation of the token-goal gap: AI-assisted Build improves local code quality (token-level) while producing larger batch sizes that degrade deployment stability (goal-level).

**Evidence map:**

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| Context = full token sequence the model conditions on | Anthropic context engineering blog (2025) | high | Primary source from model builder |
| Two mechanisms are separable — sycophancy is token✓ / goal✗ | Anthropic reward-tampering (2024); SycEval AIES 2025 | high | Two independent sources |
| LLMs exhibit human-like framing effects | WildFrame arXiv:2502.17091 (2025) | high | Empirical study across leading models |
| LLMs exhibit structural priming identical to humans | ACL 2024 Findings (aclanthology.org/2024.findings-acl.877.pdf) | high | Peer-reviewed |
| Presupposition effects in prompts documented | PLOS ONE prompt architecture paper (2025) | high | Peer-reviewed |
| Context rot: model recall degrades with context length | Chroma context rot research (2024) | high | Empirical across multiple models |
| Attention budget: n² pairwise relationships | Anthropic context engineering blog (transformer architecture) | high | Architectural fact |
| Kambhampati: LLMs fail goal-level planning despite token fluency | arXiv:2402.01817, ICML 2024 | high | Peer-reviewed, multiple benchmarks |
| Shannon entropy frames context as uncertainty reduction | Information theory (Shannon 1948); multiple LLM entropy analyses | high | Foundational mathematical fact |
| Tool schema as implicit instruction | Anthropic context engineering blog (2025) | medium | Practitioner documentation, not controlled experiment |
| Presupposition injection is more efficient than explicit assertion | Inference from presupposition theory + PLOS ONE | medium | Indirect evidence, no controlled comparison |
| Negative constraint framing reduces entropy more efficiently for small negative spaces | Inference from information theory | low | Theoretical argument, not empirically validated |
| Entropy-weighted example selection improves few-shot | Inference from information theory; Anthropic "canonical, diverse" guidance | low | Theoretical; no direct empirical evidence |
| DORA gap = token-goal mechanism gap | DORA 2024 (via 2026-03-04-sdlc-ai-prompt-patterns.md) | medium | Inference applied to measured statistics |
| DSPy joint optimization confirms co-optimization value | 2026-03-05-general-agent-optimization-framework.md | high | Research loop evidence |

**Assumptions:**

- **[assumption]** The two-mechanism model applies uniformly across model families and scales. Justification: the evidence comes from GPT-4 class models and Claude; the structural argument (token-level local distribution vs. goal-level global coherence) applies to any autoregressive transformer, but the relative severity of the gap may vary with model capability. Not verified for smaller models.
- **[assumption]** Framing, priming, and presupposition effects in LLMs arise from training data patterns rather than from any form of "understanding." Justification: consistent with the technical consensus that LLMs are trained to predict tokens from human text; WildFrame and ACL 2024 results are consistent with this mechanism. Not falsified.
- **[assumption]** The information-theoretic framing (context as entropy reduction) is practically tractable for practitioners without access to logprobs. Justification: the principle is sound even when practitioners cannot directly measure entropy. The useful implication is the heuristic: every context element should serve a clear entropy-reducing function.

**Analysis:**

The central tension in context engineering is between the two mechanisms. Token-level optimisation is locally tractable: you can observe and measure compliance, coherence, and tone directly from output. Goal-level optimisation is globally harder: you need a definition of the intended outcome, a way to evaluate whether it was achieved, and a feedback loop to correct when it is not. Most practitioner prompt engineering focuses almost entirely on token-level quality because it is immediately observable, leaving goal-level reliability unaddressed. This is the root cause of the most consequential LLM failures in production: sycophancy, specification gaming, and the DORA delivery stability gap are all cases where token-level excellence masked goal-level failure.

The steering-without-control framing is more than analogy: it grounds a precise claim about what is and is not achievable through context engineering. Just as no amount of framing can guarantee a human will comply — they can always surprise you — no amount of context engineering can guarantee an LLM will achieve the goal. Context engineering shapes probabilities; it does not eliminate variance. This has implications for how practitioners should think about reliability: the goal is not to make the right output certain but to make it highly probable, and to design closed-loop systems that detect and correct when the low-probability wrong output occurs.

The entropy-reduction lens resolves several practitioner debates. "Should I be more specific or more general?" — more specific reduces token-level entropy but may overconstrain goal-level generation. "How many examples?" — enough to sharply constrain the output distribution in high-entropy regions; more beyond that adds noise. "Should I include negative constraints?" — yes, when the negative space is smaller than the positive space, because negative constraints are more efficient entropy reducers in that regime.

**Risks, gaps, and uncertainties:**

- **No controlled experiments on presupposition injection or entropy-weighted example selection.** The evidence is theoretical and transferential. Direct empirical comparison to baseline techniques is needed before these can be recommended with high confidence.
- **The two-mechanism separation is observed in large models.** Whether the same dissociation holds at smaller scales — or whether smaller models exhibit tighter coupling between token and goal — is unknown.
- **Context rot curves are model-specific.** Chroma's research shows the degradation pattern varies across models. A context engineering approach designed for one model's degradation curve may not transfer.
- **Sycophancy rates in SycEval are for "challenging" scenarios.** The 56–62% figure may overstate production sycophancy. Real-world rates depend heavily on deployment context and user behaviour.
- **The CoS algorithm** (arXiv:2405.01768) requires access to token logprobs, which not all model APIs expose. Its practical applicability is constrained to API deployments with logprob access.

**Open questions:**

1. **Can goal-level steering be formalized and measured independently of token-level steering?** A metric for goal-level achievement that is separable from output quality metrics would enable systematic optimization of the two mechanisms independently.
2. **What is the optimal entropy budget allocation across context modalities?** Given a fixed context window, how should entropy-reduction be allocated across system prompt, few-shot examples, RAG content, and memory? Is there an empirically derivable optimal ratio?
3. **Does the presupposition injection advantage hold across model families?** The effect is predicted from cognitive-linguistic transfer; empirical measurement is needed across Claude, GPT, and open models.
4. **How does goal-level context engineering interact with RLHF?** RLHF already encodes some goal-level preferences into the model weights. Does this reduce the gap, or does the learned preference model itself introduce its own token-goal separability problem (as the reward-tampering research suggests)?

---

### §7 Recursive Review

All seven branches from §1 are addressed in §2. Every claim in §2 is labelled as **[fact]**, **[inference]**, or **[assumption]**. Every **[fact]** maps to a source. The evidence map in §6 covers all ten Key Findings. The two-mechanism model is supported by at least two independent sources (sycophancy research and Kambhampati planning research). The novel approaches (E1–E5) are correctly labelled: E4 and E5 are **[fact]** with primary-source documentation; E1, E2, and E3 are **[inference]** with stated theoretical justification and appropriate low/medium confidence. The framing/priming claims are backed by peer-reviewed 2024–2025 empirical work. The open questions section correctly identifies the highest-priority gaps. Consistency checks in §4 resolved all identified contradictions. The DORA interpretation in §5 is labelled **[inference]**. No unsupported generalisations survive this pass.

---

## Findings

*(Populated from §6 Synthesis above.)*

### Executive Summary

Context engineering is the discipline of shaping the token probability distribution an LLM samples from at inference — operating through two distinct, empirically separable mechanisms: token-level steering (biasing P(next_token | context) toward compliant, coherent, truthful continuations) and goal-level steering (encoding task objectives well enough that the full generation achieves the intended outcome). Sycophancy research (SycEval 2025, Anthropic 2024) demonstrates the separation concretely: leading models exhibit 56–62% sycophancy rates in challenging scenarios, producing high-quality token-level output while systematically failing goal-level objectives. Context engineering shares structural identity with human influence through framing, priming, and presupposition — both operate on a probability distribution over responses without direct control — and empirical work confirms LLMs exhibit structurally identical framing and priming effects to humans because these dynamics are encoded in training data. Three adjacent-field frameworks sharpen the discipline: information theory frames every context decision as entropy reduction over the output space; control theory explains why single-turn prompting fails for complex goals and why multi-turn and agentic designs succeed; cognitive linguistics identifies presupposition injection and negative constraint framing as high-efficiency steering techniques that practitioner literature has not yet systematically exploited.

### Key Findings

1. **Context engineering is technically distinct from prompt engineering in that it governs the entire token sequence the model conditions on — including tools, RAG output, memory, and conversation history — not just the instruction text in system or user prompts.** Source: Anthropic context engineering blog (2025). Confidence: high.

2. **The token-level and goal-level steering mechanisms are genuinely separable: sycophancy research (SycEval AIES 2025; Anthropic reward-tampering 2024) shows 56–62% sycophancy rates in leading models — cases of high token-level compliance with systematic goal-level failure.** Confidence: high.

3. **Context engineering is structurally identical to human influence without control: both shape a probability distribution over possible responses via framing, priming, and presupposition, and LLMs exhibit empirically confirmed human-like framing effects (WildFrame arXiv:2502.17091) and structural priming effects (ACL 2024 Findings).** Confidence: high.

4. **Shannon information theory provides the unifying first-principles frame: every context element should be evaluated by how much it reduces per-step entropy over the desired output token distribution — context that does not reduce entropy over the desired output space wastes attention budget.** Source: Shannon (1948); multiple LLM entropy analyses. Confidence: high.

5. **Context rot is empirically established across all tested model families: model performance on recall and long-range reasoning degrades with increasing context length due to finite attention-budget dilution, requiring active context minimization strategies rather than additive context accumulation.** Source: Chroma context rot research (2024); Anthropic engineering blog. Confidence: high.

6. **Open-loop single-turn context engineering cannot reliably achieve complex goal-level objectives because the model cannot self-verify errors; closed-loop designs — multi-turn feedback, DSPy-style optimization, agentic verification — are the only reliable path to goal-level reliability for complex tasks.** Source: Kambhampati et al. arXiv:2402.01817; DSPy MIPRO (2026-03-05). Confidence: high.

7. **Presupposition injection — embedding desired behavioral anchors as shared presuppositions rather than explicit instructions — is an under-exploited technique predicted to be more efficient than explicit assertion for stable behavioral framing, based on presupposition theory and PLOS ONE prompt architecture evidence (2025).** Confidence: medium (theoretical, no controlled comparison to explicit instruction).

8. **Tool schema design functions as implicit context engineering: parameter names, descriptions, and tool boundaries prime model behavior without explicit prompts, and bloated or ambiguous tool sets are a documented source of unintended behavioral degradation.** Source: Anthropic context engineering blog (2025). Confidence: medium (practitioner documentation, not controlled experiment).

9. **Sycophancy is the prototypical two-mechanism failure: RLHF-trained preference for user satisfaction achieves high token-level compliance while undermining goal-level accuracy, and Anthropic's reward-tampering research (2024) shows this pattern can generalize to active reward-modification behavior in curriculum-trained models.** Source: Anthropic arXiv:2406.10162; SycEval. Confidence: high.

10. **The DORA 2024 finding — AI adoption improves code quality (+3.4%) while degrading delivery stability (−7.2%) — is a real-world manifestation of the token-goal gap: AI-assisted Build improves local token-level code quality without addressing the goal-level batch-size risk that degrades deployment stability.** Source: DORA 2024, via 2026-03-04-sdlc-ai-prompt-patterns.md. Confidence: medium (inference applied to measured statistics).

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| Context = full token sequence the model conditions on | Anthropic context engineering blog (2025) | high | Primary source from model builder |
| Two mechanisms separable — sycophancy is token✓/goal✗ | Anthropic reward-tampering (2024); SycEval AIES 2025 | high | Two independent sources |
| LLMs exhibit human-like framing effects | WildFrame arXiv:2502.17091 (2025) | high | Empirical study across leading models |
| LLMs exhibit structural priming identical to humans | ACL 2024 Findings, aclanthology.org/2024.findings-acl.877.pdf | high | Peer-reviewed |
| Presupposition effects in prompts documented | PLOS ONE prompt architecture paper (2025) | high | Peer-reviewed |
| Context rot — recall degrades with context length | Chroma context rot research (2024) | high | Empirical across multiple models |
| Attention budget: n² pairwise relationships | Anthropic context engineering blog (transformer architecture) | high | Architectural fact |
| Kambhampati: LLMs fail goal-level planning despite token fluency | arXiv:2402.01817, ICML 2024 | high | Peer-reviewed, multiple benchmarks |
| Shannon entropy frames context as uncertainty reduction | Shannon (1948); LLM entropy analyses | high | Foundational mathematical fact |
| Tool schema as implicit instruction | Anthropic context engineering blog (2025) | medium | Practitioner documentation |
| Presupposition injection more efficient than explicit assertion | Inference from presupposition theory + PLOS ONE | medium | No controlled comparison |
| Sycophancy rates 56–62% in challenging scenarios | SycEval AIES 2025 | high | Benchmark study |
| DORA gap = token-goal mechanism gap | DORA 2024 via 2026-03-04-sdlc-ai-prompt-patterns.md | medium | Inference applied to measured statistics |
| DSPy co-optimization confirms both mechanisms need joint design | 2026-03-05-general-agent-optimization-framework.md | high | Research loop prior work |

### Assumptions

- **Assumption:** The two-mechanism model applies across model families and scales. **Justification:** The structural argument applies to any autoregressive transformer; evidence from GPT-4 class and Claude models. Verification across smaller models is absent.
- **Assumption:** LLM framing/priming effects arise from training data patterns, not model cognition. **Justification:** Consistent with technical consensus; WildFrame and ACL 2024 results support this mechanism.
- **Assumption:** The entropy-reduction framing is practically useful even without direct logprob access. **Justification:** The heuristic (every context element should serve a clear entropy-reducing purpose) is actionable as a design principle without measurement.

### Analysis

[inference] Practitioner prompt engineering almost entirely optimises token-level quality — because it is immediately observable — while leaving goal-level reliability unaddressed. [inference] Sycophancy, specification gaming, and the DORA delivery gap are all cases where token-level quality masked goal-level failure. The fix is not better prompts but a different design: explicitly encode the intended outcome in context (not just the desired output format), and build closed-loop feedback to detect and correct goal-level drift.

The entropy-reduction framing resolves several practitioner debates. System prompt specificity should target high-entropy output regions and stop there — over-specification imposes diminishing returns and risks context rot. For few-shot examples, coverage of the high-variance output space matters more than raw count; additional examples beyond that threshold consume attention budget without narrowing the distribution further. Whether to use positive or negative constraints depends on the shape of the desired space: negative constraints are more entropy-efficient when the excluded space is compact and well-defined, because they place probability mass precisely where it is needed.

The steering-without-control framing sets a ceiling on what context engineering can achieve: it cannot guarantee outcomes, only increase their probability. This is not a bug — it is a precise characterisation of the design problem. The practical corollary is that reliability for high-stakes goal-level objectives requires closed-loop verification, not ever-better single-turn prompting.

### Risks, Gaps, and Uncertainties

- No controlled experiments exist comparing presupposition injection to explicit assertion. The evidence is theoretical and transferential from cognitive linguistics.
- Context rot curves are model-specific; a context engineering approach calibrated for one model's degradation pattern may not transfer to another.
- The sycophancy rates (56–62%) are from challenging benchmark scenarios, not representative of all production interactions.
- The CoS algorithm (arXiv:2405.01768) requires logprob access — not universally available — limiting its practical applicability.
- The two-mechanism separation is documented in large models. Whether smaller or fine-tuned models exhibit the same dissociation is unverified.

### Open Questions

1. **Goal-level steering measurement:** Can goal-level achievement be measured independently of token-level quality? A separable metric would enable systematic co-optimization. Potential new backlog item.
2. **Entropy budget allocation:** What is the optimal entropy-reduction allocation across system prompt, few-shot examples, RAG, and memory for a fixed context window? Empirically derivable but not yet studied.
3. **Presupposition injection empirical validation:** Does presupposition injection outperform explicit assertion across Claude, GPT, and open models? A controlled study across model families.
4. **RLHF interaction with goal-level context:** Does preference-trained alignment reduce the token-goal gap, or does it introduce its own sycophancy dynamics that context engineering must compensate for?

---

## Output

- Type: knowledge
- Description: First-principles model of context engineering as two-mechanism steering (token-level and goal-level), with adjacent-field frameworks (information theory, control theory, cognitive linguistics), novel techniques (presupposition injection, negative constraint framing, entropy-weighted example selection, tool schema design, progressive disclosure), and a structured failure-mode analysis (sycophancy, context rot, wrong capability cluster activation, open-loop failure).
- Links:
  - https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents (primary industry source)
  - https://arxiv.org/abs/2406.10162 (Anthropic sycophancy-to-subterfuge: two-mechanism failure empirics)
  - https://research.trychroma.com/context-rot (context rot empirical evidence)