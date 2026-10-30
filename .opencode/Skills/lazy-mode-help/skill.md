---
name: lazy-mode-help
description: >
  Quick-reference card for all lazy-mode modes, skills, and commands.
  One-shot display, not a persistent mode. Trigger when the user says
  "lazy-mode help", "what lazy-mode commands", "how do I use lazy-mode".
compatibility: opencode
---
# Lazy Mode Help

Display this reference card when invoked. One-shot, do NOT change mode,
write flag files, or persist anything.

## Levels

| Level | Trigger | What change |
|-------|---------|-------------|
| **Lite** | `lite` argument | Build what's asked, name the lazier alternative in one line. |
| **Full** | no argument | The ladder enforced: YAGNI → stdlib → native → one line → minimum. Default. |
| **Ultra** | `ultra` argument | YAGNI extremist. Deletion before addition. Challenges requirements before building. |

Level sticks until changed or session end.

## Skills

| Skill | When | What it does |
|-------|------|--------------|
| **lazy-mode** | Always active for code work | Lazy mode itself. Simplest solution that works. |
| **lazy-mode-review** | Agent or user invokes | Over-engineering review: `L42: yagni: factory, one product. Inline.` |
| **lazy-mode-audit** | Agent or user invokes | Whole-repo over-engineering audit |
| **lazy-mode-debt** | Agent or user invokes | Harvest `lazy:`/`ponytail:` comments into debt ledger |
| **lazy-mode-gain** | Agent or user invokes | Measured-impact scoreboard: less code, less cost, more speed. |
| **lazy-mode-help** | Agent or user invokes | This card. |

## Comment markers

Mark deliberate shortcuts with:
- `lazy:` — primary convention. `// lazy: global lock, per-account locks if throughput matters`
- `ponytail:` — legacy equivalent, also recognized

## Deactivate

Say "stop lazy-mode" or "normal mode". Resume by invoking the skill again.

## More

Full docs + examples: https://github.com/DietrichGebert/ponytail
