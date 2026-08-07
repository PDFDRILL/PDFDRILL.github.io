# `pdfdrill embedimages` on PostScript-generated documents — finding

Date: 2026-07-30
Status: **reported, not acted on** — this is a pdfdrill question, not a site one.
Found while building the pst-knot section of <https://pdfdrill.github.io>.

Measured with pdfdrill 0.4.0, poppler, tesseract 5.3.4, on
`pst-knot-doc.pdf` (the PSTricks knot manual, 8 pages, dvips + Ghostscript 8.70)
and on `2305.04710v1.pdf` as a control.

## What happens

```
pdfdrill ocr   knot.pdf --force
pdfdrill model knot.pdf            ->  131 objects, 182 alignments
pdfdrill embedimages knot.pdf --force
                                   -> 1115 objects, 182 alignments
```

The model grows by **984 `EmbeddedImage` nodes**, an 8.5× inflation in which
about 88% of the model is one-pixel noise. They split exactly in half:

| count | `width_px` × `height_px` | `encoding` | region |
|---|---|---|---|
| 492 | `1 × 1` | `image` | absent |
| 492 | `None × None` | `None` | present |

The underlying file has **492 raster entries and every one is a 1×1 stencil mask
of 1 byte**, inline, with no XObject id — dvips painting artifacts. There is no
real image in the document. The knot figures are vector: 293 curves and 57 lines
across pages 1–6.

```
pdfimages -list pst-knot-doc.pdf | tail -n +3 | awk '$4!=1||$5!=1' | wc -l
0
```

## Two distinct issues

**1. No degenerate-image guard.** 492 one-pixel, one-byte stencil masks become
first-class model objects. `pdfdrill extractimages` documents filtering "tiny
masks/decorative <1KB"; `embedimages` does not appear to apply the same filter.
This is the one that costs, because it is what makes the model 8.5× larger.

**2. Fusion fails for inline images specifically.** The two detector views —
pdfimages (pixel metadata, no region) and pdfplumber (region, no pixel metadata)
— are not matched for inline images, so each physical stencil yields two
half-populated nodes instead of one complete one.

This second one is **narrow, not general.** On the control paper it works
correctly:

| document | raster entries | `EmbeddedImage` nodes | fused? |
|---|---|---|---|
| `2305.04710v1.pdf` | 4 | **2**, both with full dimensions | yes |
| `pst-knot-doc.pdf` | 492 (all inline) | **984**, each half-populated | no |

XObject images carry an id the two views can be matched on. Inline images do
not, so the join key is missing and nothing fuses. The summary line printed by
the command — *"Every route to an image (CDN crop, vision read, XObject
metadata, page rect) now hangs off one graph"* — is not true in the inline case,
and that is worth fixing independently of the behaviour, because it reports
success either way.

## Not a defect — a correction to an earlier reading

The run reports `0 MathPix crop(s) linked ... (Alignment 'image_region')` and
the alignment count does not move (182 before, 182 after; 174 `dehyphenate`,
8 `render`). I first read that as a third defect. It is not: `image_region`
links *MathPix crops* to the image containing them, and neither document was
drilled through MathPix in these runs, so there are no crops to link. Zero is
the correct answer.

## Suggested handling

- Apply `extractimages`' existing sub-1KB / degenerate-dimension filter in
  `embedimages`, or record such images as skips with a reason rather than
  dropping them silently — the project already treats "skipped, with a reason"
  as the correct disposal.
- Match the two detector views on geometry when no XObject id exists, or emit
  one node per physical image with whichever fields are known.
- Make the summary line report what actually fused.

## Reproduce

```bash
export PDFDRILL_NO_PREFLIGHT=1 MATHPIX_APP_ID= MATHPIX_APP_KEY=
pdfdrill ocr pst-knot-doc.pdf --force
pdfdrill model pst-knot-doc.pdf
pdfdrill embedimages pst-knot-doc.pdf --force
python3 -c "
import json, collections
d = json.load(open('model.docmodel.json'))
ei = [o for o in d['objects'] if o['type'] == 'EmbeddedImage']
print(len(d['objects']), 'objects;', len(ei), 'EmbeddedImage')
print(collections.Counter('%sx%s' % (o['props'].get('width_px'),
                                     o['props'].get('height_px')) for o in ei))"
```

Source: <https://ftp.gwdg.de/pub/ctan/graphics/pstricks/contrib/pst-knot/pst-knot-doc.pdf>
