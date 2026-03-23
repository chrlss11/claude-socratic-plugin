# /socratic init — Configuración inicial interactiva

Guía al usuario por la configuración inicial del plugin. Muestra cada tipo disponible con una descripción y ejemplo, y pregunta cuáles activar.

## Comportamiento

Cuando el usuario ejecuta `/socratic init`:

1. Saluda y explica brevemente qué hace el plugin en 2-3 líneas.

2. Lee la config actual de `~/.claude/socratic-config.json`. Si no existe, usa los defaults del plugin.

3. Para cada tipo disponible, muestra una ficha como esta:

```
─────────────────────────────────────────────
⊛ Curious
Antes de ejecutar tareas significativas, Claude
cuestiona sus propias suposiciones en voz alta.

Ejemplo:
  "¿Por qué está fallando aquí y no en el portal
  legacy? Asumo que la sesión persiste entre
  requests — ¿es correcto en este contexto?"

Estado actual: ✓ activado
─────────────────────────────────────────────
```

4. Después de mostrar TODOS los tipos, pregunta al usuario con una sola pregunta:

```
¿Cuáles tipos quieres activar? Escribe los nombres separados por coma,
o escribe "todos" para activar todos, o "ninguno" para desactivar todos.

Actualmente activos: Curious, Insight, Flow, Tradeoff, Pattern, Level Up, Concept
```

5. Procesa la respuesta del usuario:
   - Actualiza `~/.claude/socratic-config.json` con el estado correcto de cada tipo
   - Si el archivo no existe, créalo con la estructura completa de DEFAULT_CONFIG del session-start.py, aplicando las preferencias del usuario

6. Muestra un resumen final:

```
✓ Configuración guardada

  Activados (5):  ⊛ Curious  ★ Insight  ⟳ Flow  🎓 Concept  ▲ Level Up
  Desactivados (2):  ⬡ Tradeoff  ❐ Pattern

Los tipos activados aparecerán en tus sesiones a partir de ahora.
Puedes cambiarlos en cualquier momento con /socratic toggle <nombre>.
```

## Notas

- Este flujo también se ejecuta automáticamente en la primera sesión si no existe `~/.claude/socratic-config.json`
- Si el usuario ya tiene configuración, muestra el estado actual de cada tipo antes de preguntar
- El comando es idempotente — se puede correr múltiples veces sin problema
- No pierdas tipos personalizados que el usuario haya creado con `/socratic add`
