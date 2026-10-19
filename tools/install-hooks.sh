#!/usr/bin/env bash
# Install the pre-commit gate into this clone (once per clone; git does not copy hooks).
#   tools/install-hooks.sh
set -eu
cd "$(git rev-parse --show-toplevel)"
install -m 0755 tools/pre-commit .git/hooks/pre-commit
cmp -s tools/pre-commit .git/hooks/pre-commit && echo "pre-commit installed: .git/hooks/pre-commit"
