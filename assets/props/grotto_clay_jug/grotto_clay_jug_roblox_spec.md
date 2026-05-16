# grotto_clay_jug — Roblox Spec

**Category:** Tavern / kitchen prop (opaque ceramic pitcher)  
**Style contrast:** Opaque clay + side handle vs glass bottles  
**Scale:** ~0.44 m tall; pivot at base center  
**Triangles:** ~696 manifest (2 parts — under standard prop ≤800)  
**Export:** `exports/roblox_fbx_2026-05-16/grotto_clay_jug_LOD0_roblox.fbx`

## Parts & Colors

| Object | Role | Hex |
|--------|------|-----|
| jug_Body | Pitcher body + neck + lip | #A6896A |
| jug_Handle | Side strap handle | #7A6348 |

## Studio

- Shelf, kitchen, well, or loot. Fully opaque — no transparency.
- `CanCollide = true` with simple box/hull if placed.

## Build

`Blender -b --python scripts/build_grotto_clay_jug.py`
