"""Builder: grotto_canoe — rowboat reference plan (smooth oblong overlook)."""
import bpy
import bmesh
import math
import os
from mathutils import Vector

ASSET = "grotto_canoe"
DIR = os.path.join(os.path.dirname(__file__), "..", "assets", "props", ASSET)
BLEND = os.path.join(DIR, f"{ASSET}.blend")
os.makedirs(DIR, exist_ok=True)

# 1 Blender unit = 1 Roblox stud
LENGTH = 8.0
MAX_HALF_BEAM = 1.12
DEPTH = 0.58
FLOOR_Z = 0.10
GUNWALE_Z = 0.50
SEAT_Z = 0.30
SEAT_X = -0.8

for o in list(bpy.data.objects):
    bpy.data.objects.remove(o, do_unlink=True)
for c in list(bpy.data.collections):
    if c.name not in {"Collection", "Scene Collection"}:
        bpy.data.collections.remove(c)

col = bpy.data.collections.new(ASSET)
bpy.context.scene.collection.children.link(col)


def mat_wood(name, hex_c="#8E6838", rough=0.72):
    m = bpy.data.materials.new(name)
    m.use_nodes = True
    bsdf = m.node_tree.nodes.get("Principled BSDF")
    h = hex_c.lstrip("#")
    r, g, b = (int(h[i : i + 2], 16) / 255 for i in (0, 2, 4))
    bsdf.inputs["Base Color"].default_value = (r, g, b, 1)
    bsdf.inputs["Roughness"].default_value = rough
    return m


def plan_half_width(t):
    """
    Top-down silhouette (reference rowboat).
    t=0 sharp bow, t=1 rounded stern; widest ~40% aft of bow.
    Smooth oblong — no diamond corners on port/starboard.
    """
    belly = math.sin(math.pi * t) ** 1.05
    bow = max(0.02, t**0.72)
    stern = 0.36 + 0.64 * min(1.0, (1.0 - t) / 0.22)
    return MAX_HALF_BEAM * bow * stern * (0.22 + 0.78 * belly)


def sheer_gunwale(t):
    """S-curve sheer: slightly higher at bow and stern."""
    return GUNWALE_Z * (0.88 + 0.12 * math.cos(math.pi * t))


def cross_section_yz(half_w, depth, gun):
    """Smooth U (open top): rounded sides, V-bottom."""
    kz = FLOOR_Z - depth
    return [
        (half_w * 0.92, gun * 0.95),
        (half_w * 0.78, FLOOR_Z + 0.06),
        (half_w * 0.40, FLOOR_Z),
        (half_w * 0.12, kz + depth * 0.15),
        (0.0, kz),
        (-half_w * 0.12, kz + depth * 0.15),
        (-half_w * 0.40, FLOOR_Z),
        (-half_w * 0.78, FLOOR_Z + 0.06),
        (-half_w * 0.92, gun * 0.95),
    ]


def rowboat_hull_mesh(stations=10):
    bm = bmesh.new()
    floor_rings, lip_rings, out_rings = [], [], []

    for i in range(stations):
        t = i / max(stations - 1, 1)
        x = (t - 0.5) * LENGTH
        half_w = plan_half_width(t)
        depth = DEPTH * (0.35 + 0.65 * half_w / MAX_HALF_BEAM)
        gun = sheer_gunwale(t)
        prof = cross_section_yz(half_w, depth, gun)

        floor_ring, lip_ring, out_ring = [], [], []
        for y, z in prof:
            lip_ring.append(bm.verts.new((x, y, z)))
            floor_ring.append(bm.verts.new((x, y * 0.68, FLOOR_Z)))
            out_ring.append(bm.verts.new((x, y * 1.05, z - 0.05)))
        floor_rings.append(floor_ring)
        lip_rings.append(lip_ring)
        out_rings.append(out_ring)

    n = len(lip_rings[0])

    def stitch(ring_a, ring_b):
        for j in range(n - 1):
            bm.faces.new((ring_a[j], ring_a[j + 1], ring_b[j + 1], ring_b[j]))

    for i in range(stations - 1):
        stitch(floor_rings[i], floor_rings[i + 1])
        stitch(lip_rings[i], lip_rings[i + 1])
        stitch(out_rings[i], out_rings[i + 1])
        for j in range(n - 1):
            bm.faces.new(
                (
                    floor_rings[i][j],
                    floor_rings[i][j + 1],
                    lip_rings[i][j + 1],
                    lip_rings[i][j],
                )
            )
            bm.faces.new(
                (
                    lip_rings[i][j],
                    lip_rings[i][j + 1],
                    out_rings[i][j + 1],
                    out_rings[i][j],
                )
            )

    bmesh.ops.recalc_face_normals(bm, faces=bm.faces)
    bm.normal_update()
    me = bpy.data.meshes.new("canoe_hull_mesh")
    bm.to_mesh(me)
    bm.free()
    return me


def seat_mesh():
    bm = bmesh.new()
    x, z = SEAT_X, SEAT_Z
    hw = 0.55
    v = [
        bm.verts.new((x - 0.1, -hw, z)),
        bm.verts.new((x + 0.1, -hw, z)),
        bm.verts.new((x + 0.1, hw, z)),
        bm.verts.new((x - 0.1, hw, z)),
        bm.verts.new((x - 0.1, -hw, z + 0.06)),
        bm.verts.new((x + 0.1, -hw, z + 0.06)),
        bm.verts.new((x + 0.1, hw, z + 0.06)),
        bm.verts.new((x - 0.1, hw, z + 0.06)),
    ]
    bm.faces.new(v[:4])
    bm.faces.new(v[4:])
    for i in range(4):
        j = (i + 1) % 4
        bm.faces.new((v[i], v[j], v[j + 4], v[i + 4]))
    bm.normal_update()
    me = bpy.data.meshes.new("canoe_seat_mesh")
    bm.to_mesh(me)
    bm.free()
    return me


def paddle_mesh():
    bm = bmesh.new()
    x, y, z = 0.2, MAX_HALF_BEAM * 0.75, SEAT_Z + 0.08
    shaft = 2.8
    segs = 8
    rings = []
    for zl in (0.0, shaft):
        ring = []
        for s in range(segs):
            a = 2 * math.pi * s / segs
            ring.append(bm.verts.new((x, y + math.cos(a) * 0.04, z + zl)))
        rings.append(ring)
    for j in range(segs):
        jn = (j + 1) % segs
        bm.faces.new((rings[0][j], rings[0][jn], rings[1][jn], rings[1][j]))
    tip = z + shaft
    blade = [
        bm.verts.new((x + 0.35, y - 0.18, tip)),
        bm.verts.new((x + 0.55, y - 0.18, tip)),
        bm.verts.new((x + 0.55, y + 0.18, tip)),
        bm.verts.new((x + 0.35, y + 0.18, tip)),
        bm.verts.new((x + 0.35, y - 0.18, tip + 0.05)),
        bm.verts.new((x + 0.55, y - 0.18, tip + 0.05)),
        bm.verts.new((x + 0.55, y + 0.18, tip + 0.05)),
        bm.verts.new((x + 0.35, y + 0.18, tip + 0.05)),
    ]
    bm.faces.new(blade[:4])
    bm.faces.new(blade[4:])
    for i in range(4):
        j = (i + 1) % 4
        bm.faces.new((blade[i], blade[j], blade[j + 4], blade[i + 4]))
    bm.normal_update()
    me = bpy.data.meshes.new("canoe_paddle_mesh")
    bm.to_mesh(me)
    bm.free()
    return me


root = bpy.data.objects.new(f"GROTTO_{ASSET}", None)
col.objects.link(root)

wood = mat_wood("canoe_Wood", "#8E6838")
wood_dark = mat_wood("canoe_WoodDark", "#6B4E32")

hull = bpy.data.objects.new("canoe_Hull", rowboat_hull_mesh())
hull.data.materials.append(wood)
col.objects.link(hull)
hull.parent = root

seat = bpy.data.objects.new("canoe_Seat", seat_mesh())
seat.data.materials.append(wood_dark)
col.objects.link(seat)
seat.parent = root

paddle = bpy.data.objects.new("canoe_Paddle", paddle_mesh())
paddle.data.materials.append(wood)
col.objects.link(paddle)
paddle.parent = root

seat_empty = bpy.data.objects.new("Seat_Rower", None)
seat_empty.empty_display_type = "PLAIN_AXES"
seat_empty.empty_display_size = 0.25
seat_empty.location = (SEAT_X, 0.0, SEAT_Z + 0.12)
col.objects.link(seat_empty)
seat_empty.parent = root

bow_empty = bpy.data.objects.new("Ref_Bow", None)
bow_empty.empty_display_type = "SINGLE_ARROW"
bow_empty.empty_display_size = 0.45
bow_empty.location = (-LENGTH * 0.5 + 0.15, 0.0, GUNWALE_Z * 0.55)
bow_empty.rotation_euler = (0.0, math.radians(-90), 0.0)
col.objects.link(bow_empty)
bow_empty.parent = root

bpy.context.view_layer.update()
mesh_objs = [o for o in root.children_recursive if o.type == "MESH"]
pts = [o.matrix_world @ Vector(c) for o in mesh_objs for c in o.bound_box]
root.location.z = -min(v.z for v in pts)

bpy.ops.wm.save_as_mainfile(filepath=BLEND)

total = sum(sum(max(2, len(p.vertices) - 2) for p in o.data.polygons) for o in mesh_objs)
print("Saved", BLEND)
print("tris", total, "parts", [o.name for o in mesh_objs])
print("plan L/W ratio", round(LENGTH / (MAX_HALF_BEAM * 2), 2))
