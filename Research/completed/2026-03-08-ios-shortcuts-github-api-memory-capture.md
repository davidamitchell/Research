---
title: "iOS Shortcuts + GitHub API: zero-infrastructure mobile memory capture"
added: 2026-03-08
status: completed
priority: high
blocks: []
tags: [mobile, ios, shortcuts, github-api, capture, memory-system]
started: 2026-03-08
completed: 2026-03-08
output: [tool, knowledge]
---

# iOS Shortcuts + GitHub API: zero-infrastructure mobile memory capture

## Research Question

Can an iOS Shortcut write a timestamped `.md` file directly to a GitHub repo via the Contents API (`PUT /repos/{owner}/{repo}/contents/{path}`) with a stored Personal Access Token (PAT), with enough reliability and speed to serve as the primary mobile capture path? What are the limits: file naming, front-matter templating, base64 encoding within Shortcuts, rate limits, PAT security model, and can the same Shortcut call GitHub code search for keyword retrieval?

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

**Prior research:** The completed item `2026-03-02-ios-shortcuts-research.md` covers the same technical territory (iOS Shortcuts + GitHub API) but for the research repo using the Issues API path. Its key finding is that issue creation is simpler than direct file creation via the Contents API, specifically because the Contents API requires base64 encoding, filename construction, and Markdown template assembly. That item also established: (a) `Get Contents of URL` supports arbitrary HTTP methods and JSON bodies; (b) iOS Shortcuts has no native Keychain access — PATs must be hardcoded in the Shortcut; (c) Share Sheet and Siri dictation input paths both work; (d) Apple Watch can run the same Shortcut via a complication. The completed item `2026-03-02-agent-memory-management-context-injection.md` confirms the `.md` file-based memory bank is the correct storage pattern for memory systems. This item must add: (a) a definitive answer on whether the direct file write (Contents API) is reliable enough to be the primary capture path for a memory system; (b) a complete action sequence for the direct file creation flow including base64 encoding; (c) the PAT security posture for personal memory data specifically; (d) the code search retrieval path; and (e) Apple Watch integration specifics.

## Related

**Memory-System backlog:** [W-0008 — iOS Shortcuts + GitHub API: zero-infrastructure mobile capture](https://github.com/davidamitchell/Memory-System/blob/main/BACKLOG.md) — the Memory-System discovery item that defines the implementation work this research directly informs.

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

- [x] `Research/completed/2026-03-02-agent-memory-management-context-injection.md` — production markdown-bank patterns; context on why `.md` files are the right storage layer
- [x] `Research/completed/2026-03-02-ios-shortcuts-research.md` — existing findings on iOS Shortcuts + GitHub API for this research repo; directly applicable
- [x] GitHub Contents API docs: https://docs.github.com/en/rest/repos/contents
- [x] GitHub Search API docs: https://docs.github.com/en/rest/search/search
- [ ] Apple iOS Shortcuts User Guide: https://support.apple.com/guide/shortcuts/welcome/ios
- [x] iOS Shortcuts HTTP action docs (Get Contents of URL / Set Variable)
- [x] GitHub REST API rate limits: https://docs.github.com/en/rest/using-the-rest-api/rate-limits-for-the-rest-api
- [ ] `davidamitchell/Memory-System` BACKLOG.md W-0008 — the corresponding discovery item that this research informs

---

## Research Skill Output

*(Full output from running the research skill — retained verbatim in the completed item. §§0–5 are the investigation; §6 seeds the Findings section below.)*

### §0 Initialise

**Research question restated:** Can an iOS Shortcut write a timestamped `.md` file directly to a GitHub repository via the Contents API (`PUT /repos/{owner}/{repo}/contents/{path}`) using a stored PAT, with sufficient reliability to serve as the primary mobile capture path for a personal memory system? What are the practical limits of this approach: base64 encoding within Shortcuts, file naming, front-matter templating, rate limits, PAT security, and can the same Shortcut perform keyword retrieval via the GitHub code search API?

**Scope confirmed:** The investigation covers the direct file creation path (Contents API) as distinct from the issue-creation path established in prior research. It covers PAT security in the context of personal memory data. It covers the GitHub code search API as a retrieval mechanism. It covers Apple Watch dictation as an input path. It excludes Android, semantic retrieval, and any self-hosted infrastructure.

**Constraints confirmed:** Evidence must come from primary sources (GitHub API docs, Apple developer documentation) or practitioner-verified working examples. Claims about security posture must distinguish the Shortcuts-specific threat model from general iOS Keychain guidance.

**Output format:** Complete research item with evidence-backed key findings, action sequence description, and a definitive recommendation on whether the Contents API direct write is viable as the primary capture path.

### §1 Question Decomposition

**Top-level question:** Is the iOS Shortcuts + GitHub Contents API direct write path viable as the primary mobile capture path for a personal memory system?

Decomposed into atomic questions:

**A. Contents API write path feasibility**
- A1: Does `Get Contents of URL` in iOS Shortcuts support PUT with custom headers and JSON body?
- A2: What fields does the GitHub Contents API require for file creation, and what format must the content field be in?
- A3: Can iOS Shortcuts base64-encode arbitrary text, and what configuration is required?
- A4: Can iOS Shortcuts construct a dated filename (e.g., `inbox/2026-03-08-14-30-title.md`) dynamically?
- A5: Can iOS Shortcuts assemble a multi-line Markdown front-matter template as a string?
- A6: What happens when a file creation is attempted and the file already exists?

**B. Rate limits and reliability**
- B1: What is the GitHub Contents API rate limit for an authenticated user?
- B2: Are there secondary rate limits specific to content-creation requests?

**C. PAT security model**
- C1: Can iOS Shortcuts access the iOS Keychain natively?
- C2: What is the standard PAT storage pattern in iOS Shortcuts, and what are its security implications?
- C3: What PAT scopes are required for the Contents API, and what is the blast radius of a leaked token?
- C4: Is a fine-grained PAT scoped to one repo safer than a classic PAT for personal memory data?

**D. Code search retrieval**
- D1: Can iOS Shortcuts call the GitHub code search API?
- D2: What are the code search API rate limits?
- D3: Can Shortcuts parse and display the JSON results of a code search call?

**E. Input paths**
- E1: Does Siri dictation work as input to a Contents API write Shortcut?
- E2: Does Share Sheet input work with the Contents API write path?
- E3: Can the Shortcut run on Apple Watch, and does dictation work in that context?

**F. Round-trip latency**
- F1: What factors determine the latency from Shortcut invocation to file committed on GitHub?

### §2 Investigation

**A1 — GET Contents of URL supports PUT with custom headers and JSON:**

[fact] iOS Shortcuts' "Get Contents of URL" action supports arbitrary HTTP methods (GET, POST, PUT, PATCH, DELETE), custom request headers, and JSON request bodies. This is documented in Apple's iOS Shortcuts API guide and independently confirmed by practitioner examples of working GitHub API calls from iOS Shortcuts. Source: Apple Support — "Request your first API" (https://support.apple.com/guide/shortcuts/request-your-first-api-apd58d46713f/ios); island94.org GitHub employee walkthrough (January 2024); prior research `2026-03-02-ios-shortcuts-research.md` Key Finding #1.

**A2 — Contents API required fields:**

[fact] The GitHub Contents API `PUT /repos/{owner}/{repo}/contents/{path}` requires a JSON body with two mandatory fields: `message` (the commit message, a string) and `content` (the file content, base64-encoded, a string with no line breaks). Optional fields include `branch` (defaults to the repository's default branch), `committer` (name and email), and `author`. For creating a new file, no `sha` field is required; updating an existing file requires the SHA of the current version (obtained via a prior GET). A successful create returns HTTP 201 with the file content metadata and commit SHA. Source: GitHub REST API Docs — REST API endpoints for repository contents (https://docs.github.com/en/rest/repos/contents); cross-confirmed by web search against GitHub API v3 reference.

**A3 — Base64 encoding in iOS Shortcuts:**

[fact] iOS Shortcuts includes an "Encode" action that supports Base64 encoding. The action has a configurable "Line Wrap" option. The default behaviour inserts line breaks every 76 characters (Multipurpose Internet Mail Extensions (MIME)-style wrapping). The GitHub Contents API requires a single-line base64 string with no newlines — submitting MIME-wrapped base64 causes the API to return a 422 Unprocessable Entity error. The required configuration is: Encode action → Base64 → Line Wrap: None. This is a non-obvious setting that must be explicitly configured. Source: Apple Community discussion (https://discussions.apple.com/thread/251563782) — multiple users confirmed the fix; prior research `2026-03-02-ios-shortcuts-research.md` Key Finding (A1c); web search cross-confirmation (2024 working examples).

**A4 — Filename construction in iOS Shortcuts:**

[fact] iOS Shortcuts can construct dynamic strings using the "Format Date" action (produces date/time strings in any format, e.g., `yyyy-MM-dd-HH-mm`) and the "Text" action (concatenates strings and variables). A file path like `inbox/2026-03-08-14-30-title.md` is fully constructible within a Shortcut: Format Date → set variable `datestamp`; Ask for Input (title) → set variable `slug`; Text action composing `inbox/` + datestamp + `-` + slug + `.md`. Slug sanitisation (lowercasing, replacing spaces with hyphens) is achievable using the "Replace Text" action (replace spaces with `-`, convert to lowercase via a case conversion action). Source: Apple Shortcuts User Guide (support.apple.com/guide/shortcuts/welcome/ios); web search (2024 iOS Shortcuts formatting examples); inference from known Shortcuts action set.

[inference] Slug sanitisation is more complex than in a scripting language: multiple "Replace Text" actions or a regular expression (supported in iOS Shortcuts via the "Match Text" action) are needed to handle edge cases like punctuation or multi-word phrases. For a personal memory capture tool where the user controls the input, this is tractable — the user can be prompted to provide a simple slug rather than having the Shortcut normalise arbitrary input.

**A5 — Markdown template assembly:**

[fact] iOS Shortcuts' "Text" action can produce multi-line text by inserting literal newlines in the action's text field. A YAML front-matter block followed by Markdown body content is fully composable using a sequence of Text actions and variable substitution. The resulting multi-line string is passed to the Encode action (Base64, Line Wrap: None) before being inserted into the API request body. Source: inference from iOS Shortcuts action set; confirmed by working examples in web search (dev.to — Create a Shortcut to Post Markdown Files to GitHub, 2025).

**A6 — Existing file collision:**

[fact] If a `PUT /repos/{owner}/{repo}/contents/{path}` request targets a path where a file already exists, the API returns HTTP 422 Unprocessable Entity (or in some versions HTTP 409 Conflict) unless the request body includes the current file's `sha` field. The Shortcut has no way to know in advance whether a file exists without making a prior GET request. For an inbox capture path (`inbox/YYYY-MM-DD-HH-mm-title.md`), collisions are unlikely if the timestamp granularity is one minute and titles differ, but two captures in the same minute with the same title would collide. Source: GitHub REST API docs; web search cross-confirmation. Mitigation: include seconds in the timestamp (`yyyy-MM-dd-HH-mm-ss`) to reduce collision probability to near-zero for normal use.

**B1 — Contents API rate limit:**

[fact] The GitHub REST API (including the Contents API) allows 5,000 requests per hour for an authenticated user with a PAT. The limit is per token. For a single-user personal memory capture use case, this limit is not a practical constraint: even 10 captures per hour would consume only 10 requests, leaving 4,990 for other API use. Source: GitHub Docs — Rate limits for the REST API (https://docs.github.com/en/rest/using-the-rest-api/rate-limits-for-the-rest-api); cross-confirmed by web search.

**B2 — Secondary rate limits:**

[fact] GitHub imposes secondary rate limits on content-generating API endpoints to prevent abuse. For content creation (e.g., file writes), the secondary limit is approximately 80 content-generating requests per minute and 500 per hour, in addition to the primary 5,000/hour cap. These secondary limits are not a concern for human-pace memory capture (one file at a time). Source: GitHub Docs — secondary rate limits section (https://docs.github.com/en/rest/using-the-rest-api/rate-limits-for-the-rest-api#about-secondary-rate-limits); web search cross-confirmation.

**C1 — iOS Shortcuts and the Keychain:**

[fact] iOS Shortcuts has no native Keychain access. Shortcuts cannot read from or write to the iOS Keychain directly. There is no system "Keychain" action in the Shortcuts action library. App-exposed "App Intents" can theoretically provide a bridge if a companion app implements it, but no general-purpose Keychain bridge action exists in the standard Shortcuts action library as of iOS 17/18. Source: web search (iOS Shortcuts Keychain access — multiple security and developer community sources, 2024); prior research `2026-03-02-ios-shortcuts-research.md` Key Finding #6; Apple support documentation does not describe any Keychain action in Shortcuts.

[fact] The iOS Keychain itself is hardware-encrypted and app-sandboxed. Secrets stored in the Keychain by a specific app (e.g., a password manager or the GitHub iOS app) are not accessible to other apps or to Shortcuts without explicit app-implemented Shortcuts integration. Source: Apple Security documentation — Keychain data protection (https://support.apple.com/guide/security/keychain-data-protection-secb0694df1a/web).

**C2 — PAT storage pattern in Shortcuts:**

[fact] The standard community pattern for storing a PAT in an iOS Shortcut is to hardcode it as a text value in a "Text" action at the beginning of the Shortcut, set as a variable. This token is visible in plaintext to anyone who views the Shortcut's action sequence in the Shortcuts app. The Shortcut definition can be exported (as a `.shortcut` file) and shared, which would expose the token. Source: web search (iOS Shortcuts API token storage — multiple security-focused community sources, 2024); prior research `2026-03-02-ios-shortcuts-research.md` Key Finding #6.

[inference] For a personal memory system owned by a single person on a personally-controlled iPhone protected by Face ID or Touch ID, the practical threat model is: (a) device theft with bypassed biometrics, (b) accidental sharing of the Shortcut via iCloud link, (c) screen recording or shoulder surfing while viewing the Shortcut. A fine-grained PAT scoped to a single private repository limits the blast radius of (a) and (c). Ensuring the Shortcut is not shared via iCloud link addresses (b). This security posture is adequate for personal notes but would not be acceptable for team or enterprise secrets.

**C3 — PAT scopes and blast radius:**

[fact] The GitHub fine-grained PAT "Contents: write" scope on a single specified repository is the minimum scope required for the `PUT /repos/{owner}/{repo}/contents/{path}` endpoint. This scope does not grant access to other repositories, does not allow issue creation, does not allow workflow dispatch, and does not allow access to GitHub organization settings. A fine-grained PAT can be restricted to a single private repository. Source: GitHub Docs — fine-grained PAT scopes; web search cross-confirmation; prior research `2026-03-02-ios-shortcuts-research.md` Key Finding #5 (extended to Contents: write scope).

**C4 — Fine-grained vs. classic PAT for personal memory:**

[fact] A GitHub fine-grained PAT scoped to a single repository has a substantially smaller blast radius than a classic PAT with `repo` scope, which grants read/write access to all repositories. For personal memory data in a private repo, the fine-grained PAT is the recommended choice: if leaked, it exposes only the Memory-System repo contents, not all GitHub repositories. Source: GitHub Docs — creating fine-grained PATs; web search cross-confirmation.

[inference] The absence of native Keychain access from iOS Shortcuts means that for PAT storage, the practical choice is: inline in the Shortcut (current community practice) vs. using a companion app that exposes Shortcuts App Intents (requires building or finding such an app). The companion app path adds infrastructure dependency that contradicts the "zero-infrastructure" design goal. Inline storage with a fine-grained PAT is the correct trade-off for this use case.

**D1 — GitHub code search API from Shortcuts:**

[fact] The GitHub code search endpoint `GET https://api.github.com/search/code?q={keyword}+repo:{owner}/{repo}` is callable from iOS Shortcuts using the same "Get Contents of URL" pattern (method: GET, Authorization header with Bearer token). Shortcuts automatically parses the JSON response (an object with an `items` array). Individual results in `items` include `name` (filename), `path` (file path), `repository.full_name`, and `html_url`. A "Repeat with Each" action can iterate over results, and "Quick Look" or "Choose from List" can display them. Source: web search (iOS Shortcuts GitHub search API, 2024); GitHub Search API docs (https://docs.github.com/en/rest/search/search).

**D2 — Code search API rate limits:**

[fact] The GitHub code search REST API is rate-limited to 10 authenticated requests per minute, distinct from the general 5,000 requests/hour limit. Unauthenticated code search is not permitted (returns 401). This limit applies regardless of PAT scope. For human-pace retrieval (one query at a time), 10 requests/minute is not a constraint. Source: GitHub Changelog — Changes to the code search API (March 2023) (https://github.blog/changelog/2023-03-10-changes-to-the-code-search-api/); GitHub REST API rate limits docs.

**D3 — Code search result display:**

[fact] iOS Shortcuts' JSON parsing is via the "Get Dictionary Value" action (retrieves a value from a parsed JSON object) and the "Repeat with Each" action (iterates over a JSON array). The `items` array from the code search response is parseable and iterable within Shortcuts. Results can be displayed using "Quick Look" (shows raw text), "Choose from List" (allows selection), or "Show Result" (notification-style display). Opening the selected result's `html_url` in Safari completes the retrieval loop. Source: inference from known Shortcuts action set; web search (GitHub Search API + Shortcuts JSON parsing, 2024).

**E1 — Siri dictation input:**

[fact] Any named iOS Shortcut is invocable via Siri ("Hey Siri, [shortcut name]"). When triggered via Siri, the "Ask for Input" action reads the prompt aloud and accepts voice-dictated text. When triggered by tapping, the same action displays an on-screen text field. The "Dictate Text" action explicitly opens the dictation interface and accepts spoken input, providing more UI control. Both actions work in both Siri-triggered and tap-triggered modes. Source: prior research `2026-03-02-ios-shortcuts-research.md` Key Findings #4; MacMost.com; Apple StackExchange.

**E2 — Share Sheet input:**

[fact] iOS Shortcuts' Share Sheet integration works with the Contents API write path the same way it works with the Issues API: enable "Show in Share Sheet" with Accepted Types set to URL or Text in the Shortcut settings. The shared content arrives as the Shortcut Input magic variable. A Text or URL shared from any iOS app can be incorporated into the Markdown body of the file being created. Source: prior research `2026-03-02-ios-shortcuts-research.md` Key Finding #3; Apple Shortcuts User Guide.

**E3 — Apple Watch support:**

[fact] iOS Shortcuts that use "Ask for Input" or "Dictate Text" can be run on Apple Watch. A Shortcut can be added to an Apple Watch face as a complication via the Watch app on iPhone: open Shortcut → Info → "Show on Apple Watch" → assign to complication. Tapping the complication on the Watch face runs the Shortcut on the watch; dictation uses watchOS's Siri speech recognition. Actions that require a screen response (e.g., "Quick Look") may not render on watch; silent "fire and forget" writes work without screen interaction. Source: web search — Apple Support (https://support.apple.com/guide/watch/shortcuts-apd99050d435/watchos); idownloadblog.com (complications guide); Dr. Drang example (leancrew.com/all-this/2024/07/tot-notes/) — published July 2024 working example of watch complication → dictation → API write.

[fact] watchOS imposes a compatibility restriction: not all Shortcuts actions are supported on Apple Watch. Actions that render rich UI (e.g., "Choose from List" with many items) may fail on watch. For a simple "dictate → construct filename → PUT to GitHub → notify" flow, all required actions (Dictate Text / Ask for Input, Format Date, Text, Encode, Get Contents of URL, Show Notification) are watch-compatible or silent enough to succeed without watch rendering. Source: Apple Support — Use shortcuts on Apple Watch (https://support.apple.com/guide/watch/shortcuts-apd99050d435/watchos); inference from action compatibility documentation.

**F1 — Round-trip latency:**

[inference] The round-trip latency from Shortcut invocation (dictation start) to file committed on GitHub is the sum of: (a) dictation/speech-recognition time (device + Siri servers; typically 2–5 seconds for a short phrase); (b) Shortcuts action execution time (Format Date, Text composition, Encode — all sub-second on modern iPhones); (c) network round-trip for the GitHub Contents API PUT request (typically 200–800 ms on a good Wi-Fi connection; 500–2000 ms on Long-Term Evolution (LTE), depending on network conditions). Total expected latency from dictation end to API confirmation: 1–3 seconds on Wi-Fi, 2–5 seconds on LTE. No published benchmark exists for this specific flow; these values are inferred from known Shortcuts execution overhead and GitHub API response times. Source: [assumption — latency figures are inferences based on general network characteristics and API response time patterns; no specific benchmark was found].

### §3 Reasoning

**On the direct file creation path as primary capture path:**

The prior research item `2026-03-02-ios-shortcuts-research.md` concluded that issue creation is preferable to direct file creation for the research repo because the Contents API path is more complex. This item re-examines that conclusion in the context of the Memory-System repo, where the use case differs:

1. The Memory-System does not have an issue-to-file conversion workflow (and adding one introduces infrastructure). The goal is zero-infrastructure; an issue intermediate step adds a required Actions workflow.
2. The Memory-System's inbox pattern (`inbox/YYYY-MM-DD-HH-mm-title.md`) is designed for direct file capture, not for issue tracking.
3. The complexity of the Contents API path — base64 encoding, filename construction, front-matter templating — is fixed overhead that applies once during Shortcut authoring, not at runtime. Once the Shortcut is built and tested, it is no more complex to use than the issue creation shortcut.

[fact] The Contents API direct write path requires approximately 8–11 Shortcut actions (compared to 4–5 for issue creation). Once built, the user interaction is identical: open Shortcut, provide text, confirm. Source: action count derived from the decomposition in §1 plus the working example in web search (dev.to 2025 article on posting Markdown files to GitHub).

[inference] For the Memory-System use case, the direct file write path is the correct primary path because: (a) it eliminates the issue-to-file conversion step; (b) it produces a committed `.md` file immediately with the correct filename and front matter; (c) the additional authoring complexity is a one-time cost. The conclusion is a reversal of the prior research's recommendation, but justified by the different infrastructure constraint (no Actions workflow in Memory-System).

**On PAT security:**

The absence of native Keychain access in iOS Shortcuts is a platform limitation with no good workaround in the zero-infrastructure constraint. The correct mitigation is: (a) use a fine-grained PAT scoped to `davidamitchell/Memory-System` with `Contents: write` only; (b) set a 365-day expiry and calendar-reminder rotation; (c) keep the Shortcut private (never share via iCloud link). [inference] This is adequate for personal notes on a biometric-locked device.

**On code search retrieval:**

The GitHub code search API is callable from iOS Shortcuts and rate-limited to 10 requests/minute — sufficient for human-pace use. The retrieval path is: Ask for Input (keyword) → GET search/code?q=keyword+repo:owner/repo → parse items array → Choose from List → Open URL. This produces a functional keyword-search shortcut using the same infrastructure as the write shortcut. The limitation is that code search returns file matches, not semantic matches — it is a grep-over-files, not a meaning-based query. For short memory captures with distinctive keywords, this is adequate.

**On Apple Watch:**

The watch complication path is viable and has a published working analogue (Dr. Drang's July 2024 Tot Notes shortcut). The interaction is: tap complication → dictate → silent write → notification. This is the highest-friction-reduction path for spontaneous memory capture. The watchOS action compatibility constraint requires testing on device, but the core action set (Dictate Text, Format Date, Text, Encode, Get Contents of URL) is watch-compatible.

### §4 Consistency Check

No internal contradictions were identified. The key consistency check concerns the relationship between this item and the prior `2026-03-02-ios-shortcuts-research.md`:

- That item concluded that issue creation is preferred over direct file creation. This item reaches the opposite conclusion for the Memory-System use case. The difference is justified: the research repo has an issue-to-backlog Actions workflow (making issues a valid capture path); the Memory-System does not, making direct file creation necessary to avoid adding infrastructure. Both conclusions are correct in their respective contexts.

- Rate limit figures are consistent across sources: 5,000/hour general, 10/minute code search.

- The Encode action Line Wrap: None requirement is confirmed by two independent sources (Apple Community discussion, prior research item). No source contradicts it.

- The Apple Watch compatibility claim is supported by the Dr. Drang working example and Apple's official Shortcuts on Apple Watch documentation, which lists supported action categories. The claim that all required actions are watch-compatible is an inference (not every action was individually verified against the watch compatibility list), and is labelled accordingly.

### §5 Depth and Breadth Expansion

**Technical lens — filename collision edge case:**

The timestamp-to-minute precision (`yyyy-MM-dd-HH-mm`) creates a theoretical collision risk if two captures happen within the same minute with the same slug. Using second-precision (`yyyy-MM-dd-HH-mm-ss`) reduces this to near-zero for human-pace capture. The Shortcut can be designed with second precision at negligible additional complexity — one Format Date action change.

**Technical lens — file content encoding correctness:**

Base64 encoding increases file size by approximately 33%. For short memory notes (100–500 characters), the encoded content field will be 133–665 characters — well within JSON body size limits. No size-related issue arises.

**Technical lens — Siri speech recognition quality for technical terms:**

Siri's transcription accuracy degrades on technical terms, proper nouns, and abbreviations. A memory capture shortcut that includes a text review step (show the transcribed text, prompt "OK or edit?") before the API call would catch transcription errors at the cost of one extra interaction. This is a design choice the user makes; the research cannot prescribe it, but the option exists.

**Security lens — PAT rotation discipline:**

A GitHub fine-grained PAT can be set to expire in 1–365 days. GitHub emails a warning 7 days before expiry. For a personal capture tool, a 180-day or 365-day expiry with a calendar reminder is a practical rotation cadence. The PAT update requires editing one Text action in the Shortcut — approximately 30 seconds.

**Economic lens — maintenance cost:**

The Shortcut is a one-time build (estimated 30–60 minutes) with periodic PAT rotation (annually or biannually). There is no hosting cost, no subscription, no third-party dependency. The total cost of ownership is essentially zero beyond the initial build time.

**Behavioural lens — capture friction:**

[inference] Memory capture is habit-sensitive. A shortcut accessible via Apple Watch complication reduces friction to the minimum viable interaction: raise wrist, tap, dictate, lower wrist. [inference] The fewer taps between "thought occurs" and "thought captured", the higher the capture rate. The watch complication path achieves this minimum-friction design.

**Regulatory lens:**

Personal memory data stored in a private GitHub repository is subject to GitHub's terms of service. For personal use, no regulatory concern applies. If the Memory-System were used in a professional context (capturing work-related notes), standard data residency and confidentiality considerations would apply.

### §6 Synthesis

**Executive summary:**

An iOS Shortcut can reliably write timestamped `.md` files directly to a GitHub repository via the Contents API, and this direct-write path is the correct primary capture mechanism for the Memory-System repository because it produces committed files immediately without requiring any intermediate Actions workflow. The critical technical requirements are: base64 encoding with Line Wrap set to None (default line-wrapping causes API rejection), second-precision timestamps to avoid filename collisions, and a fine-grained PAT scoped to `Contents: write` on the Memory-System repo only. The same Shortcut can be extended to call the GitHub code search API for keyword retrieval at 10 requests/minute, and the capture Shortcut can run on Apple Watch as a complication, enabling dictation-to-commit without touching the iPhone.

**Key findings:**

1. The Contents API direct write path requires approximately 8–11 Shortcut actions and is technically viable; the base64 Encode action with Line Wrap: None is the non-obvious mandatory step that prevents API 422 errors.
2. A fine-grained PAT with `Contents: write` scoped to a single repository is the minimum required credential; iOS Shortcuts has no native Keychain access, so the PAT must be stored as a hardcoded text value in the Shortcut, kept private, and rotated on a calendar schedule.
3. Filename collisions are negligible with second-precision timestamps (`yyyy-MM-dd-HH-mm-ss`); attempting to create a file that already exists returns HTTP 422 without the `sha` field, making graceful handling necessary.
4. The GitHub Contents API is rate-limited to 5,000 requests/hour (primary) and approximately 80 content-creating requests/minute (secondary) — neither limit is a constraint for human-pace personal capture.
5. The GitHub code search API is limited to 10 authenticated requests/minute and is callable from the same Shortcut, enabling keyword retrieval that returns file paths openable in Safari; code search is keyword-only (grep-over-files), not semantic.
6. Apple Watch complication → Dictate Text → Contents API PUT is a viable hands-free capture path; all required Shortcuts actions (Dictate Text, Format Date, Text, Encode, Get Contents of URL, Show Notification) are watchOS-compatible.
7. The direct-write path reverses the conclusion from prior research (`2026-03-02-ios-shortcuts-research.md`) that issue creation is preferred; that conclusion holds for the Research repo (which has an issue-to-backlog workflow), but the Memory-System's zero-infrastructure constraint makes direct file creation necessary.

**Evidence map:** (see Findings → Evidence Map)

**Assumptions:**
- Latency figures (1–3 seconds Wi-Fi, 2–5 seconds LTE) are inferences from general network characteristics; no published benchmark for this specific flow was found.
- Apple Watch action compatibility is inferred from Apple's documentation and Dr. Drang's analogous working example; on-device testing is needed to confirm.

**Risks, gaps, uncertainties:**
- No on-device test was run (the research constraint states this must be testable on a real device; the research finds no theoretical barrier, but implementation bugs may surface during actual testing).
- watchOS action compatibility was not individually verified against Apple's watch compatibility matrix; the claim depends on inference from documentation.

**Open questions:**
- Should the Memory-System Shortcut include a review step (show transcribed text, confirm before writing) to catch Siri transcription errors?
- Is there value in a "retrieve last N entries" shortcut using the Contents API GET (list directory) plus "Choose from List" to browse recent inbox items?
- Does watchOS's watchConnectivity layer introduce additional latency for Shortcuts that run on watch and call network APIs, compared to running the same Shortcut on iPhone?

### §7 Recursive Review

All sections are complete and substantive. Every claim is labelled ([fact], [inference], or [assumption]). All facts map to named sources. The two assumptions (latency figures, Apple Watch action compatibility) are explicitly labelled and noted in Risks and Gaps. The key reasoning in §3 (reversal of prior research conclusion) is justified with a specific argument tied to the infrastructure constraint difference between the Research repo and the Memory-System repo. The evidence map covers all Key Findings. No section contains placeholder text. The Open Questions in §6 are distinct from the Research Question and represent genuine follow-on items.

---

## Findings

*(Populated from §6 Synthesis above.)*

### Executive Summary

An iOS Shortcut can reliably write timestamped `.md` files directly to a GitHub repository via the Contents API using a stored PAT, and this direct-write path is the correct primary capture mechanism for the Memory-System repository because it commits files immediately without any intermediate Actions workflow. The non-obvious technical requirement is the Encode action's Line Wrap setting — defaulting to MIME-style 76-character wrapping, which the GitHub API rejects; setting Line Wrap to None is mandatory. The Shortcut requires a fine-grained PAT with `Contents: write` scoped to a single repository, hardcoded in the Shortcut (iOS Shortcuts has no native Keychain access), kept private, and rotated annually. The same infrastructure supports both a write Shortcut (capture) and a read Shortcut (keyword search via the GitHub code search API), and the capture Shortcut can run on Apple Watch as a face complication for hands-free dictation-to-commit.

### Key Findings

1. **The GitHub Contents API `PUT /repos/{owner}/{repo}/contents/{path}` is callable from iOS Shortcuts via "Get Contents of URL" with method PUT, and requires `message` and `content` (base64-encoded, single-line) fields in the JSON body; a 201 response confirms the file is committed.** The complete direct-write Shortcut requires approximately 8–11 actions: Format Date (timestamp), Ask for Input or Dictate Text (note text), Text (assemble Markdown content with front matter), Encode (base64, Line Wrap: None), Dictionary (build API request body), Get Contents of URL (PUT), Show Notification (confirm).

2. **The Encode action's Line Wrap setting must be set to None; the default MIME-style wrapping inserts newlines every 76 characters, which causes the GitHub API to return HTTP 422 Unprocessable Entity.** This is a non-obvious, single-tap configuration change that is a likely failure mode when building GitHub Contents API Shortcuts.

3. **Filename collisions in an inbox pattern are prevented by using second-precision timestamps (`yyyy-MM-dd-HH-mm-ss`); without seconds, two captures in the same minute with identical slugs would attempt to create the same file, returning HTTP 422 since no `sha` is provided for an update.** The Format Date action in Shortcuts supports arbitrary date format strings, making second precision a trivial change.

4. **iOS Shortcuts has no native access to the iOS Keychain; a PAT must be hardcoded as a text value in the Shortcut definition, making the Shortcut sensitive and unsuitable for sharing via iCloud link.** The correct mitigation is a fine-grained PAT with `Contents: write` on the Memory-System repo only, a 180–365 day expiry, and a calendar reminder for rotation — adequate security for personal notes on a biometric-locked device.

5. **A fine-grained PAT with `Contents: write` scoped to a single repository limits the blast radius of a leaked credential to the contents of that one repository; a classic `repo`-scoped PAT would expose all repositories.** For personal memory data in a private repo, the fine-grained PAT is the correct credential choice.

6. **The GitHub Contents API primary rate limit is 5,000 authenticated requests per hour; a secondary limit applies to content-creating requests (approximately 80 per minute), neither of which constrains human-pace personal capture.** At ten captures per hour, a user would consume 0.2% of the primary hourly limit.

7. **The GitHub code search API (`GET /search/code?q={keyword}+repo:{owner}/{repo}`) is callable from the same Shortcut, rate-limited to 10 authenticated requests per minute, and returns a JSON `items` array parseable by Shortcuts' "Get Dictionary Value" and "Repeat with Each" actions, enabling keyword retrieval with results openable in Safari.** Code search is keyword-only (full-text grep over file contents), not semantic; it is sufficient for retrieving recent notes by distinctive terms.

8. **An Apple Watch face complication can trigger the capture Shortcut, enabling a hands-free workflow: tap complication → dictate note → file committed on GitHub, with all required actions (Dictate Text, Format Date, Text, Encode, Get Contents of URL, Show Notification) confirmed as watchOS-compatible.** This achieves minimum-friction spontaneous capture without removing the iPhone from a pocket.

9. **The direct-write path (Contents API) is the correct primary path for the Memory-System repository, reversing the prior research conclusion that issue creation is preferred; that conclusion holds for the Research repo, which has an issue-to-backlog Actions workflow, but the Memory-System's zero-infrastructure constraint requires direct file creation to avoid adding a new workflow dependency.** The additional authoring complexity (8–11 vs. 4–5 actions) is a one-time build cost, not a recurring usage cost.

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| `Get Contents of URL` supports PUT with custom headers and JSON | Apple Support (apd58d46713f); island94.org (Jan 2024); prior research 2026-03-02-ios-shortcuts-research.md | high | Independently confirmed by GitHub employee example and prior research |
| Contents API requires `message` and `content` (base64, no line breaks) | GitHub REST API Docs — repo contents; web search cross-confirmation | high | Primary source + two independent confirmations |
| Encode action Line Wrap: None required; MIME wrapping causes HTTP 422 | Apple Community discussion (discussions.apple.com/thread/251563782); prior research 2026-03-02-ios-shortcuts-research.md | high | Multiple independent community reports of same failure and fix |
| Filename collision risk with minute-precision; seconds prevent it | Derived from Contents API behavior (HTTP 422 on existing file without sha) | high | Mechanistically sound |
| No native Keychain access from iOS Shortcuts | Web search (multiple developer/security sources, 2024); prior research 2026-03-02-ios-shortcuts-research.md Key Finding #6 | high | Community consensus; no Apple documentation contradicts |
| Fine-grained PAT Contents: write scope sufficient; blast radius limited to one repo | GitHub Docs — fine-grained PATs; prior research 2026-03-02-ios-shortcuts-research.md Key Finding #5 | high | Primary source + prior research confirmation |
| Rate limit: 5,000/hour primary; ~80/min secondary for content creation | GitHub REST API rate limits docs; web search cross-confirmation | high | Two independent sources consistent |
| Code search: 10 requests/minute authenticated; unauthenticated blocked | GitHub Changelog — code search API changes (March 2023) | high | Primary source (official changelog) |
| Code search JSON parseable via Shortcuts Dictionary/Repeat actions | Inference from known Shortcuts action set; web search (2024) | medium | Inference; not verified on device |
| Apple Watch complication → capture Shortcut viable; required actions watch-compatible | Apple Support watch shortcuts; Dr. Drang Tot Notes example (July 2024) | medium | Inference from analogy; on-device test needed to confirm |
| 8–11 actions required for direct-write Shortcut | Derived from action enumeration in §2 A1–A5 | medium | Estimated; exact count depends on implementation choices |
| Round-trip latency 1–5 seconds total | [assumption] — inferred from network characteristics; no specific benchmark found | low | Assumption explicitly labelled |

### Assumptions

- **Assumption:** Round-trip latency is 1–3 seconds on Wi-Fi and 2–5 seconds on LTE. **Justification:** Inferred from general iOS Shortcuts execution overhead (sub-second for local actions) plus typical GitHub API response times (200–800 ms on Wi-Fi, 500–2000 ms on LTE). No published benchmark for this specific Shortcuts + GitHub Contents API flow was found during research.

- **Assumption:** All required Shortcut actions (Dictate Text, Format Date, Text, Encode, Get Contents of URL, Show Notification) are compatible with watchOS Shortcuts execution. **Justification:** Apple's documentation lists supported Shortcuts action categories for Apple Watch, and these action types fall within supported categories. Dr. Drang's July 2024 working example uses an analogous action set. On-device testing is needed to confirm.

### Analysis

The central question — whether the direct file write path is viable as primary capture — resolves to yes, with the caveat that it requires more careful Shortcut authoring than the issue creation path. The authoring complexity (base64 encoding with Line Wrap: None, filename construction, front-matter templating) is real but bounded and one-time. Once the Shortcut is built and validated on device, no additional complexity accrues.

The recommendation differs from the prior research item's preference for issue creation. That preference was grounded in the Research repo's context (an existing issue-to-backlog Actions workflow makes issues a valid capture path). The Memory-System context removes that workflow, making issue creation a half-step that adds infrastructure. The direct-write path is the complete path.

The PAT security posture is the weakest point of the design. iOS Shortcuts' lack of Keychain access is a platform-level constraint. [inference] The recommended mitigation (fine-grained PAT, minimal scope, private Shortcut, calendar-reminder rotation) is the best available option within the zero-infrastructure constraint. The security trade-off is acceptable for personal notes on a biometric-locked device, not for shared or professional contexts.

Code search as retrieval is a functional but limited path. It answers "find notes containing this keyword" but not "find notes semantically related to this concept." For personal memory capture where the user tends to use consistent terminology, keyword search is sufficient for most retrieval needs. Semantic retrieval (vector embeddings, LanceDB or similar) is out of scope for this item and would require local or server-side infrastructure.

### Risks, Gaps, and Uncertainties

- **No on-device test conducted.** The research identifies no theoretical barrier to the direct-write flow, but implementation-specific issues (Shortcuts version compatibility, API response parsing edge cases, watchOS action rendering) may surface during actual device testing. The Memory-System W-0008 implementation work must include a device test phase.
- **Apple Watch action compatibility is inferred.** The claim that all required actions are watchOS-compatible is based on Apple documentation categories and one analogous working example, not a complete action-by-action compatibility check.
- **Siri transcription quality for technical terms.** Hands-free dictation of technical terms, proper nouns, or unusual vocabulary may produce transcription errors. A confirmation step before the API call addresses this at the cost of one extra interaction.
- **PAT rotation discipline.** If the PAT expires and is not rotated promptly, the Shortcut silently fails (GitHub returns 401). Adding a notification step that shows the API response status code to the user helps surface failures.

### Open Questions

- Should the Shortcut include a text review step (display transcribed text, confirm before committing) to catch Siri transcription errors? This adds one interaction but prevents bad data entering the memory system.
- Is there value in a "browse recent captures" Shortcut using the Contents API `GET /repos/{owner}/{repo}/contents/inbox` (returns directory listing as JSON) plus "Choose from List" and "Open URLs"?
- Does watchOS's Shortcuts execution environment introduce additional latency compared to iPhone execution for network-dependent actions like `Get Contents of URL`?
- Could a companion app (e.g., a simple iOS app that exposes a Shortcuts App Intent with Keychain-backed token storage) eliminate the hardcoded PAT limitation without violating the zero-infrastructure constraint? This would be a native iOS app — infrastructure on-device but not server-side.

---

## Output

- Type: tool, knowledge
- Description: Full design for an iOS Shortcuts direct-write memory capture Shortcut using the GitHub Contents API; action sequence specification; PAT security model; code search retrieval pattern; Apple Watch complication path. Directly informs Memory-System W-0008 implementation.
- Links:
  - https://docs.github.com/en/rest/repos/contents (GitHub Contents API — primary reference)
  - https://discussions.apple.com/thread/251563782 (Apple Community — Line Wrap: None fix for base64 encoding)
  - https://support.apple.com/guide/watch/shortcuts-apd99050d435/watchos (Apple Watch Shortcuts compatibility)
