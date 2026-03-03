---
title: "Cross-item synthesis: methodology and tooling for extracting meta-insights from the research corpus"
added: 2026-03-03
status: backlog
priority: high
tags: [synthesis, meta-analysis, cross-item, insights, knowledge-integration, aggregation, thematic-analysis]
started: ~
completed: ~
output: [knowledge, skill, tool, backlog-item]
---

# Cross-item synthesis: methodology and tooling for extracting meta-insights from the research corpus

## Research Question

What methodology and tooling would allow periodic synthesis across multiple completed research items — producing higher-level thematic reports, contradiction maps, and actionable insight summaries — rather than treating each item as a standalone output?

## Scope

**In scope:**
- Synthesis methodology: how to combine findings from multiple completed items on a related theme into a coherent meta-insight (not just a list of item summaries)
- Thematic clustering: identifying which completed items belong to the same cluster (by tags, cross-references, named concepts, or topic proximity) as the input to a synthesis pass
- Contradiction detection: identifying when two completed items make conflicting claims about the same domain, and surfacing these as explicit tensions rather than ignoring them
- Confirmation mapping: identifying when multiple items independently reach the same conclusion, which increases the confidence of that conclusion
- Output formats for synthesis: thematic report (prose), contradiction map (table), insight digest (bullet-point summary for decision-relevant takeaways)
- Integration with the autonomous research loop: how the loop could periodically trigger a synthesis pass instead of always producing individual research items
- Relationship to the knowledge linking item (`2026-03-03-knowledge-linking-connected-corpus.md`): synthesis uses the link graph as input; the two items are complementary

**Out of scope:**
- Synthesis of a single research item's internal findings (individual item quality is covered by `2026-03-02-research-quality-assurance-methodology.md`)
- Full automated synthesis without agent reasoning — synthesis of research findings requires LLM-level reasoning, not just structural analysis
- Publishing or delivering synthesis outputs (covered by `2026-02-27-interface-and-delivery.md` and `2026-03-02-chat-conversational-interface.md`)

**Constraints:** Synthesis outputs must be committable to the repository (Markdown files, not in-memory only). Any triggered synthesis workflow must be runnable via `workflow_dispatch` from the GitHub website. Synthesis must cite the source items explicitly — no uncited claims.

## Context

The `Research/completed/` corpus now contains ~17 items spanning several clusters:
- **AI strategy and policy**: `ai-strategy`, `ai-line-1-line-2-risk-agents`, `ai-control-testing-and-assurance`, `rbnz-ai-supervisory-expectations` (backlog)
- **Agent cognition and architecture**: `predictive-processing-active-inference`, `interoception-and-the-predictive-self`, `agent-memory-management-context-injection`, `integrative-framework-agent-decision-making` (backlog)
- **Research tooling and process**: `simple-process-for-adding-research-item`, `indexing-and-tracking-method`, `github-wiki-research-content`, `context-mode-llm-context-compression`

Each cluster has reached a density where a synthesis pass would yield insights that no single item contains alone. For example, the AI strategy cluster now has enough items to produce a "State of AI Strategy and Governance in NZ Financial Services" meta-summary. The agent cognition cluster could produce an "Integrated view of agent cognition: from predictive processing to memory and decision-making" synthesis.

Currently, this synthesis work has no home in the system. Research items are written individually, and there is no mechanism for producing a higher-level view. The `2026-03-02-research-quality-assurance-methodology.md` item identifies "integration" as a quality gap but scopes it to individual item completeness; this item addresses the corpus-level synthesis problem.

The `2026-02-27-information-synthesis-entropy.md` completed item provides a theoretical grounding: synthesis reduces entropy (uncertainty) in the knowledge space by resolving competing interpretations and consolidating confirming evidence.

## Approach

1. **Synthesis methodology survey** — Review how research synthesis is structured in academic settings (systematic review, meta-analysis, scoping review) and in knowledge management tools (Roam Research synthesis notes, Obsidian MOC — Map of Content):
   - What distinguishes synthesis (integrated insight) from summary (collection of item abstracts)?
   - What is the minimum structure for a synthesis output? Proposed: theme statement, confirming evidence (from multiple items), tensions/contradictions, integrated conclusion, confidence level, and open questions that synthesis cannot resolve.
   - What are the failure modes of LLM-generated synthesis? (Hallucination of connections, false consensus, loss of nuance from individual items.)

2. **Thematic clustering method** — Define how to identify which completed items belong in the same synthesis pass:
   - Tag-based: items sharing ≥2 tags form a candidate cluster
   - Link-based: items connected via `extends`, `confirms`, or `contradicts` relationships (from `2026-03-03-knowledge-linking-connected-corpus.md`)
   - Manual: the owner or agent designates a cluster via a `synthesis-group` tag or a dedicated config file
   Assess which method is most reliable at current corpus size vs. at 100+ items.

3. **Contradiction detection design** — Define what constitutes a contradiction between two research items and how to surface it:
   - Direct contradiction: item A Key Finding 2 states "X is true" while item B Key Finding 1 states "X is false"
   - Contextual conflict: item A recommends approach P for context C, item B recommends approach Q for context C (same context, different recommendation)
   - Design a structured contradiction record format: `{item_a, finding_a, item_b, finding_b, description, resolution_status}`

4. **Synthesis output format design** — Define the Markdown structure for a synthesis output. Proposed location: `Research/synthesis/` directory. Proposed front-matter: `type: synthesis`, `source-items: [slug-a, slug-b, ...]`, `theme:`, `synthesised: YYYY-MM-DD`. This is a new directory and file type — assess whether it needs an ADR.

5. **Synthesis skill design** — Design the `synthesis` agent skill (for `davidamitchell/Skills`):
   - Input: a list of research item slugs or a theme/tag
   - Process: retrieve executive summaries + key findings from each item; identify confirming pairs, contradicting pairs, and orphaned claims; produce integrated synthesis
   - Output: a completed synthesis Markdown file following the format from step 4
   - Constraints: every claim in the synthesis must cite a source item slug; no new claims not present in the source items

6. **Automated synthesis trigger** — Design a `workflow_dispatch`-triggered workflow (`synthesise.yml`) that:
   - Accepts a theme or comma-separated list of item slugs as input
   - Runs the synthesis skill against those items
   - Commits the output to `Research/synthesis/<date>-<theme>.md`
   - Triggers `publish-wiki.yml` to add the synthesis page to the wiki
   Assess: is this a new workflow requiring an ADR, or an extension of the existing research loop?

7. **Contradiction resolution workflow** — Define what happens when a contradiction is detected: does it spawn a new research backlog item to resolve it, or does it remain as an unresolved tension in the synthesis output? Propose a policy.

## Sources

- [ ] `Research/completed/2026-02-27-information-synthesis-entropy.md` — theoretical grounding: synthesis as entropy reduction; connections as value
- [ ] `Research/backlog/2026-03-02-research-quality-assurance-methodology.md` — integration as a quality dimension; DIKW progression; Nonaka SECI model as synthesis framework
- [ ] `Research/backlog/2026-03-03-knowledge-linking-connected-corpus.md` — link graph as input to synthesis; relationship types (`confirms`, `contradicts`, `extends`)
- [ ] Systematic review methodology (Cochrane Handbook): https://training.cochrane.org/handbook — structured synthesis approach from academic meta-analysis
- [ ] Scoping review methodology (Arksey & O'Malley, 2005): framework for mapping a research area without full meta-analysis
- [ ] Obsidian Maps of Content (MOC): https://notes.nicolevanderhoeven.com/Maps+of+Content — non-hierarchical synthesis in file-based note systems
- [ ] Ahrens (2017) — *How to Take Smart Notes* — synthesis as the natural output of a mature Zettelkasten; how contradictions become the most interesting notes
- [ ] Fabric `create_report` and `extract_wisdom` patterns: https://github.com/danielmiessler/fabric — prompt patterns for synthesis from multiple sources
- [ ] arXiv: "survey paper methodology" — how academic survey papers structure synthesis across dozens of primary sources
- [ ] `src/wiki/publish.py` — existing wiki pipeline; assess how synthesis pages would be incorporated

---

## Findings

*(Fill in when completing. Follow the research skill synthesis structure.)*

### Executive Summary

3–5 sentences. What is the answer to the research question? State the key conclusion directly.

### Key Findings

Ordered list. Each finding is a specific, evidence-backed claim.

1.
2.

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

- Type: knowledge, skill, tool, backlog-item
- Description: Synthesis methodology; thematic clustering method; contradiction detection design; synthesis output format and `Research/synthesis/` directory convention; `synthesis` skill draft; `synthesise.yml` workflow design; ADR if new directory/file type introduced
- Links:
  - `Research/backlog/2026-03-03-knowledge-linking-connected-corpus.md` (link graph input dependency)
  - `Research/backlog/2026-03-02-research-quality-assurance-methodology.md` (individual item quality complement)
  - `Research/completed/2026-02-27-information-synthesis-entropy.md` (theoretical grounding)
