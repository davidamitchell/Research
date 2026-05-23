---
review_count: 2
title: "RQ 5.1: Stochastic versus Deterministic Failure Modes on Identical Unvalidated Inputs"
added: 2026-05-18T19:40:00+00:00
status: completed
priority: high
blocks:
  - 2026-05-18-rq5-2-flexibility-vs-predictability-auditability
  - 2026-05-18-agentic-explainability-vs-traditional
started: 2026-05-19T19:40:54+00:00
completed: 2026-05-19T20:00:09+00:00
output: [knowledge]
themes: [agentic-ai, llm-reasoning, security-risk, ai-architecture, formal-reliability]
cites:
  - 2026-05-18-rq4-2-adversarial-error-propagation
  - 2026-05-18-rq4-3-ood-generalization-agentic
  - 2026-05-09-llm-determinism-limits-temperature-zero
  - 2026-05-18-agentic-explainability-vs-traditional
related:
  - 2026-05-08-integrated-cascading-failure-agentic-vs-generative-ai-risk
  - 2026-05-09-governance-policy-determinism-vs-stochastic-llm
  - 2026-05-13-agent-process-reliability-architecture
superseded_by: ~
supersedes: ~
item_type: primary
confidence: medium
versions: []
---

# RQ 5.1: Stochastic versus Deterministic Failure Modes on Identical Unvalidated Inputs

## Research Question

How do the failure modes of a stochastic multi-step Large Language Model (LLM) agent, meaning a tool-using system whose action path can vary across runs, differ fundamentally from the failure modes of a deterministic coded system when both process the same unvalidated input?

## Scope

**In scope:**
- Deterministic versus stochastic runtime behaviour as the formal distinction between coded systems and LLM-based agents
- Silent semantic degradation, meaning the system keeps producing plausible-looking but semantically wrong outputs, versus explicit crash, reject, or exception paths
- Semantic drift, meaning the system's working interpretation shifts away from the real task or world state without an immediate hard failure
- A common comparison schema across detectability, replayability, propagation speed, recoverability, and formal verifiability
- Production telemetry or observability evidence for LLM or agent failure patterns

**Out of scope:**
- Remediation strategies for either system class
- Hardware faults, accelerator faults, or network faults except where a source uses them to explain failure visibility
- A claim that all deterministic distributed systems are fully transparent at every scale

**Constraints:** Use URL-backed sources only, check the seeded sources even if they are replaced, cite prior completed items with public GitHub Pages links rather than repository-relative paths, and keep tags in canonical forms.

## Context

- Prior completed work in this repository already established that tool-using LLM systems can propagate corrupted context through planning, tool use, memory, and verification, and that unconstrained out-of-distribution (OOD) deployment weakens exact correctness guarantees into bounded-risk or abstention-style guarantees. [fact; source: https://davidamitchell.github.io/Research/research/2026-05-18-rq4-2-adversarial-error-propagation.html; https://davidamitchell.github.io/Research/research/2026-05-18-rq4-3-ood-generalization-agentic.html]
- Prior completed work also established that large deterministic software systems can become globally opaque at production scale while still keeping stronger local replayability than LLM-based systems. [fact; source: https://davidamitchell.github.io/Research/research/2026-05-18-agentic-explainability-vs-traditional.html]
- The unresolved comparison is therefore not whether both system classes can fail, but how their local failure signatures differ when the same unvalidated input reaches a deterministic workflow versus a probabilistic multi-step agent. [inference; source: https://davidamitchell.github.io/Research/research/2026-05-18-rq4-2-adversarial-error-propagation.html; https://davidamitchell.github.io/Research/research/2026-05-18-rq4-3-ood-generalization-agentic.html; https://davidamitchell.github.io/Research/research/2026-05-18-agentic-explainability-vs-traditional.html]

## Approach

1. Define a comparison frame that separates local replayability, global opacity, silent semantic degradation, and explicit failure boundaries.
2. Compile the deterministic baseline from formal fault, error, and failure taxonomy plus production monitoring literature on bogus-input crashes and diagnosable failure signals.
3. Compile the stochastic agent baseline from prompt-injection, self-correction, OOD, and repeated-run nondeterminism evidence.
4. Add production telemetry and observability evidence for Large Language Model serving and agent operations.
5. Synthesize which failure modes are shared, which are unique, and which are materially worse in one system class.

## Sources

**Consulted:**

- [x] [Avizienis et al. (2004) Basic Concepts and Taxonomy of Dependable and Secure Computing](https://ieeexplore.ieee.org/document/1335465/)
- [x] [Ewaschuk (n.d.) Monitoring Distributed Systems](https://sre.google/sre-book/monitoring-distributed-systems/)
- [x] [Anthropic (2026) Trustworthy agents](https://www.anthropic.com/research/trustworthy-agents)
- [x] [Abdelnabi et al. (2023) Not what you've signed up for: Compromising Real-World Large Language Model-Integrated Applications with Indirect Prompt Injection](https://arxiv.org/abs/2302.12173)
- [x] [Yi et al. (2025) Benchmarking and Defending Against Indirect Prompt Injection Attacks on Large Language Models](https://arxiv.org/abs/2312.14197)
- [x] [Huang et al. (2024) Large Language Models Cannot Self-Correct Reasoning Yet](https://arxiv.org/abs/2310.01798)
- [x] [Atil et al. (2025) Non-Determinism of "Deterministic" LLM Settings](https://arxiv.org/abs/2408.04667)
- [x] [Denisov-Blanch et al. (2025) Measuring Determinism in Large Language Models for Software Code Review](https://arxiv.org/abs/2502.20747)
- [x] [Heim et al. (2025) A Guide to Failure in Machine Learning: Reliability and Robustness from Traditional Software to Modern Foundation Models](https://arxiv.org/abs/2503.00563)
- [x] [Dong et al. (2024) AgentOps: Enabling Observability of Large Language Model Agents](https://arxiv.org/abs/2411.05285)
- [x] [Ranganathan et al. (2026) An Empirical Study of Automation Gaps in Large Language Model Serving Systems](https://cloudintelligenceworkshop.org/papers/aiops26-Ranganathan.pdf)
- [x] [Microsoft (2025) How Microsoft defends against indirect prompt injection attacks](https://www.microsoft.com/en-us/msrc/blog/2025/07/how-microsoft-defends-against-indirect-prompt-injection-attacks)
- [x] [Mitchell (2026) Research Question 4.2: Adversarial inputs and error propagation through multi-step tool-using verification and strategy phases](https://davidamitchell.github.io/Research/research/2026-05-18-rq4-2-adversarial-error-propagation.html)
- [x] [Mitchell (2026) Research Question 4.3: Formal bounds on generalisation outside the training distribution for tool-using Large Language Model systems under non-deterministic tool outputs](https://davidamitchell.github.io/Research/research/2026-05-18-rq4-3-ood-generalization-agentic.html)
- [x] [Mitchell (2026) Practical Limits of Large Language Model Determinism: Temperature Zero, Fixed Seeds, and Constrained Prompts](https://davidamitchell.github.io/Research/research/2026-05-09-llm-determinism-limits-temperature-zero.html)
- [x] [Mitchell (2026) Are Multi-Step Large Language Model-Based Systems Inherently Less Explainable Than Equivalently Scoped Deterministic Software Systems?](https://davidamitchell.github.io/Research/research/2026-05-18-agentic-explainability-vs-traditional.html)

**Identified but not consulted:**

- [ ] [Dijkstra (1989) On the Cruelty of Really Teaching Computer Science](https://dl.acm.org/doi/10.1145/74580.74582)
- [ ] [Bernstein and Sequin (1988) Sequoia: A Fault-Tolerant Tightly Coupled Multiprocessor for Transaction Processing](https://www.computer.org/csdl/magazine/co/1988/02/r2037/13rRUxly90j)

---

## Research Skill Output

*(Full output from running the research skill, retained verbatim in the completed item. Sections 0 to 5 are the investigation, and section 6 seeds the Findings section below.)*

### §0 Initialise

- Question: how do the failure modes of a stochastic multi-step Large Language Model agent differ from the failure modes of a deterministic coded system when both process the same unvalidated input?
- Scope: local failure signatures, silent semantic degradation, replayability, propagation, observability, and formal comparison across deterministic and stochastic systems.
- Constraints: full-mode investigation, URL-backed sources only, prior completed-item sweep, canonical tags only, and mirrored synthesis plus Findings output.
- Output: executive summary, key findings, evidence map, assumptions, analysis, risks and gaps, open questions, and a populated output section.
- Prior completed items consulted: https://davidamitchell.github.io/Research/research/2026-05-18-rq4-2-adversarial-error-propagation.html ; https://davidamitchell.github.io/Research/research/2026-05-18-rq4-3-ood-generalization-agentic.html ; https://davidamitchell.github.io/Research/research/2026-05-09-llm-determinism-limits-temperature-zero.html ; https://davidamitchell.github.io/Research/research/2026-05-18-agentic-explainability-vs-traditional.html ; https://davidamitchell.github.io/Research/research/2026-05-08-integrated-cascading-failure-agentic-vs-generative-ai-risk.html

### §1 Question Decomposition

1. Prior completed-item sweep
   1.1 What stochastic failure properties were already established in Research Question 4.2 and Research Question 4.3?
   1.2 What deterministic-versus-opaque software distinction was already established in the explainability synthesis?
2. Deterministic coded-system baseline
   2.1 What formal taxonomy describes deterministic system faults, errors, and failures?
   2.2 What evidence shows how production software surfaces bogus-input failures or other explicit failure signals?
   2.3 Which deterministic failure properties remain replayable even when the system is wrong?
3. Stochastic agent baseline
   3.1 What happens when unvalidated text is misread as instructions rather than as data?
   3.2 What evidence shows that identical prompts can still produce different paths under supposedly deterministic settings?
   3.3 What evidence shows that same-model verification fails to reliably stop semantic error?
4. Production observability
   4.1 What telemetry evidence exists for failure detection and mitigation in Large Language Model serving systems?
   4.2 What observability literature says agent systems need additional tracing because of autonomy and non-determinism?
5. Comparative synthesis
   5.1 Which failure modes are shared at the abstract fault-error-failure level?
   5.2 Which failure modes are unique to stochastic agents?
   5.3 Which differences matter most for detectability, replayability, and formal verifiability?

### §2 Investigation

#### A. Prior completed-item sweep

- [fact] Research Question 4.2 concluded that once a tool-using Large Language Model system ingests corrupted context, planning, tool use, memory, and verification can propagate the error across later steps. [source: https://davidamitchell.github.io/Research/research/2026-05-18-rq4-2-adversarial-error-propagation.html]
- [fact] Research Question 4.3 concluded that under unconstrained deployment shift and stochastic tool outputs, the strongest defensible guarantees collapse from exact correctness to bounded-risk, coverage, or abstention-style guarantees. [source: https://davidamitchell.github.io/Research/research/2026-05-18-rq4-3-ood-generalization-agentic.html]
- [fact] The explainability synthesis concluded that large deterministic software systems lose global transparency at scale but still preserve stronger local replayability than Large Language Model-based systems. [source: https://davidamitchell.github.io/Research/research/2026-05-18-agentic-explainability-vs-traditional.html]
- [inference] The current item therefore needs to distinguish local failure signature from global system opacity, because those are related but not identical comparison surfaces. [source: https://davidamitchell.github.io/Research/research/2026-05-18-rq4-2-adversarial-error-propagation.html; https://davidamitchell.github.io/Research/research/2026-05-18-rq4-3-ood-generalization-agentic.html; https://davidamitchell.github.io/Research/research/2026-05-18-agentic-explainability-vs-traditional.html]

#### B. Deterministic coded-system failure baseline

- [fact] Avizienis et al. define dependable-system threats through the fault, error, and failure chain, and present a general taxonomy intended to support consistent reasoning across system types and failure causes. [source: https://ieeexplore.ieee.org/document/1335465/]
- [fact] Google Site Reliability Engineering guidance gives software that crashed on bogus input as a canonical example of a root cause that should be repaired after an incident. [source: https://sre.google/sre-book/monitoring-distributed-systems/]
- [fact] The same Google Site Reliability Engineering guidance says paging rules should remain simple, robust, and tied to clear failures rather than vague anomalies. [source: https://sre.google/sre-book/monitoring-distributed-systems/]
- [fact] Google Site Reliability Engineering guidance also says white-box monitoring is essential for debugging, because engineers otherwise cannot distinguish an actually slow dependency from a network or integration problem. [source: https://sre.google/sre-book/monitoring-distributed-systems/]
- [inference] For deterministic coded systems, unvalidated-input failures are therefore most naturally modelled as explicit boundary failures, such as reject, exception, timeout, or a replayable wrong state, rather than as inherently variable decision paths on identical replays. [source: https://ieeexplore.ieee.org/document/1335465/; https://sre.google/sre-book/monitoring-distributed-systems/; https://davidamitchell.github.io/Research/research/2026-05-18-agentic-explainability-vs-traditional.html]

#### C. Stochastic agent failure baseline

- [fact] Anthropic defines an agent as a model that directs its own processes and tool use in a self-directed loop that plans, acts, observes the result, adjusts, and repeats. [source: https://www.anthropic.com/research/trustworthy-agents]
- [fact] Anthropic says agents act with less human oversight, have more room to misread users' intent, and are targets for prompt injection attacks that can make them take costly unintended actions. [source: https://www.anthropic.com/research/trustworthy-agents]
- [fact] Abdelnabi et al. show that indirect prompt injection blurs the line between data and instructions in Large Language Model-integrated applications and can manipulate functionality, tool use, and downstream Application Programming Interface (API) calls. [source: https://arxiv.org/abs/2302.12173]
- [fact] Yi et al. find evaluated models universally vulnerable to indirect prompt injection and attribute that vulnerability to the models' inability to distinguish informational context from actionable instructions. [source: https://arxiv.org/abs/2312.14197]
- [fact] Microsoft says indirect prompt injection can arrive through webpages, emails, shared documents, or tool outputs and can lead to data exfiltration or unintended actions on behalf of the user. [source: https://www.microsoft.com/en-us/msrc/blog/2025/07/how-microsoft-defends-against-indirect-prompt-injection-attacks]
- [fact] Huang et al. report that Large Language Models struggle to self-correct reasoning without external feedback and that intrinsic self-correction can even degrade performance. [source: https://arxiv.org/abs/2310.01798]
- [fact] Research Question 4.2 concluded that corrupted state in a tool-using loop can amplify through branch selection, tool-mediated state change, and persistent memory. [source: https://davidamitchell.github.io/Research/research/2026-05-18-rq4-2-adversarial-error-propagation.html]
- [inference] For stochastic agents, the same unvalidated input can therefore be absorbed as plausible context rather than rejected as malformed input, allowing the system to continue operating while its working task representation drifts semantically away from the real goal or world state. [source: https://www.anthropic.com/research/trustworthy-agents; https://arxiv.org/abs/2302.12173; https://arxiv.org/abs/2312.14197; https://arxiv.org/abs/2310.01798; https://davidamitchell.github.io/Research/research/2026-05-18-rq4-2-adversarial-error-propagation.html]

#### D. Repeated-run nondeterminism and branching variance

- [fact] Atil et al. find that five Large Language Models configured to be deterministic still showed accuracy variation up to 15 percent across repeated runs and did not consistently reproduce identical output strings. [source: https://arxiv.org/abs/2408.04667]
- [fact] Denisov-Blanch et al. find response variation across repeated temperature-zero code-review prompts in every model family they tested, even when prompts and setup were held constant. [source: https://arxiv.org/abs/2502.20747]
- [fact] The completed determinism item in this repository synthesised vendor guidance and repeated-run evidence and concluded that temperature zero and fixed seeds narrow variance but do not create hard identical-output guarantees. [source: https://davidamitchell.github.io/Research/research/2026-05-09-llm-determinism-limits-temperature-zero.html]
- [inference] Identical unvalidated inputs can therefore produce different branch paths, different intermediate judgments, and different terminal failures in stochastic agents, whereas deterministic coded systems remain replayable from the same initial state even when they are wrong. [source: https://arxiv.org/abs/2408.04667; https://arxiv.org/abs/2502.20747; https://davidamitchell.github.io/Research/research/2026-05-09-llm-determinism-limits-temperature-zero.html; https://davidamitchell.github.io/Research/research/2026-05-18-agentic-explainability-vs-traditional.html]

#### E. Production telemetry and observability

- [fact] Ranganathan et al. analyze 156 high-severity production incidents from a large-scale Large Language Model serving platform and find that 74 percent were automatically detected but most impactful mitigations remained manual, with time-to-mitigate reaching 49 hours. [source: https://cloudintelligenceworkshop.org/papers/aiops26-Ranganathan.pdf]
- [fact] Ranganathan et al. also argue that Large Language Model serving differs operationally from traditional stateless microservices because it couples latency-critical inference, dynamic batching, accelerator scheduling, and complex dependency chains. [source: https://cloudintelligenceworkshop.org/papers/aiops26-Ranganathan.pdf]
- [fact] Dong et al. say Large Language Model agents raise safety concerns because of autonomous and non-deterministic behavior and propose AgentOps as a lifecycle observability taxonomy for tracing agent artifacts and associated data. [source: https://arxiv.org/abs/2411.05285]
- [fact] Heim et al. say one of the main barriers to Machine Learning adoption is that Machine Learning models can fail unexpectedly and propose reliability and robustness as the primary formal lenses for reasoning about those failures. [source: https://arxiv.org/abs/2503.00563]
- [inference] Production incident evidence from Large Language Model serving plus recent agent-observability research supports the conclusion that conventional incident detection is not enough to reconstruct or safely automate recovery once semantic or model-specific failure mechanisms are involved. [source: https://cloudintelligenceworkshop.org/papers/aiops26-Ranganathan.pdf; https://arxiv.org/abs/2411.05285; https://arxiv.org/abs/2503.00563]

#### F. Comparative synthesis

- [inference] Deterministic coded systems and stochastic agents share the abstract Avizienis fault, error, and failure chain, but the dominant manifestation differs materially at the point where unvalidated input crosses the boundary into runtime state. [source: https://ieeexplore.ieee.org/document/1335465/; https://arxiv.org/abs/2503.00563; https://arxiv.org/abs/2302.12173]
- [inference] The strongest deterministic-system advantage is local replayability: once code, input, and environment are fixed, the same failure path can usually be reproduced and instrumented even if the global service graph is hard to understand. [source: https://sre.google/sre-book/monitoring-distributed-systems/; https://davidamitchell.github.io/Research/research/2026-05-18-agentic-explainability-vs-traditional.html]
- [inference] The strongest stochastic-agent disadvantage is a tendency to absorb semantically misleading input as plausible context, because an invalid or attacker-shaped input can remain locally plausible, change the inferred task, and keep the loop running without any boundary exception that ordinary software monitoring would reliably classify as failure. [source: https://www.anthropic.com/research/trustworthy-agents; https://arxiv.org/abs/2302.12173; https://arxiv.org/abs/2312.14197; https://www.microsoft.com/en-us/msrc/blog/2025/07/how-microsoft-defends-against-indirect-prompt-injection-attacks]
- [inference] The comparison does not justify the stronger claim that deterministic systems never fail silently, because large distributed systems can still drift into opaque, hard-to-explain states; however, current evidence still supports a narrower asymmetry at the local bogus-input boundary. [source: https://sre.google/sre-book/monitoring-distributed-systems/; https://davidamitchell.github.io/Research/research/2026-05-18-agentic-explainability-vs-traditional.html]
search_note_subramaniam: "Subramaniam production LLM agent failure telemetry" / "Subramaniam LLM agent failure production arXiv" / "Subramaniam 2024 agent telemetry LLM" -> not found

### §3 Reasoning

- [inference] The comparison holds only if local failure boundary and global system opacity are kept separate, because deterministic distributed systems can be globally opaque without becoming locally stochastic. [source: https://sre.google/sre-book/monitoring-distributed-systems/; https://davidamitchell.github.io/Research/research/2026-05-18-agentic-explainability-vs-traditional.html]
- [inference] Explicit crash, reject, or timeout behavior is not the only possible deterministic failure signature, but it is a more common and more operationally tractable signature than the silent semantic degradation seen in prompt-injected or distribution-shifted LLM agents. [source: https://sre.google/sre-book/monitoring-distributed-systems/; https://arxiv.org/abs/2302.12173; https://arxiv.org/abs/2312.14197; https://arxiv.org/abs/2503.00563]
- [inference] Repeated-run nondeterminism matters because it turns a single invalid input from one reproducible failure trajectory into a distribution of possible failure trajectories, which directly weakens debugging and post-incident reconstruction. [source: https://arxiv.org/abs/2408.04667; https://arxiv.org/abs/2502.20747; https://davidamitchell.github.io/Research/research/2026-05-09-llm-determinism-limits-temperature-zero.html]
- [inference] Production telemetry evidence is stronger for Large Language Model serving than for full end-to-end autonomous agents, so operational conclusions about agent observability should be kept at medium confidence rather than treated as fully settled. [source: https://cloudintelligenceworkshop.org/papers/aiops26-Ranganathan.pdf; https://arxiv.org/abs/2411.05285]

### §4 Consistency Check

- [inference] The reviewed evidence is internally consistent with the claim that deterministic systems retain stronger local replayability while still becoming globally opaque at scale. [source: https://sre.google/sre-book/monitoring-distributed-systems/; https://davidamitchell.github.io/Research/research/2026-05-18-agentic-explainability-vs-traditional.html]
- [inference] The reviewed prompt-injection evidence documents vulnerability and mitigation gaps rather than reliable boundary rejection of misleading external content, which supports keeping the agent-side rejection claim below fact status. [source: https://arxiv.org/abs/2302.12173; https://arxiv.org/abs/2312.14197; https://www.microsoft.com/en-us/msrc/blog/2025/07/how-microsoft-defends-against-indirect-prompt-injection-attacks]
- [inference] The remaining tension is only about degree, not direction: deterministic systems can sometimes fail silently, but the reviewed evidence still supports stochastic agents as more silence-prone and more path-variable on identical unvalidated inputs. [source: https://ieeexplore.ieee.org/document/1335465/; https://sre.google/sre-book/monitoring-distributed-systems/; https://arxiv.org/abs/2408.04667; https://arxiv.org/abs/2502.20747]

### §5 Depth and Breadth Expansion

- [inference] Technical lens: deterministic systems concentrate failure at typed interfaces, parsers, rule boundaries, and explicit state transitions, while stochastic agents move more failure mass into latent task interpretation and next-step selection. [source: https://ieeexplore.ieee.org/document/1335465/; https://arxiv.org/abs/2302.12173; https://arxiv.org/abs/2312.14197]
- [inference] Operational lens: deterministic incidents are often easier to reproduce once the triggering request and state snapshot are captured, whereas stochastic incidents require richer traces because the same prompt can branch differently across runs. [source: https://sre.google/sre-book/monitoring-distributed-systems/; https://arxiv.org/abs/2408.04667; https://arxiv.org/abs/2502.20747; https://arxiv.org/abs/2411.05285]
- [inference] Governance lens: the comparative failure asymmetry explains why prior completed governance items in this repository keep probabilistic models in proposal roles and deterministic systems in authoritative decision roles. [source: https://davidamitchell.github.io/Research/research/2026-05-09-governance-policy-determinism-vs-stochastic-llm.html; https://davidamitchell.github.io/Research/research/2026-05-09-llm-determinism-limits-temperature-zero.html]
- [inference] Behavioural lens: because stochastic agents often continue with fluent but wrong output, humans can miss failure until downstream consequences appear, whereas deterministic reject or crash signals are more likely to trigger immediate investigation. [source: https://www.anthropic.com/research/trustworthy-agents; https://arxiv.org/abs/2302.12173; https://sre.google/sre-book/monitoring-distributed-systems/]

### §6 Synthesis

**Executive summary:**

Stochastic multi-step Large Language Model agents fail differently from deterministic coded systems because the same unvalidated input can be absorbed as plausible context, branch differently across runs, and propagate a semantically wrong task state without an immediate hard failure. [inference; source: https://www.anthropic.com/research/trustworthy-agents; https://arxiv.org/abs/2302.12173; https://arxiv.org/abs/2312.14197; https://arxiv.org/abs/2408.04667; https://arxiv.org/abs/2502.20747]
Deterministic coded systems can still be wrong or become globally opaque at production scale, but their local bogus-input failures are more often explicit, replayable, and classifiable through conventional fault-error-failure models and monitoring signals. [inference; source: https://ieeexplore.ieee.org/document/1335465/; https://sre.google/sre-book/monitoring-distributed-systems/; https://davidamitchell.github.io/Research/research/2026-05-18-agentic-explainability-vs-traditional.html]
Production evidence from Large Language Model serving shows that even when incidents are detected automatically, mitigation remains manual and slow, which is consistent with stochastic systems needing richer observability because ordinary operational telemetry does not fully capture their failure mechanisms. [inference; source: https://cloudintelligenceworkshop.org/papers/aiops26-Ranganathan.pdf; https://arxiv.org/abs/2411.05285]
Current evidence supports a narrower asymmetry: stochastic systems are more likely to fail silently and variably at the semantic layer, while deterministic systems are more likely to fail loudly or at least reproducibly at the execution boundary. [inference; source: https://ieeexplore.ieee.org/document/1335465/; https://sre.google/sre-book/monitoring-distributed-systems/; https://arxiv.org/abs/2302.12173; https://arxiv.org/abs/2312.14197; https://arxiv.org/abs/2408.04667; https://arxiv.org/abs/2502.20747]

**Key findings:**

1. **Stochastic multi-step Large Language Model systems are more likely than deterministic coded systems to continue operating after an invalid or attacker-shaped input while silently shifting toward a semantically wrong task state, because external text can be reinterpreted as instructions instead of rejected as malformed input.** ([inference]; medium confidence; source: https://www.anthropic.com/research/trustworthy-agents; https://arxiv.org/abs/2302.12173; https://arxiv.org/abs/2312.14197; https://www.microsoft.com/en-us/msrc/blog/2025/07/how-microsoft-defends-against-indirect-prompt-injection-attacks)
2. **Deterministic coded systems usually expose the same bogus-input failure through explicit reject, exception, timeout, or replayable wrong-state behavior, which makes the local failure path easier to reproduce and inspect even when the wider service graph is complex.** ([inference]; medium confidence; source: https://ieeexplore.ieee.org/document/1335465/; https://sre.google/sre-book/monitoring-distributed-systems/; https://davidamitchell.github.io/Research/research/2026-05-18-agentic-explainability-vs-traditional.html)
3. **Repeated-run evidence shows that supposedly deterministic Large Language Model settings still produce materially different outputs and assessment paths on identical prompts, which weakens exact replay of one invalid-input failure path relative to deterministic software.** ([inference]; medium confidence; source: https://arxiv.org/abs/2408.04667; https://arxiv.org/abs/2502.20747; https://davidamitchell.github.io/Research/research/2026-05-09-llm-determinism-limits-temperature-zero.html)
4. **The most distinctive agent-only failure mechanisms in the reviewed evidence are semantic drift, same-model verifier collapse, and tool or memory-mediated error propagation, because the system can keep acting on a corrupted latent task representation instead of stopping at the original boundary violation.** ([inference]; medium confidence; source: https://arxiv.org/abs/2310.01798; https://davidamitchell.github.io/Research/research/2026-05-18-rq4-2-adversarial-error-propagation.html; https://arxiv.org/abs/2302.12173; https://arxiv.org/abs/2312.14197)
5. **Production incident evidence from Large Language Model serving and recent agent-observability research together support an inferential conclusion that stochastic systems need richer observability than conventional service monitoring alone.** ([inference]; medium confidence; source: https://cloudintelligenceworkshop.org/papers/aiops26-Ranganathan.pdf; https://arxiv.org/abs/2411.05285)
6. **Both deterministic and stochastic systems fit the same abstract fault, error, and failure chain, but the practical asymmetry is where failure becomes visible: deterministic systems more often fail at the execution boundary, while stochastic systems more often fail later at the semantic interpretation layer.** ([inference]; medium confidence; source: https://ieeexplore.ieee.org/document/1335465/; https://arxiv.org/abs/2503.00563; https://arxiv.org/abs/2302.12173; https://arxiv.org/abs/2312.14197)
7. **Large deterministic systems can still become globally opaque at scale, but current evidence does not support collapsing the two classes into the same failure model, because local replayability remains stronger on the deterministic side even when global explanation remains hard.** ([inference]; medium confidence; source: https://sre.google/sre-book/monitoring-distributed-systems/; https://davidamitchell.github.io/Research/research/2026-05-18-agentic-explainability-vs-traditional.html)

**Evidence map:**

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [inference] Unvalidated external content can be absorbed as instructions and keep a stochastic agent running with the wrong task state. | https://www.anthropic.com/research/trustworthy-agents ; https://arxiv.org/abs/2302.12173 ; https://arxiv.org/abs/2312.14197 ; https://www.microsoft.com/en-us/msrc/blog/2025/07/how-microsoft-defends-against-indirect-prompt-injection-attacks | Medium | semantic boundary failure |
| [inference] Deterministic coded systems usually surface bogus-input failures as explicit or replayable boundary failures. | https://ieeexplore.ieee.org/document/1335465/ ; https://sre.google/sre-book/monitoring-distributed-systems/ ; https://davidamitchell.github.io/Research/research/2026-05-18-agentic-explainability-vs-traditional.html | Medium | local replayability |
| [inference] Identical prompts still produce materially different outputs under supposedly deterministic Large Language Model settings, which weakens exact replay of one invalid-input failure path relative to deterministic software. | https://arxiv.org/abs/2408.04667 ; https://arxiv.org/abs/2502.20747 ; https://davidamitchell.github.io/Research/research/2026-05-09-llm-determinism-limits-temperature-zero.html | Medium | repeated-run evidence |
| [inference] Semantic drift, same-model verifier collapse, and tool or memory-mediated propagation are distinctive stochastic-agent failure mechanisms. | https://arxiv.org/abs/2310.01798 ; https://arxiv.org/abs/2302.12173 ; https://arxiv.org/abs/2312.14197 ; https://davidamitchell.github.io/Research/research/2026-05-18-rq4-2-adversarial-error-propagation.html | Medium | multi-step amplification |
| [inference] Large Language Model serving incident evidence plus recent agent-observability research support the conclusion that stochastic systems need richer observability than conventional service monitoring alone. | https://cloudintelligenceworkshop.org/papers/aiops26-Ranganathan.pdf ; https://arxiv.org/abs/2411.05285 | Medium | operational evidence |
| [inference] Both system classes fit the same fault-error-failure abstraction, but visibility shifts from execution boundary to semantic layer in stochastic systems. | https://ieeexplore.ieee.org/document/1335465/ ; https://arxiv.org/abs/2503.00563 ; https://arxiv.org/abs/2302.12173 ; https://arxiv.org/abs/2312.14197 | Medium | comparison axis |
| [inference] Global opacity in deterministic distributed systems does not erase their stronger local replayability. | https://sre.google/sre-book/monitoring-distributed-systems/ ; https://davidamitchell.github.io/Research/research/2026-05-18-agentic-explainability-vs-traditional.html | Medium | scale caveat |

**Assumptions:**

- [assumption] No reviewed source provides a controlled head-to-head experiment in which the exact same unvalidated inputs are fed into both a deterministic workflow and a stochastic agent, so this item assumes that comparing formal failure properties plus production studies is a defensible proxy. [source: https://arxiv.org/abs/2503.00563; https://cloudintelligenceworkshop.org/papers/aiops26-Ranganathan.pdf]
- [assumption] The deterministic comparison assumes fixed code, configuration, and initial state, because distributed concurrency and deployment churn can create additional complexity that is operationally important but not identical to intrinsic stochastic branching. [source: https://sre.google/sre-book/monitoring-distributed-systems/; https://davidamitchell.github.io/Research/research/2026-05-18-agentic-explainability-vs-traditional.html]
- [assumption] "Unvalidated input" covers both syntactically malformed payloads and semantically misleading but locally plausible content, because both kinds of input are relevant to where each system class exposes or hides failure. [source: https://arxiv.org/abs/2302.12173; https://arxiv.org/abs/2312.14197; https://sre.google/sre-book/monitoring-distributed-systems/]

**Analysis:**

The most strongly supported parts of the evidence base are repeated-run Large Language Model nondeterminism, prompt-injection and indirect prompt-injection vulnerability, and conventional software-operations expectations that bogus-input failures surface through explicit monitoring and root-cause repair. [inference; source: https://arxiv.org/abs/2408.04667; https://arxiv.org/abs/2502.20747; https://arxiv.org/abs/2302.12173; https://arxiv.org/abs/2312.14197; https://sre.google/sre-book/monitoring-distributed-systems/]
The comparative conclusion therefore rests less on one direct benchmark and more on how these evidence families fit together: stochastic agents add path variance and a tendency to absorb semantically misleading input as plausible context on top of ordinary software failure, while deterministic systems keep stronger local replayability even when they become globally hard to understand. [inference; source: https://arxiv.org/abs/2503.00563; https://sre.google/sre-book/monitoring-distributed-systems/; https://davidamitchell.github.io/Research/research/2026-05-18-agentic-explainability-vs-traditional.html]
A plausible rival interpretation is that large deterministic distributed systems are already so opaque that the comparison gap disappears in practice. [inference; source: https://sre.google/sre-book/monitoring-distributed-systems/; https://davidamitchell.github.io/Research/research/2026-05-18-agentic-explainability-vs-traditional.html]
The reviewed evidence does not support that stronger claim, because the operational difficulty of understanding the whole deterministic system is not the same as having one input induce different failure paths across identical reruns or being silently reinterpreted as instructions. [inference; source: https://arxiv.org/abs/2302.12173; https://arxiv.org/abs/2312.14197; https://arxiv.org/abs/2408.04667; https://arxiv.org/abs/2502.20747; https://sre.google/sre-book/monitoring-distributed-systems/]

**Risks, gaps, uncertainties:**

- There is no direct controlled benchmark in the reviewed evidence that feeds the same corpus of unvalidated inputs into matched deterministic and stochastic production systems, so the comparison remains a synthesis rather than a single-study verdict. [assumption; source: https://arxiv.org/abs/2503.00563; https://cloudintelligenceworkshop.org/papers/aiops26-Ranganathan.pdf]
- The strongest production telemetry source is about Large Language Model serving rather than full autonomous tool-using agents, so the observability conclusion is stronger for model operations than for every possible agent architecture. [inference; source: https://cloudintelligenceworkshop.org/papers/aiops26-Ranganathan.pdf; https://arxiv.org/abs/2411.05285]
- The deterministic side is grounded in formal taxonomy and Site Reliability Engineering practice more than in a modern benchmark dedicated specifically to bogus-input failure visibility across microservice stacks. [inference; source: https://ieeexplore.ieee.org/document/1335465/; https://sre.google/sre-book/monitoring-distributed-systems/]

**Open questions:**

- Which fraction of real production agent incidents begin as explicit hard failures versus silent semantic degradations?
- What trace schema is minimally sufficient to reconstruct a stochastic agent's branch path after an incident?
- Under what constraints can structured outputs or deterministic harness layers convert a stochastic semantic failure into a deterministic reject path?
- How should the next item, Research Question 5.2, model the loss of formal verifiability as branch variance increases?

### §7 Recursive Review

- review_result: pass
- acronym_audit: passed
- domain_term_audit: passed
- claim_label_audit: passed
- synthesis_findings_parity: aligned
- unresolved_contradictions: none material
- confidence_setting: medium

---

## Findings

*(Populated from §6 Synthesis above.)*

### Executive Summary

Stochastic multi-step Large Language Model agents fail differently from deterministic coded systems because the same unvalidated input can be absorbed as plausible context, branch differently across runs, and propagate a semantically wrong task state without an immediate hard failure. [inference; source: https://www.anthropic.com/research/trustworthy-agents; https://arxiv.org/abs/2302.12173; https://arxiv.org/abs/2312.14197; https://arxiv.org/abs/2408.04667; https://arxiv.org/abs/2502.20747]
Deterministic coded systems can still be wrong or become globally opaque at production scale, but their local bogus-input failures are more often explicit, replayable, and classifiable through conventional fault-error-failure models and monitoring signals. [inference; source: https://ieeexplore.ieee.org/document/1335465/; https://sre.google/sre-book/monitoring-distributed-systems/; https://davidamitchell.github.io/Research/research/2026-05-18-agentic-explainability-vs-traditional.html]
Production evidence from Large Language Model serving shows that even when incidents are detected automatically, mitigation remains manual and slow, which is consistent with stochastic systems needing richer observability because ordinary operational telemetry does not fully capture their failure mechanisms. [inference; source: https://cloudintelligenceworkshop.org/papers/aiops26-Ranganathan.pdf; https://arxiv.org/abs/2411.05285]
Current evidence supports a narrower asymmetry: stochastic systems are more likely to fail silently and variably at the semantic layer, while deterministic systems are more likely to fail loudly or at least reproducibly at the execution boundary. [inference; source: https://ieeexplore.ieee.org/document/1335465/; https://sre.google/sre-book/monitoring-distributed-systems/; https://arxiv.org/abs/2302.12173; https://arxiv.org/abs/2312.14197; https://arxiv.org/abs/2408.04667; https://arxiv.org/abs/2502.20747]

### Key Findings

1. **Stochastic multi-step Large Language Model systems are more likely than deterministic coded systems to continue operating after an invalid or attacker-shaped input while silently shifting toward a semantically wrong task state, because external text can be reinterpreted as instructions instead of rejected as malformed input.** ([inference]; medium confidence; source: https://www.anthropic.com/research/trustworthy-agents; https://arxiv.org/abs/2302.12173; https://arxiv.org/abs/2312.14197; https://www.microsoft.com/en-us/msrc/blog/2025/07/how-microsoft-defends-against-indirect-prompt-injection-attacks)
2. **Deterministic coded systems usually expose the same bogus-input failure through explicit reject, exception, timeout, or replayable wrong-state behavior, which makes the local failure path easier to reproduce and inspect even when the wider service graph is complex.** ([inference]; medium confidence; source: https://ieeexplore.ieee.org/document/1335465/; https://sre.google/sre-book/monitoring-distributed-systems/; https://davidamitchell.github.io/Research/research/2026-05-18-agentic-explainability-vs-traditional.html)
3. **Repeated-run evidence shows that supposedly deterministic Large Language Model settings still produce materially different outputs and assessment paths on identical prompts, which weakens exact replay of one invalid-input failure path relative to deterministic software.** ([inference]; medium confidence; source: https://arxiv.org/abs/2408.04667; https://arxiv.org/abs/2502.20747; https://davidamitchell.github.io/Research/research/2026-05-09-llm-determinism-limits-temperature-zero.html)
4. **The most distinctive agent-only failure mechanisms in the reviewed evidence are semantic drift, same-model verifier collapse, and tool or memory-mediated error propagation, because the system can keep acting on a corrupted latent task representation instead of stopping at the original boundary violation.** ([inference]; medium confidence; source: https://arxiv.org/abs/2310.01798; https://davidamitchell.github.io/Research/research/2026-05-18-rq4-2-adversarial-error-propagation.html; https://arxiv.org/abs/2302.12173; https://arxiv.org/abs/2312.14197)
5. **Production incident evidence from Large Language Model serving and recent agent-observability research together support an inferential conclusion that stochastic systems need richer observability than conventional service monitoring alone.** ([inference]; medium confidence; source: https://cloudintelligenceworkshop.org/papers/aiops26-Ranganathan.pdf; https://arxiv.org/abs/2411.05285)
6. **Both deterministic and stochastic systems fit the same abstract fault, error, and failure chain, but the practical asymmetry is where failure becomes visible: deterministic systems more often fail at the execution boundary, while stochastic systems more often fail later at the semantic interpretation layer.** ([inference]; medium confidence; source: https://ieeexplore.ieee.org/document/1335465/; https://arxiv.org/abs/2503.00563; https://arxiv.org/abs/2302.12173; https://arxiv.org/abs/2312.14197)
7. **Large deterministic systems can still become globally opaque at scale, but current evidence does not support collapsing the two classes into the same failure model, because local replayability remains stronger on the deterministic side even when global explanation remains hard.** ([inference]; medium confidence; source: https://sre.google/sre-book/monitoring-distributed-systems/; https://davidamitchell.github.io/Research/research/2026-05-18-agentic-explainability-vs-traditional.html)

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [inference] Unvalidated external content can be absorbed as instructions and keep a stochastic agent running with the wrong task state. | https://www.anthropic.com/research/trustworthy-agents ; https://arxiv.org/abs/2302.12173 ; https://arxiv.org/abs/2312.14197 ; https://www.microsoft.com/en-us/msrc/blog/2025/07/how-microsoft-defends-against-indirect-prompt-injection-attacks | Medium | semantic boundary failure |
| [inference] Deterministic coded systems usually surface bogus-input failures as explicit or replayable boundary failures. | https://ieeexplore.ieee.org/document/1335465/ ; https://sre.google/sre-book/monitoring-distributed-systems/ ; https://davidamitchell.github.io/Research/research/2026-05-18-agentic-explainability-vs-traditional.html | Medium | local replayability |
| [inference] Identical prompts still produce materially different outputs under supposedly deterministic Large Language Model settings, which weakens exact replay of one invalid-input failure path relative to deterministic software. | https://arxiv.org/abs/2408.04667 ; https://arxiv.org/abs/2502.20747 ; https://davidamitchell.github.io/Research/research/2026-05-09-llm-determinism-limits-temperature-zero.html | Medium | repeated-run evidence |
| [inference] Semantic drift, same-model verifier collapse, and tool or memory-mediated propagation are distinctive stochastic-agent failure mechanisms. | https://arxiv.org/abs/2310.01798 ; https://arxiv.org/abs/2302.12173 ; https://arxiv.org/abs/2312.14197 ; https://davidamitchell.github.io/Research/research/2026-05-18-rq4-2-adversarial-error-propagation.html | Medium | multi-step amplification |
| [inference] Large Language Model serving incident evidence plus recent agent-observability research support the conclusion that stochastic systems need richer observability than conventional service monitoring alone. | https://cloudintelligenceworkshop.org/papers/aiops26-Ranganathan.pdf ; https://arxiv.org/abs/2411.05285 | Medium | operational evidence |
| [inference] Both system classes fit the same fault-error-failure abstraction, but visibility shifts from execution boundary to semantic layer in stochastic systems. | https://ieeexplore.ieee.org/document/1335465/ ; https://arxiv.org/abs/2503.00563 ; https://arxiv.org/abs/2302.12173 ; https://arxiv.org/abs/2312.14197 | Medium | comparison axis |
| [inference] Global opacity in deterministic distributed systems does not erase their stronger local replayability. | https://sre.google/sre-book/monitoring-distributed-systems/ ; https://davidamitchell.github.io/Research/research/2026-05-18-agentic-explainability-vs-traditional.html | Medium | scale caveat |

### Assumptions

- No reviewed source provides a controlled head-to-head experiment in which the exact same unvalidated inputs are fed into both a deterministic workflow and a stochastic agent, so this item assumes that comparing formal failure properties plus production studies is a defensible proxy. [assumption; source: https://arxiv.org/abs/2503.00563; https://cloudintelligenceworkshop.org/papers/aiops26-Ranganathan.pdf]
- The deterministic comparison assumes fixed code, configuration, and initial state, because distributed concurrency and deployment churn can create additional complexity that is operationally important but not identical to intrinsic stochastic branching. [assumption; source: https://sre.google/sre-book/monitoring-distributed-systems/; https://davidamitchell.github.io/Research/research/2026-05-18-agentic-explainability-vs-traditional.html]
- "Unvalidated input" covers both syntactically malformed payloads and semantically misleading but locally plausible content, because both kinds of input are relevant to where each system class exposes or hides failure. [assumption; source: https://arxiv.org/abs/2302.12173; https://arxiv.org/abs/2312.14197; https://sre.google/sre-book/monitoring-distributed-systems/]

### Analysis

The most strongly supported parts of the evidence base are repeated-run Large Language Model nondeterminism, prompt-injection and indirect prompt-injection vulnerability, and conventional software-operations expectations that bogus-input failures surface through explicit monitoring and root-cause repair. [inference; source: https://arxiv.org/abs/2408.04667; https://arxiv.org/abs/2502.20747; https://arxiv.org/abs/2302.12173; https://arxiv.org/abs/2312.14197; https://sre.google/sre-book/monitoring-distributed-systems/]
The comparative conclusion therefore rests less on one direct benchmark and more on how these evidence families fit together: stochastic agents add path variance and a tendency to absorb semantically misleading input as plausible context on top of ordinary software failure, while deterministic systems keep stronger local replayability even when they become globally hard to understand. [inference; source: https://arxiv.org/abs/2503.00563; https://sre.google/sre-book/monitoring-distributed-systems/; https://davidamitchell.github.io/Research/research/2026-05-18-agentic-explainability-vs-traditional.html]
A plausible rival interpretation is that large deterministic distributed systems are already so opaque that the comparison gap disappears in practice. [inference; source: https://sre.google/sre-book/monitoring-distributed-systems/; https://davidamitchell.github.io/Research/research/2026-05-18-agentic-explainability-vs-traditional.html]
The reviewed evidence does not support that stronger claim, because the operational difficulty of understanding the whole deterministic system is not the same as having one input induce different failure paths across identical reruns or being silently reinterpreted as instructions. [inference; source: https://arxiv.org/abs/2302.12173; https://arxiv.org/abs/2312.14197; https://arxiv.org/abs/2408.04667; https://arxiv.org/abs/2502.20747; https://sre.google/sre-book/monitoring-distributed-systems/]

### Risks, Gaps, and Uncertainties

- There is no direct controlled benchmark in the reviewed evidence that feeds the same corpus of unvalidated inputs into matched deterministic and stochastic production systems, so the comparison remains a synthesis rather than a single-study verdict. [assumption; source: https://arxiv.org/abs/2503.00563; https://cloudintelligenceworkshop.org/papers/aiops26-Ranganathan.pdf]
- The strongest production telemetry source is about Large Language Model serving rather than full autonomous tool-using agents, so the observability conclusion is stronger for model operations than for every possible agent architecture. [inference; source: https://cloudintelligenceworkshop.org/papers/aiops26-Ranganathan.pdf; https://arxiv.org/abs/2411.05285]
- The deterministic side is grounded in formal taxonomy and Site Reliability Engineering practice more than in a modern benchmark dedicated specifically to bogus-input failure visibility across microservice stacks. [inference; source: https://ieeexplore.ieee.org/document/1335465/; https://sre.google/sre-book/monitoring-distributed-systems/]

### Open Questions

- Which fraction of real production agent incidents begin as explicit hard failures versus silent semantic degradations?
- What trace schema is minimally sufficient to reconstruct a stochastic agent's branch path after an incident?
- Under what constraints can structured outputs or deterministic harness layers convert a stochastic semantic failure into a deterministic reject path?
- How should the next item, Research Question 5.2, model the loss of formal verifiability as branch variance increases?

---

## Output

- Type: knowledge
- Description: Comparative knowledge item showing that deterministic and stochastic systems share the same abstract fault-error-failure chain but differ materially in where failure becomes visible, with stochastic systems more likely to fail silently at the semantic layer and deterministic systems more likely to fail explicitly or replayably at the execution boundary. [inference; source: https://ieeexplore.ieee.org/document/1335465/; https://sre.google/sre-book/monitoring-distributed-systems/; https://arxiv.org/abs/2302.12173; https://arxiv.org/abs/2312.14197; https://arxiv.org/abs/2408.04667; https://arxiv.org/abs/2502.20747]
- Links:
  - https://arxiv.org/abs/2302.12173
  - https://arxiv.org/abs/2408.04667
  - https://cloudintelligenceworkshop.org/papers/aiops26-Ranganathan.pdf
