#!/usr/bin/env bash
# Sync lyrics-db across skills.
# Source of truth: mayday-mood/references/lyrics-db/
# Targets: ashin-lyrics, chat-ashin, mayday-quotes
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
SRC="$ROOT/mayday-mood/references/lyrics-db"
TARGETS=(
  "$ROOT/ashin-lyrics/references/lyrics-db"
  "$ROOT/chat-ashin/references/lyrics-db"
  "$ROOT/mayday-quotes/references/lyrics-db"
  "$ROOT/mayday-trivia/references/lyrics-db"
)

if [[ ! -d "$SRC" ]]; then
  echo "Source not found: $SRC" >&2
  exit 1
fi

for dst in "${TARGETS[@]}"; do
  mkdir -p "$dst"
  # rsync mirrors src to dst, removes stale files
  rsync -a --delete "$SRC/" "$dst/"
  echo "synced -> $dst"
done
