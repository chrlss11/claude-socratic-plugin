# claude-socratic-plugin

Plugin de Claude Code que implementa modo socrático de aprendizaje.

## Estructura

```
.claude-plugin/
  plugin.json        — metadata del plugin
  marketplace.json   — índice del marketplace
hooks/
  hooks.json         — registra el hook SessionStart
hooks-handlers/
  session-start.py   — lee config y genera contexto dinámico
commands/
  socratic.md        — skill para /socratic add|toggle|list
```

## Archivos de usuario (generados automáticamente)

- `~/.claude/socratic-config.json` — tipos activos y sus definiciones
- `~/.claude/socratic-glossary.md` — glosario de conceptos explicados

## Agregar un nuevo tipo built-in

Editar `hooks-handlers/session-start.py` en `DEFAULT_CONFIG["types"]`:

```python
"mi_tipo": {
    "emoji": "◆",
    "name": "Mi Tipo",
    "description": "Qué debe explicar este tipo.",
    "when": "Cuándo usarlo",
    "enabled": True
}
```

Luego hacer bump de versión en `plugin.json` y `marketplace.json`, y actualizar `CHANGELOG.md`.

## Convenciones

- Commits en español
- Sin comentarios en el código
- Tipos nuevos deben tener emoji único, nombre corto (1-2 palabras), y `when` específico
- El glosario nunca se borra — solo se agrega

## Publicar una versión nueva

1. Actualizar `version` en `.claude-plugin/plugin.json` y `.claude-plugin/marketplace.json`
2. Agregar entrada en `CHANGELOG.md`
3. Commit, push y tag: `git tag v1.x.x && git push --tags`
