import os
import click
import subprocess


class Rsync:
    def sync(self, src: str, dst: str) -> bool:
        try:
            subprocess.run(["rsync", "-a", "--delete", src, dst], check=True)
        except OSError as e:
            click.echo(f"An unexpected error has occured: {e}")
            return False
        else:
            return True

    def unlink(self, path: str) -> bool:
        try:
            os.unlink(path)
        except OSError as e:
            click.echo(f"An unexpected error has occured: {e}")
            return False
        else:
            return True
