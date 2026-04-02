# 2026-04-02 — Claude Code npm Source Map Leak

## Session summary

Researched and completed the research item covering the March 2026 accidental leak of Anthropic's Claude Code source code via an npm (Node Package Manager) package. The research covers root cause (missing `.npmignore` exclusion and Bun default source map generation), scope of exposure, Anthropic's response including an over-broad Digital Millennium Copyright Act (DMCA) takedown sweep, community reaction, and preventive controls for release engineering teams.

## What was done

- Created backlog item `2026-04-02-claude-code-npm-source-map-leak.md` via `python -m src.main research add`
- Started item (moved to in-progress) via `python -m src.main research start`
- Conducted research via web search across 12 sources covering: Cybernews, Bleeping Computer, CNBC, VentureBeat, Layer5, TechCrunch, Zscaler ThreatLabz, Penligent, Blockchain Council, Piunika Web, ByteIota, Business Standard
- Wrote full research skill output (§0–§7) and Findings section
- Completed item via `python -m src.main research complete`

## Research question captured

> How did the March 2026 accidental leak of Anthropic's Claude Code source code via an npm package occur, and what processes and protections can organisations adopt to prevent similar packaging-induced IP disclosures?

## Key dimensions scoped

1. Root cause: Bun source map defaults + missing `.npmignore` / `package.json` `files` whitelist
2. Exposure scope: 512,000+ lines of CLI source, no model weights or user data
3. Anthropic's response: package yanking + 8,100+ DMCA takedowns (including non-infringing repos)
4. Community reaction: viral forking, open-source reimplementations, malware lures
5. Preventive controls: `npm pack --dry-run` CI/CD gate, production build source-map suppression, package whitelist approach

## Sources used

- https://cybernews.com/security/anthropic-claude-code-source-leak/
- https://www.bleepingcomputer.com/news/artificial-intelligence/claude-code-source-code-accidentally-leaked-in-npm-package/
- https://www.cnbc.com/2026/03/31/anthropic-leak-claude-code-internal-source.html
- https://venturebeat.com/technology/claude-codes-source-code-appears-to-have-leaked-heres-what-we-know
- https://layer5.io/blog/engineering/the-claude-code-source-leak-512000-lines-a-missing-npmignore-and-the-fastest-growing-repo-in-github-history
- https://techcrunch.com/2026/04/01/anthropic-took-down-thousands-of-github-repos-trying-to-yank-its-leaked-source-code-a-move-the-company-says-was-an-accident/
- https://www.zscaler.com/blogs/security-research/anthropic-claude-code-leak
- https://www.penligent.ai/hackinglabs/claude-code-source-map-leak-what-was-exposed-and-what-it-means/
- https://byteiota.com/claude-code-source-leaked-via-npm-512k-lines-exposed/
- https://www.business-standard.com/technology/tech-news/anthropic-leaks-source-code-claude-code-again-what-happened-explained-126040100384_1.html
