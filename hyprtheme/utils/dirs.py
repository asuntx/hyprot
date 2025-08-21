import click
import os
import shutil
from hyprtheme.setup import hyprtheme_path


class DirManager:
    def __init__(self, src):
        self.src: str = os.path.join(hyprtheme_path, src)
        self.src_basename: str = src

    def copy(self, dst: str) -> None:
        try:
            shutil.copy(self.src, dst)
        except OSError as e:
            click.echo(f"An unexpected OS error occured {e}")

    def delete(self, str) -> None:
        try:
            shutil.rmtree(self.src)
        except FileNotFoundError:
            click.echo(f"{self.src_basename} not found!")
        except OSError as e:
            click.echo(f"An unexpected OS error occured {e}")
        else:
            click.echo(f"{self.src_basename} deleted succesfully")

    def rename(self, new_name: str) -> None:
        try:
            os.rename(self.src, new_name)
        except OSError as e:
            click.echo(f"An unexpected OS error occured {e}")

    def scan(self):
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
