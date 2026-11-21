# Fuentes — Unidad 5 (para integrar en FUENTES.md)

## Tabla de fuentes

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

## Copias corregidas (`extractos/limpios/`)

| Citekey | Copia | Estado | Notas |
|---|---|---|---|
| `gargarella2009a` | combinación de tres OCR corregida contra la imagen | `revisado: si` | **Capítulo completo revisado (pp. 123-148).** El escaneo del compendio está torcido y el OCR del corpus entrelaza columnas en pp. 126, 128-129, 133, 135, 137-138, 141, 146, 148. Se re-OCR-izó (tesseract spa, 300 dpi, `--psm 3` y `--psm 6`) la **otra copia** de la carpeta, `Gargarella_2009_La dificultosa tarea de la interpretación constitucional2.pdf` (una página por hoja, 28 pp; su capa de texto es letra espaciada inservible), y para cada página se eligió la mejor de las tres fuentes (corpus o re-OCR) y se corrigió contra la imagen de esa copia. En esa copia pp. 132 y 138 están cortadas a la derecha: se tomaron del compendio; la mitad inferior de p. 138 se transcribió de la imagen (los finales de renglón se leen en el margen de p. 139). Sin notas al pie ni llamadas; rayas de inciso como `–`. Erratas del impreso conservadas: «Frankfruter», «qué es lo el derecho da» (p. 126), «especiamente» (p. 148), «alegar?.» (p. 131). **Atención: aquí `[[PDF p. N]]` = página impresa**, distinto de `corpus/texto/gargarella2009a.txt` |
| `gargarella2021` | OCR del corpus corregido | `revisado: si` | **PDF 1-26 revisadas (pp. 211-236, todo el capítulo).** OCR bueno; correcciones puntuales (p. ej. «oniginalistas», «eran fragilidad», «sistemajudicial», rayas como guiones, renglones en blanco espurios, «* * *» de p. 217). PDF 24 (p. 234) re-transcripta: el OCR partía renglones. Sin notas al pie ni llamadas; encabezados en mayúsculas como párrafo propio. Se conservan «intepretativa» (título) y «preminencia» (p. 223) |

## Limpieza agregada (`extractos/limpieza/`)

- `sagues2004.txt`: folios y encabezados («151», «152 • Néstor Pedro Sagüés», «Interpretación constitucional y alquimia constitucional • 153»); notas 1, 2-3, 4, 5, 6-8 y 9 (empiezan con el número sangrado, sin renglón propio); llamadas 1-9 pegadas a puntuación.
- `gargarella2007.txt`: llamadas 1, 2, 5 y 6 pegadas a punto o paréntesis; continuación de la nota 3 al pie de PDF p. 2.

## Discrepancias con `programauba.json`

- `scalia1988`: la entrada cita el original inglés (57 U. Cin. L. Rev. 849). El compendio trae una traducción castellana sin datos de traductor ni paginación, que parece **abreviada** (remite a una cita de Tribe que no figura). Convendría registrar la traducción o anotar la entrada.
- `gargarella2009a`: la entrada da pp. 173-231 y `note: saldivia09`; el capítulo del compendio ocupa **pp. 123-148** del t. I. La paginación de la entrada no corresponde (el manifiesto del corpus ya señala que esas páginas se copiaron también a `gargarella2009e`).
- `gargarella2007`: la entrada da *Jurisprudencia Argentina* 2007-II, pp. 3-10; el PDF es un original de autor sin esa paginación, y su nota 1 cita a Sagüés como «Interpretación constitucional y alquimia **interpretativa**», Lexis Nexis (2004).
- `gargarella2021`: la entrada (libro) no registra capítulo ni páginas; el compendio trae el cap. 14, pp. 211-236.
- `fiss2008`: figura en el programa como optativa pero **no existe en `programauba.json`** y no hay PDF.
- `ely1997`: publisher «Silgo del Hombre» (errata por «Siglo del Hombre»).

## Material de la carpeta fuera del programa

- `Unidad5/Gargarella_2019_El preámbulo.pdf` — sin citekey; listado en «Para seguir leyendo» como ajeno al programa.
- `Unidad5/Gargarella_2009_La dificultosa tarea de la interpretación constitucional2.pdf` — segunda copia de `gargarella2009a`, usada para la corrección.

## Discrepancias entre notas de clase y fuentes (Unidad 5)

- Las notas presentan un «texto dos» de Gargarella que «valora el esfuerzo de Sagüés pero lo cuestiona» y luego analiza originalismo, Dworkin, Ely y Waldron. El texto que discute a Sagüés es `gargarella2007`; el que recorre esas teorías (`gargarella2009a`) no menciona a Sagüés.
- Las notas dicen que Dworkin fracasa por no poder abordar «el hecho del desacuerdo». En `gargarella2009a` (pp. 136-137) la crítica a Dworkin es el carácter monológico de Hércules (Michelman, Nino); el «hecho del desacuerdo» aparece en la sección sobre Waldron y en `gargarella2021`, p. 229.
- Las notas remiten a Waldron con «el ejemplo de la isla». En `gargarella2021` el ejemplo es la comunidad de inmigrantes que llega a su «tierra prometida» (cap. 2 del libro, retomado en pp. 230-231).
- Error de hecho en la fuente (no en las notas): `gargarella2009a`, p. 138, atribuye la nota 4 de *Carolene Products* (1938) a Earl Warren como presidente de la Corte. La unidad lo señala como agregado del editor (nota 11).
