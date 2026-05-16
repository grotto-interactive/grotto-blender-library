# grotto_canoe — Roblox Spec

**Category:** Water vehicle (rowboat reference — smooth oblong plan)  
**Scale:** 1 unit = 1 stud — ~8.0 L × 2.24 W, sit-in depth ~0.5  
**Triangles:** ~760 (3 mesh parts)  
**Export:** `exports/roblox_fbx_2026-05-16/grotto_canoe_LOD0_roblox.fbx`

## Reference

Top-down silhouette: **pointed bow**, **rounded stern**, **widest amidships**, smooth curved port/starboard (no diamond corners). Subtle S-curve sheer.

## Parts & Colors

| Object | Role | Hex |
|--------|------|-----|
| canoe_Hull | Sit-in hull | #8E6838 |
| canoe_Seat | Mid thwart | #6B4E32 |
| canoe_Paddle | Oar prop | #8E6838 |

## Markers

| Empty | Use |
|--------|-----|
| `Seat_Rower` | VehicleSeat placement |
| `Ref_Bow` | Forward = **-X** |

## Studio

- VehicleSeat at `Seat_Rower`, weld hull/seat, tune `MaxSpeed` / `TurnSpeed` for rowing.

## Build

`Blender -b --python scripts/build_grotto_canoe.py`
