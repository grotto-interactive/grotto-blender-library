# grotto_pirate_water_bottle — Roblox Spec

**Category:** Hand-held prop (pirate canteen / water flask)  
**Scale:** 1 Blender unit = 1 meter (~0.32 m tall)  
**Triangles:** ~604 manifest (4 mesh parts — under standard prop ≤800 cap)  
**Scale:** ~1.06 m tall (~3.8 studs); pivot at base center (Z=0)  
**Export:** `exports/roblox_fbx_2026-05-16/grotto_pirate_water_bottle_LOD0_roblox.fbx` (re-validated 2026-05-16)  
**Pivot:** `GROTTO_grotto_pirate_water_bottle` at base center

## Parts & Colors

| Object | Role | Hex |
|--------|------|-----|
| bottle_Glass | Unified bottle body + neck (smooth) | #4A6B52 |
| bottle_Cork | Cork stopper | #7A5A38 |
| bottle_BrassBand | Neck ferrule | #A88420 |
| bottle_RopeWrap | Neck rope | #8B7348 |

## Studio

- Hand tool / inventory icon scale; attach to hand or hip socket.
- Glass: `CanCollide = false`, slight transparency.
- Cork, rope, brass: `CanCollide = true` optional.
