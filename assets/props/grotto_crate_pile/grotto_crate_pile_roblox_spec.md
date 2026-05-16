# Grotto Crate Pile — Roblox Spec Doc

**Asset:** grotto_crate_pile  
**Category:** Props  
**File:** `grotto_crate_pile.blend` / `grotto_crate_pile.fbx`  
**Scale:** 1 Blender unit = 1 Roblox stud  
**Overall Dimensions:** ~6.1 W × 3.7 D × 5.4 H studs  
**Intended use:** Environmental scatter prop — dock, warehouse, Seed Harbor

---

## Materials & Hex Colors

| Material Name | Hex Color | Roblox Material | Notes                                 |
|---------------|-----------|-----------------|---------------------------------------|
| Crate_Wood    | `#B87F47` | SmoothPlastic   | Warm tan wood — all crate bodies      |
| Crate_Strap   | `#472E1A` | SmoothPlastic   | Dark brown — all frame & strap pieces |

---

## Arrangement

Three crates duplicated from `grotto_crate-basic`:

| Crate      | Position                        | Rotation |
|------------|---------------------------------|----------|
| Crate 1    | Bottom left, at origin          | 0°       |
| Crate 2    | Bottom right, +3.1 X / +0.5 Y  | 0°       |
| Crate 3    | On top of both, centered        | 14° Z    |

Each individual crate is 3 × 3 × 2.78 studs.  
Top crate sits at Z = 2.78 (resting on the two bottom crates), rotated 14° for a natural placed look.

---

## Studio Import Notes

1. **FBX is ready to import** — no conversion steps needed.
2. **Scale** — import at 1.0. Each unit = 1 stud.
3. **Both materials are SmoothPlastic** — apply `#B87F47` to all `Crate_Wood` objects, `#472E1A` to all strap/frame/post/band objects.
4. **Object count is high** — this is a composed prop (3 full crates × ~17 objects each = ~51 objects). Consider merging by material in Studio if performance is a concern.

---

*Asset created by Tasha — Grotto Interactive LLC*  
*Spec written: 2026-05-09*
