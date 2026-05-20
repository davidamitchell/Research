import { expect, test } from '@playwright/test';

async function countVisibleGraphPixels(page) {
  return page.locator('#graph-canvas').evaluate((canvas) => {
    const ctx = canvas.getContext('2d', { willReadFrequently: true });
    if (!ctx) return 0;
    const data = ctx.getImageData(0, 0, canvas.width, canvas.height).data;
    let colored = 0;
    for (let i = 0; i < data.length; i += 4) {
      const r = data[i];
      const g = data[i + 1];
      const b = data[i + 2];
      if (!(r === 10 && g === 15 && b === 24)) colored += 1;
    }
    return colored;
  });
}

test('graph stays visible after simulation settles', async ({ page }) => {
  await page.goto('/Research/graph.html');
  await expect(page.locator('#graph-canvas')).toBeVisible();
  await expect(page.locator('#graph-stats')).toContainText('nodes', { timeout: 30_000 });

  await page.waitForTimeout(2000);
  const earlyPixels = await countVisibleGraphPixels(page);
  await page.waitForTimeout(6000);
  const settledPixels = await countVisibleGraphPixels(page);

  expect(earlyPixels).toBeGreaterThan(200);
  expect(settledPixels).toBeGreaterThan(200);
});

test('search behavior is consistent between landing and search pages', async ({ page }) => {
  await page.goto('/Research/index.html');
  await page.locator('#landing-search').fill('gemini');
  await expect(page.locator('#landing-search-results .search-preview-item').first()).toBeVisible({
    timeout: 20_000,
  });
  const firstLandingTitle = await page
    .locator('#landing-search-results .search-preview-item span')
    .first()
    .innerText();

  await page.goto('/Research/search.html?q=gemini');
  await expect(page.locator('#search-results .card').first()).toBeVisible({ timeout: 20_000 });
  await expect(page.locator('#results-count')).not.toContainText('idle');
  const firstSearchTitle = await page.locator('#search-results .card .card-title').first().innerText();

  expect(firstSearchTitle).toBe(firstLandingTitle);
});
