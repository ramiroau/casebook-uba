# Informe U12 — Poder ejecutivo. Decretos de necesidad y urgencia. Facultades delegadas. Decretos reglamentarios.

## Archivos

- `unidades/U12.md` (nuevo) y su copia `respaldos/U12_agente.md`.
- `extractos/csjn_delfino1927.txt`, `csjn_peralta1990.txt`, `csjn_verrocchi1999.txt` (copias de `corpus/texto/`, `# modo: texto`).
- `extractos/csjn_mouviel1957.txt` (copia con limpieza mecánica de renglones de margen; ver `U12_fuentes.md`).
- `extractos/limpieza/csjn_peralta1990.txt`, `extractos/limpieza/csjn_verrocchi1999.txt`.
- `notas_unidades/U12_fuentes.md`, este informe.

No se corrió `build_casebook.sh` ni se tocaron archivos compartidos.

## Palabras

Unas 4.080 palabras fuera de los marcadores (incluye encabezados, fichas y notas y preguntas); objetivo 3.000–4.500. Extractos insertados: 17.183 palabras.

## Verificación

`insertar_extractos.py --unidades U12` → OK (13 marcadores). `verificar.py --unidades U12` → **OK**: 9 citekeys, todas en `programauba.json`; 0 citas en bloque manuales; cobertura 4/4 obligatorias; 13 extractos resueltos. Citas con `[verif. visual]`: 0 (todas las fuentes usadas tienen capa de texto). Párrafos revisados en la salida de scratchpad y corregidos con `unir:`/`parrafo:` (Delfino y Mouviel).

## Extractos

| Fuente | Tramo | PDF pp. | Palabras | Origen |
|---|---|---|---|---|
| `csjn_delfino1927` | cons. 3-18 y dispositiva | 3-8 | 1.792 | extracto |
| `csjn_mouviel1957` | dictamen Soler, tramo 1 | 3-11 | 2.786 | extracto (limpieza mecánica) |
| `csjn_mouviel1957` | dictamen Soler, tramo 2 | 11-15 | 1.358 | extracto (limpieza mecánica) |
| `csjn_mouviel1957` | sentencia completa | 17-21 | 1.342 | extracto (limpieza mecánica) |
| `csjn_peralta1990` | mayoría, cons. 16-24 | 12-15 | 1.924 | extracto |
| `csjn_peralta1990` | mayoría, cons. 25-31 | 15-18 | 1.679 | extracto |
| `csjn_peralta1990` | mayoría, cons. 32-36 | 18-19 | 896 | extracto |
| `csjn_peralta1990` | mayoría, cons. 47-48, 59 y dispositiva | 23-26 | 804 | extracto |
| `csjn_verrocchi1999` | voto que encabeza, cons. 6-11 y dispositiva | 2-6 | 1.315 | extracto |
| `csjn_verrocchi1999` | Petracchi, cons. 11-17 | 10-13 | 967 | extracto |
| `csjn_verrocchi1999` | Boggiano, cons. 6-10 | 15-17 | 713 | extracto |
| `csjn_verrocchi1999` | disidencia, cons. 6-9 | 20-22 | 976 | extracto |
| `csjn_verrocchi1999` | disidencia, cons. 11-12, 15 y dispositiva | 24-27 | 631 | extracto |

## Discrepancias notas de clase / fuentes

Ver `U12_fuentes.md`: fechas de *Peralta* (1990, no 1992) y *Verrocchi* (1999, no 1998); qué norma declara inconstitucional *Mouviel*; carácter disyuntivo de las dos circunstancias de *Verrocchi*, cons. 9.

## Pendientes

Ningún `[PENDIENTE]` en el texto. Queda una propuesta técnica para el coordinador: el corte de notas al pie (`NOTA_AL_PIE`) corre antes de `LIMPIEZA`, de modo que un número de margen en lo alto de la página no se puede filtrar con patrones; por eso se limpió a mano (mecánicamente) la copia de *Mouviel*.

## Ediciones del autor

No hay: la unidad es nueva.

## Decisiones de criterio para revisar

1. **Orden de la unidad.** Se invirtió el orden del copete: primero reglamento y delegación (*Delfino*, *Mouviel*), después decretos de necesidad y urgencia (*Peralta*, *Verrocchi*), para seguir la línea histórica. Título y copete se transcriben literales.
2. **Mouviel**: se reproduce casi todo el dictamen de Soler (salvo la parte sobre si el cumplimiento de la pena torna abstracto el caso) porque la Corte lo incorpora como fundamento y la sentencia es breve.
3. **Peralta**: se omitieron la parte sobre el amparo (cons. 3-15), la jurisprudencia de emergencia (cons. 37-46, que corresponde a la Unidad 14), propiedad e igualdad (cons. 49-58) y los votos de Oyhanarte y Belluscio (sólo tratan del amparo). La caracterización de Belluscio sigue las dos rotulaciones del compendio («disidencia de fundamentos» en las firmas, «Disidencia» en el título del voto).
4. **Verrocchi**: del voto de Petracchi se omiten los cons. 7-10 (debates de la Convención y fuente española); de la disidencia, los cons. 1-5, 10, 13 y 14.
5. **Optativas descritas en prosa sin extracto**: *Colegio Público de Abogados* (art. 76) y *Consumidores Argentinos* (estado actual de los DNU), por considerarlas indispensables para cerrar las dos líneas. *Prattico*, *Massa* y *Blanco* quedan sólo en «Para seguir leyendo» (*Massa* con una línea en el texto). *Blanco* tiene en las notas de clase un tratamiento extenso; si el autor quiere desarrollar los decretos reglamentarios, convendría promoverlo a un caso con extracto.
6. **Nota 9**: se señala que Petracchi adhiere al «considerando 10 del voto del juez Belluscio», que en el compendio no existe como voto separado. Puede ser una rareza de la copia o un indicio de cómo se formó la mayoría; conviene cotejarlo con Fallos.
7. **Síntesis**, tercera pregunta: alude al uso extendido de decretos legislativos después de 1994 sin fuente del programa; está formulada como pregunta abierta, pero el autor puede preferir apoyarla en un texto de la Unidad 11 o eliminarla.
