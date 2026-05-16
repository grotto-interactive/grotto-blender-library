# Grotto Treasure Chest — Roblox Import Specification

**Source file:** `grotto_chest.blend`  
**Prepared for:** Caleb  
**Updated:** 2026-05-14 — Underwater / Barnacled version  
**Game:** grotto-underground (Grotto Interactive Roblox Group)

---

## Export Settings

- **Format:** FBX
- **Scale:** 1 Blender unit = 1 stud
- **Axis:** Forward -Z, Up Y
- **Apply transforms:** Yes
- **Include:** Mesh only (no animation, no bones)

---

## Materials & Colors

All materials are solid color — no textures. Use `SmoothPlastic` throughout.

> **Note:** Colors have been updated to an underwater/weathered palette. The chest has been submerged — wood is dark and waterlogged, metal is corroded green, lock is tarnished bronze, barnacles are cream/off-white.

| Material | Hex | Use |
|----------|-----|-----|
| M_Wood | `#45351D` | Chest body and lid — dark waterlogged wood |
| M_Metal | `#425948` | Bands, corner reinforcements, lock hasp — corroded green metal |
| M_Gold | `#595538` | Padlock body and shackle — tarnished bronze |
| M_Dark | `#302719` | Keyhole detail — near-black encrusted |
| Barnacle_Mat | `#C4BCAA` | All 50 barnacle objects — cream/off-white |

---

## Object Inventory

### Chest Structure
| Object | Material | Notes |
|--------|----------|-------|
| Chest_Body | M_Wood | Main rectangular body |
| Chest_Lid | M_Wood | Barrel-arched lid (arch runs front-to-back in Y) |

### Metal Bands (3 bands, evenly spaced)
Each band split into 3 parts (front body strip, arch strip, back body strip).

| Object | Material |
|--------|----------|
| Band_0_Front / Band_0_Arch / Band_0_Back | M_Metal |
| Band_1_Front / Band_1_Arch / Band_1_Back | M_Metal |
| Band_2_Front / Band_2_Arch / Band_2_Back | M_Metal |

> Can be Union-merged per band in Studio (3 Band parts total).

### Corner Reinforcements (4 corners × 2 faces = 8 parts)

| Object | Material | Position |
|--------|----------|----------|
| Corner_FR_Y | M_Metal | Front face, right corner |
| Corner_FR_X | M_Metal | Right face, front corner |
| Corner_FL_Y | M_Metal | Front face, left corner |
| Corner_FL_X | M_Metal | Left face, front corner |
| Corner_BR_Y | M_Metal | Back face, right corner |
| Corner_BR_X | M_Metal | Right face, back corner |
| Corner_BL_Y | M_Metal | Back face, left corner |
| Corner_BL_X | M_Metal | Left face, back corner |

> Can be Union-merged per corner in Studio (4 Corner parts total).

### Lock & Keyhole
| Object | Material | Notes |
|--------|----------|-------|
| Lock_Hasp | M_Metal | Rectangular plate on front face at lid seam |
| Lock_Body | M_Gold | Padlock body |
| Lock_Shackle_L | M_Gold | Left arm of padlock shackle |
| Lock_Shackle_R | M_Gold | Right arm of padlock shackle |
| Lock_Shackle_Arch | M_Gold | Curved arch connecting shackle arms |
| Keyhole_Circle | M_Dark | Circle portion of keyhole |
| Keyhole_Slot | M_Dark | Tapered slot portion of keyhole |

> Can be Union-merged into a single `Padlock` part in Studio.

### Barnacles (50 objects)
| Objects | Material | Hex |
|---------|----------|-----|
| Barnacle_001 – Barnacle_050 | Barnacle_Mat | `#C4BCAA` |

- Barnacles are surface-attached, oriented to the face normals
- Distributed across lid top, front face, back face, left side, right side
- **Easiest approach:** multi-select all `Barnacle_*` parts in Studio and set Color once

---

## Roblox Studio Setup

1. **Model hierarchy:** Parent all parts under one Model named `GrottoChest`
2. **PrimaryPart:** `Chest_Body`
3. **Material:** `SmoothPlastic` for all parts — set `Color` to hex values above
4. **CanCollide:** True on `Chest_Body` and `Chest_Lid`. False on all decorative parts (bands, corners, lock, barnacles)
5. **Barnacles:** All 50 share the same color — multi-select and apply `#C4BCAA` at once
6. **Band merging:** Union each Band's 3 sub-parts — 3 Band parts total
7. **Corner merging:** Union each corner's 2 sub-parts — 4 Corner parts total
8. **Padlock:** Union all 7 lock/keyhole objects into one Padlock part
9. **Lid hinge:** Chest_Lid pivot is at the back edge (Y = +0.80, Z = 0.85). Set the hinge `CFrame` there for open animation.

---

## Approximate Dimensions

| Dimension | Studs |
|-----------|-------|
| Width (X) | ~2.4 |
| Depth (Y) | ~1.6 |
| Body height | ~0.85 |
| Total height (lid peak) | ~1.35 |
