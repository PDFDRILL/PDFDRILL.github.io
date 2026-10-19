#!/usr/bin/env python3
"""Run the deploy guard from .github/workflows/pages.yml locally, exactly as CI runs it.

The guard is not copied: it is extracted from the workflow at run time (the
`python3 - <<'GUARD' ... GUARD` heredoc of the step "Refuse to publish an
artefact nobody chose"), so a local PASS means the same code passed that CI
will run. Exit code is the guard's.

    python3 tools/ci-guard.py
"""
import os, re, subprocess, sys, tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
wf = open(os.path.join(ROOT, ".github", "workflows", "pages.yml"), encoding="utf-8").read()
m = re.search(r"python3 - <<'GUARD'\n(.*?)\n[ \t]*GUARD\n", wf, re.S)
if not m:
    sys.exit("ci-guard: no GUARD heredoc found in pages.yml — the workflow changed shape; ask the owner")
lines = m.group(1).split("\n")
indent = min(len(l) - len(l.lstrip()) for l in lines if l.strip())
code = "\n".join(l[indent:] for l in lines)
with tempfile.NamedTemporaryFile("w", suffix=".py", delete=False) as f:
    f.write(code)
try:
    sys.exit(subprocess.run([sys.executable, f.name], cwd=ROOT).returncode)
finally:
    os.unlink(f.name)
