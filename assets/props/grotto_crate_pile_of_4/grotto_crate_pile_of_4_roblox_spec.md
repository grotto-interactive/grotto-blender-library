# Grotto Crate Pile of 4 — Roblox Spec Doc

**Asset:** grotto_crate_pile_of_4  
**Category:** Props  
**File:** `grotto_crate_pile_of_4.blend` / `grotto_crate_pile_of_4.fbx`  
**Scale:** 1 Blender unit = 1 Roblox stud  
**Overall Dimensions:** ~11.2 W × 3.5 D × 5.56 H studs  
**Intended use:** Environmental scatter prop — dock, warehouse, Seed Harbor

---

## Materials & Hex Colors

| Material Name | Hex Color | Roblox Material | Notes                                 |
|---------------|-----------|-----------------|---------------------------------------|
| Crate_Wood    | `#B87F47` | SmoothPlastic   | Warm tan wood — all crate bodies      |
| Crate_Strap   | `#472E1A` | SmoothPlastic   | Dark brown — all frame & strap pieces |

---

## Arrangement

Four crates duplicated from `grotto_crate-basic`. Three form a stacked pile; one sits solo to the side.

### Stacked Pile (Crates 1–3)

| Crate   | Position                          | Rotation |
|---------|-----------------------------------|----------|
| Crate 1 | Bottom left, at origin            | 0°       |
| Crate 2 | Bottom right, +3.4 X / +0.5 Y    | 0°       |
| Crate 3 | On top, centered at +1.7 X / +0.25 Y / +2.78 Z | 14° Z |

Each crate is 3 × 3 × 2.78 studs. The two bottom crates have a small visible gap between them so they read as individual crates. The top crate rests at Z = 2.78, rotated 14° for a natural placed look.

### Solo Crate (Crate 4)

| Crate   | Position                | Rotation |
|---------|-------------------------|----------|
| Crate 4 | ~8.3 X / -0.5 Y / 0 Z  | 28° Z    |

Placed off to the side of the main pile, angled 28° — reads as a crate that's been set down separately.

---

## Studio Import Notes

1. **FBX is ready to import** — no conversion steps needed.
2. **Scale** — import at 1.0. Each unit = 1 stud.
3. **Both materials are SmoothPlastic** — apply `#B87F47` to all `Crate_Wood` objects, `#472E1A` to all strap/frame/post/band objects.
4. **Object count** — 4 full crates × ~21 objects each = ~84 objects. Consider merging by material in Studio if performance is a concern.

---

*Asset created by Tasha — Grotto Interactive LLC*  
*Spec written: 2026-05-09*
