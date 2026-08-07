"""Loader and invariant validator for the figure spec.

Interface contract:
    load(path)      -> dict          (raw spec, no mutation)
    validate(spec)  -> list[str]     (empty list == all invariants hold)
    node_rect(n)    -> (x0,y0,x1,y1) in source coords (y-down)
    group_rect(g)   -> (x0,y0,x1,y1)
    anchor_point(rect, anchor) -> (x,y)
    border_point(rect, toward)  -> (x,y)   centre-to-centre clip
"""
import json

SIDES = {"top", "right", "bottom", "left"}
KINDS = {"feed", "fallback", "escalate", "store"}
SHAPES = {"box", "store"}


def load(path):
    with open(path, encoding="utf-8") as fh:
        return json.load(fh)


def node_rect(n):
    return (n["x"] - n["w"] / 2.0, n["y"] - n["h"] / 2.0,
            n["x"] + n["w"] / 2.0, n["y"] + n["h"] / 2.0)


def group_rect(g):
    return (g["x"], g["y"], g["x"] + g["w"], g["y"] + g["h"])


def _overlap(a, b):
    return a[0] < b[2] and b[0] < a[2] and a[1] < b[3] and b[1] < a[3]


def _inside(inner, outer):
    return (inner[0] >= outer[0] and inner[1] >= outer[1]
            and inner[2] <= outer[2] and inner[3] <= outer[3])


def anchor_point(rect, anchor, res=None):
    """Anchor is {side,t} or {side,align:<id>}.

    align pins the free coordinate to the centre of the referenced object, so a
    perpendicular edge stays exactly perpendicular when either end is moved.
    """
    x0, y0, x1, y1 = rect
    side = anchor["side"]
    if "align" in anchor:
        ar = res[anchor["align"]][2]
        acx, acy = (ar[0] + ar[2]) / 2.0, (ar[1] + ar[3]) / 2.0
        if side in ("top", "bottom"):
            return (acx, y0 if side == "top" else y1)
        return (x0 if side == "left" else x1, acy)
    t = float(anchor["t"])
    if side == "top":
        return (x0 + t * (x1 - x0), y0)
    if side == "bottom":
        return (x0 + t * (x1 - x0), y1)
    if side == "left":
        return (x0, y0 + t * (y1 - y0))
    return (x1, y0 + t * (y1 - y0))          # right


def border_point(rect, toward):
    """Point where the segment centre->toward leaves rect."""
    x0, y0, x1, y1 = rect
    cx, cy = (x0 + x1) / 2.0, (y0 + y1) / 2.0
    dx, dy = toward[0] - cx, toward[1] - cy
    if dx == 0 and dy == 0:
        return (cx, cy)
    hw, hh = (x1 - x0) / 2.0, (y1 - y0) / 2.0
    sx = hw / abs(dx) if dx else float("inf")
    sy = hh / abs(dy) if dy else float("inf")
    s = min(sx, sy)
    return (cx + dx * s, cy + dy * s)


def resolve(spec):
    """id -> ('node'|'group', obj, rect)"""
    out = {}
    for g in spec["groups"]:
        out[g["id"]] = ("group", g, group_rect(g))
    for n in spec["nodes"]:
        out[n["id"]] = ("node", n, node_rect(n))
    return out


def validate(spec):
    errs = []
    canvas = spec["canvas"]
    band = canvas["label_band"]
    pal = spec["palette"]

    # C1 unique ids
    seen = {}
    for kindname, items in (("group", spec["groups"]), ("node", spec["nodes"])):
        for it in items:
            if it["id"] in seen:
                errs.append("C1 duplicate id %r (%s and %s)"
                            % (it["id"], seen[it["id"]], kindname))
            seen[it["id"]] = kindname

    gids = {g["id"] for g in spec["groups"]}
    gmap = {g["id"]: g for g in spec["groups"]}
    ids = set(seen)

    # C2 edge endpoints resolve
    for e in spec["edges"]:
        for side in ("from", "to"):
            if e[side] not in ids:
                errs.append("C2 edge %s: %s=%r does not resolve" % (e["id"], side, e[side]))
        if e["kind"] not in KINDS:
            errs.append("C2 edge %s: unknown kind %r" % (e["id"], e["kind"]))

    for n in spec["nodes"]:
        nr = node_rect(n)
        # C3 group resolves
        if "group" in n and n["group"] not in gids:
            errs.append("C3 node %s: group %r does not resolve" % (n["id"], n["group"]))
            continue
        if "group" in n:
            g = gmap[n["group"]]
            gr = group_rect(g)
            # C4 containment
            if not _inside(nr, gr):
                errs.append("C4 node %s not inside group %s" % (n["id"], g["id"]))
            # C5 below label band
            if nr[1] < g["y"] + band:
                errs.append("C5 node %s intrudes into label band of %s (top %.1f < %.1f)"
                            % (n["id"], g["id"], nr[1], g["y"] + band))
        else:
            # C7 ungrouped node must not overlap any group rect
            for g in spec["groups"]:
                if _overlap(nr, group_rect(g)):
                    errs.append("C7 ungrouped node %s overlaps group %s" % (n["id"], g["id"]))
        # C8 canvas
        if nr[0] < 0 or nr[1] < 0 or nr[2] > canvas["w"] or nr[3] > canvas["h"]:
            errs.append("C8 node %s outside canvas: %s" % (n["id"], nr))
        # C10 tone
        if n["tone"] not in pal:
            errs.append("C10 node %s: tone %r not in palette" % (n["id"], n["tone"]))
        if n.get("shape", "box") not in SHAPES:
            errs.append("C10 node %s: unknown shape %r" % (n["id"], n["shape"]))

    for g in spec["groups"]:
        gr = group_rect(g)
        if gr[0] < 0 or gr[1] < 0 or gr[2] > canvas["w"] or gr[3] > canvas["h"]:
            errs.append("C8 group %s outside canvas: %s" % (g["id"], gr))
        if g["tone"] not in pal:
            errs.append("C10 group %s: tone %r not in palette" % (g["id"], g["tone"]))

    # C6 pairwise node overlap
    ns = spec["nodes"]
    for i in range(len(ns)):
        for j in range(i + 1, len(ns)):
            if _overlap(node_rect(ns[i]), node_rect(ns[j])):
                errs.append("C6 nodes %s and %s overlap" % (ns[i]["id"], ns[j]["id"]))

    # C9 anchors
    for e in spec["edges"]:
        for key in ("from_anchor", "to_anchor"):
            a = e.get(key)
            if a is None:
                continue
            if a.get("side") not in SIDES:
                errs.append("C9 edge %s: %s side %r invalid" % (e["id"], key, a.get("side")))
            if "align" in a and "t" in a:
                errs.append("C9 edge %s: %s has both align and t" % (e["id"], key))
            if "align" in a:
                if a["align"] not in ids:
                    errs.append("C11 edge %s: %s align=%r does not resolve"
                                % (e["id"], key, a["align"]))
                    continue
                endpoint = e["from"] if key == "from_anchor" else e["to"]
                if endpoint not in ids:
                    continue          # C2 already reported the unresolved endpoint
                res = resolve(spec)
                rect = res[endpoint][2]
                px, py = anchor_point(rect, a, res)
                if a["side"] in ("top", "bottom"):
                    lo, hi = rect[0], rect[2]
                    v = px
                else:
                    lo, hi = rect[1], rect[3]
                    v = py
                if not (lo - 1e-9 <= v <= hi + 1e-9):
                    errs.append("C11 edge %s: %s align point %.2f off side %s [%.1f,%.1f]"
                                % (e["id"], key, v, a["side"], lo, hi))
            else:
                t = a.get("t")
                if not isinstance(t, (int, float)) or not (0.0 <= t <= 1.0):
                    errs.append("C9 edge %s: %s t=%r out of range" % (e["id"], key, t))

    return errs


def edge_points(spec, e, res=None):
    """Resolved (start, end) in source coords, honouring anchors."""
    res = res or resolve(spec)
    ra = res[e["from"]][2]
    rb = res[e["to"]][2]
    ca = ((ra[0] + ra[2]) / 2.0, (ra[1] + ra[3]) / 2.0)
    cb = ((rb[0] + rb[2]) / 2.0, (rb[1] + rb[3]) / 2.0)
    p = anchor_point(ra, e["from_anchor"], res) if "from_anchor" in e else border_point(ra, cb)
    q = anchor_point(rb, e["to_anchor"], res) if "to_anchor" in e else border_point(rb, ca)
    return p, q
