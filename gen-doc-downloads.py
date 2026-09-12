#!/usr/bin/env python3
"""Regenerate the per-file sizes in reports/index.html's download menus.

677 -- each row's download menu is a `<select>` of
`<option value="<slug>/<file>">Label (FMT) - SIZE</option>`, and every SIZE is
hand-transcribed from the file it links. They were CORRECT before the 676
republish (gilmore-lie-groups: "22.5 MB" against report.pdf's 23,598,702
bytes) and every republish makes all of them wrong at once -- the same drift
`gen-residual-bars.py` was written for, one column over.

    python3 gen-doc-downloads.py            # rewrite reports/index.html
    python3 gen-doc-downloads.py --check    # exit 1 if any size would change

It touches ONLY the text after the last " - " inside an `<option>` whose
`value` names an existing file under reports/. An option naming a file that
does NOT exist is a dead download link and is reported as an ERROR rather
than silently left alone -- that is the one failure a reader meets directly.

Sizes match the convention already on the page: kB (1024) with no decimal
below 1 MiB, MB (1048576) with one decimal above.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
INDEX = ROOT / "reports" / "index.html"

#: `<option value="slug/file" ...>Label (FMT) - SIZE</option>`. The label is
#: kept verbatim; only the size is recomputed.
OPTION = re.compile(
    r'(<option\s+value="([^"]+)"[^>]*>)([^<]*?)(</option>)')
SEP = "·"          # the middle dot the page already uses


def human(n: int) -> str:
    """The page's own convention, reproduced exactly.

    A non-empty file floors at 1 kB rather than rounding to "0 kB": the only
    size this differed on was penev_B/tables.md (473 bytes, written by hand as
    "1 kB"), and "0 kB" next to a working download reads as a broken link.
    An actually empty file is a real problem and says 0 kB.
    """
    if n == 0:
        return "0 kB"
    if n < 1024 * 1024:
        return "%d kB" % max(1, round(n / 1024))
    return "%.1f MB" % (n / (1024 * 1024))


def main() -> int:
    check = "--check" in sys.argv
    if not INDEX.is_file():
        print("no reports/index.html", file=sys.stderr)
        return 2
    html = INDEX.read_text(encoding="utf-8")
    changed, dead, seen = [], [], 0

    def repl(m: "re.Match") -> str:
        nonlocal seen
        open_tag, value, label, close = m.groups()
        seen += 1
        target = ROOT / "reports" / value
        if not target.is_file():
            dead.append(value)
            return m.group(0)
        size = human(target.stat().st_size)
        if SEP in label:
            head = label.rsplit(SEP, 1)[0]
            new_label = "%s%s %s" % (head, SEP, size)
        else:
            new_label = "%s %s %s" % (label.strip(), SEP, size)
        if new_label != label:
            changed.append((value, label.strip(), new_label.strip()))
        return open_tag + new_label + close

    out = OPTION.sub(repl, html)

    print("gen-doc-downloads: %d option(s) inspected" % seen)
    for value, was, now in changed:
        print("  %-52s %s -> %s" % (value, was, now))
    for value in dead:
        print("  ERROR dead link: reports/%s does not exist" % value)
    if seen == 0:
        print("inspected 0 options - refusing to claim success", file=sys.stderr)
        return 2
    if dead:
        print("%d dead download link(s)" % len(dead), file=sys.stderr)
        return 1
    if check:
        print("%d size(s) would change" % len(changed))
        return 1 if changed else 0
    if changed:
        INDEX.write_text(out, encoding="utf-8")
        print("rewrote %d size(s) in reports/index.html" % len(changed))
    else:
        print("every size already matches its file")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
