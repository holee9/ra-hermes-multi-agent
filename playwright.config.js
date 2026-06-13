// @ts-check
const { defineConfig, devices } = require('@playwright/test');
const fs = require('fs');

const launchOptions = {
  args: ['--no-sandbox', '--disable-setuid-sandbox'],
};

const chromiumExecutable = process.env.PLAYWRIGHT_CHROMIUM_EXECUTABLE
  || ['/usr/bin/chromium', '/usr/bin/chromium-browser', '/snap/bin/chromium'].find((candidate) => fs.existsSync(candidate));

if (chromiumExecutable) {
  launchOptions.executablePath = chromiumExecutable;
}

module.exports = defineConfig({
  testDir: './e2e',
  timeout: 10000,
  retries: 1,
  reporter: [['list']],
  outputDir: 'e2e/test-results',

  use: {
    headless: true,
    launchOptions,
  },

  projects: [
    {
      name: 'chromium',
      use: { ...devices['Desktop Chrome'] },
    },
  ],
});
