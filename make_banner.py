# -*- coding: utf-8 -*-
"""Genera il banner del profilo PieroFra con layout misurato.

Perche' esiste: la prima versione disegnava il testo senza misurare le righe,
quindi il titolo finiva sotto i pannelli e le didascalie si sovrapponevano alle
immagini. Qui ogni riga viene misurata con il font reale e, se non entra nella
colonna sinistra, il banner si ferma con BANNER_FAIL invece di produrre un PNG
sbagliato.
"""

import os
import sys

from PIL import Image, ImageDraw, ImageFont

LARG = 1280
ALT = 360
MARGINE = 48
DIVISORE = 600            # fine della colonna testo: nessuna scritta oltre
COLORE_BG_SX = (20, 20, 24)
COLORE_BG_DX = (34, 34, 42)
ACCENTO = (234, 118, 0)   # arancione Blender
TESTO = (240, 240, 245)
TESTO_TENUE = (176, 176, 188)
BORDO = (58, 58, 68)

FONT_BOLD = r"C:\Windows\Fonts\segoeuib.ttf"
FONT_REG = r"C:\Windows\Fonts\segoeui.ttf"

RADICE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SORGENTE_1 = os.path.join(RADICE, r"_promo_review\DEF_CONTROLLER\featured_1920x1080.png")
SORGENTE_2 = os.path.join(RADICE, r"_promo_review\INTELLIGENT_UV\iuv_featured_1920x1080.png")
# Riserva: se le anteprime locali non ci sono, si usa il primo frame delle GIF
# che vivono nel repository, cosi' il banner resta rigenerabile da chiunque.
RISERVA_1 = os.path.join(RADICE, r"PieroFra\assets\def_controller_demo.gif")
RISERVA_2 = os.path.join(RADICE, r"PieroFra\assets\intelligent_uv_demo.gif")
USCITA = os.path.join(RADICE, "PieroFra", "assets", "banner.png")


def sfondo():
    """Gradiente orizzontale: scuro a sinistra, leggermente piu' chiaro a destra."""
    img = Image.new("RGB", (LARG, ALT))
    disegno = ImageDraw.Draw(img)
    for x in range(LARG):
        t = x / float(LARG - 1)
        colore = tuple(
            int(COLORE_BG_SX[i] + (COLORE_BG_DX[i] - COLORE_BG_SX[i]) * t) for i in range(3))
        disegno.line([(x, 0), (x, ALT)], fill=colore)
    return img


def disponibili(font, testo, larghezza_massima):
    """Spezza il testo in righe che stanno davvero nella larghezza data."""
    parole = testo.split()
    righe = []
    corrente = ""
    for parola in parole:
        prova = (corrente + " " + parola).strip()
        if font.getlength(prova) <= larghezza_massima:
            corrente = prova
        else:
            if corrente:
                righe.append(corrente)
            corrente = parola
    if corrente:
        righe.append(corrente)
    return righe


def apri_sorgente(percorso, riserva):
    """Apre l'anteprima locale; se manca, usa il primo frame della GIF del repo."""
    if os.path.isfile(percorso):
        return Image.open(percorso).convert("RGB")
    if os.path.isfile(riserva):
        foto = Image.open(riserva)
        foto.seek(0)
        return foto.convert("RGB")
    return None


def main():
    foto_1 = apri_sorgente(SORGENTE_1, RISERVA_1)
    foto_2 = apri_sorgente(SORGENTE_2, RISERVA_2)
    for nome, foto in (("pannello DEF Controller", foto_1),
                       ("pannello Intelligent UV", foto_2)):
        if foto is None:
            print("BANNER_FAIL | manca | " + nome)
            return 1

    img = sfondo()
    disegno = ImageDraw.Draw(img)

    titolo = ImageFont.truetype(FONT_BOLD, 36)
    occhiello = ImageFont.truetype(FONT_BOLD, 13)
    sottotitolo = ImageFont.truetype(FONT_BOLD, 20)
    corpo = ImageFont.truetype(FONT_REG, 15)
    didascalia = ImageFont.truetype(FONT_BOLD, 15)

    colonna_sx = MARGINE
    larghezza_testo = DIVISORE - MARGINE - 28      # aria a sinistra del divisore
    problemi = []

    def scrivi(testo, font, y, colore, larghezza=larghezza_testo, x=colonna_sx):
        for riga in disponibili(font, testo, larghezza):
            larga = font.getlength(riga)
            if larga > larghezza:
                problemi.append("riga troppo larga: {0}".format(riga))
            if x + larga > DIVISORE:
                problemi.append("riga oltre il divisore: {0}".format(riga))
            disegno.text((x, y), riga, font=font, fill=colore)
            y += int(font.size * 1.35)
        return y

    # --- colonna sinistra -------------------------------------------------
    y = 74
    disegno.text((colonna_sx, y), "BLENDER TECHNICAL ART", font=occhiello, fill=ACCENTO)
    y = 100
    y = scrivi("Pierfrancesco Diodato", titolo, y, TESTO)
    y = scrivi("(PieroFra) - Blender add-on development", sottotitolo, y - 2, ACCENTO)
    y += 10
    y = scrivi("Rigging automation, non-destructive transforms, UV pipelines.",
               corpo, y, TESTO_TENUE)
    y = scrivi("Blender 4.2 LTS through 5.2+", corpo, y, TESTO_TENUE)
    y = scrivi("644 verified checks, 15 releases, 2 add-ons live on Blender Extensions.",
               corpo, y, TESTO_TENUE)

    if y > ALT - 20:
        problemi.append("colonna sinistra fuori altezza: {0} px".format(y))

    # divisore verticale, mai attraversato dal testo
    disegno.line([(DIVISORE, 58), (DIVISORE, ALT - 58)], fill=BORDO, width=1)

    # --- due pannelli a destra -------------------------------------------
    area_x = DIVISORE + 20
    area_l = LARG - MARGINE - area_x
    spazio = 22
    larg_pannello = (area_l - spazio) // 2
    alt_pannello = int(round(larg_pannello * 9 / 16.0))
    testo_didascalia = 24
    blocco = alt_pannello + testo_didascalia
    y_pannello = max(48, (ALT - blocco) // 2)

    pannelli = [
        (foto_1, "DEF Controller Auto v0.2.0"),
        (foto_2, "Intelligent UV Mapping v0.35.1"),
    ]

    for indice, (foto, etichetta) in enumerate(pannelli):
        x = area_x + indice * (larg_pannello + spazio)
        # crop centrale con lo stesso rapporto del riquadro, mai stiramento
        rapporto = larg_pannello / float(alt_pannello)
        l, a = foto.size
        if l / float(a) > rapporto:
            nuova_l = int(round(a * rapporto))
            riquadro = ((l - nuova_l) // 2, 0, (l + nuova_l) // 2, a)
        else:
            nuova_a = int(round(l / rapporto))
            riquadro = (0, (a - nuova_a) // 2, l, (a + nuova_a) // 2)
        foto = foto.crop(riquadro).resize((larg_pannello, alt_pannello), Image.LANCZOS)
        img.paste(foto, (x, y_pannello))
        disegno.rectangle(
            [(x, y_pannello), (x + larg_pannello - 1, y_pannello + alt_pannello - 1)],
            outline=BORDO, width=1)

        # didascalia su riga propria, sotto il pannello: mai sopra l'immagine
        y_did = y_pannello + alt_pannello + 8
        if y_did + testo_didascalia > ALT - 8:
            problemi.append("didascalia fuori dal banner: {0}".format(etichetta))
        disegno.text((x, y_did), etichetta, font=didascalia, fill=TESTO)

    # --- barra accento ----------------------------------------------------
    disegno.rectangle([(0, 0), (6, ALT - 1)], fill=ACCENTO)

    if problemi:
        print("BANNER_FAIL | problemi={0}".format(len(problemi)))
        for problema in problemi:
            print("  " + problema)
        return 1

    os.makedirs(os.path.dirname(USCITA), exist_ok=True)
    img.save(USCITA, "PNG", optimize=True)

    # controlli sul file scritto: dimensioni e non-piatto
    prova = Image.open(USCITA).convert("L")
    pixel = list(prova.getdata())
    media = sum(pixel) / float(len(pixel))
    varianza = sum((p - media) ** 2 for p in pixel) / float(len(pixel))
    deviazione = varianza ** 0.5
    if prova.size != (LARG, ALT):
        print("BANNER_FAIL | dimensioni={0}".format(prova.size))
        return 1
    if deviazione < 8.0:
        print("BANNER_FAIL | immagine piatta std={0:.1f}".format(deviazione))
        return 1

    print("BANNER_OK | file={0} | dim={1}x{2} | peso={3:.0f}KB | std={4:.1f}".format(
        os.path.basename(USCITA), LARG, ALT, os.path.getsize(USCITA) / 1024.0, deviazione))
    return 0


if __name__ == "__main__":
    sys.exit(main())
