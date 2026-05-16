"""Builder: grotto_clay_jug — opaque ceramic jug with side handle."""
import bpy
import bmesh
import math
import os
from mathutils import Vector

ASSET = "grotto_clay_jug"
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


def mat(name, hex_c, rough=0.85):
    m = bpy.data.materials.new(name)
    m.use_nodes = True
    bsdf = m.node_tree.nodes.get("Principled BSDF")
    h = hex_c.lstrip("#")
    r, g, b = (int(h[i : i + 2], 16) / 255 for i in (0, 2, 4))
    bsdf.inputs["Base Color"].default_value = (r, g, b, 1)
    bsdf.inputs["Roughness"].default_value = rough
    return m


def lathe_mesh(name, profile, segments=22):
    bm = bmesh.new()
    rings = []
    for z, r in profile:
        ring = []
        for a_i in range(segments):
            a = 2 * math.pi * a_i / segments
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


def body_radius_at_z(profile, z):
    for i in range(len(profile) - 1):
        z0, r0 = profile[i]
        z1, r1 = profile[i + 1]
        if z0 <= z <= z1:
            t = (z - z0) / (z1 - z0) if z1 != z0 else 0.0
            return r0 + t * (r1 - r0)
    return profile[-1][1]


def build_handle_mesh(profile, sections=6):
    """C-strap on +X; endpoints embedded in body radius at each Z."""
    bm = bmesh.new()
    tube_r = 0.018
    z_lo, z_hi = 0.14, 0.28
    r_lo = body_radius_at_z(profile, z_lo)
    r_hi = body_radius_at_z(profile, z_hi)
    z_mid = (z_lo + z_hi) * 0.5
    r_mid = body_radius_at_z(profile, z_mid)

    # Centerline ends slightly inside clay so the tube meets the surface
    embed = tube_r * 0.92
    p0 = Vector((r_lo - embed, 0.0, z_lo))
    p2 = Vector((r_hi - embed, 0.0, z_hi))
    p1 = Vector((r_mid + tube_r * 2.6, 0.0, z_mid))

    n = 20
    path = []
    for i in range(n + 1):
        t = i / n
        path.append((1 - t) ** 2 * p0 + 2 * (1 - t) * t * p1 + t**2 * p2)

    rings = []
    for i, p in enumerate(path):
        t = i / n
        # Thicker at both attachment ends (fused clay lugs)
        end_w = max(0.0, 1.0 - min(t, 1.0 - t) * 2.2)
        local_r = tube_r * (1.0 + 0.55 * end_w)

        tangent = (path[min(i + 1, n)] - path[max(i - 1, 0)]).normalized()
        up = Vector((0, 1, 0))
        side = tangent.cross(up).normalized()
        if side.length < 0.01:
            side = Vector((1, 0, 0))
        ring = []
        for s in range(sections):
            a = 2 * math.pi * s / sections
            off = side * (local_r * math.cos(a)) + up * (local_r * math.sin(a))
            ring.append(bm.verts.new(p + off))
        rings.append(ring)

    bm.verts.ensure_lookup_table()
    for i in range(len(rings) - 1):
        r0, r1 = rings[i], rings[i + 1]
        for j in range(sections):
            jn = (j + 1) % sections
            bm.faces.new((r0[j], r0[jn], r1[jn], r1[j]))
    bm.normal_update()
    me = bpy.data.meshes.new("jug_handle_mesh")
    bm.to_mesh(me)
    bm.free()
    return me


root = bpy.data.objects.new(f"GROTTO_{ASSET}", None)
col.objects.link(root)

body_mat = mat("jug_Body", "#A6896A", rough=0.9)
handle_mat = mat("jug_Handle", "#7A6348", rough=0.92)

# Pitcher jug profile (~0.48 m)
profile = [
    (0.0, 0.075),
    (0.03, 0.095),
    (0.10, 0.115),
    (0.18, 0.118),
    (0.26, 0.105),
    (0.32, 0.085),
    (0.36, 0.062),
    (0.38, 0.048),
    (0.40, 0.042),
    (0.42, 0.044),  # slight pouring lip flare
    (0.43, 0.040),
]
link_part("jug_Body", lathe_mesh("jug_body_mesh", profile, 22), body_mat, root)
link_part("jug_Handle", build_handle_mesh(profile), handle_mat, root)

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
