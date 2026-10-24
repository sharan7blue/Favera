# Agents System Overview

Faevra sells plain-English Search Console traffic-drop reports to SEO freelancers and agencies. One founder approves; an agent team prepares. Role prompts live in `.claude/agents/`; `project-manager` is the orchestrator.

## Agents in this system

| Agent                | Role                                        | Hands off to                                         |
|----------------------|---------------------------------------------|------------------------------------------------------|
| `project-manager`    | Router / entry, orchestrator (management)   | every other agent; founder (daily report)            |
| `research-analyst`   | Sourced research (research)                 | `sales-outreach`, `seo-specialist`, `copywriter`     |
| `developer`          | Site and app code (development)             | `qa-tester`                                          |
| `ux-designer`        | Layout and accessibility (development)      | `developer`, `qa-tester`                             |
| `data-engineer`      | Export parser, dormant until Gate 1 (development) | `report-reviewer`                              |
| `qa-tester`          | Code, copy and claim checks (testing)       | `project-manager` on pass; the author on block       |
| `report-reviewer`    | Recomputes every report figure (testing)    | `project-manager`, then founder review               |
| `seo-specialist`     | Site SEO and traffic-drop reports (marketing) | `report-reviewer` (reports), `developer` (site changes) |
| `copywriter`         | Site, legal-page and community copy (marketing) | `qa-tester`, then `developer`                     |
| `sales-outreach`     | Prospect scores and Gmail drafts (marketing) | `qa-tester`, then founder review                    |

Dormant roles sit in `.claude/agents-dormant/`; move one to `.claude/agents/` to activate it.

## Orchestration rules

- All founder requests enter through `project-manager` only. Start sessions with `claude --agent project-manager`.
- No agent communicates with the founder directly except `project-manager`; every other agent returns a summary of at most 150 words plus links to its caller.
- Failures bubble up to `project-manager`, not to the founder. A blocked or failed task is written to the agent's note as `blocked: <reason>`; the orchestrator decides to retry, reassign or put it under "Needs you".
- All agents read `docs/status/context.json`; only `project-manager` writes to it. A hook blocks every other agent from writing it.
- `project-manager` assigns at most three tasks a day, each with a goal, evidence links, rules and a done-when. Only it reassigns tasks.
- Agents hand work over through `docs/status/<date>-<agent>.md`, and never edit another agent's output.
- Nobody reviews their own work: code and copy go to `qa-tester`, reports to `report-reviewer`.
- Non-developer agents write only under `docs/` (enforced by a hook).

## Founder approval is always required for

Merging to `main`; DNS, email or billing changes; sending or posting anything to anyone; spending money; accessing a client's Search Console data. Drafting is automatic; sending is the founder's.

## Rules for every agent

- UK English, plain words, no emoji.
- Every fact, price or market claim links to its source with an as-of date. No invented numbers, customers or testimonials.
- Never mention the founder's day job or personal profiles anywhere.
- Never put client or agency data, secrets or personal prospect data in this repo.
- If a task has no done-when, or needs more turns than allowed, stop and report instead of guessing.

## Where things are

- Shared context: `docs/status/context.json`. Board: `docs/status/board.md`. Decisions: `docs/decisions/`.
- Plan, scores and roadmap: the Faevra project documents on claude.ai (start with `claude/faevra-start-here.md`).
- Site: `apps/web/`. App after Gate 1: `apps/app/`.
