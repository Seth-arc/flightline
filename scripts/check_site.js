// Run with the Playwright browser tool's run-code filename option against the local preview.
async (page) => {
  const base = new URL('/', page.url()).href;
  const assert = (condition, message) => { if (!condition) throw new Error(message); };
  await page.setViewportSize({ width: 1440, height: 1000 });
  await page.goto(base);
  assert(await page.title() === 'Flightline — Keep the thread', 'Page title');
  await page.getByRole('radio', { name: 'Shared change' }).click();
  assert(await page.locator('#shared-panel').isVisible(), 'Shared change panel');
  assert(!(await page.locator('#routine-panel').isVisible()), 'Inactive panel hidden');
  await page.getByRole('radio', { name: 'Shared change' }).press('ArrowRight');
  assert(await page.locator('#resume-panel').isVisible(), 'Arrow-key scenario selection');
  await page.getByRole('radio', { name: 'Resume work' }).press('Home');
  assert(await page.locator('#routine-panel').isVisible(), 'Home-key scenario selection');
  const theme = page.getByRole('button', { name: 'Dark appearance' });
  await theme.click();
  const selectedTheme = await page.locator('html').getAttribute('data-theme');
  await page.reload();
  assert(await page.locator('html').getAttribute('data-theme') === selectedTheme, 'Theme persists');
  await page.evaluate(() => Object.defineProperty(navigator, 'clipboard', { configurable: true, value: { writeText: async text => { window.copiedPrompt = text; } } }));
  await page.getByRole('button', { name: 'Copy prompt' }).click();
  await page.waitForFunction(() => document.querySelector('#copy-status').textContent.includes('Prompt copied'));
  assert((await page.evaluate(() => window.copiedPrompt)).includes('$flightline'), 'Prompt copied');
  await page.evaluate(() => Object.defineProperty(navigator, 'clipboard', { configurable: true, value: { writeText: async () => { throw new Error('Unavailable'); } } }));
  await page.getByRole('button', { name: 'Copy prompt' }).click();
  await page.waitForFunction(() => document.querySelector('#copy-status').textContent.includes('Clipboard unavailable'));
  assert((await page.evaluate(() => window.getSelection().toString())).includes('$flightline'), 'Clipboard fallback selects prompt');
  const download = await page.request.get(new URL('downloads/flightline-0.1.0.zip', base).href);
  assert(download.ok() && (await download.body()).subarray(0, 2).toString() === 'PK', 'Real ZIP download');
  await page.emulateMedia({ reducedMotion: 'reduce', colorScheme: 'dark' });
  assert(await page.evaluate(() => window.Settle.reduced()), 'Reduced motion honored');
  for (const width of [320, 390, 768, 1440]) {
    await page.setViewportSize({ width, height: 900 });
    assert(await page.evaluate(() => document.documentElement.scrollWidth <= window.innerWidth), `No overflow at ${width}`);
  }
  const noJs = await page.context().browser().newContext({ javaScriptEnabled: false, viewport: { width: 390, height: 844 } });
  try {
    const fallback = await noJs.newPage();
    await fallback.goto(base);
    assert(await fallback.locator('#resume-panel').isVisible(), 'All scenario content available without JavaScript');
    assert(!(await fallback.locator('#copy-prompt').isVisible()), 'Unavailable copy action hidden without JavaScript');
    assert(await fallback.getByRole('link', { name: 'Download the skill' }).isVisible(), 'Download available without JavaScript');
  } finally { await noJs.close(); }
  await page.emulateMedia({ reducedMotion: 'no-preference', colorScheme: 'light' });
  await page.evaluate(() => { localStorage.removeItem('flightline-theme'); });
  await page.goto(base);
  return 'PASS: scenarios, keyboard navigation, theme persistence, clipboard success/fallback, ZIP download, reduced motion, responsive widths, and no-JavaScript content.';
}
