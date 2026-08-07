# Panel series: one structural JSON per figure -> MetaPost (LaTeX) + Cytoscape.
#
#   make            build every spec in specs/ -> EPS, PDF, SVG, DVI, HTML
#   make install    build, then copy the SVG + HTML panels into ../
#   make png        raster fallback into build/, not installed
#   make docmodel   drill the built figures with pdfdrill
#   make regen      re-emit the specs from make_panels.py
#   make list       validate every spec
#   make clean
#
# Coordinates are never authored. layout.py derives them and figspec.validate
# (C1..C11) is the oracle that the derived geometry is sane.
#
# Requires: texlive-metapost (mpost + latex), ghostscript, poppler-utils,
# python3, and `npm install cytoscape` — the last only to read the version
# number that goes into the CDN URL. ImageMagick is needed for `make png` only.

SPECS  := $(wildcard specs/*.fig.json)
IDS    := $(notdir $(basename $(basename $(SPECS))))
PY     := python3
SITE   := ..
# NOTE: no trailing comments on these two. Make keeps the whitespace before a
# comment in the value, so `-resize $(WIDTH)x` would split into `-resize 1408`
# plus a stray `x` that ImageMagick tries to open as a file.
WIDTH  := 1408
DPI    := 300

.PHONY: all install png regen list clean docmodel
all: node_modules/cytoscape
	./buildall.sh

node_modules/cytoscape:
	npm install cytoscape --no-audit --no-fund

# The SVG is what the page shows; the HTML is the interactive version beside it.
# Both come from the same spec, so they cannot disagree. SVG rather than PNG
# because MetaPost emits it directly, it costs the same on disk (~900 KB for
# the series either way) and it stays sharp at any zoom or pixel density.
install: all
	@for id in $(IDS); do \
	  cp build/$$id.svg  $(SITE)/fig-$$id.svg; \
	  cp build/$$id.html $(SITE)/fig-$$id.html; \
	  printf "  fig-%-24s %6s bytes\n" "$$id.svg" "$$(stat -c%s $(SITE)/fig-$$id.svg)"; \
	done
	@echo "installed $(words $(IDS)) panels into $(SITE)/"

# A raster fallback, if one is ever wanted. Do NOT trim the output:
# canvas.aspect pads every panel to the same H/W on purpose so the series sits
# together, and trimming throws that away — the eight stop matching.
png: all
	@for id in $(IDS); do \
	  pdftoppm -r $(DPI) -png -singlefile build/$$id.pdf build/hi-$$id; \
	  magick build/hi-$$id.png -resize $(WIDTH)x -strip \
	         -define png:compression-level=9 build/fig-$$id.png; \
	  printf "  build/fig-%-20s %s\n" "$$id.png" \
	         "$$(identify -format '%wx%h' build/fig-$$id.png)"; \
	done

# Drill the site's own figures with the tool the site documents. The eight
# panels are concatenated into one PDF and run through the keyless born-digital
# route, producing pdfdrill-figures.docmodel.json plus an inspector.
#
# Worth knowing what comes out: 8 pages -> 8 Paragraphs, one blob per page.
# MetaPost emits positioned text runs with no paragraph structure, so the
# series reproduces exactly the failure section 04 of the site describes.
docmodel: all
	pdfunite build/overview.pdf build/layer1-document.pdf build/layer2-probe.pdf \
	         build/layer3-structure.pdf build/layer4-model.pdf \
	         build/layer5-provenance.pdf build/layer6-project.pdf \
	         build/layer7-qc.pdf build/pdfdrill-figures.pdf
	@W=$$(mktemp -d); mkdir -p $$W/lib/pdfdrill-figures $$W/dl; \
	 printf '{"library_root":"%s/lib","download_dir":"%s/dl"}\n' $$W $$W > $$W/config.json; \
	 cp build/pdfdrill-figures.pdf $$W/lib/pdfdrill-figures/; \
	 PDFDRILL_CONFIG=$$W/config.json PDFDRILL_NO_PREFLIGHT=1 \
	 MATHPIX_APP_ID= MATHPIX_APP_KEY= \
	   $(PY) -m pdfdrill model   $$W/lib/pdfdrill-figures/pdfdrill-figures.pdf; \
	 PDFDRILL_CONFIG=$$W/config.json PDFDRILL_NO_PREFLIGHT=1 \
	 MATHPIX_APP_ID= MATHPIX_APP_KEY= \
	   $(PY) -m pdfdrill inspect $$W/lib/pdfdrill-figures/pdfdrill-figures.pdf; \
	 cp $$W/lib/pdfdrill-figures/model.docmodel.json ./pdfdrill-figures.docmodel.json; \
	 cp $$W/lib/pdfdrill-figures/pdfdrill-figures.inspect.html $(SITE)/fig-series.inspect.html; \
	 cp build/pdfdrill-figures.pdf ./pdfdrill-figures.pdf; \
	 rm -rf $$W
	@echo "wrote pdfdrill-figures.docmodel.json and $(SITE)/fig-series.inspect.html"

regen:
	$(PY) make_panels.py

list:
	@for f in $(SPECS); do printf "  %-34s " $$(basename $$f); \
	  $(PY) figtool.py validate $$f | tail -1; done

clean:
	rm -rf build
