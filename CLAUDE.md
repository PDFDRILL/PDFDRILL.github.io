# CLAUDE.md — pdfdrill.github.io

Static GitHub Pages site for pdfdrill. No build step. `.github/workflows/pages.yml` deploys on
every push to `master`, after a guard that checks everything under `reports/`.

Your job here: **small maintenance changes** — homepage wording, publishing a delivered report,
fixing a broken link. Nothing architectural. If a task looks bigger than that, stop and ask.

## Owner's working rules — every task

1. Smallest possible step, then validate. One change per commit.
2. Never write "done", "working", "complete", "fixed". Report test output only:
   `tools/site-check.sh: C1 PASS, C2 PASS, ...`.
3. Assume nothing works until a check says so. Re-run all checks after each step.
4. Never weaken, comment out, skip or delete a failing check to get green.
   Never `git commit --no-verify`. Never set `SITE_OWNER_OK` yourself.
5. End every task with the report in `docs/maintenance/REPORT-TEMPLATE.md`:
   checks by name with result, and assumptions not verified.
6. A problem outside the task goes into `docs/maintenance/KNOWN-ISSUES.md` with the owner
   named. It is a note, not a blocker, and not a reason to start other work.

## First session in a clone

```bash
tools/install-hooks.sh     # installs the pre-commit gate; once per clone
tools/site-check.sh        # baseline: write down which checks pass BEFORE you change anything
```

Read `docs/maintenance/HISTORY.md` once. It lists what went wrong here and why each rule exists.

## Three kinds of files

| Kind | Files | Rule |
|---|---|---|
| **Fixed** | the `DESIGN` block in `index.html`, `design.sha256`, `.github/`, `check-home.py`, `tools/`, `.claude/`, this file | Never change unless the owner asks for exactly that change. The pre-commit gate refuses them. |
| **Hand-written** | `index.html` inside `CONTENT` markers, `translate.html` text, rows in `reports/index.html`, `README.md`, `docs/maintenance/*.md` | Edit, then run the checks. |
| **Delivered** | `reports/<bibkey>/*`, `files/*`, `*.inspect.html`, `*-formula-report.html`, `*-compare.html`, the TiddlyWiki files (`heimUFT.html`, `kolbe2018hubbard*.html`, `2004.05631v1.html`, `pdfdrill-audit.html`, `*.tiddlers.json`) | Copy in exactly as the owner delivered them (`cp`). Never open them to edit, reformat, "fix" or "verify". An agent once damaged one this way and cost the owner an hour. |

## Tasks

- **Change homepage wording / add a link** → skill `site-change`.
- **Publish a delivered report folder** → skill `publish-report`.
- Anything else → ask first.

### The homepage design is not content
`index.html` has a `DESIGN:BEGIN … DESIGN:END` block (dark panels, amber/teal/violet accents,
IBM Plex Mono + Spectral), hash-pinned in `design.sha256`. Shorter or new content is **never** a
reason to touch it. Commit `10c1c04` replaced the content as asked and deleted the whole
stylesheet with it; `337dbe9` restored it. Use the existing classes only (see skill `site-change`).

## Checks

`tools/site-check.sh` runs all of them and prints PASS / FAIL / KNOWN / NOT RUN per check:

| | Check | What it proves |
|---|---|---|
| C1 | `check-home.py` | design block unchanged, head tags, content markers, local links, size < 40 KB |
| C2 | `tools/ci-guard.py` | the deploy guard from `pages.yml`, run locally exactly as CI runs it |
| C3 | `gen-sitemap.py --check` | sitemap matches git (NOT RUN in a shallow clone — it would mis-date pages) |
| C4 | `gen-residual-bars.py --check` | residual bars match `report.ink.json`; drift listed in KNOWN-ISSUES shows as KNOWN |
| C5 | `tools/render.py` | page renders at 1280 and 375 px, no horizontal scroll; writes screenshots to look at |

`gen-doc-downloads.py` is **not** run and must not be run: see KNOWN-ISSUES KI-2.

A green run of C1–C5 before `git push` is required. C2 is the same code CI runs, so a local
FAIL means the deploy would be refused.

## Commits

- Subject: `<area>: <what changed>` — e.g. `index: evidence card links the 2501.06662 report`.
- One logical change. Delivered files and the `reports/index.html` row for them may share a commit.
- End the message with the trailer your harness requires.
- Before `git push`: `git pull --ff-only`. If that fails, stop and ask — no rebase, no force-push.
- The kit files themselves (`CLAUDE.md`, `.claude/`, `tools/`, `check-home.py`) change only when
  the owner commits them with `SITE_OWNER_OK=kit`.
