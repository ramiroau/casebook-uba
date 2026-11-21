# Fuentes — Unidad 14 (para integrar a FUENTES.md)

## Tabla de fuentes

| Citekey | Unidad | Carácter | PDF (en `Materiales_UBA/`) | Extracto | Modo | Paginación |
|---|---|---|---|---|---|---|
| `alegre2020` | 14 | obligatoria | `Unidad14/1_Alegre et al. - 2020 - Cuidar la vida y la Constitución La limitación de.pdf` (10 pp) | `alegre2020.txt` (copia de `corpus/texto/alegre2020.txt`) | texto | impresa = PDF (pie «-N-»). Informe de 10 pp |
| `csjn_lee2020` | 14 | obligatoria | `Unidad14/2_CSJN - 2020 - Lee, Carlos Roberto y otro c Consejo de Atención .pdf` (17 pp) | `csjn_lee2020.txt` (copia de `corpus/texto/csjn_lee2020.txt`) | texto | citar por **considerando**. Fallo unánime, un solo voto: PDF pp. 1–16; p. 17, partes |
| `csjn_petcoff2020` | 14 | optativa | `Unidad14/CSJN - 2020 - Petcoff Naidenoff, Luis c. Provincia de Formosa s.pdf` (6 pp) | — | no extraído (OCR previo, nivel B) | sólo en «Para seguir leyendo» y en prosa |
| `csjn_ibarrola2021` | 14 | optativa | `Unidad14/CSJN - 2021 - Ibarrola, Natalia Romina c. Provincia de Formosa s.pdf` (12 pp) | — | no extraído (texto nativo en `corpus/texto/`) | citado en prosa por considerando, sin extracto |

## Limpieza agregada (`extractos/limpieza/`)

- `csjn_lee2020.txt`: carátula repetida en las páginas impares (seis renglones, uno por patrón; el bloque no funcionaba porque otro archivo de limpieza ya quita «ORIGINARIO»), y unión del renglón partido en «Covid-|19─» (cons. 1, PDF p. 1).
- `alegre2020.txt`: llamadas de nota 2–22 pegadas a un punto o a comillas tipográficas (MARCA_DE_NOTA no las toma), incluida «art. 23¹³»; continuación de la nota 15 en el pie de PDF p. 7, sin número propio; unión del renglón partido en «demostrarlo-|son» (PDF p. 9). **Defecto residual**: el impreso dice «demostrarlo- son» (raya de cierre de inciso y espacio); el extracto insertado dice «demostrarlo-son». Sin el patrón quedaba «demostrarloson».
- Ninguna de las dos fuentes tiene renglones de margen con sólo un número al comienzo de página; no hizo falta tocar las copias en `extractos/`.

## Párrafos

`alegre2020`: puntos y aparte fijados con `parrafo:` contra la imagen del PDF (pp. 2–10, revisadas visualmente). `csjn_lee2020`: dos `unir:` en el cons. 2 (renglones que terminan en «a)» y «g)»).

## Discrepancias con `programauba.json`

- `csjn_lee2020`: la entrada tiene `volume`/`page` «---». La base de la CSJN confirma **Fallos 343:1704** (sumarios 153103-153116), y así lo cita *Ibarrola* (cons. 9 y 11).
- `csjn_ibarrola2021`: la entrada tiene `page` «---». Base CSJN: **Fallos 344:316**. Además el título dice «Ibarrola, Natalia Romina»; el fallo y la base dicen «Ibarrola, **Romina Natalia**».
- `csjn_petcoff2020`: Fallos 343:944 confirmado (sumario 152087, 10 de septiembre de 2020), con carátula «Petcoff Naidenoff, Luis **Carlos** c/ Formosa, Provincia de s/ amparo - habeas corpus». Es un requerimiento de informes. *Ibarrola* (cons. 10 y 11) cita otra decisión de la misma causa, «Petcoff Naidenoff, Luis», **Fallos 344:126** (25 de febrero de 2021, incidente de inhibitoria según la base), que no está en el programa.

## Discrepancias entre notas de clase y fuentes (Unidad 14)

- Las notas dicen que *Petcoff* «resuelve sobre» el cierre de las fronteras internas. La decisión del compendio (Fallos 343:944) sólo requiere informes a la provincia en tres días. U14 sigue al texto.
- Las notas dicen que *Lee* «es la continuidad, mismos hechos» de *Petcoff*. Son causas distintas (actores, expediente y vía procesal distintos) sobre el mismo programa provincial de ingreso; *Lee* no cita *Petcoff*. U14 presenta los casos como una línea sobre el mismo problema.
- Las notas ubican la «escala movediza» en el cons. 10 de *Lee*. El estándar del escrutinio creciente está en el cons. 7; el cons. 10 desarrolla el argumento temporal.
