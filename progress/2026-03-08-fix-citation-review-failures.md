# 2026-03-08 — Fix citation review failures (issues #63–#66)

## What was done

Fixed four completed research documents that failed automated quality reviews. Each document had violations across `citation-discipline`, `speculation-control`, and/or `remove-ai-slop`.

## Files changed

### `Research/completed/2026-03-08-ios-shortcuts-github-api-memory-capture.md` (Issue #66)
- citation-discipline: expanded PAT → "Personal Access Token (PAT)" at first use (Research Question); expanded MIME → "Multipurpose Internet Mail Extensions (MIME)" at first use (§2 A3); expanded LTE → "Long-Term Evolution (LTE)" at first use (§2 F1); changed "most common failure mode" → "a likely failure mode" (Key Finding 2); replaced GitHub Enterprise Server 3.16 secondary rate limit URL with the equivalent github.com URL
- speculation-control: added `[inference]` to adequacy claim (§3 On PAT security); added `[inference]` to "Memory capture is habit-sensitive" and "The fewer taps…" (§5 Behavioural lens); added `[inference]` to "best available option" (Findings Analysis)

### `Research/completed/2026-03-08-inbox-folder-capture-triage-pattern.md` (Issue #65)
- citation-discipline: expanded PKM → "Personal Knowledge Management (PKM)" at first use (Context); expanded HCI → "Human-Computer Interaction (HCI)" at first use (Findings Key Finding 3); expanded ULID → "Universally Unique Lexicographically Sortable Identifier (ULID)" at first use (§3 Reasoning); changed `[fact]` → `[inference]` on YAML front-matter claim sourced from "inferred from backlog item context" (§2 Q2b); removed unverifiable AAAI ICWSM prompt study citation from both Evidence Map tables, noting claim is `[inference]`
- speculation-control: added `Opinion:` to "The inbox pattern is the right design for this context" (§6 Analysis); added `Opinion:` to "The inbox pattern is the correct design" (Findings Analysis); added `[inference]` to "The research-loop.yml has been operating reliably" (§3 Claim 4)
- remove-ai-slop: removed "directly supporting the friction-reduction claim" over-explained causal link (Findings Key Finding 3); rewrote "Three independent literatures — HCI, GTD, and PKM — converge on the same principle" to state what each literature says without enumeration-and-convergence framing (Findings Analysis); rewrote Higher/Lower/midpoint symmetrical paragraph about accuracy trade-offs (Findings Analysis)

### `Research/completed/2026-03-08-claude-ios-mcp-remote-integration.md` (Issue #64)
- citation-discipline: expanded MCP → "Model Context Protocol (MCP)" at first use in Research Skill Output (§0); expanded SSE → "Server-Sent Events (SSE)" at first use (§1 Q2c); expanded RFC → "Request for Comments (RFC)" at first use (§1 Q7b); expanded ASGI → "Asynchronous Server Gateway Interface (ASGI)" and WSGI → "Web Server Gateway Interface (WSGI)" at first use (§5 Technical lens); expanded PAT → "Personal Access Token (PAT)" at first use in §5 (Comparison); added Cloudflare Workers pricing URL for tier limit figures (§5 Economic lens); added direct Connectors Directory link to Q7 fact (§2 Q7)
- speculation-control: added `[inference]` to Cloudflare Workers sufficiency claim (§5 Economic lens); added `Opinion:` to "OAuth 2.1 is the right long-term choice" (§6 Analysis); added `Opinion:` to "no-auth with IP allowlisting…is the most pragmatic option" (Findings Analysis); added `[inference]` to "The remote MCP connector path is superior to all other iOS memory access options" (Findings Analysis)

### `Research/completed/2026-03-08-servicenow-csdm-data-modelling.md` (Issue #63)
- citation-discipline: expanded ITSM → "IT Service Management (ITSM)", IRM → "Integrated Risk Management (IRM)", GRC → "Governance, Risk and Compliance (GRC)" at first use (Research Question); expanded CI → "Configuration Item (CI)" and CMDB → "Configuration Management Database (CMDB)" at first use (§2 B2 Technical Service fact); expanded TBM → "Technology Business Management (TBM)" at first use (§2 D1); expanded ITOM → "IT Operations Management (ITOM)" at first use (§2 F1 Novavax case); expanded DORA → "Digital Operational Resilience Act (DORA)" at first use in §2 (IRM/GRC section, not deferred to §5); expanded RBNZ → "Reserve Bank of New Zealand (RBNZ)" at first use (§6 Risks); replaced "web search synthesis" citation in CSDM 4.0 domains fact with specific sourced URLs; marked Jade Global, Beyond20, Sofigate, Plat4mation, Infocenter sources as `[inference]` with note that URLs were not verified at time of research; added `[fact]`/`[inference]` labels to all unlabelled analytical claims in §5
- speculation-control: added `[inference]` to the root-cause claim (§3); added `[inference]` to the CSDM 5 trading infrastructure implication (§5 Technical lens); added `[inference]` to "typically triggers expensive data remediation projects" (Findings Analysis)
- remove-ai-slop: rewrote three Findings Analysis paragraphs that all opened with "The [noun phrase] [verb]" to vary structure; compressed the near-verbatim repetition of the governance-responsibility insight between §3 and Findings Analysis

## No ADR required
All corrections are clarifications (label additions, acronym expansions, citation source changes). No information was permanently removed — unverifiable claims were relabelled `[inference]` rather than deleted.
