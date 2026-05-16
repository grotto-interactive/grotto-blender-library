"""Builder: grotto_scallop_shell — ribbed fan scallop (solid cup, no flat inner plane)."""
import bpy
import bmesh
import math
import os
from mathutils import Vector

ASSET = "grotto_scallop_shell"
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


def mat(name, hex_c, rough=0.78):
    m = bpy.data.materials.new(name)
    m.use_nodes = True
    bsdf = m.node_tree.nodes.get("Principled BSDF")
    h = hex_c.lstrip("#")
    r, g, b = (int(h[i : i + 2], 16) / 255 for i in (0, 2, 4))
    bsdf.inputs["Base Color"].default_value = (r, g, b, 1)
    bsdf.inputs["Roughness"].default_value = rough
    return m


def scallop_shell_mesh(arc_steps=18, num_ridges=14):
    """
    Solid scallop cup: outer ribbed dome + inner concave surface, connected at rim.
    Hinge along +X edge; fan opens toward +Y.
    """
    bm = bmesh.new()
    profile = [
        (0.0, 0.0),
        (0.03, 0.014),
        (0.06, 0.028),
        (0.09, 0.036),
        (0.115, 0.038),
        (0.135, 0.032),
        (0.15, 0.022),
    ]
    outer_rings, inner_rings = [], []

    for rad, base_h in profile:
        oring, iring = [], []
        for ai in range(arc_steps + 1):
            a = math.pi * ai / arc_steps
            x = rad * math.cos(a)
            y = rad * math.sin(a) * 0.78
            rib = 0.0
            if rad > 0.025:
                rib = 0.014 * math.sin(ai * num_ridges * math.pi / arc_steps) * (rad / 0.15)
            z_out = base_h + rib
            z_in = max(base_h - 0.018, 0.002)
            oring.append(bm.verts.new((x, y, z_out)))
            iring.append(bm.verts.new((x, y * 0.96, z_in)))
        outer_rings.append(oring)
        inner_rings.append(iring)

    bm.verts.ensure_lookup_table()

    def stitch(rings_a, rings_b):
        for i in range(len(rings_a) - 1):
            r0, r1 = rings_a[i], rings_a[i + 1]
            for j in range(arc_steps):
                bm.faces.new((r0[j], r0[j + 1], r1[j + 1], r1[j]))

    stitch(outer_rings, outer_rings)
    stitch(inner_rings, inner_rings)

    # Connect outer ↔ inner (shell thickness) + hinge cap on inner ring
    for j in range(arc_steps):
        bm.faces.new(
            (outer_rings[0][j], outer_rings[0][j + 1], inner_rings[0][j + 1], inner_rings[0][j])
        )

    bm.normal_update()
    me = bpy.data.meshes.new("scallop_shell_mesh")
    bm.to_mesh(me)
    bm.free()
    return me


root = bpy.data.objects.new(f"GROTTO_{ASSET}", None)
col.objects.link(root)

shell_mat = mat("scallop_Shell", "#E6D4B0", rough=0.82)

shell = bpy.data.objects.new("scallop_Shell", scallop_shell_mesh())
col.objects.link(shell)
shell.data.materials.append(shell_mat)
shell.parent = root

bpy.context.view_layer.update()
mesh_objs = [o for o in root.children_recursive if o.type == "MESH"]
pts = [o.matrix_world @ Vector(c) for o in mesh_objs for c in o.bound_box]
root.location.z = -min(v.z for v in pts)

bpy.ops.wm.save_as_mainfile(filepath=BLEND)


def tri_count(data):
    return sum(max(2, len(p.vertices) - 2) for p in data.polygons)


total = sum(tri_count(o.data) for o in mesh_objs)
print("Saved", BLEND)
print("tris", total)
for o in mesh_objs:
    print(" ", o.name, tri_count(o.data))
