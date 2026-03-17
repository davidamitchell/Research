---
date: 2026-05-29
slug: fix-review-violations-reliable-software-llm-era
session_type: review-fix
---

# Session: Fix Review Violations — reliable-software-llm-era

## What was done

Addressed all review violations from issues #179–#190 and #199 on
`Research/completed/2026-03-14-reliable-software-llm-era.md`.

## Changes made

### Epistemic labels
- Added `[fact]`/`[inference]` labels to all 10 Findings Key Findings (issue #185)
- Added `[inference]` labels to §5 Technical, Historical, and Behavioural lens narrative sentences (issue #182)
- Added `[inference]` labels to all §6 Analysis paragraphs (issue #183)

### Source quality
- Changed `reddit.com/r/tlaplus` (unspecific URL) from `[fact]` to `[inference]` + `[SOURCE NEEDED]` in §2 A2 and §2 D (issue #199)
- Added `[SOURCE NEEDED]` to §5 Technical lens claim about model-based testing being "independently established in SE literature" (issue #199)
- Added Newcombe et al. CACM 2015 citation to §5 Historical lens TLA+ at AWS claim (issue #199)

### Authoritative links
- Added TLA authoritative link on first use in §2 A2 (issue #179)
- Added model-based testing Wikipedia link on first use in §2 A2 (issue #188)
- Added LSP authoritative link on first use in §2 C1 (issue #184)

### Accuracy
- Fixed Findings KF2: "substantially more accessible to software engineers" → "more familiar to working engineers" (matching source language, issue #179)
- Fixed dangling "different tools" fragment in §2 D inference

### Near-verbatim repetition
- Condensed Findings Executive Summary to reference §6 Synthesis (issue #186)
- Condensed Findings KF4 to reference §2 A4 for evidence; fixed self-referential cross-reference (issue #186)

### Em-dashes
- Removed all 95 em-dash characters (—) from the file, replacing each with ` - `

## Outcome

All changes committed to branch `copilot/clean-up-research-review-issues`.
