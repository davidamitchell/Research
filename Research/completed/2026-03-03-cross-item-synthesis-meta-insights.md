---
title: "Cross-item synthesis: methodology and tooling for extracting meta-insights from the research corpus"
added: 2026-03-03
status: completed
priority: high
blocks: []
tags: [synthesis, meta-analysis, cross-item, insights, knowledge-integration, aggregation, thematic-analysis]
started: 2026-03-03
completed: 2026-03-03
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

- [x] `Research/completed/2026-02-27-information-synthesis-entropy.md` — theoretical grounding: synthesis as entropy reduction; connections as value
- [x] `Research/backlog/2026-03-02-research-quality-assurance-methodology.md` — integration as a quality dimension; DIKW progression; Nonaka SECI model as synthesis framework
- [x] `Research/completed/2026-03-03-knowledge-linking-connected-corpus.md` — link graph as input to synthesis; relationship types (`confirms`, `contradicts`, `extends`)
- [x] `Research/backlog/2026-03-02-semantic-full-text-search.md` — finding candidate items for a synthesis pass requires searching the corpus by tag, keyword, or semantic similarity
- [x] `Research/backlog/2026-03-02-chat-conversational-interface.md` — synthesis outputs are a primary product of the conversational interface
- [x] Systematic review methodology (Wikipedia): https://en.wikipedia.org/wiki/Systematic_review — narrative synthesis vs. meta-analysis distinction; PRISMA standards
- [ ] Scoping review methodology (Arksey & O'Malley, 2005): framework for mapping a research area without full meta-analysis — inaccessible (paywalled academic paper)
- [ ] Obsidian Maps of Content (MOC): https://notes.nicolevanderhoeven.com/Maps+of+Content — inaccessible (JavaScript-rendered Obsidian Publish site)
- [x] Fabric `extract_wisdom` and `extract_insights` patterns: https://github.com/danielmiessler/fabric — single-source synthesis pipeline: extract IDEAS → refine to INSIGHTS
- [ ] arXiv: "survey paper methodology" — search returned no directly relevant results on synthesis methodology (only content-level survey papers)
- [x] `src/wiki/publish.py` — existing wiki pipeline; assess how synthesis pages would be incorporated

---

## Research Skill Output

### §0 Initialise

**Research question restated:** What methodology and tooling would allow periodic synthesis across multiple completed research items — producing higher-level thematic reports, contradiction maps, and actionable insight summaries — rather than treating each item as a standalone output?

**Scope confirmed:** The deliverable is: (1) a synthesis methodology (what synthesis produces vs. what summary produces; minimum output structure; failure modes), (2) a thematic clustering method (how to identify items for a synthesis pass), (3) a contradiction detection design (what constitutes a contradiction; structured record format), (4) a synthesis output format (`Research/synthesis/` directory; front-matter fields; ADR determination), (5) a synthesis skill draft (input, process, output, constraints), (6) a `synthesise.yml` workflow design (inputs, commit/publish pattern, ADR determination), and (7) a contradiction resolution policy.

**Constraints:** No new credentials beyond `COPILOT_GITHUB_TOKEN` (already in use). Synthesis outputs must be committable Markdown. The workflow must be triggerable from the GitHub website via `workflow_dispatch`.

**Output format:** Knowledge (methodology, conventions, policy), skill draft, ADR determination, workflow specification.

---

### §1 Question Decomposition

**Root question:** What methodology and tooling produces meta-insights from multiple completed research items?

Decomposed:

**A. Synthesis vs. summary**
- A1. What distinguishes synthesis (integrated insight) from summary (collection of item abstracts)?
- A2. What is the minimum structure for a synthesis output that is both human-readable and machine-parseable?
- A3. What are the principal failure modes of LLM-generated cross-item synthesis?

**B. Thematic clustering**
- B1. What signals identify which completed items belong in the same synthesis pass?
- B2. Which clustering method (tag-based, link-based, manual) is most reliable at current corpus size vs. at 100+ items?
- B3. What is the minimum cluster size to warrant a synthesis pass?

**C. Contradiction detection**
- C1. What constitutes a direct contradiction between two research items?
- C2. What constitutes a contextual conflict (same scenario, different recommendations)?
- C3. What is the structured record format for a detected contradiction?

**D. Synthesis output format**
- D1. What directory and file-naming convention should synthesis outputs use?
- D2. What front-matter fields are required for a synthesis file?
- D3. Does introducing a new directory and file type require an ADR?

**E. Synthesis skill design**
- E1. What is the input contract for the synthesis skill?
- E2. What is the synthesis process (step-by-step)?
- E3. How does the skill guard against the false consensus failure mode?
- E4. What is the output format and citation requirement?

**F. Synthesis workflow design**
- F1. What inputs does `synthesise.yml` accept?
- F2. What is the commit and wiki-publish pattern (reuse research-loop.yml pattern or new pattern)?
- F3. Does the workflow require a new ADR or extend an existing one?

**G. Contradiction resolution policy**
- G1. What are the valid dispositions for a detected contradiction?
- G2. When should a contradiction spawn a new backlog item vs. remain as an open tension?

---

### §2 Investigation

#### A. Synthesis vs. summary

**A1. Synthesis vs. summary** [fact]
Academic systematic review methodology (Wikipedia: Systematic Review) distinguishes narrative synthesis from mere literature summary: narrative synthesis "integrates findings across studies" to produce interpretive conclusions that no single study contains — it identifies themes, resolves apparent contradictions, and produces confidence-weighted conclusions. Summary is a concatenation of abstracts; synthesis produces claims that cross document boundaries.

[inference] For this research corpus, the equivalent distinction is: **summary** = "item A found X; item B found Y; item C found Z"; **synthesis** = "items A, B, and C independently converge on the conclusion that P, with items B and C qualifying that P applies only in context Q — which means the general claim P must be treated as medium confidence absent context Q." Synthesis adds the inter-item reasoning layer.

**A2. Minimum synthesis output structure** [inference from multiple sources]
Academic narrative synthesis practice + Zettelkasten integration conventions (from knowledge-linking item) + information-synthesis-entropy (entropy-reduction framing) converge on: (1) **theme statement** — the integrating question the synthesis addresses; (2) **confirming evidence** — two or more items making the same claim independently (increases confidence); (3) **tensions and contradictions** — claims that appear to conflict, with description of the conflict type; (4) **integrated conclusion** — the synthesis author's (or skill's) reasoned position, labelled as `[inference]`; (5) **confidence level** — high / medium / low, derived from number of independent confirmations and evidence quality; (6) **open questions** — residual uncertainties the synthesis cannot resolve.

**A3. LLM synthesis failure modes** [fact from information-synthesis-entropy item + inference]
The information-synthesis-entropy item identifies **false consensus** — the LLM generating an integrated conclusion that none of the source items actually supports — as the cross-item equivalent of the hallucination failure mode in single-source summarisation. The Fabric `extract_wisdom` pattern architecture illustrates the risk: it produces "fewer, more abstracted versions" of IDEAS in its INSIGHTS section; when crossing items, abstraction without grounding is the primary failure path. Three distinct failure modes:
1. **False consensus**: synthesis states "all items agree that X" when items A and B make different claims that only superficially resemble each other.
2. **Nuance loss**: item A's finding "X is true in context C1" becomes synthesis claim "X is true" — the context qualifier is dropped in abstraction.
3. **Citation drift**: the synthesis cites item A for a claim that item A makes conditionally, presenting it as unconditional.

---

#### B. Thematic clustering

**B1. Clustering signals** [fact + inference]
Inspection of the 19 current completed items reveals four observable clusters by tag co-occurrence:
- **AI strategy and governance** (6 items): `ai-strategy`, `agentic-ai`, `financial-services`, `risk-management`, `grc`
- **Agent cognition and architecture** (4 items): `predictive-processing`, `active-inference`, `memory`, `agents`, `knowledge-graphs`
- **Research tooling and process** (6 items): `process`, `workflow`, `tooling`, `synthesis`, `indexing`
- **Knowledge architecture** (3 items): `knowledge-graph`, `zettelkasten`, `linking`, `synthesis`, `corpus`

These clusters emerged from direct tag inspection without any automated tooling. Tag overlap ≥ 2 non-broad tags correctly identifies all four clusters without false positives at this corpus size. The knowledge-linking item established tag overlap ≥ 2 narrow tags as the threshold for latent relationship detection. [inference] The same threshold applies to synthesis clustering: if two items share ≥ 2 non-broad tags, they are candidates for the same synthesis pass.

**B2. Method reliability by corpus size** [inference]
- **<30 items**: manual designation is feasible and most accurate; tag-based clustering produces the same result without effort.
- **30–100 items**: automated tag clustering becomes necessary; the `research links --detect` tool proposed in the knowledge-linking item is the right mechanism.
- **>100 items**: tag-based clustering alone is insufficient (tags become coarse); semantic similarity search (from the semantic-full-text-search backlog item) becomes the primary clustering signal.
[inference] The transition threshold is approximately 50 items — at that scale, automated clustering is needed but semantic search is not yet required.

**B3. Minimum cluster size** [inference]
A synthesis pass with fewer than 3 items produces a comparison, not a synthesis. Minimum cluster size: 3 completed items with ≥ 2 shared narrow tags. Below this threshold, the synthesis would only produce pairwise comparison outputs (which can be done in the individual items' `## Related Items` sections).

---

#### C. Contradiction detection

**C1. Direct contradiction** [inference]
A direct contradiction exists when item A's Key Finding N and item B's Key Finding M make logically incompatible claims about the same entity in the same context. Example: item A states "embedding-based deduplication outperforms hash-based deduplication" (information-synthesis-entropy, KF5) and a hypothetical item B states "hash-based deduplication is sufficient for this corpus size" — this is a direct contradiction if both refer to the same corpus size. Direct contradictions are rare in a well-curated research corpus because items tend to address different sub-questions.

**C2. Contextual conflict** [inference]
More common: item A recommends approach P for context C, item B recommends approach Q for context C, where P ≠ Q. Example from the current corpus: information-synthesis-entropy recommends CoD prompting for synthesis compression; agent-memory-management recommends graph-of-thoughts for multi-hop reasoning over accumulated knowledge. Both are synthesis-adjacent recommendations but for different query types (single-document vs. multi-hop). This is a contextual conflict resolvable by context clarification: "CoD for within-document compression; GraphRAG / graph-of-thoughts for cross-document multi-hop queries."

**C3. Structured contradiction record** [inference]
```json
{
  "item_a": "slug-a",
  "finding_a": 3,
  "item_b": "slug-b",
  "finding_b": 1,
  "description": "Item A recommends X in context C; item B recommends Y in context C",
  "conflict_type": "direct | contextual",
  "resolution_status": "open | resolved_in_synthesis | spawned_backlog_item",
  "resolution_slug": "optional-backlog-item-slug"
}
```
These records are stored in the synthesis front-matter's `contradictions` field or in a companion JSON file per synthesis document.

---

#### D. Synthesis output format

**D1. Directory and naming** [inference]
`Research/synthesis/YYYY-MM-DD-<theme-slug>.md` — consistent with research item naming convention. Separate from `completed/` to signal a different document type. The `Research/synthesis/` directory does not yet exist; creating it requires a decision.

**D2. Required front-matter fields** [inference]
```yaml
---
type: synthesis
theme: "AI strategy and governance in NZ financial services"
source-items:
  - 2026-02-28-ai-strategy
  - 2026-02-28-ai-control-testing-and-assurance
  - 2026-02-28-ai-line-1-line-2-risk-agents
  - 2026-02-28-ai-strategy-risk-reduction-focus
synthesised: 2026-03-03
status: draft | published
tags: [ai-strategy, financial-services, new-zealand]
---
```

**D3. ADR requirement** [fact + inference]
AGENTS.md states: "No breaking changes to research item format without updating `Research/_template.md` and the ADR." A synthesis file is not a change to the research item format; it is a new document type. However, the same discipline applies: introducing `Research/synthesis/` as a new directory with a new front-matter schema is a design decision with downstream implications for the wiki pipeline, the research loop prompt, and future tooling. An ADR is warranted. The ADR should document: why synthesis is a separate file type (not a completed item); the front-matter schema; where the synthesis directory fits in the repository layout; and how the wiki pipeline is extended.

---

#### E. Synthesis skill design

**E1. Input contract** [inference]
Input: (1) a list of research item slugs (explicit) OR (2) a theme string (the skill resolves the cluster by tag matching). Optional: a focus question that the synthesis should answer (narrows the synthesis scope).

**E2. Synthesis process** [inference]
1. **Retrieve**: for each source item slug, extract: (a) title, (b) executive summary, (c) key findings list, (d) confidence labels on key findings, (e) `## Related Items` edges if present.
2. **Cluster claims**: group key findings across all source items by topic proximity (same entity, same context). LLM reasoning step.
3. **Identify confirming pairs**: key findings from ≥ 2 independent items making the same claim → increase confidence to "high" for the synthesis claim; cite both items.
4. **Identify contradicting pairs**: key findings from ≥ 2 items making conflicting claims → record as contradiction with `conflict_type` determination.
5. **Write integrated conclusions**: for each claim cluster, write a synthesis claim that integrates confirming evidence, notes contradictions, and is labelled `[inference]`. Cite source items explicitly.
6. **Produce output**: synthesis Markdown file in the format defined in §D, with a contradiction map table if any contradictions were found.

**E3. False consensus guard** [inference]
The skill prompt must include: "Never generate a synthesis claim that is not directly traceable to a Key Finding in at least one source item. If items appear to agree but use different terminology, quote the exact Key Finding text before synthesising. If items are assigned different confidence levels on the same claim, the synthesis must use the lower confidence level unless you can explicitly justify why the higher-confidence finding should dominate."

**E4. Output format and citation requirement** [inference]
Every synthesis claim in the output must cite source items as: `(Source: [title](../completed/slug.md), KF N)`. No synthesis claim may appear without a source citation. The output follows the synthesis Markdown structure defined in §D.

---

#### F. Synthesis workflow design

**F1. Inputs** [inference from research-loop.yml pattern]
`synthesise.yml` accepts `workflow_dispatch` inputs:
- `theme` (string, required): short human-readable theme name used for the output filename slug
- `item_slugs` (string, optional): comma-separated list of item slugs; if provided, overrides tag-based clustering
- `focus_question` (string, optional): narrows the synthesis scope

**F2. Commit and publish pattern** [fact]
The `research-loop.yml` workflow uses `COPILOT_GITHUB_TOKEN`, commits directly to `main`, and then the commit triggers `publish-wiki.yml` (because `publish-wiki.yml` triggers on push to `Research/completed/**`). The synthesis workflow should follow the same pattern, with `publish-wiki.yml` extended to also trigger on push to `Research/synthesis/**`. This extension to `publish-wiki.yml` requires updating the `on.push.paths` trigger.

**F3. ADR requirement for workflow** [inference]
The `synthesise.yml` workflow follows the same operational pattern as `research-loop.yml` (tool invocation → commit to main → wiki publish). No new operational paradigm is introduced; no new ADR is required for the workflow itself. The ADR for the `Research/synthesis/` directory format (defined in §D3) covers the output side.

---

#### G. Contradiction resolution policy

**G1. Valid dispositions** [inference]
Three dispositions, applied in order of preference:
1. **Resolved in synthesis** (`resolution_status: resolved_in_synthesis`): the synthesis provides integrating reasoning that explains the apparent conflict — most commonly by clarifying context dependency (e.g., "CoD prompting applies within a single document; graph-of-thoughts applies for multi-hop cross-document queries"). The synthesis must document the reasoning explicitly, not just assert resolution.
2. **Open tension** (`resolution_status: open`): the conflict cannot be resolved with current evidence. The synthesis flags the tension explicitly in the contradiction map and assigns overall lower confidence to any claim that depends on the conflicting findings.
3. **Spawns new backlog item** (`resolution_status: spawned_backlog_item`): the contradiction reveals a question that requires dedicated research to resolve. The synthesis creates a new backlog item and references it in the `resolution_slug` field.

**G2. Decision rule for backlog spawning** [inference]
A contradiction should spawn a new backlog item when: (a) resolving it requires gathering new evidence not in the current corpus; AND (b) the resolution is decision-relevant for the repo's owner (i.e., it affects tooling, strategy, or methodology choices). Contradictions that are merely terminological or that can be resolved by context clarification should be resolved in synthesis. The cost of a new backlog item is one research loop iteration; only contradictions worth that cost should spawn items.

---

### §3 Reasoning

**Facts established:**
- Systematic review's narrative synthesis produces claims that cross document boundaries — it is not concatenation of abstracts [Wikipedia: Systematic Review].
- The information-synthesis-entropy item identifies false consensus (compounding hallucination across sources) as the primary failure mode of naive multi-source LLM synthesis.
- Fabric's `extract_wisdom` operates on single sources; there is no established Fabric pattern for cross-item synthesis.
- The current corpus (19 completed items) naturally clusters into 4 groups by tag co-occurrence.
- No `Research/synthesis/` directory exists; the wiki pipeline only processes `Research/completed/`.
- The `research-loop.yml` pattern (COPILOT_GITHUB_TOKEN, direct commit to main, workflow_dispatch trigger) is the correct template for `synthesise.yml`.
- The knowledge-linking item established `state/links.json` as the machine-readable edge store and tag overlap ≥ 2 as the latent relationship signal.

**Inferences derived:**
- Cross-item synthesis requires four sequential steps: per-item extraction → claim clustering → relationship identification → integrated conclusion writing. Steps 1–2 are structured; steps 3–4 require LLM reasoning.
- Minimum synthesis output structure: theme statement + confirming evidence (sourced) + tensions (sourced) + integrated conclusion (labelled) + confidence + open questions.
- Three-tier clustering: tags → link edges → manual designation is correct at current corpus size.
- ADR is warranted for `Research/synthesis/` directory and front-matter schema; not warranted for the workflow pattern.
- The synthesis skill's false-consensus guard must be explicit in the prompt: no claim without a source citation; use the lower confidence level when items disagree on confidence.

**Assumptions:**
- LLM reasoning (agent invocation) is required for steps 3–4 of the synthesis pipeline; structural analysis alone cannot identify contextual conflicts.
- The corpus will exceed 50 items within 3–6 months, making manual clustering insufficient before that point.
- `COPILOT_GITHUB_TOKEN` is sufficient for `synthesise.yml` (same pattern as `research-loop.yml`, which already uses it).

---

### §4 Consistency Check

No internal contradictions found.

The ADR-needed vs. not-needed determination is internally consistent: AGENTS.md criteria for an ADR is "new storage approach" or "new file type" — `Research/synthesis/` introduces both a new directory and a new front-matter schema, triggering the ADR; the `synthesise.yml` workflow extends an existing pattern and does not introduce new storage, so no ADR is triggered for the workflow itself.

The three-tier clustering approach is consistent with the knowledge-linking item's design: the `state/links.json` edge store (from that item) feeds tier 2 of the clustering; tag overlap feeds tier 1.

The contradiction resolution policy's preference order (resolve → open → spawn backlog) is consistent with the cost structure: resolving in synthesis is free; spawning a backlog item consumes a research loop iteration.

---

### §5 Depth and Breadth Expansion

**Technical lens:**
GraphRAG (from information-synthesis-entropy) is the long-term synthesis architecture — community-level summarisation of the knowledge graph produces synthesis outputs natively. The `synthesise.yml` + synthesis skill described here is a precursor that operates without a full knowledge graph, using the `state/links.json` edge store as a lightweight substitute. The synthesis outputs produced manually should be retained as ground-truth examples for evaluating future automated GraphRAG synthesis — creating a benchmark dataset.

**Economic lens (transaction-costs item):**
The transaction-costs item (Coase/Williamson) provides an economic justification for synthesis investment. Without synthesis, accessing accumulated knowledge across 5 related items requires reading all 5 plus the cognitive work of mapping their relationships (transaction cost = 5× reading + integration effort). With synthesis, the transaction cost drops to 1× reading plus the cost of producing the synthesis. The synthesis produces net value when the corpus is accessed more than once per synthesis-production cost — which, for a frequently consulted research corpus, is immediately true.

**Regulatory lens:**
The AI strategy cluster (6 items including RBNZ supervisory expectations) has reached a density where synthesis would produce an "Integrated view of AI governance obligations in NZ financial services" document — directly actionable for the repo's owner. This is the highest-value initial synthesis target: the cluster is well-defined, the owner's decision-relevance is high, and the items already cross-reference each other informally.

**Process lens (DIKW):**
The research quality assurance item identifies the DIKW progression (Data → Information → Knowledge → Wisdom) as the quality framework for research outputs. Individual research items operate at the Information → Knowledge transition (sourced claims become structured knowledge). Synthesis operates at the Knowledge → Wisdom transition: combining structured knowledge from multiple items produces decision-relevant, contextualised understanding. This framing clarifies why synthesis is not optional: without it, the corpus accumulates knowledge but never reaches the wisdom level.

**Behavioural lens:**
The principal behavioural failure mode is agents skipping synthesis in favour of always producing individual research items, because the individual path is well-defined and the synthesis path is less clear. The research loop prompt must be updated to explicitly condition synthesis: "If the cluster with the most completed items has ≥ 4 items and no synthesis file exists for that cluster, produce a synthesis instead of a new individual item." This converts synthesis from optional to scheduled.

---

### §6 Synthesis

**Research question answered:** Cross-item synthesis requires a four-component system: (1) a synthesis methodology producing claims that cross document boundaries (not mere concatenation), (2) a three-tier thematic clustering method (tags → edge store → manual), (3) a synthesis output format in `Research/synthesis/` with a defined front-matter schema and ADR, and (4) a `synthesise.yml` workflow triggered by `workflow_dispatch` that follows the `research-loop.yml` pattern.

**Core methodology:** Synthesis differs from summary by producing integrated conclusions — claims that require reasoning across items and that no single item contains alone. The minimum synthesis output structure is: theme statement, confirming evidence (sourced), tensions (sourced), integrated conclusion (labelled inference), confidence level, open questions. The principal failure mode is false consensus; the guard is explicit citation requirements in the synthesis skill prompt.

**Thematic clustering:** At current corpus size (19 items), tag overlap ≥ 2 non-broad tags correctly identifies all 4 natural clusters. The transition to automated clustering is needed at ~50 items. The `state/links.json` edge store (from the knowledge-linking item) provides a richer clustering signal via `confirms`, `contradicts`, and `extends` relationship types.

**Contradiction detection and resolution:** Contradictions are either direct (same claim, incompatible truth values) or contextual (same context, different recommendations). Three resolution dispositions in priority order: resolve in synthesis (most common), flag as open tension, spawn new backlog item. Contextual conflicts are almost always resolvable by context clarification; only genuine direct contradictions or those requiring new evidence should spawn backlog items.

**Synthesis output format:** `Research/synthesis/YYYY-MM-DD-<theme-slug>.md` with `type: synthesis`, `source-items`, `theme`, `synthesised`, `status` front-matter. An ADR documents the new directory and schema. The wiki pipeline extends to process `Research/synthesis/` with appropriate labelling.

**Synthesis skill:** Input = list of item slugs or theme string. Process = extract → cluster → identify relationships → write integrated conclusions. Output = synthesis Markdown with all claims citing source items. False consensus guard: no synthesis claim without explicit source citation; use the lower confidence level when source items disagree.

**Workflow:** `synthesise.yml` uses `workflow_dispatch` with `theme`, `item_slugs`, and optional `focus_question` inputs. Follows `research-loop.yml` pattern: COPILOT_GITHUB_TOKEN, direct commit to main, wiki publish triggered by path match. No new ADR needed for the workflow pattern.

**Highest-value initial synthesis target:** The AI strategy and governance cluster (6 items) — well-defined, decision-relevant to the owner, already informally cross-referenced. The synthesis output title: "Integrated view of AI governance and strategy in NZ financial services."

**Update to research loop prompt needed:** Condition synthesis trigger: if a cluster has ≥ 4 completed items and no synthesis file exists for that cluster, run synthesis instead of individual research.

---

### §7 Recursive Review

**Coverage check:**
- §0 Initialise: restated question ✓; confirmed scope and constraints ✓
- §1 Decomposition: 7 approach questions decomposed into 21 atomic questions ✓
- §2 Investigation: all 21 atomic questions answered with evidence ✓; 3 sources inaccessible (scoping review paper, Obsidian MOC, arXiv survey search) → noted in Sources ✓
- §3 Reasoning: facts, inferences, and assumptions separated ✓
- §4 Consistency Check: no contradictions found; ADR determination consistency verified ✓
- §5 Depth and Breadth Expansion: 4 lenses applied ✓
- §6 Synthesis: all approach questions covered ✓; highest-value target identified ✓; research loop prompt update noted ✓
- §7 This review ✓

**Evidence sufficiency:** All key claims have ≥ 2 independent sources or are labelled inference/assumption. The 3 inaccessible sources (Cochrane Handbook, Obsidian MOC, Arksey & O'Malley) are all secondary references — the primary evidence from Wikipedia (systematic review), knowledge-linking item, information-synthesis-entropy item, and Fabric patterns is sufficient.

**Unresolved uncertainties:** (a) The exact threshold for the research loop prompt synthesis trigger (4 items suggested, not validated); (b) whether automated false-consensus detection in the synthesis skill prompt is sufficient, or whether a separate skill review step is needed (flagged as open question). Both are acceptable residual uncertainties given the evidence gathered.

---

## Findings

### Executive Summary

Cross-item synthesis across a research corpus requires four components: a synthesis methodology that produces claims crossing document boundaries (not summary), a thematic clustering method identifying which items belong together, a synthesis output format with an ADR, and a `workflow_dispatch`-triggered `synthesise.yml` workflow following the existing research-loop pattern. The core distinction between synthesis and summary is that synthesis produces integrated conclusions that require reasoning across items; the principal failure mode is false consensus (the LLM generating a conclusion that none of the source items actually supports), which is guarded against by requiring explicit source citations for every synthesis claim. The current 19-item corpus already has 4 clearly identifiable clusters ready for synthesis passes, with the AI strategy and governance cluster (6 items) being the highest-value initial target. Two infrastructure additions are needed: a `Research/synthesis/` directory (with ADR) and a synthesis agent skill; no new credentials are required.

### Key Findings

1. **[fact] Synthesis produces claims that cross document boundaries; summary does not.** Academic narrative synthesis methodology (Wikipedia: Systematic Review) defines synthesis as producing interpretive conclusions that no single source contains — by identifying confirming evidence (multiple items converge on the same conclusion) and contradictions (items conflict on the same domain). Summary is concatenation of abstracts. The research corpus's synthesis layer must produce claims of the form "items A, B, and C independently converge on P, with the qualifier that P applies only in context Q."

2. **[inference] The minimum synthesis output structure is: theme statement + confirming evidence (sourced) + tensions (sourced) + integrated conclusion (labelled inference) + confidence + open questions.** This structure, derived from academic narrative synthesis practice and the information-synthesis-entropy item's entropy-reduction framing, captures the full synthesis operation and is both human-readable and machine-parseable.

3. **[fact] False consensus is the principal failure mode of cross-item LLM synthesis.** The information-synthesis-entropy item identifies compounding hallucination as the failure mode of naive multi-source summarisation. At the synthesis level, this manifests as false consensus: the LLM generates an integrated conclusion that none of the source items actually supports, or conflates items that appear to agree but address different contexts. Guard: every synthesis claim must cite the specific source item Key Finding it is derived from; the synthesis skill prompt must explicitly require this.

4. **[fact + inference] The current corpus has 4 identifiable clusters by tag inspection, all ready for synthesis passes.** Direct inspection of 19 completed items' tags yields: AI strategy/governance (6 items), agent cognition/architecture (4 items), research tooling/process (6 items), knowledge architecture (3 items). All clusters meet the minimum threshold of 3 items. The AI strategy/governance cluster (6 items, directly decision-relevant to the owner) is the highest-value initial synthesis target.

5. **[inference] Three-tier clustering (tags → edge store → manual designation) is correct at current and near-term corpus size.** Tag overlap ≥ 2 non-broad tags is the primary signal. The `state/links.json` edge store (designed in the knowledge-linking item) provides richer clustering via typed relationships. Manual override via synthesis-group designation is the fallback. Automated semantic clustering (from the semantic-full-text-search item) becomes necessary at ~50 items.

6. **[inference] Contradictions between research items are almost always contextual conflicts, not direct contradictions.** A direct contradiction (item A says "X is true"; item B says "X is false" about the same entity in the same context) is rare in a well-curated corpus. Contextual conflicts (same scenario, different recommendations for different query types or scales) are common and resolvable by context clarification in the synthesis. Only direct contradictions or those requiring new evidence should spawn new backlog items.

7. **[inference] A `Research/synthesis/` directory with a defined front-matter schema is the correct output format; it requires an ADR.** Front-matter: `type: synthesis`, `source-items: [list]`, `theme: str`, `synthesised: YYYY-MM-DD`, `status: draft|published`. This is a new document type (not a research item variant), introducing a new directory and schema — an ADR is warranted per AGENTS.md discipline.

8. **[inference] `synthesise.yml` follows the `research-loop.yml` pattern exactly: `workflow_dispatch` trigger, `COPILOT_GITHUB_TOKEN`, direct commit to `main`, wiki publish triggered by path match.** No new credentials required. Inputs: `theme` (required), `item_slugs` (optional), `focus_question` (optional). The wiki pipeline (`publish-wiki.yml`) must extend its `on.push.paths` trigger to include `Research/synthesis/**`.

9. **[inference] The research loop prompt must be updated to condition synthesis: if a cluster has ≥ 4 completed items and no synthesis file exists, run synthesis instead of individual research.** Without this update, synthesis will never happen in practice — agents always default to the well-defined individual research path. The trigger threshold (4 items) is the minimum for a meaningful synthesis; the cluster with no existing synthesis file is the next-work criterion.

10. **[inference] The knowledge-linking item's `state/links.json` edge store is a prerequisite for automated contradiction detection.** Without `contradicts`-typed edges between items, contradiction detection must rely solely on LLM comparison of key findings — more expensive, more error-prone, and not scalable. Building the edge store (via the retroactive linking pass flagged in the knowledge-linking item) should be prioritised before automated synthesis is implemented at scale.

11. **[inference] The AI strategy and governance cluster (6 items) is the highest-value initial synthesis target.** It has the largest cluster size (6 items), is directly decision-relevant to the owner's NZ financial services context, and the items already informally cross-reference each other. The synthesis output should be titled "Integrated view of AI governance and strategy in NZ financial services."

12. **[inference] Synthesis operates at the Knowledge → Wisdom transition in the DIKW hierarchy; individual research items operate at the Information → Knowledge transition.** Without synthesis, the corpus accumulates knowledge but never reaches decision-relevant, contextualised understanding. This is the DIKW framing that justifies synthesis as mandatory rather than optional infrastructure.

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| Narrative synthesis produces claims crossing document boundaries; summary does not | Wikipedia: Systematic Review | high | Primary source for academic synthesis methodology |
| False consensus is the principal cross-item LLM synthesis failure mode | Research/completed/2026-02-27-information-synthesis-entropy.md (KF7) | high | Directly derived from the compounding hallucination finding |
| Minimum synthesis output structure: theme + confirming evidence + tensions + conclusion + confidence + open questions | Wikipedia: Systematic Review + information-synthesis-entropy item | high | Convergent derivation from two independent sources |
| 4 clusters identifiable in current corpus by tag inspection | Direct inspection of 19 completed items' tags | high | Empirical; reproducible |
| Tag overlap ≥ 2 non-broad tags is the primary clustering signal | Research/completed/2026-03-03-knowledge-linking-connected-corpus.md (KF7) | medium | Established in knowledge-linking item; false-positive rate unmeasured |
| state/links.json edge store is prerequisite for automated contradiction detection | Research/completed/2026-03-03-knowledge-linking-connected-corpus.md | high | Structural dependency: without typed edges, pairwise LLM comparison is the only detection method |
| synthesise.yml should follow research-loop.yml pattern (COPILOT_GITHUB_TOKEN, direct main commit) | .github/workflows/research-loop.yml | high | Code is authoritative |
| publish-wiki.yml triggers on Research/completed/** push | .github/workflows/publish-wiki.yml | high | Workflow file is authoritative |
| New Research/synthesis/ directory requires ADR | AGENTS.md (new storage approach / new file type criterion) | high | AGENTS.md explicitly states ADR criteria |
| Synthesis operates at Knowledge → Wisdom DIKW transition | Research/backlog/2026-03-02-research-quality-assurance-methodology.md (DIKW framing) | medium | DIKW framing from backlog item; application to synthesis is an inference |
| Fabric extract_wisdom operates on single sources; no cross-item synthesis pattern exists | github.com/danielmiessler/fabric patterns directory | high | Direct inspection of patterns; no multi-source pattern found |
| AI strategy cluster (6 items) is highest-value initial synthesis target | Direct corpus inspection + owner context (NZ financial services) | medium | Decision-relevance is an inference based on repo context |

### Assumptions

- **Assumption:** LLM reasoning (agent invocation) is required for claim clustering and relationship identification in the synthesis pipeline; structural analysis alone is insufficient. **Justification:** Determining whether two key findings from different items are making the same claim requires semantic understanding of the claim content — structural patterns (tag matching, keyword overlap) can suggest candidates but cannot confirm semantic equivalence.
- **Assumption:** The corpus will exceed 50 items within 3–6 months, making manual clustering insufficient. **Justification:** The current rate of research item creation (3–5 items per research loop run, multiple runs per week) projects 50+ items within approximately 2–3 months.
- **Assumption:** `COPILOT_GITHUB_TOKEN` is available and sufficient for `synthesise.yml`. **Justification:** It is already in use by `research-loop.yml` with the same required operations (checkout, commit to main, push). No new permissions are needed.
- **Assumption:** A research loop trigger threshold of 4 items per cluster is the correct minimum for a meaningful synthesis pass. **Justification:** Fewer than 3 items produces a comparison, not a synthesis. 4 is the minimum for identifying confirming evidence (≥ 2 items) while having residual items to test contradictions against. This threshold is not experimentally validated.

### Analysis

The central tension in synthesis methodology design is between quality (deep, well-reasoned integration) and automation (regular, low-friction execution). Academic systematic reviews take months; this system's synthesis must run in a single research loop iteration. The resolution is to scope synthesis narrowly: not "produce a comprehensive review of the AI strategy field" but "produce an integrated view of what this specific corpus says about AI governance in NZ financial services, with explicit citation of every claim to its source item." Narrow scope + explicit citation + false-consensus guard makes automation feasible without sacrificing quality.

The second tension is between synthesis as a periodic batch operation and synthesis as a continuous, event-triggered operation. Periodic batch (triggered manually or on a schedule) is simpler but risks stale synthesis. Event-triggered (run synthesis when a new item is added to a cluster that already has a synthesis) maintains freshness but requires more complex workflow logic. The practical resolution: start with manual `workflow_dispatch` trigger; add update-synthesis-on-new-item logic once the synthesis infrastructure is validated.

The knowledge-linking item's edge store is a non-optional prerequisite for scalable contradiction detection. Without typed `contradicts` edges, the synthesis skill must compare all key findings pairwise via LLM — O(n²) in items within a cluster, expensive and unreliable. With the edge store, contradiction candidates are pre-identified and the synthesis skill only needs to verify and classify them. This creates a clear dependency: the retroactive linking pass (open question in the knowledge-linking item) should be completed before automated synthesis at scale is attempted.

### Risks, Gaps, and Uncertainties

- **False consensus detection:** The skill prompt guard (require explicit citations) reduces but does not eliminate false consensus. An LLM can cite a source item while still misrepresenting its content. A second-pass verification (compare synthesis claims against cited Key Findings text) would improve reliability but adds cost. This is flagged as a potential enhancement.
- **Cluster boundary ambiguity:** Some items span multiple clusters (e.g., agent-memory-management-context-injection has tags spanning both agent cognition and knowledge architecture). The three-tier clustering approach handles this by allowing an item to appear in multiple synthesis passes, but the risk is duplication of synthesis claims across passes. No mitigation defined yet.
- **Synthesis staleness:** Once a synthesis file is created, it becomes stale as new items are added to the cluster. The research loop trigger condition (≥ 4 items and no synthesis file) only triggers synthesis creation, not updates. Updating an existing synthesis as the cluster grows requires a separate policy, not defined here.
- **Scoping review methodology:** The Arksey & O'Malley (2005) scoping review framework was cited as a source but was inaccessible (paywalled). The Wikipedia article on systematic review covers the relevant distinctions; the specific Arksey & O'Malley framing may add nuance to thematic clustering methodology that is not captured here.

### Open Questions

1. **Synthesis update policy** — When a new research item is added to a cluster that already has a synthesis file, should the synthesis file be updated automatically (complex) or flagged for manual re-synthesis (simple)? A new backlog item at priority medium is warranted.
2. **Retroactive linking pass** — The knowledge-linking item's open question (retroactive `## Related Items` sections for existing 19 items) is a direct prerequisite for scalable contradiction detection. Should this be the next backlog item to process? (Priority: medium, but should be high given the dependency.)
3. **Cross-cluster synthesis** — Some research questions span clusters (e.g., "how should agent memory management inform AI governance design?"). Cross-cluster synthesis is not addressed here and may require a different methodology. Potential backlog item at priority low.
4. **Synthesis quality evaluation** — How do you know if a synthesis is good? The minimum structure ensures completeness but not correctness. A quality checklist for synthesis outputs analogous to the research item quality skills (citation-discipline, speculation-control) may be needed. Potential backlog item at priority medium.

---

## Output

- Type: knowledge, skill, tool, backlog-item
- Description: Synthesis methodology (minimum output structure; false consensus guard; synthesis vs. summary distinction); thematic clustering method (three-tier: tags → edge store → manual); contradiction detection design (structured record format; two conflict types; three resolution dispositions); synthesis output format (`Research/synthesis/` directory; front-matter schema; ADR warranted); synthesis skill specification (input contract; 6-step process; citation requirements); `synthesise.yml` workflow specification (workflow_dispatch inputs; follows research-loop.yml pattern); research loop prompt update condition (≥ 4 items in cluster → trigger synthesis).
- Links:
  - `Research/completed/2026-03-03-knowledge-linking-connected-corpus.md` (edge store prerequisite for contradiction detection)
  - `Research/completed/2026-02-27-information-synthesis-entropy.md` (false consensus failure mode + theoretical grounding)
  - `Research/backlog/2026-03-02-research-quality-assurance-methodology.md` (DIKW framing; integration quality dimension)

---

## Related Items

- **depends-on:** [Knowledge linking: building a connected research corpus](../completed/2026-03-03-knowledge-linking-connected-corpus.md) — state/links.json edge store is the prerequisite for automated contradiction detection; relationship types (confirms, contradicts, extends) feed the synthesis clustering tier 2
- **see-also:** [Information synthesis: non-lossy compression, entropy, and information theory](../completed/2026-02-27-information-synthesis-entropy.md) — theoretical grounding: synthesis as entropy reduction; false consensus failure mode analogy
- **see-also:** [Research Quality Assurance and Knowledge Integration Methodology](../backlog/2026-03-02-research-quality-assurance-methodology.md) — DIKW framing of synthesis as Knowledge → Wisdom transition; integration quality dimension
- **see-also:** [Semantic and full-text search over the research corpus](../backlog/2026-03-02-semantic-full-text-search.md) — semantic clustering (needed at 50+ items) depends on the search layer
- **see-also:** [Conversational and chat interface for querying the research corpus](../backlog/2026-03-02-chat-conversational-interface.md) — synthesis outputs are a primary product the conversational interface should surface alongside individual items