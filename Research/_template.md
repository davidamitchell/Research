---
title: "TITLE"
added: YYYY-MM-DDTHH:MM:SS+00:00
status: backlog  # backlog | in-progress | reviewing | completed
priority: medium  # low | medium | high
blocks: []  # slugs (filename without .md) of backlog items that cannot start until this one is complete
depends_on: []  # slugs of completed items that must exist before this item can be picked
tags: []  # Use canonical forms from docs/tag-vocabulary.md — e.g. [agentic-ai, llm, governance]
started: ~
completed: ~
output: []  # skill | tool | agent | knowledge | backlog-item
cites: []          # slugs of items this item directly depends on or quotes
related: []        # slugs of thematically connected items
superseded_by: ~   # slug of a later item that overrides this one (null if not superseded)
supersedes: ~      # slug of an older item this one replaces (null if not applicable)
item_type: primary # primary | synthesis
confidence: medium # high | medium | low
gaps: []           # open questions this item could not answer (1–5 short strings, max 100 chars each)
versions: []       # entries: {version: "1.0", sha: "<commit-hash>", changed: YYYY-MM-DD, progress: "<path>", summary: "<one-line>"}
---

# TITLE

## Research Question

State the specific, answerable question this research addresses. Avoid vague topics; prefer "What is the best X for Y given Z constraints?" over "Investigate X."

## Scope

**In scope:**
-

**Out of scope:**
-

**Constraints:** (time, source types, access)

## Context

Why is this question worth answering now? What decision or problem does the answer inform? This section is a framing device — write plainly and motivate the work. Hard factual claims (statistics, named studies) should still be sourced; working hypotheses and motivating rationale do not need labels.

## Approach

Decompose the question into sub-questions and describe how each will be investigated (literature review, experiment, prototype, expert interview, etc.).

1.
2.

## Sources

Starting points — papers, articles, videos, repos, docs.
**Every source must include a URL.** Use the display name formats below — they feed the `Author (Year)` citation labels shown on the generated site:

- `[Smith et al. (YYYY) Title of paper](https://url)` — for papers with named authors
- `[Organisation Title](https://url)` — for documentation, standards, or pages without a named author

- [ ] [Smith et al. (YYYY) Source Title](https://url) — brief description of what this source provides
- [ ] [Organisation Title](https://url) — brief description

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
