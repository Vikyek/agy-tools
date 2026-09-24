## 2024-05-24 - Semantic Logging in Shell Scripts
**Learning:** Raw `echo` statements in setup scripts lead to unstructured walls of text. Standardized functions (`info`, `warn`, `error`, `success`) equipped with ANSI colors significantly improve developer scannability, provided they check `NO_COLOR` and route errors to stderr.
**Action:** Always implement and use a `NO_COLOR`-compliant logging block with proper stdout/stderr separation instead of plain `echo` for long shell setup sequences. Use `>/dev/null` for spammy standard command outputs (like `pip install`) to keep logs concise while preserving their internal error traces.
## 2024-05-24 - Truncating and Dimming Auxiliary Text
**Learning:** Long metadata strings (like 40-character commit hashes) and static text (e.g., 'uninitialized') clutter terminal outputs and make them harder to scan.
**Action:** Truncate long hashes (e.g., to 7 characters) and use dim ANSI coloring (\e[2m) for metadata to reduce visual noise and maintain hierarchy in lists.
