# Casebook UBA — instrucciones para Claude

Flujo de trabajo y archivos: ver `README.md` y `workflow.md`. Para redactar o
revisar una unidad, usar el agente `case_book` (`.claude/agents/case_book.md`).

El proyecto está bajo Git: https://github.com/ramiroau/casebook-uba (público;
los PDFs no se versionan).

## Ediciones del autor (regla prioritaria)

Vale para cualquier sesión o agente que toque `unidades/`, incluso cuando se
pide reescribir una unidad entera.

- Son ediciones del autor las líneas cuyo último commit es de un autor humano,
  es decir, un commit **sin** el trailer `Co-Authored-By: Claude`.
  `git blame unidades/U0N.md` muestra el último commit de cada línea, y
  `git log -p unidades/U0N.md` muestra además lo que el autor eliminó.
- Las ediciones anteriores a la migración a Git (sólo en U01) están marcadas con
  `<!-- AUTOR -->` en el commit `13c5f06`: `git show 13c5f06:unidades/U01.md`.
  También valen como ediciones del autor.
- Se conservan literales: no se reformulan, no se corrigen, no se mueven y no
  se eliminan. Lo que el autor eliminó no se reintroduce.
- Si una edición del autor choca con otra regla (citekey inexistente, cita sin
  página, error tipográfico), se deja como está y se informa, con una propuesta
  que el autor decide.
- Antes de modificar una unidad, revisar `git blame` y `git log -p` de ese
  archivo y listar las ediciones del autor.
- El agente nunca trabaja en `main`. Lo hace en una rama propia
  (`agente/u0N-<tema>`), con commits que llevan el trailer `Co-Authored-By:
  Claude`, y propone la fusión por *pull request*. No fusiona por su cuenta.
- Una rama o *pull request* toca una sola unidad. Los cambios a reglas comunes
  (`ESTILO.md`, `PLANTILLA_UNIDAD.md`, `scripts/`) van por separado.
- `respaldos/` es histórico: no se agregan ni se editan archivos ahí. Las
  versiones anteriores se recuperan del historial de Git.
