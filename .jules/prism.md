## 2024-05-24 - Semantic Logging in Shell Scripts
**Learning:** Raw `echo` statements in setup scripts lead to unstructured walls of text. Standardized functions (`info`, `warn`, `error`, `success`) equipped with ANSI colors significantly improve developer scannability, provided they check `NO_COLOR` and route errors to stderr.
**Action:** Always implement and use a `NO_COLOR`-compliant logging block with proper stdout/stderr separation instead of plain `echo` for long shell setup sequences. Use `>/dev/null` for spammy standard command outputs (like `pip install`) to keep logs concise while preserving their internal error traces.

## 2025-01-28 - Truncating and Dimming Terminal Metadata
**Learning:** Long commit hashes and repetitive static text like '(uninitialized)' create visual noise in terminal lists.
**Action:** Truncate metadata strings (e.g., hashes to 7 chars) and apply dim ANSI styling (\e[2m) to make the core structure easier to scan while preserving essential info.

## 2025-05-15 - Highlighting Dynamic Variables in Setup Scripts
**Learning:** Static log strings in setup scripts become much easier to read when dynamic variables like file paths, patch names, and package names are highlighted with bold text. Furthermore, Bash `NO_COLOR` compliance should be checked with `[[ -z "${NO_COLOR:-}" ]]` to ensure colors are active when `NO_COLOR` is absent, as opposed to testing for its presence with `-v`.
**Action:** Use an explicit `C_BOLD=\033[1m` sequence (reset with `C_RST`) to highlight variables or paths inside informational outputs, and always ensure `NO_COLOR` logic defaults to enabled colors when the variable is unset.

## 2026-09-28 - Enhancing Shell Action Visibility
**Learning:** Standard text for repetitive actions (e.g., `Activating agv-dispatcher...`) blends together during fast terminal output.
**Action:** Use global color variables (e.g., \e[32m for success, \e[31m for teardown, and \e[1m for variable highlights) combined with clear iconography (▶ for start/enable, ■ for stop/disable) to create an immediate visual hierarchy. Ensure color variables are defined globally and disabled when `[[ -v NO_COLOR ]]` is true.
## 2026-10-02 - Aligning tabular CLI output
**Learning:** Relying on hardcoded space characters to pad command descriptions in CLI help text (`echo "  cmd    desc"`) leads to jagged, hard-to-read output when command lengths vary widely.
**Action:** Use `printf "  %-28s %s\n"` to enforce strict column alignment for lists and command menus, ensuring scannable and visually structured console output.
