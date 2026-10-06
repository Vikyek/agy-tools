## 2024-05-24 - Add explicit interaction & cancel hints in TUI
**Learning:** TUI interfaces need explicit action indicators (like how to cancel a prompt or how to interact with an item) as discoverability is lower than web UI.
**Action:** Always include explicitly how to use inputs when building TUI flows.
## 2026-10-06 - Adding Meaningful Color to Bash Utilities
**Learning:** Enhancing bash output with colors using semantic mapping (green for enable, red for disable) accompanied by clear unicode icons helps quickly indicate script state transitions without breaking functionality.
**Action:** Use specific color logic matching terminal UI updates alongside the standard NO_COLOR evaluation.
## 2026-10-06 - Consistent Help Menu Formatting
**Learning:** Space-aligned shell echo statements for help menus often break and result in jagged output when new commands are added.
**Action:** Use printf statements with width formatting instead of space-aligned echoes for more robust and maintainable help menus.
