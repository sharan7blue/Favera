# Project manager note — 30 Oct 2026

## Task 17 assigned to Dev: Technical SEO — schema, OG tags, Twitter cards, sitemap

**Goal:** Close four technical SEO gaps in the articles section before noindex tags come off at launch. The target audience (SEO agency leads) share articles on LinkedIn and Slack, and these are the pages most likely to earn backlinks and appear in AI search citations. Missing OG image and schema make them invisible in those contexts.

**Branch:** `week1/privacy-page` (continue on existing branch)

**Done when:**
- htmlhint and linkinator pass (run locally)
- Google Rich Results Test (https://search.google.com/test/rich-results) returns a valid Article result for each article, tested locally with `cd apps/web && python3 -m http.server 4321`
- All five changed files committed to `week1/privacy-page`
- QA tester (Quinn) signs off
- Note written to docs/status/YYYY-MM-DD-developer.md

---

## Gaps confirmed

All three article files and articles/index.html are missing:
- Schema.org JSON-LD
- og:image / og:image:width / og:image:height / og:image:alt
- twitter:card / twitter:image / twitter:title / twitter:description

The four article URLs are also absent from sitemap.xml.

Additional gap on index.html (homepage): og:image:alt is missing (og:image, og:image:width and og:image:height are already present).

---

## Work item 1: Article JSON-LD — three article files

Add two `<script type="application/ld+json">` blocks to each article `<head>`, after the existing meta tags.

### Block A — Article schema

**apps/web/articles/how-to-diagnose-google-search-console-traffic-drop.html**
```json
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "How to Diagnose a Google Search Console Traffic Drop (Step by Step)",
  "description": "A step-by-step checklist for diagnosing a Google Search Console traffic drop: which reports to open, in which order, and what each one tells you.",
  "datePublished": "2026-10-27",
  "dateModified": "2026-10-27",
  "author": { "@type": "Organization", "name": "Faevra", "url": "https://faevra.io/" },
  "publisher": {
    "@type": "Organization",
    "name": "Faevra",
    "url": "https://faevra.io/",
    "logo": { "@type": "ImageObject", "url": "https://faevra.io/favicon.svg", "width": 512, "height": 512 }
  },
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://faevra.io/articles/how-to-diagnose-google-search-console-traffic-drop" },
  "image": { "@type": "ImageObject", "url": "https://faevra.io/og.png", "width": 1200, "height": 630 }
}
```

**apps/web/articles/google-penalty-vs-algorithm-update-traffic-drop.html**
```json
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Google Penalty vs Algorithm Update vs Technical Issue: How to Tell Them Apart",
  "description": "How to correctly classify a traffic drop as a manual penalty, algorithm update or technical issue — because the diagnosis determines the fix.",
  "datePublished": "2026-10-27",
  "dateModified": "2026-10-27",
  "author": { "@type": "Organization", "name": "Faevra", "url": "https://faevra.io/" },
  "publisher": {
    "@type": "Organization",
    "name": "Faevra",
    "url": "https://faevra.io/",
    "logo": { "@type": "ImageObject", "url": "https://faevra.io/favicon.svg", "width": 512, "height": 512 }
  },
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://faevra.io/articles/google-penalty-vs-algorithm-update-traffic-drop" },
  "image": { "@type": "ImageObject", "url": "https://faevra.io/og.png", "width": 1200, "height": 630 }
}
```

**apps/web/articles/client-organic-traffic-drop-what-to-do.html**
```json
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "What to Do When a Client's Organic Traffic Drops: A Guide for SEO Agencies",
  "description": "A practical triage for SEO agencies: what to check, what to tell the client, and what not to do in the first 24 hours after a traffic drop.",
  "datePublished": "2026-10-27",
  "dateModified": "2026-10-27",
  "author": { "@type": "Organization", "name": "Faevra", "url": "https://faevra.io/" },
  "publisher": {
    "@type": "Organization",
    "name": "Faevra",
    "url": "https://faevra.io/",
    "logo": { "@type": "ImageObject", "url": "https://faevra.io/favicon.svg", "width": 512, "height": 512 }
  },
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://faevra.io/articles/client-organic-traffic-drop-what-to-do" },
  "image": { "@type": "ImageObject", "url": "https://faevra.io/og.png", "width": 1200, "height": 630 }
}
```

### Block B — BreadcrumbList (add to all three article files)

Position 3 name and item differ per article. Use a short title (under 50 characters) and the article's canonical URL.

```json
{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    { "@type": "ListItem", "position": 1, "name": "Home", "item": "https://faevra.io/" },
    { "@type": "ListItem", "position": 2, "name": "Articles", "item": "https://faevra.io/articles" },
    { "@type": "ListItem", "position": 3, "name": "[short article title]", "item": "[canonical URL]" }
  ]
}
```

Suggested short titles:
- Article 1: `Diagnose a Traffic Drop`
- Article 2: `Penalty vs Update vs Technical`
- Article 3: `When a Client's Traffic Drops`

---

## Work item 2: Schema for articles/index.html

Add one `<script type="application/ld+json">` block to articles/index.html `<head>`:

```json
{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    { "@type": "ListItem", "position": 1, "name": "Home", "item": "https://faevra.io/" },
    { "@type": "ListItem", "position": 2, "name": "Articles", "item": "https://faevra.io/articles" }
  ]
}
```

---

## Work item 3: OG image + Twitter card meta tags

### On all three article files and articles/index.html

Add after the existing `og:description` meta tag:

```html
<meta property="og:image" content="https://faevra.io/og.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="Faevra: plain-English Search Console traffic-drop reports">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:image" content="https://faevra.io/og.png">
<meta name="twitter:title" content="[copy the og:title value for this page]">
<meta name="twitter:description" content="[copy the meta description value for this page]">
```

og.png does not exist yet — the founder is creating it (spec below). Add the tags now so no further edits are needed once the file lands.

### On apps/web/index.html (homepage)

Add one line only — og:image:alt is missing. Insert immediately after the existing `og:image:height` line:

```html
<meta property="og:image:alt" content="Faevra: plain-English Search Console traffic-drop reports">
```

---

## Work item 4: sitemap.xml

Replace apps/web/sitemap.xml in full. Article URLs use extension-less paths to match their canonical tags. Privacy and terms keep .html to match how Cloudflare Pages will serve them. Do not change either pattern.

```xml
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url>
    <loc>https://faevra.io/</loc>
    <lastmod>2026-10-28</lastmod>
    <changefreq>weekly</changefreq>
    <priority>1.0</priority>
  </url>
  <url>
    <loc>https://faevra.io/articles</loc>
    <lastmod>2026-10-28</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.8</priority>
  </url>
  <url>
    <loc>https://faevra.io/articles/how-to-diagnose-google-search-console-traffic-drop</loc>
    <lastmod>2026-10-27</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.7</priority>
  </url>
  <url>
    <loc>https://faevra.io/articles/google-penalty-vs-algorithm-update-traffic-drop</loc>
    <lastmod>2026-10-27</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.7</priority>
  </url>
  <url>
    <loc>https://faevra.io/articles/client-organic-traffic-drop-what-to-do</loc>
    <lastmod>2026-10-27</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.7</priority>
  </url>
  <url>
    <loc>https://faevra.io/privacy.html</loc>
    <lastmod>2026-10-24</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.3</priority>
  </url>
  <url>
    <loc>https://faevra.io/terms.html</loc>
    <lastmod>2026-10-24</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.3</priority>
  </url>
</urlset>
```

---

## OG image spec — founder action, not a Dev task

Dev must not create or commit a placeholder image. The og.png must come from the founder. All meta tags referencing it go in now; the tags will resolve once the file exists.

| Property | Spec |
|---|---|
| File path | `apps/web/og.png` |
| Dimensions | **1200 × 630 px** |
| Aspect ratio | 1.91:1 (safe universal ratio across LinkedIn, X/Twitter, Slack, Facebook, Discord) |
| Format | **PNG** (lossless — required for text-heavy branded images; JPEG is for photographs) |
| Target file size | Under 1 MB (200–500 KB ideal). Platforms accept up to 5 MB but images over 1 MB load slowly on mobile feeds |
| Safe zone | Keep all text and the logo within the central **1140 × 580 px**. Treat the outer 30 px on every edge as potential crop zone — all platforms crop differently |
| Text | Faevra wordmark + short tagline. Main text element: minimum 60 px, weight 700+, maximum 40 characters. Use brand colours. Dark background recommended for contrast on social feeds |
| Alt text in meta | `Faevra: plain-English Search Console traffic-drop reports` |
| Export settings | 72 DPI, sRGB colour space |
| Tools | Canva, Figma, or similar |
| Delivery | Commit as `apps/web/og.png` to `week1/privacy-page` branch |

Source for specs: OG Image Size Guide 2026 (https://www.getrediate.com/blog/og-image-size-guide, as of 30 Oct 2026)

---

Mira · 30 Oct 2026
