# Task board

Only the project manager reassigns tasks. One line per task: owner, status, link.

| # | Task | Owner | Status | Done when |
| --- | --- | --- | --- | --- |
| 1 | Create repo, push, connect Cloudflare Pages | developer | in progress | preview and production links load |
| 2 | Move faevra.io DNS to Cloudflare | founder | blocked: registrar unknown | https://faevra.io loads with a valid certificate |
| 3 | Mailbox with SPF, DKIM, DMARC | founder | not started | test email passes all three |
| 4 | Page copy | copywriter | draft in `apps/web/index.html`; UX and SEO fixes applied on branch week1/site-polish (e0e51fd) | founder happy to send the link |
| 5 | Tally form linked to a sheet | developer | not started | test submission appears as a row and an email |
| 6 | CI workflow | qa-tester | drafted, untested on GitHub | a broken link fails the check |
| 7 | 60-agency prospect sheet | research-analyst | 13 verified (rows 1-13, Semetrical with caveat) + Blue Array = 14 of 60; rows 14-15 dropped; tools blocked more fetches, see round2 note | 60 rows with name, site, size, source, contact route |
| 8 | Privacy page and short terms | copywriter | privacy.html built on branch week1/privacy-page (854bc90) from v3 draft; QA passed v3 for a non-live build; terms page not built; strict placeholder check must pass before launch (scripts/check_placeholders.py --strict) | live before any access request in week 4 |
