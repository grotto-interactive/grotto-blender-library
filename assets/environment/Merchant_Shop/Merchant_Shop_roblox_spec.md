# Merchant_Shop — Roblox Spec

**Size:** ~9.2 studs wide × 7.0 studs deep × 6.2 studs tall (environment building)
**Parts:** 55 mesh objects, 6 colors

## Colors

| Material | Description | Hex |
|---|---|---|
| M_Stone | Warm grey stone walls & foundation | #BCAFA8 |
| M_Wood | Dark warm brown wood (floor, door, shelves, counter, sign posts) | #8E6838 |
| M_Roof | Very dark brown shingles | #684D28 |
| M_Sign | Light tan sign board | #D8B360 |
| M_Glass | Clear glass (set Transparency in Studio) | #D9F0FF |
| M_Metal | Dark iron hardware (hinges, knob) | #868075 |

## Parts

### Structure (M_Stone)
| Object | Description |
|---|---|
| Shop_Foundation | Low platform slab the building sits on |
| Shop_Wall_L | Left side wall |
| Shop_Wall_R | Right side wall |
| Shop_Wall_F_L | Front wall — left panel (left of door) |
| Shop_Wall_F_R | Front wall — right panel (right of door) |
| Shop_Wall_F_Top | Front wall — strip above door opening |
| Shop_Wall_B_L | Back wall — left strip (flanking big window) |
| Shop_Wall_B_R | Back wall — right strip |
| Shop_Wall_B_Bot | Back wall — bottom sill strip |
| Shop_Wall_B_Top | Back wall — top strip above window |
| Shop_Gable_F | Front triangular gable above wall top |
| Shop_Gable_B | Back triangular gable above wall top |

### Roof (M_Roof)
| Object | Description |
|---|---|
| Shop_Roof_L | Left slanted roof panel |
| Shop_Roof_R | Right slanted roof panel |

### Wood Interior & Exterior (M_Wood)
| Object | Description |
|---|---|
| Shop_Floor | Interior floor planks |
| Shop_Door | Front door panel — hinges on left, full frame width |
| Shop_Step | Entry step in front of door |
| Shop_Counter | Service counter on right side of room |
| Shop_Counter_Top | Slightly wider counter surface slab |
| Shop_Shelf_L_0 | Left wall shelf — bottom level |
| Shop_Shelf_L_1 | Left wall shelf — middle level |
| Shop_Shelf_L_2 | Left wall shelf — top level |
| Shop_Shelf_R_0 | Right wall shelf — bottom level |
| Shop_Shelf_R_1 | Right wall shelf — middle level |
| Shop_Shelf_R_2 | Right wall shelf — top level |
| Shop_Brace_L_0_* / _1_* / _2_* | Left shelf support brackets (9 total, 3 per shelf level) |
| Shop_Brace_R_0_* / _1_* / _2_* | Right shelf support brackets (9 total, 3 per shelf level) |
| Shop_Window_B_Frame | Big back window wood frame |
| Shop_Window_SL_Frame | Left side wall window frame |
| Shop_Window_SR_Frame | Right side wall window frame |
| Shop_Sign_Post_L | Left sign bracket |
| Shop_Sign_Post_R | Right sign bracket |

### Sign (M_Sign)
| Object | Description |
|---|---|
| Shop_Sign | Hanging sign board above front door |

### Glass (M_Glass)
| Object | Description |
|---|---|
| Shop_Window_B_Glass | Large back wall window glass (nearly full wall) |
| Shop_Window_SL_Glass | Left side wall window glass |
| Shop_Window_SR_Glass | Right side wall window glass |

### Metal Hardware (M_Metal)
| Object | Description |
|---|---|
| Shop_Hinge_T | Top door hinge barrel |
| Shop_Hinge_B | Bottom door hinge barrel |
| Shop_Door_Knob | Door handle knob |

## Studio Notes
- Import `Merchant_Shop.fbx` — 55 separate mesh parts
- Set each part's `Color` property to the hex above
- **Glass parts**: set `Transparency` to ~0.7 and `Material` to `Glass` in Studio
- **Door hinge**: attach a `HingeConstraint` at the left edge of the door frame (X = -0.9 relative to building center) so the door swings open into the building
- **Shop_Hinge_T / Shop_Hinge_B** are visual barrel cylinders only — the actual HingeConstraint attachment point should align with them
- Building faces **-Y** (front door opens toward -Y)
- Shelves run along the Y axis on both side walls — 3 levels at low/mid/high heights
- Counter sits on the right side of the interior with an 0.8-stud gap from the right wall
- Scale is 1 FBX unit = 1 Roblox stud — no rescaling needed on import
