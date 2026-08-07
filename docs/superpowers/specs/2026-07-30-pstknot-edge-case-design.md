# pst-knot edge case on pdfdrill.github.io — Design

Date: 2026-07-30
Status: **implemented**

## Revision history

- **rev 1** — designed around the claim that pst-knot's text layer is
  semantically empty and `inspect` renders empty page frames.
- **rev 2 (this document)** — that claim is **false**, caught by the spec's own
  Step 0 before anything shipped. Reframed around what the document actually
  does. Scope widened to fix the drillspace README, which carries the false
  claim.

## Purpose

`pst-knot-doc.pdf` is the PSTricks knot-plotting manual: 8 A4 pages out of
`dvips` + Ghostscript 8.70. It has a text layer and is not a scan, and `size`
reports both correctly. It still defeats the cheap route — and the three ways of
reading it disagree about what the document contains.

One section on <https://pdfdrill.github.io> shows all three readings with
artifacts a visitor can open, and states the cost of each without overselling.

## What was measured

Run on this host: pdfdrill 0.4.0, tesseract 5.3.4, poppler, pdfminer.six.

| Route | inspector badge | Objects | Breakdown |
|---|---|---|---|
| born-digital text layer | **8** | 20 | 8 Paragraph, 3 Citation |
| `ocr --force` @400 DPI | **119** | 131 | 109 Paragraph, 8 Equation, 2 Table, 3 Citation |
| mathpix (paid) | **79** | 88 | 24 Diagram, 22 Paragraph, 15 TableCell, 9 Formula, 5 TableRow, 2 Picture, 1 Table, 1 Toc |

The badge is `EL.filter(e => e.type !== 'Page').length` — every object carrying a
region. It does **not** match the count `pdfdrill inspect` prints on stdout
(12 / 123), which also counts `Document` and `Citation`. The site quotes the
badge, because that is the number a visitor sees.

### Three findings, none of them the original premise

1. **The text layer is thin, not empty.** It resolves 8 Paragraphs — exactly one
   per page, each a whole page of prose and LaTeX examples run together in a
   single blob, with no headings, tables or equations. The math fonts are present
   in the font layer (`CMMI10`) and nothing typed comes out. The failure is loss
   of structure, not absence of text.

2. **More elements is not better extraction.** OCR yields 119 and MathPix 79, and
   MathPix is the better model. The 119 are finely split but uniformly flat —
   `Paragraph` and `Table`, nothing else. The 79 carry `Diagram`, `Formula`,
   `Picture` and `Toc`. Counting nodes measures how hard a route chopped the
   page, not how much of the document it understood.

3. **The knots are invisible to both free routes, and not because they were
   missed.** They are vector: 293 curves and 57 lines across pages 1–6. There is
   no picture to extract — `pdfimages` reports 492 entries and every one is a 1×1
   stencil mask of 1 byte, a dvips painting artifact. A raster or blob extractor
   finds 492 single pixels. Only classifying regions on the *rendered* page
   recovers them as figures, which is why the Diagram column is `0 · 0 · 24`.

Finding 3 is the one that justifies the section: it is a case where the cheap
route is not merely lower quality but structurally incapable, and the reason is
legible.

## Decisions taken

| Question | Decision |
|---|---|
| Framing | Three assumptions, three routes — not "a document that fails". |
| Which states ship as artifacts | All three. The two free ones are reproducible; MathPix is labelled as not reproducible without keys. |
| Medium | One composite still of the three element trees. OBS loop of the live marker **deferred**. |
| Placement | New section `#ocr`, eyebrow `04 — when the text layer lies`, after `#depth`. Old 04–09 renumbered to 05–10. |
| Repo scope | `pdfdrill.github.io` + the drillspace README correction. |
| Generation | Two independent drill directories, persistent (see below). |

## Deliverables

| File | What | Size |
|---|---|---|
| `pst-knot-doc.textlayer.inspect.html` | born-digital route, badge 8 | 958 KB |
| `pst-knot-doc.ocr.inspect.html` | tesseract route, badge 119 | 1.0 MB |
| `pst-knot-doc.mathpix.inspect.html` | MathPix route, badge 79 | 1.0 MB |
| `pst-knot-elements.png` | the three element trees side by side, 1408×462 | 174 KB |
| `make-pstknot.sh` | regenerates the two free artifacts from the URL | 3 KB |
| `index.html` | new section, one nav link, eyebrows renumbered | +6.5 KB |

The still is a composite of three cropped inspector panels rather than a
screenshot of one, because the comparison *is* the content. At 174 KB it is an
order of magnitude lighter than the existing 1.4–2.1 MB hero PNGs.

## Generation

`make-pstknot.sh`, two working copies under distinct stems so neither run can
observe the other's sidecar:

```
pst-knot-doc.pdf ──┬─→ .pstknot-work/lib/pstknot-textlayer/ → model       → inspect
                   └─→ .pstknot-work/lib/pstknot-ocr/       → ocr --force → model → inspect
```

MathPix credentials are blanked in the real environment, which beats any `.env`,
forcing `model` down the born-digital route. `PDFDRILL_CONFIG` points at a
scratch config so nothing touches `~/pdfdrill-library`.

`pdfdrill embedimages` is deliberately **not** run — see below.

### Why the work directory persists

pdfdrill assigns **fresh random object and alignment ids on every clean model
build**. Two clean builds of byte-identical content therefore emit different ids
and a ~1 MB spurious diff in each committed artifact. Re-running against an
existing sidecar reuses the ids.

So `.pstknot-work/` is persistent and gitignored, and the OCR step is skipped
when `lines.json` already exists. With that, running the script twice produces
byte-identical output — verified. Deleting `.pstknot-work/` forces a clean
rebuild, which renumbers every id and produces a large diff with no change in
extracted content.

An earlier reading of this — that ids were derived from the input path — was
wrong; that test had reused a sidecar.

## Verification (all six passed)

1. All three inspect HTMLs open standalone from `file://`, confirmed by
   screenshotting each in headless Firefox and looking at the result.
2. Badges differ and all three are quoted: 8 / 119 / 79.
3. Eyebrows read `01`–`10` in document order, no gap or repeat — grepped.
4. The still carries alt text describing what each tree contains, including what
   is absent from the first two.
5. `make-pstknot.sh` run twice produces byte-identical artifacts.
6. Full rendered page height 21,759 px → 23,966 px, **+10.1%**. Against the
   measured 26 print pages that is roughly 28–29 — the section costs about 2.5
   pages. Accepted knowingly; the restructure is a separate cycle.

No headless print engine is available on this host (no chromium, no
wkhtmltopdf), so item 6 is a rendered-height proxy, not a print-engine count.

## Copy constraints applied

Banned and confirmed absent from the section: "instant", "in seconds",
"automatically", "just works", "effortless", "seamless". (Two pre-existing
"instant"s elsewhere on the page are out of scope for this addition.)

Stated plainly in the section: OCR is a raster pass whose cost scales with page
count; its equation regions are correct and their text is garbled; tesseract is
named with its version; MathPix requires paid keys and its column cannot be
reproduced for free.

Markup uses only the existing class vocabulary — `.eyebrow`, `.sub`, `.pill`,
`.grid g3`, `.card`, `.callout`, `.term`, `.btn`, `.btn primary`. No new class,
no new CSS.

## Deferred: OBS capture of the live marker

The inspector's hover→overlay link is the one thing a still cannot show. Recorded
separately and dropped in without touching surrounding markup.

| Setting | Value |
|---|---|
| Canvas | 1408×768 |
| Frame rate | 30 fps, no audio track |
| Duration | 12–18 s, looping on the opening frame |
| Encode | H.264 mp4, CRF ~23, faststart, target < 3 MB |
| Window | dark theme, bookmarks bar hidden, inspector filling the canvas |

Shot sequence: rest ~2 s with the badge legible → move down the tree across one
Paragraph, one Diagram and one Formula, pausing ~1.5 s each → return to the
opening frame. Embed `muted playsinline preload="none"` with a `poster`, plus an
adjacent text description.

## Open, reported separately

`pdfdrill embedimages` on this document lifts the 492 1×1 stencil masks into
**984** `EmbeddedImage` nodes and takes the model from 131 to 1115 objects, ~88%
one-pixel noise. Written up in full, with a control document showing the
duplication is specific to *inline* images rather than general, in
[`2026-07-30-embedimages-finding.md`](2026-07-30-embedimages-finding.md).

Not acted on here — it is a pdfdrill behaviour question, not a site question.

## Out of scope

- Restructuring `index.html` into an active, selection-driven layout. Separate
  spec. The 26-page finding and the lever — promoting the command-catalogue
  selector (`CMDS`, `index.html`) to the page spine — belong there.
- Any pdfdrill code change, including the two reproducibility findings above.
- The OBS recording.
