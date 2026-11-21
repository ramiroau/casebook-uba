# Fuentes — Unidad 17 (para integrar en FUENTES.md)

## Tabla de fuentes

| Citekey | Unidad | Carácter | PDF (en `Materiales_UBA/`) | Extracto | Modo | Paginación |
|---|---|---|---|---|---|---|
| `elias2014a` | 17 | obligatoria | `Unidad17/1_Elías_2014_El derecho de propiedad en la Constitución argentina.pdf` (14 hojas, doble página) | `elias2014a.txt` | OCR (copia corregida en `limpios/`) | cada hoja lleva dos marcadores `[[PDF p. n]]` (izq., der.); impresa = **2n+683** (izq.) / **2n+684** (der.); hoja 1: izq. en blanco, der. = p. 685. Capítulo: pp. 685-711 |
| `csjn_ercolano1922` | 17 | obligatoria | `Unidad17/2_CSJN - 1922 - Ercolano c. Lanteri de Renshaw.pdf` (17 hojas, doble página) | `csjn_ercolano1922.txt` | OCR del tomo impreso de Fallos (csjn.db, `vol_page`, vol_id 136), copia corregida en `limpios/` | `[[PDF p. N]]` = **página impresa de Fallos 136**. Citar la mayoría por página de Fallos (no numera considerandos) y la disidencia por considerando |
| `csjn_coihue2021` | 17 | optativa | `Unidad17/CSJN - 2021 - Coihue S.R.L. c Santa Cruz...pdf` (90 pp) | — | no extraído | sólo en «Para seguir leyendo» |
| `sola2010a` | 17 | optativa | `Unidad17/Sola - 2010 - Manual de Derecho Constitucional (extracto).pdf` | — | no extraído | sólo en «Para seguir leyendo» |
| `zeberio2006` | 17 | optativa | `Unidad17/Zeberio - 2006 - Los hombres y las cosas...pdf` | — | no extraído | sólo en «Para seguir leyendo» |
| `saenz2019` | 17 | optativa | `Unidad17/Sáenz - 2016 - El derecho de propiedad. Control de razonabilidad .pdf` | — | no extraído | sólo en «Para seguir leyendo» |
| `csjn_avico1934` | 17 | optativa | sin PDF en la carpeta | — | — | sólo en «Para seguir leyendo» |

## Copias corregidas (`extractos/limpios/`)

| Citekey | Copia | Estado | Notas |
|---|---|---|---|
| `elias2014a` | transcripción revisada renglón por renglón contra la imagen (corpus/pdf/elias2014a.pdf, 300 dpi, enderezada con `magick -deskew`), a partir de un re-OCR por mitad de hoja (tesseract `--psm 6`, recorte de márgenes por coordenadas) | `revisado: si` | **Capítulo completo, pp. 685-711.** El OCR del corpus (`corpus/texto/elias2014a.txt`) entrelaza las columnas en las mitades izquierdas y es inservible; el re-OCR de una mitad por vez sale casi limpio. Sin notas al pie, llamadas de nota ni encabezados; punto y aparte = renglón en blanco; cursivas y versalitas no conservadas. Erratas del impreso conservadas: «susceptibles regulación», «estaría sujetos», «puede imponer» (por «pueden»), «por dar mencionar», «en la que la no funciona», «en relación el producto». La cita de Cianciardo y Zambrano (p. 692), en bloque en el impreso, queda como párrafo |
| `csjn_ercolano1922` | OCR del tomo impreso de Fallos (`scripts/fallo_db.py 136 160 --hasta 194`), transcripto contra la imagen del compendio (corpus/pdf/csjn_ercolano1922.pdf, hojas 10-33, que reproduce el mismo tomo) | `revisado: si` | **Fallos 136:170-193 completas** (mayoría y disidencia de Bermejo). Sumarios, sentencia de primera instancia y dictamen (pp. 160-169) no se incluyen. Erratas del impreso conservadas: «ultrepasados» (cons. 14), «Block v. Hirsth» (cons. 11), «Munn v. Yllinois» (cons. 27), «Granger Caces», «sic utere tuó ut alienum non ledas» (cons. 21), «dá», «incluído», «perfectamente innocua», «cumplimento» (cons. 23). Las comillas repetidas al comienzo de cada renglón de las citas largas, uso tipográfico de la época, se suprimieron |

Los extractos crudos (`extractos/elias2014a.txt`, `extractos/csjn_ercolano1922.txt`) son copias del OCR con `# modo: ocr`; se quitaron mecánicamente los renglones que contienen sólo un número (documentado en la cabecera). No hizo falta ningún patrón de `extractos/limpieza/`.

## Discrepancias con `programauba.json`

- `csjn_avico1934`: la entrada dice `volume: 248, page: 21`. La base de la CSJN (sumarios y `vol_start`) ubica *Avico, Oscar Agustín c/ de la Pesa, Saúl G.* en **Fallos 172:21** (1934), que es también la cita de Elías (n. 7 y 41). Corregir el tomo.
- `csjn_ercolano1922`: la entrada (136:161) coincide con la base; `vol_start` registra el encabezado del caso en 136:160 (comienzo de los sumarios). El fallo de la Corte está en 136:170-179 y la disidencia en 136:180-193. Elías cita «Fallos 136:170» (n. 40 y 45). La carátula de la base agrupa tres causas (Ercolano c/ Lanteri Renshaw; Cooke c/ Naveira; Urrutia c/ Dellepiane).
- `elias2014a`: la entrada no registra páginas (pp. 685-711) ni el título completo del capítulo («El derecho de propiedad en la Constitución Nacional: una introducción teórica»). El campo `editor` duplica a Elías como autor y editor (correcto: es uno de los directores del *Tratado*).
- `saenz2019`: el PDF de la carpeta está fechado 2016 («El derecho de propiedad. Control de razonabilidad»); ya anotado en `corpus/manifiesto.csv`. No se usó.

## Discrepancias entre notas de clase y fuentes

- Las notas numeran la unidad como «Unidad 18 --- Propiedad»; en el programa v25 es la 17.
- Las notas ubican en «p. 706» el pasaje en que Elías identifica el pluralismo en la jurisprudencia de la Corte; en el impreso está en p. 707 (sección III).
- Las notas atribuyen a Elías tres problemas de que «el contenido patrimonial exige un control judicial menos intenso». En el texto, los tres problemas «macro» (pérdida de valor de la Constitución, legitimidad sociológica del Poder Judicial, efectos sobre el desarrollo) se derivan de relegar la propiedad a un derecho «de segunda categoría» (pp. 710-711); la crítica a la fórmula del control menos intenso es un párrafo previo (p. 709). U17 sigue al texto.
- Las notas resumen el test de *Ercolano* como «fin legítimo; no se afecta la sustancia; razonable en su extensión proporcionada y temporal». El fallo habla de la «naturaleza, las causas determinantes y la extensión de la medida restrictiva» y del límite del precio arbitrario o confiscatorio (Fallos 136:177-178); la fórmula de la «sustancia» no aparece. U17 sigue al texto.

## Otras observaciones

- Gargarella (`gargarella2021`, Unidad 5, p. 222) atribuye a la Corte presidida por Bermejo haber declarado inconstitucionales los controles de precios de alquileres; en *Ercolano* la mayoría los convalidó y Bermejo quedó en disidencia. El mismo párrafo registra luego el giro de *Ercolano* y la vuelta en *Mango* (1925). U17 cita a Gargarella sólo para la secuencia y para la presidencia de Bermejo.
- La nota 71 de Elías cita *Fayt* como Fallos 322:1616, en línea con lo anotado en FUENTES.md para `csjn_fayt1999`.
