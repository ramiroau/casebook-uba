# Informe — Unidad 14 (redacción nueva, noviembre de 2026)

## Archivos

- Escritos: `unidades/U14.md`, `respaldos/U14_agente.md` (copia idéntica), `extractos/alegre2020.txt`, `extractos/csjn_lee2020.txt` (copias de `corpus/texto/`, cabecera `# modo: texto`), `extractos/limpieza/alegre2020.txt`, `extractos/limpieza/csjn_lee2020.txt`, `notas_unidades/U14_fuentes.md` y este informe.
- No se tocaron archivos compartidos ni se corrió `build_casebook.sh`. Prueba: `insertar_extractos.py --unidades U14 --salida <scratchpad>`.

## Palabras

Unas 3.100 palabras de prosa propia (sin marcadores ni extractos), dentro del objetivo de 3.000 a 4.500. No se rellenó. Extractos insertados: 7.145 palabras.

## Verificación

`verificar.py --unidades U14`: **OK**. Citekeys: 4 usadas, 0 sin entrada. Citas en bloque escritas a mano: 0, y ninguna lleva `[verif. visual]`. Cobertura: 2 de 2 obligatorias. Extractos: 7 marcadores resueltos. Las citas breves en prosa (de Alegre y otros, y una de *Ibarrola*) se cotejaron con `grep` contra el texto.

## Extractos

| Fuente | PDF pp. | Palabras | Origen |
|---|---|---|---|
| alegre2020 (intro y ap. I.1) | 1–5 | 1829 | extracto |
| alegre2020 (aps. I.2 y I.3) | 5–6 | 587 | extracto |
| alegre2020 (ap. II) | 7–9 | 1023 | extracto |
| alegre2020 (ap. III) | 9–10 | 336 | extracto |
| csjn_lee2020 (cons. 1–3) | 1–9 | 1924 | extracto |
| csjn_lee2020 (cons. 4–8) | 9–13 | 777 | extracto |
| csjn_lee2020 (cons. 9–11 y parte dispositiva) | 13–16 | 669 | extracto |

Las dos obligatorias van completas: Alegre sin índice ni notas al pie, y *Lee* entero salvo la carátula y la página de partes.

## Discrepancias y pendientes

- Las discrepancias entre las notas de clase y las fuentes (*Petcoff* como decisión de fondo; *Lee* como continuidad de *Petcoff*; la «escala movediza» en el cons. 10) y las discrepancias con `programauba.json` (citas de Fallos de *Lee* 343:1704 e *Ibarrola* 344:316 faltantes; nombre invertido en *Ibarrola*; *Petcoff* 344:126 citado por *Ibarrola*) están en `U14_fuentes.md`.
- Defecto de texto conocido: en el ap. II de Alegre el extracto dice «demostrarlo-son», donde el impreso dice «demostrarlo- son». Corregirlo exigiría modificar el script o el extracto.
- No queda ningún `[PENDIENTE]`.

## Ediciones del autor

Ninguna: la unidad es nueva.

## Decisiones para revisar

1. **Notas al pie de Alegre.** El script no las inserta. Tres se resumen en prosa porque cargan contenido relevante para la unidad: nota 3 (*Verrocchi* y *Consumidores Argentinos*), nota 15 (*Granada* y los estándares de la Corte IDH sobre la suspensión de garantías) y notas 16–18 (*Arriola*, Nino y Zaffaroni). Las dos citas breves de la nota 15 no tienen marcador. Hay que decidir si conviene transcribirla como cita en bloque.
2. **Antecedentes históricos del copete.** Se cubren sólo con lo que trae el material: la reforma de 1994, la ley 26.122, la jurisprudencia citada por Alegre y la «memoria colectiva» del estado de sitio. No se agregó doctrina externa, como *Ercolano*, *Peralta* o la intervención federal que mencionan las notas. Se remite a la Unidad 12.
3. **Optativas en la línea jurisprudencial.** *Petcoff* e *Ibarrola* se describen en prosa con citekey, sin extracto, porque cierran la línea: *Ibarrola* cita *Lee* como precedente. La pregunta 9 cita textualmente el cons. 13 de *Ibarrola*, que no tiene extracto.
4. **Hechos de *Lee*.** Se extractaron completos los cons. 1 a 3 (unas 1.900 palabras), incluido el informe detallado de la provincia. Se pueden recortar con un corte interno si resultan excesivos.
5. **Puntos donde se tomó partido.** Están formulados como preguntas:
   - la nota 5 retoma la crítica de las notas de clase al análisis de proporcionalidad de *Lee* (la falta de la etapa de necesidad);
   - la nota 8 señala que la Corte no examina que la restricción se haya dispuesto por resolución de un consejo y no por ley;
   - la nota 3 plantea la objeción de que el estado de sitio podría haber sido la vía más controlada.
6. **Autoría.** La ubicación de Alegre y otros lista a los siete autores, incluido el autor del casebook, sin comentario.
