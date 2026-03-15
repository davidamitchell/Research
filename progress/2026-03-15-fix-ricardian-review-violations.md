---
date: 2026-03-15
slug: fix-ricardian-review-violations
type: maintenance
---

# Session: Fix research review violations in ricardian-contract-model

## What was done

Fixed all violations flagged by research review in `Research/completed/2026-03-14-ricardian-contract-model.md`.

### citation-discipline fixes (4 acronym expansions)

| Acronym | First-use line | Change |
|---------|---------------|--------|
| IEEE | 57 (source list) | `Institute of Electrical and Electronics Engineers (IEEE)` |
| SQL | 69 (source list) | `Structured Query Language (SQL)` |
| IPFS | 281 (§5 Technical lens) | `InterPlanetary File System (IPFS)` |
| PGP | 287 (§5 Historical lens) | `Pretty Good Privacy (PGP)` |

All subsequent occurrences left as abbreviations only.

### speculation-control fixes (5 [inference] labels)

- §5 Behavioural lens: "is the likely growth sector for Ricardian Contract adoption" → appended `[inference]`
- Findings Analysis line 490: "is now driving a return to hybrid approaches" → appended `[inference]`
- Findings Analysis line 492: "most forceful mechanism ever applied" → inline `[inference]`
- Findings Analysis line 492: "most institutionally stable current mechanism" → inline `[inference]`
- Findings Analysis line 494: "most structurally compelling driver" → inline `[inference]`

### remove-ai-slop fixes (2 changes)

- Findings Executive Summary: rewrote opening sentence from "The Ricardian Contract is a design pattern, developed by..." to "Ian Grigg and Gary Howland developed the Ricardian Contract between 1995 and 1996 as a design pattern for..." — eliminates near-verbatim repetition with §6 Executive Summary.
- Findings Analysis paragraph 494: reworded from "The RWA tokenisation sector is the most structurally compelling driver" to "RWA tokenisation is the most structurally compelling driver" — breaks the three consecutive "The [noun]..." paragraph-opening pattern.

## Files changed

- `Research/completed/2026-03-14-ricardian-contract-model.md`
