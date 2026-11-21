# Informe — Unidad 17 (Derecho de propiedad)

## Archivos

- Escritos: `unidades/U17.md` (nueva), `respaldos/U17_agente.md` (copia), `extractos/elias2014a.txt`, `extractos/csjn_ercolano1922.txt`, `extractos/limpios/elias2014a.txt`, `extractos/limpios/csjn_ercolano1922.txt`, `notas_unidades/U17_fuentes.md`, este informe.
- No se tocaron scripts, `FUENTES.md`, `README.md`, `casebook.md` ni archivos de otras unidades. No se corrió `build_casebook.sh`; la prueba se hizo con `insertar_extractos.py --salida <scratchpad>`.

## Extensión

Prosa propia (sin extractos): unas 3.350 palabras, dentro del objetivo de 3.000-4.500. No se rellenó.

## Verificación

`python3 scripts/verificar.py --unidades U17` → **OK**. 10 citekeys, todas en `programauba.json`. Cobertura: las 2 obligatorias citadas. 12 marcadores resueltos (15.759 palabras de las fuentes). Citas en bloque escritas a mano: ninguna (0/0); todo texto de fuente entra por marcador. Las 12 líneas de atribución llevan `[verif. visual]`, porque ambas fuentes son OCR transcripto contra la imagen.

## Extractos

| Fuente | Páginas | Palabras | Origen |
|---|---|---|---|
| Elías, tramo 1 | pp. 685-688 | 890 | limpio |
| Elías, tramo 2 | pp. 689-692 | 1.494 | limpio |
| Elías, tramo 3 | pp. 693-696 | 1.123 | limpio |
| Elías, tramo 4 | pp. 696-703 | 2.082 | limpio |
| Elías, tramo 5 | pp. 703-707 | 1.368 | limpio |
| Elías, tramo 6 | pp. 707-711 | 1.501 | limpio |
| *Ercolano*, mayoría | Fallos 136:170-172 | 903 | limpio |
| *Ercolano*, mayoría | Fallos 136:172-177 | 1.650 | limpio |
| *Ercolano*, mayoría y parte dispositiva | Fallos 136:177-179 | 679 | limpio |
| *Ercolano*, disidencia Bermejo, cons. 4-14 | Fallos 136:180-185 | 1.618 | limpio |
| *Ercolano*, disidencia Bermejo, cons. 15-21 | Fallos 136:185-188 | 1.293 | limpio |
| *Ercolano*, disidencia Bermejo, cons. 25-30 y parte dispositiva | Fallos 136:190-193 | 1.158 | limpio |

Elías se reproduce completo (sin notas al pie y sin los títulos I y III). *Ercolano*: la mayoría completa; de la disidencia se omiten los cons. 1-3 (admisibilidad, texto de la ley, posición de las partes) y 22-24 (citas doctrinarias sobre el poder de policía y el caso de las corridas de toros).

Párrafos: los dos limpios marcan el punto y aparte con renglón en blanco; se agregaron cuatro `parrafo:` para los párrafos que empiezan al tope de una página. Revisado en la salida del script.

## Fuentes y su preparación

- `elias2014a`: el OCR del corpus es inservible en las mitades izquierdas (columnas entrelazadas). Se re-OCRizó cada mitad enderezada y se transcribió el capítulo completo renglón por renglón contra la imagen. Detalle en `U17_fuentes.md`.
- `csjn_ercolano1922`: `fallo_db.py 136 161` falla porque `vol_start` ubica el caso en 136:160; se usó `fallo_db.py 136 160 --hasta 194`. Fallos 136:170-193 corregidas contra la imagen del compendio, que reproduce el mismo tomo.

## Discrepancias y pendientes

- `csjn_avico1934`: `programauba.json` dice Fallos 248:21; la base de la CSJN y Elías dan **172:21**. Proponer corrección de la entrada.
- Discrepancias entre notas de clase y fuentes (numeración de la unidad, página del pluralismo en Elías, los tres problemas «macro», la fórmula de la «sustancia» en *Ercolano*): ver `U17_fuentes.md`. U17 sigue a los textos.
- No hay `[PENDIENTE]` abiertos.

## Ediciones del autor

Unidad nueva: no había ediciones que conservar.

## Decisiones de criterio para revisar

1. **Copete y *New Deal*.** Ninguna lectura de la unidad trata el *New Deal*. Para el encuadre se usaron dos fuentes obligatorias de otras unidades: Gargarella 2021 (Unidad 5, pp. 220-222: *Lochner*, *West Coast Hotel*, *Hileret*-*Ercolano*-*Mango*-*Avico*) y Bouzat 2013 (Unidad 6, sec. VI: *Hileret*, la crítica a *Ercolano*, *Avico* y *Blaisdell*). Ambas tienen citekey en el programa. No se introdujo nada ajeno al programa.
2. **Línea jurisprudencial.** *Avico* (optativa, sin PDF) y *Peralta*/*Bustos* se mencionan en prosa con apoyo en Elías, Bouzat y Gargarella, sin extracto. *Coihue* (optativa) queda sólo en la bibliografía.
3. **Cita de la mayoría de *Ercolano*.** Como no numera considerandos, se cita por página de Fallos (136:170-179). El *holding* sigue los sumarios de la base de la CSJN.
4. **Selección de la disidencia.** Se omitieron los cons. 22-24 por ser doctrinarios. Si se prefiere la disidencia completa, basta extender el segundo marcador hasta «páginas 829 y 839).» y abrir uno nuevo en el cons. 24.
5. **Toma de partido.** La prosa registra dos críticas que provienen de las fuentes: la de Elías a Sampay (originalismo) y la de Bouzat a *Ercolano* (falta de apoyo fáctico). No se agregó ninguna valoración propia. La nota 10 contrasta a Elías con el esquema de razonabilidad de las notas de clase; revisar si conviene mencionarlas en el casebook.
