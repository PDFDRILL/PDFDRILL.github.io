#!/usr/bin/env python3
"""Regenerate sitemap.xml from every HTML page this repo publishes.

The hand-kept sitemap listed 13 of 105 pages; the reports, the inspectors
under files/ and the figure pages were missing, and a new page (translate.html)
was only listed because someone remembered to add it. This derives the list
from git instead, so a page is in the sitemap because it is published.

    python3 gen-sitemap.py            # rewrite sitemap.xml
    python3 gen-sitemap.py --check    # exit 1 if sitemap.xml would change

Every tracked *.html is listed except the Search Console verification file.
`index.html` is written as its directory URL (`/`, `/reports/`), the form the
pages' own canonical links use. <lastmod> is the date of the last commit that
touched the file; a file with uncommitted changes gets today's date, since it
will be newer than its last commit once pushed. No <priority>/<changefreq>:
Google ignores both.
"""
from __future__ import annotations

import datetime
import re
import subprocess
import sys
from pathlib import Path
from urllib.parse import quote

ROOT = Path(__file__).resolve().parent
BASE = "https://pdfdrill.github.io/"
SKIP = re.compile(r"^google[0-9a-f]+\.html$")      # Search Console verification
FIRST = ["index.html", "translate.html"]            # listed first, in this order


def git(*args: str) -> str:
    return subprocess.run(["git", *args], cwd=ROOT, check=True,
                          capture_output=True, text=True).stdout


def pages() -> list[str]:
    files = [f for f in git("ls-files", "-z", "*.html").split("\0")
             if f and not SKIP.match(Path(f).name)]
    head = [f for f in FIRST if f in files]
    return head + sorted(f for f in files if f not in head)


def lastmod(path: str, dirty: set[str], today: str) -> str:
    if path in dirty:
        return today
    return git("log", "-1", "--format=%cs", "--", path).strip() or today


def url(path: str) -> str:
    if path == "index.html" or path.endswith("/index.html"):
        path = path[: -len("index.html")]
    return BASE + quote(path)


def build() -> str:
    today = datetime.date.today().isoformat()
    dirty = set(git("diff", "--name-only", "HEAD").split())
    out = ['<?xml version="1.0" encoding="UTF-8"?>',
           '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for p in pages():
        out += ["  <url>", f"    <loc>{url(p)}</loc>",
                f"    <lastmod>{lastmod(p, dirty, today)}</lastmod>", "  </url>"]
    out.append("</urlset>")
    return "\n".join(out) + "\n"


def main() -> int:
    target = ROOT / "sitemap.xml"
    new = build()
    old = target.read_text(encoding="utf-8") if target.exists() else ""
    if "--check" in sys.argv[1:]:
        if new != old:
            print("sitemap.xml is out of date; run python3 gen-sitemap.py")
            return 1
        return 0
    target.write_text(new, encoding="utf-8")
    print(f"sitemap.xml: {new.count('<loc>')} URLs")
    return 0


if __name__ == "__main__":
    sys.exit(main())
