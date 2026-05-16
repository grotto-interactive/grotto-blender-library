# SandDollar — Roblox Import Spec

**Asset:** Sand Dollar (seafloor decoration)
**File:** `SandDollar.fbx`
**Scale:** 1 unit = 1 Roblox stud
**Diameter:** ~2.4 studs
**Height:** ~0.31 studs (disc + dome)

---

## Materials

| Material | Hex | RGB (0–255) | Notes |
|---|---|---|---|
| SandDollar_BodyMat | `#E0D0A8` | 224, 208, 168 | Sandy beige — main disc body |
| SandDollar_PatternMat | `#C1AD8A` | 193, 173, 138 | Sandy tan — 5-petal flower pattern + center |
| SandDollar_HoleMat | `#6B5040` | 107, 80, 64 | Dark brown — 5 hole dots at petal tips |

---

## Object List (3 parts)

| Part | Material | Notes |
|---|---|---|
| SandDollar_BodyMat_disc | SandDollar_BodyMat | Flat domed disc, 24-sided, slightly domed top |
| SandDollar_PatternMat_petals | SandDollar_PatternMat | 5 radial oval petals + small center circle, raised above disc |
| SandDollar_HoleMat_holes | SandDollar_HoleMat | 5 small dark discs at the tip of each petal |

---

## Studio Setup Notes
- Set `Color` to hex values above per part
- Set `Material` to `SmoothPlastic` on all parts
- Set `CanCollide = false` on `SandDollar_PatternMat_petals` and `SandDollar_HoleMat_holes`
- Set `CastShadow = false` on petals and holes
- Lay flat on the seafloor (Z-up orientation)
- Scatter around sandy/rocky floor areas alongside Bubbles and other environment props
