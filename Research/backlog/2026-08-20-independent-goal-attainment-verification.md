---
title: "Independent verification and durable evidence for goal attainment"
added: 2026-08-20T11:01:29+00:00
status: backlog
priority: high
blocks: []
themes: [formal-methods, governance-policy, benchmarks-eval, tools-infrastructure, regulatory-compliance]
started: ~
completed: ~
output: []
cites: [2026-04-22-ai-governance-assurance-change-control-verification, 2026-05-02-automated-claim-verification-academic-literature, 2026-04-27-cryptographic-intent-preservation-runtime-evaluation]
related: [2026-05-17-policy-enforcement-formal-verification-energy-functions, 2026-04-28-llm-as-judge-pipeline-validation-checkpoints, 2026-03-22-cross-scanner-compliance-evidence-normalisation]
superseded_by: ~
supersedes: ~
item_type: primary
confidence: medium
versions: []
---

# Independent verification and durable evidence for goal attainment

## Research Question

What reusable verification, assurance, logging, and audit mechanisms can determine whether a stated goal has been attained while remaining independent of any specific content pool or execution environment, and how should their reliability, evidence durability, and non-interference be evaluated?

## Scope

**In scope:**
- Deterministic verification procedures, evidence-based assurance patterns, immutable or tamper-evident logging, and independent audit mechanisms
- Checking primitives that can be invoked by any party inside or outside an active working context
- Criteria for evaluating reliability, replayability, tamper resistance, independence, and non-interference with the content and harness zones
- Mechanisms that produce durable evidence assertions rather than transient judgments only

**Out of scope:**
- Domain-specific policies for when or how verification results should be acted on
- Content-pool curation or execution-harness adaptation methods except where needed to prove non-interference
- Purely subjective review processes that do not yield reusable evidence artefacts

**Constraints:** Treat this zone as a provider of checking mechanisms rather than a decision-making authority. Prioritise reusable methods that can travel across domains, distinguish evidence generation from governance response, and evaluate whether the mechanism can stay independent of both the mediated content pool and the active execution environment.

## Context

This item informs how a third-zone validation layer can provide durable, domain-independent evidence that a goal was or was not met without becoming entangled in the content-pool or execution-harness design itself.

## Related

- [Automated governance assurance and change control verification patterns for AI-assisted delivery](https://davidamitchell.github.io/Research/research/2026-04-22-ai-governance-assurance-change-control-verification.html)
- [What automated claim verification approaches against scientific literature (arXiv) are used in research synthesis systems, and what is the minimum-viable verification workflow for an Artificial Intelligence (AI) research agent that must distinguish verified facts from inferences?](https://davidamitchell.github.io/Research/research/2026-05-02-automated-claim-verification-academic-literature.html)
- [Cryptographic preservation and runtime evaluation of original intent: a representation formalism for Getting Started phase intent that is simultaneously verifiable and semantically stable across the full operational lifecycle](https://davidamitchell.github.io/Research/research/2026-04-27-cryptographic-intent-preservation-runtime-evaluation.html)

## Approach

1. Define the primitive functions of an independent checking zone: verification, evidence capture, replay, auditability, and non-interference.
2. Catalogue candidate mechanisms from formal verification, assurance pipelines, provenance, immutable logging, and independent audit system design.
3. Compare how those mechanisms establish attainment, what evidence they emit, and how durable or replayable that evidence remains over time.
4. Evaluate criteria for independence from specific content pools and execution environments, including whether the mechanism changes the system it checks.
5. Synthesize a reusable set of checking primitives and an assessment rubric for reliability and evidence quality.

## Sources

- [ ] [GitHub issue #653: Four research questions](https://github.com/davidamitchell/Research/issues/653) — canonical statement of the research request and the validation-zone boundaries
- [ ] [Automated governance assurance and change control verification patterns for AI-assisted delivery](https://davidamitchell.github.io/Research/research/2026-04-22-ai-governance-assurance-change-control-verification.html) — prior repository item on machine-verifiable evidence and policy checking
- [ ] [What automated claim verification approaches against scientific literature (arXiv) are used in research synthesis systems, and what is the minimum-viable verification workflow for an Artificial Intelligence (AI) research agent that must distinguish verified facts from inferences?](https://davidamitchell.github.io/Research/research/2026-05-02-automated-claim-verification-academic-literature.html) — prior repository item on evidence-based verification workflows
- [ ] [Cryptographic preservation and runtime evaluation of original intent: a representation formalism for Getting Started phase intent that is simultaneously verifiable and semantically stable across the full operational lifecycle](https://davidamitchell.github.io/Research/research/2026-04-27-cryptographic-intent-preservation-runtime-evaluation.html) — prior repository item on verifiable intent and durable evidence
- [ ] [Supply-chain Levels for Software Artifacts (SLSA)](https://slsa.dev/) — baseline reference for attestations and tamper-evident provenance evidence

---

## Research Skill Output

*(Full output from running the research skill — retained verbatim in the completed item. §§0–5 are the investigation; §6 seeds the Findings section below.)*

### §0 Initialise

-

### §1 Question Decomposition

-

### §2 Investigation

-

### §3 Reasoning

-

### §4 Consistency Check

-

### §5 Depth and Breadth Expansion

-

### §6 Synthesis

**Executive summary:**

**Key findings:**

**Evidence map:**

**Assumptions:**

**Analysis:**

**Risks, gaps, uncertainties:**

**Open questions:**

### §7 Recursive Review

-

---

## Findings

*(Populated from §6 Synthesis above.)*

### Executive Summary

3–5 sentences. What is the answer to the research question? State the key conclusion directly. Write plain prose — no prefix labels. Bind sources as trailing inline citations: `Claim text. [inference; source: https://url]`

### Key Findings

Ordered list. Each finding is a specific, evidence-backed claim with confidence and source as a trailing parenthetical. Use **suffix style** — source at the end of the claim, not at the beginning.

1. **Claim text as a complete sentence.** (high confidence; source: https://url)
2. **Claim text as a complete sentence.** (medium confidence; source: https://url1; https://url2)

Source URLs must exactly match URLs in the `## Sources` section so the generated site can render `Author (Year)` citation links. List the primary source URL(s) from `## Sources` here.

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| | | high / medium / low | |

### Assumptions

Explicit assumptions made during the investigation and the justification for each.

- **Assumption:** ... **Justification:** ...

### Analysis

How the evidence was weighed, what trade-offs were identified, and how competing interpretations were resolved.

### Risks, Gaps, and Uncertainties

What is still unknown? Where does the evidence fall short? What could change the conclusion?

-

### Open Questions

Questions that surfaced during research but are out of scope for this item. Each may become a new backlog item.

-

---

## Output

*(Fill in when completing — what was produced as a result of this research?)*

- Type: # skill | tool | agent | knowledge | backlog-item
- Description:
- Links:
