// Faevra smoke tests — Playwright / Chromium
// Runs against http://localhost:4321 (served by playwright.config.js webServer).

const { test, expect } = require('@playwright/test');

// ── Homepage ──────────────────────────────────────────────────────────────────

test('homepage: loads with correct title', async ({ page }) => {
  await page.goto('/');
  await expect(page).toHaveTitle(/Faevra/);
});

test('homepage: exactly one h1', async ({ page }) => {
  await page.goto('/');
  await expect(page.locator('h1')).toHaveCount(1);
});

test('homepage: CTA button visible and links to Tally form', async ({ page }) => {
  await page.goto('/');
  const cta = page.locator('a.button').first();
  await expect(cta).toBeVisible();
  const href = await cta.getAttribute('href');
  expect(href).toMatch(/tally\.so/);
});

test('homepage: skip-to-content link present', async ({ page }) => {
  await page.goto('/');
  await expect(page.locator('.skip-link')).toHaveCount(1);
});

test('homepage: brand wordmark links to root', async ({ page }) => {
  await page.goto('/');
  const brand = page.locator('.brand a').first();
  await expect(brand).toBeVisible();
  const href = await brand.getAttribute('href');
  expect(href).toBe('/');
});

// ── Legal pages ───────────────────────────────────────────────────────────────

test('privacy page: loads and has h1', async ({ page }) => {
  const response = await page.goto('/privacy.html');
  expect(response?.status()).toBeLessThan(400);
  await expect(page).toHaveTitle(/Privacy/i);
  await expect(page.locator('h1')).toHaveCount(1);
});

test('terms page: loads and has h1', async ({ page }) => {
  const response = await page.goto('/terms.html');
  expect(response?.status()).toBeLessThan(400);
  await expect(page).toHaveTitle(/Terms/i);
  await expect(page.locator('h1')).toHaveCount(1);
});

// ── Internal navigation ───────────────────────────────────────────────────────

test('all internal links resolve without 4xx', async ({ page }) => {
  await page.goto('/');
  // Collect all href values as plain strings before any navigation.
  // Using live locator handles inside a navigation loop causes stale-element
  // timeouts because page.goto() replaces the DOM the locators reference.
  const hrefs = await page.$$eval('a[href]', as => as.map(a => a.getAttribute('href')));
  const checked = new Set();

  for (const href of hrefs) {
    if (!href || href.startsWith('http') || href.startsWith('#') || href.startsWith('mailto:')) continue;
    if (checked.has(href)) continue;
    checked.add(href);

    const response = await page.goto(href);
    expect(response?.status(), `${href} returned ${response?.status()}`).toBeLessThan(400);
  }
});

// ── Responsive layout ─────────────────────────────────────────────────────────

test('mobile (375 px): no horizontal overflow', async ({ page }) => {
  await page.setViewportSize({ width: 375, height: 812 });
  await page.goto('/');
  const overflow = await page.evaluate(
    () => document.body.scrollWidth > window.innerWidth
  );
  expect(overflow, 'Page has horizontal scroll at 375 px').toBe(false);
});

test('tablet (768 px): no horizontal overflow', async ({ page }) => {
  await page.setViewportSize({ width: 768, height: 1024 });
  await page.goto('/');
  const overflow = await page.evaluate(
    () => document.body.scrollWidth > window.innerWidth
  );
  expect(overflow, 'Page has horizontal scroll at 768 px').toBe(false);
});

// ── Keyboard accessibility ────────────────────────────────────────────────────

test('CTA is reachable by Tab key', async ({ page }) => {
  await page.goto('/');
  let found = false;
  for (let i = 0; i < 20; i++) {
    await page.keyboard.press('Tab');
    const focused = await page.evaluate(() => document.activeElement?.classList.contains('button'));
    if (focused) { found = true; break; }
  }
  expect(found, 'CTA button not reachable by keyboard').toBe(true);
});
