# In Progress

Research items currently being actively worked on or under review.

Files live here in two statuses:

- **`in-progress`** — item is being actively researched
- **`reviewing`** — research is complete; item is awaiting quality review

Files **do not move** when status changes from `in-progress` to `reviewing`. The file stays here until
review passes, at which point `python -m src.main research complete <filename>` moves it to
`../completed/`.

If review fails, fix the violations and run `python -m src.main research draft <filename>` again to
reset the status to `reviewing` and re-trigger the review workflow.
