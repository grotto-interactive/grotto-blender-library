# BrainCoral_A — Roblox Import Spec

**Asset:** Stylized brain coral dome  
**File:** `BrainCoral_A.fbx`  
**Scale:** 1 Blender unit = 1 Roblox stud (~4 studs wide, ~2 studs tall)  
**Export settings:** FBX, FACE smoothing, no animation, no leaf bones

---

## Parts & Colors

| Part Name | Description | Color | Hex |
|---|---|---|---|
| BrainCoral_A_Tan | Dome body — valleys and base | Warm Tan | `#D19E61` |
| BrainCoral_A_Cream | Winding maze ridges across surface | Cream | `#F2E6BF` |

---

## Studio Notes

- Import FBX — 2 parts come in as separate `MeshPart` objects
- Set `Color` per part using hex values above
- Group both parts under a `Model` named `BrainCoral_A`
- Surface: `Roughness = 0.82`, no specular
- The cream ridges are a separate mesh sitting on top of the tan base — keep both parts at the same position (world origin) so the groove pattern aligns correctly
- Dome sits flat on the ground at world origin, ~4 studs wide
- Normals recalculated outward on both parts
