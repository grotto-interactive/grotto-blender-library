# grotto_nautilus_shell — Roblox Spec

**Category:** Underwater environment scatter (planispiral nautilus)  
**Style contrast:** Flat golden spiral vs tall `grotto_conch_shell` / narrow `grotto_auger_shell`  
**Scale:** ~0.18 m wide; pivot at lowest point  
**Triangles:** ~668 (1 part — under standard prop ≤800)  
**Export:** `exports/roblox_fbx_2026-05-16/grotto_nautilus_shell_LOD0_roblox.fbx`

## Parts & Colors

| Object | Role | Hex |
|--------|------|-----|
| nautilus_Shell | Unified planispiral coil + umbilicus | #EDE4D0 |

## Studio

- Rest on seafloor; random Y rotation for scatter.
- Slightly pearlescent — lower roughness than matte conch/scallop.
- `CanCollide = false` recommended.

## Build

`Blender -b --python scripts/build_grotto_nautilus_shell.py`
