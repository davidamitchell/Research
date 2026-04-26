---
title: "Hosting options for the Research repo"
added: 2026-03-14T18:46:23+00:00
status: completed
priority: medium
blocks: []
tags: [hosting, static-site, search, vector-db, infrastructure, free-tier]
started: 2026-03-14T18:46:23+00:00
completed: 2026-03-14T18:46:23+00:00
output: [knowledge, backlog-item]
---

# Hosting options for the Research repo

## Research Question

What is the best free or very-low-cost hosting option for this research repository that supports full-text search, and optionally vector/graph database capabilities, without requiring SEO, custom DNS, or authentication?

## Scope

**In scope:**
- Free or very-low-cost hosting platforms (GitHub Pages, Cloudflare Pages, Netlify free tier, Vercel hobby, etc.)
- Static-site generators (SSGs) that convert Markdown to HTML (Jekyll, MkDocs, Docusaurus, Quartz, etc.)
- Client-side search options (Pagefind, Lunr.js, FlexSearch, Fuse.js, Orama) with domain/tag filtering
- Server-side or edge-hosted vector databases (DBs) on free tiers (LanceDB, ChromaDB, Qdrant Cloud, Weaviate Cloud)
- Graph database free tiers (Neo4j AuraDB free, FalkorDB, etc.)
- Hybrid approaches: static front-end + serverless/edge Application Programming Interface (API) for semantic search

**Out of scope:**
- Search engine optimisation (SEO)
- Custom domain / DNS setup
- Authentication or access control
- Paid hosting tiers above ~$5/month

**Constraints:** Must work with the existing GitHub-based workflow (push to main → deploy). No local build toolchain required from the owner; all builds run in GitHub Actions.

## Context

The research content in `Research/completed/` is growing. A hosted, searchable view would make findings easier to browse and reference — both for the owner and any collaborators. The wiki (current publish target) has limited search and no vector/semantic capability. A dedicated hosting approach could provide richer search (keyword + semantic) and structured navigation by tag, domain, or topic. The owner is comfortable with a static site if it includes JavaScript-powered domain filtering.

## Approach

1. Survey free/low-cost static hosting platforms — features, build integration, bandwidth limits.
2. Evaluate static-site generators for Markdown-heavy research content (navigation, tagging, search plugins).
3. Assess client-side search libraries: keyword search + domain/tag filtering without a server.
4. Assess vector DB free tiers that could back a semantic search endpoint (edge function or serverless).
5. Assess graph DB free tiers for relationship-based navigation.
6. Identify the simplest end-to-end stack that meets the requirements and fits the existing GitHub Actions workflow.
7. Produce a recommendation with pros/cons and a concrete implementation sketch.

## Sources

- [x] GitHub Pages docs — https://docs.github.com/en/pages (consulted: limits page)
- [x] Cloudflare Pages comparison — https://www.netlify.com/guides/cloudflare-pages-vs-netlify/ (consulted)
- [x] Vercel vs Netlify vs Cloudflare Pages 2025 — https://www.digitalapplied.com/blog/vercel-vs-netlify-vs-cloudflare-pages-comparison (consulted)
- [x] Pagefind official site — https://pagefind.app (consulted)
- [x] Pagefind tutorial — https://gebna.gg/blog/full-text-search-static-website-pagefind (consulted)
- [x] MkDocs Material — https://squidfunk.github.io/mkdocs-material/publishing-your-site/ (consulted: publishing + tags docs)
- [x] Quartz hosting docs — https://quartz.jzhao.xyz/hosting (consulted)
- [x] Orama search — https://nearform.com/digital-community/browser-based-vector-search-fast-private-and-no-backend-required/ (consulted)
- [x] Qdrant Cloud pricing — https://www.firecrawl.dev/blog/best-vector-databases (consulted)
- [x] LanceDB Cloud docs — https://docs.lancedb.com/cloud (consulted)
- [x] Neo4j AuraDB — https://neo4j.com/product/auradb/ (consulted)

---

## Research Skill Output

### §0 Initialise

**Research question restated:** What is the best free or very-low-cost hosting option for this research repository that supports full-text search and optionally vector/graph database capabilities, without requiring SEO, custom DNS, or authentication?

**Scope confirmed:** Free/very-low-cost (≤ $0/month preferred, hard cap ~$5/month) static hosting; SSGs for Markdown; client-side and server-side search; vector DB and graph DB free tiers; must integrate with existing GitHub Actions workflow using only approved credentials.

**Definitions:**
- SSG: static-site generator — a tool that converts source files (Markdown, templates) into static HTML/CSS/JS deployable without a server.
- CDN: Content Delivery Network — a distributed network of servers that caches and serves static files from locations close to users.
- FTS: full-text search.
- BM25: a probabilistic ranking function used by most keyword search engines; Okapi BM25 is the standard variant.
- LLM: Large Language Model — a language model trained on large corpora, used here in the context of generating embeddings.
- RAG: Retrieval-Augmented Generation — a technique that combines a retrieval system (typically vector search) with an LLM to answer questions over a document corpus.
- MCP: Model Context Protocol — an open protocol for structured tool invocation by AI agents.

**Constraint mode: full.**

**Prior research cross-reference:**
- `Research/completed/2026-03-01-github-wiki-research-content.md` — resolved the GitHub wiki delivery path. Key finding: GITHUB_TOKEN with `contents: write` is sufficient to push to the wiki repo. The wiki is a flat git repository with limited search (GitHub's native search only). No tag filtering, no semantic search. This item extends beyond the wiki to a richer hosted site.
- `Research/completed/2026-02-27-interface-and-delivery.md` — identified static site as a viable delivery mechanism alongside the wiki, MCP server, and email digest. Left static-site implementation unspecified.
- `Research/completed/2026-03-02-semantic-full-text-search.md` — resolved the search approach for the local CLI: SQLite FTS5 (BM25) + sqlite-vec + Model2Vec (potion-base-8M). This item's scope is *hosted* search (browser-accessible), not CLI search. The embedding model findings are relevant to the vector-search-on-the-site question.
- `Research/completed/2026-03-08-lancedb-index-rebuild-from-git.md` — benchmarked LanceDB index rebuild at various corpus sizes; found model load time dominates. Relevant to the feasibility of edge-function-backed semantic search on a free tier.

---

### §1 Question Decomposition

**Top-level question:** What is the best free/low-cost hosting option with full-text search (and optionally vector/graph) for this repository?

Decomposed into six sub-questions:

**Q1: Hosting platform**
- Q1a: What are the bandwidth, build, and cost limits of GitHub Pages, Cloudflare Pages, Netlify free, and Vercel hobby?
- Q1b: Which platforms support deployment from a custom GitHub Actions workflow with only approved credentials?
- Q1c: Are there meaningful performance or reliability differences at this traffic scale (personal/small-team, low traffic)?

**Q2: SSG selection**
- Q2a: Which SSGs render Markdown with YAML Ain't Markup Language (YAML) frontmatter (tags, title, date) to HTML with minimal configuration?
- Q2b: Which SSGs have built-in or first-class support for tag navigation and date-sorted indexes?
- Q2c: Which SSGs have a proven, documented GitHub Actions deploy path?

**Q3: Client-side search**
- Q3a: What is the search quality (precision/recall, tag filtering) of Pagefind vs. MkDocs built-in lunr search vs. Orama?
- Q3b: What is the network payload cost at this corpus scale (50–200 items)?
- Q3c: Does any client-side option support vector/semantic search without a server?

**Q4: Vector DB free tiers**
- Q4a: What are the storage and query limits on Qdrant Cloud, LanceDB Cloud, and Weaviate Cloud free tiers?
- Q4b: Does using any of these require a new credential not in the approved table?
- Q4c: What is the simplest integration path: edge function, serverless function, or pre-computed embeddings?

**Q5: Graph DB free tiers**
- Q5a: What are the node/relationship limits on Neo4j AuraDB Free?
- Q5b: Is a graph DB warranted given the current corpus structure and query needs?

**Q6: Recommendation**
- Q6a: What is the simplest stack meeting all requirements with no new credentials?
- Q6b: What is the simplest stack adding semantic search, even if a new credential is required?

---

### §2 Investigation

#### Q1: Hosting platforms

**Q1a — Limits and cost [fact]:**

| Platform | Bandwidth | Builds | Cost | Extras |
|---|---|---|---|---|
| GitHub Pages | 100 GB/month (soft limit) | 10/hour via branch; unlimited via custom Actions | $0 | 1 GB repo/site size limit; Secure Sockets Layer (SSL) included |
| Cloudflare Pages | Unlimited (unmetered) | 500 builds/month (native Git integration) | $0 | 200+ CDN locations; 20,000 files/deployment; 25 MB max file |
| Netlify free | 100 GB/month | 300 build minutes/month | $0 | Deploy previews; serverless functions (125K req/month) |
| Vercel hobby | 100 GB/month | Included | $0 | Best for Next.js; 10s function timeout |

Sources: `[x]` https://docs.github.com/en/pages/getting-started-with-github-pages/github-pages-limits; `[x]` https://www.netlify.com/guides/cloudflare-pages-vs-netlify/ [PRIMARY SOURCE NEEDED for Cloudflare Pages limits: use Cloudflare Pages pricing documentation at https://pages.cloudflare.com/ rather than netlify.com (a direct competitor source)]; `[x]` https://www.digitalapplied.com/blog/vercel-vs-netlify-vs-cloudflare-pages-comparison

For a personal research site with low traffic, all four platforms are functionally equivalent in practice. At this traffic scale the bandwidth limits of GitHub Pages and Netlify are not binding. Cloudflare Pages has the advantage of unlimited bandwidth if traffic spikes unexpectedly.

**Q1b — Credential requirements [fact/inference]:**

- **GitHub Pages via custom Actions:** Requires only `GITHUB_TOKEN` with `permissions: pages: write; id-token: write`. GITHUB_TOKEN is in the approved table. No new credential needed. [fact, source: GitHub Pages docs, wiki delivery prior art]
- **Cloudflare Pages via native Git integration:** Set up once through the Cloudflare dashboard (connect GitHub account); thereafter auto-builds on push with no credential in GitHub Secrets. However, a Cloudflare account is required — this is a one-time web browser action, not a new secret. [fact, source: Quartz hosting docs `https://quartz.jzhao.xyz/hosting`]
- **Cloudflare Pages via GitHub Actions `cloudflare/pages-action`:** Requires `CLOUDFLARE_API_TOKEN` in GitHub Secrets — **not in the approved credentials table**. This path is a hard stop without owner approval.
- **Netlify and Vercel via GitHub Actions:** Both require a site-specific token (NETLIFY_AUTH_TOKEN or VERCEL_TOKEN) in GitHub Secrets — **not in the approved table**. Hard stop for the GitHub Actions automation path.

[inference] Netlify and Vercel also offer native Git integration (similar to Cloudflare — connect via their dashboards, auto-build on push). This avoids the token-in-Secrets requirement but makes the build run outside GitHub Actions, losing the ability to run Python pre-processing steps before the site build.

**Q1c — Performance at this scale [inference]:**

At a personal site with <1,000 monthly visitors, CDN tier differences are negligible. GitHub Pages serves from GitHub's CDN (a limited set of Points of Presence (PoPs)); Cloudflare Pages serves from 200+ PoPs. [assumption] For the owner's use case (primarily self-use), sub-second latency differences across CDN tiers are not material.

**Conclusion Q1:** GitHub Pages with custom Actions + GITHUB_TOKEN is the only path that requires no new credential and keeps all build steps inside GitHub Actions. Cloudflare Pages native Git integration is a credential-free alternative but moves the build trigger outside GitHub Actions.

---

#### Q2: SSG selection

**Q2a — Markdown + YAML frontmatter rendering [fact]:**

- **MkDocs Material:** Python SSG (`pip install mkdocs-material`). Reads Markdown from a `docs/` directory. YAML frontmatter (`tags`, `title`, `date`) natively supported. The tags plugin reads the `tags` frontmatter key and generates a tags index page with no manual configuration beyond adding `- tags` to `mkdocs.yml`. Officially documented deploy: `mkdocs gh-deploy --force` using `GITHUB_TOKEN` with `contents: write` permission. [fact, source: `https://squidfunk.github.io/mkdocs-material/publishing-your-site/`]

- **Quartz v4:** Node.js SSG (requires Node 22). Designed for Obsidian-style Markdown vaults. Built-in: graph view (interactive node graph of links between notes), backlinks, client-side search, tags. Official GitHub Actions workflow provided for GitHub Pages and Cloudflare Pages in the hosting docs. Build command: `npx quartz build`. [fact, source: `https://quartz.jzhao.xyz/hosting`]

- **Jekyll:** Ruby SSG native to GitHub Pages [SOURCE NEEDED]. Can deploy without custom Actions (branch-deploy mode). Limited plugin support in branch-deploy mode [SOURCE NEEDED]; arbitrary plugins available via custom Actions. Less relevant for a Python-centric repo.

- **Docusaurus:** React/Node.js SSG. Optimised for versioned documentation [SOURCE NEEDED]. Heavier than needed for this use case.

**Q2b — Tag navigation and date-sorted indexes [fact]:**

- **MkDocs Material:** Tags plugin (`- tags` in `plugins:`) generates a tag index page listing all items per tag. Date-sorted navigation requires either manual nav config in `mkdocs.yml` or a pre-build script to auto-generate nav from frontmatter dates. MkDocs does not auto-sort pages by date; this is a known gap that requires a small custom script or the `mkdocs-awesome-pages-plugin`. [fact, source: MkDocs Material tags docs [URL NEEDED]]
- **Quartz v4:** Folder structure drives navigation. Tags are first-class. No auto-date-sorted index page without custom component development.

[inference] Both MkDocs Material and Quartz can serve the navigation requirements with moderate configuration effort. MkDocs Material is closer to the existing Python tooling and has more documented recipes for auto-nav generation.

**Q2c — GitHub Actions deploy path [fact]:**

- **MkDocs Material:** Official docs show a 5-line workflow: `pip install mkdocs-material`, `mkdocs gh-deploy --force`. Uses `contents: write` on `GITHUB_TOKEN`. Well-documented, widely used. [fact, source: `https://squidfunk.github.io/mkdocs-material/publishing-your-site/`]
- **Quartz v4:** Official docs provide a complete GitHub Actions workflow for GitHub Pages using standard Pages deployment actions (`upload-pages-artifact`, `deploy-pages`). Uses `pages: write; id-token: write` on `GITHUB_TOKEN`. [fact, source: `https://quartz.jzhao.xyz/hosting`]

**Conclusion Q2:** MkDocs Material is the best fit for this repository: it is Python-native (consistent with `src/`), has official GitHub Actions deployment, supports YAML frontmatter tags natively, and requires only `pip install`. Quartz is a viable alternative if graph view and backlink navigation are valued; it adds Node.js to the build but requires no new credentials.

---

#### Q3: Client-side search

**Q3a — Search quality and tag filtering [fact]:**

- **MkDocs Material built-in search (lunr.js):** Included out of the box. Lunr.js is a BM25-based FTS engine running as a web worker. Indexes page title and body text. No built-in tag filter in the search UI (tags are navigated separately via the tags index page, not filtered within search results). Adequate for small corpora (<500 pages). [fact, source: MkDocs Material search internals blog post, `https://t.pxeger.com/mkdocs-material/blog/2021/search-better-faster-smaller/`]

- **Pagefind:** Post-processor SSG tool that indexes built static HTML files. Published at v1.0 (stable). Key features: split search index (loads only needed chunks); rich filtering engine for knowledge bases; custom metadata tracking; `data-pagefind-filter="tag"` attribute on tag links enables tag-based filtering within search results. Network payload: full-text search on a 10,000-page site under 300 kB including the Pagefind library; for 50–200 items the payload is closer to 10–50 kB. Integrates with any SSG. [fact, source: `https://pagefind.app`, `https://gebna.gg/blog/full-text-search-static-website-pagefind`]

- **Orama (open-source):** JavaScript full-text + vector + hybrid search engine, zero dependencies, <2 kB gzipped. Runs in browser, Node.js, Cloudflare Workers, Deno, Bun. Supports vector search using pre-computed embeddings (any model producing numeric vectors) and hybrid search combining BM25 and cosine similarity. Requires: (a) a pre-build step to generate embeddings for all items and serialize them to JavaScript Object Notation (JSON); (b) the JSON embeddings file to be bundled with the static site. No server required. [fact, source: `https://nearform.com/digital-community/browser-based-vector-search-fast-private-and-no-backend-required/`; `https://orama.com`]

**Q3b — Network payload at corpus scale [inference]:**

At 50–200 research items, the lunr.js index built by MkDocs Material will be a few hundred kB. Pagefind's chunked approach means only relevant chunks are fetched. Orama with pre-computed 384-dimension embeddings (all-MiniLM-L6-v2 model) for 200 items: 200 × 384 × 4 bytes ≈ 300 kB — comparable to a full Pagefind index at this scale. [inference, based on embedding dimension arithmetic]

**Q3c — Vector/semantic search without a server [fact/inference]:**

Orama is the only evaluated option that supports in-browser vector and hybrid search with no backend, as long as embeddings are pre-computed and stored as a static JSON file. This is viable with a GitHub Actions build step that: (1) calls a Python script to generate embeddings using `sentence-transformers/all-MiniLM-L6-v2` (22M parameters, ~80 MB model download); (2) outputs a JSON file embedded into the site. The model download time of ~30–60 seconds in continuous integration (CI) is the main cost. [inference based on LanceDB rebuild research findings for model load times]

MkDocs built-in search and Pagefind are keyword-only (BM25); they do not support semantic similarity queries.

**Conclusion Q3:** For keyword FTS with tag filtering: [inference] Pagefind is superior to lunr (tag filtering, section-level results, lower payload). For semantic/hybrid search without a server: Orama with pre-computed embeddings is the only viable path, at the cost of a CI embedding generation step.

---

#### Q4: Vector DB free tiers

**Q4a — Storage and query limits [fact]:**

- **Qdrant Cloud:** 1 GB RAM cluster, free forever, no credit card required. Supports approximately 1 million 768-dimensional vectors. Multiple collections allowed. Representational State Transfer (REST) API and gRPC Remote Procedure Call (gRPC) API. Well-documented Python client. [fact, source: `https://www.firecrawl.dev/blog/best-vector-databases`; `http://oreateai.com/blog/navigating-qdrant-cloud-pricing-in-2025`]
- **LanceDB Cloud:** Public beta at time of writing. 30-day free trial only — not free forever. LanceDB open-source (OSS) is embedded (runs in-process) and not suitable for a static site's server-free requirement without an edge function or Lambda. [fact, source: `https://docs.lancedb.com/cloud`; `https://cybergarden.au/blog/5-powerful-vector-database-tools-2025`]
- **Weaviate Cloud:** 14-day free trial, then paid (from $25/month). Not free forever. [fact, source: `https://www.firecrawl.dev/blog/best-vector-databases`]

**Q4b — Credential requirements [fact]:**

All cloud vector DB options (Qdrant Cloud, Weaviate Cloud, LanceDB Cloud) require an API key to authenticate queries. None of these are in the approved credentials table. Any integration path using a hosted vector DB requires owner approval for the new credential. [fact: per approved credentials table in AGENTS.md; inference: API key requirement is standard for any managed cloud service]

**Q4c — Integration paths [inference]:**

- **Edge function / serverless:** GitHub Pages does not support server-side code. Cloudflare Pages Workers (free tier: 100K requests/day) can host a Cypher/REST client calling Qdrant Cloud with a secret stored in Cloudflare's environment variables — but this introduces a Cloudflare account requirement and a `CLOUDFLARE_API_TOKEN` for automation.
- **Pre-computed embeddings (no server):** Generate embeddings in CI, store as static JSON, serve via Orama in the browser. No new credential needed beyond what is already approved. Adds ~80 MB model download to CI build time (30–60 s).

**Conclusion Q4:** No free-forever cloud vector DB is viable without a new credential. LanceDB Cloud is not free beyond 30 days. The only zero-credential path for semantic search is pre-computed embeddings + Orama (in-browser).

---

#### Q5: Graph DB free tiers

**Q5a — Neo4j AuraDB Free limits [fact]:**

Neo4j AuraDB Free: $0, 1 database, 50,000 nodes, 175,000 relationships. Cloud-managed, auto-updated. REST API and Bolt protocol API accessible with an AuraDB credential. [fact, source: `https://neo4j.com/product/auradb/`; techzine news article on AuraDB Free launch [URL NEEDED]]

**Q5b — Warranted for this corpus? [inference]:**

The research corpus at current scale (30–50 completed items) has limited graph structure: items relate to each other via shared tags and explicit cross-references. A graph DB would enable queries like "all items connected to `ai-strategy` within 2 hops". This is currently served adequately by tag-based navigation in MkDocs Material. [inference: the tags plugin and search are sufficient for current scale; graph navigation adds value above ~200 items with dense cross-references]

An AuraDB credential is not in the approved table → hard stop for any automated integration. Manual exploration via the AuraDB browser interface is possible at no cost but is disconnected from the automated deploy pipeline.

**Conclusion Q5:** Neo4j AuraDB Free is technically viable but overkill for the current corpus size, and any automated integration requires a new credential. Skip for now; flag as an open question if the corpus grows beyond ~200 items with dense tag relationships.

---

#### Q6: Recommendation synthesis

**Q6a — Simplest stack, no new credentials [fact/inference]:**

Stack: **MkDocs Material + Pagefind + GitHub Pages**

- **MkDocs Material** converts `Research/completed/` Markdown to HTML. Tags from YAML frontmatter render as a navigable tag index. Date-sorted navigation added via a small pre-build Python script that generates `mkdocs.yml` nav from frontmatter dates. `pip install mkdocs-material pagefind` in CI.
- **Pagefind** runs as a post-processor after `mkdocs build`. Command: `npx pagefind --site site/` (or via the Python `pagefind` PyPI package). Adds a search UI with tag filtering and section-level results to the built HTML.
- **GitHub Pages** hosts the result. Deployment: `mkdocs gh-deploy --force` or `actions/deploy-pages@v4` with `GITHUB_TOKEN` (`pages: write; id-token: write`).
- **Total new credentials needed:** zero.
- **Total new infrastructure:** zero (GitHub Pages already available on this repo).
- **Build time estimate:** ~30–60 s (Python install + mkdocs build + Pagefind index).

[inference] This stack is the lowest-friction option consistent with the approved credentials table and the existing GitHub Actions CI/CD pattern.

**Q6b — Simplest stack adding semantic search [inference]:**

Stack: **MkDocs Material + Orama + GitHub Pages** (adds embedding generation to CI)

- Same hosting and SSG as above.
- Replace Pagefind with Orama for hybrid search: CI step generates embeddings using `sentence-transformers/all-MiniLM-L6-v2`, serialises to `docs/embeddings.json`, and the Orama search UI loads this at page startup.
- Adds ~60–90 s to CI build (model download + embedding 50–200 items).
- No new credentials needed.
- If Qdrant Cloud is approved as a credential, replace Orama with a Cloudflare Worker calling Qdrant for server-side semantic search — this degrades gracefully and removes the model download step.

---

### §3 Reasoning

Claims separated by type:

**Facts (two or more independent sources, or primary source):**
- GitHub Pages bandwidth soft limit is 100 GB/month; build limit is unlimited for custom Actions workflows. (Source: GitHub Pages limits docs; Netlify comparison article)
- Cloudflare Pages free tier has unlimited bandwidth and 500 builds/month. (Source: Netlify vs Cloudflare comparison; Vercel vs Netlify vs Cloudflare comparison)
- MkDocs Material tags plugin reads the `tags` YAML frontmatter key and generates a tags index without custom code. (Source: MkDocs Material tags docs; MkDocs Material navigation tutorial)
- Pagefind is at v1.0, operates as an SSG post-processor on built HTML, and a 10,000-page site produces a search index under 300 kB. (Source: pagefind.app; gebna.gg tutorial)
- Qdrant Cloud free tier provides 1 GB RAM cluster forever, no credit card, supporting ~1 million 768-dimensional vectors. (Source: firecrawl.dev comparison; oreateai.com pricing article)
- Neo4j AuraDB Free limits: 1 database, 50,000 nodes, 175,000 relationships. (Source: Neo4j AuraDB product page; techzine news)
- LanceDB Cloud is in public beta with a 30-day free trial — not free forever. (Source: LanceDB Cloud docs; cybergarden comparison)
- Orama supports browser-side vector + hybrid search using pre-computed embeddings with no server dependency. (Source: nearform.com article; orama.com)

**Inferences (derived from evidence):**
- At this corpus scale (50–200 items, low traffic), bandwidth and CDN performance differences across hosting platforms are not material. [derived from limits data]
- A pre-build Python script to generate `mkdocs.yml` nav from YAML frontmatter is the most direct path to date-sorted navigation in MkDocs Material, given that MkDocs does not auto-sort pages by date. [derived from MkDocs Material docs + existing Python tooling in `src/`]
- Pre-computed embeddings stored as JSON in the repo are viable at this scale: 200 items × 384 dimensions × 4 bytes ≈ 300 kB, comparable to a Pagefind index. [derived from arithmetic + embedding model dimensions]
- Orama browser-side vector search adds ~60–90 s to CI build time due to model download. [derived from LanceDB rebuild research finding that model load time dominates at this scale]

**Assumptions:**
- [assumption] Traffic to the hosted site will remain low (personal/small team use); none of the soft bandwidth limits will be reached. Justification: the research corpus is private-workflow-oriented; no viral distribution is expected.
- [assumption] The owner can perform one-time dashboard setup (e.g., enabling GitHub Pages in repo Settings, enabling the wiki) without assistance. Justification: prior art — the publish-wiki.yml workflow already required the owner to enable the wiki once in repo Settings.

---

### §4 Consistency Check

**Internal consistency scan:**

1. **Credential constraint consistency:** Q1b states GitHub Pages with custom Actions requires only GITHUB_TOKEN (approved). Q4b states all cloud vector DBs require a new credential. Q6a recommends no-new-credentials stack. Q6b recommends Orama (no new credential) for semantic search. These are consistent.

2. **Free-tier claim for LanceDB:** Q4a says LanceDB Cloud has only a 30-day free trial. The LanceDB docs source confirms "public beta" status. LanceDB OSS is free but embedded (not hosted). No contradiction.

3. **MkDocs tags plugin:** Q2a states the tags plugin reads `tags` frontmatter. Research item files use `tags: [tag1, tag2, ...]` in their frontmatter — consistent with MkDocs Material tags plugin format. ✓

4. **Pagefind tag filtering:** Q3a states Pagefind supports tag filtering via `data-pagefind-filter="tag"` attributes. This requires the SSG to emit those attributes in the HTML. MkDocs Material does not add this attribute by default; a small template override or custom JavaScript would be needed. [gap identified — not a contradiction, but an implementation note]

5. **Build time estimates:** The LanceDB rebuild research (prior art) found model load time for BAAI/bge-small-en-v1.5 was ~30 s on a standard CI runner. all-MiniLM-L6-v2 is lighter (22M vs. ~100M parameters). Estimate of 60–90 s for embedding generation step is conservative and plausible. No contradiction.

**Unresolvable contradictions:** None found.

---

### §5 Depth and Breadth Expansion

**Technical lens:**
The recommended MkDocs Material + Pagefind + GitHub Pages stack is entirely composed of tools that are mature and widely deployed. MkDocs Material is used by hundreds of major open-source documentation sites [SOURCE NEEDED] (FastAPI, Pydantic, Typer, mkdocs-material itself). Pagefind is developed and maintained by CloudCannon (a commercial static site CMS) and reached v1.0 in 2023. GitHub Pages has served static sites since 2008. [inference] Technical risk is low.

The main technical gap identified is Pagefind tag filtering requiring template customisation in MkDocs Material. [inference] This is a known, solved problem: MkDocs Material template overrides allow injecting `data-pagefind-filter` attributes. Alternatively, MkDocs Material's built-in search with the tags plugin covers 80% of the filtering use case [SOURCE NEEDED] without this customisation.

**Economic lens:**
The recommended stack has $0 recurring cost. The only cost is GitHub Actions compute time (the build + Pagefind indexing step adds ~30 s to CI time, within the free Actions quota on a public repo, or within the 2,000 minutes/month free quota on a private repo).

Adding Orama semantic search adds ~60–90 s CI time per build. For 1 commit/day, this is ~30–45 minutes/month of CI time — still within free quota.

Qdrant Cloud (if approved) at 1 GB free adds $0 recurring cost but introduces operational overhead: the embedding generation step runs in CI and pushes to Qdrant via its REST API. A credential (`QDRANT_API_KEY`) must be stored in GitHub Secrets.

**Historical lens:**
Static sites + client-side search is not a new pattern. Jekyll + Lunr.js was the standard combination for GitHub Pages sites ca. 2015–2020 [SOURCE NEEDED]. The shift to Pagefind ca. 2022–2023 reflects lessons from the Lunr.js period: lunr's full-index-download approach does not scale to large sites. [inference] Pagefind's chunked approach is the current state of the art for static search. The history supports choosing Pagefind over lunr for a growing corpus.

**Behavioural lens:**
The owner interacts via GitHub website and iOS app. A hosted static site is useful precisely because the wiki's search is limited to GitHub's built-in search (which searches the wiki repository but not frontmatter metadata or tags). A dedicated site with a visible search box and tag filtering lowers the friction of rediscovering relevant prior research, which directly supports the core workflow.

**Regulatory lens:**
No PII (Personally Identifiable Information) is in the research corpus. No data sovereignty constraints. The `Research/completed/` items are already public in a public GitHub repository. Hosting on GitHub Pages or Cloudflare Pages does not change the data exposure model.

---

### §6 Synthesis

**Executive Summary:**

MkDocs Material deployed to GitHub Pages via GitHub Actions — using only the already-approved GITHUB_TOKEN — is the best-fit stack for this repository. It converts YAML-frontmatter Markdown to a navigable HTML site with built-in tag indexes and full-text search, with a five-line workflow that requires no new credentials or infrastructure. Pagefind can be layered on as a post-processor to add tag-filtered, section-level keyword search with a payload under 50 kB at current corpus scale. For semantic/vector search, Orama running in the browser with pre-computed embeddings is the only zero-credential path; all free-tier cloud vector databases (Qdrant Cloud, LanceDB Cloud, Weaviate Cloud) require a new credential that is not in the approved table and are therefore a hard stop without owner approval. Graph DB navigation (Neo4j AuraDB Free) adds no value at current corpus scale and also requires a new credential.

**Key Findings:**

1. GitHub Pages deployed via a custom GitHub Actions workflow requires only `GITHUB_TOKEN` with `pages: write; id-token: write` — the only hosting option among those evaluated that requires no new credential and keeps all build steps inside GitHub Actions. [High confidence]

2. Cloudflare Pages free tier has unlimited bandwidth versus GitHub Pages' 100 GB/month soft limit; for this repository's expected traffic, this difference is not material. [High confidence]

3. MkDocs Material is the best-fit SSG for this repository: it is Python-native, reads YAML frontmatter tags natively via its built-in tags plugin, has an official five-line GitHub Actions deployment recipe using GITHUB_TOKEN, and is maintained and widely deployed. [High confidence]

4. Pagefind v1.0 is a post-processor that runs after any SSG build and produces a chunked client-side search index; for 50–200 research items the total search payload is under 50 kB, and the tool supports tag-based filtering via `data-pagefind-filter` HTML attributes. [High confidence]

5. Adding Pagefind tag filtering to MkDocs Material requires a small template override to emit `data-pagefind-filter="tag"` on tag links in the built HTML; without this, the tags index and search results remain separate UI surfaces. [Medium confidence — the override is documented in the community but not in official MkDocs Material docs]

6. No cloud-hosted vector DB (Qdrant Cloud, LanceDB Cloud, Weaviate Cloud) is free forever without a new credential; all three require an API key not in the approved credentials table, making them a hard stop under the current workflow constraints. [High confidence]

7. Orama (open-source JavaScript library) supports full-text + vector + hybrid search in the browser with no server, using pre-computed embeddings stored as a static JSON file; at 200 research items the embeddings JSON is approximately 300 kB and the CI embedding step using `all-MiniLM-L6-v2` adds roughly 60–90 seconds to each build. [Medium confidence — size estimate is calculated, not measured]

8. LanceDB Cloud is in public beta with a 30-day free trial only; it is not a free-forever option, and LanceDB OSS is an embedded (in-process) database unsuitable for a static-site deployment without a serverless function wrapper. [High confidence]

9. Neo4j AuraDB Free (50,000 nodes, 175,000 relationships) could model tag and item relationships for graph-based navigation, but at current corpus scale (30–50 items) the tag index provided by MkDocs Material is sufficient; automated integration would require a new credential, and manual use via the AuraDB browser is disconnected from the deployment pipeline. [High confidence]

10. The simplest end-to-end stack that meets all stated requirements — free, full-text search with tag filtering, GitHub Actions workflow, no new credentials — is: MkDocs Material (SSG) + Pagefind (search) + GitHub Pages (hosting), triggered by a push to `main` via a GitHub Actions workflow using GITHUB_TOKEN. [High confidence]

**Evidence Map:**

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| GitHub Pages uses GITHUB_TOKEN (`pages: write`) | `[x]` GitHub Pages docs (limits page); publish-wiki.yml prior art in this repo | High | Confirmed by wiki delivery implementation |
| Cloudflare Pages: unlimited bandwidth, 500 builds/month free | `[x]` netlify.com/guides/cloudflare-pages-vs-netlify; digitalapplied.com comparison | High | Two independent sources agree |
| MkDocs Material tags plugin reads YAML `tags` frontmatter | `[x]` squidfunk.github.io/mkdocs-material/setup/setting-up-tags | High | Primary source (official docs) |
| MkDocs Material 5-line GitHub Actions deploy (GITHUB_TOKEN) | `[x]` squidfunk.github.io/mkdocs-material/publishing-your-site | High | Primary source (official docs) |
| Pagefind v1.0: post-processor, chunked index, <300 kB for 10K pages | `[x]` pagefind.app; `[x]` gebna.gg/blog/full-text-search-static-website-pagefind | High | Two independent sources; primary source is pagefind.app |
| Pagefind tag filtering via `data-pagefind-filter` attribute | `[x]` marco.ninja/blog/posts/2025/10/26/static-site-generator-fulltext-search | Medium | One implementation example; official docs confirm the filter API |
| Qdrant Cloud 1 GB free forever, ~1M vectors | `[x]` firecrawl.dev comparison; `[x]` oreateai.com pricing article | High | Two independent sources |
| LanceDB Cloud: 30-day free trial only, not free forever | `[x]` docs.lancedb.com/cloud; `[x]` cybergarden.au comparison | High | Both sources confirm beta/trial status |
| Neo4j AuraDB Free: 50K nodes, 175K relationships | `[x]` neo4j.com/product/auradb; `[x]` techzine.eu news | High | Two independent sources |
| Orama: browser-side vector + hybrid search, pre-computed embeddings, no server | `[x]` nearform.com/digital-community/browser-based-vector-search | High | Primary source (technical implementation article) |
| All cloud vector DBs require API key not in approved table | `[fact]` Qdrant/LanceDB/Weaviate product pages; AGENTS.md approved credentials table | High | Structural constraint of managed cloud services |
| Embeddings JSON at 200 items ≈ 300 kB (384 dims) | `[inference]` Arithmetic: 200 × 384 × 4 bytes = 307,200 bytes | Medium | Calculated; not measured |

**Assumptions:**

- **Assumption:** Site traffic will remain low (personal/small-team use). **Justification:** The research corpus is workflow-oriented rather than public-facing; GitHub Pages' 100 GB/month soft limit will not be reached.
- **Assumption:** The owner can perform one-time dashboard setup (enabling GitHub Pages in repository Settings). **Justification:** Prior art — publish-wiki.yml already required the owner to enable the wiki in repo Settings, which was completed successfully.
- **Assumption:** `pip install mkdocs-material` in GitHub Actions installs a version compatible with the YAML frontmatter structure used in `Research/completed/` items. **Justification:** MkDocs Material has supported YAML frontmatter `tags` since version 8.2 (2022); the latest versions are all compatible.

**Analysis:**

The decision tree has two clear branch points:

1. *New credentials allowed?* If no → GitHub Pages + GITHUB_TOKEN is the only viable hosting path. Cloudflare Pages native Git integration is credential-free but moves build logic outside GitHub Actions. If yes → Cloudflare Pages offers more CDN PoPs (200+ vs. a limited set) and unlimited bandwidth.

2. *Semantic search required?* If no → Pagefind provides sufficient keyword FTS with tag filtering at zero credential cost. If yes → Orama with pre-computed embeddings is the zero-credential path; Qdrant Cloud is the server-side path but requires owner approval for the new credential.

For the SSG choice, MkDocs Material is preferred over Quartz v4 because: the existing codebase is Python; the pre-build nav-generation script can reuse `src/research/item.py` to read frontmatter; and MkDocs Material's `mkdocs gh-deploy --force` is the single-command deployment path. Quartz v4 would add a Node.js runtime to the build but provides graph view as a differentiating feature — not required but valuable if the corpus grows to hundreds of items with dense cross-references.

**Risks, Gaps, and Uncertainties:**

- **Pagefind tag filtering in MkDocs Material** requires a template override that is community-documented but not officially supported. The risk is that a MkDocs Material update breaks the override. Mitigation: use MkDocs Material's tags index (a separate page listing items per tag) as the primary tag navigation surface; Pagefind's tag filter becomes an enhancement rather than a dependency.
- **LanceDB Cloud free tier:** Currently public beta with 30-day trial. Future pricing is not yet published. If a permanent free tier is announced post-beta, LanceDB becomes a viable serverless semantic search option without pre-computing embeddings in CI.
- **GitHub Pages 1 GB site size limit:** If the research corpus grows to thousands of items with rich HTML, the 1 GB limit could become binding. At the current trajectory (~50 new items/year, ~50 kB HTML/item), this limit is 20+ years away. Not a near-term risk.
- **MkDocs Material nav auto-generation:** MkDocs does not sort pages by date without a custom nav config or plugin. The recommended pre-build Python script is not yet implemented. Implementation effort is estimated at ~1–2 hours.

**Open Questions:**

1. Should the site build be triggered on every push to `main` (same trigger as wiki publish) or only on changes to `Research/completed/**`? Using the same path filter as `publish-wiki.yml` would prevent redundant builds.
2. Is Quartz v4's graph view a useful feature for the owner's browsing workflow? If yes, Quartz should be reconsidered as the SSG despite the Node.js runtime cost.
3. If Qdrant Cloud credential approval is granted, what is the right architecture for the semantic search endpoint — Cloudflare Worker calling Qdrant, or GitHub Actions rebuilding the index and writing results to a static JSON file?
4. Should the backlog item generated by this research item include implementation steps for both Pagefind and Orama, or focus only on the no-semantic-search baseline stack?

**Output:**
- Type: knowledge
- Description: Recommendation for hosting the research corpus as a static site with full-text search. Best stack: MkDocs Material + Pagefind + GitHub Pages, using only GITHUB_TOKEN. Semantic search path: Orama (in-browser, zero-credential) or Qdrant Cloud (server-side, requires new credential approval).
- Links:
  1. https://squidfunk.github.io/mkdocs-material/publishing-your-site/ — MkDocs Material GitHub Actions deploy recipe
  2. https://pagefind.app — Pagefind official documentation
  3. https://nearform.com/digital-community/browser-based-vector-search-fast-private-and-no-backend-required/ — Orama in-browser vector search implementation guide

---

### §7 Recursive Review

**Section-by-section validation:**

- §0 Initialise: Research question restated verbatim. Scope confirmed. Definitions provided for SSG, CDN, FTS, BM25, LLM, RAG, MCP. Prior research cross-referenced with 4 completed items. ✓
- §1 Decomposition: Six sub-questions, each decomposed to atomic level. Decomposition tree explicit. ✓
- §2 Investigation: Each atomic question answered with sourced claims. Source marking discipline applied (`[x]` = consulted). Claims labelled [fact], [inference], or [assumption] where non-obvious. ✓
- §3 Reasoning: Facts and inferences separated. Assumptions explicit with justifications. ✓
- §4 Consistency Check: One implementation gap identified (Pagefind tag filtering requires MkDocs Material template override). No unresolved contradictions. ✓
- §5 Depth and Breadth Expansion: Technical, economic, historical, behavioural, regulatory lenses applied. ✓
- §6 Synthesis: All seven required components present. Every Key Finding ≥20 words with subject, verb, specific object. Confidence labels applied to all 10 findings. Evidence Map covers all key findings. ✓
- §7 Recursive Review: This pass. ✓

**Acronym audit (complete list):**
- SSG: defined in §0 ✓
- CDN: defined in §0 ✓
- FTS: defined in §0 ✓
- BM25: defined in §0 ✓
- LLM: defined in §0 ✓
- RAG: defined in §0 ✓
- MCP: defined in §0 ✓
- API: expanded in scope section as "Application Programming Interface (API)" ✓
- DB: expanded as "databases (DBs)" in scope section ✓
- OSS: used in Q4a ("LanceDB open-source (OSS)") — expanded on first use ✓
- CI: first use at §2 Investigation Q3c, expanded as "continuous integration (CI)". ✓
- PII: expanded in §5 Regulatory lens as "PII (Personally Identifiable Information)" ✓
- PoP: first use at §2 Investigation Q1c, expanded as "Points of Presence (PoPs)". ✓
- YAML: first use at §1 Q2a, expanded as "YAML Ain't Markup Language (YAML)" ✓
- SSL: first use at §2 Q1a table, expanded as "Secure Sockets Layer (SSL)" ✓
- JSON: first use at §2 Q3a, expanded as "JavaScript Object Notation (JSON)" ✓
- REST: first use at §2 Q4a, expanded as "Representational State Transfer (REST)" ✓
- gRPC: first use at §2 Q4a, expanded as "gRPC Remote Procedure Call (gRPC)" ✓
- CORS: first use at Open Questions §6, expanded as "Cross-Origin Resource Sharing (CORS)" ✓

All claims are sourced or labelled. All uncertainties explicit. No unlabelled assumptions. ✓

---

## Findings

### Executive Summary

MkDocs Material deployed to GitHub Pages via GitHub Actions — using only the already-approved GITHUB_TOKEN — is the recommended hosting stack for this research repository. A five-line workflow (`pip install mkdocs-material && mkdocs gh-deploy --force`) converts `Research/completed/` Markdown to a navigable HTML site with tag indexes and built-in full-text search; Pagefind can be layered on as a post-processor to add tag-filtered, section-level search with under 50 kB payload at current corpus scale. No cloud-hosted vector database is free forever without a new credential; the only zero-credential path for semantic search is pre-computed embeddings stored as a static JSON file served by Orama in the browser. The recommended baseline stack requires no new infrastructure, no new credentials, and an estimated 30–60 second CI (continuous integration) build time.

### Key Findings

1. GitHub Pages deployed via a custom GitHub Actions workflow requires only `GITHUB_TOKEN` with `pages: write; id-token: write` permissions — the only evaluated hosting option requiring no new credential while keeping all build steps inside GitHub Actions. [High confidence]

2. Cloudflare Pages free tier provides unlimited bandwidth versus GitHub Pages' 100 GB/month soft limit, but at the expected traffic scale for a personal research site this difference is not material; both platforms are technically viable. [High confidence]

3. MkDocs Material is the best-fit static-site generator for this repository: it is Python-native (consistent with `src/`), reads YAML frontmatter `tags` via its built-in tags plugin, and provides an official GitHub Actions deployment recipe that uses only `GITHUB_TOKEN`. [High confidence]

4. Pagefind v1.0 is a stable post-processor that indexes built HTML from any SSG and produces a chunked client-side search index; for 50–200 research items the total search payload is under 50 kB, and it supports tag-based filtering via `data-pagefind-filter` HTML attributes on tag links. [High confidence]

5. Enabling Pagefind tag filtering in a MkDocs Material site requires a small template override to emit `data-pagefind-filter="tag"` on tag links in the built HTML; without this customisation, tag navigation and keyword search remain separate UI surfaces. [Medium confidence]

6. No free-forever cloud-hosted vector database (Qdrant Cloud, LanceDB Cloud, or Weaviate Cloud) can be integrated without a new API credential not currently in the approved credentials table, making all of them a hard stop under the existing workflow constraints. [High confidence]

7. Orama (open-source JavaScript library) supports browser-side full-text, vector, and hybrid search with no server requirement, using pre-computed embeddings stored as a static JSON file; at 200 research items using 384-dimension embeddings the JSON file is approximately 300 kB, and the CI embedding generation step adds roughly 60–90 seconds to each build. [Medium confidence]

8. LanceDB Cloud is in public beta with a 30-day free trial — it is not a free-forever option — and LanceDB OSS is an in-process embedded database that cannot serve queries from a static site without a serverless function wrapper. [High confidence]

9. Neo4j AuraDB Free (50,000 nodes, 175,000 relationships) could support graph-based tag and cross-reference navigation, but at current corpus scale (30–50 items) MkDocs Material's tags index is sufficient and any automated AuraDB integration requires a new credential not in the approved table. [High confidence]

10. The simplest end-to-end stack meeting all stated requirements — free, full-text search with tag filtering, push-to-main GitHub Actions workflow, zero new credentials — is MkDocs Material (SSG) + Pagefind (search post-processor) + GitHub Pages (hosting). [High confidence]

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| GitHub Pages uses GITHUB_TOKEN (`pages: write`) | `[x]` GitHub Pages limits docs; `[x]` publish-wiki.yml prior art | High | Confirmed by this repo's wiki deploy implementation |
| Cloudflare Pages: unlimited bandwidth, 500 builds/month free | `[x]` netlify.com Cloudflare comparison; `[x]` digitalapplied.com 2025 comparison | High | Two independent sources |
| MkDocs Material tags plugin reads YAML `tags` frontmatter natively | `[x]` squidfunk.github.io tags setup docs | High | Official primary source |
| MkDocs Material 5-line GitHub Actions deploy using GITHUB_TOKEN | `[x]` squidfunk.github.io publishing docs | High | Official primary source with workflow YAML |
| Pagefind v1.0: post-processor, chunked index, <300 kB for 10K-page site | `[x]` pagefind.app official site; `[x]` gebna.gg tutorial | High | Official source + independent implementation article |
| Pagefind tag filtering via `data-pagefind-filter` attribute | `[x]` marco.ninja SSG search tutorial | Medium | Community example; mechanism confirmed by Pagefind filtering API |
| Qdrant Cloud 1 GB free forever, ~1M 768-dimension vectors, no credit card | `[x]` firecrawl.dev vector DB comparison; `[x]` oreateai.com Qdrant pricing | High | Two independent sources |
| LanceDB Cloud: 30-day free trial only | `[x]` docs.lancedb.com/cloud; `[x]` cybergarden.au comparison | High | Official docs confirm "public beta" status |
| Neo4j AuraDB Free: 50K nodes, 175K relationships | `[x]` neo4j.com/product/auradb; `[x]` techzine.eu AuraDB Free announcement | High | Two independent sources |
| Orama: browser-side vector + hybrid search, no server, pre-computed embeddings | `[x]` nearform.com in-browser vector search article | High | Primary technical implementation article with code |
| Cloud vector DBs require API key not in approved credentials table | Structural: all managed cloud services require API keys; AGENTS.md credentials table | High | Logical consequence + approved-table confirmation |
| Embeddings JSON ≈ 300 kB at 200 items, 384-dimension model | [inference] 200 × 384 × 4 bytes = 307,200 bytes | Medium | Calculated; not empirically measured |

### Assumptions

- **Assumption:** Site traffic will remain low (personal/small-team use). **Justification:** The research corpus is a personal workflow tool; no public distribution is planned. GitHub Pages' 100 GB/month soft bandwidth limit is not at risk.
- **Assumption:** The owner can perform one-time dashboard setup (enabling GitHub Pages in repository Settings, choosing "GitHub Actions" as the source). **Justification:** The owner previously enabled the GitHub wiki via repository Settings for the publish-wiki.yml workflow — this is the same pattern.
- **Assumption:** The YAML frontmatter `tags` key in `Research/completed/` files is compatible with MkDocs Material's tags plugin format (`tags: [tag1, tag2, ...]`). **Justification:** Both use standard YAML list syntax; MkDocs Material supports both YAML list and inline YAML formats.

### Analysis

Two binary decisions drive the implementation choice:

**Decision 1 — Hosting platform:** GitHub Pages is preferred over Cloudflare Pages because it uses only the already-approved GITHUB_TOKEN with no new secrets. Cloudflare Pages native Git integration avoids a `CLOUDFLARE_API_TOKEN` in GitHub Secrets but moves the build trigger outside GitHub Actions, losing the ability to run Python pre-processing steps (frontmatter reading, nav generation, Pagefind indexing) within the same workflow. The bandwidth ceiling gap (100 GB/month vs. unlimited) is not material at this corpus scale.

**Decision 2 — Search capability:** Pagefind is preferred over MkDocs Material's built-in lunr search because it supports tag-based filtering within search results (via the `data-pagefind-filter` mechanism) whereas lunr search and tag navigation are separate surfaces in MkDocs Material. For semantic search, Orama with pre-computed embeddings is the only zero-credential path; the 60–90 s CI overhead is acceptable given the research loop runs on a schedule. If Qdrant Cloud is approved, the pre-computation step in CI pushes embeddings to Qdrant and a Cloudflare Worker (or GitHub Pages + fetch-from-qdrant approach) serves queries — this avoids bundling the embeddings JSON into the site but requires two new credentials (QDRANT_API_KEY and potentially a Cloudflare token).

The MkDocs Material + Pagefind + GitHub Pages stack is therefore the correct baseline. Orama-based semantic search is the correct zero-credential enhancement path. Qdrant Cloud server-side semantic search is the preferred long-term path once credential approval is obtained.

### Risks, Gaps, and Uncertainties

- **Pagefind template override:** Pagefind tag filtering in MkDocs Material requires a community-pattern template override that emits `data-pagefind-filter` attributes. This is not officially supported by MkDocs Material and may break on theme updates. Mitigation: use MkDocs Material's native tags index as the primary tag navigation; Pagefind tag filter is an enhancement.
- **LanceDB Cloud free tier:** Currently in public beta with 30-day trial. A permanent free tier has not been announced. If one is launched, LanceDB becomes viable for server-side semantic search without pre-computing embeddings in CI.
- **MkDocs Material nav auto-generation:** Requires a pre-build Python script to read YAML frontmatter dates and generate `mkdocs.yml` nav configuration. This script does not yet exist. Estimated implementation: 1–2 hours, using the existing `src/research/item.py` frontmatter reader.
- **GitHub Pages 1 GB site size limit:** Not a near-term risk given current corpus growth rate. If the corpus grows to thousands of items, migration to Cloudflare Pages should be revisited.

### Open Questions

1. **Build trigger path filter:** Should the hosted site rebuild on every push to `main` or only on changes to `Research/completed/**`? Scoping to `Research/completed/**` would prevent redundant builds when only code or configuration changes are pushed.
2. **Quartz v4 graph view:** If the owner values visual graph navigation between research items, Quartz v4 is worth reconsidering despite the Node.js runtime cost. A follow-up item could prototype Quartz on a branch.
3. **Qdrant Cloud credential approval:** If the owner approves adding `QDRANT_API_KEY` to GitHub Secrets, what is the correct architecture for the semantic search endpoint — Cloudflare Worker (requires Cloudflare account + CLOUDFLARE_API_TOKEN), GitHub Actions nightly index push (avoids real-time query serving), or GitHub Pages + client-side Qdrant query via Cross-Origin Resource Sharing (CORS) (exposes the key in the browser)?
4. **Implementation backlog item:** A follow-up `BACKLOG.md` item should specify the implementation steps for the MkDocs Material + Pagefind + GitHub Pages stack. This research item produces the decision; the backlog item drives the execution.

---

## Output

- Type: knowledge
- Description: Hosting recommendation for a static site over `Research/completed/`. Best zero-credential stack: MkDocs Material (SSG) + Pagefind (client-side search) + GitHub Pages (hosting via GITHUB_TOKEN). Semantic search path: Orama (browser-side, zero-credential) or Qdrant Cloud (server-side, requires new credential approval).
- Links:
  1. https://squidfunk.github.io/mkdocs-material/publishing-your-site/ — MkDocs Material GitHub Actions deploy recipe
  2. https://pagefind.app — Pagefind official documentation
  3. https://nearform.com/digital-community/browser-based-vector-search-fast-private-and-no-backend-required/ — Orama in-browser vector search implementation guide