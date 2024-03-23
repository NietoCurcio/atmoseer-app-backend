import os
import sys
from pathlib import Path

class PathHelper:
    def __init__(self) -> None:
        self.repo_name = 'atmoseer-app-backend'

    def get_current_workdir(self) -> Path:
        current_workdir = Path.cwd()
        if not current_workdir.name == self.repo_name:
            raise FileNotFoundError(f"Current working directory is not {self.repo_name}: {current_workdir}")
        return current_workdir.resolve()
    
    def set_wordkir(self, workdir: str):
        built_workdir = self._build_workdir(workdir)
        os.chdir(built_workdir)
    
    def build_workdir(self, workdir: str) -> Path:
        current_workdir = self.get_current_workdir()
        target_dir = current_workdir / workdir
        if not target_dir.exists():
            raise FileNotFoundError(f"Path {target_dir} does not exist")
        return target_dir.resolve()
    
    def add_path_in_sys_path(self, path: Path):
        sys.path.append(str(path))

path_helper = PathHelper()
