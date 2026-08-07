#!/bin/bash
# Build every spec into: .flat.json + .mp + .html, then EPS, PDF, SVG and DVI.
#
#   EPS   mpost, the primary vector output
#   PDF   gs from the EPS, for pdflatex \includegraphics
#   SVG   mpost again with outputformat := "svg" — MetaPost 3 emits real SVG,
#         glyphs as reusable <use> symbols, no font dependency. This is the
#         web-facing one; it is what index.html shows.
#   DVI   a standalone LaTeX wrapper around the EPS, for DVI-based workflows.
#         dvisvgm converts it too, at the cost of flattening every glyph to a
#         separate path (~18% larger than the MetaPost SVG), which is why the
#         SVG above comes from MetaPost rather than from here.
#
# The HTML is emitted WITHOUT --inline: it loads Cytoscape from a CDN. These
# figures are served from GitHub Pages, so a 435 KB copy of the library per
# panel buys nothing.
set -u
mkdir -p build; fail=0
for f in specs/*.fig.json; do
  id=$(python3 -c "import json;print(json.load(open('$f'))['id'])")
  if ! python3 figtool.py build "$f" --outdir build >/dev/null; then
    echo "  BUILD FAIL $id"; fail=1; continue; fi

  # --- EPS (and the label widths the fit test reads)
  ( cd build && rm -f labelwidths.txt && \
    timeout 180 mpost -tex=latex -interaction=nonstopmode "$id.mp" </dev/null >/dev/null 2>&1 )
  err=$(grep -c '^! ' "build/$id.log" 2>/dev/null); err=${err:-0}

  # --- PDF
  ( cd build && gs -dNOPAUSE -dBATCH -dQUIET -dEPSCrop -sDEVICE=pdfwrite \
      -dEmbedAllFonts=true -sOutputFile="$id.pdf" "$id.eps" 2>/dev/null )

  # --- SVG. The emitted .mp hardcodes its own outputtemplate, and -s runs
  # before the file, so a command-line override loses. Derive a sibling .mp
  # with the two lines swapped instead. Jobname is "$id-svg", hence the rename.
  ( cd build && sed 's|outputtemplate := "%j.eps";|outputformat := "svg";\
outputtemplate := "%j.svg";|' "$id.mp" > "$id-svg.mp" && \
    timeout 180 mpost -tex=latex -interaction=nonstopmode "$id-svg.mp" </dev/null >/dev/null 2>&1 && \
    mv -f "$id-svg.svg" "$id.svg" 2>/dev/null )
  serr=$(grep -c '^! ' "build/$id-svg.log" 2>/dev/null); serr=${serr:-0}
  [ "$serr" -ne 0 ] && { echo "  SVG FAIL $id ($serr mpost errors)"; fail=1; }

  # --- DVI
  ( cd build && printf '%s\n' \
      '\documentclass[border=0pt]{standalone}' \
      '\usepackage{graphicx}' \
      '\begin{document}' \
      "\\includegraphics{$id.eps}" \
      '\end{document}' > "$id-dvi.tex" && \
    timeout 180 latex -interaction=nonstopmode "$id-dvi.tex" </dev/null >/dev/null 2>&1 && \
    mv -f "$id-dvi.dvi" "$id.dvi" 2>/dev/null )

  fit=$(cd build && python3 -c "
import sys; sys.path.insert(0,'..'); sys.argv=['x','$id.flat.json','labelwidths.txt']
exec(open('../test2_fit.py').read())" 2>&1 | tail -1 | sed 's/^ *//')
  sz=$(pdfinfo "build/$id.pdf" 2>/dev/null | awk -F: '/Page size/{print $2}' | xargs)
  got=""
  for ext in eps pdf svg dvi html; do
    [ -s "build/$id.$ext" ] && got="$got $ext" || got="$got -$ext"
  done
  printf "  %-20s err=%s %-26s %s\n" "$id" "$err" "$got" "$sz"
  [ "$err" -ne 0 ] && fail=1
done
echo "buildall fail=$fail"; exit $fail
