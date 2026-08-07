#!/usr/bin/env python3
"""Write the structural specs for the panel series.

Each spec carries the prompt it came from, so the prose description and the
machine-readable structure stay in one file. Coordinates appear nowhere.
"""
import json
import os

ASPECT = 512 / 279.0          # the aspect the original panel series was drawn at

PALETTE = {
    "paper": {"fill": "#eef0e6", "stroke": "#6b7363", "node": "#f8f9f4"},
    "sage":  {"fill": "#dde5d5", "stroke": "#6f7d63", "node": "#eff3ec"},
    "olive": {"fill": "#e5e7cf", "stroke": "#7a7f2c", "node": "#f3f4e7"},
    "ochre": {"fill": "#efe2c6", "stroke": "#a8801f", "node": "#f9f2e1"},
    "ink":   {"fill": "#dcdcd4", "stroke": "#3a3a35", "node": "#eeeee9"},
    "rail":  {"fill": "#d9d3c0", "stroke": "#4a463c", "node": "#e9e4d4"},
    "flag":  {"fill": "#f2ddc0", "stroke": "#b06a1a", "node": "#fbf1df"},
}

STYLE_NOTE = (
    "SHARED STYLE: muted sage green / olive / warm ochre on cream paper, "
    "charcoal ink linework. One titled card as the subject, with a persistent "
    "horizontal 'memory rail' (the sidecar) along the bottom edge that visibly "
    "grows from panel to panel. Panel {n} of 7, left-to-right pipeline; "
    "same aspect ratio across the whole series."
)


def node(nid, label, tone="sage", mono=False, sub=None, w=None):
    el = {"kind": "node", "id": nid, "label": label, "tone": tone}
    if mono:
        el["mono"] = True
    if sub:
        el["sub"] = sub
    if w:
        el["w"] = w
    return el


def row(children, gap=12, **kw):
    return dict(kind="row", gap=gap, children=children, **kw)


def col(children, gap=8, **kw):
    return dict(kind="col", gap=gap, children=children, **kw)


def group(gid, title, sub, children, tone="sage", direction="col", gap=8):
    return {"kind": "group", "id": gid, "title": title, "sub": sub,
            "tone": tone, "dir": direction, "gap": gap, "children": children}


def rail(sub, tone="rail"):
    return node("rail", "sidecar", tone=tone, sub=sub)


def panel(n, pid, title, prompt, card, edges, extra=None):
    kids = [card] + (extra or []) + [rail_of(card)]
    return {
        "id": pid, "n": n, "title": title,
        "prompt": STYLE_NOTE.format(n=n) + "\n\n" + prompt,
        "canvas": {"pad": 22, "gap": 16, "group_pad": 12,
                   "label_band": 32, "aspect": ASPECT},
        "palette": PALETTE,
        "root": {"kind": "col", "gap": 18, "children": kids},
        "edges": edges,
    }


_RAILS = {}


def rail_of(card):
    return _RAILS[card["id"]]


# --------------------------------------------------------------------------
PANELS = []

# ---- 1 : the PDF as it really is -----------------------------------------
card = group("pdfdoc", "Layer 1 - PDF document",
             "the file as it really is", [
                 row([
                     col([node("textlayer", "text layer", "sage",
                               sub="headings, paragraphs"),
                          node("fontlayer", "font layer", "sage",
                               sub="proves born-digital")], gap=8),
                     group("annot", "annotation layer",
                           "dropped by every naive reader", [
                               node("hlink", "hyperlink", "ochre",
                                    sub="no visible anchor text"),
                               node("dest", "named destination", "ochre",
                                    sub="jump target"),
                           ], tone="ochre"),
                     node("scanned", "scanned page", "ink",
                          sub="no text layer, OCR required"),
                 ], gap=18),
             ])
_RAILS["pdfdoc"] = rail("empty - nothing recorded yet")
PANELS.append(panel(
    1, "layer1-document", "Layer 1 - PDF document",
    "The card shows one paper page: heading bar, two columns of ruled text, "
    "one figure box. A translucent overlay peels up off the page revealing a "
    "hidden hyperlink marker ('here ->') that has NO visible anchor text, plus "
    "two map-pin named-destination markers. Behind it a ghosted second page is "
    "stamped 'scanned - no text layer', contrasting born-digital with scanned. "
    "The memory rail at the bottom is still empty.\n\n"
    "How to see it: pdfdrill size reports born-digital vs scanned; "
    "pdfdrill links surfaces the hidden link in ~50 ms.",
    card, [{"id": "r1", "from": "pdfdoc", "to": "rail", "kind": "store",
            "from_side": "bottom", "to_side": "top"}]))

# ---- 2 : L0 probe ---------------------------------------------------------
card = group("probe", "Layer 2 - L0 probe",
             "reads metadata, extracts nothing", [
                 row([node("size", "size", "olive", mono=True),
                      node("pdfinfo", "pdfinfo", "olive", mono=True),
                      node("links", "links", "olive", mono=True),
                      node("dests", "dests", "olive", mono=True)], gap=12),
                 row([node("toggle", "text layer / scan", "ink",
                           sub="page-1 char count decides"),
                      node("watch", "approx. 50 ms", "ink",
                           sub="no extraction")], gap=18),
             ], tone="olive")
_RAILS["probe"] = rail("3 facts written: size, links, dests")
PANELS.append(panel(
    2, "layer2-probe", "Layer 2 - L0 shallow probe",
    "Card labelled 'L0 probe'. A sparse row of tool gauges: a ruler gauge "
    "'size', a chip 'fonts', a chain icon 'links', an anchor pin 'dests'. A "
    "two-state toggle reads 'text layer / scan'. A stopwatch reads '~50 ms'. A "
    "thin pipe drops three small fact cards DOWN into the memory rail, which "
    "now holds a few cards. Deliberately sparse - this tier reads metadata, it "
    "does NOT pull paragraphs.\n\n"
    "How to see it: pdfdrill size / links / dests, each returning one sentence "
    "of prose; facts persist so re-runs are instant.",
    card, [{"id": "r1", "from": "probe", "to": "rail", "kind": "store",
            "from_side": "bottom", "to_side": "top"}]))

# ---- 3 : structural extraction -------------------------------------------
card = group("structure", "Layer 3 - L1/L2 structure",
             "the first real content", [
                 row([
                     group("l1", "L1 cheap", "what is it about", [
                         node("abstract", "abstract", "sage", mono=True),
                         node("toc", "toc", "sage", mono=True),
                         node("fonts", "fonts", "sage", mono=True)], tone="sage"),
                     group("l2", "L2 work", "real extraction", [
                         node("md", "md", "ochre", mono=True),
                         node("pagen", "page N", "ochre", mono=True)],
                         tone="ochre"),
                     node("math", "math detected", "ink",
                          sub="math fonts present"),
                 ], gap=18),
             ], tone="sage")
_RAILS["structure"] = rail("+ cached markdown, toc")
PANELS.append(panel(
    3, "layer3-structure", "Layer 3 - structural extraction",
    "Card labelled 'L1-L2 structure'. An 'abstract' ribbon across the top; a "
    "nested table-of-contents tree; a badge indicating math fonts were "
    "detected; a Markdown page emerging at the right with paragraph blocks and "
    "one code-fence glyph. A staircase of arrows shows the chain "
    "size -> fonts -> abstract -> toc -> md. More fact cards drop into the "
    "memory rail, now noticeably fuller.\n\n"
    "How to see it: pdfdrill abstract / toc / fonts, then md / page N. The "
    "Markdown is cached, so a later command never re-extracts.",
    card, [
        {"id": "c1", "from": "l1", "to": "l2", "kind": "escalate",
         "from_side": "right", "to_side": "left"},
        {"id": "r1", "from": "structure", "to": "rail", "kind": "store",
         "from_side": "bottom", "to_side": "top"}]))

# ---- 4 : the typed model --------------------------------------------------
card = group("model", "Layer 4 - L3 model",
             "flat extraction becomes a typed, queryable graph", [
                 group("textstream", "text stream", "opaque anchors, not positions", [
                     row([node("para", "paragraph", "sage"),
                          node("eqn", "equation", "sage"),
                          node("sect", "section", "sage"),
                          node("tbl", "table", "sage")], gap=12)],
                     tone="sage"),
                 group("regionstream", "region stream", "page geometry", [
                     row([node("rpara", "region", "ochre"),
                          node("reqn", "region", "ochre"),
                          node("rsect", "region", "ochre"),
                          node("rtbl", "region", "ochre")], gap=12)],
                     tone="ochre"),
             ], tone="ink")
_RAILS["model"] = rail("docmodel.json - the between-call memory")
PANELS.append(panel(
    4, "layer4-model", "Layer 4 - the unified docmodel",
    "Card labelled 'L3 model'. NOT 'user intent' - that was invented. A "
    "node-link graph where node SHAPE encodes TYPE: square = paragraph, "
    "circle = equation, triangle = figure, grid = table, hexagon = section. "
    "Each node carries a tiny anchor-pin id. TWO parallel horizontal lanes "
    "('text stream' / 'region stream') with dashed alignment links between "
    "corresponding nodes. A faint dashed bounding box on one node shows region "
    "geometry. The memory rail now shows one larger block 'docmodel.json'.\n\n"
    "How to see it: pdfdrill model (offline if a lines.json exists).",
    card, [
        {"id": "a1", "from": "para", "to": "rpara", "kind": "fallback",
         "from_side": "bottom", "to_side": "top"},
        {"id": "a2", "from": "eqn", "to": "reqn", "kind": "fallback",
         "from_side": "bottom", "to_side": "top"},
        {"id": "a3", "from": "sect", "to": "rsect", "kind": "fallback",
         "from_side": "bottom", "to_side": "top"},
        {"id": "a4", "from": "tbl", "to": "rtbl", "kind": "fallback",
         "from_side": "bottom", "to_side": "top"},
        {"id": "r1", "from": "model", "to": "rail", "kind": "store",
         "from_side": "bottom", "to_side": "top"}]))

# ---- 5 : provenance drill -------------------------------------------------
card = group("drill", "Layer 5 - drill / provenance",
             "one equation read four ways, each scored", [
                 row([node("mathpix", "mathpix", "sage", mono=True, sub="1.00"),
                      node("snip", "snip", "sage", mono=True, sub="0.99"),
                      node("vision", "vision", "sage", mono=True, sub="0.97"),
                      node("texgold", "latex", "ochre", mono=True,
                           sub="gold .tex")], gap=12),
                 node("crop", "equation crop", "ink",
                      sub="the image mathpix actually read"),
                 row([node("escalate", "escalate", "flag", mono=True,
                           sub="export the shaky ones"),
                      node("ingest", "ingest", "flag", mono=True,
                           sub="take the second reading"),
                      node("relearn", "relearn", "flag", mono=True,
                           sub="re-score")], gap=12),
             ], tone="ink")
_RAILS["drill"] = rail("+ latex_prov and score_prov per equation")
PANELS.append(panel(
    5, "layer5-provenance", "Layer 5 - drill and provenance",
    "Card labelled 'drill provenance'. Centre: ONE equation crop as an "
    "abstract boxed glyph cluster, not a real formula. Fanning out around it, "
    "four small reading cards 'mathpix', 'snip', 'vision', 'tex (gold)', each "
    "with a circular score dial 0-1. A circular feedback arrow loops the whole "
    "cluster, labelled 'escalate -> ingest -> relearn'. Three dials green "
    "(resolved), one amber (still-shaky). The memory rail gains score "
    "columns.\n\n"
    "How to see it: pdfdrill mathpix, then snip / candidates / vision / latex; "
    "close the loop with escalate -> ingest -> relearn. On a real run: "
    "9 flagged, 7 resolved, 1 correctly retained.",
    card, [
        {"id": "f1", "from": "mathpix", "to": "crop", "kind": "feed"},
        {"id": "f2", "from": "snip", "to": "crop", "kind": "feed"},
        {"id": "f3", "from": "vision", "to": "crop", "kind": "feed"},
        {"id": "f4", "from": "texgold", "to": "crop", "kind": "feed"},
        {"id": "l1", "from": "crop", "to": "escalate", "kind": "escalate"},
        {"id": "l2", "from": "escalate", "to": "ingest", "kind": "escalate",
         "from_side": "right", "to_side": "left"},
        {"id": "l3", "from": "ingest", "to": "relearn", "kind": "escalate",
         "from_side": "right", "to_side": "left"},
        {"id": "r1", "from": "drill", "to": "rail", "kind": "store",
         "from_side": "bottom", "to_side": "top"}]))

# ---- 6 : projection -------------------------------------------------------
card = group("project", "Layer 6 - project",
             "one node becomes one tiddler", [
                 row([
                     group("graph", "typed graph", "from layer 4", [
                         row([node("gpara", "paragraph", "sage"),
                              node("geqn", "equation", "sage")], gap=10)],
                         tone="sage"),
                     node("projector", "projector", "ochre", mono=True,
                          sub="a docops Projector"),
                     node("tiddler", "tiddler", "olive", mono=True,
                          sub="one record per DocObject"),
                     node("wiki", "TiddlyWiki", "ink",
                          sub="one self-contained HTML file"),
                 ], gap=16),
             ], tone="olive")
_RAILS["project"] = rail("read back by the projector")
PANELS.append(panel(
    6, "layer6-project", "Layer 6 - projection to a new document",
    "Card labelled 'project'. The typed node graph from the previous panel "
    "feeds LEFT-to-RIGHT through a small funnel/lens labelled 'projector' and "
    "emerges as a neat stack of identical 'tiddler' record-cards, each with a "
    "title bar and a few field lines. The stack assembles into a single "
    "browser window on the right showing live-rendered equation glyphs. One "
    "arrow makes the 'one node -> one tiddler' mapping explicit. The memory "
    "rail feeds UP into the projector.\n\n"
    "How to see it: pdfdrill tiddlers. Real output: 2004.05631v1.html, "
    "heimUFT.html, kolbe2018hubbard.html - each a single self-contained wiki.",
    card, [
        {"id": "p1", "from": "graph", "to": "projector", "kind": "feed",
         "from_side": "right", "to_side": "left"},
        {"id": "p2", "from": "projector", "to": "tiddler", "kind": "feed",
         "from_side": "right", "to_side": "left"},
        {"id": "p3", "from": "tiddler", "to": "wiki", "kind": "feed",
         "from_side": "right", "to_side": "left"},
        {"id": "r1", "from": "rail", "to": "projector", "kind": "store",
         "from_side": "top", "to_side": "bottom"}]))

# ---- 7 : QC report --------------------------------------------------------
card = group("qc", "Layer 7 - QC report",
             "LaTeX, KaTeX render and the image it was read from", [
                 row([node("hdr1", "LaTeX", "ink"),
                      node("hdr2", "KaTeX", "ink"),
                      node("hdr3", "image", "ink"),
                      node("hdr4", "score", "ink")], gap=10),
                 row([node("r1c1", "source", "sage"),
                      node("r1c2", "render", "sage"),
                      node("r1c3", "page crop", "sage"),
                      node("r1c4", "1.00", "sage")], gap=10),
                 row([node("r2c1", "source", "sage"),
                      node("r2c2", "render", "sage"),
                      node("r2c3", "page crop", "sage"),
                      node("r2c4", "0.99", "sage")], gap=10),
                 row([node("r3c1", "source", "flag"),
                      node("r3c2", "render", "flag"),
                      node("r3c3", "page crop", "flag"),
                      node("r3c4", "0.62", "flag")], gap=10),
             ], tone="ochre")
_RAILS["qc"] = rail("full - every provenance column feeds the table")
PANELS.append(panel(
    7, "layer7-qc", "Layer 7 - final QA and HTML output",
    "Card labelled 'QC report'. A clean 3-column comparison table with real "
    "header labels 'LaTeX | KaTeX | image'. Three or four rows: left cell = "
    "abstract code-line marks; middle = a neatly drawn rendered-equation "
    "glyph; right = a small cropped page-image snippet. A score chip per row "
    "('0.99', '1.00'), with ONE row flagged amber for a mismatch. A green wax "
    "seal 'QC ok' in the corner. The memory rail is full and feeds into the "
    "table. This is the only panel allowed a literal table.\n\n"
    "How to see it: pdfdrill report --embed produces a self-contained "
    "formula-report.html; --embed base64-inlines every crop so the artifact "
    "has no live-CDN dependency.",
    card, [{"id": "r1", "from": "rail", "to": "qc", "kind": "store",
            "from_side": "top", "to_side": "bottom"}]))


def main():
    out = "specs"
    os.makedirs(out, exist_ok=True)
    for p in PANELS:
        path = os.path.join(out, p["id"] + ".fig.json")
        with open(path, "w", encoding="utf-8") as fh:
            json.dump(p, fh, indent=2, ensure_ascii=False)
            fh.write("\n")
        print("wrote", path)


if __name__ == "__main__":
    main()


# ---- 0 : the overview (the whole ladder on one card) ----------------------
def _overview():
    ladder = row([
        group("l0", "L0 - free", "approx. 40-60 ms", [
            node("size", "size", "olive", mono=True),
            node("pdfinfo", "pdfinfo", "olive", mono=True),
            node("links", "links", "olive", mono=True),
            node("dests", "dests", "olive", mono=True)], tone="olive"),
        group("l1", "L1 - cheap", "cached, milliseconds", [
            node("abstract", "abstract", "sage", mono=True),
            node("toc", "toc", "sage", mono=True),
            node("fonts", "fonts", "sage", mono=True)], tone="sage"),
        group("l2", "L2 - work", "approx. 1 s", [
            node("md", "md", "ochre", mono=True),
            node("pagen", "page N", "ochre", mono=True),
            node("drill", "drill", "ochre", mono=True)], tone="ochre"),
        group("l3", "L3 - model", "offline, from lines.json", [
            node("model", "model", "ink", mono=True),
            node("compare", "compare", "ink", mono=True),
            node("report", "report", "ink", mono=True),
            node("tiddlers", "tiddlers", "ink", mono=True)], tone="ink"),
    ], gap=26, align="start")

    top = row([
        node("pdf", "PDF file", "paper"),
        group("prov", "competing readings", "scored provenance columns", [
            row([node("snip", "snip", "sage", mono=True),
                 node("vision", "vision", "sage", mono=True),
                 node("latex", "latex", "sage", mono=True)], gap=10)],
            tone="sage"),
        col([row([node("mathpix", "mathpix", "paper", mono=True, sub="keyed"),
                  node("ocr", "ocr", "paper", mono=True, sub="keyless")], gap=12),
             node("linesjson", "lines.json", "rail", mono=True)], gap=10),
    ], gap=26, align="end")

    spec = {
        "id": "overview", "n": 0,
        "title": "pdfdrill - drill-depth escalation over a shared sidecar",
        "prompt": STYLE_NOTE.format(n=0) + "\n\n"
        "The overview card: four escalation levels L0..L3 side by side over one "
        "shared sidecar rail that every command writes facts into, so a higher "
        "level never repeats a lower one. Above them, the PDF enters at the "
        "left; mathpix (keyed) and ocr (keyless) produce the lines.json that "
        "the offline L3 path consumes; the competing readings feed L3 as "
        "scored provenance columns.",
        "canvas": {"pad": 22, "gap": 16, "group_pad": 12,
                   "label_band": 32, "aspect": ASPECT},
        "palette": PALETTE,
        "root": {"kind": "col", "gap": 22, "children": [
            top, ladder,
            node("rail", "sidecar",
                 sub="every command records facts here; a re-run answers instantly",
                 tone="rail")]},
        "edges": [
            {"id": "e1", "from": "pdf", "to": "l0", "kind": "feed",
             "from_side": "bottom", "to_side": "top"},
            {"id": "e2", "from": "mathpix", "to": "linesjson", "kind": "feed"},
            {"id": "e3", "from": "ocr", "to": "linesjson", "kind": "fallback"},
            {"id": "e4", "from": "linesjson", "to": "l3", "kind": "feed",
             "from_side": "bottom", "to_side": "top"},
            {"id": "e5", "from": "prov", "to": "l3", "kind": "feed"},
            {"id": "e6", "from": "l0", "to": "l1", "kind": "escalate",
             "from_side": "right", "to_side": "left"},
            {"id": "e7", "from": "l1", "to": "l2", "kind": "escalate",
             "from_side": "right", "to_side": "left"},
            {"id": "e8", "from": "l2", "to": "l3", "kind": "escalate",
             "from_side": "right", "to_side": "left"},
            {"id": "e9", "from": "l0", "to": "rail", "kind": "store",
             "from_side": "bottom", "to_side": "top"},
            {"id": "e10", "from": "l1", "to": "rail", "kind": "store",
             "from_side": "bottom", "to_side": "top"},
            {"id": "e11", "from": "l2", "to": "rail", "kind": "store",
             "from_side": "bottom", "to_side": "top"},
            {"id": "e12", "from": "l3", "to": "rail", "kind": "store",
             "from_side": "bottom", "to_side": "top"},
        ]}
    return spec


PANELS.insert(0, _overview())


if __name__ == "__main__":
    main()
