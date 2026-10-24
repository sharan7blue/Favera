# Faevra team

Faevra sells plain-English Search Console traffic-drop reports to SEO freelancers and agencies. One founder (about 15 hours a week) approves; an agent team prepares. This file is the shared brief for every agent and every tool that reads `AGENTS.md`. Role prompts live in `.claude/agents/`.

## Teams and roles

| Team | Role | File | Model | Produces | Reviewed by |
| --- | --- | --- | --- | --- | --- |
| Project management | Project manager | `project-manager` | sonnet | Board, task assignments, daily 07:00 report | Founder |
| Research | Research analyst | `research-analyst` | haiku | Sourced prospect lists, competitor notes, market figures | Project manager |
| Development | Developer | `developer` | sonnet | Branches and pull requests | QA tester |
| Development | UX designer | `ux-designer` | sonnet | Page and report layout notes, accessibility review | QA tester |
| Development | Data engineer | `data-engineer` (dormant until Gate 1) | sonnet | Export parser and analysis code on synthetic data | Report reviewer |
| Testing | QA tester | `qa-tester` | sonnet | Pass or block verdicts with evidence | Project manager |
| Testing | Report reviewer | `report-reviewer` | sonnet | Recomputed figures and claim checks for each report | Founder |
| Marketing | SEO specialist | `seo-specialist` | sonnet | Site SEO change requests, manual traffic-drop reports | Report reviewer, then founder |
| Marketing | Copywriter | `copywriter` | sonnet | Site, legal-page and community copy | QA tester, then founder |
| Marketing | Sales outreach | `sales-outreach` | sonnet | Prospect scores, Gmail drafts, reply log | QA tester, then founder |

Dormant roles sit in `.claude/agents-dormant/`; move one to `.claude/agents/` to activate it.

## How work flows

1. The project manager reads the board and assigns at most three tasks a day, each with a goal, evidence links, rules and a done-when.
2. A producing role does the task and writes a note to `docs/status/<date>-<role>.md`.
3. A reviewing role checks it independently: code and copy go to the QA tester, reports go to the report reviewer.
4. The project manager puts anything that needs a decision under "Needs you" in the daily report, with a recommendation.
5. The founder approves, declines or edits. Only then does anything merge, send or publish.

Roles hand work over only through files in `docs/status/`. They never edit each other's output.

## Founder approval is always required for

Merging to `main`; DNS, email or billing changes; sending or posting anything to anyone; spending money; accessing a client's Search Console data. Drafting is automatic; sending is the founder's.

## Rules for every role

- UK English, plain words, no emoji.
- Every fact, price or market claim links to its source with an as-of date. No invented numbers, customers or testimonials.
- Never mention the founder's day job or personal profiles anywhere.
- Never put client or agency data, secrets or personal prospect data in this repo.
- Return a summary of at most 150 words plus links; detail goes in `docs/status/`.
- If a task has no done-when, or needs more turns than allowed, stop and report instead of guessing.

## Where things are

- Plan, scores and roadmap: the Faevra project documents on claude.ai (start with `claude/faevra-start-here.md` in the project).
- Board: `docs/status/board.md`. Decisions: `docs/decisions/`.
- Site: `apps/web/`. App after Gate 1: `apps/app/`.
