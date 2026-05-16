# Map — Roblox Spec

**Size:** ~5.0 studs wide × 3.5 studs deep × 0.06 studs tall (flat table prop)
**Parts:** 23 mesh objects, 8 colors

## Colors

| Material | Description | Hex |
|---|---|---|
| M_Burn | Charred dark edges | #1A0D02 |
| M_Parchment | Aged tan parchment | #C8A060 |
| M_Ink | Dark ink (dots & path) | #2E1A0D |
| M_X | Red X marker | #8C0D0D |
| M_Water | Muted blue water | #3A6E9E |
| M_Grass | Muted green grass | #4A7A30 |
| M_Mountain | Grey-brown mountains | #7A6A55 |

## Parts

| Object | Material | Description |
|---|---|---|
| Map_Burn | M_Burn | Outer charred/worn irregular border |
| Map_Parchment | M_Parchment | Inner aged parchment surface |
| Map_Dot_00 – Map_Dot_07 | M_Ink | 8 dots forming dotted trail path |
| Map_X_A, Map_X_B | M_X | Two crossed bars forming the X marker |
| Map_Water_0 – Map_Water_2 | M_Water | 3 flat wavy water shapes (upper-left) |
| Map_Grass_0 – Map_Grass_4 | M_Grass | 5 flat leaf/teardrop grass icons (upper-center) |
| Map_Mountain_0 – Map_Mountain_2 | M_Mountain | 3 flat triangle mountain icons (right of trail) |

## Studio Notes
- Import `Map.fbx` — 23 separate mesh parts
- Set each part's `Color` property to the hex above
- Map lays flat — place directly on a table surface; all parts sit at Z=0
- **Map_Burn** sits slightly below Map_Parchment to form the charred border frame
- Dotted trail winds from lower-left to upper-right where the X sits
- Landmarks are very flat (drawn/painted look) — no rescaling needed
- Scale is 1 FBX unit = 1 Roblox stud — no rescaling needed on import
