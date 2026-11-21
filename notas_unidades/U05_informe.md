# Informe — Unidad 5. Interpretación constitucional

## Archivos

- Escritos: `unidades/U05.md` (nuevo), `respaldos/U05_agente.md` (copia), `extractos/sagues2004.txt`, `extractos/gargarella2007.txt`, `extractos/scalia1988.txt`, `extractos/gargarella2009a.txt`, `extractos/gargarella2021.txt`, `extractos/limpios/gargarella2009a.txt`, `extractos/limpios/gargarella2021.txt`, `extractos/limpieza/sagues2004.txt`, `extractos/limpieza/gargarella2007.txt`, `notas_unidades/U05_fuentes.md`, este informe.
- No se tocaron archivos compartidos ni se corrió `build_casebook.sh`. Prueba con `insertar_extractos.py --salida <scratchpad>`.

## Palabras

- Prosa propia (sin marcadores): ~3.350 palabras, dentro del objetivo 3.000-4.500. No se rellenó.
- Extractos insertados: 17 marcadores, ~33.600 palabras de las fuentes.

## Verificación

`python3 scripts/verificar.py --unidades U05` → **OK**. Citekeys: 10 usadas, 0 sin entrada. Citas en bloque transcriptas a mano: 0 (todo va por marcador), por lo tanto 0 `[verif. visual]`. Cobertura: 5/5 obligatorias citadas. Extractos: 17/17 resueltos.

## Tabla de extractos

| Fuente | Páginas | Palabras | Origen |
|---|---|---|---|
| sagues2004 (secs. 1-3) | PDF 1-3 (pp. 151-153) | 641 | extracto |
| sagues2004 (secs. 4-9) | PDF 3-9 (pp. 153-159) | 2.574 | extracto |
| sagues2004 (secs. 10-14) | PDF 9-13 (pp. 159-163) | 1.475 | extracto |
| sagues2004 (sec. 15) | PDF 13-17 (pp. 163-167) | 1.604 | extracto |
| sagues2004 (secs. 16-17) | PDF 17-20 (pp. 167-170) | 1.317 | extracto |
| gargarella2007 (introducción) | PDF 1 | 329 | extracto |
| gargarella2007 (resto, sin la lista de criterios) | PDF 3-10 | 4.035 | extracto |
| scalia1988 (completo) | PDF 1-6 | 2.760 | extracto |
| gargarella2009a (I-II) | pp. 123-127 | 1.378 | limpio |
| gargarella2009a (III) | pp. 127-132 | 1.946 | limpio |
| gargarella2009a (IV) | pp. 132-137 | 2.314 | limpio |
| gargarella2009a (V) | pp. 138-141 | 1.216 | limpio |
| gargarella2009a (VI-VII) | pp. 141-148 | 2.405 | limpio |
| gargarella2021 | PDF 1-8 (pp. 211-218) | 2.685 | limpio |
| gargarella2021 | PDF 8-12 (pp. 218-222) | 1.896 | limpio |
| gargarella2021 | PDF 13-18 (pp. 223-228) | 2.325 | limpio |
| gargarella2021 | PDF 19-26 (pp. 229-236) | 2.744 | limpio |

Las cinco lecturas obligatorias quedan reproducidas completas o casi completas (sin notas al pie).

## Discrepancias notas de clase / fuentes

Detalle en `U05_fuentes.md`: el «texto dos» de las notas no discute a Sagüés; la crítica a Dworkin en el texto es el monologismo de Hércules; el ejemplo de Waldron/«la isla» es en el texto una comunidad de inmigrantes. Además, error de hecho en `gargarella2009a`, p. 138 (Warren como autor de la nota de *Carolene Products*), señalado en la unidad como agregado del editor.

## PENDIENTE abiertos

Ninguno en el texto de la unidad.

## Ediciones del autor

Unidad nueva: no había ediciones del autor.

## Decisiones de criterio para revisar

1. **Orden de lecturas**: Sagüés → Gargarella 2007 → Scalia → Gargarella 2009 → Gargarella 2021 (el programa pone Scalia último). Scalia se adelantó para que la defensa del originalismo se lea antes de las críticas de Gargarella.
2. **Sin línea jurisprudencial propia**: la unidad no tiene fallos obligatorios; el inventario de Sagüés hace de línea jurisprudencial. *Sejean* y *Rizzo* (optativos; *Rizzo* es de U13) sólo en «Para seguir leyendo». Las notas de clase usan *Rizzo* cons. 16-26 como ejemplo práctico: si se quiere, puede agregarse una pregunta con remisión a U13.
3. **Gargarella 2007**: se omite la lista con viñetas en que resume los criterios de Sagüés (PDF 1-3), redundante con la lectura anterior.
4. **Nota 11 (agregado del editor)** sobre la autoría de la nota 4 de *Carolene Products* (Stone, no Warren). Es información ajena al material, marcada como tal; el autor puede preferir quitarla.
5. **Nota 9** toma partido en primera persona («Me inclino a pensar que ese es el movimiento central de toda la unidad, aunque no estoy seguro…»). Revisar si el autor suscribe.
6. **Nota 3** propone una salida que Gargarella 2007 no examina (orden de prioridad fijado de antemano entre criterios); recoge la idea de las notas de clase («criterios léxicamente ordenados»), presentada como pregunta.
7. **Scalia**: se cita sin página (traducción re-tipeada sin paginación) y se advierte que parece abreviada.
8. **gargarella2009a**: la copia limpia usa la página impresa como marcador `[[PDF p. N]]`, a diferencia del corpus. Está documentado en la cabecera y en `U05_fuentes.md`.
9. Copete transcripto literal del programa, incluida la falta de coma en «John Hart Ely la lectura "procedimental"». Probable errata del programa.
