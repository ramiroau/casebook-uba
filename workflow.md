# Flujo de trabajo para producir el casebook

Este documento describe cómo debería trabajar el equipo de autores para
producir una nueva edición del casebook de Elementos de Derecho Constitucional,
desde el programa hasta el PDF que se entrega a los estudiantes. Recoge lo
aprendido en la redacción de noviembre de 2026, en la que las dieciocho
unidades se escribieron en una sola ronda. Ese proceso dejó tres lecciones.
Los errores de bibliografía salen caros si se detectan tarde. Las decisiones
de contenido (qué considerandos, qué votos) conviene tomarlas antes de
redactar. Y la revisión de las fuentes escaneadas es el verdadero cuello de
botella.

El principio que ordena todo lo demás es simple: **cada decisión se toma una
sola vez, en el lugar adecuado, y queda escrita.** Las decisiones sobre las
fuentes se registran en el manifiesto, las de contenido en la ficha de la
unidad, las de estilo en `ESTILO.md` y las de bibliografía en Zotero.

---

## 1. Herramientas

| Necesidad | Herramienta | Por qué |
|---|---|---|
| Texto de las unidades, scripts, extractos | **Repositorio Git en GitHub** (privado) | Historial completo, autoría de cada cambio (`git blame`), revisión por *pull request*, trabajo en paralelo sin pisarse |
| PDFs originales y escaneos | **Google Drive** (`Materiales_UBA/`, sólo lectura) | Son pesados y no cambian; Git no los necesita. El repo guarda sólo `corpus/texto/` y el manifiesto |
| Bibliografía | **Biblioteca de grupo en Zotero** + Better BibTeX con exportación automática a `programauba.json` | Una sola fuente de verdad para citekeys; nadie edita el JSON a mano |
| Edición | **VS Code** (con la extensión de GitHub) o el editor web de GitHub para quien no quiera instalar nada | Markdown con vista previa; los comentarios `<!-- -->` quedan visibles |
| Redacción asistida | **Claude Code** con el agente `case_book` y los scripts de `scripts/` | Borradores, extractos y verificación; el autor decide y corrige |
| Control automático | **GitHub Actions**: `verificar.py` y `build_casebook.sh` en cada *pull request* | Ninguna unidad entra con anclas rotas, citekeys inexistentes o lecturas obligatorias sin citar |
| Lectura y comentario del PDF | **PDF del build adjunto a cada *pull request*** (artefacto de Actions) + comentarios en la PR | El revisor comenta sobre lo que leerá el estudiante, no sobre el Markdown |
| Coordinación | **GitHub Projects** (tablero) + *issues* con plantillas | Un issue por unidad y por fuente problemática; el tablero muestra el estado de todo |
| Discusión rápida | Un canal de chat del equipo, y una reunión semanal de 30 minutos | Lo que se decide en el chat se copia al issue correspondiente; si no, no existe |

### Migración del estado actual

Hoy el proyecto vive en una carpeta de Google Drive sin control de versiones.
La regla de `CLAUDE.md` sobre ediciones del autor (los marcadores
`<!-- AUTOR -->` y los `respaldos/U0N_agente.md`) reemplaza a mano lo que Git
hace solo. Pasos:

1. Crear el repositorio con el contenido actual, excluyendo `_build/`,
   `casebook.pdf` y `corpus/pdf/` (`.gitignore`).
2. Primer commit: el estado actual tal cual. Segundo commit: quitar los
   marcadores `AUTOR` (la autoría pasa a estar en el historial).
3. Desde ahí, `respaldos/` deja de crecer: cada versión es un commit.
4. Actualizar `CLAUDE.md`. Las ediciones del autor pasan a ser los commits
   firmados por autores humanos. El agente trabaja siempre en una rama propia
   y nunca reescribe líneas cuyo último autor es humano sin que se lo pidan
   (`git blame` lo muestra).

---

## 2. Roles

Nadie necesita ser experto en todo. Cuatro roles, que una misma persona puede
acumular:

- **Editor general.** Es dueño del programa, de `ESTILO.md` y de
  `PLANTILLA_UNIDAD.md`. Fija prioridades, aprueba las fichas de unidad y hace
  la lectura final de corrido. Es el único que aprueba cambios a las reglas
  comunes.
- **Responsable de unidad.** Cada unidad tiene un responsable, asignado en
  `.github/CODEOWNERS`, cuya aprobación es obligatoria para fusionar cambios a
  `unidades/U0N.md`. Decide el contenido, revisa el borrador y responde por la
  unidad frente a la cátedra.
- **Revisor de fuentes.** Coteja contra la imagen el OCR de las páginas que se
  extractan y marca `# revisado: si`. Es tarea mecánica y paralelizable: sirve
  para ayudantes y adscriptos.
- **Técnico.** Mantiene los scripts, el CI y la exportación de Zotero, y
  resuelve los problemas de compilación.

---

## 3. El flujo, fase por fase

```
 0. Programa         1. Inventario       2. Bibliografía     3. Fichas
 congelado     →     y triage       →    saneada        →    de unidad
                                                               │
 7. Uso y      ←     6. Edición     ←    5. Redacción   ←    4. Fuentes
 retroalim.          final               y revisión          listas
```

Las fases 2, 3 y 4 corren en paralelo entre sí; la redacción de una unidad
empieza recién cuando su ficha está aprobada y sus fuentes están listas.

### Fase 0. Congelar el programa (semana 1)

- El editor general fija la versión del programa (`programa_uba_vNN.md`) y la
  etiqueta en el repo. A partir de ahí, título, copete y lecturas obligatorias
  de cada unidad no cambian durante la edición.
- Todo cambio posterior al programa entra como issue con la etiqueta
  `programa` y se aplica en la edición siguiente, salvo decisión expresa.

### Fase 1. Inventario y triage de materiales (semanas 1–2)

Objetivo: saber, antes de escribir una línea, qué fuentes hay, en qué estado y
cuánto trabajo exige cada unidad.

1. Correr la auditoría del corpus y regenerar `corpus/manifiesto.csv`. Para
   cada fuente: nivel (A texto nativo, B OCR bueno, C OCR malo o ilegible),
   vía de obtención y paginación.
2. Para los fallos de la CSJN, consultar siempre la base del observatorio
   (`scripts/fallo_db.py`). El tomo impreso de Fallos es casi siempre mejor que
   el escaneo del compendio, y la tabla `caso` confirma la cita.
3. Armar en el tablero un **semáforo por unidad** con tres datos: cuántas
   lecturas obligatorias tiene, cuántas son nivel C y si hay fallos sin fuente
   utilizable.
4. Con el semáforo, el editor general fija el orden de trabajo. Primero van
   las unidades que se dictan antes en el cuatrimestre. Entre las demás, se
   adelantan las de fuentes difíciles, porque su revisión de OCR es lo que más
   tarda y conviene arrancarla temprano.

**Entregable:** tablero con dieciocho issues de unidad, cada uno con semáforo,
responsable y fecha.

### Fase 2. Bibliografía saneada (semanas 1–3, en paralelo)

En la ronda de 2026 aparecieron, con todo ya escrito:

- claves duplicadas;
- una entrada de *Marbury* con el resumen de *Luther v. Borden*;
- citas de Fallos equivocadas o faltantes;
- citekeys que apuntaban a textos distintos de los PDF asignados.

Todo esto se corrige **antes** de redactar:

1. Importar `programauba.json` a la biblioteca de grupo de Zotero y activar la
   exportación automática con Better BibTeX en CSL-JSON. El archivo del repo
   pasa a ser un producto de Zotero.
2. Revisión cruzada, una persona por bloque de unidades:
   - cada entrada contra el PDF que la carpeta asigna (¿es el mismo texto?);
   - cada fallo contra la base del observatorio (tomo, página, fecha);
   - las páginas de cada capítulo contra el índice del libro.
3. Las discrepancias se resuelven en Zotero, nunca con claves de extracto
   alternativas como `saenz2016_art14y28`, salvo que el programa mismo asigne
   dos textos a una misma referencia.
4. Regla de citekeys: `autorAÑOletra` para doctrina, `csjn_carátulaAÑO` para
   fallos. Las claves no se renombran una vez publicadas.

**Entregable:** `programauba.json` sin duplicados y con una entrada por cada
PDF del programa. Un CI que falla si aparece una clave duplicada.

### Fase 3. Fichas de unidad: decidir antes de redactar (semanas 2–4)

Es la fase que más tiempo ahorra después. En 2026 los agentes eligieron
considerandos y estructuras por su cuenta. El resultado fue razonable, pero
cada elección hubo que revisarla y algunas chocaban con lo que se dice en
clase. Ahora la decisión la toma el responsable, en una página, antes del
borrador.

Cada responsable completa `notas_unidades/U0N_ficha.md`, con esta estructura:

```markdown
# U0N — Ficha de decisiones

## El problema de la unidad (2–3 oraciones)
¿Qué pregunta tiene que poder responder el estudiante al terminar?

## Lecturas obligatorias y qué se toma de cada una
| Citekey | Tramo a extractar (páginas o considerandos) | Para qué está |
|---|---|---|

## Línea jurisprudencial
Orden de los fallos y la tesis que los une, en una línea por fallo.
Votos que se reproducen (mayoría, disidencias, concurrencias) y por qué.

## Lo que se dice en clase y no está en las lecturas
Puntos de las notas de clase que la unidad debe recoger o, si contradicen
la fuente, señalar.

## Preguntas que no pueden faltar
Tres a cinco, las que el responsable usaría en un examen.

## Fuera de la unidad
Lo que se deja deliberadamente para otra unidad o para «Para seguir leyendo».
```

- La ficha se discute en la reunión semanal y la aprueba el editor general.
- Se revisa además el **mapa de dependencias entre unidades**: qué fallo
  pertenece a qué unidad (en 2026, *Rizzo* fue de U13 y aparece en U05 sólo
  como referencia) y qué conceptos se definen dónde. Así cada unidad sabe a
  cuáles remite y cuáles la presuponen.

**Entregable:** dieciocho fichas aprobadas y un mapa de dependencias en
`notas_unidades/MAPA.md`.

### Fase 4. Fuentes listas para extractar (semanas 2–6, en paralelo)

Con las fichas aprobadas se sabe exactamente qué páginas se van a reproducir,
y por lo tanto qué páginas hay que revisar. En 2026 se revisaron páginas que
después no se usaron.

1. Para cada tramo de la ficha, el técnico (o el agente) genera
   `extractos/<citekey>.txt` con `extraer.py` o `fallo_db.py`. Se usa la mejor
   fuente disponible; para fallos posteriores a ~1995, el PDF de la Corte.
2. Se abre un issue de revisión por cada fuente OCR, con la lista de páginas
   exactas que deben revisarse.
3. El revisor de fuentes coteja el OCR contra la imagen y corrige en
   `extractos/limpios/`. Al terminar marca `# revisado: si` y anota en la
   cabecera qué páginas cotejó y cómo. La convención es fija:
   - `visual`: contra la imagen;
   - `segundo OCR`: contra una segunda lectura automática;
   - `contexto`: reconstruido sin imagen.
   Lo que no es `visual` aparece como advertencia en el informe de la unidad.
4. Los patrones de limpieza van en `extractos/limpieza/<citekey>.txt`, bien
   anclados.
5. Trucos aprendidos:
   - un renglón con sólo un número corta la página como si empezaran las
     notas: hay que borrarlo en `limpios/`;
   - `# revisado: si` va antes de cualquier línea de cabecera con `[[PDF`;
   - en los fallos, cada voto repite los números de considerando, así que se
     usan `despues:` u `ocurrencia:` para desambiguar.

**Mejora técnica pendiente**, a resolver en esta fase:

- aplicar los patrones de limpieza **antes** del corte de notas al pie;
- admitir reemplazos, además de borrados, en `extractos/limpieza/`.

Con eso desaparecen las correcciones manuales que hicieron falta en 2026, por
ejemplo en *Mouviel* y en *Colegio de Abogados*.

**Entregable:** todas las fuentes de cada ficha resuelven sus marcadores en
modo normal (sin `--borrador`).

### Fase 5. Redacción y revisión, unidad por unidad (semanas 4–10)

Cada unidad sigue el mismo circuito, en una rama propia:

```
rama u0N  →  borrador (agente + ficha)  →  PR  →  CI verde  →
revisión de contenido (responsable)  →  revisión cruzada (otro autor)  →
fusión a main
```

1. **Borrador.** El responsable lanza el agente `case_book` sobre la rama,
   pasándole la ficha aprobada como instrucción principal. El agente respeta la
   ficha. Si se aparta, lo anota en `U0N_informe.md`, que viaja en la misma PR.
   - Las unidades se redactan **de a una por agente**, en el orden del
     tablero. La experiencia de 2026 muestra que lanzar quince agentes juntos
     agota los límites de uso a mitad de camino y obliga a retomar todo.
   - Dos o tres unidades simultáneas, cada una con su responsable atento, es
     el máximo razonable.
2. **CI.** La PR corre `verificar.py` sobre la unidad y compila el PDF de esa
   unidad sola. Si algo falla, no se pide revisión humana.
3. **Revisión de contenido.** El responsable lee **el PDF**, no el Markdown,
   con la ficha al lado. Se fija en tres cosas:
   - que los extractos sostengan el holding;
   - que la prosa propia oriente sin resumir lo que el estudiante va a leer;
   - que las preguntas sean las de la ficha o mejores.
   Corrige directamente en la rama: sus commits son las ediciones del autor.
4. **Revisión cruzada.** Otro autor, idealmente el responsable de una unidad
   vecina en el mapa de dependencias, lee con una lista breve:
   - ¿la unidad remite bien a las anteriores y no repite lo que ya está en
     ellas?
   - ¿hay construcciones adversativas o tics que `ESTILO.md` prohíbe?
   - ¿algún término se usa distinto que en otra unidad?
   - ¿la extensión es la adecuada? No se rellena para llegar a un número de
     palabras.
5. **Fusión.** Con las dos aprobaciones y el CI verde, se fusiona. El issue de
   la unidad pasa a «Lista» en el tablero.

**Regla de oro para el agente y para los humanos:** una PR toca una sola
unidad. Los cambios a reglas comunes (estilo, plantilla, scripts) van en PRs
propias, las aprueba el editor general y nunca se mezclan con contenido.

### Fase 6. Edición final (semanas 11–12)

1. **Lectura de corrido.** El editor general lee el PDF completo de principio a
   fin, en papel o tableta, y anota con un color por tipo de problema: remisión
   rota, repetición, salto de registro, error de fuente. Cada anotación se
   vuelve un issue chico, asignado al responsable de la unidad.
2. **Barrido mecánico.** Se buscan, en todo el casebook a la vez:
   - placeholders: `???`, `[PENDIENTE`, `TODO`;
   - citekeys no usadas o usadas una sola vez;
   - uniformidad de las fichas de los fallos.
3. **Edición etiquetada.** Se crea la etiqueta `edicion-2027-1c`. El CI publica
   en el *release* de GitHub el PDF (y el `.docx` si la cátedra lo pide) y el
   PDF va a la carpeta de la cátedra en Drive.
4. **Notas de la edición.** Una página con lo que cambió respecto de la
   edición anterior, generada a partir de los títulos de las PRs fusionadas.

### Fase 7. Uso en el curso y retroalimentación (durante el cuatrimestre)

- Un formulario breve, enlazado desde la advertencia preliminar del PDF, para
  que estudiantes y docentes reporten erratas. Cada respuesta se convierte en
  un issue con la etiqueta `errata` (el paso puede automatizarse).
- Las erratas se corrigen en la rama principal y se publica una edición menor
  (`edicion-2027-1c.1`) cuando se juntan varias, nunca a mitad de una unidad
  que se está dictando.
- **Retrospectiva** al cierre del cuatrimestre, en una reunión de una hora:
  - qué unidades funcionaron en clase y cuáles no;
  - qué preguntas usaron los docentes;
  - qué lecturas habría que cambiar.
  Lo que salga alimenta la fase 0 del programa siguiente.

---

## 4. Calendario modelo (doce semanas antes del inicio de clases)

| Semana | Programa y bibliografía | Fichas | Fuentes | Redacción | Edición |
|---|---|---|---|---|---|
| 1 | Programa congelado · Zotero | | Inventario y semáforo | | |
| 2 | Revisión cruzada de la bibliografía | U01–U06 | Fuentes de U01–U06 | | |
| 3 | JSON saneado | U07–U12 | Fuentes de U07–U12 | | |
| 4 | | U13–U18 · mapa | Fuentes de U13–U18 | U01–U03 | |
| 5–6 | | | Revisión OCR (continúa) | U04–U09 | |
| 7–8 | | | | U10–U15 | |
| 9–10 | | | | U16–U18 · pendientes | |
| 11 | | | | | Lectura de corrido |
| 12 | | | | | Barrido · edición etiquetada |

Las unidades del principio del cuatrimestre pueden publicarse antes, en una
edición parcial, si el calendario aprieta.

---

## 5. Definición de «terminado» para una unidad

Una unidad está terminada cuando se cumplen todas estas condiciones:

- [ ] Su ficha fue aprobada y la unidad la respeta, o el informe explica cada
  apartamiento.
- [ ] `verificar.py --unidades U0N` no da errores ni advertencias.
- [ ] Todas sus fuentes OCR están revisadas, y las que no lo fueron contra la
  imagen figuran como advertencia en el informe.
- [ ] No quedan `???`, `[PENDIENTE` ni citekeys inexistentes.
- [ ] Tiene la aprobación del responsable y de un revisor cruzado.
- [ ] Compila sola y dentro del casebook completo sin romper la numeración ni
  los encabezados.

---

## 6. Lo que no hay que repetir

Errores de la ronda de 2026, convertidos en reglas:

1. **Bibliografía al final.** Los errores de `programauba.json` se detectaron
   con las unidades ya escritas. → Fase 2 antes de redactar.
2. **Decisiones de contenido delegadas.** El agente eligió los considerandos y
   después hubo que revisar cada elección. → Ficha aprobada antes del
   borrador.
3. **Agentes masivos en paralelo.** Quince agentes simultáneos agotaron los
   límites de uso dos veces. → De a una unidad por agente, en orden.
4. **Autoría reconstruida a mano.** Los marcadores `AUTOR` y los respaldos
   reemplazaban a un control de versiones. → Git.
5. **Revisión de páginas que no se usan.** → Revisar sólo las páginas que la
   ficha manda extractar.
6. **Notas de clase que contradicen la fuente, descubiertas en el borrador.**
   → Sección específica en la ficha; la unidad sigue la fuente y lo dice.
7. **Correcciones mecánicas a mano en los extractos.** → Arreglar el script
   (limpieza antes del corte de notas; reemplazos en `limpieza/`).
