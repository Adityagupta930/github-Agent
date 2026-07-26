import os

README_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "README.md")

def append_newline():
    with open(README_PATH, "a") as f:
        f.write("\n")
