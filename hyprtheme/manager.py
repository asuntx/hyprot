import os
from typing import List, Optional
import click

from hyprtheme.setup import hyprtheme_path
from hyprtheme.utils.dirs import DirManager
from hyprtheme.utils.symlinks import Symlinks


class ThemeManager:
    def __init__(self):
        self.theme_name: Optional[str] = ""

    def set_theme_name(self, value: str):
        self.theme_name = value
        self.theme_folder: str = os.path.join(hyprtheme_path, self.theme_name)
        self.dirs = DirManager(self.theme_name)

    # todo
    def add_dot_file(self, dot_file) -> None:
        click.echo(dot_file)
        self.dirs.scan()

    def list_themes(self) -> None:
        try:
            themes: List[str] = [
                f.path for f in os.scandir(hyprtheme_path) if f.is_dir()
            ]
        except FileNotFoundError:
            click.echo("hyprtheme directory not found, run 'hyprtheme init' to fix it")
        except OSError as e:
            click.echo(f"An unexpected OS error occured: {e}")
        else:
            if themes is None or themes == []:
                click.echo(
                    "You don't have themes! create one with 'hyprtheme create {theme}'"
                )
            else:
                for t in themes:
                    click.echo(t)

    # todo
    def set_theme(self) -> None:
        try:
            conf_dirs: List[str] = [
                f.path for f in os.scandir(self.theme_folder) if f.is_dir()
            ]
        except FileNotFoundError:
            click.echo("hyprtheme directory not found, run 'hyprtheme init' to fix it")
        except OSError as e:
            click.echo(f"An unexpected OS error occured: {e}")
        else:
            for dir in conf_dirs:
                click.echo(dir)
        click.echo(f"{self.theme_name} has been set")

    # todo
    def sync_themes(self) -> None:
        """syncs all hyprtheme themes to available conf_files from user"""
        try:
            themes: List[str] = [
                f.path for f in os.scandir(hyprtheme_path) if f.is_dir()
            ]
        except FileNotFoundError:
            click.echo("hyprtheme directory not found run 'hyprtheme init' to fix it")
        except OSError as e:
            click.echo(f"An unexpected OS error occurred: {e}")

    # todo
    def create_theme(self) -> None:
        ask_clone = click.confirm(
            "Do you wanna copy all yours dot files to this theme?"
        )
        if ask_clone:
            click.echo("done")

        else:
            click.echo(
                f"{self.theme_name} has been created in {self.theme_folder}\nYou can add your dots later with 'hyprtheme add theme_name kitty' for example."
            )

    def rename_theme(self, new_theme_folder_name) -> None:
        new_theme_folder_path = os.path.join(hyprtheme_path, new_theme_folder_name)
        self.dirs.rename(self.theme_name, new_theme_folder_path)

    def delete_theme(self) -> None:
        self.dirs.delete(self.theme_name)
