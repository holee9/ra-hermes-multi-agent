// @ts-check
const { test, expect } = require('@playwright/test');
const path = require('path');
const { pathToFileURL } = require('url');

const HTML_URL = pathToFileURL(
  path.join(__dirname, '..', 'virtual-office', 'virtual-office.html')
).href;

// ──────────────────────────────────────────────────────────────
// Suite 1: 초기 로드 (Initial Load)
// ──────────────────────────────────────────────────────────────
test.describe('초기 로드', () => {
  test.beforeEach(async ({ page }) => {
    // Silence expected fetch errors for /api/config (file:// context)
    page.on('pageerror', () => {});
    await page.goto(HTML_URL);
    // Pause auto-play immediately so tests are not disturbed by running events
    await page.click('#pause');
  });

  test('should display title and subtitle', async ({ page }) => {
    await expect(page.locator('h1')).toContainText('RA VIRTUAL OFFICE');
    await expect(page.locator('.sub')).toBeVisible();
  });

  test('should render 8 characters with names', async ({ page }) => {
    const names = ['Mike', 'Theo', 'Sam', 'Margot', 'Olly', 'Finn', 'Leo', 'Gus'];
    for (const name of names) {
      await expect(page.locator('.namep', { hasText: name }).first()).toBeVisible();
    }
  });

  test('should render control buttons', async ({ page }) => {
    await expect(page.locator('#play')).toBeVisible();
    await expect(page.locator('#pause')).toBeVisible();
    await expect(page.locator('#reset')).toBeVisible();
  });

  test('should render kanban columns', async ({ page }) => {
    const columns = ['오픈', '진행중', '리뷰중', '완료'];
    for (const col of columns) {
      await expect(page.locator('#kanban .kcol .t', { hasText: col })).toBeVisible();
    }
  });

  test('should render two room sections', async ({ page }) => {
    await expect(page.locator('.room.work')).toBeVisible();
    await expect(page.locator('.room.infra')).toBeVisible();
  });
});

// ──────────────────────────────────────────────────────────────
// Suite 2: 재생 컨트롤 (Playback Controls)
// ──────────────────────────────────────────────────────────────
test.describe('재생 컨트롤', () => {
  test.beforeEach(async ({ page }) => {
    page.on('pageerror', () => {});
    await page.goto(HTML_URL);
    // Stop any auto-play that may have started
    await page.click('#pause');
    // Reset to clean state
    await page.click('#reset');
  });

  test('should start playing when play button clicked', async ({ page }) => {
    // Set to fastest speed so events fire quickly within timeout
    await page.selectOption('#speed', '450');
    await page.click('#play');
    await page.waitForTimeout(1000);
    const logChildren = await page.locator('#log > div').count();
    expect(logChildren).toBeGreaterThanOrEqual(1);
  });

  test('should stop playing when pause button clicked', async ({ page }) => {
    await page.selectOption('#speed', '900');
    await page.click('#play');
    await page.waitForTimeout(500);
    await page.click('#pause');
    const countBefore = await page.locator('#log > div').count();
    // Wait longer than one interval — no new entries should appear (allow 1 race-condition entry)
    await page.waitForTimeout(1500);
    const countAfter = await page.locator('#log > div').count();
    expect(countAfter).toBeLessThanOrEqual(countBefore + 1);
  });

  test('should reset on reset button click', async ({ page }) => {
    await page.selectOption('#speed', '450');
    await page.click('#play');
    await page.waitForTimeout(1500);
    await page.click('#reset');
    // Log must be empty
    await expect(page.locator('#log')).toHaveText('');
    // No kanban cards
    const cardCount = await page.locator('#kanban .kcard').count();
    expect(cardCount).toBe(0);
  });
});

// ──────────────────────────────────────────────────────────────
// Suite 3: 이벤트 재생 & 캔반 (Event Replay & Kanban)
// ──────────────────────────────────────────────────────────────
test.describe('이벤트 재생 & 캔반', () => {
  test.beforeEach(async ({ page }) => {
    page.on('pageerror', () => {});
    await page.goto(HTML_URL);
    await page.click('#pause');
    await page.click('#reset');
  });

  test('should show WP-204 kanban card after events play', async ({ page }) => {
    // Use 3x speed (450ms per event). 12 events * 450ms = ~5400ms; add buffer
    await page.selectOption('#speed', '450');
    await page.click('#play');
    // Wait for all 12 mock events to complete (with generous buffer)
    await page.waitForTimeout(8000);
    // WP-204 card: event 6 is matched(ra_eu, WP-204, existing:false) → addKanbanCard("WP-204","오픈")
    // then comment_added → moveKanban to "진행중"
    const card = page.locator('#kanban .kcard[data-wp="WP-204"]');
    await expect(card).toBeVisible();
  });

  test('should log events in activity log', async ({ page }) => {
    await page.selectOption('#speed', '450');
    await page.click('#play');
    await page.waitForTimeout(8000);
    const logCount = await page.locator('#log > div').count();
    expect(logCount).toBeGreaterThan(5);
  });
});

// ──────────────────────────────────────────────────────────────
// Suite 4: 속도 변경 (Speed Change)
// ──────────────────────────────────────────────────────────────
test.describe('속도 변경', () => {
  test.beforeEach(async ({ page }) => {
    page.on('pageerror', () => {});
    await page.goto(HTML_URL);
    await page.click('#pause');
    await page.click('#reset');
  });

  test('should change playback speed', async ({ page }) => {
    // At 3x speed (450ms/event), we expect more log entries in 3s than at default 1.6x (900ms/event)
    // First measure at 1.6x speed
    await page.selectOption('#speed', '900');
    await page.click('#play');
    await page.waitForTimeout(3000);
    await page.click('#pause');
    const slowCount = await page.locator('#log > div').count();

    // Reset and measure at 3x speed
    await page.click('#reset');
    await page.selectOption('#speed', '450');
    await page.click('#play');
    await page.waitForTimeout(3000);
    await page.click('#pause');
    const fastCount = await page.locator('#log > div').count();

    // 3x speed should produce at least as many entries as 1.6x in the same window
    expect(fastCount).toBeGreaterThanOrEqual(slowCount);
  });
});
