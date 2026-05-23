---
review_count: 1
title: "Deterministic circuit-breakers and real-time infrastructure constraints for hybrid reasoning stacks"
added: 2026-05-17T11:18:46+00:00
status: completed
priority: high
blocks: []
themes: [ai-architecture, tools-infrastructure, governance-policy, cost-performance, mlops-deployment, agentic-ai]
started: 2026-05-17T13:22:35+00:00
completed: 2026-05-17T13:38:41+00:00
output: []
cites:
  - 2026-05-09-hybrid-architecture-probabilistic-llm-deterministic-governance
  - 2026-04-26-ai-agent-control-plane-architecture-enterprise
  - 2026-04-26-human-in-the-loop-ai-automated-workflows
  - 2026-04-26-ai-lowcode-observability-telemetry-governance
  - 2026-04-26-implicit-rate-limiting-controls-agentic-ai-removal
related:
  - 2026-05-12-hardware-load-inference-performance
  - 2026-05-12-knowledge-graph-agentic-runtime-dependency
  - 2026-04-26-ai-lowcode-failure-modes-governance-mitigation
superseded_by: ~
supersedes: ~
item_type: primary
confidence: medium
versions:
  - version: "1.0"
    changed: 2026-05-17
    sha: c21ecd3e5cc7a85e226d36e89b450c289e12ec02
    progress: progress/2026-05-17-deterministic-circuit-breakers-hybrid-reasoning-infrastructure.md
    summary: Initial completion
---

# Deterministic circuit-breakers and real-time infrastructure constraints for hybrid reasoning stacks

## Research Question

What deterministic control-plane patterns are required to operate hybrid Large Language Model (LLM), Energy-Based Model (EBM), and formal-verifier reasoning loops safely under real-time infrastructure constraints, including bounded-latency convergence failure modes?

## Scope

**In scope:**
- Deterministic circuit-breaker patterns with statically verified fallback states
- Transaction boundary design between probabilistic generation and deterministic actuation
- Dynamic energy-function recalibration from runtime telemetry without destabilizing convergence
- Latency and convergence bounds as policy and constraint complexity scales
- Observability signals needed to trigger safe degradation and rollback paths

**Out of scope:**
- User-interface or product-experience considerations
- Formal policy encoding details, covered in the policy and formal verification companion item
- Generative state abstraction design details, covered in the interface companion item

**Constraints:** Focus on patterns suitable for production systems with strict service-level objectives and auditable failure handling.

## Context

Hybrid reasoning stacks already separate stochastic interpretation from deterministic enforcement, so the central operational question is how to keep that boundary safe when the internal search process is iterative, deadline-sensitive, and allowed to fail closed rather than act optimistically. [inference; source: https://davidamitchell.github.io/Research/research/2026-05-09-hybrid-architecture-probabilistic-llm-deterministic-governance.html; https://davidamitchell.github.io/Research/research/2026-04-26-ai-agent-control-plane-architecture-enterprise.html]

The control problem is not only model accuracy, but also bounded-latency actuation: once a hybrid stack sits on a live infrastructure path, missed convergence deadlines, verifier backlog, and overload-driven retries can widen blast radius unless deterministic fallback states already exist. [inference; source: https://sre.google/sre-book/addressing-cascading-failures/; https://aws.amazon.com/builders-library/timeouts-retries-and-backoff-with-jitter/; https://davidamitchell.github.io/Research/research/2026-04-26-implicit-rate-limiting-controls-agentic-ai-removal.html]

## Approach

1. What deterministic circuit-breaker architecture best protects control paths?
   1a. What are the trigger conditions for non-convergence and unsafe uncertainty?
   1b. What fallback baselines can be pre-verified for safe execution?
2. Where should probabilistic-to-deterministic transaction boundaries sit?
   2a. Which boundary patterns reduce unsafe side effects?
   2b. How should boundary contracts be enforced and audited?
3. How can runtime telemetry be injected into energy functions safely?
   3a. Which telemetry classes improve adaptation versus destabilize optimization?
   3b. What guardrails prevent oscillation or runaway behavior?
4. What are realistic latency bounds for EBM-guided reasoning at increasing constraint complexity?
   4a. How does complexity growth affect convergence-time distribution?
   4b. Which scheduling and time-budget policies preserve deterministic service outcomes?

## Sources

- [x] [Microsoft Azure Architecture Center Circuit Breaker pattern](https://learn.microsoft.com/azure/architecture/patterns/circuit-breaker)
- [x] [Microsoft Azure Architecture Center Retry pattern](https://learn.microsoft.com/azure/architecture/patterns/retry)
- [x] [Microsoft Azure Architecture Center Throttling pattern](https://learn.microsoft.com/azure/architecture/patterns/throttling)
- [x] [Microsoft Azure Architecture Center Bulkhead pattern](https://learn.microsoft.com/azure/architecture/patterns/bulkhead)
- [x] [Google SRE Book Addressing Cascading Failures](https://sre.google/sre-book/addressing-cascading-failures/)
- [x] [Google SRE Book Handling Overload](https://sre.google/sre-book/handling-overload/)
- [x] [AWS Builders' Library Timeouts, retries, and backoff with jitter](https://aws.amazon.com/builders-library/timeouts-retries-and-backoff-with-jitter/)
- [x] [AWS Builders' Library Using load shedding to avoid overload](https://aws.amazon.com/builders-library/using-load-shedding-to-avoid-overload/)
- [x] [AWS Builders' Library Static stability using Availability Zones](https://aws.amazon.com/builders-library/static-stability-using-availability-zones/)
- [x] [AWS Well-Architected REL11-BP05 Use static stability to prevent bimodal behavior](https://docs.aws.amazon.com/wellarchitected/2022-03-31/framework/rel_withstand_component_failures_static_stability.html)
- [x] [Mehmood et al. (2022) The Black-Box Simplex Architecture for Runtime Assurance of Autonomous Cyber-Physical Systems](https://arxiv.org/abs/2102.12981)
- [x] [Desai et al. (2019) SOTER: A Runtime Assurance Framework for Programming Safe Robotics Systems](https://arxiv.org/abs/1808.07921)
- [x] [Yang et al. (2024) Case Study: Runtime Safety Verification of Neural Network Controlled System](https://arxiv.org/abs/2408.08592)
- [x] [Du et al. (2022) Learning Iterative Reasoning through Energy Minimization](https://arxiv.org/abs/2206.15448)
- [x] [Du et al. (2024) Learning Iterative Reasoning through Energy Diffusion](https://openreview.net/forum?id=CduFAALvGe)
- [ ] [Nygard (2018) Release It! Design and Deploy Production-Ready Software](https://pragprog.com/titles/mnee2/release-it-second-edition/) - identified as a classic circuit-breaker source, but not directly consulted because the current item relied on accessible platform documentation and runtime-assurance papers for verifiable claims.
- [ ] [LeCun (2022) A Path Towards Autonomous Machine Intelligence](https://arxiv.org/abs/2206.08300) - identified as architectural background, but not directly consulted because the current item relied on later energy-based reasoning papers with explicit convergence and compute-budget claims.
- [x] [Mitchell (2026) Hybrid Architecture Design: Probabilistic Large Language Models (LLMs) for Interpretation, Deterministic Layers for Governance Enforcement](https://davidamitchell.github.io/Research/research/2026-05-09-hybrid-architecture-probabilistic-llm-deterministic-governance.html)
- [x] [Mitchell (2026) What control-plane architecture is required to manage Artificial Intelligence (AI) agents and low-code systems as distributed, semi-autonomous actors within enterprise environments?](https://davidamitchell.github.io/Research/research/2026-04-26-ai-agent-control-plane-architecture-enterprise.html)
- [x] [Mitchell (2026) When and how should human intervention be incorporated into Artificial Intelligence (AI)-driven and automated workflows?](https://davidamitchell.github.io/Research/research/2026-04-26-human-in-the-loop-ai-automated-workflows.html)
- [x] [Mitchell (2026) What observability and telemetry model is required to govern Artificial Intelligence (AI) and low-code systems at scale?](https://davidamitchell.github.io/Research/research/2026-04-26-ai-lowcode-observability-telemetry-governance.html)
- [x] [Mitchell (2026) Implicit rate-limiting controls removed by agentic Artificial Intelligence (AI): blast radius amplification and the operational risk literature gap](https://davidamitchell.github.io/Research/research/2026-04-26-implicit-rate-limiting-controls-agentic-ai-removal.html)
- [x] [Mitchell (2026) Hardware load and Large Language Model (LLM) inference performance: implications for agent reliability](https://davidamitchell.github.io/Research/research/2026-05-12-hardware-load-inference-performance.html)
- [x] [Mitchell (2026) Knowledge Graph in the live execution path of multi-step Large Language Model (LLM) systems: architecture and failure modes](https://davidamitchell.github.io/Research/research/2026-05-12-knowledge-graph-agentic-runtime-dependency.html)

## Related

- [Mitchell (2026) Hybrid Architecture Design: Probabilistic Large Language Models (LLMs) for Interpretation, Deterministic Layers for Governance Enforcement](https://davidamitchell.github.io/Research/research/2026-05-09-hybrid-architecture-probabilistic-llm-deterministic-governance.html)
- [Mitchell (2026) What control-plane architecture is required to manage Artificial Intelligence (AI) agents and low-code systems as distributed, semi-autonomous actors within enterprise environments?](https://davidamitchell.github.io/Research/research/2026-04-26-ai-agent-control-plane-architecture-enterprise.html)
- [Mitchell (2026) Hardware load and Large Language Model (LLM) inference performance: implications for agent reliability](https://davidamitchell.github.io/Research/research/2026-05-12-hardware-load-inference-performance.html)

---

## Research Skill Output

*(Full output from running the research skill, retained verbatim in the completed item. Sections 0-5 are the investigation, and section 6 seeds the Findings section below.)*

### §0 Initialise

- Question: identify deterministic control-plane patterns for safely operating hybrid Large Language Model, Energy-Based Model, and formal-verifier reasoning loops under strict latency and audit constraints.
- Scope: deterministic circuit-breakers, transaction boundaries, telemetry-driven adaptation, latency and convergence budgets, observability, and rollback paths.
- Constraints: production systems only, auditable failure handling, bounded-latency actuation, full research mode.
- Output: full section 0 to section 7 investigation plus Findings with Executive Summary, Key Findings, Evidence Map, Assumptions, Analysis, Risks, Gaps, Uncertainties, Open Questions, and Output.
- [fact; source: https://davidamitchell.github.io/Research/research/2026-05-09-hybrid-architecture-probabilistic-llm-deterministic-governance.html; https://davidamitchell.github.io/Research/research/2026-04-26-ai-agent-control-plane-architecture-enterprise.html; https://davidamitchell.github.io/Research/research/2026-04-26-human-in-the-loop-ai-automated-workflows.html; https://davidamitchell.github.io/Research/research/2026-04-26-ai-lowcode-observability-telemetry-governance.html; https://davidamitchell.github.io/Research/research/2026-04-26-implicit-rate-limiting-controls-agentic-ai-removal.html] Prior completed-item cross-reference: the most relevant completed items already establish deterministic enforcement boundaries, control-plane placement, human stop and override requirements, attributable telemetry, and the operational importance of replacing lost human pacing with engineered controls.
- [fact; source: https://arxiv.org/abs/2102.12981; https://arxiv.org/abs/1808.07921] Working definition: Runtime Assurance (RTA), a supervisory pattern that switches authority from a high-performance controller to a safer baseline when safety margins shrink, is the closest formal control model for the "deterministic circuit-breaker" requirement in this item.
- [fact; source: https://docs.aws.amazon.com/wellarchitected/2022-03-31/framework/rel_withstand_component_failures_static_stability.html; https://aws.amazon.com/builders-library/static-stability-using-availability-zones/] Working definition: statically stable means the fallback path can keep serving or fail safely without depending on a fresh reconfiguration or capacity-creation path during the incident itself.

### §1 Question Decomposition

- **Root question:** what deterministic architecture keeps a hybrid reasoning stack safe when iterative search cannot be trusted to converge before an infrastructure decision deadline?
- **A. Supervisory safety architecture**
  - A1. What runtime-supervision pattern safely transfers authority from an advanced controller to a safe baseline?
  - A2. What concrete circuit-breaker states, counters, and probe rules map to hybrid reasoning loops?
- **B. Transaction boundaries**
  - B1. Where should stochastic reasoning stop and deterministic actuation begin?
  - B2. Which boundary contracts reduce duplicated or unsafe side effects under retries and partial failure?
- **C. Telemetry and adaptation**
  - C1. Which telemetry classes should influence compute budget or fallback choice?
  - C2. Which telemetry-driven adaptations risk destabilizing the optimization objective itself?
- **D. Latency and complexity**
  - D1. How do harder reasoning problems change iterative-compute demand?
  - D2. What deadline and scheduling rules preserve deterministic service outcomes?
- **E. Degradation and rollback**
  - E1. Which fallback states are safe enough to pre-verify?
  - E2. Which observability signals should trip degrade, deny, or human-review modes?

### §2 Investigation

#### 2.1 Prior completed-item sweep

- [fact; source: https://davidamitchell.github.io/Research/research/2026-05-09-hybrid-architecture-probabilistic-llm-deterministic-governance.html] The prior hybrid-architecture item concluded that probabilistic model output should arrive at deterministic control layers as typed proposals rather than as free-form execution authority.
- [fact; source: https://davidamitchell.github.io/Research/research/2026-04-26-ai-agent-control-plane-architecture-enterprise.html] The prior control-plane item concluded that policy decision, policy administration, and enforcement should sit on a separate control plane rather than inside the stochastic execution path.
- [fact; source: https://davidamitchell.github.io/Research/research/2026-04-26-human-in-the-loop-ai-automated-workflows.html] The prior human-oversight item concluded that high-consequence automation needs a real stop or override surface with authority and safe waiting behavior, not nominal review after the fact.
- [fact; source: https://davidamitchell.github.io/Research/research/2026-04-26-implicit-rate-limiting-controls-agentic-ai-removal.html] The implicit-rate-limiting item concluded that moving from human-paced to autonomous execution removes natural friction, so engineered controls must replace the lost blast-radius limit.
- [inference; source: https://davidamitchell.github.io/Research/research/2026-05-09-hybrid-architecture-probabilistic-llm-deterministic-governance.html; https://davidamitchell.github.io/Research/research/2026-04-26-ai-agent-control-plane-architecture-enterprise.html; https://davidamitchell.github.io/Research/research/2026-04-26-human-in-the-loop-ai-automated-workflows.html; https://davidamitchell.github.io/Research/research/2026-04-26-implicit-rate-limiting-controls-agentic-ai-removal.html] This item extends that earlier work from "where deterministic enforcement belongs" to "how deterministic enforcement stays safe when the reasoning layer is iterative, deadline-sensitive, and allowed to fail closed."

#### 2.2 Deterministic circuit-breakers and verified fallback states

- [fact; source: https://learn.microsoft.com/azure/architecture/patterns/circuit-breaker] Azure's circuit-breaker pattern uses Closed, Open, and Half-Open states, trips when recent failures cross a threshold in a time window, fails fast while open, and allows only a limited number of probes while recovering.
- [fact; source: https://sre.google/sre-book/addressing-cascading-failures/] Google SRE says overload is the most common cause of cascading failures, and that slower requests increase in-flight work, saturate queues, miss Remote Procedure Call (RPC) deadlines, and trigger retries that amplify overload.
- [fact; source: https://arxiv.org/abs/2102.12981] Mehmood et al. define the Black-Box Simplex Architecture as a runtime-assurance framework in which control authority may switch from an unverified advanced controller to a backup baseline controller in order to maintain safety.
- [fact; source: https://arxiv.org/abs/1808.07921] Desai et al. say SOTER composes a high-performance uncertified controller, a safer certified controller, and a safety specification into a runtime-assurance module that preserves safety while still using the advanced controller when safe.
- [fact; source: https://arxiv.org/abs/2408.08592] Yang et al. report a safe online controller-switching strategy that moves from a neural-network controller to an obstacle-avoidance controller when runtime verification indicates rising risk.
- [inference; source: https://learn.microsoft.com/azure/architecture/patterns/circuit-breaker; https://arxiv.org/abs/2102.12981; https://arxiv.org/abs/1808.07921; https://arxiv.org/abs/2408.08592] For hybrid reasoning stacks, the circuit-breaker boundary should sit at the deterministic actuation point, where it can treat missed deadlines, failed verifier checks, or unstable search progress as reasons to revoke the advanced controller's authority and hand off to a pre-verified baseline.
- [inference; source: https://learn.microsoft.com/azure/architecture/patterns/circuit-breaker; https://sre.google/sre-book/addressing-cascading-failures/] The Half-Open analogue in a reasoning stack should be limited probe traffic, shadow execution, or low-consequence test requests, not a full restoration of production actuation on the first successful retry.

#### 2.3 Transaction boundaries between probabilistic generation and deterministic actuation

- [fact; source: https://davidamitchell.github.io/Research/research/2026-05-09-hybrid-architecture-probabilistic-llm-deterministic-governance.html] The prior hybrid-architecture item concluded that the deterministic layer needs normalized fields it can validate against schemas, intent checks, policy rules, and approval thresholds.
- [fact; source: https://davidamitchell.github.io/Research/research/2026-04-26-ai-agent-control-plane-architecture-enterprise.html] The prior control-plane item concluded that high-level governance policy should be translated into layer-specific rules and enforced at concrete policy-enforcement points rather than delegated to model prompts.
- [fact; source: https://davidamitchell.github.io/Research/research/2026-04-26-human-in-the-loop-ai-automated-workflows.html] The prior human-oversight item concluded that override and halt mechanisms need a concrete execution point and explicit waiting behavior when human review is required.
- [fact; source: https://aws.amazon.com/builders-library/timeouts-retries-and-backoff-with-jitter/] AWS says a timeout or failure does not necessarily mean side effects did not happen, so retry safety depends on idempotent Application Programming Interface (API) design.
- [inference; source: https://davidamitchell.github.io/Research/research/2026-05-09-hybrid-architecture-probabilistic-llm-deterministic-governance.html; https://davidamitchell.github.io/Research/research/2026-04-26-ai-agent-control-plane-architecture-enterprise.html; https://aws.amazon.com/builders-library/timeouts-retries-and-backoff-with-jitter/] The safe transaction boundary is therefore a typed proposal envelope, including intended action, target surface, side-effect class, deadline, and idempotency key, with the deterministic layer owning allow, deny, degrade, retry, and escalate decisions.
- [inference; source: https://aws.amazon.com/builders-library/timeouts-retries-and-backoff-with-jitter/; https://davidamitchell.github.io/Research/research/2026-04-26-human-in-the-loop-ai-automated-workflows.html] If a proposal cannot clear verification before its remaining time budget expires, the deterministic boundary should return a no-op, a lower-risk deterministic fallback, or a human-review hold state rather than let the stochastic layer make a late best effort.

#### 2.4 Telemetry injection into energy functions without destabilizing convergence

- [fact; source: https://arxiv.org/abs/2206.15448] Du et al. frame reasoning as energy minimization and say harder problems can be assigned a more complex optimization procedure by increasing the underlying computational budget.
- [fact; source: https://openreview.net/forum?id=CduFAALvGe] Du et al.'s iterative reasoning through energy diffusion adapts the number of optimization steps during inference based on problem difficulty and uses annealed energy landscapes to make inference easier and training more stable.
- [fact; source: https://sre.google/sre-book/handling-overload/] Google SRE recommends measuring capacity directly in resource signals such as Central Processing Unit (CPU) consumption rather than relying on crude request-rate proxies, and says degraded responses or local copies can be appropriate under overload.
- [fact; source: https://docs.aws.amazon.com/wellarchitected/2022-03-31/framework/rel_withstand_component_failures_static_stability.html] AWS Well-Architected says statically stable systems should use previously cached values and fixed refresh cadences during failure rather than switch into a new reactive mode that increases dependency load.
- [inference; source: https://arxiv.org/abs/2206.15448; https://openreview.net/forum?id=CduFAALvGe; https://sre.google/sre-book/handling-overload/; https://docs.aws.amazon.com/wellarchitected/2022-03-31/framework/rel_withstand_component_failures_static_stability.html] Runtime telemetry should therefore choose among pre-validated compute budgets, fallback classes, and scheduler settings, but should not directly rewrite the live energy objective inside the same decision loop.
- [inference; source: https://sre.google/sre-book/handling-overload/; https://docs.aws.amazon.com/wellarchitected/2022-03-31/framework/rel_withstand_component_failures_static_stability.html; https://openreview.net/forum?id=CduFAALvGe] Safe telemetry classes are exogenous stability signals such as queue depth, deadline slack, cache-hit rate, iteration count, and rate of energy improvement, whereas unsafe classes are noisy per-request reward surrogates that would make the optimization target itself move while the solver is still trying to converge.
- [assumption; source: https://docs.aws.amazon.com/wellarchitected/2022-03-31/framework/rel_withstand_component_failures_static_stability.html; https://arxiv.org/abs/2102.12981; https://arxiv.org/abs/1808.07921] This item assumes production recalibration of energy-function parameters should occur through versioned rollout or bounded test rollouts rather than unconstrained online self-modification, because the consulted stability and runtime-assurance sources all preserve an external supervisory layer rather than allow the controller to redefine its own safety objective in flight.

#### 2.5 Latency and convergence as constraint complexity scales

- [fact; source: https://arxiv.org/abs/2206.15448] Du et al. say harder problems lead to more complex energy landscapes and may require more computation to reach a low-energy solution.
- [fact; source: https://openreview.net/forum?id=CduFAALvGe] IRED performs best in more challenging scenarios by adaptively increasing inference steps, which implies that iterative compute demand rises with problem difficulty rather than remaining constant.
- [fact; source: https://aws.amazon.com/builders-library/using-load-shedding-to-avoid-overload/] AWS recommends enforcing per-request time-to-live and discarding doomed requests once the remaining deadline can no longer support useful work, rather than continuing work whose result will arrive too late to matter.
- [fact; source: https://davidamitchell.github.io/Research/research/2026-05-12-hardware-load-inference-performance.html] The hardware-load item found that LLM-serving degradation is threshold-based and scheduler-mediated rather than a smooth percentage-of-utilization slowdown, because queueing and batching policy shifts create abrupt latency tails.
- [inference; source: https://arxiv.org/abs/2206.15448; https://openreview.net/forum?id=CduFAALvGe; https://aws.amazon.com/builders-library/using-load-shedding-to-avoid-overload/; https://davidamitchell.github.io/Research/research/2026-05-12-hardware-load-inference-performance.html] Convergence-time distribution in a hybrid reasoning stack will therefore widen non-linearly as constraint sets, branching factor, or verifier cost rise, so deterministic outcomes require hard wall-clock budgets rather than reliance on average completion time.
- [inference; source: https://aws.amazon.com/builders-library/using-load-shedding-to-avoid-overload/; https://sre.google/sre-book/addressing-cascading-failures/; https://aws.amazon.com/builders-library/timeouts-retries-and-backoff-with-jitter/] The practical time-budget policy is to reserve explicit slices for proposal generation, deterministic verification, and commit, and to degrade or deny once remaining time cannot safely cover the later slices.

#### 2.6 Scheduling and isolation policies that preserve deterministic outcomes

- [fact; source: https://learn.microsoft.com/azure/architecture/patterns/bulkhead] Azure's bulkhead pattern isolates pools of resources so failure or excessive load in one dependency does not exhaust the resources needed for unrelated work.
- [fact; source: https://learn.microsoft.com/azure/architecture/patterns/throttling] Azure's throttling pattern preserves service-level objectives by capping or degrading requests once resource thresholds are crossed instead of letting overload collapse the entire system.
- [fact; source: https://aws.amazon.com/builders-library/using-load-shedding-to-avoid-overload/] AWS says overload handling should prioritize critical requests, keep an eye on client deadlines, and drop work that can no longer produce useful results.
- [fact; source: https://sre.google/sre-book/handling-overload/] Google SRE recommends per-customer quotas and adaptive client-side throttling so global overload does not degrade all callers equally.
- [inference; source: https://learn.microsoft.com/azure/architecture/patterns/bulkhead; https://learn.microsoft.com/azure/architecture/patterns/throttling; https://aws.amazon.com/builders-library/using-load-shedding-to-avoid-overload/; https://sre.google/sre-book/handling-overload/] Hybrid reasoning stacks need separate resource-isolation bulkheads and quotas for advisory reasoning, deterministic verification, and actuation-bound traffic so exploratory search cannot starve the very baseline controllers and health checks needed for safe recovery.

#### 2.7 Observability signals that should trip degradation and rollback

- [fact; source: https://learn.microsoft.com/azure/architecture/patterns/circuit-breaker] The Azure circuit-breaker pattern treats failure counters, time windows, state transitions, and probe success in Half-Open state as explicit monitoring surfaces.
- [fact; source: https://davidamitchell.github.io/Research/research/2026-04-26-ai-lowcode-observability-telemetry-governance.html] The observability item concluded that governance evidence must bind system actions to concrete enforcement points, correlation identifiers, and attributable actors rather than to infrastructure logs alone.
- [fact; source: https://davidamitchell.github.io/Research/research/2026-05-12-knowledge-graph-agentic-runtime-dependency.html] The knowledge-graph runtime item concluded that dependency telemetry becomes operationally meaningful only when it is joined to downstream action quality and failure consequences.
- [fact; source: https://aws.amazon.com/builders-library/using-load-shedding-to-avoid-overload/; https://sre.google/sre-book/addressing-cascading-failures/] AWS and Google both treat queue depth, deadline miss risk, wasted work, and retry amplification as first-order signals of an approaching cascade rather than as minor efficiency metrics.
- [inference; source: https://learn.microsoft.com/azure/architecture/patterns/circuit-breaker; https://davidamitchell.github.io/Research/research/2026-04-26-ai-lowcode-observability-telemetry-governance.html; https://davidamitchell.github.io/Research/research/2026-05-12-knowledge-graph-agentic-runtime-dependency.html; https://aws.amazon.com/builders-library/using-load-shedding-to-avoid-overload/; https://sre.google/sre-book/addressing-cascading-failures/] The minimum trip signals for a hybrid reasoning circuit-breaker are remaining deadline slack, iteration count without material energy improvement, verifier queue age, fallback invocation rate, stale-context age, and post-probe success ratio, because only that combined view can tell whether the next actuation is still safe.
- [inference; source: https://davidamitchell.github.io/Research/research/2026-04-26-human-in-the-loop-ai-automated-workflows.html; https://aws.amazon.com/builders-library/static-stability-using-availability-zones/; https://docs.aws.amazon.com/wellarchitected/2022-03-31/framework/rel_withstand_component_failures_static_stability.html] The rollback path should be an auditable no-op, last-known-safe deterministic output, or deferred human review state chosen before execution begins, because the fallback itself must remain statically stable under the same incident that tripped the breaker.

### §3 Reasoning

- [fact; source: https://arxiv.org/abs/2102.12981; https://arxiv.org/abs/1808.07921; https://arxiv.org/abs/2408.08592] The directly evidenced safety pattern is supervisory switching: an advanced controller is allowed to operate only while a monitored safety envelope says it remains safe, and control transfers to a baseline controller before that envelope is exhausted.
- [fact; source: https://learn.microsoft.com/azure/architecture/patterns/circuit-breaker; https://sre.google/sre-book/addressing-cascading-failures/; https://aws.amazon.com/builders-library/using-load-shedding-to-avoid-overload/] The directly evidenced infrastructure pattern is bounded failure handling: systems fail fast, shed load, and stop useless work once deadlines or failure thresholds say further effort would amplify the incident.
- [fact; source: https://arxiv.org/abs/2206.15448; https://openreview.net/forum?id=CduFAALvGe] The directly evidenced reasoning pattern is adaptive compute: harder reasoning tasks require more optimization steps or more complex optimization procedures than easier tasks.
- [inference; source: https://arxiv.org/abs/2102.12981; https://arxiv.org/abs/1808.07921; https://learn.microsoft.com/azure/architecture/patterns/circuit-breaker; https://arxiv.org/abs/2206.15448; https://openreview.net/forum?id=CduFAALvGe] Combining those patterns implies that time budget is itself a safety constraint in a hybrid reasoning stack, because an iterative solver can be correct in principle yet still unsafe in practice if it cannot finish before the deterministic actuation deadline.
- [inference; source: https://sre.google/sre-book/handling-overload/; https://docs.aws.amazon.com/wellarchitected/2022-03-31/framework/rel_withstand_component_failures_static_stability.html; https://openreview.net/forum?id=CduFAALvGe] Claims about telemetry-driven energy-function adaptation are more inferential than claims about circuit-breaker states, because the consulted sources discuss adaptive optimization and operational stability separately rather than offering a single production pattern that joins them.
- [assumption; source: https://arxiv.org/abs/2206.15448; https://openreview.net/forum?id=CduFAALvGe; https://learn.microsoft.com/azure/architecture/patterns/circuit-breaker; https://aws.amazon.com/builders-library/using-load-shedding-to-avoid-overload/] No consulted source presents a production case study of a live LLM plus EBM plus formal-verifier control path in enterprise infrastructure, so the design guidance here is a synthesis of adjacent research and reliability patterns rather than a direct copy of one documented deployment.

### §4 Consistency Check

- [fact; source: https://learn.microsoft.com/azure/architecture/patterns/circuit-breaker; https://arxiv.org/abs/2102.12981; https://arxiv.org/abs/1808.07921] The consulted sources agree that a higher-performance controller should lose authority when monitored safety conditions fail, even though they differ on whether the trigger is failure count, formal safety envelope, or runtime verification.
- [fact; source: https://arxiv.org/abs/2206.15448; https://openreview.net/forum?id=CduFAALvGe] The consulted energy-based reasoning papers agree that problem difficulty can justify more iterative compute, and neither claims that convergence time remains constant as constraints grow harder.
- [fact; source: https://sre.google/sre-book/addressing-cascading-failures/; https://aws.amazon.com/builders-library/using-load-shedding-to-avoid-overload/] The consulted infrastructure sources agree that overload and deadline miss can turn useful work into wasted work and amplify retries or queues.
- [inference; source: https://arxiv.org/abs/2206.15448; https://openreview.net/forum?id=CduFAALvGe; https://sre.google/sre-book/addressing-cascading-failures/; https://aws.amazon.com/builders-library/using-load-shedding-to-avoid-overload/] The main tension is between adaptive compute, which improves hard-case accuracy, and deterministic infrastructure, which requires bounded latency; the design only remains coherent if adaptive compute itself is subordinated to deadline-aware supervision and safe fallback.
- [inference; source: https://docs.aws.amazon.com/wellarchitected/2022-03-31/framework/rel_withstand_component_failures_static_stability.html; https://learn.microsoft.com/azure/architecture/patterns/circuit-breaker] For that reason, the item narrows "dynamic recalibration" from live objective rewriting to versioned or bounded adaptation plus per-request budget selection, which removes the contradiction between adaptation and static stability.

### §5 Depth and Breadth Expansion

- [inference; source: https://docs.aws.amazon.com/wellarchitected/2022-03-31/framework/rel_withstand_component_failures_static_stability.html; https://aws.amazon.com/builders-library/static-stability-using-availability-zones/; https://arxiv.org/abs/1808.07921] **Technical lens:** the safest architecture pays for pre-verified fallback capacity and simpler baseline controllers up front, because attempting to create a new fallback path only after the incident begins is itself a second failure mode.
- [inference; source: https://docs.aws.amazon.com/wellarchitected/2022-03-31/framework/rel_withstand_component_failures_static_stability.html; https://learn.microsoft.com/azure/architecture/patterns/bulkhead] **Economic lens:** static stability, bulkheads, and reserved verifier capacity cost more during quiet periods, but they buy down the nonlinear cost of cascade failure, retry storms, and recovery-time uncertainty.
- [inference; source: https://davidamitchell.github.io/Research/research/2026-04-26-human-in-the-loop-ai-automated-workflows.html; https://davidamitchell.github.io/Research/research/2026-04-26-ai-lowcode-observability-telemetry-governance.html] **Governance lens:** explicit stop states, attributable traces, and documented fallback selection are easier to defend than opaque "the model usually converges" claims, because they preserve auditable human and policy authority even when the stochastic layer misbehaves.
- [inference; source: https://davidamitchell.github.io/Research/research/2026-04-26-implicit-rate-limiting-controls-agentic-ai-removal.html; https://sre.google/sre-book/handling-overload/] **Historical and behavioral lens:** deterministic circuit-breakers in agentic systems replace an implicit human pacing mechanism that previously absorbed bursts and hesitation, so their absence recreates the same blast-radius problem earlier automation transitions exposed.
- [inference; source: https://davidamitchell.github.io/Research/research/2026-05-12-knowledge-graph-agentic-runtime-dependency.html; https://davidamitchell.github.io/Research/research/2026-04-26-ai-lowcode-observability-telemetry-governance.html] **Operational lens:** telemetry should be evaluated by whether it predicts unsafe actuation or degradation of decision quality, not by whether it makes dashboards look complete, because hybrid stacks fail at the join between dependency health and action consequence.

### §6 Synthesis

**Executive summary:**

Deterministic operation of hybrid reasoning stacks requires a Runtime Assurance supervisory boundary at the actuation point, where missed deadlines, failed verifier checks, or unstable search progress transfer authority to a pre-verified baseline or safe no-op state. [inference; source: https://arxiv.org/abs/2102.12981; https://arxiv.org/abs/1808.07921; https://learn.microsoft.com/azure/architecture/patterns/circuit-breaker]

The probabilistic layer can search, rank, and justify, but it should only emit typed proposals; deterministic layers must own schema validation, policy checks, idempotent commit, degrade, deny, and escalate decisions. [inference; source: https://davidamitchell.github.io/Research/research/2026-05-09-hybrid-architecture-probabilistic-llm-deterministic-governance.html; https://davidamitchell.github.io/Research/research/2026-04-26-ai-agent-control-plane-architecture-enterprise.html; https://aws.amazon.com/builders-library/timeouts-retries-and-backoff-with-jitter/]

Runtime telemetry should adjust compute budgets and choose among pre-validated fallback classes, but should not rewrite the live energy objective during the same request, because adaptive compute helps hard problems while static-stability guidance says failure handling must avoid new reactive modes under stress. [inference; source: https://arxiv.org/abs/2206.15448; https://openreview.net/forum?id=CduFAALvGe; https://docs.aws.amazon.com/wellarchitected/2022-03-31/framework/rel_withstand_component_failures_static_stability.html]

As constraint complexity and verifier cost grow, latency tails widen non-linearly, so deterministic service outcomes depend on hard wall-clock budgets, bulkheads, load shedding, and auditable rollback states rather than on average convergence time. [inference; source: https://aws.amazon.com/builders-library/using-load-shedding-to-avoid-overload/; https://sre.google/sre-book/addressing-cascading-failures/; https://learn.microsoft.com/azure/architecture/patterns/bulkhead; https://davidamitchell.github.io/Research/research/2026-05-12-hardware-load-inference-performance.html]

**Key findings:**

1. **A production hybrid reasoning stack should place a Runtime Assurance supervisory boundary at the deterministic actuation point, because the strongest available evidence shows that advanced controllers remain safe only while a monitored envelope allows them to keep authority.** ([inference]; high confidence; source: https://arxiv.org/abs/2102.12981; https://arxiv.org/abs/1808.07921; https://arxiv.org/abs/2408.08592; https://learn.microsoft.com/azure/architecture/patterns/circuit-breaker)
2. **The safe probabilistic-to-deterministic transaction boundary is a typed proposal envelope with explicit action class, target surface, deadline, and idempotency key, because retries and partial failures otherwise create duplicated or widened side effects that the stochastic layer cannot safely arbitrate alone.** ([inference]; high confidence; source: https://aws.amazon.com/builders-library/timeouts-retries-and-backoff-with-jitter/; https://davidamitchell.github.io/Research/research/2026-05-09-hybrid-architecture-probabilistic-llm-deterministic-governance.html; https://davidamitchell.github.io/Research/research/2026-04-26-ai-agent-control-plane-architecture-enterprise.html)
3. **Runtime telemetry should tune compute budget, scheduler class, and fallback selection rather than rewrite the live energy objective in the same request, because adaptive optimization helps hard cases but operational-stability guidance rejects reactive mode changes that create new failure paths under load.** ([inference]; medium confidence; source: https://arxiv.org/abs/2206.15448; https://openreview.net/forum?id=CduFAALvGe; https://sre.google/sre-book/handling-overload/; https://docs.aws.amazon.com/wellarchitected/2022-03-31/framework/rel_withstand_component_failures_static_stability.html)
4. **Convergence-time distribution in hybrid reasoning loops should be treated as threshold-driven rather than smoothly elastic, because harder energy landscapes, verifier cost, queueing policy, and hardware contention all widen latency tails abruptly once budgets or scheduler thresholds are crossed.** ([inference]; medium confidence; source: https://arxiv.org/abs/2206.15448; https://openreview.net/forum?id=CduFAALvGe; https://aws.amazon.com/builders-library/using-load-shedding-to-avoid-overload/; https://davidamitchell.github.io/Research/research/2026-05-12-hardware-load-inference-performance.html)
5. **Safe degradation needs statically stable fallback states, such as no-op, cached last-known-safe output, lower-fidelity deterministic policy, or deferred human review, because the fallback path itself must not depend on a new reconfiguration step during the incident.** ([inference]; high confidence; source: https://docs.aws.amazon.com/wellarchitected/2022-03-31/framework/rel_withstand_component_failures_static_stability.html; https://aws.amazon.com/builders-library/static-stability-using-availability-zones/; https://davidamitchell.github.io/Research/research/2026-04-26-human-in-the-loop-ai-automated-workflows.html)
6. **Priority rules and resource-isolation bulkheads should reserve capacity for health checks, baseline controllers, and actuation-bound verifier lanes ahead of advisory reasoning traffic, because overload in exploratory search can otherwise starve the exact control surfaces needed for safe recovery.** ([inference]; high confidence; source: https://learn.microsoft.com/azure/architecture/patterns/bulkhead; https://learn.microsoft.com/azure/architecture/patterns/throttling; https://aws.amazon.com/builders-library/using-load-shedding-to-avoid-overload/; https://sre.google/sre-book/handling-overload/)
7. **Observability for hybrid reasoning stacks must track deadline slack, rate of energy improvement, verifier queue age, fallback rate, and post-probe recovery success together with attributable action traces, because infrastructure counters alone do not reveal whether the next actuation remains safe.** ([inference]; medium confidence; source: https://learn.microsoft.com/azure/architecture/patterns/circuit-breaker; https://davidamitchell.github.io/Research/research/2026-04-26-ai-lowcode-observability-telemetry-governance.html; https://davidamitchell.github.io/Research/research/2026-05-12-knowledge-graph-agentic-runtime-dependency.html; https://aws.amazon.com/builders-library/using-load-shedding-to-avoid-overload/)

**Evidence map:**

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [inference] A production hybrid reasoning stack should place a Runtime Assurance supervisory boundary at the deterministic actuation point. | https://arxiv.org/abs/2102.12981; https://arxiv.org/abs/1808.07921; https://arxiv.org/abs/2408.08592; https://learn.microsoft.com/azure/architecture/patterns/circuit-breaker | high | supervisory switching |
| [inference] The safe transaction boundary is a typed proposal envelope with action class, deadline, and idempotency key. | https://aws.amazon.com/builders-library/timeouts-retries-and-backoff-with-jitter/; https://davidamitchell.github.io/Research/research/2026-05-09-hybrid-architecture-probabilistic-llm-deterministic-governance.html; https://davidamitchell.github.io/Research/research/2026-04-26-ai-agent-control-plane-architecture-enterprise.html | high | commit boundary |
| [inference] Telemetry should tune compute budgets and fallback selection rather than rewrite the live energy objective. | https://arxiv.org/abs/2206.15448; https://openreview.net/forum?id=CduFAALvGe; https://sre.google/sre-book/handling-overload/; https://docs.aws.amazon.com/wellarchitected/2022-03-31/framework/rel_withstand_component_failures_static_stability.html | medium | stable adaptation |
| [inference] Convergence-time distribution should be treated as threshold-driven rather than smoothly elastic. | https://arxiv.org/abs/2206.15448; https://openreview.net/forum?id=CduFAALvGe; https://aws.amazon.com/builders-library/using-load-shedding-to-avoid-overload/; https://davidamitchell.github.io/Research/research/2026-05-12-hardware-load-inference-performance.html | medium | tail latency |
| [inference] Safe degradation needs statically stable fallback states chosen before execution begins. | https://docs.aws.amazon.com/wellarchitected/2022-03-31/framework/rel_withstand_component_failures_static_stability.html; https://aws.amazon.com/builders-library/static-stability-using-availability-zones/; https://davidamitchell.github.io/Research/research/2026-04-26-human-in-the-loop-ai-automated-workflows.html | high | one-mode fallback |
| [inference] Priority rules and resource-isolation bulkheads should reserve capacity for verifier and baseline-controller lanes. | https://learn.microsoft.com/azure/architecture/patterns/bulkhead; https://learn.microsoft.com/azure/architecture/patterns/throttling; https://aws.amazon.com/builders-library/using-load-shedding-to-avoid-overload/; https://sre.google/sre-book/handling-overload/ | high | isolation and quotas |
| [inference] Observability must combine control-surface telemetry with attributable action traces. | https://learn.microsoft.com/azure/architecture/patterns/circuit-breaker; https://davidamitchell.github.io/Research/research/2026-04-26-ai-lowcode-observability-telemetry-governance.html; https://davidamitchell.github.io/Research/research/2026-05-12-knowledge-graph-agentic-runtime-dependency.html; https://aws.amazon.com/builders-library/using-load-shedding-to-avoid-overload/ | medium | trip-signal bundle |

**Assumptions:**

- [assumption; source: https://arxiv.org/abs/2102.12981; https://arxiv.org/abs/1808.07921] The formal verifier and supervisory layer can make a transfer-of-authority decision fast enough to fit inside the actuation deadline for the relevant control path.
- [assumption; source: https://docs.aws.amazon.com/wellarchitected/2022-03-31/framework/rel_withstand_component_failures_static_stability.html; https://aws.amazon.com/builders-library/static-stability-using-availability-zones/] Each actuation class has at least one lower-capability fallback state that is useful enough to pre-verify and keep statically stable.
- [assumption; source: https://arxiv.org/abs/2206.15448; https://openreview.net/forum?id=CduFAALvGe; https://docs.aws.amazon.com/wellarchitected/2022-03-31/framework/rel_withstand_component_failures_static_stability.html] Production teams can separate parameter-rollout cadence from per-request inference so that telemetry-driven adaptation does not become uncontrolled in-loop self-modification.

**Analysis:**

The clearest direct evidence in the consulted material comes from runtime-assurance and circuit-breaker literature, not from enterprise LLM case studies. [inference; source: https://arxiv.org/abs/2102.12981; https://arxiv.org/abs/1808.07921; https://learn.microsoft.com/azure/architecture/patterns/circuit-breaker]

That evidence is still decision-useful because the question is architectural rather than benchmark-specific: it asks who should retain authority when a high-performance controller becomes unsafe or too slow, and those sources answer that exact supervisory problem. [inference; source: https://arxiv.org/abs/2102.12981; https://arxiv.org/abs/1808.07921; https://arxiv.org/abs/2408.08592]

The main competing remedy would be to rely on better models, more accelerator capacity, or larger human-review teams instead of deterministic circuit-breakers. [inference; source: https://davidamitchell.github.io/Research/research/2026-05-12-hardware-load-inference-performance.html; https://davidamitchell.github.io/Research/research/2026-04-26-human-in-the-loop-ai-automated-workflows.html]

The consulted overload and retry literature does not support that as a full substitute, because faster or larger systems still experience queue saturation, deadline miss, retry amplification, and wasted work once load exceeds the safe envelope. [fact; source: https://sre.google/sre-book/addressing-cascading-failures/; https://aws.amazon.com/builders-library/using-load-shedding-to-avoid-overload/; https://aws.amazon.com/builders-library/timeouts-retries-and-backoff-with-jitter/]

For that reason, the best-supported design is not "optimize until the fallback is unnecessary" but "treat optimization as conditional authority under a deterministic supervisor." [inference; source: https://arxiv.org/abs/2102.12981; https://learn.microsoft.com/azure/architecture/patterns/circuit-breaker; https://davidamitchell.github.io/Research/research/2026-05-09-hybrid-architecture-probabilistic-llm-deterministic-governance.html]

The weakest part of the evidence base concerns live telemetry injection into energy functions, because the consulted papers show adaptive compute and more stable annealed landscapes, while the operations sources show why unstable reactive modes are dangerous, but none gives a production recipe for joining those two concerns. [inference; source: https://arxiv.org/abs/2206.15448; https://openreview.net/forum?id=CduFAALvGe; https://docs.aws.amazon.com/wellarchitected/2022-03-31/framework/rel_withstand_component_failures_static_stability.html]

That is why the synthesis keeps telemetry-driven adaptation at the control-plane and budget-selection level rather than claiming high confidence in per-request objective rewrites. [inference; source: https://openreview.net/forum?id=CduFAALvGe; https://docs.aws.amazon.com/wellarchitected/2022-03-31/framework/rel_withstand_component_failures_static_stability.html]

**Risks, gaps, uncertainties:**

- [inference; source: https://arxiv.org/abs/2206.15448; https://openreview.net/forum?id=CduFAALvGe] The evidence base for EBM-guided reasoning is strong enough to justify adaptive-compute claims, but thin on production data about hard real-time enterprise control paths.
- [inference; source: https://arxiv.org/abs/2102.12981; https://arxiv.org/abs/1808.07921; https://arxiv.org/abs/2408.08592] Runtime-assurance evidence comes mainly from cyber-physical and robotics settings, so applying it to enterprise reasoning stacks requires architectural translation rather than one-to-one reuse.
- [inference; source: https://docs.aws.amazon.com/wellarchitected/2022-03-31/framework/rel_withstand_component_failures_static_stability.html; https://aws.amazon.com/builders-library/static-stability-using-availability-zones/] Static stability trades higher steady-state cost and design effort for better incident behavior, and the cost threshold at which teams will actually adopt that trade remains organization-specific.

**Open questions:**

- How should a formal verifier expose partial-progress evidence so the circuit-breaker can distinguish "slow but converging" from "oscillating and unsafe" without trusting the stochastic layer's self-report?
- What verifier designs keep proof or model-check latency predictable enough for tight enterprise service-level objectives when policy complexity grows?
- Which telemetry-derived budget classes are stable enough to update automatically, and which always require human approval through the control plane?

### §7 Recursive Review

- Review result: pass.
- Acronym audit: Large Language Model (LLM), Energy-Based Model (EBM), Runtime Assurance (RTA), Remote Procedure Call (RPC), and Application Programming Interface (API) are expanded on first use in the document.
- Claim audit: every claim in Research Skill Output and Findings is labeled as fact, inference, or assumption, and each claim-bearing sentence is bound to URL-backed sources.
- Cross-item audit: prior completed items on hybrid architecture, control-plane design, human oversight, observability, hardware load, knowledge-graph runtime dependency, and implicit rate limiting are integrated where they sharpen the same governance surface.
- Remaining uncertainty: telemetry-driven objective recalibration, medium-confidence synthesis.

---

## Findings

*(Populated from §6 Synthesis above.)*

### Executive Summary

Deterministic operation of hybrid reasoning stacks requires a Runtime Assurance supervisory boundary at the actuation point, where missed deadlines, failed verifier checks, or unstable search progress transfer authority to a pre-verified baseline or safe no-op state. [inference; source: https://arxiv.org/abs/2102.12981; https://arxiv.org/abs/1808.07921; https://learn.microsoft.com/azure/architecture/patterns/circuit-breaker]

The probabilistic layer can search, rank, and justify, but it should only emit typed proposals, while deterministic layers own schema validation, policy checks, idempotent commit, degrade, deny, and escalate decisions. [inference; source: https://davidamitchell.github.io/Research/research/2026-05-09-hybrid-architecture-probabilistic-llm-deterministic-governance.html; https://davidamitchell.github.io/Research/research/2026-04-26-ai-agent-control-plane-architecture-enterprise.html; https://aws.amazon.com/builders-library/timeouts-retries-and-backoff-with-jitter/]

Runtime telemetry should adjust compute budgets and choose among pre-validated fallback classes, but should not rewrite the live energy objective during the same request, because adaptive compute helps hard problems while static-stability guidance says failure handling must avoid new reactive modes under stress. [inference; source: https://arxiv.org/abs/2206.15448; https://openreview.net/forum?id=CduFAALvGe; https://docs.aws.amazon.com/wellarchitected/2022-03-31/framework/rel_withstand_component_failures_static_stability.html]

As constraint complexity and verifier cost grow, latency tails widen non-linearly, so deterministic service outcomes depend on hard wall-clock budgets, bulkheads, load shedding, and auditable rollback states rather than on average convergence time. [inference; source: https://aws.amazon.com/builders-library/using-load-shedding-to-avoid-overload/; https://sre.google/sre-book/addressing-cascading-failures/; https://learn.microsoft.com/azure/architecture/patterns/bulkhead; https://davidamitchell.github.io/Research/research/2026-05-12-hardware-load-inference-performance.html]

### Key Findings

1. **A production hybrid reasoning stack should place a Runtime Assurance supervisory boundary at the deterministic actuation point, because the strongest available evidence shows that advanced controllers remain safe only while a monitored envelope allows them to keep authority.** ([inference]; high confidence; source: https://arxiv.org/abs/2102.12981; https://arxiv.org/abs/1808.07921; https://arxiv.org/abs/2408.08592; https://learn.microsoft.com/azure/architecture/patterns/circuit-breaker)
2. **The safe probabilistic-to-deterministic transaction boundary is a typed proposal envelope with explicit action class, target surface, deadline, and idempotency key, because retries and partial failures otherwise create duplicated or widened side effects that the stochastic layer cannot safely arbitrate alone.** ([inference]; high confidence; source: https://aws.amazon.com/builders-library/timeouts-retries-and-backoff-with-jitter/; https://davidamitchell.github.io/Research/research/2026-05-09-hybrid-architecture-probabilistic-llm-deterministic-governance.html; https://davidamitchell.github.io/Research/research/2026-04-26-ai-agent-control-plane-architecture-enterprise.html)
3. **Runtime telemetry should tune compute budget, scheduler class, and fallback selection rather than rewrite the live energy objective in the same request, because adaptive optimization helps hard cases but operational-stability guidance rejects reactive mode changes that create new failure paths under load.** ([inference]; medium confidence; source: https://arxiv.org/abs/2206.15448; https://openreview.net/forum?id=CduFAALvGe; https://sre.google/sre-book/handling-overload/; https://docs.aws.amazon.com/wellarchitected/2022-03-31/framework/rel_withstand_component_failures_static_stability.html)
4. **Convergence-time distribution in hybrid reasoning loops should be treated as threshold-driven rather than smoothly elastic, because harder energy landscapes, verifier cost, queueing policy, and hardware contention all widen latency tails abruptly once budgets or scheduler thresholds are crossed.** ([inference]; medium confidence; source: https://arxiv.org/abs/2206.15448; https://openreview.net/forum?id=CduFAALvGe; https://aws.amazon.com/builders-library/using-load-shedding-to-avoid-overload/; https://davidamitchell.github.io/Research/research/2026-05-12-hardware-load-inference-performance.html)
5. **Safe degradation needs statically stable fallback states, such as no-op, cached last-known-safe output, lower-fidelity deterministic policy, or deferred human review, because the fallback path itself must not depend on a new reconfiguration step during the incident.** ([inference]; high confidence; source: https://docs.aws.amazon.com/wellarchitected/2022-03-31/framework/rel_withstand_component_failures_static_stability.html; https://aws.amazon.com/builders-library/static-stability-using-availability-zones/; https://davidamitchell.github.io/Research/research/2026-04-26-human-in-the-loop-ai-automated-workflows.html)
6. **Priority rules and resource-isolation bulkheads should reserve capacity for health checks, baseline controllers, and actuation-bound verifier lanes ahead of advisory reasoning traffic, because overload in exploratory search can otherwise starve the exact control surfaces needed for safe recovery.** ([inference]; high confidence; source: https://learn.microsoft.com/azure/architecture/patterns/bulkhead; https://learn.microsoft.com/azure/architecture/patterns/throttling; https://aws.amazon.com/builders-library/using-load-shedding-to-avoid-overload/; https://sre.google/sre-book/handling-overload/)
7. **Observability for hybrid reasoning stacks must track deadline slack, rate of energy improvement, verifier queue age, fallback rate, and post-probe recovery success together with attributable action traces, because infrastructure counters alone do not reveal whether the next actuation remains safe.** ([inference]; medium confidence; source: https://learn.microsoft.com/azure/architecture/patterns/circuit-breaker; https://davidamitchell.github.io/Research/research/2026-04-26-ai-lowcode-observability-telemetry-governance.html; https://davidamitchell.github.io/Research/research/2026-05-12-knowledge-graph-agentic-runtime-dependency.html; https://aws.amazon.com/builders-library/using-load-shedding-to-avoid-overload/)

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [inference] A production hybrid reasoning stack should place a Runtime Assurance supervisory boundary at the deterministic actuation point. | https://arxiv.org/abs/2102.12981; https://arxiv.org/abs/1808.07921; https://arxiv.org/abs/2408.08592; https://learn.microsoft.com/azure/architecture/patterns/circuit-breaker | high | supervisory switching |
| [inference] The safe transaction boundary is a typed proposal envelope with action class, deadline, and idempotency key. | https://aws.amazon.com/builders-library/timeouts-retries-and-backoff-with-jitter/; https://davidamitchell.github.io/Research/research/2026-05-09-hybrid-architecture-probabilistic-llm-deterministic-governance.html; https://davidamitchell.github.io/Research/research/2026-04-26-ai-agent-control-plane-architecture-enterprise.html | high | commit boundary |
| [inference] Telemetry should tune compute budgets and fallback selection rather than rewrite the live energy objective. | https://arxiv.org/abs/2206.15448; https://openreview.net/forum?id=CduFAALvGe; https://sre.google/sre-book/handling-overload/; https://docs.aws.amazon.com/wellarchitected/2022-03-31/framework/rel_withstand_component_failures_static_stability.html | medium | stable adaptation |
| [inference] Convergence-time distribution should be treated as threshold-driven rather than smoothly elastic. | https://arxiv.org/abs/2206.15448; https://openreview.net/forum?id=CduFAALvGe; https://aws.amazon.com/builders-library/using-load-shedding-to-avoid-overload/; https://davidamitchell.github.io/Research/research/2026-05-12-hardware-load-inference-performance.html | medium | tail latency |
| [inference] Safe degradation needs statically stable fallback states chosen before execution begins. | https://docs.aws.amazon.com/wellarchitected/2022-03-31/framework/rel_withstand_component_failures_static_stability.html; https://aws.amazon.com/builders-library/static-stability-using-availability-zones/; https://davidamitchell.github.io/Research/research/2026-04-26-human-in-the-loop-ai-automated-workflows.html | high | one-mode fallback |
| [inference] Priority rules and resource-isolation bulkheads should reserve capacity for verifier and baseline-controller lanes. | https://learn.microsoft.com/azure/architecture/patterns/bulkhead; https://learn.microsoft.com/azure/architecture/patterns/throttling; https://aws.amazon.com/builders-library/using-load-shedding-to-avoid-overload/; https://sre.google/sre-book/handling-overload/ | high | isolation and quotas |
| [inference] Observability must combine control-surface telemetry with attributable action traces. | https://learn.microsoft.com/azure/architecture/patterns/circuit-breaker; https://davidamitchell.github.io/Research/research/2026-04-26-ai-lowcode-observability-telemetry-governance.html; https://davidamitchell.github.io/Research/research/2026-05-12-knowledge-graph-agentic-runtime-dependency.html; https://aws.amazon.com/builders-library/using-load-shedding-to-avoid-overload/ | medium | trip-signal bundle |

### Assumptions

- [assumption; source: https://arxiv.org/abs/2102.12981; https://arxiv.org/abs/1808.07921] The formal verifier and supervisory layer can make a transfer-of-authority decision fast enough to fit inside the actuation deadline for the relevant control path.
- [assumption; source: https://docs.aws.amazon.com/wellarchitected/2022-03-31/framework/rel_withstand_component_failures_static_stability.html; https://aws.amazon.com/builders-library/static-stability-using-availability-zones/] Each actuation class has at least one lower-capability fallback state that is useful enough to pre-verify and keep statically stable.
- [assumption; source: https://arxiv.org/abs/2206.15448; https://openreview.net/forum?id=CduFAALvGe; https://docs.aws.amazon.com/wellarchitected/2022-03-31/framework/rel_withstand_component_failures_static_stability.html] Production teams can separate parameter-rollout cadence from per-request inference so that telemetry-driven adaptation does not become uncontrolled in-loop self-modification.

### Analysis

The clearest direct evidence in the consulted material comes from runtime-assurance and circuit-breaker literature, not from enterprise LLM case studies. [inference; source: https://arxiv.org/abs/2102.12981; https://arxiv.org/abs/1808.07921; https://learn.microsoft.com/azure/architecture/patterns/circuit-breaker]

That evidence is still decision-useful because the question is architectural rather than benchmark-specific: it asks who should retain authority when a high-performance controller becomes unsafe or too slow, and those sources answer that exact supervisory problem. [inference; source: https://arxiv.org/abs/2102.12981; https://arxiv.org/abs/1808.07921; https://arxiv.org/abs/2408.08592]

The main competing remedy would be to rely on better models, more accelerator capacity, or larger human-review teams instead of deterministic circuit-breakers. [inference; source: https://davidamitchell.github.io/Research/research/2026-05-12-hardware-load-inference-performance.html; https://davidamitchell.github.io/Research/research/2026-04-26-human-in-the-loop-ai-automated-workflows.html]

The consulted overload and retry literature does not support that as a full substitute, because faster or larger systems still experience queue saturation, deadline miss, retry amplification, and wasted work once load exceeds the safe envelope. [fact; source: https://sre.google/sre-book/addressing-cascading-failures/; https://aws.amazon.com/builders-library/using-load-shedding-to-avoid-overload/; https://aws.amazon.com/builders-library/timeouts-retries-and-backoff-with-jitter/]

For that reason, the best-supported design is not "optimize until the fallback is unnecessary" but "treat optimization as conditional authority under a deterministic supervisor." [inference; source: https://arxiv.org/abs/2102.12981; https://learn.microsoft.com/azure/architecture/patterns/circuit-breaker; https://davidamitchell.github.io/Research/research/2026-05-09-hybrid-architecture-probabilistic-llm-deterministic-governance.html]

The weakest part of the evidence base concerns live telemetry injection into energy functions, because the consulted papers show adaptive compute and more stable annealed landscapes, while the operations sources show why unstable reactive modes are dangerous, but none gives a production recipe for joining those two concerns. [inference; source: https://arxiv.org/abs/2206.15448; https://openreview.net/forum?id=CduFAALvGe; https://docs.aws.amazon.com/wellarchitected/2022-03-31/framework/rel_withstand_component_failures_static_stability.html]

That is why the synthesis keeps telemetry-driven adaptation at the control-plane and budget-selection level rather than claiming high confidence in per-request objective rewrites. [inference; source: https://openreview.net/forum?id=CduFAALvGe; https://docs.aws.amazon.com/wellarchitected/2022-03-31/framework/rel_withstand_component_failures_static_stability.html]

### Risks, Gaps, and Uncertainties

- [inference; source: https://arxiv.org/abs/2206.15448; https://openreview.net/forum?id=CduFAALvGe] The evidence base for EBM-guided reasoning is strong enough to justify adaptive-compute claims, but thin on production data about hard real-time enterprise control paths.
- [inference; source: https://arxiv.org/abs/2102.12981; https://arxiv.org/abs/1808.07921; https://arxiv.org/abs/2408.08592] Runtime-assurance evidence comes mainly from cyber-physical and robotics settings, so applying it to enterprise reasoning stacks requires architectural translation rather than one-to-one reuse.
- [inference; source: https://docs.aws.amazon.com/wellarchitected/2022-03-31/framework/rel_withstand_component_failures_static_stability.html; https://aws.amazon.com/builders-library/static-stability-using-availability-zones/] Static stability trades higher steady-state cost and design effort for better incident behavior, and the cost threshold at which teams will actually adopt that trade remains organization-specific.

### Open Questions

- How should a formal verifier expose partial-progress evidence so the circuit-breaker can distinguish "slow but converging" from "oscillating and unsafe" without trusting the stochastic layer's self-report?
- What verifier designs keep proof or model-check latency predictable enough for tight enterprise service-level objectives when policy complexity grows?
- Which telemetry-derived budget classes are stable enough to update automatically, and which always require human approval through the control plane?

---

## Output

- Type: knowledge
- Description: Research synthesis on runtime assurance, deterministic transaction boundaries, and overload-safe fallback design for hybrid reasoning stacks.
- Links:
  - https://arxiv.org/abs/2102.12981
  - https://learn.microsoft.com/azure/architecture/patterns/circuit-breaker
  - https://aws.amazon.com/builders-library/using-load-shedding-to-avoid-overload/
