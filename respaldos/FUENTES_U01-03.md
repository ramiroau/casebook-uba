# Fuentes — Unidades 1 a 3

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
