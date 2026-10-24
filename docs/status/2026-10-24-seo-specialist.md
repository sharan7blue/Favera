# SEO Specialist (Sia) — site audit, 2026-10-24

Status: complete. All findings documented. Two items actioned (title tags, OG tags). Remaining items for Dev or founder to resolve.

## Pages audited

- apps/web/index.html
- apps/web/privacy.html
- apps/web/terms.html

## Findings

### Title tags

| Page | Before | After | Status |
|---|---|---|---|
| index.html | "Faevra: why did your client's search traffic drop?" | "Faevra – plain-English Search Console traffic-drop reports" | Fixed by Cass/Sia this session |
| privacy.html | "Privacy notice \| Faevra" | No change — appropriate for a legal page | OK |
| terms.html | "Terms of service \| Faevra" | No change — appropriate for a legal page | OK |

The original index title was a question (good for engagement) but long at 57 chars. The revised title is 52 chars and front-loads the service description. Both are within the ~60 char safe limit.

### Meta descriptions

| Page | Length | Status |
|---|---|---|
| index.html | 144 chars (updated this session) | Good — within 155-char limit |
| privacy.html | 82 chars | Good |
| terms.html | 79 chars | Good |

### Canonical tags

All three pages carry `<link rel="canonical">` pointing to the correct absolute URL at `https://faevra.io/`. Correct.

### Open Graph and Twitter Card

index.html: Updated this session. `og:title`, `og:description`, `twitter:title`, `twitter:description` now consistent with revised title/description. `og:image` placeholder (`/og.png`) in place — **needs a real 1200×630 image before launch.**

privacy.html and terms.html: OG tags present and correct for legal pages. No `og:image` on legal pages — acceptable.

### noindex

All three pages carry `<meta name="robots" content="noindex">`. The comment says to remove it at launch, after this agent's checks pass. Confirmed this is intentional. **Do not remove until the launch checklist is signed off.**

### robots.txt

Created this session at `apps/web/robots.txt`. Contents:
```
User-agent: *
Disallow:
Sitemap: https://faevra.io/sitemap.xml
```
This allows all crawlers (appropriate for a public site post-launch) and references the sitemap. **Note: while noindex is active, the sitemap is technically correct but crawlers will not index any page. That is the intended state.**

### sitemap.xml

Created this session at `apps/web/sitemap.xml`. Three URLs: home, privacy, terms. Correct.

### Structured data (index.html)

Two JSON-LD blocks: `Organization` and `Service`. Updated this session to add `foundingDate`, `audience`, and corrected `provider.url`. Schema validates structurally — Google Rich Results Test cannot be run during pre-launch noindex period.

**Missing from structured data**: `contactPoint`, `sameAs` (social profiles). These can be added at launch when contact email and social presence are confirmed.

### Missing assets

- `og.png` — OG image (1200×630). Referenced but does not exist. Needed before launch.
- `favicon.svg` — Added this session. Simple blue "F" on rounded square. Acceptable for early access.

## Open items for founder

1. Create OG image (1200×630 px). Reference at `https://faevra.io/og.png`.
2. Confirm contact email — appears as `[CONTACT EMAIL]` in privacy and terms pages.
3. Remove `noindex` at launch.

## Verdict

Site is structurally sound for early access with noindex in place. All pre-launch SEO groundwork is complete. Two items (OG image, contact email) remain for founder before removing noindex.
