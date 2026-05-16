# grotto_lighthouse — Roblox Spec

**Category:** Hero environment landmark  
**Scale:** 1 Blender unit = 1 meter (~8.3 m tall after lantern raise)  
**Triangles:** ~4,988 (37 mesh parts — hero landmark budget ≤ 5,000)  
**Pivot:** `GROTTO_grotto_lighthouse` empty at base center (floor)

## Parts & Colors

### Island base

| Object | Role | Suggested Color | Hex |
|--------|------|-----------------|-----|
| lighthouse_Island_SandShelf | Shore shelf | Sandy tan | #9E8F70 |
| lighthouse_Island_Core | Main rock mass | Mid gray rock | #737680 |
| lighthouse_Island_Boulder_01–02 | Ring boulders (dark) | Dark rock | #525860 |
| lighthouse_Island_Boulder_03 | Boulder + moss cap | Mid rock + moss | #737680 / #4A7A52 |
| lighthouse_Island_Boulder_04 | Ring boulder | Mid rock | #737680 |
| lighthouse_Island_Boulder_05–07 | Ring boulders (light) | Light rock | #94918A |
| lighthouse_Island_Boulder_08 | Water-facing rock | Wet teal rock | #3A5E68 |

### Lighthouse tower

| Object | Role | Suggested Color | Hex |
|--------|------|-----------------|-----|
| lighthouse_StoneBase | Foundation | Weathered stone | #6B6B75 |
| lighthouse_StoneLanding | Foundation step | Weathered stone | #6B6B75 |
| lighthouse_Tower_White_01–03 | Stripes | Warm white | #E8E4DC |
| lighthouse_Tower_Red_02,04,06 | Stripes | Maritime red | #B83628 |
| lighthouse_LanternDeck | Gallery deck | Dark iron | #383A42 |
| lighthouse_LanternGlass | Lamp room | Sea glass | #A8D8E8 |
| lighthouse_LanternCap | Lantern ring | Dark iron | #383A42 |
| lighthouse_Roof | Conical roof | Dark iron | #383A42 |
| lighthouse_WeatherVane | Finial | Dark iron | #383A42 |
| lighthouse_Railing | Balcony rail | Dark iron | #383A42 |
| lighthouse_DoorOpening | Entry recess | Interior dark | #1A1A22 |
| lighthouse_DoorLintels | Door frame top | Brass trim | #C8B8A0 |
| lighthouse_DoorPost_L / _R | Door posts | Warm white | #E8E4DC |
| lighthouse_DoorPanel | Entry door (ajar) | Weathered wood | #4A3010 |
| lighthouse_InteriorHall | Inner shaft | Dark interior | #1A1A22 |
| lighthouse_Staircase | Spiral stairs | Oak wood | #8B5E3C |
| lighthouse_StairCenterPole | Stair core | Dark iron | #383A42 |
| lighthouse_StairRailing | Handrail | Dark iron | #383A42 |
| lighthouse_LanternGalleryFloor | **Player walk deck** (full glass diameter) | Gallery planks | #9A9590 |
| lighthouse_GalleryLowWall | **Perimeter low wall** (~0.9 m tall) | Stone | #6B6B75 |
| lighthouse_StairLanding | Stair top platform (meets gallery) | Stone | #6B6B75 |
| lighthouse_StairTopBridge | Stair → gallery ramp plank | Gallery planks | #9A9590 |
| lighthouse_LampGlow | Interior lamp | Warm glow | #FFD972 |

## Roblox gameplay (avatar + multiplayer)

Designed against `roblox-asset-export-contract.md` (1 m = 1 BU; 1 stud ≈ 0.28 m).

| Check | Value | Notes |
|-------|-------|-------|
| Gallery walk diameter | **~6.6 studs** (1.84 m) | Full glass inner width; comfortable for **2 players** circling; tight for 3+ — treat as small encounter zone, not a hub |
| Headroom above deck | **~6 studs** (1.68 m) | R15/R6 can stand under glass; camera may clip if FOV wide — OK for gameplay |
| Low wall height | **~3.2 studs** (0.9 m) | Waist-high guard; blocks walk-off without full cage; use **CanCollide** on wall + floor |
| Stair path | Door → spiral → landing → bridge → gallery | Keep `PreciseConvexDecomposition` or **Default** collision on stairs/floor; **Box** only on simple cylinders if perf-critical |
| Multiplayer perf | 37 `MeshPart`s after export | One material per part; avoid extra invisible collision duplicates — union in Studio only if needed |
| Interaction | Optional `ProximityPrompt` at door | Suggested pattern: prompt at `lighthouse_DoorOpening`, fade teleport to gallery only if using interior instance |

**Studio import:** Group under a `Model`; set gallery `lighthouse_LanternGalleryFloor` + `lighthouse_GalleryLowWall` + `lighthouse_Staircase` to **CanCollide = true**; glass `lighthouse_LanternGlass` **CanCollide = false** (visual only). Lamp glow: non-colliding Neon.

## Studio Notes

- Import FBX from `exports/` after running `scripts/grotto_roblox_pipeline.py`.
- Parent empty exports as `Model`; tint each `MeshPart` per table above.
- Place on harbor/coast tiles; pivot sits on ground plane (Z up, -Y forward per export contract).
- `lighthouse_LampGlow` can use `Material = Neon` or PointLight child for night cycle.
- Gallery deck matches **full** `lighthouse_LanternGlass` diameter; low wall sits on deck outer edge.

## Export

```bash
/Applications/Blender.app/Contents/MacOS/Blender -b \
  "$PWD/assets/environment/grotto_lighthouse/grotto_lighthouse.blend" \
  --python "$(pwd)/scripts/grotto_roblox_pipeline.py" -- --process-open-file
```
