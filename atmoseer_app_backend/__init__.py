import sys
import os

PATHS = [
    'atmoseer',
    'atmoseer/src'
]

def configure_paths(paths: list[str]):
    for path in paths:
        try:
            current_workdir = os.getcwd()
            path_to_add = os.path.join(current_workdir, path)
            sys.path.append(path_to_add)
        except Exception as e:
            print(f"Error adding {path} to sys.path: {e}")

configure_paths(PATHS)
