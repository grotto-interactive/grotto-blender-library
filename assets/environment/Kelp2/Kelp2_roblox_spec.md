# Kelp2 — Roblox Import Spec

**Asset:** Kelp cluster v2 (undersea environment)
**File:** `Kelp2.fbx`
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
- Stalk heights: ~7.5, ~9.0, ~10.5 studs
- Cluster footprint: ~4 studs wide

## Asset Description
Three-stalk kelp cluster. Stalks are thick, flat-oval tapered columns (~0.65 wide × 0.40 deep at base) with a gentle organic sway. Each stalk has 4–6 long, flowing leaves that bloom directly out of the stalk body — leaves are thick at the base (matching stalk depth) and taper to a pointed tip. Leaves fan out 360° around each stalk at different heights. Low-poly, Roblox-ready.

## FBX Export Settings Used
- `mesh_smooth_type = FACE`
- `use_mesh_modifiers = True`
- `add_leaf_bones = False`
- `bake_anim = False`

---

## Studio Import Notes
- Import `Kelp2.fbx` via **Model** tab → Import
- Set `Kelp_GreenMat` Part Color → `Color3.fromRGB(69, 129, 74)`
- Anchor the base at seafloor level
- Works well tiled in multiples at varied Y rotations for a dense kelp forest scene
