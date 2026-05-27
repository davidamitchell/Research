---
review_count: 2
title: "Agentic Tool-Feedback Loops and Explanatory Reach: Does Wrapping an LLM in a Perception-Action Cycle Introduce Genuine Understanding or Just Delay Failure?"
added: 2026-05-18T19:40:00+00:00
status: completed
priority: high
blocks:
  - 2026-05-18-rq4-2-adversarial-error-propagation
themes: [agentic-ai, llm-reasoning, benchmarks-eval, ai-architecture]
started: 2026-05-19T11:32:05+00:00
completed: 2026-05-19T11:49:46+00:00
output: [knowledge]
cites:
  - 2026-05-18-rq2-4-causal-hierarchy-formal-limits
  - 2026-05-18-rq3-1-llm-statistical-vs-causal
  - 2026-05-18-rq3-2-stochastic-parrot-ood
  - 2026-05-18-rq3-3-cot-counterfactual-limits
related:
  - 2026-05-18-agentic-explainability-vs-traditional
  - 2026-05-18-rq4-2-adversarial-error-propagation
  - 2026-05-18-rq4-3-ood-generalization-agentic
superseded_by: ~
supersedes: ~
item_type: primary
confidence: medium
versions:
  - version: "1.0"
    sha: e0edcc98af0e15b0d3ad4f28bd48779f9477db28
    changed: 2026-05-19
    progress: progress/2026-05-19-rq4-1-agentic-loop-explanatory-reach.md
    summary: "Initial completion"
---

# Agentic Tool-Feedback Loops and Explanatory Reach: Does Wrapping an LLM in a Perception-Action Cycle Introduce Genuine Understanding or Just Delay Failure?

## Research Question

When a Large Language Model (LLM) is wrapped in an agentic loop, meaning a repeated perception, strategy-selection, tool-action, and verification cycle, does the outer loop introduce true explanatory reach, or does it mainly delay failure when the system faces novel inputs?

## Scope

**In scope:**
- The Reason and Act (ReAct) paradigm as a representative loop architecture
- Error cascade analysis, how one incorrect strategic step in a multi-step loop propagates to later tool calls and checks
- State-space search versus epistemic discovery as competing descriptions of what tool-feedback loops add
- Whether tool access and feedback lift the composite system toward Level 2 intervention reasoning or Level 3 counterfactual reasoning on Pearl's hierarchy

**Out of scope:**
- Specific framework comparisons across LangChain, AutoGen, CrewAI, or similar orchestration libraries
- Multi-agent coordination

**Constraints:** Must build on Phase 3 findings, especially Research Questions 3.1, 3.2, and 3.3, and must evaluate explanatory reach using the formal causal-hierarchy frame from Research Question 2.4.

## Context

Research Question 3.1 concluded that standard LLM training optimises prediction over observed text rather than invariant causal structure. [fact; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq3-1-llm-statistical-vs-causal.md]

Research Question 3.3 concluded that chain-of-thought (CoT) prompting lengthens the inference trace and can improve search, but does not by itself cross Pearl's causal hierarchy. [fact; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq3-3-cot-counterfactual-limits.md]

This item asks whether adding tools, feedback, and retries changes that conclusion, or whether the composite system still operates as a Level 1 pattern-matcher with a larger action surface and more opportunities to recover from, or compound, earlier mistakes. [inference; source: https://arxiv.org/abs/2210.03629; https://arxiv.org/abs/2303.11366; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq2-4-causal-hierarchy-formal-limits.md]

## Approach

1. Formally characterise the tool-feedback loop: perception, strategy selection, tool action, verification, and retry.
2. Apply the causal-hierarchy test: identify whether any component adds intervention or counterfactual semantics that the base model lacks.
3. Model error cascade: if the model makes a Level 1 strategic error early, trace how that conditions later tool use and verification.
4. Survey empirical evidence from ReAct-style systems, reflection loops, tree search, and planning benchmarks.
5. Classify the composite system: genuine explanatory reach, tool-assisted search, or delayed failure.

## Sources

- [x] [Yao et al. (2023) ReAct: Synergizing Reasoning and Acting in Language Models](https://arxiv.org/abs/2210.03629) - primary source for the canonical ReAct loop and its benchmark gains.
- [x] [ReAct Project](https://react-lm.github.io/) - accessible project page with loop description, success examples, and an explicit failure example.
- [x] [Shinn et al. (2023) Reflexion: Language Agents with Verbal Reinforcement Learning](https://arxiv.org/abs/2303.11366) - primary source for feedback-memory loops across repeated trials.
- [x] [Mialon et al. (2023) Augmented Language Models: a Survey](https://arxiv.org/abs/2302.07842) - survey source on tool-augmented models retaining the missing-token training objective while adding external modules.
- [x] [Valmeekam et al. (2023) Large Language Models Still Can't Plan](https://arxiv.org/abs/2206.10498) - planning benchmark evidence that agentic wrapping does not remove core planning limits.
- [x] [Yao et al. (2023) Tree of Thoughts: Deliberate Problem Solving with Large Language Models](https://openreview.net/forum?id=5Xc1ecxO1h) - primary source for branching, self-evaluation, and backtracking as a contrast to one linear reasoning path.
- [x] [Yang et al. (2024) A Critical Review of Causal Reasoning Benchmarks for Large Language Models](https://arxiv.org/abs/2407.08029) - benchmark-design critique relevant to judging whether agent gains imply causal understanding.
- [x] [Wang et al. (2024) CausalBench: A Comprehensive Benchmark for Evaluating Causal Reasoning Capabilities of Large Language Models](https://aclanthology.org/2024.sighan-1.17/) - benchmark source spanning text, mathematics, and code, including intervention-style evaluation.
- [x] [OpenCausalLab (2024) Causal Evaluation of Language Models (CaLM)](https://opencausalab.github.io/CaLM) - accessible large-scale summary showing accuracy collapse as causal complexity rises.
- [x] [Research repo (2026-05-19) Research Question 2.4: Pearl's Causal Hierarchy and the formal limits of observational data for intervention and counterfactual reasoning](https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq2-4-causal-hierarchy-formal-limits.md) - formal prior item on why Level 1 evidence does not generically determine Level 2 or Level 3 answers.
- [x] [Research repo (2026-05-19) Research Question 3.1: Large Language Models as Statistical Optimisers, Token Distribution vs. Invariant Causal Models of Reality](https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq3-1-llm-statistical-vs-causal.md) - prior item on the base model class.
- [x] [Research repo (2026-05-19) Research Question 3.2: The Stochastic Parrot Under Pressure, Large Language Model Failures on Out-of-Distribution Logical Prompts Requiring Structural Intervention](https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq3-2-stochastic-parrot-ood.md) - prior item on structural failure under novelty.
- [x] [Research repo (2026-05-19) Research Question 3.3: In-Context Learning and chain-of-thought Prompting, Genuine Causal Reasoning or Extended Statistical Interpolation?](https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq3-3-cot-counterfactual-limits.md) - prior item on why longer reasoning traces do not by themselves cross the causal hierarchy.
- [x] [Research repo (2026-05-19) Are Multi-Step Large Language Model-Based Systems Inherently Less Explainable Than Equivalently Scoped Deterministic Software Systems?](https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-agentic-explainability-vs-traditional.md) - adjacent item on inspectability versus faithful explanation.

---

## Research Skill Output

*(Full output from running the research skill - retained verbatim in the completed item. Sections 0 to 5 are the investigation; Section 6 seeds the Findings section below.)*

### §0 Initialise

- Question: does a tool-feedback loop around a Large Language Model (LLM) create genuine explanatory reach, or mainly delay failure by adding search, tools, and retries?
- Scope: ReAct-style loops, reflection loops, branching search, planning limits, error propagation, and causal-hierarchy classification.
- Constraints: build directly on Research Questions 2.4, 3.1, 3.2, and 3.3; use URL-backed sources only; keep tags canonical.
- Output: executive summary, key findings, evidence map, assumptions, analysis, risks, gaps, uncertainties, and open questions.
- Prior completed items consulted: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq2-4-causal-hierarchy-formal-limits.md ; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq3-1-llm-statistical-vs-causal.md ; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq3-2-stochastic-parrot-ood.md ; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq3-3-cot-counterfactual-limits.md ; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-agentic-explainability-vs-traditional.md

### §1 Question Decomposition

1. Loop mechanics
   1.1 What exactly does a ReAct-style tool-feedback loop add beyond plain next-token generation?
   1.2 Which parts of the loop are still implemented by the same predictive model?
2. Causal-hierarchy test
   2.1 Does tool access itself create reliable reasoning about the effects of actions?
   2.2 Does verification or retry create reliable reasoning about alternate worlds under different actions?
   2.3 If causal reach appears, is it inside the model, or imported from an external tool or environment?
3. Error cascade
   3.1 How does one early strategy-selection error constrain later tool calls?
   3.2 Can verification reliably detect those upstream errors, or can it also inherit them?
4. Empirical evidence
   4.1 Where do ReAct and Reflexion improve outcomes?
   4.2 What do Tree of Thoughts and planning benchmarks imply about the weakness of one-path loops?
   4.3 Do causal and unseen-task benchmarks show genuine explanatory reach or continued fragility?
5. Final classification
   5.1 Is the best-supported description "more understanding" or "better search plus grounding"?
   5.2 Where does that place the composite system on Pearl's hierarchy?

### §2 Investigation

#### A. What the loop changes, and what it does not

- [fact] ReAct interleaves reasoning traces with task-specific actions so that the model can gather observations from an external environment and condition later text on those observations. [source: https://arxiv.org/abs/2210.03629; https://react-lm.github.io/]
- [fact] Mialon et al. describe augmented language models as systems that add reasoning skills and tool use while still adhering to a standard missing-token prediction objective. [source: https://arxiv.org/abs/2302.07842]
- [inference] The outer loop therefore changes the information flow available at inference time, but it does not by itself change the base training objective identified in Research Question 3.1. [source: https://arxiv.org/abs/2302.07842; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq3-1-llm-statistical-vs-causal.md]
- [inference] A ReAct-style loop is best understood as a policy for when to think, act, observe, and continue, not as direct evidence that the model has acquired an invariant causal model of the environment. [source: https://arxiv.org/abs/2210.03629; https://react-lm.github.io/; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq3-1-llm-statistical-vs-causal.md]

#### B. What tool access and feedback actually add

- [fact] ReAct reports gains on question answering and fact verification by querying a simple Wikipedia Application Programming Interface (API), which lets the agent fetch information rather than rely only on internal recall. [source: https://arxiv.org/abs/2210.03629; https://react-lm.github.io/]
- [fact] Reflexion improves repeated-trial performance by storing verbal feedback in episodic memory and reusing that reflective text on later attempts. [source: https://arxiv.org/abs/2303.11366]
- [inference] These gains are evidence that external state, tool outputs, and feedback buffers can widen the effective context seen by the policy. [source: https://arxiv.org/abs/2210.03629; https://arxiv.org/abs/2303.11366; https://arxiv.org/abs/2302.07842]
- [inference] They are not yet evidence that the model has learned Level 2 intervention structure internally, because the new semantics can reside in the external environment, tool, or feedback record rather than in the model's own world representation. [source: https://arxiv.org/abs/2302.07842; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq2-4-causal-hierarchy-formal-limits.md]

#### C. Why the error-cascade problem remains

- [fact] Research Question 3.3 concluded that one linear chain-of-thought path compounds error risk because later steps condition on earlier generated text. [source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq3-3-cot-counterfactual-limits.md]
- [fact] Tree of Thoughts was proposed precisely because language models remain confined to left-to-right decision processes during inference and can fail on tasks that need exploration, lookahead, or recovery from early wrong moves. [source: https://openreview.net/forum?id=5Xc1ecxO1h]
- [fact] The Tree of Thoughts paper reports a large Game of 24 gap between one chain-of-thought path and branching search, 4 percent versus 74 percent on the reported setup. [source: https://openreview.net/forum?id=5Xc1ecxO1h]
- [inference] A tool-feedback loop therefore does not remove compounding error; it mainly adds more places where an early wrong strategy can be executed, observed, and sometimes corrected. [source: https://openreview.net/forum?id=5Xc1ecxO1h; https://react-lm.github.io/; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq3-3-cot-counterfactual-limits.md]
- [inference] If the loop chooses the wrong subgoal or tool, later verification operates on a trajectory already shaped by that mistake, so the system's reliability still depends on search breadth, recovery mechanisms, and the observability of failure. [source: https://openreview.net/forum?id=5Xc1ecxO1h; https://arxiv.org/abs/2303.11366; https://react-lm.github.io/]

#### D. Where agentic loops succeed empirically

- [fact] ReAct reports improved human interpretability and trustworthiness relative to baselines without reasoning traces, alongside strong gains on question answering, fact verification, and interactive decision benchmarks. [source: https://arxiv.org/abs/2210.03629; https://react-lm.github.io/]
- [fact] Reflexion reports substantial improvement over a baseline agent across sequential decision-making, coding, and reasoning tasks, including 91 percent pass@1 on HumanEval in the cited version. [source: https://arxiv.org/abs/2303.11366]
- [inference] The consistent success pattern is that loops help when performance depends on retrieving missing information, persisting feedback, or revising a local search policy after observable mistakes. [source: https://arxiv.org/abs/2210.03629; https://arxiv.org/abs/2303.11366; https://openreview.net/forum?id=5Xc1ecxO1h]
- [inference] That pattern fits a search-and-grounding explanation better than a "new explanatory reach" explanation, because the cited gains come from better trajectory management and access to external state, not from a demonstrated jump in causal-hierarchy level. [source: https://arxiv.org/abs/2210.03629; https://arxiv.org/abs/2303.11366; https://arxiv.org/abs/2302.07842; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq2-4-causal-hierarchy-formal-limits.md]

#### E. Where the same systems still fail

- [fact] The ReAct project page includes an explicit failure example in an interactive benchmark and describes the format as inspectable rather than perfect. [source: https://react-lm.github.io/]
- [fact] Valmeekam et al. argue that reported planning gains are often confounded by world-knowledge retrieval and present PlanBench because critical planning capabilities, including plan generation, remain weak even in strong models. [source: https://arxiv.org/abs/2206.10498]
- [fact] The CaLM project summary states that language models struggle on sophisticated causal reasoning tasks and that accuracy falls almost to zero as causal complexity increases. [source: https://opencausalab.github.io/CaLM]
- [fact] Yang et al. argue that several causal benchmarks can be solved through retrieval of domain knowledge, which weakens the claim that benchmark success demonstrates causal understanding. [source: https://arxiv.org/abs/2407.08029]
- [fact] Wang et al. introduce CausalBench because earlier benchmarks did not adequately distinguish genuine causal understanding from narrow guessing across text, mathematics, and code. [source: https://aclanthology.org/2024.sighan-1.17/]
- [inference] The empirical record therefore shows better loop-level performance on some tasks without resolving the deeper question of explanatory reach, because the same literature still reports fragility on planning-heavy, unseen, and causally complex problems. [source: https://arxiv.org/abs/2206.10498; https://opencausalab.github.io/CaLM; https://arxiv.org/abs/2407.08029; https://aclanthology.org/2024.sighan-1.17/]

#### F. Causal-hierarchy classification

- [fact] Research Question 2.4 concluded that Level 1 observational information does not generically determine Level 2 intervention answers or Level 3 counterfactual answers. [source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq2-4-causal-hierarchy-formal-limits.md]
- [fact] Research Question 3.2 concluded that LLM performance remains fragile when prompts require structural intervention or genuinely novel composition outside familiar text patterns. [source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq3-2-stochastic-parrot-ood.md]
- [inference] A tool-feedback loop can operationally answer higher-level questions only when the environment or tool already embodies the needed causal semantics, for example a simulator, planner, search engine, or verifier that returns information unavailable from plain text continuation alone. [source: https://arxiv.org/abs/2302.07842; https://arxiv.org/abs/2210.03629; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq2-4-causal-hierarchy-formal-limits.md]
- [inference] In that case, the composite system's reach is imported and distributed across the whole sociotechnical stack, rather than being evidence that the base language model itself has crossed from Level 1 association into intrinsic Level 2 or Level 3 reasoning. [source: https://arxiv.org/abs/2302.07842; https://arxiv.org/abs/2206.10498; https://opencausalab.github.io/CaLM; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq2-4-causal-hierarchy-formal-limits.md]

#### G. Assumptions carried into synthesis

- [assumption] ReAct, Reflexion, Tree of Thoughts, and PlanBench together are representative enough of the first-generation tool-feedback loop design space to support a classification-level conclusion about agentic loops. [justification: they cover interleaved reasoning and action, feedback memory, branching search, and planning evaluation, which together span the main mechanisms this item analyses; source: https://arxiv.org/abs/2210.03629; https://arxiv.org/abs/2303.11366; https://openreview.net/forum?id=5Xc1ecxO1h; https://arxiv.org/abs/2206.10498]
- [assumption] Improvements reported on coding, question answering, and interactive benchmarks are relevant evidence for explanatory reach only when combined with causal and unseen-task benchmarks, because task success alone does not settle whether the loop has acquired causal semantics. [justification: this item distinguishes performance gains from causal-hierarchy advancement; source: https://arxiv.org/abs/2407.08029; https://opencausalab.github.io/CaLM; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq2-4-causal-hierarchy-formal-limits.md]

### §3 Reasoning

- [inference] The strongest charitable reading of agentic loops is not that they are empty wrappers, but that they externalise information gathering, persistence, evaluation, and branching search in ways that the base model alone cannot perform reliably in one shot. [source: https://arxiv.org/abs/2210.03629; https://arxiv.org/abs/2303.11366; https://openreview.net/forum?id=5Xc1ecxO1h]
- [inference] Even under that charitable reading, the question of explanatory reach stays separate from task success, because a loop can improve end-to-end performance by searching better or calling stronger tools while leaving the model's internal semantics unchanged. [source: https://arxiv.org/abs/2302.07842; https://arxiv.org/abs/2407.08029]
- [inference] The right classification is therefore layered: local loop performance can improve materially, yet the composite system still mostly maps present inputs to actions and gets its apparent higher-level competence from external modules and task structure. [source: https://arxiv.org/abs/2210.03629; https://arxiv.org/abs/2206.10498; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq2-4-causal-hierarchy-formal-limits.md]
- [inference] This explains why inspectable reasoning traces and retries are useful governance artifacts without being proofs of genuine understanding, a distinction that aligns with the adjacent explainability item in this repository. [source: https://react-lm.github.io/; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-agentic-explainability-vs-traditional.md]

### §4 Consistency Check

- [fact] Tension: ReAct and Reflexion show clear benchmark gains, which could be read as evidence that the loop has added a qualitatively new capability. [source: https://arxiv.org/abs/2210.03629; https://arxiv.org/abs/2303.11366]
- [inference] Resolution: the gains are real, but the sources attribute them to tool access, verbal feedback, and iterative policy adjustment, not to a demonstrated internal causal model or theorem-level collapse of Pearl's hierarchy. [source: https://arxiv.org/abs/2210.03629; https://arxiv.org/abs/2303.11366; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq2-4-causal-hierarchy-formal-limits.md]
- [fact] Tension: tool outputs can let the composite system answer questions that plain text continuation would miss. [source: https://arxiv.org/abs/2210.03629; https://arxiv.org/abs/2302.07842]
- [inference] Resolution: this is compatible with the main claim, because importing observations or solver outputs from an external module expands the system's evidence base without proving that the base model has itself crossed from Level 1 to intrinsic Level 2 or Level 3 reasoning. [source: https://arxiv.org/abs/2302.07842; https://opencausalab.github.io/CaLM; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq2-4-causal-hierarchy-formal-limits.md]

### §5 Depth and Breadth Expansion

- [inference] Technical lens: the loop's main contribution is control-flow structure, including branching, memory, external calls, and stopping criteria, which is why the strongest improvements appear on tasks with search or retrieval bottlenecks. [source: https://arxiv.org/abs/2210.03629; https://arxiv.org/abs/2303.11366; https://openreview.net/forum?id=5Xc1ecxO1h]
- [inference] Epistemic lens: explanatory reach belongs to the whole assembled system only to the extent that external tools embody trustworthy domain structure, so the key question becomes where the semantics live, not whether the loop looks agentic. [source: https://arxiv.org/abs/2302.07842; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq2-4-causal-hierarchy-formal-limits.md]
- [inference] Governance lens: human-readable trajectories improve auditability and intervention opportunities, but that makes them better control surfaces than evidence of machine understanding. [source: https://react-lm.github.io/; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-agentic-explainability-vs-traditional.md]
- [inference] Strategic lens: the Phase 5 comparison between stochastic and deterministic systems should therefore compare where causal semantics are imported from deterministic tools or workflows, because that boundary supplies the semantics the language model alone still lacks. [source: https://arxiv.org/abs/2302.07842; https://arxiv.org/abs/2206.10498; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq2-4-causal-hierarchy-formal-limits.md]

### §6 Synthesis

**Executive summary:**

- [inference] Wrapping a Large Language Model (LLM) in a ReAct-style tool-feedback loop does not, on the cited evidence, give the model intrinsic causal understanding; it mainly improves search, grounding, memory, and local error recovery. [source: https://arxiv.org/abs/2210.03629; https://arxiv.org/abs/2303.11366; https://arxiv.org/abs/2302.07842; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq2-4-causal-hierarchy-formal-limits.md]
- [inference] ReAct, Reflexion, and Tree of Thoughts show that loop structure can materially improve performance by adding external observations, episodic feedback, or branching search. [source: https://arxiv.org/abs/2210.03629; https://arxiv.org/abs/2303.11366; https://openreview.net/forum?id=5Xc1ecxO1h]
- [inference] The same evidence base also shows that early strategy mistakes still propagate through later actions and checks, which is why branching, backtracking, and stronger verifiers matter so much. [source: https://openreview.net/forum?id=5Xc1ecxO1h; https://react-lm.github.io/; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq3-3-cot-counterfactual-limits.md]
- [inference] The best-supported classification is that the composite system still mostly maps present inputs to actions and gets any apparent higher-level reach from external tools or environments that already encode the needed action-effect or alternate-world semantics. [source: https://arxiv.org/abs/2302.07842; https://arxiv.org/abs/2206.10498; https://opencausalab.github.io/CaLM; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq2-4-causal-hierarchy-formal-limits.md]

**Key findings:**

1. [inference] ReAct-style loops improve performance mainly by interleaving text generation with external observations and actions, so the loop widens the model's evidence stream without changing the base next-token objective. [source: https://arxiv.org/abs/2210.03629; https://arxiv.org/abs/2302.07842]
2. [inference] Reflexion shows that verbal feedback and episodic memory can improve repeated-trial behavior, but that mechanism is best understood as local policy adaptation across attempts rather than as proof of a learned causal world model. [source: https://arxiv.org/abs/2303.11366; https://arxiv.org/abs/2302.07842]
3. [inference] Error propagation remains a structural feature of one-path agentic loops, because later actions and checks are conditioned on earlier generated strategy tokens, so the loop can execute and sometimes amplify an upstream mistake before it corrects it. [source: https://openreview.net/forum?id=5Xc1ecxO1h; https://react-lm.github.io/; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq3-3-cot-counterfactual-limits.md]
4. [inference] Tree of Thoughts shows that branching, self-evaluation, and backtracking outperform one linear chain on planning-heavy tasks, which supports the narrower conclusion that naive sequential looping is brittle under novelty and search pressure. [source: https://openreview.net/forum?id=5Xc1ecxO1h; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq3-3-cot-counterfactual-limits.md]
5. [fact] Planning and causal benchmarks still show major weakness on structurally demanding tasks, including plan generation and higher-complexity causal reasoning, across planning suites and large causal evaluations. [source: https://arxiv.org/abs/2206.10498; https://opencausalab.github.io/CaLM; https://aclanthology.org/2024.sighan-1.17/]
6. [inference] Human-readable trajectories increase inspectability and intervention opportunities, but they are better treated as audit artifacts than as evidence that the system has acquired genuine explanatory reach. [source: https://react-lm.github.io/; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-agentic-explainability-vs-traditional.md]
7. [inference] The composite system can answer some questions about the effects of actions or about alternate worlds under different actions only when an external tool, simulator, or environment already embodies those semantics, so the extra reach is imported and distributed rather than intrinsic to the language model. [source: https://arxiv.org/abs/2302.07842; https://arxiv.org/abs/2210.03629; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq2-4-causal-hierarchy-formal-limits.md]

**Evidence map:**

- [inference] ReAct-style loops widen the evidence stream without changing the base next-token objective. | source: https://arxiv.org/abs/2210.03629 ; https://arxiv.org/abs/2302.07842 | confidence: medium | notes: loop structure plus unchanged training objective
- [inference] Reflexion improves repeated-trial behavior through feedback reuse rather than demonstrated causal modelling. | source: https://arxiv.org/abs/2303.11366 ; https://arxiv.org/abs/2302.07842 | confidence: medium | notes: memory and verbal feedback
- [inference] Early strategy errors propagate through later actions and checks in one-path loops. | source: https://openreview.net/forum?id=5Xc1ecxO1h ; https://react-lm.github.io/ ; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq3-3-cot-counterfactual-limits.md | confidence: medium | notes: compounding conditional dependence
- [inference] Branching search materially outperforms one-path chains on planning-heavy tasks, which supports the conclusion that naive sequential looping is brittle under novelty and search pressure. | source: https://openreview.net/forum?id=5Xc1ecxO1h ; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq3-3-cot-counterfactual-limits.md | confidence: medium | notes: direct task result plus prior one-path brittleness
- [fact] Planning and causal benchmarks still report major weakness on higher-complexity tasks across planning suites and large causal evaluations. | source: https://arxiv.org/abs/2206.10498 ; https://opencausalab.github.io/CaLM ; https://aclanthology.org/2024.sighan-1.17/ | confidence: high | notes: planning plus causal complexity
- [inference] Inspectable traces are better audit artifacts than proofs of understanding. | source: https://react-lm.github.io/ ; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-agentic-explainability-vs-traditional.md | confidence: medium | notes: interpretability is not the same as faithful explanation
- [inference] Apparent higher-level reach is imported from external tools or environments rather than from intrinsic intervention or alternate-world modelling inside the language model. | source: https://arxiv.org/abs/2302.07842 ; https://arxiv.org/abs/2210.03629 ; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq2-4-causal-hierarchy-formal-limits.md | confidence: medium | notes: semantics live in the wider stack

**Assumptions:**

- [assumption] ReAct, Reflexion, Tree of Thoughts, and PlanBench are representative enough to classify first-generation tool-feedback loops. [justification: they span interleaved action, feedback memory, branching search, and explicit planning evaluation; source: https://arxiv.org/abs/2210.03629; https://arxiv.org/abs/2303.11366; https://openreview.net/forum?id=5Xc1ecxO1h; https://arxiv.org/abs/2206.10498]
- [assumption] Benchmark gains should count as evidence about explanatory reach only when they are checked against causal and novelty-sensitive evaluations. [justification: otherwise retrieval or task familiarity can masquerade as deeper understanding; source: https://arxiv.org/abs/2407.08029; https://opencausalab.github.io/CaLM; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq2-4-causal-hierarchy-formal-limits.md]

**Analysis:**

- [inference] The evidence is strongest for a "better controller" interpretation of agentic loops, because every major improvement mechanism in the cited sources is about information access, memory, branching, or retry policy. [source: https://arxiv.org/abs/2210.03629; https://arxiv.org/abs/2303.11366; https://openreview.net/forum?id=5Xc1ecxO1h]
- [inference] The main rival interpretation, that the loop itself creates genuine explanatory reach, would need evidence that the model can internally answer questions about the effects of actions or about alternate worlds under different actions beyond what the external tool or environment already provides. [source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq2-4-causal-hierarchy-formal-limits.md; https://arxiv.org/abs/2407.08029]
- [inference] The current sources do not show that stronger claim, and the planning and causal benchmarks point the other way by showing continuing fragility as structural demands rise. [source: https://arxiv.org/abs/2206.10498; https://opencausalab.github.io/CaLM; https://aclanthology.org/2024.sighan-1.17/]

**Risks, gaps, uncertainties:**

- [inference] The literature is stronger on task performance than on direct tests of where causal semantics reside inside the full loop, so some of the final classification still depends on inference from benchmark design and system architecture. [source: https://arxiv.org/abs/2302.07842; https://arxiv.org/abs/2407.08029]
- [assumption] A loop built around a genuinely causal external simulator or planner could give the assembled system more practical explanatory reach than the first-generation sources studied here document. [justification: external modules can encode semantics the base model lacks, but the cited sources do not isolate that boundary cleanly; source: https://arxiv.org/abs/2302.07842; https://arxiv.org/abs/2210.03629]

**Open questions:**

- What empirical design best separates causal reach imported from a deterministic tool from causal reach learned by the language model itself?
- How often does verification in real agent deployments catch upstream strategy errors, versus merely certify a locally coherent but globally wrong trajectory?
- At what point does loop orchestration become strong enough that the right unit of analysis is no longer the model, but the full assembled system with tool semantics made explicit?

### §7 Recursive Review

- [fact] This revision includes explicit labels on visible claims in Research Skill Output and Findings, with URL-backed citations on claim-bearing prose. [source: https://github.com/davidamitchell/Research/blob/2eb67648731413c8b6892d9e6a2316f723ceac8a/Research/in-progress/2026-05-18-rq4-1-agentic-loop-explanatory-reach.md]
- [fact] Acronym expansion, Section 6 and Findings parity, and inline-citation checks were completed on this revision before re-running review. [source: https://github.com/davidamitchell/Research/blob/2eb67648731413c8b6892d9e6a2316f723ceac8a/Research/in-progress/2026-05-18-rq4-1-agentic-loop-explanatory-reach.md]

---

## Findings

### Executive Summary

Wrapping a Large Language Model (LLM) in a ReAct-style tool-feedback loop does not, on the current evidence, give the model intrinsic causal understanding; it mainly improves search, grounding, memory, and local error recovery. [inference; source: https://arxiv.org/abs/2210.03629; https://arxiv.org/abs/2303.11366; https://arxiv.org/abs/2302.07842; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq2-4-causal-hierarchy-formal-limits.md]

ReAct, Reflexion, and Tree of Thoughts show that loop structure can materially improve outcomes when the task rewards retrieving missing information, persisting feedback, or branching away from an early bad path. [inference; source: https://arxiv.org/abs/2210.03629; https://arxiv.org/abs/2303.11366; https://openreview.net/forum?id=5Xc1ecxO1h]

Those gains do not erase the core failure mode identified in Phase 3, because early strategy errors still shape later tool calls and verification steps, and planning-heavy or causally complex benchmarks remain fragile. [inference; source: https://openreview.net/forum?id=5Xc1ecxO1h; https://arxiv.org/abs/2206.10498; https://opencausalab.github.io/CaLM; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq3-3-cot-counterfactual-limits.md]

The best-supported classification is that the composite system still mostly maps present inputs to actions and gets any occasional higher-level reach from external tools or environments that already encode the needed action-effect or alternate-world semantics. [inference; source: https://arxiv.org/abs/2302.07842; https://arxiv.org/abs/2210.03629; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq2-4-causal-hierarchy-formal-limits.md]

### Key Findings

1. **ReAct-style loops improve performance mainly by interleaving text generation with external observations and actions, so the loop widens the model's evidence stream without changing the base next-token objective.** ([inference]; medium confidence; source: https://arxiv.org/abs/2210.03629; https://arxiv.org/abs/2302.07842)
2. **Reflexion shows that verbal feedback and episodic memory can improve repeated-trial behavior, but that mechanism is best understood as local policy adaptation across attempts rather than as proof of a learned causal world model.** ([inference]; medium confidence; source: https://arxiv.org/abs/2303.11366; https://arxiv.org/abs/2302.07842)
3. **Error propagation remains a structural feature of one-path agentic loops, because later actions and checks are conditioned on earlier generated strategy tokens, so the loop can execute and sometimes amplify an upstream mistake before it corrects it.** ([inference]; medium confidence; source: https://openreview.net/forum?id=5Xc1ecxO1h; https://react-lm.github.io/; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq3-3-cot-counterfactual-limits.md)
4. **Tree of Thoughts shows that branching, self-evaluation, and backtracking outperform one linear chain on planning-heavy tasks, which supports the narrower conclusion that naive sequential looping is brittle under novelty and search pressure.** ([inference]; medium confidence; source: https://openreview.net/forum?id=5Xc1ecxO1h; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq3-3-cot-counterfactual-limits.md)
5. **Planning and causal benchmarks still show major weakness on structurally demanding tasks, including plan generation and higher-complexity causal reasoning, across planning suites and large causal evaluations.** ([fact]; high confidence; source: https://arxiv.org/abs/2206.10498; https://opencausalab.github.io/CaLM; https://aclanthology.org/2024.sighan-1.17/)
6. **Human-readable trajectories increase inspectability and intervention opportunities, but they are better treated as audit artifacts than as evidence that the system has acquired genuine explanatory reach.** ([inference]; medium confidence; source: https://react-lm.github.io/; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-agentic-explainability-vs-traditional.md)
7. **The composite system can answer some questions about the effects of actions or about alternate worlds under different actions only when an external tool, simulator, or environment already embodies those semantics, so the extra reach is imported and distributed rather than intrinsic to the language model.** ([inference]; medium confidence; source: https://arxiv.org/abs/2302.07842; https://arxiv.org/abs/2210.03629; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq2-4-causal-hierarchy-formal-limits.md)

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [inference] ReAct-style loops widen the evidence stream without changing the base next-token objective. | https://arxiv.org/abs/2210.03629 ; https://arxiv.org/abs/2302.07842 | medium | loop structure plus unchanged training objective |
| [inference] Reflexion improves repeated-trial behavior through feedback reuse rather than demonstrated causal modelling. | https://arxiv.org/abs/2303.11366 ; https://arxiv.org/abs/2302.07842 | medium | memory and verbal feedback |
| [inference] Early strategy errors propagate through later actions and checks in one-path loops. | https://openreview.net/forum?id=5Xc1ecxO1h ; https://react-lm.github.io/ ; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq3-3-cot-counterfactual-limits.md | medium | compounding conditional dependence |
| [inference] Branching search materially outperforms one-path chains on planning-heavy tasks, which supports the conclusion that naive sequential looping is brittle under novelty and search pressure. | https://openreview.net/forum?id=5Xc1ecxO1h ; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq3-3-cot-counterfactual-limits.md | medium | direct task result plus prior one-path brittleness |
| [fact] Planning and causal benchmarks still report major weakness on higher-complexity tasks across planning suites and large causal evaluations. | https://arxiv.org/abs/2206.10498 ; https://opencausalab.github.io/CaLM ; https://aclanthology.org/2024.sighan-1.17/ | high | planning plus causal complexity |
| [inference] Inspectable traces are better audit artifacts than proofs of understanding. | https://react-lm.github.io/ ; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-agentic-explainability-vs-traditional.md | medium | interpretability differs from faithful explanation |
| [inference] Apparent higher-level reach is imported from external tools or environments rather than from intrinsic intervention or alternate-world modelling inside the language model. | https://arxiv.org/abs/2302.07842 ; https://arxiv.org/abs/2210.03629 ; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq2-4-causal-hierarchy-formal-limits.md | medium | semantics live in the wider stack |

### Assumptions

- **Assumption:** ReAct, Reflexion, Tree of Thoughts, and PlanBench are representative enough to classify first-generation tool-feedback loops. **Justification:** They span interleaved action, feedback memory, branching search, and explicit planning evaluation. [assumption; source: https://arxiv.org/abs/2210.03629; https://arxiv.org/abs/2303.11366; https://openreview.net/forum?id=5Xc1ecxO1h; https://arxiv.org/abs/2206.10498]
- **Assumption:** Benchmark gains should count as evidence about explanatory reach only when they are checked against causal and novelty-sensitive evaluations. **Justification:** Otherwise retrieval or task familiarity can masquerade as deeper understanding. [assumption; source: https://arxiv.org/abs/2407.08029; https://opencausalab.github.io/CaLM; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq2-4-causal-hierarchy-formal-limits.md]

### Analysis

The evidence is strongest for a "better controller" interpretation of tool-feedback loops, because every major improvement mechanism in the cited sources is about information access, memory, branching, or retry policy. [inference; source: https://arxiv.org/abs/2210.03629; https://arxiv.org/abs/2303.11366; https://openreview.net/forum?id=5Xc1ecxO1h]

The main rival interpretation, that the loop itself creates genuine explanatory reach, would require evidence that the model can internally answer questions about the effects of actions or about alternate worlds under different actions beyond what the external tool or environment already provides. [inference; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq2-4-causal-hierarchy-formal-limits.md; https://arxiv.org/abs/2407.08029]

The current sources do not show that stronger claim, and the planning and causal benchmarks point the other way by showing continuing fragility as structural demands rise. [inference; source: https://arxiv.org/abs/2206.10498; https://opencausalab.github.io/CaLM; https://aclanthology.org/2024.sighan-1.17/]

This leaves a narrow but important middle position: the assembled system can become more capable and more governable without becoming more intrinsically explanatory, because the loop can relocate semantic work into tools, environments, and control logic around the model. [inference; source: https://arxiv.org/abs/2302.07842; https://react-lm.github.io/; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-agentic-explainability-vs-traditional.md]

### Risks, Gaps, and Uncertainties

- The literature is stronger on task performance than on direct tests of where causal semantics reside inside the full loop, so some of the final classification still depends on inference from benchmark design and system architecture. [inference; source: https://arxiv.org/abs/2302.07842; https://arxiv.org/abs/2407.08029]
- A loop built around a genuinely causal external simulator or planner could give the assembled system more practical explanatory reach than the first-generation sources studied here document. [assumption; source: https://arxiv.org/abs/2302.07842; https://arxiv.org/abs/2210.03629]

### Open Questions

- What empirical design best separates causal reach imported from a deterministic tool from causal reach learned by the language model itself?
- How often does verification in real agent deployments catch upstream strategy errors, versus merely certify a locally coherent but globally wrong trajectory?
- At what point does loop orchestration become strong enough that the right unit of analysis is no longer the model, but the full assembled system with tool semantics made explicit?

---

## Output

- Type: knowledge
- Description: A classification of tool-feedback loops around Large Language Models as improved search-and-grounding systems rather than systems that have, by that wrapping alone, acquired intrinsic causal understanding. [inference; source: https://arxiv.org/abs/2210.03629; https://arxiv.org/abs/2302.07842; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq2-4-causal-hierarchy-formal-limits.md]
- Links:
  - https://arxiv.org/abs/2210.03629
  - https://arxiv.org/abs/2303.11366
  - https://arxiv.org/abs/2206.10498
