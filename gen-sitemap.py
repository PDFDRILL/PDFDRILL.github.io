#!/usr/bin/env python3
"""Regenerate sitemap.xml from every HTML page this repo publishes.

The hand-kept sitemap listed 13 of 105 pages; the reports, the inspectors
under files/ and the figure pages were missing, and a new page (translate.html)
was only listed because someone remembered to add it. This derives the list
from git instead, so a page is in the sitemap because it is published.

    python3 gen-sitemap.py            # rewrite sitemap.xml and sitemap.txt
    python3 gen-sitemap.py --check    # exit 1 if either would change

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


#: Page dates captured before the history was squashed. A rewrite collapses
#: every commit into one, so `git log -1` answers the rewrite's own date for
#: all 105 pages at once and <lastmod> stops meaning anything. The dates are
#: a fact about publication, not about the repository, so they are kept as
#: data. `_baseline` is the rewrite's date: a git date that differs from it is
#: a REAL commit made since, and wins — so this file goes stale on its own
#: rather than having to be maintained.
_RECORDED = ROOT / "sitemap-lastmod.json"


def recorded() -> tuple[dict, str | None]:
    try:
        import json
        d = json.loads(_RECORDED.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return {}, None
    return d, d.pop("_baseline", None)


def lastmod(path: str, dirty: set[str], today: str,
            rec: dict | None = None, baseline: str | None = None) -> str:
    if path in dirty:
        return today
    got = git("log", "-1", "--format=%cs", "--", path).strip()
    if got and got != baseline:
        return got                      # touched since the rewrite: real date
    return (rec or {}).get(path) or got or today


def url(path: str) -> str:
    if path == "index.html" or path.endswith("/index.html"):
        path = path[: -len("index.html")]
    return BASE + quote(path)


def build() -> str:
    today = datetime.date.today().isoformat()
    dirty = set(git("diff", "--name-only", "HEAD").split())
    rec, baseline = recorded()
    out = ['<?xml version="1.0" encoding="UTF-8"?>',
           '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for p in pages():
        out += ["  <url>", f"    <loc>{url(p)}</loc>",
                f"    <lastmod>{lastmod(p, dirty, today, rec, baseline)}</lastmod>", "  </url>"]
    out.append("</urlset>")
    return "\n".join(out) + "\n"


def as_text(xml: str) -> str:
    """The same URL list as a plain-text sitemap: one URL per line, UTF-8.

    Search Console can keep a GitHub Pages sitemap.xml in "Couldn't fetch"
    for weeks while the file is valid and Bing reads it. A second sitemap at
    a NEW url has no failed state attached, and the text format is part of
    Google's sitemap protocol, so both are published from one list."""
    return "\n".join(re.findall(r"<loc>([^<]+)</loc>", xml)) + "\n"


def main() -> int:
    new = build()
    outputs = {ROOT / "sitemap.xml": new, ROOT / "sitemap.txt": as_text(new)}
    if "--check" in sys.argv[1:]:
        stale = [t.name for t, body in outputs.items()
                 if not t.exists() or t.read_text(encoding="utf-8") != body]
        if stale:
            print(f"{', '.join(stale)} out of date; run python3 gen-sitemap.py")
            return 1
        return 0
    for target, body in outputs.items():
        target.write_text(body, encoding="utf-8")
    print(f"sitemap.xml + sitemap.txt: {new.count('<loc>')} URLs")
    return 0

if __name__ == "__main__":
    sys.exit(main())
