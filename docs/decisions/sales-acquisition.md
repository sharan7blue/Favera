# Sales and Customer Acquisition Strategy

Status: active. Last updated: 2026-11-08 by project-manager.
Gate 1 deadline: 2026-11-25 (17 days from creation of this document).

---

## 1. The goal

Gate 1 (25 Nov 2026): 3 agencies give read-only Search Console access or ask for a second report.
Gate 2 (20 Dec 2026): 3 paying agencies or 5 written commitments.

The acquisition path is: cold outreach → free report offer → SC access granted → Gate 1 pass.

---

## 2. What we are selling (the USP)

Faevra produces plain-English traffic-drop reports from a Google Search Console export. The report:

- Groups pages by URL pattern (article, campaign, product, other) and compares each group before and after the drop.
- Explains what happened in plain English — which pages, which queries, when it started, and what the likely cause is.
- Is written for the agency to share with a non-technical client, not for the SEO practitioner to debug.

**Why this is different from every competitor:**

| Competitor | What it does | Why it falls short for Faevra's buyer |
|---|---|---|
| Semrush / Ahrefs position-change reports | Show keyword movements | Require the analyst to interpret; not client-ready |
| Manual Search Console analysis | Analyst builds their own story | Takes 2–4 hours per drop; inconsistent across clients |
| Generic white-label reporting tools (AgencyAnalytics, DashThis) | Build dashboards | Show raw numbers; no plain-English narrative |
| Algorithm-update trackers (Semrush Sensor, MozCast) | Flag industry-wide movements | Don’t relate the drop to the specific client’s pages |

Faevra's position: the only tool that produces a finished, client-ready plain-English explanation, not a data view that the analyst still has to interpret.

**Buyer persona:** a UK SEO agency, 5–50 people, doing monthly client reporting. They hit algorithm updates or seasonal drops regularly. Their pain is explaining drops to anxious clients quickly and credibly. They already have Search Console access.

---

## 3. The prospect list

60 verified UK SEO agencies in a private Google Sheet (CRM).
All are private limited companies or LLPs (PECR corporate-body rule).
Each row holds: legal name, site, company number, CH status, contact route, outreach status.

Sources: UK Government supplier directory (great.gov.uk), direct site and Companies House verification.
Research rounds: 5 (Oct–Nov 2026). Lead researcher: Rhea (research-analyst).

---

## 4. Outreach approach

### Rules (non-negotiable)
- Company name only: every email is from Faevra, never a personal name or personal profile.
- Email limited companies and LLPs only. No sole traders.
- One-click opt-out in every email. Any “stop” reply adds the address to the suppression list immediately.
- No separate sending domain. All emails from info@faevra.io.
- No price mentioned until Gate 2.
- No invented results, case studies or testimonials.
- Founder approves every draft before it is sent.

### The offer
Free traffic-drop report for one client site. Agency sends the Search Console export. Faevra builds the report. Agency reviews it before the client ever sees it.

The free report serves two purposes: it is the Gate 1 pass condition (SC access granted) and it proves the product to the buyer.

### Email structure
- Subject: short, specific to the agency (references their size, location or specialism).
- Body: 4–5 sentences. Who we are, what we do, the offer, the opt-out line.
- No links to faevra.io until the site is live and not noindexed.
- No attachments.
- Sender display name: Faevra.

---

## 5. Outreach pipeline (Harvey + Sol)

The pipeline uses two tools:

**Harvey** (runs on the founder’s laptop via Claude Code) handles enrichment and drafting:
1. Finds contact emails from agency sites by inspecting live signals (tech stack, careers page, footer links, job postings).
2. Writes contextual cold email drafts — one per prospect, referencing a specific signal from their site.
3. Stages each draft in the outbox queue at http://localhost:5555. The founder reviews and approves each one before anything is sent.
4. Sends approved emails from info@faevra.io via Gmail OAuth.

**Sol** (cloud agent, this session) handles tracking and reply management:
1. Reads the Google Sheets CRM after each Harvey wave and updates rows: status, draft date, Gmail draft ID.
2. Watches Gmail for replies. Logs outcome per row: “access granted” / “more info” / “stop” / “no reply after 7 days”.
3. Adds “stop” reply addresses to the suppression tab immediately.
4. Flags rows due for a follow-up (7 days, no reply) in a docs/status note for the founder to review.
5. Writes wave reports to docs/status/<date>-sales-outreach.md.

**Approval gate**: nothing is sent without the founder’s explicit approval in Harvey’s outbox UI.

---

## 6. Automation tools

### Harvey (primary — install on laptop)
Open-source sales agent running on Claude Code. Finds prospects, enriches with live signals, drafts contextual emails, stages in an outbox queue.
- Source: https://github.com/ethanplusai/harvey
- Setup reference: docs/decisions/harvey-setup.md
- Status: pending install (task 19).

### Gmail MCP (connected)
Sol uses `search_threads` to watch for replies and `create_draft` for follow-up drafts.

### Google Sheets MCP (connected)
Sol uses `get_values` and `update_values` to keep the CRM in sync.

### Clay (deferred)
500 free credits available. Potential use: bulk email enrichment for prospects where Harvey cannot find a contact email from the site itself. Decision deferred to wave 2.

---

## 7. Fake-door page

Proposed (not decided as of 2026-11-08): a separate landing page with real prices (Pro, Agency, Founding agency) to test willingness to pay before Gate 2. Decision proposed for Fri 13 Nov. Needs: a pass threshold (what percentage of visitors clicking “buy” counts as a signal), a Pro price, and a traffic plan following the company-name-only rule.

The fake-door page is separate from the outreach. Outreach aims at Gate 1 (SC access). The fake-door aims at Gate 2 signal (willingness to pay).

---

## 8. Suppression list

Maintained in the Google Sheets CRM as a separate tab. Harvey and Sol both check it before any draft or send. Any “stop” reply is added within one working day. Never contact a suppressed address again.

---

## 9. What needs the founder’s action before proceeding

- **Harvey setup** (task 19): install Harvey on the laptop per docs/decisions/harvey-setup.md.
- **Google Sheet URL/ID**: share with the agent team so Sol can read the prospect list directly.
- **Site live**: ideally outreach goes out when faevra.io is live. If starting before the site is live, omit the site link from emails and add it in the follow-up. `harvey train` requires the live URL.
- **Clay test**: approve or decline spending the 500 free credits.

---

## 10. Decisions log

| Date | Decision | Who |
|---|---|---|
| 2026-10-24 | No separate sending domain; first 30 by hand from main mailbox | founder |
| 2026-10-24 | Email limited companies only (PECR corporate-body rule) | project-manager |
| 2026-10-24 | 5 email drafts written by Sol; not sent; await mailbox and founder approval | Sol |
| 2026-11-03 | Mailbox live (info@faevra.io); 60 verified prospects reached | founder / Rhea |
| 2026-11-08 | Sales pipeline made an active priority; Sol assigned to draft-and-queue workflow | founder |
| 2026-11-08 | Harvey adopted as the enrichment and drafting tool; Sol becomes CRM tracker | founder |
