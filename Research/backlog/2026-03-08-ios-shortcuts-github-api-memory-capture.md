---
title: "iOS Shortcuts + GitHub API: zero-infrastructure mobile memory capture"
added: 2026-03-08
status: backlog
priority: high
blocks: []
tags: [mobile, ios, shortcuts, github-api, capture, memory-system]
started: ~
completed: ~
output: [tool, knowledge]
---

# iOS Shortcuts + GitHub API: zero-infrastructure mobile memory capture

## Research Question

Can an iOS Shortcut write a timestamped `.md` file directly to a GitHub repo via the Contents API (`PUT /repos/{owner}/{repo}/contents/{path}`) with a stored PAT, with enough reliability and speed to serve as the primary mobile capture path? What are the limits: file naming, front-matter templating, base64 encoding within Shortcuts, rate limits, PAT security model, and can the same Shortcut call GitHub code search for keyword retrieval?

## Scope

**In scope:**
- iOS Shortcuts capabilities and limits for HTTP calls
- Base64 encoding of file content within Shortcuts
- Siri/dictation input as capture trigger
- Share Sheet input (capture from any iOS app)
- PAT storage security within iOS Shortcuts
- GitHub Contents API rate limits and error handling
- File naming conventions achievable within Shortcuts
- Keyword retrieval via GitHub search API from the same Shortcut
- Apple Watch dictation chaining to the Shortcut

**Out of scope:**
- Android equivalents
- Semantic retrieval (separate item)
- Self-hosted infrastructure

**Constraints:** Must be testable on a real device; no simulator for Shortcuts. PAT must be stored in iOS Keychain or equivalent secure location.

## Context

The Memory-System repo (`davidamitchell/Memory-System`) uses `.md` files as the storage layer. The GitHub Contents API supports direct file creation with a PAT — no server needed. This is the only zero-infrastructure mobile capture option: no hosted component, no third-party service, no additional app. Retrieval is the weak point (GitHub search is keyword-only, not semantic). A completed research item on iOS Shortcuts for the research system already exists (`2026-03-02-ios-shortcuts-research.md`), but that item targets this research repo; this item targets the Memory-System repo and focuses specifically on the GitHub Contents API write path and the PAT security model for personal memory data.

Cross-reference: `Research/completed/2026-03-02-agent-memory-management-context-injection.md` confirms that production systems (Cursor, Devin) use exactly this markdown-file pattern as the memory storage layer.

## Approach

1. Prototype a Shortcut that accepts text input (typed or dictated) and writes to `inbox/YYYY-MM-DD-HH-MM-title.md` via the GitHub Contents API
2. Test Share Sheet trigger — capturing a URL or text selection from any iOS app
3. Test Siri dictation input as the capture trigger (hands-free)
4. Test GitHub search API call for keyword retrieval from the same Shortcut
5. Document PAT storage: iOS Keychain vs Shortcuts global variable, security implications
6. Measure round-trip latency (Shortcut invocation → file committed on GitHub)
7. Evaluate Apple Watch complication or dictation → Shortcut chain
8. Document rate limits (GitHub Contents API: 5000 requests/hour authenticated)

## Sources

- [ ] `Research/completed/2026-03-02-agent-memory-management-context-injection.md` — production markdown-bank patterns; context on why `.md` files are the right storage layer
- [ ] `Research/completed/2026-03-02-ios-shortcuts-research.md` — existing findings on iOS Shortcuts + GitHub API for this research repo; directly applicable
- [ ] GitHub Contents API docs: https://docs.github.com/en/rest/repos/contents
- [ ] GitHub Search API docs: https://docs.github.com/en/rest/search/search
- [ ] Apple iOS Shortcuts User Guide: https://support.apple.com/guide/shortcuts/welcome/ios
- [ ] iOS Shortcuts HTTP action docs (Get Contents of URL / Set Variable)
- [ ] GitHub REST API rate limits: https://docs.github.com/en/rest/using-the-rest-api/rate-limits-for-the-rest-api

---

## Research Skill Output

*(Full output from running the research skill — retained verbatim in the completed item. §§0–5 are the investigation; §6 seeds the Findings section below.)*

### §0 Initialise

Restate the research question. Confirm scope, constraints, and output format.

-

### §1 Question Decomposition

Approach sub-questions broken into atomic questions — each answerable with a single evidence-based claim.

-

### §2 Investigation

Evidence gathered per atomic question. Label each claim: **[fact]**, **[inference]**, or **[assumption]** with source.

-

### §3 Reasoning

Facts, inferences, and assumptions explicitly separated. No unsupported generalisations or narrative leaps.

-

### §4 Consistency Check

Internal contradictions identified and resolved (or explicitly flagged where unresolvable).

-

### §5 Depth and Breadth Expansion

Findings re-examined through relevant lenses (technical, regulatory, economic, historical, behavioural).

-

### §6 Synthesis

*(This section seeds the Findings below.)*

**Executive summary:**

**Key findings:**

**Evidence map:**

**Assumptions:**

**Analysis:**

**Risks, gaps, uncertainties:**

**Open questions:**

### §7 Recursive Review

Final pass: every section justified, all threads synthesised, every claim sourced or labelled, all uncertainties explicit.

-

---

## Findings

*(Populated from §6 Synthesis above.)*

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

*(Fill in when completing — what was produced as a result of this research?)*

- Type: tool, knowledge
- Description:
- Links:
