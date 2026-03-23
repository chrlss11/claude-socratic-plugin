# Changelog

Todos los cambios notables de claude-socratic-plugin se documentan aquí.

## [Unreleased]

## [1.0.0] - 2026-03-22

### Added
- 7 tipos de insights activables: `★ Insight`, `⟳ Flow`, `⬡ Tradeoff`, `❐ Pattern`, `▲ Level Up`, `🎓 Concept`, `⊛ Curious`
- Hook `SessionStart` que inyecta contexto dinámico basado en tipos activos
- Glosario persistente en `~/.claude/socratic-glossary.md` — los conceptos explicados nunca se repiten
- Configuración en `~/.claude/socratic-config.json` con defaults automáticos al primer uso
- Comando `/socratic list` — muestra todos los tipos y su estado
- Comando `/socratic toggle <nombre>` — activa o desactiva un tipo
- Comando `/socratic add <descripción>` — crea un nuevo tipo en lenguaje natural
- Compatible con Windows (Python puro, sin dependencias Unix)
