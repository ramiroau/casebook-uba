# Fuentes — Unidad 10 (para integrar en FUENTES.md)

## Tabla de fuentes

| Citekey | Unidad | Carácter | PDF (en `Materiales_UBA/`) | Extracto | Modo | Paginación |
|---|---|---|---|---|---|---|
| `saenz2019a` | 10 | obligatoria | `Unidad10/1_Sáenz and Sucunza - 2019 - Comentario al 75.12.pdf` (17 pp) | `saenz2019a.txt` | texto | **sin paginación impresa**. Citar por título de apartado. PDF pp. 1-3 = comentario al inc. 11 (moneda), sólo de Sucunza, no usado; el inc. 12 empieza al pie de PDF p. 3 |
| `arballo2019` (clave de extracto `arballo2019_art75inc13`) | 10 | obligatoria | `Unidad10/2_Arballo - 2019 - Comentario al 75.13.pdf` (21 pp) | `arballo2019_art75inc13.txt` | texto | **sin paginación impresa**. Citar por apartado (§ 1 a § 10) |
| `csjn_gcba2021` | 10 | optativa | `Unidad10/CSJN - 2021 - Gobierno de la Ciudad de Buenos Aires c. Estado Na.pdf` (91 pp) | — | no extraído | sólo en «Para seguir leyendo»; Fallos 344:809, 4-5-2021 confirmado en la base |
| `orlando2019` | 10 | optativa | `Unidad10/Orlando - 2019 - Federalismo Fiscal.pdf` (15 pp) | — | no extraído | sólo en «Para seguir leyendo» |
| `gelli2004`, `bidegain1998` | 10 | optativas | sin PDF | — | — | sólo en «Para seguir leyendo» |

Los dos extractos se copiaron de `corpus/texto/` (nivel A) con `# modo: texto`.
Se usan prácticamente completos: `saenz2019a` PDF pp. 3-17; `arballo2019_art75inc13` PDF pp. 1-21.

## Limpieza (`extractos/limpieza/`)

- `saenz2019a.txt`: 20 llamadas de nota pegadas a comillas de cierre, a «CN» o a puntos (patrones con el contexto exacto, uno por llamada); la llamada 17 pegada a «Ley N° 346» (PDF p. 4); y los dos renglones de continuación de la nota 7 que quedan al pie de PDF p. 3 antes del primer renglón numerado.
- `arballo2019_art75inc13.txt`: 64 llamadas de nota pegadas a comillas, puntos, años («de 18243», «de 199511») y signos («1964!6»). Patrones generados con contexto exacto (lookbehind de hasta diez caracteres y lookahead de tres).

## Discrepancias con `programauba.json`

- `arballo2019`: la entrada es el «Comentario al artículo 121» (Unidad 7). El PDF de la Unidad 10 es el comentario de Arballo al **art. 75 inc. 13**. Se cita `[@arballo2019]` para que cierre la cobertura y se extracta con la clave `arballo2019_art75inc13`. Hace falta una entrada propia (p. ej. `arballo2019b`, «Comentario al artículo 75 inc. 13»).
- `saenz2019a`: el campo `citation-key` dice `saenz2019` (distinto del `id`) y la entrada no registra páginas. Sucunza figura como coautor; el comentario al inc. 11 que trae el mismo PDF es sólo suyo.

## Erratas y discrepancias dentro de las fuentes (no corregidas; los extractos las reproducen)

Cotejadas con la base de sumarios de la CSJN (`observatorio-csjn/data/csjn.db`, tabla `sumario`):

- `saenz2019a`, nota 43: *Sandoval c. Neuquén* citado como Fallos 256:215 (1997); la base lo ubica en **Fallos 320:1344** (8-7-1997).
- `arballo2019_art75inc13`, § 4: *Nucete* fechado «de 2009» en el cuerpo; la nota y la base dan **Fallos 335:1222, 2012**.
- § 5: *Hidroeléctrica El Chocón* fechado «de 1999»; Fallos 320:1302 es de **1997**.
- § 9: los casos de *Telefónica* c. General Pico (320:162) y c. Chascomús (320:619) se presentan como «binomios jurisprudenciales del año 1998»; son de **1997**. Los de *Operadora* (321:658 y 321:1052) sí son de 1998.
- Nota 32: *Colgate Palmolive* citado como Fallos 336:3351 (2013); la nota 29 y la base dan **326:3351 (2003)**. El § 4 repite además el renglón de *Colgate* como viñeta separada.
- § 4 (*Dodero Viajes*): «la regla de supremacía del art. 30 de la Constitución Nacional»; la supremacía está en el art. 31. Posible errata del original; no se corrigió ni se comenta en la unidad.
- § 4 (*Barillari*): «Constituci6n», «econ6mico», «circulaci6n», «raz6n» están así en el PDF (verificado visualmente, PDF p. 11).
- § 5: «territorial”..46» (doble punto) está en el original.
- Erratas de la capa de texto de `saenz2019a` («derecho federalsólo», «localy», «CSJNque», «loscuales», «podríasustentarse», «exponeDulitzky») son palabras pegadas del PDF; se reproducen tal cual.

## Discrepancias entre notas de clase y fuentes (Unidad 10)

- Las notas dicen que el derecho común «es una delegación implícita de las provincias». Sáenz y Sucunza lo tratan como una atribución expresa del inc. 12 («Las provincias no ejercen el poder delegado a la Nación…»). U10 sigue al texto y no usa «implícita».
- Las notas mencionan *Farmacity* como caso pendiente; no está en ninguna lectura del programa y no se incluyó.
- Las notas citan páginas del compendio (pp. 330, 338, 354); el casebook cita por apartado porque los PDFs no tienen paginación impresa.
