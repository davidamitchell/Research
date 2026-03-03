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

### 4. Research the item

Investigate all sub-questions in the Approach section. Use available web tools
(`WebSearch`, `WebFetch`, or `Bash` with curl) to check every source listed and
follow any leads they produce.

**Evidence discipline:**
- Every claim you write must map to a source.
- If a source is inaccessible, note it in Risks/Gaps.
- Label derived or inferred claims as `low` confidence in the Evidence Map.
- Do not state things you cannot support.

### 5. Fill in the Findings section

Edit `Research/in-progress/<filename>` and fill in **all** subsections under `## Findings`:

- **Executive Summary** — 3–5 sentences. Direct answer to the research question. State the key conclusion first.
- **Key Findings** — ordered list, 6–12 items. Each is a specific, evidence-backed claim.
- **Evidence Map** — table: claim | source | confidence (high/medium/low) | notes. Every Key Finding must appear here.
- **Assumptions** — each assumption and its justification.
- **Analysis** — how evidence was weighed, trade-offs identified, competing interpretations resolved.
- **Risks, Gaps, and Uncertainties** — what is still unknown; where evidence is thin.
- **Open Questions** — questions that surfaced but are out of scope; may become new backlog items.
- **Output section** — type (`knowledge`), description, and links to the three most important sources.

**Writing style:**
- Direct, declarative prose. State findings as facts or clearly labelled inferences.
- No filler phrases ("it is worth noting", "importantly", "it should be said", "in conclusion").
- No sycophantic transitions. Each section earns its content.

### 6. Complete the item

```bash
python -m src.main research complete <filename>
```

This moves the file to `Research/completed/<filename>` and updates `status` and `completed` fields.

### 7. Update PROGRESS.md

1. Change the `Last updated:` line **immediately after** the `# Progress` heading (the topmost one in the file) to: `Last updated: YYYY-MM-DD (<short title>)` using today's date.
2. Insert a new Work Log entry **at the top** of the `## Work Log` section (above the existing most-recent entry):

```markdown
### YYYY-MM-DD — Research Loop (<short title>)

**Completed:**

Research item:
- `Research/completed/<filename>` — completed; <2–3 sentence summary of key findings>

Sources consulted:
- <url 1> (<description>)
- <url 2> (<description>)
- <url 3> (<description>)
```

### 8. Commit to main

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
- The PROGRESS.md update is **mandatory**. It must be in the same commit as the completed item.
- Do not skip the Evidence Map. Every Key Finding needs a row.
- If the backlog is empty, print "Backlog is empty." and exit without committing.
- **When creating new backlog items** from Open Questions, assign `priority` using this heuristic:
  - `high` — the item answers a question that directly unblocks tooling, infrastructure, or other research (set `blocks` to list what it unblocks); or the item is strategically urgent and has clear downstream impact.
  - `medium` — useful, advances understanding, but does not immediately block other work.
  - `low` — exploratory, no clear downstream dependency, nice-to-have.
  Set `blocks: []` unless the new item is a clear prerequisite for one or more other backlog items, in which case list their slugs (filename without `.md`).
