# Informe — Unidad 9 (noviembre de 2026)

## Archivos

- Escritos: `unidades/U09.md` (nuevo), `respaldos/U09_agente.md` (copia),
  `extractos/rau2019.txt`, `extractos/guidi2019.txt`,
  `extractos/csjn_famyl2000.txt` (copias de `corpus/texto/`, `# modo: texto`),
  `extractos/limpieza/rau2019.txt`, `extractos/limpieza/guidi2019.txt`,
  `notas_unidades/U09_fuentes.md`, este informe.
- No se tocaron archivos compartidos ni se corrió `build_casebook.sh`.

## Palabras

Prosa propia (sin marcadores): unas 3.650, dentro del objetivo de
3.000-4.500. Extractos insertados: 22.500 palabras.

## Verificación

`insertar_extractos.py --unidades U09`: 16 marcadores resueltos, OK.
`verificar.py --unidades U09`: OK (9 claves, 0 sin entrada; 3/3 obligatorias
citadas; 16 marcadores). Citas en bloque escritas a mano: ninguna; las citas
breves entre comillas de la prosa se cotejaron contra los extractos
(normalizadas). `[verif. visual]`: 0 (no hay fuentes OCR).
La verificación global da 2 problemas ajenos a U09 (`@klarmann`, marcador
de U12 sobre `csjn_delfino1927`); los patrones de limpieza de U09 no
coinciden con ninguna otra fuente.

## Extractos

| Fuente | Tramo | PDF pp. | Palabras | Origen |
|---|---|---|---|---|
| guidi2019 | intr. y ap. 1 | 1-5 | 1.783 | extracto |
| guidi2019 | ap. 2 | 5-7 | 745 | extracto |
| guidi2019 | aps. 3.1-3.3 | 7-10 | 1.750 | extracto |
| guidi2019 | aps. 3.4-3.5 | 10-13 | 1.302 | extracto |
| guidi2019 | ap. 4 | 13-15 | 1.007 | extracto |
| rau2019 | intr. y ap. I | 1-3 | 1.108 | extracto |
| rau2019 | aps. II-III | 3-9 | 2.570 | extracto |
| rau2019 | aps. IV-V | 9-12 | 1.537 | extracto |
| rau2019 | aps. VI-VIII | 12-15 | 1.795 | extracto |
| rau2019 | ap. X | 22-23 | 662 | extracto |
| rau2019 | aps. IX.1-IX.2 | 15-17 | 1.328 | extracto |
| csjn_famyl2000 | mayoría, cons. 10-16 | 3-5 | 1.558 | extracto |
| csjn_famyl2000 | mayoría, cons. 17-19 y dispositiva | 5-6 | 817 | extracto |
| csjn_famyl2000 | Petracchi, cons. 6 | 12-13 | 409 | extracto |
| csjn_famyl2000 | Vázquez, cons. 11-19 y dispositiva | 16-19 | 1.671 | extracto |
| rau2019 | aps. IX.3-IX.5 | 18-22 | 2.470 | extracto |

Los dos comentarios se reproducen completos (sin notas al pie).

## Discrepancias y pendientes

- Notas de clase vs. fuentes: art. 76 por art. 80 en *Famyl*; «uno cada
  treinta mil» por treinta y tres mil (art. 45); «Collella» por «Colella»;
  «Borocotó» como nombre de la causa «Pagani»; el test del art. 80 en la
  mayoría se enuncia en el cons. 12 (las notas dicen 13). Detalle en
  `U09_fuentes.md`.
- Dentro de las fuentes: el ap. IX.2 del comentario dice que la Corte
  confirmó la inconstitucionalidad de los artículos del decreto «que
  observaban esta alícuota especial», mientras que el cons. 19 de la mayoría
  dice que el veto del inc. m fue válido. No se resolvió: va como nota 8.
- `programauba.json`: `rau2019` duplicado con una entrada errónea
  («Comentario al artículo 32», pp. 1004-1016); `guidi2019` duplicado;
  `note` basura en `csjn_famyl2000`.
- Sin `[PENDIENTE]` en el texto. Hueco de contenido: el copete incluye el
  juicio político y la remoción de magistrados, pero la única lectura
  específica (`pearce2019`) es optativa y no tiene PDF. La unidad lo dice en
  «El problema» y remite a las menciones de paso de Guidi y del comentario.

## Ediciones del autor

Unidad nueva: no había ediciones del autor que conservar.

## Decisiones de criterio para revisar

1. El ap. IX de «La actividad del Congreso» se sacó de la lectura y se partió
   alrededor del caso: IX.1-IX.2 antes de *Famyl* (línea jurisprudencial),
   IX.3-IX.5 después (sección «Después de *Famyl*»). El ap. X se lee antes del
   IX.
2. *Famyl*: no se extractaron los cons. 1-9 de la mayoría (hechos y
   admisibilidad; resumidos en la ficha), el voto de Nazareno (idéntico salvo
   la omisión del cons. 10, señalada en la ficha) ni los cons. 1-10 de
   Vázquez. De Petracchi sólo el cons. 6.
3. *Bussi* (optativo) se describe en un párrafo a través de Guidi, ap. 4,
   con citekey y sin extracto.
4. `rau2019` es coautoría del autor del casebook. La prosa lo trata como
   cualquier otra fuente («los autores», «el comentario») y marca dónde toma
   posición; conviene que el autor revise si quiere otro tratamiento (p. ej.
   primera persona).
5. El holding de *Famyl* se formuló con los cons. 13, 15 y 19 y los sumarios
   39099 y 39102 de la base.
6. Las preguntas 2, 5 y 6 toman posiciones de Guidi y del comentario (control
   judicial «especialmente riguroso», principio deliberativo, unidad política)
   y las ponen en tensión con otros pasajes de los mismos textos; no se
   resuelven.
