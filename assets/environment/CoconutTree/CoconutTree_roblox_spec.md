# CoconutTree — Roblox Import Spec

**Asset:** CoconutTree  
**Created by:** Tasha (Grotto Interactive)  
**Date:** 2026-05-06  
**For:** Caleb — Roblox Studio import

---

## Files

| File | Location |
|------|----------|
| `CoconutTree.blend` | Desktop |
| `CoconutTree.fbx` | Desktop — import this one |

---

## Object Inventory

| Object | Type | Notes |
|--------|------|-------|
| `CoconutTree` | Single mesh | Trunk, 7 palm leaves, and 2 coconuts joined into one object |

- **Verts:** 239  
- **Tris:** 363  
- Clean mesh — no duplicate verts, no non-manifold edges, normals facing out

---

## Dimensions

Exported at 0.01 scale (1 Blender unit = 1 Roblox stud).

| Axis | Size |
|------|------|
| Width (X) | ~3.1 studs |
| Depth (Y) | ~3.3 studs |
| Height (Z) | ~4.2 studs |

> Note: A standard R15 character is ~5 studs tall, so this tree is slightly shorter than a player at default scale. Scale up in Studio as needed for the environment.

---

## Materials

| Material Name | Hex Color | Roughness | Used On |
|---------------|-----------|-----------|---------|
| `TrunkMat` | `#B39061` | 0.90 | Trunk |
| `LeafMat` | `#76D36C` | 0.80 | All 7 palm leaves |
| `CoconutMat` | `#81653F` | 1.00 | Both coconuts |

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

1. Import `CoconutTree.fbx` via **File → Import → Import 3D Model**
2. The mesh will arrive as a single `MeshPart` named `CoconutTree`
3. Apply material colors using the hex values in the table above
4. Scale up if needed — recommend testing at 2×–3× for a full-size environment tree
5. Set `Anchored = true` if using as a static prop
6. No rigging or animations — static asset only
