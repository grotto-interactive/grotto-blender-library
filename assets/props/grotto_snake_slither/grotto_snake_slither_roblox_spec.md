# Grotto Snake (Slithering) — Roblox Spec Doc

**Asset:** grotto_snake_slither  
**Category:** Props  
**File:** `grotto_snake_slither.blend` / `grotto_snake_slither.fbx`  
**Scale:** 1 Blender unit = 1 Roblox stud  
**Overall Dimensions:** ~8.7 W × 2.6 D × 1.0 H studs  
**Intended use:** Environmental prop — jungle, dock, pirate scene, Seed Harbor

---

## Materials & Hex Colors

| Material Name | Hex Color | Roblox Material | Notes                                          |
|---------------|-----------|-----------------|------------------------------------------------|
| Snake_Body    | `#2E7D32` | SmoothPlastic   | Deep green — body segments, head              |
| Snake_Belly   | `#A5C840` | SmoothPlastic   | Yellow-green — alternating belly stripe       |
| Snake_Eye     | `#FDD835` | SmoothPlastic   | Yellow — eyes                                 |
| Snake_Tongue  | `#C62828` | SmoothPlastic   | Red — tongue                                  |

---

## Object List

| Object              | Description                                                    |
|---------------------|----------------------------------------------------------------|
| Snake_Seg_01–24     | Body cylinder segments — 24 total, spanning the S-curve        |
| Snake_Joint_01–25   | Sphere joints at every waypoint — smooths segment connections  |
| Snake_Head          | Flattened oval head, slightly elevated, facing +X              |
| Snake_EyeL          | Left eye                                                       |
| Snake_EyeR          | Right eye                                                      |
| Snake_Tongue        | Tongue extending from snout toward +X                          |

**Total objects:** 53

---

## Layout Notes

- Snake is in a **mid-slither S-curve** pose — 1.5 sinusoidal waves along the X axis.
- **Tail** starts at the left (X ≈ −3.75) close to the ground (Z = 0.22).
- **Head** is at the right end (X ≈ +4.56), slightly raised (Z ≈ 0.83), facing **+X direction**.
- Y undulation amplitude = 1.1 studs (body swings ±1.1 from center).
- Body radius tapers: thin at tail → thick through mid-body (0.18) → narrows toward neck (0.11).
- **Body segments alternate** Snake_Body / Snake_Belly every 3 segments to create a stripe pattern.
- Joint spheres cover every segment junction for a smooth connected look.

---

## Studio Import Notes

1. **FBX is ready to import** — no conversion steps needed.
2. **Scale** — import at 1.0. Each unit = 1 stud.
3. **Apply materials by name:**
   - `Snake_Seg_*` and `Snake_Joint_*` — check name suffix; alternate groups of 3 get `#2E7D32` vs `#A5C840`
   - `Snake_Head` → `#2E7D32` SmoothPlastic
   - `Snake_Eye*` → `#FDD835` SmoothPlastic
   - `Snake_Tongue` → `#C62828` SmoothPlastic
4. **Object count** — 53 objects. **Recommended** to merge by material in Studio for performance.
5. **Orientation** — head faces +Z in Roblox Studio after FBX import with standard settings (the +X axis in Blender maps to +Z in Studio).

---

*Asset created by Tasha — Grotto Interactive LLC*  
*Spec written: 2026-05-09*
