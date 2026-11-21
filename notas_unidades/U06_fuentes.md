# Fuentes — Unidad 6 (para integrar en `FUENTES.md`)

## Tabla de fuentes

| Citekey | Unidad | Carácter | PDF (en `Materiales_UBA/`) | Extracto | Modo | Paginación |
|---|---|---|---|---|---|---|
| `saenz2016b` (clave de extracto `saenz2016_art14y28`) | 6 | obligatoria | `Unidad6/1_Saenz 2016.pdf` (11 pp) | `saenz2016_art14y28.txt` | texto | **sin paginación impresa**. Citar por apartado (introducción, aps. 1, 2, 3.1, 3.2, 3.3; notas al pie como «n. N») |
| `bouzat2013` | 6 | obligatoria | `Unidad6/2_Bouzat_2013_El principio de razonabilidad como límite sustantivo a las atribuciones del.pdf` (13 pp) | `bouzat2013.txt` | texto | **sin paginación impresa** (manuscrito Word). Citar por sección romana (I-VII). El original numera dos secciones consecutivas como «III» |
| `csjn_clarin2013` | 6 | optativa | `Unidad6/CSJN_2013_Grupo Clarín S.pdf` (392 pp, escaneo) | — | no extraído | sólo ficha en prosa (vía Bouzat) y «Para seguir leyendo» |
| `maurino2011` | 6 | optativa | `Unidad6/Maurino_2011_El artículo 28 de la Constitución.pdf` | — | no extraído | sólo «Para seguir leyendo» |

## Extractos creados

- `extractos/saenz2016_art14y28.txt`: copia de `corpus/texto/saenz2016_art14y28.txt` con `# modo: texto`. **Única edición**: en PDF p. 1 la llamada de nota 1 (tras «poder de policía del Estado”») ocupaba un renglón propio; `NOTA_AL_PIE` la tomaba como comienzo de las notas y cortaba la página. Se quitó el renglón y se unió «”: la potestad». Documentado en la cabecera.
- `extractos/bouzat2013.txt`: copia sin cambios de `corpus/texto/bouzat2013.txt` con `# modo: texto`.

## Limpieza agregada

- `extractos/limpieza/saenz2016_art14y28.txt`: llamadas de nota pegadas a comillas de cierre («”») o a un punto, que `MARCA_DE_NOTA` no reconoce (notas 2, 15, 24, 25, 27, 28, 32, 36, 38, 39, 40, 43, 44, 46). Cada patrón anclado con el texto vecino.
- `extractos/limpieza/bouzat2013.txt`: ídem, notas 8 a 18 de la sec. VI (tras «“Hileret”», «“Canale”», etc.).

## Rarezas del original conservadas

- Sáenz, PDF p. 11: «(t) cuando se impugna» por «(i)» y «“Hooft» sin comillas de cierre; verificado contra la imagen, están en el PDF.
- Sáenz, PDF p. 1: «los todos los habitantes». PDF p. 8: «parte de de una ley», «autorizada» por «autorizaba».
- Bouzat: «Higthon de Nolasco» (sec. VI), «aparto coactivo» (sec. V), «la ley que cuya constitucionalidad» (sec. III), dos secciones «III».

## Discrepancias con `programauba.json`

- `saenz2016b`: la entrada (y la de U11) es «Facultades normativas del poder ejecutivo». El PDF asignado en U06 es «Artículos 14 y 28: Poder de policía o poder de “reglamentar” los derechos. Sus límites». Se citó `[@saenz2016b]` para que cierre la cobertura, según el BRIEF. Hace falta una entrada propia (p. ej. `saenz2016c`) y cambiar la clave en el programa. Además, `programauba.json` tiene **dos entradas con id `saenz2016b`** (una con el título del art. 30, pp. 78-90, y otra con «Facultades normativas»): conviene depurarlo.
- `bouzat2013`: tipo `manuscript`, fecha `circa`. Los metadatos del PDF dan creación el 17/8/2016; el texto cita *Clarín* (2013) y *ADEBA*, posteriores a 2013. El año probablemente es aproximado.
- `csjn_avico1934` (U17, no es de esta unidad): la entrada dice Fallos 248:21; Bouzat cita Fallos 172:21 (n. 11). Verificar.

## Discrepancias entre las lecturas

- *Hileret*: Bouzat lo cita como Fallos 98:20 (n. 8) y Sáenz como Fallos 98:51 (n. 30). Las descripciones de la ley también difieren (indemnizar a cañeros que destruían plantíos, según Bouzat; deprimir la oferta para subir el precio en favor de productores locales, según Sáenz). La unidad expone las dos. La base de la CSJN no cubre ese tomo en `caso`.

## Verificación en la base de la CSJN

- *Grupo Clarín*, Fallos 336:1774, 29/10/2013 (24 sumarios). Composición según `voto`: voto conjunto Highton de Nolasco y Lorenzetti; votos propios Petracchi y Zaffaroni; disidencias parciales Maqueda y Argibay; disidencia Fayt. Usado en la ficha.
- *Iachemet*, Fallos 316:779, 29/4/1993: coincide con Sáenz (n. 40).

## Material en la carpeta fuera del programa de la unidad

- `Unidad6/CIDH_2010_Marco jurídico interamericano del Derecho a la Libertad de Expresión.pdf` (tiene entrada `cidh2010` en `programauba.json`, pero no figura en el programa v25; se menciona con `[Cf. @cidh2010]`).
- `Unidad6/Nino_1992_Garantías constitucionales.PDF` (sin citekey propia identificada).
