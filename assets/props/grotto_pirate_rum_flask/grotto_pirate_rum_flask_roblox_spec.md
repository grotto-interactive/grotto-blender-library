# grotto_pirate_rum_flask — Roblox Spec

**Category:** Hand-held / tavern prop (squat rum bottle)  
**Style contrast:** Short wide belly + wax seal vs tall green `grotto_pirate_water_bottle` canteen  
**Scale:** 1 Blender unit = 1 meter (~0.75 m tall)  
**Triangles:** ~712 manifest (3 mesh parts — under standard prop ≤800 cap)  
**Pivot:** `GROTTO_grotto_pirate_rum_flask` at base center (Z=0)  
**Export:** `exports/roblox_fbx_2026-05-16/grotto_pirate_rum_flask_LOD0_roblox.fbx` (re-exported 2026-05-16)

## Parts & Colors

| Object | Role | Hex |
|--------|------|-----|
| rum_Glass | Body + neck (lathe) | #4A3020 |
| rum_Cork | Dome stopper | #6B4E30 |
| rum_WaxSeal | Neck wax ring | #8B1E18 |

## Studio

- Tavern shelf, bar, loot pile, or hand prop (heavier read than water canteen).
- Glass: slight transparency; `CanCollide = false` optional.
- Cork + wax: solid tints; simple box collision if placed.

## Build

Regenerate mesh: `Blender -b --python scripts/build_grotto_pirate_rum_flask.py`  
Export: open blend → `scripts/grotto_roblox_pipeline.py -- --process-open-file`
