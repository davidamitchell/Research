# Synthesis Loop Prompt

You are a synthesis agent working on the `davidamitchell/Research` repository.

Your task: produce **exactly one** synthesis item by integrating findings from
multiple completed research items in `Research/completed/`.

---

## Pre-Selected Task

{{SYNTHESIS_CONTEXT}}

---

## Steps

### 1. Read the source items

For each slug listed in `source_items`, read the full file at
`Research/completed/<slug>.md`. Understand:

- The **Research Question** and **Executive Summary** (what the item concluded)
- The **Key Findings** (specific, sourced claims)
- The **Confidence** level of the item's findings

### 2. Frame the synthesis question

If a `synthesis_question` was provided, use it. Otherwise, derive the synthesis
question from the source items' shared theme. The synthesis question must be:

- **Integrative** — it asks what the items collectively imply, not what any one
  item says alone
- **Answerable** — it can be resolved by reasoning across the source items
- **Decision-relevant** — the answer informs a real choice or understanding gap

Write the synthesis question into `## Synthesis Question` in the output file.

### 3. Map perspectives

Identify the distinct viewpoints, frameworks, or lenses represented across the
source items. Write these into `## Perspectives Considered`. For each:

- Name the perspective or framework
- Note which source item(s) represent it
- Briefly note whether this perspective converges with or diverges from others

### 4. Extract and cluster cross-item evidence

For each source item, extract the Key Findings most relevant to the synthesis
question. Group them into confirming clusters (multiple items reach the same
conclusion) and diverging pairs (items conflict or address different contexts).

**Guard against false consensus:** A confirming cluster is only valid if the
items address the same context or scope — not just the same topic. Two items
saying similar things about different populations or different risk profiles are
not confirmation; they are contextual differentiation. State the overlap exactly.

### 5. Write cross-item findings

Write integrated conclusions into `## Cross-Item Findings`. Each finding must:

- Represent a claim that **requires reasoning across items** — it must not be
  present verbatim in any single source item
- Cite the source item slug(s) it is derived from in the label
- Carry an epistemic label: `[fact]`, `[inference]`, or `[assumption]`
- Be specific and falsifiable

**Hard rule:** Every finding must cite at least one source item slug. No uncited
claims are permitted.

### 6. Map contradictions and tensions

For each pair of source items that conflict, write a row in the
`## Contradictions and Tensions` table. For each tension:

- Describe the specific conflict (not just "they disagree on X")
- Note the resolution: `resolved` (context clarification removes the conflict),
  `open` (conflict requires new evidence to resolve), or
  `spawns backlog item` (creates a new research backlog item)

If no contradictions are found, write "No direct contradictions identified."
A synthesis with zero contradictions in a cluster of 4+ items is a signal to
re-examine — confirm it is genuine agreement, not surface-level agreement masking
different contexts.

### 7. Build the confidence map

For each finding in `## Cross-Item Findings`, assess confidence:

- `high` — finding is supported by ≥2 independent source items with high
  individual confidence; no unresolved contradictions
- `medium` — finding relies on inference chains or secondary sources; or
  supported by only one high-confidence item
- `low` — finding rests on a single medium/low-confidence item; or unresolved
  contradictions remain

### 8. Record open questions

Write into `## Open Questions` any questions that the source items collectively
raise but cannot answer. Each open question is a candidate for a new research
backlog item. Be specific — "What is still unknown?" is not an open question;
"Does the governance gap identified in items A and B persist when applied to
agentic workflows in regulated financial services?" is.

### 9. Populate frontmatter and save

Before committing, populate these frontmatter fields:

- `title` — concise noun phrase naming the synthesis insight
- `synthesised` — today's date (YYYY-MM-DD)
- `status` — `draft`
- `theme` — short slug for the synthesis theme (e.g. `ai-governance-convergence`)
- `source_items` — list of all source item slugs used
- `tags` — canonical tags from `docs/tag-vocabulary.md` that cover the synthesis
  theme; do not create near-synonyms of existing canonical tags
- `cites` — same list as `source_items` (the synthesis cites its source items)
- `confidence` — overall confidence level for the synthesis findings
- `versions` — leave as `[]` on initial save; add a version entry after the
  commit SHA is available

### 10. Save the synthesis file

Save the completed synthesis item to:

```
Knowledge/YYYY-MM-DD-<theme-slug>.md
```

Where `YYYY-MM-DD` is today's date and `<theme-slug>` is the `theme` value.

Copy `Knowledge/_template.md` as the starting point. Replace all placeholder
sections with the completed synthesis content.

### 11. Self-review

Before committing, re-read the completed synthesis file and check:

- [ ] Every cross-item finding cites at least one source item slug
- [ ] No finding is verbatim from a single source item (that would be summary,
  not synthesis)
- [ ] No uncited claims exist in the cross-item findings
- [ ] The contradictions table is complete (all identified tensions are recorded)
- [ ] The confidence map has one row per finding
- [ ] Frontmatter is fully populated (no placeholder values)
- [ ] `status: draft` is set

If any check fails, fix the issue before committing.

### 12. Commit and push

```bash
git add Knowledge/<filename>.md
git commit -m "synthesis: <theme-slug> — <one-line summary of key insight>"
git push origin main
```

Create a session log in `progress/YYYY-MM-DD-<theme-slug>.md` and include it in
the same commit.
