---
title: "iOS Shortcuts for research capture and query"
added: 2026-03-02
status: backlog
priority: medium
tags: [ios, shortcuts, mobile, capture, interface, delivery, siri]
started: ~
completed: ~
output: [knowledge, backlog-item]
---

# iOS Shortcuts for research capture and query

## Research Question

What iOS Shortcuts workflows provide the most value for a personal research system hosted on GitHub — covering both low-friction research capture (adding a URL or idea to the backlog from anywhere on iOS) and lightweight query (checking recent research or asking a question against the corpus) — and what GitHub APIs or existing delivery channels do they depend on?

## Scope

**In scope:**
- Research capture shortcuts: adding a new backlog item from Safari Share Sheet, copying a URL, or dictating a title via Siri
- Implementation paths: iOS Shortcuts calling the GitHub API directly (create file or create issue), Shortcuts calling a GitHub Actions `workflow_dispatch` endpoint
- Query shortcuts: retrieving a list of recently completed research items, or asking a natural-language question against the corpus
- Reading the GitHub wiki from iOS: the wiki is already accessible via Safari on iOS; assess whether a shortcut that opens the wiki Home page is sufficient or if a dedicated shortcut adds value
- Siri integration: dictating a research idea hands-free, which creates a backlog item via the GitHub API
- Share Sheet integration: sharing a URL (web page, YouTube video) directly into the research backlog

**Out of scope:**
- Android or cross-platform shortcuts
- Building a native iOS app
- Integration with third-party note-taking apps (Obsidian Mobile, Notion) as intermediaries — keep the pipeline direct to GitHub
- Persistent on-device storage of the research corpus

**Constraints:** The owner uses iPhone and the GitHub iOS app. Any shortcut must work without a Mac, without SSH keys, and without a local development environment. The GitHub API and GitHub Actions `workflow_dispatch` are the only server-side components available.

## Context

The owner interacts with the repository exclusively via the GitHub website and iOS GitHub app (stated in AGENTS.md). The GitHub iOS app covers reading and commenting on issues/PRs but does not provide a one-tap "add research idea" flow from any iOS context (e.g., reading a web article in Safari, watching a YouTube video).

iOS Shortcuts can call arbitrary HTTP APIs, process URLs and text from the Share Sheet, prompt the user for input, and chain multiple steps. A shortcut that:
1. Captures the current page URL and/or prompts for a title
2. Calls the GitHub API to create a new issue or directly create a file in `Research/backlog/`
3. Confirms success with a notification

...would provide exactly the low-friction capture path the system currently lacks from iOS.

The `2026-02-27-simple-process-for-adding-research-item.md` research (completed) identified two capture paths: `python -m src.main research add "<title>"` for agents, and a GitHub issue form for the owner. The iOS Shortcuts path is a third, mobile-native capture path that the completed research did not address.

The `2026-03-01-github-wiki-research-content.md` research (completed) established the wiki as a readable delivery channel. The wiki is accessible in Safari on iOS, but the shortcut could provide a faster path: open the wiki Home page directly, bypassing the repository navigation.

Query shortcuts are more complex — they require either the conversational interface (`2026-03-02-chat-conversational-interface.md`) or a direct call to a GitHub Actions `workflow_dispatch` that runs a search and posts the result as a new issue or comment. Assess which approach is feasible without a persistent server.

## Approach

1. **Capture shortcut design** — Design the "Add to Research Backlog" shortcut:
   - Input: URL from Share Sheet (optional) + user-prompted title
   - Action: call GitHub API (`PUT /repos/{owner}/{repo}/contents/Research/backlog/{date}-{slug}.md`) to create a new Markdown file following `_template.md` structure
   - Alternative action: call GitHub API (`POST /repos/{owner}/{repo}/issues`) to create a new issue with the title and URL, letting the existing issue-to-backlog workflow handle the rest
   - Authentication: GitHub Personal Access Token stored in iOS Keychain via Shortcuts; assess scope required (`repo` vs. `contents: write`)
   - Assess: what is simpler — direct file creation or issue creation? Issue creation requires fewer fields (title + body); file creation requires a complete Markdown template.

2. **Share Sheet integration** — Confirm that iOS Shortcuts can receive URLs via the Share Sheet extension point. Design the flow: share URL from Safari → Shortcut activates → prompts for research title → creates backlog item.

3. **Siri hands-free capture** — Design a Siri-invocable shortcut: "Hey Siri, add research idea: [title]." Assess: how does Siri dictation integrate with the shortcut's input handling?

4. **Wiki quick-access shortcut** — Design a simple shortcut that opens the GitHub wiki Home page (the compiled research index). This is one step — open URL — but having it as a named shortcut on the home screen or in Shortcuts gallery lowers the friction of accessing completed research from iOS.

5. **Query shortcut design** — Assess feasibility of a "Search Research" shortcut:
   - Option A: Shortcut triggers GitHub Actions `workflow_dispatch` with a search query; workflow runs the search and posts results as a GitHub issue; Shortcut opens the issue URL
   - Option B: Shortcut calls the conversational MCP server (if implemented) directly from iOS
   - Option C: Shortcut opens the GitHub wiki and lets the owner use Safari's find-in-page
   - Assess: Option A is the most feasible without a persistent server; Option B requires the MCP server from `2026-03-02-chat-conversational-interface.md` to have an HTTP interface

6. **Authentication and secrets** — GitHub API calls from iOS Shortcuts require a token. Assess: what scopes are required? Is a fine-grained PAT (`contents: write` on this repo only) sufficient? How is the token stored and rotated securely on-device?

7. **Shortcut distribution** — iOS Shortcuts can be shared via iCloud links. Assess whether a shareable shortcut (with placeholder token) would benefit others running similar research systems. This is optional and out of scope for the initial implementation.

## Sources

- [ ] `Research/completed/2026-02-27-simple-process-for-adding-research-item.md` — existing capture paths (agent CLI + GitHub issue form); iOS Shortcuts is the missing third path
- [ ] `Research/completed/2026-03-01-github-wiki-research-content.md` — wiki as the readable delivery channel accessible from iOS Safari
- [ ] `Research/backlog/2026-02-27-interface-and-delivery.md` — upstream interface and delivery item
- [ ] `Research/backlog/2026-03-02-chat-conversational-interface.md` — query interface (dependency for query shortcut Option B)
- [ ] GitHub REST API — Contents: https://docs.github.com/en/rest/repos/contents — `PUT` to create/update a file
- [ ] GitHub REST API — Issues: https://docs.github.com/en/rest/issues/issues — `POST` to create an issue
- [ ] GitHub REST API — Actions (workflow_dispatch): https://docs.github.com/en/rest/actions/workflows#create-a-workflow-dispatch-event
- [ ] Apple Shortcuts User Guide: https://support.apple.com/guide/shortcuts/welcome/ios — Share Sheet, Get URL, Get Contents of URL, Ask for Input, Show Notification
- [ ] Apple Shortcuts — Get Contents of URL action: supports arbitrary HTTP methods and headers (suitable for GitHub API calls)
- [ ] Community iOS Shortcut examples for GitHub API calls (search: "iOS Shortcut GitHub API")

---

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
- Description: Recommended shortcut designs for capture (Share Sheet + Siri) and query (wiki quick-access + search); GitHub API approach (issue creation vs. direct file creation); authentication pattern; implementation slice for at least the capture shortcut
- Links:
  - `Research/completed/2026-02-27-simple-process-for-adding-research-item.md` (existing capture paths)
  - `Research/completed/2026-03-01-github-wiki-research-content.md` (wiki delivery channel)
  - `Research/backlog/2026-02-27-interface-and-delivery.md` (upstream item)
  - `Research/backlog/2026-03-02-chat-conversational-interface.md` (query dependency)
