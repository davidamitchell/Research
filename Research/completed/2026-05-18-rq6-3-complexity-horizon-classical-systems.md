---
review_count: 2
title: "Research Question 6.3: The Complexity Horizon, When Classical Microservice Architectures Become as Opaque as Neural Networks"
added: 2026-05-18T19:40:00+00:00
status: completed
priority: high
blocks:
  - 2026-05-18-rq5-1-stochastic-vs-deterministic-failures
tags: [formal-methods, distributed-systems, epistemology, llm]
started: 2026-05-19T21:21:11+00:00
completed: 2026-05-19T21:40:13+00:00
output: [knowledge]
cites:
  - 2026-05-18-rq6-1-halting-problem-static-analysis
  - 2026-05-18-rq6-2-state-explosion-chaos-theory
  - 2026-05-18-rq5-1-stochastic-vs-deterministic-failures
  - 2026-05-18-agentic-explainability-vs-traditional
related:
  - 2026-05-18-rq5-2-flexibility-vs-predictability-auditability
  - 2026-05-18-rq2-3-predictive-model-fragility
superseded_by: ~
supersedes: ~
item_type: primary
confidence: medium
versions:
  - version: "1.0"
    sha: e260e4419c598852c2812c13a2a21f4891035ceb
    changed: 2026-05-19
    progress: progress/2026-05-19-rq6-3-complexity-horizon-classical-systems.md
    summary: "Initial completion"
---

# Research Question 6.3: The Complexity Horizon, When Classical Microservice Architectures Become as Opaque as Neural Networks

## Research Question

In what ways does the Complexity Horizon of deeply nested, microservice-oriented classical architectures create an epistemic barrier where a deterministic system becomes just as uninterpretable and opaque to human operators as a neural network?

## Scope

**In scope:**
- Emergent behaviour in distributed microservice architectures: system-level properties not deducible from individual service specifications
- Epistemic opacity in large distributed systems: the point at which human operators can no longer form reliable mental models of system state
- Simon's "Architecture of Complexity": hierarchical decomposition as a coping mechanism and its limits
- Dekker's "Drift into Failure": how complex systems degrade gradually without any single visible cause
- Formal characterisation of the Complexity Horizon as a function of service count, coupling, and depth of nesting

**Out of scope:**
- Specific microservice frameworks or cloud-vendor platforms beyond what illustrates the formal argument
- Remediation strategies for distributed system complexity

**Constraints:** Synthesises Phase 6 and prepares for Phase 5 comparison; must establish that the opacity of classical systems is a real phenomenon, not just a comparison rhetorical device, that warrants being placed alongside Large Language Model (LLM) opacity.

## Context

Research Question 6.1 showed that non-trivial semantic properties of unrestricted programs are undecidable, and Research Question 6.2 showed that deterministic systems can still become dynamically unpredictable through state explosion and sensitivity. [fact; source: https://davidamitchell.github.io/Research/research/2026-05-18-rq6-1-halting-problem-static-analysis.html; https://davidamitchell.github.io/Research/research/2026-05-18-rq6-2-state-explosion-chaos-theory.html]

This item applies those results to microservice architectures, where many independently deployable services, asynchronous calls, and long dependency chains can make whole-system behaviour hard to explain from local specifications alone. [inference; source: https://martinfowler.com/articles/microservices.html; https://arxiv.org/abs/2407.01710; https://sre.google/sre-book/monitoring-distributed-systems/]

The intended comparison is therefore bounded: not that deterministic systems become stochastic, but that production-scale deterministic systems can become globally opaque enough that operators rely on traces, aggregate signals, and controlled experiments rather than direct mental simulation of the whole. [inference; source: https://sre.google/sre-book/monitoring-distributed-systems/; https://principlesofchaos.org/; https://davidamitchell.github.io/Research/research/2026-05-18-rq5-1-stochastic-vs-deterministic-failures.html]

## Approach

1. Define the Complexity Horizon formally: the system scale at which no individual or team can maintain a reliable mental model of runtime behaviour.
2. Apply Simon's (1962) Architecture of Complexity: hierarchical decomposition delays but does not eliminate the Complexity Horizon.
3. Apply Dekker's (2011) Drift into Failure: in deeply nested systems, no individual component fails, and the system drifts collectively into failure states that are invisible until catastrophe.
4. Characterise emergent behaviour in microservice architectures: properties (latency spikes, cascading timeouts, split-brain events) that are not predictable from individual service specs.
5. Construct the parallel: the Complexity Horizon of classical systems is to deterministic opacity what the causal hierarchy barrier is to stochastic Large Language Model opacity, and test whether both are fundamental rather than accidental.

## Sources

- [x] [Simon, H. A. (1962) The Architecture of Complexity, Portable Document Format mirror](https://faculty.sites.iastate.edu/tesfatsi/archive/tesfatsi/ArchitectureOfComplexity.HSimon1962.pdf)
- [x] [SFI Press The Architect of Complexity, Simon (1962)](https://www.sfipress.org/21-simon-1962)
- [x] [Dekker (2011) Drift into Failure](https://www.routledge.com/Drift-into-Failure/Dekker/p/book/9781409422211)
- [x] [Nygard (2018) Release It! Design and Deploy Production-Ready Software](https://pragprog.com/titles/mnee2/release-it-second-edition/)
- [x] [Rosenthal et al. (2017) Chaos Engineering](https://arxiv.org/abs/1702.05843)
- [x] [Principles of Chaos Engineering](https://principlesofchaos.org/)
- [x] [Google Site Reliability Engineering (SRE) Book Monitoring Distributed Systems](https://sre.google/sre-book/monitoring-distributed-systems/)
- [x] [Google Site Reliability Engineering (SRE) Book Addressing Cascading Failures](https://sre.google/sre-book/addressing-cascading-failures/)
- [x] [Zhang et al. (2025) Failure Diagnosis in Microservice Systems: A Comprehensive Survey and Analysis](https://arxiv.org/abs/2407.01710)
- [x] [Fowler and Lewis (2014) Microservices](https://martinfowler.com/articles/microservices.html)
- [x] [Research Question 6.1: The Halting Problem and Rice's Theorem, the Absolute Boundary of Static Analysis for Coded Systems](https://davidamitchell.github.io/Research/research/2026-05-18-rq6-1-halting-problem-static-analysis.html)
- [x] [Research Question 6.2: State Space Explosion and Deterministic Chaos, Fragility Shared Between Concurrent Coded Systems and Machine Learning Models](https://davidamitchell.github.io/Research/research/2026-05-18-rq6-2-state-explosion-chaos-theory.html)
- [x] [Research Question 5.1: Stochastic versus Deterministic Failure Modes on Identical Unvalidated Inputs](https://davidamitchell.github.io/Research/research/2026-05-18-rq5-1-stochastic-vs-deterministic-failures.html)
- [x] [Are Multi-Step Large Language Model-Based Systems Inherently Less Explainable Than Equivalently Scoped Deterministic Software Systems?](https://davidamitchell.github.io/Research/research/2026-05-18-agentic-explainability-vs-traditional.html)

## Related

- [Research Question 6.1: The Halting Problem and Rice's Theorem, the Absolute Boundary of Static Analysis for Coded Systems](https://davidamitchell.github.io/Research/research/2026-05-18-rq6-1-halting-problem-static-analysis.html)
- [Research Question 6.2: State Space Explosion and Deterministic Chaos, Fragility Shared Between Concurrent Coded Systems and Machine Learning Models](https://davidamitchell.github.io/Research/research/2026-05-18-rq6-2-state-explosion-chaos-theory.html)
- [Research Question 5.1: Stochastic versus Deterministic Failure Modes on Identical Unvalidated Inputs](https://davidamitchell.github.io/Research/research/2026-05-18-rq5-1-stochastic-vs-deterministic-failures.html)
- [Are Multi-Step Large Language Model-Based Systems Inherently Less Explainable Than Equivalently Scoped Deterministic Software Systems?](https://davidamitchell.github.io/Research/research/2026-05-18-agentic-explainability-vs-traditional.html)

---

## Research Skill Output

*(Full output from running the research skill, retained verbatim in the completed item. Sections 0 to 5 are the investigation, and Section 6 seeds the Findings section below.)*

### §0 Initialise

Question: In what ways does a production-scale microservice architecture create a real epistemic barrier for operators, such that a deterministic system becomes as globally opaque as a neural-network system for incident explanation and prediction?
Scope: Simon on hierarchy and near-decomposability, microservice decomposition, cascading and emergent failures, Dekker's drift framing, and the bounded comparison with Large Language Model opacity.
Constraints: full-mode investigation, URL-backed citations only, canonical tags only, and direct cross-reference to prior completed repository items where they qualify the conclusion.
Output: executive summary, key findings, evidence map, assumptions, analysis, risks, gaps, uncertainties, open questions, and output metadata.
- [fact] Simon defines a complex system as one made up of many parts that interact in a nonsimple way, so that inferring the properties of the whole from the properties of the parts is not trivial, and he argues that complexity frequently takes the form of hierarchy. [source: https://faculty.sites.iastate.edu/tesfatsi/archive/tesfatsi/ArchitectureOfComplexity.HSimon1962.pdf]
- [fact] Simon defines a hierarchic system as one composed of interrelated subsystems that are themselves hierarchic, and he summarizes nearly decomposable systems as ones where short-run subsystem behaviour is approximately independent while long-run dependence appears only in aggregate form. [source: https://faculty.sites.iastate.edu/tesfatsi/archive/tesfatsi/ArchitectureOfComplexity.HSimon1962.pdf]
- [inference] For this item, the Complexity Horizon means the point at which service count, dependency degree, and nesting depth create more relevant cross-service states and interactions than operators can track directly, so explanation shifts from mental simulation to monitoring, tracing, and controlled experiment. [source: https://faculty.sites.iastate.edu/tesfatsi/archive/tesfatsi/ArchitectureOfComplexity.HSimon1962.pdf; https://sre.google/sre-book/monitoring-distributed-systems/; https://principlesofchaos.org/; https://davidamitchell.github.io/Research/research/2026-05-18-rq6-2-state-explosion-chaos-theory.html]
Prior completed-item check:
  - [fact] Research Question 6.1 established a theorem-level limit on static semantic knowledge of arbitrary programs. [source: https://davidamitchell.github.io/Research/research/2026-05-18-rq6-1-halting-problem-static-analysis.html]
  - [fact] Research Question 6.2 established that deterministic systems can still become practically hard to predict because reachable states and perturbation sensitivity grow beyond tractable inspection. [source: https://davidamitchell.github.io/Research/research/2026-05-18-rq6-2-state-explosion-chaos-theory.html]
  - [fact] Research Question 5.1 concluded that deterministic distributed systems can become globally opaque without losing stronger local replayability than stochastic systems. [source: https://davidamitchell.github.io/Research/research/2026-05-18-rq5-1-stochastic-vs-deterministic-failures.html]
  - [fact] The completed explainability comparison concluded that deterministic distributed software loses global transparency at scale even though it retains stronger local replayability than Large Language Model systems. [source: https://davidamitchell.github.io/Research/research/2026-05-18-agentic-explainability-vs-traditional.html]
  - [inference] This item therefore tests a narrower bridge claim than "all complex systems are the same": microservice decomposition delays opacity, but beyond a complexity horizon deterministic systems become globally opaque enough to justify a bounded side-by-side comparison with neural-network or Large Language Model systems. [source: https://davidamitchell.github.io/Research/research/2026-05-18-rq5-1-stochastic-vs-deterministic-failures.html; https://davidamitchell.github.io/Research/research/2026-05-18-agentic-explainability-vs-traditional.html]

### §1 Question Decomposition

1. Simon's hierarchy and its limit
   1.1 What does Simon mean by hierarchy in a complex system?
   1.2 What does near-decomposability buy in the short run and in the long run?
   1.3 Why does that make decomposition a delay mechanism rather than a complete solution?
2. Microservice architecture as applied hierarchy
   2.1 What properties of microservices make them a hierarchic or modular decomposition strategy?
   2.2 What new cross-service interaction surface appears once components are split into out-of-process services?
3. Emergent behaviour and cascades
   3.1 What evidence shows that healthy local services can still generate unexpected system-level outcomes?
   3.2 How do overload, retries, dependency chains, and cascading failures create global behaviour not obvious from one service specification?
4. Drift and operator knowledge limits
   4.1 What does Dekker's drift framing add beyond single-component failure models?
   4.2 What does Site Reliability Engineering practice say about the limits of direct human understanding in large distributed systems?
5. Complexity Horizon synthesis
   5.1 How should the Complexity Horizon be defined so it is about epistemic manageability rather than raw component count alone?
   5.2 In what sense does deterministic global opacity converge with neural-network opacity?
   5.3 In what sense does deterministic replayability remain a surviving asymmetry?

### §2 Investigation

#### Identified but not consulted

- [ ] [Simon and Ando (1961) Aggregation of Variables in Dynamic Systems](https://doi.org/10.2307/1909288)

#### A. Simon's hierarchy explains why complex systems can be analysed locally first

- [fact] Simon defines a complex system as one with many parts that interact in a nonsimple way, so that inferring whole-system properties from part properties is not trivial. [source: https://faculty.sites.iastate.edu/tesfatsi/archive/tesfatsi/ArchitectureOfComplexity.HSimon1962.pdf]
- [fact] Simon defines a hierarchic system as one composed of interrelated subsystems that are themselves hierarchic down to some lower level of elementary subsystem. [source: https://faculty.sites.iastate.edu/tesfatsi/archive/tesfatsi/ArchitectureOfComplexity.HSimon1962.pdf]
- [fact] Simon argues that complexity frequently takes the form of hierarchy and that hierarchy is one of the central structural schemes used by the architect of complexity. [source: https://faculty.sites.iastate.edu/tesfatsi/archive/tesfatsi/ArchitectureOfComplexity.HSimon1962.pdf; https://www.sfipress.org/21-simon-1962]
- [fact] Simon summarizes nearly decomposable systems with two propositions: short-run behaviour of each component subsystem is approximately independent of the others, while long-run behaviour depends on the others only in an aggregate way. [source: https://faculty.sites.iastate.edu/tesfatsi/archive/tesfatsi/ArchitectureOfComplexity.HSimon1962.pdf]
- [inference] Simon's framework implies that decomposition works by suppressing interaction detail for bounded intervals and bounded questions, not by removing cross-subsystem dependence altogether. [source: https://faculty.sites.iastate.edu/tesfatsi/archive/tesfatsi/ArchitectureOfComplexity.HSimon1962.pdf]

#### B. Microservices implement hierarchy through explicit service boundaries, but out-of-process decomposition creates a larger interaction surface

- [fact] Fowler and Lewis define the microservice style as developing one application as a suite of small services, each in its own process and communicating through lightweight mechanisms, with independent deployment and explicit remote interfaces. [source: https://martinfowler.com/articles/microservices.html]
- [fact] Fowler and Lewis also note that remote calls are more expensive than in-process calls and that changing responsibility allocation across components becomes harder once behaviour crosses process boundaries. [source: https://martinfowler.com/articles/microservices.html]
- [fact] Zhang et al. state that modern microservice systems are widely adopted for scalability and flexibility, but their independent deployment and dynamic interactions create unique failure-diagnosis challenges and can lead to cascading failures. [source: https://arxiv.org/abs/2407.01710]
- [fact] Nygard's publisher description says the second edition of *Release It!* addresses today's larger, more complex, heavily virtualized systems and treats systemic problems in large-scale systems as a central production concern. [source: https://pragprog.com/titles/mnee2/release-it-second-edition/]
- [inference] Microservice decomposition therefore converts one large internal complexity into many explicit service boundaries and runtime dependencies, which improves modular ownership locally while expanding the space of cross-service interactions that must be coordinated globally. [source: https://martinfowler.com/articles/microservices.html; https://arxiv.org/abs/2407.01710; https://pragprog.com/titles/mnee2/release-it-second-edition/]

#### C. Emergent behaviour in microservices appears when locally healthy services interact badly at system level

- [fact] The Principles of Chaos Engineering state that even when all individual services in a distributed system are functioning properly, interactions among those services can still cause unpredictable outcomes. [source: https://principlesofchaos.org/]
- [fact] The same Principles of Chaos Engineering page lists systemic weaknesses such as improper fallbacks, retry storms, downstream overload, and cascading failures from a single point of failure as examples of how distributed systems fail at system level. [source: https://principlesofchaos.org/]
- [fact] Rosenthal et al. describe Chaos Engineering as an experimental approach for distributed systems with complex behaviour and failure modes. [source: https://arxiv.org/abs/1702.05843]
- [fact] Google's cascading-failure chapter defines a cascading failure as one that grows over time because a local failure increases the probability of failure elsewhere through positive feedback. [source: https://sre.google/sre-book/addressing-cascading-failures/]
- [fact] The same Google chapter explains that overload, retries, missed deadlines, cache collapse, and health-check failure can reinforce one another so that the visible symptom is not necessarily the original local trigger. [source: https://sre.google/sre-book/addressing-cascading-failures/]
- [inference] These sources jointly show emergent behaviour in the relevant bounded sense: system-level latency spikes, retry storms, and cascades arise from service interactions and resource feedback loops that are not readable from one component specification in isolation. [source: https://principlesofchaos.org/; https://arxiv.org/abs/1702.05843; https://sre.google/sre-book/addressing-cascading-failures/; https://arxiv.org/abs/2407.01710]

#### D. Operator knowledge limits appear as post hoc reconstruction rather than direct whole-system understanding

- [fact] Google states that monitoring a complex application is itself a significant engineering endeavor and that even mature Site Reliability Engineering teams typically dedicate at least one person to monitoring for a service. [source: https://sre.google/sre-book/monitoring-distributed-systems/]
- [fact] Google says it has trended toward simpler and faster monitoring systems with better tools for post hoc analysis, and reports only limited success with complex dependency hierarchies. [source: https://sre.google/sre-book/monitoring-distributed-systems/]
- [fact] Google also says the critical path from production problem to page, triage, and deep debugging must be kept simple and comprehensible, which implies that direct whole-system reasoning does not scale cleanly with system complexity. [source: https://sre.google/sre-book/monitoring-distributed-systems/]
- [fact] Dekker's publisher summary characterizes complex-system failure as drift produced by many locally reasonable decisions in dynamic environments rather than by one isolated broken component, and one review quote on the same page states that accidents come from relationships rather than broken parts. [source: https://www.routledge.com/Drift-into-Failure/Dekker/p/book/9781409422211]
- [inference] The operational epistemic limit is therefore not that the system becomes random, but that operators increasingly explain incidents by reconstructing interaction histories from logs, traces, and experiments after the fact because no one can carry the whole causal graph in working memory. [source: https://sre.google/sre-book/monitoring-distributed-systems/; https://www.routledge.com/Drift-into-Failure/Dekker/p/book/9781409422211]

#### E. Prior completed items turn local complexity evidence into a bounded Complexity Horizon argument

- [fact] Research Question 6.1 concluded that unrestricted exact static analysis cannot decide arbitrary non-trivial semantic properties of programs. [source: https://davidamitchell.github.io/Research/research/2026-05-18-rq6-1-halting-problem-static-analysis.html]
- [fact] Research Question 6.2 concluded that deterministic systems can still become practically hard to predict because concurrency and perturbation sensitivity expand behaviour beyond tractable inspection. [source: https://davidamitchell.github.io/Research/research/2026-05-18-rq6-2-state-explosion-chaos-theory.html]
- [fact] Research Question 5.1 concluded that deterministic distributed systems can become globally opaque at scale without losing stronger local replayability than stochastic systems. [source: https://davidamitchell.github.io/Research/research/2026-05-18-rq5-1-stochastic-vs-deterministic-failures.html]
- [fact] The completed explainability comparison concluded that distributed deterministic software relies on observability and post hoc reconstruction at scale, even while retaining stronger local replayability than Large Language Model systems. [source: https://davidamitchell.github.io/Research/research/2026-05-18-agentic-explainability-vs-traditional.html]
- [inference] The Complexity Horizon is therefore best defined as the point where theorem-level limits, interaction growth, and operator cognition limits combine, so that direct whole-system explanation gives way to bounded local explanation plus reconstructed global explanation. [source: https://davidamitchell.github.io/Research/research/2026-05-18-rq6-1-halting-problem-static-analysis.html; https://davidamitchell.github.io/Research/research/2026-05-18-rq6-2-state-explosion-chaos-theory.html; https://davidamitchell.github.io/Research/research/2026-05-18-rq5-1-stochastic-vs-deterministic-failures.html; https://davidamitchell.github.io/Research/research/2026-05-18-agentic-explainability-vs-traditional.html; https://sre.google/sre-book/monitoring-distributed-systems/]

#### F. Bounded comparison with neural-network opacity

- [inference] The strongest comparison claim is not that microservice systems and neural networks share one identical mechanism of opacity, but that both can become globally difficult to explain because relevant causal structure is distributed across too many interacting elements for direct human inspection. [source: https://sre.google/sre-book/monitoring-distributed-systems/; https://principlesofchaos.org/; https://davidamitchell.github.io/Research/research/2026-05-18-agentic-explainability-vs-traditional.html]
- [inference] The strongest surviving asymmetry is that deterministic systems preserve stronger local replayability and component-level explanation, because one service call, rule, or state transition can still usually be re-run under fixed conditions even when the whole service graph is globally opaque. [source: https://martinfowler.com/articles/microservices.html; https://davidamitchell.github.io/Research/research/2026-05-18-rq5-1-stochastic-vs-deterministic-failures.html; https://davidamitchell.github.io/Research/research/2026-05-18-agentic-explainability-vs-traditional.html]

### §3 Reasoning

- [inference] Simon's theory and microservice practice support a two-level reading: decomposition works locally because interactions are structured and partially suppressible, but global explanation becomes harder as cross-service coupling, runtime dependency depth, and change velocity accumulate. [source: https://faculty.sites.iastate.edu/tesfatsi/archive/tesfatsi/ArchitectureOfComplexity.HSimon1962.pdf; https://martinfowler.com/articles/microservices.html; https://arxiv.org/abs/2407.01710]
- [inference] The strongest evidence for a real Complexity Horizon comes from operations practice rather than pure theory, because Site Reliability Engineering and chaos engineering both treat whole-system behaviour as something that must be inferred from signals and experiments rather than deduced from healthy components one by one. [source: https://sre.google/sre-book/monitoring-distributed-systems/; https://sre.google/sre-book/addressing-cascading-failures/; https://principlesofchaos.org/; https://arxiv.org/abs/1702.05843]
- [inference] Dekker's drift model strengthens the argument by explaining why searching for a single broken component often fails in complex systems: local rationality and global failure can coexist. [source: https://www.routledge.com/Drift-into-Failure/Dekker/p/book/9781409422211]
- [inference] The bounded comparison with neural-network opacity is therefore warranted at the global-explanation layer, but not at the local-execution layer, because deterministic service components remain more replayable and inspectable than stochastic model internals. [source: https://davidamitchell.github.io/Research/research/2026-05-18-rq5-1-stochastic-vs-deterministic-failures.html; https://davidamitchell.github.io/Research/research/2026-05-18-agentic-explainability-vs-traditional.html]

### §4 Consistency Check

- [fact] Tension: Simon's hierarchy seems to say decomposition makes complexity tractable. [source: https://faculty.sites.iastate.edu/tesfatsi/archive/tesfatsi/ArchitectureOfComplexity.HSimon1962.pdf]
- [inference] Resolution: Simon's own near-decomposability result is bounded by timescale and aggregation, so hierarchy delays opacity by making local analysis possible first, but it does not eliminate long-run cross-subsystem dependence. [source: https://faculty.sites.iastate.edu/tesfatsi/archive/tesfatsi/ArchitectureOfComplexity.HSimon1962.pdf]
- [fact] Tension: microservices are often sold as a simplification strategy. [source: https://martinfowler.com/articles/microservices.html]
- [inference] Resolution: microservices simplify ownership and deployment boundaries locally while simultaneously enlarging the runtime interaction surface globally. [source: https://martinfowler.com/articles/microservices.html; https://arxiv.org/abs/2407.01710]
- [fact] Tension: deterministic systems can be replayed, so they may seem fully interpretable. [source: https://davidamitchell.github.io/Research/research/2026-05-18-rq5-1-stochastic-vs-deterministic-failures.html]
- [inference] Resolution: replayability of one local path is not the same as having a tractable whole-system causal model across many interacting services and failure feedback loops. [source: https://sre.google/sre-book/monitoring-distributed-systems/; https://sre.google/sre-book/addressing-cascading-failures/; https://davidamitchell.github.io/Research/research/2026-05-18-rq5-1-stochastic-vs-deterministic-failures.html]

### §5 Depth and Breadth Expansion

- [inference] Technical lens: the Complexity Horizon grows when service count, call-chain depth, retry behaviour, and feedback loops enlarge the set of interaction paths that matter for runtime outcomes. [source: https://arxiv.org/abs/2407.01710; https://sre.google/sre-book/addressing-cascading-failures/; https://principlesofchaos.org/]
- [inference] Historical lens: Simon's hierarchy explains why modular decomposition became a durable design instinct, while later Site Reliability Engineering and chaos engineering practice explains why decomposition alone did not settle production opacity in distributed systems. [source: https://faculty.sites.iastate.edu/tesfatsi/archive/tesfatsi/ArchitectureOfComplexity.HSimon1962.pdf; https://sre.google/sre-book/monitoring-distributed-systems/; https://arxiv.org/abs/1702.05843]
- [inference] Behavioural lens: operators under time pressure naturally search for one broken part, but Dekker's drift framing and Google's post hoc analysis emphasis show that complex incidents often require relation-level reconstruction instead. [source: https://www.routledge.com/Drift-into-Failure/Dekker/p/book/9781409422211; https://sre.google/sre-book/monitoring-distributed-systems/]
- [inference] Epistemic lens: this item extends the Phase 6 line of argument from formal impossibility and state growth into production intelligibility, showing a third boundary where full code availability still does not yield easy whole-system explanation. [source: https://davidamitchell.github.io/Research/research/2026-05-18-rq6-1-halting-problem-static-analysis.html; https://davidamitchell.github.io/Research/research/2026-05-18-rq6-2-state-explosion-chaos-theory.html; https://sre.google/sre-book/monitoring-distributed-systems/]

### §6 Synthesis

**Executive summary:**

Deeply nested microservice systems can cross a real Complexity Horizon where deterministic execution remains locally replayable but whole-system behaviour becomes opaque enough that operators must explain incidents through traces, aggregate signals, and controlled experiments instead of direct mental simulation. [inference; source: https://faculty.sites.iastate.edu/tesfatsi/archive/tesfatsi/ArchitectureOfComplexity.HSimon1962.pdf; https://sre.google/sre-book/monitoring-distributed-systems/; https://principlesofchaos.org/]
Simon's hierarchy and near-decomposability explain why decomposition works first: subsystems are approximately independent in the short run and only aggregate-coupled in the long run, so architecture delays the horizon rather than abolishing it. [inference; source: https://faculty.sites.iastate.edu/tesfatsi/archive/tesfatsi/ArchitectureOfComplexity.HSimon1962.pdf]
Microservice evidence from architecture, failure-diagnosis, Site Reliability Engineering, and chaos-engineering sources shows that healthy local services can still generate retry storms, overload cascades, and other system-level outcomes that are not inferable from one service specification alone. [inference; source: https://martinfowler.com/articles/microservices.html; https://arxiv.org/abs/2407.01710; https://sre.google/sre-book/addressing-cascading-failures/; https://principlesofchaos.org/]
Dekker's drift framing shows why incident explanation at this scale often fails if investigators search for one broken part, because many locally rational actions can combine into one globally bad state. [inference; source: https://www.routledge.com/Drift-into-Failure/Dekker/p/book/9781409422211]
The resulting comparison with neural-network or Large Language Model opacity is therefore bounded but real: production-scale deterministic systems converge with stochastic systems at the global-explanation layer, even though they retain stronger local replayability and component-level intelligibility. [inference; source: https://davidamitchell.github.io/Research/research/2026-05-18-rq5-1-stochastic-vs-deterministic-failures.html; https://davidamitchell.github.io/Research/research/2026-05-18-agentic-explainability-vs-traditional.html]

**Key findings:**

1. **Simon's hierarchy result shows that complex systems become manageable by partitioning them into subsystems whose short-run behaviour is approximately independent, but his own near-decomposability conditions also show that this independence weakens at longer horizons and higher aggregation levels.** ([inference]; medium confidence; source: https://faculty.sites.iastate.edu/tesfatsi/archive/tesfatsi/ArchitectureOfComplexity.HSimon1962.pdf)
2. **Microservice architecture applies that hierarchic strategy directly by splitting one application into independently deployable out-of-process services, yet the same split creates more remote interfaces, dependency chains, and cross-team coordination points than a single-process design.** ([inference]; medium confidence; source: https://martinfowler.com/articles/microservices.html; https://arxiv.org/abs/2407.01710)
3. **Modern microservice systems exhibit emergent failure modes because independent deployment and dynamic service interactions can produce cascading failures and diagnosis challenges that are not visible from any one service specification alone.** ([inference]; medium confidence; source: https://arxiv.org/abs/2407.01710; https://principlesofchaos.org/; https://sre.google/sre-book/addressing-cascading-failures/)
4. **Site Reliability Engineering practice provides direct operational evidence for an epistemic barrier, because monitoring a complex application is itself a major engineering task, complex dependency hierarchies have had only limited success, and teams prefer simple alerting plus post hoc analysis.** ([inference]; medium confidence; source: https://sre.google/sre-book/monitoring-distributed-systems/)
5. **Dekker's drift framework helps explain why this barrier feels like opacity rather than ordinary component debugging, because many locally reasonable actions can propagate through relationships and feedback loops until the eventual failure state is visible only after reconstruction.** ([inference]; low confidence; source: https://www.routledge.com/Drift-into-Failure/Dekker/p/book/9781409422211; https://sre.google/sre-book/addressing-cascading-failures/)
6. **The Complexity Horizon is best defined as the point where service count, dependency degree, and runtime nesting depth outgrow reliable operator mental models, forcing explanation to shift from direct understanding to traces, aggregate metrics, and controlled experiment.** ([inference]; medium confidence; source: https://faculty.sites.iastate.edu/tesfatsi/archive/tesfatsi/ArchitectureOfComplexity.HSimon1962.pdf; https://sre.google/sre-book/monitoring-distributed-systems/; https://principlesofchaos.org/; https://davidamitchell.github.io/Research/research/2026-05-18-rq6-2-state-explosion-chaos-theory.html)
7. **This item extends Research Question 6.1 and Research Question 6.2 by showing that formal limits on static analysis and dynamic state growth culminate in an operational intelligibility limit, where code can remain deterministic and inspectable locally while the total system becomes globally hard to explain.** ([inference]; medium confidence; source: https://davidamitchell.github.io/Research/research/2026-05-18-rq6-1-halting-problem-static-analysis.html; https://davidamitchell.github.io/Research/research/2026-05-18-rq6-2-state-explosion-chaos-theory.html; https://sre.google/sre-book/monitoring-distributed-systems/)
8. **The bounded comparison with neural-network or Large Language Model opacity is justified at the global-explanation layer, but not as a full equivalence claim, because deterministic systems still retain stronger local replayability and component-level explanation than stochastic models do.** ([inference]; medium confidence; source: https://davidamitchell.github.io/Research/research/2026-05-18-rq5-1-stochastic-vs-deterministic-failures.html; https://davidamitchell.github.io/Research/research/2026-05-18-agentic-explainability-vs-traditional.html; https://sre.google/sre-book/monitoring-distributed-systems/)

**Evidence map:**

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [inference] Simon's hierarchy and near-decomposability make decomposition a bounded delay mechanism rather than a permanent cure for complexity. | https://faculty.sites.iastate.edu/tesfatsi/archive/tesfatsi/ArchitectureOfComplexity.HSimon1962.pdf | medium | short-run versus long-run |
| [inference] Microservices trade one large codebase for many out-of-process boundaries and runtime dependencies. | https://martinfowler.com/articles/microservices.html ; https://arxiv.org/abs/2407.01710 | medium | modularity versus coordination |
| [inference] Dynamic interactions among microservices create emergent cascading failures and diagnosis challenges beyond one service view. | https://arxiv.org/abs/2407.01710 ; https://principlesofchaos.org/ ; https://sre.google/sre-book/addressing-cascading-failures/ | medium | system-level behaviour |
| [inference] Site Reliability Engineering practice shows that whole-system understanding gives way to simple alerting plus post hoc analysis in complex services. | https://sre.google/sre-book/monitoring-distributed-systems/ | medium | operator cognition limit |
| [inference] Drift into failure is relation-level and cumulative, not reducible to one broken component. | https://www.routledge.com/Drift-into-Failure/Dekker/p/book/9781409422211 ; https://sre.google/sre-book/addressing-cascading-failures/ | low | relationship and feedback |
| [inference] The Complexity Horizon is the transition from direct mental simulation to reconstructed explanation from traces, metrics, and experiment. | https://faculty.sites.iastate.edu/tesfatsi/archive/tesfatsi/ArchitectureOfComplexity.HSimon1962.pdf ; https://sre.google/sre-book/monitoring-distributed-systems/ ; https://principlesofchaos.org/ ; https://davidamitchell.github.io/Research/research/2026-05-18-rq6-2-state-explosion-chaos-theory.html | medium | operational definition |
| [inference] Phase 6's theorem and state-growth limits culminate in an operational intelligibility limit for deterministic systems. | https://davidamitchell.github.io/Research/research/2026-05-18-rq6-1-halting-problem-static-analysis.html ; https://davidamitchell.github.io/Research/research/2026-05-18-rq6-2-state-explosion-chaos-theory.html ; https://sre.google/sre-book/monitoring-distributed-systems/ | medium | cross-item synthesis |
| [inference] Global opacity can converge across deterministic and stochastic systems without erasing stronger deterministic local replayability. | https://davidamitchell.github.io/Research/research/2026-05-18-rq5-1-stochastic-vs-deterministic-failures.html ; https://davidamitchell.github.io/Research/research/2026-05-18-agentic-explainability-vs-traditional.html ; https://sre.google/sre-book/monitoring-distributed-systems/ | medium | bounded comparison |

**Assumptions:**

- [assumption] There is no settled external metric that names or numerically fixes the Complexity Horizon, so this item operationalises the term as a shift in explanation method from direct mental modelling to reconstruction from observability artefacts and experiments. [source: https://sre.google/sre-book/monitoring-distributed-systems/; https://principlesofchaos.org/]
- [assumption] The Dekker and Nygard publisher pages are used as scoped summaries of each book's central framing because full searchable text was not accessible here, so claims drawn from them are kept at synthesis or orientation level rather than treated as exhaustive summaries of the books. [source: https://www.routledge.com/Drift-into-Failure/Dekker/p/book/9781409422211; https://pragprog.com/titles/mnee2/release-it-second-edition/]
- [assumption] The neural-network and Large Language Model comparison is intentionally bounded to global explanatory opacity rather than local execution semantics, because prior completed items already show a surviving deterministic replayability advantage. [source: https://davidamitchell.github.io/Research/research/2026-05-18-rq5-1-stochastic-vs-deterministic-failures.html; https://davidamitchell.github.io/Research/research/2026-05-18-agentic-explainability-vs-traditional.html]

**Analysis:**

- The evidence converges on a layered conclusion rather than a binary one. [inference; source: https://faculty.sites.iastate.edu/tesfatsi/archive/tesfatsi/ArchitectureOfComplexity.HSimon1962.pdf; https://sre.google/sre-book/monitoring-distributed-systems/; https://principlesofchaos.org/]
- Hierarchy and modularity matter because they make local reasoning possible, but the same evidence shows that runtime coupling, retries, shared dependencies, and overload feedback loops reintroduce global dependence that no one service owner can fully see in advance. [inference; source: https://martinfowler.com/articles/microservices.html; https://arxiv.org/abs/2407.01710; https://sre.google/sre-book/addressing-cascading-failures/]
- A plausible rival explanation is that stronger tooling or more staffing could restore more transparency than this item allows. [assumption; source: https://sre.google/sre-book/monitoring-distributed-systems/]
- The reviewed evidence does not support that stronger claim, because Google's own operations guidance still reports limited success with complex dependency hierarchies and explicitly prefers simple alerting plus post hoc analysis, which implies management of opacity rather than abolition of opacity. [inference; source: https://sre.google/sre-book/monitoring-distributed-systems/]
- Dekker's drift framing helps resolve why the system can be deterministic yet feel opaque in practice: determinism does not imply that causation is locally obvious when many relational effects accumulate before failure becomes visible. [inference; source: https://www.routledge.com/Drift-into-Failure/Dekker/p/book/9781409422211; https://sre.google/sre-book/addressing-cascading-failures/]
- The bounded comparison with neural-network opacity is therefore strongest where the question concerns whole-system explanation after or during an incident, and weakest where the question concerns exact replay of one local execution path. [inference; source: https://davidamitchell.github.io/Research/research/2026-05-18-rq5-1-stochastic-vs-deterministic-failures.html; https://davidamitchell.github.io/Research/research/2026-05-18-agentic-explainability-vs-traditional.html]

**Risks, gaps, uncertainties:**

- [inference] The cited evidence base documents operator-cognition limits qualitatively through Google's Site Reliability Engineering practice rather than through a dedicated benchmark that measures a precise service-count or dependency-depth threshold. [source: https://sre.google/sre-book/monitoring-distributed-systems/]
- [inference] The Dekker and Nygard evidence is narrower than the Simon and Google evidence because the accessible materials are publisher summaries rather than full text, so their role here is to qualify the systems-failure framing rather than to carry the central formal claim alone. [source: https://www.routledge.com/Drift-into-Failure/Dekker/p/book/9781409422211; https://pragprog.com/titles/mnee2/release-it-second-edition/]
- [inference] No reviewed source gives a controlled head-to-head benchmark comparing incident explainability in matched microservice systems and neural-network systems, so the cross-class verdict remains an evidence-backed synthesis rather than a single-study measurement. [source: https://davidamitchell.github.io/Research/research/2026-05-18-rq5-1-stochastic-vs-deterministic-failures.html; https://davidamitchell.github.io/Research/research/2026-05-18-agentic-explainability-vs-traditional.html]

**Open questions:**

- Which observable variables, dependency degree, call-chain depth, change velocity, or cross-team ownership count, best predict when a microservice estate crosses the Complexity Horizon?
- What instrumentation patterns shrink the gap between local replayability and global explainability without simply shifting more complexity into the observability layer?
- How far can the bounded comparison be extended from Large Language Model systems to broader neural-network deployment stacks without losing the local-versus-global distinction?

**Output:**

- Type: knowledge
- Description: This item formalises the Complexity Horizon as the point where deterministic decomposition stops yielding a reliable whole-system model and explanation shifts to reconstruction from traces, aggregate metrics, and controlled experiments. [inference; source: https://faculty.sites.iastate.edu/tesfatsi/archive/tesfatsi/ArchitectureOfComplexity.HSimon1962.pdf; https://sre.google/sre-book/monitoring-distributed-systems/; https://principlesofchaos.org/]
- Links:
  - https://faculty.sites.iastate.edu/tesfatsi/archive/tesfatsi/ArchitectureOfComplexity.HSimon1962.pdf
  - https://sre.google/sre-book/monitoring-distributed-systems/
  - https://principlesofchaos.org/
### §7 Recursive Review

```yaml
review_result: pass
acronym_audit: pass
domain_term_audit: pass
claim_label_audit: pass
synthesis_findings_parity: aligned
unresolved_contradictions: none_material
confidence_setting: medium
```

---

## Findings

*(Populated from §6 Synthesis above.)*

### Executive Summary

Deeply nested microservice systems can cross a real Complexity Horizon where deterministic execution remains locally replayable but whole-system behaviour becomes opaque enough that operators must explain incidents through traces, aggregate signals, and controlled experiments instead of direct mental simulation. [inference; source: https://faculty.sites.iastate.edu/tesfatsi/archive/tesfatsi/ArchitectureOfComplexity.HSimon1962.pdf; https://sre.google/sre-book/monitoring-distributed-systems/; https://principlesofchaos.org/]
Simon's hierarchy and near-decomposability explain why decomposition works first: subsystems are approximately independent in the short run and only aggregate-coupled in the long run, so architecture delays the horizon rather than abolishing it. [inference; source: https://faculty.sites.iastate.edu/tesfatsi/archive/tesfatsi/ArchitectureOfComplexity.HSimon1962.pdf]
Microservice evidence from architecture, failure-diagnosis, Site Reliability Engineering, and chaos-engineering sources shows that healthy local services can still generate retry storms, overload cascades, and other system-level outcomes that are not inferable from one service specification alone. [inference; source: https://martinfowler.com/articles/microservices.html; https://arxiv.org/abs/2407.01710; https://sre.google/sre-book/addressing-cascading-failures/; https://principlesofchaos.org/]
The resulting comparison with neural-network or Large Language Model opacity is bounded but real: production-scale deterministic systems converge with stochastic systems at the global-explanation layer, even though they retain stronger local replayability and component-level intelligibility. [inference; source: https://davidamitchell.github.io/Research/research/2026-05-18-rq5-1-stochastic-vs-deterministic-failures.html; https://davidamitchell.github.io/Research/research/2026-05-18-agentic-explainability-vs-traditional.html]

### Key Findings

1. **Simon's hierarchy result shows that complex systems become manageable by partitioning them into subsystems whose short-run behaviour is approximately independent, but his own near-decomposability conditions also show that this independence weakens at longer horizons and higher aggregation levels.** ([inference]; medium confidence; source: https://faculty.sites.iastate.edu/tesfatsi/archive/tesfatsi/ArchitectureOfComplexity.HSimon1962.pdf)
2. **Microservice architecture applies that hierarchic strategy directly by splitting one application into independently deployable out-of-process services, yet the same split creates more remote interfaces, dependency chains, and cross-team coordination points than a single-process design.** ([inference]; medium confidence; source: https://martinfowler.com/articles/microservices.html; https://arxiv.org/abs/2407.01710)
3. **Modern microservice systems exhibit emergent failure modes because independent deployment and dynamic service interactions can produce cascading failures and diagnosis challenges that are not visible from any one service specification alone.** ([inference]; medium confidence; source: https://arxiv.org/abs/2407.01710; https://principlesofchaos.org/; https://sre.google/sre-book/addressing-cascading-failures/)
4. **Site Reliability Engineering practice provides direct operational evidence for an epistemic barrier, because monitoring a complex application is itself a major engineering task, complex dependency hierarchies have had only limited success, and teams prefer simple alerting plus post hoc analysis.** ([inference]; medium confidence; source: https://sre.google/sre-book/monitoring-distributed-systems/)
5. **Dekker's drift framework helps explain why this barrier feels like opacity rather than ordinary component debugging, because many locally reasonable actions can propagate through relationships and feedback loops until the eventual failure state is visible only after reconstruction.** ([inference]; low confidence; source: https://www.routledge.com/Drift-into-Failure/Dekker/p/book/9781409422211; https://sre.google/sre-book/addressing-cascading-failures/)
6. **The Complexity Horizon is best defined as the point where service count, dependency degree, and runtime nesting depth outgrow reliable operator mental models, forcing explanation to shift from direct understanding to traces, aggregate metrics, and controlled experiment.** ([inference]; medium confidence; source: https://faculty.sites.iastate.edu/tesfatsi/archive/tesfatsi/ArchitectureOfComplexity.HSimon1962.pdf; https://sre.google/sre-book/monitoring-distributed-systems/; https://principlesofchaos.org/; https://davidamitchell.github.io/Research/research/2026-05-18-rq6-2-state-explosion-chaos-theory.html)
7. **This item extends Research Question 6.1 and Research Question 6.2 by showing that formal limits on static analysis and dynamic state growth culminate in an operational intelligibility limit, where code can remain deterministic and inspectable locally while the total system becomes globally hard to explain.** ([inference]; medium confidence; source: https://davidamitchell.github.io/Research/research/2026-05-18-rq6-1-halting-problem-static-analysis.html; https://davidamitchell.github.io/Research/research/2026-05-18-rq6-2-state-explosion-chaos-theory.html; https://sre.google/sre-book/monitoring-distributed-systems/)
8. **The bounded comparison with neural-network or Large Language Model opacity is justified at the global-explanation layer, but not as a full equivalence claim, because deterministic systems still retain stronger local replayability and component-level explanation than stochastic models do.** ([inference]; medium confidence; source: https://davidamitchell.github.io/Research/research/2026-05-18-rq5-1-stochastic-vs-deterministic-failures.html; https://davidamitchell.github.io/Research/research/2026-05-18-agentic-explainability-vs-traditional.html; https://sre.google/sre-book/monitoring-distributed-systems/)

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [inference] Simon's hierarchy and near-decomposability make decomposition a bounded delay mechanism rather than a permanent cure for complexity. | https://faculty.sites.iastate.edu/tesfatsi/archive/tesfatsi/ArchitectureOfComplexity.HSimon1962.pdf | medium | short-run versus long-run |
| [inference] Microservices trade one large codebase for many out-of-process boundaries and runtime dependencies. | https://martinfowler.com/articles/microservices.html ; https://arxiv.org/abs/2407.01710 | medium | modularity versus coordination |
| [inference] Dynamic interactions among microservices create emergent cascading failures and diagnosis challenges beyond one service view. | https://arxiv.org/abs/2407.01710 ; https://principlesofchaos.org/ ; https://sre.google/sre-book/addressing-cascading-failures/ | medium | system-level behaviour |
| [inference] Site Reliability Engineering practice shows that whole-system understanding gives way to simple alerting plus post hoc analysis in complex services. | https://sre.google/sre-book/monitoring-distributed-systems/ | medium | operator cognition limit |
| [inference] Drift into failure is relation-level and cumulative, not reducible to one broken component. | https://www.routledge.com/Drift-into-Failure/Dekker/p/book/9781409422211 ; https://sre.google/sre-book/addressing-cascading-failures/ | low | relationship and feedback |
| [inference] The Complexity Horizon is the transition from direct mental simulation to reconstructed explanation from traces, metrics, and experiment. | https://faculty.sites.iastate.edu/tesfatsi/archive/tesfatsi/ArchitectureOfComplexity.HSimon1962.pdf ; https://sre.google/sre-book/monitoring-distributed-systems/ ; https://principlesofchaos.org/ ; https://davidamitchell.github.io/Research/research/2026-05-18-rq6-2-state-explosion-chaos-theory.html | medium | operational definition |
| [inference] Phase 6's theorem and state-growth limits culminate in an operational intelligibility limit for deterministic systems. | https://davidamitchell.github.io/Research/research/2026-05-18-rq6-1-halting-problem-static-analysis.html ; https://davidamitchell.github.io/Research/research/2026-05-18-rq6-2-state-explosion-chaos-theory.html ; https://sre.google/sre-book/monitoring-distributed-systems/ | medium | cross-item synthesis |
| [inference] Global opacity can converge across deterministic and stochastic systems without erasing stronger deterministic local replayability. | https://davidamitchell.github.io/Research/research/2026-05-18-rq5-1-stochastic-vs-deterministic-failures.html ; https://davidamitchell.github.io/Research/research/2026-05-18-agentic-explainability-vs-traditional.html ; https://sre.google/sre-book/monitoring-distributed-systems/ | medium | bounded comparison |

### Assumptions

- [assumption] There is no settled external metric that names or numerically fixes the Complexity Horizon, so this item operationalises the term as a shift in explanation method from direct mental modelling to reconstruction from observability artefacts and experiments. [source: https://sre.google/sre-book/monitoring-distributed-systems/; https://principlesofchaos.org/]
- [assumption] The Dekker and Nygard publisher pages are used as scoped summaries of each book's central framing because full searchable text was not accessible here, so claims drawn from them are kept at synthesis or orientation level rather than treated as exhaustive summaries of the books. [source: https://www.routledge.com/Drift-into-Failure/Dekker/p/book/9781409422211; https://pragprog.com/titles/mnee2/release-it-second-edition/]
- [assumption] The neural-network and Large Language Model comparison is intentionally bounded to global explanatory opacity rather than local execution semantics, because prior completed items already show a surviving deterministic replayability advantage. [source: https://davidamitchell.github.io/Research/research/2026-05-18-rq5-1-stochastic-vs-deterministic-failures.html; https://davidamitchell.github.io/Research/research/2026-05-18-agentic-explainability-vs-traditional.html]

### Analysis

The evidence converges on a layered conclusion rather than a binary one. [inference; source: https://faculty.sites.iastate.edu/tesfatsi/archive/tesfatsi/ArchitectureOfComplexity.HSimon1962.pdf; https://sre.google/sre-book/monitoring-distributed-systems/; https://principlesofchaos.org/]
Hierarchy and modularity matter because they make local reasoning possible, but the same evidence shows that runtime coupling, retries, shared dependencies, and overload feedback loops reintroduce global dependence that no one service owner can fully see in advance. [inference; source: https://martinfowler.com/articles/microservices.html; https://arxiv.org/abs/2407.01710; https://sre.google/sre-book/addressing-cascading-failures/]
A plausible rival explanation is that stronger tooling or more staffing could restore more transparency than this item allows. [assumption; source: https://sre.google/sre-book/monitoring-distributed-systems/]
The reviewed evidence does not support that stronger claim, because Google's own operations guidance still reports limited success with complex dependency hierarchies and explicitly prefers simple alerting plus post hoc analysis, which implies management of opacity rather than abolition of opacity. [inference; source: https://sre.google/sre-book/monitoring-distributed-systems/]
Dekker's drift framing helps resolve why the system can be deterministic yet feel opaque in practice: determinism does not imply that causation is locally obvious when many relational effects accumulate before failure becomes visible. [inference; source: https://www.routledge.com/Drift-into-Failure/Dekker/p/book/9781409422211; https://sre.google/sre-book/addressing-cascading-failures/]
The bounded comparison with neural-network opacity is therefore strongest where the question concerns whole-system explanation after or during an incident, and weakest where the question concerns exact replay of one local execution path. [inference; source: https://davidamitchell.github.io/Research/research/2026-05-18-rq5-1-stochastic-vs-deterministic-failures.html; https://davidamitchell.github.io/Research/research/2026-05-18-agentic-explainability-vs-traditional.html]

### Risks, Gaps, and Uncertainties

- [inference] The cited evidence base documents operator-cognition limits qualitatively through Google's Site Reliability Engineering practice rather than through a dedicated benchmark that measures a precise service-count or dependency-depth threshold. [source: https://sre.google/sre-book/monitoring-distributed-systems/]
- [inference] The Dekker and Nygard evidence is narrower than the Simon and Google evidence because the accessible materials are publisher summaries rather than full text, so their role here is to qualify the systems-failure framing rather than to carry the central formal claim alone. [source: https://www.routledge.com/Drift-into-Failure/Dekker/p/book/9781409422211; https://pragprog.com/titles/mnee2/release-it-second-edition/]
- [inference] No reviewed source gives a controlled head-to-head benchmark comparing incident explainability in matched microservice systems and neural-network systems, so the cross-class verdict remains an evidence-backed synthesis rather than a single-study measurement. [source: https://davidamitchell.github.io/Research/research/2026-05-18-rq5-1-stochastic-vs-deterministic-failures.html; https://davidamitchell.github.io/Research/research/2026-05-18-agentic-explainability-vs-traditional.html]

### Open Questions

- Which observable variables, dependency degree, call-chain depth, change velocity, or cross-team ownership count, best predict when a microservice estate crosses the Complexity Horizon?
- What instrumentation patterns shrink the gap between local replayability and global explainability without simply shifting more complexity into the observability layer?
- How far can the bounded comparison be extended from Large Language Model systems to broader neural-network deployment stacks without losing the local-versus-global distinction?

---

## Output

- Type: knowledge
- Description: This item formalises the Complexity Horizon as the point where deterministic decomposition stops yielding a reliable whole-system model and explanation shifts to reconstruction from traces, aggregate metrics, and controlled experiments. [inference; source: https://faculty.sites.iastate.edu/tesfatsi/archive/tesfatsi/ArchitectureOfComplexity.HSimon1962.pdf; https://sre.google/sre-book/monitoring-distributed-systems/; https://principlesofchaos.org/]
- Links:
  - https://faculty.sites.iastate.edu/tesfatsi/archive/tesfatsi/ArchitectureOfComplexity.HSimon1962.pdf
  - https://sre.google/sre-book/monitoring-distributed-systems/
  - https://principlesofchaos.org/
