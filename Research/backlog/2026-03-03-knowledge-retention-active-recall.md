---
title: "Knowledge retention: mechanisms for ensuring completed research is recalled and applied over time"
added: 2026-03-03
status: backlog
priority: medium
tags: [retention, recall, spaced-repetition, knowledge-decay, application, active-recall, knowledge-management]
started: ~
completed: ~
output: [knowledge, tool, backlog-item]
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

- [ ] Ebbinghaus (1885) — forgetting curve: foundational evidence on knowledge decay without re-engagement; https://en.wikipedia.org/wiki/Forgetting_curve
- [ ] Spaced repetition: SM-2 algorithm (Wozniak, 1990) — https://www.supermemo.com/en/blog/application-of-a-computer-to-improve-the-results-obtained-in-working-with-the-supermemo-method; assess applicability to research-level knowledge
- [ ] Make It Stick (Brown, Roediger, McDaniel, 2014) — evidence-based learning science: retrieval practice, interleaving, elaborative interrogation; what actually works for durable knowledge
- [ ] Ahrens (2017) — *How to Take Smart Notes* — re-engagement through writing and linking as the retention mechanism; why writing up findings matters more than re-reading
- [ ] `Research/backlog/2026-03-02-research-quality-assurance-methodology.md` — wisdom dimension: accumulated body of completed research forming decision-relevant understanding; retention is the prerequisite
- [ ] `Research/backlog/2026-03-03-cross-item-synthesis-meta-insights.md` — synthesis as a higher-retention output; digest and recall should prioritise synthesis items
- [ ] `Research/backlog/2026-03-02-chat-conversational-interface.md` — conversational recall ("what do I know about X?") as an active recall mechanism
- [ ] Obsidian Spaced Repetition plugin: https://www.stephenmwangi.com/obsidian-spaced-repetition/ — community implementation of SR for Markdown notes; patterns to adapt for this corpus
- [ ] `research-prompt.md` — agent recall instruction target: where to add the "check completed items before starting" instruction
- [ ] `state/index.json` and `src/state.py` — extension point for `last_reviewed` tracking

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
- Description: Knowledge decay characterisation for research-level understanding; spaced repetition applicability assessment; contextual recall mechanism designs; periodic digest workflow design; retention state tracking schema; agent recall instruction for `research-prompt.md`
- Links:
  - `Research/backlog/2026-03-02-research-quality-assurance-methodology.md` (wisdom dimension prerequisite)
  - `Research/backlog/2026-03-03-cross-item-synthesis-meta-insights.md` (synthesis as retention amplifier)
  - `Research/backlog/2026-03-02-chat-conversational-interface.md` (conversational recall mechanism)
  - `research-prompt.md` (agent recall instruction target)
