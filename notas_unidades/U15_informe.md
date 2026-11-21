# Informe — Unidad 15. Principio de autonomía personal

## Archivos

- Escritos: `unidades/U15.md` (nueva), `respaldos/U15_agente.md` (copia idéntica), `notas_unidades/U15_fuentes.md`, este informe.
- Extractos nuevos: `extractos/gargarella2009e.txt`, `extractos/csjn_cha1991.txt`, `extractos/csjn_alitt2006.txt`.
- Copias corregidas nuevas: `extractos/limpios/gargarella2009e.txt`, `extractos/limpios/csjn_cha1991.txt`, `extractos/limpios/csjn_alitt2006.txt` (las tres `# revisado: si`).
- No se tocaron archivos compartidos ni `extractos/limpieza/` (no hizo falta ningún patrón: el mobiliario de página se quitó en las copias de `limpios/`). No se corrió `build_casebook.sh`.

## Palabras

- Prosa propia (sin marcadores de extracto, con encabezados y fichas): **3.788**, dentro del objetivo de 3.000-4.500.
- Texto de las fuentes insertado: 19.017 palabras en 16 marcadores.

## Verificación

`python3 scripts/insertar_extractos.py --unidades U15 --salida <scratchpad>` → OK. `python3 scripts/verificar.py --unidades U15` → **OK**: 10 citekeys, 0 sin entrada; 0 citas en bloque escritas a mano; cobertura: 3 obligatorias, todas citadas; 16 marcadores resueltos. **6** líneas de atribución con `[verif. visual]` (los seis tramos de Gargarella, fuente OCR revisada página por página). Pandoc procesa la salida sin errores.

## Extractos

| Fuente | Páginas | Palabras | Origen |
|---|---|---|---|
| `gargarella2009e`, introducción (Mill, perfeccionismo) | PDF 1-3 (pp. 779-781) | 869 | limpio |
| `gargarella2009e`, Stephen, Devlin, Hart | PDF 3-6 (pp. 781-784) | 1.208 | limpio |
| `gargarella2009e`, constituciones, fallos, privacidad espacial | PDF 6-11 (pp. 784-789) | 1.156 | limpio |
| `gargarella2009e`, II. Neutralidad | PDF 11-13 (pp. 789-791) | 701 | limpio |
| `gargarella2009e`, III. Paternalismo | PDF 13-15 (pp. 791-793) | 964 | limpio |
| `gargarella2009e`, IV. Privacidad y autogobierno | PDF 15-18 (pp. 793-796) | 1.166 | limpio |
| `csjn_cha1991`, voto que encabeza, cons. 6-13 y dispositiva | Fallos 1546-1549 | 1.145 | limpio |
| `csjn_cha1991`, Boggiano, cons. 9-13 (1.er párr.) y 14-18 | Fallos 1589-1595 | 1.653 | limpio |
| `csjn_cha1991`, disidencia de Fayt, cons. 8-14, 18 y dispositiva | Fallos 1599-1604 | 1.572 | limpio |
| `csjn_cha1991`, disidencia de Petracchi, cons. 15 | Fallos 1611 | 109 | limpio |
| `csjn_cha1991`, disidencia de Petracchi, cons. 17-19 | Fallos 1612-1618 | 2.518 | limpio |
| `csjn_cha1991`, disidencia de Petracchi, cons. 20 | Fallos 1618-1620 | 978 | limpio |
| `csjn_cha1991`, disidencia de Petracchi, cons. 22-23 y dispositiva | Fallos 1623-1625 | 931 | limpio |
| `csjn_alitt2006`, cons. 5-12 | PDF 6-12 | 1.735 | limpio |
| `csjn_alitt2006`, cons. 13-19 | PDF 12-16 | 1.310 | limpio |
| `csjn_alitt2006`, cons. 21-24 y dispositiva | PDF 17-20 | 1.002 | limpio |

Párrafos revisados en la salida: se fijaron con `parrafo:` los que empiezan en página nueva (Gargarella pp. 780, 784, 788; *CHA* 1548, 1590, 1624) y con `unir:` un corte espurio de *ALITT* (cons. 12). En *ALITT* se quitaron además cinco renglones en blanco espurios de la copia corregida.

## Fuentes y textos elegidos

- *CHA*: se usó el OCR del **tomo impreso de Fallos** (`fallo_db.py 314 1531`), muy superior al OCR del compendio, que es el mismo tomo escaneado (PDF p. *n* = Fallos 1530 + *n*). Las páginas usadas se corrigieron contra la imagen; para detectar errores se cruzaron los dos OCR y se buscaron palabras ausentes del corpus.
- *ALITT*: capa de texto nativa, con una codificación defectuosa (raya → «C», «¿» → «)»). Para no perder las rayas, el extracto base se marcó `# modo: ocr` y la corrección mecánica se hizo en `limpios/`. **Decisión a revisar**: alternativa sería mantener `modo: texto` y quitar las «C» con patrones de limpieza, perdiendo las rayas.
- Gargarella: el OCR de `corpus/` tenía notas al pie entrelazadas y palabras rotas; se transcribió una copia limpia renglón por renglón contra la imagen de las 18 páginas.

## Discrepancias y pendientes

- No hay `[PENDIENTE]` abiertos.
- `gargarella2009e` en `programauba.json`: páginas 173–231 (erróneas; el capítulo es pp. 779-796) y tomo no verificado. Ver `U15_fuentes.md`.
- Gargarella, nota 9: cita *Montalvo* como Fallos 308:1392, que es la cita de *Bazterrica*; y dice que *Montalvo* fue «unos meses» posterior a *Bazterrica* (1986). La unidad no reproduce esos datos.
- Notas de clase: numeran la unidad como 16; atribuyen a Gargarella un ejemplo de aborto («cinco días») que en el texto es de divorcio (tres meses); agrupan *Griswold*/*Roe* con *CHA*/*Montalvo* como blancos de la crítica perfeccionista, cuando el texto los critica por su concepción espacial de la privacidad. Detalle en `U15_fuentes.md`.

## Ediciones del autor

Ninguna: la unidad es nueva.

## Decisiones de criterio para revisar

1. **Selección de votos en *CHA***. Del lado de la mayoría se reproduce el voto que encabeza (Levene) y el de **Boggiano**, elegido porque hace explícito el fundamento perfeccionista (cita a Devlin y a *Bowers*) y dialoga directamente con Gargarella. Quedan fuera los votos de Cavagna Martínez, Barra, Belluscio, Nazareno y Moliné O'Connor. De Fayt se omiten los cons. 1-7 (incluidos los 6-7 sobre la «etiología» de la homosexualidad, que la nota 5 menciona) y 15-17. De Petracchi se omiten los cons. 1-14 (arbitrariedad y estándar de escrutinio, resumidos en la línea de encuadre), 16 (jurisprudencia universitaria estadounidense) y 21 (familia). En Boggiano se omite el resto del cons. 13 (transcripción de *Bowers*).
2. ***ALITT***: sólo el voto que encabeza; el voto de Fayt se describe en una línea. Se omiten cons. 1-4 (antecedentes, resumidos en la ficha) y 20.
3. **Privacidad e intimidad (art. 18)**: las lecturas obligatorias no hacen la distinción del copete. La unidad lo dice y remite a Nino (optativa) sin describir su contenido, que no se leyó.
4. **Aborto**: las obligatorias lo tratan sólo vía *Roe*. Se mencionó *F., A. L.* (optativa) en prosa, sin extracto, verificado contra el texto del fallo (cons. 8 y 20), señalando que invoca el art. 19 *in fine* (principio de reserva) y no la cláusula de acciones privadas. La nota 10 formula esa diferencia como pregunta.
5. **Lugares donde se tomó una posición leve**: la síntesis dice que «puede pensarse» que *ALITT* resolvió un caso en que la abstención estatal bastaba; la nota 5 pregunta si la disidencia de Fayt reproduce el prejuicio que combate. *Arriola* (que las notas de clase mencionan) no está en el programa y no se incluyó.
6. *Bazterrica* (optativa) se menciona en la introducción con lo que de él dicen Gargarella y Petracchi; no se leyó el fallo.
