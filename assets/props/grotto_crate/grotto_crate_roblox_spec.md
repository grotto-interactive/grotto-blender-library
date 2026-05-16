# Grotto Crate — Roblox Spec Doc

**Asset:** grotto_crate  
**Category:** Props  
**File:** `grotto_crate.blend`  
**Scale:** 1 Blender unit = 1 Roblox stud  
**Overall Dimensions:** 3 × 3 × 2.78 studs (W × D × H, including top/bottom frame)  
**Intended use:** Stackable scatter prop — Seed Harbor and general Grotto Underground environments

---

## Materials & Hex Colors

Apply these as solid colors in Roblox Studio. No textures needed — solid flat materials only.

| Material Name   | Hex Color | Roblox Material | Notes                              |
|-----------------|-----------|-----------------|-------------------------------------|
| Crate_Wood      | `#B87F47` | SmoothPlastic   | Warm tan wood — main crate body    |
| Crate_Strap     | `#472E1A` | SmoothPlastic   | Dark brown — all frame/strap pieces |
| Crate_Stamp     | `#2E1A0A` | SmoothPlastic   | Near-black brown — GROTTO logos    |
| Crate_Rivet     | `#403B33` | Metal           | Dark iron — rivets (Metallic material, use Roblox "Metal" type) |

---

## Object List by Material

### Crate_Wood (`#B87F47`)
- `Crate_Wood` — main box body (3 × 3 × 2.5 studs)

### Crate_Strap (`#472E1A`)
- `Crate_CornerPost_0` through `Crate_CornerPost_3` — 4 vertical corner posts (run full height)
- `Crate_Band` × 8 — horizontal strap bands on all 4 faces, 2 levels (near top and near bottom)
- `Crate_TopFrame` × 4 — border frame rails on top face
- `Crate_BotFrame` × 4 — border frame rails on bottom face

### Crate_Stamp (`#2E1A0A`)
- `Crate_Logo` — "GROTTO" stamp on front face (slight diagonal, Copperplate font, raised)
- `Crate_Logo_Top` — "GROTTO" stamp on top face (same angle, same style)

### Crate_Rivet (`#403B33` + Metal)
- `Crate_Rivet_00` through `Crate_Rivet_15` — 16 rivets total, 2 per band segment on each face at both levels

---

## Studio Import Notes

1. **Convert text to mesh before FBX export** — In Blender, select `Crate_Logo` and `Crate_Logo_Top`, then Object → Convert → Mesh. Do this on a copy if you want to keep the editable text in the .blend.

2. **Hide reference collections before export** — In the Outliner, hide `!! R15 Reference (hide before export)` and `!! Scale Reference (hide before export)` before exporting FBX.

3. **FBX export settings:**
   - Scale: 1.0
   - Apply Transform: ✓
   - Export only "Your Asset" collection

4. **Rivets** — Use Roblox **Metal** material type for `Crate_Rivet` pieces to get the metallic sheen. All other pieces use **SmoothPlastic**.

5. **Stamped logos** — The GROTTO logos are raised geometry (not decals). Apply `#2E1A0A` as a solid SmoothPlastic color. They sit slightly proud of the wood face.

6. **Stacking** — Crate bottom sits at Y = 0 (ground level). Stack multiples by offsetting 2.78 studs in the vertical axis.

---

*Asset created by Tasha — Grotto Interactive LLC*  
*Spec written: 2026-05-09*
