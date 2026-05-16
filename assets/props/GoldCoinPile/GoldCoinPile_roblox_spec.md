# GoldCoinPile — Roblox Import Spec

**Asset:** Gold Coin Pile (treasure prop)
**File:** `GoldCoinPile.fbx`
**Scale:** 1 unit = 1 Roblox stud
**Footprint:** ~2.4 studs wide × ~0.6 studs tall
**Coins:** 17 total — 3 stacks (4 + 3 + 2 high), 5 flat scattered, 3 tilted/tipped

---

## Materials

| Material | Hex | RGB (0–255) | Notes |
|---|---|---|---|
| GoldCoinPile_CoinMat | `#FFD700` | 255, 215, 0 | Bright gold — set Metallic in Studio |

---

## Object List (1 part)

| Part | Material | Notes |
|---|---|---|
| GoldCoinPile_CoinMat_pile | GoldCoinPile_CoinMat | All 17 coins combined — stacks, scattered, and tilted |

---

## Studio Setup Notes
- Set `Color` to `#FFD700`
- Set `Material` to `SmoothPlastic` or `Metal` for a shiny gold look
- Set `Reflectance` / `Metalness` high for gold sheen
- Set `CanCollide = true` on the pile object (it's a solid prop)
- Place on any flat surface — seafloor, chest interior, cave floor
- Pairs well with the treasure chest (`grotto_chest`) for a loot scene
