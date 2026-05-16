# Underwater — Roblox Import Spec

**Asset:** Branch Coral cluster  
**File:** `Underwater.fbx`  
**Scale:** 1 Blender unit = 1 Roblox stud  
**Export settings:** FBX, FACE smoothing, no animation, no leaf bones

---

## Parts & Colors

| Part Name | Color | Hex |
|---|---|---|
| Coral_Base_Pink | Pink base mound | `#FF6BA6` |
| Coral_Pink_01 | Tall center pink branch | `#FF6BA6` |
| Coral_Pink_02 | Left-leaning pink branch | `#FF6BA6` |
| Coral_Pink_03 | Front-right pink branch | `#FF6BA6` |
| Coral_Pink_04 | Short back pink branch | `#FF6BA6` |
| Coral_Orange_01 | Right-leaning orange branch | `#FF9426` |
| Coral_Orange_02 | Back-left orange branch | `#FF9426` |
| Coral_Orange_03 | Right orange branch | `#FF9426` |
| Coral_Orange_04 | Far-left orange branch | `#FF9426` |

---

## Studio Notes

- Import FBX — each part will come in as a separate `MeshPart`
- Set `Color` property per part using hex values above
- All parts share the same origin (world center) — group under a `Model` named `BranchCoral`
- Surface appearance: `Roughness = 0.85`, no specular
- Normals recalculated outward — no flipped face issues expected
