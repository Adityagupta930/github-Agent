import subprocess
import os
from datetime import datetime

README = "README.md"
TOKEN = os.environ.get("GITHUB_TOKEN")
USERNAME = os.environ.get("GITHUB_USERNAME")

if not TOKEN or not USERNAME:
    print("❌ GITHUB_TOKEN aur GITHUB_USERNAME environment variables set karo")
    exit(1)

# Remote URL me token inject karo
result = subprocess.run(["git", "remote", "get-url", "origin"], capture_output=True, text=True)
original_url = result.stdout.strip()

# https://github.com/user/repo.git → https://token@github.com/user/repo.git
auth_url = original_url.replace("https://", f"https://{USERNAME}:{TOKEN}@")
subprocess.run(["git", "remote", "set-url", "origin", auth_url])

# README me ek newline add karo
with open(README, "a") as f:
    f.write("\n")

# Git commit aur push
date_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
subprocess.run(["git", "add", README])
subprocess.run(["git", "commit", "-m", f"daily commit: {date_str}"])
subprocess.run(["git", "push"])

# URL wapas original kar do (security ke liye)
subprocess.run(["git", "remote", "set-url", "origin", original_url])

print(f"Commit ho gaya: {date_str}")
