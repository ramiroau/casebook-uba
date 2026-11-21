# Brief común para la redacción en paralelo de U04–U18 (noviembre de 2026)

Varias instancias del agente `case_book` trabajan a la vez, una por unidad.
Vale todo lo que dice `.claude/agents/case_book.md`, con estos agregados y
excepciones, que prevalecen por ser condiciones del trabajo en paralelo.

## Antes de escribir

- Leer completos `ESTILO.md` (atención a la regla nueva: **ninguna construcción
  adversativa** del tipo «Esto es A, no B», «No es B, es A», «no sólo… sino»),
  `PLANTILLA_UNIDAD.md`, `FUENTES.md`, `README.md`.
- Modelos de registro y de estructura: `unidades/U02.md` (unidad de doctrina) y
  `unidades/U03.md` (doctrina + línea jurisprudencial con fichas, votos
  titulados y extractos largos de considerandos). Imitar su estructura:
  El problema → Lectura(s) → línea jurisprudencial y Caso(s) → Notas y
  preguntas → Síntesis → Para seguir leyendo. Las «Preguntas que guían la
  lectura» se integran a las Notas y preguntas (como en U02/U03).
- Título y copete: literales de `../Programa_UBA/last_version/programa_uba_v25.md`.
- Tu unidad no existe todavía: no hay ediciones del autor que conservar.

## Fuentes

- Texto normalizado de todas las fuentes del programa: `corpus/texto/<id>.txt`
  (mismo formato `[[PDF p. N]]` que `extractos/`). Ver `corpus/manifiesto.csv`
  (columnas `nivel`, `via`, `paginacion`, `notas`) y `corpus/README.md`.
- Para extractar una fuente, copiarla a `extractos/<citekey>.txt` y ajustar la
  cabecera: `# modo: texto` si es nivel A (texto nativo); `# modo: ocr` si es
  B o C. Las OCR exigen `extractos/limpios/<citekey>.txt` corregido contra la
  imagen **sólo en las páginas que se extractan** y marcado `# revisado: si`.
  Imagen: `corpus/pdf/<id>.pdf` si existe, si no el original en
  `../Materiales_UBA/` (nunca modificar los originales). Leer páginas con Read
  y `pages`.
- **Fallos de la CSJN**: la base `~/Documents/observatorio-csjn/data/csjn.db`
  (sólo lectura) sirve para (a) confirmar la cita de Fallos (`caso`), (b)
  identificar el holding con los sumarios (`sumario`, campo `texto`) y (c)
  obtener un texto mejor. `python3 scripts/fallo_db.py TOMO PAGINA --salida
  …` saca el OCR del **tomo impreso de Fallos** (muy superior a los escaneos
  del compendio para fallos viejos; `[[PDF p. N]]` = página impresa de Fallos)
  o, con `--fuente documento`, el texto del PDF de la Corte (bueno para fallos
  recientes). Elegir el mejor texto para cada fallo; si se usa el del tomo,
  queda `# modo: ocr` y hay que revisar las páginas extractadas (el OCR es
  bueno: corregir errores puntuales y cotejar con la imagen del compendio
  cuando haya dudas). El texto siempre se extrae de la decisión.
- Fuentes compartidas entre unidades — no las extracte quien no es dueño:
  - `csjn_rizzo2013`: dueña U13 (en U05 es optativa: sólo bibliografía).
  - `saenz2016b`: dueña U11. En U06 el PDF asignado es otro texto
    («Artículos 14 y 28»): usar clave de extracto `saenz2016_art14y28`
    (texto en `corpus/texto/saenz2016_art14y28.txt`), citar `[@saenz2016b]`
    para que la cobertura cierre y anotar la discrepancia.
  - En U10 el PDF de Arballo es el comentario al art. 75 inc. 13: clave de
    extracto `arballo2019_art75inc13`, cita `[@arballo2019]`, discrepancia
    anotada. En U07 `arballo2019` (art. 121) es optativa: sólo bibliografía.
- Política de lecturas: las **obligatorias** se reproducen extensamente por
  marcador (preferencia absoluta por extractos largos, varias páginas; en
  fallos, los considerandos que sostienen el holding de cada voto relevante,
  en bloques largos). Las **optativas** van sólo en «Para seguir leyendo»,
  con citekey y casi sin descripción; las que no tienen PDF, marcadas
  «(sin PDF en la carpeta)». Si en una unidad un fallo optativo es
  indispensable para la línea jurisprudencial, puede describirse en prosa
  con citekey, sin extracto.
- Si una fuente obligatoria es ilegible y no se puede corregir en tiempo
  razonable, no forzar: encuadrarla y dejar `[PENDIENTE: …]`.

## Recursos compartidos: reglas de convivencia

- **No correr `build_casebook.sh`** (borra `_build/` y pisa `casebook.pdf`
  de los demás). Para probar: `python3 scripts/insertar_extractos.py
  --unidades U0N --salida <tu scratchpad>/U0N` y `python3 scripts/verificar.py
  --unidades U0N`. Revisar los párrafos en la salida.
- **No editar** `scripts/*.py`, `FUENTES.md`, `README.md`, `casebook.md`,
  `programauba.json`, `ESTILO.md`, ni archivos de otras unidades.
- Patrones de limpieza (encabezados, pies, carátulas): en
  `extractos/limpieza/<citekey>.txt`, un regex por renglón, comentarios con
  `#`. `verificar.py` los carga solos. Cuidado: los patrones se aplican a
  **todas** las fuentes; anclarlos bien (`^\s*…\s*$`, texto específico).
- Lo que iría en `FUENTES.md` (filas de la tabla de fuentes, estado de
  `limpios/`, discrepancias con `programauba.json`) va en
  `notas_unidades/U0N_fuentes.md`, con el mismo formato de tablas. El
  coordinador lo integra después.
- El informe final (formato de la sección «Informe final» del agente) va
  también en `notas_unidades/U0N_informe.md`.
- Al terminar, copiar la unidad a `respaldos/U0N_agente.md`.

## Detalles técnicos aprendidos en U01–U03

- `ocurrencia: N` debe ir **antes** del `desde` al que se aplica; en los fallos
  cada voto repite considerandos, usar `despues:` u `ocurrencia:`.
- Un renglón que contiene sólo un número se toma como inicio de las notas al
  pie y corta la página: en `limpios/` borrarlo; en fuentes de texto, si
  corta un extracto, agregar el patrón de limpieza correspondiente o elegir
  otras anclas.
- Encabezados de votos dentro de un caso: `####` (un quinto nivel se imprime
  en línea con el texto).
- Citekeys: sólo las de `programauba.json`. No inventar.
- Prosa propia breve; no rellenar para alcanzar el objetivo de palabras.
- Trabajar sin hacer preguntas: decidir con criterio y dejar las decisiones
  anotadas en el informe.
