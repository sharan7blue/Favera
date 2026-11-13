# Developer note — 13 November 2026

## Task
Build the free tool: page-type loss grouper at `apps/web/tools/page-type-grouper.html` on branch `week4/free-tool-page-type-grouper`.

## What was built

A single self-contained HTML file. No external scripts or stylesheets are loaded at runtime except the Google Fonts stylesheet (same fonts already used in `styles.css`). All CSS and JavaScript are inline.

**What the tool does:**
- Accepts two Google Search Console "Pages" CSV exports via file input or drag-and-drop (before period and after period).
- Parses the CSV entirely in the browser — no data leaves the machine.
- Groups URLs into four types (article, campaign, product, other) using the first-match rule set in the brief.
- Shows a headline sentence naming the worst-performing type and the click loss.
- Renders a summary table sorted by change (biggest loss first), with columns: page type, pages affected, clicks before, clicks after, change, share of total loss.
- Shows a custom-pattern text input (and Re-analyse button) when the "other" row's absolute click loss exceeds 20% of the total loss. Re-analysis adds the entered segment as a fifth type.
- CTA link to `https://tally.so/r/KpY948` at the bottom.

**Design:** matches the existing site — same CSS custom properties, same dark/light colour scheme, same DM Serif Display / DM Sans font stack, same `.button` style.

**Accessibility:** one `h1`, semantic `<section>` elements, visible keyboard focus on all interactive elements, `aria-live` on results and error regions, skip link, explicit `type="button"` on all `<button>` elements.

**SEO:** `<meta name="robots" content="noindex">`, correct `<meta name="description">`, title tag `Traffic Drop Analyser — Faevra`.

## Checks

- **validate_agents:** pass (10 agents valid).
- **check_placeholders --strict:** fails due to 6 pre-existing `[CONFIRM]` markers in `privacy.html` and `terms.html`. The new file is in `apps/web/tools/` which the script's glob (`apps/web/*.html`) does not scan. The new file contains no placeholders.
- **htmlhint / linkinator:** npm packages could not be installed — no outbound access to registry.npmjs.org (confirmed via proxy status). Manual equivalents run in Python:
  - HTML structure: valid doctype, charset, title, no uppercase tags, no duplicate IDs, all buttons have explicit `type`, no unescaped `&` in HTML attribute values.
  - Internal links (`/favicon.svg`, `/`, `/privacy.html`, `/terms.html`): all resolve on disk.

## Decisions

- Used `@import` approach would match styles.css but since this is a standalone file, chose `<link rel="stylesheet">` with properly escaped `&amp;` in the Google Fonts URL.
- No `<link rel="canonical">` added — page is noindexed and not yet public.

## Status
PR open. QA to verify acceptance criteria.
