# grotto_scallop_shell — Roblox Spec

**Category:** Underwater environment scatter (fan / scallop shell)  
**Style contrast:** Flat ribbed fan vs spiral `grotto_conch_shell`  
**Scale:** ~0.25 m wide; lies flat; pivot at lowest point  
**Triangles:** ~468 (1 part — under standard prop ≤800)  
**Export:** `exports/roblox_fbx_2026-05-16/grotto_scallop_shell_LOD0_roblox.fbx`

## Parts & Colors

| Object | Role | Hex |
|--------|------|-----|
| scallop_Shell | Solid ribbed fan cup (one mesh) | #E6D4B0 |

## Studio

- Lay flat on seafloor; rotate randomly on Y for scatter variety.
- `CanCollide = false` recommended.

## Build

`Blender -b --python scripts/build_grotto_scallop_shell.py`
