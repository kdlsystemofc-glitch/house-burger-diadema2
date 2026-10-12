// CHECK-SEÇÃO mecânico. Uso: node scripts/check-section.js
const { chromium } = require('playwright');
const path = require('path');
const fs = require('fs');
const ROOT = path.resolve(__dirname, '..');
const SITE = path.join(ROOT, 'site');
const URL = require('url').pathToFileURL(path.join(ROOT, 'site', 'index.html')).href;
const results = [];
const report = (name, ok, info = '') => results.push({ name, ok, info });

function walk(dir) {
  return fs.readdirSync(dir, { withFileTypes: true }).flatMap(d =>
    d.isDirectory() ? walk(path.join(dir, d.name)) : [path.join(dir, d.name)]);
}
const textFiles = walk(SITE).filter(f => /\.(html|css|js|json|svg|txt|xml|webmanifest)$/i.test(f));
const read = f => fs.readFileSync(f, 'utf8');

// 1. nenhuma referência a "design/"
const designRefs = textFiles.filter(f => /design\//.test(read(f)));
report('sem referência a design/', designRefs.length === 0, designRefs.join(', '));

// 2. nenhum max-width em px em html, body, main ou wrapper global
const bad = [];
for (const f of textFiles.filter(f => f.endsWith('.css'))) {
  const css = read(f).replace(/\/\*[\s\S]*?\*\//g, '');
  for (const m of css.matchAll(/([^{}]+)\{([^{}]*)\}/g)) {
    const selectors = m[1].split(',').map(s => s.trim());
    const globalSel = selectors.some(s => /^(html|body|main|:root)$|wrapper|container|^\.page$|^\.site$/i.test(s));
    if (globalSel && /max-width\s*:\s*[^;]*\d+px/i.test(m[2])) bad.push(`${path.basename(f)}: ${m[1].trim()}`);
  }
}
report('sem max-width px em html/body/main/wrapper', bad.length === 0, bad.join('; '));

// 3. sem lorem/ipsum
const lorem = textFiles.filter(f => /lorem|ipsum/i.test(read(f)));
report('sem lorem/ipsum', lorem.length === 0, lorem.join(', '));

(async () => {
  const browser = await chromium.launch();
  const norm = s => s.replace(/\s+/g, ' ').trim().toLowerCase();
  const cliente = norm(read(path.join(ROOT, 'CLIENTE.MD')));
  const allow = new Set(JSON.parse(read(path.join(__dirname, 'microcopy.json'))).allow.map(norm));
  for (const w of [1440, 390]) {
    const page = await browser.newPage({ viewport: { width: w, height: w > 500 ? 900 : 844 } });
    const errors = [];
    page.on('pageerror', e => errors.push(e.message));
    page.on('console', m => { if (m.type() === 'error') errors.push(m.text()); });
    await page.goto(URL, { waitUntil: 'networkidle' });
    await page.evaluate(() => document.fonts.ready);
    // 4. scrollWidth <= viewport
    const sw = await page.evaluate(() => [document.documentElement.scrollWidth, window.innerWidth]);
    report(`scrollWidth <= viewport @${w}`, sw[0] <= sw[1], `${sw[0]} / ${sw[1]}`);
    report(`console sem erros @${w}`, errors.length === 0, errors.join(' | '));
    if (w === 1440) {
      // 5. todo texto visível existe em CLIENTE.MD, na lista de microcopy ou está marcado como PENDÊNCIA
      const texts = await page.evaluate(() => {
        const out = [];
        const tw = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT);
        while (tw.nextNode()) {
          const n = tw.currentNode, t = n.textContent.trim();
          if (!t) continue;
          const el = n.parentElement;
          if (el.closest('script,style,noscript,template,[data-pendencia]')) continue;
          const cs = getComputedStyle(el);
          if (cs.display === 'none' || cs.visibility === 'hidden') continue;
          out.push(t);
        }
        return out;
      });
      const orphan = texts.filter(t => { const n = norm(t); return !(allow.has(n) || cliente.includes(n)); });
      report('texto visível vem de CLIENTE.MD / microcopy / PENDÊNCIA', orphan.length === 0, orphan.map(t => `"${t}"`).join(', '));
    }
    await page.close();
  }
  await browser.close();
  for (const r of results) console.log(`${r.ok ? 'OK     ' : 'FALHOU '} ${r.name}${r.info ? '  -> ' + r.info : ''}`);
  process.exitCode = results.every(r => r.ok) ? 0 : 1;
})();
