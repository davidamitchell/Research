---
title: "Substrate-aware enterprise strategic objectives and feasible delivery allocation"
added: 2026-11-01T10:53:33+00:00
status: backlog
priority: medium
blocks: []
themes: [enterprise-adoption, organisational-design, software-engineering, formal-methods, cost-performance]
started: ~
completed: ~
output: []
cites: []
related:
  - 2026-10-01-thinnest-viable-internal-platform-standard
  - 2026-10-02-ideal-internal-platform-product-standard
  - 2026-10-23-dependency-properties-coordination-mechanisms
  - 2026-06-13-local-global-optima-knowledge-work-throughput
  - 2026-06-13-platform-engineering-innersource-hybrid-standardization
  - 2026-05-31-gore-strategic-intent-to-delivery-decomposition
superseded_by: ~
supersedes: ~
item_type: primary
confidence: medium
versions: []
---

# Substrate-aware enterprise strategic objectives and feasible delivery allocation

## Research Question

What evidence supports or challenges the need for enterprise strategic objectives to explicitly incorporate the existing delivery substrate (multi-year Software as a Service (SaaS) contracts, embedded platform commitments, established team topologies, capacity limits, and architectural dependencies), and which objective-formulation criteria and mechanisms make subsequent allocation between stream-aligned autonomy and centralized architectural coordination feasible without generating technical or capability debt?

## Scope

**In scope:**
- Criteria and decision rules at the enterprise strategic-objective layer that surface delivery-substrate constraints.
- Evidence for and against substrate-aware formulation, including conditions under which substrate-independent objectives remain feasible.
- Mechanisms that connect objective formulation to operating-model choice and the allocation of autonomy and architectural coordination.
- Positive capacity and buffer models that reserve room for coordination, change, maintenance, and capability development rather than leave debt as the residual.
- Contract horizons, embedded platform commitments, team cognitive load, shared bottlenecks, and architectural dependencies.

**Out of scope:**
- Team-level backlog prioritisation, sprint planning, and stand-up practices.
- Purely financial head-count models disconnected from delivery architecture.
- Evaluation of specific tooling.

**Constraints:**
- No industry, enterprise size, or strategic planning horizon is specified; state where any proposed rule depends on these factors.
- Distinguish constraints that are fixed within the objective's horizon from commitments that can be renegotiated or changed through a funded transition; do not assume the current substrate must remain permanent.
- Seek primary research, standards, and documented enterprise cases; distinguish practitioner guidance from empirical evidence and cross-domain analogies from validated enterprise mechanisms.
- Assess the assumptions and transfer limits of mathematical capacity models; do not invent enterprise capacity thresholds or buffer percentages.
- Define technical debt and capability debt separately and specify observable indicators for each.
- Expected eventual output: a knowledge synthesis of evidence, conditional formulation criteria, and allocation mechanisms. No investigation is performed when adding this item.

## Context

[Issue #686](https://github.com/davidamitchell/Research/issues/686) asks how enterprise architecture and operating-model choices can inform strategic objectives before allocation decisions, testing the hypothesis that discovering entrenched delivery constraints only during execution turns delivery pressure into local workarounds and accumulated debt.

## Approach

1. What evidence shows that acknowledging substrate constraints during objective formulation improves enterprise delivery feasibility? Review enterprise cases and studies, distinguishing observed outcomes from proposed explanations.
2. Under what conditions can substrate-independent strategic objectives remain feasible? Seek counterexamples and compare explicit constraint incorporation with later decomposition, funded substrate change, and staged commitment.
3. Which objective-level criterion reveals a binding contract or embedded platform commitment within the planning horizon? Examine constraint registers and objective specifications for treatment of exit costs, renewal dates, and transition lead times.
4. Which objective-level criterion exposes capacity or architectural-dependency infeasibility before allocation? Examine demand, shared bottleneck, dependency, and cognitive-load representations.
5. Which dependency property indicates that a delivery decision requires centralized architectural coordination rather than stream-aligned autonomy? Compare decision-rights and interaction-mode mechanisms using the constraint categories identified in questions 3 and 4.
6. Which traceability mechanism preserves feasibility when strategic intent is decomposed into scoped delivery objectives? Examine goal refinement and constraint propagation, drawing on questions 3 and 4.
7. Under what assumptions does each seeded cross-domain capacity model apply to enterprise delivery? Assess Erlang's queueing work, Little's law, Amdahl's law, Gunther's Universal Scalability Law, railway block signalling, and International Union of Railways (UIC) Code 406 separately; identify where an analogy lacks empirical validation.
8. Which positive capacity or buffer rule prevents technical debt from absorbing excess demand? Examine maintenance and coordination reservations, testing applicability against question 7.
9. Which positive capacity or buffer rule prevents capability debt from absorbing excess demand? Examine protected learning, capability development, and transition capacity, testing applicability against question 7.

Readiness: **READY**. Specific, answerable in principle, scoped, motivated, and decomposed; investigate both necessity and counterexamples rather than assume the motivating hypothesis is true.

## Related

- [Satisfiable internal platforms](https://davidamitchell.github.io/Research/research/2026-10-01-thinnest-viable-internal-platform-standard.html): starting point for Thinnest Viable Platform (TVP), cognitive-load, and fixed-capacity questions.
- [Ideal internal platforms as products](https://davidamitchell.github.io/Research/research/2026-10-02-ideal-internal-platform-product-standard.html): starting point for assessing platform commitments as operating-model choices.
- [Dependency properties and coordination mechanisms](https://davidamitchell.github.io/Research/research/2026-10-23-dependency-properties-coordination-mechanisms.html): starting point for question 5's allocation criteria.
- [Local and global optima in knowledge-work throughput](https://davidamitchell.github.io/Research/research/2026-06-13-local-global-optima-knowledge-work-throughput.html): starting point for shared bottlenecks and the difference between team and enterprise feasibility.
- [Platform engineering, InnerSource, and hybrid standardisation](https://davidamitchell.github.io/Research/research/2026-06-13-platform-engineering-innersource-hybrid-standardization.html): adjacent operating-model research in the issue's local-versus-global cluster.
- [Goal-Oriented Requirements Engineering (GORE): translating strategic intent to scoped delivery objectives](https://davidamitchell.github.io/Research/research/2026-05-31-gore-strategic-intent-to-delivery-decomposition.html): starting point for question 6's objective-refinement mechanisms.

## Sources

Unconsulted starting points. Issue-linked entries preserve bibliographic leads supplied by the requester; locate and verify the original publications during research rather than cite the issue as evidence for the theories.

- [ ] [Issue #686: Erlang (1909) and Little (1961)](https://github.com/davidamitchell/Research/issues/686): queueing and flow foundations to locate.
- [ ] [Issue #686: Amdahl (1967) and Gunther's Universal Scalability Law](https://github.com/davidamitchell/Research/issues/686): serial work, contention, and coordination foundations to locate.
- [ ] [Issue #686: railway block signalling and UIC Code 406](https://github.com/davidamitchell/Research/issues/686): capacity and buffer foundations to locate; verify the relevant edition and transfer assumptions.
- [ ] [Issue #686: Conway (1968), Skelton and Pais (2019) Team Topologies, and Wardley Mapping](https://github.com/davidamitchell/Research/issues/686): organisational structure and strategy-mapping foundations to locate.
- [ ] [Issue #686: Cunningham (1992) technical debt and Goldratt's Theory of Constraints](https://github.com/davidamitchell/Research/issues/686): debt and bottleneck foundations to locate.
- [ ] [Satisfiable internal platforms](https://davidamitchell.github.io/Research/research/2026-10-01-thinnest-viable-internal-platform-standard.html)
- [ ] [Ideal internal platforms as products](https://davidamitchell.github.io/Research/research/2026-10-02-ideal-internal-platform-product-standard.html)
- [ ] [Dependency properties and coordination mechanisms](https://davidamitchell.github.io/Research/research/2026-10-23-dependency-properties-coordination-mechanisms.html)
- [ ] [Local and global optima in knowledge-work throughput](https://davidamitchell.github.io/Research/research/2026-06-13-local-global-optima-knowledge-work-throughput.html)
- [ ] [Platform engineering, InnerSource, and hybrid standardisation](https://davidamitchell.github.io/Research/research/2026-06-13-platform-engineering-innersource-hybrid-standardization.html)
- [ ] [Goal-Oriented Requirements Engineering: translating strategic intent to scoped delivery objectives](https://davidamitchell.github.io/Research/research/2026-05-31-gore-strategic-intent-to-delivery-decomposition.html)

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
