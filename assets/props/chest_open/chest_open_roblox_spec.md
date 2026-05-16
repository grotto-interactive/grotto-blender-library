# ChestOpen — Roblox Spec

**Size:** ~9.9 studs wide × 6.6 deep × 3.5 studs tall (body) — lid pre-rotated open  
**Parts:** 20 mesh objects, 2 colors

## Parts & Colors

| Object | Material | Color | Hex |
|---|---|---|---|
| Chest_Body | Wood | Dark Brown | #47230A |
| Chest_Interior | Wood | Dark Brown | #47230A |
| Chest_Lid | Wood | Dark Brown | #47230A |
| Band_0_Arch | Metal | Dark Bronze | #332814 |
| Band_0_Back | Metal | Dark Bronze | #332814 |
| Band_0_Front | Metal | Dark Bronze | #332814 |
| Band_1_Arch | Metal | Dark Bronze | #332814 |
| Band_1_Back | Metal | Dark Bronze | #332814 |
| Band_1_Front | Metal | Dark Bronze | #332814 |
| Band_2_Arch | Metal | Dark Bronze | #332814 |
| Band_2_Back | Metal | Dark Bronze | #332814 |
| Band_2_Front | Metal | Dark Bronze | #332814 |
| Corner_BL_X | Metal | Dark Bronze | #332814 |
| Corner_BL_Y | Metal | Dark Bronze | #332814 |
| Corner_BR_X | Metal | Dark Bronze | #332814 |
| Corner_BR_Y | Metal | Dark Bronze | #332814 |
| Corner_FL_X | Metal | Dark Bronze | #332814 |
| Corner_FL_Y | Metal | Dark Bronze | #332814 |
| Corner_FR_X | Metal | Dark Bronze | #332814 |
| Corner_FR_Y | Metal | Dark Bronze | #332814 |

## Studio Notes
- Import `chest_open.fbx` — 20 separate mesh parts will come in
- Set each part's `Color` property to the hex value above
- **Lid is pre-rotated open** — do not adjust lid rotation in Studio; it imports in its open pose
- **Chest_Interior** contains the 4 inner walls and floor with normals facing inward — these render correctly from inside the chest; no additional interior parts needed
- Scale is 1 FBX unit = 1 Roblox stud — no rescaling needed on import
- The chest body has no top face (removed to reveal the open interior)
