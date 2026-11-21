# Casebook UBA — instrucciones para Claude

Flujo de trabajo y archivos: ver `README.md`. Para redactar o revisar una
unidad, usar el agente `case_book` (`.claude/agents/case_book.md`).

## Ediciones del autor (regla prioritaria)

Vale para cualquier sesión o agente que toque `unidades/`, incluso cuando se
pide reescribir una unidad entera.

- Son ediciones del autor: toda diferencia entre `unidades/U0N.md` y
  `respaldos/U0N_agente.md` (la última versión escrita por el agente), todo
  pasaje entre `<!-- AUTOR -->` y `<!-- /AUTOR -->` y toda nota
  `<!-- AUTOR: eliminado … -->`.
- Se conservan literales: no se reformulan, no se corrigen, no se mueven y no
  se eliminan. Lo que el autor eliminó no se reintroduce.
- Si una edición del autor choca con otra regla (citekey inexistente, cita sin
  página, error tipográfico), se deja como está y se informa, con una propuesta
  que el autor decide.
- Antes de modificar una unidad, hacer `diff` contra `respaldos/U0N_agente.md`.
  Si ese archivo no existe, preguntar antes de reescribir.
- Al terminar una reescritura, envolver las ediciones conservadas con los
  marcadores `AUTOR` y recién entonces copiar la unidad a
  `respaldos/U0N_agente.md`. Ese archivo no se edita a mano.
- Los cambios puramente mecánicos pedidos de manera expresa (por ejemplo,
  unir renglones de un párrafo) no alteran el texto y pueden aplicarse a todo
  el archivo; en ese caso se aplican también a `respaldos/U0N_agente.md`, para
  que el `diff` siga mostrando sólo las ediciones del autor.
