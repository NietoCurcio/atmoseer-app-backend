from app.helpers.PathHelper import path_helper

ATMOSEER_PATHS = ['atmoseer', 'atmoseer/src']

def _add_paths_to_sys_path(paths: list[str]):
    for path in paths:
        try:
            current_workdir = path_helper.get_current_workdir()
            path_helper.add_path_in_sys_path(current_workdir / path)
        except Exception as e:
            print(f"Error adding {path} to sys.path: {e}")

def configure_atmoseer_paths():
    _add_paths_to_sys_path(ATMOSEER_PATHS)

configure_atmoseer_paths()
