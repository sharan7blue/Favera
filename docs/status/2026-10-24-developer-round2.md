# Developer round 2, 2026-10-24

Branch: week1/privacy-page (from week1/site-polish). Not pushed. Source: docs/drafts/privacy-and-terms-v3.md (privacy notice only); QA: docs/status/2026-10-24-qa-tester-round3.md.

## Done
- apps/web/privacy.html: noindex, canonical https://faevra.io/privacy.html, reuses styles.css, DRAFT banner kept, FAEVRA LTD / 17534431 / registered office as in the draft. No terms section. Every [CONFIRM...] marker, plus [CONTACT EMAIL] and [LAST UPDATED DATE], is visible and wrapped in <mark>.
- index.html footer links to /privacy.html.
- styles.css: added banner, mark, table and legal-page rules (appended, nothing existing changed).
- scripts/check_placeholders.py (warns, exit 0; --strict exits 1). CLAUDE.md Commands line added. ci.yml: non-failing step added.

## Checks
- validate_agents.py: 10 agents valid.
- check_placeholders.py: 8 hits (2 REPLACE_ME on index.html lines 52-53, 6 lines with [CONFIRM in privacy.html); --strict exits 1 as intended.
- html.parser: both pages parse.
- Playwright screenshots /tmp/privacy-360.png and /tmp/privacy-1280.png; viewed the 360px one: no horizontal overflow (scrollWidth 360), table fits.
- htmlhint and linkinator did NOT run (npm blocked in sandbox, ENOTFOUND; not worked around). CLAUDE.md asks for all four before a PR, so run them in CI or locally.

## Notes for others
- The checker looks only for [CONFIRM and REPLACE_ME, as asked. [CONTACT EMAIL] and [LAST UPDATED DATE] are not caught by it; QA's "[ fails the build" idea would need a wider pattern.
- The draft's marker names differ from its table (analytics vs Cloudflare Web Analytics; ICO fee absent from the notice), as QA noted; I kept the notice text as written.
- Not committed: docs/drafts/privacy-and-terms-v3.md and docs/status/2026-10-24-copywriter-round3.md remain untracked (other roles' files).
- Project memory not updated: no .claude/agent-memory in the repo.
