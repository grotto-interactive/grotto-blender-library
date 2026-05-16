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
import traceback
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


def _is_reference_placeholder(obj: bpy.types.Object) -> bool:
    """Skip reference / empty-holder meshes (e.g. Ref_Head) from transform + export prep."""
    if obj.type != "MESH":
        return True
    name = obj.name
    if name.startswith(("Ref_", "REF_", "ref_")):
        return True
    if obj.data is None:
        return True
    if len(obj.data.vertices) == 0:
        return True
    return False


def _objects_respecting_layer_excludes(layer_coll, out: list) -> None:
    """Flatten objects from layer collections, skipping excluded subtrees."""
    if getattr(layer_coll, "exclude", False):
        return
    for ob in layer_coll.collection.objects:
        out.append(ob)
    for child in layer_coll.children:
        _objects_respecting_layer_excludes(child, out)


def visible_layer_objects(view_layer: bpy.types.ViewLayer) -> list[bpy.types.Object]:
    raw: list[bpy.types.Object] = []
    _objects_respecting_layer_excludes(view_layer.layer_collection, raw)
    seen = set()
    out: list[bpy.types.Object] = []
    for ob in raw:
        if ob in seen:
            continue
        seen.add(ob)
        out.append(ob)
    return out


def mesh_candidates_for_transform(view_layer: bpy.types.ViewLayer):
    """Meshes in the active ViewLayer that should receive apply + pivot."""
    seen = set()
    for obj in visible_layer_objects(view_layer):
        if obj in seen:
            continue
        seen.add(obj)
        if obj.type != "MESH" or rigged(obj) or _is_reference_placeholder(obj):
            continue
        yield obj


def all_manifest_meshes(view_layer: bpy.types.ViewLayer):
    """Meshes counted in manifest (exclude reference placeholders; keep rigged)."""
    seen = set()
    for obj in visible_layer_objects(view_layer):
        if obj in seen:
            continue
        seen.add(obj)
        if obj.type != "MESH" or _is_reference_placeholder(obj):
            continue
        yield obj


def _iter_view3d_override_bases():
    wm = bpy.context.window_manager
    for window in wm.windows:
        screen = window.screen
        for area in screen.areas:
            if area.type != "VIEW_3D":
                continue
            for region in area.regions:
                if region.type == "WINDOW":
                    yield {
                        "window": window,
                        "screen": screen,
                        "area": area,
                        "region": region,
                    }
                    break


def _apply_mesh_local_matrix_api(mesh_obj: bpy.types.Object):
    """Apply transforms without bpy.ops (local matrix into mesh data)."""
    if mesh_obj.type != "MESH" or mesh_obj.data is None:
        return
    mat = mesh_obj.matrix_local.copy()
    mesh_obj.data.transform(mat)
    mesh_obj.matrix_local = mathutils.Matrix.Identity(4)
    mesh_obj.data.update()


def tf_apply(mesh_obj: bpy.types.Object):
    mesh_obj.hide_set(False)
    mesh_obj.hide_viewport = False

    applied = False
    for base in _iter_view3d_override_bases():
        try:
            with bpy.context.temp_override(
                **base,
                scene=bpy.context.scene,
                view_layer=bpy.context.view_layer,
                active_object=mesh_obj,
                selected_objects=[mesh_obj],
                selected_editable_objects=[mesh_obj],
            ):
                bpy.ops.object.select_all(action="DESELECT")
                mesh_obj.select_set(True)
                bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
            applied = True
            break
        except RuntimeError:
            continue

    if not applied:
        _apply_mesh_local_matrix_api(mesh_obj)


def pivot_floor(mesh_obj: bpy.types.Object):
    mesh_obj.hide_set(False)
    mesh_obj.hide_viewport = False

    wm = mesh_obj.matrix_world
    ws = [(wm @ mathutils.Vector(c)) for c in mesh_obj.bound_box]
    cx = sum(v.x for v in ws) / len(ws)
    cy = sum(v.y for v in ws) / len(ws)
    mz = min(v.z for v in ws)

    applied = False
    for base in _iter_view3d_override_bases():
        try:
            with bpy.context.temp_override(
                **base,
                scene=bpy.context.scene,
                view_layer=bpy.context.view_layer,
                active_object=mesh_obj,
                selected_objects=[mesh_obj],
                selected_editable_objects=[mesh_obj],
            ):
                bpy.ops.object.select_all(action="DESELECT")
                mesh_obj.select_set(True)
                bpy.context.scene.cursor.location = (cx, cy, mz)
                bpy.ops.object.origin_set(type="ORIGIN_CURSOR", center="MEDIAN")
            applied = True
            break
        except RuntimeError:
            continue

    if not applied:
        print(
            f"WARN: could not run origin_set for {mesh_obj.name}; pivot may need manual check.",
            file=sys.stderr,
        )


def parent_empty(nm: str, objs: list[bpy.types.Object]) -> bpy.types.Object:
    sc = bpy.context.scene
    rt = bpy.data.objects.get(nm)
    if rt is None:
        rt = bpy.data.objects.new(nm, None)
        sc.collection.objects.link(rt)
    for ch in objs:
        ch.hide_set(False)
        mw = ch.matrix_world.copy()
        ch.parent = rt
        ch.matrix_world = mw
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
    now = dt.datetime.now(dt.timezone.utc)
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

    vl = bpy.context.view_layer

    for ob in list(mesh_candidates_for_transform(vl)):
        split_multimat(ob)

    for ob in list(mesh_candidates_for_transform(vl)):
        tf_apply(ob)
        pivot_floor(ob)

    meshes = list(all_manifest_meshes(vl))
    arms = [o for o in visible_layer_objects(vl) if o.type == "ARMATURE"]
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
    try:
        main()
    except SystemExit as e:
        code = e.code
        if code is None or code == 0:
            sys.exit(0)
        if isinstance(code, int):
            sys.exit(code)
        sys.exit(1)
    except BaseException:
        traceback.print_exc()
        sys.exit(1)
