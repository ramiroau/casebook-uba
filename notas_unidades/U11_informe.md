# U11 — informe

## Archivos

- Escritos: `unidades/U11.md` (nueva), `respaldos/U11_agente.md`, `extractos/god1991.txt`, `extractos/saenz2016b.txt`, `extractos/limpieza/god1991.txt`, `extractos/limpieza/saenz2016b.txt`, `notas_unidades/U11_fuentes.md`, este informe.
- No se tocaron archivos compartidos ni se corrió `build_casebook.sh`. Prueba con `insertar_extractos.py --salida <scratchpad>`.

## Palabras

Prosa propia: unas 2.600 palabras (con encabezados y citekeys), por debajo del objetivo de 3.000-4.500. No se rellenó: la unidad es de doctrina, sin fallos propios, y el peso está en los extractos (15.275 palabras de las fuentes).

## Verificación

`python3 scripts/verificar.py --unidades U11` → **OK**. Citekeys: 8 usadas, 0 sin entrada. Citas en bloque escritas a mano: 0 (todo va por marcador). Cobertura: 2 obligatorias, ambas citadas. Extractos: 12 marcadores resueltos. `[verif. visual]`: 0 (las dos fuentes tienen capa de texto). Las citas breves entre comillas de la prosa se cotejaron por script contra los extractos normalizados.

## Extractos

| Fuente | Páginas del PDF (impresas) | Palabras | Origen |
|---|---|---|---|
| god1991 | 1-3 (7-9) | 758 | extracto |
| god1991 | 3-6 (9-12) | 1.336 | extracto |
| god1991 | 6-9 (12-15) | 1.559 | extracto |
| god1991 | 9-11 (15-17) | 954 | extracto |
| god1991 | 12-13 (18-19) | 794 | extracto |
| god1991 | 13-16 (19-22) | 1.150 | extracto |
| saenz2016b | 1-4 (aps. 1-2) | 1.367 | extracto |
| saenz2016b | 4-7 (ap. 3) | 1.646 | extracto |
| saenz2016b | 8-12 (aps. 4 y 4.1) | 2.006 | extracto |
| saenz2016b | 12-14 (ap. 4.2) | 1.044 | extracto |
| saenz2016b | 14-18 (ap. 5) | 1.348 | extracto |
| saenz2016b | 18-21 (ap. 5) | 1.313 | extracto |

Ambos textos se reproducen casi completos, sin notas al pie. De O'Donnell faltan sólo el título, los encabezados de sección y las notas; de Sáenz, el título del ap. 1, el encabezado del ap. 4 (el tramo arranca en el primer párrafo) y las notas.

## Discrepancias y pendientes

- Discrepancias con notas de clase y con `programauba.json`: ver `U11_fuentes.md`. Las más importantes: **id `saenz2016b` duplicado** en `programauba.json` (una de las dos entradas es el comentario al art. 30), y `god1991` remite a *Novos Estudos* 1991 mientras el PDF es la traducción castellana de la versión de 1994 del *Journal of Democracy*.
- Sin `[PENDIENTE]` abiertos en el texto.

## Ediciones del autor

Ninguna (unidad nueva).

## Decisiones para revisar

1. **Sin sección de casos.** El programa de U11 no asigna fallos. Los fallos que reseña Sáenz (*Delfino*, *Mouviel*, *Peralta*, *Rodríguez*, *Verrocchi*, *Consumidores Argentinos*, *Massa*, *Cocchia*, *Colegio Público*, *Camaronera*) se leen a través del comentario y se remiten a U12. La estructura queda: El problema → dos Lecturas → Notas y preguntas → Síntesis → Para seguir leyendo.
2. **Sáenz extractado casi completo, incluidos los aps. 4 y 5 (DNU y delegación)**, que se superponen con la U12. Se eligió así porque es la lectura obligatoria y el comentario es el único lugar de la unidad donde aparece la reforma de 1994. Si se prefiere aliviar la unidad, los dos marcadores del ap. 5 y el del ap. 4.2 son los candidatos a recortar.
3. **Presidencialismo vs. parlamentarismo.** El copete lo pide, pero ninguna obligatoria lo desarrolla. La unidad lo encuadra con la nota 11 de O'Donnell (citada brevemente en prosa) y remite a las optativas, que van sólo en «Para seguir leyendo», como pide el brief.
4. **Nota 6 de Notas y preguntas** conecta la regulación de los DNU en el Núcleo de Coincidencias Básicas con la «cláusula cerrojo» de U03 [@saenz2016a]. Una versión anterior mencionaba la reelección presidencial de 1994; se quitó porque ninguna fuente de la unidad lo dice.
5. **Síntesis.** Atribuye a Sáenz cierta confianza en el control judicial y a O'Donnell escepticismo sobre el diseño. Es una lectura de los dos textos (Sáenz ap. 4.2; O'Donnell pp. 21-22); conviene revisar si es justa.
6. Paginación de O'Donnell: se cita por la impresa de la traducción (PDF + 6). La bibliografía remite a otra edición: ver discrepancia.
