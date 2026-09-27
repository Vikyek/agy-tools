import sys

filepath = ".jules/sentinel.md"
with open(filepath, "r") as f:
    content = f.read()

new_entry = """
## 2026-09-27 - Prevent command injection in gh pr commands
**Vulnerability:** A command injection vulnerability existed where `subprocess.run(["gh", "pr", "view", str(number), ...])` and `subprocess.run(["gh", "pr", "merge", str(number), ...])` allowed option injection if a PR number/branch string started with a dash.
**Learning:** `gh` and other CLI tools can interpret arguments that start with `-` as options rather than positional arguments.
**Prevention:** Always use `--` in subprocess calls to explicitly denote the end of options and the beginning of positional arguments (e.g. `subprocess.run(["gh", "pr", "view", "--json", "comments,reviews", "--", str(number)])`).
"""

if "2026-09-27" not in content:
    with open(filepath, "a") as f:
        f.write(new_entry)
