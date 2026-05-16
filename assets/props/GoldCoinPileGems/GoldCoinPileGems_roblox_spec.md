# GoldCoinPileGems — Roblox Import Spec

**Asset:** Gold Coin Pile with Scattered Coins and Gemstones (treasure prop)
**File:** `GoldCoinPileGems.fbx`
**Scale:** 1 unit = 1 Roblox stud
**Footprint:** ~4.5 studs wide (coins) — gems reach ~2.1 studs from center
**Coins:** 27 total — 3 stacks at center, 8 scattered near pile, 10 spread outward (includes 2 close pairs)
**Gems:** 10 total — 3 ruby, 3 emerald, 2 sapphire, 2 amethyst; faceted 8-sided shape, ~0.42 studs wide × ~0.38 studs tall

---

## Materials

| Material | Hex | RGB (0–255) | Notes |
|---|---|---|---|
| GoldCoinPile_CoinMat | `#FFD700` | 255, 215, 0 | Bright gold — set Metallic in Studio |
| GemPile_RubyMat | `#CC2200` | 204, 34, 0 | Deep red — set Metallic or Neon |
| GemPile_EmeraldMat | `#1A8C3A` | 26, 140, 58 | Rich green — set Metallic or Neon |
| GemPile_SapphireMat | `#1A3ACC` | 26, 58, 204 | Deep blue — set Metallic or Neon |
| GemPile_AmethystMat | `#7B2FBE` | 123, 47, 190 | Purple — set Metallic or Neon |

---

## Object List (5 parts)

| Part | Material | Notes |
|---|---|---|
| GoldCoinPile_CoinMat_pile | GoldCoinPile_CoinMat | All 27 coins — stacks, tilted, near scatter, and far scatter |
| GemPile_RubyMat_gems | GemPile_RubyMat | 3 ruby gems scattered among coins |
| GemPile_EmeraldMat_gems | GemPile_EmeraldMat | 3 emerald gems scattered among coins |
| GemPile_SapphireMat_gems | GemPile_SapphireMat | 2 sapphire gems scattered among coins |
| GemPile_AmethystMat_gems | GemPile_AmethystMat | 2 amethyst gems scattered among coins |

---

## Studio Setup Notes
- Set `Color` to hex values above per part
- Set coins `Material` to `SmoothPlastic` or `Metal` for gold sheen
- Set gems `Material` to `Neon` or `Glass` for a glowing jewel look — or `SmoothPlastic` for flat color
- Set `CanCollide = true` on the coin pile; `CanCollide = false` on all gem parts
- Pairs well with `GoldCoinPile`, `GoldCoinPileScattered`, and `grotto_chest` for treasure scenes
