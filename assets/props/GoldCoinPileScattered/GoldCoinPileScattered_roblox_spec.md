# GoldCoinPileScattered — Roblox Import Spec

**Asset:** Gold Coin Pile with Scattered Coins (treasure prop)
**File:** `GoldCoinPileScattered.fbx`
**Scale:** 1 unit = 1 Roblox stud
**Footprint:** ~4.5 studs wide (main pile ~1.8 studs, scattered coins reach ~2.1 studs out)
**Coins:** 27 total — 3 stacks at center, 8 scattered near pile, 10 spread outward (includes 2 close pairs)

---

## Materials

| Material | Hex | RGB (0–255) | Notes |
|---|---|---|---|
| GoldCoinPile_CoinMat | `#FFD700` | 255, 215, 0 | Bright gold — set Metallic in Studio |

---

## Object List (1 part)

| Part | Material | Notes |
|---|---|---|
| GoldCoinPile_CoinMat_pile | GoldCoinPile_CoinMat | All 27 coins — stacks, tilted, near scatter, and far scatter with 2 close pairs |

---

## Studio Setup Notes
- Set `Color` to `#FFD700`
- Set `Material` to `SmoothPlastic` or `Metal` for a shiny gold look
- Set `CanCollide = true`
- The scattered coins spread ~2.1 studs from center — leave floor space around it
- Pairs well with `GoldCoinPile` (tighter version) and `grotto_chest` for treasure scenes
