# UnderwaterCave — Roblox Import Spec

**Asset:** Underwater cave arch / tunnel entrance (undersea environment)
**File:** `UnderwaterCave.fbx`
**Category:** environment

---

## Objects in FBX

| Object Name | Material | Hex Color | Roblox Color |
|---|---|---|---|
| `UnderwaterCave_RockMat` | UnderwaterCave_RockMat | `#59647B` | `Color3.fromRGB(89, 100, 123)` |

> One object, one material. Set the Part's `Color` to the value above in Studio.

---

## Scale
- Built at **1 Blender unit = 1 Roblox stud**
- Arch opening: ~14 studs wide × ~10.5 studs tall
- Overall rock mass: ~28 studs wide × ~20 studs tall × ~8 studs deep
- Rock wall thickness (sides): ~7 studs
- Rock wall thickness (top): ~9.5 studs

## Asset Description
Single stone cave arch — open on both sides as a walk-through tunnel entrance. Inner arch is a smooth elliptical arch with straight vertical sides at the base (~14 studs wide, ~10.5 studs tall). Outer rocky silhouette is heavily irregular with large angular juts and deep indentations giving a rough, natural stone look. Front and back rock faces are displaced for additional surface roughness — angular faceted geometry reads as rough stone under Roblox's flat shading. Blue-grey stone color throughout. Low-poly, Roblox-ready.

## Mound geometry (approximate)
| Feature | Dimension |
|---|---|
| Arch opening width | 14 studs |
| Arch opening height | 10.5 studs |
| Outer rock width | ~28 studs |
| Outer rock height | ~20 studs |
| Tunnel depth | ~8 studs |

## FBX Export Settings Used
- `mesh_smooth_type = FACE`
- `use_mesh_modifiers = True`
- `add_leaf_bones = False`
- `bake_anim = False`

---

## Studio Import Notes
- Import `UnderwaterCave.fbx` via **Model** tab → Import
- Set `UnderwaterCave_RockMat` Part Color → `Color3.fromRGB(89, 100, 123)`
- Place with base flat on the seafloor (bottom edge at seafloor level)
- Arch tunnel opens along the Y axis — rotate as needed to face the correct direction
- Works well combined with Kelp and SandMounds assets for an undersea scene
