"""Give palm leaf meshes real thickness for Roblox (solidify coplanar fronds)."""
import bpy
import bmesh
import os
import sys

# 1 Blender unit = 1 Roblox stud
LEAF_THICKNESS = 0.80

PALM_ASSETS = [
    ("PalmTree", ("LeafMat",)),
    ("PalmTree2", ("LeafMat",)),
    ("PalmTree3", ("LeafMat",)),
    ("DeadPalmTree", ("DeadLeafMat", "DryLeafMat")),
    ("CoconutTree", ("LeafMat",)),
]

DIR = os.path.join(os.path.dirname(__file__), "..", "assets", "environment")


def thicken_object(obj, thickness):
    me = obj.data
    before = len(me.polygons)
    bm = bmesh.new()
    bm.from_mesh(me)
    if not bm.faces:
        bm.free()
        return 0
    bmesh.ops.solidify(bm, geom=bm.faces[:], thickness=thickness)
    bmesh.ops.remove_doubles(bm, verts=bm.verts, dist=1e-4)
    bmesh.ops.recalc_face_normals(bm, faces=bm.faces)
    bm.normal_update()
    bm.to_mesh(me)
    bm.free()
    me.update()
    return len(me.polygons) - before


def process_blend(asset, leaf_suffixes):
    blend = os.path.join(DIR, asset, f"{asset}.blend")
    if not os.path.isfile(blend):
        print("SKIP missing", blend)
        return

    bpy.ops.wm.open_mainfile(filepath=blend)
    updated = []
    for o in bpy.data.objects:
        if o.type != "MESH":
            continue
        if not any(suffix in o.name for suffix in leaf_suffixes):
            continue
        delta = thicken_object(o, LEAF_THICKNESS)
        updated.append((o.name, delta))
        print(f"  {o.name}: +{delta} faces (thickness {LEAF_THICKNESS})")

    if not updated:
        print("WARN no leaf meshes matched in", asset)
        return

    bpy.ops.wm.save_as_mainfile(filepath=blend)
    print("Saved", blend)


def main():
  # Optional: --asset PalmTree to run one file
    only = None
    if "--asset" in sys.argv:
        i = sys.argv.index("--asset")
        if i + 1 < len(sys.argv):
            only = sys.argv[i + 1]

    for asset, suffixes in PALM_ASSETS:
        if only and asset != only:
            continue
        print("===", asset, "===")
        process_blend(asset, suffixes)


if __name__ == "__main__":
    main()
