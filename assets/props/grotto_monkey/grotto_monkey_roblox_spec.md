# Grotto Monkey — Roblox Spec Doc

**Asset:** grotto_monkey  
**Category:** Props  
**File:** `grotto_monkey.blend` / `grotto_monkey.fbx`  
**Scale:** 1 Blender unit = 1 Roblox stud  
**Overall Dimensions:** ~3.0 W × 2.5 D × 4.5 H studs  
**Intended use:** Environmental prop — pirate dock, jungle scene, Seed Harbor

---

## Materials & Hex Colors

| Material Name | Hex Color | Roblox Material | Notes                                              |
|---------------|-----------|-----------------|---------------------------------------------------|
| Monkey_Brown  | `#8B5A2B` | SmoothPlastic   | Warm brown — body, head, arms, legs, tail         |
| Monkey_Tan    | `#D2956A` | SmoothPlastic   | Light tan — belly, muzzle, inner ears, hands, feet|
| Monkey_Eye    | `#1A1A1A` | SmoothPlastic   | Near-black — eyes                                 |

---

## Object List

| Object               | Material      | Description                          |
|----------------------|---------------|--------------------------------------|
| Monkey_Body          | Monkey_Brown  | Main torso sphere                    |
| Monkey_Belly         | Monkey_Tan    | Belly patch on front of body         |
| Monkey_Head          | Monkey_Brown  | Head sphere (large, cartoon scale)   |
| Monkey_Muzzle        | Monkey_Tan    | Face muzzle oval                     |
| Monkey_Nose          | Monkey_Tan    | Small nose sphere                    |
| Monkey_EarL/R        | Monkey_Brown  | Outer ear spheres (×2)               |
| Monkey_EarInnerL/R   | Monkey_Tan    | Inner ear discs (×2)                 |
| Monkey_EyeL/R        | Monkey_Eye    | Eyes (×2)                            |
| Monkey_ArmL/R        | Monkey_Brown  | Arm cylinders, angled 15° out (×2)   |
| Monkey_ShoulderCapL/R| Monkey_Brown  | Shoulder junction spheres (×2)       |
| Monkey_HandL/R       | Monkey_Tan    | Hand spheres at arm tips (×2)        |
| Monkey_LegL/R        | Monkey_Brown  | Leg cylinders (×2)                   |
| Monkey_FootL/R       | Monkey_Tan    | Foot ovals (×2)                      |
| Monkey_Tail_1–5      | Monkey_Brown  | Tail segments — 5 chained cylinders  |
| Monkey_TailJoint_1–6 | Monkey_Brown  | Spheres at each tail joint           |

**Total objects:** 32

---

## Layout Notes

- Monkey faces **-Y direction**.
- Feet sit at **Z=0** (ground level). Total height ~4.5 studs.
- **Arms** connect at shoulders (X=±0.72, Z=2.15) with 15° outward tilt. Shoulder cap spheres cover the joint.
- **Tail** starts at rump (inside back of body) and curves outward to the right, sweeping backward then up. Six joint spheres cover the segment connections.
- All parts scaled ~2× from base build for Roblox prop proportions.

---

## Studio Import Notes

1. **FBX is ready to import** — no conversion steps needed.
2. **Scale** — import at 1.0. Each unit = 1 stud.
3. **Apply materials by name:**
   - `Monkey_Body`, `Monkey_Head`, `Monkey_Arm*`, `Monkey_Leg*`, `Monkey_Ear[LR]`, `Monkey_Shoulder*`, `Monkey_Tail*` → `#8B5A2B` SmoothPlastic
   - `Monkey_Belly`, `Monkey_Muzzle`, `Monkey_Nose`, `Monkey_EarInner*`, `Monkey_Hand*`, `Monkey_Foot*` → `#D2956A` SmoothPlastic
   - `Monkey_Eye*` → `#1A1A1A` SmoothPlastic
4. **Object count** — 32 objects. Consider merging by material in Studio for performance.
5. **Orientation** — monkey faces -Z in Roblox Studio after FBX import with standard settings.

---

*Asset created by Tasha — Grotto Interactive LLC*  
*Spec written: 2026-05-09*
