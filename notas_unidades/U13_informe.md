# Informe — Unidad 13. Poder judicial (noviembre de 2026)

## Archivos escritos o modificados

- `unidades/U13.md` (nueva) y su copia `respaldos/U13_agente.md`.
- `extractos/csjn_siri1957.txt`, `extractos/csjn_kot1958.txt`, `extractos/csjn_rizzo2013.txt` (OCR de los tomos impresos de Fallos, `# modo: ocr`) y `extractos/csjn_colegio2021.txt` (texto nativo).
- `extractos/limpios/csjn_siri1957.txt`, `csjn_kot1958.txt`, `csjn_rizzo2013.txt` (corregidas en las páginas extractadas, `# revisado: si`).
- `extractos/limpieza/csjn_colegio2021.txt` (carátula de las páginas impares).
- `notas_unidades/U13_fuentes.md`, este informe.
- No se tocaron scripts, `FUENTES.md`, `README.md`, `casebook.md`, `programauba.json` ni archivos de otras unidades. No se corrió `build_casebook.sh`.

## Palabras

Prosa propia (incluye fichas, encuadres, notas y síntesis; sin extractos ni marcadores): unas **4.150**, dentro del objetivo de 3.000–4.500. No se rellenó.

## Verificación

`insertar_extractos.py --unidades U13` → OK (17 marcadores). `verificar.py --unidades U13` → **OK**: 9 citekeys, todas en `programauba.json`; 0 citas en bloque escritas a mano (todo va por marcador); cobertura: las 4 obligatorias citadas; 17 extractos resueltos (18.389 palabras). Citas con `[verif. visual]`: 0 (las fuentes OCR van por `limpios/` revisados).

## Extractos

| Fuente | Tramo | Páginas | Palabras | Origen |
|---|---|---|---|---|
| `csjn_siri1957` | voto que encabeza, últimos considerandos | Fallos 239:463–464 | 557 | limpio |
| `csjn_siri1957` | disidencia de Herrera | Fallos 239:466–467 | 660 | limpio |
| `csjn_kot1958` | voto que encabeza (1) | Fallos 241:298–300 | 889 | limpio |
| `csjn_kot1958` | voto que encabeza (2) y parte dispositiva | Fallos 241:300–305 | 1.716 | limpio |
| `csjn_kot1958` | disidencia, cons. 1–5 | Fallos 241:306–309 | 1.288 | limpio |
| `csjn_kot1958` | disidencia, cons. 11–12 | Fallos 241:312–313 | 456 | limpio |
| `csjn_rizzo2013` | voto que encabeza, cons. 10–13 | Fallos 336:784–786 | 765 | limpio |
| `csjn_rizzo2013` | voto que encabeza, cons. 16–20 | Fallos 336:787–791 | 1.106 | limpio |
| `csjn_rizzo2013` | voto que encabeza, cons. 21–28 | Fallos 336:791–797 | 1.820 | limpio |
| `csjn_rizzo2013` | voto que encabeza, cons. 29–35 | Fallos 336:797–800 | 1.089 | limpio |
| `csjn_rizzo2013` | Petracchi y Argibay, cons. 11–14 | Fallos 336:814–816 | 597 | limpio |
| `csjn_rizzo2013` | Zaffaroni, cons. 4–6 | Fallos 336:820–822 | 633 | limpio |
| `csjn_rizzo2013` | Zaffaroni, cons. 11–16 | Fallos 336:825–831 | 1.936 | limpio |
| `csjn_colegio2021` | voto que encabeza, cons. 6–7 | PDF 5–9 | 1.023 | extracto (texto) |
| `csjn_colegio2021` | voto que encabeza, cons. 9–15 | PDF 14–22 | 1.880 | extracto (texto) |
| `csjn_colegio2021` | voto que encabeza, cons. 17 | PDF 23–26 | 743 | extracto (texto) |
| `csjn_colegio2021` | Lorenzetti, cons. 13–15 | PDF 42–48 | 1.231 | extracto (texto) |

## Elección del texto de cada fallo

- *Siri*: el PDF del compendio es una copia mecanografiada de mala calidad (el manifiesto la marca nivel C). Se usó el OCR del tomo impreso de Fallos 239 (bueno) y se cotejó con la copia del compendio.
- *Kot*: el compendio reproduce el tomo impreso; el OCR del tomo en `csjn.db` es más completo que el del escaneo a doble página, pero confunde «c»/«e». Corregido contra la imagen del compendio. `fallo_db.py` no encuentra el fallo en `vol_start`; se leyó `vol_page` directamente (sólo lectura). El campo `documento` de la base para 241:291 es basura.
- *Rizzo*: tres textos posibles (capa OCR del escaneo del compendio, OCR del PDF de la Corte en `documento`, OCR del tomo impreso). Se eligió el del tomo, que es el más limpio, y se corrigió con un cotejo palabra por palabra contra la capa del compendio, resolviendo cada discrepancia con la imagen.
- *Colegio de Abogados*: texto nativo del PDF de la Corte.

## Discrepancias y pendientes

- Notas de clase vs. fuentes: ver `U13_fuentes.md` (enumeración de los vicios de la ley 26.855 en *Rizzo*, cons. 29 frente a cons. 36–40).
- Ferreyra cita *Siri* como Fallos 329:459 (es 239:459).
- **Comillas de *Colegio de Abogados***: la capa de texto del PDF codifica las comillas como «―…‖» (p. ej. «―Monner Sans‖»), y así salen en el extracto. No se pueden reemplazar con `limpieza/` (sólo borra). Propuesta: una normalización `―`→`“`, `‖`→`”` para esta fuente en `insertar_extractos.py`, o pasarla a `limpios/`. Queda a decisión del coordinador.
- *Colegio de Abogados*, cons. 17: el PDF trae «paralizació n del f uncionamiento» y «operará n», con espacios espurios; salen así en el extracto. Mismo remedio que el anterior.
- Detalle técnico (para el coordinador): `cabecera()` en `insertar_extractos.py` corta en el primer `[[PDF` del archivo, de modo que una línea de cabecera como `# paginacion: [[PDF p. N]] = …` antes de `# revisado: si` hace que la copia figure como no revisada. Lo resolví en mis archivos cambiando la redacción; `extractos/limpios/csjn_elortondo1888.txt` (de otra unidad) tiene esa línea.
- No hay `[PENDIENTE]` abiertos en la unidad.

## Ediciones del autor

Unidad nueva: no había ediciones del autor que conservar ni marcadores `AUTOR`.

## Decisiones de criterio para revisar

1. **Estructura en dos líneas jurisprudenciales** (amparo: *Siri*→*Kot*; Consejo: *Rizzo*→*Colegio*). El resto del copete (competencia federal, competencia de la Corte, recurso extraordinario) no tiene lectura obligatoria y queda remitido a la bibliografía optativa; lo dije en «El problema».
2. **Puente con Ferreyra (optativa).** La sección breve «Después de *Kot*» describe la ley 16.986, la ley 17.454 y la flexibilización posterior a 1983 citando `[@ferreyra2016]` por apartado. Es la única optativa usada en prosa; si se prefiere, puede reducirse a la mención del art. 43 y de *Rizzo* cons. 3 y 11.
3. **Selección de considerandos.** *Siri* y *Kot*: casi completos (voto que encabeza entero en *Kot*). *Rizzo*: voto que encabeza cons. 10–13 y 16–35 (se omiten 1–9, admisibilidad y lista de precedentes; 14–15, transcripción del art. 114 y de la ley, resumidos en prosa; 36–43, restricciones a las candidaturas y efectos); Petracchi y Argibay cons. 11–14; Zaffaroni cons. 4–6 y 11–16 (se omiten 7–10, la enmienda Bandrés). *Colegio*: cons. 6–7, 9–15 y 17 (se omite el cons. 8, que repite los debates citados en *Rizzo*, y la parte dispositiva, resumida en la ficha); Lorenzetti cons. 13–15 (se omiten 1–12 y 16–19).
4. **Cita de considerandos sin número.** *Siri* y el voto que encabeza *Kot* no numeran los considerandos: la línea de atribución agrega la página de Fallos.
5. **Versalitas y puntos suspensivos** en las transcripciones OCR: ver `U13_fuentes.md`.
6. **Notas y preguntas 11 y 12** vinculan el remedio de *Colegio de Abogados* con la pregunta de *Siri* y con *Fayt*/*Schiffrin* (U03). Son conexiones propias; no toman partido.
