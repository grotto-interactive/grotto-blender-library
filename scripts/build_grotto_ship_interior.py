"""Add R15 walkable cargo hold + deck hatch to grotto_ship."""
import bpy
import bmesh
import math
import os
from mathutils import Vector

ASSET = "grotto_ship"
DIR = os.path.join(os.path.dirname(__file__), "..", "assets", "props", ASSET)
BLEND = os.path.join(DIR, f"{ASSET}.blend")

# Cargo hold (studs) — floor low in bilge, ~5.1 studs headroom to deck underside
HOLD_X0, HOLD_X1 = -1.2, 3.2
HOLD_Y = 1.85
FLOOR_Z = -3.85
CEILING_Z = 1.22
HATCH_X, HATCH_Y = 0.35, 0.0
HATCH_HALF = 0.95
DECK_Z = 1.52

# Main deck walkable footprint (open air)
DECK_WALK_X0, DECK_WALK_X1 = -2.8, 3.4
DECK_WALK_Y = 2.35
DECK_WALK_Z = DECK_Z + 0.04


def mat_get(name, hex_c, rough=0.72):
    m = bpy.data.materials.get(name)
    if m:
        return m
    m = bpy.data.materials.new(name)
    m.use_nodes = True
    bsdf = m.node_tree.nodes.get("Principled BSDF")
    h = hex_c.lstrip("#")
    r, g, b = (int(h[i : i + 2], 16) / 255 for i in (0, 2, 4))
    bsdf.inputs["Base Color"].default_value = (r, g, b, 1)
    bsdf.inputs["Roughness"].default_value = rough
    return m


def box_mesh(name, sx, sy, sz):
    bm = bmesh.new()
    bmesh.ops.create_cube(bm, size=1.0)
    bmesh.ops.scale(bm, verts=bm.verts, vec=(sx, sy, sz))
    bmesh.ops.translate(bm, verts=bm.verts, vec=(0, 0, sz * 0.5))
    me = bpy.data.meshes.new(name)
    bm.to_mesh(me)
    bm.free()
    return me


def wall_mesh(name, length, height, thickness):
    bm = bmesh.new()
    bmesh.ops.create_cube(bm, size=1.0)
    bmesh.ops.scale(bm, verts=bm.verts, vec=(length, thickness, height))
    bmesh.ops.translate(bm, verts=bm.verts, vec=(0, 0, height * 0.5))
    me = bpy.data.meshes.new(name)
    bm.to_mesh(me)
    bm.free()
    return me


def ladder_mesh(name, height, width=0.55, rungs=9):
    bm = bmesh.new()
    rail_t = 0.06
    depth = 0.12
    for side in (-1, 1):
        y = side * (width * 0.5)
        bmesh.ops.create_cube(bm, size=1.0)
        last = bm.verts[-8:]
        bmesh.ops.scale(bm, verts=last, vec=(rail_t, depth, height))
        bmesh.ops.translate(bm, verts=last, vec=(0, y, height * 0.5))
    step_h = height / (rungs + 1)
    for i in range(rungs):
        z = step_h * (i + 1)
        bmesh.ops.create_cube(bm, size=1.0)
        last = bm.verts[-8:]
        bmesh.ops.scale(bm, verts=last, vec=(width * 0.85, depth * 1.2, 0.05))
        bmesh.ops.translate(bm, verts=last, vec=(0, 0, z))
    me = bpy.data.meshes.new(name)
    bm.to_mesh(me)
    bm.free()
    return me


def hatch_frame_mesh(name, outer, inner, height):
    bm = bmesh.new()
    rail = (outer - inner) * 0.5
    specs = [
        ((outer, rail, height), (0, (outer + inner) * 0.25, height * 0.5)),
        ((outer, rail, height), (0, -(outer + inner) * 0.25, height * 0.5)),
        ((rail, outer, height), ((outer + inner) * 0.25, 0, height * 0.5)),
        ((rail, outer, height), (-(outer + inner) * 0.25, 0, height * 0.5)),
    ]
    for (sx, sy, sz), (ox, oy, oz) in specs:
        bmesh.ops.create_cube(bm, size=1.0)
        last = bm.verts[-8:]
        bmesh.ops.scale(bm, verts=last, vec=(sx, sy, sz))
        bmesh.ops.translate(bm, verts=last, vec=(ox, oy, oz))
    me = bpy.data.meshes.new(name)
    bm.to_mesh(me)
    bm.free()
    return me


def cut_deck_hatch():
    deck = bpy.data.objects.get("Deck_Main")
    if not deck or deck.type != "MESH":
        return
    me = deck.data
    bm = bmesh.new()
    bm.from_mesh(me)
    mw = deck.matrix_world
    inv = mw.inverted()
    remove = []
    for f in bm.faces:
        c = mw @ f.calc_center_median()
        if (
            abs(c.x - HATCH_X) < HATCH_HALF
            and abs(c.y - HATCH_Y) < HATCH_HALF
            and c.z > DECK_Z - 0.15
        ):
            remove.append(f)
    if remove:
        bmesh.ops.delete(bm, geom=remove, context="FACES")
        bm.to_mesh(me)
        me.update()
    bm.free()


def remove_prior_interior():
    prefixes = (
        "ship_Cargo",
        "ship_DeckHatch",
        "ship_Ladder",
        "ship_Interior",
        "Ref_Cargo",
        "Ref_DeckWalk",
        "Ref_Hatch",
    )
    for o in list(bpy.data.objects):
        if any(o.name.startswith(p) for p in prefixes):
            bpy.data.objects.remove(o, do_unlink=True)


bpy.ops.wm.open_mainfile(filepath=BLEND)
remove_prior_interior()

root = bpy.data.objects.get(f"GROTTO_{ASSET}")
if not root:
    raise RuntimeError(f"GROTTO_{ASSET} not found")

mat_hull = mat_get("M_Hull", "#331607")
mat_deck = mat_get("M_Deck", "#996B33")

hold_len = HOLD_X1 - HOLD_X0
hold_ctr_x = (HOLD_X0 + HOLD_X1) * 0.5
hold_h = CEILING_Z - FLOOR_Z

parts = []

# Cargo deck floor
floor = bpy.data.objects.new(
    "ship_CargoDeck_Floor",
    box_mesh("ship_cargo_floor", hold_len, HOLD_Y * 2, 0.12),
)
floor.location = (hold_ctr_x, 0, FLOOR_Z)
floor.data.materials.append(mat_deck)
parts.append(floor)

# Inner bulkheads (thin walls)
wall_h = hold_h
for name, loc, rot_z, length in [
    ("ship_CargoWall_Port", (hold_ctr_x, HOLD_Y, FLOOR_Z), 0, hold_len),
    ("ship_CargoWall_Stbd", (hold_ctr_x, -HOLD_Y, FLOOR_Z), 0, hold_len),
    ("ship_CargoWall_Bow", (HOLD_X1, 0, FLOOR_Z), math.pi / 2, HOLD_Y * 2),
    ("ship_CargoWall_Stern", (HOLD_X0, 0, FLOOR_Z), math.pi / 2, HOLD_Y * 2),
]:
    w = bpy.data.objects.new(name, wall_mesh(name, length, wall_h, 0.1))
    w.location = loc
    w.rotation_euler = (0, 0, rot_z)
    w.data.materials.append(mat_hull)
    parts.append(w)

# Ceiling plane (deck underside visual)
ceil = bpy.data.objects.new(
    "ship_CargoDeck_Ceiling",
    box_mesh("ship_cargo_ceil", hold_len * 0.98, HOLD_Y * 1.96, 0.06),
)
ceil.location = (hold_ctr_x, 0, CEILING_Z)
ceil.data.materials.append(mat_hull)
parts.append(ceil)

# Hatch frame on main deck
frame = bpy.data.objects.new(
    "ship_DeckHatch_Frame",
    hatch_frame_mesh("ship_hatch_frame", HATCH_HALF * 2.1, HATCH_HALF * 1.5, 0.14),
)
frame.location = (HATCH_X, HATCH_Y, DECK_Z + 0.02)
frame.data.materials.append(mat_hull)
parts.append(frame)

# Ladder: deck down to cargo floor
ladder_h = DECK_Z - FLOOR_Z - 0.2
ladder = bpy.data.objects.new("ship_Ladder", ladder_mesh("ship_ladder", ladder_h))
ladder.location = (HATCH_X + 0.55, HATCH_Y, FLOOR_Z + 0.1)
ladder.data.materials.append(mat_deck)
parts.append(ladder)

# Optional storage shelf along stern bulkhead
shelf = bpy.data.objects.new(
    "ship_CargoShelf",
    box_mesh("ship_cargo_shelf", 1.6, 0.35, 0.08),
)
shelf.location = (HOLD_X0 + 0.9, -HOLD_Y + 0.25, FLOOR_Z + 1.1)
shelf.data.materials.append(mat_deck)
parts.append(shelf)

shelf2 = shelf.copy()
shelf2.data = shelf.data
shelf2.name = "ship_CargoShelf_02"
shelf2.location = (HOLD_X0 + 0.9, HOLD_Y - 0.25, FLOOR_Z + 1.1)
parts.append(shelf2)

for p in parts:
    bpy.context.scene.collection.objects.link(p)
    p.parent = root

cut_deck_hatch()

# Reference empties for Studio scripting
def add_empty(name, loc, display="PLAIN_AXES", size=0.35):
    e = bpy.data.objects.new(name, None)
    e.empty_display_type = display
    e.empty_display_size = size
    e.location = loc
    bpy.context.scene.collection.objects.link(e)
    e.parent = root
    return e


add_empty("Ref_Hatch", (HATCH_X, HATCH_Y, DECK_Z + 0.15), "SPHERE", 0.4)
add_empty(
    "Ref_CargoBounds",
    (hold_ctr_x, 0, (FLOOR_Z + CEILING_Z) * 0.5),
    "CUBE",
    max(hold_len, HOLD_Y * 2, hold_h) * 0.5,
)
add_empty(
    "Ref_DeckWalkBounds",
    ((DECK_WALK_X0 + DECK_WALK_X1) * 0.5, 0, DECK_WALK_Z),
    "CUBE",
    max(DECK_WALK_X1 - DECK_WALK_X0, DECK_WALK_Y * 2) * 0.5,
)

bpy.ops.wm.save_as_mainfile(filepath=BLEND)

mesh_objs = [o for o in root.children_recursive if o.type == "MESH"]
total = sum(sum(max(2, len(p.vertices) - 2) for p in o.data.polygons) for o in mesh_objs)
print("Saved", BLEND)
print("Added interior parts:", [p.name for p in parts])
print(
    "Cargo hold clear:",
    round(hold_len, 2),
    "x",
    round(HOLD_Y * 2, 2),
    "x",
    round(hold_h, 2),
    "studs",
)
print("Scene mesh tris (approx):", total)
