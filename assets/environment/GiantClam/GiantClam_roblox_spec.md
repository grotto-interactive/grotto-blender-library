# GiantClam — Roblox Import Spec

**Date:** 2026-05-14  
**Version:** Underwater Environment Prop  
**Prepared for:** Caleb  
**Game:** grotto-underground (Grotto Interactive Roblox Group)  
**FBX file:** `GiantClam.fbx`  
**Scale:** 1 Blender unit = 1 Roblox stud  
**Axis:** Forward -Z, Up Y

---

## Materials & Colors

| Material | Hex | Use |
|----------|-----|-----|
| GiantClam_ShellMat | `#C8B89A` | All 3 parts — weathered cream/tan shell |

`SmoothPlastic` on everything. Single color pass — multi-select all 3 parts.

---

## Object Inventory (3 parts total)

| Object | Material | Notes |
|--------|----------|-------|
| `GiantClam_ShellTop` | ShellMat | Upper valve — gently domed, radial ribs and growth rings on exterior |
| `GiantClam_ShellBottom` | ShellMat | Lower valve — flatter base, rests on seafloor |
| `GiantClam_HingeRidge` | ShellMat | Small elongated bump at the hinge (rear center) |

Shell is closed — both valves meet at the lateral edges and lip with a natural seam. Hinge is at the back (+Y), lip opening faces forward (-Y).

---

## Roblox Studio Setup

1. **Model:** Parent all 3 parts under one Model named `GiantClam`
2. **PrimaryPart:** `GiantClam_ShellBottom`
3. **Shell color:** Multi-select all 3 parts → `SmoothPlastic` → `#C8B89A`
4. **CanCollide:** True on `ShellTop` and `ShellBottom`. False on `HingeRidge` (decorative)
5. **Anchored:** True on everything — static environment prop

---

## Approximate Dimensions

| Dimension | Studs |
|-----------|-------|
| Total width (left to right) | ~11.0 |
| Depth (hinge to lip) | ~4.0 |
| Upper dome height (above seam) | ~2.1 |
| Lower depth (below seam) | ~0.7 |
| Total height (top to bottom) | ~2.8 |
