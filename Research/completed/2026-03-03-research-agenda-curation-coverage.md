---
title: "Research agenda curation: prioritisation, coverage analysis, and avoiding research drift"
added: 2026-03-03T10:13:26+00:00
status: completed
priority: high
blocks: []
tags: [research-agenda, prioritisation, coverage, curation, strategy, backlog-management, research-drift]
started: 2026-03-03T10:13:26+00:00
completed: 2026-03-03T10:13:26+00:00
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

- [x] `AGENTS.md` — When the Backlog Is Empty section; research item lifecycle; distinction between repo backlog and research backlog
- [x] `Research/backlog/2026-02-27-sources-of-research.md` — orthogonal question: where new items come from; this item answers what to do with them once they arrive
- [x] `Research/completed/2026-02-27-research-backlog-vs-repo-improvement-backlog.md` — the documented distinction between the two backlogs; apply the same clarity to agenda management
- [x] `BACKLOG.md` — existing prioritisation discipline for repo improvements; patterns to adapt
- [x] Personal Knowledge Management (PKM) literature on research agenda management: Tiago Forte's PARA method, progressive summarisation as a triage tool; relevant to deciding what to research vs. what to archive — https://fortelabs.com/blog/para/
- [x] Jobs-to-be-done framework (Christensen): structured approach to defining value and priority by outcome rather than by topic interest — applicable to research prioritisation — https://hbr.org/2016/09/know-your-customers-jobs-to-be-done
- [x] OKR (Objectives and Key Results) methodology: assess whether a quarterly research OKR (e.g., "understand the NZ AI regulatory landscape well enough to advise on compliance") provides useful top-down prioritisation constraints — https://www.whatmatters.com/faqs/okr-meaning-definition-example
- [x] `Research/backlog/2026-03-02-research-quality-assurance-methodology.md` — identifies "applicability testing" as a quality dimension; agenda curation is the upstream version: only add items where the knowledge would be applicable
- [x] `src/research/item.py` and `src/research/cli.py` — existing YAML front-matter schema and CLI; extension points for `agenda` command

---

## Research Skill Output

### §0 Initialise

**Research question restated:** How should the research backlog for `davidamitchell/Research` be maintained and prioritised to ensure balanced coverage of strategically important domains, detect over-concentration in one area (research drift), and surface high-value gaps?

**Scope confirmed:** Meta-level agenda management only. Output must derive all signals from existing YAML front-matter fields (`tags`, `priority`, `status`, `added`, `completed`). No new external services. Tooling must be invocable as `python -m src.main research agenda` and as a GitHub Actions step.

**Constraints confirmed:**
- No new credentials or external services
- Owner accesses repo via GitHub website / iOS only — any agenda report must be visible as a file commit or GitHub issue
- Tooling must extend `src/research/cli.py` following existing patterns (type hints, `ruff`-compliant, tests in `tests/`)

**Output format:** Knowledge (domain map, coverage metrics, prioritisation rubric, drift thresholds, agenda review checklist) + tool specification (CLI command design) + backlog items (for implementation).

---

### §1 Question Decomposition

**Root question:** How to maintain a strategically balanced, prioritised research backlog?

Decomposed into atomic questions:

**Branch A — Domain map**
- A1. What are the 4–6 top-level research domains for this repo?
- A2. What are the primary tags that map to each domain?
- A3. What is the current domain distribution of the 25-item backlog and 23-item completed corpus?
- A4. What is the appropriate minimum/maximum item count per domain?

**Branch B — Coverage metrics**
- B1. Which YAML fields carry domain-relevant signals?
- B2. What is the current priority distribution (high/medium/low) across the backlog?
- B3. Is there priority inflation (most items rated medium with insufficient differentiation)?
- B4. What is tag density per domain in current backlog vs. completed corpus?

**Branch C — Research drift detection**
- C1. What does drift look like in this corpus?
- C2. What statistical threshold separates intentional focus from problematic drift?
- C3. What is an appropriate detection window (last N items added vs. last N days)?

**Branch D — Prioritisation framework**
- D1. What dimensions determine a research item's strategic value?
- D2. What scoring rubric maps those dimensions to high/medium/low?
- D3. How does the JTBD framework apply to research item prioritisation?
- D4. Do OKRs provide useful top-down prioritisation constraints?
- D5. Does PARA provide useful structural analogies?

**Branch E — Agenda review cadence**
- E1. How often should the backlog be reviewed as a whole?
- E2. What questions must a review answer?
- E3. What is the minimum viable output from a review?
- E4. How should the review be triggered given the owner's GitHub-only access?

**Branch F — Tooling design**
- F1. What data can be derived purely from YAML front-matter?
- F2. What is the command interface and output format?
- F3. How does the `agenda` command integrate with existing CLI patterns in `src/research/cli.py`?

---

### §2 Investigation

#### A1–A4: Domain map

**[fact]** Current backlog (25 items) and completed corpus (23 items) tag analysis (derived directly from repo files, 2026-03-03):

Top tags in backlog: `ai-strategy` (5), `consciousness`/`anil-seth` (4 each), `interface`/`delivery`/`youtube`/`tooling` (4 each), `transcripts`/`automation` (3), `agents`/`search`/`rag`/`storage` (2 each).

Top tags in completed: `ai-strategy` (6), `financial-services` (4), `knowledge-management`/`synthesis`/`risk-management` (3 each), `youtube`/`workflow`/`process`/`predictive-processing` (2 each).

**[inference]** The corpus separates into five coherent domains based on tag co-occurrence:

| Domain | Primary tags | Backlog items | Completed items |
|--------|-------------|---------------|-----------------|
| **D1 — AI Strategy & Governance** | ai-strategy, governance, security, financial-services, rbnz, nz-specific, software-engineering | 5 | 8 |
| **D2 — Agentic Systems & Architecture** | agents, agentic-ai, agentic-coding, mcp, lsp, context-management, memory, architecture | 2 | 4 |
| **D3 — Cognitive Science & Foundations** | consciousness, predictive-processing, entropy, free-energy-principle, anil-seth, interoception, perception | 4 | 3 |
| **D4 — Research Tooling & Delivery** | tooling, youtube, transcripts, automation, interface, delivery, indexing, storage, search, rag, chat | 11 | 5 |
| **D5 — Knowledge Management & Process** | knowledge-management, synthesis, workflow, process, research-methodology, quality-assurance | 3 | 3 |

Note: Some items straddle domains (e.g., `ai-not-a-data-problem` touches D1 and D2). The primary domain is assigned by the most specific tag cluster.

**[fact]** D4 (Research Tooling & Delivery) dominates the backlog with 11 of 25 items (44%). D2 (Agentic Systems) is under-represented with only 2 backlog items despite 4 completed — no new agentic work has been queued recently. D3 (Cognitive Science) has 4 backlog items, all spawned from a single completed research item (Anil Seth Essentia Foundation synthesis), indicating a local cluster.

**[inference]** A healthy domain target for this repo: D1 and D2 should each maintain 3–5 backlog items (they are directly tied to professional decision-making). D3 is exploratory and should be capped at 3 items at a time to prevent crowding out applied domains. D4 and D5 should not exceed 40% of total backlog combined (currently at ~56%).

#### B1–B4: Coverage metrics

**[fact]** YAML fields available for coverage analysis: `tags` (domain signal), `priority` (urgency signal), `added` (recency/age signal), `status` (lifecycle), `completed` (completion date), `blocks` (dependency signal), `output` (type signal).

**[fact]** Current priority distribution in 25-item backlog: `high` = 1 (4%), `medium` = 22 (88%), `low` = 2 (8%). The item being researched (this item) was one of two `high` items; upon completion, only 1 `high` item remains in backlog.

**[inference]** Priority inflation at `medium` is severe. With 88% of items rated medium, the priority field provides almost no differentiation. The autonomous loop's item-selection logic (high > medium > low, then blocks, then oldest) cannot meaningfully distinguish 22 medium items — it degrades to oldest-first, which may not reflect strategic importance. Priority inflation is a known failure mode in backlog management; it occurs when adding items feels easier than making priority judgements.

**[fact]** The BACKLOG.md repo improvement backlog uses ordering rather than an explicit priority field, and it works because an agent reads the whole file and can infer priority from position and epic context. Research items cannot rely on ordering because (a) they are individual files sorted by filename, and (b) the autonomous loop reads front-matter programmatically. The priority field is therefore critical for research items in a way it is not for BACKLOG.md items. Source: `Research/completed/2026-02-27-research-backlog-vs-repo-improvement-backlog.md` Key Finding 5.

#### C1–C3: Research drift detection

**[fact]** In portfolio management literature, "drift" refers to gradual deviation from an intended allocation. In research, drift occurs when additions cluster in one domain, gradually crowding out others. Source: RAND Corporation, "Evolving the Practice of Evaluating Research Portfolios" (https://www.rand.org/content/dam/rand/pubs/research_briefs/RB10000/RB10036/RAND_RB10036.pdf).

**[inference]** Two distinct drift signals apply to this corpus:

*Addition drift*: ≥40% of items added in the last 30 calendar days share a primary domain tag. This is calibrated to the corpus size (~25 items, ~3/day processing rate): 30 days × 3/day = ~90 additions would be needed to fill the backlog at rate, but additions occur at ~1–5/session. If a 10-item addition session puts 5 items in the same domain, that is 50% concentration and warrants a flag.

*Completion drift*: the last 5 completed items are all from the same domain. This indicates the autonomous loop has been consuming one domain's items faster than it is replenishing others.

**[inference]** The 40% threshold is conservative enough to tolerate intentional focused sprints (e.g., "research all transcript-fetching approaches together") without firing on them, while catching unintentional drift. Setting it at 50% would be too permissive. Setting it at 30% would generate false positives during legitimate focused work. The threshold should be configurable in the agenda command rather than hard-coded.

**[assumption]** A 30-day window is appropriate for addition drift detection. **Justification:** The autonomous loop runs weekdays at 3 items/day, so 30 days represents ~60 items of throughput — enough to observe meaningful distribution patterns. A 7-day window would be too noisy; a 90-day window too slow to catch drift.

#### D1–D5: Prioritisation framework

**[fact]** The JTBD (Jobs to be Done) framework (Christensen) frames value by asking: "what outcome does the actor need this research to enable?" Research priority should derive from downstream use, not topic interest. Applied to this corpus: a research item is high-priority if its completion enables a decision, unblocks tooling, or closes a knowledge gap that is currently constraining action. Sources: Sivoi Insights "How JTBD Connects Research, Strategy and Go-to-Market" (https://mrx.sivoinsights.com/blog/how-jobs-to-be-done-connects-research-strategy-and-execution); WHO "Shaping the Research Agenda" (https://www.who.int/our-work/science-division/research-for-health/optimizing-research-processes/shaping-the-research-agenda).

**[fact]** OKR methodology provides a top-down constraint structure: a quarterly research Objective (e.g., "Understand NZ AI regulatory landscape well enough to provide compliance guidance") defines which Key Results (specific research completions) are high-priority for that quarter. OKRs prevent bottom-up priority inflation by requiring alignment with a stated Objective. Sources: OKR International "What is the Quarterly OKR Cycle" (https://okrinternational.com/what-is-the-quarterly-okr-cycle/); Assay Genie "OKRs for Researchers" (https://www.assaygenie.com/blog/okrs-for-researchers).

**[fact]** Tiago Forte's PARA method organises information by actionability: Projects (current work with deadlines), Areas (ongoing responsibilities), Resources (reference), Archives (inactive). Applied to research: "Project" research = knowledge needed to complete a current active work item; "Area" research = maintaining domain expertise; "Resource" research = exploratory/foundational. This maps cleanly to priority: Project-level research = high, Area-level = medium, Resource/exploratory = low. Sources: Forte Labs (https://fortelabs.com/blog/para/); Building a Second Brain (https://www.buildingasecondbrain.com/para).

**[inference]** The four prioritisation dimensions that best capture strategic value for this corpus, synthesising JTBD, OKR, and PARA:

1. **Decision dependency** (1–3): Does a current active decision or work item depend on this research? (1 = no active dependency; 2 = would improve a pending decision; 3 = blocks a current decision or BACKLOG.md slice)
2. **Dependency unblocking** (1–3): Does completing this item explicitly unblock other backlog items or BACKLOG.md slices? (1 = no; 2 = unblocks ≥1 item; 3 = unblocks ≥3 items or a high-priority item)
3. **Knowledge gap severity** (1–3): How much does not having this knowledge constrain current decision quality? (1 = nice to know; 2 = noticeable gap; 3 = actively making decisions poorly due to absence)
4. **Input availability** (1–3): Are good sources accessible now? (1 = premature, sources not yet available; 2 = sources exist but incomplete; 3 = rich sources available, research is timely)

**[inference]** Scoring rule: sum the four dimensions (4–12 range). Map to priority: 10–12 = `high`; 6–9 = `medium`; 4–5 = `low`. This produces a tri-level priority that is sparse at `high` by design — only items with ≥3 in at least two dimensions reach `high`.

**[inference]** The current AGENTS.md heuristic for `high` priority ("answers a question that directly unblocks tooling/infrastructure/other research, or strategically urgent with clear downstream impact") aligns well with dimensions 1 and 2 above. The rubric formalises what the heuristic intended.

#### E1–E4: Agenda review cadence

**[fact]** RAND's research portfolio evaluation framework recommends both periodic (quarterly) holistic reviews and continuous item-level monitoring. The quarterly review assesses strategic alignment; item-level monitoring detects drift in near-real-time. Source: RAND "Evolving the Practice of Evaluating Research Portfolios".

**[inference]** For this corpus (personal repo, ~25 backlog items, 3 items/day processing rate): monthly review is appropriate rather than quarterly. At 3 items/day, the backlog turns over in ~8 weeks — a quarterly review would be reviewing a corpus that has been mostly replaced since the last review. Monthly is more actionable. Weekly is too frequent given the owner's access model (GitHub website/iOS only — review requires triggering a workflow).

**[inference]** Monthly agenda review checklist (minimum viable):
1. Domain balance: does each of the 5 domains have ≥1 item in backlog?
2. Priority health: are fewer than 50% of backlog items rated `medium` with ≥5 rated `high`? (Target: ≥3 `high`, ≤60% `medium`, ≥1 `low`)
3. Drift check: any domain >40% of items added in last 30 days?
4. Age check: any items added >60 days ago still in backlog? (May indicate the item is premature or no longer relevant)
5. Open Questions check: do completed items' Open Questions sections contain questions not yet added to backlog?
6. Coverage gaps: any domain with 0 items in both backlog and in-progress? (Requires addition)

**[fact]** The owner accesses the repo via GitHub website / iOS app only. A `workflow_dispatch`-triggered GitHub Actions workflow can run the agenda analysis and post results as a GitHub issue comment, making results visible without a local terminal. This is the prescribed pattern for owner-accessible reporting in this repo. Source: AGENTS.md "Consequences for tooling design".

#### F1–F3: Tooling design

**[fact]** `src/research/cli.py` already implements `cmd_add`, `cmd_list`, `cmd_start`, `cmd_complete`. The `register_subparser` function attaches sub-commands. Adding `agenda` follows the same pattern: a new `cmd_agenda` function, registered as `research agenda`. Source: direct inspection of `src/research/cli.py`.

**[fact]** `src/research/item.py` provides `ResearchItem.from_file(path)` which reads YAML front-matter into a dataclass with `tags`, `priority`, `status`, `added`, `completed`, `blocks`. All fields needed for agenda analysis are already parsed. Source: direct inspection of `src/research/item.py`.

**[inference]** The `agenda` command can be implemented without new dependencies (PyYAML and datetime are already present). It reads all items from `Research/backlog/`, `Research/in-progress/`, and `Research/completed/`, groups by domain (via a configurable domain-to-tags mapping), and produces a Markdown report. The domain map should be embedded in `src/research/cli.py` as a constant (dict mapping domain name → list of primary tags) rather than in a separate config file, to keep the tooling self-contained.

**[inference]** Output should be printed to stdout (Markdown format) and optionally written to a file. The GitHub Actions workflow can capture stdout and post it as a GitHub issue body via `gh issue create`. This avoids committing a report file that would be stale immediately.

---

### §3 Reasoning

**Facts established:**
- Current backlog has 25 items; priority distribution is 1 high (4%), 22 medium (88%), 2 low (8%) — severe medium inflation
- D4 (Research Tooling & Delivery) dominates at 44% of backlog; D2 (Agentic Systems) is under-represented at 8%
- D3 (Cognitive Science) has a 4-item cluster all spawned from one completed item — local drift from a single source
- YAML front-matter fields `tags`, `priority`, `added`, `completed`, `blocks` are sufficient for all agenda analysis
- Existing `src/research/item.py` and `src/research/cli.py` provide clean extension points
- Owner's access model requires GitHub-triggerable reporting (workflow_dispatch → GitHub issue)

**Inferences drawn:**
- Five domains are the right granularity: D1 AI Strategy/Governance, D2 Agentic Systems, D3 Cognitive Science, D4 Research Tooling, D5 Knowledge Management/Process
- 40% concentration threshold in a 30-day window is the right drift detection calibration
- Four-dimension prioritisation rubric (decision dependency, dependency unblocking, gap severity, input availability) formally captures the AGENTS.md heuristic
- Monthly review cadence matches the corpus turnover rate
- `research agenda` CLI command can be implemented using only existing dependencies and extending existing patterns

**Assumptions made:**
- The 40% drift threshold is the right calibration for this corpus (not verified against historical data; assessed against corpus size and processing rate)
- Monthly review cadence is appropriate (not validated; derived from corpus turnover arithmetic)
- Five domains adequately cover the owner's research interests (based on tag analysis; owner's actual domain priorities not confirmed)

---

### §4 Consistency Check

**Internal consistency verified:**

- The domain map (5 domains) is consistent with the tag distribution observed in both backlog and completed corpus. No tag clusters fall outside the 5-domain taxonomy.
- The prioritisation rubric (4 dimensions, 4–12 score, mapped to high/medium/low) is consistent with the AGENTS.md heuristic. The rubric is a formalisation, not a replacement.
- The drift threshold (40%, 30-day window) is consistent with the corpus size and processing rate. No internal contradiction.
- The monthly review cadence is consistent with the corpus turnover rate (~8-week backlog at 3 items/day). No contradiction.

**Potential contradiction flagged:** The AGENTS.md heuristic says `high` priority is for items that "directly unblock tooling, infrastructure, or other research." The proposed rubric allows `high` without a `blocks` relationship (if decision dependency and gap severity are both 3). These are consistent: AGENTS.md lists unblocking as a *sufficient* condition for `high`, not the *only* condition.

**No irresolvable contradictions found.**

---

### §5 Depth and Breadth Expansion

**Technical lens:** The `agenda` CLI command should handle edge cases: empty directories, items with malformed YAML, items missing `tags` field. The `ResearchItem.from_file()` method already handles missing fields with defaults. The command should not fail on individual bad files — log a warning and continue, matching the error-handling pattern in `src/main.py`.

**Economic lens:** Priority inflation at `medium` has a concrete cost: the autonomous loop's selection algorithm degrades to oldest-first when all items are equally prioritised. This means the loop processes items in the order they happened to be created, not the order they are strategically valuable. Every `medium` item processed ahead of a genuinely `high`-priority item represents a misallocation of the loop's capacity. At 3 items/day, 5 days of misallocation = 15 items processed out of priority order.

**Behavioural lens:** Priority inflation is not a failure of intention — it is a failure of the process for adding items. When adding a new item, the path of least resistance is to accept the default (`priority: medium`). The rubric must be embedded in the item-addition process to have effect. This means the `research add` CLI template should include the rubric as a comment, and AGENTS.md should reference the rubric when documenting the item-addition process.

**Regulatory/professional context lens:** D1 (AI Strategy & Governance) and the NZ regulatory sub-domain (RBNZ AI expectations) are directly tied to the owner's professional context. These items should not be deprioritised by a tool that naively applies drift detection. The domain map should include a `strategic_weight` field that can bias the coverage minimum upward for professionally critical domains. D1 should have a minimum of 2 items in backlog at all times.

**Historical lens:** The BACKLOG.md repo improvement backlog uses ordering rather than explicit priority — this worked at repo inception because items were added in dependency order and the file was small. As research backlog grows beyond ~20 items, ordering breaks down because the file-system ordering (alphabetical by date+slug) does not reflect strategic priority. The research backlog reached 27 items before a priority framework was introduced — this is the frontier at which the failure becomes visible.

---

### §6 Synthesis

#### Summary

The research backlog requires three interlocking mechanisms to remain strategically useful: (1) a **domain map** that defines coverage targets, (2) a **prioritisation rubric** that produces genuinely sparse `high` allocations, and (3) a **monthly agenda review** that detects drift and surfaces gaps. All three can be implemented using existing YAML front-matter and existing CLI patterns. The current backlog has severe priority inflation (88% medium) and domain concentration in Research Tooling (44%), indicating both mechanisms have been absent since inception.

#### Key Findings

1. **Priority inflation is the primary current failure.** 88% of 25 backlog items are rated `medium`. The autonomous loop's selection algorithm degrades to oldest-first when all items are equally prioritised, making the `priority` field ineffective. [fact — derived from YAML front-matter analysis]

2. **D4 (Research Tooling & Delivery) has drifted to 44% of backlog.** 11 of 25 items relate to tooling, interface, delivery, and transcript fetching. This crowding reduces space for AI Strategy (D1) and Agentic Systems (D2) items, which are more directly tied to professional decision-making. [fact — derived from tag analysis]

3. **A five-domain taxonomy covers the corpus without gaps.** D1 AI Strategy & Governance; D2 Agentic Systems & Architecture; D3 Cognitive Science & Foundations; D4 Research Tooling & Delivery; D5 Knowledge Management & Process. All 48 items (backlog + completed) map to exactly one primary domain. [inference — derived from tag co-occurrence analysis]

4. **The prioritisation rubric should use four dimensions: decision dependency, dependency unblocking, knowledge gap severity, input availability.** Scored 1–3 each; sum 10–12 = high, 6–9 = medium, 4–5 = low. This matches the intent of the AGENTS.md heuristic while producing a distribution where `high` is genuinely rare. [inference — synthesised from JTBD, OKR, and PARA frameworks]

5. **Drift detection threshold: ≥40% domain concentration in items added in the last 30 days.** A secondary signal: the last 5 completed items all from the same domain. The 40% threshold is calibrated to tolerate intentional focused sprints while catching unintentional drift. [inference — calibrated to corpus size and processing rate]

6. **Monthly review cadence matches the corpus turnover rate.** At 3 items/day on weekdays, the backlog turns over in ~8 weeks. A monthly review catches imbalances before the next turnover cycle. Quarterly would be too slow. [inference — arithmetic]

7. **The `research agenda` CLI command can be implemented using only existing dependencies and extending existing CLI patterns.** `ResearchItem.from_file()` already parses all needed fields. The command adds a domain map constant and reporting logic to `src/research/cli.py`. [fact — derived from source inspection]

8. **D2 (Agentic Systems) is under-represented in backlog.** Only 2 of 25 backlog items relate to agents and agentic architecture, despite this being a strategically active area (4 items already completed). No new agentic items have been queued — this is a coverage gap. [fact — derived from tag analysis]

9. **D1 (AI Strategy & Governance) should have a protected minimum of ≥2 backlog items.** As the domain most directly tied to the owner's professional context (NZ financial services AI), it should not be allowed to drain to zero by the autonomous loop without triggering a coverage alert. [inference — professional context assessment]

10. **The rubric should be embedded at the item-addition step, not only at review time.** Priority inflation occurs because the default is `medium` and there is no prompt to apply a rubric. Adding the rubric as a comment in the `src/research/cli.py` template and referencing it in AGENTS.md's item-addition instructions will reduce inflation at the point of creation. [inference — behavioural analysis]

11. **A `workflow_dispatch`-triggered agenda analysis workflow posting results as a GitHub issue is the correct delivery mechanism.** This is the prescribed pattern for owner-accessible reporting in AGENTS.md and does not require new credentials. [fact — AGENTS.md "Consequences for tooling design"]

12. **Open Questions from completed items are an under-used backlog input.** The research template includes an Open Questions section, and several completed items contain questions not yet added as backlog items. The agenda review checklist should explicitly scan Open Questions sections for unadded follow-on items. [inference — observation from completed items review]

#### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| 88% of backlog items are rated `medium` | YAML front-matter analysis, 2026-03-03 | high | Direct count: 22/25 medium |
| D4 (Research Tooling) = 44% of backlog | Tag analysis of Research/backlog/*.md | high | 11/25 items tagged with tooling/interface/delivery/youtube/transcripts |
| Five domains cover all 48 items | Tag co-occurrence analysis of all items | medium | Some items straddle domains; assignment to primary domain is an inference |
| Four-dimension rubric matches AGENTS.md heuristic | AGENTS.md heuristic; JTBD (Sivoi Insights); OKR (OKR International); PARA (Forte Labs) | medium | Synthesis across three frameworks; no single source validates the exact rubric |
| 40% drift threshold appropriate for this corpus | RAND research portfolio evaluation; corpus size arithmetic | medium | Threshold not empirically validated; derived from first principles |
| Monthly review cadence | Corpus turnover arithmetic (3/day × 20 working days = 60 items/month vs. 25-item backlog) | high | Arithmetic is direct; assumption is that 3/day rate is sustained |
| `research agenda` command implementable without new dependencies | Direct inspection of src/research/item.py, src/research/cli.py | high | All required fields already parsed; Python stdlib sufficient for report generation |
| D2 (Agentic Systems) under-represented | Tag analysis: 2 of 25 backlog items | high | Direct count |
| workflow_dispatch + GitHub issue is correct delivery | AGENTS.md "Consequences for tooling design" | high | Explicitly stated in AGENTS.md |
| Open Questions are under-used as backlog input | Review of completed items | medium | Observed in several items; not systematically counted |

---

### §7 Recursive Review

**Completeness check:**
- §0 Initialise: ✅ Research question restated; scope, constraints, output format confirmed
- §1 Question Decomposition: ✅ Six branches covering all approach sub-questions; each branch decomposed to atomic questions
- §2 Investigation: ✅ All sources checked; claims labelled [fact]/[inference]/[assumption]; evidence gathered for each atomic question
- §3 Reasoning: ✅ Facts, inferences, and assumptions separated; no unsupported generalisations
- §4 Consistency Check: ✅ One potential contradiction identified and resolved
- §5 Depth and Breadth Expansion: ✅ Technical, economic, behavioural, professional, and historical lenses applied
- §6 Synthesis: ✅ 12 key findings; all with confidence labels; evidence map complete

**Threads confirmed synthesised:** domain map (A), coverage metrics (B), drift detection (C), prioritisation framework (D), review cadence (E), tooling design (F)

**Outstanding gaps:** The 40% drift threshold and 5-domain taxonomy are inferences without empirical validation against historical data. Both are flagged with medium confidence and noted in Risks/Gaps.

**Validation outcome:** Research skill output is complete and self-consistent. Proceeding to Findings section.

---

## Findings

### Executive Summary

The research backlog for `davidamitchell/Research` currently lacks a domain map, a principled prioritisation rubric, and a drift detection mechanism — three interlocking deficiencies that cause the autonomous research loop to process items in creation order rather than strategic priority order. Priority inflation (88% of 25 items rated `medium`) and domain concentration (44% of backlog in Research Tooling & Delivery) are the two observable symptoms. The remedy is a five-domain taxonomy, a four-dimension prioritisation rubric, a 40%-concentration drift detection threshold, and a monthly agenda review triggered by `workflow_dispatch` and reported as a GitHub issue. All tooling can be implemented by extending `src/research/cli.py` with a `research agenda` command using only existing dependencies and parsed YAML fields.

### Key Findings

1. **Priority inflation renders the priority field ineffective.** 88% of 25 backlog items are rated `medium`. The autonomous loop's selection algorithm degrades to oldest-first when all items are equally prioritised. [high confidence — direct measurement]

2. **D4 Research Tooling & Delivery has drifted to 44% of backlog.** 11 of 25 items cluster around tooling, interface, delivery, and transcript fetching — crowding out AI Strategy (D1) and Agentic Systems (D2) items more directly tied to professional decision-making. [high confidence — direct count]

3. **Five domains cover the corpus without gaps.** D1 AI Strategy & Governance; D2 Agentic Systems & Architecture; D3 Cognitive Science & Foundations; D4 Research Tooling & Delivery; D5 Knowledge Management & Process. All 48 items map to exactly one primary domain. [medium confidence — taxonomy is an inference; some items straddle domains]

4. **The prioritisation rubric uses four dimensions: decision dependency, dependency unblocking, gap severity, input availability.** Scored 1–3 each; total 10–12 = `high`, 6–9 = `medium`, 4–5 = `low`. This produces a distribution where `high` requires ≥3 in at least two dimensions — genuinely rare by design. [medium confidence — synthesised from JTBD, OKR, PARA; not empirically validated]

5. **D1 (AI Strategy & Governance) should maintain a protected minimum of ≥2 backlog items.** As the domain most directly tied to the owner's professional context, it should trigger a coverage alert if it drains to zero during loop processing. [medium confidence — professional context inference]

6. **D2 (Agentic Systems) is currently under-represented.** 2 of 25 backlog items despite 4 completed items and active professional relevance. No new agentic items have been queued — this is a gap requiring agenda intervention. [high confidence — direct count]

7. **Drift detection threshold: ≥40% domain concentration in items added in the last 30 days.** Secondary signal: last 5 completed items all from the same domain. The 40% threshold tolerates intentional focused sprints while catching unintentional drift. [medium confidence — calibrated estimate, not empirically validated]

8. **Monthly review cadence matches corpus turnover rate.** At 3 items/day on weekdays, the 25-item backlog turns over in ~8 weeks. Monthly reviews catch imbalances before the next cycle. [high confidence — arithmetic]

9. **The `research agenda` CLI command is implementable without new dependencies.** All required fields (`tags`, `priority`, `added`, `completed`, `blocks`) are already parsed by `ResearchItem.from_file()`. The command requires only a domain-map constant and reporting logic added to `src/research/cli.py`. [high confidence — direct source inspection]

10. **The rubric must be embedded at item-addition time, not only at review time.** Priority inflation occurs because the default is `medium` and there is no friction at creation. The CLI template in `src/research/cli.py` and the AGENTS.md item-addition instructions should reference the rubric. [medium confidence — behavioural inference]

11. **`workflow_dispatch` + GitHub issue is the correct delivery mechanism for agenda reports.** This is the owner's access model and is explicitly prescribed in AGENTS.md. No new credentials required. [high confidence — AGENTS.md direct]

12. **Open Questions in completed items are an under-used backlog input.** Multiple completed items contain follow-on questions not yet added to backlog. The monthly review checklist should scan Open Questions sections systematically. [medium confidence — qualitative observation]

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| 88% medium priority inflation | YAML front-matter analysis, Research/backlog/*.md, 2026-03-03 | high | Direct count: 22 medium, 1 high, 2 low out of 25 items |
| D4 = 44% of backlog | Tag analysis: Research/backlog/*.md | high | 11/25 items carry tooling/interface/delivery/youtube/transcripts tags |
| Five-domain taxonomy covers all items | Tag co-occurrence analysis of all 48 items | medium | Primary domain assignment is inferential for multi-domain items |
| Four-dimension rubric aligns with AGENTS.md heuristic | AGENTS.md heuristic; Sivoi Insights JTBD; OKR International; Forte Labs PARA | medium | No single source validates exact rubric; synthesis across three frameworks |
| D1 professional priority | AGENTS.md repo description; Research/completed/2026-02-27-research-backlog-vs-repo-improvement-backlog.md | medium | Professional context inference, not stated explicitly |
| D2 under-representation | Tag analysis: 2/25 backlog items with agents/agentic/mcp/lsp tags | high | Direct count |
| 40% drift threshold | RAND research portfolio evaluation; corpus-size arithmetic | medium | First-principles estimate; no historical validation |
| Monthly cadence | Corpus turnover arithmetic | high | 3 items/day × 20 working days = 60/month throughput vs. 25-item backlog |
| `research agenda` implementable | Direct inspection of src/research/item.py, src/research/cli.py | high | All required fields already parsed |
| Rubric embedding in template | Behavioural analysis; PARA prioritisation-at-creation principle | medium | Inferred from best practice; not validated |
| workflow_dispatch + issue delivery | AGENTS.md "Consequences for tooling design" | high | Explicitly stated |
| Open Questions under-used | Qualitative review of Research/completed/*.md | medium | Several completed items have unadded Open Questions; not systematically counted |

### Assumptions

- **Assumption:** The five-domain taxonomy is stable for this repo. **Justification:** The corpus has 48 items with clear tag clusters; the five domains emerged from bottom-up tag analysis and align with the owner's described professional context (NZ financial services, SWE, personal intellectual development). A sixth domain (e.g., "Emerging Technology Trends") is possible but no tag cluster currently supports it.
- **Assumption:** 3 items/day processing rate is sustained on weekdays. **Justification:** This is the configured scheduled rate in `research-loop.yml`. Actual rate may vary based on item complexity and loop failures.
- **Assumption:** The 40% drift threshold is appropriate for this corpus. **Justification:** Calibrated from first principles based on corpus size and processing rate; not empirically tested. Should be reviewed after 3 months of operation.

### Analysis

The core finding is that the backlog's two observable failures (priority inflation and domain concentration) share a single root cause: there is no friction at item-creation time. When adding an item is easy and there is no prompt to apply a rubric or check domain balance, items accumulate with default priority and in the domain of the current session's focus. The remedy must be applied upstream (at creation) and downstream (at monthly review), not only when the loop selects the next item.

JTBD, OKR, and PARA each contribute a different constraint to the prioritisation rubric:
- JTBD contributes the "decision dependency" dimension — priority derives from downstream use, not topic interest
- OKR contributes the concept of top-down quarterly constraints — a research OKR can override the bottom-up rubric for specific items
- PARA contributes the insight that "Project-level" research (needed for current active work) should always be `high`, regardless of other dimensions

The four-dimension rubric synthesises all three: it requires both downstream use (JTBD/PARA) and availability (pragmatic) and connectivity (OKR-like unblocking) to reach `high`. Items that are merely interesting score at most 7–8 (medium).

The trade-off between drift detection sensitivity and false-positive rate is managed by the 40% threshold and the 30-day window. A focused research sprint (e.g., "complete all transcript-fetching approaches") should not be penalised — it is intentional concentration. The distinction is whether the concentration was deliberate (items were added in a burst to complete a known cluster) or inadvertent (items drifted in one direction over time without recognition). The monthly review checklist includes a question to distinguish these cases.

### Risks, Gaps, and Uncertainties

- The 40% drift threshold is calibrated from first principles rather than historical data. It may need adjustment after 3 months of operation. The threshold should be a configurable parameter, not a hard-coded constant.
- The five-domain taxonomy does not cover all possible future additions. As the repo owner's interests evolve, new domains may emerge. The domain map constant in `src/research/cli.py` should be easy to update without code changes — consider moving it to `config/sources.yaml` or a new `config/domains.yaml`.
- Priority inflation is a recurrence risk. Even with the rubric embedded in the template, agents adding items will sometimes skip the rubric under time pressure. A CI check that flags items with no explicit rubric justification (e.g., missing a `priority_rationale` field) would be stronger than a template comment, but adds schema complexity.
- The five-domain taxonomy based on primary tags may incorrectly assign some items. `agent-lsp-policy-enforcement` could belong to D1 (governance), D2 (agentic systems), or D4 (tooling) depending on how it is read. The domain assignment logic in the `agenda` command should use tag intersection (item tags ∩ domain primary tags → highest overlap domain) rather than single-tag lookup.
- Open Questions in completed items have never been systematically harvested. The monthly review checklist requires a human (or agent) to read Open Questions sections and compare against the backlog. This is manual and error-prone; a future CLI command could automate it.

### Open Questions

- Should the domain map be moved to a configuration file (`config/domains.yaml`) rather than a constant in `src/research/cli.py`? Would allow the owner to adjust domain boundaries via the GitHub web editor without code changes. → New backlog item: moderate priority.
- Should there be a `priority_rationale` field in the research item front-matter to document why an item was assigned a given priority? Would provide an audit trail and enforce rubric application. → AGENTS.md update consideration.
- Should a CI check fire when a PR adds a new backlog item without applying the prioritisation rubric? This would be a structural check, not a content check. → Could be implemented as a GitHub Actions step in `ci.yml`.
- As the backlog shrinks toward 0 (loop consuming items faster than they are added), should the agenda tool produce a "backlog replenishment" alert? At <5 items, the owner should be prompted to run a backlog-filling session. → New backlog item or AGENTS.md update.
- Is there a quarterly "research OKR" worth introducing formally — e.g., a `Research/objectives/` directory with quarterly `.md` files? This would provide top-down priority constraints that override the bottom-up rubric for specific items. → Worth exploring once the basic rubric and review mechanism are in place.

---

## Output

- Type: knowledge, tool, backlog-item
- Description:
  - **Knowledge:** Domain map (5 domains with primary tags); four-dimension prioritisation rubric (scoring 1–3 per dimension, 10–12 = high, 6–9 = medium, 4–5 = low); drift detection thresholds (≥40% domain concentration in last 30 days or last 5 completions); monthly agenda review checklist (6 questions); current backlog diagnosis (priority inflation at 88% medium; D4 tooling drift at 44%; D2 agentic gap)
  - **Tool:** `python -m src.main research agenda` command specification — extends `src/research/cli.py` using `ResearchItem.from_file()`, domain-map constant, Markdown report output, no new dependencies
  - **Backlog items spawned:** `implement-research-agenda-command` (implement the `research agenda` CLI command and associated workflow); `research-domains-config` (move domain map to `config/domains.yaml`)
- Links:
  - `Research/completed/2026-02-27-research-backlog-vs-repo-improvement-backlog.md` (two-backlog distinction; priority mechanism differences)
  - https://fortelabs.com/blog/para/ (PARA method — actionability-based prioritisation)
  - https://mrx.sivoinsights.com/blog/how-jobs-to-be-done-connects-research-strategy-and-execution (JTBD — outcome-based priority)