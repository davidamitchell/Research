---
review_count: 2
title: "What are the established norms from academic pre-print repositories and Personal Knowledge Management (PKM) systems for versioning, correcting, and amending published research items, and does a YAML Ain't Markup Language (YAML) frontmatter `versions:` array with git history as the diff meet those standards?"
added: 2026-05-02T06:11:10+00:00
status: reviewing
priority: high  # low | medium | high
blocks: []  # slugs (filename without .md) of backlog items that cannot start until this one is complete
tags: [research-tooling, workflow, knowledge-graph, organisational-learning]
started: 2026-05-02T10:41:11+00:00
completed: ~
output: [knowledge]  # skill | tool | agent | knowledge | backlog-item
cites: [2026-04-27-academic-post-publication-amendment-practices, 2026-03-03-knowledge-linking-connected-corpus]
related: [2026-05-01-coding-agent-context-management-transparency]
superseded_by: ~
supersedes: 2026-04-27-academic-post-publication-amendment-practices
item_type: primary
confidence: medium
versions: []
---

# What are the established norms from academic pre-print repositories and Personal Knowledge Management (PKM) systems for versioning, correcting, and amending published research items, and does a YAML Ain't Markup Language (YAML) frontmatter `versions:` array with git history as the diff meet those standards?

## Research Question

What are the established norms and practical conventions from academic pre-print repositories (arXiv, Social Science Research Network (SSRN), Open Science Framework (OSF)) and Personal Knowledge Management (PKM) implementations (Zettelkasten, Obsidian, Roam Research, Logseq) for how published research items should be corrected, versioned, retracted, or extended after initial publication, specifically: what auditability standards must a versioning model meet, how is the distinction between minor correction and substantive revision defined, and does a pragmatic model using a YAML Ain't Markup Language (YAML) frontmatter `versions:` array (version number, commit SHA (Secure Hash Algorithm), date, progress log path, one-line summary) combined with git commit history as the diff provide sufficient auditability, or is a stricter arXiv-style immutable-file-per-version approach warranted?

## Scope

**In scope:**
- arXiv versioning model: how v1, v2, vN are numbered, what triggers a new version, whether the original is preserved, and how the version history is displayed
- SSRN and OSF versioning: how corrections and revisions are handled; whether original versions are preserved
- Registered reports model: how pre-registration and staged disclosure affect amendment norms
- PKM versioning: how Zettelkasten handles developed notes, how Obsidian and Logseq handle version history, and what minimum record each requires
- Minimum auditability standard: what an independent reader needs to reconstruct what changed, when, and why, and whether the proposed model meets that standard
- Correction vs revision distinction: what thresholds distinguish minor corrections (typos, acronym expansions, broken URLs) from substantive revisions (changed findings, revised conclusions)
- `replicates:` and `corrects:` relationship types: whether these warrant addition to the `## Related Items` edge vocabulary alongside the existing five types (`extends`, `contradicts`, `depends-on`, `spawned-from`, `see-also`)
- Risk assessment: what could go wrong with the pragmatic model (commit history rewrite, SHA collision, orphaned progress logs)

**Out of scope:**
- Retraction and misconduct processes beyond their relevance to record-preservation norms
- Database-backed version control systems
- Semantic Versioning (SemVer) style software-release semantics

**Constraints:**
- Expand all acronyms on first use
- Compare the pragmatic model against at least two alternatives
- Produce a concrete recommendation for the repository

## Context

- [fact; source: https://github.com/davidamitchell/Research/blob/main/BACKLOG.md; https://github.com/davidamitchell/Research/blob/main/docs-adr/0013-research-item-frontmatter-schema-extension.md] W-0048 exists to validate the pragmatic `versions:` design that Architecture Decision Record (ADR) 0013 implemented before external validation, so this item is the deferred evidence check on an already-shipped schema choice.
- [fact; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-27-academic-post-publication-amendment-practices.md; https://github.com/davidamitchell/Research/blob/main/docs-adr/0013-research-item-frontmatter-schema-extension.md] An adjacent completed item established that mature publishing systems preserve old records and surface explicit amendment notices, while ADR 0013 chose a lighter `versions:` plus git-history model, so the live question here is whether that lighter model now provides equivalent minimum reader-facing auditability.

## Approach

1. **arXiv versioning model analysis:** Review arXiv's versioning policy and implementation, including what counts as a new version and how prior versions remain visible.
2. **SSRN and OSF amendment norms:** Review SSRN and OSF revision handling, preserving any evidence gap explicitly where official text is inaccessible.
3. **PKM versioning review:** Study Zettelkasten note evolution, Obsidian git-backed history, and any retrievable Logseq version-control guidance.
4. **Auditability standard definition:** Derive the minimum information required to reconstruct what changed, when, and why.
5. **Alternative model comparison:** Compare the proposed pragmatic model against immutable vN files, an in-file amendments appendix, and a separate amendments file.
6. **Relationship vocabulary evaluation:** Decide whether `corrects:` or `replicates:` add real value beyond the existing edge vocabulary.
7. **Recommendation:** Produce a concrete recommendation for the repository and note whether ADR-0013 needs updating.

## Sources

- [x] [arXiv Submission Version Availability](https://info.arxiv.org/help/versions.html) - official arXiv versioning policy
- [ ] [SSRN FAQ - Paper Citation](https://www.ssrn.com/index.cfm/en/ssrn-faq/#papercitation) - seeded SSRN policy page; inaccessible in this session
- [ ] [SSRN Support - Submit a Revised Paper](https://support.ssrn.com/knowledgebase/articles/271237-how-do-i-submit-a-revised-paper) - seeded SSRN support page; inaccessible in this session
- [x] [Open Science Framework (OSF) Welcome to Registrations and Preregistrations](https://help.osf.io/article/330-welcome-to-registrations) - official registration and update workflow
- [x] [Open Science Framework (OSF) Advanced Actions on Registrations](https://help.osf.io/article/113-advanced-actions-registrations) - official update and withdrawal workflow
- [x] [Center for Open Science Registered Reports](https://www.cos.io/initiatives/registered-reports) - registered-reports continuity and sequential registration guidance
- [x] [Ahrens (2017) How to Take Smart Notes](https://www.soenkeahrens.de/en/takesmartnotes) - tool-agnostic Zettelkasten guidance
- [x] [Obsidian Git Plugin README](https://github.com/denolehov/obsidian-git/blob/master/README.md) - official plugin features for commit history, diff, and restore
- [ ] [Logseq Version Control](https://docs.logseq.com/#/page/version%20control) - seeded Logseq page; not directly retrievable as usable text here
- [x] [Git user manual - object names and commits](https://git-scm.com/docs/user-manual#object-name) - official commit identity and content-addressing guidance
- [x] [Git - Rewriting History](https://git-scm.com/book/en/v2/Git-Tools-Rewriting-History) - official history-rewrite guidance
- [x] [Git hash-function transition](https://git-scm.com/docs/hash-function-transition) - official SHA-1 and SHA-256 object-name guidance
- [x] [Srivastava et al. (2023) Beyond the Imitation Game](https://arxiv.org/abs/2206.04615) - concrete multi-version arXiv example
- [x] [Research Repo (2026) Academic post-publication amendment practices](https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-27-academic-post-publication-amendment-practices.md) - prior completed item on the broader amendment-control problem
- [x] [Research Repo (2026) Knowledge linking: building a connected research corpus](https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-03-knowledge-linking-connected-corpus.md) - prior completed item on relationship vocabulary
- [x] [Research Repo (2026) Architecture Decision Record 0013 Research Item Frontmatter Schema Extension](https://github.com/davidamitchell/Research/blob/main/docs-adr/0013-research-item-frontmatter-schema-extension.md) - current repository design under review

---

## Research Skill Output

*(Full output from running the research skill - retained verbatim in the completed item. Sections 0 to 5 are the investigation, and section 6 seeds the Findings section below.)*

### §0 Initialise

- [fact; source: https://info.arxiv.org/help/versions.html; https://help.osf.io/article/330-welcome-to-registrations] Question: determine whether this repository's `versions:` plus git-history model satisfies the minimum auditability norm that pre-print and registry systems use for post-publication change.
- [fact; source: https://github.com/davidamitchell/Research/blob/main/BACKLOG.md; https://github.com/davidamitchell/Research/blob/main/docs-adr/0013-research-item-frontmatter-schema-extension.md] Scope: compare the current repository model with arXiv-style visible version chains, OSF-style read-only registration plus explicit update flow, and PKM tools that rely on git-backed history rather than immutable duplicate files.
- [fact; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-27-academic-post-publication-amendment-practices.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-03-knowledge-linking-connected-corpus.md] Prior work: the adjacent amendment-practices item provides the broader publishing baseline, and the knowledge-linking item provides the current relationship-edge vocabulary that this item may refine.
- [fact; source: https://github.com/davidamitchell/Research/blob/main/docs-adr/0013-research-item-frontmatter-schema-extension.md] Output: produce a repository-level recommendation on whether to keep the pragmatic model, replace it with immutable per-version files, or adopt a hybrid with stricter controls.

### §1 Question Decomposition

- **Root question:** does a `versions:` notice index plus git commit history satisfy the same minimum reader needs that academic versioned-record systems satisfy?
- **A. Pre-print and registry norms**
  - A1. What does arXiv require for revisions, corrections, withdrawals, and visible version history?
  - A2. What does OSF require for frozen registrations and later updates?
  - A3. What do registered reports imply about staged amendments and continuity?
  - A4. What evidence remains missing for SSRN?
- **B. PKM norms**
  - B1. Does Zettelkasten itself require immutable duplicate files for note evolution?
  - B2. What audit surfaces do Obsidian git workflows expose?
  - B3. What, if anything, can be concluded about Logseq from retrievable official evidence?
- **C. Git as audit substrate**
  - C1. What does git guarantee about commit identity and content immutability?
  - C2. What are git's actual audit risks?
- **D. Model comparison**
  - D1. What minimum fields must a reader have to reconstruct what changed, when, and why?
  - D2. How do the four candidate models score against that minimum?
- **E. Relationship vocabulary**
  - E1. Does `corrects:` express a distinct governance relation?
  - E2. Does `replicates:` express a relation this corpus materially needs now?

### §2 Investigation

#### A. Pre-print and registry norms

- [fact; source: https://info.arxiv.org/help/versions.html] arXiv states that once a work is public each version becomes a permanent part of the scientific record and may not be removed, and any replacement or withdrawal creates a new version under the same stable identifier.
- [fact; source: https://info.arxiv.org/help/versions.html] arXiv displays all available versions in the submission-history section, allows authors to cite a specific version, and treats appended errata, expanded versions, annual updates, and living reviews as later versions of the same work rather than as unrelated new files.
- [fact; source: https://arxiv.org/abs/2206.04615] The BIG-Bench example shows that arXiv's policy is not merely theoretical, because one public abstract page exposes v1, v2, and v3 under one identifier with dates and downloadable prior versions.
- [fact; source: https://help.osf.io/article/330-welcome-to-registrations] OSF registrations are time-stamped, read-only records, and once a registration is submitted the registration and associated files cannot be edited in place.
- [fact; source: https://help.osf.io/article/113-advanced-actions-registrations] OSF handles later change through an explicit update flow that requires justification, routes through approval, and preserves the original registration instead of silently mutating it.
- [fact; source: https://help.osf.io/article/113-advanced-actions-registrations] OSF frames updates as a way to transparently reflect necessary changes caused by events outside the researcher's control or unexpected anomalies, which implies that amendment is exceptional and reason-bearing rather than routine editing.
- [fact; source: https://www.cos.io/initiatives/registered-reports; https://help.osf.io/article/330-welcome-to-registrations] Registered reports push the same norm further by treating continuity from Stage 1 to final publication as a governed commitment, and sequential registrations are allowed only when each completed cycle preserves the prior accepted version.
- Access note: SSRN seeded FAQ and support pages returned Cloudflare interstitials in this runtime, so this item records SSRN as an unresolved evidence gap rather than inferring SSRN-specific display or retention behavior from uncitable secondary summaries.

#### B. PKM norms

- [fact; source: https://www.soenkeahrens.de/en/takesmartnotes] Ahrens describes Zettelkasten as tool-agnostic and emphasises the principles of linked, developing notes rather than any requirement for immutable duplicate files whenever a note evolves.
- [inference; source: https://www.soenkeahrens.de/en/takesmartnotes] Zettelkasten therefore supplies a norm of evolvable notes plus preserved context, not a norm of mandatory per-version file cloning, which makes it compatible with commit-based history if change remains reconstructible.
- [fact; source: https://github.com/denolehov/obsidian-git/blob/master/README.md] The Obsidian Git plugin exposes automatic commit, pull, push, history view, diff view, and restore-oriented workflows, which means its practical versioning model is a stable note file backed by explicit git snapshots rather than sibling files for each revision.
- [inference; source: https://github.com/denolehov/obsidian-git/blob/master/README.md; https://git-scm.com/docs/user-manual#object-name] Obsidian Git's model matches the repository's pragmatic design more closely than arXiv's visible version-chain interface does, because the human-readable note remains singular while the history substrate lives in commit objects and diffs.
- Access note: the seeded Logseq version-control page did not yield usable plain-text evidence here, and official code search did not surface a stable dedicated page for note-level versioning, so this item does not make Logseq-specific claims beyond noting the evidence gap.

#### C. Git as audit substrate

- [fact; source: https://git-scm.com/docs/user-manual#object-name] Git stores project history as interrelated snapshots called commits, each commit has a globally unique object name derived from its contents, and a commit cannot change without its object name also changing.
- [fact; source: https://git-scm.com/book/en/v2/Git-Tools-Rewriting-History] Git also explicitly allows local history rewriting, and its own documentation warns that once work is pushed it should generally be treated as final because rewriting pushed history confuses collaborators and replaces commit identifiers.
- [fact; source: https://git-scm.com/docs/hash-function-transition] Git now documents both SHA-1 and SHA-256 object naming, which means the practical identity guarantee is content-addressed object naming rather than dependence on one forever-specific hash function.
- [inference; source: https://git-scm.com/docs/user-manual#object-name; https://git-scm.com/book/en/v2/Git-Tools-Rewriting-History; https://git-scm.com/docs/hash-function-transition] For this repository, the dominant audit risk is therefore not accidental identifier collision but reachable-history loss through force-push, rebase, or amended commits on `main`.

#### D. Minimum auditability standard

- [inference; source: https://info.arxiv.org/help/versions.html; https://help.osf.io/article/113-advanced-actions-registrations; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-27-academic-post-publication-amendment-practices.md] An independent reader needs five things to reconstruct a post-publication change safely: a stable record being amended, a visible version or update number, a timestamp, a terse reason for change, and a path to inspect the exact old and new content.
- [inference; source: https://info.arxiv.org/help/versions.html; https://git-scm.com/docs/user-manual#object-name] arXiv satisfies the fifth requirement with public version files under one identifier, while a git-backed corpus can satisfy it with a full commit SHA plus reachable commit history if the commit remains permanently addressable.
- [inference; source: https://help.osf.io/article/113-advanced-actions-registrations; https://www.cos.io/initiatives/registered-reports] OSF and registered reports show that an update model does not need duplicated full-text files per version to be legitimate, but it does need explicit reader-facing notice, justification, and preserved prior state.

#### E. Candidate model comparison

- [inference; source: https://info.arxiv.org/help/versions.html] **Immutable vN files:** strongest reader-visible preservation, but highest duplication cost and highest maintenance burden, because every correction or revision requires a full-file copy even when git already stores the diff.
- [inference; source: https://help.osf.io/article/113-advanced-actions-registrations; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-27-academic-post-publication-amendment-practices.md] **Separate amendment file:** strong separation between record and notice, but duplicates part of the explanation burden that `versions:` plus a progress log already carries, and creates another file-coordination surface for agents.
- [inference; source: https://www.cos.io/initiatives/registered-reports; https://github.com/denolehov/obsidian-git/blob/master/README.md] **In-file amendments appendix:** lowest file-count burden, but weakest protection against quiet overwrite, because the amendment notice and the amended text can be changed together without an obvious external boundary.
- [inference; source: https://git-scm.com/docs/user-manual#object-name; https://git-scm.com/book/en/v2/Git-Tools-Rewriting-History; https://github.com/davidamitchell/Research/blob/main/docs-adr/0013-research-item-frontmatter-schema-extension.md] **`versions:` plus git history:** sufficient if and only if each substantive change increments the visible version chain, records date and reason, points to a full commit SHA, links the progress log, and relies on append-only reachable history on `main`.

#### F. Correction vs revision threshold

- [inference; source: https://help.osf.io/article/113-advanced-actions-registrations; https://info.arxiv.org/help/versions.html; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-27-academic-post-publication-amendment-practices.md] A **minor correction** is a change that improves access, wording precision, or metadata without changing any finding, confidence grade, cited-source identity, or conclusion, so it can stay within the same major version line.
- [inference; source: https://info.arxiv.org/help/versions.html; https://www.cos.io/initiatives/registered-reports] A **substantive revision** is any change that alters the evidence balance, findings, confidence, interpretation, or recommended action, because those changes modify what the record means rather than merely how it is read.
- [inference; source: https://github.com/davidamitchell/Research/blob/main/docs-adr/0013-research-item-frontmatter-schema-extension.md] The current repository rule that tags and related-item metadata are exempt from `versions:` entries remains consistent with this threshold, but ADR-0013 does not yet define the correction-versus-revision boundary explicitly enough for repeatable agent behavior.

#### G. Relationship vocabulary

- [fact; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-03-knowledge-linking-connected-corpus.md] The current corpus already encodes `extends`, `contradicts`, `depends-on`, `spawned-from`, and `see-also`, so any new edge type should represent a relation that those five cannot express cleanly.
- [inference; source: https://info.arxiv.org/help/versions.html; https://help.osf.io/article/113-advanced-actions-registrations; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-27-academic-post-publication-amendment-practices.md] `corrects:` is warranted, because amendment systems treat correction as a distinct governance relation between a later notice and an earlier record, and `extends` or `contradicts` do not tell the reader that the later item is the authoritative fix.
- [inference; source: https://help.osf.io/article/330-welcome-to-registrations; https://www.cos.io/initiatives/registered-reports] `replicates:` is not yet warranted for this repository's relationship vocabulary, because the sampled amendment and note-evolution systems distinguish version lineage from study-design repetition, and the corpus does not currently operate a systematic replication programme that needs a dedicated edge.

### §3 Reasoning

- [inference; source: https://info.arxiv.org/help/versions.html; https://help.osf.io/article/113-advanced-actions-registrations; https://git-scm.com/docs/user-manual#object-name] The convergent norm across arXiv, OSF, and git-backed PKM is not "one file per version"; it is "preserve prior state and surface later change in a way a reader can inspect."
- [inference; source: https://info.arxiv.org/help/versions.html; https://git-scm.com/book/en/v2/Git-Tools-Rewriting-History] That means the repository does not need arXiv-style duplicate files if its stable item plus `versions:` chain plus full commit SHA already lets a reader retrieve the old state reliably.
- [inference; source: https://git-scm.com/book/en/v2/Git-Tools-Rewriting-History; https://github.com/denolehov/obsidian-git/blob/master/README.md] The real discriminator is therefore not file multiplicity but append-only history discipline, because git-backed note systems are only auditable when history remains reachable and not silently rewritten.
- [inference; source: https://help.osf.io/article/113-advanced-actions-registrations; https://github.com/davidamitchell/Research/blob/main/docs-adr/0013-research-item-frontmatter-schema-extension.md] The pragmatic repository model is strong enough, but only if ADR-0013 is interpreted as a visible notice layer on top of immutable commit history rather than as permission to edit completed items with minimal explanation.

### §4 Consistency Check

- [fact; source: https://info.arxiv.org/help/versions.html; https://help.osf.io/article/113-advanced-actions-registrations] The external evidence consistently preserves prior state and requires explicit later notice; no sampled primary source endorsed silent substantive overwrite.
- [fact; source: https://git-scm.com/book/en/v2/Git-Tools-Rewriting-History; https://git-scm.com/docs/user-manual#object-name] The git evidence is internally consistent that commit IDs are content-addressed and that history rewriting changes them, so append-only reachable history is a necessary precondition for auditability.
- [inference; source: https://github.com/denolehov/obsidian-git/blob/master/README.md; https://www.soenkeahrens.de/en/takesmartnotes] The PKM evidence supports stable files plus inspectable history, but it does not by itself answer public-reader discoverability, so the recommendation must still lean on arXiv and OSF for the explicit notice requirement.
- [inference; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-27-academic-post-publication-amendment-practices.md; https://github.com/davidamitchell/Research/blob/main/docs-adr/0013-research-item-frontmatter-schema-extension.md] The new conclusion narrows and supersedes the earlier amendment-practices item because the repository now has a site-rendered `versions:` table and structured progress-log linkage that did not exist when the earlier item preferred separate amendment files.

### §5 Depth and Breadth Expansion

- [fact; source: https://git-scm.com/book/en/v2/Git-Tools-Rewriting-History; https://git-scm.com/docs/hash-function-transition] The technical lens shows that force-push and history rewrite are higher-probability audit failures than SHA collisions, because git documents routine history rewriting explicitly while hash-function migration exists precisely to manage the lower-probability cryptographic edge case.
- [fact; source: https://help.osf.io/article/113-advanced-actions-registrations; https://www.cos.io/initiatives/registered-reports] The governance lens shows that amendment systems are designed to make later interpretation legible to third parties, not merely to authors, so the repository's visible version table and progress-link requirement are governance controls rather than documentation niceties.
- [inference; source: https://github.com/denolehov/obsidian-git/blob/master/README.md; https://www.soenkeahrens.de/en/takesmartnotes] The behavioural lens suggests that a single canonical file lowers everyday note-maintenance friction, which makes policy compliance more likely than a duplicate-file model that asks authors and agents to clone whole items for minor corrections.
- [inference; source: https://info.arxiv.org/help/versions.html; https://help.osf.io/article/113-advanced-actions-registrations; https://git-scm.com/docs/user-manual#object-name] The operationally balanced design is therefore a hybrid: stable item path, explicit visible version chain, append-only commit history, and a rule that major interpretive change increments the major version instead of spawning a sibling full-text file.

### §6 Synthesis

**Executive summary:**

- [inference; source: https://info.arxiv.org/help/versions.html; https://help.osf.io/article/113-advanced-actions-registrations; https://git-scm.com/docs/user-manual#object-name; https://git-scm.com/book/en/v2/Git-Tools-Rewriting-History] The repository's frontmatter `versions:` array plus git commit history is sufficient for this corpus if it is treated as a visible, append-only version chain with full commit SHAs and progress-log links, rather than as a lightweight note-to-self on top of silently mutable files.
- [fact; source: https://info.arxiv.org/help/versions.html; https://help.osf.io/article/113-advanced-actions-registrations] arXiv and OSF both preserve prior state and surface later change explicitly.
- [inference; source: https://info.arxiv.org/help/versions.html; https://help.osf.io/article/113-advanced-actions-registrations; https://git-scm.com/docs/user-manual#object-name] Those patterns mean the repository does not need an arXiv-style vN-file scheme to meet the same minimum norm, because a visible version chain can be implemented without duplicating full-text files.
- [inference; source: https://github.com/denolehov/obsidian-git/blob/master/README.md; https://www.soenkeahrens.de/en/takesmartnotes; https://git-scm.com/docs/user-manual#object-name] PKM practice supports the same conclusion, because note systems centered on git history assume one live note backed by inspectable commit snapshots rather than one full file per note revision.
- [inference; source: https://git-scm.com/book/en/v2/Git-Tools-Rewriting-History; https://github.com/davidamitchell/Research/blob/main/docs-adr/0013-research-item-frontmatter-schema-extension.md] The main design change still needed is not a stricter file-layout model but a stricter governance rule in ADR-0013 that defines correction-versus-revision thresholds and treats rewrite of pushed `main` history as disallowed for versioned completed items.

**Key findings:**

- 1. [fact; source: https://info.arxiv.org/help/versions.html; https://arxiv.org/abs/2206.04615] arXiv's governing norm is a stable identifier with an explicit visible version chain, because replacements, withdrawals, errata, annual updates, and living reviews all remain linked under one record while prior versions stay accessible. **Confidence: high**
- 2. [fact; source: https://help.osf.io/article/330-welcome-to-registrations; https://help.osf.io/article/113-advanced-actions-registrations] OSF's governing norm is frozen primary records plus explicit update workflow, because submitted registrations cannot be edited in place and later changes require a separate, justified update process that preserves the original registration. **Confidence: high**
- 3. [inference; source: https://www.cos.io/initiatives/registered-reports; https://help.osf.io/article/113-advanced-actions-registrations] Registered-reports practice reinforces the same principle by making amendment acceptable only when continuity and justification remain explicit, which favours reader-visible notice chains over silent mutation. **Confidence: medium**
- 4. [inference; source: https://www.soenkeahrens.de/en/takesmartnotes; https://github.com/denolehov/obsidian-git/blob/master/README.md] The retrievable PKM evidence does not support mandatory immutable per-version note files, because Zettelkasten is tool-agnostic and Obsidian Git implements auditability through commits, diffs, and history views around one canonical note. **Confidence: medium**
- 5. [inference; source: https://git-scm.com/docs/user-manual#object-name; https://git-scm.com/book/en/v2/Git-Tools-Rewriting-History] Git can satisfy the "what changed" inspection requirement because commits are content-addressed snapshots, but git can only serve as a trustworthy audit substrate when pushed history is treated as append-only. **Confidence: high**
- 6. [inference; source: https://info.arxiv.org/help/versions.html; https://help.osf.io/article/113-advanced-actions-registrations; https://git-scm.com/docs/user-manual#object-name; https://github.com/davidamitchell/Research/blob/main/docs-adr/0013-research-item-frontmatter-schema-extension.md] The repository's current `versions:` model is therefore sufficient if each substantive edit records a visible version number, changed date, one-line reason, full commit SHA, and linked progress log, because together those fields recreate the minimum audit trail that the sampled systems require. **Confidence: medium**
- 7. [inference; source: https://help.osf.io/article/113-advanced-actions-registrations; https://info.arxiv.org/help/versions.html; https://github.com/davidamitchell/Research/blob/main/docs-adr/0013-research-item-frontmatter-schema-extension.md] The correction-versus-revision boundary should be formalised as minor when findings and evidence balance stay unchanged, and major when any finding, confidence grade, recommendation, or cited-source identity changes. **Confidence: medium**
- 8. [inference; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-03-knowledge-linking-connected-corpus.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-27-academic-post-publication-amendment-practices.md; https://info.arxiv.org/help/versions.html] `corrects:` should be added to the relationship vocabulary because it expresses authoritative amendment lineage, while `replicates:` should wait until the corpus actually tracks a repeatable replication programme that needs a distinct edge. **Confidence: medium**

**Evidence map:**

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [fact] arXiv preserves prior versions under one stable identifier and exposes version history publicly. | https://info.arxiv.org/help/versions.html; https://arxiv.org/abs/2206.04615 | high | Stable identifier plus visible version chain |
| [fact] OSF freezes submitted registrations and routes later changes through explicit updates. | https://help.osf.io/article/330-welcome-to-registrations; https://help.osf.io/article/113-advanced-actions-registrations | high | Read-only record plus justified update |
| [inference] Registered reports favour explicit continuity and staged amendment over silent mutation. | https://www.cos.io/initiatives/registered-reports; https://help.osf.io/article/113-advanced-actions-registrations | medium | Continuity logic, not a one-sentence rule |
| [inference] PKM evidence supports one canonical note plus git-backed history rather than duplicate full-text files. | https://www.soenkeahrens.de/en/takesmartnotes; https://github.com/denolehov/obsidian-git/blob/master/README.md | medium | Logseq remains an evidence gap |
| [inference] Git can satisfy the inspection requirement if pushed history stays append-only. | https://git-scm.com/docs/user-manual#object-name; https://git-scm.com/book/en/v2/Git-Tools-Rewriting-History | high | Git properties plus governance constraint |
| [inference] `versions:` plus git meets the minimum norm if version number, date, reason, full SHA, and progress link stay visible. | https://info.arxiv.org/help/versions.html; https://help.osf.io/article/113-advanced-actions-registrations; https://git-scm.com/docs/user-manual#object-name; https://github.com/davidamitchell/Research/blob/main/docs-adr/0013-research-item-frontmatter-schema-extension.md | medium | Reader-visible notice plus diff substrate |
| [inference] Minor versus major version boundaries should follow interpretive impact, not text length. | https://help.osf.io/article/113-advanced-actions-registrations; https://info.arxiv.org/help/versions.html; https://github.com/davidamitchell/Research/blob/main/docs-adr/0013-research-item-frontmatter-schema-extension.md | medium | Governance threshold derived from sampled systems |
| [inference] `corrects:` is warranted now, while `replicates:` is not yet warranted. | https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-03-knowledge-linking-connected-corpus.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-27-academic-post-publication-amendment-practices.md; https://info.arxiv.org/help/versions.html | medium | Distinct amendment lineage versus future replication need |

**Assumptions:**

- [assumption; source: https://github.com/denolehov/obsidian-git/blob/master/README.md; https://git-scm.com/docs/user-manual#object-name] The Obsidian Git plugin is a reasonable proxy for PKM systems that externalise versioning into git, because it is an official implementation document for one widely used markdown-note workflow and exposes the exact audit surfaces this item evaluates.
- [assumption; source: https://github.com/davidamitchell/Research/blob/main/docs-adr/0013-research-item-frontmatter-schema-extension.md; https://git-scm.com/book/en/v2/Git-Tools-Rewriting-History] The repository can enforce an append-only norm on `main` well enough for audit purposes, even though git itself technically permits history rewriting.

**Analysis:**

- [inference; source: https://info.arxiv.org/help/versions.html; https://help.osf.io/article/113-advanced-actions-registrations] The core norm across the sampled academic systems is preservation plus explanation, not preservation plus file duplication, so the repository should optimise for reader legibility of change rather than mimic arXiv's exact storage surface.
- [inference; source: https://git-scm.com/docs/user-manual#object-name; https://git-scm.com/book/en/v2/Git-Tools-Rewriting-History] Git already supplies the diff and immutable snapshot identity that arXiv exposes through public file versions, which means the repository only needs a human-readable notice index on top of git rather than a second full-text archival layer.
- [inference; source: https://github.com/denolehov/obsidian-git/blob/master/README.md; https://www.soenkeahrens.de/en/takesmartnotes] PKM practice matters because this corpus is both a publication surface and a working knowledge base, and the retrievable PKM evidence suggests that keeping one canonical note and pushing version granularity into history tools lowers maintenance friction.
- [inference; source: https://git-scm.com/book/en/v2/Git-Tools-Rewriting-History; https://github.com/davidamitchell/Research/blob/main/docs-adr/0013-research-item-frontmatter-schema-extension.md] The strongest challenge to the pragmatic model is not insufficiency of frontmatter fields but governance slippage, because a `versions:` array is only as trustworthy as the repository rule that prevents later disappearance or replacement of the commit it names.
- [inference; source: https://help.osf.io/article/113-advanced-actions-registrations; https://www.cos.io/initiatives/registered-reports] The main rival remedy, separate amendment files, remains defensible for public scholarly systems with indexing infrastructure, but in this repository it adds coordination overhead without giving readers more exact diff fidelity than git already provides.

**Risks, gaps, uncertainties:**

- [fact; source: https://git-scm.com/book/en/v2/Git-Tools-Rewriting-History] History rewrite on `main` would break the pragmatic model's auditability more severely than any ordinary editing mistake, because the `versions:` entry would then point at a commit path that may no longer be reachable in the shared branch history.
- [fact; source: https://git-scm.com/docs/hash-function-transition] Hash-function change is a real but lower-order risk, because git already documents SHA-256 migration and treats object naming as a repository-format concern rather than a reason to abandon content-addressed audit trails.
- [inference; source: https://github.com/davidamitchell/Research/blob/main/docs-adr/0013-research-item-frontmatter-schema-extension.md] Orphaned progress-log paths remain possible if later refactors move session logs, so the repository should continue treating the progress path as part of the durable audit chain rather than as disposable process exhaust.
- [inference; source: https://github.com/denolehov/obsidian-git/blob/master/README.md; https://www.soenkeahrens.de/en/takesmartnotes] The PKM comparison is weaker than the pre-print comparison because the retrievable evidence is concentrated in Zettelkasten principle guidance and Obsidian Git documentation, with no directly usable SSRN or Logseq primary text available in this session.

**Open questions:**

- [inference; source: https://git-scm.com/book/en/v2/Git-Tools-Rewriting-History; https://github.com/davidamitchell/Research/blob/main/docs-adr/0013-research-item-frontmatter-schema-extension.md] Should the repository add an automated check that rejects force-push-like history rewrites or non-full SHAs in `versions:` entries so the append-only assumption is enforced rather than merely documented?
- [inference; source: https://info.arxiv.org/help/versions.html; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-03-knowledge-linking-connected-corpus.md] If `corrects:` is added, should the site render a stronger reader warning for corrected items in the same way it already renders `superseded_by:` banners?
- [inference; source: https://help.osf.io/article/330-welcome-to-registrations; https://www.cos.io/initiatives/registered-reports] If the corpus starts producing deliberate replications of earlier claims, should `replicates:` become part of the canonical edge vocabulary at that point rather than now?

### §7 Recursive Review

- [fact; source: https://info.arxiv.org/help/versions.html; https://help.osf.io/article/113-advanced-actions-registrations; https://git-scm.com/docs/user-manual#object-name] Every substantive conclusion in this item is anchored to accessible arXiv, OSF, git, PKM, or prior-repository evidence, and the recommendation is kept at medium overall confidence because SSRN and Logseq remain unresolved evidence gaps.
- [fact; source: https://github.com/davidamitchell/Research/blob/main/docs-adr/0013-research-item-frontmatter-schema-extension.md] The synthesis and Findings sections are aligned on recommendation, confidence, and proposed relationship-vocabulary change.
- [inference; source: https://git-scm.com/book/en/v2/Git-Tools-Rewriting-History; https://github.com/davidamitchell/Research/blob/main/docs-adr/0013-research-item-frontmatter-schema-extension.md] No unresolved contradiction remains strong enough to force a different repository design, but the recommendation depends on an explicit no-history-rewrite governance rule that ADR-0013 should record more clearly.

---

## Findings

### Executive Summary

The repository's frontmatter `versions:` array plus git commit history is sufficient for this corpus if it is treated as a visible, append-only version chain with full commit SHAs and progress-log links, rather than as a lightweight note-to-self on top of silently mutable files. [inference; source: https://info.arxiv.org/help/versions.html; https://help.osf.io/article/113-advanced-actions-registrations; https://git-scm.com/docs/user-manual#object-name; https://git-scm.com/book/en/v2/Git-Tools-Rewriting-History]

arXiv and OSF both preserve prior state and surface later change explicitly. [fact; source: https://info.arxiv.org/help/versions.html; https://help.osf.io/article/113-advanced-actions-registrations]

Those patterns mean this repository does not need an arXiv-style vN-file scheme to satisfy the same minimum auditability norm, because a visible version chain can be implemented without duplicating full-text files. [inference; source: https://info.arxiv.org/help/versions.html; https://help.osf.io/article/113-advanced-actions-registrations; https://git-scm.com/docs/user-manual#object-name]

The retrievable PKM evidence points the same way, because Zettelkasten is tool-agnostic about note evolution and Obsidian Git uses one canonical note backed by commit history, diff view, and restore workflows rather than one full file per revision. [inference; source: https://www.soenkeahrens.de/en/takesmartnotes; https://github.com/denolehov/obsidian-git/blob/master/README.md]

The main repository change still required is therefore governance, not storage layout: ADR-0013 should define correction-versus-revision thresholds explicitly and treat rewrite of pushed `main` history as disallowed for completed items that carry `versions:` entries. [inference; source: https://git-scm.com/book/en/v2/Git-Tools-Rewriting-History; https://github.com/davidamitchell/Research/blob/main/docs-adr/0013-research-item-frontmatter-schema-extension.md]

### Key Findings

1. **arXiv's governing norm is a stable identifier with an explicit visible version chain, because replacements, withdrawals, errata, annual updates, and living reviews all remain linked under one record while prior versions stay accessible.** ([fact]; high confidence; source: https://info.arxiv.org/help/versions.html; https://arxiv.org/abs/2206.04615)
2. **OSF's governing norm is frozen primary records plus explicit update workflow, because submitted registrations cannot be edited in place and later changes require a separate, justified update process that preserves the original registration.** ([fact]; high confidence; source: https://help.osf.io/article/330-welcome-to-registrations; https://help.osf.io/article/113-advanced-actions-registrations)
3. **Registered-reports practice reinforces the same principle by making amendment acceptable only when continuity and justification remain explicit, which favours reader-visible notice chains over silent mutation.** ([inference]; medium confidence; source: https://www.cos.io/initiatives/registered-reports; https://help.osf.io/article/113-advanced-actions-registrations)
4. **The retrievable PKM evidence does not support mandatory immutable per-version note files, because Zettelkasten is tool-agnostic and Obsidian Git implements auditability through commits, diffs, and history views around one canonical note.** ([inference]; medium confidence; source: https://www.soenkeahrens.de/en/takesmartnotes; https://github.com/denolehov/obsidian-git/blob/master/README.md)
5. **Git can satisfy the "what changed" inspection requirement because commits are content-addressed snapshots, but git can only serve as a trustworthy audit substrate when pushed history is treated as append-only.** ([inference]; high confidence; source: https://git-scm.com/docs/user-manual#object-name; https://git-scm.com/book/en/v2/Git-Tools-Rewriting-History)
6. **The repository's current `versions:` model is therefore sufficient if each substantive edit records a visible version number, changed date, one-line reason, full commit SHA, and linked progress log, because together those fields recreate the minimum audit trail that the sampled systems require.** ([inference]; medium confidence; source: https://info.arxiv.org/help/versions.html; https://help.osf.io/article/113-advanced-actions-registrations; https://git-scm.com/docs/user-manual#object-name; https://github.com/davidamitchell/Research/blob/main/docs-adr/0013-research-item-frontmatter-schema-extension.md)
7. **The correction-versus-revision boundary should be formalised as minor when findings and evidence balance stay unchanged, and major when any finding, confidence grade, recommendation, or cited-source identity changes.** ([inference]; medium confidence; source: https://help.osf.io/article/113-advanced-actions-registrations; https://info.arxiv.org/help/versions.html; https://github.com/davidamitchell/Research/blob/main/docs-adr/0013-research-item-frontmatter-schema-extension.md)
8. **`corrects:` should be added to the relationship vocabulary because it expresses authoritative amendment lineage, while `replicates:` should wait until the corpus actually tracks a repeatable replication programme that needs a distinct edge.** ([inference]; medium confidence; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-03-knowledge-linking-connected-corpus.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-27-academic-post-publication-amendment-practices.md; https://info.arxiv.org/help/versions.html)

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [fact] arXiv preserves prior versions under one stable identifier and exposes version history publicly. | https://info.arxiv.org/help/versions.html; https://arxiv.org/abs/2206.04615 | high | Stable identifier plus visible version chain |
| [fact] OSF freezes submitted registrations and routes later changes through explicit updates. | https://help.osf.io/article/330-welcome-to-registrations; https://help.osf.io/article/113-advanced-actions-registrations | high | Read-only record plus justified update |
| [inference] Registered reports favour explicit continuity and staged amendment over silent mutation. | https://www.cos.io/initiatives/registered-reports; https://help.osf.io/article/113-advanced-actions-registrations | medium | Continuity logic rather than one-line rule |
| [inference] PKM evidence supports one canonical note plus git-backed history rather than duplicate full-text files. | https://www.soenkeahrens.de/en/takesmartnotes; https://github.com/denolehov/obsidian-git/blob/master/README.md | medium | Logseq remains a gap |
| [inference] Git can satisfy the inspection requirement if pushed history stays append-only. | https://git-scm.com/docs/user-manual#object-name; https://git-scm.com/book/en/v2/Git-Tools-Rewriting-History | high | Git properties plus governance constraint |
| [inference] `versions:` plus git meets the minimum norm if version number, date, reason, full SHA, and progress link stay visible. | https://info.arxiv.org/help/versions.html; https://help.osf.io/article/113-advanced-actions-registrations; https://git-scm.com/docs/user-manual#object-name; https://github.com/davidamitchell/Research/blob/main/docs-adr/0013-research-item-frontmatter-schema-extension.md | medium | Reader-visible notice plus diff substrate |
| [inference] Minor versus major version boundaries should follow interpretive impact, not text length. | https://help.osf.io/article/113-advanced-actions-registrations; https://info.arxiv.org/help/versions.html; https://github.com/davidamitchell/Research/blob/main/docs-adr/0013-research-item-frontmatter-schema-extension.md | medium | Governance threshold derived from sampled systems |
| [inference] `corrects:` is warranted now, while `replicates:` is not yet warranted. | https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-03-knowledge-linking-connected-corpus.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-27-academic-post-publication-amendment-practices.md; https://info.arxiv.org/help/versions.html | medium | Distinct amendment lineage versus future replication need |

### Assumptions

- Obsidian Git is a reasonable proxy for PKM systems that externalise versioning into git, because it is an official implementation document for one widely used markdown-note workflow and exposes the exact audit surfaces this item evaluates. [assumption; source: https://github.com/denolehov/obsidian-git/blob/master/README.md; https://git-scm.com/docs/user-manual#object-name]
- The repository can enforce an append-only norm on `main` well enough for audit purposes, even though git itself technically permits history rewriting. [assumption; source: https://github.com/davidamitchell/Research/blob/main/docs-adr/0013-research-item-frontmatter-schema-extension.md; https://git-scm.com/book/en/v2/Git-Tools-Rewriting-History]

### Analysis

The core norm across the sampled academic systems is preservation plus explanation, not preservation plus file duplication, so the repository should optimise for reader legibility of change rather than mimic arXiv's exact storage surface. [inference; source: https://info.arxiv.org/help/versions.html; https://help.osf.io/article/113-advanced-actions-registrations]

Git already supplies the diff and immutable snapshot identity that arXiv exposes through public file versions, which means the repository only needs a human-readable notice index on top of git rather than a second full-text archival layer. [inference; source: https://git-scm.com/docs/user-manual#object-name; https://git-scm.com/book/en/v2/Git-Tools-Rewriting-History]

PKM practice matters because this corpus is both a publication surface and a working knowledge base, and the retrievable PKM evidence suggests that keeping one canonical note and pushing version granularity into history tools lowers maintenance friction. [inference; source: https://github.com/denolehov/obsidian-git/blob/master/README.md; https://www.soenkeahrens.de/en/takesmartnotes]

The strongest challenge to the pragmatic model is not insufficiency of frontmatter fields but governance slippage, because a `versions:` array is only as trustworthy as the repository rule that prevents later disappearance or replacement of the commit it names. [inference; source: https://git-scm.com/book/en/v2/Git-Tools-Rewriting-History; https://github.com/davidamitchell/Research/blob/main/docs-adr/0013-research-item-frontmatter-schema-extension.md]

The main rival remedy, separate amendment files, remains defensible for public scholarly systems with indexing infrastructure, but in this repository it adds coordination overhead without giving readers more exact diff fidelity than git already provides. [inference; source: https://help.osf.io/article/113-advanced-actions-registrations; https://www.cos.io/initiatives/registered-reports]

### Risks, Gaps, and Uncertainties

- History rewrite on `main` would break the pragmatic model's auditability more severely than any ordinary editing mistake, because the `versions:` entry would then point at a commit path that may no longer be reachable in shared history. [fact; source: https://git-scm.com/book/en/v2/Git-Tools-Rewriting-History]
- Hash-function change is a real but lower-order risk, because git already documents SHA-256 migration and treats object naming as a repository-format concern rather than as a reason to abandon content-addressed audit trails. [fact; source: https://git-scm.com/docs/hash-function-transition]
- Orphaned progress-log paths remain possible if later refactors move session logs, so the repository should continue treating the progress path as part of the durable audit chain rather than as disposable process exhaust. [inference; source: https://github.com/davidamitchell/Research/blob/main/docs-adr/0013-research-item-frontmatter-schema-extension.md]
- The PKM comparison is weaker than the pre-print comparison because the retrievable evidence is concentrated in Zettelkasten principle guidance and Obsidian Git documentation, with no directly usable SSRN or Logseq primary text available in this session. [inference; source: https://github.com/denolehov/obsidian-git/blob/master/README.md; https://www.soenkeahrens.de/en/takesmartnotes]

### Open Questions

- Should the repository add an automated check that rejects history rewrites or non-full SHAs in `versions:` entries so the append-only assumption is enforced rather than merely documented? [inference; source: https://git-scm.com/book/en/v2/Git-Tools-Rewriting-History; https://github.com/davidamitchell/Research/blob/main/docs-adr/0013-research-item-frontmatter-schema-extension.md]
- If `corrects:` is added, should the site render a stronger reader warning for corrected items in the same way it already renders `superseded_by:` banners? [inference; source: https://info.arxiv.org/help/versions.html; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-03-knowledge-linking-connected-corpus.md]
- If the corpus starts producing deliberate replications of earlier claims, should `replicates:` become part of the canonical edge vocabulary at that point rather than now? [inference; source: https://help.osf.io/article/330-welcome-to-registrations; https://www.cos.io/initiatives/registered-reports]

---

## Output

- Type: knowledge
- Description: The item validates the repository's pragmatic versioning model as sufficient with stronger governance constraints, recommends adding `corrects:` but not yet `replicates:`, and calls for an ADR-0013 update that formalises append-only history and version-threshold rules. [inference; source: https://info.arxiv.org/help/versions.html; https://help.osf.io/article/113-advanced-actions-registrations; https://git-scm.com/book/en/v2/Git-Tools-Rewriting-History; https://github.com/davidamitchell/Research/blob/main/docs-adr/0013-research-item-frontmatter-schema-extension.md]
- Links:
  - https://info.arxiv.org/help/versions.html
  - https://help.osf.io/article/113-advanced-actions-registrations
  - https://git-scm.com/docs/user-manual#object-name
