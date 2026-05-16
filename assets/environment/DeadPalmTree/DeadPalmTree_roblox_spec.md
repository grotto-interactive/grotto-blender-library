# DeadPalmTree — Roblox Import Spec

**Asset:** DeadPalmTree  
**Created by:** Tasha (Grotto Interactive)  
**Date:** 2026-05-06  
**For:** Caleb — Roblox Studio import

---

## Files

| File | Location |
|------|----------|
| `DeadPalmTree.blend` | Desktop |
| `DeadPalmTree.fbx` | Desktop — import this one |

---

## Object Inventory

| Object | Type | Notes |
|--------|------|-------|
| `DeadPalmTree` | Single mesh | Trunk and dead/dry leaves joined into one object |

- **Verts:** 215  
- **Tris:** 253  
- Clean mesh — static asset, no rigging or animations

---

## Dimensions

Exported at 0.01 scale (1 Blender unit = 1 Roblox stud).

| Axis | Size |
|------|------|
| Width (X) | ~2.7 studs |
| Depth (Y) | ~2.6 studs |
| Height (Z) | ~3.6 studs |

> A standard R15 character is ~5 studs tall. This tree is shorter than a player — scale up in Studio as needed for the environment.

---

## Materials

| Material Name | Hex Color | Roughness | Used On |
|---------------|-----------|-----------|---------|
| `DeadTrunkMat` | `#472D16` | 1.00 | Trunk |
| `DeadLeafMat` | `#84591E` | 1.00 | Dead brown leaves |
| `DryLeafMat` | `#937A19` | 1.00 | Dry yellowish leaves |

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

1. Import `DeadPalmTree.fbx` via **File → Import → Import 3D Model**
2. The mesh will arrive as a single `MeshPart` named `DeadPalmTree`
3. Apply material colors using the hex values in the table above
4. Scale up as needed — recommend testing at 2×–3× for a full-size environment tree
5. Set `Anchored = true` if using as a static prop
6. No rigging or animations — static asset only
