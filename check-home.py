#!/usr/bin/env python3
"""check-home.py — the homepage contract. Run before every commit that touches index.html.

    python3 check-home.py            # checks index.html
    python3 check-home.py --pin      # re-pin design.sha256 (ONLY when Wulf asked for a design change)

Exit 0 only if every test passes. Each test prints PASS/FAIL with its name.
Stdlib only.
"""
import hashlib, os, re, sys
from html.parser import HTMLParser

ROOT = os.path.dirname(os.path.abspath(__file__))
PAGE = os.path.join(ROOT, "index.html")
PIN = os.path.join(ROOT, "design.sha256")
SECTIONS = ["hero", "ingestion", "functions", "projection", "evidence", "examples"]
HEAD_REQUIRED = [
    r'<meta name="google-site-verification" content="z5gFtqi9199Eg2nvpbuiYbVltjVtAB3QYXU6Eh3Hx-0"',
    r'<link rel="canonical" href="https://pdfdrill.github.io/">',
    r'<meta name="description" content="[^"]{40,}">',
    r'<meta name="viewport"',
    r'<link rel="icon" href="/favicon.ico"',
    r'<link rel="manifest" href="/site.webmanifest">',
    r'fonts.googleapis.com/css2\?family=IBM\+Plex\+Mono',
]

def design_block(s):
    m = re.search(r"<!-- DESIGN:BEGIN.*?-->(.*?)<!-- DESIGN:END -->", s, re.S)
    return m.group(1) if m else None

class Links(HTMLParser):
    def __init__(self):
        super().__init__(); self.refs = []; self.ids = set()
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if "id" in a: self.ids.add(a["id"])
        for k in ("href", "src"):
            if a.get(k): self.refs.append(a[k])

def main():
    s = open(PAGE, encoding="utf-8").read()
    block = design_block(s)
    if "--pin" in sys.argv:
        if block is None: sys.exit("no DESIGN block to pin")
        open(PIN, "w").write(hashlib.sha256(block.encode()).hexdigest() + "\n")
        print("pinned", PIN); return 0

    results = []
    def test(name, ok, detail=""):
        results.append(ok); print(f"{'PASS' if ok else 'FAIL'}  {name}" + (f" — {detail}" if detail and not ok else ""))

    # T1 design block exists and is byte-identical to the pinned one
    want = open(PIN).read().strip() if os.path.exists(PIN) else None
    got = hashlib.sha256(block.encode()).hexdigest() if block is not None else None
    test("T1 design block unchanged", block is not None and want is not None and got == want,
         "DESIGN:BEGIN/END block missing or edited; restore it from git (git show HEAD~1:index.html)")

    # T2 no second stylesheet sneaking in outside the design block
    outside = s.replace(block or "", "")
    test("T2 no <style> outside design block", "<style" not in outside)

    # T3 required head tags
    miss = [r for r in HEAD_REQUIRED if not re.search(r, s)]
    test("T3 required head tags", not miss, "missing: " + ", ".join(miss))

    # T4 content markers paired, in order, each section id present
    p = Links(); p.feed(s)
    bad = []
    pos = -1
    for k in SECTIONS:
        a, b = s.find(f"<!-- CONTENT:{k} -->"), s.find(f"<!-- /CONTENT:{k} -->")
        if a < 0 or b < a or a < pos: bad.append(k)
        pos = b
        if k != "hero" and k not in p.ids: bad.append(f"#{k}")
    test("T4 content markers and section ids", not bad, "problem: " + ", ".join(bad))

    # T5 every local link/src resolves to a file in the repo; every #anchor exists
    broken = []
    for r in p.refs:
        if re.match(r"^(https?:|mailto:|//)", r): continue
        if r.startswith("#"):
            if r[1:] not in p.ids: broken.append(r)
            continue
        path = r.split("#")[0].split("?")[0]
        f = os.path.join(ROOT, path.lstrip("/"))
        if path.endswith("/"): f = os.path.join(f, "index.html")
        if not os.path.isfile(f): broken.append(r)
    test("T5 local links resolve", not broken, "broken: " + ", ".join(broken))

    # T6 page stays a homepage, not a document: size cap
    n = len(s.encode())
    test("T6 index.html under 40 KB", n < 40_000, f"{n} bytes")

    print(f"{sum(results)}/{len(results)} passed")
    return 0 if all(results) else 1

if __name__ == "__main__":
    sys.exit(main())
