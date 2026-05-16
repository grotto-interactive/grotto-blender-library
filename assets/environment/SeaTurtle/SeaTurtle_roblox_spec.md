# SeaTurtle — Roblox Import Spec

**Date:** 2026-05-14  
**Version:** Underwater Environment Prop  
**Prepared for:** Caleb  
**Game:** grotto-underground (Grotto Interactive Roblox Group)  
**FBX file:** `SeaTurtle.fbx`  
**Scale:** 1 Blender unit = 1 Roblox stud  
**Axis:** Forward -Z, Up Y

---

## Materials & Colors

| Material | Hex | Use |
|----------|-----|-----|
| SeaTurtle_ShellMat | `#495C3A` | Carapace — dark olive green |
| SeaTurtle_BellyMat | `#C8B76F` | Plastron — warm cream/gold |
| SeaTurtle_SkinMat | `#3D6B49` | Head, neck, tail, all 4 flippers — sea green |
| SeaTurtle_EyeWhiteMat | `#E7DFCC` | Eye whites (×2) — off-white |
| SeaTurtle_PupilMat | `#191108` | Pupils (×2) — near-black |

`SmoothPlastic` on everything. Five color passes total — multi-select by material group.

---

## Object Inventory (13 parts total)

### Shell (2 parts)
| Object | Material | Notes |
|--------|----------|-------|
| `SeaTurtle_Carapace` | ShellMat | Domed low-poly shell top |
| `SeaTurtle_Plastron` | BellyMat | Flat oval belly plate |

### Body (3 parts)
| Object | Material | Notes |
|--------|----------|-------|
| `SeaTurtle_Head` | SkinMat | Rounded oblong head, faces -Y |
| `SeaTurtle_Neck` | SkinMat | Short tapered cylinder connecting head to shell |
| `SeaTurtle_Tail` | SkinMat | Small stubby cone at rear |

### Flippers (4 parts)
| Object | Material | Notes |
|--------|----------|-------|
| `SeaTurtle_Flipper_FR` | SkinMat | Front right — wide half-dome paddle |
| `SeaTurtle_Flipper_FL` | SkinMat | Front left — wide half-dome paddle |
| `SeaTurtle_Flipper_RR` | SkinMat | Rear right — shorter paddle |
| `SeaTurtle_Flipper_RL` | SkinMat | Rear left — shorter paddle |

### Eyes (4 parts)
| Object | Material | Notes |
|--------|----------|-------|
| `SeaTurtle_Eye_R` | EyeWhiteMat | Right eye white — set into head surface |
| `SeaTurtle_Eye_L` | EyeWhiteMat | Left eye white — set into head surface |
| `SeaTurtle_Pupil_R` | PupilMat | Right pupil — sits on outer face of Eye_R |
| `SeaTurtle_Pupil_L` | PupilMat | Left pupil — sits on outer face of Eye_L |

---

## Roblox Studio Setup

1. **Model:** Parent all 13 parts under one Model named `SeaTurtle`
2. **PrimaryPart:** `SeaTurtle_Carapace`
3. **Shell color:** `SeaTurtle_Carapace` → `SmoothPlastic` → `#495C3A`
4. **Belly color:** `SeaTurtle_Plastron` → `SmoothPlastic` → `#C8B76F`
5. **Skin color:** Multi-select Head, Neck, Tail, all 4 Flippers → `SmoothPlastic` → `#3D6B49`
6. **Eye whites:** Multi-select Eye_R + Eye_L → `SmoothPlastic` → `#E7DFCC`
7. **Pupils:** Multi-select Pupil_R + Pupil_L → `SmoothPlastic` → `#191108`
8. **CanCollide:** True on `Carapace` and `Plastron`. False on all other parts (decorative)
9. **Anchored:** True on everything — static environment prop
10. **Optional unions:** Head + Neck → `TurtleHead`; Flipper pairs can stay separate for future animation

---

## Approximate Dimensions

| Dimension | Studs |
|-----------|-------|
| Total length (head to tail) | ~4.8 |
| Shell length | ~2.9 |
| Shell width | ~2.1 |
| Shell dome height | ~0.8 |
| Flipper span (tip to tip) | ~3.1 |
