#!/usr/bin/env python3
"""
corpus.py — capa normalizada del corpus: un texto por fuente del programa y un
manifiesto que dice, para cada lectura, de dónde sale el texto y cuánto vale.

Para cada aparición (unidad, citekey) de `programa_uba_v25.md`:

  1. Resuelve el PDF de `Materiales_UBA/UnidadN/` según MAPA (abajo).
  2. Decide la vía de extracción por regla, a partir de la auditoría:
       texto         PDF digital con capa limpia      → pdftotext
       conservar     escaneo con OCR previo aceptable → pdftotext
       ocr           escaneo sin texto                → ocrmypdf
       ocr-forzado   capa basura o fuentes rotas      → ocrmypdf --force-ocr
       partir+ocr    escaneo a doble página           → corte en el lomo + ocrmypdf
  3. Deja el PDF con OCR en `corpus/pdf/<id>.pdf` y el texto en
     `corpus/texto/<id>.txt`, con marcadores `[[PDF p. N]]` que remiten SIEMPRE
     a la página del PDF original (en los partidos, el marcador se repite para
     la mitad izquierda y la derecha, igual que `extraer.py --doble`).
  4. Escribe `corpus/manifiesto.csv` y `corpus/manifiesto.json`.

Nunca modifica `Materiales_UBA/` ni `extractos/`. Es idempotente: no rehace un
OCR existente salvo con --forzar.

Uso:
    python3 scripts/corpus.py                 # todo
    python3 scripts/corpus.py --solo-manifiesto
    python3 scripts/corpus.py --forzar csjn_cha1991
"""
import argparse, csv, datetime, hashlib, io, json, os, re, shutil, subprocess, sys, tempfile, unicodedata

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)
import auditar_corpus as aud  # noqa: E402

RAIZ = os.path.normpath(os.path.join(AQUI, ".."))
MAT = os.path.normpath(os.path.join(RAIZ, "..", "Materiales_UBA"))
PROGRAMA = os.path.normpath(os.path.join(RAIZ, "..", "Programa_UBA", "last_version", "programa_uba_v25.md"))
BIB = os.path.join(RAIZ, "programauba.json")
OUT = os.path.join(RAIZ, "corpus")
UMBRAL = 85  # puntaje mínimo para aceptar una capa de texto existente

# ---------------------------------------------------------------------------
# (unidad, citekey) → regex sobre el nombre del archivo (NFC) en UnidadN/.
# None = no hay PDF. Un tercer elemento opcional fija el id de la fuente cuando
# el PDF no corresponde a la entrada bibliográfica.
# ---------------------------------------------------------------------------
MAPA = {
    (1, "gargarella2009d"): r"^1_Gargarella_2009",
    (1, "holmes1993"): r"^2_Holmes",
    (1, "nino1996a"): r"^Nino_1996",
    (2, "gargarella2015b"): r"^1_Gargarella_2015",
    (2, "pisarello2013"): r"^Pisarello_2013_Un Largo Termidor\.pdf$",
    (3, "saenz2016a"): r"^1_",
    (3, "csjn_fayt1999"): r"^2_CSJN - 1999",
    (3, "csjn_schiffrin2017"): r"^3_CSJN - 2017",
    (3, "quintana1988"): r"^Quintana",
    (4, "gargarella2009c"): r"^1_Gargarella_2009",
    (4, "elfman2019"): r"^2_Elfman",
    (4, "marbury"): r"^3_U\.S\.",
    (4, "csjn_elortondo1888"): r"^4_FALLO",
    (4, "gargarella1996"): r"^Gargarella_1996",
    (4, "csjn_sojo1887"): r"Sojo",
    (4, "csjn_thomas2010"): r"Thomas",
    (4, "highton2014"): r"^Highton",
    (5, "sagues2004"): r"^1_Sag",
    (5, "gargarella2007"): r"^2_Gargarella_2007",
    (5, "gargarella2009a"): r"^3_Gargarella",
    (5, "gargarella2021"): r"^4_Gargarella",
    (5, "scalia1988"): r"^5_Scalia",
    (5, "ely1997"): None,
    (5, "csjn_rizzo2013"): r"Rizzo",
    (5, "csjn_sejean1986"): r"Sejean",
    (5, "nino1992b"): r"^Nino_1992_Interpretaci",
    (5, "fiss2008"): None,
    (6, "saenz2016b"): (r"^1_Saenz 2016", "saenz2016_art14y28"),
    (6, "bouzat2013"): r"^2_Bouzat",
    (6, "csjn_clarin2013"): r"Clar",
    (6, "maurino2011"): r"^Maurino_2011",
    (7, "jgb2008"): r"^1_Gonz",
    (7, "mendez2021"): r"^2_M",
    (7, "csjn_evolucion2023"): r"^4_CSJN_2023",
    (7, "csjn_confederacion2024"): r"^5_CSJN_2024",
    (7, "csjn_shi2021"): r"Shi, Jinchui",
    (7, "csjn_farmacity2021"): r"Farmacity",
    (7, "csjn_esso2021"): r"Esso",
    (7, "csjn_zavalia2006"): r"Zavalia",
    (7, "csjn_ucr2013"): r"^CSJN_2013_UCR",
    (7, "csjn_ucr2018"): None,
    (7, "csjn_ucr2019"): None,
    (7, "csjn_ucr2019b"): None,
    (7, "arballo2019"): r"^Arballo - 2019 - Comentario al art",
    (7, "azrak2018"): r"^Azrak_2018",
    (7, "limanski2016"): r"^Limanski",
    (7, "gervasoni2011"): r"^Gervasoni",
    (8, "abregu1997"): r"^1_Abreg",
    (8, "csjn_ekmekdjian1992"): r"^2_CSJN_1992",
    (8, "csjn_giroldi1995"): None,
    (8, "csjn_esposito2004"): None,
    (8, "csjn_ministerio2017"): r"Ministerio",
    (8, "hitters2009"): r"^Hitters",
    (8, "rosenkrantz2005"): r"^Rosenkrantz",
    (8, "filippini2005"): r"^Filippini",
    (8, "biscardi2016"): r"^Biscardi",
    (9, "rau2019"): r"^1_",
    (9, "guidi2019"): r"^2_Guidi",
    (9, "csjn_famyl2000"): r"^3_CSJN",
    (9, "tula2004"): r"Tula",
    (9, "csjn_bussi2007"): r"Bussi",
    (9, "pearce2019"): None,
    (9, "ley27412"): None,
    (9, "funcionamiento_parlamentario"): None,
    (10, "saenz2019a"): r"^1_S",
    (10, "arballo2019"): (r"^2_Arballo", "arballo2019_art75inc13"),
    (10, "csjn_gcba2021"): r"Gobierno de la Ciudad",
    (10, "gelli2004"): None,
    (10, "bidegain1998"): None,
    (10, "orlando2019"): r"^Orlando",
    (11, "god1991"): r"^1_O'Donnell",
    (11, "saenz2016b"): r"^2_S",
    (11, "alegre2010"): r"^Alegre-Democracia",
    (11, "nino1988"): r"^Nino - 1988",
    (11, "ollier2012"): r"^Ollier",
    (11, "sagues2001"): None,
    (12, "csjn_delfino1927"): r"^1_CSJN",
    (12, "csjn_mouviel1957"): r"^2_CSJN",
    (12, "csjn_peralta1990"): r"^3_CSJN",
    (12, "csjn_verrocchi1999"): r"^4_CSJN",
    (12, "csjn_blanco2018"): r"Blanco",
    (12, "csjn_colegio2008"): r"Colegio P",
    (12, "csjn_consumidores2010"): r"Consumidores",
    (12, "csjn_prattico1960"): r"Prattico",
    (12, "csjn_massa2006"): r"Massa",
    (13, "csjn_siri1957"): r"^1_FALLO",
    (13, "csjn_kot1958"): r"^2_CSJN",
    (13, "csjn_rizzo2013"): r"^3_CSJN_2013",
    (13, "csjn_colegio2021"): r"^4_CSJN",
    (13, "otegui2016"): r"^Otegui",
    (13, "csjn_halabi2009"): r"Halabi",
    (13, "ferreyra2016"): r"^Ferreyra",
    (13, "vergara2016"): r"^Vergara",
    (13, "dassen2016"): r"^Dassen",
    (14, "alegre2020"): r"^1_Alegre",
    (14, "csjn_lee2020"): r"^2_CSJN",
    (14, "csjn_petcoff2020"): r"Petcoff",
    (14, "csjn_ibarrola2021"): r"Ibarrola",
    (15, "gargarella2009e"): r"^2_Gargarella",
    (15, "csjn_cha1991"): r"^3_CSJN_1991",
    (15, "csjn_alitt2006"): r"^4_CSJN",
    (15, "csjn_fal2012"): r"FAL",
    (15, "csjn_castillo2017"): r"Castillo",
    (15, "monti2014"): r"^Monti",
    (15, "faerman2010"): None,
    (15, "maurino2009"): None,
    (15, "csjn_bazterrica1986"): r"Bazterrica",
    (15, "nino1992a"): r"^Nino_1992_El bien",
    (16, "saba2005"): r"^1_Saba.*\.pdf$",
    (16, "treacy2011"): r"^2_Treacy",
    (16, "csjn_gonzalez2000"): r"^3_CSJN.*\.pdf$",
    (16, "csjn_repetto1988"): r"Repetto",
    (16, "csjn_reyes2007"): r"Reyes",
    (16, "saldivia2018"): r"^Saldivia",
    (17, "elias2014a"): r"^1_El",
    (17, "csjn_ercolano1922"): r"^2_CSJN",
    (17, "csjn_coihue2021"): r"Coihue",
    (17, "sola2010a"): r"^Sola",
    (17, "zeberio2006"): r"^Zeberio",
    (17, "saenz2019"): r"^S.enz - 2016 - El derecho de propiedad",
    (17, "csjn_avico1934"): None,
    (18, "courtis2001"): r"^1_Abramovich",
    (18, "csjn_quisbeth2012"): r"^2_CSJN",
    (18, "csjn_salas2011"): r"Salas",
    (18, "gargarella2007a"): r"^Gargarella et al",
    (18, "holmes2015"): r"^Holmes_Sunstein",
    (18, "csjn_benghalensis2000"): r"Benghalensis",
    (18, "csjn_defensor2007"): r"Defensor",
    (18, "csjn_mendoza2008"): r"Mendoza",
}

# Fuentes que, aunque se procesen, no alcanzan el nivel B por la calidad del
# original (decisión tomada mirando la imagen, no el puntaje).
ORIGINAL_DEFICIENTE = {
    "csjn_siri1957": "copia mimeografiada a máquina; reemplazar por Fallos 239:459 impreso",
    "nino1996a": "fotocopia de 1 bit, torcida y subrayada a mano",
}

# Copias revisadas a mano que ya existen en el casebook.
REVISADAS = {"gargarella2009d": "extractos/limpios/gargarella2009d.txt"}

# Problemas bibliográficos y de paginación conocidos (ver AUDITORIA_CORPUS.md y FUENTES.md).
NOTAS = {
    (6, "saenz2016b"): "CLAVE ERRÓNEA: el PDF es «Artículos 14 y 28: poder de policía…»; saenz2016b es «Facultades normativas del PE» (U11)",
    (10, "arballo2019"): "CLAVE ERRÓNEA: el PDF es el comentario al art. 75 inc. 13; arballo2019 es el comentario al art. 121 (U7)",
    (10, "saenz2019a"): "la entrada repite citation-key saenz2019 y omite a Sucunza",
    (15, "gargarella2009e"): "la entrada lleva pp. 173–231 (copiadas de gargarella2009a); hay otra copia rotulada 779–796",
    (18, "courtis2001"): "el PDF es Abramovich y Courtis 2009, no Courtis 2001",
    (17, "saenz2019"): "el PDF está fechado 2016 («…Control de razonabilidad»); verificar edición",
    (5, "scalia1988"): "el PDF es una traducción castellana; la entrada cita el original inglés",
    (4, "marbury"): "el PDF es una traducción castellana sin paginación de U.S.",
    (5, "fiss2008"): "no existe en programauba.json",
    (13, "ferreyra2016"): "la entrada repite las pp. 871–887 de otegui2016",
    (1, "holmes1993"): "sin paginación impresa; la edición del compendio es FCE 1999, pp. 217–262",
    (15, "faerman2010"): "¿corresponde a «Fernández Valle 2010» de la carpeta? Verificar",
}
PAGINACION = {
    "gargarella2009d": "doble página: PDF p. n = impresas 2n+20 / 2n+21",
    "holmes1993": "sin paginación impresa; citar por sección",
    "nino1996a": "impresa = PDF + 12",
    "gargarella2015b": "impresa = PDF + 11",
    "saenz2016a": "sin paginación impresa; citar por apartado",
    "csjn_fayt1999": "citar por considerando",
    "csjn_schiffrin2017": "citar por voto + considerando; impresa = PDF",
}


def nfc(s):
    return unicodedata.normalize("NFC", s)


def leer_programa():
    prog = open(PROGRAMA, encoding="utf-8").read()
    partes = re.split(r"^## Unidad (\d+)\.", prog, flags=re.M)
    filas = []
    for i in range(1, len(partes), 2):
        n, cuerpo = int(partes[i]), partes[i + 1]
        for clase, rot in (("mandatory", "obligatoria"), ("optional", "optativa")):
            m = re.search(r"\{\.%s-refs\}([^:]*)" % clase, cuerpo)
            for k in re.findall(r"@([\w:-]+)", m.group(1) if m else ""):
                filas.append((n, k, rot))
    return filas


def resolver(unidad, patron):
    carpeta = os.path.join(MAT, f"Unidad{unidad}")
    hits = [f for f in sorted(os.listdir(carpeta))
            if f.lower().endswith(".pdf") and re.search(patron, nfc(f))]
    if len(hits) != 1:
        sys.exit(f"MAPA ambiguo o vacío: Unidad{unidad} /{patron}/ → {hits}")
    return os.path.join(carpeta, hits[0])


def via(a):
    q = (a.get("quality") or {}).get("score") or 0
    if a["kind"] in ("scan-no-text", "scan-with-ocr", "mixed") and a["pages_scanned"] and \
            a["pages_landscape"] >= 0.6 * a["pages"]:
        return "partir+ocr"
    if a["kind"] == "scan-no-text":
        return "ocr"
    if q < UMBRAL:
        return "ocr-forzado"
    return "conservar" if a["kind"].startswith("scan") else "texto"


# --------------------------------------------------------------------------- OCR
def partir(pdf, destino):
    """Rasteriza a 300 dpi, corta las hojas apaisadas en el lomo y arma un PDF
    de imágenes. Devuelve el mapa página-salida → (página-original, lado)."""
    import fitz
    from PIL import Image
    from extraer import canal_central
    src = fitz.open(pdf)
    out = fitz.open()
    mapa = []
    with tempfile.TemporaryDirectory() as td:
        for i, p in enumerate(src, 1):
            pix = p.get_pixmap(dpi=300, colorspace=fitz.csGRAY)  # aplica /Rotate
            png = os.path.join(td, f"p{i}.png")
            pix.save(png)
            im = Image.open(png)
            if im.width > im.height * 1.15:
                xi, xd = canal_central(png)
                trozos = [("izq", im.crop((0, 0, xi, im.height))),
                          ("der", im.crop((xd, 0, im.width, im.height)))]
            else:
                trozos = [("", im)]
            for lado, t in trozos:
                buf = io.BytesIO()
                t.save(buf, format="JPEG", quality=80, dpi=(300, 300))
                w, h = t.width * 72 / 300, t.height * 72 / 300
                pg = out.new_page(width=w, height=h)
                pg.insert_image(pg.rect, stream=buf.getvalue())
                mapa.append((i, lado))
    out.save(destino, deflate=True)
    return mapa


def ocrmypdf(entrada, salida, modo):
    """modo: 'nuevo' (sin texto previo: injerta la capa, conserva las imágenes),
    'rehacer' (capa OCR invisible basura: --redo-ocr, conserva las imágenes),
    'forzar' (texto vectorial con fuentes rotas: rasteriza todo)."""
    cmd = ["ocrmypdf", "-l", "spa", "--rotate-pages", "--output-type", "pdf",
           "-j", "8", "--quiet"]
    extra = {"nuevo": [], "rehacer": ["--redo-ocr"], "forzar": ["--force-ocr"]}[modo]
    with tempfile.TemporaryDirectory() as td:
        tmp = os.path.join(td, "salida.pdf")  # se arma fuera de Drive y se copia al final
        r = subprocess.run(cmd + extra + [entrada, tmp], capture_output=True, text=True)
        if r.returncode != 0 and modo != "forzar":
            # imágenes dañadas en el original (p. ej. JPEG corruptos de la Xerox):
            # sólo se pueden recuperar rasterizando
            print(f"    {modo} falló ({r.stderr.strip().splitlines()[-1][:90] if r.stderr.strip() else r.returncode}); reintento con --force-ocr", flush=True)
            modo = "forzar"
            r = subprocess.run(cmd + ["--force-ocr", entrada, tmp], capture_output=True, text=True)
        if r.returncode != 0:
            raise RuntimeError(r.stderr[-800:])
        shutil.copyfile(tmp, salida)
    return modo


def textos_por_pagina(pdf):
    out = subprocess.run(["pdftotext", "-layout", "-q", pdf, "-"],
                         capture_output=True, text=True).stdout.split("\f")
    if out and not out[-1].strip():
        out = out[:-1]
    return out


def escribir_texto(ruta, cab, paginas, mapa):
    partes = [f"# {k}: {v}" for k, v in cab.items()] + [""]
    for txt, (n, lado) in zip(paginas, mapa):
        partes.append(f"[[PDF p. {n}]]" + (f"  <!-- {lado} -->" if lado else ""))
        partes.append(txt.rstrip())
        partes.append("")
    with open(ruta, "w", encoding="utf-8") as f:
        f.write("\n".join(partes))


def md5(ruta):
    h = hashlib.md5()
    with open(ruta, "rb") as f:
        for b in iter(lambda: f.read(1 << 20), b""):
            h.update(b)
    return h.hexdigest()


def procesar(fid, pdf, a, ruta_via, forzar_ocr):
    """Devuelve dict con el resultado de la extracción para una fuente."""
    os.makedirs(os.path.join(OUT, "pdf"), exist_ok=True)
    os.makedirs(os.path.join(OUT, "texto"), exist_ok=True)
    pdf_ocr = os.path.join(OUT, "pdf", f"{fid}.pdf")
    mapa_json = os.path.join(OUT, "pdf", f"{fid}.mapa.json")
    txt = os.path.join(OUT, "texto", f"{fid}.txt")
    cab = {"fuente": os.path.relpath(pdf, MAT), "md5_original": a["md5"], "via": ruta_via}

    if ruta_via in ("texto", "conservar"):
        paginas = textos_por_pagina(pdf)
        mapa = [(i, "") for i in range(1, len(paginas) + 1)]
        origen = pdf
    else:
        if forzar_ocr or not os.path.exists(pdf_ocr):
            t0 = datetime.datetime.now()
            with tempfile.TemporaryDirectory() as td:
                if ruta_via == "partir+ocr":
                    tmp = os.path.join(td, "partido.pdf")
                    mapa = partir(pdf, tmp)
                    cab["modo_ocrmypdf"] = ocrmypdf(tmp, pdf_ocr, "nuevo")
                else:
                    local = os.path.join(td, "orig.pdf")
                    shutil.copyfile(pdf, local)
                    import fitz
                    mapa = [(i, "") for i in range(1, fitz.open(local).page_count + 1)]
                    if ruta_via == "ocr":
                        modo = "nuevo"
                    elif a.get("invisible_text", 0) > 0.5 and a["kind"].startswith("scan"):
                        modo = "rehacer"
                    else:
                        modo = "forzar"
                    cab["modo_ocrmypdf"] = ocrmypdf(local, pdf_ocr, modo)
            json.dump(mapa, open(mapa_json, "w"))
            print(f"    OCR {fid}: {(datetime.datetime.now() - t0).seconds}s", flush=True)
        mapa = [tuple(x) for x in json.load(open(mapa_json))]
        paginas = textos_por_pagina(pdf_ocr)
        origen = pdf_ocr
        cab["motor"] = "ocrmypdf + tesseract spa (300 dpi" + (", partido en el lomo)" if ruta_via == "partir+ocr" else ")")
    cab["generado"] = datetime.date.today().isoformat()
    escribir_texto(txt, cab, paginas, mapa)

    q = aud.text_quality(aud.norm("\n".join(paginas))) or {}
    debiles = sorted({n for t, (n, _) in zip(paginas, mapa)
                      if len(t.strip()) > 300 and ((aud.text_quality(t) or {}).get("score", 100) < 70)})
    vacias = sorted({n for t, (n, _) in zip(paginas, mapa) if len(t.strip()) < 20})
    return dict(pdf_texto=os.path.relpath(origen, RAIZ) if origen != pdf else "(original)",
                texto=os.path.relpath(txt, RAIZ), calidad_final=q.get("score"),
                paginas_debiles=debiles, paginas_vacias=vacias)


def nivel(fid, ruta_via, q):
    if fid in ORIGINAL_DEFICIENTE:
        return "C"
    if q is None:
        return "C"
    if ruta_via == "texto" and q >= 90:
        return "A"
    return "B" if q >= UMBRAL else "C"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--solo-manifiesto", action="store_true",
                    help="no corre OCR nuevo; sólo usa lo ya generado")
    ap.add_argument("--forzar", nargs="*", default=[], help="ids a re-OCRear ('todos' = todos)")
    args = ap.parse_args()

    bib = {x["id"]: x for x in json.load(open(BIB, encoding="utf-8"))}
    filas = leer_programa()
    faltan_mapa = [(n, k) for n, k, _ in filas if (n, k) not in MAPA]
    if faltan_mapa:
        sys.exit(f"apariciones del programa sin entrada en MAPA: {faltan_mapa}")

    cache_aud, cache_proc = {}, {}
    man = []
    for n, k, caracter in filas:
        e = bib.get(k, {})
        au = (e.get("author") or e.get("editor") or [{}])[0]
        yr = (e.get("issued", {}).get("date-parts") or [[""]])[0][0]
        fila = dict(unidad=n, citekey=k, caracter=caracter, tipo_bib=e.get("type", ""),
                    autor=au.get("family") or au.get("literal") or "", anio=yr,
                    titulo=e.get("title", ""), id_fuente="", pdf_original="", md5="",
                    paginas="", tipo_pdf="", doble_pagina="", calidad_original="",
                    via="", pdf_texto="", texto="", calidad_final="", nivel="falta",
                    revisado="no", paginas_debiles="", paginacion=PAGINACION.get(k, ""),
                    notas=NOTAS.get((n, k), ""))
        m = MAPA[(n, k)]
        if m is None:
            fila["via"] = "conseguir PDF"
            man.append(fila)
            continue
        patron, fid = (m if isinstance(m, tuple) else (m, k))
        pdf = resolver(n, patron)
        if pdf not in cache_aud:
            aud.ROOT = MAT
            cache_aud[pdf] = aud.audit(pdf)
        a = cache_aud[pdf]
        rv = via(a)
        clave_proc = (fid, pdf)
        if clave_proc not in cache_proc:
            if args.solo_manifiesto and rv not in ("texto", "conservar") and \
                    not os.path.exists(os.path.join(OUT, "pdf", f"{fid}.pdf")):
                cache_proc[clave_proc] = dict(pdf_texto="", texto="", calidad_final=None,
                                              paginas_debiles=[], paginas_vacias=[])
            else:
                print(f"[{n:>2}] {fid} ← {rv}", flush=True)
                cache_proc[clave_proc] = procesar(fid, pdf, a, rv,
                                                  fid in args.forzar or "todos" in args.forzar)
        r = cache_proc[clave_proc]
        q0 = (a.get("quality") or {}).get("score")
        fila.update(id_fuente=fid, pdf_original=os.path.relpath(pdf, MAT), md5=a["md5"],
                    paginas=a["pages"], tipo_pdf=a["kind"],
                    doble_pagina="si" if rv == "partir+ocr" else "no",
                    calidad_original="" if q0 is None else q0, via=rv,
                    pdf_texto=r["pdf_texto"], texto=r["texto"],
                    calidad_final="" if r["calidad_final"] is None else r["calidad_final"],
                    nivel=nivel(fid, rv, r["calidad_final"]) if r["texto"] else "pendiente",
                    revisado="si" if fid in REVISADAS else "no",
                    paginas_debiles=" ".join(map(str, r["paginas_debiles"])))
        extra = [fila["notas"]] if fila["notas"] else []
        if fid in ORIGINAL_DEFICIENTE:
            extra.append("ORIGINAL DEFICIENTE: " + ORIGINAL_DEFICIENTE[fid])
        if fid in REVISADAS:
            extra.append("copia revisada: " + REVISADAS[fid])
        if r["paginas_vacias"]:
            extra.append("páginas sin texto: " + " ".join(map(str, r["paginas_vacias"])))
        fila["notas"] = "; ".join(extra)
        man.append(fila)

    with open(os.path.join(OUT, "manifiesto.csv"), "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(man[0].keys()))
        w.writeheader()
        w.writerows(man)
    json.dump(man, open(os.path.join(OUT, "manifiesto.json"), "w", encoding="utf-8"),
              ensure_ascii=False, indent=1)
    from collections import Counter
    print("\nniveles:", dict(Counter((r["caracter"], r["nivel"]) for r in man)))
    print("→", os.path.join(OUT, "manifiesto.csv"))


if __name__ == "__main__":
    main()
