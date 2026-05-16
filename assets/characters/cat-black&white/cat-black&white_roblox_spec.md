# cat-black&white — Roblox Import Spec

**Asset:** Black and White Cat  
**File:** `cat-black&white.fbx`  
**Scale:** 1 unit = 1 Roblox stud

---

## Materials

| Material | Hex | Parts |
|---|---|---|
| Cat_BlackMat | `#050505` | body, head, neck, ears, legs, tail, tailJoint, pupils |
| Cat_WhiteMat | `#FFFFFF` | earTips, earSpots, chest, muzzle, paws, body spots, sclera, brows, catchlights, tailTip |
| Cat_EyeMat | `#F2B71A` | irises (amber/gold) — use Neon material in Studio for glow |
| Cat_PinkMat | `#F29999` | nose |

---

## Object List

**Cat_BlackMat (#050505)**
- Cat_BlackMat_body, Cat_BlackMat_head, Cat_BlackMat_neck
- Cat_BlackMat_ear_L, Cat_BlackMat_ear_R
- Cat_BlackMat_frontL_leg, Cat_BlackMat_frontR_leg
- Cat_BlackMat_backL_leg, Cat_BlackMat_backR_leg
- Cat_BlackMat_tail, Cat_BlackMat_tailJoint
- Cat_BlackMat_pupil_L, Cat_BlackMat_pupil_R

**Cat_WhiteMat (#FFFFFF)**
- Cat_WhiteMat_earTip_L, Cat_WhiteMat_earTip_R
- Cat_WhiteMat_earSpot_L, Cat_WhiteMat_earSpot_R
- Cat_WhiteMat_chest, Cat_WhiteMat_muzzle
- Cat_WhiteMat_spot_1, Cat_WhiteMat_spot_2, Cat_WhiteMat_tailTip
- Cat_WhiteMat_frontL_paw, Cat_WhiteMat_frontR_paw
- Cat_WhiteMat_backL_paw, Cat_WhiteMat_backR_paw
- Cat_WhiteMat_sclera_L, Cat_WhiteMat_sclera_R
- Cat_WhiteMat_catchlight_L, Cat_WhiteMat_catchlight_R
- Cat_WhiteMat_brow_L, Cat_WhiteMat_brow_R

**Cat_EyeMat (#F2B71A)**
- Cat_EyeMat_iris_L, Cat_EyeMat_iris_R

**Cat_PinkMat (#F29999)**
- Cat_PinkMat_nose

---

## Studio Setup Notes
- Set `Color` on each MeshPart using hex values above
- Set `CanCollide = false` on all face patches (eyes, nose, muzzle, brows, sclera, catchlights)
- Eye layer order front-to-back: catchlight → pupil → iris → sclera
- Use `Neon` material on iris parts for glowing amber eyes, `SmoothPlastic` for everything else
- No rig — wire parts to R15 bones manually in Studio
