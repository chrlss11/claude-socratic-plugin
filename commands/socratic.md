# /socratic — Manage Socratic learning types

Use this command to add new learning types, toggle existing ones on/off, or list all available types.

## Usage

- `/socratic add <description>` — Create a new learning type from a description
- `/socratic toggle <name>` — Enable or disable a type by name
- `/socratic list` — Show all types and their current status

---

## /socratic add <description>

When the user runs `/socratic add <description>`:

1. Parse the description to understand what kind of learning insight they want
2. Generate a type definition:
   - Choose a fitting emoji that hasn't been used yet
   - Create a short name (1-2 words)
   - Write a clear `description` of what this type should surface
   - Write a `when` field: specific trigger condition for using this type
   - Set `"enabled": true`
3. Read `~/.claude/socratic-config.json`
4. Add the new type under `"types"` using a lowercase key (no spaces)
5. Save back to the file
6. Confirm what was added, showing the full type definition

---

## /socratic toggle <name>

1. Read `~/.claude/socratic-config.json`
2. Find the type by name (case-insensitive match against the `"name"` field or the key)
3. Flip its `"enabled"` field
4. Save the file
5. Confirm: "✓ {Name} is now {enabled/disabled}"

---

## /socratic list

1. Read `~/.claude/socratic-config.json`
2. Display all types as a table:

| Status | Emoji | Name | When |
|--------|-------|------|------|
| ✓ on   | ★     | Insight | After writing non-trivial code |
| ✓ on   | ⊛     | Curious | Before significant tasks |
| ✗ off  | ▲     | Level Up | After solving something reusable |

3. Show total count: "X of Y types enabled"
