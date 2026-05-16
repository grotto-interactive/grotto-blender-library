# grotto_message_in_bottle — Roblox Spec

**Category:** Quest / decor prop (castaway message, open neck)  
**Scale:** ~0.44 m tall; pivot at base center  
**Triangles:** ~428 (2 parts — under standard prop ≤800)  
**Export:** `exports/roblox_fbx_2026-05-16/grotto_message_in_bottle_LOD0_roblox.fbx`

## Parts & Colors

| Object | Role | Hex |
|--------|------|-----|
| msg_Glass | Bottle body + tall open neck | #8CB8A8 |
| msg_Scroll | Rolled note inside belly only | #F2E6C8 |

## Studio

- No cork — neck is open.
- Glass: transparency optional; scroll opaque cream in belly.
- `msg_Scroll` separate MeshPart for quest tint/highlight.

## Build

`Blender -b --python scripts/build_grotto_message_in_bottle.py`
