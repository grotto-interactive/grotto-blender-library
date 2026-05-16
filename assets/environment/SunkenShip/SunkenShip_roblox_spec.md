# SunkenShip — Roblox Import Spec

**Asset:** Broken sunken pirate ship (undersea environment)
**File:** `SunkenShip.fbx`
**Category:** environment

---

## Objects in FBX

| Object Name Pattern | Material | Hex Color | Roblox Color |
|---|---|---|---|
| `Hull_*`, `Deck_*`, `Sterncastle`, `FC_*`, `SC_*`, `MD_*`, `Stairs_*` | M_Hull | `#7C5530` | `Color3.fromRGB(124, 85, 48)` |
| `Deck_*` (deck planking) | M_Deck | `#CBAD7C` | `Color3.fromRGB(203, 173, 124)` |
| `Mast_Base`, `Mast_Fallen`, `Yard`, `CrowsNest` | M_Hull | `#7C5530` | `Color3.fromRGB(124, 85, 48)` |
| `Sail` | M_Sail | `#F7F1E1` | `Color3.fromRGB(247, 241, 225)` |
| `Flag_Main` | M_Flag | `#494949` | `Color3.fromRGB(73, 73, 73)` |
| `Cannon_Barrel_*`, `Cannon_Carriage_*`, `Porthole_*`, `Anchor_Ring` | M_Metal | `#616169` | `Color3.fromRGB(97, 97, 105)` |
| `Wheel_*` | M_Wheel | `#996C38` | `Color3.fromRGB(153, 108, 56)` |
| `Plank_*` | M_Hull | `#7C5530` | `Color3.fromRGB(124, 85, 48)` |

> Set each Part's `Color` in Studio to match the material it belongs to. Match by object name prefix.

---

## Scale
- Built at **1 Blender unit = 1 Roblox stud**
- Full wreck footprint: ~30 studs wide × ~25 studs deep (including scattered debris)
- Each hull half: ~8 studs wide × ~5 studs tall (above seafloor), ~5 studs below seafloor
- Mast: split into `Mast_Base` (stump on hull) and `Mast_Fallen` (fallen top, on seafloor)
- Broken planks (`Plank_00–11`): 2–4 studs long, scattered across the seafloor

## Asset Description
Pirate ship broken in half — two hull halves angled ~50° outward from the break point, tips diving into the seafloor. Both break faces are near seafloor level with jagged, splintered edges. The bow half retains the mast stump (`Mast_Base`); the mast top (`Mast_Fallen`) has snapped off and fallen to the seafloor along with the yard, sail, crow's nest, and flag. The stern half includes the sterncastle, ship's wheel, aft railings, and two cannon pairs. Hull surfaces show worn, damaged geometry with roughed-up break edges and displaced planking. 12 broken planks are scattered around the wreck site. Low-poly, Roblox-ready.

## Wreck Pose
| Feature | Detail |
|---|---|
| Break point | Midship — Hull and Deck split at x=0 (Blender) |
| Bow half angle | ~50° outward (bow tip into seafloor) |
| Stern half angle | ~50° outward (stern tip into seafloor) |
| Break edges | Jagged and roughed up on both hull halves |
| Mast_Base | Stump remains attached to the bow hull |
| Mast_Fallen | Snapped top lying on the seafloor, bow side |
| Sail / Yard / CrowsNest / Flag_Main | Fallen with the mast on the seafloor |
| Break gap | ~6 studs between the two half break faces |
| Plank scatter | ~20 studs radius from break center |

## FBX Export Settings Used
- `mesh_smooth_type = FACE`
- `use_mesh_modifiers = True`
- `add_leaf_bones = False`
- `bake_anim = False`

---

## Studio Import Notes
- Import `SunkenShip.fbx` via **Model** tab → Import
- Apply colors per object name prefix using the table above
- Place with the break gap centered on the seafloor — both hull halves should be partially submerged
- `Mast_Fallen`, `Sail`, `Yard`, `CrowsNest`, and `Flag_Main` are on the seafloor on the bow side — no repositioning needed
- `Plank_*` objects are pre-scattered; no repositioning needed
- Works well with Kelp, SandMounds, and UnderwaterCave assets for a full undersea scene
