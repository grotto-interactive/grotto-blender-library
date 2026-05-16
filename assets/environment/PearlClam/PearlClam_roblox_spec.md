# PearlClam — Roblox Import Spec

**Date:** 2026-05-14  
**Version:** Underwater Environment Prop  
**Prepared for:** Caleb  
**Game:** grotto-underground (Grotto Interactive Roblox Group)  
**FBX file:** `PearlClam.fbx`  
**Scale:** 1 Blender unit = 1 Roblox stud  
**Axis:** Forward -Z, Up Y

---

## Materials & Colors

| Material | Hex | Use |
|----------|-----|-----|
| PearlClam_ShellMat | `#C8B89A` | Shell parts — weathered cream/tan |
| PearlClam_PearlMat | `#F0ECE4` | Pearl — warm lustrous white |

`SmoothPlastic` on everything. Two color passes — multi-select the 3 shell parts for one, Pearl alone for the other.

---

## Object Inventory (4 parts total)

| Object | Material | Notes |
|--------|----------|-------|
| `PearlClam_ShellTop` | ShellMat | Upper valve — domed with radial ribs and growth rings, hinge end raised ~12°, ~0.45 stud wall thickness |
| `PearlClam_ShellBottom` | ShellMat | Lower valve — flat base resting on seafloor, matching wall thickness |
| `PearlClam_HingeRidge` | ShellMat | Small elongated bump at the hinge (rear center) |
| `PearlClam_Pearl` | PearlMat | Sphere (~0.95 studs diameter) nestled inside at the hinge opening |

Shell opens at the narrow hinge end (rear). The wide lip (front) stays closed. Interior wall thickness is ~0.45 studs — visible as a substantial rim through the opening. All transforms baked — no object-level adjustments needed in Studio.

---

## Roblox Studio Setup

1. **Model:** Parent all 4 parts under one Model named `PearlClam`
2. **PrimaryPart:** `PearlClam_ShellBottom`
3. **Shell color:** Multi-select `ShellTop`, `ShellBottom`, `HingeRidge` → `SmoothPlastic` → `#C8B89A`
4. **Pearl color:** Select `Pearl` → `SmoothPlastic` → `#F0ECE4`
5. **CanCollide:** True on `ShellTop` and `ShellBottom`. False on `HingeRidge` and `Pearl` (decorative)
6. **Anchored:** True on everything — static environment prop

---

## Approximate Dimensions

| Dimension | Studs |
|-----------|-------|
| Total width (left to right) | ~11.0 |
| Depth (hinge to lip) | ~4.0 |
| Total height (top shell peak) | ~2.5 |
| Wall thickness (center) | ~0.45 |
| Hinge end gap | ~0.8 |
| Pearl diameter | ~0.95 |
