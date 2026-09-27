## 2024-05-24 - Semantic Logging in Shell Scripts
**Learning:** Raw `echo` statements in setup scripts lead to unstructured walls of text. Standardized functions (`info`, `warn`, `error`, `success`) equipped with ANSI colors significantly improve developer scannability, provided they check `NO_COLOR` and route errors to stderr.
**Action:** Always implement and use a `NO_COLOR`-compliant logging block with proper stdout/stderr separation instead of plain `echo` for long shell setup sequences. Use `>/dev/null` for spammy standard command outputs (like `pip install`) to keep logs concise while preserving their internal error traces.

## 2025-01-28 - Truncating and Dimming Terminal Metadata
**Learning:** Long commit hashes and repetitive static text like '(uninitialized)' create visual noise in terminal lists.
**Action:** Truncate metadata strings (e.g., hashes to 7 chars) and apply dim ANSI styling (\e[2m) to make the core structure easier to scan while preserving essential info.
