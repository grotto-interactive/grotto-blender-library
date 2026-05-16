# Kelp3 — Roblox Import Spec

**Asset:** Kelp / seagrass cluster v3 (undersea environment)
**File:** `Kelp3.fbx`
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
- Leaf heights: ~4–4.5 studs tall
- Cluster footprint: ~4 studs wide

## Asset Description
Three-cluster seagrass/kelp patch — no stalk. 15 thick, flowing leaves grow directly from the seafloor, fanning 360° around three base points. Each leaf starts narrow at the base, blooms to full width, then tapers to a pointed tip. Leaves have significant depth at the base (0.35 studs) tapering to a slim tip, giving them real volume. Low-poly, Roblox-ready.

## FBX Export Settings Used
- `mesh_smooth_type = FACE`
- `use_mesh_modifiers = True`
- `add_leaf_bones = False`
- `bake_anim = False`

---

## Studio Import Notes
- Import `Kelp3.fbx` via **Model** tab → Import
- Set `Kelp_GreenMat` Part Color → `Color3.fromRGB(69, 129, 74)`
- Anchor base flat on the seafloor
- Tile in multiples at varied Y rotations for dense underwater ground cover
