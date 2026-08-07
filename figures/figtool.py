#!/usr/bin/env python3
"""figtool - edit and build structural figure specs.

    figtool.py show     <spec>                     tree view
    figtool.py prompt   <spec> [--set TEXT|--file F]  read/write the prompt
    figtool.py validate <spec>                     compile + check invariants
    figtool.py build    <spec> [--outdir DIR]      -> .flat.json, .mp, .html
    figtool.py add      <spec> --parent ID --id ID --label TEXT
                               [--tone T] [--mono] [--sub TEXT] [--after ID]
    figtool.py addgroup <spec> --parent ID --id ID --title TEXT
                               [--sub TEXT] [--tone T] [--dir row|col]
    figtool.py rm       <spec> --id ID             element + edges touching it
    figtool.py set      <spec> --id ID [--label|--title|--sub|--tone|--w|--h V]
    figtool.py edge     <spec> --from ID --to ID [--kind K]
                               [--from-side S] [--to-side S] [--id E]
    figtool.py rmedge   <spec> --id E

Every mutating command re-compiles and re-validates before writing; if the
edit would break an invariant the file is left untouched and the errors are
printed. Coordinates are never authored - they are derived by layout.py.
"""
import argparse
import json
import os
import signal
import sys

import figspec
import layout

KINDS = ("feed", "fallback", "escalate", "store")


def load(path):
    with open(path, encoding="utf-8") as fh:
        return json.load(fh)


def save(path, src):
    with open(path, "w", encoding="utf-8") as fh:
        json.dump(src, fh, indent=2, ensure_ascii=False)
        fh.write("\n")


def strip_private(el):
    if isinstance(el, dict):
        for k in [k for k in el if k.startswith("_")]:
            del el[k]
        for c in el.get("children", []):
            strip_private(c)


def walk(el, parent=None):
    yield el, parent
    for c in el.get("children", []):
        yield from walk(c, el)


def find(src, eid):
    for el, parent in walk(src["root"]):
        if el.get("id") == eid:
            return el, parent
    return None, None


def check(src):
    """Compile and validate a candidate spec; return list of errors."""
    trial = json.loads(json.dumps(src))
    try:
        flat = layout.compile(trial)
    except Exception as exc:                       # noqa: BLE001
        return ["compile failed: %s: %s" % (type(exc).__name__, exc)]
    errs = figspec.validate(flat)
    if flat["_unknown_edge_ends"]:
        errs.append("edge endpoints not present in the figure: %s"
                    % ", ".join(flat["_unknown_edge_ends"]))
    return errs


def commit(path, src):
    errs = check(src)
    if errs:
        print("REJECTED - the edit would break the figure:", file=sys.stderr)
        for e in errs:
            print("  " + e, file=sys.stderr)
        return 1
    strip_private(src["root"])
    save(path, src)
    print("ok")
    return 0


# ---------------------------------------------------------------- commands --
def cmd_show(a):
    src = load(a.spec)
    print("%s  [%s]" % (src.get("title", "?"), src.get("id", "?")))
    ids = []

    def rec(el, depth):
        k = el["kind"]
        if k == "node":
            lbl = el.get("label", "")
            extra = " +sub" if "sub" in el else ""
            print("%s- node   %-12s %r%s" % ("  " * depth, el.get("id", ""), lbl, extra))
            ids.append(el.get("id"))
        elif k == "group":
            print("%s- group  %-12s %r  dir=%s"
                  % ("  " * depth, el.get("id", ""), el.get("title", ""),
                     el.get("dir", "col")))
            ids.append(el.get("id"))
        elif k == "spacer":
            print("%s- spacer" % ("  " * depth))
        else:
            print("%s- %-6s %s" % ("  " * depth, k, "gap=%s" % el.get("gap", "")))
        for c in el.get("children", []):
            rec(c, depth + 1)

    rec(src["root"], 1)
    print("\nedges:")
    for e in src.get("edges", []):
        print("  %-5s %-12s -> %-12s %s"
              % (e.get("id", ""), e["from"], e["to"], e.get("kind", "feed")))
    flat = layout.compile(json.loads(json.dumps(src)))
    print("\ncanvas %sx%s   %d groups, %d nodes"
          % (flat["canvas"]["w"], flat["canvas"]["h"],
             len(flat["groups"]), len(flat["nodes"])))
    return 0


def cmd_prompt(a):
    src = load(a.spec)
    if a.set is None and a.file is None:
        print(src.get("prompt", ""))
        return 0
    src["prompt"] = open(a.file, encoding="utf-8").read() if a.file else a.set
    return commit(a.spec, src)


def cmd_validate(a):
    errs = check(load(a.spec))
    for e in errs:
        print(" ", e)
    print("VALID" if not errs else "INVALID (%d)" % len(errs))
    return 1 if errs else 0


def cmd_build(a):
    import emit_html
    import emit_mp
    src = load(a.spec)
    errs = check(src)
    if errs:
        for e in errs:
            print(" ", e, file=sys.stderr)
        return 1
    flat = layout.compile(src)
    stem = os.path.join(a.outdir, src["id"])
    os.makedirs(a.outdir, exist_ok=True)
    pub = {k: v for k, v in flat.items() if not k.startswith("_")}
    with open(stem + ".flat.json", "w", encoding="utf-8") as fh:
        json.dump(pub, fh, indent=1)
    flat["_outputformat"] = "eps"
    with open(stem + ".mp", "w", encoding="utf-8") as fh:
        fh.write(emit_mp.emit(flat))
    js = None
    if a.inline:
        js = open("node_modules/cytoscape/dist/cytoscape.min.js",
                  encoding="utf-8").read()
    v = json.load(open("node_modules/cytoscape/package.json"))["version"]
    with open(stem + ".html", "w", encoding="utf-8") as fh:
        fh.write(emit_html.emit(flat, js=js, cdn_version=v))
    print("built %s.{flat.json,mp,html}" % stem)
    return 0


def cmd_add(a):
    src = load(a.spec)
    if find(src, a.id)[0]:
        print("id %r already exists" % a.id, file=sys.stderr)
        return 1
    parent, _ = find(src, a.parent)
    if parent is None:
        print("parent %r not found" % a.parent, file=sys.stderr)
        return 1
    el = {"kind": "node", "id": a.id, "label": a.label,
          "tone": a.tone or parent.get("tone", "src")}
    if a.mono:
        el["mono"] = True
    if a.sub:
        el["sub"] = a.sub
    kids = parent.setdefault("children", [])
    idx = len(kids)
    if a.after:
        for i, c in enumerate(kids):
            if c.get("id") == a.after:
                idx = i + 1
    kids.insert(idx, el)
    return commit(a.spec, src)


def cmd_addgroup(a):
    src = load(a.spec)
    if find(src, a.id)[0]:
        print("id %r already exists" % a.id, file=sys.stderr)
        return 1
    parent, _ = find(src, a.parent)
    if parent is None:
        print("parent %r not found" % a.parent, file=sys.stderr)
        return 1
    parent.setdefault("children", []).append(
        {"kind": "group", "id": a.id, "title": a.title, "sub": a.sub or "",
         "tone": a.tone or "src", "dir": a.dir, "children": []})
    return commit(a.spec, src)


def cmd_rm(a):
    src = load(a.spec)
    el, parent = find(src, a.id)
    if el is None:
        print("id %r not found" % a.id, file=sys.stderr)
        return 1
    if parent is None:
        print("cannot remove the root", file=sys.stderr)
        return 1
    gone = {e.get("id") for e, _ in walk(el)}
    parent["children"].remove(el)
    src["edges"] = [e for e in src.get("edges", [])
                    if e["from"] not in gone and e["to"] not in gone]
    return commit(a.spec, src)


def cmd_set(a):
    src = load(a.spec)
    el, _ = find(src, a.id)
    if el is None:
        print("id %r not found" % a.id, file=sys.stderr)
        return 1
    for key in ("label", "title", "sub", "tone"):
        v = getattr(a, key)
        if v is not None:
            el[key] = v
    for key in ("w", "h"):
        v = getattr(a, key)
        if v is not None:
            el[key] = float(v)
    return commit(a.spec, src)


def cmd_edge(a):
    src = load(a.spec)
    edges = src.setdefault("edges", [])
    eid = a.id or "e%d" % (len(edges) + 1)
    if any(e.get("id") == eid for e in edges):
        print("edge id %r already exists" % eid, file=sys.stderr)
        return 1
    e = {"id": eid, "from": getattr(a, "from"), "to": a.to, "kind": a.kind}
    if a.from_side:
        e["from_side"] = a.from_side
    if a.to_side:
        e["to_side"] = a.to_side
    edges.append(e)
    return commit(a.spec, src)


def cmd_rmedge(a):
    src = load(a.spec)
    before = len(src.get("edges", []))
    src["edges"] = [e for e in src.get("edges", []) if e.get("id") != a.id]
    if len(src["edges"]) == before:
        print("edge %r not found" % a.id, file=sys.stderr)
        return 1
    return commit(a.spec, src)


def main():
    p = argparse.ArgumentParser(prog="figtool", description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="cmd", required=True)

    def spec_arg(sp):
        sp.add_argument("spec")
        return sp

    spec_arg(sub.add_parser("show")).set_defaults(fn=cmd_show)
    spec_arg(sub.add_parser("validate")).set_defaults(fn=cmd_validate)

    sp = spec_arg(sub.add_parser("prompt"))
    sp.add_argument("--set")
    sp.add_argument("--file")
    sp.set_defaults(fn=cmd_prompt)

    sp = spec_arg(sub.add_parser("build"))
    sp.add_argument("--outdir", default="build")
    sp.add_argument("--inline", action="store_true")
    sp.set_defaults(fn=cmd_build)

    sp = spec_arg(sub.add_parser("add"))
    sp.add_argument("--parent", required=True)
    sp.add_argument("--id", required=True)
    sp.add_argument("--label", required=True)
    sp.add_argument("--tone")
    sp.add_argument("--sub")
    sp.add_argument("--after")
    sp.add_argument("--mono", action="store_true")
    sp.set_defaults(fn=cmd_add)

    sp = spec_arg(sub.add_parser("addgroup"))
    sp.add_argument("--parent", required=True)
    sp.add_argument("--id", required=True)
    sp.add_argument("--title", required=True)
    sp.add_argument("--sub")
    sp.add_argument("--tone")
    sp.add_argument("--dir", default="col", choices=("row", "col"))
    sp.set_defaults(fn=cmd_addgroup)

    sp = spec_arg(sub.add_parser("rm"))
    sp.add_argument("--id", required=True)
    sp.set_defaults(fn=cmd_rm)

    sp = spec_arg(sub.add_parser("set"))
    sp.add_argument("--id", required=True)
    for k in ("label", "title", "sub", "tone", "w", "h"):
        sp.add_argument("--" + k)
    sp.set_defaults(fn=cmd_set)

    sp = spec_arg(sub.add_parser("edge"))
    sp.add_argument("--from", required=True, dest="from")
    sp.add_argument("--to", required=True)
    sp.add_argument("--kind", default="feed", choices=KINDS)
    sp.add_argument("--from-side", dest="from_side",
                    choices=("top", "right", "bottom", "left"))
    sp.add_argument("--to-side", dest="to_side",
                    choices=("top", "right", "bottom", "left"))
    sp.add_argument("--id")
    sp.set_defaults(fn=cmd_edge)

    sp = spec_arg(sub.add_parser("rmedge"))
    sp.add_argument("--id", required=True)
    sp.set_defaults(fn=cmd_rmedge)

    a = p.parse_args()
    return a.fn(a)


if __name__ == "__main__":
    # a CLI must survive being piped into head/less
    try:
        signal.signal(signal.SIGPIPE, signal.SIG_DFL)
    except (AttributeError, ValueError):
        pass
    sys.exit(main())
