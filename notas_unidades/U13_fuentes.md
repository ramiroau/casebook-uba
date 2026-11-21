# Fuentes — Unidad 13 (para integrar en `FUENTES.md`)

## Tabla de fuentes

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

## Copias corregidas (`extractos/limpios/`)

| Citekey | Copia | Estado | Notas |
|---|---|---|---|
| `csjn_siri1957` | OCR del tomo impreso de Fallos 239 (`csjn.db`, `vol_page`), sin encabezados de página | `revisado: si` | **Revisadas Fallos 239:463-467** (voto que encabeza y disidencia de Herrera). La imagen del tomo no está disponible; se cotejó contra la copia mecanografiada del compendio (PDF 3-11), que trae el mismo texto con diferencias menores de forma («núms.» por «nº», «solo» por «sólo»; agrega «Notifíquese y devuélvanse»). Correcciones puntuales: «garantín», «inte-egridad», «clánsulas», «ambigiiedades», «ell...», «n existe», «4 quo», «qne», «argiiir», «decorosy», «hase», «ardenamiento», comillas duplicadas, restos de margen («S», «E», «: :», «UPALRS IA»). Versalitas del impreso («GONZÁLEZ», firmas) transcriptas como «González» y en mayúsculas. «vol. III … nº 82; confr., además, nº 89 y 90» reconstruido del OCR («vol. 111 … n* 82 … n” 89»). 459-462 sin revisar (sumarios y dictámenes: no se extractan) |
| `csjn_kot1958` | OCR del tomo impreso de Fallos 241 (vol_id 243), sin encabezados de página. El fallo no está en `vol_start`, por eso `fallo_db.py` falla: se leyeron las páginas 291-313 directamente de `vol_page` (sólo lectura) | `revisado: si` | **Revisadas Fallos 241:298-309 y 312-313**, contra la imagen del mismo tomo que reproduce el compendio (PDF 5-12, doble página). El OCR confunde sistemáticamente «c» con «e» («eon», «euyo», «cireunstancia»), «u» con «n» («partienlares»), y deforma las versalitas: cada caso se corrigió por separado contra la imagen. Se conservan grafías del impreso: «proteje», «ocassio», «incluídos», «ni cual es el estado». Versalitas (Jofré, Ennecce-rus-Nipperdey, Alberdi, Balladore Pallieri, Mortati, Jellinek, Colliard, De Cupis, Vallarta, Dimock) en minúsculas y mayúsculas; firmas en mayúsculas. Ordinales de la disidencia como «1º)» … «14º)», como en el impreso. 291-297 (sumarios, dictamen, resultas) y 310-311 (cons. 6 a 10 de la disidencia) sin revisar |
| `csjn_rizzo2013` | OCR del tomo impreso de Fallos 336-I, sin encabezados de página ni los renglones en blanco del OCR (caían en medio de los párrafos: los puntos y aparte se fijaron con `parrafo:` contra la sangría del original) | `revisado: si` | **Revisadas Fallos 336:784-800** (voto que encabeza, cons. 10 a 35), **814-816** (Petracchi y Argibay, cons. 11 a 14) y **820-831** (Zaffaroni, cons. 3 a 17). Método: comparación palabra por palabra contra la capa OCR del escaneo del compendio (`corpus/texto/csjn_rizzo2013.txt`) y, en cada discrepancia, contra la imagen (PDF 7, 15-16, 18-22, 32, 65). El OCR del tomo es mucho mejor que el del escaneo; sus errores típicos: «%» por «°», «(..)» por «(…)», rayas perdidas o duplicadas («-—», «—-»), «Órgano» con mayúscula, «1V» por «IV», «Op. Ccit.» por «op. cit.». Puntos suspensivos: «(…)»/«…» donde el original trae el carácter de elipsis, «(...)» donde trae tres puntos. Se agregaron las comillas simples de «‘representantes de los jueces’» (cons. 23), que el OCR perdió. Dos renglones con sólo «336» (encabezados mal leídos) quitados. El resto (dictamen, cons. 1-9 y 36-43 del voto que encabeza, cons. 1-10 de Petracchi y Argibay, cons. 1-2 de Zaffaroni) sin revisar |

`csjn_colegio2021` es texto nativo (`# modo: texto`). Carátula repetida en las páginas impares: patrones en `extractos/limpieza/csjn_colegio2021.txt`, anclados a la sangría profunda.

Detalle técnico: la cabecera de los `limpios/` no puede contener la cadena `[[PDF` antes de `# revisado:` ---`cabecera()` corta en el primer `[[PDF`---; por eso la línea de paginación dice «el marcador de página = …». (`extractos/limpios/csjn_elortondo1888.txt`, de otra unidad, tiene `# paginacion: [[PDF p. N]]` en la línea 6: si `revisado` va después, no se lee. No lo toqué.)

## Discrepancias con `programauba.json` y entre fuentes

- `csjn_siri1957`: el campo `note` arrastra basura de sincronización (`mlzsync1:…csjn_siri1958`). La fecha completa es 27 de diciembre de 1957 (la entrada sólo tiene el año).
- `csjn_kot1958`: el `title` es «Samuel, Kot S.R.L.» (la carátula es «Kot, Samuel S. R. L. s/ recurso de hábeas corpus»); `note` con basura de sincronización (`…csjn_cullen1893`). Fecha completa: 5 de septiembre de 1958.
- `csjn_rizzo2013`: sin fecha completa (18 de junio de 2013, confirmada en `csjn.db`, tabla `sumario`).
- `ferreyra2016` y `otegui2016` tienen la misma paginación en la entrada (871–887); ya anotado en `corpus/manifiesto.csv`.
- Ferreyra cita *Siri* como «Fallos 329:459» (nota 5); es 239:459.
- *Kot*: el ordinal de la Cámara en el impreso es «Cámara 3ª»; el OCR del tomo lo leía «3*».

## Material en la carpeta fuera del programa

- `Unidad13/CSJN_1988_Di Mascio.pdf`, `Unidad13/CSJN_2015_Uriarte c.pdf` (fallos sin citekey; *Uriarte* lo cita *Colegio de Abogados*, cons. 13 y 17).
- `Unidad13/Madison et al_2006_El Federalista No.pdf`.
- `Unidad13/Maurino - 2016 - Los procesos colectivos.pdf`.
- `Unidad13/Garantia-de-imparcialidad-y-perspectiva-de-genero.pdf`.

## Discrepancias entre notas de clase y fuentes

- Las notas (U13, «Caso Rizzo») cuentan cuatro vicios de la ley 26.855: equilibrio, representación, independencia y «demasiadas restricciones sobre la posibilidad de candidatearse». El cons. 29 del voto que encabeza enumera los cuatro primeros como equilibrio, representación, independencia y «vulnera el ejercicio de los derechos de los ciudadanos al distorsionar el proceso electoral»; las restricciones a las candidaturas (cons. 36 a 40) se tratan aparte, «sin perjuicio de lo expuesto». U13 sigue al texto.
- La tabla de las notas atribuye a la ley 26.855 «6 académicos» y a la ley 26.080 «Se excluye» al presidente de la Corte; coincide con *Rizzo* cons. 15 y *Colegio de Abogados* cons. 10 y 17. Las notas dicen que la composición de 24.937/24.939 era de 20 miembros, y *Colegio de Abogados* (cons. 17) lo confirma.
- Las notas dicen que la ley 16.986 vedaba el amparo «si existían otros recursos disponibles» y fijaba «15 días hábiles»: coincide con Ferreyra (apartado «Ley 16986»).
