# Fuentes — Unidad 8 (para integrar en FUENTES.md)

## Filas para la tabla de fuentes

| Citekey | Unidad | Carácter | PDF (en `Materiales_UBA/`) | Extracto | Modo | Paginación |
|---|---|---|---|---|---|---|
| `abregu1997` | 8 | obligatoria | `Unidad8/1_Abregú_Courtis_1997_La aplicación del derecho internacional de los derechos humanos por los.pdf` (28 pp) | `abregu1997.txt` | texto | **sin paginación impresa** (versión re-tipeada). Citar por sección (I–V). El capítulo publicado ocupa pp. 3–31 según `programauba.json`. Cuerpo: PDF 1–20; notas al final del archivo |
| `csjn_ekmekdjian1992` | 8 | obligatoria | `Unidad8/2_CSJN_1992_Ekmekdjian, Miguel Angel c.pdf` (58 pp, escaneo del tomo 315 de Fallos) | `csjn_ekmekdjian1992.txt` | OCR (copia corregida en `limpios/`) | citar por **voto + considerando**. Fallos 315 = PDF + 1491 (PDF 1 = p. 1492) |
| `csjn_ministerio2017` | 8 | optativa | `Unidad8/CSJN_2017_Ministerio de Relaciones Exteriores y Cultos s- informe de sentencia dictada en.pdf` (30 pp) | — | no extraído | sólo prosa breve y «Para seguir leyendo». Se leyó `corpus/texto/csjn_ministerio2017.txt` (voto que encabeza, cons. 1–3, 7–11, 16–20) |
| `csjn_giroldi1995` | 8 | optativa | sin PDF | — | — | sólo prosa (a través de la cita en Abregú, sección IV.2) y bibliografía |
| `csjn_esposito2004` | 8 | optativa | sin PDF | — | — | sólo bibliografía |
| `hitters2009`, `rosenkrantz2005`, `filippini2005`, `biscardi2016` | 8 | optativas | en `Unidad8/` | — | no extraídos | sólo «Para seguir leyendo» |

## Estructura interna del fallo

### *Ekmekdjian c. Sofovich* (Fallos 315:1492), 7 de julio de 1992

- PDF 1: final del fallo anterior y comienzo de los sumarios; PDF 1–12: sumarios.
- Mayoría (Cavagna Martínez, Barra, Fayt, Nazareno, Boggiano): PDF 12–31, cons. 1–32. Firmas en PDF 31 (verificadas contra la imagen).
- Disidencia de Petracchi y Moliné O'Connor: PDF 31–47, cons. 1–26.
- Disidencia de Levene: PDF 48–55, cons. 1–22.
- Disidencia de Belluscio: PDF 56–58, cons. 1–6.
- Citas confirmadas en la base del observatorio (tabla `sumario`): Ekmekdjian 315:1492; Giroldi 318:514 (7/4/1995); Espósito 327:5668 (23/12/2004); Ministerio de Relaciones Exteriores 340:47 (14/2/2017; `programauba.json` no registra tomo y página).

## Copias corregidas (`extractos/limpios/`)

| Citekey | Copia | Estado | Notas |
|---|---|---|---|
| `csjn_ekmekdjian1992` | capa OCR previa del PDF del compendio (escaneo del tomo; conserva sangrías) | `revisado: si` | Corregidas: PDF 12–14, 18, 20–28, 30–31 (mayoría), 36–41, 46–47 (Petracchi y Moliné O'Connor), 52, 55 (Levene), 56–58 (Belluscio). Método: cotejo palabra por palabra con un segundo OCR independiente del mismo tomo (`scripts/fallo_db.py 315 1492`, tabla `vol_page`); cada discrepancia se resolvió una por una y las dudosas contra la imagen (PDF 18, 21, 22, 23, 25, 31, 37, 38, 39, 40, 58). Los pasajes en que los dos OCR coinciden no se cotejaron renglón por renglón con la imagen salvo en esas páginas. Se quitaron los encabezados de página en todo el archivo, una línea con un «0» suelto (cons. 5, PDF 13) que cortaba la página y el resto del cons. 5 deformado. «e/» por «c/» corregido en las carátulas citadas. Erratas del impreso conservadas: «art. 17 de la Convención de Viena» (cons. 18, PDF 21: el texto citado es el art. 27), «EVerfGE», «Cancado», «J.C.J.», «Steart», «servir legal y honradamente» (cons. 12, PDF 18). En PDF 40 el renglón «-algunos, muy atendibles-» terminaba en raya y el script lo pegaba a «en»: se subió «en» al renglón anterior |

## Limpieza (`extractos/limpieza/abregu1997.txt`)

Trece patrones, anclados al contexto exacto, para llamadas de nota pegadas a cifras o siglas que `MARCA_DE_NOTA` no reconoce: «art. 1.1**16**», «art. 2**17**», «art. 2.2**18**», «art. 2.1**19**», «art. 2**20**», «art. 3**21**» (sección II, PDF 4), «Corte IDH**28**», «Moncayo**38**», «CN**39**», «art. 7.5**51**», «Humanos 1995**53**», «Courtis**56**», «1976–1983**59**».

## Discrepancias con `programauba.json`

- `abregu1997`. La entrada lista como autores a Abregú y Courtis; el texto está firmado sólo por Martín Abregú (los dos son compiladores del volumen). El campo `container-title` mezcla compiladores, título del libro y editorial. `type` es `article-journal` aunque se trata de un capítulo de libro.
- `csjn_ministerio2017`. Sin `container-title`/`volume`/`page`: corresponde Fallos 340:47. El campo `note` dice `csjn_cippec2014` (resto de una fusión). El título dice «Cultos»; el fallo dice «Culto».
- `hitters2009`, `rosenkrantz2005`, `filippini2005`. El campo `title-short` de las tres arrastra el título de Abregú. `rosenkrantz2005` tiene «pŕestamos» con tilde errónea en el título.

## Discrepancias entre notas de clase y fuentes

- Las notas dicen que en *Martín & Cía.* «ley posterior deroga ley anterior». Abregú (sección III.1) dice que la Corte consideró que la eventual responsabilidad internacional no debía alterar la aplicación de la jerarquía legal de los tratados. U08 sigue al texto.
- Las notas ubican el programa de Sofovich como «la Noche del Domingo». El fallo dice «La Noche del Sábado» (mayoría, cons. 2) o «La noche del sábado» (disidencias).
- Las notas citan como art. 27 de la Convención de Viena el fundamento del cons. 18 de la mayoría; el tomo imprime «art. 17» (errata; el texto citado es el art. 27).
- Las notas atribuyen a *Ekmekdjian* (cons. 32) un intento de «restringir cómo se va a aplicar»; el cons. 32 trata de la extensión de la respuesta. Coincide en sustancia.
