---
title: "Kona and Aleph at their core, with Lean and unifying concepts"
added: 2026-05-17T10:41:11+00:00
status: reviewing
priority: medium
blocks: []
tags: [formal-methods, theorem-proving, lean, agentic-ai]
started: 2026-05-17T19:52:08+00:00
completed: ~
output: []
cites:
  - 2026-03-18-formal-proof-engineering-leanstral
  - 2026-03-10-formal-spec-intent-alignment-agentic-coding
related:
  - 2026-05-17-policy-enforcement-formal-verification-energy-functions
superseded_by: ~
supersedes: ~
item_type: primary
confidence: medium
versions: []
---

# Kona and Aleph at their core, with Lean and unifying concepts

## Research Question

What are Kona and Aleph at their core, what do they each do in practice, how does Lean (the theorem prover) relate to them, and which unifying concepts explain where they overlap and differ?

## Scope

**In scope:**
- Core definition of Kona and Aleph (what each system is and is for)
- Deep analysis of Kona and Aleph architecture, workflows, and intended users
- Lean theorem prover basics at a light-touch level, focused on comparison and context
- Light-touch survey of adjacent concepts and tools, including interactive theorem proving (where a user steers proof construction), automated theorem proving (where the system searches on its own), formal verification, tactic systems (proof-command systems), and proof automation
- Follow-up research questions that expose unifying concepts and unresolved tensions

**Out of scope:**
- Full implementation tutorials for any tool
- Exhaustive benchmark replication or new experimental evaluation
- Commercial procurement analysis

**Constraints:** Use publicly available primary documentation, papers, and technical write-ups. Resolve naming ambiguity first if multiple projects use the names "Kona" or "Aleph".

## Context

The practical decision this item supports is whether the named systems should be treated as proof assistants, proof-automation services, or adjacent reasoning infrastructure when choosing follow-up research and tooling directions. [inference; source: https://davidamitchell.github.io/Research/research/2026-03-18-formal-proof-engineering-leanstral.html; https://davidamitchell.github.io/Research/research/2026-03-10-formal-spec-intent-alignment-agentic-coding.html]

## Approach

1. Disambiguation pass: which publicly documented projects are meant by “Kona” and “Aleph” in this context?
   1a. Identify candidate projects for each name and decide inclusion/exclusion criteria.
   1b. Confirm the selected Kona and Aleph entities with primary sources.
2. For Kona: what is it, what problem does it solve, and how does it work at a system level?
   2a. Core model and design goals.
   2b. Workflow, interfaces, and automation strategy.
3. For Aleph: what is it, what problem does it solve, and how does it work at a system level?
   3a. Core model and design goals.
   3b. Workflow, interfaces, and automation strategy.
4. How does Lean fit relative to Kona and Aleph?
   4a. Role of Lean in formal proof development.
   4b. Integration points, compatibility, and conceptual differences.
5. Which unifying concepts span all three, for example proof search, tactic orchestration (sequencing proof commands), trust model, and human review inside the workflow?
6. What are the highest-value follow-up questions for deeper research on those unifying concepts?

## Sources

- [x] [Lean Language Home](https://lean-lang.org/)
- [x] [Lean Learn](https://lean-lang.org/learn/)
- [x] [Theorem Proving in Lean 4](https://lean-lang.org/theorem_proving_in_lean4/)
- [x] [de Moura and Ullrich (2021) The Lean 4 Theorem Prover and Programming Language](https://doi.org/10.1007/978-3-030-79876-5_37)
- [x] [Lean Community Documentation](https://leanprover-community.github.io/)
- [x] [leanprover-community mathlib4 README](https://github.com/leanprover-community/mathlib4)
- [x] [GitHub Aleph prover App](https://github.com/apps/aleph-prover)
- [x] [Python Package Index (PyPI) AlephProver Command Line Interface (CLI)](https://pypi.org/project/alephprover/)
- [x] [logical-intelligence proofs repository](https://github.com/logical-intelligence/proofs)
- [x] [LeanDojo-v2](https://leandojo.org/leandojo.html)
- [x] [Yang et al. (2023) LeanDojo: Theorem Proving with Retrieval-Augmented Language Models](https://github.com/lean-dojo/ReProver)
- [x] [Song et al. (2025) Lean Copilot: Large Language Models as Copilots for Theorem Proving in Lean](https://arxiv.org/abs/2404.12534)
- [x] [Mitchell (2026) More formal proof engineering: Leanstral and Artificial Intelligence (AI)-assisted formal verification](https://davidamitchell.github.io/Research/research/2026-03-18-formal-proof-engineering-leanstral.html)
- [x] [Mitchell (2026) Formal intent specification and language choice for AI alignment in agentic coding systems](https://davidamitchell.github.io/Research/research/2026-03-10-formal-spec-intent-alignment-agentic-coding.html)
- [ ] [OpenAI Research](https://openai.com/research/) - seed disambiguation path, not consulted as evidence
- [ ] [arXiv Computer Science Logic recent submissions](https://arxiv.org/list/cs.LO/recent) - identified as a background literature surface, but narrower consulted sources above were more specific

## Related

- [Mitchell (2026) More formal proof engineering: Leanstral and Artificial Intelligence (AI)-assisted formal verification](https://davidamitchell.github.io/Research/research/2026-03-18-formal-proof-engineering-leanstral.html)
- [Mitchell (2026) Formal intent specification and language choice for AI alignment in agentic coding systems](https://davidamitchell.github.io/Research/research/2026-03-10-formal-spec-intent-alignment-agentic-coding.html)
- [Mitchell (2026) Policy enforcement and formal verification as Energy-Based Model (EBM) optimization signals](https://davidamitchell.github.io/Research/research/2026-05-17-policy-enforcement-formal-verification-energy-functions.html)

---

## Research Skill Output

*(Full output from running the research skill, retained verbatim in the completed item. Sections 0 to 5 are the investigation, and section 6 seeds the Findings section below.)*

### §0 Initialise

- Question: determine what Aleph and Kona are at their core, how Lean relates to them, and which shared concepts best explain overlap and difference.
- Scope: deep characterization of Aleph and Kona where public evidence exists; light-touch Lean foundation; adjacent concepts only where needed to explain comparison.
- Constraints: public sources only, resolve naming ambiguity first, full research mode, no speculative internals for unresolved systems.
- Output: full sections 0 through 7 plus Findings with Executive Summary, Key Findings, Evidence Map, Assumptions, Analysis, Risks, Gaps, Uncertainties, Open Questions, and Output.
- [fact; source: https://davidamitchell.github.io/Research/research/2026-03-18-formal-proof-engineering-leanstral.html; https://davidamitchell.github.io/Research/research/2026-03-10-formal-spec-intent-alignment-agentic-coding.html] Prior completed-item sweep: the closest completed repository work already established Lean as a mechanically checked proof substrate and framed Artificial Intelligence (AI)-assisted proof engineering as a stack above that substrate, but no completed item directly covered Aleph or any publicly documented Kona.
- [fact; source: https://lean-lang.org/learn/; https://doi.org/10.1007/978-3-030-79876-5_37] Working definition: Lean is an interactive theorem prover and functional programming language whose kernel checks proof terms and whose wider ecosystem supports both mathematics and formal verification.
- [fact; source: https://github.com/apps/aleph-prover; https://pypi.org/project/alephprover/] Working definition: Aleph Prover is an external proof-automation service for Lean 4 repositories, exposed as a GitHub App and Command Line Interface (CLI), that submits proof jobs against Lean projects and returns patches or pull requests.
- [assumption; source: https://lean-lang.org/; https://github.com/apps/aleph-prover] Working assumption: if Kona is the intended comparison target, it should have an accessible official surface comparable to Lean or Aleph; if no such surface can be found, the responsible conclusion is unresolved identification rather than invented characterization.

### §1 Question Decomposition

- **Root question:** what can be said, from public evidence, about Kona and Aleph as systems around Lean, and what conceptual map best explains their relationship?
- **A. Disambiguation**
  - A1. Which publicly documented candidate systems match the name Aleph in the theorem-proving context?
  - A2. Which publicly documented candidate systems match the name Kona in the theorem-proving or Lean context?
  - A3. Which candidate, if any, can be confirmed with primary sources?
- **B. Aleph**
  - B1. What does Aleph officially claim to do?
  - B2. What workflow and interfaces does Aleph expose?
  - B3. What trust boundary exists between Aleph and Lean?
- **C. Lean**
  - C1. What is Lean at its core?
  - C2. Which Lean properties matter for comparing it with automation layers such as Aleph?
- **D. Unifying concepts**
  - D1. Which concepts connect Lean, Aleph, and the wider AI-assisted theorem-proving landscape?
  - D2. Which concepts separate substrate, automation layer, and unresolved naming candidate?
- **E. Follow-up questions**
  - E1. What highest-value research questions remain after the public evidence pass?
  - E2. Which missing evidence would most change the current conclusion about Kona?

### §2 Investigation

#### 2.1 Disambiguation and source-access notes

- Search note: `Kona Lean 4`; `Kona theorem prover`; `site:openai.com Kona theorem prover`; `site:github.com Kona Lean 4 theorem proving` -> no accessible official Kona project page located in this session.
- [fact; source: https://github.com/apps/aleph-prover; https://pypi.org/project/alephprover/] Aleph is disambiguated cleanly: the public theorem-proving referent is Aleph Prover, a Lean 4 proof-automation service with official GitHub App and Python Package Index (PyPI) surfaces.
- [inference; source: https://lean-lang.org/; https://arxiv.org/abs/2501.18639; https://github.com/apps/aleph-prover] Kona is not disambiguated cleanly from the accessible public evidence base used here, because the consulted official Lean surfaces and current Lean survey did not identify a Lean- or theorem-proving system named Kona, while Aleph had direct official surfaces that made its identification straightforward.
- [inference; source: https://github.com/apps/aleph-prover; https://pypi.org/project/alephprover/; https://lean-lang.org/] The defensible comparison set is therefore asymmetric: Aleph and Lean can be characterized directly, while Kona can only be characterized as an unresolved public referent.

#### 2.2 What Lean is at its core

- [fact; source: https://lean-lang.org/; https://lean-lang.org/learn/] Lean describes itself as an open-source programming language and proof assistant, built for formalizing mathematics, correct software, and formal verification, rather than as a standalone automated prover.
- [fact; source: https://doi.org/10.1007/978-3-030-79876-5_37; https://lean-lang.org/learn/] The Lean 4 system description says Lean 4 is a reimplementation of the Lean interactive theorem prover in Lean itself, is fully extensible, and couples theorem proving with efficient functional programming so users can build proof automation inside the same environment.
- [fact; source: https://lean-lang.org/theorem_proving_in_lean4/; https://leanprover-community.github.io/] Lean's official tutorial and community documentation position Lean as a human-steered proving environment where users interact with goals, tactics, and definitions, with community tooling and mathlib widening the reachable proof space.
- [fact; source: https://github.com/leanprover-community/mathlib4; https://leanprover-community.github.io/] The mathlib ecosystem adds a large maintained library of mathematics, tactics, documentation, and build workflows, which makes Lean a practical substrate for both research mathematics and verified software projects.
- [inference; source: https://lean-lang.org/; https://doi.org/10.1007/978-3-030-79876-5_37; https://github.com/leanprover-community/mathlib4] At core, Lean is the substrate and trust anchor in this comparison: it defines the logic, proof language, kernel checking, libraries, and build environment against which higher-level automation must operate.

#### 2.3 What Aleph is at its core

- [fact; source: https://github.com/apps/aleph-prover; https://pypi.org/project/alephprover/] Aleph Prover's public product surfaces describe it as an automated theorem prover for Lean 4 projects that clones repositories, generates proofs, and opens pull requests or applies diffs with proven theorems.
- [fact; source: https://pypi.org/project/alephprover/] The Aleph CLI workflow is explicit: it finds the Lean project root, zips the project, uploads it to an external service, polls for completion, and downloads a proof diff that can be applied with `git apply`.
- [fact; source: https://github.com/apps/aleph-prover; https://prover.logicalintelligence.com/] The public integration surfaces show Aleph as a third-party service owned by logiq-ai or Logical Intelligence, exposed through a GitHub App and a hosted prover site rather than as a self-contained proof assistant.
- [fact; source: https://github.com/logical-intelligence/proofs; https://github.com/apps/aleph-prover] The public proofs repository provides at least one worked example of Aleph's output, describing a formal proof of a conjecture as automatically proven using the Aleph prover system and linking the formal statement back to an upstream Lean formalization.
- [inference; source: https://github.com/apps/aleph-prover; https://pypi.org/project/alephprover/; https://github.com/logical-intelligence/proofs] At core, Aleph is best understood as a productized automation layer around Lean repositories: it packages proof search, job orchestration, repository handling, and patch delivery, while delegating final proof validity to Lean's checking pipeline.

#### 2.4 Adjacent Lean automation and the trust boundary

- [fact; source: https://leandojo.org/leandojo.html; https://github.com/lean-dojo/ReProver] LeanDojo and ReProver represent a research-oriented path to Lean automation, turning Lean into a gym-like environment, retrieving premises, and generating tactics or proof steps through retrieval-augmented models.
- [fact; source: https://arxiv.org/abs/2404.12534; https://github.com/lean-dojo/LeanCopilot] Lean Copilot represents a human-assistance path, embedding Large Language Models (LLMs) into Lean so users can request tactic suggestions, premise selection, or proof search inside the interactive proving workflow.
- [inference; source: https://github.com/apps/aleph-prover; https://pypi.org/project/alephprover/; https://arxiv.org/abs/2404.12534; https://leandojo.org/leandojo.html] Aleph differs from these adjacent tools less by the underlying theorem-proving substrate than by packaging and operating model: LeanDojo and ReProver are research infrastructure, Lean Copilot is in-editor assistance, and Aleph is a hosted repository-level service that returns patches or pull requests.
- [inference; source: https://lean-lang.org/; https://doi.org/10.1007/978-3-030-79876-5_37; https://github.com/apps/aleph-prover] The trust model is shared across these systems at the deepest level: automated suggestions matter only insofar as Lean can elaborate and check the resulting proof terms, so automation improves search and ergonomics but does not replace the kernel-checked substrate.

#### 2.5 What can and cannot be said about Kona

- [inference; source: https://lean-lang.org/; https://arxiv.org/abs/2501.18639; https://github.com/apps/aleph-prover] No public primary source consulted in this item was sufficient to identify a theorem-proving or Lean-adjacent system named Kona, so claims about Kona's architecture, workflow, intended user, or relation to Lean would exceed the evidence.
- [inference; source: https://github.com/apps/aleph-prover; https://pypi.org/project/alephprover/; https://lean-lang.org/] The most responsible synthesis is not that Kona does not exist, but that Kona is unresolved in the accessible public record used here, which leaves the Aleph-versus-Lean comparison robust and the Kona branch open.

#### 2.6 Unifying concepts and follow-up questions

- [fact; source: https://lean-lang.org/theorem_proving_in_lean4/; https://leandojo.org/leandojo.html; https://arxiv.org/abs/2404.12534] The shared technical concepts across Lean and Lean-based automation are proof states, tactics, premise selection, and proof search over a mechanically checked formal language.
- [fact; source: https://github.com/apps/aleph-prover; https://pypi.org/project/alephprover/; https://github.com/lean-dojo/LeanCopilot] The shared workflow concepts across Aleph and other Lean automation tools are orchestration around an existing Lean project, model-generated candidate steps, and a feedback loop in which proofs are accepted only when the Lean environment can verify them.
- [inference; source: https://github.com/apps/aleph-prover; https://github.com/lean-dojo/LeanCopilot; https://leandojo.org/leandojo.html; https://davidamitchell.github.io/Research/research/2026-03-18-formal-proof-engineering-leanstral.html] The unifying conceptual map is layered: Lean is the verification substrate, proof-automation systems operate as search or assistance layers above it, and hosted products such as Aleph add repository and service orchestration around that automation layer.
- [inference; source: https://lean-lang.org/; https://github.com/apps/aleph-prover; https://arxiv.org/abs/2404.12534] The highest-value follow-up questions are which official Kona source the original request intended, how Aleph performs against open research baselines on shared Lean benchmarks, and where hosted proof services fit relative to in-editor copilots and open-source research frameworks.

### §3 Reasoning

- [fact; source: https://lean-lang.org/; https://doi.org/10.1007/978-3-030-79876-5_37] What can be stated as fact is bounded: Lean is a proof assistant and programming language with a kernel-checked trust model, and Aleph is a public Lean 4 proof-automation service with repository-facing interfaces.
- [inference; source: https://github.com/apps/aleph-prover; https://pypi.org/project/alephprover/; https://arxiv.org/abs/2404.12534] The classification "substrate versus automation layer" is an inference from the documented interfaces and workflows rather than a sentence stated verbatim by any one source.
- [assumption; source: https://lean-lang.org/; https://github.com/apps/aleph-prover] The unresolved Kona branch is handled conservatively by assuming that absent public primary evidence, characterization would be less reliable than explicitly preserving the ambiguity.
- [inference; source: https://github.com/apps/aleph-prover; https://github.com/lean-dojo/LeanCopilot; https://leandojo.org/leandojo.html] Packaging and operating-model differences matter analytically because they shape intended user, trust handoff, and review surface even when underlying proof search techniques overlap.

### §4 Consistency Check

- [fact; source: https://github.com/apps/aleph-prover; https://pypi.org/project/alephprover/] Aleph's GitHub App description and CLI documentation are consistent on the core workflow: Lean repository in, automated proof attempt, patch or pull request out.
- [fact; source: https://lean-lang.org/; https://doi.org/10.1007/978-3-030-79876-5_37; https://leanprover-community.github.io/] Lean's homepage, tutorial, system paper, and community documentation are consistent on Lean being a proof assistant and programming language rather than a hosted proving service.
- [inference; source: https://lean-lang.org/; https://arxiv.org/abs/2501.18639; https://github.com/apps/aleph-prover] The only unresolved inconsistency risk is entity identification for Kona, and the item resolves it by leaving the branch open instead of forcing an unsupported match.

### §5 Depth and Breadth Expansion

#### Technical lens

- [fact; source: https://lean-lang.org/theorem_proving_in_lean4/; https://github.com/apps/aleph-prover] Technically, the sharpest distinction is between a formal language and checker on one side, and a service that automates candidate proof construction around that checker on the other.

#### Historical lens

- [fact; source: https://doi.org/10.1007/978-3-030-79876-5_37; https://arxiv.org/abs/2404.12534; https://leandojo.org/leandojo.html] Historically, the Lean ecosystem has moved from interactive proving toward a spectrum of research and product automation layers, including retrieval-augmented proving, in-editor copilots, and hosted proof services.

#### Behavioural lens

- [inference; source: https://github.com/apps/aleph-prover; https://github.com/lean-dojo/LeanCopilot] Behaviourally, Aleph assumes a repository-owner workflow centered on asynchronous proof jobs and code review, while Lean Copilot assumes an interactive user who stays inside the editor and accepts or rejects suggestions in real time.

#### Economic lens

- [inference; source: https://pypi.org/project/alephprover/; https://github.com/lean-dojo/LeanCopilot; https://leandojo.org/leandojo.html] The packaging split also implies a different cost structure: Aleph externalizes compute and orchestration into a hosted service, whereas LeanDojo-style tooling and Lean Copilot shift more setup and model-management burden toward the user or research team.

#### Governance lens

- [inference; source: https://lean-lang.org/; https://github.com/apps/aleph-prover; https://davidamitchell.github.io/Research/research/2026-03-10-formal-spec-intent-alignment-agentic-coding.html] Governance remains anchored in Lean's checker and in human review of repository changes, because proof automation can propose or search, but the consequence-bearing action is still accepting verified patches into a codebase.

### §6 Synthesis

**Executive summary:**

Aleph is a publicly documented Lean 4 proof-automation service layered on top of Lean, while Kona could not be resolved to a publicly documented Lean- or theorem-proving system from the accessible evidence base used in this item. [inference; source: https://github.com/apps/aleph-prover; https://pypi.org/project/alephprover/; https://lean-lang.org/; https://arxiv.org/abs/2501.18639] Lean itself is the core proof substrate: a programming language and interactive theorem prover with kernel-checked trust, extensibility, and a large surrounding ecosystem. [fact; source: https://lean-lang.org/; https://doi.org/10.1007/978-3-030-79876-5_37; https://leanprover-community.github.io/; https://github.com/leanprover-community/mathlib4] Aleph sits above that substrate as a hosted automation and repository-orchestration layer that uploads Lean projects, searches for proofs, and returns diffs or pull requests. [fact; source: https://github.com/apps/aleph-prover; https://pypi.org/project/alephprover/; https://github.com/logical-intelligence/proofs] The most useful unifying concepts are proof search, tactic and premise orchestration, kernel-checked trust, and the distinction between interactive assistance, research infrastructure, and productized hosted automation. [inference; source: https://leandojo.org/leandojo.html; https://arxiv.org/abs/2404.12534; https://github.com/lean-dojo/ReProver; https://github.com/apps/aleph-prover]

**Key findings:**

1. **Lean is the foundational system in this comparison because it combines an interactive theorem prover, a functional programming language, and a kernel-checked verification model that all higher-level automation layers must ultimately satisfy.** ([fact]; high confidence; source: https://lean-lang.org/; https://doi.org/10.1007/978-3-030-79876-5_37; https://leanprover-community.github.io/)
2. **Aleph Prover is not a replacement for Lean itself but a hosted automation layer for Lean 4 repositories, exposing repository cloning, proof generation, and patch or pull-request delivery through GitHub App and CLI interfaces.** ([fact]; high confidence; source: https://github.com/apps/aleph-prover; https://pypi.org/project/alephprover/)
3. **The accessible public evidence does not currently support a confident technical characterization of Kona, so the responsible synthesis is to preserve Kona as an unresolved referent rather than force a speculative mapping onto another proving project.** ([inference]; medium confidence; source: https://lean-lang.org/; https://arxiv.org/abs/2501.18639; https://github.com/apps/aleph-prover)
4. **Aleph, Lean Copilot, LeanDojo, and ReProver all participate in the same broad AI-assisted theorem-proving space, but they occupy different operating positions across hosted service automation, in-editor assistance, and research infrastructure.** ([inference]; medium confidence; source: https://github.com/apps/aleph-prover; https://arxiv.org/abs/2404.12534; https://leandojo.org/leandojo.html; https://github.com/lean-dojo/ReProver)
5. **The deepest common trust mechanism across Lean-based automation tools is still Lean's own checking pipeline, which means model-generated tactics or whole proofs matter only when they elaborate and verify inside Lean's formal environment.** ([inference]; high confidence; source: https://lean-lang.org/; https://doi.org/10.1007/978-3-030-79876-5_37; https://github.com/apps/aleph-prover; https://github.com/lean-dojo/LeanCopilot)
6. **The most decision-useful unifying concepts for follow-up research are proof search, tactic sequencing, premise retrieval, repository workflow integration, and human review placement, because those concepts explain most of the observed overlap and most of the practical differences.** ([inference]; medium confidence; source: https://lean-lang.org/theorem_proving_in_lean4/; https://leandojo.org/leandojo.html; https://arxiv.org/abs/2404.12534; https://github.com/apps/aleph-prover)
7. **The highest-value next step is not deeper generic research on Lean, but identification of the exact official Kona source intended by the original request, because that missing referent is now the main barrier to a symmetric system comparison.** ([inference]; medium confidence; source: https://lean-lang.org/; https://github.com/apps/aleph-prover; https://arxiv.org/abs/2404.12534)

**Evidence map:**

| claim | source | confidence | notes |
|---|---|---|---|
| [fact] Lean is the foundational proof substrate with kernel-checked verification and extensibility. | https://lean-lang.org/ ; https://doi.org/10.1007/978-3-030-79876-5_37 ; https://leanprover-community.github.io/ | high | official docs plus system paper |
| [fact] Aleph is a hosted automation layer for Lean 4 repositories, exposed through GitHub App and CLI surfaces. | https://github.com/apps/aleph-prover ; https://pypi.org/project/alephprover/ | high | direct product surfaces |
| [inference] Kona remains unresolved in the accessible public evidence base. | https://lean-lang.org/ ; https://arxiv.org/abs/2501.18639 ; https://github.com/apps/aleph-prover | medium | negative-evidence synthesis |
| [inference] Lean-based automation spans hosted service, in-editor copilot, and research-infrastructure positions. | https://github.com/apps/aleph-prover ; https://arxiv.org/abs/2404.12534 ; https://leandojo.org/leandojo.html ; https://github.com/lean-dojo/ReProver | medium | comparative synthesis |
| [inference] Lean's checker remains the deepest trust mechanism across these tools. | https://lean-lang.org/ ; https://doi.org/10.1007/978-3-030-79876-5_37 ; https://github.com/lean-dojo/LeanCopilot ; https://github.com/apps/aleph-prover | high | substrate-plus-tool comparison |
| [inference] Proof search, tactic sequencing, premise retrieval, repository workflow, and human review explain most overlap and difference. | https://lean-lang.org/theorem_proving_in_lean4/ ; https://leandojo.org/leandojo.html ; https://arxiv.org/abs/2404.12534 ; https://github.com/apps/aleph-prover | medium | concept map |
| [inference] Confirming the intended Kona source is the highest-value follow-up question. | https://lean-lang.org/ ; https://github.com/apps/aleph-prover ; https://arxiv.org/abs/2404.12534 | medium | evidence-gap driven |

**Assumptions:**

- [assumption; source: https://lean-lang.org/; https://github.com/apps/aleph-prover] This item assumes the intended Kona referent should have a public official surface comparable to Lean or Aleph; if the intended system is private, internal, or recently announced, the public-record method used here will under-identify it.
- [assumption; source: https://github.com/apps/aleph-prover; https://pypi.org/project/alephprover/] This item assumes Aleph's public product descriptions are materially representative of its operating model even though the full backend implementation is not publicly inspectable from the consulted sources.

**Analysis:**

The evidence is strong on the Lean side and strong on the Aleph side because both have direct official product or documentation surfaces. [fact; source: https://lean-lang.org/; https://github.com/apps/aleph-prover; https://pypi.org/project/alephprover/] The evidence is weak on the Kona side because the research question required disambiguation first, and the accessible primary-source search did not resolve an official Kona system page. [inference; source: https://lean-lang.org/; https://arxiv.org/abs/2501.18639; https://github.com/apps/aleph-prover/] That asymmetry makes the most reliable synthesis layered rather than pairwise: Lean is the formal substrate, Aleph is one automation layer around that substrate, and Kona remains a missing referent that prevents a symmetric technical comparison. [inference; source: https://doi.org/10.1007/978-3-030-79876-5_37; https://github.com/apps/aleph-prover; https://pypi.org/project/alephprover/] The adjacent-tool comparison matters because it shows Aleph is not unique in using model assistance for theorem proving, but is distinct in packaging itself as a hosted repository service rather than as an in-editor copilot or an open research framework. [inference; source: https://arxiv.org/abs/2404.12534; https://leandojo.org/leandojo.html; https://github.com/lean-dojo/ReProver; https://github.com/apps/aleph-prover]

**Risks, gaps, uncertainties:**

- The largest unresolved gap is entity identification for Kona, which lowers confidence in any conclusion that requires a direct Kona-versus-Aleph technical comparison. [inference; source: https://lean-lang.org/; https://arxiv.org/abs/2501.18639; https://github.com/apps/aleph-prover]
- Aleph's public sources document interfaces and workflow clearly, but they do not expose enough backend detail to evaluate internal search strategy, benchmark methodology, or service reliability in depth. [fact; source: https://github.com/apps/aleph-prover; https://pypi.org/project/alephprover/; https://github.com/logical-intelligence/proofs]
- The public evidence base says more about Lean's trust model than about Aleph's empirical performance, so practical tool-choice decisions still need benchmark and workflow evidence beyond marketing or README-level claims. [inference; source: https://lean-lang.org/; https://doi.org/10.1007/978-3-030-79876-5_37; https://github.com/apps/aleph-prover]

**Open questions:**

- Which exact official Kona project, repository, or paper did the original request intend?
- How does Aleph perform on shared Lean benchmarks relative to Lean Copilot, ReProver, and other public systems?
- What review and approval workflow is most effective when hosted proof services open pull requests against live Lean repositories?
- Which classes of proof task are best served by in-editor copilots versus asynchronous hosted proof services?

### §7 Recursive Review

- Review result: pass
- Acronym audit: Lean, AI, CLI, and LLM are expanded on first use in visible prose where they appear.
- Claim audit: factual claims in Research Skill Output are source-bound; inferential claims are labelled; unresolved Kona identification remains explicit rather than hidden.
- Cross-item audit: prior completed items on Leanstral and formal specification are integrated where they sharpen substrate-versus-automation interpretation.

---

## Findings

### Executive Summary

Aleph is a publicly documented Lean 4 proof-automation service layered on top of Lean, while Kona could not be resolved to a publicly documented Lean- or theorem-proving system from the accessible evidence base used in this item. [inference; source: https://github.com/apps/aleph-prover; https://pypi.org/project/alephprover/; https://lean-lang.org/; https://arxiv.org/abs/2501.18639] Lean itself is the core proof substrate: a programming language and interactive theorem prover with kernel-checked trust, extensibility, and a large surrounding ecosystem. [fact; source: https://lean-lang.org/; https://doi.org/10.1007/978-3-030-79876-5_37; https://leanprover-community.github.io/; https://github.com/leanprover-community/mathlib4] Aleph sits above that substrate as a hosted automation and repository-orchestration layer that uploads Lean projects, searches for proofs, and returns diffs or pull requests. [fact; source: https://github.com/apps/aleph-prover; https://pypi.org/project/alephprover/; https://github.com/logical-intelligence/proofs] The most useful unifying concepts are proof search, tactic and premise orchestration, kernel-checked trust, and the distinction between interactive assistance, research infrastructure, and productized hosted automation. [inference; source: https://leandojo.org/leandojo.html; https://arxiv.org/abs/2404.12534; https://github.com/lean-dojo/ReProver; https://github.com/apps/aleph-prover]

### Key Findings

1. **Lean is the foundational system in this comparison because it combines an interactive theorem prover, a functional programming language, and a kernel-checked verification model that all higher-level automation layers must ultimately satisfy.** ([fact]; high confidence; source: https://lean-lang.org/; https://doi.org/10.1007/978-3-030-79876-5_37; https://leanprover-community.github.io/)
2. **Aleph Prover is not a replacement for Lean itself but a hosted automation layer for Lean 4 repositories, exposing repository cloning, proof generation, and patch or pull-request delivery through GitHub App and CLI interfaces.** ([fact]; high confidence; source: https://github.com/apps/aleph-prover; https://pypi.org/project/alephprover/)
3. **The accessible public evidence does not currently support a confident technical characterization of Kona, so the responsible synthesis is to preserve Kona as an unresolved referent rather than force a speculative mapping onto another proving project.** ([inference]; medium confidence; source: https://lean-lang.org/; https://arxiv.org/abs/2501.18639; https://github.com/apps/aleph-prover)
4. **Aleph, Lean Copilot, LeanDojo, and ReProver all participate in the same broad AI-assisted theorem-proving space, but they occupy different operating positions across hosted service automation, in-editor assistance, and research infrastructure.** ([inference]; medium confidence; source: https://github.com/apps/aleph-prover; https://arxiv.org/abs/2404.12534; https://leandojo.org/leandojo.html; https://github.com/lean-dojo/ReProver)
5. **The deepest common trust mechanism across Lean-based automation tools is still Lean's own checking pipeline, which means model-generated tactics or whole proofs matter only when they elaborate and verify inside Lean's formal environment.** ([inference]; high confidence; source: https://lean-lang.org/; https://doi.org/10.1007/978-3-030-79876-5_37; https://github.com/apps/aleph-prover; https://github.com/lean-dojo/LeanCopilot)
6. **The most decision-useful unifying concepts for follow-up research are proof search, tactic sequencing, premise retrieval, repository workflow integration, and human review placement, because those concepts explain most of the observed overlap and most of the practical differences.** ([inference]; medium confidence; source: https://lean-lang.org/theorem_proving_in_lean4/; https://leandojo.org/leandojo.html; https://arxiv.org/abs/2404.12534; https://github.com/apps/aleph-prover)
7. **The highest-value next step is not deeper generic research on Lean, but identification of the exact official Kona source intended by the original request, because that missing referent is now the main barrier to a symmetric system comparison.** ([inference]; medium confidence; source: https://lean-lang.org/; https://github.com/apps/aleph-prover; https://arxiv.org/abs/2404.12534)

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [fact] Lean is the foundational proof substrate with kernel-checked verification and extensibility. | https://lean-lang.org/ ; https://doi.org/10.1007/978-3-030-79876-5_37 ; https://leanprover-community.github.io/ | high | official docs plus system paper |
| [fact] Aleph is a hosted automation layer for Lean 4 repositories, exposed through GitHub App and CLI surfaces. | https://github.com/apps/aleph-prover ; https://pypi.org/project/alephprover/ | high | direct product surfaces |
| [inference] Kona remains unresolved in the accessible public evidence base. | https://lean-lang.org/ ; https://arxiv.org/abs/2501.18639 ; https://github.com/apps/aleph-prover | medium | negative-evidence synthesis |
| [inference] Lean-based automation spans hosted service, in-editor copilot, and research-infrastructure positions. | https://github.com/apps/aleph-prover ; https://arxiv.org/abs/2404.12534 ; https://leandojo.org/leandojo.html ; https://github.com/lean-dojo/ReProver | medium | comparative synthesis |
| [inference] Lean's checker remains the deepest trust mechanism across these tools. | https://lean-lang.org/ ; https://doi.org/10.1007/978-3-030-79876-5_37 ; https://github.com/lean-dojo/LeanCopilot ; https://github.com/apps/aleph-prover | high | substrate-plus-tool comparison |
| [inference] Proof search, tactic sequencing, premise retrieval, repository workflow, and human review explain most overlap and difference. | https://lean-lang.org/theorem_proving_in_lean4/ ; https://leandojo.org/leandojo.html ; https://arxiv.org/abs/2404.12534 ; https://github.com/apps/aleph-prover | medium | concept map |
| [inference] Confirming the intended Kona source is the highest-value follow-up question. | https://lean-lang.org/ ; https://github.com/apps/aleph-prover ; https://arxiv.org/abs/2404.12534 | medium | evidence-gap driven |

### Assumptions

- This item assumes the intended Kona referent should have a public official surface comparable to Lean or Aleph; if the intended system is private, internal, or recently announced, the public-record method used here will under-identify it. [assumption; source: https://lean-lang.org/; https://github.com/apps/aleph-prover]
- This item assumes Aleph's public product descriptions are materially representative of its operating model even though the full backend implementation is not publicly inspectable from the consulted sources. [assumption; source: https://github.com/apps/aleph-prover; https://pypi.org/project/alephprover/]

### Analysis

The evidence is strong on the Lean side and strong on the Aleph side because both have direct official product or documentation surfaces. [fact; source: https://lean-lang.org/; https://github.com/apps/aleph-prover; https://pypi.org/project/alephprover/] The evidence is weak on the Kona side because the research question required disambiguation first, and the accessible primary-source search did not resolve an official Kona system page. [inference; source: https://lean-lang.org/; https://arxiv.org/abs/2501.18639; https://github.com/apps/aleph-prover/] That asymmetry makes the most reliable synthesis layered rather than pairwise: Lean is the formal substrate, Aleph is one automation layer around that substrate, and Kona remains a missing referent that prevents a symmetric technical comparison. [inference; source: https://doi.org/10.1007/978-3-030-79876-5_37; https://github.com/apps/aleph-prover; https://pypi.org/project/alephprover/] The adjacent-tool comparison matters because it shows Aleph is not unique in using model assistance for theorem proving, but is distinct in packaging itself as a hosted repository service rather than as an in-editor copilot or an open research framework. [inference; source: https://arxiv.org/abs/2404.12534; https://leandojo.org/leandojo.html; https://github.com/lean-dojo/ReProver; https://github.com/apps/aleph-prover]

### Risks, Gaps, and Uncertainties

- The largest unresolved gap is entity identification for Kona, which lowers confidence in any conclusion that requires a direct Kona-versus-Aleph technical comparison. [inference; source: https://lean-lang.org/; https://arxiv.org/abs/2501.18639; https://github.com/apps/aleph-prover]
- Aleph's public sources document interfaces and workflow clearly, but they do not expose enough backend detail to evaluate internal search strategy, benchmark methodology, or service reliability in depth. [fact; source: https://github.com/apps/aleph-prover; https://pypi.org/project/alephprover/; https://github.com/logical-intelligence/proofs]
- The public evidence base says more about Lean's trust model than about Aleph's empirical performance, so practical tool-choice decisions still need benchmark and workflow evidence beyond marketing or README-level claims. [inference; source: https://lean-lang.org/; https://doi.org/10.1007/978-3-030-79876-5_37; https://github.com/apps/aleph-prover]

### Open Questions

1. Which exact official Kona project, repository, or paper did the original request intend?
2. How does Aleph perform on shared Lean benchmarks relative to Lean Copilot, ReProver, and other public systems?
3. What review and approval workflow is most effective when hosted proof services open pull requests against live Lean repositories?
4. Which classes of proof task are best served by in-editor copilots versus asynchronous hosted proof services?

---

## Output

- Type: knowledge
- Description: This item establishes a conservative conceptual map in which Lean is the verified substrate, Aleph is a hosted automation layer above that substrate, and Kona remains unresolved pending an authoritative public source. [inference; source: https://lean-lang.org/; https://github.com/apps/aleph-prover; https://pypi.org/project/alephprover/]
- Links:
- https://lean-lang.org/
- https://github.com/apps/aleph-prover
- https://pypi.org/project/alephprover/
