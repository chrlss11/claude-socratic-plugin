# claude-socratic-plugin

> Modo socrático para Claude Code — aprende mientras construyes.

Diseñado para desarrolladores empíricos: sin universidad, sin teoría vacía. Solo contexto útil en el momento exacto que lo necesitas.

---

## ¿Qué hace?

Inyecta bloques de conocimiento contextual en las respuestas de Claude, activados automáticamente según lo que está pasando en tu código.

La clave: **⊛ Curious** aparece *antes* de ejecutar — Claude cuestiona sus propias suposiciones en voz alta antes de hacer algo. Los demás tipos aparecen *después*.

---

## Tipos de insights

### ⊛ Curious
> Antes de ejecutar tareas significativas, Claude cuestiona sus suposiciones en voz alta.

```
⊛ Curious ─────────────────────────────────────
¿Por qué está fallando el login aquí y no en el portal legacy?
Asumo que la sesión persiste entre requests — ¿es eso correcto
en este contexto de Playwright? Si no, el problema está antes
de esta función.
─────────────────────────────────────────────────
```

---

### ★ Insight
> Decisiones de implementación específicas al código recién escrito.

```
★ Insight ─────────────────────────────────────
Se usa `waitForSelector` con timeout explícito en lugar del
default porque el portal SAT tiene latencia variable (2-15s).
El default de Playwright (30s) es demasiado permisivo y enmascara
errores reales de carga.
─────────────────────────────────────────────────
```

---

### ⟳ Flow
> Traza el camino de ejecución de código complejo.

```
⟳ Flow ─────────────────────────────────────────
request HTTP → detectPortal() → bifurcación legacy/nuevo
  ├─ legacy: ptscdecprov.clouda.sat.gob.mx
  │    └─ loginCIEC() → searchByPeriod() → downloadXML()
  └─ nuevo:  pstcdypisr.clouda.sat.gob.mx (>= 2025)
       └─ loginEFirma() → selectYear() → exportCSV()
─────────────────────────────────────────────────
```

---

### ⬡ Tradeoff
> Qué alternativas existían y por qué se eligió este approach.

```
⬡ Tradeoff ─────────────────────────────────────
Se pudo haber usado `page.evaluate()` para extraer datos del
DOM, pero se eligió interceptar la respuesta de red porque:
(1) es más estable ante cambios de UI, (2) el portal usa renders
parciales que hacen el DOM inconsistente.
─────────────────────────────────────────────────
```

---

### ❐ Pattern
> El patrón de diseño en uso y por qué encaja aquí.

```
❐ Pattern ────────────────────────────────────────
Se aplica Strategy pattern: `detectPortal()` selecciona en
runtime qué implementación usar (legacy vs nuevo). Encaja aquí
porque SAT tiene dos portales con la misma interfaz lógica pero
diferente UI — Strategy permite agregar un tercer portal sin
tocar el orquestador.
─────────────────────────────────────────────────
```

---

### ▲ Level Up
> Conocimiento transferible a otros contextos.

```
▲ Level Up ──────────────────────────────────────
Cuando un servicio externo cambia su portal sin deprecar el
anterior, el patrón más sostenible es detectar la versión en
runtime en lugar de mantener dos implementaciones separadas.
Aplica a cualquier integración con APIs gubernamentales o
sistemas legacy que coexisten.
─────────────────────────────────────────────────
```

---

### 🎓 Concept
> Define términos, patrones y paradigmas — sin academicismo.

```
🎓 Concept ───────────────────────────────────────
**AST (Abstract Syntax Tree)**
Representación del código como árbol de nodos. Cada nodo es
una construcción del lenguaje (función, variable, if). Se usa
en linters, compiladores y herramientas como cocoindex-code
para entender código sin ejecutarlo.
─────────────────────────────────────────────────
```

Los conceptos explicados se guardan en `~/.claude/socratic-glossary.md` — Claude los consulta al inicio de cada sesión y nunca repite una explicación.

---

## Instalación

```bash
claude plugin install chrlss11/claude-socratic-plugin
```

---

## Comandos

### `/socratic init`
Configuración inicial interactiva. Muestra cada tipo con descripción y ejemplo, y pregunta cuáles activar:

```
─────────────────────────────────────────────
⊛ Curious
Antes de ejecutar tareas significativas, Claude
cuestiona sus propias suposiciones en voz alta.

Ejemplo:
  "¿Por qué está fallando aquí y no en el portal
  legacy? Asumo que la sesión persiste — ¿es
  correcto en este contexto?"

Estado actual: ✓ activado
─────────────────────────────────────────────

¿Cuáles tipos quieres activar? Escribe los nombres separados por coma,
o escribe "todos" / "ninguno".

✓ Configuración guardada

  Activados (5):  ⊛ Curious  ★ Insight  ⟳ Flow  🎓 Concept  ▲ Level Up
  Desactivados (2):  ⬡ Tradeoff  ❐ Pattern
```

---

### `/socratic list`

```
Tipos activos: 6 de 7

  ✓  ⊛  Curious    — Antes de tareas significativas
  ✓  ★  Insight    — Después de escribir código
  ✓  ⟳  Flow       — Después de código async/pipeline
  ✓  ⬡  Tradeoff   — Después de decisiones de diseño
  ✓  ❐  Pattern    — Cuando se aplica un patrón
  ✓  🎓 Concept    — Cuando aparece un término técnico
  ✗  ▲  Level Up   — Desactivado
```

---

### `/socratic toggle <nombre>`

```
/socratic toggle flow

✓ Flow está ahora desactivado
```

---

### `/socratic add <descripción>`

```
/socratic add quiero que me expliques el impacto en performance
              de cada decision que tomamos

✓ Nuevo tipo creado:

  Emoji:       ⚡
  Nombre:      Performance
  Descripción: Analiza el impacto en performance de la decisión
               tomada — memoria, latencia, CPU, o I/O.
  Cuándo:      Después de cambios con impacto potencial en rendimiento
```

---

## Glosario

Cada concepto explicado por 🎓 se persiste en `~/.claude/socratic-glossary.md`:

```markdown
## AST (Abstract Syntax Tree)
Representación del código como árbol de nodos...

## Strategy Pattern
Patrón que encapsula algoritmos intercambiables...

## Idempotencia
Propiedad de una operación que produce el mismo resultado...
```

Claude consulta este archivo al inicio de cada sesión. Los conceptos ya explicados no se repiten — solo se referencian.

---

## Configuración manual

Los tipos se almacenan en `~/.claude/socratic-config.json`. Puedes editarlo directamente o usar los comandos `/socratic`.

---

## Licencia

MIT — [chrlss11](https://github.com/chrlss11)
