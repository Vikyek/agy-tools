## 2024-05-24 - Semantic Logging in Shell Scripts
**Learning:** Raw `echo` statements in setup scripts lead to unstructured walls of text. Standardized functions (`info`, `warn`, `error`, `success`) equipped with ANSI colors significantly improve developer scannability, provided they check `NO_COLOR` and route errors to stderr.
**Action:** Always implement and use a `NO_COLOR`-compliant logging block with proper stdout/stderr separation instead of plain `echo` for long shell setup sequences. Use `>/dev/null` for spammy standard command outputs (like `pip install`) to keep logs concise while preserving their internal error traces.

## 2024-10-25 - Truncating Hashes & Dimming Metadata
**Learning:** Printing full 40-character commit hashes in terminal lists creates visual noise that distracts from the core statuses (ENABLED/DISABLED).
**Action:** Truncate commit hashes to 7 characters (preserving git status prefixes like `+` or `U`) and apply dim ANSI colors (\e[2m) to auxiliary text to maintain visual hierarchy and improve scannability.
