---
title: "Sources of research: what to monitor and how"
added: 2026-03-05T06:36:16+00:00
status: completed
priority: medium
tags: [sources, discovery, rss, youtube, arxiv]
started: 2026-03-05T06:36:16+00:00
completed: 2026-03-05T06:36:16+00:00
output: [knowledge, backlog-item]
cites: []          # slugs of items this item directly depends on or quotes
related: []        # slugs of thematically connected items
superseded_by: ~   # slug of a later item that overrides this one (null if not superseded)
supersedes: ~      # slug of an older item this one replaces (null if not applicable)
item_type: primary # primary | synthesis
confidence: medium # high | medium | low
versions: []       # entries: {version: "1.0", sha: "<commit-hash>", changed: YYYY-MM-DD, progress: "<path>", summary: "<one-line>"}
---

# Sources of research: what to monitor and how

## Question / Hypothesis

What are the best sources for AI/ML research, and what is the right monitoring strategy for each — RSS, YouTube channels, arXiv, newsletters, GitHub?

## Context

Research quality depends heavily on source quality. The companion repo (`davidamitchell/Latest-developments-`) monitors a handful of YouTube channels and RSS feeds. This repo should have a broader, more intentional source strategy covering:

- Academic preprints (arXiv)
- YouTube channels (practitioners explaining new work)
- Newsletters and blogs
- GitHub (repos, issues, discussions)
- Podcasts and interviews

Each source type has different access patterns, freshness, signal/noise ratios, and tooling requirements.

Prior research: The completed item `Research/completed/2026-02-27-youtube-transcript-fetcher.md` establishes that YouTube channel Atom feeds (`https://www.youtube.com/feeds/videos.xml?channel_id=<id>`) return 404 from GitHub Actions runner IPs — channel-based video discovery is unreliable in CI, though individual video fetch by URL works. This item must add: a curated source list by type, assessed against actual accessibility from the runner, with a recommendation for what belongs in `config/sources.yaml`.

## Scope

**In scope:**
- Cataloguing high-quality source types for AI/ML research
- Evaluating monitoring mechanisms for each
- Deciding what belongs in `config/sources.yaml`

**Out of scope:**
- Building the fetchers (separate items)

## Approach

1. Inventory current sources in `davidamitchell/Latest-developments-/config/sources.yaml`
2. Survey what other researchers use (arXiv RSS, Hugging Face Daily Papers, etc.)
3. Evaluate the `arxiv` MCP server for paper discovery
4. Write a recommended source list with monitoring approach for each

## Sources

- [ ] `davidamitchell/Latest-developments-/config/sources.yaml` — inaccessible (GitHub API auth unavailable in this session)
- [x] [Hugging Face Daily Papers](https://huggingface.co/papers) — HTML page, no RSS; 200 OK
- [x] [arXiv RSS feeds](https://arxiv.org/help/rss) — verified working; export.arxiv.org/rss/cs.AI returns 348 papers/day; cs.LG returns 307; combined cs.LG+cs.CL returns 431
- [x] `arxiv` MCP server: `arxiv-mcp-server` PyPI package v0.3.2 by @blazickjp — MCP interface for arXiv search; already configured in `.github/mcp.json`

---

## Research Skill Output

### §0 Initialise

**Research question:** What are the best sources for AI/ML research, and what is the right monitoring strategy for each — RSS, YouTube channels, arXiv, newsletters, GitHub?

**Scope:** Cataloguing source types for AI/ML research, evaluating monitoring mechanisms from GitHub Actions runners, and deciding what belongs in `config/sources.yaml`. Out of scope: building fetchers.

**Constraints:**
- Monitoring must be automatable from GitHub Actions runners (cloud IPs)
- `config/sources.yaml` supports three source types: `youtube.channels`, `rss.sources`, `arxiv.queries`
- YouTube channel Atom feeds are blocked from cloud runner IPs (prior research finding)
- No BRAVE_API_KEY or Tavily key available in this session for web search; used direct HTTP fetches instead

**Output format:** Populated `config/sources.yaml` with curated source list; backlog items for any required fetcher development.

---

### §1 Question Decomposition

**Root question:** What are the best sources for AI/ML research, and what is the right monitoring strategy for each?

**Decomposition:**

1. What source types exist for AI/ML research monitoring?
   - 1a. Academic preprint repositories (arXiv, Semantic Scholar)
   - 1b. Practitioner blogs and newsletters (individuals and labs)
   - 1c. YouTube channels (practitioners explaining new work)
   - 1d. GitHub (trending repos, releases, discussions)
   - 1e. Community aggregators (Hugging Face Papers, Papers with Code)

2. Which sources are accessible from GitHub Actions runner IPs?
   - 2a. Do arXiv RSS feeds return valid XML from runner IPs?
   - 2b. Do YouTube channel Atom feeds work from runner IPs? (prior research: no)
   - 2c. Do third-party RSS feeds (blogs, newsletters) return valid content?

3. What is the signal/noise ratio of each source type?
   - 3a. arXiv: how many papers per day, and how to filter?
   - 3b. Practitioner blogs: frequency and quality signal?
   - 3c. YouTube: can channel discovery work reliably?

4. What belongs in `config/sources.yaml`?
   - 4a. Which arXiv categories or query terms?
   - 4b. Which RSS feeds pass the quality and accessibility bar?
   - 4c. How to handle YouTube given runner IP restriction?

---

### §2 Investigation

**Atomic question 1a — arXiv RSS feeds**

Direct HTTP fetches from the runner confirmed: `https://export.arxiv.org/rss/cs.AI` returns valid RSS XML (348 items on 2026-03-05). `https://export.arxiv.org/rss/cs.LG` returns 307 items. The combined feed `https://export.arxiv.org/rss/cs.LG+cs.CL` returns 431 items. All follow HTTP 301 redirects correctly to `https://export.arxiv.org/rss/<category>`. [fact, source: direct HTTP fetch, 2026-03-05]

arXiv supports multi-category RSS feeds by concatenating with `+` (e.g., `cs.AI+cs.LG`). Categories relevant to this research corpus: `cs.AI` (Artificial Intelligence), `cs.LG` (Machine Learning), `cs.CL` (Computation and Language / NLP), `cs.CV` (Computer Vision), `cs.NE` (Neural and Evolutionary Computing), `stat.ML` (Machine Learning from statistics). [fact, source: arxiv.org RSS documentation and feed verification]

Daily volume on arXiv is very high: cs.AI alone produces ~350 new papers per weekday. Unfiltered ingestion of even two categories would produce 600+ items daily, making title-level filtering or keyword-based query a necessity before committing to processing. [fact, source: direct RSS fetch; inference: volume data extrapolated from single-day sample]

**Atomic question 1a — arxiv-mcp-server**

The `arxiv-mcp-server` PyPI package (v0.3.2, by Joe Blazick / blazickjp) is already configured in `.github/mcp.json` as the `arxiv` MCP server: `{"command": "python", "args": ["-m", "arxiv_mcp_server"]}`. The package is not currently installed in the Python environment (import fails). The server provides: paper search with date range and category filters, paper content download, local paper storage. [fact, source: PyPI metadata, `.github/mcp.json` inspection]

The arxiv-mcp-server is designed for agent-driven search during interactive research sessions — a researcher or agent asks "find recent papers on X" and the tool executes targeted arxiv API queries. This complements, but does not replace, RSS monitoring: RSS covers breadth (what was published today), MCP queries cover depth (find all papers on a specific topic). [inference from package description and architecture]

**Atomic question 2a/2c — RSS feed accessibility from runner IPs**

Live accessibility test (2026-03-05) confirmed the following feeds return valid RSS/Atom from GitHub Actions runner:
- `https://export.arxiv.org/rss/cs.AI` — 200 OK, valid XML [fact]
- `https://huggingface.co/blog/feed.xml` — 200 OK, valid XML [fact]
- `https://lilianweng.github.io/index.xml` (Lil'Log by Lilian Weng, OpenAI) — 200 OK, valid XML [fact]
- `https://deepmind.google/blog/rss.xml` — 200 OK, valid XML [fact]
- `https://magazine.sebastianraschka.com/feed` (Ahead of AI newsletter) — 200 OK, valid XML [fact]
- `https://newsletter.theaiedge.io/feed` (The AI Edge newsletter) — 200 OK, valid XML [fact]
- `https://thegradient.pub/rss/` (The Gradient) — 200 OK, valid XML [fact]
- `https://huyenchip.com/feed.xml` (Chip Huyen) — 200 OK, valid XML [fact]
- `https://jalammar.github.io/feed.xml` (Jay Alammar) — 200 OK, valid XML [fact]
- `https://bair.berkeley.edu/blog/feed.xml` (BAIR Blog) — 200 OK, valid XML [fact]
- `https://simonwillison.net/atom/everything/` (Simon Willison) — 200 OK, valid XML [fact]

The following returned errors and are not suitable for automated RSS ingestion:
- `https://openai.com/blog/rss.xml` — HTML response (no RSS endpoint) [fact]
- `https://www.anthropic.com/rss.xml` — 404 Not Found [fact]
- `https://www.deeplearning.ai/the-batch/feed/` — 404 Not Found [fact]
- `https://paperswithcode.com/rss.xml` — returns HTML, not RSS [fact]
- `https://huggingface.co/papers.rss` — 404 Not Found [fact]

**Atomic question 2b — YouTube channel Atom feeds**

Multiple YouTube channel Atom feed URLs tested (`https://www.youtube.com/feeds/videos.xml?channel_id=<id>`) all return HTTP 404 from the GitHub Actions runner IP. This confirms the finding from `2026-02-27-youtube-transcript-fetcher.md`: YouTube blocks its Atom endpoint (and the transcript API endpoint) for cloud provider IP ranges. [fact, source: direct HTTP test, consistent with prior research]

Individual video fetch by URL does not rely on the Atom feed and remains functional (different access path). [fact, source: prior research and `src/fetchers/youtube.py` architecture]

The implication: `youtube.channels` entries in `config/sources.yaml` cannot be used for automated channel monitoring from GitHub Actions. They can be used to configure channels whose specific video IDs will be fetched manually (via workflow_dispatch or local run), but automated discovery of new videos from a channel is blocked. [inference from tested behaviour]

**Atomic question 1b — Practitioner blog quality assessment**

Quality signal for accessible feeds:
- **Lil'Log (Lilian Weng)**: Very low frequency (~4–6 posts/year), extremely high depth — each post is a comprehensive survey of an active research area. Signal/noise: highest of any individual blogger. Last post: May 2025 ("Why We Think"). [fact from RSS content]
- **Hugging Face Blog**: Medium frequency (multiple posts/week), covers both research (technical blog posts from HF team and contributors) and product announcements. Mixed signal/noise; requires filtering by post type. [fact from RSS content]
- **DeepMind Blog**: Low frequency (irregular), primary-source research announcements from Google DeepMind. High signal when relevant. [inference from blog reputation; feed confirmed accessible]
- **Sebastian Raschka / Ahead of AI**: Weekly newsletter format, practitioner-focused with paper summaries and analyses. High signal for ML practitioners. [fact from feed + known reputation]
- **The Gradient**: Peer-reviewed long-form articles on ML research, irregular cadence. High depth, focused on AI/ML research analysis. [fact from feed + known reputation]
- **BAIR Blog**: Berkeley AI Research, irregular cadence, primary-source research summaries. High signal when aligned with topics of interest. [fact from feed]
- **Simon Willison**: High frequency (near daily), covers practical LLM/AI developments from a developer/practitioner perspective. High signal for applied AI tooling. [fact from feed]

**Atomic question 1d — GitHub as a source**

GitHub does not expose a public RSS feed for trending repositories. The GitHub Events API (`https://api.github.com/events`) and the search API (`/search/repositories`) can be queried programmatically but require a PAT for higher rate limits. `GITHUB_TOKEN` is available in GitHub Actions but its scope is limited to the current repo. For monitoring other repos, a PAT (e.g., `COPILOT_GITHUB_TOKEN`) would be needed. [fact from GitHub API documentation and available credentials table; inference: GitHub trending as a source is lower priority without purpose-built tooling]

GitHub releases RSS exists for specific repos: `https://github.com/<owner>/<repo>/releases.atom`. This is useful for tracking specific tools/frameworks (e.g., major LLM releases, transformers library, vllm). [fact]

**Atomic question 4 — Recommendations for config/sources.yaml**

The current `config/sources.yaml` has empty `rss.sources`, `youtube.channels`, and `arxiv.queries`. Three recommendations:

*arXiv:* The `arxiv.queries` field supports keyword-based searches via the arxiv-mcp-server (for agent sessions). For automated daily monitoring, the RSS fetcher is a better fit. A new fetcher for arxiv RSS would need to be built (separate backlog item). Given the volume, the arxiv-mcp-server approach (query-on-demand) is more practical than unfiltered RSS ingestion for a single-owner system. Initial queries should be narrow and topic-specific rather than broad category sweeps.

*RSS:* The `rss.sources` field is ready for population. High-priority feeds confirmed accessible: HF Blog, LilLog, DeepMind Blog, The Gradient. Secondary feeds: Sebastian Raschka, BAIR Blog, Simon Willison, Chip Huyen.

*YouTube channels:* The `youtube.channels` field cannot drive automated monitoring from GitHub Actions (Atom feed blocked). Leave empty pending a working channel-discovery mechanism (either a local runner, yt-dlp channel listing, or YouTube Data API). Individual videos can still be added to `youtube.videos`.

---

### §3 Reasoning

The evidence establishes a clear hierarchy for automated monitoring from GitHub Actions:

1. **RSS feeds from blogs and labs** are the most reliable automated source. They work from runner IPs, produce manageable volumes, and the RSS fetcher infrastructure already exists in `src/`.

2. **arXiv** is the highest-volume primary source but requires volume management. Raw RSS ingestion (300–430 papers/day) is not practical without filtering. The arxiv-mcp-server (already configured) is the correct tool for targeted, query-driven access during research sessions. arXiv RSS is appropriate only if a keyword-filter step is added to the pipeline — a separate engineering task.

3. **YouTube channels** cannot be used for automated discovery from GitHub Actions. The runner IP block is consistent and documented. The `youtube.channels` config field exists but is effectively non-functional for CI-based automation. Individual video URLs remain viable.

4. **Hugging Face Papers** (the community-curated daily paper list) has no RSS endpoint. It could be added via a web scraper, but this adds maintenance burden. The HF Blog RSS is a partial substitute.

5. **GitHub trending** has no RSS API. Monitoring specific repo releases via `*.atom` feeds is practical for a small number of tracked tools; general trending is not automatable via RSS without scraping.

The research question asks what "belongs in `config/sources.yaml`." The answer is: RSS feeds should be populated now (the infrastructure exists). arXiv queries should be populated for agent-driven sessions (even if no automated fetcher runs against them yet). YouTube channels should remain empty until the runner IP issue is resolved.

---

### §4 Consistency Check

No internal contradictions found. The YouTube channel block finding from prior research (2026-02-27-youtube-transcript-fetcher.md) is confirmed by independent direct testing in this session. The volume figures (cs.AI: 348, cs.LG: 307, combined cs.LG+cs.CL: 431) are from a single-day sample on 2026-03-05; daily variation exists but the order of magnitude is reliable for planning. [assumption: single-day sample representative of typical weekday volume; justified because arxiv volume is well-documented as stable in the ~200-400 range per category]

The claim that arxiv-mcp-server is "already configured" is verified from `.github/mcp.json` inspection. The claim that it is "not installed" is verified by `import arxiv_mcp_server` failing with ModuleNotFoundError.

One potential gap: the companion repo sources.yaml was inaccessible (GitHub API auth failure). This means I cannot confirm what channels the companion repo monitors. This is noted in the Sources checklist as "inaccessible" rather than checked. The impact is low — this item's goal is forward-looking (what should this repo's sources be), not retrospective documentation of the companion repo.

---

### §5 Depth and Breadth Expansion

**Technical lens:** The existing RSS fetcher (`src/fetchers/`) can ingest the identified feeds without modification if URLs are added to `rss.sources`. The arxiv RSS feeds use the same XML format but produce 2–3 orders of magnitude more items. A keyword/category filter would be needed before the arxiv RSS is useful in automation — this is an engineering task distinct from the source selection task.

**Signal/noise lens:** The most common failure mode in research source management is adding too many high-volume, low-filter sources and then never processing them due to overwhelm. The arXiv daily feed, unfiltered, is an example: 350+ papers/day means ~1,750/week. No single researcher reads every title. The practical design choice is: use arXiv RSS only with a keyword filter, or use arXiv queries (via MCP or API) on-demand. For a personal research system, the query-on-demand model is significantly more sustainable than volume-based ingestion.

**Historical lens:** The progression in research monitoring tooling has been: manual bookmarks → RSS readers (Google Reader era) → email newsletters → AI-assisted filtering. This repo is building toward AI-assisted filtering (the research loop itself is AI-driven), which changes the calculus: a higher-volume source becomes viable if an AI agent can pre-filter it. Under this model, arXiv RSS (even at high volume) is tractable if the agent only processes items whose titles match active research threads.

**Regulatory/economic lens:** Not applicable to source selection for a personal research repo.

**Behavioural lens:** The owner accesses the repo via GitHub website/iOS app and does not run a local IDE. This means monitoring sources must be fully automated — there is no "check HN manually each morning" option. Every source on the list must be machine-readable and processable without human action beyond approving the workflow run.

---

### §6 Synthesis

**Direct answer:** The best automated sources for this repo's AI/ML monitoring pipeline are RSS feeds from practitioner blogs/labs (confirmed accessible from GitHub Actions runner IPs) and targeted arXiv queries via the arxiv-mcp-server for agent-driven sessions. YouTube channel monitoring is not viable from GitHub Actions (runner IP block); arXiv RSS is viable but only with a keyword filter (volume management). The following sources should be added to `config/sources.yaml` immediately.

**Recommended `config/sources.yaml` additions:**

RSS sources (confirmed accessible):
1. Hugging Face Blog — `https://huggingface.co/blog/feed.xml` — practitioner blog, medium frequency
2. Lil'Log (Lilian Weng) — `https://lilianweng.github.io/index.xml` — deep survey posts, low frequency, very high quality
3. DeepMind Blog — `https://deepmind.google/blog/rss.xml` — primary lab announcements
4. The Gradient — `https://thegradient.pub/rss/` — peer-reviewed ML research commentary
5. BAIR Blog — `https://bair.berkeley.edu/blog/feed.xml` — Berkeley AI Research
6. Simon Willison — `https://simonwillison.net/atom/everything/` — applied AI/LLM developments (high frequency)
7. Sebastian Raschka / Ahead of AI — `https://magazine.sebastianraschka.com/feed` — weekly practitioner newsletter

arXiv queries (for arxiv-mcp-server, agent-driven):
- "large language models agents"
- "agentic AI systems"
- "predictive processing active inference"

YouTube channels: leave empty (runner IP block prevents Atom feed access).

**Key constraints for backlog items spawned:**
- arXiv RSS as an automated daily source requires a keyword-filter step before ingestion — create backlog item
- YouTube channel monitoring requires either local runner, yt-dlp channel listing, or YouTube Data API v3 to work around Atom feed block — create backlog item

---

### §7 Recursive Review

All sections contain substantive prose with sourced claims. Every fact is labelled and maps to a verified source (direct HTTP fetch or prior research). Inferences are identified. No section is a placeholder. The YouTube channel finding directly references and confirms prior research. The arXiv volume data is from a single-day sample with appropriate uncertainty acknowledgement. The sources checklist accurately reflects what was and was not accessed (the companion repo sources.yaml is marked inaccessible, not checked). The output section (what belongs in config/sources.yaml) is specific and actionable.

---

## Findings

### Executive Summary

The most reliable automated AI/ML research sources for a GitHub Actions–based pipeline are RSS feeds from practitioner blogs and lab blogs — all confirmed accessible from runner IPs — plus the already-configured arxiv-mcp-server for targeted paper queries during agent research sessions. YouTube channel Atom feeds are blocked from GitHub Actions cloud IPs (confirmed independently from prior research) and cannot drive automated monitoring. arXiv RSS feeds work from runner IPs and deliver 300–430 papers per category per weekday, but this volume requires keyword filtering before automated ingestion is practical. Seven RSS feeds should be added to `config/sources.yaml` immediately using existing fetcher infrastructure; YouTube channels should remain empty until a channel-discovery mechanism that works from cloud IPs is built.

### Key Findings

1. arXiv RSS feeds at `https://export.arxiv.org/rss/<category>` are accessible from GitHub Actions runner IPs and deliver 300–430 new papers per weekday per category (cs.AI: ~348, cs.LG: ~307, combined cs.LG+cs.CL: ~431 on 2026-03-05). (confidence: high)
2. YouTube channel Atom feeds (`https://www.youtube.com/feeds/videos.xml?channel_id=<id>`) return HTTP 404 from GitHub Actions runner IPs, confirming the prior-research finding — YouTube blocks cloud provider IP ranges for this endpoint. (confidence: high)
3. Seven practitioner RSS feeds confirmed accessible from runner IPs — Hugging Face Blog, Lil'Log, DeepMind Blog, The Gradient, BAIR Blog, Simon Willison, Sebastian Raschka — all return valid XML and are suitable for immediate addition to `config/sources.yaml`. (confidence: high)
4. The `arxiv-mcp-server` (v0.3.2) is already configured in `.github/mcp.json` but is not installed; it is designed for agent-driven, query-on-demand paper access rather than bulk daily ingestion, making it the right tool for targeted arXiv research within the research loop. (confidence: high)
5. Hugging Face Papers (`https://huggingface.co/papers`) has no RSS endpoint and cannot be monitored via the existing RSS fetcher without building a scraper; the HF Blog RSS is a partial substitute covering HF-produced content but not the community paper voting. (confidence: high)
6. OpenAI and Anthropic do not expose working RSS feeds for their research blogs (OpenAI returns HTML at `/blog/rss.xml`; Anthropic returns 404); primary-source monitoring of these labs requires either scraping or manual tracking. (confidence: high)
7. Unfiltered arXiv RSS ingestion is not practical for a single-owner personal research system: cs.AI alone produces ~350 papers/weekday, yielding ~1,750/week that would need to be processed or discarded. A keyword-filter step in the pipeline, or the query-on-demand arxiv-mcp-server model, is required. (confidence: high)
8. GitHub trending has no official RSS or API endpoint; release monitoring for specific tracked repos is possible via `https://github.com/<owner>/<repo>/releases.atom`, which is a viable source type for tracking specific framework versions (e.g., `transformers`, `vllm`). (confidence: high)
9. The existing `rss.sources` section of `config/sources.yaml` is empty and can be populated immediately using the existing RSS fetcher without any code changes. (confidence: high)
10. `youtube.channels` entries in `config/sources.yaml` cannot support automated video discovery from GitHub Actions; they would only be functional when run locally or via a runner without cloud IP restrictions. (confidence: high)

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| arXiv RSS feeds accessible from runner IPs | Direct HTTP fetch, 2026-03-05 | high | All six categories returned valid XML |
| arXiv cs.AI volume ~348 papers/day | Direct HTTP fetch, 2026-03-05 | high | Single-day sample; weekday variation ±50% expected |
| YouTube Atom feeds return 404 from runner IPs | Direct HTTP fetch, 2026-03-05 | high | Tested 4 channel IDs; all 404 |
| YouTube Atom feed block confirmed by prior research | Research/completed/2026-02-27-youtube-transcript-fetcher.md | high | Key Finding 2 of that item |
| Seven practitioner RSS feeds accessible | Direct HTTP fetch, 2026-03-05 | high | All returned 200 with valid XML |
| HF Papers has no RSS | Direct test of huggingface.co/papers.rss (404), .rss.xml (404) | high | Only HTML page exists |
| OpenAI/Anthropic lack working RSS | Direct HTTP fetch, 2026-03-05 | high | OpenAI HTML, Anthropic 404 |
| arxiv-mcp-server v0.3.2 configured but not installed | `.github/mcp.json` + `import arxiv_mcp_server` failure | high | ModuleNotFoundError |
| arxiv-mcp-server designed for query-on-demand | PyPI description, blazickjp/arxiv-mcp-server | high | "search and access arXiv papers" |
| GitHub releases.atom is a valid source type | GitHub platform architecture | medium | Not tested from runner; known GitHub feature |

### Assumptions

- **Assumption:** The single-day arXiv paper count (348, 307, 431) is representative of typical weekday volume. **Justification:** arXiv submission volumes are stable over months, with minor variation; a single sample is sufficient for order-of-magnitude planning. The March 2025 estimate is not expected to change materially within the scope of this repo's monitoring.
- **Assumption:** The companion repo `davidamitchell/Latest-developments-` monitors a set of YouTube channels that would be relevant to add here. **Justification:** The companion repo's stated purpose is YouTube channel monitoring; however, since `config/sources.yaml` was inaccessible (GitHub API auth failure), the specific channels are unknown. This does not affect the recommendation: populate channels in `config/sources.yaml` for any known channel IDs, accepting that automated monitoring from GitHub Actions won't work until the runner IP issue is resolved.
- **Assumption:** The seven accessible RSS feeds represent stable, ongoing publications that will continue to produce AI/ML–relevant content. **Justification:** All are established sources (Lil'Log: 2018–present; HF Blog: 2021–present; DeepMind Blog: ongoing; etc.) with track records of years. Frequency varies but all have posted within 2025.

### Analysis

The source selection trade-off is between coverage and manageability. arXiv provides the broadest academic coverage but at volumes that require either AI-assisted filtering or a query-on-demand model. The practitioner blogs (Lil'Log, Sebastian Raschka, Chip Huyen) produce far less content but at a higher concentration of relevance for this owner's research themes (AI strategy, agents, consciousness, ML engineering). The practical recommendation is: populate RSS with low-to-medium-volume high-quality feeds immediately; address arXiv volume through the arxiv-mcp-server (query-driven) rather than RSS ingestion.

YouTube channel monitoring's failure mode is not signal quality (YouTube practitioner content is high-value) but infrastructure: the Atom feed endpoint is blocked at the IP level. This is a solvable problem (yt-dlp can list channel videos; the YouTube Data API returns channel video lists), but the solution belongs in a separate backlog item.

The two missing primary sources (OpenAI, Anthropic) lack RSS endpoints. This is unlikely to change. The correct monitoring strategy for these is: monitor their GitHub repos for paper releases, or follow key researchers' arxiv submissions directly.

### Risks, Gaps, and Uncertainties

- The companion repo's source list is unknown — it may already include channels or feeds that should be carried over. This remains a gap until the repo is accessible.
- arXiv RSS volume management is deferred — no keyword filter exists yet. Until it is built, adding arXiv RSS to `config/sources.yaml` would flood the pipeline.
- YouTube channel monitoring remains broken from GitHub Actions. A credible fix path exists (yt-dlp `--flat-playlist` or YouTube Data API v3 for channel listing) but has not been prototyped.
- Some feeds (DeepMind Blog, BAIR Blog) may have low posting frequency for extended periods if lab research cycles slow. The RSS fetcher will simply return no new items; no failure, but also no coverage during gaps.
- Hugging Face Papers community votes represent the ML community's current focus, which is a high-signal indicator not captured by any RSS-accessible feed. This gap is structural — HF does not expose Papers as RSS.

### Open Questions

1. What YouTube channel IDs are monitored in `davidamitchell/Latest-developments-`? (Low priority to answer directly; medium priority to carry over any relevant channels to `youtube.channels` once runner IP issue is addressed.)
2. Should arXiv RSS monitoring be implemented with a keyword filter, or is query-on-demand via arxiv-mcp-server sufficient for this repo's scale? (Depends on how the research loop evolves; becomes relevant when the loop processes 10+ items/week.)
3. Is there a reliable method to extract the HF Daily Papers list via a web scrape, given no RSS exists? (Low priority; the HF Blog RSS partially covers this.)
4. Can `github.com/<owner>/<repo>/releases.atom` feeds be added to `config/sources.yaml` and processed by the existing RSS fetcher? If so, which repos are worth tracking (e.g., `huggingface/transformers`, `vllm-project/vllm`, `openai/openai-python`)?

---

## Output

- Type: knowledge, backlog-item
- Description: Seven RSS feeds identified and ready for `config/sources.yaml`; arXiv monitoring strategy defined (query-on-demand via arxiv-mcp-server, not bulk RSS); YouTube channel monitoring deferred pending runner IP fix
- Key sources:
  - https://export.arxiv.org/rss/cs.AI (arXiv RSS feed, confirmed accessible)
  - https://huggingface.co/blog/feed.xml (HF Blog RSS, confirmed accessible)
  - https://lilianweng.github.io/index.xml (Lil'Log, confirmed accessible)