## 2024-05-24 - Semantic Logging in Shell Scripts
**Learning:** Raw `echo` statements in setup scripts lead to unstructured walls of text. Standardized functions (`info`, `warn`, `error`, `success`) equipped with ANSI colors significantly improve developer scannability, provided they check `NO_COLOR` and route errors to stderr.
**Action:** Always implement and use a `NO_COLOR`-compliant logging block with proper stdout/stderr separation instead of plain `echo` for long shell setup sequences. Use `>/dev/null` for spammy standard command outputs (like `pip install`) to keep logs concise while preserving their internal error traces.

## 2025-01-28 - Truncating and Dimming Terminal Metadata
**Learning:** Long commit hashes and repetitive static text like '(uninitialized)' create visual noise in terminal lists.
**Action:** Truncate metadata strings (e.g., hashes to 7 chars) and apply dim ANSI styling (\e[2m) to make the core structure easier to scan while preserving essential info.

## 2025-05-15 - Highlighting Dynamic Variables in Setup Scripts
**Learning:** Static log strings in setup scripts become much easier to read when dynamic variables like file paths, patch names, and package names are highlighted with bold text. Furthermore, Bash `NO_COLOR` compliance should be checked with `[[ -z "${NO_COLOR:-}" ]]` to ensure colors are active when `NO_COLOR` is absent, as opposed to testing for its presence with `-v`.
**Action:** Use an explicit `C_BOLD=\033[1m` sequence (reset with `C_RST`) to highlight variables or paths inside informational outputs, and always ensure `NO_COLOR` logic defaults to enabled colors when the variable is unset.

## 2025-09-29 - Visual Hierarchy for State Changes
**Learning:** Repetitive state-change actions (like enable/disable loops) are hard to scan as plain text. Combining semantic colors (e.g., green for start, red for stop) with standard iconography (▶, ■) and bolded target variables drastically improves visual hierarchy.
**Action:** Enhance loops iterating over state changes with `echo -e "${COLOR_GREEN}▶${COLOR_RESET} Activating ${COLOR_BOLD}${var}${COLOR_RESET}..."` patterns. Always initialize color variables within a proper `[[ -z "${NO_COLOR:-}" ]]` check.
