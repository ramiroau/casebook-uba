#!/usr/bin/env bash
# build_casebook.sh — compila el casebook a PDF.
#
#   ./build_casebook.sh              todas las unidades escritas
#   ./build_casebook.sh U03          sólo la unidad 3
#   ./build_casebook.sh --docx       además genera .docx
#   ./build_casebook.sh --borrador   admite OCR sin revisar
#
# Los pasajes largos de las fuentes no están transcritos en unidades/: cada
# unidad los señala con un marcador <!-- EXTRACTO … --> y
# scripts/insertar_extractos.py los copia desde extractos/ en _build/, que es
# lo que efectivamente se compila. Con --borrador se aceptan fuentes OCR
# todavía no revisadas (con una advertencia visible en el texto).
#
# La bibliografía es la del programa (programauba.json) y el estilo de cita es
# la Guía Argentina de Citas Legales. El casebook sólo lee esos archivos: la
# cadena de compilación del programa no se toca.

set -euo pipefail
cd "$(dirname "$0")"

DOCX=0
BORRADOR=()
PEDIDAS=()
for arg in "$@"; do
  case "$arg" in
    --docx)     DOCX=1 ;;
    --borrador) BORRADOR=(--borrador) ;;
    *)          PEDIDAS+=("$arg") ;;
  esac
done

rm -rf _build
python3 scripts/insertar_extractos.py --salida _build \
  ${PEDIDAS[@]+--unidades "${PEDIDAS[@]}"} ${BORRADOR[@]+"${BORRADOR[@]}"}

UNIDADES=()
# orden numérico, no alfabético
while IFS= read -r f; do UNIDADES+=("$f"); done < <(ls _build/U*.md | sort)

echo "→ unidades: ${UNIDADES[*]}"

COMUNES=(
  casebook.md "${UNIDADES[@]}"
  --from=markdown
  --citeproc
  --bibliography=programauba.json
  --csl=guia-argentina-de-citas-legales.csl
  --resource-path=.
)

pandoc "${COMUNES[@]}" \
  --pdf-engine=xelatex \
  -V mainfont="Times New Roman" \
  -V geometry:margin=2.7cm \
  -o casebook.pdf

echo "→ casebook.pdf"

if [ "$DOCX" -eq 1 ]; then
  pandoc "${COMUNES[@]}" -o casebook.docx
  echo "→ casebook.docx"
fi

python3 scripts/verificar.py || echo "(la verificación reportó problemas)"
