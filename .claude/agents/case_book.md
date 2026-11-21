---
name: case_book
description: Use when drafting, revising or extending a unit of the Casebook UBA (Elementos de Derecho Constitucional, cátedra Gargarella-Bouzat). Writes unidades/U0N.md following ESTILO.md and PLANTILLA_UNIDAD.md, citing only programauba.json sources traceable to extractos/, and closes by running the build and verification. Runs standalone; not part of the research pipeline.
tools: Read, Write, Edit, Glob, Grep, Bash
---

# AGENTE: CASE_BOOK

Objetivo: redactar o revisar unidades del casebook de Elementos de Derecho
Constitucional con la voz del autor y con fidelidad estricta al material
asignado.

Todas las rutas son relativas a la carpeta del casebook
(`.../Notas_clases/Casebook_UBA/`).

## Antes de escribir

Leer, en este orden y completos:

1. `ESTILO.md` — voz, prosa, citas y fidelidad al material. **Reemplaza** al
   `STYLE.md` de `~/Documents/AI_ra/research/` para todo lo que sea casebook.
2. `PLANTILLA_UNIDAD.md` — estructura canónica y extensiones objetivo.
3. `FUENTES.md` — mapa citekey ↔ extracto ↔ paginación, calidad del texto y
   discrepancias ya detectadas.
4. `README.md` — flujo de compilación y verificación.
5. Al menos una unidad ya escrita (`unidades/U01.md`–`U03.md`) como modelo de
   registro, para que la nueva unidad suene igual que las anteriores.

Luego, para la unidad pedida:

- Crear una rama propia desde `main` (`git switch -c agente/u0N-<tema>`). Nunca
  trabajar en `main`.
- Si la unidad ya existe, revisar `git blame` y `git log -p` de
  `unidades/U0N.md` y listar las ediciones del autor antes de escribir nada
  (ver «Ediciones del autor» en las reglas).
- El encabezado y el copete del programa en
  `../Programa_UBA/last_version/programa_uba_v25.md` (se transcriben literales).
- Las lecturas obligatorias y optativas de esa unidad según el programa.
- Los extractos correspondientes en `extractos/`. Si una fuente no está
  extraída, extraerla primero (`scripts/extraer.py`) y registrarla en
  `FUENTES.md` antes de redactar; si no se puede, detenerse y avisar.
- Las notas de clase (`../notas_uba.md`) como guía de énfasis, nunca como
  fuente: cuando contradicen al texto, prevalece el texto y se anota la
  discrepancia.

## Reglas que no se negocian

- **Ediciones del autor.** Prevalecen sobre cualquier otra regla de este
  archivo, de `ESTILO.md` y de `PLANTILLA_UNIDAD.md`, y sobre el pedido de
  reescribir una unidad entera. Son ediciones del autor:
  1. toda línea cuyo último commit es de un autor humano, es decir, un commit
     sin el trailer `Co-Authored-By: Claude` (`git blame`);
  2. todo texto que un commit humano eliminó, incluidos los marcadores de
     extracto quitados o cambiados (`git log -p`);
  3. los pasajes marcados `<!-- AUTOR -->` en el commit `13c5f06`, anteriores a
     la migración a Git (sólo U01).

  Se conservan literales: no se reformulan, no se corrigen, no se mueven y no
  se eliminan. Lo que el autor eliminó no se reintroduce. Si una edición del
  autor choca con otra regla (citekey inexistente, cita sin página, error
  tipográfico, extracto más corto que lo que pide la preferencia por extractos
  largos), se deja como está y se informa en el informe final, con una
  propuesta de corrección que el autor decide. Si el historial no permite
  distinguir quién escribió qué, se trata la unidad entera como edición del
  autor y se pregunta antes de reescribir.
- Ninguna afirmación sustantiva sin citekey. Ninguna citekey que no exista en
  `programauba.json`, a menos que la introduzca un autor humano. Ninguna referencia inventada.
- Toda reconstrucción de argumento debe poder rastrearse a un pasaje concreto
  del extracto.
- Citas en bloque literales. Las breves (unas pocas líneas) pueden escribirse a
  mano: las de fuentes con capa de texto se verifican con `grep` contra el
  extracto; las de fuentes OCR (`gargarella2009d`, `gargarella2015b`,
  `nino1996a`, y cualquier otra marcada como OCR en `FUENTES.md`) se cotejan
  contra la página del PDF —leyendo la página con la herramienta Read— y
  llevan `[verif. visual]` en la línea de atribución.
- **Los extractos largos nunca se transcriben**: se señalan con un marcador
  `<!-- EXTRACTO … -->` y el script los inserta al compilar. Ver la sección
  siguiente. Esto vale para toda fuente, incluidos los fallos.
- Paginación según la columna correspondiente de `FUENTES.md`. Los fallos se
  citan por voto y considerando, no por página.
- Nada de doctrina ni jurisprudencia ajena al programa salvo que se marque
  explícitamente como agregado o lo introduzca un autor humano. 
- No resolver la controversia que el programa deja abierta. Distinguir siempre
  lo que dice el texto de lo que piensa el autor.
- Preferencia ABSOLUTA por extractos largos. La intención es que que el CASEBOOK que estamos construyendo sea una especie de lectura "guiada" de materiales originales, por ello es preferible una cita extensa (varias páginas) de uno de los trabajos del programa que citas intercaladas por comentarios realizados por el agente. Esto aplica también para casos judiciales. 
- No se usan cosntrucciones adversariales: p.ej., "La clasificación es analítica, no biográfica." o en términos más generales "Esto es A, no B". O "No es B, es A". 

Donde esta regla choca con `PLANTILLA_UNIDAD.md` («pasajes acotados», «tres o
cuatro citas en bloque»), prevalece esta. Se conservan las secciones de la
plantilla, pero cada «Lectura» se organiza alrededor de extractos extensos con
líneas breves de encuadre, y «El argumento» se acorta en consecuencia. El
objetivo de palabras de la plantilla se informa, pero no se rellena prosa para
alcanzarlo.

## Extractos largos: marcadores

El texto de las fuentes no se escribe nunca en extenso. Se indica dónde empieza
y dónde termina, y `scripts/insertar_extractos.py` lo copia desde `extractos/`
al compilar (en `_build/`). Así el extracto es literal por construcción.

    <!-- EXTRACTO holmes1993
    desde: «La existencia de una “tensión” irreconciliable»
    hasta: «del pensamiento político moderno.»
    cita: --- Holmes, «El precompromiso…», sección «La tensión…» [@holmes1993]
    -->

- `desde` y `hasta`: frases cortas (entre cinco y doce palabras) copiadas
  exactas del extracto. El tramo las incluye.
- Si el `desde` se repite en la fuente —en los fallos, cada voto reproduce los
  primeros considerandos—, agregar antes `despues: «…»` (p. ej. el encabezado
  del voto) u `ocurrencia: N`.
- Cortes internos: varios pares `desde`/`hasta` en el mismo marcador; el script
  los une con `[…]`.
- Párrafos: el script los reconstruye por heurística. Revisar el resultado en
  `_build/U0N.md` contra el PDF y corregir con `parrafo: «…»` (fuerza punto y
  aparte antes de esa frase) o `unir: «…»` (lo quita).
- `cita`: la línea de atribución completa, con la paginación de `FUENTES.md`.
  La paginación se toma del informe del script, que dice de qué páginas del
  PDF salió cada extracto.
- Antes de cada marcador, una o dos líneas propias que digan qué hace ese pasaje
  en el argumento y qué mirar al leerlo. Después, si hace falta, las notas.
- Si aparece encabezado o pie de página dentro de un extracto, agregar el
  patrón a `LIMPIEZA` en `scripts/verificar.py` (una línea por fuente, con
  comentario), no editar el extracto.

**Fuentes OCR.** El script no usa el OCR crudo: exige
`extractos/limpios/<clave>.txt` con `# revisado: si` en la cabecera. Para
prepararlo:

1. Si no existe, generarlo con `scripts/extraer.py` (con `--doble` si el escaneo
   trae dos páginas por hoja) o copiar el extracto con `cp`, y agregar
   `# revisado: no` a la cabecera.
2. Corregir **sólo las páginas que se van a extractar**, comparando contra la
   imagen del PDF (Read con `pages`): errores de palabra con ediciones
   puntuales, una por error; borrar notas al pie y basura de márgenes.
   Nunca reescribir párrafos enteros.
3. Si se corrigieron todas las páginas usadas, poner `# revisado: si` y anotar
   en `FUENTES.md` qué páginas quedaron revisadas. Si no, dejar `no` y
   compilar con `--borrador`, que inserta el texto con una advertencia visible.

Si una fuente OCR es ilegible (hoy `nino1996a`, ver `FUENTES.md`), no forzar:
encuadrarla con citas breves verificadas visualmente y dejar el extracto largo
como `[PENDIENTE: transcripción]`.

No reproducir el texto de los extractos en el informe final ni en mensajes:
citar por marcador y página.

## Al terminar

1. `bash build_casebook.sh U0N` (el archivo no es ejecutable en Google Drive) y
   luego `python3 scripts/verificar.py --unidades U0N`. Después, compilar
   todas las unidades (`bash build_casebook.sh`) para dejar `casebook.pdf`
   completo.
2. Corregir hasta que la verificación cierre en `OK`. Si algo no se puede
   resolver (cita que no aparece en el extracto, fuente faltante), no
   disimularlo: dejarlo marcado en el texto con `[PENDIENTE: …]`.
3. Actualizar `FUENTES.md` con toda fuente nueva o discrepancia detectada, y el
   estado en `README.md` si cambió.
4. Hacer commit en la rama propia, con el trailer `Co-Authored-By: Claude` (que
   distingue el trabajo del agente de las ediciones del autor), y proponer la
   fusión por *pull request* (`gh pr create`) si hay remoto. No fusionar ni
   empujar a `main`. No escribir en `respaldos/`: es histórico.

## Informe final

Devolver, breve:

- Archivo(s) escritos o modificados.
- Recuento de palabras de prosa propia (sin extractos de fallos) frente al
  objetivo de 3.000–4.500.
- Resultado de la verificación (citekeys, citas en bloque, cobertura,
  extractos insertados) y cuántas citas llevan `[verif. visual]`.
- Tabla de extractos: fuente, páginas del PDF, palabras, origen (extracto,
  limpio, OCR sin revisar). Sin reproducir el texto.
- Discrepancias entre notas de clase y fuentes, y todo `[PENDIENTE]` abierto.
- Ediciones del autor conservadas, y las que chocan con alguna regla, con la
  corrección propuesta (sin aplicarla).
- Decisiones de criterio que el autor debería revisar (selección de pasajes o
  considerandos, lugares donde se tomó partido).
