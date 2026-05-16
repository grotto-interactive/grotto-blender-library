"""Builder: grotto_nautilus_shell — planispiral chambered nautilus (one mesh)."""
import bpy
import bmesh
import math
import os
from mathutils import Vector

ASSET = "grotto_nautilus_shell"
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


def mat(name, hex_c, rough=0.42):
    m = bpy.data.materials.new(name)
    m.use_nodes = True
    bsdf = m.node_tree.nodes.get("Principled BSDF")
    h = hex_c.lstrip("#")
    r, g, b = (int(h[i : i + 2], 16) / 255 for i in (0, 2, 4))
    bsdf.inputs["Base Color"].default_value = (r, g, b, 1)
    bsdf.inputs["Roughness"].default_value = rough
    bsdf.inputs["Specular IOR Level"].default_value = 0.35
    return m


def unified_nautilus_mesh(steps=28, turns=2.65, tube_segments=12):
    """Planispiral nautilus — calibrated radius + thick overlapping whorls."""
    bm = bmesh.new()
    centers = []
    max_theta = turns * 2 * math.pi
    r_min, r_max = 0.005, 0.078
    growth = math.log(r_max / r_min) / max_theta

    for i in range(steps):
        t = i / max(steps - 1, 1)
        theta = t * max_theta
        path_r = r_min * math.exp(growth * theta)
        # Visible dome so it reads in 3D, not a flat line
        z = 0.006 + 0.028 * t + 0.006 * math.sin(theta * 0.45)
        centers.append(Vector((path_r * math.cos(theta), path_r * math.sin(theta), z)))

    rings = []
    for i, center in enumerate(centers):
        t = i / max(steps - 1, 1)
        path_r = center.xy.length
        # Tube scales with whorl — whorls overlap like a real nautilus
        tr = max(0.011, min(0.034, path_r * 0.30 + 0.008))

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
            off = side * (tr * math.cos(a)) + fwd * (tr * math.sin(a))
            ring.append(bm.verts.new(center + off))
        rings.append(ring)

    bm.verts.ensure_lookup_table()
    for i in range(len(rings) - 1):
        r0, r1 = rings[i], rings[i + 1]
        for j in range(tube_segments):
            jn = (j + 1) % tube_segments
            bm.faces.new((r0[j], r0[jn], r1[jn], r1[j]))
    bm.faces.new(list(reversed(rings[-1])))
    if len(rings[0]) >= 3:
        bm.faces.new(rings[0])

    # Umbilicus — shallow dent at center
    for v in bm.verts:
        xy = Vector((v.co.x, v.co.y, 0.0))
        if xy.length < 0.022 and v.co.z < 0.04:
            inward = -xy.normalized() if xy.length > 1e-4 else Vector((0.0, 0.0, -1.0))
            v.co += inward * 0.005
            v.co.z -= 0.003

    bm.normal_update()
    me = bpy.data.meshes.new("nautilus_shell_mesh")
    bm.to_mesh(me)
    bm.free()
    return me


root = bpy.data.objects.new(f"GROTTO_{ASSET}", None)
col.objects.link(root)

shell_mat = mat("nautilus_Shell", "#EDE4D0", rough=0.42)
shell = bpy.data.objects.new("nautilus_Shell", unified_nautilus_mesh())
col.objects.link(shell)
shell.data.materials.append(shell_mat)
shell.parent = root

# Tilt so spiral disc and thickness read in viewport (not edge-on line)
root.rotation_euler = (math.radians(58), math.radians(14), math.radians(28))

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
