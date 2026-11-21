# Fuentes — Unidad 16 (para integrar en FUENTES.md)

## Tabla de fuentes

| Citekey | Unidad | Carácter | PDF (en `Materiales_UBA/`) | Extracto | Modo | Paginación |
|---|---|---|---|---|---|---|
| `saba2005` | 16 | obligatoria | `Unidad16/1_Saba - 2005 - (Des)igualdad estructural copy.pdf` (29 pp) | `saba2005.txt` | texto | versión de autor numerada 1-29, sin paginación de revista: **página citada = PDF** |
| `treacy2011` | 16 | obligatoria | `Unidad16/2_Treacy - 2011 - Categorías sospechosas y control de constitucional.pdf` (36 pp) | `treacy2011.txt` | texto | impresa = PDF **+180** (*Lecciones y Ensayos* 89, pp. 181-216) |
| `csjn_gonzalez2000` | 16 | obligatoria | `Unidad16/3_CSJN - 2000 - González de Delgado.pdf` (44 pp; idéntico, mismo md5, a `Unidad15/CSJN - 2000 - González de Delgado.pdf`) | `csjn_gonzalez2000.txt` | texto | citar por **voto + considerando** |
| `csjn_gonzalez2000` (dictamen) | 16 | obligatoria | no está en el PDF del compendio; tomo impreso de Fallos 323 vía `csjn.db` (`fallo_db.py 323 2659 --fuente volumen`) | `csjn_gonzalez2000_dictamen.txt` (clave de extracto distinta de la citekey; se cita `[@csjn_gonzalez2000]`) | ocr (copia en `limpios/`) | página impresa de Fallos (323:2670-2673); citar por apartado del dictamen |
| `csjn_repetto1988` | 16 | optativa | `Unidad16/CSJN - 1988 - Repetto...pdf` | — | no extraído | sólo en «Para seguir leyendo» y descrito en prosa (vía Treacy y Saba) |
| `csjn_reyes2007` | 16 | optativa | `Unidad16/CSJN - 2007 - Reyes Aguilera.pdf` | — | no extraído | ídem |
| `saldivia2018` | 16 | optativa | `Unidad16/Saldivia Menajovsky - 2018 - ...pdf` | — | no extraído | sólo en «Para seguir leyendo» |

## Estado de `limpios/`

| Citekey | Copia | Estado | Notas |
|---|---|---|---|
| `csjn_gonzalez2000_dictamen` | capa de texto del tomo de Fallos 323 (vol_id 379, motor `pdftotext`) | `revisado: si` | Sólo pp. 2670-2673 (aps. V a VII del dictamen y firma). **Sin imagen disponible**: el compendio no trae el dictamen y la base no guarda el PDF del tomo. Correcciones por contexto, una por error: «arto»→«art.», «a qua»→«a quo», «NQ»→«Nº», «gobiemo»→«gobierno», «00 lo que»→«En lo que», «Suprem:-»→«Suprema», «{producto»→comillas, «N acianal», «accionan tes», «por.», «241J265»→«241/265». En p. 2671 la capa desordena palabras en columnas; el orden se restituyó por la sintaxis y por la transcripción del fallo de Cámara que el propio dictamen cita (y los sumarios 39608-39614 de la base). Conviene cotejar contra el tomo impreso cuando haya acceso |

## Cambios mecánicos en extractos de texto

- `saba2005.txt`: se quitó el renglón con la sola llamada de nota «9» (PDF p. 3, superíndice de «Mill»), que el corte de notas tomaba como comienzo del pie y truncaba la página. Documentado en la cabecera.
- `csjn_gonzalez2000.txt`: se quitaron 24 renglones en blanco espurios dentro de párrafos (PDF pp. 8-9, 11-13, 19-20, voto de Petracchi), que partían frases y palabras con guion. Documentado en la cabecera.
- `treacy2011.txt`: sin cambios.

## Patrones de limpieza (`extractos/limpieza/`)

- `saba2005.txt`: dos continuaciones de notas por encima del primer número (PDF pp. 5 y 26); llamadas de nota tras cifra, comilla tipográfica o espacio (generadas recorriendo la numeración 1-78 en orden y ancladas con 5-14 caracteres de contexto).
- `treacy2011.txt`: encabezados y pie de imprenta («Lecciones y ensayos 89.indd …»); bloque de notas al pie (desde el primer renglón «N. » a 15 espacios hasta el pie; las notas de esta revista no empiezan con un renglón de sólo número); cuatro continuaciones de notas (PDF pp. 11, 19, 23, 29); llamadas de nota tras punto, comilla o raya (numeración 1-58).
- `csjn_gonzalez2000.txt`: carátula de páginas impares («G. 653. XXXIII.», «RECURSO DE HECHO», carátula de partes, «ES COPIA») y continuación de la nota 5 del voto de Petracchi (PDF p. 19).
- Se corrió `verificar.py` sobre todas las unidades con estos patrones: no rompen ningún marcador ajeno (el único problema reportado es `@klarmann` en U01, ajeno a U16).

## Discrepancias con `programauba.json`

- `csjn_gonzalez2000`: la entrada da `page: 2659` (Fallos 323:2659), confirmado por la base (sumarios 39608-39983, vol_start 323:2659). El campo `note` arrastra basura de sincronización (`mlzsync1:…csjn_nicosia`).
- `saba2005`: la entrada registra la *Revista Derecho y Humanidades* 11 (2005) sin páginas; el PDF es una versión de autor sin paginación de revista y su portada registra otras dos publicaciones (UCES 2004, pp. 479-514; Alegre y Gargarella 2007). Se cita por la numeración del PDF.
- `treacy2011`: `container-title` dice «Lecciones y Ensayos No» (sobra «No»); falta el número (89).

## Discrepancias entre fuentes

- *González de Delgado*: Treacy dice que la mayoría rechazó con fundamentos ajenos a la igualdad, vinculados a la competencia (p. 200 n. 31); Saba, que «la mayoría de los argumentos de los Ministros» se articularon en torno a la no discriminación (p. 24). El texto del fallo da la razón a Treacy respecto de la sentencia (remisión al dictamen); la observación de Saba sólo vale para los votos concurrentes. Se planteó como pregunta (nota 6).
- Saba atribuye a Petracchi la frase sobre «perpetuar la inferioridad legal, social y económica de la mujer» (p. 25); en el voto (cons. 9) es la descripción de lo que sostuvo la Corte norteamericana en *United States v. Virginia*, que Petracchi hace suya en la nota 5. Se planteó como pregunta (nota 7).
- Treacy escribe «Mantecón Valdez» en el cuerpo y «Mantecón Valdés» en la nota 23 y en p. 197; «Arenzon» y «Arenzón». Se reproducen tal cual.
- El programa habla de igualdad como «no subordinación»; Saba usa «no sometimiento (o no exclusión)». Se señala en «El problema».

## Discrepancias entre notas de clase y fuentes

Las notas tratan la igualdad bajo el título «Unidad 17» con el copete de un programa anterior.

- Las notas dicen que Saba postula una visión «robusta» de la igualdad; el término es de Saldivia (optativa). Saba habla de igualdad «estructural».
- Las notas definen la desigualdad estructural como la que «no es el resultado de una circunstancia (p.ej. crisis económicas) sino que tiene una evolución constante». El texto la define por el sometimiento y la exclusión sistemática de grupos por otros grupos (pp. 4, 20); la contraposición con las crisis no aparece.
- Las notas dicen que el argumento le permitió a Saba defender la paridad de género o una lista partidaria sólo de mujeres. El texto no trata esos casos; su ejemplo final es una agencia estatal que sólo contrata mujeres (pp. 27-28). La unidad sigue al texto.
