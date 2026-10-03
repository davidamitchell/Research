---
title: "Cross-effects among three-zone agent interventions"
added: 2026-10-03T08:39:00+00:00
status: backlog
priority: high
blocks: []
themes: [agentic-ai, tools-infrastructure, knowledge-management, governance-policy]
started: ~
completed: ~
output: []
cites: [2026-08-20-mediated-content-pool-semantic-clarity, 2026-08-20-flat-vector-rag-context-collision, 2026-08-20-execution-harness-closed-loop-performance, 2026-08-20-independent-goal-attainment-verification, 2026-08-20-three-zone-interface-feedback-constraints, 2026-07-20-agent-memory-evaluation-framework, 2026-05-18-rq4-2-adversarial-error-propagation, 2026-03-10-adversarial-agents-shared-goals-multi-perspective, 2026-04-28-llm-as-judge-pipeline-validation-checkpoints, 2026-05-17-ai-policy-ambiguity-feedback-loop-systemic-homogenization-risk, 2026-03-12-failure-mode-taxonomy-expansion]
related: [2026-07-20-tbox-abox-graphrag, 2026-03-08-context-engineering-first-principles, 2026-05-12-rag-document-drift-agent-behavior, 2026-05-01-terminal-bench-minimal-coding-agent-benchmarks, 2026-08-20-neuro-symbolic-nuance-loss-explainability]
superseded_by: ~
supersedes: ~
item_type: primary
confidence: medium
versions: []
---

# Cross-effects among three-zone agent interventions

## Research Question

Under what conditions do the measured benefits of pool-level annotations, harness context management, and goal-attainment verification hold, shrink, or reverse as the consumer model, task family, content-pool properties, and verifier model family vary, and which properties predict those changes?

## Scope

**In scope:**
- Test whether provenance and justification overlays—including the Provenance Ontology (PROV-O), Resource Description Framework-star (RDF-star), and minimal justification sets—change large language model (LLM) consumer outputs on the conflict categories identified in retrieval-augmented generation (RAG) context-collision work; vary consumer model.
- Compare observation masking with summarisation across model configurations and non-coding task families, varying pool structure such as the terminological box (TBox), assertional box (ABox), noise, and ambiguity.
- Measure verifier accuracy against independent evidence while varying verifier/harness model-family alignment and shared context; retain the prior reliability rubric's graded notion of independence.
- Vary one zone at a time, report interaction effects, and determine when each measured improvement can be treated as independent. Explain the supplied counter-cases rather than rediscovering them.
- Account for selection artefacts and other measurement limitations when comparing gains.

**Out of scope:**
- Assigning ownership of the resolver step, which the three-zone interface item defers to issue #653.
- Re-evaluating the earlier studies without testing cross-zone effects.

**Constraints:** Use controlled comparisons where available; distinguish measured results from hypotheses when direct experiments or suitable benchmarks are absent. Report consumer model, task family, pool properties, verifier family, and interaction effects so the conditions for any claimed independence are explicit.

## Context

This research informs whether the three proposed interventions can be adopted independently or must be selected conditionally, since an improvement measured in one zone may depend on the consumer, task, pool, harness, or verifier in another.

## Approach

1. **Pool to consumer:** Apply the content-pool item's provenance and justification overlays to the context-collision item's conflict categories; compare consumer outputs across model families and score both annotation quality and downstream conflict resolution.
2. **Harness to pool:** Compare observation masking with summarisation on non-coding tasks while varying pool structure, noise, and ambiguity; test whether the measured masking advantage persists or reverses.
3. **Verifier to harness:** Measure goal-attainment verifier accuracy against independent evidence while varying shared context and model-family alignment between harness and verifier; report independence as a graded factor.
4. **Cross-zone synthesis:** Separate single-zone effects from interactions, reconcile the specified counter-cases, and state the pool, harness, and verifier conditions under which each gain can be treated as independent.

## Related

- [Ontology schema-versus-instance choices in graph-based retrieval](https://davidamitchell.github.io/Research/research/2026-07-20-tbox-abox-graphrag.html)
- [Model-specific context-engineering effects](https://davidamitchell.github.io/Research/research/2026-03-08-context-engineering-first-principles.html)
- [Behavioral change after retrieval corpus edits](https://davidamitchell.github.io/Research/research/2026-05-12-rag-document-drift-agent-behavior.html)

## Sources

Starting points from issue #669 and its cited work; no research has been conducted for this backlog item.

- [ ] [GitHub issue #669: Cross-effects among three-zone agent interventions](https://github.com/davidamitchell/Research/issues/669) — question, scope, evidence standard, and counter-cases.
- [ ] [Semantic clarity and conflict resolvability in mediated content pools](https://davidamitchell.github.io/Research/research/2026-08-20-mediated-content-pool-semantic-clarity.html) — proposed pool-level provenance and justification annotations.
- [ ] [Context collision and relational blindness in flat-vector retrieval-augmented generation](https://davidamitchell.github.io/Research/research/2026-08-20-flat-vector-rag-context-collision.html) — conflict categories and reported conflict-label intervention.
- [ ] [Closed-loop performance techniques for mediated execution harnesses](https://davidamitchell.github.io/Research/research/2026-08-20-execution-harness-closed-loop-performance.html) — observation masking and summarisation comparison.
- [ ] [Independent verification and durable evidence for goal attainment](https://davidamitchell.github.io/Research/research/2026-08-20-independent-goal-attainment-verification.html) — reliability rubric and graded independence.
- [ ] [Zone-specific interface constraints in three-zone architectures](https://davidamitchell.github.io/Research/research/2026-08-20-three-zone-interface-feedback-constraints.html) — interfaces, selection-artefact caveat, and resolver deferral.
- [ ] [Evaluation frameworks for agentic memory quality, relevance, and retrieval accuracy](https://davidamitchell.github.io/Research/research/2026-07-20-agent-memory-evaluation-framework.html) — provenance-fidelity evaluation gap.
- [ ] [Adversarial input propagation through multi-step tool-using systems](https://davidamitchell.github.io/Research/research/2026-05-18-rq4-2-adversarial-error-propagation.html) — verifier and strategy-selection error propagation.
- [ ] [Adversarial agents with shared goals: multi-perspective coverage](https://davidamitchell.github.io/Research/research/2026-03-10-adversarial-agents-shared-goals-multi-perspective.html) — evidence on agent independence and shared perspectives.
- [ ] [Large Language Model-as-judge pipeline validation checkpoints](https://davidamitchell.github.io/Research/research/2026-04-28-llm-as-judge-pipeline-validation-checkpoints.html) — verifier placement and pipeline validation.
- [ ] [Policy ambiguity and feedback-loop homogenisation risk](https://davidamitchell.github.io/Research/research/2026-05-17-ai-policy-ambiguity-feedback-loop-systemic-homogenization-risk.html) — model-family alignment risk.
- [ ] [Failure mode taxonomy: empirical frequency and causal mechanisms](https://davidamitchell.github.io/Research/research/2026-03-12-failure-mode-taxonomy-expansion.html) — co-located monitor case identified as unquantified.
- [ ] [Schema-led versus instance-emergent ontology approaches in graph-based retrieval](https://davidamitchell.github.io/Research/research/2026-07-20-tbox-abox-graphrag.html) — ontology gain and noisy-corpus reversal.
- [ ] [Context engineering: first principles of steering large language model output](https://davidamitchell.github.io/Research/research/2026-03-08-context-engineering-first-principles.html) — model-specific context-rot curves.
- [ ] [Behavioral change after retrieval-augmented generation source-document edits](https://davidamitchell.github.io/Research/research/2026-05-12-rag-document-drift-agent-behavior.html) — corpus edits changing behaviour with weights and prompts fixed.
- [ ] [Minimal coding-agent benchmark results across model families](https://davidamitchell.github.io/Research/research/2026-05-01-terminal-bench-minimal-coding-agent-benchmarks.html) — leaderboard counter-case to minimal-harness superiority.
- [ ] [Nuance collapse in deterministic neuro-symbolic ontology pipelines](https://davidamitchell.github.io/Research/research/2026-08-20-neuro-symbolic-nuance-loss-explainability.html) — ambiguity lost through normalisation.

---

## Research Skill Output

*(Full output from running the research skill — retained verbatim in the completed item. §§0–5 are the investigation; §6 seeds the Findings section below.)*

### §0 Initialise

Restate the research question. Confirm scope, constraints, and output format.

-

### §1 Question Decomposition

Approach sub-questions broken into atomic questions — each answerable with a single evidence-based claim.

-

### §2 Investigation

Evidence gathered per atomic question. Label each claim: **[fact]**, **[inference]**, or **[assumption]** with source.

-

### §3 Reasoning

Facts, inferences, and assumptions explicitly separated. No unsupported generalisations or narrative leaps.

-

### §4 Consistency Check

Internal contradictions identified and resolved (or explicitly flagged where unresolvable).

-

### §5 Depth and Breadth Expansion

Findings re-examined through relevant lenses (technical, regulatory, economic, historical, behavioural).

-

### §6 Synthesis

*(This section seeds the Findings below.)*

**Executive summary:**

**Key findings:**

**Evidence map:**

**Assumptions:**

**Analysis:**

**Risks, gaps, uncertainties:**

**Open questions:**

### §7 Recursive Review

Final pass: every section justified, all threads synthesised, every claim sourced or labelled, all uncertainties explicit.

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
