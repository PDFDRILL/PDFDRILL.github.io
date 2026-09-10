#!/usr/bin/env python3
"""Regenerate reports/index.html's residual bars from each report.ink.json.

640 -- the bars in the Residual column are DERIVED data (a distribution over
report.ink.json's rows, rendered as a coloured bar + code counts), but they
had been hand-maintained since 2 September and every one of them had drifted
from the file it claims to describe -- exactly the failure Guard 2 in
.github/workflows/pages.yml exists to catch. Run this instead of hand-editing
rows:

    python3 gen-residual-bars.py            # rewrite reports/index.html
    python3 gen-residual-bars.py --check    # exit 1 if any bar would change

It touches ONLY the second `<td class="res">` cell (the one holding
`<div class="bar">...`) of each row whose bibkey has a reports/<k>/report.ink.json.
A row with no ink.json (0902.0431 -- withdrawn, "not measured") or no `<div
class="bar">` in that cell (a doc mid-rebuild, "not rebuilt") is left alone;
this script only ever replaces markup shaped like what it also emits.
"""
from __future__ import annotations

import collections
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
INDEX = ROOT / "reports" / "index.html"

#: inkdrill's flag -> the single-letter code the report and this bar both use.
#: Order here is display order, left to right, worst to best -- matches the
#: legend and every bar already on the page. "unrendered" (U) is real data
#: (8 of 21 documents carry it, mielke-geometrodynamics alone has 743 rows of
#: it); "absent" (A) is a flag inkconvert.py can emit but no published
#: report.ink.json has ever used it, so it is not in this table -- see the
#: commit message for why that is deliberate rather than an oversight.
LET = collections.OrderedDict([
    ("component", ("C", "#dc1e1e")),
    ("weak", ("W", "#e69614")),
    ("stable", ("S", "#5c96c8")),
    ("unrendered", ("U", "#9a6ac8")),
    ("noise", ("N", "#787878")),
    ("clean", ("K", "#28a028")),
])

ROW_RE = re.compile(r'<code class="doc">([^<]+)</code>(.*?)</tr>', re.S)
#: the SECOND `<td class="res">...</td>` in a row is the bar cell; the first
#: is the "cor/unr/flag/dbt" summary and must not be touched. Neither cell
#: nests a `<td>`, so non-greedy up to the first `</td>` is exact.
RES_RE = re.compile(r'<td class="res">.*?</td>', re.S)


def bar_cell(dist: collections.Counter) -> str:
    total = sum(dist.values())
    bars, cts = [], []
    for flag, (code, colour) in LET.items():
        n = dist.get(flag, 0)
        if not n:
            continue
        pct = f"{n / total * 100:.4g}"
        bars.append(f'<i style="width:{pct}%;background:{colour}"></i>')
        cts.append(f'<b style="color:{colour}">{code}</b>{n}')
    return (f'<td class="res"><div class="bar">{"".join(bars)}</div>'
            f'<div class="cts">{" ".join(cts)}</div></td>')


def main() -> int:
    check_only = "--check" in sys.argv
    html = INDEX.read_text(encoding="utf-8")
    changed, skipped = [], []

    def fix_row(m: re.Match) -> str:
        k, cell = m.group(1), m.group(2)
        ink_path = ROOT / "reports" / k / "report.ink.json"
        if not ink_path.exists():
            return m.group(0)
        rows = json.loads(ink_path.read_text(encoding="utf-8"))["rows"]
        dist = collections.Counter(r["flag"] for r in rows)
        new_cell = bar_cell(dist)

        res_cells = RES_RE.findall(cell)
        if len(res_cells) < 2 or "<div class=\"bar\">" not in res_cells[1]:
            skipped.append(k)
            return m.group(0)
        old_cell = res_cells[1]
        if old_cell == new_cell:
            return m.group(0)
        changed.append((k, old_cell, new_cell))
        # Replace only the second occurrence of the res-cell pattern within
        # this row's slice.
        first, rest = cell.split(old_cell, 1)
        return m.group(0).replace(cell, first + new_cell + rest, 1)

    new_html = ROW_RE.sub(fix_row, html)

    if skipped:
        print(f"left alone (no bar to regenerate): {', '.join(skipped)}")
    if not changed:
        print("residual bars: 0 rows differ from report.ink.json")
        return 0

    print(f"residual bars: {len(changed)} row(s) disagree with report.ink.json")
    for k, old, new in changed:
        print(f"  {k}")
    if check_only:
        return 1
    INDEX.write_text(new_html, encoding="utf-8")
    print(f"rewrote {INDEX}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
