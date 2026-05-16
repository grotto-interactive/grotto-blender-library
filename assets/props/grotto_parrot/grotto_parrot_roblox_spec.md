# Grotto Parrot — Roblox Spec Doc

**Asset:** grotto_parrot  
**Category:** Props  
**File:** `grotto_parrot.blend` / `grotto_parrot.fbx`  
**Scale:** 1 Blender unit = 1 Roblox stud  
**Overall Dimensions:** ~2.0 W × 2.5 D × 2.8 H studs  
**Intended use:** Environmental prop — birdcage perch, pirate shoulder, dock scene, Seed Harbor

---

## Materials & Hex Colors

| Material Name | Hex Color | Roblox Material | Notes                                    |
|---------------|-----------|-----------------|------------------------------------------|
| Parrot_Body   | `#3CB34A` | SmoothPlastic   | Bright green — body, head                |
| Parrot_Wing   | `#C62828` | SmoothPlastic   | Red — wings, tail                        |
| Parrot_Beak   | `#F9A825` | SmoothPlastic   | Yellow — upper and lower beak            |
| Parrot_Eye    | `#1A1A1A` | SmoothPlastic   | Near-black — eyes                        |
| Parrot_Feet   | `#8B6914` | SmoothPlastic   | Dark brown — legs and feet               |

---

## Object List

| Object            | Description                              |
|-------------------|------------------------------------------|
| Parrot_Body       | Main body sphere                         |
| Parrot_Head       | Head sphere                              |
| Parrot_BeakUpper  | Upper beak (cone)                        |
| Parrot_BeakLower  | Lower beak (smaller cone)                |
| Parrot_EyeL       | Left eye                                 |
| Parrot_EyeR       | Right eye                                |
| Parrot_WingL      | Left wing — oval, wrapped against body   |
| Parrot_WingR      | Right wing — oval, wrapped against body  |
| Parrot_Tail       | Tapered tail cone, angled backward       |
| Parrot_LegL       | Left leg cylinder                        |
| Parrot_LegR       | Right leg cylinder                       |
| Parrot_FootL      | Left foot                                |
| Parrot_FootR      | Right foot                               |

**Total objects:** 13

---

## Layout Notes

- Bird faces **-Y direction** (beak points toward -Y).
- Feet sit at **Z=0** (ground level).
- Wings are oval spheres embedded into the body sides — both use `Parrot_Wing` red material.
- Tail is a 4-sided tapered cone angled backward and slightly downward from the rump.
- All parts scaled 2× from base build for Roblox prop proportions.

---

## Studio Import Notes

1. **FBX is ready to import** — no conversion steps needed.
2. **Scale** — import at 1.0. Each unit = 1 stud.
3. **Apply materials by object name prefix:**
   - `Parrot_Body`, `Parrot_Head` → `#3CB34A` SmoothPlastic
   - `Parrot_Wing*`, `Parrot_Tail` → `#C62828` SmoothPlastic
   - `Parrot_Beak*` → `#F9A825` SmoothPlastic
   - `Parrot_Eye*` → `#1A1A1A` SmoothPlastic
   - `Parrot_Leg*`, `Parrot_Foot*` → `#8B6914` SmoothPlastic
4. **Object count** — 13 objects. Consider merging by material in Studio for performance.
5. **Orientation** — bird faces -Z in Roblox Studio after FBX import with standard settings.

---

*Asset created by Tasha — Grotto Interactive LLC*  
*Spec written: 2026-05-09*
