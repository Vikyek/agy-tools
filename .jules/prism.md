## 2024-05-24 - Semantic Logging in Shell Scripts
**Learning:** Raw `echo` statements in setup scripts lead to unstructured walls of text. Standardized functions (`info`, `warn`, `error`, `success`) equipped with ANSI colors significantly improve developer scannability, provided they check `NO_COLOR` and route errors to stderr.
**Action:** Always implement and use a `NO_COLOR`-compliant logging block with proper stdout/stderr separation instead of plain `echo` for long shell setup sequences. Use `>/dev/null` for spammy standard command outputs (like `pip install`) to keep logs concise while preserving their internal error traces.

## 2025-01-18 - Truncating and Dimming Auxiliary Output
**Learning:** Printing full 40-character commit hashes and static metadata like "uninitialized" creates unnecessary visual noise in terminal lists.
**Action:** Truncate long hashes (e.g. to 7 characters) while preserving status prefixes (+, -, U), and use ANSI dim styling (\e[2m) for all auxiliary text to maintain visual hierarchy.
