"""Grotto to Roblox — run inside Blender. Read grotto-brain decisions:
../grotto-brain/entries/decisions/roblox-asset-export-contract.md
../grotto-brain/entries/decisions/fbx-per-material-decomposition.md
Examples:
 Blender -b f.blend --python scripts/grotto_roblox_pipeline.py -- --process-open-file
 Blender -b --python scripts/grotto_roblox_pipeline.py -- --filepath m.obj"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import shutil
import sys
from pathlib import Path

import bpy  # type: ignore
import bmesh  # type: ignore
import mathutils  # type: ignore


def argv_tail():
    if "--" not in sys.argv:
        return []
    return sys.argv[sys.argv.index("--") + 1 :]


def parse_args(av):
    ap = argparse.ArgumentParser()
    ap.add_argument("--process-open-file", action="store_true")
    ap.add_argument("--filepath", default="")
    ap.add_argument("--out-dir", default="")
    ap.add_argument("--manifest-dir", default="")
    ap.add_argument("--no-backup-blend", action="store_true")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--prop-tris-soft", type=int, default=800)
    ap.add_argument("--tri-hard-cap", type=int, default=21000)
    return ap.parse_args(av)


def repo_root() -> Path:
    return Path(__file__).resolve().parents[1]


def tri_count(mesh) -> int:
    return sum(max(2, len(p.vertices) - 2) for p in mesh.polygons)


def rigged(obj):
    return any(m.type == "ARMATURE" for m in obj.modifiers)


def split_multimat(mesh_obj):
    if mesh_obj.type != "MESH" or rigged(mesh_obj):
        return []
    D = mesh_obj.data
    mats = D.materials
    if not mats or len(mats) <= 1:
        return []
    wm = mesh_obj.matrix_world.copy()
    bm = bmesh.new()
    bm.from_mesh(D)
    bm.faces.ensure_lookup_table()
    spawned = []
    for mi in sorted({f.material_index for f in bm.faces}):
        b2 = bm.copy()
        b2.faces.ensure_lookup_table()
        dead = [f for f in b2.faces if f.material_index != mi]
        if not dead or len(dead) == len(b2.faces):
            b2.free()
            continue
        bmesh.ops.delete(b2, geom=dead, context="FACES")
        b2.faces.ensure_lookup_table()
        if not b2.faces:
            b2.free()
            continue
        slug = bpy.path.clean_name(mesh_obj.name + f"_slot{mi}")
        if mi < len(mats) and mats[mi]:
            slug = bpy.path.clean_name(mesh_obj.name + "_" + mats[mi].name.replace(".", "_"))[:62]
        nm = bpy.data.meshes.new(slug + "_DATA")
        b2.to_mesh(nm)
        b2.free()
        mat = mats[mi] if mi < len(mats) else None
        if mat:
            nm.materials.clear()
            nm.materials.append(mat)
        ob = bpy.data.objects.new(slug, nm)
        bpy.context.collection.objects.link(ob)
        ob.matrix_world = wm
        spawned.append(ob)
    bm.free()
    if not spawned:
        return []
    bpy.data.objects.remove(mesh_obj, do_unlink=True)
    return spawned


def tf_apply(mesh_obj):
    bpy.ops.object.select_all(action="DESELECT")
    mesh_obj.hide_set(False)
    mesh_obj.select_set(True)
    bpy.context.view_layer.objects.active = mesh_obj
    bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)


def pivot_floor(mesh_obj):
    bpy.ops.object.select_all(action="DESELECT")
    mesh_obj.hide_set(False)
    mesh_obj.select_set(True)
    bpy.context.view_layer.objects.active = mesh_obj
    wm = mesh_obj.matrix_world
    ws = [(wm @ mathutils.Vector(c)) for c in mesh_obj.bound_box]
    cx = sum(v.x for v in ws) / len(ws)
    cy = sum(v.y for v in ws) / len(ws)
    mz = min(v.z for v in ws)
    bpy.context.scene.cursor.location = (cx, cy, mz)
    bpy.ops.object.origin_set(type="ORIGIN_CURSOR", center="MEDIAN")


def parent_empty(nm, objs):
    sc = bpy.context.scene
    rt = bpy.data.objects.get(nm)
    if rt is None:
        rt = bpy.data.objects.new(nm, None)
        sc.collection.objects.link(rt)
    bpy.ops.object.select_all(action="DESELECT")
    for ob in objs:
        ob.hide_set(False)
        ob.select_set(True)
    bpy.context.view_layer.objects.active = rt
    bpy.ops.object.parent_set(type="OBJECT", keep_transform=True)
    bpy.ops.object.select_all(action="DESELECT")
    return rt


def export_fbx(path: Path):
    path.parent.mkdir(parents=True, exist_ok=True)
    bpy.ops.export_scene.fbx(
        filepath=str(path),
        path_mode="AUTO",
        bake_anim=False,
        use_selection=False,
        object_types={"EMPTY", "MESH", "ARMATURE"},
        use_mesh_modifiers=True,
        mesh_smooth_type="FACE",
        add_leaf_bones=False,
        axis_forward="-Y",
        axis_up="Z",
        primary_bone_axis="Y",
        secondary_bone_axis="X",
        apply_scale_options="FBX_SCALE_ALL",
        bake_space_transform=False,
        armature_nodetype="NULL",
        use_armature_deform_only=True,
    )


def manifest(meshes, soft, hard):
    warns, skin_notes = [], []
    total_tris = 0
    for o in meshes:
        mats = getattr(o.data, "materials", None)
        slots = len(mats) if mats else 0
        if mats and len(mats) > 1 and rigged(o):
            skin_notes.append(f"{o.name}: {slots} mats on rigged mesh — audit in Studio.")
        t = tri_count(o.data)
        total_tris += t
        meta = {"object": o.name, "triangles": t, "material_slots": slots}
        if t > hard:
            warns.append({"level": "HARD_OVER_ENGINE_CAP", **meta})
        elif t > soft:
            warns.append({"level": "OVER_PROP_SOFT_CAP", **meta})
    now = dt.datetime.utcnow().replace(tzinfo=dt.timezone.utc)
    return {
        "generated_utc": now.isoformat().replace("+00:00", "Z"),
        "triangle_total_approx_scene": total_tris,
        "triangle_warnings": warns,
        "skinned_material_notes": skin_notes,
    }


def load_file(p: Path):
    ext = p.suffix.lower()
    if ext == ".obj":
        bpy.ops.wm.read_factory_settings(use_empty=True)
        if hasattr(bpy.ops.wm, "obj_import"):
            bpy.ops.wm.obj_import(filepath=str(p))
        else:
            raise SystemExit("Enable OBJ importer (Blender >=4 wm.obj_import).")
        return None
    if ext == ".blend":
        bpy.ops.wm.open_mainfile(filepath=str(p))
        return p
    raise SystemExit("Expected .blend or .obj")



def main():
    args = parse_args(argv_tail())
    rr = repo_root()

    if args.filepath:
        tgt = Path(args.filepath).expanduser().resolve()
        load_file(tgt)
        bpy.context.view_layer.update()
        bd = tgt if tgt.suffix.lower() == ".blend" else None
        if tgt.suffix.lower() == ".obj":
            stem = tgt.stem
        else:
            stem = bpy.path.display_name_from_filepath(str(tgt))
    elif args.process_open_file:
        fp = bpy.data.filepath
        if not fp:
            raise SystemExit("Open a .blend with: Blender -b file.blend --python ...")
        bd = Path(fp).resolve()
        stem = bpy.path.display_name_from_filepath(str(bd))
    else:
        raise SystemExit("Pass --process-open-file or --filepath.")

    stamp = dt.date.today().isoformat()
    out_dir = Path(args.out_dir) if args.out_dir else rr / "exports" / f"roblox_fbx_{stamp}"
    man_dir = Path(args.manifest_dir) if args.manifest_dir else rr / "exports" / "manifests"
    out_dir.mkdir(parents=True, exist_ok=True)
    man_dir.mkdir(parents=True, exist_ok=True)

    scn = bpy.context.scene
    for ob in list(scn.objects):
        if ob.type == "MESH" and not rigged(ob):
            split_multimat(ob)

    meshes = [o for o in scn.objects if o.type == "MESH"]
    for ob in meshes:
        if not rigged(ob):
            tf_apply(ob)
            pivot_floor(ob)

    arms = [o for o in scn.objects if o.type == "ARMATURE"]
    kids = meshes + arms
    root_nm = "GROTTO_" + bpy.path.clean_name(stem)
    parent_empty(root_nm, kids)

    mf = manifest(meshes, args.prop_tris_soft, args.tri_hard_cap)
    (man_dir / f"{stem}.json").write_text(json.dumps(mf, indent=2))
    fbx_path = out_dir / f"{stem}_LOD0_roblox.fbx"

    if args.dry_run:
        print("DRY_RUN", fbx_path)
        return

    export_fbx(fbx_path)

    if args.filepath and Path(args.filepath).suffix.lower() == ".obj":
        print("OBJ import; save .blend manually if you want a working file.")
    elif bpy.data.filepath:
        blend_path = Path(bpy.data.filepath)
        if not args.no_backup_blend:
            bak = blend_path.with_suffix(blend_path.suffix + ".grotto-backup")
            if not bak.exists():
                shutil.copy2(blend_path, bak)
        bpy.ops.wm.save_mainfile(filepath=str(blend_path))
        print("Saved blend", blend_path)

    print("Wrote FBX", fbx_path)


if __name__ == "__main__":
    main()
