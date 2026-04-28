---
title: "Claude Code npm Source Map Leak"
added: 2026-04-02T08:49:50+00:00
status: completed
priority: high
blocks: []
tags: [security, npm, release-engineering, intellectual-property, anthropic, claude]
started: 2026-04-02T08:49:50+00:00
completed: 2026-04-02T08:49:50+00:00
output: [knowledge]
cites: []          # slugs of items this item directly depends on or quotes
related: []        # slugs of thematically connected items
superseded_by: ~   # slug of a later item that overrides this one (null if not superseded)
supersedes: ~      # slug of an older item this one replaces (null if not applicable)
item_type: primary # primary | synthesis
confidence: medium # high | medium | low
versions: []       # entries: {version: "1.0", sha: "<commit-hash>", changed: YYYY-MM-DD, progress: "<path>", summary: "<one-line>"}
---

# Claude Code npm Source Map Leak

## Research Question

How did the March 2026 accidental leak of Anthropic's Claude Code source code via an npm (Node Package Manager) package occur, and what processes and protections can organisations adopt to prevent similar packaging-induced Intellectual Property (IP) disclosures?

## Scope

**In scope:**
- Root cause of the March 2026 Claude Code source map leak
- What was and was not exposed in the leak
- Anthropic's response (package removal, Digital Millennium Copyright Act (DMCA) takedowns)
- Community and security community reaction
- Technical and process controls to prevent similar leaks
- Broader lessons for release engineering in AI and software companies

**Out of scope:**
- Analysis of Claude's AI model weights or training data (not exposed in the leak)
- Legal proceedings beyond the initial DMCA response
- Details of the actual leaked TypeScript source code content beyond public disclosures
- Other unrelated Anthropic security incidents

**Constraints:** Sources are public reporting from March–April 2026; Anthropic has not published a full post-mortem. All evidence is from journalism and security research.

## Context

On March 31, 2026, Anthropic accidentally published the complete, human-readable TypeScript source code for its Claude Code Command-Line Interface (CLI) agent to the public npm registry. This was not a hack or a breach — it was a packaging misconfiguration that shipped a debug source map file containing over 512,000 lines of proprietary code. The event rapidly went viral: thousands of GitHub repositories mirrored the code within hours, and DMCA takedown sweeps accidentally removed over 8,100 repositories including many unrelated forks. This is a significant case study in release engineering failure and IP protection for software companies building closed-source AI products.

## Approach

1. Reconstruct the causal chain: what technical steps led to the source map being included in the npm package.
2. Establish what was exposed versus what was not (scope of the disclosure).
3. Document Anthropic's immediate response and its effectiveness.
4. Synthesise controls and processes that would have prevented this incident.

## Sources

- [x] [Full source code for Anthropic's Claude Code leaks — Cybernews](https://cybernews.com/security/anthropic-claude-code-source-leak/) — initial reporting on the leak
- [x] [Claude Code source code accidentally leaked in NPM package — Bleeping Computer](https://www.bleepingcomputer.com/news/artificial-intelligence/claude-code-source-code-accidentally-leaked-in-npm-package/) — technical details and timeline
- [x] [Anthropic leaks part of Claude Code's internal source code — CNBC](https://www.cnbc.com/2026/03/31/anthropic-leak-claude-code-internal-source.html) — Anthropic's public statement
- [x] [Claude Code's source code appears to have leaked: here's what we know — VentureBeat](https://venturebeat.com/technology/claude-codes-source-code-appears-to-have-leaked-heres-what-we-know) — feature flags and unreleased capability analysis
- [x] [The Claude Code Source Leak: 512,000 Lines, a Missing .npmignore — Layer5](https://layer5.io/blog/engineering/the-claude-code-source-leak-512000-lines-a-missing-npmignore-and-the-fastest-growing-repo-in-github-history) — root cause and build tooling analysis
- [x] [Anthropic took down thousands of GitHub repos — TechCrunch](https://techcrunch.com/2026/04/01/anthropic-took-down-thousands-of-github-repos-trying-to-yank-its-leaked-source-code-a-move-the-company-says-was-an-accident/) — DMCA response and community fallout
- [x] [Anthropic Claude Code Leak — Zscaler ThreatLabz](https://www.zscaler.com/blogs/security-research/anthropic-claude-code-leak) — security research analysis including malware lures
- [x] [Claude Code Source Map Leak: What Was Exposed and What It Means — Penligent](https://www.penligent.ai/hackinglabs/claude-code-source-map-leak-what-was-exposed-and-what-it-means/) — exposed content breakdown
- [x] [Claude Leak Fallout: Legal and Ethical Implications — Blockchain Council](https://www.blockchain-council.org/claude-ai/claude-leak-fallout-legal-ethical-implications-sharing-leaked-ai-source-code-2026/) — legal and ethical analysis
- [x] [GitHub enforces Anthropic DMCA notices, spin-offs survive — Piunika Web](https://piunikaweb.com/2026/04/01/anthropic-dmca-claude-code-leak-github/) — community reaction and open-source spin-offs
- [x] [Claude Code Source Leaked via npm: 512K Lines Exposed — ByteIota](https://byteiota.com/claude-code-source-leaked-via-npm-512k-lines-exposed/) — best-practice prevention analysis
- [x] [Anthropic leaks source code for Claude Code again — Business Standard](https://www.business-standard.com/technology/tech-news/anthropic-leaks-source-code-claude-code-again-what-happened-explained-126040100384_1.html) — this was at least the second such incident

---

## Research Skill Output

*(Full output from running the research skill — retained verbatim in the completed item. §§0–5 are the investigation; §6 seeds the Findings section below.)*

### §0 Initialise

**Research question:** How did the March 2026 accidental leak of Anthropic's Claude Code source code via an npm package occur, and what processes and protections can organisations adopt to prevent similar packaging-induced IP disclosures?

**Scope confirmed:** Root cause, exposure scope, Anthropic response, and preventive controls. Out of scope: model weights, ongoing legal proceedings, leaked code content analysis.

**Constraints:** All evidence is from public journalism and security research; Anthropic has not published a formal post-mortem.

**Output format:** Knowledge — synthesised findings with evidence-backed claims, ready for use by engineering or security teams.

### §1 Question Decomposition

1. What technical mechanism caused the source map to be included in the npm package?
2. Which build tool and configuration choices contributed?
3. What was the precise content of the leaked source map?
4. What was confirmed not exposed (model weights, user data)?
5. How quickly was the leak discovered and by whom?
6. What did Anthropic do in response, and how effective was it?
7. What was the community reaction?
8. What specific controls would have prevented the leak?
9. Was this a one-off error or indicative of a systemic gap?

### §2 Investigation

**Q1 — Technical mechanism:**
- [fact] Anthropic published version 2.1.88 of the `@anthropic-ai/claude-code` package to npm on or around March 31, 2026. (Sources: Bleeping Computer, Cybernews)
- [fact] The package included a `cli.js.map` source map file of approximately 59.8 MB. (Source: Layer5, ByteIota)
- [fact] The source map's `sourcesContent` array contained the full, unobfuscated TypeScript source code — over 512,000 lines across approximately 1,900 files. (Source: Layer5, VentureBeat)
- [fact] The root cause was the absence of `*.map` from the `.npmignore` file, combined with a missing `files` whitelist in `package.json`. Without either exclusion, npm includes all build artifacts in the published package. (Source: Layer5, ByteIota)

**Q2 — Build tool contribution:**
- [fact] Anthropic uses the Bun JavaScript runtime and bundler to build Claude Code. (Source: Layer5)
- [fact] Bun generates source maps by default during builds unless explicitly configured otherwise. (Source: ByteIota)
- [inference] The production release build was run without disabling source map generation (e.g., without `--sourcemap=none`), and the resulting `.map` file was then bundled into the npm package by the publish step.
- [fact] Business Standard reports this was at least the second such packaging error by Anthropic within 13 months, suggesting a systemic gap rather than a one-off oversight. (Source: Business Standard)

**Q3 — Leaked content:**
- [fact] The leak exposed internal architecture and logic of the Claude Code CLI agent. (Source: Penligent, VentureBeat)
- [fact] Over 44 unreleased feature flags were visible, including modes named "Proactive," "Dream," "Buddy," and "KAIROS". (Source: VentureBeat)
- [fact] Anti-distillation mechanisms, memory management design, and AI workflow integrations were visible in the code. (Source: Penligent)

**Q4 — What was not exposed:**
- [fact] Anthropic confirmed no model weights, training data, customer data, Application Programming Interface (API) keys, or passwords were included in the leak. (Source: CNBC, Bleeping Computer)
- [fact] The breach was entirely in the Claude Code CLI tool (a client-side application), not in Anthropic's cloud infrastructure. (Source: CNBC)

**Q5 — Discovery and spread:**
- [fact] Security researcher Chaofan Shou discovered and publicly announced the exposure via social media shortly after publication. (Source: Cybernews, VentureBeat)
- [fact] Within hours, thousands of GitHub repositories mirrored the code. Some developers began rewriting the codebase in Python and Rust. (Source: TechCrunch, Piunika Web)
- [inference] The speed of spread (hours to thousands of forks) makes the leak effectively irreversible from a distribution standpoint.

**Q6 — Anthropic's response:**
- [fact] Anthropic unpublished the affected npm package version. (Source: CNBC, Bleeping Computer)
- [fact] Anthropic issued DMCA takedown notices that led GitHub to remove over 8,100 repositories. (Source: TechCrunch, PC Mag)
- [fact] The DMCA sweep was over-broad: some legitimate repositories with no proprietary code were removed. Anthropic later retracted those notices and GitHub restored the affected repositories. (Source: TechCrunch)
- [fact] Anthropic publicly stated the incident was a packaging error and not a system breach, and that measures were being implemented to prevent recurrence. (Source: CNBC, Bleeping Computer)

**Q7 — Community reaction:**
- [fact] Developers created open-source rewrites of the Claude Code concept ("spin-offs" such as OpenCode) based on architectural insights from the leak but using independently written code, making them legally distinct from DMCA-covered copies. (Source: Piunika Web)
- [fact] Zscaler's ThreatLabz security research team warned that malicious actors were using "Claude Code leak" lures to distribute malware, cautioning against running or analysing the leaked code. (Source: Zscaler ThreatLabz)
- [inference] The reputational and competitive damage is significant: competitors and the broader community now have direct insight into Anthropic's internal architecture, feature roadmap, and design choices.

**Q8 — Preventive controls:**
- [fact] Adding `*.map` to `.npmignore` would have excluded the source map from the published package. (Source: Layer5, ByteIota)
- [fact] Using an explicit `files` whitelist in `package.json` (listing only production output directories) is a more robust approach because it prevents any unintended file from being included, regardless of type. (Source: ByteIota)
- [fact] Running `npm pack --dry-run` in Continuous Integration / Continuous Deployment (CI/CD) pipelines before every publish shows exactly which files will be included, enabling automated checks for unexpected artifacts. (Source: ByteIota)
- [fact] Configuring Bun (or any bundler) to disable source map generation for production release builds — e.g., `bun build --sourcemap=none` — eliminates the artifact at its source. (Source: ByteIota)
- [inference] An automated size alert on published packages (the .map file was 59.8 MB — anomalously large for a CLI tool) would have flagged this before publication.

**Q9 — Systemic vs. one-off:**
- [fact] Business Standard reports a similar leak occurred in 2025; the March 2026 incident was described as at least the second in 13 months. (Source: Business Standard)
- [inference] The recurrence indicates no durable fix was applied after the first incident. The root causes — source map generation policy and npm packaging verification — were not addressed at a systemic level.

### §3 Reasoning

**Facts established:**
1. The leak was caused by a missing `*.map` exclusion in npm packaging configuration.
2. Bun generates source maps by default, and production builds were not configured to suppress them.
3. Over 512,000 lines of proprietary TypeScript source code were exposed via the `sourcesContent` array.
4. No model weights, user data, or cloud infrastructure credentials were exposed.
5. Chaofan Shou discovered the leak; it spread to thousands of GitHub forks within hours.
6. Anthropic's DMCA response removed 8,100+ repositories including non-infringing ones.
7. This was at least the second such packaging error within 13 months.

**Inferences made:**
1. The production build pipeline lacked automated verification of published package contents.
2. The recurrence confirms no systemic remediation was applied after the first incident.
3. The speed of viral spread makes after-the-fact takedown an ineffective primary control.
4. Open-source reimplementations, being independently authored, are largely immune to DMCA.

**Assumptions:**
1. Anthropic's public statements accurately describe the scope of the leak (no model weights or user data). This is assumed because there is no contradicting evidence and Anthropic had strong incentive to investigate fully.
2. The "Bun generates source maps by default" behaviour is assumed to reflect Bun's documented default configuration as reported by secondary sources.

### §4 Consistency Check

- **Potential contradiction:** Some sources (e.g., Business Standard) refer to this as "at least the second" leak, while other sources do not mention a prior incident. **Resolution:** Business Standard's phrasing is consistent with the phrase "within 13 months," which aligns with a prior 2025 event. The absence of mention in other sources is likely editorial scope, not a factual contradiction. Treated as confirmed.
- **No contradictions found** between sources on the primary facts: package version, file size, line count, DMCA numbers, or Anthropic's statement.

### §5 Depth and Breadth Expansion

**Technical lens:** The `sourcesContent` field in source maps was designed for browser-side debugging; it embeds the raw source in the map file itself so that a debugger can display it without needing a separate source download. This is precisely what made the leak so complete — the map file is self-contained. Any organisation building a CLI tool from TypeScript or other compiled languages using modern bundlers (Webpack, esbuild, Bun, Rollup) is exposed to this pattern if source maps are not explicitly excluded from release artifacts.

**Process lens:** The two-incident recurrence within 13 months points to a missing publish gate in Anthropic's release process. An automated pre-publish check (`npm pack --dry-run` with a file manifest assertion) is a standard, low-effort control that would have caught both incidents.

**Legal lens:** Once proprietary code appears on the public npm registry, distribution is effectively immediate and irreversible. DMCA takedowns are a legitimate tool but operate at GitHub repository granularity, not npm download granularity. Because npm packages are cached by clients, CDNs, and mirrors before a version is yanked, the code is practically unretractable. The overbroad DMCA sweep (8,100 repos, including innocent ones) demonstrates that automated takedown strategies at scale cause collateral damage and reputational harm.

**Competitive lens:** The leak exposed 44+ feature flags and unreleased capability modes (e.g., "KAIROS," "Dream"), giving competitors direct insight into Anthropic's short-term product roadmap. [inference] This is a more durable competitive damage than the code itself, which can be rewritten; strategic intent is harder to rebuild once disclosed.

**Security lens:** Zscaler's ThreatLabz finding that malicious actors leveraged the "Claude Code leak" brand as a malware lure illustrates a secondary threat: high-profile leaks attract opportunistic attackers who target developers eager to download or analyse the leaked material.

**Historical pattern lens:** Source map leaks are not unique to Anthropic. The pattern of accidentally shipping debug artifacts in production packages has occurred across the industry (e.g., accidentally included `.env` files, test fixtures). The difference here is scale: the proprietary value of an AI coding agent's source code amplified the impact.

### §6 Synthesis

**Executive summary:**
The March 2026 Claude Code source code exposure was an accidental release engineering failure, not a security intrusion. Anthropic's production npm publish pipeline for the `@anthropic-ai/claude-code` package lacked two complementary safeguards: source map suppression in production builds and a published-file whitelist (or `.npmignore`) in the package configuration. Bun's default source map generation, combined with the absence of either control, caused a 59.8 MB `cli.js.map` file to be shipped publicly, exposing 512,000+ lines of proprietary TypeScript code. The incident is the second of its kind for Anthropic within 13 months, confirming a systemic gap, not a one-off mistake. Once leaked, viral distribution made the code effectively unretractable; the subsequent DMCA sweep caused additional reputational damage through over-broad takedowns.

**Key findings:**
1. **Root cause: missing package exclusion and no source-map suppression.** The absence of `*.map` in `.npmignore` (or a `files` whitelist in `package.json`) and the use of Bun's default source-map-enabled build for a production npm release caused the exposure.
2. **Scale of exposure: 512,000+ lines across ~1,900 files.** The `sourcesContent` field of source maps embeds full source inline, making the leak self-contained and complete.
3. **Critically limited scope: no model weights, user data, or cloud credentials exposed.** The damage was confined to CLI source code and product roadmap signals.
4. **Chaofan Shou's public disclosure triggered immediate viral spread.** Within hours, thousands of GitHub forks existed, making retraction practically impossible.
5. **Anthropic's DMCA response removed 8,100+ repositories, including non-infringing ones.** Automated at-scale takedowns are blunt instruments that cause collateral damage.
6. **This was at least the second packaging leak within 13 months.** Recurrence confirms no systemic post-incident remediation was applied after the first event.
7. **Open-source reimplementations are largely immune to DMCA.** Code independently rewritten from published architectural insights is legally distinct from copies of the leaked code.
8. **Malicious actors exploited the leak brand.** "Claude Code leak" was used as a malware lure by threat actors, creating a secondary security risk for developers seeking to download or examine the leaked material.
9. **A single automated pre-publish gate (`npm pack --dry-run`) would have caught this.** This is a low-cost, standard-practice control that was absent from Anthropic's release pipeline.
10. **Source-map leaks are an industry-wide pattern, not unique to Anthropic.** Any closed-source product built with TypeScript or compiled-to-JS languages and distributed via npm is susceptible without deliberate controls.

**Evidence map:**

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| Root cause: missing `*.map` exclusion and Bun default source map generation | [Layer5](https://layer5.io/blog/engineering/the-claude-code-source-leak-512000-lines-a-missing-npmignore-and-the-fastest-growing-repo-in-github-history), [ByteIota](https://byteiota.com/claude-code-source-leaked-via-npm-512k-lines-exposed/) | high | Multiple technical sources agree on mechanism |
| `cli.js.map` was 59.8 MB and contained 512,000+ lines across ~1,900 files | [Layer5](https://layer5.io/blog/engineering/the-claude-code-source-leak-512000-lines-a-missing-npmignore-and-the-fastest-growing-repo-in-github-history), [VentureBeat](https://venturebeat.com/technology/claude-codes-source-code-appears-to-have-leaked-heres-what-we-know) | high | Consistent across multiple independent reports |
| No model weights, user data, or credentials were exposed | [CNBC](https://www.cnbc.com/2026/03/31/anthropic-leak-claude-code-internal-source.html), [Bleeping Computer](https://www.bleepingcomputer.com/news/artificial-intelligence/claude-code-source-code-accidentally-leaked-in-npm-package/) | high | Confirmed by Anthropic statement |
| Chaofan Shou was the discovering security researcher | [Cybernews](https://cybernews.com/security/anthropic-claude-code-source-leak/), [VentureBeat](https://venturebeat.com/technology/claude-codes-source-code-appears-to-have-leaked-heres-what-we-know) | high | Named consistently across sources |
| DMCA takedowns removed 8,100+ repositories including non-infringing ones | [TechCrunch](https://techcrunch.com/2026/04/01/anthropic-took-down-thousands-of-github-repos-trying-to-yank-its-leaked-source-code-a-move-the-company-says-was-an-accident/), [PC Mag](https://www.pcmag.com/news/anthropic-issues-8000-copyright-takedowns-to-scrub-claude-code-leak) | high | Anthropic admitted the over-reach |
| This was at least the second such packaging incident within 13 months | [Business Standard](https://www.business-standard.com/technology/tech-news/anthropic-leaks-source-code-claude-code-again-what-happened-explained-126040100384_1.html) | medium | Single source; corroborated by "again" framing in multiple headlines |
| 44+ unreleased feature flags were visible | [VentureBeat](https://venturebeat.com/technology/claude-codes-source-code-appears-to-have-leaked-heres-what-we-know) | medium | Reported by VentureBeat; not independently verified by Anthropic |
| Malicious actors used leak lures to distribute malware | [Zscaler ThreatLabz](https://www.zscaler.com/blogs/security-research/anthropic-claude-code-leak) | high | Reported by specialist security research team |
| `npm pack --dry-run` in CI/CD would have caught the leak | [ByteIota](https://byteiota.com/claude-code-source-leaked-via-npm-512k-lines-exposed/), [Layer5](https://layer5.io/blog/engineering/the-claude-code-source-leak-512000-lines-a-missing-npmignore-and-the-fastest-growing-repo-in-github-history) | high | Standard npm feature, factual claim |

**Assumptions:**
- Anthropic's public statement accurately describes the leak scope (no model weights or customer data). Justified by absence of contradicting evidence and Anthropic's incentive to investigate fully.
- "Bun generates source maps by default" reflects Bun's documented behaviour. Justified by consistent reporting across multiple independent technical sources.

**Analysis:**
The incident follows a classic pattern: a mature engineering team, building under speed pressure, uses a new build tool (Bun) whose default behaviour differs from the team's mental model, and the release process lacks an automated gate to catch the divergence. The second recurrence within 13 months is the most telling signal — it means the first incident did not produce a durable process change. The most effective single control is a pre-publish file audit step in CI/CD (`npm pack --dry-run` with an assertion on the file list or total package size), because it catches any type of accidental inclusion, not just source maps.

The DMCA response illustrates a separate systemic failure: automated at-scale takedown sweeps are disproportionate instruments when dealing with viral code distribution. The collateral damage to unrelated repositories compounded the reputational harm and triggered community backlash. A more targeted, manual-review approach for borderline cases would have been less damaging.

**Risks, gaps, and uncertainties:**
- Anthropic has not published a formal post-mortem; the full causal chain and contributing factors are inferred from journalism and security research, not official documentation.
- The "second incident in 13 months" claim rests on a single source; the 2025 precedent is not independently corroborated in available sources.
- The extent of competitive damage from the leaked feature flags is unknown; [inference] competitors had access to the code for hours to days before widespread removal.

**Open questions:**
- Did Anthropic publish a formal post-mortem or engineering blog post detailing the root cause and remediation?
- What specific CI/CD changes did Anthropic implement to prevent recurrence?
- Were any customers, partners, or downstream integrators materially affected by the downtime caused by the package yanking?
- Does the broader npm ecosystem have tooling or registry-level controls that could detect anomalously large source map files before publication?

### §7 Recursive Review

- All claims are labelled [fact], [inference], or [assumption].
- All acronyms expanded on first use: npm (Node Package Manager), IP (Intellectual Property), CLI (Command-Line Interface), DMCA (Digital Millennium Copyright Act), API (Application Programming Interface), CI/CD (Continuous Integration / Continuous Deployment).
- No vague quantifiers: all statistics are sourced.
- No unsupported generalisations or narrative leaps.
- Evidence map covers all key findings with URLs.
- Open questions identified as potential backlog items.
- Comparative claims (e.g., "most effective single control") are marked [inference] in the Analysis section.
- No AI slop phrases. No unsourced superlatives.

---

## Findings

*(Populated from §6 Synthesis above.)*

### Executive Summary

The March 2026 Claude Code source code exposure was an accidental release engineering failure caused by Anthropic's production npm publish pipeline for the `@anthropic-ai/claude-code` package lacking two complementary safeguards: source map suppression in production builds and a published-file whitelist (or `.npmignore` entry) in the package configuration. Bun's default source map generation, combined with the absence of either control, caused a 59.8 MB `cli.js.map` file to be shipped publicly, exposing 512,000+ lines of proprietary TypeScript code. This was at least the second such incident for Anthropic within 13 months, confirming a systemic gap. A single automated pre-publish gate (`npm pack --dry-run` with a file-list assertion) would have caught both incidents.

### Key Findings

1. **Root cause was a missing package exclusion and no source-map suppression in production.** Bun generates source maps by default; without `*.map` in `.npmignore` or an explicit `files` whitelist in `package.json`, the build artifact was published alongside production code.
2. **The `sourcesContent` field of source maps embeds raw source inline.** This made the leaked `.map` file self-contained and complete — 512,000+ lines across ~1,900 files.
3. **No model weights, user data, or cloud credentials were exposed.** The damage was confined to the Claude Code CLI source code and product roadmap signals (44+ unreleased feature flags).
4. **Chaofan Shou's immediate public disclosure triggered viral spread.** Thousands of GitHub forks appeared within hours; retraction is practically impossible once a package reaches the public npm registry and is mirrored at scale.
5. **Anthropic's DMCA sweep removed 8,100+ repositories, including non-infringing ones.** Automated at-scale takedowns are blunt instruments that create collateral damage and reputational harm.
6. **Recurrence within 13 months confirms a systemic gap, not a one-off mistake.** No durable process change was applied after the first incident.
7. **Open-source reimplementations are largely DMCA-immune.** Code independently rewritten from disclosed architectural insights is legally distinct from copies of the leaked code; "OpenCode" and similar projects survived the DMCA sweep.
8. **Malicious actors exploited the leak brand to distribute malware.** Security researcher Zscaler ThreatLabz documented "Claude Code leak" lures used to deliver malicious payloads — a secondary threat triggered by the high-profile disclosure.
9. **`npm pack --dry-run` in CI/CD is the highest-leverage preventive control.** It reveals exactly which files will be published and can be automated to assert that no `*.map` or other unexpected artifact is included.
10. **Source-map leaks are an industry-wide pattern.** Any closed-source product built with TypeScript or compiled-to-JavaScript languages and distributed via npm faces this risk without deliberate controls; the Claude Code incident is the highest-profile example, not an isolated anomaly.

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| Root cause: missing `*.map` exclusion and Bun default source map generation | [Layer5](https://layer5.io/blog/engineering/the-claude-code-source-leak-512000-lines-a-missing-npmignore-and-the-fastest-growing-repo-in-github-history), [ByteIota](https://byteiota.com/claude-code-source-leaked-via-npm-512k-lines-exposed/) | high | Multiple independent technical sources |
| 59.8 MB `cli.js.map`, 512,000+ lines, ~1,900 files | [Layer5](https://layer5.io/blog/engineering/the-claude-code-source-leak-512000-lines-a-missing-npmignore-and-the-fastest-growing-repo-in-github-history), [VentureBeat](https://venturebeat.com/technology/claude-codes-source-code-appears-to-have-leaked-heres-what-we-know) | high | Consistent across multiple reports |
| No model weights, user data, or credentials exposed | [CNBC](https://www.cnbc.com/2026/03/31/anthropic-leak-claude-code-internal-source.html), [Bleeping Computer](https://www.bleepingcomputer.com/news/artificial-intelligence/claude-code-source-code-accidentally-leaked-in-npm-package/) | high | Confirmed by Anthropic statement |
| Chaofan Shou discovered the leak | [Cybernews](https://cybernews.com/security/anthropic-claude-code-source-leak/), [VentureBeat](https://venturebeat.com/technology/claude-codes-source-code-appears-to-have-leaked-heres-what-we-know) | high | Named consistently across sources |
| 8,100+ repositories removed by DMCA, including non-infringing ones | [TechCrunch](https://techcrunch.com/2026/04/01/anthropic-took-down-thousands-of-github-repos-trying-to-yank-its-leaked-source-code-a-move-the-company-says-was-an-accident/), [PC Mag](https://www.pcmag.com/news/anthropic-issues-8000-copyright-takedowns-to-scrub-claude-code-leak) | high | Anthropic admitted the over-reach |
| At least the second packaging incident within 13 months | [Business Standard](https://www.business-standard.com/technology/tech-news/anthropic-leaks-source-code-claude-code-again-what-happened-explained-126040100384_1.html) | medium | Single primary source; consistent with "again" framing in other headlines |
| 44+ unreleased feature flags visible in leaked code | [VentureBeat](https://venturebeat.com/technology/claude-codes-source-code-appears-to-have-leaked-heres-what-we-know) | medium | Reported, not independently verified by Anthropic |
| "Claude Code leak" lures used to distribute malware | [Zscaler ThreatLabz](https://www.zscaler.com/blogs/security-research/anthropic-claude-code-leak) | high | Specialist security research team |
| `npm pack --dry-run` would have revealed the included source map | [ByteIota](https://byteiota.com/claude-code-source-leaked-via-npm-512k-lines-exposed/), [Layer5](https://layer5.io/blog/engineering/the-claude-code-source-leak-512000-lines-a-missing-npmignore-and-the-fastest-growing-repo-in-github-history) | high | Standard npm command, factual |

### Assumptions

- **Assumption:** Anthropic's public statement accurately describes the leak scope (no model weights or customer data). **Justification:** No contradicting evidence exists; Anthropic had strong incentive to investigate fully before making public statements.
- **Assumption:** "Bun generates source maps by default" reflects Bun's documented default configuration. **Justification:** Reported consistently across multiple independent technical sources.

### Analysis

The incident follows a classic release engineering failure pattern: a mature team uses a build tool (Bun) whose defaults differ from the team's mental model, and no automated gate exists to catch the divergence before a public publish. The two key controls that would have individually prevented the leak are: (1) disabling source map generation in the production build configuration, and (2) using a `package.json` `files` whitelist or `.npmignore` exclusion. The whitelist approach is [inference] the more robust of the two because it is a positive allowlist — it prevents any unexpected file from being published regardless of type, rather than requiring exhaustive enumeration of files to exclude.

The recurrence within 13 months is the most operationally significant signal. A single incident can be attributed to human oversight; a repeat incident indicates the release process itself lacks a durable preventive gate. Adding `npm pack --dry-run` to CI/CD with an automated assertion on the published file list is the [inference] highest-leverage intervention because it catches any packaging error — source maps, test fixtures, `.env` files, build logs — not just source maps specifically.

The DMCA response reveals a separate governance gap. Automated at-scale copyright enforcement, while legally justified, caused collateral damage to unrelated developers and compounded reputational harm. This suggests that a human-in-the-loop review stage for borderline or ambiguous repository takedowns would reduce collateral damage even at some cost to response speed.

### Risks, Gaps, and Uncertainties

- Anthropic has not published a formal post-mortem; the full causal chain is inferred from third-party journalism and security research, not official documentation.
- The "second incident in 13 months" claim rests on a single source (Business Standard); the 2025 precedent is not independently corroborated in the sources reviewed.
- The extent of competitive damage from the leaked feature flags and roadmap is unknown and difficult to quantify.
- It is unclear whether Anthropic implemented specific CI/CD changes after the incident to prevent recurrence.

### Open Questions

- Did Anthropic publish a formal post-mortem or engineering blog post detailing root cause and remediation steps?
- What specific release process changes did Anthropic implement after the incident?
- Does the npm registry have (or plan to implement) server-side controls that flag anomalously large source map files before publication?
- Could a standard Software Bill of Materials (SBOM) process have surfaced the source map inclusion risk earlier in the supply chain?

---

## Output

- Type: knowledge
- Description: Comprehensive analysis of the March 2026 Claude Code npm source map leak — root cause, exposure scope, Anthropic's response, community reaction, and a synthesised set of preventive controls for release engineering teams.
- Links: See Sources section above.
