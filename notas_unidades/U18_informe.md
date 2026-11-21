# U18 — informe final

## Archivos

- Escritos: `unidades/U18.md` (nueva), `respaldos/U18_agente.md` (copia idéntica), `extractos/courtis2001.txt` (copia del corpus, `# modo: ocr`), `extractos/limpios/courtis2001.txt` (`# revisado: si`), `extractos/csjn_quisbeth2012.txt` (`# modo: texto`), `extractos/limpieza/csjn_quisbeth2012.txt`, `notas_unidades/U18_fuentes.md`, este informe.
- No se tocaron archivos compartidos ni se corrió `build_casebook.sh`. Prueba: `insertar_extractos.py --unidades U18 --salida <scratchpad>/U18` (OK) y `verificar.py --unidades U18`.

## Palabras

Prosa propia (sin extractos, con títulos y ficha): unas 2.900 palabras, frente al objetivo de 3.000-4.500. No se rellenó: la unidad se apoya en los extractos (unas 14.000 palabras de las fuentes).

## Verificación

`verificar.py --unidades U18`: **OK**. 8 citekeys, 0 sin entrada; 0 citas en bloque escritas a mano; cobertura 2/2 obligatorias; 11 marcadores resueltos. Citas con `[verif. visual]`: ninguna en bloque. Hay citas breves en línea de Abramovich y Courtis («notoriamente endeble», «caso límite», «individualizada y concreta», «reflejan algunas particularidades de los derechos sociales», «una parte gana y la otra pierde», «en el plano de una teoría constitucional o política»), cotejadas contra la imagen de las pp. 974, 978, 983, 984 y 992 y presentes en la copia revisada.

## Extractos

| Fuente | Tramo | PDF pp. | Impresas | Palabras | Origen |
|---|---|---|---|---|---|
| `courtis2001` | sección I | 2-7 | 973-978 | 1.411 | limpio |
| `courtis2001` | sección II | 7-15 | 978-986 | 2.761 | limpio |
| `courtis2001` | sección III, ap. 1 | 16-20 | 987-991 | 1.400 | limpio |
| `courtis2001` | sección III, aps. 2-4 | 20-27 | 991-998 | 1.870 | limpio |
| `csjn_quisbeth2012` | voto que encabeza, cons. 3 | 3-5 | — | 627 | extracto |
| `csjn_quisbeth2012` | voto que encabeza, cons. 9-12 | 15-19 | — | 788 | extracto |
| `csjn_quisbeth2012` | voto que encabeza, cons. 13-15 | 19-27 | — | 2.316 | extracto |
| `csjn_quisbeth2012` | voto que encabeza, cons. 16-17 y dispositiva | 28-31 | — | 559 | extracto |
| `csjn_quisbeth2012` | Petracchi, cons. 8-11 | 32-35 | — | 843 | extracto |
| `csjn_quisbeth2012` | Petracchi, cons. 15-18 y dispositiva | 38-42 | — | 973 | extracto |
| `csjn_quisbeth2012` | Argibay, cons. 9, 11-12 y dispositiva | 53-57 | — | 462 | extracto |

El capítulo de Abramovich y Courtis se reproduce completo (sin notas). Puntos y aparte corregidos con `parrafo:`/`unir:` y revisados en la salida.

## Discrepancias y pendientes

- Ver `U18_fuentes.md`: edición del PDF de Abramovich y Courtis distinta de la entrada `courtis2001` (y orden de autores); *Quisbeth* en Fallos 335:452 y 24/4/2012 (la entrada dice 335:454 y 24/6/2012); notas de clase: numeración de la unidad, ubicación de la «indeterminación fáctica», «mínimo razonable».
- Sin `[PENDIENTE]` abiertos en el texto.
- Riesgo a revisar: en las pp. 975 y 995 del escaneo el margen derecho está cortado; las letras perdidas se completaron por el contexto. La reconstrucción menos segura es «derecho de propiedad: a ello se destina» (p. 975). La «Ubicación» de la lectura lo advierte. Convendría cotejar con otra copia del texto.

## Ediciones del autor

Unidad nueva: no había ediciones del autor que conservar.

## Decisiones de criterio a revisar

- Selección de *Quisbeth*: se omiten los cons. 1-2 y 4-8 del voto que encabeza (hechos, trámite, sistema de fuentes), resumidos en la ficha; se incluye el cons. 3 completo porque expone la posición del Tribunal Superior local (*Alba Quintana*) que la Corte revoca. De Petracchi se omiten los cons. 12-14 (examen del subsidio y de los paradores); de Argibay, los cons. 1-8 y 10 (hechos y reseña normativa sobre discapacidad).
- El *holding* se tomó del cons. 17 (y 12), en línea con el sumario 622 de la base de la CSJN.
- Los fallos optativos (*Benghalensis*, *Defensor del Pueblo*, *Mendoza*, *Salas*) se mencionan en una línea cada uno en «El problema» y en la nota 8, sin extractos y sin reconstruir sus holdings.
- Donde se tomó posición: la nota 9 y la síntesis formulan la objeción democrática (desacuerdo razonable sobre los medios) como pregunta abierta, siguiendo el énfasis de las notas de clase; el texto de Abramovich y Courtis declara que deja esa discusión a un lado (p. 992), y así se lo presenta.
- El título de la sección de jurisprudencia es «el derecho a la vivienda ante la Corte Suprema», porque el único fallo obligatorio es de vivienda.
