import subprocess
import shutil

GIT = shutil.which("git")

if GIT is None:
    raise RuntimeError("Git executable nahi mila; Git install/PATH check karo")

def commit_and_push(filename, message):
    subprocess.run([GIT, "add", filename], check=True)
    subprocess.run([GIT, "commit", "-m", message], check=True)
    subprocess.run([GIT, "push"], check=True)
