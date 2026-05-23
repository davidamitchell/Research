---
review_count: 2
title: "Research Question 5.2: Flexibility vs. Predictability, How the Agentic Tradeoff Affects Auditability and Formal Verification in Production Pipelines"
added: 2026-05-18T19:40:00+00:00
status: completed
priority: high
blocks:
  - 2026-05-18-agentic-production-tradeoffs
started: 2026-05-19T20:02:20+00:00
completed: 2026-05-19T20:29:09+00:00
output: [knowledge]
themes: [agentic-ai, ai-architecture, mlops-deployment, governance-policy, formal-verification]
cites:
  - 2026-05-18-rq5-1-stochastic-vs-deterministic-failures
  - 2026-05-18-agentic-explainability-vs-traditional
  - 2026-04-26-ai-lowcode-observability-telemetry-governance
  - 2026-05-09-governance-policy-determinism-vs-stochastic-llm
related:
  - 2026-05-09-llm-determinism-limits-temperature-zero
  - 2026-05-18-rq4-2-adversarial-error-propagation
  - 2026-05-18-rq2-4-causal-hierarchy-formal-limits
superseded_by: ~
supersedes: ~
item_type: primary
confidence: medium
versions:
  - version: "1.0"
    sha: 14f9a38a97c8f40ccac36b5bd097d69d289590dc
    changed: 2026-05-19
    progress: progress/2026-05-19-rq5-2-flexibility-vs-predictability-auditability.md
    summary: "Initial completion"
---

# Research Question 5.2: Flexibility vs. Predictability, How the Agentic Tradeoff Affects Auditability and Formal Verification in Production Pipelines

## Research Question

In a production pipeline with uncontrolled inputs, how does the trade-off between the flexibility of an agentic system and the predictability of a deterministic execution model affect the auditability and formal verification of the system's runtime state?

## Scope

**In scope:**
- Lineage tracking: can the decision path of an agentic system be reconstructed post hoc with sufficient fidelity for audit?
- State-space growth in agentic systems: does branching from Large Language Model (LLM) outputs make formal verification materially harder than for deterministic workflows?
- Non-Deterministic Finite Automata (NDFA), Markov Decision Process (MDP), and related state-transition abstractions for runtime verification of agentic pipelines
- Formal verification approaches, especially model checking, for deterministic, probabilistic, and nondeterministic workflow abstractions
- Regulatory and compliance implications of partially reconstructable or only approximately verifiable runtime state

**Out of scope:**
- Clause-by-clause treatment of individual compliance regimes beyond the logging and traceability implications of the European Union (EU) Artificial Intelligence (AI) Act
- Mechanistic interpretability of model internals in isolation from end-to-end pipeline behavior
- A claim that deterministic distributed systems are globally transparent without observability work

**Constraints:** Builds directly on Research Question 5.1, must connect back to formal verification theory from the seeded model-checking sources, must check the seeded sources even where they are replaced by accessible equivalents, and must use URL-backed citations throughout.

## Context

- Research Question 5.1 already established that stochastic agent pipelines and deterministic coded systems fail differently on the same unvalidated input, with agent pipelines more prone to silent semantic drift and branch variance. [fact; source: https://davidamitchell.github.io/Research/research/2026-05-18-rq5-1-stochastic-vs-deterministic-failures.html]
- The explainability comparison already established that deterministic software loses global transparency at production scale but retains stronger local replayability than LLM-based systems. [fact; source: https://davidamitchell.github.io/Research/research/2026-05-18-agentic-explainability-vs-traditional.html]
- Prior observability work in this repository concluded that governance-grade reconstruction depends on trace, payload, and audit records that preserve identity, correlation, tool, and state lineage across system boundaries. [fact; source: https://davidamitchell.github.io/Research/research/2026-04-26-ai-lowcode-observability-telemetry-governance.html]
- The unresolved question is therefore narrower than "are agents risky": it is whether increased runtime flexibility pushes audit and verification from exact replay and finite-state proof toward partial reconstruction, bounded abstractions, and approximate checking. [inference; source: https://davidamitchell.github.io/Research/research/2026-05-18-rq5-1-stochastic-vs-deterministic-failures.html; https://davidamitchell.github.io/Research/research/2026-05-18-agentic-explainability-vs-traditional.html; https://davidamitchell.github.io/Research/research/2026-04-26-ai-lowcode-observability-telemetry-governance.html]

## Approach

1. Formalise what an audit trail must capture to reconstruct one agent run, including prompts, retrieval, tool use, model configuration, outputs, and side effects.
2. Compare the formal models that current verification tools actually support, including finite-state, probabilistic, and nondeterministic state-transition systems.
3. Distinguish what can be verified exactly, what can only be verified after abstraction, and what remains approximate or runtime-only in agentic pipelines.
4. Connect those technical limits to regulated operating environments that require traceability, contestability, and durable event logs.
5. Synthesize the flexibility-predictability frontier for production design.

## Sources

**Consulted:**

- [x] [Anthropic (2026) Trustworthy agents](https://www.anthropic.com/research/trustworthy-agents) - agent definition, self-directed loop, and oversight surfaces.
- [x] [OpenTelemetry Generative Artificial Intelligence spans](https://opentelemetry.io/docs/specs/semconv/gen-ai/gen-ai-spans/) - span structure for model calls, tool calls, inputs, outputs, and configuration.
- [x] [OpenTelemetry Generative Artificial Intelligence events](https://opentelemetry.io/docs/specs/semconv/gen-ai/gen-ai-events/) - event-level capture of request and response details.
- [x] [OpenTelemetry Generative Artificial Intelligence attribute registry](https://opentelemetry.io/docs/specs/semconv/registry/attributes/gen-ai/) - canonical fields for conversation, retrieval, tool, and model telemetry.
- [x] [European Commission Artificial Intelligence (AI) Act Service Desk Article 12 Record-keeping](https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-12) - accessible text of the EU Artificial Intelligence Act logging and traceability requirement.
- [x] [PRISM Probabilistic Model Checker](https://www.prismmodelchecker.org/) - overview of supported probabilistic verification models and property classes.
- [x] [PRISM manual introduction](https://www.prismmodelchecker.org/manual/Main/AllOnOnePage) - formal verification framing, supported models, and temporal logics.
- [x] [PRISM language introduction](https://www.prismmodelchecker.org/manual/ThePRISMLanguage/Introduction) - state-based model structure and probabilistic commands.
- [x] [PRISM local nondeterminism](https://www.prismmodelchecker.org/manual/ThePRISMLanguage/LocalNondeterminism) - explicit treatment of nondeterministic choices in Markov Decision Processes.
- [x] [PRISM property specification introduction](https://www.prismmodelchecker.org/manual/PropertySpecification/Introduction) - supported property languages and quantitative queries.
- [x] [PRISM statistical model checking](https://www.prismmodelchecker.org/manual/RunningPRISM/StatisticalModelChecking) - approximate checking limits on large or nondeterministic models.
- [x] [Storm model checker](https://www.stormchecker.org/) - current probabilistic and partially observable verification targets.
- [x] [Holzmann (2003) SPIN Model Checker book extras](https://spinroot.com/spin/Doc/Book_extras/) - explicit-state model-checking topics including abstraction, partial-order reduction, and state compression.
- [x] [Dong et al. (2024) AgentOps: Enabling Observability of Large Language Model Agents](https://arxiv.org/abs/2411.05285) - peer-reviewed taxonomy of artifacts and data that should be traced through the agent lifecycle.
- [x] [Abdelnabi et al. (2023) Indirect Prompt Injection in Large Language Model-Integrated Applications](https://arxiv.org/abs/2302.12173) - evidence that uncontrolled data can become executable instruction context.
- [x] [Huang et al. (2024) Large Language Models Cannot Self-Correct Reasoning Yet](https://arxiv.org/abs/2310.01798) - evidence that intrinsic self-correction is unreliable without external feedback.
- [x] [Heim et al. (2025) A Guide to Failure in Machine Learning](https://arxiv.org/abs/2503.00563) - reliability and robustness framing for machine-learning failure analysis.
- [x] [Mitchell (2026) Research Question 5.1: Stochastic versus Deterministic Failure Modes on Identical Unvalidated Inputs](https://davidamitchell.github.io/Research/research/2026-05-18-rq5-1-stochastic-vs-deterministic-failures.html) - immediate prior repository item on failure signatures and replayability.
- [x] [Mitchell (2026) Are Multi-Step Large Language Model-Based Systems Inherently Less Explainable Than Equivalently Scoped Deterministic Software Systems?](https://davidamitchell.github.io/Research/research/2026-05-18-agentic-explainability-vs-traditional.html) - prior repository item on local replayability versus global opacity.
- [x] [Mitchell (2026) What observability and telemetry model is required to govern Artificial Intelligence and low-code systems at scale?](https://davidamitchell.github.io/Research/research/2026-04-26-ai-lowcode-observability-telemetry-governance.html) - prior repository item on governance-grade traceability fields.
- [x] [Mitchell (2026) Governance Policy Application: Deterministic Requirements vs Stochastic Large Language Model Elements](https://davidamitchell.github.io/Research/research/2026-05-09-governance-policy-determinism-vs-stochastic-llm.html) - prior repository item on deterministic control surfaces in governed decisions.

**Identified but not consulted:**

- [ ] [Clarke et al. (2018) Model Checking, MIT Press](https://mitpress.mit.edu/9780262038553/model-checking/) - seeded canonical textbook locator checked, but the accessible evidence extracted for this item came from PRISM, Storm, and SPIN documentation plus accessible papers.
- [ ] [Baier and Katoen (2008) Principles of Model Checking, MIT Press](https://mitpress.mit.edu/9780262026499/principles-of-model-checking/) - seeded canonical textbook locator checked, but the publisher page did not yield extractable content in this environment.

## Related

- [Research Question 5.1: Stochastic versus Deterministic Failure Modes on Identical Unvalidated Inputs](https://davidamitchell.github.io/Research/research/2026-05-18-rq5-1-stochastic-vs-deterministic-failures.html)
- [Are Multi-Step Large Language Model-Based Systems Inherently Less Explainable Than Equivalently Scoped Deterministic Software Systems?](https://davidamitchell.github.io/Research/research/2026-05-18-agentic-explainability-vs-traditional.html)
- [What observability and telemetry model is required to govern Artificial Intelligence and low-code systems at scale?](https://davidamitchell.github.io/Research/research/2026-04-26-ai-lowcode-observability-telemetry-governance.html)

---

## Research Skill Output

*(Full output from running the research skill. Sections 0 to 5 are the investigation, and section 6 seeds the Findings section below.)*

### §0 Initialise

- Question: in a production pipeline with uncontrolled inputs, how does the flexibility of an agentic system affect auditability and formal verification compared with a more predictable deterministic execution model?
- Scope: runtime lineage reconstruction, state-transition abstractions, formal verification boundaries, and regulated-operation implications.
- Constraints: full-mode investigation, seeded-source check completed, URL-backed citations only, and mirrored synthesis plus Findings output required.
- Output: knowledge, specifically a structured synthesis with executive summary, key findings, evidence map, assumptions, analysis, risks and gaps, open questions, and output links.
- Prior completed items consulted: https://davidamitchell.github.io/Research/research/2026-05-18-rq5-1-stochastic-vs-deterministic-failures.html ; https://davidamitchell.github.io/Research/research/2026-05-18-agentic-explainability-vs-traditional.html ; https://davidamitchell.github.io/Research/research/2026-04-26-ai-lowcode-observability-telemetry-governance.html ; https://davidamitchell.github.io/Research/research/2026-05-09-governance-policy-determinism-vs-stochastic-llm.html

### §1 Question Decomposition

1. Audit reconstruction requirements
   1.1 Which fields must be recorded to reconstruct one run of an agentic pipeline?
   1.2 Which of those fields are specific to Large Language Model tool-use systems rather than generic software logs?
2. Formal model choice
   2.1 Which finite-state and probabilistic models do current verification tools support directly?
   2.2 Where does nondeterminism enter those models?
   2.3 Which supported abstractions are closest to open-loop agent behavior?
3. Verification boundary
   3.1 What can deterministic model checking prove exactly on finite abstractions?
   3.2 What can probabilistic model checking prove on nondeterministic or stochastic abstractions?
   3.3 When does the problem move from exact verification to approximation or runtime monitoring?
4. Agentic control-surface effects
   4.1 How do autonomy, tool access, and uncontrolled inputs enlarge the runtime state that must be audited?
   4.2 Why is self-explanation or self-correction an insufficient substitute for trace reconstruction?
5. Production synthesis
   5.1 How does auditability change as flexibility increases?
   5.2 How does formal verifiability change as flexibility increases?
   5.3 What design pattern follows for regulated production environments?

### §2 Investigation

#### Access notes

- access_note_mitpress_locators: checked; direct content extraction unavailable in this environment.
- access_note_eurlex_locator: checked; extracted Article 12 wording taken from the European Commission service-desk mirror.

#### A. Prior completed-item sweep

- [fact] Research Question 5.1 concluded that stochastic agent pipelines can produce different branch paths and different failure surfaces on identical unvalidated inputs, while deterministic systems retain stronger replayability from the same initial state. [source: https://davidamitchell.github.io/Research/research/2026-05-18-rq5-1-stochastic-vs-deterministic-failures.html]
- [fact] The explainability comparison concluded that deterministic distributed systems lose global transparency at scale but preserve stronger local replayability than LLM-based systems. [source: https://davidamitchell.github.io/Research/research/2026-05-18-agentic-explainability-vs-traditional.html]
- [fact] The observability item concluded that governance-grade reconstruction requires cross-system traces, payload logs, decision logs, attribution fields, and the ability to correlate events across boundaries. [source: https://davidamitchell.github.io/Research/research/2026-04-26-ai-lowcode-observability-telemetry-governance.html]
- [inference] The present item therefore turns the comparison from "which class fails" into "which class still supports post hoc reconstruction and tractable proof once failure occurs in a real pipeline." [source: https://davidamitchell.github.io/Research/research/2026-05-18-rq5-1-stochastic-vs-deterministic-failures.html; https://davidamitchell.github.io/Research/research/2026-05-18-agentic-explainability-vs-traditional.html; https://davidamitchell.github.io/Research/research/2026-04-26-ai-lowcode-observability-telemetry-governance.html]

#### B. Audit lineage requires richer state capture for agentic pipelines

- [fact] OpenTelemetry's generative Artificial Intelligence inference span includes operation name, provider, request model, optional seed, conversation identifier, input messages, output messages, system instructions, tool definitions, finish reasons, token usage, and error type. [source: https://opentelemetry.io/docs/specs/semconv/gen-ai/gen-ai-spans/]
- [fact] The OpenTelemetry attribute registry also defines retrieval-document fields, retrieval-query text, data-source identifiers, tool-call identifiers, tool-call arguments, and tool-call results. [source: https://opentelemetry.io/docs/specs/semconv/registry/attributes/gen-ai/]
- [fact] OpenTelemetry's generative Artificial Intelligence events specification says request and response details may be captured as separate events so that inputs and outputs can be stored independently from the main trace. [source: https://opentelemetry.io/docs/specs/semconv/gen-ai/gen-ai-events/]
- [fact] Article 12 of the EU Artificial Intelligence Act requires high-risk systems to allow automatic recording of events over the lifetime of the system and to record events relevant to traceability appropriate to the intended purpose. [source: https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-12]
- [fact] Article 12 also specifies concrete minimum fields for some high-risk systems, including period of use, reference database, matched input data, and the identity of the humans who verified results. [source: https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-12]
- [fact] Dong et al. argue that agent observability needs lifecycle tracing of agent artifacts and associated data because autonomous and non-deterministic behavior raises safety concerns. [source: https://arxiv.org/abs/2411.05285]
- [inference] A reconstructable audit trail for an agentic pipeline therefore needs at least actor identity, conversation or run identity, model and configuration identity, input and retrieval lineage, tool-call lineage, output lineage, and error or override lineage, because no single log stream captures the whole decision path. [source: https://opentelemetry.io/docs/specs/semconv/gen-ai/gen-ai-spans/; https://opentelemetry.io/docs/specs/semconv/registry/attributes/gen-ai/; https://opentelemetry.io/docs/specs/semconv/gen-ai/gen-ai-events/; https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-12; https://arxiv.org/abs/2411.05285; https://davidamitchell.github.io/Research/research/2026-04-26-ai-lowcode-observability-telemetry-governance.html]

#### C. Current verification tooling supports finite-state and probabilistic state-transition models, not raw open-ended language traces

- [fact] PRISM defines probabilistic model checking as a formal verification technique in which a precise mathematical model is analysed against temporal-logic properties. [source: https://www.prismmodelchecker.org/manual/Main/AllOnOnePage]
- [fact] PRISM directly supports Discrete-Time Markov Chains (DTMCs), Continuous-Time Markov Chains (CTMCs), Markov Decision Processes (MDPs), probabilistic automata, probabilistic timed automata, and partially observable variants. [source: https://www.prismmodelchecker.org/; https://www.prismmodelchecker.org/manual/Main/AllOnOnePage]
- [fact] PRISM models use explicit state variables and commands whose guards and updates define transitions, with probabilities or rates attached to the updates. [source: https://www.prismmodelchecker.org/manual/ThePRISMLanguage/Introduction]
- [fact] PRISM treats overlapping commands in MDPs as local nondeterminism, which creates nondeterministic choices between distributions in a state. [source: https://www.prismmodelchecker.org/manual/ThePRISMLanguage/LocalNondeterminism]
- [fact] PRISM's property language supports probabilistic and temporal queries such as eventual termination, bounded error probability, maximum probability over an MDP, and long-run state occupancy. [source: https://www.prismmodelchecker.org/manual/PropertySpecification/Introduction]
- [fact] Storm likewise supports Markov chains, MDPs, Markov automata, partially observable Markov models, and model-checking queries such as reachability, reach-avoid, Probabilistic Computation Tree Logic (PCTL), Continuous Stochastic Logic (CSL), and Linear Temporal Logic (LTL). [source: https://www.stormchecker.org/]
- [inference] Current mainstream quantitative verifiers therefore operate on finite or finitised state-transition abstractions, not on unrestricted natural-language reasoning traces or unconstrained environment state directly. [source: https://www.prismmodelchecker.org/; https://www.prismmodelchecker.org/manual/Main/AllOnOnePage; https://www.stormchecker.org/]

#### D. Exact checking remains possible only after aggressive abstraction, even for deterministic systems

- [fact] Holzmann's SPIN materials dedicate separate treatment to design abstraction, controlling complexity, search optimization, partial-order reduction, state compression, and lowering verification complexity. [source: https://spinroot.com/spin/Doc/Book_extras/]
- [fact] PRISM says statistical model checking is useful on very large models when normal model checking is infeasible, because it samples random paths rather than explicitly constructing the full model. [source: https://www.prismmodelchecker.org/manual/RunningPRISM/StatisticalModelChecking]
- [fact] PRISM also states that statistical model checking is not well suited to models that exhibit nondeterminism, such as MDPs, because random paths are not well defined for those models. [source: https://www.prismmodelchecker.org/manual/RunningPRISM/StatisticalModelChecking]
- [inference] State-space explosion is therefore a baseline verification problem for complex deterministic systems, and agentic systems inherit that baseline before adding stochastic branching and tool-mediated state growth. [source: https://spinroot.com/spin/Doc/Book_extras/; https://www.prismmodelchecker.org/manual/RunningPRISM/StatisticalModelChecking]
- [inference] The practical consequence is not that deterministic systems are easy and agentic systems are impossible, but that deterministic systems usually admit tighter abstractions with smaller semantic loss because the control flow and update rules are explicit before runtime. [source: https://www.prismmodelchecker.org/manual/ThePRISMLanguage/Introduction; https://spinroot.com/spin/Doc/Book_extras/; https://davidamitchell.github.io/Research/research/2026-05-18-agentic-explainability-vs-traditional.html]

#### E. Agentic flexibility enlarges the runtime state that must be audited and approximated

- [fact] Anthropic defines an agent as a model that directs its own processes and tool use in a self-directed loop that plans, acts, observes the result, adjusts, and repeats. [source: https://www.anthropic.com/research/trustworthy-agents]
- [fact] Anthropic also says agent behavior depends on four layers: the model, a harness of instructions and guardrails, tools, and the environment in which the agent runs. [source: https://www.anthropic.com/research/trustworthy-agents]
- [fact] Anthropic says the autonomy that makes agents useful also creates more room to misread user intent and take actions with unintended consequences. [source: https://www.anthropic.com/research/trustworthy-agents]
- [fact] Abdelnabi et al. show that indirect prompt injection blurs the line between data and instructions and can manipulate application functionality and downstream Application Programming Interface (API) calls. [source: https://arxiv.org/abs/2302.12173]
- [fact] Huang et al. report that intrinsic self-correction without external feedback is unreliable and can even degrade performance. [source: https://arxiv.org/abs/2310.01798]
- [fact] Heim et al. argue that unexpected machine-learning failure should be analysed through reliability and robustness rather than by assuming one uniform failure mechanism. [source: https://arxiv.org/abs/2503.00563]
- [inference] In an agentic pipeline with uncontrolled inputs, runtime state includes not just code location and variable values but also prompt content, retrieved external text, model-selected branch actions, tool outputs, and environment-side effects. [source: https://www.anthropic.com/research/trustworthy-agents; https://arxiv.org/abs/2302.12173; https://opentelemetry.io/docs/specs/semconv/registry/attributes/gen-ai/; https://davidamitchell.github.io/Research/research/2026-05-18-rq5-1-stochastic-vs-deterministic-failures.html]
- [inference] Self-explanation or self-correction is therefore not a substitute for audit lineage, because the reconstructable path has to come from durable traces of what happened, not only from the model's later narrative about what it thinks happened. [source: https://arxiv.org/abs/2310.01798; https://opentelemetry.io/docs/specs/semconv/gen-ai/gen-ai-events/; https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-12]

#### F. The flexibility-predictability frontier shifts assurance from proof toward bounded abstraction and governance controls

- [fact] PRISM and Storm can verify probabilistic reachability, temporal, reward, and worst-case properties on explicit probabilistic or nondeterministic models. [source: https://www.prismmodelchecker.org/; https://www.prismmodelchecker.org/manual/PropertySpecification/Introduction; https://www.stormchecker.org/]
- [fact] Governance-oriented prior work in this repository concluded that consequential policy decisions are most defensible when deterministic enforcement and evidence logging sit at the final control surface. [source: https://davidamitchell.github.io/Research/research/2026-05-09-governance-policy-determinism-vs-stochastic-llm.html]
- [fact] The same prior work on observability concluded that provable governance depends on retaining enough trace and decision context to reconstruct what system acted, with which permissions, on what inputs, and under which controls. [source: https://davidamitchell.github.io/Research/research/2026-04-26-ai-lowcode-observability-telemetry-governance.html]
- [inference] Agentic pipelines are not formally unverifiable in principle, but the verifiable object is a bounded abstraction such as an MDP, probabilistic automaton, or monitored control shell rather than the full semantic content of an open-ended run. [source: https://www.prismmodelchecker.org/; https://www.prismmodelchecker.org/manual/ThePRISMLanguage/LocalNondeterminism; https://www.stormchecker.org/; https://spinroot.com/spin/Doc/Book_extras/]
- [inference] As flexibility increases through open-ended prompting, retrieval, tool choice, retries, and mutable external state, exact replay and exhaustive proof decrease while dependence on rich telemetry, explicit constraints, and deterministic final decision surfaces increases. [source: https://www.anthropic.com/research/trustworthy-agents; https://opentelemetry.io/docs/specs/semconv/registry/attributes/gen-ai/; https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-12; https://davidamitchell.github.io/Research/research/2026-05-09-governance-policy-determinism-vs-stochastic-llm.html]
- [assumption] This item treats "formal verification of runtime state" as verification of a finite abstraction of the runtime state rather than verification of the full semantic content of every generated token sequence, because the accessible verifier sources are all state-transition tools that require finitised models. [source: https://www.prismmodelchecker.org/manual/Main/AllOnOnePage; https://www.stormchecker.org/]

### §3 Reasoning

- [inference] The available tool sources do not support the strong claim that stochastic or agentic systems are beyond all formal analysis, because PRISM and Storm explicitly support probabilistic and nondeterministic models. [source: https://www.prismmodelchecker.org/; https://www.stormchecker.org/]
- [inference] The defensible distinction is instead between direct verification of an already finite transition system and verification of a lossy abstraction of a more open-ended agentic workflow. [source: https://www.prismmodelchecker.org/manual/ThePRISMLanguage/Introduction; https://www.prismmodelchecker.org/manual/RunningPRISM/StatisticalModelChecking; https://www.anthropic.com/research/trustworthy-agents]
- [inference] Auditability follows the same pattern: deterministic systems can often reconstruct execution from fewer dimensions of state, while agentic systems require wider lineage capture because prompts, retrieved context, tool outputs, and environment state all matter to the resulting path. [source: https://opentelemetry.io/docs/specs/semconv/gen-ai/gen-ai-spans/; https://opentelemetry.io/docs/specs/semconv/registry/attributes/gen-ai/; https://davidamitchell.github.io/Research/research/2026-04-26-ai-lowcode-observability-telemetry-governance.html]
- [inference] This makes the frontier a shift in assurance mode rather than a binary jump from "verifiable" to "not verifiable": the more flexible the pipeline, the more assurance comes from constrained shells, runtime telemetry, and partial proofs over abstractions. [source: https://www.prismmodelchecker.org/manual/RunningPRISM/StatisticalModelChecking; https://spinroot.com/spin/Doc/Book_extras/; https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-12]

### §4 Consistency Check

- [fact] Tension: probabilistic model checkers already verify systems with randomness and nondeterminism. [source: https://www.prismmodelchecker.org/; https://www.stormchecker.org/]
- [inference] Resolution: that does not contradict the main claim, because those verifiers require explicit finite-state abstractions, whereas open-ended agentic pipelines expose additional semantic and environmental state that must first be abstracted away. [source: https://www.prismmodelchecker.org/manual/ThePRISMLanguage/Introduction; https://www.anthropic.com/research/trustworthy-agents]
- [fact] Tension: statistical model checking can scale to models that normal model checking cannot. [source: https://www.prismmodelchecker.org/manual/RunningPRISM/StatisticalModelChecking]
- [inference] Resolution: statistical model checking weakens the guarantee from exhaustive proof to controlled approximation, and PRISM warns that it is not well suited to nondeterministic models such as MDPs without arbitrary randomization choices. [source: https://www.prismmodelchecker.org/manual/RunningPRISM/StatisticalModelChecking]
- [fact] Tension: deterministic distributed systems also need traces and post hoc reconstruction. [source: https://spinroot.com/spin/Doc/Book_extras/; https://davidamitchell.github.io/Research/research/2026-05-18-agentic-explainability-vs-traditional.html]
- [inference] Resolution: the comparison is therefore relative, not absolute, and the retained asymmetry is local replayability and smaller abstraction loss on deterministic control surfaces. [source: https://davidamitchell.github.io/Research/research/2026-05-18-agentic-explainability-vs-traditional.html; https://www.prismmodelchecker.org/manual/ThePRISMLanguage/Introduction]

### §5 Depth and Breadth Expansion

- [inference] Technical lens: the most relevant formal boundary is not whether randomness exists, but whether the modeled system can be finitised without discarding the very semantics that matter for the property being checked. [source: https://www.prismmodelchecker.org/manual/Main/AllOnOnePage; https://www.stormchecker.org/]
- [inference] Regulatory lens: Article 12 does not require theorem-proving over full semantic state, but it does require enough logging to make the system's functioning traceable for the intended purpose, which raises the implementation burden as agent autonomy grows. [source: https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-12]
- [inference] Economic lens: richer telemetry and constrained control shells are not optional overhead for flexible agents, because they substitute for the stronger replayability that deterministic workflows often get "for free" from explicit code paths. [source: https://opentelemetry.io/docs/specs/semconv/registry/attributes/gen-ai/; https://davidamitchell.github.io/Research/research/2026-04-26-ai-lowcode-observability-telemetry-governance.html]
- [inference] Historical lens: explicit-state model checking already developed abstraction, reduction, and compression techniques for deterministic concurrency because exact global reasoning was hard even there, which means agentic systems extend an old tractability problem rather than creating a wholly new one. [source: https://spinroot.com/spin/Doc/Book_extras/]
- [inference] Behavioural lens: if agents can misread intent, receive adversarial instructions through data, and fail to self-correct reliably, then human reviewers need replayable traces of actual events rather than trust in the model's own retrospective explanation. [source: https://www.anthropic.com/research/trustworthy-agents; https://arxiv.org/abs/2302.12173; https://arxiv.org/abs/2310.01798]

### §6 Synthesis

**Executive summary:**

Agentic flexibility reduces exact auditability and full-state formal verifiability unless the system is wrapped in a constrained, trace-rich control shell that records the run well enough to reconstruct what happened and abstracts the workflow into a finite verification target. [inference; source: https://opentelemetry.io/docs/specs/semconv/gen-ai/gen-ai-spans/; https://www.prismmodelchecker.org/manual/Main/AllOnOnePage; https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-12]

Deterministic pipelines also face state-space and observability limits, but current verification tools fit them more naturally because their control flow and update rules are explicit before runtime, which keeps abstraction loss lower and replayability stronger. [inference; source: https://spinroot.com/spin/Doc/Book_extras/; https://www.prismmodelchecker.org/manual/ThePRISMLanguage/Introduction; https://davidamitchell.github.io/Research/research/2026-05-18-agentic-explainability-vs-traditional.html]

Probabilistic model checking shows that stochastic systems are not outside formal methods altogether, yet the tractable object is a finitised Markov-style abstraction such as an MDP rather than the full semantic content of an open-ended agent run. [inference; source: https://www.prismmodelchecker.org/; https://www.prismmodelchecker.org/manual/ThePRISMLanguage/LocalNondeterminism; https://www.stormchecker.org/]

For regulated production use, the practical design implication is to keep deterministic authority at the final consequential control surface while allowing agentic components upstream only when prompts, retrieval, tool use, outputs, and overrides are durably logged. [inference; source: https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-12; https://davidamitchell.github.io/Research/research/2026-05-09-governance-policy-determinism-vs-stochastic-llm.html; https://davidamitchell.github.io/Research/research/2026-04-26-ai-lowcode-observability-telemetry-governance.html]

**Key findings:**

1. **A production-grade audit trail for an agentic pipeline must capture conversation identity, model identity, prompt and instruction state, retrieval lineage, tool-call lineage, outputs, and errors, because current observability standards and agent-observability literature split those facts across traces, events, attributes, and lifecycle artifacts rather than one canonical log record.** ([inference]; medium confidence; source: https://opentelemetry.io/docs/specs/semconv/gen-ai/gen-ai-spans/; https://opentelemetry.io/docs/specs/semconv/gen-ai/gen-ai-events/; https://opentelemetry.io/docs/specs/semconv/registry/attributes/gen-ai/; https://arxiv.org/abs/2411.05285; https://davidamitchell.github.io/Research/research/2026-04-26-ai-lowcode-observability-telemetry-governance.html)
2. **The European Union Artificial Intelligence Act's automatic logging requirement means that recorded event traces, not only post hoc textual explanations, are needed where a high-risk system's functioning must later be reconstructed for monitoring or investigation.** ([inference]; medium confidence; source: https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-12; https://davidamitchell.github.io/Research/research/2026-04-26-ai-lowcode-observability-telemetry-governance.html)
3. **Current mainstream formal-verification tooling already supports probabilistic and nondeterministic state-transition models such as Markov Decision Processes, so the practical boundary is not randomness by itself but whether an open-ended workflow can be compressed into a finite model with acceptable semantic loss.** ([inference]; medium confidence; source: https://www.prismmodelchecker.org/; https://www.prismmodelchecker.org/manual/Main/AllOnOnePage; https://www.prismmodelchecker.org/manual/ThePRISMLanguage/LocalNondeterminism; https://www.stormchecker.org/)
4. **Deterministic production workflows still face state-space explosion and rely on abstraction, reduction, and compression, but they usually preserve stronger local replayability because explicit guards and updates exist before execution rather than being selected at runtime by a language model.** ([inference]; medium confidence; source: https://spinroot.com/spin/Doc/Book_extras/; https://www.prismmodelchecker.org/manual/ThePRISMLanguage/Introduction; https://davidamitchell.github.io/Research/research/2026-05-18-agentic-explainability-vs-traditional.html)
5. **Agentic flexibility expands the relevant runtime state to include prompt content, retrieved data, tool choices, tool outputs, and environment side effects, so the abstraction required for formal verification loses more semantic detail than it typically does in an equivalently scoped deterministic workflow.** ([inference]; medium confidence; source: https://www.anthropic.com/research/trustworthy-agents; https://arxiv.org/abs/2302.12173; https://opentelemetry.io/docs/specs/semconv/registry/attributes/gen-ai/; https://davidamitchell.github.io/Research/research/2026-05-18-rq5-1-stochastic-vs-deterministic-failures.html)
6. **PRISM says statistical model checking is useful when explicit probabilistic verification becomes infeasible, but is not well suited to models with unresolved nondeterministic choices such as Markov Decision Processes because random paths are not well defined for them.** ([fact]; medium confidence; source: https://www.prismmodelchecker.org/manual/RunningPRISM/StatisticalModelChecking)
7. **Because agents can misread intent, absorb adversarial instructions through data, and fail to self-correct reliably, trustworthy auditability depends more on durable event lineage than on the model's later narrative or self-reported reasoning.** ([inference]; medium confidence; source: https://www.anthropic.com/research/trustworthy-agents; https://arxiv.org/abs/2302.12173; https://arxiv.org/abs/2310.01798)
8. **The most defensible production pattern is therefore a hybrid one in which flexible agentic components operate inside bounded tools and telemetry envelopes, while deterministic logic remains authoritative for final approvals, denials, or other consequential state changes.** ([inference]; medium confidence; source: https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-12; https://davidamitchell.github.io/Research/research/2026-05-09-governance-policy-determinism-vs-stochastic-llm.html; https://davidamitchell.github.io/Research/research/2026-04-26-ai-lowcode-observability-telemetry-governance.html)

**Evidence map:**

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [inference] Audit reconstruction for agentic pipelines requires prompt, output, retrieval, tool, and configuration lineage across traces, events, attributes, and lifecycle artifacts. | https://opentelemetry.io/docs/specs/semconv/gen-ai/gen-ai-spans/ ; https://opentelemetry.io/docs/specs/semconv/gen-ai/gen-ai-events/ ; https://opentelemetry.io/docs/specs/semconv/registry/attributes/gen-ai/ ; https://arxiv.org/abs/2411.05285 ; https://davidamitchell.github.io/Research/research/2026-04-26-ai-lowcode-observability-telemetry-governance.html | medium | multi-source audit synthesis |
| [inference] Article 12's automatic logging duty means recorded event traces, not only post hoc textual explanations, are needed for later reconstruction of high-risk system functioning. | https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-12 ; https://davidamitchell.github.io/Research/research/2026-04-26-ai-lowcode-observability-telemetry-governance.html | medium | regulatory plus prior observability synthesis |
| [inference] Probabilistic model checkers support random and nondeterministic finite-state models, so the practical boundary is whether the workflow can be compressed into a finite model with acceptable semantic loss. | https://www.prismmodelchecker.org/ ; https://www.prismmodelchecker.org/manual/Main/AllOnOnePage ; https://www.prismmodelchecker.org/manual/ThePRISMLanguage/LocalNondeterminism ; https://www.stormchecker.org/ | medium | supported-model synthesis |
| [inference] Deterministic workflows usually preserve stronger local replayability and lower abstraction loss than agentic workflows. | https://spinroot.com/spin/Doc/Book_extras/ ; https://www.prismmodelchecker.org/manual/ThePRISMLanguage/Introduction ; https://davidamitchell.github.io/Research/research/2026-05-18-agentic-explainability-vs-traditional.html | medium | relative comparison |
| [inference] Agentic flexibility enlarges runtime state through prompts, retrieval, tool use, and environment side effects. | https://www.anthropic.com/research/trustworthy-agents ; https://arxiv.org/abs/2302.12173 ; https://opentelemetry.io/docs/specs/semconv/registry/attributes/gen-ai/ ; https://davidamitchell.github.io/Research/research/2026-05-18-rq5-1-stochastic-vs-deterministic-failures.html | medium | multiple control surfaces |
| [fact] PRISM states that statistical model checking is approximate and is not well suited to unresolved nondeterminism in Markov Decision Processes. | https://www.prismmodelchecker.org/manual/RunningPRISM/StatisticalModelChecking | medium | direct tool limitation |
| [inference] Durable lineage is more trustworthy for audit than self-reported model reasoning when the model can misread intent or fail to self-correct. | https://www.anthropic.com/research/trustworthy-agents ; https://arxiv.org/abs/2302.12173 ; https://arxiv.org/abs/2310.01798 | medium | behavioural risk synthesis |
| [inference] Regulated production systems should keep deterministic authority at the final consequential control surface. | https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-12 ; https://davidamitchell.github.io/Research/research/2026-05-09-governance-policy-determinism-vs-stochastic-llm.html ; https://davidamitchell.github.io/Research/research/2026-04-26-ai-lowcode-observability-telemetry-governance.html | medium | governance synthesis |

**Assumptions:**

- [assumption] Formal verification of an agentic pipeline in practice means verification of a finite abstraction of the pipeline rather than full semantic verification of every generated token sequence. [source: https://www.prismmodelchecker.org/manual/Main/AllOnOnePage; https://www.stormchecker.org/] Justification: the accessible verifier sources all operate on finitised state-transition models.
- [assumption] Auditability in this item means post hoc reconstruction sufficient for incident review, monitoring, and accountability rather than perfect recovery of latent model intent. [source: https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-12; https://davidamitchell.github.io/Research/research/2026-04-26-ai-lowcode-observability-telemetry-governance.html] Justification: the regulatory and observability sources define traceability through recorded events and reconstruction artefacts.

**Analysis:**

The evidence does not support a simplistic claim that deterministic systems are verifiable and agentic systems are not. [inference; source: https://www.prismmodelchecker.org/; https://www.stormchecker.org/] PRISM and Storm show that probabilistic and nondeterministic models are legitimate formal-verification targets. [fact; source: https://www.prismmodelchecker.org/; https://www.stormchecker.org/]

The stronger claim is about semantic distance between the running system and the finite model being verified. [inference; source: https://www.prismmodelchecker.org/manual/ThePRISMLanguage/Introduction; https://spinroot.com/spin/Doc/Book_extras/; https://davidamitchell.github.io/Research/research/2026-05-18-agentic-explainability-vs-traditional.html] Deterministic workflows start from explicit guards, updates, and control flow, so abstraction still loses information, but it usually loses less of the decision surface that matters for audit and replay. [inference; source: https://www.prismmodelchecker.org/manual/ThePRISMLanguage/Introduction; https://spinroot.com/spin/Doc/Book_extras/; https://davidamitchell.github.io/Research/research/2026-05-18-agentic-explainability-vs-traditional.html]

Agentic workflows widen that distance because the branch-driving state includes prompt text, retrieved text, tool options, tool results, and environment-side effects, and some of those surfaces can be adversarial or only partly captured unless the operator deliberately instruments them. [inference; source: https://www.anthropic.com/research/trustworthy-agents; https://arxiv.org/abs/2302.12173; https://opentelemetry.io/docs/specs/semconv/registry/attributes/gen-ai/]

An alternative interpretation is that better models or stronger self-correction could close much of the gap without changing the control pattern. [inference; source: https://arxiv.org/abs/2310.01798; https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-12] The available evidence does not fully support that alternative, because Huang et al. find unreliable intrinsic self-correction, and the logging requirement in Article 12 still points to event reconstruction rather than trust in model introspection. [inference; source: https://arxiv.org/abs/2310.01798; https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-12]

The practical equilibrium is therefore hybrid: use formal methods where a bounded finite abstraction exists, use runtime traces to preserve what the abstraction drops, and keep deterministic logic authoritative where the consequence of error or contestation is high. [inference; source: https://www.prismmodelchecker.org/manual/RunningPRISM/StatisticalModelChecking; https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-12; https://davidamitchell.github.io/Research/research/2026-05-09-governance-policy-determinism-vs-stochastic-llm.html]

**Risks, gaps, uncertainties:**

- This item does not quantify a numerical Pareto frontier between flexibility and verifiability, because the accessible sources support a qualitative boundary more strongly than a single cross-system metric. [inference; source: https://www.prismmodelchecker.org/manual/RunningPRISM/StatisticalModelChecking; https://www.anthropic.com/research/trustworthy-agents]
- The line between acceptable abstraction loss and excessive semantic loss remains domain-specific, especially when external tools mutate the environment. [inference; source: https://www.anthropic.com/research/trustworthy-agents; https://opentelemetry.io/docs/specs/semconv/registry/attributes/gen-ai/]
- The OpenTelemetry generative Artificial Intelligence conventions are still marked as development status, so field names are informative and directionally useful but not yet a settled regulatory schema. [fact; source: https://opentelemetry.io/docs/specs/semconv/gen-ai/gen-ai-spans/; https://opentelemetry.io/docs/specs/semconv/gen-ai/gen-ai-events/; https://opentelemetry.io/docs/specs/semconv/registry/attributes/gen-ai/]

**Open questions:**

- Which bounded abstraction patterns best preserve the semantics of retrieval and tool choice in enterprise agent pipelines without collapsing tractability?
- What runtime-monitoring or shielding pattern provides the strongest complement to model checking for tool-using agents in mutable environments?
- How should operators measure when an audit trail is reconstructable enough for contestability rather than merely rich enough for debugging?

### §7 Recursive Review

- review_result: pass
- source_url_audit: passed
- acronym_audit: passed
- claim_label_audit: passed
- findings_parity_audit: passed
- related_item_sweep: repeated before synthesis and aligned to cited completed items
- unresolved_contradictions: none material

---

## Findings

### Executive Summary

Agentic flexibility reduces exact auditability and full-state formal verifiability unless the system is wrapped in a constrained, trace-rich control shell that records the run well enough to reconstruct what happened and abstracts the workflow into a finite verification target. [inference; source: https://opentelemetry.io/docs/specs/semconv/gen-ai/gen-ai-spans/; https://www.prismmodelchecker.org/manual/Main/AllOnOnePage; https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-12]

Deterministic pipelines also face state-space and observability limits, but current verification tools fit them more naturally because their control flow and update rules are explicit before runtime, which keeps abstraction loss lower and replayability stronger. [inference; source: https://spinroot.com/spin/Doc/Book_extras/; https://www.prismmodelchecker.org/manual/ThePRISMLanguage/Introduction; https://davidamitchell.github.io/Research/research/2026-05-18-agentic-explainability-vs-traditional.html]

Probabilistic model checking shows that stochastic systems are not outside formal methods altogether, yet the tractable object is a finitised Markov-style abstraction such as an MDP rather than the full semantic content of an open-ended agent run. [inference; source: https://www.prismmodelchecker.org/; https://www.prismmodelchecker.org/manual/ThePRISMLanguage/LocalNondeterminism; https://www.stormchecker.org/]

For regulated production use, the practical design implication is to keep deterministic authority at the final consequential control surface while allowing agentic components upstream only when prompts, retrieval, tool use, outputs, and overrides are durably logged. [inference; source: https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-12; https://davidamitchell.github.io/Research/research/2026-05-09-governance-policy-determinism-vs-stochastic-llm.html; https://davidamitchell.github.io/Research/research/2026-04-26-ai-lowcode-observability-telemetry-governance.html]

### Key Findings

1. **A production-grade audit trail for an agentic pipeline must capture conversation identity, model identity, prompt and instruction state, retrieval lineage, tool-call lineage, outputs, and errors, because current observability standards and agent-observability literature split those facts across traces, events, attributes, and lifecycle artifacts rather than one canonical log record.** ([inference]; medium confidence; source: https://opentelemetry.io/docs/specs/semconv/gen-ai/gen-ai-spans/; https://opentelemetry.io/docs/specs/semconv/gen-ai/gen-ai-events/; https://opentelemetry.io/docs/specs/semconv/registry/attributes/gen-ai/; https://arxiv.org/abs/2411.05285; https://davidamitchell.github.io/Research/research/2026-04-26-ai-lowcode-observability-telemetry-governance.html)
2. **The European Union Artificial Intelligence Act's automatic logging requirement means that recorded event traces, not only post hoc textual explanations, are needed where a high-risk system's functioning must later be reconstructed for monitoring or investigation.** ([inference]; medium confidence; source: https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-12; https://davidamitchell.github.io/Research/research/2026-04-26-ai-lowcode-observability-telemetry-governance.html)
3. **Current mainstream formal-verification tooling already supports probabilistic and nondeterministic state-transition models such as Markov Decision Processes, so the practical boundary is not randomness by itself but whether an open-ended workflow can be compressed into a finite model with acceptable semantic loss.** ([inference]; medium confidence; source: https://www.prismmodelchecker.org/; https://www.prismmodelchecker.org/manual/Main/AllOnOnePage; https://www.prismmodelchecker.org/manual/ThePRISMLanguage/LocalNondeterminism; https://www.stormchecker.org/)
4. **Deterministic production workflows still face state-space explosion and rely on abstraction, reduction, and compression, but they usually preserve stronger local replayability because explicit guards and updates exist before execution rather than being selected at runtime by a language model.** ([inference]; medium confidence; source: https://spinroot.com/spin/Doc/Book_extras/; https://www.prismmodelchecker.org/manual/ThePRISMLanguage/Introduction; https://davidamitchell.github.io/Research/research/2026-05-18-agentic-explainability-vs-traditional.html)
5. **Agentic flexibility expands the relevant runtime state to include prompt content, retrieved data, tool choices, tool outputs, and environment side effects, so the abstraction required for formal verification loses more semantic detail than it typically does in an equivalently scoped deterministic workflow.** ([inference]; medium confidence; source: https://www.anthropic.com/research/trustworthy-agents; https://arxiv.org/abs/2302.12173; https://opentelemetry.io/docs/specs/semconv/registry/attributes/gen-ai/; https://davidamitchell.github.io/Research/research/2026-05-18-rq5-1-stochastic-vs-deterministic-failures.html)
6. **PRISM says statistical model checking is useful when explicit probabilistic verification becomes infeasible, but is not well suited to models with unresolved nondeterministic choices such as Markov Decision Processes because random paths are not well defined for them.** ([fact]; medium confidence; source: https://www.prismmodelchecker.org/manual/RunningPRISM/StatisticalModelChecking)
7. **Because agents can misread intent, absorb adversarial instructions through data, and fail to self-correct reliably, trustworthy auditability depends more on durable event lineage than on the model's later narrative or self-reported reasoning.** ([inference]; medium confidence; source: https://www.anthropic.com/research/trustworthy-agents; https://arxiv.org/abs/2302.12173; https://arxiv.org/abs/2310.01798)
8. **The most defensible production pattern is therefore a hybrid one in which flexible agentic components operate inside bounded tools and telemetry envelopes, while deterministic logic remains authoritative for final approvals, denials, or other consequential state changes.** ([inference]; medium confidence; source: https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-12; https://davidamitchell.github.io/Research/research/2026-05-09-governance-policy-determinism-vs-stochastic-llm.html; https://davidamitchell.github.io/Research/research/2026-04-26-ai-lowcode-observability-telemetry-governance.html)

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [inference] Audit reconstruction for agentic pipelines requires prompt, output, retrieval, tool, and configuration lineage across traces, events, attributes, and lifecycle artifacts. | https://opentelemetry.io/docs/specs/semconv/gen-ai/gen-ai-spans/ ; https://opentelemetry.io/docs/specs/semconv/gen-ai/gen-ai-events/ ; https://opentelemetry.io/docs/specs/semconv/registry/attributes/gen-ai/ ; https://arxiv.org/abs/2411.05285 ; https://davidamitchell.github.io/Research/research/2026-04-26-ai-lowcode-observability-telemetry-governance.html | medium | multi-source audit synthesis |
| [inference] Article 12's automatic logging duty means recorded event traces, not only post hoc textual explanations, are needed for later reconstruction of high-risk system functioning. | https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-12 ; https://davidamitchell.github.io/Research/research/2026-04-26-ai-lowcode-observability-telemetry-governance.html | medium | regulatory plus prior observability synthesis |
| [inference] Probabilistic model checkers support random and nondeterministic finite-state models, so the practical boundary is whether the workflow can be compressed into a finite model with acceptable semantic loss. | https://www.prismmodelchecker.org/ ; https://www.prismmodelchecker.org/manual/Main/AllOnOnePage ; https://www.prismmodelchecker.org/manual/ThePRISMLanguage/LocalNondeterminism ; https://www.stormchecker.org/ | medium | supported-model synthesis |
| [inference] Deterministic workflows usually preserve stronger local replayability and lower abstraction loss than agentic workflows. | https://spinroot.com/spin/Doc/Book_extras/ ; https://www.prismmodelchecker.org/manual/ThePRISMLanguage/Introduction ; https://davidamitchell.github.io/Research/research/2026-05-18-agentic-explainability-vs-traditional.html | medium | relative comparison |
| [inference] Agentic flexibility enlarges runtime state through prompts, retrieval, tool use, and environment side effects. | https://www.anthropic.com/research/trustworthy-agents ; https://arxiv.org/abs/2302.12173 ; https://opentelemetry.io/docs/specs/semconv/registry/attributes/gen-ai/ ; https://davidamitchell.github.io/Research/research/2026-05-18-rq5-1-stochastic-vs-deterministic-failures.html | medium | multiple control surfaces |
| [fact] PRISM states that statistical model checking is approximate and is not well suited to unresolved nondeterminism in Markov Decision Processes. | https://www.prismmodelchecker.org/manual/RunningPRISM/StatisticalModelChecking | medium | direct tool limitation |
| [inference] Durable lineage is more trustworthy for audit than self-reported model reasoning when the model can misread intent or fail to self-correct. | https://www.anthropic.com/research/trustworthy-agents ; https://arxiv.org/abs/2302.12173 ; https://arxiv.org/abs/2310.01798 | medium | behavioural risk synthesis |
| [inference] Regulated production systems should keep deterministic authority at the final consequential control surface. | https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-12 ; https://davidamitchell.github.io/Research/research/2026-05-09-governance-policy-determinism-vs-stochastic-llm.html ; https://davidamitchell.github.io/Research/research/2026-04-26-ai-lowcode-observability-telemetry-governance.html | medium | governance synthesis |

### Assumptions

- **Assumption:** Formal verification of an agentic pipeline in practice means verification of a finite abstraction of the pipeline rather than full semantic verification of every generated token sequence. [assumption; source: https://www.prismmodelchecker.org/manual/Main/AllOnOnePage; https://www.stormchecker.org/] **Justification:** the accessible verifier sources all operate on finitised state-transition models.
- **Assumption:** Auditability in this item means post hoc reconstruction sufficient for incident review, monitoring, and accountability rather than perfect recovery of latent model intent. [assumption; source: https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-12; https://davidamitchell.github.io/Research/research/2026-04-26-ai-lowcode-observability-telemetry-governance.html] **Justification:** the regulatory and observability sources define traceability through recorded events and reconstruction artefacts.

### Analysis

The evidence does not support a simplistic claim that deterministic systems are verifiable and agentic systems are not. [inference; source: https://www.prismmodelchecker.org/; https://www.stormchecker.org/] PRISM and Storm show that probabilistic and nondeterministic models are legitimate formal-verification targets. [fact; source: https://www.prismmodelchecker.org/; https://www.stormchecker.org/]

The stronger claim is about semantic distance between the running system and the finite model being verified. [inference; source: https://www.prismmodelchecker.org/manual/ThePRISMLanguage/Introduction; https://spinroot.com/spin/Doc/Book_extras/; https://davidamitchell.github.io/Research/research/2026-05-18-agentic-explainability-vs-traditional.html] Deterministic workflows start from explicit guards, updates, and control flow, so abstraction still loses information, but it usually loses less of the decision surface that matters for audit and replay. [inference; source: https://www.prismmodelchecker.org/manual/ThePRISMLanguage/Introduction; https://spinroot.com/spin/Doc/Book_extras/; https://davidamitchell.github.io/Research/research/2026-05-18-agentic-explainability-vs-traditional.html]

Agentic workflows widen that distance because the branch-driving state includes prompt text, retrieved text, tool options, tool results, and environment-side effects, and some of those surfaces can be adversarial or only partly captured unless the operator deliberately instruments them. [inference; source: https://www.anthropic.com/research/trustworthy-agents; https://arxiv.org/abs/2302.12173; https://opentelemetry.io/docs/specs/semconv/registry/attributes/gen-ai/]

An alternative interpretation is that better models or stronger self-correction could close much of the gap without changing the control pattern. [inference; source: https://arxiv.org/abs/2310.01798; https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-12] The available evidence does not fully support that alternative, because Huang et al. find unreliable intrinsic self-correction, and the logging requirement in Article 12 still points to event reconstruction rather than trust in model introspection. [inference; source: https://arxiv.org/abs/2310.01798; https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-12]

The practical equilibrium is therefore hybrid: use formal methods where a bounded finite abstraction exists, use runtime traces to preserve what the abstraction drops, and keep deterministic logic authoritative where the consequence of error or contestation is high. [inference; source: https://www.prismmodelchecker.org/manual/RunningPRISM/StatisticalModelChecking; https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-12; https://davidamitchell.github.io/Research/research/2026-05-09-governance-policy-determinism-vs-stochastic-llm.html]

### Risks, Gaps, and Uncertainties

- This item does not quantify a numerical Pareto frontier between flexibility and verifiability, because the accessible sources support a qualitative boundary more strongly than a single cross-system metric. [inference; source: https://www.prismmodelchecker.org/manual/RunningPRISM/StatisticalModelChecking; https://www.anthropic.com/research/trustworthy-agents]
- The line between acceptable abstraction loss and excessive semantic loss remains domain-specific, especially when external tools mutate the environment. [inference; source: https://www.anthropic.com/research/trustworthy-agents; https://opentelemetry.io/docs/specs/semconv/registry/attributes/gen-ai/]
- The OpenTelemetry generative Artificial Intelligence conventions are still marked as development status, so field names are informative and directionally useful but not yet a settled regulatory schema. [fact; source: https://opentelemetry.io/docs/specs/semconv/gen-ai/gen-ai-spans/; https://opentelemetry.io/docs/specs/semconv/gen-ai/gen-ai-events/; https://opentelemetry.io/docs/specs/semconv/registry/attributes/gen-ai/]

### Open Questions

- Which bounded abstraction patterns best preserve the semantics of retrieval and tool choice in enterprise agent pipelines without collapsing tractability?
- What runtime-monitoring or shielding pattern provides the strongest complement to model checking for tool-using agents in mutable environments?
- How should operators measure when an audit trail is reconstructable enough for contestability rather than merely rich enough for debugging?

---

## Output

- Type: knowledge
- Description: Knowledge item on how agentic flexibility shifts auditability and formal verification from exact replay and proof toward bounded abstractions, richer telemetry, and deterministic final control surfaces. [inference; source: https://www.prismmodelchecker.org/manual/Main/AllOnOnePage; https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-12; https://davidamitchell.github.io/Research/research/2026-05-09-governance-policy-determinism-vs-stochastic-llm.html]
- Links:
  - https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-12
  - https://www.prismmodelchecker.org/manual/Main/AllOnOnePage
  - https://opentelemetry.io/docs/specs/semconv/registry/attributes/gen-ai/
