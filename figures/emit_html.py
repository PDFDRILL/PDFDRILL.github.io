"""Emit a self-contained Cytoscape.js page from the figure spec.

Interface contract:
    payload(spec) -> dict     {elements, style, canvas}
    emit(spec, js) -> str     complete HTML

Geometry rules, mirroring emit_mp.py:
  * positions are spec coordinates verbatim (both spec and Cytoscape are y-down)
  * group rectangles are ordinary nodes with explicit w/h, NOT compound parents,
    so their rect equals the spec rect exactly instead of being auto-fitted
  * every text run is its own zero-size element at the same point MetaPost uses,
    so per-run font sizes match instead of collapsing into one multi-line label
  * every edge endpoint is an explicit percentage derived from the same
    figspec.edge_points() the MetaPost emitter uses
"""
import json
import figspec

STYLE = {
    "feed":     ("#3c3836", 0.9, None),
    "fallback": ("#665c54", 0.8, [4, 3]),
    "escalate": ("#af3a03", 1.5, None),
    "store":    ("#7c6f64", 0.8, [2.2, 2.2]),
}


def _pct(rect, pt):
    """Absolute point -> Cytoscape endpoint percentage (0% 0% == node centre)."""
    x0, y0, x1, y1 = rect
    cx, cy = (x0 + x1) / 2.0, (y0 + y1) / 2.0
    w, h = x1 - x0, y1 - y0
    return "%.12g%% %.12g%%" % ((pt[0] - cx) / w * 100.0, (pt[1] - cy) / h * 100.0)


def payload(spec):
    C = spec["canvas"]
    band = C["label_band"]
    pal = spec["palette"]
    res = figspec.resolve(spec)
    els, tid = [], [0]

    def text(x, y, label, fs, weight="normal", family="serif"):
        tid[0] += 1
        els.append({
            "data": {"id": "__t%d" % tid[0], "label": label, "fs": fs,
                     "weight": weight, "family": family},
            "position": {"x": x, "y": y},
            "classes": "txt", "grabbable": False, "selectable": False})

    els.append({
        "data": {"id": "__frame", "w": C["w"], "h": C["h"]},
        "position": {"x": C["w"] / 2.0, "y": C["h"] / 2.0},
        "classes": "frame", "grabbable": False, "selectable": False})

    for g in spec["groups"]:
        p = pal[g["tone"]]
        x0, y0, x1, y1 = figspec.group_rect(g)
        els.append({
            "data": {"id": g["id"], "w": g["w"], "h": g["h"],
                     "fill": p["fill"], "stroke": p["stroke"], "radius": 7,
                     "bw": 0.9, "kind": "group", "title": g["title"]},
            "position": {"x": (x0 + x1) / 2.0, "y": (y0 + y1) / 2.0},
            "classes": "grp", "grabbable": False, "selectable": False})
        text((x0 + x1) / 2.0, y0 + 12, g["title"], 9.5, "bold")
        text((x0 + x1) / 2.0, y0 + 24, g["sub"], 7)

    for n in spec["nodes"]:
        p = pal[n["tone"]]
        store = n.get("shape", "box") == "store"
        fam = "monospace" if n.get("mono") else "serif"
        size = 9 if store else 8.5
        els.append({
            "data": {"id": n["id"], "w": n["w"], "h": n["h"],
                     "fill": p["node"], "stroke": p["stroke"],
                     "radius": 8 if store else 4, "bw": 1.2 if store else 0.8,
                     "kind": "node", "title": n["label"]},
            "position": {"x": n["x"], "y": n["y"]},
            "classes": "nd", "grabbable": False})
        if "sub" in n:
            dy = n["h"] / 4.0
            text(n["x"], n["y"] - dy, n["label"], size,
                 "normal" if n.get("mono") else "bold", fam)
            text(n["x"], n["y"] + dy, n["sub"], 7)
        else:
            text(n["x"], n["y"], n["label"], size,
                 "normal" if n.get("mono") else "bold", fam)

    for e in spec["edges"]:
        p, q = figspec.edge_points(spec, e, res)
        col, wid, dash = STYLE[e["kind"]]
        d = {"id": e["id"], "source": e["from"], "target": e["to"],
             "kind": e["kind"], "col": col, "wid": wid,
             "sep": _pct(res[e["from"]][2], p),
             "tep": _pct(res[e["to"]][2], q)}
        if dash:
            d["dash"] = dash
        els.append({"data": d, "classes": "eg", "selectable": False})

    style = [
        {"selector": "node.grp", "style": {
            "shape": "round-rectangle", "width": "data(w)", "height": "data(h)",
            "corner-radius": "data(radius)",
            "background-color": "data(fill)", "border-color": "data(stroke)",
            "border-width": "data(bw)", "label": "", "z-index": 1,
            "z-index-compare": "manual"}},
        {"selector": "node.nd", "style": {
            "shape": "round-rectangle", "width": "data(w)", "height": "data(h)",
            "corner-radius": "data(radius)",
            "background-color": "data(fill)", "border-color": "data(stroke)",
            "border-width": "data(bw)", "label": "", "z-index": 3,
            "z-index-compare": "manual"}},
        {"selector": "node.txt", "style": {
            "width": 1, "height": 1, "background-opacity": 0, "border-width": 0,
            "events": "no", "label": "data(label)",
            "font-size": "data(fs)", "font-weight": "data(weight)",
            "font-family": "data(family)", "color": "#282828",
            "text-valign": "center", "text-halign": "center",
            "text-wrap": "none", "z-index": 4, "z-index-compare": "manual"}},
        {"selector": "edge.eg", "style": {
            "curve-style": "straight",
            "line-color": "data(col)", "width": "data(wid)",
            "target-arrow-color": "data(col)", "target-arrow-shape": "triangle",
            "arrow-scale": 0.55,
            "source-endpoint": "data(sep)", "target-endpoint": "data(tep)",
            "z-index": 2, "z-index-compare": "manual"}},
        {"selector": "edge[?dash]", "style": {
            "line-style": "dashed", "line-dash-pattern": "data(dash)"}},
        {"selector": "node.frame", "style": {
            "width": "data(w)", "height": "data(h)", "shape": "rectangle",
            "background-opacity": 0, "border-width": 0, "label": "",
            "events": "no", "z-index": 0, "z-index-compare": "manual"}},
        {"selector": "node.nd:active", "style": {"overlay-opacity": 0.12}},
    ]
    return {"elements": els, "style": style, "canvas": C,
            "title": spec.get("title", "figure")}


HTML = """<!DOCTYPE html>
<meta charset="utf-8">
<title>%(title)s</title>
<style>
  html,body{margin:0;background:#fbf9f4;color:#282828;
            font:14px/1.5 Georgia,'Times New Roman',serif}
  main{max-width:%(maxw)dpx;margin:2rem auto;padding:0 1rem}
  h1{font-size:1.15rem;font-weight:normal;margin:0 0 .25rem}
  p.cap{font-size:.8rem;color:#665c54;margin:.25rem 0 1rem}
  #cy{width:100%%;aspect-ratio:%(w)d/%(h)d;background:#fff;
      border:1px solid #d5cdbb;border-radius:4px}
  .bar{margin-top:.6rem;font-size:.75rem;color:#665c54}
  button{font:inherit;font-size:.75rem;padding:.15rem .5rem;margin-right:.3rem;
         background:#f2ece0;border:1px solid #d5cdbb;border-radius:3px;cursor:pointer}
  #sel{font-family:monospace}
</style>
<main>
<h1>%(title)s</h1>
<p class="cap">Drag to pan, scroll to zoom, click a box for its identifier.
Geometry is generated from the same source file as the LaTeX figure.</p>
<div id="cy"></div>
<div class="bar"><button id="fit">reset view</button><span id="sel"></span></div>
</main>
%(script)s
<script>
const PAYLOAD = %(payload)s;
const cy = cytoscape({
  container: document.getElementById('cy'),
  elements: PAYLOAD.elements,
  style: PAYLOAD.style,
  layout: { name: 'preset' },
  minZoom: 0.3, maxZoom: 6, wheelSensitivity: 0.2,
  boxSelectionEnabled: false, autoungrabify: true
});
function fit(){ cy.fit(undefined, 12); }
fit();
document.getElementById('fit').addEventListener('click', fit);
addEventListener('resize', fit);
cy.on('tap', 'node.nd, node.grp', e =>
  document.getElementById('sel').textContent = '  ' + e.target.data('title'));
cy.on('tap', e => { if (e.target === cy)
  document.getElementById('sel').textContent = ''; });
</script>
"""


def emit(spec, js=None, cdn_version=None):
    pl = payload(spec)
    C = pl["canvas"]
    if js is not None:
        script = "<script>%s</script>" % js.replace("</script", "<\\/script")
    else:
        script = ('<script src="https://cdn.jsdelivr.net/npm/cytoscape@%s/'
                  'dist/cytoscape.min.js"></script>' % cdn_version)
    return HTML % {"title": pl["title"], "w": C["w"], "h": C["h"],
                   "maxw": C["w"] + 32, "script": script,
                   "payload": json.dumps(pl, separators=(",", ":"))}


if __name__ == "__main__":
    import sys
    args = sys.argv[1:]
    mode = "--cdn" if "--cdn" in args else "--inline"
    args = [a for a in args if not a.startswith("--")]
    spec = figspec.load(args[0] if args else "pdfdrill-figure.json")
    errs = figspec.validate(spec)
    if errs:
        for e in errs:
            print("SPEC ERROR:", e)
        sys.exit(1)
    out = args[1] if len(args) > 1 else "pdfdrill-figure.html"
    if mode == "--inline":
        js = open("node_modules/cytoscape/dist/cytoscape.min.js",
                  encoding="utf-8").read()
        html = emit(spec, js=js)
    else:
        import re
        v = json.load(open("node_modules/cytoscape/package.json"))["version"]
        html = emit(spec, cdn_version=v)
    with open(out, "w", encoding="utf-8") as fh:
        fh.write(html)
    with open("payload.json", "w", encoding="utf-8") as fh:
        json.dump(payload(spec), fh, indent=1)
    print("wrote %s (%d bytes, %s)" % (out, len(html), mode))
