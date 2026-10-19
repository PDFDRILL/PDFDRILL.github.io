# Known issues

Notes, not blockers. Each has an owner who decides; do not start work on one without being asked.
Add new entries at the end with the next number. Remove an entry only when the owner closes it.

## KI-1 — residual bar colour drift in the killing1889 row
- **Owner:** Wulf (decides which colour for class `X` / crop is canonical).
- **Seen:** `gen-residual-bars.py --check` lists `killing1889`. The hand-written row colours `X`
  `#9a6ac8` and orders it before `N`; the generator emits `#8c8c9e`, after `N`. Counts agree, so
  the deploy guard passes.
- **Effect on you:** `tools/site-check.sh` reports C4 as KNOWN while this is the only drift.
  Running `gen-residual-bars.py` rewrites this row too — do not commit that change until decided.

## KI-2 — gen-doc-downloads.py corrupts the two newest rows
- **Owner:** Wulf (fix the script, or rewrite the rows to its format).
- **Seen:** `killing1889` and `BH3FR` file menus use ` &middot; ` and decimal units (165 kB);
  the script expects ` - ` and binary units. Its `--check` proposes
  `… &middot; 165 kB · 161 kB` — appending a second size instead of replacing.
- **Effect on you:** do not run it (denied in `.claude/settings.json`). Write sizes by hand
  (skill `publish-report`).

## KI-3 — the deploy publishes the maintenance files
- **Owner:** Wulf (`pages.yml` is frozen).
- **Seen:** the stage step excludes only `.git`, `.github`, `.pstknot-work`, `node_modules`, so
  `CLAUDE.md`, `.claude/`, `tools/`, `docs/` are served on the public site.
- **Effect on you:** keep nothing private in these files.

## KI-4 — source links to github.com/WulfKolbe/pdfdrill unverified
- **Owner:** Wulf.
- **Seen:** the homepage hero and footer link the pdfdrill source repo. Not checked whether it is
  public; if private, visitors get a 404.
