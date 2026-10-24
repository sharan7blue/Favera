# SEO audit of apps/web/index.html

Role: seo-specialist. Date: 2026-10-24. Source audited: `apps/web/index.html` as of 2026-10-24 (54 lines). Nothing in `apps/web` was edited. Audit is by reading the file; no live URL exists yet (board task 1 and 2 in progress or blocked), so nothing was fetched and no ranking, index or traffic claim is made.

Handoff: developer (change requests below), then qa-tester. Owner of launch flip: developer, with founder approval for the merge to `main` and any DNS step.

## Findings

| Item | Status | Note |
| --- | --- | --- |
| `<html lang="en-GB">`, charset, viewport | Pass | Nothing to change. |
| `<title>` | Pass | "Faevra: why did your client's search traffic drop?" matches the h1 and the page intent. Keep. |
| Meta description | Pass | One sentence, says what the product is and who it is for. Keep. |
| Canonical | Missing | Add. Needs the final production host; board task 2 says `https://faevra.io`. Confirm www or apex before launch. |
| Open Graph | Missing | Add. An image is also missing (no image file exists in `apps/web`). |
| Twitter/X card | Missing | Add. |
| Organization structured data | Missing | Add JSON-LD, minimal and factual (see below). |
| Robots meta | `noindex` present | Correct for now. Comment says to remove at launch. See flip checklist. |
| robots.txt, sitemap.xml | Missing | Plan below. Do not publish a sitemap while the site is noindex. |
| Favicon | Missing | Add one; browsers request `/favicon.ico` anyway and get a 404. |
| Headings | Pass | One h1, three h2s, sensible order. The brand name is a `<p>`, which is fine. |
| Placeholder CTA | Launch blocker | `https://tally.so/r/REPLACE_ME` is still in the page (board task 5). |
| Privacy page | Not yet | Board task 8. Do not link to or list it in the sitemap until it is live. |

## Change request 1: head additions (developer, apply on a `weekN/` branch)

Insert after the meta description and before the stylesheet link. Replace `https://faevra.io/` if the final host differs. Keep the existing `noindex` line until the launch day flip.

```html
  <link rel="canonical" href="https://faevra.io/">
  <link rel="icon" href="/favicon.svg" type="image/svg+xml">
  <meta name="theme-color" content="#ffffff">

  <meta property="og:type" content="website">
  <meta property="og:site_name" content="Faevra">
  <meta property="og:locale" content="en_GB">
  <meta property="og:url" content="https://faevra.io/">
  <meta property="og:title" content="Faevra: why did your client's search traffic drop?">
  <meta property="og:description" content="Faevra turns a Google Search Console export into a plain-English traffic-drop report for SEO freelancers and agencies.">
  <meta property="og:image" content="https://faevra.io/og.png">
  <meta property="og:image:alt" content="Faevra: why did your client's search traffic drop?">

  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="Faevra: why did your client's search traffic drop?">
  <meta name="twitter:description" content="Faevra turns a Google Search Console export into a plain-English traffic-drop report for SEO freelancers and agencies.">
  <meta name="twitter:image" content="https://faevra.io/og.png">
```

Assets the developer or ux-designer must supply (none exist today): `apps/web/favicon.svg` and `apps/web/og.png` (1200 x 630 is the usual share-image size; plain brand name and the h1 text, no invented numbers, logos or testimonials). Until `og.png` exists, drop the three image lines rather than pointing at a 404.

## Change request 2: Organization structured data

Place before `</head>`. Deliberately minimal to follow the site-copy rules: no contact address or email (mailbox does not exist yet, board task 3), no `sameAs` links (no personal profiles anywhere), no logo (none exists), no ratings or reviews.

```html
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "Organization",
    "name": "Faevra",
    "legalName": "Faevra Ltd",
    "url": "https://faevra.io/",
    "description": "Faevra turns a Google Search Console export into a plain-English traffic-drop report for SEO freelancers and agencies."
  }
  </script>
```

Add `logo` once a logo file is live, and `contactPoint` or `email` only once the mailbox passes SPF, DKIM and DMARC. Validate with Google's Rich Results Test or the Schema.org validator after the page is live (as-of check needed at launch; I have not run either).

## Change request 3: noindex that cannot be forgotten on previews

The meta tag only protects the page it is in. Cloudflare Pages also serves every branch preview on a `*.pages.dev` host, and the production `*.pages.dev` alias keeps working after launch. Add `apps/web/_headers` now:

```
# Keep every pages.dev host out of search, before and after launch.
https://*.pages.dev/*
  X-Robots-Tag: noindex
```

Cloudflare documents that `_headers` rules can match on a host and apply to `pages.dev` URLs; confirm against the current Cloudflare Pages docs when implementing (not fetched in this audit). After launch, this rule keeps previews and the `pages.dev` alias unindexed while `faevra.io` becomes indexable, which also avoids duplicate-content between hosts. The canonical tag backs this up.

Do not add a site-wide `X-Robots-Tag: noindex` here, as it would defeat the launch flip.

## Change request 4: robots.txt and sitemap plan

Pre-launch (now): do not add a sitemap. Optional robots.txt is not needed; noindex is the control. Do NOT put `Disallow: /` in robots.txt: a crawler blocked by robots.txt cannot see the `noindex` tag, and blocked URLs can still appear in results from links.

At launch, add `apps/web/robots.txt`:

```
User-agent: *
Allow: /

Sitemap: https://faevra.io/sitemap.xml
```

AI-crawler access: the role brief covers it, but allowing or blocking AI crawlers (for example GPTBot, ClaudeBot, PerplexityBot, Google-Extended) is a policy choice for the founder, not an SEO default. Recommendation: allow all (the `User-agent: *` rule above), because the product wants to be found and cited by name. If the founder prefers to block any, it is a per-bot `Disallow: /` block added to the same file. Route the decision via project-manager.

At launch, add `apps/web/sitemap.xml`, listing live, indexable canonical URLs only. Today that is one URL:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url>
    <loc>https://faevra.io/</loc>
    <lastmod>2026-MM-DD</lastmod>
  </url>
</urlset>
```

Set `lastmod` to the real launch date. Add the privacy and terms pages only once they are live (board task 8). Keep `lastmod` honest: change it only when the page content changes.

## Launch-day checklist (flip noindex safely)

Preconditions (all must be true; otherwise do not flip):

1. Founder has given approval to launch (merge to `main`, and any DNS change are founder-approved per CLAUDE.md).
2. https://faevra.io loads over a valid certificate (board task 2 done-when) and the host choice (apex or www) is final, with the other redirecting to it.
3. `REPLACE_ME` is gone from the CTA and the Tally form is published and a test submission lands in the sheet and email (board task 5).
4. Privacy page is live and linked (board task 8) before any access request is invited.
5. qa-tester has passed the CI and the four commands in CLAUDE.md (HTMLHint, linkinator, agent validation).
6. Head additions from change request 1 and 2 are merged; `og.png` and `favicon.svg` return 200.
7. `_headers` from change request 3 is deployed.

The flip, in one pull request on a `weekN/launch-seo` branch, then founder-approved merge:

1. Delete the two lines in `index.html`: the comment "Remove the next line at launch..." and `<meta name="robots" content="noindex">`. Do not replace with `index, follow`; the default is indexable.
2. Add `robots.txt` and `sitemap.xml` as above.
3. Confirm no `noindex` remains anywhere: `grep -rn "noindex" apps/web` should return only the comment-free `_headers` pages.dev rule.

Post-deploy checks (same day, on the live host, record results with date in a new status note):

1. `curl -sI https://faevra.io/` shows no `X-Robots-Tag: noindex`; `curl -s https://faevra.io/ | grep -i robots` returns nothing.
2. `curl -sI https://<project>.pages.dev/` still shows `X-Robots-Tag: noindex`.
3. `https://faevra.io/robots.txt` and `/sitemap.xml` return 200 with the correct content types, and the sitemap URL matches the canonical exactly (scheme, host, trailing slash).
4. The `www` or non-preferred host redirects with a 301 to the canonical host.
5. View source: canonical, OG, Twitter and JSON-LD are present and use `https://faevra.io/`.
6. Share the URL in a link-preview checker for OG and Twitter cards (founder or developer; posting anywhere is founder-approved, so use a checker tool, not a public post).
7. Search Console: adding a property and verifying ownership is a DNS or file change, so it needs founder approval. Then submit the sitemap and use URL Inspection on `/` to request indexing. Do not report indexing or ranking as achieved until data shows it.

Rollback if something is wrong: restore the `noindex` meta line and redeploy. Pages that were already crawled drop out only after a recrawl, so avoid flipping early.

## Open items for project-manager

- Founder decision: allow or block AI crawlers (recommendation: allow).
- Final canonical host (apex vs www) depends on board task 2 (registrar still unknown).
- Share image and favicon need an owner (suggest ux-designer, then developer).
- No project memory directory exists for this role (`.claude/agent-memory` absent), so no memory was updated.
