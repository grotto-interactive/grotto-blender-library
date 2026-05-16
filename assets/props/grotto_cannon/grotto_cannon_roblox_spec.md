# Grotto Cannon — Roblox Spec Doc

**Asset:** grotto_cannon  
**Category:** Props  
**File:** `grotto_cannon.blend` / `grotto_cannon.fbx`  
**Scale:** 1 Blender unit = 1 Roblox stud  
**Overall Dimensions:** ~2.4 W × 4.5 D × 1.8 H studs  
**Intended use:** Environmental prop — pirate dock, ship deck, Seed Harbor

---

## Materials & Hex Colors

| Material Name | Hex Color | Roblox Material | Notes                                              |
|---------------|-----------|-----------------|--------------------------------------------------- |
| Cannon_Iron   | `#3A3A3A` | SmoothPlastic   | Dark iron gray — barrel, bands, axles, hubs, pins  |
| Cannon_Wood   | `#6B4226` | SmoothPlastic   | Dark reddish brown — carriage cheeks, cross braces, wheels |
| Cannon_Bore   | `#0A0A0A` | SmoothPlastic   | Near-black — bore disk at muzzle, sells hollow look |

---

## Object List

### Iron Parts (`#3A3A3A`)
| Object                  | Description                              |
|-------------------------|------------------------------------------|
| Cannon_Barrel           | Main barrel cylinder                     |
| Cannon_Muzzle           | Wider ring at muzzle end                 |
| Cannon_Band_1           | Decorative band near muzzle              |
| Cannon_Band_2           | Decorative band at midpoint              |
| Cannon_Breech           | Wider section at breech end              |
| Cannon_Cascabel         | Ball at very back of barrel              |
| Cannon_TrunnionPin_L    | Left trunnion pin (barrel to carriage)   |
| Cannon_TrunnionPin_R    | Right trunnion pin (barrel to carriage)  |
| Cannon_AxleFront        | Front axle rod                           |
| Cannon_AxleRear         | Rear axle rod                            |
| Cannon_Hub_1–4          | Wheel hub caps (4 total)                 |
| Cannon_Bore             | Near-black bore disk at muzzle face      |

### Wood Parts (`#6B4226`)
| Object                  | Description                              |
|-------------------------|------------------------------------------|
| Cannon_CheekL           | Left carriage side plank                 |
| Cannon_CheekR           | Right carriage side plank                |
| Cannon_CrossFront       | Front cross brace                        |
| Cannon_CrossMid         | Middle cross brace                       |
| Cannon_CrossRear        | Rear cross brace                         |
| Cannon_Wheel_1–4        | Four carriage wheels                     |

---

## Layout Notes

- **Barrel** points along the Y axis — muzzle at -Y (front), cascabel at +Y (rear).
- **Carriage** sits flat on the ground. Cheeks run the length of the carriage on each side.
- **Wheels** are at all four corners. Axles pass through the cheeks at Z=0.55.
- **Trunnion pins** protrude from both sides of the barrel at the balance point, connecting the barrel to the carriage cheeks.
- Barrel is seated into the top of the carriage cheeks — no manual alignment needed in Studio.

---

## Studio Import Notes

1. **FBX is ready to import** — no conversion steps needed.
2. **Scale** — import at 1.0. Each unit = 1 stud.
3. **Apply materials by name** — all `Cannon_Iron` parts get `#3A3A3A`, all `Cannon_Wood` parts get `#6B4226`. Both SmoothPlastic.
4. **Bore** — apply `#0A0A0A` SmoothPlastic to `Cannon_Bore`. The near-black color simulates a hollow barrel opening at the muzzle.
5. **Object count** — ~22 objects. Consider merging by material in Studio if performance is a concern.
5. **Orientation** — cannon fires in the -Z direction in Roblox (the -Y axis in Blender maps to -Z in Studio after FBX import with standard settings).

---

*Asset created by Tasha — Grotto Interactive LLC*  
*Spec written: 2026-05-09 — Updated: 2026-05-09*
