# Grotto Crate (Basic) — Roblox Spec Doc

**Asset:** grotto_crate-basic  
**Category:** Props  
**File:** `grotto_crate-basic.blend` / `grotto_crate-basic.fbx`  
**Scale:** 1 Blender unit = 1 Roblox stud  
**Overall Dimensions:** 3 × 3 × 2.78 studs (W × D × H, including top/bottom frame)  
**Intended use:** Stackable scatter prop — Seed Harbor and general Grotto Underground environments

---

## Materials & Hex Colors

| Material Name | Hex Color | Roblox Material | Notes                                 |
|---------------|-----------|-----------------|---------------------------------------|
| Crate_Wood    | `#B87F47` | SmoothPlastic   | Warm tan wood — main crate body       |
| Crate_Strap   | `#472E1A` | SmoothPlastic   | Dark brown — all frame & strap pieces |

---

## Object List by Material

### Crate_Wood (`#B87F47`)
- `Crate_Wood` — main box body (3 × 3 × 2.5 studs)

### Crate_Strap (`#472E1A`)
- `Crate_CornerPost_0` through `Crate_CornerPost_3` — 4 vertical corner posts (full height)
- `Crate_Band` × 8 — horizontal strap bands on all 4 faces, 2 levels
- `Crate_TopFrame` × 4 — border frame rails on top face
- `Crate_BotFrame` × 4 — border frame rails on bottom face

---

## Studio Import Notes

1. **FBX is ready to import** — no conversion steps needed.
2. **Scale** — import at 1.0. Each unit = 1 stud.
3. **Both materials are SmoothPlastic** — apply `#B87F47` to `Crate_Wood` and `#472E1A` to all strap/frame/post/band objects.
4. **Stacking** — bottom sits at Y = 0. Offset 2.78 studs vertically to stack.

---

*Asset created by Tasha — Grotto Interactive LLC*  
*Spec written: 2026-05-09*
