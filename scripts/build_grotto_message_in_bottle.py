"""Builder: grotto_message_in_bottle — glass bottle with rolled scroll + cork."""
import bpy
import bmesh
import math
import os
from mathutils import Vector, Euler

ASSET = "grotto_message_in_bottle"
DIR = os.path.join(os.path.dirname(__file__), "..", "assets", "props", ASSET)
BLEND = os.path.join(DIR, f"{ASSET}.blend")
os.makedirs(DIR, exist_ok=True)

for o in list(bpy.data.objects):
    bpy.data.objects.remove(o, do_unlink=True)
for c in list(bpy.data.collections):
    if c.name not in {"Collection", "Scene Collection"}:
        bpy.data.collections.remove(c)

col = bpy.data.collections.new(ASSET)
bpy.context.scene.collection.children.link(col)


def mat(name, hex_c, rough=0.45, transmission=0.0):
    m = bpy.data.materials.new(name)
    m.use_nodes = True
    bsdf = m.node_tree.nodes.get("Principled BSDF")
    h = hex_c.lstrip("#")
    r, g, b = (int(h[i : i + 2], 16) / 255 for i in (0, 2, 4))
    bsdf.inputs["Base Color"].default_value = (r, g, b, 1)
    bsdf.inputs["Roughness"].default_value = rough
    if transmission > 0 and "Transmission Weight" in bsdf.inputs:
        bsdf.inputs["Transmission Weight"].default_value = transmission
    return m


def lathe_mesh(name, profile, segments=18):
    bm = bmesh.new()
    rings = []
    for z, r in profile:
        ring = []
        for i in range(segments):
            a = 2 * math.pi * i / segments
            ring.append(bm.verts.new((r * math.cos(a), r * math.sin(a), z)))
        rings.append(ring)
    bm.verts.ensure_lookup_table()
    for i in range(len(rings) - 1):
        r0, r1 = rings[i], rings[i + 1]
        for j in range(segments):
            jn = (j + 1) % segments
            bm.faces.new((r0[j], r0[jn], r1[jn], r1[j]))
    bm.faces.new(rings[0])
    bm.faces.new(list(reversed(rings[-1])))
    bm.normal_update()
    me = bpy.data.meshes.new(name)
    bm.to_mesh(me)
    bm.free()
    return me


def link_part(name, mesh, material, parent):
    o = bpy.data.objects.new(name, mesh)
    col.objects.link(o)
    o.data.materials.append(material)
    o.parent = parent
    return o


root = bpy.data.objects.new(f"GROTTO_{ASSET}", None)
col.objects.link(root)

glass_mat = mat("msg_Glass", "#8CB8A8", rough=0.18, transmission=0.35)
scroll_mat = mat("msg_Scroll", "#F2E6C8", rough=0.75)

# Classic message-bottle silhouette — taller neck (~0.44 m)
profile = [
    (0.0, 0.055),
    (0.04, 0.078),
    (0.10, 0.092),
    (0.17, 0.094),
    (0.23, 0.082),
    (0.27, 0.068),   # shoulder
    (0.30, 0.048),
    (0.34, 0.034),   # neck
    (0.38, 0.030),
    (0.41, 0.028),
    (0.44, 0.028),   # lip
]
NECK_R = profile[-1][1]

glass = link_part("msg_Glass", lathe_mesh("msg_glass_mesh", profile, 18), glass_mat, root)

# Rolled scroll in belly — vertical roll (open neck, no cork)
scroll_z = 0.15
bpy.ops.mesh.primitive_cylinder_add(
    vertices=10, radius=0.014, depth=0.14, location=(0.0, 0.0, scroll_z)
)
scroll = bpy.context.view_layer.objects.active
scroll.name = "msg_Scroll"
scroll.rotation_euler = Euler((math.radians(6), 0.0, math.radians(4)), "XYZ")
bpy.ops.object.transform_apply(rotation=True)
scroll.data.materials.append(scroll_mat)
for c in list(scroll.users_collection):
    c.objects.unlink(scroll)
col.objects.link(scroll)
scroll.parent = root

# Floor pivot
bpy.context.view_layer.update()
mesh_objs = [o for o in root.children_recursive if o.type == "MESH"]
pts = [o.matrix_world @ Vector(c) for o in mesh_objs for c in o.bound_box]
root.location.z = -min(v.z for v in pts)

bpy.ops.wm.save_as_mainfile(filepath=BLEND)


def tri_count(data):
    return sum(max(2, len(p.vertices) - 2) for p in data.polygons)


total = sum(tri_count(o.data) for o in mesh_objs)
print("Saved", BLEND)
print("height_m", round(max(v.z for v in pts) - min(v.z for v in pts), 3))
print("tris", total)
for o in mesh_objs:
    print(" ", o.name, tri_count(o.data))
