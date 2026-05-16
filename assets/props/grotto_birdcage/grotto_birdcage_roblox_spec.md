# Grotto Birdcage — Roblox Spec Doc

**Asset:** grotto_birdcage  
**Category:** Props  
**File:** `grotto_birdcage.blend` / `grotto_birdcage.fbx`  
**Scale:** 1 Blender unit = 1 Roblox stud  
**Overall Dimensions:** ~2.1 W × 2.1 D × ~3.7 H studs  
**Intended use:** Environmental prop — pirate dock, tavern, ship cabin, Seed Harbor

---

## Materials & Hex Colors

| Material Name | Hex Color | Roblox Material | Notes                        |
|---------------|-----------|-----------------|------------------------------|
| Cage_Brass    | `#C9A060` | SmoothPlastic   | Warm aged brass — all parts  |

---

## Object List

| Object          | Description                                 |
|-----------------|---------------------------------------------|
| Cage_Base       | Flat circular base disc                     |
| Cage_RingBottom | Structural ring at bottom of bars           |
| Cage_RingMid    | Structural ring at midpoint of bars         |
| Cage_RingTop    | Structural ring at top of bars / dome base  |
| Cage_Bar_01–12  | 12 vertical bars around the cage perimeter  |
| Cage_Dome       | Hemisphere dome cap at top                  |
| Cage_Knob       | Small sphere at dome tip                    |
| Cage_HangRing   | Vertical hanging ring at very top           |

**Total objects:** 19

---

## Layout Notes

- Cage centered at world origin (X=0, Y=0). Base sits flat on Z=0.
- **Bars** are arranged evenly at 30° intervals around radius = 1.0 stud. Bar height = 2.5 studs.
- **Three horizontal rings** at: Z=0.08 (bottom), Z=1.33 (mid), Z=2.58 (top/dome base).
- **Dome** is a hemisphere, radius = 1.0 stud, base at Z=2.58, peak at Z=3.58.
- **Hang ring** is vertical (rotated 90° on X) — acts as a hook loop for hanging the cage.

---

## Studio Import Notes

1. **FBX is ready to import** — no conversion steps needed.
2. **Scale** — import at 1.0. Each unit = 1 stud.
3. **All parts use one material** — apply `#C9A060` SmoothPlastic to every object.
4. **Object count** — 19 objects. Consider merging all into one mesh by material in Studio for performance.
5. **Orientation** — cage sits upright. Hang ring at top for attaching to a ceiling/rope attachment point.

---

*Asset created by Tasha — Grotto Interactive LLC*  
*Spec written: 2026-05-09*
