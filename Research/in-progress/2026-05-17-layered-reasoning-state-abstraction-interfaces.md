---
review_count: 1
title: "Layered reasoning stack interfaces: state abstraction and Large Language Model (LLM) ↔ Energy-Based Model (EBM) protocols"
added: 2026-05-17T11:18:46+00:00
status: reviewing
priority: high
blocks: []
tags: [agentic-ai, llm, invariants, workflow, formal-methods]
started: 2026-05-17T13:41:59+00:00
completed: ~
output: [knowledge]
cites:
  - 2026-05-09-hybrid-architecture-probabilistic-llm-deterministic-governance
  - 2026-04-26-ai-agent-control-plane-architecture-enterprise
  - 2026-03-10-language-for-llm-agent-output
  - 2026-04-26-llm-verifiability-asymmetry-code-world-action
  - 2026-05-17-deterministic-circuit-breakers-hybrid-reasoning-infrastructure
related:
  - 2026-04-26-ai-lowcode-governance-enforcement-architecture
  - 2026-04-26-policy-coherence-machine-checkable-prerequisite
  - 2026-05-09-governance-policy-determinism-vs-stochastic-llm
superseded_by: ~
supersedes: ~
item_type: primary
confidence: medium
versions: []
---

# Layered reasoning stack interfaces: state abstraction and Large Language Model (LLM) ↔ Energy-Based Model (EBM) protocols

## Research Question

What state abstraction boundaries and interface protocols are most effective for mapping Large Language Model (LLM) candidate outputs into Energy-Based Model (EBM) evaluation state spaces while preserving all policy-relevant constraints and minimizing non-functional variance?

## Scope

**In scope:**
- Lossy-but-sufficient state representations for plans, code, and natural language
- Abstract Syntax Tree (AST), graph, and schema options for policy-relevant state mapping
- Interface contracts for round-tripping between generative and energy-evaluation layers
- Asynchronous EBM feedback strategies that avoid full regeneration loops

**Out of scope:**
- Model pretraining or fine-tuning procedures
- Vendor-specific deployment details for one cloud provider
- Full policy language semantics, covered in the policy and formal verification item

**Constraints:** Focus on methods that can be implemented in production orchestration systems with auditable transformation steps.

## Context

This item isolates the interface and representation problem so architecture teams can choose tractable state schemas before investing in policy engines or infrastructure control patterns. [inference; source: https://davidamitchell.github.io/Research/research/2026-05-09-hybrid-architecture-probabilistic-llm-deterministic-governance.html; https://davidamitchell.github.io/Research/research/2026-04-26-ai-agent-control-plane-architecture-enterprise.html; https://davidamitchell.github.io/Research/research/2026-03-10-language-for-llm-agent-output.html]

## Approach

1. What invariants define a lossy-but-sufficient representation that still preserves all enforceable constraints?
   1a. Which constraint classes are mandatory to preserve?
   1b. Which non-functional variance can be safely discarded?
2. Which representation forms best support EBM scoring and optimization?
   2a. How do AST, graph, and typed-schema forms compare for policy alignment?
   2b. What metadata is required for deterministic reconstruction and audit?
3. What interface protocol should connect LLM output and EBM scoring?
   3a. How should candidate generation, normalization, and scoring payloads be versioned?
   3b. What failure modes appear in forward and reverse translation?
4. How can asynchronous EBM feedback guide generation without full re-generation?
   4a. What scalar feedback channels are stable in practice?
   4b. What convergence diagnostics should terminate or continue generation?

## Sources

- [ ] [LeCun et al. (2006) A Tutorial on Energy-Based Learning](http://yann.lecun.com/exdb/publis/pdf/lecun-06.pdf) - identified from the seed list but not directly consulted because the page returned raw Portable Document Format (PDF) bytes without extractable text in this runtime
- [x] [LeCun (2022) A Path Towards Autonomous Machine Intelligence](https://openreview.net/forum?id=BZ5a1r-kVsf)
- [x] [Dawid and LeCun (2023) Introduction to Latent Variable Energy-Based Models: A Path Towards Autonomous Machine Intelligence](https://arxiv.org/abs/2306.02572)
- [x] [OpenAI Structured Outputs](https://developers.openai.com/api/docs/guides/structured-outputs)
- [x] [Model Context Protocol Specification](https://modelcontextprotocol.io/specification/2025-06-18/)
- [x] [Model Context Protocol Architecture overview](https://modelcontextprotocol.io/docs/learn/architecture.md)
- [x] [Model Context Protocol Versioning](https://modelcontextprotocol.io/docs/learn/versioning.md)
- [x] [Cousot and Cousot (1977) Abstract interpretation: a unified lattice model for static analysis of programs by construction or approximation of fixpoints](https://www.di.ens.fr/~cousot/COUSOTpapers/POPL77.shtml)
- [x] [JSON Schema What is JavaScript Object Notation (JSON) Schema?](https://json-schema.org/overview/what-is-jsonschema)
- [x] [JSON Schema JavaScript Object Notation (JSON) Schema Specification](https://json-schema.org/specification.html)
- [x] [Python Software Foundation Abstract Syntax Trees](https://docs.python.org/3/library/ast.html)
- [x] [LibCST Why LibCST for Concrete Syntax Trees](https://libcst.readthedocs.io/en/latest/why_libcst.html)
- [x] [Internet Engineering Task Force (IETF) Request for Comments (RFC) 6902 JavaScript Object Notation (JSON) Patch](https://datatracker.ietf.org/doc/html/rfc6902)
- [x] [Internet Engineering Task Force (IETF) Request for Comments (RFC) 7396 JSON Merge Patch](https://datatracker.ietf.org/doc/html/rfc7396)
- [x] [Allamanis et al. (2018) Learning to Represent Programs with Graphs](https://arxiv.org/abs/1711.00740)
- [x] [Mitchell (2026) Hybrid Architecture Design: Probabilistic Large Language Models (LLMs) for Interpretation, Deterministic Layers for Governance Enforcement](https://davidamitchell.github.io/Research/research/2026-05-09-hybrid-architecture-probabilistic-llm-deterministic-governance.html)
- [x] [Mitchell (2026) What control-plane architecture is required to manage Artificial Intelligence (AI) agents and low-code systems as distributed, semi-autonomous actors within enterprise environments?](https://davidamitchell.github.io/Research/research/2026-04-26-ai-agent-control-plane-architecture-enterprise.html)
- [x] [Mitchell (2026) Language designed for LLM agents to produce: addressing generation-layer failure modes in agentic systems](https://davidamitchell.github.io/Research/research/2026-03-10-language-for-llm-agent-output.html)
- [x] [Mitchell (2026) What is the precise technical distinction between code generation and other Large Language Model outputs in terms of external verifiability, and what does this asymmetry imply for safe deployment boundaries in a regulated financial institution?](https://davidamitchell.github.io/Research/research/2026-04-26-llm-verifiability-asymmetry-code-world-action.html)
- [x] [Mitchell (2026) Deterministic circuit-breakers and real-time infrastructure constraints for hybrid reasoning stacks](https://davidamitchell.github.io/Research/research/2026-05-17-deterministic-circuit-breakers-hybrid-reasoning-infrastructure.html)

## Related

- [Mitchell (2026) Hybrid Architecture Design: Probabilistic Large Language Models (LLMs) for Interpretation, Deterministic Layers for Governance Enforcement](https://davidamitchell.github.io/Research/research/2026-05-09-hybrid-architecture-probabilistic-llm-deterministic-governance.html)
- [Mitchell (2026) Deterministic circuit-breakers and real-time infrastructure constraints for hybrid reasoning stacks](https://davidamitchell.github.io/Research/research/2026-05-17-deterministic-circuit-breakers-hybrid-reasoning-infrastructure.html)
- [Mitchell (2026) Language designed for LLM agents to produce: addressing generation-layer failure modes in agentic systems](https://davidamitchell.github.io/Research/research/2026-03-10-language-for-llm-agent-output.html)

---

## Research Skill Output

*(Full output from running the research skill, retained verbatim in the completed item. Sections 0-5 are the investigation, and section 6 seeds the Findings section below.)*

### §0 Initialise

- Question: determine which abstractions and interface contracts let a generative layer emit candidates that an Energy-Based Model can score against policy-relevant constraints without carrying unnecessary surface variance.
- Scope: plans, code, and natural-language candidates; representation choices across JavaScript Object Notation (JSON) Schema, Abstract Syntax Tree (AST), graph, and lossless syntax forms; forward and reverse translation; asynchronous feedback; auditable production orchestration.
- Constraints: production systems only, explicit audit fields, full research mode, no attempt to solve full policy-language semantics.
- Output: full section 0 to section 7 investigation plus Findings with Executive Summary, Key Findings, Evidence Map, Assumptions, Analysis, Risks, Gaps, Uncertainties, Open Questions, and Output.
- [fact; source: https://davidamitchell.github.io/Research/research/2026-05-09-hybrid-architecture-probabilistic-llm-deterministic-governance.html; https://davidamitchell.github.io/Research/research/2026-04-26-ai-agent-control-plane-architecture-enterprise.html; https://davidamitchell.github.io/Research/research/2026-03-10-language-for-llm-agent-output.html; https://davidamitchell.github.io/Research/research/2026-04-26-llm-verifiability-asymmetry-code-world-action.html] Prior completed-item cross-reference: adjacent repository work already establishes four premises used here, namely that the generative layer should emit structured proposals, that deterministic governance sits on a separate control plane, that output formats for agentic systems should be machine-checkable rather than free-form, and that verifier pipelines require externally checkable state rather than prose alone.
- [fact; source: https://www.di.ens.fr/~cousot/COUSOTpapers/POPL77.shtml] Working definition: an abstraction is adequate when it preserves the properties of interest for the downstream analysis rather than reproducing the entire concrete state.
- [fact; source: https://openreview.net/forum?id=BZ5a1r-kVsf; https://arxiv.org/abs/2306.02572] Working definition: the relevant EBM-side state is a multi-level representation of percepts or action plans that supports reasoning and planning over abstract structure rather than over raw token sequences.

### §1 Question Decomposition

- **Root question:** what interface boundary lets an LLM emit candidates that an EBM can score, patch, and reject using stable policy-relevant state rather than brittle surface text?
- **A. Abstraction target**
  - A1. Which state properties must survive normalization because deterministic governance or energy scoring depends on them?
  - A2. Which surface features can be discarded without changing any enforceable decision?
- **B. Representation choice**
  - B1. What does a typed schema preserve well?
  - B2. What does an AST or Concrete Syntax Tree (CST) preserve well?
  - B3. What does a graph preserve well?
  - B4. Which combination gives the best trade-off for plans, code, and natural language?
- **C. Interface contract**
  - C1. How should candidate, normalization, scoring, and feedback payloads be structured?
  - C2. How should versioning and capability negotiation work?
  - C3. What metadata is mandatory for reconstruction and audit?
- **D. Feedback loop**
  - D1. Which partial-update channels allow local correction instead of full regeneration?
  - D2. Which scalar signals are stable enough to drive iterative improvement?
  - D3. Which diagnostics indicate convergence, stall, or fail-closed fallback?

### §2 Investigation

#### 2.1 Source access and replacement notes

- [assumption; source: https://openreview.net/forum?id=BZ5a1r-kVsf; https://arxiv.org/abs/2306.02572] Access note: the seeded `arXiv:2006.02562` link did not resolve to LeCun's architecture paper, so the accessible OpenReview 2022 paper and the 2023 LeCun co-authored energy-based notes were used instead.
- [assumption; source: https://openreview.net/forum?id=BZ5a1r-kVsf; https://arxiv.org/abs/2306.02572] Access note: the seeded 2006 EBM tutorial returned raw Portable Document Format bytes in this runtime, so extractable EBM claims were taken from the accessible 2022 and 2023 LeCun sources.
- [assumption; source: https://developers.openai.com/api/docs/guides/structured-outputs] Access note: the seeded OpenAI blog URL returned `403`, so the current official OpenAI developer guide for Structured Outputs was used as the primary source for schema-constrained generation claims.

#### 2.2 Prior completed-item sweep

- [fact; source: https://davidamitchell.github.io/Research/research/2026-05-09-hybrid-architecture-probabilistic-llm-deterministic-governance.html] The prior hybrid-architecture item concluded that the safe boundary between generation and enforcement is a schema-constrained proposal record rather than free-form text.
- [fact; source: https://davidamitchell.github.io/Research/research/2026-04-26-ai-agent-control-plane-architecture-enterprise.html] The prior control-plane item concluded that policy decisions depend on normalized policy inputs, translation services, and separate enforcement points instead of prompt-only governance.
- [fact; source: https://davidamitchell.github.io/Research/research/2026-03-10-language-for-llm-agent-output.html] The prior output-language item concluded that typed or grammar-constrained outputs reduce structural generation failures but do not by themselves solve semantic or goal-level errors.
- [fact; source: https://davidamitchell.github.io/Research/research/2026-04-26-llm-verifiability-asymmetry-code-world-action.html] The prior verifiability item concluded that outputs become governable only when they can enter an external verifier pipeline with machine-checkable state.
- [inference; source: https://davidamitchell.github.io/Research/research/2026-05-09-hybrid-architecture-probabilistic-llm-deterministic-governance.html; https://davidamitchell.github.io/Research/research/2026-03-10-language-for-llm-agent-output.html; https://davidamitchell.github.io/Research/research/2026-04-26-llm-verifiability-asymmetry-code-world-action.html] This item extends those findings from "use a structured proposal" to the narrower question of which normalized state should cross the boundary and how that state should evolve under iterative EBM feedback.

#### 2.3 What a policy-preserving abstraction must keep

- [fact; source: https://www.di.ens.fr/~cousot/COUSOTpapers/POPL77.shtml] Cousot and Cousot define abstract interpretation as computing over abstract objects that preserve only the properties needed for the question being asked, rather than preserving the full concrete execution.
- [fact; source: https://openreview.net/forum?id=BZ5a1r-kVsf] LeCun's 2022 paper asks for representations of percepts and action plans at multiple levels of abstraction so a system can reason, predict, and plan at multiple time horizons.
- [fact; source: https://arxiv.org/abs/2306.02572] Dawid and LeCun's 2023 notes say the future autonomous-intelligence architecture combines energy-based and latent-variable models inside a hierarchical representation stack rather than using one flat representation.
- [inference; source: https://www.di.ens.fr/~cousot/COUSOTpapers/POPL77.shtml; https://openreview.net/forum?id=BZ5a1r-kVsf; https://arxiv.org/abs/2306.02572; https://davidamitchell.github.io/Research/research/2026-05-09-hybrid-architecture-probabilistic-llm-deterministic-governance.html; https://davidamitchell.github.io/Research/research/2026-04-26-ai-agent-control-plane-architecture-enterprise.html] For this interface problem, the preserved invariants are the fields that affect whether an action is valid, safe, attributable, and reconstructible: actor or machine identity, intended action, target surface, argument values and types, dependency edges, side-effect class, risk or approval state, deadline or budget, and provenance identifiers.
- [inference; source: https://www.di.ens.fr/~cousot/COUSOTpapers/POPL77.shtml; https://docs.python.org/3/library/ast.html; https://libcst.readthedocs.io/en/latest/why_libcst.html; https://datatracker.ietf.org/doc/html/rfc7396] Non-functional variance can be discarded only after any policy-bearing detail is surfaced elsewhere, so whitespace, comment placement, stylistic paraphrase, and semantically irrelevant field ordering are safe to drop only when provenance, annotations, and formatting-sensitive semantics have already been extracted into explicit fields.

#### 2.4 What typed schemas, syntax trees, and graphs each preserve

- [fact; source: https://json-schema.org/overview/what-is-jsonschema; https://json-schema.org/specification.html] JSON Schema is a declarative language for defining the structure and constraints of JSON data, and validators check whether an instance conforms to the schema.
- [fact; source: https://developers.openai.com/api/docs/guides/structured-outputs] OpenAI Structured Outputs says the model can be constrained to adhere to a supplied JSON Schema, making missing required keys and invalid enumeration values programmatically detectable.
- [fact; source: https://docs.python.org/3/library/ast.html] Python's `ast` module represents the abstract syntax grammar of code and produces a structural tree suitable for compilation and programmatic inspection.
- [fact; source: https://libcst.readthedocs.io/en/latest/why_libcst.html] LibCST documents the trade-off that an AST preserves code semantics but is lossy with respect to comments, whitespace, and exact source printing, while a lossless CST preserves those surface details.
- [fact; source: https://arxiv.org/abs/1711.00740] Allamanis et al. represent programs as graphs that combine syntactic and semantic structure, and state that less structured program representations miss long-range dependencies such as variable use across distant locations.
- [inference; source: https://json-schema.org/overview/what-is-jsonschema; https://developers.openai.com/api/docs/guides/structured-outputs; https://docs.python.org/3/library/ast.html; https://libcst.readthedocs.io/en/latest/why_libcst.html; https://arxiv.org/abs/1711.00740] No single representation is sufficient across the full boundary: typed schemas are best for portable interchange and validation, AST or CST views are best for syntax-aware normalization and faithful reconstruction of code, and graph views are best for cross-node dependency, control, and resource relations that matter to energy scoring.
- [inference; source: https://davidamitchell.github.io/Research/research/2026-03-10-language-for-llm-agent-output.html; https://arxiv.org/abs/1711.00740; https://json-schema.org/overview/what-is-jsonschema] The practical abstraction boundary is therefore multi-view, with a canonical typed envelope as the interchange contract and optional AST or graph projections attached or derivable for domains where syntax fidelity or dependency reasoning matters.

#### 2.5 What the interface protocol must do

- [fact; source: https://modelcontextprotocol.io/specification/2025-06-18/; https://modelcontextprotocol.io/docs/learn/architecture.md] Model Context Protocol (MCP) is a stateful protocol built on JavaScript Object Notation Remote Procedure Call (JSON-RPC) 2.0 with lifecycle management, capability negotiation, structured tools or resources, progress tracking, cancellation, and error reporting.
- [fact; source: https://modelcontextprotocol.io/docs/learn/versioning.md] MCP uses date-based string version identifiers, allows clients and servers to support multiple versions, and requires the session to agree on a single version during initialization.
- [fact; source: https://developers.openai.com/api/docs/guides/structured-outputs] OpenAI distinguishes between structured responses to the user and structured function-calling for tool invocation, which is a concrete example of separating interchange contract from execution channel.
- [inference; source: https://modelcontextprotocol.io/specification/2025-06-18/; https://modelcontextprotocol.io/docs/learn/versioning.md; https://developers.openai.com/api/docs/guides/structured-outputs; https://davidamitchell.github.io/Research/research/2026-04-26-ai-agent-control-plane-architecture-enterprise.html] The LLM to EBM boundary should use a versioned candidate envelope that carries at least `candidate_id`, `schema_version`, `capability_profile`, `normalization_trace`, `canonical_state`, `provenance`, and `expected_side_effect_class`, so every score or rejection is anchored to one negotiated interface and one auditable state snapshot.
- [inference; source: https://davidamitchell.github.io/Research/research/2026-04-26-llm-verifiability-asymmetry-code-world-action.html; https://davidamitchell.github.io/Research/research/2026-05-09-hybrid-architecture-probabilistic-llm-deterministic-governance.html; https://modelcontextprotocol.io/specification/2025-06-18/] The normalization stage should be explicit and logged rather than hidden inside either model call, because external verifiability depends on being able to reconstruct how free-form candidate material became scoreable state.

#### 2.6 What asynchronous feedback should look like

- [fact; source: https://datatracker.ietf.org/doc/html/rfc6902] JSON Patch defines ordered `add`, `remove`, `replace`, `move`, `copy`, and `test` operations for partial updates to JSON documents.
- [fact; source: https://datatracker.ietf.org/doc/html/rfc7396] JSON Merge Patch describes object-shaped partial updates by example, replaces members recursively, treats `null` as deletion, and is not appropriate for all JSON syntaxes, especially when array-local edits matter.
- [fact; source: https://davidamitchell.github.io/Research/research/2026-05-17-deterministic-circuit-breakers-hybrid-reasoning-infrastructure.html] The deterministic-circuit-breakers companion item concludes that iterative reasoning on a live control path must respect bounded deadlines, stable fallback states, and explicit continuation or stop rules.
- [inference; source: https://datatracker.ietf.org/doc/html/rfc6902; https://datatracker.ietf.org/doc/html/rfc7396; https://davidamitchell.github.io/Research/research/2026-05-17-deterministic-circuit-breakers-hybrid-reasoning-infrastructure.html] Asynchronous EBM feedback should therefore prefer localized repair channels over whole-output replacement: per-field or per-subgraph energy terms, invariant-violation lists, JSON Patch for precise tree edits, and JSON Merge Patch only for object-dominant states where array surgery is not needed.
- [inference; source: https://datatracker.ietf.org/doc/html/rfc6902; https://developers.openai.com/api/docs/guides/structured-outputs; https://davidamitchell.github.io/Research/research/2026-05-17-deterministic-circuit-breakers-hybrid-reasoning-infrastructure.html] Stable scalar channels are totals and deltas tied to named constraint families, such as syntax validity, policy coverage, dependency consistency, and side-effect risk, because opaque single-number energies are too hard to debug under production deadlines.

#### 2.7 Convergence and failure diagnostics

- [fact; source: https://modelcontextprotocol.io/specification/2025-06-18/; https://modelcontextprotocol.io/docs/learn/architecture.md] MCP exposes cancellation, progress, and structured error reporting as first-class protocol utilities.
- [fact; source: https://davidamitchell.github.io/Research/research/2026-05-17-deterministic-circuit-breakers-hybrid-reasoning-infrastructure.html] The infrastructure companion item treats missed deadlines, repeated failures, and unstable search progress as reasons to revoke advanced-controller authority.
- [inference; source: https://modelcontextprotocol.io/specification/2025-06-18/; https://davidamitchell.github.io/Research/research/2026-05-17-deterministic-circuit-breakers-hybrid-reasoning-infrastructure.html; https://datatracker.ietf.org/doc/html/rfc6902] The interface should terminate or continue based on observable diagnostics rather than model confidence alone: validator fixed point reached, net energy improvement below threshold for `n` rounds, repeated patch cycles on the same path, budget exhaustion, contradiction count not decreasing, or policy-critical violation still present after repair.

### §3 Reasoning

- [fact; source: https://www.di.ens.fr/~cousot/COUSOTpapers/POPL77.shtml] The research question is not "which representation is richest" but "which abstraction preserves the properties the EBM and policy stack actually score."
- [fact; source: https://json-schema.org/overview/what-is-jsonschema; https://docs.python.org/3/library/ast.html; https://libcst.readthedocs.io/en/latest/why_libcst.html; https://arxiv.org/abs/1711.00740] The evidence shows that schemas, syntax trees, and graphs preserve different property families, so forcing one form to do all three jobs creates either blind spots or unnecessary variance.
- [inference; source: https://json-schema.org/overview/what-is-jsonschema; https://arxiv.org/abs/1711.00740; https://developers.openai.com/api/docs/guides/structured-outputs] The boundary object should therefore be typed first and richer by attachment, meaning a canonical schema envelope with optional AST or graph views instead of multiple peer representations competing for authority.
- [inference; source: https://datatracker.ietf.org/doc/html/rfc6902; https://datatracker.ietf.org/doc/html/rfc7396; https://davidamitchell.github.io/Research/research/2026-05-17-deterministic-circuit-breakers-hybrid-reasoning-infrastructure.html] Partial feedback is superior to full regeneration whenever the failure is local and the system is deadline-sensitive, because it preserves already-validated state and shortens the control loop.
- [assumption; source: https://modelcontextprotocol.io/specification/2025-06-18/; https://davidamitchell.github.io/Research/research/2026-05-09-hybrid-architecture-probabilistic-llm-deterministic-governance.html] Production orchestrators can record normalization traces and candidate identifiers for every round. **Justification:** without that assumption, the recommended audit and patch loop would degrade into opaque retry behavior rather than a governable interface.

### §4 Consistency Check

- [fact; source: https://docs.python.org/3/library/ast.html; https://libcst.readthedocs.io/en/latest/why_libcst.html] AST and CST evidence is internally consistent: ASTs are concise semantic structures, while CSTs preserve exact source form and comments.
- [fact; source: https://json-schema.org/overview/what-is-jsonschema; https://arxiv.org/abs/1711.00740] Schema and graph evidence is also consistent: schemas constrain local field structure, while graphs capture non-local program or plan relations.
- [inference; source: https://docs.python.org/3/library/ast.html; https://json-schema.org/overview/what-is-jsonschema; https://arxiv.org/abs/1711.00740] These representations are complementary rather than contradictory, so the recommendation becomes layered composition rather than winner-take-all selection.
- [inference; source: https://datatracker.ietf.org/doc/html/rfc6902; https://datatracker.ietf.org/doc/html/rfc7396] Patch and merge-patch evidence is also non-conflicting once scope is narrowed: JSON Patch is the precise edit format, while JSON Merge Patch is the simpler object-level shortcut.

### §5 Depth and Breadth Expansion

- [inference; source: https://arxiv.org/abs/1711.00740; https://docs.python.org/3/library/ast.html] Technical lens: graph augmentation matters most when constraint violations depend on cross-reference, aliasing, or ordering relations that a plain tree or schema would not expose.
- [inference; source: https://modelcontextprotocol.io/docs/learn/versioning.md; https://modelcontextprotocol.io/specification/2025-06-18/] Operational lens: date-versioned contracts and capability negotiation reduce upgrade ambiguity and let orchestrators reject unsupported candidate shapes before scoring begins.
- [inference; source: https://datatracker.ietf.org/doc/html/rfc6902; https://davidamitchell.github.io/Research/research/2026-05-17-deterministic-circuit-breakers-hybrid-reasoning-infrastructure.html] Economic lens: localized repair should lower compute and latency costs whenever only a small part of the state violates constraints, because the system avoids regenerating already-acceptable structure.
- [inference; source: https://www.di.ens.fr/~cousot/COUSOTpapers/POPL77.shtml; https://openreview.net/forum?id=BZ5a1r-kVsf] Historical lens: both abstract interpretation and LeCun's multi-level reasoning framing argue against raw-token interfaces and toward explicit intermediate abstractions tied to the questions the downstream system can answer.
- [inference; source: https://developers.openai.com/api/docs/guides/structured-outputs; https://davidamitchell.github.io/Research/research/2026-05-09-hybrid-architecture-probabilistic-llm-deterministic-governance.html] Behavioural lens: typed contracts narrow the surface on which the generator can hide ambiguity, which makes human review and deterministic scoring more reliable than reviewing a persuasive narrative.

### §6 Synthesis

**Executive summary:**

The most effective boundary is a layered canonical-state interface in which the Large Language Model emits a typed proposal envelope, normalization extracts policy-relevant invariants into canonical fields, and the Energy-Based Model scores that canonical state rather than raw text. [inference; source: https://www.di.ens.fr/~cousot/COUSOTpapers/POPL77.shtml; https://developers.openai.com/api/docs/guides/structured-outputs; https://davidamitchell.github.io/Research/research/2026-05-09-hybrid-architecture-probabilistic-llm-deterministic-governance.html]

No single representation is enough across plans, code, and natural language: JavaScript Object Notation (JSON) Schema is best as the portable interchange contract, Abstract Syntax Tree or Concrete Syntax Tree views are best when syntax fidelity or reconstruction matters, and graph projections are best for dependency and control relations that span distant nodes. [inference; source: https://json-schema.org/overview/what-is-jsonschema; https://docs.python.org/3/library/ast.html; https://libcst.readthedocs.io/en/latest/why_libcst.html; https://arxiv.org/abs/1711.00740]

The protocol should be stateful and versioned, carry provenance and normalization traces, and return localized repair signals such as invariant-specific energy terms and JavaScript Object Notation (JSON) Patch operations instead of forcing full regeneration on every miss. [inference; source: https://modelcontextprotocol.io/specification/2025-06-18/; https://modelcontextprotocol.io/docs/learn/versioning.md; https://datatracker.ietf.org/doc/html/rfc6902; https://davidamitchell.github.io/Research/research/2026-05-17-deterministic-circuit-breakers-hybrid-reasoning-infrastructure.html]

**Key findings:**

1. **The boundary should preserve only the fields that change a deterministic decision, namely identity, intended action, target surface, typed arguments, dependency edges, side-effect class, risk or approval state, budget or deadline, and provenance identifiers, while stripping presentation-only surface form.** ([inference]; high confidence; source: https://www.di.ens.fr/~cousot/COUSOTpapers/POPL77.shtml; https://openreview.net/forum?id=BZ5a1r-kVsf; https://davidamitchell.github.io/Research/research/2026-04-26-ai-agent-control-plane-architecture-enterprise.html)
2. **A canonical typed schema should be the authoritative interchange object because schema validators and structured-generation runtimes can reject malformed or underspecified boundary states before they enter the scoring or execution path.** ([inference]; medium confidence; source: https://json-schema.org/overview/what-is-jsonschema; https://developers.openai.com/api/docs/guides/structured-outputs)
3. **Code-oriented candidates still need an Abstract Syntax Tree or lossless Concrete Syntax Tree view behind that schema envelope, because schema fields alone do not preserve syntax-sensitive semantics, faithful reconstruction, comments, or formatting-dependent audit trails.** ([inference]; high confidence; source: https://docs.python.org/3/library/ast.html; https://libcst.readthedocs.io/en/latest/why_libcst.html)
4. **Plan and code candidates that contain long-range control, data, or resource dependencies should expose a graph projection in addition to tree or schema views, because graph representations capture semantic relations that flatter structures routinely hide.** ([inference]; medium confidence; source: https://arxiv.org/abs/1711.00740; https://davidamitchell.github.io/Research/research/2026-03-10-language-for-llm-agent-output.html)
5. **The protocol between generation and scoring should be stateful, version-negotiated, and explicitly trace normalization, because without one agreed contract version and one reconstruction trail the scored state cannot be audited or compared across iterations.** ([inference]; high confidence; source: https://modelcontextprotocol.io/specification/2025-06-18/; https://modelcontextprotocol.io/docs/learn/versioning.md; https://davidamitchell.github.io/Research/research/2026-04-26-llm-verifiability-asymmetry-code-world-action.html)
6. **Asynchronous EBM guidance should return localized repair artifacts such as invariant-family scores, named violations, and JavaScript Object Notation (JSON) Patch operations, because partial repair preserves validated substructure and shortens deadline-sensitive loops better than unconditional full regeneration when failures are local.** ([inference]; medium confidence; source: https://datatracker.ietf.org/doc/html/rfc6902; https://datatracker.ietf.org/doc/html/rfc7396; https://davidamitchell.github.io/Research/research/2026-05-17-deterministic-circuit-breakers-hybrid-reasoning-infrastructure.html)
7. **The loop should continue only while observable diagnostics improve, such as validator coverage, aggregate energy, contradiction count, or unresolved critical violations, and it should fail closed when progress stalls, deadlines expire, or the same patch path oscillates.** ([inference]; medium confidence; source: https://modelcontextprotocol.io/specification/2025-06-18/; https://davidamitchell.github.io/Research/research/2026-05-17-deterministic-circuit-breakers-hybrid-reasoning-infrastructure.html; https://datatracker.ietf.org/doc/html/rfc6902)

**Evidence map:**

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [inference] Preserve only decision-relevant invariants and discard presentation-only variance. | https://www.di.ens.fr/~cousot/COUSOTpapers/POPL77.shtml; https://openreview.net/forum?id=BZ5a1r-kVsf; https://davidamitchell.github.io/Research/research/2026-04-26-ai-agent-control-plane-architecture-enterprise.html | High | Abstract interpretation plus prior control-plane findings define the preserved property class. |
| [inference] Typed schema should be the authoritative interchange contract. | https://json-schema.org/overview/what-is-jsonschema; https://developers.openai.com/api/docs/guides/structured-outputs | Medium | Validators and structured outputs support schema-first interchange, but the cross-representation choice is still architectural synthesis. |
| [inference] Code still needs AST or CST views for syntax fidelity and reconstruction. | https://docs.python.org/3/library/ast.html; https://libcst.readthedocs.io/en/latest/why_libcst.html | High | AST is lossy for formatting, CST is lossless but noisier. |
| [inference] Graph projections are needed for long-range semantic constraints. | https://arxiv.org/abs/1711.00740; https://davidamitchell.github.io/Research/research/2026-03-10-language-for-llm-agent-output.html | Medium | Graph evidence is strongest for code semantics; extension to plans is inferential. |
| [inference] The protocol must be stateful, versioned, and normalization-aware. | https://modelcontextprotocol.io/specification/2025-06-18/; https://modelcontextprotocol.io/docs/learn/versioning.md; https://davidamitchell.github.io/Research/research/2026-04-26-llm-verifiability-asymmetry-code-world-action.html | High | Auditability requires one agreed protocol version and one reconstruction trail. |
| [inference] Partial repair via JSON Patch is better than full regeneration for local misses. | https://datatracker.ietf.org/doc/html/rfc6902; https://datatracker.ietf.org/doc/html/rfc7396; https://davidamitchell.github.io/Research/research/2026-05-17-deterministic-circuit-breakers-hybrid-reasoning-infrastructure.html | Medium | Patch semantics plus deadline-sensitive control-path evidence support localized repair, but the item does not cite an end-to-end benchmark. |
| [inference] Convergence should depend on observable improvement and fail closed on stall or oscillation. | https://modelcontextprotocol.io/specification/2025-06-18/; https://davidamitchell.github.io/Research/research/2026-05-17-deterministic-circuit-breakers-hybrid-reasoning-infrastructure.html; https://datatracker.ietf.org/doc/html/rfc6902 | Medium | The exact thresholds are design choices, but the need for explicit diagnostics is well supported. |

**Assumptions:**

- [assumption; source: https://modelcontextprotocol.io/specification/2025-06-18/; https://developers.openai.com/api/docs/guides/structured-outputs] Production orchestrators can attach a stable candidate identifier and schema version to every candidate round. Justification: without that capability, version-safe patching and replay become ambiguous.
- [assumption; source: https://davidamitchell.github.io/Research/research/2026-05-17-deterministic-circuit-breakers-hybrid-reasoning-infrastructure.html; https://datatracker.ietf.org/doc/html/rfc6902] Most costly misses in the target deployment are local enough that partial repair saves time over full regeneration. Justification: if misses are usually global, patch feedback would add complexity without enough latency benefit.

**Analysis:**

The evidence supports a layered rather than monolithic interface because each representation family answers a different control question. [inference; source: https://json-schema.org/overview/what-is-jsonschema; https://docs.python.org/3/library/ast.html; https://arxiv.org/abs/1711.00740]

Schemas are strong where the boundary needs stable field names, types, required keys, and validator-compatible interchange, but they are weak where the EBM must reason about aliasing, ordering, or long-range dependency. [inference; source: https://json-schema.org/overview/what-is-jsonschema; https://arxiv.org/abs/1711.00740]

AST and CST representations solve the inverse problem: they retain structure and, in the CST case, exact source fidelity, but they are poor as a cross-service contract unless their semantics are re-expressed as canonical fields. [inference; source: https://docs.python.org/3/library/ast.html; https://libcst.readthedocs.io/en/latest/why_libcst.html]

That trade-off makes the best design a canonical typed envelope with derivable or attached domain-specific projections rather than one universal representation. [inference; source: https://developers.openai.com/api/docs/guides/structured-outputs; https://docs.python.org/3/library/ast.html; https://arxiv.org/abs/1711.00740]

The same reasoning applies to feedback: when the problem is local, patch semantics plus named violation scores keep already-accepted structure intact and shorten the control loop; when the problem is global, the protocol should stop and request regeneration or safe fallback instead of pretending every miss is locally repairable. [inference; source: https://datatracker.ietf.org/doc/html/rfc6902; https://datatracker.ietf.org/doc/html/rfc7396; https://davidamitchell.github.io/Research/research/2026-05-17-deterministic-circuit-breakers-hybrid-reasoning-infrastructure.html]

**Risks, gaps, uncertainties:**

- [inference; source: https://www.di.ens.fr/~cousot/COUSOTpapers/POPL77.shtml; https://json-schema.org/overview/what-is-jsonschema; https://docs.python.org/3/library/ast.html; https://arxiv.org/abs/1711.00740; https://datatracker.ietf.org/doc/html/rfc6902] The consulted evidence base comes from adjacent literatures on abstract interpretation, schema validation, syntax trees, graph representations, and patch protocols rather than from one end-to-end benchmark that directly compares all three boundary forms inside an EBM-governed agent loop.
- [inference; source: https://arxiv.org/abs/1711.00740] The graph evidence is strongest for source code rather than for natural-language plans, so the recommendation to project plan state into graphs is best read as a bounded analogy from dependency-heavy code representations rather than as a directly benchmarked result.
- [inference; source: https://openreview.net/forum?id=BZ5a1r-kVsf; https://arxiv.org/abs/2306.02572] The item relies on LeCun's accessible 2022 and 2023 architecture papers rather than on the older tutorial text, so classic EBM interface terminology may be underrepresented even though the higher-level abstraction argument is still supported.
- [inference; source: https://modelcontextprotocol.io/specification/2025-06-18/; https://davidamitchell.github.io/Research/research/2026-05-17-deterministic-circuit-breakers-hybrid-reasoning-infrastructure.html] Exact scalar-threshold settings for convergence, oscillation, and stop conditions remain deployment-specific because the consulted protocol and infrastructure sources specify the need for explicit diagnostics and fail-closed behavior but do not prescribe one universal numeric threshold set.

**Open questions:**

- What minimum canonical field set supports both natural-language action plans and code patches without forcing two unrelated schemas?
- Which graph vocabulary is most useful for policy scoring over plans, dependency graphs, temporal graphs, or resource-access graphs?
- Can one EBM score both semantic validity and operational risk, or should those be separate energy terms combined only at the control layer?
- What benchmark would best measure whether patch-based feedback actually reduces latency and failure rate relative to full regeneration in production agent loops?

### §7 Recursive Review

- Review result: pass
- Acronym audit: Large Language Model (LLM), Energy-Based Model (EBM), Abstract Syntax Tree (AST), Concrete Syntax Tree (CST), JavaScript Object Notation (JSON), Model Context Protocol (MCP), and Portable Document Format (PDF) are expanded on first use in the document.
- Claim audit: visible factual claims are source-bound; evaluative claims remain labeled as inference; assumptions carry source-backed justification.
- Cross-item audit: findings that depend on adjacent completed items cite them with URL-backed links rather than repository-relative paths.
- Synthesis parity audit: section 6 and Findings use the same substantive claims, confidence levels, and source families.

---

## Findings

### Executive Summary

The most effective boundary is a layered canonical-state interface in which the Large Language Model emits a typed proposal envelope, normalization extracts policy-relevant invariants into canonical fields, and the Energy-Based Model scores that canonical state rather than raw text. [inference; source: https://www.di.ens.fr/~cousot/COUSOTpapers/POPL77.shtml; https://developers.openai.com/api/docs/guides/structured-outputs; https://davidamitchell.github.io/Research/research/2026-05-09-hybrid-architecture-probabilistic-llm-deterministic-governance.html]

No single representation is enough across plans, code, and natural language: JavaScript Object Notation (JSON) Schema is best as the portable interchange contract, Abstract Syntax Tree or Concrete Syntax Tree views are best when syntax fidelity or reconstruction matters, and graph projections are best for dependency and control relations that span distant nodes. [inference; source: https://json-schema.org/overview/what-is-jsonschema; https://docs.python.org/3/library/ast.html; https://libcst.readthedocs.io/en/latest/why_libcst.html; https://arxiv.org/abs/1711.00740]

The protocol should be stateful and versioned, carry provenance and normalization traces, and return localized repair signals such as invariant-specific energy terms and JavaScript Object Notation (JSON) Patch operations instead of forcing full regeneration on every miss. [inference; source: https://modelcontextprotocol.io/specification/2025-06-18/; https://modelcontextprotocol.io/docs/learn/versioning.md; https://datatracker.ietf.org/doc/html/rfc6902; https://davidamitchell.github.io/Research/research/2026-05-17-deterministic-circuit-breakers-hybrid-reasoning-infrastructure.html]

### Key Findings

1. **The boundary should preserve only the fields that change a deterministic decision, namely identity, intended action, target surface, typed arguments, dependency edges, side-effect class, risk or approval state, budget or deadline, and provenance identifiers, while stripping presentation-only surface form.** ([inference]; high confidence; source: https://www.di.ens.fr/~cousot/COUSOTpapers/POPL77.shtml; https://openreview.net/forum?id=BZ5a1r-kVsf; https://davidamitchell.github.io/Research/research/2026-04-26-ai-agent-control-plane-architecture-enterprise.html)
2. **A canonical typed schema should be the authoritative interchange object because schema validators and structured-generation runtimes can reject malformed or underspecified boundary states before they enter the scoring or execution path.** ([inference]; medium confidence; source: https://json-schema.org/overview/what-is-jsonschema; https://developers.openai.com/api/docs/guides/structured-outputs)
3. **Code-oriented candidates still need an Abstract Syntax Tree or lossless Concrete Syntax Tree view behind that schema envelope, because schema fields alone do not preserve syntax-sensitive semantics, faithful reconstruction, comments, or formatting-dependent audit trails.** ([inference]; high confidence; source: https://docs.python.org/3/library/ast.html; https://libcst.readthedocs.io/en/latest/why_libcst.html)
4. **Plan and code candidates that contain long-range control, data, or resource dependencies should expose a graph projection in addition to tree or schema views, because graph representations capture semantic relations that flatter structures routinely hide.** ([inference]; medium confidence; source: https://arxiv.org/abs/1711.00740; https://davidamitchell.github.io/Research/research/2026-03-10-language-for-llm-agent-output.html)
5. **The protocol between generation and scoring should be stateful, version-negotiated, and explicitly trace normalization, because without one agreed contract version and one reconstruction trail the scored state cannot be audited or compared across iterations.** ([inference]; high confidence; source: https://modelcontextprotocol.io/specification/2025-06-18/; https://modelcontextprotocol.io/docs/learn/versioning.md; https://davidamitchell.github.io/Research/research/2026-04-26-llm-verifiability-asymmetry-code-world-action.html)
6. **Asynchronous EBM guidance should return localized repair artifacts such as invariant-family scores, named violations, and JavaScript Object Notation (JSON) Patch operations, because partial repair preserves validated substructure and shortens deadline-sensitive loops better than unconditional full regeneration when failures are local.** ([inference]; medium confidence; source: https://datatracker.ietf.org/doc/html/rfc6902; https://datatracker.ietf.org/doc/html/rfc7396; https://davidamitchell.github.io/Research/research/2026-05-17-deterministic-circuit-breakers-hybrid-reasoning-infrastructure.html)
7. **The loop should continue only while observable diagnostics improve, such as validator coverage, aggregate energy, contradiction count, or unresolved critical violations, and it should fail closed when progress stalls, deadlines expire, or the same patch path oscillates.** ([inference]; medium confidence; source: https://modelcontextprotocol.io/specification/2025-06-18/; https://davidamitchell.github.io/Research/research/2026-05-17-deterministic-circuit-breakers-hybrid-reasoning-infrastructure.html; https://datatracker.ietf.org/doc/html/rfc6902)

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [inference] Preserve only decision-relevant invariants and discard presentation-only variance. | https://www.di.ens.fr/~cousot/COUSOTpapers/POPL77.shtml; https://openreview.net/forum?id=BZ5a1r-kVsf; https://davidamitchell.github.io/Research/research/2026-04-26-ai-agent-control-plane-architecture-enterprise.html | High | Abstract interpretation plus prior control-plane findings define the preserved property class. |
| [inference] Typed schema should be the authoritative interchange contract. | https://json-schema.org/overview/what-is-jsonschema; https://developers.openai.com/api/docs/guides/structured-outputs | Medium | Validators and structured outputs support schema-first interchange, but the cross-representation choice is still architectural synthesis. |
| [inference] Code still needs AST or CST views for syntax fidelity and reconstruction. | https://docs.python.org/3/library/ast.html; https://libcst.readthedocs.io/en/latest/why_libcst.html | High | AST is lossy for formatting, CST is lossless but noisier. |
| [inference] Graph projections are needed for long-range semantic constraints. | https://arxiv.org/abs/1711.00740; https://davidamitchell.github.io/Research/research/2026-03-10-language-for-llm-agent-output.html | Medium | Graph evidence is strongest for code semantics; extension to plans is inferential. |
| [inference] The protocol must be stateful, versioned, and normalization-aware. | https://modelcontextprotocol.io/specification/2025-06-18/; https://modelcontextprotocol.io/docs/learn/versioning.md; https://davidamitchell.github.io/Research/research/2026-04-26-llm-verifiability-asymmetry-code-world-action.html | High | Auditability requires one agreed protocol version and one reconstruction trail. |
| [inference] Partial repair via JSON Patch is better than full regeneration for local misses. | https://datatracker.ietf.org/doc/html/rfc6902; https://datatracker.ietf.org/doc/html/rfc7396; https://davidamitchell.github.io/Research/research/2026-05-17-deterministic-circuit-breakers-hybrid-reasoning-infrastructure.html | Medium | Patch semantics plus deadline-sensitive control-path evidence support localized repair, but the item does not cite an end-to-end benchmark. |
| [inference] Convergence should depend on observable improvement and fail closed on stall or oscillation. | https://modelcontextprotocol.io/specification/2025-06-18/; https://davidamitchell.github.io/Research/research/2026-05-17-deterministic-circuit-breakers-hybrid-reasoning-infrastructure.html; https://datatracker.ietf.org/doc/html/rfc6902 | Medium | The exact thresholds are design choices, but the need for explicit diagnostics is well supported. |

### Assumptions

- [assumption; source: https://modelcontextprotocol.io/specification/2025-06-18/; https://developers.openai.com/api/docs/guides/structured-outputs] Production orchestrators can attach a stable candidate identifier and schema version to every candidate round. Justification: without that capability, version-safe patching and replay become ambiguous.
- [assumption; source: https://davidamitchell.github.io/Research/research/2026-05-17-deterministic-circuit-breakers-hybrid-reasoning-infrastructure.html; https://datatracker.ietf.org/doc/html/rfc6902] Most costly misses in the target deployment are local enough that partial repair saves time over full regeneration. Justification: if misses are usually global, patch feedback would add complexity without enough latency benefit.

### Analysis

The evidence supports a layered rather than monolithic interface because each representation family answers a different control question. [inference; source: https://json-schema.org/overview/what-is-jsonschema; https://docs.python.org/3/library/ast.html; https://arxiv.org/abs/1711.00740]

Schemas are strong where the boundary needs stable field names, types, required keys, and validator-compatible interchange, but they are weak where the EBM must reason about aliasing, ordering, or long-range dependency. [inference; source: https://json-schema.org/overview/what-is-jsonschema; https://arxiv.org/abs/1711.00740]

AST and CST representations solve the inverse problem: they retain structure and, in the CST case, exact source fidelity, but they are poor as a cross-service contract unless their semantics are re-expressed as canonical fields. [inference; source: https://docs.python.org/3/library/ast.html; https://libcst.readthedocs.io/en/latest/why_libcst.html]

That trade-off makes the best design a canonical typed envelope with derivable or attached domain-specific projections rather than one universal representation. [inference; source: https://developers.openai.com/api/docs/guides/structured-outputs; https://docs.python.org/3/library/ast.html; https://arxiv.org/abs/1711.00740]

The same reasoning applies to feedback: when the problem is local, patch semantics plus named violation scores keep already-accepted structure intact and shorten the control loop; when the problem is global, the protocol should stop and request regeneration or safe fallback instead of pretending every miss is locally repairable. [inference; source: https://datatracker.ietf.org/doc/html/rfc6902; https://datatracker.ietf.org/doc/html/rfc7396; https://davidamitchell.github.io/Research/research/2026-05-17-deterministic-circuit-breakers-hybrid-reasoning-infrastructure.html]

### Risks, Gaps, and Uncertainties

- The consulted evidence base comes from adjacent literatures on abstract interpretation, schema validation, syntax trees, graph representations, and patch protocols rather than from one end-to-end benchmark that directly compares all three boundary forms inside an EBM-governed agent loop. [inference; source: https://www.di.ens.fr/~cousot/COUSOTpapers/POPL77.shtml; https://json-schema.org/overview/what-is-jsonschema; https://docs.python.org/3/library/ast.html; https://arxiv.org/abs/1711.00740; https://datatracker.ietf.org/doc/html/rfc6902]
- The graph evidence is strongest for source code rather than for natural-language plans, so the recommendation to project plan state into graphs is best read as a bounded analogy from dependency-heavy code representations rather than as a directly benchmarked result. [inference; source: https://arxiv.org/abs/1711.00740]
- The item relies on LeCun's accessible 2022 and 2023 architecture papers rather than on the older tutorial text, so classic EBM interface terminology may be underrepresented even though the higher-level abstraction argument is still supported. [inference; source: https://openreview.net/forum?id=BZ5a1r-kVsf; https://arxiv.org/abs/2306.02572]
- Exact scalar-threshold settings for convergence, oscillation, and stop conditions remain deployment-specific because the consulted protocol and infrastructure sources specify the need for explicit diagnostics and fail-closed behavior but do not prescribe one universal numeric threshold set. [inference; source: https://modelcontextprotocol.io/specification/2025-06-18/; https://davidamitchell.github.io/Research/research/2026-05-17-deterministic-circuit-breakers-hybrid-reasoning-infrastructure.html]

### Open Questions

- What minimum canonical field set supports both natural-language action plans and code patches without forcing two unrelated schemas?
- Which graph vocabulary is most useful for policy scoring over plans, dependency graphs, temporal graphs, or resource-access graphs?
- Can one EBM score both semantic validity and operational risk, or should those be separate energy terms combined only at the control layer?
- What benchmark would best measure whether patch-based feedback actually reduces latency and failure rate relative to full regeneration in production agent loops?

---

## Output

- Type: knowledge
- Description: Interface-design guidance for mapping generative candidates into auditable, policy-preserving EBM state using a canonical typed envelope with optional AST, CST, or graph projections and localized repair channels. [inference; source: https://www.di.ens.fr/~cousot/COUSOTpapers/POPL77.shtml; https://developers.openai.com/api/docs/guides/structured-outputs; https://datatracker.ietf.org/doc/html/rfc6902]
- Links:
  - https://www.di.ens.fr/~cousot/COUSOTpapers/POPL77.shtml
  - https://openreview.net/forum?id=BZ5a1r-kVsf
  - https://developers.openai.com/api/docs/guides/structured-outputs
