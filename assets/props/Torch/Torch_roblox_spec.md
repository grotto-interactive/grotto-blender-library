# Torch — Roblox Spec

**Size:** ~3.2 studs tall (hand-held prop)
**Parts:** 4 mesh objects, 4 colors

## Parts & Colors

| Object | Material | Color | Hex |
|---|---|---|---|
| Torch_Handle | M_Wood | Dark Brown | #47230A |
| Torch_Cup | M_Metal | Dark Bronze | #332814 |
| Torch_FlameBase | M_FlameBase | Orange Flame | #FF6205 |
| Torch_FlameTip | M_FlameTip | Yellow Tip | #FFE633 |

## Studio Notes
- Import `Torch.fbx` — 4 separate mesh parts
- Set each part's `Color` property to the hex value above
- **Torch_Handle** is a cone shape — narrow at the grip (bottom), widens toward the cup
- **Torch_Cup** is a small flared metal collar between handle and flame
- **Torch_FlameBase** is a cartoon-style bulging orange flame body
- **Torch_FlameTip** sits on top of the flame base and tapers to a sharp yellow point
- Designed as a hand-held item — attach to character hand or use as a tool prop
- Scale is 1 FBX unit = 1 Roblox stud — no rescaling needed on import
