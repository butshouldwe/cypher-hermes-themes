#!/usr/bin/env bash
# Install the Cypher Hermes dashboard themes.
set -euo pipefail
DEST="${HERMES_HOME:-$HOME/.hermes}/dashboard-themes"
mkdir -p "$DEST"
cp "$(dirname "$0")"/*.yaml "$DEST/"
echo "Installed $(ls "$(dirname "$0")"/*.yaml | wc -l | tr -d ' ') themes → $DEST"
echo "Reload the dashboard and pick a 'Cypher · …' theme."
