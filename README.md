# PDFDRILL.github.io

Homepage and evidence reports for **pdfdrill**, which converts PDFs into structured,
evidence-backed document objects for LLM use.

**Live site: https://pdfdrill.github.io/**

Plain static HTML, no build step (`.nojekyll`). Deployed by `.github/workflows/pages.yml`
on push to `master`, after a guard that checks every file under `reports/`.

## What is here

| Path | What it is |
|---|---|
| `index.html` | Homepage: ingestion, document object functions, output projection, evidence reports. |
| `reports/` | Evidence reports per document (`reports/<bibkey>/`) and the index of them. |
| `translate.html` | `pdfdrill translate`: a Chinese PDF in English with formulas intact. |
| `heimUFT.html`, `kolbe2018hubbard*.html`, `2004.05631v1.html` | Whole documents as single-file TiddlyWikis. |
| `pdfdrill-audit.html`, `*.inspect.html`, `files/` | Document-model inspectors. |
| `figures/`, `fig-*.svg/html` | Figure sources and renders. |
| `gen-*.py` | Generators for the sitemap and parts of `reports/index.html`. |

## Maintaining it

Maintenance is done by a Claude Code CLI under `CLAUDE.md`. Start there; the rules,
skills (`.claude/skills/`), checks (`tools/site-check.sh`) and history
(`docs/maintenance/`) all hang off it.
