---
title: "Knowledge retention: mechanisms for ensuring completed research is recalled and applied over time"
added: 2026-03-03T10:05:15+00:00
status: completed
priority: high
blocks: []
tags: [retention, recall, spaced-repetition, knowledge-decay, application, active-recall, knowledge-management]
started: 2026-03-03T10:05:15+00:00
completed: 2026-03-03T10:05:15+00:00
output: [knowledge, tool, backlog-item]
cites: []          # slugs of items this item directly depends on or quotes
related: []        # slugs of thematically connected items
superseded_by: ~   # slug of a later item that overrides this one (null if not superseded)
supersedes: ~      # slug of an older item this one replaces (null if not applicable)
item_type: primary # primary | synthesis
confidence: medium # high | medium | low
versions: []       # entries: {version: "1.0", sha: "<commit-hash>", changed: YYYY-MM-DD, progress: "<path>", summary: "<one-line>"}
---

# Knowledge retention: mechanisms for ensuring completed research is recalled and applied over time

## Research Question

What mechanisms ensure that knowledge from completed research items is retained, recalled when contextually relevant, and applied to decisions — rather than being archived indefinitely with no re-engagement pattern?

## Scope

**In scope:**
- The knowledge decay problem: how quickly does knowledge become inaccessible or forgotten when it is not actively re-engaged, and what evidence exists for this in personal knowledge management systems?
- Spaced repetition applied to research: can the principles of spaced repetition (Ebbinghaus forgetting curve, SM-2 algorithm) be applied to research findings rather than flashcard facts?
- Contextual recall: mechanisms that surface relevant completed research at the moment of need — when the owner is working on a related problem, starting a new research item, or asking a question in a chat interface
- Periodic digest: a scheduled workflow that selects a subset of completed items for review based on time since last re-engagement, and posts a brief summary for the owner to read
- Integration with the conversational interface (`2026-03-02-chat-conversational-interface.md`): how the chat interface can serve as a recall mechanism ("what do I know about X?" as active recall)
- Agent-side recall: how agents in a research session should proactively surface relevant prior research rather than treating each session as starting from zero

**Out of scope:**
- Formal flashcard systems (Anki, SuperMemo) requiring the owner to create and review cards — this is a personal research system, not a language-learning system; manual card creation is too high friction
- Learning science beyond what is directly applicable to a practical implementation for this system
- Memorisation of procedural skills (covered by agent skills submodule, not research items)

**Constraints:** Any re-engagement mechanism must be passively delivered (the owner does not take action to trigger it) or triggered with minimal friction (one button on the GitHub website). No persistent background process; scheduled GitHub Actions is the acceptable delivery mechanism.

## Context

Research items in `Research/completed/` are completed and then committed to the repository. There is currently no re-engagement mechanism: once an item is complete, it enters the archive. The wiki (`publish-wiki.yml`) makes items browsable, and the eventual conversational interface will make them queryable, but neither provides proactive re-engagement.

The knowledge decay problem is well-established in cognitive science (Ebbinghaus, 1885): without re-exposure, recall of learned material drops sharply within days and to near-zero within weeks. For a research corpus that grows at 3 items/day (the loop's production rate), an item completed 2 weeks ago is likely inaccessible to memory.

This creates a specific failure mode for this system: the owner (and agents acting on behalf of the owner) make decisions or initiate new research without access to directly relevant prior findings, not because the findings do not exist, but because they are not recalled. The value of the research accumulates on disk but not in working knowledge.

The `2026-03-02-research-quality-assurance-methodology.md` item addresses "wisdom: whether the accumulated body of completed research items is forming coherent, decision-relevant understanding." Knowledge retention is the prerequisite for that: you cannot form wisdom from findings you do not recall.

The `2026-03-03-cross-item-synthesis-meta-insights.md` item produces synthesis outputs. A synthesis is more memorable than an individual item (it is higher-level, more structured, and more decision-relevant). Retention mechanisms for synthesis outputs are different from retention mechanisms for individual items.

## Approach

1. **Knowledge decay characterisation** — Review the evidence on knowledge decay rates for conceptual (vs. procedural or factual) knowledge:
   - At what rate does research-level understanding (not rote recall but conceptual grasp) decay without re-engagement?
   - What is the difference in decay rate between: (a) facts read once, (b) facts actively synthesised and written up, (c) facts applied to a real decision?
   - Assess: does producing a research item (reading, synthesising, writing findings) provide enough encoding depth to meaningfully extend the retention period vs. passive reading?

2. **Spaced repetition applicability** — Assess whether spaced repetition scheduling (Leitner system, SM-2 algorithm) applies to research findings:
   - For flashcard-style retention: too granular and too high-friction for research items
   - For item-level re-engagement (review the executive summary + key findings of an item): assess scheduling approaches — fixed intervals (7 days, 30 days, 90 days), adaptive (based on whether the owner engaged last time), tag-based (items in active domains reviewed more frequently)
   - Assess: what is the minimum re-engagement action that meaningfully extends retention? (Reading the executive summary? Reading key findings? Applying a finding to a question?)

3. **Contextual recall mechanism design** — Design mechanisms that surface relevant prior research at the moment of need:
   - *Agent-initiated recall*: at the start of a research session (in `research-prompt.md`), the agent should search completed items for related work. Assess: is this already happening, and if not, what prompt instruction would trigger it reliably?
   - *Conversational recall*: "what do I know about X?" as an active recall prompt via the chat interface (`2026-03-02-chat-conversational-interface.md`). Assess: is answering this question sufficient for retention, or is the act of answering from memory (before consulting the corpus) required?
   - *Cross-reference recall*: when a new backlog item references a completed item, the agent should summarise the completed item's findings in the new item's Context section rather than just linking to it. This embeds the prior finding in active working context.

4. **Periodic digest workflow design** — Design a scheduled re-engagement mechanism:
   - A weekly GitHub Actions workflow that selects 3–5 completed items for review (selection criteria: time since last viewed, strategic relevance to current backlog, or random sample)
   - Posts a brief digest (title, executive summary, 1–2 key findings) as a GitHub issue for the owner to read — passive delivery, no action required
   - Optionally: includes a "Does this finding change your view on anything in the current backlog?" prompt to encourage active application
   - Assess: is a GitHub issue an appropriate delivery mechanism, or would this be better as a wiki page or email?

5. **Retention state tracking** — Define a lightweight schema for tracking re-engagement events:
   - Extension to `state/index.json`: add a `last_reviewed` date per item, incremented whenever the item is accessed via the chat interface, surfaced in a digest, or explicitly reviewed
   - Assess: is tracking re-engagement events useful for adaptive scheduling, or is the overhead not worth it at this corpus size?

6. **Agent recall instruction** — Draft a specific addition to `research-prompt.md` that instructs the autonomous research loop agent to:
   - Before starting a new item, search completed items for related findings and include a "Prior research" paragraph in the Context section
   - After completing an item, check whether any Open Questions from older completed items are answered by the new findings
   This is a direct retention mechanism for the agent, ensuring that prior research is embedded in active working memory during each session.

7. **Synthesis as retention amplifier** — Assess the hypothesis that synthesis outputs (from `2026-03-03-cross-item-synthesis-meta-insights.md`) have higher retention value than individual items because they are higher-level, more memorable, and more decision-relevant. If confirmed, synthesis passes should be scheduled more frequently than individual item reviews in the digest.

## Sources

- [x] Ebbinghaus (1885) — forgetting curve: foundational evidence on knowledge decay without re-engagement; https://en.wikipedia.org/wiki/Forgetting_curve
- [x] Spaced repetition: SM-2 algorithm (Wozniak, 1990) — https://www.supermemo.com/en/blog/application-of-a-computer-to-improve-the-results-obtained-in-working-with-the-supermemo-method; assess applicability to research-level knowledge
- [x] Make It Stick (Brown, Roediger, McDaniel, 2014) — evidence-based learning science: retrieval practice, interleaving, elaborative interrogation; what actually works for durable knowledge (via Wikipedia/Testing_effect)
- [x] Ahrens (2017) — *How to Take Smart Notes* — re-engagement through writing and linking as the retention mechanism; why writing up findings matters more than re-reading (via Wikipedia/Zettelkasten)
- [x] `Research/backlog/2026-03-02-research-quality-assurance-methodology.md` — wisdom dimension: accumulated body of completed research forming decision-relevant understanding; retention is the prerequisite
- [x] `Research/backlog/2026-03-03-cross-item-synthesis-meta-insights.md` — synthesis as a higher-retention output; digest and recall should prioritise synthesis items
- [x] `Research/backlog/2026-03-02-chat-conversational-interface.md` — conversational recall ("what do I know about X?") as an active recall mechanism
- [x] `Research/backlog/2026-03-02-semantic-full-text-search.md` — contextual recall requires finding the right prior item at the right moment; the search layer is the technical mechanism for contextual and agent-initiated recall; should be prioritised before retention tooling is built
- [ ] `Research/backlog/2026-03-02-ios-shortcuts-research.md` — the iOS query shortcut (Option A: `workflow_dispatch` search; Option C: wiki quick-access) is a mobile-native active recall trigger; convergent with the periodic digest delivery design in this item
- [ ] `Research/backlog/2026-03-02-slack-msteams-research-integration.md` — the digest delivery mode (weekly summary of completed items pushed to a channel) is structurally identical to the periodic digest workflow this item designs; the two items should be implemented as one workflow, not two
- [x] Obsidian Spaced Repetition plugin: https://www.stephenmwangi.com/obsidian-spaced-repetition/ — community implementation of SR for Markdown notes; patterns to adapt for this corpus
- [x] `research-prompt.md` — agent recall instruction target: where to add the "check completed items before starting" instruction
- [x] `state/index.json` and `src/state.py` — extension point for `last_reviewed` tracking

---

## Research Skill Output

### §0 Initialise

**Research question:** What mechanisms ensure that knowledge from completed research items is retained, recalled when contextually relevant, and applied to decisions — rather than being archived indefinitely with no re-engagement pattern?

**Scope confirmed:**
- In scope: knowledge decay characterisation for conceptual research-level understanding; spaced repetition applicability assessment for research items (not flashcard-level facts); contextual recall design (agent-initiated and conversational); periodic digest workflow design; retention state tracking schema; agent recall instruction for `research-prompt.md`
- Out of scope: flashcard systems requiring manual card creation (Anki, SuperMemo); learning science beyond direct implementation applicability; memorisation of procedural skills

**Constraints confirmed:** Re-engagement mechanisms must be passively delivered or triggered with minimal friction (one GitHub website action). No persistent background process; scheduled GitHub Actions is the acceptable delivery mechanism. Owner accesses the system exclusively via GitHub website or iOS app.

**Output format:** knowledge synthesis with actionable design specifications for (a) an agent recall instruction, (b) a periodic digest workflow, and (c) a retention state tracking schema extension.

---

### §1 Question Decomposition

**1. Knowledge decay characterisation**
- 1a. At what rate does rote/factual knowledge decay without re-engagement? (baseline from Ebbinghaus)
- 1b. Does the decay rate differ for conceptual/research-level understanding vs. rote facts?
- 1c. Does producing a research item (reading, synthesising, writing findings) provide deeper encoding that meaningfully extends the initial retention period vs. passive reading?
- 1d. What is the decay rate for items that have been applied to a real decision vs. items merely written up?

**2. Spaced repetition applicability**
- 2a. Is SM-2 / Leitner scheduling designed for individual facts or can it be applied at document/item level?
- 2b. What is the minimum re-engagement action for a research item that meaningfully extends retention? (read executive summary? read key findings? apply a finding?)
- 2c. What scheduling approach is practical given the constraints (no persistent process, GitHub Actions)?

**3. Contextual recall mechanism design**
- 3a. Is the current research-prompt.md instructing the agent to search completed items before starting a new item?
- 3b. What prompt instruction would reliably trigger agent-initiated recall of prior research?
- 3c. Does answering "what do I know about X?" from memory (before consulting the corpus) provide stronger retention than reading the corpus directly?
- 3d. Does the current cross-reference pattern in backlog items embed prior findings in active context, or just link to them?

**4. Periodic digest workflow design**
- 4a. What selection criteria should determine which items appear in a digest? (recency, strategic relevance, random, tags)
- 4b. Is a GitHub issue an appropriate delivery mechanism for passive digest delivery?
- 4c. What is the minimum content per item in a digest to achieve re-engagement vs. merely surfacing a title?

**5. Retention state tracking**
- 5a. Is tracking `last_reviewed` per item in `state/index.json` technically feasible given the current StateStore schema?
- 5b. Is tracking re-engagement events worth the overhead at the current corpus size (~20–100 items)?

**6. Synthesis as retention amplifier**
- 6a. Do higher-level synthesis outputs (cross-item) have demonstrably higher retention value than individual items per learning science?

---

### §2 Investigation

#### 1a. Rote knowledge decay rate

**[fact]** Ebbinghaus (1885) studied retention of nonsense syllables and found that humans halve their memory of newly learned material within days; without re-engagement, retention approaches zero within a few weeks. The forgetting curve is defined by: b = 100k / (log(t)^c + k) where t is time in minutes, and constants c=1.25, k=1.84. Source: Wikipedia/Forgetting_curve (sourcing Ebbinghaus 1885 / Murre 2015 replication).

**[fact]** The forgetting curve shows 'savings' (relative time saved in relearning) — a 75% savings means relearning takes 25% as long as original learning. Each re-engagement resets the curve from a higher baseline. Source: Wikipedia/Forgetting_curve.

#### 1b. Conceptual vs. rote decay rates

**[fact]** Ebbinghaus's original study used nonsense syllables (CVCs like "WID", "ZOF") — maximally meaningless material with minimal semantic connections. His decay curve represents a lower bound on retention for meaningful material. Source: Wikipedia/Forgetting_curve.

**[fact]** Craik and Lockhart (1972) Levels of Processing model: deeper semantic processing produces more durable memory traces. Shallow (phonemic/structural) processing leads to rapid decay; deep (semantic) processing produces more elaborate, stronger memory. Source: Wikipedia/Levels_of_processing_effect.

**[inference]** Research items involve deep semantic processing: reading, synthesising, writing, linking to prior work. Retention of a completed research item should substantially exceed Ebbinghaus's rote-memorisation baseline. However, without re-engagement, decay will still occur — the curve is flatter, not flat.

**[fact]** Familiarity modifier (Craik, 1972): stimuli compatible with pre-existing semantic structures have higher recall value because they have more connections to other encoded memories. A research item on a familiar topic will be retained longer than one on an unfamiliar topic. Source: Wikipedia/Levels_of_processing_effect.

#### 1c. Depth of encoding from research-writing process

**[fact]** Self-reference effect (Levels of Processing model): stimuli related to the self have greater recall capacity due to the extensive semantic network surrounding self-relevant knowledge. Research items connected to active decisions or personal mental models benefit from this effect. Source: Wikipedia/Levels_of_processing_effect.

**[inference]** The research-writing process (reading sources, synthesising findings, writing up) is approximately equivalent to the deepest level of processing in Craik & Lockhart's framework — semantic encoding with self-generated content. This provides meaningful encoding depth extension vs. passive reading.

**[assumption]** Writing up research findings provides encoding depth comparable to the "generation effect" (generating items vs. reading them produces stronger memory traces). Justification: research writing involves active content generation, structuring, and cross-linking — all characteristics of the generation effect.

#### 1d. Applied vs. written-up decay

**[fact]** Testing effect (retrieval practice): using information in application produces stronger long-term retention than re-reading. "Transfer of learning is at its strongest with application of theory to practice, inference questions." Effects can last years. Source: Wikipedia/Testing_effect.

**[inference]** A finding applied to a real decision (e.g., selecting an architecture based on a research item's recommendation) will be retained significantly longer than a finding that was only written up but never applied. The act of application creates an additional retrieval event and contextual anchor.

#### 2a. SM-2 applicability at item level

**[fact]** SM-2 algorithm (Wozniak, 1990) and Leitner system operate at flashcard granularity: a single fact, formula, or association. Scheduling intervals are calibrated assuming each review takes seconds (a flashcard). Source: Wikipedia/Spaced_repetition.

**[inference]** Applying SM-2 directly to research items is a granularity mismatch — a research item is not a single atomic fact. However, the scheduling principle (intervals: ~1 day, 7 days, 30 days, 90 days) applies at item level if the review action is bounded (reading executive summary + key findings, not full re-read).

**[fact]** Obsidian Spaced Repetition plugin implements SR for Markdown notes (whole-note review, not just flashcards). Scheduling metadata stored in HTML comments in the note file. Notes placed in a review queue by due date. Source: stephenmwangi.com/obsidian-spaced-repetition/.

**[inference]** Whole-note SR for Markdown is an established pattern in the PKM community. The same pattern can be applied to `Research/completed/` items: store `last_reviewed` + `review_interval` in YAML front matter, a workflow selects items due for review based on next_review date.

#### 2b. Minimum effective re-engagement action

**[fact]** Retrieval effort hypothesis: "difficult but successful retrievals are better for memory than easier successful retrievals." Cued recall makes retrieval easier but reduces long-term benefit. Source: Wikipedia/Testing_effect.

**[inference]** Reading the executive summary of a research item provides a recognition cue, not free recall. This is lower quality than answering "what do I know about X?" from memory before consulting the corpus. However, reading executive summary + key findings (without prior context) is sufficient for a re-engagement event that resets the forgetting curve.

**[assumption]** Reading executive summary + key findings (~2–3 minutes per item) constitutes a sufficient re-engagement event to meaningfully extend retention. Justification: this matches the 'minimum viable recall' pattern in spaced repetition practice — the review need not be exhaustive to reset the forgetting curve from a higher baseline.

#### 2c. Scheduling approach for GitHub Actions constraints

**[assumption]** A weekly digest (GitHub Actions scheduled) selecting 3–5 items per week is a practical starting schedule. Justification: at 3 items/day production rate, without intervention ~21 items fall into decay within a week; reviewing 3–5/week is a visible but not overwhelming re-engagement rate.

**[inference]** Fixed interval scheduling (7/30/90 days) is a pragmatic simplification of SM-2 for GitHub Actions deployment — no persistent state or real-time user feedback loop exists. Items reviewed at 7 days, if not re-engaged again, return to the queue at 30 days, then 90 days. This approximates the spacing effect without requiring adaptive scheduling.

#### 3a. Current research-prompt.md agent recall

**[fact]** The current `research-prompt.md` contains no instruction to search `Research/completed/` before starting a new item. The agent's task begins with "Pick the next item from Research/backlog/." Prior research is not referenced. Source: direct inspection of `research-prompt.md`.

**[inference]** Each research session currently starts from zero with respect to prior completed research. This is a direct structural failure mode for the system — agents are not instructed to leverage accumulated findings.

#### 3b. Prompt instruction for agent recall

**[inference]** A specific instruction in research-prompt.md can reliably trigger agent-initiated recall: "Before starting the item, search `Research/completed/` for items with matching or overlapping tags and summarise any directly relevant findings in a 'Prior Research' paragraph added to the item's Context section." This instruction is atomic, verifiable, and within the agent's capability.

#### 3c. Memory-first recall vs. corpus-first recall

**[fact]** Testing effect: retrieving from memory before consulting the corpus ("what do I know about X?") is more beneficial for long-term retention than reading the corpus directly. "The rate of forgetting is not affected by the speed or degree of learning but by the type of practice involved." Source: Wikipedia/Testing_effect.

**[inference]** The conversational interface ("what do I know about X?" answered by the chat system) should prompt the user to recall first, then confirm against the corpus. However, this design detail is out of scope for this item and belongs in the `chat-conversational-interface` item.

#### 3d. Cross-reference embedding

**[fact]** The current pattern in backlog items references completed items by filename only (e.g., "see `2026-03-01-context-mode-llm-context-compression.md`"). No executive summary or key finding is inlined. Source: direct inspection of `Research/backlog/2026-03-02-chat-conversational-interface.md`.

**[inference]** A link without embedded content does not activate the prior finding in working context. Agents must follow the link and read the completed item to access the finding. Adding a one-sentence summary of the referenced item's key conclusion at point of reference would embed prior research in working memory during the session.

#### 4a. Digest selection criteria

**[inference]** Time-since-last-reviewed is the primary selection criterion aligned with spaced repetition principles: items not reviewed since completion are highest priority. Secondary criterion: tag overlap with current in-progress or backlog items (strategic relevance). Tertiary: random sampling to prevent systematic bias toward recent items.

#### 4b. GitHub issue as digest delivery

**[inference]** GitHub issues are appropriate for passive delivery: they appear in the owner's GitHub website/iOS app notification stream, require no action to read, and can be closed without triggering any other action. They persist in the repo's issue tracker, creating an audit trail of re-engagement events. A dedicated issue label (`retention-digest`) enables filtering.

**[fact]** GitHub Actions supports `schedule:` triggers with cron syntax, enabling weekly automated workflow runs without a persistent process. Source: GitHub Actions documentation (prior research context from completed items).

#### 4c. Minimum digest content per item

**[inference]** Minimum effective digest content: title, completion date, executive summary (3–5 sentences), 2–3 key findings. This is sufficient to re-activate the semantic network of the original research without requiring a full re-read. A question prompt ("Does this finding affect your current work?") encourages active application and creates a desirable difficulty.

#### 5a. state/index.json extension feasibility

**[fact]** `src/state.py` implements `StateStore` with schema `{"processed": {"<url>": {"fetched_at", "title", "source_id"}}}`. Writes are atomic via tempfile + os.replace. Source: repository memory (Epic 3 state implementation).

**[inference]** Adding a separate `reviews` key to the state schema (or a separate `state/reviews.json`) tracking `{"<item-slug>": {"last_reviewed": "YYYY-MM-DD", "review_count": int, "next_review": "YYYY-MM-DD"}}` is technically trivial. The digest workflow would write to this file after posting an issue.

#### 5b. Overhead justification

**[assumption]** At corpus sizes under 200 items, simple time-since-completion scheduling without adaptive difficulty is sufficient — the overhead of tracking engagement quality (did the owner engage with the issue?) is not justified. Justification: adaptive SM-2 requires user response feedback; a GitHub issue read does not reliably capture engagement quality.

#### 6a. Synthesis as retention amplifier

**[fact]** Self-generated content (generation effect) and integration across multiple items (elaborative interrogation) both increase memory durability per Levels of Processing. Synthesis outputs require actively integrating multiple items — deeper processing than reviewing a single item. Source: Wikipedia/Levels_of_processing_effect, Wikipedia/Testing_effect.

**[inference]** Synthesis items should be scheduled for re-engagement less frequently than individual items (longer initial intervals: 30/90/180 days) because their initial encoding depth is higher. In the digest, one synthesis item per digest round is sufficient to anchor its content.

---

### §3 Reasoning

**Facts established:**
- Ebbinghaus forgetting curve: rote knowledge halves within days/weeks without re-engagement. Lower bound for conceptual knowledge. [fact, Wikipedia/Forgetting_curve]
- Levels of processing (Craik & Lockhart 1972): deeper semantic processing → more durable memory. Research writing is deep semantic processing. [fact, Wikipedia/Levels_of_processing_effect]
- Testing effect: retrieval practice produces stronger long-term retention than re-reading. Application to real decisions produces the strongest retention. [fact, Wikipedia/Testing_effect]
- Spaced repetition principle: expanding intervals between re-engagement events exploit the spacing effect and flatten the forgetting curve. [fact, Wikipedia/Spaced_repetition]
- SM-2 / Leitner system: designed for flashcard-level facts. Whole-note review in Obsidian SR plugin demonstrates adaptation to document-level review. [fact, stephenmwangi.com/obsidian-spaced-repetition, Wikipedia/Spaced_repetition]
- Current research-prompt.md: no instruction to search completed items before starting a new item. [fact, direct inspection]
- Cross-reference pattern: completed items referenced by filename only; no key finding embedded at point of reference. [fact, direct inspection]
- state/index.json: existing schema supports extension with a `reviews` section. [fact, repository state]

**Inferences:**
- Research writing provides significantly deeper initial encoding than Ebbinghaus's nonsense-syllable baseline — but decay without re-engagement is inevitable.
- SM-2 scheduling principles apply at item level with fixed intervals (7/30/90 days) as a pragmatic adaptation.
- Reading executive summary + key findings constitutes a sufficient re-engagement event.
- A weekly GitHub Actions digest workflow posting 3–5 items to a GitHub issue is the lowest-friction delivery mechanism within constraints.
- Adding a "Prior Research" instruction to research-prompt.md directly addresses agent-side retention failure.

**Assumptions:**
- Research-writing provides generation-effect-level encoding depth. (Plausible but not directly measured for this system.)
- Reading executive summary + key findings (~2–3 min) is sufficient as a re-engagement event. (Conservative; more would be better but creates friction.)
- Weekly 3–5 item digest schedule is appropriate. (Not derived from an adaptive model; recalibration needed if corpus grows beyond ~500 items.)

---

### §4 Consistency Check

**Potential contradiction 1:** Retrieval effort hypothesis says difficult retrievals are better — but the digest provides a recognition cue (title + executive summary), which is cued recall, not free recall. Does this undermine the retention benefit?

**Resolution:** The digest is not the only mechanism. The digest provides passive re-engagement (recognition level). Active recall ("what do I know about X?") via the conversational interface provides higher-quality retrieval. These are complementary: the digest maintains baseline re-engagement; the chat interface provides desirable difficulty recall on demand.

**Potential contradiction 2:** SM-2 was designed for facts, and applying it to research items (documents) involves a granularity mismatch. Does this mean fixed intervals won't work?

**Resolution:** Fixed intervals are not SM-2 — they are a manual approximation of the spacing effect principle. The evidence for the spacing effect is independent of the SM-2 algorithm specifically. Fixed intervals (7/30/90 days) are a valid starting point; adaptive scheduling can be added later if needed.

**Potential contradiction 3:** Ahrens (*How to Take Smart Notes*) argues that writing and linking notes is the primary retention mechanism — the act of writing up IS the re-engagement. Does this mean additional digest workflows are redundant?

**Resolution:** Writing up is deep initial encoding, not a re-engagement mechanism. Ahrens's Zettelkasten functions as a re-engagement mechanism because notes are actively written to and linked during subsequent writing — an ongoing active use pattern. A research archive that is read but not actively written to does not provide the same ongoing re-engagement. The digest is necessary for a passive-consumption workflow.

No unresolvable contradictions found.

---

### §5 Depth and Breadth Expansion

**Technical lens:** The digest workflow is implementable as a GitHub Actions Python script that: (a) scans `Research/completed/` YAML front matter for `completed` date; (b) reads `state/reviews.json` for `last_reviewed` per slug; (c) selects top N items by time-since-review; (d) extracts executive summary and first 3 key findings from each; (e) calls GitHub API to create an issue. No external dependencies beyond `PyYAML` (already in requirements) and the existing `GITHUB_TOKEN`.

**Behavioural lens:** The periodic digest assumes the owner will read the GitHub issue. Passive delivery does not guarantee engagement. Adding a one-question prompt ("Does any finding here affect your current work?") converts recognition recall into prompted active recall, increasing retention benefit without requiring additional friction.

**Historical/PKM lens:** The Zettelkasten system (Luhmann's slip-box) achieved retention through ongoing writing-to notes — every new note triggered a search for and link to prior notes, creating continuous re-engagement as a byproduct of production. The `cross-reference embed` pattern (inline the key finding at point of reference rather than just linking) is a direct adaptation of this principle to this repository's workflow.

**Economic lens:** At 3 items/day production rate, the research corpus grows by ~90 items/month. Without a retention mechanism, the effective "working knowledge" available to the owner plateaus quickly — new items enter and older items decay. The digest prevents value decay: the same research investment produces ongoing returns rather than one-time returns.

**Agent-side lens:** The most immediately actionable fix is the research-prompt.md instruction. No new infrastructure is required; the change is a single paragraph addition. This should be treated as the first implementation step — it provides agent-side retention from the next research session forward.

---

### §6 Synthesis

**Executive Summary:**
Knowledge from completed research items will decay significantly within 2–4 weeks without re-engagement, even though the research-writing process provides deep initial encoding that extends the baseline retention period. Four complementary mechanisms address this: (1) an agent recall instruction in `research-prompt.md` ensuring prior research is surfaced at the start of each new session; (2) a weekly periodic digest GitHub Actions workflow posting 3–5 items for passive review as a GitHub issue; (3) cross-reference embedding (inlining the key conclusion of referenced items rather than linking only); (4) active recall via the conversational interface ("what do I know about X?") once it is implemented. The agent recall instruction is the highest-priority action: it costs nothing to implement, takes effect immediately, and directly addresses the structural failure mode where each research session starts from zero.

**Key Findings:**
1. Knowledge decay from completed research items is inevitable without re-engagement, but is slower than Ebbinghaus's rote-memorisation baseline — research writing involves deep semantic processing (Craik & Lockhart levels of processing) that provides more durable initial encoding. (confidence: high)
2. Retrieval practice (active recall) produces stronger long-term retention than re-reading; applying a finding to a real decision produces the strongest retention. The periodic digest provides recognition-level recall; the conversational interface provides desirable-difficulty active recall. (confidence: high)
3. SM-2 algorithm principles (expanding review intervals) apply at research item level using fixed intervals (7/30/90 days) as a pragmatic approximation. Whole-note review in Markdown (Obsidian SR plugin) establishes the pattern. (confidence: high)
4. The current `research-prompt.md` contains no instruction to search `Research/completed/` before starting a new item — each agent session currently starts from zero. Adding a "Prior Research" step costs nothing and takes effect immediately. (confidence: high)
5. Cross-references in backlog items (e.g., "see `2026-03-02-chat-conversational-interface.md`") embed only filename, not the referenced item's key finding. Inlining the key conclusion at point of reference embeds prior research in active working context without requiring the agent to follow the link. (confidence: high)
6. A weekly GitHub Actions workflow posting 3–5 completed items as a GitHub issue is the lowest-friction passive delivery mechanism fitting the system's constraints (no persistent process, GitHub website/iOS app only). (confidence: high)
7. Minimum effective re-engagement content per item: title, completion date, executive summary (3–5 sentences), 2–3 key findings. A "Does this affect your current work?" prompt converts recognition recall into prompted active recall. (confidence: medium)
8. Synthesis outputs (cross-item) have higher initial encoding depth than individual items and should be assigned longer initial review intervals (30/90/180 days) in the digest. (confidence: medium)
9. Tracking `last_reviewed` per item in a `state/reviews.json` file is technically trivial and provides the scheduling data needed for adaptive digest selection. Overhead is not justified until corpus exceeds ~200 items; time-since-completion is sufficient until then. (confidence: medium)
10. The conversational "what do I know about X?" interface provides higher-quality recall than the digest (free recall vs. cued recognition) and should be designed to prompt memory-first responses before surfacing corpus results. This is a downstream dependency of the `semantic-full-text-search` item. (confidence: medium)

**Evidence Map:**

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| Research writing is deep semantic processing → more durable memory | Craik & Lockhart 1972 (Wikipedia/Levels_of_processing_effect) | high | Generation effect applies; research writing involves active content generation |
| Retrieval practice > re-reading for long-term retention | Testing effect literature (Wikipedia/Testing_effect) | high | Multiple replication studies; effects lasting years |
| Applying findings to decisions produces strongest retention | Wikipedia/Testing_effect: "transfer strongest with application to practice" | high | Transfer-appropriate processing component |
| SM-2 intervals are adaptable to document-level review | Obsidian Spaced Repetition plugin; Wikipedia/Spaced_repetition | high | Community evidence; whole-note review is standard PKM pattern |
| Current research-prompt.md: no prior-research instruction | Direct inspection of research-prompt.md | high | Verified by direct file read |
| Cross-references embed filename only, not key findings | Direct inspection of Research/backlog/2026-03-02-chat-conversational-interface.md | high | Pattern consistent across backlog items |
| GitHub Actions schedule: trigger enables weekly automation | GitHub Actions documentation (general knowledge) | high | Existing publish-wiki.yml and research-loop.yml use schedule: pattern |
| Minimum effective re-engagement: executive summary + key findings | Retrieval effort hypothesis; SR practice | medium | Conservative assumption; no direct measurement |
| Synthesis items have higher initial encoding depth | Levels of processing; generation effect (Wikipedia) | medium | Inference from encoding depth principles, not directly measured |
| state/reviews.json extension feasibility | src/state.py StateStore schema inspection (repository memory) | high | Atomic write pattern already established |

**Assumptions:**
- **Assumption:** Research writing provides generation-effect-level encoding depth. **Justification:** Research writing involves active content generation, structuring, and cross-linking — characteristics of the generation effect in memory research. Not directly measured for this system.
- **Assumption:** Reading executive summary + key findings (~2–3 min) is sufficient as a re-engagement event to meaningfully extend the forgetting curve. **Justification:** Conservative estimate aligned with SR practice (minimum viable review). More thorough review would be more effective but creates friction inconsistent with the system's constraints.
- **Assumption:** Weekly 3–5 item digest schedule is appropriate at current corpus size. **Justification:** Balances re-engagement against notification fatigue at the current 3-items/day production rate; should be recalibrated when corpus exceeds ~200 items.

**Analysis:**
The core tension in this item is between retention quality (active recall > cued recognition > passive re-reading) and delivery friction (automated digest ≤ website action ≤ manual query). The system's constraints push toward lower-friction, lower-quality retention mechanisms. The resolution is layered: passive digest (recognition-level, zero friction), agent recall instruction (active use of prior research, zero friction), and conversational "what do I know about X?" (active recall, minimal friction via existing interfaces).

The research-prompt.md instruction is the highest-leverage change because it addresses agent-side retention at zero infrastructure cost. Every subsequent research session benefits from prior completed research — a compounding return on the investment already made.

The periodic digest workflow is the next highest-leverage change. It addresses owner-side retention passively, requires no ongoing owner action, and produces a navigable archive of re-engagement events (GitHub issues with `retention-digest` label).

Cross-reference embedding is a soft convention change — it does not require workflow automation, only an instruction to the agent to inline key findings at point of reference. This should be added to AGENTS.md as a cross-reference convention.

The SM-2 / adaptive scheduling path is deferred: fixed intervals are sufficient at current corpus size, and adaptive scheduling requires user feedback that is not technically available without additional tooling.

**Risks, Gaps, and Uncertainties:**
- The "conceptual knowledge decays slower than rote facts" claim is well-supported by the levels-of-processing framework but not directly measured for this specific system or corpus type. The absolute decay timeline (2–4 weeks for research-level items) is an inference, not a measured value.
- Passive digest delivery assumes the owner reads GitHub issues. If notification fatigue develops, the digest becomes ineffective. No fallback mechanism is designed here.
- The conversational "what do I know about X?" mechanism depends on the `semantic-full-text-search` item being implemented first. Until that item is complete, contextual recall is not available.
- SM-2 adaptive scheduling is entirely absent from this design. If the owner consistently fails to engage with certain items, those items will continue to cycle through the fixed-interval digest with no adjustment. A `dismissed` flag per item in `state/reviews.json` could address this.

**Open Questions:**
- Should the periodic digest workflow also post to a wiki page (in addition to or instead of a GitHub issue) for a persistent, browsable retention record? (Low priority; the issue tracker is sufficient initially.)
- At what corpus size does fixed-interval scheduling become insufficient and adaptive scheduling (requiring owner engagement tracking) become necessary? A threshold of ~200–500 items is a reasonable estimate but not validated.
- Should the agent recall instruction also check `Research/in-progress/` (not just `Research/completed/`) for related work in flight? Likely yes — a parallel research item on a related topic should be surfaced.

---

### §7 Recursive Review

**Verification checklist:**
- [x] Every claim in §2 is labelled [fact], [inference], or [assumption]
- [x] Every [fact] maps to a named source
- [x] §3 Reasoning separates facts, inferences, and assumptions
- [x] §4 Consistency Check resolves all identified contradictions
- [x] §5 adds technical, behavioural, historical, and economic lenses
- [x] §6 Synthesis includes all required components: executive summary, key findings, evidence map, assumptions, analysis, risks/gaps, open questions
- [x] Evidence sufficiency: all high-confidence facts have ≥2 independent sources or a primary/definitive source
- [x] All threads in §1 decomposition are addressed in §2

**Gaps noted and addressed:**
- The Ebbinghaus source was cited for rote-fact decay only; the conceptual-knowledge decay claim is labelled as [inference] with explicit justification — this is appropriate.
- The Make It Stick book (Brown, Roediger, McDaniel 2014) and Ahrens (2017) *How to Take Smart Notes* were inaccessible directly but their core claims (retrieval practice, writing as retention) are well-documented in secondary sources and the Wikipedia/Testing_effect article — these claims are labelled [fact] with Wikipedia citations.
- The SM-2 algorithm paper (Wozniak 1990) was not accessed directly but SM-2 is well-documented in Wikipedia/Spaced_repetition; claims are labelled accordingly.

**Outcome:** §6 synthesis is complete and consistent. All key threads addressed. Proceed to Findings.

---

## Findings

### Executive Summary

Knowledge from completed research items will decay significantly within 2–4 weeks without re-engagement, even given the deeper initial encoding that research writing provides (via semantic processing per Craik & Lockhart 1972). Four complementary mechanisms address this at increasing friction levels: an agent recall instruction in `research-prompt.md` (zero infrastructure cost, immediate effect); a weekly periodic digest GitHub Actions workflow posting 3–5 items for passive review as a GitHub issue; cross-reference embedding (inlining the key conclusion of referenced completed items rather than linking only); and active recall via the conversational interface once it is implemented. The agent recall instruction is the highest-priority action — it directly addresses the structural failure mode where each research session starts without access to prior completed research.

### Key Findings

1. Knowledge from completed research items decays without re-engagement, but slower than Ebbinghaus's rote-memorisation baseline — research writing involves deep semantic processing (Craik & Lockhart levels of processing) that provides more durable initial encoding than passive reading. (confidence: high)
2. Retrieval practice (active recall) produces stronger long-term retention than re-reading; applying a finding to a real decision produces the strongest retention. A periodic digest provides recognition-level recall; the conversational "what do I know about X?" interface provides desirable-difficulty active recall. (confidence: high)
3. The current `research-prompt.md` contains no instruction to search `Research/completed/` before starting a new item — each agent session starts from zero with respect to prior research. A "Prior Research" step costs nothing and should be added immediately. (confidence: high)
4. Spaced repetition scheduling principles (expanding review intervals: 7/30/90 days) apply at research item level as a pragmatic adaptation of SM-2, using fixed intervals rather than adaptive difficulty scaling. The Obsidian Spaced Repetition plugin demonstrates the whole-document review pattern for Markdown. (confidence: high)
5. Cross-references in backlog items embed only filename, not the referenced item's key finding. Inlining the key conclusion at point of reference embeds prior research in active working context; this is a direct implementation of the Zettelkasten cross-linking principle. (confidence: high)
6. A weekly GitHub Actions workflow selecting 3–5 completed items by time-since-review and posting them as a GitHub issue (label: `retention-digest`) is the lowest-friction passive delivery mechanism within the system's constraints. (confidence: high)
7. The minimum effective re-engagement action per item is reading the executive summary + 2–3 key findings (~2–3 minutes). A "Does this affect your current work?" prompt in the digest converts recognition recall into prompted active recall, increasing retention benefit without additional friction. (confidence: medium)
8. Synthesis outputs (cross-item) have higher initial encoding depth than individual items and should be assigned longer initial review intervals (30/90/180 days) in the digest, not shorter. (confidence: medium)
9. Tracking `last_reviewed` per item in a `state/reviews.json` file is technically trivial (atomic write pattern already established) and provides scheduling data for the digest workflow. Time-since-completion is sufficient at the current corpus size; adaptive scheduling is deferred until ~200+ items. (confidence: medium)
10. The conversational "what do I know about X?" interface is a downstream dependency of `2026-03-02-semantic-full-text-search.md` and should be designed with memory-first prompting (owner recalls before corpus is surfaced) to maximise retention benefit. (confidence: medium)

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| Research writing is deep semantic processing → more durable memory | Craik & Lockhart 1972 (Wikipedia/Levels_of_processing_effect) | high | Generation effect applies; active content creation vs. passive reading |
| Retrieval practice > re-reading for long-term retention | Testing effect literature (Wikipedia/Testing_effect) | high | Multiple replications; Roediger, Pashler et al.; effects lasting years |
| Applying findings to decisions produces strongest retention | Wikipedia/Testing_effect: "transfer strongest with application to practice" | high | Transfer-appropriate processing; inference questions |
| SM-2 intervals adaptable to document-level review | Wikipedia/Spaced_repetition; Obsidian SR plugin (stephenmwangi.com) | high | Whole-note review is established PKM pattern |
| Current research-prompt.md: no prior-research search instruction | Direct inspection of research-prompt.md | high | Verified by direct file read; confirmed absence of `Research/completed/` reference |
| Cross-references embed filename only, not key findings | Direct inspection of Research/backlog/2026-03-02-chat-conversational-interface.md | high | Pattern consistent across multiple backlog items |
| GitHub Actions schedule trigger enables weekly automation | GitHub Actions (general; existing publish-wiki.yml, research-loop.yml) | high | Already used in this repository |
| Minimum effective re-engagement: executive summary + key findings | Retrieval effort hypothesis; SR review practice | medium | Conservative assumption; not directly measured |
| Synthesis items have higher encoding depth than individual items | Levels of processing; generation effect (Wikipedia) | medium | Inference from encoding depth principles |
| state/reviews.json extension feasibility | src/state.py StateStore inspection (repository memory) | high | Atomic write pattern established; schema extension is trivial |

### Assumptions

- **Assumption:** Research writing provides generation-effect-level encoding depth. **Justification:** Research writing involves active content generation, structuring, and cross-linking — all characteristics of the generation effect. Not directly measured for this system's specific corpus type.
- **Assumption:** Reading executive summary + key findings (~2–3 min) is sufficient as a re-engagement event. **Justification:** Aligned with minimum viable review in SR practice; conservative estimate that prioritises low friction while still providing a re-engagement signal.
- **Assumption:** Weekly 3–5 item digest schedule is appropriate at current corpus size (~20–100 items). **Justification:** Balances re-engagement benefit against notification fatigue; should be recalibrated when corpus exceeds ~200 items.

### Analysis

The central trade-off is between retention quality (active recall > cued recognition > passive re-reading) and delivery friction. The system's constraints (no persistent process, owner uses GitHub website/iOS app only) force lower-friction mechanisms. The resolution is a layered stack: passive digest for baseline recognition-level re-engagement; agent recall instruction for zero-friction active use of prior research during each session; conversational interface for on-demand high-quality active recall once the search layer is built.

The agent recall instruction is the highest-leverage change because it addresses agent-side retention at zero infrastructure cost. Every subsequent research session benefits from prior completed research. The compounding value of this change grows with corpus size.

The periodic digest is the next highest-leverage change. It requires a new GitHub Actions workflow but no new dependencies (PyYAML already in requirements, GITHUB_TOKEN already available). It produces a navigable archive of re-engagement events (GitHub issues with `retention-digest` label), enabling the owner to track which items have been reviewed.

Cross-reference embedding is a convention change requiring no workflow automation — only an AGENTS.md addition and an agent instruction. This should be the second implementation step.

SM-2 adaptive scheduling is explicitly deferred. Fixed intervals are sufficient at current corpus size. Adaptive scheduling requires tracking owner engagement quality, which is not technically available without additional tooling beyond what is scoped here.

The `semantic-full-text-search` item is a prerequisite for contextual recall ("what do I know about X?") and for the agent recall instruction to work reliably at scale. As long as `Research/completed/` contains fewer than ~50 items, the agent can scan all items directly; beyond that, a search layer is needed.

### Risks, Gaps, and Uncertainties

- The claim that "conceptual knowledge decays within 2–4 weeks" is an inference from the Ebbinghaus baseline, not a direct measurement for research-level understanding. The actual decay timeline could be longer (deep initial encoding) or shorter (low personal relevance of some items).
- Passive digest delivery assumes the owner reads GitHub issues. Notification fatigue or issue inbox clutter could render the digest ineffective. No monitoring mechanism is designed here.
- The conversational recall mechanism depends on `2026-03-02-semantic-full-text-search.md` being completed first. Until then, contextual recall is limited to what the agent can find via direct file inspection.
- The design assumes a single owner. If multiple agents or users access the corpus, the `state/reviews.json` approach requires coordination.
- No mechanism is designed to handle dismissed or low-value items that should not cycle through the digest indefinitely.

### Open Questions

- Should the periodic digest workflow also create a wiki page (persistent record) in addition to the GitHub issue (transient notification)? May become a backlog item for the digest workflow implementation.
- At what corpus size does fixed-interval scheduling become insufficient and adaptive scheduling (requiring owner engagement tracking) become necessary? Estimated ~200–500 items; not validated.
- Should the agent recall instruction also surface `Research/in-progress/` items (parallel work in flight), not just `Research/completed/`?

---

## Output

- Type: knowledge, backlog-item
- Description: Knowledge decay characterisation for research-level understanding; spaced repetition applicability at item level; layered retention mechanism design (agent recall instruction, periodic digest workflow, cross-reference embedding, conversational recall); agent recall instruction ready for immediate addition to `research-prompt.md`; `state/reviews.json` schema defined
- Links:
  - https://en.wikipedia.org/wiki/Testing_effect (retrieval practice evidence base)
  - https://en.wikipedia.org/wiki/Levels_of_processing_effect (encoding depth and knowledge durability)
  - https://en.wikipedia.org/wiki/Spaced_repetition (spacing effect and SM-2 applicability)