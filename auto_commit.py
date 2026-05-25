import os
from datetime import datetime
from file_handler import append_newline
from git_handler import get_remote_url, set_remote_url, commit_and_push

README = "README.md"
TOKEN = os.environ.get("GITHUB_TOKEN")
USERNAME = os.environ.get("GITHUB_USERNAME")

if not TOKEN or not USERNAME:
    print("GITHUB_TOKEN aur GITHUB_USERNAME environment variables set karo")
    exit(1)

original_url = get_remote_url()
auth_url = original_url.replace("https://", f"https://{USERNAME}:{TOKEN}@")
set_remote_url(auth_url)

append_newline(README)

date_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
commit_and_push(README, f"daily commit: {date_str}")

set_remote_url(original_url)
print(f"Commit ho gaya: {date_str}")
