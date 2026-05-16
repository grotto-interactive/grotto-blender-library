# Starfish — Roblox Import Spec

**Asset:** Stylized fantasy sea star (undersea / tidepool environment)
**File:** `Starfish.fbx`
**Category:** environment

---

## Objects in FBX

| Object Name Pattern | Material | Hex Color | Roblox Color |
|---|---|---|---|
| `Starfish_Arm_00` – `Starfish_Arm_04` | M_StarfishBody | `#B84878` | `Color3.fromRGB(184, 72, 120)` |
| `Starfish_Knob_*`, `Starfish_SideKnob_*` | M_StarfishCoral | `#E89050` | `Color3.fromRGB(232, 144, 80)` |

> Two materials total. Set each Part's `Color` in Studio to match.

---

## Object List (40 total)

| Objects | Count | Material |
|---|---|---|
| `Starfish_Arm_00` – `Starfish_Arm_04` | 5 | M_StarfishBody |
| `Starfish_Knob_[0-4]_[0-2]` (spine knobs) | 15 | M_StarfishCoral |
| `Starfish_SideKnob_[0-4]_[0-1]_[0-1]` (side knobs) | 20 | M_StarfishCoral |

---

## Scale
- Built at **1 Blender unit = 1 Roblox stud**
- Total diameter (tip to tip): ~7.5 studs
- Arm height at base: ~0.5 studs (rounded cross-section)
- Sits flat on the seafloor

## Asset Description
Stylized fantasy sea star for a cozy maritime tidepool world. Five thick, rounded arms with a half-ellipse cross-section and soft asymmetry — each arm is slightly different in length, width, and angle for a hand-crafted organic feel. Organic bump ridges are baked into the arm geometry along the length. Coral-orange knobs (spine + side rows) are embedded into the surface at ~75% emergence. Deep rose-purple body (`M_StarfishBody`) with warm coral-orange knobs (`M_StarfishCoral`). Low-poly, Roblox-ready.

## FBX Export Settings Used
- `mesh_smooth_type = FACE`
- `use_mesh_modifiers = True`
- `add_leaf_bones = False`
- `bake_anim = False`

---

## Studio Import Notes
- Import `Starfish.fbx` via **Model** tab → Import
- Set all `Starfish_Arm_*` Parts → `Color3.fromRGB(184, 72, 120)`
- Set all `Starfish_Knob_*` and `Starfish_SideKnob_*` Parts → `Color3.fromRGB(232, 144, 80)`
- Place flat on the seafloor — base already at z=0
- Rotate Y at varied angles when scattering multiples
- Works well with Crab, Kelp, SandMounds, and UnderwaterCave assets
