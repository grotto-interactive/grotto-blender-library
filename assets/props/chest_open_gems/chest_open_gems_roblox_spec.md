# ChestOpenGems — Roblox Spec

**Size:** ~9.9 studs wide × 6.6 deep × 3.5 studs tall (body) — lid pre-rotated open  
**Parts:** 62 mesh objects, 8 colors

## Colors

| Material | Gem Type | Hex |
|---|---|---|
| M_Wood | Dark Brown (chest wood) | #47230A |
| M_Metal | Dark Bronze (bands & corners) | #332814 |
| M_Ruby | Ruby — deep red | #CC0D0D |
| M_Sapphire | Sapphire — royal blue | #0D1AD9 |
| M_Emerald | Emerald — rich green | #0AB226 |
| M_Amethyst | Amethyst — purple | #8C1ACC |
| M_Diamond | Diamond — icy white-blue | #D9F2FF |
| M_Topaz | Topaz — amber gold | #E69908 |

## Chest Parts (20 objects)

| Object | Hex |
|---|---|
| Chest_Body, Chest_Interior, Chest_Lid | #47230A |
| Band_0_Arch/Back/Front, Band_1_Arch/Back/Front, Band_2_Arch/Back/Front | #332814 |
| Corner_BL_X/Y, Corner_BR_X/Y, Corner_FL_X/Y, Corner_FR_X/Y | #332814 |

## Gem Mass (1 object)

| Object | Hex | Description |
|---|---|---|
| Gem_Mass | #332814 | Dark base block filling chest interior Z=0–2.8 |

Set `Gem_Mass` to `#332814` so it reads as shadow depth beneath the gems.

## Gem Parts (41 objects — 6 gem types cycling in order)

| Layer | Objects | Description |
|---|---|---|
| Layer 1 | Gem_L1_00 – Gem_L1_12 | 13 gems flat on mass surface |
| Layer 2 | Gem_L2_00 – Gem_L2_10 | 11 gems mid-height, lightly tilted |
| Layer 3 | Gem_L3_00 – Gem_L3_07 | 8 gems upper layer, more tilted |
| Layer 4 | Gem_L4_00 – Gem_L4_06 | 7 gems top heap, heavily tilted |
| Layer 5 | Gem_L5_00 – Gem_L5_01 | 2 gems at peak, standing proud |

Gem color assignment cycles: Ruby → Sapphire → Emerald → Amethyst → Diamond → Topaz → repeat

## Gem Shape
Each gem is a faceted hexagonal cut: flat pavilion base, 6-sided crown facets, small table (flat top). Set each `Gem_*` part's `Color` to whichever gem hex matches its material name suffix.

## Studio Notes
- Import `chest_open_gems.fbx` — 62 separate mesh parts
- **Lid is pre-rotated open** — import as-is, do not adjust
- **Chest_Interior** inner walls face inward and render correctly from inside
- **Gem_Mass** fills the chest to Z=2.8 (4/5 of body height); set it dark (#332814) so it reads as depth
- Gems sit on top of Gem_Mass and pile above the rim — no gem clips below Z=2.8
- Scale is 1 FBX unit = 1 Roblox stud — no rescaling needed on import
