# claude-socratic-plugin

Claude Code plugin that implements socratic learning mode.

## Structure

```
.claude-plugin/
  plugin.json        — plugin metadata
  marketplace.json   — marketplace index
hooks/
  hooks.json         — registers the SessionStart hook
hooks-handlers/
  session-start.py   — reads config and generates dynamic context
commands/
  socratic.md        — skill for /socratic add|toggle|list
  init.md            — skill for /socratic init
```

## User files (auto-generated)

- `~/.claude/socratic-config.json` — active types and their definitions
- `~/.claude/socratic-glossary.md` — glossary of explained concepts

## Adding a new built-in type

Edit `hooks-handlers/session-start.py` in `DEFAULT_CONFIG["types"]`:

```python
"my_type": {
    "emoji": "◆",
    "name": "My Type",
    "description": "What this type should explain.",
    "when": "When to use it",
    "enabled": True
}
```

Then bump the version in `plugin.json` and `marketplace.json`, and update `CHANGELOG.md`.

## Conventions

- No comments in code
- New types must have a unique emoji, short name (1-2 words), and specific `when` field
- The glossary is append-only — never delete entries

## Releasing a new version

1. Update `version` in `.claude-plugin/plugin.json` and `.claude-plugin/marketplace.json`
2. Add entry in `CHANGELOG.md`
3. Commit, push and tag: `git tag v1.x.x && git push --tags`
