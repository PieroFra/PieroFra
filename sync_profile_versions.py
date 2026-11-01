# -*- coding: utf-8 -*-
"""Sincronizza automaticamente le versioni degli add-on nel README del profilo
PieroFra con le versioni reali dichiarate nei manifest dei singoli progetti.

Sorgenti letti (blender_manifest.toml di ogni progetto):
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

# Mapping: (nome visualizzato, file manifest, chiave di ricerca nel titolo)
PROJECTS = [
    ("CTRL_DEF", WORKSPACE / "CTRL_DEF" / "blender_manifest.toml", "CTRL_DEF"),
    ("A.C.T.D.", WORKSPACE / "ACTD" / "packaging" / "blender_manifest.toml", "A.C.T.D."),
    ("intelligent_uv", WORKSPACE / "intelligent_uv" / "blender_manifest.toml", None),
]


def read_version(manifest_path: Path) -> str:
    """Estrae 'version = "X.Y.Z"' da un blender_manifest.toml (solo stdlib)."""
    text = manifest_path.read_text(encoding="utf-8")
    match = re.search(r'^version\s*=\s*"([0-9A-Za-z.]+)"', text, re.MULTILINE)
    if not match:
        raise ValueError("Versione non trovata in %s" % manifest_path)
    return match.group(1)


def main() -> int:
    versions = {}
    for name, manifest, _title_key in PROJECTS:
        try:
            versions[name] = read_version(manifest)
        except (OSError, ValueError) as exc:
            print("SYNC_VERSIONS_FAIL | manifest non leggibile: %s | %s" % (manifest, exc))
            return 1

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
        if "CTRL_DEF" in line:
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
        "SYNC_VERSIONS_OK | ctrl_def=v%s | actd=v%s | intelligent_uv=v%s"
        % (versions["CTRL_DEF"], versions["A.C.T.D."], versions["intelligent_uv"])
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
