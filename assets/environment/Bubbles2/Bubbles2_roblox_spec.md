# Bubbles2 — Roblox Import Spec

**Asset:** Underwater Bubble Stream (single rising column)
**File:** `Bubbles2.fbx`
**Scale:** 1 unit = 1 Roblox stud
**Height:** ~5.3 studs — bubbles get smaller toward the top

---

## Material

| Material | Hex | RGB (0–255) | Notes |
|---|---|---|---|
| Bubbles_BubbleMat | `#8CE0FF` | 140, 224, 255 | Set Transparency 0.4–0.6 in Studio |

---

## Object List (12 parts)

| Part | Radius | Notes |
|---|---|---|
| Bubbles_BubbleMat_bubble_01 | 0.16 | bottom |
| Bubbles_BubbleMat_bubble_02 | 0.24 | |
| Bubbles_BubbleMat_bubble_03 | 0.18 | |
| Bubbles_BubbleMat_bubble_04 | 0.32 | |
| Bubbles_BubbleMat_bubble_05 | 0.20 | |
| Bubbles_BubbleMat_bubble_06 | 0.28 | |
| Bubbles_BubbleMat_bubble_07 | 0.22 | |
| Bubbles_BubbleMat_bubble_08 | 0.10 | top — small |
| Bubbles_BubbleMat_bubble_09 | 0.08 | top — small |
| Bubbles_BubbleMat_bubble_10 | 0.12 | top — small |
| Bubbles_BubbleMat_bubble_11 | 0.07 | top — tiny |
| Bubbles_BubbleMat_bubble_12 | 0.09 | top — tiny |

---

## Studio Setup Notes
- Set `Color` to `#8CE0FF` on all parts
- Set `Material` to `Glass` or `ForceField`
- Set `Transparency` to `0.4–0.6` on all parts
- Set `CanCollide = false` and `CastShadow = false` on all parts
- Pairs well with Bubbles (3-stream version) for varied seafloor decoration
