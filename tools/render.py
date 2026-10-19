#!/usr/bin/env python3
"""Render a page at 1280 px and 375 px, report horizontal overflow, save screenshots.

    python3 tools/render.py               # index.html
    python3 tools/render.py translate.html

Exit 0: rendered, no overflow at either width. Exit 1: overflow.
Exit 2: Playwright/Chromium not available — the check is NOT RUN, not passed.
Screenshots go to $TMPDIR (outside the repo); their paths are printed. Look at them.
"""
import os, sys, tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
page = sys.argv[1] if len(sys.argv) > 1 else "index.html"
path = os.path.join(ROOT, page)
try:
    from playwright.sync_api import sync_playwright
except ImportError:
    print("NOT RUN  render — playwright missing (pip install playwright && playwright install chromium)")
    sys.exit(2)
out = tempfile.mkdtemp(prefix="site-render-")
bad = 0
try:
    with sync_playwright() as p:
        b = p.chromium.launch()
        for w, name in ((1280, "desktop"), (375, "mobile")):
            pg = b.new_page(viewport={"width": w, "height": 900})
            pg.goto("file://" + path)
            pg.wait_for_timeout(800)
            sw = pg.evaluate("document.documentElement.scrollWidth")
            shot = os.path.join(out, f"{os.path.splitext(page)[0]}-{name}.png")
            pg.screenshot(path=shot, full_page=True)
            ok = sw <= w
            bad += not ok
            print(f"{'PASS' if ok else 'FAIL'}  {name} {w}px scrollWidth={sw}  {shot}")
        b.close()
except Exception as e:  # browser missing etc.
    print(f"NOT RUN  render — {e.__class__.__name__}: {str(e).splitlines()[0]}")
    sys.exit(2)
sys.exit(1 if bad else 0)
