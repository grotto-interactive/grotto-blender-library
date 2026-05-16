# Villager — Roblox Import Spec

**Asset:** Villager  
**Created by:** Tasha (Grotto Interactive)  
**Date:** 2026-05-06  
**For:** Caleb — Roblox Studio import

---

## Files

| File | Location |
|------|----------|
| `Villager.blend` | `characters/Villager/` |
| `Villager.fbx` | `characters/Villager/` — import this one |

---

## Object Inventory

| Object | Type | Notes |
|--------|------|-------|
| `Villager` | Skinned mesh | Single mesh, weighted to armature |
| `VillagerRig` | Armature | 16-bone R15-compatible rig |

- **Verts:** 248  
- **Tris:** 270  
- Rigged — deforms with bones, no animations baked in

---

## Rig — Bone Hierarchy (R15-compatible)

```
Root
└── LowerTorso
    ├── UpperTorso
    │   ├── Head
    │   ├── LeftUpperArm → LeftLowerArm → LeftHand
    │   └── RightUpperArm → RightLowerArm → RightHand
    ├── LeftUpperLeg → LeftLowerLeg → LeftFoot
    └── RightUpperLeg → RightLowerLeg → RightFoot
```

Bone names match Roblox R15 conventions — the Animation Editor should recognize them automatically.

---

## Dimensions

Exported at 0.01 scale (1 Blender unit = 1 Roblox stud).

| Axis | Size |
|------|------|
| Width (X) | ~2.5 studs (shoulder to shoulder) |
| Depth (Y) | ~1.2 studs |
| Height (Z) | ~5.5 studs |

> Matches standard R15 character height (~5 studs). Scale as needed in Studio.

---

## Materials

| Material Name | Hex Color | Roughness | Used On |
|---------------|-----------|-----------|---------|
| `VillagerSkinMat` | `#A0522D` | 0.80 | Head, neck, lower arms, hands |
| `VillagerShirtMat` | `#4A7C3F` | 0.85 | Torso, upper arms (sleeves) |
| `VillagerPantsMat` | `#3A2010` | 0.85 | Upper and lower legs |
| `VillagerBootsMat` | `#2E1F0E` | 0.90 | Feet |
| `VillagerHairMat` | `#1A0A00` | 0.90 | Hair cap |
| `VillagerEyeMat` | `#1A0A00` | 0.90 | Eyes |
| `VillagerMouthMat` | `#5C2B1A` | 0.85 | Mouth |

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
| Object Types | Armature + Mesh |
| Bake Animations | No |
| Leaf Bones | None |

---

## Studio Setup Notes

1. Import `Villager.fbx` via **File → Import → Import 3D Model**
2. The mesh (`Villager`) and rig (`VillagerRig`) will arrive together as a skinned model
3. Apply material colors using the hex values in the table above
4. The rig uses R15-compatible bone names — open the **Animation Editor** plugin to create or apply animations
5. To use as a static NPC prop: set `Anchored = true` on the root part
6. To script as an NPC with movement: add a `Humanoid` and use `AnimationController` or standard NPC scripts
7. Scale in Studio as needed — character arrives close to default R15 height
