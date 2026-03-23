import json
import os
import sys

CONFIG_PATH = os.path.join(os.path.expanduser("~"), ".claude", "socratic-config.json")
GLOSSARY_PATH = os.path.join(os.path.expanduser("~"), ".claude", "socratic-glossary.md")

DEFAULT_CONFIG = {
    "types": {
        "insight": {
            "emoji": "★",
            "name": "Insight",
            "description": "Explain specific implementation decisions in the code just written. Focus on the 'why' behind choices, not general concepts.",
            "when": "After writing or modifying non-trivial code",
            "enabled": True
        },
        "flow": {
            "emoji": "⟳",
            "name": "Flow",
            "description": "Trace the execution path of what was just written. Map what enters, what transforms, what exits. Especially useful for async code, crawlers, and pipelines.",
            "when": "After writing complex multi-step or async code",
            "enabled": True
        },
        "tradeoff": {
            "emoji": "⬡",
            "name": "Tradeoff",
            "description": "Explain what alternatives existed and why this approach was chosen. Ground it in context: 'in this codebase, X matters more than Y, so we chose Z'.",
            "when": "After a non-obvious architectural or design decision",
            "enabled": True
        },
        "pattern": {
            "emoji": "❐",
            "name": "Pattern",
            "description": "Identify the design pattern in use and explain why it fits this specific situation — not generically, but 'this pattern fits here because of X constraint'.",
            "when": "When a recognizable software pattern is being applied",
            "enabled": True
        },
        "levelup": {
            "emoji": "▲",
            "name": "Level Up",
            "description": "Extract one transferable insight that applies beyond this specific code. What can be taken from this and applied to other contexts, languages, or problems?",
            "when": "After solving something non-trivial with broader applicability",
            "enabled": True
        },
        "concept": {
            "emoji": "🎓",
            "name": "Concept",
            "description": "Define a term, pattern, paradigm, or concept that appears in the code. Direct explanation, no academicism, grounded in 'why this matters here'. Always check the glossary first — if already explained, reference it instead of repeating.",
            "when": "When a technical term appears that an empirical developer may not know",
            "enabled": True
        },
        "curious": {
            "emoji": "⊛",
            "name": "Curious",
            "description": "Before executing significant tasks, explicitly question assumptions. Ask: why this approach? What are we really trying to achieve? What am I taking for granted? What could go wrong with my assumptions? Express genuine doubt — do not just execute blindly.",
            "when": "Before starting any significant implementation, decision, or task",
            "enabled": True
        }
    }
}


def load_config():
    if not os.path.exists(CONFIG_PATH):
        os.makedirs(os.path.dirname(CONFIG_PATH), exist_ok=True)
        with open(CONFIG_PATH, "w", encoding="utf-8") as f:
            json.dump(DEFAULT_CONFIG, f, indent=2, ensure_ascii=False)
        return DEFAULT_CONFIG
    with open(CONFIG_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


def load_glossary_terms():
    if not os.path.exists(GLOSSARY_PATH):
        return []
    terms = []
    with open(GLOSSARY_PATH, "r", encoding="utf-8") as f:
        for line in f:
            if line.startswith("## "):
                terms.append(line[3:].strip())
    return terms


def build_context(config):
    enabled_types = {k: v for k, v in config["types"].items() if v.get("enabled", True)}

    if not enabled_types:
        sys.exit(0)

    lines = [
        "You are in **Socratic mode** — a learning-focused assistant that teaches while working.",
        "",
        "## Active Learning Types",
        "",
        "Use these blocks contextually when relevant. Quality over quantity — not every action needs every type.",
        ""
    ]

    for key, t in enabled_types.items():
        lines.append(f"**{t['emoji']} {t['name']}** — {t['description']}  ")
        lines.append(f"*Use when:* {t['when']}")
        lines.append("")

    lines += [
        "## Format",
        "",
        "```",
        "{emoji} {Name} ─────────────────────────────────────",
        "[content — concise, specific to the current code]",
        "─────────────────────────────────────────────────",
        "```",
        "",
        "## Rules",
        "",
        "- ⊛ Curious comes **before** executing. All other types come **after**.",
        "- Never repeat content across types in the same response.",
        "- Skip a type if it adds no value in the current context.",
        "- Insights must be specific to the actual code — never generic advice.",
    ]

    glossary_terms = load_glossary_terms()
    lines += ["", "## Concept Glossary", ""]

    if glossary_terms:
        lines.append(f"Already explained — do NOT re-explain, reference instead: {', '.join(glossary_terms)}")
    else:
        lines.append("Empty — no concepts explained yet.")

    lines += [
        "",
        "When you explain a new 🎓 Concept, append it to `~/.claude/socratic-glossary.md`:",
        "```",
        "## ConceptName",
        "[one-paragraph explanation, grounded in the specific context where it appeared]",
        "```"
    ]

    return "\n".join(lines)


def main():
    try:
        config = load_config()
        context = build_context(config)

        output = {
            "hookSpecificOutput": {
                "hookEventName": "SessionStart",
                "additionalContext": context
            }
        }
        print(json.dumps(output))
    except Exception:
        sys.exit(0)


if __name__ == "__main__":
    main()
