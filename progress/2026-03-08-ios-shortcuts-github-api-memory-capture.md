# 2026-03-08 — Research Loop (ios-shortcuts-github-api-memory-capture)

**Completed:**

Research item:
- `Research/completed/2026-03-08-ios-shortcuts-github-api-memory-capture.md` — completed; an iOS Shortcut can reliably write timestamped `.md` files directly to a GitHub repository via the Contents API as the primary mobile capture path for the Memory-System repo, with the critical requirement that the Encode action's Line Wrap setting must be set to None (MIME wrapping causes HTTP 422). A fine-grained PAT with `Contents: write` on a single repository is the correct credential, hardcoded in the Shortcut since iOS Shortcuts has no Keychain access; the same infrastructure supports keyword retrieval via the GitHub code search API and hands-free capture via Apple Watch complication.

Sources consulted:
- https://docs.github.com/en/rest/repos/contents (GitHub Contents API — required fields, error codes, authentication)
- https://discussions.apple.com/thread/251563782 (Apple Community — Encode action Line Wrap: None requirement confirmed)
- https://github.blog/changelog/2023-03-10-changes-to-the-code-search-api/ (GitHub Changelog — code search API rate limit: 10 requests/minute authenticated)
- https://support.apple.com/guide/watch/shortcuts-apd99050d435/watchos (Apple Watch Shortcuts compatibility)
- https://docs.github.com/en/rest/using-the-rest-api/rate-limits-for-the-rest-api (GitHub REST API rate limits)
