# SunkenAnchor — Roblox Import Spec

**Date:** 2026-05-14  
**Version:** Underwater / Barnacled  
**Prepared for:** Caleb  
**Game:** grotto-underground (Grotto Interactive Roblox Group)  
**FBX file:** `SunkenAnchor.fbx`  
**Scale:** 1 Blender unit = 1 Roblox stud  
**Axis:** Forward -Z, Up Y

---

## Materials & Colors

| Material | Hex | Use |
|----------|-----|-----|
| Anchor_IronMat | `#383026` | All 8 anchor parts — dark corroded iron |
| Barnacle_Mat | `#C4BCAA` | All 100 barnacle objects — cream/off-white |

`SmoothPlastic` on everything. Two color passes total — multi-select all 8 anchor parts for one, multi-select all `Barnacle_*` for the other.

---

## Object Inventory (108 parts total)

### Anchor Structure (8 parts)

| Object | Notes |
|--------|-------|
| `Anchor_Shank` | Main vertical shaft |
| `Anchor_Ring` | Circular ring at the top of the shank |
| `Anchor_Stock` | Horizontal bar crossing the shank near the top |
| `Anchor_Crown` | Junction block at the base of the shank |
| `Anchor_Arm_L` | Left arm extending diagonally down from crown |
| `Anchor_Arm_R` | Right arm extending diagonally down from crown |
| `Anchor_Fluke_L` | Left fluke (flat blade) at the tip of the left arm |
| `Anchor_Fluke_R` | Right fluke (flat blade) at the tip of the right arm |

### Barnacles (100 parts)

| Objects | Notes |
|---------|-------|
| `Barnacle_001` – `Barnacle_100` | Cream/off-white barnacle clusters |

Barnacles are surface-attached, distributed across the full shank (top to bottom), stock, crown, arms, and flukes. Multi-select all `Barnacle_*` in Studio and set `#C4BCAA` in one shot.

---

## Roblox Studio Setup

1. **Model:** Parent all 108 parts under one Model named `SunkenAnchor`
2. **PrimaryPart:** `Anchor_Shank`
3. **Iron color:** Multi-select all 8 anchor parts → `SmoothPlastic` → `#383026`
4. **Barnacle color:** Multi-select all `Barnacle_*` → `SmoothPlastic` → `#C4BCAA`
5. **CanCollide:** True on `Anchor_Shank`, `Anchor_Crown`, `Anchor_Arm_L`, `Anchor_Arm_R`. False on `Anchor_Ring`, `Anchor_Stock`, flukes, and all barnacles (decorative)
6. **Anchored:** True on everything — static environment prop
7. **Optional unions to save part count:**
   - `Anchor_Arm_L` + `Anchor_Fluke_L` → `AnchorArm_L`
   - `Anchor_Arm_R` + `Anchor_Fluke_R` → `AnchorArm_R`
   - All `Barnacle_*` → `Barnacles` (100 → 1)

---

## Approximate Dimensions

| Dimension | Studs |
|-----------|-------|
| Height (shank + ring) | ~5.0 |
| Width (arm span) | ~3.2 |
| Stock width | ~3.0 |
| Fluke depth | ~0.5 |
