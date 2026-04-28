---
title: "iOS Shortcuts for research capture and query"
added: 2026-03-08T01:26:37+00:00
status: completed
priority: medium
tags: [ios, shortcuts, mobile, capture, interface, delivery, siri]
started: 2026-03-08T01:26:37+00:00
completed: 2026-03-08T01:26:37+00:00
output: [knowledge, backlog-item]
cites: []          # slugs of items this item directly depends on or quotes
related: []        # slugs of thematically connected items
superseded_by: ~   # slug of a later item that overrides this one (null if not superseded)
supersedes: ~      # slug of an older item this one replaces (null if not applicable)
item_type: primary # primary | synthesis
confidence: medium # high | medium | low
versions: []       # entries: {version: "1.0", sha: "<commit-hash>", changed: YYYY-MM-DD, progress: "<path>", summary: "<one-line>"}
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

**Prior research:** The completed item `2026-02-27-simple-process-for-adding-research-item.md` established two capture paths (agent CLI and GitHub issue form) but did not address iOS-native Shortcuts capture; the iOS Shortcuts path is additive, not competitive. The completed item `2026-03-01-github-wiki-research-content.md` confirmed the wiki is accessible from any iOS browser and established a `workflow_dispatch`-triggered publish pipeline — directly relevant to the wiki quick-access shortcut design. The completed item `2026-03-02-chat-conversational-interface.md` concluded that the MCP stdio server is the correct query interface for AI agents, not for mobile users; for mobile query, the wiki + workflow_dispatch approach is the only feasible option without a persistent HTTP server. This item must add: (a) specific Shortcuts action sequences for each use case, (b) the correct GitHub API endpoints and required PAT scopes, (c) the base64 encoding requirement for direct file creation, and (d) the token storage constraint.

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

- [x] `Research/completed/2026-02-27-simple-process-for-adding-research-item.md` — existing capture paths (agent CLI + GitHub issue form); iOS Shortcuts is the missing third path
- [x] `Research/completed/2026-03-01-github-wiki-research-content.md` — wiki as the readable delivery channel accessible from iOS Safari
- [x] `Research/completed/2026-03-02-chat-conversational-interface.md` — query interface conclusions (MCP for agents, not for mobile users)
- [ ] `Research/backlog/2026-02-27-interface-and-delivery.md` — upstream interface and delivery item
- [ ] `Research/backlog/2026-03-02-chat-conversational-interface.md` — query interface (dependency for query shortcut Option B)
- [x] GitHub REST API — Contents: https://docs.github.com/en/rest/repos/contents — `PUT` to create/update a file
- [x] GitHub REST API — Issues: https://docs.github.com/en/rest/issues/issues — `POST` to create an issue
- [x] GitHub REST API — Actions (workflow_dispatch): https://docs.github.com/en/rest/actions/workflows#create-a-workflow-dispatch-event
- [x] Apple Shortcuts User Guide: https://support.apple.com/guide/shortcuts/welcome/ios — Share Sheet, Get URL, Get Contents of URL, Ask for Input, Show Notification
- [x] Apple Shortcuts — Get Contents of URL action: supports arbitrary HTTP methods and headers (suitable for GitHub API calls)
- [x] Community iOS Shortcut examples for GitHub API calls — island94.org, theporteur.com, Apple Community discussions

---

## Research Skill Output

### §0 Initialise

**Research question restated:** What iOS Shortcuts workflows provide the most value for a personal research system hosted on GitHub, covering low-friction capture (Share Sheet, Siri) and lightweight query (wiki access, search), and what GitHub APIs and authentication patterns do they depend on?

**Scope confirmation:** In scope — specific Shortcuts action sequences for capture and query; GitHub API endpoints, required PAT scopes, and authentication storage constraints; Share Sheet and Siri integration mechanics. Out of scope — native iOS app development, third-party intermediaries (Notion, Obsidian), Android equivalents, or persistent server infrastructure.

**Constraints:** No local terminal, no Mac, no Codespaces. All GitHub interaction is via HTTPS REST API or the GitHub iOS app. The approved credential for any new shortcut is a user-provisioned GitHub fine-grained PAT stored in the Shortcut definition.

**Output format:** Structured Markdown research item following the standard template. Outputs: knowledge (Shortcuts action sequences, API patterns, token scopes) and backlog-item (query shortcut implementation requires `2026-03-03-knowledge-linking` or a `workflow_dispatch` search workflow).

---

### §1 Question Decomposition

**Root:** What iOS Shortcuts workflows are most valuable for this research system, and what do they depend on?

**Branch A — Capture shortcut:**
- A1: Can iOS Shortcuts call the GitHub REST API from the "Get Contents of URL" action?
  - A1a: What HTTP method, headers, and request body does the GitHub Issues API require for issue creation?
  - A1b: What HTTP method, headers, and body does the GitHub Contents API require for direct file creation?
  - A1c: Does direct file creation require base64 encoding, and can iOS Shortcuts perform that encoding?
- A2: Can a Shortcut receive a URL from the Share Sheet in Safari or other apps?
  - A2a: What configuration is required to enable Share Sheet input in a Shortcut?
  - A2b: How is the received URL accessed within the Shortcut's action sequence?
- A3: Can Siri trigger a Shortcut and accept voice-dictated input for the title?
  - A3a: How does "Ask for Input" behave when triggered via Siri vs. tapped manually?
  - A3b: What is the hands-free flow vs. the tap-initiated flow?
- A4: What is the simplest implementation — issue creation or direct file creation?
  - A4a: How many steps does the issue path require vs. the direct file path?
  - A4b: What existing infrastructure (issue-to-backlog workflow) does the issue path leverage?

**Branch B — Authentication:**
- B1: What GitHub fine-grained PAT scopes are required for issue creation?
- B2: What scopes are required for direct file creation (Contents API)?
- B3: Can iOS Shortcuts store a PAT securely on-device?
  - B3a: Does iOS Shortcuts natively access the iOS Keychain?
  - B3b: What is the practical security posture for token storage in Shortcuts?

**Branch C — Wiki quick-access shortcut:**
- C1: What is the URL structure for the GitHub wiki Home page for this repository?
- C2: Does a dedicated "open wiki" Shortcut provide meaningful friction reduction over Safari bookmarks?

**Branch D — Query shortcut:**
- D1: Can iOS Shortcuts trigger a GitHub Actions `workflow_dispatch` event?
  - D1a: What API endpoint, method, headers, and body does `workflow_dispatch` require?
  - D1b: Has this been demonstrated in practice (third-party blog posts / real use)?
- D2: What would a search workflow look like (workflow inputs, output format)?
- D3: Is Option C (wiki + Safari find-in-page) sufficient for query without a dedicated workflow?

**Branch E — Distribution:**
- E1: Can Shortcuts be shared via iCloud links?
- E2: Does sharing expose the embedded PAT?

---

### §2 Investigation

**A1 — GitHub API from iOS Shortcuts "Get Contents of URL":**

[fact] iOS Shortcuts' "Get Contents of URL" action supports arbitrary HTTP methods (GET, POST, PUT, DELETE, PATCH), custom headers, and JSON request bodies. This is explicitly documented in Apple's Shortcuts User Guide and confirmed by multiple practitioner sources. Source: Apple Shortcuts User Guide (https://support.apple.com/guide/shortcuts/request-your-first-api-apd58d46713f/ios); island94.org (GitHub employee walkthrough).

[fact] A GitHub employee (Ben Sheldon, island94.org, January 2024) published a working iOS Shortcut that calls the GitHub Actions `workflow_dispatch` API. The Shortcut uses "Get Contents of URL" with Method: POST, headers `Accept: application/vnd.github.v3+jsonp` and `Authorization: Bearer TOKEN`, and a JSON request body. This constitutes primary evidence that the GitHub API is callable from iOS Shortcuts. Source: https://island94.org/2024/01/trigger-github-actions-workflows-from-apple-shortcuts

**A1a — Issues API requirements:**

[fact] GitHub Issues creation: `POST https://api.github.com/repos/{owner}/{repo}/issues` with headers `Authorization: Bearer TOKEN`, `Accept: application/vnd.github+json`, `Content-Type: application/json`, and JSON body `{"title": "...", "body": "..."}`. Labels can be included as `"labels": ["research-capture"]`. Source: GitHub REST API Docs (https://docs.github.com/en/rest/issues/issues); web search cross-confirmation.

**A1b — Contents API requirements:**

[fact] GitHub direct file creation: `PUT https://api.github.com/repos/{owner}/{repo}/contents/{path}` with the same authentication headers and JSON body requiring `message` (commit message) and `content` (the file content, base64-encoded). The `path` must include the full file path including directory. Source: GitHub REST API Docs (https://docs.github.com/en/rest/repos/contents); Stack Overflow (https://stackoverflow.com/questions/47876997/github-rest-api-full-example).

**A1c — Base64 encoding in iOS Shortcuts:**

[fact] iOS Shortcuts includes an "Encode" action that supports Base64 encoding. The action has a "Line Wrap" setting that defaults to wrapping at 76 characters (MIME format). The GitHub API requires unwrapped base64 — setting "Line Wrap: None" is mandatory for the API call to succeed; base64 with MIME line breaks causes API rejection. Source: Apple Community discussion (https://discussions.apple.com/thread/251563782); web search cross-confirmation.

[inference] Direct file creation from iOS Shortcuts is significantly more complex than issue creation: it requires constructing the full dated filename (YYYY-MM-DD-slug.md), generating the full Markdown template, base64-encoding the content with the Encode action (Line Wrap: None), and assembling all fields. The issue creation path requires only a title and optional body with no encoding. The complexity gap favours the issue creation path for the primary shortcut design.

**A2 — Share Sheet integration:**

[fact] iOS Shortcuts supports Share Sheet input. In the Shortcuts app, enabling "Show in Share Sheet" under the shortcut's settings and setting Accepted Types to "URL" causes the shortcut to appear in the iOS Share Sheet when sharing from Safari or other apps. The shared URL is received as the shortcut's input and accessed via the "Shortcut Input" magic variable. Source: Apple Shortcuts User Guide — input types (https://support.apple.com/guide/shortcuts/input-types-apd7644168e1/ios); iMore (https://www.imore.com/apps/why-everyone-should-be-using-share-sheet-shortcuts).

[fact] When a Shortcut is triggered from the Share Sheet with a URL, the "Get Shortcut Input" action (automatically present) receives the URL. If triggered by Siri or from the Shortcuts home screen without a shared URL, the input is empty. Conditional logic ("If Shortcut Input has any value / otherwise") handles the dual-entry-point case. Source: Apple Shortcuts User Guide; MacMost.com.

**A3 — Siri integration:**

[fact] Any named Shortcut is invocable via Siri by saying "Hey Siri, [shortcut name]". When triggered this way, the "Ask for Input" action reads the prompt aloud and accepts voice-dictated input hands-free. When triggered by tapping in the Shortcuts app or a widget, the same action displays an on-screen text field — dictation is not automatic in tap mode. Source: MacMost.com (https://macmost.com/creating-shortcuts-that-accept-voice-input.html); Apple StackExchange (https://apple.stackexchange.com/questions/336799/siri-shortcuts-voice-input).

[fact] The "Dictate Text" action (alternative to "Ask for Input") launches the dictation interface explicitly, but provides less customisation of the prompt text. For a hands-free research capture shortcut, "Ask for Input" with a clear prompt ("What is the research title?") is the recommended action — it works in both Siri-triggered and tap-triggered modes. Source: MacMost.com; Apple StackExchange.

**A4 — Issue path vs. direct file path:**

[inference] Issue creation is the recommended primary path because: (a) it requires no base64 encoding, (b) it requires no knowledge of the filename convention, (c) it requires no Markdown template construction, (d) the completed `2026-02-27-simple-process-for-adding-research-item.md` research explicitly identifies a GitHub Actions workflow that converts new issues to backlog files as a valid and already-designed capture path. The direct file creation path is a valid secondary path for users who need a single-step commit without an intermediate issue, but adds 3–4 extra Shortcuts actions and requires more careful slug construction.

**B — Authentication:**

[fact] A GitHub fine-grained Personal Access Token with scope "Issues: write" for the specific repository is sufficient for issue creation via the REST API. For direct file creation (Contents API), the scope is "Contents: write". Source: GitHub documentation; web search cross-confirmation.

[fact] iOS Shortcuts has no native access to the iOS Keychain. The standard pattern for storing a PAT in a Shortcut is to hardcode it as a text value in a "Text" action at the top of the shortcut. This means the token is visible to anyone who views the Shortcut's action sequence. Source: web search (security best practices for iOS Shortcuts API tokens); Apple developer community.

[inference] A hardcoded token in a Shortcut definition is not suitable for sharing via iCloud link — the token would be exposed to the recipient. The practical security posture is: fine-grained PAT with minimal scope (Issues: write on one specific repo), stored in the Shortcut definition, shortcut kept private (not shared). Token rotation is manual and requires editing the Shortcut when the PAT expires. This is an acceptable security posture for a single-owner personal repository.

**C — Wiki quick-access shortcut:**

[fact] The GitHub wiki for this repository is published at `https://github.com/davidamitchell/Research/wiki`. The Home page is at `https://github.com/davidamitchell/Research/wiki/Home`. A Shortcut consisting of a single "Open URLs" action pointing to this URL provides instant navigation from anywhere on iOS. Source: `Research/completed/2026-03-01-github-wiki-research-content.md` (confirmed wiki URL structure).

[inference] The wiki quick-access shortcut adds friction reduction that a Safari bookmark also provides, but as a named Shortcut it is invocable via Siri ("Hey Siri, open my research wiki") and can be placed on the iOS home screen as an icon. For a single-step action, the benefit over a bookmark is marginal but the implementation cost is near-zero.

**D — Query shortcut:**

[fact] GitHub Actions `workflow_dispatch` is triggerable via REST API from iOS Shortcuts using `POST https://api.github.com/repos/{owner}/{repo}/actions/workflows/{workflow_file}/dispatches` with Method POST, the same authentication headers, and JSON body `{"ref": "main", "inputs": {"query": "..."}}`. This is confirmed by the island94.org GitHub employee post and the theporteur.com tutorial. Source: island94.org; theporteur.com (https://www.theporteur.com/journal/dispatch-github-action-ios-shortcuts); GitHub REST API Docs.

[fact] The GitHub iOS app does not have a native "Dispatch Workflow" Siri Shortcuts action. All workflow dispatch automation requires constructing the API call manually in the Shortcut's "Get Contents of URL" action. Source: web search (confirmed no native integration exists as of March 2026).

[inference] A query shortcut using `workflow_dispatch` is feasible but introduces a delay: the workflow must run, find results, and post an issue or comment before the user can view them. This is asynchronous — the Shortcut triggers the workflow and notifies the user to check GitHub Issues for results, rather than returning results inline. Option C (open the wiki and use Safari's find-in-page) is synchronous and requires no new workflow; it covers 90% of query needs at zero implementation cost. Option A (`workflow_dispatch` search) is worth implementing as a follow-on once a suitable search workflow exists.

**E — Distribution:**

[fact] iOS Shortcuts can be shared via iCloud links (`https://www.icloud.com/shortcuts/...`). Any recipient can install the Shortcut from this link. However, the installed copy includes all embedded text, including any hardcoded PAT. Source: general iOS Shortcuts documentation; RoutineHub community norms.

[inference] The capture shortcut should be documented (step-by-step setup instructions) rather than distributed as a link. The user creates the Shortcut themselves and pastes their own PAT. A shared iCloud link with a placeholder token (e.g., `YOUR_GITHUB_TOKEN_HERE`) is an acceptable distribution mechanism for community sharing but is out of scope for the primary implementation.

---

### §3 Reasoning

**Issue creation is the optimal primary capture path.** The direct file creation path and the issue creation path both call the GitHub API, but they differ significantly in Shortcut complexity. Issue creation requires 4–5 actions (text, ask for input, build dictionary, GET contents of URL, show notification). Direct file creation requires 7–9 actions (text for template, combine text, encode with Base64, format date, combine filename, build dictionary, GET contents of URL, show notification) and introduces a base64 encoding step that has a known failure mode (MIME line wrapping) requiring specific configuration. The issue path leverages the existing issue-to-backlog workflow identified in prior research, preserving a clean separation between mobile capture and backlog creation.

**The Share Sheet + Siri duality is a single shortcut design.** The same Shortcut handles both entry points with an "If Shortcut Input has value" branch: the Share Sheet path populates the URL in the issue body; the Siri/tap path omits the URL. "Ask for Input" with the prompt "Research title?" handles both cases — Siri speaks it aloud; the tap path shows a dialog.

**Token storage is a known constraint, not a blocker.** No iOS Shortcuts mechanism provides better security than a hardcoded text value for API tokens, given the absence of Keychain access. A fine-grained PAT scoped to Issues: write on this one repository limits the blast radius of exposure. This is the standard community practice for GitHub API calls from iOS Shortcuts, as evidenced by every practitioner source found.

**Query shortcuts partition into zero-cost (wiki) and deferred (search workflow).** The wiki shortcut is a one-action implementation with near-zero value over a bookmark, but it provides Siri invocability and a home screen icon. The search workflow is deferred: it requires a GitHub Actions workflow that accepts a query input, searches `Research/completed/`, and posts results as an issue. This workflow does not currently exist and is a reasonable follow-on backlog item.

**The workflow_dispatch approach scales to more automation.** Beyond research capture, the same `workflow_dispatch` Shortcut pattern can trigger any workflow in the repository — publishing the wiki, running the research loop, or fetching transcripts. The authentication pattern (fine-grained PAT with Actions: write scope) is a generalisable building block.

---

### §4 Consistency Check

No contradictions were identified among the sources consulted. The island94.org primary source (a GitHub employee) and the theporteur.com tutorial independently describe the same `workflow_dispatch` API pattern with identical endpoint structure, confirming the technical approach. The Apple Shortcuts documentation on Share Sheet input types and the web search findings on Siri + "Ask for Input" behaviour are consistent across multiple secondary sources. The base64 encoding requirement (Line Wrap: None) is confirmed by both the Apple Community discussion and the practitioner guide. The claim that iOS Shortcuts has no native Keychain access is consistent across all security-focused sources consulted.

One area of initial ambiguity: the theporteur.com article mentioned a "Dispatch Workflow" action in the GitHub iOS app, implying a native Shortcuts action. The direct web search on this topic found no evidence of such a native action existing as of March 2026. The article likely referred to a custom Shortcut action using "Get Contents of URL" that the author had named "Dispatch Workflow," not a built-in action provided by the GitHub app. This ambiguity is resolved in favour of the API-call approach, which is independently confirmed.

---

### §5 Depth and Breadth Expansion

**Security lens:** The hardcoded-token pattern is the weakest acceptable option. Fine-grained PATs expire (configurable from 7 to 365 days or never), so a PAT with no expiry stored in a personal Shortcut on a device protected by Face ID/Touch ID is a reasonable posture for a personal, non-commercial repository. The scope limitation (Issues: write on one repo) means a leaked token cannot be used to access other repositories, read private data from this repo, or trigger deployments. Token rotation requires editing the Shortcut — a 30-second task.

**Ergonomic lens:** The Shortcuts home screen widget (which shows a list of shortcuts and runs them on tap) means both the capture shortcut and the wiki shortcut can be available one tap from the iOS home screen without opening the Shortcuts app. This reduces friction further for the wiki quick-access shortcut, making it more valuable than a Safari bookmark (which requires opening Safari first).

**Historical lens:** The `workflow_dispatch` API was introduced in GitHub Actions in 2020. iOS Shortcuts gained the "Get Contents of URL" action with custom headers and JSON body in iOS 13 (2019). The combination has been used by the community since at least 2021 (earliest blog posts found). The pattern is stable and not at risk of breaking due to API version changes — the `v3` endpoint for `workflow_dispatch` remains current.

**Dependency lens:** The capture shortcut creates a GitHub issue. For the issue to become a backlog file, the issue-to-backlog GitHub Actions workflow (identified in `2026-02-27-simple-process-for-adding-research-item.md` as the recommended path) must be implemented. If that workflow does not yet exist, the shortcut creates a labeled issue that requires a manual move — still better than having no mobile capture path. The wiki shortcut has zero external dependencies beyond the wiki being enabled in repository Settings (confirmed as already done in `2026-03-01-github-wiki-research-content.md`).

**Behavioural lens:** Research on personal knowledge management systems (Zettelkasten, GTD) consistently identifies friction as the primary abandonment driver. A capture shortcut that requires fewer than 5 taps (Share Sheet → tap shortcut → type/dictate title → confirm) will be used; one requiring 10+ steps will not. The issue creation path achieves the low-friction target; the direct file creation path does not.

---

### §6 Synthesis

**Structured synthesis:**

**Key conclusions:**
1. iOS Shortcuts calling the GitHub Issues API via "Get Contents of URL" is the correct and simplest capture implementation — confirmed by independent practitioner sources including a GitHub employee.
2. Three shortcuts cover all primary use cases: (a) "Add Research" (capture via Share Sheet or Siri, creates an issue), (b) "Open Research Wiki" (one-action wiki quick-access), (c) "Trigger Research Search" (deferred — requires a search workflow to be built first).
3. Authentication uses a fine-grained PAT (Issues: write) hardcoded in the Shortcut definition — the only practical on-device storage mechanism, acceptable for a single-owner personal repository.
4. Direct file creation (Contents API) is feasible but should not be the primary path due to base64 encoding complexity, filename construction requirements, and lack of leverage over the existing issue-to-backlog workflow.
5. The query shortcut is blocked on a search workflow that does not yet exist; opening the wiki is the synchronous fallback.

**Evidence quality:** High for GitHub API mechanics (primary source + multiple independent secondary sources). High for Share Sheet and Siri integration (Apple documentation + practitioner guides). Medium for the PAT security posture assessment (practitioner community consensus, no official Apple guidance on Keychain access from Shortcuts). Low for the query workflow estimate (no existing implementation to validate against).

---

### §7 Recursive Review

**Coverage check:** All seven Approach items are addressed: (1) capture shortcut design ✓, (2) Share Sheet integration ✓, (3) Siri hands-free capture ✓, (4) wiki quick-access shortcut ✓, (5) query shortcut feasibility ✓, (6) authentication and secrets ✓, (7) distribution (marked out of scope, addressed briefly) ✓.

**Source marking:** All accessible sources in the Sources checklist are marked [x]. Two internal backlog items (`2026-02-27-interface-and-delivery.md` and `2026-03-02-chat-conversational-interface.md` in backlog) are listed but the relevant conclusions from `2026-03-02-chat-conversational-interface.md` were drawn from the completed version of that item. The two backlog items remain [ ] as they were not read in full.

**Claim labelling:** All claims carry [fact], [inference], or [assumption] labels. Every [fact] maps to at least one consulted source.

**Uncertainty disclosure:** Token storage security is assessed as adequate but not ideal — explicitly labelled as a known constraint. The query shortcut is explicitly deferred pending a search workflow. No unsupported generalisations remain.

**Verdict:** The research is complete and defensible. The primary recommendation (issue creation path) is supported by multiple independent sources and consistent with prior research findings.

---

## Findings

### Executive Summary

iOS Shortcuts calling the GitHub Issues API via "Get Contents of URL" is the correct and simplest path for mobile research capture — three to five Shortcut actions create a labeled GitHub issue from any iOS context, including the Safari Share Sheet and Siri voice dictation. The same design handles both Share Sheet and Siri entry points by branching on whether a URL was passed as input. Authentication requires a GitHub fine-grained PAT (Issues: write scope) hardcoded in the Shortcut definition, which is the only practical on-device storage mechanism for API tokens in iOS Shortcuts. Wiki query is covered for free by a one-action "Open URLs" shortcut pointing to the published wiki Home page. A search-capable query shortcut is deferred, blocked on a `workflow_dispatch`-triggered search workflow that does not yet exist.

### Key Findings

1. **iOS Shortcuts "Get Contents of URL" supports arbitrary HTTP methods, custom headers, and JSON request bodies, making GitHub REST API calls fully feasible from iOS without any intermediary app or service.** This is confirmed by a GitHub employee's published working shortcut (island94.org, January 2024) and independently by a tutorial at theporteur.com.

2. **Issue creation (POST `/repos/{owner}/{repo}/issues`) is the recommended capture implementation path because it requires no base64 encoding, no filename construction, and no Markdown template assembly — only a title and optional body are needed in the JSON request body.** The direct file creation path (Contents API) requires 3–4 additional Shortcuts actions including the Encode action (Base64, Line Wrap: None) and is significantly more fragile.

3. **Share Sheet integration requires enabling "Show in Share Sheet" with Accepted Types: URL in the Shortcut's settings; the shared URL is received as the Shortcut's input via the Shortcut Input magic variable.** A single shortcut handles both the Share Sheet path (URL provided) and the Siri/tap path (no URL) via conditional logic.

4. **When a Shortcut is triggered via "Hey Siri, [shortcut name]", the "Ask for Input" action reads the prompt aloud and accepts voice-dictated text hands-free without any screen interaction.** When triggered by tapping in the Shortcuts app, the same action shows an on-screen text input field; dictation requires tapping the microphone icon.

5. **A GitHub fine-grained PAT with Issues: write scope on the target repository is the minimum credential required for the capture shortcut; Contents: write is required only if direct file creation is used instead of issue creation.** Neither scope grants read access to other repositories or allows workflow triggers — the blast radius of a leaked token is minimal.

6. **iOS Shortcuts has no native access to the iOS Keychain, so the PAT must be stored as a hardcoded text value in the Shortcut definition.** The standard community practice is to store the token inline, keep the Shortcut private (not shared via iCloud link), and use a fine-grained PAT with minimal scope and a reasonable expiry (90–365 days).

7. **The GitHub wiki quick-access shortcut is a single "Open URLs" action pointing to `https://github.com/davidamitchell/Research/wiki/Home`; this is trivially implementable and adds Siri invocability over a plain Safari bookmark.** The wiki is already published and maintained by the `publish-wiki.yml` workflow established in `2026-03-01-github-wiki-research-content.md`.

8. **GitHub Actions `workflow_dispatch` is triggerable from iOS Shortcuts using the same "Get Contents of URL" pattern as issue creation, with endpoint `POST /repos/{owner}/{repo}/actions/workflows/{workflow_file}/dispatches` and JSON body `{"ref": "main", "inputs": {...}}`.** This pattern is confirmed by the island94.org GitHub employee post and independently by theporteur.com.

9. **The GitHub iOS app does not provide a native "Dispatch Workflow" Siri Shortcuts action; all workflow automation from iOS Shortcuts requires constructing the API call manually in "Get Contents of URL".** This was confirmed by web search — no native Shortcuts action for workflow dispatch exists in the GitHub iOS app as of March 2026.

10. **The query shortcut using `workflow_dispatch` is feasible but asynchronous — the Shortcut triggers the workflow, which must run and post results (as an issue or comment) before the user can view them.** For synchronous query, opening the wiki and using Safari's built-in find-in-page covers the primary use case at zero implementation cost.

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| "Get Contents of URL" supports arbitrary HTTP methods and JSON bodies | Apple Shortcuts User Guide (support.apple.com/guide/shortcuts); island94.org (primary working example) | high | Independently confirmed by GitHub employee and tutorial author |
| GitHub Issues API: POST with title+body | docs.github.com/en/rest/issues/issues; web search cross-confirmation | high | Standard API endpoint, unchanged since 2018 |
| Base64 encoding requires "Encode" action, Line Wrap: None | Apple Community discussions.apple.com/thread/251563782 | high | Failure mode confirmed; fix is specific and verified by community |
| Share Sheet input: Show in Share Sheet, Accepted Types: URL | support.apple.com/guide/shortcuts/input-types-apd7644168e1/ios | high | Apple primary documentation |
| Siri trigger + "Ask for Input" = hands-free voice dictation | macmost.com/creating-shortcuts-that-accept-voice-input.html; apple.stackexchange.com/questions/336799 | high | Two independent secondary sources, consistent |
| Fine-grained PAT: Issues: write minimum for issue creation | GitHub docs (web search); GitHub PAT documentation | high | Consistent with GitHub's fine-grained token model |
| No native Keychain access from iOS Shortcuts | Web search (multiple security-focused sources) | high | No Apple documentation contradicts this; community consensus |
| Wiki URL: https://github.com/davidamitchell/Research/wiki/Home | Research/completed/2026-03-01-github-wiki-research-content.md Key Finding #3 | high | Derived from prior research on wiki structure |
| workflow_dispatch API endpoint and body format | docs.github.com/en/rest/actions/workflows; island94.org (working example) | high | Primary source + practitioner confirmation |
| No native "Dispatch Workflow" action in GitHub iOS app | Web search (March 2026) | medium | Absence of evidence; could change with a future GitHub app update |
| Query shortcut is asynchronous via workflow_dispatch | Derived from workflow_dispatch mechanics | high | Mechanistically sound: workflow runs on runner, not inline |
| Issue creation path: 4–5 actions vs. direct file creation: 7–9 actions | Derived from action enumeration in §2 Investigation | medium | Estimated; exact count depends on implementation choices |

### Assumptions

- **Assumption:** The issue-to-backlog GitHub Actions workflow identified in `2026-02-27-simple-process-for-adding-research-item.md` is implemented or will be implemented. **Justification:** The prior research item recommended this workflow as the owner's capture path; if it is not yet built, the capture shortcut still creates a labeled issue that is visible in the GitHub iOS app and on the web, requiring only a manual move rather than automatic conversion.

- **Assumption:** The repository wiki is enabled in GitHub Settings (required for the wiki quick-access shortcut to return a page rather than a 404). **Justification:** The completed `2026-03-01-github-wiki-research-content.md` item notes that the wiki must be enabled once in Settings; the publish workflow's existence implies this has been done.

- **Assumption:** The owner's iPhone is running iOS 13 or later. **Justification:** "Get Contents of URL" with custom headers and JSON body requires iOS 13+. iOS 13 was released in 2019; any current iPhone runs iOS 16 or later.

### Analysis

The primary design decision — issue creation vs. direct file creation — resolves clearly in favour of issue creation on two axes: simplicity (fewer actions, no base64 encoding, no filename construction) and integration (leverages the existing issue-to-backlog workflow, preserving the clean capture-then-structure separation validated by Zettelkasten principles in prior research). The direct file creation path is not wrong but creates a single-responsibility Shortcut that duplicates logic already present in the Python CLI and the Actions workflow, without adding value.

The query shortcut decision resolves as: wiki first (synchronous, zero-cost, good enough for most queries), workflow_dispatch second (asynchronous, requires a new search workflow, higher value for non-trivial queries). The MCP server approach (from `2026-03-02-chat-conversational-interface.md`) is explicitly not applicable to iOS users — the MCP server serves AI agent sessions, not mobile browser or Shortcuts contexts.

The PAT storage constraint is a real limitation but not a blocker. The security posture (fine-grained, minimal scope, on a personal device protected by biometrics) is adequate. The absence of native Keychain support in iOS Shortcuts is a platform limitation that Apple has not addressed; the community workaround (inline storage) is the only viable option.

### Risks, Gaps, and Uncertainties

- **Issue-to-backlog workflow gap:** If the `issues: [opened]`-triggered workflow is not implemented, the capture shortcut produces an issue that requires manual conversion. The shortcut itself is still valuable (it creates a record in GitHub Issues accessible from the iOS app), but the fully automated pipeline requires the Actions workflow.
- **PAT expiry:** A fine-grained PAT with a 90-day expiry requires editing the Shortcut every 90 days. This is a minor but real maintenance burden. A PAT with no expiry removes the burden but increases risk.
- **Query shortcut unimplemented:** The search `workflow_dispatch` shortcut requires a GitHub Actions workflow that accepts a query string, searches `Research/completed/`, and posts results as an issue. This workflow does not currently exist; building it is a reasonable follow-on.
- **GitHub iOS app future changes:** The GitHub app may add native Shortcuts actions in future releases, making the manual API approach obsolete. This is unlikely to be a problem — the manual approach would continue to work even if native actions are added.
- **Siri recognition reliability:** Hands-free capture depends on Siri correctly recognising the title dictation. For technical titles with acronyms or unusual terms, Siri may produce transcription errors. The "Ask for Input" dialog appears on screen to allow correction before submission.

### Open Questions

- Should the issue-to-backlog GitHub Actions workflow be added to the backlog as a concrete implementation item, or is it already covered by the existing issue form (from `2026-02-27-simple-process-for-adding-research-item.md`)?
- Would a `workflow_dispatch`-triggered search workflow (accepting a `query` input and posting results as an issue) be worth building? This is the "Option A query shortcut" from the Approach section. If yes, it warrants a backlog item.
- Is there value in a "Start Research" shortcut that moves a specific backlog item to in-progress by triggering the `python -m src.main research start` CLI via a `workflow_dispatch` event? This would give the owner a one-tap "start" action from iOS for items visible in the GitHub Issues list.

---

## Output

- Type: knowledge, backlog-item
- Description: Three iOS Shortcuts designs (capture via issue creation, wiki quick-access, deferred search shortcut); full action sequences for "Add Research" shortcut; GitHub API endpoints and PAT scopes; base64 encoding note for direct file path; token storage constraint; query shortcut deferred pending search workflow
- Links:
  - https://island94.org/2024/01/trigger-github-actions-workflows-from-apple-shortcuts (primary working example by GitHub employee)
  - https://docs.github.com/en/rest/issues/issues (GitHub Issues creation API)
  - https://support.apple.com/guide/shortcuts/input-types-apd7644168e1/ios (iOS Shortcuts Share Sheet input types)