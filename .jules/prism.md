## 2024-05-24 - Semantic Logging in Shell Scripts
**Learning:** Raw `echo` statements in setup scripts lead to unstructured walls of text. Standardized functions (`info`, `warn`, `error`, `success`) equipped with ANSI colors significantly improve developer scannability, provided they check `NO_COLOR` and route errors to stderr.
**Action:** Always implement and use a `NO_COLOR`-compliant logging block with proper stdout/stderr separation instead of plain `echo` for long shell setup sequences. Use `>/dev/null` for spammy standard command outputs (like `pip install`) to keep logs concise while preserving their internal error traces.

## 2024-09-16 - Truncating Git Hashes for Scannability
**Learning:** Printing full 40-character Git hashes in terminal list commands creates unnecessary visual noise and horizontal scrolling, harming readability.
**Action:** When printing Git commit hashes in terminal outputs, extract and display only the first 7 characters (the standard short hash length). Use dim ANSI color styling (`\e[2m`) to de-emphasize this metadata compared to the primary list items, and ensure proper extraction of any Git status prefix flags (like `+`, `-`, `U`) before truncating. Always verify that `NO_COLOR` logic is properly handled.
