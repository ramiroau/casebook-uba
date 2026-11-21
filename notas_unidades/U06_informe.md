# Informe — Unidad 6 (Debido proceso sustantivo. Razonabilidad)

## Archivos

- Escritos: `unidades/U06.md` (nuevo), `respaldos/U06_agente.md` (copia idéntica), `extractos/saenz2016_art14y28.txt`, `extractos/bouzat2013.txt`, `extractos/limpieza/saenz2016_art14y28.txt`, `extractos/limpieza/bouzat2013.txt`, `notas_unidades/U06_fuentes.md`, este informe.
- No se tocaron scripts, `FUENTES.md`, `README.md`, `casebook.md`, `programauba.json` ni archivos de otras unidades. No se corrió `build_casebook.sh`.

## Palabras

Prosa propia: unas 3.300 palabras (sin extractos ni corchetes de cita), dentro del objetivo de 3.000 a 4.500. Extractos insertados: 12.233 palabras de las fuentes.

## Verificación

`python3 scripts/insertar_extractos.py --unidades U06 --salida <scratchpad>` → OK (15 marcadores). `python3 scripts/verificar.py --unidades U06` → **OK**: 7 claves usadas, 0 sin entrada; 0 citas en bloque escritas a mano; cobertura 2/2 obligatorias; 15 marcadores resueltos. Ninguna cita lleva `[verif. visual]` (las dos fuentes tienen capa de texto). Las citas breves en prosa (unas treinta) se cotejaron con un script contra los extractos: todas aparecen literalmente.

## Extractos

| Fuente (clave de extracto) | Tramo | PDF pp. | Palabras | Origen |
|---|---|---|---|---|
| saenz2016_art14y28 | introducción y ap. 1 | 1–3 | 1.069 | extracto |
| saenz2016_art14y28 | ap. 2 | 3–4 | 666 | extracto |
| saenz2016_art14y28 | ap. 3.1 | 4–7 | 1.615 | extracto |
| saenz2016_art14y28 | ap. 3.2 | 7–8 | 435 | extracto |
| saenz2016_art14y28 | ap. 3.3 (idoneidad, proporcionalidad, deferencia) | 8–10 | 824 | extracto |
| saenz2016_art14y28 | ap. 3.3 (necesariedad y síntesis) | 10–11 | 568 | extracto |
| bouzat2013 | secs. I y II | 1–2 | 530 | extracto |
| bouzat2013 | secs. III (las dos) | 2–4 | 1.383 | extracto |
| bouzat2013 | sec. IV | 4–5 | 685 | extracto |
| bouzat2013 | sec. V | 6–7 | 1.027 | extracto |
| bouzat2013 | sec. VI (Hileret, Canale, Ercolano) | 7–9 | 902 | extracto |
| bouzat2013 | sec. VI (Avico a Massa) | 9–10 | 700 | extracto |
| bouzat2013 | sec. VI (igualdad y expresión) | 10 | 385 | extracto |
| bouzat2013 | sec. VI (Clarín, Diócesis, ADEBA) | 11–12 | 1.058 | extracto |
| bouzat2013 | sec. VII | 12–13 | 386 | extracto |

Las dos lecturas obligatorias se reproducen completas, sin notas al pie. Párrafos revisados en la salida: se unieron los renglones de la lista final de Sáenz (`unir:`) y se forzó el punto y aparte antes del voto de Petracchi en Bouzat (`parrafo:`).

## Discrepancias y pendientes

- Notas de clase frente a fuentes:
  - Las notas presentan el cuarto paso de Bouzat como «proporcionalidad de grado de afectación e importancia del derecho». El texto lo formula como comparación entre los beneficios de la ley y la disminución del derecho, con un límite fundado en la dignidad (sec. III). La unidad sigue al texto.
  - Las notas explican *Arenzón* por falta de «proporción» entre medida y fin. Sáenz lo usa como ejemplo de falta de idoneidad, de exceso reglamentario y de criterio estricto en igualdad (aps. 3.1 y 3.3). La unidad sigue al texto.
  - Las notas dicen que la diferencia entre el escrutinio norteamericano y la proporcionalidad europea en la Corte argentina es «casuística y no muy relevante». Ninguna lectura lo dice; Bouzat afirma que los estándares europeos fueron «aceptados en forma parcial» (sec. III). No se usó.
  - Las notas atribuyen a Maurino (optativa) la referencia a *Inchauspe*. No se usó, porque Maurino queda sólo en bibliografía.
- Discrepancias entre las fuentes y con `programauba.json`: ver `U06_fuentes.md` (clave `saenz2016b` errónea y duplicada en el JSON; *Hileret* citado como 98:20 y 98:51 con descripciones distintas; año de `bouzat2013`; *Avico* 172:21 frente a 248:21 en el JSON).
- No queda ningún `[PENDIENTE]` abierto.

## Ediciones del autor

Ninguna: la unidad es nueva y no había respaldo previo.

## Decisiones de criterio para revisar

1. **Sin fallos obligatorios.** La línea jurisprudencial se arma con la sec. VI de Bouzat, en cuatro tramos, bajo el título «La jurisprudencia: de *Hileret* a *Clarín*». *Clarín* (optativo) lleva una ficha breve en prosa, sin extracto, con la composición tomada de la base de la CSJN. Si el autor prefiere, *Clarín* puede bajarse a «Para seguir leyendo» y la ficha eliminarse.
2. **Ubicación de la sec. VII de Bouzat.** Su conclusión va al final de la sección jurisprudencial, después de *Clarín*, porque cierra la revisión de casos.
3. **«Test tripartito».** La unidad deja abierta su referencia: puede ser la tríada de límites de Sáenz (legalidad, fines, razonabilidad) o la de juicios del art. 28 (idoneidad, proporcionalidad, necesariedad). Se plantea en «El problema» y en la nota 1.
4. **Notas al pie de Sáenz.** No se insertan. Se mencionan en prosa, con cita «n. N»: *Elortondo*, *Hileret*, *Cipo*, *Chicago Milwaukee* y la cita de Alberdi. Las referencias a casos de otras unidades (*Ercolano* y *Avico* en U17, *Peralta* y *Massa* en U12, *Repetto* en U16, *Elortondo* en U04) son remisiones textuales, sin citekey del fallo.
5. **Remisiones a otras unidades.** La unidad remite a U01 (concepciones de la democracia, con `@gargarella2009d` y `@holmes1993` en la nota 5), U04 (objeción contramayoritaria), U05 (interpretación) y U07 (federalismo). Conviene confirmar que la numeración coincide con la de las unidades redactadas en paralelo.
6. **Bibliografía fuera del programa.** En «Para seguir leyendo» se menciona `cidh2010` (con `Cf.`), que tiene entrada en el JSON pero no figura en el programa v25, y el PDF de Nino sin citekey. Se pueden quitar si el autor no quiere mencionarlos.
7. **Única edición al texto de la fuente**: se quitó del extracto de Sáenz el renglón suelto de la llamada de nota 1 (PDF p. 1). El texto no cambia; está documentado en la cabecera del extracto.
