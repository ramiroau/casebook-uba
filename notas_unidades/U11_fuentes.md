# U11 — notas de fuentes (para integrar en FUENTES.md)

## Tabla de fuentes

| Citekey | Unidad | Carácter | PDF (en `Materiales_UBA/`) | Extracto | Modo | Paginación |
|---|---|---|---|---|---|---|
| `god1991` | 11 | obligatoria | `Unidad11/1_O'Donnell_1991_Democracia Delegativa.pdf` (17 pp) | `god1991.txt` (copia de `corpus/texto/god1991.txt`) | texto | impresa = PDF **+6** (traducción en *Journal of Democracy en Español*, pp. 7-23). Notas al final, PDF pp. 16-17 (pp. 22-23) |
| `saenz2016b` | 11 (dueña) | obligatoria | `Unidad11/2_Sáenz - 2016 - Facultades normativas del poder ejecutivo.pdf` (21 pp) | `saenz2016b.txt` (copia de `corpus/texto/saenz2016b.txt`) | texto | **sin paginación impresa** (versión de imprenta). Citar por apartado (1 a 5, con 4.1 y 4.2) |
| `alegre2010` | 11 | optativa | `Unidad11/Alegre-Democracia sin presidentes.pdf` | — | no extraído | sólo «Para seguir leyendo» |
| `nino1988` | 11 | optativa | `Unidad11/Nino - 1988 - Presidencialismo v. Parlamentarismo.pdf` | — | no extraído (corpus nivel B) | sólo «Para seguir leyendo» |
| `ollier2012` | 11 | optativa | `Unidad11/Ollier_2012_Más allá del presidencialismo….pdf` | — | no extraído | sólo «Para seguir leyendo» |
| `sagues2001` | 11 | optativa | sin PDF en la carpeta | — | — | sólo «Para seguir leyendo» |

## Limpieza agregada

- `extractos/limpieza/god1991.txt`: encabezados de página («N Journal of Democracy en Español», «Guillermo O’Donnell N»), nota con asterisco de PDF p. 1 (sin número propio) y llamadas de nota 1-12 pegadas a la puntuación, que `MARCA_DE_NOTA` no toma. Todas ancladas en el texto vecino.
- `extractos/limpieza/saenz2016b.txt`: continuaciones de notas al pie que quedan antes del renglón con el número de la nota siguiente (fin de la nota 2 en PDF p. 2, de la nota 36 en p. 11, de la nota 55 en p. 18) y llamadas de nota que `MARCA_DE_NOTA` no toma (tras comillas tipográficas, mayúscula, cifra o espacio: 11, 16, 17, 21, 22, 24, 25, 28, 29, 33, 34, 37, 39, 40, 47, 48, 53, 57, 58, 59, 62, 66, 67).

## Párrafos

- `god1991`: los títulos de sección centrados («Acerca de las Instituciones», etc.) hacen que la heurística parta el primer párrafo de cada sección después del primer renglón; corregido con `unir:` en los cinco marcadores afectados. Los títulos no se extractan (los tramos empiezan después).
- `saenz2016b`: PDF p. 8 termina en «…arrastra aquel fallo.» a margen completo; no se puede saber si «Ello llevó a que…» (p. 9) abre párrafo. Se dejó unido (mismo criterio que Holmes p. 17).

## Discrepancias con `programauba.json`

- `god1991`. La entrada remite a *Novos Estudos* (CEBRAP) 31 (1991), pp. 25-40, en portugués. El PDF de la carpeta es la traducción castellana de la versión inglesa («Delegative Democracy», *Journal of Democracy* 5:1, 1994, pp. 55-69), publicada en *Journal of Democracy en Español* (pp. 7-23). La nota del autor la llama «versión corregida y abreviada» del texto de 1991. El casebook cita por la paginación de la traducción. Convendría ajustar la entrada (o agregar una nueva) para la edición que efectivamente se lee.
- `saenz2016b`. **El id está duplicado en `programauba.json`**: hay dos entradas con `id: saenz2016b`, una «Facultades normativas del poder ejecutivo» (correcta para U11) y otra «Artículo 30. Reforma de la Constitución», pp. 78-90 (que es la obra de `saenz2016a`). Con ids duplicados, el resultado de citeproc es impredecible: hay que eliminar o renombrar la segunda. Ver también la discrepancia de U06 (`saenz2016_art14y28`).
- `saenz2016b`. La entrada lleva `page: "---"`.

## Erratas del original conservadas (`saenz2016b`)

«leye 26.364» (ap. 3), «Aceval Pollachi» en el cuerpo y «Pollacchi» en la nota (ap. 4.2), «revindicación» (ap. 4.1), «este Tribunales» (cita de *Verrocchi*, ap. 4.1), «Decreto Nº 1.204/200151» (ap. 5; el «51» tiene el cuerpo del texto en la capa del PDF y no corresponde a ninguna llamada de nota de esa página), «Mas reciente», «claúsula», «universos», «poder de reglamentar las (“Cocchia”…)» y la frase trunca «siempre que para que el contenidos de una ley» (ap. 5).

## Discrepancias entre notas de clase y fuentes (Unidad 11)

- Las notas citan a O'Donnell: «Riña general por un beneficio restringido y a corto plazo» (p. 18). El texto dice «riña general por **el** beneficio restringido y a corto plazo» (p. 18).
- Bajo el excursus sobre O'Donnell, las notas explican por qué la dinámica delegativa no se da en EE.UU. («Congreso más fuerte por las circunscripciones uninominales»). O'Donnell no trata a EE.UU.; su contraste es Uruguay y Chile (pp. 16-17). El argumento parece venir de Nino (optativa).
- Las notas (resumen de Sáenz) ponen al Jefe de Gabinete como «Titular de la Administración Pública Nacional». Sáenz dice que el titular jerárquico es el Presidente; la reforma procuró transferir al Jefe de Gabinete el ejercicio directo de la administración y eso «no se ha trasladado a la práctica» (ap. 2).
- Las notas incluyen la reglamentación (99.2) y los DNU (99.3) dentro de la «potestad co-legislativa». Sáenz llama co-legislativas a la iniciativa (art. 77) y al veto (arts. 80 y 83), y enumera aparte la reglamentación y la legislación por delegación o urgencia (ap. 2); en el ap. 3 sí califica de «co-legislativa» la facultad reglamentaria en la tradición de Cádiz.
- (Para U12) Las notas fechan *Peralta* en 1992; Sáenz dice 1990 (ap. 4.1).
