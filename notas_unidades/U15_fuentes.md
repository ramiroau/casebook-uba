# Fuentes — Unidad 15 (para integrar en `FUENTES.md`)

## Tabla de fuentes

| Citekey | Unidad | Carácter | PDF (en `Materiales_UBA/`) | Extracto | Modo | Paginación |
|---|---|---|---|---|---|---|
| `gargarella2009e` | 15 | obligatoria | `Unidad15/2_Gargarella - 2009 - Constitucionalismo y Privacidad.pdf` (18 pp; imagen en `corpus/pdf/gargarella2009e.pdf`) | `gargarella2009e.txt` (copia de `corpus/texto/`) | OCR `spa` | impresa = PDF **+778**. Capítulo XXIX: pp. 779-796 |
| `csjn_cha1991` | 15 | obligatoria | `Unidad15/3_CSJN_1991_Comunidad Homosexual Argentina c. Inspección General de Justicia.pdf` (95 pp = tomo impreso, Fallos 314:1531-1625) | `csjn_cha1991.txt` (OCR del tomo impreso, `scripts/fallo_db.py 314 1531`) | OCR (copia corregida en `limpios/`) | `[[PDF p. N]]` = página impresa de Fallos; PDF del compendio p. *n* = Fallos 1530 + *n*. Citar por voto y considerando |
| `csjn_alitt2006` | 15 | obligatoria | `Unidad15/4_CSJN - 2006 - Asociación Lucha por la Identidad Travesti Transex.pdf` (43 pp) | `csjn_alitt2006.txt` (copia de `corpus/texto/`) | texto nativo, marcado `ocr` por la codificación (copia corregida en `limpios/`) | citar por voto y considerando |
| `csjn_bazterrica1986` | 15 | optativa | `Unidad15/CSJN - 1986 - Bazterrica, Gustavo Mario.pdf` | — | no extraído | sólo en «Para seguir leyendo» y en una mención de la introducción |
| `csjn_fal2012` | 15 | optativa | `Unidad15/CSJN_2012_FAL.pdf` | — (se consultó `corpus/texto/csjn_fal2012.txt`, cons. 8 y 20) | no extraído | mencionado en prosa sin extracto (cons. 8 y 20) |
| `csjn_castillo2017`, `monti2014`, `nino1992a` | 15 | optativas | en `Unidad15/` | — | no extraídos | sólo en «Para seguir leyendo» |
| `faerman2010`, `maurino2009` | 15 | optativas | sin PDF en la carpeta | — | — | sólo en «Para seguir leyendo» |

## Estructura interna de los fallos

### *Comunidad Homosexual Argentina* (Fallos 314:1531), 22 de noviembre de 1991

- Sumarios: Fallos 1531-1544. «Fallo de la Corte Suprema»: 1544-1549, cons. 1° a 13, firmado por Levene (H) solo.
- Votos concurrentes (página de inicio según el encabezado de cada voto en el OCR del tomo): Cavagna Martínez 1550, Barra 1559, Belluscio 1569, Nazareno 1573, Moliné O'Connor 1579, Boggiano 1585-1596.
- Disidencia de Fayt: 1596-1604, cons. 1° a 18.
- Disidencia de Petracchi: 1605-1625, cons. 1° a 23.
- Resultado: siete votos por la improcedencia, dos disidencias.

### *ALITT* (Fallos 329:5266), 21 de noviembre de 2006

- Voto que encabeza el pronunciamiento: PDF pp. 1-20, cons. 1° a 24. Firmas: Petracchi, Highton de Nolasco, Fayt (según su voto), Maqueda, Zaffaroni, Lorenzetti, Argibay.
- Voto de Fayt: PDF pp. 23-43, cons. 1° a 23 (desarrollo paralelo). PDF p. 21 sólo lleva «VO-//-»; p. 22 está en blanco.

## Copias corregidas (`extractos/limpios/`)

| Citekey | Copia | Estado | Notas |
|---|---|---|---|
| `gargarella2009e` | transcripción corregida del OCR de `corpus/texto/`, página por página contra la imagen de `corpus/pdf/gargarella2009e.pdf` | `revisado: si` | **Capítulo completo (PDF 1-18, pp. 779-796).** Un párrafo por renglón; sin notas al pie, llamadas de nota ni encabezados. Rayas como «–». PDF 15 (p. 793): el margen corta las primeras letras de varios renglones; completadas por el contexto («usar», «medidas», «final», «no se encuentran», «sujetos», «supuesto», «tan», «sujeto», «pregunta», «genuinamente»). Se conserva la errata «ser considera como tal» (p. 792) y «defendiéramos» (p. 794, verificado con ampliación). «sta-tus quo» (p. 791) transcripto «status quo» |
| `csjn_cha1991` | OCR del tomo impreso de Fallos (csjn.db, `vol_page`) con encabezados quitados y párrafos reunidos | `revisado: si` (sólo las páginas usadas) | Revisadas contra la imagen del compendio: Fallos 1546-1549, 1589-1591, 1593-1595, 1599-1602, 1604, 1611-1620, 1623-1625. Ordinales «1º)» → «1°)» (el OCR los leía «1%)», «29)», «72)»). Palabras pegadas por la justificación del impreso separadas una por una («porotra», «acuestionarlainterpretación», «elcarácterarbitrario», etc.). Comillas simples internas restituidas en los cons. 19 y 23 de Petracchi. Rayas de cierre de inciso a fin de renglón conservadas (6 casos detectados y revisados). Se conserva «se envile y degrada» (cons. 19 de Petracchi, p. 1617). El resto del archivo es OCR sin revisar |
| `csjn_alitt2006` | capa de texto nativa del PDF con corrección mecánica de la codificación | `revisado: si` (PDF 1-20) | La capa codifica la raya como «C» («CindicóC», «Csubrayó la cámaraC») y «¿» como «)». Se reemplazaron los 77 casos de «C» (revisados en contexto) y el único «)por qué» (PDF 7). Cotejo visual de PDF 7 y 16. Se quitaron la carátula de las páginas impares, los pies «- N -», «ES COPIA» y cinco renglones en blanco espurios entre palabra cortada y continuación. El extracto base lleva `# modo: ocr` sólo para que la inserción use la copia corregida; es nivel A |

## Discrepancias con `programauba.json`

- `gargarella2009e`. La entrada dice `page: 173–231` (copiado de `gargarella2009a`, como ya advierte `corpus/manifiesto.csv`). El capítulo del compendio es el XXIX y ocupa **pp. 779-796**; el encabezado de las páginas pares es «Igualdad, libertad de expresión, acceso a la información...». La entrada dice `volume: I`; no se verificó si el capítulo está en el tomo I o en el II. El campo `note` dice `saldivia09`.
- `csjn_cha1991`. La entrada sólo tiene el año; la fecha es **22 de noviembre de 1991** (Fallos 314:1544). `title-short: CSJN`, inusual.
- `nino1992a`. El campo `citation-key` dice `nino1992`, distinto del `id`.
- `csjn_bazterrica1986`, `csjn_castillo2017`, `csjn_fal2012`. El campo `note` arrastra restos de sincronización (`...csjn_nicosia`, `csjn_cippec2014`, `...csjn_garrido2016`).
- `faerman2010`. Sin PDF. En la carpeta hay `Fernández Valle_2010_Derechos sexuales y reproductivos.pdf`; el manifiesto pregunta si corresponde. No se verificó: la unidad lo lista como material fuera del programa.

## Discrepancias detectadas en las fuentes

- Gargarella, nota 9 (p. 786): cita *Montalvo* como «Fallos 308: 1392». Esa es la cita de *Bazterrica* según `programauba.json` y según la disidencia de Petracchi en *CHA* (cons. 22). El texto dice además que *Montalvo* desdijo a *Bazterrica* «unos meses atrás»; *Bazterrica* es de 1986. U15 no reproduce la cita de Fallos de *Montalvo* ni la fecha.
- `Unidad15/CSJN - 2000 - González de Delgado.pdf` está en la carpeta de la U15 y corresponde a `csjn_gonzalez2000` (U16).

## Discrepancias entre notas de clase y fuentes (Unidad 15)

- Las notas numeran la unidad como 16 («Unidad 16 - Autonomía personal»); el programa v25 la numera 15.
- Las notas atribuyen a Gargarella, como ejemplo de paternalismo difícil, «cinco días para realizar aborto». El texto usa el divorcio y un plazo de tres meses (p. 792). U15 sigue al texto.
- Las notas agrupan *CHA*, *Montalvo* y *Griswold*–*Roe* como blancos de la crítica a Devlin. En el texto, *CHA* y *Montalvo* se critican por perfeccionistas (pp. 785-786); *Griswold* y *Roe*, por su concepción espacial y familiar de la privacidad (pp. 786-789). U15 sigue al texto.
- Las notas atribuyen a Nino cuatro tipos de daño a terceros inadmisibles. Nino (`nino1992a`) es optativo y no se leyó para esta unidad: U15 no los usa.
- Las notas sobre *F.A.L.* citan el cons. 8; el texto del fallo (`corpus/texto/csjn_fal2012.txt`) coincide. U15 agrega que el art. 19 invocado es el *in fine* (principio de reserva), cons. 20.
