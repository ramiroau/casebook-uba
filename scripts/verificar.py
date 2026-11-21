#!/usr/bin/env python3
"""
verificar.py — control de calidad del casebook. Cuatro chequeos:

1. citekeys   Toda clave @foo usada en unidades/*.md existe en programauba.json.
2. citas      Toda cita en bloque (`> …`) aparece literalmente en algún archivo
              de extractos/, comparando con espacios normalizados.
3. cobertura  Toda lectura obligatoria del programa para las unidades escritas
              aparece citada en el archivo de esa unidad.
4. extractos  Todo marcador <!-- EXTRACTO … --> se resuelve contra su fuente
              (ver insertar_extractos.py). El texto insertado es literal por
              construcción, de modo que lo que se controla son las anclas y,
              para fuentes OCR, que exista la copia revisada en
              extractos/limpios/.

Uso: python3 scripts/verificar.py [--unidades U03 U01 ...]
"""

import argparse
import glob
import json
import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROGRAMA = os.path.join(
    RAIZ, "..", "Programa_UBA", "last_version", "programa_uba_v25.md"
)

CLAVE = re.compile(r"@([A-Za-z][A-Za-z0-9_]*[0-9A-Za-z])")
# citas en bloque: líneas que empiezan con ">" y no son la línea de atribución
# (la atribución arranca con una raya o directamente con la clave)
ATRIBUCION = re.compile(r"^>\s*(?:---|\[@)")

# Mobiliario de página: encabezados, pies, carátulas y marcas de continuación
# que el PDF interpone en medio de un párrafo. No es contenido: se descarta
# antes de comparar. Cada patrón corresponde a una fuente identificada en
# FUENTES.md.
LIMPIEZA = [
    r"\[\[PDF p\. \d+\]\]",                      # marcador propio del extracto
    r"-//-",                                     # continuación de página (CSJN)
    r"^\s*-?\s*\d{1,3}\s*-?\s*$",                # pie: -14-
    r"^\s*CSJ \d+/\d+.*$",                       # carátula Schiffrin
    r"^\s*S[ceh]h?iffrin,.*$",
    r"^\s*Nacional\s+s?[i/]?\s*acci[óo]n\s+meramente.*$",
    r"^\s*F\. \d+\. [IVXL]+\.\s*$",              # carátula Fayt
    r"^\s*Fayt, Carlos Santiago c/ Estado Nacional\s*$",
    r"^\s*s/ proceso de conocimiento\.\s*$",
    r"^\s*Corte Suprema de Justicia de la Naci[óo]n\s*$",
    r"^\s*Stephen Holmes\s+El Precompromiso.*$",  # encabezado Holmes
    r"^\s*Tomado de Jon Elster y Rune Slagstad,.*$",  # pie Holmes, PDF p. 1
    r"^\s*páginas 217 a 262\.\s*$",
    r"(?<=esclavo\.)129(?=\s)",                  # Holmes PDF p. 25: llamada de nota pegada al punto
    r"(?<=criminales\.)41(?=\s*$)",             # Holmes PDF p. 7: llamada de nota pegada al punto
    r"(?<=perpetuidad”\.)43(?=\s)",             # Holmes PDF p. 7: llamada de nota pegada al punto
    r"(?<=colectiva\. )\)\s*$",                  # Holmes PDF p. 26: resto de margen
    r"(?<=convencido de )\[ ",                   # Holmes PDF p. 26: resto de margen
    r"^\s*ART[ÍI]CULO 30 – REFORMA DE LA CONSTITUCION\s*$",
    # Sáenz PDF p. 3: la nota 6 sigue en el pie de p. 3 sin número propio, y
    # el corte de notas (primer renglón con sólo un número) la dejaría dentro
    # del cuerpo
    r"^ ?una Constitución\. Para decirlo en términos jurídicos[\s\S]*?págs\. 1/2\.\s*$",
    r"(?<=13\.233)14(?=\.)",                     # Sáenz PDF p. 6: llamada de nota pegada a «13.233»
    r"^\s*8chiffrin,.*$",                        # carátula Schiffrin (variante OCR)
    r"(?<=apartado I del )A(?=Núcleo de Coin)",  # Fayt cons. 15: comillas de apertura mal codificadas («A»)
    r"(?<=Básicas)@(?= incorporado)",           # Fayt cons. 15: comillas de cierre mal codificadas («@»)
    # encabezados Gargarella 2009 (OCR: el número de página puede faltar y el
    # comienzo de la palabra puede perderse en el lomo)
    r"^\s*\d{0,2}\s*INTRODUCCI[ÓO]N\. CONSTITUCI[ÓO]N, IGUALITARISMO Y DEMOCRACIA\s*$",
    r"^\s*\S*STITUCIONALISMO VERSUS DEMOCRACIA\s*\d{0,2}\s*$",
]
# Patrones adicionales por fuente: extractos/limpieza/<clave>.txt, un regex por
# renglón (los renglones vacíos y los que empiezan con «#» se ignoran). Permite
# que cada unidad agregue los suyos sin tocar este archivo.
for _f in sorted(glob.glob(os.path.join(RAIZ, "extractos", "limpieza", "*.txt"))):
    for _ln in open(_f, encoding="utf-8").read().splitlines():
        if _ln.strip() and not _ln.lstrip().startswith("#"):
            LIMPIEZA.append(_ln)
LIMPIEZA_RE = [re.compile(p, re.M) for p in LIMPIEZA]


PAGINA = re.compile(r"\[\[PDF p\. \d+\]\]")
NOTA_AL_PIE = re.compile(r"^\s*\d{1,2}\s*$", re.M)
MARCA_DE_NOTA = re.compile(r"(?<=[a-záéíóúñ)\"])\d{1,2}(?=[\s(,.;:]|$)")


def sin_notas(s):
    """Descarta el bloque de notas al pie de cada página.

    En estos PDFs las notas se imprimen al pie, separadas del cuerpo por una
    línea que contiene sólo el número de la nota. Ese bloque se interpone en
    medio de un párrafo que sigue en la página siguiente, de modo que hay que
    quitarlo para poder verificar una cita que cruza el corte de página.
    """
    salida = []
    for pagina in PAGINA.split(s):
        m = NOTA_AL_PIE.search(pagina)
        salida.append(pagina[: m.start()] if m else pagina)
    return "\n".join(salida)


def norm(s, extracto=False):
    """Reduce un texto a su secuencia de caracteres significativos.

    En los extractos se descarta primero el mobiliario de página ---encabezados,
    pies, carátulas, marcas de continuación y notas al pie--- y se reúnen las
    palabras cortadas a fin de renglón. Después, en ambos lados, se homogeneizan
    comillas y se eliminan guiones, barras y **todos** los espacios.

    Quitar los espacios es necesario porque el texto de estos PDFs mete espacios
    espurios dentro de las palabras ("consti tuyente", "perspecti va"): sin eso,
    ninguna cita de *Schiffrin* verificaría. Lo que se compara es entonces la
    secuencia de caracteres, que sigue siendo una prueba fuerte: una palabra
    cambiada, agregada u omitida hace fallar la comparación igual.
    """
    if extracto:
        s = sin_notas(s)          # necesita los marcadores de página intactos
        for rx in LIMPIEZA_RE:
            s = rx.sub(" ", s)
        s = MARCA_DE_NOTA.sub("", s)
        # palabra cortada a fin de renglón: se reúne antes de tocar los espacios
        s = re.sub(r"[-–—]\s*\n\s*", "", s)
    s = s.replace("‘", "'").replace("’", "'")
    s = s.replace("“", '"').replace("”", '"')
    s = s.replace("…", "...")
    s = re.sub(r"[-–—/]", "", s)
    return re.sub(r"\s+", "", s)


def bloques(texto):
    """Extrae las citas en bloque de un archivo markdown.

    Devuelve pares (cita, visual). `visual` es verdadero cuando la línea de
    atribución lleva la marca `[verif. visual]`, que se usa en las citas tomadas
    de fuentes escaneadas: ahí el extracto es OCR y contiene errores de palabra,
    de modo que la cita se coteja contra la imagen de la página del PDF y no
    contra el extracto. Ver FUENTES.md.
    """
    out, buf, atrib = [], [], None
    for linea in texto.split("\n"):
        if linea.startswith(">"):
            if ATRIBUCION.match(linea) or atrib is not None:
                # la atribución puede ocupar más de un renglón
                atrib = linea if atrib is None else atrib + " " + linea
                continue
            cuerpo = linea[1:].strip()
            if cuerpo:
                buf.append(cuerpo)
        else:
            if buf:
                out.append((" ".join(buf), "verif. visual" in (atrib or "")))
                buf = []
            atrib = None
    if buf:
        out.append((" ".join(buf), "verif. visual" in (atrib or "")))
    return out


def fragmentos(cita):
    """Parte una cita en los tramos separados por [...] o […].

    Devuelve pares (texto legible, texto normalizado): el primero es para el
    mensaje de error, el segundo para la comparación.
    """
    partes = re.split(r"\[\s*(?:\.\.\.|…)\s*\]", cita)
    out = []
    for p in partes:
        legible = re.sub(r"\s+", " ", p).strip()
        if len(norm(p)) > 25:
            out.append((legible, norm(p)))
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--unidades", nargs="*", default=None)
    args = ap.parse_args()

    bib = {e["id"] for e in json.load(open(os.path.join(RAIZ, "programauba.json")))}
    extractos = {}
    for f in glob.glob(os.path.join(RAIZ, "extractos", "*.txt")):
        extractos[os.path.basename(f)[:-4]] = norm(
            open(f, encoding="utf-8").read(), extracto=True
        )

    archivos = sorted(glob.glob(os.path.join(RAIZ, "unidades", "*.md")))
    if args.unidades:
        archivos = [a for a in archivos
                    if os.path.basename(a)[:-3] in args.unidades]

    fallas = 0

    # --- 1. citekeys ---------------------------------------------------------
    print("== citekeys ==")
    usadas = set()
    for a in archivos:
        txt = open(a, encoding="utf-8").read()
        for k in CLAVE.findall(txt):
            usadas.add(k)
    huerfanas = sorted(usadas - bib)
    for k in huerfanas:
        print(f"  FALTA en programauba.json: @{k}")
        fallas += 1
    print(f"  {len(usadas)} claves usadas, {len(huerfanas)} sin entrada")

    # --- 2. citas en bloque --------------------------------------------------
    print("\n== citas en bloque ==")
    total = ok = vis = 0
    for a in archivos:
        for cita, visual in bloques(open(a, encoding="utf-8").read()):
            frs = fragmentos(cita)
            if not frs:
                continue
            total += 1
            encontrada = any(
                all(fr in cuerpo for _, fr in frs) for cuerpo in extractos.values()
            )
            if encontrada:
                ok += 1
            elif visual:
                vis += 1
            else:
                fallas += 1
                print(f"  NO VERIFICADA en {os.path.basename(a)}:")
                for legible, fr in frs:
                    donde = [n for n, c in extractos.items() if fr in c]
                    estado = donde[0] if donde else "NO APARECE"
                    print(f"    [{estado}] {legible[:90]}...")
    print(f"  {ok}/{total} citas verificadas literalmente contra extractos/")
    if vis:
        print(f"  {vis} cotejadas contra la imagen del PDF (fuentes escaneadas)")

    # --- 3. cobertura del programa -------------------------------------------
    print("\n== cobertura del programa ==")
    prog = open(PROGRAMA, encoding="utf-8").read()
    unidades_prog = re.split(r"^## Unidad (\d+)\.", prog, flags=re.M)
    mapa = {}
    for i in range(1, len(unidades_prog), 2):
        n = int(unidades_prog[i])
        cuerpo = unidades_prog[i + 1]
        m = re.search(r"\{\.mandatory-refs\}([^:]*)", cuerpo)
        mapa[n] = CLAVE.findall(m.group(1)) if m else []

    for a in archivos:
        n = int(re.search(r"U(\d+)", os.path.basename(a)).group(1))
        txt = open(a, encoding="utf-8").read()
        faltan = [k for k in mapa.get(n, []) if f"@{k}" not in txt]
        if faltan:
            fallas += 1
            print(f"  U{n:02d}: obligatorias sin citar → {', '.join(faltan)}")
        else:
            print(f"  U{n:02d}: {len(mapa.get(n, []))} obligatorias, todas citadas")

    # --- 4. marcadores de extracto ------------------------------------------
    print("\n== extractos insertados ==")
    from insertar_extractos import expandir
    cache, n_ok, palabras = {}, 0, 0
    for a in archivos:
        _, infs, fls = expandir(open(a, encoding="utf-8").read(), cache=cache)
        n_ok += len(infs)
        palabras += sum(i["palabras"] for i in infs)
        for fl in fls:
            fallas += 1
            print(f"  {os.path.basename(a)}, {fl}")
    print(f"  {n_ok} marcadores resueltos ({palabras} palabras de las fuentes)")

    print(f"\n{'OK' if not fallas else str(fallas) + ' PROBLEMA(S)'}")
    return 1 if fallas else 0


if __name__ == "__main__":
    sys.exit(main())
