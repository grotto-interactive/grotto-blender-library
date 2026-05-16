# Torch_Wall — Roblox Spec

**Size:** ~4.0 studs tall × ~1.0 stud deep (wall-mounted sconce)
**Parts:** 7 mesh objects, 4 colors

## Parts & Colors

| Object | Material | Color | Hex |
|---|---|---|---|
| Torch_WallPlate | M_Metal | Dark Bronze | #332814 |
| Torch_Arm | M_Metal | Dark Bronze | #332814 |
| Torch_Cradle | M_Metal | Dark Bronze | #332814 |
| Torch_Cup | M_Metal | Dark Bronze | #332814 |
| Torch_Handle | M_Wood | Dark Brown | #47230A |
| Torch_FlameBase | M_FlameBase | Orange Flame | #FF6205 |
| Torch_FlameTip | M_FlameTip | Yellow Tip | #FFE633 |

## Studio Notes
- Import `Torch_Wall.fbx` — 7 separate mesh parts
- Set each part's `Color` property to the hex value above
- **Torch_WallPlate** is the flat backing plate — position flush against a wall surface
- **Torch_Arm** is the horizontal bracket extending from the plate
- **Torch_Cradle** is the ring at the end of the arm that holds the torch
- **Torch_Handle** sits 3/4 of its length down through the cradle ring; only the top quarter and flame extend above
- **Torch_Cup** is the small flared metal collar at the top of the handle
- **Torch_FlameBase** and **Torch_FlameTip** form the cartoon-style flame above the cup
- Mount by placing Torch_WallPlate flush against a wall — all other parts extend outward automatically
- Scale is 1 FBX unit = 1 Roblox stud — no rescaling needed on import
