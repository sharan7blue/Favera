---
name: qa-tester-round4
description: Quinn QA — end-of-session-3 pre-launch audit
sources: [cowork]
---

# QA tester — round 4 (2026-10-24, end of session 3)

Agent: qa-tester (Quinn). Status: pass with noted blockers.

## Checks run

### Placeholder scan (check_placeholders.py --strict)
Exit code: 1 (expected — all 6 warnings are [CONFIRM] marks that require founder input before launch)
- privacy.html line 59: cookies check
- privacy.html line 91: Cloudflare data and country
- privacy.html line 92: Google Workspace data and country
- privacy.html line 93: Tally data and country re-verify
- terms.html line 56: pricing, payment terms and refund policy
- terms.html line 59: liability cap

These are launch-gate items, not bugs. `--strict` is expected to fail until the founder clears them.

### HTML structural checks
- Heading hierarchy: one h1 per page, no skipped levels. PASS.
- Canonical link: present on all three pages. PASS.
- lang="en-GB": set on all three pages. PASS.
- noindex meta: present on all three pages (correct for pre-launch). PASS.

### Internal link resolution
- index.html: /favicon.svg ✓, /privacy.html ✓, /terms.html ✓
- privacy.html: /favicon.svg ✓, /terms.html ✓
- terms.html: /favicon.svg ✓, /privacy.html ✓

### Skip links
- index.html: `.skip-link` present, target `#main-content` present. PASS.
- privacy.html: `.skip-link` present, target `#main` present. PASS.
- terms.html: `.skip-link` present, target `#main` present. PASS.

### Analytics beacon
- All three pages: beacon script is commented out (correct — REPLACE_WITH_CF_ANALYTICS_TOKEN placeholder would send invalid requests). PASS.

### Structured data (index.html)
- Organization schema: present. PASS.
- Service schema: present (added by Sia, SEO round 2). PASS.
- Validation blocked until live URL — Google Rich Results Test must run post-push.

### OG tags
- index.html: full set (type, site_name, locale, url, title, description, image). PASS.
- privacy.html: full set added by Sia. PASS.
- terms.html: full set added by Sia. PASS.

### Dark mode
- CSS mark rule: dark variant present (`#4a3800 / #ffe58a`). PASS.
- styles.css: no duplicate rules (Uma cleaned them up). PASS.

## Blockers (require founder action before launch)

1. Resolve all 6 [CONFIRM] marks in privacy.html and terms.html.
2. Set [CONTACT EMAIL] in privacy.html (3 occurrences) and terms.html (2 occurrences).
3. Set [LAST UPDATED DATE] in privacy.html and terms.html.
4. Create Cloudflare Pages project → get real analytics token → uncomment beacon on all three pages.
5. Publish Tally form KpY948.
6. Set up Faevra email mailbox (hello@faevra.io or similar).
7. Create og.png (1200 × 630) at faevra.io/og.png.
8. After all above, run htmlhint (in CI) and linkinator to catch any remaining issues.
9. Run Google Rich Results Test on live URL.
10. Flip noindex: remove the noindex meta tag from all three pages.

## Not blocked / not run

- htmlhint: npm registry unreachable in this container; CI must run it.
- linkinator: same block.
- Manual browser test: recommend founder loads pages in light and dark mode, checks skip link with Tab key.

## Summary for project manager

End-of-session-3 QA complete. All structural checks pass. The 6 [CONFIRM] placeholder warnings are expected launch-gate items. Internal links resolve. Skip links target correct IDs. Analytics beacon is safely commented out. Structured data and OG tags are complete across all three pages. Ten founder-action items remain before the noindex flip; none are blockers for the GitHub push (which is itself blocked by the GitHub App install, tracked as task 23).
