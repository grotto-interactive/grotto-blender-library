# grotto_conch_shell — Roblox Spec

**Category:** Underwater environment scatter (spiral seashell)  
**Scale:** ~0.18 m wide; pivot at lowest point (seafloor rest)  
**Triangles:** ~628 (2 parts — under standard prop ≤800)  
**Export:** `exports/roblox_fbx_2026-05-16/grotto_conch_shell_LOD0_roblox.fbx`

## Parts & Colors

| Object | Role | Hex |
|--------|------|-----|
| conch_Shell | Unified spiral (wide mouth → pointed tip) | #E8D8B8 |
| conch_Lip | Inner aperture edge | #E8B8A0 |

## Studio

- Scatter on sand near reef, clams, kelp.
- `CanCollide = false` optional for small scatter.
- Rest orientation: lies on side, opening tilted up.

## Build

`Blender -b --python scripts/build_grotto_conch_shell.py`
