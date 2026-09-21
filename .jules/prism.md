## 2024-05-24 - Semantic Logging in Shell Scripts
**Learning:** Raw `echo` statements in setup scripts lead to unstructured walls of text. Standardized functions (`info`, `warn`, `error`, `success`) equipped with ANSI colors significantly improve developer scannability, provided they check `NO_COLOR` and route errors to stderr.
**Action:** Always implement and use a `NO_COLOR`-compliant logging block with proper stdout/stderr separation instead of plain `echo` for long shell setup sequences. Use `>/dev/null` for spammy standard command outputs (like `pip install`) to keep logs concise while preserving their internal error traces.
## 2026-09-21 - Visual Hierarchy in Terminal Lists
**Learning:** Printing full 40-character commit hashes and static informational text in terminal lists creates visual noise and reduces readability.
**Action:** When printing long metadata strings (like commit hashes) in terminal lists, truncate them (e.g., to 7 characters) and use dim ANSI coloring (\e[2m) for them and other auxiliary text to reduce visual noise and maintain visual hierarchy.
