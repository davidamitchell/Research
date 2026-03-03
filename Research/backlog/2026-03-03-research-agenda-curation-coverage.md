---
title: "Research agenda curation: prioritisation, coverage analysis, and avoiding research drift"
added: 2026-03-03
status: backlog
priority: medium
tags: [research-agenda, prioritisation, coverage, curation, strategy, backlog-management, research-drift]
started: ~
completed: ~
output: [knowledge, tool, backlog-item]
---

# Research agenda curation: prioritisation, coverage analysis, and avoiding research drift

## Research Question

How should the research backlog be maintained and prioritised to ensure balanced coverage of important domains, detect over-concentration in one area (research drift), and surface high-value gaps — rather than accumulating items that are interesting but strategically unfocused?

## Scope

**In scope:**
- Domain map: defining the key research domains relevant to this repo's owner (NZ financial services AI, agentic systems, research tooling, cognitive science and AI foundations) and their relative strategic importance
- Coverage metrics: how to measure whether the backlog and completed corpus are balanced across domains, and how to detect when one domain is crowding out others
- Prioritisation methodology: what factors should determine a research item's priority (`high`/`medium`/`low`) beyond intuition — strategic urgency, dependency unblocking, knowledge gap severity, time-sensitivity
- Research drift detection: how to notice when a series of backlog additions is narrowing to a single sub-topic (e.g., six consecutive items all about agent memory) and when that is appropriate vs. when it indicates loss of strategic focus
- Agenda review cadence: how often the backlog should be reviewed as a whole (vs. item by item), and what questions to ask during that review
- Tooling: a lightweight analysis command (`python -m src.main research agenda`) that reports tag distribution, domain coverage, and priority queue state

**Out of scope:**
- Individual research item prioritisation within a sprint (covered by the autonomous loop's item selection)
- Backlog item filing mechanics (covered by existing CLI tooling and `2026-02-27-simple-process-for-adding-research-item.md`)
- The content of any specific research domain (this is meta-level agenda management, not object-level research)

**Constraints:** Tooling must derive all signals from existing YAML front-matter (`tags`, `priority`, `status`, `added`, `completed`). No new external services. Any agenda analysis must be runnable as a GitHub Actions step or locally via `python -m src.main`.

## Context

The research backlog currently contains ~27 items spanning several loosely defined domains. There is no explicit domain map, no coverage target, and no process for reviewing the backlog as a whole. Items are added when ideas arise (from completed research Open Questions, from the owner's reading, or from agent sessions) and prioritised ad hoc.

As the autonomous loop processes 3 items per day on weekdays, the backlog is consumed rapidly. Without intentional curation, the loop will work through whatever happens to be at the top of the file system, which is not necessarily what is most strategically important.

There is a related AGENTS.md instruction: "When the Backlog Is Empty: Review `Research/backlog/` — pick up a research item that hasn't been started." But there is no guidance on *which* item to pick up or how to assess whether the overall backlog is healthy.

The `2026-02-27-sources-of-research.md` backlog item addresses where new research input comes from (sources). This item addresses the orthogonal question: once input is available, how do you decide what to investigate and in what order?

The `BACKLOG.md` repo improvement backlog has its own prioritisation discipline (Epic numbering, slice sequencing). The research backlog (`Research/backlog/`) lacks an equivalent discipline. This research item is about designing that discipline.

## Approach

1. **Domain map definition** — Define the primary research domains for this repository and their strategic priority:
   - What are the 4–6 top-level domains? (Proposed: AI strategy and governance; agentic systems and architecture; cognitive science and AI foundations; research tooling and process; NZ regulatory and financial services context; emerging technology trends)
   - How does each domain relate to the owner's professional context (NZ financial services, SWE, personal intellectual development)?
   - What is the appropriate balance across domains? Should some domains always have ≥2 items in the backlog? Should some be capped?

2. **Coverage metric design** — Define measurable coverage metrics derivable from YAML front-matter:
   - *Tag density per domain*: for each domain, how many backlog items are tagged with its primary tags?
   - *Completion rate per domain*: of all items ever added per domain, what fraction has been completed?
   - *Recency balance*: when was the most recent item added per domain, and when was the most recent item completed per domain?
   - *Priority distribution*: what fraction of backlog items are `high` vs. `medium` vs. `low`? Is there priority inflation (everything becomes high)?

3. **Research drift detection** — Define what research drift looks like in this corpus and how to detect it:
   - Proposed signal: if ≥40% of backlog items added in the last 30 days share a primary domain tag, that domain is drifting toward over-representation
   - Secondary signal: if the last 5 completed items are all from the same domain, the loop may be stuck in a local area
   - Assess: what threshold is appropriate? What is the expected false-positive rate (drift signal fired when the concentration is intentional, e.g., during a focused research sprint)?

4. **Prioritisation framework** — Design a structured prioritisation framework for research items. Proposed dimensions:
   - *Strategic urgency*: does a decision depend on this research being completed in the next 30 days?
   - *Dependency unblocking*: does this item's completion unlock other backlog items or BACKLOG.md slices?
   - *Knowledge gap severity*: how much does the absence of this knowledge constrain decision quality?
   - *Input availability*: are good sources available and accessible now, or is this premature?
   Produce a simple scoring rubric (1–3 per dimension) that can be applied when adding or triaging items.

5. **Agenda review cadence and checklist** — Design a lightweight monthly agenda review:
   - What questions should the review answer? (Coverage balanced? Any domain with 0 items? Any items > 60 days old with no progress? Any completed items that spawned Open Questions that have not been added to backlog?)
   - Who/what triggers the review? (Proposed: `workflow_dispatch`-triggered analysis that posts a summary as a GitHub issue for the owner to review)
   - What is the minimum useful output from the review? (Proposed: a list of coverage gaps and a prioritised "next 5 items to research" recommendation)

6. **Tooling design** — Design a `python -m src.main research agenda` command:
   - Reads all items in `Research/backlog/` and `Research/completed/`
   - Reports: tag frequency distribution, priority distribution, domain coverage (using the domain map from step 1), items ≥ 60 days old without progress, Open Questions from completed items that have not spawned backlog items
   - Output: a human-readable report (Markdown table) that can be committed as `Research/agenda-report.md` or posted as a GitHub issue comment

7. **Assess relationship to BACKLOG.md** — The `BACKLOG.md` repo improvement backlog and the `Research/backlog/` research agenda serve different purposes (AGENTS.md explicitly documents this distinction). Assess whether any tooling or conventions from BACKLOG.md's prioritisation discipline should be adapted for the research agenda.

## Sources

- [ ] `AGENTS.md` — When the Backlog Is Empty section; research item lifecycle; distinction between repo backlog and research backlog
- [ ] `Research/backlog/2026-02-27-sources-of-research.md` — orthogonal question: where new items come from; this item answers what to do with them once they arrive
- [ ] `Research/completed/2026-02-27-research-backlog-vs-repo-improvement-backlog.md` — the documented distinction between the two backlogs; apply the same clarity to agenda management
- [ ] `BACKLOG.md` — existing prioritisation discipline for repo improvements; patterns to adapt
- [ ] Personal Knowledge Management (PKM) literature on research agenda management: Tiago Forte's PARA method, progressive summarisation as a triage tool; relevant to deciding what to research vs. what to archive
- [ ] Jobs-to-be-done framework (Christensen): structured approach to defining value and priority by outcome rather than by topic interest — applicable to research prioritisation
- [ ] OKR (Objectives and Key Results) methodology: assess whether a quarterly research OKR (e.g., "understand the NZ AI regulatory landscape well enough to advise on compliance") provides useful top-down prioritisation constraints
- [ ] `Research/backlog/2026-03-02-research-quality-assurance-methodology.md` — identifies "applicability testing" as a quality dimension; agenda curation is the upstream version: only add items where the knowledge would be applicable
- [ ] `src/research/item.py` and `src/research/cli.py` — existing YAML front-matter schema and CLI; extension points for `agenda` command

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
- Description: Domain map; coverage metrics definition; drift detection thresholds; prioritisation framework (scoring rubric); agenda review cadence and checklist; `research agenda` CLI command design
- Links:
  - `Research/completed/2026-02-27-research-backlog-vs-repo-improvement-backlog.md` (distinction between backlogs)
  - `Research/backlog/2026-02-27-sources-of-research.md` (complementary: where items come from)
  - `src/research/cli.py` (extension point for `agenda` command)
