# cat-calico — Roblox Import Spec

**Asset:** Calico Cat (black, orange, white)
**File:** `cat-calico.fbx`  
**Scale:** 1 unit = 1 Roblox stud

---

## Materials

| Material | Hex | RGB (0–255) | Color |
|---|---|---|---|
| Cat_BlackMat | `#050505` | 5, 5, 5 | near-black |
| Cat_OrangeMat | `#CD6108` | 205, 97, 8 | orange |
| Cat_WhiteMat | `#FFFFFF` | 255, 255, 255 | white |
| Cat_EyeMat | `#EB9E0D` | 235, 158, 13 | amber — use Neon in Studio |
| Cat_PinkMat | `#F29999` | 242, 153, 153 | pink |

---

## Object List — color per part

### Black — Cat_BlackMat (#050505)
- `Cat_BlackMat_body`
- `Cat_BlackMat_neck`
- `Cat_BlackMat_ear_L`
- `Cat_BlackMat_frontR_leg`
- `Cat_BlackMat_backL_leg`
- `Cat_BlackMat_pupil_L`, `Cat_BlackMat_pupil_R`

### Orange — Cat_OrangeMat (#CD6108)
- `Cat_BlackMat_head` ← orange despite name
- `Cat_BlackMat_ear_R` ← orange despite name
- `Cat_BlackMat_frontL_leg` ← orange despite name
- `Cat_BlackMat_backR_leg` ← orange despite name
- `Cat_BlackMat_tail` ← orange despite name
- `Cat_BlackMat_tailJoint` ← orange despite name

### White — Cat_WhiteMat (#FFFFFF)
- `Cat_WhiteMat_earTip_L/R`, `Cat_WhiteMat_earSpot_L/R`
- `Cat_WhiteMat_chest`, `Cat_WhiteMat_muzzle`
- `Cat_WhiteMat_spot_1`, `Cat_WhiteMat_spot_2`, `Cat_WhiteMat_tailTip`
- `Cat_WhiteMat_frontL/R_paw`, `Cat_WhiteMat_backL/R_paw`
- `Cat_WhiteMat_sclera_L/R`, `Cat_WhiteMat_catchlight_L/R`, `Cat_WhiteMat_brow_L/R`

### Amber — Cat_EyeMat (#EB9E0D)
- `Cat_EyeMat_iris_L`, `Cat_EyeMat_iris_R`

### Pink — Cat_PinkMat (#F29999)
- `Cat_PinkMat_nose`

---

## Studio Notes
- **Note:** Several parts named `Cat_BlackMat_*` are actually assigned Cat_OrangeMat — see "Orange" list above
- Set `CanCollide = false` on all face patches (eyes, nose, muzzle, brows, sclera, catchlights)
- Use `Neon` on iris parts for glowing amber eyes
- Eye layer order: catchlight → pupil → iris → sclera
