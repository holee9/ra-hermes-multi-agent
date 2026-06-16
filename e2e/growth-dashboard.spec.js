// @ts-check
const { test, expect } = require('@playwright/test');
const path = require('path');
const { pathToFileURL } = require('url');

const DASHBOARD_URL = pathToFileURL(
  path.join(__dirname, '..', 'docs', 'growth-dashboard.html')
).href;

test.describe('growth dashboard', () => {
  test.beforeEach(async ({ page }) => {
    await page.goto(DASHBOARD_URL);
  });

  test('renders the static growth dashboard snapshot', async ({ page }) => {
    await expect(page.locator('h1')).toContainText('RA Hermes Growth Dashboard');
    await expect(page.locator('text=Readiness Matrix')).toBeVisible();
    await expect(page.locator('text=Agent Balance')).toBeVisible();
    await expect(page.locator('text=Latest Growth Metrics')).toBeVisible();
    await expect(page.locator('text=Growth Report Trend')).toBeVisible();
  });

  test('shows current readiness and timer status', async ({ page }) => {
    await expect(page.locator('.kpi').filter({ hasText: 'Readiness' })).toContainText('16/16');
    await expect(page.locator('.kpi').filter({ hasText: 'Auto Growth Timer' })).toContainText('inactive/disabled');
    await expect(page.locator('.kpi').filter({ hasText: 'Metrics Timer' })).toContainText('active/enabled');
  });
});
