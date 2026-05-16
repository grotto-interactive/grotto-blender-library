"""Builder: grotto_conch_shell — unified spiral conch (one continuous shell)."""
import bpy
import bmesh
import math
import os
from mathutils import Vector

ASSET = "grotto_conch_shell"
DIR = os.path.join(os.path.dirname(__file__), "..", "assets", "environment", ASSET)
BLEND = os.path.join(DIR, f"{ASSET}.blend")
os.makedirs(DIR, exist_ok=True)

for o in list(bpy.data.objects):
    bpy.data.objects.remove(o, do_unlink=True)
for c in list(bpy.data.collections):
    if c.name not in {"Collection", "Scene Collection"}:
        bpy.data.collections.remove(c)

col = bpy.data.collections.new(ASSET)
bpy.context.scene.collection.children.link(col)


def mat(name, hex_c, rough=0.75):
    m = bpy.data.materials.new(name)
    m.use_nodes = True
    bsdf = m.node_tree.nodes.get("Principled BSDF")
    h = hex_c.lstrip("#")
    r, g, b = (int(h[i : i + 2], 16) / 255 for i in (0, 2, 4))
    bsdf.inputs["Base Color"].default_value = (r, g, b, 1)
    bsdf.inputs["Roughness"].default_value = rough
    return m


def link_part(name, mesh, material, parent):
    o = bpy.data.objects.new(name, mesh)
    col.objects.link(o)
    o.data.materials.append(material)
    o.parent = parent
    return o


def unified_conch_mesh(steps=26, turns=1.65, tube_segments=10):
    """
    One spiral shell: wide aperture tapering to a pointed spire tip.
    Single continuous tube — no separate body + curly tail.
    """
    bm = bmesh.new()
    centers = []

    for i in range(steps):
        t = i / max(steps - 1, 1)
        ang = t * turns * 2 * math.pi
        # Spiral path rises and moves outward gently
        path_r = 0.018 + t * 0.055
        z = 0.01 + t * 0.15
        centers.append(Vector((path_r * math.cos(ang), path_r * math.sin(ang), z)))

    rings = []
    for i, center in enumerate(centers):
        t = i / max(steps - 1, 1)
        # Wide mouth at t=0, needle tip at t=1
        tr = 0.078 * (1.0 - t) ** 0.55 + 0.006
        # Slightly oval cross-section at the aperture
        scale_y = 1.0 + 0.22 * (1.0 - t)

        i0 = max(i - 1, 0)
        i1 = min(i + 1, steps - 1)
        tangent = (centers[i1] - centers[i0]).normalized()
        up = Vector((0, 0, 1))
        side = tangent.cross(up).normalized()
        if side.length < 0.01:
            side = Vector((1, 0, 0))
        fwd = side.cross(tangent).normalized()

        ring = []
        for s in range(tube_segments):
            a = 2 * math.pi * s / tube_segments
            off = side * (tr * math.cos(a)) + fwd * (tr * math.sin(a) * scale_y)
            ring.append(bm.verts.new(center + off))
        rings.append(ring)

    bm.verts.ensure_lookup_table()
    for i in range(len(rings) - 1):
        r0, r1 = rings[i], rings[i + 1]
        for j in range(tube_segments):
            jn = (j + 1) % tube_segments
            bm.faces.new((r0[j], r0[jn], r1[jn], r1[j]))
    # Cap the tip
    bm.faces.new(list(reversed(rings[-1])))
    bm.normal_update()
    me = bpy.data.meshes.new("conch_shell_mesh")
    bm.to_mesh(me)
    bm.free()
    return me


root = bpy.data.objects.new(f"GROTTO_{ASSET}", None)
col.objects.link(root)

shell_mat = mat("conch_Shell", "#E8D8B8", rough=0.8)
lip_mat = mat("conch_Lip", "#E8B8A0", rough=0.7)

link_part("conch_Shell", unified_conch_mesh(), shell_mat, root)

# Inner lip at the wide opening (first ring region)
bpy.ops.mesh.primitive_torus_add(
    major_segments=12,
    minor_segments=5,
    major_radius=0.068,
    minor_radius=0.009,
    location=(0.018, 0.0, 0.028),
)
lip = bpy.context.view_layer.objects.active
lip.name = "conch_Lip"
lip.scale = (1.15, 0.85, 1.0)
bpy.ops.object.transform_apply(scale=True)
lip.data.materials.append(lip_mat)
for c in list(lip.users_collection):
    c.objects.unlink(lip)
col.objects.link(lip)
lip.parent = root

# Rest on seafloor — aperture edge down, spire tip up
root.rotation_euler = (math.radians(72), math.radians(8), math.radians(18))

bpy.context.view_layer.update()
mesh_objs = [o for o in root.children_recursive if o.type == "MESH"]
pts = [o.matrix_world @ Vector(c) for o in mesh_objs for c in o.bound_box]
root.location.z = -min(v.z for v in pts)

bpy.ops.wm.save_as_mainfile(filepath=BLEND)


def tri_count(data):
    return sum(max(2, len(p.vertices) - 2) for p in data.polygons)


total = sum(tri_count(o.data) for o in mesh_objs)
print("Saved", BLEND)
print("tris", total, "parts", [o.name for o in mesh_objs])
