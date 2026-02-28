---
title: "Simple process for adding a research item"
added: 2026-02-27
status: backlog
priority: high
tags: [process, workflow, tooling]
started: ~
completed: ~
output: [tool, knowledge]
---

# Simple process for adding a research item

## Question / Hypothesis

What is the minimum-friction workflow for adding a new research item so that good ideas get captured before they are lost?

## Context

Without a fast capture process, high-value research ideas get lost or deferred indefinitely. The current process (copy template, rename file, fill in fields, commit) has several manual steps. There may be a better approach — CLI command, GitHub issue template, voice note → text, etc.

## Scope

**In scope:**
- Evaluating CLI-based item creation (`python -m src.main research add "<title>"`)
- Evaluating GitHub issue templates as a capture mechanism
- Mobile-friendly capture options

**Out of scope:**
- Full research management UI

## Approach

1. Review how similar tools (Zettelkasten apps, research notebooks) handle quick capture
2. Prototype the CLI command approach (maps to `BACKLOG.md` Epic 1.1)
3. Evaluate trade-offs: CLI vs issue template vs direct file edit

## Sources

- [ ] Zettelkasten quick-capture patterns
- [ ] GitHub issue template docs

## Findings

*(Fill in when completing. Follow the research skill synthesis structure.)*

### Executive Summary

3–5 sentences. What is the answer to the research question? State the key conclusion directly.

### Key Findings

Ordered list. Each finding is a specific, evidence-backed claim.

1.
2.

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| | | high / medium / low | |

### Assumptions

Explicit assumptions made during the investigation and the justification for each.

- **Assumption:** ... **Justification:** ...

### Analysis

How the evidence was weighed, what trade-offs were identified, and how competing interpretations were resolved.

### Risks, Gaps, and Uncertainties

What is still unknown? Where does the evidence fall short? What could change the conclusion?

-

### Open Questions

Questions that surfaced during research but are out of scope for this item. Each may become a new backlog item.

-

---

## Output

- Type: tool, knowledge
- Description: CLI `research add` command + updated workflow docs
