# OpenClam — Roblox Import Spec

**Date:** 2026-05-14  
**Version:** Underwater Environment Prop  
**Prepared for:** Caleb  
**Game:** grotto-underground (Grotto Interactive Roblox Group)  
**FBX file:** `OpenClam.fbx`  
**Scale:** 1 Blender unit = 1 Roblox stud  
**Axis:** Forward -Z, Up Y

---

## Materials & Colors

| Material | Hex | Use |
|----------|-----|-----|
| OpenClam_ShellMat | `#C8B89A` | All 3 parts — weathered cream/tan shell |

`SmoothPlastic` on everything. Single color pass — multi-select all 3 parts.

---

## Object Inventory (3 parts total)

| Object | Material | Notes |
|--------|----------|-------|
| `OpenClam_ShellTop` | ShellMat | Upper valve — gently domed with radial ribs, hinge end raised ~12° |
| `OpenClam_ShellBottom` | ShellMat | Lower valve — flat base resting on seafloor |
| `OpenClam_HingeRidge` | ShellMat | Small elongated bump at the hinge (rear center) |

Shell is slightly open at the narrow hinge end (rear). The wide lip (front) stays closed. Top shell rotation is baked into the mesh — no object-level transform needed in Studio.

---

## Roblox Studio Setup

1. **Model:** Parent all 3 parts under one Model named `OpenClam`
2. **PrimaryPart:** `OpenClam_ShellBottom`
3. **Shell color:** Multi-select all 3 parts → `SmoothPlastic` → `#C8B89A`
4. **CanCollide:** True on `ShellTop` and `ShellBottom`. False on `HingeRidge` (decorative)
5. **Anchored:** True on everything — static environment prop

---

## Approximate Dimensions

| Dimension | Studs |
|-----------|-------|
| Total width (left to right) | ~11.0 |
| Depth (hinge to lip) | ~4.0 |
| Upper dome height (center) | ~2.5 |
| Hinge end gap (top to bottom) | ~0.8 |
| Total height at hinge | ~1.8 |
