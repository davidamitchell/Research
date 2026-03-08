---
title: "Inbox folder capture-and-triage pattern for memory systems"
added: 2026-03-08
status: backlog
priority: medium
tags: [inbox, capture, triage, pattern, memory-system, workflow, gtd]
started: ~
completed: ~
output: [knowledge, tool]
---

# Inbox folder capture-and-triage pattern for memory systems

## Research Question

Is an "inbox folder" pattern — where all new memory captures land in an unprocessed queue before being reviewed, tagged, and promoted into the main memory store — a good design for a personal memory system, and what does a minimal, effective implementation look like?

## Scope

**In scope:**
- The GTD-inspired inbox pattern applied to digital memory systems
- Design of the inbox: where captures land (folder, file, issue queue), what format they use
- Triage workflow: how items move from inbox to processed memory (manual review, semi-automated tagging, discard path)
- Tooling for triage: CLI commands, git-based review, or AI-assisted classification
- Integration with capture paths (iOS Shortcuts, Telegram bot, Slack bot) — all land in inbox first

**Out of scope:**
- Full GTD system implementation (focus on the inbox/capture-triage loop only)
- Email inbox as a capture source (separate concern)

**Constraints:** Must work in the git-backed memory store without requiring a database or persistent server for the inbox itself.

## Context

Multiple capture paths (iOS Shortcuts, Telegram bot, Slack bot, manual file creation) all need a common landing zone so that raw, unprocessed captures don't pollute the searchable memory store until they have been reviewed and enriched. The inbox pattern is well-established in productivity systems (GTD's "collect" phase) but needs to be adapted for a git-backed, agent-friendly memory system.

The key design question is whether the inbox should be a folder (`inbox/`), a dedicated file (`INBOX.md`), a git branch, or a GitHub issue queue — and how the triage step integrates with the existing memory structure.

## Related

**Memory-System backlog:** [W-0012 — Inbox folder capture and triage pattern](https://github.com/davidamitchell/Memory-System/blob/main/BACKLOG.md) — this research item investigates the inbox design pattern for the W-0012 discovery item on structuring the capture-to-store workflow.

## Approach

1. **Pattern survey:** Review how inbox/capture patterns are used in GTD, Zettelkasten, and similar personal knowledge management systems. Identify the core invariants (fast capture, deferred classification, explicit triage step).
2. **Inbox format options:** Evaluate four inbox representations for a git-backed store: (a) `inbox/` folder with one file per capture, (b) single `INBOX.md` append-only file, (c) git branch per capture batch, (d) GitHub Issues queue. Score each on: capture speed, triage UX, git history cleanliness, agent-readability.
3. **Triage workflow design:** Design the triage step — what decisions are made (keep/discard, tag, relate, promote), what tools support it, and how it integrates with the existing memory CLI.
4. **AI-assisted triage:** Evaluate whether an agent can pre-classify inbox items (assign tags, suggest relations, flag duplicates) to reduce manual triage burden. What prompt or tool is needed?
5. **Integration with capture paths:** Confirm that each capture path (iOS Shortcuts, Telegram, Slack, manual) can write to the inbox format without friction.
6. **Prototype:** Implement the chosen inbox format and a minimal triage command. Test with 20 synthetic captures.

## Sources

- [ ] David Allen, *Getting Things Done* — inbox/collect phase
- [ ] Zettelkasten inbox practices — https://zettelkasten.de/posts/
- [ ] GitHub Issues as a capture inbox — community examples
- [ ] `davidamitchell/Memory-System` BACKLOG.md W-0012 — the corresponding discovery item that this research informs

---

## Research Skill Output

*(To be populated when research is conducted.)*

### §0 Initialise

-

### §1 Question Decomposition

-

### §2 Investigation

-

### §3 Reasoning

-

### §4 Consistency Check

-

### §5 Depth and Breadth Expansion

-

### §6 Synthesis

**Executive summary:**

**Key findings:**

**Evidence map:**

**Assumptions:**

**Analysis:**

**Risks, gaps, uncertainties:**

**Open questions:**

### §7 Recursive Review

-

---

## Findings

*(To be populated when research is completed.)*

### Executive Summary

### Key Findings

1.
2.

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| | | high / medium / low | |

### Assumptions

- **Assumption:** ... **Justification:** ...

### Analysis

### Risks, Gaps, and Uncertainties

-

### Open Questions

-

---

## Output

- Type:
- Description:
- Links:
