# Project manager — 24 Oct 2026 (session 2)

Autonomous build run per founder's instruction. All items that do not need founder input completed this session.

## Done

- **privacy.html → v4**: England and Wales confirmed; controller/processor split written; retention as founder policy; Tally BV (Belgium, EU servers) facts added from verified cookie/privacy policy; Cloudflare Web Analytics named but cookie claim left as [CONFIRM]; invoice/tax line corrected to "if and when we issue invoices". Committed on branch `week1/privacy-page`.
- **terms.html stub**: plain-English terms covering what the service is, IP, confidentiality, governing law, and placeholder sections for pricing and liability cap. Footer links from index.html and privacy.html updated. Committed on branch `week1/privacy-page`.
- **Tally form KpY948**: six questions (name, company, website, work email, retainer size, biggest pain). Thank-you page set. Self-notification email to sharanshekar16@gmail.com. index.html CTA updated from REPLACE_ME to real form URL. Form is a **draft — founder must publish it** at https://tally.so/forms/KpY948/edit before launch.
- **board.md and context.json**: updated for v4 privacy, terms stub, Tally form, and all blockers.

## Blocked (needs founder)

1. **Contact email** — placeholder [CONTACT EMAIL] in privacy.html, terms.html, index.html footer. Provide the Google Workspace address once set up (board #3).
2. **GitHub App** — push is refused until the Claude GitHub App is installed for sharan7blue/Favera (or repo renamed to faevra). All code is in the local build workspace only.
3. **Publish Tally form** — founder opens https://tally.so/forms/KpY948/edit and clicks Publish. Custom notification email subject/body needs Tally Pro.
4. **Cloudflare Web Analytics cookie claim** — open https://developers.cloudflare.com/web-analytics/ and confirm whether it sets cookies. Until confirmed, the privacy notice does not say "cookie-free".
5. **Tally cookies in private window** — open the form in a private/incognito window and check the browser's cookie inspector before launch.
6. **DNS registrar** — needed to point faevra.io to Cloudflare Pages (board #2).
7. **Prospect list** — 14 of 60 verified; Rhea's fetch tools are blocked; more rows need a browser-connected session or founder-supplied agency names.

## Week 1 spec status (as of 24 Oct)

| # | Task | Status |
| --- | --- | --- |
| 1 | Repo push + Cloudflare Pages | blocked: GitHub App |
| 2 | DNS | blocked: registrar |
| 3 | Mailbox | not started |
| 4 | Page copy | done (branch week1/site-polish) |
| 5 | Tally form | draft created; not published |
| 6 | CI workflow | drafted; untested on GitHub |
| 7 | Prospect sheet | 14/60 verified |
| 8 | Privacy page | v4 draft committed |
| 9 | Terms page | stub committed |
