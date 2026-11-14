
# Pierfrancesco Diodato (`PieroFra`)

[![XERJ Corpus Hub contributor](https://hub.xerj.org/contributors/PieroFra/badge.svg)](https://hub.xerj.org/contributors/PieroFra)
[![Blender](https://img.shields.io/badge/Blender-4.2%20LTS--5.2%2B-EA7600?logo=blender&logoColor=white)](https://www.blender.org/)
[![Automated Checks](https://img.shields.io/badge/Automated%20Checks-828%2B%20verified%20checks-2EA043)](#by-the-numbers)
[![License](https://img.shields.io/badge/License-GPL--3.0--or--later-blue)](https://www.gnu.org/licenses/gpl-3.0.html)

> **I build production-ready Blender tools that make rigging and UV workflows faster, safer and reversible.**

CS & Game Dev Student | Aspiring Technical Artist & Blender Add-on Developer focused on rigging automation, non-destructive deformation workflows, and UV pipelines for Blender 4.2 LTS through 5.2+.

**Featured project: BBone to Bones (`v0.2.1`)**  
Convert Blender Bendy Bones (`bbone_segments > 1`) into game-ready bone chains (`<name>_seg_00..XX`) with curved joint boundary blending (`< 0.001 m`), one-click deform-only influence cap, non-destructive `Revert to BBones`, and 5 engine export presets (`UNITY`, `UNITY_GLTF`, `UNREAL`, `UNREAL_GLTF`, `GODOT`).  
[Watch the live GIF demo](#bbone-to-bones-bendy-bones-to-game-ready-chains) | [Direct GIF](https://raw.githubusercontent.com/PieroFra/PieroFra/main/assets/bbone_to_bones_demo_v3.gif) | [1080p 60fps MP4 video](https://raw.githubusercontent.com/PieroFra/PieroFra/main/assets/bbone_showcase_1080p.mp4) | [Live on Blender Extensions](https://extensions.blender.org/add-ons/bbone-to-bones/) | [GitHub Release v0.2.1](https://github.com/PieroFra/bbone-to-bones/releases/tag/v0.2.1) | [Documentation](https://github.com/PieroFra/bbone-to-bones#readme)

## Start Here

Not sure which add-on to try first? Pick your workflow:

The **Rigging Suite** consists of **3 independent rigging add-ons** (zero dependencies between them, automatically unified into a single **Rigging Suite** tab when installed together), **plus Intelligent UV Mapping** for texturing and game-engine UV prep. Pick your workflow:

1. **Exporting Bendy Bones to Unity, Unreal or Godot?** -> **[BBone to Bones](https://extensions.blender.org/add-ons/bbone-to-bones/)** (`v0.2.1`)
2. **Generating FK controllers from an existing `DEF_` skeleton?** -> **[DEF Controller Auto (`CTRL_DEF`)](https://extensions.blender.org/add-ons/ctrl-def/)** (`v0.3.3`)
3. **Wiring `MCH_` / `ORG_` / `DEF_` constraints across one or two armatures?** -> **[Auto Copy Transforms DEF (`A.C.T.D.`)](https://extensions.blender.org/add-ons/auto-copy-transforms-def/)** (`v1.3.1`)
4. **Preparing meshes for baking or game engines?** -> **[Intelligent UV Mapping](https://github.com/PieroFra/intelligent_uv)** (`v0.36.3`)

## By the Numbers

Every project here ships with a deterministic headless regression suite, published releases with SHA256 checksums, and CI-friendly verification scripts.

| Metric | Value |
|---|---|
| **Blender Compatibility** | Blender `4.2 LTS` through `5.2 LTS` (officially tested headless & GUI on 5.2 LTS) |
| **Automated Headless Verification** | **828+ verified checks**: `652` in 12 suites on Auto Copy Transforms DEF, `146` in 29 suites on Intelligent UV (CI on Blender 4.2 & 5.2), `24+` headless checks plus ZIP install and Godot/Unity round-trip on BBone to Bones, `6` e2e checks on CTRL_DEF |
| **Official Blender Extensions** | **3 approved & live** (`bbone-to-bones`, `ctrl-def`, `auto-copy-transforms-def`), **0 external runtime dependencies** (100% Python stdlib + `bpy`) |

## Add-ons

<!-- AUTO-VERSIONS:START -->
| Add-on | Version | Extensions | Repo | Tracker |
|---|---|---|---|---|
| BBone to Bones | v0.2.1 | [Live listing](https://extensions.blender.org/add-ons/bbone-to-bones/) | [PieroFra/bbone-to-bones](https://github.com/PieroFra/bbone-to-bones) | [Issues](https://github.com/PieroFra/bbone-to-bones/issues) |
| DEF Controller Auto (`CTRL_DEF`) | v0.3.3 | [Live listing](https://extensions.blender.org/add-ons/ctrl-def/) | [PieroFra/def-controller-auto](https://github.com/PieroFra/def-controller-auto) | [Issues](https://github.com/PieroFra/def-controller-auto/issues) |
| Auto Copy Transforms DEF (`A.C.T.D.`) | v1.3.1 | [Live listing](https://extensions.blender.org/add-ons/auto-copy-transforms-def/) | [PieroFra/auto-copy-transforms-def](https://github.com/PieroFra/auto-copy-transforms-def) | [Issues](https://github.com/PieroFra/auto-copy-transforms-def/issues) |
| Intelligent UV Mapping | v0.36.3 | *GitHub Release* ([v0.36.3](https://github.com/PieroFra/intelligent_uv/releases/tag/v0.36.3), optional RizomUV bridge) | [PieroFra/intelligent_uv](https://github.com/PieroFra/intelligent_uv) | [Issues](https://github.com/PieroFra/intelligent_uv/issues) |<!-- AUTO-VERSIONS:END -->

### BBone to Bones (v0.2.1)

Converts Blender Bendy Bones (`bbone_segments > 1`) into game-ready bone chains (`<name>_seg_00..XX`) with curved joint boundary blending (`< 0.001 m`), one-click deform-only influence cap, non-destructive `Revert to BBones`, and 5 engine export presets (`UNITY`, `UNITY_GLTF`, `UNREAL`, `UNREAL_GLTF`, `GODOT`). Approved and live on [Blender Extensions](https://extensions.blender.org/add-ons/bbone-to-bones/) and published as [GitHub Release v0.2.1](https://github.com/PieroFra/bbone-to-bones/releases/tag/v0.2.1).

### DEF Controller Auto (`CTRL_DEF` v0.3.3)

Generates tracked, color-coded FK controllers with shared custom shapes from the `DEF_` chain. Zero dependency cycles, deterministic naming, and a 1-click synergy with Auto Copy Transforms DEF for a complete controller + constraint pipeline.

### Auto Copy Transforms DEF (`A.C.T.D.` v1.3.1)

Deterministic automation of Copy Transforms / Rotation / Location / Scale constraints between a source armature (`MCH_`) and destination armatures (`DEF_`, `ORG_`). Live preview, pattern learning, and a reversible JSON registry: nothing is baked in, everything can be undone. Approved on [Blender Extensions](https://extensions.blender.org/add-ons/auto-copy-transforms-def/) and indexed on the [XERJ Corpus Hub](https://hub.xerj.org/contributors/PieroFra).

### Intelligent UV Mapping (v0.36.3)

Automated UV unwrapping driven by curvature (VSA shape clustering), seam pinning, global texel density control, UDIM multi-tile workflows, and an optional bridge with RizomUV via Live Link, Lua scripting, or full automation.

[GitHub Release v0.36.3](https://github.com/PieroFra/intelligent_uv/releases/tag/v0.36.3) | [Direct ZIP Download](https://github.com/PieroFra/intelligent_uv/releases/download/v0.36.3/intelligent_uv-0.36.3.zip) | [Documentation](https://github.com/PieroFra/intelligent_uv#readme) | [v0.36.3 demo video (16:9 MP4)](https://github.com/PieroFra/intelligent_uv/releases/download/v0.36.3/intelligent_uv_0363_16x9.mp4)

## Demos

### BBone to Bones: Bendy Bones to game-ready chains

![BBone to Bones demo](assets/bbone_to_bones_demo_v3.gif)

### DEF Controller Auto: FK controller generation from a `DEF_` chain

![DEF Controller Auto demo](assets/def_controller_demo.gif)

### Auto Copy Transforms DEF: constraint automation with live preview

![ACTD demo](assets/actd_demo.gif)

[1080p 60fps MP4 showcase](https://raw.githubusercontent.com/PieroFra/PieroFra/main/assets/actd_showcase_1080p.mp4)

### Intelligent UV Mapping: curvature-driven unwrap and texel density

![Intelligent UV demo](assets/intelligent_uv_demo.gif)

## Roadmap & Active Maintenance

All four projects are actively maintained with recurring verification passes:

- **BBone to Bones**: engine round-trip regression on Godot and Unity, and release archive SHA256 validation.

- **DEF Controller Auto (`CTRL_DEF`)**: custom widget library presets, multi-limb batch templates, and Blender 4.2 - 5.2 LTS CI matrix.
- **Auto Copy Transforms DEF (`A.C.T.D.`)**: one-click restore operator from `actd_replace_backup_*.json` snapshots, extended multi-armature batch rules, and automated release archive validation in CI.
- **Intelligent UV Mapping**: headless end-to-end UV pipeline regression suite and clean-install gate verification on virgin Blender profiles.

## Contact & Collaboration

I am open to collaborations, Python/Blender tool development, technical art pipelines, and freelance work.

> **What rigging or UV step is still slowing you down?** Open an issue on any tracker with the workflow you want automated next.

- **GitHub Issues & Inquiries**: [@PieroFra](https://github.com/PieroFra) on GitHub (or open an issue on the relevant repository tracker)
- **Blender Extensions**: [BBone to Bones](https://extensions.blender.org/add-ons/bbone-to-bones/) (approved & live) | [CTRL_DEF](https://extensions.blender.org/add-ons/ctrl-def/) (approved & live) | [A.C.T.D.](https://extensions.blender.org/add-ons/auto-copy-transforms-def/) (approved & live) | [Author profile](https://extensions.blender.org/author/96040/)
- **XERJ Corpus Hub**: [hub.xerj.org/contributors/PieroFra](https://hub.xerj.org/contributors/PieroFra)
- **Reddit**: [u/Previous-Nebula7736](https://www.reddit.com/user/Previous-Nebula7736/) (release posts and workflow threads on `r/blender`)
- **ArtStation**: [artstation.com/pierofra](https://www.artstation.com/pierofra/)
