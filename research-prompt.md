# Research Loop Prompt

You are a research agent working on the `davidamitchell/Research` repository.

Your task: complete **exactly one** research item.

---

## Pre-Selected Item

The item selection and setup have already been handled by the workflow.
Work on this item only:

{{ITEM_CONTEXT}}

Begin exactly at the step indicated in the **Action** line above. Do not
re-run earlier steps unless the Action explicitly says to.

---

## Steps

### 1. Read the item

Read the file at the path given above in full. Understand:
- The **Research Question** (what needs to be answered)
- The **Scope** (what is in/out)
- The **Approach** (sub-questions to investigate)
- The **Sources** (starting points -- check all of them)

**Prior research cross-reference (mandatory):** Apply the prior work check
defined in `.github/skills/research/SKILL.md §0`. Search `Research/completed/`
for related items before beginning §2 Investigation. If you cite prior completed
items in §0, Findings, or the Evidence Map, cite them with URL-backed links
rather than repository-relative file paths.
Before drafting Findings, and again during Step 6 self-review, repeat this scan
for adjacent completed items that materially qualify the same control surface or
failure mechanism, especially identity, access control, information
architecture, rate limiting, deployment pipelines, systems-capability debt, and
other governance surfaces your conclusions touch.

**Frontmatter fields to populate during research (set before committing):**

- `cites:` — after §2 Investigation, list the slugs (filename without `.md`) of
  any completed items this item directly depends on or quotes. Set during §6
  Synthesis when evidence from prior items is used.
- `related:` — list slugs of completed items that are thematically connected but
  not directly cited. Set during §6 Synthesis.
- `supersedes:` — if the new findings materially contradict or replace the
  conclusions of an existing completed item, set this to that item's slug and
  also update `superseded_by:` in the older item to this item's slug.
- `item_type:` — set to `synthesis` if the research question explicitly asks to
  integrate or compare findings across existing completed items; otherwise leave
  as `primary`.
- `confidence:` — set at §7 Recursive Review based on the overall evidence
  quality of the Key Findings:
  - `high` — all key findings supported by primary sources; no unresolved contradictions
  - `medium` — key findings supported by secondary sources or inference chains with low uncertainty
  - `low` — key findings rely on a single source, significant gaps remain, or multiple unresolved contradictions exist
- `versions:` — leave as `[]` on initial completion. Add a version entry
  (`version: "1.0"`, `sha: <commit hash>`, `changed: YYYY-MM-DD`,
  `progress: <session log path>`, `summary: "Initial completion"`) after the
  item is committed and you have the commit SHA.
- `tags:` — assign tags at §6 Synthesis. **Consult `docs/tag-vocabulary.md`
  and use only canonical forms.** Do not create tags that are near-synonyms of
  existing canonical tags. Use `agentic-ai` not `ai`; use `llm` not
  `large-language-model`; check the vocabulary table for all 20 canonical
  clusters before assigning tags.

### 2. Research the item -- follow the research skill in full

Open `.github/skills/research/SKILL.md` and run every section. Write the
complete output into the `## Research Skill Output` section of the item as you
go. **This output is retained verbatim in the completed item.**

**§0 Initialise:** Restate the research question. Confirm scope, constraints,
and output format. Write into `### §0 Initialise`.

**§1 Question Decomposition:** Recursively break the Approach sub-questions into
atomic questions -- each answerable with a single evidence-based claim. Write
the decomposition tree into `### §1 Question Decomposition`.

**§2 Investigation:** For each atomic question, run an iterative
evidence-gathering loop: gather sources, classify them (primary / secondary /
tertiary), extract claims, cross-verify across independent sources, identify
contradictions, update the evidence map. Use available web tools (`WebSearch`,
`WebFetch`, or `Bash` with curl) to check every source listed in the item and
follow leads they produce. Apply source-marking discipline as defined in
`.github/skills/research/SKILL.md §2 Source Marking`. Write into
`### §2 Investigation`.

**Evidence discipline:**
- Label every claim as **[fact]**, **[inference]**, or **[assumption]**.
- Every **[fact]** must map to a source. If a source is inaccessible, note it
  in Risks/Gaps.
- Source-access observations are workflow metadata, not evidence-backed facts.
  Record broken or blocked URLs in §2 as plain `Access note:` bullets written
  as metadata fragments, not full declarative sentences; do not cite
  inaccessible URLs as support for their own 404/403 outcomes.
- Treat every `Access note:` bullet and every failed-search note in §2 as
  claim-bearing prose for review purposes: add an explicit `[fact]`,
  `[inference]`, or `[assumption]` label if the note remains in visible text,
  and bind any evidence-backed conclusion to accessible sources rather than to
  the inaccessible URL itself.
- If an `Access note:` only reports what happened in this session, for example a
  blocked fetch, a broad search query that found nothing useful, or a manual
  source substitution decision, do **not** label it as `[fact]` using the
  substitute source alone. Either rewrite it as an `[assumption]` or pure
  metadata fragment, or delete it after updating `## Sources` to the working
  source.
- Do not carry execution-path statements such as "blocked in this runtime",
  "fetched via web search", or "direct page fetch failed" into Findings or
  Risks/Gaps. Rewrite them as source-qualification claims grounded in the
  accessible source itself, or omit them.
- Cross-source continuity or evolution statements such as "the position remains
  consistent", "this sharpens the earlier claim", or "this is not a reversal"
  are usually **[inference]**, not **[fact]**, unless a single cited source
  explicitly makes that comparison itself.
- **[inference]** = derived from evidence; **[assumption]** = not verified,
  state the justification.
- Evidence sufficiency: at least two independent credible sources agree, or a
  primary source is definitive.
- **Failed primary-source searches must be recorded explicitly in §2.** When a
  secondary source cites a paper, arXiv preprint, or DOI that you cannot
  locate, write a note directly in §2 stating the search query used and the
  outcome ("not found"). Do not silently absorb the gap into a lower confidence
  label alone -- the explicit record is required so Risks/Gaps can be populated
  accurately and reviewers can re-check the search.

**Output quality:** Apply the output quality rules defined in
`.github/skills/research/SKILL.md §6 Output Quality`.

**§3 Reasoning:** Remove narrative glue and unsupported generalisations. Write
into `### §3 Reasoning`.

**§4 Consistency Check:** Scan for internal contradictions and unsupported
leaps. Resolve or explicitly flag unresolvable contradictions. Write into
`### §4 Consistency Check`.

**§5 Depth and Breadth Expansion:** Re-evaluate findings through relevant lenses
(technical, regulatory, economic, historical, behavioural). Add any new
insights. Write into `### §5 Depth and Breadth Expansion`.

**§6 Synthesis:** Produce the structured synthesis output and write it into
`### §6 Synthesis` in the Research Skill Output section.

**§7 Recursive Review:** Validate that every section is justified, all threads
synthesised, every claim sourced or labelled, all uncertainties explicit.
Record the outcome in `### §7 Recursive Review`.

### 3. Seed the Findings section from §6

With `## Research Skill Output` complete, copy the §6 Synthesis content into
`## Findings` -- expanding each component into the full structured subsections.
No new claims may appear in Findings that are not already in the Research Skill
Output.
If you later edit Findings during review fixes, mirror the same substantive
change back into `§6 Synthesis` before proceeding so the two sections stay
aligned.

- **Executive Summary** -- 3-5 sentences. Direct answer to the research
  question. **The first sentence must state the answer as a specific,
  falsifiable claim -- not a restatement of the question, not a description of
  what the item covers, not a hedged "it depends." If the answer is genuinely
  uncertain, state the best-supported conclusion followed by the primary
  uncertainty.** State the key conclusion first. Write plain prose; do not
  prefix sentences with `[type; source:]` labels.
- **Key Findings** -- ordered list, 6-12 items. Each is a specific,
  evidence-backed claim with a confidence label and source as a trailing
  parenthetical. Format: `1. **Claim text as a complete sentence.** (high
  confidence; source: https://url1; https://url2)` **Each Key Finding must be
  a complete sentence of at least 20 words containing a subject, a verb, and a
  specific object or complement.** Do not include findings that are
  reformulations of the research question, findings that apply generically to
  all research items, or findings that consist only of a label without a claim.
- **Evidence Map** -- table: claim | source | confidence | notes. Every Key
  Finding must appear here. **The `source` cell in every row must contain one or
  more URL-backed citations or DOIs, not only source names or shorthand labels,
  so the row is independently verifiable on its own.**
- **Assumptions** -- each assumption and its justification. Must match
  **[assumption]** labels in §2 Investigation.
- **Analysis** -- how evidence was weighed, trade-offs identified, competing
  interpretations resolved.
- **Risks, Gaps, and Uncertainties** -- what is still unknown; where evidence
  is thin.
- **Open Questions** -- questions that surfaced but are out of scope; may become
  new backlog items.
- **Output section** -- type (`knowledge`), description, and links to the three
  most important sources. Treat the `Description` line as claim-bearing prose:
  if it makes a substantive claim, append a suffix epistemic label and
  URL-backed source just as you would in Executive Summary or Analysis.
- **Inline evidence discipline in Findings** -- every sentence in Findings that
  asserts a factual or inferential claim must bind its epistemic label and
  supporting source inline. Use the **suffix** (trailing) form:
  - **Executive Summary and Analysis:** plain prose sentences; each sentence
    that makes a claim ends with a trailing citation:
    `Claim text. [inference; source: https://url1; https://url2]`
  - **Key Findings:** confidence and source as a trailing parenthetical after
    the claim: `1. **Claim text.** (high confidence; source: https://url1)`
  Do not write labels **before** the claim text (prefix style such as
  `[inference; source: URL] Claim text.`). The Evidence Map is required, but it
  does **not** substitute for inline source binding in Executive Summary, Key
  Findings, or Analysis.

**Writing style:**
- Direct, declarative prose. State findings as facts or clearly labelled
  inferences.
- No filler phrases ("it is worth noting", "importantly", "it should be said",
  "in conclusion").
- No sycophantic transitions. Each section earns its content.

### 4. Companion skill checks

Apply all four companion skill pre-output checks defined in
`.github/skills/research/SKILL.md §8 Output Finalisation`. All four must pass
before proceeding. Fix any violations in the item before moving on.

In addition, apply the pre-output checklists from:
- `.github/skills/citation-discipline/SKILL.md` -- verifies all factual claims
  are bound to verifiable sources, acronyms are expanded, and no citation is a
  bare source name without a URL or DOI.
- `.github/skills/inline-citation/SKILL.md` -- verifies every citation in
  `## Findings` has a URL-backed source and that sources in the `## Sources`
  section use display names suitable for `Author (Year)` rendering on the
  generated site. Use the canonical display-name format
  `[Author et al. (YYYY) Title](https://url)` where an author and year are known,
  or `[Organisation Title](https://url)` where only an organisation name is
  available. These display names feed the inline citation labels shown on the
  generated GitHub Pages.

**Critical: acronym expansion audit (run inline -- do not defer to the skill
file).**
This is the most common citation-discipline failure. 19+ research reviews have
failed for this reason alone. Run it now, before Step 5:

1. List every acronym, initialism, and abbreviation used in
   `## Research Skill Output` and `## Findings`.
2. For **each one**, confirm it is expanded on its **first use in the entire
   document** -- not just in each section.
3. Format: `Full Name (ABBR)` at first use; `ABBR` alone thereafter.
4. These abbreviations have failed review most often -- check each one
   explicitly:

| Abbreviation | Required expansion on first use |
|---|---|
| LLM | Large Language Model (LLM) |
| API | Application Programming Interface (API) |
| CLI | Command Line Interface (CLI) |
| SDK | Software Development Kit (SDK) |
| PAT | Personal Access Token (PAT) |
| MCP | Model Context Protocol (MCP) |
| RAG | Retrieval-Augmented Generation (RAG) |
| CoT | chain-of-thought (CoT) |
| SRE | Site Reliability Engineering (SRE) |
| ITSM | IT Service Management (ITSM) |
| PaaS | Platform as a Service (PaaS) |
| MECE | Mutually Exclusive, Collectively Exhaustive (MECE) |
| PR | pull request (PR) |
| MBPP | Mostly Basic Python Problems (MBPP) |
| A/B | A/B test, or rewrite to plain language such as head-to-head comparison |

Also expand any domain-specific abbreviation introduced in this item's topic
area. Fix every violation before moving on.

### 5. Sense check

Re-read the completed item as a critical reader, not as its author. Apply all
four checks:

- **Logic** -- Are the conclusions actually supported by the evidence gathered?
  Could an informed reader challenge any causal link or inference?
- **Consistency** -- Do the numbers, dates, claims, and confidence levels agree
  across sections (§2, Key Findings, Evidence Map)? Do the conclusions align
  with what the sources actually say?
- **Reality** -- Does the overall picture match how the domain works in
  practice? Are there obvious real-world constraints, counterexamples, or
  mainstream positions that the item ignores or contradicts without explanation?
- **Clarity** -- Would a knowledgeable non-specialist understand the argument
  and reach the same conclusion? Are there unstated assumptions that a reader
  would need to fill in themselves?

If any check surfaces a problem, fix it before proceeding.

### 6. Self-review before draft commit

Before committing, run an inline self-review to catch the most common
violations. This avoids spending a full external review cycle on
easily-detectable issues.

**Check all of the following before proceeding:**

   1. **Acronym/abbreviation expansion** -- scan every section of
    `## Research Skill Output` and `## Findings`. List every abbreviation used.
    Confirm each is expanded at its **first occurrence in the entire document**
    (not per-section). The most commonly failed ones are: LLM, API, CLI, SDK,
    PAT, MCP, RAG, CoT, PDF, GPT, GPT-4, SRE, PR, ITSM, PINT, CVE, OWASP,
    MBPP, and A/B. Fix every unexpanded abbreviation before proceeding, and
    prefer rewriting comparison shorthand like `A/B` into plain language when
    possible.

1a. **Domain-term clarity** -- scan for non-self-evident shorthand such as
    "maturity ladder", "knowledge graph", "critic stack", "verifier stack",
    "human-in-the-loop", "graph database", "active recall", or "spaced
    repetition". On first use, either replace the shorthand with plain
    language or bind it to an authoritative definition source. Do not assume a
    reviewer will treat domain jargon as self-explanatory. The expansion or
    definition must appear in the audited prose itself on first use; placing it
    only in `## Sources` does not satisfy review.
    If you intentionally keep a coined or internal design label because no
    authoritative definition exists, mark the first occurrence explicitly as
    `Definition needed:` and explain the nearest evidence-backed functional
    equivalent rather than presenting the label as settled terminology.

2. **Claim labels** -- every factual or inferential claim in
    `## Research Skill Output` must carry a `[fact]`, `[inference]`, or
    `[assumption]` label. Headings and question decomposition sub-headings are
    exempt. Fix any unlabelled claims.

2a. **Findings inline labels and sources** -- every factual or inferential
    claim in `## Findings`, especially Executive Summary, Key Findings, and
    Analysis, must carry an inline `[fact]`, `[inference]`, or `[assumption]`
    label and bind its supporting source AFTER the claim text (suffix style).
    Use `Claim text. [inference; source: URL]` for prose and
    `1. **Claim text.** ([inference]; high confidence; source: URL)` for Key Findings.
    Prefix-style labels placed before the claim (such as
    `[inference; source: URL] Claim text.`) are non-conforming.
    The Evidence Map alone is insufficient.

2aa. **Synthesis/Findings parity** -- if any post-review fix changes wording,
     labels, confidence, or sources in `## Findings`, make the equivalent
     change in `§6 Synthesis` before proceeding. The two sections are mirrored
     outputs and must not diverge.


2b. **Context and Evidence Map audit** -- treat the `## Context` section and
    every Evidence Map row as claim-bearing prose, not as exempt scaffolding.
    Context sentences that assert factual or behavioral claims need inline
    labels and source binding, and every Evidence Map claim cell must begin
    with `[fact]`, `[inference]`, or `[assumption]`. Every Evidence Map
    **source** cell must also contain URL-backed citations or DOIs rather than
    bare source names. Evidence Map **notes** cells should stay short metadata
    fragments rather than evaluative sentences; if a note needs its own claim,
    move that claim into the labeled claim cell or Findings prose with source
    binding. If a seed video, transcript,
    or other listed source was inaccessible in this session, do **not** cite it
    as direct support for downstream factual claims in Findings; either remove
    the citation, downgrade the claim, or mark the dependency as an assumption.

2bb. **Synthesis-table audit** -- treat every table in `§6 Synthesis` and
    `## Findings`, not just the Evidence Map, as claim-bearing content. If a
    stage table, capability matrix, progression table, or assessment table
    contains proposed thresholds or design judgments, each row must make the
    epistemic status explicit, for example `[inference]` or `[assumption]`,
    and each row must carry direct supporting sources in the row itself, not
    only in surrounding prose. Do not leave synthesis tables as bare unlabeled
    fragments, because review treats unlabeled table cells as unsupported
    claims.

2c. **No self-referential citations** -- do not cite "this file", "self-audit",
    "investigation record", or similar internal phrases as sources in `§0`,
    `§7`, or `## Findings`. Every cited claim must bind to a verifiable URL or
    a pinpoint citation to an external standard, platform document, or prior
    completed research item with a GitHub URL. If a sentence is only describing
    the item's own structure or workflow state, either remove the citation need
    by rewriting it as pure metadata or cite the item's GitHub URL explicitly.
    `§7 Recursive Review` is audited the same way as the rest of `## Research Skill Output`:
    if you leave visible review-outcome sentences there, they need `[fact]`,
    `[inference]`, or `[assumption]` labels and either an explicit GitHub URL
     citation for the item or a rewrite into pure metadata fragments. Prefer the
     pure-metadata form by default; do not turn "audit completed" notes into
     sourced claims unless the audit result itself is the subject of evidence.

2c1. **§0 workflow-metadata claims** -- treat `§0` notes about output format,
    workflow constraints, or evidence-handling rules as internal workflow
    metadata, not as externally sourced facts. Do not attach outside URLs to
    sentences such as "Constraints confirmed" or "Output format confirmed"
    unless a cited source directly makes that exact claim. Rewrite these lines
    as pure metadata or `[assumption]` with a justification when they describe
    how this item will be handled rather than what the external evidence says.

2d. **Source substitution and surface coverage** -- if a seeded URL is dead,
    redirected away from the needed content, or replaced by a newer official
    page, update the entry in `## Sources` to the working official URL before
    drafting Findings. Do not cite replacement sources as proof that the old
    URL failed. For any architecture or operating-model claim that spans
    multiple control surfaces, confirm the cited sources directly support each
    named surface; otherwise narrow the claim, lower confidence, or add the
    missing source before proceeding.

2e. **Repository cross-reference sweep** -- for each Key Finding and Evidence
    Map row that touches a governance surface also covered elsewhere in
    `Research/completed/`, search for materially related completed items and
    cite the most relevant ones with URL-backed links. If adjacent completed
    work would sharpen, qualify, or offer a rival explanation for the claim,
    include it before drafting or revising Findings rather than waiting for the
    review workflow to surface the gap.

2f. **Confidence-evidence alignment for synthesis claims** -- if a Key Finding
    or Evidence Map row is supported mainly by same-repository companion-item
    syntheses, do **not** assign `high` confidence unless the claim also cites
    at least one independent primary source or credible external secondary
    source at the point of claim. Otherwise downgrade the confidence to
    `medium` or narrow the claim so the stronger confidence is actually earned.

2g. **Comparative-claim coverage** -- if a sentence compares two control
    surfaces, operating models, or investment choices, confirm the cited
    sources directly support **both** sides of the comparison. Evidence for
    only one side does not support the comparison by itself: either add the
    missing source, narrow the sentence to the supported half, or keep it as
    `[inference]` and lower confidence.
    Benchmark-ranking, "best benchmark," "most decision-useful," "stronger
    evidence," "leader," "laggard," "most popular," and similar comparative
    synthesis claims should default to `[inference]` unless a cited source
    itself makes that comparison directly. Do not treat benchmark design facts
    or score tables as if they automatically prove the evaluative judgment you
    derive from them.

2h. **Executive-summary clause coverage** -- if one Executive Summary sentence
    combines a conceptual or philosophical thesis claim with a present-day
    empirical, interpretability, or deployment claim, ensure the citation set
    directly supports **each clause**. Do not let a theory source carry a
    frontier-model evidence claim, and do not let a frontier-model source stand
    in for the original thesis statement.

3. **Vague quantifiers** -- check for unsourced "many", "most", "significant",
   "state-of-the-art". Replace with specific numbers or add a source, or
   qualify as `[inference]`.

4. **AI slop phrases** -- scan `## Findings` for: "Furthermore",
   "Additionally", "It is important to note", "In conclusion", "It is worth
   noting", "Importantly". Remove or rewrite each occurrence.

5. **Em-dashes** -- scan the entire document for `—` (U+2014 em-dash). Every
   occurrence is a violation. Replace each with a comma, colon, or restructured
   sentence. Em-dashes are prohibited without exception.

6. **Failed primary-source searches** -- scan §2 Investigation for any claim
   where a secondary source references a paper, arXiv preprint, or DOI that
   you were unable to locate. For each such case, confirm there is an explicit
   inline note recording the search query used and the "not found" outcome.
   A missing note here is a gap in Risks/Gaps -- add it before proceeding.

7. **Staged-content sanity check** -- after `git add`, run `git diff --cached --stat`
   and confirm the staged diff contains the full rewritten research item, not
   just a file move or frontmatter change. Do not trigger review on a commit
   unless the staged line count matches the amount of content you expect.

If you fix anything in this self-review, re-read the affected sentences to
confirm the fix did not introduce a new violation before proceeding.

### 7. Mark as draft and trigger review

```bash
SLUG=$(basename <filename> .md)
python -m src.main research draft <filename>
git add Research/in-progress/<filename>
git diff --cached --stat
git commit -m "research: draft - ${SLUG}"
git push origin main
```

This updates the item's `status` to `reviewing` in place (no file move). The
file remains in `Research/in-progress/`.

Then trigger the review workflow and **wait for it to complete**:

```bash
gh workflow run research-review.yml -f item_path=Research/in-progress/<filename>
# Allow ~20 s for the run to register before querying its ID
sleep 20
RUN_ID=$(gh run list --workflow=research-review.yml --branch=main --limit=1 --json databaseId --jq '.[0].databaseId')
gh run watch "$RUN_ID" --exit-status || true
```

### 8. Handle review outcome

Pull the latest version of the item (the review workflow commits `review_count`
back to the file):

```bash
git pull --rebase origin main
```

Read the `review_count` field from the item's YAML frontmatter:

```bash
REVIEW_COUNT=$(grep -m1 '^review_count:' Research/in-progress/<filename> | awk '{print $2}')
```

- **If `REVIEW_COUNT` is absent or 0:** the review workflow did not run or did
  not commit -- re-trigger from Step 7.
- **If `REVIEW_COUNT >= 1`:** the review ran. Check the latest review workflow
  log for `OVERALL: FAIL` to decide whether to fix anything before completing:

  ```bash
  LAST_RUN=$(gh run list --workflow=research-review.yml --limit=1 --json databaseId --jq '.[0].databaseId')
  gh run view "$LAST_RUN" --log | grep -E "OVERALL:|VIOLATION:" || true
  ```

  - **OVERALL: PASS** (or `review_count >= 2`, which auto-passes): proceed to
    Step 9.
  - **OVERALL: FAIL and `review_count` is 1:** fix the flagged violations in
    the item, apply the Step 6 self-review, then loop back to Step 7 to trigger
    one final review pass. After that second pass the item will auto-pass
    regardless.

### 9. Complete the item

```bash
python -m src.main research complete <filename>
```

This moves the file to `Research/completed/<filename>` and updates `status` and
`completed` fields.

### 10. Update learnings.md

Read `learnings.md`. Check whether any finding from this item adds signal to an
existing cross-cutting thread:

- If a finding **strengthens, extends, or contradicts** an existing thread ->
  update that thread's **The learning** claim and add the item to its
  **Evidence** list.
- If the item establishes a **genuinely new cross-cutting theme** -> add a new
  numbered thread entry.
- If no findings are cross-cutting -> skip this step (no update needed).

Do not add findings that are already captured or that apply only to this item.
`learnings.md` is a synthesis layer across items, not a per-item summary.

### 11. Create session log

Create a new file `progress/YYYY-MM-DD-{slug}.md` where `{slug}` is the
short-title portion of the research item filename (e.g.
`slack-msteams-research-integration` from
`2026-03-02-slack-msteams-research-integration.md`) with this content:

```markdown
# YYYY-MM-DD -- Research Loop ({slug})

**Completed:**

Research item:
- `Research/completed/<filename>` -- completed; <2-3 sentence summary of key findings>

Sources consulted:
- <url 1> (<description>)
- <url 2> (<description>)
- <url 3> (<description>)

## Mini-Retro

1. **Did the process work?** <answer>
2. **What slowed down or went wrong?** <answer>
3. **What single change would prevent this next time?** <answer -- if nothing, say so>
4. **Is this a pattern?** <answer -- if yes, note whether it matches a known pattern in the instructions or warrants adding a new one>
```

### 12. Apply retro improvements immediately

Re-read the Mini-Retro you just wrote (questions 3 and 4). For each
actionable improvement identified:

- **If question 3 names a concrete change** (not "nothing") and the change
  belongs in `research-prompt.md`, apply it now -- before committing. Edit the
  relevant rule, checklist item, or step in `research-prompt.md` directly.
- **If the retro notes a pattern** (question 4 = "yes"), also check whether
  the same fix needs to go into a companion skill file in `.github/skills/`.
  If so, note the required change in the session log under a new
  `## Pending skill improvements` heading -- you cannot edit the skills
  submodule directly, but the note ensures the gap is not lost.

Do not defer improvements to a follow-up task or PR comment. The retro is only
useful if its output is applied in the same session. If question 3 says
"nothing", skip this step. If you make a change, briefly note it in the session
log under `## Applied improvements`.

### 13. Commit to main

```bash
git add .
git commit -m "research: complete - <short-title-from-filename>"
git push origin main
```

The commit message format is `research: complete - <slug>` where `<slug>` is
the date-and-slug portion of the filename (e.g.
`research: complete - ai-strategy-swe-focus`).

---

## Rules

- Do **one item** only. Stop after the commit.
- Commit **directly to `main`**. Do not open a pull request.
- Do **not** edit `PROGRESS.md` -- it is now static and conflict-free by
  design. Session logs go in `progress/` only.
- The session log in `progress/` is **mandatory**. It must be in the same
  commit as the completed item.
- Do not skip the Evidence Map. Every Key Finding needs a row.
- If no item is available, print "Backlog is empty." and exit without
  committing.
- **When creating new backlog items** from Open Questions, assign `priority`
  using this heuristic:
  - `high` -- the item answers a question that directly unblocks tooling,
    infrastructure, or other research (set `blocks` to list what it unblocks);
    or the item is strategically urgent and has clear downstream impact.
  - `medium` -- useful, advances understanding, but does not immediately block
    other work.
  - `low` -- exploratory, no clear downstream dependency, nice-to-have.
  Set `blocks: []` unless the new item is a clear prerequisite for one or more
  other backlog items, in which case list their slugs (filename without `.md`).
- **New backlog items must be created in `Research/backlog/`**, never in
  `Research/in-progress/` or the repo root. Use the filename format
  `YYYY-MM-DD-<slug>.md`.
- **`Research/backlog/`, `Research/in-progress/`, and `Research/completed/`
  each contain a `.gitkeep` file. Never delete it.** Git drops empty
  directories; the `.gitkeep` keeps each directory tracked so the workflow
  `find` commands do not fail.
