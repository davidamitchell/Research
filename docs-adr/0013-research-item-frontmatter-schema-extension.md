# ADR-0013: Research Item Frontmatter Schema Extension (W-0044 to W-0049)

Date: 2026-04-28
Status: accepted

## Context

Five open backlog items (W-0044, W-0045, W-0046, W-0047, W-0049) each required
mutating the same four files: `Research/_template.md`, `src/research/item.py`,
`scripts/build_site.py`, and `research-prompt.md`. Completing them separately
would have forced five separate migrations of the ~214 existing completed items
and created merge-conflict risk on every subsequent PR touching those files.

The gaps each item addressed:

| Item | Gap |
|---|---|
| W-0044 | No machine-readable citation or relationship graph between items; cross-references only exist as prose |
| W-0045 | No signal when a newer item has superseded an older one; readers cannot detect stale findings |
| W-0046 | No distinction between primary research (single-question answer) and synthesis (cross-item integration) |
| W-0047 | No item-level confidence grade; individual claim labels (`[fact]`/`[inference]`) do not surface an overall reliability score |
| W-0049 | No audit trail for post-completion edits; when a finding is corrected there is no record of what changed |

W-0048 (research-first validation of the versioning design against academic norms)
was deferred: the pragmatic model is low-risk and the design can be amended via a
superseding ADR if the research contradicts it.

## Decision

Add seven new YAML frontmatter fields to the research item schema. All seven
are appended immediately after the existing `output:` field:

```yaml
cites: []          # slugs of items this item directly depends on or quotes
related: []        # slugs of thematically connected items
superseded_by: ~   # slug of a later item that overrides this one (null if not superseded)
supersedes: ~      # slug of an older item this one replaces (null if not applicable)
item_type: primary # primary | synthesis
confidence: medium # high | medium | low
versions: []       # entries: {version: "1.0", sha: "<commit-hash>", changed: YYYY-MM-DD, progress: "<path>", summary: "<one-line>"}
```

### Field semantics

**`cites`** — machine-readable citation list. The agent populates this during
§6 Synthesis with the slugs of any completed items directly quoted or depended
upon. Enables a programmatic citation graph.

**`related`** — thematic connections that do not rise to the level of citation.
Populated during §6 Synthesis when the agent identifies related completed items
that inform the same topic area.

**`superseded_by` / `supersedes`** — a symmetric pair. When item B materially
overrides item A: `superseded_by: <slug-of-B>` is set on A and
`supersedes: <slug-of-A>` is set on B. Both must be updated atomically in the
same commit. Setting only one side is a schema violation.

**`item_type`** — `primary` for a single-question research session; `synthesis`
for an item that integrates findings across multiple completed items. The
research loop excludes `synthesis` items from autonomous processing (they
require the separate synthesis workflow, W-0051).

**`confidence`** — overall evidence quality grade, set at §7 Recursive Review:
- `high`: all key findings supported by primary sources; no unresolved contradictions
- `medium`: key findings supported by secondary sources or inference chains with low uncertainty
- `low`: key findings rely on a single source, significant gaps remain, or multiple unresolved contradictions

**`versions`** — audit trail for post-completion edits. An entry is added each
time findings, claims, or conclusions change. Tag additions and `## Related
Items` changes are exempt. Sub-fields:
- `version`: `"1.0"` on initial completion; `"1.x"` for minor corrections; `"2.0"` for substantive revisions
- `sha`: the commit hash, populated after the commit
- `changed`: date of the change (`YYYY-MM-DD`)
- `progress`: path to the session log that records what changed
- `summary`: one-line description of what changed

### Immutability rule (versions field)

Any edit to a completed item's **findings, claims, or conclusions** requires:
1. A new `versions:` entry added before committing
2. A `progress/YYYY-MM-DD-{slug}.md` session log created
3. The `sha` field populated after the commit is made

The `versions:` field is the human-readable index. Git history is the diff.
No file renaming or archiving is used.

### Migration

All existing items in `Research/completed/`, `Research/backlog/`, and
`Research/in-progress/` were migrated in a single commit by appending the
seven new fields with their defaults after the `output:` line. No existing
field values were changed. Items that already had some of the new fields were
migrated to add only the missing ones.

### Site rendering

`scripts/build_site.py` was updated to:
- Render a superseded banner (dusk-coloured warning block) on item pages where
  `superseded_by` is set, linking to the superseding item
- Show a `synthesis` badge (dusk border) on synthesis item cards and pages
- Show a confidence badge (green/grey/red border) on every item page
- Render `cites` and `related` as structured link lists below each item's
  related section, with `rel-pill` labels
- Render `supersedes` as a `rel-pill` link
- Render `versions` as a table (version, date, commit SHA link, summary) below
  the cites/related sections

### Agent instructions

`research-prompt.md` was updated with an explicit "Frontmatter fields to
populate during research" block in Step 1, directing the agent to:
- Populate `cites` and `related` during §6 Synthesis
- Check for supersession during §6 and update both the new and old item if needed
- Set `item_type: synthesis` when the question explicitly asks for cross-item integration
- Set `confidence` at §7 Recursive Review using the defined criteria
- Leave `versions` as `[]` on initial completion and populate after committing

## Consequences

### Positive

- Citation graph is machine-readable; tooling can answer "what items does this one
  depend on?" without parsing prose.
- Supersession is surfaced to readers as a visual banner; stale findings are
  clearly marked.
- Synthesis items are distinguishable from primary items in browse and tag pages.
- Item-level confidence grades are visible at a glance; readers can filter for
  high-confidence findings.
- Post-completion edits are auditable via the `versions` array.
- All five backlog items (W-0044 through W-0049 except W-0048) are resolved in
  a single migration, eliminating repeated file migrations.

### Negative / Trade-offs

- The supersession rule requires updating two items atomically when supersession
  occurs. An agent that only updates one side creates an inconsistent schema
  state. Enforcement is by convention (this ADR and the research prompt) not by
  a validator.
- `confidence` is a coarse three-level grade. An agent may disagree about
  whether a finding meets the `high` bar. The criteria are intentionally
  conservative (requiring primary sources for `high`) to reduce grade inflation.
- The `versions` SHA field must be populated after the commit (the SHA is not
  known until the commit exists). This requires a second edit and commit per
  initial completion, or accepting that `sha` starts as `~` and is patched in
  a follow-up commit.

### Neutral

- W-0048 (validate versioning design against academic norms) remains open. If its
  findings contradict the `versions` design, a superseding ADR will be written
  and the schema amended. The `versions` field itself records that correction.
- The `blocks:` field in the template already existed and is not changed by this ADR.
