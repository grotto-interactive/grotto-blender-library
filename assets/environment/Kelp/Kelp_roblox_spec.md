# Kelp — Roblox Import Spec

**Asset:** Kelp cluster (undersea environment)  
**File:** `Kelp.fbx`  
**Category:** environment  

---

## Objects in FBX

| Object Name | Material | Hex Color | Roblox Color (BrickColor/Color3) |
|---|---|---|---|
| `Kelp_GreenMat` | Kelp_GreenMat | `#45814A` | `Color3.fromRGB(69, 129, 74)` |

> One object, one material. Set the Part's `Color` to the value above in Studio.

---

## Scale
- Built at **1 Blender unit = 1 Roblox stud**
- Stalk heights: ~7.5, ~9.0, ~10.5 studs (cluster of 3)
- Overall footprint: ~3 studs wide

## FBX Export Settings Used
- `mesh_smooth_type = FACE`
- `use_mesh_modifiers = True`
- `add_leaf_bones = False`
- `bake_anim = False`

---

## Studio Import Notes
- Import `Kelp.fbx` via **Model** tab → Import
- Set `Kelp_GreenMat` Part Color → `Color3.fromRGB(69, 129, 74)`
- The blades are 3D (have thickness) — no need to enable DoubleSided
- Anchor the base at ground/seafloor level
- Works well grouped in multiples at different Y rotations for a dense kelp forest

---

## Asset Description
Three-stalk kelp cluster. Stalks are tapered 8-sided cylinders that lean slightly at the top. Each stalk has 4–6 rounded petal-shaped blade fronds radiating outward at evenly distributed angles around the stalk. Blades are smaller toward the top of each stalk. Low-poly, Roblox-ready.
