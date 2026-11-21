# U18 — notas de fuentes (para integrar a FUENTES.md)

## Filas de la tabla de fuentes

| Citekey | Unidad | Carácter | PDF (en `Materiales_UBA/`) | Extracto | Modo | Paginación |
|---|---|---|---|---|---|---|
| `courtis2001` | 18 | obligatoria | `Unidad18/1_Abramovich_Courtis_2009_Apuntes sobre la exigibilidad de los deechos sociales.pdf` (28 pp) | `courtis2001.txt` (copia corregida en `limpios/`) | OCR `spa` | impresa = PDF **+971**. Capítulo XXXVII: pp. 973-998 (PDF 2-27). PDF 1 = p. 972 (final del capítulo anterior); PDF 28 = portadilla «Constitución y medio ambiente» |
| `csjn_quisbeth2012` | 18 | obligatoria | `Unidad18/2_CSJN_2012_Quisbeth Castro c.pdf` (58 pp) | `csjn_quisbeth2012.txt` | texto | citar por **voto + considerando** |
| `csjn_salas2011`, `gargarella2007a`, `holmes2015`, `csjn_benghalensis2000`, `csjn_defensor2007`, `csjn_mendoza2008` | 18 | optativas | en `Unidad18/` | — | no extraídas | sólo en «Para seguir leyendo» (y mención de una línea en «El problema») |

## Copias corregidas (`extractos/limpios/`)

| Citekey | Copia | Estado | Notas |
|---|---|---|---|
| `courtis2001` | re-OCR propio: `pdftoppm -r 400 -gray`, `magick -deskew 40% -threshold 60%`, `tesseract -l spa --psm 6`, página por página | `revisado: si` | **Capítulo completo revisado (PDF 2-27, pp. 973-998).** El OCR del corpus (`ocrmypdf`) entrelazaba renglones en PDF 4, 5, 8 y 23 y era inutilizable allí. Se quitaron encabezados, notas al pie y llamadas de nota; se corrigió con ediciones puntuales, una por error, contra la imagen (lectura de todas las páginas con Read; ampliaciones de PDF 4, 17, 19, 23). Renglones renglón por renglón como en el impreso, con guiones de corte; renglones en blanco sólo para títulos, citas en bloque e incisos i-iii; el resto de los puntos y aparte se fijó con `parrafo:` en los marcadores de U18. Rayas de inciso como «–», cursivas no conservadas. **Margen derecho cortado en el escaneo** en PDF 4 (p. 975), PDF 24 (p. 995) y, en menor medida, PDF 22 (p. 993): las letras perdidas se completaron por el contexto (p. ej. «pro-tección», «Judi-cial», «auto-motor», «que debe desarrollar», «del PIDESC», «una barrera»). La reconstrucción menos segura es «derecho de propiedad: a ello se destina» (p. 975): la puntuación tras «propiedad» no se ve; también «a sus titulares como el servicio educativo» (sin coma, p. 975). Convendría cotejarlas con otra copia del texto |

## Discrepancias con `programauba.json`

- `courtis2001`. La entrada describe Abramovich y Courtis, «Apuntes sobre la exigibilidad judicial de los derechos sociales», *Cuadernos electrónicos de filosofía del derecho* 4 (2001), `page: 4`. El PDF del compendio es otra edición: capítulo XXXVII de una obra colectiva con título corriente «Derechos sociales/Derechos colectivos», pp. 973-998, que el manifiesto del corpus fecha en 2009 (el nombre del archivo dice 2009). No se identificó la obra (la p. 972 cierra un capítulo sobre diálogo democrático y la p. 999 abre «Constitución y medio ambiente»). U18 cita con la paginación del compendio y lo advierte en la «Ubicación». Además, el orden de autores en la entrada es Courtis, Abramovich; el capítulo firma «Víctor Abramovich y Christian Courtis».
- `csjn_quisbeth2012`. La entrada dice Fallos **335:454** y fecha **2012-06-24**. La base de la CSJN (`sumario`, ids 620-628, 671, 156521) registra **Fallos 335:452**, 24 de abril de 2012; la sentencia del compendio está fechada «Buenos Aires, 24 de abril de 2012». U18 usa 335:452 y el 24 de abril en la ficha; la bibliografía sigue sin corregir. Carátula en la base: «Q.C.S.Y. c/ Gobierno de la Ciudad de Buenos Aires y otro s/ amparo».

## Estructura interna de *Quisbeth Castro* (Fallos 335:452), 24 de abril de 2012

- Voto que encabeza el pronunciamiento: cons. 1° a 17 y parte dispositiva, PDF pp. 1-31. Firmas: Lorenzetti, Highton de Nolasco, Fayt, Maqueda, Zaffaroni; Petracchi y Argibay «según su voto».
- Voto de Petracchi: PDF pp. 32-43. Remite a los cons. 1° a 7° de la mayoría; cons. 8° a 18 propios.
- Voto de Argibay: PDF pp. 45-57 (PDF 44 sin texto). Cons. 1º a 12 propios.
- PDF 58: enlace al dictamen de la Procuración (no incluido).
- Mezcla «°» (voto que encabeza, Petracchi) y «º» (Argibay, algunos de Petracchi) en los ordinales de los considerandos: las anclas los copian tal cual.

## Limpieza

- `extractos/limpieza/csjn_quisbeth2012.txt`: carátula repetida en las páginas impares («Q. 64. XLVI.», «Q. C., S. Y. c/ Gobierno de la Ciudad de Buenos», «Aires s/ amparo.»), anclada con 20 o más espacios iniciales. «RECURSO DE HECHO», «ES COPIA», «-//-» y los números de página «-N-» ya los quitan patrones existentes.

## Discrepancias entre notas de clase y fuentes (Unidad 18)

- Las notas de clase numeran esta unidad como «Unidad 19 — DESC» (y la 18 como «Propiedad»); el programa v25 la numera 18.
- Las notas presentan la «indeterminación fáctica» como segundo obstáculo de Abramovich y Courtis. En el texto es la tercera observación dentro del primer obstáculo, «La determinación de la conducta debida» (pp. 990-991); los obstáculos son cuatro: determinación de la conducta debida, autorrestricción frente a cuestiones políticas y técnicas, inadecuación de los mecanismos procesales y escasa tradición de control (pp. 987-998). U18 sigue al texto.
- Las notas atribuyen a *Quisbeth* la exigencia de un «mínimo razonable (c. 12)». La expresión no aparece en el fallo; el cons. 12 del voto que encabeza habla de una «garantía mínima del derecho fundamental» y de las «garantías mínimas indispensables». U18 usa la fórmula del fallo.
- Las notas ubican la discusión sobre recursos y planificación en el cons. 15; el argumento presupuestario está en el cons. 14 (pautas del Comité sobre el «máximo de los recursos») y la crítica a la falta de planificación coordinada al final del cons. 15. Coincide en lo sustancial.
