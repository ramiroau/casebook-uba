# Casebook UBA

Casebook de Elementos de Derecho Constitucional, cátedra Gargarella-Bouzat,
comisión 6661/6651. Acompaña al programa analítico y al compendio de materiales;
no los reemplaza. Estado actual: **las 18 unidades redactadas según `ESTILO.md` de noviembre de 2026** (U01–U03 revisadas; U04–U18 nuevas, ver `notas_unidades/`). Las lecturas obligatorias se reproducen extensamente por marcador; el proyecto está bajo Git (https://github.com/ramiroau/casebook-uba); la autoría de cada línea está en el historial (`git blame`) y las reglas sobre ediciones del autor, en `CLAUDE.md`.

## Compilar

    bash build_casebook.sh              # todas las unidades escritas → casebook.pdf
    bash build_casebook.sh U03          # sólo una unidad
    bash build_casebook.sh --docx       # además .docx
    bash build_casebook.sh --borrador   # admite fuentes OCR todavía no revisadas

(`bash` delante porque Google Drive no conserva el permiso de ejecución.)

Las unidades no transcriben los pasajes largos de las fuentes: los señalan con
un marcador `<!-- EXTRACTO clave … -->` que indica dónde empieza y dónde
termina el tramo. Al compilar, `scripts/insertar_extractos.py` copia el texto
desde `extractos/` en `_build/U0N.md`, que es lo que pandoc compila. La
sintaxis completa está en la cabecera del script. Para las fuentes OCR se usa
la copia corregida de `extractos/limpios/`, que debe estar marcada
`# revisado: si`.

El script corre `scripts/verificar.py` al final.

## Verificar

    python3 scripts/verificar.py [--unidades U01 U03]

Cuatro controles:

1. **citekeys** — toda clave `@foo` usada existe en `programauba.json`.
2. **citas en bloque** — cada cita textual aparece literalmente en el extracto de
   su fuente. Las que provienen de PDFs escaneados llevan `[verif. visual]` en su
   línea de atribución y se cuentan aparte: esas se cotejaron contra la imagen de
   la página, porque el OCR tiene errores de palabra.
3. **cobertura** — toda lectura obligatoria del programa para cada unidad escrita
   está citada en el archivo de esa unidad.
4. **extractos** — todo marcador de extracto se resuelve contra su fuente: las
   anclas existen y no son ambiguas, y las fuentes OCR tienen copia revisada.

## Archivos

| | |
|---|---|
| `casebook.md` | YAML y advertencia preliminar; los archivos de unidad se concatenan detrás |
| `unidades/U0N.md` | una unidad por archivo, sin YAML propio |
| `ESTILO.md` | guía de estilo en castellano, destilada del corpus propio |
| `PLANTILLA_UNIDAD.md` | estructura canónica de una unidad |
| `FUENTES.md` | mapa PDF ↔ citekey ↔ extracto ↔ paginación, y discrepancias detectadas |
| `extractos/` | texto de cada fuente, con marcadores `[[PDF p. N]]` |
| `extractos/limpios/` | copias corregidas a mano de los extractos OCR (cabecera `# revisado: si/no`) |
| `_build/` | unidades con los extractos ya insertados; se regenera en cada compilación |
| `respaldos/` | histórico, anterior a la migración a Git (21-11-2026); no se agregan archivos: las versiones anteriores están en el historial |
| `scripts/extraer.py` | `pdftotext -layout` o `tesseract -l spa` → `extractos/` (`--doble` para escaneos de dos páginas por hoja) |
| `scripts/insertar_extractos.py` | expande los marcadores `EXTRACTO` → `_build/` |
| `scripts/paginacion.py` | infiere el mapeo página de PDF → página impresa |
| `scripts/verificar.py` | control de calidad (carga además los patrones de `extractos/limpieza/<clave>.txt`) |
| `scripts/fallo_db.py` | texto de un fallo desde `csjn.db` del observatorio: OCR del tomo impreso de Fallos o PDF de la Corte |
| `notas_unidades/` | brief de la redacción en paralelo, informes y notas de fuentes de U04–U18 |
| `scripts/auditar_corpus.py` | auditoría de todos los PDFs de `Materiales_UBA` → `auditoria_corpus.json` (ver `AUDITORIA_CORPUS.md`) |
| `scripts/corpus.py` | mapea cada lectura del programa a su PDF, hace OCR donde hace falta y escribe `corpus/` y su manifiesto |
| `corpus/` | texto normalizado de todas las fuentes del programa + `manifiesto.csv` (ver `corpus/README.md`) |
| `programauba.json`, `guia-argentina-de-citas-legales.csl` | copias de `../Programa_UBA/last_version/` |

La bibliografía y el CSL son copias: la fuente sigue siendo la del programa. El
casebook no toca la cadena de compilación del programa
(`render_with_bib_preprocessing.R`, `preprocess_bib.py`).

## Agregar una unidad

1. Extraer las fuentes: `python3 scripts/extraer.py --modo texto|ocr --salida
   extractos/<citekey>.txt "<ruta al PDF>"`.
2. Anotar la fuente en `FUENTES.md` (paginación, calidad del texto, estructura de
   los fallos).
3. Si la fuente es OCR, preparar su copia en `extractos/limpios/` y corregir
   las páginas que se van a extractar contra la imagen del PDF.
4. Escribir `unidades/U0N.md` siguiendo `PLANTILLA_UNIDAD.md` y `ESTILO.md`,
   con marcadores para los extractos largos. El agente `case_book`
   (`.claude/agents/case_book.md`) hace este paso.
5. `bash build_casebook.sh`, revisar los extractos en `_build/` y que la
   verificación cierre en `OK`.
