---
description: Change wording or links on the pdfdrill.github.io homepage (index.html) or another hand-written page, without touching the design. Use for any homepage text, card, link or section change.
---

# site-change — a small change to the homepage

## Contract
- **Input:** one change the owner asked for, in their words.
- **Output:** one commit that changes only text inside `<!-- CONTENT:name -->` markers (plus nav
  links in `<header class="bar">` if a section was added), with C1–C5 green.
- **Never:** edit the `DESIGN` block, add `<style>` or new CSS classes, add claims the owner's
  skill card does not make, link to a file that is not in the repo.

## Steps — validate after each

1. `tools/site-check.sh` → record the baseline result.
2. Find the section: `grep -n 'CONTENT:' index.html`. Edit inside one block only.
3. `python3 check-home.py` → must be 6/6. If T1 fails you touched the design: `git checkout index.html`, start again.
4. `python3 tools/render.py` → open both screenshots it prints and look at them. Check the
   changed section reads correctly at 375 px.
5. `tools/site-check.sh` → C1–C5 PASS (or KNOWN). Compare with step 1: nothing that passed may now fail.
6. Commit: `index: <what changed>`. Report with `docs/maintenance/REPORT-TEMPLATE.md`.

## Building blocks (existing classes — use only these)

```html
<!-- CONTENT:name -->
<section id="name">
  <div class="wrap">
    <p class="eyebrow">06 — label</p>
    <h2>Short claim.</h2>
    <p class="sub">One or two sentences.</p>
    <div class="grid g3">                       <!-- g2 for two columns -->
      <div class="card">                        <!-- add teal | violet | key -->
        <h4><span class="dot"></span>Title</h4>
        <p>Text.</p>
        <div class="ms"><a href="reports/x/inspect.html">→ example</a></div>
      </div>
    </div>
  </div>
</section>
<!-- /CONTENT:name -->
```

Also available: `.route` (chips with `<span>`/`<i>→</i>`, `span.out` for the result),
`.goal` (callout with `<b>Label</b>`), `table.docs` (`td.l` for the link column),
`.btn` / `.btn.primary` / `.btn.alt` inside `.cta`, `.badge`.

**Adding a section** also means: add its name to `SECTIONS` in `check-home.py` — that file is
fixed, so ask the owner to approve that one-line change; until then add content to an existing section.
