# 2026-05-31 -- Research: commit-trends-repo-velocity-rework-abandonment

**Item:** `Research/completed/2026-05-29-commit-trends-repo-velocity-rework-abandonment.md`

**Completed:**
- Moved item from `backlog` to `in-progress` (pre-staged by workflow)
- Read research question: what longitudinal studies (2019-2026) show about directional shifts across seven metrics: repository creation rate, lines-of-code (LOC) velocity, rework share, project abandonment, AI slop indicators, useless-test prevalence, and unshipped-project rates
- Cross-referenced six related completed items (ai-first-software-ecology, productivity-incentive-metrics, it-throughput-constraint-magnitude, ai-code-entropy, build-vs-improve-throughput-tradeoff, oss-sustainability-ai-generated-contributions)
- Conducted full §0–§7 evidence gathering across all seven metric areas:
  - GitHub Octoverse 2019/2025: repository creation 44M to 121M/year, commit volume ~1B/year (+25% YoY)
  - GitClear 2025: code churn 3.1% to 5.7% (+84% relative); moved code 24.1% to 9.5% (-61%); copy-paste 8.3% to 12.3% (+48%); 211M line enterprise-skewed dataset
  - DevOps Research and Assessment (DORA) 2024: every 25% AI adoption = -7.2% delivery stability, -1.5% throughput, +2.1% individual productivity
  - Avelino et al. (2019): 16% of 1,932 popular GitHub projects abandoned; 41% rescued
  - Baltes et al. (2026): "tragedy of the commons" framing for AI slop; three clusters (Quality Degradation, Review Friction, Forces and Consequences)
  - Standish CHAOS 2020: 19% cancelled, 50% challenged (secondary summary; primary paywalled)
  - International Data Corporation (IDC)/Lenovo 2025 via CIO.com: 4 of 33 AI proof-of-concept (POC) projects reach production (88% non-deployment rate; secondary source)
  - No population-level longitudinal study found for useless-test prevalence
- Wrote complete Research Skill Output (§0–§7) and seeded Findings section
- Applied acronym audit: LOC, AI, DORA, pull request (PR), year-over-year (YoY), machine learning (ML), POC, Don't Repeat Yourself (DRY), Service Level Agreement (SLA), IDC all expanded on first prose use
- Marked as draft; triggered three review cycles
- Review pass 1 (actual): FAIL — SLA/IDC expansion, bold claim sentences, §6 opening inference label, Analysis missing label
- Review pass 1 (second trigger, now pass 2): FAIL — gitnux.org [fact] → [inference]; teaminnovatics.com [fact] → [inference]; Exec Summary DORA causal sentence; KF2/KF5/KF11 confidence; missing alternative explanation
- Review pass 2 (third trigger): FAIL — Standish CHAOS [fact] → [inference]; IDC/Lenovo [fact] → [inference]; mutation-testing definition [fact] → [inference]; "stable for decades" overstating evidence; Exec Summary "caused by" causal claim; missing cross-item reference to throughput-constraint item
- Fixed all violations; triggered final review — auto-passed at cap (review_count = 2 = MAX_REVIEWS)
- Completed item: moved to `Research/completed/`
- Updated `learnings.md` Thread 11 with 2019-2026 longitudinal quantification evidence

## Mini-Retro

1. **Did the process work?** Mostly. The research itself was thorough and the evidence gathered was solid across all seven metric areas. The review workflow correctly identified real violations in each pass.

2. **What slowed down or went wrong?** Three review cycles were needed instead of two. The most persistent pattern was `[fact]` assigned to claims where the cited source was secondary (paywalled primary, secondary media, personal blog) and for causal claims that were inferences, not directly observed facts. The citation-discipline skill's distinction between primary and secondary sources for `[fact]` labels needs to be applied earlier in the self-review, not just at the companion-skill check stage.

3. **What single change would prevent this next time?** Run a dedicated "secondary-source `[fact]` audit" before triggering the first review: grep for all `[fact]` labels, then for each one verify the cited URL is a primary source (government report, peer-reviewed paper, official platform statistics, or first-party dataset). Any claim backed only by a secondary aggregator, media article, secondary blog, or paywalled summary must be `[inference]`. Also check all "caused by" or directional causal language in Exec Summary for `[fact]` labels.

4. **Is this a pattern?** Yes. This matches the existing Known Recurring Pattern: `[fact]` on a historical origin or secondary-source claim. The prior Known Recurring Pattern table already covers similar cases (Wikipedia sole source, secondary practitioner source for historical origins). The new specific instance is `[fact]` for paywalled-primary stats cited via secondary media (CIO.com, thestory.is), which should be added as a row.

5. **Does any documentation need updating?** The Known Recurring Patterns table in `.github/copilot-instructions.md` should gain a row: "`[fact]` assigned to paywalled primary data cited via secondary media coverage" — same fix rule as the existing patterns.

6. **Do the default instructions need updating?** Not structurally. The existing `[fact]` source-quality rule is stated correctly in the task prompt. The gap is in the self-review step where the grep pattern should explicitly include `cio.com`, `thestory.is`, and similar secondary-media patterns alongside `gitnux`, `teaminnovatics`, and `botmonster` that were already on the check list.
