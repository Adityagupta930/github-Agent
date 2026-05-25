import subprocess

def get_remote_url():
    result = subprocess.run(["git", "remote", "get-url", "origin"], capture_output=True, text=True)
    return result.stdout.strip()

def set_remote_url(url):
    subprocess.run(["git", "remote", "set-url", "origin", url])

def commit_and_push(filename, message):
    subprocess.run(["git", "add", filename])
    subprocess.run(["git", "commit", "-m", message])
    subprocess.run(["git", "push"])
