# Grotto Crate Pile of 2 — Roblox Spec Doc

**Asset:** grotto_crate_pile_of_2  
**Category:** Props  
**File:** `grotto_crate_pile_of_2.blend` / `grotto_crate_pile_of_2.fbx`  
**Scale:** 1 Blender unit = 1 Roblox stud  
**Overall Dimensions:** ~6 W × 5 D × 2.78 H studs  
**Intended use:** Environmental scatter prop — dock, warehouse, Seed Harbor

---

## Materials & Hex Colors

| Material Name | Hex Color | Roblox Material | Notes                                 |
|---------------|-----------|-----------------|---------------------------------------|
| Crate_Wood    | `#B87F47` | SmoothPlastic   | Warm tan wood — all crate bodies      |
| Crate_Strap   | `#472E1A` | SmoothPlastic   | Dark brown — all frame & strap pieces |

---

## Arrangement

Two crates — one upright, one leaning with its corner resting against the upright crate.

### Upright Crate (Crate 4)

| Crate   | Position               | Rotation |
|---------|------------------------|----------|
| Crate 4 | 8.0 X / -0.5 Y / 0 Z  | 28° Z    |

Sits flat on the ground, rotated 28° for a natural placed look.

### Leaning Crate (Crate 5)

| Crate   | Position                     | Rotation                     |
|---------|------------------------------|------------------------------|
| Crate 5 | ~10.78 X / -2.59 Y / 0.87 Z | -25.3° X, 9.1° Y, -156.3° Z |

Leaning with its back corner just grazing the front face of Crate 4. Tilted ~25° with a slight side lean so only the corner tip contacts Crate 4. Z offset (0.87) accounts for the lean geometry. All transforms are baked — no manual adjustment needed in Studio.

---

## Studio Import Notes

1. **FBX is ready to import** — no conversion steps needed.
2. **Scale** — import at 1.0. Each unit = 1 stud.
3. **Both materials are SmoothPlastic** — apply `#B87F47` to all `Crate_Wood` objects, `#472E1A` to all strap/frame/post/band objects.
4. **Crate 5 lean** — tilted ~25° with corner resting on Crate 4. All transforms baked into FBX; no manual rotation needed in Studio.
5. **Object count** — 2 crates × 21 objects each = 42 objects. Consider merging by material in Studio if performance is a concern.

---

*Asset created by Tasha — Grotto Interactive LLC*  
*Spec written: 2026-05-09*
