## 2024-05-24 - Semantic Logging in Shell Scripts
**Learning:** Raw `echo` statements in setup scripts lead to unstructured walls of text. Standardized functions (`info`, `warn`, `error`, `success`) equipped with ANSI colors significantly improve developer scannability, provided they check `NO_COLOR` and route errors to stderr.
**Action:** Always implement and use a `NO_COLOR`-compliant logging block with proper stdout/stderr separation instead of plain `echo` for long shell setup sequences. Use `>/dev/null` for spammy standard command outputs (like `pip install`) to keep logs concise while preserving their internal error traces.
## 2026-10-06 - Consistent Help Menu Formatting
**Learning:** Space-aligned shell echo statements for help menus often break and result in jagged output when new commands are added.
**Action:** Use printf statements with width formatting instead of space-aligned echoes for more robust and maintainable help menus.
## 2026-10-06 - Adding Meaningful Color to Bash Utilities
**Learning:** Enhancing bash output with colors using semantic mapping (green for enable, red for disable) accompanied by clear unicode icons helps quickly indicate script state transitions without breaking functionality.
**Action:** Use specific color logic matching terminal UI updates alongside the standard NO_COLOR evaluation.
