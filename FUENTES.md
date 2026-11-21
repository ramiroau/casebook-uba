# Fuentes — Unidades 1 a 18

Mapa entre los PDFs de `../Materiales_UBA/`, las claves de `programauba.json` y
los extractos de texto de `extractos/`. Toda cita del casebook debe poder
rastrearse hasta una línea de esta tabla.

## Regla de citación por fuente

Los extractos llevan marcadores `[[PDF p. N]]`. La columna **paginación** dice
cómo convertir esa página del PDF en la referencia que va en el casebook.

| Citekey | Unidad | Carácter | PDF (en `Materiales_UBA/`) | Extracto | Modo | Paginación |
|---|---|---|---|---|---|---|
| `gargarella2009d` | 1 | obligatoria | `Unidad1/1_Gargarella_2009_Constitucionalismo versus Democracia.pdf` (10 pp) | `gargarella2009d.txt` | OCR `spa` | escaneo a doble página: PDF p. *n* = impresas **2n+20 / 2n+21**. Capítulo: pp. 23–40 |
| `holmes1993` | 1 | obligatoria | `Unidad1/2_Holmes_1993_El precompromiso y la paradoja de la democracia.pdf` (26 pp) | `holmes1993.txt` | texto | **sin paginación impresa** (traducción re-tipeada). Citar por título de sección |
| `nino1996a` | 1 | optativa | `Unidad1/Nino_1996_El carácter complejo de la democracia constitucional.pdf` (17 pp) | `nino1996a.txt` | OCR `spa` | impresa = PDF **+12**. Capítulo: pp. 13–28 |
| `gargarella2015b` | 2 | obligatoria | `Unidad2/1_Gargarella_2015_La sala de máquinas de la Constitución.pdf` (29 pp) | `gargarella2015b.txt` | OCR `spa` | impresa = PDF **+11**. Capítulo: pp. 13–39 |
| `pisarello2013` | 2 | optativa | `Unidad2/Pisarello_2013_Un Largo Termidor.pdf` (219 pp) | `pisarello2013.txt` | texto | verificar antes de citar; solo se usa en «Para seguir leyendo» |
| `saenz2016a` | 3 | obligatoria | `Unidad3/1_Sáenz - Artículo 30. Reforma de la Constitución.pdf` (9 pp) | `saenz2016a.txt` | texto | **sin paginación impresa** (versión de imprenta). Citar por apartado; el capítulo publicado ocupa pp. 78–90 |
| `csjn_fayt1999` | 3 | obligatoria | `Unidad3/2_CSJN - 1999 - Fayt, Carlos S..pdf` (27 pp) | `csjn_fayt1999.txt` | texto | citar por **considerando**, no por página |
| `csjn_schiffrin2017` | 3 | obligatoria | `Unidad3/3_CSJN - 2017 - Schifrin...pdf` (118 pp) | `csjn_schiffrin2017.txt` | OCR previo del escaneo (copia corregida en `limpios/`) | citar por **voto + considerando**. Paginación impresa = PDF |
| `quintana1988` | 3 | optativa | `Unidad3/Quintana_1988_Tratado...PDF` | — | no extraído | solo en «Para seguir leyendo» |

## Calidad del texto y consecuencias

`holmes1993`, `saenz2016a`, `csjn_fayt1999` y `pisarello2013` tienen capa de
texto nativa (`csjn_schiffrin2017` tiene una capa OCR previa, ver abajo): las citas textuales se verifican
por `grep` contra el extracto.

`gargarella2009d`, `gargarella2015b` y `nino1996a` provienen de OCR. El OCR es
legible pero comete errores de palabra (p. ej. «igualitarism» por
«igualitarismo», «muestras» por «nuestras», «12» por «la»). En el caso de
`gargarella2009d` hay una dificultad adicional: es un escaneo a doble página y el
reconocimiento entrelaza las dos columnas, de modo que el orden del texto en el
extracto no siempre es el del original. **Ninguna cita en bloque tomada de estos
tres extractos se fija sin cotejarla visualmente contra la página del PDF.** El
extracto sirve para localizar el pasaje, no para transcribirlo.

Esas citas llevan la marca `[verif. visual]` al final de su línea de atribución.
`scripts/verificar.py` las reconoce y las cuenta aparte, en lugar de reportarlas
como no verificadas: son las únicas que no se comparan contra `extractos/`.

## Copias corregidas de los extractos OCR (`extractos/limpios/`)

Los extractos largos se insertan al compilar desde el texto de la fuente (ver
`README.md`). Para las fuentes OCR eso exige una copia corregida contra la
imagen del PDF, marcada `# revisado: si`. Estado:

| Citekey | Copia | Estado | Notas |
|---|---|---|---|
| `gargarella2009d` | re-OCR con `extraer.py --doble` (cada mitad de la hoja por separado, cortada en el borde de la sombra del lomo) | `revisado: si` | **Capítulo completo revisado (pp. 23-40).** Corregidas contra la imagen (200 dpi), renglón por renglón y sin notas al pie ni llamadas de nota: PDF 1 der. (p. 23) y PDF 2 a 6 y 8 completas en la pasada de U01 v0.2; PDF 7 (pp. 34-35), PDF 9 completa (pp. 38-39) y PDF 10 izq. (p. 40) en la de U01 v0.3. **Sin revisar**: PDF 1 izq. (p. 22, final del capítulo anterior) y PDF 10 der. (p. 41, portadilla de la parte siguiente); ninguna se usa. En pp. 34 y 40 el lomo corta las últimas letras de varios renglones: se completaron por el contexto (p. ej. «físicas;», «tenga», «conozcamos»), sin cambiar ninguna palabra legible. Se respetaron dos rarezas del impreso: «sostienen» sin punto final al cerrar el párrafo de p. 39 (no se ve punto bajo el subrayado) y «simplemente ,“defiendo» con el espacio antes de la coma (p. 40); también «una *sección tercera* o que uno siempre» (p. 38), que parece un resto de edición del original. Rayas de inciso transcriptas como `–`, igual que en el impreso; cursivas no conservadas. Cada mitad lleva su propio `[[PDF p. N]]`: la izquierda es la impresa 2n+20, la derecha 2n+21 |
| `nino1996a` | copia del extracto OCR original | `revisado: no` | Fotocopia de 1 bit, torcida y subrayada a mano. El OCR es malo con cualquier configuración probada (enderezado, `--psm` 1, 4 y 6). Corregirlo equivale a transcribirlo. Es optativa: conviene conseguir una versión con capa de texto antes de extractarla en extenso |
| `gargarella2015b` | re-OCR de la **otra copia** de la carpeta, `CAPITULO I- EL PRIMER DERECHO CONSTITUCIONAL LATINOAMERICANO (1810-1850).pdf` (sin resaltar, dos páginas por hoja), media hoja por vez | `revisado: si` | **Capítulo completo del compendio revisado (pp. 13-40, PDF 2-29).** El PDF del compendio está resaltado con marcador amarillo y el OCR pierde renglones enteros (puntaje heurístico alto, texto inservible). Cada página se corrigió renglón por renglón contra la imagen de la copia sin resaltar, sin notas al pie, llamadas de nota ni encabezados; las citas en bloque del original quedan como párrafos. Los marcadores `[[PDF p. N]]` siguen la numeración del PDF del compendio (impresa = PDF + 11). Erratas del impreso conservadas: «entoncès» (p. 18), «sacrifico» (p. 29), «Constituciones Consulares Napoleónicas de 1799 y 1892» (p. 34, verificado con ampliación), «concentrase» (p. 40). El compendio termina en p. 40, a mitad de la sección sobre el modelo liberal |
| `csjn_schiffrin2017` | capa OCR del escaneo, corregida en las páginas extractadas | `revisado: si` | El PDF es un escaneo con OCR previo (ver `AUDITORIA_CORPUS.md`); por eso el extracto pasó a `# modo: ocr`. Corregidas: PDF 4-10, 13-17, 22-25, 28-31 (voto que encabeza), 72-75 y 86 (Rosatti), 93-99, 103-108, 115-116 (Rosenkrantz). Errores típicos corregidos uno por uno: «u»/«U» por comillas de cierre, «3 o» por 3°, palabras partidas («baj o», «Ej ecuti vo»), «T. 111» por «T. III», sellos y restos de margen. Páginas con dudas cotejadas contra la imagen (PDF 16, 105-106). Se conservan sin acento «cabria» (p. 16) y otros casos ilegibles a la resolución disponible. El resto del archivo es la capa OCR sin corregir y no se usa |

## Discrepancias con `programauba.json` detectadas al redactar

Se anotan acá y **no se corrigieron**: la bibliografía es la del programa y su
edición es una decisión aparte.

- `holmes1993`. La entrada no registra páginas ni el año de la edición usada. El
  PDF del compendio lleva al pie: «Tomado de Jon Elster y Rune Slagstad,
  *Constitucionalismo y democracia*, México, Fondo de Cultura Económica, **1999**,
  páginas **217 a 262**». La entrada dice 1993, que es el año de la edición
  original en inglés. Convendría agregar `page: 217-262` y decidir qué edición se
  cita.
- `csjn_fayt1999`. La entrada indica `Fallos 322:1609`. La base de la CSJN
  (`observatorio-csjn/data/csjn.db`) confirma que la sentencia está en
  **Fallos 322:1616**; en 322:1609 está la resolución sobre la recusación
  planteada en la misma causa (sumarios 137958-137959). *Schiffrin* cita
  `Fallos: 322:1616`. U03 v0.2 usa 322:1616 en la ficha; la entrada de la
  bibliografía sigue sin corregir.
- `csjn_schiffrin2017`. El campo `note` arrastra basura de sincronización
  (`mlzsync1:...csjn_bonevo`). No afecta el renderizado, pero conviene limpiarlo.
- `gargarella2009d`. El campo `note` dice `gargarella2009a`, que es otra clave del
  mismo archivo. Probablemente un resto de una fusión de entradas.

## Observaciones sobre los textos con capa de texto

- `holmes1993`. La transcripción del compendio trae errores de tipeo que los
  extractos reproducen tal cual (p. ej. «Tribal pregunta» por «Tribe pregunta»,
  «la sabrían» por «lo sabrían», «iNo» por «¡No», «estará representados»). La
  capa de texto no conserva los puntos y aparte: se reconstruyen con `parrafo:`
  en los marcadores de U01, contrastados contra los saltos verticales del PDF
  (`pdftotext -bbox-layout`). Restos de margen y una llamada de nota de PDF
  pp. 25-26 se filtran con patrones de `LIMPIEZA` en `scripts/verificar.py`.
  Desde U01 v0.3 el capítulo se extracta completo: los puntos y aparte de todas
  las páginas (1-26) se fijaron con `parrafo:`/`unir:` contra los saltos
  verticales de `pdftotext -bbox-layout`, y se agregaron a `LIMPIEZA` las
  llamadas de nota 41 y 43 de PDF p. 7, pegadas al punto. Las letras sueltas en
  medio de frase («toda e teoría», «la s distinción», «una le asamblea») están
  en el impreso del compendio, no en la capa de texto: se reproducen tal cual.
  El cierre de PDF p. 17 («…esa misma complacencia.») llega al margen derecho,
  así que no se puede saber si «La dificultad de atar al futuro» (p. 18) abre
  párrafo; se dejó unido.

## Discrepancias entre notas de clase y fuentes (Unidad 1)

- Las notas atribuyen a Hume la regla de que los padres no pueden obligar a sus
  hijos. En Holmes la regla es de Locke; Hume señala la contradicción entre esa
  regla y la ficción del contrato originario (sección «La prohibición de
  obstruir el futuro»).
- Las notas cuentan la disputa Madison-Jefferson como quinto argumento de
  Gargarella y Ulises como sexto. En el texto, Madison aparece como un caso en
  que se plantea «un dilema semejante» y Ulises como «un último y prometedor
  argumento»; los argumentos examinados y descartados en serie son cuatro
  (pp. 25-27). U01 sigue al texto.
- Las notas dicen que para Nino la constitución histórica es un buen *proxy* de
  la ideal. El capítulo (p. 25) dice que su preservación se supone instrumental
  para la protección de los derechos y que su observancia suele coincidir con
  ese respeto, pero que la coincidencia es imperfecta. U01 sigue al texto.
- U01 v0.1 decía que para Gargarella el argumento de las tradiciones es «el más
  débil». El texto dice «más vulnerable que el recién examinado» (p. 27).
  Corregido.

## Estructura interna de los fallos

### *Fayt* (Fallos 322:1609), 19 de agosto de 1999

- Considerandos numerados 1° a 21° en el voto que encabeza.
- Mayoría: Nazareno, Moliné O'Connor, Belluscio, Boggiano, López (PDF pp. 1–13).
- Vázquez, según su voto (PDF pp. 14–22).
- Bossert, en disidencia parcial (PDF pp. 23–27).

### *Schiffrin* (Fallos 340:257), 28 de marzo de 2017

- Voto que encabeza el pronunciamiento, suscripto por Lorenzetti: PDF pp. 1–32.
- Maqueda, por su voto: PDF pp. 33–70.
- Rosatti, por su voto: PDF pp. 71–90.
- Rosenkrantz, en disidencia: PDF pp. 91–118.
- La página de firmas (PDF p. 32, verificada visualmente) lleva cuatro firmas:
  Lorenzetti, Maqueda, Rosatti y Rosenkrantz. Highton de Nolasco no suscribió.

## Material presente en las carpetas pero fuera del programa

No entra al casebook. Se registra para que la omisión sea deliberada y no un
descuido.

- `Unidad1/constitucionalismo-y-democracia-0.pdf` — Alfonso Ruiz Miguel,
  «Constitucionalismo y democracia», *Isonomía* 21 (2004). Sin citekey en
  `programauba.json`. Candidato natural a bibliografía optativa de la Unidad 1.
- `Unidad2/CAPITULO I- ... (1810-1850) (editado).pdf` y su versión sin editar
  (16 pp cada uno) — mismo capítulo que `gargarella2015b`, en un recorte más
  breve. Imagen pura, sin capa de texto. Se toma como canónico el archivo
  numerado de 29 pp, que es el que `build_compendio.py` incorpora al compendio.
- `Unidad2/Convención Constituyente 1853_1853_Congreso General Constituyente.pdf`
  — fuente primaria, sin citekey.
- `Unidad3/Rosanvallon_2006_La Democracia Inconclusa.pdf` — sin citekey. Las
  notas de clase lo mencionan como recomendación oral («Recomendar
  Rosanvallon»).

## Limpieza de extractos agregada en U01-U03 v0.2 (`LIMPIEZA` en `scripts/verificar.py`)

- `saenz2016a`, PDF p. 3: la nota 6 continúa en el pie de p. 3 sin número propio;
  sin un patrón específico quedaba dentro del cuerpo. También la llamada de nota
  14 pegada a «13.233» (PDF p. 6).
- `csjn_fayt1999`, cons. 15: la capa de texto codifica las comillas de
  «Núcleo de Coincidencias Básicas» como «A…@»; se quitan los dos caracteres.
- `csjn_schiffrin2017`: variante OCR de la carátula («8chiffrin»).


# Unidades 4 a 18

Integrado de `notas_unidades/U0N_fuentes.md` (redacción en paralelo, noviembre de 2026). Los informes completos de cada unidad están en `notas_unidades/U0N_informe.md`. Patrones de limpieza por fuente: `extractos/limpieza/<clave>.txt`. Fallos tomados del tomo impreso de Fallos: `scripts/fallo_db.py`.

## U04 — notas de fuentes (para integrar en FUENTES.md)

### Tabla de fuentes

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

### Copias corregidas (`extractos/limpios/`)

| Citekey | Copia | Estado | Notas |
|---|---|---|---|
| `csjn_elortondo1888` | OCR del tomo impreso de Fallos (csjn.db, `vol_page`), corregido contra la imagen del compendio | `revisado: si` | **Revisadas: Fallos 184-189, 193-203 y 211** (compendio PDF 2-7, 11-21 y 29), que son todas las páginas extractadas. Corrección renglón por renglón con la imagen a 130 dpi y contraste palabra por palabra con el OCR del compendio (`corpus/texto/`), encabezados de página y pie («T. III 13») quitados. Ortografía de la época conservada («espropiacion», «sinó», «ú», «esplicitas»). Erratas del impreso conservadas: «puuto» (p. 185), «una nuevo requisito» (p. 201), «lo posibilidad» (p. 198), «exhorbitante» (p. 187), «ejercicicio» (p. 194). Lecturas a decidir: «su eta á» (p. 184, tipo dañado) se leyó «sujeta á»; donde el tipo es ambiguo entre «u» y «n» y los dos OCR discrepan se tomó la palabra correcta («Constitucion» p. 186, «indisputable» p. 196, «tomarse» p. 196). **Sin revisar** (no se usan): Fallos 162, 190-192, 204-210. El OCR del tomo es muy superior al del compendio, que es una fotocopia con texto forzado por ocrmypdf |

### Transformaciones de extractos con capa de texto

- `marbury.txt`: el PDF está a doble interlineado y `pdftotext` pone un renglón en blanco entre cada par de renglones, lo que haría de cada renglón un párrafo. Al crear el extracto se quitó el renglón en blanco simple y se dejó uno solo donde había dos o más. Además, en PDF p. 15 se subió «sería» al renglón anterior («una constitución escrita- sería») para que el guion de inciso no se reúna como corte de palabra. Sólo cambia el espacio en blanco; la verificación (que ignora espacios) no se ve afectada.

### Limpieza (`extractos/limpieza/elfman2019.txt`)

- Continuaciones de notas al pie que quedan sobre el primer renglón numerado de la página y el corte de notas no alcanza: PDF pp. 4 (n. 12), 5 (n. 16), 6 (n. 22), 12 (n. 50), 14 (n. 63), 16 (n. 76), 19 (n. 92). Patrones anclados al texto de cada nota.
- Llamadas de nota que `MARCA_DE_NOTA` no reconoce: tras comilla tipográfica de cierre (”36, ”64, ”65, ”67, ”68, ”70, ”79, ”86, ”87, ”95, ”96, ”98, ”99, ”101, ”103, ”105, ”106), tras dígito («1853-607», n. 7), de tres cifras (100, 102, 104) y antes de paréntesis de cierre («Judicial61)»). Cada patrón lleva su contexto en el lookbehind.

### Discrepancias con `programauba.json`

- `marbury`: el campo `abstract` describe *Luther v. Borden* (48 U.S. 1, 1849), y `note` termina en `ussc_luther`. Es un resto de otra entrada. `volume` 5 y `page` 137 son correctos para *Marbury*. No afecta el renderizado de la cita, pero conviene limpiar los dos campos.
- `elfman2019`: `page` es «---». El título de la entrada es «Comentario al artículo 31»; el PDF se titula «Supremacía constitucional. Control de constitucionalidad y control de convencionalidad (Arts. 27, 31, 43, 75 inc. 22 y 24, 116 CN)».
- `csjn_elortondo1888`: `volume` 33, `page` 162 confirmados en csjn.db (sumarios de Fallos 33:162). La entrada no tiene fecha completa: 14 de abril de 1888.
- `gargarella2009c`: el campo `note` dice `gargarella2009a` (mismo resto de fusión que en `gargarella2009d`).
- Elfman (n. 74) cita *Fayt* como «Fallos: 326:1616»; la cita correcta es 322:1616 (ver U03). Errata del texto, no de la bibliografía.

### Discrepancias entre notas de clase y fuentes (Unidad 4)

- Las notas presentan *Sojo* como «el Marbury argentino». Elfman (ap. II.a, n. 18) señala que en *Sojo* la Corte desarrolló el razonamiento del control sin impugnar la validez de una norma, y que *Elortondo* fue el primer caso en que invalidó una ley. U04 sigue a Elfman y deja la comparación como pregunta (nota 10).
- El copete de las notas de clase (versión anterior del programa) incluye «El caso Sojo» y la «jurisprudencia constitucional y cómo leerla»; el copete v25 menciona *Marbury* y los modelos concentrado y difuso, y *Elortondo* es obligatorio. U04 sigue al programa v25.
- Las notas remiten a Nino (pp. 659-688) como lectura central de la unidad; Nino no figura en la bibliografía de la Unidad 4 del programa v25. No se usó.

## Fuentes — Unidad 5 (para integrar en FUENTES.md)

### Tabla de fuentes

| Citekey | Unidad | Carácter | PDF (en `Materiales_UBA/`) | Extracto | Modo | Paginación |
|---|---|---|---|---|---|---|
| `sagues2004` | 5 | obligatoria | `Unidad5/1_Sagüés - 2004 - Interpretación constitucional y alquimia constituc.pdf` (20 pp) | `sagues2004.txt` | texto | impresa = PDF **+150**. Artículo: pp. 151-170 |
| `gargarella2007` | 5 | obligatoria | `Unidad5/2_Gargarella_2007_De la alquimia interpretativa al maltrato constitucional.pdf` (11 pp) | `gargarella2007.txt` | texto | **sin paginación de la revista** (original de autor). Citar por sección |
| `gargarella2009a` | 5 | obligatoria | `Unidad5/3_Gargarella-La dificultosa tarea...(versión más clara).pdf` (14 hojas, doble página) | `gargarella2009a.txt` (copia del corpus) | OCR (copia corregida en `limpios/`) | en `limpios/` los marcadores `[[PDF p. N]]` llevan **la página impresa** (123-148). En el corpus: PDF *n* izq = 2n+120, der = 2n+121 |
| `gargarella2021` | 5 | obligatoria | `Unidad5/4_Gargarella_El derecho como una conversación (cap. interpretacion, extracto).pdf` (26 pp) | `gargarella2021.txt` | OCR (copia corregida en `limpios/`) | impresa = PDF **+210**. Capítulo 14: pp. 211-236 |
| `scalia1988` | 5 | obligatoria | `Unidad5/5_Scalia_1988_Originalism The lesser evil.pdf` (6 pp) | `scalia1988.txt` | texto | **sin paginación** (traducción castellana re-tipeada). Citar sin página |
| `nino1992b` | 5 | optativa | `Unidad5/Nino_1992_Interpretación de la Constitución.PDF` | — | no extraído | sólo «Para seguir leyendo» |
| `csjn_sejean1986` | 5 | optativa | `Unidad5/CSJN - 1986 - Sejean...pdf` | — | no extraído | sólo «Para seguir leyendo» |
| `csjn_rizzo2013` | 5 (dueña U13) | optativa | `Unidad5/CSJN_2013_Rizzo...pdf` | — | no extraído aquí | sólo «Para seguir leyendo» |
| `ely1997` | 5 | optativa | sin PDF | — | — | — |

### Copias corregidas (`extractos/limpios/`)

| Citekey | Copia | Estado | Notas |
|---|---|---|---|
| `gargarella2009a` | combinación de tres OCR corregida contra la imagen | `revisado: si` | **Capítulo completo revisado (pp. 123-148).** El escaneo del compendio está torcido y el OCR del corpus entrelaza columnas en pp. 126, 128-129, 133, 135, 137-138, 141, 146, 148. Se re-OCR-izó (tesseract spa, 300 dpi, `--psm 3` y `--psm 6`) la **otra copia** de la carpeta, `Gargarella_2009_La dificultosa tarea de la interpretación constitucional2.pdf` (una página por hoja, 28 pp; su capa de texto es letra espaciada inservible), y para cada página se eligió la mejor de las tres fuentes (corpus o re-OCR) y se corrigió contra la imagen de esa copia. En esa copia pp. 132 y 138 están cortadas a la derecha: se tomaron del compendio; la mitad inferior de p. 138 se transcribió de la imagen (los finales de renglón se leen en el margen de p. 139). Sin notas al pie ni llamadas; rayas de inciso como `–`. Erratas del impreso conservadas: «Frankfruter», «qué es lo el derecho da» (p. 126), «especiamente» (p. 148), «alegar?.» (p. 131). **Atención: aquí `[[PDF p. N]]` = página impresa**, distinto de `corpus/texto/gargarella2009a.txt` |
| `gargarella2021` | OCR del corpus corregido | `revisado: si` | **PDF 1-26 revisadas (pp. 211-236, todo el capítulo).** OCR bueno; correcciones puntuales (p. ej. «oniginalistas», «eran fragilidad», «sistemajudicial», rayas como guiones, renglones en blanco espurios, «* * *» de p. 217). PDF 24 (p. 234) re-transcripta: el OCR partía renglones. Sin notas al pie ni llamadas; encabezados en mayúsculas como párrafo propio. Se conservan «intepretativa» (título) y «preminencia» (p. 223) |

### Limpieza agregada (`extractos/limpieza/`)

- `sagues2004.txt`: folios y encabezados («151», «152 • Néstor Pedro Sagüés», «Interpretación constitucional y alquimia constitucional • 153»); notas 1, 2-3, 4, 5, 6-8 y 9 (empiezan con el número sangrado, sin renglón propio); llamadas 1-9 pegadas a puntuación.
- `gargarella2007.txt`: llamadas 1, 2, 5 y 6 pegadas a punto o paréntesis; continuación de la nota 3 al pie de PDF p. 2.

### Discrepancias con `programauba.json`

- `scalia1988`: la entrada cita el original inglés (57 U. Cin. L. Rev. 849). El compendio trae una traducción castellana sin datos de traductor ni paginación, que parece **abreviada** (remite a una cita de Tribe que no figura). Convendría registrar la traducción o anotar la entrada.
- `gargarella2009a`: la entrada da pp. 173-231 y `note: saldivia09`; el capítulo del compendio ocupa **pp. 123-148** del t. I. La paginación de la entrada no corresponde (el manifiesto del corpus ya señala que esas páginas se copiaron también a `gargarella2009e`).
- `gargarella2007`: la entrada da *Jurisprudencia Argentina* 2007-II, pp. 3-10; el PDF es un original de autor sin esa paginación, y su nota 1 cita a Sagüés como «Interpretación constitucional y alquimia **interpretativa**», Lexis Nexis (2004).
- `gargarella2021`: la entrada (libro) no registra capítulo ni páginas; el compendio trae el cap. 14, pp. 211-236.
- `fiss2008`: figura en el programa como optativa pero **no existe en `programauba.json`** y no hay PDF.
- `ely1997`: publisher «Silgo del Hombre» (errata por «Siglo del Hombre»).

### Material de la carpeta fuera del programa

- `Unidad5/Gargarella_2019_El preámbulo.pdf` — sin citekey; listado en «Para seguir leyendo» como ajeno al programa.
- `Unidad5/Gargarella_2009_La dificultosa tarea de la interpretación constitucional2.pdf` — segunda copia de `gargarella2009a`, usada para la corrección.

### Discrepancias entre notas de clase y fuentes (Unidad 5)

- Las notas presentan un «texto dos» de Gargarella que «valora el esfuerzo de Sagüés pero lo cuestiona» y luego analiza originalismo, Dworkin, Ely y Waldron. El texto que discute a Sagüés es `gargarella2007`; el que recorre esas teorías (`gargarella2009a`) no menciona a Sagüés.
- Las notas dicen que Dworkin fracasa por no poder abordar «el hecho del desacuerdo». En `gargarella2009a` (pp. 136-137) la crítica a Dworkin es el carácter monológico de Hércules (Michelman, Nino); el «hecho del desacuerdo» aparece en la sección sobre Waldron y en `gargarella2021`, p. 229.
- Las notas remiten a Waldron con «el ejemplo de la isla». En `gargarella2021` el ejemplo es la comunidad de inmigrantes que llega a su «tierra prometida» (cap. 2 del libro, retomado en pp. 230-231).
- Error de hecho en la fuente (no en las notas): `gargarella2009a`, p. 138, atribuye la nota 4 de *Carolene Products* (1938) a Earl Warren como presidente de la Corte. La unidad lo señala como agregado del editor (nota 11).

## Fuentes — Unidad 6 (para integrar en `FUENTES.md`)

### Tabla de fuentes

| Citekey | Unidad | Carácter | PDF (en `Materiales_UBA/`) | Extracto | Modo | Paginación |
|---|---|---|---|---|---|---|
| `saenz2016b` (clave de extracto `saenz2016_art14y28`) | 6 | obligatoria | `Unidad6/1_Saenz 2016.pdf` (11 pp) | `saenz2016_art14y28.txt` | texto | **sin paginación impresa**. Citar por apartado (introducción, aps. 1, 2, 3.1, 3.2, 3.3; notas al pie como «n. N») |
| `bouzat2013` | 6 | obligatoria | `Unidad6/2_Bouzat_2013_El principio de razonabilidad como límite sustantivo a las atribuciones del.pdf` (13 pp) | `bouzat2013.txt` | texto | **sin paginación impresa** (manuscrito Word). Citar por sección romana (I-VII). El original numera dos secciones consecutivas como «III» |
| `csjn_clarin2013` | 6 | optativa | `Unidad6/CSJN_2013_Grupo Clarín S.pdf` (392 pp, escaneo) | — | no extraído | sólo ficha en prosa (vía Bouzat) y «Para seguir leyendo» |
| `maurino2011` | 6 | optativa | `Unidad6/Maurino_2011_El artículo 28 de la Constitución.pdf` | — | no extraído | sólo «Para seguir leyendo» |

### Extractos creados

- `extractos/saenz2016_art14y28.txt`: copia de `corpus/texto/saenz2016_art14y28.txt` con `# modo: texto`. **Única edición**: en PDF p. 1 la llamada de nota 1 (tras «poder de policía del Estado”») ocupaba un renglón propio; `NOTA_AL_PIE` la tomaba como comienzo de las notas y cortaba la página. Se quitó el renglón y se unió «”: la potestad». Documentado en la cabecera.
- `extractos/bouzat2013.txt`: copia sin cambios de `corpus/texto/bouzat2013.txt` con `# modo: texto`.

### Limpieza agregada

- `extractos/limpieza/saenz2016_art14y28.txt`: llamadas de nota pegadas a comillas de cierre («”») o a un punto, que `MARCA_DE_NOTA` no reconoce (notas 2, 15, 24, 25, 27, 28, 32, 36, 38, 39, 40, 43, 44, 46). Cada patrón anclado con el texto vecino.
- `extractos/limpieza/bouzat2013.txt`: ídem, notas 8 a 18 de la sec. VI (tras «“Hileret”», «“Canale”», etc.).

### Rarezas del original conservadas

- Sáenz, PDF p. 11: «(t) cuando se impugna» por «(i)» y «“Hooft» sin comillas de cierre; verificado contra la imagen, están en el PDF.
- Sáenz, PDF p. 1: «los todos los habitantes». PDF p. 8: «parte de de una ley», «autorizada» por «autorizaba».
- Bouzat: «Higthon de Nolasco» (sec. VI), «aparto coactivo» (sec. V), «la ley que cuya constitucionalidad» (sec. III), dos secciones «III».

### Discrepancias con `programauba.json`

- `saenz2016b`: la entrada (y la de U11) es «Facultades normativas del poder ejecutivo». El PDF asignado en U06 es «Artículos 14 y 28: Poder de policía o poder de “reglamentar” los derechos. Sus límites». Se citó `[@saenz2016b]` para que cierre la cobertura, según el BRIEF. Hace falta una entrada propia (p. ej. `saenz2016c`) y cambiar la clave en el programa. Además, `programauba.json` tiene **dos entradas con id `saenz2016b`** (una con el título del art. 30, pp. 78-90, y otra con «Facultades normativas»): conviene depurarlo.
- `bouzat2013`: tipo `manuscript`, fecha `circa`. Los metadatos del PDF dan creación el 17/8/2016; el texto cita *Clarín* (2013) y *ADEBA*, posteriores a 2013. El año probablemente es aproximado.
- `csjn_avico1934` (U17, no es de esta unidad): la entrada dice Fallos 248:21; Bouzat cita Fallos 172:21 (n. 11). Verificar.

### Discrepancias entre las lecturas

- *Hileret*: Bouzat lo cita como Fallos 98:20 (n. 8) y Sáenz como Fallos 98:51 (n. 30). Las descripciones de la ley también difieren (indemnizar a cañeros que destruían plantíos, según Bouzat; deprimir la oferta para subir el precio en favor de productores locales, según Sáenz). La unidad expone las dos. La base de la CSJN no cubre ese tomo en `caso`.

### Verificación en la base de la CSJN

- *Grupo Clarín*, Fallos 336:1774, 29/10/2013 (24 sumarios). Composición según `voto`: voto conjunto Highton de Nolasco y Lorenzetti; votos propios Petracchi y Zaffaroni; disidencias parciales Maqueda y Argibay; disidencia Fayt. Usado en la ficha.
- *Iachemet*, Fallos 316:779, 29/4/1993: coincide con Sáenz (n. 40).

### Material en la carpeta fuera del programa de la unidad

- `Unidad6/CIDH_2010_Marco jurídico interamericano del Derecho a la Libertad de Expresión.pdf` (tiene entrada `cidh2010` en `programauba.json`, pero no figura en el programa v25; se menciona con `[Cf. @cidh2010]`).
- `Unidad6/Nino_1992_Garantías constitucionales.PDF` (sin citekey propia identificada).

## U07 — notas de fuentes (para integrar en FUENTES.md)

### Filas de la tabla de fuentes

| Citekey | Unidad | Carácter | PDF (en `Materiales_UBA/`) | Extracto | Modo | Paginación |
|---|---|---|---|---|---|---|
| `jgb2008` | 7 | obligatoria | `Unidad7/1_González Bertomeu_2008_Notas sobre federalismo2.pdf` (46 pp) | `jgb2008.txt` | texto (re-extraído con PyMuPDF, ver abajo) | versión de autor con paginación propia 1-46 = PDF. Se cita por esa página. No es la paginación del libro de Gargarella (2008) |
| `mendez2021` | 7 | obligatoria | `Unidad7/2_Méndez Montenegro_Vitaliani_2021_Haz lo que yo digo, pero no lo que yo hago.pdf` (14 pp) | `mendez2021.txt` | texto (re-extraído con PyMuPDF, por columnas) | impresa = PDF **+52** (JA 2021-III, pp. 53-66) |
| `csjn_evolucion2023` | 7 | obligatoria | `Unidad7/4_CSJN_2023_Evolución Libral y otro c. Provincia de San Juan s- amparo.pdf` (51 pp) | `csjn_evolucion2023.txt` | texto (copia de `corpus/texto/`) | citar por **voto + considerando** |
| `csjn_confederacion2024` | 7 | obligatoria | `Unidad7/5_CSJN_2024_Confederación Frente Amplio de Formosa c. Provincia de Formosa.pdf` (57 pp) | `csjn_confederacion2024.txt` | texto (copia de `corpus/texto/`) | citar por **voto + considerando** |
| optativas de U07 | 7 | optativas | ver `corpus/manifiesto.csv` | — | no extraídas | sólo en «Para seguir leyendo» |

### Re-extracción de `jgb2008` y `mendez2021`

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

### Limpieza (`extractos/limpieza/`)

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

### Estructura de los fallos

#### *Evolución Liberal* (Fallos 346:543), 1 de junio de 2023

- Voto de Rosatti y Maqueda (encabeza): PDF pp. 1-17, cons. 1 a 12 y parte dispositiva.
- Rosenkrantz, por su voto: PDF pp. 18-50, cons. 1 a 20 y parte dispositiva.
- Firmas (PDF p. 50): Rosatti, Rosenkrantz, Maqueda. Lorenzetti no suscribió.
- Antes: cautelar del 9 de mayo de 2023 (Fallos 346:461) y rechazo de recusaciones (Fallos 346:486), según la base de la CSJN.

#### *Confederación Frente Amplio Formoseño* (Fallos 347:2044), 19 de diciembre de 2024

- Voto de Rosatti y Maqueda (encabeza): PDF pp. 1-20, «Resulta» I a V, cons. 1 a 15 (**no hay cons. 12**: el texto pasa del 11 al 13) y parte dispositiva.
- Rosenkrantz, por su voto: PDF pp. 21-41, cons. 1 a 13; declara la inconstitucionalidad «en su aplicación al caso concreto» y permite al gobernador terminar el mandato 2023-2027 (cons. 11 y 13).
- Lorenzetti, por su voto: PDF pp. 42-56, cons. 1 a 16.
- Firmas (PDF p. 56): Rosatti, Rosenkrantz, Maqueda, Lorenzetti.

### Discrepancias con `programauba.json`

- `csjn_confederacion2024`: `number` dice `999/2023`; el expediente es **CSJ 922/2023**. El título dice «Confederación Frente Amplio de Formosa»; la carátula es «Confederación Frente Amplio **Formoseño** c/ Formosa, Provincia de s/ amparo». La cita de Fallos (347:2044) la confirma la base de la CSJN.
- `csjn_evolucion2023`: la entrada aparece duplicada en el JSON (dos registros con el mismo `id`).
- `csjn_ucr2013` (optativa): la entrada apunta a Fallos 336:1756, que es la **medida cautelar** del 22 de octubre de 2013. La sentencia de fondo, que los dos fallos obligatorios citan como «Santiago del Estero», es Fallos **336:2148** (5 de noviembre de 2013). Decidir cuál se quiere citar.
- `csjn_ucr2018`, `csjn_ucr2019`: sin Fallos (`---`). Según los fallos obligatorios: Santa Cruz = Fallos 341:1869; La Rioja = Fallos 342:343. *Río Negro* (Fallos 342:287), central en la línea, no tiene citekey.
- `csjn_ucr2018`, `csjn_ucr2019`, `csjn_ucr2019b`: sin PDF en la carpeta.
- `jgb2008`: `page: ---`; el PDF es una versión de autor de 46 pp. sin la paginación del libro.
- `gervasoni2011`: `note` arrastra `gervasoni2011a`.

### Discrepancias internas de las fuentes

- `mendez2021`, nota 2: «Fallos 336:2248» para Santiago del Estero (fondo); los fallos de la Corte citan 336:2148. Notas 3 y 4: La Rioja y Río Negro figuran ambos como «Fallos 342:235»; los fallos de la Corte citan La Rioja = 342:343 y Río Negro = 342:287. Las notas no se reproducen en el casebook.
- `mendez2021`, p. 57: «vulnera el art. 5º de la Constitución provincial» (por el contexto, el art. 5 de la Constitución Nacional). Se reproduce tal cual.
- `csjn_confederacion2024`, voto de Rosenkrantz, cons. 10: la lista de mandatos de Insfrán omite los períodos 1995-1999 y 1999-2003 como gobernador, aunque el mismo considerando le computa 37 años en los cargos.

### Discrepancias entre notas de clase y fuentes

- Las notas resumen a Méndez Montenegro y Vitaliani diciendo que en *Santiago* «la autonomía provincial no es "plena"» y listan «Máxima prudencia» como rasgo de *Santiago*. En el artículo, «máxima prudencia» aparece en la reseña de *Santa Cruz* (p. 57). Sin consecuencias: el casebook sigue al texto.
- Las notas mencionan para JGB que «las provincias "de bajo costo"» es tesis de Gervasoni; en JGB la expresión «bolsones potenciales de electores de bajo costo» se atribuye a Gibson y Calvo (p. 28), y Gervasoni aparece en nota (p. 35, n. 131).
- Las notas atribuyen a JGB «Desigualdad en el derecho / Experimentación jurídica / Aplicación de tratados» como «tres temas adicionales»: coincide con el texto (pp. 36-41).

## Fuentes — Unidad 8 (para integrar en FUENTES.md)

### Filas para la tabla de fuentes

| Citekey | Unidad | Carácter | PDF (en `Materiales_UBA/`) | Extracto | Modo | Paginación |
|---|---|---|---|---|---|---|
| `abregu1997` | 8 | obligatoria | `Unidad8/1_Abregú_Courtis_1997_La aplicación del derecho internacional de los derechos humanos por los.pdf` (28 pp) | `abregu1997.txt` | texto | **sin paginación impresa** (versión re-tipeada). Citar por sección (I–V). El capítulo publicado ocupa pp. 3–31 según `programauba.json`. Cuerpo: PDF 1–20; notas al final del archivo |
| `csjn_ekmekdjian1992` | 8 | obligatoria | `Unidad8/2_CSJN_1992_Ekmekdjian, Miguel Angel c.pdf` (58 pp, escaneo del tomo 315 de Fallos) | `csjn_ekmekdjian1992.txt` | OCR (copia corregida en `limpios/`) | citar por **voto + considerando**. Fallos 315 = PDF + 1491 (PDF 1 = p. 1492) |
| `csjn_ministerio2017` | 8 | optativa | `Unidad8/CSJN_2017_Ministerio de Relaciones Exteriores y Cultos s- informe de sentencia dictada en.pdf` (30 pp) | — | no extraído | sólo prosa breve y «Para seguir leyendo». Se leyó `corpus/texto/csjn_ministerio2017.txt` (voto que encabeza, cons. 1–3, 7–11, 16–20) |
| `csjn_giroldi1995` | 8 | optativa | sin PDF | — | — | sólo prosa (a través de la cita en Abregú, sección IV.2) y bibliografía |
| `csjn_esposito2004` | 8 | optativa | sin PDF | — | — | sólo bibliografía |
| `hitters2009`, `rosenkrantz2005`, `filippini2005`, `biscardi2016` | 8 | optativas | en `Unidad8/` | — | no extraídos | sólo «Para seguir leyendo» |

### Estructura interna del fallo

#### *Ekmekdjian c. Sofovich* (Fallos 315:1492), 7 de julio de 1992

- PDF 1: final del fallo anterior y comienzo de los sumarios; PDF 1–12: sumarios.
- Mayoría (Cavagna Martínez, Barra, Fayt, Nazareno, Boggiano): PDF 12–31, cons. 1–32. Firmas en PDF 31 (verificadas contra la imagen).
- Disidencia de Petracchi y Moliné O'Connor: PDF 31–47, cons. 1–26.
- Disidencia de Levene: PDF 48–55, cons. 1–22.
- Disidencia de Belluscio: PDF 56–58, cons. 1–6.
- Citas confirmadas en la base del observatorio (tabla `sumario`): Ekmekdjian 315:1492; Giroldi 318:514 (7/4/1995); Espósito 327:5668 (23/12/2004); Ministerio de Relaciones Exteriores 340:47 (14/2/2017; `programauba.json` no registra tomo y página).

### Copias corregidas (`extractos/limpios/`)

| Citekey | Copia | Estado | Notas |
|---|---|---|---|
| `csjn_ekmekdjian1992` | capa OCR previa del PDF del compendio (escaneo del tomo; conserva sangrías) | `revisado: si` | Corregidas: PDF 12–14, 18, 20–28, 30–31 (mayoría), 36–41, 46–47 (Petracchi y Moliné O'Connor), 52, 55 (Levene), 56–58 (Belluscio). Método: cotejo palabra por palabra con un segundo OCR independiente del mismo tomo (`scripts/fallo_db.py 315 1492`, tabla `vol_page`); cada discrepancia se resolvió una por una y las dudosas contra la imagen (PDF 18, 21, 22, 23, 25, 31, 37, 38, 39, 40, 58). Los pasajes en que los dos OCR coinciden no se cotejaron renglón por renglón con la imagen salvo en esas páginas. Se quitaron los encabezados de página en todo el archivo, una línea con un «0» suelto (cons. 5, PDF 13) que cortaba la página y el resto del cons. 5 deformado. «e/» por «c/» corregido en las carátulas citadas. Erratas del impreso conservadas: «art. 17 de la Convención de Viena» (cons. 18, PDF 21: el texto citado es el art. 27), «EVerfGE», «Cancado», «J.C.J.», «Steart», «servir legal y honradamente» (cons. 12, PDF 18). En PDF 40 el renglón «-algunos, muy atendibles-» terminaba en raya y el script lo pegaba a «en»: se subió «en» al renglón anterior |

### Limpieza (`extractos/limpieza/abregu1997.txt`)

Trece patrones, anclados al contexto exacto, para llamadas de nota pegadas a cifras o siglas que `MARCA_DE_NOTA` no reconoce: «art. 1.1**16**», «art. 2**17**», «art. 2.2**18**», «art. 2.1**19**», «art. 2**20**», «art. 3**21**» (sección II, PDF 4), «Corte IDH**28**», «Moncayo**38**», «CN**39**», «art. 7.5**51**», «Humanos 1995**53**», «Courtis**56**», «1976–1983**59**».

### Discrepancias con `programauba.json`

- `abregu1997`. La entrada lista como autores a Abregú y Courtis; el texto está firmado sólo por Martín Abregú (los dos son compiladores del volumen). El campo `container-title` mezcla compiladores, título del libro y editorial. `type` es `article-journal` aunque se trata de un capítulo de libro.
- `csjn_ministerio2017`. Sin `container-title`/`volume`/`page`: corresponde Fallos 340:47. El campo `note` dice `csjn_cippec2014` (resto de una fusión). El título dice «Cultos»; el fallo dice «Culto».
- `hitters2009`, `rosenkrantz2005`, `filippini2005`. El campo `title-short` de las tres arrastra el título de Abregú. `rosenkrantz2005` tiene «pŕestamos» con tilde errónea en el título.

### Discrepancias entre notas de clase y fuentes

- Las notas dicen que en *Martín & Cía.* «ley posterior deroga ley anterior». Abregú (sección III.1) dice que la Corte consideró que la eventual responsabilidad internacional no debía alterar la aplicación de la jerarquía legal de los tratados. U08 sigue al texto.
- Las notas ubican el programa de Sofovich como «la Noche del Domingo». El fallo dice «La Noche del Sábado» (mayoría, cons. 2) o «La noche del sábado» (disidencias).
- Las notas citan como art. 27 de la Convención de Viena el fundamento del cons. 18 de la mayoría; el tomo imprime «art. 17» (errata; el texto citado es el art. 27).
- Las notas atribuyen a *Ekmekdjian* (cons. 32) un intento de «restringir cómo se va a aplicar»; el cons. 32 trata de la extensión de la respuesta. Coincide en sustancia.

## Fuentes — Unidad 9 (para integrar en `FUENTES.md`)

### Tabla de fuentes

| Citekey | Unidad | Carácter | PDF (en `Materiales_UBA/`) | Extracto | Modo | Paginación |
|---|---|---|---|---|---|---|
| `rau2019` | 9 | obligatoria | `Unidad9/1_Álvarez Ugarte et al_2019_La actividad del Congreso.pdf` (23 pp) | `rau2019.txt` (copia de `corpus/texto/rau2019.txt`) | texto | versión de autor numerada 1-23 (= PDF), **sin la paginación de la obra** (pp. 528-562 según `programauba.json`). Citar por **apartado** (I a X) |
| `guidi2019` | 9 | obligatoria | `Unidad9/2_Guidi_2019_Elección y conformación de Cámaras.pdf` (15 pp) | `guidi2019.txt` (copia de `corpus/texto/guidi2019.txt`) | texto | versión de autor sin paginación impresa (la obra: pp. 503-527). Citar por **apartado** (1 a 4) |
| `csjn_famyl2000` | 9 | obligatoria | `Unidad9/3_CSJN - 2000 - Famyl S.A. c. Estado Nacional s. acción de amparo.pdf` (19 pp) | `csjn_famyl2000.txt` (copia de `corpus/texto/csjn_famyl2000.txt`) | texto | citar por **voto + considerando**. Fallos 323:2256 (confirmado en `csjn.db`, sumarios 38877-38880, 38936-38939, 39098-39105, 39139-39140) |
| `csjn_bussi2007` | 9 | optativa | `Unidad9/2007_Bussi, Antonio c.pdf` | — | no extraído | sólo «Para seguir leyendo»; descrito en prosa a través de Guidi, ap. 4 |
| `tula2004` | 9 | optativa | `Unidad9/María Inés Tula (2004)…pdf` | — | no extraído | sólo «Para seguir leyendo» |
| `pearce2019`, `ley27412`, `funcionamiento_parlamentario` | 9 | optativas | sin PDF | — | — | «(sin PDF en la carpeta)» |

### Calidad del texto y limpieza

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

### Estructura de *Famyl* (Fallos 323:2256), 29 de agosto de 2000

- Voto que encabeza el pronunciamiento (Moliné O'Connor, Fayt, Belluscio,
  Boggiano, Bossert): cons. 1-19 y parte dispositiva, PDF pp. 1-6.
- Nazareno, según su voto: PDF pp. 7-10. Adhiere a cons. 1-9; omite el cons.
  10 de la mayoría (regla de no revisión del procedimiento legislativo y su
  excepción); sus cons. 10-18 = cons. 11-19 de la mayoría.
- Petracchi, según su voto: PDF pp. 10-13 (cons. 1-6).
- Vázquez, en disidencia: PDF pp. 13-19 (cons. 1-19). Revoca: rige la alícuota
  reducida del 10,5%.
- La línea de firmas del compendio no incluye a López.

### Discrepancias con `programauba.json`

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

### Discrepancias entre notas de clase y fuentes (Unidad 9)

- Notas: en *Famyl* la promulgación parcial «viola el art. 76». El fallo
  aplica el **art. 80** (cons. 11-15). U09 sigue al fallo.
- Notas: la base constitucional de Diputados es «uno cada treinta mil». El
  art. 45 vigente dice uno cada **treinta y tres mil** (Guidi, ap. 3.1).
- Notas: «caso Collella». El comentario escribe «Colella» (Fallos 268:352).
- Notas: «CNE, caso Borocotó». Guidi lo cita como causa «Pagani»
  (CNE, sentencia 3738/2006).
- Notas atribuyen a la mayoría de *Famyl* los dos requisitos del art. 80
  «(cdo. 13)»: el test se enuncia en el cons. 12 y se aplica en el 13.

## Fuentes — Unidad 10 (para integrar en FUENTES.md)

### Tabla de fuentes

| Citekey | Unidad | Carácter | PDF (en `Materiales_UBA/`) | Extracto | Modo | Paginación |
|---|---|---|---|---|---|---|
| `saenz2019a` | 10 | obligatoria | `Unidad10/1_Sáenz and Sucunza - 2019 - Comentario al 75.12.pdf` (17 pp) | `saenz2019a.txt` | texto | **sin paginación impresa**. Citar por título de apartado. PDF pp. 1-3 = comentario al inc. 11 (moneda), sólo de Sucunza, no usado; el inc. 12 empieza al pie de PDF p. 3 |
| `arballo2019` (clave de extracto `arballo2019_art75inc13`) | 10 | obligatoria | `Unidad10/2_Arballo - 2019 - Comentario al 75.13.pdf` (21 pp) | `arballo2019_art75inc13.txt` | texto | **sin paginación impresa**. Citar por apartado (§ 1 a § 10) |
| `csjn_gcba2021` | 10 | optativa | `Unidad10/CSJN - 2021 - Gobierno de la Ciudad de Buenos Aires c. Estado Na.pdf` (91 pp) | — | no extraído | sólo en «Para seguir leyendo»; Fallos 344:809, 4-5-2021 confirmado en la base |
| `orlando2019` | 10 | optativa | `Unidad10/Orlando - 2019 - Federalismo Fiscal.pdf` (15 pp) | — | no extraído | sólo en «Para seguir leyendo» |
| `gelli2004`, `bidegain1998` | 10 | optativas | sin PDF | — | — | sólo en «Para seguir leyendo» |

Los dos extractos se copiaron de `corpus/texto/` (nivel A) con `# modo: texto`.
Se usan prácticamente completos: `saenz2019a` PDF pp. 3-17; `arballo2019_art75inc13` PDF pp. 1-21.

### Limpieza (`extractos/limpieza/`)

- `saenz2019a.txt`: 20 llamadas de nota pegadas a comillas de cierre, a «CN» o a puntos (patrones con el contexto exacto, uno por llamada); la llamada 17 pegada a «Ley N° 346» (PDF p. 4); y los dos renglones de continuación de la nota 7 que quedan al pie de PDF p. 3 antes del primer renglón numerado.
- `arballo2019_art75inc13.txt`: 64 llamadas de nota pegadas a comillas, puntos, años («de 18243», «de 199511») y signos («1964!6»). Patrones generados con contexto exacto (lookbehind de hasta diez caracteres y lookahead de tres).

### Discrepancias con `programauba.json`

- `arballo2019`: la entrada es el «Comentario al artículo 121» (Unidad 7). El PDF de la Unidad 10 es el comentario de Arballo al **art. 75 inc. 13**. Se cita `[@arballo2019]` para que cierre la cobertura y se extracta con la clave `arballo2019_art75inc13`. Hace falta una entrada propia (p. ej. `arballo2019b`, «Comentario al artículo 75 inc. 13»).
- `saenz2019a`: el campo `citation-key` dice `saenz2019` (distinto del `id`) y la entrada no registra páginas. Sucunza figura como coautor; el comentario al inc. 11 que trae el mismo PDF es sólo suyo.

### Erratas y discrepancias dentro de las fuentes (no corregidas; los extractos las reproducen)

Cotejadas con la base de sumarios de la CSJN (`observatorio-csjn/data/csjn.db`, tabla `sumario`):

- `saenz2019a`, nota 43: *Sandoval c. Neuquén* citado como Fallos 256:215 (1997); la base lo ubica en **Fallos 320:1344** (8-7-1997).
- `arballo2019_art75inc13`, § 4: *Nucete* fechado «de 2009» en el cuerpo; la nota y la base dan **Fallos 335:1222, 2012**.
- § 5: *Hidroeléctrica El Chocón* fechado «de 1999»; Fallos 320:1302 es de **1997**.
- § 9: los casos de *Telefónica* c. General Pico (320:162) y c. Chascomús (320:619) se presentan como «binomios jurisprudenciales del año 1998»; son de **1997**. Los de *Operadora* (321:658 y 321:1052) sí son de 1998.
- Nota 32: *Colgate Palmolive* citado como Fallos 336:3351 (2013); la nota 29 y la base dan **326:3351 (2003)**. El § 4 repite además el renglón de *Colgate* como viñeta separada.
- § 4 (*Dodero Viajes*): «la regla de supremacía del art. 30 de la Constitución Nacional»; la supremacía está en el art. 31. Posible errata del original; no se corrigió ni se comenta en la unidad.
- § 4 (*Barillari*): «Constituci6n», «econ6mico», «circulaci6n», «raz6n» están así en el PDF (verificado visualmente, PDF p. 11).
- § 5: «territorial”..46» (doble punto) está en el original.
- Erratas de la capa de texto de `saenz2019a` («derecho federalsólo», «localy», «CSJNque», «loscuales», «podríasustentarse», «exponeDulitzky») son palabras pegadas del PDF; se reproducen tal cual.

### Discrepancias entre notas de clase y fuentes (Unidad 10)

- Las notas dicen que el derecho común «es una delegación implícita de las provincias». Sáenz y Sucunza lo tratan como una atribución expresa del inc. 12 («Las provincias no ejercen el poder delegado a la Nación…»). U10 sigue al texto y no usa «implícita».
- Las notas mencionan *Farmacity* como caso pendiente; no está en ninguna lectura del programa y no se incluyó.
- Las notas citan páginas del compendio (pp. 330, 338, 354); el casebook cita por apartado porque los PDFs no tienen paginación impresa.

## U11 — notas de fuentes (para integrar en FUENTES.md)

### Tabla de fuentes

| Citekey | Unidad | Carácter | PDF (en `Materiales_UBA/`) | Extracto | Modo | Paginación |
|---|---|---|---|---|---|---|
| `god1991` | 11 | obligatoria | `Unidad11/1_O'Donnell_1991_Democracia Delegativa.pdf` (17 pp) | `god1991.txt` (copia de `corpus/texto/god1991.txt`) | texto | impresa = PDF **+6** (traducción en *Journal of Democracy en Español*, pp. 7-23). Notas al final, PDF pp. 16-17 (pp. 22-23) |
| `saenz2016b` | 11 (dueña) | obligatoria | `Unidad11/2_Sáenz - 2016 - Facultades normativas del poder ejecutivo.pdf` (21 pp) | `saenz2016b.txt` (copia de `corpus/texto/saenz2016b.txt`) | texto | **sin paginación impresa** (versión de imprenta). Citar por apartado (1 a 5, con 4.1 y 4.2) |
| `alegre2010` | 11 | optativa | `Unidad11/Alegre-Democracia sin presidentes.pdf` | — | no extraído | sólo «Para seguir leyendo» |
| `nino1988` | 11 | optativa | `Unidad11/Nino - 1988 - Presidencialismo v. Parlamentarismo.pdf` | — | no extraído (corpus nivel B) | sólo «Para seguir leyendo» |
| `ollier2012` | 11 | optativa | `Unidad11/Ollier_2012_Más allá del presidencialismo….pdf` | — | no extraído | sólo «Para seguir leyendo» |
| `sagues2001` | 11 | optativa | sin PDF en la carpeta | — | — | sólo «Para seguir leyendo» |

### Limpieza agregada

- `extractos/limpieza/god1991.txt`: encabezados de página («N Journal of Democracy en Español», «Guillermo O’Donnell N»), nota con asterisco de PDF p. 1 (sin número propio) y llamadas de nota 1-12 pegadas a la puntuación, que `MARCA_DE_NOTA` no toma. Todas ancladas en el texto vecino.
- `extractos/limpieza/saenz2016b.txt`: continuaciones de notas al pie que quedan antes del renglón con el número de la nota siguiente (fin de la nota 2 en PDF p. 2, de la nota 36 en p. 11, de la nota 55 en p. 18) y llamadas de nota que `MARCA_DE_NOTA` no toma (tras comillas tipográficas, mayúscula, cifra o espacio: 11, 16, 17, 21, 22, 24, 25, 28, 29, 33, 34, 37, 39, 40, 47, 48, 53, 57, 58, 59, 62, 66, 67).

### Párrafos

- `god1991`: los títulos de sección centrados («Acerca de las Instituciones», etc.) hacen que la heurística parta el primer párrafo de cada sección después del primer renglón; corregido con `unir:` en los cinco marcadores afectados. Los títulos no se extractan (los tramos empiezan después).
- `saenz2016b`: PDF p. 8 termina en «…arrastra aquel fallo.» a margen completo; no se puede saber si «Ello llevó a que…» (p. 9) abre párrafo. Se dejó unido (mismo criterio que Holmes p. 17).

### Discrepancias con `programauba.json`

- `god1991`. La entrada remite a *Novos Estudos* (CEBRAP) 31 (1991), pp. 25-40, en portugués. El PDF de la carpeta es la traducción castellana de la versión inglesa («Delegative Democracy», *Journal of Democracy* 5:1, 1994, pp. 55-69), publicada en *Journal of Democracy en Español* (pp. 7-23). La nota del autor la llama «versión corregida y abreviada» del texto de 1991. El casebook cita por la paginación de la traducción. Convendría ajustar la entrada (o agregar una nueva) para la edición que efectivamente se lee.
- `saenz2016b`. **El id está duplicado en `programauba.json`**: hay dos entradas con `id: saenz2016b`, una «Facultades normativas del poder ejecutivo» (correcta para U11) y otra «Artículo 30. Reforma de la Constitución», pp. 78-90 (que es la obra de `saenz2016a`). Con ids duplicados, el resultado de citeproc es impredecible: hay que eliminar o renombrar la segunda. Ver también la discrepancia de U06 (`saenz2016_art14y28`).
- `saenz2016b`. La entrada lleva `page: "---"`.

### Erratas del original conservadas (`saenz2016b`)

«leye 26.364» (ap. 3), «Aceval Pollachi» en el cuerpo y «Pollacchi» en la nota (ap. 4.2), «revindicación» (ap. 4.1), «este Tribunales» (cita de *Verrocchi*, ap. 4.1), «Decreto Nº 1.204/200151» (ap. 5; el «51» tiene el cuerpo del texto en la capa del PDF y no corresponde a ninguna llamada de nota de esa página), «Mas reciente», «claúsula», «universos», «poder de reglamentar las (“Cocchia”…)» y la frase trunca «siempre que para que el contenidos de una ley» (ap. 5).

### Discrepancias entre notas de clase y fuentes (Unidad 11)

- Las notas citan a O'Donnell: «Riña general por un beneficio restringido y a corto plazo» (p. 18). El texto dice «riña general por **el** beneficio restringido y a corto plazo» (p. 18).
- Bajo el excursus sobre O'Donnell, las notas explican por qué la dinámica delegativa no se da en EE.UU. («Congreso más fuerte por las circunscripciones uninominales»). O'Donnell no trata a EE.UU.; su contraste es Uruguay y Chile (pp. 16-17). El argumento parece venir de Nino (optativa).
- Las notas (resumen de Sáenz) ponen al Jefe de Gabinete como «Titular de la Administración Pública Nacional». Sáenz dice que el titular jerárquico es el Presidente; la reforma procuró transferir al Jefe de Gabinete el ejercicio directo de la administración y eso «no se ha trasladado a la práctica» (ap. 2).
- Las notas incluyen la reglamentación (99.2) y los DNU (99.3) dentro de la «potestad co-legislativa». Sáenz llama co-legislativas a la iniciativa (art. 77) y al veto (arts. 80 y 83), y enumera aparte la reglamentación y la legislación por delegación o urgencia (ap. 2); en el ap. 3 sí califica de «co-legislativa» la facultad reglamentaria en la tradición de Cádiz.
- (Para U12) Las notas fechan *Peralta* en 1992; Sáenz dice 1990 (ap. 4.1).

## U12 — notas de fuentes (para integrar en FUENTES.md)

### Tabla de fuentes

| Citekey | Unidad | Carácter | PDF (en `Materiales_UBA/`) | Extracto | Modo | Paginación |
|---|---|---|---|---|---|---|
| `csjn_delfino1927` | 12 | obligatoria | `Unidad12/1_CSJN - 1927 - Delfino, A.M. y Cía.pdf` (8 pp) | `csjn_delfino1927.txt` | texto | citar por **considerando**. Versión de la Colección de Análisis Jurisprudencial (La Ley), sin paginación de Fallos |
| `csjn_mouviel1957` | 12 | obligatoria | `Unidad12/2_CSJN - 1957 - Mouviel, Raúl Oscar y otros.pdf` (21 pp) | `csjn_mouviel1957.txt` | texto (con limpieza mecánica, ver abajo) | dictamen del procurador: PDF pp. 2-17; sentencia: PDF pp. 17-21. Los considerandos de la sentencia **no están numerados**: citar «sentencia» o «dictamen» |
| `csjn_peralta1990` | 12 | obligatoria | `Unidad12/3_CSJN - 1990 - Peralta, Luis Arcenio y otro c Estado Nacional (M.pdf` (31 pp) | `csjn_peralta1990.txt` | texto | citar por **voto + considerando**. Impresión web de biblioteca.jus.gov.ar (La Ley 1991-C, 158) |
| `csjn_verrocchi1999` | 12 | obligatoria | `Unidad12/4_CSJN - 1999 - Verrochi, Ezio Daniel c. Poder Ejecutivo Nacional.pdf` (27 pp) | `csjn_verrocchi1999.txt` | texto | citar por **voto + considerando**. Copia oficial de la Corte (V. 916. XXXII) |
| `csjn_prattico1960`, `csjn_massa2006`, `csjn_colegio2008`, `csjn_consumidores2010`, `csjn_blanco2018` | 12 | optativas | carpeta `Unidad12/` | — | no extraídas | sólo «Para seguir leyendo»; `colegio2008` y `consumidores2010` se describen en prosa (texto de `corpus/texto/`) |

### Estructura interna de los fallos

#### *Delfino* (Fallos 148:430), 20 de junio de 1927
- Cons. 1-2: procedencia del recurso; cons. 3-18: fondo; parte dispositiva (confirma).
- Firmas en el compendio: Bermejo, Repetto, «Laurentena» (sic; Laurencena).

#### *Mouviel* (Fallos 237:636), 17 de mayo de 1957
- Dictamen de Sebastián Soler, 25 de abril de 1956 (PDF pp. 2-17).
- Sentencia unánime (PDF pp. 17-21): Orgaz, Argañarás, Galli, Herrera, Villegas Basavilbaso. Revoca.

#### *Peralta* (Fallos 313:1513), 27 de diciembre de 1990
- Dictamen del procurador Oscar E. Roger (PDF pp. 3-8).
- Mayoría (PDF pp. 9-26): cons. 1-15 amparo; 16-31 reglamentos de necesidad y urgencia; 32-59 contenido (unión nacional, emergencia, propiedad, igualdad). Firmas: Levene, Cavagna Martínez, Fayt, Barra, Nazareno, Moliné O'Connor.
- Oyhanarte, disidencia de fundamentos y según su voto (PDF pp. 26-30): amparo inapto; rechaza la demanda.
- Belluscio (PDF pp. 30-31): en las firmas, «en disidencia de fundamentos»; el voto se titula «Disidencia»; revoca y rechaza el amparo por falta de prueba de inexistencia de otras vías.
- Petracchi no firma.

#### *Verrocchi* (Fallos 322:1726), 19 de agosto de 1999
- Voto que encabeza (Fayt, Belluscio, Bossert): PDF pp. 1-6, cons. 1-11.
- Petracchi, por su voto: PDF pp. 7-13, cons. 7-18 (adhiere a los cons. 1-6 de la mayoría).
- Boggiano, por su voto: PDF pp. 14-17, cons. 1-10.
- Disidencia conjunta de Nazareno, Moliné O'Connor y López: PDF pp. 18-27, cons. 1-15.

### Limpieza

- `extractos/limpieza/csjn_peralta1990.txt`: encabezado «5/13/2018 Fallo Peralta» y pie con la URL de biblioteca.jus.gov.ar y el folio «N/31».
- `extractos/limpieza/csjn_verrocchi1999.txt`: carátula repetida en páginas impares («V. 916. XXXII.», «Verrocchi, Ezio Daniel c/ …», «C orteS uprema deJ usticia dela N ación») y marcas «ES COPIA», «VO-//-», «DISI-//-».
- `csjn_mouviel1957`: **limpieza mecánica en el extracto**. El PDF trae en el margen superior de cada página un renglón con sólo «19» (y el folio al pie). Como `NOTA_AL_PIE` (renglón con sólo un número) corta la página **antes** de aplicar `LIMPIEZA`, un patrón en `extractos/limpieza/` no alcanza: el corte dejaba un renglón por página. En la copia `extractos/csjn_mouviel1957.txt` se borraron con `perl` los 38 renglones que contienen sólo un número y la marca «19» pegada al final de 4 renglones (PDF pp. 4, 14, 15, 20). No se tocó ninguna otra palabra; la cabecera lo documenta (`# limpieza_mecanica`). `diff` contra `corpus/texto/csjn_mouviel1957.txt`: 38 renglones borrados y 4 modificados. **Propuesta al coordinador**: en `verificar.py`/`insertar_extractos.py`, aplicar `LIMPIEZA` antes del corte de notas, o bien anclar `NOTA_AL_PIE` a la mitad inferior de la página.

### Discrepancias con `programauba.json`

- `csjn_mouviel1957` aparece **dos veces** en el JSON (una con `note` de sincronización).
- `csjn_verrocchi1999`: `citation-key` dice `csjn_verrochi1999` y el título «Verrochi» (la carátula oficial es «Verrocchi»); `note` arrastra basura (`…csjn_partidodemocrata1957`).
- `csjn_delfino1927`: `citation-key` dice `csjn_deflino1927`; `note` con basura (`…csjn_adc2012`). Sin fecha en la base del observatorio, pero los sumarios 121268, 121856, 122408 y 123426 confirman Fallos 148:430.
- Citas de Fallos confirmadas con los sumarios de `csjn.db`: 148:430, 237:636, 313:1513, 322:1726.

### Erratas de los textos que los extractos reproducen tal cual

- *Delfino*, cons. 5: «que la contribución ha puesto» (por «constitución»); firma «Laurentena».
- *Mouviel*, sentencia: «ratificado por la ley 13.830» (el dictamen y el sumario 94392 dicen 13.030); «nulla pna» (por «poena»); «La primera de estas formas de no puede» (dictamen).
- *Verrocchi*: «legistativo» (voto que encabeza, cons. 7); asteriscos de la capa de texto («deba*tes», «Cá*mara», «situacio*nes», «mayo*ría»).
- *Peralta*: «le punto» (cons. 15, fuera de los extractos), «objectivos» (cons. 20), «persecusión» (sumario).

### Discrepancias entre notas de clase y fuentes

- Las notas fechan *Peralta* en 1992 y *Verrocchi* en 1998; los fallos son del 27/12/1990 y del 19/8/1999. U12 sigue a los fallos.
- Las notas resumen *Mouviel* diciendo que «el Congreso sí delegó al PEN, lo que es inconstitucional». La sentencia declara inconstitucional el art. 7 inc. a del decreto 33.265/44 (ratificado por ley) y dice que el art. 27 del Código de Procedimientos sólo atribuye la facultad de *juzgar* faltas. U12 sigue a la sentencia.
- Las notas presentan las dos condiciones de *Verrocchi* como requisitos; el cons. 9 exige la concurrencia de «alguna de estas dos circunstancias» (disyuntiva). U12 sigue al texto.

## Fuentes — Unidad 13 (para integrar en `FUENTES.md`)

### Tabla de fuentes

| Citekey | Unidad | Carácter | PDF (en `Materiales_UBA/`) | Extracto | Modo | Paginación |
|---|---|---|---|---|---|---|
| `csjn_siri1957` | 13 | obligatoria | `Unidad13/1_FALLO CCXXXIX. .pdf` (11 pp, copia mecanografiada de la sentencia; imagen deficiente) | `csjn_siri1957.txt` (OCR del **tomo impreso de Fallos 239**, pp. 459-467, desde `csjn.db` con `fallo_db.py 239 459`) | OCR (copia corregida en `limpios/`) | marcador `[[PDF p. N]]` = página impresa de Fallos 239. Considerandos sin numerar: se citan como «últimos considerandos» con la página de Fallos entre paréntesis |
| `csjn_kot1958` | 13 | obligatoria | `Unidad13/2_CSJN - 1958 - Samuel, Kot S.R.L..pdf` (12 pp, escaneo a doble página del tomo impreso) | `csjn_kot1958.txt` (OCR del tomo impreso de Fallos 241, pp. 291-313, desde `csjn.db`, tabla `vol_page`, vol_id 243) | OCR (copia corregida en `limpios/`) | `[[PDF p. N]]` = página impresa de Fallos 241. Voto que encabeza sin numerar (se cita con la página de Fallos); disidencia por considerando |
| `csjn_rizzo2013` | 13 | obligatoria (en U05 optativa: sólo bibliografía) | `Unidad13/3_CSJN_2013_Rizzo, Jorge Gabriel c.pdf` (67 pp, escaneo de la sentencia firmada con capa OCR previa) | `csjn_rizzo2013.txt` (OCR del **tomo impreso de Fallos 336-I**, pp. 760-831, `fallo_db.py 336 760 --fuente volumen --hasta 837`, recortado en 831) | OCR (copia corregida en `limpios/`) | `[[PDF p. N]]` = página impresa de Fallos 336. Se cita por voto y considerando |
| `csjn_colegio2021` | 13 | obligatoria | `Unidad13/4_CSJN - 2021 - Colegio de Abogados de la Ciudad de Buenos Aires c.pdf` (55 pp, texto nativo) | `csjn_colegio2021.txt` (copia de `corpus/texto/csjn_colegio2021.txt`) | texto | `[[PDF p. N]]` = página del PDF de la Corte. Se cita por voto y considerando |
| `otegui2016` | 13 | optativa | `Unidad13/Otegui - 2016 - Recurso extraordinario federal...pdf` | — | — | sólo en «Para seguir leyendo» |
| `csjn_halabi2009` | 13 | optativa | `Unidad13/CSJN - 2009 - Halabi.pdf` | — | — | sólo en «Para seguir leyendo» |
| `ferreyra2016` | 13 | optativa | `Unidad13/Ferreyra - 2016 - Acción de Amparo.pdf` | — (se usa `corpus/texto/ferreyra2016.txt` para una cita en prosa) | texto (nivel A) | sin paginación impresa en el PDF: se cita por apartado («Ley 16986», «El amparo después de 1983») |
| `vergara2016` | 13 | optativa | `Unidad13/Vergara_Viola_2016_Competencia Federal.pdf` | — | — | sólo en «Para seguir leyendo» |
| `dassen2016` | 13 | optativa | `Unidad13/Dassen_Guidi_2016_Consejo de la Magistratura...pdf` | — | — | sólo en «Para seguir leyendo» |

### Copias corregidas (`extractos/limpios/`)

| Citekey | Copia | Estado | Notas |
|---|---|---|---|
| `csjn_siri1957` | OCR del tomo impreso de Fallos 239 (`csjn.db`, `vol_page`), sin encabezados de página | `revisado: si` | **Revisadas Fallos 239:463-467** (voto que encabeza y disidencia de Herrera). La imagen del tomo no está disponible; se cotejó contra la copia mecanografiada del compendio (PDF 3-11), que trae el mismo texto con diferencias menores de forma («núms.» por «nº», «solo» por «sólo»; agrega «Notifíquese y devuélvanse»). Correcciones puntuales: «garantín», «inte-egridad», «clánsulas», «ambigiiedades», «ell...», «n existe», «4 quo», «qne», «argiiir», «decorosy», «hase», «ardenamiento», comillas duplicadas, restos de margen («S», «E», «: :», «UPALRS IA»). Versalitas del impreso («GONZÁLEZ», firmas) transcriptas como «González» y en mayúsculas. «vol. III … nº 82; confr., además, nº 89 y 90» reconstruido del OCR («vol. 111 … n* 82 … n” 89»). 459-462 sin revisar (sumarios y dictámenes: no se extractan) |
| `csjn_kot1958` | OCR del tomo impreso de Fallos 241 (vol_id 243), sin encabezados de página. El fallo no está en `vol_start`, por eso `fallo_db.py` falla: se leyeron las páginas 291-313 directamente de `vol_page` (sólo lectura) | `revisado: si` | **Revisadas Fallos 241:298-309 y 312-313**, contra la imagen del mismo tomo que reproduce el compendio (PDF 5-12, doble página). El OCR confunde sistemáticamente «c» con «e» («eon», «euyo», «cireunstancia»), «u» con «n» («partienlares»), y deforma las versalitas: cada caso se corrigió por separado contra la imagen. Se conservan grafías del impreso: «proteje», «ocassio», «incluídos», «ni cual es el estado». Versalitas (Jofré, Ennecce-rus-Nipperdey, Alberdi, Balladore Pallieri, Mortati, Jellinek, Colliard, De Cupis, Vallarta, Dimock) en minúsculas y mayúsculas; firmas en mayúsculas. Ordinales de la disidencia como «1º)» … «14º)», como en el impreso. 291-297 (sumarios, dictamen, resultas) y 310-311 (cons. 6 a 10 de la disidencia) sin revisar |
| `csjn_rizzo2013` | OCR del tomo impreso de Fallos 336-I, sin encabezados de página ni los renglones en blanco del OCR (caían en medio de los párrafos: los puntos y aparte se fijaron con `parrafo:` contra la sangría del original) | `revisado: si` | **Revisadas Fallos 336:784-800** (voto que encabeza, cons. 10 a 35), **814-816** (Petracchi y Argibay, cons. 11 a 14) y **820-831** (Zaffaroni, cons. 3 a 17). Método: comparación palabra por palabra contra la capa OCR del escaneo del compendio (`corpus/texto/csjn_rizzo2013.txt`) y, en cada discrepancia, contra la imagen (PDF 7, 15-16, 18-22, 32, 65). El OCR del tomo es mucho mejor que el del escaneo; sus errores típicos: «%» por «°», «(..)» por «(…)», rayas perdidas o duplicadas («-—», «—-»), «Órgano» con mayúscula, «1V» por «IV», «Op. Ccit.» por «op. cit.». Puntos suspensivos: «(…)»/«…» donde el original trae el carácter de elipsis, «(...)» donde trae tres puntos. Se agregaron las comillas simples de «‘representantes de los jueces’» (cons. 23), que el OCR perdió. Dos renglones con sólo «336» (encabezados mal leídos) quitados. El resto (dictamen, cons. 1-9 y 36-43 del voto que encabeza, cons. 1-10 de Petracchi y Argibay, cons. 1-2 de Zaffaroni) sin revisar |

`csjn_colegio2021` es texto nativo (`# modo: texto`). Carátula repetida en las páginas impares: patrones en `extractos/limpieza/csjn_colegio2021.txt`, anclados a la sangría profunda.

Detalle técnico: la cabecera de los `limpios/` no puede contener la cadena `[[PDF` antes de `# revisado:` ---`cabecera()` corta en el primer `[[PDF`---; por eso la línea de paginación dice «el marcador de página = …». (`extractos/limpios/csjn_elortondo1888.txt`, de otra unidad, tiene `# paginacion: [[PDF p. N]]` en la línea 6: si `revisado` va después, no se lee. No lo toqué.)

### Discrepancias con `programauba.json` y entre fuentes

- `csjn_siri1957`: el campo `note` arrastra basura de sincronización (`mlzsync1:…csjn_siri1958`). La fecha completa es 27 de diciembre de 1957 (la entrada sólo tiene el año).
- `csjn_kot1958`: el `title` es «Samuel, Kot S.R.L.» (la carátula es «Kot, Samuel S. R. L. s/ recurso de hábeas corpus»); `note` con basura de sincronización (`…csjn_cullen1893`). Fecha completa: 5 de septiembre de 1958.
- `csjn_rizzo2013`: sin fecha completa (18 de junio de 2013, confirmada en `csjn.db`, tabla `sumario`).
- `ferreyra2016` y `otegui2016` tienen la misma paginación en la entrada (871–887); ya anotado en `corpus/manifiesto.csv`.
- Ferreyra cita *Siri* como «Fallos 329:459» (nota 5); es 239:459.
- *Kot*: el ordinal de la Cámara en el impreso es «Cámara 3ª»; el OCR del tomo lo leía «3*».

### Material en la carpeta fuera del programa

- `Unidad13/CSJN_1988_Di Mascio.pdf`, `Unidad13/CSJN_2015_Uriarte c.pdf` (fallos sin citekey; *Uriarte* lo cita *Colegio de Abogados*, cons. 13 y 17).
- `Unidad13/Madison et al_2006_El Federalista No.pdf`.
- `Unidad13/Maurino - 2016 - Los procesos colectivos.pdf`.
- `Unidad13/Garantia-de-imparcialidad-y-perspectiva-de-genero.pdf`.

### Discrepancias entre notas de clase y fuentes

- Las notas (U13, «Caso Rizzo») cuentan cuatro vicios de la ley 26.855: equilibrio, representación, independencia y «demasiadas restricciones sobre la posibilidad de candidatearse». El cons. 29 del voto que encabeza enumera los cuatro primeros como equilibrio, representación, independencia y «vulnera el ejercicio de los derechos de los ciudadanos al distorsionar el proceso electoral»; las restricciones a las candidaturas (cons. 36 a 40) se tratan aparte, «sin perjuicio de lo expuesto». U13 sigue al texto.
- La tabla de las notas atribuye a la ley 26.855 «6 académicos» y a la ley 26.080 «Se excluye» al presidente de la Corte; coincide con *Rizzo* cons. 15 y *Colegio de Abogados* cons. 10 y 17. Las notas dicen que la composición de 24.937/24.939 era de 20 miembros, y *Colegio de Abogados* (cons. 17) lo confirma.
- Las notas dicen que la ley 16.986 vedaba el amparo «si existían otros recursos disponibles» y fijaba «15 días hábiles»: coincide con Ferreyra (apartado «Ley 16986»).

## Fuentes — Unidad 14 (para integrar a FUENTES.md)

### Tabla de fuentes

| Citekey | Unidad | Carácter | PDF (en `Materiales_UBA/`) | Extracto | Modo | Paginación |
|---|---|---|---|---|---|---|
| `alegre2020` | 14 | obligatoria | `Unidad14/1_Alegre et al. - 2020 - Cuidar la vida y la Constitución La limitación de.pdf` (10 pp) | `alegre2020.txt` (copia de `corpus/texto/alegre2020.txt`) | texto | impresa = PDF (pie «-N-»). Informe de 10 pp |
| `csjn_lee2020` | 14 | obligatoria | `Unidad14/2_CSJN - 2020 - Lee, Carlos Roberto y otro c Consejo de Atención .pdf` (17 pp) | `csjn_lee2020.txt` (copia de `corpus/texto/csjn_lee2020.txt`) | texto | citar por **considerando**. Fallo unánime, un solo voto: PDF pp. 1–16; p. 17, partes |
| `csjn_petcoff2020` | 14 | optativa | `Unidad14/CSJN - 2020 - Petcoff Naidenoff, Luis c. Provincia de Formosa s.pdf` (6 pp) | — | no extraído (OCR previo, nivel B) | sólo en «Para seguir leyendo» y en prosa |
| `csjn_ibarrola2021` | 14 | optativa | `Unidad14/CSJN - 2021 - Ibarrola, Natalia Romina c. Provincia de Formosa s.pdf` (12 pp) | — | no extraído (texto nativo en `corpus/texto/`) | citado en prosa por considerando, sin extracto |

### Limpieza agregada (`extractos/limpieza/`)

- `csjn_lee2020.txt`: carátula repetida en las páginas impares (seis renglones, uno por patrón; el bloque no funcionaba porque otro archivo de limpieza ya quita «ORIGINARIO»), y unión del renglón partido en «Covid-|19─» (cons. 1, PDF p. 1).
- `alegre2020.txt`: llamadas de nota 2–22 pegadas a un punto o a comillas tipográficas (MARCA_DE_NOTA no las toma), incluida «art. 23¹³»; continuación de la nota 15 en el pie de PDF p. 7, sin número propio; unión del renglón partido en «demostrarlo-|son» (PDF p. 9). **Defecto residual**: el impreso dice «demostrarlo- son» (raya de cierre de inciso y espacio); el extracto insertado dice «demostrarlo-son». Sin el patrón quedaba «demostrarloson».
- Ninguna de las dos fuentes tiene renglones de margen con sólo un número al comienzo de página; no hizo falta tocar las copias en `extractos/`.

### Párrafos

`alegre2020`: puntos y aparte fijados con `parrafo:` contra la imagen del PDF (pp. 2–10, revisadas visualmente). `csjn_lee2020`: dos `unir:` en el cons. 2 (renglones que terminan en «a)» y «g)»).

### Discrepancias con `programauba.json`

- `csjn_lee2020`: la entrada tiene `volume`/`page` «---». La base de la CSJN confirma **Fallos 343:1704** (sumarios 153103-153116), y así lo cita *Ibarrola* (cons. 9 y 11).
- `csjn_ibarrola2021`: la entrada tiene `page` «---». Base CSJN: **Fallos 344:316**. Además el título dice «Ibarrola, Natalia Romina»; el fallo y la base dicen «Ibarrola, **Romina Natalia**».
- `csjn_petcoff2020`: Fallos 343:944 confirmado (sumario 152087, 10 de septiembre de 2020), con carátula «Petcoff Naidenoff, Luis **Carlos** c/ Formosa, Provincia de s/ amparo - habeas corpus». Es un requerimiento de informes. *Ibarrola* (cons. 10 y 11) cita otra decisión de la misma causa, «Petcoff Naidenoff, Luis», **Fallos 344:126** (25 de febrero de 2021, incidente de inhibitoria según la base), que no está en el programa.

### Discrepancias entre notas de clase y fuentes (Unidad 14)

- Las notas dicen que *Petcoff* «resuelve sobre» el cierre de las fronteras internas. La decisión del compendio (Fallos 343:944) sólo requiere informes a la provincia en tres días. U14 sigue al texto.
- Las notas dicen que *Lee* «es la continuidad, mismos hechos» de *Petcoff*. Son causas distintas (actores, expediente y vía procesal distintos) sobre el mismo programa provincial de ingreso; *Lee* no cita *Petcoff*. U14 presenta los casos como una línea sobre el mismo problema.
- Las notas ubican la «escala movediza» en el cons. 10 de *Lee*. El estándar del escrutinio creciente está en el cons. 7; el cons. 10 desarrolla el argumento temporal.

## Fuentes — Unidad 15 (para integrar en `FUENTES.md`)

### Tabla de fuentes

| Citekey | Unidad | Carácter | PDF (en `Materiales_UBA/`) | Extracto | Modo | Paginación |
|---|---|---|---|---|---|---|
| `gargarella2009e` | 15 | obligatoria | `Unidad15/2_Gargarella - 2009 - Constitucionalismo y Privacidad.pdf` (18 pp; imagen en `corpus/pdf/gargarella2009e.pdf`) | `gargarella2009e.txt` (copia de `corpus/texto/`) | OCR `spa` | impresa = PDF **+778**. Capítulo XXIX: pp. 779-796 |
| `csjn_cha1991` | 15 | obligatoria | `Unidad15/3_CSJN_1991_Comunidad Homosexual Argentina c. Inspección General de Justicia.pdf` (95 pp = tomo impreso, Fallos 314:1531-1625) | `csjn_cha1991.txt` (OCR del tomo impreso, `scripts/fallo_db.py 314 1531`) | OCR (copia corregida en `limpios/`) | `[[PDF p. N]]` = página impresa de Fallos; PDF del compendio p. *n* = Fallos 1530 + *n*. Citar por voto y considerando |
| `csjn_alitt2006` | 15 | obligatoria | `Unidad15/4_CSJN - 2006 - Asociación Lucha por la Identidad Travesti Transex.pdf` (43 pp) | `csjn_alitt2006.txt` (copia de `corpus/texto/`) | texto nativo, marcado `ocr` por la codificación (copia corregida en `limpios/`) | citar por voto y considerando |
| `csjn_bazterrica1986` | 15 | optativa | `Unidad15/CSJN - 1986 - Bazterrica, Gustavo Mario.pdf` | — | no extraído | sólo en «Para seguir leyendo» y en una mención de la introducción |
| `csjn_fal2012` | 15 | optativa | `Unidad15/CSJN_2012_FAL.pdf` | — (se consultó `corpus/texto/csjn_fal2012.txt`, cons. 8 y 20) | no extraído | mencionado en prosa sin extracto (cons. 8 y 20) |
| `csjn_castillo2017`, `monti2014`, `nino1992a` | 15 | optativas | en `Unidad15/` | — | no extraídos | sólo en «Para seguir leyendo» |
| `faerman2010`, `maurino2009` | 15 | optativas | sin PDF en la carpeta | — | — | sólo en «Para seguir leyendo» |

### Estructura interna de los fallos

#### *Comunidad Homosexual Argentina* (Fallos 314:1531), 22 de noviembre de 1991

- Sumarios: Fallos 1531-1544. «Fallo de la Corte Suprema»: 1544-1549, cons. 1° a 13, firmado por Levene (H) solo.
- Votos concurrentes (página de inicio según el encabezado de cada voto en el OCR del tomo): Cavagna Martínez 1550, Barra 1559, Belluscio 1569, Nazareno 1573, Moliné O'Connor 1579, Boggiano 1585-1596.
- Disidencia de Fayt: 1596-1604, cons. 1° a 18.
- Disidencia de Petracchi: 1605-1625, cons. 1° a 23.
- Resultado: siete votos por la improcedencia, dos disidencias.

#### *ALITT* (Fallos 329:5266), 21 de noviembre de 2006

- Voto que encabeza el pronunciamiento: PDF pp. 1-20, cons. 1° a 24. Firmas: Petracchi, Highton de Nolasco, Fayt (según su voto), Maqueda, Zaffaroni, Lorenzetti, Argibay.
- Voto de Fayt: PDF pp. 23-43, cons. 1° a 23 (desarrollo paralelo). PDF p. 21 sólo lleva «VO-//-»; p. 22 está en blanco.

### Copias corregidas (`extractos/limpios/`)

| Citekey | Copia | Estado | Notas |
|---|---|---|---|
| `gargarella2009e` | transcripción corregida del OCR de `corpus/texto/`, página por página contra la imagen de `corpus/pdf/gargarella2009e.pdf` | `revisado: si` | **Capítulo completo (PDF 1-18, pp. 779-796).** Un párrafo por renglón; sin notas al pie, llamadas de nota ni encabezados. Rayas como «–». PDF 15 (p. 793): el margen corta las primeras letras de varios renglones; completadas por el contexto («usar», «medidas», «final», «no se encuentran», «sujetos», «supuesto», «tan», «sujeto», «pregunta», «genuinamente»). Se conserva la errata «ser considera como tal» (p. 792) y «defendiéramos» (p. 794, verificado con ampliación). «sta-tus quo» (p. 791) transcripto «status quo» |
| `csjn_cha1991` | OCR del tomo impreso de Fallos (csjn.db, `vol_page`) con encabezados quitados y párrafos reunidos | `revisado: si` (sólo las páginas usadas) | Revisadas contra la imagen del compendio: Fallos 1546-1549, 1589-1591, 1593-1595, 1599-1602, 1604, 1611-1620, 1623-1625. Ordinales «1º)» → «1°)» (el OCR los leía «1%)», «29)», «72)»). Palabras pegadas por la justificación del impreso separadas una por una («porotra», «acuestionarlainterpretación», «elcarácterarbitrario», etc.). Comillas simples internas restituidas en los cons. 19 y 23 de Petracchi. Rayas de cierre de inciso a fin de renglón conservadas (6 casos detectados y revisados). Se conserva «se envile y degrada» (cons. 19 de Petracchi, p. 1617). El resto del archivo es OCR sin revisar |
| `csjn_alitt2006` | capa de texto nativa del PDF con corrección mecánica de la codificación | `revisado: si` (PDF 1-20) | La capa codifica la raya como «C» («CindicóC», «Csubrayó la cámaraC») y «¿» como «)». Se reemplazaron los 77 casos de «C» (revisados en contexto) y el único «)por qué» (PDF 7). Cotejo visual de PDF 7 y 16. Se quitaron la carátula de las páginas impares, los pies «- N -», «ES COPIA» y cinco renglones en blanco espurios entre palabra cortada y continuación. El extracto base lleva `# modo: ocr` sólo para que la inserción use la copia corregida; es nivel A |

### Discrepancias con `programauba.json`

- `gargarella2009e`. La entrada dice `page: 173–231` (copiado de `gargarella2009a`, como ya advierte `corpus/manifiesto.csv`). El capítulo del compendio es el XXIX y ocupa **pp. 779-796**; el encabezado de las páginas pares es «Igualdad, libertad de expresión, acceso a la información...». La entrada dice `volume: I`; no se verificó si el capítulo está en el tomo I o en el II. El campo `note` dice `saldivia09`.
- `csjn_cha1991`. La entrada sólo tiene el año; la fecha es **22 de noviembre de 1991** (Fallos 314:1544). `title-short: CSJN`, inusual.
- `nino1992a`. El campo `citation-key` dice `nino1992`, distinto del `id`.
- `csjn_bazterrica1986`, `csjn_castillo2017`, `csjn_fal2012`. El campo `note` arrastra restos de sincronización (`...csjn_nicosia`, `csjn_cippec2014`, `...csjn_garrido2016`).
- `faerman2010`. Sin PDF. En la carpeta hay `Fernández Valle_2010_Derechos sexuales y reproductivos.pdf`; el manifiesto pregunta si corresponde. No se verificó: la unidad lo lista como material fuera del programa.

### Discrepancias detectadas en las fuentes

- Gargarella, nota 9 (p. 786): cita *Montalvo* como «Fallos 308: 1392». Esa es la cita de *Bazterrica* según `programauba.json` y según la disidencia de Petracchi en *CHA* (cons. 22). El texto dice además que *Montalvo* desdijo a *Bazterrica* «unos meses atrás»; *Bazterrica* es de 1986. U15 no reproduce la cita de Fallos de *Montalvo* ni la fecha.
- `Unidad15/CSJN - 2000 - González de Delgado.pdf` está en la carpeta de la U15 y corresponde a `csjn_gonzalez2000` (U16).

### Discrepancias entre notas de clase y fuentes (Unidad 15)

- Las notas numeran la unidad como 16 («Unidad 16 - Autonomía personal»); el programa v25 la numera 15.
- Las notas atribuyen a Gargarella, como ejemplo de paternalismo difícil, «cinco días para realizar aborto». El texto usa el divorcio y un plazo de tres meses (p. 792). U15 sigue al texto.
- Las notas agrupan *CHA*, *Montalvo* y *Griswold*–*Roe* como blancos de la crítica a Devlin. En el texto, *CHA* y *Montalvo* se critican por perfeccionistas (pp. 785-786); *Griswold* y *Roe*, por su concepción espacial y familiar de la privacidad (pp. 786-789). U15 sigue al texto.
- Las notas atribuyen a Nino cuatro tipos de daño a terceros inadmisibles. Nino (`nino1992a`) es optativo y no se leyó para esta unidad: U15 no los usa.
- Las notas sobre *F.A.L.* citan el cons. 8; el texto del fallo (`corpus/texto/csjn_fal2012.txt`) coincide. U15 agrega que el art. 19 invocado es el *in fine* (principio de reserva), cons. 20.

## Fuentes — Unidad 16 (para integrar en FUENTES.md)

### Tabla de fuentes

| Citekey | Unidad | Carácter | PDF (en `Materiales_UBA/`) | Extracto | Modo | Paginación |
|---|---|---|---|---|---|---|
| `saba2005` | 16 | obligatoria | `Unidad16/1_Saba - 2005 - (Des)igualdad estructural copy.pdf` (29 pp) | `saba2005.txt` | texto | versión de autor numerada 1-29, sin paginación de revista: **página citada = PDF** |
| `treacy2011` | 16 | obligatoria | `Unidad16/2_Treacy - 2011 - Categorías sospechosas y control de constitucional.pdf` (36 pp) | `treacy2011.txt` | texto | impresa = PDF **+180** (*Lecciones y Ensayos* 89, pp. 181-216) |
| `csjn_gonzalez2000` | 16 | obligatoria | `Unidad16/3_CSJN - 2000 - González de Delgado.pdf` (44 pp; idéntico, mismo md5, a `Unidad15/CSJN - 2000 - González de Delgado.pdf`) | `csjn_gonzalez2000.txt` | texto | citar por **voto + considerando** |
| `csjn_gonzalez2000` (dictamen) | 16 | obligatoria | no está en el PDF del compendio; tomo impreso de Fallos 323 vía `csjn.db` (`fallo_db.py 323 2659 --fuente volumen`) | `csjn_gonzalez2000_dictamen.txt` (clave de extracto distinta de la citekey; se cita `[@csjn_gonzalez2000]`) | ocr (copia en `limpios/`) | página impresa de Fallos (323:2670-2673); citar por apartado del dictamen |
| `csjn_repetto1988` | 16 | optativa | `Unidad16/CSJN - 1988 - Repetto...pdf` | — | no extraído | sólo en «Para seguir leyendo» y descrito en prosa (vía Treacy y Saba) |
| `csjn_reyes2007` | 16 | optativa | `Unidad16/CSJN - 2007 - Reyes Aguilera.pdf` | — | no extraído | ídem |
| `saldivia2018` | 16 | optativa | `Unidad16/Saldivia Menajovsky - 2018 - ...pdf` | — | no extraído | sólo en «Para seguir leyendo» |

### Estado de `limpios/`

| Citekey | Copia | Estado | Notas |
|---|---|---|---|
| `csjn_gonzalez2000_dictamen` | capa de texto del tomo de Fallos 323 (vol_id 379, motor `pdftotext`) | `revisado: si` | Sólo pp. 2670-2673 (aps. V a VII del dictamen y firma). **Sin imagen disponible**: el compendio no trae el dictamen y la base no guarda el PDF del tomo. Correcciones por contexto, una por error: «arto»→«art.», «a qua»→«a quo», «NQ»→«Nº», «gobiemo»→«gobierno», «00 lo que»→«En lo que», «Suprem:-»→«Suprema», «{producto»→comillas, «N acianal», «accionan tes», «por.», «241J265»→«241/265». En p. 2671 la capa desordena palabras en columnas; el orden se restituyó por la sintaxis y por la transcripción del fallo de Cámara que el propio dictamen cita (y los sumarios 39608-39614 de la base). Conviene cotejar contra el tomo impreso cuando haya acceso |

### Cambios mecánicos en extractos de texto

- `saba2005.txt`: se quitó el renglón con la sola llamada de nota «9» (PDF p. 3, superíndice de «Mill»), que el corte de notas tomaba como comienzo del pie y truncaba la página. Documentado en la cabecera.
- `csjn_gonzalez2000.txt`: se quitaron 24 renglones en blanco espurios dentro de párrafos (PDF pp. 8-9, 11-13, 19-20, voto de Petracchi), que partían frases y palabras con guion. Documentado en la cabecera.
- `treacy2011.txt`: sin cambios.

### Patrones de limpieza (`extractos/limpieza/`)

- `saba2005.txt`: dos continuaciones de notas por encima del primer número (PDF pp. 5 y 26); llamadas de nota tras cifra, comilla tipográfica o espacio (generadas recorriendo la numeración 1-78 en orden y ancladas con 5-14 caracteres de contexto).
- `treacy2011.txt`: encabezados y pie de imprenta («Lecciones y ensayos 89.indd …»); bloque de notas al pie (desde el primer renglón «N. » a 15 espacios hasta el pie; las notas de esta revista no empiezan con un renglón de sólo número); cuatro continuaciones de notas (PDF pp. 11, 19, 23, 29); llamadas de nota tras punto, comilla o raya (numeración 1-58).
- `csjn_gonzalez2000.txt`: carátula de páginas impares («G. 653. XXXIII.», «RECURSO DE HECHO», carátula de partes, «ES COPIA») y continuación de la nota 5 del voto de Petracchi (PDF p. 19).
- Se corrió `verificar.py` sobre todas las unidades con estos patrones: no rompen ningún marcador ajeno (el único problema reportado es `@klarmann` en U01, ajeno a U16).

### Discrepancias con `programauba.json`

- `csjn_gonzalez2000`: la entrada da `page: 2659` (Fallos 323:2659), confirmado por la base (sumarios 39608-39983, vol_start 323:2659). El campo `note` arrastra basura de sincronización (`mlzsync1:…csjn_nicosia`).
- `saba2005`: la entrada registra la *Revista Derecho y Humanidades* 11 (2005) sin páginas; el PDF es una versión de autor sin paginación de revista y su portada registra otras dos publicaciones (UCES 2004, pp. 479-514; Alegre y Gargarella 2007). Se cita por la numeración del PDF.
- `treacy2011`: `container-title` dice «Lecciones y Ensayos No» (sobra «No»); falta el número (89).

### Discrepancias entre fuentes

- *González de Delgado*: Treacy dice que la mayoría rechazó con fundamentos ajenos a la igualdad, vinculados a la competencia (p. 200 n. 31); Saba, que «la mayoría de los argumentos de los Ministros» se articularon en torno a la no discriminación (p. 24). El texto del fallo da la razón a Treacy respecto de la sentencia (remisión al dictamen); la observación de Saba sólo vale para los votos concurrentes. Se planteó como pregunta (nota 6).
- Saba atribuye a Petracchi la frase sobre «perpetuar la inferioridad legal, social y económica de la mujer» (p. 25); en el voto (cons. 9) es la descripción de lo que sostuvo la Corte norteamericana en *United States v. Virginia*, que Petracchi hace suya en la nota 5. Se planteó como pregunta (nota 7).
- Treacy escribe «Mantecón Valdez» en el cuerpo y «Mantecón Valdés» en la nota 23 y en p. 197; «Arenzon» y «Arenzón». Se reproducen tal cual.
- El programa habla de igualdad como «no subordinación»; Saba usa «no sometimiento (o no exclusión)». Se señala en «El problema».

### Discrepancias entre notas de clase y fuentes

Las notas tratan la igualdad bajo el título «Unidad 17» con el copete de un programa anterior.

- Las notas dicen que Saba postula una visión «robusta» de la igualdad; el término es de Saldivia (optativa). Saba habla de igualdad «estructural».
- Las notas definen la desigualdad estructural como la que «no es el resultado de una circunstancia (p.ej. crisis económicas) sino que tiene una evolución constante». El texto la define por el sometimiento y la exclusión sistemática de grupos por otros grupos (pp. 4, 20); la contraposición con las crisis no aparece.
- Las notas dicen que el argumento le permitió a Saba defender la paridad de género o una lista partidaria sólo de mujeres. El texto no trata esos casos; su ejemplo final es una agencia estatal que sólo contrata mujeres (pp. 27-28). La unidad sigue al texto.

## Fuentes — Unidad 17 (para integrar en FUENTES.md)

### Tabla de fuentes

| Citekey | Unidad | Carácter | PDF (en `Materiales_UBA/`) | Extracto | Modo | Paginación |
|---|---|---|---|---|---|---|
| `elias2014a` | 17 | obligatoria | `Unidad17/1_Elías_2014_El derecho de propiedad en la Constitución argentina.pdf` (14 hojas, doble página) | `elias2014a.txt` | OCR (copia corregida en `limpios/`) | cada hoja lleva dos marcadores `[[PDF p. n]]` (izq., der.); impresa = **2n+683** (izq.) / **2n+684** (der.); hoja 1: izq. en blanco, der. = p. 685. Capítulo: pp. 685-711 |
| `csjn_ercolano1922` | 17 | obligatoria | `Unidad17/2_CSJN - 1922 - Ercolano c. Lanteri de Renshaw.pdf` (17 hojas, doble página) | `csjn_ercolano1922.txt` | OCR del tomo impreso de Fallos (csjn.db, `vol_page`, vol_id 136), copia corregida en `limpios/` | `[[PDF p. N]]` = **página impresa de Fallos 136**. Citar la mayoría por página de Fallos (no numera considerandos) y la disidencia por considerando |
| `csjn_coihue2021` | 17 | optativa | `Unidad17/CSJN - 2021 - Coihue S.R.L. c Santa Cruz...pdf` (90 pp) | — | no extraído | sólo en «Para seguir leyendo» |
| `sola2010a` | 17 | optativa | `Unidad17/Sola - 2010 - Manual de Derecho Constitucional (extracto).pdf` | — | no extraído | sólo en «Para seguir leyendo» |
| `zeberio2006` | 17 | optativa | `Unidad17/Zeberio - 2006 - Los hombres y las cosas...pdf` | — | no extraído | sólo en «Para seguir leyendo» |
| `saenz2019` | 17 | optativa | `Unidad17/Sáenz - 2016 - El derecho de propiedad. Control de razonabilidad .pdf` | — | no extraído | sólo en «Para seguir leyendo» |
| `csjn_avico1934` | 17 | optativa | sin PDF en la carpeta | — | — | sólo en «Para seguir leyendo» |

### Copias corregidas (`extractos/limpios/`)

| Citekey | Copia | Estado | Notas |
|---|---|---|---|
| `elias2014a` | transcripción revisada renglón por renglón contra la imagen (corpus/pdf/elias2014a.pdf, 300 dpi, enderezada con `magick -deskew`), a partir de un re-OCR por mitad de hoja (tesseract `--psm 6`, recorte de márgenes por coordenadas) | `revisado: si` | **Capítulo completo, pp. 685-711.** El OCR del corpus (`corpus/texto/elias2014a.txt`) entrelaza las columnas en las mitades izquierdas y es inservible; el re-OCR de una mitad por vez sale casi limpio. Sin notas al pie, llamadas de nota ni encabezados; punto y aparte = renglón en blanco; cursivas y versalitas no conservadas. Erratas del impreso conservadas: «susceptibles regulación», «estaría sujetos», «puede imponer» (por «pueden»), «por dar mencionar», «en la que la no funciona», «en relación el producto». La cita de Cianciardo y Zambrano (p. 692), en bloque en el impreso, queda como párrafo |
| `csjn_ercolano1922` | OCR del tomo impreso de Fallos (`scripts/fallo_db.py 136 160 --hasta 194`), transcripto contra la imagen del compendio (corpus/pdf/csjn_ercolano1922.pdf, hojas 10-33, que reproduce el mismo tomo) | `revisado: si` | **Fallos 136:170-193 completas** (mayoría y disidencia de Bermejo). Sumarios, sentencia de primera instancia y dictamen (pp. 160-169) no se incluyen. Erratas del impreso conservadas: «ultrepasados» (cons. 14), «Block v. Hirsth» (cons. 11), «Munn v. Yllinois» (cons. 27), «Granger Caces», «sic utere tuó ut alienum non ledas» (cons. 21), «dá», «incluído», «perfectamente innocua», «cumplimento» (cons. 23). Las comillas repetidas al comienzo de cada renglón de las citas largas, uso tipográfico de la época, se suprimieron |

Los extractos crudos (`extractos/elias2014a.txt`, `extractos/csjn_ercolano1922.txt`) son copias del OCR con `# modo: ocr`; se quitaron mecánicamente los renglones que contienen sólo un número (documentado en la cabecera). No hizo falta ningún patrón de `extractos/limpieza/`.

### Discrepancias con `programauba.json`

- `csjn_avico1934`: la entrada dice `volume: 248, page: 21`. La base de la CSJN (sumarios y `vol_start`) ubica *Avico, Oscar Agustín c/ de la Pesa, Saúl G.* en **Fallos 172:21** (1934), que es también la cita de Elías (n. 7 y 41). Corregir el tomo.
- `csjn_ercolano1922`: la entrada (136:161) coincide con la base; `vol_start` registra el encabezado del caso en 136:160 (comienzo de los sumarios). El fallo de la Corte está en 136:170-179 y la disidencia en 136:180-193. Elías cita «Fallos 136:170» (n. 40 y 45). La carátula de la base agrupa tres causas (Ercolano c/ Lanteri Renshaw; Cooke c/ Naveira; Urrutia c/ Dellepiane).
- `elias2014a`: la entrada no registra páginas (pp. 685-711) ni el título completo del capítulo («El derecho de propiedad en la Constitución Nacional: una introducción teórica»). El campo `editor` duplica a Elías como autor y editor (correcto: es uno de los directores del *Tratado*).
- `saenz2019`: el PDF de la carpeta está fechado 2016 («El derecho de propiedad. Control de razonabilidad»); ya anotado en `corpus/manifiesto.csv`. No se usó.

### Discrepancias entre notas de clase y fuentes

- Las notas numeran la unidad como «Unidad 18 --- Propiedad»; en el programa v25 es la 17.
- Las notas ubican en «p. 706» el pasaje en que Elías identifica el pluralismo en la jurisprudencia de la Corte; en el impreso está en p. 707 (sección III).
- Las notas atribuyen a Elías tres problemas de que «el contenido patrimonial exige un control judicial menos intenso». En el texto, los tres problemas «macro» (pérdida de valor de la Constitución, legitimidad sociológica del Poder Judicial, efectos sobre el desarrollo) se derivan de relegar la propiedad a un derecho «de segunda categoría» (pp. 710-711); la crítica a la fórmula del control menos intenso es un párrafo previo (p. 709). U17 sigue al texto.
- Las notas resumen el test de *Ercolano* como «fin legítimo; no se afecta la sustancia; razonable en su extensión proporcionada y temporal». El fallo habla de la «naturaleza, las causas determinantes y la extensión de la medida restrictiva» y del límite del precio arbitrario o confiscatorio (Fallos 136:177-178); la fórmula de la «sustancia» no aparece. U17 sigue al texto.

### Otras observaciones

- Gargarella (`gargarella2021`, Unidad 5, p. 222) atribuye a la Corte presidida por Bermejo haber declarado inconstitucionales los controles de precios de alquileres; en *Ercolano* la mayoría los convalidó y Bermejo quedó en disidencia. El mismo párrafo registra luego el giro de *Ercolano* y la vuelta en *Mango* (1925). U17 cita a Gargarella sólo para la secuencia y para la presidencia de Bermejo.
- La nota 71 de Elías cita *Fayt* como Fallos 322:1616, en línea con lo anotado en FUENTES.md para `csjn_fayt1999`.

## U18 — notas de fuentes (para integrar a FUENTES.md)

### Filas de la tabla de fuentes

| Citekey | Unidad | Carácter | PDF (en `Materiales_UBA/`) | Extracto | Modo | Paginación |
|---|---|---|---|---|---|---|
| `courtis2001` | 18 | obligatoria | `Unidad18/1_Abramovich_Courtis_2009_Apuntes sobre la exigibilidad de los deechos sociales.pdf` (28 pp) | `courtis2001.txt` (copia corregida en `limpios/`) | OCR `spa` | impresa = PDF **+971**. Capítulo XXXVII: pp. 973-998 (PDF 2-27). PDF 1 = p. 972 (final del capítulo anterior); PDF 28 = portadilla «Constitución y medio ambiente» |
| `csjn_quisbeth2012` | 18 | obligatoria | `Unidad18/2_CSJN_2012_Quisbeth Castro c.pdf` (58 pp) | `csjn_quisbeth2012.txt` | texto | citar por **voto + considerando** |
| `csjn_salas2011`, `gargarella2007a`, `holmes2015`, `csjn_benghalensis2000`, `csjn_defensor2007`, `csjn_mendoza2008` | 18 | optativas | en `Unidad18/` | — | no extraídas | sólo en «Para seguir leyendo» (y mención de una línea en «El problema») |

### Copias corregidas (`extractos/limpios/`)

| Citekey | Copia | Estado | Notas |
|---|---|---|---|
| `courtis2001` | re-OCR propio: `pdftoppm -r 400 -gray`, `magick -deskew 40% -threshold 60%`, `tesseract -l spa --psm 6`, página por página | `revisado: si` | **Capítulo completo revisado (PDF 2-27, pp. 973-998).** El OCR del corpus (`ocrmypdf`) entrelazaba renglones en PDF 4, 5, 8 y 23 y era inutilizable allí. Se quitaron encabezados, notas al pie y llamadas de nota; se corrigió con ediciones puntuales, una por error, contra la imagen (lectura de todas las páginas con Read; ampliaciones de PDF 4, 17, 19, 23). Renglones renglón por renglón como en el impreso, con guiones de corte; renglones en blanco sólo para títulos, citas en bloque e incisos i-iii; el resto de los puntos y aparte se fijó con `parrafo:` en los marcadores de U18. Rayas de inciso como «–», cursivas no conservadas. **Margen derecho cortado en el escaneo** en PDF 4 (p. 975), PDF 24 (p. 995) y, en menor medida, PDF 22 (p. 993): las letras perdidas se completaron por el contexto (p. ej. «pro-tección», «Judi-cial», «auto-motor», «que debe desarrollar», «del PIDESC», «una barrera»). La reconstrucción menos segura es «derecho de propiedad: a ello se destina» (p. 975): la puntuación tras «propiedad» no se ve; también «a sus titulares como el servicio educativo» (sin coma, p. 975). Convendría cotejarlas con otra copia del texto |

### Discrepancias con `programauba.json`

- `courtis2001`. La entrada describe Abramovich y Courtis, «Apuntes sobre la exigibilidad judicial de los derechos sociales», *Cuadernos electrónicos de filosofía del derecho* 4 (2001), `page: 4`. El PDF del compendio es otra edición: capítulo XXXVII de una obra colectiva con título corriente «Derechos sociales/Derechos colectivos», pp. 973-998, que el manifiesto del corpus fecha en 2009 (el nombre del archivo dice 2009). No se identificó la obra (la p. 972 cierra un capítulo sobre diálogo democrático y la p. 999 abre «Constitución y medio ambiente»). U18 cita con la paginación del compendio y lo advierte en la «Ubicación». Además, el orden de autores en la entrada es Courtis, Abramovich; el capítulo firma «Víctor Abramovich y Christian Courtis».
- `csjn_quisbeth2012`. La entrada dice Fallos **335:454** y fecha **2012-06-24**. La base de la CSJN (`sumario`, ids 620-628, 671, 156521) registra **Fallos 335:452**, 24 de abril de 2012; la sentencia del compendio está fechada «Buenos Aires, 24 de abril de 2012». U18 usa 335:452 y el 24 de abril en la ficha; la bibliografía sigue sin corregir. Carátula en la base: «Q.C.S.Y. c/ Gobierno de la Ciudad de Buenos Aires y otro s/ amparo».

### Estructura interna de *Quisbeth Castro* (Fallos 335:452), 24 de abril de 2012

- Voto que encabeza el pronunciamiento: cons. 1° a 17 y parte dispositiva, PDF pp. 1-31. Firmas: Lorenzetti, Highton de Nolasco, Fayt, Maqueda, Zaffaroni; Petracchi y Argibay «según su voto».
- Voto de Petracchi: PDF pp. 32-43. Remite a los cons. 1° a 7° de la mayoría; cons. 8° a 18 propios.
- Voto de Argibay: PDF pp. 45-57 (PDF 44 sin texto). Cons. 1º a 12 propios.
- PDF 58: enlace al dictamen de la Procuración (no incluido).
- Mezcla «°» (voto que encabeza, Petracchi) y «º» (Argibay, algunos de Petracchi) en los ordinales de los considerandos: las anclas los copian tal cual.

### Limpieza

- `extractos/limpieza/csjn_quisbeth2012.txt`: carátula repetida en las páginas impares («Q. 64. XLVI.», «Q. C., S. Y. c/ Gobierno de la Ciudad de Buenos», «Aires s/ amparo.»), anclada con 20 o más espacios iniciales. «RECURSO DE HECHO», «ES COPIA», «-//-» y los números de página «-N-» ya los quitan patrones existentes.

### Discrepancias entre notas de clase y fuentes (Unidad 18)

- Las notas de clase numeran esta unidad como «Unidad 19 — DESC» (y la 18 como «Propiedad»); el programa v25 la numera 18.
- Las notas presentan la «indeterminación fáctica» como segundo obstáculo de Abramovich y Courtis. En el texto es la tercera observación dentro del primer obstáculo, «La determinación de la conducta debida» (pp. 990-991); los obstáculos son cuatro: determinación de la conducta debida, autorrestricción frente a cuestiones políticas y técnicas, inadecuación de los mecanismos procesales y escasa tradición de control (pp. 987-998). U18 sigue al texto.
- Las notas atribuyen a *Quisbeth* la exigencia de un «mínimo razonable (c. 12)». La expresión no aparece en el fallo; el cons. 12 del voto que encabeza habla de una «garantía mínima del derecho fundamental» y de las «garantías mínimas indispensables». U18 usa la fórmula del fallo.
- Las notas ubican la discusión sobre recursos y planificación en el cons. 15; el argumento presupuestario está en el cons. 14 (pautas del Comité sobre el «máximo de los recursos») y la crítica a la falta de planificación coordinada al final del cons. 15. Coincide en lo sustancial.
