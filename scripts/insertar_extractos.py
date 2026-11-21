#!/usr/bin/env python3
"""
insertar_extractos.py — expande los marcadores de extracto de las unidades.

Las unidades no transcriben los pasajes largos de las fuentes: los señalan con
un marcador, y este script copia el texto desde `extractos/` en el momento de
compilar. Así el extracto es literal por construcción y el archivo de la unidad
contiene sólo la prosa del autor y las indicaciones de corte.

Sintaxis del marcador (un comentario HTML, invisible si no se expande):

    <!-- EXTRACTO holmes1993
    desde: «La existencia de una “tensión” irreconciliable»
    hasta: «del pensamiento político moderno.»
    desde: «Al ponerlo en entredicho»           (tramos adicionales: opcional)
    hasta: «entre constitucionalismo y»
    despues: «Voto del juez»                    (busca el `desde` siguiente sólo
                                                 después de esta frase: opcional)
    ocurrencia: 2                               (o toma la N-ésima aparición
                                                 del `desde` siguiente: opcional)
    parrafo: «Martin Shapiro ofrece»            (fuerza un punto y aparte)
    unir: «concluye con una afirmación»         (quita un punto y aparte espurio)
    cita: --- Holmes, «El precompromiso…», sección «La tensión…» [@holmes1993]
    -->

- `desde` y `hasta` son anclas: frases cortas y exactas del texto fuente. El
  tramo va desde el comienzo de `desde` hasta el final de `hasta`, inclusive.
  `desde` debe aparecer una sola vez en la fuente; si se repite ---en los
  fallos, cada voto suele reproducir los primeros considerandos---, se
  desambigua con `despues` (la primera aparición posterior a esa frase) o con
  `ocurrencia`. `hasta` se busca después de `desde`, y el `desde` de cada
  tramo adicional, después del tramo anterior. Los espacios, guiones y cortes de renglón no cuentan para la
  comparación (la misma normalización que usa verificar.py).
- Varios pares `desde`/`hasta` producen tramos unidos por `[…]`.
- `parrafo` y `unir` corrigen la reconstrucción de párrafos, que es heurística
  (pdftotext no conserva el punto y aparte).
- `cita` es la línea de atribución, tal cual va debajo del bloque.

Fuentes OCR. Si el extracto de una clave es `# modo: ocr`, se usa
`extractos/limpios/<clave>.txt`, que es una copia corregida a mano contra la
imagen del PDF y debe llevar en su cabecera `# revisado: si`. Si no existe o no
está revisada, el marcador falla, salvo con `--borrador`, que inserta el texto
tal como está precedido de una advertencia visible.

Uso:
    python3 scripts/insertar_extractos.py [--unidades U01 ...] [--salida _build]
                                          [--borrador]
Escribe `<salida>/U0N.md` y un informe por marcador. Sale con código 1 si algún
marcador no se pudo resolver.
"""

import argparse
import bisect
import glob
import os
import re
import sys
from collections import Counter

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from verificar import LIMPIEZA_RE, MARCA_DE_NOTA, NOTA_AL_PIE, norm  # noqa: E402

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EXTRACTOS = os.path.join(RAIZ, "extractos")
LIMPIOS = os.path.join(EXTRACTOS, "limpios")

MARCADOR = re.compile(r"<!--\s*EXTRACTO\s+([A-Za-z0-9_]+)\s*\n(.*?)-->", re.S)
PAGINA = re.compile(r"\[\[PDF p\. (\d+)\]\]")
QUITAR = "\x00"
FIN_DE_PARRAFO = tuple('.:;?!»”")')


class Falla(Exception):
    pass


# --- lectura de la fuente ----------------------------------------------------

def cabecera(texto):
    return dict(re.findall(r"^#\s*(\w+):\s*(.*?)\s*$", texto.split("[[PDF", 1)[0], re.M))


def cargar(clave, borrador):
    """Devuelve (texto del extracto, origen, advertencia o None)."""
    base = os.path.join(EXTRACTOS, f"{clave}.txt")
    if not os.path.exists(base):
        raise Falla(f"no hay extracto para @{clave} en extractos/")
    texto = open(base, encoding="utf-8").read()
    if cabecera(texto).get("modo") != "ocr":
        return texto, "extracto", None

    limpio = os.path.join(LIMPIOS, f"{clave}.txt")
    if os.path.exists(limpio):
        texto_l = open(limpio, encoding="utf-8").read()
        if cabecera(texto_l).get("revisado", "").lower() in ("si", "sí"):
            return texto_l, "limpio", None
        problema = f"extractos/limpios/{clave}.txt no está marcado `# revisado: si`"
        texto = texto_l
    else:
        problema = f"@{clave} es OCR y no tiene extractos/limpios/{clave}.txt"
    if not borrador:
        raise Falla(problema)
    return texto, "ocr sin revisar", problema


def renglones(texto):
    """Lista de (página, renglón) sin mobiliario de página ni notas al pie.

    Los renglones en blanco se conservan como "" porque marcan punto y aparte;
    los que quedan vacíos por limpieza se descartan del todo, para que un
    encabezado quitado en medio de un párrafo no lo corte.
    """
    salida = []
    partes = PAGINA.split(texto)
    for i in range(1, len(partes), 2):
        pag, cuerpo = int(partes[i]), partes[i + 1]
        m = NOTA_AL_PIE.search(cuerpo)
        if m:
            cuerpo = cuerpo[: m.start()]
        for rx in LIMPIEZA_RE:
            cuerpo = rx.sub(QUITAR, cuerpo)
        lineas = []
        for ln in cuerpo.split("\n"):
            if QUITAR in ln and not ln.replace(QUITAR, "").strip():
                continue
            ln = MARCA_DE_NOTA.sub("", ln.replace(QUITAR, "").rstrip())
            lineas.append(ln)
        # los blancos al borde de la página no son punto y aparte
        while lineas and not lineas[0].strip():
            lineas.pop(0)
        while lineas and not lineas[-1].strip():
            lineas.pop()
        salida.extend((pag, ln) for ln in lineas)
    return salida


def sangria(ln):
    return len(ln) - len(ln.lstrip(" "))


def parrafos(rs):
    """Reconstruye párrafos a partir de renglones. Heurística:

    - renglón en blanco → punto y aparte;
    - sangría que aumenta → punto y aparte (sangría de primera línea o comienzo
      de una cita en bloque);
    - sangría que vuelve al margen después de dos o más renglones sangrados →
      punto y aparte (fin de la cita en bloque);
    - renglón anterior corto y terminado en puntuación final → punto y aparte.

    Devuelve una lista de párrafos, cada uno una lista de (página, renglón).
    """
    margen, ancho = {}, {}
    por_pag = {}
    for pag, ln in rs:
        if ln.strip():
            por_pag.setdefault(pag, []).append(ln)
    for pag, lns in por_pag.items():
        margen[pag] = Counter(sangria(l) for l in lns).most_common(1)[0][0]
        largos = sorted(len(l.strip()) for l in lns)
        ancho[pag] = largos[int(len(largos) * 0.9)]

    out, cur, racha = [], [], 0
    for pag, ln in rs:
        if not ln.strip():
            if cur:
                out.append(cur)
            cur, racha = [], 0
            continue
        hondo = sangria(ln) - margen[pag] >= 3
        if cur:
            ppag, prev = cur[-1]
            prev_hondo = sangria(prev) - margen[ppag] >= 3
            corte = (
                (hondo and not prev_hondo)
                or (not hondo and prev_hondo and racha >= 2)
                or (len(prev.strip()) < 0.75 * ancho[ppag]
                    and prev.rstrip().endswith(FIN_DE_PARRAFO))
            )
            if corte:
                out.append(cur)
                cur, racha = [], 0
        racha = racha + 1 if hondo else 0
        cur.append((pag, ln))
    if cur:
        out.append(cur)
    return out


def texto_corrido(texto):
    """Devuelve (T, pagina_de): el texto con párrafos separados por "\\n\\n" y,
    para cada carácter de T, la página del PDF de la que proviene."""
    T, pags = [], []

    def poner(s, pag):
        T.append(s)
        pags.extend([pag] * len(s))

    for i, par in enumerate(parrafos(renglones(texto))):
        if i:
            poner("\n\n", par[0][0])
        for j, (pag, ln) in enumerate(par):
            ln = re.sub(r" {2,}", " ", ln.strip())
            if j:
                prev = T[-1]
                # palabra cortada a fin de renglón: se reúne sin guion
                if re.search(r"[A-Za-zÁÉÍÓÚáéíóúñÑüÜ]-$", prev) and ln[:1].islower():
                    T[-1] = prev[:-1]
                    pags.pop()
                else:
                    poner(" ", pag)
            poner(ln, pag)
    return "".join(T), pags


def normalizado(T):
    """Aplica a T la normalización de verificar.norm carácter por carácter y
    devuelve (N, origen), donde origen[k] es el índice en T del carácter N[k]."""
    N, origen = [], []
    for j, c in enumerate(T):
        r = norm(c) if c not in "…" else "..."
        for x in r:
            N.append(x)
            origen.append(j)
    return "".join(N), origen


# --- marcadores --------------------------------------------------------------

def campos(cuerpo):
    out = []
    for ln in cuerpo.strip().split("\n"):
        m = re.match(r"\s*(desde|hasta|despues|después|ocurrencia|parrafo|párrafo|unir|cita|nota)\s*:\s*(.*)$", ln)
        if not m:
            if ln.strip():
                raise Falla(f"renglón no reconocido en el marcador: {ln.strip()!r}")
            continue
        k, v = m.group(1).replace("á", "a").replace("é", "e"), m.group(2).strip()
        if k != "cita":
            v = re.sub(r"^«(.*)»$", r"\1", v)
        out.append((k, v))
    return out


def buscar(N, ancla, desde_k=0, unica=False, ocurrencia=1):
    a = norm(ancla)
    if len(a) < 12:
        raise Falla(f"ancla demasiado corta para ser inequívoca: «{ancla}»")
    k = desde_k - 1
    for _ in range(ocurrencia):
        k = N.find(a, k + 1)
        if k < 0:
            raise Falla(f"no aparece en la fuente (o no {ocurrencia} veces): «{ancla}»")
    if unica and N.find(a, k + 1) >= 0:
        raise Falla(f"aparece más de una vez en la fuente; alargar el ancla, o "
                    f"usar `despues` u `ocurrencia`: «{ancla}»")
    return k, k + len(a)


def resolver(clave, cuerpo, borrador, cache):
    if clave not in cache:
        texto, origen, aviso = cargar(clave, borrador)
        T, pags = texto_corrido(texto)
        cache[clave] = (T, pags, *normalizado(T), origen, aviso)
    T, pags, N, origen_N, origen, aviso = cache[clave]

    cs = campos(cuerpo)
    pares, cita, forzar, unir = [], None, [], []
    pendiente, despues, ocurrencia = None, None, None
    for k, v in cs:
        if k == "desde":
            if pendiente is not None:
                raise Falla("dos `desde` seguidos sin `hasta`")
            pendiente = (v, despues, ocurrencia)
            despues = ocurrencia = None
        elif k == "hasta":
            if pendiente is None:
                raise Falla("`hasta` sin `desde`")
            pares.append((*pendiente, v))
            pendiente = None
        elif k == "despues":
            despues = v
        elif k == "ocurrencia":
            if not v.isdigit() or int(v) < 1:
                raise Falla(f"`ocurrencia` debe ser un número: {v!r}")
            ocurrencia = int(v)
        elif k == "parrafo":
            forzar.append(v)
        elif k == "unir":
            unir.append(v)
        elif k == "cita":
            cita = v
    if pendiente is not None or not pares:
        raise Falla("cada tramo necesita un `desde` y un `hasta`")
    if not cita:
        raise Falla("falta la línea `cita:`")

    tramos, paginas_usadas = [], []
    fin_k = 0  # los tramos siguientes se buscan después del anterior
    for n, (d, despues, ocurrencia, h) in enumerate(pares):
        if despues:
            _, base_k = buscar(N, despues, desde_k=fin_k)
            i0, _ = buscar(N, d, desde_k=base_k)
        elif ocurrencia or n:
            i0, _ = buscar(N, d, desde_k=fin_k, ocurrencia=ocurrencia or 1)
        else:
            i0, _ = buscar(N, d, unica=True)
        _, i1 = buscar(N, h, desde_k=i0 + 1)
        fin_k = i1
        t0, t1 = origen_N[i0], origen_N[i1 - 1] + 1
        tramos.append((t0, t1))
        paginas_usadas += [pags[t0], pags[t1 - 1]]
    for (a0, a1), (b0, _) in zip(tramos, tramos[1:]):
        if b0 < a1:
            raise Falla("los tramos se superponen o están fuera de orden")

    def ajustar(s, base):
        """Aplica `parrafo` y `unir` dentro del tramo T[base:base+len(s)].

        Las posiciones se calculan sobre el tramo original y los cortes se
        aplican de atrás hacia adelante, para que cada inserción no desplace
        a las siguientes."""
        cortes = []
        for ancla in forzar + unir:
            a = norm(ancla)
            n0 = N.find(a, bisect.bisect_left(origen_N, base))
            if n0 < 0:
                # con varios tramos, el ancla puede caer en uno anterior
                if N.find(a, bisect.bisect_left(origen_N, tramos[0][0])) >= 0:
                    continue
                raise Falla(f"no aparece en la fuente: «{ancla}»")
            t = origen_N[n0] - base
            if not 0 < t < len(s):
                continue  # el ancla cae en otro tramo
            cortes.append((t, ancla in forzar))
        for t, aparte in sorted(cortes, reverse=True):
            antes = s[:t].rstrip(" \n")
            s = antes + ("\n\n" if aparte else " ") + s[t:]
        return s

    texto = ""
    for n, (t0, t1) in enumerate(tramos):
        s = ajustar(T[t0:t1], t0)
        if n:
            hay_aparte = "\n\n" in T[tramos[n - 1][1]:t0]
            texto += " […]" + ("\n\n" if hay_aparte else " ")
        texto += s

    lineas = []
    if aviso:
        lineas += [f"> **[TEXTO OCR SIN REVISAR — {aviso}]**", ">"]
    for par in texto.split("\n\n"):
        lineas += ["> " + par.strip(), ">"]
    lineas.append("> " + cita)

    informe = {
        "clave": clave,
        "origen": origen,
        "tramos": len(tramos),
        "paginas": (min(paginas_usadas), max(paginas_usadas)),
        "palabras": len(texto.split()),
    }
    return "\n".join(lineas), informe


def expandir(texto, borrador=False, cache=None):
    """Devuelve (texto expandido, informes, fallas)."""
    cache = {} if cache is None else cache
    informes, fallas = [], []

    def sub(m):
        clave = m.group(1)
        linea = texto.count("\n", 0, m.start()) + 1
        try:
            bloque, inf = resolver(clave, m.group(2), borrador, cache)
        except Falla as e:
            fallas.append(f"renglón {linea}, @{clave}: {e}")
            return m.group(0)
        inf["renglon"] = linea
        informes.append(inf)
        return bloque

    return MARCADOR.sub(sub, texto), informes, fallas


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--unidades", nargs="*", default=None)
    ap.add_argument("--salida", default=os.path.join(RAIZ, "_build"))
    ap.add_argument("--borrador", action="store_true",
                    help="inserta OCR sin revisar con una advertencia visible")
    args = ap.parse_args()

    archivos = sorted(glob.glob(os.path.join(RAIZ, "unidades", "U*.md")))
    if args.unidades:
        archivos = [a for a in archivos if os.path.basename(a)[:-3] in args.unidades]
    os.makedirs(args.salida, exist_ok=True)

    cache, total_fallas = {}, 0
    for a in archivos:
        nombre = os.path.basename(a)
        exp, infs, fallas = expandir(open(a, encoding="utf-8").read(), args.borrador, cache)
        with open(os.path.join(args.salida, nombre), "w", encoding="utf-8") as f:
            f.write(exp)
        if infs or fallas:
            print(f"{nombre}:")
        for i in infs:
            p0, p1 = i["paginas"]
            pp = f"PDF p. {p0}" if p0 == p1 else f"PDF pp. {p0}–{p1}"
            print(f"  renglón {i['renglon']:>4}  @{i['clave']:<20} {pp:<14} "
                  f"{i['palabras']:>5} palabras  {i['tramos']} tramo(s)  [{i['origen']}]")
        for fl in fallas:
            print(f"  FALLA {fl}")
        total_fallas += len(fallas)

    print(f"→ {os.path.relpath(args.salida, RAIZ)}/ "
          f"({'OK' if not total_fallas else str(total_fallas) + ' marcador(es) sin resolver'})")
    return 1 if total_fallas else 0


if __name__ == "__main__":
    sys.exit(main())
