"""Compile a structural figure spec into the flat spec the emitters consume.

Interface contract:
    compile(src) -> flat            flat spec, identical shape to what
                                    emit_mp.py / emit_html.py already read
    measure(el, ctx) -> (w, h)      intrinsic size of one element
    place(el, x, y, ctx, out)       assign absolute coordinates

The structural spec carries NO x/y. Authors describe nesting; this module
derives geometry. Everything downstream (figspec.validate, both emitters,
the whole test suite) is unchanged.

Element kinds
    node    leaf box. w/h optional; derived from the label when absent.
    group   titled container: label band on top, children below.
    row     horizontal container.
    col     vertical container.
    spacer  fixed empty box.

Containers take `gap` (between children) and `pad` (inside edge).
`stretch` (default true) gives every child of a col the same width, and every
child of a row the same height, which is what makes stacks line up.
"""
import math

# advance width per character, in bp, measured against the cmtt/cmr metrics
# that T2.2 checks; deliberately generous so the fit test has slack to report.
CW_MONO   = 5.05
CW_SERIF  = 4.95
CW_SMALL  = 3.65
LABEL_PAD = 26.0

DEF_H     = 24.0
DEF_SUB_H = 34.0


def _text_w(s, cw):
    return len(s) * cw


def est_node_w(el):
    lab = _text_w(el.get("label", ""), CW_MONO if el.get("mono") else CW_SERIF)
    sub = _text_w(el.get("sub", ""), CW_SMALL) if "sub" in el else 0.0
    return math.ceil(max(lab, sub) + LABEL_PAD)


def est_group_w(el):
    t = _text_w(el.get("title", ""), 5.45)
    s = _text_w(el.get("sub", ""), CW_SMALL)
    return math.ceil(max(t, s) + LABEL_PAD)


def measure(el, ctx):
    kind = el["kind"]
    if kind == "spacer":
        return (float(el.get("w", 0)), float(el.get("h", 0)))

    if kind == "node":
        w = float(el["w"]) if "w" in el else est_node_w(el)
        h = float(el["h"]) if "h" in el else (DEF_SUB_H if "sub" in el else DEF_H)
        el["_w"], el["_h"] = w, h
        return (w, h)

    children = el.get("children", [])
    gap = float(el.get("gap", ctx["gap"]))
    dims = [measure(c, ctx) for c in children]

    inner_dir = el.get("dir", "col") if kind == "group" else kind
    if inner_dir == "row":
        cw = sum(d[0] for d in dims) + gap * max(0, len(dims) - 1)
        ch = max([d[1] for d in dims], default=0.0)
    else:
        cw = max([d[0] for d in dims], default=0.0)
        ch = sum(d[1] for d in dims) + gap * max(0, len(dims) - 1)

    if kind == "group":
        pad = float(el.get("pad", ctx["group_pad"]))
        w = max(cw + 2 * pad, est_group_w(el))
        h = ch + 2 * pad + ctx["label_band"]
        el["_w"], el["_h"], el["_cw"], el["_ch"] = w, h, cw, ch
        return (w, h)

    pad = float(el.get("pad", 0))
    w, h = cw + 2 * pad, ch + 2 * pad
    el["_w"], el["_h"], el["_cw"], el["_ch"] = w, h, cw, ch
    return (w, h)


def _align_offset(mode, free):
    return {"start": 0.0, "center": free / 2.0, "end": free}.get(mode, free / 2.0)


def place(el, x, y, ctx, out, group=None):
    """x,y is the top-left of this element."""
    kind = el["kind"]
    if kind == "spacer":
        return
    if kind == "node":
        n = {"id": el["id"], "x": x + el["_w"] / 2.0, "y": y + el["_h"] / 2.0,
             "w": el["_w"], "h": el["_h"], "label": el.get("label", ""),
             "tone": el.get("tone", "src")}
        for k in ("sub", "mono", "shape"):
            if k in el:
                n[k] = el[k]
        if group:
            n["group"] = group
        out["nodes"].append(n)
        return

    if kind == "group":
        pad = float(el.get("pad", ctx["group_pad"]))
        out["groups"].append({
            "id": el["id"], "x": x, "y": y, "w": el["_w"], "h": el["_h"],
            "title": el.get("title", ""), "sub": el.get("sub", ""),
            "tone": el.get("tone", "src")})
        inner_x = x + pad
        inner_y = y + ctx["label_band"] + pad
        inner_w = el["_w"] - 2 * pad
        _lay_children(el, inner_x, inner_y, inner_w, el["_ch"],
                      el.get("dir", "col"), ctx, out, group=el["id"])
        return

    pad = float(el.get("pad", 0))
    _lay_children(el, x + pad, y + pad, el["_w"] - 2 * pad, el["_h"] - 2 * pad,
                  kind, ctx, out, group=group)


def _lay_children(el, x, y, avail_w, avail_h, direction, ctx, out, group):
    children = [c for c in el.get("children", [])]
    if not children:
        return
    gap = float(el.get("gap", ctx["gap"]))
    stretch = el.get("stretch", True)
    align = el.get("align", "center")

    if direction == "row":
        # distribute leftover horizontal space when the row is wider than needed
        used = sum(c["_w"] for c in children) + gap * (len(children) - 1)
        cx = x + _align_offset(el.get("justify", "center"), avail_w - used)
        for c in children:
            h = avail_h if (stretch and c["kind"] != "spacer") else c["_h"]
            if stretch and c["kind"] != "spacer":
                c["_h"] = h
            cy = y + _align_offset(align, avail_h - c["_h"])
            place(c, cx, cy, ctx, out, group)
            cx += c["_w"] + gap
    else:
        used = sum(c["_h"] for c in children) + gap * (len(children) - 1)
        cy = y + _align_offset(el.get("justify", "center"), avail_h - used)
        for c in children:
            if stretch and c["kind"] != "spacer":
                c["_w"] = avail_w
            cx = x + _align_offset(align, avail_w - c["_w"])
            place(c, cx, cy, ctx, out, group)
            cy += c["_h"] + gap


def compile(src):
    cv = src.get("canvas", {})
    ctx = {"gap": float(cv.get("gap", 16)),
           "group_pad": float(cv.get("group_pad", 12)),
           "label_band": float(cv.get("label_band", 32))}
    pad = float(cv.get("pad", 24))

    root = src["root"]
    cw, ch = measure(root, ctx)

    out = {"title": src.get("title", src.get("id", "figure")),
           "prompt": src.get("prompt", ""),
           "canvas": {"w": 0, "h": 0, "label_band": ctx["label_band"]},
           "palette": src["palette"], "groups": [], "nodes": [], "edges": []}

    W, H = cw + 2 * pad, ch + 2 * pad
    aspect = cv.get("aspect")
    if aspect:
        if W / H < aspect:
            W = H * aspect
        else:
            H = W / aspect
    ox = (W - cw) / 2.0
    oy = (H - ch) / 2.0
    place(root, ox, oy, ctx, out)

    out["canvas"]["w"] = round(W, 3)
    out["canvas"]["h"] = round(H, 3)
    if "tex_preamble" in src:
        out["tex_preamble"] = src["tex_preamble"]

    known = {g["id"] for g in out["groups"]} | {n["id"] for n in out["nodes"]}
    for e in src.get("edges", []):
        ed = {"id": e.get("id", "e%d" % (len(out["edges"]) + 1)),
              "from": e["from"], "to": e["to"], "kind": e.get("kind", "feed")}
        # A side hint pins the face; it must also pin the position along that
        # face or every edge into a wide element lands on its midpoint and the
        # whole bundle converges to a point. figspec supports {side, align:<id>}
        # for exactly this (C9/C11) — emit it rather than a bare t: 0.5.
        #
        # Which end aligns matters: for a drop from a narrow tier onto a wide
        # rail, the tier uses its own centre and the rail aligns to the tier.
        # So an end aligns to the other only when it is the larger one in the
        # free axis. An explicit *_t always wins.
        dims = {x["id"]: (x["w"], x["h"])
                for x in out["groups"] + out["nodes"]}
        for side_key, anchor_key, self_id, other_id in (
                ("from_side", "from_anchor", e["from"], e["to"]),
                ("to_side", "to_anchor", e["to"], e["from"])):
            if side_key not in e:
                continue
            t_key = side_key.replace("_side", "_t")
            if t_key in e:
                ed[anchor_key] = {"side": e[side_key], "t": e[t_key]}
                continue
            side = e[side_key]
            free = 0 if side in ("top", "bottom") else 1   # 0 = w, 1 = h
            a, b = dims.get(self_id), dims.get(other_id)
            if a and b and a[free] > b[free] * 1.15:
                ed[anchor_key] = {"side": side, "align": other_id}
            else:
                ed[anchor_key] = {"side": side, "t": 0.5}
        out["edges"].append(ed)
    out["_unknown_edge_ends"] = sorted(
        {x for e in out["edges"] for x in (e["from"], e["to"])} - known)
    return out
