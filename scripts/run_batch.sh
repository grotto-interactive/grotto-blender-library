#!/usr/bin/env bash
# Batch all assets/**/*.blend through grotto_roblox_pipeline.py
# - Stops entire run if the same .blend crashes twice in a row (attempt 1 + retry).
# - Logs each failed asset path (with exit code / reason) to exports/batch_failures_<stamp>.log
# - Non-crash Blender failures are logged; processing continues with remaining assets.

set -uo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
BLENDER="${BLENDER_BIN:-/Applications/Blender.app/Contents/MacOS/Blender}"
PY="$ROOT/scripts/grotto_roblox_pipeline.py"
export GROTTO_PIPELINE_ROOT="$ROOT"

STAMP="$(date +%Y%m%d_%H%M%S)"
FAIL_LOG="$ROOT/exports/batch_failures_${STAMP}.log"
RUN_LOG="$ROOT/exports/batch_run_${STAMP}.log"

if [[ ! -x "$BLENDER" ]]; then
  echo "Set BLENDER_BIN to your Blender CLI (currently: $BLENDER)" >&2
  exit 1
fi

is_crash() {
  local ec=$1
  case "$ec" in
    139) return 0 ;;  # 128 + SIGSEGV(11)
    134) return 0 ;;  # 128 + SIGABRT(6)
    136) return 0 ;;
    143) return 0 ;;
    11) return 0 ;;   # raw SIGSEGV on some setups
    10) return 0 ;;   # SIGBUS
  esac
  return 1
}

BLENDS=()
while IFS= read -r f; do
  [[ -n "$f" ]] && BLENDS+=("$f")
done < <(find "$ROOT/assets" -type f -iname '*.blend' | LC_ALL=C sort)

total="${#BLENDS[@]}"
ok=0
fail_noncrash=0
aborted_early=0
processed=0

echo "Processing $total .blend files — failures -> $FAIL_LOG"
echo "Full log -> $RUN_LOG"
echo "batch_start $(date -u +%Y-%m-%dT%H:%M:%SZ) total=$total" >>"$RUN_LOG"

for f in "${BLENDS[@]}"; do
  [[ -n "$f" ]] || continue
  rel="${f#$ROOT/}"
  processed=$((processed + 1))
  echo "===== ($processed/$total) $rel" | tee -a "$RUN_LOG"
  asset_failed=0

  for attempt in 1 2; do
    "$BLENDER" -b "$f" --python "$PY" -- --process-open-file >>"$RUN_LOG" 2>&1
    ec=$?

    if [[ $ec -eq 0 ]]; then
      ok=$((ok + 1))
      asset_failed=0
      break
    fi

    if is_crash "$ec"; then
      printf '%s\tcrash\texit=%d\tattempt=%d\n' "$f" "$ec" "$attempt" >>"$FAIL_LOG"
      if [[ "$attempt" -eq 2 ]]; then
        echo "ABORT: repeated Blender crash on same asset: $f (exit $ec)" | tee -a "$RUN_LOG" "$FAIL_LOG"
        aborted_early=1
        break 2
      fi
      echo "Retrying after crash (attempt $attempt): $rel" | tee -a "$RUN_LOG"
      continue
    fi

    printf '%s\terror\texit=%d\tattempt=%d\n' "$f" "$ec" "$attempt" >>"$FAIL_LOG"
    fail_noncrash=$((fail_noncrash + 1))
    asset_failed=1
    break
  done
done

echo "" | tee -a "$RUN_LOG"
echo "batch_end $(date -u +%Y-%m-%dT%H:%M:%SZ)" | tee -a "$RUN_LOG"
echo "total_blend_files=$total processed_stopped_at=$processed ok=$ok fail_noncrash=$fail_noncrash aborted_early=$aborted_early" | tee -a "$RUN_LOG"
echo "Done. FBX under exports/roblox_fbx_<date>/; manifests under exports/manifests/"
echo "Failure log: $FAIL_LOG"

exit 0
