# Faevra

Search Console traffic-drop reports for SEO freelancers and agencies. Solo founder, about 15 hours a week. Gate 1 is 2026-11-25, Gate 2 is 2026-12-20.

## Commands
- Run the site: `cd apps/web && python3 -m http.server 4321`
- Lint HTML: `npx --yes htmlhint@1.1.4 "apps/web/**/*.html"`
- Check links: `npx --yes linkinator@6.1.1 apps/web --recurse --skip "^https?://"`
- Validate agents: `python3 scripts/validate_agents.py`

## Workflow
- Branch `weekN/<task>`; never push to `main`. A hook and a deny rule enforce this.
- Run all four commands above before opening a pull request.
- Write a note to `docs/status/<YYYY-MM-DD>-<agent>.md` when a task ends, or when blocked.

## Founder approval is always required for
Merging to `main`; DNS, email or billing changes; sending or posting anything to anyone; spending money; accessing a client's Search Console data.

## Never
- Mention the founder's day job or personal profiles anywhere.
- Put client or agency data, secrets or personal prospect data in this repo.
