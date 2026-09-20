## 2024-05-24 - Semantic Logging in Shell Scripts
**Learning:** Raw `echo` statements in setup scripts lead to unstructured walls of text. Standardized functions (`info`, `warn`, `error`, `success`) equipped with ANSI colors significantly improve developer scannability, provided they check `NO_COLOR` and route errors to stderr.
**Action:** Always implement and use a `NO_COLOR`-compliant logging block with proper stdout/stderr separation instead of plain `echo` for long shell setup sequences. Use `>/dev/null` for spammy standard command outputs (like `pip install`) to keep logs concise while preserving their internal error traces.
## 2024-10-27 - Dimming and Truncating Hashes in Terminal Lists
**Learning:** Printing long metadata strings (like 40-character commit hashes) clutters terminal list outputs. Truncating them (e.g., to 7 characters) and using dim ANSI coloring (`\e[2m`) significantly reduces visual noise and improves visual hierarchy without losing readability.
**Action:** When printing long metadata strings in terminal lists, truncate them and use dim ANSI coloring (`\e[2m`) to reduce visual noise while maintaining the core structure.
