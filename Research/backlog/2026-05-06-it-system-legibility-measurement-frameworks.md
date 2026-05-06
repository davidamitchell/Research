---
title: "What measurement systems and frameworks exist for quantifying Information Technology system legibility — the ability to reason about, understand, and comprehensively characterise a runtime ecosystem of interconnected applications, services, and systems — who is actively defining and applying them, and how?"
added: 2026-05-06T07:32:54+00:00
status: backlog  # backlog | in-progress | reviewing | completed
priority: medium  # low | medium | high
blocks: []  # slugs (filename without .md) of backlog items that cannot start until this one is complete
tags: [observability, enterprise-architecture, dependency-mapping, it-architecture, systems-thinking, measurement]
started: ~
completed: ~
output: []  # skill | tool | agent | knowledge | backlog-item
cites: []          # slugs of items this item directly depends on or quotes
related: [2026-03-21-dependency-mapping-dotnet-terraform-dynatrace, 2026-03-21-technology-capability-models, 2026-04-27-enterprise-stack-value-distribution-governance-frameworks]
superseded_by: ~   # slug of a later item that overrides this one (null if not superseded)
supersedes: ~      # slug of an older item this one replaces (null if not applicable)
item_type: primary # primary | synthesis
confidence: medium # high | medium | low
versions: []       # entries: {version: "1.0", sha: "<commit-hash>", changed: YYYY-MM-DD, progress: "<path>", summary: "<one-line>"}
---

# What measurement systems and frameworks exist for quantifying Information Technology system legibility — the ability to reason about, understand, and comprehensively characterise a runtime ecosystem of interconnected applications, services, and systems — who is actively defining and applying them, and how?

## Research Question

What measurement systems and frameworks exist for quantifying Information Technology (IT) system legibility — defined as the ability to reason about, understand, and comprehensively characterise the entirety of interconnected applications, services, and systems that constitute an organisation's runtime ecosystem — who (in academic research, standards bodies, and industry practice) is actively defining and applying these frameworks, and what does practical implementation look like?

## Scope

**In scope:**
- Definitions and theoretical models of IT system legibility, system comprehensibility, and whole-estate understandability
- Formal measurement frameworks and metrics for quantifying how well-understood a runtime IT ecosystem is (e.g. fitness functions, architectural health metrics, Configuration Management Database (CMDB) coverage rates, service dependency completeness)
- Adjacent concepts: architectural observability, cognitive complexity of IT estates, system transparency, run-book coverage, infrastructure discoverability
- Academic research, practitioner frameworks, standards (e.g. The Open Group Architecture Framework (TOGAF), Business Information and Network (BIAN), TM Forum), and vendor tooling in this space
- Who is actively working in this area: research groups, standards bodies, enterprise architecture practices, observability vendors
- Practical implementation examples: tooling, assessment approaches, maturity models, case studies

**Out of scope:**
- Individual-service observability and monitoring (e.g. application performance metrics for a single service) unless used as a component of a whole-ecosystem legibility framework
- Network topology mapping as a standalone discipline (in scope only when used as input to a legibility framework)
- Purely theoretical computer science complexity measures (Kolmogorov complexity, cyclomatic complexity) unless they are applied directly to IT estate characterisation

**Constraints:**
- Primary sources preferred; secondary synthesis acceptable where primary is unavailable
- Recency: fast-moving field — sources older than five years should be flagged
- Scope is practitioner-oriented: weight implementations and applied frameworks over pure theory

## Context

Large organisations routinely operate IT estates comprising hundreds to thousands of interconnected services, applications, and infrastructure components. The practical ability to reason about, understand, and fully describe this ecosystem — its boundaries, dependencies, ownership, and runtime behaviour — is a foundational prerequisite for safe change management, AI agent deployment, governance, and cost control. This question seeks to understand whether the field has formalised this ability as a measurable property, who is defining and using such frameworks, and what practical tools exist to assess and improve it.

## Approach

Decomposed into five sub-questions, each to be investigated separately and then synthesised:

1. **Definition:** How is "IT system legibility" (or equivalent concepts such as system comprehensibility, architectural transparency, or estate understandability) defined in academic and practitioner literature? What adjacent or synonymous concepts exist, and how do they relate?

2. **Frameworks and metrics:** What formal frameworks or measurement approaches exist for quantifying the legibility of an IT estate? Are there scoring rubrics, maturity models, or coverage metrics in common use?

3. **Who is working in this space:** Which academic research groups, standards bodies (e.g. TOGAF, BIAN, TM Forum), enterprise architecture communities, and vendors are actively defining or applying IT system legibility frameworks? What are their primary outputs?

4. **Tooling and practical implementation:** What tooling supports legibility assessment — Configuration Management Databases (CMDBs), service meshes, dependency graph tools, observability platforms, software intelligence platforms — and how do organisations use them to improve legibility?

5. **Practical application examples:** What case studies or published accounts exist of organisations successfully measuring and improving IT system legibility? What did the process look like, and what outcomes were achieved?

## Sources

Starting points — papers, articles, videos, repos, docs.
**Every source must include a URL.** Use the display name formats below — they feed the `Author (Year)` citation labels shown on the generated site:

- `[Smith et al. (YYYY) Title of paper](https://url)` — for papers with named authors
- `[Organisation Title](https://url)` — for documentation, standards, or pages without a named author

- [ ] [Ford et al. (2017) Building Evolutionary Architectures](https://www.oreilly.com/library/view/building-evolutionary-architectures/9781491986356/) — introduces architectural fitness functions as measurable properties of a system; relevant to legibility-as-measurement
- [ ] [The Open Group TOGAF Standard](https://www.opengroup.org/togaf) — enterprise architecture framework that addresses IT estate documentation and understandability
- [ ] [LeanIX Enterprise Architecture Management](https://www.leanix.net/) — practitioner tooling for IT system mapping and legibility; vendor perspective
- [ ] [Thoughtworks Technology Radar: Software Intelligence](https://www.thoughtworks.com/radar) — tracks emerging tools and practices for IT estate understanding
- [ ] [CAST Software Application Intelligence](https://www.castsoftware.com/) — software intelligence tooling measuring structural quality and complexity of IT applications
- [ ] [Backstage Developer Portal (Spotify)](https://backstage.io/) — open-source developer portal addressing service catalogue completeness and discoverability
- [ ] [Dynatrace Software Intelligence Platform](https://www.dynatrace.com/) — observability and AI-powered dependency mapping across runtime ecosystems

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
