## 2026-09-06 - Dynamic Curses Layouts and Vim Keybindings
**Learning:** Hardcoded coordinates in terminal UIs (like curses) can lead to visual bugs or misaligned cursors when input data lengths vary. Additionally, users expect standard terminal keybindings (like j/k for navigation) in TUI applications.
**Action:** Always calculate dynamic coordinates based on text lengths in curses applications and map standard terminal navigation keys alongside arrow keys.

## 2024-05-20 - Permanent Keyboard Shortcuts for TUI
**Learning:** In a curses-based TUI, ephemeral status messages can overwrite keyboard shortcut instructions, leaving the user without guidance.
**Action:** Always reserve a dedicated, persistent bottom row for core keyboard shortcuts so they are never obscured by temporary status updates.

## 2026-09-08 - Respecting NO_COLOR Standard in CLI
**Learning:** Terminal utilities that use ANSI escape codes for semantic formatting (like green for enabled, red for disabled) must provide a way to disable color output. This ensures accessibility for users with color vision deficiency or environments that don't support color rendering.
**Action:** Always check the `NO_COLOR` environment variable before applying ANSI escape codes in CLI tools.

## 2025-05-18 - Truncate Long Hashes for Visual Hierarchy
**Learning:** Terminal outputs displaying full 40-character commit hashes next to module statuses create unnecessary visual noise and distract from the actual status. Truncating the hashes and dimming them reduces visual noise and improves the visual hierarchy.
**Action:** When printing long metadata strings (like commit hashes) in terminal lists, truncate them (e.g., to 7 characters) and use dim ANSI coloring (\e[2m) to reduce visual noise.
