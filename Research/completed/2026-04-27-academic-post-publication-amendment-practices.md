---
review_count: 2
title: "How do academic and scientific publishing systems handle post-publication corrections, amendments, retractions, and commentary, and what is the minimal viable analogue for a versioned git-based research corpus?"
added: 2026-04-27T06:20:00+00:00
status: completed
priority: high
blocks: []
tags: [academic-publishing, post-publication, corrections, retractions, amendments, rebuttal, immutability, versioning, knowledge-management, research-methodology, doi, corrigendum, erratum]
started: 2026-04-27T08:55:01+00:00
completed: 2026-04-27T09:27:23+00:00
output: [knowledge]
cites: []          # slugs of items this item directly depends on or quotes
related: []        # slugs of thematically connected items
superseded_by: ~   # slug of a later item that overrides this one (null if not superseded)
supersedes: ~      # slug of an older item this one replaces (null if not applicable)
item_type: primary # primary | synthesis
confidence: medium # high | medium | low
versions: []       # entries: {version: "1.0", sha: "<commit-hash>", changed: YYYY-MM-DD, progress: "<path>", summary: "<one-line>"}
---

# How do academic and scientific publishing systems handle post-publication corrections, amendments, retractions, and commentary, and what is the minimal viable analogue for a versioned git-based research corpus?

## Research Question

How do established academic and scientific publishing systems (journal publishers, preprint servers, living review platforms) handle post-publication corrections, amendments, retractions, and formal commentary, and what is the minimal viable analogue for a versioned, git-based private research corpus where completed items should be treated as immutable records with narrow, explicitly defined exceptions?

## Scope

**In scope:**
- The four main post-publication update mechanisms in academic publishing: corrigenda or errata (corrections), retractions (invalidations), comments and replies (formal challenges and responses), and living reviews (continuously updated systematic reviews)
- The structural conventions used: how corrections are physically attached to the original record, what metadata fields change, what signals readers and indexing systems receive
- Preprint server versioning (arXiv, bioRxiv): how version history is preserved and surfaced, what constitutes a "new version" versus a "new paper"
- The distinction between acceptable silent corrections (typos, broken URLs) and corrections that require a formal record (factual claim changes, methodology changes, finding reversals)
- Cochrane Reviews as the gold standard for living systematic reviews: update protocol, versioning, what triggers an update versus a new review
- The practical minimum: what the smallest viable amendment mechanism looks like for a git-backed, Markdown-based corpus, specifically what must be structured data (frontmatter fields) versus prose

**Out of scope:**
- Legal aspects of retractions (libel, misconduct investigations)
- Full systematic review methodology (Preferred Reporting Items for Systematic Reviews and Meta-Analyses (PRISMA), Grading of Recommendations Assessment, Development and Evaluation (GRADE)), only the update and amendment protocol is in scope
- Publisher-specific proprietary systems (CrossRef mechanics, Digital Object Identifier (DOI) redirect infrastructure)
- Any mechanism requiring a database or external service, because the target implementation is pure git plus Markdown

**Constraints:**
- Primary sources preferred: publisher guidelines, Committee on Publication Ethics (COPE) guidance, actual retraction notices, and arXiv versioning documentation
- The output must include a specific recommendation for the amendment frontmatter schema and amendment item template for this repository

## Context

[fact; source: https://davidamitchell.github.io/Research/research/2026-04-22-knowledge-curation-governance-for-regulated-ai.html; https://davidamitchell.github.io/Research/research/2026-03-02-agent-memory-management-context-injection.html] Prior completed work in this repository already identified provenance, freshness, contradiction handling, and correction-to-source traceability as governance requirements for authoritative knowledge systems.

[inference; source: https://www.nature.com/nature/editorial-policies/correction-and-retraction-policy; https://info.arxiv.org/help/versions.html] This item narrows that broader governance problem to completed research notes: if the corpus is meant to preserve what was believed at a point in time, substantive post-publication changes need a formal amendment path rather than silent overwrite.

## Approach

1. **Corrigendum and erratum mechanics:** Survey major journal publishers for their published correction policies. What triggers a correction? What is physically published? How is it linked to the original? What metadata changes?
2. **Retraction mechanics:** Survey publisher policies and retraction-oriented guidance. What constitutes a retraction versus a correction? What is the minimum retraction notice? Is the original removed or marked? What fields change?
3. **Comment and reply mechanics:** Survey how journals handle formal post-publication commentary. What is the structural relationship between comment and original? How are they indexed and linked?
4. **Living reviews:** Survey Cochrane update protocol and at least one other living-review format. What triggers an update? What is preserved from prior versions? What is the versioning convention?
5. **Preprint versioning:** Survey arXiv and bioRxiv versioning. What is preserved between versions? What triggers a new version? How are citations to earlier versions handled?
6. **Minimal viable analogue:** Based on the above, define the minimal set of mechanisms needed for a git-backed Markdown corpus. Specifically: what frontmatter fields are needed, what file naming convention for amendment items, what the amendment item template must contain, and what the three acceptable silent-edit exceptions are.
7. **Synthesis:** Produce a schema recommendation and amendment item template as the primary output.

## Sources

- [ ] [Committee on Publication Ethics (COPE) - Retraction Guidelines](https://publicationethics.org/retraction-guidelines) — - seeded primary source for retraction standards; not quoted directly below
- [ ] [COPE - Correction Guidelines](https://publicationethics.org/cope-guidelines-retracting-articles) — - seeded primary source for correction standards; not quoted directly below
- [x] [Nature - Corrections, Retractions and Matters Arising](https://www.nature.com/nature/editorial-policies/correction-and-retraction-policy) — - primary policy for corrections, retractions, addenda, expressions of concern, and formal commentary
- [x] [Nature - Matters Arising](https://www.nature.com/nature/for-authors/matters-arising) — - primary guidance for formal comment and reply handling
- [x] [Public Library of Science (PLOS) ONE - Corrections, Expressions of Concern, and Retractions](https://journals.plos.org/plosone/s/corrections-and-retractions) — - primary policy for correction and retraction thresholds
- [x] [Public Library of Science (PLOS) ONE - Comments](https://journals.plos.org/plosone/s/comments) — - primary guidance for lightweight post-publication discussion
- [x] [BMJ (British Medical Journal) Author Hub - Correction and retraction policies](https://authors.bmj.com/policies/correction-retraction-policies/) — - primary policy for version-of-record corrections and retractions
- [x] [arXiv - Submission Guidelines](https://info.arxiv.org/help/submit/index.html) — - primary guidance telling authors to replace rather than resubmit corrected work
- [x] [arXiv - Submission Version Availability](https://info.arxiv.org/help/versions.html) — - primary guidance for permanent version history, withdrawals, comments, and living-review updates
- [x] [bioRxiv - Frequently Asked Questions](https://www.biorxiv.org/about/FAQ) — - official revision guidance quoted through web search
- [x] [Cochrane Handbook for Systematic Reviews of Interventions, current version](https://www.cochrane.org/authors/handbooks-and-manuals/handbook/current) — - primary handbook showing review updating as a distinct governed process
- [x] [Cochrane decision framework for update proposals](https://documentation.cochrane.org/emkb/editorial-manager-for-authors/new-and-returning-authors/update-an-existing-review/decision-frameworkfor-update-proposals) — - primary trigger logic for update versus new protocol
- [x] [Guidance for the production and publication of Cochrane living systematic reviews](https://resources.cochrane.org/sites/resources.cochrane.org/files/uploads/inline-files/Transform/201912_LSR_Revised_Guidance.pdf) — - primary living-review guidance for versioning, update cadence, and transition out of living mode
- [x] [The Living Guidelines Handbook: Guidance for the production and publication of living clinical practice guidelines](https://research.monash.edu/en/publications/the-living-guidelines-handbook-guidance-for-the-production-and-pu/) — - official living-guideline guidance outside Cochrane, located through web search

## Related

- [Knowledge curation governance for regulated Artificial Intelligence (AI)](https://davidamitchell.github.io/Research/research/2026-04-22-knowledge-curation-governance-for-regulated-ai.html)
- [Agent memory management and context injection](https://davidamitchell.github.io/Research/research/2026-03-02-agent-memory-management-context-injection.html)
- [Context layers and aligned decisions synthesis](https://davidamitchell.github.io/Research/research/2026-03-15-context-layers-aligned-decisions-synthesis.html)

---

## Research Skill Output

*(Full output from running the research skill, retained verbatim in the completed item. Sections 0 to 5 are the investigation, and section 6 seeds the Findings section below.)*

### §0 Initialise

- [fact; source: https://www.nature.com/nature/editorial-policies/correction-and-retraction-policy; https://info.arxiv.org/help/versions.html] **Research question restated:** this item asks how mature publishing systems preserve the integrity of the scientific record after publication, and which of those mechanisms should be copied into a git-based research corpus whose completed items are intended to remain stable records.
- [fact; source: https://www.nature.com/nature/for-authors/matters-arising; https://documentation.cochrane.org/emkb/editorial-manager-for-authors/new-and-returning-authors/update-an-existing-review/decision-frameworkfor-update-proposals] **Scope confirmed:** the investigation covers corrections, retractions, commentary and reply, living-review updates, and preprint versioning, then reduces them to the minimum structured mechanism needed for this repository.
- [fact; source: https://www.nature.com/nature/editorial-policies/correction-and-retraction-policy; https://journals.plos.org/plosone/s/corrections-and-retractions; https://authors.bmj.com/policies/correction-retraction-policies/] **Constraints confirmed:** primary publisher and platform sources were weighted most heavily; blocked seeded sources were recorded as gaps; and the output must end with a frontmatter and amendment-template recommendation that can be implemented in pure git plus Markdown.
- [fact; source: https://davidamitchell.github.io/Research/research/2026-04-22-knowledge-curation-governance-for-regulated-ai.html; https://davidamitchell.github.io/Research/research/2026-03-02-agent-memory-management-context-injection.html; https://davidamitchell.github.io/Research/research/2026-03-15-context-layers-aligned-decisions-synthesis.html] **Prior work cross-reference:** adjacent completed items already established that provenance, freshness, contradiction handling, and correction-to-source traceability are governance problems rather than mere formatting problems, so this item treats post-publication amendment as another control surface in that same chain.
- [fact; source: https://www.nature.com/nature/editorial-policies/correction-and-retraction-policy; https://info.arxiv.org/help/versions.html] **Output format:** this item produces knowledge, specifically a recommendation for immutable completed items plus formal amendment records, with explicit thresholds for silent edits, correction, commentary, retraction, and living-update behavior.

### §1 Question Decomposition

- **Root question:** what minimum post-publication control model preserves provenance for a git-based research corpus without importing unnecessary journal infrastructure?
- **A. Correction threshold**
  - A1. Which kinds of errors trigger a formal correction rather than a silent fix?
  - A2. What information must a correction notice contain to preserve reader trust and indexing value?
- **B. Retraction threshold**
  - B1. What makes a published record unreliable enough to retract rather than correct?
  - B2. What happens to the original record after retraction?
- **C. Commentary mechanics**
  - C1. How do publishers distinguish formal challenge or clarification from correction?
  - C2. How are comments and replies linked to the original record?
- **D. Living-update mechanics**
  - D1. When is an update to the same review justified?
  - D2. When do scope or method changes require a new review or protocol instead?
- **E. Preprint versioning**
  - E1. How do versioned preprint systems preserve history while allowing revision?
  - E2. How do comments, replies, withdrawals, and annual updates fit into that history?
- **F. Repository analogue**
  - F1. Which fields must live in frontmatter on the original item?
  - F2. Which fields must live on a separate amendment item?
  - F3. Which post-completion edits are safe enough to remain silent?

### §2 Investigation

#### Source qualification notes

- [fact; source: https://journals.plos.org/plosone/s/corrections-and-retractions; https://www.nature.com/nature/editorial-policies/correction-and-retraction-policy] Direct Committee on Publication Ethics (COPE) text is not quoted below, so COPE-aligned conclusions are grounded only where accessible publisher policies explicitly cite or implement COPE guidance.

#### A. Correction mechanics

- [fact; source: https://www.nature.com/nature/editorial-policies/correction-and-retraction-policy] Nature distinguishes Author Correction, Publisher Correction, and Addendum, publishes them as separate notices, bidirectionally links them to the original article, indexes them, and uses Crossmark, which the policy defines as an industry-standard mechanism that lets readers check whether the article version they are reading is current.
- [fact; source: https://www.nature.com/nature/editorial-policies/correction-and-retraction-policy] Nature usually corrects the original HyperText Markup Language (HTML) and Portable Document Format (PDF) article as well as publishing the amendment notice, and when changed figures, tables, or data-bearing text are involved the notice reproduces the original data for transparency.
- [fact; source: https://journals.plos.org/plosone/s/corrections-and-retractions] Public Library of Science (PLOS) publishes a correction when errors affect the main contents or understanding of the article, while the overall results and conclusions remain upheld and no reliability concern exists.
- [fact; source: https://journals.plos.org/plosone/s/corrections-and-retractions] PLOS also uses correction notices for important metadata problems such as author-name, funding, competing-interest, or data-availability errors, but explicitly declines to publish corrections for typographical or other minor issues that do not substantively affect integrity, understanding, or indexing.
- [fact; source: https://authors.bmj.com/policies/correction-retraction-policies/] BMJ (British Medical Journal) states that honest errors require a published correction notice, that minor post-publication changes which do not affect scientific understanding may be rejected, and that previous electronic versions should prominently note when a newer corrected version exists.
- [inference; source: https://www.nature.com/nature/editorial-policies/correction-and-retraction-policy; https://journals.plos.org/plosone/s/corrections-and-retractions; https://authors.bmj.com/policies/correction-retraction-policies/] Across publishers, the practical threshold for a formal correction is not authorship blame or the size of the textual edit; it is whether the change affects interpretation, discoverability, metadata, or the trustworthiness of the record.

#### B. Retraction mechanics

- [fact; source: https://www.nature.com/nature/editorial-policies/correction-and-retraction-policy] Nature retracts an article when the integrity of the published work is substantially undermined by errors in conduct, analysis, reporting, or ethics violations, and the original article remains available with retracted status clearly marked and linked to the retraction statement.
- [fact; source: https://journals.plos.org/plosone/s/corrections-and-retractions] PLOS retracts articles for unresolved integrity, validity, or reliability problems, or for serious policy non-compliance, keeps retracted articles online with retracted status clearly indicated, and treats complete removal as a rare exception where availability itself poses a substantial risk.
- [fact; source: https://authors.bmj.com/policies/correction-retraction-policies/] BMJ replaces the online article with a metadata page plus retraction note, keeps the original text accessible, watermarks the PDF as retracted, and indexes the retraction notice against the original record.
- [fact; source: https://www.nature.com/nature/editorial-policies/correction-and-retraction-policy; https://journals.plos.org/plosone/s/corrections-and-retractions; https://authors.bmj.com/policies/correction-retraction-policies/] All three publisher policies preserve bibliographic discoverability and provide an explicit reasoned notice instead of deleting the record outright, except in narrow legal or safety cases.
- [inference; source: https://www.nature.com/nature/editorial-policies/correction-and-retraction-policy; https://journals.plos.org/plosone/s/corrections-and-retractions; https://authors.bmj.com/policies/correction-retraction-policies/] The retraction pattern is therefore "preserve, mark, explain" rather than "erase and replace," which maps cleanly to git history and weakly to silent file editing.

#### C. Commentary and reply mechanics

- [fact; source: https://www.nature.com/nature/for-authors/matters-arising] Nature treats Matters Arising as formal post-publication commentary on research papers published within the previous 18 months, requires correspondents to contact original authors first, peer reviews the comment, and usually publishes it alongside a Reply from the original authors.
- [fact; source: https://www.nature.com/nature/for-authors/matters-arising] Nature states that Matters Arising and Replies are published online, not in print, and are bidirectionally linked with the original published paper.
- [fact; source: https://journals.plos.org/plosone/s/comments; https://journals.plos.org/plosone/s/corrections-and-retractions] PLOS provides article-attached comments and threaded responses for additions, clarifications, and criticism, requires them to be evidence-based, and explicitly directs authors to comments rather than correction notices for minor issues that do not affect scientific integrity, understanding, or indexing.
- [fact; source: https://info.arxiv.org/help/versions.html] arXiv assigns one identifier to each "Comment" and each "Reply to Comment," and then requires any further discussion to continue through replacement versions under those same identifiers.
- [inference; source: https://www.nature.com/nature/for-authors/matters-arising; https://journals.plos.org/plosone/s/comments; https://info.arxiv.org/help/versions.html] Formal commentary is structurally separate from correction and retraction: it preserves disputation and clarification without silently editing the original record and without forcing every challenge into an invalidation workflow.

#### D. Living reviews

- [fact; source: https://www.cochrane.org/authors/handbooks-and-manuals/handbook/current; https://documentation.cochrane.org/emkb/editorial-manager-for-authors/new-and-returning-authors/update-an-existing-review/decision-frameworkfor-update-proposals] Cochrane treats updating as a distinct governed process, asks whether the review remains a priority area, whether enough new or newly problematic evidence exists to change findings, and whether the review still fits the same question, scope, and methods.
- [fact; source: https://documentation.cochrane.org/emkb/editorial-manager-for-authors/new-and-returning-authors/update-an-existing-review/decision-frameworkfor-update-proposals] Cochrane directs authors to start a new protocol instead of an update when scope changes alter the review question or inclusion criteria materially, when methods need substantive reconsideration, or when an entirely new author team takes over.
- [fact; source: https://resources.cochrane.org/sites/resources.cochrane.org/files/uploads/inline-files/Transform/201912_LSR_Revised_Guidance.pdf] Cochrane living systematic review guidance says living mode is justified when a review question is high priority for decision-making, new evidence is expected to emerge and potentially change conclusions, and the team can commit to continual monitoring and explicit update schedules.
- [fact; source: https://resources.cochrane.org/sites/resources.cochrane.org/files/uploads/inline-files/Transform/201912_LSR_Revised_Guidance.pdf] The same guidance requires readers to be informed about currency through versioned update records such as a "What's New" table and requires the protocol to pre-specify reasons for transition out of living mode when the topic stops meeting living-review criteria.
- [fact; source: https://research.monash.edu/en/publications/the-living-guidelines-handbook-guidance-for-the-production-and-pu/] An official living-guidelines handbook outside Cochrane also treats living mode as conditional on continuing priority, frequent evidence change, and resourcing, which supports the general rule that "living" is a governed operating mode rather than a default state.
- [inference; source: https://documentation.cochrane.org/emkb/editorial-manager-for-authors/new-and-returning-authors/update-an-existing-review/decision-frameworkfor-update-proposals; https://resources.cochrane.org/sites/resources.cochrane.org/files/uploads/inline-files/Transform/201912_LSR_Revised_Guidance.pdf; https://research.monash.edu/en/publications/the-living-guidelines-handbook-guidance-for-the-production-and-pu/] Living review systems preserve continuity only while the question, methods, and governance commitments remain stable; once those change materially, the correct analogue is a new record, not an overwritten one.

#### E. Preprint versioning

- [fact; source: https://info.arxiv.org/help/submit/index.html; https://info.arxiv.org/help/versions.html] arXiv tells authors not to submit a corrected article or erratum as a new paper, but to replace the original submission, and once a paper is public each version becomes a permanent part of the scientific record that may not be removed.
- [fact; source: https://info.arxiv.org/help/versions.html] arXiv increments the version portion of the identifier for replacements and withdrawals, keeps prior versions available in submission history, allows authors to cite specific versions, and explicitly treats annual updates, living reviews, and appended errata as versioned continuations of the same work.
- [fact; source: https://info.arxiv.org/help/versions.html] arXiv also distinguishes comments and replies from ordinary revisions by giving each comment and each reply its own identifier, after which further discussion continues through version history under that identifier.
- [fact; source: https://www.biorxiv.org/about/FAQ] bioRxiv states in its FAQ that a revised manuscript is posted under the same Digital Object Identifier (DOI) and that the original version remains accessible in the Info or History tab on the article page.
- [inference; source: https://info.arxiv.org/help/versions.html; https://www.biorxiv.org/about/FAQ] The preprint pattern is "stable public identifier plus visible version chain," which makes it a strong analogue for immutable completed notes that still need a controlled way to absorb corrections or periodic updates.

#### F. Minimal viable analogue for this repository

- [inference; source: https://www.nature.com/nature/editorial-policies/correction-and-retraction-policy; https://journals.plos.org/plosone/s/corrections-and-retractions; https://authors.bmj.com/policies/correction-retraction-policies/; https://info.arxiv.org/help/versions.html] The smallest viable model for this repository is not journal-style full republication infrastructure; it is an immutable original item plus a linked amendment record, because all sampled systems preserve the original record and attach the change as an explicit, separately discoverable notice or version.
- [inference; source: https://www.nature.com/nature/editorial-policies/correction-and-retraction-policy; https://authors.bmj.com/policies/correction-retraction-policies/] The original completed item needs only three new structured fields to expose reader-facing state: `record_status`, `version_of_record`, meaning the canonical published instance that later notices amend, and `amendments`.
- [inference; source: https://www.nature.com/nature/for-authors/matters-arising; https://documentation.cochrane.org/emkb/editorial-manager-for-authors/new-and-returning-authors/update-an-existing-review/decision-frameworkfor-update-proposals; https://info.arxiv.org/help/versions.html] Each amendment item needs the minimum structured data required to say what it is, what original record it targets, which committed version it evaluates, and whether it corrects, retracts, comments on, replies to, or updates that target.
- [inference; source: https://journals.plos.org/plosone/s/corrections-and-retractions; https://authors.bmj.com/policies/correction-retraction-policies/] The three silent-edit exceptions should be exactly: broken-URL repair where the cited source identity does not change, tag updates that do not alter interpretation, and citation-URL normalization that improves access to the same cited source without changing the claim.
- [inference; source: https://documentation.cochrane.org/emkb/editorial-manager-for-authors/new-and-returning-authors/update-an-existing-review/decision-frameworkfor-update-proposals; https://resources.cochrane.org/sites/resources.cochrane.org/files/uploads/inline-files/Transform/201912_LSR_Revised_Guidance.pdf] Standard completed research items should default to correction, commentary, or retraction notices; living-update behavior should be opt-in and reserved for items explicitly designated as living syntheses whose question and method are expected to remain stable across updates.
- [assumption; source: https://davidamitchell.github.io/Research/research/2026-04-22-knowledge-curation-governance-for-regulated-ai.html] A git commit hash is a sufficient local stand-in for a canonical version-of-record identifier because this corpus is private and git already preserves immutable version lineage at commit granularity.

### §3 Reasoning

- [inference; source: https://www.nature.com/nature/editorial-policies/correction-and-retraction-policy; https://journals.plos.org/plosone/s/corrections-and-retractions; https://authors.bmj.com/policies/correction-retraction-policies/] The core invariant across publisher policies is that post-publication governance protects the reader's ability to reconstruct what changed, why it changed, and how the prior record should now be interpreted.
- [inference; source: https://www.nature.com/nature/for-authors/matters-arising; https://journals.plos.org/plosone/s/comments; https://info.arxiv.org/help/versions.html] Commentary, correction, and retraction solve different problems, so collapsing them into one "edit completed file" mechanism would destroy useful distinctions between challenge, clarification, and invalidation.
- [inference; source: https://documentation.cochrane.org/emkb/editorial-manager-for-authors/new-and-returning-authors/update-an-existing-review/decision-frameworkfor-update-proposals; https://resources.cochrane.org/sites/resources.cochrane.org/files/uploads/inline-files/Transform/201912_LSR_Revised_Guidance.pdf; https://info.arxiv.org/help/versions.html] Living updates are governance-heavy and should therefore be exceptional in this repository; they fit recurring syntheses, but not ordinary completed notes whose main value is that they capture a dated conclusion.
- [inference; source: https://authors.bmj.com/policies/correction-retraction-policies/; https://info.arxiv.org/help/versions.html] A commit-linked amendment file can reproduce the essential information architecture of journal notices and preprint version chains without needing a database, a redirect system, or a separate index service.
- [inference; source: https://info.arxiv.org/help/versions.html; https://www.biorxiv.org/about/FAQ; https://authors.bmj.com/policies/correction-retraction-policies/] A pure git or arXiv-style in-place version chain with visible history is a credible alternative design, but it is not the minimal analogue for this repository because arXiv, bioRxiv, and BMJ pair that model with reader-facing version-history surfaces that this corpus does not yet expose.

### §4 Consistency Check

- [fact; source: https://www.nature.com/nature/editorial-policies/correction-and-retraction-policy; https://journals.plos.org/plosone/s/corrections-and-retractions; https://authors.bmj.com/policies/correction-retraction-policies/] No examined publisher policy supported silent substantive edits to the version of record after publication without a linked amendment notice.
- [fact; source: https://documentation.cochrane.org/emkb/editorial-manager-for-authors/new-and-returning-authors/update-an-existing-review/decision-frameworkfor-update-proposals; https://resources.cochrane.org/sites/resources.cochrane.org/files/uploads/inline-files/Transform/201912_LSR_Revised_Guidance.pdf] No examined living-review policy treated major scope or method drift as an ordinary update; the supported pattern was new protocol, new review, or transition out of living mode.
- [fact; source: https://info.arxiv.org/help/versions.html; https://www.biorxiv.org/about/FAQ] The preprint evidence was internally consistent: revisions preserve history, stable public identity remains, and reader-visible version history does the interpretive work that silent overwrites would otherwise erase.
- [inference; source: https://www.nature.com/nature/editorial-policies/correction-and-retraction-policy; https://info.arxiv.org/help/versions.html] The recommended git analogue therefore remains consistent with both journal and preprint practice: preserve the old record, surface the new state, and never make readers infer change from absent evidence.

### §5 Depth and Breadth Expansion

- [fact; source: https://davidamitchell.github.io/Research/research/2026-04-22-knowledge-curation-governance-for-regulated-ai.html] The governance lens matters because the repository is not only storing notes; it is managing an authoritative knowledge object whose downstream consumers need provenance, replayability, and correction-to-source lineage.
- [fact; source: https://journals.plos.org/plosone/s/corrections-and-retractions; https://authors.bmj.com/policies/correction-retraction-policies/] The behavioral lens matters because publishers explicitly reject minor change churn after publication, which prevents the version of record from turning into a rolling scratchpad and preserves shared reference points for readers.
- [fact; source: https://resources.cochrane.org/sites/resources.cochrane.org/files/uploads/inline-files/Transform/201912_LSR_Revised_Guidance.pdf; https://research.monash.edu/en/publications/the-living-guidelines-handbook-guidance-for-the-production-and-pu/] The operational lens matters because living mode consumes ongoing monitoring and editorial capacity, so making all completed items implicitly living would create hidden maintenance debt for the repository.
- [fact; source: https://info.arxiv.org/help/versions.html; https://authors.bmj.com/policies/correction-retraction-policies/] The technical lens matters because git already supplies immutable version history, but readers still need a human-legible notice layer that says which commit is the version of record and which later files reinterpret it.
- [inference; source: https://www.nature.com/nature/for-authors/matters-arising; https://journals.plos.org/plosone/s/comments; https://documentation.cochrane.org/emkb/editorial-manager-for-authors/new-and-returning-authors/update-an-existing-review/decision-frameworkfor-update-proposals] The cleanest repository design is therefore plural rather than singular: one path for correction, one for commentary, one for retraction, and one opt-in path for living updates.

### §6 Synthesis

*(This section seeds the Findings below.)*

**Executive summary:**

- [inference; source: https://www.nature.com/nature/editorial-policies/correction-and-retraction-policy; https://journals.plos.org/plosone/s/corrections-and-retractions; https://authors.bmj.com/policies/correction-retraction-policies/; https://info.arxiv.org/help/versions.html] The best-supported minimal analogue is an immutable completed item plus a separate amendment file, with the original item retaining only reader-signal metadata such as status, originating commit, and linked notices.
- [fact; source: https://www.nature.com/nature/editorial-policies/correction-and-retraction-policy; https://journals.plos.org/plosone/s/corrections-and-retractions; https://authors.bmj.com/policies/correction-retraction-policies/] Journal publishers consistently treat substantive post-publication change as a formal notice problem, not as a silent editing problem: corrections, retractions, and expressions of concern are separately published, linked, and indexed against the original record.
- [fact; source: https://www.nature.com/nature/for-authors/matters-arising; https://info.arxiv.org/help/versions.html] Formal challenge and reply are separate objects from correction, which means the repository should support commentary without forcing every dispute into either overwrite or invalidation.
- [fact; source: https://documentation.cochrane.org/emkb/editorial-manager-for-authors/new-and-returning-authors/update-an-existing-review/decision-frameworkfor-update-proposals; https://resources.cochrane.org/sites/resources.cochrane.org/files/uploads/inline-files/Transform/201912_LSR_Revised_Guidance.pdf; https://www.biorxiv.org/about/FAQ] Living-update behavior should be opt-in rather than default because mature systems only preserve one evolving record while the question and method remain stable and the version history remains visible.

**Key findings:**

- 1. [fact; source: https://www.nature.com/nature/editorial-policies/correction-and-retraction-policy; https://journals.plos.org/plosone/s/corrections-and-retractions; https://authors.bmj.com/policies/correction-retraction-policies/] Major publishers preserve the published record and attach a separately published notice when interpretation, metadata, or trustworthiness changes, which means substantive amendment is modeled as linked record-keeping rather than as silent overwrite. **Confidence: high**
- 2. [fact; source: https://journals.plos.org/plosone/s/corrections-and-retractions; https://authors.bmj.com/policies/correction-retraction-policies/] The practical threshold for a formal correction is effect on understanding, indexing, or scientific integrity, while typographical cleanup and other low-impact issues are usually rejected or diverted into lightweight comment channels. **Confidence: high**
- 3. [fact; source: https://www.nature.com/nature/editorial-policies/correction-and-retraction-policy; https://journals.plos.org/plosone/s/corrections-and-retractions; https://authors.bmj.com/policies/correction-retraction-policies/] Retraction systems are designed to preserve discoverability while clearly marking unreliability, because readers need both the reason for invalidation and access to the prior record for auditability and scholarly traceability. **Confidence: high**
- 4. [fact; source: https://www.nature.com/nature/for-authors/matters-arising; https://journals.plos.org/plosone/s/comments; https://info.arxiv.org/help/versions.html] Post-publication commentary is a distinct mechanism from correction or retraction, because challenge and reply preserve debate and clarification without rewriting the original or declaring it invalid. **Confidence: high**
- 5. [fact; source: https://documentation.cochrane.org/emkb/editorial-manager-for-authors/new-and-returning-authors/update-an-existing-review/decision-frameworkfor-update-proposals; https://resources.cochrane.org/sites/resources.cochrane.org/files/uploads/inline-files/Transform/201912_LSR_Revised_Guidance.pdf; https://research.monash.edu/en/publications/the-living-guidelines-handbook-guidance-for-the-production-and-pu/] Living-review systems only keep updating the same record while the question remains stable, decision-relevant, and operationally funded, and they switch to a new protocol or leave living mode when scope or method drift becomes material. **Confidence: high**
- 6. [fact; source: https://info.arxiv.org/help/submit/index.html; https://info.arxiv.org/help/versions.html; https://www.biorxiv.org/about/FAQ] Preprint platforms treat revision as a stable-identifier, visible-version-history problem, which shows that history-preserving updates can work without replacing the original public object or fragmenting it into unrelated records. **Confidence: high**
- 7. [inference; source: https://www.nature.com/nature/editorial-policies/correction-and-retraction-policy; https://authors.bmj.com/policies/correction-retraction-policies/; https://info.arxiv.org/help/versions.html] For this repository, the minimum frontmatter on the original completed item is `record_status`, `version_of_record`, and `amendments`, because those three fields are enough to tell readers the current interpretive state, the commit being amended, and where to find the notices. **Confidence: medium**
- 8. [inference; source: https://journals.plos.org/plosone/s/corrections-and-retractions; https://authors.bmj.com/policies/correction-retraction-policies/; https://documentation.cochrane.org/emkb/editorial-manager-for-authors/new-and-returning-authors/update-an-existing-review/decision-frameworkfor-update-proposals] The only silent post-completion edits that fit the publisher evidence are broken-URL repair, tag updates, and citation-URL normalization, because each can improve access or classification without changing the interpretive content of the record. **Confidence: medium**

**Evidence map:**

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [fact] Publishers preserve the original record and attach linked amendment notices for substantive change. | [Nature policy](https://www.nature.com/nature/editorial-policies/correction-and-retraction-policy); [PLOS policy](https://journals.plos.org/plosone/s/corrections-and-retractions); [BMJ policy](https://authors.bmj.com/policies/correction-retraction-policies/) | high | Cross-publisher convergence |
| [fact] Correction threshold is impact on interpretation, indexing, or integrity, not trivial wording cleanup. | [PLOS policy](https://journals.plos.org/plosone/s/corrections-and-retractions); [BMJ policy](https://authors.bmj.com/policies/correction-retraction-policies/) | high | Minor issues diverted or rejected |
| [fact] Retraction preserves discoverability while marking unreliability and publishing reasons. | [Nature policy](https://www.nature.com/nature/editorial-policies/correction-and-retraction-policy); [PLOS policy](https://journals.plos.org/plosone/s/corrections-and-retractions); [BMJ policy](https://authors.bmj.com/policies/correction-retraction-policies/) | high | Removal is exceptional |
| [fact] Commentary and reply are separate from correction and retraction. | [Nature Matters Arising](https://www.nature.com/nature/for-authors/matters-arising); [PLOS comments](https://journals.plos.org/plosone/s/comments); [arXiv versions](https://info.arxiv.org/help/versions.html) | high | Debate path, not invalidation path |
| [fact] Living mode continues only while question, priority, and methods remain stable enough to justify one evolving record. | [Cochrane update framework](https://documentation.cochrane.org/emkb/editorial-manager-for-authors/new-and-returning-authors/update-an-existing-review/decision-frameworkfor-update-proposals); [Cochrane living-review guidance](https://resources.cochrane.org/sites/resources.cochrane.org/files/uploads/inline-files/Transform/201912_LSR_Revised_Guidance.pdf); [Living Guidelines Handbook](https://research.monash.edu/en/publications/the-living-guidelines-handbook-guidance-for-the-production-and-pu/) | high | New protocol when drift becomes material |
| [fact] Preprint revision preserves stable identity and visible version history. | [arXiv submission guidance](https://info.arxiv.org/help/submit/index.html); [arXiv versions](https://info.arxiv.org/help/versions.html); [bioRxiv FAQ](https://www.biorxiv.org/about/FAQ) | high | Revision, withdrawal, and comment all keep history visible |
| [inference] Original completed items need `record_status`, `version_of_record`, and `amendments` as minimum structured metadata. | [Nature policy](https://www.nature.com/nature/editorial-policies/correction-and-retraction-policy); [BMJ policy](https://authors.bmj.com/policies/correction-retraction-policies/); [arXiv versions](https://info.arxiv.org/help/versions.html); [Knowledge curation governance](https://davidamitchell.github.io/Research/research/2026-04-22-knowledge-curation-governance-for-regulated-ai.html) | medium | Minimal reader-signal set |
| [inference] Only broken-URL repair, tag updates, and citation-URL normalization should remain silent. | [PLOS policy](https://journals.plos.org/plosone/s/corrections-and-retractions); [BMJ policy](https://authors.bmj.com/policies/correction-retraction-policies/); [Cochrane update framework](https://documentation.cochrane.org/emkb/editorial-manager-for-authors/new-and-returning-authors/update-an-existing-review/decision-frameworkfor-update-proposals) | medium | Access or classification only |

**Assumptions:**

- [assumption; source: https://davidamitchell.github.io/Research/research/2026-04-22-knowledge-curation-governance-for-regulated-ai.html] A git commit hash can stand in for a canonical version-of-record identifier because this repository already treats git history as the authoritative provenance layer.
- [assumption; source: https://www.nature.com/nature/editorial-policies/correction-and-retraction-policy; https://authors.bmj.com/policies/correction-retraction-policies/] Updating a completed item's frontmatter to expose `record_status` and `amendments` is acceptable if the same commit also adds the formal amendment file, so the metadata change is reader-visible rather than silent.

**Analysis:**

- [inference; source: https://www.nature.com/nature/editorial-policies/correction-and-retraction-policy; https://journals.plos.org/plosone/s/corrections-and-retractions; https://authors.bmj.com/policies/correction-retraction-policies/] The strongest evidence came from publisher policies because they make the record-governance rules explicit, and those policies converged on the same design choice: preserve the original, publish a notice, and signal the amended state to readers.
- [inference; source: https://www.nature.com/nature/for-authors/matters-arising; https://journals.plos.org/plosone/s/comments; https://info.arxiv.org/help/versions.html] Commentary was weighed separately from correction because the sources treat disagreement and clarification as discourse objects, not necessarily as defects in the original record.
- [inference; source: https://documentation.cochrane.org/emkb/editorial-manager-for-authors/new-and-returning-authors/update-an-existing-review/decision-frameworkfor-update-proposals; https://resources.cochrane.org/sites/resources.cochrane.org/files/uploads/inline-files/Transform/201912_LSR_Revised_Guidance.pdf; https://info.arxiv.org/help/versions.html] Living-review and preprint evidence mattered because they show two different ways to keep one logical work alive over time without erasing history, but both demand visible version lineage and explicit stopping rules.
- [inference; source: https://davidamitchell.github.io/Research/research/2026-04-22-knowledge-curation-governance-for-regulated-ai.html; https://davidamitchell.github.io/Research/research/2026-03-02-agent-memory-management-context-injection.html] The repository analogue was then narrowed by local constraints: unlike journals, this corpus already has immutable git history, so the missing layer is not archival storage but the human-readable notice and linkage model that tells readers how to interpret later changes.
- [inference; source: https://www.nature.com/nature/editorial-policies/correction-and-retraction-policy; https://authors.bmj.com/policies/correction-retraction-policies/; https://info.arxiv.org/help/versions.html] **Recommended original-item frontmatter schema:** the minimal original-record metadata is:

```yaml
record_status: active        # active | corrected | commented | retracted | living
version_of_record: <commit-sha>
amendments: []
```

- [inference; source: https://www.nature.com/nature/for-authors/matters-arising; https://documentation.cochrane.org/emkb/editorial-manager-for-authors/new-and-returning-authors/update-an-existing-review/decision-frameworkfor-update-proposals; https://info.arxiv.org/help/versions.html] **Recommended amendment-item frontmatter schema:** the minimal amendment metadata is:

```yaml
title: "<human-readable amendment title>"
added: <iso-8601 timestamp>
status: completed
priority: medium
tags: [amendment]
amends: <original-item-slug>
amendment_type: correction   # correction | commentary | reply | retraction | living-update
target_version: <commit-sha>
impact: scoped               # metadata-only | scoped | invalidates
```

- [inference; source: https://info.arxiv.org/help/versions.html; https://authors.bmj.com/policies/correction-retraction-policies/] **Recommended file naming convention and template:** amendment files should use `YYYY-MM-DD-<original-slug>-<amendment-type>.md` and contain the sections `## Summary`, `## Trigger`, `## What Changed`, `## Impact on Findings`, `## Evidence`, and `## Reader Action`, because that is the smallest structure that preserves reason, scope, evidence, and downstream interpretation.

**Risks, gaps, uncertainties:**

- [fact; source: https://journals.plos.org/plosone/s/corrections-and-retractions; https://www.nature.com/nature/editorial-policies/correction-and-retraction-policy] Direct COPE text is not quoted in this section, so COPE-aligned conclusions rest on publisher policies that cite or implement COPE rather than on direct quotation from COPE itself.
- [fact; source: https://www.biorxiv.org/about/FAQ] The bioRxiv evidence in this section is limited to the revision rule stated in the Frequently Asked Questions (FAQ), so it supports the stable-identifier claim but not a broader reconstruction of bioRxiv's full versioning model.
- [fact; source: https://research.monash.edu/en/publications/the-living-guidelines-handbook-guidance-for-the-production-and-pu/] The non-Cochrane living-guidance evidence was lighter than the Cochrane evidence, so cross-platform claims about stopping criteria outside Cochrane should be treated as corroborative rather than definitive.
- [inference; source: https://info.arxiv.org/help/versions.html; https://authors.bmj.com/policies/correction-retraction-policies/] The repository still needs an implementation choice on where reader-facing banners should render: in frontmatter-driven site generation, in amendment files only, or in both.

**Open questions:**

- [inference; source: https://resources.cochrane.org/sites/resources.cochrane.org/files/uploads/inline-files/Transform/201912_LSR_Revised_Guidance.pdf; https://info.arxiv.org/help/versions.html] Should the repository support a distinct `living` class of research item now, or should it first implement only correction, commentary, and retraction notices and add living mode later when a real use case appears?
- [inference; source: https://www.nature.com/nature/for-authors/matters-arising; https://journals.plos.org/plosone/s/comments] Should formal commentary in this repository require an author reply path, or is one-way comment linkage sufficient for the first implementation?
- [inference; source: https://authors.bmj.com/policies/correction-retraction-policies/; https://info.arxiv.org/help/versions.html] Should `version_of_record` capture only the completion commit hash, or also store the path and date of the completing commit to simplify later rendering and audits?

### §7 Recursive Review

- [fact; source: https://www.nature.com/nature/editorial-policies/correction-and-retraction-policy; https://journals.plos.org/plosone/s/corrections-and-retractions; https://authors.bmj.com/policies/correction-retraction-policies/; https://info.arxiv.org/help/versions.html] Visible claims in sections 0 through 6 were checked for inline labels and URL-backed support, and the strongest conclusions remain limited to patterns corroborated by multiple primary policies.
- [fact; source: https://www.nature.com/nature/for-authors/matters-arising; https://journals.plos.org/plosone/s/comments; https://documentation.cochrane.org/emkb/editorial-manager-for-authors/new-and-returning-authors/update-an-existing-review/decision-frameworkfor-update-proposals] The synthesis maintains the necessary distinctions between correction, commentary, retraction, and living update, so the recommended repository mechanism does not collapse separate governance problems into one edit path.
- [fact; source: https://davidamitchell.github.io/Research/research/2026-04-22-knowledge-curation-governance-for-regulated-ai.html; https://davidamitchell.github.io/Research/research/2026-03-02-agent-memory-management-context-injection.html] The repository cross-reference sweep did not reveal a contradictory completed item; instead, the adjacent governance items strengthened the need for provenance-preserving amendment records.
- [inference; source: https://www.biorxiv.org/about/FAQ; https://research.monash.edu/en/publications/the-living-guidelines-handbook-guidance-for-the-production-and-pu/] Remaining uncertainty is concentrated in two thinner evidence areas, bioRxiv page access and non-Cochrane living-guideline detail, so claims depending on them were kept at medium rather than high confidence when they influenced design choices.

---

## Findings

### Executive Summary

[inference; source: https://www.nature.com/nature/editorial-policies/correction-and-retraction-policy; https://journals.plos.org/plosone/s/corrections-and-retractions; https://authors.bmj.com/policies/correction-retraction-policies/; https://info.arxiv.org/help/versions.html] The strongest minimal analogue for this repository is an immutable completed item plus a separate amendment file, with the original item carrying only reader-signal metadata such as status, originating commit, and linked notices.

[fact; source: https://www.nature.com/nature/editorial-policies/correction-and-retraction-policy; https://journals.plos.org/plosone/s/corrections-and-retractions; https://authors.bmj.com/policies/correction-retraction-policies/] Journal publishers consistently treat substantive post-publication change as a formal notice problem rather than a silent editing problem, because they preserve the original record and publish linked notices for correction, concern, or retraction.

[fact; source: https://www.nature.com/nature/for-authors/matters-arising; https://info.arxiv.org/help/versions.html] Formal challenge and reply are separate objects from correction, which means the repository should support commentary without forcing every dispute into either overwrite or invalidation.

[fact; source: https://documentation.cochrane.org/emkb/editorial-manager-for-authors/new-and-returning-authors/update-an-existing-review/decision-frameworkfor-update-proposals; https://resources.cochrane.org/sites/resources.cochrane.org/files/uploads/inline-files/Transform/201912_LSR_Revised_Guidance.pdf; https://www.biorxiv.org/about/FAQ] Living-update behavior should be opt-in rather than default, because mature systems keep one evolving record only while the question and method remain stable and the version history remains visible.

[inference; source: https://info.arxiv.org/help/versions.html; https://www.biorxiv.org/about/FAQ; https://authors.bmj.com/policies/correction-retraction-policies/] A pure in-place version chain remains a plausible later design, but it would stop being "minimal" here because it also needs reader-facing version-history surfaces comparable to arXiv submission history or BMJ previous-version notices.

### Key Findings

1. [fact; source: https://www.nature.com/nature/editorial-policies/correction-and-retraction-policy; https://journals.plos.org/plosone/s/corrections-and-retractions; https://authors.bmj.com/policies/correction-retraction-policies/] Major publishers preserve the published record and attach a separately published notice when interpretation, metadata, or trustworthiness changes, which means substantive amendment is modeled as linked record-keeping rather than as silent overwrite. **Confidence: high**
2. [fact; source: https://journals.plos.org/plosone/s/corrections-and-retractions; https://authors.bmj.com/policies/correction-retraction-policies/] The practical threshold for a formal correction is effect on understanding, indexing, or scientific integrity, while typographical cleanup and other low-impact issues are usually rejected or diverted into lightweight comment channels. **Confidence: high**
3. [fact; source: https://www.nature.com/nature/editorial-policies/correction-and-retraction-policy; https://journals.plos.org/plosone/s/corrections-and-retractions; https://authors.bmj.com/policies/correction-retraction-policies/] Retraction systems are designed to preserve discoverability while clearly marking unreliability, because readers need both the reason for invalidation and access to the prior record for auditability and scholarly traceability. **Confidence: high**
4. [fact; source: https://www.nature.com/nature/for-authors/matters-arising; https://journals.plos.org/plosone/s/comments; https://info.arxiv.org/help/versions.html] Post-publication commentary is a distinct mechanism from correction or retraction, because challenge and reply preserve debate and clarification without rewriting the original or declaring it invalid. **Confidence: high**
5. [fact; source: https://documentation.cochrane.org/emkb/editorial-manager-for-authors/new-and-returning-authors/update-an-existing-review/decision-frameworkfor-update-proposals; https://resources.cochrane.org/sites/resources.cochrane.org/files/uploads/inline-files/Transform/201912_LSR_Revised_Guidance.pdf; https://research.monash.edu/en/publications/the-living-guidelines-handbook-guidance-for-the-production-and-pu/] Living-review systems only keep updating the same record while the question remains stable, decision-relevant, and operationally funded, and they switch to a new protocol or leave living mode when scope or method drift becomes material. **Confidence: high**
6. [fact; source: https://info.arxiv.org/help/submit/index.html; https://info.arxiv.org/help/versions.html; https://www.biorxiv.org/about/FAQ] Preprint platforms treat revision as a stable-identifier, visible-version-history problem, which shows that history-preserving updates can work without replacing the original public object or fragmenting it into unrelated records. **Confidence: high**
7. [inference; source: https://www.nature.com/nature/editorial-policies/correction-and-retraction-policy; https://authors.bmj.com/policies/correction-retraction-policies/; https://info.arxiv.org/help/versions.html] For this repository, the minimum frontmatter on the original completed item is `record_status`, `version_of_record`, meaning the canonical published instance that later notices amend, and `amendments`, because those three fields are enough to tell readers the current interpretive state, the commit being amended, and where to find the notices. **Confidence: medium**
8. [inference; source: https://journals.plos.org/plosone/s/corrections-and-retractions; https://authors.bmj.com/policies/correction-retraction-policies/; https://documentation.cochrane.org/emkb/editorial-manager-for-authors/new-and-returning-authors/update-an-existing-review/decision-frameworkfor-update-proposals] The only silent post-completion edits that fit the publisher evidence are broken-URL repair, tag updates, and citation-URL normalization, because each can improve access or classification without changing the interpretive content of the record. **Confidence: medium**

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [fact] Publishers preserve the original record and attach linked amendment notices for substantive change. | [Nature policy](https://www.nature.com/nature/editorial-policies/correction-and-retraction-policy); [PLOS policy](https://journals.plos.org/plosone/s/corrections-and-retractions); [BMJ policy](https://authors.bmj.com/policies/correction-retraction-policies/) | high | Cross-publisher convergence |
| [fact] Correction threshold is impact on interpretation, indexing, or integrity, not trivial wording cleanup. | [PLOS policy](https://journals.plos.org/plosone/s/corrections-and-retractions); [BMJ policy](https://authors.bmj.com/policies/correction-retraction-policies/) | high | Minor issues diverted or rejected |
| [fact] Retraction preserves discoverability while marking unreliability and publishing reasons. | [Nature policy](https://www.nature.com/nature/editorial-policies/correction-and-retraction-policy); [PLOS policy](https://journals.plos.org/plosone/s/corrections-and-retractions); [BMJ policy](https://authors.bmj.com/policies/correction-retraction-policies/) | high | Removal is exceptional |
| [fact] Commentary and reply are separate from correction and retraction. | [Nature Matters Arising](https://www.nature.com/nature/for-authors/matters-arising); [PLOS comments](https://journals.plos.org/plosone/s/comments); [arXiv versions](https://info.arxiv.org/help/versions.html) | high | Debate path, not invalidation path |
| [fact] Living mode continues only while question, priority, and methods remain stable enough to justify one evolving record. | [Cochrane update framework](https://documentation.cochrane.org/emkb/editorial-manager-for-authors/new-and-returning-authors/update-an-existing-review/decision-frameworkfor-update-proposals); [Cochrane living-review guidance](https://resources.cochrane.org/sites/resources.cochrane.org/files/uploads/inline-files/Transform/201912_LSR_Revised_Guidance.pdf); [Living Guidelines Handbook](https://research.monash.edu/en/publications/the-living-guidelines-handbook-guidance-for-the-production-and-pu/) | high | New protocol when drift becomes material |
| [fact] Preprint revision preserves stable identity and visible version history. | [arXiv submission guidance](https://info.arxiv.org/help/submit/index.html); [arXiv versions](https://info.arxiv.org/help/versions.html); [bioRxiv FAQ](https://www.biorxiv.org/about/FAQ) | high | Revision, withdrawal, and comment all keep history visible |
| [inference] Original completed items need `record_status`, `version_of_record`, and `amendments` as minimum structured metadata. | [Nature policy](https://www.nature.com/nature/editorial-policies/correction-and-retraction-policy); [BMJ policy](https://authors.bmj.com/policies/correction-retraction-policies/); [arXiv versions](https://info.arxiv.org/help/versions.html); [Knowledge curation governance](https://davidamitchell.github.io/Research/research/2026-04-22-knowledge-curation-governance-for-regulated-ai.html) | medium | Minimal reader-signal set |
| [inference] Only broken-URL repair, tag updates, and citation-URL normalization should remain silent. | [PLOS policy](https://journals.plos.org/plosone/s/corrections-and-retractions); [BMJ policy](https://authors.bmj.com/policies/correction-retraction-policies/); [Cochrane update framework](https://documentation.cochrane.org/emkb/editorial-manager-for-authors/new-and-returning-authors/update-an-existing-review/decision-frameworkfor-update-proposals) | medium | Access or classification only |

### Assumptions

- [assumption; source: https://davidamitchell.github.io/Research/research/2026-04-22-knowledge-curation-governance-for-regulated-ai.html] **Assumption:** a git commit hash can stand in for a canonical version-of-record identifier. **Justification:** this repository already treats git history as the authoritative provenance layer, so the missing mechanism is reader-facing notice and linkage rather than immutable storage.
- [assumption; source: https://www.nature.com/nature/editorial-policies/correction-and-retraction-policy; https://authors.bmj.com/policies/correction-retraction-policies/] **Assumption:** updating a completed item's frontmatter to expose `record_status` and `amendments` is acceptable if the same commit also adds the amendment file. **Justification:** publisher systems update reader-facing status on the original record while preserving the original content, and the same pattern can be reproduced here without silent content rewrite.

### Analysis

[inference; source: https://www.nature.com/nature/editorial-policies/correction-and-retraction-policy; https://journals.plos.org/plosone/s/corrections-and-retractions; https://authors.bmj.com/policies/correction-retraction-policies/] The decisive evidence came from publisher policies because they make the post-publication control model explicit, and those policies converged on the same rule: preserve the original, publish a notice, and signal the amended state to readers.

[inference; source: https://www.nature.com/nature/for-authors/matters-arising; https://journals.plos.org/plosone/s/comments; https://info.arxiv.org/help/versions.html] Commentary was kept separate from correction because the sources consistently frame disagreement and clarification as discourse objects, not necessarily as defects in the original record.

[inference; source: https://documentation.cochrane.org/emkb/editorial-manager-for-authors/new-and-returning-authors/update-an-existing-review/decision-frameworkfor-update-proposals; https://resources.cochrane.org/sites/resources.cochrane.org/files/uploads/inline-files/Transform/201912_LSR_Revised_Guidance.pdf; https://info.arxiv.org/help/versions.html] Living-review and preprint evidence mattered because both show how one logical work can evolve over time without erasing history, but both also impose visible version lineage and explicit stopping rules.

[inference; source: https://davidamitchell.github.io/Research/research/2026-04-22-knowledge-curation-governance-for-regulated-ai.html; https://davidamitchell.github.io/Research/research/2026-03-02-agent-memory-management-context-injection.html] The local design choice was then narrowed by repository context: git already solves archival immutability, so the required analogue is a notice-and-linkage layer that tells readers which commit is the canonical version of record and how later files reinterpret it.

[inference; source: https://info.arxiv.org/help/versions.html; https://www.biorxiv.org/about/FAQ; https://authors.bmj.com/policies/correction-retraction-policies/] A pure git or arXiv-style in-place version chain with visible history remains a credible later design, but it is not the minimal analogue for this repository because arXiv, bioRxiv, and BMJ pair that model with reader-facing version-history surfaces that this corpus does not yet expose.

[inference; source: https://www.nature.com/nature/editorial-policies/correction-and-retraction-policy; https://authors.bmj.com/policies/correction-retraction-policies/; https://info.arxiv.org/help/versions.html] **Recommended original-item frontmatter schema:** the minimal original-record metadata is:

```yaml
record_status: active        # active | corrected | commented | retracted | living
version_of_record: <commit-sha>
amendments: []
```

[inference; source: https://www.nature.com/nature/for-authors/matters-arising; https://documentation.cochrane.org/emkb/editorial-manager-for-authors/new-and-returning-authors/update-an-existing-review/decision-frameworkfor-update-proposals; https://info.arxiv.org/help/versions.html] **Recommended amendment-item frontmatter schema:** the minimal amendment metadata is:

```yaml
title: "<human-readable amendment title>"
added: <iso-8601 timestamp>
status: completed
priority: medium
tags: [amendment]
amends: <original-item-slug>
amendment_type: correction   # correction | commentary | reply | retraction | living-update
target_version: <commit-sha>
impact: scoped               # metadata-only | scoped | invalidates
```

[inference; source: https://info.arxiv.org/help/versions.html; https://authors.bmj.com/policies/correction-retraction-policies/] **Recommended file naming convention and template:** amendment files should use `YYYY-MM-DD-<original-slug>-<amendment-type>.md` and contain the sections `## Summary`, `## Trigger`, `## What Changed`, `## Impact on Findings`, `## Evidence`, and `## Reader Action`, because that is the smallest structure that preserves reason, scope, evidence, and downstream interpretation.

### Risks, Gaps, and Uncertainties

- [fact; source: https://journals.plos.org/plosone/s/corrections-and-retractions; https://www.nature.com/nature/editorial-policies/correction-and-retraction-policy] Direct COPE text is not quoted in this item, so COPE-aligned conclusions are supported indirectly through accessible publisher policies rather than by direct quotation from COPE.
- [fact; source: https://www.biorxiv.org/about/FAQ] The bioRxiv evidence in this item is limited to the revision rule stated in the Frequently Asked Questions (FAQ), so it supports the stable-identifier claim but not a broader reconstruction of bioRxiv's full versioning model.
- [fact; source: https://research.monash.edu/en/publications/the-living-guidelines-handbook-guidance-for-the-production-and-pu/] The non-Cochrane living-guidance evidence was thinner than the Cochrane evidence, so the external corroboration for stop-or-continue criteria should be treated as supportive rather than decisive.
- [inference; source: https://authors.bmj.com/policies/correction-retraction-policies/; https://info.arxiv.org/help/versions.html] The implementation question that remains open is how the site should render amendment banners or notice blocks so readers see current status without opening a second file first.

### Open Questions

- [inference; source: https://resources.cochrane.org/sites/resources.cochrane.org/files/uploads/inline-files/Transform/201912_LSR_Revised_Guidance.pdf; https://info.arxiv.org/help/versions.html] Should the repository support an explicit `living` class of research item now, or should it first implement only correction, commentary, and retraction notices and add living mode later when a concrete use case appears?
- [inference; source: https://www.nature.com/nature/for-authors/matters-arising; https://journals.plos.org/plosone/s/comments] Should formal commentary in this repository require a reply path from the original author, or is one-way comment linkage sufficient for the first implementation?
- [inference; source: https://authors.bmj.com/policies/correction-retraction-policies/; https://info.arxiv.org/help/versions.html] Should `version_of_record` store only the completion commit hash, or also store the completion date and original path to simplify future rendering and audits?

---

## Output

- Type: knowledge
- Description: Amendment schema recommendation and item-template recommendation for immutable completed research items, including silent-edit thresholds and linked-notice mechanics.
- Links:
  - [Nature - Corrections, Retractions and Matters Arising](https://www.nature.com/nature/editorial-policies/correction-and-retraction-policy)
  - [arXiv - Submission Version Availability](https://info.arxiv.org/help/versions.html)
  - [Cochrane decision framework for update proposals](https://documentation.cochrane.org/emkb/editorial-manager-for-authors/new-and-returning-authors/update-an-existing-review/decision-frameworkfor-update-proposals)
