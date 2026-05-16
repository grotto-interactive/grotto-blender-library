# SchoolOfFish — Roblox Import Spec

**Asset:** School of fish — ambient undersea formation (12 fish)
**File:** `SchoolOfFish.fbx`
**Category:** environment

---

## Objects in FBX

| Object Name Pattern | Material | Hex Color | Roblox Color |
|---|---|---|---|
| `Fish_[00-11]_Body` | M_FishBody | `#62B8D8` | `Color3.fromRGB(98, 184, 216)` |
| `Fish_[00-11]_DorsalFin`, `Fish_[00-11]_PecPort`, `Fish_[00-11]_PecStbd`, `Fish_[00-11]_Tail` | M_FishFin | `#2878A8` | `Color3.fromRGB(40, 120, 168)` |
| `Fish_[00-11]_EyeL`, `Fish_[00-11]_EyeR` | M_FishEye | `#0A0A0A` | `Color3.fromRGB(10, 10, 10)` |

> Three materials total. Set each Part's `Color` in Studio to match.

---

## Object List (84 total — 12 fish × 7 parts each)

| Part | Count | Material |
|---|---|---|
| `Fish_[00-11]_Body` | 12 | M_FishBody |
| `Fish_[00-11]_DorsalFin` | 12 | M_FishFin |
| `Fish_[00-11]_PecPort` | 12 | M_FishFin |
| `Fish_[00-11]_PecStbd` | 12 | M_FishFin |
| `Fish_[00-11]_Tail` | 12 | M_FishFin |
| `Fish_[00-11]_EyeL` | 12 | M_FishEye |
| `Fish_[00-11]_EyeR` | 12 | M_FishEye |

---

## Scale
- Built at **1 Blender unit = 1 Roblox stud**
- Individual fish body: ~1.2 studs long × ~0.44 studs wide × ~0.34 studs tall
- Full formation footprint: ~4 studs wide × ~6 studs deep × ~5 studs tall (3D scatter)
- Fish vary slightly in scale (0.85–1.0×) for a natural look

## Asset Description
12 low-poly stylized fish in a loose 3D school formation. Each fish has a tapered ellipsoid body, a forked tail fin, a dorsal fin, bilateral pectoral fins, and two dark eyes. All fins are solid wedge prisms — visible and readable from all angles. Fish are scattered at varied positions, rotations, and scales to simulate natural schooling behavior. Bright teal body with darker teal fins. Roblox-ready ambient asset for undersea scenes.

## FBX Export Settings Used
- `mesh_smooth_type = FACE`
- `use_mesh_modifiers = True`
- `add_leaf_bones = False`
- `bake_anim = False`

---

## Studio Import Notes
- Import `SchoolOfFish.fbx` via **Model** tab → Import
- Set all `Fish_*_Body` Parts → `Color3.fromRGB(98, 184, 216)`
- Set all `Fish_*_DorsalFin`, `Fish_*_PecPort`, `Fish_*_PecStbd`, `Fish_*_Tail` Parts → `Color3.fromRGB(40, 120, 168)`
- Set all `Fish_*_EyeL` and `Fish_*_EyeR` Parts → `Color3.fromRGB(10, 10, 10)`
- Formation is pre-arranged — no repositioning needed
- Can place the whole group and rotate Y to vary swimming direction
- Works well with Kelp, SandMounds, SunkenShip, and UnderwaterCave assets
