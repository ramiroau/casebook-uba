# corpus/

Capa normalizada de las fuentes del programa. Se genera con
`python3 scripts/corpus.py` y nunca toca `../Materiales_UBA/` ni `extractos/`.

| | |
|---|---|
| `manifiesto.csv` / `.json` | una fila por aparición (unidad, citekey) en `programa_uba_v25.md` |
| `texto/<id>.txt` | texto de la fuente, con `[[PDF p. N]]` = página del **PDF original** |
| `pdf/<id>.pdf` | copia con capa OCR (sólo las fuentes que la necesitaron) |
| `pdf/<id>.mapa.json` | página del PDF con OCR → (página original, lado) |

En los escaneos a doble página, cada mitad lleva el marcador de su página
original, seguido de `<!-- izq -->` o `<!-- der -->`.

## Columnas del manifiesto

- `unidad`, `citekey`, `caracter` (obligatoria/optativa), `tipo_bib`, `autor`,
  `anio`, `titulo`: según el programa y `programauba.json`.
- `id_fuente`: nombre del texto en `texto/`. Es el citekey, salvo cuando el PDF
  no corresponde a la entrada (p. ej. `saenz2016_art14y28`).
- `pdf_original`, `md5`, `paginas`, `tipo_pdf`: el archivo de `Materiales_UBA`.
  Si el md5 cambia, la fuente cambió y hay que regenerar.
- `via`: `texto` · `conservar` (OCR previo aceptable) · `ocr` · `ocr-forzado`
  (capa basura o fuentes rotas) · `partir+ocr` (doble página) · `conseguir PDF`.
- `calidad_original` / `calidad_final`: puntaje heurístico 0–100 (palabras
  funcionales del castellano, penalización por letras sueltas y mezclas
  letra-dígito). **Sirve para ordenar, no para certificar**: el OCR de *Siri*
  puntúa 93 y es ilegible.
- `nivel`:
  - `A`: texto nativo limpio.
  - `B`: OCR aceptable, sin revisar.
  - `C`: original deficiente o puntaje bajo.
  - `falta`: no hay PDF.
- `revisado`: `si` cuando hay copia corregida contra la imagen.
- `paginas_debiles`: páginas originales con puntaje < 70.
- `paginacion`: regla para convertir la página del PDF en la página impresa,
  cuando se conoce.
- `notas`: problemas bibliográficos y de la fuente.

## Límites conocidos

- En los escaneos a doble página de libros encuadernados (*Kot*, *Ercolano*,
  *Prattico*, *Elías*), las últimas letras junto al lomo están deformadas en el
  original. El OCR las pierde aunque el corte sea correcto.
- El OCR no conserva cursivas ni distingue notas al pie del cuerpo.
