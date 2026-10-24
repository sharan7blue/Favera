# Faevra

Plain-English Search Console traffic-drop reports for SEO freelancers and agencies.

- `apps/web/` the one-page site, plain HTML and CSS, deployed by Cloudflare Pages
- `docs/` plan, decisions and daily status written by the agent team
- `.claude/agents/` the seven agent definitions (manager plus six specialists)
- `.claude/settings.json` deny rules and hooks that enforce the approval list

## Run locally

```sh
cd apps/web && python3 -m http.server 4321
```

Open http://localhost:4321. Every change goes on a branch named `week1/<task>`; Cloudflare Pages builds a preview link per branch and `main` is production.

## Not in this repo

Agency and prospect data lives in a private Google Sheet. Secrets live in Cloudflare and GitHub settings.
