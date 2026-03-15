---
date: 2026-03-15
slug: fix-team-size-review-violations
---

# Fix research review violations: team-size-limits-brooks-dunbar-network-theory

## What was done

Fixed all violations flagged by research review in `Research/completed/2026-03-12-team-size-limits-brooks-dunbar-network-theory.md`.

## Changes made

**citation-discipline:**
- Expanded "FM" → "Field Manual (FM)" at first use (sources checklist, line 101)
- Expanded "AWS" → "Amazon Web Services (AWS)" at first use (sources checklist, line 103)
- Expanded "BBC" → "British Broadcasting Corporation (BBC)" at first use (Claim 2b, line 197)
- Expanded "MIT" → "Massachusetts Institute of Technology (MIT)" at first use (Claim 2e, line 203)
- Added [SOURCE NEEDED] to the §5 fire team history claim ("since at least the 1960s across multiple major armies")

**speculation-control:**
- Removed overconfident intensifier "clearly" from "clearly disproportionate" in the [inference]-labelled inflection analysis (§3)
- Added [fact] label to "Brooks explicitly distinguishes these cases" (§5 Technical lens)
- Added [fact] label + [SOURCE NEEDED] to fire team history assertion (§5 Historical/military lens)
- Added [inference] labels to "Trust formation dynamics..." and "This constraint is related to but not identical to..." (§5 Behavioural lens)

**remove-ai-slop:**
- Added a differentiating opening note to `## Findings` clarifying it consolidates and extends §6 Synthesis, incorporating §4 consistency resolutions and §5 lenses, and is organised by theme/confidence rather than by question.

## Outcome

All 8 violations resolved. Single commit: `80ba82b`.
