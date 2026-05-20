"""Widen door and raise Merchant_Shop for full R15 walk/stand clearance."""
import bpy
import bmesh
import os

BLEND = os.path.join(
    os.path.dirname(__file__),
    "..",
    "assets",
    "environment",
    "Merchant_Shop",
    "Merchant_Shop.blend",
)

SILL_Z = 0.4
HEIGHT_ADD = 2.0
DOOR_WIDTH = 2.4
DOOR_HEIGHT = 5.6
WALL_F_L_X = -2.75
WALL_F_R_X = 2.75


def raise_verts(obj, delta):
    bm = bmesh.new()
    bm.from_mesh(obj.data)
    for v in bm.verts:
        if v.co.z > SILL_Z + 0.02:
            v.co.z += delta
    bm.to_mesh(obj.data)
    obj.data.update()
    bm.free()


def scale_verts_x(obj, target_width):
    bm = bmesh.new()
    bm.from_mesh(obj.data)
    xs = [v.co.x for v in bm.verts]
    cur = max(xs) - min(xs)
    if cur < 1e-6:
        bm.free()
        return
    sx = target_width / cur
    cx = (max(xs) + min(xs)) * 0.5
    for v in bm.verts:
        v.co.x = cx + (v.co.x - cx) * sx
    bm.to_mesh(obj.data)
    obj.data.update()
    bm.free()


def scale_verts_z(obj, target_height, base_z=SILL_Z):
    bm = bmesh.new()
    bm.from_mesh(obj.data)
    zs = [v.co.z for v in bm.verts]
    cur = max(zs) - min(zs)
    if cur < 1e-6:
        bm.free()
        return
    sz = target_height / cur
    for v in bm.verts:
        if v.co.z > base_z + 0.02:
            v.co.z = base_z + (v.co.z - base_z) * sz
    bm.to_mesh(obj.data)
    obj.data.update()
    bm.free()


bpy.ops.wm.open_mainfile(filepath=BLEND)

raise_names = (
    "Shop_Wall_",
    "Shop_Gable_",
    "Shop_Roof_",
    "Shop_Window_",
    "Shop_Shelf_",
    "Shop_Brace_",
    "Shop_Counter",
    "Shop_Sign",
    "Shop_Hinge_",
    "Shop_Door_Knob",
)

for o in bpy.data.objects:
    if o.type != "MESH":
        continue
    if any(o.name.startswith(p) for p in raise_names):
        raise_verts(o, HEIGHT_ADD)
    if o.name == "Shop_Wall_F_Top":
        o.location.x = 0.0
        o.location.z = 5.2
        scale_verts_x(o, DOOR_WIDTH)
        scale_verts_z(o, 1.2, base_z=o.location.z - 0.6)

# Front wall panels — widen door gap
bpy.data.objects["Shop_Wall_F_L"].location.x = WALL_F_L_X
bpy.data.objects["Shop_Wall_F_R"].location.x = WALL_F_R_X

# Door — wider and taller
door = bpy.data.objects["Shop_Door"]
door.location.x = 0.0
door.location.y = -3.05
door.location.z = SILL_Z
scale_verts_x(door, DOOR_WIDTH)
scale_verts_z(door, DOOR_HEIGHT, base_z=SILL_Z)

# Hinges follow door edge
for name, z in (("Shop_Hinge_T", 2.85 + HEIGHT_ADD), ("Shop_Hinge_B", 0.8)):
    h = bpy.data.objects[name]
    h.location.x = -0.9
    h.location.z = z

knob = bpy.data.objects["Shop_Door_Knob"]
knob.location.x = 0.68 + (DOOR_WIDTH - 1.8) * 0.25
knob.location.z = 1.55 + HEIGHT_ADD * 0.5

bpy.context.view_layer.update()
bpy.ops.wm.save_as_mainfile(filepath=BLEND)

# Quick validation
from mathutils import Vector

floor = bpy.data.objects["Shop_Floor"]
floor_top = max((floor.matrix_world @ Vector(c)).z for c in floor.bound_box)
wl = bpy.data.objects["Shop_Wall_L"]
wall_top = max((wl.matrix_world @ Vector(c)).z for c in wl.bound_box)
wfl = bpy.data.objects["Shop_Wall_F_L"]
wfr = bpy.data.objects["Shop_Wall_F_R"]
gap = min((wfr.matrix_world @ Vector(c)).x for c in wfr.bound_box) - max(
    (wfl.matrix_world @ Vector(c)).x for c in wfl.bound_box
)
print("Saved", BLEND)
print("Door gap width:", round(gap, 2), "studs")
print("Interior height (floor top to wall top):", round(wall_top - floor_top, 2), "studs")
