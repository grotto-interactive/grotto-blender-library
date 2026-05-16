# ChestOpenCoins — Roblox Spec

**Size:** ~9.9 studs wide × 6.6 deep × 3.5 studs tall (body) — lid pre-rotated open  
**Parts:** 169 mesh objects, 3 colors

## Colors

| Material | Color Name | Hex |
|---|---|---|
| M_Wood | Dark Brown (chest wood) | #47230A |
| M_Metal | Dark Bronze (bands & corners) | #332814 |
| M_Gold_Coin | Gold (coins & coin mass) | #C88C0A |

## Chest Parts (20 objects)

| Object | Hex |
|---|---|
| Chest_Body, Chest_Interior, Chest_Lid | #47230A |
| Band_0_Arch/Back/Front, Band_1_Arch/Back/Front, Band_2_Arch/Back/Front | #332814 |
| Corner_BL_X/Y, Corner_BR_X/Y, Corner_FL_X/Y, Corner_FR_X/Y | #332814 |

## Coin Parts (149 objects — all #C88C0A)

| Object | Description |
|---|---|
| Coin_Mass | Solid gold block filling chest interior Z=0–3.0 |
| Coin_Top_00 – Coin_Top_23 | 24 coins on first surface layer |
| Coin_Heap_00 – Coin_Heap_07 | 8 coins on sub-layer |
| Coin_Peak_00 – Coin_Peak_02 | 3 coins at original peak |
| Coin_Extra_00 – Coin_Extra_14 | 15 coins on upper layer |
| Coin_Scatter_00 – Coin_Scatter_23 | 24 scattered coins with wide angle variety |
| Coin_Dbl_00 – Coin_Dbl_62 | 63 doubled coins filling gaps, varied heights |
| Coin_Dbl2_00 – Coin_Dbl2_10 | 11 additional coins completing the double |

## Studio Notes
- Import `chest_open_coins.fbx` — 169 separate mesh parts
- Set all `Coin_*` parts to `#C88C0A`
- Set chest wood parts to `#47230A`, metal parts to `#332814`
- **Lid is pre-rotated open** — import as-is, do not adjust
- **Chest_Interior** inner walls face inward and render correctly from inside
- All coins sit fully on top of the coin mass — nothing clips below Z=3.0
- Scale is 1 FBX unit = 1 Roblox stud — no rescaling needed on import
