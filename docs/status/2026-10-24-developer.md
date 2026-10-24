# Developer note, 2026-10-24: week1/site-polish

Branch `week1/site-polish` (from `main`, not pushed). Sources: docs/status/2026-10-24-ux-designer.md and 2026-10-24-seo-specialist.md.

## Applied
- UX fixes 2 to 6: button hover/active, full-width button under 480 px, `color-scheme: light dark`, explicit button focus-visible outline, tighter hero spacing on phones, `text-wrap: balance` on h1/h2 and `pretty` on the lead.
- SEO head: canonical `https://faevra.io/`, Open Graph and Twitter tags (card type `summary`), Organization JSON-LD (as written by the SEO note), theme-color for light and dark.
- `apps/web/_headers`: `X-Robots-Tag: noindex` for `https://*.pages.dev/*`. Not verified against current Cloudflare docs.
- `apps/web/robots.txt`: `User-agent: *` / `Allow: /`, no `Disallow: /`, no Sitemap line (sitemap is a launch task).

## Not done, on purpose
- Page `<meta name="robots" content="noindex">` left in place (launch flip is founder-approved later).
- Tally `REPLACE_ME` link untouched (UX fix 1, board task 5).
- No `og:image` / `twitter:image` and no favicon link: no image assets exist; I did not invent any. Twitter card is `summary` rather than `summary_large_image` for that reason. Owner needed for `og.png` (1200x630) and `favicon.svg`; then add the tags and switch to `summary_large_image`.
- UX fix 7 (brand link) skipped: needs more pages.
- Host (apex vs www) still undecided (board task 2); canonical uses the apex as instructed.

## Checks (2026-10-24)
- `python3 scripts/validate_agents.py`: 10 agents valid.
- htmlhint and linkinator: NOT RUN. `registry.npmjs.org` is unreachable from this sandbox (DNS fails; it is on the proxy no-proxy list) and nothing is cached. I did not bypass the proxy settings. Stand-in: HTML parsed with Python, JSON-LD parsed as valid JSON, the only local references are `styles.css` (exists). QA or CI must run the two commands.
