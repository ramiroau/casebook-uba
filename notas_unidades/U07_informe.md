# Informe U07 — Federalismo y régimen municipal (noviembre de 2026)

## Archivos

- Escritos: `unidades/U07.md` (nueva), `respaldos/U07_agente.md` (copia).
- Extractos nuevos: `extractos/jgb2008.txt` y `extractos/mendez2021.txt` (re-extraídos del PDF con PyMuPDF; el texto de `corpus/` no era insertable), `extractos/csjn_evolucion2023.txt` y `extractos/csjn_confederacion2024.txt` (copias de `corpus/texto/` con `# modo: texto`).
- Limpieza: `extractos/limpieza/csjn_evolucion2023.txt`, `extractos/limpieza/csjn_confederacion2024.txt`.
- Notas: `notas_unidades/U07_fuentes.md`, este informe, y `notas_unidades/U07_gen_extractos.py` (script de re-extracción, para reproducibilidad).
- No se tocaron archivos compartidos ni se corrió `build_casebook.sh`.

## Palabras

Prosa propia (sin marcadores): unas 3.900 palabras, incluidos títulos, fichas y bibliografía, frente al objetivo de 3.000-4.500. Extractos insertados: 30.708 palabras de las fuentes.

## Verificación

`python3 scripts/insertar_extractos.py --unidades U07` (salida en el scratchpad) y `python3 scripts/verificar.py --unidades U07`: **OK**.
- citekeys: 16 usadas, 0 sin entrada.
- citas en bloque: 0 (todo el texto de las fuentes va por marcador).
- cobertura: 4 obligatorias, todas citadas.
- extractos: 22 marcadores resueltos.
- `[verif. visual]`: 0 (ninguna fuente OCR).

## Extractos

| Fuente | PDF pp. | Palabras | Origen |
|---|---|---|---|
| `jgb2008` secs. 1-2 | 1-5 | 1.137 | extracto (re-extraído) |
| `jgb2008` sec. 3 | 5-13 | 1.997 | extracto |
| `jgb2008` sec. 4 | 13-24 | 2.481 | extracto |
| `jgb2008` sec. 5 (representación) | 24-32 | 2.068 | extracto |
| `jgb2008` sec. 5 (federalismo fiscal, 2 tramos) | 32-36 | 658 | extracto |
| `jgb2008` sec. 5 (otros estándares) y 6 | 36-43 | 1.737 | extracto |
| `mendez2021` I-II | 1-3 | 1.138 | extracto (re-extraído) |
| `mendez2021` III | 3-10 | 4.638 | extracto |
| `mendez2021` IV | 10-12 | 1.581 | extracto |
| `mendez2021` V-VI | 12-14 | 1.502 | extracto |
| *Evolución Liberal*, Rosatti y Maqueda, cons. 4-9 | 5-14 | 2.119 | extracto |
| ídem, cons. 11-12 y dispositiva | 15-17 | 412 | extracto |
| ídem, Rosenkrantz, cons. 5-12 | 24-31 | 1.623 | extracto |
| ídem, Rosenkrantz, cons. 14 | 36-39 | 607 | extracto |
| ídem, Rosenkrantz, cons. 17-18 | 44-47 | 696 | extracto |
| ídem, Rosenkrantz, cons. 20 y dispositiva | 49-50 | 355 | extracto |
| *Formosa*, Rosatti y Maqueda, cons. 5-13 | 11-19 | 2.238 | extracto |
| ídem, cons. 14-15 y dispositiva | 20 | 239 | extracto |
| ídem, Rosenkrantz, cons. 10-11 | 34-38 | 1.328 | extracto |
| ídem, Rosenkrantz, cons. 13 y dispositiva | 40-41 | 346 | extracto |
| ídem, Lorenzetti, cons. 3-6 | 43-48 | 1.480 | extracto |
| ídem, Lorenzetti, cons. 16 | 55-56 | 328 | extracto |

Párrafos revisados en la salida: se corrigieron con `unir`/`parrafo` los cortes espurios después de «Fallos:» y «"D.», un corte de página en el voto de Rosenkrantz en *Evolución* (cons. 5) y uno en el de Lorenzetti en *Formosa* (cons. 5). En JGB y Méndez los puntos y aparte vienen de la geometría del PDF (espacio vertical y sangría), con un `unir` en JGB p. 35.

## Discrepancias y pendientes

- Notas de clase vs. fuentes: ver `U07_fuentes.md` («máxima prudencia» es de *Santa Cruz* en el artículo, no de *Santiago*; «bajo costo» es de Gibson y Calvo en JGB, no de Gervasoni). Ninguna afecta al texto.
- Discrepancias con `programauba.json`: expediente y título de `csjn_confederacion2024` (922/2023, «Formoseño»), entrada duplicada de `csjn_evolucion2023`, `csjn_ucr2013` apunta a la cautelar (336:1756) y no al fondo (336:2148), optativas sin Fallos ni PDF, *Río Negro* (342:287) sin citekey.
- Errores de las fuentes conservados: notas 2-4 de Méndez con citas de Fallos erradas (no se reproducen); «art. 5º de la Constitución provincial» en Méndez p. 57.
- `[PENDIENTE]` abiertos: ninguno.
- El extracto de JGB y el de Méndez dependen de la re-extracción: si se regenera `corpus/` y alguien vuelve a copiar `corpus/texto/` a `extractos/`, los marcadores fallarán.

## Ediciones del autor

Unidad nueva: no había ediciones del autor que conservar ni marcadores `AUTOR`.

## Decisiones de criterio a revisar

1. **Extensión.** JGB se reproduce casi completo (pp. 1-43 sin notas ni cuadro) y Méndez completo. Las notas al pie de JGB son extensas y a veces sustantivas (p. ej. n. 51 sobre el art. 31 y el control judicial, n. 92 sobre las reformas de 1994 y el art. 124); quedan fuera y se remite al compendio. Si la unidad resulta larga, el primer candidato a recorte es el tramo sobre Estados Unidos (pp. 15-18) o la sección «Otros estándares».
2. **Art. 124 y régimen municipal.** El copete menciona el art. 124 y el título el régimen municipal, pero las lecturas obligatorias casi no los tratan (JGB sólo en nota 92). No agregué doctrina externa; lo dejé como pregunta (nota 3) y remití a las optativas (*Shi*, *Esso*, *Farmacity*, Arballo, Azrak).
3. **Selección de considerandos.** En *Evolución* se omiten los cons. 1-3 y 10 del voto de Rosatti y Maqueda (antecedentes y Linares Quintana) y, del voto de Rosenkrantz, los cons. 1-4 (antecedentes), 13 (historia de la reelección: Gorostiaga, Alberdi, convención de 1994), 15-16 (ventaja electoral, Jefferson y la Enmienda XXII) y 19 (equiparación de gobernador y vicegobernador). En *Formosa* se omiten los «Resulta», los cons. 1-4 de Rosatti y Maqueda (competencia y reseña de la línea, ya leída en *Evolución*), la enumeración de precedentes sobre margen de apreciación del cons. 13, los cons. 1-9 y 12 de Rosenkrantz (remiten a *Evolución*) y los cons. 1-2 y 7-15 de Lorenzetti (el cons. 16 los resume). El cons. 13 de Rosenkrantz en *Evolución* es un buen candidato a agregar si se quiere más historia constitucional.
4. **Títulos de voto.** Los dos fallos se componen de votos concurrentes, sin un voto suscripto por tres jueces; los titulé «Voto de los jueces Rosatti y Maqueda» (el que encabeza) y lo dije en la ficha. Los sumarios de la base CSJN atribuyen esos pasajes a «voto de los jueces Rosatti y Maqueda».
5. **Holding de *Formosa*.** Lo formulé sobre los votos de Rosatti-Maqueda y Lorenzetti, que coinciden en declarar inconstitucional la norma. Rosenkrantz concurre con un alcance distinto (aplicación al caso, mandato en curso salvado), lo que dejé en la ficha y en la nota 7. Conviene revisar si se quiere presentar el *holding* como común a los tres votos.
6. **Línea jurisprudencial.** *Río Negro* (2019) no está en el programa; se describe en prosa con apoyo en la reseña de los fallos obligatorios y de Méndez, sin extracto ni citekey propia.
7. **«Estado actual».** La síntesis presenta *Formosa* como estado actual de la cuestión. Es una apreciación descriptiva; el programa no dice nada al respecto.
