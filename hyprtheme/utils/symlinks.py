import os
import click

# todo


class Symlinks:
    def __init__(self, src, dst):
        self.src: str = src
        self.dst: str = dst

    def set_dst(self, value: str):
        self.dst = value

    def link(self) -> None:
        try:
            os.symlink(self.src, self.dst)
        except OSError as e:
            click.echo(f"An unexpected error has occured: {e}")

    def unlink(self) -> None:
        try:
            os.unlink(self.src)
        except OSError as e:
            click.echo(f"An unexpected error has occured: {e}")
