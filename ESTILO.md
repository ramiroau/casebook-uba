# ESTILO — casebook de Elementos de Derecho Constitucional

Guía derivada de tres corpus propios: las notas de clase
(`../notas_uba.md`, 26.486 palabras), la prosa del programa
(`../Programa_UBA/last_version/programa_uba_v25.md`) y los trabajos académicos
en castellano (`27_libertad/libertad_v1.md`,
`46_academic_freedom/libertad_academica_v1.md`,
`0_viejas_cosas/argentina_djp_v1.md`). Es descriptiva antes que prescriptiva:
cada regla se apoya en un rasgo observable en esos textos.

El `STYLE.md` de `~/Documents/AI_ra/research/` sigue vigente para lo general
—voz analítica, un argumento por párrafo, ninguna afirmación sin fuente,
citekeys en formato pandoc— pero está en inglés y pensado para papers. Esto lo
reemplaza para el casebook.

## Voz

El registro es el del profesor que escribe, no el del manual que dicta. Primera
persona del plural cuando se toma partido («creo que», «me parece», «voy a
sostener»); primera del plural cuando se describe la práctica compartida
(«nuestro derecho constitucional», «lo que hacemos en esta materia»). El
casebook nunca finge neutralidad donde los autores tienen posición, pero distingue
siempre entre lo que el texto fuente dice y lo que los autores piensan del texto. De todas formas, el tono general debe ser más bien neutral y descriptivo. 

Rasgos a conservar:

- **Preguntas directas para abrir un problema**, en general de a dos o tres:
  «¿Con qué está comprometido nuestro derecho? ¿Qué lo define? ¿Cómo se
  diferencia de la política?». Abren sección; no se responden de inmediato.
- **Hedging explícito**. «tentativamente», «no intento ser concluyente»,
  «aunque no estoy seguro de ello». La incertidumbre se dice, no se disimula.
- **Comodidad con el desacuerdo**. Cuando dos autores del programa se
  contradicen, el casebook marca la contradicción en lugar de sintetizarla en
  un promedio. Las controversias se dejan abiertas.
- **Sin floritura**. Ningún superlativo sin respaldo, ninguna metáfora
  decorativa, ningún párrafo que solo anuncie lo que viene después (salvo el
  párrafo-hoja-de-ruta, ver abajo).

## Prosa

- **Párrafos densos y desarrollados**, no telegráficos. Un argumento por
  párrafo, pero el argumento se despliega: premisa, apoyo, consecuencia. Las
  notas de clase son listas de bullets; el casebook no lo es.
- **Raya larga `---` como inciso**, pegada a la palabra pero con espacios, a diferencia del corpus: `el derecho ---entonces--- es`. Se usa mucho y se usa bien: para
  matizar sin abrir paréntesis. 
- No se deben usar construcciones adversariales, p.ej., "La clasificación es analítica, no biográfica." o en términos más generales "Esto es A, no B". O "No es B, es A". 
- **Cursivas para el término técnico en su primera aparición** (*poder
  constituyente*, *precompromiso*, *dificultad contramayoritaria*) y para el
  verbo cuando el énfasis está en el verbo (lo que el derecho *es*).
- **Cursivas para nombres de casos**: *Fayt*, *Schiffrin*, *Marbury*. Siempre.
- **Párrafo-hoja-de-ruta** al final de la sección de apertura de cada unidad,
  en el molde de «Procedo, entonces, de la siguiente manera. En la primera
  sección…». Una vez por unidad, no más.
- «p.ej.» abreviado; «etcétera» completo; «Cf.» dentro del corchete de cita.
- Números de artículos constitucionales en cifras: art. 30, art. 99 inc. 4.

## Citas

- Formato pandoc con citekey de `programauba.json`: `[@saenz2016a]`. Si no están en el JSON, pueden ponerse citekeys inventadas, siempre y cuando respondan al corpus. 
- Página sin prefijo «p.», tal como en el corpus: `[@holmes1993, 231]`.
- Varias claves juntas con punto y coma: `[@csjn_fayt1999; @csjn_schiffrin2017]`.
- Remisión comparativa: `[Cf. @nino1996a]`.
- **Ninguna afirmación sustantiva sin citekey.** Si algo sale de las notas de
  clase y no del material asignado, o se apoya en el material o se marca como
  apreciación propia del autor.
- **Ninguna fuente que no esté en `programauba.json`.** Si hace falta una nueva,
  se agrega primero a la bibliografía y se registra en `FUENTES.md`.
- Los fallos se citan por considerando y por voto, no por página: «*Schiffrin*,
  voto de Rosatti, cons. 18».

## Fidelidad al material

Esta es la regla que gobierna a las demás. El casebook existe para **encuadrar y
destacar** los textos asignados, no para sustituirlos.

1. Toda reconstrucción de un argumento debe poder rastrearse hasta un pasaje del
   extracto correspondiente en `extractos/`.
2. Cuando las notas de clase afirman algo que el texto fuente no sostiene,
   **prevalece el texto fuente** y la discrepancia se anota.
3. Las citas en bloque son literales. Los cortes se marcan con `[…]` y los
   agregados del autor van entre corchetes. Pero nuestra intención es dejar los agregados del autor al mínimo: la idea es enmarcar casos, extrayendo de ellos los datos principales. Siempre es posible testear en contra de la base de datos de la CSJN que está en ~/Documents/observatorio-csjn/data/csjn.db. 
4. Las citas provenientes de extractos OCR (`gargarella2009d`,
   `gargarella2015b`, `nino1996a`) se cotejan visualmente contra la página del
   PDF antes de fijarse. Ver `FUENTES.md`.
5. El casebook no introduce doctrina ni jurisprudencia ajena al programa. Si una
   conexión externa es imprescindible, se marca explícitamente como agregado.

## Lo que el casebook no hace

- No resuelve la controversia que el programa quiere dejar abierta.
- No reemplaza la lectura: cada sección remite al compendio.
- No adopta el tono del manual («la doctrina mayoritaria sostiene…») sin decir
  qué doctrina y dónde.
- No usa bullets como sustituto del argumento. Las listas se reservan para
  enumeraciones genuinas: requisitos, etapas, posiciones en un debate.

## Estructura modelo

1. Se introduce el problema o la cuestión y se hace un breve repaso por la jurisprudencia o por la doctrina, en párrafos distintos, y en forma de prosa y a modo de introducción. 
2. Luego se desarrollan esos puntos de jurisprudencia y/o doctrina, con el siguiente criterio: 
  a. Se privilegia una línea histórica, que muestra la evolución de la jurisprudencia hasta su "estado actual de la cuestión". 
  b. Los hechos del caso los resume el agente que redacta, se extrae de la decisión los considerandos relevantes, con el holding y los obiter dictum. Para identificar el holding, pueden ayudar los sumarios a disposición en la base de datos de la CSJN señalada más arriba. Pero se extrae el texto **siempre** de la decisión. Se presenta ese texto en formato largo: preferimos una cita larga que varias citas conectadas por comentarios de los autores. 
  c. Al final la unidad o la sección, si es claramente diferente a la que continúa, se pone una sección de "Notas y preguntas" y otra de "Síntesis". Y finalmente, una sección "Para seguir leyendo" con bibliografía adicional, casi sin descripciones.
