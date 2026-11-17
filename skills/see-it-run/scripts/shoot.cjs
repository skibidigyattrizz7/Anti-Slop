#!/usr/bin/env node
/* Open a page at phone and desktop size, save screenshots, and report what can be measured.

Usage:
  node shoot.cjs <url-or-html-file> [--out DIR] [--dark]
  node shoot.cjs --selftest

Prints a JSON report: page title, HTTP status, console errors, failed requests,
horizontal overflow, tap targets under 24 px (with the first few named), images with
no alt text. --dark renders the page with a dark colour-scheme preference.
Exit codes: 0 no problems, 1 problems found, 2 usage or setup error.

Needs Playwright with Chromium (npm i playwright && npx playwright install chromium).
It cannot judge whether the page looks good. Look at the screenshots for that.
*/
const fs = require('fs');
const os = require('os');
const path = require('path');

const SIZES = { phone: { width: 375, height: 812 }, desktop: { width: 1280, height: 800 } };

function toUrl(target) {
  if (/^https?:\/\//i.test(target) || target.startsWith('file://')) return target;
  const p = path.resolve(target);
  if (!fs.existsSync(p)) throw new Error('No such file: ' + p);
  return 'file://' + p;
}

async function shoot(target, outDir, dark = false) {
  let chromium;
  try { ({ chromium } = require('playwright')); }
  catch { throw new Error('Playwright is not installed. Run: npm i playwright && npx playwright install chromium'); }
  fs.mkdirSync(outDir, { recursive: true });
  const url = toUrl(target);
  const browser = await chromium.launch();
  const report = { url, screenshots: {}, views: {}, problems: [] };
  try {
    for (const [name, viewport] of Object.entries(SIZES)) {
      const page = await browser.newPage({ viewport, colorScheme: dark ? 'dark' : 'light' });
      const consoleErrors = [], failedRequests = [];
      page.on('console', m => { if (m.type() === 'error') consoleErrors.push(m.text().slice(0, 200)); });
      page.on('pageerror', e => consoleErrors.push(String(e).slice(0, 200)));
      page.on('requestfailed', r => failedRequests.push(r.url().slice(0, 200)));
      const res = await page.goto(url, { waitUntil: 'load', timeout: 30000 });
      await page.waitForTimeout(500);
      const m = await page.evaluate(() => {
        const visible = el => { const r = el.getBoundingClientRect(); return r.width > 0 && r.height > 0; };
        const targets = [...document.querySelectorAll('a, button, input, select, textarea, [role=button]')].filter(visible);
        const small = targets.filter(el => { const r = el.getBoundingClientRect(); return r.width < 24 || r.height < 24; });
        return {
          title: document.title,
          overflowPx: Math.max(0, document.documentElement.scrollWidth - window.innerWidth),
          smallTapTargets: small.length,
          smallTapTargetExamples: small.slice(0, 5).map(el => { const r = el.getBoundingClientRect(); return `<${el.tagName.toLowerCase()}> "${(el.innerText || el.getAttribute('aria-label') || '').trim().slice(0, 30)}" ${Math.round(r.width)}x${Math.round(r.height)}`; }),
          imagesWithoutAlt: [...document.images].filter(i => !i.hasAttribute('alt')).length,
        };
      });
      const file = path.join(outDir, name + '.png');
      await page.screenshot({ path: file, fullPage: true });
      report.screenshots[name] = file;
      report.views[name] = { status: res ? res.status() : null, ...m, consoleErrors, failedRequests };
      if (res && res.status() >= 400) report.problems.push(`${name}: HTTP ${res.status()}`);
      if (m.overflowPx > 0) report.problems.push(`${name}: page scrolls sideways by ${m.overflowPx}px`);
      if (consoleErrors.length) report.problems.push(`${name}: ${consoleErrors.length} console error(s)`);
      if (failedRequests.length) report.problems.push(`${name}: ${failedRequests.length} failed request(s)`);
      if (name === 'phone' && m.smallTapTargets) report.problems.push(`phone: ${m.smallTapTargets} tap target(s) under 24px`);
      if (m.imagesWithoutAlt) report.problems.push(`${name}: ${m.imagesWithoutAlt} image(s) with no alt text`);
      await page.close();
    }
  } finally { await browser.close(); }
  return report;
}

async function selftest() {
  const dir = fs.mkdtempSync(path.join(os.tmpdir(), 'shoot-'));
  const bad = path.join(dir, 'bad.html'), good = path.join(dir, 'good.html');
  fs.writeFileSync(bad, '<title>bad</title><div style="width:900px">wide</div><a href="#" style="font-size:8px">x</a><img src="data:,"><script>console.error("boom")</script>');
  fs.writeFileSync(good, '<title>good</title><meta name="viewport" content="width=device-width"><p>fine</p>');
  const b = await shoot(bad, path.join(dir, 'bad'));
  const g = await shoot(good, path.join(dir, 'good'));
  const has = s => b.problems.some(p => p.includes(s));
  if (!b.views.phone.smallTapTargetExamples.length) throw new Error('small tap target not named');
  if (!has('phone: page scrolls sideways') || !has('console error') || !has('no alt text')) throw new Error('bad page not flagged: ' + JSON.stringify(b.problems));
  if (g.problems.length) throw new Error('good page flagged: ' + JSON.stringify(g.problems));
  if (!fs.existsSync(b.screenshots.phone) || !fs.existsSync(g.screenshots.desktop)) throw new Error('screenshots missing');
  console.log('selftest ok');
}

(async () => {
  const args = process.argv.slice(2);
  try {
    if (args[0] === '--selftest') { await selftest(); return; }
    const i = args.indexOf('--out');
    const outDir = i >= 0 ? args.splice(i, 2)[1] : null;
    const d = args.indexOf('--dark');
    const dark = d >= 0 && args.splice(d, 1).length > 0;
    if (args.length !== 1) { console.error('Usage: node shoot.cjs <url-or-html-file> [--out DIR] [--dark]'); process.exit(2); }
    const report = await shoot(args[0], outDir || fs.mkdtempSync(path.join(os.tmpdir(), 'shots-')), dark);
    console.log(JSON.stringify(report, null, 2));
    process.exit(report.problems.length ? 1 : 0);
  } catch (e) { console.error(String(e.message || e)); process.exit(2); }
})();
