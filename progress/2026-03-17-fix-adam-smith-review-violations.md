# Session: Fix Adam Smith Research Item Review Violations
**Date:** 2026-03-17
**Slug:** fix-adam-smith-review-violations

## Task
Apply review-violation fixes to `Research/completed/2026-03-15-adam-smith-org-design-desire-paths-ai.md` based on issues #202, #203, #207, #208, #209, #210, #211, #212, #213, #214.

## Changes Made

### Em-dash removal (all issues)
Replaced all 98 em-dash characters (—) with ` - ` (space-hyphen-space) throughout the document.

### Issue #208 - Mises Institute URL
- §2 A4: Added `[URL NEEDED]` after `Mises Institute PDF` citation for Herbener "An Integration"
- Findings Assumptions: Added `[URL NEEDED]` after `Mises Institute` in Herbener 1987 reference

### Issue #209 - Wikipedia-sourced fact relabelled
- §2 C1: Relabelled `**[fact]**` to `**[inference]**` for the desire-path definition sourced solely to Wikipedia (tertiary source)

### Issue #214 - Acronym expansions and Springer incomplete citation
- §6 Assumptions (first use): Expanded `UX` to `User Experience (UX)`
- Findings Evidence Map: Expanded `HR` to `Human Resources (HR)` at first use
- §2 E evidence: Added `[full citation NEEDED: author, title, URL/DOI required]` to Springer article citation
- §6 Evidence Map: Added same note to Springer paper citation
- Findings Evidence Map: Added same note to Springer formal/informal org paper citation

## Issues Not Applicable
The following issues reference content not present in the current 482-line document:
- **#202** (shadow IT claim, DoL abbreviation) - that specific shadow IT text and "DoL" abbreviation are not in the file
- **#203** (Technical/Regulatory/Behavioural lens specific claims) - those specific lens sections/sentences not in the file
- **#207** (Miller Nash citations, fourfold claim) - not in the file
- **#208** (cmu.edu, Forrester, Findings ES Wikipedia) - those claims not in the file
- **#210** (KF1-KF8 labels) - Findings uses numbered items 1-12, not KF format
- **#211** (LinkedIn pulse incomplete URL) - LinkedIn has full URL in sources list; no inline "(linkedin.com/pulse)" citation exists
- **#212** (F1 statistics bundled citation) - not in the file
- **#213** (KF8 Wikipedia, Irrational Labs) - not in the file

## Outcome
Committed as `f499d48` on branch `copilot/clean-up-research-review-issues`.
