# MapleTree — Roblox Import Spec

**Asset:** MapleTree  
**Created by:** Tasha (Grotto Interactive)  
**Date:** 2026-05-06  
**For:** Caleb — Roblox Studio import

---

## Files

| File | Location |
|------|----------|
| `MapleTree.blend` | Desktop |
| `MapleTree.fbx` | Desktop — import this one |

---

## Object Inventory

| Object | Type | Notes |
|--------|------|-------|
| `MapleTree` | Single mesh | Trunk and crown joined into one object |

- **Verts:** 337  
- **Tris:** 650  
- Clean mesh — static asset, no rigging or animations

---

## Dimensions

Exported at 0.01 scale (1 Blender unit = 1 Roblox stud).

| Axis | Size |
|------|------|
| Width (X) | ~4.9 studs |
| Depth (Y) | ~5.5 studs |
| Height (Z) | ~6.5 studs |

> A standard R15 character is ~5 studs tall. This tree is taller than a player at default scale — scale up further in Studio as needed for the environment.

---

## Materials

| Material Name | Hex Color | Roughness | Used On |
|---------------|-----------|-----------|---------|
| `MapleTrunk.001` | `#6B3A1F` | 0.90 | Trunk |
| `MapleCrown.001` | `#4A9C28` | 0.80 | Crown / foliage |

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

1. Import `MapleTree.fbx` via **File → Import → Import 3D Model**
2. The mesh will arrive as a single `MeshPart` named `MapleTree`
3. Apply material colors using the hex values in the table above
4. Scale up as needed for the environment
5. Set `Anchored = true` if using as a static prop
6. No rigging or animations — static asset only
