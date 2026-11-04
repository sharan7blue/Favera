# Project manager note — 4 November 2026

**Agent:** Mira (project-manager)
**Gate 1:** 25 Nov 2026 — 21 days

---

## Done today

- **Board corrected (PR #4 — week2/update-board-4nov):** Task 7 (prospect sheet, 60 rows) marked done; Task 17 (meta/OG/sitemap, PR #1 merged 31 Oct) marked done.
- **Legal pages updated (PR #5 — week2/privacy-contact-email):** `[CONTACT EMAIL]` → `privacy@faevra.io` and `[LAST UPDATED DATE]` → `4 November 2026` applied to privacy.html (3 instances) and terms.html (2 instances). Confirmed by founder.
- **context.json updated (this branch):** prospects.verified corrected to 60; round-5 research file added; contact email item removed from open_for_founder; unresolved_confirms trimmed; decisions brought current.

## Awaiting founder merge

| PR | Branch | What it does |
|----|--------|--------------|
| #4 | week2/update-board-4nov | Board: tasks 7 and 17 marked done |
| #5 | week2/privacy-contact-email | Legal pages: contact email and date |
| #6 (this) | week2/context-note-4nov | context.json and this note |

## Remaining [CONFIRM] items in privacy.html (7)

These need founder answers before the noindex flip. None block the site going live — they block the privacy page being treated as final.

1. Cookies check
2. Cloudflare Web Analytics cookie-free (open https://developers.cloudflare.com/web-analytics/)
3. Cloudflare logging
4. Tally cookies (check in a private browser window)
5. Cloudflare data and country
6. Google Workspace data and country
7. Tally data and country

## Single blocker for site going live

Connect Cloudflare Pages to the GitHub repo (5 minutes in the dashboard):

> apps.cloudflare.com → Pages → Create a project → Connect to Git → sharan7blue/Favera → build command: (blank) → output directory: `apps/web`

Nothing else blocks this. Mailbox, DNS, GitHub App, and 60 verified prospects are all done.

## Once site is live — next steps in order

1. Publish Tally form at https://tally.so/forms/KpY948/edit
2. Approve and send 5 outreach emails (drafts in docs/status/2026-10-24-sales-outreach.md)
3. Create og.png (spec in docs/status/2026-10-30-project-manager.md) and commit as apps/web/og.png
4. Answer the 7 privacy [CONFIRM] items above so the page can be finalised
5. Confirm ICO fee position: https://ico.org.uk/for-organisations/ukgdpr/accountability-and-governance/data-protection-fee/
