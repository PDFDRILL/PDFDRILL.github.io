# The panel series in the structural format

Eight figures: `overview` plus `layer1`..`layer7`, each one file in `specs/`.

    specs/layer4-model.fig.json
        |-- prompt   the prose description the panel came from
        |-- palette  sage / olive / ochre / ink on cream
        |-- root     nested rows, cols and groups - NO coordinates
        `-- edges    id -> id, with optional side hints

## What changed from the first version

Coordinates are no longer authored. `layout.py` measures each element
bottom-up and places it top-down, so adding or removing a box re-flows the
figure. The old flat format is still what the emitters consume - `layout.py`
compiles the structural spec into it, which means the entire existing test
suite still applies unchanged.

Node widths are derived from label length. `canvas.aspect` pins every panel to
the same H/W (512/279, the ratio the original series was drawn at) by padding
the short axis, so the eight sit together as a series regardless of content.

## CLI

    figtool.py show     specs/layer4-model.fig.json
    figtool.py prompt   specs/layer4-model.fig.json
    figtool.py add      specs/layer2-probe.fig.json --parent probe \
                        --id pdffonts --label pdffonts --mono --tone olive
    figtool.py set      specs/layer2-probe.fig.json --id pdffonts --sub "font table"
    figtool.py edge     specs/layer2-probe.fig.json --from pdffonts --to rail --kind store
    figtool.py rm       specs/layer2-probe.fig.json --id pdffonts
    figtool.py build    specs/layer2-probe.fig.json --outdir build

Every mutating command compiles and validates before writing. If the edit
would break an invariant the file is left **byte-identical** and the errors go
to stderr - verified in T7.6. `rm` also drops any edge that touched the
removed element.

## Edge kinds

`feed` solid, `escalate` heavy ochre, `fallback` dashed, `store` dotted.
Edges are centre-to-centre clipped at the box border by default; `--from-side`
/ `--to-side` pin an edge to a face when you want it perpendicular. Side hints
survive re-layout, absolute anchors would not.

## Tests

| Test | Checks |
|---|---|
| T5 | a structural spec compiles to geometry satisfying C1..C11 |
| T6 | headless Cytoscape matches the MetaPost geometry, all 8 figures, 101 boxes |
| T7 | CLI add / set / edge / rm, and that an invalid edit is refused |
| T8 | ink coverage per rendered figure - catches blank or degenerate output |

## Verification status

**All eight print renderings have now been looked at** and are correct. Checked
by rendering each `build/<id>.pdf` at 150 dpi and viewing it. Alongside the
programmatic checks — zero MetaPost errors on all eight, invariants satisfied,
geometry identical across renderers — that covers the print path.

Two edge-routing defects were found this way, which no programmatic check
caught because the geometry was valid in both cases:

* **The overview's four `store` edges converged to a point.** `layout.py`
  compiled every side hint to `{side, t: 0.5}`, so all four drops landed on the
  rail's top *midpoint*. `figspec` has supported `{side, align:<id>}` all along
  (C9/C11 validate it) but the structural compiler never emitted it, making a
  supported feature unreachable from a structural spec. Fixed: an end now
  aligns to the other end when it is the larger one in the free axis, so a
  narrow tier drops from its own centre and the wide rail aligns to the tier.
  An explicit `*_t` still wins.
* **Layer 6's `store` edge runs diagonally.** Same root cause, not yet given a
  side hint. Cosmetic; left alone.

One cosmetic artifact remains across the series: a single box sitting beside a
tall group is stretched to match it, so `scanned page` (layer 1) and
`math detected` (layer 3) are mostly empty with the label floating mid-box.

**Still not verified: the browser rendering.** Headless Firefox never fires
`requestAnimationFrame` before `--screenshot` fires at `load`, and Cytoscape
paints on rAF, so the canvas reads blank for harness reasons rather than figure
reasons — measured directly: a synchronous canvas draw gives 3600 non-blank
pixels, the identical draw inside rAF gives 0. Everything short of the paint
call checks out (library inlined, no external refs, zero JS errors, elements and
style rules resolved, container sized, `fit()` leaving the frame in view).
Closing it needs a driver that waits for a frame — Playwright or Puppeteer — or
opening one of the `fig-*.html` files by hand.

## Outputs

Each spec produces five files in `build/`:

| Format | Produced by | Used for |
|---|---|---|
| `.eps` | `mpost` | the primary vector output; everything else derives from it |
| `.pdf` | `gs -dEPSCrop` from the EPS | `\includegraphics` under pdflatex |
| `.svg` | `mpost` again with `outputformat := "svg"` | **the page** — `make install` copies these |
| `.dvi` | `latex` on a `standalone` wrapper around the EPS | DVI-based workflows |
| `.html` | `emit_html.py` | the interactive Cytoscape rendering |

Two notes on the SVG. MetaPost 3 emits **real** SVG — this is not the
`outputformat := "pdf"` trap recorded above, which silently wrote PostScript;
verified by rendering it. Glyphs come through as reusable `<use>` symbols with
no `font-family` reference at all, so the file needs no font to display
correctly.

The SVG comes from MetaPost rather than from the DVI via `dvisvgm`, although
both work. `dvisvgm` flattens every glyph to its own `<path>` — measured at
114,907 bytes against MetaPost's 97,246 for the same panel, ~18% larger with no
gain. The DVI is still emitted, because it is a useful artifact in its own right
and it is what a DVI toolchain wants.

`dvisvgm 3.6` has no `--libgs` option; it handled the EPS-bearing DVI without
one.

## Cytoscape is loaded from a CDN, not inlined

`figtool.py build --inline` exists and would embed the 435 KB library in each
panel. It is deliberately **not** used: these figures are served from GitHub
Pages, so eight copies of the same library buy nothing. Emitted HTML is ~8–18 KB
per panel instead of ~453 KB, and the series drops from 3.6 MB to about 95 KB.

The "one self-contained file, no server" claim elsewhere on the site is about
the TiddlyWiki and inspector artifacts, which genuinely are self-contained. It
was never a claim about these figures.

`test2_fit.py`, `test5_layout.py`, `test6_series.js` and `test8_ink.py` are
referenced by the build and the old `Makefile.series` but ship in neither
archive, so T2.2 and T5–T8 did not run here.

The seven panels are a structural translation of the Gemini prompts, not a
copy of the sketch style: these are clean vector diagrams with real text,
which is exactly what the original transcript said generative art does worst.
The palette follows the sage/olive/ochre-on-cream direction; the hand-drawn
linework and the graph-paper background are not reproduced.
