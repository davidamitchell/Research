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

*(to be filled in)*

## Output

- Type: knowledge, backlog-item
- Description: Storage policy per content type; ADR if significant decision
