import os
import sys

PATHS = [
    "atmoseer",
    os.path.join("atmoseer", "src"),
]


def configure_paths(paths: list[str]):
    for path in paths:
        try:
            current_workdir = os.getcwd()
            path_to_add = os.path.join(current_workdir, path)
            if not os.path.exists(path_to_add):
                raise FileNotFoundError(
                    f"Path {path_to_add} does not exist. Make sure to initialize {path} submodule"
                )
            sys.path.append(path_to_add)
        except Exception as e:
            print(f"Error adding {path} to sys.path: {e}")
            exit(1)


configure_paths(PATHS)
