# PalmTree2 — Roblox Import Spec

**Asset:** PalmTree2  
**Created by:** Tasha (Grotto Interactive)  
**Date:** 2026-05-06  
**For:** Caleb — Roblox Studio import

---

## Files

| File | Location |
|------|----------|
| `PalmTree2.blend` | Desktop |
| `PalmTree2.fbx` | Desktop — import this one |

---

## Object Inventory

| Object | Type | Notes |
|--------|------|-------|
| `PalmTree2` | Single mesh | Trunk and palm leaves joined into one object |

- **Verts:** 198  
- **Tris:** 247  
- Clean mesh — static asset, no rigging or animations

---

## Dimensions

Exported at 0.01 scale (1 Blender unit = 1 Roblox stud).

| Axis | Size |
|------|------|
| Width (X) | ~3.1 studs |
| Depth (Y) | ~2.8 studs |
| Height (Z) | ~5.5 studs |

> A standard R15 character is ~5 studs tall. This is the tallest of the palm variants — roughly player height at default scale. Scale up in Studio as needed.

---

## Materials

| Material Name | Hex Color | Roughness | Used On |
|---------------|-----------|-----------|---------|
| `TrunkMat.003` | `#72471E` | 0.90 | Trunk |
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

1. Import `PalmTree2.fbx` via **File → Import → Import 3D Model**
2. The mesh will arrive as a single `MeshPart` named `PalmTree2`
3. Apply material colors using the hex values in the table above
4. Scale up as needed for the environment — recommend testing at 2× for a full-size tree
5. Set `Anchored = true` if using as a static prop
6. No rigging or animations — static asset only
