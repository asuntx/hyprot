import os
import click
from hyprtheme.utils.paths import XDG_CONFIG_HOME


class Symlinks:
    def __init__(self, dst: str):
        self.dst = dst
        self.basename: str = os.path.basename(dst)
        self.src: str = os.path.join(XDG_CONFIG_HOME, dst)

    def link(self) -> None:
        try:
            os.symlink(self.dst, self.src)
        except OSError as e:
            click.echo(f"An unexpected error has occured: {e}")

    def unlink(self) -> None:
        try:
            os.unlink(self.dst)
        except OSError as e:
            click.echo(f"An unexpected error has occured: {e}")
