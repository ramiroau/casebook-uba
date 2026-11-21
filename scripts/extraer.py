#!/usr/bin/env python3
"""
extraer.py — prepara los archivos de `extractos/` a partir de los PDFs de
`Materiales_UBA/UnidadN/`.

Cada extracto es texto plano con un marcador `[[PDF p. N]]` al inicio de cada
página, de modo que cualquier cita textual del casebook pueda rastrearse hasta
la página del PDF y, a través de FUENTES.md, hasta la página impresa del
original.

Modos:
  --modo texto   pdftotext -layout (PDFs con capa de texto usable)
  --modo ocr     rasteriza a 300 dpi y corre tesseract -l spa
  --doble        (con --modo ocr) el escaneo trae dos páginas impresas por
                 página de PDF: se corta la imagen en el canal central y se
                 reconoce cada mitad por separado, para que el OCR no
                 entrelace las columnas. Cada mitad lleva su propio marcador
                 [[PDF p. N]] (el mismo número dos veces), primero la
                 izquierda.

Uso:
  python3 scripts/extraer.py --modo texto --salida extractos/holmes1993.txt \
      "/ruta/al/archivo.pdf"
  python3 scripts/extraer.py --modo ocr --salida extractos/gargarella2009d.txt \
      "/ruta/al/archivo.pdf"
"""

import argparse
import os
import re
import subprocess
import sys
import tempfile

MARCADOR = "[[PDF p. {}]]"


def paginas(pdf):
    out = subprocess.run(["pdfinfo", pdf], capture_output=True, text=True).stdout
    m = re.search(r"^Pages:\s+(\d+)", out, re.M)
    if not m:
        sys.exit(f"no pude leer la cantidad de páginas de {pdf}")
    return int(m.group(1))


def via_texto(pdf):
    out = subprocess.run(
        ["pdftotext", "-layout", "-q", pdf, "-"],
        capture_output=True, text=True,
    ).stdout
    # pdftotext separa páginas con form feed
    return out.split("\f")


def canal_central(png):
    """Devuelve (x_izq, x_der): dónde termina la página impresa izquierda y dónde
    empieza la derecha.

    El canal entre ambas es la franja con menos tinta entre el 35 % y el 65 %
    del ancho. Pero junto al lomo el escaneo suele traer una banda negra (la
    sombra de la encuadernación) pegada al texto, y tesseract descarta las
    letras que la tocan. Por eso cada mitad se corta donde empieza esa banda,
    no en el centro del canal.
    """
    from PIL import Image
    im = Image.open(png).convert("L")
    w, h = im.size
    px = im.load()
    y0, y1 = int(h * 0.08), int(h * 0.92)   # sin márgenes superior e inferior
    paso = max(1, (y1 - y0) // 400)
    filas = range(y0, y1, paso)

    def tinta(x):
        return sum(px[x, y] < 128 for y in filas) / len(filas)

    xs = range(int(w * 0.35), int(w * 0.65))
    t = {x: tinta(x) for x in xs}
    umbral = min(t.values()) + 0.01
    mejor, inicio = (0, w // 2), None
    for x in xs:
        if t[x] <= umbral:
            inicio = x if inicio is None else inicio
            if x - inicio + 1 > mejor[0]:
                mejor = (x - inicio + 1, inicio + (x - inicio) // 2)
        else:
            inicio = None
    centro = mejor[1]

    # desde el centro hacia cada lado: se saltea la banda de sombra (columnas
    # casi negras) y el corte queda en su borde
    def borde(x, d):
        n = 0
        while 0 < x < w - 1 and n < w // 20:
            x += d
            n += 1
            if t.get(x, tinta(x)) > 0.6:
                while 0 < x < w - 1 and tinta(x) > 0.6:
                    x += d
                return x
        return centro
    return borde(centro, -1), borde(centro, +1)


def ocr(png, idioma):
    r = subprocess.run(
        ["tesseract", png, "stdout", "-l", idioma, "--psm", "1"],
        capture_output=True, text=True,
    )
    return r.stdout


def via_ocr(pdf, dpi=300, idioma="spa", doble=False):
    n = paginas(pdf)
    texto = []
    with tempfile.TemporaryDirectory() as td:
        for p in range(1, n + 1):
            base = os.path.join(td, f"p{p:03d}")
            subprocess.run(
                ["pdftoppm", "-r", str(dpi), "-gray", "-f", str(p), "-l", str(p),
                 "-png", pdf, base],
                check=True, capture_output=True,
            )
            png = next(
                (os.path.join(td, f) for f in sorted(os.listdir(td))
                 if f.startswith(f"p{p:03d}") and f.endswith(".png")),
                None,
            )
            if png is None:
                texto.append("")
                print(f"  p.{p}: sin imagen", file=sys.stderr)
                continue
            if doble:
                from PIL import Image
                im = Image.open(png)
                xi, xd = canal_central(png)
                mitades = []
                for lado, caja in (("izq", (0, 0, xi, im.height)),
                                   ("der", (xd, 0, im.width, im.height))):
                    ruta = f"{base}-{lado}.png"
                    im.crop(caja).save(ruta)
                    mitades.append(ocr(ruta, idioma).rstrip())
                # cada mitad es una página impresa: repetir el marcador
                # permite que las notas al pie se filtren por página y que un
                # párrafo que cruza de una a otra no se corte
                salida = f"\n\n{MARCADOR.format(p)}\n".join(mitades)
            else:
                salida = ocr(png, idioma)
            texto.append(salida)
            print(f"  p.{p}/{n} ocr ok ({len(salida)} car.)", file=sys.stderr)
    return texto


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("pdf")
    ap.add_argument("--modo", choices=["texto", "ocr"], default="texto")
    ap.add_argument("--salida", required=True)
    ap.add_argument("--dpi", type=int, default=300)
    ap.add_argument("--doble", action="store_true",
                    help="dos páginas impresas por página de PDF (sólo OCR)")
    args = ap.parse_args()

    if not os.path.exists(args.pdf):
        sys.exit(f"no existe: {args.pdf}")

    pags = via_texto(args.pdf) if args.modo == "texto" else via_ocr(args.pdf, args.dpi, doble=args.doble)

    partes = [
        f"# fuente: {os.path.basename(args.pdf)}",
        f"# modo: {args.modo}",
        f"# paginas: {len(pags)}",
        "",
    ]
    for i, p in enumerate(pags, start=1):
        if args.modo == "texto" and i == len(pags) and not p.strip():
            continue  # cola vacía que deja el último form feed
        partes.append(MARCADOR.format(i))
        partes.append(p.rstrip())
        partes.append("")

    os.makedirs(os.path.dirname(args.salida), exist_ok=True)
    with open(args.salida, "w", encoding="utf-8") as f:
        f.write("\n".join(partes))
    print(f"→ {args.salida} ({os.path.getsize(args.salida)} bytes)")


if __name__ == "__main__":
    main()
