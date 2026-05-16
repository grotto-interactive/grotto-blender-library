"""One-shot builder: grotto_pirate_rum_flask — run inside Blender on empty or overwrite."""
import bpy
import bmesh
import math
import os
from mathutils import Vector

ASSET = "grotto_pirate_rum_flask"
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


def mat(name, hex_c, rough=0.45, metallic=0.0):
    m = bpy.data.materials.new(name)
    m.use_nodes = True
    bsdf = m.node_tree.nodes.get("Principled BSDF")
    h = hex_c.lstrip("#")
    r, g, b = (int(h[i : i + 2], 16) / 255 for i in (0, 2, 4))
    bsdf.inputs["Base Color"].default_value = (r, g, b, 1)
    bsdf.inputs["Roughness"].default_value = rough
    bsdf.inputs["Metallic"].default_value = metallic
    return m


def lathe_mesh(name, profile, segments=24, z_offset=0.0):
    """profile: list of (z, radius) from bottom to top."""
    bm = bmesh.new()
    rings = []
    for z, r in profile:
        ring = []
        for i in range(segments):
            a = 2 * math.pi * i / segments
            ring.append(bm.verts.new((r * math.cos(a), r * math.sin(a), z + z_offset)))
        rings.append(ring)
    bm.verts.ensure_lookup_table()
    for i in range(len(rings) - 1):
        r0, r1 = rings[i], rings[i + 1]
        for j in range(segments):
            jn = (j + 1) % segments
            bm.faces.new((r0[j], r0[jn], r1[jn], r1[j]))
    # caps
    bm.faces.new(rings[0])
    bm.faces.new(list(reversed(rings[-1])))
    bm.normal_update()
    me = bpy.data.meshes.new(name)
    bm.to_mesh(me)
    bm.free()
    return me


def link_mesh(name, mesh, mat_obj, parent):
    o = bpy.data.objects.new(name, mesh)
    col.objects.link(o)
    o.data.materials.append(mat_obj)
    o.parent = parent
    return o


def parent_to_asset(obj, parent):
    """Keep all export meshes in the asset collection (not default Collection)."""
    for c in list(obj.users_collection):
        if obj.name in c.objects:
            c.objects.unlink(obj)
    if obj.name not in col.objects:
        col.objects.link(obj)
    obj.parent = parent


# Parent empty
root = bpy.data.objects.new(f"GROTTO_{ASSET}", None)
col.objects.link(root)

glass_mat = mat("rum_Glass", "#4A3020", rough=0.25, metallic=0.05)
cork_mat = mat("rum_Cork", "#6B4E30", rough=0.85)
wax_mat = mat("rum_WaxSeal", "#8B1E18", rough=0.6)

# Squat rum bottle profile (meters)
profile = [
    (0.0, 0.11),
    (0.04, 0.13),
    (0.10, 0.145),
    (0.16, 0.14),
    (0.22, 0.11),
    (0.26, 0.075),
    (0.29, 0.048),
    (0.31, 0.038),
    (0.33, 0.036),
]
NECK_TOP = profile[-1][0]
NECK_R = profile[-1][1]

glass_mesh = lathe_mesh("rum_glass_mesh", profile, segments=20)
link_mesh("rum_Glass", glass_mesh, glass_mat, root)

# Cork — short dome on neck
bpy.ops.mesh.primitive_uv_sphere_add(
    segments=16, ring_count=8, radius=NECK_R * 1.15, location=(0, 0, NECK_TOP + NECK_R * 0.9)
)
cork = bpy.context.view_layer.objects.active
cork.name = "rum_Cork"
cork.scale = (1.0, 1.0, 0.75)
bpy.ops.object.transform_apply(scale=True)
cork.data.materials.append(cork_mat)
parent_to_asset(cork, root)
# Seat cork: align bottom slightly into neck opening (not floating above)
bpy.context.view_layer.update()
from mathutils import Vector as _V

bb_c = [cork.matrix_world @ _V(c) for c in cork.bound_box]
cork_h = max(v.z for v in bb_c) - min(v.z for v in bb_c)
cork.location.z += NECK_TOP - min(v.z for v in bb_c) - cork_h * 0.08

# Wax drip collar
bpy.ops.mesh.primitive_torus_add(
    major_segments=10,
    minor_segments=5,
    major_radius=NECK_R * 1.05,
    minor_radius=0.012,
    location=(0, 0, NECK_TOP + 0.01),
)
wax = bpy.context.view_layer.objects.active
wax.name = "rum_WaxSeal"
wax.data.materials.append(wax_mat)
parent_to_asset(wax, root)

# Floor pivot
bpy.context.view_layer.update()
mesh_objs = [o for o in root.children_recursive if o.type == "MESH"]
pts = []
for o in mesh_objs:
    for c in o.bound_box:
        pts.append(o.matrix_world @ Vector(c))
min_z = min(v.z for v in pts)
root.location.z = -min_z

bpy.ops.wm.save_as_mainfile(filepath=BLEND)
print("Saved", BLEND)
print("height_m", round(max(v.z for v in pts) - min_z, 3))
