# BrokenColumn — Roblox Import Spec

**Date:** 2026-05-14  
**Version:** Underwater / Barnacled  
**Prepared for:** Caleb  
**Game:** grotto-underground (Grotto Interactive Roblox Group)  
**FBX file:** `BrokenColumn.fbx`  
**Scale:** 1 Blender unit = 1 Roblox stud  
**Axis:** Forward -Z, Up Y

---

## Materials & Colors

| Material | Hex | Use |
|----------|-----|-----|
| Column_StoneMat | `#81796C` | All 16 ruin parts — weathered stone |
| Barnacle_Mat | `#C4BCAA` | All 89 barnacle objects — cream/off-white |

`SmoothPlastic` on everything. Two color passes total — multi-select all ruin parts for one, multi-select all `Barnacle_*` for the other.

---

## Object Inventory (105 parts total)

### Platform (2 parts)
| Object | Notes |
|--------|-------|
| `Platform_Step1` | Bottom step — widest, sits on ground |
| `Platform_Step2` | Top step — narrower, sits on Step1 |

> Can be Union-merged into one `Platform` part in Studio.

### Tall Column Stub (2 parts)
| Object | Notes |
|--------|-------|
| `ColumnStub_Tall_Base` | Octagonal plinth sitting on Step2 |
| `ColumnStub_Tall_Shaft` | Column shaft, jagged break at top — taller of the two |

### Short Column Stub (2 parts)
| Object | Notes |
|--------|-------|
| `ColumnStub_Short_Base` | Octagonal plinth sitting on Step2 |
| `ColumnStub_Short_Shaft` | Column shaft, heavier break — shorter stub |

### Fallen Pieces (2 parts)
| Object | Notes |
|--------|-------|
| `Beam_Fallen` | Architrave/lintel lying on ground at an angle, one end broken |
| `Column_Fallen` | Column drum lying on its side, slight roll tilt, jagged both ends |

### Rubble (8 parts)
| Objects | Notes |
|---------|-------|
| `Rubble_01` – `Rubble_08` | Irregular broken stone chunks scattered around the base |

### Barnacles (89 parts)
| Objects | Notes |
|---------|-------|
| `Barnacle_001` – `Barnacle_089` | Cream/off-white barnacle clusters |

Barnacles are surface-attached via raycasting — distributed across column shaft sides, platform tops, rubble, and fallen pieces. Multi-select all `Barnacle_*` in Studio and set `#C4BCAA` in one shot.

---

## Roblox Studio Setup

1. **Model:** Parent all 105 parts under one Model named `BrokenColumn`
2. **PrimaryPart:** `Platform_Step1`
3. **Stone color:** Multi-select all 16 ruin parts → `SmoothPlastic` → `#81796C`
4. **Barnacle color:** Multi-select all `Barnacle_*` → `SmoothPlastic` → `#C4BCAA`
5. **CanCollide:** True on `Platform_Step1`, `Platform_Step2`, both shaft objects. False on rubble, fallen pieces, and barnacles (all decorative)
6. **Anchored:** True on everything — static environment prop
7. **Optional unions to save part count:**
   - `Platform_Step1` + `Platform_Step2` → `Platform`
   - Each stub base + shaft → `ColumnStub_Tall`, `ColumnStub_Short`
   - All `Rubble_*` → `Rubble`
   - All `Barnacle_*` → `Barnacles` (biggest part count saving — 89 → 1)
