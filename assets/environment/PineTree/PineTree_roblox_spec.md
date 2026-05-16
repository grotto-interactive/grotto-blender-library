# PineTree — Roblox Import Spec

**Asset:** PineTree  
**Created by:** Tasha (Grotto Interactive)  
**Date:** 2026-05-06  
**For:** Caleb — Roblox Studio import

---

## Files

| File | Location |
|------|----------|
| `PineTree.blend` | Desktop |
| `PineTree.fbx` | Desktop — import this one |

---

## Object Inventory

| Object | Type | Notes |
|--------|------|-------|
| `PineTree` | Single mesh | Trunk and foliage joined into one object |

- **Verts:** 138  
- **Tris:** 214  
- Clean mesh — static asset, no rigging or animations

---

## Dimensions

Exported at 0.01 scale (1 Blender unit = 1 Roblox stud).

| Axis | Size |
|------|------|
| Width (X) | ~4.8 studs |
| Depth (Y) | ~4.9 studs |
| Height (Z) | ~5.9 studs |

> A standard R15 character is ~5 studs tall. This tree imports close to player height — scale up in Studio for a full-size pine.

---

## Materials

| Material Name | Hex Color | Roughness | Used On |
|---------------|-----------|-----------|---------|
| `PineFoliageMat` | `#19601E` | 0.85 | Foliage / branches |
| `PineTrunkMat` | `#512D11` | 0.95 | Trunk |

> Blender node materials do not import directly into Roblox. Recreate as `SurfaceAppearance` or plain `Color` properties using the hex values above.

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

1. Import `PineTree.fbx` via **File → Import → Import 3D Model**
2. The mesh will arrive as a single `MeshPart` named `PineTree`
3. Apply material colors using the hex values in the table above
4. Scale up as needed — recommend testing at 2×–3× for a full-size environment tree
5. Set `Anchored = true` if using as a static prop
6. No rigging or animations — static asset only
