---
review_count: 2
title: "Research Question 4.2: Adversarial inputs and error propagation through multi-step tool-using verification and strategy phases"
added: 2026-05-18T19:40:00+00:00
status: completed
priority: high
blocks:
  - 2026-05-18-rq4-3-ood-generalization-agentic
tags: [agentic-ai, llm, evaluation, prompt-injection]
started: 2026-05-19T11:52:12+00:00
completed: 2026-05-19T12:12:50+00:00
output: [knowledge]
cites:
  - 2026-05-18-rq4-1-agentic-loop-explanatory-reach
  - 2026-05-02-ai-security-threat-model-prompt-injection-rag-supply-chain
related:
  - 2026-05-08-integrated-cascading-failure-agentic-vs-generative-ai-risk
  - 2026-04-30-human-bias-ai-trust-rlhf-sycophancy
  - 2026-05-18-rq4-3-ood-generalization-agentic
superseded_by: ~
supersedes: ~
item_type: primary
confidence: medium
versions: []
---

# Research Question 4.2: Adversarial inputs and error propagation through multi-step tool-using verification and strategy phases

## Research Question

How do adversarial inputs or unexpected environmental shifts propagate error through a multi-step tool-using Large Language Model (LLM) system's verification and strategy-selection phases when the underlying model lacks grounded knowledge of how actions and environmental changes actually produce outcomes in the system?

## Scope

**In scope:**
- Gradual corruption of the system's working context across multi-step inference, sometimes called semantic drift
- Cascading failure modes in the perception, strategy, action, and verification loop
- Brittle verification loops, meaning failures that occur when the same Large Language Model is asked to judge whether its own intermediate reasoning or tool use was correct
- Formal error-propagation models for multi-step tool-using sequences
- Prompt injection, meaning malicious instructions embedded in user input, retrieved documents, webpages, or tool outputs that the model treats as instructions

**Out of scope:**
- Adversarial attacks on model weights or parameters, including white-box gradient attacks
- Defensive design details beyond what is needed to explain why the failure occurs

**Constraints:** Builds directly on Research Question 4.1, must model propagation formally rather than only cataloguing examples, must use URL-backed sources only, and must keep tags in canonical forms where a canonical tag exists.

## Context

Research Question 4.1 concluded that tool-feedback loops widen search and grounding opportunities but do not by themselves give the base model grounded causal reasoning about the environment. [fact; source: https://davidamitchell.github.io/Research/research/2026-05-18-rq4-1-agentic-loop-explanatory-reach.html]

This item examines what happens when the same loop is exposed to adversarial or shifted inputs, because strategy selection, tool choice, and verification can all be driven by a state representation that already contains a high-confidence semantic error. [inference; source: https://davidamitchell.github.io/Research/research/2026-05-18-rq4-1-agentic-loop-explanatory-reach.html; https://arxiv.org/abs/2302.12173; https://arxiv.org/abs/2310.01798]

Prompt injection is the most concrete empirical case because it shows how text that looks like ordinary content can be reinterpreted as instructions and then propagated through planning, tool use, memory, and later verification. [fact; source: https://arxiv.org/abs/2302.12173; https://arxiv.org/abs/2312.14197; https://www.microsoft.com/en-us/msrc/blog/2025/07/how-microsoft-defends-against-indirect-prompt-injection-attacks]

## Approach

1. Define an adversarial-input model for multi-step tool-using Large Language Model systems, including both prompt injection and environmental shift.
2. Model how a corrupted state representation propagates from perception into strategy selection, tool action, memory, and verification.
3. Formalise why generic self-verification is brittle when it uses the same model class and the same contaminated context.
4. Survey prompt injection and memory-poisoning evidence as empirical cases of adversarial propagation.
5. Derive a compact error-amplification model across repeated loop steps.

## Sources

- [x] [Mitchell (2026) Research Question 4.1: Tool-feedback loops and explanatory reach](https://davidamitchell.github.io/Research/research/2026-05-18-rq4-1-agentic-loop-explanatory-reach.html) - prior completed item on loop-level causal limits and path-dependent error.
- [x] [Mitchell (2026) Artificial Intelligence security threat model for prompt injection, Retrieval-Augmented Generation, supply chain compromise, and data exfiltration](https://davidamitchell.github.io/Research/research/2026-05-02-ai-security-threat-model-prompt-injection-rag-supply-chain.html) - prior completed item on structural prompt-injection risk in tool-using systems.
- [x] [Mitchell (2026) Integrated cascading failure in agentic versus generative Artificial Intelligence risk](https://davidamitchell.github.io/Research/research/2026-05-08-integrated-cascading-failure-agentic-vs-generative-ai-risk.html) - prior completed synthesis on persistence and blast radius in multi-step systems.
- [x] [Anthropic (2026) Trustworthy agents](https://www.anthropic.com/research/trustworthy-agents) - accessible definition of an agent loop and its oversight surfaces.
- [x] [Amodei et al. (2016) Concrete Problems in Artificial Intelligence (AI) Safety](https://arxiv.org/abs/1606.06565) - distributional shift as a practical safety problem.
- [x] [Goodfellow et al. (2015) Explaining and Harnessing Adversarial Examples](https://arxiv.org/abs/1412.6572) - canonical adversarial-example framing for high-confidence error under worst-case perturbation.
- [x] [Perez and Ribeiro (2022) Ignore Previous Prompt: Attack Techniques For Language Models](https://arxiv.org/abs/2211.09527) - direct prompt-injection evidence showing goal hijacking and prompt leaking in deployed Large Language Models.
- [x] [Ziegler et al. (2022) Adversarial Training for High-Stakes Reliability](https://arxiv.org/abs/2205.01663) - empirical evidence that adversarial robustness is attack-specific rather than automatic.
- [x] [Greshake et al. (2023) Not what you've signed up for: Compromising Real-World Large Language Model-Integrated Applications with Indirect Prompt Injection](https://arxiv.org/abs/2302.12173) - foundational indirect prompt-injection paper.
- [x] [Yi et al. (2025) Benchmarking and Defending Against Indirect Prompt Injection Attacks on Large Language Models](https://arxiv.org/abs/2312.14197) - benchmark evidence that evaluated models remain vulnerable because they do not reliably distinguish context from instructions.
- [x] [Huang et al. (2024) Large Language Models Cannot Self-Correct Reasoning Yet](https://arxiv.org/abs/2310.01798) - primary evidence on intrinsic self-correction limits.
- [x] [Wu et al. (2024) Large Language Models Can Self-Correct with Key Condition Verification](https://aclanthology.org/2024.emnlp-main.714/) - evidence that structured verification can outperform generic self-correction.
- [x] [Open Worldwide Application Security Project (OWASP) Prompt Injection](https://owasp.org/www-community/attacks/PromptInjection) - accessible explanation of the prompt-injection semantic gap and attack forms.
- [x] [Microsoft (2025) How Microsoft defends against indirect prompt injection attacks](https://www.microsoft.com/en-us/msrc/blog/2025/07/how-microsoft-defends-against-indirect-prompt-injection-attacks) - official description of tool-mediated exfiltration and unintended-action pathways.
- [x] [Unit 42 (2025) Indirect prompt injection poisons Artificial Intelligence (AI) long-term memory](https://unit42.paloaltonetworks.com/indirect-prompt-injection-poisons-ai-longterm-memory/) - proof of concept showing cross-session propagation through memory summarization.

---

## Research Skill Output

*(Full output from running the research skill, retained verbatim in the completed item. Sections 0 to 5 are the investigation. Section 6 seeds the Findings section below.)*

### §0 Initialise

- Question: How do adversarial inputs and environmental shifts propagate error through the strategy and verification stages of a multi-step tool-using Large Language Model system?
- Scope: Adversarial input modelling, path-dependent propagation, brittle self-verification, prompt-injection evidence, and a formal amplification model.
- Constraints: Full-mode investigation, URL-backed sources only, direct cross-reference to prior completed items, explicit claim labels in the investigation, and no unsupported domain shorthand.
- Output: Knowledge item with executive summary, key findings, evidence map, assumptions, analysis, risks and gaps, and open questions.
- Prior completed items consulted: https://davidamitchell.github.io/Research/research/2026-05-18-rq4-1-agentic-loop-explanatory-reach.html ; https://davidamitchell.github.io/Research/research/2026-05-02-ai-security-threat-model-prompt-injection-rag-supply-chain.html ; https://davidamitchell.github.io/Research/research/2026-05-08-integrated-cascading-failure-agentic-vs-generative-ai-risk.html ; https://davidamitchell.github.io/Research/research/2026-04-30-human-bias-ai-trust-rlhf-sycophancy.html

### §1 Question Decomposition

1. Adversarial input model
   1.1 What counts as an adversarial input for a multi-step tool-using Large Language Model system?
   1.2 How do direct prompt injection, indirect prompt injection, and environmental shift fit that model?
2. Propagation path
   2.1 How does corrupted perception alter strategy selection?
   2.2 How do tool calls, memory updates, and later observations make the error path-dependent?
   2.3 Under what conditions does one local error become a cross-step or cross-session failure?
3. Verification limits
   3.1 Why is generic self-verification by the same model not an independent check?
   3.2 What evidence shows the limit of intrinsic self-correction?
   3.3 What does successful structured verification add that naive self-checking lacks?
4. Empirical grounding
   4.1 What do prompt-injection papers show about data-versus-instruction ambiguity?
   4.2 What do official security reports show about tool-mediated exfiltration and memory poisoning?
   4.3 What does distributional-shift work add about non-adversarial but still misleading observations?
5. Formalisation
   5.1 How can expected semantic error be represented over repeated steps?
   5.2 When does the loop damp error, and when does it amplify error?

### §2 Investigation

#### A. Prior completed-item sweep

- [fact] Research Question 4.1 concluded that tool-feedback loops add search, retrieval, and grounding opportunities but do not by themselves give the base Large Language Model grounded causal reasoning about the environment. [source: https://davidamitchell.github.io/Research/research/2026-05-18-rq4-1-agentic-loop-explanatory-reach.html]
- [fact] The repository threat-model item concluded that prompt injection is structural in tool-using systems because untrusted text can cross from data into instruction channels once it enters context. [source: https://davidamitchell.github.io/Research/research/2026-05-02-ai-security-threat-model-prompt-injection-rag-supply-chain.html]
- [fact] The repository cascading-failure synthesis concluded that memory, tool use, and delegated action increase persistence and blast radius once an error enters a multi-step loop. [source: https://davidamitchell.github.io/Research/research/2026-05-08-integrated-cascading-failure-agentic-vs-generative-ai-risk.html]

#### B. Adversarial input model

- [fact] Goodfellow et al. define adversarial examples as intentionally worst-case perturbations that cause high-confidence model error. [source: https://arxiv.org/abs/1412.6572]
- [fact] Perez and Ribeiro show that simple handcrafted prompts can cause goal hijacking and prompt leaking in deployed Large Language Models. [source: https://arxiv.org/abs/2211.09527]
- [fact] Greshake et al. show that indirect prompt injection works by embedding attacker instructions in retrieved or external content, which blurs the boundary between data and instructions in Large Language Model-integrated applications. [source: https://arxiv.org/abs/2302.12173]
- [fact] Yi et al. report that evaluated models remain universally vulnerable to indirect prompt injection and attribute that vulnerability to the models' inability to distinguish informational context from actionable instructions. [source: https://arxiv.org/abs/2312.14197]
- [inference] For this item, an adversarial input is therefore best modelled as any observation or retrieved artifact that remains locally plausible under the model's learned distribution while shifting the loop's latent task state away from the real environment or the user's intent. [source: https://arxiv.org/abs/1412.6572; https://arxiv.org/abs/2302.12173; https://arxiv.org/abs/2312.14197]
- [inference] Unexpected environmental shift belongs in the same propagation family when it makes familiar heuristics look locally sensible even though the environment's actual causal structure has changed. [source: https://arxiv.org/abs/1606.06565; https://davidamitchell.github.io/Research/research/2026-05-18-rq4-1-agentic-loop-explanatory-reach.html]

#### C. How corruption propagates through the loop

- [fact] Anthropic defines an agent as a model operating in a self-directed loop that plans, acts, observes the result, adjusts, and repeats, with model, harness, tools, and environment all affecting behavior. [source: https://www.anthropic.com/research/trustworthy-agents]
- [inference] If perception produces a corrupted state representation, strategy selection optimizes against that representation rather than against the world state, so the chosen subgoal and tool sequence can be conditionally rational for the wrong problem. [source: https://www.anthropic.com/research/trustworthy-agents; https://davidamitchell.github.io/Research/research/2026-05-18-rq4-1-agentic-loop-explanatory-reach.html; https://arxiv.org/abs/2302.12173]
- [inference] Once a wrong strategy is executed, subsequent observations become path-dependent because the agent samples tools, documents, and memory updates selected by the corrupted plan rather than by the original goal. [source: https://www.anthropic.com/research/trustworthy-agents; https://davidamitchell.github.io/Research/research/2026-05-18-rq4-1-agentic-loop-explanatory-reach.html; https://unit42.paloaltonetworks.com/indirect-prompt-injection-poisons-ai-longterm-memory/]
- [fact] Microsoft states that indirect prompt injection can arise from webpages, emails, shared documents, or tool outputs, and that tool-enabled systems can be induced to exfiltrate data or perform unintended actions. [source: https://www.microsoft.com/en-us/msrc/blog/2025/07/how-microsoft-defends-against-indirect-prompt-injection-attacks]
- [fact] Unit 42 show a proof of concept in which indirect prompt injection manipulates session summarization, stores malicious instructions in persistent memory, and causes later sessions to exfiltrate conversation history. [source: https://unit42.paloaltonetworks.com/indirect-prompt-injection-poisons-ai-longterm-memory/]
- [inference] The loop therefore has at least three amplification channels after initial corruption: branch selection, tool-mediated state changes, and persistent memory writes. [source: https://www.microsoft.com/en-us/msrc/blog/2025/07/how-microsoft-defends-against-indirect-prompt-injection-attacks; https://unit42.paloaltonetworks.com/indirect-prompt-injection-poisons-ai-longterm-memory/; https://www.anthropic.com/research/trustworthy-agents]

#### D. Why generic self-verification is brittle

- [fact] Huang et al. find that Large Language Models struggle to self-correct reasoning without external feedback and that performance can even degrade after intrinsic self-correction. [source: https://arxiv.org/abs/2310.01798]
- [fact] Wu et al. report gains from key-condition verification, which works by masking and checking specific conditions rather than asking for unconstrained generic self-correction. [source: https://aclanthology.org/2024.emnlp-main.714/]
- [fact] Yi et al. identify one cause of indirect prompt-injection success as models' inability to distinguish context from instructions, which is the same classification task a verification step must solve if it inspects the same contaminated context. [source: https://arxiv.org/abs/2312.14197]
- [inference] Generic Large Language Model self-verification is brittle because it reuses the same representation space and the same distributional heuristics that produced the original mistake, so attacks that live inside those blind spots are not checked by an independent evidence channel. [source: https://arxiv.org/abs/2310.01798; https://arxiv.org/abs/2312.14197; https://davidamitchell.github.io/Research/research/2026-05-18-rq4-1-agentic-loop-explanatory-reach.html]
- [inference] Verification improves only when it introduces a partially independent constraint, such as explicit condition isolation, deterministic policy rules, or a verifier external to the model, rather than another free-form judgment from the same model class. [source: https://aclanthology.org/2024.emnlp-main.714/; https://www.microsoft.com/en-us/msrc/blog/2025/07/how-microsoft-defends-against-indirect-prompt-injection-attacks; https://www.anthropic.com/research/trustworthy-agents]

#### E. Environmental shift and attack-specific robustness

- [fact] Amodei et al. list distributional shift as one of the practical safety problems that emerges when deployment conditions diverge from training conditions. [source: https://arxiv.org/abs/1606.06565]
- [fact] Ziegler et al. show that adversarial training improved robustness to the attacks they trained on without harming in-distribution performance, which demonstrates that robustness has to be constructed against specific adversarial surfaces rather than assumed. [source: https://arxiv.org/abs/2205.01663]
- [inference] Environmental shift and adversarial prompting have the same structural effect at the loop level when they create observations for which local heuristic confidence is a poor guide to causal validity. [source: https://arxiv.org/abs/1606.06565; https://arxiv.org/abs/2205.01663; https://davidamitchell.github.io/Research/research/2026-05-18-rq4-1-agentic-loop-explanatory-reach.html]
- [inference] Because the loop keeps conditioning on its own earlier outputs, even moderate initial misalignment can persist or widen when the environment does not supply a crisp independent contradiction. [source: https://arxiv.org/abs/2310.01798; https://www.anthropic.com/research/trustworthy-agents; https://davidamitchell.github.io/Research/research/2026-05-18-rq4-1-agentic-loop-explanatory-reach.html]

#### F. Formal error-propagation model

- [inference] Let `E_t` denote expected semantic error magnitude in the loop's working state at step `t`, let `i_t` denote fresh adversarial or shifted input at that step, let `m_t` denote amplification from path-dependent strategy and memory updates, and let `r_t` denote error removed by an independent verifier or environment signal. [source: https://www.anthropic.com/research/trustworthy-agents; https://arxiv.org/abs/1606.06565; https://arxiv.org/abs/2302.12173]
- [inference] A minimal propagation equation is `E_{t+1} = (1 + m_t - r_t)E_t + i_t`, where error grows when path dependence and persistence dominate correction, and shrinks only when an independent corrective signal removes more error than the loop reintroduces. [source: https://www.anthropic.com/research/trustworthy-agents; https://arxiv.org/abs/2310.01798; https://unit42.paloaltonetworks.com/indirect-prompt-injection-poisons-ai-longterm-memory/; https://davidamitchell.github.io/Research/research/2026-05-18-rq4-1-agentic-loop-explanatory-reach.html]
- [inference] When verification is performed by the same causally limited model on the same contaminated context, `r_t` approaches zero for blind-spot-consistent attacks, so the amplification factor across `N` steps approaches `A_N = product(1 + m_t)` plus the cumulative fresh-input terms. [source: https://arxiv.org/abs/2310.01798; https://arxiv.org/abs/2312.14197; https://arxiv.org/abs/2302.12173]
- [inference] In practical terms, prompt injection, poisoned retrieval, or state drift become most dangerous when they alter future branch selection or persistent memory, because then `m_t` remains positive for multiple subsequent steps rather than only for the current one. [source: https://unit42.paloaltonetworks.com/indirect-prompt-injection-poisons-ai-longterm-memory/; https://www.microsoft.com/en-us/msrc/blog/2025/07/how-microsoft-defends-against-indirect-prompt-injection-attacks; https://arxiv.org/abs/2302.12173]

#### G. Assumptions carried into synthesis

- [assumption] The planning, acting, observing, and adjusting loop described by Anthropic and analyzed in Research Question 4.1 is representative enough of common multi-step tool-using systems to support a structural conclusion about propagation. [justification: the core dependency is the reuse of model-generated state to choose later actions and interpret later observations, which appears across the cited loop descriptions; source: https://www.anthropic.com/research/trustworthy-agents; https://davidamitchell.github.io/Research/research/2026-05-18-rq4-1-agentic-loop-explanatory-reach.html]
- [assumption] Expected semantic error magnitude is a useful abstraction even though the cited papers measure attack success, accuracy, or qualitative failure rather than a single shared scalar. [justification: the abstraction is used only to express direction of propagation and the dependence on amplification versus correction, not to claim a universal numeric constant; source: https://arxiv.org/abs/2312.14197; https://arxiv.org/abs/2310.01798; https://arxiv.org/abs/2205.01663]
- [assumption] Unexpected environmental shift can be treated as propagation-equivalent to adversarial input at the loop level because both enter the system as misleading observations that are locally plausible but globally misaligned. [justification: the item studies how errors move once inside the loop, not whether the initial misalignment was maliciously crafted; source: https://arxiv.org/abs/1606.06565; https://arxiv.org/abs/2205.01663]

### §3 Reasoning

- [inference] The most direct evidence in this item concerns three grounded subclaims: multi-step tool-using systems are recurrent plan-act-observe loops, prompt injection exploits data-versus-instruction ambiguity, and intrinsic self-correction without external feedback is weak. [source: https://www.anthropic.com/research/trustworthy-agents; https://arxiv.org/abs/2302.12173; https://arxiv.org/abs/2312.14197; https://arxiv.org/abs/2310.01798]
- [inference] Combining those subclaims supports the central conclusion that a verification phase implemented as another free-form model judgment is usually a continuation of the same reasoning process rather than an independent check on it. [source: https://www.anthropic.com/research/trustworthy-agents; https://arxiv.org/abs/2310.01798; https://arxiv.org/abs/2312.14197]
- [inference] The formal propagation equation is a structural synthesis rather than a measured universal law, so the coefficients should be read as parameters that vary by architecture, tool surface, and correction channel. [source: https://arxiv.org/abs/1606.06565; https://arxiv.org/abs/2205.01663; https://arxiv.org/abs/2302.12173]
- [assumption] Cross-session memory poisoning is not required for the main conclusion, but it is treated as a valid upper-bound example of what happens when a local semantic error is allowed to persist into future orchestration prompts. [justification: the core argument only needs cross-step propagation, while the memory case shows the same mechanism over a longer horizon; source: https://unit42.paloaltonetworks.com/indirect-prompt-injection-poisons-ai-longterm-memory/]

### §4 Consistency Check

- [inference] The reviewed prompt-injection and self-correction sources all continue to treat tools, reflection, and memory as live risk surfaces rather than as automatic cures for the underlying failure modes. [source: https://arxiv.org/abs/2302.12173; https://arxiv.org/abs/2312.14197; https://arxiv.org/abs/2310.01798]
- [inference] The strongest apparent tension is between Huang et al., who show generic self-correction limits, and Wu et al., who show gains from key-condition verification, but the tension resolves because Wu et al. add a more structured verification procedure rather than validating naive self-assessment. [source: https://arxiv.org/abs/2310.01798; https://aclanthology.org/2024.emnlp-main.714/]
- [inference] No contradiction remains between adversarial-input papers and distributional-shift papers once both are treated as cases where high-likelihood observations fail to preserve the task's real semantics. [source: https://arxiv.org/abs/1412.6572; https://arxiv.org/abs/1606.06565; https://arxiv.org/abs/2302.12173]

### §5 Depth and Breadth Expansion

- [inference] Technically, architectures are especially exposed when contaminated context can influence not only one output but also tool permissions, memory summaries, or future orchestration prompts. [source: https://www.microsoft.com/en-us/msrc/blog/2025/07/how-microsoft-defends-against-indirect-prompt-injection-attacks; https://unit42.paloaltonetworks.com/indirect-prompt-injection-poisons-ai-longterm-memory/; https://www.anthropic.com/research/trustworthy-agents]
- [inference] Behaviourally, human reviewers can overestimate the value of a "verification" step when it is only another model-generated opinion, because the loop presents coherent plans and rationales even when no independent evidence channel has been added. [source: https://davidamitchell.github.io/Research/research/2026-04-30-human-bias-ai-trust-rlhf-sycophancy.html; https://arxiv.org/abs/2310.01798]
- [inference] Governance guidance from Anthropic, Microsoft, and the Cybersecurity and Infrastructure Security Agency (CISA) points toward the same operational pattern: keeping humans in control, constraining tool permissions, and adding external controls around agent behavior. [source: https://www.anthropic.com/research/trustworthy-agents; https://www.microsoft.com/en-us/msrc/blog/2025/07/how-microsoft-defends-against-indirect-prompt-injection-attacks; https://www.cisa.gov/resources-tools/resources/careful-adoption-agentic-ai-services]
- [inference] Operationally, propagation risk grows with action breadth and persistence, because the same initial semantic error can touch more systems, survive longer, and remain undetected until a costly contradiction appears. [source: https://unit42.paloaltonetworks.com/indirect-prompt-injection-poisons-ai-longterm-memory/; https://www.microsoft.com/en-us/msrc/blog/2025/07/how-microsoft-defends-against-indirect-prompt-injection-attacks; https://davidamitchell.github.io/Research/research/2026-05-08-integrated-cascading-failure-agentic-vs-generative-ai-risk.html]

### §6 Synthesis

**Executive summary:**

Adversarial inputs and environmental shifts propagate through multi-step tool-using Large Language Model systems mainly by corrupting the working state that later strategy and verification steps reuse, not by causing one isolated bad output. [inference; source: https://www.anthropic.com/research/trustworthy-agents; https://arxiv.org/abs/2302.12173; https://davidamitchell.github.io/Research/research/2026-05-18-rq4-1-agentic-loop-explanatory-reach.html]

When verification is implemented as another free-form judgment from the same model on the same context, it is usually not an independent check and cannot reliably detect blind-spot-consistent errors. [inference; source: https://arxiv.org/abs/2310.01798; https://aclanthology.org/2024.emnlp-main.714/; https://arxiv.org/abs/2312.14197]

Prompt injection, meaning malicious instructions embedded in content that the model later treats as authoritative instructions, is the clearest empirical example in this item because attacker text can be ingested as data, reinterpreted as instructions, and then propagated through tool calls, memory summaries, or future plans. [inference; source: https://owasp.org/www-community/attacks/PromptInjection; https://arxiv.org/abs/2302.12173; https://www.microsoft.com/en-us/msrc/blog/2025/07/how-microsoft-defends-against-indirect-prompt-injection-attacks; https://unit42.paloaltonetworks.com/indirect-prompt-injection-poisons-ai-longterm-memory/]

The best-supported formal picture is an amplification process in which error grows whenever path dependence and persistence outpace independent correction, which means agent loops without external verifiers mostly redistribute and sometimes magnify causal ignorance rather than curing it. [inference; source: https://arxiv.org/abs/2310.01798; https://arxiv.org/abs/2302.12173; https://davidamitchell.github.io/Research/research/2026-05-18-rq4-1-agentic-loop-explanatory-reach.html]

**Key findings:**

1. **Indirect prompt injection succeeds because tool-using Large Language Model applications routinely concatenate retrieved content with user instructions, leaving models unable to reliably separate informational context from actionable commands.** ([fact]; high confidence; source: https://arxiv.org/abs/2302.12173; https://arxiv.org/abs/2312.14197; https://owasp.org/www-community/attacks/PromptInjection)
2. **Once the loop's perception stage encodes a corrupted task state, strategy selection can remain internally coherent while optimizing for the wrong objective, so later tool calls inherit rather than repair the original semantic error.** ([inference]; medium confidence; source: https://www.anthropic.com/research/trustworthy-agents; https://davidamitchell.github.io/Research/research/2026-05-18-rq4-1-agentic-loop-explanatory-reach.html; https://arxiv.org/abs/2302.12173)
3. **Tool use and persistent memory can extend adversarial corruption beyond one response by letting a locally plausible mistake change external state and, in documented cases, influence later sessions.** ([inference]; medium confidence; source: https://www.microsoft.com/en-us/msrc/blog/2025/07/how-microsoft-defends-against-indirect-prompt-injection-attacks; https://unit42.paloaltonetworks.com/indirect-prompt-injection-poisons-ai-longterm-memory/; https://arxiv.org/abs/2302.12173)
4. **Generic self-verification by the same model class is not an independent safety layer, because intrinsic self-correction remains weak without external feedback and usually inspects the same contaminated context that produced the original mistake.** ([inference]; high confidence; source: https://arxiv.org/abs/2310.01798; https://arxiv.org/abs/2312.14197; https://davidamitchell.github.io/Research/research/2026-05-18-rq4-1-agentic-loop-explanatory-reach.html)
5. **Structured verification can recover some reasoning errors only when it introduces extra constraints such as explicit condition isolation, which shows that correction comes from added independence rather than from reflection alone.** ([inference]; medium confidence; source: https://aclanthology.org/2024.emnlp-main.714/; https://arxiv.org/abs/2310.01798)
6. **Unexpected environmental shifts and adversarial prompting are propagation-equivalent at the loop level when they both create observations that look familiar to the model while no longer preserving the environment's real causal structure.** ([inference]; medium confidence; source: https://arxiv.org/abs/1606.06565; https://arxiv.org/abs/2205.01663; https://davidamitchell.github.io/Research/research/2026-05-18-rq4-1-agentic-loop-explanatory-reach.html)
7. **A useful formal approximation is that expected semantic error grows across repeated steps whenever path-dependent amplification and persistence exceed the error removed by independent correction signals.** ([inference]; medium confidence; source: https://arxiv.org/abs/2310.01798; https://arxiv.org/abs/2302.12173; https://unit42.paloaltonetworks.com/indirect-prompt-injection-poisons-ai-longterm-memory/)

**Evidence map:**

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [fact] Indirect prompt injection succeeds because tool-using Large Language Model applications blur the boundary between retrieved content and instructions. | https://arxiv.org/abs/2302.12173; https://arxiv.org/abs/2312.14197; https://owasp.org/www-community/attacks/PromptInjection | high | Data-instruction ambiguity |
| [inference] Corrupted perception state propagates into strategy selection, so later tool choices remain coherent relative to the wrong state representation. | https://www.anthropic.com/research/trustworthy-agents; https://davidamitchell.github.io/Research/research/2026-05-18-rq4-1-agentic-loop-explanatory-reach.html; https://arxiv.org/abs/2302.12173 | medium | Path dependence |
| [inference] Tool use and persistent memory can extend local semantic corruption into external-state change and, in documented cases, cross-session persistence. | https://www.microsoft.com/en-us/msrc/blog/2025/07/how-microsoft-defends-against-indirect-prompt-injection-attacks; https://unit42.paloaltonetworks.com/indirect-prompt-injection-poisons-ai-longterm-memory/; https://arxiv.org/abs/2302.12173 | medium | Memory and action surface |
| [inference] Generic self-verification is not an independent safety layer when it reuses the same model and the same contaminated context. | https://arxiv.org/abs/2310.01798; https://arxiv.org/abs/2312.14197; https://davidamitchell.github.io/Research/research/2026-05-18-rq4-1-agentic-loop-explanatory-reach.html | high | Shared blind spots |
| [inference] Structured verification helps mainly when it adds an extra independent constraint rather than another unconstrained judgment. | https://aclanthology.org/2024.emnlp-main.714/; https://arxiv.org/abs/2310.01798 | medium | Condition isolation |
| [inference] Environmental shift and adversarial prompting are propagation-equivalent when both make locally plausible observations causally misleading. | https://arxiv.org/abs/1606.06565; https://arxiv.org/abs/2205.01663; https://davidamitchell.github.io/Research/research/2026-05-18-rq4-1-agentic-loop-explanatory-reach.html | medium | Shift versus attack |
| [inference] Expected semantic error grows across repeated steps when amplification and persistence exceed independent correction. | https://arxiv.org/abs/2310.01798; https://arxiv.org/abs/2302.12173; https://unit42.paloaltonetworks.com/indirect-prompt-injection-poisons-ai-longterm-memory/ | medium | Structural model |

**Assumptions:**

- [assumption] The Anthropic agent-loop description and Research Question 4.1 together represent the common structure of contemporary multi-step tool-using systems closely enough for a structural propagation model. [justification: the argument depends on recurrent state reuse across planning, acting, observing, and updating, which both sources describe directly; source: https://www.anthropic.com/research/trustworthy-agents; https://davidamitchell.github.io/Research/research/2026-05-18-rq4-1-agentic-loop-explanatory-reach.html]
- [assumption] Expected semantic error magnitude is an acceptable synthesis variable even though the cited studies report attack success, accuracy, or qualitative failure rather than one shared scalar measurement. [justification: the model is directional and comparative rather than calibrated to one benchmark; source: https://arxiv.org/abs/2312.14197; https://arxiv.org/abs/2310.01798; https://arxiv.org/abs/2205.01663]
- [assumption] Environmental shift can be grouped with adversarial input for propagation analysis because the mechanism under study is misleading observation entering a recurrent loop, not attacker intent itself. [justification: the item asks how error moves once inside the loop; source: https://arxiv.org/abs/1606.06565; https://arxiv.org/abs/2205.01663]

**Analysis:**

The strongest evidence in this item is on indirect prompt injection and intrinsic self-correction, because those claims rest on direct primary studies and official security guidance rather than on analogy alone. [inference; source: https://arxiv.org/abs/2302.12173; https://arxiv.org/abs/2312.14197; https://arxiv.org/abs/2310.01798; https://www.microsoft.com/en-us/msrc/blog/2025/07/how-microsoft-defends-against-indirect-prompt-injection-attacks]

The weakest element is the cross-domain bridge from classical adversarial examples to language-model agent loops, so Goodfellow et al. is used here to motivate the adversarial-input framing rather than as direct evidence about tool-using Large Language Model applications. [inference; source: https://arxiv.org/abs/1412.6572; https://arxiv.org/abs/2302.12173]

Wu et al. is the main rival interpretation because it shows that models can sometimes improve answers during verification, but its gains require key-condition isolation rather than unconstrained reflection, which supports rather than contradicts the independence claim. [inference; source: https://aclanthology.org/2024.emnlp-main.714/; https://arxiv.org/abs/2310.01798]

Another rival explanation is that failures arise only from overly permissive tools rather than from model-level causal limits, but Greshake, Yi, and Microsoft all show that misclassification of context as instructions already misroutes the loop before any one tool policy is discussed. [inference; source: https://arxiv.org/abs/2302.12173; https://arxiv.org/abs/2312.14197; https://www.microsoft.com/en-us/msrc/blog/2025/07/how-microsoft-defends-against-indirect-prompt-injection-attacks]

The formal propagation model is therefore best read as a structural synthesis: attack severity depends on path dependence, persistence, and verifier independence, not only on raw model accuracy at one isolated step. [inference; source: https://www.anthropic.com/research/trustworthy-agents; https://arxiv.org/abs/2310.01798; https://unit42.paloaltonetworks.com/indirect-prompt-injection-poisons-ai-longterm-memory/]

**Risks, gaps, uncertainties:**

- No cited source directly estimates one shared numeric amplification coefficient across full plan-act-verify loops, so the formal equation is structural rather than benchmark-calibrated. [inference; source: https://arxiv.org/abs/2310.01798; https://arxiv.org/abs/2312.14197]
- The cited evidence on cross-session memory poisoning in this item comes from a proof of concept and vendor guidance rather than from a multi-platform benchmark study. [fact; source: https://unit42.paloaltonetworks.com/indirect-prompt-injection-poisons-ai-longterm-memory/; https://www.microsoft.com/en-us/msrc/blog/2025/07/how-microsoft-defends-against-indirect-prompt-injection-attacks]
- The environmental-shift argument is strongest at the structural level and weaker at the level of one shared empirical benchmark that jointly measures shift, tool use, and verification failure in the same loop. [inference; source: https://arxiv.org/abs/1606.06565; https://arxiv.org/abs/2205.01663]

**Open questions:**

- Which benchmark design best measures full-loop propagation, including planning, tool use, memory, and verification, under both prompt injection and non-malicious environmental shift? [inference; source: https://arxiv.org/abs/2312.14197; https://www.anthropic.com/research/trustworthy-agents]
- How much independent correction is added by deterministic policy engines, typed tool interfaces, or formal verifiers compared with model-only verification? [inference; source: https://aclanthology.org/2024.emnlp-main.714/; https://www.microsoft.com/en-us/msrc/blog/2025/07/how-microsoft-defends-against-indirect-prompt-injection-attacks]
- When does memory persistence improve robustness by preserving context, and when does it mainly extend the lifetime of semantically corrupted state? [inference; source: https://unit42.paloaltonetworks.com/indirect-prompt-injection-poisons-ai-longterm-memory/; https://www.anthropic.com/research/trustworthy-agents]

### §7 Recursive Review

- Review result: pass
- Acronym audit: Research Question (RQ), Large Language Model (LLM), Open Worldwide Application Security Project (OWASP), Artificial Intelligence (AI), Cybersecurity and Infrastructure Security Agency (CISA)
- Domain-term audit: multi-step tool-using used instead of unexplained agentic shorthand in the main explanatory prose; prompt injection defined in Scope
- Claim audit: all visible claims in Research Skill Output labeled as fact, inference, or assumption
- Findings parity: matched to Section 6
- Confidence: medium

---

## Findings

### Executive Summary

Adversarial inputs and environmental shifts propagate through multi-step tool-using Large Language Model systems mainly by corrupting the working state that later strategy and verification steps reuse, not by causing one isolated bad output. [inference; source: https://www.anthropic.com/research/trustworthy-agents; https://arxiv.org/abs/2302.12173; https://davidamitchell.github.io/Research/research/2026-05-18-rq4-1-agentic-loop-explanatory-reach.html]

When verification is implemented as another free-form judgment from the same model on the same context, it is usually not an independent check and cannot reliably detect blind-spot-consistent errors. [inference; source: https://arxiv.org/abs/2310.01798; https://aclanthology.org/2024.emnlp-main.714/; https://arxiv.org/abs/2312.14197]

Prompt injection, meaning malicious instructions embedded in content that the model later treats as authoritative instructions, is the clearest empirical example in this item because attacker text can be ingested as data, reinterpreted as instructions, and then propagated through tool calls, memory summaries, or future plans. [inference; source: https://owasp.org/www-community/attacks/PromptInjection; https://arxiv.org/abs/2302.12173; https://www.microsoft.com/en-us/msrc/blog/2025/07/how-microsoft-defends-against-indirect-prompt-injection-attacks; https://unit42.paloaltonetworks.com/indirect-prompt-injection-poisons-ai-longterm-memory/]

The best-supported formal picture is an amplification process in which error grows whenever path dependence and persistence outpace independent correction, which means agent loops without external verifiers mostly redistribute and sometimes magnify causal ignorance rather than curing it. [inference; source: https://arxiv.org/abs/2310.01798; https://arxiv.org/abs/2302.12173; https://davidamitchell.github.io/Research/research/2026-05-18-rq4-1-agentic-loop-explanatory-reach.html]

### Key Findings

1. **Indirect prompt injection succeeds because tool-using Large Language Model applications routinely concatenate retrieved content with user instructions, leaving models unable to reliably separate informational context from actionable commands.** ([fact]; high confidence; source: https://arxiv.org/abs/2302.12173; https://arxiv.org/abs/2312.14197; https://owasp.org/www-community/attacks/PromptInjection)
2. **Once the loop's perception stage encodes a corrupted task state, strategy selection can remain internally coherent while optimizing for the wrong objective, so later tool calls inherit rather than repair the original semantic error.** ([inference]; medium confidence; source: https://www.anthropic.com/research/trustworthy-agents; https://davidamitchell.github.io/Research/research/2026-05-18-rq4-1-agentic-loop-explanatory-reach.html; https://arxiv.org/abs/2302.12173)
3. **Tool use and persistent memory can extend adversarial corruption beyond one response by letting a locally plausible mistake change external state and, in documented cases, influence later sessions.** ([inference]; medium confidence; source: https://www.microsoft.com/en-us/msrc/blog/2025/07/how-microsoft-defends-against-indirect-prompt-injection-attacks; https://unit42.paloaltonetworks.com/indirect-prompt-injection-poisons-ai-longterm-memory/; https://arxiv.org/abs/2302.12173)
4. **Generic self-verification by the same model class is not an independent safety layer, because intrinsic self-correction remains weak without external feedback and usually inspects the same contaminated context that produced the original mistake.** ([inference]; high confidence; source: https://arxiv.org/abs/2310.01798; https://arxiv.org/abs/2312.14197; https://davidamitchell.github.io/Research/research/2026-05-18-rq4-1-agentic-loop-explanatory-reach.html)
5. **Structured verification can recover some reasoning errors only when it introduces extra constraints such as explicit condition isolation, which shows that correction comes from added independence rather than from reflection alone.** ([inference]; medium confidence; source: https://aclanthology.org/2024.emnlp-main.714/; https://arxiv.org/abs/2310.01798)
6. **Unexpected environmental shifts and adversarial prompting are propagation-equivalent at the loop level when they both create observations that look familiar to the model while no longer preserving the environment's real causal structure.** ([inference]; medium confidence; source: https://arxiv.org/abs/1606.06565; https://arxiv.org/abs/2205.01663; https://davidamitchell.github.io/Research/research/2026-05-18-rq4-1-agentic-loop-explanatory-reach.html)
7. **A useful formal approximation is that expected semantic error grows across repeated steps whenever path-dependent amplification and persistence exceed the error removed by independent correction signals.** ([inference]; medium confidence; source: https://arxiv.org/abs/2310.01798; https://arxiv.org/abs/2302.12173; https://unit42.paloaltonetworks.com/indirect-prompt-injection-poisons-ai-longterm-memory/)

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [fact] Indirect prompt injection succeeds because tool-using Large Language Model applications blur the boundary between retrieved content and instructions. | https://arxiv.org/abs/2302.12173; https://arxiv.org/abs/2312.14197; https://owasp.org/www-community/attacks/PromptInjection | high | Data-instruction ambiguity |
| [inference] Corrupted perception state propagates into strategy selection, so later tool choices remain coherent relative to the wrong state representation. | https://www.anthropic.com/research/trustworthy-agents; https://davidamitchell.github.io/Research/research/2026-05-18-rq4-1-agentic-loop-explanatory-reach.html; https://arxiv.org/abs/2302.12173 | medium | Path dependence |
| [inference] Tool use and persistent memory can extend local semantic corruption into external-state change and, in documented cases, cross-session persistence. | https://www.microsoft.com/en-us/msrc/blog/2025/07/how-microsoft-defends-against-indirect-prompt-injection-attacks; https://unit42.paloaltonetworks.com/indirect-prompt-injection-poisons-ai-longterm-memory/; https://arxiv.org/abs/2302.12173 | medium | Memory and action surface |
| [inference] Generic self-verification is not an independent safety layer when it reuses the same model and the same contaminated context. | https://arxiv.org/abs/2310.01798; https://arxiv.org/abs/2312.14197; https://davidamitchell.github.io/Research/research/2026-05-18-rq4-1-agentic-loop-explanatory-reach.html | high | Shared blind spots |
| [inference] Structured verification helps mainly when it adds an extra independent constraint rather than another unconstrained judgment. | https://aclanthology.org/2024.emnlp-main.714/; https://arxiv.org/abs/2310.01798 | medium | Condition isolation |
| [inference] Environmental shift and adversarial prompting are propagation-equivalent when both make locally plausible observations causally misleading. | https://arxiv.org/abs/1606.06565; https://arxiv.org/abs/2205.01663; https://davidamitchell.github.io/Research/research/2026-05-18-rq4-1-agentic-loop-explanatory-reach.html | medium | Shift versus attack |
| [inference] Expected semantic error grows across repeated steps when amplification and persistence exceed independent correction. | https://arxiv.org/abs/2310.01798; https://arxiv.org/abs/2302.12173; https://unit42.paloaltonetworks.com/indirect-prompt-injection-poisons-ai-longterm-memory/ | medium | Structural model |

### Assumptions

- The Anthropic agent-loop description and Research Question 4.1 together represent the common structure of contemporary multi-step tool-using systems closely enough for a structural propagation model. [assumption; source: https://www.anthropic.com/research/trustworthy-agents; https://davidamitchell.github.io/Research/research/2026-05-18-rq4-1-agentic-loop-explanatory-reach.html]
- Expected semantic error magnitude is an acceptable synthesis variable even though the cited studies report attack success, accuracy, or qualitative failure rather than one shared scalar measurement. [assumption; source: https://arxiv.org/abs/2312.14197; https://arxiv.org/abs/2310.01798; https://arxiv.org/abs/2205.01663]
- Environmental shift can be grouped with adversarial input for propagation analysis because the mechanism under study is misleading observation entering a recurrent loop, not attacker intent itself. [assumption; source: https://arxiv.org/abs/1606.06565; https://arxiv.org/abs/2205.01663]

### Analysis

The strongest evidence in this item is on indirect prompt injection and intrinsic self-correction, because those claims rest on direct primary studies and official security guidance rather than on analogy alone. [inference; source: https://arxiv.org/abs/2302.12173; https://arxiv.org/abs/2312.14197; https://arxiv.org/abs/2310.01798; https://www.microsoft.com/en-us/msrc/blog/2025/07/how-microsoft-defends-against-indirect-prompt-injection-attacks]

The weakest element is the cross-domain bridge from classical adversarial examples to language-model agent loops, so Goodfellow et al. is used here to motivate the adversarial-input framing rather than as direct evidence about tool-using Large Language Model applications. [inference; source: https://arxiv.org/abs/1412.6572; https://arxiv.org/abs/2302.12173]

Wu et al. is the main rival interpretation because it shows that models can sometimes improve answers during verification, but its gains require key-condition isolation rather than unconstrained reflection, which supports rather than contradicts the independence claim. [inference; source: https://aclanthology.org/2024.emnlp-main.714/; https://arxiv.org/abs/2310.01798]

Another rival explanation is that failures arise only from overly permissive tools rather than from model-level causal limits, but Greshake, Yi, and Microsoft all show that misclassification of context as instructions already misroutes the loop before any one tool policy is discussed. [inference; source: https://arxiv.org/abs/2302.12173; https://arxiv.org/abs/2312.14197; https://www.microsoft.com/en-us/msrc/blog/2025/07/how-microsoft-defends-against-indirect-prompt-injection-attacks]

The formal propagation model is therefore best read as a structural synthesis: attack severity depends on path dependence, persistence, and verifier independence, not only on raw model accuracy at one isolated step. [inference; source: https://www.anthropic.com/research/trustworthy-agents; https://arxiv.org/abs/2310.01798; https://unit42.paloaltonetworks.com/indirect-prompt-injection-poisons-ai-longterm-memory/]

### Risks, Gaps, and Uncertainties

- No cited source directly estimates one shared numeric amplification coefficient across full plan-act-verify loops, so the formal equation is structural rather than benchmark-calibrated. [inference; source: https://arxiv.org/abs/2310.01798; https://arxiv.org/abs/2312.14197]
- The cited evidence on cross-session memory poisoning in this item comes from a proof of concept and vendor guidance rather than from a multi-platform benchmark study. [fact; source: https://unit42.paloaltonetworks.com/indirect-prompt-injection-poisons-ai-longterm-memory/; https://www.microsoft.com/en-us/msrc/blog/2025/07/how-microsoft-defends-against-indirect-prompt-injection-attacks]
- The environmental-shift argument is strongest at the structural level and weaker at the level of one shared empirical benchmark that jointly measures shift, tool use, and verification failure in the same loop. [inference; source: https://arxiv.org/abs/1606.06565; https://arxiv.org/abs/2205.01663]

### Open Questions

- Which benchmark design best measures full-loop propagation, including planning, tool use, memory, and verification, under both prompt injection and non-malicious environmental shift? [inference; source: https://arxiv.org/abs/2312.14197; https://www.anthropic.com/research/trustworthy-agents]
- How much independent correction is added by deterministic policy engines, typed tool interfaces, or formal verifiers compared with model-only verification? [inference; source: https://aclanthology.org/2024.emnlp-main.714/; https://www.microsoft.com/en-us/msrc/blog/2025/07/how-microsoft-defends-against-indirect-prompt-injection-attacks]
- When does memory persistence improve robustness by preserving context, and when does it mainly extend the lifetime of semantically corrupted state? [inference; source: https://unit42.paloaltonetworks.com/indirect-prompt-injection-poisons-ai-longterm-memory/; https://www.anthropic.com/research/trustworthy-agents]

---

## Output

- Type: knowledge
- Description: This item formalises adversarial propagation in multi-step tool-using Large Language Model systems as a path-dependent amplification problem, with prompt injection as the clearest empirical case and same-model verification as the main structural weak point. [inference; source: https://arxiv.org/abs/2302.12173; https://arxiv.org/abs/2310.01798; https://unit42.paloaltonetworks.com/indirect-prompt-injection-poisons-ai-longterm-memory/]
- Links:
  - https://arxiv.org/abs/2302.12173
  - https://arxiv.org/abs/2310.01798
  - https://arxiv.org/abs/2312.14197
