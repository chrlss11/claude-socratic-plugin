# Changelog

All notable changes to claude-socratic-plugin are documented here.

## [Unreleased]

## [1.2.0] - 2026-03-22

### Changed
- First session without config automatically detects its absence and runs the init flow before responding to the user

## [1.1.0] - 2026-03-22

### Added
- `/socratic init` command — interactive setup that shows each type with a description and example, then asks which to enable

## [1.0.0] - 2026-03-22

### Added
- 7 activatable insight types: `★ Insight`, `⟳ Flow`, `⬡ Tradeoff`, `❐ Pattern`, `▲ Level Up`, `🎓 Concept`, `⊛ Curious`
- `SessionStart` hook that injects dynamic context based on active types
- Persistent glossary at `~/.claude/socratic-glossary.md` — explained concepts are never repeated
- Config at `~/.claude/socratic-config.json` with automatic defaults on first use
- `/socratic list` command — shows all types and their current status
- `/socratic toggle <name>` command — enables or disables a type
- `/socratic add <description>` command — creates a new type from a natural language description
- Windows compatible (pure Python, no Unix dependencies)
