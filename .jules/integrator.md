## 2026-09-27 - Remove explicit patch logic for submodules
**Learning:** Cluttery patch files applied to submodules are difficult to maintain, conflict easily with upstream changes, and create synchronization bugs across components.
**Action:** When updating a metapackage, avoid writing `.patch` files. Instead, branch and commit necessary fixes directly within the submodule's repository (if possible), advance the submodule pointer to the latest commit, and remove obsolete patching logic from setup scripts.
