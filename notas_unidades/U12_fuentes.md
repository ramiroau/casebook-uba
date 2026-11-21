# U12 — notas de fuentes (para integrar en FUENTES.md)

## Tabla de fuentes

| Citekey | Unidad | Carácter | PDF (en `Materiales_UBA/`) | Extracto | Modo | Paginación |
|---|---|---|---|---|---|---|
| `csjn_delfino1927` | 12 | obligatoria | `Unidad12/1_CSJN - 1927 - Delfino, A.M. y Cía.pdf` (8 pp) | `csjn_delfino1927.txt` | texto | citar por **considerando**. Versión de la Colección de Análisis Jurisprudencial (La Ley), sin paginación de Fallos |
| `csjn_mouviel1957` | 12 | obligatoria | `Unidad12/2_CSJN - 1957 - Mouviel, Raúl Oscar y otros.pdf` (21 pp) | `csjn_mouviel1957.txt` | texto (con limpieza mecánica, ver abajo) | dictamen del procurador: PDF pp. 2-17; sentencia: PDF pp. 17-21. Los considerandos de la sentencia **no están numerados**: citar «sentencia» o «dictamen» |
| `csjn_peralta1990` | 12 | obligatoria | `Unidad12/3_CSJN - 1990 - Peralta, Luis Arcenio y otro c Estado Nacional (M.pdf` (31 pp) | `csjn_peralta1990.txt` | texto | citar por **voto + considerando**. Impresión web de biblioteca.jus.gov.ar (La Ley 1991-C, 158) |
| `csjn_verrocchi1999` | 12 | obligatoria | `Unidad12/4_CSJN - 1999 - Verrochi, Ezio Daniel c. Poder Ejecutivo Nacional.pdf` (27 pp) | `csjn_verrocchi1999.txt` | texto | citar por **voto + considerando**. Copia oficial de la Corte (V. 916. XXXII) |
| `csjn_prattico1960`, `csjn_massa2006`, `csjn_colegio2008`, `csjn_consumidores2010`, `csjn_blanco2018` | 12 | optativas | carpeta `Unidad12/` | — | no extraídas | sólo «Para seguir leyendo»; `colegio2008` y `consumidores2010` se describen en prosa (texto de `corpus/texto/`) |

## Estructura interna de los fallos

### *Delfino* (Fallos 148:430), 20 de junio de 1927
- Cons. 1-2: procedencia del recurso; cons. 3-18: fondo; parte dispositiva (confirma).
- Firmas en el compendio: Bermejo, Repetto, «Laurentena» (sic; Laurencena).

### *Mouviel* (Fallos 237:636), 17 de mayo de 1957
- Dictamen de Sebastián Soler, 25 de abril de 1956 (PDF pp. 2-17).
- Sentencia unánime (PDF pp. 17-21): Orgaz, Argañarás, Galli, Herrera, Villegas Basavilbaso. Revoca.

### *Peralta* (Fallos 313:1513), 27 de diciembre de 1990
- Dictamen del procurador Oscar E. Roger (PDF pp. 3-8).
- Mayoría (PDF pp. 9-26): cons. 1-15 amparo; 16-31 reglamentos de necesidad y urgencia; 32-59 contenido (unión nacional, emergencia, propiedad, igualdad). Firmas: Levene, Cavagna Martínez, Fayt, Barra, Nazareno, Moliné O'Connor.
- Oyhanarte, disidencia de fundamentos y según su voto (PDF pp. 26-30): amparo inapto; rechaza la demanda.
- Belluscio (PDF pp. 30-31): en las firmas, «en disidencia de fundamentos»; el voto se titula «Disidencia»; revoca y rechaza el amparo por falta de prueba de inexistencia de otras vías.
- Petracchi no firma.

### *Verrocchi* (Fallos 322:1726), 19 de agosto de 1999
- Voto que encabeza (Fayt, Belluscio, Bossert): PDF pp. 1-6, cons. 1-11.
- Petracchi, por su voto: PDF pp. 7-13, cons. 7-18 (adhiere a los cons. 1-6 de la mayoría).
- Boggiano, por su voto: PDF pp. 14-17, cons. 1-10.
- Disidencia conjunta de Nazareno, Moliné O'Connor y López: PDF pp. 18-27, cons. 1-15.

## Limpieza

- `extractos/limpieza/csjn_peralta1990.txt`: encabezado «5/13/2018 Fallo Peralta» y pie con la URL de biblioteca.jus.gov.ar y el folio «N/31».
- `extractos/limpieza/csjn_verrocchi1999.txt`: carátula repetida en páginas impares («V. 916. XXXII.», «Verrocchi, Ezio Daniel c/ …», «C orteS uprema deJ usticia dela N ación») y marcas «ES COPIA», «VO-//-», «DISI-//-».
- `csjn_mouviel1957`: **limpieza mecánica en el extracto**. El PDF trae en el margen superior de cada página un renglón con sólo «19» (y el folio al pie). Como `NOTA_AL_PIE` (renglón con sólo un número) corta la página **antes** de aplicar `LIMPIEZA`, un patrón en `extractos/limpieza/` no alcanza: el corte dejaba un renglón por página. En la copia `extractos/csjn_mouviel1957.txt` se borraron con `perl` los 38 renglones que contienen sólo un número y la marca «19» pegada al final de 4 renglones (PDF pp. 4, 14, 15, 20). No se tocó ninguna otra palabra; la cabecera lo documenta (`# limpieza_mecanica`). `diff` contra `corpus/texto/csjn_mouviel1957.txt`: 38 renglones borrados y 4 modificados. **Propuesta al coordinador**: en `verificar.py`/`insertar_extractos.py`, aplicar `LIMPIEZA` antes del corte de notas, o bien anclar `NOTA_AL_PIE` a la mitad inferior de la página.

## Discrepancias con `programauba.json`

- `csjn_mouviel1957` aparece **dos veces** en el JSON (una con `note` de sincronización).
- `csjn_verrocchi1999`: `citation-key` dice `csjn_verrochi1999` y el título «Verrochi» (la carátula oficial es «Verrocchi»); `note` arrastra basura (`…csjn_partidodemocrata1957`).
- `csjn_delfino1927`: `citation-key` dice `csjn_deflino1927`; `note` con basura (`…csjn_adc2012`). Sin fecha en la base del observatorio, pero los sumarios 121268, 121856, 122408 y 123426 confirman Fallos 148:430.
- Citas de Fallos confirmadas con los sumarios de `csjn.db`: 148:430, 237:636, 313:1513, 322:1726.

## Erratas de los textos que los extractos reproducen tal cual

- *Delfino*, cons. 5: «que la contribución ha puesto» (por «constitución»); firma «Laurentena».
- *Mouviel*, sentencia: «ratificado por la ley 13.830» (el dictamen y el sumario 94392 dicen 13.030); «nulla pna» (por «poena»); «La primera de estas formas de no puede» (dictamen).
- *Verrocchi*: «legistativo» (voto que encabeza, cons. 7); asteriscos de la capa de texto («deba*tes», «Cá*mara», «situacio*nes», «mayo*ría»).
- *Peralta*: «le punto» (cons. 15, fuera de los extractos), «objectivos» (cons. 20), «persecusión» (sumario).

## Discrepancias entre notas de clase y fuentes

- Las notas fechan *Peralta* en 1992 y *Verrocchi* en 1998; los fallos son del 27/12/1990 y del 19/8/1999. U12 sigue a los fallos.
- Las notas resumen *Mouviel* diciendo que «el Congreso sí delegó al PEN, lo que es inconstitucional». La sentencia declara inconstitucional el art. 7 inc. a del decreto 33.265/44 (ratificado por ley) y dice que el art. 27 del Código de Procedimientos sólo atribuye la facultad de *juzgar* faltas. U12 sigue a la sentencia.
- Las notas presentan las dos condiciones de *Verrocchi* como requisitos; el cons. 9 exige la concurrencia de «alguna de estas dos circunstancias» (disyuntiva). U12 sigue al texto.
