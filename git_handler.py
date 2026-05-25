import subprocess
import shutil

GIT = shutil.which("git")  # full path resolve karo

def get_remote_url():
    result = subprocess.run([GIT, "remote", "get-url", "origin"], capture_output=True, text=True)
    return result.stdout.strip()

def set_remote_url(url):
    subprocess.run([GIT, "remote", "set-url", "origin", url])

def commit_and_push(filename, message):
    subprocess.run([GIT, "add", filename])
    subprocess.run([GIT, "commit", "-m", message])
    subprocess.run([GIT, "push"])
