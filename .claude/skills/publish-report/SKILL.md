---
description: Publish a report folder the owner delivered (reports/<bibkey>/) on pdfdrill.github.io and add its row to reports/index.html so the deploy guard accepts it. Use when the owner hands over new or rebuilt report artefacts.
---

# publish-report — put a delivered report online

## Contract
- **Input:** a folder of artefacts from the owner for one `<bibkey>`, plus from the owner: title,
  author, source line, document page count, equation count. If any is missing, ask — they are
  not in the artefacts (`report.build.json` `pages` is the *report's* page count, not the document's).
- **Output:** `reports/<bibkey>/` holding only allowed files, byte-identical to what was
  delivered, plus one row in `reports/index.html`; C2 (the deploy guard) PASS.
- **Never:** open, edit, regenerate, compress or "fix" a delivered file. If a delivered file fails
  the guard, stop and report it to the owner — the producer fixes it, not you.

## Allowed files (from the guard in `.github/workflows/pages.yml`)
`report.pdf report.ink.json report.build.json inspect.html compare.html residuals.pdf
evidence-equation.pdf evidence-formula.pdf evidence-table.pdf evidence-image.pdf
formula-report.html tables.html tables.md <bibkey>.md`. Anything else is refused by the deploy.
A new artefact kind needs the owner to change the guard — ask; do not rename files to fit.

## Steps — validate after each

1. `tools/site-check.sh` → baseline.
2. Copy: `mkdir -p reports/<bibkey> && cp <delivered>/<allowed files> reports/<bibkey>/`.
   Then `cmp` each copied file against its source → all identical.
3. `python3 tools/ci-guard.py` → expect exactly one new failure: `<bibkey> is published but has
   no row in index.html`. Any other failure: stop, report to the owner.
4. Add the row to `reports/index.html`: copy the nearest existing `<tr>` (the `killing1889` row
   is the most recent), then change bibkey, title, author, source, pages, equations, measured
   date (`built_at` in `report.build.json`) and the file menu. Use the owner's numbers; never estimate.
   Leave the residual bar cell to the generator.
5. `python3 gen-residual-bars.py` → fills the bar from `report.ink.json`.
   Then `python3 gen-residual-bars.py --check` → your row must not be listed.
   `git diff reports/index.html` must change only your row. The generator rewrites every row:
   if it also changed `killing1889`, that is KNOWN-ISSUES KI-1 — stop and ask the owner to decide it.
6. `python3 tools/ci-guard.py` → PASS.
7. `tools/site-check.sh` → C1–C5 PASS or KNOWN; nothing that passed in step 1 now fails.
8. Commit: `reports/<bibkey>: <title, short>`. Report with `docs/maintenance/REPORT-TEMPLATE.md`.

Do **not** run `gen-doc-downloads.py` (KNOWN-ISSUES KI-2). Sizes in the file menu: write them
by hand in the `&middot;` form of the `killing1889` row, decimal units from `ls -l` bytes:
`< 1 000 000` → kB, no decimal (164 971 → `165 kB`); otherwise MB, one decimal (4 170 064 → `4.2 MB`).
