import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def append_newline(filepath):

    safe_path = os.path.realpath(os.path.join(BASE_DIR, filepath))
    if not safe_path.startswith(BASE_DIR):
        raise ValueError("Invalid file path")
    with open(safe_path, "a") as f:
        f.write("\n")








