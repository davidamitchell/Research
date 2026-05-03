---
title: "What structured knowledge-gap tracking and automatic backlog-promotion patterns exist in Personal Knowledge Management (PKM) and research systems, and which design is most suitable for a YAML Ain't Markup Language (YAML) frontmatter file-based corpus?"
added: 2026-05-02T06:11:10+00:00
status: reviewing
priority: medium  # low | medium | high
blocks: []  # slugs (filename without .md) of backlog items that cannot start until this one is complete
tags: [workflow, research-tooling, organisational-learning, knowledge-graph]
started: 2026-05-03T04:45:58+00:00
completed: ~
output: []  # skill | tool | agent | knowledge | backlog-item
cites:
  - 2026-03-03-cross-item-synthesis-meta-insights
  - 2026-05-02-cross-item-synthesis-knowledge-map-architecture
related:
  - 2026-03-12-exploration-synthesis-gap
  - 2026-03-03-research-agenda-curation-coverage
superseded_by: ~
supersedes: ~
item_type: primary
confidence: medium
versions: []
---

# What structured knowledge-gap tracking and automatic backlog-promotion patterns exist in Personal Knowledge Management (PKM) and research systems, and which design is most suitable for a YAML Ain't Markup Language (YAML) frontmatter file-based corpus?

## Research Question

What structured knowledge-gap tracking and automatic backlog-promotion patterns exist in Personal Knowledge Management (PKM) systems (Zettelkasten, Obsidian, Roam Research, Logseq) and academic research management tools, how do they handle unresolved questions that recur across multiple notes or papers, and which design, specifically for a YAML frontmatter field in a file-based Markdown corpus with a Python aggregation script, provides the best balance between structured data quality, minimal agent overhead, and reliable automatic promotion of persistently unresolved gaps into new research backlog items?

## Scope

**In scope:**
- PKM systems: Zettelkasten, Obsidian, Roam Research, and Logseq, specifically how each handles open questions, unanswered notes, and recurring gaps
- Academic research management: how systematic review tools and evidence-synthesis frameworks record evidence gaps, uncertainty, and future research implications
- Knowledge gap aggregation design patterns: deduplication strategies, occurrence counting, and promotion thresholds
- YAML field design: what fields best capture a gap, and how to balance expressiveness with aggregation reliability
- Aggregation script design: how to read gap fields from frontmatter, deduplicate, count occurrences, and write a structured `gap_registry.json` JavaScript Object Notation (JSON) registry file
- Failure modes: sparse or low-quality gap strings that defeat deduplication, over-promotion of trivially similar gaps, and agent overhead that discourages gap tracking

**Out of scope:**
- Full-text semantic gap extraction from body text
- Gap tracking in non-file-based systems that require a persistent database
- Automated execution of gap research after promotion

**Constraints:**
- Expand all acronyms on first use
- The design must work with Python 3.11+ and standard library plus YAML parsing; no external database or vector index required
- The YAML field must be writable by a Large Language Model (LLM) agent with a simple instruction such as "list 1-5 open questions this item could not answer"

## Context

W-0040 in `BACKLOG.md` proposes a `gaps:` YAML frontmatter field, an `aggregate_gaps.py` script, and automatic promotion of gaps appearing in three or more items. [fact; source: https://github.com/davidamitchell/Research/blob/main/BACKLOG.md]

The design choice matters because prior completed items in this repository already favor explicit provenance, heuristic-first aggregation, and layered selection over opaque whole-corpus inference. [fact; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-03-cross-item-synthesis-meta-insights.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-02-cross-item-synthesis-knowledge-map-architecture.md]

This item therefore asks a narrower implementation question: what is the lightest structured gap format that still scales beyond ad hoc note-level reminders and can reliably promote recurring unresolved questions into backlog items. [inference; source: https://github.com/davidamitchell/Research/blob/main/BACKLOG.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-03-cross-item-synthesis-meta-insights.md]

## Approach

1. **PKM system survey:** Review Zettelkasten, Obsidian, Roam Research, and Logseq patterns for surfacing recurring open questions and the data structure each pattern relies on.
2. **Academic research gap tracking review:** Review systematic review and evidence-synthesis guidance to see how evidence gaps and future research implications are structured.
3. **YAML field design options:** Compare free-text string lists, controlled vocabularies, and lightweight structured objects for LLM writeability and aggregation reliability.
4. **Deduplication strategy evaluation:** Compare exact matching, fuzzy string similarity, and embedding-based semantic similarity for short gap questions in a roughly 200-item file corpus.
5. **Promotion threshold analysis:** Compare threshold options and recommend the smallest threshold that avoids promoting one-off paraphrase noise.
6. **Design recommendation:** Produce a concrete frontmatter schema, registry schema, aggregation logic, and promotion rule.

## Sources

- [x] [Ahrens (2017) How to Take Smart Notes](https://www.soenkeahrens.de/en/takesmartnotes)
- [x] [Sascha (2025) Universal Questions for Any Note-Taking System](https://zettelkasten.de/posts/universal-questions-for-note-taking-system/)
- [x] [Sascha (2018) Structural Layers in Note Taking](https://zettelkasten.de/posts/three-layers-structure-zettelkasten/)
- [x] [Blacksmithgu Dataview Documentation](https://blacksmithgu.github.io/obsidian-dataview/)
- [x] [Blacksmithgu Dataview Data Commands](https://blacksmithgu.github.io/obsidian-dataview/queries/data-commands/)
- [x] [Blacksmithgu Dataview Query Types](https://blacksmithgu.github.io/obsidian-dataview/queries/query-types/#task)
- [ ] [Logseq Advanced Queries Documentation](https://docs.logseq.com/#/page/Advanced%20Queries) - official page is JavaScript-rendered and was not directly quotable in this session
- [ ] [Logseq Datalog Documentation](https://docs.logseq.com/#/page/datalog) - official page is JavaScript-rendered and was not directly quotable in this session
- [x] [Covidence Systematic Review Software](https://www.covidence.org/)
- [x] [Schunemann et al. (2024) Cochrane Handbook Chapter 14: Completing Summary of Findings tables and grading the certainty of the evidence](https://training.cochrane.org/handbook/current/chapter-14)
- [x] [Schunemann et al. (2024) Cochrane Handbook Chapter 15: Interpreting results and drawing conclusions](https://training.cochrane.org/handbook/current/chapter-15)
- [x] [Grading of Recommendations Assessment, Development and Evaluation (GRADE) Working Group Handbook](https://gdt.gradepro.org/app/handbook/handbook.html)
- [ ] [Rayyan Help: How to Add or Remove Labels and Exclusion Reasons in Rayyan](https://help.rayyan.ai/hc/en-us/articles/16759720118929-How-to-Add-or-Remove-Labels-and-Exclusion-Reasons-in-Rayyan) - official help page returned a Cloudflare interstitial in this session
- [ ] [Rayyan Help: Understanding Blinding, Labels, Reasons, and Ratings in Collaborative Reviews](https://help.rayyan.ai/hc/en-us/articles/35305653554705-Understanding-Blinding-Labels-Reasons-and-Ratings-in-Collaborative-Reviews) - official help page returned a Cloudflare interstitial in this session
- [x] [Zotero Documentation: Collections and Tags](https://www.zotero.org/support/collections_and_tags)
- [x] [Zotero Documentation: Searching and Saved Searches](https://www.zotero.org/support/searching)
- [x] [RapidFuzz Documentation](https://github.com/maxbachmann/RapidFuzz)
- [x] [Sentence Transformers Semantic Textual Similarity](https://www.sbert.net/docs/sentence_transformer/usage/semantic_textual_similarity.html)
- [x] [NVIDIA NeMo Semantic Deduplication](https://docs.nvidia.com/nemo-framework/user-guide/25.07/datacuration/semdedup.html)

---

## Research Skill Output

*(Full output from running the research skill, retained verbatim in the completed item. Sections 0-5 are the investigation, and section 6 seeds the Findings section below.)*

### §0 Initialise

- Question: determine which structured gap-tracking pattern from PKM and research systems best fits a YAML frontmatter corpus with file-based aggregation
- Scope: PKM patterns, systematic-review gap handling, field design, deduplication strategy, promotion threshold, and script design are in scope; full-text extraction and database-backed systems are out of scope
- Constraints: Python 3.11+, file-based operation, YAML-only authoring, low agent overhead, and no vector index as a baseline
- Output format: knowledge output with a concrete frontmatter schema, registry schema, aggregation logic, and promotion rule
- [fact] Prior work cross-reference: W-0040 already defines the desired capability, while prior repository research argues for explicit provenance and heuristic-first aggregation rather than opaque whole-corpus inference. [source: https://github.com/davidamitchell/Research/blob/main/BACKLOG.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-03-cross-item-synthesis-meta-insights.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-02-cross-item-synthesis-knowledge-map-architecture.md]

### §1 Question Decomposition

**A. PKM patterns**
- A1. How do mature PKM systems surface unresolved questions across many notes?
- A2. What data structures do those systems rely on: tags, metadata fields, tasks, block references, or structure notes?
- A3. What scaling limits appear when open questions are left as free text only?

**B. Academic review patterns**
- B1. How do systematic review frameworks represent uncertainty and future research needs?
- B2. What is structured versus free-form in those systems?
- B3. Do they prioritize gaps by recurrence or by decision relevance?

**C. Field design**
- C1. Is a free-text list sufficient for reliable aggregation?
- C2. Is a controlled vocabulary too costly for agents and humans?
- C3. What is the minimum structured object that materially improves deduplication?

**D. Deduplication**
- D1. What does exact matching do well and poorly?
- D2. What does fuzzy string matching do well and poorly?
- D3. What does embedding-based semantic matching require operationally?

**E. Promotion**
- E1. What threshold is high enough to avoid two-item noise?
- E2. What threshold is low enough to surface real recurring gaps before the corpus is much larger?

**F. Recommendation**
- F1. What frontmatter schema should this repository adopt now?
- F2. What registry schema should the script emit?
- F3. What matching and promotion policy is the best first implementation?

### §2 Investigation

#### 2.1 PKM and note-system patterns

- [fact] Zettelkasten practice on zettelkasten.de treats long-run note systems as future-oriented tools that need explicit entry points rather than retrieval alone, and warns that tags do not scale well because they dilute connections as note volume grows. [source: https://zettelkasten.de/posts/universal-questions-for-note-taking-system/]
- [fact] The same Zettelkasten guidance says direct links with explanations and topic entry points are more durable than a growing undifferentiated tag cloud. [source: https://zettelkasten.de/posts/universal-questions-for-note-taking-system/]
- [fact] The structural-layers article says full-text search and tags are sufficient only for a smaller archive, after which hub notes and then structure notes emerge to organize recurring themes. [source: https://zettelkasten.de/posts/three-layers-structure-zettelkasten/]
- [fact] Obsidian Dataview is a live index and query engine over note metadata, including YAML frontmatter, inline fields, tags, tasks, and links, and it keeps queries automatically up to date. [source: https://blacksmithgu.github.io/obsidian-dataview/]
- [fact] Dataview query commands can select notes by tag, folder, or link, and task queries operate at task level rather than only at page level. [source: https://blacksmithgu.github.io/obsidian-dataview/queries/data-commands/; https://blacksmithgu.github.io/obsidian-dataview/queries/query-types/#task]
- [inference] The strongest PKM pattern is not "infer open questions from prose later" but "capture open questions in a queryable surface now, then use dynamic queries or structure notes to surface them later." [source: https://zettelkasten.de/posts/universal-questions-for-note-taking-system/; https://zettelkasten.de/posts/three-layers-structure-zettelkasten/; https://blacksmithgu.github.io/obsidian-dataview/]
- [assumption] Access note: the official Logseq advanced-query pages were JavaScript-rendered in this session, so Logseq is treated as a supporting pattern rather than an anchor source. The raw exported page still exposed a Datalog-style block model with `block/tags` and `block/refs`, which is directionally consistent with block-level query patterns. [source: https://docs.logseq.com/#/page/Advanced%20Queries; https://docs.logseq.com/#/page/datalog]

#### 2.2 Academic evidence-gap and review-system patterns

- [fact] Covidence presents itself as a collaborative systematic review platform optimized for faster reviews and distributed review-team workflow, but its public marketing surface emphasizes workflow management rather than a public, fine-grained gap-schema model. [source: https://www.covidence.org/]
- [fact] Cochrane Chapter 14 states that Summary of Findings tables present the main findings of a review in a transparent, structured, and simple tabular format, including important outcomes and certainty of evidence. [source: https://training.cochrane.org/handbook/current/chapter-14]
- [fact] Cochrane Chapter 15 states that reviews inform future research and that author conclusions are explicitly divided into implications for practice and implications for research. [source: https://training.cochrane.org/handbook/current/chapter-15]
- [fact] The GRADE handbook describes GRADE outputs as evidence summaries plus graded recommendations built on a transparent, structured assessment of certainty. [source: https://gdt.gradepro.org/app/handbook/handbook.html]
- [fact] Zotero supports detailed item tags, collections, and continuously updated saved searches, including searches across tags and note text. [source: https://www.zotero.org/support/collections_and_tags; https://www.zotero.org/support/searching]
- [inference] Academic review systems separate two layers: structured evidence judgments that are easy to aggregate, and narrative interpretation that explains them. They do not depend on semantic clustering of arbitrary prose as the primary control surface. [source: https://training.cochrane.org/handbook/current/chapter-14; https://training.cochrane.org/handbook/current/chapter-15; https://gdt.gradepro.org/app/handbook/handbook.html; https://www.zotero.org/support/searching]
- [assumption] Access note: Rayyan's official help center URLs were behind a Cloudflare challenge in this session, so Rayyan is not used as an anchor source for the recommendation. [source: https://help.rayyan.ai/hc/en-us/articles/16759720118929-How-to-Add-or-Remove-Labels-and-Exclusion-Reasons-in-Rayyan; https://help.rayyan.ai/hc/en-us/articles/35305653554705-Understanding-Blinding-Labels-Reasons-and-Ratings-in-Collaborative-Reviews]

#### 2.3 Deduplication strategy comparison

- [fact] RapidFuzz documents practical fuzzy string scorers such as ratio, token sort ratio, token set ratio, and weighted ratio, and notes that preprocessing materially affects similarity scores. [source: https://github.com/maxbachmann/RapidFuzz]
- [fact] RapidFuzz's token set ratio returns a perfect score when one string is a subset of another, which is useful for formatting variants but risky for over-merging questions that share a core phrase while differing in scope. [source: https://github.com/maxbachmann/RapidFuzz]
- [fact] Sentence Transformers semantic textual similarity computes embeddings for all texts and then compares them by cosine or other similarity metrics. [source: https://www.sbert.net/docs/sentence_transformer/usage/semantic_textual_similarity.html]
- [fact] NVIDIA NeMo's semantic deduplication workflow requires embedding generation, clustering, within-cluster pairwise similarity, duplicate thresholds, representative selection, unique identifiers, and threshold experimentation. [source: https://docs.nvidia.com/nemo-framework/user-guide/25.07/datacuration/semdedup.html]
- [inference] Exact matching after lowercase and punctuation normalization is too brittle for LLM-authored questions, because semantically identical gaps often differ by leading phrasing, token order, or qualifier words. [source: https://github.com/maxbachmann/RapidFuzz; https://www.soenkeahrens.de/en/takesmartnotes]
- [inference] Embedding-based semantic deduplication is disproportionate for a roughly 200-item YAML corpus because it introduces model selection, threshold tuning, clustering, and storage concerns that the current repository explicitly wants to avoid. [source: https://docs.nvidia.com/nemo-framework/user-guide/25.07/datacuration/semdedup.html; https://www.sbert.net/docs/sentence_transformer/usage/semantic_textual_similarity.html]
- [inference] The practical middle ground is bounded fuzzy comparison inside a coarse area bucket, with normalized exact matching first and fuzzy consolidation second, so obvious paraphrases merge while unrelated questions on different surfaces remain separate. [source: https://github.com/maxbachmann/RapidFuzz; https://docs.nvidia.com/nemo-framework/user-guide/25.07/datacuration/semdedup.html]

#### 2.4 Field-design comparison

- [fact] Dataview and Zotero both reward fields and tags that are easy to write and easy to query later, while Zettelkasten guidance warns that broad tags alone lose explanatory power as scale increases. [source: https://blacksmithgu.github.io/obsidian-dataview/; https://www.zotero.org/support/collections_and_tags; https://zettelkasten.de/posts/universal-questions-for-note-taking-system/]
- [inference] A pure free-text list is easiest for agents but leaves the aggregator with no boundary signal, so near-duplicate questions about different domains can collapse incorrectly. [source: https://blacksmithgu.github.io/obsidian-dataview/; https://github.com/maxbachmann/RapidFuzz]
- [inference] A full controlled taxonomy is better for aggregation but too costly at capture time for an agent prompt whose real job is to close an item, not classify a mini-ontology. [source: https://www.zotero.org/support/collections_and_tags; https://training.cochrane.org/handbook/current/chapter-15]
- [inference] The best balance is a lightweight structured object with one required natural-language field and one optional coarse classifier drawn from existing canonical tags or a short area list. [source: https://blacksmithgu.github.io/obsidian-dataview/; https://www.zotero.org/support/searching; https://zettelkasten.de/posts/three-layers-structure-zettelkasten/]

#### 2.5 Promotion-threshold comparison

- [fact] W-0040 currently defines promotion when a gap appears in three or more completed items. [source: https://github.com/davidamitchell/Research/blob/main/BACKLOG.md]
- [inference] A threshold of two distinct items is too noisy for agent-authored gap text because two mentions can arise from one local topic cluster, one fashionable framing, or one paraphrase family rather than a corpus-level structural gap. [source: https://github.com/davidamitchell/Research/blob/main/BACKLOG.md; https://github.com/maxbachmann/RapidFuzz]
- [inference] A threshold of five distinct items is too slow for the current corpus size, because it would delay promotion until a recurring gap had already accumulated substantial unresolved debt. [source: https://github.com/davidamitchell/Research/blob/main/BACKLOG.md; https://training.cochrane.org/handbook/current/chapter-15]
- [inference] Three distinct completed items is the best first threshold because it is high enough to reject most pairwise noise and low enough to surface genuinely repeated unanswered questions before they become entrenched. [source: https://github.com/davidamitchell/Research/blob/main/BACKLOG.md; https://training.cochrane.org/handbook/current/chapter-15]

#### 2.6 Concrete design recommendation evidence

- [inference] The repository should not try to reproduce academic evidence-taxonomy depth inside frontmatter. It should capture only the minimum data needed to aggregate and promote unanswered questions reliably. [source: https://training.cochrane.org/handbook/current/chapter-14; https://training.cochrane.org/handbook/current/chapter-15]
- [inference] The recommended frontmatter shape is:

  ```yaml
  gaps:
    - question: "What benchmark best predicts long-horizon coding-agent reliability?"
      area: evaluation
    - question: "What minimum evidence package should justify production deployment?"
      area: governance
  ```

  where `question` is required and `area` is optional but recommended. [source: https://blacksmithgu.github.io/obsidian-dataview/; https://www.zotero.org/support/collections_and_tags; https://github.com/davidamitchell/Research/blob/main/BACKLOG.md]
- [inference] The registry output should preserve both canonical and variant phrasing, for example `{canonical_question, area, variants, item_slugs, count, promote, backlog_slug}` rather than overwriting all variants into one silent merge result. [source: https://github.com/maxbachmann/RapidFuzz; https://github.com/davidamitchell/Research/blob/main/BACKLOG.md]
- [inference] Matching order should be: normalize exact match first, then compare only within the same `area` bucket using a bounded fuzzy threshold, and leave low-confidence clusters separate rather than auto-merging them. [source: https://github.com/maxbachmann/RapidFuzz; https://docs.nvidia.com/nemo-framework/user-guide/25.07/datacuration/semdedup.html]
- [inference] Embedding-based semantic deduplication should be deferred until there is evidence that structured questions plus bounded fuzzy matching still produce unacceptable false negatives at current corpus scale. [source: https://docs.nvidia.com/nemo-framework/user-guide/25.07/datacuration/semdedup.html; https://www.sbert.net/docs/sentence_transformer/usage/semantic_textual_similarity.html]

### §3 Reasoning

- [inference] The consistent pattern across PKM and research-review tools is "capture explicitly, query later." Systems scale when the author records the unresolved question in a bounded field or note type, not when a later process tries to infer all unresolved questions from rich narrative prose. [source: https://zettelkasten.de/posts/universal-questions-for-note-taking-system/; https://zettelkasten.de/posts/three-layers-structure-zettelkasten/; https://blacksmithgu.github.io/obsidian-dataview/; https://www.zotero.org/support/searching]
- [inference] This makes a pure free-text list too weak and a rich taxonomy too heavy. The gap field should be just structured enough to constrain matching, but not so structured that authors skip it or agents fill it poorly. [source: https://www.zotero.org/support/collections_and_tags; https://training.cochrane.org/handbook/current/chapter-15]
- [inference] Deduplication should follow the same principle as the rest of the repository's architecture: heuristics first, heavier semantic machinery later only if the simple layer proves inadequate. [source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-02-cross-item-synthesis-knowledge-map-architecture.md; https://docs.nvidia.com/nemo-framework/user-guide/25.07/datacuration/semdedup.html]
- [assumption] A short `area` classifier can reuse the repository's existing canonical tag vocabulary or a small hand-maintained area list without introducing enough overhead to discourage capture. [source: https://github.com/davidamitchell/Research/blob/main/docs/tag-vocabulary.md; https://blacksmithgu.github.io/obsidian-dataview/]

### §4 Consistency Check

- [fact] The PKM evidence and the academic-review evidence both favor explicit structure plus later aggregation rather than fully unstructured narrative capture. [source: https://zettelkasten.de/posts/three-layers-structure-zettelkasten/; https://training.cochrane.org/handbook/current/chapter-14]
- [fact] The deduplication sources do not conflict on the operational trade-off: fuzzy methods are cheaper than embedding pipelines, and embedding pipelines require additional model, clustering, and threshold choices. [source: https://github.com/maxbachmann/RapidFuzz; https://docs.nvidia.com/nemo-framework/user-guide/25.07/datacuration/semdedup.html; https://www.sbert.net/docs/sentence_transformer/usage/semantic_textual_similarity.html]
- [inference] The only material uncertainty is not whether structured gap capture is needed, but how much structure is the minimum that still reduces false merges. That is why the recommendation stops at `question` plus optional `area`, not a larger schema. [source: https://blacksmithgu.github.io/obsidian-dataview/; https://www.zotero.org/support/collections_and_tags]

### §5 Depth and Breadth Expansion

- [inference] From a technical lens, the recommended schema is intentionally small because file-based automation benefits from deterministic fields and low merge friction. A larger schema would produce more missing values, more agent inconsistency, and more review overhead than signal. [source: https://blacksmithgu.github.io/obsidian-dataview/; https://github.com/davidamitchell/Research/blob/main/BACKLOG.md]
- [inference] From a behavioral lens, open-question capture succeeds only if it feels like a short closing step. Academic review methods tolerate richer schemas because the whole workflow is already structured and labor-intensive; this repository should not import that whole burden. [source: https://training.cochrane.org/handbook/current/chapter-15; https://www.covidence.org/]
- [inference] From an information-architecture lens, the role of the registry is closer to a structure note or saved search than to a semantic knowledge graph. It is an entry point for recurring unresolved questions, not a full ontology of uncertainty. [source: https://zettelkasten.de/posts/three-layers-structure-zettelkasten/; https://www.zotero.org/support/searching]
- [inference] From a governance lens, a threshold of three promotes only repeated unresolved questions and leaves one-off uncertainties inside the item where they belong. That keeps the research backlog tied to repeated decision-value signals rather than to every local caveat. [source: https://github.com/davidamitchell/Research/blob/main/BACKLOG.md; https://training.cochrane.org/handbook/current/chapter-15]

### §6 Synthesis

**Executive Summary**

The best-fit design is a lightweight structured `gaps:` field whose entries store a required natural-language `question` and an optional coarse `area`, aggregated by normalized exact matching first and bounded fuzzy matching second, with promotion to backlog at three distinct completed-item mentions. [inference; source: https://blacksmithgu.github.io/obsidian-dataview/; https://www.zotero.org/support/searching; https://github.com/maxbachmann/RapidFuzz; https://github.com/davidamitchell/Research/blob/main/BACKLOG.md]

PKM systems and academic review methods converge on the same architectural lesson: recurring unknowns should be captured explicitly in a structured, queryable surface and then surfaced through dynamic aggregation, rather than inferred later from arbitrary prose. [inference; source: https://zettelkasten.de/posts/universal-questions-for-note-taking-system/; https://zettelkasten.de/posts/three-layers-structure-zettelkasten/; https://training.cochrane.org/handbook/current/chapter-14; https://training.cochrane.org/handbook/current/chapter-15]

Exact matching alone is too brittle for agent-authored question phrasing, while embedding-based semantic deduplication introduces model, clustering, and threshold complexity that is disproportionate for a file-based corpus of this size and constraint set. [inference; source: https://github.com/maxbachmann/RapidFuzz; https://docs.nvidia.com/nemo-framework/user-guide/25.07/datacuration/semdedup.html; https://www.sbert.net/docs/sentence_transformer/usage/semantic_textual_similarity.html]

The result should behave more like a saved search or structure note than like a full semantic platform: capture only enough structure to keep recurring gaps legible, deduplicated, and promotable. [inference; source: https://www.zotero.org/support/searching; https://zettelkasten.de/posts/three-layers-structure-zettelkasten/]

**Key Findings**

1. **Mature PKM systems surface recurring open questions through explicit metadata, links, tasks, or structure notes, and not by depending on later semantic inference over free-form narrative prose.** ([inference]; high confidence; source: https://zettelkasten.de/posts/universal-questions-for-note-taking-system/; https://zettelkasten.de/posts/three-layers-structure-zettelkasten/; https://blacksmithgu.github.io/obsidian-dataview/)
2. **Academic review frameworks separate structured evidence summaries from narrative interpretation, which means recurring uncertainty is made aggregatable by design before it becomes a research-priority conclusion.** ([inference]; high confidence; source: https://training.cochrane.org/handbook/current/chapter-14; https://training.cochrane.org/handbook/current/chapter-15; https://gdt.gradepro.org/app/handbook/handbook.html)
3. **A pure free-text `gaps:` list is too weak for reliable automatic promotion because it gives the aggregator no boundary signal and forces all deduplication decisions onto unstable question phrasing alone.** ([inference]; medium confidence; source: https://blacksmithgu.github.io/obsidian-dataview/; https://www.zotero.org/support/collections_and_tags; https://github.com/maxbachmann/RapidFuzz)
4. **A full controlled taxonomy is the wrong first design for this repository because it improves aggregation at the cost of much higher capture friction for humans and Large Language Model agents closing research items.** ([inference]; medium confidence; source: https://www.zotero.org/support/collections_and_tags; https://training.cochrane.org/handbook/current/chapter-15; https://www.covidence.org/)
5. **The best current frontmatter design is a lightweight object with `question` required and `area` optional but recommended, because that is the smallest schema that materially improves grouping without turning gap capture into ontology work.** ([inference]; medium confidence; source: https://blacksmithgu.github.io/obsidian-dataview/; https://www.zotero.org/support/searching; https://zettelkasten.de/posts/three-layers-structure-zettelkasten/)
6. **For a roughly 200-item file corpus, normalized exact matching followed by bounded fuzzy comparison inside the same `area` bucket is the best middle ground between brittleness and over-engineering.** ([inference]; medium confidence; source: https://github.com/maxbachmann/RapidFuzz; https://docs.nvidia.com/nemo-framework/user-guide/25.07/datacuration/semdedup.html)
7. **Embedding-based semantic deduplication should be deferred because the documented workflow requires embedding generation, clustering, threshold tuning, and model-choice governance that exceed this repository's baseline design constraints.** ([fact]; high confidence; source: https://docs.nvidia.com/nemo-framework/user-guide/25.07/datacuration/semdedup.html; https://www.sbert.net/docs/sentence_transformer/usage/semantic_textual_similarity.html)
8. **Promotion at three distinct completed-item mentions is the strongest first threshold because two-item recurrence is too noisy and five-item recurrence is too slow for the current corpus size and backlog-management goal.** ([inference]; medium confidence; source: https://github.com/davidamitchell/Research/blob/main/BACKLOG.md; https://training.cochrane.org/handbook/current/chapter-15)

**Evidence Map**

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [inference] PKM systems favor explicit capture plus later query, not latent inference from prose. | https://zettelkasten.de/posts/universal-questions-for-note-taking-system/; https://zettelkasten.de/posts/three-layers-structure-zettelkasten/; https://blacksmithgu.github.io/obsidian-dataview/ | high | Zettelkasten plus Dataview convergence |
| [inference] Academic review methods make uncertainty aggregatable through structured evidence summaries and explicit implications for research. | https://training.cochrane.org/handbook/current/chapter-14; https://training.cochrane.org/handbook/current/chapter-15; https://gdt.gradepro.org/app/handbook/handbook.html | high | Structured review outputs |
| [inference] Free-text-only gaps are too weak for reliable automatic promotion. | https://blacksmithgu.github.io/obsidian-dataview/; https://www.zotero.org/support/collections_and_tags; https://github.com/maxbachmann/RapidFuzz | medium | No boundary field for safe grouping |
| [inference] Full taxonomies impose too much capture overhead for this repository's closing workflow. | https://www.zotero.org/support/collections_and_tags; https://training.cochrane.org/handbook/current/chapter-15; https://www.covidence.org/ | medium | Review burden versus capture simplicity |
| [inference] `question` plus optional `area` is the minimum useful structured schema. | https://blacksmithgu.github.io/obsidian-dataview/; https://www.zotero.org/support/searching; https://zettelkasten.de/posts/three-layers-structure-zettelkasten/ | medium | Smallest schema with grouping signal |
| [inference] Normalized exact plus bounded fuzzy matching inside `area` is the best first dedupe layer. | https://github.com/maxbachmann/RapidFuzz; https://docs.nvidia.com/nemo-framework/user-guide/25.07/datacuration/semdedup.html | medium | Heuristic-first merge strategy |
| [fact] Embedding dedupe requires embeddings, clustering, thresholds, and model-choice decisions. | https://docs.nvidia.com/nemo-framework/user-guide/25.07/datacuration/semdedup.html; https://www.sbert.net/docs/sentence_transformer/usage/semantic_textual_similarity.html | high | Operational complexity is explicit |
| [inference] Three distinct mentions is the best first promotion threshold. | https://github.com/davidamitchell/Research/blob/main/BACKLOG.md; https://training.cochrane.org/handbook/current/chapter-15 | medium | Balance between noise and delay |

**Assumptions**

- [assumption] The optional `area` field can reuse existing canonical tags or a short hand-maintained area list without materially increasing capture burden. [source: https://github.com/davidamitchell/Research/blob/main/docs/tag-vocabulary.md; https://blacksmithgu.github.io/obsidian-dataview/]
- [assumption] Leaving uncertain fuzzy matches unmerged is preferable to aggressive auto-merging, because backlog promotion errors are costlier than a small number of false negatives in the first implementation. [source: https://github.com/maxbachmann/RapidFuzz; https://github.com/davidamitchell/Research/blob/main/BACKLOG.md]

**Analysis**

The evidence points toward a hybrid of PKM minimalism and systematic-review structure. [inference; source: https://zettelkasten.de/posts/three-layers-structure-zettelkasten/; https://training.cochrane.org/handbook/current/chapter-14]

PKM tools show that recurring questions become useful when they are queryable and connected to entry points, while academic review methods show that uncertainty only becomes decision-useful when it is expressed in a structured summary layer rather than buried in narrative discussion. [inference; source: https://blacksmithgu.github.io/obsidian-dataview/; https://www.zotero.org/support/searching; https://training.cochrane.org/handbook/current/chapter-15]

That combination rules out both extremes: free-text-only capture leaves too much ambiguity for reliable grouping, and a rich multi-field taxonomy would turn a low-friction closing step into a classification burden that this repository does not need. [inference; source: https://www.zotero.org/support/collections_and_tags; https://www.covidence.org/]

The matching trade-off is similar. Exact equality alone undercounts paraphrases, but embedding-based dedupe clearly belongs to a different operational class with model, clustering, and threshold choices that this repository has explicitly deferred elsewhere. [inference; source: https://github.com/maxbachmann/RapidFuzz; https://docs.nvidia.com/nemo-framework/user-guide/25.07/datacuration/semdedup.html; https://www.sbert.net/docs/sentence_transformer/usage/semantic_textual_similarity.html]

The clean first implementation is therefore deterministic normalization plus bounded fuzzy comparison within `area`, variant preservation in the registry, and promotion only when three distinct completed items converge on the same unresolved question family. [inference; source: https://github.com/maxbachmann/RapidFuzz; https://github.com/davidamitchell/Research/blob/main/BACKLOG.md]

**Risks, gaps, uncertainties**

- The recommendation relies more heavily on Cochrane, GRADE, and Zotero than on deep vendor-specific Rayyan and Covidence help documentation, so fine-grained product-behavior claims should be treated as medium-confidence extrapolations rather than as product-spec facts. [inference; source: https://training.cochrane.org/handbook/current/chapter-14; https://training.cochrane.org/handbook/current/chapter-15; https://gdt.gradepro.org/app/handbook/handbook.html; https://www.zotero.org/support/searching; https://www.covidence.org/]
- The exact fuzzy-threshold value still needs calibration against real corpus examples because W-0040 has not yet produced a historical `gaps:` dataset for threshold testing. [assumption; source: https://github.com/davidamitchell/Research/blob/main/BACKLOG.md; https://github.com/maxbachmann/RapidFuzz]
- The recommendation assumes most gap strings will be short, well-formed questions rather than long paragraph fragments, because bounded fuzzy matching is safer on concise prompts than on long descriptive text. [assumption; source: https://github.com/maxbachmann/RapidFuzz; https://blacksmithgu.github.io/obsidian-dataview/]
- False-positive and false-negative rates cannot yet be quantified empirically because the repository does not currently store structured historical gap entries. [fact; source: https://github.com/davidamitchell/Research/blob/main/BACKLOG.md]

**Open Questions**

- Should `area` reuse canonical tags directly, or should W-0040 define a smaller area vocabulary dedicated to gap clustering?
- Should the registry store a manual `canonical_question` override so reviewers can merge or split clusters without editing historical item frontmatter?
- Should promoted gaps create backlog items automatically, or first mark `promote: true` and let the loop create the backlog item only after checking for an existing equivalent slug?

### §7 Recursive Review

- Coverage audit: complete
- Claim-label audit: complete
- Acronym expansion audit: complete
- Inline citation audit: complete
- Synthesis and Findings parity: complete
- Material uncertainties: threshold calibration and incomplete vendor-help coverage remain explicit

---

## Findings

### Executive Summary

The best-fit design is a lightweight structured `gaps:` field whose entries store a required natural-language `question` and an optional coarse `area`, aggregated by normalized exact matching first and bounded fuzzy matching second, with promotion to backlog at three distinct completed-item mentions. [inference; source: https://blacksmithgu.github.io/obsidian-dataview/; https://www.zotero.org/support/searching; https://github.com/maxbachmann/RapidFuzz; https://github.com/davidamitchell/Research/blob/main/BACKLOG.md]

PKM systems and academic review methods converge on the same architectural lesson: recurring unknowns should be captured explicitly in a structured, queryable surface and then surfaced through dynamic aggregation, rather than inferred later from arbitrary prose. [inference; source: https://zettelkasten.de/posts/universal-questions-for-note-taking-system/; https://zettelkasten.de/posts/three-layers-structure-zettelkasten/; https://training.cochrane.org/handbook/current/chapter-14; https://training.cochrane.org/handbook/current/chapter-15]

Exact matching alone is too brittle for agent-authored question phrasing, while embedding-based semantic deduplication introduces model, clustering, and threshold complexity that is disproportionate for a file-based corpus of this size and constraint set. [inference; source: https://github.com/maxbachmann/RapidFuzz; https://docs.nvidia.com/nemo-framework/user-guide/25.07/datacuration/semdedup.html; https://www.sbert.net/docs/sentence_transformer/usage/semantic_textual_similarity.html]

The result should behave more like a saved search or structure note than like a full semantic platform: capture only enough structure to keep recurring gaps legible, deduplicated, and promotable. [inference; source: https://www.zotero.org/support/searching; https://zettelkasten.de/posts/three-layers-structure-zettelkasten/]

### Key Findings

1. **Mature PKM systems surface recurring open questions through explicit metadata, links, tasks, or structure notes, and not by depending on later semantic inference over free-form narrative prose.** ([inference]; high confidence; source: https://zettelkasten.de/posts/universal-questions-for-note-taking-system/; https://zettelkasten.de/posts/three-layers-structure-zettelkasten/; https://blacksmithgu.github.io/obsidian-dataview/)
2. **Academic review frameworks separate structured evidence summaries from narrative interpretation, which means recurring uncertainty is made aggregatable by design before it becomes a research-priority conclusion.** ([inference]; high confidence; source: https://training.cochrane.org/handbook/current/chapter-14; https://training.cochrane.org/handbook/current/chapter-15; https://gdt.gradepro.org/app/handbook/handbook.html)
3. **A pure free-text `gaps:` list is too weak for reliable automatic promotion because it gives the aggregator no boundary signal and forces all deduplication decisions onto unstable question phrasing alone.** ([inference]; medium confidence; source: https://blacksmithgu.github.io/obsidian-dataview/; https://www.zotero.org/support/collections_and_tags; https://github.com/maxbachmann/RapidFuzz)
4. **A full controlled taxonomy is the wrong first design for this repository because it improves aggregation at the cost of much higher capture friction for humans and Large Language Model agents closing research items.** ([inference]; medium confidence; source: https://www.zotero.org/support/collections_and_tags; https://training.cochrane.org/handbook/current/chapter-15; https://www.covidence.org/)
5. **The best current frontmatter design is a lightweight object with `question` required and `area` optional but recommended, because that is the smallest schema that materially improves grouping without turning gap capture into ontology work.** ([inference]; medium confidence; source: https://blacksmithgu.github.io/obsidian-dataview/; https://www.zotero.org/support/searching; https://zettelkasten.de/posts/three-layers-structure-zettelkasten/)
6. **For a roughly 200-item file corpus, normalized exact matching followed by bounded fuzzy comparison inside the same `area` bucket is the best middle ground between brittleness and over-engineering.** ([inference]; medium confidence; source: https://github.com/maxbachmann/RapidFuzz; https://docs.nvidia.com/nemo-framework/user-guide/25.07/datacuration/semdedup.html)
7. **Embedding-based semantic deduplication should be deferred because the documented workflow requires embedding generation, clustering, threshold tuning, and model-choice governance that exceed this repository's baseline design constraints.** ([fact]; high confidence; source: https://docs.nvidia.com/nemo-framework/user-guide/25.07/datacuration/semdedup.html; https://www.sbert.net/docs/sentence_transformer/usage/semantic_textual_similarity.html)
8. **Promotion at three distinct completed-item mentions is the strongest first threshold because two-item recurrence is too noisy and five-item recurrence is too slow for the current corpus size and backlog-management goal.** ([inference]; medium confidence; source: https://github.com/davidamitchell/Research/blob/main/BACKLOG.md; https://training.cochrane.org/handbook/current/chapter-15)

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [inference] PKM systems favor explicit capture plus later query, not latent inference from prose. | https://zettelkasten.de/posts/universal-questions-for-note-taking-system/; https://zettelkasten.de/posts/three-layers-structure-zettelkasten/; https://blacksmithgu.github.io/obsidian-dataview/ | high | PKM convergence |
| [inference] Academic review methods make uncertainty aggregatable through structured evidence summaries and explicit implications for research. | https://training.cochrane.org/handbook/current/chapter-14; https://training.cochrane.org/handbook/current/chapter-15; https://gdt.gradepro.org/app/handbook/handbook.html | high | Review-method convergence |
| [inference] Free-text-only gaps are too weak for reliable automatic promotion. | https://blacksmithgu.github.io/obsidian-dataview/; https://www.zotero.org/support/collections_and_tags; https://github.com/maxbachmann/RapidFuzz | medium | Missing boundary signal |
| [inference] Full taxonomies impose too much capture overhead for this repository's closing workflow. | https://www.zotero.org/support/collections_and_tags; https://training.cochrane.org/handbook/current/chapter-15; https://www.covidence.org/ | medium | Higher capture friction |
| [inference] `question` plus optional `area` is the minimum useful structured schema. | https://blacksmithgu.github.io/obsidian-dataview/; https://www.zotero.org/support/searching; https://zettelkasten.de/posts/three-layers-structure-zettelkasten/ | medium | Smallest useful schema |
| [inference] Normalized exact plus bounded fuzzy matching inside `area` is the best first dedupe layer. | https://github.com/maxbachmann/RapidFuzz; https://docs.nvidia.com/nemo-framework/user-guide/25.07/datacuration/semdedup.html | medium | Heuristic-first strategy |
| [fact] Embedding dedupe requires embeddings, clustering, thresholds, and model-choice decisions. | https://docs.nvidia.com/nemo-framework/user-guide/25.07/datacuration/semdedup.html; https://www.sbert.net/docs/sentence_transformer/usage/semantic_textual_similarity.html | high | Complexity explicit in docs |
| [inference] Three distinct mentions is the best first promotion threshold. | https://github.com/davidamitchell/Research/blob/main/BACKLOG.md; https://training.cochrane.org/handbook/current/chapter-15 | medium | Noise versus delay trade-off |

### Assumptions

- [assumption] The optional `area` field can reuse existing canonical tags or a short hand-maintained area list without materially increasing capture burden. [source: https://github.com/davidamitchell/Research/blob/main/docs/tag-vocabulary.md; https://blacksmithgu.github.io/obsidian-dataview/]
- [assumption] Leaving uncertain fuzzy matches unmerged is preferable to aggressive auto-merging, because backlog promotion errors are costlier than a small number of false negatives in the first implementation. [source: https://github.com/maxbachmann/RapidFuzz; https://github.com/davidamitchell/Research/blob/main/BACKLOG.md]

### Analysis

The evidence points toward a hybrid of PKM minimalism and systematic-review structure. [inference; source: https://zettelkasten.de/posts/three-layers-structure-zettelkasten/; https://training.cochrane.org/handbook/current/chapter-14]

PKM tools show that recurring questions become useful when they are queryable and connected to entry points, while academic review methods show that uncertainty only becomes decision-useful when it is expressed in a structured summary layer rather than buried in narrative discussion. [inference; source: https://blacksmithgu.github.io/obsidian-dataview/; https://www.zotero.org/support/searching; https://training.cochrane.org/handbook/current/chapter-15]

That combination rules out both extremes: free-text-only capture leaves too much ambiguity for reliable grouping, and a rich multi-field taxonomy would turn a low-friction closing step into a classification burden that this repository does not need. [inference; source: https://www.zotero.org/support/collections_and_tags; https://www.covidence.org/]

The matching trade-off is similar. Exact equality alone undercounts paraphrases, but embedding-based dedupe clearly belongs to a different operational class with model, clustering, and threshold choices that this repository has explicitly deferred elsewhere. [inference; source: https://github.com/maxbachmann/RapidFuzz; https://docs.nvidia.com/nemo-framework/user-guide/25.07/datacuration/semdedup.html; https://www.sbert.net/docs/sentence_transformer/usage/semantic_textual_similarity.html]

The clean first implementation is therefore deterministic normalization plus bounded fuzzy comparison within `area`, variant preservation in the registry, and promotion only when three distinct completed items converge on the same unresolved question family. [inference; source: https://github.com/maxbachmann/RapidFuzz; https://github.com/davidamitchell/Research/blob/main/BACKLOG.md]

### Risks, Gaps, and Uncertainties

- The recommendation relies more heavily on Cochrane, GRADE, and Zotero than on deep vendor-specific Rayyan and Covidence help documentation, so fine-grained product-behavior claims should be treated as medium-confidence extrapolations rather than as product-spec facts. [inference; source: https://training.cochrane.org/handbook/current/chapter-14; https://training.cochrane.org/handbook/current/chapter-15; https://gdt.gradepro.org/app/handbook/handbook.html; https://www.zotero.org/support/searching; https://www.covidence.org/]
- The exact fuzzy-threshold value still needs calibration against real corpus examples because W-0040 has not yet produced a historical `gaps:` dataset for threshold testing. [assumption; source: https://github.com/davidamitchell/Research/blob/main/BACKLOG.md; https://github.com/maxbachmann/RapidFuzz]
- The recommendation assumes most gap strings will be short, well-formed questions rather than long paragraph fragments, because bounded fuzzy matching is safer on concise prompts than on long descriptive text. [assumption; source: https://github.com/maxbachmann/RapidFuzz; https://blacksmithgu.github.io/obsidian-dataview/]
- False-positive and false-negative rates cannot yet be quantified empirically because the repository does not currently store structured historical gap entries. [fact; source: https://github.com/davidamitchell/Research/blob/main/BACKLOG.md]

### Open Questions

- Should `area` reuse canonical tags directly, or should W-0040 define a smaller area vocabulary dedicated to gap clustering?
- Should the registry store a manual `canonical_question` override so reviewers can merge or split clusters without editing historical item frontmatter?
- Should promoted gaps create backlog items automatically, or first mark `promote: true` and let the loop create the backlog item only after checking for an existing equivalent slug?

---

## Output

- Type: knowledge
- Description: Recommended a lightweight structured-gap design for W-0040: `gaps:` entries with required `question`, optional `area`, heuristic-first aggregation, and promotion at three distinct completed-item mentions. [inference; source: https://github.com/davidamitchell/Research/blob/main/BACKLOG.md; https://github.com/maxbachmann/RapidFuzz; https://training.cochrane.org/handbook/current/chapter-15]
- Links:
  - https://training.cochrane.org/handbook/current/chapter-15
  - https://blacksmithgu.github.io/obsidian-dataview/
  - https://github.com/maxbachmann/RapidFuzz
