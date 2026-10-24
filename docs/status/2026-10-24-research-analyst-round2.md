# Board #7, round 2: UK SEO agency prospects (as of 2026-10-24)

Status: partial. 1 new verified agency out of the 20 asked for. Rows 9 to 15 re-checked (section 1). The original file, docs/status/2026-10-24-research-analyst.md, is unchanged; its rows 9 to 15 are marked by the verdicts below.

Method: each agency was checked by opening its own site and its Companies House (CH) record. Search snippets and directory listings were not used as sources. Directory employee bands were not used as sizes. "Size" means a headcount or team statement on the site, otherwise "unknown". No one has been contacted.

Limits met in this run: Chrome was not connected. Shell curl to CH and agency sites was refused by the proxy (403). Guessed URLs were refused by the fetch tool unless they appeared in a search result or a page already opened. Several sites blocked robots or returned server errors. The tool budget (60 calls) was nearly used up.

## 1. Rows 9 to 15 from docs/status/2026-10-24-research-analyst.md

| # | Name | Verdict | Evidence (CH record; site) | As of |
|---|---|---|---|---|
| 9 | Horizon Digital Agency Limited | Verified | CH 10036859: Active, Private limited Company, incorporated 2 March 2016, registered office 32 Turner Road, Leicester LE5 0QA. Site footer: "© 2024 — Horizon Digital Agency Limited | Registered Office: 32 Turner Rd, Leicester, LE5 0QA". Site gives no company number and no headcount. | 2026-10-24 |
| 10 | Pinnacle Internet Marketing Limited | Verified | CH 05685452: Active, Private limited Company, incorporated 24 January 2006, registered office Pimnet House, 25-27 Pantbach Road, Cardiff CF14 1TU. Site footer: "© Pinnacle Internet Marketing Ltd. 2026"; the site address matches CH. Site gives no company number. | 2026-10-24 |
| 11 | Semetrical Ltd | Verified, with caveat | CH 08728596: Active, Private limited Company, incorporated 11 October 2013, registered office 64 Southwark Bridge Road, London SE1 0AS. Site: "© 2026 Semetrical. All rights reserved." The site does not state "Ltd", and its address (124 City Road, London EC1V 2NX) differs from CH. Confirm the trading entity before any use. | 2026-10-24 |
| 12 | SDG New Media Ltd (trading as Figment Agency) | Verified | CH 05708841: Active, Private limited Company, incorporated 14 February 2006, registered office 1 Buckland's Wharf, Thames Side, Kingston upon Thames KT1 1TF. Site footer: "Company No. 5708841" and "Figment is a registered trademark of SDG New Media Ltd." | 2026-10-24 |
| 13 | SearchQuest Europe Ltd (trading as SQ Digital) | Verified | CH 06898297: Active, Private limited Company, incorporated 7 May 2009, registered office 80 Church Street, Lancaster LA1 1ET. Site footer: "© 2026 SearchQuest Europe Limited"; the site address matches CH. Site gives no company number and no headcount. | 2026-10-24 |
| 14 | Anicca Digital Ltd | Dropped (for now) | Site footer and contact page give "Anicca Digital Ltd", company number 06984338 and registered office 19 Warren Park Way, Enderby, Leicester LE19 4SA. The CH record could not be opened: three WebFetch attempts returned client errors. Re-check CH before use; the site states "a team of 15 specialists". | 2026-10-24 |
| 15 | PNdigital | Dropped | The site gives no legal name and no company number. "Ltd" appears only in third-party link URLs. Without a legal name there is nothing to match at CH. | 2026-10-24 |

## 2. New verified agencies (1 of 20 asked for)

| Name | Site | Company number | Size | Companies House link | Site source link | As of | Contact route |
|---|---|---|---|---|---|---|---|
| Blue Array Ltd | https://www.bluearray.co.uk/ | 09610441 | unknown (no headcount on site; "over a decade" of trading) | https://find-and-update.company-information.service.gov.uk/company/09610441 | https://www.bluearray.co.uk/ (footer: "© Copyright 2017 - 2026 Blue Array Ltd", company number 09610441) | 2026-10-24 | Site homepage; contact page URL not opened yet |

CH record for 09610441: Active, Private limited Company, incorporated 27 May 2015, registered office Work.Life Reading, The White Building, 33 King's Road, Reading RG1 3AR. The site lists Reading, London and Seville offices, and states SEO is its core service.

## 3. Dropped candidates (new)

- Artios (https://artios.io/): presents itself as a GEO agency, not an SEO agency. No legal name or company number on the site. Offices in New York, Florida and London.
- Passion Digital (https://www.passiondigital.co.uk/): no legal name or company number on the site. SEO is not a stated main service.
- UK Linkology (https://www.uklinkology.co.uk/): the site footer says it is "an Ology Holdings Limited company". CH 07802825 is UK LINKOLOGY LTD (Active, Private limited, incorporated 10 October 2011). The owner name does not match the CH name, so this is unresolved. Re-check which entity operates the site.
- Wildcat Digital (https://www.wildcatdigital.co.uk/, Sheffield): no legal name or company number on the site. "wildcat-digital-ltd" appears only in a LinkedIn URL.
- SEO Impact (https://www.seoimpact.co.uk/): footer has no "Ltd". Number NI678675 is a Northern Ireland format. The site says "You'll be working directly with me, not an outsourced team", which is the sole-trader pattern. Excluded.
- ClickSlice (https://www.clickslice.co.uk/seo-agency-liverpool/): footer gives "Company No. 10876199" and says "just over a dozen of us". The CH record could not be opened (client error), so it is unverified. Strong candidate; re-check first.
- Fly High Media (https://www.flyhighmedia.co.uk/seo-liverpool): no legal name or company number. Offices given as Manchester, Cheshire and the Wirral, against a Liverpool headline.
- Elite SEO Team Ltd (CH 15423566): dissolved 1 July 2025.
- SEO Agency Liverpool Limited (CH 15891941): dissolved 21 April 2026.
- Bulldog Digital Media (https://bulldogdigitalmedia.co.uk/seo-liverpool/): redirects to bulldogdigitalmedia.com. The redirect target was refused by the fetch tool, so it is not checked.
- Minty Digital (mintydigital.co.uk) and Improve My Search Ranking (improvemysearchranking.co.uk): redirect to .com domains. Not checked.
- Odyssey New Media, Absolute Digital Media: site fetch failed (server or client error).
- Searchmode, Growwwise, Re:signal: robots.txt disallows fetching.
- Herdl, Front Page Advantage, CreativeWeb, Geeky Tech, Passion-style directory names without a URL seen in this run: not fetched.

## 4. Next steps for the project manager

- Re-check ClickSlice (CH 10876199) and Anicca Digital (CH 06984338) when the CH tool is reachable. Either could be added.
- Resolve the UK Linkology owner name before using it.
- Find 19 more verified agencies. The remaining candidates need URLs that appear in search results or directory pages, since guessed URLs are refused in this tool.
- Row 11 (Semetrical) is verified only on name; confirm before use.
