# Crab — Roblox Import Spec

**Asset:** Ambient crab (undersea environment)
**File:** `Crab.fbx`
**Category:** environment

---

## Objects in FBX

| Object Name Pattern | Material | Hex Color | Roblox Color |
|---|---|---|---|
| `Carapace`, `Plastron`, `Claw_*`, `Eye_*_Stalk`, `Leg_*` | M_Crab | `#C1502A` | `Color3.fromRGB(193, 80, 42)` |
| `Eye_Port_Ball`, `Eye_Stbd_Ball` | M_Eye | `#050505` | `Color3.fromRGB(5, 5, 5)` |

> Two materials total. Set each Part's `Color` in Studio to match.

---

## Object List (32 total)

| Object | Material |
|---|---|
| `Carapace` | M_Crab |
| `Plastron` | M_Crab |
| `Eye_Port_Stalk`, `Eye_Stbd_Stalk` | M_Crab |
| `Eye_Port_Ball`, `Eye_Stbd_Ball` | M_Eye |
| `Claw_Port_Arm`, `Claw_Stbd_Arm` | M_Crab |
| `Claw_Port_Fore`, `Claw_Stbd_Fore` | M_Crab |
| `Claw_Port_PincerBase`, `Claw_Stbd_PincerBase` | M_Crab |
| `Claw_Port_FingerUpper`, `Claw_Stbd_FingerUpper` | M_Crab |
| `Claw_Port_FingerLower`, `Claw_Stbd_FingerLower` | M_Crab |
| `Leg_Port_0_Upper` – `Leg_Port_3_Upper` | M_Crab |
| `Leg_Port_0_Lower` – `Leg_Port_3_Lower` | M_Crab |
| `Leg_Stbd_0_Upper` – `Leg_Stbd_3_Upper` | M_Crab |
| `Leg_Stbd_0_Lower` – `Leg_Stbd_3_Lower` | M_Crab |

---

## Scale
- Built at **1 Blender unit = 1 Roblox stud**
- Carapace: ~2.8 studs wide × ~2.0 studs deep × ~0.64 studs tall
- Total width including legs: ~5.5 studs
- Total width including claws: ~7.0 studs
- Sits flat on seafloor

## Asset Description
Low-poly ambient crab. Oval carapace (top shell) with matching plastron (flat bottom shell). Two eye stalks with dark eyeballs at the front. Two front claws (arm → forearm → pincer base → two open fingers). Eight walking legs in two-segment pairs (upper + lower), spread outward and bent to the seafloor. Warm orange-red color. Roblox-ready ambient creature for undersea scenes.

## FBX Export Settings Used
- `mesh_smooth_type = FACE`
- `use_mesh_modifiers = True`
- `add_leaf_bones = False`
- `bake_anim = False`

---

## Studio Import Notes
- Import `Crab.fbx` via **Model** tab → Import
- Set all `M_Crab` Parts → `Color3.fromRGB(193, 80, 42)`
- Set `Eye_Port_Ball` and `Eye_Stbd_Ball` Parts → `Color3.fromRGB(5, 5, 5)`
- Place flat on the seafloor — base already sits at z=0
- Scatter multiples at varied Y rotations for a natural ambient population
- Works well with SunkenShip, Kelp, and SandMounds assets
