# PalmTree — Roblox Import Spec

**Asset:** PalmTree  
**Created by:** Tasha (Grotto Interactive)  
**Date:** 2026-05-06  
**For:** Caleb — Roblox Studio import

---

## Files

| File | Location |
|------|----------|
| `PalmTree.blend` | Desktop |
| `PalmTree.fbx` | Desktop — import this one |

---

## Object Inventory

| Object | Type | Notes |
|--------|------|-------|
| `PalmTree` | Single mesh | Trunk and palm leaves joined into one object |

- **Verts:** 191  
- **Tris:** 233  
- Clean mesh — static asset, no rigging or animations

---

## Dimensions

Exported at 0.01 scale (1 Blender unit = 1 Roblox stud).

| Axis | Size |
|------|------|
| Width (X) | ~2.3 studs |
| Depth (Y) | ~2.4 studs |
| Height (Z) | ~2.8 studs |

> A standard R15 character is ~5 studs tall. This is a shorter palm — scale up in Studio as needed for the environment.

---

## Materials

| Material Name | Hex Color | Roughness | Used On |
|---------------|-----------|-----------|---------|
| `TrunkMat.002` | `#72471E` | 0.90 | Trunk |
| `LeafMat` | `#2DA526` | 0.80 | Palm leaves |

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

1. Import `PalmTree.fbx` via **File → Import → Import 3D Model**
2. The mesh will arrive as a single `MeshPart` named `PalmTree`
3. Apply material colors using the hex values in the table above
4. Scale up as needed — recommend testing at 2×–3× for a full-size environment tree
5. Set `Anchored = true` if using as a static prop
6. No rigging or animations — static asset only
