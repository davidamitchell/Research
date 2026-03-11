# Research Loop Prompt

You are a research agent working on the `davidamitchell/Research` repository.

Your task: complete **exactly one** research item from `Research/backlog/`.

---

## Steps

### 1. Pick the next item

List `Research/backlog/` and read the front matter of each `.md` file.
Select the **highest-priority** item by applying these rules in order:
1. `priority: high` before `priority: medium` before `priority: low`
2. For equal priority, prefer items with a non-empty `blocks` list — these unblock other work and should be done first.
3. For remaining ties, pick the **oldest** item (earliest date in filename).

Note the filename (e.g. `2026-02-28-ai-strategy-swe-focus.md`).

### 2. Start the item

```bash
python -m src.main research start <filename>
```

This moves the file from `Research/backlog/<filename>` to `Research/in-progress/<filename>` and updates its `status` and `started` fields.

### 3. Read the item

Read `Research/in-progress/<filename>` in full. Understand:
- The **Research Question** (what needs to be answered)
- The **Scope** (what is in/out)
- The **Approach** (sub-questions to investigate)
- The **Sources** (starting points — check all of them)

**Prior research cross-reference (mandatory):** Apply the prior work check defined in `.github/skills/research/SKILL.md §0`. Search `Research/completed/` for related items before beginning §2 Investigation.

### 4. Research the item — follow the research skill in full

Open `.github/skills/research/SKILL.md` and run every section. Write the complete output into the `## Research Skill Output` section of the item as you go. **This output is retained verbatim in the completed item.**

**§0 Initialise:** Restate the research question. Confirm scope, constraints, and output format. Write into `### §0 Initialise`.

**§1 Question Decomposition:** Recursively break the Approach sub-questions into atomic questions — each answerable with a single evidence-based claim. Write the decomposition tree into `### §1 Question Decomposition`.

**§2 Investigation:** For each atomic question, run an iterative evidence-gathering loop: gather sources, classify them (primary / secondary / tertiary), extract claims, cross-verify across independent sources, identify contradictions, update the evidence map. Use available web tools (`WebSearch`, `WebFetch`, or `Bash` with curl) to check every source listed in the item and follow leads they produce. Apply source-marking discipline as defined in `.github/skills/research/SKILL.md §2 Source Marking`. Write into `### §2 Investigation`.

**Evidence discipline:**
- Label every claim as **[fact]**, **[inference]**, or **[assumption]**.
- Every **[fact]** must map to a source. If a source is inaccessible, note it in Risks/Gaps.
- **[inference]** = derived from evidence; **[assumption]** = not verified, state the justification.
- Evidence sufficiency: at least two independent credible sources agree, or a primary source is definitive.

**Output quality:** Apply the output quality rules defined in `.github/skills/research/SKILL.md §6 Output Quality`.

**§3 Reasoning:** Remove narrative glue and unsupported generalisations. Write into `### §3 Reasoning`.

**§4 Consistency Check:** Scan for internal contradictions and unsupported leaps. Resolve or explicitly flag unresolvable contradictions. Write into `### §4 Consistency Check`.

**§5 Depth and Breadth Expansion:** Re-evaluate findings through relevant lenses (technical, regulatory, economic, historical, behavioural). Add any new insights. Write into `### §5 Depth and Breadth Expansion`.

**§6 Synthesis:** Produce the structured synthesis output and write it into `### §6 Synthesis` in the Research Skill Output section.

**§7 Recursive Review:** Validate that every section is justified, all threads synthesised, every claim sourced or labelled, all uncertainties explicit. Record the outcome in `### §7 Recursive Review`.

### 5. Seed the Findings section from §6

With `## Research Skill Output` complete, copy the §6 Synthesis content into `## Findings` — expanding each component into the full structured subsections. No new claims may appear in Findings that are not already in the Research Skill Output.

- **Executive Summary** — 3–5 sentences. Direct answer to the research question. **The first sentence must state the answer as a specific, falsifiable claim — not a restatement of the question, not a description of what the item covers, not a hedged "it depends." If the answer is genuinely uncertain, state the best-supported conclusion followed by the primary uncertainty.** State the key conclusion first.
- **Key Findings** — ordered list, 6–12 items. Each is a specific, evidence-backed claim with confidence label (high / medium / low). **Each Key Finding must be a complete sentence of at least 20 words containing a subject, a verb, and a specific object or complement.** Do not include findings that are reformulations of the research question, findings that apply generically to all research items, or findings that consist only of a label without a claim.
- **Evidence Map** — table: claim | source | confidence | notes. Every Key Finding must appear here.
- **Assumptions** — each assumption and its justification. Must match **[assumption]** labels in §2 Investigation.
- **Analysis** — how evidence was weighed, trade-offs identified, competing interpretations resolved.
- **Risks, Gaps, and Uncertainties** — what is still unknown; where evidence is thin.
- **Open Questions** — questions that surfaced but are out of scope; may become new backlog items.
- **Output section** — type (`knowledge`), description, and links to the three most important sources.

**Writing style:**
- Direct, declarative prose. State findings as facts or clearly labelled inferences.
- No filler phrases ("it is worth noting", "importantly", "it should be said", "in conclusion").
- No sycophantic transitions. Each section earns its content.

### 6. Companion skill checks

Apply all three companion skill pre-output checks defined in `.github/skills/research/SKILL.md §8 Output Finalisation`. All three must pass before proceeding. Fix any violations in the item before moving on.

### 7. Sense check

Re-read the completed item as a critical reader, not as its author. Apply all four checks:

- **Logic** — Are the conclusions actually supported by the evidence gathered? Could an informed reader challenge any causal link or inference?
- **Consistency** — Do the numbers, dates, claims, and confidence levels agree across sections (§2, Key Findings, Evidence Map)? Do the conclusions align with what the sources actually say?
- **Reality** — Does the overall picture match how the domain works in practice? Are there obvious real-world constraints, counterexamples, or mainstream positions that the item ignores or contradicts without explanation?
- **Clarity** — Would a knowledgeable non-specialist understand the argument and reach the same conclusion? Are there unstated assumptions that a reader would need to fill in themselves?

If any check surfaces a problem, fix it before proceeding.

### 8. Mark for review and trigger the reviewer

```bash
python -m src.main research draft <filename>
git add Research/in-progress/<filename>
git commit -m "research: draft - <short-title-from-filename>"
git push origin main
gh workflow run research-review.yml --field item_path=Research/in-progress/<filename>
```

This updates the item's `status` to `reviewing` without moving the file. The `gh workflow run` call triggers the automated review workflow against the committed item.

Wait for the `research-review` workflow run to complete (use `gh run watch` or check the Actions tab). If the review **fails**, a GitHub issue labelled `research-review` is created with the violations. Address every violation, then loop back to step 4 (re-run the relevant research skill sections) and repeat from step 8.

If the review **passes** (no issue created or issue closed), proceed to step 9.

### 9. Complete the item

```bash
python -m src.main research complete <filename>
```

This moves the file to `Research/completed/<filename>` and updates `status` and `completed` fields.

### 10. Create session log

Create a new file `progress/YYYY-MM-DD-{slug}.md` where `{slug}` is the short-title portion of the research item filename (e.g. `slack-msteams-research-integration` from `2026-03-02-slack-msteams-research-integration.md`) with this content:

```markdown
# YYYY-MM-DD — Research Loop ({slug})

**Completed:**

Research item:
- `Research/completed/<filename>` — completed; <2–3 sentence summary of key findings>

Sources consulted:
- <url 1> (<description>)
- <url 2> (<description>)
- <url 3> (<description>)
```

### 11. Commit to main

```bash
git add .
git commit -m "research: complete - <short-title-from-filename>"
git push origin main
```

The commit message format is `research: complete - <slug>` where `<slug>` is the date-and-slug
portion of the filename (e.g. `research: complete - ai-strategy-swe-focus`).

---

## Rules

- Do **one item** only. Stop after the commit.
- Commit **directly to `main`**. Do not open a pull request.
- Do **not** edit `PROGRESS.md` — it is now static and conflict-free by design. Session logs go in `progress/` only.
- The session log in `progress/` is **mandatory**. It must be in the same commit as the completed item.
- Do not skip the Evidence Map. Every Key Finding needs a row.
- If the backlog is empty, print "Backlog is empty." and exit without committing.
- **When creating new backlog items** from Open Questions, assign `priority` using this heuristic:
  - `high` — the item answers a question that directly unblocks tooling, infrastructure, or other research (set `blocks` to list what it unblocks); or the item is strategically urgent and has clear downstream impact.
  - `medium` — useful, advances understanding, but does not immediately block other work.
  - `low` — exploratory, no clear downstream dependency, nice-to-have.
  Set `blocks: []` unless the new item is a clear prerequisite for one or more other backlog items, in which case list their slugs (filename without `.md`).
