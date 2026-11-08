# Harvey Setup — Faevra

Status: pending setup. Added: 2026-11-08.
Harvey runs on the founder's laptop. This file is the reference configuration.
Do not clone Harvey into this repo; keep it in a separate directory.

---

## What Harvey is

Harvey is an open-source autonomous sales agent that runs on top of Claude Code.
Source: https://github.com/ethanplusai/harvey

For Faevra's pipeline:
- Harvey finds contact emails from agency sites, inspects signals (tech stack, careers page, footer links), and writes contextual cold email drafts.
- Drafts wait in a local outbox at http://localhost:5555. The founder reviews each one and approves before anything is sent.
- Harvey sends from info@faevra.io via Gmail OAuth. No separate sending domain.

Sol (the sales-outreach agent) works downstream: it syncs Harvey's completed drafts to the Google Sheets CRM and watches Gmail for replies.

---

## Prerequisites

- Python 3.11+ (macOS ships 3.9; `brew install python@3.13`)
- Claude Pro or Max with `claude login` already done
- Access to info@faevra.io Gmail account for OAuth

---

## Install (run outside the Faevra repo)

```bash
cd ~/projects   # or wherever you keep separate projects
git clone https://github.com/ethanplusai/harvey.git harvey-faevra
cd harvey-faevra
python3.13 -m venv .venv
source .venv/bin/activate
pip install -e .
cp .env.example .env
```

Edit `.env`: the only required value is the Gmail provider. Harvey will open a browser for the Google OAuth flow on first run.

---

## Configuration

Create `harvey.local.yaml` in the Harvey directory (this file is gitignored and overrides `harvey.yaml`):

```yaml
persona:
  name: "Faevra"
  company: "Faevra"
  role: "Business Development"
  email: "info@faevra.io"
  linkedin: ""              # never use; LinkedIn automation violates TOS
  tone: "professional, plain-spoken, direct"

product:
  name: "Faevra"
  description: >-
    Plain-English traffic-drop reports for UK SEO agencies.
    When a client\'s organic traffic drops, Faevra analyses the Search Console
    export and produces a finished, client-ready explanation: which pages,
    which queries, when it started, and what the likely cause is.
    The agency shares it directly with their client.
  pricing: ""              # no price until Gate 2 (20 Dec 2026)
  key_benefits:
    - "Client-ready plain-English explanation — no analyst interpretation needed"
    - "Groups pages by URL pattern to pinpoint exactly which parts of the site were hit"
    - "Works from a standard Search Console export — no integrations required"
  objection_responses:
    "already use Semrush or Ahrefs": >-
      Those are great for tracking rankings. Faevra does something different:
      it produces the finished client-ready explanation after a drop, so your
      team doesn't spend 2–3 hours writing it up.
    "not interested": >-
      No problem at all. If a client\'s traffic ever drops and you need a quick
      explanation for them, we\'d be glad to show you what the report looks like.

offer:
  primary: ""               # no price until Gate 2
  entry: >-
    Free traffic-drop report for one client site in exchange for
    15 minutes of feedback.
  goal: "get_reply"
  booking_method: "ask_preference"
  booking_url: ""
  meeting_duration: "15 minutes"
  meeting_owner: "Faevra"

icp:
  industries:
    - "SEO Agency"
    - "Digital Marketing Agency"
  company_size: "5-50 employees"
  titles:
    - "Director"
    - "Managing Director"
    - "Head of SEO"
    - "SEO Director"
    - "Founder"
  geography:
    - "United Kingdom"
  hiring_signals:
    - "SEO Manager"
    - "SEO Executive"
    - "SEO Strategist"

channels:
  email:
    enabled: true
    provider: "gmail"
    max_daily_sends: 10          # conservative; founder reviews every draft
    require_approval: true       # drafts wait in outbox; founder approves each
    send_to_risky: false
    max_bounce_rate: 0.03
  linkedin:
    enabled: false               # LinkedIn automation violates TOS
    max_daily_connections: 0
    max_daily_messages: 0

usage:
  max_daily_claude_percent: 60
  heartbeat_interval_minutes: 15
  quiet_hours:
    start: "21:00"
    end: "08:00"
    timezone: "Europe/London"
```

---

## First run

```bash
# Option A: Guided (recommended for first time)
cd ~/projects/harvey-faevra
source .venv/bin/activate
claude
# Then say: "set up Harvey for me"

# Option B: Manual
cd ~/projects/harvey-faevra
source .venv/bin/activate
harvey train https://faevra.io   # run once site is live; builds product_knowledge.md
harvey dashboard                 # http://localhost:5555
```

Note: `harvey train` scrapes the site to build product knowledge. Run it only once faevra.io is live and not noindexed. Until then, the product description in `harvey.local.yaml` above bootstraps Harvey's knowledge.

---

## Working with the existing prospect list

Do not use `harvey discover` on the first run. We already have 60 verified UK limited companies in the CRM sheet. Import them directly to skip discovery and ensure only pre-screened, PECR-compliant companies are contacted.

Check Harvey's docs for the `harvey import` command or use the dashboard import flow to load a CSV export from the CRM sheet.

---

## Rules before any sends (non-negotiable)

1. `require_approval: true` must stay on. Never set it to `false`.
2. Use only the pre-imported 60 agencies. Do not let Harvey discover new UK prospects autonomously until the existing list is worked through.
3. All emails from info@faevra.io. No personal name in the sign-off.
4. Every draft must include: "Reply 'stop' at any time and I won't contact you again." Check Harvey's outbox copy before approving.
5. No price in any email. No case studies or invented results.
6. If Harvey sends to a sole trader or non-UK company, add them to the suppression list immediately.
7. After approving a batch, export the sent list to Sol for CRM sync.

---

## Known conflicts and mitigations

| Issue | Harvey default | Faevra mitigation |
|---|---|---|
| `--dangerously-skip-permissions` | On | Harvey runs in a separate directory; Faevra repo not affected |
| Discovers any company | `harvey discover` | Use `harvey import` with the pre-screened 60 |
| Recommends separate sending domain | Yes | Use Gmail (info@faevra.io); `require_approval: true` |
| LinkedIn enabled | Yes | `linkedin.enabled: false` in harvey.local.yaml |
| No PECR filtering | None | Only import pre-screened limited companies from CRM |
| Opt-out line | Not standard | Check every outbox draft before approving |
