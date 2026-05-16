# FanCoral_A — Roblox Import Spec

**Asset:** Stylized sea fan coral  
**File:** `FanCoral_A.fbx`  
**Scale:** 1 Blender unit = 1 Roblox stud  
**Export settings:** FBX, FACE smoothing, no animation, no leaf bones

---

## Parts & Colors

| Part Name | Description | Color | Hex |
|---|---|---|---|
| FanCoral_Stalk_Purple | Main stalk | Purple | `#7314BF` |
| FanCoral_PrimFL_Purple | Far-left primary branch | Purple | `#7314BF` |
| FanCoral_PrimL_Purple | Left primary branch | Purple | `#7314BF` |
| FanCoral_PrimC_Purple | Center primary branch | Purple | `#7314BF` |
| FanCoral_PrimR_Purple | Right primary branch | Purple | `#7314BF` |
| FanCoral_PrimFR_Purple | Far-right primary branch | Purple | `#7314BF` |
| FanCoral_SecFL_L_Magenta | Far-left outer secondary | Magenta | `#E0148C` |
| FanCoral_SecFL_R_Magenta | Far-left inner secondary | Magenta | `#E0148C` |
| FanCoral_SecL_L_Magenta | Left outer secondary | Magenta | `#E0148C` |
| FanCoral_SecL_R_Magenta | Left inner secondary | Magenta | `#E0148C` |
| FanCoral_SecC_L_Magenta | Center-left secondary | Magenta | `#E0148C` |
| FanCoral_SecC_R_Magenta | Center-right secondary | Magenta | `#E0148C` |
| FanCoral_SecR_L_Magenta | Right inner secondary | Magenta | `#E0148C` |
| FanCoral_SecR_R_Magenta | Right outer secondary | Magenta | `#E0148C` |
| FanCoral_SecFR_L_Magenta | Far-right inner secondary | Magenta | `#E0148C` |
| FanCoral_SecFR_R_Magenta | Far-right outer secondary | Magenta | `#E0148C` |

---

## Studio Notes

- Import FBX — each part comes in as a separate `MeshPart`
- Set `Color` per part using hex values above (2 colors total)
- Group all parts under a `Model` named `FanCoral_A`
- Surface: `Roughness = 0.72`, no specular
- Asset sits flat on the ground — stalk base at world origin
- Normals recalculated outward — no flipped face issues expected
