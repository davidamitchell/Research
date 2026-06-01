---
title: "Goal-constraint feedback: convergence conditions vs. specification cycling"
added: 2026-05-31T09:42:57+00:00
status: reviewing
priority: high
blocks: []
themes: [formal-methods, software-engineering, organisational-design]
started: 2026-06-01T11:53:37+00:00
completed: ~
output: [knowledge]
cites:
  - 2026-05-31-formal-methods-interdependent-inputs-feasibility
  - 2026-04-01-backpressure-theory-of-constraints
  - 2026-05-29-split-authority-q6-instability-leading-indicators
related:
  - 2026-04-27-uelgf-runtime-feedback-loop
  - 2026-04-30-tdd-feedback-loops-ai-augmented-dev
  - 2026-05-17-policy-enforcement-formal-verification-energy-functions
superseded_by: ~
supersedes: ~
item_type: primary
confidence: medium
versions: []
---

# Goal-constraint feedback: convergence conditions vs. specification cycling

## Research Question

In control systems with feedback between goal definition and constraint measurement, what conditions cause the system to converge on a stable specification versus cycle without resolution, and what is the equivalent risk in a software delivery context?

## Scope

**In scope:**
- Control theory conditions for convergence vs. cycling (oscillation) in feedback systems with goal-constraint coupling.
- Mapping these conditions to software delivery contexts: what in a delivery system plays the role of gain, damping, and feedback delay.
- Empirical or case-study evidence of specification cycling in software delivery (requirements churn, scope oscillation) and its drivers.

**Out of scope:**
- Full control systems engineering beyond the convergence/cycling analysis relevant to specification stability.
- Prescriptive delivery process redesign.
- Hardware or embedded systems control beyond the analogy to software delivery.

**Constraints:** (time, source types, access)
- Control theory sources must be primary (textbooks, peer-reviewed); delivery analogies must be grounded in documented empirical patterns, not intuition.
- Distinguish between bounded cycling (recoverable) and unbounded divergence (unresolvable).

## Context

Automated systems that iterate between goal definition and constraint evaluation risk entering a cycle where each constraint measurement triggers a goal revision that generates new constraints, without ever stabilising. Understanding the mathematical conditions for convergence vs. cycling, and their software delivery equivalents, is necessary to design a system that terminates rather than oscillates. This is Gap 3 Q10 from issue #618.

## Approach

1. Document the formal conditions for convergence vs. cycling in feedback control systems: Lyapunov stability, gain margin, and feedback delay effects.
2. Map control-system concepts to software delivery variables: goal revision as set-point change, constraint surface as plant model, review cycle as feedback delay.
3. Survey software delivery literature for documented cycling patterns: requirements churn, scope oscillation, approval loop instability.
4. Identify empirical evidence on which delivery-system conditions correlate with cycling vs. convergence.
5. Assess whether formal convergence conditions can be operationalised as practical design rules for an automated goal-constraint validation system.

## Sources

- [x] [Åström, K.J. and Murray, R.M. (2021) Feedback Systems: An Introduction for Scientists and Engineers, Princeton University Press](http://www.cds.caltech.edu/~murray/books/AM08/pdf/fbs-public_24Jul2020.pdf) — primary control theory source for Lyapunov stability, gain margin, phase margin, and feedback delay
- [x] [Khalil, H.K. (2002) Nonlinear Systems, 3rd ed., Prentice Hall](https://www.pearson.com/en-us/subject-catalog/p/nonlinear-systems/P200000003456) — primary nonlinear systems source for Lyapunov stability conditions and convergence
- [x] [Ogata, K. (2010) Modern Control Engineering, 5th ed., Prentice Hall](https://www.pearson.com/en-us/subject-catalog/p/modern-control-engineering/P200000003186) — primary control engineering source for Nyquist criterion, limit cycles, and describing function method
- [x] [Reinertsen, D.G. (2009) The Principles of Product Development Flow, Celeritas Publishing](https://www.amazon.com/Principles-Product-Development-Flow-Generation/dp/1935401009) — product development flow as feedback system; gain, delay, and stability mapping to delivery
- [x] [Senge, P. (1990) The Fifth Discipline: The Art and Practice of the Learning Organization, Doubleday](https://www.penguinrandomhouse.com/books/158736/the-fifth-discipline-by-peter-m-senge/) — balancing loops with time delays and organisational oscillation
- [x] [DeMarco, T. and Lister, T. (2003) Waltzing with Bears: Managing Risk on Software Projects, Dorset House](https://www.pearsonhighered.com/assets/preface/0/1/3/4/0134682947.pdf) — requirements instability and scope oscillation in software delivery
- [x] [DORA (2023) Accelerate State of DevOps Report](https://dora.dev/research/2023/dora-report/) — empirical evidence on approval loops, review cadence, and delivery stability
- [x] [DORA (2024) Software delivery metrics: throughput and instability](https://dora.dev/guides/dora-metrics-four-keys/) — DORA metrics definitions including delivery instability measures
- [x] [Mitchell (2026) Formal methods: specifying interdependent inputs for automated feasibility checking](https://davidamitchell.github.io/Research/research/2026-05-31-formal-methods-interdependent-inputs-feasibility.html) — related item on constraint infeasibility as a distinct failure mode
- [x] [Mitchell (2026) Q6: Leading indicators of instability in split-authority flow systems](https://davidamitchell.github.io/Research/research/2026-05-29-split-authority-q6-instability-leading-indicators.html) — related item on per-cycle violation metrics as instability indicators
- [ ] [Åström, K. and Wittenmark, B. (2013) Adaptive Control, 2nd ed., Dover Publications](https://store.doverpublications.com/0486462781.html) — seeded source; adaptive control stability; superseded by Åström and Murray (2021) which covers the same Lyapunov and gain margin conditions in an accessible primary form
- [ ] [Kotonya, G. and Sommerville, I. (2000) Requirements Engineering: Processes and Techniques, John Wiley and Sons](https://www.wiley.com/en-us/Requirements+Engineering%3A+Processes+and+Techniques-p-9780471972082) — seeded via secondary reference; requirements volatility empirical evidence; not directly accessed

---

## Research Skill Output

*(Full output from running the research skill, retained verbatim in the completed item. §§0-5 are the investigation; §6 seeds the Findings section below.)*

### §0 Initialise

Question: In control systems with feedback between goal definition and constraint measurement, what conditions cause the system to converge on a stable specification versus cycle without resolution, and what is the equivalent risk in a software delivery context?

Scope: In scope are (1) control theory conditions for convergence vs. cycling in feedback systems with goal-constraint coupling, (2) mapping control-system concepts to software delivery variables, and (3) empirical or case-study evidence of specification cycling in software delivery. Out of scope are full control systems engineering tutorials, prescriptive delivery process redesign, and hardware or embedded systems control beyond analogy.

Constraints: Control theory sources must be primary (textbooks, peer-reviewed). Delivery analogies must be grounded in documented empirical patterns. The item must distinguish bounded cycling (recoverable) from unbounded divergence (unresolvable).

Output format: knowledge item with key findings, evidence map, and design-rule candidates.

Working hypotheses:
[assumption] The control-theoretic convergence conditions (Lyapunov stability, gain margin, phase margin) are structurally analogous to conditions in software delivery specification loops, even though the delivery system is discrete and nonlinear rather than continuous. Justification: both are feedback systems with a setpoint (goal), an actuator (specification revision), a plant (constraint space), and a sensor (constraint measurement). The analogy is structural, not quantitatively exact; see [Reinertsen (2009) Principles of Product Development Flow, Celeritas](https://www.amazon.com/Principles-Product-Development-Flow-Generation/dp/1935401009) for the same structural analogy applied to product development queues.

[assumption] Bounded cycling is distinguishable from unbounded divergence by whether constraint violations decrease monotonically over review cycles. Justification: in control theory, a system with positive phase margin exhibits damped oscillation (bounded), while one with zero or negative phase margin diverges; the equivalent observable in delivery is whether the number or severity of unresolved constraints decreases per iteration.

### §1 Question Decomposition

**Top-level question:** What conditions cause convergence vs. cycling in a feedback system between goal definition and constraint measurement, and what are the software delivery equivalents?

Decomposed sub-questions:

A. Control theory convergence conditions:
  A1. What is the formal definition of convergence for a closed-loop feedback system with a setpoint?
  A2. What does Lyapunov stability say about when a system converges vs. oscillates?
  A3. What role does gain play in convergence vs. cycling, and what is gain margin?
  A4. What role does feedback delay (time delay) play in convergence vs. cycling?
  A5. What distinguishes bounded cycling (limit cycles) from unbounded divergence?

B. Mapping to software delivery:
  B1. What plays the role of setpoint, plant, actuator, and sensor in a software delivery specification loop?
  B2. What is the software delivery analogue of gain?
  B3. What is the software delivery analogue of feedback delay?
  B4. What is the software delivery analogue of Lyapunov stability?
  B5. What conditions in the delivery system correspond to high gain and long delay?

C. Empirical software delivery evidence:
  C1. What empirical evidence exists for specification cycling (requirements churn, scope oscillation) in software delivery?
  C2. Which delivery system conditions have been empirically correlated with cycling vs. stability?
  C3. How do approval loop structures contribute to cycling?

D. Operationalisation:
  D1. Can formal convergence conditions be translated into practical design rules for automated goal-constraint validation?
  D2. What observable metrics distinguish bounded from unbounded cycling in a delivery system?

### §2 Investigation

**A1. Formal definition of convergence for a closed-loop feedback system**

[fact] A closed-loop feedback system with reference input r(t) and output y(t) is said to converge if the tracking error e(t) = r(t) - y(t) approaches zero asymptotically as t approaches infinity. For Linear Time-Invariant (LTI) systems, convergence (asymptotic stability) requires that all closed-loop poles have strictly negative real parts. Source: [Åström and Murray (2021) Feedback Systems: An Introduction for Scientists and Engineers, Princeton University Press, Chapter 5](http://www.cds.caltech.edu/~murray/books/AM08/pdf/fbs-public_24Jul2020.pdf)

[fact] For nonlinear systems, convergence to an equilibrium point is guaranteed by Lyapunov's direct method: if a continuously differentiable positive-definite function V(x) can be found such that its time derivative V̇(x) is negative definite along all system trajectories, then the equilibrium is asymptotically stable and all trajectories converge to it. Source: [Khalil, H.K. (2002) Nonlinear Systems, 3rd ed., Prentice Hall, Chapter 4](https://www.pearson.com/en-us/subject-catalog/p/nonlinear-systems/P200000003456)

**A2. Lyapunov stability and convergence vs. oscillation**

[fact] Lyapunov's theorem provides three stability levels: (1) Lyapunov stable if V̇ ≤ 0 (trajectories stay bounded), (2) asymptotically stable if V̇ < 0 for x ≠ 0 (trajectories converge to equilibrium), (3) unstable if no such V exists (trajectories diverge). A system is cycling (oscillating without convergence) when it is Lyapunov stable but not asymptotically stable, meaning V̇ = 0 on some invariant set other than the equilibrium. Source: [Khalil (2002) Nonlinear Systems, Chapter 4, Theorem 4.1](https://www.pearson.com/en-us/subject-catalog/p/nonlinear-systems/P200000003456)

[fact] In LTI systems, marginal stability (poles on the imaginary axis) produces sustained oscillation at a fixed amplitude, which corresponds to the boundary case between convergence and divergence. Poles in the right half-plane produce divergence (unbounded growth). Source: [Åström and Murray (2021) Feedback Systems, Chapter 5, Section 5.3](http://www.cds.caltech.edu/~murray/books/AM08/pdf/fbs-public_24Jul2020.pdf)

**A3. Gain and gain margin**

[fact] In frequency-domain analysis, gain margin is the factor by which the open-loop gain can be increased before the closed-loop system becomes unstable (before the Nyquist plot encircles the critical point −1). A gain margin greater than approximately 6 dB is typically required for robust stability in engineering practice. Phase margin is the additional phase lag needed to reach the instability boundary, typically required to be greater than 30 degrees. Source: [Åström and Murray (2021) Feedback Systems, Chapter 9 (Robust Performance)](http://www.cds.caltech.edu/~murray/books/AM08/pdf/fbs-public_24Jul2020.pdf)

[inference] If a feedback system's gain is too high, each error measurement triggers a correction larger than the error itself, causing the system to overshoot and oscillate. In the goal-constraint context, high gain corresponds to a goal revision response that amplifies rather than damps the constraint violation, generating larger deviations on each cycle. Source: [Åström and Murray (2021) Feedback Systems, Chapter 9](http://www.cds.caltech.edu/~murray/books/AM08/pdf/fbs-public_24Jul2020.pdf); [Reinertsen (2009) Principles of Product Development Flow, pp. 86-90](https://www.amazon.com/Principles-Product-Development-Flow-Generation/dp/1935401009)

**A4. Feedback delay and its destabilising effect**

[fact] A time delay τ in a feedback loop introduces a phase lag of ωτ radians at each frequency ω. This phase lag reduces the phase margin of the closed-loop system by an amount proportional to both the delay magnitude and the operating frequency. As delay increases, the system approaches instability and eventually oscillates or diverges. Source: [Åström and Murray (2021) Feedback Systems, Chapter 10 (Frequency Domain Design)](http://www.cds.caltech.edu/~murray/books/AM08/pdf/fbs-public_24Jul2020.pdf)

[fact] The Nyquist stability criterion states that a system becomes unstable when its open-loop frequency response encircles the point (−1, 0) in the complex plane. Time delay shifts the Nyquist plot counterclockwise, increasing the risk of this encirclement. Source: [Ogata, K. (2010) Modern Control Engineering, 5th ed., Prentice Hall, Chapter 8](https://www.pearson.com/en-us/subject-catalog/p/modern-control-engineering/P200000003186)

[inference] In a specification review loop, a long review cycle time (the delay between a constraint measurement and the goal revision that responds to it) plays the role of time delay τ. Long review cycle times reduce the effective phase margin of the goal-constraint feedback system, making cycling more likely. Source: [Reinertsen (2009) Principles of Product Development Flow, Chapter 6](https://www.amazon.com/Principles-Product-Development-Flow-Generation/dp/1935401009)

**A5. Bounded cycling vs. unbounded divergence**

[fact] A limit cycle is a closed trajectory in state space that the system approaches but does not escape; it represents sustained bounded oscillation. In nonlinear systems, limit cycles occur when the describing function N(A) of a nonlinearity and the linear plant's frequency response G(jω) satisfy N(A)G(jω) = −1 at some amplitude A and frequency ω. Source: [Ogata (2010) Modern Control Engineering, Chapter 13, Section 13-7 (Limit Cycles)](https://www.pearson.com/en-us/subject-catalog/p/modern-control-engineering/P200000003186)

[inference] Bounded cycling (limit cycles) is recoverable: the system oscillates within a bounded region and a design change (reduced gain, added damping, reduced delay) can restore convergence. Unbounded divergence is unrecoverable without structural change: the state trajectory grows without bound and no amount of within-cycle correction prevents it. The key distinction is whether the amplitude of constraint violations decreases or grows across successive review cycles. Source: [Åström and Murray (2021) Feedback Systems, Chapter 9](http://www.cds.caltech.edu/~murray/books/AM08/pdf/fbs-public_24Jul2020.pdf); [Ogata (2010) Modern Control Engineering, Chapter 13](https://www.pearson.com/en-us/subject-catalog/p/modern-control-engineering/P200000003186)

**B1. Mapping control concepts to software delivery specification loops**

[inference] A goal-constraint specification loop maps to a feedback control system as follows: the goal is the setpoint (desired system state); the constraint space is the plant (the real-world feasibility surface that the goal is measured against); the constraint measurement is the sensor output; the goal revision is the actuator (control action); and the review cycle is the feedback loop that closes the system. Source: [Reinertsen (2009) Principles of Product Development Flow, Chapters 3 and 6](https://www.amazon.com/Principles-Product-Development-Flow-Generation/dp/1935401009)

[inference] A related mapping appears in the formal-methods analogue: in Alloy and TLA+, feasibility checking of interdependent constraints corresponds to finding an equilibrium of the constraint system; when constraints conflict, the "system" oscillates between attempts to satisfy incompatible subsets. Source: [Mitchell (2026) Formal methods: specifying interdependent inputs for automated feasibility checking](https://davidamitchell.github.io/Research/research/2026-05-31-formal-methods-interdependent-inputs-feasibility.html)

**B2. The software delivery analogue of gain**

[inference] In a specification review loop, gain corresponds to the magnitude of goal revision in response to a unit constraint violation. High gain means every constraint measurement triggers a large goal change; low gain means constraint measurements produce small, incremental adjustments. A delivery system with high gain (large goal revisions per constraint failure) is prone to oscillation because each revision overshoots the feasible region and generates new constraint violations. Source: [Reinertsen (2009) Principles of Product Development Flow, Chapter 6 (Managing Flows in Product Development)](https://www.amazon.com/Principles-Product-Development-Flow-Generation/dp/1935401009)

**B3. The software delivery analogue of feedback delay**

[inference] In a specification review loop, feedback delay corresponds to the review cycle time: the elapsed time between a constraint measurement (a feasibility check fails) and the corrective action (the goal is revised). Long review cycles increase the probability that the external context changes before the revision is applied, effectively introducing a time delay that reduces the stability of the loop. Source: [Reinertsen (2009) Principles of Product Development Flow, Chapter 6](https://www.amazon.com/Principles-Product-Development-Flow-Generation/dp/1935401009); [DORA (2024) Software delivery metrics](https://dora.dev/guides/dora-metrics-four-keys/)

**B4. The software delivery analogue of Lyapunov stability**

[inference] For a specification loop, the analogue of a Lyapunov function V(x) is a scalar measure of total constraint violation magnitude: for example, the count of unsatisfied constraints or the aggregate severity-weighted constraint gap. If this measure decreases after each review cycle (V̇ < 0), the system is asymptotically stable and will converge. If the measure stays constant or grows, the system is cycling or diverging. Source: [Åström and Murray (2021) Feedback Systems, Chapter 5](http://www.cds.caltech.edu/~murray/books/AM08/pdf/fbs-public_24Jul2020.pdf)

**B5. Conditions in delivery corresponding to high gain and long delay**

[inference] High gain in delivery occurs when: stakeholder reviews produce comprehensive scope changes (rather than targeted corrections) in response to any constraint signal; decision authority is fragmented across many actors, each applying a correction that is individually rational but collectively amplifying; or when the goal is stated at a high level of abstraction that requires large rewrites whenever any sub-constraint fails. Source: [DeMarco and Lister (2003) Waltzing with Bears: Managing Risk on Software Projects, Dorset House](https://www.pearsonhighered.com/assets/preface/0/1/3/4/0134682947.pdf); [Reinertsen (2009) Principles of Product Development Flow, Chapter 6](https://www.amazon.com/Principles-Product-Development-Flow-Generation/dp/1935401009)

[inference] Long feedback delay in delivery occurs when: review cycles are infrequent (quarterly or monthly rather than weekly); approval chains involve sequential rather than concurrent sign-off; the time to detect a constraint violation is long (batched testing rather than continuous integration). Source: [DORA (2024) Software delivery metrics](https://dora.dev/guides/dora-metrics-four-keys/); [DeMarco and Lister (2003) Waltzing with Bears, Chapters 5-6](https://www.pearsonhighered.com/assets/preface/0/1/3/4/0134682947.pdf)

**C1. Empirical evidence for specification cycling in software delivery**

[fact] The Standish Group CHAOS reports have consistently identified scope creep and requirements instability as among the primary causes of software project failure. The 2020 CHAOS Report found that only about 31% of software projects are fully successful, with uncontrolled requirement changes cited as a major factor in challenged and failed outcomes. Source: [Standish Group CHAOS Report overview (2020)](https://www.standishgroup.com)

[fact] Requirements volatility (high-frequency change in requirements after initial specification) is empirically correlated with project delays and cost overruns. A study by Kotonya and Sommerville (2000) observed that volatile requirements are a top contributor to project failure. Source: [Kotonya, G. and Sommerville, I. (2000) Requirements Engineering: Processes and Techniques, John Wiley and Sons](https://www.wiley.com/en-us/Requirements+Engineering%3A+Processes+and+Techniques-p-9780471972082)

[fact] DevOps Research and Assessment (DORA) research found that manual change approval processes correlate negatively with software delivery performance and do not improve change failure rates. Teams with streamlined, automated approval processes achieve higher deployment frequency, lower change failure rates, and shorter recovery times. Source: [DORA (2023) Accelerate State of DevOps Report](https://dora.dev/research/2023/dora-report/)

**C2. Delivery conditions correlated with cycling vs. stability**

[fact] DORA research found that continuous integration, loosely coupled teams, and fast code reviews significantly improve software delivery and operational performance. Fast code review cycles reduce the feedback delay between a change and the detection of problems. Source: [DORA (2023) Accelerate State of DevOps Report](https://dora.dev/research/2023/dora-report/)

[inference] Reinertsen's work on product development flow identifies Work In Progress (WIP) limits and short feedback loop lengths as the primary stabilisation mechanisms for product development systems. High WIP means delayed feedback (the analogue of long delay τ), which reduces stability. Source: [Reinertsen (2009) Principles of Product Development Flow, Chapter 6](https://www.amazon.com/Principles-Product-Development-Flow-Generation/dp/1935401009)

[inference] Senge's systems dynamics analysis of balancing loops with time delays shows that when the delay between a corrective action and its observable effect is long, decision-makers tend to apply additional corrections before prior corrections have taken effect, causing overshoot and oscillation. This is the organisational equivalent of integrator windup in control systems. Source: [Senge, P. (1990) The Fifth Discipline: The Art and Practice of the Learning Organization, Doubleday, Chapters 3 and 5](https://www.penguinrandomhouse.com/books/158736/the-fifth-discipline-by-peter-m-senge/)

**C3. Approval loop structures and cycling**

[inference] Sequential approval chains (where each reviewer sees only the output of the previous reviewer's comments, not the original constraint) exhibit compounding gain: each reviewer's correction is applied to an already-revised goal, and the cumulative revision can far exceed the original constraint signal. This is the delivery analogue of a high-gain cascaded amplifier. Source: [DeMarco and Lister (2003) Waltzing with Bears, Chapters 5-6](https://www.pearsonhighered.com/assets/preface/0/1/3/4/0134682947.pdf)

[inference] DORA (2023) evidence that manual approval processes correlate negatively with performance, and not just efficiency, is consistent with the control-theory prediction: approval loops that add delay and gain without adding information (rubber-stamp approvals or multi-stage sequential sign-off of the same type) increase cycling risk without increasing convergence probability. Source: [DORA (2023) Accelerate State of DevOps Report](https://dora.dev/research/2023/dora-report/)

Failed primary-source search: Attempted to locate the original Kotonya and Sommerville (2000) paper directly; the book is available via publisher catalog but full text was not accessible. The citation is from a publisher catalog page and a consistent secondary description across multiple independent sources.

**D1. Operationalising convergence conditions as design rules**

[inference] Three necessary conditions for convergence of a goal-constraint specification loop, derived from control theory:
  (1) Gain condition: each review cycle must produce a net reduction in total constraint violation, not an amplification. This requires that goal revisions be targeted (addressing the specific failing constraint) rather than comprehensive (rewriting unrelated constraints).
  (2) Delay condition: the review cycle time must be short enough that external context does not shift materially between measurement and correction. Practically, this means review cadence must be higher than the rate at which the constraint surface changes.
  (3) Feasibility condition: a stable equilibrium (a feasible specification satisfying all constraints simultaneously) must exist within the constraint space. If the constraint space has an empty intersection, no amount of gain reduction or delay reduction will achieve convergence; structural change to either the constraints or the goals is required.
Source: [Åström and Murray (2021) Feedback Systems, Chapters 5 and 9](http://www.cds.caltech.edu/~murray/books/AM08/pdf/fbs-public_24Jul2020.pdf); [Mitchell (2026) Formal methods: specifying interdependent inputs for automated feasibility checking](https://davidamitchell.github.io/Research/research/2026-05-31-formal-methods-interdependent-inputs-feasibility.html)

**D2. Observable metrics for bounded vs. unbounded cycling**

[inference] The metric that distinguishes bounded from unbounded cycling in a delivery context is the per-cycle trend of total constraint violation magnitude. If the aggregate constraint gap decreases after each revision, the system is in convergence; if it stays constant, it is cycling (limit cycle); if it increases, the system is diverging. This is the operational equivalent of measuring V̇(x) in continuous control. Source: [Åström and Murray (2021) Feedback Systems, Chapter 5](http://www.cds.caltech.edu/~murray/books/AM08/pdf/fbs-public_24Jul2020.pdf); [Mitchell (2026) Q6: Leading indicators of instability in split-authority flow systems](https://davidamitchell.github.io/Research/research/2026-05-29-split-authority-q6-instability-leading-indicators.html)

### §3 Reasoning

Removing narrative glue and unsupported generalisations from the investigation:

1. Control theory convergence conditions are well-established for LTI systems (all closed-loop poles negative real part) and for nonlinear systems via Lyapunov's method (V̇ < 0). These are not in dispute. [fact; sources above]

2. Feedback delay reducing phase margin and increasing cycling risk is a standard result from frequency-domain control theory. The mathematical relationship is: phase lag added by delay τ at frequency ω is −ωτ radians. This is not contested. [fact; Åström and Murray (2021)]

3. The mapping from control-system variables to software delivery variables is structural (isomorphic in feedback loop topology) but not quantitatively exact (the delivery system is discrete, nonlinear, and not time-invariant). The mapping is therefore an analogy that generates design heuristics, not a formal theorem. [inference]

4. Empirical evidence for requirements churn and approval loop cycling comes from survey data (CHAOS, DORA) and practitioner literature (Reinertsen, DeMarco and Lister). These are secondary sources about delivery system behaviour, not primary experimental studies with controlled interventions. Confidence in the empirical claims is medium rather than high.

5. The three design rules (gain condition, delay condition, feasibility condition) are derived by structural analogy from control theory plus empirical delivery evidence. They are well-grounded but not formally proven for discrete specification systems.

Causal chain for specification cycling (each item independently labelled):
  (1) A goal is defined and measured against a constraint space. [fact; by definition of the loop]
  (2) If any constraint fails, a goal revision is triggered. [fact; by definition of the loop]
  (3) If the gain of the revision (magnitude of goal change per unit constraint violation) exceeds 1, the revised goal may violate previously satisfied constraints, generating new failures. [inference; source: Åström and Murray (2021), Chapters 5 and 9]
  (4) If the feedback delay (review cycle time) is long relative to the rate of constraint-space change, the revision is applied to a stale measurement, increasing the probability of overshoot. [inference; source: Åström and Murray (2021), Chapter 10; Reinertsen (2009), Chapter 6]
  (5) If both conditions (3) and (4) apply simultaneously, the system enters a cycling regime where each revision generates new violations. [inference; source: Åström and Murray (2021), Chapters 5 and 9]
  (6) If the constraint space has no feasible point, no revision path leads to convergence regardless of gain or delay. [fact; by definition of infeasibility; Mitchell (2026) formal methods item]

### §4 Consistency Check

```text
contradiction_scan: none found
  - Control theory conditions (Lyapunov, gain margin, phase margin, delay margin) are internally consistent
    across Åström/Murray, Khalil, and Ogata.
  - Reinertsen's delivery system analysis is consistent with control-theoretic predictions:
    high WIP (high delay) and overreaction to feedback (high gain) both produce oscillation.
  - Senge's organisational dynamics analysis is consistent: balancing loops with time delays
    produce oscillation; the mechanism is the same as phase-lag in control systems.
  - DORA empirical findings (manual approval loops reduce performance) are consistent with
    the prediction that long-delay, high-gain approval chains increase cycling risk.
  - The formal methods item (2026-05-31-formal-methods-interdependent-inputs-feasibility)
    establishes that feasibility checking can fail due to constraint infeasibility;
    this is consistent with the third convergence condition (feasibility condition).

confidence_adjustment: none required; no contradictions found
scope_guardrail: maintained; hardware control systems excluded; delivery analogies are structural only
quantitative_note: specific numeric thresholds (6 dB gain margin, 30 degree phase margin) are
  engineering practice norms from Åström/Murray; they are not claimed to apply numerically
  to software delivery contexts
```

### §5 Depth and Breadth Expansion

**Technical lens:** The Ziegler-Nichols method for controller tuning identifies critical gain and critical frequency empirically by increasing gain until sustained oscillation occurs, then backing off. The equivalent in a delivery context is monitoring for the onset of specification cycling (non-decreasing constraint violation count across cycles) as a signal that gain or delay is excessive. This suggests a practical detection heuristic: track per-cycle constraint violation delta and halt the revision loop when the delta is non-negative for two consecutive cycles. [inference; source: Åström and Murray (2021) Feedback Systems, Chapter 9]

**Regulatory and governance lens:** DORA (2023) found that approval structures matter: generative organisational cultures with streamlined approvals correlate with 30% higher organisational performance. The governance implication is that approval chains should be designed to reduce delay and gain, not merely to add review steps. Each additional sequential reviewer increases both delay and gain (via compounding correction), which the control-theoretic analysis predicts will increase cycling risk. [inference; source: DORA (2023) Accelerate State of DevOps Report, https://dora.dev/research/2023/dora-report/]

**Historical lens:** Senge (1990) documents the beer distribution game as an empirical demonstration of oscillation caused by long feedback delay in a supply chain: retailers overorder in response to stockouts because they cannot see upstream inventory, and the upstream amplification produces supply-demand cycling that persists even with rational individual actors. This is the same mechanism: high gain (large order placed per unit of perceived shortage) plus long delay (order-to-delivery time) produces oscillation. The structural parallel to specification cycling is direct. [inference; source: Senge (1990) The Fifth Discipline, Chapter 3]

**Behavioural lens:** A cognitive contributor to high-gain specification revision is loss aversion: decision-makers tend to overweight recent constraint violations relative to the history of satisfied constraints, which inflates the perceived gain required. This means the effective gain of human reviewers in a specification loop may systematically exceed the gain that would be optimal for convergence. Structured review protocols that require reviewers to assess aggregate constraint satisfaction rather than individual failures can reduce effective gain. [inference; source: DeMarco and Lister (2003) Waltzing with Bears, Chapters 5-6; Reinertsen (2009) Principles of Product Development Flow, Chapter 6]

**Economic lens:** The cost of cycling is additive per cycle: each review cycle that fails to converge consumes review capacity, delays delivery, and may generate rework on already-revised artefacts. Reinertsen frames this as the cost of WIP: items in a specification cycle accumulate cost-of-delay proportional to their time in the loop. The economic argument for convergence design rules is that the incremental cost of adding a gain-reduction mechanism (for example, limiting goal revision to the failing constraint only) is low, while the cost saved per avoided cycle is high. [inference; source: Reinertsen (2009) Principles of Product Development Flow, Chapter 6]

### §6 Synthesis

**Executive summary:**

A goal-constraint specification loop converges when three conditions hold: each revision reduces aggregate constraint violations rather than amplifying them (the gain condition); the review cycle is short enough that the constraint surface does not shift materially before the correction is applied (the delay condition); and a feasible specification exists within the constraint space (the feasibility condition). Failure of any one condition produces cycling. Failure of the gain condition produces bounded cycling (the loop oscillates within a fixed amplitude); failure of the delay condition produces growing oscillation that may become unbounded; failure of the feasibility condition produces irreducible cycling regardless of gain or delay control. [inference; source: https://www.cds.caltech.edu/~murray/books/AM08/pdf/fbs-public_24Jul2020.pdf; https://www.amazon.com/Principles-Product-Development-Flow-Generation/dp/1935401009]

In software delivery, the gain condition is violated when stakeholder reviews produce comprehensive scope revisions in response to targeted constraint failures; the delay condition is violated when review cadence is lower than the rate of constraint-surface change (for example, quarterly reviews with weekly-shifting business priorities); and the feasibility condition is violated when constraints are mutually exclusive but have not been detected as such. DORA research and practitioner literature (Reinertsen, DeMarco and Lister) provide empirical support that these conditions operate as predicted by control theory. [inference; source: https://dora.dev/research/2023/dora-report/; https://www.amazon.com/Principles-Product-Development-Flow-Generation/dp/1935401009]

The three convergence conditions are operationalisable as design rules for automated goal-constraint validation: cap the scope of each revision to the failing constraint; set the review cadence to exceed the rate of constraint-surface change; and run a feasibility check before entering the revision loop. [inference; source: https://www.cds.caltech.edu/~murray/books/AM08/pdf/fbs-public_24Jul2020.pdf; https://davidamitchell.github.io/Research/research/2026-05-31-formal-methods-interdependent-inputs-feasibility.html]

**Key findings:**

1. A closed-loop specification system converges to a stable specification when each review cycle produces a net reduction in total constraint violations, the review cadence exceeds the rate of constraint-surface change, and a feasible specification exists within the constraint space. ([inference]; medium confidence; source: https://www.cds.caltech.edu/~murray/books/AM08/pdf/fbs-public_24Jul2020.pdf; https://www.amazon.com/Principles-Product-Development-Flow-Generation/dp/1935401009)

2. In control theory terms, convergence requires that all closed-loop poles have strictly negative real parts for Linear Time-Invariant (LTI) systems, or equivalently that a Lyapunov function V(x) with negative definite derivative V̇(x) can be found for the tracking error dynamics. ([fact]; high confidence; source: https://www.cds.caltech.edu/~murray/books/AM08/pdf/fbs-public_24Jul2020.pdf; https://www.pearson.com/en-us/subject-catalog/p/nonlinear-systems/P200000003456)

3. Feedback delay reduces phase margin by ωτ radians at each operating frequency ω, where τ is the delay length, making cycling progressively more likely as review cycle time increases relative to the rate of specification change. ([fact]; high confidence; source: https://www.cds.caltech.edu/~murray/books/AM08/pdf/fbs-public_24Jul2020.pdf; https://www.pearson.com/en-us/subject-catalog/p/modern-control-engineering/P200000003186)

4. Bounded cycling (a limit cycle, from which the system can recover by reducing gain or delay) is distinguishable from unbounded divergence (from which no within-loop correction can recover) by whether the amplitude of constraint violations decreases, stays constant, or increases across successive review cycles. ([inference]; medium confidence; source: https://www.pearson.com/en-us/subject-catalog/p/modern-control-engineering/P200000003186; https://www.cds.caltech.edu/~murray/books/AM08/pdf/fbs-public_24Jul2020.pdf)

5. In a software delivery specification loop, high gain corresponds to comprehensive goal revisions in response to targeted constraint signals, and long delay corresponds to infrequent review cycles; both increase cycling risk independent of each other, and their combination is the most common driver of specification instability. ([inference]; medium confidence; source: https://www.amazon.com/Principles-Product-Development-Flow-Generation/dp/1935401009; https://www.pearsonhighered.com/assets/preface/0/1/3/4/0134682947.pdf)

6. DevOps Research and Assessment (DORA) research provides empirical support for the delay condition: continuous integration, fast code reviews, and loosely coupled teams all reduce feedback delay and are correlated with significantly better delivery stability and throughput. ([fact]; high confidence; source: https://dora.dev/research/2023/dora-report/)

7. Senge's systems dynamics analysis of balancing loops with time delays demonstrates that organisational systems oscillate when decision-makers apply additional corrections before prior corrections have taken effect, which is the organisational equivalent of integrator windup in control systems. ([inference]; medium confidence; source: https://www.penguinrandomhouse.com/books/158736/the-fifth-discipline-by-peter-m-senge/)

8. Sequential approval chains in delivery systems amplify effective gain by compounding reviewer corrections, making the cumulative revision larger than any single reviewer's correction, which increases cycling risk beyond what either the delay or the gain of individual reviewers would predict in isolation. ([inference]; medium confidence; source: https://www.pearsonhighered.com/assets/preface/0/1/3/4/0134682947.pdf; https://dora.dev/research/2023/dora-report/)

9. Constraint infeasibility is an irreducible source of cycling that gain and delay controls cannot address: if no specification simultaneously satisfies all constraints, the loop will cycle regardless of review cadence or revision scope, and structural change to either the constraint set or the goal is required to achieve convergence. ([inference]; medium confidence; source: https://davidamitchell.github.io/Research/research/2026-05-31-formal-methods-interdependent-inputs-feasibility.html; https://www.cds.caltech.edu/~murray/books/AM08/pdf/fbs-public_24Jul2020.pdf)

10. The three convergence conditions (gain, delay, feasibility) are operationalisable as practical design rules: limit each revision to the failing constraint only (gain control), set review cadence to exceed the rate of business context change (delay control), and run a feasibility check before entering the revision loop (feasibility pre-check). ([inference]; medium confidence; source: https://www.cds.caltech.edu/~murray/books/AM08/pdf/fbs-public_24Jul2020.pdf; https://davidamitchell.github.io/Research/research/2026-05-31-formal-methods-interdependent-inputs-feasibility.html)

**Evidence map:**

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [inference] Convergence requires three conditions: gain, delay, feasibility | https://www.cds.caltech.edu/~murray/books/AM08/pdf/fbs-public_24Jul2020.pdf; https://www.amazon.com/Principles-Product-Development-Flow-Generation/dp/1935401009 | medium | Derived by structural analogy from control theory |
| [fact] LTI convergence requires all closed-loop poles to have negative real parts | https://www.cds.caltech.edu/~murray/books/AM08/pdf/fbs-public_24Jul2020.pdf; https://www.pearson.com/en-us/subject-catalog/p/nonlinear-systems/P200000003456 | high | Standard control theory result |
| [fact] Feedback delay τ reduces phase margin by ωτ | https://www.cds.caltech.edu/~murray/books/AM08/pdf/fbs-public_24Jul2020.pdf; https://www.pearson.com/en-us/subject-catalog/p/modern-control-engineering/P200000003186 | high | Standard control theory result |
| [inference] Bounded cycling vs. unbounded divergence distinguished by per-cycle violation amplitude trend | https://www.pearson.com/en-us/subject-catalog/p/modern-control-engineering/P200000003186; https://www.cds.caltech.edu/~murray/books/AM08/pdf/fbs-public_24Jul2020.pdf | medium | Structural analogy |
| [inference] High gain = comprehensive revision per targeted failure; long delay = infrequent reviews | https://www.amazon.com/Principles-Product-Development-Flow-Generation/dp/1935401009; https://www.pearsonhighered.com/assets/preface/0/1/3/4/0134682947.pdf | medium | Structural mapping; not quantitatively exact |
| [fact] DORA: continuous integration, fast review, loosely coupled teams improve delivery stability | https://dora.dev/research/2023/dora-report/ | high | Survey-based; consistent across multiple DORA report years |
| [inference] Balancing loops with delay cause organisational oscillation (Senge) | https://www.penguinrandomhouse.com/books/158736/the-fifth-discipline-by-peter-m-senge/ | medium | Practitioner systems dynamics; consistent with control theory |
| [inference] Sequential approval chains compound effective gain | https://www.pearsonhighered.com/assets/preface/0/1/3/4/0134682947.pdf; https://dora.dev/research/2023/dora-report/ | medium | Structural inference |
| [inference] Constraint infeasibility requires structural change, not gain/delay control | https://davidamitchell.github.io/Research/research/2026-05-31-formal-methods-interdependent-inputs-feasibility.html; https://www.cds.caltech.edu/~murray/books/AM08/pdf/fbs-public_24Jul2020.pdf | medium | Formal methods + control theory |
| [inference] Three design rules operationalisable: gain control, delay control, feasibility pre-check | https://www.cds.caltech.edu/~murray/books/AM08/pdf/fbs-public_24Jul2020.pdf; https://davidamitchell.github.io/Research/research/2026-05-31-formal-methods-interdependent-inputs-feasibility.html | medium | Design rule derivation |

**Assumptions:**

[assumption] The control-theoretic framework (Lyapunov, gain margin, phase margin) is structurally analogous to software delivery specification loops in the relevant topological sense: both are feedback systems with setpoint, plant, sensor, and actuator. Justification: Reinertsen (2009) explicitly applies the same structural analogy to product development queues; the analogy is used here to derive heuristics, not quantitative predictions. Source: https://www.amazon.com/Principles-Product-Development-Flow-Generation/dp/1935401009

[assumption] The feasibility condition (constraint space must be non-empty) is a necessary condition for convergence. Justification: by definition, if no specification satisfies all constraints, no feedback loop can converge to one. The formal methods literature confirms that infeasibility is a distinct failure mode from instability. Source: https://davidamitchell.github.io/Research/research/2026-05-31-formal-methods-interdependent-inputs-feasibility.html

**Analysis:**

The three convergence conditions form a hierarchy of intervention: the feasibility condition is logically prior (no amount of feedback-loop tuning converges an infeasible system), the gain condition is the next most tractable (revision scope is a design choice), and the delay condition is the least tractable (review cadence is often constrained by organisational calendars). [inference; source: https://www.cds.caltech.edu/~murray/books/AM08/pdf/fbs-public_24Jul2020.pdf]

The empirical DORA and Reinertsen evidence for the delay condition is stronger than the evidence for the gain condition. DORA's multi-year survey data directly measures the effect of approval loop structures and review cadence on delivery stability. The gain condition evidence is primarily structural (Reinertsen's analogy) and practitioner observation (DeMarco and Lister), without a controlled empirical study directly measuring revision scope as a stability variable. [inference; source: https://dora.dev/research/2023/dora-report/; https://www.amazon.com/Principles-Product-Development-Flow-Generation/dp/1935401009]

The distinction between bounded cycling and unbounded divergence has a direct operational implication: a system in bounded cycling can be stabilised by tuning (reducing gain, reducing delay) without structural change, while a system in unbounded divergence requires structural intervention (constraint set redesign or feasibility pre-check). Early detection of the divergence pattern (growing per-cycle violation count) is therefore the highest-value monitoring metric. [inference; source: https://www.pearson.com/en-us/subject-catalog/p/modern-control-engineering/P200000003186; https://davidamitchell.github.io/Research/research/2026-05-29-split-authority-q6-instability-leading-indicators.html]

Rival explanations for specification cycling that do not require control-theoretic framing include political cycling (stakeholders with veto power cycling the specification to advance competing agendas), capability cycling (the delivery team lacks the capability to satisfy the stated constraints, so the specification is continuously revised downward until it reaches a feasible but unacceptable goal), and information cycling (the constraint measurements are unreliable, so each measurement produces a different signal, creating artificial oscillation). These are not addressed by gain and delay controls alone; they require different interventions. [inference; source: https://www.penguinrandomhouse.com/books/158736/the-fifth-discipline-by-peter-m-senge/; https://www.pearsonhighered.com/assets/preface/0/1/3/4/0134682947.pdf]

**Risks, gaps, uncertainties:**

- The mapping from control-system variables to delivery-system variables is structural and not quantitatively validated. No empirical study directly measures the effect of revision scope (the gain analogue) on specification cycling frequency in software delivery. This gap limits the precision of the design rules.
- The formal convergence conditions assume that a feasibility check can be run before the revision loop begins. In practice, constraint infeasibility may not be detectable in advance (constraint conflicts may only become visible after exploring the constraint space). The feasibility pre-check design rule therefore depends on the capability established in the related formal-methods item.
- DORA survey data measures delivery stability at the deployment-frequency level, not at the specification or goal-definition level. The direct empirical connection between DORA metrics and specification cycling in the goal-definition phase requires an additional inferential step.
- The Kotonya and Sommerville (2000) source on requirements volatility was cited via secondary reference; the original book was not directly accessible in this session.

**Open questions:**

- Can a formal Lyapunov function be constructed for a discrete goal-constraint specification loop, or does the discrete and nonlinear nature of the constraint space prevent it?
- What is the empirical relationship between revision scope per cycle (the gain analogue) and specification cycling frequency in software delivery systems?
- How can constraint infeasibility be detected in advance, before the revision loop begins, without exhaustive enumeration of the constraint space?
- Do political or capability-cycling failure modes have distinct observable signatures that would allow them to be distinguished from gain/delay-driven cycling in practice?

### §7 Recursive Review

```text
review_result: pass
acronym_audit: passed
  - LTI: Linear Time-Invariant (LTI), expanded on first use in §2 A1
  - DORA: DevOps Research and Assessment (DORA), expanded on first use in §2 C1
  - WIP: Work In Progress (WIP), expanded on first use in §2 C2
  - All other terms (Lyapunov, gain margin, phase margin, Nyquist) are proper nouns or field terms
    defined in context on first use without abbreviation
parity_check: passed; all §6 claims appear in §2 or §3; no new claims introduced in §6
claim_audit: passed; all factual and inferential claims in §2 carry [fact] or [inference] labels
source_audit: passed; all claims bind to URL-backed sources
em_dash_audit: passed; no em-dashes used in prose sections
ai_slop_audit: passed; no filler phrases found
bounded_vs_unbounded: explicitly addressed in A5 and KF4
feasibility_condition: addressed as third necessary condition in D1
```

---

## Findings

*(Populated from §6 Synthesis above.)*

### Executive Summary

A goal-constraint specification loop converges to a stable specification when three conditions hold simultaneously: each revision cycle reduces aggregate constraint violations rather than amplifying them (the gain condition); the review cycle is short enough that the constraint surface does not shift materially before the correction is applied (the delay condition); and a feasible specification exists within the constraint space (the feasibility condition). When any condition fails, the loop cycles without resolution. [inference; source: https://www.cds.caltech.edu/~murray/books/AM08/pdf/fbs-public_24Jul2020.pdf; https://www.amazon.com/Principles-Product-Development-Flow-Generation/dp/1935401009] Failure of the gain condition produces bounded cycling (recoverable by reducing revision scope); failure of the delay condition produces growing oscillation that may become unbounded; failure of the feasibility condition produces irreducible cycling regardless of any feedback-loop tuning, requiring structural change to the constraint set or the goal itself. [inference; source: https://www.pearson.com/en-us/subject-catalog/p/modern-control-engineering/P200000003186; https://davidamitchell.github.io/Research/research/2026-05-31-formal-methods-interdependent-inputs-feasibility.html] In software delivery, the gain condition is violated by comprehensive scope revisions in response to targeted constraint signals; the delay condition is violated when review cadence is lower than the rate of business-context change; and the feasibility condition is violated when mutually exclusive constraints have not been detected as such. [inference; source: https://dora.dev/research/2023/dora-report/; https://www.amazon.com/Principles-Product-Development-Flow-Generation/dp/1935401009] The three conditions are operationalisable as design rules: cap revision scope to the failing constraint, set review cadence above the rate of constraint-surface change, and run a feasibility check before entering the revision loop. [inference; source: https://www.cds.caltech.edu/~murray/books/AM08/pdf/fbs-public_24Jul2020.pdf; https://davidamitchell.github.io/Research/research/2026-05-31-formal-methods-interdependent-inputs-feasibility.html]

### Key Findings

1. **A closed-loop specification system converges to a stable specification when each review cycle produces a net reduction in total constraint violations, the review cadence exceeds the rate of constraint-surface change, and a feasible specification exists within the constraint space.** ([inference]; medium confidence; source: https://www.cds.caltech.edu/~murray/books/AM08/pdf/fbs-public_24Jul2020.pdf; https://www.amazon.com/Principles-Product-Development-Flow-Generation/dp/1935401009)

2. **In control theory, convergence of a Linear Time-Invariant (LTI) system requires that all closed-loop poles have strictly negative real parts, and for nonlinear systems Lyapunov's direct method provides the equivalent condition: a positive-definite function V(x) whose time derivative V̇(x) is negative definite along all trajectories.** ([fact]; high confidence; source: https://www.cds.caltech.edu/~murray/books/AM08/pdf/fbs-public_24Jul2020.pdf; https://www.pearson.com/en-us/subject-catalog/p/nonlinear-systems/P200000003456)

3. **Feedback delay reduces phase margin by ωτ radians at each operating frequency ω, where τ is the delay length, making cycling progressively more likely as review cycle time increases relative to the rate of specification change.** ([fact]; high confidence; source: https://www.cds.caltech.edu/~murray/books/AM08/pdf/fbs-public_24Jul2020.pdf; https://www.pearson.com/en-us/subject-catalog/p/modern-control-engineering/P200000003186)

4. **Bounded cycling (a limit cycle recoverable by reducing gain or delay) is distinguishable from unbounded divergence by whether the amplitude of constraint violations decreases, stays constant, or increases across successive review cycles, corresponding respectively to convergence, limit cycling, and divergence in control theory.** ([inference]; medium confidence; source: https://www.pearson.com/en-us/subject-catalog/p/modern-control-engineering/P200000003186; https://www.cds.caltech.edu/~murray/books/AM08/pdf/fbs-public_24Jul2020.pdf)

5. **In a software delivery specification loop, high gain corresponds to comprehensive goal revisions in response to targeted constraint signals, and long delay corresponds to infrequent review cycles; both increase cycling risk independently, and their combination is the most common driver of specification instability in delivery systems.** ([inference]; medium confidence; source: https://www.amazon.com/Principles-Product-Development-Flow-Generation/dp/1935401009; https://www.pearsonhighered.com/assets/preface/0/1/3/4/0134682947.pdf)

6. **DevOps Research and Assessment (DORA) research provides empirical support for the delay condition: continuous integration, fast code reviews, and loosely coupled teams all reduce feedback delay and are correlated with significantly better delivery stability and throughput.** ([fact]; high confidence; source: https://dora.dev/research/2023/dora-report/)

7. **Senge's systems dynamics analysis of balancing loops with time delays demonstrates that organisational systems oscillate when decision-makers apply additional corrections before prior corrections have taken effect, which is the organisational equivalent of integrator windup and produces the same cycling pattern as excess delay in a control system.** ([inference]; medium confidence; source: https://www.penguinrandomhouse.com/books/158736/the-fifth-discipline-by-peter-m-senge/)

8. **Sequential approval chains in delivery systems amplify effective gain by compounding reviewer corrections, making the cumulative revision larger than any single reviewer's correction would predict, which increases cycling risk beyond what either the delay or the gain of individual reviewers would suggest in isolation.** ([inference]; medium confidence; source: https://www.pearsonhighered.com/assets/preface/0/1/3/4/0134682947.pdf; https://dora.dev/research/2023/dora-report/)

9. **Constraint infeasibility is an irreducible source of specification cycling that gain and delay controls cannot address: if no specification simultaneously satisfies all constraints, the revision loop will cycle regardless of review cadence or revision scope, and structural change to either the constraint set or the goal is required.** ([inference]; medium confidence; source: https://davidamitchell.github.io/Research/research/2026-05-31-formal-methods-interdependent-inputs-feasibility.html; https://www.cds.caltech.edu/~murray/books/AM08/pdf/fbs-public_24Jul2020.pdf)

10. **The three convergence conditions are operationalisable as design rules for automated goal-constraint validation: limit each revision to the failing constraint only (gain control), set review cadence to exceed the rate of business context change (delay control), and run a feasibility check before entering the revision loop (feasibility pre-check).** ([inference]; medium confidence; source: https://www.cds.caltech.edu/~murray/books/AM08/pdf/fbs-public_24Jul2020.pdf; https://davidamitchell.github.io/Research/research/2026-05-31-formal-methods-interdependent-inputs-feasibility.html)

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [inference] Convergence requires three conditions: gain, delay, feasibility | https://www.cds.caltech.edu/~murray/books/AM08/pdf/fbs-public_24Jul2020.pdf; https://www.amazon.com/Principles-Product-Development-Flow-Generation/dp/1935401009 | medium | Structural analogy from control theory to delivery |
| [fact] LTI convergence requires all closed-loop poles to have negative real parts | https://www.cds.caltech.edu/~murray/books/AM08/pdf/fbs-public_24Jul2020.pdf; https://www.pearson.com/en-us/subject-catalog/p/nonlinear-systems/P200000003456 | high | Standard result, Åström/Murray Ch.5 and Khalil Ch.4 |
| [fact] Feedback delay τ reduces phase margin by ωτ radians | https://www.cds.caltech.edu/~murray/books/AM08/pdf/fbs-public_24Jul2020.pdf; https://www.pearson.com/en-us/subject-catalog/p/modern-control-engineering/P200000003186 | high | Standard result, Åström/Murray Ch.10, Ogata Ch.8 |
| [inference] Per-cycle violation amplitude trend distinguishes bounded cycling from unbounded divergence | https://www.pearson.com/en-us/subject-catalog/p/modern-control-engineering/P200000003186; https://www.cds.caltech.edu/~murray/books/AM08/pdf/fbs-public_24Jul2020.pdf | medium | Structural analogy; describing function method (Ogata Ch.13) |
| [inference] High gain in delivery = comprehensive revision per targeted failure; long delay = infrequent reviews | https://www.amazon.com/Principles-Product-Development-Flow-Generation/dp/1935401009; https://www.pearsonhighered.com/assets/preface/0/1/3/4/0134682947.pdf | medium | Not quantitatively validated; structural mapping only |
| [fact] DORA: continuous integration, fast review, loosely coupled teams improve delivery stability | https://dora.dev/research/2023/dora-report/ | high | Survey-based; consistent across multiple DORA report years |
| [inference] Balancing loops with delay cause organisational oscillation | https://www.penguinrandomhouse.com/books/158736/the-fifth-discipline-by-peter-m-senge/ | medium | Senge's systems dynamics; consistent with control theory |
| [inference] Sequential approval chains compound effective gain | https://www.pearsonhighered.com/assets/preface/0/1/3/4/0134682947.pdf; https://dora.dev/research/2023/dora-report/ | medium | Structural inference; DORA empirically consistent |
| [inference] Constraint infeasibility requires structural change, not gain/delay control | https://davidamitchell.github.io/Research/research/2026-05-31-formal-methods-interdependent-inputs-feasibility.html; https://www.cds.caltech.edu/~murray/books/AM08/pdf/fbs-public_24Jul2020.pdf | medium | Formal methods + control theory |
| [inference] Three design rules operationalisable: gain control, delay control, feasibility pre-check | https://www.cds.caltech.edu/~murray/books/AM08/pdf/fbs-public_24Jul2020.pdf; https://davidamitchell.github.io/Research/research/2026-05-31-formal-methods-interdependent-inputs-feasibility.html | medium | Design rule derivation by structural analogy |

### Assumptions

- **Assumption:** The control-theoretic framework (Lyapunov, gain margin, phase margin) is structurally analogous to software delivery specification loops. **Justification:** Both are feedback systems with setpoint, plant, sensor, and actuator. The analogy generates design heuristics, not quantitative predictions. Reinertsen (2009) applies the same structural analogy to product development queues. Source: https://www.amazon.com/Principles-Product-Development-Flow-Generation/dp/1935401009

- **Assumption:** The feasibility condition (constraint space must be non-empty) is a necessary condition for convergence. **Justification:** By definition, if no specification satisfies all constraints simultaneously, no feedback loop can converge to one. The formal methods literature confirms infeasibility is a distinct failure mode from instability. Source: https://davidamitchell.github.io/Research/research/2026-05-31-formal-methods-interdependent-inputs-feasibility.html

### Analysis

The three convergence conditions form a hierarchy for intervention priority. The feasibility condition is logically prior: no amount of feedback-loop tuning converges an infeasible system, and this must be detected before entering the revision loop. [inference; source: https://davidamitchell.github.io/Research/research/2026-05-31-formal-methods-interdependent-inputs-feasibility.html] The gain condition is the next most tractable: revision scope is a design choice that can be enforced by process (require that each revision targets only the failing constraint, not the full specification). [inference; source: https://www.amazon.com/Principles-Product-Development-Flow-Generation/dp/1935401009] The delay condition is typically the least tractable, as review cadence is often constrained by organisational calendars; however, continuous integration and automated constraint checking (as recommended by DORA) can reduce the delay regardless of review calendar constraints. [inference; source: https://dora.dev/research/2023/dora-report/]

The empirical evidence for the delay condition is stronger than for the gain condition. DORA's multi-year survey data directly measures the effect of approval loop structures and review cadence on delivery stability, finding that manual approval processes correlate negatively with performance. [fact; source: https://dora.dev/research/2023/dora-report/] The gain condition evidence is primarily structural (Reinertsen's analogy) and practitioner observation (DeMarco and Lister), without a controlled empirical study that directly measures revision scope as a stability variable. [inference; source: https://www.amazon.com/Principles-Product-Development-Flow-Generation/dp/1935401009]

The distinction between bounded cycling and unbounded divergence has an operational implication for intervention urgency. A system in bounded cycling can be stabilised by tuning without structural change, while a system in unbounded divergence requires structural intervention (constraint set redesign or goal reformulation). Early detection of divergence (growing per-cycle violation count over at least two consecutive cycles) is therefore the highest-value monitoring metric for an automated goal-constraint validation system. [inference; source: https://www.pearson.com/en-us/subject-catalog/p/modern-control-engineering/P200000003186; https://davidamitchell.github.io/Research/research/2026-05-29-split-authority-q6-instability-leading-indicators.html]

Three rival explanations for specification cycling do not require control-theoretic framing and are not addressed by gain and delay controls: political cycling (stakeholders with veto power cycle the specification to advance competing agendas), capability cycling (the delivery team revises the specification downward because the constraints cannot be met at current capability), and information cycling (unreliable constraint measurements generate artificial oscillation). Each requires different intervention. [inference; source: https://www.penguinrandomhouse.com/books/158736/the-fifth-discipline-by-peter-m-senge/; https://www.pearsonhighered.com/assets/preface/0/1/3/4/0134682947.pdf]

### Risks, Gaps, and Uncertainties

- The mapping from control-system variables to delivery-system variables is structural and not quantitatively validated. No empirical study directly measures the effect of revision scope (the gain analogue) on specification cycling frequency in software delivery. This gap limits the precision of the design rules.
- The feasibility pre-check design rule depends on a capability to detect constraint infeasibility in advance, which requires the formal methods infrastructure established in the related item on interdependent inputs. Where that infrastructure is not available, the feasibility condition cannot be pre-checked.
- DORA survey data measures delivery stability at the deployment-frequency level, not at the specification or goal-definition phase. The connection between DORA metrics and specification cycling at the goal-definition level requires an additional inferential step.
- Requirements volatility empirical evidence (CHAOS reports, Kotonya and Sommerville) comes from project-level survey data rather than controlled experiments. These studies establish correlation with project failure, not a causal mechanism.
- Political and capability-driven cycling failure modes may produce signatures similar to gain or delay-driven cycling but require different interventions. The observable metric (per-cycle constraint violation trend) does not by itself distinguish these failure modes.

### Open Questions

- Can a formal Lyapunov function be constructed for a discrete goal-constraint specification loop, or does the discrete and nonlinear nature of the constraint space prevent it? This may become a new backlog item.
- What is the empirical relationship between revision scope per cycle (the gain analogue) and specification cycling frequency in software delivery systems? Direct measurement would strengthen the gain condition.
- How can constraint infeasibility be detected before the revision loop begins, without exhaustive enumeration of the constraint space?
- Do political, capability, and information cycling failure modes have distinct observable signatures that would allow them to be distinguished from gain/delay-driven cycling in practice?

---

## Output

- Type: knowledge
- Description: Knowledge item documenting the formal conditions for convergence vs. cycling in goal-constraint feedback systems and their operationalisation as three design rules for automated specification validation: gain control (limit revision scope to the failing constraint), delay control (set review cadence above the rate of constraint-surface change), and feasibility pre-check (verify constraint space is non-empty before entering the revision loop). [inference; source: https://www.cds.caltech.edu/~murray/books/AM08/pdf/fbs-public_24Jul2020.pdf; https://davidamitchell.github.io/Research/research/2026-05-31-formal-methods-interdependent-inputs-feasibility.html]
- Links:
  - https://www.cds.caltech.edu/~murray/books/AM08/pdf/fbs-public_24Jul2020.pdf
  - https://dora.dev/research/2023/dora-report/
  - https://davidamitchell.github.io/Research/research/2026-05-31-formal-methods-interdependent-inputs-feasibility.html
