# -*- coding: utf-8 -*-
"""Sincronizza automaticamente le versioni degli add-on nel README del profilo
PieroFra con le versioni reali dichiarate nei manifest dei singoli progetti.

Sorgenti letti (blender_manifest.toml di ogni progetto):
  - ../bbone_to_bones/blender_manifest.toml  -> versione BBone to Bones
  - ../CTRL_DEF/blender_manifest.toml        -> versione CTRL_DEF
  - ../ACTD/packaging/blender_manifest.toml  -> versione A.C.T.D.
  - ../intelligent_uv/blender_manifest.toml  -> versione Intelligent UV

Aggiorna nel README:
  - la tabella della sezione "Add-ons" tra i marcatori AUTO-VERSIONS;
  - i titoli delle sottosezioni di ogni add-on ( "`CTRL_DEF` vX.Y.Z" ecc.).

Uso (Python di Blender o qualsiasi stdlib >= 3.8):
    python sync_profile_versions.py

Nota: lo script NON tocca il codice degli add-on, legge solo i manifest.
"""
import re
import sys
from pathlib import Path

# Percorsi di partenza: la radice del profilo e la cartella del workspace addon
REPO = Path(__file__).resolve().parent
WORKSPACE = REPO.parent
README = REPO / "README.md"

# Mapping: (nome visualizzato, file manifest, slug GitHub per le release)
PROJECTS = [
    ("BBone to Bones", WORKSPACE / "bbone_to_bones" / "blender_manifest.toml", "PieroFra/bbone-to-bones"),
    ("CTRL_DEF", WORKSPACE / "CTRL_DEF" / "blender_manifest.toml", "PieroFra/def-controller-auto"),
    ("A.C.T.D.", WORKSPACE / "ACTD" / "packaging" / "blender_manifest.toml", "PieroFra/auto-copy-transforms-def"),
    ("intelligent_uv", WORKSPACE / "intelligent_uv" / "blender_manifest.toml", "PieroFra/intelligent_uv"),
]


def read_version(manifest_path: Path) -> str:
    """Estrae 'version = "X.Y.Z"' da un blender_manifest.toml (solo stdlib)."""
    text = manifest_path.read_text(encoding="utf-8")
    match = re.search(r'^version\s*=\s*"([0-9A-Za-z.]+)"', text, re.MULTILINE)
    if not match:
        raise ValueError("Versione non trovata in %s" % manifest_path)
    return match.group(1)


def _semver(testo: str):
    """Tupla ordinabile da una stringa tipo 'v0.2.0' (None se non e' semver)."""
    corrispondenza = re.match(r"^v?(\d+)\.(\d+)\.(\d+)$", testo.strip())
    if not corrispondenza:
        return None
    return tuple(int(gruppo) for gruppo in corrispondenza.groups())


def read_published_version(slug: str, repo: Path) -> str:
    """Versione realmente pubblicata: l'ultima release GitHub, non il manifest.

    Il manifest dice cosa c'e' nel working tree: chi sta preparando la 0.3.0
    senza averla rilasciata non deve vedersela annunciata sul profilo. Le
    release GitHub sono la fonte autorevole (i tag locali possono essere
    indietro: e' successo con CTRL_DEF, tag fermo a v0.1.2 e release a v0.2.0).
    """
    import json
    import subprocess

    try:
        esito = subprocess.run(
            ["gh", "release", "list", "-R", slug, "--limit", "100", "--json", "tagName"],
            capture_output=True, text=True, timeout=120,
        )
        if esito.returncode == 0 and (esito.stdout or "").strip():
            dati = json.loads(esito.stdout)
            candidate = [d.get("tagName", "") for d in dati]
            candidate = [t for t in candidate if _semver(t)]
            if candidate:
                migliore = max(candidate, key=_semver)
                return ".".join(str(parte) for parte in _semver(migliore))
    except (OSError, ValueError, subprocess.SubprocessError):
        pass

    # Riserva: tag git locali, se gh non e' disponibile o non risponde.
    try:
        esito = subprocess.run(
            ["git", "tag", "--list"],
            cwd=str(repo), capture_output=True, text=True, timeout=30,
        )
    except (OSError, subprocess.SubprocessError) as exc:
        raise ValueError("ne' gh ne' git disponibili per %s: %s" % (slug, exc))
    candidate = [t for t in (esito.stdout or "").splitlines() if _semver(t)]
    if candidate:
        return ".".join(str(p) for p in _semver(max(candidate, key=_semver)))
    raise ValueError("nessuna release ne' tag di versione per %s" % slug)


def main() -> int:
    versions = {}
    avvisi = []
    for name, manifest, slug in PROJECTS:
        repo = manifest.parent
        if repo.name == "packaging":
            repo = repo.parent
        try:
            versions[name] = read_published_version(slug, repo)
        except (OSError, ValueError) as exc:
            print("SYNC_VERSIONS_FAIL | versione pubblicata non leggibile: %s | %s" % (name, exc))
            return 1
        # se il manifest e' avanti rispetto alla release, e' lavoro non pubblicato
        try:
            nel_manifest = read_version(manifest)
        except (OSError, ValueError):
            nel_manifest = None
        if nel_manifest and nel_manifest != versions[name]:
            avvisi.append("%s: manifest %s, ultima release %s (non pubblicata)"
                          % (name, nel_manifest, versions[name]))

    text = README.read_text(encoding="utf-8")
    original = text

    # 1) Tabella tra i marcatori AUTO-VERSIONS: sostituisce "| vX.Y.Z |" nella
    #    colonna Version della riga corrispondente all'add-on.
    start = text.find("<!-- AUTO-VERSIONS:START -->")
    end = text.find("<!-- AUTO-VERSIONS:END -->")
    if start == -1 or end == -1 or start > end:
        print("SYNC_VERSIONS_FAIL | marcatori AUTO-VERSIONS mancanti o invertiti in README.md")
        return 1

    def patch_table_row(line: str) -> str:
        if "BBone to Bones" in line:
            new = versions["BBone to Bones"]
        elif "CTRL_DEF" in line:
            new = versions["CTRL_DEF"]
        elif "A.C.T.D." in line:
            new = versions["A.C.T.D."]
        elif "Intelligent UV Mapping" in line:
            new = versions["intelligent_uv"]
        else:
            return line
        return re.sub(r"\| v[0-9][0-9A-Za-z.]* \|", "| v%s |" % new, line, count=1)

    table = "\n".join(patch_table_row(l) for l in text[start:end].splitlines())
    text = text[:start] + table + text[end:]

    # 2) Titoli delle sottosezioni e riferimenti incrociati nel testo.
    #    es. "### DEF Controller Auto (`CTRL_DEF` v0.2.0)" -> nuova versione.
    text = re.sub(
        r"(### BBone to Bones \(v)[0-9][0-9A-Za-z.]*\)",
        r"\g<1>%s)" % versions["BBone to Bones"],
        text,
    )
    text = re.sub(
        r"(### Auto Copy Transforms DEF \(`A\.C\.T\.D\.` v)[0-9][0-9A-Za-z.]*\)",
        r"\g<1>%s)" % versions["A.C.T.D."],
        text,
    )
    text = re.sub(
        r"(### Intelligent UV Mapping \(v)[0-9][0-9A-Za-z.]*\)",
        r"\g<1>%s)" % versions["intelligent_uv"],
        text,
    )
    # Riferimenti incrociati nel testo libero (es. "CTRL_DEF` v0.2.0)").
    text = re.sub(
        r"(`CTRL_DEF` v)[0-9][0-9A-Za-z.]*\)",
        r"\g<1>%s)" % versions["CTRL_DEF"],
        text,
    )
    text = re.sub(
        r"(`A\.C\.T\.D\.` v)[0-9][0-9A-Za-z.]*\)",
        r"\g<1>%s)" % versions["A.C.T.D."],
        text,
    )

    if not text.endswith("\n"):
        text += "\n"
    if text != original:
        README.write_text(text, encoding="utf-8", newline="\n")
    print(
        "SYNC_VERSIONS_OK | bbone_to_bones=v%s | ctrl_def=v%s | actd=v%s | intelligent_uv=v%s"
        % (versions["BBone to Bones"], versions["CTRL_DEF"], versions["A.C.T.D."], versions["intelligent_uv"])
    )
    for avviso in avvisi:
        print("SYNC_VERSIONS_WARN | " + avviso)
    return 0


if __name__ == "__main__":
    sys.exit(main())
