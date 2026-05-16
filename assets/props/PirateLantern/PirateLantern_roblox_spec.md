# PirateLantern — Roblox Import Spec

**Asset:** PirateLantern  
**Created by:** Tasha (Grotto Interactive)  
**Date:** 2026-05-06  
**For:** Caleb — Roblox Studio import

---

## Files

| File | Location |
|------|----------|
| `PirateLantern.blend` | `props/PirateLantern/` |
| `PirateLantern.fbx` | `props/PirateLantern/` — import this one |

---

## Object Inventory

| Object | Type | Notes |
|--------|------|-------|
| `PirateLantern` | Single mesh | Static prop, no rig |

- **Verts:** 94  
- **Tris:** 77  
- Clean mesh — static asset, no rigging or animations

---

## Dimensions

Exported at 0.01 scale (1 Blender unit = 1 Roblox stud).

| Axis | Size |
|------|------|
| Width (X) | ~0.8 studs |
| Depth (Y) | ~0.8 studs |
| Height (Z) | ~2.1 studs (including handle) |

> A standard R15 character is ~5 studs tall. This lantern is roughly held-in-hand scale — scale up in Studio as needed.

---

## Materials

| Material Name | Hex Color | Roughness | Metallic | Used On |
|---------------|-----------|-----------|---------|---------|
| `PirateLanternMetal` | `#3A3018` | 0.88 | 0.70 | Frame, corner posts, top/bottom plates, handle |
| `PirateLanternGlass` | `#FF9520` | 0.10 | 0.00 | 4 glass panels (body) |
| `PirateLanternFlame` | `#FF4500` | 0.30 | 0.00 | Inner flame cone |

> Blender node materials do not import directly into Roblox. Recreate as `SurfaceAppearance` or plain `Color` properties using the hex values above. For the glass panels, consider using a semi-transparent `SurfaceAppearance` with the amber color for a glowing effect.

---

## FBX Export Settings Used

| Setting | Value |
|---------|-------|
| Format | FBX Binary |
| Scale | 0.01 (centimeters) |
| Forward Axis | -Z |
| Up Axis | Y |
| Triangulated | Yes |
| Transforms Applied | Yes |
| Leaf Bones | None |

---

## Studio Setup Notes

1. Import `PirateLantern.fbx` via **File → Import → Import 3D Model**
2. The mesh will arrive as a single `MeshPart` named `PirateLantern`
3. Apply material colors using the hex values in the table above
4. For the glass panels (`PirateLanternGlass`), use a semi-transparent material with a `PointLight` inside to simulate the flame glow
5. Set `Anchored = true` if using as a static prop (hanging on a wall, sitting on a table)
6. To hang the lantern: attach it to a hook or rope via the handle loop at the top
7. Scale up as needed — recommend 2×–3× for a wall-mounted or floor lantern
