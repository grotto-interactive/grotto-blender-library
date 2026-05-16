"""Builder: grotto_apothecary_bottle — tall narrow potion bottle (distinct from canteen + rum flask)."""
import bpy
import bmesh
import math
import os
from mathutils import Vector

ASSET = "grotto_apothecary_bottle"
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


def mat(name, hex_c, rough=0.4, transmission=0.0):
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


def lathe_mesh(name, profile, segments=20):
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

glass_mat = mat("apo_Glass", "#2D4F4A", rough=0.2, transmission=0.25)
stop_mat = mat("apo_Stopper", "#8FA89E", rough=0.15, transmission=0.35)

# Tall potion profile — smooth bulb-to-neck (no separate ring mesh or shoulder bump)
profile = [
    (0.0, 0.065),
    (0.05, 0.095),
    (0.12, 0.11),
    (0.20, 0.102),
    (0.28, 0.082),
    (0.34, 0.058),
    (0.38, 0.046),
    (0.41, 0.040),
    (0.44, 0.036),
]
NECK_TOP = profile[-1][0]
NECK_R = profile[-1][1]

glass = link_part("apo_Glass", lathe_mesh("apo_glass_mesh", profile, 20), glass_mat, root)

# Round glass stopper — sized to neck, seated on lip
bpy.ops.mesh.primitive_uv_sphere_add(segments=12, ring_count=6, radius=NECK_R * 1.15)
stopper = bpy.context.view_layer.objects.active
stopper.name = "apo_Stopper"
stopper.scale = (1.0, 1.0, 1.35)
bpy.ops.object.transform_apply(scale=True)
stopper.data.materials.append(stop_mat)
for c in list(stopper.users_collection):
    c.objects.unlink(stopper)
col.objects.link(stopper)
stopper.parent = root

bpy.context.view_layer.update()
lip_z = max(
    (glass.matrix_world @ v.co).z
    for v in glass.data.vertices
    if math.sqrt(v.co.x ** 2 + v.co.y ** 2) < NECK_R * 1.3
)
bb = [stopper.matrix_world @ Vector(c) for c in stopper.bound_box]
stop_h = max(v.z for v in bb) - min(v.z for v in bb)
from mathutils import Matrix
stopper.matrix_world = Matrix.Translation((0, 0, lip_z + stop_h * 0.38))
bb = [stopper.matrix_world @ Vector(c) for c in stopper.bound_box]
stopper.matrix_world.translation.z += lip_z - min(v.z for v in bb)

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
print("height_m", round(max(v.z for v in pts) - min(v.z for v in pts) + root.location.z, 3))
print("tris", total)
