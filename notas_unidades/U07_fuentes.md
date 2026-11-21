# U07 — notas de fuentes (para integrar en FUENTES.md)

## Filas de la tabla de fuentes

| Citekey | Unidad | Carácter | PDF (en `Materiales_UBA/`) | Extracto | Modo | Paginación |
|---|---|---|---|---|---|---|
| `jgb2008` | 7 | obligatoria | `Unidad7/1_González Bertomeu_2008_Notas sobre federalismo2.pdf` (46 pp) | `jgb2008.txt` | texto (re-extraído con PyMuPDF, ver abajo) | versión de autor con paginación propia 1-46 = PDF. Se cita por esa página. No es la paginación del libro de Gargarella (2008) |
| `mendez2021` | 7 | obligatoria | `Unidad7/2_Méndez Montenegro_Vitaliani_2021_Haz lo que yo digo, pero no lo que yo hago.pdf` (14 pp) | `mendez2021.txt` | texto (re-extraído con PyMuPDF, por columnas) | impresa = PDF **+52** (JA 2021-III, pp. 53-66) |
| `csjn_evolucion2023` | 7 | obligatoria | `Unidad7/4_CSJN_2023_Evolución Libral y otro c. Provincia de San Juan s- amparo.pdf` (51 pp) | `csjn_evolucion2023.txt` | texto (copia de `corpus/texto/`) | citar por **voto + considerando** |
| `csjn_confederacion2024` | 7 | obligatoria | `Unidad7/5_CSJN_2024_Confederación Frente Amplio de Formosa c. Provincia de Formosa.pdf` (57 pp) | `csjn_confederacion2024.txt` | texto (copia de `corpus/texto/`) | citar por **voto + considerando** |
| optativas de U07 | 7 | optativas | ver `corpus/manifiesto.csv` | — | no extraídas | sólo en «Para seguir leyendo» |

## Re-extracción de `jgb2008` y `mendez2021`

El texto de `corpus/texto/` no servía para insertar extractos:

- `jgb2008`: `pdftotext -layout` deja las notas al pie (muy extensas) dentro del
  cuerpo, sin un renglón con sólo el número que dispare el corte de notas, y
  las llamadas de nota pegadas a puntos y comas («estado.3 Así»), que
  `MARCA_DE_NOTA` no quita.
- `mendez2021`: el artículo está a dos columnas y `-layout` intercala las dos
  columnas renglón por renglón.

Ambos se regeneraron desde el PDF digital con PyMuPDF
(`notas_unidades/U07_gen_extractos.py`, copia del script usado):

- `jgb2008`: sólo renglones del cuerpo (11,3 pt); se descartan notas (9,4 pt),
  superíndices de llamada, número de página, el cuadro de PDF p. 35 y su
  leyenda; punto y aparte por el espacio vertical entre renglones (> 24 pt).
  Los renglones cortados con guion U+2010 («sub‐») se reúnen sin espacio.
- `mendez2021`: columna izquierda y luego derecha, sólo 9,5 pt; se descartan
  notas (8 pt), cabezales y pies (8 y 10 pt) y el título de p. 1; se quitan
  las llamadas «(N)»; punto y aparte por sangría de primera línea y por
  títulos de sección.

No se cambió ninguna palabra. Las cabeceras de los dos archivos documentan el
criterio. Al regenerar `corpus/`, estos dos extractos no deben pisarse con la
versión `-layout`.

## Limpieza (`extractos/limpieza/`)

- `csjn_evolucion2023.txt`: carátula de páginas impares (`ORIGINARIO`,
  «Evolución Liberal y otro c/ San Juan,», «Provincia de s/ amparo.»),
  anclada a renglones con sangría de 20 o más espacios.
- `csjn_confederacion2024.txt`: carátula («Confederación Frente Amplio»,
  «Formoseño c/ Formosa, Provincia de s/», «amparo.»), anclada igual. El
  patrón de `ORIGINARIO` está en el archivo de *Evolución* y sirve a los dos.
- `CSJ …`, «Corte Suprema de Justicia de la Nación» y «- N -» ya los cubre
  `LIMPIEZA` global. En *Confederación* el número de página es un renglón con
  sólo la cifra: lo toma el corte de notas, al final de la página, sin efecto
  sobre el cuerpo.

## Estructura de los fallos

### *Evolución Liberal* (Fallos 346:543), 1 de junio de 2023

- Voto de Rosatti y Maqueda (encabeza): PDF pp. 1-17, cons. 1 a 12 y parte dispositiva.
- Rosenkrantz, por su voto: PDF pp. 18-50, cons. 1 a 20 y parte dispositiva.
- Firmas (PDF p. 50): Rosatti, Rosenkrantz, Maqueda. Lorenzetti no suscribió.
- Antes: cautelar del 9 de mayo de 2023 (Fallos 346:461) y rechazo de recusaciones (Fallos 346:486), según la base de la CSJN.

### *Confederación Frente Amplio Formoseño* (Fallos 347:2044), 19 de diciembre de 2024

- Voto de Rosatti y Maqueda (encabeza): PDF pp. 1-20, «Resulta» I a V, cons. 1 a 15 (**no hay cons. 12**: el texto pasa del 11 al 13) y parte dispositiva.
- Rosenkrantz, por su voto: PDF pp. 21-41, cons. 1 a 13; declara la inconstitucionalidad «en su aplicación al caso concreto» y permite al gobernador terminar el mandato 2023-2027 (cons. 11 y 13).
- Lorenzetti, por su voto: PDF pp. 42-56, cons. 1 a 16.
- Firmas (PDF p. 56): Rosatti, Rosenkrantz, Maqueda, Lorenzetti.

## Discrepancias con `programauba.json`

- `csjn_confederacion2024`: `number` dice `999/2023`; el expediente es **CSJ 922/2023**. El título dice «Confederación Frente Amplio de Formosa»; la carátula es «Confederación Frente Amplio **Formoseño** c/ Formosa, Provincia de s/ amparo». La cita de Fallos (347:2044) la confirma la base de la CSJN.
- `csjn_evolucion2023`: la entrada aparece duplicada en el JSON (dos registros con el mismo `id`).
- `csjn_ucr2013` (optativa): la entrada apunta a Fallos 336:1756, que es la **medida cautelar** del 22 de octubre de 2013. La sentencia de fondo, que los dos fallos obligatorios citan como «Santiago del Estero», es Fallos **336:2148** (5 de noviembre de 2013). Decidir cuál se quiere citar.
- `csjn_ucr2018`, `csjn_ucr2019`: sin Fallos (`---`). Según los fallos obligatorios: Santa Cruz = Fallos 341:1869; La Rioja = Fallos 342:343. *Río Negro* (Fallos 342:287), central en la línea, no tiene citekey.
- `csjn_ucr2018`, `csjn_ucr2019`, `csjn_ucr2019b`: sin PDF en la carpeta.
- `jgb2008`: `page: ---`; el PDF es una versión de autor de 46 pp. sin la paginación del libro.
- `gervasoni2011`: `note` arrastra `gervasoni2011a`.

## Discrepancias internas de las fuentes

- `mendez2021`, nota 2: «Fallos 336:2248» para Santiago del Estero (fondo); los fallos de la Corte citan 336:2148. Notas 3 y 4: La Rioja y Río Negro figuran ambos como «Fallos 342:235»; los fallos de la Corte citan La Rioja = 342:343 y Río Negro = 342:287. Las notas no se reproducen en el casebook.
- `mendez2021`, p. 57: «vulnera el art. 5º de la Constitución provincial» (por el contexto, el art. 5 de la Constitución Nacional). Se reproduce tal cual.
- `csjn_confederacion2024`, voto de Rosenkrantz, cons. 10: la lista de mandatos de Insfrán omite los períodos 1995-1999 y 1999-2003 como gobernador, aunque el mismo considerando le computa 37 años en los cargos.

## Discrepancias entre notas de clase y fuentes

- Las notas resumen a Méndez Montenegro y Vitaliani diciendo que en *Santiago* «la autonomía provincial no es "plena"» y listan «Máxima prudencia» como rasgo de *Santiago*. En el artículo, «máxima prudencia» aparece en la reseña de *Santa Cruz* (p. 57). Sin consecuencias: el casebook sigue al texto.
- Las notas mencionan para JGB que «las provincias "de bajo costo"» es tesis de Gervasoni; en JGB la expresión «bolsones potenciales de electores de bajo costo» se atribuye a Gibson y Calvo (p. 28), y Gervasoni aparece en nota (p. 35, n. 131).
- Las notas atribuyen a JGB «Desigualdad en el derecho / Experimentación jurídica / Aplicación de tratados» como «tres temas adicionales»: coincide con el texto (pp. 36-41).
