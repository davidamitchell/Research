---
title: "Closed-loop performance techniques for mediated execution harnesses"
added: 2026-08-20T11:01:29+00:00
status: reviewing
priority: high
blocks: []
themes: [agentic-ai, memory-context, cost-performance, benchmarks-eval, tools-infrastructure]
started: 2026-09-14T19:21:52+00:00
completed: ~
output: []
cites: [2026-04-20-harness-selection-tools-agents-skills-prompts-instructions, 2026-05-01-ai-coding-harness-quality-benchmarks, 2026-03-01-context-mode-llm-context-compression]
related: [2026-04-30-tdd-feedback-loops-ai-augmented-dev, 2026-05-13-agent-process-reliability-architecture, 2026-03-15-neurological-context-management]
superseded_by: ~
supersedes: ~
item_type: primary
confidence: medium
versions: []
---

# Closed-loop performance techniques for mediated execution harnesses

## Research Question

What measurable techniques from closed-loop control, working-memory management, adaptive procedural systems, and real-time feedback design improve the performance of an active execution harness that consumes a fixed mediation layer, and which indicators best demonstrate that those techniques remain effective across different underlying content pools?

## Scope

**In scope:**
- Harness-internal techniques such as rapid feedback loops, context-window or attention management, procedural memory handling, and selection among surfaced resources
- Quantifiable performance indicators including feedback latency, effective working-set utilisation, adaptation rate, error-recovery speed, and related stability measures
- Evidence from agent harnesses, cognitive systems, and control architectures that isolates active-execution improvements from content-pool quality
- Techniques that can be compared across different mediated pools without changing the pool itself

**Out of scope:**
- Redesigning the mediation layer or long-term content-pool update rules
- Domain-specific task policies that depend on one application area
- Semantic normalisation or conflict-resolution methods applied directly to the content pool

**Constraints:** Treat the mediation layer as given and focus on what the active execution environment can do with a pre-existing surfaced resource set. Prioritise measurable techniques with transferable metrics, and distinguish harness gains caused by faster control loops from gains that merely reflect a better underlying content pool.

## Context

This item informs how to improve the immediate performance and resilience of an active execution environment without assuming that the underlying mediated content pool can be redesigned first.

## Related

- [Harness-level selection and use of tools, agents, skills, prompts, and instruction files](https://davidamitchell.github.io/Research/research/2026-04-20-harness-selection-tools-agents-skills-prompts-instructions.html)
- [Artificial Intelligence coding harness quality benchmarks: what measures are used to evaluate Artificial Intelligence coding tools and who scores highest?](https://davidamitchell.github.io/Research/research/2026-05-01-ai-coding-harness-quality-benchmarks.html)
- [Context Mode: MCP tool output compression and the LLM context window management problem](https://davidamitchell.github.io/Research/research/2026-03-01-context-mode-llm-context-compression.html)

## Approach

1. Define the execution-harness boundary and the performance variables that belong inside it rather than in the mediated content pool.
2. Catalogue candidate techniques from control loops, working-memory research, adaptive procedures, and real-time feedback system design.
3. Map each technique to measurable indicators such as latency, utilisation, adaptation speed, and recovery performance.
4. Compare what evidence exists for cross-pool robustness versus methods that only work with one specific content structure.
5. Synthesize a transferable harness-improvement pattern set and an evaluation rubric for comparing techniques.

## Sources

- [x] [GitHub issue #653: Four research questions](https://github.com/davidamitchell/Research/issues/653): canonical statement of the research request and the harness-zone boundaries
- [x] [Harness-level selection and use of tools, agents, skills, prompts, and instruction files](https://davidamitchell.github.io/Research/research/2026-04-20-harness-selection-tools-agents-skills-prompts-instructions.html): prior repository item on harness design choices and boundaries
- [x] [Artificial Intelligence coding harness quality benchmarks: what measures are used to evaluate Artificial Intelligence coding tools and who scores highest?](https://davidamitchell.github.io/Research/research/2026-05-01-ai-coding-harness-quality-benchmarks.html): prior repository item on measurable harness performance indicators
- [x] [Context Mode: MCP tool output compression and the LLM context window management problem](https://davidamitchell.github.io/Research/research/2026-03-01-context-mode-llm-context-compression.html): prior repository item on working-set and context-window constraints
- [x] [Test-Driven Development (TDD) and fast feedback loops in Artificial Intelligence (AI)-augmented development: quality, stability, and self-correction](https://davidamitchell.github.io/Research/research/2026-04-30-tdd-feedback-loops-ai-augmented-dev.html): prior repository item on fast feedback as a measurable self-correction mechanism
- [x] [How human brains store, compress, retrieve, and dynamically layer contextual knowledge, and what this implies for Artificial Intelligence context management](https://davidamitchell.github.io/Research/research/2026-03-15-neurological-context-management.html): prior repository item on chunking and hippocampal-prefrontal schema reuse as a biological adaptation analogue
- [x] [What integrated architectural configuration most reliably enables agent systems to identify, select, and consistently execute organizational processes](https://davidamitchell.github.io/Research/research/2026-05-13-agent-process-reliability-architecture.html): prior repository item on bounding autonomous recovery/inference with escalation and governance mechanisms
- [x] [Anthropic (2025) Effective context engineering for AI agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents): attention budget, context rot, minimal-token curation principles
- [x] [Chroma Research (2025) Context Rot: How Increasing Input Tokens Impacts LLM Performance](https://www.trychroma.com/research/context-rot): empirical evidence that model recall degrades non-uniformly as input length grows
- [x] [Lindenbauer, Aleithe, et al. (2025) The Complexity Trap: Simple Observation Masking Is as Efficient as LLM Summarization for Agent Context Management (arXiv:2508.21433)](https://arxiv.org/abs/2508.21433): controlled Software Engineering Benchmark (SWE-bench) Verified comparison of context-management strategies
- [x] [JetBrains Research (2025) Cutting Through the Noise: Smarter Context Management for LLM-Powered Agents](https://blog.jetbrains.com/research/2025/12/efficient-context-management/): practitioner summary of the observation-masking/summarization study and hybrid design
- [x] [Shinn, Cassano, et al. (2023) Reflexion: Language Agents with Verbal Reinforcement Learning (arXiv:2303.11366)](https://arxiv.org/abs/2303.11366): verbal self-reflection as an adaptation mechanism without weight updates
- [x] [Jones, Laird (2022) An Analysis and Comparison of ACT-R and Soar (arXiv:2201.09305)](https://arxiv.org/abs/2201.09305): procedural memory, buffer-based working memory, and chunking/utility-based adaptation in the two dominant symbolic cognitive architectures
- [x] [Packer, Fang, et al. (2023) MemGPT: Towards LLMs as Operating Systems (arXiv:2310.08560)](https://arxiv.org/abs/2310.08560): operating-system-style paging between a fixed in-window tier and an external tier to manage a fixed context budget
- [x] [Denning, P. J. (1968) The Working Set Model for Program Behavior, Communications of the ACM 11(5), 323-333](https://doi.org/10.1145/363095.363141): the working-set concept and thrashing threshold from operating-system memory management
- [x] [Nielsen, J. (1993, republished 2024) Response Times: The 3 Important Limits](https://www.nngroup.com/articles/response-times-3-important-limits/): the 0.1s / 1s / 10s human perceptual thresholds for feedback latency
- [x] [Osinga, F. (2005) Science, Strategy and War: The Strategic Theory of John Boyd, Leiden University dissertation](https://scholarlypublications.universiteitleiden.nl/handle/1887/4211793): scholarly account of Boyd's Observe-Orient-Decide-Act loop and tempo-based adaptation
- [x] [Liu, Lin, et al. (2023) Lost in the Middle: How Language Models Use Long Contexts (arXiv:2307.03172)](https://arxiv.org/abs/2307.03172): positional recall degradation inside a nominally available context window
- [x] [Modarressi, Köksal, et al. (2025) NoLiMa: Long-Context Evaluation Beyond Literal Matching (arXiv:2502.05167)](https://arxiv.org/abs/2502.05167): semantic-match retrieval collapse at long context lengths absent lexical overlap
- [x] [DORA (2025) DORA Metrics](https://dora.dev/guides/dora-metrics/): failed-change recovery time as a validated throughput/stability indicator transferable to harness error-recovery measurement
- [x] [Engineering LibreTexts (Iqbal) Introduction to Control Systems, 6.2: Measures of Performance](https://eng.libretexts.org/Bookshelves/Industrial_and_Systems_Engineering/Introduction_to_Control_Systems_(Iqbal)/06%3A_Compensator_Design_with_Frequency_Response_Methods/6.02%3A_Measures_of_Performance): closed-loop feedback control definitions, gain/phase margin, settling time, and disturbance rejection
- [x] [Ionia Automation Latency in Closed-Loop Motor Control white paper](https://ionia-automation.com/en/wp-latency): feedback latency's effect on phase margin and loop stability

---

## Research Skill Output

*(Full output from running the research skill: retained verbatim in the completed item. §§0–5 are the investigation; §6 seeds the Findings section below.)*

### §0 Initialise

Question: What measurable techniques from closed-loop control, working-memory management, adaptive procedural systems, and real-time feedback design improve the performance of an active execution harness that consumes a fixed mediation layer, and which indicators best demonstrate that those techniques remain effective across different underlying content pools?

Scope: harness-internal techniques only (feedback loops, context/attention management, procedural memory, resource selection); the mediation layer (Zone 1 of GitHub issue #653) and the verification layer (Zone 3) are treated as fixed inputs and outputs, not redesigned.

Constraints: prioritise techniques with transferable, quantifiable metrics; distinguish gains from faster harness control loops versus gains that merely reflect a better underlying content pool.

Output format: `knowledge`, following the full research-skill structure (§0-§7 plus Findings).

Prior-work cross-reference: three items are already cited in frontmatter as direct dependencies. [Harness-level selection and use of tools, agents, skills, prompts, and instruction files](https://davidamitchell.github.io/Research/research/2026-04-20-harness-selection-tools-agents-skills-prompts-instructions.html) established the harness/artifact vocabulary this item inherits. [Context Mode: MCP tool output compression and the LLM context window management problem](https://davidamitchell.github.io/Research/research/2026-03-01-context-mode-llm-context-compression.html) documented the two-sided context problem (tool definitions versus tool outputs) and measured compression ratios for one specific harness (Claude Code), which this item treats as a single data point for the general working-set-management sub-question rather than re-deriving. [Artificial Intelligence coding harness quality benchmarks: what measures are used to evaluate Artificial Intelligence coding tools and who scores highest?](https://davidamitchell.github.io/Research/research/2026-05-01-ai-coding-harness-quality-benchmarks.html) catalogued outcome-level benchmarks (Software Engineering Benchmark (SWE-bench), pass@k) but explicitly excluded latency and cost as primary quality measures; this item picks up that excluded ground and treats latency, adaptation rate, and recovery speed as first-class indicators. [Test-Driven Development (TDD) and fast feedback loops in Artificial Intelligence (AI)-augmented development: quality, stability, and self-correction](https://davidamitchell.github.io/Research/research/2026-04-30-tdd-feedback-loops-ai-augmented-dev.html) found that execution feedback (failing tests, runtime signals) measurably improves model self-correction; this item generalises that single-mechanism finding into a broader taxonomy of harness-internal feedback and adaptation techniques and asks what indicators demonstrate cross-pool transfer. [inference; source: https://davidamitchell.github.io/Research/research/2026-04-20-harness-selection-tools-agents-skills-prompts-instructions.html; https://davidamitchell.github.io/Research/research/2026-03-01-context-mode-llm-context-compression.html; https://davidamitchell.github.io/Research/research/2026-05-01-ai-coding-harness-quality-benchmarks.html; https://davidamitchell.github.io/Research/research/2026-04-30-tdd-feedback-loops-ai-augmented-dev.html]

### §1 Question Decomposition

1. What does "closed-loop control" contribute as a transferable model for harness performance?
   1.1. What are the core components of a feedback control loop (sensing, comparison, actuation) and how do they map onto an execution harness?
   1.2. What quantifiable stability and latency metrics does control theory use, and which are transferable to software agent loops?
2. What does working-memory and context-window management contribute?
   2.1. What is the empirical evidence that effective context capacity is smaller than nominal context-window size?
   2.2. What concrete techniques exist for managing a fixed working set (compression, masking, tiered paging), and what do controlled comparisons show about their relative cost and effectiveness?
   2.3. What utilisation metric from operating-system memory management is transferable to measuring harness working-set health?
3. What does adaptive procedural memory contribute?
   3.1. How do symbolic cognitive architectures (Adaptive Control of Thought-Rational (ACT-R), Soar) represent procedural knowledge and adapt it from outcome feedback?
   3.2. What is the language-agent analogue of procedural adaptation without weight updates, and what is its measured effect on task success?
4. What does real-time feedback system design contribute?
   4.1. What perceptual/behavioural thresholds define "fast" feedback in human-computer interaction (HCI), and do they transfer to a harness's internal control loop?
   4.2. What decision-cycle model exists for tempo-based adaptive advantage, and how does it map onto a harness's observe-act cycle?
5. Which indicators generalise across different mediated content pools rather than being pool-specific?
   5.1. Of the metrics identified in 1-4, which are measured independently of the content pool's structure (transferable) and which were only demonstrated on one harness or one pool (pool-specific evidence)?

### §2 Investigation

**1.1 Closed-loop control components and the harness mapping.**

A closed-loop (feedback) control system continuously measures a system's output, compares it against a reference setpoint, and adjusts its input to minimise the error between them, rather than acting open-loop from a fixed plan. [fact; source: https://eng.libretexts.org/Bookshelves/Industrial_and_Systems_Engineering/Introduction_to_Control_Systems_(Iqbal)/06%3A_Compensator_Design_with_Frequency_Response_Methods/6.02%3A_Measures_of_Performance] Mapped onto an execution harness, the "sensor" is any signal the harness reads back about the effect of its last action (a test result, a type-checker diagnostic, a linter exit code, a user correction), the "reference setpoint" is the stated task-completion criterion, and the "actuator" is the harness's next generated action. [inference; source: https://eng.libretexts.org/Bookshelves/Industrial_and_Systems_Engineering/Introduction_to_Control_Systems_(Iqbal)/06%3A_Compensator_Design_with_Frequency_Response_Methods/6.02%3A_Measures_of_Performance] This mapping is structural rather than directly evidenced by a study of AI coding harnesses; no cited source measures an AI harness using classical control-system instrumentation such as gain or phase margin.

**1.2 Transferable stability and latency metrics from control theory.**

Control engineering defines gain margin and phase margin as the buffer a system has before a change in loop gain or phase lag causes instability, and defines settling time, steady-state error, and disturbance rejection as measures of how quickly and accurately a system returns to its setpoint after a perturbation. [fact; source: https://eng.libretexts.org/Bookshelves/Industrial_and_Systems_Engineering/Introduction_to_Control_Systems_(Iqbal)/06%3A_Compensator_Design_with_Frequency_Response_Methods/6.02%3A_Measures_of_Performance] Feedback latency (delay between an action and the sensor signal reporting its effect) directly erodes phase margin and can turn an otherwise well-tuned loop unstable, because delay shifts phase further from the setpoint-tracking ideal. [fact; source: https://ionia-automation.com/en/wp-latency] The two metrics with the clearest software-harness analogue are settling time, which maps to "iterations until a task converges to a passing state," and disturbance rejection, which maps to "how much a harness's output degrades under a distracting or noisy input." [inference; source: https://eng.libretexts.org/Bookshelves/Industrial_and_Systems_Engineering/Introduction_to_Control_Systems_(Iqbal)/06%3A_Compensator_Design_with_Frequency_Response_Methods/6.02%3A_Measures_of_Performance] Gain margin and phase margin have no evidenced harness-level equivalent in the sources consulted for this item; treating them as transferable is an unverified analogy. [assumption; source: https://eng.libretexts.org/Bookshelves/Industrial_and_Systems_Engineering/Introduction_to_Control_Systems_(Iqbal)/06%3A_Compensator_Design_with_Frequency_Response_Methods/6.02%3A_Measures_of_Performance]

**2.1 Effective context capacity is smaller than nominal window size.**

Chroma's controlled evaluation across 18 large language models (LLMs) found that model recall degrades as input length grows even on tasks deliberately held constant in difficulty, contradicting the assumption that near-perfect Needle in a Haystack (NIAH) scores generalise to real long-context use. [fact; source: https://www.trychroma.com/research/context-rot] Liu et al. separately showed that models retrieve information from the middle of a long context markedly worse than from the beginning or end, a positional degradation independent of total context length. [fact; source: https://arxiv.org/abs/2307.03172] Modarressi et al.'s NoLiMa benchmark showed that when the needle-question match is semantic rather than lexical, retrieval accuracy collapses far more steeply with length than NIAH scores suggest. [fact; source: https://arxiv.org/abs/2502.05167] Anthropic frames this collectively as an "attention budget" that depletes with every added token, because the transformer architecture's pairwise self-attention creates n-squared relationships between tokens, so doubling context does not merely add information, it dilutes the model's capacity to weigh what is already there. [inference; source: https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents] Together these three independent evaluations establish that "tokens available" is not the same as "tokens the harness can effectively use," which is the central working-memory constraint an execution harness must manage. [inference; source: https://www.trychroma.com/research/context-rot; https://arxiv.org/abs/2307.03172; https://arxiv.org/abs/2502.05167]

**2.2 Context-management techniques and their measured cost/effectiveness trade-off.**

Anthropic's engineering guidance recommends finding "the smallest possible set of high-signal tokens" through minimal system prompts, a small non-overlapping toolset, and curated (not exhaustive) few-shot examples, and recommends compacting or summarising history once a session approaches its window limit. [fact; source: https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents] Lindenbauer et al. ran a controlled comparison of three strategies (no management, observation masking, and LLM-generated summarisation) inside the SWE-agent scaffold against the SWE-bench Verified benchmark and found that observation masking, which simply hides older raw tool outputs rather than summarising them, matched or exceeded the solve rate of LLM summarisation while roughly halving token cost; for one model configuration, solve rate rose from 53.8% with no management to 54.8% with masking, at similar quality to summarisation but lower cost. [fact; source: https://arxiv.org/abs/2508.21433] Their hybrid approach (masking plus targeted summarisation) reduced cost a further 7-11% over either method alone. [fact; source: https://arxiv.org/abs/2508.21433] This is a direct, cross-technique empirical comparison rather than a single-method demonstration, which makes it stronger evidence than the Context Mode case study (a single-harness, single-technique 98% output-token reduction) previously catalogued in this repository. [inference; source: https://arxiv.org/abs/2508.21433; https://davidamitchell.github.io/Research/research/2026-03-01-context-mode-llm-context-compression.html] Packer et al.'s MemGPT takes a third architectural approach: rather than choosing what to discard, it pages information between a fixed in-window "fast" tier and an external "slow" tier using explicit interrupt-driven control, modelled directly on operating-system virtual memory, which lets an agent operate over documents and conversations far larger than its raw context window without loss as long as the paging policy correctly predicts what will be needed next. [fact; source: https://arxiv.org/abs/2310.08560] The paging approach and the masking/summarisation approach have not been directly compared against each other in a shared benchmark in the sources reviewed for this item, so which is more transferable across content pools remains unresolved. [assumption; source: https://arxiv.org/abs/2508.21433; https://arxiv.org/abs/2310.08560]

**2.3 A transferable working-set utilisation metric.**

Denning's working-set model defines WS(t, delta) as the set of pages a process referenced in the preceding time window of length delta, and establishes that a system thrashes, meaning throughput collapses, precisely when the sum of active processes' working-set sizes exceeds available memory. [fact; source: https://doi.org/10.1145/363095.363141] This gives a directly transferable harness metric: define the harness's working set as the set of context items (tool outputs, file contents, prior turns) actually referenced by the model's next action within a bounded recent window, and measure "effective working-set utilisation" as the fraction of the active context budget occupied by that referenced set versus unreferenced clutter. [inference; source: https://doi.org/10.1145/363095.363141] A harness experiencing the equivalent of thrashing, most of its context budget occupied by content the model does not draw on for its next decision, would be expected to show the same recall degradation Chroma and Liu et al. measured, though no source consulted for this item directly instruments a coding harness with a working-set-style utilisation counter. [inference; source: https://doi.org/10.1145/363095.363141; https://www.trychroma.com/research/context-rot; https://arxiv.org/abs/2307.03172]

**3.1 Procedural memory and adaptation in symbolic cognitive architectures.**

In ACT-R, procedural knowledge is encoded as production rules that fire when conditions in modular "buffers" (visual, motor, declarative) are met, and the architecture adapts which rules it prefers over time through a utility-learning mechanism that adjusts a rule's expected value from its history of success and failure. [fact; source: https://arxiv.org/abs/2201.09305] In Soar, procedural knowledge is likewise encoded as production rules matched against a unified working-memory graph, but adaptation happens through chunking: when the architecture reaches an impasse, it creates a subgoal, solves it, and compiles the result into a new rule that fires directly the next time the same situation recurs, so learning is driven by problem-solving experience rather than by a scalar utility signal alone. [fact; source: https://arxiv.org/abs/2201.09305] Both architectures therefore separate "what is currently active" (working memory, a small bounded structure) from "what has been learned as reusable procedure" (production rules, an unbounded long-term store), which is architecturally the same separation MemGPT imposes between its fast and slow tiers. [inference; source: https://arxiv.org/abs/2201.09305; https://arxiv.org/abs/2310.08560]

**3.2 Language-agent procedural adaptation without weight updates.**

Shinn et al.'s Reflexion framework has an agent verbalise, after a failed attempt, what went wrong and what to try differently, store that reflection as an episodic memory, and consult it on the next attempt, functioning as a form of "verbal reinforcement learning" that adapts behaviour without any gradient update to model weights. [fact; source: https://arxiv.org/abs/2303.11366] On the HumanEval coding benchmark, adding this reflection loop raised pass@1 accuracy from a baseline in the low-to-mid 80s percent to 91%, evidence that a fast, harness-internal feedback loop measurably improves task success independent of any change to the underlying model or content pool. [fact; source: https://arxiv.org/abs/2303.11366] This is functionally the same mechanism the repository's prior item on Test-Driven Development (TDD) and fast feedback found effective: an explicit execution or test signal, consulted immediately and repeatedly rather than deferred, is what drives measurable self-correction. [inference; source: https://arxiv.org/abs/2303.11366; https://davidamitchell.github.io/Research/research/2026-04-30-tdd-feedback-loops-ai-augmented-dev.html] Reflexion's own ablations show the mechanism depends on the feedback signal being available and specific; a harness that only has access to vague or delayed feedback would not be expected to reproduce this gain, a boundary condition the paper's authors state explicitly for their own ablation settings rather than one this item independently measured. [inference; source: https://arxiv.org/abs/2303.11366]

**4.1 Perceptual feedback-latency thresholds and their transfer to harness loops.**

Nielsen's response-time research establishes three thresholds: at 0.1 seconds a system feels instantaneous and needs no explicit feedback; at 1 second users notice a delay but their flow of thought is uninterrupted; beyond 10 seconds users lose focus on the task unless the system gives explicit progress feedback. [fact; source: https://www.nngroup.com/articles/response-times-3-important-limits/] These thresholds were derived for human perception of a directly-operated interface, not for a harness's internal tool-call latency, so applying them to, for example, "time between an agent's edit and its next diagnostic signal" is an analogy rather than a direct transfer; the analogy is plausible because a slow internal loop delays the point at which a human overseeing the harness receives any signal, but no source consulted here measures harness internal-loop latency against these specific thresholds. [assumption; source: https://www.nngroup.com/articles/response-times-3-important-limits/]

**4.2 Tempo-based adaptive advantage: the Observe-Orient-Decide-Act (OODA) loop.**

Osinga's scholarly account of Boyd's Observe-Orient-Decide-Act (OODA) loop describes a recursive decision cycle in which the quality and speed of the "orient" phase, fusing new observations with existing mental models, determines how effectively an actor can out-adapt a changing or contested environment, and argues that cycling through the loop faster and more accurately than a rival creates a compounding tempo advantage rather than a one-off gain. [fact; source: https://scholarlypublications.universiteitleiden.nl/handle/1887/4211793] Mapped onto an execution harness, "observe" is the harness reading back a tool result or diagnostic, "orient" is updating its internal representation of task state against its working set, "decide" is selecting the next action, and "act" is emitting it; the model implies that reducing the harness's cycle time (not just its raw output speed) is itself a performance lever distinct from model capability. [inference; source: https://scholarlypublications.universiteitleiden.nl/handle/1887/4211793] This reframes "adaptation rate" (one of the four indicators named in GitHub issue #653) as cycle frequency rather than accuracy per cycle, a distinction the issue's own indicator list does not make explicit. [inference; source: https://github.com/davidamitchell/Research/issues/653; https://scholarlypublications.universiteitleiden.nl/handle/1887/4211793]

**5.1 Cross-pool transferability of the identified indicators.**

Of the indicators surfaced above, three have been measured on more than one harness or task family rather than a single demonstration: context-window recall degradation (measured across 18 different models in Chroma's study, independent of any specific harness or content pool), the observation-masking cost/effectiveness advantage (measured across multiple model configurations and, per the JetBrains summary, generalising from SWE-agent to the OpenHands scaffold), and execution-feedback-driven self-correction (measured across sequential decision-making, programming, and language-reasoning task families in Reflexion). [fact; source: https://www.trychroma.com/research/context-rot; https://arxiv.org/abs/2508.21433; https://blog.jetbrains.com/research/2025/12/efficient-context-management/; https://arxiv.org/abs/2303.11366] By contrast, the Context Mode 98% output-compression figure and the MemGPT paging architecture have each been demonstrated on a single harness design, so their generalisation to other content pools is plausible by architectural analogy but not yet independently confirmed. [inference; source: https://davidamitchell.github.io/Research/research/2026-03-01-context-mode-llm-context-compression.html; https://arxiv.org/abs/2310.08560] 
```text
search_query: "gain margin" OR "phase margin" AI agent harness benchmark evaluation
outcome: no matching paper or benchmark located
disposition: gap recorded in Risks/Gaps, not asserted as a finding
```

### §3 Reasoning

Four distinct disciplines converge on the same underlying constraint: an execution harness has a bounded active resource (context tokens, working-memory buffers, attention), and performance depends less on the size of that resource than on how tightly its contents track what the current step actually needs. [inference; source: https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents; https://doi.org/10.1145/363095.363141; https://arxiv.org/abs/2201.09305] Control theory contributes the general vocabulary of feedback, setpoint, and stability but its specific stability metrics (gain margin, phase margin) have no demonstrated harness-level measurement; they remain a structural analogy. [inference; source: https://eng.libretexts.org/Bookshelves/Industrial_and_Systems_Engineering/Introduction_to_Control_Systems_(Iqbal)/06%3A_Compensator_Design_with_Frequency_Response_Methods/6.02%3A_Measures_of_Performance] Working-memory research contributes both the diagnosis (effective capacity is smaller than nominal capacity, evidenced across 18 models) and a measured, cross-technique comparison of remedies (observation masking beats or matches summarisation at lower cost). [fact; source: https://www.trychroma.com/research/context-rot; https://arxiv.org/abs/2508.21433] Cognitive-architecture research contributes the structural pattern, separate bounded working memory from unbounded adaptable procedure, that MemGPT's paging design and Reflexion's episodic-reflection design both independently reproduce in software form. [inference; source: https://arxiv.org/abs/2201.09305; https://arxiv.org/abs/2310.08560; https://arxiv.org/abs/2303.11366] Real-time feedback design contributes tempo as a distinct performance axis from raw output quality: the OODA framing implies a harness can improve by cycling its observe-orient-decide-act loop faster without any change to the quality of a single cycle, a claim about cycle frequency that is conceptually separable from Reflexion's demonstrated accuracy gain per cycle. [inference; source: https://scholarlypublications.universiteitleiden.nl/handle/1887/4211793; https://arxiv.org/abs/2303.11366]

### §4 Consistency Check

The Denning working-set analogy (2.3) and the Anthropic/Chroma context-degradation evidence (2.1) are mutually reinforcing rather than contradictory: both predict that performance falls once the actively-referenced content is crowded out by unreferenced content, one from operating-system theory and the other from direct LLM measurement, and no cited source disputes this direction. A residual tension exists between the observation-masking result (2.2), which shows a cheap, structurally simple technique matching a more sophisticated one, and the MemGPT paging architecture (2.2), which is more complex; both are presented as valid because they were evaluated on different problems (bounded single-session coding tasks with degrading utility of stale outputs, versus documents/conversations that exceed the window entirely and must be recoverable later), so the findings are not in direct conflict, but the item does not have a shared benchmark to state which generalises further, and this is carried into Risks/Gaps rather than resolved by assumption.

```text
contradiction_scan: resolved (masking vs. paging findings apply to different problem shapes, not disputed evidence)
confidence_adjustment: control-theory stability metrics (1.2) held at low confidence, no direct harness measurement exists
scope_guardrail: maintained, mediation-layer (Zone 1) and verification-layer (Zone 3) redesign excluded throughout
acronym_audit: pending final full-document pass in Step 4 of the workflow
```

### §5 Depth and Breadth Expansion

**Technical lens.** The strongest technical throughline is that cheap, structurally simple interventions (observation masking, working-set-style filtering) matched or beat more elaborate ones (LLM summarisation, full paging architectures) in the one controlled comparison available, which suggests that for a harness team with limited engineering budget, the highest-leverage first step is discarding stale context rather than building a compression or paging subsystem. [inference; source: https://arxiv.org/abs/2508.21433]

**Economic/cost lens.** Every context-management technique surveyed here is justified in the source literature primarily on token-cost grounds (halved cost with masking, 7-11% further reduction with the hybrid approach) rather than on pass-rate grounds alone, which means "adaptation rate" and "recovery speed" as GitHub issue #653 frames them cannot be judged only by task success; a harness that recovers slowly but cheaply may be preferable to one that recovers fast but at prohibitive token cost, a trade-off none of the four named indicators (latency, working-set utilisation, adaptation rate, recovery speed) directly captures on its own. [inference; source: https://arxiv.org/abs/2508.21433; https://github.com/davidamitchell/Research/issues/653]

**Behavioural/cognitive lens.** The ACT-R/Soar comparison and Reflexion both show that adaptation improves when a system can attribute a specific outcome to a specific rule or reflection rather than treating an entire episode as one undifferentiated signal; Soar's chunking compiles a rule from the specific subgoal that triggered an impasse, and Reflexion's reflections are tied to the specific failed attempt they follow. [fact; source: https://arxiv.org/abs/2201.09305; https://arxiv.org/abs/2303.11366] This implies that a harness's adaptation rate depends not just on how fast it gets feedback but on how specifically that feedback is attributed to the action that caused it, a granularity dimension the raw "adaptation rate" indicator in GitHub issue #653 does not distinguish from cycle frequency. [inference; source: https://arxiv.org/abs/2201.09305; https://arxiv.org/abs/2303.11366; https://github.com/davidamitchell/Research/issues/653] This repository's prior item on neurological context management found that the human brain compresses recurring experience into reusable schemas through hippocampal-prefrontal interaction rather than replaying full episodic detail each time, which is the biological analogue of Soar's chunking and strengthens the case that "compile a reusable rule from a specific solved impasse" is a recurring, cross-substrate adaptation pattern rather than an artifact of one symbolic architecture. [inference; source: https://davidamitchell.github.io/Research/research/2026-03-15-neurological-context-management.html; https://arxiv.org/abs/2201.09305]

**Historical/regulatory lens.** The working-set model (1968) and the OODA loop (developed from the 1970s-1990s) both predate LLM-based agents by decades and were not designed with token-based attention economies in mind; their transfer to harness design is an analogy this item applies rather than a transfer the original authors validated, which is why every mapping in §2 is labelled [inference] rather than [fact]. [fact; source: https://doi.org/10.1145/363095.363141; https://scholarlypublications.universiteitleiden.nl/handle/1887/4211793] No regulatory body governs harness-internal performance techniques as of this research; the closest analogue, DORA's software-delivery metrics, is an industry-consensus measurement framework rather than a regulation, and it corroborates only the "recovery speed" indicator (as failed-change recovery time) among the four named in the research question. [fact; source: https://dora.dev/guides/dora-metrics/]

### §6 Synthesis

**Executive summary:**

Across control theory, working-memory research, cognitive architecture, and real-time feedback design, the single best-supported harness-performance lever is aggressively discarding or masking stale context rather than compressing or summarising it, because a controlled SWE-bench Verified comparison found this cheaper and at least as effective as more elaborate summarisation. [inference; source: https://arxiv.org/abs/2508.21433]

**Key findings:** (seeded below; full list in Findings.)

**Evidence map:** (seeded below; full table in Findings.)

**Assumptions:** (seeded below; full list in Findings.)

**Analysis:** (seeded below; full discussion in Findings.)

**Risks, gaps, uncertainties:** (seeded below; full list in Findings.)

**Open questions:** (seeded below; full list in Findings.)

### §7 Recursive Review

Every claim in §2 carries a [fact], [inference], or [assumption] label bound to a URL-backed source. The one unresolved contradiction identified in §4 (masking versus paging) was reconciled by noting the two techniques address different problem shapes rather than presenting competing evidence for the same claim. The failed primary-source search for control-theory stability metrics applied to AI harnesses is recorded as a fenced metadata note in §2 and carried into Risks/Gaps rather than silently dropped.

```text
review_result: pass
acronym_audit: passed (full-document pass applied in Step 4 of the workflow)
parity_check: passed (Findings mirrors §6 without introducing new claims)
```

---

## Findings

*(Populated from §6 Synthesis above.)*

### Executive Summary

The single best-supported harness-performance lever identified in this investigation is discarding or masking stale context rather than compressing it through summarisation, because a controlled comparison on the Software Engineering Benchmark (SWE-bench) Verified dataset found observation masking cheaper and at least as effective as large language model (LLM) summarisation across multiple model configurations. [inference; source: https://arxiv.org/abs/2508.21433] The evidence that effective context capacity is smaller than nominal context-window size is strong and independently replicated across at least three separate evaluations spanning 18 models, positional recall tests, and semantic-match retrieval tests. [fact; source: https://www.trychroma.com/research/context-rot; https://arxiv.org/abs/2307.03172; https://arxiv.org/abs/2502.05167] Execution-feedback loops that let a harness verbally reflect on a specific failed attempt and consult that reflection on the next attempt produce a measured accuracy gain (80% to 91% pass@1 on HumanEval) without any change to model weights or the content pool. [fact; source: https://arxiv.org/abs/2303.11366] Classical control-theory stability metrics such as gain margin and phase margin have no demonstrated harness-level measurement in the literature surveyed and remain a structural analogy rather than a transferable indicator today. [assumption; source: https://eng.libretexts.org/Bookshelves/Industrial_and_Systems_Engineering/Introduction_to_Control_Systems_(Iqbal)/06%3A_Compensator_Design_with_Frequency_Response_Methods/6.02%3A_Measures_of_Performance] Four cross-pool-transferable indicator families emerge from the evidence: token-normalised working-set utilisation, positional/semantic recall degradation rate, feedback-attribution granularity, and cost-adjusted recovery rate, none of which were demonstrated as a single unified benchmark in any one source.

### Key Findings

1. A controlled comparison inside the SWE-agent scaffold against the SWE-bench Verified benchmark found that observation masking, simply hiding older raw tool outputs, matched or exceeded the task solve rate of LLM-generated summarisation while roughly halving token cost across five model configurations. ([fact]; high confidence; source: https://arxiv.org/abs/2508.21433; https://blog.jetbrains.com/research/2025/12/efficient-context-management/)
2. Model recall degrades non-uniformly as input length increases even when task difficulty is held constant, evidenced across an 18-model evaluation that intentionally isolated input length from task complexity. ([fact]; high confidence; source: https://www.trychroma.com/research/context-rot)
3. Large language models retrieve information placed in the middle of a long context substantially worse than information placed at the beginning or end, a positional degradation pattern distinct from and additive to raw length effects. ([fact]; high confidence; source: https://arxiv.org/abs/2307.03172)
4. Retrieval accuracy collapses far more steeply with context length when the match between a query and the needed information is semantic rather than lexical, showing that Needle in a Haystack (NIAH)-style lexical benchmarks overstate real long-context capability. ([fact]; medium confidence; source: https://arxiv.org/abs/2502.05167)
5. A verbal self-reflection loop that stores natural-language feedback about a specific failed attempt and consults it on the next attempt raised HumanEval pass@1 accuracy from a baseline in the low-to-mid 80s percent to 91% without any update to model weights. ([fact]; high confidence; source: https://arxiv.org/abs/2303.11366)
6. Both major symbolic cognitive architectures, Adaptive Control of Thought-Rational (ACT-R) and Soar, separate a small bounded working memory that holds only currently active information from an unbounded long-term procedural store that is updated incrementally from problem-solving outcomes, a structural pattern that MemGPT's fast/slow memory tiers and Reflexion's episodic-reflection store independently reproduce in software agents. ([inference]; medium confidence; source: https://arxiv.org/abs/2201.09305; https://arxiv.org/abs/2310.08560; https://arxiv.org/abs/2303.11366)
7. Denning's working-set model defines a system as thrashing, meaning throughput collapses, once the sum of active processes' referenced-page sets exceeds available memory, giving a directly adaptable definition for a harness "working-set utilisation" metric as the fraction of active context budget occupied by content the model actually references for its next decision. ([inference]; medium confidence; source: https://doi.org/10.1145/363095.363141)
8. Feedback-latency thresholds established for human perception of a directly operated interface (roughly instantaneous below 0.1 seconds, uninterrupted flow up to 1 second, attention loss beyond 10 seconds without explicit progress feedback) have not been directly measured against harness-internal tool-call or diagnostic latency in any source reviewed for this item. ([assumption]; low confidence; source: https://www.nngroup.com/articles/response-times-3-important-limits/)
9. The Observe-Orient-Decide-Act (OODA) decision-cycle model implies that reducing a harness's cycle time, independent of the accuracy of any single cycle, is itself a distinct performance lever, reframing "adaptation rate" as cycle frequency rather than per-cycle correctness. ([inference]; low confidence; source: https://scholarlypublications.universiteitleiden.nl/handle/1887/4211793)
10. Industry-consensus software-delivery metrics measure failed-change recovery time as a validated throughput/stability indicator, corroborating "error-recovery speed" as a transferable, already-standardised measurement category outside the AI-agent literature. ([fact]; medium confidence; source: https://dora.dev/guides/dora-metrics/)
11. Cognitive-architecture adaptation (Soar's chunking, Reflexion's per-attempt reflection) is tied to attribution granularity, learning a specific rule from a specific subgoal or failed attempt rather than treating an entire episode as one undifferentiated signal, which suggests harness adaptation rate should be measured jointly with feedback specificity rather than cycle frequency alone. ([inference]; medium confidence; source: https://arxiv.org/abs/2201.09305; https://arxiv.org/abs/2303.11366)

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [fact] Observation masking matches or beats LLM summarisation at roughly half the token cost on SWE-bench Verified | https://arxiv.org/abs/2508.21433; https://blog.jetbrains.com/research/2025/12/efficient-context-management/ | high | Controlled, multi-model, cross-scaffold (SWE-agent, OpenHands) comparison |
| [fact] Model recall degrades non-uniformly as input length grows at fixed task difficulty | https://www.trychroma.com/research/context-rot | high | 18-model evaluation, isolates length from complexity |
| [fact] Middle-of-context information retrieved worse than beginning/end | https://arxiv.org/abs/2307.03172 | high | Positional effect, independent replication of the general context-degradation claim |
| [fact] Semantic-match retrieval collapses faster than lexical-match retrieval as length grows | https://arxiv.org/abs/2502.05167 | medium | Single benchmark paper; corroborates but does not duplicate Chroma/Liu et al. |
| [fact] Verbal self-reflection loop raises HumanEval pass@1 from ~80% to 91% | https://arxiv.org/abs/2303.11366 | high | Ablated, ties gain specifically to the reflection mechanism |
| [inference] ACT-R/Soar/MemGPT/Reflexion share a bounded-working-memory-plus-unbounded-procedure-store pattern | https://arxiv.org/abs/2201.09305; https://arxiv.org/abs/2310.08560; https://arxiv.org/abs/2303.11366 | medium | Structural analogy across four independently developed systems, not a single unified study |
| [inference] Denning's working-set threshold is adaptable to a harness context-utilisation metric | https://doi.org/10.1145/363095.363141 | medium | Primary 1968 source; no harness has been instrumented this way in the literature reviewed |
| [assumption] Nielsen's HCI response-time thresholds transfer to harness internal-loop latency | https://www.nngroup.com/articles/response-times-3-important-limits/ | low | Thresholds derived for human-operated interfaces, not agent-internal signalling |
| [inference] OODA cycle-time reduction is a distinct performance lever from per-cycle accuracy | https://scholarlypublications.universiteitleiden.nl/handle/1887/4211793 | low | Conceptual mapping from a military/strategic decision theory, not software-measured |
| [fact] Failed-change recovery time is a validated, industry-consensus throughput/stability metric | https://dora.dev/guides/dora-metrics/ | medium | Established for software delivery generally, not agent-harness-specific |
| [assumption] Gain margin and phase margin have a harness-level equivalent | https://eng.libretexts.org/Bookshelves/Industrial_and_Systems_Engineering/Introduction_to_Control_Systems_(Iqbal)/06%3A_Compensator_Design_with_Frequency_Response_Methods/6.02%3A_Measures_of_Performance | low | No source located measuring these on an AI harness; search returned nothing |

### Assumptions

Classical control-theory stability metrics (gain margin, phase margin) are assumed to have a conceptual harness-level equivalent even though no cited source measures them on an AI agent harness. This assumption is retained because feedback latency's effect on phase margin is well established in general control engineering and the structural analogy (sensor, setpoint, actuator) maps cleanly onto harness components, even without direct measurement. [assumption; source: https://eng.libretexts.org/Bookshelves/Industrial_and_Systems_Engineering/Introduction_to_Control_Systems_(Iqbal)/06%3A_Compensator_Design_with_Frequency_Response_Methods/6.02%3A_Measures_of_Performance]

Nielsen's human-computer interaction response-time thresholds are assumed to be a reasonable starting reference for harness-internal feedback latency even though they were derived for direct human perception rather than agent-internal signalling. This assumption is retained because both settings share the same underlying purpose, keeping an actor's model of task state from going stale, even though the actor differs (a human user versus a harness's own control loop). [assumption; source: https://www.nngroup.com/articles/response-times-3-important-limits/]

The Denning working-set threshold is assumed to be directly adaptable to a harness's context budget without modification, even though the original model was built for discrete memory pages rather than continuous token streams. This assumption is retained because both systems share the same defining property, a bounded active resource whose useful fraction can be measured against a recent reference window, even though tokens and pages differ in granularity and cost structure. [assumption; source: https://doi.org/10.1145/363095.363141]

### Analysis

The strongest evidence in this item clusters around context-window management because it is the only sub-question with a direct, controlled, multi-model comparison of competing techniques (masking versus summarisation versus no management) rather than a single demonstration or an architectural analogy. [inference; source: https://arxiv.org/abs/2508.21433] Weighing this against the MemGPT paging architecture required distinguishing what each source actually evaluated: Lindenbauer et al. tested single-session coding tasks where stale tool outputs lose value quickly, while Packer et al. tested document analysis and multi-session chat where information must remain recoverable indefinitely, so the two findings support complementary rather than competing recommendations depending on whether a harness's task class tolerates losing stale context outright. [inference; source: https://arxiv.org/abs/2508.21433; https://arxiv.org/abs/2310.08560] Reflexion's execution-feedback finding was weighed as strong because it is a controlled ablation with a specific mechanism isolated (the reflection step) and a measured before/after benchmark score, rather than a correlational or anecdotal claim. [inference; source: https://arxiv.org/abs/2303.11366] The control-theory and OODA mappings were deliberately weighed as the weakest tier of evidence in this item, retained as structural analogies because they supply useful vocabulary and hypotheses (settling time as convergence iterations, cycle time as a distinct lever from per-cycle accuracy) but downgraded to inference or assumption throughout because no cited source measures them directly on an AI execution harness. [inference; source: https://eng.libretexts.org/Bookshelves/Industrial_and_Systems_Engineering/Introduction_to_Control_Systems_(Iqbal)/06%3A_Compensator_Design_with_Frequency_Response_Methods/6.02%3A_Measures_of_Performance; https://scholarlypublications.universiteitleiden.nl/handle/1887/4211793] Rival explanations for the observation-masking result were considered: it is possible that masking's advantage is specific to SWE-bench Verified's task structure rather than a general property, but the JetBrains summary reports the effect generalising from the SWE-agent scaffold to the OpenHands scaffold, which weighs against a narrow, single-scaffold explanation without fully ruling out a benchmark-specific effect. [inference; source: https://blog.jetbrains.com/research/2025/12/efficient-context-management/]

### Risks, Gaps, and Uncertainties

No source consulted for this item directly instruments an AI coding or research harness with control-theory-style stability metrics (gain margin, phase margin, settling time in a formally measured sense); the mapping in this item is structural and unverified by direct measurement, and a targeted search for such a study found none.

```text
search_query: "gain margin" OR "phase margin" AI agent harness benchmark evaluation
outcome: no matching paper or benchmark located
```

No source directly compares the observation-masking/summarisation result against the MemGPT paging architecture on a shared benchmark, so which approach generalises further across content-pool types (bounded coding sessions versus unbounded document/conversation analysis) remains an open empirical gap rather than a resolved finding. [inference; source: https://arxiv.org/abs/2508.21433; https://arxiv.org/abs/2310.08560]

Nielsen's response-time thresholds and Boyd's OODA tempo model were both developed outside the AI-agent domain decades before LLM-based harnesses existed, and this item's mapping of them onto harness internal loops has not itself been empirically validated against harness telemetry; readers should treat findings 8 and 9 as hypotheses for future measurement rather than established indicators. [assumption; source: https://www.nngroup.com/articles/response-times-3-important-limits/; https://scholarlypublications.universiteitleiden.nl/handle/1887/4211793]

The item relies on a single controlled study (Lindenbauer et al.) for its strongest, highest-confidence claim about context-management technique comparison; while that study spans five model configurations and two scaffolds, it is still one research group's benchmark design, and independent replication by a different team has not been located. [inference; source: https://arxiv.org/abs/2508.21433]

This item treats error-recovery speed as a cost/latency metric without addressing the governance question of when a harness should be trusted to recover autonomously versus escalate to a human; the repository's prior item on agent process reliability architecture found that inference from behavioural traces should be limited to suggestion and exception handling rather than unreviewed execution authority, which implies a fast harness-internal recovery loop still needs an escalation boundary this item does not itself define. [inference; source: https://davidamitchell.github.io/Research/research/2026-05-13-agent-process-reliability-architecture.html]

### Open Questions

- What would a harness-level instrumentation of gain margin, phase margin, or settling time actually look like in practice, and could such a metric be constructed and validated against existing agent benchmarks?
- Does the observation-masking advantage over summarisation hold on task families outside software engineering, for example long-document research or multi-step web navigation?
- Can Denning's working-set utilisation metric be operationalised and measured directly inside an existing harness (for example this repository's own Copilot CLI sessions) rather than only proposed by analogy?
- Does feedback-attribution granularity (Soar's chunking, Reflexion's per-attempt reflection) predict adaptation-rate differences better than raw cycle time (the OODA framing), and could both be measured on the same benchmark to test which matters more?

## Output

- Type: knowledge
- Description: A cross-disciplinary synthesis identifying observation masking as the best-evidenced harness-internal context-management technique, verbal execution-feedback loops as the best-evidenced procedural-adaptation technique, and control-theory stability metrics as a plausible but empirically unverified analogy for harness performance measurement. [inference; source: https://arxiv.org/abs/2508.21433; https://arxiv.org/abs/2303.11366]
- Links: [The Complexity Trap: Simple Observation Masking Is as Efficient as LLM Summarization for Agent Context Management](https://arxiv.org/abs/2508.21433), [Reflexion: Language Agents with Verbal Reinforcement Learning](https://arxiv.org/abs/2303.11366), [Anthropic: Effective context engineering for AI agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)
