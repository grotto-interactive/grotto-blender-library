# MCP / Cursor agent context — Grotto Blender → Roblox

When assisting with Blender work for **Grotto**:

1. **Primary written spec**
   - `docs/grotto-brain/entries/decisions/roblox-asset-export-contract.md`
   - `docs/grotto-brain/entries/decisions/fbx-per-material-decomposition.md`
   - Vision: skim `entries/philosophy/platform-independent-generative-os-north-star.md` and `entries/philosophy/beauty-fluidity-rule.md`.

2. **This repo (`grotto-blender-library`)**
   - `assets/` — Blender source tree synced from Tosha’s “Gamers Grotto” Desktop folder (no OBJ present in snapshot; importer path exists for OBJ in the pipeline script).
   - `scripts/grotto_roblox_pipeline.py` — material split (static meshes), apply transforms, floor pivot, `GROTTO_<name>` parent empty, FBX export aligned to the contract axes, manifest JSON under `exports/manifests/`.

3. **Roblox adapter** — authored place/code: repo `cozy-grotto-roblox` (see brain entry `seed-harbor-runtime-world-system.md`).

Blender does not run Cursor MCP. Use project rules plus `@`-references to **`docs/grotto-brain/`** (symlink to the canon repo) so agents always load the corpus.
