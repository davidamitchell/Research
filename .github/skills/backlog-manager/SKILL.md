---
name: backlog-manager
version: "1.0"
description: Manages an outcome-focused backlog stored in /work/backlog.md. Handles
  command-driven operations to add, refine, list, start, complete, and archive work
  items. Each item is tracked with a status, creation date, and a clear observable
  outcome statement. Use when asked to manage a backlog, add work items, or check
  what to work on next.
---

# Backlog Manager

## When Not to Use

- When the project requires complex dependency tracking between items
- When multiple people need concurrent write access (this is a single-file, single-user system)
- When risk tracking, resource allocation, or sprint planning are required
- When the work is exploratory and outcomes cannot yet be stated (use a notes file instead until outcomes can be defined)

---

## Interaction Protocol

**On ambiguous commands**, ask before acting:

- If `Add` input lacks a clear outcome, ask: "What does success look like for this item?"
- If `Refine` input is unclear, ask which specific aspect to improve: Outcome, Context, or Notes

**Output style**:

- `List` and `Next`: plain text only, no commentary
- All other commands: confirm the action taken in one sentence, then show the updated item
- Do not volunteer prioritization opinions or suggest what to work on unless `Next` is called

---

## Inputs and Outputs

**Input**: A command string (`Add`, `Refine`, `List`, `Next`, `Start`, `Complete`, `Archive`) with an optional item ID and description  
**Output**: Confirmation of action and/or formatted item(s) from `/work/backlog.md`  
**Composability**: Use alongside strategy-author (to derive outcomes from strategy) or research (to inform item context)

---

## 1. Source of Truth

All work is stored in `/work/backlog.md`. If the file does not exist, create it.

The file is the only source of truth. Read it fresh at the start of every session.
No reliance on memory.

---

## 2. File Structure

The file is an ordered list of work items using this format:

```md
# Backlog

---

## W-0001

status: needing_refinement
created: 2026-02-21
updated: 2026-02-21

### Outcome

Clear, observable end state. Must describe what is true when complete.

### Context

Optional background or rationale.

### Notes

Free-form thinking.

---

## W-0002

status: ready
created: 2026-02-22
updated: 2026-02-22

### Outcome

System supports distributed rate limiting across horizontally scaled nodes.

### Context

Current limiter is instance-local.

### Notes
```

Rules:

- Items appear in creation order.
- Order represents priority.
- IDs are sequential and never reused.
- Items are never deleted.
- Items are never silently reordered.

---

## 3. Allowed Status Values

- `needing_refinement`
- `ready`
- `active`
- `done`
- `archived`

No other statuses are permitted.

---

## 4. Outcome Standard

Every item must contain a clear Outcome section.

Outcome must:

- Describe an observable result
- Avoid describing tasks or implementation steps
- Avoid vague language
- Be testable in principle

If an added item does not meet this standard, it must default to `status: needing_refinement`.

---

## 5. Commands

### Add

```
Add: <title or description>
```

Action:

- Generate next sequential ID
- Create new item at end of file
- Set `status: needing_refinement`
- Set `created` and `updated` to today
- Convert input into a clear outcome statement if possible
- If clarity is insufficient, preserve the original text under Notes and leave Outcome minimal

Do not decompose. Do not infer scope beyond the text.

---

### Refine W-XXXX

Action:

- Improve Outcome clarity
- Remove ambiguity
- Move supporting material into Context or Notes
- Change status to `ready` only if the outcome is specific and observable
- Update `updated` date

---

### List

Action:

- List all items as: `W-XXXX – status – first line of Outcome`
- Preserve file order
- No commentary

---

### Next

Action:

- Return the first item with `status: ready`
- If none exist, return the first item with `status: needing_refinement`
- No reprioritization

---

### Start W-XXXX

Action:

- Change status to `active`
- Update `updated` date

---

### Complete W-XXXX

Action:

- Change status to `done`
- Update `updated` date

---

### Archive W-XXXX

Action:

- Change status to `archived`
- Update `updated` date

---

## 6. Constraints

- No deletion
- No reordering
- No status changes without an explicit command
- No rewriting Outcome unless explicitly refining
- No autonomous prioritization
- No hidden scoring

---

## 7. Session Initialization

On session start:

1. Read `/work/backlog.md`
2. Validate:
   - Unique IDs
   - Sequential numbering
   - Valid statuses
   - Each item contains an Outcome section
3. Report only if inconsistencies exist
