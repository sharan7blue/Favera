# Developer note — 28 Oct 2026

## Task 15: Articles section on site

**Status: done**

### What was built

`apps/web/articles/index.html` — the articles listing page at faevra.io/articles.

Structural choices:
- Same HTML pattern as article pages: doctype, `lang="en-GB"`, `../styles.css`, skip-link, brand header, `#main-content`, footer.
- `og:type` set to `website` (not `article`).
- `noindex` and `draft-banner` in place until founder approves for publish.
- Lists all 3 article drafts with date, DM Serif Display title (as a link), and summary text drawn from each article's meta description.

CSS additions to `apps/web/styles.css` (new "Article listing" block):
- `.article-list` — strips list-style and padding.
- `.article-item` — 1.5rem padding-top/bottom, bottom border rule.
- `.article-date`, `.article-title`, `.article-summary` — spacing and typography, title uses DM Serif Display at 1.3rem.
- `.article-title a` — inherits `--text` colour on rest, switches to `--accent` on hover.

### Checks run

Python structural validator: 12/12 pass (DOCTYPE, lang, canonical, description, og:title, noindex, skip-link, h1, main, footer, draft-banner, 3 article links present).

htmlhint and linkinator cannot run in this environment (npm registry unreachable). Must be run locally before merge.

### Done-when status

- [x] `apps/web/articles/index.html` committed to branch `week1/privacy-page`
- [x] Article list CSS added to `apps/web/styles.css`
- [ ] htmlhint and linkinator — must run locally (npm registry unreachable in cloud)
- [ ] Founder review before removing noindex and draft-banner

### Handoff

Board task 15 marked done. No further action required from developer until founder approves articles for publish.
