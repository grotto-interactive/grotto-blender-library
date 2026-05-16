# Grotto Crate Pile of 5 — Roblox Spec Doc

**Asset:** grotto_crate_pile_of_5  
**Category:** Props  
**File:** `grotto_crate_pile_of_5.blend` / `grotto_crate_pile_of_5.fbx`  
**Scale:** 1 Blender unit = 1 Roblox stud  
**Overall Dimensions:** ~16 W × 6 D × 5.56 H studs  
**Intended use:** Environmental scatter prop — dock, warehouse, Seed Harbor

---

## Materials & Hex Colors

| Material Name | Hex Color | Roblox Material | Notes                                 |
|---------------|-----------|-----------------|---------------------------------------|
| Crate_Wood    | `#B87F47` | SmoothPlastic   | Warm tan wood — all crate bodies      |
| Crate_Strap   | `#472E1A` | SmoothPlastic   | Dark brown — all frame & strap pieces |

---

## Arrangement

Five crates duplicated from `grotto_crate-basic`. Three form a stacked pile; two sit to the side.

### Stacked Pile (Crates 1–3)

| Crate   | Position                                          | Rotation |
|---------|---------------------------------------------------|----------|
| Crate 1 | Bottom left, -2.5 X / 0 Y / 0 Z                  | 0°       |
| Crate 2 | Bottom right, +0.9 X / +0.5 Y / 0 Z              | 0°       |
| Crate 3 | On top, centered at -0.8 X / +0.25 Y / +2.78 Z   | 14° Z    |

Each crate is 3 × 3 × 2.78 studs. The two bottom crates have a small visible gap so they read as individual crates. The top crate rests at Z = 2.78, rotated 14° for a natural placed look.

### Solo Crate (Crate 4)

| Crate   | Position                | Rotation |
|---------|-------------------------|----------|
| Crate 4 | ~8.0 X / -0.5 Y / 0 Z  | 28° Z    |

Placed off to the side of the main pile at 28° — reads as a crate set down separately.

### Leaning Crate (Crate 5)

| Crate   | Position                        | Rotation                              |
|---------|---------------------------------|---------------------------------------|
| Crate 5 | ~10.78 X / -2.59 Y / 0.87 Z    | -25.3° X, 9.1° Y, -156.3° Z          |

Leaning with its back corner just grazing the front face of Crate 4. The crate is tilted ~25° with a slight side lean so only the corner tip contacts Crate 4. Z offset (0.87) accounts for the lean geometry. Parts import with all transforms baked — no manual adjustment needed in Studio.

---

## Studio Import Notes

1. **FBX is ready to import** — no conversion steps needed.
2. **Scale** — import at 1.0. Each unit = 1 stud.
3. **Both materials are SmoothPlastic** — apply `#B87F47` to all `Crate_Wood` objects, `#472E1A` to all strap/frame/post/band objects.
4. **Crate 5 lean** — Crate 5 is tilted ~25° with a slight side lean, corner just touching Crate 4. All transforms are baked into the FBX; no manual rotation needed in Studio.
5. **Object count** — 5 full crates × ~21 objects each = ~105 objects. Consider merging by material in Studio if performance is a concern.

---

*Asset created by Tasha — Grotto Interactive LLC*  
*Spec written: 2026-05-09 — Updated: 2026-05-09*
