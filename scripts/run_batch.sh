#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
BLENDER="${BLENDER_BIN:-/Applications/Blender.app/Contents/MacOS/Blender}"
PY="$ROOT/scripts/grotto_roblox_pipeline.py"
export GROTTO_PIPELINE_ROOT="$ROOT"

if [[ ! -x "$BLENDER" ]]; then
  echo "Set BLENDER_BIN to your Blender CLI (currently: $BLENDER)" >&2
  exit 1
fi

count=0
while IFS= read -r f; do
  [[ -n "$f" ]] || continue
  count=$((count + 1))
done < <(find "$ROOT/assets" -type f -iname '*.blend' | LC_ALL=C sort)

echo "Processing $count .blend files"
while IFS= read -r f; do
  [[ -n "$f" ]] || continue
  echo "===== $f"
  "$BLENDER" -b "$f" --python "$PY" -- --process-open-file || {
    echo "FAILED: $f" >&2
  }
done < <(find "$ROOT/assets" -type f -iname '*.blend' | LC_ALL=C sort)
echo "Done. FBX outputs under exports/roblox_fbx_<date>/; manifests under exports/manifests/"
