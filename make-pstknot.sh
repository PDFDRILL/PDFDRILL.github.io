#!/usr/bin/env bash
# Regenerate the pst-knot inspect artifacts used by the "when the text layer
# lies" section of index.html.
#
# Produces, in this directory:
#   pst-knot-doc.textlayer.inspect.html   born-digital text layer (pdfminer.six)
#   pst-knot-doc.ocr.inspect.html         tesseract raster pass (ocr --force)
#
# The MathPix artifact (pst-knot-doc.mathpix.inspect.html) is NOT regenerated
# here — it needs paid keys. That asymmetry is the point of the section.
#
# Requires pdfdrill on PYTHONPATH (https://github.com/WulfKolbe/pdfdrill),
# poppler-utils and tesseract. Run `pdfdrill doctor` if something is missing.

set -euo pipefail

OUT_DIR="$(cd "$(dirname "$0")" && pwd)"
URL=https://ftp.gwdg.de/pub/ctan/graphics/pstricks/contrib/pst-knot/pst-knot-doc.pdf

# A PERSISTENT work directory, not mktemp -d, and deliberately not wiped.
#
# pdfdrill assigns fresh random object and alignment ids on every clean model
# build, so two clean builds of identical content emit different ids and a ~1 MB
# spurious git diff. Re-running against an existing sidecar reuses the ids, so
# keeping this directory makes repeated regeneration byte-stable.
#
# Gitignored. Delete it to force a clean rebuild — which WILL renumber every id
# and produce a large diff in the two committed artifacts, with no change in the
# extracted content.
WORK="$OUT_DIR/.pstknot-work"

# Isolate: our own library root and download dir, and no MathPix credentials.
# The real environment beats any .env file, so blanking the keys here forces
# `model` down the born-digital text-layer route rather than MathPix.
mkdir -p "$WORK/lib" "$WORK/dl"
printf '{\n  "library_root": "%s/lib",\n  "download_dir": "%s/dl"\n}\n' \
       "$WORK" "$WORK" > "$WORK/config.json"
export PDFDRILL_CONFIG="$WORK/config.json"
export PDFDRILL_NO_PREFLIGHT=1
export MATHPIX_APP_ID=
export MATHPIX_APP_KEY=

echo "==> fetching pst-knot-doc.pdf"
python3 -m pdfdrill size "$URL" >/dev/null
SRC="$WORK/lib/pst-knot-doc/pst-knot-doc.pdf"
[ -f "$SRC" ] || { echo "download failed: $SRC missing" >&2; exit 1; }

# Two independent working copies under distinct stems. Neither run can observe
# the other's sidecar, so either artifact can be regenerated on its own.
for stem in textlayer ocr; do
  mkdir -p "$WORK/lib/pstknot-$stem"
  cp "$SRC" "$WORK/lib/pstknot-$stem/pstknot-$stem.pdf"
done

echo "==> route 1: born-digital text layer"
python3 -m pdfdrill model   "$WORK/lib/pstknot-textlayer/pstknot-textlayer.pdf"
python3 -m pdfdrill inspect "$WORK/lib/pstknot-textlayer/pstknot-textlayer.pdf"

echo "==> route 2: tesseract raster pass"
# Only OCR when there is no lines.json yet. Re-running `ocr --force` would
# rebuild it and renumber every id, which is what makes the emitted artifact
# byte-unstable across runs.
if [ ! -f "$WORK/lib/pstknot-ocr/pstknot-ocr.lines.json" ]; then
  python3 -m pdfdrill ocr   "$WORK/lib/pstknot-ocr/pstknot-ocr.pdf" --force
else
  echo "    (lines.json present — reusing it; delete .pstknot-work to re-OCR)"
fi
python3 -m pdfdrill model   "$WORK/lib/pstknot-ocr/pstknot-ocr.pdf"
python3 -m pdfdrill inspect "$WORK/lib/pstknot-ocr/pstknot-ocr.pdf"

# Deliberately NOT run: `pdfdrill embedimages`. On this document it lifts 492
# 1x1 stencil masks (dvips painting artifacts, 1 byte each) into 984
# EmbeddedImage nodes and takes the model from 131 to 1115 objects. See the
# design spec for the measurement.

cp "$WORK/lib/pstknot-textlayer/pstknot-textlayer.inspect.html" \
   "$OUT_DIR/pst-knot-doc.textlayer.inspect.html"
cp "$WORK/lib/pstknot-ocr/pstknot-ocr.inspect.html" \
   "$OUT_DIR/pst-knot-doc.ocr.inspect.html"

echo
echo "==> element counts (inspect shows non-Page objects)"
for r in textlayer ocr; do
  python3 - "$WORK/lib/pstknot-$r/model.docmodel.json" "$r" <<'PY'
import json, sys, collections
d = json.load(open(sys.argv[1]))
objs = d.get("objects") or []
if isinstance(objs, dict):
    objs = list(objs.values())
c = collections.Counter(o.get("type") for o in objs)
print(f"    {sys.argv[2]:10s} {len(objs) - c['Page']:4d} elements   {dict(c.most_common())}")
PY
done
echo
echo "wrote pst-knot-doc.textlayer.inspect.html and pst-knot-doc.ocr.inspect.html"
