# Auditoría del corpus de PDFs — 2026-11-19

> **Estado (2026-11-19):** el OCR de §2 y §3 está hecho con `scripts/corpus.py`
> (23 fuentes). El estado de cada lectura está en `corpus/manifiesto.csv`:
> obligatorias 35 A · 14 B · 1 C (*Siri*); optativas 47 A · 15 B · 1 C
> (`nino1996a`) · 16 sin PDF. Siguen pendientes los reemplazos de fuente y las
> correcciones bibliográficas, que no son trabajo de OCR.

Alcance: los 158 PDFs de `../Materiales_UBA/` (carpetas `UnidadN`, `ciudadania`,
`feminismo`, `Unidad20_no_entra`). Se excluyen `TPs_1` y `TPs_2` (trabajos de
estudiantes). Ningún archivo original fue modificado.

Reproducir: `python3 -I scripts/auditar_corpus.py "../Materiales_UBA"` →
`auditoria_corpus.json` (una fila por PDF: páginas, capa de texto, escaneo,
apaisado/rotación, texto invisible, calidad, md5).

**Puntaje de calidad (0–100).** Es una heurística, no una tasa de error: mide la
proporción de palabras funcionales del castellano y penaliza letras sueltas y
tokens que mezclan letras con dígitos. Un texto limpio da más de 90. Una capa con
letras separadas por espacios («L A S A L A») da 0.

## 1. Panorama

| Tipo | PDFs | Qué implica |
|---|---|---|
| Digital (texto nativo) | 109 (2 con fuentes rotas) | `pdftotext` alcanza; las citas se verifican por `grep` |
| Escaneo con OCR previo | 23 | Hay que medir la capa: en 6 es inservible |
| Escaneo sin texto | 26 | Necesita OCR |

- Ningún PDF está cifrado ni falló al abrirse.
- La mayoría de los escaneos están a 300 dpi; ninguno tiene una resolución que impida el OCR.
- La prueba de OCR nuevo (`tesseract -l spa --psm 1`, 300 dpi) dio puntaje
  91–100 en todas las lecturas problemáticas, salvo *Siri*.

## 2. Lecturas obligatorias (programa v25): estado y acción

Todas las obligatorias tienen PDF. Las que no figuran en la tabla son digitales
y limpias (puntaje > 90).

| U | Citekey | Archivo | Problema | Acción |
|---|---|---|---|---|
| 1 | `gargarella2009d` | `1_Gargarella_2009_…` | Escaneo a doble página, rotado, sin texto | Ya resuelto (`limpios/`, revisado) |
| 1 | `holmes1993` | `2_Holmes…` | Digital, pero es una retranscripción con erratas | Ya documentado en FUENTES |
| 2 | `gargarella2015b` | `1_Gargarella_2015_…` | Capa OCR invisible **basura** (puntaje 0) | Re-OCR forzado (prueba: 97) |
| 3 | `csjn_schiffrin2017` | `3_CSJN - 2017 - Schifrin…` | Escaneo con OCR aceptable (96) | Usable; citas en bloque con verif. visual |
| 4 | `csjn_elortondo1888` | `4_FALLO XXXIII. .pdf` | Texto nativo con **codificación de fuentes rota** (basura) | Rasterizar y re-OCR (prueba: 85; la ortografía de 1888, «sinó», «á», es del original) |
| 5 | `gargarella2009a` | `3_Gargarella-La dificultosa tarea…(versión más clara)` | Doble página, rotado, sin texto | Partir hojas y OCR (prueba: 97). Hay otra versión con capa basura (`Gargarella_2009_…2.pdf`) |
| 5 | `gargarella2021` | `4_Gargarella_El derecho como una conversación…` | Escaneo sin texto (400 dpi) | OCR (prueba: 100) |
| 5 | `scalia1988` | `5_Scalia_1988_…` | Es una **traducción castellana**; la bibliografía cita el original (p. 849) | Decidir qué se cita |
| 4 | `marbury` | `3_U.S._1803_Marbury v Madison.pdf` | **Traducción** (¿abreviada?), sin la paginación de U.S. | Igual que Scalia |
| 6 | `saenz2016b` | `1_Saenz 2016.pdf` | **Clave equivocada**: el PDF es «Artículos 14 y 28: poder de policía…»; `saenz2016b` es «Facultades normativas del PE» (U11) | Nueva entrada bibliográfica para U6 |
| 10 | `arballo2019` | `2_Arballo - 2019 - Comentario al 75.13.pdf` | **Clave equivocada**: `arballo2019` es el comentario al art. 121 (U7) | Nueva entrada para art. 75 inc. 13 |
| 10 | `saenz2019a` | `1_Sáenz and Sucunza…75.12` | El campo `citation-key` repite `saenz2019`; falta Sucunza como autor | Corregir la entrada |
| 13 | `csjn_siri1957` | `1_FALLO CCXXXIX. .pdf` | Copia mimeografiada a máquina; la capa existente da 11 y el re-OCR sigue con errores en cada renglón | **Reemplazar la fuente** (Fallos 239:459 impreso o SAIJ); si no, transcribir a mano |
| 13 | `csjn_kot1958` | `2_CSJN - 1958 - Samuel, Kot…` | Doble página, 1 bit, 200 dpi, sin texto | Partir y OCR (prueba: 91) |
| 13 | `csjn_rizzo2013` | `3_CSJN_2013_Rizzo…` | Escaneo con OCR (91) | Usable con verif. visual |
| 15 | `gargarella2009e` | `2_Gargarella - 2009 - Constitucionalismo y Privacidad.pdf` | Sin texto. La entrada lleva pp. 173–231, copiadas de `gargarella2009a`; la otra copia se llama `779-796 …` | OCR (prueba: 97) y corregir páginas |
| 15 | `csjn_cha1991` | `3_CSJN_1991_Comunidad Homosexual…` | 95 pp. con **codificación de fuentes rota** (puntaje 0) | Rasterizar y re-OCR (prueba: 96) |
| 17 | `elias2014a` | `1_Elías_2014_…` | Doble página, rotado, sin texto, ~100 dpi por página | Partir y OCR (prueba: 98) |
| 17 | `csjn_ercolano1922` | `2_CSJN - 1922 - Ercolano…` | Doble página, 200 dpi, sin texto | Partir y OCR (prueba: 96) |
| 18 | `courtis2001` | `1_Abramovich_Courtis_2009_…` | **Autor, año y título** del PDF no coinciden con la entrada; escaneo rotado, sin texto | Decidir la edición; OCR (prueba: 94) |

Además:

- La carpeta de U7 salta del `2_` al `4_`: no hay `3_`. ¿Hay una lectura retirada?
- En U12 hay dos obligatorias de la década de 1950. Son digitales, pero conviene
  verificar que sean versiones completas.

## 3. Optativas

**Sin PDF en la carpeta (16):**

- **U5:** `ely1997`; `fiss2008`, que además **no existe** en `programauba.json`.
- **U7:** `csjn_ucr2018`, `csjn_ucr2019`, `csjn_ucr2019b`.
- **U8:** `csjn_giroldi1995`, `csjn_esposito2004`.
- **U9:** `pearce2019`, `ley27412`, `funcionamiento_parlamentario`.
- **U10:** `gelli2004`, `bidegain1998`.
- **U11:** `sagues2001`.
- **U15:** `faerman2010` (¿será el «Fernández Valle 2010»?), `maurino2009`.
- **U17:** `csjn_avico1934`.

**Con PDF pero sin texto utilizable:**

- **Escaneo sin texto:** `quintana1988`, `csjn_clarin2013` (392 pp.),
  `csjn_ucr2013`, `nino1992b`, `csjn_prattico1960`, `csjn_bazterrica1986`
  (87 pp.), `csjn_repetto1988`.
- **OCR existente de mala calidad:** `nino1996a` (0; fotocopia de 1 bit),
  `nino1988` (40), `nino1992a` (79).

`saenz2019` («El derecho de propiedad») corresponde a un PDF fechado 2016
(`Sáenz - 2016 - El derecho de propiedad…`): hay que verificar la edición.

## 4. Duplicados y material fuera del programa

- **Copias idénticas (md5):** 15 pares. Rizzo (U5 y U13), González de Delgado
  (U15 y U16), Clarín y Nino 1992, *Garantías* (U6 y U20), y seis textos
  repetidos entre U4 y U8, entre otros. No hacen daño, pero el manifiesto debe
  apuntar a una sola copia canónica por citekey.
- **Mismo texto con distinta calidad:**
  - Gargarella 2009a: dos PDFs. Se usa la «versión más clara».
  - Gargarella 2009e: dos PDFs.
  - Gargarella 2015b: tres PDFs (el canónico y dos recortes del capítulo).
  - Pisarello: dos PDFs («firmado» y sin firmar).
- **Sin citekey:** Ruiz Miguel (U1), Convención 1853 (U2; OCR de puntaje 26),
  Rosanvallon (U3), Gargarella 2019 *Preámbulo* (U5), CIDH 2010 (U6), Azrak 2016
  (U7), Di Mascio, Uriarte, *Federalista* y otros (U13), y las carpetas
  `ciudadania` y `feminismo`.

## 5. Diagnóstico para el canal de extracción actual

`scripts/extraer.py` elige entre `texto` y `ocr` a mano, archivo por archivo.
La auditoría muestra tres casos que esa elección no cubre bien:

1. **Capa de texto presente pero basura.** Afecta a gargarella2015b,
   elortondo1888, cha1991, siri1957 y Gargarella 2009a (versión alternativa).
   `--modo texto` produce basura sin dar error. Antes de extraer hay que medir la
   calidad y rechazar las capas que no pasen el umbral.
2. **Codificación de fuentes rota en PDFs «digitales».** Afecta a CHA y
   Elortondo. Tampoco sirve `ocrmypdf --redo-ocr`: hace falta `--force-ocr`, que
   rasteriza la página.
3. **Doble página y rotación.** Afecta a 9 archivos, 5 de ellos obligatorios.
   `--doble` resuelve el corte, pero no detecta solo ni la rotación (`/Rotate`
   90/270) ni si la hoja es doble.

Ninguno de estos casos aparece hoy en un manifiesto. El estado de cada fuente
vive en la prosa de `FUENTES.md`.
