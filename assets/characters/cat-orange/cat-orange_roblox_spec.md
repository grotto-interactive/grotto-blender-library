# cat-orange — Roblox Import Spec

**Asset:** Orange and White Cat  
**File:** `cat-orange.fbx`  
**Scale:** 1 unit = 1 Roblox stud

---

## Materials

| Material | Hex | RGB (0–255) | Parts |
|---|---|---|---|
| Cat_BlackMat | `#CD6108` | 205, 97, 8 | body, head, neck, ears, legs, tail, tailJoint, pupils |
| Cat_WhiteMat | `#FFFFFF` | 255, 255, 255 | earTips, earSpots, chest, muzzle, paws, spots, sclera, brows, catchlights, tailTip |
| Cat_EyeMat | `#EB9E0D` | 235, 158, 13 | irises (amber) — use Neon material in Studio for glow |
| Cat_PinkMat | `#F29999` | 242, 153, 153 | nose |

---

## Object List (same 35 parts as cat-black&white — only colors differ)

**Cat_BlackMat (#CD6108 orange)**
- Cat_BlackMat_body, Cat_BlackMat_head, Cat_BlackMat_neck
- Cat_BlackMat_ear_L, Cat_BlackMat_ear_R
- Cat_BlackMat_frontL_leg, Cat_BlackMat_frontR_leg
- Cat_BlackMat_backL_leg, Cat_BlackMat_backR_leg
- Cat_BlackMat_tail, Cat_BlackMat_tailJoint
- Cat_BlackMat_pupil_L, Cat_BlackMat_pupil_R

**Cat_WhiteMat (#FFFFFF)**
- Cat_WhiteMat_earTip_L/R, Cat_WhiteMat_earSpot_L/R
- Cat_WhiteMat_chest, Cat_WhiteMat_muzzle
- Cat_WhiteMat_spot_1, Cat_WhiteMat_spot_2, Cat_WhiteMat_tailTip
- Cat_WhiteMat_frontL/R_paw, Cat_WhiteMat_backL/R_paw
- Cat_WhiteMat_sclera_L/R, Cat_WhiteMat_catchlight_L/R, Cat_WhiteMat_brow_L/R

**Cat_EyeMat (#EB9E0D amber)**
- Cat_EyeMat_iris_L, Cat_EyeMat_iris_R

**Cat_PinkMat (#F29999)**
- Cat_PinkMat_nose

---

## Studio Notes
- Same structure as cat-black&white — apply colors above per part
- Set `CanCollide = false` on all face patches
- Use `Neon` material on iris parts for glowing amber eyes
- Eye layer order: catchlight → pupil → iris → sclera
