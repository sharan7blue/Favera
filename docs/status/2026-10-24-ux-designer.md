# UX review: apps/web (2026-10-24)

Scope: `apps/web/index.html`, `apps/web/styles.css`. Rendered with Playwright/Chromium at 360 and 1280 px, light and dark; screenshots in `/tmp/ux/` (`360-light.png`, `360-dark.png`, `1280-light.png`, `1280-dark.png`). Contrast ratios computed from the CSS tokens on 2026-10-24 (WCAG 2.x relative luminance). Nothing in `apps/web` was edited.

## Result: no blockers. Passes below, then 7 fixes.

| Check | Result |
| --- | --- |
| Contrast, body text | light 16.5:1, dark 15.9:1 (AA needs 4.5) |
| Contrast, `.note` (--quiet) | light 6.8:1, dark 7.4:1 |
| Contrast, button label on accent | light 5.8:1, dark 7.2:1 |
| Button vs page (non-text, needs 3) | light 5.6:1, dark 6.7:1 |
| Focus outline (--text on --bg) | 16.5:1 light, 15.9:1 dark |
| Horizontal scroll at 360 px | none (scrollWidth 360) |
| Heading order | h1, then four h2s, no skips |
| Landmarks | header, main, footer present; one h1 |
| Tap target | button 212 x 50 px (min 44) |
| Hairline rules (1.26:1) | decorative only, acceptable |

## Fixes, by impact

1. **Primary link is a placeholder.** `href="https://tally.so/r/REPLACE_ME"` (index.html line 22) is the only call to action and goes nowhere. Blocked on board task 5; developer to swap in the published Tally URL before the link is shared. No CSS change.

2. **Button has no hover or active state; mobile reach.** Add to styles.css:
```css
.button:hover { filter: brightness(1.08); }
.button:active { transform: translateY(1px); }
@media (max-width: 480px) {
  .button { display: block; text-align: center; padding: 0.9rem 1.2rem; }
}
```
Full-width on phones gives a thumb-sized target and keeps the CTA visible above the note.

3. **Declare both colour schemes** so scrollbars and form controls (the later Tally embed or any inputs) match dark mode. Add to `:root`:
```css
:root { color-scheme: light dark; }
```

4. **Keep keyboard focus visible on the button against its own fill.** The 3px `--text` outline works, but make it robust when the accent changes:
```css
.button:focus-visible { outline: 3px solid var(--text); outline-offset: 3px; }
```
Also add a skip link only if navigation is added later (not needed with one header line).

5. **Hero rhythm at 360 px.** h1 at 2.1rem (33.6 px) is fine but the 2.5rem top margin plus 24px header padding pushes the CTA lower than needed. Tighten on small screens:
```css
@media (max-width: 480px) {
  h1 { font-size: 1.9rem; margin-top: 1.75rem; text-wrap: balance; }
  h2 { margin-top: 2rem; }
}
```
Rationale: an agency reader should see the headline and the button without scrolling on a small phone.

6. **Prevent orphaned last words in headings and the lead.**
```css
h1, h2 { text-wrap: balance; }
.lead { text-wrap: pretty; }
```

7. **Make the brand a link to the top once more pages exist** (privacy page is board task 8). Then: `<p class="brand"><a href="/">Faevra</a></p>` and `.brand a { color: inherit; text-decoration: none; }`. Not needed while the site is one page.

## Notes for later (not now)
- When the example report is added, use real `<table>` markup with `<th scope>`, and keep body text at 17 px or above on mobile.
- Links in body copy (privacy, terms) will need an underline; the global `a` style currently has none beyond the browser default, which is fine.
- Copy is Cass's remit; no copy changes proposed.
