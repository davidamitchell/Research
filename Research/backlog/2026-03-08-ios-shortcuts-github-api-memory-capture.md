---
title: "iOS Shortcuts + GitHub API for frictionless memory capture"
added: 2026-03-08
status: backlog
priority: high
tags: [ios-shortcuts, github-api, memory-capture, mobile, automation]
started: ~
completed: ~
output: [tool, knowledge]
---

# iOS Shortcuts + GitHub API for frictionless memory capture

## Research Question

Can iOS Shortcuts, using the GitHub REST API directly, provide a sufficiently frictionless capture path for adding memory items to a GitHub-backed memory system from an iPhone — and what are the practical limitations (auth, payload size, latency, error handling)?

## Scope

**In scope:**
- GitHub REST API endpoints usable from iOS Shortcuts (create file, append to file, create issue)
- Authentication approaches available in Shortcuts (Bearer token in header, stored in Keychain or Shortcuts variable)
- Shortcut design patterns for low-tap capture (share sheet, widget, back tap)
- Error handling and offline behaviour
- Practical payload limits and rate limits

**Out of scope:**
- Android or cross-platform automation tools
- Third-party automation platforms (Zapier, Make) — separate research item

**Constraints:** Must be operable from iPhone with no Mac or laptop required. Must use only tools available on iOS without sideloading.

## Context

The Memory-System project requires a fast, mobile-native capture path so that insights, links, and observations can be added to the knowledge graph from an iPhone with minimal friction. The GitHub REST API is already available as a backend (the memory system stores data in a GitHub repo), and iOS Shortcuts can make authenticated HTTP requests — making this a potentially zero-infrastructure capture path.

The hypothesis is that a Shortcut can accept text (from the share sheet, clipboard, or dictation), construct a JSON payload, and POST to the GitHub API to create or append a memory item — all without leaving the current app.

## Related

**Memory-System backlog:** [W-0008 — iOS Shortcuts + GitHub API capture path](https://github.com/davidamitchell/Memory-System/blob/main/BACKLOG.md) — this research item investigates whether iOS Shortcuts with the GitHub REST API is a viable implementation path for the W-0008 discovery item.

## Approach

1. **API endpoint survey:** Identify the GitHub API calls needed (create file vs update file vs create issue) and evaluate each for use from Shortcuts (latency, complexity, error surface).
2. **Auth design:** Determine the best approach for storing a PAT or fine-grained token in Shortcuts — Keychain access, environment variable emulation, or encrypted Shortcuts variable.
3. **UX flow design:** Map the minimal-tap journey from "I have something to capture" to "it's in the memory system" for three scenarios: share sheet (from browser/app), widget button, and dictation.
4. **Error handling and offline:** How does the Shortcut behave when offline or when the API returns an error? Can partial drafts be recovered?
5. **Prototype and test:** Build a working Shortcut and test round-trip latency, reliability, and UX friction against the target of ≤ 3 taps.

## Sources

- [ ] GitHub REST API docs: create/update file endpoint — https://docs.github.com/en/rest/repos/contents
- [ ] iOS Shortcuts documentation for HTTP requests — https://support.apple.com/guide/shortcuts/
- [ ] Community examples of GitHub API calls from iOS Shortcuts
- [ ] `davidamitchell/Memory-System` BACKLOG.md W-0008 — the corresponding discovery item that this research informs

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
