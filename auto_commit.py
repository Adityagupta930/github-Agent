import os
import sys
from datetime import datetime
from file_handler import append_newline
from git_handler import commit_and_push

README = "README.md"

try:
    append_newline()

    date_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    commit_and_push(README, f"daily commit: {date_str}")
except Exception as error:
    print(f"Commit/push failed: {error}", file=sys.stderr)
    raise SystemExit(1) from error

print(f"Commit aur push successful: {date_str}")
