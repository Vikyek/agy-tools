## 2024-05-24 - Semantic Logging in Shell Scripts
**Learning:** Raw `echo` statements in setup scripts lead to unstructured walls of text. Standardized functions (`info`, `warn`, `error`, `success`) equipped with ANSI colors significantly improve developer scannability, provided they check `NO_COLOR` and route errors to stderr.
**Action:** Always implement and use a `NO_COLOR`-compliant logging block with proper stdout/stderr separation instead of plain `echo` for long shell setup sequences. Use `>/dev/null` for spammy standard command outputs (like `pip install`) to keep logs concise while preserving their internal error traces.
## 2026-09-17 - Dim and truncate long commit hashes
**Learning:** When printing long metadata strings (like 40-character commit hashes) in terminal lists, truncate them (e.g., to 7 characters) and use dim ANSI coloring (\e[2m) to reduce visual noise and maintain visual hierarchy.
**Action:** Truncate to 7 characters and use `\e[2m` for metadata fields in list outputs.
