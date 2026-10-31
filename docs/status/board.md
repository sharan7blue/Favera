# Task board

Only the project manager reassigns tasks. One line per task: owner, status, link.

| # | Task | Owner | Status | Done when |
| --- | --- | --- | --- | --- |
| 1 | Create repo, push, connect Cloudflare Pages | developer | GitHub App installed (31 Oct 2026); blocked: Cloudflare Pages not yet connected; DNS registrar unknown | preview and production links load |
| 2 | Move faevra.io DNS to Cloudflare | founder | blocked: registrar unknown | https://faevra.io loads with a valid certificate |
| 3 | Mailbox with SPF, DKIM, DMARC | founder | done (31 Oct 2026): mailbox live; SPF, DKIM, DMARC confirmed by founder | test email passes all three |
| 4 | Page copy | copywriter | done (session 3): hero headline, lead, benefits, "who it is for" all sharpened; fourth bullet "You review it first" added | founder happy to send the link |
| 5 | Tally form | developer | draft form KpY948 at https://tally.so/forms/KpY948/edit; selfEmail set; index.html CTA wired; form not yet published | test submission appears as a row and an email |
| 6 | CI workflow | qa-tester | drafted in .github/workflows/ci.yml; GitHub App now installed — developer can test on branch | a broken link fails the check |
| 7 | 60-agency prospect sheet | research-analyst | 28 verified rows (rounds 1–4, 27 Oct 2026); docs/status/2026-10-27-research-analyst.md | 60 rows with name, site, size, source, contact route |
| 8 | Privacy page | copywriter | v4 committed; 6 [CONFIRM] groups remain — all require founder sign-off | live before any access request in week 4 |
| 9 | Terms page | copywriter | stub committed; 2 [CONFIRM] groups remain — Gate 1 items | live alongside privacy page before any access request |
| 10 | SEO audit | seo-specialist | done (session 3): title tags, OG tags, meta descriptions updated; robots.txt and sitemap.xml added; favicon.svg added; structured data improved; full audit in docs/status/2026-10-24-seo-specialist.md | noindex removed at launch |
| 11 | UX / accessibility audit | ux-designer | done (session 3): focus tokens, header/section/footer spacing, button colour guard, list spacing, brand link on index, section aria-label; full audit in docs/status/2026-10-24-ux-designer-round2.md | passes WCAG 2.2 AA on all three pages |
| 12 | Outreach drafts | sales-outreach | done (session 3): 5 drafts in docs/status/2026-10-24-sales-outreach.md — not sent; founder must approve and send from Faevra mailbox | founder approves and sends when mailbox is live |
| 13 | QA pre-launch audit | qa-tester | done (session 3): structural checks pass all 3 pages; all internal links resolve; 6 [CONFIRM] placeholders remain (expected); og.png missing; full report in docs/status/2026-10-24-qa-tester.md | placeholder check exits 0 at launch |
| 14 | Article topic research | seo-specialist | done (27 Oct 2026): 10 briefs in docs/status/2026-10-27-seo-specialist.md; 5 keyword guides can draft now; 5 data studies wait for Gate 1 | 10 topic briefs with keyword, intent, and source |
| 15 | Articles section on site | developer | done (28 Oct 2026): apps/web/articles/index.html built; article-list styles added to styles.css; all 3 drafts linked; structural checks pass; note in docs/status/2026-10-28-developer.md | apps/web/articles/index.html listing page and shared article template live on branch |
| 16 | Draft 3 articles (keyword guides 6, 8, 7) | copywriter | 3 drafts written and QA'd (27 Oct 2026): apps/web/articles/; 2 minor claim citations fixed; ready for founder review | 3 complete HTML article drafts in apps/web/articles/ committed to branch; QA pass required before founder review |
| 17 | Technical SEO: Article schema, OG tags, Twitter cards, sitemap | developer | QA pass (30 Oct 2026) — PR #1 open at https://github.com/sharan7blue/Favera/pull/1; htmlhint/linkinator must run locally before merge; og.png and Rich Results Test pending site live | htmlhint/linkinator pass; Rich Results Test returns valid Article for each article; sitemap lists all article URLs; QA pass |
