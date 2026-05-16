---
title: "Reference architecture definition, framework landscape, and required detail level"
added: 2026-05-16T04:50:59+00:00
status: backlog  # backlog | in-progress | reviewing | completed
priority: medium  # low | medium | high
blocks: []  # slugs (filename without .md) of backlog items that cannot start until this one is complete
tags: [reference-architecture, enterprise, capability-model, architecture-framework]
started: ~
completed: ~
output: []  # skill | tool | agent | knowledge | backlog-item
cites: []
related:
  - 2026-05-08-ai-capability-reference-architecture-second-cycle-update
  - 2026-05-06-ai-capability-reference-architecture-security-supply-chain-update
superseded_by: ~
supersedes: ~
item_type: primary
confidence: medium
versions: []
---

# Reference architecture definition, framework landscape, and required detail level

## Research Question

What should a practical reference architecture include, which established architecture frameworks define or structure it, and how much detail should be specified across capabilities, components, flow diagrams, and technology choices so that stakeholders can use it consistently?

## Scope

**In scope:**
- Definitions of reference architecture from recognised standards bodies and enterprise architecture guidance
- Frameworks that explicitly describe reference architecture structure, including The Open Group Architecture Framework (TOGAF), International Organization for Standardization (ISO) / International Electrotechnical Commission (IEC) / Institute of Electrical and Electronics Engineers (IEEE) 42010, and major cloud provider architecture frameworks
- Practical detail levels for capability views, component views, flow views, and technology-binding decisions
- Common interpretation of the statement "we need a reference architecture" in enterprise planning and governance contexts

**Out of scope:**
- Product-by-product implementation runbooks for a specific organisation
- Deep evaluation of one vendor stack over another
- Domain-specific reference architectures for a single niche industry unless needed as examples

**Constraints:** (time, source types, access)
- Prioritise publicly accessible standards, framework documentation, and authoritative architecture guidance
- Distinguish normative definitions from consultancy opinion where possible
- Produce guidance that is usable across multiple organisations, not a single local environment

## Context

This question informs how to scope architecture work when stakeholders request a "reference architecture" but mean different levels of abstraction, detail, and decision commitment.

## Approach

1. Identify and compare formal definitions of reference architecture from standards and established enterprise architecture frameworks.
2. Map how each framework treats capabilities, components, information or process flows, and technology choices.
3. Derive a practical detail-level model (minimum viable reference architecture versus implementation-ready architecture).
4. Analyse trade-offs of staying technology-agnostic versus including explicit technology patterns.
5. Synthesize a decision-oriented interpretation guide for what organisations usually mean when they request a reference architecture.

## Sources

Starting points — papers, articles, videos, repos, docs.
**Every source must include a URL.** Use the display name formats below — they feed the `Author (Year)` citation labels shown on the generated site:

- `[Smith et al. (YYYY) Title of paper](https://url)` — for papers with named authors
- `[Organisation Title](https://url)` — for documentation, standards, or pages without a named author

- [ ] [The Open Group Architecture Framework (TOGAF) Standard](https://www.opengroup.org/togaf) — baseline enterprise architecture framework definition and usage context
- [ ] [ISO/IEC/IEEE 42010 Systems and software engineering — Architecture description](https://www.iso.org/standard/74393.html) — formal architecture description concepts and concerns/viewpoints model
- [ ] [Microsoft Azure Architecture Center](https://learn.microsoft.com/azure/architecture/) — practical reference architectures and level-of-detail patterns
- [ ] [Amazon Web Services Architecture Center](https://aws.amazon.com/architecture/) — reference architectures and component/flow representation examples
- [ ] [Google Cloud Architecture Framework](https://cloud.google.com/architecture/framework) — architecture decision domains and prescriptive design guidance

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
