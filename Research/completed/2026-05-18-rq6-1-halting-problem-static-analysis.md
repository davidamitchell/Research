---
review_count: 1
title: "RQ 6.1: The Halting Problem and Rice's Theorem, the Absolute Boundary of Static Analysis for Coded Systems"
added: 2026-05-18T19:40:00+00:00
status: completed
priority: high
blocks:
  - 2026-05-18-rq6-2-state-explosion-chaos-theory
tags: [formal-methods, epistemology, philosophy-of-science]
themes: [security-risk, ai-architecture, formal-verification, computational-theory]
started: 2026-05-19T20:31:03+00:00
completed: 2026-05-19T20:53:17+00:00
output: [knowledge]
cites:
  - 2026-05-18-rq1-1-popper-falsifiability
  - 2026-05-18-rq2-4-causal-hierarchy-formal-limits
related:
  - 2026-05-18-rq1-3-instrumentalism-failure-modes
  - 2026-05-18-rq2-2-duhem-quine-underdetermination
superseded_by: ~
supersedes: ~
item_type: primary
confidence: medium
versions:
  - version: "1.0"
    sha: "6c8408720ab35ce4d6a94cee8d1280fb9d02e7ba"
    changed: 2026-05-19
    progress: "progress/2026-05-19-rq6-1-halting-problem-static-analysis.md"
    summary: "Initial completion"
---

# RQ 6.1: The Halting Problem and Rice's Theorem, the Absolute Boundary of Static Analysis for Coded Systems

## Research Question

How do the Halting Problem (Turing) and Rice's Theorem formalise the absolute boundary of static analysis, proving that it is mathematically impossible to write a general algorithm to verify whether an arbitrary coded system possesses specific non-trivial semantic properties?

## Scope

**In scope:**
- Turing's Halting Problem proof and its implications for static verification of program behaviour
- Rice's Theorem: all non-trivial semantic properties of programs are undecidable
- Godel's First Incompleteness Theorem as a broader parallel about formal limits
- Practical implications: what static analysis tools, linters, type checkers, model checkers, and deductive verifiers can actually prove, and what they cannot
- Connection to Phase 1's framework on limits of knowledge

**Out of scope:**
- Implementation details of specific static analysis tools
- Decidable subclasses such as bounded model checking for one concrete toolchain or one restricted language

**Constraints:** This item runs in parallel with Phases 2 to 4, branches off Phase 1, and feeds into the Phase 5 comparison. It must connect the computability results to the broader question of what can be known about a system from its formal description alone.

## Context

Research Question 2.4 showed that observational data generically cannot determine interventional or counterfactual claims, establishing a formal limit on what can be inferred from one evidence layer alone. [fact; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq2-4-causal-hierarchy-formal-limits.md]

This item asks for the coded-system analogue: whether source descriptions alone can support a general decision procedure for semantic properties such as termination or behavioural equivalence. [inference; source: https://builds.openlogicproject.org/content/turing-machines/undecidability/halting-problem.pdf; https://theory.stanford.edu/~trevisan/cs154-12/noterice.pdf]

Research Question 1.1 argued that stronger theories rule out more possibilities; Rice's Theorem applies the same boundary-setting question to software analysis by showing which semantic verdicts no universal analyser can deliver. [inference; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq1-1-popper-falsifiability.md; https://theory.stanford.edu/~trevisan/cs154-12/noterice.pdf]

## Approach

1. Present the Halting Problem formally: no Turing machine can decide, for all program-input pairs, whether the program halts.
2. Derive Rice's Theorem from the Halting Problem: any non-trivial semantic property of a program is undecidable.
3. Use Godel's First Incompleteness Theorem as a parallel about formal limits on proof.
4. Map the boundary: what properties can be statically verified, and which ones require restriction, abstraction, or approximation?
5. Connect the result to Phase 1 by treating undecidability as a theorem-level limit on what can be known about coded systems from their description alone.

## Sources

- [ ] [Turing (1936) On Computable Numbers, with an Application to the Entscheidungsproblem](https://doi.org/10.1112/plms/s2-42.1.230)
- [ ] [Rice (1953) Classes of Recursively Enumerable Sets and Their Decision Problems](https://doi.org/10.2307/1990888)
- [x] [Godel (1931) Uber formal unentscheidbare Satze der Principia Mathematica und verwandter Systeme](https://doi.org/10.1007/BF01700692)
- [ ] [Sipser (2012) Introduction to the Theory of Computation](https://www.cengage.com/c/introduction-to-the-theory-of-computation-3e-sipser/9781133187790/)
- [x] [Ben-David (2021) Undecidability and the Halting Problem](https://cs.uwaterloo.ca/~s4bendav/files/CS360S21Lec16.pdf)
- [x] [Open Logic Project (2026) The Halting Problem](https://builds.openlogicproject.org/content/turing-machines/undecidability/halting-problem.pdf)
- [x] [Trevisan and Williams (2012) Notes on Rice's Theorem](https://theory.stanford.edu/~trevisan/cs154-12/noterice.pdf)
- [x] [Cousot and Cousot (1977) Abstract interpretation: a unified lattice model for static analysis of programs by construction or approximation of fixpoints](https://www.di.ens.fr/~cousot/COUSOTpapers/POPL77.shtml)
- [x] [Cousot (2008) Abstract Interpretation](https://www.di.ens.fr/~cousot/AI/)
- [x] [Solar-Lezama (2025) A brief introduction to constraint-based verification and synthesis](https://people.csail.mit.edu/asolar/SynthesisCourse/Lecture18.htm)
- [x] [Schultz (2025) Model Checking notes](https://will62794.github.io/my-notes/notes/Model_Checking/Model_Checking.html)
- [x] [Stanford Encyclopedia of Philosophy (2025) Godel's incompleteness theorems](https://plato.stanford.edu/entries/goedel-incompleteness/)
- [x] [Research repo (2026-05-19) Research Question 1.1: Formalising Popper's falsifiability as a criterion between mechanism and interpolation](https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq1-1-popper-falsifiability.md)
- [x] [Research repo (2026-05-19) Research Question 2.4: Pearl's Causal Hierarchy and the formal limits of observational data for intervention and counterfactual reasoning](https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq2-4-causal-hierarchy-formal-limits.md)

---

## Research Skill Output

### §0 Initialise

- Question: How do the Halting Problem and Rice's Theorem set a theorem-level limit on static analysis of arbitrary coded systems?
- Scope: halting undecidability, Rice's Theorem, the Godel parallel, abstract interpretation, deductive verification, and model checking under restriction.
- Constraints: full mode, web-linked citations only, canonical tags only, and explicit linkage to prior completed repository items where they materially qualify the conclusion.
- Output: executive summary, key findings, evidence map, assumptions, analysis, risks, gaps, uncertainties, open questions, and an output section.
- Prior completed items consulted: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq1-1-popper-falsifiability.md ; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq2-4-causal-hierarchy-formal-limits.md ; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq1-3-instrumentalism-failure-modes.md ; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq2-2-duhem-quine-underdetermination.md

### §1 Question Decomposition

1. Halting boundary
   1.1 What does the Halting Problem state for arbitrary program-input pairs?
   1.2 Why does diagonalisation rule out a universal exact termination decider?
2. Rice boundary
   2.1 What counts as a non-trivial semantic property of a program?
   2.2 How does Rice's Theorem generalise the halting result beyond termination?
3. Practical verification consequences
   3.1 What kind of static claims remain decidable when the problem is restricted?
   3.2 How do abstract interpretation and deductive verification respond to undecidability?
   3.3 Why does model checking become tractable only on finite-state or otherwise bounded abstractions?
4. Philosophical parallel
   4.1 What does Godel's First Incompleteness Theorem say about formal proof systems?
   4.2 In what sense is that theorem parallel to, but not identical with, Turing and Rice?
5. Cross-item synthesis
   5.1 How does this coded-system boundary relate to Research Question 1.1 on falsifiability?
   5.2 How does it relate to Research Question 2.4 on the Causal Hierarchy's non-collapse?

### §2 Investigation

#### Identified but not consulted

- [ ] [Turing (1936) On Computable Numbers, with an Application to the Entscheidungsproblem](https://doi.org/10.1112/plms/s2-42.1.230)
- [ ] [Rice (1953) Classes of Recursively Enumerable Sets and Their Decision Problems](https://doi.org/10.2307/1990888)
- [ ] [Sipser (2012) Introduction to the Theory of Computation](https://www.cengage.com/c/introduction-to-the-theory-of-computation-3e-sipser/9781133187790/)

#### A. The Halting Problem

- [fact] The Open Logic Project defines the halting function as the function that returns `1` when machine `M_e` halts on input `n` and `0` otherwise, and then proves that this function is not Turing-computable. [source: https://builds.openlogicproject.org/content/turing-machines/undecidability/halting-problem.pdf]
- [fact] The Waterloo lecture defines the halting problem language `H_TM` as the set of encoded machine-input pairs where the machine halts on that input, and states that this language is undecidable. [source: https://cs.uwaterloo.ca/~s4bendav/files/CS360S21Lec16.pdf]
- [fact] The same lecture notes attribute the first proof of this undecidability result to Alan Turing in 1936 and derive the contradiction by diagonalisation over a putative decider. [source: https://cs.uwaterloo.ca/~s4bendav/files/CS360S21Lec16.pdf]
- [inference] A universal static analyser that exactly answered termination for every arbitrary program-input pair would compute the halting function, so the halting theorem directly rules such an analyser out. [source: https://builds.openlogicproject.org/content/turing-machines/undecidability/halting-problem.pdf; https://cs.uwaterloo.ca/~s4bendav/files/CS360S21Lec16.pdf]

#### B. Rice's Theorem

- [fact] Trevisan and Williams state Rice's Theorem as follows: for any set of languages `C`, the language of Turing-machine descriptions whose recognised language lies in `C` is either empty, universal, or undecidable. [source: https://theory.stanford.edu/~trevisan/cs154-12/noterice.pdf]
- [fact] The same notes explicitly interpret the theorem as showing that every non-trivial property of the language recognised by a Turing machine is undecidable. [source: https://theory.stanford.edu/~trevisan/cs154-12/noterice.pdf]
- [fact] Their examples include properties such as recognising a regular language, accepting finitely many inputs, or accepting only prime numbers, all of which remain undecidable because they are semantic rather than trivial syntactic properties. [source: https://theory.stanford.edu/~trevisan/cs154-12/noterice.pdf]
- [inference] Rice's Theorem generalises the halting barrier from one semantic property, termination on one input, to the entire class of non-trivial semantic verdicts about arbitrary programs. [source: https://theory.stanford.edu/~trevisan/cs154-12/noterice.pdf; https://builds.openlogicproject.org/content/turing-machines/undecidability/halting-problem.pdf]

#### C. The Godel parallel

- [fact] The Stanford Encyclopedia of Philosophy states that in any consistent formal system capable of expressing enough arithmetic, there are statements that can neither be proved nor disproved within that system. [source: https://plato.stanford.edu/entries/goedel-incompleteness/]
- [fact] The same entry emphasises that Godel's first theorem is about derivability within a formal system, not about an absolute notion of truth detached from any system. [source: https://plato.stanford.edu/entries/goedel-incompleteness/]
- [fact] The text returned from Godel's 1931 paper includes his own discussion of an "unentscheidbaren Satz", an undecidable sentence, as a metamathematically constructed statement. [source: https://doi.org/10.1007/BF01700692]
- [inference] Godel, Turing, and Rice therefore describe parallel boundaries on formal knowledge, but the boundary object differs: Godel limits internal proof in axiomatic systems, whereas Turing and Rice limit algorithmic decision about program semantics. [source: https://plato.stanford.edu/entries/goedel-incompleteness/; https://doi.org/10.1007/BF01700692; https://theory.stanford.edu/~trevisan/cs154-12/noterice.pdf]

#### D. Why practical static analysis uses abstraction or restriction

- [fact] The 1977 Cousot and Cousot summary defines abstract interpretation as analysing actual program executions through an abstract universe that yields information about those executions. [source: https://www.di.ens.fr/~cousot/COUSOTpapers/POPL77.shtml]
- [fact] That summary states that the resulting execution summaries are typically simpler to obtain but inaccurate, and that despite incomplete results, abstract interpretation still answers questions that tolerate imprecise answers, including partial correctness proofs that ignore termination, type checking, and optimisation feasibility checks. [source: https://www.di.ens.fr/~cousot/COUSOTpapers/POPL77.shtml]
- [fact] Cousot's later overview states that abstractions should preferably be sound, meaning conclusions drawn from the abstract semantics are not wrong relative to the concrete semantics, while unsound abstractions such as debugging and bounded model checking can miss behaviours because parts of executions are left out. [source: https://www.di.ens.fr/~cousot/AI/]
- [inference] Practical static analysis survives undecidability by replacing exact universal semantics with sound over-approximation, unsound but useful under-approximation, or both, rather than by defeating Turing or Rice. [source: https://www.di.ens.fr/~cousot/COUSOTpapers/POPL77.shtml; https://www.di.ens.fr/~cousot/AI/; https://theory.stanford.edu/~trevisan/cs154-12/noterice.pdf]

#### E. Deductive verification and model checking

- [fact] Solar-Lezama's lecture notes define a Hoare triple, written `{A} cmd {B}`, as a partial-correctness assertion that guarantees the postcondition only if the program terminates, while total correctness additionally requires termination. [source: https://people.csail.mit.edu/asolar/SynthesisCourse/Lecture18.htm]
- [fact] The same notes define the weakest precondition as the least precondition that makes a Hoare triple valid for a target postcondition, and state that it can be computed algorithmically for loop-free programs but not in general for programs with loops. [source: https://people.csail.mit.edu/asolar/SynthesisCourse/Lecture18.htm]
- [fact] Schultz's model-checking notes describe model checking as verifying whether a finite-state transition model satisfies a temporal-logic specification. [source: https://will62794.github.io/my-notes/notes/Model_Checking/Model_Checking.html]
- [fact] The same notes state that there is a linear-time algorithm for Computation Tree Logic (CTL) model checking in the size of the finite-state model and the formula, and an algorithm for Linear Temporal Logic (LTL) model checking that is linear in the model size and exponential in formula length. [source: https://will62794.github.io/my-notes/notes/Model_Checking/Model_Checking.html]
- [inference] Deductive verification and model checking therefore do not refute undecidability; they work by narrowing the question to proof obligations with supplied invariants or to finite-state abstractions where algorithmic checking becomes possible. [source: https://people.csail.mit.edu/asolar/SynthesisCourse/Lecture18.htm; https://will62794.github.io/my-notes/notes/Model_Checking/Model_Checking.html; https://www.di.ens.fr/~cousot/AI/]

#### F. Cross-item integration

- [fact] Research Question 1.1 concluded that stronger scientific theories have greater empirical content because they forbid more possible states of affairs and expose themselves to more severe tests. [source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq1-1-popper-falsifiability.md]
- [fact] Research Question 2.4 concluded that lower-layer observational evidence does not generically determine higher-layer intervention or counterfactual answers. [source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq2-4-causal-hierarchy-formal-limits.md]
- [inference] Rice's Theorem is the coded-system counterpart to those earlier boundaries, because it shows that source descriptions do not generically determine arbitrary semantic truths about an unrestricted program. [source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq1-1-popper-falsifiability.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq2-4-causal-hierarchy-formal-limits.md; https://theory.stanford.edu/~trevisan/cs154-12/noterice.pdf]

### §3 Reasoning

- [fact] The halting result rules out a universal exact termination decider for arbitrary programs, while Rice's Theorem extends that impossibility to all non-trivial semantic properties. [source: https://builds.openlogicproject.org/content/turing-machines/undecidability/halting-problem.pdf; https://theory.stanford.edu/~trevisan/cs154-12/noterice.pdf]
- [inference] Any claim that a static analyser is both general-purpose and exact must therefore be false unless "general-purpose" or "exact" has been quietly narrowed. [source: https://theory.stanford.edu/~trevisan/cs154-12/noterice.pdf; https://www.di.ens.fr/~cousot/COUSOTpapers/POPL77.shtml]
- [fact] The abstract-interpretation literature and the verification notes both describe useful analyses that remain possible once the target property, the semantic domain, or the program model is restricted. [source: https://www.di.ens.fr/~cousot/COUSOTpapers/POPL77.shtml; https://www.di.ens.fr/~cousot/AI/; https://people.csail.mit.edu/asolar/SynthesisCourse/Lecture18.htm; https://will62794.github.io/my-notes/notes/Model_Checking/Model_Checking.html]
- [inference] The practical lesson is not that verification is futile, but that trustworthy verification must declare its abstraction boundary explicitly because undecidability sits outside any particular tool implementation. [source: https://www.di.ens.fr/~cousot/AI/; https://people.csail.mit.edu/asolar/SynthesisCourse/Lecture18.htm; https://will62794.github.io/my-notes/notes/Model_Checking/Model_Checking.html]

### §4 Consistency Check

- [fact] Tension: model checking proves rich temporal properties algorithmically. [source: https://will62794.github.io/my-notes/notes/Model_Checking/Model_Checking.html]
- [inference] Resolution: the tractability result assumes a finite-state transition system, so it is a success under restriction rather than a counterexample to Rice's universal boundary. [source: https://will62794.github.io/my-notes/notes/Model_Checking/Model_Checking.html; https://theory.stanford.edu/~trevisan/cs154-12/noterice.pdf]
- [fact] Tension: abstract interpretation and Hoare-style verification still prove useful properties of real programs. [source: https://www.di.ens.fr/~cousot/COUSOTpapers/POPL77.shtml; https://people.csail.mit.edu/asolar/SynthesisCourse/Lecture18.htm]
- [inference] Resolution: those methods rely on abstraction, supplied invariants, restricted domains, or partial-correctness objectives, so they are compatible with undecidability rather than exceptions to it. [source: https://www.di.ens.fr/~cousot/AI/; https://people.csail.mit.edu/asolar/SynthesisCourse/Lecture18.htm]
- [fact] Tension: Godel's theorem concerns proof, not program execution. [source: https://plato.stanford.edu/entries/goedel-incompleteness/]
- [inference] Resolution: the comparison is a disciplined analogy about formal limits on knowability, not a claim that Godel's theorem logically entails Rice's Theorem. [source: https://plato.stanford.edu/entries/goedel-incompleteness/; https://doi.org/10.1007/BF01700692; https://theory.stanford.edu/~trevisan/cs154-12/noterice.pdf]

### §5 Depth and Breadth Expansion

- [fact] Historical lens: Godel's 1931 incompleteness result predates Turing's 1936 undecidability result, and together they shifted formal-limits arguments from engineering failure claims to theorem-level impossibility statements. [source: https://doi.org/10.1007/BF01700692; https://plato.stanford.edu/entries/goedel-incompleteness/; https://cs.uwaterloo.ca/~s4bendav/files/CS360S21Lec16.pdf]
- [fact] Technical lens: the impossibility theorems attach to unrestricted semantic universality, while model checking, abstract interpretation, and deductive verification regain traction by changing the state space, the property class, or the proof obligations. [source: https://theory.stanford.edu/~trevisan/cs154-12/noterice.pdf; https://www.di.ens.fr/~cousot/AI/; https://people.csail.mit.edu/asolar/SynthesisCourse/Lecture18.htm; https://will62794.github.io/my-notes/notes/Model_Checking/Model_Checking.html]
- [inference] Engineering lens: strong claims about software assurance are only as strong as the restrictions that make them decidable or the approximations that keep them sound. [source: https://www.di.ens.fr/~cousot/AI/; https://www.di.ens.fr/~cousot/COUSOTpapers/POPL77.shtml; https://people.csail.mit.edu/asolar/SynthesisCourse/Lecture18.htm]
- [inference] Epistemic lens: this mirrors the repository's earlier formal-boundary items by showing that coded systems, like causal and scientific models, have a non-removable gap between full semantic truth and what one evidence layer can certify. [source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq1-1-popper-falsifiability.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq2-4-causal-hierarchy-formal-limits.md; https://theory.stanford.edu/~trevisan/cs154-12/noterice.pdf]

### §6 Synthesis

**Executive summary:**

No general algorithm can decide whether arbitrary programs halt or whether they have any other non-trivial semantic property, so universal exact static verification of unrestricted coded systems is mathematically impossible. [fact; source: https://builds.openlogicproject.org/content/turing-machines/undecidability/halting-problem.pdf; https://theory.stanford.edu/~trevisan/cs154-12/noterice.pdf]

Practical verification works only by restriction or approximation: finite-state model checking makes decidable checks over reduced models, while abstract interpretation and deductive verification trade completeness for sound abstractions or for proof obligations that require extra structure. [inference; source: https://will62794.github.io/my-notes/notes/Model_Checking/Model_Checking.html; https://www.di.ens.fr/~cousot/COUSOTpapers/POPL77.shtml; https://www.di.ens.fr/~cousot/AI/; https://people.csail.mit.edu/asolar/SynthesisCourse/Lecture18.htm]

Godel's First Incompleteness Theorem is a valid parallel rather than the same result, because it marks an internal proof boundary in arithmetic while Turing and Rice mark an algorithmic decision boundary for program semantics. [inference; source: https://plato.stanford.edu/entries/goedel-incompleteness/; https://doi.org/10.1007/BF01700692; https://theory.stanford.edu/~trevisan/cs154-12/noterice.pdf]

Relative to earlier repository items, Rice's Theorem plays for coded systems the role that Popperian falsifiability and the Causal Hierarchy play for scientific and causal models: it states a hard limit on what one representational layer can certify by itself. [inference; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq1-1-popper-falsifiability.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq2-4-causal-hierarchy-formal-limits.md; https://theory.stanford.edu/~trevisan/cs154-12/noterice.pdf]

**Key findings:**

1. The halting problem proves that no general procedure can decide, for every arbitrary program and input pair, whether execution halts, so exact universal termination checking is impossible in the unrestricted case. ([fact]; medium confidence; source: https://builds.openlogicproject.org/content/turing-machines/undecidability/halting-problem.pdf; https://cs.uwaterloo.ca/~s4bendav/files/CS360S21Lec16.pdf)
2. Rice's Theorem extends this impossibility from termination to every non-trivial semantic property of a program, which means the barrier is about meaning and behaviour rather than one special verification question. ([fact]; medium confidence; source: https://theory.stanford.edu/~trevisan/cs154-12/noterice.pdf)
3. A static analyser for arbitrary general-purpose programs written in languages expressive enough to simulate general computation cannot be both universal and exact about semantic behaviour, because such a tool would decide a class of questions that Turing and Rice prove undecidable. ([inference]; medium confidence; source: https://builds.openlogicproject.org/content/turing-machines/undecidability/halting-problem.pdf; https://theory.stanford.edu/~trevisan/cs154-12/noterice.pdf; https://www.di.ens.fr/~cousot/COUSOTpapers/POPL77.shtml)
4. Abstract interpretation provides a systematic response to undecidability by analysing concrete executions through abstractions that aim to remain sound while tolerating inaccuracy about concrete behaviour. ([fact]; medium confidence; source: https://www.di.ens.fr/~cousot/COUSOTpapers/POPL77.shtml; https://www.di.ens.fr/~cousot/AI/)
5. Deductive verification hits the same boundary for looping programs, because total-correctness proofs require invariants and termination arguments that are not computable automatically in full generality. ([fact]; medium confidence; source: https://people.csail.mit.edu/asolar/SynthesisCourse/Lecture18.htm)
6. Model checking regains decidability only after the system has been reduced to a finite-state transition model or another bounded abstraction, making algorithmic temporal-logic checking possible on that narrowed domain. ([fact]; low confidence; source: https://will62794.github.io/my-notes/notes/Model_Checking/Model_Checking.html)
7. Godel's first incompleteness theorem is a disciplined parallel, not a substitute proof, because it limits what a formal arithmetic system can prove while Turing and Rice limit what software analysis can decide. ([inference]; medium confidence; source: https://plato.stanford.edu/entries/goedel-incompleteness/; https://doi.org/10.1007/BF01700692; https://theory.stanford.edu/~trevisan/cs154-12/noterice.pdf)
8. This theorem family gives coded systems the same kind of hard epistemic boundary that earlier repository items found for scientific demarcation and causal inference, namely that one formal layer does not generically settle every deeper semantic truth. ([inference]; medium confidence; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq1-1-popper-falsifiability.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq2-4-causal-hierarchy-formal-limits.md; https://theory.stanford.edu/~trevisan/cs154-12/noterice.pdf)

**Evidence map:**

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [fact] No universal exact halting decider exists for arbitrary program-input pairs. | https://builds.openlogicproject.org/content/turing-machines/undecidability/halting-problem.pdf ; https://cs.uwaterloo.ca/~s4bendav/files/CS360S21Lec16.pdf | medium | diagonalisation result |
| [fact] Every non-trivial semantic property of a Turing machine's recognised language is undecidable. | https://theory.stanford.edu/~trevisan/cs154-12/noterice.pdf | medium | semantic-property theorem |
| [inference] Universal exact static analysis of unrestricted coded systems is impossible. | https://builds.openlogicproject.org/content/turing-machines/undecidability/halting-problem.pdf ; https://theory.stanford.edu/~trevisan/cs154-12/noterice.pdf ; https://www.di.ens.fr/~cousot/COUSOTpapers/POPL77.shtml | medium | halting plus Rice |
| [fact] Abstract interpretation responds to undecidability through sound but inexact abstraction over program semantics. | https://www.di.ens.fr/~cousot/COUSOTpapers/POPL77.shtml ; https://www.di.ens.fr/~cousot/AI/ | medium | approximation trade-off |
| [fact] Hoare-style and weakest-precondition verification need extra structure for loops and total correctness. | https://people.csail.mit.edu/asolar/SynthesisCourse/Lecture18.htm | medium | invariants and ranking functions |
| [fact] Model checking is algorithmic on finite-state transition systems and bounded temporal-logic problems. | https://will62794.github.io/my-notes/notes/Model_Checking/Model_Checking.html | low | decidability under restriction |
| [inference] Godel's theorem is an epistemic parallel but not the same undecidability theorem. | https://plato.stanford.edu/entries/goedel-incompleteness/ ; https://doi.org/10.1007/BF01700692 ; https://theory.stanford.edu/~trevisan/cs154-12/noterice.pdf | medium | proof boundary versus decision boundary |
| [inference] Rice's boundary is the coded-system analogue of earlier repository limits on scientific and causal inference. | https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq1-1-popper-falsifiability.md ; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq2-4-causal-hierarchy-formal-limits.md ; https://theory.stanford.edu/~trevisan/cs154-12/noterice.pdf | medium | cross-item synthesis |

**Assumptions:**

- [assumption] "General algorithm" in this item means one procedure over arbitrary general-purpose programs rather than over a restricted language or bounded abstraction, because the impossibility theorems target unrestricted universality. [source: https://builds.openlogicproject.org/content/turing-machines/undecidability/halting-problem.pdf; https://theory.stanford.edu/~trevisan/cs154-12/noterice.pdf; https://will62794.github.io/my-notes/notes/Model_Checking/Model_Checking.html]
- [assumption] "Static analysis" here includes abstract interpretation, deductive verification, and model checking insofar as each reasons about program behaviour without executing the target program on the target input of interest. [source: https://www.di.ens.fr/~cousot/AI/; https://people.csail.mit.edu/asolar/SynthesisCourse/Lecture18.htm; https://will62794.github.io/my-notes/notes/Model_Checking/Model_Checking.html]
- [assumption] The comparison to Popper and the Causal Hierarchy is a synthesis claim about formal limits on inferability, not an assertion that these theorems are mathematically reducible to one another. [source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq1-1-popper-falsifiability.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq2-4-causal-hierarchy-formal-limits.md; https://plato.stanford.edu/entries/goedel-incompleteness/]

**Analysis:**

The strongest part of the evidence base is the boundary from halting undecidability to Rice's general semantic theorem, because the two results align directly on unrestricted program semantics even though this item accessed Rice through authoritative lecture notes rather than the original journal article. [inference; source: https://builds.openlogicproject.org/content/turing-machines/undecidability/halting-problem.pdf; https://theory.stanford.edu/~trevisan/cs154-12/noterice.pdf]

A plausible rival interpretation is that modern verification tools already prove many deep properties and therefore weaken the theorem-level conclusion, but the Cousot, Solar-Lezama, and model-checking sources all show that those successes depend on abstraction, proof obligations, or finite-state reduction rather than on a universal exact semantic decider. [inference; source: https://www.di.ens.fr/~cousot/AI/; https://www.di.ens.fr/~cousot/COUSOTpapers/POPL77.shtml; https://people.csail.mit.edu/asolar/SynthesisCourse/Lecture18.htm; https://will62794.github.io/my-notes/notes/Model_Checking/Model_Checking.html]

Another rival interpretation is that Godel alone already settles the software-analysis question, but the evidence supports a narrower conclusion: Godel clarifies the analogy, while the software claim itself depends on Turing-style undecidability and Rice's semantic generalisation. [inference; source: https://plato.stanford.edu/entries/goedel-incompleteness/; https://doi.org/10.1007/BF01700692; https://theory.stanford.edu/~trevisan/cs154-12/noterice.pdf]

The cross-item synthesis is justified because the earlier Popper and Causal Hierarchy items are both theorem-level statements about what one layer of evidence cannot settle, which is structurally the same role Rice's Theorem plays here for source code and semantic behaviour. [inference; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq1-1-popper-falsifiability.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq2-4-causal-hierarchy-formal-limits.md; https://theory.stanford.edu/~trevisan/cs154-12/noterice.pdf]

**Risks, gaps, uncertainties:**

- The cited verification sources show that restricted fragments and bounded cases exist, but this item does not enumerate those special cases exhaustively. [fact; source: https://will62794.github.io/my-notes/notes/Model_Checking/Model_Checking.html; https://people.csail.mit.edu/asolar/SynthesisCourse/Lecture18.htm; https://www.di.ens.fr/~cousot/AI/]
- The Godel comparison is interpretive and lower-confidence than the core computability claims, because the proof objects and success criteria differ even though both families concern formal limits. [inference; source: https://plato.stanford.edu/entries/goedel-incompleteness/; https://doi.org/10.1007/BF01700692; https://theory.stanford.edu/~trevisan/cs154-12/noterice.pdf]
- The engineering discussion is deliberately theorem-first rather than tool-first, so a follow-on item could catalogue which industrial assurances correspond to which restriction or abstraction pattern. [inference; source: https://www.di.ens.fr/~cousot/AI/; https://www.di.ens.fr/~cousot/COUSOTpapers/POPL77.shtml]

**Open questions:**

- Which practically important software classes, embedded control loops, smart contracts, typed total languages, or domain-specific workflow engines, recover the largest decidable fragment without collapsing usefulness?
- How should a later comparison item separate impossibility from tractable approximation when contrasting coded systems with agentic systems?
- Is there a clean taxonomy of assurance claims that maps each claim to its required restriction, abstraction, or proof obligation?

### §7 Recursive Review

```text
review_result: pass
acronym_audit: pass
domain_term_audit: pass
claim_label_audit: pass
citation_audit: pass
synthesis_findings_parity: aligned
confidence_assignment: medium
```

---

## Findings

### Executive Summary

No general algorithm can decide whether arbitrary programs halt or whether they satisfy any other non-trivial semantic property, so universal exact static verification of unrestricted coded systems is mathematically impossible. [fact; source: https://builds.openlogicproject.org/content/turing-machines/undecidability/halting-problem.pdf; https://theory.stanford.edu/~trevisan/cs154-12/noterice.pdf]

Practical verification succeeds only by narrowing the target, the model, or the semantics, or by accepting approximation through sound but incomplete abstractions. [inference; source: https://www.di.ens.fr/~cousot/COUSOTpapers/POPL77.shtml; https://www.di.ens.fr/~cousot/AI/; https://people.csail.mit.edu/asolar/SynthesisCourse/Lecture18.htm; https://will62794.github.io/my-notes/notes/Model_Checking/Model_Checking.html]

Godel's First Incompleteness Theorem is a parallel rather than the same result, because it limits what formal arithmetic systems can prove while Turing and Rice limit what program analysis can decide about behaviour. [inference; source: https://plato.stanford.edu/entries/goedel-incompleteness/; https://doi.org/10.1007/BF01700692; https://theory.stanford.edu/~trevisan/cs154-12/noterice.pdf]

Relative to earlier repository items, Rice's Theorem plays for coded systems the same boundary-setting role that Popperian falsifiability and the Causal Hierarchy play for scientific and causal models. [inference; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq1-1-popper-falsifiability.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq2-4-causal-hierarchy-formal-limits.md; https://theory.stanford.edu/~trevisan/cs154-12/noterice.pdf]

### Key Findings

1. **The halting problem proves that no general procedure can decide, for every arbitrary program and input pair, whether execution halts, so exact universal termination checking is impossible in the unrestricted case.** ([fact]; medium confidence; source: https://builds.openlogicproject.org/content/turing-machines/undecidability/halting-problem.pdf; https://cs.uwaterloo.ca/~s4bendav/files/CS360S21Lec16.pdf)
2. **Rice's Theorem extends this impossibility from termination to every non-trivial semantic property of a program, which means the barrier concerns behavioural meaning rather than one isolated verification task.** ([fact]; medium confidence; source: https://theory.stanford.edu/~trevisan/cs154-12/noterice.pdf)
3. **A static analyser for arbitrary general-purpose programs written in languages expressive enough to simulate general computation cannot therefore be both universal and exact about semantic behaviour, because such a tool would decide a question family that Turing and Rice prove undecidable.** ([inference]; medium confidence; source: https://builds.openlogicproject.org/content/turing-machines/undecidability/halting-problem.pdf; https://theory.stanford.edu/~trevisan/cs154-12/noterice.pdf; https://www.di.ens.fr/~cousot/COUSOTpapers/POPL77.shtml)
4. **Abstract interpretation provides a systematic response to undecidability by analysing concrete executions through abstractions that aim to remain sound while tolerating inaccuracy about concrete behaviour.** ([fact]; medium confidence; source: https://www.di.ens.fr/~cousot/COUSOTpapers/POPL77.shtml; https://www.di.ens.fr/~cousot/AI/)
5. **Deductive verification hits the same boundary for looping programs, because total-correctness proofs require invariants and termination arguments that are not computable automatically in full generality.** ([fact]; medium confidence; source: https://people.csail.mit.edu/asolar/SynthesisCourse/Lecture18.htm)
6. **Model checking regains decidability only after the system has been reduced to a finite-state transition model or another bounded abstraction, making algorithmic temporal-logic checking possible on that narrowed domain.** ([fact]; low confidence; source: https://will62794.github.io/my-notes/notes/Model_Checking/Model_Checking.html)
7. **Godel's first incompleteness theorem is a disciplined parallel, not a substitute proof, because it limits what a formal arithmetic system can prove while Turing and Rice limit what software analysis can decide.** ([inference]; medium confidence; source: https://plato.stanford.edu/entries/goedel-incompleteness/; https://doi.org/10.1007/BF01700692; https://theory.stanford.edu/~trevisan/cs154-12/noterice.pdf)
8. **This theorem family gives coded systems the same kind of hard epistemic boundary that earlier repository items found for scientific demarcation and causal inference, namely that one formal layer does not generically settle every deeper semantic truth.** ([inference]; medium confidence; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq1-1-popper-falsifiability.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq2-4-causal-hierarchy-formal-limits.md; https://theory.stanford.edu/~trevisan/cs154-12/noterice.pdf)

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [fact] No universal exact halting decider exists for arbitrary program-input pairs. | https://builds.openlogicproject.org/content/turing-machines/undecidability/halting-problem.pdf ; https://cs.uwaterloo.ca/~s4bendav/files/CS360S21Lec16.pdf | medium | diagonalisation result |
| [fact] Every non-trivial semantic property of a Turing machine's recognised language is undecidable. | https://theory.stanford.edu/~trevisan/cs154-12/noterice.pdf | medium | semantic-property theorem |
| [inference] Universal exact static analysis of unrestricted coded systems is impossible. | https://builds.openlogicproject.org/content/turing-machines/undecidability/halting-problem.pdf ; https://theory.stanford.edu/~trevisan/cs154-12/noterice.pdf ; https://www.di.ens.fr/~cousot/COUSOTpapers/POPL77.shtml | medium | halting plus Rice |
| [fact] Abstract interpretation responds to undecidability through sound but inexact abstraction over program semantics. | https://www.di.ens.fr/~cousot/COUSOTpapers/POPL77.shtml ; https://www.di.ens.fr/~cousot/AI/ | medium | approximation trade-off |
| [fact] Hoare-style and weakest-precondition verification need extra structure for loops and total correctness. | https://people.csail.mit.edu/asolar/SynthesisCourse/Lecture18.htm | medium | invariants and ranking functions |
| [fact] Model checking is algorithmic on finite-state transition systems and bounded temporal-logic problems. | https://will62794.github.io/my-notes/notes/Model_Checking/Model_Checking.html | low | decidability under restriction |
| [inference] Godel's theorem is an epistemic parallel but not the same undecidability theorem. | https://plato.stanford.edu/entries/goedel-incompleteness/ ; https://doi.org/10.1007/BF01700692 ; https://theory.stanford.edu/~trevisan/cs154-12/noterice.pdf | medium | proof boundary versus decision boundary |
| [inference] Rice's boundary is the coded-system analogue of earlier repository limits on scientific and causal inference. | https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq1-1-popper-falsifiability.md ; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq2-4-causal-hierarchy-formal-limits.md ; https://theory.stanford.edu/~trevisan/cs154-12/noterice.pdf | medium | cross-item synthesis |

### Assumptions

- [assumption] "General algorithm" in this item means one procedure over arbitrary general-purpose programs rather than over a restricted language or bounded abstraction, because the impossibility theorems target unrestricted universality. [source: https://builds.openlogicproject.org/content/turing-machines/undecidability/halting-problem.pdf; https://theory.stanford.edu/~trevisan/cs154-12/noterice.pdf; https://will62794.github.io/my-notes/notes/Model_Checking/Model_Checking.html]
- [assumption] "Static analysis" here includes abstract interpretation, deductive verification, and model checking insofar as each reasons about program behaviour without executing the target program on the target input of interest. [source: https://www.di.ens.fr/~cousot/AI/; https://people.csail.mit.edu/asolar/SynthesisCourse/Lecture18.htm; https://will62794.github.io/my-notes/notes/Model_Checking/Model_Checking.html]
- [assumption] The comparison to Popper and the Causal Hierarchy is a synthesis claim about formal limits on inferability, not an assertion that these theorems are mathematically reducible to one another. [source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq1-1-popper-falsifiability.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq2-4-causal-hierarchy-formal-limits.md; https://plato.stanford.edu/entries/goedel-incompleteness/]

### Analysis

The most secure conclusion in the item is the move from halting undecidability to Rice's general semantic barrier, because both sources address unrestricted program semantics directly rather than through a tool-specific engineering interpretation. [inference; source: https://builds.openlogicproject.org/content/turing-machines/undecidability/halting-problem.pdf; https://theory.stanford.edu/~trevisan/cs154-12/noterice.pdf]

A natural objection is that modern verifiers already prove many deep software properties, but the accessible evidence shows that those successes always depend on a smaller domain, a sound abstraction, or extra proof structure rather than on a universal semantic decider. [inference; source: https://www.di.ens.fr/~cousot/AI/; https://www.di.ens.fr/~cousot/COUSOTpapers/POPL77.shtml; https://people.csail.mit.edu/asolar/SynthesisCourse/Lecture18.htm; https://will62794.github.io/my-notes/notes/Model_Checking/Model_Checking.html]

Another objection is that Godel already settles the software case, but the evidence supports a narrower and cleaner synthesis: Godel clarifies the shape of the limit, while Turing and Rice establish the specific impossibility for algorithmic semantic analysis. [inference; source: https://plato.stanford.edu/entries/goedel-incompleteness/; https://doi.org/10.1007/BF01700692; https://theory.stanford.edu/~trevisan/cs154-12/noterice.pdf]

The cross-item comparison is warranted because the earlier Popper and Causal Hierarchy items also identify boundaries where one evidential layer cannot settle every deeper claim, which is structurally the same role Rice's Theorem plays for source code and behaviour. [inference; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq1-1-popper-falsifiability.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-18-rq2-4-causal-hierarchy-formal-limits.md; https://theory.stanford.edu/~trevisan/cs154-12/noterice.pdf]

### Risks, Gaps, and Uncertainties

- The cited verification sources show that restricted fragments and bounded cases exist, but this item does not enumerate those special cases exhaustively. [fact; source: https://will62794.github.io/my-notes/notes/Model_Checking/Model_Checking.html; https://people.csail.mit.edu/asolar/SynthesisCourse/Lecture18.htm; https://www.di.ens.fr/~cousot/AI/]
- The Godel bridge is interpretive and therefore lower-confidence than the core computability claims, because the proof target is formal derivability rather than semantic program analysis. [inference; source: https://plato.stanford.edu/entries/goedel-incompleteness/; https://doi.org/10.1007/BF01700692; https://theory.stanford.edu/~trevisan/cs154-12/noterice.pdf]
- A follow-on engineering item would still be useful to map concrete assurance claims, such as absence of runtime errors or temporal-safety invariants, to the exact restriction or abstraction that makes each claim checkable. [inference; source: https://www.di.ens.fr/~cousot/AI/; https://www.di.ens.fr/~cousot/COUSOTpapers/POPL77.shtml; https://will62794.github.io/my-notes/notes/Model_Checking/Model_Checking.html]

### Open Questions

- Which practically important software classes recover the largest decidable fragment without losing too much expressive power?
- How should the later comparison item separate impossibility theorems from tractable approximation when contrasting coded systems with agentic systems?
- Is there a clean assurance taxonomy that maps each verification claim to the restriction, abstraction, or proof obligation that makes it valid?

---

## Output

- Type: knowledge
- Description: Formal synthesis showing that universal exact static verification of arbitrary coded systems is impossible, and that practical verification works only through restriction or approximation. [inference; source: https://builds.openlogicproject.org/content/turing-machines/undecidability/halting-problem.pdf; https://theory.stanford.edu/~trevisan/cs154-12/noterice.pdf; https://www.di.ens.fr/~cousot/COUSOTpapers/POPL77.shtml]
- Links:
  - https://builds.openlogicproject.org/content/turing-machines/undecidability/halting-problem.pdf
  - https://theory.stanford.edu/~trevisan/cs154-12/noterice.pdf
  - https://www.di.ens.fr/~cousot/COUSOTpapers/POPL77.shtml
