# U04 — informe del agente (noviembre de 2026)

## Archivos

- Escrito: `unidades/U04.md` (nuevo) y su copia `respaldos/U04_agente.md`.
- Extractos nuevos: `extractos/gargarella2009c.txt`, `extractos/elfman2019.txt`, `extractos/marbury.txt` (texto), `extractos/csjn_elortondo1888.txt` (OCR del tomo de Fallos) y `extractos/limpios/csjn_elortondo1888.txt` (`revisado: si`).
- Limpieza: `extractos/limpieza/elfman2019.txt`.
- Notas: `notas_unidades/U04_fuentes.md` (para integrar en `FUENTES.md`) y este informe.
- No se tocaron scripts, `FUENTES.md`, `README.md` ni archivos de otras unidades. No se corrió `build_casebook.sh`.

## Palabras

Prosa propia: unas 3.700 palabras (sin marcadores ni extractos, con encabezados y fichas), dentro del objetivo de 3.000-4.500. Extractos insertados: 23.299 palabras.

## Verificación

`python3 scripts/verificar.py --unidades U04` → **OK**: 8 citekeys, todas en `programauba.json`; 4 obligatorias citadas; 16 marcadores resueltos; 0 citas en bloque escritas a mano (todo el texto de las fuentes entra por marcador), de modo que ninguna lleva `[verif. visual]`. La verificación completa del casebook marca un único problema ajeno a U04 (`@klarmann`, sin entrada en la bibliografía).

## Extractos

| Fuente | Páginas del PDF | Palabras | Origen |
|---|---|---|---|
| gargarella2009c, introd. y secc. 1 | 1-3 | 1.576 | extracto |
| gargarella2009c, secc. 2 | 3-5 | 1.272 | extracto |
| gargarella2009c, secc. 3 | 5-9 | 2.198 | extracto |
| gargarella2009c, secc. 4 | 9-10 | 946 | extracto |
| gargarella2009c, secc. 5-6 | 10-14 | 2.235 | extracto |
| elfman2019, introd. y ap. I | 1-4 | 1.035 | extracto |
| elfman2019, aps. II.a-II.b | 4-10 | 1.732 | extracto |
| elfman2019, ap. II.c | 10-17 | 1.493 | extracto |
| elfman2019, ap. III | 17-21 | 1.173 | extracto |
| marbury, hechos | 1 | 211 | extracto |
| marbury, cuestiones 1 y 2 | 2-8 | 1.864 | extracto |
| marbury, cuestión 3 y decisión | 9-18 | 2.402 | extracto |
| csjn_elortondo1888, mayoría, cons. 1-17 | Fallos 184-189 (compendio 2-7) | 1.777 | limpio |
| csjn_elortondo1888, mayoría, cons. 24-27 y firmas | Fallos 193-197 (compendio 11-15) | 1.270 | limpio |
| csjn_elortondo1888, disidencia Zavalía | Fallos 197-203 (compendio 15-21) | 1.960 | limpio |
| csjn_elortondo1888, cierre de la disidencia | Fallos 211 (compendio 29) | 154 | limpio |

Las dos lecturas de doctrina y *Marbury* van completas (Elfman sin notas al pie ni bibliografía). De *Elortondo* se omiten los cons. 18-23 de la mayoría y Fallos 203-211 de la disidencia (jurisprudencia y doctrina extranjera transcripta, argumentos de equidad), resumidos en prosa.

## Discrepancias y pendientes

- Notas de clase vs. fuentes: *Sojo* como «Marbury argentino» frente a Elfman, para quien el primer caso de invalidación es *Elortondo* (ver `U04_fuentes.md`). Las notas remiten a Nino, que no está en la bibliografía v25 de la unidad.
- Bibliografía: `marbury` arrastra el `abstract` y la `note` de *Luther v. Borden*; `elfman2019` sin páginas y con título distinto del PDF. Detalle en `U04_fuentes.md`.
- No hay `[PENDIENTE]` abiertos.

## Ediciones del autor

Ninguna: la unidad es nueva.

## Decisiones para revisar

1. **Texto de *Elortondo***: se usó el OCR del tomo impreso de Fallos (csjn.db) en lugar del OCR del compendio, y se lo corrigió contra la imagen del compendio. Tres lecturas por tipo ambiguo («Constitucion», «indisputable», «tomarse») y una por tipo dañado («sujeta») se tomaron por la palabra correcta; están listadas en la cabecera de la copia limpia.
2. **Selección en *Elortondo***: mayoría cons. 1-17 y 24-27; disidencia hasta Fallos 203 y el cierre de Fallos 211. Si se quiere aligerar, el primer bloque de la mayoría podría empezar en el cons. 3.
3. **Elfman ap. III** (control de convencionalidad) se reproduce aunque el tema es de la Unidad 8, porque la lectura es obligatoria en U04 completa. Puede cortarse.
4. ***Sojo*** (optativo) se describe en prosa en la sección de jurisprudencia, con una cita breve del fallo verificada contra `corpus/texto/csjn_sojo1887.txt`, porque lo exigen Elfman y la línea histórica.
5. **Citación**: Elfman por apartado (la paginación del PDF es la del manuscrito); Gargarella por sección; *Marbury* por cuestión; la disidencia de Zavalía por página de Fallos.
6. **`marbury.txt`**: se normalizó el doble interlineado al crear el extracto (sólo espacio en blanco); está documentado en su cabecera.
7. En la ficha de *Elortondo* se mencionan los sumarios de la base de la Corte para ubicar el *holding* sobre control judicial (cons. 25) junto al de expropiación; la nota 4 conecta el estándar de deferencia con *Fayt*/*Schiffrin* (U03).
