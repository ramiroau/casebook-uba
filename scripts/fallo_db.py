#!/usr/bin/env python3
"""fallo_db.py — texto de un fallo de la CSJN desde la base del observatorio.

    python3 scripts/fallo_db.py TOMO PAGINA [--salida extractos/<clave>.txt]
                                [--fuente documento|volumen] [--hasta PAG]

Dos fuentes posibles en ~/Documents/observatorio-csjn/data/csjn.db:

- `volumen` (por defecto para fallos anteriores a ~1995): OCR de las páginas
  del tomo impreso de Fallos (tabla vol_page). Suele ser mucho mejor que los
  escaneos del compendio. Cada página va marcada `[[PDF p. N]]` con N = página
  impresa de Fallos. El fallo termina donde empieza el siguiente según
  vol_start (o en --hasta).
- `documento`: texto del PDF del fallo publicado por la Corte (tabla
  documento). Bueno para fallos recientes; para los viejos suele ser basura.

La salida lleva cabecera `# modo: ocr` (volumen) o `# modo: texto`
(documento). Para `ocr`, insertar_extractos.py exige la copia corregida en
extractos/limpios/. Sólo lectura sobre la base.
"""
import argparse
import os
import sqlite3
import subprocess
import sys
from datetime import date

DB = os.path.expanduser("~/Documents/observatorio-csjn/data/csjn.db")


def dz(blob):
    return subprocess.run(["zstd", "-dcf"], input=blob, capture_output=True,
                          check=True).stdout.decode("utf-8", "replace")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("tomo", type=int)
    ap.add_argument("pagina", type=int)
    ap.add_argument("--salida")
    ap.add_argument("--fuente", choices=["volumen", "documento"])
    ap.add_argument("--hasta", type=int, help="última página impresa a incluir")
    a = ap.parse_args()
    con = sqlite3.connect(f"file:{DB}?mode=ro", uri=True)

    fuente = a.fuente or ("volumen" if a.tomo < 318 else "documento")
    out = []
    if fuente == "documento":
        r = con.execute("select text, n_pages from documento where tomo=? and pagina=? "
                        "and text_status='ok' order by n_words desc limit 1",
                        (a.tomo, a.pagina)).fetchone()
        if not r:
            sys.exit("sin documento con texto para ese fallo")
        cab = f"# fuente: csjn.db documento, Fallos {a.tomo}:{a.pagina}\n# modo: texto\n"
        # el texto del documento no tiene cortes de página fiables: una sola marca
        out.append("[[PDF p. 1]]\n" + dz(r[0]))
    else:
        r = con.execute("select vol_id from vol_start where tomo=? and pagina=? "
                        "order by source limit 1", (a.tomo, a.pagina)).fetchone()
        if not r:
            sys.exit("el fallo no está ubicado en vol_start")
        vol = r[0]
        if a.hasta:
            fin = a.hasta
        else:
            n = con.execute("select min(pagina) from vol_start where tomo=? and pagina>?",
                            (a.tomo, a.pagina)).fetchone()[0]
            fin = n if n else a.pagina + 40   # incluye la página donde empieza el siguiente
        filas = con.execute("select printed, text from vol_page where vol_id=? and "
                            "printed between ? and ? order by pdf_page",
                            (vol, a.pagina, fin)).fetchall()
        if not filas:
            sys.exit("sin páginas OCR del tomo")
        cab = (f"# fuente: csjn.db vol_page (tomo impreso de Fallos, vol_id {vol}), "
               f"Fallos {a.tomo}:{a.pagina}-{fin}\n# modo: ocr\n"
               "# paginacion: [[PDF p. N]] = página impresa de Fallos\n")
        for printed, t in filas:
            out.append(f"[[PDF p. {printed}]]\n" + dz(t))
    texto = cab + f"# generado: {date.today()}\n\n" + "\n\n".join(out) + "\n"
    if a.salida:
        open(a.salida, "w", encoding="utf-8").write(texto)
        print(f"→ {a.salida}")
    else:
        sys.stdout.write(texto)


if __name__ == "__main__":
    main()
