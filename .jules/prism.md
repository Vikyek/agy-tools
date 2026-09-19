## 2024-05-24 - Semantic Logging in Shell Scripts
**Learning:** Raw `echo` statements in setup scripts lead to unstructured walls of text. Standardized functions (`info`, `warn`, `error`, `success`) equipped with ANSI colors significantly improve developer scannability, provided they check `NO_COLOR` and route errors to stderr.
**Action:** Always implement and use a `NO_COLOR`-compliant logging block with proper stdout/stderr separation instead of plain `echo` for long shell setup sequences. Use `>/dev/null` for spammy standard command outputs (like `pip install`) to keep logs concise while preserving their internal error traces.

## 2024-05-27 - Truncating and dimming Git Hashes
**Learning:** 40-character git hashes in lists create a lot of visual noise. Extracting the first 7 chars and applying dim formatting (\e[2m) makes terminal lists much more readable while preserving essential identity info.
**Action:** Always truncate long metadata strings (like hashes) in console lists, and use dim formatting to push them visually behind primary information like module names or statuses.
