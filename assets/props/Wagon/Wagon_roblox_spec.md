# Wagon — Roblox Spec

**Size:** ~5.6 studs long × 5.0 studs wide × 2.4 studs tall (world prop)
**Parts:** 54 mesh objects, 2 colors

## Parts & Colors

| Object | Material | Color | Hex |
|---|---|---|---|
| Wagon_Bed | M_Wood | Warm Brown | #8E6838 |
| Wagon_Side_L | M_Wood | Warm Brown | #8E6838 |
| Wagon_Side_R | M_Wood | Warm Brown | #8E6838 |
| Wagon_Front | M_Wood | Warm Brown | #8E6838 |
| Wagon_Back | M_Wood | Warm Brown | #8E6838 |
| Wagon_Seat | M_Wood | Warm Brown | #8E6838 |
| Wagon_Tongue | M_Wood | Warm Brown | #8E6838 |
| Wagon_Axle_F | M_Metal | Dark Iron | #605950 |
| Wagon_Axle_B | M_Metal | Dark Iron | #605950 |
| Wagon_Hitch | M_Metal | Dark Iron | #605950 |
| Wheel_FL_Rim | M_Metal | Dark Iron | #605950 |
| Wheel_FL_Wood | M_Wood | Warm Brown | #8E6838 |
| Wheel_FL_Hub | M_Metal | Dark Iron | #605950 |
| Wheel_FL_Spoke_0 – Wheel_FL_Spoke_7 | M_Wood | Warm Brown | #8E6838 |
| Wheel_FR_Rim | M_Metal | Dark Iron | #605950 |
| Wheel_FR_Wood | M_Wood | Warm Brown | #8E6838 |
| Wheel_FR_Hub | M_Metal | Dark Iron | #605950 |
| Wheel_FR_Spoke_0 – Wheel_FR_Spoke_7 | M_Wood | Warm Brown | #8E6838 |
| Wheel_BL_Rim | M_Metal | Dark Iron | #605950 |
| Wheel_BL_Wood | M_Wood | Warm Brown | #8E6838 |
| Wheel_BL_Hub | M_Metal | Dark Iron | #605950 |
| Wheel_BL_Spoke_0 – Wheel_BL_Spoke_7 | M_Wood | Warm Brown | #8E6838 |
| Wheel_BR_Rim | M_Metal | Dark Iron | #605950 |
| Wheel_BR_Wood | M_Wood | Warm Brown | #8E6838 |
| Wheel_BR_Hub | M_Metal | Dark Iron | #605950 |
| Wheel_BR_Spoke_0 – Wheel_BR_Spoke_7 | M_Wood | Warm Brown | #8E6838 |

## Studio Notes
- Import `Wagon.fbx` — 54 separate mesh parts
- Set each part's `Color` property to the hex value above
- **Wagon_Bed** is the flat floor of the wagon box
- **Wagon_Side_L / Wagon_Side_R** are the long plank side walls
- **Wagon_Front / Wagon_Back** are the short end walls of the box
- **Wagon_Seat** is the driver's bench at the front of the box
- **Wagon_Tongue** is the long wooden hitch arm extending forward for the horse
- **Wagon_Axle_F / Wagon_Axle_B** are the iron axle rods spanning the full wheel width
- **Wagon_Hitch** is the metal bracket connecting the tongue to the front axle
- **Wheel_XX_Rim** is the outer iron tire ring of each wheel (FL=front-left, FR=front-right, BL=back-left, BR=back-right)
- **Wheel_XX_Wood** is the inner wooden face disc of each wheel
- **Wheel_XX_Hub** is the center iron hub cap where the axle passes through
- **Wheel_XX_Spoke_0–7** are the 8 flat wooden spokes radiating from hub to rim
- Wagon sits flat on the ground — wheels touch Z=0
- Scale is 1 FBX unit = 1 Roblox stud — no rescaling needed on import
- Place as a static world prop or animate wheel rotation for a moving wagon
