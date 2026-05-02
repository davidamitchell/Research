---
title: "What are the established norms from academic pre-print repositories and Personal Knowledge Management (PKM) systems for versioning, correcting, and amending published research items, and does a frontmatter `versions:` array with git history as the diff meet those standards?"
added: 2026-05-02T06:11:10+00:00
status: backlog  # backlog | in-progress | reviewing | completed
priority: high  # low | medium | high
blocks: []  # slugs (filename without .md) of backlog items that cannot start until this one is complete
tags: [research-tooling, workflow, knowledge-graph, organisational-learning]
started: ~
completed: ~
output: []  # skill | tool | agent | knowledge | backlog-item
cites: []
related: []
superseded_by: ~
supersedes: ~
item_type: primary
confidence: medium
versions: []
---

# What are the established norms from academic pre-print repositories and Personal Knowledge Management (PKM) systems for versioning, correcting, and amending published research items, and does a frontmatter `versions:` array with git history as the diff meet those standards?

## Research Question

What are the established norms and practical conventions from academic pre-print repositories (arXiv, Social Science Research Network (SSRN), Open Science Framework (OSF)) and Personal Knowledge Management (PKM) implementations (Zettelkasten, Obsidian, Roam Research, Logseq) for how published research items should be corrected, versioned, retracted, or extended after initial publication — specifically: what auditability standards must a versioning model meet, how is the distinction between minor correction and substantive revision defined, and does a pragmatic model using a YAML frontmatter `versions:` array (version number, commit SHA (Secure Hash Algorithm), date, progress log path, one-line summary) combined with git commit history as the diff provide sufficient auditability, or is a stricter arXiv-style immutable-file-per-version approach warranted?

## Scope

**In scope:**
- arXiv versioning model: how v1, v2, vN are numbered, what triggers a new version, whether the original is preserved, and how the version history is displayed
- SSRN and OSF versioning: how corrections and revisions are handled; whether original versions are preserved
- Registered reports model: how pre-registration and staged disclosure affect amendment norms
- PKM versioning: how Zettelkasten handles "developed notes" (updated permanent notes), how Obsidian and Logseq handle version history (git integration, plugin-based history)
- Minimum auditability standard: what an independent reader needs to reconstruct what changed, when, and why — and whether the proposed model meets that standard
- Correction vs revision distinction: what thresholds distinguish minor corrections (typos, acronym expansions, broken URLs) from substantive revisions (changed findings, revised conclusions)
- `replicates:` and `corrects:` relationship types: whether these warrant addition to the `## Related Items` edge vocabulary alongside the existing five types (`extends`, `contradicts`, `depends-on`, `spawned-from`, `see-also`)
- Risk assessment: what could go wrong with the pragmatic model (commit history rewrite, SHA collision, orphaned progress logs)

**Out of scope:**
- Retraction and misconduct processes (not applicable to a single-author personal research repository)
- Database-backed version control systems
- Code versioning semantics (SemVer) — research item versioning has different semantics

**Constraints:**
- Expand all acronyms on first use
- The evaluation must compare the proposed pragmatic model against at least two alternative approaches (arXiv-style vN files, separate amendments file)
- Findings must produce a concrete recommendation: adopt the pragmatic model, adopt a stricter model, or adopt a hybrid — with justification

## Context

W-0048 in `BACKLOG.md` defines this research item: validate the pragmatic frontmatter versioning model against academic pre-print and PKM norms before the schema is locked in. Completed items in this repo are currently edited post-completion with no formal record of what changed, when, or why. W-0049 implements the `versions:` field and already ran under "Option B" (implement now, validate later). This research item provides the validation: if findings contradict the current design, an Architecture Decision Record (ADR) supersedes the W-0049 design and the schema is updated. The research item also evaluates whether `replicates:` and `corrects:` relationship types should join the `## Related Items` vocabulary.

## Approach

1. **arXiv versioning model analysis**: Review arXiv's versioning policy and implementation — how versions are numbered, what triggers a new version submission, whether original versions are permanently preserved, and how corrections-only submissions differ from revision submissions.
2. **SSRN and OSF amendment norms**: Review SSRN's revision and retraction policies; review OSF's pre-registration amendment process and how corrections to registered reports are handled.
3. **PKM versioning review**: Study how Zettelkasten handles note evolution (Luhmann's folgezettel), how Obsidian's git plugin handles version history, how Logseq handles journal-style note evolution, and what minimum record each requires.
4. **Auditability standard definition**: From the academic pre-print models, define the minimum information an independent reader needs to reconstruct "what changed, when, and why" — and test whether the YAML `versions:` array plus git commit history meets that standard.
5. **Alternative model comparison**: Compare the proposed pragmatic model against: (a) arXiv-style immutable vN files (separate file per version), (b) an amendments appendix section in the item file, and (c) a separate `amendments/` directory with diff files. Assess each for auditability, maintenance burden, and LLM agent compatibility.
6. **Relationship vocabulary evaluation**: Assess whether `replicates:` and `corrects:` relationship types are warranted given the PKM and academic pre-print edge vocabularies; propose addition or rejection with supporting evidence.
7. **Recommendation**: Produce a concrete recommendation for the frontmatter versioning model, correction/revision threshold definitions, and relationship vocabulary changes; note whether an ADR update is required.

## Sources

- [ ] [arXiv help — Versions](https://info.arxiv.org/help/versions.html) — arXiv versioning policy: how versions are numbered, preserved, and linked
- [ ] [SSRN — Paper Revision Policy](https://www.ssrn.com/index.cfm/en/ssrn-faq/#papercitation) — SSRN revision and retraction norms for pre-print papers
- [ ] [Open Science Framework (OSF) — Registrations](https://help.osf.io/article/330-welcome-to-registrations) — OSF pre-registration and amendment process; how corrections to registered research are handled
- [ ] [Ahrens (2017) How to Take Smart Notes: One Simple Technique to Boost Writing, Learning and Thinking](https://www.soenkeahrens.de/en/takesmartnotes) — Zettelkasten permanent note development and evolution norms
- [ ] [Obsidian git plugin documentation](https://publish.obsidian.md/git-doc/Start+here) — version history and amendment tracking in Obsidian using git
- [ ] [Srivastava et al. (2023) Beyond the Imitation Game: Quantifying and Extrapolating the Capabilities of Language Models (BIG-Bench)](https://arxiv.org/abs/2206.04615) — example of large-scale research artifact versioning across multiple author revisions

---

## Research Skill Output

*(Full output from running the research skill — retained verbatim in the completed item. §§0–5 are the investigation; §6 seeds the Findings section below.)*

### §0 Initialise

-

### §1 Question Decomposition

-

### §2 Investigation

-

### §3 Reasoning

-

### §4 Consistency Check

-

### §5 Depth and Breadth Expansion

-

### §6 Synthesis

**Executive summary:**

**Key findings:**

**Evidence map:**

**Assumptions:**

**Analysis:**

**Risks, gaps, uncertainties:**

**Open questions:**

### §7 Recursive Review

-

---

## Findings

*(Populated from §6 Synthesis above.)*

### Executive Summary

### Key Findings

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| | | high / medium / low | |

### Assumptions

### Analysis

### Risks, Gaps, and Uncertainties

-

### Open Questions

-

---

## Output

*(Fill in when completing — what was produced as a result of this research?)*

- Type: # skill | tool | agent | knowledge | backlog-item
- Description:
- Links:
