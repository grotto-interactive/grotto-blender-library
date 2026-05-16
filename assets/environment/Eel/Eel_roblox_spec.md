# Eel — Roblox Import Spec

**Asset:** Underwater Eel (serpentine sea creature)
**File:** `Eel.fbx`
**Scale:** 1 unit = 1 Roblox stud
**Length:** ~6.3 studs (tail to snout tip)
**Max Width:** ~0.9 studs at thickest body cross-section

---

## Materials

| Material | Hex | RGB (0–255) | Notes |
|---|---|---|---|
| Eel_BodyMat | `#2D4A1A` | 45, 74, 26 | Dark olive green — body, jaw area |
| Eel_BellyMat | `#8DB878` | 141, 184, 120 | Light olive — underside belly strip |
| Eel_FinMat | `#1A3010` | 26, 48, 16 | Very dark green — all fins |
| Eel_EyeMat | `#0D0D0D` | 13, 13, 13 | Near black — eyes, nostrils, mouth |

---

## Object List (11 parts)

### Body — Eel_BodyMat (`#2D4A1A`)
- `Eel_BodyMat_body` — full S-curve tube body, tapers from thick midsection to thin tail and rounded snout; upper jaw closes at snout tip

### Belly — Eel_BellyMat (`#8DB878`)
- `Eel_BellyMat_belly` — lighter-colored underside strip running from tail to neck

### Fins — Eel_FinMat (`#1A3010`)
- `Eel_FinMat_dorsalFin` — continuous ridge fin along the top, from tail to head
- `Eel_FinMat_tailFin` — vertical diamond-shaped fin at the tail end
- `Eel_FinMat_pectoralFin_L` — small triangular side fin, left, near head
- `Eel_FinMat_pectoralFin_R` — small triangular side fin, right, near head

### Face — Eel_EyeMat (`#0D0D0D`)
- `Eel_EyeMat_eye_L` — small dark eye sphere, left side of head
- `Eel_EyeMat_eye_R` — small dark eye sphere, right side of head
- `Eel_EyeMat_nostril_L` — tiny nostril dot, left, top of snout
- `Eel_EyeMat_nostril_R` — tiny nostril dot, right, top of snout
- `Eel_EyeMat_mouth` — dark lower arc closing the snout opening (slightly open mouth)

---

## Studio Setup Notes
- Set `Color` to the hex values above per part
- Set `Material` to `SmoothPlastic` on all body/belly/fin parts
- Set `Material` to `Neon` on `Eel_EyeMat_*` parts for dark glowing eyes (or use `SmoothPlastic` for flat dark)
- Set `CanCollide = false` on all face parts (eyes, nostrils, mouth)
- Set `CastShadow = false` on fins and face parts
- Scatter along the seafloor or attach to coral/rock formations
- Pairs well with Bubbles and Bubbles2 for ambient underwater decoration
