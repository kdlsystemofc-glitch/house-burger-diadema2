// Uso: node scripts/shot.js [seletor-da-secao]  ->  screenshots/<id>-<w>.png e screenshots/full-<w>.png
// Opções: --widths=1440,390  --full-only
const { chromium } = require('playwright');
const path = require('path');
const fs = require('fs');
const ROOT = path.resolve(__dirname, '..');
const URL = require('url').pathToFileURL(path.join(ROOT, 'site', 'index.html')).href;
const OUT = path.join(ROOT, 'screenshots');
const args = process.argv.slice(2);
const opt = k => (args.find(a => a.startsWith(`--${k}=`)) || '').split('=')[1];
const sel = args.find(a => !a.startsWith('--'));
const widths = (opt('widths') || '1440,390').split(',').map(Number);
const HEIGHTS = { 2560: 1440, 1920: 1080, 1440: 900, 1366: 768, 1280: 720, 1024: 768, 768: 1024, 430: 932, 390: 844, 360: 740, 320: 568, 844: 390 };
(async () => {
  fs.mkdirSync(OUT, { recursive: true });
  const browser = await chromium.launch();
  for (const w of widths) {
    const page = await browser.newPage({ viewport: { width: w, height: HEIGHTS[w] || 900 } });
    await page.goto(URL, { waitUntil: 'networkidle' });
    await page.evaluate(async () => {
      document.querySelectorAll('img[loading=lazy]').forEach(i => { i.loading = 'eager'; });
      await Promise.all([...document.images].filter(i => !i.complete).map(i => new Promise(r => { i.onload = i.onerror = r; })));
      await document.fonts.ready;
    });
    await page.waitForFunction(() => [...document.images].every(i => i.complete && i.naturalWidth > 0), null, { timeout: 15000 });
    if (sel) {
      const el = await page.$(sel);
      if (!el) { console.error('seção não encontrada:', sel); process.exitCode = 1; }
      else {
        const name = sel.replace(/[^a-z0-9-]/gi, '');
        await el.scrollIntoViewIfNeeded(); await page.waitForTimeout(500);
        await el.screenshot({ path: path.join(OUT, `${name}-${w}.png`) });
        console.log('salvo', `screenshots/${name}-${w}.png`);
      }
    }
    await page.screenshot({ path: path.join(OUT, `full-${w}.png`), fullPage: true });
    console.log('salvo', `screenshots/full-${w}.png`);
    await page.close();
  }
  await browser.close();
})();
