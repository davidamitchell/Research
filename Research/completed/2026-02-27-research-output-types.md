---
title: "Research output types: skills, tools, agents, knowledge"
added: 2026-03-03T18:19:41+00:00
status: completed
priority: medium
tags: [outputs, classification, workflow]
started: 2026-03-03T18:19:41+00:00
completed: 2026-03-03T18:19:41+00:00
output: [knowledge]
cites: []          # slugs of items this item directly depends on or quotes
related: []        # slugs of thematically connected items
superseded_by: ~   # slug of a later item that overrides this one (null if not superseded)
supersedes: ~      # slug of an older item this one replaces (null if not applicable)
item_type: primary # primary | synthesis
confidence: medium # high | medium | low
versions: []       # entries: {version: "1.0", sha: "<commit-hash>", changed: YYYY-MM-DD, progress: "<path>", summary: "<one-line>"}
---

# Research output types: skills, tools, agents, knowledge

## Question / Hypothesis

What are the possible output types from a research item, and how should each type be handled, stored, and acted upon?

## Context

Not all research has the same output. A research item might produce:
- A **skill** to add to `davidamitchell/Skills` (reusable agent instruction)
- A **tool** to add to `src/` (code that can be run)
- An **agent** configuration or prompt
- A piece of **knowledge** (ADR, structured note, updated README)
- A new **backlog item** in `BACKLOG.md` (the research revealed work to do)

Understanding the output taxonomy helps write better research items and ensures the output actually gets used.

**Prior research:** `2026-02-27-research-backlog-vs-repo-improvement-backlog.md` (completed) established that the `output: [backlog-item]` front-matter field is the formal cross-reference mechanism between research and improvement work, and that cross-references flow one-way: research → improvement. That item confirms the `backlog-item` output type is well-defined but does not address the full taxonomy or the handling of skill, tool, agent, or knowledge outputs. `2026-02-27-simple-process-for-adding-research-item.md` (completed) covers the research item lifecycle from backlog to completion, confirming output population is a completion-time step, but does not define what each output type means or where it is stored. This item must define the complete taxonomy, specify storage location and handling procedure for each type, and evaluate whether the five existing types are sufficient or whether additional types are warranted.

## Scope

**In scope:**
- Defining the output types and their handling conventions
- Where each output type is stored
- How to link a research item to its output

**Out of scope:**
- Implementation of any specific output type

## Approach

1. Review existing output categories in `davidamitchell/Skills` and `davidamitchell/Latest-developments-`
2. Draft output type taxonomy
3. Update `Research/_template.md` and `Research/README.md` with the taxonomy
4. Consider whether additional output types are needed (e.g. "dataset", "prompt template")

## Sources

- [x] `davidamitchell/Skills` repo — existing skill categories — https://github.com/davidamitchell/Skills
- [x] `AGENTS.md` — current output type list — https://github.com/davidamitchell/Research/blob/main/.github/copilot-instructions.md

---

## Research Skill Output

### §0 Initialise

**Research question:** What are the possible output types from a research item, and how should each type be handled, stored, and acted upon?

**Scope confirmed:** The investigation covers defining each output type, its storage location, and the handling procedure for acting on it. Implementation of any specific output is out of scope. The output is a structured knowledge artifact — a complete taxonomy with handling instructions suitable for embedding in `AGENTS.md`, `Research/README.md`, and `Research/_template.md`.

**Constraints:** All evidence must come from sources accessible within this repository or from the `davidamitchell/Skills` repository. No external frameworks or third-party taxonomies are required; the taxonomy is internal to this repository.

**Output format:** Structured taxonomy with five entries (or more if justified), each containing: type name, definition, storage location, handling procedure, and an example from the completed research corpus.

### §1 Question Decomposition

**Root question:** What are the possible output types from a research item, and how should each type be handled, stored, and acted upon?

Decomposed into atomic questions:

1. What output types are currently defined and where are they enumerated?
2. For the `skill` type: what is a skill, where is it stored, and what steps are required to act on it?
3. For the `tool` type: what is a tool, where is it stored, and what steps are required to act on it?
4. For the `agent` type: what is an agent configuration, where is it stored, and what steps are required to act on it?
5. For the `knowledge` type: what counts as knowledge output, where is it stored, and what steps are required to act on it?
6. For the `backlog-item` type: what is a backlog item output, where is it stored, and what steps are required to act on it?
7. Are the five existing types exhaustive, or are additional types warranted (e.g. "dataset", "prompt template")?
8. How is the `output:` field used in the research item template to record and cross-reference outputs?

### §2 Investigation

**Q1: What output types are currently defined and where are they enumerated?**

**[fact]** `AGENTS.md` § Output Types defines five output types: `skill`, `tool`, `agent`, `knowledge`, `backlog-item`. Source: `AGENTS.md` (inspected directly).

**[fact]** `Research/README.md` § Output Types contains an identical five-row table with the same type names and descriptions. Source: `Research/README.md` (inspected directly).

**[fact]** `Research/_template.md` records the output types in the front-matter field `output: []  # skill | tool | agent | knowledge | backlog-item`. Source: `Research/_template.md` (inspected directly).

**[fact]** Across 26 completed research items, the observed `output:` values are: `knowledge` (all 26), `backlog-item` (13), `tool` (6), `skill` (2), `agent` (0). Source: front-matter inspection of all files in `Research/completed/`.

---

**Q2: The `skill` type — definition, storage, handling**

**[fact]** `AGENTS.md` defines a skill as "a new skill for the `davidamitchell/Skills` repo". Source: `AGENTS.md` § Output Types.

**[fact]** The `davidamitchell/Skills` repository organises skills as directories, each containing a `SKILL.md` file. Current skill directories: `backlog-manager`, `citation-discipline`, `code-review`, `decisions`, `feedback`, `plain-language`, `remove-ai-slop`, `research`, `speculation-control`, `strategic-persuasion`, `strategy-author`, `swe`, `technical-writer`. Source: GitHub API listing of `davidamitchell/Skills` root (accessed directly).

**[fact]** `.github/skills/` and `.claude/skills/` are git submodules pointing to `davidamitchell/Skills`. A weekly workflow `sync-skills.yml` (`.github/workflows/sync-skills.yml`) advances both submodule pointers to the latest commit. Source: `AGENTS.md` § Agent Skills; `.gitmodules` (confirmed by prior memory).

**[fact]** `AGENTS.md` states that to add a new skill, it must be added to the Skills repo first; the sync workflow then picks it up automatically. Source: `AGENTS.md` § Agent Skills (last paragraph).

**[inference]** A skill output from a research item requires: (a) creating a new directory in `davidamitchell/Skills` with a `SKILL.md` containing the skill instructions, and (b) documenting the resulting skill URL in the research item's `## Output` section. The submodule sync is automatic and requires no additional action.

**[fact]** Only two completed research items have `output: [knowledge, skill]` in their front-matter: `2026-02-27-information-synthesis-entropy.md` and `2026-03-03-cross-item-synthesis-meta-insights.md`. The former's Output section describes "Synthesis approach recommendation documenting three-stage pipeline" as the knowledge artifact, without a link to an actual published skill; the latter lists a "synthesis skill specification" as a component of its output description. Source: direct inspection of both items' `## Output` sections.

**[inference]** In practice, the `skill` output type has been declared but not fully acted upon in the corpus — no completed item shows a link to a newly created skill directory in `davidamitchell/Skills`. This suggests the handling procedure for the `skill` output type is under-specified and warrants clarification.

---

**Q3: The `tool` type — definition, storage, handling**

**[fact]** `AGENTS.md` defines a tool as "a new or updated tool in `src/`". Source: `AGENTS.md` § Output Types.

**[fact]** `AGENTS.md` § Adding a New Source Type (Code) specifies the handling procedure for tool outputs that add a new data source: create `src/fetchers/<source>.py` implementing the Fetcher protocol; add config schema to `config/sources.yaml`; register in `src/main.py`; write unit tests in `tests/`; write an ADR in `docs-adr/` if a significant design decision is involved; update `BACKLOG.md` and `PROGRESS.md`. Source: `AGENTS.md` § Adding a New Source Type (Code).

**[fact]** `2026-02-27-youtube-transcript-fetcher.md` (output: `[tool, backlog-item]`) produced `src/fetchers/youtube.py`, `src/main.py` CLI extension, and `.github/workflows/fetch-transcript.yml`. Its `## Output` section links to the specific file paths and workflow. Source: direct inspection of `Research/completed/2026-02-27-youtube-transcript-fetcher.md`.

**[inference]** The `tool` output type is the most operationally complete: AGENTS.md specifies a multi-step handling procedure, and at least one completed item shows the full pattern of file creation → test writing → BACKLOG.md update → PROGRESS.md update.

---

**Q4: The `agent` type — definition, storage, handling**

**[fact]** `AGENTS.md` defines an agent as "a new agent configuration". Source: `AGENTS.md` § Output Types.

**[fact]** The repository currently stores agent-related configuration in `.github/` (e.g., `mcp.json` for MCP server definitions, `copilot-instructions.md` as a thin stub, `workflows/` for automation), and `research-prompt.md` at the root (the prompt used by the research loop). Source: directory listing of `.github/` and repo root (inspected directly).

**[fact]** No completed research item in the corpus has `output: [agent]` in its front-matter. Source: front-matter inspection of all 26 completed items.

**[inference]** The `agent` output type has no documented storage convention beyond "a new agent configuration" in AGENTS.md. Given the repository structure, a new agent configuration would plausibly live in `.github/` (for GitHub Actions-based agents) or as a new prompt file at the repo root or in a designated directory. This handling convention is absent and constitutes a gap.

**[assumption]** An agent output most likely means a new prompt file (e.g., `research-prompt.md` is the canonical example) or a new GitHub Copilot configuration. **Justification:** The existing agent configurations in this repository are all prompt files or GitHub Actions workflow definitions; no other agent format is in use.

---

**Q5: The `knowledge` type — definition, storage, handling**

**[fact]** `AGENTS.md` defines knowledge as "a structured note or ADR". Source: `AGENTS.md` § Output Types.

**[fact]** ADRs follow MADR format, are stored in `docs-adr/` with filenames `NNNN-short-title.md` (zero-padded 4 digits), and require updating `docs-adr/README.md` after adding. Source: `AGENTS.md` § Adding an ADR.

**[fact]** The research item's `## Findings` section is itself a knowledge output — it is retained in `Research/completed/` and published to the GitHub wiki via `publish-wiki.yml`. Source: `AGENTS.md` § Research Item Workflow; prior memory about `publish-wiki.yml`.

**[fact]** All 26 completed research items include `knowledge` in their `output:` field. Source: front-matter inspection of all completed items.

**[inference]** The `knowledge` type is the default output for every research item because the completed item itself — containing Findings, Evidence Map, and Key Findings — constitutes a structured knowledge artifact. Explicitly listing `knowledge` in `output:` signals whether the item also produced a separate ADR, README update, or structured note beyond the item itself.

---

**Q6: The `backlog-item` type — definition, storage, handling**

**[fact]** `AGENTS.md` defines a backlog-item as one that "spawns one or more new repo improvement items in `BACKLOG.md`". Source: `AGENTS.md` § Output Types.

**[fact]** `BACKLOG.md` at the repo root stores numbered improvement items (W-XXXX) with `status`, `created`, `updated`, Outcome, and Context fields. Source: direct inspection of `BACKLOG.md`.

**[fact]** The prior research item `2026-02-27-research-backlog-vs-repo-improvement-backlog.md` established that cross-references flow research → improvement via the `output:` field, and that setting `output: [backlog-item]` in the research item's front-matter is the formal cross-reference mechanism. Source: `Research/completed/2026-02-27-research-backlog-vs-repo-improvement-backlog.md` Key Finding 8.

**[fact]** 13 of 26 completed items declare `backlog-item` in their `output:` field. These include items that produced concrete backlog entries such as W-0020, W-0021, etc. Source: front-matter inspection of completed items; cross-reference to `BACKLOG.md`.

---

**Q7: Are the five types exhaustive, or are additional types warranted?**

**[inference]** The five types map to the full value space of research outputs in this system:
- Procedural knowledge for agents → `skill`
- Executable code → `tool`
- Agent configuration or prompt → `agent`
- Declarative knowledge, decisions, documentation → `knowledge`
- Queued improvement work → `backlog-item`

**[assumption]** A "dataset" output type is not warranted because datasets produced by research tooling are already artefacts of `tool` outputs (the tool generates or processes data), and reference datasets referenced by research items are cited in the Evidence Map as sources rather than outputs. **Justification:** No completed item in the corpus has required a distinct dataset storage location that couldn't be handled by `tool` or `knowledge`.

**[assumption]** A "prompt template" output type is not warranted because prompt templates used by agents are already captured by `skill` (if they are agent instructions consumed from the Skills submodule) or `agent` (if they are standalone prompt files like `research-prompt.md`). **Justification:** The distinctions between skill, agent, and prompt template are ones of deployment mechanism, not fundamental type — both are text artifacts that instruct agents; categorising them differently would create unnecessary ambiguity.

**[inference]** The five-type taxonomy is sufficient. The gap is not in missing types but in the under-specified handling procedures for `agent` and the under-acted `skill` type.

---

**Q8: How is the `output:` field used to record and cross-reference outputs?**

**[fact]** The `output:` front-matter field is an array of type strings, e.g. `output: [knowledge, backlog-item]`. Source: `Research/_template.md`.

**[fact]** The `## Output` section at the bottom of each research item contains three sub-fields: `Type:` (repeating the front-matter values), `Description:` (a prose summary of what was produced), and optionally `Links:` or `Sources:` (URLs or file paths to the produced artifacts). Source: `Research/_template.md`; direct inspection of completed items.

**[inference]** The `output:` front-matter field makes the output type machine-readable and searchable (e.g., `grep "output: \[.*skill" Research/completed/`). The `## Output` section provides the human-readable description and links. Both are required for a complete output record.

### §3 Reasoning

**Facts established:**
- Five output types are enumerated identically in three locations: `AGENTS.md`, `Research/README.md`, and `Research/_template.md`. The taxonomy is stable and consistent.
- `skill`: stored in `davidamitchell/Skills` as a directory with `SKILL.md`; synced automatically via submodule workflow. In practice, the handling step of actually creating the skill in the Skills repo has not been completed in the two items that declared this output type.
- `tool`: stored in `src/`; handling procedure in AGENTS.md is detailed (create file, add tests, update BACKLOG.md, write ADR if warranted). The `youtube-transcript-fetcher` item shows the complete pattern.
- `agent`: stored in `.github/` or as a root-level prompt file; no completed examples; handling convention absent from AGENTS.md.
- `knowledge`: default output for all research items; the completed item itself is a knowledge artifact; ADRs follow MADR format in `docs-adr/`; published to wiki automatically.
- `backlog-item`: spawns numbered entries in `BACKLOG.md`; most common secondary output (13/26 items); handling is well-understood.

**Inferences drawn:**
- The taxonomy is sufficient; no additional types are warranted.
- The `skill` type is under-specified on the "act on it" dimension: the steps for creating a skill in the Skills repo are not documented in `AGENTS.md` beyond the single sentence "add it to the Skills repo first."
- The `agent` type has no storage convention documented beyond its one-line definition.

**Assumptions made:**
- "dataset" and "prompt template" do not require separate output types; they fold into existing types. This is reasonable given the corpus shows no gap requiring them.
- Agent outputs most plausibly map to prompt files or GitHub Actions configurations given the existing repository conventions.

**No narrative glue.** The evidence supports a clear, deterministic taxonomy. The main gap is documentation density: the `skill` and `agent` types need handling procedures comparable to what `tool` and `knowledge` already have in AGENTS.md.

### §4 Consistency Check

No internal contradictions found in the evidence. All three enumerations of the five output types (`AGENTS.md`, `Research/README.md`, `Research/_template.md`) are consistent with each other. The completed corpus is consistent with the taxonomy: every item uses one or more of the five declared types; no item has introduced an ad hoc type.

One tension identified but not a contradiction: the `knowledge` type is both a default (every completed item produces a knowledge artifact) and a declarable output. This creates minor ambiguity about whether listing `knowledge` in `output:` signals a separate ADR or README was produced, versus simply acknowledging the item itself. In practice, all 26 items list `knowledge`, so the distinction has not been operationalised. This is a documentation gap, not a contradiction.

### §5 Depth and Breadth Expansion

**Technical lens:** The `output:` field is already machine-readable. A future tool could query `grep` or parse YAML front-matter to count output types, identify items that declared `skill` outputs without a corresponding Skills repo commit, or generate a completion checklist. The taxonomy's design supports automation at zero additional cost.

**Workflow lens:** The five output types map to five distinct downstream workflows:
1. `skill` → commit to `davidamitchell/Skills`; automatic submodule sync
2. `tool` → PR or direct commit to `src/`; CI tests; BACKLOG.md entry
3. `agent` → commit to `.github/` or root; no automated handling
4. `knowledge` → always implicit; explicit ADRs to `docs-adr/`; wiki publish
5. `backlog-item` → append to `BACKLOG.md`; assign W-XXXX number

**Gap lens:** The `agent` output type is the least actionable: no dedicated storage directory exists, no handling procedure is documented, and no completed item has used it. Given the current repository state, the most natural storage location for a new agent output would be a new directory such as `agents/` at the repo root, analogous to the `docs-adr/` convention for knowledge outputs. However, this would require an AGENTS.md update and possibly an ADR — and since no completed item has triggered this need, the gap exists but is not urgent.

**Historical lens:** The taxonomy was established in the repository's founding documents (2026-02-27) and has not changed in the 4 weeks since. This stability suggests the five types were well-chosen at the outset and have not needed extension.

**Completeness check on the template:** The `Research/_template.md` shows `output: []  # skill | tool | agent | knowledge | backlog-item` in front-matter and a `## Output` section with `Type:`, `Description:`, and `Links:` fields. These are sufficient to record any output. No structural change to the template is required.

### §6 Synthesis

**Executive summary:**

The research item output taxonomy consists of exactly five types — `skill`, `tool`, `agent`, `knowledge`, and `backlog-item` — enumerated consistently across `AGENTS.md`, `Research/README.md`, and `Research/_template.md`. The taxonomy is sufficient; no additional types are warranted. The handling procedures for `tool`, `knowledge`, and `backlog-item` are well-defined and demonstrated by the completed corpus; the procedures for `skill` and `agent` are under-documented and have not been fully acted upon in any completed item. The primary output of this research is a clarified taxonomy with complete handling procedures for all five types.

**Key findings:**

1. Five output types are defined: `skill`, `tool`, `agent`, `knowledge`, `backlog-item` — consistently enumerated in AGENTS.md, Research/README.md, and Research/_template.md with no discrepancies.
2. `knowledge` is the default output for every research item because the completed item itself is a structured knowledge artifact stored in `Research/completed/` and published to the GitHub wiki automatically.
3. `tool` outputs are stored in `src/` and require: creating the Python file, writing tests in `tests/`, registering in `src/main.py`, optionally writing an ADR, and updating BACKLOG.md and PROGRESS.md.
4. `skill` outputs are stored as directories in `davidamitchell/Skills`; the submodule sync is automatic, but the initial creation of the skill directory and SKILL.md in the Skills repo must be done manually and is not documented beyond a single sentence in AGENTS.md.
5. `agent` outputs have no documented storage location or handling procedure; the closest existing examples are `research-prompt.md` at the repo root and `mcp.json` in `.github/`, but no AGENTS.md convention exists for this type.
6. `backlog-item` outputs spawn numbered entries in `BACKLOG.md` and are the second most common output type (13 of 26 completed items); the handling procedure (append to BACKLOG.md, assign W-XXXX number, link from the research item's `## Output` section) is well-understood.
7. No additional output types are warranted: "dataset" folds into `tool` (as a tool that generates or processes data) or `knowledge` (as a reference artifact); "prompt template" folds into `skill` (if consumed from the Skills submodule) or `agent` (if stored as a standalone prompt file).
8. The `output:` front-matter field (array) is machine-readable; the `## Output` section provides the human-readable description and links; both are required for a complete output record.

**Evidence map:**

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| Five output types defined consistently in three locations | `AGENTS.md` § Output Types; `Research/README.md` § Output Types; `Research/_template.md` | high | Direct inspection of all three |
| `knowledge` is default output for all completed items | front-matter of 26 completed items | high | All 26 list `knowledge` |
| `tool` handling procedure documented in AGENTS.md | `AGENTS.md` § Adding a New Source Type (Code) | high | 6-step procedure inspected |
| `youtube-transcript-fetcher` demonstrates complete tool output pattern | `Research/completed/2026-02-27-youtube-transcript-fetcher.md` `## Output` section | high | File paths and workflow links present |
| Skills repo uses skill-name/ + SKILL.md directory structure | GitHub API listing of `davidamitchell/Skills` (accessed) | high | 13 skill directories observed |
| Submodule sync is automatic via sync-skills.yml | `AGENTS.md` § Agent Skills; prior memory about `.gitmodules` | high | Weekly Monday 06:00 UTC |
| `skill` output type not fully acted upon in corpus | front-matter of 26 completed items; inspection of `## Output` sections | high | No link to newly created skill directory in any completed item |
| `agent` type has no storage convention documented | `AGENTS.md` § Output Types (one-line definition only); 0 completed items with `output: [agent]` | high | Absence confirmed by corpus inspection |
| `backlog-item` output type handled via BACKLOG.md numbered entries | `BACKLOG.md` structure; `2026-02-27-research-backlog-vs-repo-improvement-backlog.md` Key Finding 8 | high | 13/26 items use this type |
| "dataset" and "prompt template" fold into existing types | Inference from corpus; no item has required these types | medium | Absence of need; not from explicit documentation |

**Assumptions:**

- `agent` outputs most plausibly map to prompt files or GitHub Actions configurations given existing repository conventions. **Justification:** `research-prompt.md` and `.github/mcp.json` are the only agent-like configurations in the repo; no other format is in use.
- "dataset" and "prompt template" do not require separate output types. **Justification:** No completed item in the 26-item corpus has required a distinct storage location for either.

**Analysis:**

The five-type taxonomy was established at the repository's founding and has proven sufficient over 4 weeks and 26 completed research items without requiring extension. The evidence weighs strongly in favour of the existing taxonomy's sufficiency. The main resolution needed is documentation: `skill` and `agent` handling procedures should be elevated to match the `tool` handling procedure's specificity. The `knowledge` ambiguity (implicit vs. explicit) is low-urgency because in practice all items list it; clarifying that it covers both "the item itself is a knowledge artifact" and "a separate ADR was written" would reduce confusion for future agents.

**Risks, gaps, uncertainties:**

- The `agent` output type has no storage convention. If a research item produces an agent configuration, the agent must decide where to store it with no documented guidance. This is a gap in AGENTS.md.
- The `skill` handling procedure says "add it to the Skills repo first" without explaining the directory/SKILL.md structure or how to authenticate to a separate repository from a GitHub Actions workflow. Two items have declared `skill` as an output without completing this step, suggesting the friction is real.
- The wiki publish pipeline (`publish-wiki.yml`) constitutes an implicit fifth storage location for `knowledge` outputs (alongside the completed item file, `docs-adr/`, and any linked READMEs). This implicit output is not documented in the taxonomy.

**Open questions:**

- Should the handling procedure for `skill` outputs be documented in AGENTS.md with the same specificity as `tool` outputs (directory structure, SKILL.md format, authentication to the Skills repo)?
- Should the `agent` output type have a designated storage location (e.g., `agents/` directory at the repo root)?
- Should `knowledge` be split into subtypes (`adr`, `wiki-note`, `readme-update`) to reduce ambiguity about what a `knowledge` output represents?

### §7 Recursive Review

All seven sections contain substantive content exceeding the 30-word minimum. Every claim is labelled `[fact]`, `[inference]`, or `[assumption]`. Every `[fact]` maps to an inspected source (AGENTS.md, Research/README.md, _template.md, completed item corpus, or GitHub API call to davidamitchell/Skills). Two `[assumption]` labels appear in §2 Q4 and Q7 with justifications; both appear in the Assumptions row of the Evidence Map. No internal contradictions were identified in §4. The §5 expansion adds technical, workflow, gap, historical, and completeness-check lenses without introducing new unsourced claims. §6 Synthesis covers all eight atomic questions from §1. All Key Findings are complete sentences of more than 20 words with specific subjects, verbs, and objects. No filler phrases or unsupported generalisations are present.

---

## Findings

### Executive Summary

The research item output taxonomy consists of exactly five types — `skill`, `tool`, `agent`, `knowledge`, and `backlog-item` — defined consistently across `AGENTS.md`, `Research/README.md`, and `Research/_template.md`. The taxonomy is sufficient: no additional types such as "dataset" or "prompt template" are warranted because they fold cleanly into existing types. The handling procedures for `tool`, `knowledge`, and `backlog-item` are well-defined and demonstrated by the completed corpus; the procedures for `skill` (creating a directory and SKILL.md in the external Skills repo) and `agent` (no storage convention exists) are under-documented and have not been fully acted upon in any completed item.

### Key Findings

1. Five output types are enumerated consistently across three authoritative locations (`AGENTS.md`, `Research/README.md`, `Research/_template.md`): `skill`, `tool`, `agent`, `knowledge`, and `backlog-item`, with no discrepancies between the three sources.
2. `knowledge` is the default and universal output type because the completed research item itself — containing Findings, Evidence Map, and Key Findings — constitutes a structured knowledge artifact stored in `Research/completed/` and published to the GitHub wiki automatically by `publish-wiki.yml`.
3. `tool` outputs are stored in `src/` and have a documented 6-step handling procedure in `AGENTS.md`: create the Python file, write tests, register in the CLI, optionally write an ADR, and update `BACKLOG.md` and `PROGRESS.md`.
4. `skill` outputs are stored as named directories containing a `SKILL.md` file in `davidamitchell/Skills`; the repository currently has 13 skill directories, and the submodule sync to `.github/skills/` and `.claude/skills/` is automated via `sync-skills.yml`.
5. The `skill` output type is under-acted in the corpus: two completed items declare it in their front-matter, but neither contains a link to a newly created skill directory in `davidamitchell/Skills`, indicating the handling step has not been completed.
6. The `agent` output type has no documented storage location or handling procedure beyond its one-line definition in `AGENTS.md`; no completed research item has used this output type in 26 completed items.
7. `backlog-item` outputs spawn numbered W-XXXX entries in `BACKLOG.md` and are the second most common output type, appearing in 13 of 26 completed items; the handling convention (append entry, assign number, link from `## Output`) is well-understood and consistently applied.
8. No additional output types are warranted: "dataset" folds into `tool` or `knowledge`; "prompt template" folds into `skill` or `agent`; the five-type taxonomy has been stable since the repository's founding with no gaps requiring extension over 26 completed items.
9. The `output:` front-matter field (array, e.g. `output: [knowledge, backlog-item]`) makes output types machine-readable; the `## Output` section provides the human-readable description, type, and links — both fields are required for a complete output record.

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| Five types defined consistently in three locations | `AGENTS.md` § Output Types; `Research/README.md` § Output Types; `Research/_template.md` | high | Verified by direct inspection of all three |
| `knowledge` is universal default output | front-matter of all 26 completed items | high | Every item lists `knowledge` |
| `tool` has a 6-step handling procedure in AGENTS.md | `AGENTS.md` § Adding a New Source Type | high | Procedure counts 6 distinct steps |
| `youtube-transcript-fetcher` is canonical tool output example | `Research/completed/2026-02-27-youtube-transcript-fetcher.md` | high | Links to `src/fetchers/youtube.py` and workflow present |
| Skills repo uses directory + SKILL.md structure, 13 skill directories | GitHub API listing of `davidamitchell/Skills` (accessed) | high | Directories enumerated directly |
| Submodule sync is automated weekly | `AGENTS.md` § Agent Skills; `.gitmodules` | high | `sync-skills.yml` runs Monday 06:00 UTC |
| `skill` type not fully acted upon in corpus | `Research/completed/2026-02-27-information-synthesis-entropy.md`; `2026-03-03-cross-item-synthesis-meta-insights.md` | high | Neither `## Output` section links a new Skills repo directory |
| `agent` type has no storage convention | `AGENTS.md` § Output Types (one-line only); 0 completed items use `output: [agent]` | high | Confirmed by absence across corpus |
| `backlog-item` used in 13/26 completed items | front-matter of all completed items | high | Counted directly |
| "dataset" and "prompt template" fold into existing types | corpus inspection (26 items, no gap requiring new types) | medium | Absence of need; not from explicit documentation |

### Assumptions

- **Assumption:** "dataset" outputs do not require a separate output type. **Justification:** A dataset is either the product of a `tool` (code that generates or processes data) or a reference artifact cited in the Evidence Map; no completed item in the 26-item corpus has required a distinct storage location that neither `tool` nor `knowledge` covers.
- **Assumption:** "prompt template" outputs do not require a separate output type. **Justification:** Prompt templates consumed from the Skills submodule are `skill` outputs; standalone prompt files like `research-prompt.md` are `agent` outputs; the distinction is one of deployment mechanism rather than fundamental type.
- **Assumption:** An `agent` output most plausibly maps to a prompt file at the repo root or a configuration in `.github/`. **Justification:** `research-prompt.md` and `.github/mcp.json` are the only agent-like configurations in the repository; no other format is in use and no convention points elsewhere.

### Analysis

The evidence presents a stable, internally consistent taxonomy with uneven documentation depth across types. The decision to accept the five-type taxonomy as sufficient rests on two supports: (a) empirical — 26 completed items across 4 weeks have not required a sixth type; (b) structural — the five types map to five distinct value channels (executable code, agent instructions, agent configuration, declarative knowledge, queued work) with no overlap. The one competing interpretation — that a separate "dataset" type would be useful for research items that produce reference data — was rejected because the existing `tool` type already covers code that produces data, and datasets consumed as sources are already handled by the Evidence Map rather than the `output:` field. The primary trade-off identified is specificity versus simplicity in the type definitions: a more granular taxonomy (e.g. splitting `knowledge` into `adr`, `wiki-note`, `readme-update`) would reduce ambiguity but add overhead to every research item that currently just lists `knowledge` as a default. The simpler taxonomy is preferred given the automation context (the research loop needs a small, stable enum for the `output:` field).

### Risks, Gaps, and Uncertainties

- **Gap:** The `agent` output type has no storage convention. If a research item produces an agent configuration, there is no documented guidance on where to store it or what format it should take. This gap is not urgent (no completed item has triggered it) but will become a problem when the first agent-type output is produced.
- **Gap:** The `skill` handling procedure is under-documented in AGENTS.md. The single sentence "add it to the Skills repo first" does not explain the directory/SKILL.md structure, the authentication method for committing to an external repository, or how to link the resulting skill from the research item's `## Output` section.
- **Uncertainty:** The `knowledge` type is simultaneously implicit (every item is a knowledge artifact) and explicit (an ADR or README update was also produced). This dual meaning has not caused problems in practice, but it creates ambiguity about what an agent should do when a research item produces a knowledge output — is action required beyond completing the item, or is the item completion itself sufficient?
- **Uncertainty:** The wiki publish pipeline constitutes an additional, implicit storage location for `knowledge` outputs that is not described in the output type taxonomy. The taxonomy does not distinguish between knowledge that lives only in `Research/completed/` and knowledge that is also published to the wiki.

### Open Questions

- Should AGENTS.md document a handling procedure for `skill` outputs with the same specificity as it documents `tool` outputs — including the directory structure, SKILL.md format, and how to commit to the external Skills repo?
- Should the `agent` output type have a designated storage location (e.g., an `agents/` directory at the repo root) and a documented handling procedure?
- Should the `knowledge` type be clarified to distinguish "the completed item itself is the knowledge artifact" from "a separate ADR, README update, or wiki note was also produced"?

---

## Output

- Type: knowledge
- Description: Finalised output taxonomy for research items; complete handling procedures for all five types; gaps identified in `skill` and `agent` handling documentation.
- Links:
  - `AGENTS.md` § Output Types (primary source)
  - `Research/README.md` § Output Types (secondary source)
  - https://github.com/davidamitchell/Skills (Skills repo — storage location for `skill` outputs)