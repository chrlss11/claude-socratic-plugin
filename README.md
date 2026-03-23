# claude-socratic-plugin

Socratic learning mode for Claude Code. Surfaces educational insights while you work — without slowing you down.

Built for empirical developers who learn by doing, not by attending university.

## What it does

Injects contextual learning blocks into Claude's responses based on what's happening in your code:

| Type | When |
|------|------|
| ⊛ **Curious** | Before significant tasks — questions assumptions out loud |
| ★ **Insight** | After writing code — explains the implementation decisions |
| ⟳ **Flow** | After complex async/pipeline code — traces execution path |
| ⬡ **Tradeoff** | After design decisions — explains what was considered and why |
| ❐ **Pattern** | When a design pattern is applied — explains why it fits here |
| ▲ **Level Up** | After non-trivial solutions — extracts transferable knowledge |
| 🎓 **Concept** | When a technical term appears — defines it in plain language |

All concepts explained via 🎓 are saved to `~/.claude/socratic-glossary.md` so they're never explained twice.

## Installation

```bash
claude plugin install chrlss11/claude-socratic-plugin
```

## Commands

```bash
/socratic list              # Show all types and their status
/socratic toggle <name>     # Enable or disable a type
/socratic add <description> # Add a custom learning type
```

## Configuration

Types are stored in `~/.claude/socratic-config.json`. Edit directly or use `/socratic` commands.

## Glossary

Concepts explained via 🎓 Concept are persisted to `~/.claude/socratic-glossary.md`. Claude checks this before explaining anything — no repetition.
