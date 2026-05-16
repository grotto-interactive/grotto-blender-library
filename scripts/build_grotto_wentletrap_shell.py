"""Builder: grotto_wentletrap_shell — clean stacked spiral whorls (fresh start)."""
import bpy
import bmesh
import math
import os
from mathutils import Vector

ASSET = "grotto_wentletrap_shell"
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


def mat_pearl(name, hex_c="#F5F0E8"):
    m = bpy.data.materials.new(name)
    m.use_nodes = True
    bsdf = m.node_tree.nodes.get("Principled BSDF")
    h = hex_c.lstrip("#")
    r, g, b = (int(h[i : i + 2], 16) / 255 for i in (0, 2, 4))
    bsdf.inputs["Base Color"].default_value = (r, g, b, 1)
    bsdf.inputs["Roughness"].default_value = 0.30
    if "Specular IOR Level" in bsdf.inputs:
        bsdf.inputs["Specular IOR Level"].default_value = 0.40
    return m


def rib_mul(angle, spiral_deg, ribs=8, amount=0.20):
    """Rounded raised ribs following the spiral."""
    phase = math.radians(spiral_deg) + angle
    return 1.0 + amount * max(0.0, math.cos(ribs * phase)) ** 3


def spiral_mouth_radius(angle, r, z_frac, spin_deg, w_idx, whorls):
    """
    Conch-like spiral aperture: oval lip on the outer arc, slit along the spiral,
    pinched on the inner whorl side. Fades toward the tip.
    """
    if z_frac > 0.32 or w_idx > 2:
        return r

    fade = (1.0 - z_frac / 0.32) * max(0.0, 1.0 - w_idx / 2.8)
    if fade <= 0.0:
        return r

    spiral_ang = math.radians(spin_deg)
    rel = (angle - spiral_ang + math.pi) % (2.0 * math.pi) - math.pi

    # Oval lip — wider on the outer spiral face (like conch aperture)
    outer = max(0.0, math.cos(rel * 0.80))
    inner = max(0.0, math.cos(rel * 0.55 + math.pi * 0.15))

    lip = 1.0 + 0.24 * fade * (outer**1.1)
    slit = 0.48 + 0.52 * (inner**0.85)
    oval = 1.0 + 0.14 * fade * outer - 0.08 * fade * max(0.0, -math.cos(rel))

    return r * lip * slit * oval


def build_shell(
    whorls=10,
    layers_per_whorl=3,
    sides=10,
    height=0.36,
    r_bottom=0.050,
    r_top=0.010,
):
    bm = bmesh.new()
    whorl_h = height / whorls
    spiral_per_whorl = 32.0
    rings = []

    for w in range(whorls):
        z0 = w * whorl_h
        spin = w * spiral_per_whorl
        r_lo = r_bottom + (r_top - r_bottom) * (w / whorls)
        r_hi = r_bottom + (r_top - r_bottom) * ((w + 1) / whorls)

        for layer in range(layers_per_whorl + 1):
            if w > 0 and layer == 0:
                continue
            u = layer / layers_per_whorl
            z = z0 + u * whorl_h
            z_frac = z / height

            # Whorl belly curve: fuller in the middle of each step
            belly = math.sin(u * math.pi) ** 0.75
            r = (r_lo * (1.0 - u) + r_hi * u) * (1.0 + 0.10 * belly)

            spin_here = spin + u * spiral_per_whorl
            spiral_ang = math.radians(spin_here)
            ox = 0.003 * w * math.cos(spiral_ang)
            oy = 0.003 * w * math.sin(spiral_ang)
            if w <= 1:
                mouth_shift = 0.011 * (1.0 - w * 0.45) * (1.0 - z_frac * 2.5)
                ox += mouth_shift * math.cos(spiral_ang)
                oy += mouth_shift * math.sin(spiral_ang)
            center = Vector((ox, oy, z))

            ring = []
            for s in range(sides):
                ang = 2.0 * math.pi * s / sides
                rad = r * rib_mul(ang, spin_here)
                rad = spiral_mouth_radius(ang, rad, z_frac, spin_here, w, whorls)
                # Conch-style oval cross-section at the mouth
                if z_frac <= 0.32 and w <= 2:
                    fade = (1.0 - z_frac / 0.32) * max(0.0, 1.0 - w / 2.8)
                    rel = ang - spiral_ang
                    rad *= 1.0 + 0.20 * fade * max(0.0, math.cos(rel)) ** 0.9
                    rad *= 1.0 - 0.10 * fade * max(0.0, -math.cos(rel)) ** 1.2
                ring.append(bm.verts.new(center + Vector((math.cos(ang) * rad, math.sin(ang) * rad, 0.0))))
            rings.append(ring)

    bm.verts.ensure_lookup_table()
    for i in range(len(rings) - 1):
        a, b = rings[i], rings[i + 1]
        for s in range(sides):
            sn = (s + 1) % sides
            bm.faces.new((a[s], a[sn], b[sn], b[s]))

    # Pointed apex
    top = rings[-1]
    tip = bm.verts.new(Vector((top[0].co.x, top[0].co.y, top[0].co.z + 0.016)))
    for s in range(sides):
        sn = (s + 1) % sides
        bm.faces.new((tip, top[sn], top[s]))

    bm.normal_update()
    me = bpy.data.meshes.new("wentletrap_shell_mesh")
    bm.to_mesh(me)
    bm.free()
    return me


root = bpy.data.objects.new(f"GROTTO_{ASSET}", None)
col.objects.link(root)

shell = bpy.data.objects.new("wentletrap_Shell", build_shell())
shell.data.materials.append(mat_pearl("wentletrap_Shell"))
col.objects.link(shell)
shell.parent = root

root.rotation_euler = (0.0, 0.0, 0.0)

bpy.context.view_layer.update()
mesh_objs = [o for o in root.children_recursive if o.type == "MESH"]
pts = [o.matrix_world @ Vector(c) for o in mesh_objs for c in o.bound_box]
root.location.z = -min(v.z for v in pts)

bpy.ops.wm.save_as_mainfile(filepath=BLEND)

total = sum(max(2, len(p.vertices) - 2) for p in shell.data.polygons)
print("Saved", BLEND)
print("tris", total, "parts", [o.name for o in mesh_objs])
