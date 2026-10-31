# CI Guardrails Pipeline

Date: 2026-10-31
Status: Implemented on branch week1/ci-pipeline

## Context

The previous CI was a single flat job: htmlhint, linkinator, validate_agents, check_placeholders. Adequate for a scaffold, not adequate for a product that sells quality assurance to SEO agencies.

Every claim Faevra makes about a client's site will be judged against Faevra's own site. If faevra.io has a missing alt attribute, a colour-contrast failure, or an OG image that does not exist, a competitor or sceptical client will find it. The CI pipeline is the first and cheapest place to catch this.

## Decision

Expand CI into a multi-stage guardrails pipeline. Every PR to main must pass all gates. No exceptions.

## Stages

### 1. Code quality (retained from week 1)
HTML lint, local link check, agent file validation, placeholder warnings.

### 2. Accessibility — WCAG 2.1 AA
pa11y-ci runs against every page served from localhost. Fails on any WCAG 2.1 AA violation.

Rationale: accessibility is a ranking signal (Core Web Vitals, usability), a legal obligation in the UK under the Equality Act 2010, and a basic professional standard. Faevra cannot advise agencies on traffic without holding its own pages to that standard.

### 3. SEO and metadata
Validates: title length (10-60 chars), meta description (50-160 chars), canonical tag, one h1 per page, OG tags on index (og:title, og:description, og:image, og:url), sitemap.xml exists, robots.txt exists.

Rationale: the product is Search Console analysis. Every page must pass the same checks Faevra flags for clients.

### 4. Image standards
Validates: every img has alt text, OG image file exists at the path referenced, width and height attributes present (warned if missing — affects CLS).

Rationale: Google image search, Core Web Vitals (CLS), and client credibility. A missing OG image is invisible to users until someone shares a link.

### 5. Playwright smoke tests
Headless Chromium, running against localhost: homepage loads, one h1, CTA visible and links to Tally form, privacy and terms pages load, no horizontal scroll at 375 px and 768 px viewports, skip link present, all internal links resolve, CTA reachable by Tab key.

Runs only after accessibility, SEO and image gates all pass.

## Future roadmap (not in this PR)

- Post-merge Lighthouse run against Cloudflare Pages preview URL once Pages is live. Track Performance, Accessibility, Best Practices, SEO scores. Flag if Performance < 90 or Accessibility < 95.
- schema.org/ImageObject on every editorial image (filename, alt, dimensions in structured data).
- Video SEO: schema.org/VideoObject with thumbnail, duration, upload date when Faevra publishes video content.
- Core Web Vitals: scheduled weekly Lighthouse run tracking LCP, CLS, INP over time. Posted to board.md.
- Google Discover eligibility: max-image-preview large meta tag, hero images >= 1200 px.
- Keyword mapping script: target keyword list checked against page copy and meta on every PR.

## Consequences

- PRs take approximately 3-4 minutes to pass CI instead of 30 seconds.
- All new pages must have alt text, canonical, OG tags and meta description before merge.
- og.png must be committed to the repo before any page referencing it can pass the image-standards gate.
