---
title: "Local index vs reference: what to store vs link"
added: 2026-02-27
status: backlog
priority: medium
tags: [indexing, storage, local, reference]
started: ~
completed: ~
output: [knowledge, backlog-item]
---

# Local index vs reference: what to store vs link

## Question / Hypothesis

For each type of research content, should we store a local copy / index, or just maintain a reference (URL, citation)? What are the right trade-offs between storage cost, offline access, durability, and searchability?

## Context

Not everything needs to be stored locally. Some content (YouTube transcripts, arXiv PDFs) is large and changes rarely — it may be better to fetch on demand. Other content (key passages, structured notes) should be stored locally for fast retrieval and to guard against link rot.

The right answer varies by content type:
- **Transcripts**: large, fetchable on demand, worth caching if used frequently
- **Papers**: moderately large, authoritative, worth local storage if referenced often
- **Web pages**: ephemeral, prone to link rot, worth local snapshot for key pages
- **Notes / synthesis**: always local — this is the primary research output

## Scope

**In scope:**
- Decision framework for local vs reference
- Storage format recommendations per content type
- Git-friendliness of each approach (large files → Git LFS?)

**Out of scope:**
- Implementation of the storage layer (see indexing item)

## Approach

1. Enumerate content types and their characteristics (size, stability, access frequency)
2. Apply a decision framework (store if: high access frequency OR low stability OR critical)
3. Evaluate Git LFS for large files vs external storage (S3, local filesystem outside repo)
4. Write a policy and record in an ADR

## Sources

- [ ] Git LFS docs: https://git-lfs.com
- [ ] Similar decisions in knowledge management tools (Obsidian, Logseq)

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

- Type: knowledge, backlog-item
- Description: Storage policy per content type; ADR if significant decision
