# Pierfrancesco Diodato (`PieroFra`)

Blender Technical Artist & Add-on Developer focused on rigging automation, non-destructive deformation workflows, and UV pipelines for Blender 4.2 LTS through 5.2+.

Every add-on here ships with a deterministic headless regression suite, published releases with SHA256 checksums, and CI-friendly verification scripts.

## Featured Project

### DEF Controller Auto (`CTRL_DEF` v0.2.0)

The flagship add-on: **Approved & Live on [Blender Extensions](https://extensions.blender.org/add-ons/ctrl-def/)**. Together with Auto Copy Transforms DEF it forms a complete 1-click rigging pipeline: generate tracked, color-coded FK controllers from a `DEF_` chain, then wire every constraint deterministically in a single pass. Zero dependency cycles, reversible JSON registry, no manual per-bone work.

| Repo | Release | Extensions | Issues |
|---|---|---|---|
| [def-controller-auto](https://github.com/PieroFra/def-controller-auto) | [v0.2.0](https://github.com/PieroFra/def-controller-auto/releases) | [Live listing](https://extensions.blender.org/add-ons/ctrl-def/) | [Open issues](https://github.com/PieroFra/def-controller-auto/issues) |

## Add-ons

| Add-on | Version | Repo | Tracker |
|---|---|---|---|
| DEF Controller Auto (`CTRL_DEF`) | v0.2.0 | [PieroFra/def-controller-auto](https://github.com/PieroFra/def-controller-auto) | [Issues](https://github.com/PieroFra/def-controller-auto/issues) |
| Auto Copy Transforms DEF (`A.C.T.D.`) | v1.3.0 | [PieroFra/auto-copy-transforms-def](https://github.com/PieroFra/auto-copy-transforms-def) | [Issues](https://github.com/PieroFra/auto-copy-transforms-def/issues) |
| Intelligent UV Mapping | v0.35.1 | [PieroFra/intelligent_uv](https://github.com/PieroFra/intelligent_uv) | [Issues](https://github.com/PieroFra/intelligent_uv/issues) |

### DEF Controller Auto (`CTRL_DEF` v0.2.0)

Generates tracked, color-coded FK controllers with shared custom shapes from the `DEF_` chain. Zero dependency cycles, deterministic naming, and a 1-click synergy with Auto Copy Transforms DEF for a complete controller + constraint pipeline.

### Auto Copy Transforms DEF (`A.C.T.D.` v1.3.0)

Deterministic automation of Copy Transforms / Rotation / Location / Scale constraints between a source armature (`MCH_`) and destination armatures (`DEF_`, `ORG_`). Live preview, pattern learning, and a reversible JSON registry: nothing is baked in, everything can be undone.

### Intelligent UV Mapping (v0.35.1)

Automated UV unwrapping driven by curvature (VSA shape clustering), seam pinning, global texel density control, UDIM multi-tile workflows, and an optional bridge with RizomUV via Live Link, Lua scripting, or full automation.

## Demos

### DEF Controller Auto: FK controller generation from a `DEF_` chain

![DEF Controller Auto demo](assets/def_controller_demo.gif)

### Auto Copy Transforms DEF: constraint automation with live preview

![ACTD demo](assets/actd_demo.gif)

### Intelligent UV Mapping: curvature-driven unwrap and texel density

![Intelligent UV demo](assets/intelligent_uv_demo.gif)

## Find my work

- [Blender Extensions: CTRL_DEF](https://extensions.blender.org/add-ons/ctrl-def/) (approved & live)
- [Blender Extensions: author profile](https://extensions.blender.org/author/pierofra/)
- [Reddit: u/Previous-Nebula7736](https://www.reddit.com/user/Previous-Nebula7736/) (release posts and workflow threads on r/blender)
- [ArtStation](https://www.artstation.com/pierofra/)
