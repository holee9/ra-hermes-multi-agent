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
    await expect(page.locator('h1')).toContainText('RA Growth Operations Dashboard');
    await expect(page.locator('.growth-summary')).toContainText('RA Growth Operations');
    await expect(page.locator('.growth-summary')).toContainText('성장 추세 미측정');
    await expect(page.locator('text=Mike / US FDA')).toBeVisible();
    await expect(page.locator('text=Theo / EU MDR')).toBeVisible();
    await expect(page.locator('text=Sam / MFDS')).toBeVisible();
    await expect(page.locator('text=Growth Signal Flow')).toBeVisible();
    await expect(page.locator('text=Growth Trend Verdict')).toBeVisible();
    await expect(page.locator('.kpi').filter({ hasText: 'Growth Trend Verdict' })).toContainText('측정 불충분');
    await expect(page.locator('text=Growth Evidence Radar')).toBeVisible();
    await expect(page.locator('text=Coverage Guard Basis')).toBeVisible();
    await expect(page.getByRole('heading', { name: 'Depth Proxy & Source Coverage' })).toBeVisible();
    await expect(page.locator('section').filter({ hasText: 'Coverage Guard Basis' })).toContainText('legacy_pre_activation_floor');
    await expect(page.locator('text=Readiness Matrix')).toBeVisible();
    await expect(page.getByRole('heading', { name: 'Growth Trend', exact: true })).toBeVisible();
    await expect(page.locator('text=Latest Growth Metrics')).toBeVisible();
    await expect(page.locator('text=Growth Report Trend')).toBeVisible();
  });

  test('shows current growth measurement and readiness status', async ({ page }) => {
    await expect(page.locator('.kpi').filter({ hasText: 'Readiness' })).toContainText('16/16');
    await expect(page.locator('.kpi').filter({ hasText: 'Metrics Collection' })).toContainText('active/enabled');
    await expect(page.locator('.kpi').filter({ hasText: 'Latest Growth Input' })).toContainText('0');
  });

  test('renders visual charts and status indicators', async ({ page }) => {
    await expect(page.locator('svg.radar')).toBeVisible();
    await expect(page.locator('.radar-fill')).toBeVisible();
    await expect(page.locator('.bar-fill').first()).toBeVisible();
    await expect(page.locator('.dot.ok').first()).toBeVisible();
    await expect(page.locator('svg.sparkline').first()).toBeVisible();
  });
});
