---
title: "LanceDB vector index rebuild from git history"
added: 2026-03-08
status: backlog
priority: medium
tags: [lancedb, vector-index, git, rebuild, durability, memory-system]
started: ~
completed: ~
output: [tool, knowledge]
---

# LanceDB vector index rebuild from git history

## Research Question

Can a LanceDB vector index be reliably rebuilt from scratch using only the git history of a memory-store repository — and what is the correct design for keeping the index reproducible, portable, and survivable across environment changes?

## Scope

**In scope:**
- LanceDB's on-disk format and its git-friendliness (what can/cannot be committed)
- Rebuild process: reading all memory items from git-tracked files and re-embedding them
- Embedding model version pinning: ensuring a rebuild produces a semantically equivalent index
- CI pipeline for automated index validation (rebuild smoke test on push)
- Handling deleted or modified items during a rebuild

**Out of scope:**
- LanceDB cloud (focus on local/self-hosted)
- Comparison with other vector DBs (separate research item)
- Real-time incremental update (separate concern from full rebuild)

**Constraints:** Must work in a GitHub Actions environment. Rebuild must complete in a reasonable time (target < 5 minutes for a personal-scale memory store of up to 10,000 items).

## Context

The Memory-System stores memories as structured Markdown files in a git repository, with a LanceDB index as a derived artefact for vector search. Because the index is derived — not source-of-truth — it must be rebuildable from the git history alone. This is important for: (a) moving to a new machine, (b) recovering from index corruption, (c) changing the embedding model, and (d) validating the index is consistent with the source data in CI.

The design question is: what is the right rebuild workflow, and what needs to be committed vs gitignored?

## Related

**Memory-System backlog:** [W-0015 — LanceDB index rebuild from git](https://github.com/davidamitchell/Memory-System/blob/main/BACKLOG.md) — this research item directly supports the W-0015 discovery item on ensuring the vector index is reproducible from git history.

## Approach

1. **LanceDB on-disk format:** Understand what LanceDB writes to disk (Lance files, manifest, indices). What can be committed to git? What is too large or volatile to commit?
2. **Rebuild script design:** Design a `rebuild_index.py` script that: reads all memory files from disk (or git), generates embeddings using the pinned model, and writes a fresh LanceDB table.
3. **Embedding model pinning:** Determine how to pin the embedding model version (model name + version in config) so that a rebuild six months later produces a compatible index.
4. **Deleted and modified items:** How does the rebuild handle memories that have been edited or deleted since they were first indexed? The git log is the authoritative list of current items.
5. **CI integration:** Write a GitHub Actions job that runs the rebuild script on push and verifies the resulting index returns expected results for a set of test queries.
6. **Performance benchmark:** Measure rebuild time for a 1,000-item and 10,000-item corpus on the GitHub Actions free tier.

## Sources

- [ ] LanceDB documentation on the Lance file format — https://lancedb.github.io/lancedb/
- [ ] LanceDB Python API — https://lancedb.github.io/lancedb/python/python/
- [ ] SentenceTransformers model versioning — https://www.sbert.net/
- [ ] GitHub Actions resource limits (disk, memory, time) — https://docs.github.com/en/actions/using-github-hosted-runners/about-github-hosted-runners
- [ ] `davidamitchell/Memory-System` BACKLOG.md W-0015 — the corresponding discovery item that this research informs

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
