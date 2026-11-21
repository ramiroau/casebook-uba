# Informe — Unidad 8 (redacción nueva, noviembre de 2026)

## Archivos

- Escritos: `unidades/U08.md`, `respaldos/U08_agente.md` (copia idéntica), `extractos/abregu1997.txt` (`# modo: texto`), `extractos/csjn_ekmekdjian1992.txt` (`# modo: ocr`), `extractos/limpios/csjn_ekmekdjian1992.txt` (`# revisado: si`), `extractos/limpieza/abregu1997.txt`, `notas_unidades/U08_fuentes.md`, este informe.
- No se tocaron scripts, `FUENTES.md`, `README.md`, `casebook.md` ni archivos de otras unidades. No se corrió `build_casebook.sh`.

## Palabras

Prosa propia (sin extractos): **3.473** palabras, dentro del objetivo de 3.000–4.500. Extractos insertados: 15.849 palabras (Abregú 7.532; *Ekmekdjian* 7.317).

## Verificación

`insertar_extractos.py --unidades U08` → OK (14 marcadores resueltos). `verificar.py --unidades U08` → **OK**: 9 citekeys, 0 sin entrada; cobertura: 2 obligatorias, ambas citadas; 0 citas en bloque escritas a mano (todo va por marcador), por lo tanto 0 con `[verif. visual]`.

## Extractos

| Fuente | Tramo | PDF pp. | Palabras | Origen |
|---|---|---|---|---|
| `abregu1997` | sección I | 1–3 | 1.202 | extracto |
| `abregu1997` | sección II | 3–5 | 1.016 | extracto |
| `abregu1997` | sección III (1 a 3) | 5–9 | 1.807 | extracto |
| `abregu1997` | sección IV, aps. 1–2 | 9–12 | 1.690 | extracto |
| `abregu1997` | sección IV, aps. 3–5 | 13–18 | 2.817 | extracto |
| `csjn_ekmekdjian1992` | mayoría, cons. 1–3 | 12–13 | 396 | limpio |
| `csjn_ekmekdjian1992` | mayoría, cons. 7 y 12 | 14–18 | 409 | limpio |
| `csjn_ekmekdjian1992` | mayoría, cons. 15–22 | 20–24 | 1.379 | limpio |
| `csjn_ekmekdjian1992` | mayoría, cons. 24–27 (1.er párr.) | 25–28 | 1.292 | limpio |
| `csjn_ekmekdjian1992` | mayoría, cons. 31–32 y dispositiva | 30–31 | 269 | limpio |
| `csjn_ekmekdjian1992` | Petracchi y Moliné O'Connor, cons. 13–19 | 36–41 | 2.103 | limpio |
| `csjn_ekmekdjian1992` | Petracchi y Moliné O'Connor, cons. 25–26 y dispositiva | 46–47 | 368 | limpio |
| `csjn_ekmekdjian1992` | Levene, cons. 11–12, 20–22 y dispositiva | 52, 55 | 571 | limpio |
| `csjn_ekmekdjian1992` | Belluscio, cons. 4–6 y dispositiva | 56–58 | 530 | limpio |

Abregú se reproduce completo salvo la sección V (estructura del libro) y las notas.

## Discrepancias entre notas de clase y fuentes

- *Martín & Cía.*: las notas dicen «ley posterior deroga ley anterior»; Abregú (III.1) lo formula en términos de responsabilidad internacional y jerarquía legal. Se siguió el texto.
- Nombre del programa: las notas dicen «la Noche del Domingo»; el fallo, «La Noche del Sábado».
- Cons. 18 de la mayoría: el tomo imprime «art. 17 de la Convención de Viena» donde el texto citado es el art. 27 (errata conservada y señalada en la línea de encuadre).

## [PENDIENTE]

Ninguno en el texto. Observación de método: en el OCR de *Ekmekdjian* los pasajes en que los dos OCR independientes coinciden no se cotejaron renglón por renglón contra la imagen salvo en 11 de las 25 páginas usadas (detalle en `U08_fuentes.md`). Si el coordinador exige cotejo visual completo, faltan PDF 12–14, 20, 24, 26–28, 30, 36, 41, 46–47, 52, 55–57.

## Ediciones del autor

Unidad nueva: no hay ediciones del autor.

## Decisiones de criterio a revisar

1. **Selección de *Ekmekdjian*.** Se extractan los cuatro votos. De la mayoría se omiten los cons. 4–6, 8–11 (concentración de medios, cita de *Tornillo*), 13–14 (derecho comparado y provincial), el resto del cons. 27 (derecho comparado sobre sentimiento religioso) y los cons. 28–30. Si se quiere la parte sobre medios entera, agregar cons. 8–11 (PDF 14–18, requiere revisar PDF 15–17).
2. **Disidencias.** Se presenta la de Petracchi y Moliné O'Connor con más extensión porque coincide con la mayoría en la operatividad (presunción de operatividad, cons. 15–17) y diverge en legitimación; la ficha y una línea de encuadre lo dicen. Es una lectura del cuadro de votos que el autor puede querer matizar.
3. **Optativos en prosa.** *Giroldi* y *Ministerio de Relaciones Exteriores* se describen en una sección breve porque el copete nombra a *Ministerio*. *Giroldi* se describe sólo a través del pasaje que transcribe Abregú (no hay PDF). *Ministerio* se describe a partir del voto que encabeza (cons. 1–3, 7–11, 16–20), leído en `corpus/texto/`; no se identificó con certeza a los firmantes del voto que encabeza en la página de firmas (OCR ilegible), por eso sólo se nombra a Rosatti (por su voto) y Maqueda (disidencia). *Espósito* queda sólo en bibliografía.
4. **Tomar partido.** La nota 2 (posible circularidad del argumento de la Convención de Viena) y el último párrafo de la síntesis (la doctrina general se construyó en un caso de alcance discutible) formulan objeciones; se dejaron como preguntas, sin resolver.
5. **Paginación de Abregú.** Sin paginación impresa: se cita por sección (I–IV, con apartado). Si se consigue la edición de Del Puerto, conviene pasar a páginas.
6. **Fallos 340:47** para *Ministerio* y **318:514** para *Giroldi* se tomaron de la base del observatorio y se escribieron en la prosa; `programauba.json` no registra la cita de *Ministerio*.
