---
title: "Policy enforcement and formal verification as Energy-Based Model (EBM) optimization signals"
added: 2026-05-17T11:18:46+00:00
status: reviewing
priority: high
blocks: []
tags: [policy, formal-methods, verification, governance, agentic-ai]
started: 2026-05-17T19:04:41+00:00
completed: ~
output: [knowledge]
cites:
  - 2026-05-09-policy-as-code-guardrails-regulatory-ai-governance
  - 2026-05-17-layered-reasoning-state-abstraction-interfaces
  - 2026-05-17-deterministic-circuit-breakers-hybrid-reasoning-infrastructure
  - 2026-03-10-formal-spec-intent-alignment-agentic-coding
related:
  - 2026-05-09-governance-policy-determinism-vs-stochastic-llm
  - 2026-05-09-hybrid-architecture-probabilistic-llm-deterministic-governance
  - 2026-04-26-ai-agent-control-plane-architecture-enterprise
  - 2026-03-10-formal-spec-intent-alignment-agentic-coding
superseded_by: ~
supersedes: ~
item_type: primary
confidence: medium
versions: []
---

# Policy enforcement and formal verification as Energy-Based Model (EBM) optimization signals

## Research Question

How can discrete policy engines and formal verifiers be translated into continuous or structured optimization signals that guide Energy-Based Model (EBM) search while preserving the original natural-language intent of requirements?

## Scope

**In scope:**
- Continuous relaxation of binary Allow/Deny policy evaluation into distance-to-compliance metrics
- Compilation patterns from declarative policy (for example, Open Policy Agent (OPA) Rego) into energy functions
- Translation inversion risks between natural-language requirements and formalized constraints
- Semantic drift detection and two-way validation patterns
- Converting verifier/compiler failures into actionable optimization penalties or critiques

**Out of scope:**
- Full theorem proving tutorials
- Building new policy languages from scratch
- Runtime infrastructure fallback mechanics (covered in the deterministic infrastructure item)

**Constraints:** Prefer methods that can produce explainable audit trails showing how formal outcomes map back to business-policy intent.

## Context

This item tests whether policy and proof systems can shape search during candidate generation instead of acting only as a final reject gate after the model has already committed to a plan. [inference; source: https://davidamitchell.github.io/Research/research/2026-05-09-policy-as-code-guardrails-regulatory-ai-governance.html; https://davidamitchell.github.io/Research/research/2026-05-17-layered-reasoning-state-abstraction-interfaces.html; https://davidamitchell.github.io/Research/research/2026-05-17-deterministic-circuit-breakers-hybrid-reasoning-infrastructure.html]

## Approach

1. How can binary policy outcomes be transformed into distance-to-compliance signals?
   1a. Which relaxation strategies preserve policy semantics?
   1b. How should violations be weighted by risk class?
2. How can declarative policies be compiled into energy landscapes?
   2a. What mapping from rule violations to penalty terms is most tractable?
   2b. Which optimization methods handle sparse and discontinuous penalty structure best?
3. How can translation inversion be detected early?
   3a. What two-way validation checks align formal constraints with original intent?
   3b. Which test harness patterns catch wrong-but-provable encodings?
4. How should verifier failures be translated into refinement guidance?
   4a. What error ontology best supports automated remediation suggestions?
   4b. How should uncertainty be represented when proof obligations are incomplete?

## Sources

- [x] [Open Policy Agent Rego Policy Language](https://www.openpolicyagent.org/docs/latest/policy-language/)
- [x] [Open Policy Agent REST API Compile API](https://www.openpolicyagent.org/docs/latest/rest-api/#compile-api)
- [x] [Open Policy Agent Evaluating a Data Filter Policy](https://www.openpolicyagent.org/docs/filtering/partial-evaluation)
- [x] [Open Policy Agent Writing Valid Data Filtering Policies](https://www.openpolicyagent.org/docs/filtering/fragment)
- [x] [Open Policy Agent Decision Logs](https://www.openpolicyagent.org/docs/latest/management-decision-logs/)
- [x] [Lean Community Theorem Proving in Lean 4 Tactics](https://leanprover.github.io/theorem_proving_in_lean4/Tactics/)
- [x] [Lean Language Reference Reading Proof States](https://lean-lang.org/doc/reference/latest/Tactic-Proofs/Reading-Proof-States/)
- [x] [NASA Formal Requirements Elicitation Tool](https://software.nasa.gov/software/ARC-18066-1)
- [x] [NASA SW-VnV FRET User Manual](https://github.com/NASA-SW-VnV/fret/blob/master/fret-electron/docs/_media/userManual.md)
- [x] [Conrad et al. (2022) A Compositional Proof Framework for FRETish Requirements](https://arxiv.org/abs/2201.03641)
- [x] [Microsoft Z3 Guide Optimization](https://microsoft.github.io/z3guide/docs/optimization/intro/)
- [x] [Microsoft Z3 Guide Soft Constraints](https://microsoft.github.io/z3guide/docs/optimization/softconstraints/)
- [x] [Microsoft Z3 Guide Cores and Satisfying Subsets](https://microsoft.github.io/z3guide/programming/Example%20Programs/Cores%20and%20Satisfying%20Subsets/)
- [x] [Microsoft Z3 Guide Parameters](https://microsoft.github.io/z3guide/programming/Parameters/)
- [x] [Bjorner et al. (n.d.) Programming Z3](https://theory.stanford.edu/~nikolaj/programmingz3.html)
- [x] [Leofante et al. (2018) Automated Verification of Neural Networks: Advances, Challenges and Perspectives](https://arxiv.org/abs/1805.09938)
- [ ] [Open Policy Agent Documentation](https://www.openpolicyagent.org/docs/latest/) - identified parent documentation page, but narrower consulted pages above were used for extractable claims
- [ ] [The Lean Theorem Prover](https://leanprover.github.io/) - identified parent documentation page, but the consulted tactic and proof-state pages above were more specific
- [ ] [Katz et al. (2023) Formal Verification of Neural Networks: Advances and Challenges](https://arxiv.org/abs/2310.09110) - identified in the seed list, but the linked identifier resolves to an unrelated paper, so it was not used as evidence here

## Related

- [Mitchell (2026) Implementation Patterns for Regulatory Compliance in Artificial Intelligence-Driven Data Governance: Policy-as-Code, Guardrails, and Output Validation](https://davidamitchell.github.io/Research/research/2026-05-09-policy-as-code-guardrails-regulatory-ai-governance.html)
- [Mitchell (2026) Layered reasoning stack interfaces: state abstraction and Large Language Model (LLM) ↔ Energy-Based Model (EBM) protocols](https://davidamitchell.github.io/Research/research/2026-05-17-layered-reasoning-state-abstraction-interfaces.html)
- [Mitchell (2026) Deterministic circuit-breakers and real-time infrastructure constraints for hybrid reasoning stacks](https://davidamitchell.github.io/Research/research/2026-05-17-deterministic-circuit-breakers-hybrid-reasoning-infrastructure.html)
- [Mitchell (2026) Formal intent specification and language choice for AI alignment in agentic coding systems](https://davidamitchell.github.io/Research/research/2026-03-10-formal-spec-intent-alignment-agentic-coding.html)

---

## Research Skill Output

*(Full output from running the research skill, retained verbatim in the completed item. Sections 0 to 5 are the investigation, and section 6 seeds the Findings section below.)*

### §0 Initialise

- Question: determine how discrete policy engines and formal verifiers can become optimization guidance for Energy-Based Model search without losing the original business meaning of the requirement.
- Scope: distance-to-compliance signals, policy compilation into structured objectives, translation inversion detection, verifier-failure feedback, and explainable audit traces.
- Constraints: production-oriented methods only, explicit traceability from business requirement to formal rule to optimization term, and full research mode.
- Output: full sections 0 through 7 plus Findings with Executive Summary, Key Findings, Evidence Map, Assumptions, Analysis, Risks, Gaps, Uncertainties, Open Questions, and Output.
- [fact; source: https://davidamitchell.github.io/Research/research/2026-05-09-policy-as-code-guardrails-regulatory-ai-governance.html; https://davidamitchell.github.io/Research/research/2026-05-17-layered-reasoning-state-abstraction-interfaces.html; https://davidamitchell.github.io/Research/research/2026-05-17-deterministic-circuit-breakers-hybrid-reasoning-infrastructure.html] Prior completed-item cross-reference: adjacent repository work already established that governance signals need typed proposal boundaries, explicit control-plane enforcement, and fail-closed handling under deadline pressure, so this item narrows the problem to how those deterministic signals should be encoded as optimization guidance.
- [fact; source: https://software.nasa.gov/software/ARC-18066-1; https://arxiv.org/abs/2201.03641] Working definition: preserving natural-language intent means keeping a requirement reviewable across structured natural language, formal logic, and analysis views with evidence that the formalization captures the intended semantics.
- [fact; source: https://software.nasa.gov/software/ARC-18066-1; https://arxiv.org/abs/2201.03641] Working definition: translation inversion means a formal rule that remains internally valid but changes, narrows, or reverses the intended meaning of the original business requirement.
- [fact; source: https://microsoft.github.io/z3guide/docs/optimization/softconstraints/; https://theory.stanford.edu/~nikolaj/programmingz3.html] Working definition: a structured optimization signal can include hard infeasibility constraints, weighted soft penalties, and solver diagnostics such as unsatisfiable cores, rather than only a single scalar score.
- [inference; source: https://www.openpolicyagent.org/docs/filtering/partial-evaluation; https://davidamitchell.github.io/Research/research/2026-05-17-layered-reasoning-state-abstraction-interfaces.html] Working definition: canonical state means the normalized field-level representation that preserves the policy-relevant meaning of a candidate while discarding presentation-only variation.
- [fact; source: https://leanprover.github.io/theorem_proving_in_lean4/Tactics/; https://lean-lang.org/doc/reference/latest/Tactic-Proofs/Reading-Proof-States/] Working definition: verifier feedback includes explicit proof states, remaining goals, and local context that tell a repair loop what is still missing, not just a pass or fail bit.

### §1 Question Decomposition

- **Root question:** how should a system translate business requirements into formal policy and verification signals that can guide search continuously while still remaining auditable and semantically faithful?
- **A. Distance-to-compliance**
  - A1. Which parts of a policy can be relaxed into weighted penalties, and which must remain hard constraints?
  - A2. How should policy severities or risk classes be represented so penalty weights stay explainable?
- **B. Policy compilation**
  - B1. How can declarative Rego rules be compiled into residual conditions over canonical state?
  - B2. Which optimization structures best handle sparse, discontinuous, or grouped violations?
- **C. Intent preservation**
  - C1. Which intermediate representation best keeps a traceable link between natural-language clauses and formal constraints?
  - C2. Which validation checks catch a formally valid but semantically wrong encoding early?
- **D. Verifier feedback**
  - D1. Which diagnostics from theorem provers and satisfiability solvers are specific enough to drive local repair?
  - D2. How should unresolved proof obligations, timeouts, or approximate checks be represented in the search loop?

### §2 Investigation

#### 2.1 Source access and replacement notes

- [assumption; source: https://arxiv.org/abs/1805.09938] Seed identifier `2310.09110` and title string `Formal Verification of Neural Networks: Advances and Challenges` did not produce a usable matching survey in this session, so this item uses the accessible Leofante et al. review for verification trade-off evidence. Justification: the exact-versus-approximate distinction needed here is directly available in that accessible survey.
- [assumption; source: https://leanprover.github.io/theorem_proving_in_lean4/Tactics/; https://lean-lang.org/doc/reference/latest/Tactic-Proofs/Reading-Proof-States/] The seed Lean homepage was replaced with the narrower tactic and proof-state pages because those pages exposed the verifier-workflow details needed for extractable claims in this item. Justification: the parent page was not the most specific authoritative surface for this question.

#### 2.2 Prior completed-item sweep

- [fact; source: https://davidamitchell.github.io/Research/research/2026-05-09-policy-as-code-guardrails-regulatory-ai-governance.html] The policy-as-code implementation item concluded that typed proposal objects, deterministic policy engines, and explicit audit fields are stronger governance boundaries than free-form text moderation alone.
- [fact; source: https://davidamitchell.github.io/Research/research/2026-05-17-layered-reasoning-state-abstraction-interfaces.html] The layered-reasoning item concluded that an Energy-Based Model interface should score canonical state rather than raw text and should preserve only policy-relevant invariants across the boundary.
- [fact; source: https://davidamitchell.github.io/Research/research/2026-05-17-deterministic-circuit-breakers-hybrid-reasoning-infrastructure.html] The deterministic-circuit-breaker item concluded that iterative reasoning loops need explicit stop conditions, fallback states, and deadline-aware supervision instead of optimistic retries.
- [inference; source: https://davidamitchell.github.io/Research/research/2026-05-09-policy-as-code-guardrails-regulatory-ai-governance.html; https://davidamitchell.github.io/Research/research/2026-05-17-layered-reasoning-state-abstraction-interfaces.html; https://davidamitchell.github.io/Research/research/2026-05-17-deterministic-circuit-breakers-hybrid-reasoning-infrastructure.html] This item extends that prior work from interface and control placement into the narrower design question of how to turn policy and verification outcomes into optimizer-visible signals without collapsing their semantics.

#### 2.3 Turning binary policy outcomes into distance-to-compliance signals

- [fact; source: https://www.openpolicyagent.org/docs/latest/policy-language/] OPA is built for policy evaluation over structured data, Rego reasons over structured documents such as Application Programming Interface (API) requests and configuration data, and rules can define composite values rather than only booleans.
- [fact; source: https://www.openpolicyagent.org/docs/filtering/partial-evaluation; https://www.openpolicyagent.org/docs/filtering/fragment] OPA partial evaluation lets callers declare some inputs unknown, evaluates the known parts of the policy, and leaves residual conditions over the unknown fields that can later be translated into another target representation.
- [fact; source: https://microsoft.github.io/z3guide/docs/optimization/intro/; https://microsoft.github.io/z3guide/docs/optimization/softconstraints/] Z3 supports optimization objectives directly and supports weighted soft constraints, where each unsatisfied soft constraint contributes a penalty and grouped constraints can be tracked separately.
- [inference; source: https://www.openpolicyagent.org/docs/filtering/partial-evaluation; https://www.openpolicyagent.org/docs/filtering/fragment; https://microsoft.github.io/z3guide/docs/optimization/softconstraints/] The cleanest relaxation strategy is to decompose an Allow or Deny decision into named atomic obligations over canonical state, keep legally or safety-critical obligations as hard infeasible constraints, and map repairable obligations to weighted soft penalties that measure how many residual clauses remain unsatisfied.
- [inference; source: https://microsoft.github.io/z3guide/docs/optimization/softconstraints/; https://www.openpolicyagent.org/docs/latest/policy-language/; https://davidamitchell.github.io/Research/research/2026-05-09-policy-as-code-guardrails-regulatory-ai-governance.html] Risk weighting should sit in named objective families tied to policy classes or rule groups rather than in one opaque aggregate score, because grouped soft constraints and structured policy outputs keep the reason for a penalty visible to reviewers.

#### 2.4 Compiling declarative policy into structured energy terms

- [fact; source: https://www.openpolicyagent.org/docs/latest/rest-api/#compile-api] OPA's Compile API exposes partial evaluation and data-filtering functionality as an explicit integration surface.
- [fact; source: https://www.openpolicyagent.org/docs/filtering/fragment] The translatable fragment requires a clear distinction between known and unknown values and supports simple comparisons and a limited set of built-ins when policies are to be compiled into downstream query targets.
- [inference; source: https://www.openpolicyagent.org/docs/latest/rest-api/#compile-api; https://www.openpolicyagent.org/docs/filtering/partial-evaluation; https://www.openpolicyagent.org/docs/filtering/fragment] Rego should therefore be compiled by treating candidate-dependent fields as unknown, treating policy context and business facts as known, and translating each residual condition into either a hard feasibility test or a named penalty term over the canonical candidate state.
- [inference; source: https://microsoft.github.io/z3guide/docs/optimization/intro/; https://microsoft.github.io/z3guide/docs/optimization/softconstraints/; https://www.openpolicyagent.org/docs/latest/rest-api/#compile-api] Sparse and discontinuous violation structure is more tractable when optimization stays structured, for example as grouped hard and soft objectives over residual clauses, than when the system tries to force every policy distinction into one smooth surrogate score.
- [inference; source: https://davidamitchell.github.io/Research/research/2026-05-17-layered-reasoning-state-abstraction-interfaces.html; https://www.openpolicyagent.org/docs/latest/rest-api/#compile-api; https://www.openpolicyagent.org/docs/filtering/partial-evaluation] The most robust compilation target is a canonical typed envelope plus optional domain views, because the residual policy clauses need stable field names while richer graph or syntax projections may still be necessary for local repair and dependency scoring.

#### 2.5 Preserving natural-language intent and catching translation inversion

- [fact; source: https://software.nasa.gov/software/ARC-18066-1; https://github.com/NASA-SW-VnV/fret/blob/master/fret-electron/docs/_media/userManual.md] FRET lets users write hierarchical requirements in a structured natural language, assigns those requirements unambiguous semantics, and presents multiple views such as natural language, formal logics, diagrams, and analysis exports so people with different expertise can inspect the same requirement.
- [fact; source: https://arxiv.org/abs/2201.03641] Conrad et al. formalize FRET's structured requirement language, FRETish, and prove semantic equivalence between FRETish specifications and their temporal-logic counterparts generated by the tool.
- [inference; source: https://software.nasa.gov/software/ARC-18066-1; https://arxiv.org/abs/2201.03641] The safest way to preserve intent is to introduce an explicit intermediate requirement record, similar in spirit to FRETish, that links each natural-language clause to one formal rule, one canonical state field family, and one optimization or verifier term.
- [inference; source: https://github.com/NASA-SW-VnV/fret/blob/master/fret-electron/docs/_media/userManual.md; https://arxiv.org/abs/2201.03641; https://www.openpolicyagent.org/docs/latest/management-decision-logs/] Two-way validation should use side-by-side views, positive and negative exemplars, and execution traces that point back to the originating clause, because a rule can remain formally consistent while still drifting away from the business meaning that stakeholders intended.
- [inference; source: https://davidamitchell.github.io/Research/research/2026-05-09-policy-as-code-guardrails-regulatory-ai-governance.html; https://software.nasa.gov/software/ARC-18066-1; https://arxiv.org/abs/2201.03641] Wrong-but-provable encodings are most likely when policy authors jump directly from prose to enforcement logic without a reviewable intermediate representation, so the translation loop should require both clause-level traceability and executable example cases before a penalty term is trusted.

#### 2.6 Converting verifier failures into actionable refinement guidance

- [fact; source: https://leanprover.github.io/theorem_proving_in_lean4/Tactics/; https://lean-lang.org/doc/reference/latest/Tactic-Proofs/Reading-Proof-States/] Lean tactics work by transforming a proof state made of ordered goals and local assumptions, and unsolved goals remain explicit with the context needed to continue the proof.
- [fact; source: https://microsoft.github.io/z3guide/programming/Example%20Programs/Cores%20and%20Satisfying%20Subsets/; https://microsoft.github.io/z3guide/programming/Parameters/; https://theory.stanford.edu/~nikolaj/programmingz3.html] Z3 can track assumptions, extract unsatisfiable cores, and enable unsatisfiable core generation as a solver feature, which exposes a subset of constraints sufficient to explain infeasibility.
- [inference; source: https://leanprover.github.io/theorem_proving_in_lean4/Tactics/; https://lean-lang.org/doc/reference/latest/Tactic-Proofs/Reading-Proof-States/; https://microsoft.github.io/z3guide/programming/Example%20Programs/Cores%20and%20Satisfying%20Subsets/] Verifier failures should be translated into structured critiques containing the violated clause identifiers, affected state paths, remaining proof goals or unsatisfiable core members, and the smallest candidate-local edit that could discharge the failure, instead of collapsing everything into one negative energy bump.
- [inference; source: https://www.openpolicyagent.org/docs/filtering/partial-evaluation; https://microsoft.github.io/z3guide/programming/Example%20Programs/Cores%20and%20Satisfying%20Subsets/; https://davidamitchell.github.io/Research/research/2026-05-17-layered-reasoning-state-abstraction-interfaces.html] Local repair should target only the residual clauses or state regions named by the diagnostic, because preserving already-satisfied structure reduces churn and makes the audit trail easier to interpret.

#### 2.7 Representing uncertainty, approximation, and unresolved proof obligations

- [fact; source: https://arxiv.org/abs/1805.09938] Leofante et al. distinguish exact verification methods, which provide exact guarantees but scale poorly, from relaxation-based or approximate methods, which scale better but can be conservative.
- [inference; source: https://arxiv.org/abs/1805.09938; https://microsoft.github.io/z3guide/docs/optimization/softconstraints/; https://davidamitchell.github.io/Research/research/2026-05-17-deterministic-circuit-breakers-hybrid-reasoning-infrastructure.html] Search loops should represent at least three verifier statuses, namely hard failure, unresolved or approximate result, and discharged obligation, because unresolved proof work should neither disappear into zero penalty nor be treated as equivalent to a proven violation.
- [inference; source: https://arxiv.org/abs/1805.09938; https://lean-lang.org/doc/reference/latest/Tactic-Proofs/Reading-Proof-States/; https://davidamitchell.github.io/Research/research/2026-05-17-deterministic-circuit-breakers-hybrid-reasoning-infrastructure.html] For policy-critical actions, unresolved obligations caused by timeout, unsupported fragment, or approximate bound should escalate to fail-closed fallback or human review rather than remain in the optimization loop indefinitely.

#### 2.8 Audit trails that reconnect formal outcomes to business intent

- [fact; source: https://www.openpolicyagent.org/docs/latest/management-decision-logs/] OPA decision logs record policy path, input, result, bundle revision, decision identifier, trace identifier, span identifier, timestamp, and masked or erased fields for auditing and offline debugging.
- [fact; source: https://github.com/NASA-SW-VnV/fret/blob/master/fret-electron/docs/_media/userManual.md; https://software.nasa.gov/software/ARC-18066-1] FRET keeps multiple requirement representations and exports them to analysis tools, which creates a traceable path from requirement wording to formal artifact.
- [inference; source: https://www.openpolicyagent.org/docs/latest/management-decision-logs/; https://software.nasa.gov/software/ARC-18066-1; https://davidamitchell.github.io/Research/research/2026-05-09-policy-as-code-guardrails-regulatory-ai-governance.html] An explainable audit trail for policy-guided search therefore needs one correlated record that binds business clause identifier, formal rule revision, canonical state snapshot, violated path or proof goal, penalty family, and suggested repair, so reviewers can see why the system preferred one repair over another.

### §3 Reasoning

- [fact; source: https://www.openpolicyagent.org/docs/filtering/partial-evaluation; https://microsoft.github.io/z3guide/docs/optimization/softconstraints/] The direct technical bridge between discrete policy and optimization is not a continuous relaxation of whole-policy text, but a decomposition of policy into residual clause checks that can become hard or soft structured objectives.
- [fact; source: https://software.nasa.gov/software/ARC-18066-1; https://arxiv.org/abs/2201.03641] The evidence on intent preservation points toward a controlled intermediate representation with explicit semantic links rather than direct prose-to-penalty compilation.
- [fact; source: https://leanprover.github.io/theorem_proving_in_lean4/Tactics/; https://microsoft.github.io/z3guide/programming/Example%20Programs/Cores%20and%20Satisfying%20Subsets/] The evidence on verifier feedback points toward localized diagnostics, because proof states and unsatisfiable cores already identify which obligations remain or conflict.
- [inference; source: https://www.openpolicyagent.org/docs/filtering/partial-evaluation; https://microsoft.github.io/z3guide/docs/optimization/softconstraints/; https://arxiv.org/abs/1805.09938] The strongest design is therefore a hybrid objective stack: hard constraints for non-negotiable obligations, weighted soft penalties for repairable deviations, and explicit unknown or timeout states for unresolved proof work.
- [assumption; source: https://www.openpolicyagent.org/docs/latest/management-decision-logs/; https://github.com/NASA-SW-VnV/fret/blob/master/fret-electron/docs/_media/userManual.md] Production orchestrators can persist clause-level trace links and candidate-local repair records for each iteration. Justification: without that persistence, the proposed audit and refinement loop becomes an opaque retry cycle rather than a governable control surface.

### §4 Consistency Check

- [fact; source: https://www.openpolicyagent.org/docs/filtering/partial-evaluation; https://microsoft.github.io/z3guide/docs/optimization/softconstraints/] The consulted policy-compilation and optimization sources are consistent about representation shape: both work over structured clauses and weighted obligations rather than over free-form narrative text.
- [fact; source: https://software.nasa.gov/software/ARC-18066-1; https://arxiv.org/abs/2201.03641] The consulted intent-preservation sources are consistent that structured natural language plus formal semantics is preferable to uncontrolled prose when the downstream artifact must remain reviewable and analyzable.
- [fact; source: https://leanprover.github.io/theorem_proving_in_lean4/Tactics/; https://lean-lang.org/doc/reference/latest/Tactic-Proofs/Reading-Proof-States/; https://microsoft.github.io/z3guide/programming/Example%20Programs/Cores%20and%20Satisfying%20Subsets/] The consulted verifier sources are also consistent that failure information is structured, context-bearing, and actionable at the level of specific goals or constraint subsets.
- [inference; source: https://arxiv.org/abs/1805.09938; https://davidamitchell.github.io/Research/research/2026-05-17-deterministic-circuit-breakers-hybrid-reasoning-infrastructure.html] The main tension is between using approximate checks for scalable guidance and requiring exact evidence for high-impact decisions, so the proposed design keeps approximation in the advisory layer and reserves hard gating for exact or policy-critical obligations.

### §5 Depth and Breadth Expansion

- [inference; source: https://www.openpolicyagent.org/docs/latest/rest-api/#compile-api; https://microsoft.github.io/z3guide/docs/optimization/intro/] Technical lens: compile-time separation between known policy context and unknown candidate state makes policy-to-objective translation more stable than scoring candidates against raw prompt text on each iteration.
- [inference; source: https://software.nasa.gov/software/ARC-18066-1; https://github.com/NASA-SW-VnV/fret/blob/master/fret-electron/docs/_media/userManual.md] Behavioural lens: reviewers are more likely to catch semantic drift when they can inspect the same requirement as business language, formal logic, and analysis artifact instead of being asked to trust a hidden compiler.
- [inference; source: https://www.openpolicyagent.org/docs/latest/management-decision-logs/; https://davidamitchell.github.io/Research/research/2026-05-09-policy-as-code-guardrails-regulatory-ai-governance.html] Governance lens: structured penalty families let organizations explain which policy domain drove a repair or escalation, which is stronger for audit and challenge rights than a raw "score went down" explanation.
- [inference; source: https://arxiv.org/abs/1805.09938; https://davidamitchell.github.io/Research/research/2026-05-17-deterministic-circuit-breakers-hybrid-reasoning-infrastructure.html] Operational lens: unresolved proof work is a queue-management and fallback problem as much as a logic problem, because search quality becomes irrelevant once the system can no longer satisfy its execution deadline safely.
- [inference; source: https://microsoft.github.io/z3guide/programming/Example%20Programs/Cores%20and%20Satisfying%20Subsets/; https://lean-lang.org/doc/reference/latest/Tactic-Proofs/Reading-Proof-States/] Economic lens: localized repair guidance should reduce recomputation cost relative to full regeneration whenever only a small subset of obligations has failed.

### §6 Synthesis

**Executive summary:**
Policy and formal-verification signals should guide Energy-Based Model search through a two-tier objective stack in which non-negotiable obligations remain hard feasibility constraints and repairable obligations become named weighted penalties over canonical state. [inference; source: https://www.openpolicyagent.org/docs/filtering/partial-evaluation; https://microsoft.github.io/z3guide/docs/optimization/softconstraints/; https://davidamitchell.github.io/Research/research/2026-05-17-layered-reasoning-state-abstraction-interfaces.html]

Rego policies are well-suited to this translation because OPA can partially evaluate policies against known context and emit residual conditions over unknown candidate fields, which can then become hard or soft objective terms rather than opaque final-stage booleans. [inference; source: https://www.openpolicyagent.org/docs/latest/rest-api/#compile-api; https://www.openpolicyagent.org/docs/filtering/partial-evaluation; https://www.openpolicyagent.org/docs/filtering/fragment]

Natural-language intent is best preserved by an intermediate requirement representation, similar to FRETish, that keeps clause-level semantic links between business wording, formal rules, canonical state fields, and resulting penalties or verifier diagnostics. [inference; source: https://software.nasa.gov/software/ARC-18066-1; https://arxiv.org/abs/2201.03641]

Verifier outputs should enter the loop as structured repair guidance, such as unsatisfiable cores, remaining proof goals, affected state paths, and explicit unknown states for unresolved obligations, with fail-closed escalation when policy-critical proof work cannot be discharged in time. [inference; source: https://microsoft.github.io/z3guide/programming/Example%20Programs/Cores%20and%20Satisfying%20Subsets/; https://lean-lang.org/doc/reference/latest/Tactic-Proofs/Reading-Proof-States/; https://arxiv.org/abs/1805.09938; https://davidamitchell.github.io/Research/research/2026-05-17-deterministic-circuit-breakers-hybrid-reasoning-infrastructure.html]

**Key findings:**

1. **The most reliable translation keeps legally or safety-critical obligations as hard constraints while mapping repairable policy clauses to named weighted penalties, because Z3-style soft constraints support graded infeasibility without blurring the obligations that must never be traded away.** ([inference]; medium confidence; source: https://microsoft.github.io/z3guide/docs/optimization/intro/; https://microsoft.github.io/z3guide/docs/optimization/softconstraints/; https://davidamitchell.github.io/Research/research/2026-05-09-policy-as-code-guardrails-regulatory-ai-governance.html)
2. **OPA partial evaluation provides a practical compilation mechanism for policy-guided search because it specializes Rego against known business context and leaves residual conditions over unknown candidate fields that can be re-used as structured objective terms.** ([inference]; medium confidence; source: https://www.openpolicyagent.org/docs/latest/rest-api/#compile-api; https://www.openpolicyagent.org/docs/filtering/partial-evaluation; https://www.openpolicyagent.org/docs/filtering/fragment)
3. **A canonical state boundary is necessary because policy compilation and optimization both depend on stable field-level semantics, while adjacent repository work shows that scoring raw text directly leaves too much variance and too little traceability for governance use.** ([inference]; medium confidence; source: https://www.openpolicyagent.org/docs/filtering/partial-evaluation; https://davidamitchell.github.io/Research/research/2026-05-17-layered-reasoning-state-abstraction-interfaces.html; https://davidamitchell.github.io/Research/research/2026-05-09-policy-as-code-guardrails-regulatory-ai-governance.html)
4. **Intent preservation is strongest when each business clause is linked through an intermediate structured requirement record to one formal rule family and one optimization term family, because FRET's multiple representations and semantic-equivalence proofs make translation drift easier to detect.** ([inference]; high confidence; source: https://software.nasa.gov/software/ARC-18066-1; https://github.com/NASA-SW-VnV/fret/blob/master/fret-electron/docs/_media/userManual.md; https://arxiv.org/abs/2201.03641; https://davidamitchell.github.io/Research/research/2026-03-10-formal-spec-intent-alignment-agentic-coding.html)
5. **Wrong-but-provable encodings are best caught with two-way validation harnesses that combine side-by-side requirement views, executable positive and negative examples, and policy decision traces, because formal consistency alone does not guarantee business-semantic fidelity.** ([inference]; medium confidence; source: https://github.com/NASA-SW-VnV/fret/blob/master/fret-electron/docs/_media/userManual.md; https://arxiv.org/abs/2201.03641; https://www.openpolicyagent.org/docs/latest/management-decision-logs/; https://davidamitchell.github.io/Research/research/2026-03-10-formal-spec-intent-alignment-agentic-coding.html)
6. **Verifier failures should be converted into localized repair artifacts, such as unsatisfiable cores, remaining proof goals, and affected state paths, because those diagnostics expose the smallest conflicting obligation set more directly than a single negative reward number can.** ([inference]; high confidence; source: https://microsoft.github.io/z3guide/programming/Example%20Programs/Cores%20and%20Satisfying%20Subsets/; https://microsoft.github.io/z3guide/programming/Parameters/; https://theory.stanford.edu/~nikolaj/programmingz3.html; https://lean-lang.org/doc/reference/latest/Tactic-Proofs/Reading-Proof-States/)
7. **Approximate or relaxation-based verification results should guide ranking and repair but should not silently authorize policy-critical actions, because the verification literature distinguishes exact guarantees from scalable but conservative approximations.** ([inference]; medium confidence; source: https://arxiv.org/abs/1805.09938; https://davidamitchell.github.io/Research/research/2026-05-17-deterministic-circuit-breakers-hybrid-reasoning-infrastructure.html)
8. **Unresolved proof obligations, timeouts, and unsupported fragments need an explicit unknown or escalation status instead of a soft pass, because a search loop cannot treat incomplete formal evidence as equivalent to either compliance or violation.** ([inference]; medium confidence; source: https://leanprover.github.io/theorem_proving_in_lean4/Tactics/; https://lean-lang.org/doc/reference/latest/Tactic-Proofs/Reading-Proof-States/; https://arxiv.org/abs/1805.09938; https://davidamitchell.github.io/Research/research/2026-05-17-deterministic-circuit-breakers-hybrid-reasoning-infrastructure.html)
9. **Explainable audit trails require one correlated record that ties business clause identifier, formal rule revision, canonical state snapshot, violated path or proof goal, penalty family, and final action, because OPA decision logs and FRET requirement views solve different parts of the traceability problem and need to be joined.** ([inference]; high confidence; source: https://www.openpolicyagent.org/docs/latest/management-decision-logs/; https://software.nasa.gov/software/ARC-18066-1; https://github.com/NASA-SW-VnV/fret/blob/master/fret-electron/docs/_media/userManual.md)

**Evidence map:**

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [inference] Hard obligations should stay infeasible while repairable ones become weighted penalties. | https://microsoft.github.io/z3guide/docs/optimization/intro/; https://microsoft.github.io/z3guide/docs/optimization/softconstraints/; https://davidamitchell.github.io/Research/research/2026-05-09-policy-as-code-guardrails-regulatory-ai-governance.html | Medium | Hard versus soft tiering |
| [inference] OPA partial evaluation provides a practical compilation path because it emits residual conditions over unknown fields that can be reused as structured objective terms. | https://www.openpolicyagent.org/docs/latest/rest-api/#compile-api; https://www.openpolicyagent.org/docs/filtering/partial-evaluation; https://www.openpolicyagent.org/docs/filtering/fragment | Medium | Documented residual-condition path supports the design inference |
| [inference] Canonical state is the right scoring boundary for governed search. | https://www.openpolicyagent.org/docs/filtering/partial-evaluation; https://davidamitchell.github.io/Research/research/2026-05-17-layered-reasoning-state-abstraction-interfaces.html; https://davidamitchell.github.io/Research/research/2026-05-09-policy-as-code-guardrails-regulatory-ai-governance.html | Medium | Cross-item synthesis |
| [inference] An intermediate requirement record modeled on FRET best preserves intent across translation layers. | https://software.nasa.gov/software/ARC-18066-1; https://github.com/NASA-SW-VnV/fret/blob/master/fret-electron/docs/_media/userManual.md; https://arxiv.org/abs/2201.03641; https://davidamitchell.github.io/Research/research/2026-03-10-formal-spec-intent-alignment-agentic-coding.html | High | Multiple representations plus semantic equivalence plus adjacent intent-alignment synthesis |
| [inference] Two-way validation with examples and traces catches formally valid but semantically wrong encodings. | https://github.com/NASA-SW-VnV/fret/blob/master/fret-electron/docs/_media/userManual.md; https://arxiv.org/abs/2201.03641; https://www.openpolicyagent.org/docs/latest/management-decision-logs/; https://davidamitchell.github.io/Research/research/2026-03-10-formal-spec-intent-alignment-agentic-coding.html | Medium | Validation harness design plus adjacent intent-mismatch synthesis |
| [inference] Unsatisfiable cores and remaining proof goals should drive localized repair suggestions. | https://microsoft.github.io/z3guide/programming/Example%20Programs/Cores%20and%20Satisfying%20Subsets/; https://microsoft.github.io/z3guide/programming/Parameters/; https://theory.stanford.edu/~nikolaj/programmingz3.html; https://lean-lang.org/doc/reference/latest/Tactic-Proofs/Reading-Proof-States/ | High | Diagnostic specificity |
| [inference] Approximate verification can guide ranking but should not silently authorize policy-critical action. | https://arxiv.org/abs/1805.09938; https://davidamitchell.github.io/Research/research/2026-05-17-deterministic-circuit-breakers-hybrid-reasoning-infrastructure.html | Medium | Exact versus approximate split |
| [inference] Timeouts and unresolved obligations need explicit unknown or escalation status. | https://leanprover.github.io/theorem_proving_in_lean4/Tactics/; https://lean-lang.org/doc/reference/latest/Tactic-Proofs/Reading-Proof-States/; https://arxiv.org/abs/1805.09938; https://davidamitchell.github.io/Research/research/2026-05-17-deterministic-circuit-breakers-hybrid-reasoning-infrastructure.html | Medium | No silent pass |
| [inference] Auditability requires one trace that reconnects clause, rule revision, diagnostics, penalty, and action. | https://www.openpolicyagent.org/docs/latest/management-decision-logs/; https://software.nasa.gov/software/ARC-18066-1; https://github.com/NASA-SW-VnV/fret/blob/master/fret-electron/docs/_media/userManual.md | High | Joined requirement-to-decision trace |

**Assumptions:**

- [assumption; source: https://www.openpolicyagent.org/docs/latest/management-decision-logs/; https://github.com/NASA-SW-VnV/fret/blob/master/fret-electron/docs/_media/userManual.md] The orchestration layer can persist clause identifiers, canonical state snapshots, and repair diagnostics per iteration. Justification: without stored trace links, the proposed audit model cannot be implemented.
- [assumption; source: https://microsoft.github.io/z3guide/docs/optimization/softconstraints/; https://www.openpolicyagent.org/docs/filtering/partial-evaluation] The search loop can accept structured objective families and local patch proposals instead of only a single scalar loss. Justification: hard and soft clause structure is central to the recommended translation.

**Analysis:**

The evidence favors clause-level compilation over direct prose scoring because OPA already separates known context from unknown candidate state and because structured optimization tools already separate hard and soft obligations. [inference; source: https://www.openpolicyagent.org/docs/filtering/partial-evaluation; https://microsoft.github.io/z3guide/docs/optimization/softconstraints/]

The main design trade-off is between preserving exact formal meaning and keeping the search loop computationally useful. A system that keeps every obligation hard will often become brittle or non-progressing, while a system that softens everything loses the distinction between unacceptable and repairable deviations. [inference; source: https://microsoft.github.io/z3guide/docs/optimization/softconstraints/; https://arxiv.org/abs/1805.09938]

Semantic anchoring through structured requirement representations similar to FRET resolves the most serious translation risk because it provides a reviewable path from business prose to formal clause, whereas direct natural-language-to-penalty compilers leave too few checkpoints for human review. [inference; source: https://software.nasa.gov/software/ARC-18066-1; https://arxiv.org/abs/2201.03641; https://davidamitchell.github.io/Research/research/2026-03-10-formal-spec-intent-alignment-agentic-coding.html]

Lean proof states and Z3 unsatisfiable cores matter because they already expose repair-relevant structure. A loop that ignores that structure and consumes only pass or fail outcomes throws away the most valuable part of the verifier signal. [inference; source: https://lean-lang.org/doc/reference/latest/Tactic-Proofs/Reading-Proof-States/; https://microsoft.github.io/z3guide/programming/Example%20Programs/Cores%20and%20Satisfying%20Subsets/]

The rival design, keeping policy engines and provers as pure final gates, is simpler to implement and avoids mixing search with governance logic. It is weaker when the goal is guided repair, because the model learns only that a candidate was rejected, not which obligation family should change next. [inference; source: https://www.openpolicyagent.org/docs/filtering/partial-evaluation; https://davidamitchell.github.io/Research/research/2026-05-09-policy-as-code-guardrails-regulatory-ai-governance.html]

**Risks, gaps, uncertainties:**

- Public documentation is strong on policy compilation, solver objectives, and verifier diagnostics, but weak on end-to-end production case studies that combine Large Language Model generation, Energy-Based Model search, and formal proof systems in one deployed control path. [inference; source: https://www.openpolicyagent.org/docs/filtering/partial-evaluation; https://microsoft.github.io/z3guide/docs/optimization/intro/; https://arxiv.org/abs/1805.09938]
- The recommended intermediate representation borrows heavily from structured requirement representations similar to FRET, but no consulted source proves that one representation fits every policy domain or every proof system. [inference; source: https://software.nasa.gov/software/ARC-18066-1; https://arxiv.org/abs/2201.03641]
- The evidence base supports grouped hard and soft objectives well, but it does not specify one canonical weighting scheme for business risk classes; organizations will still need governance decisions about weight assignment. [inference; source: https://microsoft.github.io/z3guide/docs/optimization/softconstraints/; https://www.openpolicyagent.org/docs/latest/management-decision-logs/]
- Recent architecture-specific advances beyond the accessible 2018 verification survey may be underrepresented in the exact-versus-approximate trade-off discussion here. [inference; source: https://arxiv.org/abs/1805.09938]

**Open questions:**

- Which canonical state schema works best for mixed code, workflow, and natural-language candidates when one candidate spans several artifact types?
- Which mutation or adversarial test suites are most effective for detecting translation inversion between prose policy and formal clauses?
- Which human-review interfaces best present unsatisfied clause sets and proof-state diagnostics without overwhelming policy owners?
- When approximate verification remains unresolved, what escalation threshold best separates safe retry from mandatory human review?

### §7 Recursive Review

- Review result: pass
- Acronym audit: pass for EBM, OPA, API, LLM, and FRETish terms
- Claim audit: pass
- Cross-item audit: pass
- Residual uncertainty: end-to-end production evidence for a full Large Language Model plus EBM plus prover loop remains indirect

---

## Findings

### Executive Summary

Policy and formal-verification signals should guide Energy-Based Model search through a two-tier objective stack in which non-negotiable obligations remain hard feasibility constraints and repairable obligations become named weighted penalties over canonical state. [inference; source: https://www.openpolicyagent.org/docs/filtering/partial-evaluation; https://microsoft.github.io/z3guide/docs/optimization/softconstraints/; https://davidamitchell.github.io/Research/research/2026-05-17-layered-reasoning-state-abstraction-interfaces.html]

Rego policies are well-suited to this translation because OPA can partially evaluate policies against known context and emit residual conditions over unknown candidate fields, which can then become hard or soft objective terms rather than opaque final-stage booleans. [inference; source: https://www.openpolicyagent.org/docs/latest/rest-api/#compile-api; https://www.openpolicyagent.org/docs/filtering/partial-evaluation; https://www.openpolicyagent.org/docs/filtering/fragment]

Natural-language intent is best preserved by an intermediate requirement representation, similar to FRETish, that keeps clause-level semantic links between business wording, formal rules, canonical state fields, and resulting penalties or verifier diagnostics. [inference; source: https://software.nasa.gov/software/ARC-18066-1; https://arxiv.org/abs/2201.03641]

Verifier outputs should enter the loop as structured repair guidance, such as unsatisfiable cores, remaining proof goals, affected state paths, and explicit unknown states for unresolved obligations, with fail-closed escalation when policy-critical proof work cannot be discharged in time. [inference; source: https://microsoft.github.io/z3guide/programming/Example%20Programs/Cores%20and%20Satisfying%20Subsets/; https://lean-lang.org/doc/reference/latest/Tactic-Proofs/Reading-Proof-States/; https://arxiv.org/abs/1805.09938; https://davidamitchell.github.io/Research/research/2026-05-17-deterministic-circuit-breakers-hybrid-reasoning-infrastructure.html]

### Key Findings

1. **The most reliable translation keeps legally or safety-critical obligations as hard constraints while mapping repairable policy clauses to named weighted penalties, because Z3-style soft constraints support graded infeasibility without blurring the obligations that must never be traded away.** ([inference]; medium confidence; source: https://microsoft.github.io/z3guide/docs/optimization/intro/; https://microsoft.github.io/z3guide/docs/optimization/softconstraints/; https://davidamitchell.github.io/Research/research/2026-05-09-policy-as-code-guardrails-regulatory-ai-governance.html)
2. **OPA partial evaluation provides a practical compilation mechanism for policy-guided search because it specializes Rego against known business context and leaves residual conditions over unknown candidate fields that can be re-used as structured objective terms.** ([inference]; medium confidence; source: https://www.openpolicyagent.org/docs/latest/rest-api/#compile-api; https://www.openpolicyagent.org/docs/filtering/partial-evaluation; https://www.openpolicyagent.org/docs/filtering/fragment)
3. **A canonical state boundary is necessary because policy compilation and optimization both depend on stable field-level semantics, while adjacent repository work shows that scoring raw text directly leaves too much variance and too little traceability for governance use.** ([inference]; medium confidence; source: https://www.openpolicyagent.org/docs/filtering/partial-evaluation; https://davidamitchell.github.io/Research/research/2026-05-17-layered-reasoning-state-abstraction-interfaces.html; https://davidamitchell.github.io/Research/research/2026-05-09-policy-as-code-guardrails-regulatory-ai-governance.html)
4. **Intent preservation is strongest when each business clause is linked through an intermediate structured requirement record to one formal rule family and one optimization term family, because FRET's multiple representations and semantic-equivalence proofs make translation drift easier to detect.** ([inference]; high confidence; source: https://software.nasa.gov/software/ARC-18066-1; https://github.com/NASA-SW-VnV/fret/blob/master/fret-electron/docs/_media/userManual.md; https://arxiv.org/abs/2201.03641; https://davidamitchell.github.io/Research/research/2026-03-10-formal-spec-intent-alignment-agentic-coding.html)
5. **Wrong-but-provable encodings are best caught with two-way validation harnesses that combine side-by-side requirement views, executable positive and negative examples, and policy decision traces, because formal consistency alone does not guarantee business-semantic fidelity.** ([inference]; medium confidence; source: https://github.com/NASA-SW-VnV/fret/blob/master/fret-electron/docs/_media/userManual.md; https://arxiv.org/abs/2201.03641; https://www.openpolicyagent.org/docs/latest/management-decision-logs/; https://davidamitchell.github.io/Research/research/2026-03-10-formal-spec-intent-alignment-agentic-coding.html)
6. **Verifier failures should be converted into localized repair artifacts, such as unsatisfiable cores, remaining proof goals, and affected state paths, because those diagnostics expose the smallest conflicting obligation set more directly than a single negative reward number can.** ([inference]; high confidence; source: https://microsoft.github.io/z3guide/programming/Example%20Programs/Cores%20and%20Satisfying%20Subsets/; https://microsoft.github.io/z3guide/programming/Parameters/; https://theory.stanford.edu/~nikolaj/programmingz3.html; https://lean-lang.org/doc/reference/latest/Tactic-Proofs/Reading-Proof-States/)
7. **Approximate or relaxation-based verification results should guide ranking and repair but should not silently authorize policy-critical actions, because the verification literature distinguishes exact guarantees from scalable but conservative approximations.** ([inference]; medium confidence; source: https://arxiv.org/abs/1805.09938; https://davidamitchell.github.io/Research/research/2026-05-17-deterministic-circuit-breakers-hybrid-reasoning-infrastructure.html)
8. **Unresolved proof obligations, timeouts, and unsupported fragments need an explicit unknown or escalation status instead of a soft pass, because a search loop cannot treat incomplete formal evidence as equivalent to either compliance or violation.** ([inference]; medium confidence; source: https://leanprover.github.io/theorem_proving_in_lean4/Tactics/; https://lean-lang.org/doc/reference/latest/Tactic-Proofs/Reading-Proof-States/; https://arxiv.org/abs/1805.09938; https://davidamitchell.github.io/Research/research/2026-05-17-deterministic-circuit-breakers-hybrid-reasoning-infrastructure.html)
9. **Explainable audit trails require one correlated record that ties business clause identifier, formal rule revision, canonical state snapshot, violated path or proof goal, penalty family, and final action, because OPA decision logs and FRET requirement views solve different parts of the traceability problem and need to be joined.** ([inference]; high confidence; source: https://www.openpolicyagent.org/docs/latest/management-decision-logs/; https://software.nasa.gov/software/ARC-18066-1; https://github.com/NASA-SW-VnV/fret/blob/master/fret-electron/docs/_media/userManual.md)

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [inference] Hard obligations should stay infeasible while repairable ones become weighted penalties. | https://microsoft.github.io/z3guide/docs/optimization/intro/; https://microsoft.github.io/z3guide/docs/optimization/softconstraints/; https://davidamitchell.github.io/Research/research/2026-05-09-policy-as-code-guardrails-regulatory-ai-governance.html | Medium | Hard versus soft tiering |
| [inference] OPA partial evaluation provides a practical compilation path because it emits residual conditions over unknown fields that can be reused as structured objective terms. | https://www.openpolicyagent.org/docs/latest/rest-api/#compile-api; https://www.openpolicyagent.org/docs/filtering/partial-evaluation; https://www.openpolicyagent.org/docs/filtering/fragment | Medium | Documented residual-condition path supports the design inference |
| [inference] Canonical state is the right scoring boundary for governed search. | https://www.openpolicyagent.org/docs/filtering/partial-evaluation; https://davidamitchell.github.io/Research/research/2026-05-17-layered-reasoning-state-abstraction-interfaces.html; https://davidamitchell.github.io/Research/research/2026-05-09-policy-as-code-guardrails-regulatory-ai-governance.html | Medium | Cross-item synthesis |
| [inference] An intermediate requirement record modeled on FRET best preserves intent across translation layers. | https://software.nasa.gov/software/ARC-18066-1; https://github.com/NASA-SW-VnV/fret/blob/master/fret-electron/docs/_media/userManual.md; https://arxiv.org/abs/2201.03641; https://davidamitchell.github.io/Research/research/2026-03-10-formal-spec-intent-alignment-agentic-coding.html | High | Multiple representations plus semantic equivalence plus adjacent intent-alignment synthesis |
| [inference] Two-way validation with examples and traces catches formally valid but semantically wrong encodings. | https://github.com/NASA-SW-VnV/fret/blob/master/fret-electron/docs/_media/userManual.md; https://arxiv.org/abs/2201.03641; https://www.openpolicyagent.org/docs/latest/management-decision-logs/; https://davidamitchell.github.io/Research/research/2026-03-10-formal-spec-intent-alignment-agentic-coding.html | Medium | Validation harness design plus adjacent intent-mismatch synthesis |
| [inference] Unsatisfiable cores and remaining proof goals should drive localized repair suggestions. | https://microsoft.github.io/z3guide/programming/Example%20Programs/Cores%20and%20Satisfying%20Subsets/; https://microsoft.github.io/z3guide/programming/Parameters/; https://theory.stanford.edu/~nikolaj/programmingz3.html; https://lean-lang.org/doc/reference/latest/Tactic-Proofs/Reading-Proof-States/ | High | Diagnostic specificity |
| [inference] Approximate verification can guide ranking but should not silently authorize policy-critical action. | https://arxiv.org/abs/1805.09938; https://davidamitchell.github.io/Research/research/2026-05-17-deterministic-circuit-breakers-hybrid-reasoning-infrastructure.html | Medium | Exact versus approximate split |
| [inference] Timeouts and unresolved obligations need explicit unknown or escalation status. | https://leanprover.github.io/theorem_proving_in_lean4/Tactics/; https://lean-lang.org/doc/reference/latest/Tactic-Proofs/Reading-Proof-States/; https://arxiv.org/abs/1805.09938; https://davidamitchell.github.io/Research/research/2026-05-17-deterministic-circuit-breakers-hybrid-reasoning-infrastructure.html | Medium | No silent pass |
| [inference] Auditability requires one trace that reconnects clause, rule revision, diagnostics, penalty, and action. | https://www.openpolicyagent.org/docs/latest/management-decision-logs/; https://software.nasa.gov/software/ARC-18066-1; https://github.com/NASA-SW-VnV/fret/blob/master/fret-electron/docs/_media/userManual.md | High | Joined requirement-to-decision trace |

### Assumptions

- [assumption; source: https://www.openpolicyagent.org/docs/latest/management-decision-logs/; https://github.com/NASA-SW-VnV/fret/blob/master/fret-electron/docs/_media/userManual.md] The orchestration layer can persist clause identifiers, canonical state snapshots, and repair diagnostics per iteration. Justification: without stored trace links, the proposed audit model cannot be implemented.
- [assumption; source: https://microsoft.github.io/z3guide/docs/optimization/softconstraints/; https://www.openpolicyagent.org/docs/filtering/partial-evaluation] The search loop can accept structured objective families and local patch proposals instead of only a single scalar loss. Justification: hard and soft clause structure is central to the recommended translation.

### Analysis

The evidence favors clause-level compilation over direct prose scoring because OPA already separates known context from unknown candidate state and because structured optimization tools already separate hard and soft obligations. [inference; source: https://www.openpolicyagent.org/docs/filtering/partial-evaluation; https://microsoft.github.io/z3guide/docs/optimization/softconstraints/]

The main design trade-off is between preserving exact formal meaning and keeping the search loop computationally useful. A system that keeps every obligation hard will often become brittle or non-progressing, while a system that softens everything loses the distinction between unacceptable and repairable deviations. [inference; source: https://microsoft.github.io/z3guide/docs/optimization/softconstraints/; https://arxiv.org/abs/1805.09938]

Semantic anchoring through structured requirement representations similar to FRET resolves the most serious translation risk because it provides a reviewable path from business prose to formal clause, whereas direct natural-language-to-penalty compilers leave too few checkpoints for human review. [inference; source: https://software.nasa.gov/software/ARC-18066-1; https://arxiv.org/abs/2201.03641; https://davidamitchell.github.io/Research/research/2026-03-10-formal-spec-intent-alignment-agentic-coding.html]

Lean proof states and Z3 unsatisfiable cores matter because they already expose repair-relevant structure. A loop that ignores that structure and consumes only pass or fail outcomes throws away the most valuable part of the verifier signal. [inference; source: https://lean-lang.org/doc/reference/latest/Tactic-Proofs/Reading-Proof-States/; https://microsoft.github.io/z3guide/programming/Example%20Programs/Cores%20and%20Satisfying%20Subsets/]

The rival design, keeping policy engines and provers as pure final gates, is simpler to implement and avoids mixing search with governance logic. It is weaker when the goal is guided repair, because the model learns only that a candidate was rejected, not which obligation family should change next. [inference; source: https://www.openpolicyagent.org/docs/filtering/partial-evaluation; https://davidamitchell.github.io/Research/research/2026-05-09-policy-as-code-guardrails-regulatory-ai-governance.html]

### Risks, Gaps, and Uncertainties

- Public documentation is strong on policy compilation, solver objectives, and verifier diagnostics, but weak on end-to-end production case studies that combine Large Language Model generation, Energy-Based Model search, and formal proof systems in one deployed control path. [inference; source: https://www.openpolicyagent.org/docs/filtering/partial-evaluation; https://microsoft.github.io/z3guide/docs/optimization/intro/; https://arxiv.org/abs/1805.09938]
- The recommended intermediate representation borrows heavily from structured requirement representations similar to FRET, but no consulted source proves that one representation fits every policy domain or every proof system. [inference; source: https://software.nasa.gov/software/ARC-18066-1; https://arxiv.org/abs/2201.03641]
- The evidence base supports grouped hard and soft objectives well, but it does not specify one canonical weighting scheme for business risk classes; organizations will still need governance decisions about weight assignment. [inference; source: https://microsoft.github.io/z3guide/docs/optimization/softconstraints/; https://www.openpolicyagent.org/docs/latest/management-decision-logs/]
- Recent architecture-specific advances beyond the accessible 2018 verification survey may be underrepresented in the exact-versus-approximate trade-off discussion here. [inference; source: https://arxiv.org/abs/1805.09938]

### Open Questions

- Which canonical state schema works best for mixed code, workflow, and natural-language candidates when one candidate spans several artifact types?
- Which mutation or adversarial test suites are most effective for detecting translation inversion between prose policy and formal clauses?
- Which human-review interfaces best present unsatisfied clause sets and proof-state diagnostics without overwhelming policy owners?
- When approximate verification remains unresolved, what escalation threshold best separates safe retry from mandatory human review?

---

## Output

- Type: knowledge
- Description: A design synthesis for turning policy and proof outcomes into auditable search guidance, centered on hard and soft clause decomposition, semantic anchoring through structured requirement representations similar to FRET, and structured verifier diagnostics. [inference; source: https://www.openpolicyagent.org/docs/filtering/partial-evaluation; https://arxiv.org/abs/2201.03641; https://microsoft.github.io/z3guide/programming/Example%20Programs/Cores%20and%20Satisfying%20Subsets/]
- Links:
  - https://www.openpolicyagent.org/docs/filtering/partial-evaluation
  - https://arxiv.org/abs/2201.03641
  - https://microsoft.github.io/z3guide/programming/Example%20Programs/Cores%20and%20Satisfying%20Subsets/
