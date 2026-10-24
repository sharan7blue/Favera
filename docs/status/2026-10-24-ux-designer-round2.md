# UX Designer (Uma) — session 2 audit, 2026-10-24

Status: complete. Patches applied to apps/web/styles.css and apps/web/index.html.

## Audit findings

### Accessibility
1. **Skip link**: present and functional. No change needed.
2. **Focus styles**: `focus-visible` outline was missing from `a` elements and `.brand a`. Fixed — added `a:focus-visible` rule and explicit `.brand a:focus-visible`.
3. **`<main>` landmark**: present on all three pages with `id` attributes. No change needed.
4. **`<section>` without label**: the `#example` placeholder section had no accessible name. Fixed — added `aria-label="Example report (coming soon)"`.
5. **Button colour contrast (light mode)**: `#1f5fd1` on white → 5.57:1 (passes WCAG AA). Dark mode: `#6a9bff` on `#0e0d0c` → checked passes. No change needed.
6. **Body text contrast**: `#1c1b19` on `#fbfaf8` → passes WCAG AAA. Dark: `#f1efea` on `#161513` → passes.

### Layout
7. **Header bottom padding**: none set; brand sat too close to hero h1. Fixed — added `padding-bottom: 8px` to `header.wrap`.
8. **Section top padding**: sections had a rule border but no top breathing room. Fixed — added `padding-top: 0.25rem`.
9. **Footer border**: footer had no visual separator. Fixed — added `border-top: 1px solid var(--rule)`.
10. **List items**: no `margin-bottom` on `li` in main content. Fixed — `section li { margin-bottom: 0.4rem }`.
11. **Button colour on link element**: `color` could be overridden by link cascade. Fixed — added `!important` guard on `.button` colour.
12. **Brand link on index.html**: header brand was a plain `<p>`, not a link back to home. Privacy and terms pages had `<a href="/">` on brand but index did not. Fixed — wrapped brand text in `<a href="/">` on index.html.

### Dark mode
13. **`--focus` token**: focus outlines used hard-coded `var(--text)` which passes in light but could conflict in dark. Added `--focus` token (same as `--accent` per scheme) so focus rings use the brand colour rather than the body text colour.
14. **`mark` element**: already had dark-mode override. No change.

### Mobile
15. **Button padding on mobile**: was 0.9rem 1.2rem, consistent with the updated default 0.75rem 1.4rem. No conflict.

## Files changed
- `apps/web/styles.css` — CSS tokens, focus styles, header/section/footer spacing, button colour guard, list spacing.
- `apps/web/index.html` — brand wrapped in `<a href="/">`, `#example` section aria-label added, `.note-cta` class removed (redundant), analytics comment format fixed.

## Passed to
developer (Dev) to review before Quinn's QA pass.
