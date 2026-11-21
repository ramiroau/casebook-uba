# Informe — Unidad 10 (noviembre de 2026)

## Archivos

- Escritos: `unidades/U10.md` (nueva), `respaldos/U10_agente.md` (copia), `extractos/saenz2019a.txt`, `extractos/arballo2019_art75inc13.txt` (copias de `corpus/texto/`, `# modo: texto`), `extractos/limpieza/saenz2019a.txt`, `extractos/limpieza/arballo2019_art75inc13.txt`, `notas_unidades/U10_fuentes.md`, este informe.
- No se tocaron archivos compartidos ni se corrió `build_casebook.sh`.

## Palabras

Prosa propia: unas 3.000 palabras sin los cuadros de casos (3.700 con ellos), dentro del objetivo de 3.000-4.500. No se rellenó.

## Verificación

`insertar_extractos.py --unidades U10` (salida en el scratchpad): 10 marcadores resueltos, OK. `verificar.py --unidades U10`: citekeys 6 usadas, 0 sin entrada; citas en bloque 0 (todo va por marcador); cobertura: 2 obligatorias, ambas citadas; extractos: 10 marcadores, 16.383 palabras. **OK**. Citas con `[verif. visual]`: 0 (ninguna fuente OCR).

## Extractos

| Fuente | PDF pp. | Palabras | Origen |
|---|---|---|---|
| saenz2019a (inc. 12 y derecho federal) | 3-6 | 1.833 | extracto (texto) |
| saenz2019a (legislación común) | 6-9 | 1.759 | extracto |
| saenz2019a (CCC, quiebras, jurados, aplicación) | 9-10 | 961 | extracto |
| saenz2019a (normas procesales) | 11-15 | 2.766 | extracto |
| saenz2019a (procesos colectivos) | 15-17 | 913 | extracto |
| arballo2019_art75inc13 §§ 1-2 | 1-5 | 2.144 | extracto |
| arballo2019_art75inc13 §§ 3-4 | 6-11 | 1.892 | extracto |
| arballo2019_art75inc13 §§ 5-6 | 11-15 | 1.521 | extracto |
| arballo2019_art75inc13 §§ 7-9 | 15-20 | 2.019 | extracto |
| arballo2019_art75inc13 § 10 | 20-21 | 614 | extracto |

Párrafos revisados en la salida: los encabezados subrayados de Sáenz-Sucunza quedaban pegados al primer renglón del párrafo siguiente; se corrigieron con `parrafo:`/`unir:`. Las viñetas de Arballo (§ 4) se reconstruyeron igual. Las notas al pie se descartan; las llamadas de nota pegadas al texto se quitan con patrones en `extractos/limpieza/`.

## Discrepancias y pendientes

- Clave `arballo2019`: el programa remite al comentario al art. 121; el PDF es el del art. 75 inc. 13. Se cita `[@arballo2019]` y se dice en la «Ubicación». Hace falta una entrada propia en la bibliografía.
- Fechas y tomos erróneos dentro de los comentarios (*Sandoval*, *Nucete*, *El Chocón*, *Telefónica* 1997, *Colgate*): detalle en `U10_fuentes.md`. Los cuadros de casos siguen a la base de la Corte y lo dicen debajo de cada cuadro.
- Notas de clase vs. fuentes: «delegación implícita» del derecho común (el texto la trata como atribución expresa); *Farmacity* (fuera del programa, omitido).
- No queda ningún `[PENDIENTE]`.

## Ediciones del autor

Ninguna: la unidad es nueva.

## Decisiones que el autor debería revisar

1. **Sin fallos obligatorios.** El programa pide una «aproximación a través de casos» pero no asigna fallos. La sección «La línea jurisprudencial» ordena en dos cuadros los casos que reseñan los comentarios (tomos y fechas cotejados con la base de sumarios), sin extractos de fallos, porque no integran el programa. Si se quiere una lectura directa, los candidatos naturales son *Bressani* (1937), *Transportes Vidal* (1984) y *Barillari* (2012) para el inc. 13, y *Banco del Suquía* (2002) para el inc. 12, pero agregarlos supondría sumar jurisprudencia al programa.
2. **Comentario al inc. 11 omitido.** El PDF de Sáenz-Sucunza abre con el comentario al inc. 11 (moneda), sólo de Sucunza (PDF pp. 1-3). No se reproduce porque el copete no menciona la moneda.
3. **Procesos colectivos incluidos.** El último apartado de Sáenz-Sucunza (PDF pp. 15-17) está lejos del eje de la unidad; se reproduce para que el comentario se lea completo. Se puede quitar sin afectar el resto.
4. **Competencias impositivas.** Se cubren con el § 5 de Arballo; el federalismo fiscal y la coparticipación quedan en la optativa de Orlando. Las notas de clase tienen material sobre coparticipación que la unidad no usa porque no está en las obligatorias.
5. **Tensión entre los comentarios.** En «El problema» y en la «Síntesis» se presenta como abierta una diferencia de dirección: Sáenz-Sucunza piden rediscutir la reserva provincial de los códigos procesales; Arballo advierte sobre la expansión federal. Es una lectura del autor del casebook y conviene confirmarla.
6. **Pregunta 10** vincula el optativo *GCBA c. Estado Nacional* (2021) sin describir su contenido más allá del tema; revisar si se quiere.
