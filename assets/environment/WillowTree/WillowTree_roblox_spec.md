# WillowTree — Roblox Import Spec

**Asset:** WillowTree  
**Created by:** Tasha (Grotto Interactive)  
**Date:** 2026-05-06  
**For:** Caleb — Roblox Studio import

---

## Files

| File | Location |
|------|----------|
| `WillowTree.blend` | Desktop |
| `WillowTree.fbx` | Desktop — import this one |

---

## Object Inventory

| Object | Type | Notes |
|--------|------|-------|
| `WillowTree` | Single mesh | Trunk and hanging fronds joined into one object |

- **Verts:** 412  
- **Tris:** 532  
- Clean mesh — static asset, no rigging or animations

---

## Dimensions

Exported at 0.01 scale (1 Blender unit = 1 Roblox stud).

| Axis | Size |
|------|------|
| Width (X) | ~4.5 studs |
| Depth (Y) | ~4.5 studs |
| Height (Z) | ~6.3 studs |

> A standard R15 character is ~5 studs tall. This is the tallest tree in the set — slightly taller than player height at default scale. Scale up in Studio as needed.

---

## Materials

| Material Name | Hex Color | Roughness | Used On |
|---------------|-----------|-----------|---------|
| `WillowFrondMat` | `#7AAD33` | 0.75 | Hanging fronds / foliage |
| `WillowTrunkMat` | `#593816` | 0.95 | Trunk |

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

1. Import `WillowTree.fbx` via **File → Import → Import 3D Model**
2. The mesh will arrive as a single `MeshPart` named `WillowTree`
3. Apply material colors using the hex values in the table above
4. Scale up as needed for the environment
5. Set `Anchored = true` if using as a static prop
6. No rigging or animations — static asset only
