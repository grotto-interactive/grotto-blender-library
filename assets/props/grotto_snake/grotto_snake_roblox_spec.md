# Grotto Snake — Roblox Spec Doc

**Asset:** grotto_snake  
**Category:** Props  
**File:** `grotto_snake.blend` / `grotto_snake.fbx`  
**Scale:** 1 Blender unit = 1 Roblox stud  
**Overall Dimensions:** ~3.2 W × 3.2 D × 1.9 H studs  
**Intended use:** Environmental prop — jungle, dock, pirate scene, Seed Harbor

---

## Materials & Hex Colors

| Material Name | Hex Color | Roblox Material | Notes                                          |
|---------------|-----------|-----------------|------------------------------------------------|
| Snake_Body    | `#2E7D32` | SmoothPlastic   | Deep green — body segments, head              |
| Snake_Belly   | `#A5C840` | SmoothPlastic   | Yellow-green — alternating belly stripe       |
| Snake_Eye     | `#FDD835` | SmoothPlastic   | Yellow — eyes                                 |
| Snake_Tongue  | `#C62828` | SmoothPlastic   | Red — single tongue                           |

---

## Object List

| Object              | Description                                           |
|---------------------|-------------------------------------------------------|
| Snake_Seg_01–27     | Body cylinder segments — 27 total, coil + neck        |
| Snake_Joint_01–28   | Sphere joints at every waypoint — smooths connections |
| Snake_Head          | Flattened oval head, slightly tilted forward          |
| Snake_EyeL          | Left eye                                              |
| Snake_EyeR          | Right eye                                             |
| Snake_Tongue        | Single tongue prong extending from snout              |

**Total objects:** 59

---

## Layout Notes

- Snake is **coiled** flat on the ground — 1.75 loops winding clockwise inward.
- **Tail** starts at the outer edge (radius 1.5 studs) and winds inward to the centre.
- **Head** rises up from the coil centre via a S-curve neck, reaching Z≈1.74.
- Head faces **-Y direction**.
- **Body segments alternate** Snake_Body / Snake_Belly every 3 segments to create a stripe pattern.
- Body radius tapers: thin at tail (0.06) → thick through coil (0.18) → narrows at neck (0.11).
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
4. **Object count** — 59 objects. **Strongly recommended** to merge by material in Studio for performance.
5. **Orientation** — head faces -Z in Roblox Studio after FBX import with standard settings.

---

*Asset created by Tasha — Grotto Interactive LLC*  
*Spec written: 2026-05-09*
