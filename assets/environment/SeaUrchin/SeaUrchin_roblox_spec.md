# SeaUrchin — Roblox Import Spec

**Date:** 2026-05-14  
**Version:** Underwater Environment Prop  
**Prepared for:** Caleb  
**Game:** grotto-underground (Grotto Interactive Roblox Group)  
**FBX file:** `SeaUrchin.fbx`  
**Scale:** 1 Blender unit = 1 Roblox stud  
**Axis:** Forward -Z, Up Y

---

## Materials & Colors

| Material | Hex | Use |
|----------|-----|-----|
| SeaUrchin_TestMat  | `#3A2B1E` | Test body — dark brownish-purple shell |
| SeaUrchin_SpineMat | `#C8BFB0` | All spines — warm cream/off-white |
| SeaUrchin_MouthMat | `#1E1410` | Mouth disc — near-black underside |

`SmoothPlastic` on everything. Three color passes — one per part.

---

## Object Inventory (3 parts total)

| Object | Material | Notes |
|--------|----------|-------|
| `SeaUrchin_Test` | TestMat | Slightly flattened sphere body (test), faint 5-fold radial bumps on surface |
| `SeaUrchin_Spines` | SpineMat | 160 spines joined into one mesh — radiate from top and sides, none on underside |
| `SeaUrchin_Mouth` | MouthMat | Small dark disc on underside (oral surface / peristome) |

Spines cover the upper hemisphere and sides only. The lower dome is bare. Spine lengths vary organically between ~0.85 and ~1.55 studs with subtle angle wobble.

---

## Roblox Studio Setup

1. **Model:** Parent all 3 parts under one Model named `SeaUrchin`
2. **PrimaryPart:** `SeaUrchin_Test`
3. **Body color:** Select `Test` → `SmoothPlastic` → `#3A2B1E`
4. **Spine color:** Select `Spines` → `SmoothPlastic` → `#C8BFB0`
5. **Mouth color:** Select `Mouth` → `SmoothPlastic` → `#1E1410`
6. **CanCollide:** True on `Test`. False on `Spines` and `Mouth` (decorative)
7. **Anchored:** True on everything — static environment prop

---

## Approximate Dimensions

| Dimension | Studs |
|-----------|-------|
| Body width (equatorial) | ~3.0 |
| Body height (flattened) | ~2.5 |
| Total diameter with spines | ~6.1 |
| Spine length range | ~0.85 – 1.55 |
| Mouth disc diameter | ~0.88 |
