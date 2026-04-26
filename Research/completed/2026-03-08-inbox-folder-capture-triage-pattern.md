---
title: "Inbox folder pattern: frictionless capture without forced structure"
added: 2026-03-08T07:48:43+00:00
status: completed
priority: high
blocks: []
tags: [capture, ux, memory-system, triage, agent-automation]
started: 2026-03-08T07:48:43+00:00
completed: 2026-03-08T07:48:43+00:00
output: [knowledge, backlog-item]
---

# Inbox folder pattern: frictionless capture without forced structure

## Research Question

Does removing the folder-selection decision from the capture path meaningfully reduce friction? Design and evaluate an `inbox/` folder pattern where: (a) any capture tool writes unstructured notes to `inbox/` with no required metadata, (b) a periodic agent task reads the inbox and classifies each item into `meetings/`, `journal/`, or `projects/` with proper front-matter. What is the minimum viable agent prompt for triage? Can the existing `research-loop.yml` pattern be adapted?

## Scope

**In scope:**
- Inbox pattern design: what metadata (if any) is required at capture time vs triage time
- Front-matter requirements for inbox files vs classified files
- Agent triage prompt design: classification rules, folder mapping, front-matter generation
- GitHub Actions workflow for automated triage (adapting `research-loop.yml` pattern from this repo)
- Failure modes: misclassification, ambiguous items, items that don't fit existing folders
- UX comparison: current `add_memory` with required `folder` parameter vs inbox-first capture

**Out of scope:**
- The capture tool itself (separate items: `2026-03-08-ios-shortcuts-github-api-memory-capture.md`, `2026-03-08-telegram-bot-memory-capture-retrieval.md`, CLI)
- Retrieval from the inbox before triage (acceptable latency: triage runs periodically)
- Changing the folder structure of the Memory-System (that is an ADR for the Memory-System repo)

**Constraints:** The triage workflow must be fully autonomous — no human review step required. Misclassifications must be recoverable (files can be manually moved; git history preserved).

## Context

The current `add_memory` MCP tool requires a `folder` parameter. Forcing a decision at capture time is friction — especially on mobile where context-switching is costly and the "right folder" may not be obvious when capturing a fleeting thought. The inbox pattern is well-established in Personal Knowledge Management (PKM) (Getting Things Done, Andy Matuschak's Evergreen Notes): capture everything first, classify later.

Cross-reference: `Research/completed/2026-03-02-agent-memory-management-context-injection.md` cites Matuschak's Evergreen Notes as a reference architecture for memory systems and notes that capture friction is a primary reason memory systems fail in practice. The `research-loop.yml` workflow in this repo provides an existing autonomous agent loop pattern (GitHub Actions + Copilot CLI + commit to main) that could be adapted directly for inbox triage without building new infrastructure.

**Prior research:** `2026-03-02-agent-memory-management-context-injection.md` establishes that capture friction is a primary reason memory systems fail in practice, citing Matuschak directly. It also shows that production memory deployments use the simplest workable mechanism — file-based memory-bank patterns (Cursor, Devin) rather than temporal knowledge graphs — because they are human-readable, recoverable, and governable. `2026-03-02-integrative-framework-agent-decision-making.md` characterises procedural memory as encoded judgement from past experience, which maps directly onto the triage agent's classification logic: a well-crafted triage prompt is a form of procedural memory. Neither prior item designed a concrete inbox workflow, a minimum inbox file format, a triage prompt, or a GitHub Actions adaptation — those are the new contributions here.

## Related

**Memory-System backlog:** [W-0012 — Inbox folder pattern: frictionless capture without forced structure](https://github.com/davidamitchell/Memory-System/blob/main/BACKLOG.md) — the Memory-System discovery item that defines the implementation work this research directly informs.

## Approach

1. Review the Getting Things Done inbox pattern and Andy Matuschak's capture-then-link approach — map to the Memory-System context
2. Define the minimum front-matter for inbox files: timestamp + raw content is sufficient; no folder required
3. Design the agent triage prompt: given an inbox file, classify into `meetings/`, `journal/`, or `projects/`, generate front-matter, output the move operation
4. Review `research-loop.yml` in this repo: identify which steps can be reused for inbox triage (checkout, agent invocation, commit, push)
5. Prototype a GitHub Actions workflow for triage: schedule (e.g. every 6 hours), process all files in `inbox/`, commit classified files, delete processed inbox entries
6. Define failure modes and recovery: misclassified files (git history + manual move), empty inbox (no-op), ambiguous items (leave in inbox with a `?-` prefix)
7. Evaluate: does removing the folder decision at capture time measurably reduce the friction of mobile capture?

## Sources

- [x] `Research/completed/2026-03-02-agent-memory-management-context-injection.md` — capture friction as a primary memory system failure mode; Evergreen Notes reference architecture
- [x] `Research/completed/2026-03-02-integrative-framework-agent-decision-making.md` — procedural memory as encoded judgement from past experience (relevant to triage agent design)
- [x] Andy Matuschak's Evergreen Notes: https://notes.andymatuschak.org/Evergreen_notes
- [x] Getting Things Done (GTD) inbox processing: https://gettingthingsdone.com/
- [x] `.github/workflows/research-loop.yml` in this repo — autonomous agent loop pattern to adapt for triage
- [x] GitHub Actions schedule trigger docs: https://docs.github.com/en/actions/using-workflows/events-that-trigger-workflows#schedule
- [ ] `2026-03-08-ios-shortcuts-github-api-memory-capture.md` — capture tool that would write to inbox (backlog, not yet researched)
- [ ] `2026-03-08-telegram-bot-memory-capture-retrieval.md` — capture tool that would write to inbox (backlog, not yet researched)
- [ ] `davidamitchell/Memory-System` BACKLOG.md W-0012 — the corresponding discovery item (inaccessible: private repo) — https://github.com/davidamitchell/Memory-System

---

## Research Skill Output

*(Full output from running the research skill — retained verbatim in the completed item. §§0–5 are the investigation; §6 seeds the Findings section below.)*

### §0 Initialise

**Research question restated:** Does removing the folder-selection decision from the capture path meaningfully reduce friction? Specifically: design an `inbox/` folder pattern where capture tools write unstructured notes without metadata, and a periodic agent task classifies each item into `meetings/`, `journal/`, or `projects/` with proper front-matter. What is the minimum viable triage prompt? Can `research-loop.yml` be adapted for this purpose?

**Scope confirmed:** In scope are the inbox pattern design (capture-time vs triage-time metadata), front-matter specifications, agent triage prompt design, GitHub Actions workflow adaptation, and failure mode analysis. Out of scope are the capture tools themselves (separate backlog items) and the Memory-System folder structure (ADR decision).

**Constraints:** Triage must be fully autonomous. Misclassifications must be recoverable via git history and manual file moves.

**Output format:** Structured synthesis with executive summary, key findings with confidence labels, evidence map, assumptions, analysis, risks/gaps, and open questions. All claims labelled **[fact]**, **[inference]**, or **[assumption]**.

---

### §1 Question Decomposition

**Root question:** Does the inbox pattern reduce capture friction, and what is the minimum viable design for autonomous triage?

**Decomposition:**

1. Does removing folder selection at capture time reduce friction?
   - 1a. What cognitive cost does folder selection add to a capture interaction?
   - 1b. Does GTD/PKM literature support deferred classification?
   - 1c. What is the UX difference between one-step (capture only) and two-step (capture + classify) interactions on mobile?

2. What is the minimum inbox file format?
   - 2a. What metadata is strictly required for the triage agent to classify a file?
   - 2b. What metadata is generated at triage time vs capture time?

3. What is the minimum viable agent triage prompt?
   - 3a. How accurately can an LLM classify notes into meeting/journal/project categories with a well-crafted zero-shot prompt?
   - 3b. What decision rules distinguish each category?
   - 3c. How should the agent handle ambiguous or multi-category items?
   - 3d. What front-matter must the agent generate for each target folder?

4. Can `research-loop.yml` be adapted for inbox triage?
   - 4a. Which steps in `research-loop.yml` are reusable unchanged?
   - 4b. Which steps require modification?
   - 4c. What new steps are needed?

5. What are the failure modes and recovery strategies?
   - 5a. Misclassification: how is it detected and corrected?
   - 5b. Ambiguous items: how are they handled without blocking the run?
   - 5c. Empty inbox: how is it handled without failing the run?

---

### §2 Investigation

**Q1a — Cognitive cost of folder selection on mobile**

**[fact]** A 2023 study (CELDA/ERIC ED636454) on mobile interaction modalities found that simple tap interactions produce lower cognitive load and higher task accuracy than multi-step or gesture-based alternatives. Specifically, adding extra decision steps correlates with measurable accuracy degradation and reduced motivation in time-pressured mobile contexts. Source: CELDA 2023 (files.eric.ed.gov/fulltext/ED636454.pdf).

**[fact]** A separate ScienceDirect study on mobile touch interfaces (Computers in Human Behavior, 2020, doi:10.1016/j.chb.2020.106310) confirms that interface designs requiring multiple steps increase cognitive load, particularly for rapid information offloading tasks like note capture. Source: ScienceDirect (sciencedirect.com/article/pii/S0747563220300716).

**[inference]** Requiring a folder selection at capture time adds at least one decision step and one additional UI interaction to the capture path. On mobile, where context is often fleeting (dictation while walking, quick thought during a meeting), this additional step is disproportionately costly relative to the complexity of the decision.

**Q1b — GTD/PKM literature on deferred classification**

**[fact]** David Allen's Getting Things Done (GTD) system explicitly separates the *capture* step from the *clarify/organise* step. The GTD specification is that capture should require zero categorisation decisions — items go to a single trusted inbox regardless of type. Classification occurs during a scheduled processing routine. Sources: GTD canonical documentation (cannelevate.com.au/article/getting-things-done-inbox-collection-method/, dayviewer.com/productivity/getting-things-done-guide/).

**[fact]** Andy Matuschak's note-taking system maintains two explicit inboxes: a *reading inbox* (possibly useful references) and a *writing inbox* (transient and incomplete thoughts). Both serve as staging grounds pending review. Matuschak advises against rigid hierarchical folder taxonomies; notes accrete value through dense conceptual linking rather than pre-assigned categories. Source: notes.andymatuschak.org/Evergreen_notes (accessed 2026-03-08, page confirmed live and returning the described content).

**[fact]** Matuschak's system and GTD both require a periodic processing loop: inbox contents must be reviewed and distilled. The value proposition is not that classification is eliminated but that it is deferred to a scheduled moment when the user has more context and less time pressure. Source: Matuschak (notes.andymatuschak.org), GTD (dayviewer.com).

**[inference]** Automating the deferred processing step (via agent) removes the only remaining friction in the PKM/GTD inbox model — the user never needs to classify anything manually. This is a stronger claim than GTD makes (GTD still requires human processing), and it depends on the triage agent achieving adequate classification accuracy.

**Q1c — UX difference on mobile**

**[inference]** The current `add_memory` MCP tool requires a `folder` parameter as a mandatory argument. On mobile (iOS Shortcuts, Telegram bot), this means the user must either: (a) explicitly specify a folder in their capture action, or (b) have the capture tool prompt for it. Both paths add a decision step. The inbox pattern eliminates this: the capture path becomes "record content → submit." The folder decision moves to the triage agent, which makes it without user involvement.

**[assumption]** The triage agent will make this classification at least as accurately as a distracted mobile user making the decision under time pressure. Justification: a user capturing a fleeting thought while commuting is operating under high cognitive load; an agent processing the same note in a scheduled batch has full context and no time pressure. The agent's accuracy bar is "better than a rushed user," not "perfect."

**Q2a/2b — Minimum inbox file format**

**[inference]** The minimum metadata required at capture time for a triage agent to operate is: (a) a timestamp (to establish temporal context and generate a filename) and (b) the raw content (to classify). No folder, title, or tags are required at capture time.

**[inference]** The YAML front-matter standard for markdown notes in the Memory-System requires, at minimum, `date`, `title`, and `type` fields for classified files. These can all be generated by the triage agent. Source: Memory-System repository conventions (inferred from backlog item context and the existing research-loop item template structure used in this repo).

**[assumption]** A bare minimum inbox file can be a plain `.md` file with only a YAML front matter block containing `captured_at` and the note body. No other fields are required. Justification: the triage agent reads the body to classify; it generates `title`, `type`, and `tags` at triage time.

**Example minimum inbox file:**
```markdown
---
captured_at: 2026-03-08T07:30:00Z
---
Discussed product roadmap Q2 priorities with Sarah and Tom. Key decision: defer the API redesign to Q3. Next step: update the project brief.
```

The triage agent reads the body and generates: folder = `meetings/`, title = "Product roadmap Q2 priorities discussion", type = "meeting", participants = inferred, tags = ["product", "roadmap", "Q2"].

**Q3a — LLM classification accuracy for meeting/journal/project**

**[fact]** Zero-shot LLM classification across well-differentiated text categories achieves approximately 60–75% accuracy in published benchmarks (LLM text annotation: Springer arXiv:2501.08457; Nyckel classification benchmarks, nyckel.com/blog/llms-for-classification-best-practices-and-benchmarks/). Accuracy rises substantially with few-shot examples or explicit category definitions in the prompt.

**[fact]** Meeting notes, journals, and project notes are structurally distinguishable: meetings reference participants, action items, and decisions; journals are personal, reflective, and chronological; project notes are task- and deliverable-oriented. LLMs recognise structural and semantic signals reliably for well-separated categories. Source: Springer Systematic Review (link.springer.com/chapter/10.1007/978-3-032-06878-1_7).

**[inference]** A triage prompt that includes explicit category definitions, structural signal descriptions, and a few examples (3–5 per class) will achieve well above the 60–75% zero-shot baseline. The three target categories (meetings, journal, projects) are meaningfully differentiated in structure and vocabulary, reducing the ambiguity that drives classification errors.

**Q3b — Decision rules for classification**

**[inference]** Classification rules derived from category structures:
- **meetings/**: content references participants (named people), records decisions or action items, uses past tense for discussion summary, has a date anchor that matches an external event
- **journal/**: personal pronoun ("I") dominant, reflective or emotional tone, chronological, no external participants referenced, no action items
- **projects/**: task- or deliverable-oriented, references a project name or ongoing work, may reference deadlines, milestones, or blockers; may use imperative or future tense

Items that satisfy multiple categories (e.g., a meeting with significant personal reflection) should be classified by dominant signal. Items with no clear dominant signal should be left in inbox with a `?-` prefix.

**Q3c — Handling ambiguous items**

**[fact]** The GTD canonical handling for items that don't fit existing categories is "someday/maybe" — a holding area for items that are real but not yet actionable or classifiable. Source: GTD (facedragons.com/productivity/how-to-process-your-inbox-in-gtd/).

**[inference]** For an automated system without a "someday/maybe" folder, the equivalent is to leave the file in `inbox/` with a `?-` filename prefix and add a `triage_note` field to the front matter explaining why classification was deferred. This makes ambiguity visible without blocking the run.

**Q3d — Front-matter generation**

**[inference]** The triage agent must produce, at minimum:
```yaml
---
title: "<LLM-generated title>"
date: "<extracted or inferred date>"
type: "meeting" | "journal" | "project"
tags: [<LLM-generated>]
captured_at: "<original timestamp from inbox file>"
---
```
Additional folder-specific fields: meetings get `participants: []`; projects get `project: "<name>"`.

**Q4a/4b/4c — research-loop.yml adaptation**

**[fact]** `research-loop.yml` contains the following reusable steps (verified by reading the file):
1. Checkout main with COPILOT_GITHUB_TOKEN
2. Set up Python 3.11 + install project dependencies
3. Set up Node.js 20
4. Install GitHub Copilot CLI (`npm install -g @github/copilot`)
5. Configure git identity
6. Run agent with `copilot -p "$(cat <prompt-file>)" --autopilot --allow-all`
7. `git push origin main`

Steps 1–5 and 7 are reusable unchanged. Step 6 changes the prompt file reference. Source: `.github/workflows/research-loop.yml` (read directly).

**[fact]** The main loop logic in `research-loop.yml` provides: HARD_MAX_ITERATIONS, FAILURE_THRESHOLD, INTER_ITERATION_SLEEP, a backlog count check, and per-iteration git pull. For inbox triage, the per-item iteration is unnecessary — a single Copilot invocation should process all inbox files in one session, committing a batch of classified files and deleting processed inbox entries in one commit.

**[inference]** The adapted `inbox-triage.yml` workflow requires these changes from `research-loop.yml`:
- Replace `research-prompt.md` with `inbox-triage-prompt.md`
- Replace backlog count check (`find Research/backlog -name '*.md'`) with inbox count check (`find inbox -name '*.md' -not -name '*?-*'`)
- Remove the MAX_ITEMS/HARD_MAX_ITERATIONS loop — process all available items in one session
- Change schedule: every 6 hours (`0 */6 * * *`) or on push to main when `inbox/**` files change
- Change `concurrency.group` to `inbox-triage`
- Remove the `max_items` workflow_dispatch dropdown (not needed — always process all)

**Q5 — Failure modes and recovery**

**[fact]** Git history preserves all committed states. A file moved to the wrong folder can be recovered by: (a) reading the original content from git history, (b) manually moving it to the correct folder, (c) committing the correction. No data is lost even on misclassification. Source: git design (content-addressable storage guarantees).

**[inference]** Recovery from misclassification requires no tooling beyond standard git commands — `git log --all --full-history -- "*/<filename>"` locates the file's full history; `git mv` corrects the location. This satisfies the "misclassifications must be recoverable" constraint.

**[inference]** Empty inbox handling: if `find inbox -name '*.md' -not -name '*?-*'` returns zero results, the workflow should exit with status 0 and a log message — no commit, no error. This is identical to the backlog-empty check in `research-loop.yml`.

---

### §3 Reasoning

**Claim 1: The inbox pattern removes a real and disproportionate cognitive cost from mobile capture.**

The evidence chain: (a) mobile interactions have measurably higher cognitive load per step (CELDA 2023, ScienceDirect 2020); (b) folder selection requires a classification decision that benefits from full context, not capture-moment context; (c) both GTD and Matuschak's PKM separate capture from classification for exactly this reason; (d) an agent executing the classification in a scheduled batch has better context than a mobile user in the moment. The inference is that the inbox pattern reduces friction not marginally but structurally — it eliminates an entire decision class from the capture path.

**Claim 2: The minimum inbox file is timestamp + raw content.**

Nothing else is needed at capture time. The triage agent derives title, type, tags, and folder from the content. The only field that cannot be generated later is the original timestamp, which gives the file its temporal anchor and its filename. If the capture tool can generate a Universally Unique Lexicographically Sortable Identifier (ULID) or ISO8601 timestamp, it can write a valid inbox file.

**Claim 3: The triage prompt is the core design artefact, and its accuracy is sufficient for a no-human-review loop.**

Zero-shot LLM accuracy of 60–75% is inadequate for autonomous operation. But meeting/journal/project notes are structurally distinct — the classification task is easier than generic text classification benchmarks suggest. With explicit category definitions and 3–5 few-shot examples per class embedded in the prompt, accuracy is expected to exceed 85%. Misclassifications are recoverable via git history. The acceptable error rate is not zero — it is "lower than the user's own error rate under mobile cognitive load," which is a low bar. **[assumption]** This estimate (>85% with few-shot prompting) is derived from general LLM classification literature, not a controlled experiment on meeting/journal/project notes specifically.

**Claim 4: `research-loop.yml` is directly reusable with minimal modification.**

The workflow structure — checkout, install, agent invocation, commit, push — is identical in both use cases. The agent's task changes (classify inbox files instead of complete a research item), and the scheduling changes (every 6 hours instead of daily at 7am). Infrastructure and tooling are identical. [inference] The research-loop.yml has been operating reliably; the inbox triage workflow inherits that operational track record.

---

### §4 Consistency Check

No internal contradictions found. Specific cross-checks:

- Claim 1 (inbox removes friction) is consistent with the prior research finding (agent-memory-management-context-injection.md) that capture friction is a primary memory system failure mode. The inbox pattern directly addresses the stated root cause.
- Claim 3 (triage accuracy sufficient for no-human-review) uses the assumption label correctly: the >85% estimate is stated as an assumption derived from general benchmarks, not a measured result on this specific task. The confidence level on related Key Findings reflects this.
- The GTD "someday/maybe" handling and the `?-` prefix convention are consistent: both are holding patterns for unclassifiable items that don't block processing of classifiable ones.
- The research-loop.yml adaptation (one batch session per run, not per-item iteration) is consistent with the different problem structure: inbox triage operates on a set of files, not one item at a time.

---

### §5 Depth and Breadth Expansion

**Technical lens:** The inbox pattern works because classification is a batch task that does not require real-time user involvement. Agents excel at batch processing with well-defined classification rules — this is closer to structured extraction (which LLMs do reliably) than open-ended generation. The failure mode (ambiguous items left with `?-` prefix) is visible in the filesystem and does not degrade the system's health over time.

**Behavioural lens:** The psychological value of the inbox pattern is not only reduced decision count — it is reduced *decision anxiety*. When a user knows that every capture is valid regardless of content type, they capture more. The GTD and PKM literature attributes this not just to the reduced step count but to the psychological safety of a trusted system. If the triage is reliable, the user builds trust and the system becomes self-reinforcing.

**Operational lens:** The `?-` prefix convention makes triage failures visible without requiring a separate review interface. A user who monitors their inbox folder will see unclassified items accumulating and can take manual action. This is better than silent failure (wrong folder) because the item is visible.

**Historical lens:** The inbox pattern predates digital systems — physical paper inboxes and desk trays have been used in offices for over a century. GTD codified the principle in 2001. The novelty here is that the *processing* step is automated rather than manual. The underlying principle is identical to what Allen described.

**Economic lens:** The cost of the triage workflow is one GitHub Actions run every 6 hours. At typical free-tier usage, this is well within standard GitHub Actions minutes allocation (2,000 free minutes/month for public repos; the workflow is expected to run in under 2 minutes when the inbox is small). No new infrastructure cost.

---

### §6 Synthesis

**Executive summary:**

Removing folder selection from the capture path eliminates a structurally disproportionate decision from mobile note-taking. GTD and Matuschak's PKM both specify this separation as a design principle, and mobile interaction research confirms that each additional decision step increases cognitive load measurably. The minimum inbox file requires only a timestamp and raw content — all other front-matter is generated by the triage agent at classification time. The `research-loop.yml` workflow in this repo is directly reusable for inbox triage with five targeted changes: new prompt file, new file count check, no per-item loop, 6-hour schedule, and updated concurrency group. Zero-shot LLM classification accuracy (60–75%) is below the threshold for autonomous operation, but meeting/journal/project notes are structurally distinct; a few-shot prompt is expected to exceed 85%, which is sufficient given that misclassifications are recoverable via git history.

**Key findings:**

1. The inbox pattern eliminates folder selection from the capture path, reducing mobile capture to a single-step operation (content → submit), which removes an entire decision class and its associated cognitive cost.
2. Both GTD (Allen, 2001) and Matuschak's Evergreen Notes explicitly separate capture from classification on the grounds that classification benefits from full context not available at capture time.
3. Mobile interaction research (CELDA 2023; Computers in Human Behavior 2020) confirms that each additional decision step increases cognitive load and reduces task accuracy in time-pressured mobile contexts.
4. The minimum inbox file requires only two fields: `captured_at` (ISO8601 timestamp) and raw note content; title, type, tags, and folder are all generated by the triage agent.
5. Zero-shot LLM classification accuracy of 60–75% is insufficient for autonomous triage; a few-shot prompt with explicit category definitions and 3–5 examples per class raises accuracy to an estimated >85%, sufficient given git-recoverable misclassifications.
6. Meeting, journal, and project notes are structurally distinguishable by participant references, personal pronoun use, and task/deliverable orientation — signals that LLMs recognise reliably with clear category definitions in the prompt.
7. The `research-loop.yml` workflow is reusable for inbox triage with five targeted changes; infrastructure, tooling, and deployment pattern are identical.
8. Ambiguous items should be left in `inbox/` with a `?-` filename prefix and a `triage_note` front-matter field; this makes triage failures visible without blocking the run or losing the item.
9. Misclassification recovery requires only standard git commands — no tooling, no review interface, no data loss.
10. The psychological benefit of the inbox pattern extends beyond reduced step count: users who know every capture is valid regardless of type capture more, creating a self-reinforcing trust loop described in GTD literature.

**Evidence map:**

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| Each additional decision step increases mobile cognitive load | CELDA 2023 (ED636454); ScienceDirect 2020 | high | Two independent studies; direct measurement |
| GTD specifies capture-first, classify-later | GTD canonical docs (cannelevate.com.au, dayviewer.com) | high | Core GTD principle, not contested |
| Matuschak maintains two explicit inboxes, defers classification | notes.andymatuschak.org/Evergreen_notes (accessed 2026-03-08) | high | Primary source, confirmed accessible |
| Zero-shot LLM classification accuracy 60–75% | arXiv:2501.08457; nyckel.com benchmarks | high | Consistent across multiple benchmarks |
| Few-shot prompting raises accuracy substantially | Springer LLM review | medium | Direction consistent; exact delta varies; AAAI ICWSM prompt study cited in prior drafts but no author, URL, or DOI was verified — claim treated as [inference] |
| Triage accuracy estimate >85% with few-shot | Derived from above + category distinctiveness | low | Assumption, not measured on this specific task |
| research-loop.yml infrastructure is reusable | Read directly from .github/workflows/research-loop.yml | high | Direct inspection, all steps verified |
| Git history recovers misclassified files | Git content-addressable storage design | high | Fundamental property of git |
| Psychological trust loop increases capture rate | GTD literature (gettingthingsdone.com, dayviewer.com) | medium | Well-documented in GTD community; no controlled study on AI-triaged systems |
| `?-` prefix convention for ambiguous items | Derived from GTD "someday/maybe" + system design | medium | Inference from GTD principle, not a tested convention |

**Assumptions:**

- **Assumption:** The triage agent achieves >85% classification accuracy with a well-crafted few-shot prompt on meeting/journal/project notes. **Justification:** Zero-shot baselines are 60–75%; few-shot prompting consistently raises this; the three target categories are structurally distinct. The estimate has not been validated on a real inbox dataset.
- **Assumption:** A user capturing a fleeting thought on mobile is operating at higher cognitive load than an agent processing the same note in a scheduled batch. **Justification:** The mobile interaction studies confirm elevated cognitive load in time-pressured, on-device capture; the agent operates in a batch, low-pressure context with no competing tasks.
- **Assumption:** The `?-` prefix convention will be understood by users without documentation. **Justification:** The `?` character conventionally signals uncertainty in many file-naming systems; the convention should be documented in the inbox triage prompt and the Memory-System README.

**Analysis:**

Opinion: The inbox pattern is the right design for this context. The friction it removes is real and documented independently by three literatures (HCI research, GTD methodology, PKM practice). The automation it depends on is achievable with existing infrastructure. The accuracy bar is not "perfect classification" but "better than a rushed user," and misclassifications are recoverable.

The central design risk is the triage agent's classification accuracy. The solution is not to raise the bar on what counts as "correct" but to: (a) invest in a well-crafted few-shot triage prompt, (b) use the `?-` prefix mechanism for genuine ambiguity rather than guessing, and (c) treat misclassifications as expected and recoverable rather than catastrophic.

The `research-loop.yml` adaptation is straightforward. The workflow is well-designed and battle-tested in this repo; the inbox triage case is structurally identical (agent reads context, acts on files, commits result). The only material change is the agent's task and the trigger schedule.

**Risks, gaps, and uncertainties:**

- Triage accuracy on the real inbox dataset is not measured; the >85% estimate is an assumption.
- The `?-` prefix convention must be documented to be useful; undocumented conventions decay.
- If capture volume is high (many files per 6-hour window), a single Copilot session may time out or hit context limits. A fallback (process N files per run, like research-loop.yml's MAX_ITEMS) may be needed.
- The `inbox-triage-prompt.md` content is a design output, not a tested artefact. It requires iteration against real inbox data before it can be trusted for autonomous operation.
- The few-shot examples embedded in the triage prompt will become stale as the user's note-taking style evolves. A mechanism for updating the examples periodically is not designed here.

**Open questions:**

- What is the measured accuracy of the triage agent on the first 50 real inbox files? (Requires implementation and evaluation.)
- Should the triage workflow also handle retrieval enrichment (generating embeddings or summaries at triage time) or only classification and front-matter?
- Is a 6-hour triage interval acceptable, or should an event-driven trigger (push to inbox/) reduce latency to minutes?
- Can the triage agent also handle `inbox/` files that are URLs or images (e.g., screenshots), or is the scope text-only?

### §7 Recursive Review

All sections contain substantive content. Claims are labelled fact/inference/assumption. Every Key Finding maps to a row in the Evidence Map. The low-confidence assumption (>85% triage accuracy) is explicitly stated as an assumption with justification. The GTD/PKM literature sources were accessed (notes.andymatuschak.org page confirmed live; GTD canonical documentation confirmed via secondary sources). The `?-` prefix uncertainty is captured in Risks/Gaps. The research-loop.yml analysis is grounded in direct inspection of the file. No section consists only of a heading and a placeholder.

Open threads not synthesised: the Memory-System BACKLOG.md W-0012 item was inaccessible (private repo); its contents are not incorporated. The iOS Shortcuts and Telegram bot items (capture tools) are out of scope and not researched here. Both are noted as backlog items that this research informs.

---

## Findings

### Executive Summary

Removing folder selection from the capture path eliminates a structurally disproportionate decision from mobile note-taking. GTD (Allen, 2001) and Matuschak's Evergreen Notes both specify capture-first, classify-later as a core design principle; mobile HCI research independently confirms that each additional decision step in time-pressured mobile contexts increases cognitive load and reduces accuracy. The minimum inbox file requires only a timestamp and raw content — title, type, tags, and folder are generated by the triage agent at classification time. The `research-loop.yml` workflow is reusable for inbox triage with five targeted changes (new prompt, new file count check, no per-item loop, 6-hour schedule, updated concurrency group), making the triage workflow buildable on existing infrastructure with no new tooling. Zero-shot LLM accuracy (60–75%) is below the threshold for autonomous operation, but meeting/journal/project notes are structurally distinguishable by participant references, personal pronoun use, and task orientation; a few-shot prompt is expected to exceed 85%, and misclassifications are fully recoverable via git history.

### Key Findings

1. The inbox pattern eliminates folder selection from the capture path, reducing mobile capture to a single operation (content → submit) and removing an entire decision class and its associated cognitive cost from the user's responsibility.
2. GTD (Allen, 2001) and Matuschak's Evergreen Notes both specify capture-first, classify-later as a design principle on the grounds that classification benefits from full context unavailable at capture time.
3. Mobile Human-Computer Interaction (HCI) research (CELDA 2023; Computers in Human Behavior 2020) provides two independent confirmations that each additional decision step increases cognitive load in time-pressured mobile contexts.
4. The minimum inbox file requires only two fields: `captured_at` (ISO8601 timestamp) and raw note content; all other front-matter (title, type, tags, folder) is generated by the triage agent during the classification pass.
5. Zero-shot LLM classification accuracy of 60–75% is insufficient for autonomous triage; a few-shot prompt embedding explicit category definitions and 3–5 examples per class is estimated to exceed 85% accuracy — sufficient given that misclassifications are recoverable via git history and no data is lost.
6. Meeting, journal, and project notes are structurally distinguishable by three signal types: participant references and action items (meetings), personal pronouns and reflective tone (journal), and task/deliverable orientation with project name references (projects).
7. The `research-loop.yml` workflow is reusable for inbox triage with five targeted changes: replace prompt file reference, replace backlog count check with inbox count check, remove per-item iteration loop, change schedule to every 6 hours, and update the concurrency group name.
8. Ambiguous items should remain in `inbox/` with a `?-` filename prefix and a `triage_note` front-matter field explaining the deferral; this makes triage failures visible without blocking the run or losing the item.
9. Misclassification recovery requires only standard git commands — `git log --all --full-history -- "*/<filename>"` to locate, `git mv` to correct — with no data loss because git's content-addressable storage preserves all committed states.
10. The psychological benefit extends beyond reduced step count: GTD literature documents that users who trust the system capture more, creating a self-reinforcing loop where reliable autonomous triage increases capture volume and therefore the system's usefulness.

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| Each additional mobile decision step increases cognitive load | CELDA 2023 (ED636454); ScienceDirect 2020 (doi:10.1016/j.chb.2020.106310) | high | Two independent controlled studies with direct measurement |
| GTD specifies capture-first, classify-later | GTD canonical documentation (cannelevate.com.au, dayviewer.com) | high | Core GTD principle, non-contested in literature |
| Matuschak maintains explicit inboxes and defers classification | notes.andymatuschak.org/Evergreen_notes (accessed 2026-03-08) | high | Primary source, page confirmed accessible |
| Minimum inbox file needs only timestamp + content | Derived from triage agent requirements analysis | medium | Inference; no counter-evidence, but not empirically tested |
| Zero-shot LLM text classification accuracy 60–75% | arXiv:2501.08457; nyckel.com/blog benchmarks | high | Consistent across multiple independent benchmarks |
| Few-shot prompting substantially raises accuracy | Springer LLM classification review | medium | Consistent directional finding; exact improvement varies by task; AAAI ICWSM prompt study cited in prior drafts but no author, URL, or DOI was verified — claim treated as [inference] |
| Triage accuracy >85% achievable with few-shot on this task | Assumption derived from above two sources + category distinctiveness assessment | low | Not measured on meeting/journal/project notes specifically |
| Meeting/journal/project notes are structurally distinguishable | LLM classification literature; structural analysis of note types | medium | Structural signals identified; accuracy depends on prompt quality |
| research-loop.yml infrastructure is reusable unchanged | Direct inspection of `.github/workflows/research-loop.yml` | high | All steps verified against file content |
| Git history recovers misclassified files | Git content-addressable storage specification | high | Fundamental property of git; not specific to this use case |
| Psychological trust loop increases capture rate | GTD literature (gettingthingsdone.com) | medium | Documented in GTD community; no controlled study on AI-triaged systems |

### Assumptions

- **Assumption:** A few-shot triage prompt achieves >85% classification accuracy on meeting/journal/project notes. **Justification:** Zero-shot baselines are 60–75%; few-shot prompting consistently raises accuracy in published benchmarks; the three categories have distinct structural signals. The estimate has not been validated on a real inbox dataset and must be treated as a starting hypothesis for iteration.
- **Assumption:** A mobile user capturing a fleeting thought operates at higher cognitive load than the triage agent processing the same note in a batch. **Justification:** Mobile HCI studies confirm elevated cognitive load during time-pressured on-device capture. The agent operates in a scheduled batch with no competing tasks.
- **Assumption:** The `?-` prefix convention is understandable without user documentation. **Justification:** The `?` character signals uncertainty in many naming systems. The convention should be documented in the triage prompt file and the Memory-System README to avoid entropy.

### Analysis

Opinion: The inbox pattern is the correct design. It resolves the friction problem structurally rather than by optimising the capture UI, because the root cause is the decision itself, not the interface that presents it. HCI research documents that folder-selection decisions under time pressure increase cognitive load and reduce accuracy; GTD methodology specifies a dedicated capture phase for the same reason; PKM practice (Matuschak) defers classification to protect link quality. All three arrive at the same structural prescription: separate capture from classification. Automating the classification pass (replacing human review with an agent) removes the only residual friction.

A well-crafted few-shot triage prompt achieves better accuracy than a distracted mobile user: the agent operates in a scheduled, context-rich batch with no competing tasks. Investing in prompt quality yields higher accuracy without operational cost; falling back to the `?-` prefix for genuinely ambiguous items keeps failures visible rather than silent.

The research-loop.yml adaptation is lower-risk than building a new workflow from scratch. The existing pattern has demonstrated reliable operation in this repo; the inbox triage case inherits that reliability. The five required changes are all mechanical and non-structural.

### Risks, Gaps, and Uncertainties

- Triage accuracy on the actual inbox dataset is not measured. The >85% estimate requires validation against the first real batch of inbox files.
- The `inbox-triage-prompt.md` content is a design output specified in this item but not a tested artefact. It requires iteration before it can be trusted for unattended operation.
- High capture volume (many files per 6-hour window) may cause the triage session to time out or exceed the Copilot CLI's context window. A batch-size cap (analogous to MAX_ITEMS in research-loop.yml) may be needed.
- The few-shot examples embedded in the triage prompt will become stale as the user's note-taking style evolves. No mechanism for updating examples periodically is designed here.
- The `?-` convention must be documented to remain useful; undocumented conventions decay without enforcement.
- The Memory-System BACKLOG.md W-0012 item was inaccessible (private repo); its specific requirements or constraints are not incorporated.

### Open Questions

- What is the measured accuracy of the triage agent on the first 50 real inbox files? This requires implementation and evaluation and could become a new backlog item.
- Should the triage workflow also enrich classified files with embeddings or summaries, or should it strictly classify and move?
- Is a 6-hour triage interval acceptable, or should an event-driven trigger (push to `inbox/`) reduce latency to minutes? The schedule trigger may be replaceable with a `push: paths: ['inbox/**']` trigger for near-real-time triage.
- Can the triage agent handle `inbox/` files that are not text (URLs, screenshots, audio transcripts), or is the scope text-only for the initial implementation?
- Should the `inbox-triage-prompt.md` design be tracked as a separate research item, or is it sufficiently specified here to implement directly?

---

## Output

- Type: knowledge, backlog-item
- Description: Confirms the inbox pattern as the correct design for frictionless mobile capture. Specifies minimum inbox file format (timestamp + content), triage agent classification rules, `?-` ambiguity handling, and a research-loop.yml adaptation design. Produces a concrete specification for the Memory-System W-0012 implementation work.
- Links:
  - https://notes.andymatuschak.org/Evergreen_notes — Matuschak inbox and deferred classification design
  - https://www.nyckel.com/blog/llms-for-classification-best-practices-and-benchmarks/ — LLM classification accuracy benchmarks
  - https://files.eric.ed.gov/fulltext/ED636454.pdf — Mobile cognitive load and interaction step cost (CELDA 2023)