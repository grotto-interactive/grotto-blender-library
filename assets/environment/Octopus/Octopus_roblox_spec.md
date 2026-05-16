# Octopus — Roblox Import Spec

**Asset:** Stylized fantasy octopus (undersea / grotto environment)
**File:** `Octopus.fbx`
**Category:** environment

---

## Objects in FBX

| Object Name Pattern | Material | Hex Color | Roblox Color |
|---|---|---|---|
| `Octopus_Head`, `Octopus_Tent_[0-7]_Seg[00-06]` | M_OctopusBody | `#7060C8` | `Color3.fromRGB(112, 96, 200)` |
| `Octopus_Eye_Port`, `Octopus_Eye_Stbd`, `Octopus_Sucker_[0-7]_[00-03]` | M_OctopusAccent | `#D8A060` | `Color3.fromRGB(216, 160, 96)` |
| `Octopus_Pupil_Port`, `Octopus_Pupil_Stbd` | M_OctopusEye | `#0A0A0A` | `Color3.fromRGB(10, 10, 10)` |

> Three materials total. Set each Part's `Color` in Studio to match.

---

## Object List (93 total)

| Object | Count | Material |
|---|---|---|
| `Octopus_Head` | 1 | M_OctopusBody |
| `Octopus_Tent_[0-7]_Seg[00-06]` | 56 | M_OctopusBody |
| `Octopus_Eye_Port`, `Octopus_Eye_Stbd` | 2 | M_OctopusAccent |
| `Octopus_Sucker_[0-7]_[00-03]` | 32 | M_OctopusAccent |
| `Octopus_Pupil_Port`, `Octopus_Pupil_Stbd` | 2 | M_OctopusEye |

---

## Scale
- Built at **1 Blender unit = 1 Roblox stud**
- Body height: ~1.9 studs (seafloor to dome top)
- Body width at widest: ~2.8 studs
- Tentacle span tip-to-tip: ~9.2 studs (back tentacle longest at ~4.6 studs radius)
- Sits flat on the seafloor — base already at z=0

## Asset Description
Stylized fantasy octopus for a cozy undersea grotto world. Rounded dome head with a soft, gently curved top, widening at the midsection where large amber eyes sit on the forward sides. A wide web skirt at the base flares outward before the eight tentacles emerge. Tentacles flow directly from the body surface, spreading outward flat along the seafloor with tapered tips — some curl slightly upward for a fantastical feel. Warm amber accent suckers run along each tentacle. Periwinkle-violet body with warm amber accents and dark eyes. Low-poly, Roblox-ready.

## FBX Export Settings Used
- `mesh_smooth_type = FACE`
- `use_mesh_modifiers = True`
- `add_leaf_bones = False`
- `bake_anim = False`

---

## Studio Import Notes
- Import `Octopus.fbx` via **Model** tab → Import
- Set `Octopus_Head` and all `Octopus_Tent_*` Parts → `Color3.fromRGB(112, 96, 200)`
- Set `Octopus_Eye_Port`, `Octopus_Eye_Stbd`, and all `Octopus_Sucker_*` Parts → `Color3.fromRGB(216, 160, 96)`
- Set `Octopus_Pupil_Port` and `Octopus_Pupil_Stbd` → `Color3.fromRGB(10, 10, 10)`
- Place flat on the seafloor — base already at z=0
- Rotate Y to vary facing direction when placing multiples
- Works well with UnderwaterCave, SunkenShip, Kelp, and SandMounds assets
