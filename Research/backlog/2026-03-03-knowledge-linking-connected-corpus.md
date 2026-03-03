---
title: "Knowledge linking: building a connected research corpus via explicit cross-references and a knowledge graph"
added: 2026-03-03
status: backlog
priority: high
blocks: [2026-03-03-cross-item-synthesis-meta-insights]
tags: [knowledge-graph, zettelkasten, cross-references, linking, synthesis, backlinks, corpus]
started: ~
completed: ~
output: [knowledge, tool, backlog-item]
---

# Knowledge linking: building a connected research corpus via explicit cross-references and a knowledge graph

## Research Question

What is the minimum viable approach to making the `Research/completed/` corpus a connected knowledge network — where items explicitly reference related items, contradictions and confirmations are surfaced, and synthesis paths are traceable — rather than a flat archive of isolated notes?

## Scope

**In scope:**
- Patterns for explicit cross-referencing between research items: link syntax, placement conventions, directionality (A → B vs. bidirectional)
- Backlink tracking: given that item B references item A, how does item A surface that relationship without manual maintenance?
- Lightweight knowledge graph options: can the `state/index.json` file or a companion JSON file represent edges (relationships) between items without a database?
- Tooling for auto-detecting latent relationships: items that share tags, terms, or cited sources but do not yet cross-reference each other
- Relationship types worth encoding: `confirms`, `contradicts`, `extends`, `depends-on`, `spawned-from`, `see-also`
- Zettelkasten-style linking for a file-based Markdown corpus: what the key principles are and which ones translate to this repo's structure
- Integration with the wiki (`publish-wiki.yml`): how cross-item links render in the wiki output and whether the sidebar or Home page can surface a graph view

**Out of scope:**
- Full graph database (Neo4j, ArangoDB) — must remain file-based and git-friendly
- Visual graph rendering in a web UI (a separate concern from the linking data structure)
- Linking within a single research item (internal headings, footnotes)

**Constraints:** No new external services or credentials. Any tooling must run in GitHub Actions. The graph representation must remain human-readable (JSON or YAML, not binary).

## Context

The `Research/completed/` corpus currently has ~17 items. Items reference each other inline (e.g., "see `2026-02-27-indexing-and-tracking-method.md`") but these references are unstructured prose, not machine-readable links. There is no backlink index: if item B says "this extends item A," item A has no record of that relationship.

As the corpus grows, the absence of explicit linking means two failure modes emerge:
1. **Rediscovery waste** — a new research item investigates a question already partially answered in a prior item, without the agent realising the prior item is relevant.
2. **Synthesis blindness** — when synthesising across items, the agent cannot identify which items form a cluster of related findings because the relationships are not machine-readable.

The `2026-03-02-chat-conversational-interface.md` backlog item includes "cross-reference navigation" as a required capability: "you asked about search; related items are local-database, local-index-vs-reference, and semantic-full-text-search." This requires a machine-readable link structure that the conversational interface can traverse.

The `2026-02-27-information-synthesis-entropy.md` completed item (information-theoretic framing of synthesis) and the Zettelkasten method both point to the same insight: value emerges not from individual notes but from the connections between them.

The `2026-03-02-research-quality-assurance-methodology.md` backlog item identifies "integration: whether findings from this item connect to, extend, or contradict findings from related completed items" as a quality dimension not yet covered by existing skills. A machine-readable link graph is the prerequisite for checking this automatically.

## Approach

1. **Zettelkasten principles audit** — Review Ahrens (2017) *How to Take Smart Notes* and the Zettelkasten introduction (zettelkasten.de) for the core principles of linked note-taking. Identify which principles apply to a research-item-level corpus (items are denser than Zettel atomic notes) vs. which require adaptation.

2. **Cross-reference syntax design** — Define a convention for cross-references in research item Markdown:
   - Where links appear: a dedicated `## Related Items` section, or inline citations in findings, or both?
   - Link format: relative Markdown links (`[title](../completed/slug.md)`) vs. slug-only references (`see: 2026-02-27-indexing-and-tracking-method`)?
   - Relationship type tagging: optional label (`extends:`, `contradicts:`, `depends-on:`) or free-form prose?
   - Assess: what format is both human-readable when browsing GitHub and machine-parseable for tooling?

3. **Backlink index design** — Design a lightweight backlink index (a JSON file, likely alongside `state/index.json`) that records all known edges between items. Structure: `{"edges": [{"from": "slug-a", "to": "slug-b", "type": "extends"}]}`. Assess: can this be generated automatically by scanning the `## Related Items` sections of all completed items, or does it require manual maintenance?

4. **Auto-detection of latent relationships** — Design a tool (`python -m src.main research links --detect`) that scans the completed corpus for items that share ≥2 tags, cite the same source URL, or use the same named concepts (DIKW, active inference, Zettelkasten) and suggests cross-references that have not been added yet. Assess: what is the false-positive rate and is this useful enough to build?

5. **Wiki integration** — Assess how cross-item links should render in the wiki. The current `publish-wiki.yml` + `src/wiki/publish.py` pipeline generates `Home.md` and `_Sidebar.md`. Could a "Related Items" section in the wiki page be generated from the backlink index? Could the `_Sidebar.md` include a cluster view (items grouped by shared tags or relationships)?

6. **Relationship type vocabulary** — Define and justify a minimal set of relationship types. Proposed: `extends` (adds to findings), `contradicts` (conflicts with a finding), `depends-on` (this item's findings assume the prior item's findings are correct), `spawned-from` (this item was created from an Open Questions entry in the prior item), `see-also` (related but not directionally dependent). Assess whether a richer vocabulary adds value or introduces maintenance burden.

7. **ADR decision** — If a new JSON index file for the link graph is introduced, this is a new storage approach requiring an ADR per AGENTS.md criteria.

## Sources

- [ ] Zettelkasten introduction: https://zettelkasten.de/introduction/ — core principles of linked notes and emergence of insight through connection
- [ ] Ahrens (2017) — *How to Take Smart Notes* — practical Zettelkasten for researchers; cross-referencing and integration as first-class practices
- [ ] `Research/completed/2026-02-27-information-synthesis-entropy.md` — information-theoretic framing: connections between notes are where value emerges
- [ ] `Research/backlog/2026-03-02-research-quality-assurance-methodology.md` — identifies integration (cross-item connection) as an uncovered quality dimension
- [ ] `Research/backlog/2026-03-02-chat-conversational-interface.md` — cross-reference navigation as a required capability of the conversational interface
- [ ] `Research/completed/2026-03-01-github-wiki-research-content.md` — existing wiki pipeline; assess how link graph integrates with `_Sidebar.md` and item pages
- [ ] Obsidian backlinks model: https://help.obsidian.md/plugins/backlinks — how a popular Zettelkasten tool implements backlinks; patterns to adapt
- [ ] Roam Research / Logseq — bidirectional linking in file-based note systems; relevant prior art for Markdown-native cross-referencing
- [ ] `src/wiki/publish.py` — current wiki generation code; assess extension points for cross-item link rendering
- [ ] `state/index.json` and `src/state.py` — existing state model; assess whether the link graph can extend this schema or needs a separate file
- [ ] `Research/backlog/2026-03-02-semantic-full-text-search.md` — the search layer is the interactive navigation mechanism for the link graph; both items together constitute a "connected, queryable corpus"; should be prioritised in tandem

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

- Type: knowledge, tool, backlog-item
- Description: Cross-reference syntax convention; backlink index design; auto-detection tool proposal; wiki integration assessment; ADR if new index file introduced
- Links:
  - `Research/backlog/2026-03-02-research-quality-assurance-methodology.md` (integration quality dimension)
  - `Research/backlog/2026-03-02-chat-conversational-interface.md` (cross-reference navigation dependency)
  - `Research/completed/2026-03-01-github-wiki-research-content.md` (wiki pipeline to extend)
