# Jellyfish — Roblox Import Spec

**Asset:** Stylized fantasy jellyfish (undersea / grotto environment)
**File:** `Jellyfish.fbx`
**Category:** environment

---

## Objects in FBX

| Object Name Pattern | Material | Hex Color | Roblox Color |
|---|---|---|---|
| `Jellyfish_Bell` | M_JellyBell | `#E0C0F0` | `Color3.fromRGB(224, 192, 240)` |
| `Jellyfish_Core` | M_JellyBell | `#E0C0F0` | `Color3.fromRGB(224, 192, 240)` |
| `Jellyfish_OralArm_[0-3]_Seg[00-02]`, `Jellyfish_Mid_[0-7]_Seg[00-02]`, `Jellyfish_Tent_[0-7]_Seg[00-03]` | M_JellyTentacle | `#C060C8` | `Color3.fromRGB(192, 96, 200)` |

> Two materials total. Set each Part's `Color` in Studio to match.

---

## Object List (70 total)

| Object | Count | Material |
|---|---|---|
| `Jellyfish_Bell` | 1 | M_JellyBell |
| `Jellyfish_Core` | 1 | M_JellyBell |
| `Jellyfish_OralArm_[0-3]_Seg[00-02]` | 12 | M_JellyTentacle |
| `Jellyfish_Mid_[0-7]_Seg[00-02]` | 24 | M_JellyTentacle |
| `Jellyfish_Tent_[0-7]_Seg[00-03]` | 32 | M_JellyTentacle |

---

## Scale
- Built at **1 Blender unit = 1 Roblox stud**
- Bell diameter: ~2.0 studs wide × ~1.24 studs tall
- Full height including tentacles: ~3.5 studs
- Outer tentacle span tip-to-tip: ~2.0 studs (hang straight down)

## Asset Description
Stylized fantasy jellyfish for a cozy undersea grotto world. Smooth rounded dome bell with a gentle elliptical profile and soft faceted low-poly surface. Three rings of hanging tentacles: four short oral arms at the center, eight medium-length middle tentacles, and eight long outer tentacles at the bell rim. All tentacles hang straight down, tapered to fine points. Soft lavender bell with vivid violet-magenta tentacles. Low-poly, Roblox-ready.

## FBX Export Settings Used
- `mesh_smooth_type = FACE`
- `use_mesh_modifiers = True`
- `add_leaf_bones = False`
- `bake_anim = False`

---

## Studio Import Notes
- Import `Jellyfish.fbx` via **Model** tab → Import
- Set `Jellyfish_Bell` and `Jellyfish_Core` → `Color3.fromRGB(224, 192, 240)`
- Set all `Jellyfish_OralArm_*`, `Jellyfish_Mid_*`, and `Jellyfish_Tent_*` Parts → `Color3.fromRGB(192, 96, 200)`
- Place floating above the seafloor or mid-water column
- Rotate Y to vary facing direction when placing multiples
- Works well with Kelp, SchoolOfFish, UnderwaterCave, and SunkenShip assets
