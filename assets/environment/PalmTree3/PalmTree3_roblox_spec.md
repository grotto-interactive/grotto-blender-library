# PalmTree3 — Roblox Import Spec

**Asset:** PalmTree3  
**Created by:** Tasha (Grotto Interactive)  
**Date:** 2026-05-06  
**For:** Caleb — Roblox Studio import

---

## Files

| File | Location |
|------|----------|
| `PalmTree3.blend` | Desktop |
| `PalmTree3.fbx` | Desktop — import this one |

---

## Object Inventory

| Object | Type | Notes |
|--------|------|-------|
| `PalmTree3` | Single mesh | Trunk and palm leaves joined into one object |

- **Verts:** 244  
- **Tris:** 269  
- Clean mesh — static asset, no rigging or animations

---

## Dimensions

Exported at 0.01 scale (1 Blender unit = 1 Roblox stud).

| Axis | Size |
|------|------|
| Width (X) | ~2.6 studs |
| Depth (Y) | ~2.5 studs |
| Height (Z) | ~2.2 studs |

> A standard R15 character is ~5 studs tall. This is a very short palm — more of a bush/sapling scale. Scale up significantly in Studio if a full-size tree is needed.

---

## Materials

| Material Name | Hex Color | Roughness | Used On |
|---------------|-----------|-----------|---------|
| `TrunkMat.004` | `#72471E` | 0.90 | Trunk |
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

1. Import `PalmTree3.fbx` via **File → Import → Import 3D Model**
2. The mesh will arrive as a single `MeshPart` named `PalmTree3`
3. Apply material colors using the hex values in the table above
4. Scale up significantly as needed — this palm imports very small relative to player scale
5. Set `Anchored = true` if using as a static prop
6. No rigging or animations — static asset only
