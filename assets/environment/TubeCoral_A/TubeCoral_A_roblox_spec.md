# TubeCoral_A — Roblox Import Spec

**Asset:** Stylized tube coral cluster  
**File:** `TubeCoral_A.fbx`  
**Scale:** 1 Blender unit = 1 Roblox stud  
**Export settings:** FBX, FACE smoothing, no animation, no leaf bones

---

## Parts & Colors

| Part Name | Height (studs) | Color | Hex |
|---|---|---|---|
| TubeCoral_Teal_01 | 4.2 — tallest, center | Teal | `#0DADB3` |
| TubeCoral_Teal_02 | 3.6 | Teal | `#0DADB3` |
| TubeCoral_Teal_03 | 3.8 | Teal | `#0DADB3` |
| TubeCoral_Teal_04 | 2.4 | Teal | `#0DADB3` |
| TubeCoral_Yellow_01 | 2.9 | Yellow | `#FAD11F` |
| TubeCoral_Yellow_02 | 2.2 | Yellow | `#FAD11F` |
| TubeCoral_Yellow_03 | 2.6 | Yellow | `#FAD11F` |

---

## Studio Notes

- Import FBX — each part comes in as a separate `MeshPart`
- Set `Color` per part using hex values above (2 colors total)
- Group all parts under a `Model` named `TubeCoral_A`
- Surface: `Roughness = 0.75`, no specular
- Tubes are hollow — inner faces are intentionally inward-facing for shadow depth
- All tubes sit at world origin (z = 0), slightly tilted for organic clustering
- Normals recalculated outward — no flipped face issues expected
