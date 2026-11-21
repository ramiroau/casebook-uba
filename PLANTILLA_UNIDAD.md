# Plantilla de unidad

Estructura canónica. Formato híbrido: los fallos de la CSJN se reproducen como
extractos editados —son de dominio público—; la doctrina bajo copyright se
encuadra, se reconstruye y se cita en pasajes acotados, remitiendo al compendio.

Extensión objetivo: 3.000 a 4.500 palabras de prosa propia por unidad, sin
contar los extractos de fallos.

---

## Unidad N. <título exacto del programa v25> {-}

Bajo el título, en cursiva y una sola línea, el copete temático del programa
(el párrafo que en `programa_uba_v25.md` sigue al encabezado de la unidad).
Se transcribe literal: es el contrato con los estudiantes.

### El problema {-}

400 a 600 palabras. Por qué existe esta unidad, qué está en juego, qué pregunta
abre y por qué no tiene respuesta pacífica. Abre con preguntas directas. Cierra
con el párrafo-hoja-de-ruta que anuncia el recorrido de la unidad.

### Preguntas que guían la lectura {-}

Cuatro a seis preguntas numeradas. Son las que el estudiante debe poder
responder después de leer, y anticipan el registro del examen. No son
retóricas: cada una tiene apoyo en un texto concreto de la unidad.

### Lectura: <Apellido>, «<Título>» [@citekey] {-}

Se repite por cada lectura obligatoria de doctrina.

**Ubicación.** Una o dos líneas: dónde está en el compendio, cuántas páginas,
si es obligatoria u optativa, de qué obra forma parte.

**El argumento.** Reconstrucción fiel del texto, en prosa propia, con citekey
por afirmación sustantiva. No es un resumen lineal capítulo por capítulo: es la
identificación de la tesis, los pasos que la sostienen y los supuestos que
asume. Entre 800 y 1.200 palabras.

**Pasajes clave.** Tres o cuatro citas en bloque, literales, con referencia
precisa. Cada una va precedida de una línea que dice por qué ese pasaje y no
otro. Este es el corazón del casebook: el pasaje se destaca, no se parafrasea.

> Cita literal, con cortes marcados `[…]` y agregados entre corchetes.
>
> [@citekey, página]

**Notas y preguntas.** Tres a cinco observaciones numeradas: tensiones internas
del texto, objeciones disponibles, conexiones con otras unidades del programa,
y —cuando corresponda— desacuerdo del autor con el texto, dicho como tal.

### Caso: *Nombre* (año) [@citekey] {-}

Se repite por cada fallo de la unidad.

**Ficha.** Tribunal y fecha; cita de Fallos; hechos en cuatro o cinco líneas;
la cuestión constitucional en una pregunta; qué decidió; cómo se compuso la
mayoría y quién disidió. Todo verificado contra el extracto.

**Extracto editado.** Considerandos seleccionados del fallo, con su numeración
original, cortes señalados con `[…]`. Los votos van separados y titulados
(«Voto que encabeza el pronunciamiento», «Voto del juez X», «Disidencia del
juez Y»). Antes de cada bloque, una línea del autor que explica qué hace ese
considerando en la arquitectura del fallo. La selección busca que el estudiante
pueda seguir el razonamiento sin el fallo completo, no que lo lea entero.

**Notas y preguntas.** Igual que en las lecturas: qué quedó sin decidir, qué
hace la disidencia con el argumento de la mayoría, cómo dialoga el caso con la
doctrina de la unidad.

### Síntesis: qué queda abierto {-}

200 a 400 palabras. No cierra la controversia: la formula con precisión. Dice
qué se llevó ganado en la unidad y qué desacuerdo persiste, y por qué persistir
es lo correcto.

### Para seguir leyendo {-}

La bibliografía optativa de la unidad según el programa, con citekey y una
línea por entrada que diga qué agrega respecto de la obligatoria. También va
acá el material que está en la carpeta de la unidad pero fuera del programa,
identificado como tal.

---

## Convenciones de archivo

- Un archivo por unidad: `unidades/U01.md`, `unidades/U02.md`, …
- Todos los encabezados llevan `{-}`: el casebook no numera secciones, igual
  que el programa.
- Los archivos de unidad no llevan YAML propio. El YAML vive en `casebook.md`,
  que los incluye en orden.
- Las citas en bloque de fallos usan `>` de markdown, no `:::` divs, para que
  el pipeline se mantenga simple.
- Los extractos de más de unas pocas líneas (de doctrina o de fallos) no se
  transcriben: van como marcador `<!-- EXTRACTO clave … -->` y se insertan al
  compilar. Ver `README.md` y la cabecera de `scripts/insertar_extractos.py`.
