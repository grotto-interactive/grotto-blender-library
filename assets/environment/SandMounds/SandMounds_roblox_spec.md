# SandMounds — Roblox Import Spec

**Asset:** Sand mound cluster (undersea environment)
**File:** `SandMounds.fbx`
**Category:** environment

---

## Objects in FBX

| Object Name | Material | Hex Color | Roblox Color |
|---|---|---|---|
| `SandMounds_SandMat` | SandMounds_SandMat | `#C5AD75` | `Color3.fromRGB(197, 173, 117)` |

> One object, one material. Set the Part's `Color` to the value above in Studio.

---

## Scale
- Built at **1 Blender unit = 1 Roblox stud**
- Mound heights: ~1.6–3.5 studs tall
- Mound widths: ~4–8.4 studs wide
- Full cluster footprint: ~14 studs wide × 10 studs deep

## Asset Description
Cluster of 5 sand mounds at varied sizes — one large center mound, two large flanking mounds, one medium, and one small. Each mound is a low-poly dome with slightly oval/irregular base for a natural feel. Faceted shading gives a stylized Roblox-ready look. Warm sandy tan color throughout.

## Mound sizes (approximate)
| Mound | Width | Height |
|---|---|---|
| Centre (large) | 8.4 studs | 3.5 studs |
| Right (large) | 7.0 studs | 3.0 studs |
| Left (large) | 7.2 studs | 2.8 studs |
| Front-right (medium) | 4.8 studs | 2.0 studs |
| Front-left (small) | 4.6 studs | 1.6 studs |

## FBX Export Settings Used
- `mesh_smooth_type = FACE`
- `use_mesh_modifiers = True`
- `add_leaf_bones = False`
- `bake_anim = False`

---

## Studio Import Notes
- Import `SandMounds.fbx` via **Model** tab → Import
- Set `SandMounds_SandMat` Part Color → `Color3.fromRGB(197, 173, 117)`
- Place flat on the seafloor
- Works well combined with Kelp assets for an undersea scene
