#!/usr/bin/env bash
set -euo pipefail

# Run validation checks on all Eris cookbooks and manifests.
#
# Usage:
#   scripts/test-cookbooks.sh

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"

echo "=== Eris Cookbook Tests ==="
echo ""

echo "Running check.py ..."
python3 "$SCRIPT_DIR/check.py"

echo ""
echo "All tests passed."
