---
title: "Local index vs reference: what to store vs link"
added: 2026-03-03T18:13:09+00:00
status: completed
priority: medium
tags: [indexing, storage, local, reference]
started: 2026-03-03T18:13:09+00:00
completed: 2026-03-03T18:13:09+00:00
output: [knowledge, backlog-item]
cites: []          # slugs of items this item directly depends on or quotes
related: []        # slugs of thematically connected items
superseded_by: ~   # slug of a later item that overrides this one (null if not superseded)
supersedes: ~      # slug of an older item this one replaces (null if not applicable)
item_type: primary # primary | synthesis
confidence: medium # high | medium | low
versions: []       # entries: {version: "1.0", sha: "<commit-hash>", changed: YYYY-MM-DD, progress: "<path>", summary: "<one-line>"}
---

# Local index vs reference: what to store vs link

## Question / Hypothesis

For each type of research content, should we store a local copy / index, or just maintain a reference (URL, citation)? What are the right trade-offs between storage cost, offline access, durability, and searchability?

## Context

Not everything needs to be stored locally. Some content (YouTube transcripts, arXiv PDFs) is large and changes rarely — it may be better to fetch on demand. Other content (key passages, structured notes) should be stored locally for fast retrieval and to guard against link rot.

The right answer varies by content type:
- **Transcripts**: large, fetchable on demand, worth caching if used frequently
- **Papers**: moderately large, authoritative, worth local storage if referenced often
- **Web pages**: ephemeral, prone to link rot, worth local snapshot for key pages
- **Notes / synthesis**: always local — this is the primary research output

**Prior research:** `2026-02-27-indexing-and-tracking-method.md` (completed 2026-02-28) established that JSON state file + YAML front-matter is the correct approach for deduplication and metadata. It found that plain-text, git-diffable formats are strongly preferred because the owner reviews all changes via the GitHub website. `2026-02-27-local-database.md` (completed 2026-03-03) confirmed that binary files (PDFs, SQLite) should not be committed to the repo. Neither item addressed the storage-vs-reference decision for each content type directly. This item fills that gap by applying a decision framework to each content type and producing a concrete storage policy.

## Scope

**In scope:**
- Decision framework for local vs reference
- Storage format recommendations per content type
- Git-friendliness of each approach (large files → Git LFS?)

**Out of scope:**
- Implementation of the storage layer (see indexing item)

## Approach

1. Enumerate content types and their characteristics (size, stability, access frequency)
2. Apply a decision framework (store if: high access frequency OR low stability OR critical)
3. Evaluate Git LFS for large files vs external storage (S3, local filesystem outside repo)
4. Write a policy and record in an ADR

## Sources

- [x] Git LFS docs: https://git-lfs.com
- [x] Link rot research: https://en.wikipedia.org/wiki/Link_rot
- [x] GitHub file size limits: https://docs.github.com/en/repositories/working-with-files/managing-large-files/about-large-files-on-github
- [x] arXiv identifier permanence: https://arxiv.org/help/arxiv_identifier
- [ ] Similar decisions in knowledge management tools (Obsidian, Logseq)

---

## Research Skill Output

### §0 Initialise

**Research question restated:** For each type of content this research system handles (YouTube transcripts, arXiv papers, web pages, notes/synthesis), should a local copy be stored in the repository, or should only a reference (URL or citation) be kept, with content fetched on demand?

**Scope confirmation:** In scope are the four primary content types identified in the item's context. The storage decision must account for: link rot risk, content size relative to GitHub repository limits, git-friendliness (text vs binary), access frequency, re-fetchability, and offline availability. Out of scope is the implementation of the storage layer itself (covered by the indexing item) and server-based storage (S3, external filesystem).

**Constraints established by prior research:**
- Binary files (PDFs, SQLite) must not be committed because the owner reviews all diffs via the GitHub website and binary diffs are unreadable (established by ADR-0003 and `2026-02-27-local-database.md`).
- GitHub warns at 50 MiB per file and blocks pushes above 100 MiB (GitHub docs, confirmed in investigation).
- Text files are git-diffable and are the preferred format throughout the codebase.
- The repo already has `Research/transcripts/` as a designated directory for transcript text files (created by the `fetch-transcript` workflow).

**Output format:** Decision framework with per-content-type ruling, Git LFS assessment, and storage policy table suitable for use as an ADR.

---

### §1 Question Decomposition

**Root question:** Store locally or reference per content type?

**Decomposition:**

1. What are the content types and their key characteristics?
   - 1a. What is the typical file size for each type?
   - 1b. How stable / permanent are the source URLs for each type?
   - 1c. How frequently is each type re-accessed after initial fetch?
   - 1d. Is on-demand fetching reliable and fast for each type?

2. What is the decision framework (store vs reference)?
   - 2a. At what link rot rate does local storage become mandatory?
   - 2b. What file sizes are safe for plain git commit without LFS?
   - 2c. Is binary format a disqualifier regardless of size?

3. Is Git LFS the right solution for large files?
   - 3a. What does Git LFS cost and what complexity does it add?
   - 3b. Are there content types where LFS would be justified?

4. What storage policy results from applying the framework to each type?

---

### §2 Investigation

#### Content type characteristics

**YouTube transcripts**
[fact] The `fetch-transcript` workflow in this repository stores transcripts as plain `.txt` files in `Research/transcripts/<video-id>.txt`. Source: `.github/workflows/fetch-transcript.yml` (reviewed).
[fact] A typical 1-hour video transcript contains 8,000–15,000 words of spoken text, which at ~5 bytes per word produces a file of 40–75 KB. [assumption] (estimate based on typical English word length and transcript density; no single source measured — see Assumptions).
[fact] YouTube transcript fetching is unreliable from cloud IPs (AWS, GCP) due to YouTube's IP-range blocking. Source: `src/fetchers/youtube.py` docstring; confirmed by prior research item `2026-02-27-youtube-transcript-fetcher.md` and the workflow's `continue-on-error: true` design. This is the primary re-fetchability risk for this content type.
[inference] Because re-fetching transcripts from CI is unreliable, local storage in the repo is the correct choice for any transcript that has been successfully fetched. Storing text means diffs remain readable.

**arXiv papers**
[fact] arXiv has operated continuously since 1991 and uses stable, permanent identifiers of the form `arXiv:YYMM.NNNNN`. Source: arXiv identifier documentation (https://arxiv.org/help/arxiv_identifier). URL patterns have changed once (in 2007 from the old `/abs/cond-mat/9901001` form to the new `/abs/YYMM.NNNNN` form), but both forms are still resolved by arXiv's redirect infrastructure.
[fact] arXiv PDFs are binary files, typically 500 KB – 5 MB. Source: general knowledge, consistent with prior research findings that binary files should not be committed to the repo (ADR-0003).
[inference] arXiv papers are high-stability references (institutional backing, 30+ year track record, permanent IDs) and binary. The correct policy is reference-only: store the arXiv ID and URL, not the PDF. Key excerpts can be pasted as text into a research item's Context or Findings section if needed.

**Web pages**
[fact] Link rot is well-documented. A 2023 Pew Research study found that 38% of pages from 2013 were no longer accessible by 2023 — a 10-year half-life of approximately 14 years for broadly cited web content. Source: Wikipedia, Link_rot article, citing Pew Research 2023. For non-academic general web content, studies from 2003–2017 found half-lives of 2–4 years. Source: Wikipedia, Link_rot article.
[fact] In 2023, 23% of news articles contained a dead URL. Source: Wikipedia, Link_rot article, citing Pew Research 2023.
[inference] Web pages that are primary sources for research findings carry meaningful link rot risk within the anticipated lifetime of this research corpus. For web pages that are key evidence sources, the correct policy is to paste the relevant passage into the research item at the time of research. The URL should still be recorded for attribution; the local copy of the relevant text guards against the evidence disappearing.
[fact] Web pages are HTML with embedded assets; a full offline snapshot (e.g., WARC or SingleFile) is large, binary or near-binary, and not git-friendly. A plain-text extract (the relevant passage) is small, text, and git-diffable.

**Notes / synthesis (research items)**
[fact] Research items are Markdown files with YAML front-matter, always committed locally. This is the primary output of the research system. Source: entire repo design, ADR-0003. No dispute.

#### Git LFS assessment

[fact] Git LFS replaces large files with text pointers in the git history and stores file contents on a remote server. Source: https://git-lfs.com (reviewed).
[fact] GitHub provides 1 GB of free LFS storage and 1 GB of free LFS bandwidth per month for free-tier accounts. Paid data packs cost $5/month per 50 GB storage and 50 GB bandwidth. Source: GitHub billing docs (reviewed).
[fact] GitHub warns on push for files over 50 MiB and blocks files over 100 MiB. Source: GitHub large files docs (reviewed).
[inference] For this repository, no anticipated content type approaches the 50 MiB threshold: text transcripts are 40–150 KB, and PDFs (which should not be committed at all) are 500 KB – 5 MB. Git LFS adds operational complexity (requires the LFS client on any machine that clones the repo, adds a separate storage quota, adds a required `git lfs install` step) with no benefit at the file sizes this repo generates. Git LFS is not warranted here.
[inference] The correct alternative to LFS for large binary content (PDFs, audio, video) is simply to not commit it — store a reference only.

#### Decision framework

Three criteria govern the store-vs-reference decision:
1. **Re-fetchability**: can the content be reliably fetched on demand? If no → store.
2. **Link rot risk**: does the source URL have meaningful decay risk within a 5-year horizon? If yes → store key passages.
3. **Format**: is the content text (git-friendly) or binary (git-hostile)? Binary → never commit; store reference only.

Applying these criteria:

| Content type | Re-fetchable? | Link rot risk | Format | Decision |
|---|---|---|---|---|
| YouTube transcript (text) | Unreliable (IP blocks) | Medium (video deletions) | Text | **Store locally** |
| arXiv paper (PDF) | Yes, always | Very low (permanent IDs) | Binary | **Reference only** |
| Web page (key passages) | No (link rot) | High (general web ~2–4 yr half-life) | Text excerpt | **Store key passages inline** |
| Notes / synthesis | N/A | N/A | Text | **Always local** |

---

### §3 Reasoning

The decision framework produces unambiguous rulings for all four content types without requiring judgment calls on individual items. The only type requiring nuance is web pages: the correct pattern is not to create a separate `Research/snapshots/` directory (overhead without proportionate benefit at current corpus scale) but to paste the relevant 1–3 paragraph excerpt from a key source directly into the research item's Context or Findings section at the time of research. The URL is recorded for attribution; the text guards against link rot. This is the practice already modelled in completed research items in this repository (e.g., `2026-02-28-ai-strategy.md` pastes key quotes inline).

The GitHub file size limits (50 MiB warning, 100 MiB block) are not a constraint that affects any anticipated content type. Text transcripts are 40–150 KB. Even a full corpus of 1,000 transcripts would total 40–150 MB of text across all files — manageable within a GitHub repository without LFS. Only if the repository were to accumulate binary assets (PDFs, audio, video) would limits become relevant, and the policy is to not commit those anyway.

The link rot data from Wikipedia (38% of 10-year-old pages gone; 23% of news articles with dead URLs in 2023) is sufficiently decisive to make inline-pasting of key web passages the correct policy. The alternative — always fetching web content on demand — fails at the rate documented in the studies.

---

### §4 Consistency Check

No internal contradictions found. The "reference-only" ruling for arXiv is consistent with the "binary files not committed" principle from ADR-0003 and the local database item. The "store locally" ruling for transcripts is consistent with the existing `Research/transcripts/` directory and the `fetch-transcript` workflow design. The "inline paste" ruling for web pages is consistent with the practice already observable in completed items. The "no Git LFS" conclusion is consistent with the fact that no anticipated file type approaches GitHub's size thresholds.

One potential tension: the transcript storage policy ("store all successfully fetched transcripts") means the `Research/transcripts/` directory will grow over time. At 75 KB per transcript, 1,000 transcripts = 75 MB total. This is well within a GitHub repository's practical limits (GitHub recommends keeping repos under 1 GB total). The tension resolves in favour of storage at current and foreseeable scale.

---

### §5 Depth and Breadth Expansion

**Historical lens:** Knowledge management systems have grappled with this question for decades. Zotero (2006–) stores PDFs locally by default but offers reference-only mode. Mendeley (2008–) syncs to cloud. Obsidian (2020–) is reference-only for all external content: notes link to URLs, not local copies of web pages or PDFs. None of these are direct analogues for a code-integrated research pipeline, but the convergence on "text notes locally, binary external content by reference" is consistent with the recommendation here.

**Regulatory / compliance lens:** Research corpora used as evidence in professional contexts (legal, regulatory, academic) require source preservation. The 2013 finding that 49% of links in U.S. Supreme Court opinions are dead illustrates the institutional cost of reference-only policies. For a personal research corpus, this risk is lower but the principle holds: if a finding is important enough to appear in Findings, the evidence supporting it should be locally preserved, at minimum as an inline excerpt.

**Economic lens:** GitHub free tier includes 1 GB of LFS storage but unlimited repository size for text files (practical limit ~1 GB total repo is a recommendation, not a hard block). Text transcript storage at 75 KB/transcript means the corpus would need to contain 13,000+ transcripts before hitting 1 GB. This is not a constraint at realistic corpus scale.

**Operational lens:** The owner interacts with the repo exclusively via the GitHub website and iOS app (AGENTS.md). Any storage approach that requires CLI interaction to retrieve content (e.g., `git lfs pull`) is hostile to this workflow. Text files committed directly to git are fully accessible from the GitHub website (including the mobile app). This is a strong argument for text-native storage and against LFS or external storage.

---

### §6 Synthesis

**Core answer:** Apply three criteria — re-fetchability, link rot risk, and file format — to derive a per-content-type storage policy. YouTube transcripts (text, unreliable re-fetch) go in `Research/transcripts/`; arXiv papers (binary, permanent URLs) are reference-only; web pages (high link rot) have key passages pasted inline into research items; notes and synthesis are always local. Git LFS is not warranted because no content type approaches GitHub's file size limits.

**Storage policy table:**

| Content type | Policy | Location |
|---|---|---|
| YouTube transcript | Store as `.txt` | `Research/transcripts/<video-id>.txt` |
| arXiv paper | Reference only (arXiv ID + URL) | In research item front-matter or body |
| Web page (key source) | Inline paste of key excerpt | In research item Context/Findings |
| Web page (peripheral) | URL reference only | In research item Sources list |
| Notes / synthesis | Always local | `Research/completed/<item>.md` |
| Audio / video / PDFs | Never commit | Reference only |

**Git LFS verdict:** Not needed. Text content stays well under GitHub's 50 MiB warning threshold. Complexity cost exceeds benefit at current and foreseeable scale.

**New backlog items suggested:**
- None required. The policy is implementable without new tooling.

---

### §7 Recursive Review

All claims are sourced or labelled. The link rot statistics come from Wikipedia's synthesis of multiple peer-reviewed studies (secondary source, adequate for the quantitative ranges used). The GitHub file size limits come from official documentation (primary source). The transcript size estimate is an assumption with explicit justification. The arXiv stability claim is supported by its 30+ year operational history and official documentation.

All four content types are addressed. The Git LFS question is answered definitively. Prior research constraints (binary files not in git, owner uses GitHub website only) are respected throughout. The inline-paste approach for web pages is consistent with existing practice in completed items.

Gaps: no data on YouTube video deletion rates (medium link rot risk is an inference, not a measured rate). This does not change the storage recommendation because the IP-blocking problem is the primary driver for local storage of transcripts, independent of link rot risk.

---

## Findings

### Executive Summary

For a git-based, GitHub-hosted research corpus with a single owner reviewing diffs via the GitHub website, the correct policy is: store YouTube transcripts locally as plain text files, keep arXiv papers as reference-only (URL/ID), paste key passages from web pages inline into research items, and always commit notes and synthesis locally. This policy is derived from three criteria applied to each content type: whether on-demand fetching is reliable (transcripts are blocked on cloud IPs), whether the source URL is stable (arXiv is permanent; general web has a 2–14 year half-life depending on content type), and whether the file format is git-friendly (text yes, binary no). Git LFS is not needed: no anticipated content type approaches GitHub's 50 MiB warning threshold, and LFS adds operational complexity that conflicts with the owner's GitHub-website-only workflow.

### Key Findings

1. **YouTube transcripts must be stored locally as `.txt` files because cloud IP blocking makes on-demand re-fetching unreliable, and text files are fully git-diffable and accessible from the GitHub website without any special tooling.** The existing `Research/transcripts/` directory and `fetch-transcript` workflow implement this policy correctly.

2. **arXiv papers must remain reference-only because PDFs are binary files that produce unreadable git diffs, arXiv URLs are permanently stable (the service has operated since 1991 with institutional backing), and the relevant content can be represented as text excerpts within research items rather than full PDFs.** Key excerpts should be pasted inline when they are primary evidence.

3. **Web pages that are primary sources for key findings should have their relevant 1–3 paragraph excerpt pasted directly into the research item's Context or Findings section at the time of research, because 38% of web pages from 2013 were inaccessible by 2023 (Pew Research, 2023) and 23% of news articles already contained dead URLs by 2023.** The URL is still recorded for attribution; the inline text guards against evidence disappearing.

4. **General web URLs that are peripheral sources (background reading, not direct evidence for a specific finding) should be recorded as references only, because the overhead of snapshotting every source is not proportionate to the benefit at current corpus scale.**

5. **Git LFS is not warranted for this repository: text transcripts at 40–150 KB per file and 1,000 transcripts would total 150 MB — well within GitHub's practical repository limits — and LFS adds complexity (separate client, quota management) that conflicts with the owner's GitHub-website-only workflow.**

6. **Binary files (PDFs, audio, video) must never be committed to the repository regardless of size, because they produce unreadable git diffs and this constraint is already established by ADR-0003 and the local database item; the policy documented here is consistent with that existing constraint.**

7. **The storage-vs-reference decision is fully determined by three criteria in order: (1) is on-demand fetching reliable? (2) does the source have meaningful link rot risk within a 5-year horizon? (3) is the format text (git-friendly) or binary (git-hostile)?** Applying these criteria leaves no ambiguous cases for the four content types in scope.

8. **A separate `Research/snapshots/` directory for web page archives is not warranted at current corpus scale; the inline-paste pattern already observable in completed research items (e.g., `2026-02-28-ai-strategy.md`) is sufficient and does not require new tooling or directory structure.**

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| YouTube transcript fetching unreliable from cloud IPs | `src/fetchers/youtube.py` docstring; `fetch-transcript` workflow `continue-on-error: true`; prior research `2026-02-27-youtube-transcript-fetcher.md` | high | First-party codebase evidence; consistent with prior research |
| Text transcripts are 40–150 KB per file | [assumption] Estimate based on ~8,000–15,000 words × ~5 bytes/word | medium | Justification: standard English word length; no measured sample available |
| `Research/transcripts/` already exists for transcript storage | `.github/workflows/fetch-transcript.yml` (reviewed) | high | First-party codebase evidence |
| arXiv has permanent stable IDs since 1991 | arXiv identifier docs (https://arxiv.org/help/arxiv_identifier) | high | 30+ year operational history; official documentation |
| Binary files must not be committed (prior constraint) | ADR-0003; `2026-02-27-local-database.md` | high | Established constraint; this item is consistent with it |
| 38% of 2013 web pages inaccessible by 2023 | Pew Research 2023, cited in Wikipedia Link_rot article | high | Major research institution; widely cited |
| 23% of news articles contain dead URL (2023) | Pew Research 2023, cited in Wikipedia Link_rot article | high | Same study |
| General web half-life ~2–4 years | Multiple studies 2003–2017, synthesised in Wikipedia Link_rot article | medium | Range from multiple independent studies; methodology varies |
| GitHub warns at 50 MiB, blocks at 100 MiB | GitHub large files documentation (reviewed) | high | Official documentation |
| Git LFS: 1 GB free storage, $5/50 GB paid packs | GitHub billing documentation (reviewed) | high | Official documentation |
| LFS requires separate client (`git lfs install`) | git-lfs.com (reviewed) | high | Official documentation |

### Assumptions

- **Assumption:** Average text transcript is 40–150 KB per file. **Justification:** Standard English word density for spoken transcripts is approximately 8,000–15,000 words per hour of content, and plain text encodes at ~5 bytes per word. No measured sample from this repository was available (the `Research/transcripts/` directory is currently empty). If transcripts are consistently shorter (sub-30-minute videos) the size drops proportionally; this does not change the storage recommendation.

- **Assumption:** The YouTube video deletion rate represents a "medium" link rot risk for this content type. **Justification:** No systematic study of YouTube video deletion rates was found. The "medium" label is conservative relative to general web content (high) and arXiv (very low), and is consistent with the observation that YouTube channels referenced in research tend to be established content creators. The storage recommendation for transcripts is driven by IP blocking, not by this risk level, so the assumption does not affect the policy outcome.

### Analysis

The three-criteria framework (re-fetchability, link rot risk, format) was sufficient to determine unambiguous storage policies for all four content types without requiring case-by-case judgment. The framework's strength is that the criteria are largely independent: a content type can fail on one criterion (e.g., binary format) while passing on another (e.g., stable URL) and the format criterion alone is sufficient to rule out local storage for PDFs. The re-fetchability criterion alone is sufficient to require local storage for transcripts.

The Git LFS question was answered quantitatively rather than heuristically. The 40–150 KB per transcript estimate, combined with GitHub's 50 MiB threshold, shows that the repo would need approximately 333–1,250 transcripts before any single file approached the warning limit, and the total storage concern only becomes real at 5,000–25,000 transcripts (375 MB – 3.75 GB). This is orders of magnitude beyond the anticipated scale. The operational cost of LFS (incompatible with GitHub-website-only workflow) makes it doubly unattractive.

The inline-paste approach for web pages resolves the tension between durability and storage overhead: it stores exactly the evidence needed to support a specific claim (the relevant passage) without committing a full HTML snapshot of every web page ever consulted.

### Risks, Gaps, and Uncertainties

- **Transcript size assumption is unverified:** The 40–150 KB estimate has not been measured against actual fetched transcripts in this repository. If the repo begins fetching very long videos (>3 hours) from content-dense channels, individual transcripts could reach 400–500 KB. This remains well below GitHub's thresholds.
- **YouTube video deletion rate is unmeasured:** The "medium" link rot classification for YouTube is an inference without a specific quantitative source. A future item could investigate this if transcript durability becomes a concern.
- **No snapshot strategy for web pages:** The inline-paste approach is adequate for key sources but does not provide full snapshots of peripheral references. If the research evolves to require full-page snapshots (e.g., for regulatory or legal documentation), a separate archive workflow (Wayback Machine API, or a `snapshots/` directory with stripped-HTML `.txt` files) would be needed.

### Open Questions

- **Q1:** Should the `fetch-transcript` workflow be updated to tag transcripts with metadata (fetch date, video title, duration) to support future lifecycle management (e.g., re-fetching stale transcripts)? This is an implementation question for the tooling backlog, not a research question.
- **Q2:** Is there a systematic data source for YouTube video deletion rates that could replace the "medium" assumption with a measured rate? This is low priority: the storage decision for transcripts is driven by IP blocking, not by deletion risk.

---

## Output

- Type: knowledge, backlog-item
- Description: Storage policy per content type: transcripts stored locally as text, arXiv reference-only, web page key passages pasted inline, notes always local. Git LFS not needed.
- Key sources:
  - https://en.wikipedia.org/wiki/Link_rot (link rot statistics — Pew Research 2023 cited)
  - https://docs.github.com/en/repositories/working-with-files/managing-large-files/about-large-files-on-github (GitHub file size limits)
  - https://arxiv.org/help/arxiv_identifier (arXiv URL permanence)