---
title: "Keeping research backlog separate from repo improvement backlog"
added: 2026-02-27
status: backlog
priority: high
tags: [process, workflow, organisation]
started: ~
completed: ~
output: [knowledge]
---

# Keeping research backlog separate from repo improvement backlog

## Question / Hypothesis

What is the cleanest way to separate two distinct types of work — *what to research* vs *how to improve this repo* — so that neither overwhelms the other and each can be prioritised independently?

## Context

In a repo that is both a research tracker *and* a code project, the backlog naturally splits into two kinds of items:
1. **Research items** — questions and topics to investigate (e.g. "best way to synthesise information")
2. **Repo improvement items** — code, tooling, and structural work (e.g. "add YouTube fetcher")

Mixing these in a single list makes prioritisation harder and obscures what is actually being worked on.

## Scope

**In scope:**
- File-system separation strategy
- Labelling and status field conventions
- How to reference a research item from a repo improvement item and vice versa

**Out of scope:**
- External project management tools

## Approach

1. Implement the two-file approach: `Research/backlog/` + `BACKLOG.md`
2. Define a cross-reference convention (e.g. `see Research/backlog/YYYY-MM-DD-title.md`)
3. Document the convention in `AGENTS.md` and `Research/README.md`

## Sources

- [ ] Existing conventions in `davidamitchell/Latest-developments-`

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

- Type: knowledge
- Description: Updated `AGENTS.md` section on backlog separation; cross-reference convention
