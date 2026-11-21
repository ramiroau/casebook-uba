# U04 — notas de fuentes (para integrar en FUENTES.md)

## Tabla de fuentes

| Citekey | Unidad | Carácter | PDF (en `Materiales_UBA/`) | Extracto | Modo | Paginación |
|---|---|---|---|---|---|---|
| `gargarella2009c` | 4 | obligatoria | `Unidad4/1_Gargarella_2009_Un papel renovado para la Corte Suprema.pdf` (14 pp) | `gargarella2009c.txt` (copia de `corpus/texto/`) | texto | **sin paginación impresa**. Citar por sección (introducción, secc. 1 a 6). El capítulo publicado ocupa pp. 149-172 según `programauba.json` |
| `elfman2019` | 4 | obligatoria | `Unidad4/2_Elfman - 2019 - Comentario al artículo 31.pdf` (25 pp) | `elfman2019.txt` (copia de `corpus/texto/`) | texto | versión de autor con paginación propia (1-25 = PDF) que no es la de la edición publicada. Citar por apartado (introducción, I, II.a, II.b, II.c, II.c.1-3, III.a, III.b) y, para notas, «n. N» |
| `marbury` | 4 | obligatoria | `Unidad4/3_U.S._1803_Marbury v Madison.pdf` (18 pp) | `marbury.txt` | texto | traducción castellana sin paginación. Citar como opinión de la Corte (Marshall) y por cuestión; la cita oficial es 5 U.S. 137 |
| `csjn_elortondo1888` | 4 | obligatoria | `Unidad4/4_FALLO XXXIII. .pdf` (29 pp, compendio) | `csjn_elortondo1888.txt` (OCR del tomo impreso de Fallos, `scripts/fallo_db.py 33 162`, recortado a Fallos 162 y 184-211) | OCR (copia corregida en `limpios/`) | `[[PDF p. N]]` = **página de Fallos**. Compendio PDF p. 1 = Fallos 162; PDF p. N = Fallos N+182 (N ≥ 2). Mayoría: por considerando (1° a 27°). Disidencia de Zavalía: sin considerandos, citar por página de Fallos (33:197-211) |
| `gargarella1996` | 4 | optativa | `Unidad4/Gargarella_1996_La justicia frente al gobierno.pdf` | — | no extraído | sólo «Para seguir leyendo» |
| `csjn_sojo1887` | 4 | optativa | `Unidad4/CSJN - 1887 - Sojo, Eduardo c Cámara de Diputados de la Nación.pdf` | — (se usó `corpus/texto/csjn_sojo1887.txt` para una cita breve en prosa) | — | descripto en prosa en la sección de jurisprudencia; sin extracto |
| `csjn_thomas2010` | 4 | optativa | `Unidad4/CSJN_2010_Thomas, Enrique c.pdf` | — | no extraído | sólo «Para seguir leyendo» |
| `highton2014` | 4 | optativa | `Unidad4/Highton de Nolasco_2014_Sistemas concentrado y difuso...pdf` | — | no extraído | sólo «Para seguir leyendo» |

## Copias corregidas (`extractos/limpios/`)

| Citekey | Copia | Estado | Notas |
|---|---|---|---|
| `csjn_elortondo1888` | OCR del tomo impreso de Fallos (csjn.db, `vol_page`), corregido contra la imagen del compendio | `revisado: si` | **Revisadas: Fallos 184-189, 193-203 y 211** (compendio PDF 2-7, 11-21 y 29), que son todas las páginas extractadas. Corrección renglón por renglón con la imagen a 130 dpi y contraste palabra por palabra con el OCR del compendio (`corpus/texto/`), encabezados de página y pie («T. III 13») quitados. Ortografía de la época conservada («espropiacion», «sinó», «ú», «esplicitas»). Erratas del impreso conservadas: «puuto» (p. 185), «una nuevo requisito» (p. 201), «lo posibilidad» (p. 198), «exhorbitante» (p. 187), «ejercicicio» (p. 194). Lecturas a decidir: «su eta á» (p. 184, tipo dañado) se leyó «sujeta á»; donde el tipo es ambiguo entre «u» y «n» y los dos OCR discrepan se tomó la palabra correcta («Constitucion» p. 186, «indisputable» p. 196, «tomarse» p. 196). **Sin revisar** (no se usan): Fallos 162, 190-192, 204-210. El OCR del tomo es muy superior al del compendio, que es una fotocopia con texto forzado por ocrmypdf |

## Transformaciones de extractos con capa de texto

- `marbury.txt`: el PDF está a doble interlineado y `pdftotext` pone un renglón en blanco entre cada par de renglones, lo que haría de cada renglón un párrafo. Al crear el extracto se quitó el renglón en blanco simple y se dejó uno solo donde había dos o más. Además, en PDF p. 15 se subió «sería» al renglón anterior («una constitución escrita- sería») para que el guion de inciso no se reúna como corte de palabra. Sólo cambia el espacio en blanco; la verificación (que ignora espacios) no se ve afectada.

## Limpieza (`extractos/limpieza/elfman2019.txt`)

- Continuaciones de notas al pie que quedan sobre el primer renglón numerado de la página y el corte de notas no alcanza: PDF pp. 4 (n. 12), 5 (n. 16), 6 (n. 22), 12 (n. 50), 14 (n. 63), 16 (n. 76), 19 (n. 92). Patrones anclados al texto de cada nota.
- Llamadas de nota que `MARCA_DE_NOTA` no reconoce: tras comilla tipográfica de cierre (”36, ”64, ”65, ”67, ”68, ”70, ”79, ”86, ”87, ”95, ”96, ”98, ”99, ”101, ”103, ”105, ”106), tras dígito («1853-607», n. 7), de tres cifras (100, 102, 104) y antes de paréntesis de cierre («Judicial61)»). Cada patrón lleva su contexto en el lookbehind.

## Discrepancias con `programauba.json`

- `marbury`: el campo `abstract` describe *Luther v. Borden* (48 U.S. 1, 1849), y `note` termina en `ussc_luther`. Es un resto de otra entrada. `volume` 5 y `page` 137 son correctos para *Marbury*. No afecta el renderizado de la cita, pero conviene limpiar los dos campos.
- `elfman2019`: `page` es «---». El título de la entrada es «Comentario al artículo 31»; el PDF se titula «Supremacía constitucional. Control de constitucionalidad y control de convencionalidad (Arts. 27, 31, 43, 75 inc. 22 y 24, 116 CN)».
- `csjn_elortondo1888`: `volume` 33, `page` 162 confirmados en csjn.db (sumarios de Fallos 33:162). La entrada no tiene fecha completa: 14 de abril de 1888.
- `gargarella2009c`: el campo `note` dice `gargarella2009a` (mismo resto de fusión que en `gargarella2009d`).
- Elfman (n. 74) cita *Fayt* como «Fallos: 326:1616»; la cita correcta es 322:1616 (ver U03). Errata del texto, no de la bibliografía.

## Discrepancias entre notas de clase y fuentes (Unidad 4)

- Las notas presentan *Sojo* como «el Marbury argentino». Elfman (ap. II.a, n. 18) señala que en *Sojo* la Corte desarrolló el razonamiento del control sin impugnar la validez de una norma, y que *Elortondo* fue el primer caso en que invalidó una ley. U04 sigue a Elfman y deja la comparación como pregunta (nota 10).
- El copete de las notas de clase (versión anterior del programa) incluye «El caso Sojo» y la «jurisprudencia constitucional y cómo leerla»; el copete v25 menciona *Marbury* y los modelos concentrado y difuso, y *Elortondo* es obligatorio. U04 sigue al programa v25.
- Las notas remiten a Nino (pp. 659-688) como lectura central de la unidad; Nino no figura en la bibliografía de la Unidad 4 del programa v25. No se usó.
