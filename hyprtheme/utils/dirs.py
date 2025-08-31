import click
import os
import shutil
from hyprtheme.utils.paths import HYPERTHEME_PATH
from typing import Iterable
class DirManager:
    def __init__(self, src):
        self.src: str = os.path.join(HYPERTHEME_PATH, src)
        self.src_basename: str = src

    def create(self, src: str) -> bool:
        try:
            os.mkdir(src)
        except OSError as e:
            click.echo(f"An unexpected OS error has occured: {e}")
            return False
        else:
            return True

    def copy(self, src: str, dst: str) -> bool:
        try:
            shutil.copytree(src, dst)
        except FileExistsError:
            click.echo(f"{src} already exists")
            return False
        except OSError as e:
            click.echo(f"An unexpected OS error occured: {e}")
            return False
        else:
            return True

    def delete(self, src: str) -> bool:
        try:
            shutil.rmtree(src)
        except OSError as e:
            click.echo(f"An unexpected OS error occured: {e}")
            return False
        else:
            return True

    def rename(self, new_name: str) -> bool:
        try:
            os.rename(self.src, new_name)
        except OSError as e:
            click.echo(f"An unexpected OS error occured {e}")
            return False
        else:
            return True

    def scan(self) -> None | Iterable:
        if not os.path.exists(self.src):
            click.echo(f"{self.src} doesn't exist")
            return
        try:
            files = os.scandir(self.src)
        except FileNotFoundError:
            click.echo(f"{self.src_basename} not found")
        except OSError as e:
            click.echo(f"An unexpected OS error occured {e}")
        else:
            return files
