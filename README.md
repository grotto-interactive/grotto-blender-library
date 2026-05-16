# grotto-blender-library

Authoritative **Blender source + Roblox export pipeline** for Grotto, aligned with the sibling **Grotto Brain** corpus.

## Layout

| Path | Role |
|------|------|
| `assets/` | Blender tree (synced from Desktop `Gamers Grotto`). |
| `docs/grotto-brain` | Symlink to `../grotto-brain` — decisions + philosophy the pipeline implements. |
| `docs/BLENDER_AGENT_CONTEXT.md` | What Cursor / MCP-style agents should read first for Blender help. |
| `scripts/grotto_roblox_pipeline.py` | Run **inside Blender** — split multi-material static meshes, apply transforms, set floor pivot, parent under `GROTTO_<stem>`, export FBX + manifest. |
| `scripts/run_batch.sh` | Batch all `assets/**/*.blend` through the pipeline. |
| `exports/` | Created by the script: dated `roblox_fbx_*` folders + `manifests/*.json`. |

## One-off (single file)

```bash
cd /Users/toshahixson/dev/grotto/grotto-blender-library
/Applications/Blender.app/Contents/MacOS/Blender -b "assets/props/Barrel/Barrel.blend" \
  --python scripts/grotto_roblox_pipeline.py -- --process-open-file
```

## Full library batch

```bash
./scripts/run_batch.sh
```

Set `BLENDER_BIN` if Blender lives somewhere else.

## Limitations (important)

- **Skinned / rigged meshes** are not auto-split by material (would break weights). The manifest flags multi-material rigged assets for manual review.
- **Character skeleton standard** (`grotto-skeleton-spec.md`) is still a stub — defer rigged character conformance until Orange + Tosha lock bones.
- This environment cannot run Blender headlessly (Metal GPU init crash); **run the batch on Tosha’s Mac** inside a normal Blender install.

After a successful batch, add `exports/` and commit:

```bash
git add exports && git commit -m "Regenerate Roblox FBX outputs from Blender pipeline."
```
