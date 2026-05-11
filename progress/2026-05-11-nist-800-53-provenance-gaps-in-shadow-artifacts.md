# 2026-05-11 -- Research Loop (nist-800-53-provenance-gaps-in-shadow-artifacts)

**Completed:**

Research item:
- `Research/completed/2026-05-09-nist-800-53-provenance-gaps-in-shadow-artifacts.md` -- completed; the item finds that Microsoft Lists, Excel, and PowerPoint preserve only partial native provenance once workforce artifacts become authoritative records or spawn downstream derivatives. It maps those gaps primarily to Audit and Accountability (AU)-3, Audit and Accountability (AU)-10, Audit and Accountability (AU)-12, Configuration Management (CM)-3, Configuration Management (CM)-8, and System and Information Integrity (SI)-7, with severity rising sharply for payroll, access, compliance, and risk-reporting use cases.

Sources consulted:
- https://doi.org/10.6028/NIST.SP.800-53r5 (primary National Institute of Standards and Technology control catalog)
- https://support.microsoft.com/en-us/office/how-versioning-works-in-lists-and-libraries-0f6cd105-974f-44a4-aadb-43ac5bdfd247 (Microsoft Lists and SharePoint version-history behavior)
- https://support.microsoft.com/en-us/office/work-together-on-powerpoint-presentations-0c30ee3f-8674-4f0e-97be-89cf2892a34d (PowerPoint revision-highlighting and version-history limits)

## Mini-Retro

1. **Did the process work?** Yes. The research content passed review on the first substantive pass, and the completed item now has the expected control mapping, Findings, and learnings update.
2. **What slowed down or went wrong?** The research-review workflow passed the item but failed to push its `review_count` update because `main` advanced during the run.
3. **What single change would prevent this next time?** Add a pull-rebase-and-retry step, or equivalent push retry logic, to the research-review workflow before it pushes the `review_count` commit.
4. **Is this a pattern?** No clear pattern yet. This looked like a branch-race condition in the workflow rather than a repeated research-authoring failure.
5. **Does any documentation need updating?** `learnings.md` was updated because this item adds cross-cutting signal about provenance needing to survive across derivative artifact chains.
6. **Do the default instructions need updating?** No. The friction came from workflow push behavior rather than from missing research-loop instructions.
