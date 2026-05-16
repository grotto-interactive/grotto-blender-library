# Basket — Roblox Spec

**Size:** ~1.36 studs diameter × 0.80 studs tall (shop prop)
**Parts:** 4 mesh objects, 2 colors

## Parts & Colors

| Object | Material | Color | Hex |
|---|---|---|---|
| Basket_Body | M_Wicker | Warm straw tan | #CAA368 |
| Basket_Band_0 | M_Rim | Dark tan band (lower) | #B78E50 |
| Basket_Band_1 | M_Rim | Dark tan band (upper) | #B78E50 |
| Basket_Rim | M_Rim | Dark tan lip ring at top | #B78E50 |

## Studio Notes
- Import `Basket.fbx` — 4 separate mesh parts
- Set each part's `Color` property to the hex value above
- **Basket_Body** is the tapered open cylinder — wider at top, narrower at base, hollow (no top cap)
- **Basket_Band_0 / Band_1** are thin horizontal wicker rings around the body for texture detail
- **Basket_Rim** is the narrow lip ring at the top edge — slightly wider and darker than the body
- Basket sits flat — base rests at Z=0
- Scale is 1 FBX unit = 1 Roblox stud — no rescaling needed on import
- Works as a floor prop, counter decoration, or shelf item in the Merchant Shop
