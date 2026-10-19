#!/usr/bin/env bash
# All site checks, one line each: PASS / FAIL / KNOWN / NOT RUN.
# Exit 0 only if nothing FAILed. NOT RUN is not a pass: report it as unverified.
#   tools/site-check.sh
set -u
cd "$(dirname "$0")/.." || exit 1
log=$(mktemp); fails=0

say() { printf '%-8s %s\n' "$1" "$2"; }
run() {  # run NAME cmd...
  local name=$1; shift
  if "$@" >"$log" 2>&1; then say PASS "$name"; else say FAIL "$name"; sed 's/^/         /' "$log" | tail -8; fails=$((fails+1)); fi
}

run "C1 check-home.py (design, head, markers, links, size)" python3 check-home.py
run "C2 deploy guard from pages.yml" python3 tools/ci-guard.py

if [ "$(git rev-parse --is-shallow-repository)" = true ]; then
  say "NOT RUN" "C3 sitemap — shallow clone; dates would be wrong (git fetch --unshallow first)"
else
  run "C3 sitemap matches git" python3 gen-sitemap.py --check
fi

# C4: drift on rows listed in KNOWN_DRIFT is reported as KNOWN (docs/maintenance/KNOWN-ISSUES.md KI-1).
# Any other disagreeing row is a FAIL. Remove a name here only when the owner has resolved it.
KNOWN_DRIFT="killing1889"
if python3 gen-residual-bars.py --check >"$log" 2>&1; then
  say PASS "C4 residual bars match report.ink.json"
else
  rows=$(awk '/disagree with report.ink.json/{f=1;next} f&&NF{print $1}' "$log" | sort | tr '\n' ' ')
  want=$(echo "$KNOWN_DRIFT" | tr ' ' '\n' | sort | tr '\n' ' ')
  if [ -n "$rows" ] && [ "$rows" = "$want" ]; then
    say KNOWN "C4 residual bars — only known drift: ${rows}(KI-1)"
  else
    say FAIL "C4 residual bars disagree: ${rows:-see output}"; sed 's/^/         /' "$log" | tail -8; fails=$((fails+1))
  fi
fi

python3 tools/render.py >"$log" 2>&1; rc=$?
case $rc in
  0) say PASS "C5 render 1280/375 px, no overflow"; sed 's/^/         /' "$log";;
  2) say "NOT RUN" "C5 render — $(tail -1 "$log")";;
  *) say FAIL "C5 render"; sed 's/^/         /' "$log"; fails=$((fails+1));;
esac

say "NOT RUN" "gen-doc-downloads.py — must not run (KI-2)"
rm -f "$log"
echo "failures: $fails"
exit $(( fails > 0 ))
