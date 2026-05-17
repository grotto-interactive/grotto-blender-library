# Grotto Ship — Roblox Import Specification

**Source file:** `~/Desktop/grotto_ship.blend`  
**Prepared for:** Caleb  
**Date:** 2026-05-05  
**Game:** grotto-underground (Grotto Interactive Roblox Group)

---

## Export Settings

- **Format:** FBX
- **Scale:** Export at Blender scale (1 Blender unit = 1 stud in Roblox — confirm with Orange if rescaling is needed)
- **Triangulate:** Yes (apply Triangulate modifier or check "Triangulate Faces" on export)
- **Apply transforms:** Yes
- **Include:** Mesh + Materials (no armatures, no animations)

---

## Materials & Colors

All materials use solid colors (no textures). Map these to Roblox `SurfaceAppearance` or solid `Material = SmoothPlastic` with `Color` set to the hex below.

| Material | Hex | Use |
|----------|-----|-----|
| M_Hull | `#331607` | Dark brown — hull body, mast, yard, rails, cannon carriages |
| M_Deck | `#996B33` | Mid brown — deck planking |
| M_Sail | `#EDE0BF` | Off-white cream — main sail |
| M_Wheel | `#51260A` | Deep brown — ship's wheel |
| M_Metal | `#1E1E23` | Near-black dark grey — cannon barrels, portholes, anchor ring |
| M_Rope | `#8C724C` | Tan — rigging ropes |
| M_Flag | `#050505` | Near-black — flag body |
| M_SKWhite | `#F2F2E5` | Off-white — skull body, crossbones, teeth |
| M_SKDark | `#0A0A0A` | Near-black — skull eye sockets, nose, jaw |

> **Note:** Discard any `.001` / `.002` duplicates (M_Hull.001, M_Deck.001, etc.) — they are identical to the base material.

---

## Object Inventory

### Hull & Structure
| Object | Material | Notes |
|--------|----------|-------|
| Hull | M_Hull / M_Deck | Main hull body |
| Deck_Main | M_Deck | Main deck surface |
| Deck_Bow | M_Deck | Bow deck |
| Deck_Stern | M_Deck | Stern deck |
| Sterncastle | M_Hull | Raised rear castle |
| Mast | M_Hull | Center mast, Z=14 |
| Yard | M_Hull | Horizontal spar, Z=23 |
| CrowsNest | M_Hull | Crow's nest, Z=21 |
| Sail | M_Sail | Main sail |
| Anchor_Ring | M_Metal | Bow anchor ring |
| Stairs_Starboard | M_Hull / M_Deck | Starboard staircase |

### Cannons (Port = P, Starboard = S)
| Object | Material |
|--------|----------|
| Cannon_Barrel_P_0 / P_1 | M_Metal |
| Cannon_Barrel_S_0 / S_1 | M_Metal |
| Cannon_Carriage_P_0 / P_1 | M_Hull |
| Cannon_Carriage_S_0 / S_1 | M_Hull |
| Porthole_P_0 / P_1 | M_Metal |
| Porthole_S_0 / S_1 | M_Metal |

### Forecastle Rails & Posts (bow railing, 16 posts + 15 rails each side)
- `FC_Post00`–`FC_Post15` — M_Hull
- `FC_Rail00`–`FC_Rail14` — M_Hull
- `FC_SideGap_Port` / `FC_SideGap_Stbd` — M_Hull
- `FC_AftWall` / `SC_FwdWall` — M_Hull

### Sterncastle Railing (stern upper deck railing)
- `SC_PL0`–`SC_PL4`, `SC_PR0`–`SC_PR4` — M_Hull (port/starboard posts)
- `SC_RL0`–`SC_RL3`, `SC_RR0`–`SC_RR3` — M_Hull (port/starboard rails)
- `SC_PB0`–`SC_PB4` — M_Hull (back posts)
- `SC_RB0`–`SC_RB3` — M_Hull (back rails)

### Mid-Deck Railing
- `MD_PL0`–`MD_PL6`, `MD_PR0`–`MD_PR6` — M_Hull (posts)
- `MD_RL0`–`MD_RL5`, `MD_RR0`–`MD_RR5` — M_Hull (rails)

### Ship's Wheel
| Object | Material |
|--------|----------|
| Wheel_Hub | M_Wheel |
| Wheel_Post | M_Wheel |
| Wheel_Rim | M_Wheel |
| Wheel_Spoke0–7 | M_Wheel |

### Flag — Jolly Roger (Skull & Crossbones)
| Object | Material | Notes |
|--------|----------|-------|
| Flag_Main | M_Flag | Black flag body, billow curve |
| Flag_Skull_Port | M_SKWhite | Skull — port side face |
| Flag_Skull_Stbd | M_SKWhite | Skull — starboard side face |
| Flag_Bones_Port | M_SKWhite | Crossbones — port side (2 bone faces at ±45°) |
| Flag_Bones_Stbd | M_SKWhite | Crossbones — starboard side |
| Flag_SKDark_Port | M_SKDark | Eye sockets + nose + jaw — port side |
| Flag_SKDark_Stbd | M_SKDark | Eye sockets + nose + jaw — starboard side |
| Flag_Teeth_Port | M_SKWhite | 5 teeth — port side |
| Flag_Teeth_Stbd | M_SKWhite | 5 teeth — starboard side |

> **Flag note:** The flag geometry is double-sided (Port + Stbd objects) to be visible from both sides. In Roblox, set `BackSurface = SmoothNoOutlines` or disable backface culling on the flag parts so both faces render.

---

## Interior & Gameplay (R15)

Below-deck **cargo hold** and main **deck walk** volumes were added for avatar movement and item storage.

### New objects

| Object | Role |
|--------|------|
| `ship_CargoDeck_Floor` | Walkable cargo deck (use `CanCollide = true`) |
| `ship_CargoWall_*` | Inner bulkheads (port/stbd/bow/stern) |
| `ship_CargoDeck_Ceiling` | Deck underside visual |
| `ship_DeckHatch_Frame` | Hatch rim on `Deck_Main` |
| `ship_Ladder` | Ladder from hatch to hold |
| `ship_CargoShelf` / `_02` | Shelf ledges for crate placement |
| `Ref_Hatch` | Hatch entry point (spawn / teleport) |
| `Ref_CargoBounds` | Cargo hold volume center (~4.4 × 3.7 × 5.1 studs clear) |
| `Ref_DeckWalkBounds` | Open main-deck walk footprint |

### Clear dimensions (studs)

| Zone | Size (L × W × H) | Notes |
|------|------------------|-------|
| Cargo hold | ~4.4 × 3.7 × **5.1** | Floor z ≈ −3.85, ceiling z ≈ 1.22; R15 can stand |
| Main deck walk | ~6.2 × 4.7 | z ≈ 1.56; bow/stern decks extend further |
| Hatch opening | ~1.9 × 1.5 | Center ~(0.35, 0) on `Deck_Main` |

### Studio setup

1. Weld all `ship_*` interior parts to `GROTTO_grotto_ship` (or `GrottoShip` model).
2. **Cargo floor** `ship_CargoDeck_Floor` — primary walk collision below deck; snap crates to shelves or `Ref_CargoBounds`.
3. **Hull** `Hull_M_Hull` — if players cannot enter the hold, set `CanCollide = false` on the hull and rely on deck + inner walls, or add invisible exterior collision only.
4. **Hatch** — align spawn / `ProximityPrompt` to `Ref_Hatch`; ladder is visual; add `TrussPart` or `Part` ladder collision if needed.
5. **Storage** — parent loot crates to `ship_CargoShelf` attachments or grid inside `Ref_CargoBounds`.

Re-run interior builder: `Blender -b assets/props/grotto_ship/grotto_ship.blend --python scripts/build_grotto_ship_interior.py`

---

## Roblox Studio Import Notes

1. **Parent all parts under one Model** named `GrottoShip`.
2. **PrimaryPart** → Hull (the main collision/anchor part).
3. **Naming:** Keep the object names from Blender — they match the design intent and will be referenced by scripts.
4. **Materials:** Use `SmoothPlastic` for hull/deck/wheel, `Metal` or `SmoothPlastic` for cannons/metal parts, `Neon` is not needed. Set `Color` to the hex values in the table above.
5. **Flag parts:** Group all `Flag_*` objects under a sub-Model named `Flag`. The flag is decorative — no collision needed (`CanCollide = false`).
6. **Cannons:** Each `Cannon_Barrel` + `Cannon_Carriage` pair is one cannon unit. Group as `Cannon_P0`, `Cannon_P1`, `Cannon_S0`, `Cannon_S1`.
7. **Scale check:** Ship hull is ~17 studs long × 12 studs wide × 27 studs tall from keel to flag top. Adjust scale in Studio if needed for gameplay feel.

---

## Unused / Legacy Materials (safe to ignore)
These were from earlier design iterations and are not assigned to any current geometry:
- M_FlagBase, M_FlagEye, M_FlagEyeWhite, M_FlagOctopus, M_FlagPupil
