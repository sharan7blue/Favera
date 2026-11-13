# Research: page-type loss grouper (free tool)

Analyst: research-analyst (Rhea). Date: 2026-11-13. Status: research only, nothing posted or published.

Access note: no Ahrefs, Semrush or Keyword Planner access, so search volumes and domain ratings are not verified. The git branch `week4/free-tool-page-type-grouper` does not exist (only `week1/*` refs are present), and this session cannot run git, so this note is written to the working tree for the caller to commit.

## 1. Search intent

Volumes are not verified. The phrases below are candidates; a keyword tool (open item on the board) must confirm them before copy is final.

| Candidate phrase | Intent | Volume | Source (opened, as-of) |
| --- | --- | --- | --- |
| how to diagnose google search console traffic drop | Investigate | Not checked | [Google guide](https://developers.google.com/search/docs/monitor-debug/debugging-search-traffic-drops?hl=en), last updated 2025-12-18 |
| find pages losing clicks in search console | Investigate | Not checked | [Pravin Kumar guide](https://www.pravinkumar.co/blog/find-pages-losing-clicks-in-search-console-2026), published 2026-10-05 |
| why did my organic traffic drop | Investigate | Not checked | [Seer Interactive](https://www.seerinteractive.com/blog/18-ways-to-diagnose-a-decline-in-organic-traffic/), updated May 2026 |
| compare date ranges search console | Set up a check | Not checked | Google guide above (compare last 3 months with previous 3) |
| client organic traffic drop what to do | Agency action | Not checked | Board task 14 brief, repo file docs/status/2026-10-27-seo-specialist.md (not reopened) |

Google's own guide breaks the drop down by query, page and other fields, but does not group pages by type. That supports the page-type step as a gap in the standard method.

## 2. Competitor free tools

DR and monthly traffic are not checked. Pricing and features are as stated on each page at the date shown.

| Tool | Link | What it does | Free? | Groups by URL pattern or type? | As-of |
| --- | --- | --- | --- | --- | --- |
| Swetrix GSC Export Analyzer | [link](https://swetrix.com/uk/tools/gsc-export-analyzer) | Browser-side analysis of GSC exports: declining pages, CTR gaps, cannibalisation | Yes; "results calculated locally in your browser" | Not described | Page undated; footer 2021-2026 |
| Apify Content Decay Audit | [link](https://apify.com/cygnix_labs/content-decay-audit) | Compares two Pages exports; labels pages LOST, DECAYING and so on | Partly: $1.00 per 1,000 pages, first 25 pages per run free; runs on Apify servers | Not described; merges URL variants only | Sample run 2026-10-20; page modified 2026-11-12 |
| SEOTesting Content Groups | [link](https://seotesting.com/content-groups/) | Groups by URL pattern, regex or query, pulled from a GSC account | 14-day free trial; no free tier shown | Yes (URL patterns) | Undated text |
| quickseo.ai Page Groups | [link](https://quickseo.ai/features/page-groups) | Groups by URL rules, shows clicks and impressions per group | Part of paid plan | Yes (URL rules); type not stated | © 2026 only |
| Coupler.io GSC Looker Studio template | [link](https://blog.coupler.io/content-grouping-for-search-console/) | Manual category sheet loaded into a dashboard | Free sign-up, no card; limits not stated | Manual categories, not patterns | Byline 2026-10-09 |

## 3. Positioning gap

URL-pattern grouping is not unoccupied. SEOTesting and quickseo.ai already do it, inside account-connected products that are free only as a trial or not at all. [Sitechecker](https://sitechecker.pro/en/google-search-console-dashboard/) also offers URL-rule segments, with no free tier shown (undated page).

The narrower position looks open: a free, browser-only, two-export before and after comparison that groups lost clicks by page type (article, campaign, product, other) and names the type that drove the drop. Swetrix is the closest free browser tool, but no page describes type grouping. The Apify tool compares two exports but runs on a server and charges per page.

Confidence: moderate. About eight searches and ten pages were opened. This is not an exhaustive market scan.

## 4. Recommended on-page copy

| Element | Copy | Length |
| --- | --- | --- |
| Page title | Free Search Console Page Type Grouper \| Faevra | 46 characters |
| Meta description | Upload two Search Console Pages exports to see which page type lost the clicks. Free, runs in your browser, no sign-up, no upload to any server. | 144 characters |
| h1 | Find which page type lost your clicks | |
| Subheading | Compare two Search Console Pages exports and group every URL as article, campaign, product or other, so you can see which group drove the drop. | One sentence |
| CTA label (to Tally) | Get the weekly report with full history | |

Caveats for the developer and QA: the copy claims "runs in your browser" and "no upload", so the build must match this. The Tally form KpY948 is still a draft (context.json), so the CTA must not go live until the founder publishes it.

## 5. Traffic angle

Recommendation: do not start a new article. Link the free tool from the existing draft apps/web/articles/how-to-diagnose-google-search-console-traffic-drop.html (repo file) as its main step, and make the tool page the target for the same investigative phrase.

Reason: the search phrase is already in the draft, the tool sits where the reader is already looking, and it costs nothing to build. A directory listing would need outside contact, which needs founder approval.

## Notes for the caller

- No memory was consulted: no memory tool was available in this session and no memory snapshot was attached.
- Nothing was posted, sent or published.
