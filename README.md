# claude-socratic-plugin

> Socratic mode for Claude Code — learn while you build.

Designed for empirical developers: no academia, no empty theory. Just useful context at the exact moment you need it.

---

## What does it do?

It injects contextual knowledge blocks into Claude's responses, triggered automatically based on what's happening in your code.

The key: **⊛ Curious** appears *before* executing — Claude questions its own assumptions out loud before doing anything. All other types appear *after*.

---

## Insight types

### ⊛ Curious
> Before executing significant tasks, Claude questions its assumptions out loud.

```
⊛ Curious ─────────────────────────────────────
Why is login failing here but not on the legacy portal?
I'm assuming the session persists between requests — is that
correct in this Playwright context? If not, the problem is
upstream from this function.
─────────────────────────────────────────────────
```

---

### ★ Insight
> Specific implementation decisions in the code just written.

```
★ Insight ─────────────────────────────────────
`waitForSelector` is used with an explicit timeout instead of
the default because the SAT portal has variable latency (2-15s).
Playwright's default (30s) is too permissive and masks real
load errors.
─────────────────────────────────────────────────
```

---

### ⟳ Flow
> Traces the execution path of complex code.

```
⟳ Flow ─────────────────────────────────────────
HTTP request → detectPortal() → legacy/new branch
  ├─ legacy: ptscdecprov.clouda.sat.gob.mx
  │    └─ loginCIEC() → searchByPeriod() → downloadXML()
  └─ new:    pstcdypisr.clouda.sat.gob.mx (>= 2025)
       └─ loginEFirma() → selectYear() → exportCSV()
─────────────────────────────────────────────────
```

---

### ⬡ Tradeoff
> What alternatives existed and why this approach was chosen.

```
⬡ Tradeoff ─────────────────────────────────────
`page.evaluate()` could have been used to extract data from
the DOM, but intercepting the network response was chosen because:
(1) it's more stable against UI changes, (2) the portal uses
partial renders that make the DOM inconsistent.
─────────────────────────────────────────────────
```

---

### ❐ Pattern
> The design pattern in use and why it fits here.

```
❐ Pattern ────────────────────────────────────────
Strategy pattern applied: `detectPortal()` selects at runtime
which implementation to use (legacy vs new). It fits here
because SAT has two portals with the same logical interface but
different UI — Strategy allows adding a third portal without
touching the orchestrator.
─────────────────────────────────────────────────
```

---

### ▲ Level Up
> Transferable knowledge applicable beyond this specific code.

```
▲ Level Up ──────────────────────────────────────
When an external service changes its portal without deprecating
the old one, the most sustainable pattern is to detect the version
at runtime instead of maintaining two separate implementations.
Applies to any integration with government APIs or coexisting
legacy systems.
─────────────────────────────────────────────────
```

---

### 🎓 Concept
> Defines terms, patterns, and paradigms — no academicism.

```
🎓 Concept ───────────────────────────────────────
**AST (Abstract Syntax Tree)**
Representation of code as a tree of nodes. Each node is a
language construct (function, variable, if). Used in linters,
compilers, and tools like cocoindex-code to understand code
without executing it.
─────────────────────────────────────────────────
```

Explained concepts are saved to `~/.claude/socratic-glossary.md` — Claude checks it at the start of each session and never repeats an explanation.

---

## Installation

**1. Register the marketplace:**
```bash
claude plugin marketplace add chrlss11/claude-socratic-plugin
```

**2. Install the plugin:**
```bash
claude plugin install claude-socratic-plugin@claude-socratic-plugin
```

**3. Restart Claude Code.** On your first session the plugin will automatically guide you through the initial setup.

Or if you already installed and want to configure manually:
```
/socratic init
```

---

## Commands

### `/socratic init`
Interactive initial setup. Shows each type with its description and example, and asks which ones to enable:

```
─────────────────────────────────────────────
⊛ Curious
Before executing significant tasks, Claude
questions its own assumptions out loud.

Example:
  "Why is it failing here but not on the legacy
  portal? I'm assuming the session persists — is
  that correct in this context?"

Current status: ✓ enabled
─────────────────────────────────────────────

Which types do you want to enable? Type the names separated by commas,
or type "all" / "none".

✓ Configuration saved

  Enabled (5):   ⊛ Curious  ★ Insight  ⟳ Flow  🎓 Concept  ▲ Level Up
  Disabled (2):  ⬡ Tradeoff  ❐ Pattern
```

---

### `/socratic list`

```
Active types: 6 of 7

  ✓  ⊛  Curious    — Before significant tasks
  ✓  ★  Insight    — After writing code
  ✓  ⟳  Flow       — After async/pipeline code
  ✓  ⬡  Tradeoff   — After design decisions
  ✓  ❐  Pattern    — When a pattern is applied
  ✓  🎓 Concept    — When a technical term appears
  ✗  ▲  Level Up   — Disabled
```

---

### `/socratic toggle <name>`

```
/socratic toggle flow

✓ Flow is now disabled
```

---

### `/socratic add <description>`

```
/socratic add explain the performance impact of each decision we make

✓ New type created:

  Emoji:       ⚡
  Name:        Performance
  Description: Analyzes the performance impact of the decision
               made — memory, latency, CPU, or I/O.
  When:        After changes with potential performance impact
```

---

## Glossary

Each concept explained by 🎓 is persisted in `~/.claude/socratic-glossary.md`:

```markdown
## AST (Abstract Syntax Tree)
Representation of code as a tree of nodes...

## Strategy Pattern
Pattern that encapsulates interchangeable algorithms...

## Idempotency
Property of an operation that produces the same result...
```

Claude checks this file at the start of each session. Already-explained concepts are not repeated — only referenced.

---

## Manual configuration

Types are stored in `~/.claude/socratic-config.json`. You can edit it directly or use the `/socratic` commands.

---

## License

MIT — [chrlss11](https://github.com/chrlss11)
