#!/usr/bin/env python3
"""
paginacion.py — infiere el mapeo `página del PDF → página impresa del original`
leyendo el número que aparece como encabezado o pie en cada página del extracto.

Sirve para que las citas del casebook (`[@holmes1993, p. 231]`) usen la
paginación de la publicación y no el índice del PDF. La inferencia es una
propuesta: el desfase constante que informa al final es lo que se anota en
FUENTES.md, y las excepciones se revisan a mano.

Uso: python3 scripts/paginacion.py extractos/holmes1993.txt
"""

import collections
import re
import sys

MARCADOR = re.compile(r"^\[\[PDF p\. (\d+)\]\]$")
NUM = re.compile(r"\b(\d{1,4})\b")


def candidatos(lineas):
    """Números que aparecen en las 3 primeras o 3 últimas líneas no vacías."""
    utiles = [l.strip() for l in lineas if l.strip()]
    zona = utiles[:3] + utiles[-3:]
    out = []
    for l in zona:
        out += [int(n) for n in NUM.findall(l)]
    return out


def main(path):
    paginas = collections.OrderedDict()
    actual, buf = None, []
    for linea in open(path, encoding="utf-8"):
        m = MARCADOR.match(linea.rstrip("\n"))
        if m:
            if actual is not None:
                paginas[actual] = buf
            actual, buf = int(m.group(1)), []
        elif actual is not None:
            buf.append(linea)
    if actual is not None:
        paginas[actual] = buf

    desfases = collections.Counter()
    detalle = []
    for pdfp, lineas in paginas.items():
        cands = candidatos(lineas)
        # el desfase plausible: impresa - pdf, en un rango razonable
        posibles = sorted({c - pdfp for c in cands if 0 <= c < 2000})
        detalle.append((pdfp, cands[:8], posibles[:8]))
        for d in posibles:
            desfases[d] += 1

    print(f"# {path} — {len(paginas)} páginas de PDF\n")
    print("desfases (impresa - pdf) más frecuentes:")
    for d, n in desfases.most_common(6):
        print(f"  {d:+5d} → aparece en {n} de {len(paginas)} páginas")
    mejor = desfases.most_common(1)[0][0] if desfases else 0
    print(f"\npropuesta: impresa = pdf {mejor:+d}\n")
    print("página por página (pdf | candidatos | impresa propuesta):")
    for pdfp, cands, _ in detalle:
        esperada = pdfp + mejor
        marca = "ok" if esperada in cands else "REVISAR"
        print(f"  {pdfp:4d} | {cands} | {esperada} {marca}")


if __name__ == "__main__":
    main(sys.argv[1])
