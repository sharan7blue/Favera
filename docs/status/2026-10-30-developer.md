# Developer note — 2026-10-30

## Task 17: schema.org JSON-LD, OG/Twitter meta tags, sitemap update

### What was done

4 work items across 6 files, committed to `week1/privacy-page`.

**1. Article JSON-LD (3 files)**
Added `Article` and `BreadcrumbList` schema.org JSON-LD blocks to the `<head>` of each article:
- `apps/web/articles/how-to-diagnose-google-search-console-traffic-drop.html`
- `apps/web/articles/google-penalty-vs-algorithm-update-traffic-drop.html`
- `apps/web/articles/client-organic-traffic-drop-what-to-do.html`

Each article block includes headline, description, datePublished/dateModified (2026-10-27), author, publisher with logo, mainEntityOfPage and image. BreadcrumbList has 3 items: Home, Articles, article page.

**2. Articles index JSON-LD (1 file)**
Added `BreadcrumbList` schema.org JSON-LD (2 items: Home, Articles) to `apps/web/articles/index.html`.

**3. OG image and Twitter card meta tags (4 files)**
Added `og:image`, `og:image:width`, `og:image:height`, `og:image:alt`, `twitter:card`, `twitter:image`, `twitter:title`, `twitter:description` to all 3 article pages and the articles index page.

**4. Homepage og:image:alt**
Already present at line 23 of `apps/web/index.html` from a prior commit. No change required.

**5. sitemap.xml**
Replaced with 7-URL sitemap: homepage, articles index, 3 article pages, privacy.html, terms.html. All entries include `<lastmod>` dates.

### Commit SHA

`1858275`

Branch: `week1/privacy-page`

### Validators

- `python3 scripts/validate_agents.py` — pass (10 agents valid)
- `python3 scripts/check_placeholders.py --strict` — 6 known placeholders in privacy.html and terms.html (expected; not introduced by this task)
- `npx htmlhint` — npm registry unreachable in cloud environment; JSON-LD blocks manually verified as valid JSON (braces, commas, quotes checked)
- `npx linkinator` — npm registry unreachable; all href values in changed files were present before this PR, no new external URLs introduced beyond schema.org context URLs

**Founder must run `npx --yes htmlhint@1.1.4 "apps/web/**/*.html"` and `npx --yes linkinator@6.1.1 apps/web --recurse --skip "^https?://"` locally before merge.**

### QA handoff note for Quinn

Schema validity self-checked. JSON-LD blocks in 4 files are valid JSON. OG and Twitter card meta tags follow the same pattern as the homepage (which was previously QA'd). sitemap.xml has 7 well-formed entries with lastmod dates. htmlhint/linkinator could not run in cloud environment — must be run locally before merge. All pages still carry `noindex`.

### Notes

- The 6 commits with article files were in a detached HEAD state and were fast-forwarded onto `week1/privacy-page` before task changes were applied.
- og.png (1200x630 px) remains an open item for the founder (listed in context.json open_for_founder).
