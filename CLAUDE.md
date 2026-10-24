# Faevra: rules for every Claude session

- UK English. Plain words. No emoji.
- Never mention the founder's day job or personal profiles in any copy, commit or file.
- Work on branches named `week1/<task>` (later `weekN/<task>`). Never push to `main`.
- Run the checks in `.github/workflows/ci.yml` locally before pushing.
- Every factual claim in copy or reports links to its source with an as-of date. No invented numbers, testimonials or customers.
- Client or agency data never enters this repo.
- Always wait for the founder's approval before: merging to `main`; changing DNS, email or billing; sending or posting anything to anyone; spending money; accessing a client's Search Console.
- Write a note to `docs/status/<YYYY-MM-DD>-<agent>.md` when a task finishes. If blocked, say so there instead of guessing.
- Stop conditions: if a task needs more than its `maxTurns`, or the done-when is unclear, stop and report.
