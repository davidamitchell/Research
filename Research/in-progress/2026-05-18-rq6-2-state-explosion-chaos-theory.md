---
review_count: 2
title: "Research Question 6.2: State Space Explosion and Deterministic Chaos, Fragility Shared Between Concurrent Coded Systems and Machine Learning Models"
added: 2026-05-18T19:40:00+00:00
status: reviewing
priority: high
blocks:
  - 2026-05-18-rq6-3-complexity-horizon-classical-systems
tags: [formal-methods, machine-learning, distributed-systems, epistemology, chaos-theory]
started: 2026-05-19T20:56:44+00:00
completed: ~
output: [knowledge]
cites:
  - 2026-05-18-rq6-1-halting-problem-static-analysis
  - 2026-05-18-rq2-3-predictive-model-fragility
related:
  - 2026-05-18-rq5-1-stochastic-vs-deterministic-failures
superseded_by: ~
supersedes: ~
item_type: primary
confidence: medium
versions: []
---

# Research Question 6.2: State Space Explosion and Deterministic Chaos, Fragility Shared Between Concurrent Coded Systems and Machine Learning Models

## Research Question

How do state space explosion in concurrent systems and chaos theory, especially sensitive dependence on initial conditions, mirror the fragility of machine learning models when subjected to minor input perturbations?

## Scope

**In scope:**
- State space explosion in concurrent systems: the combinatorial growth of reachable states in multi-threaded programs
- Race conditions and concurrency anomalies as manifestations of state space explosion at runtime
- Deterministic chaos, including the Lorenz attractor and the butterfly effect: how deterministic systems exhibit sensitive dependence on initial conditions
- Formal comparison: does perturbation sensitivity in machine learning models, especially adversarial examples, share the mathematical structure of chaotic sensitivity in deterministic algorithms?
- Lamport's logical clocks as a partial ordering solution to concurrency non-determinism

**Out of scope:**
- Numerical chaos in floating-point arithmetic (a narrower technical topic)
- Chaos in biological or physical systems beyond what directly illuminates software system properties

**Constraints:** Builds on Research Question 6.1's undecidability foundations; must connect to Research Question 2.3's structural stability analysis as a bridge between the two tracks.

## Context

- [fact] Research Question 6.1 established that unrestricted static analysis cannot determine arbitrary non-trivial semantic properties of programs. [source: https://davidamitchell.github.io/Research/research/2026-05-18-rq6-1-halting-problem-static-analysis.html]
- [inference] This item examines a different limit, that even fully specified deterministic programs can remain practically hard to verify or predict once concurrency and sensitivity dominate behavior. [source: https://davidamitchell.github.io/Research/research/2026-05-18-rq6-1-halting-problem-static-analysis.html; https://www.cs.vsb.cz/kot/down/Texts/StateSpace.pdf; https://doi.org/10.1175/1520-0469(1963)020%3C0130:DNF%3E2.0.CO;2]
- [inference] The bridge to Research Question 2.3 is that fragility is not unique to learned models, because deterministic coded systems can also exhibit large behavioral shifts after small local perturbations. [source: https://davidamitchell.github.io/Research/research/2026-05-18-rq2-3-predictive-model-fragility.html; https://www.cs.vsb.cz/kot/down/Texts/StateSpace.pdf; https://doi.org/10.1175/1520-0469(1963)020%3C0130:DNF%3E2.0.CO;2]

## Approach

1. Define state space explosion formally: in a concurrent system with N threads, the reachable state space grows exponentially; quantify this growth.
2. Analyse race conditions as manifestations of state space explosion: non-deterministic interleavings that produce qualitatively different outputs.
3. Introduce deterministic chaos via the Lorenz (1963) attractor: a deterministic system that is practically unpredictable due to sensitive dependence.
4. Establish the mathematical parallel: sensitive dependence on initial conditions in chaotic systems vs. sensitivity to input perturbations in adversarially attacked machine learning models.
5. Apply Lamport's logical clocks as a partial ordering constraint; show what can and cannot be guaranteed even with clock-based ordering.

## Sources

- [x] [Lorenz, E. N. (1963) Deterministic Nonperiodic Flow](https://doi.org/10.1175/1520-0469(1963)020%3C0130:DNF%3E2.0.CO;2)
- [x] [Ghys and Leys (2006) Lorenz and Modular Flows: A Visual Introduction](https://www.ams.org/publicoutreach/feature-column/fcarc-lorenz)
- [x] [Lamport, L. (1978) Time, Clocks, and the Ordering of Events in a Distributed System, Portable Document Format (PDF) mirror](https://lamport.azurewebsites.net/pubs/time-clocks.pdf)
- [ ] [Lamport, L. (1978) Time, Clocks, and the Ordering of Events in a Distributed System, Digital Object Identifier (DOI) record](https://doi.org/10.1145/359545.359563)
- [ ] [Clarke, E. M. et al. (2018) Model Checking](https://mitpress.mit.edu/9780262038553/model-checking/)
- [x] [Kot, M. (2003) The State Explosion Problem](https://www.cs.vsb.cz/kot/down/Texts/StateSpace.pdf)
- [x] [Oracle Java Tutorials: Thread Interference](https://docs.oracle.com/javase/tutorial/essential/concurrency/interfere.html)
- [x] [MITRE CWE-362 Concurrent Execution using Shared Resource with Improper Synchronization](https://cwe.mitre.org/data/definitions/362.html)
- [x] [Goodfellow et al. (2015) Explaining and Harnessing Adversarial Examples](https://arxiv.org/abs/1412.6572)
- [x] [Research Question 6.1: The Halting Problem and Rice's Theorem, the Absolute Boundary of Static Analysis for Coded Systems](https://davidamitchell.github.io/Research/research/2026-05-18-rq6-1-halting-problem-static-analysis.html)
- [x] [Research Question 2.3: Structural Stability vs. Predictive Fragility, Dynamical Systems Theory and the Cost of Noise](https://davidamitchell.github.io/Research/research/2026-05-18-rq2-3-predictive-model-fragility.html)
- [x] [Research Question 5.1: Stochastic versus Deterministic Failure Modes on Identical Unvalidated Inputs](https://davidamitchell.github.io/Research/research/2026-05-18-rq5-1-stochastic-vs-deterministic-failures.html)

---

## Research Skill Output

*(Full output from running the research skill, retained verbatim in the completed item. Sections 0 to 5 are the investigation, and Section 6 seeds the Findings section below.)*

### §0 Initialise

- Question: How state space explosion in concurrent systems and sensitive dependence in deterministic chaos compare with minor-perturbation fragility in machine learning models.
- Scope: concurrent state growth, race conditions, Lorenz-style chaotic sensitivity, adversarial fragility, and Lamport logical clocks.
- Constraints: full-mode investigation; connect Research Question 6.1 and Research Question 2.3; output as a full structured synthesis plus mirrored Findings section.
- [fact] For this item, state space explosion means exponential growth in reachable system states as processes and variables increase, deterministic chaos means deterministic dynamics with sensitive dependence on initial conditions, and an adversarial example means an input altered by a small worst-case perturbation that changes a model's output. [source: https://www.cs.vsb.cz/kot/down/Texts/StateSpace.pdf; https://doi.org/10.1175/1520-0469(1963)020%3C0130:DNF%3E2.0.CO;2; https://arxiv.org/abs/1412.6572]
- Prior completed-item check:
  - [fact] Research Question 6.1 concluded that unrestricted exact static analysis cannot decide arbitrary non-trivial semantic properties of programs, so this item starts from a formal impossibility boundary and moves to dynamic fragility. [source: https://davidamitchell.github.io/Research/research/2026-05-18-rq6-1-halting-problem-static-analysis.html]
  - [fact] Research Question 2.3 concluded that predictive systems without invariant structure can remain observationally successful while becoming fragile under perturbation or shift. [source: https://davidamitchell.github.io/Research/research/2026-05-18-rq2-3-predictive-model-fragility.html]
  - [fact] Research Question 5.1 concluded that deterministic coded systems usually preserve stronger replayability than stochastic language-model systems even when both are fragile. [source: https://davidamitchell.github.io/Research/research/2026-05-18-rq5-1-stochastic-vs-deterministic-failures.html]
  - [inference] This item should therefore test a narrower bridge claim, that deterministic systems can share perturbation fragility with machine learning models without sharing the same exact mechanism or the same observability profile. [source: https://davidamitchell.github.io/Research/research/2026-05-18-rq2-3-predictive-model-fragility.html; https://davidamitchell.github.io/Research/research/2026-05-18-rq5-1-stochastic-vs-deterministic-failures.html]

### §1 Question Decomposition

1. State space explosion in concurrency
   1.1 What is the formal object that grows, local states, shared-variable valuations, and interleavings?
   1.2 Why does that object grow exponentially as concurrent components and variables increase?
   1.3 How do race conditions show the runtime consequence of many feasible interleavings?
2. Deterministic chaos
   2.1 What does Lorenz's 1963 result show about deterministic systems and small initial differences?
   2.2 Why does deterministic law fail to guarantee practical long-range predictability in chaotic systems?
3. Machine learning perturbation fragility
   3.1 What do adversarial examples show about small perturbations and classification behavior?
   3.2 What mechanism does the Goodfellow et al. paper propose for that fragility?
4. Formal comparison
   4.1 In what sense are chaos sensitivity and adversarial fragility structurally similar?
   4.2 In what sense are they different, trajectory divergence over time versus local decision-boundary sensitivity?
5. Concurrency control surface
   5.1 What does Lamport's happened-before relation formally guarantee?
   5.2 What remains unresolved after logical clocks are introduced?
6. Cross-item synthesis
   6.1 How does this dynamic-fragility argument extend the static impossibility boundary in Research Question 6.1?
   6.2 How does it sharpen the invariant-structure argument from Research Question 2.3?

### §2 Investigation

- [assumption] This item treats the Lorenz Digital Object Identifier (DOI) record plus the American Mathematical Society article, the Lamport Portable Document Format (PDF) mirror, and the Kot survey note as the operative claim-bearing sources because they contain the specific text used in the analysis below. [source: https://doi.org/10.1175/1520-0469(1963)020%3C0130:DNF%3E2.0.CO;2; https://www.ams.org/publicoutreach/feature-column/fcarc-lorenz; https://lamport.azurewebsites.net/pubs/time-clocks.pdf; https://www.cs.vsb.cz/kot/down/Texts/StateSpace.pdf; https://mitpress.mit.edu/9780262038553/model-checking/]

#### A. State space explosion in concurrent systems

- [fact] Kot defines state-space methods for concurrent systems as building a structure containing all states a system can reach and all transitions it can make between those states. [source: https://www.cs.vsb.cz/kot/down/Texts/StateSpace.pdf]
- [fact] Kot states that state-space methods suffer from a fundamental problem because the size of a system's state space often grows exponentially in the number of its processes and variables. [source: https://www.cs.vsb.cz/kot/down/Texts/StateSpace.pdf]
- [fact] Kot adds that the base of that exponential growth depends on the number of local states per process, the number of values a variable may store, and the coupling among components. [source: https://www.cs.vsb.cz/kot/down/Texts/StateSpace.pdf]
- [inference] If N concurrent components each contribute multiple local states, the joint reachable-state set grows combinatorially as the product of those local possibilities before one even accounts for alternate execution schedules. [source: https://www.cs.vsb.cz/kot/down/Texts/StateSpace.pdf]

#### B. Race conditions as operational evidence of interleaving explosion

- [fact] Oracle's thread-interference tutorial explains that even a simple increment like `c++` decomposes into read, modify, and write steps, so two concurrent operations can interleave and overwrite one another. [source: https://docs.oracle.com/javase/tutorial/essential/concurrency/interfere.html]
- [fact] Oracle gives an explicit lost-update example in which one thread's increment is overwritten by another thread's decrement because their steps overlap in a different order. [source: https://docs.oracle.com/javase/tutorial/essential/concurrency/interfere.html]
- [fact] MITRE's Common Weakness Enumeration entry CWE-362 defines a race condition as a concurrent code sequence that requires temporary exclusive access to a shared resource but still has a timing window in which another code sequence can modify that resource. [source: https://cwe.mitre.org/data/definitions/362.html]
- [fact] The same CWE entry says race conditions violate exclusivity and atomicity because an interfering code sequence can still access the shared resource before the original sequence completes. [source: https://cwe.mitre.org/data/definitions/362.html]
- [inference] Race conditions are the runtime face of state-space explosion because different valid interleavings of the same underlying program can lead to qualitatively different outcomes, including correct results, lost updates, or corrupted shared state. [source: https://docs.oracle.com/javase/tutorial/essential/concurrency/interfere.html; https://cwe.mitre.org/data/definitions/362.html; https://www.cs.vsb.cz/kot/down/Texts/StateSpace.pdf]

#### C. Deterministic chaos and sensitive dependence on initial conditions

- [fact] The first page of Lorenz's paper states that nonperiodic solutions in the studied system are ordinarily unstable with respect to small modifications, so slightly differing initial states can evolve into considerably different states. [source: https://doi.org/10.1175/1520-0469(1963)020%3C0130:DNF%3E2.0.CO;2]
- [fact] The American Mathematical Society feature article describes the Lorenz attractor as a paradigmatic symbol of chaos theory arising from a simplified atmospheric model. [source: https://www.ams.org/publicoutreach/feature-column/fcarc-lorenz]
- [fact] The American Mathematical Society feature article says the Lorenz picture is robust in the sense that perturbing the equation preserves the phenomenon of trajectories approaching what is now called a strange attractor. [source: https://www.ams.org/publicoutreach/feature-column/fcarc-lorenz]
- [inference] Deterministic chaos therefore marks a regime in which the governing law remains fixed, but practical long-range prediction collapses because tiny initial differences amplify into large trajectory differences over time. [source: https://doi.org/10.1175/1520-0469(1963)020%3C0130:DNF%3E2.0.CO;2; https://www.ams.org/publicoutreach/feature-column/fcarc-lorenz]

#### D. Adversarial fragility in machine learning

- [fact] Goodfellow et al. state that several machine learning models misclassify adversarial examples, inputs formed by small intentionally worst-case perturbations, and do so with high confidence. [source: https://arxiv.org/abs/1412.6572]
- [fact] Goodfellow et al. argue that the primary cause of vulnerability to adversarial perturbation is the models' linear nature in high-dimensional spaces rather than extreme nonlinearity. [source: https://arxiv.org/abs/1412.6572]
- [fact] The same paper reports that adversarial examples often generalize across architectures and training sets, which suggests a structural rather than purely incidental mechanism. [source: https://arxiv.org/abs/1412.6572]
- [fact] Research Question 2.3 concluded that predictive systems lacking invariant governing structure can behave differently under perturbation or deployment shift even when held-out performance looks strong. [source: https://davidamitchell.github.io/Research/research/2026-05-18-rq2-3-predictive-model-fragility.html]
- [inference] Adversarial fragility is therefore a perturbation-sensitivity phenomenon in which small input moves cross a decision boundary or exploit a high-dimensional linear response that the model has not been constrained to stabilize. [source: https://arxiv.org/abs/1412.6572; https://davidamitchell.github.io/Research/research/2026-05-18-rq2-3-predictive-model-fragility.html]

#### E. Lamport logical clocks as a partial-order response

- [fact] Lamport's abstract states that the concept of one event happening before another in a distributed system defines a partial ordering of events and that a distributed algorithm can synchronize logical clocks to totally order events. [source: https://lamport.azurewebsites.net/pubs/time-clocks.pdf]
- [fact] Lamport defines the happened-before relation so that events in the same process preserve sequence order, message send precedes receipt, and the relation is transitive. [source: https://lamport.azurewebsites.net/pubs/time-clocks.pdf]
- [fact] Lamport defines two events as concurrent when neither happens before the other. [source: https://lamport.azurewebsites.net/pubs/time-clocks.pdf]
- [inference] Logical clocks improve reasoning about causality, but they do not remove the underlying concurrency problem because concurrent events remain causally incomparable even when a logical timestamping scheme imposes a convenient total order for coordination. [source: https://lamport.azurewebsites.net/pubs/time-clocks.pdf]

#### F. Cross-item integration and boundary setting

- [fact] Research Question 6.1 concluded that unrestricted exact static analysis of arbitrary program semantics is impossible, which means dynamic reasoning must still confront practical limits after the theorem-level limit is acknowledged. [source: https://davidamitchell.github.io/Research/research/2026-05-18-rq6-1-halting-problem-static-analysis.html]
- [fact] Research Question 5.1 concluded that deterministic coded systems preserve stronger replayability than stochastic language-model systems, even though both can fail under bad inputs. [source: https://davidamitchell.github.io/Research/research/2026-05-18-rq5-1-stochastic-vs-deterministic-failures.html]
- [inference] This item extends Research Question 6.1 by showing that even when a system is deterministic and fully specified, fragility can reappear through combinatorial growth and perturbation sensitivity rather than through semantic undecidability alone. [source: https://davidamitchell.github.io/Research/research/2026-05-18-rq6-1-halting-problem-static-analysis.html; https://www.cs.vsb.cz/kot/down/Texts/StateSpace.pdf; https://doi.org/10.1175/1520-0469(1963)020%3C0130:DNF%3E2.0.CO;2]
- [inference] This item also sharpens Research Question 2.3 by distinguishing two neighboring but non-identical fragility classes, trajectory-level sensitive dependence in chaotic dynamics and decision-boundary sensitivity in machine learning models. [source: https://davidamitchell.github.io/Research/research/2026-05-18-rq2-3-predictive-model-fragility.html; https://arxiv.org/abs/1412.6572; https://doi.org/10.1175/1520-0469(1963)020%3C0130:DNF%3E2.0.CO;2]

### §3 Reasoning

- [fact] The concurrent-systems evidence establishes exponential growth in reachable states and schedule-sensitive failures, while the Lorenz and adversarial-learning evidence establishes two different perturbation-sensitivity mechanisms. [source: https://www.cs.vsb.cz/kot/down/Texts/StateSpace.pdf; https://docs.oracle.com/javase/tutorial/essential/concurrency/interfere.html; https://doi.org/10.1175/1520-0469(1963)020%3C0130:DNF%3E2.0.CO;2; https://arxiv.org/abs/1412.6572]
- [inference] The strongest defensible common claim is not that concurrency, chaos, and adversarial machine learning are the same theory, but that each shows how small local differences can produce large global behavioral differences in deterministic or near-deterministic computational systems. [source: https://www.cs.vsb.cz/kot/down/Texts/StateSpace.pdf; https://doi.org/10.1175/1520-0469(1963)020%3C0130:DNF%3E2.0.CO;2; https://arxiv.org/abs/1412.6572]
- [inference] The strongest defensible difference claim is that chaotic systems amplify nearby initial states through time-evolving dynamics, whereas adversarial examples exploit the geometry of a learned classifier at or near a decision boundary. [source: https://doi.org/10.1175/1520-0469(1963)020%3C0130:DNF%3E2.0.CO;2; https://arxiv.org/abs/1412.6572]
- [inference] Lamport's logical clocks belong in the comparison because they show that some concurrency fragility can be disciplined through causal ordering, but not eliminated by wishing away the existence of concurrent states. [source: https://lamport.azurewebsites.net/pubs/time-clocks.pdf]

### §4 Consistency Check

- [fact] Tension: Lorenz-style chaos studies continuous dynamical systems, while adversarial examples are usually analyzed in high-dimensional classifiers. [source: https://doi.org/10.1175/1520-0469(1963)020%3C0130:DNF%3E2.0.CO;2; https://arxiv.org/abs/1412.6572]
- [inference] Resolution: the comparison is about fragility under small perturbations, not about literal identity of the governing mathematics, so the correct bridge is structural analogy plus bounded contrast. [source: https://doi.org/10.1175/1520-0469(1963)020%3C0130:DNF%3E2.0.CO;2; https://arxiv.org/abs/1412.6572]
- [fact] Tension: logical clocks can impose an event order and therefore seem to solve nondeterminism. [source: https://lamport.azurewebsites.net/pubs/time-clocks.pdf]
- [inference] Resolution: Lamport solves a coordination and reasoning problem about causal order, not the entire explosion of reachable concurrent states or every schedule-dependent bug. [source: https://lamport.azurewebsites.net/pubs/time-clocks.pdf; https://www.cs.vsb.cz/kot/down/Texts/StateSpace.pdf]
- [fact] Tension: Research Question 5.1 found stronger replayability for deterministic coded systems. [source: https://davidamitchell.github.io/Research/research/2026-05-18-rq5-1-stochastic-vs-deterministic-failures.html]
- [inference] Resolution: replayability and fragility are different axes, so a deterministic system can be more replayable than a stochastic one while still being fragile under interleavings or sensitive initial conditions. [source: https://davidamitchell.github.io/Research/research/2026-05-18-rq5-1-stochastic-vs-deterministic-failures.html; https://docs.oracle.com/javase/tutorial/essential/concurrency/interfere.html; https://doi.org/10.1175/1520-0469(1963)020%3C0130:DNF%3E2.0.CO;2]

### §5 Depth and Breadth Expansion

- [inference] Technical lens: concurrency fragility comes from branching combinations of states and schedules, chaos fragility comes from trajectory divergence under tiny initial differences, and adversarial fragility comes from unstable local geometry in a learned decision surface. [source: https://www.cs.vsb.cz/kot/down/Texts/StateSpace.pdf; https://doi.org/10.1175/1520-0469(1963)020%3C0130:DNF%3E2.0.CO;2; https://arxiv.org/abs/1412.6572]
- [fact] Historical lens: Lorenz published the deterministic-chaos result in 1963, and Lamport published the happened-before ordering framework in 1978. [source: https://doi.org/10.1175/1520-0469(1963)020%3C0130:DNF%3E2.0.CO;2; https://lamport.azurewebsites.net/pubs/time-clocks.pdf]
- [inference] Operational lens: the practical governance lesson is that deterministic systems do not become safe merely because they are non-stochastic, since concurrency and sensitivity can still destroy tractable prediction or exhaustive verification. [source: https://www.cs.vsb.cz/kot/down/Texts/StateSpace.pdf; https://docs.oracle.com/javase/tutorial/essential/concurrency/interfere.html; https://davidamitchell.github.io/Research/research/2026-05-18-rq6-1-halting-problem-static-analysis.html]
- [inference] Epistemic lens: this item completes a two-step boundary argument in which Research Question 6.1 explains why unrestricted exact semantic knowledge is impossible in general, while the present item explains why practical prediction can still fail badly even after the code and update rules are fully known. [source: https://davidamitchell.github.io/Research/research/2026-05-18-rq6-1-halting-problem-static-analysis.html; https://www.cs.vsb.cz/kot/down/Texts/StateSpace.pdf; https://doi.org/10.1175/1520-0469(1963)020%3C0130:DNF%3E2.0.CO;2]

### §6 Synthesis

**Executive summary:**

State space explosion and deterministic chaos do mirror machine-learning fragility, but only at the level of bounded perturbation sensitivity rather than as one shared mathematical theorem. [inference; source: https://www.cs.vsb.cz/kot/down/Texts/StateSpace.pdf; https://doi.org/10.1175/1520-0469(1963)020%3C0130:DNF%3E2.0.CO;2; https://arxiv.org/abs/1412.6572]
In concurrent coded systems, the core mechanism is combinatorial growth of reachable states and interleavings, which makes exhaustive verification or prediction practically intractable and manifests concretely in race conditions. [fact; source: https://www.cs.vsb.cz/kot/down/Texts/StateSpace.pdf; https://docs.oracle.com/javase/tutorial/essential/concurrency/interfere.html; https://cwe.mitre.org/data/definitions/362.html]
In Lorenz-style chaos, the core mechanism is sensitive dependence on initial conditions, where tiny initial differences evolve into large trajectory differences despite fully deterministic governing equations. [fact; source: https://doi.org/10.1175/1520-0469(1963)020%3C0130:DNF%3E2.0.CO;2; https://www.ams.org/publicoutreach/feature-column/fcarc-lorenz]
In adversarial machine learning, small worst-case perturbations can force high-confidence errors through high-dimensional linear sensitivity and unstable learned boundaries, which makes adversarial fragility a useful comparison point rather than a proven equivalent of chaotic sensitivity. [inference; source: https://arxiv.org/abs/1412.6572; https://davidamitchell.github.io/Research/research/2026-05-18-rq2-3-predictive-model-fragility.html]
Lamport's logical clocks narrow one part of the concurrency problem by preserving causal order, but they do not remove the underlying branching state space or all schedule-dependent behavior. [inference; source: https://lamport.azurewebsites.net/pubs/time-clocks.pdf; https://www.cs.vsb.cz/kot/down/Texts/StateSpace.pdf]

**Key findings:**

1. [fact] State space explosion in concurrent systems is a genuine exponential-growth problem, because the reachable state space often grows exponentially in the number of processes and variables rather than merely linearly with added components. [source: https://www.cs.vsb.cz/kot/down/Texts/StateSpace.pdf] **Confidence:** Medium.
2. [inference] Race conditions are the runtime symptom of that explosion, because multiple valid interleavings of simple read-modify-write operations can produce different outcomes from the same code and nominal input. [source: https://docs.oracle.com/javase/tutorial/essential/concurrency/interfere.html; https://cwe.mitre.org/data/definitions/362.html; https://www.cs.vsb.cz/kot/down/Texts/StateSpace.pdf] **Confidence:** Medium.
3. [fact] Lorenz's deterministic nonperiodic-flow result shows that deterministic equations can still yield practical unpredictability when small initial differences grow into considerably different later states. [source: https://doi.org/10.1175/1520-0469(1963)020%3C0130:DNF%3E2.0.CO;2; https://www.ams.org/publicoutreach/feature-column/fcarc-lorenz] **Confidence:** Medium.
4. [inference] Adversarial examples show small-perturbation vulnerability inside machine learning, and this item treats that result as an analogous sensitivity pattern because small worst-case perturbations can force high-confidence misclassification through high-dimensional linear behavior. [source: https://arxiv.org/abs/1412.6572] **Confidence:** Medium.
5. [inference] Across concurrency, chaos, and adversarial learning, small local perturbations can trigger much larger qualitative behavioral changes than a simple reading of the governing rules would suggest. [source: https://www.cs.vsb.cz/kot/down/Texts/StateSpace.pdf; https://doi.org/10.1175/1520-0469(1963)020%3C0130:DNF%3E2.0.CO;2; https://arxiv.org/abs/1412.6572] **Confidence:** Medium.
6. [inference] The analogy stops at mechanism, because chaotic sensitivity tracks divergence of nearby trajectories through time while adversarial fragility usually tracks local instability of a learned classifier around a decision boundary at inference time. [source: https://doi.org/10.1175/1520-0469(1963)020%3C0130:DNF%3E2.0.CO;2; https://arxiv.org/abs/1412.6572] **Confidence:** Medium.
7. [fact] Lamport's happened-before relation provides a rigorous partial-order framework for causal ordering in distributed systems, but concurrent events remain those for which neither event happens before the other. [source: https://lamport.azurewebsites.net/pubs/time-clocks.pdf] **Confidence:** Medium.
8. [inference] This item extends Research Question 6.1 and Research Question 2.3 together by showing that formal impossibility and structural fragility are complementary rather than competing explanations of why deterministic coded systems can still be hard to predict, verify, or stabilize. [source: https://davidamitchell.github.io/Research/research/2026-05-18-rq6-1-halting-problem-static-analysis.html; https://davidamitchell.github.io/Research/research/2026-05-18-rq2-3-predictive-model-fragility.html; https://www.cs.vsb.cz/kot/down/Texts/StateSpace.pdf; https://doi.org/10.1175/1520-0469(1963)020%3C0130:DNF%3E2.0.CO;2] **Confidence:** Medium.

**Evidence map:**

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [fact] Reachable state spaces in concurrent systems often grow exponentially with added processes and variables. | https://www.cs.vsb.cz/kot/down/Texts/StateSpace.pdf | high | Formal state-growth claim |
| [inference] Race conditions operationalize interleaving explosion because different valid schedules can overwrite one another's effects. | https://docs.oracle.com/javase/tutorial/essential/concurrency/interfere.html ; https://cwe.mitre.org/data/definitions/362.html ; https://www.cs.vsb.cz/kot/down/Texts/StateSpace.pdf | medium | Lost-update example plus concurrency definition |
| [fact] Lorenz's system shows small initial differences yielding considerably different later states under deterministic equations. | https://doi.org/10.1175/1520-0469(1963)020%3C0130:DNF%3E2.0.CO;2 ; https://www.ams.org/publicoutreach/feature-column/fcarc-lorenz | medium | Classic chaos result |
| [inference] Adversarial examples provide a useful analogue because small perturbations can produce high-confidence model errors, with high-dimensional linearity offered as a primary explanation inside machine learning. | https://arxiv.org/abs/1412.6572 | medium | Analogy grounded in primary adversarial-example paper |
| [inference] Concurrency fragility, chaos sensitivity, and adversarial fragility share a bounded perturbation-sensitivity pattern without sharing one identical mechanism. | https://www.cs.vsb.cz/kot/down/Texts/StateSpace.pdf ; https://doi.org/10.1175/1520-0469(1963)020%3C0130:DNF%3E2.0.CO;2 ; https://arxiv.org/abs/1412.6572 | medium | Structural analogy, not theorem identity |
| [inference] Chaotic sensitivity and adversarial fragility differ because one is trajectory divergence over time and the other is local decision-boundary sensitivity. | https://doi.org/10.1175/1520-0469(1963)020%3C0130:DNF%3E2.0.CO;2 ; https://arxiv.org/abs/1412.6572 | medium | Mechanism contrast |
| [fact] Lamport clocks formalize happened-before as a partial order and define concurrency as causal incomparability. | https://lamport.azurewebsites.net/pubs/time-clocks.pdf | high | Formal ordering result |
| [inference] Research Question 6.1 and Research Question 2.3 combine into a stronger boundary claim once dynamic sensitivity is added. | https://davidamitchell.github.io/Research/research/2026-05-18-rq6-1-halting-problem-static-analysis.html ; https://davidamitchell.github.io/Research/research/2026-05-18-rq2-3-predictive-model-fragility.html ; https://www.cs.vsb.cz/kot/down/Texts/StateSpace.pdf ; https://doi.org/10.1175/1520-0469(1963)020%3C0130:DNF%3E2.0.CO;2 | medium | Cross-item synthesis |

**Assumptions:**

- [assumption] The Lorenz paper's abstracted statement about instability under small modifications is sufficient for this item's bounded comparison, because the question asks for a formal mirror of fragility rather than a full proof survey of modern chaos theory. [source: https://doi.org/10.1175/1520-0469(1963)020%3C0130:DNF%3E2.0.CO;2; https://www.ams.org/publicoutreach/feature-column/fcarc-lorenz]
- [assumption] Kot's accessible state-explosion note is an adequate substitute for the seeded paywalled model-checking book because it states the needed exponential-growth claim directly and in scope. [source: https://www.cs.vsb.cz/kot/down/Texts/StateSpace.pdf; https://mitpress.mit.edu/9780262038553/model-checking/]

**Analysis:**

The analogy is defensible because all three domains punish small local differences with much larger downstream behavioral changes than naive intuitions expect. [inference; source: https://www.cs.vsb.cz/kot/down/Texts/StateSpace.pdf; https://doi.org/10.1175/1520-0469(1963)020%3C0130:DNF%3E2.0.CO;2; https://arxiv.org/abs/1412.6572]
Its limit is mechanistic rather than empirical, because concurrent software fragility is combinatorial, chaotic fragility is dynamical, and adversarial machine-learning fragility is geometric and statistical. [inference; source: https://www.cs.vsb.cz/kot/down/Texts/StateSpace.pdf; https://doi.org/10.1175/1520-0469(1963)020%3C0130:DNF%3E2.0.CO;2; https://arxiv.org/abs/1412.6572]
Lamport's logical clocks matter because they show one principled mitigation strategy, adding causal structure to event order, yet they also clarify the limit of that mitigation because concurrency itself is not abolished by assigning timestamps. [inference; source: https://lamport.azurewebsites.net/pubs/time-clocks.pdf]
That bounded reading fits the prior repository items better than a stronger claim of literal equivalence, because Research Question 6.1 is about semantic undecidability and Research Question 2.3 is about missing invariant structure rather than about one universal fragility mechanism. [inference; source: https://davidamitchell.github.io/Research/research/2026-05-18-rq6-1-halting-problem-static-analysis.html; https://davidamitchell.github.io/Research/research/2026-05-18-rq2-3-predictive-model-fragility.html]

**Risks, gaps, uncertainties:**

- [fact] The Lorenz source base used here is narrower than the source base for concurrency and adversarial examples, because the argument relies on the Lorenz DOI record plus one accessible American Mathematical Society exposition rather than on a broader sampled chaos-theory literature. [source: https://doi.org/10.1175/1520-0469(1963)020%3C0130:DNF%3E2.0.CO;2; https://www.ams.org/publicoutreach/feature-column/fcarc-lorenz]
- [fact] The state-space evidence is grounded in an accessible survey note rather than the seeded model-checking textbook, so the exponential-growth claim is secure but the broader reduction-technique literature is only lightly sampled here. [source: https://www.cs.vsb.cz/kot/down/Texts/StateSpace.pdf; https://mitpress.mit.edu/9780262038553/model-checking/]
- [inference] The machine-learning comparison is strongest for adversarial examples and broader predictive fragility, but weaker for any claim that all machine-learning perturbation sensitivity should be interpreted through chaos-theory vocabulary. [source: https://arxiv.org/abs/1412.6572; https://davidamitchell.github.io/Research/research/2026-05-18-rq2-3-predictive-model-fragility.html]

**Open questions:**

- How far can the chaos-versus-adversarial analogy be pushed before it stops being decision-useful for formal verification or robustness engineering?
- What stronger source base would be needed to compare Lyapunov-style instability measures with modern adversarial-robustness metrics directly?
- Which partial-order or reduction techniques best shrink concurrent state spaces without hiding the most safety-critical race behaviors?

### §7 Recursive Review

review_result: pass
acronym_audit: passed after expanding machine learning on first use and avoiding unexplained new acronyms in Findings prose
claim_label_audit: passed, all claim-bearing prose in Research Skill Output is marked as fact, inference, or assumption
cross_item_integration: Research Question 6.1 and Research Question 2.3 cited directly, Research Question 5.1 cited as related operational qualifier
remaining_limit: medium-confidence boundary kept on the strongest analogy claims because the compared mechanisms are adjacent, not identical

---

## Findings

*(Populated from §6 Synthesis above.)*

### Executive Summary

State space explosion and deterministic chaos do mirror machine-learning fragility, but only at the level of bounded perturbation sensitivity rather than as one shared mathematical theorem. [inference; source: https://www.cs.vsb.cz/kot/down/Texts/StateSpace.pdf; https://doi.org/10.1175/1520-0469(1963)020%3C0130:DNF%3E2.0.CO;2; https://arxiv.org/abs/1412.6572]
In concurrent coded systems, the core mechanism is combinatorial growth of reachable states and interleavings, which makes exhaustive verification or prediction practically intractable and manifests concretely in race conditions. [fact; source: https://www.cs.vsb.cz/kot/down/Texts/StateSpace.pdf; https://docs.oracle.com/javase/tutorial/essential/concurrency/interfere.html; https://cwe.mitre.org/data/definitions/362.html]
In Lorenz-style chaos, the core mechanism is sensitive dependence on initial conditions, where tiny initial differences evolve into large trajectory differences despite fully deterministic governing equations. [fact; source: https://doi.org/10.1175/1520-0469(1963)020%3C0130:DNF%3E2.0.CO;2; https://www.ams.org/publicoutreach/feature-column/fcarc-lorenz]
In adversarial machine learning, small worst-case perturbations can force high-confidence errors through high-dimensional linear sensitivity and unstable learned boundaries, which makes adversarial fragility a useful comparison point rather than a proven equivalent of chaotic sensitivity. [inference; source: https://arxiv.org/abs/1412.6572; https://davidamitchell.github.io/Research/research/2026-05-18-rq2-3-predictive-model-fragility.html]
Lamport's logical clocks narrow one part of the concurrency problem by preserving causal order, but they do not remove the underlying branching state space or all schedule-dependent behavior. [inference; source: https://lamport.azurewebsites.net/pubs/time-clocks.pdf; https://www.cs.vsb.cz/kot/down/Texts/StateSpace.pdf]

### Key Findings

1. **State space explosion in concurrent systems is a genuine exponential-growth problem, because the reachable state space often grows exponentially in the number of processes and variables rather than merely linearly with added components.** ([fact]; medium confidence; source: https://www.cs.vsb.cz/kot/down/Texts/StateSpace.pdf)
2. **Race conditions are the runtime symptom of that explosion, because multiple valid interleavings of simple read-modify-write operations can produce different outcomes from the same code and nominal input.** ([inference]; medium confidence; source: https://docs.oracle.com/javase/tutorial/essential/concurrency/interfere.html; https://cwe.mitre.org/data/definitions/362.html; https://www.cs.vsb.cz/kot/down/Texts/StateSpace.pdf)
3. **Lorenz's deterministic nonperiodic-flow result shows that deterministic equations can still yield practical unpredictability when small initial differences grow into considerably different later states.** ([fact]; medium confidence; source: https://doi.org/10.1175/1520-0469(1963)020%3C0130:DNF%3E2.0.CO;2; https://www.ams.org/publicoutreach/feature-column/fcarc-lorenz)
4. **Adversarial examples show small-perturbation vulnerability inside machine learning, and this item treats that result as an analogous sensitivity pattern because small worst-case perturbations can force high-confidence misclassification through high-dimensional linear behavior.** ([inference]; medium confidence; source: https://arxiv.org/abs/1412.6572)
5. **Across concurrency, chaos, and adversarial learning, small local perturbations can trigger much larger qualitative behavioral changes than a simple reading of the governing rules would suggest.** ([inference]; medium confidence; source: https://www.cs.vsb.cz/kot/down/Texts/StateSpace.pdf; https://doi.org/10.1175/1520-0469(1963)020%3C0130:DNF%3E2.0.CO;2; https://arxiv.org/abs/1412.6572)
6. **The analogy stops at mechanism, because chaotic sensitivity tracks divergence of nearby trajectories through time while adversarial fragility usually tracks local instability of a learned classifier around a decision boundary at inference time.** ([inference]; medium confidence; source: https://doi.org/10.1175/1520-0469(1963)020%3C0130:DNF%3E2.0.CO;2; https://arxiv.org/abs/1412.6572)
7. **Lamport's happened-before relation provides a rigorous partial-order framework for causal ordering in distributed systems, but concurrent events remain those for which neither event happens before the other.** ([fact]; medium confidence; source: https://lamport.azurewebsites.net/pubs/time-clocks.pdf)
8. **This item extends Research Question 6.1 and Research Question 2.3 together by showing that formal impossibility and structural fragility are complementary rather than competing explanations of why deterministic coded systems can still be hard to predict, verify, or stabilize.** ([inference]; medium confidence; source: https://davidamitchell.github.io/Research/research/2026-05-18-rq6-1-halting-problem-static-analysis.html; https://davidamitchell.github.io/Research/research/2026-05-18-rq2-3-predictive-model-fragility.html; https://www.cs.vsb.cz/kot/down/Texts/StateSpace.pdf; https://doi.org/10.1175/1520-0469(1963)020%3C0130:DNF%3E2.0.CO;2)

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [fact] Reachable state spaces in concurrent systems often grow exponentially with added processes and variables. | https://www.cs.vsb.cz/kot/down/Texts/StateSpace.pdf | high | Formal state-growth claim |
| [inference] Race conditions operationalize interleaving explosion because different valid schedules can overwrite one another's effects. | https://docs.oracle.com/javase/tutorial/essential/concurrency/interfere.html ; https://cwe.mitre.org/data/definitions/362.html ; https://www.cs.vsb.cz/kot/down/Texts/StateSpace.pdf | medium | Lost-update example plus concurrency definition |
| [fact] Lorenz's system shows small initial differences yielding considerably different later states under deterministic equations. | https://doi.org/10.1175/1520-0469(1963)020%3C0130:DNF%3E2.0.CO;2 ; https://www.ams.org/publicoutreach/feature-column/fcarc-lorenz | medium | Classic chaos result |
| [inference] Adversarial examples provide a useful analogue because small perturbations can produce high-confidence model errors, with high-dimensional linearity offered as a primary explanation inside machine learning. | https://arxiv.org/abs/1412.6572 | medium | Analogy grounded in primary adversarial-example paper |
| [inference] Concurrency fragility, chaos sensitivity, and adversarial fragility share a bounded perturbation-sensitivity pattern without sharing one identical mechanism. | https://www.cs.vsb.cz/kot/down/Texts/StateSpace.pdf ; https://doi.org/10.1175/1520-0469(1963)020%3C0130:DNF%3E2.0.CO;2 ; https://arxiv.org/abs/1412.6572 | medium | Structural analogy, not theorem identity |
| [inference] Chaotic sensitivity and adversarial fragility differ because one is trajectory divergence over time and the other is local decision-boundary sensitivity. | https://doi.org/10.1175/1520-0469(1963)020%3C0130:DNF%3E2.0.CO;2 ; https://arxiv.org/abs/1412.6572 | medium | Mechanism contrast |
| [fact] Lamport clocks formalize happened-before as a partial order and define concurrency as causal incomparability. | https://lamport.azurewebsites.net/pubs/time-clocks.pdf | high | Formal ordering result |
| [inference] Research Questions 6.1 and 2.3 combine into a stronger boundary claim once dynamic sensitivity is added. | https://davidamitchell.github.io/Research/research/2026-05-18-rq6-1-halting-problem-static-analysis.html ; https://davidamitchell.github.io/Research/research/2026-05-18-rq2-3-predictive-model-fragility.html ; https://www.cs.vsb.cz/kot/down/Texts/StateSpace.pdf ; https://doi.org/10.1175/1520-0469(1963)020%3C0130:DNF%3E2.0.CO;2 | medium | Cross-item synthesis |

### Assumptions

- [assumption] The Lorenz paper's abstracted statement about instability under small modifications is sufficient for this item's bounded comparison, because the question asks for a formal mirror of fragility rather than a full proof survey of modern chaos theory. [source: https://doi.org/10.1175/1520-0469(1963)020%3C0130:DNF%3E2.0.CO;2; https://www.ams.org/publicoutreach/feature-column/fcarc-lorenz]
- [assumption] Kot's accessible state-explosion note is an adequate substitute for the seeded paywalled model-checking book because it states the needed exponential-growth claim directly and in scope. [source: https://www.cs.vsb.cz/kot/down/Texts/StateSpace.pdf; https://mitpress.mit.edu/9780262038553/model-checking/]

### Analysis

The analogy is defensible because all three domains punish small local differences with much larger downstream behavioral changes than naive intuitions expect. [inference; source: https://www.cs.vsb.cz/kot/down/Texts/StateSpace.pdf; https://doi.org/10.1175/1520-0469(1963)020%3C0130:DNF%3E2.0.CO;2; https://arxiv.org/abs/1412.6572]
Its limit is mechanistic rather than empirical, because concurrent software fragility is combinatorial, chaotic fragility is dynamical, and adversarial machine-learning fragility is geometric and statistical. [inference; source: https://www.cs.vsb.cz/kot/down/Texts/StateSpace.pdf; https://doi.org/10.1175/1520-0469(1963)020%3C0130:DNF%3E2.0.CO;2; https://arxiv.org/abs/1412.6572]
Lamport's logical clocks matter because they show one principled mitigation strategy, adding causal structure to event order, yet they also clarify the limit of that mitigation because concurrency itself is not abolished by assigning timestamps. [inference; source: https://lamport.azurewebsites.net/pubs/time-clocks.pdf]
That bounded reading fits the prior repository items better than a stronger claim of literal equivalence, because Research Question 6.1 is about semantic undecidability and Research Question 2.3 is about missing invariant structure rather than about one universal fragility mechanism. [inference; source: https://davidamitchell.github.io/Research/research/2026-05-18-rq6-1-halting-problem-static-analysis.html; https://davidamitchell.github.io/Research/research/2026-05-18-rq2-3-predictive-model-fragility.html]

### Risks, Gaps, and Uncertainties

- [fact] The Lorenz source base used here is narrower than the source base for concurrency and adversarial examples, because the argument relies on the Lorenz DOI record plus one accessible American Mathematical Society exposition rather than on a broader sampled chaos-theory literature. [source: https://doi.org/10.1175/1520-0469(1963)020%3C0130:DNF%3E2.0.CO;2; https://www.ams.org/publicoutreach/feature-column/fcarc-lorenz]
- [fact] The state-space evidence is grounded in an accessible survey note rather than the seeded model-checking textbook, so the exponential-growth claim is secure but the broader reduction-technique literature is only lightly sampled here. [source: https://www.cs.vsb.cz/kot/down/Texts/StateSpace.pdf; https://mitpress.mit.edu/9780262038553/model-checking/]
- [inference] The machine-learning comparison is strongest for adversarial examples and broader predictive fragility, but weaker for any claim that all machine-learning perturbation sensitivity should be interpreted through chaos-theory vocabulary. [source: https://arxiv.org/abs/1412.6572; https://davidamitchell.github.io/Research/research/2026-05-18-rq2-3-predictive-model-fragility.html]

### Open Questions

- How far can the chaos-versus-adversarial analogy be pushed before it stops being decision-useful for formal verification or robustness engineering?
- What stronger source base would be needed to compare Lyapunov-style instability measures with modern adversarial-robustness metrics directly?
- Which partial-order or reduction techniques best shrink concurrent state spaces without hiding the most safety-critical race behaviors?

---

## Output

- Type: knowledge
- Description: comparative knowledge note on concurrency, chaos, and perturbation sensitivity.
- Links:
  - https://www.cs.vsb.cz/kot/down/Texts/StateSpace.pdf
  - https://doi.org/10.1175/1520-0469(1963)020%3C0130:DNF%3E2.0.CO;2
  - https://arxiv.org/abs/1412.6572
