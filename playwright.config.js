// @ts-check
const { defineConfig, devices } = require('@playwright/test');

module.exports = defineConfig({
  testDir: './tests',
  timeout: 30_000,
  retries: 0,
  workers: 1,

  use: {
    baseURL: 'http://localhost:4321',
    headless: true,
    screenshot: 'only-on-failure',
    trace: 'on-first-retry',
  },

  projects: [
    {
      name: 'chromium',
      use: { ...devices['Desktop Chrome'] },
    },
  ],

  // Starts the static server before any test and stops it after.
  webServer: {
    command: 'python3 -m http.server 4321 --directory apps/web',
    port: 4321,
    reuseExistingServer: false,
    timeout: 10_000,
  },
});
