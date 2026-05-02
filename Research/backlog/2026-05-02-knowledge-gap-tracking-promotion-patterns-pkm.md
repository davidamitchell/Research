---
title: "What structured knowledge-gap tracking and automatic backlog-promotion patterns exist in Personal Knowledge Management (PKM) and research systems, and which design is most suitable for a YAML-frontmatter file-based corpus?"
added: 2026-05-02T06:11:10+00:00
status: backlog  # backlog | in-progress | reviewing | completed
priority: medium  # low | medium | high
blocks: []  # slugs (filename without .md) of backlog items that cannot start until this one is complete
tags: [knowledge-graph, workflow, research-tooling, agentic-ai, organisational-learning]
started: ~
completed: ~
output: []  # skill | tool | agent | knowledge | backlog-item
cites: []
related: [2026-03-12-exploration-synthesis-gap, 2026-03-03-cross-item-synthesis-meta-insights]
superseded_by: ~
supersedes: ~
item_type: primary
confidence: medium
versions: []
---

# What structured knowledge-gap tracking and automatic backlog-promotion patterns exist in Personal Knowledge Management (PKM) and research systems, and which design is most suitable for a YAML-frontmatter file-based corpus?

## Research Question

What structured knowledge-gap tracking and automatic backlog-promotion patterns exist in Personal Knowledge Management (PKM) systems (Zettelkasten, Obsidian, Roam Research, Logseq) and academic research management tools, how do they handle unresolved questions that recur across multiple notes or papers, and which design — specifically for a YAML-frontmatter field in a file-based Markdown corpus with a Python aggregation script — provides the best balance between structured data quality, minimal agent overhead, and reliable automatic promotion of persistently unresolved gaps into new research backlog items?

## Scope

**In scope:**
- PKM systems: Zettelkasten (paper and digital), Obsidian (with Dataview and community plugins), Roam Research, Logseq — how each handles open questions, unanswered notes, and recurring gaps
- Academic research management: how systematic review tools (Covidence, Rayyan, Zotero) and literature review workflows track evidence gaps and research limitations across papers
- Knowledge gap aggregation design patterns: deduplication strategies (exact match, fuzzy match, semantic similarity), occurrence counting, and promotion thresholds
- YAML field design: what fields best capture a gap (free-text string vs controlled vocabulary vs structured sub-fields), how to balance expressiveness with aggregation reliability
- Aggregation script design: how to read gap fields from frontmatter, deduplicate, count occurrences, and write a structured `gap_registry.json`; what the `promote: true` threshold should be and why
- Failure modes: sparse or low-quality gap strings that defeat deduplication; over-promotion of trivially similar gaps; agent overhead that discourages gap tracking

**Out of scope:**
- Full-text semantic gap extraction from body text (W-0040 uses frontmatter YAML only)
- Gap tracking in non-file-based systems (databases, graph databases)
- Automated gap research execution (the item only tracks and promotes gaps; research is performed separately)

**Constraints:**
- Expand all acronyms on first use
- The design must work with Python 3.11+ and standard library + YAML parsing; no external database or vector index required
- The YAML field must be writable by an LLM agent with a simple instruction: "list 1–5 open questions this item could not answer"

## Context

W-0040 in `BACKLOG.md` proposes a `gaps:` YAML frontmatter field, an `aggregate_gaps.py` script, and automatic promotion of gaps appearing in three or more items. Before implementing, the design must be grounded in evidence about how existing PKM systems handle recurring unresolved questions — specifically: what field granularity works, what deduplication approach is practical for free-text strings written by an LLM, and what promotion threshold is appropriate. This research item prevents designing the gap registry on untested assumptions about agent behaviour and string similarity.

## Approach

1. **PKM system survey**: Review Zettelkasten, Obsidian (Dataview plugin, "open questions" note type), Roam Research (block references for unresolved notes), and Logseq (queries over tagged blocks); document how each handles recurring open questions and what data structure underlies the mechanism.
2. **Academic research gap tracking review**: Survey systematic review tools (Covidence, Rayyan) and evidence synthesis frameworks (GRADE — Grading of Recommendations Assessment, Development and Evaluation) for how evidence gaps are recorded across studies and promoted to new research priorities.
3. **YAML field design options**: Evaluate free-text string list, controlled vocabulary with a gap taxonomy, and structured sub-field designs (question + domain + severity); assess each for LLM writeability, deduplication reliability, and aggregation script complexity.
4. **Deduplication strategy evaluation**: Compare exact match, Levenshtein distance (fuzzy string match), and embedding-based semantic similarity for deduplicating LLM-generated gap strings; assess practical accuracy vs compute cost for a ~200-item corpus.
5. **Promotion threshold analysis**: Evaluate promotion threshold options (2 items, 3 items, 5 items, statistical outlier); identify what threshold minimises false promotions (trivial variations) while catching genuine recurring gaps.
6. **Design recommendation**: Produce concrete YAML field specification, aggregation script design, and promotion logic recommendation with supporting evidence from the PKM and academic review literature.

## Sources

- [ ] [Ahrens (2017) How to Take Smart Notes: One Simple Technique to Boost Writing, Learning and Thinking](https://www.soenkeahrens.de/en/takesmartnotes) — Zettelkasten methodology including open question cards and gap tracking
- [ ] [Obsidian documentation — Dataview plugin](https://blacksmithgu.github.io/obsidian-dataview/) — structured frontmatter querying for open questions and recurring themes in Obsidian
- [ ] [Logseq documentation — Queries](https://docs.logseq.com/#/page/queries) — block-level query patterns for surfacing unresolved questions across notes
- [ ] [Covidence — Systematic Review Software](https://www.covidence.org/) — evidence gap tracking and extraction in systematic review workflows
- [ ] [Higgins et al. (2023) Cochrane Handbook for Systematic Reviews of Interventions](https://training.cochrane.org/handbook) — GRADE evidence gap recording and future research prioritisation in systematic review
- [ ] [Fuzzywuzzy / rapidfuzz Python library documentation](https://github.com/maxbachmann/RapidFuzz) — practical fuzzy string matching for deduplication of LLM-generated text

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

### Key Findings

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| | | high / medium / low | |

### Assumptions

### Analysis

### Risks, Gaps, and Uncertainties

-

### Open Questions

-

---

## Output

*(Fill in when completing — what was produced as a result of this research?)*

- Type: # skill | tool | agent | knowledge | backlog-item
- Description:
- Links:
