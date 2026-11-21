# Informe — Unidad 16. Principio de igualdad

## Archivos

- Escritos: `unidades/U16.md` (nueva), `respaldos/U16_agente.md` (copia idéntica), `notas_unidades/U16_fuentes.md`, este informe.
- Extractos nuevos: `extractos/saba2005.txt`, `extractos/treacy2011.txt`, `extractos/csjn_gonzalez2000.txt`, `extractos/csjn_gonzalez2000_dictamen.txt`.
- Copia corregida nueva: `extractos/limpios/csjn_gonzalez2000_dictamen.txt` (`# revisado: si`, ver salvedad abajo).
- Patrones nuevos: `extractos/limpieza/saba2005.txt`, `treacy2011.txt`, `csjn_gonzalez2000.txt`.
- No se tocaron archivos compartidos. No se corrió `build_casebook.sh`.

## Palabras

- Prosa propia (sin marcadores, con encabezados, ficha y notas): **3.565**, dentro del objetivo de 3.000-4.500.
- Texto de las fuentes insertado: 33.228 palabras en 16 marcadores. Es mucho; responde a la preferencia por extractos largos (Saba completo, Treacy casi completo, voto de Petracchi completo).

## Verificación

`insertar_extractos.py --unidades U16` → OK. `verificar.py --unidades U16` → **OK**: 6 citekeys, 0 sin entrada; 0 citas en bloque escritas a mano; cobertura: 3 obligatorias, todas citadas; 16 marcadores resueltos. **0** líneas con `[verif. visual]` (las tres fuentes principales tienen texto nativo). `verificar.py` sobre todas las unidades: el único problema es `@klarmann` en U01, ajeno. Pandoc procesa la salida sin errores.

## Extractos

| Fuente | Páginas | Palabras | Origen |
|---|---|---|---|
| `saba2005`, intro (Moreno, Berlin, propósito) | PDF 1-5 | 1.604 | extracto |
| `saba2005`, trato igual y no discriminación | PDF 5-13 | 4.008 | extracto |
| `saba2005`, acciones afirmativas | PDF 13-18 | 2.460 | extracto |
| `saba2005`, individualista y estructural | PDF 18-25 | 3.130 | extracto |
| `saba2005`, dos conceptos de categorías sospechosas, conclusión | PDF 25-29 | 1.817 | extracto |
| `treacy2011`, I-II | PDF 2-5 (pp. 182-185) | 1.521 | extracto |
| `treacy2011`, III | PDF 5-17 (pp. 185-197) | 3.862 | extracto |
| `treacy2011`, IV | PDF 17-29 (pp. 197-209) | 4.240 | extracto |
| `treacy2011`, V-VII | PDF 29-36 (pp. 209-216) | 2.719 | extracto |
| `csjn_gonzalez2000`, sentencia | PDF 1 | 141 | extracto |
| `csjn_gonzalez2000_dictamen`, ap. VII | Fallos 323:2670-2673 | 1.217 | limpio (sin imagen) |
| `csjn_gonzalez2000`, Petracchi cons. 1-13 | PDF 7-23 | 4.159 | extracto |
| `csjn_gonzalez2000`, Fayt cons. 7 | PDF 3-6 | 830 | extracto |
| `csjn_gonzalez2000`, Boggiano cons. 3-11 | PDF 24-27 | 765 | extracto |
| `csjn_gonzalez2000`, Bossert cons. 8-11 | PDF 34-37 | 795 | extracto |
| `csjn_gonzalez2000`, Vázquez cons. 6 | PDF 43 | 196 | extracto |

## Discrepancias y pendientes

- Notas de clase vs. fuentes: tres discrepancias (igualdad «robusta», definición de desigualdad estructural, ejemplos de paridad y listas de mujeres). Detalle en `U16_fuentes.md`. La unidad sigue al texto.
- Entre fuentes: Treacy y Saba describen de modo distinto los fundamentos de la mayoría en *González de Delgado*; Saba atribuye a Petracchi una frase que en el voto describe *United States v. Virginia*. Se dejaron como preguntas (notas 6 y 7).
- **Salvedad sobre el dictamen**: la copia de `limpios/` se corrigió por contexto, sin imagen (el compendio no reproduce el dictamen y la base no guarda el PDF del tomo); en p. 2671 se restituyó el orden de palabras que la capa de texto desordena. Marcada `revisado: si` con esa advertencia en la cabecera. Propuesta: cotejar con el tomo impreso de Fallos 323 cuando sea posible, o quitar el marcador si se prefiere usar sólo el compendio.
- No queda ningún `[PENDIENTE]` abierto.

## Ediciones del autor

Unidad nueva: no hay ediciones del autor.

## Decisiones de criterio a revisar

1. Se incluyó el **dictamen del Procurador General** (ap. VII), que no está en el compendio, porque es el fundamento de la mayoría y sin él no se entiende el *holding*. Clave de extracto propia (`csjn_gonzalez2000_dictamen`), cita `[@csjn_gonzalez2000]`.
2. El *holding* se formuló a partir del dictamen y de los sumarios de la base (competencia de la Universidad, control de legalidad, ningún derecho de los padres a la educación diferenciada). Los argumentos de igualdad quedan en los votos concurrentes.
3. Votos: Petracchi completo (el que leen las dos lecturas); Fayt cons. 7 (la parte propia, que Saba cita en la n. 45); Boggiano cons. 3-11 (lectura opuesta de la Convención); Bossert cons. 8-11 (omití cons. 1-7, que reproducen el razonamiento de competencia); Vázquez sólo cons. 6.
4. Se tomaron extractos completos de Saba y casi completos de Treacy (sin el resumen ni las notas). Si resultan demasiado largos, el recorte natural es la sección IV de Treacy (pp. 197-209), salvo el apartado «a) Sexo».
5. *Repetto* y *Reyes Aguilera* (optativas) se describen en prosa en la sección jurisprudencial, con citekey, apoyadas en Treacy y Saba; no se extractaron.
6. En «El problema» se señala que el programa dice «no subordinación» y Saba dice «no sometimiento». Se usó el término del texto en todo el resto.
7. Cambios mecánicos en dos extractos de texto (renglón con la llamada «9» en Saba; 24 renglones en blanco espurios en el voto de Petracchi), documentados en las cabeceras. Las llamadas de nota de Saba y Treacy se filtraron con patrones generados recorriendo la numeración en orden y anclados con contexto.
