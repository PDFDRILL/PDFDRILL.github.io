# History — what happened here, and the rule each event left behind

Full detail is in `git log` (80 commits, 2026-08-07 → 2026-10-19). Nothing was squashed or
rewritten; this file is the short version for a new session.

## Timeline

| When | Commits | What happened |
|---|---|---|
| 08-07 – 08-08 | `aa35e02` … `e92e730` | Site created; translation example (arXiv 2409.18839) on the homepage. |
| 08-24 | `a418eb6` … `ecdf11b` | `reports/` begins: formula reports, markdown, inspect view, ink.json per document. |
| 08-25 | `7ea2e82` … `421b9e0` | Deploy moved from the legacy Pages builder to `pages.yml` (Actions). The guard is written: refuse unchosen files, zero-byte files, and index claims that contradict the artefacts. |
| 08-27 | `394a9f6` … `7f0f56c` | Guard extended: measurement must be credible (p90 component ratio), joined to its report, not an absent reading. |
| 08-28 – 09-23 | `6a6fdaa` … `912980f` | Report rounds: 20+ documents rebuilt, re-measured and republished; `corrections.html`, `containers.html`; generators `gen-residual-bars.py`, `gen-doc-downloads.py`. |
| 09-26 – 09-27 | `fada95a` … `5aa7e75` | Translate section and GIF on the homepage; `translate.html`; sitemap generated from git. |
| 09-28 – 10-14 | `fba22a5` … `e4e563e` | BH3FR (Heim/Dröscher 1985) and killing1889 (Math. Ann. 33) published. |
| 10-19 18:46 | `10c1c04` | Homepage replaced by the owner's short skill card — **and the entire stylesheet deleted with it.** |
| 10-19 | `337dbe9` | Skill-card content back in the original design; design block hash-pinned; `check-home.py`. |
| 10-19 | (this kit) | `CLAUDE.md`, `.claude/` settings and skills, `tools/`, this file. |

## Lessons — each is now a rule or a check

1. **Shorter content is not a design change.** `10c1c04` read "short and concise" as "remove
   layout and colour". → design block pinned by hash, `check-home.py` T1, pre-commit gate.
2. **Never edit or "verify" a delivered HTML file.** An agent edited a generated wiki before upload
   and damaged it; the owner lost an hour. → delivered files are `Edit`-denied in `.claude/settings.json`; copy only.
3. **The legacy Pages builder timed out** (~100 MB of history from four pushes on 08-06). It was
   replaced by Actions with a shallow checkout. Large blobs stay in history; do not try to "clean" it
   (`git filter-branch` / force-push are denied).
4. **jsDelivr has a size limit.** Moving the large wiki to another repo served via jsDelivr failed;
   it had to be moved back. Large files are served from this repo.
5. **A guard that checks names proves nothing** — a zero-byte `report.pdf` passed (`13a64d1`).
   → guard checks content.
6. **The guard's allow-list must grow with the artefacts.** From 09-05 every deploy failed silently
   and the live site served an older build, because new artefact kinds were not in `ALLOWED`.
   → a new artefact kind is an owner decision, added in the same commit that first publishes it.
7. **Derived numbers drift when typed by hand** — residual bars and download sizes drifted from
   their files. → generators; but see KNOWN-ISSUES KI-1/KI-2 before running them.
8. **The sitemap dates come from git.** In a shallow clone it re-dates every older page. → C3 is
   NOT RUN in shallow clones; pre-commit refuses a sitemap from one.
9. **The owner pays for a CLI and an auditor; an audit that always finds many errors makes the net
   result nil.** → small steps, checks after each, report only check output.
