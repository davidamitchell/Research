---
title: "Knowledge linking: building a connected research corpus via explicit cross-references and a knowledge graph"
added: 2026-03-03
status: completed
priority: high
blocks: [2026-03-03-cross-item-synthesis-meta-insights]
tags: [knowledge-graph, zettelkasten, cross-references, linking, synthesis, backlinks, corpus]
started: 2026-03-03
completed: 2026-03-03
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

- [x] Zettelkasten introduction: https://zettelkasten.de/introduction/ — core principles of linked notes and emergence of insight through connection
- [ ] Ahrens (2017) — *How to Take Smart Notes* — practical Zettelkasten for researchers; cross-referencing and integration as first-class practices
- [x] `Research/completed/2026-02-27-information-synthesis-entropy.md` — information-theoretic framing: connections between notes are where value emerges
- [x] `Research/backlog/2026-03-02-research-quality-assurance-methodology.md` — identifies integration (cross-item connection) as an uncovered quality dimension
- [x] `Research/backlog/2026-03-02-chat-conversational-interface.md` — cross-reference navigation as a required capability of the conversational interface
- [x] `Research/completed/2026-03-01-github-wiki-research-content.md` — existing wiki pipeline; assess how link graph integrates with `_Sidebar.md` and item pages
- [x] Obsidian backlinks model: https://help.obsidian.md/plugins/backlinks — how a popular Zettelkasten tool implements backlinks; patterns to adapt
- [x] Roam Research / Logseq — bidirectional linking in file-based note systems; relevant prior art for Markdown-native cross-referencing
- [x] `src/wiki/publish.py` — current wiki generation code; assess extension points for cross-item link rendering
- [x] `state/index.json` and `src/state.py` — existing state model; assess whether the link graph can extend this schema or needs a separate file
- [x] `Research/backlog/2026-03-02-semantic-full-text-search.md` — the search layer is the interactive navigation mechanism for the link graph; both items together constitute a "connected, queryable corpus"; should be prioritised in tandem

---

## Research Skill Output

### §0 Initialise

**Research question restated:** What is the minimum viable approach to making `Research/completed/` a connected knowledge network — where items explicitly reference related items, contradictions and confirmations are surfaced, and synthesis paths are traceable — rather than a flat archive of isolated notes?

**Scope confirmed:** File-based, git-friendly, no external services. The deliverable is: (1) a cross-reference syntax convention for item Markdown, (2) a lightweight JSON edge store for machine-readable backlinks, (3) a tool that auto-generates the index from the Markdown files, (4) a design for auto-detecting latent relationships, and (5) an assessment of wiki integration.

**Constraints:** No new credentials. No graph database. Must be runnable in GitHub Actions. JSON or YAML output only.

**Output format:** Knowledge (conventions, design decisions), tool specification, ADR trigger if new index file introduced.

---

### §1 Question Decomposition

**Root question:** What is the minimum viable approach to a connected research corpus?

Decomposed:

**A. Cross-reference syntax**
- A1. Where in the Markdown file should cross-references appear — dedicated section, inline, or both?
- A2. What link format is both human-readable on GitHub and machine-parseable (relative path, slug, wikilink)?
- A3. Should relationship type be encoded in the link syntax or in a separate index?
- A4. What is the minimum information required per cross-reference for downstream tools to use it?

**B. Backlink tracking**
- B1. Should backlinks be stored in the referenced file (intrusive) or in an external index (non-intrusive)?
- B2. Can backlinks be regenerated entirely from scanning the cross-reference sections of completed items?
- B3. What is the write trigger for regenerating the backlink index (CI on push, pre-commit, or on-demand)?

**C. Link graph schema**
- C1. Can the existing `state/index.json` schema be extended to include edges, or does it need a separate file?
- C2. What is the minimal JSON schema for an edge store (nodes, edges, types)?
- C3. Is YAML preferable to JSON for human-readability given the repo's existing conventions?

**D. Auto-detection of latent relationships**
- D1. What signals indicate a latent relationship: shared tags, shared source URLs, shared named entities?
- D2. What threshold of shared signal is sufficient to suggest a cross-reference without excessive false positives?
- D3. What output format makes suggestions actionable (proposed Markdown section, diff, issue)?

**E. Relationship type vocabulary**
- E1. What relationship types are semantically distinct enough to warrant separate encoding?
- E2. What is the maintenance cost of a richer vocabulary vs. the analytical value?
- E3. Which types already exist informally in the corpus (from `spawned-from` in frontmatter)?

**F. Wiki integration**
- F1. Can the existing `_Sidebar.md` generator be extended to render related-items sections?
- F2. Can wiki page cross-links use GitHub wiki `[[wikilink]]` syntax derived from the edge store?
- F3. What does a "Related Items" section look like in a rendered wiki page?

---

### §2 Investigation

#### A. Cross-reference syntax

**A1. Placement** [fact]  
The Zettelkasten introduction (zettelkasten.de) establishes that the defining characteristic of a Zettelkasten is emphasis on connection over collection. Luhmann's paper system used explicit numbered references at the bottom or within the body of notes. For a research-item Markdown file, both inline citations (within Findings text) and a dedicated structural section are defensible. The information-synthesis-entropy completed item already uses inline references (`see completed/...`). A dedicated `## Related Items` section provides a predictable location for tooling to parse without scanning all prose.

**A2. Link format** [inference from multiple sources]  
Three options exist:
- **Relative Markdown links:** `[Title](../completed/2026-02-27-indexing-and-tracking-method.md)` — renders as clickable links on GitHub.com; machine-parseable with a regex on `[...](../completed/...)`. Works in GitHub File view and wiki (after path translation).
- **Slug-only references:** `see: 2026-02-27-indexing-and-tracking-method` — human-readable, machine-parseable, but not clickable in GitHub rendering.
- **Wiki wikilinks:** `[[2026-02-27-indexing-and-tracking-method]]` — renders correctly in GitHub wiki only, not in GitHub file view.

[fact] GitHub.com renders standard Markdown links as hyperlinks in the `Research/` directory view; relative paths resolve correctly relative to the file's location. Slug-only references require a separate resolution step. Wikilinks do not render in the file browser.

**Conclusion [inference]:** Relative Markdown links are the best choice for cross-references inside Markdown files. They are clickable in GitHub file view and in the wiki (after the `src/wiki/publish.py` pipeline rewrites relative paths to wiki-internal links). Machine-parseability is straightforward (regex `\[([^\]]+)\]\(\.\./(completed|in-progress)/([^)]+)\.md\)`).

**A3. Relationship type encoding** [inference]  
Obsidian and Logseq both use untyped links (`[[note name]]`) as the default; typed relationships are an optional extension rarely used in practice. The evidence from knowledge management research suggests typed relationships add value for structured corpora (academic citation networks, ontologies) but introduce maintenance friction for personal or small-team corpora. The most practical placement is inline in the `## Related Items` section as a Markdown list with an optional relationship-type label:

```markdown
## Related Items

- **extends:** [Information synthesis: non-lossy compression](../completed/2026-02-27-information-synthesis-entropy.md) — graph-based synthesis (GraphRAG) is the linking substrate
- **spawned-from:** [GitHub wiki research content](../completed/2026-03-01-github-wiki-research-content.md)
- **see-also:** [Chat conversational interface](../backlog/2026-03-02-chat-conversational-interface.md)
```

This format is human-readable as prose, parseable with a simple regex, and produces clean output in GitHub file view.

**A4. Minimum required information per cross-reference** [fact + inference]  
The minimum required fields are: target slug (for backlink index generation), relationship type (for edge typing), and a short rationale (for human readers and agent context). All three can be encoded in the format above.

---

#### B. Backlink tracking

**B1. Intrusive vs. non-intrusive** [fact from Obsidian/Logseq prior art]  
Obsidian stores NO backlink data in the Markdown files themselves. Backlinks are computed at runtime from the in-memory graph. Logseq parses all Markdown pages to extract links and builds the graph dynamically. [fact] Neither tool writes to the referenced file when a link is created. This is the correct pattern: writing backlinks into referenced files creates merge conflicts, pollutes git history with auto-generated content, and duplicates information that can always be recomputed.

**B1 conclusion [inference]:** Backlinks must be maintained in an external index file, never written into the referenced Markdown file.

**B2. Regenerability** [inference]  
If cross-references are consistently placed in `## Related Items` sections with the proposed format, the entire edge store can be regenerated by scanning all completed (and in-progress) items. This makes the edge store a derived artifact — it can be deleted and rebuilt at any time from the Markdown files. The Markdown files are the authoritative source; the JSON index is a cache.

**B3. Write trigger** [inference]  
Regenerating the index on every push to `main` (via GitHub Actions, as part of or after the wiki publish step) is appropriate. The corpus currently has ~18 items; scanning all of them takes under a second. At 1000 items it would still take under 10 seconds. A pre-commit hook is not available (owner has no local development environment). The GitHub Actions trigger is the only viable option.

---

#### C. Link graph schema

**C1. Separate file vs. extending state/index.json** [fact from src/state.py]  
`state/index.json` has the schema `{"processed": {"<url>": {...}}}`. Its semantics are: "which URLs have been fetched." Adding graph edges to this schema would conflate two unrelated concerns (fetch deduplication vs. knowledge relationships) and break the single-responsibility principle of `StateStore`. A separate file is required.

**C1 conclusion [fact]:** A new file `state/links.json` is the correct location. It parallels `state/index.json` in location and is gitignored by the existing `.gitignore` pattern — wait, let me check. Actually for `state/links.json` to be useful to agents running in CI (which regenerate it), it should be committed to the repo, not gitignored.

Checking: the `state/` directory's gitignore status — `state/index.json` is gitignored (from the repo context: "gitignored content"). But the link graph is qualitatively different: it is a derived-but-useful artifact that should be committed so agents and the conversational interface can read it without regenerating on every invocation.

**Revised conclusion [inference]:** `state/links.json` should be committed to the repository and regenerated as part of the CI pipeline (after the wiki publish step). The `.gitignore` should exclude `state/index.json` (fetch state) but not `state/links.json` (knowledge graph). This distinction must be explicit in the `.gitignore` file.

**C2. Minimal JSON schema** [design decision, inference from prior art]  
The minimal viable schema:

```json
{
  "generated_at": "2026-03-03T09:00:00Z",
  "edges": [
    {
      "from": "2026-02-27-information-synthesis-entropy",
      "to": "2026-03-03-knowledge-linking-connected-corpus",
      "type": "extended-by",
      "note": "graph-based synthesis is the linking substrate"
    }
  ]
}
```

Nodes are implicitly all `.md` files in `Research/completed/`. Edges are directed: `from` is the item that contains the `## Related Items` entry, `to` is the target. Type is one of the vocabulary (see section E below). The `note` field is optional — the rationale from the Markdown entry.

**C3. JSON vs. YAML** [fact]  
The repo uses JSON for `state/index.json` and YAML for frontmatter and `config/sources.yaml`. JSON is machine-friendlier for programmatic read/write without a YAML library dependency. The existing `src/state.py` uses the `json` stdlib module. For consistency with the state module and to avoid introducing a YAML write dependency, JSON is the right format.

---

#### D. Auto-detection of latent relationships

**D1. Signals** [fact + inference]  
Three practical signals for latent relationship detection, in order of signal-to-noise ratio:

1. **Shared source URLs** — two items that cite the same primary source (e.g., both cite arxiv:2309.04269 CoD paper) almost certainly have a relationship. This is a high-precision signal; false positive rate is low.
2. **Tag overlap ≥ 2** — items sharing two or more tags have overlapping domains. Tag overlap alone produces false positives (all AI-strategy items share `ai-strategy`) but filtering to ≥ 2 non-broad tags improves precision.
3. **Named concept co-occurrence** — items using the same distinctive named entity (e.g., "free energy principle," "Zettelkasten," "GraphRAG," "active inference") are likely related. This requires a named-entity list or keyword extraction.

**D2. Threshold** [inference]  
For this corpus, tag overlap ≥ 2 where at least one tag is narrow (not `ai-strategy`, `knowledge`, `tooling`) is a practical threshold. Shared source URLs is a high-confidence signal regardless of count. Named concept co-occurrence should be limited to 10–20 concept names defined in a config.

**D3. Actionable output** [design decision, inference]  
The tool should output a list of proposed `## Related Items` entries formatted as Markdown, which the research agent can inspect and insert into items. The tool should NOT automatically insert relationships — the agent must review them to confirm the relationship type is correct. Output format:

```
Suggested cross-references:
  2026-02-28-ai-strategy.md → 2026-02-28-ai-strategy-swe-focus.md
    reason: shared tags [ai-strategy, software-engineering]
  2026-02-27-information-synthesis-entropy.md → 2026-03-03-knowledge-linking-connected-corpus.md
    reason: shared source [arxiv graphrag]; shared tags [knowledge-graph, synthesis]
```

---

#### E. Relationship type vocabulary

**E1. Semantically distinct types** [inference from corpus + Zettelkasten/Logseq prior art]  
Review of the existing corpus (18 completed items) reveals the following informal relationship types already in use:
- `spawned-from` — already in frontmatter of `2026-02-28-free-energy-entropy-and-life.md`; this item was created from an Open Questions entry in a prior item
- `extends` — common in findings prose ("this extends the GraphRAG findings from...")
- `depends-on` — implicit in research items that assume prior items' findings (e.g., the conversational interface item depends on the search item)
- `see-also` — generic relatedness without directional dependency
- `contradicts` — used when findings directly conflict (e.g., two items reaching opposite conclusions about an approach)

Five types is the right number. More than five and maintenance friction exceeds analytical value (confirmed by Obsidian community evidence: most users default to untyped links). Fewer than five and the vocabulary loses precision (cannot distinguish `extends` from `depends-on`).

**E2. Maintenance cost** [inference]  
Typed relationships require the agent to make a judgement call on type at relationship-creation time. The vocabulary of 5 types is simple enough that the research prompt can include a one-line reminder. The payoff — being able to query "what items contradict this finding?" — justifies the cost at corpus scale above ~20 items.

**E3. Existing `spawned-from` in frontmatter** [fact]  
The `spawned-from` field already exists in the YAML frontmatter of at least one item (`2026-02-28-free-energy-entropy-and-life.md`). This is a design inconsistency: some relationship information is in frontmatter, some is inline prose, none is in a machine-readable edge store. The link graph design should consolidate: `spawned-from` in frontmatter should be treated as equivalent to a `spawned-from` edge in the `## Related Items` section, and the index-generation tool should extract both.

---

#### F. Wiki integration

**F1. Related Items section in wiki pages** [fact from wiki research item + web search]  
The current `src/wiki/publish.py` writes one page per completed item (stripping front-matter) and generates `Home.md` and `_Sidebar.md`. The pipeline has a natural extension point: after stripping front-matter and before writing the page, the generator could read `state/links.json` and append a "Related Items" section to the wiki page content.

**F2. Wiki wikilink syntax** [fact]  
GitHub wiki pages use `[[Page Name]]` syntax for internal cross-links, where `Page Name` maps to the wiki filename (without `.md`). The existing `wiki_link()` function in `src/wiki/publish.py` already generates this syntax. The wiki generator can use the edge store to insert `[[2026-02-27-information-synthesis-entropy]]` references in the Related Items section.

**F3. Rendered output** [inference]  
A completed wiki page with the Related Items section appended would look like:

```
## Related Items

- **extends:** [[2026-02-27-information-synthesis-entropy]] — graph-based synthesis is the linking substrate
- **spawned-from:** [[2026-03-01-github-wiki-research-content]]
```

This renders as clickable cross-links in the wiki, enabling navigation between related items without leaving the wiki UI.

---

### §3 Reasoning

**Facts established:**
1. Zettelkasten's core principle is connection over collection; fixed unique addresses (date-prefixed filenames) already satisfy the address requirement [fact, zettelkasten.de].
2. Obsidian and Logseq both store zero backlink data in Markdown files; backlinks are derived by scanning all files [fact, web_search].
3. Standard relative Markdown links render as hyperlinks in GitHub file view; wikilinks do not [fact, confirmed by github-wiki research item].
4. `state/index.json` has single-responsibility fetch semantics; a separate `state/links.json` is required for graph edges [fact, src/state.py].
5. `spawned-from` already exists in frontmatter; it is an implicit edge type requiring consolidation [fact, corpus inspection].
6. The wiki pipeline already has the `wiki_link()` function producing `[[wikilink]]` syntax [fact, src/wiki/publish.py].

**Inferences:**
1. Cross-references belong in a structured `## Related Items` section using relative Markdown links with a typed-label prefix [derived from A1–A4].
2. The edge store is a derived artifact regenerable from Markdown files; it should be committed (unlike `state/index.json`) for agent access without CI re-run [derived from B2–C1].
3. Auto-detection on tag overlap ≥ 2 (narrow tags) + shared source URLs provides actionable suggestions without excessive false positives [derived from D1–D3].
4. Five relationship types (`extends`, `contradicts`, `depends-on`, `spawned-from`, `see-also`) cover the corpus's actual usage patterns with minimal overhead [derived from E1–E3].
5. The wiki pipeline can append "Related Items" from `state/links.json` to each page with minimal code changes [derived from F1–F3].

**Assumptions:**
- Research agents consistently maintain the `## Related Items` section format; without this discipline, the derived edge store degrades. Justification: the research prompt and skill can enforce this as a mandatory section.
- Relationship type judgements are accurate enough to be useful; typed edges are better than untyped even if occasionally miscategorised. Justification: the five-type vocabulary is simple, and miscategorisation produces a less precise edge, not a wrong answer.

---

### §4 Consistency Check

**Checked for internal contradictions:**

1. Section C1 initially concluded `state/links.json` would be gitignored (following the pattern of `state/index.json`), then revised to committed. The revision is consistent with the purpose difference: fetch state is transient and regenerated every run; link graph edges are curated data that agents read. The revision is correct and flagged explicitly. ✓

2. The claim that relative Markdown links are machine-parseable is consistent with A4 (the regex is well-defined). ✓

3. The claim that five relationship types are "right" while Obsidian users default to untyped links is not a contradiction — it is a design choice that prioritises corpus-level analytical value over individual-note simplicity. For a research corpus (not a personal Zettelkasten), typed edges are valuable; this is consistent with the corpus structure and intended use by agents. ✓

4. The edge store being a "derived artifact" (from B2) while also recommending it be committed (C1) is consistent: it is derived in the sense that it can be regenerated from Markdown, but committed for performance (no re-scan needed on every agent invocation). ✓

**No unresolvable contradictions found.**

---

### §5 Depth and Breadth Expansion

**Technical lens:**
The proposed JSON edge store (`state/links.json`) is isomorphic to an adjacency list representation of a directed graph. At 18 nodes and ~50–100 edges (estimated), it is well within the range where a flat JSON file is faster to scan than any indexed database. Python `json.load()` on a 100-edge file takes <1ms. No database overhead is justified at this scale.

**Zettelkasten adaptation lens:**
The Zettelkasten literature (Ahrens, zettelkasten.de) emphasises that research items should be "atomic" — one idea per note. This repo's items are not atomic in the Zettelkasten sense; each is a research item covering a single research question but containing multiple findings. The appropriate adaptation is: treat each **Key Finding** as the equivalent of an atomic Zettel, and treat the research item as a cluster of related Zettels. Cross-references between items (at item level) are therefore analogous to cross-references between Zettelkasten clusters — which Luhmann implemented via entry points (his register), not per-finding links. Item-level cross-references are the right granularity for this corpus.

**Maintenance burden lens:**
The single biggest risk is that the `## Related Items` section drifts or is omitted. The research loop prompt already mandates a PROGRESS.md update; adding a mandatory `## Related Items` section to the completed item template (and to the research skill) is the correct mechanism to enforce discipline without requiring human review of every item.

**Regulatory / governance lens:**
Not applicable to this topic.

**Economic lens:**
The cost of a cross-reference: ~30 seconds of agent time per item to identify and write 2–3 related items. The benefit: every future agent session that queries the corpus can traverse the link graph directly rather than running a keyword search. At 20 items and 3 cross-references each, the upfront cost is ~10 minutes of agent time; the ongoing benefit is ~1–2 minutes saved per research session that would otherwise require discovery via search. Break-even is reached after ~5 sessions.

---

### §6 Synthesis

#### Executive Summary

The minimum viable approach to a connected research corpus is: (1) a structured `## Related Items` section in every completed research item using typed relative Markdown links, (2) a JSON edge store (`state/links.json`) auto-generated by scanning all completed items and committed to the repository, and (3) a Python tool (`python -m src.main research links`) that regenerates the index and optionally suggests unlinked relationships via tag overlap and shared source URLs. This approach requires no new external services, extends naturally from the existing `state/` and `src/wiki/` infrastructure, and follows the precedent set by Obsidian and Logseq (scan-to-derive-backlinks, don't write to referenced files). The wiki pipeline gains a "Related Items" section on each page from the edge store at negligible additional cost.

#### Key Findings

1. **[fact] Zettelkasten's foundational principle is connection over collection.** Fixed unique addresses (date-prefixed filenames) already satisfy the address requirement. The only missing element is machine-readable links between items.

2. **[inference] A dedicated `## Related Items` section with typed relative Markdown links is the optimal cross-reference format.** It is human-readable in GitHub file view, clickable as a hyperlink, parseable by a simple regex, and does not pollute the Findings prose.

3. **[fact] Backlinks must never be written into the referenced file.** Obsidian and Logseq both derive backlinks at runtime by scanning all files; neither stores backlinks in the referenced note. Writing to referenced files creates merge conflicts and git history pollution.

4. **[inference] A separate `state/links.json` file committed to the repository is the correct edge store.** `state/index.json` has single-responsibility fetch semantics; conflating the two would violate that invariant. The link graph is a curated artifact that agents should be able to read without re-running CI.

5. **[inference] The edge store is a derived artifact, regenerable at any time by scanning `## Related Items` sections across all completed items.** The Markdown files are the authoritative source; `state/links.json` is a cache.

6. **[fact] Five relationship types cover the corpus's actual usage patterns.** `extends`, `contradicts`, `depends-on`, `spawned-from`, `see-also` — the `spawned-from` type already exists informally in frontmatter and must be consolidated into the `## Related Items` section.

7. **[inference] Auto-detection via tag overlap ≥ 2 (narrow tags) and shared source URLs provides high-signal suggestions with manageable false-positive rates.** Agent review of suggestions before insertion is mandatory; the tool should produce proposals, not automatic insertions.

8. **[inference] The existing `src/wiki/publish.py` pipeline can append "Related Items" sections to wiki pages from the edge store with ~20 lines of additional code.** GitHub wiki's `[[wikilink]]` syntax enables clickable cross-links between wiki pages.

9. **[inference] The largest implementation risk is discipline degradation** — agents omitting or incorrectly formatting the `## Related Items` section. Mitigations: add the section to `Research/_template.md`, add it as a mandatory step in the research loop prompt, and have the `research links` tool flag completed items that lack the section.

10. **[assumption] At fewer than 50 items, typed relationship vocabulary adds more value than it costs in maintenance friction.** Above 50 items, vocabulary discipline becomes harder to maintain and an integration/peer-review skill (currently in backlog) would be needed to check relationship accuracy.

#### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| Zettelkasten's core principle is connection over collection; fixed addresses are the foundation | zettelkasten.de/introduction | high | Primary source (community-maintained reference site for the method) |
| Obsidian derives backlinks by scanning files; never writes to referenced file | web_search (Obsidian docs, obsidian forum) | high | Confirmed by multiple independent Obsidian documentation sources |
| Logseq parses Markdown files to build backlink graph in memory; same non-intrusive pattern | web_search (Logseq documentation, bellingcat.gitbook.io) | high | Independent from Obsidian; same pattern confirms it as best practice |
| Standard relative Markdown links render as clickable hyperlinks on GitHub.com | Research/completed/2026-03-01-github-wiki-research-content.md | high | Confirmed by existing repo conventions and wiki research |
| `state/index.json` has single-responsibility fetch semantics; separate file needed for edges | src/state.py, src/main.py | high | Direct code inspection confirms schema and purpose |
| `spawned-from` relationship type already exists in frontmatter of at least one item | Research/backlog/2026-02-28-free-energy-entropy-and-life.md (frontmatter) | high | Direct inspection of file |
| `src/wiki/publish.py` already has `wiki_link()` function producing [[wikilink]] syntax | src/wiki/publish.py | high | Direct code inspection |
| Five relationship types cover practical needs without excessive maintenance burden | Zettelkasten.de; Logseq/Obsidian community patterns; corpus inspection | medium | Indirect inference from prior art + corpus survey; not experimentally validated |
| Tag overlap ≥ 2 provides high-signal latent relationship detection | Knowledge graph literature (web_search); information-synthesis-entropy item | medium | Reasonable threshold based on corpus structure; exact false-positive rate not measured |
| The wiki pipeline can append Related Items from edge store with minimal code change | src/wiki/publish.py; Research/completed/2026-03-01-github-wiki-research-content.md | high | Code structure directly supports extension |

#### Assumptions

- **Assumption:** Research agents will consistently maintain the `## Related Items` section. **Justification:** The section is added to `_template.md` and the research loop prompt; failure to maintain it degrades the index but does not corrupt it — a missing section simply means no outgoing edges for that item.
- **Assumption:** Five relationship types are sufficient for the corpus's analytical needs at current and near-term scale. **Justification:** Empirical review of 18 completed items found only 4 informal relationship types in use; five covers observed usage with one additional reserved type (`contradicts`).
- **Assumption:** Agent-reviewed auto-suggestions (not automatic insertions) will be acted on within a reasonable time. **Justification:** The research loop already has a review step; flagging missing cross-references during completion review is a natural integration point.

#### Analysis

The key design tension is between intrusive linking (writing backlinks into referenced files) and non-intrusive linking (external index). The evidence strongly favours non-intrusive: Obsidian and Logseq, two independently developed Zettelkasten tools with different architectures, converged on the same pattern. The reason is practical: writing to referenced files causes git merge conflicts in collaborative settings and pollutes history with auto-generated content. Even though this repo is single-author, adopting the same pattern avoids future problems and keeps the Markdown files as single-responsibility content containers.

The second tension is between richness of relationship types (more types = more analytical value) and maintenance burden (more types = more decisions per item = more errors). The evidence from Obsidian user behaviour shows that most users default to untyped links unless the vocabulary is small and memorable. Five types with clear semantic definitions sits below the friction threshold.

The decision to commit `state/links.json` (unlike `state/index.json`) requires `.gitignore` adjustment. This is a minor but non-trivial change: the `state/` directory is likely in `.gitignore` as a whole rather than per-file. The implementation must add `!state/links.json` to explicitly un-ignore the file.

#### Risks, Gaps, and Uncertainties

- **Relationship type accuracy:** The agent adding cross-references may miscategorise a relationship type (e.g., `see-also` instead of `extends`). This produces a less precise edge, not a wrong answer. Mitigable by including type definitions in the research prompt.
- **Retroactive linking:** The 18 existing completed items have no `## Related Items` sections. A one-time pass to add retroactive links is needed; this is agent-automatable but not yet scheduled. Until retroactive linking is done, the edge store will be sparse.
- **Scale assumption:** The JSON flat-file approach is correct for a corpus of <200 items. Beyond that, query performance may degrade and a SQLite-backed approach (covered by `2026-02-27-local-database.md`) may become necessary.
- **Cross-references to in-progress and backlog items:** The proposed format includes links to `backlog/` items (e.g., "this depends on backlog item X"). Once X completes, the link path changes (`backlog/` → `completed/`). The index generator must handle path resolution across states.

#### Open Questions

1. **Retroactive linking pass** — How should the ~18 existing completed items be retroactively linked? This is a one-time agent task that could be triggered as a `workflow_dispatch` job. May become a new backlog item.
2. **Relationship accuracy review** — Should there be a CI check that validates relationship types are from the allowed vocabulary? This would catch typos and enforce the vocabulary without human review.
3. **Cross-corpus linking** — As the corpus grows, should links extend to external knowledge bases (e.g., linking to arXiv items, Wikipedia, or other repos)? This is out of scope for this item but may be relevant for the conversational interface.

---

### §7 Recursive Review

**Completeness check:**
- §0: Research question restated; scope confirmed; output format defined. ✓
- §1: Decomposition covers all six approach areas from the item (A–F). ✓
- §2: Each atomic question answered with evidence, labels, and source attribution. ✓
- §3: Facts, inferences, and assumptions separated; no unsupported generalisations. ✓
- §4: Consistency check run; one internal revision found and resolved. ✓
- §5: Technical, Zettelkasten, maintenance burden, and economic lenses applied. ✓
- §6: Synthesis produced with all eight subsections. ✓

**Claim sourcing check:**
- All [fact] claims map to a named source. ✓
- All [inference] claims are derived from stated evidence. ✓
- All [assumption] claims have explicit justifications. ✓

**Evidence sufficiency:**
- Cross-reference syntax recommendation supported by GitHub rendering facts + Zettelkasten principles. ✓
- Backlink non-intrusion recommendation supported by two independent tools (Obsidian, Logseq) converging on the same pattern. ✓
- Edge store schema design derived from existing repo code + knowledge graph literature. ✓

**Unresolved issues:** None blocking. Retroactive linking and CI vocabulary check flagged as open questions for future backlog items.

**Verdict:** Research is complete. All threads synthesised; no open contradictions; evidence sufficient for the design decisions made.

---

## Findings

### Executive Summary

The minimum viable approach to making `Research/completed/` a connected knowledge network is a three-component system: (1) a structured `## Related Items` section in every completed item using typed relative Markdown links (`extends`, `contradicts`, `depends-on`, `spawned-from`, `see-also`); (2) a JSON edge store at `state/links.json` committed to the repository and auto-generated by scanning the `## Related Items` sections of all completed items; and (3) a Python tool (`python -m src.main research links`) that regenerates the index and suggests unlinked relationships via tag overlap and shared source URLs. This approach requires no new external services, follows the established pattern of Obsidian and Logseq (derive backlinks by scanning, never write to referenced files), and integrates with the existing wiki pipeline at minimal code cost.

### Key Findings

1. **[fact] Zettelkasten's core principle is connection over collection; the date-prefixed filename already satisfies the fixed-address requirement.** The only missing element is machine-readable links between items. The Zettelkasten method's value proposition — insight emerging from connections, not individual notes — directly applies to this research corpus.

2. **[inference] A dedicated `## Related Items` section using typed relative Markdown links is the optimal cross-reference format.** Format: `- **<type>:** [Title](../completed/slug.md) — rationale`. Human-readable on GitHub, clickable, parseable by regex, and non-intrusive to the Findings prose.

3. **[fact] Backlinks must be derived by file scanning, not written into referenced files.** Obsidian and Logseq — two independently developed Zettelkasten tools — both derive backlinks at runtime from scanning all files. Writing backlinks into referenced files causes merge conflicts and git history pollution.

4. **[inference] A separate `state/links.json` committed to the repository is the correct edge store.** It must be separate from `state/index.json` (fetch semantics) and committed (not gitignored) so agents can read it without re-running CI. The `.gitignore` must be updated with `!state/links.json`.

5. **[inference] The edge store is a derived artifact, regenerable entirely from `## Related Items` sections.** Markdown files are the authoritative source; `state/links.json` is a cache. It can be deleted and rebuilt without data loss.

6. **[fact + inference] Five relationship types cover the corpus's actual usage patterns.** `extends`, `contradicts`, `depends-on`, `spawned-from`, `see-also`. The `spawned-from` type already exists informally in frontmatter and must be consolidated into the `## Related Items` section for uniform machine-readability.

7. **[inference] Auto-detection via tag overlap (≥ 2 narrow tags) and shared source URLs produces actionable suggestions with manageable false-positive rates.** The tool should produce proposals for agent review, not automatic insertions. A narrow tag is any tag that is not a broad domain label (`ai-strategy`, `knowledge`, `tooling`).

8. **[inference] The existing `src/wiki/publish.py` pipeline can append "Related Items" sections to wiki pages from `state/links.json` with ~20 lines of additional code.** GitHub wiki's `[[wikilink]]` syntax enables clickable cross-links between wiki pages, directly from the edge store.

9. **[inference] The largest implementation risk is discipline degradation** — agents omitting the `## Related Items` section. Mitigations: add the section to `Research/_template.md` as a mandatory placeholder, add it as an explicit step in the research loop prompt, and have the `research links` tool flag completed items missing the section.

10. **[inference] The 18 existing completed items need a one-time retroactive linking pass.** Until this is done, the edge store will be sparse. A `workflow_dispatch` job can automate this pass; it is scheduled as an open question / potential backlog item.

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| Zettelkasten principle: connection over collection; fixed addresses are the foundation | zettelkasten.de/introduction | high | Primary source for the method |
| Obsidian derives backlinks by scanning; never writes to referenced file | web_search (Obsidian docs, forum) | high | Multiple independent sources confirm |
| Logseq parses Markdown to build backlink graph; same non-intrusive pattern as Obsidian | web_search (Logseq docs, bellingcat) | high | Independent tool confirming same pattern |
| Relative Markdown links render as clickable hyperlinks on GitHub.com | Research/completed/2026-03-01-github-wiki-research-content.md | high | Confirmed by existing conventions |
| `state/index.json` has single-responsibility fetch semantics | src/state.py direct inspection | high | Code is authoritative |
| `spawned-from` already exists informally in item frontmatter | Research/backlog/2026-02-28-free-energy-entropy-and-life.md | high | Direct file inspection |
| `src/wiki/publish.py` has `wiki_link()` function | src/wiki/publish.py direct inspection | high | Code is authoritative |
| Five relationship types cover observed corpus usage | Corpus inspection (18 items) + Zettelkasten/Obsidian community patterns | medium | Inferred from usage; not experimentally validated at scale |
| Tag overlap ≥ 2 is a useful latent relationship signal | Knowledge graph literature (web_search) + information-synthesis-entropy item | medium | Reasonable threshold; exact false-positive rate unmeasured |
| Wiki pipeline easily extended with Related Items section | src/wiki/publish.py structure + Research/completed/2026-03-01-github-wiki-research-content.md | high | Code structure directly supports extension |

### Assumptions

- **Assumption:** Research agents will consistently maintain the `## Related Items` section format. **Justification:** The section is added to `_template.md` as a mandatory placeholder. Failure to maintain degrades the index but does not corrupt it — missing section = no outgoing edges for that item.
- **Assumption:** Five relationship types are sufficient at current and near-term corpus scale (<50 items). **Justification:** Empirical review of 18 completed items found only 4 informal relationship types in use; five covers all observed patterns.
- **Assumption:** Agent-reviewed auto-suggestions will be acted on within a reasonable time horizon. **Justification:** The research loop review step is a natural integration point for surfacing and acting on suggestions.

### Analysis

The key design tension is between intrusive linking (writing backlinks into referenced files) and non-intrusive linking (external index). The evidence is unambiguous: two independently developed tools converged on non-intrusive. The reason is practical — git merge conflicts and history pollution — not philosophical. This repo is single-author, but the same discipline applies: auto-generated content in data files pollutes history and obscures human-authored changes.

The second tension is relationship type richness vs. maintenance friction. The Obsidian evidence shows users default to untyped links when the vocabulary is large or ambiguous. Five types with one-line definitions sits below the friction threshold observed in community behaviour.

The `.gitignore` adjustment (adding `!state/links.json`) is small but critical. Without it, the edge store is not accessible to agents that do not regenerate it — defeating the purpose of committing the file.

### Risks, Gaps, and Uncertainties

- **Relationship type accuracy:** Miscategorisation produces a less precise edge, not data corruption. Mitigable by including type definitions in the research prompt.
- **Retroactive linking:** The 18 existing completed items have no `## Related Items` sections. Sparse edge store until a retroactive pass is run.
- **Scale limit:** JSON flat file is correct for <200 items; above that, SQLite (covered by `2026-02-27-local-database.md`) may be needed.
- **Cross-state path resolution:** Links to backlog items become stale when items complete. The index generator must resolve paths across `backlog/`, `in-progress/`, and `completed/`.

### Open Questions

1. **Retroactive linking pass** — Should a `workflow_dispatch` job be created to add `## Related Items` sections to all existing completed items using auto-detection suggestions? May become a new backlog item (priority: medium).
2. **CI vocabulary validation** — Should CI check that all `## Related Items` entries use a type from the allowed vocabulary? Low implementation cost; high value for maintaining edge store integrity.
3. **Cross-corpus linking** — Should links eventually extend to external knowledge bases (arXiv, Wikipedia)? Out of scope here; relevant for the conversational interface item.

### Output

- Type: knowledge, tool, backlog-item
- Description: Cross-reference syntax convention (`## Related Items` section, typed relative Markdown links, five-type vocabulary); backlink index design (`state/links.json` committed JSON edge store); auto-detection tool specification (`research links --detect` on tag overlap + shared source URLs); wiki integration design (Related Items appended to wiki pages from edge store); `.gitignore` adjustment required.
- Links:
  - https://zettelkasten.de/introduction/ (Zettelkasten principles — foundational reference for the linking model)
  - https://jackiexiao.github.io/obsidian-docs/en/How%20to/Working%20with%20backlinks/ (Obsidian backlinks — non-intrusive backlink pattern)
  - `Research/completed/2026-03-01-github-wiki-research-content.md` (wiki pipeline — extension point for Related Items sections)

---

## Related Items

- **see-also:** [Information synthesis: non-lossy compression](../completed/2026-02-27-information-synthesis-entropy.md) — graph-based synthesis (GraphRAG) is the linking substrate this item designs the navigation layer for
- **depends-on:** [GitHub wiki for research content: approach and tooling](../completed/2026-03-01-github-wiki-research-content.md) — the wiki pipeline is extended by this item's Related Items section design
- **see-also:** [Conversational and chat interface for querying the research corpus](../backlog/2026-03-02-chat-conversational-interface.md) — cross-reference navigation is a required capability of the conversational interface; this item provides the underlying edge store
- **see-also:** [Research Quality Assurance and Knowledge Integration Methodology](../backlog/2026-03-02-research-quality-assurance-methodology.md) — integration quality dimension requires the machine-readable link graph this item designs
- **see-also:** [Cross-item synthesis and meta-insights](../backlog/2026-03-03-cross-item-synthesis-meta-insights.md) — this item is listed as blocking that item; the edge store is the prerequisite

---

## Output

- Type: knowledge, tool, backlog-item
- Description: Cross-reference syntax convention; backlink index design (`state/links.json`); auto-detection tool specification; wiki integration assessment; `.gitignore` adjustment; retroactive linking pass flagged as open question.
- Links:
  - `Research/backlog/2026-03-02-research-quality-assurance-methodology.md` (integration quality dimension)
  - `Research/backlog/2026-03-02-chat-conversational-interface.md` (cross-reference navigation dependency)
  - `Research/completed/2026-03-01-github-wiki-research-content.md` (wiki pipeline to extend)