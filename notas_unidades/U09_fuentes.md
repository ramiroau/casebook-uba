# Fuentes — Unidad 9 (para integrar en `FUENTES.md`)

## Tabla de fuentes

| Citekey | Unidad | Carácter | PDF (en `Materiales_UBA/`) | Extracto | Modo | Paginación |
|---|---|---|---|---|---|---|
| `rau2019` | 9 | obligatoria | `Unidad9/1_Álvarez Ugarte et al_2019_La actividad del Congreso.pdf` (23 pp) | `rau2019.txt` (copia de `corpus/texto/rau2019.txt`) | texto | versión de autor numerada 1-23 (= PDF), **sin la paginación de la obra** (pp. 528-562 según `programauba.json`). Citar por **apartado** (I a X) |
| `guidi2019` | 9 | obligatoria | `Unidad9/2_Guidi_2019_Elección y conformación de Cámaras.pdf` (15 pp) | `guidi2019.txt` (copia de `corpus/texto/guidi2019.txt`) | texto | versión de autor sin paginación impresa (la obra: pp. 503-527). Citar por **apartado** (1 a 4) |
| `csjn_famyl2000` | 9 | obligatoria | `Unidad9/3_CSJN - 2000 - Famyl S.A. c. Estado Nacional s. acción de amparo.pdf` (19 pp) | `csjn_famyl2000.txt` (copia de `corpus/texto/csjn_famyl2000.txt`) | texto | citar por **voto + considerando**. Fallos 323:2256 (confirmado en `csjn.db`, sumarios 38877-38880, 38936-38939, 39098-39105, 39139-39140) |
| `csjn_bussi2007` | 9 | optativa | `Unidad9/2007_Bussi, Antonio c.pdf` | — | no extraído | sólo «Para seguir leyendo»; descrito en prosa a través de Guidi, ap. 4 |
| `tula2004` | 9 | optativa | `Unidad9/María Inés Tula (2004)…pdf` | — | no extraído | sólo «Para seguir leyendo» |
| `pearce2019`, `ley27412`, `funcionamiento_parlamentario` | 9 | optativas | sin PDF | — | — | «(sin PDF en la carpeta)» |

## Calidad del texto y limpieza

Las tres obligatorias son nivel A (capa de texto nativa). No hizo falta `limpios/`.

- `rau2019`: las notas al pie llevan el número **en el mismo renglón** que su
  texto (`1         Los capítulos…`), así que el corte de notas
  (`NOTA_AL_PIE`, renglón con sólo un número) toma el número de página y deja
  las notas en el cuerpo. Se agregó en `extractos/limpieza/rau2019.txt` un
  patrón por página (PDF 1-12, 14-19, 21-23) que quita el bloque de notas,
  anclado en su primer y último renglón, y 40 patrones para llamadas de nota
  pegadas a punto, comillas tipográficas o precedidas de espacio, que
  `MARCA_DE_NOTA` no toma. Ningún patrón coincide con otra fuente de
  `extractos/` (verificado).
- `guidi2019`: notas con renglón numérico propio (el corte funciona), salvo
  la nota 42 (PDF p. 9, número en el mismo renglón) y la continuación de la
  nota 60 en PDF p. 13. Patrones en `extractos/limpieza/guidi2019.txt`, más
  18 llamadas de nota tras comillas tipográficas, mayúscula («CN36») o cifra
  («200930», «185331», «art. 4539»).
- Párrafos: los dos comentarios están justificados y sin sangría; los puntos y
  aparte se fijaron con `parrafo:` a partir de `pdftotext -bbox-layout`
  (renglón que no llega al margen derecho o salto vertical), y se cotejó la
  imagen de Guidi PDF p. 2. Una `unir:` en rau2019 (cita de Nino partida entre
  PDF pp. 10-11).
- `csjn_famyl2000`: texto de la publicación en La Ley (no el tomo de Fallos);
  párrafos separados por renglones en blanco, sin problemas. Considerandos
  numerados «1)», «2)»… sin «°». Se cotejó contra el texto de la base
  (`fallo_db.py 323 2256`): mismo contenido.
- Erratas del original reproducidas tal cual: rau2019 «capituo», «reglmaentos»,
  «la presencial del Presidente», «e quórum», «durante le curso», «en el este
  procedimiento», «Ambos casos» (tras enumerar tres fallos, ap. IX.1);
  guidi2019 «Liphart», «una curiosa la radicalización», «deliberacion» sin
  tilde; famyl voto de Vázquez «señor Procuradora», «briden».

## Estructura de *Famyl* (Fallos 323:2256), 29 de agosto de 2000

- Voto que encabeza el pronunciamiento (Moliné O'Connor, Fayt, Belluscio,
  Boggiano, Bossert): cons. 1-19 y parte dispositiva, PDF pp. 1-6.
- Nazareno, según su voto: PDF pp. 7-10. Adhiere a cons. 1-9; omite el cons.
  10 de la mayoría (regla de no revisión del procedimiento legislativo y su
  excepción); sus cons. 10-18 = cons. 11-19 de la mayoría.
- Petracchi, según su voto: PDF pp. 10-13 (cons. 1-6).
- Vázquez, en disidencia: PDF pp. 13-19 (cons. 1-19). Revoca: rige la alícuota
  reducida del 10,5%.
- La línea de firmas del compendio no incluye a López.

## Discrepancias con `programauba.json`

- `rau2019` aparece **dos veces**: una entrada con título «Comentario al
  artículo 32», autor sólo Álvarez Ugarte, pp. 1004-1016 (que no corresponde
  a este PDF), y otra correcta («La actividad del Congreso», Álvarez Ugarte,
  Dvoskin y Guidi, pp. 528-562). Conviene eliminar o renombrar la primera.
- `guidi2019` aparece dos veces con datos iguales (guion distinto en `page`).
- `csjn_famyl2000`: el campo `note` dice `csjn_cippec2014` (resto de una fusión).
- `rau2019`: la nota 1 del PDF atribuye los caps. I, IV, V, VI a Álvarez
  Ugarte, II y III a Guidi, VII a Dvoskin y Guidi; VIII a X no tienen
  atribución en la nota.
- `pearce2019`: `page: "---"`.

## Discrepancias entre notas de clase y fuentes (Unidad 9)

- Notas: en *Famyl* la promulgación parcial «viola el art. 76». El fallo
  aplica el **art. 80** (cons. 11-15). U09 sigue al fallo.
- Notas: la base constitucional de Diputados es «uno cada treinta mil». El
  art. 45 vigente dice uno cada **treinta y tres mil** (Guidi, ap. 3.1).
- Notas: «caso Collella». El comentario escribe «Colella» (Fallos 268:352).
- Notas: «CNE, caso Borocotó». Guidi lo cita como causa «Pagani»
  (CNE, sentencia 3738/2006).
- Notas atribuyen a la mayoría de *Famyl* los dos requisitos del art. 80
  «(cdo. 13)»: el test se enuncia en el cons. 12 y se aplica en el 13.
