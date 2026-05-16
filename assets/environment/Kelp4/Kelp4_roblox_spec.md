# Kelp4 — Roblox Import Spec

**Asset:** Kelp / seagrass cluster v4 (undersea environment)
**File:** `Kelp4.fbx`
**Category:** environment

---

## Objects in FBX

| Object Name | Material | Hex Color | Roblox Color |
|---|---|---|---|
| `Kelp_GreenMat` | Kelp_GreenMat | `#45814A` | `Color3.fromRGB(69, 129, 74)` |

> One object, one material. Set the Part's `Color` to the value above in Studio.

---

## Scale
- Built at **1 Blender unit = 1 Roblox stud**
- Leaf heights: ~6.5–8.0 studs tall
- Cluster footprint: ~4 studs wide

## Asset Description
Three-cluster kelp patch — no stalk. 15 thick, flowing leaves grow directly from the seafloor. Leaves are taller than v3 (6.5–8 studs) and have pronounced S-curve flow — a primary sway plus a secondary ripple that gives each leaf the appearance of moving in an underwater current. Leaves fan 360° around three base points, thick at the base and tapering to a pointed tip. Low-poly, Roblox-ready.

## FBX Export Settings Used
- `mesh_smooth_type = FACE`
- `use_mesh_modifiers = True`
- `add_leaf_bones = False`
- `bake_anim = False`

---

## Studio Import Notes
- Import `Kelp4.fbx` via **Model** tab → Import
- Set `Kelp_GreenMat` Part Color → `Color3.fromRGB(69, 129, 74)`
- Anchor base flat on the seafloor
- Tile in multiples at varied Y rotations for a dense underwater scene
